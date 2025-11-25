'use client'

import { FileText } from 'lucide-react'

interface ReportDisplayProps {
  report: string | null
}

export default function ReportDisplay({ report }: ReportDisplayProps) {
  if (!report) {
    return (
      <div className="flex flex-col items-center justify-center h-full min-h-[400px] text-slate-400">
        <FileText className="w-16 h-16 mb-4 opacity-50" />
        <p>Il report di analisi apparirà qui</p>
      </div>
    )
  }

  return (
    <div className="h-full min-h-[400px] max-h-[600px] overflow-y-auto">
      <div className="prose prose-invert max-w-none">
        <div className="bg-slate-900/50 rounded-lg p-6 text-slate-100 whitespace-pre-wrap">
          {report}
        </div>
      </div>
    </div>
  )
}

