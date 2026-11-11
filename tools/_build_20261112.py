import json,re,os
R=os.environ['HOME']+'/mnt/fps-radar'
prev=open(R+'/reports/2026-11/FPS레이더_2026-11-11.html',encoding='utf-8').read()
head=prev[:prev.index('</head>')+7]
tail=prev[prev.index('</main>'):]
raw=open(os.environ['HOME']+'/w/blocks.txt',encoding='utf-8').read()
B={}
for m in re.finditer(r'===(\w+)===\n(.*?)(?=\n===\w+===)',raw,re.S): B[m.group(1)]=m.group(2).strip()
th=json.load(open(R+'/assets/thumbs.json',encoding='utf-8'))['games']
def U(k): return th[k]['url']
OW=U('오버워치2');WD=U('워독스 (WARDOGS)');MR=U('마블 라이벌즈');DF=U('델타포스');PUBG=U('배틀그라운드(PUBG)')
def thumb(m,n,u=None):
    if u: return f'<span class="thumb" data-mono="{m}" data-name="{n}"><img src="{u}" alt=""></span>'
    return f'<span class="thumb noimg" data-mono="{m}" data-name="{n}"></span>'
def row(m,n,u,name,gem,k,dt,dsub,typ):
    return f'''<tr>
<td><div class="g-cell">{thumb(m,n,u)}<span class="g-name">{name}<em>{gem}</em></span></div></td>
<td class="ev2"><button class="e2" type="button" aria-expanded="false"><span class="d1">{B[k+'_D1']}</span></button><span class="d2">{B[k+'_D2']}</span></td>
<td>{dt}<span class="dsub">{dsub}</span></td>
<td><span class="typ">{typ}</span></td>
<td>{B[k+'_REACT']}</td>
</tr>
'''
def A(u,t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
SV={'pc':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="2.5" width="13" height="9" rx="1.5"/><path d="M5.5 14h5M8 11.5V14"/></svg>',
'home':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2 7.1 8 2.3l6 4.8v6.2a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/><path d="M6.3 14.3V9.7h3.4v4.6"/></svg>',
'mail':'<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="3.3" width="13" height="9.4" rx="1.4"/><path d="m2.3 4.7 5.7 3.9 5.7-3.9"/></svg>'}
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
BF=U('배틀필드 6 · REDSEC');MYC=U('마이코펑크 (Mycopunk)');GTA=U('GTA VI')
sWD='https://store.steampowered.com/app/1867240/?l=koreana'
dWD='https://steamcommunity.com/app/1867240/discussions/'
nWD='https://steamcommunity.com/app/1867240/allnews/'
dMR='https://steamcommunity.com/app/2767030/discussions/'
MRB='https://www.gosugamers.net/entertainment/news/79489-all-marvel-rivals-season-11-buffs-and-nerfs-explained-new-patch-notes-revealed'
MRS='https://www.gosugamers.net/entertainment/news/79488-marvel-rivals-season-11-adds-strategist-nightcrawler-and-anniversary-events-with-2-500-free-units'
dBF='https://steamcommunity.com/app/2807960/discussions/'
nBF='https://steamcommunity.com/app/2807960/allnews/'
EAU='https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-2-1-2-0'
OWI='https://www.inven.co.kr/board/overwatch/4538'
HOT='https://hot.inven.co.kr'
KRP='https://www.krafton.com/news/press/%ED%81%AC%EB%9E%98%ED%94%84%ED%86%A4-%EC%A7%80%EC%8A%A4%ED%83%80-2026-%EC%B6%9C%ED%92%88%EC%9E%91-5%EC%A2%85-%EA%B3%B5%EA%B0%9C/'
INW='https://m.inews24.com/v/2022038'
PBI='https://www.inven.co.kr/board/battlegrounds/5046'
RMY='https://bbs.ruliweb.com/game/87426'
sMY='https://store.steampowered.com/app/3247750/?l=koreana'
oMY='https://www.mycopunkgame.com/'
GEM='https://www.gematsu.com/2026/11/ratchet-clank-ranger-rumble-canceled'
RSN='https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026'
OWN='https://overwatch.blizzard.com/ko-kr/news/patch-notes/live/2026/11/'
GI='https://gameinformer.com/2026/11/10/playstation-cancels-in-development-live-service-shooter-fairgames-at-jade-raymonds'
RUL='https://bbs.ruliweb.com/'
masthead=prev[prev.index('<body>'):prev.index('<main id="main">')]
masthead=masthead.replace('2026년 11월 11일 (수)','2026년 11월 12일 (목)').replace('커버기간: 11/10(화) 오전 – 11/11(수) 오후','커버기간: 11/11(수) 오후 – 11/12(목) 오전').replace('스팀·웹 15시대까지 수집','스팀·웹 07시대까지 수집')
assert '11월 12일' in masthead and '07시대' in masthead
notice='<div class="notice"><span class="k">신선도</span><span><b>스팀 웹 도구 응답이 11/11 판과 같은 옛 목록이라 모두 버렸습니다.</b><span class="lb"></span>스팀·인벤·루리웹은 데스크톱 내장 브라우저로 07시대에 다시 열었습니다.<span class="lb"></span>인벤 오버워치 목록의 최신 글은 07:13에 올라왔습니다.</span></div>'
kpis=f'<div class="kpis" id="summary"><div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">9건</div><div class="sub">{A(nBF,"배틀필드 6 카지노 하이스트")}<span class="sep">·</span>{A(OWN,"오버워치 군림")}<span class="sep">·</span>{A(nWD,"워독스 시즌 3 오늘 밤")}</div></div><div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">배틀필드 6 핵 제목 2건이 답글 114개를 모았습니다</div><div class="sub">첫 12건 답글 <b>225개</b>의 51%입니다. <a href="#risk">상세 보기</a></div></div><div class="kpi"><div class="lbl">신작 반응</div><div class="big">마이코펑크는 스팀 88%인데 루리웹 글은 1개입니다</div><div class="sub">전체 평가 <b>4,943개</b>입니다. {A(RMY,"루리웹 게시판")}</div></div><div class="kpi"><div class="lbl">국내 포커스</div><div class="big">인벤 오버워치 50건 중 19건이 6대6·탱커 글입니다</div><div class="sub">조회 합계 <b>3,938회</b>입니다</div></div></div>'
def li(s,lab,name,txt,win,today):
    return f'<li class="{"today" if today else ""}"><span class="s {s}">{lab}</span><span class="t"><b>{name}</b> {txt}<span class="win">{win}</span></span></li>'
G=[('11.13 금',True,[('start','시작','마블 라이벌즈 시즌 11 둠스데이','시작 예정으로 보도됐습니다','나이트크롤러 · 기사 기준')]),
('11.19 목',False,[('start','시작','GTA VI','출시됩니다','PS5·Xbox · Rockstar 뉴스와이어'),('start','시작','지스타 2026','부산 벡스코에서 열립니다','~11/22 · 크래프톤 5종 중 슈터 1종'),('start','시작','마블 라이벌즈 2주년 이벤트','시작 예정입니다','유닛 2,500개 · 기사 기준')]),
('11.20 금',False,[('start','시작','오버워치 정크랫의 전리품 사냥','열립니다','~11/24 · 주말 경험치 2배')]),
('11.21 토',False,[('end','종료','라쳇 &amp; 클랭: 레인저 럼블','상점에서 내려갑니다','서비스 종료 2027-05-01 · Gematsu')]),
('11.25 수',False,[('start','시작','오버워치 OWCS 월드 파이널 응원 대회','시작합니다','~12/8 · 블리자드 패치노트')]),
('12.08 화',False,[('start','시작','배틀필드 6 서버 브라우저와 플래툰','3단계로 예고됐습니다','플래툰 지연 안내 · EA 공지'),('end','종료','오버워치 군림 이벤트','끝납니다','블리자드 패치노트')])]
T=[('start','시작','워독스 시즌 3','22:00~24:00 점검 뒤 열립니다','Sabatulo 맵 · 공식 패치노트'),('on','진행','배틀필드 6 카지노 하이스트','이틀째입니다','11/11 시작 · 스팀 공식 소식'),('on','진행','오버워치 군림 이벤트','9일째입니다','11/4~12/8 · 블리자드 패치노트'),('on','진행','델타포스 시즌 오로라','사흘째입니다','11/10 시작 · 이전 판 이월'),('end','종료','서든어택 콤보 패스 시즌4','끝납니다','인벤 10/15 기사 · 이전 판 이월'),('on','진행','디비전 2 센트럴 파크의 메아리','출시 10일째입니다','11/3 출시 · 이전 판 이월'),('on','진행','Sulfur 1.0','출시 16일째입니다','10/28 출시 · 이전 판 이월'),('on','진행','마이코펑크 1.0','출시 23일째입니다','10/21 출시 · 스팀 상점'),('on','진행','서든어택 시즌4 문라이즈','이어집니다','~12/10 · 이전 판 이월')]
total=len(T)+sum(len(x[2]) for x in G)
tl=f'<div class="timeline">\n<h3>움직이는 일정 {total}건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/12)입니다.</p>\n'
tl+=f'<details class="dgroup today" open>\n<summary><span class="dg-d">11.12 목</span><span class="dg-t">오늘</span><span class="dg-n">{len(T)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,True) for x in T)+'</ol>\n</details>\n'
for d,op,items in G:
    tl+=f'<details class="dgroup"{" open" if op else ""}>\n<summary><span class="dg-d">{d}</span><span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,False) for x in items)+'</ol>\n</details>\n'
tl+='</div>\n'
H=[('01','패치노트','워독스 · 시즌 3 공식','시즌 3 패치노트, 토론 화제 51%가 시즌 변화',B['H1_UNDER'],nWD,'WD','WARDOGS',WD),
('02','6대6·탱커 19건','오버워치 · 인벤 자유게시판','6대6 시험 공지 이틀째, 탱커 삭제 글 687회',B['H2_UNDER'],OWI,'OW','OVERWATCH 2',OW),
('03','하향 20명','마블 라이벌즈 · 시즌 11','둠스데이 내일 개막, 전략가 치유·보호막 하향',B['H3_UNDER'],MRB,'MR','MARVEL RIVALS',MR)]
def shot(m,n,img):
    return f'<div class="shot{"" if img else " noimg"}" data-mono="{m}" data-name="{n}">'+(f'<img src="{img}" alt="">' if img else '')
heroes='<section class="heroes">\n'+''.join(f'''<a class="hero" href="{u}" target="_blank" rel="noopener">
{shot(m,n,img)}<span class="rank">{r}</span><span class="flag n">{fl}</span><div class="over"><div class="gm">{gm}</div><h3>{h3}</h3></div></div>
<div class="under">{un}</div>
</a>
''' for r,fl,gm,h3,un,u,m,n,img in H)+'</section>\n'
evkey3='<div class="evkey"><b>근거 표기</b><span><span class="ev kr">KR·기사</span><span class="d">국내 매체</span></span><span><span class="ev gl">글로벌·기사</span><span class="d">해외 매체</span></span><span><span class="ev cm">커뮤니티</span><span class="d">원문 직접 확인</span></span><span><span class="ev of">공식</span><span class="d">공식 공지</span></span><span><span class="ev mt">지표</span><span class="d">수치</span></span><span><span class="ev na">국내 반응 미확인</span><span class="d">국내 소스 미확인</span></span></div>'
TH='<thead><tr><th>게임</th><th>이벤트 / 업데이트</th><th>날짜</th><th>유형</th><th>커뮤니티 반응 · 관전 포인트</th></tr></thead>'
kr='<div class="sec" id="kr"><span class="idx">03</span><h2>국내 포커스</h2><span class="rule"></span></div>\n<p class="sub-lead">국내 서비스·국내 배경 IP·국내 커뮤니티(<b>인벤·루리웹·아카라이브</b>) 반응 중심.</p>\n'+evkey3+'\n<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
kr+=row('OW','OVERWATCH 2',OW,'오버워치2','6대6·탱커 논쟁','K1','11/12','최신 50건','모드 · 국내 반응')
kr+=row('PUBG','KRAFTON',PUBG,'크래프톤 · 지스타 2026','출품 5종 · 슈터 1종','K2','11/19','보도자료 10/20','행사 · 출품')
kr+=row('MYC','MYCOPUNK',MYC,'마이코펑크 (Mycopunk)','루리웹 신설 8일째','K3','11/12','게시판 글 1개','신작 · 국내 반응')
kr+='</tbody>\n</table></div>\n'
gl='<div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>\n<p class="sub-lead">근거는 <b>스팀 커뮤니티 토론·리뷰 원문</b>과 <b>SiegeGG·Dot Esports·Liquipedia</b> 등 전문지, 그리고 공식 패치노트입니다.</p>\n'
gl+=f'''<div class="evkey">
<b>오늘 연 해외 커뮤니티</b>
<span><span class="ev cm">확인</span>{A(dWD,"워독스")}<span class="d">고정글 뺀 28건 · 방금 전~1시간 전 · 활성 주제 1,910건</span></span>
<span><span class="ev cm">확인</span>{A(dMR,"마블 라이벌즈")}<span class="d">고정글 뺀 10건 · 방금 전~2시간 전 · 활성 주제 458건</span></span>
<span><span class="ev cm">확인</span>{A(dBF,"배틀필드 6")}<span class="d">고정글 뺀 12건 · 2분 전~1시간 전 · 활성 주제 1,640건</span></span>
<span><span class="ev mt">확인</span><span class="d">스팀 상점: 워독스·마이코펑크 당일 값</span></span>
<span><span class="ev gl">매체만</span><span class="d">마블 라이벌즈 시즌 11 밸런스: 해외 기사</span></span>
<span><span class="ev na">미열람</span><span class="d">레인보우 식스 시즈 · CS2 · 에이펙스 · 데스티니 2 · THE FINALS · 델타포스 토론</span></span>
<span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>
</div>
'''
gl+='<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
gl+=row('WD','WARDOGS',WD,'워독스 (WARDOGS)','시즌 3 패치노트','G1','11/12','첫 28건','시즌 · 토론')
gl+=row('MR','MARVEL RIVALS',MR,'마블 라이벌즈','시즌 11 밸런스','G2','11/13','첫 10건','밸런스 · 토론')
gl+=row('BF6','BATTLEFIELD 6 / REDSEC',BF,'배틀필드 6','카지노 하이스트','G3','11/11','첫 12건','이벤트 · 토론')
gl+='</tbody>\n</table></div>\n'
L=lrow('MYC','MYCOPUNK',MYC,'마이코펑크 (Mycopunk)','곰팡이 버스터즈 · 4인 협동','출시','t-new','10.21','상점 기준 · PC·PS5','Pigeons at Play · Devolver Digital','전체 <b>4,943개</b> 중 <b>88%</b> · 30일 <b>807개</b>, <b>86%</b> · 루리웹 글 <b>1개</b>',lk(sMY,'pc','스팀')+'<br>'+lk(oMY,'home','공식'))
L+=lrow('BF6','BATTLEFIELD 6 / REDSEC',BF,'배틀필드 6 카지노 하이스트','시즌 5 이벤트 · European Casino','출시','t-new','11.11','스팀 공식 소식','—','업데이트 공지 댓글 <b>721개</b> · 토론 활성 <b>1,640건</b> · 핵 글 답글 <b>106개</b>',lk(nBF,'pc','스팀')+'<br>'+lk(EAU,'home','공식'))
L+=lrow('WD','WARDOGS',WD,'워독스 시즌 3','Sabatulo · Limited Mode','예정','t-live','11.12','22:00~24:00 점검 뒤 · 공식','BULKHEAD · Team17','한국어 <b>2,715개</b> 중 <b>36%</b> · 30일 <b>69,417개</b>, <b>72%</b> · 토론 활성 <b>1,910건</b>',lk(nWD,'pc','스팀')+'<br>'+lk(sWD,'pc','상점'))
L+=lrow('MR','MARVEL RIVALS',MR,'마블 라이벌즈 시즌 11','둠스데이 · 나이트크롤러','예정','t-live','11.13','기사 기준','—','영웅 <b>29명</b> 조정(상향 9·하향 20) · 토론 활성 <b>458건</b>',lk(dMR,'pc','스팀')+'<br>'+lk(MRS,'mail','정리 기사'))
L+=lrow('GTA6','GTA VI',GTA,'GTA VI','PS5 · Xbox','예정','t-live','11.19','Rockstar 뉴스와이어','Rockstar Games','IGDB 캐시 날짜와 <b>일치</b> · 워독스 패치노트가 <b>직접 언급</b>',lk(RSN,'home','공식'))
L+=lrow('R&amp;C','RANGER RUMBLE',None,'라쳇 &amp; 클랭: 레인저 럼블','모바일 히어로 슈터 · 개발 중단','중단','t-warn','11.21','상점 내림 · 종료 27.05.01','Oh BiBi · 소니','11/6 발표 · 소프트 런칭 <b>6개국</b> 확대 뒤 중단 · IGDB <b>미등록</b>',lk(GEM,'mail','정리 기사'))
L+=lrow('GS','지스타 2026',None,'지스타 2026','부산 벡스코 · 크래프톤','예정','t-live','11.19~22','보도자료 10/20','—','크래프톤 <b>5종</b> 중 슈터 <b>1종</b> · 데드넷 <b>미출품</b> · 인벤 배그 언급 <b>0건</b>',lk(KRP,'home','공식')+'<br>'+lk(INW,'mail','정리 기사'),grp=True)
L+=lrow('IGDB','IGDB 슈터 예정',None,'11/12~11/26 IGDB 슈터 예정','Irreverence 외 · 소규모 다수','미확정','t-warn','11.12~26','IGDB 캐시 값','—','캐시에 <b>24종</b> · 11/12에 <b>8종</b>이 몰림 · 상점 대조 <b>1건</b> 일치','—',grp=True)
launch='<div class="sec" id="launch"><span class="idx">05</span><h2>신작 출시·발표</h2><span class="rule"></span></div>\n<p class="sub-lead">최근 나온 슈터와 곧 나올 슈터를 한 표에 모읍니다.</p>\n<div class="tablewrap launch"><table>\n<colgroup><col class="c-g"><col class="c-s"><col class="c-d"><col class="c-m"><col class="c-sig"><col class="c-l"></colgroup>\n<thead><tr><th>게임</th><th>상태</th><th>날짜</th><th>개발 · 배급</th><th>관심 신호</th><th>링크</th></tr></thead>\n<tbody>\n'+L+'</tbody>\n</table></div>\n'
def card(m,n,img,chips,gm,h3,k,src):
    tb=f'<div class="tbanner{"" if img else " noimg"}" data-mono="{m}" data-name="{n}">'+(f'<img src="{img}" alt="">' if img else '')+'</div>'
    o=B[k+'_OBS']; k1,d2=o.split('<span class="d2">',1)
    return f'''<div class="tcard">
{tb}
<div class="tin">
<div class="chips">{chips}</div>
<div class="gm">{gm}</div>
<h3>{h3}</h3><p>{B[k+'_P']}</p>
<div class="obs"><button class="e2" type="button" aria-expanded="false">{k1}</button><span class="d2">{d2}</div>
<div class="src">{src}</div>
</div>
</div>
'''
trend='<div class="sec" id="trend"><span class="idx">06</span><h2>신작 동향</h2><span class="rule"></span></div>\n<div class="trend-grid">\n'
trend+=card('WD','WARDOGS',WD,'<span class="tag t-new">시즌 3 당일</span><span class="tag t-warn">한국어 36%</span>','신작 슈터 · 워독스','한국어 긍정은 개막 전날까지 36%입니다','T1',A(sWD,'워독스 스팀 상점')+' · '+A(nWD,'시즌 3 패치노트'))
trend+=card('MYC','MYCOPUNK',MYC,'<span class="tag t-new">해외 88%</span><span class="tag t-warn">국내 글 1개</span>','국내외 격차 · 마이코펑크','스팀 호평에도 국내 게시판은 비어 있습니다','T2',A(sMY,'스팀 상점')+' · '+A(RMY,'루리웹 게시판'))
trend+=card('R&amp;C','RANGER RUMBLE',None,'<span class="tag t-warn">개발 중단</span><span class="tag t-live">소니 2종</span>','시장 신호 · 소니 라이브 서비스','나흘 사이 소니 계열 슈터 2종이 멈췄습니다','T3',A(GEM,'Gematsu')+' · '+A(GI,'Game Informer'))
trend+='</div>\n'
risk=f'''<div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>
<article class="risk high"><div class="lvl">HIGH · 핵 제목 2건이 답글의 51%입니다</div><h3>카지노 하이스트 첫날에도 핵 글이 맨 위입니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R1_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R1_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R1_LESSON']}</ol></div></article><article class="risk"><div class="lvl">MID · 마블 라이벌즈 하향 20명</div><h3>하향 20명 공지에 지원 역할 이탈 글이 나옵니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R2_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R2_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R2_LESSON']}</ol></div></article>
'''
action=f'''<div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>
<article class="act"><div class="num">1</div><div><h3>워독스 시즌 3 첫날 토론을 같은 기준으로 다시 셉니다</h3><p>{B['A1_P']}</p></div></article><article class="act"><div class="num">2</div><div><h3>오버워치 탱커 이탈 글을 FAQ 후보로 모읍니다</h3><p>{B['A2_P']}</p></div></article>
'''
caveat='''<div class="caveat">
<span class="k">유의사항</span>
<span class="crow"><b class="ck">방법</b><span>이번 판은 11/12 07시대에 데스크톱 내장 브라우저로 읽었습니다.<span class="lb"></span>인벤 50건은 11/11 11:51 글부터라 어제 판 목록과 일부 겹칩니다.</span></span><span class="crow"><b class="ck">캐시</b><span>웹 도구가 돌려준 워독스 토론·상점 값은 11/11 판과 같아 쓰지 않았습니다.</span></span><span class="crow"><b class="ck">정정</b><span>어제 판이 지스타 슈터 후보로 적은 데드넷은 확정 출품작에 없습니다.</span></span><span class="crow"><b class="ck">미열람</b><span>아카라이브와 레인보우 식스 시즈, CS2, 델타포스 토론은 열지 않았습니다.</span></span><span class="crow"><b class="ck">일정</b><span>IGDB 캐시는 11/10 09:20 갱신본이고 상점 대조 1건은 날짜가 맞았습니다.<span class="lb"></span>마블 라이벌즈 시즌 11 날짜는 기사 기준입니다.</span></span>
</div>
'''
S=[('스팀 토론',[(dWD,'워독스 토론'),(dMR,'마블 라이벌즈 토론'),(dBF,'배틀필드 6 토론')]),('스팀 상점·소식',[(sWD,'워독스 상점'),(sMY,'마이코펑크 상점'),(nWD,'워독스 시즌 3 패치노트'),(nBF,'배틀필드 6 소식')]),('공식',[(EAU,'EA 업데이트 2.1.2.0'),(KRP,'크래프톤 지스타 보도자료'),(RSN,'Rockstar 뉴스와이어'),(OWN,'블리자드 11월 패치노트')]),('기사',[(MRB,'GosuGamers 시즌 11 밸런스'),(MRS,'GosuGamers 시즌 11 개요'),(GEM,'Gematsu 레인저 럼블'),(INW,'아이뉴스24 크래프톤 부스'),(GI,'Game Informer 페어게임즈')]),('국내 커뮤니티',[(HOT,'인벤 핫벤'),(OWI,'인벤 오버워치 자유게시판'),(PBI,'인벤 배그 게시판'),(RUL,'루리웹 메인 신설 게시판'),(RMY,'루리웹 마이코펑크 게시판')])]
n=sum(len(x[1]) for x in S)
src=f'<!-- 09 출처 -->\n<details class="sources" id="sources" open>\n<summary>출처 링크 {n}건</summary>\n<div class="body">\n<ul>\n'+''.join(f'<li><b>{k}</b>'+' · '.join(A(u,t) for u,t in v)+'</li>\n' for k,v in S)+'</ul>\n<div class="colophon">\n<b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.126<br>\n모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n</div>\n</div>\n</details>\n</div>\n'
body='<main id="main">\n<div class="wrap">\n'+B['LEAD']+'\n'+notice+'\n'+kpis+'\n<div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>\n'+tl+'<div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n'+heroes+kr+gl+launch+trend+risk+action+caveat+src
h=head.replace('2026-11-11','2026-11-12').replace('11월 11일','11월 12일')
out=h+'\n'+masthead+body+tail
p=R+'/reports/2026-11/FPS레이더_2026-11-12.html'
open(p,'w',encoding='utf-8').write(out)
print(len(out), total, n)
