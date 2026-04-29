"use client";

import {
  RiArrowLeftLine,
  RiArrowRightLine,
  RiSave3Line,
  RiPlayCircleLine,
  RiCheckDoubleLine,
} from "@remixicon/react";
import type { BuilderStep } from "./types";
import { BUILDER_STEPS } from "./types";

export default function BuilderActionBar({
  current,
  blocked,
  blockReason,
  onBack,
  onNext,
  onSaveDraft,
  onFinish,
  saving,
}: {
  current: BuilderStep;
  blocked?: boolean;
  blockReason?: string;
  onBack: () => void;
  onNext: () => void;
  onSaveDraft: () => void;
  onFinish: () => void;
  saving?: boolean;
}) {
  const isFirst = current === BUILDER_STEPS[0];
  const isLast = current === BUILDER_STEPS[BUILDER_STEPS.length - 1];
  const nextLabel = current === "execute" ? "Execute" : "Next";

  return (
    <div
      className="sticky bottom-0 mt-4 surface-floating px-5 py-3 flex items-center justify-between gap-3"
      style={{ borderRadius: 16 }}
    >
      <button
        type="button"
        onClick={onBack}
        disabled={isFirst}
        className="inline-flex items-center gap-1.5 px-3 py-2 rounded-md text-sm font-bold focus-ring transition-all disabled:opacity-40"
        style={{
          color: "var(--color-teal)",
        }}
      >
        <RiArrowLeftLine size={16} />
        Back
      </button>

      <div className="flex items-center gap-3">
        {blocked && blockReason && (
          <span
            className="text-xs"
            style={{ color: "var(--color-brandy)" }}
          >
            {blockReason}
          </span>
        )}

        <button
          type="button"
          onClick={onSaveDraft}
          disabled={saving}
          className="inline-flex items-center gap-1.5 px-3 py-2 rounded-md text-sm font-bold focus-ring transition-all disabled:opacity-40"
          style={{
            backgroundColor: "rgba(21, 97, 109, 0.12)",
            color: "var(--color-teal)",
          }}
        >
          <RiSave3Line size={16} />
          {saving ? "Saving..." : "Save Draft"}
        </button>

        {isLast ? (
          <button
            type="button"
            onClick={onFinish}
            className="cta inline-flex items-center gap-1.5 text-sm"
          >
            <RiCheckDoubleLine size={16} />
            Finish & start new
          </button>
        ) : (
          <button
            type="button"
            onClick={onNext}
            disabled={blocked}
            className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {current === "validate" ? (
              <>
                <RiPlayCircleLine size={16} />
                {nextLabel}
              </>
            ) : (
              <>
                {nextLabel}
                <RiArrowRightLine size={16} />
              </>
            )}
          </button>
        )}
      </div>
    </div>
  );
}
