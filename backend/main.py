"""
Main FastAPI application for Lab Trading AI Financial Analyst
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent.financial_agent import FinancialAgent

load_dotenv()

app = FastAPI(
    title="Lab Trading API",
    description="AI Financial Analyst API for Crypto and Macro Analysis",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent
agent = FinancialAgent()

class AnalysisRequest(BaseModel):
    query: str
    context: Optional[dict] = None

class AnalysisResponse(BaseModel):
    report: str
    sources: Optional[list] = None
    timestamp: Optional[str] = None

@app.get("/")
async def root():
    return {
        "message": "Lab Trading API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    """
    Main endpoint for financial analysis queries
    """
    try:
        result = await agent.analyze(request.query, request.context)
        return AnalysisResponse(
            report=result.get("report", ""),
            sources=result.get("sources", []),
            timestamp=result.get("timestamp")
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during analysis: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

