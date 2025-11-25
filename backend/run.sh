#!/bin/bash

# Script per avviare il backend
cd "$(dirname "$0")"

# Attiva virtual environment se esiste
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Avvia FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8000

