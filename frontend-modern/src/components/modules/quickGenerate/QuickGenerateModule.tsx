'use client';

import React, { useCallback, useMemo, useRef, useState } from 'react';
import {
  RiCheckFill,
  RiCloseFill,
  RiFlashlightLine,
  RiLoader4Line,
} from '@remixicon/react';
import { useJobHistoryStore } from '../../../store/useJobHistoryStore';
import { DecomposeAnalysisPanel } from './DecomposeAnalysisPanel';
import { QuickGenerateInputPanel } from './QuickGenerateInputPanel';
import { TcList } from './TcCard';
import type {
  DecomposeAnalysis,
  GeneratedTc,
  JobPhase,
} from './types';

/**
 * QuickGenerate orchestrator — owns all state (mode, inputs, streaming
 * phase, analysis, generated TCs) and delegates rendering to focused
 * sub-components. Keeps SSE parsing and history bookkeeping
 * close together so the data flow stays readable.
 */
const QuickGenerateModule: React.FC = () => {
  const [testItem, setTestItem] = useState('');
  const [context, setContext] = useState('');
  const [model, setModel] = useState('gpt-5.4');

  const [phase, setPhase] = useState<JobPhase>('idle');
  const [analysis, setAnalysis] = useState<DecomposeAnalysis | null>(null);
  const [generatedTcs, setGeneratedTcs] = useState<GeneratedTc[]>([]);
  const [generatingScenarioId, setGeneratingScenarioId] = useState<number | null>(null);
  const [cost, setCost] = useState(0);
  const [errorMsg, setErrorMsg] = useState('');
  const [reasoningExpanded, setReasoningExpanded] = useState(true);

  const abortRef = useRef<(() => void) | null>(null);

  const reset = useCallback(() => {
    setPhase('idle');
    setAnalysis(null);
    setGeneratedTcs([]);
    setGeneratingScenarioId(null);
    setCost(0);
    setErrorMsg('');
    setReasoningExpanded(true);
  }, []);

  const handleGenerate = useCallback(async () => {
    if (!testItem.trim()) return;
    reset();
    // 一律先進入 decomposing（AI 正在判斷要拆幾筆），收到 analysis 後才切到 generating。
    setPhase('decomposing');

    let stopped = false;
    const controller = new AbortController();
    const abortCurrent = () => {
      stopped = true;
      controller.abort();
    };
    abortRef.current = abortCurrent;

    // Track latest stats so we can write them into history on job.completed.
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
      const res = await fetch('/api/quick-generate/stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        signal: controller.signal,
        body: JSON.stringify({
          testItem: testItem.trim(),
          context: context.trim() || null,
          model,
        }),
      });

      if (!res.ok || !res.body) throw new Error('Request failed');

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (!stopped) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split('\n\n');
        buffer = parts.pop() ?? '';

        for (const part of parts) {
          const line = part.replace(/^data: /, '').trim();
          if (!line) continue;
          try {
            const event = JSON.parse(line);

            // Mirror stats so history gets an accurate snapshot.
            if (event.stats) {
              if (event.stats.total !== undefined) latest.total = Number(event.stats.total);
              if (event.stats.processed !== undefined) latest.processed = Number(event.stats.processed);
              if (event.stats.currentCost !== undefined) latest.cost = Number(event.stats.currentCost);
              if (event.stats.inputTokens !== undefined) latest.inputTokens = Number(event.stats.inputTokens);
              if (event.stats.outputTokens !== undefined) latest.outputTokens = Number(event.stats.outputTokens);
              if (event.stats.cacheCreationTokens !== undefined)
                latest.cacheCreationTokens = Number(event.stats.cacheCreationTokens);
              if (event.stats.cacheReadTokens !== undefined)
                latest.cacheReadTokens = Number(event.stats.cacheReadTokens);
            }

            if (event.type === 'decompose.analysis') {
              setAnalysis({
                reasoning: event.reasoning,
                scenarios: event.scenarios,
                keywords: event.keywords ?? [],
              });
              setPhase('generating');
            } else if (event.type === 'tc.generating') {
              setGeneratingScenarioId(event.scenarioId);
            } else if (event.type === 'tc.completed') {
              setGeneratedTcs((prev) => [
                ...prev,
                { scenarioId: event.scenarioId, scenarioName: event.scenarioName, tc: event.tc },
              ]);
              setGeneratingScenarioId(null);
              if (event.stats?.currentCost) setCost(event.stats.currentCost);
            } else if (event.type === 'job.completed') {
              if (event.stats?.currentCost) setCost(event.stats.currentCost);
              setPhase('done');
              useJobHistoryStore.getState().appendRecord({
                id: `quick-${Date.now().toString(36)}`,
                kind: 'quick',
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
                note: 'auto-split',
              });
            } else if (event.type === 'job.failed') {
              setErrorMsg(event.message ?? 'Unknown error');
              setPhase('error');
            }
          } catch {
            // Ignore malformed SSE frames — keep reading.
          }
        }
      }
    } catch (err) {
      if (stopped) return;
      setErrorMsg(err instanceof Error ? err.message : 'Backend unavailable');
      setPhase('error');
    } finally {
      if (abortRef.current === abortCurrent) abortRef.current = null;
    }
  }, [testItem, context, model, reset]);

  const handleStop = useCallback(() => {
    abortRef.current?.();
    setPhase('idle');
  }, []);

  const isRunning = phase === 'decomposing' || phase === 'generating';

  // Derived: which scenario ids already have a generated TC.
  const completedScenarioIds = useMemo(
    () => new Set(generatedTcs.map((t) => t.scenarioId)),
    [generatedTcs],
  );

  return (
    <div className="flex h-full gap-3 overflow-hidden p-1">
      {/* Left Panel — Input */}
      <QuickGenerateInputPanel
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

      {/* Right Panel — Results */}
      <div className="flex-1 flex flex-col gap-2 min-w-0 overflow-hidden">
        {/* Idle state */}
        {phase === 'idle' && generatedTcs.length === 0 && (
          <div
            className="flex-1 flex flex-col items-center justify-center gap-3"
            style={{ color: 'var(--text-muted)' }}
          >
            <RiFlashlightLine className="size-12 opacity-30" />
            <div className="text-sm text-center">
              Fill in the input and click Generate
            </div>
          </div>
        )}

        {/* Error */}
        {phase === 'error' && (
          <div
            className="selectable p-2 text-xs flex items-start gap-2 status-bar-field"
            style={{ color: 'var(--status-reject-dark)' }}
          >
            <RiCloseFill className="size-4 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}

        {/* Scrollable results area */}
        <div className="flex-1 overflow-auto flex flex-col gap-2">
          {/* Decompose analysis block */}
          {analysis && (
            <DecomposeAnalysisPanel
              analysis={analysis}
              generatingScenarioId={generatingScenarioId}
              completedScenarioIds={completedScenarioIds}
              expanded={reasoningExpanded}
              onToggleExpanded={() => setReasoningExpanded((v) => !v)}
            />
          )}

          {/* Generating spinner (single / with_context, before any TC arrives) */}
          {isRunning && generatedTcs.length === 0 && !analysis && (
            <div className="flex items-center gap-2 p-2 text-xs status-bar-field">
              <RiLoader4Line className="size-4 animate-spin shrink-0" />
              {phase === 'decomposing' ? 'Analysing requirement...' : 'Generating test case...'}
            </div>
          )}

          {/* TC stacked cards */}
          {generatedTcs.length > 0 && <TcList tcs={generatedTcs} />}

          {/* Generating next TC indicator */}
          {isRunning && generatingScenarioId !== null && (
            <div className="flex items-center gap-2 p-2 text-xs status-bar-field">
              <RiLoader4Line className="size-4 animate-spin shrink-0" />
              Generating TC for scenario #{generatingScenarioId}...
            </div>
          )}

          {/* Done summary */}
          {phase === 'done' && generatedTcs.length > 0 && (
            <div
              className="flex items-center gap-2 p-2 text-xs status-bar-field"
              style={{ color: 'var(--status-accept-dark)' }}
            >
              <RiCheckFill className="size-4 shrink-0" />
              {generatedTcs.length} TC{generatedTcs.length !== 1 ? 's' : ''} generated successfully.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default QuickGenerateModule;
