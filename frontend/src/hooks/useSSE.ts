"use client";

import { useEffect } from "react";

import { useJobStore } from "@/src/store/useJobStore";

type UseSSEOptions = {
  enabled: boolean;
  url: string | null;
  onMessage?: (data: string) => void;
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
      onMessage?.(event.data);
      appendLog({
        level: "info",
        message: event.data,
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
