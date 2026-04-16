"use client";

import { Desktop } from "@/src/components/system/Desktop";
import { Taskbar } from "@/src/components/system/Taskbar";
import { WindowManager } from "@/src/components/system/WindowManager";

export default function Home() {
  return (
    <main className="desktop-shell">
      <Desktop />
      <WindowManager />
      <Taskbar />
    </main>
  );
}
