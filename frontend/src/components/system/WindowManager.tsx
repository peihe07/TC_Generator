"use client";

import { ConfigureWindow } from "@/src/components/modules/configure/ConfigureWindow";
import { ExportWindow } from "@/src/components/modules/export/ExportWindow";
import { GenerateWindow } from "@/src/components/modules/generate/GenerateWindow";
import { ReviewWindow } from "@/src/components/modules/review/ReviewWindow";
import { UploadWindow } from "@/src/components/modules/upload/UploadWindow";
import { AppWindow } from "@/src/components/system/AppWindow";
import { useWindowStore } from "@/src/store/useWindowStore";

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
        <ReviewWindow />
      </AppWindow>
      <AppWindow windowState={windows.export}>
        <ExportWindow />
      </AppWindow>
    </>
  );
}
