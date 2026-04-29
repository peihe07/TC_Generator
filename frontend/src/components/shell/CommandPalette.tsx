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
  RiArchive2Line,
  type RemixiconComponentType,
} from "@remixicon/react";
import { useRouter } from "next/navigation";
import { useEffect, useMemo, useState } from "react";
import { toRuns } from "../../services/runAdapter";
import { useCommandPaletteStore } from "../../store/useCommandPaletteStore";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";

interface Command {
  id: string;
  label: string;
  group: "Navigate" | "Action" | "Run";
  href?: string;
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
  { id: "act-new-run", label: "New Run", group: "Action", href: "/run-builder", icon: RiAddLine, keywords: "create start generate" },
  { id: "nav-legacy", label: "Open Legacy Desktop", group: "Action", href: "/legacy", icon: RiArchive2Line, keywords: "98 windows old" },
];

export default function CommandPalette() {
  const open = useCommandPaletteStore((s) => s.open);
  const setOpen = useCommandPaletteStore((s) => s.setOpen);
  const toggle = useCommandPaletteStore((s) => s.toggle);
  const router = useRouter();
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);

  const [query, setQuery] = useState("");
  const [activeIndex, setActiveIndex] = useState(0);

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
    if (open && !loaded) loadFromStorage();
    if (open) {
      setQuery("");
      setActiveIndex(0);
    }
  }, [open, loaded, loadFromStorage]);

  const runCommands: Command[] = useMemo(() => {
    if (!query.trim()) return [];
    return toRuns(records)
      .slice(0, 8)
      .map((r) => ({
        id: `run-${r.id}`,
        label: `${r.kindLabel} · ${r.id}`,
        group: "Run" as const,
        href: `/runs/${r.id}`,
        icon: RiPlayCircleLine,
        keywords: r.model,
      }));
  }, [records, query]);

  const allCommands = useMemo(
    () => [...STATIC_COMMANDS, ...runCommands],
    [runCommands]
  );

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return allCommands;
    return allCommands.filter((c) => {
      const hay = `${c.label} ${c.keywords ?? ""} ${c.group}`.toLowerCase();
      return hay.includes(q);
    });
  }, [allCommands, query]);

  useEffect(() => {
    setActiveIndex(0);
  }, [query]);

  const grouped = useMemo(() => {
    const map = new Map<Command["group"], Command[]>();
    for (const c of filtered) {
      const arr = map.get(c.group) ?? [];
      arr.push(c);
      map.set(c.group, arr);
    }
    return Array.from(map.entries());
  }, [filtered]);

  if (!open) return null;

  const exec = (cmd: Command) => {
    if (cmd.href) router.push(cmd.href);
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

  // 計算每個項目在 filtered 中的 index 以對應 activeIndex
  let runningIdx = 0;

  return (
    <div
      className="fixed inset-0 z-50 flex items-start justify-center p-4 pt-[15vh]"
      onClick={() => setOpen(false)}
      style={{ backgroundColor: "rgba(0, 21, 36, 0.45)", backdropFilter: "blur(4px)" }}
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className="surface-floating w-full max-w-xl overflow-hidden"
      >
        <input
          autoFocus
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Type a command, page, or run id..."
          className="w-full bg-transparent px-5 py-4 text-base outline-none text-primary placeholder:text-[var(--color-teal)] placeholder:opacity-60"
        />
        <div
          className="border-t-0"
          style={{
            boxShadow: "inset 0 1px 0 rgba(21, 97, 109, 0.15)",
          }}
        />
        <div className="max-h-[50vh] overflow-y-auto py-2">
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
                      <span className="flex-1 text-sm text-primary truncate">
                        {c.label}
                      </span>
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
