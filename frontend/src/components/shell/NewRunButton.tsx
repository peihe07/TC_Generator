"use client";

import Link from "next/link";
import { RiAddLine } from "@remixicon/react";

export default function NewRunButton() {
  return (
    <Link href="/run-builder" className="cta inline-flex items-center gap-1.5 text-sm">
      <RiAddLine size={16} />
      New Run
    </Link>
  );
}
