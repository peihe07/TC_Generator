"use client";

import {
  RiCheckFill,
  RiCloseFill,
  RiFlashlightLine,
  RiLoader4Line,
  RiPlayLine,
  RiRefreshLine,
  RiStopFill,
} from "@remixicon/react";
import { useCallback, useMemo, useRef, useState } from "react";
import { useJobHistoryStore } from "../../store/useJobHistoryStore";
import { buildWorkspaceHeader } from "../../lib/workspaceHeader";
import { useWorkspaceStore } from "../../store/useWorkspaceStore";

type JobPhase = "idle" | "decomposing" | "generating" | "done" | "error";

interface Scenario {
  id: number;
  name: string;
  description: string;
  test_item: string;
}

interface Keyword {
  keyword: string;
  meaning: string;
  scenarios: number[];
}

interface DecomposeAnalysis {
  reasoning: string;
  scenarios: Scenario[];
  keywords: Keyword[];
}

interface GeneratedTc {
  scenarioId: number;
  scenarioName?: string;
  tc: {
    tc_title: string;
    pre_conditions: string;
    input_test_data: string;
    test_procedure: string;
    expected_result: string;
    design_method: string;
    priority: string;
  };
}

const MODEL_OPTIONS = [
  { value: "gpt-5.4", label: "GPT-5.4" },
  { value: "gpt-5", label: "GPT-5" },
];

