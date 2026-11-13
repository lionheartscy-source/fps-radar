import json,re,os
R=os.environ['HOME']+'/mnt/fps-radar'
prev=open(R+'/reports/2026-11/FPS레이더_2026-11-13.html',encoding='utf-8').read()
head=prev[:prev.index('</head>')+7]
tail=prev[prev.index('</main>'):]
raw=open(os.environ['HOME']+'/w/blocks.txt',encoding='utf-8').read()
B={}
for m in re.finditer(r'===(\w+)===\n(.*?)(?=\n===\w+===)',raw,re.S): B[m.group(1)]=m.group(2).strip()
th=json.load(open(R+'/assets/thumbs.json',encoding='utf-8'))['games']
def U(k): return th[k]['url']
OW=U('오버워치2');WD=U('워독스 (WARDOGS)');MR=U('마블 라이벌즈');PUBG=U('배틀그라운드(PUBG)');R6=U('레인보우 식스 시즈')
BF=U('배틀필드 6 · REDSEC');GTA=U('GTA VI');DK=U('DERELIKT')
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
sWD='https://store.steampowered.com/app/1867240/?l=koreana'
dWD='https://steamcommunity.com/app/1867240/discussions/'
dMR='https://steamcommunity.com/app/2767030/discussions/'
BEE='https://beebom.com/marvel-rivals-season-11-start-date/'
dBF='https://steamcommunity.com/app/2807960/discussions/'
pBFA='https://steamcommunity.com/app/2807960/discussions/0/738187822665741891/'
dR6='https://steamcommunity.com/app/359550/discussions/'
dCC='https://steamcommunity.com/app/4651830/discussions/'
FW='https://finalweapon.net/2026/11/13/ubisoft-is-reportedly-developing-a-new-rainbow-six-vegas-game/'
KOT='https://kotaku.com/overwatch-hudson-omnic-detective-damage-support-role-2000756631'
GOSU='https://www.gosugamers.net/entertainment/news/79497-overwatch-confirms-its-next-playable-hero-hudson-is-now-damage-not-support'
OWI='https://www.inven.co.kr/board/overwatch/4538'
HUD='https://www.inven.co.kr/board/overwatch/4538/5941460'
HOT='https://hot.inven.co.kr'
FN='https://fnnews.com/news/202611101703540636'
sDK='https://store.steampowered.com/app/3810510/?l=koreana'
PSL='https://www.playstationlifestyle.net/2026/11/13/derelikt-ps5-fps-release'
PX='https://www.purexbox.com/news/2026/11/13plus-xbox-games-are-releasing-today-including-a-retro-inspired-shooter-november-13'
RSN='https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026'
KRP='https://www.krafton.com/news/press/%ED%81%AC%EB%9E%98%ED%94%84%ED%86%A4-%EC%A7%80%EC%8A%A4%ED%83%80-2026-%EC%B6%9C%ED%92%88%EC%9E%91-5%EC%A2%85-%EA%B3%B5%EA%B0%9C/'
DLT='https://www.dailyt.co.kr/newsView/dlt202611110016'
OWN='https://overwatch.blizzard.com/ko-kr/news/patch-notes/live/2026/11/'
GEM='https://www.gematsu.com/2026/11/ratchet-clank-ranger-rumble-canceled'
RUL='https://bbs.ruliweb.com/'
masthead=prev[prev.index('<body>'):prev.index('<main id="main">')]
masthead=masthead.replace('2026년 11월 13일 (금)','2026년 11월 14일 (토)').replace('커버기간: 11/12(목) 오전 – 11/13(금) 오전','커버기간: 11/13(금) 오전 – 11/14(토) 오전')
assert '11월 14일' in masthead and '11/14(토) 오전' in masthead
notice='<div class="notice"><span class="k">신선도</span><span><b>스팀·인벤·루리웹은 데스크톱 내장 브라우저로 07시대에 열었습니다.</b><span class="lb"></span>워독스 토론 맨 위 글은 2분 전 시각이 찍혀 있었습니다.<span class="lb"></span>인벤 오버워치 목록의 최신 글은 03:42에 올라왔습니다.</span></div>'
kpis=f'<div class="kpis" id="summary"><div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">12건</div><div class="sub">{A(dMR,"마블 라이벌즈 시즌 11")}<span class="sep">·</span>{A(dWD,"워독스 시즌 3")}<span class="sep">·</span>{A(sDK,"DERELIKT 출시")}</div></div><div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">워독스 미니건 헬기 글 답글이 78개입니다</div><div class="sub">전날 15개에서 <b>다섯 배 넘게</b> 늘었습니다. <a href="#risk">상세 보기</a></div></div><div class="kpi"><div class="lbl">신작 반응</div><div class="big">DERELIKT 첫 평가 14개 중 85%가 긍정입니다</div><div class="sub">한국어는 <b>미지원</b>입니다. {A(sDK,"스팀 상점")}</div></div><div class="kpi"><div class="lbl">국내 포커스</div><div class="big">허드슨 공격 전환 글이 핫벤 1위입니다</div><div class="sub">인벤 조회는 <b>2,691회</b>입니다</div></div></div>'
def li(s,lab,name,txt,win,today):
    return f'<li class="{"today" if today else ""}"><span class="s {s}">{lab}</span><span class="t"><b>{name}</b> {txt}<span class="win">{win}</span></span></li>'
