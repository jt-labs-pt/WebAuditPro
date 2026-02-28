@echo off
setlocal
title Auto-Installer & Launcher
cls

echo ====================================================
echo   INITIALIZING SYSTEM...
echo ====================================================

:: 1. CHECK FOR PYTHON
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [NOTICE] Python is missing. Starting automatic installation...
    echo [1/2] Downloading Python (this may take a minute)...
    
    :: Downloads the official Python 3.11 installer via PowerShell
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -OutFile 'python_setup.exe'"
    
    echo [2/2] Installing Python... Please wait for the process to finish.
    :: Installs silently, adds to PATH for all users
    start /wait python_setup.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    :: Cleanup
    del python_setup.exe
    echo [SUCCESS] Python installed!
    echo ----------------------------------------------------
    echo PLEASE CLOSE THIS WINDOW AND RUN 'start_me.bat' AGAIN.
    echo ----------------------------------------------------
    pause
    exit
)

:: 2. SETUP VIRTUAL ENVIRONMENT
if not exist "venv\" (
    echo [SYSTEM] Creating isolated environment (venv)...
    python -m venv venv
)

:: 3. INSTALL LIBRARIES (NO REQUIREMENTS.TXT NEEDED)
echo [SYSTEM] Checking dependencies (whois, requests, bs4)...
call venv\Scripts\activate
python -m pip install --upgrade pip >nul
pip install python-whois requests beautifulsoup4 --quiet

:: 4. RUN YOUR APP
echo [SYSTEM] Starting your application...
echo ----------------------------------------------------
:: Replace 'o_teu_script.py' with your actual filename
python webaudit.py
echo ----------------------------------------------------
echo App closed.
pause