export default function QuickGenerateView() {
  const [testItem, setTestItem] = useState("");
  const [context, setContext] = useState("");
  const [model, setModel] = useState("gpt-5.4");

  const [phase, setPhase] = useState<JobPhase>("idle");
  const [analysis, setAnalysis] = useState<DecomposeAnalysis | null>(null);
  const [generatedTcs, setGeneratedTcs] = useState<GeneratedTc[]>([]);
  const [generatingScenarioId, setGeneratingScenarioId] = useState<
    number | null
  >(null);
  const [cost, setCost] = useState(0);
  const [errorMsg, setErrorMsg] = useState("");

  const abortRef = useRef<(() => void) | null>(null);
  const currentWorkspaceId = useWorkspaceStore((s) => s.currentId);

  const reset = useCallback(() => {
    setPhase("idle");
    setAnalysis(null);
    setGeneratedTcs([]);
    setGeneratingScenarioId(null);
    setCost(0);
    setErrorMsg("");
  }, []);

  const handleGenerate = useCallback(async () => {
    if (!testItem.trim()) return;
    reset();
    setPhase("decomposing");

    let stopped = false;
    const controller = new AbortController();
    const abortCurrent = () => {
      stopped = true;
      controller.abort();
    };
    abortRef.current = abortCurrent;

    const startedAt = Date.now();
    const latest = {
      total: 0,
      processed: 0,
      cost: 0,
      inputTokens: 0,
      outputTokens: 0,
      cacheCreationTokens: 0,
      cacheReadTokens: 0,
    };

    try {
      const res = await fetch("/api/quick-generate/stream", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...buildWorkspaceHeader(),
        },
        signal: controller.signal,
        body: JSON.stringify({
          testItem: testItem.trim(),
          context: context.trim() || null,
          model,
        }),
      });

      if (!res.ok || !res.body) throw new Error("Request failed");

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (!stopped) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split("\n\n");
        buffer = parts.pop() ?? "";

        for (const part of parts) {
          const line = part.replace(/^data: /, "").trim();
          if (!line) continue;
          try {
            const event = JSON.parse(line);

            if (event.stats) {
              if (event.stats.total !== undefined)
                latest.total = Number(event.stats.total);
              if (event.stats.processed !== undefined)
                latest.processed = Number(event.stats.processed);
              if (event.stats.currentCost !== undefined)
                latest.cost = Number(event.stats.currentCost);
              if (event.stats.inputTokens !== undefined)
                latest.inputTokens = Number(event.stats.inputTokens);
              if (event.stats.outputTokens !== undefined)
                latest.outputTokens = Number(event.stats.outputTokens);
              if (event.stats.cacheCreationTokens !== undefined)
                latest.cacheCreationTokens = Number(
                  event.stats.cacheCreationTokens
                );
              if (event.stats.cacheReadTokens !== undefined)
                latest.cacheReadTokens = Number(event.stats.cacheReadTokens);
            }

            if (event.type === "decompose.analysis") {
              setAnalysis({
                reasoning: event.reasoning,
                scenarios: event.scenarios,
                keywords: event.keywords ?? [],
              });
              setPhase("generating");
            } else if (event.type === "tc.generating") {
              setGeneratingScenarioId(event.scenarioId);
            } else if (event.type === "tc.completed") {
              setGeneratedTcs((prev) => [
                ...prev,
                {
                  scenarioId: event.scenarioId,
                  scenarioName: event.scenarioName,
                  tc: event.tc,
                },
              ]);
              setGeneratingScenarioId(null);
              if (event.stats?.currentCost) setCost(event.stats.currentCost);
            } else if (event.type === "job.completed") {
              if (event.stats?.currentCost) setCost(event.stats.currentCost);
              setPhase("done");
              useJobHistoryStore.getState().appendRecord({
                id: `quick-${Date.now().toString(36)}`,
                kind: "quick",
                model,
                startedAt,
                finishedAt: Date.now(),
                rowsTotal: Math.max(latest.total, 1),
                rowsProcessed: Math.max(latest.processed, 1),
                cost: latest.cost,
                inputTokens: latest.inputTokens,
                outputTokens: latest.outputTokens,
                cacheReadTokens: latest.cacheReadTokens,
                cacheCreationTokens: latest.cacheCreationTokens,
                note: "auto-split",
                workspaceId: currentWorkspaceId,
              });
            } else if (event.type === "job.failed") {
              setErrorMsg(event.message ?? "Unknown error");
              setPhase("error");
            }
          } catch {
            // Ignore malformed SSE frames — keep reading.
          }
        }
      }
    } catch (err) {
      if (stopped) return;
      setErrorMsg(err instanceof Error ? err.message : "Backend unavailable");
      setPhase("error");
    } finally {
      if (abortRef.current === abortCurrent) abortRef.current = null;
    }
  }, [testItem, context, model, reset, currentWorkspaceId]);

  const handleStop = useCallback(() => {
    abortRef.current?.();
    setPhase("idle");
  }, []);

  const isRunning = phase === "decomposing" || phase === "generating";

  const completedScenarioIds = useMemo(
    () => new Set(generatedTcs.map((t) => t.scenarioId)),
    [generatedTcs]
  );

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Quick TC</h1>
        <p className="text-secondary text-sm">
          One-shot generation from free-form requirement text — AI auto-splits
          into scenarios and emits TCs as they finish.
        </p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-[360px_1fr] gap-4">
        <InputPanel
          testItem={testItem}
          context={context}
          model={model}
          phase={phase}
          cost={cost}
          onTestItemChange={setTestItem}
          onContextChange={setContext}
          onModelChange={setModel}
          onGenerate={handleGenerate}
          onStop={handleStop}
          onReset={reset}
        />

        <ResultsPanel
          phase={phase}
          analysis={analysis}
          generatedTcs={generatedTcs}
          generatingScenarioId={generatingScenarioId}
          completedScenarioIds={completedScenarioIds}
          errorMsg={errorMsg}
          isRunning={isRunning}
        />
      </div>
    </div>
  );
}