T=[('start','시작','DERELIKT','스팀 국내 상점에 나왔습니다','해외 11/13 · PS5·Xbox 동시'),('on','진행','마블 라이벌즈 시즌 11 둠스데이','이틀째입니다','11/13 개막 · 나이트크롤러'),('on','진행','워독스 시즌 3','사흘째입니다','11/12 밤 개막 · 공식 고정글'),('on','진행','배틀필드 6 서버 브라우저 1단계 시험','이틀째입니다','랩스 테스터 우선 · BFComms'),('on','진행','배틀필드 6 카지노 하이스트','나흘째입니다','11/11 시작 · 스팀 공식 소식'),('on','진행','오버워치 군림 이벤트','11일째입니다','11/4~12/8 · 블리자드 패치노트'),('on','진행','델타포스 시즌 오로라','5일째입니다','11/10 시작 · 이전 판 이월'),('on','진행','Toxic Commando 게임 패스','사흘째입니다','11/12 합류 · Pure Xbox'),('on','진행','디비전 2 센트럴 파크의 메아리','출시 12일째입니다','11/3 출시 · 이전 판 이월'),('on','진행','Sulfur 1.0','출시 18일째입니다','10/28 출시 · 이전 판 이월'),('on','진행','마이코펑크 1.0','출시 25일째입니다','10/21 출시 · 스팀 상점'),('on','진행','서든어택 시즌4 문라이즈','이어집니다','~12/10 · 이전 판 이월')]
G=[('11.19 목',True,[('start','시작','GTA VI','출시됩니다','PS5·Xbox · Rockstar 뉴스와이어'),('start','시작','지스타 2026','부산 벡스코에서 열립니다','~11/22 · 대형사 4곳 일반 전시 불참'),('start','시작','마블 라이벌즈 2주년 이벤트','시작 예정입니다','유닛 2,500개 · 기사 기준')]),
('11.20 금',False,[('start','시작','오버워치 정크랫의 전리품 사냥','열립니다','~11/24 · 주말 경험치 2배')]),
('11.21 토',False,[('end','종료','라쳇 &amp; 클랭: 레인저 럼블','상점에서 내려갑니다','서비스 종료 2027-05-01 · Gematsu')]),
('11.25 수',False,[('start','시작','오버워치 OWCS 월드 파이널 응원 대회','시작합니다','~12/8 · 블리자드 패치노트')]),
('12.08 화',False,[('start','시작','배틀필드 6 서버 브라우저와 플래툰','3단계로 예고됐습니다','플래툰 지연 안내 · EA 공지'),('end','종료','오버워치 군림 이벤트','끝납니다','블리자드 패치노트')]),
('12월 · 날짜 미정',False,[('start','시작','오버워치 허드슨','시즌 6에 공격 영웅으로 합류합니다','55번째 영웅 · Kotaku')])]
total=len(T)+sum(len(x[2]) for x in G)
tl=f'<div class="timeline">\n<h3>움직이는 일정 {total}건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/14)입니다.</p>\n'
tl+=f'<details class="dgroup today" open>\n<summary><span class="dg-d">11.14 토</span><span class="dg-t">오늘</span><span class="dg-n">{len(T)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,True) for x in T)+'</ol>\n</details>\n'
for d,op,items in G:
    tl+=f'<details class="dgroup"{" open" if op else ""}>\n<summary><span class="dg-d">{d}</span><span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,False) for x in items)+'</ol>\n</details>\n'
