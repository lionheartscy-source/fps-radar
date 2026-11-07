import json,re,sys,os
R=os.environ['HOME']+'/mnt/fps-radar'
prev=open(R+'/reports/2026-11/FPS레이더_2026-11-07.html',encoding='utf-8').read()
head=prev[:prev.index('</head>')+7]
tail=prev[prev.index('</main>'):]
th=json.load(open(R+'/assets/thumbs.json',encoding='utf-8'))['games']
def U(k): return th[k]['url']
OW=U('오버워치2');WD=U('워독스 (WARDOGS)');MR=U('마블 라이벌즈');MYC=U('마이코펑크 (Mycopunk)');SUL=U('Sulfur');BF=U('배틀필드 6 · REDSEC');AP=U('에이펙스 레전드')
def thumb(m,n,u=None):
    if u: return f'<span class="thumb" data-mono="{m}" data-name="{n}"><img src="{u}" alt=""></span>'
    return f'<span class="thumb noimg" data-mono="{m}" data-name="{n}"></span>'
def ev(*k):
    L={'cm':'커뮤니티','mt':'지표','of':'공식','kr':'KR·기사','na':'국내 반응 미확인'}
    return '<span class="evrow">'+''.join(f'<span class="ev {x}">{L[x]}</span>' for x in k)+'</span>'
