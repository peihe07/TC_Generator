"use client";

import {
  RiArrowRightLine,
  RiHome3Line,
  RiPlayCircleLine,
  RiFileList3Line,
  RiInboxLine,
  RiDatabase2Line,
  RiSettings3Line,
  RiAddLine,
  RiDownload2Line,
  RiRefreshLine,
  RiBookmarkLine,
  RiDraftLine,
  RiCloseCircleLine,
  type RemixiconComponentType,
} from "@remixicon/react";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useRef, useState } from "react";
import { fetchSpecLibrary, type SpecLibraryEntry } from "../../services/jobAdapter";
import { toRuns } from "../../services/runAdapter";
import { useBuilderDraftStore } from "../../store/useBuilderDraftStore";
import { useCommandPaletteStore } from "../../store/useCommandPaletteStore";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { formatSpecLibraryLabel } from "../../lib/specLibrary";

type CommandGroup = "Navigate" | "Action" | "Run" | "Template" | "Output";

interface Command {
  id: string;
  label: string;
  hint?: string;
  group: CommandGroup;
  href?: string;
  external?: boolean; // <a target=_blank style download
  onSelect?: () => void;
  icon: RemixiconComponentType;
  keywords?: string;
}

const STATIC_COMMANDS: Command[] = [
  { id: "nav-home", label: "Home", group: "Navigate", href: "/", icon: RiHome3Line },
  { id: "nav-runs", label: "Runs", group: "Navigate", href: "/runs", icon: RiPlayCircleLine },
  { id: "nav-templates", label: "Templates", group: "Navigate", href: "/templates", icon: RiFileList3Line },
  { id: "nav-outputs", label: "Outputs", group: "Navigate", href: "/outputs", icon: RiInboxLine },
  { id: "nav-data", label: "Data", group: "Navigate", href: "/data", icon: RiDatabase2Line },
  { id: "nav-settings", label: "Settings", group: "Navigate", href: "/settings", icon: RiSettings3Line },
  { id: "act-new-run", label: "New Run", group: "Action", href: "/run-builder", icon: RiAddLine, keywords: "create start generate builder" },
];

