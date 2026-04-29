"use client";

import Link from "next/link";
import { RiAddLine } from "@remixicon/react";
import { track } from "../../lib/telemetry";

export default function NewRunButton() {
  return (
    <Link
      href="/run-builder"
      onClick={() => track("home_new_run_click", { source: "top-nav" })}
      className="cta inline-flex items-center gap-1.5 text-sm"
    >
      <RiAddLine size={16} />
      New Run
    </Link>
  );
}
