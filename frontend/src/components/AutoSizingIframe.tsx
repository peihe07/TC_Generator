"use client";

import { useEffect, useRef, useState } from "react";

export default function AutoSizingIframe({
  src,
  title,
}: {
  src: string;
  title: string;
}) {
  const ref = useRef<HTMLIFrameElement | null>(null);
  const [height, setHeight] = useState<number>(480);

  useEffect(() => {
    const iframe = ref.current;
    if (!iframe) return;

    let observer: ResizeObserver | null = null;
    let cancelled = false;

    const measure = () => {
      try {
        const doc = iframe.contentDocument;
        if (!doc) return;
        const next = Math.max(
          doc.body?.scrollHeight ?? 0,
          doc.documentElement?.scrollHeight ?? 0
        );
        if (next > 0 && !cancelled) setHeight(next);
      } catch {
        // 跨網域時讀不到，直接放棄；同源 public/*.html 不會走到這
      }
    };

    const onLoad = () => {
      measure();
      try {
        const doc = iframe.contentDocument;
        const target = doc?.body;
        if (!target || typeof ResizeObserver === "undefined") return;
        observer = new ResizeObserver(() => measure());
        observer.observe(target);
      } catch {
        // 跨網域略過
      }
    };

    iframe.addEventListener("load", onLoad);
    if (iframe.contentDocument?.readyState === "complete") onLoad();

    return () => {
      cancelled = true;
      iframe.removeEventListener("load", onLoad);
      observer?.disconnect();
    };
  }, [src]);

  return (
    <iframe
      ref={ref}
      src={src}
      title={title}
      style={{
        width: "100%",
        height,
        border: "none",
        display: "block",
        backgroundColor: "transparent",
      }}
    />
  );
}
