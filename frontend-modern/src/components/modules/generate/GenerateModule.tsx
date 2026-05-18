'use client';

import React, { useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { createJobLog } from '../../../lib/logging';
import { startGeneration } from '../../../services/jobAdapter';
import { estimateGenerateCost, formatEstimate } from '../../../lib/costEstimate';
import {
  RiPlayListAddLine,
  RiMoneyDollarCircleLine,
  RiTimeLine,
  RiCheckDoubleFill,
  RiStopCircleLine,
  RiAlertLine,
} from '@remixicon/react';
import { Button } from '../../ui';

// Progress-bar chunk geometry (matches preview/progress.html).
const CHUNK_WIDTH = 14;
const CHUNK_GAP = 2;

// §P2 cost budget threshold — fraction of config.budgetLimit at which
// the Session Stats "Current Cost" switches to warning style. At 1.0
// (or above) the warning adds a pulse animation.
const COST_WARN_THRESHOLD = 0.8;

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
    addTcRowAfter,
  } = useJobStore();
  const { advanceWindow } = useWindowStore();
  const runnerRef = useRef<{ stop: () => void } | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);
  // SSE 中斷時保留待處理 row id 給 Resume 用；空陣列代表沒有可恢復的中斷。
  const [pendingResumeIds, setPendingResumeIds] = useState<string[]>([]);
  const isDisconnected = pendingResumeIds.length > 0;

  const progress = useMemo(() => {
    if (!stats.total) {
      return 0;
    }
    return Math.round((stats.processed / stats.total) * 100);
  }, [stats.processed, stats.total]);

  // §P2 Cost budget threshold state. `config.budgetLimit` can legitimately
  // be 0 (user cleared the slider); treat it as "no budget cap" and never
  // flag warn/over — showing a red icon with no reference limit is noise.
  const budgetLimit = config.budgetLimit;
  const costRatio = budgetLimit > 0 ? stats.cost / budgetLimit : 0;
  const isCostWarn = budgetLimit > 0 && costRatio >= COST_WARN_THRESHOLD;
  const isCostOverBudget = budgetLimit > 0 && costRatio >= 1;

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

  const runGeneration = (rowsToRun: typeof tcRows, isResume: boolean) => {
    if (!rowsToRun.length) return;

    setProcessing(true);
    setPendingResumeIds([]);
    if (!isResume) {
      setElapsedSeconds(0);
    }
    // Progress denominator = 原始 Requirement ID 數，不是 row 數，避免 AI 拆分後
    // tcRows 變多讓進度條倒退（jobAdapter 那邊也會以同樣的 reqId set 為基準）。
    // Resume 時只計入這批待跑的 reqId，所以分母會降到剩餘量，符合「續跑」語意。
    const initialReqCount = new Set(
      rowsToRun.map((r) => r.reqId).filter(Boolean),
    ).size || rowsToRun.length;
    updateStats({
      total: initialReqCount,
      processed: 0,
      success: 0,
      fail: 0,
      // cost / token 為累積值，不在新 job 起始時歸零。
    });
    rowsToRun.forEach((row) => updateTcRow(row.id, { status: 'generating' }));
    appendLog(
      createJobLog(
        'info',
        isResume
          ? `Resuming ${rowsToRun.length} pending row(s) after disconnect.`
          : `Queued ${rowsToRun.length} row(s) for generation.`,
      ),
    );

    runnerRef.current = startGeneration(
      {
        jobId: jobMetadata?.jobId ?? null,
        rows: rowsToRun,
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
        onRowAdded: (row, parentId, message) => {
          // AI 把同一 req 拆成多筆 TC 時的第 2..N 筆：插在 parent 後面。
          addTcRowAfter(parentId, row);
          appendLog(createJobLog('info', message));
        },
        onReqSplit: (info) => {
          // 每筆 TC 的 row event 自帶 splitDecision，這裡只負責在 log panel 凸顯拆分事件。
          // 若 AI 拆 >1 筆用 success 等級讓使用者看到進展，1 筆則 info。
          appendLog(createJobLog(
            info.tcCount > 1 ? 'success' : 'info',
            info.message || `${info.reqId}: AI split into ${info.tcCount} TC(s).`,
          ));
        },
        onComplete: (message) => {
          setProcessing(false);
          setPendingResumeIds([]);
          appendLog(createJobLog('success', message));
          advanceWindow('generate', 'review', 'TC Generator - Review Results');
        },
        onError: (message) => {
          setProcessing(false);
          // 偵測「斷線」訊號 → 進入可恢復狀態，不要把 row 視為失敗。
          // jobAdapter 在 source.onerror 固定回 "Live backend stream disconnected."
          if (message.toLowerCase().includes('disconnect')) {
            const stillPending = useJobStore
              .getState()
              .tcRows.filter((row) => row.status === 'generating')
              .map((row) => row.id);
            if (stillPending.length > 0) {
              setPendingResumeIds(stillPending);
              appendLog(
                createJobLog(
                  'warn',
                  `${message} ${stillPending.length} row(s) pending — click Resume to continue.`,
                ),
              );
              return;
            }
          }
          appendLog(createJobLog('warn', message));
        },
      },
    );
  };

  const startRun = () => {
    if (!tcRows.length || isProcessing) {
      return;
    }
    runGeneration(tcRows, false);
  };

  const handleResume = () => {
    if (!isDisconnected || isProcessing) return;
    const pendingSet = new Set(pendingResumeIds);
    const pendingRows = tcRows.filter((row) => pendingSet.has(row.id));
    if (!pendingRows.length) {
      // Pending row 已被刪除 / 完成 — 直接清掉狀態。
      setPendingResumeIds([]);
      return;
    }
    runGeneration(pendingRows, true);
  };

  const discardResume = () => {
    if (!isDisconnected) return;
    const pendingSet = new Set(pendingResumeIds);
    pendingSet.forEach((id) => updateTcRow(id, { status: 'fail' }));
    setPendingResumeIds([]);
    appendLog(
      createJobLog(
        'warn',
        `Discarded ${pendingSet.size} pending row(s); marked as failed.`,
      ),
    );
  };

  const stopRun = () => {
    runnerRef.current?.stop();
    runnerRef.current = null;
    setProcessing(false);
    setPendingResumeIds([]);
    appendLog(createJobLog('warn', 'Generation stopped by operator.'));
  };

  return (
    <div className="modern-workflow-page modern-generate-page flex flex-col h-full gap-4">
      <fieldset className="p-4 border-sunken">
        <legend className="px-2">Progress</legend>
        <div className="flex flex-col gap-2">
          <div className="flex justify-between text-xs mb-1">
            <span>Processing {stats.processed} / {stats.total || tcRows.length} requirements</span>
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

      <div className="modern-generate-layout flex-1 flex gap-4 min-h-0">
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

        <div className="modern-generate-stats w-48 flex flex-col gap-4">
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
                <span className="type-h1 font-mono">{stats.processed}</span>
              </div>
              <div className="stat-sunken">
                <span
                  className="text-xs flex items-center gap-1"
                  style={{ color: 'var(--text-muted)' }}
                >
                  <RiMoneyDollarCircleLine className="size-3" /> Current Cost
                </span>
                <span
                  className="type-h1 font-mono flex items-center gap-1"
                  style={
                    isCostWarn
                      ? {
                          color: 'var(--status-reject-dark)',
                          ...(isCostOverBudget
                            ? { animation: 'agent-pulse 1s ease-in-out infinite' }
                            : {}),
                        }
                      : undefined
                  }
                  title={
                    isCostOverBudget
                      ? `Over budget: $${stats.cost.toFixed(4)} / $${budgetLimit.toFixed(2)}`
                      : isCostWarn
                        ? `${Math.round(costRatio * 100)}% of budget used ($${stats.cost.toFixed(4)} / $${budgetLimit.toFixed(2)})`
                        : undefined
                  }
                >
                  {isCostWarn && <RiAlertLine className="size-4" />}
                  ${stats.cost.toFixed(4)}
                </span>
              </div>
              <div className="stat-sunken">
                <span
                  className="text-xs flex items-center gap-1"
                  style={{ color: 'var(--text-muted)' }}
                >
                  <RiTimeLine className="size-3" /> Elapsed
                </span>
                <span className="type-h1 font-mono">
                  {String(Math.floor(elapsedSeconds / 60)).padStart(2, '0')}:{String(elapsedSeconds % 60).padStart(2, '0')}
                </span>
              </div>
            </div>
          </fieldset>
        </div>
      </div>

      {isDisconnected && (
        <div
          className="paper-card p-2 text-xs flex items-center gap-2"
          style={{
            background: 'var(--status-warn-bg-soft, #fff8e1)',
            border: '1px solid var(--status-warn-border, #e6a23c)',
            color: 'var(--status-warn-dark, #7a5200)',
          }}
        >
          <RiAlertLine className="size-4 shrink-0" />
          <span className="flex-1">
            <strong>連線中斷。</strong>
            {' '}{pendingResumeIds.length} 筆 row 尚未處理 — 按 Resume 重連續跑這批，或 Discard 將其標為 fail。
          </span>
          <Button
            className="flex items-center gap-1 default"
            onClick={handleResume}
            disabled={isProcessing}
          >
            <RiPlayListAddLine className="size-3" /> Resume
          </Button>
          <Button onClick={discardResume} disabled={isProcessing}>
            Discard
          </Button>
        </div>
      )}

      <div className="modern-workflow-bottom-bar flex justify-between items-center pt-2">
        <Button className="flex items-center gap-1" disabled={!isProcessing} onClick={stopRun}>
          <RiStopCircleLine className="size-4" /> Cancel
        </Button>
        <div className="flex items-center gap-2">
          {!isProcessing && tcRows.length > 0 && (() => {
            const reqCount = new Set(tcRows.map((r) => r.reqId).filter(Boolean)).size || tcRows.length;
            const estimate = estimateGenerateCost(reqCount, config.model);
            return (
              <span
                className="text-xs"
                style={{ color: 'var(--text-muted)' }}
                title={`Rough estimate using ~${1500} input + ~${800 * 2.5} output tokens per requirement on ${config.model}. Actual cost may vary ±30%.`}
              >
                Est. ~{formatEstimate(estimate)} for {reqCount} req(s)
              </span>
            );
          })()}
          <Button
            className="flex items-center gap-1 default"
            disabled={isProcessing || isDisconnected || !tcRows.length}
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
            onClick={() => advanceWindow('generate', 'review', 'TC Generator - Review Results')}
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
