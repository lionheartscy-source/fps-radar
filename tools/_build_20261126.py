# -*- coding: utf-8 -*-
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREV = os.path.join(ROOT, 'reports/2026-11/FPS레이더_2026-11-25.html')
OUT = os.path.join(ROOT, 'reports/2026-11/FPS레이더_2026-11-26.html')
s = open(PREV, encoding='utf-8').read()
head = s[:s.find('<body')]
tail = s[s.find('</main>'):]
head = head.replace('2026-11-25', '2026-11-26')

T = 'target="_blank" rel="noopener"'
def a(u, t): return f'<a href="{u}" {T}>{t}</a>'
SVG = {
 'pc': '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg>',
 'mail': '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="3.3" width="13" height="9.4" rx="1.4"/><path d="m2.3 4.7 5.7 3.9 5.7-3.9"/></svg>',
}
def lk(u, kind, label): return f'<a href="{u}" {T}>{SVG[kind]}<span>{label}</span></a>'

IMG = {
 'OW': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2357570/26446ff05a359d4942e277f82fd347e89b275be3/header.jpg?t=1786471282',
 'PUBG': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/578080/841ea38bc58cabb70aef65365cf50bc2d79329d9/header.jpg?t=1786493086',
 'WD': 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1867240/24c0b6c0621560e922fbed18545921e7eaa9036e/capsule_616x353.jpg?t=1794420220',
 'EXO': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1286320/capsule_616x353.jpg?t=1795568630',
 'CS2': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/730/162664aa5da85f418105350c5d67ca565f6c3713/header.jpg?t=1784564069',
 'FIN': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2073850/61f55ef49a74c76bf9fda9ec35bc3101eeee2b3e/header.jpg?t=1787220389',
 'DK': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3810510/ecd586ce4f242e46d4febaf9209c3d09d5f9d4c8/capsule_616x353.jpg?t=1794855109',
 'BR': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4434380/e4ae8975f072b3d62f39d692d9750e7338f9b078/capsule_616x353.jpg?t=1795446162',
 'SA': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4823770/3f6f8df34c5f725c7f9a4db5c091f682be2c364b/capsule_616x353.jpg?t=1795626542',
 'G8': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4783980/00b44a553fb18b11352263ba42481d917d8d3910/capsule_616x353.jpg?t=1795452965',
 'HG': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1752080/capsule_616x353.jpg?t=1795644705',
 'CL': 'https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4768180/411a12bf6a84488dfa98243ac44afd670beb3166/capsule_616x353.jpg?t=1793200387',
 'SF2': 'https://cdn.gamemeca.com/gmdata/0001/784/056/gm131633_thumb_2_.webp',
}
def thumb(key, mono, name, cls='thumb'):
    return f'<span class="{cls}" data-mono="{mono}" data-name="{name}"><img src="{IMG[key]}" alt=""></span>'

LB = '<span class="lb"></span>'
def ev(*k):
    lab = {'kr':'KR·기사','gl':'글로벌·기사','cm':'커뮤니티','of':'공식','mt':'지표','na':'국내 반응 미확인'}
    return '<span class="evrow">' + ''.join(f'<span class="ev {x}">{lab[x]}</span>' for x in k) + '</span>'

U = {
 'ow870': 'https://overwatch.nexon.com/news/event/870',
 'inv_ow_440': 'https://www.inven.co.kr/board/overwatch/4538/5941807',
 'inv_ow_std': 'https://www.inven.co.kr/board/overwatch/4538/5941850',
 'inv_ow_bad': 'https://www.inven.co.kr/board/overwatch/4538/5941845',
 'inv_ow': 'https://www.inven.co.kr/board/overwatch/4538',
 'pubg_pol': 'https://pubg.com/ko/news/11411',
 'pubg_ban': 'https://pubg.com/ko/news/11418',
 'inv_pubg': 'https://www.inven.co.kr/board/battlegrounds/5046',
 'pubg_hack': 'https://steamcommunity.com/app/578080/discussions/1/570429562442457714/',
 'wd_cool': 'https://steamcommunity.com/app/1867240/discussions/0/571549822592693063/',
 'wd_ac': 'https://steamcommunity.com/app/1867240/discussions/0/573807613531160057/',
 'wd_wall': 'https://steamcommunity.com/app/1867240/discussions/0/573807531688786942/',
 'wd_cwis': 'https://steamcommunity.com/app/1867240/discussions/0/573807531688794200/',
 'wd_s4': 'https://steamcommunity.com/app/1867240/discussions/0/574932530844862320/',
 'wd_d': 'https://steamcommunity.com/app/1867240/discussions/',
 'wd_store': 'https://store.steampowered.com/app/1867240/?l=koreana',
 'exo_inv': 'https://www.inven.co.kr/webzine/news/?news=323813',
 'exo_off': 'https://steamcommunity.com/app/1286320/discussions/0/573807613531146542/',
 'exo_ref': 'https://steamcommunity.com/app/1286320/discussions/0/573807613531142358/',
 'exo_p2p': 'https://steamcommunity.com/app/1286320/discussions/0/573807613531153857/',
 'exo_save': 'https://steamcommunity.com/app/1286320/discussions/0/573807613531146381/',
 'exo_d': 'https://steamcommunity.com/app/1286320/discussions/',
 'exo_store': 'https://store.steampowered.com/app/1286320/?l=koreana',
 'strafe': 'https://www.strafe.com/news/read/singapore-major-2026-day-2-recap-s1mple-eliminated-as-flyquest-and-nip-advance/',
 'hltv': 'https://www.hltv.org/news/46053/chinggis-warriors-condemn-bcgame-to-0-3-exit-in-singapore',
 'cs_vac': 'https://steamcommunity.com/app/730/discussions/0/563674514368649559/',
 'cs_d': 'https://steamcommunity.com/app/730/discussions/',
 'fin_ch': 'https://steamcommunity.com/app/2073850/discussions/0/571555456253921751/',
 'fin_em': 'https://steamcommunity.com/app/2073850/discussions/0/571555456253770981/',
 'fin_sw': 'https://steamcommunity.com/app/2073850/discussions/0/571555456253795284/',
 'fin_d': 'https://steamcommunity.com/app/2073850/discussions/',
 'api': 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=1867240',
 'st_dk': 'https://store.steampowered.com/app/3810510/?l=koreana',
 'st_br': 'https://store.steampowered.com/app/4434380/?l=koreana',
 'st_sa': 'https://store.steampowered.com/app/4823770/?l=koreana',
 'st_g8': 'https://store.steampowered.com/app/4783980/?l=koreana',
 'st_hg': 'https://store.steampowered.com/app/1752080/?l=koreana',
 'st_cl': 'https://store.steampowered.com/app/4768180/?l=koreana',
 'st_my': 'https://store.steampowered.com/app/3247750/?l=koreana',
 'hg_pr': 'https://www.gamespress.com/HUNGER-Announces-Open-Beta-for-27-November-Ahead-of-Early-Access-Launc',
 'ruli': 'https://bbs.ruliweb.com/',
 'ruli_hg': 'https://bbs.ruliweb.com/game/87435',
 'sf2': 'https://www.gamemeca.com/view.php?gid=1784056',
}

