def lrow(name,mono,gname,em,tag,tcls,dt,dem,mk,sig,lk_,grp=False):
    g=' class="grp"' if grp else ''
    return f'      <tr{g}>\n        <td class="g"><div class="g-cell">{th(name,mono)}<span class="g-name">{gname}<em>{em}</em></span></div></td>\n        <td><span class="tag {tcls}">{tag}</span></td>\n        <td class="dt">{dt}<em>{dem}</em></td>\n        <td class="mk">{mk}</td>\n        <td class="sig">{sig}</td>\n        <td class="lk">{lk_}</td>\n      </tr>\n'
l5=''
l5+=lrow('WARDOGS','WD','워독스 (WARDOGS)','앞서 해보기 39일째','출시','t-new','09.10','한국어 상점 기준','BULKHEAD · Team17','시즌 2 <b>10월 15일</b> 시작 · 한국어 평가 <b>1,198개</b>, 긍정 <b>58%</b>(어제와 같은 값) · 정가 <b>39.99달러</b>',lk('st_wd','pc','스팀')+'<br>'+lk('bulk','home','공식'))
l5+=lrow('ARC RAIDERS','ARC','아크 레이더스','PvE 전용 테스트 6일째','진행','t-warn','10.13','~10.20','Embark Studios','일반 토론 첫 15건 중 PvE 제목 <b>8건</b> · 답글 최다 <b>501개</b> · 종료까지 <b>2일</b>',lk('st_arc','pc','스팀')+'<br>'+lk('ig','mail','정리 기사'))
l5+=lrow('BATTLEFIELD 6','BF6','배틀필드 6 시즌 5','무료 체험 진행','진행','t-warn','10.13','인벤은 10.14 · 날짜 엇갈림','—','체험 종료는 한국 시각 <b>10월 20일 02시</b>로 전해지나 기사마다 엇갈림 · 오늘 토론 목록은 어제와 어긋나 수치 제외',lk('st_bf','pc','스팀')+'<br>'+lk('ts','mail','정리 기사'))
l5+=lrow('WARHAMMER 40,000: BOLTGUN 2','BG2','워해머 40,000: 볼트건 2','출시 보도 5일째','출시','t-warn','10.14','오늘 상점 미확인','Auroch Digital · Big Fan Games, Devolver Digital','어제까지 상점은 출시 전 표시 · 사용자 평가 <b>0건</b> · 정가 <b>24.99달러</b> · 오늘은 상점을 다시 열지 못함',lk('st_bg2','pc','스팀')+'<br>'+lk('gem','mail','정리 기사'))
l5+=lrow('MYCOPUNK','MYC','마이코펑크 (Mycopunk)','정식 출시 · 해보기 종료','예정','t-live','10.20','앞서 해보기 종료 · 2일 남음','Pigeons at Play · Devolver Digital','어제 읽은 평가 <b>4,138개</b> 중 <b>88%</b> · 최근 30일 <b>65개</b> 중 <b>78%</b> · 오늘은 상점을 다시 열지 못함',lk('st_myc','pc','스팀')+'<br>'+lk('mo','mail','정리 기사'))
l5+=lrow('디비전 2','DIV','디비전 2 센트럴 파크의 메아리','확장 DLC','발표','t-live','11.03','유비소프트 공지','Ubisoft','IGDB 캐시와 공식 공지 날짜 <b>일치</b> · 새 엔드게임 콘텐츠를 담는다고 전해짐 · 겹치는 신작 <b>0종</b>',lk('ubi','home','공식')+'<br>'+lk('mp1','mail','정리 기사'))
l5+=lrow('소형작 3종','IND','IGDB 등재 소형 PC 슈터','Athanasia · I Am Your Beast · Battle Nap','미확인','t-warn','10.19~10.22','IGDB 캐시 값','—','캐시에만 있는 소형 PC작 <b>3종</b> · 마이코펑크와 같은 주 · 상점 날짜는 열지 못함','—',True)
l5+=lrow('콘솔 소형작','CON','콘솔 소형작 2종','Dreadway · Darkenstein 3D','미확인','t-warn','10.22 · 10.23','IGDB 캐시 값','—','캐시에만 있는 콘솔작 <b>2종</b> · Xbox와 PS5 각 1종 · 상점 날짜는 열지 못함','—',True)
sec05=('  <!-- 05 -->\n  <div class="sec" id="launch"><span class="idx">05</span><h2>신작 출시·발표</h2><span class="rule"></span></div>\n'
'  <p class="sub-lead">최근 나온 슈터와 곧 나올 슈터를 한 표에 모읍니다. 날짜는 스팀 상점과 IGDB 캐시를 대조했고 소형작은 상점을 열지 못했습니다. 오늘도 새로 공개된 슈터는 확인하지 못했습니다.</p>\n'
'  <div class="tablewrap launch"><table>\n    <colgroup><col class="c-g"><col class="c-s"><col class="c-d"><col class="c-m"><col class="c-sig"><col class="c-l"></colgroup>\n    <thead><tr><th>게임</th><th>상태</th><th>날짜</th><th>개발 · 배급</th><th>관심 신호</th><th>링크</th></tr></thead>\n    <tbody>\n'+l5+'    </tbody>\n  </table></div>\n')
def card(name,mono,chips,gm,h3,body,ob,srcs):
    tb=TH.get(name)
    img=f'<img src="{tb}" alt="{name}">' if tb else ''
    nc='' if tb else ' noimg'
    return f'    <div class="tcard">\n      <div class="tbanner{nc}" data-mono="{mono}" data-name="{name}">{img}</div>\n      <div class="tin">\n        <div class="chips">{chips}</div>\n        <div class="gm">{gm}</div>\n        <h3>{h3}</h3>{body}\n        {obs(ob)}\n        <div class="src">{srcs}</div>\n      </div>\n    </div>\n'
