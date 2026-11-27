# -*- coding: utf-8 -*-
import re, os, json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREV=ROOT+'/reports/2026-11/FPS레이더_2026-11-27.html'
OUT=ROOT+'/reports/2026-11/FPS레이더_2026-11-28.html'
s=open(PREV,encoding='utf-8').read()
head=s[:s.find('<body')]
tail=s[s.find('</main>'):]
head=head.replace('2026-11-27','2026-11-28')
def blocks(p):
    t=open(os.path.expanduser(p),encoding='utf-8').read()
    out={}
    for m in re.finditer(r'===(.+?)===\n(.*?)(?=\n===|\Z)',t,re.S):
        out[m.group(1)]=m.group(2).strip()
    return out
B=blocks('~/w/blocks.txt'); B.update(blocks('~/w/blocks2.txt'))
T='target="_blank" rel="noopener"'
def a(u,t): return f'<a href="{u}" {T}>{t}</a>'
SVG={'pc':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg>',
 'mail':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="3.3" width="13" height="9.4" rx="1.4"/><path d="m2.3 4.7 5.7 3.9 5.7-3.9"/></svg>'}
def lk(u,k,l): return f'<a href="{u}" {T}>{SVG[k]}<span>{l}</span></a>'
ST='https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/'
IMG={'SA':'../../assets/thumbs/sudden-attack.jpg',
'OW':ST+'2357570/26446ff05a359d4942e277f82fd347e89b275be3/header.jpg?t=1786471282',
'WD':ST+'1867240/24c0b6c0621560e922fbed18545921e7eaa9036e/capsule_616x353.jpg?t=1794488577',
'BF6':ST+'2807960/c12d12ce3c7d217398d3fcad77427bfc9d57c570/header.jpg?t=1789484400',
'CS2':ST+'730/162664aa5da85f418105350c5d67ca565f6c3713/header.jpg?t=1784564069',
'TF':ST+'2073850/61f55ef49a74c76bf9fda9ec35bc3101eeee2b3e/header.jpg?t=1787220389',
'DK':ST+'3810510/ecd586ce4f242e46d4febaf9209c3d09d5f9d4c8/capsule_616x353.jpg?t=1794855109',
'G8':ST+'4783980/00b44a553fb18b11352263ba42481d917d8d3910/capsule_616x353.jpg?t=1795723209',
'HG':ST+'1752080/capsule_616x353.jpg?t=1795644705',
'DE':ST+'4714830/4a97eb208fd69d19ef11766a1be85b054284f271/capsule_616x353.jpg?t=1795200998',
'BFW':ST+'4653750/01164ac838c4305df20612eb3eddf57dd85cb893/capsule_616x353.jpg?t=1795816227',
'CL':ST+'4768180/411a12bf6a84488dfa98243ac44afd670beb3166/capsule_616x353.jpg?t=1793200387',
'GE':ST+'3734220/d7bbf1a79027e0d819187cf7e17f785375887d1d/capsule_616x353.jpg?t=1795618362'}
NAME={'SA':('SA','서든어택'),'OW':('OW','OVERWATCH 2'),'WD':('WD','WARDOGS'),'BF6':('BF6','BATTLEFIELD 6'),'CS2':('CS2','COUNTER-STRIKE 2'),'TF':('TF','THE FINALS'),'DK':('DK','DERELIKT'),'G8':('G8','GUNBOAT-8'),'HG':('HG','HUNGER'),'DE':('DE','DESERT ECHO'),'BFW':('TBF','THE BRAVE FEW'),'CL':('CL','CRONOS: LAZARUS'),'GE':('GE','GUNS OF ESCHATON'),'CF':('CF','CROSSFIRE'),'IG':('IGDB','IGDB 슈터 예정')}
def thumb(k,cls='thumb'):
    m,n=NAME[k]
    if k in IMG: return f'<span class="{cls}" data-mono="{m}" data-name="{n}"><img src="{IMG[k]}" alt=""></span>'
    return f'<span class="{cls} noimg" data-mono="{m}" data-name="{n}"></span>'
LB='<span class="lb"></span>'
def store(i): return f'https://store.steampowered.com/app/{i}/?l=koreana'
U={'ga':'https://sa.nexon.com/InfoCenter/gmstory/view.aspx?n4ArticleSN=475','sanl':'https://sa.nexon.com/news/notice/list.aspx',
'sarb':'https://sa.nexon.com/community/free/view.aspx?n4ArticleSN=3314515','safont':'https://sa.nexon.com/community/free/view.aspx?n4ArticleSN=3314510',
'owmem':'https://www.inven.co.kr/board/overwatch/4538/5941869','ownx':'https://www.inven.co.kr/board/overwatch/4538/5941899','owstd':'https://www.inven.co.kr/board/overwatch/4538/5941871','owb':'https://www.inven.co.kr/board/overwatch/4538','owev':'https://overwatch.nexon.com/news/event/870',
'cfs':'https://www.inven.co.kr/webzine/news/?news=323945','wf':'https://www.inven.co.kr/webzine/news/?news=323822',
'wdcw':'https://steamcommunity.com/app/1867240/discussions/0/573807613531287915/','wddead':'https://steamcommunity.com/app/1867240/discussions/0/573807613531316134/','wdsdb':'https://steamcommunity.com/app/1867240/discussions/0/573807613531404462/','wdd':'https://steamcommunity.com/app/1867240/discussions/',
'bfdy':'https://steamcommunity.com/app/2807960/discussions/0/567051865431459136/','bfdead':'https://steamcommunity.com/app/2807960/discussions/0/567052214089182313/','bfbot':'https://steamcommunity.com/app/2807960/discussions/0/567052482018017646/','bfki':'https://steamcommunity.com/app/2807960/discussions/0/564794055139009742/','bfd':'https://steamcommunity.com/app/2807960/discussions/',
'cs710':'https://steamcommunity.com/app/730/discussions/0/563674774513916237/','csvac':'https://steamcommunity.com/app/730/discussions/0/591812126801193036/','csd':'https://steamcommunity.com/app/730/discussions/',
'tfch':'https://steamcommunity.com/app/2073850/discussions/0/571555813716494282/','tfbp':'https://steamcommunity.com/app/2073850/discussions/0/532101291506167186/','tfaw':'https://steamcommunity.com/app/2073850/discussions/0/571555813716420075/','tfd':'https://steamcommunity.com/app/2073850/discussions/',
'owsd':'https://steamcommunity.com/app/2357570/discussions/0/573807613531246471/',
'tgm':'https://www.thefinals.wiki/wiki/The_Grand_Major_2026','dh':'https://dreamhack.com/stockholm/?p=39618','d2':'https://www.dust2.us/news/80356/both-m80-and-wildcard-eliminated-from-pgl-major-singapore',
'ig':'https://insider-gaming.com/hunger-test-feedback-open-beta-change/','gp':'https://www.gamespress.com/HUNGER-Announces-Open-Beta-for-27-November-Ahead-of-Early-Access-Launc','mm':'https://mein-mmo.de/hunger-open-beta-und-ea-release-ankuendigung/2/',
'rw':'https://bbs.ruliweb.com/','rwh':'https://bbs.ruliweb.com/game/87435','api':'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=1867240'}

mast='''<body>
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
<span>기준일 <b>2026년 11월 28일 (토)</b></span>
<span class="cover-pill">커버기간: 11/27(금) – 11/28(토) 07시대</span>
<span>스팀·웹 07시대까지 수집</span>
</div>
</div>
</header>
<main id="main">
<div class="wrap">
'''
lead=f'<p class="lead">{B["lead"]}</p>\n'
notice=f'<div class="notice"><span class="k">신선도</span><span><b>스팀·인벤·루리웹·서든어택 공식은 데스크톱 내장 브라우저로 07시대에 열었습니다.</b>{LB}인벤 오버워치 목록은 ?p=1로 열었고 최신 글이 04:33입니다.{LB}핫벤과 아카라이브는 이번 판에서 열지 않았습니다.</span></div>\n'
kpis=('<div class="kpis" id="summary">'
 f'<div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">9건</div><div class="sub">{a(U["owev"],"꽃 신령 나흘째")}<span class="sep">·</span>{a(U["d2"],"CS2 Stage 2")}<span class="sep">·</span>{a(U["tgm"],"TGM26 이틀째")}</div></div>'
 f'<div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">서든어택 롤백 요구가 이틀째 이어집니다</div><div class="sub">공지 댓글이 <b>177개</b>로 늘었습니다. <a href="#risk">상세 보기</a></div></div>'
 f'<div class="kpi"><div class="lbl">신작 반응</div><div class="big">HUNGER 오픈 베타가 이틀째입니다</div><div class="sub">루리웹 신설 게시판 <b>5일째 1위</b>입니다. {a(store(1752080),"상점")}</div></div>'
 f'<div class="kpi"><div class="lbl">국내 포커스</div><div class="big">크로스파이어 CFS 2026 그룹 스테이지가 열렸습니다</div><div class="sub">총상금은 <b>143만 달러</b>입니다. {a(U["cfs"],"기사")}</div></div></div>\n')

def li(s,txt,win,today=False):
    cls={'on':'진행','start':'시작','end':'종료'}[s]
    return f'<li class="{"today" if today else ""}"><span class="s {s}">{cls}</span><span class="t">{txt}<span class="win">{win}</span></span></li>'
groups=[
 ('11.28 토',True,True,[('on','<b>오버워치 달빛 품은 꽃 신령</b> 나흘째입니다','~12/9 09시'),('on','<b>OWCS 응원 대회</b> 나흘째입니다','~12/8'),('on','<b>워독스 시즌 3</b> 17일째입니다','접속 61,824명'),('on','<b>오버워치 군림 이벤트</b> 25일째입니다','~12/8'),('on','<b>마블 IGNITE 그랜드 파이널</b> 6일째입니다','~11/29'),('on','<b>HUNGER 오픈 베타</b> 이틀째입니다','~11/29'),('on','<b>THE FINALS 그랜드 메이저</b> Phase 2를 치릅니다','결승 11/29'),('on','<b>CFS 2026 그룹 스테이지</b> 이틀째입니다','~11/29 우한'),('start','<b>CS2 메이저 Stage 2</b> 시작합니다','Dust2.us')]),
 ('11.29 일',False,True,[('end','<b>THE FINALS 그랜드 메이저</b> 결승이 열립니다','The Throne'),('end','<b>HUNGER 오픈 베타</b> 막을 내립니다','무료'),('end','<b>CFS 2026 그룹 스테이지</b> 끝납니다','인벤')]),
 ('11.30 월',False,False,[('start','<b>배그 운영정책 개정</b> 적용됩니다','11/23 공지')]),
 ('12.01 화',False,False,[('start','<b>IGDB 슈터 14건</b> 몰렸습니다','상점 2건 확인'),('end','<b>스팀 어워드 추천</b> 03시에 마감됩니다','PT 11/30 10시')]),
 ('12.02 수',False,False,[('start','<b>배그 아이브 외형 개선</b> PC에 적용됩니다','티켓 10장')]),
 ('12.03 목',False,False,[('start','<b>HUNGER</b> 앞서 해보기로 나옵니다','19시 KST'),('end','<b>TGM26 이벤트 패스</b> 판매가 끝납니다','공식 공지'),('start','<b>OWCS 월드 파이널</b> 방송 시작합니다','~12/7')]),
 ('12.04 금',False,False,[('start','<b>AGF 2026</b> 개막합니다','~12/6 킨텍스'),('start','<b>Cronos: Lazarus</b> 스팀에 나옵니다','IGDB 12/3')]),
 ('12.06 일',False,False,[('end','<b>CFS 2026 그랜드 파이널</b> 막을 내립니다','상금 143만 달러')]),
 ('12.08 화',False,False,[('start','<b>배틀필드 6 플래툰</b> 3단계로 예고됐습니다','EA 공지'),('end','<b>오버워치 군림 이벤트</b> 끝납니다','패치노트')]),
 ('12.09 수',False,False,[('end','<b>오버워치 달빛 품은 꽃 신령</b> 09시에 끝납니다','수령 기한 동일'),('start','<b>Guns of Eschaton</b> 스팀에 나옵니다','IGDB 12/8')]),
 ('2027년',False,False,[('end','<b>엑조프라이멀</b> 본편·DLC 3/31 10시 판매를 멈춥니다','재다운로드 가능'),('end','<b>엑조프라이멀</b> 9/30 서비스를 마칩니다','인벤 11/25')]),
]
total=sum(len(g[3]) for g in groups)
tl=[f'<div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>\n<div class="timeline">\n<h3>움직이는 일정 {total}건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/28)입니다.</p>']
for d,today,op,items in groups:
    dt='<span class="dg-t">오늘</span>' if today else ''
    tl.append(f'<details class="dgroup{" today" if today else ""}"{" open" if op else ""}>\n<summary><span class="dg-d">{d}</span>{dt}<span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">'+''.join(li(s,t,w,today) for s,t,w in items)+'</ol>\n</details>')
tl.append('</div>\n')
tl='\n'.join(tl)

def hero(url,k,rank,flag,gm,h3,under):
    m,n=NAME[k]
    return f'<a class="hero" href="{url}" {T}>\n<div class="shot" data-mono="{m}" data-name="{n}"><img src="{IMG[k]}" alt=""><span class="rank">{rank}</span><span class="flag n">{flag}</span><div class="over"><div class="gm">{gm}</div><h3>{h3}</h3></div></div>\n<div class="under">{under}</div>\n</a>'
heroes=('<div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n<section class="heroes">\n'
 +hero(U['ga'],'SA','01','롤백 요구','서든어택 · 넥슨','해상도 패치 반발 이틀째, 후속 공지 없음',B['02-1'])+'\n'
 +hero(U['wddead'],'WD','02','접속 +37%','워독스 · 시즌 3','접속은 늘고 "죽은 게임" 글도 늘어',B['02-2'])+'\n'
 +hero(U['bfbot'],'BF6','03','봇 로비','배틀필드 6 · 스팀 토론','접속 39% 반등 속 "봇 천지" 불만',B['02-3'])+'\n</section>\n')

def row(k,gname,sub,n,date,dsub,typ):
    return (f'<tr>\n<td><div class="g-cell">{thumb(k)}<span class="g-name">{gname}<em>{sub}</em></span></div></td>\n'
     f'<td class="ev2"><button class="e2" type="button" aria-expanded="false"><span class="d1">{B[n+"-d1"]}</span></button><span class="d2">{B[n+"-d2"]}</span></td>\n'
     f'<td>{date}<span class="dsub">{dsub}</span></td>\n<td><span class="typ">{typ}</span></td>\n<td>{B[n+"-반응"]}</td>\n</tr>')
TH='<thead><tr><th>게임</th><th>이벤트 / 업데이트</th><th>날짜</th><th>유형</th><th>커뮤니티 반응 · 관전 포인트</th></tr></thead>'
kr=('<div class="sec" id="kr"><span class="idx">03</span><h2>국내 포커스</h2><span class="rule"></span></div>\n'
 '<p class="sub-lead">국내 서비스·국내 배경 IP·국내 커뮤니티(<b>인벤·루리웹·아카라이브</b>) 반응 중심.</p>\n'
 '<div class="evkey"><b>근거 표기</b><span><span class="ev kr">KR·기사</span><span class="d">국내 매체</span></span><span><span class="ev gl">글로벌·기사</span><span class="d">해외 매체</span></span><span><span class="ev cm">커뮤니티</span><span class="d">원문 직접 확인</span></span><span><span class="ev of">공식</span><span class="d">공식 공지</span></span><span><span class="ev mt">지표</span><span class="d">수치</span></span><span><span class="ev na">국내 반응 미확인</span><span class="d">국내 소스 미확인</span></span></div>\n'
 '<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
 +row('SA','서든어택','해상도 반발 이틀째 · 넥슨','03-1','11/26~','후속 공지 없음','패치 · 여론')+'\n'
 +row('OW','오버워치2','메모리 제보 · 넥슨 클라이언트','03-2','11/26 21:11','조회 589회','결함 · 여론')+'\n'
 +row('CF','크로스파이어','CFS 2026 그랜드 파이널 · 스마일게이트','03-3','11/27~29','그룹 스테이지','대회')+'\n</tbody>\n</table></div>\n')
def ek(cls,lab,link,d):
    return f'<span><span class="ev {cls}">{lab}</span>{link}<span class="d">{d}</span></span>'
gl=('<div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>\n'
 '<p class="sub-lead">근거는 <b>스팀 커뮤니티 토론·리뷰 원문</b>과 <b>SiegeGG·Dot Esports·Liquipedia</b> 등 전문지, 그리고 공식 패치노트입니다.</p>\n'
 '<div class="evkey">\n<b>오늘 연 해외 커뮤니티</b>\n'
 +ek('cm','확인',a(U['wdd'],'워독스'),'상위 22건 · 방금 전부터 · 활성 주제 1,915건')+'\n'
 +ek('cm','확인',a(U['bfd'],'배틀필드 6'),'상위 16건 · 방금 전부터 · 활성 주제 1,168건')+'\n'
 +ek('cm','확인',a(U['tfd'],'THE FINALS'),'상위 16건 · 10분 전부터 · 활성 주제 535건')+'\n'
 +ek('cm','확인',a(U['csd'],'CS2'),'상위 16건 · 5분 전부터 · 활성 주제 1,501건')+'\n'
 +ek('cm','확인','','목록만: 오버워치2(317건) · PUBG(599건) · 에이펙스(556건) · 마블 라이벌즈(504건) · 델타포스(288건) · 시즈(245건) · 엑조프라이멀(263건)')+'\n'
 +ek('mt','확인','','스팀 Web API 현재 접속자 18종 · 07:35 한 번 · 스팀 상점 9종')+'\n'
 +ek('gl','매체만','','CS2 Stage 1 결과: Dust2.us · TGM26 일정: THE FINALS 위키')+'\n'
 +ek('na','제외','','HUNGER 토론은 스팀 콘텐츠 설정 확인 화면에 막혀 열지 못했습니다')+'\n'
 +ek('na','축 없음','','발로란트와 서든어택은 스팀 미등록')+'\n</div>\n'
 '<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
 +row('WD','워독스 (WARDOGS)','시즌 3 17일째 · 접속 반등','04-1','11/28','접속 +37%','치트 · 지표')+'\n'
 +row('BF6','배틀필드 6','봇 로비 · "죽은 게임" 논쟁','04-2','11/27~','토론 3건','여론 · 지표')+'\n'
 +row('CS2','Counter-Strike 2','PGL 메이저 Stage 1 종료','04-3','11/27','Stage 2 11/28','대회 · 치트')+'\n'
 +row('TF','THE FINALS','그랜드 메이저 이틀째','04-4','11/27~29','스톡홀름','대회 · 여론')+'\n</tbody>\n</table></div>\n')

def lrow(k,name,sub,tag,tagc,dt,dtem,mk,sig,links,grp=False):
    g=' class="grp"' if grp else ''
    return (f'<tr{g}>\n<td class="g"><div class="g-cell">{thumb(k)}<span class="g-name">{name}<em>{sub}</em></span></div></td>\n'
      f'<td><span class="tag {tagc}">{tag}</span></td>\n<td class="dt">{dt}<em>{dtem}</em></td>\n<td class="mk">{mk}</td>\n<td class="sig">{sig}</td>\n<td class="lk">{links}</td>\n</tr>')
launch=('<div class="sec" id="launch"><span class="idx">05</span><h2>신작 출시·발표</h2><span class="rule"></span></div>\n'
 '<p class="sub-lead">최근 나온 슈터와 곧 나올 슈터를 한 표에 모읍니다.</p>\n'
 '<div class="tablewrap launch"><table>\n<colgroup><col class="c-g"><col class="c-s"><col class="c-d"><col class="c-m"><col class="c-sig"><col class="c-l"></colgroup>\n'
 '<thead><tr><th>게임</th><th>상태</th><th>날짜</th><th>개발 · 배급</th><th>관심 신호</th><th>링크</th></tr></thead>\n<tbody>\n'
 +lrow('DK','DERELIKT','레트로 SF 호러 FPS','출시','t-new','11.14','해외 11.13 · 시차','Visuwyg','평가 <b>360개</b> 중 <b>85%</b>(전날 348개 85%) · 접속 <b>98명</b>(전날 69명) · 할인 10%',lk(store(3810510),'pc','스팀'))+'\n'
 +lrow('G8','GUNBOAT-8','해상 탄막 로그라이크 · 아레나 슈팅','출시','t-new','11.27','앞서 해보기 · IGDB 캐시 없음','Orange Acorn Games','평가 <b>7개</b>(점수 비공개, 전날 0개) · 접속 <b>39명</b>(전날 38명)',lk(store(4783980),'pc','스팀'))+'\n'
 +lrow('DE','Desert Echo','3인칭 아레나 슈팅 · 타워 디펜스','예정','t-live','12.01','IGDB 11.30','DevTraum GmbH','IGDB와 <b>1일</b> 차이 · 평가 0개',lk(store(4714830),'pc','스팀'))+'\n'
 +lrow('BFW','The Brave Few','2차대전 제병협동 슈팅','예정','t-live','12.01','IGDB 11.30','Indub','IGDB와 <b>1일</b> 차이 · 평가 0개',lk(store(4653750),'pc','스팀'))+'\n'
 +lrow('HG','HUNGER','1인칭 약탈 슈팅 · 오픈 베타 11.27~29','예정','t-live','12.03','19시 KST · 앞서 해보기','GOOD FUN CORP','CBT 최고 접속 <b>16,000명</b>(Insider Gaming) · 루리웹 신설 1위 <b>5일째</b> · 한국어 미지원',lk(store(1752080),'pc','스팀')+'<br>'+lk(U['ig'],'mail','정리 기사'))+'\n'
 +lrow('CL','Cronos: Lazarus','생존 공포 3인칭 슈팅','예정','t-live','12.04','IGDB 12.03','Bloober Team · PixelAnt Games','IGDB와 <b>1일</b> 차이 · 평가 0개',lk(store(4768180),'pc','스팀'))+'\n'
 +lrow('GE','Guns of Eschaton','웨스턴 소울라이크 FPS','예정','t-live','12.09','IGDB 12.08','Eschatology Entertainment','IGDB와 <b>1일</b> 차이 · 평가 0개',lk(store(3734220),'pc','스팀'))+'\n'
 +lrow('IG','12/1 IGDB 슈터 예정','Black Mesa: Classic·Dead Exodus 외','미확정','t-warn','12.01','IGDB 캐시 값','—','하루에 <b>14건</b>(전날 15건) · 2주 <b>32건</b> 중 상점 대조 <b>4건</b>, 모두 하루 차이','—',grp=True)+'\n'
 +'</tbody>\n</table></div>\n')

def obs(k):
    kk,body=B[k].split('|||')
    return f'<div class="obs"><button class="e2" type="button" aria-expanded="false">{kk}</button><span class="d2">{body}</span></div>'
def tcard(k,chips,gm,n,src):
    m,nm=NAME[k]
    ban=f'<span class="tbanner" data-mono="{m}" data-name="{nm}"><img src="{IMG[k]}" alt=""></span>'
    ch=''.join(f'<span class="tag {c}">{t}</span>' for t,c in chips)
    return f'<div class="tcard">\n{ban}\n<div class="tin">\n<div class="chips">{ch}</div>\n<div class="gm">{gm}</div>\n<h3>{B[n+"-h3"]}</h3><p>{B[n+"-p"]}</p>\n{obs(n+"-obs")}\n<div class="src">{src}</div>\n</div>\n</div>'
trend=('<div class="sec" id="trend"><span class="idx">06</span><h2>신작 동향</h2><span class="rule"></span></div>\n<div class="trend-grid">\n'
 +tcard('HG',[('오픈 베타 이틀째','t-live'),('한국어 미지원','t-warn')],'신작 예정 · HUNGER','06-1',' · '.join([a(store(1752080),'HUNGER 상점'),a(U['ig'],'Insider Gaming 베타 정리'),a(U['gp'],'오픈 베타 보도자료'),a(U['rw'],'루리웹 신설 게시판')]))+'\n'
 +tcard('CL',[('12/1 14건','t-warn'),('상점 대조 4건','t-live')],'12월 첫 주 · IGDB 캐시','06-2',' · '.join([a(store(4714830),'Desert Echo 상점'),a(store(4653750),'The Brave Few 상점'),a(store(4768180),'Cronos: Lazarus 상점'),a(store(3734220),'Guns of Eschaton 상점')]))+'\n'
 +tcard('G8',[('출시 이틀째','t-new'),('평가 7개','t-warn')],'신작 출시 · GUNBOAT-8','06-3',a(store(4783980),'GUNBOAT-8 상점'))+'\n</div>\n')

def risk(cls,lvl,n):
    c=' '+cls if cls else ''
    return (f'<article class="risk{c}"><div class="lvl">{lvl}</div><h3>{B[n+"-h3"]}</h3>'
     f'<div class="row"><span class="k">무엇이</span><span>{B[n+"-무엇이"]}</span></div><div class="row"><span class="k">맥락</span><span>{B[n+"-맥락"]}</span></div>'
     f'<div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B[n+"-교훈"]}</ol></div></article>')
riskh=('<div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>\n'
 +risk('high','HIGH · 화면 개편 반발','07-1')+risk('','MID · 접속 반등 속 이탈 논쟁','07-2')+'\n')
act=('<div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>\n'
 +''.join(f'<article class="act"><div class="num">{i}</div><div><h3>{B[f"08-{i}-h3"]}</h3><p>{B[f"08-{i}-p"]}</p></div></article>' for i in (1,2))+'\n')
cv=[('방법','11/28 07시대에 데스크톱 내장 브라우저로 읽었습니다.','토론 수치는 목록 첫 페이지 상위 글에서 셌습니다.'),
    ('측정','동시 접속은 스팀 Web API로 07:35에 한 번 잰 값입니다.','미국 블랙 프라이데이 저녁과 겹쳐 반등 폭을 추세로 보지 않았습니다.'),
    ('일정','IGDB 캐시는 11/27 09:20 갱신본을 썼습니다.','상점과 맞춘 4건이 모두 하루씩 어긋났습니다.'),
    ('미확인','CS2 결정전 Lynn Vision과 HEROIC 결과는 확인하지 못했습니다.','CFS 국내 커뮤니티 반응은 열람하지 않았습니다.'),
    ('차단','HUNGER 스팀 토론은 콘텐츠 설정 확인 화면 때문에 못 열었습니다.','인벤 이미지는 외부 로드가 막혀 크로스파이어는 타일로 뒀습니다.'),
    ('출처','40만→6만 명, 90% 이탈은 이용자 주장입니다.','SteamDB 원자료와 대조하지 않고 그대로 옮겼습니다.')]
caveat='<div class="caveat">\n<span class="k">유의사항</span>\n'+''.join(f'<span class="crow"><b class="ck">{k}</b><span>{x}{LB}{y}</span></span>' for k,x,y in cv)+'\n</div>\n'
srcs=[('스팀 토론',[(U['wdcw'],'워독스 치터가 이겼다 글'),(U['wddead'],'워독스 게임 죽었다 글'),(U['wdsdb'],'워독스 SteamDB 예측 글'),(U['wdd'],'워독스 토론'),(U['bfdy'],'배틀필드 6 죽어 가나 글'),(U['bfdead'],'배틀필드 6 이 게임 죽었나 글'),(U['bfbot'],'배틀필드 6 봇 글'),(U['bfki'],'배틀필드 6 알려진 문제 고정글'),(U['cs710'],'CS2 10판 중 7판 글'),(U['csvac'],'CS2 VAC 글'),(U['tfch'],'THE FINALS 치터 대책 글'),(U['tfbp'],'THE FINALS 옛 배틀패스 글'),(U['tfaw'],'THE FINALS 어워드 표 글'),(U['owsd'],'오버워치 하락 글')]),
 ('스팀 상점·지표',[(store(1867240),'워독스 상점'),(store(3810510),'DERELIKT 상점'),(store(4783980),'GUNBOAT-8 상점'),(store(4714830),'Desert Echo 상점'),(store(4653750),'The Brave Few 상점'),(store(1752080),'HUNGER 상점'),(store(4768180),'Cronos: Lazarus 상점'),(store(3734220),'Guns of Eschaton 상점'),(U['api'],'스팀 Web API 현재 접속자')]),
 ('공식',[(U['ga'],'서든어택 GM이야기 개선패치 7'),(U['sanl'],'서든어택 공지 목록'),(U['owev'],'오버워치 꽃 신령 이벤트')]),
 ('기사',[(U['d2'],'Dust2.us Stage 1 마지막 날'),(U['tgm'],'THE FINALS 위키 TGM26'),(U['dh'],'드림핵 스톡홀름'),(U['cfs'],'인벤 CFS 2026 플레이인'),(U['ig'],'Insider Gaming HUNGER 베타'),(U['gp'],'HUNGER 오픈 베타 보도자료'),(U['mm'],'mein-mmo HUNGER 일정')]),
 ('국내 커뮤니티',[(U['owmem'],'인벤 메모리 16GB 글'),(U['ownx'],'인벤 넥슨 업데이트 글'),(U['owstd'],'인벤 스타디움 글'),(U['owb'],'인벤 오버워치 자유게시판'),(U['sarb'],'서든어택 자유게시판 롤백 글'),(U['safont'],'서든어택 자유게시판 폰트 글'),(U['rw'],'루리웹 메인 신설 게시판'),(U['rwh'],'루리웹 HUNGER 게시판')])]
nsrc=sum(len(x[1]) for x in srcs)
sources=(f'<!-- 09 출처 -->\n<details class="sources" id="sources" open>\n<summary>출처 링크 {nsrc}건</summary>\n<div class="body">\n<ul>\n'
 +'\n'.join(f'<li><b>{h}</b>'+' · '.join(a(u,t) for u,t in L)+'</li>' for h,L in srcs)
 +'\n</ul>\n<div class="colophon">\n<b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.142<br>\n모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n</div>\n</div>\n</details>\n</div>\n')
html=head+mast+lead+notice+kpis+tl+'\n'+heroes+kr+gl+launch+trend+riskh+act+caveat+sources+tail
open(OUT,'w',encoding='utf-8').write(html)
print('ok',len(html),total,nsrc)
