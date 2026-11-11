import json,re,os
R=os.environ['HOME']+'/mnt/fps-radar'
prev=open(R+'/reports/2026-11/FPS레이더_2026-11-10.html',encoding='utf-8').read()
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
sWD='https://store.steampowered.com/app/1867240/?l=koreana'
dWD='https://steamcommunity.com/app/1867240/discussions/'
dDF='https://steamcommunity.com/app/2507950/discussions/'
LWG='https://lastwordongaming.com/2026/11/09/wardogs-season-3-bulkhead-bans/'
GI='https://gameinformer.com/2026/11/10/playstation-cancels-in-development-live-service-shooter-fairgames-at-jade-raymonds'
OWD='https://news.blizzard.com/en-us/article/24316733/directors-take-5v5-and-6v6-better-together'
OWI='https://www.inven.co.kr/board/overwatch/4538'
MRA='https://khelnow.com/gaming/marvel-rivals-season-11-release-timings-202611'
GST='https://ceoscoredaily.com/page/view/2026101914162321527'
EA='https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-community-update-more-to-season-5'
OWN='https://overwatch.blizzard.com/ko-kr/news/patch-notes/live/2026/11/'
DFN='https://noping.com/kr/blog/delta-force-season-aurora'

masthead=prev[prev.index('<body>'):prev.index('<main id="main">')]
masthead=masthead.replace('2026년 11월 10일 (화)','2026년 11월 11일 (수)').replace('커버기간: 11/9(월) 오전 – 11/10(화) 오전','커버기간: 11/10(화) 오전 – 11/11(수) 오후').replace('스팀·웹 7시대까지 수집','스팀·웹 15시대까지 수집')
notice='<div class="notice"><span class="k">캐시</span><span><b>마블 라이벌즈 스팀 토론 첫 화면은 11/8·11/10 판과 같은 목록이라 지표에서 뺐습니다.</b><span class="lb"></span>워독스·델타포스 토론과 인벤 오버워치는 당일 값입니다.<span class="lb"></span>인벤 목록의 최신 글은 14:58에 올라왔습니다.</span></div>'
kpis=f'<div class="kpis" id="summary"><div class="kpi"><div class="lbl">진행 중 시즌·이벤트</div><div class="big">8건</div><div class="sub">{A(DFN,"델타포스 오로라")}<span class="sep">·</span>{A(EA,"배틀필드 6 시즌 5")}<span class="sep">·</span>{A(OWN,"오버워치 군림")}</div></div><div class="kpi risk"><div class="lbl">논란·리스크 신호</div><div class="big">워독스 치트·제재 제목 7건에 답글 221개가 몰렸습니다</div><div class="sub">첫 12건 답글 <b>254개</b>의 87%입니다. <a href="#risk">상세 보기</a></div></div><div class="kpi"><div class="lbl">신작 반응</div><div class="big">소니 페어게임즈 개발 중단이 보도됐습니다</div><div class="sub">테스트 리텐션이 <b>목표 미달</b>이었습니다. {A(GI,"Game Informer")}</div></div><div class="kpi"><div class="lbl">국내 포커스</div><div class="big">인벤 오버워치에 6대6 제목이 8건 올랐습니다</div><div class="sub">조회 합계 <b>1,776회</b>입니다</div></div></div>'
def li(s,lab,name,txt,win,today):
    return f'<li class="{"today" if today else ""}"><span class="s {s}">{lab}</span><span class="t"><b>{name}</b> {txt}<span class="win">{win}</span></span></li>'