t6=('  <!-- 06 -->\n  <div class="sec" id="trend"><span class="idx">06</span><h2>신작 동향</h2><span class="rule"></span></div>\n  <div class="trend-grid">\n')
t6+=card('MYCOPUNK','MYC','<span class="tag t-live">해보기 종료 예정</span><span class="tag t-good">긍정 88%</span>','신작 슈터 · 마이코펑크','정식 출시를 이틀 앞두고 최근 긍정률이 전체보다 10%p 낮습니다.',
 '앞서 해보기는 스팀 기준 <b>10월 20일</b>에 끝나 <b>이틀</b> 남았습니다. 어제 읽은 전체 평가는 4,138개이고 <b>88%</b>가 호평입니다.'+LB+'최근 30일은 65개 가운데 <b>78%</b>입니다. 오늘은 상점을 다시 열지 못했습니다.',
 '10%p 격차가 출시 전에 움직이는지 지켜봅니다.'+LB+'가격을 올리는 시점이 알려지는지 살핍니다.'+LB+'정식 버전 명칭을 상점에서 다시 확인합니다.',a('st_myc','스팀 상점')+' · '+a('mo','MassivelyOP 일정'))
t6+=card('디비전 2','DIV','<span class="tag t-live">확장 예고</span><span class="tag t-good">공식 공지</span>','신규 확장 · 디비전 2','센트럴 파크의 메아리 확장이 11월 3일에 나옵니다.',
 '유비소프트는 9월 24일 공지로 출시일이 <b>11월 3일</b>이라고 밝혔습니다. IGDB 캐시의 날짜와 같습니다.'+LB+'mp1st는 새 엔드게임 경험이 담긴다고 전했습니다. 세부 내용은 열어 보지 못했습니다.',
 '출시 2주 전에 상점 가격과 사전 구매가 열리는지 봅니다.'+LB+'같은 주에 겹치는 신작이 있는지 확인합니다.'+LB+'스팀 토론에서 확장 이야기가 늘어나는지 살핍니다.',a('ubi','유비소프트 공지')+' · '+a('mp1','mp1st 보도'))
