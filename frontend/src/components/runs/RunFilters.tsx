"use client";

import { RiSearchLine } from "@remixicon/react";
import type { RunKind, RunStatus } from "../../services/runAdapter";

const STATUS_OPTIONS: Array<{ value: RunStatus | "all"; label: string }> = [
  { value: "all", label: "All" },
  { value: "running", label: "Running" },
  { value: "completed", label: "Completed" },
  { value: "failed", label: "Failed" },
  { value: "partial", label: "Partial" },
];

const KIND_OPTIONS: Array<{ value: RunKind | "all"; label: string }> = [
  { value: "all", label: "All kinds" },
  { value: "generate", label: "Generate" },
  { value: "quick", label: "Quick" },
  { value: "group", label: "Group" },
  { value: "regenerate", label: "Regenerate" },
  { value: "rerun", label: "Rerun" },
  { value: "export", label: "Export" },
  { value: "suggest-fix", label: "Suggest Fix" },
];

export interface RunFilterValue {
  status: RunStatus | "all";
  kind: RunKind | "all";
  q: string;
  showArchived: boolean;
}

export default function RunFilters({
  value,
  onChange,
}: {
  value: RunFilterValue;
  onChange: (next: RunFilterValue) => void;
}) {
  return (
    <div className="surface p-4 flex flex-wrap items-center gap-3">
      <Pills
        value={value.status}
        options={STATUS_OPTIONS}
        onChange={(v) => onChange({ ...value, status: v as RunStatus | "all" })}
      />

      <select
        value={value.kind}
        onChange={(e) =>
          onChange({ ...value, kind: e.target.value as RunKind | "all" })
        }
        className="bg-transparent text-sm py-1.5 px-2 rounded-md focus-ring text-secondary"
        style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.2)" }}
      >
        {KIND_OPTIONS.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>

      <div
        className="flex items-center gap-2 px-3 py-1.5 rounded-md flex-1 min-w-[200px]"
        style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.2)" }}
      >
        <RiSearchLine size={14} className="text-secondary" />
        <input
          value={value.q}
          onChange={(e) => onChange({ ...value, q: e.target.value })}
          placeholder="Search by run id..."
          className="bg-transparent text-sm flex-1 outline-none text-primary placeholder:text-[var(--color-teal)] placeholder:opacity-60"
        />
      </div>

      <label className="flex items-center gap-2 text-xs font-bold text-secondary cursor-pointer focus-ring rounded">
        <input
          type="checkbox"
          checked={value.showArchived}
          onChange={(e) =>
            onChange({ ...value, showArchived: e.target.checked })
          }
          className="sr-only"
        />
        <span
          className="flex items-center justify-center w-4 h-4 rounded transition-all"
          style={{
            backgroundColor: value.showArchived
              ? "var(--color-tangerine)"
              : "transparent",
            boxShadow: value.showArchived
              ? "0 1px 2px var(--shadow-tint)"
              : "inset 0 0 0 1.5px var(--color-teal)",
            color: "var(--color-ink)",
          }}
        >
          {value.showArchived && (
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
        Show archived
      </label>
    </div>
  );
}

function Pills<T extends string>({
  value,
  options,
  onChange,
}: {
  value: T;
  options: Array<{ value: T; label: string }>;
  onChange: (v: T) => void;
}) {
  return (
    <div className="flex items-center gap-1">
      {options.map((o) => {
        const active = o.value === value;
        return (
          <button
            key={o.value}
            type="button"
            onClick={() => onChange(o.value)}
            className="px-3 py-1.5 text-xs font-bold rounded-md focus-ring transition-all"
            style={{
              backgroundColor: active
                ? "var(--color-tangerine)"
                : "transparent",
              color: active ? "var(--color-ink)" : "var(--color-teal)",
            }}
          >
            {o.label}
          </button>
        );
      })}
    </div>
  );
}
