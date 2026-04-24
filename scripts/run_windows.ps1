$ErrorActionPreference = "Stop"
. .\.venv\Scripts\Activate.ps1
uvicorn app.main:app --host 127.0.0.1 --port 18080 --reload
