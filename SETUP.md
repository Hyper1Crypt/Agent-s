# Guida Setup Completa

## 🚀 Quick Start

### 1. Setup Frontend

```bash
# Installa dipendenze
npm install

# Avvia in sviluppo
npm run dev
```

Il frontend sarà disponibile su `http://localhost:3000`

### 2. Setup Backend

```bash
# Vai nella cartella backend
cd backend

# Crea virtual environment
python -m venv venv

# Attiva virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Installa dipendenze
pip install -r requirements.txt
```

### 3. Configurazione Environment

Crea un file `.env` nella root del progetto:

```env
# OpenAI (REQUIRED)
OPENAI_API_KEY=sk-your-key-here

# Crypto APIs (Optional - per funzionalità avanzate)
COINGLASS_API_KEY=your_key_here
CRYPTOQUANT_API_KEY=your_key_here
GLASSNODE_API_KEY=your_key_here

# API URL (per frontend)
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 4. Avvia Backend

```bash
# Dalla cartella backend
uvicorn main:app --reload --port 8000

# Oppure usa lo script
./run.sh
```

Il backend sarà disponibile su `http://localhost:8000`

## 📋 Verifica Installazione

### Test Frontend
Apri `http://localhost:3000` - dovresti vedere l'interfaccia

### Test Backend
Apri `http://localhost:8000/docs` - dovresti vedere la documentazione Swagger

### Test API
```bash
curl http://localhost:8000/health
```

Dovresti ricevere: `{"status": "healthy"}`

## 🔧 Troubleshooting

### Errore: "OPENAI_API_KEY non trovata"
- Verifica che il file `.env` esista
- Verifica che la chiave sia corretta
- Riavvia il backend dopo aver modificato `.env`

### Errore: "Module not found"
- Assicurati di aver attivato il virtual environment
- Reinstalla le dipendenze: `pip install -r requirements.txt`

### Errore: Porta già in uso
- Cambia la porta nel comando uvicorn: `--port 8001`
- Aggiorna `NEXT_PUBLIC_API_URL` nel `.env`

### Frontend non si connette al backend
- Verifica che il backend sia in esecuzione
- Controlla `NEXT_PUBLIC_API_URL` nel `.env`
- Verifica CORS nel backend (già configurato per localhost:3000)

## 🌐 Deploy

### Frontend su Vercel

1. Push su GitHub
2. Vai su [Vercel](https://vercel.com)
3. Importa il repository
4. Configura variabili ambiente:
   - `NEXT_PUBLIC_API_URL` = URL del tuo backend deployato
5. Deploy!

### Backend su Heroku/Railway/Render

1. Assicurati di avere `Procfile` e `requirements.txt`
2. Push su GitHub
3. Connetti il repository al servizio
4. Configura variabili ambiente:
   - `OPENAI_API_KEY`
   - `COINGLASS_API_KEY` (opzionale)
   - `CRYPTOQUANT_API_KEY` (opzionale)
   - `GLASSNODE_API_KEY` (opzionale)
5. Deploy!

## 📝 Note Importanti

- **API Keys**: Alcuni tools funzionano senza API keys (usando API pubbliche), ma per funzionalità complete serve almeno `OPENAI_API_KEY`
- **Rate Limits**: Le API pubbliche hanno limiti di rate, considera upgrade per produzione
- **Database**: Il database SQLite viene creato automaticamente nella cartella `data/`

## 🎯 Prossimi Passi

1. Ottieni una OpenAI API Key da [platform.openai.com](https://platform.openai.com)
2. Testa l'app con una query semplice
3. Personalizza i tools secondo le tue esigenze
4. Aggiungi altre fonti dati se necessario

