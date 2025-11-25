# 🚀 Guida Completa al Deploy - Passo Passo

## 📋 Panoramica

La tua app ha **2 componenti** che vanno deployate separatamente:

1. **Backend Python** (FastAPI) → Railway/Render/Heroku
2. **Frontend Next.js** → Vercel

**Ordine importante**: Deploya prima il BACKEND, poi il FRONTEND.

---

## 🎯 STEP 1: Deploy Backend (Railway - Consigliato)

### Perché Railway?
- ✅ Facile da usare
- ✅ Gratuito per iniziare
- ✅ Deploy automatico da GitHub
- ✅ Supporta Python 3.11/3.12

### Passo 1.1: Crea Account Railway

1. Vai su https://railway.app
2. Clicca **"Start a New Project"**
3. Scegli **"Login with GitHub"**
4. Autorizza Railway ad accedere ai tuoi repository

### Passo 1.2: Crea Nuovo Progetto

1. Clicca **"New Project"**
2. Seleziona **"Deploy from GitHub repo"**
3. Cerca e seleziona il repository: **`Hyper1Crypt/Agent-s`**
4. Railway inizierà a cercare il progetto

### Passo 1.3: Configura il Servizio

Railway potrebbe non riconoscere automaticamente che è un progetto Python. Configuralo così:

1. Clicca sul servizio appena creato
2. Vai su **"Settings"** (icona ingranaggio)
3. Scorri fino a **"Root Directory"**
4. Imposta: **`backend`**
5. Clicca **"Save"**

### Passo 1.4: Configura Python Version

1. Sempre in **Settings**
2. Cerca **"Build Command"** o **"Start Command"**
3. Se non c'è, vai su **"Variables"** tab
4. Aggiungi variabile:
   - **Name**: `PYTHON_VERSION`
   - **Value**: `3.11`
   - Clicca **"Add"**

### Passo 1.5: Configura Start Command

1. In **Settings** → **"Deploy"**
2. Trova **"Start Command"**
3. Inserisci:
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
4. Salva

### Passo 1.6: Aggiungi Variabili Ambiente

