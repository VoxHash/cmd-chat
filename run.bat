@echo off
REM Run script for cmd-chat (Windows)

setlocal enabledelayedexpansion

REM Check if virtual environment exists
if not exist "venv" (
    echo ⚠️  Virtual environment not found
    echo 💡 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import sanic" 2>nul
if errorlevel 1 (
    echo ⚠️  Dependencies not installed
    echo 💡 Installing dependencies...
    pip install -r requirements.txt
)

REM Run the application
echo 🚀 Starting cmd-chat...
python run.py %*