# ───────── 글쓰기 에이전트 원고 ─────────
LEAD = '<span class="lrow hi"><b class="lk">핵심</b><span class="lt"><b>캡콤이 엑조프라이멀 서비스를 2027년 9월 30일 끝냅니다.</b></span></span><span class="lrow"><b class="lk">스팀</b><span class="lt">워독스 동시 접속자가 50,883명으로 늘었습니다.<span class="lb"></span>월핵 불만 글은 37개에서 69개가 됐습니다.</span></span><span class="lrow"><b class="lk">대회</b><span class="lt">s1mple의 BC.Game이 메이저에서 0-3으로 탈락했습니다.<span class="lb"></span>CS2 접속자는 667,694명까지 올랐습니다.</span></span><span class="lrow"><b class="lk">국내</b><span class="lt">크래프톤이 배그 운영정책을 11월 30일부터 바꿉니다.<span class="lb"></span>제재 통보 때 위반 조항과 이의제기하는 법을 알립니다.</span></span><span class="lrow"><b class="lk">방법</b><span class="lt">수치는 오늘 07:34 스팀 Web API와 토론 목록에서 뽑았습니다.<span class="lb"></span>목요일 아침 값을 수요일 아침과 비교했습니다.</span></span>'
UNDER_EXO = '2024년 7월 시즌4 이후로 신규 콘텐츠가 한 번도 나오지 않았습니다.<span class="lb"></span>본편과 DLC 판매는 2027년 3월 31일 10시에 끝나고 재다운로드는 서비스 종료 전까지 됩니다.<span class="lb"></span>스팀 동시 접속자는 16명이며 지난 30일 평가 16개 중 31%만 긍정입니다.<span class="lb"></span><b>토론에서는 "Offline patch"(오프라인 패치) 글에 답글 12개가 달렸습니다.</b>'
UNDER_WD = '워독스 동시 접속은 50,883명으로 어제 48,313명보다 약 5% 늘었습니다.<span class="lb"></span>월핵 불만 글이 하루 새 37개에서 69개로 뛰었고 접속 끊김 글도 최근 3시간 동안 5건입니다.<span class="lb"></span>CWIS를 빼 달라는 요구 글엔 의견 44건이 모였고 어제는 19건이었습니다.<span class="lb"></span><b>9월 22일 "쿨한 개발사라는 착각" 토론은 답글 118개로 26분 전에도 갱신됐습니다.</b>'
UNDER_CS = 'FlyQuest와 NIP가 3-0으로 Stage 2 진출을 가장 먼저 확정했습니다.<span class="lb"></span>Chinggis Warriors는 Nuke 13-10을 포함해 BC.Game을 2-1로 꺾었습니다.<span class="lb"></span>s1mple의 팀은 0-3으로 탈락했고 Strafe는 그의 메이저 15회 중 최악 성적이라고 썼습니다.<span class="lb"></span><b>CS2 동시 접속은 어제 605,277명에서 667,694명으로 올랐습니다.</b>'

OW_D1 = '빠른 대전과 경쟁전만 440분을 쌓으면 D.Va 스킨을 줍니다.'
OW_D2 = '11/25 09시부터 12/9 09시까지 꽃 신령 이벤트가 열립니다.<span class="lb"></span>빠른 대전·경쟁전 플레이 시간만 9단계로 440분을 쌓습니다.<span class="lb"></span>최종 보상은 D.Va 스킨이며 넥슨 PC방은 2배로 인정됩니다.'
OW_R = '<b>① 정리 글</b> 11/24 올라온 넥슨 안내 요약이 <b>1,899회</b> 열렸습니다. 어제 아침에는 880회였고 추천 6개, 답글 7개가 달렸습니다. 본문은 <b>"최소 440분(7시간 20분)을 게임해야함"</b>이라고 적었습니다.<span class="lb"></span><b>② 모드 제외</b> 11/25 23:51 글이 147회 읽히고 의견 3개를 모았습니다. 본문은 <b>"스타디움도 아케이드도 안 된대"</b>라는 내용입니다. 이어서 <b>"빠대랑 경쟁만 된단거네"</b>라고 정리했습니다.<span class="lb"></span><b>③ 체감</b> 11/25 17:04 글 "이번 이벤트 별로다"는 377회 조회됐습니다. 작성자는 1시간을 해도 하나밖에 못 했다고 썼습니다. OWCS 응원 이벤트는 여러 개 쌓였다며 <b>"매우불편"</b>을 꼽았습니다.<span class="lb"></span><b>집계되는 모드와 빠지는 모드를 공지 첫머리에 나란히 적어야 합니다.</b>'
PUBG_D1 = '크래프톤이 11/30부터 새 운영정책을 적용합니다.'
PUBG_D2 = '크래프톤이 11/23 공지로 제재 수위 기준 6가지를 밝혔습니다.<span class="lb"></span>신설 조항에 따라 통보 때 위반 조항과 기간, 이의제기 방법을 알립니다.<span class="lb"></span>개정안은 2026년 11월 30일부터 적용됩니다.'
PUBG_R = '<b>① 국내 반응</b> 인벤 배틀그라운드 전체 목록을 첫 장부터 살폈습니다. 최신 게시물은 11/24 작성분이고 개정을 다룬 것은 <b>0건</b>입니다.<span class="lb"></span><b>② 스팀 토론</b> <b>"Where\'s the hackusations team?"</b> 글에 답글 <b>23개</b>가 달렸습니다. 핵 의심 처리팀이 어디 있느냐는 물음입니다. 어제 17개에서 늘었고 7시간 전에도 갱신됐습니다. 스팀 동시 접속자는 108,846명입니다.<span class="lb"></span><b>③ 제재 현황</b> 11/25 주간 공지에는 11/16~11/22 영구 이용 제한 명단이 붙었습니다. 본문에는 건수를 적지 않았습니다. 그래서 제재 규모를 숫자로 확인할 수 없습니다.<span class="lb"></span><b>통보문에 이의제기 경로를 넣으면 처리팀이 없다는 불신 글에 답할 근거가 생깁니다.</b>'

