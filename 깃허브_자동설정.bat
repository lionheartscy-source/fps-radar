@echo off
chcp 949 >nul
title FPS레이더 - GitHub 자동 업로드 설정 (1회만 실행)
REM ============================================================
REM  이 파일은 한 번만 더블클릭하면 됩니다.
REM   [1] 잔여 잠금 파일 정리
REM   [2] GitHub 인증을 Windows에 저장 (브라우저 로그인 1회)
REM   [3] 밀린 리포트 업로드
REM   [4] 매일 오전 10시 자동 업로드 예약 등록
REM ============================================================
setlocal enabledelayedexpansion

set "REPO=C:\Users\LION\Documents\GitHub\fps-radar"

REM ── git 실행파일 찾기 (PATH 우선, 없으면 GitHub Desktop 번들 git)
set "GIT=git"
where git >nul 2>nul
if errorlevel 1 (
  if exist "%LocalAppData%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe" (
    for /d %%D in ("%LocalAppData%\GitHubDesktop\app-*") do set "GIT=%%D\resources\app\git\cmd\git.exe"
  )
)
"%GIT%" --version >nul 2>nul
if errorlevel 1 (
  echo.
  echo  [오류] git 을 찾을 수 없습니다.
  echo         https://git-scm.com/download/win 에서 Git for Windows 를 설치한 뒤 다시 실행하세요.
  echo.
  pause
  exit /b 1
)

cd /d "%REPO%" || (echo  [오류] 저장소 폴더를 찾을 수 없습니다: %REPO% & pause & exit /b 1)

echo.
echo ================================================
echo   [1/4] 잔여 잠금 파일 정리
echo ================================================
if exist "%REPO%\.git\index.lock" (del /f /q "%REPO%\.git\index.lock" & echo    - index.lock 삭제)
if exist "%REPO%\.git\HEAD.lock" (del /f /q "%REPO%\.git\HEAD.lock" & echo    - HEAD.lock 삭제)
if exist "%REPO%\.git\objects\maintenance.lock" (del /f /q "%REPO%\.git\objects\maintenance.lock" & echo    - maintenance.lock 삭제)
echo    완료.

echo.
echo ================================================
echo   [2/4] 인증 저장 방식 설정
echo ================================================
set "CH="
for /f "delims=" %%H in ('"%GIT%" config --global credential.helper 2^>nul') do set "CH=%%H"
if not defined CH (
  "%GIT%" config --global credential.helper manager
  echo    credential.helper = manager  ^(새로 설정^)
) else (
  echo    credential.helper = !CH!  ^(기존 설정 유지^)
)
"%GIT%" config --global --replace-all user.name "cheesepizza"
"%GIT%" config --global --replace-all user.email "cheesepizza@lionhearts.co.kr"
"%GIT%" config core.autocrlf false
echo    완료.

echo.
echo ================================================
echo   [3/4] GitHub 로그인 + 밀린 리포트 업로드
echo ================================================
echo    브라우저 창이 뜨면 GitHub 계정으로 로그인하세요.
echo    (최초 1회만 뜨고, 이후에는 자동으로 처리됩니다)
echo.
"%GIT%" pull --rebase --autostash
"%GIT%" push
if errorlevel 1 (
  echo.
  echo    [실패] 업로드에 실패했습니다. 위 메시지를 확인하세요.
  echo           로그인 창이 안 떴다면 Git for Windows 를 최신 버전으로 다시 설치해보세요.
  echo.
  pause
  exit /b 1
)
echo    업로드 성공.

echo.
echo ================================================
echo   [4/4] 매일 오전 10시 자동 업로드 예약 등록
echo ================================================
schtasks /create /tn "FPS레이더 자동 업로드" /tr "%REPO%\push_radar_auto.bat" /sc daily /st 10:00 /f
if errorlevel 1 (
  echo.
  echo    [실패] 예약 등록에 실패했습니다.
  echo           이 파일을 마우스 오른쪽 클릭 - "관리자 권한으로 실행" 으로 다시 시도해보세요.
  echo.
  pause
  exit /b 1
)
echo    등록 완료.

echo.
echo ================================================
echo   설정이 모두 끝났습니다.
echo.
echo   - 매일 오전 10시에 자동으로 GitHub 에 올라갑니다.
echo   - PC 가 켜져 있고 로그인된 상태여야 합니다.
echo   - 실행 기록: %LocalAppData%\fps-radar-push.log
echo   - 예약 확인/해제: 시작 메뉴 - "작업 스케줄러"
echo ================================================
echo.
pause
endlocal
