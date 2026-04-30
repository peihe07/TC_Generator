"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const items = [
  { href: "/", label: "Home" },
  { href: "/quick", label: "Quick TC" },
  { href: "/runs", label: "Runs" },
  { href: "/templates", label: "Templates" },
  { href: "/outputs", label: "Outputs" },
  { href: "/data", label: "Data" },
  { href: "/diagrams", label: "Diagrams" },
  { href: "/rules", label: "Rules" },
] as const;

export default function PrimaryNav() {
  const pathname = usePathname();

  return (
    <nav className="flex items-center gap-1">
      {items.map((item) => {
        const active =
          item.href === "/"
            ? pathname === "/"
            : pathname.startsWith(item.href);
        return (
          <Link
            key={item.href}
            href={item.href}
            className={`relative px-4 py-2 text-sm transition-colors focus-ring rounded-md ${
              active
                ? "text-[var(--color-papaya)] font-bold"
                : "text-[var(--color-papaya)]/70 hover:text-[var(--color-papaya)]"
            }`}
          >
            {item.label}
            {active && (
              <span
                className="absolute left-2 right-2 -bottom-0.5 h-0.5 rounded-full"
                style={{ backgroundColor: "var(--color-tangerine)" }}
              />
            )}
          </Link>
        );
      })}
    </nav>
  );
}
