import Link from "next/link";
import type { RemixiconComponentType } from "@remixicon/react";

interface EmptyStateProps {
  Icon?: RemixiconComponentType;
  title: string;
  description?: React.ReactNode;
  action?: {
    label: string;
    href: string;
  };
  size?: "sm" | "md";
}

export default function EmptyState({
  Icon,
  title,
  description,
  action,
  size = "md",
}: EmptyStateProps) {
  const padding = size === "sm" ? "p-6" : "p-10";
  return (
    <div className={`surface ${padding} text-center space-y-3`}>
      {Icon && (
        <div className="flex justify-center">
          <span
            className="flex items-center justify-center w-12 h-12 rounded-full"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            <Icon size={22} />
          </span>
        </div>
      )}
      <div className="space-y-1">
        <h3 className="text-base font-bold text-primary">{title}</h3>
        {description && (
          <p className="text-sm text-secondary">{description}</p>
        )}
      </div>
      {action && (
        <div className="pt-1">
          <Link href={action.href} className="cta inline-flex text-sm">
            {action.label}
          </Link>
        </div>
      )}
    </div>
  );
}
