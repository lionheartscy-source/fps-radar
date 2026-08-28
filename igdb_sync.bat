@echo off
chcp 65001 >nul
title IGDB 동기화 - FPS레이더
REM ============================================================
REM  IGDB 에서 게임 커버·아트워크와 신작 캘린더를 받아옵니다.
REM   - assets/igdb_cache.json     게임별 이미지·메타
REM   - assets/igdb_upcoming.json  향후 슈터 신작 목록
REM  PowerShell 로 동작하므로 별도 설치가 필요 없습니다.
REM ============================================================
setlocal
cd /d "%~dp0"

where powershell >nul 2>nul
if errorlevel 1 goto :NOPS

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\igdb_sync.ps1"
set "RC=%errorlevel%"
echo.
pause
exit /b %RC%

:NOPS
echo.
echo  [오류] PowerShell 을 찾을 수 없습니다.
echo         Windows 기본 구성 요소라 보통 있어야 합니다.
echo         시작 메뉴에서 "PowerShell" 을 검색해 실행되는지 확인해 주세요.
echo.
pause
exit /b 1
