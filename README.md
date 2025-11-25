<<<<<<< HEAD
# Lab Trading - AI Financial Analyst

Assistente personalizzato di analisi finanziaria per crypto e macroeconomia, costruito con **LangChain** e **Next.js**.

## 🎯 Caratteristiche

- **Analisi Multi-Fonte**: PDF, news, dati crypto, calendario economico
- **Ragionamento Avanzato**: AI che interpreta e collega informazioni
- **Report Operativi**: Conclusioni chiare con azioni consigliate
- **Interfaccia Moderna**: UI pulita e intuitiva
- **Scalabile**: Architettura modulare e ampliabile

## 🏗️ Architettura

### Frontend (Next.js + TypeScript)
- Interfaccia React moderna con Tailwind CSS
- Chat interface per interazioni
- Display report strutturati
- Deploy su Vercel

### Backend (Python + FastAPI + LangChain)
- Agent intelligente con LangChain
- Tools modulari per diverse fonti dati
- API REST per comunicazione
- Database SQLite per storico

## 🚀 Setup

### Prerequisiti

- Node.js 18+
- Python 3.10+
- OpenAI API Key

### Installazione Frontend

```bash
npm install
```

### Installazione Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configurazione

1. Copia `.env.example` in `.env`
2. Aggiungi le tue API keys:

```env
OPENAI_API_KEY=your_key_here
COINGLASS_API_KEY=optional
CRYPTOQUANT_API_KEY=optional
GLASSNODE_API_KEY=optional
```

## 🏃 Esecuzione

### Frontend (sviluppo)

```bash
npm run dev
```

Apri [http://localhost:3000](http://localhost:3000)

### Backend (sviluppo)

```bash
cd backend
uvicorn main:app --reload --port 8000
```

API disponibile su [http://localhost:8000](http://localhost:8000)

## 📦 Tools Disponibili

### 1. PDF Reader
- Legge PDF da URL web o file locali
- Estrazione testo con pypdf e pdfplumber

### 2. News Scraper
- Raccolta news crypto e finanziarie
- Supporto per CoinDesk, CryptoCompare

### 3. Crypto Data
- **Funding Rate**: CoinGlass API
- **Open Interest**: Dati OI in tempo reale
- **Liquidazioni**: Liquidazioni 24h
- **Exchange Flows**: Inflows/outflows (con CryptoQuant)

### 4. Economic Calendar
- Eventi macroeconomici
- Supporto per date specifiche o range

### 5. Database
- Salvataggio analisi storiche
- Ricerca nelle analisi passate
- Recupero dati per timeframe

## 🔧 Esempi di Utilizzo

### Analisi Crypto Completa

```
Analizza BTCUSDT per questa settimana considerando macro, funding e news critiche.
```

### Analisi Macro

```
Quali sono gli eventi macro più importanti di questa settimana?
```

### Ricerca Storica

```
Cerca nelle analisi passate per BTCUSDT
```

## 📁 Struttura Progetto

```
LAB TRADING/
├── app/                    # Next.js app directory
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/             # React components
│   ├── ChatInterface.tsx
│   └── ReportDisplay.tsx
├── backend/               # Python backend
│   ├── main.py           # FastAPI app
│   ├── agent/            # LangChain agent
│   │   └── financial_agent.py
│   └── tools/            # LangChain tools
│       ├── pdf_reader.py
│       ├── news_scraper.py
│       ├── crypto_data.py
│       ├── economic_calendar.py
│       └── database.py
├── data/                 # Database e file locali
├── package.json
├── requirements.txt
└── README.md
```

## 🌐 Deploy

### Frontend su Vercel

1. Push su GitHub
2. Importa progetto su Vercel
3. Configura variabili ambiente
4. Deploy automatico

### Backend

Il backend può essere deployato su:
- **Heroku**
- **Railway**
- **Render**
- **AWS/GCP**

Ricorda di configurare le variabili ambiente nel servizio di hosting.

## 🔐 Sicurezza

- Non committare file `.env`
- Usa variabili ambiente per API keys
- Implementa rate limiting in produzione
- Valida input utente

## 📝 Note

- Alcuni tools usano API pubbliche gratuite (limiti applicabili)
- Per produzione, considera API keys premium per dati più completi
- Il database SQLite può essere sostituito con PostgreSQL per scalabilità

## 🤝 Contribuire

1. Fork il progetto
2. Crea feature branch
3. Commit changes
4. Push e crea Pull Request

## 📄 Licenza

MIT License

---

**Sviluppato con ❤️ per trader e investitori**

=======
# Agent-s
>>>>>>> 3b457c79a3280a6b16c47d0363d391600805a20b