WD_D1 = '시즌 3 15일째 동시 접속이 5만 명대로 올랐습니다.'
WD_D2 = '오늘 07:34 동시 접속은 50,883명으로 어제보다 약 5% 많습니다.<span class="lb"></span>스팀 상점 지난 30일 평가는 62,090개 중 78%가 긍정입니다.<span class="lb"></span>한국어 리뷰 2,994개로 좁히면 39%만 호의적입니다.'
WD_R = '<b>① 신뢰</b> 개발사를 겨냥한 글에 의견 118개가 붙었습니다. 출시 2주 만에 <b>"cheat infested to the core"(뼛속까지 치트가 들끓는다)</b>고 썼습니다. 치터 조롱 영상이 홍보용이었다는 주장도 담겼습니다.<span class="lb"></span><b>② 제재</b> <b>"Is Anti-cheat working?"(안티치트가 작동하긴 하나)</b>에 38개가 달렸습니다. 월핵 사용자만 돈을 번다는 글도 커졌습니다. 어제 37개였던 댓글은 69개로 불었습니다.<span class="lb"></span><b>③ 끊김</b> <b>"DISCONNECTIION"(접속 끊김)</b>에는 답글 11건이 이어졌습니다. 최근 3시간 사이 연결 문제를 호소한 글은 5건입니다.<span class="lb"></span><b>접속이 반등해도 개발사 불신이 커지면 제재 실적과 끊김 원인을 따로 공지합니다.</b>'
EXO_D1 = '캡콤이 2027년 9월 30일 서비스 종료를 알렸습니다.'
EXO_D2 = '캡콤이 11/25 공식 홈페이지와 SNS로 종료를 공지했습니다.<span class="lb"></span>본편·DLC 판매는 2027년 3월 31일 오전 10시에 끝납니다.<span class="lb"></span>그 뒤에도 서비스 종료 전까지는 다시 내려받을 수 있습니다.'
EXO_R = '<b>① 소장</b> <b>"Offline patch"(오프라인 패치)</b>에 42분 전까지 12개가 달렸습니다. 캡콤에 P2P 멀티 지원을 요구하자는 제안도 나왔습니다. 토론 활성 주제는 263건입니다.<span class="lb"></span><b>② 환불</b> <b>"NO REFUNDS!"(환불 불가!)</b> 글에는 1시간 전까지 답글 4건이 붙었습니다. <b>"I tried to save this game."(이 게임을 살리려 했다)</b>에는 의견 12개가 모였습니다.<span class="lb"></span><b>③ 지표</b> 오늘 07시대 스팀 동시 접속은 16명에 그쳤습니다. 지난 30일 평가 16개 중 31%만 긍정입니다. 전체 리뷰 2,601개는 75%가 호평이었습니다.<span class="lb"></span><b>종료 공지에 오프라인·소장 가능 여부를 함께 밝혀야 요구 글이 줄어듭니다.</b>'
CS_D1 = 'FlyQuest와 NIP가 Stage 2에 먼저 올랐습니다.'
CS_D2 = 'FlyQuest와 NIP가 3-0으로 Stage 2에 갔습니다.<span class="lb"></span>s1mple이 뛴 BC.Game은 세 번 모두 져 탈락했습니다.<span class="lb"></span>FaZe·HEROIC·100 Thieves는 1-2로 벼랑에 몰렸습니다.'
CS_R = '<b>① 이변</b> Chinggis Warriors가 BC.Game을 2-1로 꺾었습니다. 마지막 Nuke를 13-10으로 가져갔습니다. Strafe는 s1mple의 메이저 15회 출전 중 최악 성적이라고 썼습니다. DENDELE도 0-3으로 짐을 쌌습니다.<span class="lb"></span><b>② 접속</b> 스팀 동시 접속은 667,694명으로 어제보다 약 10% 늘었습니다. 스타 선수가 빨리 떨어진 날에도 이용자는 더 모였습니다. Stage 2는 11/28 토요일에 시작합니다.<span class="lb"></span><b>③ VAC</b> VAC이 처음 4~8라운드만 검사한다는 추측 글이 방금 올라왔습니다. 아직 댓글은 달리지 않았습니다.<span class="lb"></span><b>스타 선수가 일찍 탈락한 날엔 대회 일정 공지를 탈락 소식과 함께 갱신합니다.</b>'
FIN_D1 = '그랜드 메이저 2026이 내일 11/27 막을 올립니다.'
FIN_D2 = '그랜드 메이저 2026은 11/27부터 11/29까지 열립니다.<span class="lb"></span>스팀 동시 접속은 오늘 12,546명으로 집계됐습니다.<span class="lb"></span>토론 활성 주제는 어제 594건에서 558건으로 줄었습니다.'
FIN_R = '<b>① 치트</b> 토론 주제는 줄었지만 <b>"CHEATERS EVERYWHERE"(사방이 치터)</b>는 어제보다 8개 많은 22개입니다. 엠바크에 대책을 내놓으라는 글도 24건으로 불었습니다.<span class="lb"></span><b>② 무기</b> <b>"sword is broken"(검이 고장 났다)</b>에 의견 17개가 달렸습니다. 쌍검 버그를 알리는 새 글도 26분 전에 올라왔습니다. 아직 댓글은 1개만 붙었습니다.<span class="lb"></span><b>③ 진척</b> 지난 배틀패스는 채우기 너무 어렵다는 글에 의견 31개가 모였습니다. 무기 버그와는 별개의 불만도 쌓이고 있습니다.<span class="lb"></span><b>대회 전날 치트 글이 늘면 대회 서버와 일반 서버 대응을 나눠 안내합니다.</b>'

CARDP_HG = 'GOOD FUN CORP가 만든 1인칭 약탈 슈팅 게임입니다.<span class="lb"></span>무료 오픈 베타가 11월 27일부터 사흘 열립니다.<span class="lb"></span>스팀 한국어 상점에 적힌 앞서 해보기 날짜는 12월 3일입니다.<span class="lb"></span>보도자료에 따르면 찜이 70만 건을 넘었습니다.<span class="lb"></span>첫날엔 GUNBOAT-8 출시와 THE FINALS 그랜드 메이저 개막이 겹칩니다.'
OBS_HG = '<div class="obs"><button class="e2" type="button" aria-expanded="false"><span class="k">관전 포인트</span></button><span class="d2">루리웹 신설 게시판 14개 중 맨 위를 사흘째 지킵니다.<span class="lb"></span>같은 사이트 DB에는 한국어 미지원으로 표시돼 있습니다.<span class="lb"></span>스팀 평가는 아직 하나도 달리지 않았습니다.</span></div>'
CARDP_SMALL = 'DERELIKT는 평가 335개 중 84%가 긍정입니다.<span class="lb"></span>동시 접속은 어제 102명에서 84명으로 줄었습니다.<span class="lb"></span>Blackout Route는 평가 40개에 77% 긍정을 받았습니다.<span class="lb"></span>Mycopunk 접속자는 320명에서 430명으로 늘었습니다.<span class="lb"></span>Strato Alto는 오늘 출시됐고 07시대 평가가 0개였습니다.'
OBS_SMALL = '<div class="obs"><button class="e2" type="button" aria-expanded="false"><span class="k">관전 포인트</span></button><span class="d2">마이코펑크 전체 평가는 5,341개 중 88%가 긍정입니다.<span class="lb"></span>루리웹 신설 게시판엔 나머지 세 작품 없이 이 게임만 있습니다.<span class="lb"></span>Strato Alto는 전날 11월 25일로 잡혔다가 IGDB 캐시에서 빠졌습니다.</span></div>'
CARDP_DEC = 'IGDB 캐시에는 12월 1일 하루에만 슈터 13건이 몰렸습니다.<span class="lb"></span>Black Mesa: Classic 같은 소규모 작품이 많습니다.<span class="lb"></span>오늘부터 2주 동안 잡힌 슈터는 29건입니다.<span class="lb"></span>Cronos: Lazarus는 상점 12월 4일, IGDB 12월 3일로 하루 어긋납니다.<span class="lb"></span>HUNGER 앞서 해보기와 킨텍스 AGF 2026 개막도 같은 주에 있습니다.'
OBS_DEC = '<div class="obs"><button class="e2" type="button" aria-expanded="false"><span class="k">관전 포인트</span></button><span class="d2">상점과 대조한 3건 가운데 2건이 캐시와 어긋났습니다.<span class="lb"></span>Strato Alto는 빠졌고 Cronos: Lazarus는 하루 차이가 났습니다.<span class="lb"></span>GUNBOAT-8은 아예 캐시에 없습니다.</span></div>'

