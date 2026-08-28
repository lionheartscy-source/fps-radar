#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGDB 동기화 스크립트 — FPS레이더

하는 일
  1) Twitch OAuth 토큰 발급(캐시해서 만료 전까지 재사용)
  2) 추적 대상 게임의 커버/아트워크 이미지ID + 메타데이터 조회
     -> assets/igdb_cache.json
  3) 향후 N일 내 출시 예정인 슈터 신작 목록 조회
     -> assets/igdb_upcoming.json

실행: python tools/igdb_sync.py       (또는 igdb_sync.bat 더블클릭)

설정: tools/igdb_config.json  (git에 올라가지 않음)
  {
    "client_id": "...",
    "client_secret": "...",
    "upcoming_days": 60
  }

IGDB 이미지 주소 규칙 (핫링크 허용):
  https://images.igdb.com/igdb/image/upload/t_<size>/<image_id>.jpg
  size: t_thumb / t_cover_small / t_cover_big / t_screenshot_med
        t_screenshot_big / t_screenshot_huge / t_720p / t_1080p
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "tools", "igdb_config.json")
TOKEN_PATH = os.path.join(ROOT, "tools", ".igdb_token.json")
CACHE_PATH = os.path.join(ROOT, "assets", "igdb_cache.json")
UPCOMING_PATH = os.path.join(ROOT, "assets", "igdb_upcoming.json")

IMG = "https://images.igdb.com/igdb/image/upload/t_{size}/{iid}.jpg"

# ── 추적 대상: "리포트에서 쓰는 한글명": "IGDB 검색어"
TRACKED = {
    "발로란트": "Valorant",
    "오버워치2": "Overwatch 2",
    "에이펙스 레전드": "Apex Legends",
    "콜오브듀티: MW4": "Call of Duty: Modern Warfare 4",
    "Counter-Strike 2": "Counter-Strike 2",
    "레인보우 식스 시즈": "Tom Clancy's Rainbow Six Siege",
    "배틀필드 6": "Battlefield 6",
    "데스티니 2": "Destiny 2",
    "마블 라이벌즈": "Marvel Rivals",
    "델타 포스": "Delta Force",
    "THE FINALS": "The Finals",
    "배틀그라운드(PUBG)": "PUBG: Battlegrounds",
    "서든어택": "Sudden Attack",
    "타임 테이커즈": "Time Takers",
}

# IGDB 장르/테마 ID — 5: Shooter, 4: Fighting 제외 등
GENRE_SHOOTER = 5
# 플랫폼 — 6: PC(Windows), 48: PS4, 167: PS5, 49: Xbox One, 169: Xbox Series
PLATFORMS = [6, 48, 167, 49, 169]


def log(msg):
    print(msg, flush=True)


def die(msg, code=1):
    log("\n[오류] %s\n" % msg)
    sys.exit(code)


def load_config():
    if not os.path.exists(CONFIG_PATH):
        die(
            "설정 파일이 없습니다: tools\\igdb_config.json\n"
            "        tools\\igdb_config.example.json 을 복사해 이름을 igdb_config.json 으로 바꾸고\n"
            "        Twitch 개발자 콘솔의 Client ID / Client Secret 을 채워 넣으세요."
        )
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    for k in ("client_id", "client_secret"):
        if not cfg.get(k) or cfg[k].startswith("여기에"):
            die("igdb_config.json 의 %s 값이 비어 있습니다." % k)
    cfg.setdefault("upcoming_days", 60)
    return cfg


