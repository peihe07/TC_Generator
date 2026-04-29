"use client";

import {
  RiBookmarkLine,
  RiFileList3Line,
  RiSearchLine,
} from "@remixicon/react";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import {
  fetchSpecLibrary,
  type SpecLibraryEntry,
} from "../../services/jobAdapter";
import { formatSpecLibraryLabel } from "../modules/upload/UploadModule";

export default function TemplatesView() {
  const [entries, setEntries] = useState<SpecLibraryEntry[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");

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

  const filtered = useMemo(() => {
    if (!entries) return null;
    const q = query.trim().toLowerCase();
    if (!q) return entries;
    return entries.filter((e) => {
      const hay = `${e.name} ${formatSpecLibraryLabel(
        e.name
      )} ${e.sourceFile ?? ""}`.toLowerCase();
      return hay.includes(q);
    });
  }, [entries, query]);

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
        className="surface px-4 py-2 flex items-center gap-2"
        style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.15)" }}
      >
        <RiSearchLine size={16} className="text-secondary" />
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search templates..."
          className="bg-transparent text-sm flex-1 outline-none text-primary placeholder:text-[var(--color-teal)] placeholder:opacity-60"
        />
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
        <div className="surface p-8 text-center text-secondary text-sm">
          Loading templates...
        </div>
      )}

      {filtered && filtered.length === 0 && (
        <div className="surface p-8 text-center text-muted text-sm">
          {entries && entries.length > 0
            ? "No templates match the search."
            : "No templates yet."}
        </div>
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
          <h2 className="text-base font-bold text-primary truncate">
            {label}
          </h2>
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
