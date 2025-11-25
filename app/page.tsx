'use client'

import { useState } from 'react'
import { Send, Loader2, TrendingUp, FileText, BarChart3 } from 'lucide-react'
import ChatInterface from '@/components/ChatInterface'
import ReportDisplay from '@/components/ReportDisplay'

export default function Home() {
  const [report, setReport] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const handleAnalysisComplete = (analysisReport: string) => {
    setReport(analysisReport)
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <TrendingUp className="w-10 h-10 text-primary-400" />
            <h1 className="text-5xl font-bold text-white">
              Lab Trading
            </h1>
          </div>
          <p className="text-xl text-slate-300 max-w-2xl mx-auto">
            Assistente personalizzato di analisi finanziaria per crypto e macroeconomia
          </p>
          <div className="flex items-center justify-center gap-6 mt-6">
            <div className="flex items-center gap-2 text-slate-400">
              <FileText className="w-5 h-5" />
              <span>Analisi PDF</span>
            </div>
            <div className="flex items-center gap-2 text-slate-400">
              <BarChart3 className="w-5 h-5" />
              <span>Dati Crypto</span>
            </div>
            <div className="flex items-center gap-2 text-slate-400">
              <TrendingUp className="w-5 h-5" />
              <span>Report Operativi</span>
            </div>
          </div>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto">
          {/* Chat Interface */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl shadow-2xl border border-slate-700/50 p-6">
            <h2 className="text-2xl font-semibold text-white mb-4">
              Fai una domanda
            </h2>
            <ChatInterface 
              onAnalysisComplete={handleAnalysisComplete}
              isLoading={isLoading}
              setIsLoading={setIsLoading}
            />
          </div>

          {/* Report Display */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl shadow-2xl border border-slate-700/50 p-6">
            <h2 className="text-2xl font-semibold text-white mb-4">
              Report Analisi
            </h2>
            <ReportDisplay report={report} />
          </div>
        </div>
      </div>
    </main>
  )
}

