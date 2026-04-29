"use client";

import {
  RiCheckLine,
  RiCloseLine,
  RiAlertLine,
} from "@remixicon/react";
import { useEffect, useMemo, useRef } from "react";
import { track } from "../../../lib/telemetry";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../store/useJobStore";

export default function ValidateStep() {
  const tcRows = useJobStore((s) => s.tcRows);
  const config = useJobStore((s) => s.config);
  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  const checks = useMemo(() => buildChecks(tcRows, config, jobMetadata), [
    tcRows,
    config,
    jobMetadata,
  ]);

  const criticalFails = checks.filter(
    (c) => c.status === "fail" && c.critical
  ).length;

  const lastFailCount = useRef<number | null>(null);
  useEffect(() => {
    if (criticalFails === 0) {
      markStepComplete("validate", true);
    } else {
      markStepComplete("validate", false);
      if (lastFailCount.current !== criticalFails) {
        track("builder_validation_fail", { criticalCount: criticalFails });
      }
    }
    lastFailCount.current = criticalFails;
  }, [criticalFails, markStepComplete]);

  const reqCount = useMemo(
    () =>
      new Set(tcRows.map((r) => r.reqId).filter(Boolean)).size ||
      tcRows.length,
    [tcRows]
  );
  const testSetsCount = useMemo(
    () =>
      new Set(tcRows.map((r) => r.testSet).filter(Boolean)).size,
    [tcRows]
  );

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h2 className="text-xl font-bold text-primary">Validate</h2>
        <p className="text-sm text-secondary">
          Confirm everything is in order before kicking off the run.
        </p>
      </header>

      {criticalFails > 0 && (
        <div
          className="surface p-4 flex items-start gap-3 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          <RiAlertLine size={18} className="shrink-0 mt-0.5" />
          <div>
            <div className="font-bold">
              {criticalFails} critical issue{criticalFails > 1 ? "s" : ""} —
              fix before continuing.
            </div>
            <p className="text-secondary text-xs mt-0.5">
              Resolve the items below in earlier steps. Validate refreshes
              automatically.
            </p>
          </div>
        </div>
      )}

      <section className="surface p-5 space-y-3">
        <h3 className="text-xs uppercase tracking-wider text-secondary font-bold">
          Pre-flight Checks
        </h3>
        <ul className="space-y-1">
          {checks.map((c) => (
            <CheckRow key={c.id} check={c} />
          ))}
        </ul>
      </section>

      <section className="surface p-5 space-y-3">
        <h3 className="text-xs uppercase tracking-wider text-secondary font-bold">
          Run Snapshot
        </h3>
        <dl className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-sm">
          <SnapshotItem label="Rows" value={String(tcRows.length)} />
          <SnapshotItem label="Requirements" value={String(reqCount)} />
          <SnapshotItem label="Test Sets" value={String(testSetsCount)} />
          <SnapshotItem label="Model" value={config.model} />
          <SnapshotItem
            label="Batch Size"
            value={String(config.batchSize)}
          />
          <SnapshotItem
            label="Budget"
            value={`$${config.budgetLimit}`}
          />
          <SnapshotItem
            label="Target Columns"
            value={String(config.targetColumns.length)}
          />
          <SnapshotItem
            label="Strict"
            value={config.strictValidation ? "On" : "Off"}
          />
        </dl>
      </section>
    </div>
  );
}

interface Check {
  id: string;
  label: string;
  status: "ok" | "warn" | "fail";
  critical: boolean;
  detail?: string;
}

function buildChecks(
  tcRows: ReturnType<typeof useJobStore.getState>["tcRows"],
  config: ReturnType<typeof useJobStore.getState>["config"],
  jobMetadata: ReturnType<typeof useJobStore.getState>["jobMetadata"]
): Check[] {
  const out: Check[] = [];

  out.push({
    id: "rows",
    label: "Dataset loaded",
    status: tcRows.length > 0 ? "ok" : "fail",
    critical: true,
    detail:
      tcRows.length > 0
        ? `${tcRows.length} row(s) ready`
        : "Go to Select Data and parse a workbook",
  });

  out.push({
    id: "job-id",
    label: "Job context",
    status: jobMetadata?.jobId ? "ok" : "warn",
    critical: false,
    detail: jobMetadata?.jobId
      ? `Backend jobId ${jobMetadata.jobId}`
      : "No backend jobId yet (may be created on execute)",
  });

  out.push({
    id: "target-cols",
    label: "Target columns",
    status: config.targetColumns.length > 0 ? "ok" : "fail",
    critical: true,
    detail:
      config.targetColumns.length > 0
        ? `${config.targetColumns.length} column(s) selected`
        : "Pick at least one target column in Configure",
  });

  const testSetCount = new Set(
    tcRows.map((r) => r.testSet).filter(Boolean)
  ).size;
  out.push({
    id: "test-sets",
    label: "Test Sets assigned",
    status: testSetCount > 0 ? "ok" : "warn",
    critical: false,
    detail:
      testSetCount > 0
        ? `${testSetCount} distinct Test Set(s)`
        : "All rows share the default Test Set",
  });

  out.push({
    id: "budget",
    label: "Budget set",
    status: config.budgetLimit > 0 ? "ok" : "warn",
    critical: false,
    detail:
      config.budgetLimit > 0
        ? `$${config.budgetLimit} cap`
        : "No budget cap (cost won't be flagged)",
  });

  return out;
}

function CheckRow({ check }: { check: Check }) {
  const colors = {
    ok: "var(--color-teal)",
    warn: "var(--color-tangerine)",
    fail: "var(--color-brandy)",
  } as const;
  const Icon =
    check.status === "ok"
      ? RiCheckLine
      : check.status === "warn"
      ? RiAlertLine
      : RiCloseLine;
  return (
    <li className="flex items-start gap-3 px-2 py-2 rounded row-hover">
      <span
        className="flex items-center justify-center w-5 h-5 rounded-full shrink-0 mt-0.5"
        style={{
          backgroundColor: colors[check.status] + "22",
          color: colors[check.status],
        }}
      >
        <Icon size={12} />
      </span>
      <div className="flex-1">
        <div className="text-sm text-primary font-bold">{check.label}</div>
        {check.detail && (
          <div className="text-xs text-muted">{check.detail}</div>
        )}
      </div>
      {check.status === "fail" && check.critical && (
        <span
          className="text-[10px] font-bold uppercase tracking-wider"
          style={{ color: "var(--color-brandy)" }}
        >
          Blocking
        </span>
      )}
    </li>
  );
}

function SnapshotItem({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-[10px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-base font-bold text-primary truncate">{value}</dd>
    </div>
  );
}
