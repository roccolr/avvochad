@echo off
echo Controllo di Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Errore: Python non è installato. Scaricalo da https://www.python.org/downloads/
    pause
    exit /b
)

echo Installazione dei requirements...
pip install -r requirements.txt
pip install google.generativeai
pip install pyinstaller

echo Creazione dell'eseguibile
pyinstaller --onefile --console test.py

echo Installazione completata!
pause
