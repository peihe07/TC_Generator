import Link from "next/link";
import {
  RiAddLine,
  RiFileList3Line,
  RiUploadCloud2Line,
} from "@remixicon/react";
import { track } from "../../lib/telemetry";

type Action = {
  href: string;
  label: string;
  desc: string;
  icon: typeof RiAddLine;
  primary?: boolean;
};

const actions: Action[] = [
  {
    href: "/run-builder",
    label: "New Run",
    desc: "Start a fresh generation flow",
    icon: RiAddLine,
    primary: true,
  },
  {
    href: "/templates",
    label: "Use Template",
    desc: "Pick a saved configuration",
    icon: RiFileList3Line,
  },
  {
    href: "/data",
    label: "Upload Data",
    desc: "Add a dataset to the registry",
    icon: RiUploadCloud2Line,
  },
];

export default function QuickActions() {
  return (
    <section className="surface p-5 space-y-3">
      <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
        Quick Actions
      </h2>
      <div className="space-y-2">
        {actions.map(({ href, label, desc, icon: Icon, primary }) => (
          <Link
            key={href}
            href={href}
            onClick={() => {
              if (href === "/run-builder")
                track("home_new_run_click", { source: "quick-actions" });
            }}
            className="flex items-center gap-3 p-3 rounded-lg row-hover focus-ring transition-all"
          >
            <span
              className="flex items-center justify-center w-9 h-9 rounded-lg"
              style={{
                backgroundColor: primary
                  ? "var(--color-tangerine)"
                  : "rgba(21, 97, 109, 0.12)",
                color: primary ? "var(--color-ink)" : "var(--color-teal)",
              }}
            >
              <Icon size={18} />
            </span>
            <div className="flex-1 min-w-0">
              <div className="text-sm font-bold text-primary">{label}</div>
              <div className="text-xs text-muted">{desc}</div>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