R1_TITLE = '접속자는 늘었지만 개발사 불신 글이 커지고 있습니다.'
R1_WHAT = '9/22 마케팅 비판 글엔 답글 118개가 쌓였습니다.<span class="lb"></span>치터 조롱 영상은 홍보용이었다는 주장으로 26분 전에도 갱신됐습니다.<span class="lb"></span><b>"Is Anti-cheat working?"(안티치트가 작동하긴 하나)</b>엔 의견 38개가 붙었습니다.<span class="lb"></span>월핵 사용자만 돈을 번다는 글은 37개에서 69개로 불었습니다.<span class="lb"></span>최근 3시간 사이 접속 끊김 제보도 5건 올라왔습니다.'
R1_CTX = '동시 접속 50,883명은 어제 48,313명보다 약 5% 많습니다.<span class="lb"></span>5만 명뿐이니 이번 시즌은 실패라는 글엔 답글이 0개입니다.<span class="lb"></span>시즌 4 초기화까지 뭘 할지 묻는 스레드엔 의견 95개가 달렸습니다.<span class="lb"></span>타르코프·배틀필드 6·아르마·스타 시티즌·그레이 존 워페어·THE FINALS가 거론됩니다.<span class="lb"></span>한국어 평가 2,994개 중 긍정은 39%뿐입니다.'
R1_LESSON = '<ol><li><b>신뢰</b> 지표가 반등해도 불신 담론에는 따로 답해야 합니다.</li><li><b>공지</b> 제재 실적과 끊김 원인은 나눠서 알립니다.</li><li><b>기록</b> 이탈 글에 나온 대체 게임 이름을 적어 둡니다.</li></ol>'
R2_TITLE = '종료 공지 뒤 오프라인 패치 요구가 이어지고 있습니다.'
R2_WHAT = '캡콤은 11/25에 2027-09-30 종료를 공지했습니다.<span class="lb"></span>서바이벌 패스 프리미엄은 그날 10시에 판매가 멈췄습니다.<span class="lb"></span>본편과 DLC는 2027-03-31 10시까지만 팝니다.<span class="lb"></span>스팀 <b>"Offline patch"(오프라인 패치)</b> 토론엔 답글이 12개입니다.<span class="lb"></span><b>"NO REFUNDS!"(환불 불가!)</b>엔 댓글 4개, 단독 실행·P2P 요청 글은 4건입니다.'
R2_CTX = '2023년 7월 출시작으로 2024년 7월 시즌4 뒤 새 콘텐츠가 없습니다.<span class="lb"></span>현재 스팀 동시 접속자는 16명에 그칩니다.<span class="lb"></span>지난 30일 평가 16개 중 긍정은 31%로, 전체 2,601개의 75%보다 낮습니다.<span class="lb"></span>판매가 끝나도 종료 전까지는 다시 내려받을 수 있습니다.<span class="lb"></span>같은 주 PUBG는 11/30부터 제재 통보에 이의제기 방법을 넣습니다.'
R2_LESSON = '<ol><li><b>일정</b> 판매 중단과 플레이 가능 기한을 한 표로 보여 줍니다.</li><li><b>문의</b> 오프라인 지원과 소장할 수 있는지를 먼저 답해 둡니다.</li><li><b>유료</b> 남은 판매 상품을 어떻게 처리할지 기준을 밝힙니다.</li></ol>'
A1_H3 = '종료 공지엔 판매 중단·플레이 기한·오프라인 여부를 함께 적습니다.'
A1_P = '엑조프라이멀은 종료 관련 날짜를 셋으로 나눠 알렸습니다.<span class="lb"></span>프리미엄 패스는 11/25에, 본편은 2027-03-31에 판매가 끝납니다.<span class="lb"></span>공지 직후 스팀의 오프라인 패치 요구 글은 답글 12개를 모았습니다.<span class="lb"></span>우리도 종료를 알릴 땐 세 날짜와 단독 실행 가능 여부를 한 표로 묶겠습니다.'
A2_H3 = '제재 통보문에는 위반 조항과 이의제기 경로를 함께 넣어야 합니다.'
A2_P = 'PUBG는 11/30부터 제재 통보에 조항·기간·이의제기 방법을 넣습니다.<span class="lb"></span>스팀 핵 의심 처리팀 찾기 글은 답글 17개에서 23개가 됐습니다.<span class="lb"></span>워독스의 안티치트 작동 의문 스레드도 의견 38개를 모았습니다.<span class="lb"></span>우리도 제재 통보문에 위반 조항과 이의제기 경로를 꼭 함께 적겠습니다.'

