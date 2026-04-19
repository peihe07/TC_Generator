'use client';

import React, { useState, useCallback, useRef } from 'react';
import { useJobHistoryStore } from '../../../store/useJobHistoryStore';
import {
  RiFlashlightLine,
  RiListCheck2,
  RiFileTextLine,
  RiArrowRightLine,
  RiCheckFill,
  RiCloseFill,
  RiRefreshLine,
  RiLightbulbLine,
  RiArrowDownSLine,
  RiArrowUpSLine,
  RiLoader4Line,
} from '@remixicon/react';

// --- Types ---
type Mode = 'single' | 'with_context' | 'decompose';

interface GeneratedTc {
  scenarioId: number;
  scenarioName?: string;
  tc: {
    test_item_rewrite: string;
    pre_conditions: string;
    input_test_data: string;
    test_procedure: string;
    expected_result: string;
    design_method: string;
    priority: string;
  };
}

interface Scenario {
  id: number;
  name: string;
  description: string;
  test_item: string;
}

interface DecomposeAnalysis {
  reasoning: string;
  scenarios: Scenario[];
}

type JobPhase = 'idle' | 'decomposing' | 'generating' | 'done' | 'error';

const MODE_CONFIG: { id: Mode; label: string; icon: React.ReactNode; desc: string }[] = [
  {
    id: 'single',
    label: 'Single TC',
    icon: <RiFlashlightLine className="size-4" />,
    desc: 'One test item → one TC',
  },
  {
    id: 'with_context',
    label: 'With Context',
    icon: <RiFileTextLine className="size-4" />,
    desc: 'Test item + additional criteria or context',
  },
  {
    id: 'decompose',
    label: 'Decompose',
    icon: <RiListCheck2 className="size-4" />,
    desc: 'Full requirement → AI splits into multiple TCs',
  },
];

// 與 .status-badge 的 Win95 系統色風格一致（飽和 + sunken inset）
const PRIORITY_STYLE: Record<string, React.CSSProperties> = {
  High:   { background: '#c00000', color: '#ffffff' },
  Medium: { background: '#e0a000', color: '#000000' },
  Low:    { background: '#909090', color: '#ffffff' },
};
const PRIORITY_BASE: React.CSSProperties = {
  border: '2px solid',
  borderColor: '#606060 #f0f0f0 #f0f0f0 #606060',
  boxShadow: 'inset 1px 1px 0 rgba(0,0,0,0.25)',
  fontWeight: 'bold',
  padding: '1px 6px',
  fontSize: 10,
  letterSpacing: 0.5,
  textTransform: 'uppercase',
};

// --- Sub-components ---

const COLUMN_HEADERS: { key: keyof GeneratedTc['tc']; label: string; muted?: boolean }[] = [
  { key: 'test_item_rewrite', label: 'Test Item' },
  { key: 'pre_conditions', label: 'Pre-Conditions' },
  { key: 'input_test_data', label: 'Input Test Data', muted: true },
  { key: 'test_procedure', label: 'Test Procedure' },
  { key: 'expected_result', label: 'Expected Result' },
];