function InputPanel({
  testItem,
  context,
  model,
  phase,
  cost,
  onTestItemChange,
  onContextChange,
  onModelChange,
  onGenerate,
  onStop,
  onReset,
}: {
  testItem: string;
  context: string;
  model: string;
  phase: JobPhase;
  cost: number;
  onTestItemChange: (v: string) => void;
  onContextChange: (v: string) => void;
  onModelChange: (v: string) => void;
  onGenerate: () => void;
  onStop: () => void;
  onReset: () => void;
}) {
  const isRunning = phase === "decomposing" || phase === "generating";
  const canGenerate = testItem.trim().length > 0 && !isRunning;

  return (
    <aside className="surface p-5 space-y-4 self-start">
      <div className="space-y-1.5">
        <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
          Requirement
        </label>
        <textarea
          className="w-full text-sm p-3 rounded-md focus-ring"
          placeholder="貼上完整的 requirement 文字…"
          value={testItem}
          rows={8}
          onChange={(e) => onTestItemChange(e.target.value)}
          style={{
            backgroundColor: "rgba(0, 21, 36, 0.04)",
            color: "var(--color-ink)",
            resize: "vertical",
            minHeight: 120,
          }}
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
          Context (optional)
        </label>
        <textarea
          className="w-full text-sm p-3 rounded-md focus-ring"
          placeholder="背景說明、相關 spec 段落…"
          value={context}
          rows={4}
          onChange={(e) => onContextChange(e.target.value)}
          style={{
            backgroundColor: "rgba(0, 21, 36, 0.04)",
            color: "var(--color-ink)",
            resize: "vertical",
            minHeight: 80,
          }}
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
          Model
        </label>
        <select
          className="w-full text-sm p-2 rounded-md focus-ring"
          value={model}
          onChange={(e) => onModelChange(e.target.value)}
          style={{
            backgroundColor: "rgba(0, 21, 36, 0.04)",
            color: "var(--color-ink)",
          }}
        >
          {MODEL_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>

      <div className="flex items-center gap-2 flex-wrap">
        {!isRunning ? (
          <button
            type="button"
            onClick={onGenerate}
            disabled={!canGenerate}
            className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-40"
          >
            <RiPlayLine size={14} />
            Generate
          </button>
        ) : (
          <button
            type="button"
            onClick={onStop}
            className="inline-flex items-center gap-1.5 text-sm px-3 py-2 rounded-md font-bold focus-ring"
            style={{
              backgroundColor: "rgba(120, 41, 15, 0.12)",
              color: "var(--color-brandy)",
            }}
          >
            <RiStopFill size={14} />
            Stop
          </button>
        )}
        <button
          type="button"
          onClick={onReset}
          disabled={isRunning}
          className="inline-flex items-center gap-1.5 text-sm px-3 py-2 rounded-md focus-ring disabled:opacity-40"
          style={{
            backgroundColor: "rgba(21, 97, 109, 0.08)",
            color: "var(--color-teal)",
          }}
        >
          <RiRefreshLine size={14} />
          Reset
        </button>
      </div>

      {cost > 0 && (
        <div className="text-xs text-muted">
          Cost so far: <strong className="text-primary">${cost.toFixed(4)}</strong>
        </div>
      )}
    </aside>
  );
}

function ResultsPanel({
  phase,
  analysis,
  generatedTcs,
  generatingScenarioId,
  completedScenarioIds,
  errorMsg,
  isRunning,
}: {
  phase: JobPhase;
  analysis: DecomposeAnalysis | null;
  generatedTcs: GeneratedTc[];
  generatingScenarioId: number | null;
  completedScenarioIds: Set<number>;
  errorMsg: string;
  isRunning: boolean;
}) {
  const showIdle = phase === "idle" && generatedTcs.length === 0;

  return (
    <section className="space-y-3 min-w-0">
      {showIdle && (
        <div
          className="surface p-12 flex flex-col items-center justify-center gap-3 text-secondary"
          style={{ minHeight: 320 }}
        >
          <RiFlashlightLine size={48} className="opacity-40" />
          <div className="text-sm">Fill in the input and click Generate.</div>
        </div>
      )}

      {phase === "error" && (
        <div
          className="text-sm px-4 py-3 rounded-md flex items-start gap-2"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          <RiCloseFill size={16} className="shrink-0 mt-0.5" />
          <span>{errorMsg}</span>
        </div>
      )}

      {analysis && (
        <DecomposePanel
          analysis={analysis}
          generatingScenarioId={generatingScenarioId}
          completedScenarioIds={completedScenarioIds}
        />
      )}

      {isRunning && generatedTcs.length === 0 && !analysis && (
        <div className="surface p-4 flex items-center gap-2 text-sm text-secondary">
          <RiLoader4Line size={16} className="animate-spin shrink-0" />
          {phase === "decomposing"
            ? "Analysing requirement…"
            : "Generating test case…"}
        </div>
      )}

      {generatedTcs.map((row) => (
        <TcCard
          key={`${row.scenarioId}-${row.tc.tc_title}`}
          tc={row}
        />
      ))}

      {isRunning && generatingScenarioId !== null && (
        <div className="surface p-3 flex items-center gap-2 text-xs text-secondary">
          <RiLoader4Line size={14} className="animate-spin shrink-0" />
          Generating TC for scenario #{generatingScenarioId}…
        </div>
      )}

      {phase === "done" && generatedTcs.length > 0 && (
        <div
          className="text-sm px-4 py-3 rounded-md flex items-center gap-2"
          style={{
            color: "var(--color-teal)",
            backgroundColor: "rgba(21, 97, 109, 0.10)",
          }}
        >
          <RiCheckFill size={16} className="shrink-0" />
          {generatedTcs.length} TC{generatedTcs.length !== 1 ? "s" : ""}{" "}
          generated. Saved to Runs history.
        </div>
      )}
    </section>
  );
}

function DecomposePanel({
  analysis,
  generatingScenarioId,
  completedScenarioIds,
}: {
  analysis: DecomposeAnalysis;
  generatingScenarioId: number | null;
  completedScenarioIds: Set<number>;
}) {
  return (
    <div className="surface p-5 space-y-3">
      <div className="space-y-1">
        <h2 className="text-sm font-bold uppercase tracking-wider text-primary">
          Decompose Analysis
        </h2>
        <p className="text-xs text-secondary whitespace-pre-wrap">
          {analysis.reasoning}
        </p>
      </div>

      <div className="space-y-1.5">
        <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
          Scenarios ({analysis.scenarios.length})
        </div>
        <ul className="space-y-1.5">
          {analysis.scenarios.map((s) => {
            const isDone = completedScenarioIds.has(s.id);
            const isGen = generatingScenarioId === s.id;
            return (
              <li
                key={s.id}
                className="flex items-start gap-2 text-xs"
                style={{
                  color: isDone ? "var(--color-teal)" : "var(--color-ink)",
                }}
              >
                <span className="shrink-0 mt-0.5">
                  {isDone ? (
                    <RiCheckFill size={14} />
                  ) : isGen ? (
                    <RiLoader4Line size={14} className="animate-spin" />
                  ) : (
                    <span className="inline-block w-3.5 h-3.5 rounded-full border border-current opacity-40" />
                  )}
                </span>
                <span>
                  <strong>#{s.id}</strong> {s.name} — {s.description}
                </span>
              </li>
            );
          })}
        </ul>
      </div>

      {analysis.keywords.length > 0 && (
        <div className="space-y-1.5">
          <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
            Keywords
          </div>
          <ul className="flex flex-wrap gap-1.5">
            {analysis.keywords.map((k) => (
              <li
                key={k.keyword}
                className="text-[10px] px-2 py-0.5 rounded font-bold"
                style={{
                  color: "var(--color-tangerine)",
                  backgroundColor: "rgba(255, 125, 0, 0.10)",
                }}
                title={k.meaning}
              >
                {k.keyword}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

function TcCard({ tc }: { tc: GeneratedTc }) {
  return (
    <article className="surface p-5 space-y-2">
      <header className="flex items-start justify-between gap-3 flex-wrap">
        <div className="space-y-0.5">
          <h3 className="text-base font-bold text-primary">
            {tc.tc.tc_title}
          </h3>
          {tc.scenarioName && (
            <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
              Scenario #{tc.scenarioId} · {tc.scenarioName}
            </div>
          )}
        </div>
        <div className="flex items-center gap-2 text-[10px] uppercase tracking-wider font-bold">
          <span
            className="px-2 py-0.5 rounded"
            style={{
              color: "var(--color-teal)",
              backgroundColor: "rgba(21, 97, 109, 0.12)",
            }}
          >
            {tc.tc.priority}
          </span>
          <span className="text-muted">{tc.tc.design_method}</span>
        </div>
      </header>

      <Field label="Pre-Conditions" value={tc.tc.pre_conditions} />
      <Field label="Input Test Data" value={tc.tc.input_test_data} />
      <Field label="Test Procedure" value={tc.tc.test_procedure} />
      <Field label="Expected Result" value={tc.tc.expected_result} />
    </article>
  );
}

function Field({ label, value }: { label: string; value: string }) {
  return (
    <div className="space-y-0.5">
      <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
        {label}
      </div>
      <pre
        className="text-xs whitespace-pre-wrap text-primary"
        style={{ fontFamily: "inherit" }}
      >
        {value || "—"}
      </pre>
    </div>
  );
}
