"use client";

import { useState } from "react";

type RulesTab = "aspice" | "ai" | "design";

const TABS: { id: RulesTab; label: string; src: string }[] = [
  { id: "aspice", label: "ASPICE SWE.6 Writing Rules", src: "/rules-aspice.html" },
  { id: "ai", label: "AI Instruction", src: "/rules-ai-instruction.html" },
  { id: "design", label: "Design Method Decision", src: "/rules-design-method.html" },
];

export default function RulesView() {
  const [active, setActive] = useState<RulesTab>("aspice");
  const current = TABS.find((t) => t.id === active) ?? TABS[0];

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Rules</h1>
        <p className="text-secondary text-sm">
          Reference rule sheets used by the generator for ASPICE SWE.6 test
          case writing.
        </p>
      </header>

      <nav
        role="tablist"
        aria-label="Rule sheets"
        className="flex items-center gap-1 flex-wrap"
      >
        {TABS.map((tab) => {
          const isActive = tab.id === active;
          return (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={isActive}
              onClick={() => setActive(tab.id)}
              className="relative px-4 py-2 text-sm font-bold rounded-md transition-colors focus-ring"
              style={{
                color: isActive ? "var(--color-papaya)" : "var(--color-ink)",
                backgroundColor: isActive
                  ? "var(--color-teal)"
                  : "rgba(21, 97, 109, 0.08)",
              }}
            >
              {tab.label}
            </button>
          );
        })}
      </nav>

      <div
        role="tabpanel"
        className="surface overflow-hidden"
        style={{ height: "calc(100vh - 240px)", minHeight: 480 }}
      >
        <iframe
          key={current.id}
          src={current.src}
          title={current.label}
          style={{
            width: "100%",
            height: "100%",
            border: "none",
            display: "block",
          }}
        />
      </div>
    </div>
  );
}
