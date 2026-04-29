"use client";

import {
  RiAlertLine,
  RiCheckDoubleFill,
  RiMoneyDollarCircleLine,
  RiPlayListAddLine,
  RiStopCircleLine,
  RiTimeLine,
} from "@remixicon/react";
import { useEffect, useMemo, useRef, useState } from "react";
import { estimateGenerateCost, formatEstimate } from "../../../lib/costEstimate";
import { createJobLog } from "../../../lib/logging";
import { startGeneration } from "../../../services/jobAdapter";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../store/useJobStore";

const COST_WARN_THRESHOLD = 0.8;

export default function ExecuteStep({ onAdvance }: { onAdvance: () => void }) {
  const tcRows = useJobStore((s) => s.tcRows);
  const logs = useJobStore((s) => s.logs);
  const stats = useJobStore((s) => s.stats);
  const isProcessing = useJobStore((s) => s.isProcessing);
  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const config = useJobStore((s) => s.config);
  const appendLog = useJobStore((s) => s.appendLog);
  const updateStats = useJobStore((s) => s.updateStats);
  const setProcessing = useJobStore((s) => s.setProcessing);
  const updateTcRow = useJobStore((s) => s.updateTcRow);
  const addTcRowAfter = useJobStore((s) => s.addTcRowAfter);

  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  const runnerRef = useRef<{ stop: () => void } | null>(null);
  const startedAtRef = useRef<number | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);
  const [pendingResumeIds, setPendingResumeIds] = useState<string[]>([]);
  const isDisconnected = pendingResumeIds.length > 0;

  // 使用真實時間驅動 elapsed，不依賴 onProgress 計數（這比 legacy 行為更正確）
  useEffect(() => {
    if (!isProcessing || !startedAtRef.current) return;
    const id = setInterval(() => {
      const start = startedAtRef.current;
      if (!start) return;
      setElapsedSeconds(Math.floor((Date.now() - start) / 1000));
    }, 1000);
    return () => clearInterval(id);
  }, [isProcessing]);

  const progress = useMemo(() => {
    if (!stats.total) return 0;
    return Math.round((stats.processed / stats.total) * 100);
  }, [stats.processed, stats.total]);

  const budgetLimit = config.budgetLimit;
  const costRatio = budgetLimit > 0 ? stats.cost / budgetLimit : 0;
  const isCostWarn = budgetLimit > 0 && costRatio >= COST_WARN_THRESHOLD;
  const isCostOverBudget = budgetLimit > 0 && costRatio >= 1;

  const reqCount = useMemo(() => {
    return (
      new Set(tcRows.map((r) => r.reqId).filter(Boolean)).size ||
      tcRows.length
    );
  }, [tcRows]);

  const estimate = useMemo(
    () => estimateGenerateCost(reqCount, config.model),
    [reqCount, config.model]
  );

  const runGeneration = (
    rowsToRun: typeof tcRows,
    isResume: boolean
  ) => {
    if (!rowsToRun.length) return;

    setProcessing(true);
    setPendingResumeIds([]);
    if (!isResume) {
      startedAtRef.current = Date.now();
      setElapsedSeconds(0);
    }
    const initialReqCount =
      new Set(rowsToRun.map((r) => r.reqId).filter(Boolean)).size ||
      rowsToRun.length;
    updateStats({
      total: initialReqCount,
      processed: 0,
      success: 0,
      fail: 0,
    });
    rowsToRun.forEach((row) => updateTcRow(row.id, { status: "generating" }));
    appendLog(
      createJobLog(
        "info",
        isResume
          ? `Resuming ${rowsToRun.length} pending row(s) after disconnect.`
          : `Queued ${rowsToRun.length} row(s) for generation.`
      )
    );

    runnerRef.current = startGeneration(
      {
        jobId: jobMetadata?.jobId ?? null,
        rows: rowsToRun,
        config,
      },
      {
        onProgress: (next) => updateStats(next),
        onRow: (row, message) => {
          updateTcRow(row.id, row);
          appendLog(createJobLog("info", message));
        },
        onRowAdded: (row, parentId, message) => {
          addTcRowAfter(parentId, row);
          appendLog(createJobLog("info", message));
        },
        onReqSplit: (info) => {
          appendLog(
            createJobLog(
              info.tcCount > 1 ? "success" : "info",
              info.message ||
                `${info.reqId}: AI split into ${info.tcCount} TC(s).`
            )
          );
        },
        onComplete: (message) => {
          setProcessing(false);
          setPendingResumeIds([]);
          appendLog(createJobLog("success", message));
          markStepComplete("execute", true);
          onAdvance();
        },
        onError: (message) => {
          setProcessing(false);
          if (message.toLowerCase().includes("disconnect")) {
            const stillPending = useJobStore
              .getState()
              .tcRows.filter((row) => row.status === "generating")
              .map((row) => row.id);
            if (stillPending.length > 0) {
              setPendingResumeIds(stillPending);
              appendLog(
                createJobLog(
                  "warn",
                  `${message} ${stillPending.length} row(s) pending — click Resume to continue.`
                )
              );
              return;
            }
          }
          appendLog(createJobLog("warn", message));
        },
      }
    );
  };

  const startRun = () => {
    if (!tcRows.length || isProcessing) return;
    runGeneration(tcRows, false);
  };

  const handleResume = () => {
    if (!isDisconnected || isProcessing) return;
    const pendingSet = new Set(pendingResumeIds);
    const pendingRows = tcRows.filter((row) => pendingSet.has(row.id));
    if (!pendingRows.length) {
      setPendingResumeIds([]);
      return;
    }
    runGeneration(pendingRows, true);
  };

  const discardResume = () => {
    if (!isDisconnected) return;
    const pendingSet = new Set(pendingResumeIds);
    pendingSet.forEach((id) => updateTcRow(id, { status: "fail" }));
    setPendingResumeIds([]);
    appendLog(
      createJobLog(
        "warn",
        `Discarded ${pendingSet.size} pending row(s); marked as failed.`
      )
    );
  };

  const stopRun = () => {
    runnerRef.current?.stop();
    runnerRef.current = null;
    setProcessing(false);
    setPendingResumeIds([]);
    appendLog(createJobLog("warn", "Generation stopped by operator."));
  };

  const elapsedLabel = `${String(Math.floor(elapsedSeconds / 60)).padStart(
    2,
    "0"
  )}:${String(elapsedSeconds % 60).padStart(2, "0")}`;

  if (!tcRows.length) {
    return (
      <div className="surface p-8 text-center space-y-2">
        <p className="text-sm text-secondary">
          No rows loaded. Go back to <strong>Select Data</strong> and parse a
          workbook first.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <section className="surface p-5 space-y-3">
        <div className="flex items-end justify-between gap-3 flex-wrap">
          <div>
            <div className="text-xs uppercase tracking-wider text-secondary">
              Progress
            </div>
            <div className="text-2xl font-bold text-primary">
              {stats.processed} / {stats.total || tcRows.length}
              <span className="text-base font-normal text-secondary ml-2">
                requirements
              </span>
            </div>
          </div>
          <div className="text-3xl font-bold" style={{ color: "var(--color-tangerine)" }}>
            {progress}%
          </div>
        </div>

        <div
          className="h-2 rounded-full overflow-hidden"
          style={{ backgroundColor: "rgba(21, 97, 109, 0.15)" }}
        >
          <div
            className="h-full transition-all duration-300"
            style={{
              width: `${progress}%`,
              backgroundColor: "var(--color-tangerine)",
            }}
          />
        </div>
      </section>

      <section className="grid grid-cols-3 gap-4">
        <Stat
          icon={<RiPlayListAddLine size={16} />}
          label="Processed"
          value={String(stats.processed)}
        />
        <Stat
          icon={<RiMoneyDollarCircleLine size={16} />}
          label="Current Cost"
          value={`$${stats.cost.toFixed(4)}`}
          accent={
            isCostOverBudget
              ? "var(--color-brandy)"
              : isCostWarn
              ? "var(--color-tangerine)"
              : undefined
          }
          hint={
            budgetLimit > 0
              ? `${Math.round(costRatio * 100)}% of $${budgetLimit.toFixed(2)} budget`
              : undefined
          }
        />
        <Stat
          icon={<RiTimeLine size={16} />}
          label="Elapsed"
          value={elapsedLabel}
        />
      </section>

      <section className="surface p-4 space-y-2">
        <div className="flex items-center justify-between">
          <h3 className="text-xs uppercase tracking-wider text-secondary">
            Generation Log
          </h3>
          <span className="text-xs text-muted">{logs.length} entries</span>
        </div>
        <div
          className="font-mono text-xs leading-relaxed overflow-auto p-3 rounded-md max-h-[280px]"
          style={{
            backgroundColor: "rgba(0, 21, 36, 0.04)",
            boxShadow: "inset 0 1px 2px rgba(0, 21, 36, 0.08)",
          }}
        >
          {logs.length === 0 ? (
            <span className="text-muted">No entries yet.</span>
          ) : (
            logs.map((log, i) => (
              <div key={i} className="flex gap-2">
                <span className="text-muted shrink-0">[{log.timestamp}]</span>
                <span style={{ color: levelColor(log.level) }}>
                  {log.message}
                </span>
              </div>
            ))
          )}
          {isProcessing && (
            <span
              className="inline-block"
              style={{ animation: "agent-pulse 1s ease-in-out infinite" }}
            >
              _
            </span>
          )}
        </div>
      </section>

      {isDisconnected && (
        <section
          className="surface p-3 flex items-center gap-3 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          <RiAlertLine size={18} />
          <span className="flex-1">
            <strong>Disconnected.</strong> {pendingResumeIds.length} row(s)
            pending — Resume to continue or Discard to mark as failed.
          </span>
          <button
            type="button"
            onClick={handleResume}
            disabled={isProcessing}
            className="cta inline-flex items-center gap-1.5 text-xs px-3 py-1.5"
          >
            <RiPlayListAddLine size={14} /> Resume
          </button>
          <button
            type="button"
            onClick={discardResume}
            disabled={isProcessing}
            className="text-xs px-3 py-1.5 rounded-md focus-ring"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            Discard
          </button>
        </section>
      )}

      <div className="flex items-center justify-between gap-3 flex-wrap">
        <button
          type="button"
          onClick={stopRun}
          disabled={!isProcessing}
          className="inline-flex items-center gap-1.5 px-4 py-2 rounded-md text-sm font-bold focus-ring transition-all disabled:opacity-40"
          style={{
            backgroundColor: "rgba(120, 41, 15, 0.1)",
            color: "var(--color-brandy)",
          }}
        >
          <RiStopCircleLine size={16} /> Cancel
        </button>

        <div className="flex items-center gap-3 flex-wrap">
          {!isProcessing && (
            <span
              className="text-xs text-muted"
              title={`Rough estimate on ${config.model}. Actual cost may vary ±30%.`}
            >
              Est. ~{formatEstimate(estimate)} for {reqCount} req(s)
            </span>
          )}
          <button
            type="button"
            onClick={startRun}
            disabled={isProcessing || isDisconnected || !tcRows.length}
            className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <RiPlayListAddLine size={16} /> Start Run
          </button>
          <button
            type="button"
            onClick={() => {
              markStepComplete("execute", true);
              onAdvance();
            }}
            disabled={isProcessing || !tcRows.length}
            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-md text-sm font-bold focus-ring transition-all disabled:opacity-40"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            Review Results <RiCheckDoubleFill size={16} />
          </button>
        </div>
      </div>
    </div>
  );
}

function levelColor(level: string): string {
  switch (level) {
    case "error":
      return "var(--color-brandy)";
    case "success":
      return "var(--color-teal)";
    case "warn":
      return "var(--color-tangerine)";
    default:
      return "var(--color-ink)";
  }
}

function Stat({
  icon,
  label,
  value,
  hint,
  accent,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  hint?: string;
  accent?: string;
}) {
  return (
    <div className="surface p-4 space-y-1">
      <div className="text-xs flex items-center gap-1.5 text-secondary uppercase tracking-wider">
        {icon}
        {label}
      </div>
      <div
        className="text-2xl font-bold"
        style={{ color: accent ?? "var(--color-ink)" }}
      >
        {value}
      </div>
      {hint && <div className="text-xs text-muted">{hint}</div>}
    </div>
  );
}
