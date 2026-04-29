export default function KpiCard({
  label,
  value,
  hint,
  accent,
}: {
  label: string;
  value: string;
  hint?: string;
  accent?: string;
}) {
  return (
    <div className="surface p-5 flex flex-col gap-2">
      <span className="text-xs uppercase tracking-wider text-secondary">
        {label}
      </span>
      <span
        className="text-3xl font-bold"
        style={{ color: accent ?? "var(--color-ink)" }}
      >
        {value}
      </span>
      {hint && <span className="text-xs text-muted">{hint}</span>}
    </div>
  );
}
