# -----------------------------------------------------------
#  IGDB 동기화 - FPS레이더  (PowerShell 판, 파이썬 설치 불필요)
#  * 이 파일은 반드시 UTF-8 with BOM 으로 저장해야 합니다.
#    (Windows PowerShell 5.1 은 BOM 이 없으면 한글을 깨뜨립니다)
# -----------------------------------------------------------

$ErrorActionPreference = 'Stop'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

$Root         = Split-Path -Parent $PSScriptRoot
$ConfigPath   = Join-Path $PSScriptRoot 'igdb_config.json'
$TokenPath    = Join-Path $PSScriptRoot '.igdb_token.json'
$AssetsDir    = Join-Path $Root 'assets'
$CachePath    = Join-Path $AssetsDir 'igdb_cache.json'
$UpcomingPath = Join-Path $AssetsDir 'igdb_upcoming.json'

$ImgFmt = 'https://images.igdb.com/igdb/image/upload/t_{0}/{1}.jpg'

# 추적 대상: 리포트에서 쓰는 한글명 = IGDB 검색어
$Tracked = [ordered]@{
  '발로란트'           = 'Valorant'
  '오버워치2'          = 'Overwatch 2'
  '에이펙스 레전드'    = 'Apex Legends'
  '콜오브듀티: MW4'    = 'Call of Duty: Modern Warfare 4'
  'Counter-Strike 2'   = 'Counter-Strike 2'
  '레인보우 식스 시즈' = "Tom Clancy's Rainbow Six Siege"
  '배틀필드 6'         = 'Battlefield 6'
  '데스티니 2'         = 'Destiny 2'
  '마블 라이벌즈'      = 'Marvel Rivals'
  '델타 포스'          = 'Delta Force'
  'THE FINALS'         = 'The Finals'
  '배틀그라운드(PUBG)' = 'PUBG: Battlegrounds'
  '서든어택'           = 'Sudden Attack'
  '타임 테이커즈'      = 'Time Takers'
}

$GenreShooter = 5
$Platforms    = '6,48,167,49,169'   # PC, PS4, PS5, XboxOne, XboxSeries

function Say([string]$m) { Write-Host $m }

function Die([string]$m) {
  Write-Host ''
  Write-Host "[오류] $m" -ForegroundColor Red
  Write-Host ''
  exit 1
}

function Write-JsonFile($Path, $Obj) {
  $json = $Obj | ConvertTo-Json -Depth 12
  $enc  = New-Object System.Text.UTF8Encoding $false
  [System.IO.File]::WriteAllText($Path, $json, $enc)
}

# ── 설정 읽기 ─────────────────────────────────────────────
if (-not (Test-Path $ConfigPath)) {
  Die "설정 파일이 없습니다: tools\igdb_config.json"
}
try {
  $cfg = Get-Content $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
} catch {
  Die "igdb_config.json 을 읽을 수 없습니다. JSON 문법(쉼표, 큰따옴표)을 확인하세요."
}
foreach ($k in @('client_id','client_secret')) {
  $v = $cfg.$k
  if ([string]::IsNullOrWhiteSpace($v) -or $v -like '여기에*') {
    Die "igdb_config.json 의 $k 값이 비어 있습니다."
  }
}
$UpcomingDays = 60
if ($cfg.upcoming_days) { $UpcomingDays = [int]$cfg.upcoming_days }

Say ('=' * 56)
Say ' IGDB 동기화 - FPS레이더'
Say ('=' * 56)

# ── 토큰 ──────────────────────────────────────────────────
function Get-IgdbToken {
  if (Test-Path $TokenPath) {
    try {
      $t    = Get-Content $TokenPath -Raw -Encoding UTF8 | ConvertFrom-Json
      $left = [double]$t.expires_at - [double]([DateTimeOffset]::UtcNow.ToUnixTimeSeconds())
      if ($left -gt 86400) {
        $exp = [DateTimeOffset]::FromUnixTimeSeconds([int64]$t.expires_at).LocalDateTime
        Say ("  토큰: 캐시 재사용 (만료 {0:yyyy-MM-dd})" -f $exp)
        return $t.access_token
      }
    } catch {}
  }
  Say '  토큰: 새로 발급 중...'
  $body = @{
    client_id     = $cfg.client_id
    client_secret = $cfg.client_secret
    grant_type    = 'client_credentials'
  }
  try {
    $r = Invoke-RestMethod -Method Post -Uri 'https://id.twitch.tv/oauth2/token' -Body $body -TimeoutSec 30
  } catch {
    Die "토큰 발급 실패. Client ID / Secret 을 확인하세요. $($_.Exception.Message)"
  }
  $expiresAt = [double]([DateTimeOffset]::UtcNow.ToUnixTimeSeconds()) + [double]$r.expires_in
  $tok = [ordered]@{ access_token = $r.access_token; expires_at = $expiresAt }
  Write-JsonFile $TokenPath $tok
  $exp = [DateTimeOffset]::FromUnixTimeSeconds([int64]$expiresAt).LocalDateTime
  Say ("  토큰: 발급 완료 (만료 {0:yyyy-MM-dd})" -f $exp)
  return $r.access_token
}

