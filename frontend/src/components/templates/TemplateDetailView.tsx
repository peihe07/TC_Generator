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
  type SpecChangelogEntry,
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
            <div className="flex items-center gap-2 flex-wrap">
              <h1 className="text-3xl font-bold text-primary">{label}</h1>
              {entry.deprecated && (
                <span
                  className="text-[10px] uppercase tracking-wider font-bold px-2 py-0.5 rounded"
                  style={{
                    color: "var(--color-brandy)",
                    backgroundColor: "rgba(120, 41, 15, 0.1)",
                  }}
                >
                  deprecated
                </span>
              )}
            </div>
            <code className="text-xs text-muted">{entry.name}</code>
          </div>
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <DeprecateToggle
            entry={entry}
            onChange={(updated) => setEntry({ ...entry, ...updated })}
          />
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
        </div>
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

      <ChangelogSection
        templateId={entry.name}
        version={entry.version ?? null}
        entries={entry.changelog ?? []}
        onAppended={(updated) => {
          setEntry({
            ...entry,
            version: updated.version ?? entry.version,
            changelog: updated.changelog ?? entry.changelog,
          });
        }}
      />

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
            <span>Clone, deprecate, override actions</span>
          </li>
        </ul>
      </section>
    </div>
  );
}

function ChangelogSection({
  templateId,
  version,
  entries,
  onAppended,
}: {
  templateId: string;
  version: string | null;
  entries: SpecChangelogEntry[];
  onAppended: (updated: { version?: string | null; changelog?: SpecChangelogEntry[] }) => void;
}) {
  const [showForm, setShowForm] = useState(false);
  const [draftVersion, setDraftVersion] = useState("");
  const [draftMessage, setDraftMessage] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async () => {
    if (!draftMessage.trim()) {
      setError("Message required.");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch(
        `/api/spec-library/${encodeURIComponent(templateId)}/changelog`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            version: draftVersion.trim() || undefined,
            message: draftMessage.trim(),
          }),
        }
      );
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail ?? `Status ${res.status}`);
      }
      const body = await res.json();
      onAppended({
        version: body.spec?.version,
        changelog: body.spec?.changelog,
      });
      track("template_save", {
        templateId,
        kind: "changelog",
        version: body.spec?.version ?? undefined,
      });
      setDraftVersion("");
      setDraftMessage("");
      setShowForm(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Append failed");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section className="surface p-5 space-y-3">
      <header className="flex items-center justify-between gap-2">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Changelog
        </h2>
        <div className="flex items-center gap-2">
          {version && (
            <code className="text-xs text-secondary">v{version}</code>
          )}
          <button
            type="button"
            onClick={() => {
              setShowForm((v) => !v);
              setError(null);
            }}
            className="text-xs font-bold focus-ring rounded px-2 py-1"
            style={{ color: "var(--color-tangerine)" }}
          >
            {showForm ? "Cancel" : "+ Add entry"}
          </button>
        </div>
      </header>

      {entries.length === 0 ? (
        <p className="text-xs text-muted">
          No changelog entries yet.
        </p>
      ) : (
        <ol className="space-y-2">
          {[...entries].reverse().map((c, i) => (
            <li
              key={`${c.ts}-${i}`}
              className="flex items-start gap-3"
            >
              <span
                className="mt-1.5 inline-block w-2 h-2 rounded-full shrink-0"
                style={{ backgroundColor: "var(--color-tangerine)" }}
              />
              <div className="flex-1 min-w-0 space-y-0.5">
                <div className="flex items-center gap-2 text-xs">
                  <span className="font-bold text-primary">v{c.version}</span>
                  <span className="text-muted">
                    {new Date(c.ts).toLocaleString()}
                  </span>
                  {c.author && (
                    <span className="text-muted">· {c.author}</span>
                  )}
                </div>
                <div className="text-sm text-secondary whitespace-pre-wrap">
                  {c.message}
                </div>
              </div>
            </li>
          ))}
        </ol>
      )}

      {showForm && (
        <div className="space-y-2 pt-1">
          <input
            value={draftVersion}
            onChange={(e) => setDraftVersion(e.target.value)}
            placeholder={`Version (default ${version ?? "1.0.0"})`}
            className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring placeholder:text-[var(--color-teal)] placeholder:opacity-60"
            style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
          />
          <textarea
            value={draftMessage}
            onChange={(e) => setDraftMessage(e.target.value)}
            placeholder="What changed?"
            rows={3}
            className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring resize-y placeholder:text-[var(--color-teal)] placeholder:opacity-60"
            style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
          />
          {error && (
            <p
              className="text-xs"
              style={{ color: "var(--color-brandy)" }}
            >
              {error}
            </p>
          )}
          <div className="flex justify-end">
            <button
              type="button"
              onClick={() => void submit()}
              disabled={submitting}
              className="cta inline-flex items-center text-xs px-3 py-1.5 disabled:opacity-50"
            >
              {submitting ? "Saving…" : "Save entry"}
            </button>
          </div>
        </div>
      )}
    </section>
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

function DeprecateToggle({
  entry,
  onChange,
}: {
  entry: SpecLibraryEntry;
  onChange: (patch: Partial<SpecLibraryEntry>) => void;
}) {
  const [busy, setBusy] = useState(false);
  const isDeprecated = !!entry.deprecated;

  const submit = async () => {
    const next = !isDeprecated;
    if (
      next &&
      !window.confirm(
        `Mark "${entry.name}" as deprecated? It will be hidden from the Templates list by default.`
      )
    )
      return;
    setBusy(true);
    try {
      const res = await fetch(
        `/api/spec-library/${encodeURIComponent(entry.name)}`,
        {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ deprecated: next }),
        }
      );
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail ?? `Status ${res.status}`);
      }
      const body = await res.json();
      onChange({ deprecated: !!body.spec?.deprecated });
      track("template_save", {
        templateId: entry.name,
        kind: "deprecate",
      });
    } catch (err) {
      window.alert(err instanceof Error ? err.message : "Update failed");
    } finally {
      setBusy(false);
    }
  };

  return (
    <button
      type="button"
      onClick={() => void submit()}
      disabled={busy}
      className="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-md font-bold focus-ring disabled:opacity-50"
      style={{
        backgroundColor: isDeprecated
          ? "rgba(21, 97, 109, 0.12)"
          : "rgba(120, 41, 15, 0.1)",
        color: isDeprecated ? "var(--color-teal)" : "var(--color-brandy)",
      }}
    >
      {busy
        ? "Saving…"
        : isDeprecated
        ? "Undeprecate"
        : "Deprecate"}
    </button>
  );
}
