"use client";

import {
  RiDatabase2Line,
  RiArrowRightLine,
  RiUploadCloud2Line,
} from "@remixicon/react";
import Link from "next/link";
import EmptyState from "../shell/EmptyState";
import { useEffect, useMemo } from "react";
import { useBuilderDraftStore } from "../../store/useBuilderDraftStore";
import { useJobStore } from "../../store/useJobStore";
import { useWorkspaceFilteredRecords } from "../../lib/useWorkspaceFiltered";
import {
  formatCost,
  formatRelativeTime,
} from "../../services/runAdapter";

interface Dataset {
  jobId: string;
  fileName?: string;
  latestKind: string;
  latestActivity: number;
  rowCount: number;
  totalCost: number;
  runCount: number;
  active?: boolean;
}

const KIND_LABEL: Record<string, string> = {
  generate: "Generate",
  quick: "Quick Generate",
  group: "Group",
  regenerate: "Regenerate",
  rerun: "Rerun",
  "suggest-fix": "Suggest Fix",
  export: "Export",
};

export default function DataView() {
  const records = useWorkspaceFilteredRecords();

  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const tcRows = useJobStore((s) => s.tcRows);

  const draft = useBuilderDraftStore((s) => s.draft);
  const draftLoaded = useBuilderDraftStore((s) => s.loaded);
  const loadDraft = useBuilderDraftStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!draftLoaded) loadDraft();
  }, [draftLoaded, loadDraft]);

  const datasets = useMemo<Dataset[]>(() => {
    const map = new Map<string, Dataset>();

    for (const rec of records) {
      const cur = map.get(rec.id);
      if (!cur) {
        map.set(rec.id, {
          jobId: rec.id,
          latestKind: rec.kind,
          latestActivity: rec.startedAt,
          rowCount: rec.rowsTotal,
          totalCost: rec.cost ?? 0,
          runCount: 1,
        });
      } else {
        cur.runCount += 1;
        cur.totalCost += rec.cost ?? 0;
        if (rec.startedAt > cur.latestActivity) {
          cur.latestActivity = rec.startedAt;
          cur.latestKind = rec.kind;
        }
        if (rec.rowsTotal > cur.rowCount) cur.rowCount = rec.rowsTotal;
      }
    }

    // 當前 active 的 dataset (in-memory job + draft)
    if (jobMetadata?.jobId && !map.has(jobMetadata.jobId)) {
      map.set(jobMetadata.jobId, {
        jobId: jobMetadata.jobId,
        fileName: draft?.data?.fileName,
        latestKind: "generate",
        latestActivity: Date.now(),
        rowCount: tcRows.length,
        totalCost: 0,
        runCount: 0,
        active: true,
      });
    } else if (jobMetadata?.jobId) {
      const cur = map.get(jobMetadata.jobId);
      if (cur) {
        cur.fileName = draft?.data?.fileName ?? cur.fileName;
        cur.active = true;
      }
    }

    // draft.data 沒在 history 裡（user 上傳了但還沒開始 generate）
    if (draft?.data?.datasetId && !map.has(draft.data.datasetId)) {
      map.set(draft.data.datasetId, {
        jobId: draft.data.datasetId,
        fileName: draft.data.fileName,
        latestKind: "uploaded",
        latestActivity: draft.updatedAt,
        rowCount: draft.data.rowCount ?? 0,
        totalCost: 0,
        runCount: 0,
        active: jobMetadata?.jobId === draft.data.datasetId,
      });
    }

    return Array.from(map.values()).sort(
      (a, b) => b.latestActivity - a.latestActivity
    );
  }, [records, jobMetadata, tcRows, draft]);

  return (
    <div className="space-y-6">
      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Data</h1>
          <p className="text-secondary text-sm">
            Datasets you have parsed and used. Each entry maps to a backend
            job context.
          </p>
        </div>
        <Link
          href="/run-builder"
          className="cta inline-flex items-center gap-1.5 text-sm"
        >
          <RiUploadCloud2Line size={16} />
          Upload via New Run
        </Link>
      </header>

      {datasets.length === 0 ? (
        <EmptyState
          Icon={RiDatabase2Line}
          title="No datasets yet"
          description="Upload a workbook in a New Run to register it here."
          action={{ label: "Start New Run", href: "/run-builder" }}
        />
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {datasets.map((d) => (
            <DatasetCard key={d.jobId} dataset={d} />
          ))}
        </div>
      )}
    </div>
  );
}

function DatasetCard({ dataset }: { dataset: Dataset }) {
  const label =
    dataset.fileName ??
    `Job ${dataset.jobId.slice(0, 8)}…`;

  return (
    <article className="surface p-5 space-y-3">
      <div className="flex items-start gap-3">
        <span
          className="flex items-center justify-center w-10 h-10 rounded-lg shrink-0"
          style={{
            backgroundColor: dataset.active
              ? "rgba(255, 125, 0, 0.18)"
              : "rgba(21, 97, 109, 0.12)",
            color: dataset.active
              ? "var(--color-tangerine)"
              : "var(--color-teal)",
          }}
        >
          <RiDatabase2Line size={20} />
        </span>
        <div className="flex-1 min-w-0">
          <h2 className="text-base font-bold text-primary truncate">
            {label}
          </h2>
          <code className="text-[10px] text-muted truncate block">
            {dataset.jobId}
          </code>
          {dataset.active && (
            <span
              className="text-[10px] uppercase tracking-wider font-bold"
              style={{ color: "var(--color-tangerine)" }}
            >
              Active in builder
            </span>
          )}
        </div>
      </div>

      <dl className="grid grid-cols-3 gap-2 text-xs">
        <Stat label="Rows" value={String(dataset.rowCount || "—")} />
        <Stat label="Runs" value={String(dataset.runCount)} />
        <Stat label="Cost" value={formatCost(dataset.totalCost)} />
      </dl>

      <div className="flex items-center justify-between gap-2 pt-1">
        <span className="text-[10px] text-muted">
          {KIND_LABEL[dataset.latestKind] ?? dataset.latestKind} ·{" "}
          {formatRelativeTime(dataset.latestActivity)}
        </span>
        <Link
          href={`/run-builder?dataset=${encodeURIComponent(dataset.jobId)}`}
          className="text-xs font-bold focus-ring rounded px-2 py-1 inline-flex items-center gap-1"
          style={{ color: "var(--color-tangerine)" }}
        >
          Use in New Run
          <RiArrowRightLine size={12} />
        </Link>
      </div>
    </article>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-[9px] uppercase tracking-wider text-muted">
        {label}
      </dt>
      <dd className="text-sm font-bold text-primary truncate">{value}</dd>
    </div>
  );
}
