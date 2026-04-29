"use client";

import { RiCheckLine } from "@remixicon/react";
import { BUILDER_STEPS, STEP_DEFINITIONS, type BuilderStep } from "./types";

export default function BuilderStepper({
  current,
  onJump,
  highestVisited,
}: {
  current: BuilderStep;
  onJump: (step: BuilderStep) => void;
  highestVisited: BuilderStep;
}) {
  const currentIdx = BUILDER_STEPS.indexOf(current);
  const visitedIdx = BUILDER_STEPS.indexOf(highestVisited);

  return (
    <div className="surface p-4">
      <ol className="flex items-center gap-2">
        {BUILDER_STEPS.map((step, idx) => {
          const def = STEP_DEFINITIONS[step];
          const done = idx < currentIdx;
          const active = idx === currentIdx;
          const reachable = idx <= visitedIdx;

          return (
            <li
              key={step}
              className="flex-1 flex items-center gap-2 min-w-0"
            >
              <button
                type="button"
                disabled={!reachable}
                onClick={() => reachable && onJump(step)}
                className="flex items-center gap-2.5 min-w-0 focus-ring rounded-md px-2 py-1.5 transition-all"
                style={{
                  opacity: reachable ? 1 : 0.4,
                  cursor: reachable ? "pointer" : "not-allowed",
                }}
              >
                <span
                  className="flex items-center justify-center w-7 h-7 rounded-full text-xs font-bold shrink-0"
                  style={{
                    backgroundColor: active
                      ? "var(--color-tangerine)"
                      : done
                      ? "var(--color-teal)"
                      : "rgba(21, 97, 109, 0.15)",
                    color: active || done ? "var(--color-papaya)" : "var(--color-teal)",
                  }}
                >
                  {done ? <RiCheckLine size={14} /> : idx + 1}
                </span>
                <div className="min-w-0 text-left hidden md:block">
                  <div
                    className="text-xs font-bold truncate"
                    style={{
                      color: active ? "var(--color-ink)" : "var(--color-teal)",
                    }}
                  >
                    {def.label}
                  </div>
                  <div className="text-[10px] text-muted truncate">
                    {def.description}
                  </div>
                </div>
              </button>
              {idx < BUILDER_STEPS.length - 1 && (
                <span
                  className="flex-1 h-px"
                  style={{
                    backgroundColor:
                      idx < currentIdx
                        ? "var(--color-teal)"
                        : "rgba(21, 97, 109, 0.2)",
                  }}
                />
              )}
            </li>
          );
        })}
      </ol>
    </div>
  );
}
