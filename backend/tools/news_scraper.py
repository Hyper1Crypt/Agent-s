"""
News Scraper Tool for financial and crypto news
"""
import httpx
from bs4 import BeautifulSoup
from typing import List, Dict
from langchain.tools import Tool
from datetime import datetime, timedelta

class NewsScraperTool:
    """
    Tool for scraping financial and crypto news
    """
    
    def __init__(self):
        self.name = "news_scraper"
        self.description = """Usa questo tool per raccogliere news finanziarie e crypto.
        
Input: query di ricerca (es. "bitcoin", "macro economy", "fed rate")
Output: Lista di news recenti con titolo, fonte e data
        
Esempio: news_scraper("bitcoin funding rate")
"""
        
        # News sources
        self.sources = {
            "coindesk": "https://www.coindesk.com/search/?s={query}",
            "cointelegraph": "https://cointelegraph.com/search?q={query}",
            "reuters": "https://www.reuters.com/search/news?blob={query}",
        }
    
    def _scrape_coindesk(self, query: str) -> List[Dict]:
        """Scrape CoinDesk news"""
        try:
            url = f"https://www.coindesk.com/search/?s={query}"
            response = httpx.get(url, timeout=10.0, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            soup = BeautifulSoup(response.text, 'html.parser')
            
            news = []
            articles = soup.find_all('article', limit=5)
            for article in articles:
                title_elem = article.find('h3') or article.find('h2')
                link_elem = article.find('a')
                date_elem = article.find('time')
                
                if title_elem:
                    news.append({
                        "title": title_elem.get_text(strip=True),
                        "url": link_elem.get('href', '') if link_elem else '',
                        "date": date_elem.get_text(strip=True) if date_elem else '',
                        "source": "CoinDesk"
                    })
            return news
        except Exception as e:
            return [{"error": f"Errore scraping CoinDesk: {str(e)}"}]
    
    def _get_crypto_news_api(self, query: str) -> List[Dict]:
        """Get news from CryptoCompare API (free tier)"""
        try:
            # Using CryptoCompare free API
            url = "https://min-api.cryptocompare.com/data/v2/news/"
            params = {
                "lang": "EN",
                "categories": "BTC,ETH" if "bitcoin" in query.lower() or "btc" in query.lower() else None
            }
            
            response = httpx.get(url, params=params, timeout=10.0)
            data = response.json()
            
            news = []
            if data.get("Data"):
                for item in data["Data"][:5]:
                    news.append({
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "date": datetime.fromtimestamp(item.get("published_on", 0)).strftime("%Y-%m-%d %H:%M"),
                        "source": item.get("source", "CryptoCompare")
                    })
            return news
        except Exception as e:
            return []
    
    def scrape_news(self, query: str) -> str:
        """
        Main method to scrape news
        """
        try:
            all_news = []
            
            # Try API first (more reliable)
            api_news = self._get_crypto_news_api(query)
            all_news.extend(api_news)
            
            # Try scraping CoinDesk
            coindesk_news = self._scrape_coindesk(query)
            all_news.extend(coindesk_news)
            
            if not all_news:
                return f"Nessuna news trovata per: {query}"
            
            # Format output
            result = f"News trovate per '{query}':\n\n"
            for i, item in enumerate(all_news[:10], 1):  # Limit to 10
                if "error" in item:
                    continue
                result += f"{i}. {item.get('title', 'N/A')}\n"
                result += f"   Fonte: {item.get('source', 'N/A')}\n"
                result += f"   Data: {item.get('date', 'N/A')}\n"
                if item.get('url'):
                    result += f"   URL: {item.get('url')}\n"
                result += "\n"
            
            return result
        except Exception as e:
            return f"Errore nel raccogliere news: {str(e)}"
    
    def get_tool(self) -> Tool:
        """Return LangChain Tool instance"""
        return Tool(
            name=self.name,
            description=self.description,
            func=self.scrape_news
        )

