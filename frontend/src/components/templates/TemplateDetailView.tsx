"use client";

import {
  RiArrowLeftLine,
  RiArrowRightLine,
  RiBookmarkLine,
  RiFileList3Line,
} from "@remixicon/react";
import Link from "next/link";
import { useEffect, useState } from "react";
import {
  fetchSpecLibrary,
  type SpecLibraryEntry,
} from "../../services/jobAdapter";
import { formatSpecLibraryLabel } from "../../lib/specLibrary";
import { track } from "../../lib/telemetry";
import { Skeleton, SkeletonRows } from "../shell/Skeleton";

interface UsageResponse {
  name: string;
  usageCount: number;
  lastUsedAt: number | null;
  recentRunIds: string[];
}

export default function TemplateDetailView({
  templateId,
}: {
  templateId: string;
}) {
  const [entry, setEntry] = useState<SpecLibraryEntry | null | undefined>(
    undefined
  );
  const [error, setError] = useState<string | null>(null);
  const [usage, setUsage] = useState<UsageResponse | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetchSpecLibrary()
      .then((list) => {
        if (cancelled) return;
        const found = list.find((e) => e.name === templateId);
        setEntry(found ?? null);
      })
      .catch((err) => {
        if (!cancelled)
          setError(err instanceof Error ? err.message : "Fetch failed");
      });
    fetch(`/api/spec-library/${encodeURIComponent(templateId)}/usage`)
      .then(async (res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return (await res.json()) as UsageResponse;
      })
      .then((data) => {
        if (!cancelled) setUsage(data);
      })
      .catch(() => {
        // 默默 fallback
      });
    return () => {
      cancelled = true;
    };
  }, [templateId]);

  if (entry === undefined && !error) {
    return (
      <div className="space-y-6">
        <BackLink />
        <header className="flex items-start gap-4">
          <Skeleton width={48} height={48} rounded={10} />
          <div className="flex-1 space-y-2">
            <Skeleton height={28} width="40%" />
            <Skeleton height={12} width="25%" />
          </div>
        </header>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          {[0, 1, 2].map((i) => (
            <div key={i} className="surface p-4 space-y-2">
              <Skeleton height={10} width="40%" />
              <Skeleton height={20} width="60%" />
            </div>
          ))}
        </div>
        <div className="surface p-5">
          <SkeletonRows rows={3} />
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="space-y-6">
        <BackLink />
        <div
          className="surface p-6 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          {error}
        </div>
      </div>
    );
  }

  if (entry === null || entry === undefined) {
    return (
      <div className="space-y-6">
        <BackLink />
        <div className="surface p-10 text-center space-y-2">
          <h1 className="text-xl font-bold text-primary">
            Template not found
          </h1>
          <p className="text-sm text-muted">
            <code className="text-secondary">{templateId}</code>
          </p>
        </div>
      </div>
    );
  }

  const label = formatSpecLibraryLabel(entry.name);

  return (
    <div className="space-y-6">
      <BackLink />

      <header className="flex items-start justify-between gap-4 flex-wrap">
        <div className="flex items-start gap-4">
          <span
            className="flex items-center justify-center w-12 h-12 rounded-lg shrink-0"
            style={{
              backgroundColor: "rgba(255, 125, 0, 0.18)",
              color: "var(--color-tangerine)",
            }}
          >
            <RiBookmarkLine size={24} />
          </span>
          <div className="space-y-1">
            <h1 className="text-3xl font-bold text-primary">{label}</h1>
            <code className="text-xs text-muted">{entry.name}</code>
          </div>
        </div>

        <Link
          href={`/run-builder?templateId=${encodeURIComponent(entry.name)}`}
          onClick={() =>
            track("template_use_click", { templateId: entry.name })
          }
          className="cta inline-flex items-center gap-1.5 text-sm"
        >
          Use in New Run
          <RiArrowRightLine size={16} />
        </Link>
      </header>

      <section className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <Stat
          icon={<RiFileList3Line size={14} />}
          label="Entries"
          value={
            entry.entriesCount != null ? entry.entriesCount.toString() : "—"
          }
        />
        <Stat label="Embedding Model" value={entry.embeddingModel ?? "—"} />
        <Stat label="Updated" value={entry.updatedAt ?? "—"} />
      </section>

      {entry.sourceFile && (
        <section className="surface p-5 space-y-2">
          <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
            Source File
          </h2>
          <code className="block text-sm text-secondary break-all">
            {entry.sourceFile}
          </code>
        </section>
      )}

      <section className="surface p-5 space-y-3">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Usage
        </h2>
        {usage ? (
          <div className="space-y-3">
            <dl className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-sm">
              <div>
                <dt className="text-[10px] uppercase tracking-wider text-muted">
                  Runs using this template
                </dt>
                <dd className="text-2xl font-bold text-primary">
                  {usage.usageCount}
                </dd>
              </div>
              <div>
                <dt className="text-[10px] uppercase tracking-wider text-muted">
                  Last used
                </dt>
                <dd className="text-sm text-primary">
                  {usage.lastUsedAt
                    ? formatRelativeTs(usage.lastUsedAt)
                    : "—"}
                </dd>
              </div>
            </dl>
            {usage.recentRunIds.length > 0 && (
              <div className="space-y-1">
                <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
                  Recent runs
                </div>
                <ul className="space-y-1 text-xs">
                  {usage.recentRunIds.map((runId) => (
                    <li key={runId}>
                      <Link
                        href={`/runs/${runId}`}
                        className="font-bold focus-ring rounded"
                        style={{ color: "var(--color-tangerine)" }}
                      >
                        {runId}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ) : (
          <p className="text-xs text-muted">Loading usage…</p>
        )}
      </section>

      <section className="surface p-5 space-y-3">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Coming Soon
        </h2>
        <ul className="space-y-1.5 text-sm text-secondary">
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Entries preview (search and inspect rules)</span>
          </li>
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Version history and changelog</span>
          </li>
          <li className="flex gap-2">
            <span style={{ color: "var(--color-tangerine)" }}>›</span>
            <span>Clone, deprecate, override actions</span>
          </li>
        </ul>
      </section>
    </div>
  );
}

function formatRelativeTs(ts: number): string {
  const diff = Date.now() - ts;
  if (diff < 60_000) return "just now";
  if (diff < 3_600_000) return `${Math.floor(diff / 60_000)}m ago`;
  if (diff < 86_400_000) return `${Math.floor(diff / 3_600_000)}h ago`;
  return `${Math.floor(diff / 86_400_000)}d ago`;
}

function BackLink() {
  return (
    <Link
      href="/templates"
      className="inline-flex items-center gap-1.5 text-sm text-secondary hover:text-primary focus-ring rounded"
    >
      <RiArrowLeftLine size={16} />
      Back to templates
    </Link>
  );
}

function Stat({
  icon,
  label,
  value,
}: {
  icon?: React.ReactNode;
  label: string;
  value: string;
}) {
  return (
    <div className="surface p-4 space-y-1">
      <div className="text-xs flex items-center gap-1.5 uppercase tracking-wider text-secondary">
        {icon}
        {label}
      </div>
      <div className="text-base font-bold text-primary truncate">{value}</div>
    </div>
  );
}
