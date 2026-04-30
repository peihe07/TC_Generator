"use client";

import {
  RiArrowDownSLine,
  RiBox3Line,
  RiAddLine,
  RiCheckLine,
  RiDeleteBin6Line,
} from "@remixicon/react";
import { useEffect, useRef, useState } from "react";
import { useWorkspaceStore } from "../../store/useWorkspaceStore";

export default function WorkspaceSwitcher() {
  const workspaces = useWorkspaceStore((s) => s.workspaces);
  const currentId = useWorkspaceStore((s) => s.currentId);
  const loaded = useWorkspaceStore((s) => s.loaded);
  const loadFromStorage = useWorkspaceStore((s) => s.loadFromStorage);
  const switchWorkspace = useWorkspaceStore((s) => s.switchWorkspace);
  const createWorkspace = useWorkspaceStore((s) => s.createWorkspace);
  const removeWorkspace = useWorkspaceStore((s) => s.removeWorkspace);

  const [open, setOpen] = useState(false);
  const [adding, setAdding] = useState(false);
  const [draftName, setDraftName] = useState("");
  const containerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  useEffect(() => {
    if (!open) return;
    const onClick = (e: MouseEvent) => {
      if (
        containerRef.current &&
        !containerRef.current.contains(e.target as Node)
      ) {
        setOpen(false);
        setAdding(false);
      }
    };
    window.addEventListener("mousedown", onClick);
    return () => window.removeEventListener("mousedown", onClick);
  }, [open]);

  const current = workspaces.find((w) => w.id === currentId) ?? workspaces[0];

  const submitNew = () => {
    const name = draftName.trim();
    if (!name) return;
    createWorkspace(name);
    setDraftName("");
    setAdding(false);
    setOpen(false);
  };

  return (
    <div ref={containerRef} className="relative">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex items-center gap-2 px-3 py-2 rounded-md text-[var(--color-papaya)] hover:bg-white/10 focus-ring transition-colors"
      >
        <RiBox3Line size={18} style={{ color: "var(--color-tangerine)" }} />
        <span className="text-sm font-bold tracking-tight max-w-[180px] truncate">
          {current?.name ?? "Workspace"}
        </span>
        <RiArrowDownSLine size={16} className="opacity-70" />
      </button>

      {open && (
        <div
          className="absolute left-0 top-full mt-2 w-64 surface-floating overflow-hidden z-40"
          style={{ borderRadius: 12 }}
          role="menu"
        >
          <ul className="py-1 max-h-[260px] overflow-y-auto">
            {workspaces.map((ws) => {
              const active = ws.id === currentId;
              return (
                <li
                  key={ws.id}
                  className="flex items-center gap-2 px-3 py-2 text-sm row-hover"
                >
                  <button
                    type="button"
                    onClick={() => {
                      switchWorkspace(ws.id);
                      setOpen(false);
                    }}
                    className="flex-1 flex items-center gap-2 text-left text-primary focus-ring rounded"
                  >
                    {active ? (
                      <RiCheckLine
                        size={14}
                        style={{ color: "var(--color-tangerine)" }}
                      />
                    ) : (
                      <span className="inline-block w-3.5" />
                    )}
                    <span className="truncate">{ws.name}</span>
                  </button>
                  {workspaces.length > 1 && (
                    <button
                      type="button"
                      onClick={() => {
                        if (
                          window.confirm(
                            `Remove workspace "${ws.name}"? Records stay tagged with the old id.`
                          )
                        ) {
                          removeWorkspace(ws.id);
                        }
                      }}
                      className="text-muted hover:text-[var(--color-brandy)] focus-ring rounded p-1"
                      aria-label={`Remove workspace ${ws.name}`}
                    >
                      <RiDeleteBin6Line size={12} />
                    </button>
                  )}
                </li>
              );
            })}
          </ul>

          <div
            style={{
              boxShadow: "inset 0 1px 0 rgba(21, 97, 109, 0.15)",
            }}
            className="px-2 py-2"
          >
            {adding ? (
              <div className="space-y-2">
                <input
                  autoFocus
                  value={draftName}
                  onChange={(e) => setDraftName(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") submitNew();
                    if (e.key === "Escape") {
                      setAdding(false);
                      setDraftName("");
                    }
                  }}
                  placeholder="Workspace name"
                  className="w-full bg-transparent text-sm py-1.5 px-2 rounded text-primary focus-ring"
                  style={{
                    boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)",
                  }}
                />
                <div className="flex justify-end gap-2">
                  <button
                    type="button"
                    onClick={() => {
                      setAdding(false);
                      setDraftName("");
                    }}
                    className="text-xs px-2 py-1 rounded text-secondary"
                  >
                    Cancel
                  </button>
                  <button
                    type="button"
                    onClick={submitNew}
                    disabled={!draftName.trim()}
                    className="cta inline-flex items-center text-xs px-3 py-1 disabled:opacity-50"
                  >
                    Create
                  </button>
                </div>
              </div>
            ) : (
              <button
                type="button"
                onClick={() => setAdding(true)}
                className="w-full flex items-center gap-2 px-2 py-1.5 rounded text-sm font-bold focus-ring"
                style={{ color: "var(--color-tangerine)" }}
              >
                <RiAddLine size={14} />
                New workspace
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
