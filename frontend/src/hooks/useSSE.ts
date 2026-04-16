"use client";

import { useEffect } from "react";

import { useJobStore } from "@/src/store/useJobStore";

type UseSSEOptions = {
  enabled: boolean;
  url: string | null;
  onMessage?: (data: string | Record<string, unknown>) => void;
  onError?: () => void;
};

export function useSSE({ enabled, url, onMessage, onError }: UseSSEOptions) {
  const appendLog = useJobStore((state) => state.appendLog);

  useEffect(() => {
    if (!enabled || !url) {
      return;
    }

    const source = new EventSource(url);

    source.onmessage = (event) => {
      let payload: string | Record<string, unknown> = event.data;
      let logMessage = event.data;

      try {
        const parsed = JSON.parse(event.data) as Record<string, unknown>;
        payload = parsed;
        if (typeof parsed.message === "string") {
          logMessage = parsed.message;
        }
      } catch {
        payload = event.data;
      }

      onMessage?.(payload);
      appendLog({
        level: "info",
        message: logMessage,
      });
    };

    source.onerror = () => {
      onError?.();
      appendLog({
        level: "error",
        message: "Live stream disconnected. Waiting for the backend to recover.",
      });
      source.close();
    };

    return () => {
      source.close();
    };
  }, [appendLog, enabled, onError, onMessage, url]);
}
