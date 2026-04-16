'use client';

import React, { useMemo, useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { startGeneration } from '../../../services/jobAdapter';
import {
  RiPlayListAddLine,
  RiMoneyDollarCircleLine,
  RiTimeLine,
  RiCheckDoubleFill,
  RiStopCircleLine
} from '@remixicon/react';

const GenerateModule: React.FC = () => {
  const {
    tcRows,
    logs,
    appendLog,
    stats,
    updateStats,
    isProcessing,
    setProcessing,
    jobMetadata,
    config,
    updateTcRow,
  } = useJobStore();
  const { openWindow } = useWindowStore();
  const runnerRef = useRef<{ stop: () => void } | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);

  const progress = useMemo(() => {
    if (!stats.total) {
      return 0;
    }
    return Math.round((stats.processed / stats.total) * 100);
  }, [stats.processed, stats.total]);

  const startRun = () => {
    if (!tcRows.length || isProcessing) {
      return;
    }

    setProcessing(true);
    setElapsedSeconds(0);
    updateStats({
      total: tcRows.length,
      processed: 0,
      success: 0,
      fail: 0,
      cost: 0,
    });
    tcRows.forEach((row) => updateTcRow(row.id, { status: 'generating' }));
    appendLog(createJobLog('info', `Queued ${tcRows.length} row(s) for generation.`));

    runnerRef.current = startGeneration(
      {
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
        config,
      },
      {
        onProgress: (nextStats) => {
          updateStats(nextStats);
          setElapsedSeconds((current) => current + 1);
        },
        onRow: (row, message) => {
          updateTcRow(row.id, row);
          appendLog(createJobLog('info', message));
        },
        onComplete: (message) => {
          setProcessing(false);
          appendLog(createJobLog('success', message));
          openWindow('review', 'TC Generator - Review Results');
        },
        onError: (message) => {
          setProcessing(false);
          appendLog(createJobLog('warn', message));
        },
      },
    );
  };

  const stopRun = () => {
    runnerRef.current?.stop();
    runnerRef.current = null;
    setProcessing(false);
    appendLog(createJobLog('warn', 'Generation stopped by operator.'));
  };

  return (
    <div className="flex flex-col h-full gap-4">
      <fieldset className="p-4 border-2 border-sunken">
        <legend className="px-2 font-bold">Progress: {progress}%</legend>
        <div className="flex flex-col gap-2">
          <div className="flex justify-between text-xs font-sans mb-1">
            <span>Processing {stats.processed} / {stats.total || tcRows.length} TCs</span>
            <span>Elapsed: {String(Math.floor(elapsedSeconds / 60)).padStart(2, '0')}:{String(elapsedSeconds % 60).padStart(2, '0')}</span>
          </div>
          <div className="h-6 border-2 border-sunken bg-gray-200 p-0.5 flex gap-0.5 overflow-hidden">
            {Array.from({ length: Math.floor(progress / 2.5) }).map((_, i) => (
              <div key={i} className="w-2 h-full bg-blue-900 shadow-[inset_-1px_-1px_0_rgba(0,0,0,0.5)]" />
            ))}
          </div>
        </div>
      </fieldset>

      <div className="flex-1 flex gap-4 min-h-0">
        <div className="flex-1 flex flex-col gap-1">
          <label className="text-sm font-bold">Generation Log:</label>
          <div className="flex-1 bg-black text-green-500 font-mono text-xs p-2 border-2 border-sunken overflow-auto leading-relaxed">
            {logs.map((log, i) => (
              <div key={i} className="flex gap-2">
                <span className="text-gray-500">[{log.timestamp}]</span>
                <span className={log.level === 'error' ? 'text-red-500' : log.level === 'success' ? 'text-blue-400' : ''}>
                  {log.message}
                </span>
              </div>
            ))}
            {isProcessing && <div className="animate-pulse">_</div>}
          </div>
        </div>

        <div className="w-48 flex flex-col gap-4">
          <fieldset className="flex-1">
            <legend className="text-sm font-bold">Session Stats</legend>
            <div className="flex flex-col gap-4 p-1">
              <div className="flex flex-col gap-1">
                <span className="text-xs text-gray-600 flex items-center gap-1">
                  <RiPlayListAddLine className="size-3" /> Processed
                </span>
                <span className="text-lg font-bold font-mono">{stats.processed}</span>
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-xs text-gray-600 flex items-center gap-1">
                  <RiMoneyDollarCircleLine className="size-3" /> Current Cost
                </span>
                <span className="text-lg font-bold font-mono text-red-700">${stats.cost.toFixed(4)}</span>
              </div>
              <div className="flex flex-col gap-1">
                <span className="text-xs text-gray-600 flex items-center gap-1">
                  <RiTimeLine className="size-3" /> Elapsed
                </span>
                <span className="text-lg font-bold font-mono">
                  {String(Math.floor(elapsedSeconds / 60)).padStart(2, '0')}:{String(elapsedSeconds % 60).padStart(2, '0')}
                </span>
              </div>
            </div>
          </fieldset>
        </div>
      </div>

      <div className="flex justify-between items-center pt-2">
        <button className="flex items-center gap-1" disabled={!isProcessing} onClick={stopRun}>
          <RiStopCircleLine className="size-4" /> Cancel
        </button>
        <div className="flex items-center gap-2">
          <button
            className="flex items-center gap-1 font-bold"
            disabled={isProcessing || !tcRows.length}
            onClick={startRun}
          >
            <RiPlayListAddLine className="size-4 text-green-700" /> Start Run
          </button>
          <button
            className="flex items-center gap-1 font-bold"
            disabled={isProcessing || !tcRows.length}
            onClick={() => openWindow('review', 'TC Generator - Review Results')}
          >
            Review Results <RiCheckDoubleFill className="size-4 text-blue-700" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default GenerateModule;