export default function CommandPalette() {
  const open = useCommandPaletteStore((s) => s.open);
  const setOpen = useCommandPaletteStore((s) => s.setOpen);
  const toggle = useCommandPaletteStore((s) => s.toggle);
  const router = useRouter();
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);
  const draft = useBuilderDraftStore((s) => s.draft);
  const draftLoaded = useBuilderDraftStore((s) => s.loaded);
  const loadDraft = useBuilderDraftStore((s) => s.loadFromStorage);
  const clearDraft = useBuilderDraftStore((s) => s.clear);

  const [query, setQuery] = useState("");
  const [activeIndex, setActiveIndex] = useState(0);
  const [templates, setTemplates] = useState<SpecLibraryEntry[]>([]);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  // 全域 Cmd/Ctrl+K
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        toggle();
      } else if (e.key === "Escape") {
        setOpen(false);
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [toggle, setOpen]);

  useEffect(() => {
    if (!open) {
      // 關閉時把焦點還給先前的元素，鍵盤使用者不會迷路
      previousFocusRef.current?.focus?.();
      previousFocusRef.current = null;
      return;
    }
    previousFocusRef.current =
      typeof document !== "undefined"
        ? (document.activeElement as HTMLElement | null)
        : null;
    if (!loaded) loadFromStorage();
    if (!draftLoaded) loadDraft();
    setQuery("");
    setActiveIndex(0);
    // 拉一次 templates（沿用 spec-library）
    fetchSpecLibrary()
      .then((list) => setTemplates(list))
      .catch(() => setTemplates([]));
  }, [open, loaded, loadFromStorage, draftLoaded, loadDraft]);

  // ---------- Dynamic commands ----------
  const runs = useMemo(() => toRuns(records), [records]);

  const recentRunCommands: Command[] = useMemo(() => {
    return runs.slice(0, 6).map((r) => ({
      id: `run-${r.id}`,
      label: `Open ${r.kindLabel}`,
      hint: r.id,
      group: "Run" as const,
      href: `/runs/${r.id}`,
      icon: RiPlayCircleLine,
      keywords: `${r.id} ${r.model} open`,
    }));
  }, [runs]);

  const rerunCommands: Command[] = useMemo(() => {
    return runs.slice(0, 5).map((r) => ({
      id: `rerun-${r.id}`,
      label: `Rerun ${r.kindLabel}`,
      hint: r.id,
      group: "Run" as const,
      href: `/run-builder?from=${encodeURIComponent(r.id)}`,
      icon: RiRefreshLine,
      keywords: `rerun ${r.id} ${r.model}`,
    }));
  }, [runs]);

  const outputCommands: Command[] = useMemo(() => {
    return runs
      .filter(
        (r) =>
          r.status !== "running" &&
          ["generate", "quick", "rerun", "regenerate"].includes(r.kind)
      )
      .slice(0, 5)
      .map((r) => ({
        id: `dl-${r.id}`,
        label: `Download output`,
        hint: r.id,
        group: "Output" as const,
        href: `/api/export/download/${encodeURIComponent(r.id)}`,
        external: true,
        icon: RiDownload2Line,
        keywords: `download export ${r.id}`,
      }));
  }, [runs]);

  const templateCommands: Command[] = useMemo(() => {
    return templates.slice(0, 6).map((t) => ({
      id: `tpl-${t.name}`,
      label: `Use template ${formatSpecLibraryLabel(t.name)}`,
      hint: t.name,
      group: "Template" as const,
      href: `/run-builder?templateId=${encodeURIComponent(t.name)}`,
      icon: RiBookmarkLine,
      keywords: `${t.name} ${formatSpecLibraryLabel(t.name)} template`,
    }));
  }, [templates]);

  const draftCommands: Command[] = useMemo(() => {
    if (!draft) return [];
    return [
      {
        id: "draft-resume",
        label: "Resume current draft",
        hint: draft.id,
        group: "Action",
        href: `/run-builder?step=${draft.currentStep}`,
        icon: RiDraftLine,
        keywords: "draft resume continue",
      },
      {
        id: "draft-discard",
        label: "Discard current draft",
        hint: draft.id,
        group: "Action",
        onSelect: () => {
          if (window.confirm("Discard current draft?")) {
            clearDraft();
          }
        },
        icon: RiCloseCircleLine,
        keywords: "draft delete reset",
      },
    ];
  }, [draft, clearDraft]);

  const allCommands = useMemo(
    () => [
      ...STATIC_COMMANDS,
      ...draftCommands,
      ...recentRunCommands,
      ...rerunCommands,
      ...outputCommands,
      ...templateCommands,
    ],
    [
      draftCommands,
      recentRunCommands,
      rerunCommands,
      outputCommands,
      templateCommands,
    ]
  );

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return allCommands;
    return allCommands.filter((c) => {
      const hay = `${c.label} ${c.hint ?? ""} ${c.keywords ?? ""} ${c.group}`.toLowerCase();
      return hay.includes(q);
    });
  }, [allCommands, query]);

  useEffect(() => {
    setActiveIndex(0);
  }, [query]);

  const grouped = useMemo(() => {
    const order: CommandGroup[] = [
      "Action",
      "Navigate",
      "Run",
      "Template",
      "Output",
    ];
    const map = new Map<CommandGroup, Command[]>();
    for (const c of filtered) {
      const arr = map.get(c.group) ?? [];
      arr.push(c);
      map.set(c.group, arr);
    }
    return order
      .filter((g) => map.has(g))
      .map((g) => [g, map.get(g)!] as const);
  }, [filtered]);

  if (!open) return null;

  const exec = (cmd: Command) => {
    if (cmd.onSelect) {
      cmd.onSelect();
      setOpen(false);
      return;
    }
    if (cmd.href) {
      if (cmd.external) {
        window.open(cmd.href, "_blank", "noopener");
      } else {
        router.push(cmd.href);
      }
    }
    setOpen(false);
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActiveIndex((i) => Math.min(filtered.length - 1, i + 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActiveIndex((i) => Math.max(0, i - 1));
    } else if (e.key === "Enter") {
      e.preventDefault();
      const cmd = filtered[activeIndex];
      if (cmd) exec(cmd);
    }
  };

  let runningIdx = 0;

  return (
    <div
      className="fixed inset-0 z-50 flex items-start justify-center p-4 pt-[15vh]"
      onClick={() => setOpen(false)}
      style={{
        backgroundColor: "rgba(0, 21, 36, 0.45)",
        backdropFilter: "blur(4px)",
      }}
      role="presentation"
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className="surface-floating w-full max-w-xl overflow-hidden"
        role="dialog"
        aria-label="Command palette"
        aria-modal="true"
      >
        <input
          autoFocus
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Type a command, run id, template, or page..."
          className="w-full bg-transparent px-5 py-4 text-base outline-none text-primary placeholder:text-[var(--color-teal)] placeholder:opacity-60"
        />
        <div style={{ boxShadow: "inset 0 1px 0 rgba(21, 97, 109, 0.15)" }} />
        <div className="max-h-[55vh] overflow-y-auto py-2">
          {filtered.length === 0 ? (
            <div className="px-5 py-6 text-sm text-muted text-center">
              No results
            </div>
          ) : (
            grouped.map(([group, items]) => (
              <div key={group} className="py-1">
                <div className="px-5 py-1 text-xs uppercase tracking-wider text-muted">
                  {group}
                </div>
                {items.map((c) => {
                  const idx = runningIdx++;
                  const active = idx === activeIndex;
                  const Icon = c.icon;
                  return (
                    <button
                      key={c.id}
                      type="button"
                      onClick={() => exec(c)}
                      onMouseEnter={() => setActiveIndex(idx)}
                      className="w-full flex items-center gap-3 px-5 py-2 text-left transition-colors"
                      style={{
                        backgroundColor: active
                          ? "rgba(255, 125, 0, 0.18)"
                          : "transparent",
                      }}
                    >
                      <Icon size={16} />
                      <div className="flex-1 min-w-0">
                        <div className="text-sm text-primary truncate">
                          {c.label}
                        </div>
                        {c.hint && (
                          <div className="text-[10px] text-muted truncate">
                            {c.hint}
                          </div>
                        )}
                      </div>
                      {active && (
                        <RiArrowRightLine
                          size={14}
                          style={{ color: "var(--color-tangerine)" }}
                        />
                      )}
                    </button>
                  );
                })}
              </div>
            ))
          )}
        </div>
        <div
          className="px-5 py-2 text-xs text-muted flex items-center gap-3"
          style={{ boxShadow: "inset 0 1px 0 rgba(21, 97, 109, 0.15)" }}
        >
          <span>
            <kbd className="px-1.5 py-0.5 rounded bg-white/40">↑↓</kbd> navigate
          </span>
          <span>
            <kbd className="px-1.5 py-0.5 rounded bg-white/40">↵</kbd> select
          </span>
          <span>
            <kbd className="px-1.5 py-0.5 rounded bg-white/40">esc</kbd> close
          </span>
        </div>
      </div>
    </div>
  );
}
