"use client";

import { ConfigureWindow } from "@/src/components/modules/configure/ConfigureWindow";
import { GenerateWindow } from "@/src/components/modules/generate/GenerateWindow";
import { UploadWindow } from "@/src/components/modules/upload/UploadWindow";
import { AppWindow } from "@/src/components/system/AppWindow";
import { useWindowStore } from "@/src/store/useWindowStore";

function PlaceholderWindow({
  title,
  message,
}: {
  title: string;
  message: string;
}) {
  return (
    <div className="window-content-grid">
      <div className="sunken-panel">
        <h3>{title}</h3>
        <p>{message}</p>
      </div>
    </div>
  );
}

export function WindowManager() {
  const windows = useWindowStore((state) => state.windows);

  return (
    <>
      <AppWindow windowState={windows.upload}>
        <UploadWindow />
      </AppWindow>
      <AppWindow windowState={windows.configure}>
        <ConfigureWindow />
      </AppWindow>
      <AppWindow windowState={windows.generate}>
        <GenerateWindow />
      </AppWindow>
      <AppWindow windowState={windows.review}>
        <PlaceholderWindow
          title="Review Desk"
          message="Diff view and validation triage are staged after the upload flow is stable."
        />
      </AppWindow>
      <AppWindow windowState={windows.export}>
        <PlaceholderWindow
          title="Export Cabinet"
          message="Column toggles and download packaging will be added after generation wiring."
        />
      </AppWindow>
    </>
  );
}