G=[('11.12 목',True,[('start','시작','워독스 시즌 3','시작한다고 보도됐습니다','Sabatulo 맵 · 기사 기준'),('end','종료','서든어택 콤보 패스 시즌4','끝납니다','인벤 10/15 기사 · 이전 판 이월')]),
('11.13 금',False,[('start','시작','마블 라이벌즈 시즌 11','시작 예정으로 보도됐습니다','03:00 PT · 기사 기준')]),
('11.19 목',False,[('start','시작','GTA VI','출시 예정으로 복수 매체가 보도했습니다','PS5·Xbox · 공식 미확인'),('start','시작','지스타 2026','부산 벡스코에서 열립니다','~11/22 · 크래프톤 100부스 이상')]),
('11.20 금',False,[('start','시작','오버워치 정크랫의 전리품 사냥','열립니다','~11/24 · 주말 경험치 2배')]),
('11.25 수',False,[('start','시작','오버워치 OWCS 월드 파이널 응원 대회','시작합니다','~12/8 · 블리자드 패치노트')]),
('12.08 화',False,[('start','시작','배틀필드 6 서버 브라우저와 플래툰','3단계로 예고됐습니다','플래툰 지연 안내 · EA 공지'),('end','종료','오버워치 군림 이벤트','끝납니다','블리자드 패치노트')])]
T=[('on','진행','오버워치 군림 이벤트','8일째입니다','11/4~12/8 · 블리자드 패치노트'),('on','진행','델타포스 시즌 오로라','이틀째입니다','11/10 시작 · 스팀 토론 확인'),('on','진행','배틀필드 6 시즌 5 2단계','이틀째입니다','유럽 카지노 맵 · EA 공지'),('end','종료','워독스 시즌 2','28일째로 마지막 날입니다','10/15 시작 · 시즌 3 기사 기준'),('on','진행','디비전 2 센트럴 파크의 메아리','출시 9일째입니다','11/3 출시 · 이전 판 이월'),('on','진행','Sulfur 1.0','출시 15일째입니다','10/28 출시'),('on','진행','마이코펑크 1.0','출시 23일째입니다','10/20 출시 · PC·PS5'),('on','진행','서든어택 시즌4 문라이즈','이어집니다','~12/10 · 이전 판 이월')]
total=len(T)+sum(len(x[2]) for x in G)
tl=f'<div class="timeline">\n<h3>움직이는 일정 {total}건</h3>\n<p class="hint">날짜 머리를 누르면 그 날 일정을 접거나 펼칠 수 있습니다. 붉은 묶음이 오늘(11/11)입니다.</p>\n'
tl+=f'<details class="dgroup today" open>\n<summary><span class="dg-d">11.11 수</span><span class="dg-t">오늘</span><span class="dg-n">{len(T)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,True) for x in T)+'</ol>\n</details>\n'
for d,op,items in G:
    tl+=f'<details class="dgroup"{" open" if op else ""}>\n<summary><span class="dg-d">{d}</span><span class="dg-n">{len(items)}건</span></summary>\n<ol class="tl">'+''.join(li(*x,False) for x in items)+'</ol>\n</details>\n'
