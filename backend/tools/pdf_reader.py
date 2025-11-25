"""
PDF Reader Tool for LangChain
Supports web URLs and local file uploads
"""
import os
import httpx
from typing import Optional
from langchain.tools import Tool
try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader
from io import BytesIO
import pdfplumber

class PDFReaderTool:
    """
    Tool for reading and extracting text from PDF files
    """
    
    def __init__(self):
        self.name = "pdf_reader"
        self.description = """Usa questo tool per leggere e analizzare PDF.
        
Input: URL del PDF o path del file locale
Output: Testo estratto dal PDF
        
Esempio: pdf_reader("https://example.com/report.pdf")
"""
    
    def _read_pdf_from_url(self, url: str) -> str:
        """Download and read PDF from URL"""
        try:
            response = httpx.get(url, timeout=30.0)
            response.raise_for_status()
            pdf_bytes = BytesIO(response.content)
            
            # Try pdfplumber first (better for complex layouts)
            try:
                with pdfplumber.open(pdf_bytes) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text() or ""
                    return text
            except:
                # Fallback to pypdf
                reader = PdfReader(pdf_bytes)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"Errore nel leggere PDF da URL: {str(e)}"
    
    def _read_pdf_from_file(self, file_path: str) -> str:
        """Read PDF from local file"""
        try:
            if not os.path.exists(file_path):
                return f"File non trovato: {file_path}"
            
            # Try pdfplumber first
            try:
                with pdfplumber.open(file_path) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text() or ""
                    return text
            except:
                # Fallback to pypdf
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"Errore nel leggere PDF locale: {str(e)}"
    
    def read_pdf(self, input_str: str) -> str:
        """
        Main method to read PDF
        Supports both URLs and local file paths
        """
        input_str = input_str.strip()
        
        # Check if it's a URL
        if input_str.startswith("http://") or input_str.startswith("https://"):
            return self._read_pdf_from_url(input_str)
        else:
            # Assume it's a local file path
            return self._read_pdf_from_file(input_str)
    
    def get_tool(self) -> Tool:
        """Return LangChain Tool instance"""
        return Tool(
            name=self.name,
            description=self.description,
            func=self.read_pdf
        )

