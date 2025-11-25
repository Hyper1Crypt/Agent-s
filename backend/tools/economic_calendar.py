"""
Economic Calendar Tool for macro events
"""
import httpx
from typing import List, Dict
from langchain.tools import Tool
from datetime import datetime, timedelta

class EconomicCalendarTool:
    """
    Tool for fetching economic calendar events
    """
    
    def __init__(self):
        self.name = "economic_calendar"
        self.description = """Usa questo tool per ottenere eventi del calendario economico.
        
Input: data (opzionale, formato YYYY-MM-DD) o "today", "tomorrow", "this_week"
Output: Lista di eventi macroeconomici
        
Esempio: economic_calendar("today")
         economic_calendar("2024-01-15")
         economic_calendar("this_week")
"""
    
    def _get_events_from_api(self, start_date: str, end_date: str) -> List[Dict]:
        """Get events from free economic calendar API"""
        try:
            # Using TradingEconomics API (free tier) or alternative
            # For demo, we'll use a mock structure that can be replaced with real API
            
            # Alternative: Investing.com scraping or other free APIs
            url = "https://api.tradingeconomics.com/calendar"
            # Note: Requires API key for full access
            
            # Mock data structure for demonstration
            # In production, replace with actual API call
            return []
        except Exception as e:
            return []
    
    def _get_mock_events(self, date_str: str) -> List[Dict]:
        """Mock events for demonstration"""
        events = [
            {
                "date": date_str,
                "time": "14:30",
                "country": "US",
                "event": "CPI (Consumer Price Index)",
                "impact": "High",
                "forecast": "0.3%",
                "previous": "0.2%"
            },
            {
                "date": date_str,
                "time": "16:00",
                "country": "US",
                "event": "Fed Interest Rate Decision",
                "impact": "High",
                "forecast": "5.25%",
                "previous": "5.25%"
            }
        ]
        return events
    
    def get_calendar(self, input_str: str) -> str:
        """
        Main method to get economic calendar
        """
        try:
            input_str = input_str.strip().lower()
            
            # Parse date input
            if input_str == "today":
                date = datetime.now()
            elif input_str == "tomorrow":
                date = datetime.now() + timedelta(days=1)
            elif input_str == "this_week":
                # Get events for the week
                today = datetime.now()
                start_date = today - timedelta(days=today.weekday())
                end_date = start_date + timedelta(days=6)
                
                result = f"Calendario Economico - Questa Settimana ({start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}):\n\n"
                
                # For demo, return mock events
                events = self._get_mock_events(today.strftime("%Y-%m-%d"))
                for event in events:
                    result += f"📅 {event['date']} {event['time']} ({event['country']})\n"
                    result += f"   Evento: {event['event']}\n"
                    result += f"   Impatto: {event['impact']}\n"
                    result += f"   Previsione: {event['forecast']}\n"
                    result += f"   Precedente: {event['previous']}\n\n"
                
                return result
            else:
                # Try to parse as date
                try:
                    date = datetime.strptime(input_str, "%Y-%m-%d")
                except:
                    date = datetime.now()
            
            date_str = date.strftime("%Y-%m-%d")
            
            # Get events (mock for now, replace with real API)
            events = self._get_mock_events(date_str)
            
            if not events:
                return f"Nessun evento economico trovato per {date_str}"
            
            result = f"Calendario Economico - {date_str}:\n\n"
            for event in events:
                result += f"📅 {event['time']} ({event['country']})\n"
                result += f"   Evento: {event['event']}\n"
                result += f"   Impatto: {event['impact']}\n"
                result += f"   Previsione: {event['forecast']}\n"
                result += f"   Precedente: {event['previous']}\n\n"
            
            return result
        except Exception as e:
            return f"Errore nel recuperare calendario economico: {str(e)}"
    
    def get_tool(self) -> Tool:
        """Return LangChain Tool instance"""
        return Tool(
            name=self.name,
            description=self.description,
            func=self.get_calendar
        )