t6+=card('BATTLEFIELD 6','BF6','<span class="tag t-live">무료 체험</span><span class="tag t-warn">기간 엇갈림</span>','시즌 · 배틀필드 6','체험 종료일이 10월 20일과 12월 2일로 엇갈려 전해집니다.',
 '무료 체험은 한국 시각 <b>10월 16일 02시</b>에 시작해 <b>20일 02시</b>에 끝난다고 timesaver.gg가 전했습니다. 일부 보도는 <b>12월 2일</b>까지라고 합니다.'+LB+'오늘 읽은 토론 목록은 어제 기록과 어긋나 수치를 싣지 않았습니다.',
 '종료 직전과 직후에 한국어 평가 수가 달라지는지 봅니다.'+LB+'공식 공지로 종료 시각이 확정되는지 살핍니다.'+LB+'종료 뒤 토론 제목이 어떻게 바뀌는지 봅니다.',a('steam_bf','배틀필드 6 일반 토론')+' · '+a('ts','timesaver 무료 체험'))
t6+='  </div>\n'
def lesson(items): return '<div class="lesson"><span class="k">우리 운영 교훈</span><ol>'+''.join(f'<li><b>{b}</b> {r}</li>' for b,r in items)+'</ol></div>'
def rk(cls,lvl,h3,what,ctx,les): return f'  <article class="risk{cls}">\n    <div class="lvl">{lvl}</div>\n    <h3>{h3}</h3>\n    <div class="row"><span class="k">무엇이</span><span>{what}</span></div>\n    <div class="row"><span class="k">맥락</span><span>{ctx}</span></div>\n    {lesson(les)}\n  </article>\n'
s7='  <!-- 07 -->\n  <div class="sec" id="risk"><span class="idx">07</span><h2>리스크 신호와 운영 교훈</h2><span class="rule"></span></div>\n'
s7+=rk(' high','HIGH · 워독스 치트와 초기화','시즌 2 사흘 뒤에도 치트와 초기화 불만 제목이 이어집니다.',
 '시즌 2가 10월 15일에 시작해 4일째입니다.'+LB+'일반 토론 첫 15건 중 치트 2건과 초기화 2건이 보입니다.'+LB+'한국어 평가 1,198개와 긍정 58%는 어제와 같은 값입니다.',
 '개발진이 "We got a few things wrong" 글을 고정하고 잠갔습니다.'+LB+'"Stop crying about the wipe"는 답글 20개가 달렸습니다.'+LB+'playnews는 진행도 리셋을 전했고 GamingTrend는 언급하지 않았습니다.',
 [('초기화 사실을 이용자가 알기 전에 공지해야 합니다.','제목에 "wipe"가 이미 오르내립니다.'),('치트 제재 안내를 따로 두는 편이 좋습니다.','"Banned for cheating while afk"처럼 오탐 호소도 보입니다.'),('고정글이 잠기면 답할 곳이 사라집니다.','불만을 받을 창구를 함께 열어 두어야 합니다.')])
s7+=rk('','MID · 아크 레이더스 PvE 테스트','PvE 찬성과 반대 글이 같은 목록에서 크게 맞붙습니다.',
 '테스트는 10월 13일부터 20일까지이고 오늘이 6일째입니다.'+LB+'일반 토론 첫 15건 중 PvE 제목이 8건입니다.'+LB+'Inven Global은 영구 도입 보장이 없다고 전했습니다.',
 '답글 501개 글 "To the PVE \'Community\'..."이 있습니다.'+LB+'"ARC Raiders Is a Complete Joke"는 255개입니다.'+LB+'"Anyone else getting insane lag in pve mode?" 같은 성능 불만도 있습니다.',
 [('찬성과 반대를 따로 세어야 합니다.','한쪽 목소리만 보면 방향을 잘못 읽습니다.'),('종료 뒤 진행도 처리를 미리 정해야 합니다.','초기화를 묻는 글이 어제까지 이어졌습니다.'),('시각 표기가 캐시일 수 있습니다.','"방금 전"만 찍힌 목록은 확정 근거로 쓰지 않습니다.')])
