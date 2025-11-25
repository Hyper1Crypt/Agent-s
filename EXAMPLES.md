# Esempi di Utilizzo

## 💬 Query di Esempio

### Analisi Crypto Completa

```
Analizza BTCUSDT per questa settimana considerando macro, funding e news critiche.
```

**Cosa fa l'agent:**
1. Recupera funding rate da CoinGlass
2. Cerca news recenti su Bitcoin
3. Controlla eventi macro della settimana
4. Genera report completo con conclusioni operative

### Analisi Solo Funding

```
Qual è il funding rate attuale di BTCUSDT? Mostra anche open interest e liquidazioni recenti.
```

**Cosa fa l'agent:**
1. Chiama crypto_data tool per funding
2. Recupera open interest
3. Recupera dati liquidazioni
4. Presenta dati strutturati

### Analisi Macro

```
Quali sono gli eventi macro più importanti di questa settimana? Analizza il loro impatto potenziale sul mercato crypto.
```

**Cosa fa l'agent:**
1. Recupera calendario economico
2. Identifica eventi ad alto impatto
3. Analizza correlazione con crypto
4. Fornisce valutazione rischio/opportunità

### Analisi PDF

```
Analizza questo report macro: https://example.com/macro-report-2024.pdf
```

**Cosa fa l'agent:**
1. Scarica PDF dall'URL
2. Estrae testo completo
3. Analizza contenuto
4. Genera summary e insights

### Ricerca Storica

```
Cerca nelle analisi passate per BTCUSDT. Quali erano le conclusioni la scorsa settimana?
```

**Cosa fa l'agent:**
1. Interroga database storico
2. Recupera analisi precedenti
3. Confronta con situazione attuale
4. Evidenzia cambiamenti

### Analisi Sentiment

```
Qual è il sentiment attuale del mercato crypto? Cosa dicono le news?
```

**Cosa fa l'agent:**
1. Raccoglie news recenti
2. Analizza tono e contenuto
3. Valuta sentiment generale
4. Identifica temi ricorrenti

## 📊 Esempi di Report Generati

### Report Completo BTCUSDT

```
# Analisi BTCUSDT - Settimana Corrente

## Contesto Macroeconomico
- Eventi Fed previsti: Decisione tassi interesse mercoledì
- CPI in uscita giovedì: Previsione +0.3%
- Impatto atteso: Neutrale-Positivo per crypto

## Dati di Mercato
- Prezzo attuale: $42,500
- Funding Rate: 0.01% (neutrale)
- Open Interest: $12.5B (+5% settimanale)

## News Critiche
1. Approvazione ETF Bitcoin: Impatto positivo
2. Regolamentazione EU: Incertezza
3. Adozione istituzionale: Trend positivo

## Analisi del Sentiment
- Sentiment generale: Positivo (65%)
- Fattori positivi: ETF, adozione istituzionale
- Fattori negativi: Regolamentazione, volatilità

## Rischi e Opportunità
- Rischio: Correzione tecnica possibile
- Opportunità: Breakout sopra $45k

## Conclusione Operativa
**Azione Consigliata**: Posizione long con stop loss a $40k
**Motivazione**: Trend positivo, funding neutrale, eventi macro favorevoli
```

## 🔧 Esempi di Integrazione API

### Test Backend Diretto

```python
import requests

url = "http://localhost:8000/api/analyze"
payload = {
    "query": "Analizza BTCUSDT funding rate"
}

response = requests.post(url, json=payload)
print(response.json())
```

### Test con Python Async

```python
import asyncio
from agent.financial_agent import FinancialAgent

async def test():
    agent = FinancialAgent()
    result = await agent.analyze("Qual è il funding rate di BTCUSDT?")
    print(result['report'])

asyncio.run(test())
```

## 🎯 Best Practices

### Query Efficaci

✅ **Buone query:**
- Specifiche e chiare
- Includono contesto (timeframe, simbolo)
- Richiedono dati concreti

❌ **Query da evitare:**
- Troppo generiche ("Analizza tutto")
- Senza contesto
- Richieste impossibili ("Prevedi il futuro")

### Esempi Ottimali

```
✅ "Analizza BTCUSDT per questa settimana considerando macro, funding e news"
✅ "Qual è il sentiment attuale del mercato crypto basato sulle news?"
✅ "Confronta il funding rate di BTCUSDT con quello di ETHUSDT"
```

```
❌ "Dimmi tutto"
❌ "Cosa succederà domani?"
❌ "Analizza"
```

## 📈 Use Cases Reali

### Trader Giornaliero
```
Ogni mattina: "Quali sono gli eventi macro di oggi? Analizza BTCUSDT considerando funding e news."
```

### Investitore Swing
```
Settimanale: "Analisi completa BTCUSDT per questa settimana. Includi macro, sentiment e dati on-chain."
```

### Analista Macro
```
"Analizza questo report Fed: [URL PDF]. Qual è l'impatto previsto su crypto?"
```

## 🔍 Debugging

### Verifica Tools

```python
# Test singolo tool
from tools.crypto_data import CryptoDataTool

tool = CryptoDataTool()
result = tool.get_crypto_data("BTCUSDT funding")
print(result)
```

### Verifica Database

```python
from tools.database import DatabaseTool

db = DatabaseTool()
result = db.database_operation("retrieve BTCUSDT last_week")
print(result)
```

## 📝 Note

- Le query possono richiedere 30-60 secondi per analisi complete
- Alcuni tools hanno rate limits (API pubbliche)
- Per produzione, considera API keys premium per dati più completi
- Il database si popola automaticamente con ogni analisi