$Token = Get-IgdbToken

# ── IGDB 호출 ─────────────────────────────────────────────
function Invoke-Igdb([string]$Endpoint, [string]$Query, [bool]$Retry = $true) {
  $headers = @{ 'Client-ID' = $cfg.client_id; 'Authorization' = "Bearer $Token" }
  try {
    $uri = "https://api.igdb.com/v4/$Endpoint"
    $res = Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -Body $Query -ContentType 'text/plain' -TimeoutSec 30
    Start-Sleep -Milliseconds 280
    return $res
  } catch {
    $code = 0
    if ($_.Exception.Response) {
      try { $code = [int]$_.Exception.Response.StatusCode } catch { $code = 0 }
    }
    if ($code -eq 401 -and $Retry) {
      Remove-Item $TokenPath -ErrorAction SilentlyContinue
      $script:Token = Get-IgdbToken
      return Invoke-Igdb $Endpoint $Query $false
    }
    if ($code -eq 429 -and $Retry) {
      Start-Sleep -Seconds 2
      return Invoke-Igdb $Endpoint $Query $false
    }
    Say "  [경고] $Endpoint 호출 실패 (HTTP $code)"
    return @()
  }
}

function Pick-Richest($Arr) {
  # 같은 이름 후보 중 이미지·메타가 가장 풍부한 것(대개 본편)을 고른다
  $best  = $null
  $score = -1
  foreach ($r in @($Arr)) {
    $s = 0
    if ($r.cover)       { $s = $s + 3 }
    if ($r.artworks)    { $s = $s + @($r.artworks).Count }
    if ($r.screenshots) { $s = $s + @($r.screenshots).Count }
    if ($s -gt $score) { $score = $s; $best = $r }
  }
  return $best
}

function Select-Best($Results, [string]$Want) {
  if (-not $Results) { return $null }
  $arr = @($Results)
  if ($arr.Count -eq 0) { return $null }
  $w = $Want.ToLower()
  # 1) 이름 완전 일치
  foreach ($r in $arr) { if ($r.name -and $r.name.ToLower() -eq $w) { return $r } }
  # 2) 포함하는 것 중 '이름이 가장 짧은' 항목 - 부제/번들/DLC 배제 효과
  $cand = @($arr | Where-Object { $_.name -and $_.name.ToLower().Contains($w) })
  if ($cand.Count -gt 0) {
    $cand = @($cand | Sort-Object { $_.name.Length })
    return $cand[0]
  }
  return $arr[0]
}

# ── 1) 게임 이미지 / 메타 ─────────────────────────────────
Say ''
Say ('[1/2] 게임 커버·아트워크 조회 ({0}종)' -f $Tracked.Count)
$games   = [ordered]@{}
$okCount = 0

foreach ($ko in $Tracked.Keys) {
  $en = $Tracked[$ko]
  $esc    = $en -replace '"','\"'
  $fields = 'fields name,slug,url,first_release_date,cover.image_id,artworks.image_id,screenshots.image_id,genres.name,involved_companies.company.name;'

  # (1) 이름이 정확히 일치하는 항목 우선 - 번들/DLC/동명이곡 오매칭 방지
  $q1   = $fields + ' where name = "' + $esc + '"; limit 8;'
  $r1   = @(Invoke-Igdb 'games' $q1)
  $best = $null
  $how  = '정확'
  if ($r1.Count -gt 0) { $best = Pick-Richest $r1 }

  # (2) 없으면 퍼지 검색으로 폴백
  if (-not $best) {
    $how  = '검색'
    $q2   = 'search "' + $esc + '"; ' + $fields + ' limit 20;'
    $best = Select-Best (Invoke-Igdb 'games' $q2) $en
  }

  if (-not $best) {
    Say ("  - {0,-18} 검색 결과 없음" -f $ko)
    $games[$ko] = [ordered]@{ igdb_id = $null; note = 'IGDB 검색 실패' }
    continue
  }

  $cover = $null
  if ($best.cover) { $cover = $best.cover.image_id }
  $arts  = @()
  $shots = @()
  if ($best.artworks)    { $arts  = @($best.artworks    | Where-Object { $_.image_id } | ForEach-Object { $_.image_id }) }
  if ($best.screenshots) { $shots = @($best.screenshots | Where-Object { $_.image_id } | ForEach-Object { $_.image_id }) }

  # 리포트 타일은 가로형이 어울리므로 아트워크 > 스크린샷 > 커버 순
  $banner = $cover
  if ($arts.Count -gt 0)       { $banner = $arts[0] }
  elseif ($shots.Count -gt 0)  { $banner = $shots[0] }

  $bannerUrl = $null
  $coverUrl  = $null
  if ($banner) { $bannerUrl = ($ImgFmt -f '720p', $banner) }
  if ($cover)  { $coverUrl  = ($ImgFmt -f 'cover_big', $cover) }

  $genreNames = @()
  if ($best.genres) { $genreNames = @($best.genres | ForEach-Object { $_.name }) }
  $companyNames = @()
  if ($best.involved_companies) {
    $companyNames = @($best.involved_companies | Where-Object { $_.company } | ForEach-Object { $_.company.name })
    $companyNames = @($companyNames | Select-Object -First 3)
  }

  $games[$ko] = [ordered]@{
    igdb_id         = $best.id
    igdb_name       = $best.name
    igdb_url        = $best.url
    cover_image_id  = $cover
    banner_image_id = $banner
    banner_url      = $bannerUrl
    cover_url       = $coverUrl
    artworks        = @($arts  | Select-Object -First 5)
    screenshots     = @($shots | Select-Object -First 5)
    genres          = $genreNames
    companies       = $companyNames
  }

  $mark = '이미지없음'
  if ($banner) { $okCount = $okCount + 1; $mark = 'OK        ' }
  Say ("  - {0,-18} {1} [{2}]  {3}" -f $ko, $mark, $how, $best.name)
}