s7+=rk('','MID · 배틀필드 6 무료 체험','체험 종료일이 엇갈려 마감 안내가 흔들릴 수 있습니다.',
 '체험은 한국 시각 20일 02시에 끝난다고 전해집니다.'+LB+'일부 보도는 12월 2일까지라고 합니다.',
 '두 날짜 모두 공식 공지 원문이 아니라 매체 보도입니다.'+LB+'오늘 읽은 스팀 토론 목록은 어제 기록과 맞지 않아 뺐습니다.',
 [('종료 시각은 공식 공지로만 확정해야 합니다.','매체마다 달라 이용자 문의가 몰릴 수 있습니다.'),('마감 직전 접속 폭주에 대비해야 합니다.','체험 이용자가 한꺼번에 구매를 고민하는 시기입니다.'),('토론 수집은 목록 신선도부터 확인합니다.','어긋난 목록을 쓰면 잘못된 변화를 말하게 됩니다.')])
s8=('<!-- 08 -->\n  <div class="sec" id="action"><span class="idx">08</span><h2>CM 액션 제안</h2><span class="rule"></span></div>\n'
'  <article class="act">\n    <div class="num">1</div>\n    <div><h3>PvE 테스트가 끝나기 전에 찬반 제목을 따로 세어 둡니다.</h3>\n      <p>테스트는 10월 20일에 끝납니다.'+LB+'<b>①</b> 일반 토론 첫 15건에서 PvE 찬성과 반대 제목을 따로 셉니다. 오늘 기준값은 PvE 제목 8건입니다.'+LB+'<b>②</b> 종료 다음 날 같은 방식으로 다시 세어 비교합니다. 영구 도입 공지가 나오면 그 글 반응도 따로 적습니다.</p>\n    </div>\n  </article>\n'
'  <article class="act">\n    <div class="num">2</div>\n    <div><h3>워독스 시즌 2 전체 패치노트가 나오면 초기화 범위부터 읽습니다.</h3>\n      <p>고정글 "We got a few things wrong"이 잠겨 있어 이용자 질문이 갈 곳이 없습니다.'+LB+'<b>①</b> 전체 패치노트에서 초기화 범위를 읽고 playnews 보도와 맞는지 대조합니다.'+LB+'<b>②</b> 치트 제목은 제재 호소와 신고 글로 나눠 셉니다. 기준은 한국어 평가 1,198개에 긍정 58%입니다.</p>\n    </div>\n  </article>\n')
caveat=('  <div class="caveat">\n    <span class="k">유의사항</span>\n'
'    <span class="crow"><b class="ck">방법</b><span>스팀 토론은 일반 토론 방 첫 15건 제목만 오늘 오전 7시대에 읽었습니다. 본문은 열지 못했습니다.</span></span>'
'<span class="crow"><b class="ck">캐시</b><span>워독스 상점 수치는 어제와 똑같은 값이라 제외했습니다. 스팀 목록의 "방금 전" 표기와 인벤 오버워치 목록은 스냅샷일 수 있습니다.</span></span>'
'<span class="crow"><b class="ck">제외</b><span>배틀필드 6 토론은 어제 기록과 어긋나는 목록이 와서 뺐습니다. 볼트건 2와 마이코펑크 상점은 오늘 다시 열지 못했습니다.</span></span>'
'<span class="crow"><b class="ck">불일치</b><span>IGDB 캐시와 공식 공지 날짜 어긋남은 0건입니다. 체험 종료일은 기사마다 다릅니다. 파이널 시각은 환산값입니다.</span></span>'
'<span class="crow"><b class="ck">이월</b><span>마블 라이벌즈, 서든어택, 오버워치 일정은 어제 판을 이어 썼습니다. 03은 두 행만 담았습니다.</span></span>\n  </div>\n')
def li(lbl,*links): return f'        <li><b>{lbl}</b>'+' · '.join(links)+'</li>\n'
src9=('  <!-- 09 출처 -->\n  <details class="sources" id="sources" open>\n    <summary>출처 링크 NNN건</summary>\n    <div class="body">\n      <ul>\n'
+li('VCT 챔피언스 상하이',a('hs','Hotspawn 파이널 전망'),a('hs3','Hotspawn 상위 3팀'),a('vlr','VLR 상위 결승'),a('spike','The Spike 결과'))
+li('오버워치',a('hot','인벤 핫벤'),a('ow','인벤 오버워치 자유게시판'))
+li('워독스',a('steam_wd','워독스 일반 토론'),a('gt','GamingTrend 시즌 2'),a('pn','playnews 시즌 2 초기화'),a('st_wd','워독스 스팀 상점'))
+li('아크 레이더스',a('steam_arc','아크 레이더스 일반 토론'),a('ig','Inven Global PvE 테스트'),a('st_arc','아크 레이더스 스팀 상점'))
+li('배틀필드 6',a('steam_bf','배틀필드 6 일반 토론'),a('ts','timesaver 무료 체험'),a('inv_s5','인벤 시즌 5 기사'))
+li('신작 출시·발표 링크',a('st_bg2','볼트건 2 스팀'),a('st_myc','마이코펑크 스팀'),a('gem','Gematsu 볼트건 2'),a('mo','MassivelyOP 마이코펑크'),a('ubi','유비소프트 확장 공지'),a('mp1','mp1st 확장 보도'))
+'      </ul>\n      <div class="colophon">\n        <b>FPS 이벤트 동향 레이더</b> · 라이온하트 · 자동 생성 리포트 · No.101<br>\n        모니터링: 루리웹 · 인벤 · 아카라이브 · 스팀 커뮤니티 · 해외 전문지 (국내+글로벌 병행)\n      </div>\n    </div>\n  </details>\n\n</div>\n\n\n')
n=len(re.findall('<a ',src9)); src9=src9.replace('NNN',str(n))
main=('<main id="main">\n<div class="wrap">\n'+lead+notice+'  '+kpis+'  <!-- 01 -->\n  <div class="sec" id="today"><span class="idx">01</span><h2>오늘의 일정</h2><span class="rule"></span></div>\n  '+tl
+'  <!-- 02 -->\n  <div class="sec" id="headline"><span class="idx">02</span><h2>오늘의 헤드라인</h2><span class="rule"></span></div>\n'+heroes
+'  <!-- 03 -->\n  <div class="sec" id="kr"><span class="idx">03</span><h2>국내 포커스</h2><span class="rule"></span></div>\n  <p class="sub-lead">국내 서비스·국내 배경 IP·국내 커뮤니티(<b>인벤·루리웹·아카라이브</b>) 반응 중심.</p>\n  '+evkey03+tab(OWd+VAr)
+'  <!-- 04 -->\n  <div class="sec" id="gl"><span class="idx">04</span><h2>글로벌 포커스</h2><span class="rule"></span></div>\n  <p class="sub-lead">근거는 <b>스팀 커뮤니티 토론 원문</b>과 <b>Hotspawn·Inven Global·GamingTrend</b> 등 매체, 그리고 공식 안내문입니다.</p>\n'+glkey+tab(ARCr+WDr)
+sec05+t6+s7+s8+caveat+src9)
out=pre+main+post
open(R+'/reports/2026-10/FPS레이더_2026-10-18.html','w',encoding='utf-8').write(out)
print(len(out), tot)
