@echo off
chcp 949 >nul
REM ============================================================
REM  작업 스케줄러가 매일 호출하는 래퍼입니다. 직접 실행할 필요 없습니다.
REM  - push_radar.bat 을 사람 개입 없이 실행 (< nul 로 pause 무한대기 방지)
REM  - 실행 기록을 저장소 밖 로그 파일에 남김 (저장소 오염 방지)
REM ============================================================
setlocal
set "LOG=%LocalAppData%\fps-radar-push.log"
cd /d "%~dp0"

REM 잔여 잠금 파일이 있으면 정리
if exist "%~dp0.git\index.lock" del /f /q "%~dp0.git\index.lock" 2>nul
if exist "%~dp0.git\HEAD.lock" del /f /q "%~dp0.git\HEAD.lock" 2>nul

>>"%LOG%" echo.
>>"%LOG%" echo ===== %DATE% %TIME% =====
call "%~dp0push_radar.bat" <nul >>"%LOG%" 2>&1
>>"%LOG%" echo ----- exit code: %errorlevel% -----
endlocal
