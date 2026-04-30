"use client";

import {
  RiBookmarkLine,
  RiFileList3Line,
  RiSearchLine,
} from "@remixicon/react";
import EmptyState from "../shell/EmptyState";
import { SkeletonCard } from "../shell/Skeleton";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import {
  fetchSpecLibrary,
  type SpecLibraryEntry,
} from "../../services/jobAdapter";
import { formatSpecLibraryLabel } from "../../lib/specLibrary";

export default function TemplatesView() {
  const [entries, setEntries] = useState<SpecLibraryEntry[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");
  const [showDeprecated, setShowDeprecated] = useState(false);

  useEffect(() => {
    let cancelled = false;
    fetchSpecLibrary()
      .then((list) => {
        if (!cancelled) setEntries(list);
      })
      .catch((err) => {
        if (!cancelled)
          setError(err instanceof Error ? err.message : "Fetch failed");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const deprecatedCount = useMemo(
    () => entries?.filter((e) => e.deprecated).length ?? 0,
    [entries]
  );

  const filtered = useMemo(() => {
    if (!entries) return null;
    const q = query.trim().toLowerCase();
    return entries.filter((e) => {
      if (e.deprecated && !showDeprecated) return false;
      if (!q) return true;
      const hay = `${e.name} ${formatSpecLibraryLabel(
        e.name
      )} ${e.sourceFile ?? ""}`.toLowerCase();
      return hay.includes(q);
    });
  }, [entries, query, showDeprecated]);

  return (
    <div className="space-y-6">
      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Templates</h1>
          <p className="text-secondary text-sm">
            Reusable, versioned generation rules. Powered by spec-library.
          </p>
        </div>
        {entries && (
          <span className="text-xs text-muted">
            {filtered?.length ?? 0} of {entries.length}
          </span>
        )}
      </header>

      <div
        className="surface px-4 py-2 flex items-center gap-3 flex-wrap"
        style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.15)" }}
      >
        <div className="flex items-center gap-2 flex-1 min-w-[200px]">
          <RiSearchLine size={16} className="text-secondary" />
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search templates..."
            className="bg-transparent text-sm flex-1 outline-none text-primary placeholder:text-[var(--color-teal)] placeholder:opacity-60"
          />
        </div>
        {deprecatedCount > 0 && (
          <label className="flex items-center gap-2 text-xs font-bold text-secondary cursor-pointer focus-ring rounded">
            <input
              type="checkbox"
              checked={showDeprecated}
              onChange={(e) => setShowDeprecated(e.target.checked)}
              className="sr-only"
            />
            <span
              className="flex items-center justify-center w-4 h-4 rounded transition-all"
              style={{
                backgroundColor: showDeprecated
                  ? "var(--color-tangerine)"
                  : "transparent",
                boxShadow: showDeprecated
                  ? "0 1px 2px var(--shadow-tint)"
                  : "inset 0 0 0 1.5px var(--color-teal)",
                color: "var(--color-ink)",
              }}
            >
              {showDeprecated && (
                <svg width="10" height="10" viewBox="0 0 12 12" fill="none">
                  <path
                    d="M2 6.5L5 9.5L10 3.5"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
              )}
            </span>
            Show deprecated ({deprecatedCount})
          </label>
        )}
      </div>

      {error && (
        <div
          className="surface p-4 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          {error}
        </div>
      )}

      {entries === null && !error && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Array.from({ length: 6 }).map((_, i) => (
            <SkeletonCard key={i} />
          ))}
        </div>
      )}

      {filtered && filtered.length === 0 && (
        <EmptyState
          Icon={RiBookmarkLine}
          title={
            entries && entries.length > 0
              ? "No templates match the search"
              : "No templates yet"
          }
          description={
            entries && entries.length > 0
              ? "Try a different keyword."
              : "Templates appear once your spec library is populated."
          }
        />
      )}

      {filtered && filtered.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filtered.map((entry) => (
            <TemplateCard key={entry.name} entry={entry} />
          ))}
        </div>
      )}
    </div>
  );
}

function TemplateCard({ entry }: { entry: SpecLibraryEntry }) {
  const label = formatSpecLibraryLabel(entry.name);
  return (
    <Link
      href={`/templates/${encodeURIComponent(entry.name)}`}
      className="surface p-5 space-y-3 block focus-ring"
      style={{ opacity: entry.deprecated ? 0.55 : 1 }}
    >
      <div className="flex items-start gap-3">
        <span
          className="flex items-center justify-center w-10 h-10 rounded-lg shrink-0"
          style={{
            backgroundColor: "rgba(255, 125, 0, 0.18)",
            color: "var(--color-tangerine)",
          }}
        >
          <RiBookmarkLine size={20} />
        </span>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap">
            <h2 className="text-base font-bold text-primary truncate">
              {label}
            </h2>
            {entry.deprecated && (
              <span
                className="text-[10px] uppercase tracking-wider font-bold"
                style={{ color: "var(--color-brandy)" }}
              >
                deprecated
              </span>
            )}
          </div>
          <p className="text-xs text-muted truncate">{entry.name}</p>
        </div>
      </div>

      <dl className="grid grid-cols-2 gap-2 text-xs">
        <Stat
          icon={<RiFileList3Line size={12} />}
          label="Entries"
          value={
            entry.entriesCount != null ? entry.entriesCount.toString() : "—"
          }
        />
        <Stat
          label="Model"
          value={entry.embeddingModel ?? "—"}
        />
      </dl>

      {entry.updatedAt && (
        <div className="text-[10px] text-muted">
          Updated {entry.updatedAt}
        </div>
      )}
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
    <div>
      <dt className="flex items-center gap-1 text-[10px] uppercase tracking-wider text-muted">
        {icon}
        {label}
      </dt>
      <dd className="text-sm text-primary truncate">{value}</dd>
    </div>
  );
}
