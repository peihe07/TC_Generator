"use client";

import { useState, type ReactNode } from "react";
import { RiArrowDownSLine } from "@remixicon/react";

export function Section({
  title,
  defaultOpen = true,
  hint,
  children,
}: {
  title: string;
  defaultOpen?: boolean;
  hint?: string;
  children: ReactNode;
}) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <section className="surface p-5 space-y-3">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="w-full flex items-center justify-between gap-3 focus-ring rounded"
      >
        <div className="text-left">
          <h3 className="text-base font-bold text-primary">{title}</h3>
          {hint && <p className="text-xs text-muted mt-0.5">{hint}</p>}
        </div>
        <RiArrowDownSLine
          size={20}
          className="transition-transform"
          style={{
            transform: open ? "rotate(0deg)" : "rotate(-90deg)",
            color: "var(--color-teal)",
          }}
        />
      </button>
      {open && <div className="pt-2">{children}</div>}
    </section>
  );
}

export function RadioCard({
  name,
  value,
  label,
  checked,
  onChange,
}: {
  name: string;
  value: string;
  label: string;
  checked: boolean;
  onChange: () => void;
}) {
  return (
    <label
      className="flex items-center gap-3 px-3 py-2 rounded-lg cursor-pointer transition-all row-hover"
      style={{
        boxShadow: checked
          ? "inset 0 0 0 2px var(--color-tangerine)"
          : "inset 0 0 0 1px rgba(21, 97, 109, 0.15)",
      }}
    >
      <input
        type="radio"
        name={name}
        value={value}
        checked={checked}
        onChange={onChange}
        className="sr-only"
      />
      <span
        className="flex items-center justify-center w-4 h-4 rounded-full"
        style={{
          boxShadow: checked
            ? "inset 0 0 0 5px var(--color-tangerine)"
            : "inset 0 0 0 1.5px var(--color-teal)",
        }}
      />
      <span className="text-sm text-primary font-bold">{label}</span>
    </label>
  );
}

export function CheckboxCard({
  label,
  checked,
  onChange,
}: {
  label: string;
  checked: boolean;
  onChange: (c: boolean) => void;
}) {
  return (
    <label
      className="flex items-center gap-3 px-3 py-2 rounded-lg cursor-pointer transition-all row-hover"
      style={{
        boxShadow: checked
          ? "inset 0 0 0 2px var(--color-tangerine)"
          : "inset 0 0 0 1px rgba(21, 97, 109, 0.15)",
      }}
    >
      <input
        type="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="sr-only"
      />
      <span
        className="flex items-center justify-center w-4 h-4 rounded transition-all"
        style={{
          backgroundColor: checked ? "var(--color-tangerine)" : "transparent",
          boxShadow: checked
            ? "0 1px 2px var(--shadow-tint)"
            : "inset 0 0 0 1.5px var(--color-teal)",
          color: "var(--color-ink)",
        }}
      >
        {checked && (
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
      <span className="text-sm text-primary">{label}</span>
    </label>
  );
}

export function Slider({
  label,
  value,
  min,
  max,
  onChange,
  display,
}: {
  label: string;
  value: number;
  min: number;
  max: number;
  onChange: (v: number) => void;
  display: string;
}) {
  const pct = ((value - min) / (max - min)) * 100;
  return (
    <div className="space-y-1.5">
      <div className="flex items-center justify-between text-sm">
        <span className="text-primary">{label}</span>
        <span
          className="font-bold"
          style={{ color: "var(--color-tangerine)" }}
        >
          {display}
        </span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(e) => onChange(parseInt(e.target.value, 10))}
        className="w-full appearance-none cursor-pointer focus-ring"
        style={{
          height: 4,
          borderRadius: 4,
          background: `linear-gradient(to right, var(--color-tangerine) 0%, var(--color-tangerine) ${pct}%, rgba(21, 97, 109, 0.2) ${pct}%, rgba(21, 97, 109, 0.2) 100%)`,
        }}
      />
    </div>
  );
}

export function NumberField({
  label,
  value,
  placeholder,
  onChange,
  displayHint,
}: {
  label: string;
  value: number;
  placeholder?: string;
  onChange: (v: number) => void;
  displayHint?: string;
}) {
  return (
    <div className="space-y-1.5">
      <div className="flex items-center justify-between text-sm">
        <span className="text-primary">{label}</span>
        {displayHint && <span className="text-xs text-muted">{displayHint}</span>}
      </div>
      <input
        type="number"
        min={0}
        step={0.01}
        placeholder={placeholder}
        value={value || ""}
        onChange={(e) => {
          const v = parseFloat(e.target.value);
          onChange(Number.isFinite(v) && v > 0 ? v : 0);
        }}
        className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring placeholder:text-[var(--color-teal)] placeholder:opacity-60"
        style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
      />
    </div>
  );
}

export function Toggle({
  label,
  description,
  checked,
  onChange,
}: {
  label: string;
  description?: string;
  checked: boolean;
  onChange: (c: boolean) => void;
}) {
  return (
    <div className="flex items-start gap-3">
      <button
        type="button"
        onClick={() => onChange(!checked)}
        role="switch"
        aria-checked={checked}
        className="relative shrink-0 w-10 h-5 rounded-full transition-all focus-ring mt-0.5"
        style={{
          backgroundColor: checked
            ? "var(--color-tangerine)"
            : "rgba(21, 97, 109, 0.25)",
        }}
      >
        <span
          className="absolute top-0.5 w-4 h-4 rounded-full bg-white transition-all shadow-sm"
          style={{ left: checked ? 22 : 2 }}
        />
      </button>
      <div className="space-y-0.5">
        <div className="text-sm text-primary font-bold">{label}</div>
        {description && (
          <div className="text-xs text-muted">{description}</div>
        )}
      </div>
    </div>
  );
}

export function StatusPill({
  tone,
  children,
}: {
  tone: "ok" | "warn" | "fail" | "info";
  children: ReactNode;
}) {
  const colors: Record<typeof tone, string> = {
    ok: "var(--color-teal)",
    warn: "var(--color-tangerine)",
    fail: "var(--color-brandy)",
    info: "var(--color-teal)",
  };
  return (
    <span
      className="inline-flex items-center gap-1.5 text-xs font-bold"
      style={{ color: colors[tone] }}
    >
      <span
        className="inline-block w-1.5 h-1.5 rounded-full"
        style={{ backgroundColor: colors[tone] }}
      />
      {children}
    </span>
  );
}