# ───────── 조립 ─────────
B = []
B.append('''<body>
<a class="skip" href="#main">본문 바로가기</a>
<div id="prog" aria-hidden="true"></div>
<header class="masthead">
<button class="themebtn" id="themebtn" type="button" aria-pressed="false" title="화면 테마">
<span class="lbltext">테마</span><span class="val" id="themelbl">LIGHT</span>
</button>
<div class="mh-inner">
<p class="eyebrow"><span class="live"></span>FPS · 슈터 데일리 커뮤니티/이벤트 레이더</p>
<h1>오늘의 FPS·슈터 동향 레이더</h1>
<div class="meta">
<span>기준일 <b>2026년 11월 26일 (목)</b></span>
<span class="cover-pill">커버기간: 11/25(수) – 11/26(목) 07시대</span>
<span>스팀·웹 07시대까지 수집</span>
</div>
</div>
</header>
<main id="main">
<div class="wrap">''')
B.append(f'<p class="lead">{LEAD}</p>')
B.append('<div class="notice"><span class="k">신선도</span><span><b>스팀·인벤·루리웹·펍지 공식은 데스크톱 내장 브라우저로 07시대에 열었습니다.</b><span class="lb"></span>인벤 오버워치 목록은 ?p=1로 열었고 최신 글이 06:16입니다.<span class="lb"></span>핫벤과 아카라이브는 이번 판에서 열지 않았습니다.</span></div>')
B.append('<div class="kpis" id="summary">'
 f'<div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">7건</div><div class="sub">{a(U["ow870"],"꽃 신령 이틀째")}<span class="sep">·</span>{a(U["strafe"],"CS2 메이저")}<span class="sep">·</span>{a(U["wd_d"],"워독스 시즌 3")}</div></div>'
 '<div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">워독스 개발사 불신 글에 답글이 118개 쌓였습니다</div><div class="sub">월핵 글은 <b>37개→69개</b>로 늘었습니다. <a href="#risk">상세 보기</a></div></div>'
 f'<div class="kpi"><div class="lbl">신작 반응</div><div class="big">HUNGER 오픈 베타가 내일 열립니다</div><div class="sub">루리웹 신설 게시판 <b>사흘째 1위</b>입니다. {a(U["st_hg"],"상점")}</div></div>'
 f'<div class="kpi"><div class="lbl">국내 포커스</div><div class="big">배그 제재 통보에 이의제기 방법이 들어갑니다</div><div class="sub"><b>11/30</b>부터 적용합니다. {a(U["pubg_pol"],"공지")}</div></div>'
 '</div>')

# 01 일정
def li(s, label, name, text, win, today=False):
    return f'<li class="{"today" if today else ""}"><span class="s {s}">{label}</span><span class="t"><b>{name}</b> {text}<span class="win">{win}</span></span></li>'
G = [
 ('11.26 목', True, [
  ('on','진행','오버워치 달빛 품은 꽃 신령','이틀째입니다','~12/9 09시'),
  ('on','진행','OWCS 응원 대회','이틀째입니다','~12/8'),
  ('on','진행','CS2 PGL 메이저 싱가포르','Stage 1 사흘째입니다','2팀 진출'),
  ('on','진행','워독스 시즌 3','15일째입니다','접속 50,883명'),
  ('on','진행','오버워치 군림 이벤트','23일째입니다','~12/8'),
  ('on','진행','마블 IGNITE 그랜드 파이널','나흘째입니다','~11/29'),
  ('on','진행','스페셜포스 2 스킬','사전예약 10일째입니다','11/17~'),
  ('end','종료','서든어택 브레드의 선택','마감됩니다','게임메카'),
  ('start','시작','Strato Alto','스팀에 나옵니다','상점 11/26'),
 ]),
 ('11.27 금', False, [
  ('start','시작','THE FINALS 그랜드 메이저 2026','개막합니다','~11/29'),
  ('start','시작','GUNBOAT-8','앞서 해보기로 나옵니다','상점 11/27'),
  ('start','시작','HUNGER 오픈 베타','무료로 열립니다','~11/29'),
 ]),
 ('11.28 토', False, [('start','시작','CS2 메이저 Stage 2','시작합니다','Strafe')]),
 ('11.30 월', False, [('start','시작','배그 운영정책 개정','적용됩니다','11/23 공지')]),
 ('12.01 화', False, [
  ('start','시작','IGDB 슈터 예정작 13건','하루에 몰렸습니다','상점 미대조'),
  ('end','종료','스팀 어워드 추천','03시에 마감됩니다','PT 11/30 10시'),
 ]),
 ('12.02 수', False, [('start','시작','배그 아이브 외형 개선','PC에 적용됩니다','티켓 10장')]),
 ('12.03 목', False, [
  ('start','시작','HUNGER','앞서 해보기로 나옵니다','상점 12/3'),
  ('end','종료','TGM26 이벤트 패스','판매가 끝납니다','공식 공지'),
  ('start','시작','OWCS 월드 파이널 방송','시작합니다','~12/7'),
 ]),
 ('12.04 금', False, [
  ('start','시작','AGF 2026','개막합니다','~12/6 킨텍스'),
  ('start','시작','Cronos: Lazarus','스팀에 나옵니다','IGDB 12/3'),
 ]),
 ('12.08 화', False, [
  ('start','시작','배틀필드 6 플래툰','3단계로 예고됐습니다','EA 공지'),
  ('end','종료','오버워치 군림 이벤트','끝납니다','패치노트'),
 ]),
 ('12.09 수', False, [('end','종료','오버워치 달빛 품은 꽃 신령','09시에 끝납니다','수령 기한 동일')]),
 ('12월 · 날짜 미정', False, [('start','시작','스페셜포스 2 스킬','PC로 정식 출시됩니다','게임메카 11/24')]),
 ('2027년', False, [
  ('end','종료','엑조프라이멀 본편·DLC','3/31 10시 판매를 멈춥니다','재다운로드 가능'),
  ('end','종료','엑조프라이멀','9/30 서비스를 마칩니다','인벤 11/25'),
 ]),
]
total = sum(len(x[2]) for x in G)
tl = [f'<div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>',
      '<div class="timeline">', f'<h3>움직이는 일정 {total}건</h3>',
      '<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/26)입니다.</p>']
for i,(d,isT,items) in enumerate(G):
    cls = 'dgroup today' if isT else 'dgroup'
    op = ' open' if i < 2 else ''
    tag = '<span class="dg-t">오늘</span>' if isT else ''
    tl.append(f'<details class="{cls}"{op}>')
    tl.append(f'<summary><span class="dg-d">{d}</span>{tag}<span class="dg-n">{len(items)}건</span></summary>')
    tl.append('<ol class="tl">' + ''.join(li(*it, today=isT) for it in items) + '</ol>')
    tl.append('</details>')
tl.append('</div>')
B += tl

# 02 헤드라인
def hero(url, key, mono, name, rank, flag, gm, h3, badges, under):
    return (f'<a class="hero" href="{url}" {T}>\n<div class="shot" data-mono="{mono}" data-name="{name}"><img src="{IMG[key]}" alt=""><span class="rank">{rank}</span><span class="flag n">{flag}</span><div class="over"><div class="gm">{gm}</div><h3>{h3}</h3></div></div>\n'
            f'<div class="under">{badges} {under}</div>\n</a>')
B.append('<div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n<section class="heroes">')
B.append(hero(U['exo_inv'],'EXO','EXO','EXOPRIMAL','01','서비스 종료','엑조프라이멀 · 캡콤','2027년 9월 30일 서비스 종료 발표',ev('kr','cm','mt'),UNDER_EXO))
B.append(hero(U['wd_cool'],'WD','WD','WARDOGS','02','개발사 불신','워독스 · 시즌 3','접속은 반등, 불신 글 답글 118개',ev('cm','mt'),UNDER_WD))
B.append(hero(U['strafe'],'CS2','CS2','COUNTER-STRIKE 2','03','s1mple 탈락','CS2 · PGL 싱가포르','Stage 1 이틀째, FlyQuest·NIP 진출',ev('gl','mt'),UNDER_CS))
B.append('</section>')

