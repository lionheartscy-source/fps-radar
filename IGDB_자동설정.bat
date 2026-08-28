@echo off
chcp 65001 >nul
title IGDB 매일 자동 동기화 등록 (1회만 실행)
setlocal
set "REPO=%~dp0"
if "%REPO:~-1%"=="\" set "REPO=%REPO:~0,-1%"

echo.
echo ================================================
echo   IGDB 매일 자동 동기화 등록
echo ================================================
echo.

if exist "%REPO%\tools\igdb_config.json" goto :HAVECFG

echo  [중단] tools\igdb_config.json 이 아직 없습니다.
echo.
echo    1. tools\igdb_config.example.json 을 복사
echo    2. 이름을 igdb_config.json 으로 변경
echo    3. Twitch Client ID / Secret 을 채워 넣기
echo.
echo    그 다음 이 파일을 다시 실행하세요.
echo.
pause
exit /b 1

:HAVECFG
echo  [1/2] 지금 한 번 실행해 정상 동작을 확인합니다...
echo.
call "%REPO%\igdb_sync.bat"

echo.
echo  [2/2] 매일 오전 9시 20분 자동 실행 등록...
schtasks /create /tn "FPS레이더 IGDB 동기화" /tr "%REPO%\igdb_sync_auto.bat" /sc daily /st 09:20 /f
if errorlevel 1 goto :FAIL

echo.
echo ================================================
echo   완료. 매일 09:20 에 IGDB 데이터가 갱신됩니다.
echo   (리포트 생성 09:34 보다 먼저 돌아갑니다)
echo   실행 기록: %LocalAppData%\fps-radar-igdb.log
echo ================================================
echo.
pause
exit /b 0

:FAIL
echo.
echo  [실패] 예약 등록 실패. 마우스 오른쪽 - 관리자 권한으로 실행 으로 다시 시도하세요.
echo.
pause
exit /b 1
