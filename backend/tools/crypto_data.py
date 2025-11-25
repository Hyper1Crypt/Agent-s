"""
Crypto Data Tool for CoinGlass, CryptoQuant, Glassnode integration
"""
import httpx
import os
from typing import Dict, Optional
from langchain.tools import Tool
from datetime import datetime, timedelta

class CryptoDataTool:
    """
    Tool for fetching crypto data from various sources
    """
    
    def __init__(self):
        self.name = "crypto_data"
        self.description = """Usa questo tool per ottenere dati crypto avanzati.
        
Input: simbolo della coppia (es. "BTCUSDT") e tipo di dato richiesto
Tipi disponibili: funding, open_interest, liquidation, on_chain, exchange_flows
        
Esempio: crypto_data("BTCUSDT funding")
         crypto_data("BTCUSDT open_interest")
         crypto_data("BTCUSDT liquidation")
"""
        
        # API keys (should be in environment variables)
        self.coinglass_api_key = os.getenv("COINGLASS_API_KEY", "")
        self.cryptoquant_api_key = os.getenv("CRYPTOQUANT_API_KEY", "")
        self.glassnode_api_key = os.getenv("GLASSNODE_API_KEY", "")
    
    def _get_funding_rate(self, symbol: str) -> str:
        """Get funding rate from CoinGlass"""
        try:
            # CoinGlass public API (no key needed for basic data)
            url = "https://open-api.coinglass.com/public/v2/funding"
            params = {
                "symbol": symbol.replace("USDT", "").replace("USD", "")
            }
            
            response = httpx.get(url, params=params, timeout=10.0, headers={
                "accept": "application/json"
            })
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    funding_data = data["data"][0] if data["data"] else {}
                    return f"""Funding Rate per {symbol}:
- Funding Rate: {funding_data.get('uMarginList', [{}])[0].get('rate', 'N/A')}%
- Exchange: {funding_data.get('exchangeName', 'N/A')}
- Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
            return f"Dati funding non disponibili per {symbol}"
        except Exception as e:
            return f"Errore nel recuperare funding rate: {str(e)}"
    
    def _get_open_interest(self, symbol: str) -> str:
        """Get open interest data"""
        try:
            # Using CoinGlass for OI
            url = "https://open-api.coinglass.com/public/v2/open_interest"
            params = {
                "symbol": symbol.replace("USDT", "").replace("USD", "")
            }
            
            response = httpx.get(url, params=params, timeout=10.0, headers={
                "accept": "application/json"
            })
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    oi_data = data["data"][0] if data["data"] else {}
                    return f"""Open Interest per {symbol}:
- Open Interest: ${oi_data.get('openInterest', 'N/A')}
- Exchange: {oi_data.get('exchangeName', 'N/A')}
- Change 24h: {oi_data.get('change24h', 'N/A')}%
"""
            return f"Dati open interest non disponibili per {symbol}"
        except Exception as e:
            return f"Errore nel recuperare open interest: {str(e)}"
    
    def _get_liquidations(self, symbol: str) -> str:
        """Get liquidation data"""
        try:
            url = "https://open-api.coinglass.com/public/v2/liquidation"
            params = {
                "symbol": symbol.replace("USDT", "").replace("USD", "")
            }
            
            response = httpx.get(url, params=params, timeout=10.0, headers={
                "accept": "application/json"
            })
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    liq_data = data["data"][0] if data["data"] else {}
                    return f"""Liquidazioni per {symbol}:
- Liquidazioni 24h: ${liq_data.get('liquidation24h', 'N/A')}
- Long: ${liq_data.get('longLiquidation', 'N/A')}
- Short: ${liq_data.get('shortLiquidation', 'N/A')}
"""
            return f"Dati liquidazioni non disponibili per {symbol}"
        except Exception as e:
            return f"Errore nel recuperare liquidazioni: {str(e)}"
    
    def _get_exchange_flows(self, symbol: str) -> str:
        """Get exchange flows (inflows/outflows)"""
        try:
            # Using CryptoQuant API if available
            if not self.cryptoquant_api_key:
                return "API key CryptoQuant non configurata"
            
            coin = symbol.replace("USDT", "").replace("USD", "")
            url = f"https://api.cryptoquant.com/v1/btc/exchange-flows"
            params = {
                "exchange": "all",
                "window": "24h"
            }
            headers = {
                "Authorization": f"Bearer {self.cryptoquant_api_key}"
            }
            
            response = httpx.get(url, params=params, headers=headers, timeout=10.0)
            
            if response.status_code == 200:
                data = response.json()
                return f"""Exchange Flows per {coin}:
{data}
"""
            return f"Dati exchange flows non disponibili"
        except Exception as e:
            return f"Errore nel recuperare exchange flows: {str(e)}"
    
    def get_crypto_data(self, input_str: str) -> str:
        """
        Main method to get crypto data
        Format: "SYMBOL TYPE" (e.g., "BTCUSDT funding")
        """
        try:
            parts = input_str.strip().upper().split()
            if len(parts) < 2:
                return "Formato: SYMBOL TYPE (es. BTCUSDT funding)"
            
            symbol = parts[0]
            data_type = parts[1].lower()
            
            if data_type == "funding":
                return self._get_funding_rate(symbol)
            elif data_type == "open_interest" or data_type == "oi":
                return self._get_open_interest(symbol)
            elif data_type == "liquidation" or data_type == "liq":
                return self._get_liquidations(symbol)
            elif data_type == "flows" or data_type == "exchange_flows":
                return self._get_exchange_flows(symbol)
            else:
                return f"Tipo di dato non supportato: {data_type}. Tipi disponibili: funding, open_interest, liquidation, flows"
        except Exception as e:
            return f"Errore nel recuperare dati crypto: {str(e)}"
    
    def get_tool(self) -> Tool:
        """Return LangChain Tool instance"""
        return Tool(
            name=self.name,
            description=self.description,
            func=self.get_crypto_data
        )

