"use client";

import { useEffect, useRef, useState } from "react";
import {
  RiLoader4Line,
  RiPlayMiniFill,
  RiPulseLine,
  RiStopMiniFill,
} from "@remixicon/react";

import { useBackendBaseUrl, useHealthcheck } from "@/src/hooks/usePythonAPI";
import { useSSE } from "@/src/hooks/useSSE";
import { useJobStore } from "@/src/store/useJobStore";
import type { TcRow, ValidationIssue } from "@/src/lib/types";

function buildMockGeneratedRow(row: TcRow): Pick<TcRow, "status" | "reviewStatus" | "generated" | "validation"> {
  const rewrite = `(${row.testItem || row.reqId} -> Observable outcome confirmed)`;
  const warningMode = row.reqId.endsWith("2") || row.reqId.endsWith("4");
  const validation: ValidationIssue[] = warningMode
    ? [
        {
          id: `${row.id}-warn-procedure`,
          severity: "warning",
          field: "test_procedure",
          message: "Final verification wording should be tightened before export.",
        },
      ]
    : [
        {
          id: `${row.id}-pass-shape`,
          severity: "passing",
          field: "expected_result",
          message: "Mock output is structurally aligned with the generated steps.",
        },
      ];

  return {
    status: warningMode ? "error" : "ready",
    reviewStatus: "pending",
    generated: {
      testItemRewrite: rewrite,
      preConditions: warningMode
        ? "1. Vehicle profile loaded\n2. Open setup screen"
        : "1. Vehicle profile loaded\n2. Required subsystem available",
      testProcedure:
        "1. Open the source screen and prepare the feature.\n2. Trigger the target behavior and verify the visible outcome.",
      expectedResult:
        "1. The setup screen is ready for the operator.\n2. The requested behavior is shown with the correct visible outcome.",
      designMethod: warningMode
        ? "Functional smoke review"
        : "功能測試 (Functional based ; no specific technique)",
      priority: warningMode ? "Medium" : "High",
    },
    validation,
  };
}

export function GenerateWindow() {
  const jobId = useJobStore((state) => state.jobId);
  const tcRows = useJobStore((state) => state.tcRows);
  const logs = useJobStore((state) => state.logs);
  const stats = useJobStore((state) => state.stats);
  const config = useJobStore((state) => state.config);
  const setJobId = useJobStore((state) => state.setJobId);
  const setStats = useJobStore((state) => state.setStats);
  const updateRow = useJobStore((state) => state.updateRow);
  const appendLog = useJobStore((state) => state.appendLog);
  const health = useHealthcheck();
  const backendBaseUrl = useBackendBaseUrl();
  const [isMockRunning, setIsMockRunning] = useState(false);
  const mockTimer = useRef<number | null>(null);

  useSSE({
    enabled: Boolean(backendBaseUrl && jobId),
    url: backendBaseUrl && jobId ? `${backendBaseUrl}/api/generate/stream?jobId=${jobId}` : null,
    onMessage: (data) => {
      if (data.toLowerCase().includes("complete")) {
        setStats({ processed: stats.total });
      }
    },
  });

  useEffect(() => {
    return () => {
      if (mockTimer.current) {
        window.clearInterval(mockTimer.current);
      }
    };
  }, []);

  const startMockRun = () => {
    if (!tcRows.length || isMockRunning) {
      return;
    }

    setIsMockRunning(true);
    setJobId(`mock-${Date.now()}`);
    setStats({ total: tcRows.length, processed: 0, currentCost: 0 });
    appendLog({
      level: "info",
      message: `Mock generation queued for ${tcRows.length} row(s) with batch size ${config.batchSize}.`,
    });

    let processed = 0;
    mockTimer.current = window.setInterval(() => {
      const nextChunk = tcRows.slice(processed, processed + config.batchSize);
      processed += nextChunk.length;
      const currentCost = Number((processed * 0.0085).toFixed(4));
      nextChunk.forEach((row) => updateRow(row.id, buildMockGeneratedRow(row)));
      setStats({
        total: tcRows.length,
        processed,
        currentCost,
      });
      appendLog({
        level: "info",
        message: `Processed ${processed}/${tcRows.length} rows. Estimated mock cost $${currentCost.toFixed(4)}.`,
      });

      if (processed >= tcRows.length) {
        if (mockTimer.current) {
          window.clearInterval(mockTimer.current);
        }
        mockTimer.current = null;
        setIsMockRunning(false);
        appendLog({
          level: "info",
          message: "Mock generation complete. Review and export windows are ready for the next phase.",
        });
      }
    }, 1200);
  };

  const stopMockRun = () => {
    if (mockTimer.current) {
      window.clearInterval(mockTimer.current);
    }
    mockTimer.current = null;
    setIsMockRunning(false);
    appendLog({
      level: "error",
      message: "Mock generation stopped by operator.",
    });
  };

  return (
    <div className={`window-content-grid ${isMockRunning ? "is-busy" : ""}`}>
      <div className="sunken-panel accent-panel">
        <div>
          <p className="eyebrow">Phase 1 / Generate</p>
          <h2>Run the desktop like a control room.</h2>
          <p>
            This monitor now shows backend reachability and a local mock
            execution path so the shell can be exercised before the Python API
            is fully wired.
          </p>
        </div>
        <div className="metric-strip">
          <div className="metric-card">
            <span className="metric-label">Processed</span>
            <strong>
              {stats.processed}/{stats.total || tcRows.length}
            </strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Cost</span>
            <strong>${stats.currentCost.toFixed(4)}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Health</span>
            <strong>
              {backendBaseUrl
                ? health.isSuccess
                  ? "online"
                  : health.isPending
                    ? "probing"
                    : "offline"
                : "unset"}
            </strong>
          </div>
        </div>
      </div>

      <div className="window-columns">
        <div className="sunken-panel">
          <h3>Run Controls</h3>
          <div className="button-row">
            <button type="button" onClick={startMockRun} disabled={!tcRows.length || isMockRunning}>
              <RiPlayMiniFill size={14} />
              Start mock run
            </button>
            <button type="button" onClick={stopMockRun} disabled={!isMockRunning}>
              <RiStopMiniFill size={14} />
              Stop
            </button>
          </div>

          <div className="checklist-panel">
            <div className="checklist-row">
              <RiPulseLine size={16} />
              <div>
                <strong>Python health</strong>
                <p>
                  {backendBaseUrl
                    ? health.isSuccess
                      ? "Service responded to /api/health."
                      : health.isPending
                        ? "Health probe in flight."
                        : "No response from configured backend."
                    : "Backend URL is not configured yet."}
                </p>
              </div>
            </div>
            <div className="checklist-row">
              <RiLoader4Line size={16} className={isMockRunning ? "spin" : ""} />
              <div>
                <strong>Stream target</strong>
                <p>
                  {jobId && backendBaseUrl
                    ? `${backendBaseUrl}/api/generate/stream?jobId=${jobId}`
                    : "No active SSE stream. Mock runs still update the desktop logs."}
                </p>
              </div>
            </div>
          </div>

          <div className="sunken-subpanel">
            <h4>Runtime assumptions</h4>
            <p>
              Batch size is currently <strong>{config.batchSize}</strong> and
              strict validation is{" "}
              <strong>{config.strictValidation ? "enabled" : "disabled"}</strong>.
            </p>
          </div>
        </div>

        <div className="sunken-panel">
          <h3>Live Console</h3>
          <div className="log-list tall">
            {logs.map((log, index) => (
              <div key={`${log.timestamp}-${index}`} className={`log-entry ${log.level}`}>
                <span>[{log.timestamp}]</span>
                <span>{log.message}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
