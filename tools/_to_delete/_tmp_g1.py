import re,json,os
R=os.path.expanduser('~/mnt/fps-radar')
old=open(R+'/reports/2026-10/FPS레이더_2026-10-17.html',encoding='utf-8').read()
i=old.find('<main'); j=old.find('</main>')
pre=old[:i].replace('2026-10-17','2026-10-18').replace('2026년 10월 17일 (토)','2026년 10월 18일 (일)').replace('커버기간: 10/16(금) 오전 – 10/17(토) 오전','커버기간: 10/17(토) 오전 – 10/18(일) 오전')
post=old[j:]
TH={}
for m in re.finditer(r'data-name="([^"]+)"[^>]*><img src="([^"]*)"',old): TH.setdefault(m.group(1),m.group(2))
def th(name,mono,cls='thumb'):
    s=TH.get(name)
    if s: return f'<span class="{cls}" data-mono="{mono}" data-name="{name}"><img src="{s}" alt=""></span>'
    return f'<span class="{cls} noimg" data-mono="{mono}" data-name="{name}"></span>'
U={
'steam_bf':'https://steamcommunity.com/app/2807960/discussions/0/','steam_arc':'https://steamcommunity.com/app/1808500/discussions/0/','steam_wd':'https://steamcommunity.com/app/1867240/discussions/0/',
'st_arc':'https://store.steampowered.com/app/1808500/?l=koreana','st_wd':'https://store.steampowered.com/app/1867240/?l=koreana','st_bf':'https://store.steampowered.com/app/2807960/?l=koreana',
'st_myc':'https://store.steampowered.com/app/3247750/Mycopunk/?l=koreana','st_bg2':'https://store.steampowered.com/app/3115160/Warhammer_40000_Boltgun_2/?l=koreana',
'hot':'https://hot.inven.co.kr','ow':'https://www.inven.co.kr/board/overwatch/4538?p=1',
'hs':'https://www.hotspawn.com/valorant/news/loud-on-the-verge-of-a-historic-second-valorant-champions-title','hs3':'https://www.hotspawn.com/valorant/news/valorant-champions-shanghai-top-3',
'vlr':'https://www.vlr.gg/773533/revenge-is-sweet-loud-advances-to-shanghai-grand-final','spike':'https://www.thespike.gg/events/results/valorant-champions-tour-2026-champions-shanghai/4233',
'ig':'https://www.invenglobal.com/articles/26485/arc-raiders-to-test-pvp-free-pve-mode-in-october','gt':'https://gamingtrend.com/news/wardogs-releases-season-2-on-october-15/',
'pn':'https://www.playnews.gg/en/updates/wardogs-will-the-season-2-progression-reset-scare-players-away','ts':'https://timesaver.gg/blog/battlefield-6-free-trial-season-5-dates-platforms',
'gem':'https://www.gematsu.com/2026/08/warhammer-40000-boltgun-ii-launches-october-14-for-ps5-xbox-series-and-pc-later-for-switch-2','mo':'https://massivelyop.com/2026/09/24/colorful-co-op-shooter-mycopunk-confirms-its-1-0-release-date-of-october-20/',
'bulk':'https://bulkhead.com/games/wardogs','ubi':'https://www.ubisoft.com/en-us/game/the-division/news-updates/23q5ICm6Mf4PUPuPUUS0uP/the-division-2-echoes-of-central-park-coming-on-november-3','mp1':'https://mp1st.com/news/the-division-2-echoes-of-central-park-releases-november-3-brings-new-endgame-experience',
'inv_s5':'https://www.inven.co.kr/webzine/news/?news=321844'}
def a(k,t): return f'<a href="{U[k]}" target="_blank" rel="noopener">{t}</a>'
LB='<span class="lb"></span>'
SV={'pc':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg>',
'home':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2 7.1 8 2.3l6 4.8v6.2a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/><path d="M6.3 14.3V9.7h3.4v4.6"/></svg>',
'mail':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="3.3" width="13" height="9.4" rx="1.4"/><path d="m2.3 4.7 5.7 3.9 5.7-3.9"/></svg>'}
def lk(k,ic,t): return f'<a href="{U[k]}" target="_blank" rel="noopener">{SV[ic]}<span>{t}</span></a>'
def ev2(d1,d2): return f'<td class="ev2"><button class="e2" type="button" aria-expanded="false"><span class="d1">{d1}</span></button><span class="d2">{d2}</span></td>'
def obs(t): return f'<div class="obs"><button class="e2" type="button" aria-expanded="false"><span class="k">관전 포인트</span></button><span class="d2">{t}</span></div>'
def row(name,mono,gname,em,d1,d2,dt,dsub,typ,react):
    return f'<tr>\n<td><div class="g-cell">{th(name,mono)}<span class="g-name">{gname}<em>{em}</em></span></div></td>\n{ev2(d1,d2)}\n<td>{dt}<span class="dsub">{dsub}</span></td>\n<td><span class="typ">{typ}</span></td>\n<td>{react}</td>\n</tr>\n'
EV={'cm':'<span class="ev cm">커뮤니티</span>','mt':'<span class="ev mt">지표</span>','gl':'<span class="ev gl">글로벌·기사</span>','kr':'<span class="ev kr">KR·기사</span>','of':'<span class="ev of">공식</span>','na':'<span class="ev na">국내 반응 미확인</span>'}
def er(*k): return '<span class="evrow">'+''.join(EV[x] for x in k)+'</span>'
def src(*l): return '<span class="src-inline">'+' · '.join(l)+'</span>'
today=[('on','진행','<b>VCT 챔피언스 상하이 그랜드 파이널</b> LOUD 대 Vitality가 열립니다','15시 · 5판 3선승'),
('on','진행','<b>워독스 시즌 2</b> 4일째입니다','10/15 시작'),
('on','진행','<b>아크 레이더스 PvE 전용 테스트</b> 6일째입니다','~10/20'),
('on','진행','<b>배틀필드 6 시즌 5와 스팀 무료 체험</b> 이어집니다','체험 ~10/20 02시'),
('on','진행','<b>워해머 40,000: 볼트건 2</b> 출시 5일째입니다','상점 표시 미확인'),
('on','진행','<b>마블 라이벌즈 시즌 10.5</b> 10일째입니다','신규 영웅 없음'),
('on','진행','<b>오버워치 핼러윈 이벤트</b> 이어집니다','맵 ~11/3'),
('on','진행','<b>오버워치 나 혼자만 레벨업 콜라보</b> 이어집니다','~10/21'),
('on','진행','<b>아크 레이더스 얼어붙은 산길</b> 11일째입니다','10/8 시작'),
('on','진행','<b>서든어택 시즌4 문라이즈</b> 돌아갑니다','~12/10')]
groups=[('10.18 일','오늘',today),
('10.20 화',None,[('end','종료','<b>아크 레이더스 PvE 테스트</b> 끝납니다','영구 도입 미약속'),('start','시작','<b>마이코펑크</b> 정식 출시와 해보기 종료가 겹칩니다','스팀 기준'),('end','종료','<b>배틀필드 6 스팀 무료 체험</b> 끝납니다','02시 · 2차 정보')]),
('10.21 수',None,[('end','종료','<b>오버워치 나 혼자만 레벨업 콜라보</b> 끝납니다','넥슨 공지 기준'),('start','시작','<b>배틀필드 6 Dead Space 시나리오</b> 시작합니다','~11/8 · 인벤 기준')]),
('10.22 목',None,[('end','종료','<b>오버워치 출석체크</b> 마감됩니다','오전 10시'),('end','종료','<b>서든어택 브레드 스킨</b> 판매가 끝납니다','상점 내림')]),
('11.03 화',None,[('start','시작','<b>디비전 2 센트럴 파크의 메아리</b> 확장이 나옵니다','유비소프트 공지')])]
tot=sum(len(g[2]) for g in groups)
tl=f'<div class="timeline">\n<h3>움직이는 일정 {tot}건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(10/18)입니다.</p>\n'
for gi,(d,tg,items) in enumerate(groups):
    cls='dgroup today' if tg else 'dgroup'; op=' open' if gi<2 else ''
    tl+=f'<details class="{cls}"{op}>\n<summary><span class="dg-d">{d}</span>'+(f'<span class="dg-t">{tg}</span>' if tg else '')+f'<span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">\n'
    for s,l,t,w in items:
        c=' class="today"' if tg else ''
        tl+=f'<li{c}><span class="s {s}">{l}</span><span class="t">{t}<span class="win">{w}</span></span></li>\n'
    tl+='</ol>\n</details>\n'
tl+='</div>\n'
lead=('<p class="lead"><span class="lrow hi"><b class="lk">핵심</b><span class="lt"><b>발로란트 챔피언스 상하이 그랜드 파이널에서 오늘 15시 LOUD와 Vitality가 5판 3선승으로 맞붙습니다.</b></span></span>'
'<span class="lrow"><b class="lk">스팀</b><span class="lt">아크 레이더스 일반 토론 첫 15건 중 8건이 PvE 제목이고 답글 501개 글도 있습니다. 워독스 첫 15건에는 치트 2건과 초기화 2건이 보입니다.</span></span>'
'<span class="lrow"><b class="lk">국내</b><span class="lt">인벤 핫벤 상위 200건에는 슈터 글이 한 건도 없습니다. 오버워치 자유게시판은 어제와 같은 05:26 글이 맨 위입니다.</span></span>'
'<span class="lrow"><b class="lk">일정</b><span class="lt">배틀필드 6 체험과 아크 레이더스 PvE 테스트는 모레 20일에 함께 끝납니다.</span></span></p>\n')
notice=('<div class="notice"><span class="k">측정 주의</span><span><b>워독스 상점 수치는 어제 판과 같은 값이라 변화 지표로 쓰지 않았습니다.</b>'+LB+'일요일 판이라 어제 오전부터 오늘 오전까지 묶었습니다.'+LB+'배틀필드 6 토론 목록은 어제 기록과 어긋나 이번 판에서 뺐습니다.'+LB+'스팀 목록의 "방금 전" 표기는 캐시 가능성이 있어 시각을 인용하지 않았습니다.</span></div>\n')
kpis=('<div class="kpis" id="summary"><div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">10건+</div><div class="sub">'+a('steam_bf','배틀필드 6 무료 체험')+'<span class="sep">·</span>'+a('ig','아크 레이더스 PvE')+'<span class="sep">·</span>'+a('gt','워독스 시즌 2')+'<span class="sep">·</span>'+a('hs3','VCT 챔피언스')+'</div></div>'
'<div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">아크 레이더스 PvE 찬반 글이 크게 붙었습니다</div><div class="sub">첫 15건 중 PvE 제목은 <b>8건</b>입니다. <a href="#risk">상세 보기</a></div></div>'
'<div class="kpi"><div class="lbl">신작 반응</div><div class="big">워독스 한국어 평가는 1,198개, 긍정 58%입니다</div><div class="sub">어제와 같은 값이라 <b>변화로 보지 않았습니다</b></div></div>'
'<div class="kpi"><div class="lbl">국내 포커스</div><div class="big">핫벤 200위 안 슈터 글은 0건입니다</div><div class="sub">오버워치 게시판은 <b>어제 스냅샷</b>과 같습니다</div></div></div>\n')
def hero(rank,flag,name,mono,gm,h3,under,url):
    inner=f'<span class="rank">{rank}</span><span class="flag n">{flag}</span><div class="over"><div class="gm">{gm}</div><h3>{h3}</h3></div>'
    t=th(name,mono,'shot').replace('<span class="shot','<div class="shot').replace('</span>','</div>')
    if 'noimg' in t: t=t.replace('></div>','>'+inner+'</div>')
    else: t=t.replace('</div>',inner+'</div>')
    return f'    <a class="hero" href="{url}" target="_blank" rel="noopener">\n      {t}\n      <div class="under">{under}</div>\n    </a>\n'
heroes='  <section class="heroes">\n'+hero('01','그랜드 파이널','VALORANT','VAL','발로란트 · VCT 챔피언스 상하이','LOUD 대 Vitality, 오늘 15시 5판 3선승',
 er('gl','na')+' Vitality가 하위 결승에서 100 Thieves를 3대1로 꺾었습니다. Hotspawn은 그랜드 파이널이 LOUD 대 Vitality의 5판 3선승이라고 전했습니다. 한국 시각 15시 시작은 브라질 매체 안내를 환산한 값입니다. 한국 팀이 없어 국내 반응은 확인하지 못했습니다.',U['hs'])
heroes+=hero('02','PvE 찬반','ARC RAIDERS','ARC','아크 레이더스 · PvE 테스트 6일째','토론 첫 15건 중 PvE 제목 8건',
 er('cm','mt')+' 일반 토론 첫 15건 중 PvE 제목이 8건입니다. "To the PVE \'Community\'..." 글에는 답글 501개가 달렸습니다. "ARC Raiders Is a Complete Joke"는 255개이고 "Should Keep PvE"는 21개입니다. 목록이 "방금 전"으로만 찍혀 캐시 가능성이 있습니다.',U['steam_arc'])
heroes+=hero('03','시즌 2 초기화','WARDOGS','WD','워독스 · 시즌 2 4일째','첫 15건에 치트 2건과 초기화 2건',
 er('cm','mt')+' 개발자 고정글 "Backend Update Season 02 | We got a few things wrong"이 잠긴 채 올라와 있습니다. 첫 15건에는 "Cheater heaven now"와 "Stop crying about the wipe"가 보입니다. "Uninstalled, Not worth stress and anxiety"도 있습니다. 한국어 평가 1,198개와 긍정 58%는 어제와 같은 값입니다.',U['steam_wd'])
heroes+='  </section>\n'
OWd=row('OVERWATCH 2','OW','오버워치2','인벤 핫벤','핫벤 상위 200건에 오버워치 글이 보이지 않았습니다.','오늘 07시대 핫벤 200건을 훑었으나 슈터 글은 한 건도 없었습니다.'+LB+'어제는 오버워치 4건이 있었습니다.'+LB+'자유게시판 목록은 05:26 글이 맨 위라 어제 스냅샷으로 판단했습니다.','10/18','핫벤 200건 훑음','핫벤 · 국내 반응',
 er('cm','mt')+' 핫벤 상위 200건과 오버워치 자유게시판 목록을 살폈습니다. 반응은 크게 두 가지입니다.'+LB+'<b>① 핫벤</b> 슈터 글은 0건이고 어제의 4건이 모두 빠졌습니다.'+LB+'<b>② 자유게시판</b> "지금 북미섭이 왜 저렇게 됐을까를 찾다보니까"가 <b>조회 158회</b>, 의견 5개입니다. "헤드셋 끼면 안더움?"에는 의견 12개가 붙었습니다.'+LB+'맨 위 글이 어제와 같은 05:26이라 새 글을 놓쳤을 수 있습니다.'+src(a('hot','인벤 핫벤'),a('ow','인벤 오버워치 자유게시판')))
VAr=row('VALORANT','VAL','발로란트','챔피언스 상하이','오늘 15시 그랜드 파이널에서 LOUD가 Vitality를 만납니다.','Vitality가 하위 결승에서 100 Thieves를 3대1로 이겼습니다.'+LB+'Hotspawn은 그랜드 파이널이 5판 3선승이고 Mercedes-Benz Arena에서 열린다고 전했습니다.'+LB+'LOUD는 어제 상위 결승에서 Vitality를 2대1로 이겼습니다.','10/18','파이널 15시','e스포츠 · 국내 반응 미확인',
 er('gl','na')+' <b>① 하위</b> Vitality가 100 Thieves를 <b>3대1</b>로 꺾었습니다. 맵 점수는 확인하지 못했습니다.'+LB+'<b>② 파이널</b> 둘은 이번 대회에서 세 번째로 만납니다. 이번에는 5판 3선승입니다.'+LB+'<b>③ 시각</b> 15시는 브라질 매체의 새벽 3시 안내를 환산한 값입니다.'+LB+'한국 팀이 없어 국내 반응 지표를 만들 수 없습니다.'+src(a('hs','Hotspawn 파이널 전망'),a('vlr','VLR 상위 결승'),a('spike','The Spike 결과')))
tab=lambda body:'  <div class="tablewrap"><table>\n    <thead><tr><th>게임</th><th>이벤트 / 업데이트</th><th>날짜</th><th>유형</th><th>커뮤니티 반응 · 관전 포인트</th></tr></thead>\n    <tbody>\n'+body+'    </tbody>\n  </table></div>\n'
ARCr=row('ARC RAIDERS','ARC','아크 레이더스','PvE 테스트 6일째','PvE 테스트는 모레 20일에 끝나고 영구 도입은 미정입니다.','PvE 전용 테스트는 10월 13일부터 20일까지입니다.'+LB+'Inven Global은 영구 도입이 약속되지 않았다고 전했습니다.'+LB+'오늘은 6일째입니다.','10/18','PvE 10/13~20','테스트 · PvE',
 er('cm','gl','mt')+' 일반 토론 첫 15건을 읽었습니다. PvE 제목이 <b>8건</b>이라 목록의 절반 넘게 PvE입니다.'+LB+'<b>① 반대</b> "ARC Raiders Is a Complete Joke"에 답글 <b>255개</b>, "pve folks are gonna be the downfall of this game"에 12개가 붙었습니다.'+LB+'<b>② 찬성</b> "Should Keep PvE"가 21개, "PLEASE make the PVE Mode Permanent!"가 2개입니다.'+LB+'<b>③ 논쟁</b> "To the PVE \'Community\'..."는 답글 <b>501개</b>입니다. 시각이 "방금 전"뿐이라 캐시일 수 있습니다.'+src(a('steam_arc','아크 레이더스 일반 토론'),a('ig','Inven Global PvE 테스트')))
WDr=row('WARDOGS','WD','워독스 (WARDOGS)','시즌 2 4일째','시즌 2 초기화 뒤 치트와 진행도 불만 제목이 이어집니다.','신규 무기 4종과 차량, 설치물이 더해진 시즌 2가 10월 15일에 시작했습니다.'+LB+'개발진은 "We got a few things wrong"이라는 백엔드 업데이트 글을 고정했습니다.'+LB+'GamingTrend 기사에는 초기화 언급이 없습니다.','10/18','시즌 2 4일째','앞서 해보기 · 시즌 2',
 er('cm','gl','mt')+' 일반 토론 첫 15건에서 불만 제목을 세 갈래로 나눴습니다.'+LB+'<b>① 치트 2건</b> "Cheater heaven now"와 "Banned for cheating while afk watching youtube?"입니다.'+LB+'<b>② 초기화 2건</b> "Stop crying about the wipe"와 "Garbage AR meta, everything else is irrelavent now. Progession is cooked day one of wipe."입니다.'+LB+'<b>③ 이탈</b> "Uninstalled, Not worth stress and anxiety" 답글은 16개입니다.'+LB+'한국어 평가 1,198개와 긍정 58%는 어제와 같습니다.'+src(a('steam_wd','워독스 일반 토론'),a('gt','GamingTrend 시즌 2'),a('pn','playnews 시즌 2 초기화'),a('st_wd','워독스 스팀 상점')))
glkey=('  <div class="evkey">\n    <b>오늘 연 해외 커뮤니티</b>\n    <span><span class="ev cm">확인</span>'+a('steam_arc','아크 레이더스')+' · '+a('steam_wd','워독스')+'<span class="d">오전 7시대 확인 · 일반 토론 방 첫 15건 제목만 읽음 · 본문은 열지 못함</span></span>\n'
'    <span><span class="ev mt">확인</span><span class="d">스팀 한국어 평가: 워독스 1,198개 긍정 58% · 어제와 같은 값이라 변화로 쓰지 않음</span></span>\n'
'    <span><span class="ev na">제외</span><span class="d">배틀필드 6 토론은 어제 기록과 어긋나는 목록이 와서 이번 판에서 뺌</span></span>\n'
'    <span><span class="ev na">미열람</span><span class="d">레인보우 식스 시즈 · CS2 · 에이펙스 · 데스티니 2 · THE FINALS · 데드록 토론 · 아크 레이더스 한국어 평가</span></span>\n'
'    <span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>\n  </div>\n')
evkey03=re.search(r'<div class="evkey"><b>근거 표기</b>.*?</div>\n',old,flags=re.S).group(0)
