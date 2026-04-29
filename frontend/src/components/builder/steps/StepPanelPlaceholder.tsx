export default function StepPanelPlaceholder({
  title,
  description,
  upcoming,
}: {
  title: string;
  description: string;
  upcoming: string[];
}) {
  return (
    <div className="surface p-8 space-y-4">
      <header className="space-y-1">
        <h2 className="text-xl font-bold text-primary">{title}</h2>
        <p className="text-sm text-secondary">{description}</p>
      </header>
      <div className="space-y-1.5">
        <div className="text-xs uppercase tracking-wider text-muted">
          Upcoming
        </div>
        <ul className="space-y-1 text-sm text-secondary">
          {upcoming.map((u) => (
            <li key={u} className="flex gap-2">
              <span style={{ color: "var(--color-tangerine)" }}>›</span>
              <span>{u}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
