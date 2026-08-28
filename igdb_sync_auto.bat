@echo off
chcp 65001 >nul
REM 작업 스케줄러가 매일 09:20 에 호출하는 래퍼입니다. 직접 실행할 필요 없습니다.
setlocal
set "LOG=%LocalAppData%\fps-radar-igdb.log"
cd /d "%~dp0"
>>"%LOG%" echo.
>>"%LOG%" echo ===== %DATE% %TIME% =====
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\igdb_sync.ps1" <nul >>"%LOG%" 2>&1
>>"%LOG%" echo ----- exit code: %errorlevel% -----
endlocal
