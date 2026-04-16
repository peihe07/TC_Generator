"use client";

import { RiFileExcel2Line, RiFolderChartLine, RiSettings3Line } from "@remixicon/react";

import { DESKTOP_ICON_ORDER, WINDOW_DEFINITIONS } from "@/src/lib/constants";
import type { WindowId } from "@/src/lib/types";
import { useWindowStore } from "@/src/store/useWindowStore";

const iconMap: Record<WindowId, React.ReactNode> = {
  upload: <RiFileExcel2Line size={28} />,
  configure: <RiSettings3Line size={28} />,
  generate: <RiFolderChartLine size={28} />,
  review: <RiFolderChartLine size={28} />,
  export: <RiFolderChartLine size={28} />,
};

export function Desktop() {
  const openWindow = useWindowStore((state) => state.openWindow);

  return (
    <section className="desktop">
      <div className="desktop-icon-grid">
        {DESKTOP_ICON_ORDER.map((id) => {
          const item = WINDOW_DEFINITIONS[id];
          return (
            <button
              key={id}
              className="desktop-icon"
              onDoubleClick={() => openWindow(id)}
              title={item.description}
              type="button"
            >
              <span className="desktop-icon-glyph">{iconMap[id]}</span>
              <span className="icon-label">{item.title}</span>
            </button>
          );
        })}
      </div>
    </section>
  );
}