def src(u,t): return f'<span class="src-inline"><a href="{u}" target="_blank" rel="noopener">{t}</a></span>'
def row(m,n,u,name,gem,d1,d2,dt,dsub,typ,badges,react,link):
    return f'''<tr>
<td><div class="g-cell">{thumb(m,n,u)}<span class="g-name">{name}<em>{gem}</em></span></div></td>
<td class="ev2"><button class="e2" type="button" aria-expanded="false"><span class="d1">{d1}</span></button><span class="d2">{d2}</span></td>
<td>{dt}<span class="dsub">{dsub}</span></td>
<td><span class="typ">{typ}</span></td>
<td>{ev(*badges)} <span class="lb"></span>{react}{link}</td>
</tr>
'''
def A(u,t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
SV={'pc':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg>',
'home':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2 7.1 8 2.3l6 4.8v6.2a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/><path d="M6.3 14.3V9.7h3.4v4.6"/></svg>'}
def lk(u,ic,t): return f'<a href="{u}" target="_blank" rel="noopener">{SV[ic]}<span>{t}</span></a>'
def lrow(m,n,u,name,em,tag,tagc,dt,dtem,mk,sig,link,grp=False):
    return f'''<tr{' class="grp"' if grp else ''}>
<td class="g"><div class="g-cell">{thumb(m,n,u)}<span class="g-name">{name}<em>{em}</em></span></div></td>
<td><span class="tag {tagc}">{tag}</span></td>
<td class="dt">{dt}<em>{dtem}</em></td>
<td class="mk">{mk}</td>
<td class="sig">{sig}</td>
<td class="lk">{link}</td>
</tr>
'''
steamWD='https://store.steampowered.com/app/1867240/?l=koreana'
EA='https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-community-update-more-to-season-5'
OWN='https://overwatch.blizzard.com/ko-kr/news/patch-notes/live/2026/11/'
LEAD='''<p class="lead"><span class="lrow hi"><b class="lk">핵심</b><span class="lt"><b>고정글을 뺀 워독스 토론 첫 12건에 달린 답글은 합계 245개이고 최다 글은 69개입니다.</b></span></span><span class="lrow"><b class="lk">스팀</b><span class="lt">접속 64,000명을 내건 제목에 의견이 <b>51개</b> 달렸습니다.<span class="lb"></span>열감지 글 2건에는 각각 <b>28개</b>와 <b>12개</b>가 붙었습니다.</span></span><span class="lrow"><b class="lk">국내</b><span class="lt">핫벤 상위 30위에서 슈터 글은 0건이었습니다.<span class="lb"></span>인벤 오버워치 쪽은 최다 595회 읽혔습니다.</span></span><span class="lrow"><b class="lk">방법</b><span class="lt">11/8 07시대에 썼고 핫벤은 11-06 기준입니다.<span class="lb"></span>상점 값은 이틀째 변동이 없어 지표에서 제외했습니다.<span class="lb"></span>THE FINALS·마이코펑크 목록은 11/7 판과 같아 뺐습니다.</span></span></p>'''
H=[('01','답글 69개','워독스 · 스팀 토론','12건 답글 합계 245개, 최다 69개','활성 주제 1,910건 중 고정글을 빼면 12건이 보였습니다.<span class="lb"></span>6분 전 올라온 글이 <b>69개</b>로 가장 많은 답글을 모았습니다.<span class="lb"></span>저녁 접속 64,000명을 내건 제목에 <b>51개</b>가 달렸습니다.<span class="lb"></span>12건을 모두 더하면 의견 합계가 <b>245개</b>에 이릅니다.','https://steamcommunity.com/app/1867240/discussions/','WD','WARDOGS',WD),
('02','댓글 11개','오버워치 · 인벤 자유게시판','스블 콜라보 디바 스킨, 댓글 11개 최다','최다 댓글은 "스블 콜라보 디바 스킨에"로 <b>11개</b>였습니다.<span class="lb"></span>"독트린 뭐임?"은 조회 <b>389회</b>에 답글 5개가 붙었습니다.<span class="lb"></span>"넥슨은 진짜 실시간 밴 없는거임???"은 <b>312회</b> 읽혔습니다.<span class="lb"></span>독트린 제목은 40건 중 4건이고 답글 합계는 <b>6개</b>입니다.','https://www.inven.co.kr/board/overwatch/4538','OW','OVERWATCH 2',OW),
('03','답글 22개','마블 라이벌즈 · 스팀 토론','탱커 글 22개 &gt; 봇 매치 글 17개','활성 주제는 591건이고 목록에는 10건이 보였습니다.<span class="lb"></span>탱커 이용자를 두고 쓴 5분 전 글에 <b>22개</b>가 달렸습니다.<span class="lb"></span>봇 매치를 다룬 1시간 전 게시물에는 <b>17개</b>가 붙었습니다.','https://steamcommunity.com/app/2767030/discussions/','MR','MARVEL RIVALS',MR)]
heroes='<section class="heroes">\n'+''.join(f'''<a class="hero" href="{u}" target="_blank" rel="noopener">
<div class="shot" data-mono="{m}" data-name="{n}"><img src="{img}" alt=""><span class="rank">{r}</span><span class="flag n">{fl}</span><div class="over"><div class="gm">{gm}</div><h3>{h3}</h3></div></div>
<div class="under">{ev('cm','mt')} {un}</div>
</a>
''' for r,fl,gm,h3,un,u,m,n,img in H)+'</section>'
KR=[row('HV','인벤 핫벤',None,'인벤 핫벤','핫벤 11-06 기준','상위 30위에 슈터 글이 한 건도 없었습니다.','30건 모두 11-06 작성이라 하루 전 값일 수 있습니다.<span class="lb"></span>슈터 글은 0건이고 로스트아크 글이 22건을 차지했습니다.<span class="lb"></span>나머지는 LoL 4건, 메이플스토리 3건, WoW 1건입니다.','11/8','30위까지','순위 · 국내 반응',['mt'],'<b>① 장르</b> 30위 안에 슈터 글이 한 건도 없었습니다.<span class="lb"></span>기준일이 11-06이라 하루 전 값일 수 있습니다.<span class="lb"></span><b>② 상위권</b> 1위는 LoL이고 1.1만 회 읽혔으며 댓글이 30개입니다.<span class="lb"></span>로스트아크 8주년 방송 글은 2위로 조회 9.4만에 의견 70개가 붙었습니다.<span class="lb"></span><b>③ 오버워치</b> 관련 항목은 174위에서만 보였습니다.<span class="lb"></span>조회 238회에 의견 4개가 붙었습니다.',src('https://hot.inven.co.kr','인벤 핫벤')),
row('OW','OVERWATCH 2',OW,'오버워치2','인벤 자유게시판','"힐유저인데"로 시작하는 글이 595회 읽혔습니다.','11/8 05:05까지 앞쪽 40건 중 최다 조회는 595회입니다.<span class="lb"></span>댓글은 스블 콜라보 디바 스킨 글이 11개로 최다입니다.<span class="lb"></span>독트린 제목은 4건이고 OWCS·대회 제목도 4건입니다.','11/8','앞쪽 40건','게시판 · 국내 반응',['cm','mt'],'<b>① 화제</b> "힐유저인데"로 시작한 글은 추천 4개, 댓글 6개입니다.<span class="lb"></span>"독트린 뭐임?"은 389회 읽혔고 답글 5개가 달렸습니다.<span class="lb"></span>"이걸 티원이 결승을 가네"는 조회 359회에 댓글 4개입니다.<span class="lb"></span>"넥슨은 진짜 실시간 밴 없는거임???"은 312회 읽혔습니다.<span class="lb"></span><b>② 묶음</b> 독트린 제목은 40건 중 4건이고 댓글 합계는 6개입니다.<span class="lb"></span>OWCS·대회는 넷, PC방·넥슨은 셋을 차지했습니다.<span class="lb"></span>패스 제목 4건 중 "군림 패스 끗~"은 추천 4개입니다.<span class="lb"></span><b>③ 작성자</b> 닉네임 Venture 한 사람이 40건 중 10건을 썼습니다.<span class="lb"></span>이 글들에 달린 의견은 모두 1개 이하입니다.<span class="lb"></span>"❤️옵치하면서 친구 만드실 분!❤️"은 조회 133회입니다.<span class="lb"></span>서버 모집 제목은 130회 읽혔습니다.',src('https://www.inven.co.kr/board/overwatch/4538','인벤 오버워치 자유게시판')),
row('RW','루리웹 신설 게시판',None,'루리웹 신설 게시판','루리웹 신설 14종','신설 게시판 14종이 나흘째 같은 차례입니다.','차례가 11/5·11/6·11/7 판과 같아 나흘째 이어졌습니다.<span class="lb"></span>마이코펑크는 스팀 슈터로 1.0이 10/20에 나왔습니다.<span class="lb"></span>나머지 13종은 갈래 정보가 없고 글 수도 확인하지 않았습니다.','11/8','신설 14종','게시판 · 국내 반응',['mt'],'<b>① 변동</b> 11/8 목록도 11/5·11/6·11/7 판과 순서가 같습니다.<span class="lb"></span>나흘째 이어진 차례여서 변화가 없었습니다.<span class="lb"></span><b>② 명단</b> 앞쪽은 마이코펑크, 쟈오훈, 다크스웜, 몬스터 헌터 아웃랜더스입니다.<span class="lb"></span>이어서 워해머 서바이버즈, 쁘띠플래닛, 드레드무어, 그라브하운즈, 실버 파인즈입니다.<span class="lb"></span>끝은 파밍 캠프, 아노말리스, 원피스 그랜드 레스토랑, 스튜피드 네버 다이즈, 레인98입니다.<span class="lb"></span><b>③ 장르</b> 마이코펑크는 스팀 슈터이고 1.0이 10/20에 출시됐습니다.<span class="lb"></span>나머지 13종은 갈래 정보가 없습니다.<span class="lb"></span>게시판별 글 수와 조회수는 열어보지 않았습니다.',src('https://bbs.ruliweb.com/','루리웹 메인'))]
GL=[row('WD','WARDOGS',WD,'워독스 (WARDOGS)','열감지 논쟁 집중','열감지 제목 두 건에 답글 40개가 달렸습니다.','활성 주제는 1,910건이고 이 중 12건을 읽었습니다.<span class="lb"></span>모두 1시간 안에 올라왔고 답글은 합계 245개입니다.<span class="lb"></span>상점 평가는 11/7 판과 이틀째 같아 기준에서 뺐습니다.','11/8','첫 12건','품질 · 토론',['cm','mt'],'<b>① 논쟁</b> "Thermals, Yes or No?"는 열감지 찬반을 묻습니다. 방금 전 올라왔고 <b>답글 28개</b>가 달렸습니다. 두 번째는 "Thermals Make Late Wipe Miserable"이고 2분 전 글입니다. 열감지 탓에 와이프 후반이 괴롭다는 뜻이며 의견 12개가 붙었습니다. 두 제목의 합계는 40개입니다.<span class="lb"></span><b>② 흥행 우려</b> 가장 큰 글은 "Another flop of a game due to DEI woke propaganda"입니다. DEI 선전 탓에 또 망한 게임이라는 뜻입니다. 6분 전 올라온 글에 <b>답글 69개</b>가 이어졌습니다. "64,000 PLAYERS ONLINE IN THE EVENING. STILL THINK EVERYTHING IS FINE?"도 있습니다. 저녁 접속자 6만 4천 명인데 괜찮다고 보느냐는 뜻입니다. 2분 전 글에 <b>51개</b>가 쌓였습니다. 두 글을 더하면 120개입니다.<span class="lb"></span><b>③ 제도 요구</b> "Revives have to be limited"는 부활을 제한해야 한다는 글입니다. 1시간 전 올라와 <b>답글 19개</b>가 붙었습니다. "cheaters gonna kill wardogs"(치터가 워독스를 죽일 것이다)에는 14개가 달렸습니다.',src('https://steamcommunity.com/app/1867240/discussions/','워독스 토론')),
row('MR','MARVEL RIVALS',MR,'마블 라이벌즈','매칭·봇 불만','매칭과 봇 제목 두 건에 답글 23개가 달렸습니다.','활성 주제는 591건이고 이 중 10건을 읽었습니다.<span class="lb"></span>2분 전부터 3시간 전까지 올라왔고 답글은 합계 62개입니다.<span class="lb"></span>패치 내용은 공식 노트를 열지 않아 단정하지 않습니다.','11/8','첫 10건','품질 · 토론',['cm','mt'],'<b>① 탱커 반응</b> 가장 큰 글은 "Tank players have such a massive victim complex"입니다. 방어 역할 이용자에게 피해의식이 크다고 말하는 제목입니다. 5분 전 올라온 글에 <b>답글 22개</b>가 붙었습니다.<span class="lb"></span><b>② 봇 매치</b> "Marvel Rivals has made bot matches even worse and refuses to remove them. Please spread the word."입니다. 글쓴이는 봇 매치가 더 나빠졌는데도 없애지 않는다며 알려 달라고 합니다. <b>답글 17개</b>가 달렸고 1시간 전에 올라왔습니다.<span class="lb"></span><b>③ 로비 불만</b> "Lol this game is so unbalanced you\'re getting thrown against full lobby stack"은 같은 시간대 글입니다. 꽉 찬 스택 로비와 붙는다며 게임이 불균형하다는 뜻입니다. 답글이 6개뿐이라 봇 매치 글보다 11개 적습니다. 두 제목을 더하면 23개로 탱커 반응 22개와 비슷합니다.',src('https://steamcommunity.com/app/2767030/discussions/','마블 라이벌즈 토론')),
row('APEX','APEX LEGENDS',AP,'에이펙스 레전드','서버·치트 제목','서버와 치트 제목 두 건에 답글 17개가 달렸습니다.','활성 주제는 483건이고 고정글 4개를 뺀 11건이 보입니다.<span class="lb"></span>17분 전부터 3시간 전까지 올라왔고 합계 답글은 22개입니다.<span class="lb"></span>버그 제보 두 건에는 각각 2개와 1개가 붙었습니다.','11/8','첫 11건','품질 · 토론',['cm','mt'],'<b>① 서버 불만</b> 가장 큰 글은 "Apex has the worst servers in gaming history for its scale..."입니다. 규모에 비해 서버가 게임 역사상 최악이라는 주장입니다. 1시간 전 글에 <b>답글 13개</b>가 달렸습니다.<span class="lb"></span><b>② 부정행위</b> "CLOSET CHEATERS"는 몰래 치트를 쓰는 이용자를 뜻합니다. 이 글에는 <b>4개</b>가 붙었습니다.<span class="lb"></span><b>③ 버그 제보</b> "A bug in the game. After scanning enemies, their locations remain on the mini-map."에는 답글 2개가 달렸습니다. 적을 스캔한 뒤에도 위치가 미니맵에 남는다는 제보입니다. "invisible walls at the storm site"는 17분 전 글이고 <b>답글 1개</b>가 붙었습니다. 스톰 사이트에 보이지 않는 벽이 있다는 뜻입니다.',src('https://steamcommunity.com/app/1172470/discussions/','에이펙스 토론')),
row('BF6','BATTLEFIELD 6',BF,'배틀필드 6 (BATTLEFIELD 6)','시즌 5 일정','시즌 5 2단계가 11/10에 열릴 예정입니다.','11/10 2단계에는 근접전 유럽 카지노 맵과 카지노 강탈 이벤트가 있습니다.<span class="lb"></span>멀티플레이어 리더보드와 밸런스 조정도 같은 날 들어옵니다.<span class="lb"></span>3단계는 12/8이고 서버 브라우저와 플래툰이 예정입니다.','11/8','공식 공지','일정 · 공식',['of'],'<b>① 밸런스</b> 2단계에서 SCW-10과 KV9의 확장 탄창이 약해집니다. 저사용 부속품은 반대로 강해집니다. Dead Space 콜라보 이벤트 Convergence는 11/10까지입니다.<span class="lb"></span><b>② 3단계 일정</b> 12/8에는 서버 브라우저가 매치메이킹과 병행됩니다. 플래툰과 블랙웰 필즈, 뉴 소벡 시티 맵 업데이트도 들어갑니다.<span class="lb"></span><b>③ 변경 가능성</b> 공지 상단에는 게시 이후 B-81 칼바리 차량과 플래툰 기능 지연이 발표됐다는 안내가 있습니다. 12/8 내용은 바뀔 수 있습니다. 11/10 날짜와 항목은 원문으로 확인했습니다.',src(EA,'EA 시즌 5 공지'))]
def card(m,n,u,chips,gm,h3,p,obs,srcs,c2='t-warn',c1='t-new'):
    c=chips.split('|')
    return f'''<div class="tcard">
<div class="tbanner" data-mono="{m}" data-name="{n}">{f'<img src="{u}" alt="">' if u else ''}</div>
<div class="tin">
<div class="chips"><span class="tag {c1}">{c[0]}</span><span class="tag {c2}">{c[1]}</span></div>
<div class="gm">{gm}</div>
<h3>{h3}</h3><p>{p}</p>
<div class="obs"><button class="e2" type="button" aria-expanded="false"><span class="k">관전 포인트</span></button><span class="d2">{obs}</span></div>
<div class="src">{srcs}</div>
</div>
</div>
'''
cards=card('WD','WARDOGS',WD,'앞서 해보기|불만 집중','신작 슈터 · 워독스','토론 1,910건에 불만 제목이 몰렸습니다.','스팀 토론 활성 주제가 <b>1,910건</b>으로 집계됐습니다.<span class="lb"></span>읽은 <b>12건</b>에 달린 답글이 합계 <b>245개</b>였습니다.<span class="lb"></span>앞서 해보기는 9/10 출시 후 <b>60일째</b>입니다.','상점 평가 값이 11/7 판과 똑같이 나왔습니다.<span class="lb"></span>최근 30일 <b>40,351개</b> 중 긍정은 <b>51%</b>였습니다.<span class="lb"></span>한국어 평가 <b>2,498개</b>에서는 호평이 <b>29%</b>에 그쳤습니다.',A('https://steamcommunity.com/app/1867240/discussions/','워독스 토론')+' · '+A(steamWD,'워독스 스팀 상점'))
cards+=card('MYC','MYCOPUNK',MYC,'값 동일|변화 없음','상점 값 · 마이코펑크·Sulfur','두 게임 상점 값이 11/7 판과 같았습니다.','마이코펑크는 전체 평가 <b>4,523개</b> 중 긍정이 <b>88%</b>입니다.<span class="lb"></span>최근 30일 <b>435개</b>로 좁히면 <b>82%</b>까지 내려갑니다.<span class="lb"></span>Sulfur는 한국어 <b>202개</b> 중 <b>81%</b>가 긍정입니다.','마이코펑크는 <b>10/20</b>에 1.0이 출시됐습니다.<span class="lb"></span>Sulfur도 <b>10/28</b>에 같은 버전을 냈습니다.<span class="lb"></span>값이 같아 오늘은 변화 지표로 쓰지 못했습니다.',A('https://store.steampowered.com/app/3247750/?l=koreana','마이코펑크 스팀 상점')+' · '+A('https://store.steampowered.com/app/2124120/?l=koreana','Sulfur 스팀 상점'),c1='t-live')
cards+=card('IGDB','IGDB 슈터 예정',None,'예정 12종|GTA VI','신작 일정 · IGDB 예정','11/10~13에 PC 슈터 12종이 예정됐습니다.','IGDB 캐시에 PC 슈터 <b>12종</b>이 잡혀 있습니다.<span class="lb"></span>11/10에는 <b>2종</b>으로 Deiity와 Rense가 나옵니다.<span class="lb"></span>11/11~13은 하루마다 <b>3종, 4종, 3종</b>입니다.','GTA VI는 <b>11/19</b> 출시로 복수 매체가 보도했습니다.<span class="lb"></span>로크스타 공식 페이지는 열어 보지 못한 상태입니다.<span class="lb"></span><b>12종</b> 모두 스팀 출시 날짜는 확인하지 못했습니다.','IGDB 캐시 · 상점 날짜 미확인',c1='t-live')
def risk(cls,lvl,h3,what,ctx,l):
    return f'<article class="{cls}"><div class="lvl">{lvl}</div><h3>{h3}</h3><div class="row"><span class="k">무엇이</span><span>{what}</span></div><div class="row"><span class="k">맥락</span><span>{ctx}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>'+''.join(f'<li>{x}</li>' for x in l)+'</ol></div></article>'
risks=risk('risk high','HIGH · 워독스 토론에 열감지와 흥행 불만이 몰렸습니다','읽은 12건에 답글 245개가 달렸습니다.','불만 글은 "Another flop of a game due to DEI woke propaganda"입니다.<span class="lb"></span>여기에는 의견이 <b>69개</b> 달려 가장 많았습니다.<span class="lb"></span>저녁 접속자 <b>64,000명</b>을 내세운 글에 <b>51개</b>가 붙었습니다.<span class="lb"></span>"Thermals, Yes or No?"에는 <b>28개</b>가 달렸습니다.<span class="lb"></span>이어 다른 열감지 글에도 <b>12개</b>가 쌓였습니다.','열감지 제목 2건에 달린 답글을 합치면 <b>40개</b>입니다.<span class="lb"></span>시즌 2는 <b>10/15</b>에 이미 시작한 상태입니다.<span class="lb"></span><b>11/12</b> 초기화 언급은 이전 판 토론 제목에서만 나왔습니다.<span class="lb"></span>이 날짜는 아직 공식으로 확인된 바가 없습니다.',['<b>분리</b> 해외 불만 글은 국내 공지 문구와 나눠 분류합니다.','<b>합산</b> 열감지 의견은 두 제목을 한 묶음으로 셉니다.','<b>보류</b> 초기화 언급은 공식 확인 전에 단정하지 않습니다.'])
risks+=risk('risk','MID · 마블 라이벌즈 토론에 매칭과 봇 불만이 보입니다','봇과 매칭 불만 제목이 23개를 모았습니다.','마블 라이벌즈 스팀 토론 활성 주제는 <b>591건</b>입니다.<span class="lb"></span>읽은 <b>10건</b>에 달린 의견을 모두 더하면 <b>62개</b>입니다.<span class="lb"></span>"Tank players have such a massive victim complex"에는 <b>22개</b>가 달렸습니다.<span class="lb"></span>봇 매치를 없애지 않는다고 지적한 제목에는 <b>17개</b>가 붙었습니다.<span class="lb"></span>매칭에서 상대 풀스택을 만난다는 글에는 <b>6개</b>가 달렸습니다.','읽은 <b>62개</b> 중 봇과 매칭 제목 2건이 <b>23개</b>를 차지합니다.<span class="lb"></span>탱커 이용자를 다룬 글도 <b>22개</b>로 비슷합니다.<span class="lb"></span>에이펙스 스팀 토론은 활성 <b>483건</b>입니다.<span class="lb"></span>서버 제목은 <b>13개</b>, 치트 제목은 <b>4개</b>입니다.',['<b>합산</b> 봇과 매칭 제목은 한 묶음으로 더해 셉니다.','<b>대상</b> 특정 역할을 겨냥한 글은 불만 글과 따로 봅니다.','<b>비교</b> 에이펙스 서버와 치트 제목은 별도로 기록해 둡니다.'])
def act(n,h,p): return f'<article class="act"><div class="num">{n}</div><div><h3>{h}</h3><p>{p}</p></div></article>'
acts=act(1,'워독스 불만 제목을 열감지·성능·치트로 나누고 초기화 공지를 확인하겠습니다.','읽은 <b>12건</b>의 답글을 더하면 합계가 <b>245개</b>입니다.<span class="lb"></span>"cheaters gonna kill wardogs"에는 <b>14개</b>가 달렸습니다.<span class="lb"></span><b>11/12</b> 초기화는 이전 판 제목에서만 나와 공지를 확인합니다.')+act(2,'인벤 오버워치 질문을 안내 문구 후보로 모으겠습니다.','11/8 05:05까지 앞쪽 <b>40건</b>을 읽었습니다.<span class="lb"></span>"넥슨은 진짜 실시간 밴 없는거임???"은 조회 <b>312회</b>에 댓글 <b>1개</b>입니다.<span class="lb"></span>"주말 pc방이벤트있잖여"는 <b>241회</b> 읽혔고 반응은 <b>5개</b>였습니다.')
def li(cls,s,tx,b,rest,win): return f'<li class="{cls}"><span class="s {s}">{tx}</span><span class="t"><b>{b}</b> {rest}<span class="win">{win}</span></span></li>'
def grp(d,items,today=False,op=False):
    dt='<span class="dg-t">오늘</span>' if today else ''
    return f'<details class="dgroup{" today" if today else ""}"{" open" if op else ""}>\n<summary><span class="dg-d">{d}</span>{dt}<span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">'+''.join(items)+'</ol>\n</details>\n'
td='today'
G=[grp('11.08 일',[li(td,'on','진행','오버워치 군림 이벤트','5일째입니다','11/4~12/8 · 블리자드 패치노트'),
li(td,'start','시작','디비전 2 센트럴 파크의 메아리','출시 6일째입니다','11/3 출시 · 11/7 판 이월'),
li(td,'on','진행','배틀필드 6 Dead Space 이벤트','20일째입니다','~11/10 · EA 공지'),
li(td,'on','진행','Sulfur 1.0','출시 12일째입니다','10/28 출시'),
li(td,'on','진행','마이코펑크 1.0','출시 20일째입니다','10/20 출시 · PC·PS5'),
li(td,'on','진행','워독스 시즌 2','25일째입니다','10/15 시작'),
li(td,'on','진행','서든어택 시즌4 문라이즈','이어집니다','~12/10 · 11/7 판 이월')],True,True),
grp('11.10 화',[li('','end','종료','배틀필드 6 Dead Space 이벤트','끝납니다','EA 공지'),li('','start','시작','배틀필드 6 시즌 5 2단계','시작합니다','유럽 카지노 맵 · EA 공지')],False,True),
grp('11.12 목',[li('','end','종료','서든어택 콤보 패스 시즌4','끝납니다','인벤 10/15 기사 · 이전 판 이월'),li('','start','시작','워독스 초기화 가능성','토론 제목에서 언급됐습니다','공식 확인 못함 · 이전 판 이월')]),
grp('11.19 목',[li('','start','시작','GTA VI','출시 예정으로 복수 매체가 보도했습니다','PS5·Xbox · 공식 미확인')]),
grp('11.20 금',[li('','start','시작','오버워치 정크랫의 전리품 사냥','열립니다','~11/24 · 주말 경험치 2배')]),
grp('11.25 수',[li('','start','시작','오버워치 OWCS 월드 파이널 응원 대회','시작합니다','~12/8 · 블리자드 패치노트')]),
grp('12.08 화',[li('','start','시작','배틀필드 6 서버 브라우저와 플래툰','3단계로 예고됐습니다','일부 지연 안내 · EA 공지'),li('','end','종료','오버워치 군림 이벤트','끝납니다','블리자드 패치노트')])]
timeline='<div class="timeline">\n<h3>움직이는 일정 16건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/8)입니다.</p>\n'+''.join(G)+'</div>'
rows05=lrow('WD','WARDOGS',WD,'워독스 (WARDOGS)','앞서 해보기 60일째','출시','t-new','09.10','한국어 상점은 09.11 표기','—','토론 활성 <b>1,910건</b> · 첫 12건 답글 <b>245개</b> · 한국어 <b>2,498개</b> 중 <b>29%</b>(11/7 판과 같은 값)',lk(steamWD,'pc','스팀'))
rows05+=lrow('MYC','MYCOPUNK',MYC,'마이코펑크 (Mycopunk)','정식 1.0 · PC·PS5','출시','t-new','10.20','앞서 해보기 종료','—','스팀 전체 <b>4,523개</b> 중 <b>88%</b> · 최근 30일 <b>435개</b>, <b>82%</b> · 11/7 판과 <b>같은 값</b>',lk('https://store.steampowered.com/app/3247750/?l=koreana','pc','스팀'))
rows05+=lrow('SUL','SULFUR',SUL,'Sulfur','1.0 · 앞서 해보기 종료','출시','t-new','10.28','상점 표기 2026.10.28','—','한국어 <b>202개</b> 중 <b>81%</b> · 최근 30일 <b>1,080개</b>, <b>80%</b> · 11/7 판과 <b>같은 값</b>',lk('https://store.steampowered.com/app/2124120/?l=koreana','pc','스팀'))
rows05+=lrow('BF6','BATTLEFIELD 6',BF,'배틀필드 6 시즌 5 2단계','유럽 카지노 맵 · 리더보드','예정','t-live','11.10','EA 공지','—','3단계는 <b>12/8</b>이나 플래툰 <b>지연 안내</b> · Dead Space 이벤트 <b>11/10</b> 종료',lk(EA,'home','공식'))
rows05+=lrow('GTA6','GTA VI',None,'GTA VI','PS5 · Xbox','미확정','t-warn','11.19','IGDB 캐시 값','—','복수 매체가 <b>11/19</b>로 보도 · 공식 페이지와 상점 날짜는 <b>확인 전</b>','—')
rows05+=lrow('OW','OVERWATCH 2',OW,'오버워치 정크랫의 전리품 사냥','주말 경험치 2배','예정','t-live','11.20','~11/24','—','군림 이벤트 <b>12/8</b>까지 · 월드 파이널 응원 대회 <b>11/25</b> 시작',lk(OWN,'home','공식'))
rows05+=lrow('IGDB','IGDB 슈터 예정',None,'11/10~11/13 IGDB 슈터 예정','Deiity 외 · PC','미확정','t-warn','11.10~13','IGDB 캐시 값','—','캐시에 <b>12종</b> · 11/12에 <b>4종</b>이 몰림 · <b>상점 날짜는 확인 전</b>','—',True)
rows05+=lrow('RW','루리웹 신설 게시판',None,'루리웹 신설 게시판 14종','마이코펑크 외 · 나흘째 같은 차례','발표','t-live','11.08','신설 14종','—','신설 <b>14종</b> 중 확인한 슈터는 마이코펑크 <b>1종</b> · 글 수는 <b>미확인</b>','—',True)
launch=f'''<div class="tablewrap launch"><table>
<colgroup><col class="c-g"><col class="c-s"><col class="c-d"><col class="c-m"><col class="c-sig"><col class="c-l"></colgroup>
<thead><tr><th>게임</th><th>상태</th><th>날짜</th><th>개발 · 배급</th><th>관심 신호</th><th>링크</th></tr></thead>
<tbody>
{rows05}</tbody>
  </table></div>'''
def kpi(cls,l,big,sub): return f'<div class="kpi{cls}"><div class="lbl">{l}</div><div class="big">{big}</div><div class="sub">{sub}</div></div>'
kpis='<div class="kpis" id="summary">'+kpi('','진행 중 시즌·이벤트','7건',A('https://steamcommunity.com/app/1867240/discussions/','워독스 시즌 2')+'<span class="sep">·</span>'+A(EA,'배틀필드 6 시즌 5')+'<span class="sep">·</span>'+A(OWN,'오버워치 군림'))+kpi(' risk','논란·리스크 신호','워독스 토론 최다 글에 답글 69개가 달렸습니다','열감지 제목 2건 합계는 <b>40개</b>입니다. <a href="#risk">상세 보기</a>')+kpi('','신작 반응','워독스 활성 주제는 1,910건입니다','읽은 12건 답글 합계는 <b>245개</b>입니다. '+A(steamWD,'스팀 상점'))+kpi('','국내 포커스','핫벤 30위 안에 슈터 글은 0건입니다','인벤 오버워치 최다 조회는 <b>595회</b>입니다')+'</div>'
notice='<div class="notice"><span class="k">캐시</span><span><b>스팀 상점 값 세 건과 THE FINALS·마이코펑크 토론 목록은 11/7 판과 같은 옛 값이라 이번 판 지표에서 뺐습니다.</b><span class="lb"></span>핫벤 30위는 모두 11-06 작성 글이었습니다.<span class="lb"></span>워독스와 마블 라이벌즈, 에이펙스 토론은 당일 값입니다.</span></div>'
evkey='''<div class="evkey">
<b>오늘 연 해외 커뮤니티</b>
<span><span class="ev cm">확인</span><a href="https://steamcommunity.com/app/1867240/discussions/" target="_blank" rel="noopener">워독스</a><span class="d">고정글 뺀 12건 · 방금 전~1시간 전 · 활성 주제 1,910건</span></span>
<span><span class="ev cm">확인</span><a href="https://steamcommunity.com/app/2767030/discussions/" target="_blank" rel="noopener">마블 라이벌즈</a><span class="d">고정글 뺀 10건 · 2분 전~3시간 전 · 활성 주제 591건</span></span>
<span><span class="ev cm">확인</span><a href="https://steamcommunity.com/app/1172470/discussions/" target="_blank" rel="noopener">에이펙스 레전드</a><span class="d">고정글 4개 뺀 11건 · 17분 전~3시간 전 · 활성 주제 483건</span></span>
<span><span class="ev mt">확인</span><span class="d">스팀 상점: 워독스·마이코펑크·Sulfur 모두 11/7 판과 같은 값</span></span>
<span><span class="ev na">옛 값</span><span class="d">THE FINALS와 마이코펑크 토론 첫 화면은 11/7 판과 같아 뺐습니다</span></span>
<span><span class="ev na">미열람</span><span class="d">레인보우 식스 시즈 · CS2 · 데스티니 2 · 디비전 2 · 아크 레이더스 토론</span></span>
<span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>
</div>'''
evkey03=re.search(r'<div class="evkey"><b>근거 표기</b>.*?</div>',prev,re.S).group(0)
def sec(i,id_,t): return f'<div class="sec" id="{id_}"><span class="idx">{i}</span><h2>{t}</h2><span class="rule"></span></div>'
tbl=lambda rows:'<div class="tablewrap"><table>\n<thead><tr><th>게임</th><th>이벤트 / 업데이트</th><th>날짜</th><th>유형</th><th>커뮤니티 반응 · 관전 포인트</th></tr></thead>\n<tbody>\n'+''.join(rows)+'</tbody>\n  </table></div>'
caveat='''<div class="caveat">
<span class="k">유의사항</span>
<span class="crow"><b class="ck">방법</b><span>인벤 오버워치 자유게시판은 11/8 05:05까지 당일 값입니다.<span class="lb"></span>목록에는 시각만 있어 날짜는 가리지 못했습니다.</span></span><span class="crow"><b class="ck">캐시</b><span>스팀 상점 세 건과 THE FINALS·마이코펑크 토론이 11/7 판과 같았습니다.<span class="lb"></span>핫벤은 11-06 기준입니다.</span></span><span class="crow"><b class="ck">미열람</b><span>레인보우 식스 시즈, CS2, 데스티니 2, 아카라이브는 열지 않았습니다.</span></span><span class="crow"><b class="ck">날짜</b><span>IGDB 캐시는 11/7 09:20에 갱신됐습니다.<span class="lb"></span>05 표의 IGDB 항목과 GTA VI는 상점 날짜를 대조하지 못했습니다.<span class="lb"></span>오버워치 이브 프로토콜 콜라보는 공식 노트에서 찾지 못해 뺐습니다.</span></span>
</div>'''
sources='''<!-- 09 출처 -->
  <details class="sources" id="sources" open>
    <summary>출처 링크 11건</summary>
    <div class="body">
      <ul>
<li><b>스팀 토론</b><a href="https://steamcommunity.com/app/1867240/discussions/" target="_blank" rel="noopener">워독스 토론</a> · <a href="https://steamcommunity.com/app/2767030/discussions/" target="_blank" rel="noopener">마블 라이벌즈 토론</a> · <a href="https://steamcommunity.com/app/1172470/discussions/" target="_blank" rel="noopener">에이펙스 토론</a></li>
<li><b>스팀 상점</b><a href="https://store.steampowered.com/app/1867240/?l=koreana" target="_blank" rel="noopener">워독스 스팀 상점</a> · <a href="https://store.steampowered.com/app/3247750/?l=koreana" target="_blank" rel="noopener">마이코펑크 스팀 상점</a> · <a href="https://store.steampowered.com/app/2124120/?l=koreana" target="_blank" rel="noopener">Sulfur 스팀 상점</a></li>
<li><b>공식</b><a href="https://overwatch.blizzard.com/ko-kr/news/patch-notes/live/2026/11/" target="_blank" rel="noopener">블리자드 11월 패치노트</a> · <a href="EAURL" target="_blank" rel="noopener">EA 시즌 5 공지</a></li>
<li><b>핫벤·인벤 오버워치·루리웹</b><a href="https://hot.inven.co.kr" target="_blank" rel="noopener">인벤 핫벤</a> · <a href="https://www.inven.co.kr/board/overwatch/4538" target="_blank" rel="noopener">인벤 오버워치 자유게시판</a> · <a href="https://bbs.ruliweb.com/" target="_blank" rel="noopener">루리웹 메인</a></li>
      </ul>
      <div class="colophon">
        <b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.122<br>
        모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)
      </div>
    </div>
  </details>
'''.replace('EAURL',EA)
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
      <span>기준일 <b>2026년 11월 8일 (일)</b></span>
      <span class="cover-pill">커버기간: 11/7(토) 오전 – 11/8(일) 오전</span>
      <span>스팀·웹 7시대까지 수집</span>
    </div>
  </div>
</header>

<main id="main">
<div class="wrap">
'''
sub03='  <p class="sub-lead">국내 서비스·국내 배경 IP·국내 커뮤니티(<b>인벤·루리웹·아카라이브</b>) 반응 중심.</p>\n  '+evkey03+'\n  '
sub04='  <p class="sub-lead">근거는 <b>스팀 커뮤니티 토론 원문</b>과 <b>스팀 상점 지표</b>, 공식 공지입니다.</p>\n'+evkey+'\n  '
body=mast+LEAD+'\n'+notice+'\n'+kpis+'\n'+sec('01','today','오늘의 일정')+'\n'+timeline+'\n'+sec('02','headline','오늘의 헤드라인')+'\n'+heroes+'\n'+sec('03','kr','국내 포커스')+'\n'+sub03+tbl(KR)+'\n\n'+sec('04','gl','글로벌 포커스')+'\n'+sub04+tbl(GL)+'\n\n'+sec('05','launch','신작 출시·발표')+'\n  <p class="sub-lead">최근 나온 슈터와 곧 나올 슈터를 한 표에 모읍니다.</p>\n  '+launch+'\n\n'+sec('06','trend','신작 동향')+'\n  <div class="trend-grid">\n'+cards+'</div>\n\n'+sec('07','risk','리스크 신호와 운영 교훈')+'\n'+risks+'\n\n'+sec('08','action','CM 액션 제안')+'\n'+acts+'\n\n'+caveat+'\n'+sources+'\n\n</div>\n\n\n'
html=head+'\n'+body+tail
for a,b in [('2026-11-07','2026-11-08'),('11월 7일','11월 8일')]:
    html=html.replace(a,b)
out=R+'/reports/2026-11/FPS레이더_2026-11-08.html'
open(out,'w',encoding='utf-8').write(html)
print(len(html))