def g_cell(key, mono, name, title, sub):
    return f'<td><div class="g-cell">{thumb(key,mono,name)}<span class="g-name">{title}<em>{sub}</em></span></div></td>'
def row(gc, d1, d2, date, dsub, typ, badges, r, srcs):
    return ('<tr>\n' + gc + '\n'
      f'<td class="ev2"><button class="e2" type="button" aria-expanded="false"><span class="d1">{d1}</span></button><span class="d2">{d2}</span></td>\n'
      f'<td>{date}<span class="dsub">{dsub}</span></td>\n<td><span class="typ">{typ}</span></td>\n'
      f'<td>{badges}<span class="lb"></span>{r}<span class="src-inline">{" · ".join(srcs)}</span></td>\n</tr>')
THEAD = '<thead><tr><th>게임</th><th>이벤트 / 업데이트</th><th>날짜</th><th>유형</th><th>커뮤니티 반응 · 관전 포인트</th></tr></thead>'

# 03
B.append('<div class="sec" id="kr"><span class="idx">03</span><h2>국내 포커스</h2><span class="rule"></span></div>')
B.append('<p class="sub-lead">국내 서비스·국내 배경 IP·국내 커뮤니티(<b>인벤·루리웹·아카라이브</b>) 반응 중심.</p>')
B.append('<div class="evkey"><b>근거 표기</b><span><span class="ev kr">KR·기사</span><span class="d">국내 매체</span></span><span><span class="ev gl">글로벌·기사</span><span class="d">해외 매체</span></span><span><span class="ev cm">커뮤니티</span><span class="d">원문 직접 확인</span></span><span><span class="ev of">공식</span><span class="d">공식 공지</span></span><span><span class="ev mt">지표</span><span class="d">수치</span></span><span><span class="ev na">국내 반응 미확인</span><span class="d">국내 소스 미확인</span></span></div>')
B.append('<div class="tablewrap"><table>\n' + THEAD + '\n<tbody>')
B.append(row(g_cell('OW','OW','OVERWATCH 2','오버워치2','꽃 신령 이틀째 · 모드 제외'), OW_D1, OW_D2, '11/25~12/9','넥슨 공지','이벤트 · 게시판', ev('of','cm','mt'), OW_R,
  [a(U['ow870'],'넥슨 꽃 신령 공지'), a(U['inv_ow_440'],'인벤 정리 글'), a(U['inv_ow_std'],'인벤 스타디움 제외 글'), a(U['inv_ow_bad'],'인벤 불만 글'), a(U['inv_ow'],'인벤 오버워치 자유게시판')]))
B.append(row(g_cell('PUBG','PUBG','PUBG: BATTLEGROUNDS','배틀그라운드','운영정책 개정 · 11/30 적용'), PUBG_D1, PUBG_D2, '11/30~','11/23 공지','정책 · 제재', ev('of','mt','na'), PUBG_R,
  [a(U['pubg_pol'],'운영정책 개정 공지'), a(U['pubg_ban'],'주간 제재 현황'), a(U['inv_pubg'],'인벤 배그 게시판'), a(U['pubg_hack'],'스팀 처리팀 글')]))
B.append('</tbody>\n</table></div>')

# 04
B.append('<div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>')
B.append('<p class="sub-lead">근거는 <b>스팀 커뮤니티 토론·리뷰 원문</b>과 <b>SiegeGG·Dot Esports·Liquipedia</b> 등 전문지, 그리고 공식 패치노트입니다.</p>')
B.append('<div class="evkey">\n<b>오늘 연 해외 커뮤니티</b>\n'
 f'<span><span class="ev cm">확인</span>{a(U["wd_d"],"워독스")}<span class="d">상위 30건 · 방금~2시간 전 · 활성 주제 1,913건 · 글 본문 2건</span></span>\n'
 f'<span><span class="ev cm">확인</span>{a(U["exo_d"],"엑조프라이멀")}<span class="d">상위 12건 · 42분 전부터 · 활성 주제 263건 · 목록만</span></span>\n'
 f'<span><span class="ev cm">확인</span>{a(U["fin_d"],"THE FINALS")}<span class="d">상위 14건 · 26분 전부터 · 활성 주제 558건 · 목록만</span></span>\n'
 f'<span><span class="ev cm">확인</span>{a(U["cs_d"],"CS2")}<span class="d">상위 14건 · 방금부터 · 활성 주제 1,532건 · 목록만</span></span>\n'
 '<span><span class="ev cm">확인</span><span class="d">목록만: 배틀필드 6(1,205건) · PUBG(600건) · 에이펙스(522건) · 마블 라이벌즈(497건) · 오버워치2(328건) · 델타포스(286건) · 시즈(244건)</span></span>\n'
 '<span><span class="ev mt">확인</span><span class="d">스팀 Web API 현재 접속자 21종 · 07:34 한 번 · 스팀 상점 10종</span></span>\n'
 '<span><span class="ev gl">매체만</span><span class="d">CS2 메이저 2일차 결과: Strafe · HLTV</span></span>\n'
 '<span><span class="ev na">제외</span><span class="d">데스티니 2 토론은 고정글 1건뿐이라 뺐습니다</span></span>\n'
 '<span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>\n</div>')
B.append('<div class="tablewrap"><table>\n' + THEAD + '\n<tbody>')
B.append(row(g_cell('WD','WD','WARDOGS','워독스 (WARDOGS)','시즌 3 15일째 · 개발사 불신'), WD_D1, WD_D2, '11/26','접속 +5%','치트 · 여론', ev('cm','mt'), WD_R,
  [a(U['wd_cool'],'쿨한 개발사 착각 글'), a(U['wd_ac'],'안티치트 의문 글'), a(U['wd_wall'],'월핵 글'), a(U['wd_d'],'워독스 토론')]))
B.append(row(g_cell('EXO','EXO','EXOPRIMAL','엑조프라이멀','서비스 종료 발표 · 캡콤'), EXO_D1, EXO_D2, '11/25 발표','2027/9/30 종료','종료 · 여론', ev('kr','cm','mt'), EXO_R,
  [a(U['exo_inv'],'인벤 종료 기사'), a(U['exo_off'],'오프라인 패치 글'), a(U['exo_ref'],'환불 글'), a(U['exo_save'],'살리려 했다 글'), a(U['exo_store'],'스팀 상점')]))
