# 🚀 Guida al Deploy Completa

## 📋 Prerequisiti

Prima di deployare, assicurati di avere:
- ✅ Repository GitHub configurato
- ✅ OpenAI API Key
- ✅ Account Vercel (per frontend)
- ✅ Account per backend hosting (Railway/Render/Heroku)

---

## 🎨 Deploy Frontend su Vercel

### Step 1: Connetti Repository

1. Vai su [Vercel](https://vercel.com)
2. Clicca "Add New Project"
3. Importa il repository `Hyper1Crypt/Agent-s`
4. Vercel rileverà automaticamente Next.js

### Step 2: Configurazione Build

Vercel dovrebbe auto-configurare:
- **Framework Preset**: Next.js
- **Root Directory**: `/` (root del progetto)
- **Build Command**: `npm run build`
- **Output Directory**: `.next`

### Step 3: Variabili Ambiente

Aggiungi queste variabili ambiente su Vercel:

```
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

**⚠️ IMPORTANTE**: Sostituisci `your-backend-url.railway.app` con l'URL del tuo backend deployato.

### Step 4: Deploy

Clicca "Deploy" e aspetta il completamento.

**URL Frontend**: `https://your-project.vercel.app`

---

## ⚙️ Deploy Backend

### Opzione 1: Railway (Consigliato) 🚂

#### Setup Railway

1. Vai su [Railway](https://railway.app)
2. Clicca "New Project"
3. Seleziona "Deploy from GitHub repo"
4. Scegli il repository `Hyper1Crypt/Agent-s`

#### Configurazione

1. **Root Directory**: Imposta a `/backend`
2. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. **Python Version**: 3.11 o 3.12 (evita 3.13 per compatibilità)

#### Variabili Ambiente

Aggiungi su Railway:

```
OPENAI_API_KEY=sk-your-key-here
COINGLASS_API_KEY=optional
CRYPTOQUANT_API_KEY=optional
GLASSNODE_API_KEY=optional
PORT=8000
```

#### Deploy

Railway installerà automaticamente le dipendenze da `requirements.txt` e avvierà il server.

**URL Backend**: `https://your-project.railway.app`

---

### Opzione 2: Render 🎨

#### Setup Render

1. Vai su [Render](https://render.com)
2. Clicca "New Web Service"
3. Connetti il repository GitHub

#### Configurazione

- **Name**: `lab-trading-backend`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Root Directory**: `/backend`

#### Variabili Ambiente

Stesse variabili di Railway.

---

### Opzione 3: Heroku 🟣

#### Setup Heroku

1. Installa [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Crea app: `heroku create your-app-name`

#### Configurazione

```bash
cd backend
heroku config:set OPENAI_API_KEY=sk-your-key-here
heroku config:set PORT=8000
```

#### Deploy

```bash
git subtree push --prefix backend heroku main
```

Oppure usa il Procfile già presente.

---

## 🔗 Collegare Frontend e Backend

### Dopo il Deploy del Backend

1. Copia l'URL del backend (es. `https://your-backend.railway.app`)
2. Vai su Vercel → Settings → Environment Variables
3. Aggiorna `NEXT_PUBLIC_API_URL` con l'URL del backend
4. Riavvia il deployment su Vercel

### Verifica Connessione

1. Apri il frontend deployato
2. Apri la console del browser (F12)
3. Prova a fare una query
4. Controlla che le chiamate API vadano al backend corretto

---

## ✅ Checklist Pre-Deploy

### Frontend
- [ ] Repository GitHub configurato
- [ ] `package.json` con tutte le dipendenze
- [ ] `next.config.js` configurato
- [ ] Variabile `NEXT_PUBLIC_API_URL` pronta

### Backend
- [ ] `requirements.txt` completo
- [ ] `Procfile` presente (per Heroku)
- [ ] `main.py` con CORS configurato
- [ ] Variabili ambiente configurate
- [ ] OpenAI API Key pronta

---

## 🐛 Troubleshooting Deploy

### Frontend non si connette al Backend

**Problema**: CORS errors o 404

**Soluzione**:
1. Verifica che `NEXT_PUBLIC_API_URL` sia corretto su Vercel
2. Controlla che il backend accetti richieste dal dominio Vercel
3. Verifica i log del backend per errori CORS

### Backend non si avvia

**Problema**: Errori durante il build o startup

**Soluzione**:
1. Controlla i log del servizio di hosting
2. Verifica che tutte le dipendenze siano in `requirements.txt`
3. Assicurati che Python version sia 3.11 o 3.12
4. Controlla che `OPENAI_API_KEY` sia configurata

### Errori "Module not found"

**Problema**: Dipendenze mancanti

**Soluzione**:
1. Verifica `requirements.txt` completo
2. Controlla che il root directory sia `/backend`
3. Riavvia il deployment

---

## 🔐 Sicurezza in Produzione

### Best Practices

1. **Non committare `.env`**: Già nel `.gitignore`
2. **Usa HTTPS**: Vercel e Railway lo forniscono automaticamente
3. **Rate Limiting**: Considera di aggiungere rate limiting al backend
4. **API Keys**: Usa variabili ambiente, mai hardcoded
5. **CORS**: Restringi gli origins in produzione se possibile

### Esempio CORS Ristretto

Nel `backend/main.py`, puoi restringere CORS:

```python
cors_origins = [
    "https://your-frontend.vercel.app",
    "https://your-frontend-production.vercel.app",
]
```

---

## 📊 Monitoraggio

### Vercel Analytics

Vercel fornisce analytics automatici per il frontend.

### Backend Logs

- **Railway**: Dashboard → Logs
- **Render**: Dashboard → Logs
- **Heroku**: `heroku logs --tail`

---

## 🎯 Prossimi Passi Dopo Deploy

1. ✅ Testa tutte le funzionalità
2. ✅ Verifica che le API keys funzionino
3. ✅ Monitora i log per errori
4. ✅ Configura un dominio personalizzato (opzionale)
5. ✅ Aggiungi monitoring/alerting (opzionale)

---

## 📞 Supporto

Se hai problemi durante il deploy:
1. Controlla i log del servizio
2. Verifica le variabili ambiente
3. Testa localmente prima di deployare
4. Consulta la documentazione del servizio di hosting

---

**Buon deploy! 🚀**

