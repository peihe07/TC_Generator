import Link from "next/link";

export default function PagePlaceholder({
  title,
  description,
  upcoming,
}: {
  title: string;
  description: string;
  upcoming: string[];
}) {
  return (
    <div className="space-y-6">
      <header className="space-y-2">
        <h1 className="text-3xl font-bold text-primary">{title}</h1>
        <p className="text-secondary text-sm">{description}</p>
      </header>

      <section className="surface p-6 space-y-3">
        <h2 className="text-sm font-bold text-primary uppercase tracking-wider">
          Upcoming
        </h2>
        <ul className="space-y-1.5 text-sm text-secondary">
          {upcoming.map((item) => (
            <li key={item} className="flex gap-2">
              <span style={{ color: "var(--color-tangerine)" }}>›</span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </section>

      <p className="text-xs text-muted">
        Legacy desktop available at{" "}
        <Link
          href="/legacy"
          className="underline decoration-dotted hover:opacity-80"
          style={{ color: "var(--color-tangerine)" }}
        >
          /legacy
        </Link>
      </p>
    </div>
  );
}
