@echo off
REM ============================================================
REM  FPS 레이더 자동 커밋·푸시 + 아카이브 사본 저장 (Windows)
REM  - fps-radar 저장소에서 실행: 오늘 리포트 + reports.json 커밋 후 GitHub push
REM  - 추가로 오늘 리포트 파일을 아카이브 폴더에도 사본 저장
REM  사용: 이 파일을 저장소 폴더에 두고 더블클릭 또는 예약 작업이 실행
REM ============================================================
setlocal

REM ▼ 저장소 폴더 (GitHub Desktop 클론 위치)
set "REPO=C:\Users\LION\Documents\GitHub\fps-radar"
REM ▼ 아카이브(사본 보관) 폴더 — 매일 발행 파일을 여기에도 저장
set "ARCHIVE=C:\Users\LION\Desktop\Project S\14. 일간 FPS 이벤트 동향 리서칭"

REM ▼ git 실행파일 찾기 (PATH 우선, 없으면 GitHub Desktop 번들 git)
set "GIT=git"
where git >nul 2>nul
if errorlevel 1 (
  if exist "%LocalAppData%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" (
    for /d %%D in ("%LocalAppData%\GitHubDesktop\app-*") do set "GIT=%%D\resources\app\git\cmd\git.exe"
  )
)

cd /d "%REPO%" || (echo [오류] 저장소 폴더를 찾을 수 없습니다: %REPO% & pause & exit /b 1)

REM ▼ 오늘 날짜 (YYYY-MM-DD, 로케일 무관)
for /f %%D in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set "TODAY=%%D"

REM ▼ 오늘 리포트 파일을 아카이브 폴더에도 사본 저장 (폴더가 있을 때만)
if exist "%ARCHIVE%" (
  if exist "%REPO%\FPS레이더_%TODAY%.html" (
    copy /Y "%REPO%\FPS레이더_%TODAY%.html" "%ARCHIVE%\" >nul && echo [아카이브] 사본 저장 완료: %ARCHIVE%
  )
) else (
  echo [아카이브] 폴더를 찾을 수 없어 사본 저장 건너뜀: %ARCHIVE%
)

echo [1/4] 원격 변경분 동기화 (rebase)...
"%GIT%" pull --rebase --autostash || (echo [경고] pull 실패 - 네트워크/충돌 확인 & pause & exit /b 1)

echo [2/4] 변경분 스테이징...
"%GIT%" add -A

REM ▼ 변경 없으면 종료
"%GIT%" diff --cached --quiet && (echo [알림] 커밋할 변경사항이 없습니다. & exit /b 0)

echo [3/4] 커밋...
"%GIT%" commit -m "FPS 레이더 %TODAY%" || (echo [오류] 커밋 실패 & pause & exit /b 1)

echo [4/4] 푸시...
"%GIT%" push || (echo [오류] 푸시 실패 - 인증(PAT/SSH) 확인 & pause & exit /b 1)

echo [완료] %TODAY% 편집호 GitHub 반영 + 아카이브 사본 저장 완료.
endlocal