const TcCard: React.FC<{ tc: GeneratedTc; index: number }> = ({ tc, index }) => {
  const priorityColor = PRIORITY_STYLE[tc.tc.priority] ?? { background: '#909090', color: '#ffffff' };
  return (
    <div className="flex flex-col">
      <div className="title-bar-mini">
        <RiFlashlightLine className="size-3" />
        <span className="flex-1">
          TC {index + 1}{tc.scenarioName ? ` — ${tc.scenarioName}` : ''}
        </span>
        <span style={{ ...PRIORITY_BASE, ...priorityColor }}>{tc.tc.priority}</span>
        <span className="text-[10px] opacity-75 ml-2">{tc.tc.design_method}</span>
      </div>
      <div className="paper-card">
        <div className="flex flex-col">
          {COLUMN_HEADERS.map((c) => {
            const raw = tc.tc[c.key] as string;
            return (
              <div key={c.key} style={{ borderTop: '1px solid var(--win95-gray-lighter)' }}>
                <div
                  className="px-2 py-1 font-bold uppercase"
                  style={{
                    background: '#e8e8e8',
                    borderBottom: '1px solid #d0d0d0',
                    fontSize: 10,
                    color: 'var(--text-muted)',
                    letterSpacing: 0.5,
                  }}
                >
                  {c.label}
                </div>
                <div
                  className="selectable px-3 py-2 text-xs whitespace-pre-wrap"
                  style={{
                    color: c.muted ? 'var(--win95-gray-mid)' : 'var(--win95-black)',
                    fontStyle: c.muted ? 'italic' : 'normal',
                    wordBreak: 'break-word',
                    lineHeight: 1.5,
                  }}
                >
                  {raw || '—'}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

const TcList: React.FC<{ tcs: GeneratedTc[] }> = ({ tcs }) => (
  <div className="flex flex-col gap-3">
    {tcs.map((tc, i) => (
      <TcCard key={`${tc.scenarioId}-${i}`} tc={tc} index={i} />
    ))}
  </div>
);

// --- Mock TC builder (used when backend is unavailable) ---
function buildMockTc(scenarioId: number, scenarioName: string | undefined, testItem: string): GeneratedTc {
  return {
    scenarioId,
    scenarioName,
    tc: {
      test_item_rewrite: `(${testItem}) → Expected observable outcome is verified.`,
      pre_conditions: '1. System is in the required initial state.\n2. All prerequisite conditions are satisfied.',
      input_test_data: 'NA',
      test_procedure:
        '1. Prepare the required initial state.\n2. Execute the target operation.\n3. Verify the observable result matches the expected outcome.',
      expected_result:
        '1. Initial state preparation succeeds.\n2. Target operation is accepted by the system.\n3. Observable result matches the stated requirement.',
      design_method: 'Scenario',
      priority: 'Medium',
    },
  };
}

// --- Main Module ---
const QuickGenerateModule: React.FC = () => {
  const [mode, setMode] = useState<Mode>('single');
  const [testItem, setTestItem] = useState('');
  const [context, setContext] = useState('');
  const [model, setModel] = useState('gpt-4.1');

  const [phase, setPhase] = useState<JobPhase>('idle');
  const [analysis, setAnalysis] = useState<DecomposeAnalysis | null>(null);
  const [generatedTcs, setGeneratedTcs] = useState<GeneratedTc[]>([]);
  const [generatingScenarioId, setGeneratingScenarioId] = useState<number | null>(null);
  const [cost, setCost] = useState(0);
  const [errorMsg, setErrorMsg] = useState('');
  const [reasoningExpanded, setReasoningExpanded] = useState(true);

  const abortRef = useRef<(() => void) | null>(null);

  const reset = () => {
    setPhase('idle');
    setAnalysis(null);
    setGeneratedTcs([]);
    setGeneratingScenarioId(null);
    setCost(0);
    setErrorMsg('');
    setReasoningExpanded(true);
  };

  // --- Mock fallback (used when backend is unavailable) ---
  const runMock = useCallback(async (stopped: () => boolean) => {
    const item = testItem.trim();
    const delay = (ms: number) => new Promise((r) => setTimeout(r, ms));

    if (mode === 'decompose') {
      await delay(900);
      if (stopped()) return;
      const mockScenarios: Scenario[] = [
        { id: 1, name: 'Normal flow', description: 'Verify the primary success path.', test_item: `${item} — happy path` },
        { id: 2, name: 'Boundary condition', description: 'Test edge-case inputs or state limits.', test_item: `${item} — boundary` },
        { id: 3, name: 'Error handling', description: 'Confirm graceful failure on invalid input.', test_item: `${item} — error case` },
      ];
      setAnalysis({
        reasoning: '[Mock] Identified 3 distinct test scenarios: the primary success path, a boundary condition, and an error-handling case. Each represents an independent observable behaviour.',
        scenarios: mockScenarios,
      });
      setPhase('generating');

      for (const s of mockScenarios) {
        if (stopped()) return;
        setGeneratingScenarioId(s.id);
        await delay(700);
        if (stopped()) return;
        setGeneratedTcs((prev) => [...prev, buildMockTc(s.id, s.name, s.test_item)]);
        setGeneratingScenarioId(null);
      }
    } else {
      await delay(800);
      if (stopped()) return;
      setGeneratedTcs([buildMockTc(1, undefined, item)]);
    }

    setPhase('done');
  }, [testItem, mode]);

  const handleGenerate = useCallback(async () => {
    if (!testItem.trim()) return;
    reset();
    setPhase(mode === 'decompose' ? 'decomposing' : 'generating');

    let stopped = false;
    abortRef.current = () => { stopped = true; };
    const isStopped = () => stopped;

    // 追蹤最新 stats，在 job.completed 時寫入 history
    const startedAt = Date.now();
    const latest = {
      total: 0, processed: 0, cost: 0,
      inputTokens: 0, outputTokens: 0,
      cacheCreationTokens: 0, cacheReadTokens: 0,
    };

    try {
      const res = await fetch('/api/quick-generate/stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          testItem: testItem.trim(),
          context: context.trim() || null,
          mode,
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

            // 同步擷取 stats 供 history 使用
            if (event.stats) {
              if (event.stats.total !== undefined) latest.total = Number(event.stats.total);
              if (event.stats.processed !== undefined) latest.processed = Number(event.stats.processed);
              if (event.stats.currentCost !== undefined) latest.cost = Number(event.stats.currentCost);
              if (event.stats.inputTokens !== undefined) latest.inputTokens = Number(event.stats.inputTokens);
              if (event.stats.outputTokens !== undefined) latest.outputTokens = Number(event.stats.outputTokens);
              if (event.stats.cacheCreationTokens !== undefined) latest.cacheCreationTokens = Number(event.stats.cacheCreationTokens);
              if (event.stats.cacheReadTokens !== undefined) latest.cacheReadTokens = Number(event.stats.cacheReadTokens);
            }

            if (event.type === 'decompose.analysis') {
              setAnalysis({ reasoning: event.reasoning, scenarios: event.scenarios });
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
              // 寫入 history
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
                note: mode,
              });
            } else if (event.type === 'job.failed') {
              setErrorMsg(event.message ?? 'Unknown error');
              setPhase('error');
            }
          } catch {
            // ignore parse errors
          }
        }
      }
    } catch {
      // Backend unavailable — run local mock
      await runMock(isStopped);
    }
  }, [testItem, context, mode, model, runMock]);

  const isRunning = phase === 'decomposing' || phase === 'generating';

  return (
    <div className="flex h-full gap-3 overflow-hidden p-1">
      {/* Left Panel — Input */}
      <div className="w-[320px] flex flex-col gap-2 shrink-0">
        {/* Mode selector */}
        <fieldset>
          <legend className="font-bold text-sm">Mode</legend>
          <div className="flex flex-col gap-1 p-1">
            {MODE_CONFIG.map((m) => (
              <label
                key={m.id}
                className="flex items-start gap-2 p-1 cursor-pointer"
                style={mode === m.id ? { background: '#000080', color: '#ffffff' } : {}}
              >
                <input
                  type="radio"
                  name="mode"
                  value={m.id}
                  checked={mode === m.id}
                  onChange={() => { setMode(m.id); reset(); }}
                  className="mt-0.5"
                />
                <div>
                  <div className="flex items-center gap-1 text-xs font-bold">
                    {m.icon} {m.label}
                  </div>
                  <div className="text-[10px]" style={{ color: mode === m.id ? 'rgba(255,255,255,0.7)' : 'var(--win95-gray-mid)' }}>{m.desc}</div>
                </div>
              </label>
            ))}
          </div>
        </fieldset>

        {/* Test Item input */}
        <fieldset className="flex-1 flex flex-col overflow-hidden">
          <legend className="font-bold text-sm">
            {mode === 'decompose' ? 'Requirement Description' : 'Test Item'}
          </legend>
          <textarea
            className="flex-1 p-2 text-xs resize-none min-h-[100px] border-2 border-sunken"
            placeholder={
              mode === 'decompose'
                ? 'Paste full requirement text. AI will identify distinct test scenarios...'
                : 'Enter the test item or condition to generate a TC for...'
            }
            value={testItem}
            onChange={(e) => setTestItem(e.target.value)}
            disabled={isRunning}
          />
        </fieldset>

        {/* Context input (only for with_context) */}
        {mode === 'with_context' && (
          <fieldset className="flex flex-col">
            <legend className="font-bold text-sm">Additional Criteria / Context</legend>
            <textarea
              className="p-2 text-xs resize-none min-h-[80px] border-2 border-sunken"
              placeholder="System constraints, related requirements, environment details..."
              value={context}
              onChange={(e) => setContext(e.target.value)}
              disabled={isRunning}
            />
          </fieldset>
        )}

        {/* Model selector */}
        <div className="field-row">
          <label className="text-xs font-bold">Model:</label>
          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            disabled={isRunning}
          >
            <option value="gpt-5">GPT-5</option>
            <option value="gpt-4.1">GPT-4.1</option>
            <option value="gpt-4.1-mini">GPT-4.1 mini</option>
            <option value="gpt-4o-mini">GPT-4o mini</option>
          </select>
        </div>

        {/* Generate / Stop buttons */}
        <div className="flex gap-2">
          {isRunning ? (
            <button
              className="flex-1 flex items-center justify-center gap-2 font-bold"
              onClick={() => { abortRef.current?.(); setPhase('idle'); }}
            >
              <RiCloseFill className="size-4" /> Stop
            </button>
          ) : (
            <button
              className="flex-1 py-2 flex items-center justify-center gap-2 text-sm font-bold default"
              disabled={!testItem.trim()}
              onClick={handleGenerate}
            >
              <RiArrowRightLine className="size-4" />
              {mode === 'decompose' ? 'Analyse & Generate' : 'Generate TC'}
            </button>
          )}
          {(phase === 'done' || phase === 'error') && (
            <>
              <button
                className="px-3 py-2 text-sm flex items-center gap-1 font-bold"
                onClick={handleGenerate}
                disabled={!testItem.trim()}
                title="Regenerate with same input"
              >
                <RiRefreshLine className="size-4" /> Regenerate
              </button>
              <button
                className="px-3 py-2 text-sm flex items-center gap-1"
                onClick={reset}
                title="Clear results"
              >
                <RiCloseFill className="size-4" />
              </button>
            </>
          )}
        </div>

        {/* Cost display */}
        {cost > 0 && (
          <div className="text-[10px] text-gray-500 text-right font-mono">
            Cost: ${cost.toFixed(4)}
          </div>
        )}
      </div>

      {/* Right Panel — Results */}
      <div className="flex-1 flex flex-col gap-2 min-w-0 overflow-hidden">
        {/* Idle state */}
        {phase === 'idle' && generatedTcs.length === 0 && (
          <div className="flex-1 flex flex-col items-center justify-center text-gray-400 gap-3">
            <RiFlashlightLine className="size-12 opacity-30" />
            <div className="text-sm text-center">
              Fill in the input and click Generate
            </div>
          </div>
        )}

        {/* Error */}
        {phase === 'error' && (
          <div className="selectable p-2 text-xs flex items-start gap-2 status-bar-field" style={{ color: 'var(--status-reject-dark)' }}>
            <RiCloseFill className="size-4 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}

        {/* Scrollable results area */}
        <div className="flex-1 overflow-auto flex flex-col gap-2">
          {/* Decompose analysis block */}
          {analysis && (
            <div style={{ border: '2px solid', borderColor: 'var(--win95-gray-mid) var(--win95-white) var(--win95-white) var(--win95-gray-mid)' }}>
              <div
                className="flex items-center gap-2 px-2 py-1 cursor-pointer select-none"
                style={{ background: 'var(--win95-navy)', color: 'var(--win95-white)' }}
                onClick={() => setReasoningExpanded((v) => !v)}
              >
                <RiLightbulbLine className="size-3 shrink-0" />
                <span className="text-xs font-bold flex-1">
                  AI Analysis — {analysis.scenarios.length} scenario{analysis.scenarios.length !== 1 ? 's' : ''} identified
                </span>
                {reasoningExpanded ? <RiArrowUpSLine className="size-3" /> : <RiArrowDownSLine className="size-3" />}
              </div>
              {reasoningExpanded && (
                <div className="p-2 flex flex-col gap-1" style={{ background: 'var(--win95-white)' }}>
                  <p className="text-xs leading-relaxed" style={{ color: 'var(--text-muted)' }}>{analysis.reasoning}</p>
                  <div className="flex flex-col gap-1 mt-1">
                    {analysis.scenarios.map((s) => {
                      const isGenerating = generatingScenarioId === s.id;
                      const isDone = generatedTcs.some((t) => t.scenarioId === s.id);
                      return (
                        <div
                          key={s.id}
                          className="flex items-center gap-2 px-2 py-1 text-xs"
                          style={{
                            background: isDone ? '#d4edda' : isGenerating ? '#fff3cd' : '#f0f0f0',
                            border: '1px solid var(--win95-gray)',
                          }}
                        >
                          {isDone
                            ? <RiCheckFill className="size-3 shrink-0" style={{ color: 'var(--status-accept-dark)' }} />
                            : isGenerating
                              ? <RiLoader4Line className="size-3 shrink-0 animate-spin" />
                              : <RiArrowRightLine className="size-3 shrink-0" style={{ color: 'var(--win95-gray-mid)' }} />}
                          <span className="font-bold text-[11px]">#{s.id} {s.name}</span>
                          <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>{s.description}</span>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Generating spinner (single/with_context) */}
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
            <div className="flex items-center gap-2 p-2 text-xs status-bar-field" style={{ color: 'var(--status-accept-dark)' }}>
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
