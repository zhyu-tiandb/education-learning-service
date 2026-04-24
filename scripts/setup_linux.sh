#!/usr/bin/env bash
set -e

echo "[1/4] Creating virtual environment..."
python3 -m venv .venv

echo "[2/4] Activating virtual environment..."
source .venv/bin/activate

echo "[3/4] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "[4/4] Done. Start service with:"
echo "uvicorn app.main:app --host 127.0.0.1 --port 18080 --reload"
