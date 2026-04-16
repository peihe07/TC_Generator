"use client";

import { useEffect, useState } from "react";
import { RiComputerLine } from "@remixicon/react";

import { DESKTOP_ICON_ORDER } from "@/src/lib/constants";
import { useWindowStore } from "@/src/store/useWindowStore";

export function Taskbar() {
  const windows = useWindowStore((state) => state.windows);
  const toggleWindow = useWindowStore((state) => state.toggleWindow);
  const openWindow = useWindowStore((state) => state.openWindow);
  const focusedWindowId = useWindowStore((state) => state.focusedWindowId);
  const [now, setNow] = useState("");

  useEffect(() => {
    const updateClock = () =>
      setNow(
        new Date().toLocaleTimeString("en-US", {
          hour: "2-digit",
          minute: "2-digit",
        }),
      );

    updateClock();
    const interval = window.setInterval(updateClock, 1000);
    return () => window.clearInterval(interval);
  }, []);

  return (
    <footer className="taskbar">
      <button className="taskbar-start" onClick={() => openWindow("upload")}>
        <RiComputerLine size={16} />
        Start
      </button>
      <div className="taskbar-tabs">
        {DESKTOP_ICON_ORDER.map((id) => {
          const item = windows[id];
          if (!item.isOpen) {
            return null;
          }

          return (
            <button
              key={id}
              className={`taskbar-tab ${focusedWindowId === id && !item.isMinimized ? "active" : ""}`}
              onClick={() => toggleWindow(id)}
              title={item.title}
            >
              <span className="taskbar-tab-icon">{item.icon}</span>
              <span>{item.title}</span>
            </button>
          );
        })}
      </div>
      <div className="taskbar-clock">{now || "--:--"}</div>
    </footer>
  );
}
