$ErrorActionPreference = "Stop"

Write-Host "[1/4] Creating virtual environment..."
python -m venv .venv

Write-Host "[2/4] Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "[3/4] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "[4/4] Done. Start service with:"
Write-Host "uvicorn app.main:app --host 127.0.0.1 --port 18080 --reload"
