'use client';

import React, { useLayoutEffect, useMemo, useRef, useState } from 'react';
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
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import { Button } from '../../ui';

// Progress-bar chunk geometry (matches preview/progress.html).
const CHUNK_WIDTH = 14;
const CHUNK_GAP = 2;

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

  // 動態依 bar 可用寬度計算 chunk 數量（preview/progress.html 的行為）
  const progressBarRef = useRef<HTMLDivElement>(null);
  const [totalChunks, setTotalChunks] = useState(1);
  useLayoutEffect(() => {
    const el = progressBarRef.current;
    if (!el) return;
    const recalc = () => {
      // 扣掉 2px border (×2) + 2px padding (×2) = 8px = clientWidth already excludes
      // border, so only subtract padding (4px total).
      const inner = el.clientWidth - 4;
      // 公式：Math.floor((innerWidth + gap) / (chunkWidth + gap))
      const count = Math.max(1, Math.floor((inner + CHUNK_GAP) / (CHUNK_WIDTH + CHUNK_GAP)));
      setTotalChunks(count);
    };
    recalc();
    const ro = new ResizeObserver(recalc);
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const solidCount = Math.floor((progress / 100) * totalChunks);
  const hasPartial =
    progress > 0 && progress < 100 && (progress / 100) * totalChunks > solidCount;

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

  const buildContext = () => {
    const jobId = jobMetadata?.jobId ?? '未開啟 job';
    return `[context: 目前在 Generate Module, job=${jobId}]\n[進度: ${stats.processed}/${stats.total || tcRows.length} rows, 成本 $${stats.cost.toFixed(4)}]\n`;
  };

  return (
    <div className="flex flex-col h-full gap-4">
      <div className="flex justify-end">
        <HelpFromAgentButton contextPrompt={buildContext()} title="求助 AI" />
      </div>
      <fieldset className="p-4 border-sunken">
        <legend className="px-2">Progress</legend>
        <div className="flex flex-col gap-2">
          <div className="flex justify-between text-xs mb-1">
            <span>Processing {stats.processed} / {stats.total || tcRows.length} TCs</span>
            <span>Elapsed: {String(Math.floor(elapsedSeconds / 60)).padStart(2, '0')}:{String(elapsedSeconds % 60).padStart(2, '0')}</span>
          </div>
          <div className="flex items-center gap-2">
            <div ref={progressBarRef} className="progress-bar-wrap flex-1">
              {Array.from({ length: solidCount }).map((_, i) => (
                <div key={i} className="progress-chunk" />
              ))}
              {hasPartial && <div className="progress-chunk progress-chunk--partial" />}
            </div>
            <span className="progress-label">{progress}%</span>
          </div>
        </div>
      </fieldset>

      <div className="flex-1 flex gap-4 min-h-0">
        <div className="flex-1 flex flex-col gap-1">
          <label className="text-sm font-bold">Generation Log:</label>
          <div className="selectable flex-1 bg-white font-mono text-xs p-2 border-sunken overflow-auto leading-relaxed">
            {logs.map((log, i) => (
              <div key={i} className="flex gap-2">
                <span style={{ color: 'var(--win95-gray-mid)' }}>[{log.timestamp}]</span>
                <span style={{
                  color: log.level === 'error' ? 'var(--status-reject-dark)'
                       : log.level === 'success' ? 'var(--status-accept-dark)'
                       : log.level === 'warn' ? 'var(--status-warn-dark)'
                       : 'var(--win95-black)'
                }}>
                  {log.message}
                </span>
              </div>
            ))}
            {isProcessing && <div style={{ animation: 'agent-pulse 1s ease-in-out infinite' }}>_</div>}
          </div>
        </div>

        <div className="w-48 flex flex-col gap-4">
          <fieldset className="flex-1">
            <legend className="text-sm">Session Stats</legend>
            <div className="flex flex-col gap-2 p-1">
              <div className="stat-sunken">
                <span
                  className="text-xs flex items-center gap-1"
                  style={{ color: 'var(--text-muted)' }}
                >
                  <RiPlayListAddLine className="size-3" /> Processed
                </span>
                <span className="text-lg font-bold font-mono">{stats.processed}</span>
              </div>
              <div className="stat-sunken">
                <span
                  className="text-xs flex items-center gap-1"
                  style={{ color: 'var(--text-muted)' }}
                >
                  <RiMoneyDollarCircleLine className="size-3" /> Current Cost
                </span>
                <span className="text-lg font-bold font-mono">${stats.cost.toFixed(4)}</span>
              </div>
              <div className="stat-sunken">
                <span
                  className="text-xs flex items-center gap-1"
                  style={{ color: 'var(--text-muted)' }}
                >
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
        <Button className="flex items-center gap-1" disabled={!isProcessing} onClick={stopRun}>
          <RiStopCircleLine className="size-4" /> Cancel
        </Button>
        <div className="flex items-center gap-2">
          <Button
            className="flex items-center gap-1 default"
            disabled={isProcessing || !tcRows.length}
            onClick={startRun}
          >
            <RiPlayListAddLine
              className="size-4"
              style={{ color: 'var(--status-accept-dark)' }}
            />{' '}
            Start Run
          </Button>
          <Button
            className="flex items-center gap-1 default"
            disabled={isProcessing || !tcRows.length}
            onClick={() => openWindow('review', 'TC Generator - Review Results')}
          >
            Review Results{' '}
            <RiCheckDoubleFill
              className="size-4"
              style={{ color: 'var(--win95-navy)' }}
            />
          </Button>
        </div>
      </div>
    </div>
  );
};

export default GenerateModule;
