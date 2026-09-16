@echo off
setlocal EnableExtensions EnableDelayedExpansion

title Ryutai Local Preview

set "BASE_DIR=C:\Users\yuki_\OneDrive\Documents\github"
set "REPO_DIR=%BASE_DIR%\product_blog_ryutai"
set "REPO_URL=https://github.com/yuki746289/product_blog_ryutai.git"
set "BRANCH=develop"

echo.
echo ========================================
echo   Ryutai Local Preview
echo ========================================
echo.

where git.exe >nul 2>&1
if errorlevel 1 (
    echo [ERROR] git.exe was not found.
    echo Git for Windows must be installed and added to PATH.
    goto :error
)

set "BASH_EXE="
if exist "C:\Program Files\Git\bin\bash.exe" (
    set "BASH_EXE=C:\Program Files\Git\bin\bash.exe"
) else if exist "C:\Program Files (x86)\Git\bin\bash.exe" (
    set "BASH_EXE=C:\Program Files (x86)\Git\bin\bash.exe"
) else (
    for /f "delims=" %%I in ('where bash.exe 2^>nul') do (
        if not defined BASH_EXE set "BASH_EXE=%%I"
    )
)

if not defined BASH_EXE (
    echo [ERROR] Git Bash ^(bash.exe^) was not found.
    echo Expected location:
    echo   C:\Program Files\Git\bin\bash.exe
    goto :error
)

if not exist "%BASE_DIR%" (
    echo [INFO] Creating:
    echo   %BASE_DIR%
    mkdir "%BASE_DIR%"
    if errorlevel 1 goto :error
)

if not exist "%REPO_DIR%\.git" (
    echo [INFO] Repository not found. Cloning develop...
    git clone -b "%BRANCH%" "%REPO_URL%" "%REPO_DIR%"
    if errorlevel 1 (
        echo [ERROR] git clone failed.
        goto :error
    )
) else (
    echo [INFO] Repository already exists.
)

cd /d "%REPO_DIR%"
if errorlevel 1 goto :error

echo [INFO] Switching to %BRANCH%...
git checkout "%BRANCH%"
if errorlevel 1 goto :error

echo [INFO] Pulling latest %BRANCH%...
git pull --ff-only origin "%BRANCH%"
if errorlevel 1 (
    echo.
    echo [ERROR] git pull failed.
    echo Local changes or branch divergence may exist.
    echo Please check:
    echo   %REPO_DIR%
    goto :error
)

if not exist "%REPO_DIR%\deploy_local.sh" (
    echo [ERROR] deploy_local.sh was not found after pull.
    goto :error
)

echo.
echo [INFO] Deploying to Apache local folder...
"%BASH_EXE%" -lc "cd '/c/Users/yuki_/OneDrive/Documents/github/product_blog_ryutai' && bash deploy_local.sh"
if errorlevel 1 (
    echo [ERROR] Local deploy failed.
    goto :error
)

echo.
echo ========================================
echo   Completed successfully
echo ========================================
echo.
echo Local URL:
echo   http://localhost/ryutai/
echo.
pause
exit /b 0

:error
echo.
echo ========================================
echo   FAILED
echo ========================================
echo.
echo Please copy the error message above and send it to ChatGPT.
echo.
pause
exit /b 1