B.append(row(g_cell('CS2','CS2','COUNTER-STRIKE 2','Counter-Strike 2','PGL 메이저 Stage 1 2일차'), CS_D1, CS_D2, '11/25','첫 탈락·진출','대회 · 지표', ev('gl','mt'), CS_R,
  [a(U['strafe'],'Strafe 2일차 정리'), a(U['hltv'],'HLTV BC.Game 탈락'), a(U['cs_vac'],'VAC 추측 글'), a(U['cs_d'],'CS2 토론')]))
B.append(row(g_cell('FIN','TF','THE FINALS','THE FINALS','그랜드 메이저 D-1 · 치트'), FIN_D1, FIN_D2, '11/27~29','대회 전날','치트 · 대회', ev('cm','mt'), FIN_R,
  [a(U['fin_ch'],'치터 글'), a(U['fin_em'],'치트 대책 요구 글'), a(U['fin_sw'],'검 고장 글'), a(U['fin_d'],'THE FINALS 토론')]))
B.append('</tbody>\n</table></div>')

# 05
def lrow(key, mono, name, title, sub, tag, tagtxt, dt, dsub, mk, sig, links, grp=False):
    th = thumb(key,mono,name) if key else f'<span class="thumb noimg" data-mono="{mono}" data-name="{name}"></span>'
    gattr = ' class="grp"' if grp else ''
    return (f'<tr{gattr}>\n<td class="g"><div class="g-cell">{th}<span class="g-name">{title}<em>{sub}</em></span></div></td>\n'
            f'<td><span class="tag {tag}">{tagtxt}</span></td>\n<td class="dt">{dt}<em>{dsub}</em></td>\n<td class="mk">{mk}</td>\n<td class="sig">{sig}</td>\n<td class="lk">{links}</td>\n</tr>')
B.append('<div class="sec" id="launch"><span class="idx">05</span><h2>신작 출시·발표</h2><span class="rule"></span></div>')
B.append('<p class="sub-lead">최근 나온 슈터와 곧 나올 슈터를 한 표에 모읍니다.</p>')
B.append('<div class="tablewrap launch"><table>\n<colgroup><col class="c-g"><col class="c-s"><col class="c-d"><col class="c-m"><col class="c-sig"><col class="c-l"></colgroup>\n<thead><tr><th>게임</th><th>상태</th><th>날짜</th><th>개발 · 배급</th><th>관심 신호</th><th>링크</th></tr></thead>\n<tbody>')
L = [
 lrow('DK','DK','DERELIKT','DERELIKT','레트로 SF 호러 FPS','t-new','출시','11.14','해외 11.13 · 시차','Visuwyg · Hyperstrange','평가 <b>335개</b> 중 <b>84%</b>(전날 319개 84%) · 접속 <b>84명</b>(전날 102명)', lk(U['st_dk'],'pc','스팀')),
 lrow('BR','BR','BLACKOUT ROUTE','Blackout Route','1인칭 협동 파밍 탈출 호러','t-new','출시','11.24','IGDB 11.23 · 앞서 해보기','Blackout Inc.','평가 <b>40개</b> 중 <b>77%</b>(전날 30개 76%) · API 접속 <b>10명</b>(전날 0명)', lk(U['st_br'],'pc','스팀')),
 lrow('SA','SA','STRATO ALTO','Strato Alto','아레나 슈팅 · 액션 로그라이크','t-new','출시','11.26','IGDB 캐시에서 빠짐','Reject Games','07시대 평가 <b>0개</b> · API 접속 <b>1명</b>', lk(U['st_sa'],'pc','스팀')),
 lrow('G8','G8','GUNBOAT-8','GUNBOAT-8','해상 탄막 로그라이크 · 아레나 슈팅','t-warn','예정','11.27','앞서 해보기 · IGDB 캐시 없음','Orange Acorn Games','평가 <b>0개</b> · API 접속 <b>42명</b> · 같은 날 일정 <b>2건</b>과 겹침', lk(U['st_g8'],'pc','스팀')),
 lrow('HG','HG','HUNGER','HUNGER','1인칭 약탈 슈팅 · 오픈 베타 11.27~29','t-live','예정','12.03','앞서 해보기 · IGDB 캐시 없음','GOOD FUN CORP','찜 <b>70만 건</b> 이상(보도자료) · 루리웹 신설 게시판 14개 중 <b>1위</b> 사흘째', lk(U['st_hg'],'pc','스팀') + '<br>' + lk(U['hg_pr'],'mail','정리 기사')),
 lrow('CL','CL','CRONOS: LAZARUS','Cronos: Lazarus','생존 공포 3인칭 슈팅','t-live','예정','12.04','IGDB 12.03','Bloober Team · PixelAnt Games','IGDB와 <b>1일</b> 차이 · 평가 <b>0개</b>', lk(U['st_cl'],'pc','스팀')),
 lrow('SF2','SF2','SPECIAL FORCE 2 S.K.I.L.L.','스페셜포스 2 스킬','밀리터리 FPS · 사전예약 11.17~','t-warn','발표','12월','PC · 일자 미공개','버티고우 게임즈','기사 조회 <b>2,875회</b>·댓글 <b>0개</b>(전날 확인) · 리마스터 접속 <b>3명</b>', lk(U['sf2'],'mail','정리 기사')),
 lrow(None,'IGDB','IGDB 슈터 예정','12/1 IGDB 슈터 예정','Black Mesa: Classic 외 · 소규모 다수','t-warn','미확정','12.01','IGDB 캐시 값','—','하루에 <b>13건</b>이 몰림 · 향후 2주 캐시 <b>29건</b> 중 상점 대조 <b>3건</b>','—', grp=True),
]
B.append('\n'.join(L))
B.append('</tbody>\n</table></div>')

# 06
def card(key, mono, name, chips, gm, h3, p, obs, srcs):
    return (f'<div class="tcard">\n{thumb(key,mono,name,"tbanner")}\n<div class="tin">\n<div class="chips">{chips}</div>\n<div class="gm">{gm}</div>\n'
            f'<h3>{h3}</h3><p>{p}</p>\n{obs}\n<div class="src">{" · ".join(srcs)}</div>\n</div>\n</div>')
B.append('<div class="sec" id="trend"><span class="idx">06</span><h2>신작 동향</h2><span class="rule"></span></div>\n<div class="trend-grid">')
B.append(card('HG','HG','HUNGER','<span class="tag t-live">오픈 베타 11/27</span><span class="tag t-warn">한국어 미지원</span>','신작 예정 · HUNGER','HUNGER 오픈 베타가 내일 시작합니다.',CARDP_HG,OBS_HG,
  [a(U['st_hg'],'HUNGER 상점'), a(U['hg_pr'],'오픈 베타 보도자료'), a(U['ruli_hg'],'루리웹 HUNGER 게시판')]))
