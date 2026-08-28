@echo off
chcp 949 >nul
title FPS레이더 - GitHub 업로드
REM ============================================================
REM  FPS레이더 커밋·푸시 + 아카이브 사본 저장
REM  - 시작 시 잔여 .git 잠금 파일을 먼저 정리한다
REM  - 각 단계 실패 시 원인을 화면에 남기고 멈춘다
REM ============================================================
setlocal

set "REPO=C:\Users\LION\Documents\GitHub\fps-radar"
set "ARCHIVE=C:\Users\LION\Desktop\Project S\14. 일간 FPS 이벤트 동향 리서칭"

REM ── git 실행파일 찾기 (PATH 우선, 없으면 GitHub Desktop 번들)
set "GIT=git"
where git >nul 2>nul
if not errorlevel 1 goto :GITOK
for /d %%D in ("%LocalAppData%\GitHubDesktop\app-*") do set "GIT=%%D\resources\app\git\cmd\git.exe"
:GITOK

cd /d "%REPO%"
if errorlevel 1 goto :NOREPO

REM ── 잔여 잠금 파일 정리 (이게 있으면 git 이 통째로 막힌다)
if exist "%REPO%\.git\index.lock" del /f /q "%REPO%\.git\index.lock" >nul 2>nul
if exist "%REPO%\.git\HEAD.lock" del /f /q "%REPO%\.git\HEAD.lock" >nul 2>nul
if exist "%REPO%\.git\objects\maintenance.lock" del /f /q "%REPO%\.git\objects\maintenance.lock" >nul 2>nul
if exist "%REPO%\.git\index.lock" goto :LOCKED

for /f %%D in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set "TODAY=%%D"

REM ── 저장소 루트에 오늘 리포트가 있으면 아카이브 폴더에도 사본 저장
if not exist "%ARCHIVE%" goto :ARCHSKIP
if not exist "%REPO%\FPS레이더_%TODAY%.html" goto :ARCHDONE
copy /Y "%REPO%\FPS레이더_%TODAY%.html" "%ARCHIVE%\" >nul
echo [아카이브] 사본 저장 완료
goto :ARCHDONE
:ARCHSKIP
echo [아카이브] 폴더를 찾을 수 없어 건너뜀
:ARCHDONE

echo.
echo [1/4] 원격 동기화 (pull --rebase)...
"%GIT%" pull --rebase --autostash
if errorlevel 1 goto :FAILPULL

echo.
echo [2/4] 변경분 스테이징...
"%GIT%" add -A
if errorlevel 1 goto :FAILADD

"%GIT%" diff --cached --quiet
if not errorlevel 1 goto :NOCHANGE

echo.
echo [3/4] 커밋...
"%GIT%" commit -m "FPS Radar %TODAY%"
if errorlevel 1 goto :FAILCOMMIT

echo.
echo [4/4] 푸시...
"%GIT%" push
if errorlevel 1 goto :FAILPUSH

echo.
echo ============================================
echo  [완료] %TODAY% GitHub 반영 완료
echo ============================================
goto :END

:NOCHANGE
echo.
echo  [알림] 커밋할 변경사항이 없습니다. (이미 모두 반영된 상태)
goto :END

:NOREPO
echo.
echo  [오류] 저장소 폴더를 찾을 수 없습니다: %REPO%
goto :END

:LOCKED
echo.
echo  [오류] .git\index.lock 을 지울 수 없습니다.
echo         GitHub Desktop 이나 다른 git 프로그램이 실행 중이면 종료하고 다시 시도하세요.
goto :END

:FAILPULL
echo.
echo  [실패] 원격 동기화(pull) 오류. 위 메시지를 확인하세요.
echo         네트워크 문제이거나 충돌일 수 있습니다.
goto :END

:FAILADD
echo.
echo  [실패] 스테이징(add) 오류. 위 메시지를 확인하세요.
goto :END

:FAILCOMMIT
echo.
echo  [실패] 커밋 오류. 위 메시지를 확인하세요.
goto :END

:FAILPUSH
echo.
echo  [실패] 푸시 오류. 위 메시지를 확인하세요.
echo         인증 문제로 보이면 깃허브_자동설정.bat 을 다시 실행해 로그인하세요.
goto :END

:END
echo.
pause
endlocal
