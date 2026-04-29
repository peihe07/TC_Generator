"use client";

import Link from "next/link";
import { RiArchive2Line, RiArrowRightLine, RiInformationLine } from "@remixicon/react";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import type { BuilderStep } from "../types";

export default function LegacyBridgeStep({
  step,
  title,
  description,
  legacyModuleNotes,
  onAdvance,
}: {
  step: BuilderStep;
  title: string;
  description: string;
  legacyModuleNotes: string[];
  onAdvance: () => void;
}) {
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  return (
    <div className="space-y-4">
      <section className="surface p-6 space-y-4">
        <header className="space-y-1">
          <h2 className="text-xl font-bold text-primary">{title}</h2>
          <p className="text-sm text-secondary">{description}</p>
        </header>

        <div
          className="flex items-start gap-3 p-3 rounded-lg"
          style={{
            backgroundColor: "rgba(255, 125, 0, 0.1)",
          }}
        >
          <RiInformationLine
            size={18}
            className="shrink-0 mt-0.5"
            style={{ color: "var(--color-tangerine)" }}
          />
          <div className="space-y-1 text-sm text-primary">
            <div className="font-bold">
              This step is still in legacy desktop mode.
            </div>
            <p className="text-secondary text-xs">
              Phase 2b will rewrite the {title} module in the new design.
              Continue in the legacy desktop for now — your data and config
              are shared with the new builder via the underlying job store.
            </p>
          </div>
        </div>

        <div className="space-y-2">
          <h3 className="text-xs uppercase tracking-wider text-secondary">
            Legacy module covers
          </h3>
          <ul className="space-y-1 text-sm text-secondary">
            {legacyModuleNotes.map((n) => (
              <li key={n} className="flex gap-2">
                <span style={{ color: "var(--color-tangerine)" }}>›</span>
                <span>{n}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="flex items-center gap-2 flex-wrap pt-2">
          <Link
            href="/legacy"
            className="cta inline-flex items-center gap-1.5 text-sm"
          >
            <RiArchive2Line size={16} />
            Continue in Legacy Desktop
          </Link>
          <button
            type="button"
            onClick={() => {
              markStepComplete(step, true);
              onAdvance();
            }}
            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-md text-sm font-bold focus-ring transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            Skip — already done in legacy
            <RiArrowRightLine size={14} />
          </button>
        </div>
      </section>
    </div>
  );
}