B.append(card('DK','DK','DERELIKT','<span class="tag t-new">평가 335개</span><span class="tag t-live">30일 긍정 92%</span>','소형 슈터 · DERELIKT · Blackout Route · Mycopunk · Strato Alto','최근 출시작 네 편의 접속 흐름이 갈렸습니다.',CARDP_SMALL,OBS_SMALL,
  [a(U['st_dk'],'DERELIKT 상점'), a(U['st_br'],'Blackout Route 상점'), a(U['st_my'],'Mycopunk 상점'), a(U['st_sa'],'Strato Alto 상점')]))
B.append(card('CL','CL','CRONOS: LAZARUS','<span class="tag t-warn">12/1 13건</span><span class="tag t-live">12/4 Cronos</span>','12월 첫 주 · IGDB 캐시','12월 첫 주에 소형 슈터 출시가 몰립니다.',CARDP_DEC,OBS_DEC,
  [a(U['st_cl'],'Cronos: Lazarus 상점'), a(U['st_sa'],'Strato Alto 상점'), a(U['st_g8'],'GUNBOAT-8 상점')]))
B.append('</div>')

# 07
B.append('<div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>')
B.append(f'<article class="risk high"><div class="lvl">HIGH · 개발사 불신</div><h3>{R1_TITLE}</h3><div class="row"><span class="k">무엇이</span><span>{R1_WHAT}</span></div><div class="row"><span class="k">맥락</span><span>{R1_CTX}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span>{R1_LESSON}</div></article>'
         f'<article class="risk"><div class="lvl">MID · 서비스 종료</div><h3>{R2_TITLE}</h3><div class="row"><span class="k">무엇이</span><span>{R2_WHAT}</span></div><div class="row"><span class="k">맥락</span><span>{R2_CTX}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span>{R2_LESSON}</div></article>')
# 08
B.append('<div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>')
B.append(f'<article class="act"><div class="num">1</div><div><h3>{A1_H3}</h3><p>{A1_P}</p></div></article><article class="act"><div class="num">2</div><div><h3>{A2_H3}</h3><p>{A2_P}</p></div></article>')
# caveat
cv = [('방법','이번 판은 11/26 07시대에 데스크톱 내장 브라우저로 읽었습니다.<span class="lb"></span>토론 수치는 목록 첫 페이지 상위 글에서 셌습니다.'),
      ('측정','동시 접속은 스팀 Web API로 07:34에 한 번 잰 값입니다.<span class="lb"></span>목요일 아침 값을 수요일 아침과 견줬습니다.'),
      ('일정','IGDB 캐시는 11/25 09:20 갱신본입니다.<span class="lb"></span>상점과 맞춘 3건 중 2건이 어긋났습니다.'),
      ('미공개','배그 주간 제재 공지는 영구 제한 명단만 붙였습니다.<span class="lb"></span>본문에 건수가 없어 규모를 셀 수 없었습니다.'),
      ('미확인','Liquipedia는 사람 확인 화면이 떠서 열지 않았습니다.<span class="lb"></span>CS2 결과는 Strafe와 HLTV 기사로 맞췄습니다.'),
      ('시차','엑조프라이멀 종료일은 인벤 기사의 9월 30일을 따랐습니다.<span class="lb"></span>스팀 토론 제목은 미국 기준으로 9월 29일이라 적었습니다.')]
B.append('<div class="caveat">\n<span class="k">유의사항</span>\n' + ''.join(f'<span class="crow"><b class="ck">{k}</b><span>{v}</span></span>' for k,v in cv) + '\n</div>')
# 09
srcs = [
 ('스팀 토론', [(U['wd_cool'],'워독스 쿨한 개발사 착각 글'),(U['wd_ac'],'워독스 안티치트 의문 글'),(U['wd_wall'],'워독스 월핵 글'),(U['wd_cwis'],'워독스 CWIS 글'),(U['wd_s4'],'워독스 시즌 4 대기 글'),(U['wd_d'],'워독스 토론'),
   (U['exo_off'],'엑조프라이멀 오프라인 패치 글'),(U['exo_p2p'],'엑조프라이멀 P2P 요구 글'),(U['exo_ref'],'엑조프라이멀 환불 글'),(U['exo_save'],'엑조프라이멀 살리려 했다 글'),(U['exo_d'],'엑조프라이멀 토론'),
   (U['cs_vac'],'CS2 VAC 추측 글'),(U['cs_d'],'CS2 토론'),(U['fin_ch'],'THE FINALS 치터 글'),(U['fin_em'],'THE FINALS 치트 대책 글'),(U['fin_sw'],'THE FINALS 검 고장 글'),(U['pubg_hack'],'PUBG 처리팀 글')]),
 ('스팀 상점·지표', [(U['wd_store'],'워독스 상점'),(U['exo_store'],'엑조프라이멀 상점'),(U['st_dk'],'DERELIKT 상점'),(U['st_br'],'Blackout Route 상점'),(U['st_sa'],'Strato Alto 상점'),(U['st_g8'],'GUNBOAT-8 상점'),(U['st_hg'],'HUNGER 상점'),(U['st_cl'],'Cronos: Lazarus 상점'),(U['st_my'],'Mycopunk 상점'),(U['api'],'스팀 Web API 현재 접속자')]),
 ('공식', [(U['ow870'],'넥슨 꽃 신령 이벤트 공지'),(U['pubg_pol'],'PUBG 운영정책 개정 안내'),(U['pubg_ban'],'PUBG 주간 제재 현황')]),
 ('기사', [(U['exo_inv'],'인벤 엑조프라이멀 종료'),(U['strafe'],'Strafe 메이저 2일차'),(U['hltv'],'HLTV BC.Game 탈락'),(U['hg_pr'],'HUNGER 오픈 베타 보도자료'),(U['sf2'],'게임메카 스페셜포스 2 스킬')]),
 ('국내 커뮤니티', [(U['inv_ow_440'],'인벤 꽃 신령 정리 글'),(U['inv_ow_std'],'인벤 스타디움 제외 글'),(U['inv_ow_bad'],'인벤 이벤트 불만 글'),(U['inv_ow'],'인벤 오버워치 자유게시판'),(U['inv_pubg'],'인벤 배그 전체 게시판'),(U['ruli'],'루리웹 메인 신설 게시판'),(U['ruli_hg'],'루리웹 HUNGER 게시판')]),
]
nsrc = sum(len(x[1]) for x in srcs)
B.append(f'<!-- 09 출처 -->\n<details class="sources" id="sources" open>\n<summary>출처 링크 {nsrc}건</summary>\n<div class="body">\n<ul>')
for k, lst in srcs:
    B.append(f'<li><b>{k}</b>' + ' · '.join(a(u,t) for u,t in lst) + '</li>')
B.append('</ul>\n<div class="colophon">\n<b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.140<br>\n모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n</div>\n</div>\n</details>\n</div>\n')

html = head + '\n'.join(B) + tail
open(OUT, 'w', encoding='utf-8').write(html)
print('written', OUT, len(html), 'schedule', total, 'sources', nsrc)
