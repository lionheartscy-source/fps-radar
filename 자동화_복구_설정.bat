@echo off
chcp 949 >nul
title FPS레이더 - 자동화 복구 설정 (1회만 실행)
REM ============================================================
REM  2026-09-07 신설. 이 파일 하나만 더블클릭하면 됩니다.
REM  push_radar.bat 을 따로 실행할 필요 없습니다 (아래 [3/3] 에 포함).
REM   [1] .git 잔여 파일 정리
REM   [2] 예약 작업 재등록 (08:40 / 10:00, 절전 해제, 놓친 실행 따라잡기)
REM   [3] 지금 한 번 업로드
REM ============================================================
setlocal

set "REPO=%~dp0"
if "%REPO:~-1%"=="\" set "REPO=%REPO:~0,-1%"
cd /d "%REPO%"

echo.
echo ================================================
echo   [1/3] .git 잔여 파일 정리
echo ================================================
if exist "%REPO%\.git\index.lock" (del /f /q "%REPO%\.git\index.lock" & echo    - index.lock 삭제)
if exist "%REPO%\.git\HEAD.lock" (del /f /q "%REPO%\.git\HEAD.lock" & echo    - HEAD.lock 삭제)
if exist "%REPO%\.git\objects\maintenance.lock" (del /f /q "%REPO%\.git\objects\maintenance.lock" & echo    - maintenance.lock 삭제)
if exist "%REPO%\.git\__probe_test__" (del /f /q "%REPO%\.git\__probe_test__" & echo    - __probe_test__ 삭제)
echo    완료.

echo.
echo ================================================
echo   [2/3] 예약 작업 재등록
echo ================================================
where powershell >nul 2>nul
if errorlevel 1 goto :NOPS
powershell -NoProfile -ExecutionPolicy Bypass -File "%REPO%\tools\fix_schedules.ps1"
if errorlevel 1 goto :FAIL
REM PowerShell 이 콘솔 코드페이지를 UTF-8 로 바꿔 놓으므로 되돌린다 (한글 깨짐 방지)
chcp 949 >nul

echo.
echo ================================================
echo   설정 요약
echo ================================================
echo    리포트 생성 07:34  ^(Claude 예약 작업^)
echo    자동 업로드 08:40  ^(주^)
echo    IGDB 동기화 09:20
echo    자동 업로드 10:00  ^(예비. 올릴 것 없으면 그냥 끝남^)
echo.
echo    PC 가 자고 있으면 깨워서 실행합니다.
echo    그 시각에 꺼져 있었다면 다음에 켤 때 밀린 분이 올라갑니다.
echo    예약 확인/해제: 시작 메뉴 - "작업 스케줄러"
echo    실행 기록: %%LocalAppData%%\fps-radar-push.log
echo.

echo ================================================
echo   [3/3] 지금 한 번 업로드
echo ================================================
echo    아래부터는 push_radar.bat 의 출력입니다.
echo    이 창은 업로드 결과를 보여준 뒤 키 입력을 기다립니다.
echo.
endlocal
call "%~dp0push_radar.bat"
exit /b 0

:NOPS
echo.
echo  [오류] PowerShell 을 찾을 수 없습니다.
echo.
pause
exit /b 1

:FAIL
echo.
echo  [실패] 예약 등록에 실패했습니다.
echo         이 파일을 오른쪽 클릭 - "관리자 권한으로 실행" 으로 다시 시도해보세요.
echo.
pause
exit /b 1
