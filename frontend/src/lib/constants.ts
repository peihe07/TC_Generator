import type { WindowDefinition, WindowId } from "@/src/lib/types";

export const DEFAULT_JOB_CONFIG = {
  model: "claude-sonnet-4-6",
  batchSize: 5,
  budget: 5,
  strictValidation: false,
};

export const WINDOW_DEFINITIONS: Record<WindowId, WindowDefinition> = {
  upload: {
    id: "upload",
    title: "Upload Center",
    description: "Drop in raw specs and preview the first rows before parsing.",
    icon: "A:",
    position: { x: 72, y: 64 },
    size: { width: 620, height: 520 },
  },
  configure: {
    id: "configure",
    title: "Generator Setup",
    description: "Tune batch size, model, budget, and framework matching.",
    icon: "B:",
    position: { x: 280, y: 96 },
    size: { width: 520, height: 440 },
  },
  generate: {
    id: "generate",
    title: "Generation Monitor",
    description: "Watch live logs, queue state, and cost progression.",
    icon: "C:",
    position: { x: 180, y: 140 },
    size: { width: 540, height: 420 },
  },
  review: {
    id: "review",
    title: "Review Desk",
    description: "Compare original requirements against generated output.",
    icon: "D:",
    position: { x: 340, y: 120 },
    size: { width: 560, height: 440 },
  },
  export: {
    id: "export",
    title: "Export Cabinet",
    description: "Choose columns, package output, and ship the workbook.",
    icon: "E:",
    position: { x: 420, y: 168 },
    size: { width: 480, height: 380 },
  },
};

export const DESKTOP_ICON_ORDER: WindowId[] = [
  "upload",
  "configure",
  "generate",
  "review",
  "export",
];
