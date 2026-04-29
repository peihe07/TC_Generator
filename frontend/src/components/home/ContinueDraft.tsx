"use client";

import Link from "next/link";
import { useEffect } from "react";
import { RiDraftLine, RiArrowRightLine } from "@remixicon/react";
import { useBuilderDraftStore } from "../../store/useBuilderDraftStore";
import { STEP_DEFINITIONS } from "../builder/types";
import { formatRelativeTime } from "../../services/runAdapter";

export default function ContinueDraft() {
  const draft = useBuilderDraftStore((s) => s.draft);
  const loaded = useBuilderDraftStore((s) => s.loaded);
  const loadFromStorage = useBuilderDraftStore((s) => s.loadFromStorage);
  const clear = useBuilderDraftStore((s) => s.clear);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  if (!loaded || !draft) return null;

  const stepDef = STEP_DEFINITIONS[draft.currentStep];

  return (
    <section className="surface p-5 flex items-center gap-4">
      <span
        className="flex items-center justify-center w-10 h-10 rounded-lg shrink-0"
        style={{
          backgroundColor: "rgba(255, 125, 0, 0.18)",
          color: "var(--color-tangerine)",
        }}
      >
        <RiDraftLine size={20} />
      </span>
      <div className="flex-1 min-w-0">
        <div className="text-sm font-bold text-primary">
          Continue draft — {stepDef.label}
        </div>
        <div className="text-xs text-muted">
          Updated {formatRelativeTime(draft.updatedAt)} ·{" "}
          <code>{draft.id}</code>
        </div>
      </div>
      <button
        type="button"
        onClick={() => {
          if (window.confirm("Discard current draft?")) clear();
        }}
        className="text-xs text-muted hover:text-secondary focus-ring rounded px-2 py-1"
      >
        Discard
      </button>
      <Link
        href={`/run-builder?step=${draft.currentStep}`}
        className="cta inline-flex items-center gap-1.5 text-sm"
      >
        Resume
        <RiArrowRightLine size={16} />
      </Link>
    </section>
  );
}