# ── 2) 향후 슈터 신작 ─────────────────────────────────────
Say ''
Say ("[2/2] 향후 {0}일 슈터 신작 조회" -f $UpcomingDays)
$now   = [int64]([DateTimeOffset]::UtcNow.ToUnixTimeSeconds())
$until = $now + ($UpcomingDays * 86400)
$q2 = "fields game.name,game.url,game.cover.image_id,date,human,platform.name; where date > $now & date < $until & game.genres = ($GenreShooter) & platform = ($Platforms) & game.version_parent = null; sort date asc; limit 60;"
$rows = Invoke-Igdb 'release_dates' $q2

$seen     = @{}
$upcoming = New-Object System.Collections.ArrayList
foreach ($r in @($rows)) {
  $g = $r.game
  if (-not $g)    { continue }
  if (-not $g.id) { continue }
  $key = [string]$g.id
  if ($seen.ContainsKey($key)) { continue }
  $seen[$key] = $true

  $cid = $null
  if ($g.cover) { $cid = $g.cover.image_id }
  $cUrl = $null
  $bUrl = $null
  if ($cid) {
    $cUrl = ($ImgFmt -f 'cover_big', $cid)
    $bUrl = ($ImgFmt -f '720p', $cid)
  }
  $pName = $null
  if ($r.platform) { $pName = $r.platform.name }

  $row = [ordered]@{
    name       = $g.name
    date       = [DateTimeOffset]::FromUnixTimeSeconds([int64]$r.date).LocalDateTime.ToString('yyyy-MM-dd')
    human      = $r.human
    platform   = $pName
    igdb_url   = $g.url
    cover_url  = $cUrl
    banner_url = $bUrl
  }
  [void]$upcoming.Add($row)
}
$upcoming = @($upcoming | Sort-Object { $_.date })
Say ("  - {0}건 수집" -f $upcoming.Count)
foreach ($r in @($upcoming | Select-Object -First 8)) {
  Say ("      {0}  {1}" -f $r.date, $r.name)
}
if ($upcoming.Count -gt 8) { Say ("      ... 외 {0}건" -f ($upcoming.Count - 8)) }

# ── 저장 ──────────────────────────────────────────────────
if (-not (Test-Path $AssetsDir)) { New-Item -ItemType Directory -Path $AssetsDir | Out-Null }
$stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

$cacheObj = [ordered]@{
  '_생성시각'       = $stamp
  '_출처'           = 'IGDB (api.igdb.com/v4) · 이미지는 images.igdb.com 핫링크 허용'
  '_이미지주소규칙' = 'https://images.igdb.com/igdb/image/upload/t_<size>/<image_id>.jpg (size: thumb / cover_small / cover_big / screenshot_med / screenshot_big / screenshot_huge / 720p / 1080p)'
  '_사용법'         = '리포트 썸네일은 banner_url 우선, 없으면 cover_url.'
  'games'           = $games
}
Write-JsonFile $CachePath $cacheObj
Say ''
Say '저장: assets/igdb_cache.json'

$upObj = [ordered]@{
  '_생성시각' = $stamp
  '_범위'     = ("향후 {0}일 · 장르=Shooter · PC/PS/Xbox" -f $UpcomingDays)
  '_주의'     = 'IGDB 등록 기준이라 국내 게임·미등록 신작은 빠질 수 있음. 웹 검색으로 보완할 것.'
  'releases'  = $upcoming
}
Write-JsonFile $UpcomingPath $upObj
Say '저장: assets/igdb_upcoming.json'

Say ''
Say ("완료 - 이미지 확보 {0}/{1}종, 신작 {2}건" -f $okCount, $Tracked.Count, $upcoming.Count)
Say ('=' * 56)
