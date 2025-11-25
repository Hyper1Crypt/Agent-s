# ⚡ Quick Start - Deploy Rapido

## 🎯 In 5 Minuti

### 1️⃣ Backend su Railway (3 min)

1. Vai su https://railway.app → Login con GitHub
2. New Project → Deploy from GitHub → Seleziona `Agent-s`
3. Settings → Root Directory: `backend`
4. Settings → Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Variables → Aggiungi `OPENAI_API_KEY` = tua chiave
6. Settings → Networking → Generate Domain → **COPIA URL**

### 2️⃣ Frontend su Vercel (2 min)

1. Vai su https://vercel.com → Login con GitHub
2. Add New Project → Seleziona `Agent-s` → Import
3. Environment Variables → Aggiungi:
   - `NEXT_PUBLIC_API_URL` = URL backend copiato prima
4. Deploy → **FATTO!**

### ✅ Verifica

- Backend: Apri URL Railway → Dovresti vedere `{"status": "running"}`
- Frontend: Apri URL Vercel → Dovresti vedere l'interfaccia

**Problemi?** Leggi `GUIDA_DEPLOY.md` per dettagli completi.
