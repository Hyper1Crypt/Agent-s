"""
Database Tool for storing and retrieving historical data
"""
import sqlite3
import os
from typing import Dict, List, Optional
from langchain.tools import Tool
from datetime import datetime
import json

class DatabaseTool:
    """
    Tool for database operations (store/retrieve historical data)
    """
    
    def __init__(self, db_path: str = "data/trading_history.db"):
        self.name = "database"
        self.description = """Usa questo tool per salvare e recuperare dati storici.
        
Operazioni disponibili:
- save: Salva un'analisi o dato
- retrieve: Recupera dati storici
- search: Cerca nelle analisi passate

Esempio: database("save BTCUSDT analysis 2024-01-15")
         database("retrieve BTCUSDT last_week")
         database("search funding rate BTC")
"""
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Initialize database tables"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                query TEXT,
                report TEXT,
                sources TEXT,
                timestamp TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS market_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                data_type TEXT,
                data_value TEXT,
                timestamp TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _save_analysis(self, symbol: str, query: str, report: str, sources: List[str]) -> str:
        """Save analysis to database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO analyses (symbol, query, report, sources, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (symbol, query, report, json.dumps(sources), datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
            return f"Analisi salvata per {symbol}"
        except Exception as e:
            return f"Errore nel salvare analisi: {str(e)}"
    
    def _retrieve_analysis(self, symbol: str, timeframe: str = "last_week") -> str:
        """Retrieve historical analysis"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if timeframe == "last_week":
                cursor.execute("""
                    SELECT query, report, timestamp FROM analyses
                    WHERE symbol = ? AND created_at >= datetime('now', '-7 days')
                    ORDER BY created_at DESC
                    LIMIT 5
                """, (symbol,))
            elif timeframe == "last_month":
                cursor.execute("""
                    SELECT query, report, timestamp FROM analyses
                    WHERE symbol = ? AND created_at >= datetime('now', '-30 days')
                    ORDER BY created_at DESC
                    LIMIT 10
                """, (symbol,))
            else:
                cursor.execute("""
                    SELECT query, report, timestamp FROM analyses
                    WHERE symbol = ?
                    ORDER BY created_at DESC
                    LIMIT 5
                """, (symbol,))
            
            results = cursor.fetchall()
            conn.close()
            
            if not results:
                return f"Nessuna analisi trovata per {symbol}"
            
            output = f"Analisi storiche per {symbol}:\n\n"
            for i, (query, report, timestamp) in enumerate(results, 1):
                output += f"{i}. Query: {query}\n"
                output += f"   Data: {timestamp}\n"
                output += f"   Report: {report[:200]}...\n\n"
            
            return output
        except Exception as e:
            return f"Errore nel recuperare analisi: {str(e)}"
    
    def _search_analyses(self, search_term: str) -> str:
        """Search in historical analyses"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT symbol, query, report, timestamp FROM analyses
                WHERE query LIKE ? OR report LIKE ?
                ORDER BY created_at DESC
                LIMIT 10
            """, (f"%{search_term}%", f"%{search_term}%"))
            
            results = cursor.fetchall()
            conn.close()
            
            if not results:
                return f"Nessun risultato trovato per: {search_term}"
            
            output = f"Risultati ricerca per '{search_term}':\n\n"
            for i, (symbol, query, report, timestamp) in enumerate(results, 1):
                output += f"{i}. {symbol} - {query}\n"
                output += f"   Data: {timestamp}\n"
                output += f"   Preview: {report[:150]}...\n\n"
            
            return output
        except Exception as e:
            return f"Errore nella ricerca: {str(e)}"
    
    def database_operation(self, input_str: str) -> str:
        """
        Main method for database operations
        Format: "operation [params]"
        """
        try:
            parts = input_str.strip().split(maxsplit=1)
            if len(parts) < 1:
                return "Formato: operation [params]"
            
            operation = parts[0].lower()
            params = parts[1] if len(parts) > 1 else ""
            
            if operation == "save":
                # Parse save operation
                # Format: "save SYMBOL analysis [data]"
                return "Operazione save: implementare parsing completo"
            elif operation == "retrieve":
                # Parse retrieve operation
                # Format: "retrieve SYMBOL [timeframe]"
                symbol_parts = params.split()
                if len(symbol_parts) >= 1:
                    symbol = symbol_parts[0]
                    timeframe = symbol_parts[1] if len(symbol_parts) > 1 else "last_week"
                    return self._retrieve_analysis(symbol, timeframe)
                return "Formato: retrieve SYMBOL [timeframe]"
            elif operation == "search":
                # Search operation
                return self._search_analyses(params)
            else:
                return f"Operazione non supportata: {operation}. Operazioni: save, retrieve, search"
        except Exception as e:
            return f"Errore nell'operazione database: {str(e)}"
    
    def get_tool(self) -> Tool:
        """Return LangChain Tool instance"""
        return Tool(
            name=self.name,
            description=self.description,
            func=self.database_operation
        )

