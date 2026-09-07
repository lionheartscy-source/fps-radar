# -----------------------------------------------------------
#  FPS레이더 - 자동 작업 재등록 (절전 해제 + 놓친 실행 따라잡기)
#  * 이 파일은 반드시 UTF-8 with BOM 으로 저장해야 합니다.
#  * 2026-09-07 신설. 직접 실행할 필요 없이 자동화_복구_설정.bat 이 불러옵니다.
# -----------------------------------------------------------

$ErrorActionPreference = 'Stop'
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

$Repo    = Split-Path -Parent $PSScriptRoot
$PushBat = Join-Path $Repo 'push_radar_auto.bat'
$IgdbBat = Join-Path $Repo 'igdb_sync_auto.bat'

$TaskPush = 'FPS레이더 자동 업로드'
$TaskIgdb = 'FPS레이더 IGDB 동기화'

function Say([string]$m) { Write-Host $m }

# 공통 설정: 절전에서 깨워 실행 + 놓쳤으면 나중에라도 실행 + 배터리에서도 실행
function New-Settings {
  New-ScheduledTaskSettingsSet `
    -WakeToRun `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1)
}

function Show-Task([string]$name) {
  try {
    $t = Get-ScheduledTask -TaskName $name -ErrorAction Stop
    $i = Get-ScheduledTaskInfo -TaskName $name -ErrorAction Stop
    $times = ($t.Triggers | ForEach-Object { ([datetime]$_.StartBoundary).ToString('HH:mm') }) -join ', '
    Say ("   [{0}]" -f $name)
    Say ("     상태       : {0}" -f $t.State)
    Say ("     실행 시각  : {0}" -f $times)
    Say ("     절전 해제  : {0}" -f $t.Settings.WakeToRun)
    Say ("     놓친 실행  : {0}" -f $t.Settings.StartWhenAvailable)
    Say ("     마지막 실행: {0}  (결과 {1})" -f $i.LastRunTime, $i.LastTaskResult)
    Say ("     다음 실행  : {0}" -f $i.NextRunTime)
  } catch {
    Say ("   [{0}] 등록된 작업을 찾지 못했습니다." -f $name)
  }
  Say ''
}

Say ''
Say '================================================'
Say '  [1/3] 업로드 작업 재등록 (08:40 / 10:00)'
Say '================================================'
if (-not (Test-Path $PushBat)) { throw "파일을 찾지 못했습니다: $PushBat" }
$aPush = New-ScheduledTaskAction -Execute $PushBat -WorkingDirectory $Repo
$tPush = @(
  (New-ScheduledTaskTrigger -Daily -At '08:40'),
  (New-ScheduledTaskTrigger -Daily -At '10:00')
)
Register-ScheduledTask -TaskName $TaskPush -Action $aPush -Trigger $tPush `
  -Settings (New-Settings) -Description 'FPS레이더 리포트를 GitHub 에 업로드합니다.' -Force | Out-Null
Say '   완료. 리포트 생성 직후(08:40)와 예비(10:00) 두 번 돕니다.'
Say '   올릴 것이 없으면 두 번째 실행은 그냥 끝납니다.'
Say ''

Say '================================================'
Say '  [2/3] IGDB 동기화 작업 재등록 (09:20)'
Say '================================================'
if (Test-Path $IgdbBat) {
  $aIgdb = New-ScheduledTaskAction -Execute $IgdbBat -WorkingDirectory $Repo
  $tIgdb = New-ScheduledTaskTrigger -Daily -At '09:20'
  Register-ScheduledTask -TaskName $TaskIgdb -Action $aIgdb -Trigger $tIgdb `
    -Settings (New-Settings) -Description 'IGDB 신작 일정을 받아 assets/igdb_*.json 을 갱신합니다.' -Force | Out-Null
  Say '   완료.'
} else {
  Say ('   건너뜀. 파일이 없습니다: ' + $IgdbBat)
}
Say ''

Say '================================================'
Say '  [3/3] 현재 상태'
Say '================================================'
Show-Task $TaskPush
Show-Task $TaskIgdb

Say '  * 절전 해제가 True 여도 Windows 전원 옵션에서'
Say '    "예약된 작업으로 깨우기 허용"이 꺼져 있으면 동작하지 않습니다.'
Say '  * PC 가 완전히 꺼져 있으면 어느 옵션도 소용없습니다.'
Say '    다만 "놓친 실행"이 True 이면 다음 부팅 뒤에 밀린 분이 올라갑니다.'
Say ''