1. Vai su **"Variables"** tab
2. Clicca **"New Variable"**
3. Aggiungi queste variabili una per una:

   **Variabile 1:**
   - Name: `OPENAI_API_KEY`
   - Value: `sk-tua-chiave-openai-qui` (sostituisci con la tua chiave reale)
   - Clicca **"Add"**

   **Variabile 2 (opzionale):**
   - Name: `COINGLASS_API_KEY`
   - Value: `tua-chiave-coinglass` (se ce l'hai)
   - Clicca **"Add"**

   **Variabile 3 (opzionale):**
   - Name: `CRYPTOQUANT_API_KEY`
   - Value: `tua-chiave-cryptoquant` (se ce l'hai)
   - Clicca **"Add"**

   **Variabile 4 (opzionale):**
   - Name: `GLASSNODE_API_KEY`
   - Value: `tua-chiave-glassnode` (se ce l'hai)
   - Clicca **"Add"**

### Passo 1.7: Avvia il Deploy

1. Railway dovrebbe iniziare automaticamente il deploy
2. Se non parte, vai su **"Deployments"** tab
3. Clicca **"Redeploy"**
4. Aspetta che finisca (può richiedere 2-5 minuti)

### Passo 1.8: Ottieni URL del Backend

1. Vai su **"Settings"** → **"Networking"**
2. Clicca **"Generate Domain"**
3. Copia l'URL generato (es: `https://your-project.railway.app`)
4. **SALVA QUESTO URL** - ti servirà per il frontend!

### Passo 1.9: Verifica Backend Funziona

1. Apri l'URL del backend nel browser
2. Dovresti vedere: `{"message": "Lab Trading API", "status": "running"}`
3. Aggiungi `/docs` all'URL per vedere la documentazione Swagger
4. Se vedi la documentazione, il backend funziona! ✅

---

## 🎨 STEP 2: Deploy Frontend (Vercel)

### Passo 2.1: Crea Account Vercel

1. Vai su https://vercel.com
2. Clicca **"Sign Up"**
3. Scegli **"Continue with GitHub"**
4. Autorizza Vercel ad accedere ai repository

### Passo 2.2: Importa Progetto

1. Clicca **"Add New Project"**
2. Cerca il repository: **`Hyper1Crypt/Agent-s`**
3. Clicca **"Import"**

### Passo 2.3: Configurazione Progetto

Vercel dovrebbe auto-rilevare Next.js. Verifica:

- **Framework Preset**: Next.js ✅
- **Root Directory**: `./` (root del progetto) ✅
- **Build Command**: `npm run build` ✅
- **Output Directory**: `.next` ✅

Se tutto è corretto, continua.

### Passo 2.4: Aggiungi Variabile Ambiente

**IMPORTANTE**: Prima di deployare, aggiungi la variabile!

1. Nella sezione **"Environment Variables"**
2. Clicca **"Add"** o **"New"**
3. Aggiungi:
   - **Name**: `NEXT_PUBLIC_API_URL`
   - **Value**: L'URL del backend che hai salvato prima (es: `https://your-project.railway.app`)
   - **Environments**: Seleziona tutte (Production, Preview, Development)
   - Clicca **"Add"**

### Passo 2.5: Deploy

1. Clicca **"Deploy"** in basso
2. Aspetta che finisca (1-3 minuti)
3. Vercel ti mostrerà l'URL del frontend (es: `https://your-project.vercel.app`)

### Passo 2.6: Verifica Frontend Funziona

1. Apri l'URL del frontend nel browser
2. Dovresti vedere l'interfaccia della web app
3. Prova a fare una query di test (es: "Qual è il funding rate di BTCUSDT?")
4. Se funziona, sei a posto! ✅

---

## 🔧 Troubleshooting Comune

### Problema: Backend non si avvia su Railway

**Sintomi**: Errori nei log, deploy fallito

**Soluzioni**:
1. Verifica che **Root Directory** sia `backend`
2. Verifica che **Start Command** sia corretto
3. Controlla i log su Railway per errori specifici
4. Assicurati che `OPENAI_API_KEY` sia configurata

### Problema: Frontend non si connette al Backend

**Sintomi**: Errori CORS, 404, o "Network Error"

**Soluzioni**:
1. Verifica che `NEXT_PUBLIC_API_URL` su Vercel sia corretto (senza `/api` alla fine)
2. Verifica che il backend sia online (apri l'URL del backend)
3. Controlla la console del browser (F12) per errori specifici
4. Verifica che il backend accetti richieste CORS (già configurato)

### Problema: Errori Python 3.13

**Sintomi**: Errori durante build del backend

**Soluzioni**:
1. Su Railway, imposta `PYTHON_VERSION=3.11` nelle variabili
2. Oppure modifica `runtime.txt` nel backend con `python-3.11.0`

### Problema: "Module not found" nel Backend

**Sintomi**: Errori Python su moduli mancanti

**Soluzioni**:
1. Verifica che `requirements.txt` sia completo
2. Controlla i log di Railway per vedere quale modulo manca
3. Aggiungi il modulo mancante a `requirements.txt` e fai redeploy

---

## ✅ Checklist Finale

Prima di considerare il deploy completato:

- [ ] Backend deployato e accessibile
- [ ] Backend risponde a `/health` con `{"status": "healthy"}`
- [ ] Frontend deployato e accessibile
- [ ] Variabile `NEXT_PUBLIC_API_URL` configurata su Vercel
- [ ] Frontend si connette al backend
- [ ] Puoi fare una query di test e ricevere una risposta
- [ ] Nessun errore nella console del browser

---

## 🎯 Prossimi Passi Dopo Deploy

1. **Testa tutte le funzionalità**
   - PDF reading
   - News scraping
   - Crypto data
   - Economic calendar

2. **Monitora i log**
   - Railway: Dashboard → Logs
   - Vercel: Dashboard → Logs

3. **Ottimizza (opzionale)**
   - Aggiungi dominio personalizzato
   - Configura rate limiting
   - Aggiungi monitoring (Sentry, etc.)

---

## 📞 Se Hai Problemi

1. **Controlla i log** su Railway e Vercel
2. **Verifica le variabili ambiente** sono corrette
3. **Testa localmente** prima di deployare
4. **Controlla la documentazione** di Railway/Vercel

---

## 🎉 Congratulazioni!

Se hai completato tutti gli step, la tua web app è online e funzionante!

**URL Frontend**: `https://your-project.vercel.app`
**URL Backend**: `https://your-project.railway.app`

Buon lavoro! 🚀