tl+='</div>\n'
H=[('01','개발 중단','페어게임즈 · 블룸버그 보도','소니, PvP 슈터 페어게임즈 개발 중단',B['H1_UNDER'],GI,'FG','FAIRGAMES',None),
('02','6대6 제목 8건','오버워치 · 디렉터의 관점','시즌 6에 6대6 역할 고정 경쟁전 시험',B['H2_UNDER'],OWD,'OW','OVERWATCH 2',OW),
('03','답글 96개','워독스 · 스팀 토론','치트 호소 96개, 18만 5천 제재 뒤에도',B['H3_UNDER'],dWD,'WD','WARDOGS',WD)]
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
kr+=row('OW','OVERWATCH 2',OW,'오버워치2','6대6 역할 고정 시험','K2','11/11','공지·앞쪽 40건','모드 · 국내 반응')
kr+=row('HV','인벤 핫벤',None,'인벤 핫벤','핫벤 30위·200위','K1','11/11','30위까지','순위 · 국내 반응')
kr+=row('PUBG','KRAFTON',PUBG,'크래프톤 · 지스타 2026','11/19~11/22 벡스코','K3','11/19','기사 10/19','행사 · 출품')
kr+='</tbody>\n</table></div>\n'
gl='<div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>\n<p class="sub-lead">근거는 <b>스팀 커뮤니티 토론 원문</b>과 <b>스팀 상점 지표</b>, 그리고 해외 전문지 보도입니다.</p>\n'
gl+=f'''<div class="evkey">
<b>오늘 연 해외 커뮤니티</b>
<span><span class="ev cm">확인</span>{A(dWD,"워독스")}<span class="d">고정글 뺀 12건 · 방금 전~29분 전 · 활성 주제 1,908건</span></span>
<span><span class="ev cm">확인</span>{A(dDF,"델타포스")}<span class="d">첫 15건 · 30분 전~7시간 전 · 활성 주제 287건</span></span>
<span><span class="ev mt">확인</span><span class="d">스팀 상점: 워독스 당일 값</span></span>
<span><span class="ev gl">매체만</span><span class="d">페어게임즈 · 마블 라이벌즈 시즌 11: 해외 기사</span></span>
<span><span class="ev na">옛 값</span><span class="d">마블 라이벌즈 토론은 11/8 판과 같은 목록이라 뺐습니다</span></span>
<span><span class="ev na">미열람</span><span class="d">레인보우 식스 시즈 · CS2 · 에이펙스 · 데스티니 2 · THE FINALS · 배틀필드 6 토론</span></span>
<span><span class="ev na">축 없음</span><span class="d">발로란트와 서든어택은 스팀 미등록</span></span>
</div>
'''
gl+='<div class="tablewrap"><table>\n'+TH+'\n<tbody>\n'
gl+=row('WD','WARDOGS',WD,'워독스 (WARDOGS)','치트·제재 글','G1','11/11','첫 12건','제재 · 토론')
gl+=row('FG','FAIRGAMES',None,'페어게임즈 (Fairgames)','개발 중단 보도','G2','11/10','블룸버그 보도','개발 중단 · 기사')
gl+=row('DF','DELTA FORCE',DF,'델타포스','시즌 오로라 이틀째','G3','11/11','첫 15건','시즌 · 토론')
gl+='</tbody>\n</table></div>\n'
L=lrow('WD','WARDOGS',WD,'워독스 시즌 3','Sabatulo 맵 · 3개월 시즌','예정','t-live','11.12','기사 기준 · 앞서 해보기 09.10','BULKHEAD · Team17','한국어 <b>2,694개</b> 중 <b>36%</b>(전날 35%) · 30일 <b>67,349개</b>, <b>71%</b> · 토론 활성 <b>1,908건</b>',lk(sWD,'pc','스팀')+'<br>'+lk(LWG,'mail','정리 기사'))
L+=lrow('DF','DELTA FORCE',DF,'델타포스 시즌 오로라','Zenith Port · AN94','출시','t-new','11.10','기사 기준','—','토론 활성 <b>287건</b> · 첫 15건 답글 <b>19개</b> · 건스미스 제목 <b>3건</b>',lk(dDF,'pc','스팀')+'<br>'+lk(DFN,'mail','정리 기사'))
L+=lrow('FG','FAIRGAMES',None,'페어게임즈 (Fairgames)','PS5·PC · 개발 중단','발표','t-warn','11.10','블룸버그 보도','Haven Studios · 소니','2023년 발표 · 수천 명 테스트 <b>목표 미달</b> · 해고 <b>0명</b>',lk(GI,'mail','정리 기사'))
L+=lrow('OW','OVERWATCH 2',OW,'오버워치 6대6 역할 고정 시험','시즌 6 첫 4주','발표','t-live','11.10','시즌 6 날짜 미공지','—','경쟁전 선택지 <b>3개</b> · 인벤 6대6 제목 <b>8건</b>, 조회 <b>1,776회</b>',lk(OWD,'home','공식'))
L+=lrow('MR','MARVEL RIVALS',MR,'마블 라이벌즈 시즌 11','신규 영웅 미확정','예정','t-live','11.13','기사 기준 · 03:00 PT','—','신규 영웅 <b>2명</b> 예상 기사 · 토론 첫 화면 <b>옛 값</b>',lk(MRA,'mail','정리 기사'))
L+=lrow('GTA6','GTA VI',None,'GTA VI','PS5 · Xbox','미확정','t-warn','11.19','IGDB 캐시 값','—','복수 매체가 <b>11/19</b>로 보도 · 상점 날짜 <b>확인 전</b>','—')
L+=lrow('GS','지스타 2026',None,'지스타 2026','부산 벡스코 · 크래프톤','예정','t-live','11.19~22','기사 10/19','—','크래프톤 <b>100부스</b> 이상 · 슈터 후보 <b>2종</b> · 넥슨·넷마블·엔씨 BTC <b>불참</b>',lk(GST,'mail','정리 기사'),grp=True)
L+=lrow('IGDB','IGDB 슈터 예정',None,'11/11~11/13 IGDB 슈터 예정','Headshot Holdout 외 · PC','미확정','t-warn','11.11~13','IGDB 캐시 값','—','캐시에 <b>16종</b> · 11/12에 <b>8종</b>이 몰림 · <b>상점 날짜는 확인 전</b>','—',grp=True)
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
trend+=card('WD','WARDOGS',WD,'<span class="tag t-new">시즌 3 전날</span><span class="tag t-warn">한국어 36%</span>','신작 슈터 · 워독스','한국어 긍정이 36%로 1%p 올랐습니다','T1',A(sWD,'워독스 스팀 상점')+' · '+A(LWG,'Last Word on Gaming'))
trend+=card('FG','FAIRGAMES',None,'<span class="tag t-warn">개발 중단</span><span class="tag t-live">PvP 슈터</span>','시장 신호 · 페어게임즈','PvP 슈터 하나가 출시 전에 멈췄습니다','T2',A(GI,'Game Informer'))
trend+=card('IGDB','IGDB 슈터 예정',None,'<span class="tag t-live">예정 16종</span><span class="tag t-warn">지스타 11/19</span>','신작 일정 · IGDB 예정','11/11~11/13에 슈터 16종이 잡혔습니다','T3','IGDB 캐시 · '+A(GST,'지스타 기사'))
trend+='</div>\n'
risk=f'''<div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>
<article class="risk high"><div class="lvl">HIGH · 치트·제재 글이 답글의 87%입니다</div><h3>18만 5천 제재 발표 뒤에도 치트 호소가 최다입니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R1_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R1_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R1_LESSON']}</ol></div></article><article class="risk"><div class="lvl">MID · 델타포스 시즌 이틀째 건스미스 잠금 글</div><h3>건스미스 잠금과 설치 용량 불만이 올라왔습니다</h3><div class="row"><span class="k">무엇이</span><span>{B['R2_WHAT']}</span></div><div class="row"><span class="k">맥락</span><span>{B['R2_CTX']}</span></div><div class="lesson"><span class="k">우리 운영 교훈</span><ol>{B['R2_LESSON']}</ol></div></article>
'''
action=f'''<div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>
<article class="act"><div class="num">1</div><div><h3>워독스 시즌 3 첫날 치트 글을 다시 셉니다</h3><p>{B['A1_P']}</p></div></article><article class="act"><div class="num">2</div><div><h3>오버워치 6대6 질문을 FAQ 후보로 모읍니다</h3><p>{B['A2_P']}</p></div></article>
'''
caveat='''<div class="caveat">
<span class="k">유의사항</span>
<span class="crow"><b class="ck">방법</b><span>이번 판은 예약 실행이 늦어 11/11 15시대에 읽었습니다.<span class="lb"></span>인벤 목록에는 시각만 있어 글 날짜는 가리지 못했습니다.</span></span><span class="crow"><b class="ck">캐시</b><span>마블 라이벌즈 토론은 11/8 판 목록 그대로였습니다.<span class="lb"></span>마이코펑크와 Sulfur 상점은 이번에 다시 확인하지 않아 05 표에서 뺐습니다.</span></span><span class="crow"><b class="ck">미열람</b><span>루리웹 신설 게시판과 아카라이브, 레인보우 식스 시즈, CS2는 열지 않았습니다.</span></span><span class="crow"><b class="ck">일정</b><span>워독스 시즌 3과 마블 라이벌즈 시즌 11은 기사 기준이며 공식 공지와는 맞춰 보지 못했습니다.<span class="lb"></span>IGDB 캐시는 11/10 09:20 갱신본이고 상점과의 대조는 0건입니다.</span></span>
</div>
'''
S=[('스팀 토론',[(dWD,'워독스 토론'),(dDF,'델타포스 토론')]),('스팀 상점',[(sWD,'워독스 스팀 상점')]),('공식',[(OWD,'오버워치 디렉터의 관점'),(OWN,'블리자드 11월 패치노트'),(EA,'EA 시즌 5 공지')]),('기사',[(GI,'Game Informer 페어게임즈'),(LWG,'Last Word on Gaming 워독스'),(MRA,'Khel Now 마블 라이벌즈 시즌 11'),(GST,'CEO스코어데일리 지스타'),(DFN,'노핑 델타포스 시즌 정리')]),('핫벤·인벤 오버워치',[('https://hot.inven.co.kr','인벤 핫벤'),(OWI,'인벤 오버워치 자유게시판')])]
n=sum(len(x[1]) for x in S)
src=f'<!-- 09 출처 -->\n<details class="sources" id="sources" open>\n<summary>출처 링크 {n}건</summary>\n<div class="body">\n<ul>\n'+''.join(f'<li><b>{k}</b>'+' · '.join(A(u,t) for u,t in v)+'</li>\n' for k,v in S)+'</ul>\n<div class="colophon">\n<b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.125<br>\n모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n</div>\n</div>\n</details>\n</div>\n'
body='<main id="main">\n<div class="wrap">\n'+B['LEAD']+'\n'+notice+'\n'+kpis+'\n<div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>\n'+tl+'<div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n'+heroes+kr+gl+launch+trend+risk+action+caveat+src
h=head.replace('2026-11-10','2026-11-11').replace('11월 10일','11월 11일')
out=h+'\n'+masthead+body+tail
p=R+'/reports/2026-11/FPS레이더_2026-11-11.html'
open(p,'w',encoding='utf-8').write(out)
print(len(out), total)