tl+='</div>\n'
H=[('01','핫벤 1위','오버워치2 · 신규 영웅','허드슨, 지원가 대신 공격으로 합류',B['H1_UNDER'],HUD,'OW','OVERWATCH 2',OW),
('02','제재 66개','마블 라이벌즈 · 시즌 11','개막 다음 날 채팅 제재 불만이 몰려',B['H2_UNDER'],dMR,'MR','MARVEL RIVALS',MR),
('03','보도','레인보우 식스 · 베가스','베가스 신작 개발 보도, 시즈 포럼은 조용',B['H3_UNDER'],FW,'R6','RAINBOW SIX',R6)]
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
kr+=row('OW','OVERWATCH 2',OW,'오버워치2','신규 영웅 허드슨','K1','11/13','역할 전환 공개','영웅 · 국내 반응')
kr+=row('PUBG','PUBG',PUBG,'배틀그라운드(PUBG)','저용량 모바일 2종','K2','11/10','실적 콘퍼런스콜','발표 · 신흥시장')
kr+='</tbody>\n</table></div>\n'
gl='<div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>\n<p class="sub-lead">근거는 <b>스팀 커뮤니티 토론·리뷰 원문</b>과 <b>SiegeGG·Dot Esports·Liquipedia</b> 등 전문지, 그리고 공식 패치노트입니다.</p>\n'
gl+=f'''<div class="evkey">
<b>오늘 연 해외 커뮤니티</b>
<span><span class="ev cm">확인</span>{A(dWD,"워독스")}<span class="d">고정글 뺀 47건 · 2분 전~1시간 전 · 활성 주제 1,912건</span></span>
<span><span class="ev cm">확인</span>{A(dMR,"마블 라이벌즈")}<span class="d">고정글 뺀 45건 · 11분 전부터 · 활성 주제 479건</span></span>
<span><span class="ev cm">확인</span>{A(dBF,"배틀필드 6")}<span class="d">고정글 뺀 47건 · 13분 전~10시간 전 · 활성 주제 1,500건</span></span>
<span><span class="ev cm">확인</span>{A(dR6,"레인보우 식스 시즈")}<span class="d">고정글 뺀 47건 · 55분 전부터 · 활성 주제 259건</span></span>
<span><span class="ev cm">확인</span>{A(dCC,"신더시티")}<span class="d">활성 주제 62건 · 자막 요청 답글 233개</span></span>
<span><span class="ev mt">확인</span><span class="d">스팀 상점: 워독스·DERELIKT 당일 값</span></span>
<span><span class="ev gl">매체만</span><span class="d">허드슨 역할 전환 · 베가스 신작 보도: 해외 기사</span></span>
<span><span class="ev na">미열람</span><span class="d">CS2 · 에이펙스 · 데스티니 2 · THE FINALS · 델타포스 토론</span></span>
<span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>
</div>
'''
gl+='<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
gl+=row('WD','WARDOGS',WD,'워독스 (WARDOGS)','시즌 3 사흘째','G1','11/14','활동 47건','시즌 · 토론')
gl+=row('MR','MARVEL RIVALS',MR,'마블 라이벌즈','시즌 11 둠스데이','G2','11/13','첫 45건','시즌 · 토론')
gl+=row('BF6','BATTLEFIELD 6 / REDSEC',BF,'배틀필드 6','부착물 해금 수정','G3','11/14','공식 고정글','패치 · 토론')
gl+=row('R6','RAINBOW SIX',R6,'레인보우 식스','베가스 신작 보도','G4','11/13','Insider Gaming','보도 · 토론')
gl+='</tbody>\n</table></div>\n'
L=lrow('WD','WARDOGS',WD,'워독스 시즌 3','Sabatulo · Limited Mode','출시','t-new','11.12','22~24시 점검 뒤 · 공식','BULKHEAD · Team17','한국어 <b>2,778개</b> 중 <b>37%</b> · 30일 <b>72,684개</b>, <b>71%</b> · 미니건 헬기 답글 <b>78개</b>',lk(dWD,'pc','스팀 토론')+'<br>'+lk(sWD,'pc','상점'))
L+=lrow('MR','MARVEL RIVALS',MR,'마블 라이벌즈 시즌 11','둠스데이 · 나이트크롤러','출시','t-new','11.13','20시 개막 · 기사 기준','—','토론 활성 <b>479건</b>(전날 459) · 채팅 제재 4건 답글 <b>66개</b>',lk(dMR,'pc','스팀')+'<br>'+lk(BEE,'mail','정리 기사'))
L+=lrow('DRK','DERELIKT',DK,'DERELIKT','레트로 SF 호러 FPS','출시','t-new','11.14','해외 11.13 · IGDB 일치','1인 개발 · Hyperstrange','평가 <b>14개</b> 중 <b>85%</b> · ₩<b>15,300</b>(10% 할인) · 한국어 <b>미지원</b>',lk(sDK,'pc','스팀')+'<br>'+lk(PSL,'mail','정리 기사'))
L+=lrow('GTA6','GTA VI',GTA,'GTA VI','PS5 · Xbox','예정','t-live','11.19','Rockstar 뉴스와이어','Rockstar Games','IGDB 캐시 날짜와 <b>일치</b> · 그날 캐시에 <b>4건</b>이 몰림',lk(RSN,'home','공식'))
L+=lrow('OW','OVERWATCH 2',OW,'오버워치 허드슨','55번째 영웅 · 옴닉 탐정','발표','t-live','12월','시즌 6 · 날짜 미정','Blizzard','2026 신규 <b>10명</b> 중 공격 <b>5명</b> · 인벤 글 <b>2,691회</b>',lk(KOT,'mail','정리 기사')+'<br>'+lk(GOSU,'mail','정리 기사'))
L+=lrow('R6','RAINBOW SIX',R6,'레인보우 식스 베가스 신작','코드명 Spades · 보도','발표','t-warn','11.13','보도일 · 공식 미확인','—','전작 <b>2008년</b> · 시즈 토론 50건 중 관련 제목 <b>0건</b>',lk(FW,'mail','정리 기사')+'<br>'+lk(dR6,'pc','시즈 토론'))
L+=lrow('GS','지스타 2026',None,'지스타 2026','부산 벡스코 · 인디 쇼케이스','예정','t-live','11.19~22','기사 11/11','—','대형사 <b>4곳</b> 일반 전시 불참 · 인디 <b>114곳</b> · 크래프톤 슈터 <b>1종</b>',lk(KRP,'home','공식')+'<br>'+lk(DLT,'mail','정리 기사'),grp=True)
L+=lrow('IGDB','IGDB 슈터 예정',None,'11/14~11/27 IGDB 슈터 예정','Overspray 외 · 소규모 다수','미확정','t-warn','11.14~27','IGDB 캐시 값','—','캐시에 <b>12건</b> · 11/19에 <b>4건</b>이 몰림 · 상점 대조 <b>2건</b> 중 어긋남 <b>0건</b>','—',grp=True)
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
trend+=card('DRK','DERELIKT',DK,'<span class="tag t-new">11/14 출시</span><span class="tag t-warn">한국어 미지원</span>','소형 슈터 · DERELIKT','첫 평가 14개 중 85%가 긍정입니다','T1',A(sDK,'스팀 상점')+' · '+A(PSL,'PlayStation LifeStyle'))
trend+=card('R6','RAINBOW SIX',R6,'<span class="tag t-warn">보도</span><span class="tag t-live">초기 개발</span>','시리즈 부활 · 레인보우 식스 베가스','베가스 신작 보도에도 시즈 포럼은 조용합니다','T2',A(FW,'Final Weapon')+' · '+A(dR6,'시즈 토론'))
trend+=card('OW','OVERWATCH 2',OW,'<span class="tag t-live">12월 시즌 6</span><span class="tag t-warn">역할 전환</span>','신규 영웅 · 오버워치 허드슨','올해 신규 영웅 절반이 공격입니다','T3',A(KOT,'Kotaku')+' · '+A(GOSU,'GosuGamers'))
trend+='</div>\n'
risk=f'''<div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>
<article class="risk high"><div class="lvl">HIGH · 미니건 헬기 답글 78개</div><h3>시즌 사흘째 미니건 헬기 불만이 다섯 배로 불었습니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R1_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R1_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R1_LESSON']}</ol></div></article><article class="risk"><div class="lvl">MID · 채팅 제재 답글 66개</div><h3>시즌 11 개막 다음 날 채팅 제재 불만이 몰렸습니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R2_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R2_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R2_LESSON']}</ol></div></article>
'''
action=f'''<div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>
<article class="act"><div class="num">1</div><div><h3>허드슨 역할 전환 국내 반응을 주말 동안 잽니다</h3><p>{B['A1_P']}</p></div></article><article class="act"><div class="num">2</div><div><h3>새 성능 모드 위치를 FAQ 후보로 둡니다</h3><p>{B['A2_P']}</p></div></article>
'''
caveat='''<div class="caveat">
<span class="k">유의사항</span>
<span class="crow"><b class="ck">방법</b><span>이번 판은 11/14 07시대에 데스크톱 내장 브라우저로 읽었습니다.<span class="lb"></span>스팀 수치는 토론 목록 첫 페이지에서 고정글을 뺀 값입니다.</span></span><span class="crow"><b class="ck">분류</b><span>워독스 헬기·탈것은 제목 낱말로 셌습니다.<span class="lb"></span>어제 13건은 차량까지 넓게 잡아 오늘 6건과 기준이 다릅니다.</span></span><span class="crow"><b class="ck">일정</b><span>IGDB 캐시는 11/13 09:20 갱신본입니다.<span class="lb"></span>상점 대조 2건은 어긋남이 없고 DERELIKT 날짜 차이는 시차였습니다.</span></span><span class="crow"><b class="ck">보도</b><span>베가스 신작은 유비소프트 확인 전 보도입니다.<span class="lb"></span>Insider Gaming 원문은 열리지 않아 재인용 기사로 확인했습니다.</span></span><span class="crow"><b class="ck">원문</b><span>인벤 허드슨 글 본문은 텍스트가 없어 제목과 댓글만 읽었습니다.</span></span><span class="crow"><b class="ck">미열람</b><span>아카라이브와 CS2, 델타포스 토론은 열지 않았습니다.</span></span>
</div>
'''
S=[('스팀 토론',[(dWD,'워독스 토론'),(dMR,'마블 라이벌즈 토론'),(dBF,'배틀필드 6 토론'),(pBFA,'BFComms 부착물 수정'),(dR6,'시즈 토론'),(dCC,'신더시티 토론')]),('스팀 상점',[(sWD,'워독스 상점'),(sDK,'DERELIKT 상점')]),('공식',[(RSN,'Rockstar 뉴스와이어'),(KRP,'크래프톤 지스타 보도자료'),(OWN,'블리자드 11월 패치노트')]),('기사',[(KOT,'Kotaku 허드슨'),(GOSU,'GosuGamers 허드슨'),(FW,'Final Weapon 베가스'),(FN,'파이낸셜뉴스 배그 경량판'),(PSL,'PlayStation LifeStyle DERELIKT'),(PX,'Pure Xbox 11/13'),(BEE,'Beebom 시즌 11'),(DLT,'데일리환경 지스타'),(GEM,'Gematsu 레인저 럼블')]),('국내 커뮤니티',[(HOT,'인벤 핫벤'),(OWI,'인벤 오버워치 자유게시판'),(HUD,'인벤 허드슨 글'),(RUL,'루리웹 메인 신설 게시판')])]
n=sum(len(x[1]) for x in S)
src=f'<!-- 09 출처 -->\n<details class="sources" id="sources" open>\n<summary>출처 링크 {n}건</summary>\n<div class="body">\n<ul>\n'+''.join(f'<li><b>{k}</b>'+' · '.join(A(u,t) for u,t in v)+'</li>\n' for k,v in S)+'</ul>\n<div class="colophon">\n<b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.128<br>\n모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n</div>\n</div>\n</details>\n</div>\n'
body='<main id="main">\n<div class="wrap">\n'+B['LEAD']+'\n'+notice+'\n'+kpis+'\n<div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>\n'+tl+'<div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n'+heroes+kr+gl+launch+trend+risk+action+caveat+src
h=head.replace('2026-11-13','2026-11-14').replace('11월 13일','11월 14일')
out=h+'\n'+masthead+body+tail
p=R+'/reports/2026-11/FPS레이더_2026-11-14.html'
open(p,'w',encoding='utf-8').write(out)
print(len(out), total, n)
