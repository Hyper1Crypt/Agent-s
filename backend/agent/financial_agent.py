"""
Financial Agent using LangChain for multi-source analysis
"""
import os
from datetime import datetime
from typing import Dict, List, Optional
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from langchain_core.messages import HumanMessage, AIMessage

from tools.pdf_reader import PDFReaderTool
from tools.news_scraper import NewsScraperTool
from tools.crypto_data import CryptoDataTool
from tools.economic_calendar import EconomicCalendarTool
from tools.database import DatabaseTool

class FinancialAgent:
    """
    Main financial analysis agent that orchestrates multiple tools
    """
    
    def __init__(self):
        # Support multiple LLM providers
        llm_provider = os.getenv("LLM_PROVIDER", "openai").lower()
        
        if llm_provider == "gemini":
            # Google Gemini (FREE tier available)
            from langchain_google_genai import ChatGoogleGenerativeAI
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY non trovata. Ottienila da: https://makersuite.google.com/app/apikey")
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                temperature=0.3,
                google_api_key=api_key
            )
        elif llm_provider == "groq":
            # Groq (FREE tier, very fast)
            from langchain_groq import ChatGroq
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY non trovata. Ottienila da: https://console.groq.com/keys")
            self.llm = ChatGroq(
                model="llama-3.1-70b-versatile",  # or "mixtral-8x7b-32768"
                temperature=0.3,
                groq_api_key=api_key
            )
        else:
            # Default: OpenAI
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY non trovata nelle variabili ambiente")
            self.llm = ChatOpenAI(
                model="gpt-3.5-turbo",  # More affordable than gpt-4-turbo
                temperature=0.3,
                api_key=api_key
            )
        
        # Initialize tools
        self.tools = [
            PDFReaderTool().get_tool(),
            NewsScraperTool().get_tool(),
            CryptoDataTool().get_tool(),
            EconomicCalendarTool().get_tool(),
            DatabaseTool().get_tool(),
        ]
        
        # Create agent prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """Sei un assistente finanziario esperto specializzato in analisi crypto e macroeconomica.
            
Il tuo compito è:
1. Raccogliere informazioni da fonti multiple (PDF, news, dati crypto, calendario economico)
2. Analizzare i dati in profondità
3. Generare report operativi chiari e completi

Struttura del report:
- Contesto macroeconomico
- Dati di mercato rilevanti
- Funding e Open Interest (se applicabile)
- News e eventi critici
- Analisi del sentiment
- Rischi e opportunità
- Conclusione operativa (azione consigliata + motivazione)

Sii preciso, obiettivo e basati sempre sui dati raccolti."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        # Create agent (using create_tool_calling_agent for LangChain 0.1.0+)
        try:
            self.agent = create_tool_calling_agent(
                llm=self.llm,
                tools=self.tools,
                prompt=self.prompt
            )
            self.agent_executor = AgentExecutor(
                agent=self.agent,
                tools=self.tools,
                verbose=True,
                max_iterations=15,
                handle_parsing_errors=True
            )
        except Exception as e:
            # Fallback for older LangChain versions
            try:
                from langchain.agents import initialize_agent, AgentType
                self.agent_executor = initialize_agent(
                    tools=self.tools,
                    llm=self.llm,
                    agent=AgentType.OPENAI_FUNCTIONS,
                    verbose=True,
                    max_iterations=15,
                    handle_parsing_errors=True
                )
            except Exception as e2:
                # Last resort: use simple LLM with tools
                print(f"Warning: Could not create agent, using fallback. Error: {e2}")
                self.agent_executor = None
    
    async def analyze(self, query: str, context: Optional[Dict] = None) -> Dict:
        """
        Main analysis method
        """
        try:
            if self.agent_executor is None:
                return {
                    "report": "Errore: Agent non inizializzato correttamente. Verifica le dipendenze LangChain.",
                    "sources": [],
                    "timestamp": datetime.now().isoformat()
                }
            
            # Execute agent
            if hasattr(self.agent_executor, 'ainvoke'):
                result = await self.agent_executor.ainvoke({
                    "input": query,
                    "chat_history": []
                })
            elif hasattr(self.agent_executor, 'run'):
                # Fallback for sync execution
                result = self.agent_executor.run(query)
                result = {"output": result}
            else:
                return {
                    "report": "Errore: Metodo di esecuzione agent non trovato.",
                    "sources": [],
                    "timestamp": datetime.now().isoformat()
                }
            
            report = result.get("output", "Analisi completata.")
            
            return {
                "report": report,
                "sources": result.get("sources", []),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            return {
                "report": f"Errore durante l'analisi: {str(e)}\n\nDettagli: {error_details}",
                "sources": [],
                "timestamp": datetime.now().isoformat()
            }