def get_token(cfg):
    """토큰을 캐시에서 재사용하고, 만료가 임박하면 새로 발급."""
    if os.path.exists(TOKEN_PATH):
        try:
            with open(TOKEN_PATH, encoding="utf-8") as f:
                tok = json.load(f)
            # 만료 1일 전까지만 재사용
            if tok.get("expires_at", 0) - time.time() > 86400:
                log("  토큰: 캐시 재사용 (만료 %s)"
                    % time.strftime("%Y-%m-%d", time.localtime(tok["expires_at"])))
                return tok["access_token"]
        except Exception:
            pass

    log("  토큰: 새로 발급 중...")
    body = urllib.parse.urlencode({
        "client_id": cfg["client_id"],
        "client_secret": cfg["client_secret"],
        "grant_type": "client_credentials",
    }).encode()
    req = urllib.request.Request("https://id.twitch.tv/oauth2/token", data=body, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        die("토큰 발급 실패 (HTTP %s). Client ID/Secret 을 확인하세요.\n        %s"
            % (e.code, e.read().decode("utf-8", "replace")[:300]))
    except Exception as e:
        die("토큰 발급 중 네트워크 오류: %s" % e)

    d["expires_at"] = time.time() + d.get("expires_in", 0)
    with open(TOKEN_PATH, "w", encoding="utf-8") as f:
        json.dump(d, f)
    log("  토큰: 발급 완료 (만료 %s)"
        % time.strftime("%Y-%m-%d", time.localtime(d["expires_at"])))
    return d["access_token"]


def igdb(endpoint, query, cfg, token, _retry=True):
    """IGDB APIv4 호출. 초당 4요청 제한이 있어 호출마다 살짝 쉼."""
    req = urllib.request.Request(
        "https://api.igdb.com/v4/%s" % endpoint,
        data=query.encode("utf-8"),
        headers={
            "Client-ID": cfg["client_id"],
            "Authorization": "Bearer %s" % token,
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            out = json.load(r)
        time.sleep(0.28)  # 4 req/sec 제한 준수
        return out
    except urllib.error.HTTPError as e:
        if e.code == 401 and _retry:
            # 토큰 만료 -> 캐시 삭제 후 1회 재시도
            if os.path.exists(TOKEN_PATH):
                os.remove(TOKEN_PATH)
            return igdb(endpoint, query, cfg, get_token(cfg), _retry=False)
        if e.code == 429:
            time.sleep(2)
            if _retry:
                return igdb(endpoint, query, cfg, token, _retry=False)
        log("  [경고] %s 호출 실패 (HTTP %s): %s"
            % (endpoint, e.code, e.read().decode("utf-8", "replace")[:200]))
        return []
    except Exception as e:
        log("  [경고] %s 호출 중 오류: %s" % (endpoint, e))
        return []


def esc(s):
    return s.replace('"', '\\"')


def pick_best(results, want):
    """검색 결과 중 이름이 가장 가까운 것을 고른다."""
    if not results:
        return None
    w = want.lower()
    for r in results:
        if r.get("name", "").lower() == w:
            return r
    for r in results:
        if w in r.get("name", "").lower():
            return r
    return results[0]


def sync_games(cfg, token):
    log("\n[1/2] 게임 커버·아트워크 조회 (%d종)" % len(TRACKED))
    games = {}
    for ko, en in TRACKED.items():
        q = ('search "%s"; '
             'fields name,slug,cover.image_id,artworks.image_id,screenshots.image_id,'
             'first_release_date,genres.name,involved_companies.company.name,url; '
             'limit 8;' % esc(en))
        best = pick_best(igdb("games", q, cfg, token), en)
        if not best:
            log("  - %-18s 검색 결과 없음" % ko)
            games[ko] = {"igdb_id": None, "메모": "IGDB 검색 실패"}
            continue

        cover = (best.get("cover") or {}).get("image_id")
        arts = [a["image_id"] for a in best.get("artworks", []) if a.get("image_id")]
        shots = [s["image_id"] for s in best.get("screenshots", []) if s.get("image_id")]
        # 리포트 타일은 가로형이 어울리므로 아트워크 > 스크린샷 > 커버 순으로 대표 이미지 선정
        banner_id = (arts[0] if arts else (shots[0] if shots else cover))

        games[ko] = {
            "igdb_id": best.get("id"),
            "igdb_name": best.get("name"),
            "igdb_url": best.get("url"),
            "cover_image_id": cover,
            "banner_image_id": banner_id,
            "banner_url": IMG.format(size="720p", iid=banner_id) if banner_id else None,
            "cover_url": IMG.format(size="cover_big", iid=cover) if cover else None,
            "artworks": arts[:5],
            "screenshots": shots[:5],
            "genres": [g["name"] for g in best.get("genres", [])],
            "companies": [c["company"]["name"] for c in best.get("involved_companies", [])
                          if c.get("company")][:3],
        }
        mark = "OK " if banner_id else "이미지없음"
        log("  - %-18s %s  %s" % (ko, mark, best.get("name", "")))
    return games


def sync_upcoming(cfg, token, days):
    log("\n[2/2] 향후 %d일 슈터 신작 조회" % days)
    now = int(time.time())
    until = now + days * 86400
    q = ('fields game.name,game.slug,game.cover.image_id,game.url,date,platform.name,'
         'human,region; '
         'where date > %d & date < %d '
         '& game.genres = (%d) '
         '& platform = (%s) '
         '& game.version_parent = null; '
         'sort date asc; limit 60;'
         % (now, until, GENRE_SHOOTER, ",".join(str(p) for p in PLATFORMS)))
    rows = igdb("release_dates", q, cfg, token)

    seen, out = set(), []
    for r in rows:
        g = r.get("game") or {}
        gid = g.get("id")
        if not gid or gid in seen:
            continue
        seen.add(gid)
        cid = (g.get("cover") or {}).get("image_id")
        out.append({
            "name": g.get("name"),
            "date": time.strftime("%Y-%m-%d", time.localtime(r["date"])),
            "human": r.get("human"),
            "platform": (r.get("platform") or {}).get("name"),
            "igdb_url": g.get("url"),
            "cover_url": IMG.format(size="cover_big", iid=cid) if cid else None,
            "banner_url": IMG.format(size="720p", iid=cid) if cid else None,
        })
    out.sort(key=lambda x: x["date"])
    log("  - %d건 수집" % len(out))
    for r in out[:8]:
        log("      %s  %s" % (r["date"], r["name"]))
    if len(out) > 8:
        log("      ... 외 %d건" % (len(out) - 8))
    return out


def main():
    log("=" * 56)
    log(" IGDB 동기화 — FPS레이더")
    log("=" * 56)
    cfg = load_config()
    token = get_token(cfg)

    games = sync_games(cfg, token)
    upcoming = sync_upcoming(cfg, token, cfg["upcoming_days"])

    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "_생성시각": stamp,
            "_출처": "IGDB (api.igdb.com/v4) · 이미지는 images.igdb.com 핫링크 허용",
            "_이미지주소규칙": "https://images.igdb.com/igdb/image/upload/t_<size>/<image_id>.jpg "
                              "(size: thumb/cover_small/cover_big/screenshot_med/screenshot_big/"
                              "screenshot_huge/720p/1080p)",
            "_사용법": "리포트 썸네일은 banner_url 을 우선 사용. 없으면 cover_url.",
            "games": games,
        }, f, ensure_ascii=False, indent=2)
    log("\n저장: assets/igdb_cache.json")

    with open(UPCOMING_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "_생성시각": stamp,
            "_범위": "향후 %d일 · 장르=Shooter · PC/PS/Xbox" % cfg["upcoming_days"],
            "_주의": "IGDB 등록 기준이라 국내 게임·미등록 신작은 빠질 수 있음. 웹 검색으로 보완할 것.",
            "releases": upcoming,
        }, f, ensure_ascii=False, indent=2)
    log("저장: assets/igdb_upcoming.json")

    ok = sum(1 for v in games.values() if v.get("banner_image_id"))
    log("\n완료 — 이미지 확보 %d/%d종, 신작 %d건" % (ok, len(games), len(upcoming)))
    log("=" * 56)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        die("예상치 못한 오류: %s" % e)
