# Architettura del Sistema

## 📐 Overview

Il sistema è diviso in due componenti principali:

1. **Frontend**: Next.js 14 con TypeScript, deployato su Vercel
2. **Backend**: Python FastAPI con LangChain, deployabile su vari servizi

## 🏗️ Struttura Frontend

```
app/
├── layout.tsx          # Layout principale
├── page.tsx            # Pagina home con chat e report
└── globals.css         # Stili globali Tailwind

components/
├── ChatInterface.tsx   # Componente chat per query utente
└── ReportDisplay.tsx   # Componente per visualizzare report
```

### Tecnologie Frontend
- **Next.js 14**: Framework React con App Router
- **TypeScript**: Type safety
- **Tailwind CSS**: Styling moderno
- **Axios**: HTTP client per chiamate API
- **Lucide React**: Icone moderne

## 🔧 Struttura Backend

```
backend/
├── main.py                    # FastAPI application entry point
├── agent/
│   └── financial_agent.py    # Agent principale LangChain
└── tools/
    ├── pdf_reader.py         # Tool per leggere PDF
    ├── news_scraper.py       # Tool per news finanziarie
    ├── crypto_data.py        # Tool per dati crypto (CoinGlass, etc.)
    ├── economic_calendar.py  # Tool per calendario economico
    └── database.py           # Tool per database storico
```

### Tecnologie Backend
- **FastAPI**: Web framework moderno e veloce
- **LangChain**: Framework per applicazioni LLM
- **OpenAI GPT-4**: Modello di linguaggio
- **SQLite**: Database per storico (scalabile a PostgreSQL)
- **Pypdf/pdfplumber**: Lettura PDF
- **BeautifulSoup**: Web scraping
- **httpx**: HTTP client async

## 🔄 Flusso di Dati

```
Utente → Frontend (Next.js) → API Request → Backend (FastAPI)
                                              ↓
                                    Financial Agent (LangChain)
                                              ↓
                                    [Seleziona Tools Necessari]
                                              ↓
                    ┌─────────────────────────┼─────────────────────────┐
                    ↓                         ↓                         ↓
            PDF Reader              News Scraper              Crypto Data
                    ↓                         ↓                         ↓
            Economic Calendar              Database
                    └─────────────────────────┼─────────────────────────┘
                                              ↓
                                    [Elabora Dati]
                                              ↓
                                    [Genera Report]
                                              ↓
                                    Backend → Frontend → Utente
```

## 🧠 Agent Architecture

### Financial Agent

L'agent è costruito con LangChain e utilizza un approccio **tool-calling**:

1. **Input**: Query utente (es. "Analizza BTCUSDT...")
2. **Planning**: L'agent decide quali tools usare
3. **Execution**: Esegue i tools selezionati
4. **Synthesis**: Combina i risultati
5. **Output**: Genera report strutturato

### Tools Disponibili

#### 1. PDF Reader
- **Input**: URL PDF o path file locale
- **Output**: Testo estratto
- **Use Case**: Analisi report macro, whitepaper crypto

#### 2. News Scraper
- **Input**: Query di ricerca
- **Output**: Lista news recenti
- **Sources**: CoinDesk, CryptoCompare, Reuters

#### 3. Crypto Data
- **Input**: Simbolo + tipo dato (funding, OI, liquidations)
- **Output**: Dati strutturati
- **APIs**: CoinGlass (pubblico), CryptoQuant (con key), Glassnode (con key)

#### 4. Economic Calendar
- **Input**: Data o timeframe
- **Output**: Eventi macroeconomici
- **Use Case**: Eventi Fed, CPI, NFP, etc.

#### 5. Database
- **Input**: Operazione (save/retrieve/search)
- **Output**: Dati storici
- **Use Case**: Memoria analisi passate, trend storici

## 📊 Database Schema

### Table: analyses
```sql
- id: INTEGER PRIMARY KEY
- symbol: TEXT
- query: TEXT
- report: TEXT
- sources: TEXT (JSON)
- timestamp: TEXT
- created_at: TEXT
```

### Table: market_data
```sql
- id: INTEGER PRIMARY KEY
- symbol: TEXT
- data_type: TEXT (funding, oi, etc.)
- data_value: TEXT (JSON)
- timestamp: TEXT
- created_at: TEXT
```

## 🔐 Sicurezza

### Environment Variables
- `OPENAI_API_KEY`: Required
- `COINGLASS_API_KEY`: Optional
- `CRYPTOQUANT_API_KEY`: Optional
- `GLASSNODE_API_KEY`: Optional

### Best Practices
- Mai committare `.env`
- Validazione input utente
- Rate limiting (da implementare)
- CORS configurato per domini specifici

## 🚀 Scalabilità

### Frontend
- **Vercel**: Auto-scaling, CDN globale
- **Next.js**: Server-side rendering quando necessario
- **Static Assets**: Ottimizzati automaticamente

### Backend
- **FastAPI**: Async/await per performance
- **Database**: SQLite → PostgreSQL per produzione
- **Caching**: Da implementare (Redis opzionale)
- **Load Balancing**: Supportato da servizi cloud

## 🔌 API Endpoints

### GET `/`
- Health check base

### GET `/health`
- Status check
- Response: `{"status": "healthy"}`

### POST `/api/analyze`
- **Request**: `{"query": "string", "context": {}}`
- **Response**: `{"report": "string", "sources": [], "timestamp": "string"}`
- **Timeout**: 5 minuti (300s)

## 📈 Estensioni Future

### Possibili Aggiunte
1. **ML Models**: Predizioni prezzo, sentiment analysis avanzata
2. **Real-time Data**: WebSocket per dati live
3. **User Accounts**: Multi-utente con storico personale
4. **Advanced Analytics**: Grafici, visualizzazioni
5. **Alerts**: Notifiche per eventi critici
6. **Portfolio Tracking**: Tracking posizioni utente

### Integrazioni Aggiuntive
- **TradingView API**: Grafici avanzati
- **Binance/Coinbase API**: Dati exchange diretti
- **Twitter API**: Sentiment social media
- **Reddit API**: Sentiment community crypto

## 🧪 Testing Strategy

### Unit Tests
- Test per ogni tool
- Test agent logic
- Test database operations

### Integration Tests
- Test API endpoints
- Test agent con tools reali
- Test frontend-backend communication

### E2E Tests
- Test flusso completo utente
- Test con dati reali (sandbox)

## 📝 Note Tecniche

### LangChain Version Compatibility
Il codice supporta multiple versioni di LangChain con fallback:
1. LangChain 0.1.0+ (preferred)
2. LangChain legacy (fallback)
3. Simple LLM (last resort)

### Error Handling
- Try-catch in ogni tool
- Error messages descrittivi
- Logging per debugging
- Graceful degradation

### Performance
- Async operations dove possibile
- Timeout configurabili
- Caching da implementare
- Database indexing per query veloci

