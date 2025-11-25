"""
Script di test per verificare il funzionamento dell'agent
"""
import os
import asyncio
from dotenv import load_dotenv
from agent.financial_agent import FinancialAgent

load_dotenv()

async def test_agent():
    """Test base dell'agent"""
    print("🚀 Inizializzazione Financial Agent...")
    
    try:
        agent = FinancialAgent()
        print("✅ Agent inizializzato correttamente\n")
    except Exception as e:
        print(f"❌ Errore nell'inizializzazione: {e}")
        return
    
    # Test query semplice
    test_queries = [
        "Qual è il funding rate attuale di BTCUSDT?",
        "Cerca news recenti su Bitcoin",
        "Quali eventi macro sono previsti per questa settimana?",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*60}")
        print(f"Test {i}/{len(test_queries)}")
        print(f"Query: {query}")
        print(f"{'='*60}\n")
        
        try:
            result = await agent.analyze(query)
            print(f"✅ Risultato:")
            print(f"{result['report'][:500]}...")  # Mostra primi 500 caratteri
            print(f"\nTimestamp: {result['timestamp']}")
        except Exception as e:
            print(f"❌ Errore: {e}")
        
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    # Verifica API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY non trovata nel file .env")
        print("Aggiungi la chiave nel file .env nella root del progetto")
        exit(1)
    
    print("🧪 Test Financial Agent\n")
    asyncio.run(test_agent())

