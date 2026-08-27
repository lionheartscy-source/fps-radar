@echo off
setlocal
set "REPO=C:\Users\LION\Documents\GitHub\fps-radar"
set "GIT=git"
where git >nul 2>nul
if errorlevel 1 (
  for /d %%D in ("%LocalAppData%\GitHubDesktop\app-*") do set "GIT=%%D\resources\app\git\cmd\git.exe"
)
cd /d "%REPO%" || (echo [오류] 폴더 없음: %REPO% & pause & exit /b 1)
for /f %%D in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set "TODAY=%%D"
echo [1/4] pull --rebase ...
"%GIT%" pull --rebase --autostash || (echo [경고] pull 실패 & pause & exit /b 1)
echo [2/4] add ...
"%GIT%" add -A
"%GIT%" diff --cached --quiet && (echo [알림] 변경사항 없음 & exit /b 0)
echo [3/4] commit ...
"%GIT%" commit -m "FPS 레이더 %TODAY%" || (echo [오류] 커밋 실패 & pause & exit /b 1)
echo [4/4] push ...
"%GIT%" push || (echo [오류] 푸시 실패 - 인증 확인 & pause & exit /b 1)
echo [완료] %TODAY% 반영됨. Pages 배포 ~1분.
endlocal