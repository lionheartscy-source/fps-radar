#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FPS레이더 리포트 문장 검사기.

사용법:
    python3 tools/check_prose.py reports/2026-09/FPS레이더_2026-09-02.html

리포트 HTML에서 '산문 영역'만 뽑아 문장 단위로 검사한다.
검사 항목은 2026-09-02에 사용자가 지적한 문제들에서 그대로 나왔다.

  1. 줄표(—)로 문장 잇기
  2. 인접한 두 문장이 같은 낱말을 반복 (예: "몰릴 구간입니다" → "몰립니다")
  3. 모호한 명사 (구간·지점·부분·측면·차원 …)
  4. 명사구로 끝나 서술어가 없는 문장 (예: "출시 2일차.", "오늘의 조치.")
  5. 단위 없는 괄호 숫자 (예: "…죽였다"(52) → 댓글 52개)
  6. 문장이 70자를 넘음
  7. 표 반응 칸에 ①②③ 번호가 없음
  8. 섹션별·전체 글자 수 상한 초과

종료 코드 0이면 통과, 1이면 고칠 것이 남았다는 뜻이다.
"""
import re
import sys
from statistics import mean

# ── 상한 ──────────────────────────────────────────────
BODY_MAX = 12900
SECTION_MAX = {
    'lead+notice+kpi': 750, '01 일정': 1150, '02 헤드라인': 800,
    '03 국내': 2250, '04 글로벌': 2600, '05 신작': 1450,
    '06 리스크': 2300, '07 액션': 600, 'caveat': 500, '08 출처': 1150,
}
SENT_MAX = 70          # 인용문이 든 문장은 예외
SENT_AVG_MAX = 38
VAGUE = ['구간', '지점', '부분', '측면', '차원', '여진', '방아쇠', '거점',
         '논지', '비교치', '실무 포인트', '격상']
# 인접 중복 검사에서 무시할 흔한 낱말
COMMON = {'입니다', '있습니다', '합니다', '없습니다', '했습니다', '됐습니다',
          '오늘', '어제', '그리고', '하지만', '때문', '이번', '다음'}


def strip_tags(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()


def split_sents(t):
    parts = re.split(r'(?<=다\.)\s|(?<=요\.)\s|(?<=\.)\s(?=[가-힣①-③"])', t)
    return [p.strip() for p in parts if len(p.strip()) > 3]


def collect(html):
    """(라벨, 원문HTML) 목록으로 산문 영역만 모은다."""
    out = []
    for anchor, name in [('id="kr"', '03'), ('id="gl"', '04')]:
        if anchor not in html:
            continue
        i = html.index(anchor)
        seg = html[i:html.index('</table>', i)]
        for row in re.findall(r'<tr>(.*?)</tr>', seg, re.S):
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if len(tds) < 5:
                continue
            g = re.search(r'g-name">([^<]*)', row)
            g = g.group(1)[:10] if g else '?'
            cell = re.sub(r'<span class="src-inline">.*?</span>', '', tds[4], flags=re.S)
            cell = re.sub(r'<span class="evrow">.*?</span>', '', cell, flags=re.S)
            out.append((f'{name}·{g}·2열', tds[1]))
            out.append((f'{name}·{g}·반응', cell))
    m = re.search(r'<p class="lead">(.*?)</p>', html, re.S)
    if m:
        out.append(('lead', m.group(1)))
    for tag, label in [('under', '02카드'), ('obs', '05관전'), ('lesson', '06교훈')]:
        for i, mm in enumerate(re.finditer(r'<div class="' + tag + r'">(.*?)</div>', html, re.S), 1):
            body = re.sub(r'<span class="evrow">.*?</span>', '', mm.group(1), flags=re.S)
            out.append((f'{label}{i}', body))
    for i, mm in enumerate(re.finditer(
            r'<div class="row"><span class="k">([^<]*)</span><span>(.*?)</span></div>', html, re.S), 1):
        out.append((f'06{mm.group(1)}{i}', mm.group(2)))
    for i, mm in enumerate(re.finditer(r'<article class="act">.*?<p>(.*?)</p>', html, re.S), 1):
        out.append((f'07액션{i}', mm.group(1)))
    m = re.search(r'<div class="caveat">(.*?)</div>', html, re.S)
    if m:
        out.append(('caveat', m.group(1)))
    return out


def section_lengths(html):
    body = html[html.index('<main id="main">'):html.index('</main>')]
    marks = [('lead+notice+kpi', '<p class="lead">', '<div class="sec" id="today">'),
             ('01 일정', '<div class="sec" id="today">', '<div class="sec" id="headline">'),
             ('02 헤드라인', '<div class="sec" id="headline">', '<div class="sec" id="kr">'),
             ('03 국내', '<div class="sec" id="kr">', '<div class="sec" id="gl">'),
             ('04 글로벌', '<div class="sec" id="gl">', '<div class="sec" id="trend">'),
             ('05 신작', '<div class="sec" id="trend">', '<div class="sec" id="risk">'),
             ('06 리스크', '<div class="sec" id="risk">', '<div class="sec" id="action">'),
             ('07 액션', '<div class="sec" id="action">', '<div class="caveat">'),
             ('caveat', '<div class="caveat">', '<details class="sources"'),
             ('08 출처', '<details class="sources"', '</details>')]
    res = {}
    for name, a, z in marks:
        if a not in body:
            continue
        seg = body[body.index(a):body.index(z)] if z in body else body[body.index(a):]
        res[name] = len(strip_tags(seg))
    return len(strip_tags(body)), res


def main(path):
    html = open(path, encoding='utf-8').read()
    problems = []
    lens = []

    for label, raw in collect(html):
        text = strip_tags(raw)
        sents = split_sents(text)
        lens += [len(x) for x in sents]

        if '—' in text:
            problems.append((label, '줄표로 문장을 이었습니다', text[:60]))

        stems = [set(w for w in re.findall(r'[가-힣]{2,}', x) if w not in COMMON) for x in sents]
        for i in range(len(sents) - 1):
            # 인용문 안의 낱말은 제외
            q = set(re.findall(r'[가-힣]{2,}', ''.join(re.findall(r'"([^"]*)"', sents[i] + sents[i + 1]))))
            dup = (stems[i] & stems[i + 1]) - q
            if dup:
                problems.append((label, f'인접 문장 낱말 반복 {sorted(dup)}',
                                 f'{sents[i][:32]} || {sents[i+1][:32]}'))

        for w in VAGUE:
            if w in text:
                problems.append((label, f'모호한 낱말 "{w}"', text[max(0, text.find(w) - 25):text.find(w) + 25]))

        for x in sents:
            # ①②③ 열거 항목과 인용문은 명사구로 끝나도 자연스럽다
            listish = bool(re.match(r'^[①②③④]', x)) or '"' in x
            core = x.rstrip('. ')
            if not listish and core and not re.search(r'(다|요|까|오|죠|셈|것)$', core) and len(core) < 30:
                problems.append((label, '서술어 없이 명사구로 끝났습니다', x))
            if len(x) > SENT_MAX and not listish:
                problems.append((label, f'문장이 {len(x)}자로 깁니다', x[:70]))

        for mm in re.finditer(r'"\s*\(\s*[0-9,]+\s*\)', text):
            problems.append((label, '괄호 숫자에 단위가 없습니다', text[max(0, mm.start() - 30):mm.end() + 10]))

    # 표 반응 칸 번호
    for anchor, name in [('id="kr"', '03'), ('id="gl"', '04')]:
        if anchor not in html:
            continue
        i = html.index(anchor)
        seg = html[i:html.index('</table>', i)]
        for row in re.findall(r'<tr>(.*?)</tr>', seg, re.S):
            tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if len(tds) < 5:
                continue
            n = len(re.findall(r'[①②③④]', tds[4]))
            g = re.search(r'g-name">([^<]*)', row)
            g = g.group(1)[:10] if g else '?'
            if n == 0:
                problems.append((f'{name}·{g}', '반응 칸에 ①②③ 번호가 없습니다', ''))
            elif n > 3:
                problems.append((f'{name}·{g}', f'번호가 {n}개입니다(3개 이하)', ''))

    total, secs = section_lengths(html)
    if total > BODY_MAX:
        problems.append(('본문', f'{total}자 (상한 {BODY_MAX})', ''))
    for k, v in secs.items():
        cap = SECTION_MAX.get(k)
        if cap and v > cap:
            problems.append((k, f'{v}자 (상한 {cap})', ''))

    avg = round(mean(lens)) if lens else 0
    if avg > SENT_AVG_MAX:
        problems.append(('산문 전체', f'평균 문장 {avg}자 (상한 {SENT_AVG_MAX})', ''))

    print(f'본문 {total}자 · 산문 {len(lens)}문장 · 평균 {avg}자')
    for k, v in secs.items():
        cap = SECTION_MAX.get(k, 0)
        print(f'  {k:16s} {v:5d}자' + (f'  ⚠ 상한 {cap}' if cap and v > cap else ''))
    if not problems:
        print('\n✅ 지적 사항 없음')
        return 0
    print(f'\n❌ 고칠 것 {len(problems)}건')
    for label, kind, ctx in problems:
        print(f'  [{label}] {kind}')
        if ctx:
            print(f'      {ctx}')
    return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('사용법: python3 tools/check_prose.py <리포트.html>')
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
