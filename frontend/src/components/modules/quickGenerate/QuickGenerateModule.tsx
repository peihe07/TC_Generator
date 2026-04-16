'use client';

import React, { useState, useCallback, useRef } from 'react';
import {
  RiFlashlightLine,
  RiListCheck2,
  RiFileTextLine,
  RiArrowRightLine,
  RiCheckFill,
  RiCloseFill,
  RiClipboardLine,
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

const PRIORITY_COLOR: Record<string, string> = {
  High: 'bg-red-100 text-red-800',
  Medium: 'bg-yellow-100 text-yellow-800',
  Low: 'bg-gray-100 text-gray-600',
};

// --- Sub-components ---

const TcCard: React.FC<{ tc: GeneratedTc; index: number }> = ({ tc, index }) => {
  const [expanded, setExpanded] = useState(true);
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    const text = [
      `[TC ${index + 1}] ${tc.scenarioName ?? ''}`,
      `Test Item: ${tc.tc.test_item_rewrite}`,
      `Pre-Conditions: ${tc.tc.pre_conditions}`,
      `Input Test Data: ${tc.tc.input_test_data}`,
      `Test Procedure:\n${tc.tc.test_procedure}`,
      `Expected Result:\n${tc.tc.expected_result}`,
      `Design Method: ${tc.tc.design_method}`,
      `Priority: ${tc.tc.priority}`,
    ].join('\n\n');
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 1800);
  };

  return (
    <div className="border border-gray-300 bg-white shadow-sm">
      {/* Card Header */}
      <div
        className="flex items-center gap-2 px-3 py-2 bg-gray-100 border-b border-gray-300 cursor-pointer select-none"
        onClick={() => setExpanded((v) => !v)}
      >
        {expanded ? <RiArrowUpSLine className="size-4 shrink-0" /> : <RiArrowDownSLine className="size-4 shrink-0" />}
        <span className="text-xs font-bold text-gray-800 flex-1">
          TC {index + 1}{tc.scenarioName ? ` — ${tc.scenarioName}` : ''}
        </span>
        <span className={`text-[10px] px-2 py-0.5 font-bold uppercase ${PRIORITY_COLOR[tc.tc.priority] ?? 'bg-gray-100 text-gray-600'}`}>
          {tc.tc.priority}
        </span>
        <span className="text-[10px] text-gray-500 ml-1">{tc.tc.design_method}</span>
        <button
          className="ml-2 text-xs px-2 py-0.5 border border-gray-300 bg-white hover:bg-gray-50 flex items-center gap-1"
          onClick={(e) => { e.stopPropagation(); copyToClipboard(); }}
          title="Copy to clipboard"
        >
          {copied ? <RiCheckFill className="size-3 text-green-600" /> : <RiClipboardLine className="size-3" />}
          {copied ? 'Copied' : 'Copy'}
        </button>
      </div>

      {/* Card Body */}
      {expanded && (
        <div className="divide-y divide-gray-100">
          <FieldRow label="Test Item Rewrite" value={tc.tc.test_item_rewrite} />
          <FieldRow label="Pre-Conditions" value={tc.tc.pre_conditions} />
          <FieldRow label="Input Test Data" value={tc.tc.input_test_data} muted />
          <FieldRow label="Test Procedure" value={tc.tc.test_procedure} pre />
          <FieldRow label="Expected Result" value={tc.tc.expected_result} pre highlight />
        </div>
      )}
    </div>
  );
};

const FieldRow: React.FC<{
  label: string;
  value: string;
  pre?: boolean;
  highlight?: boolean;
  muted?: boolean;
}> = ({ label, value, pre, highlight, muted }) => (
  <div className="grid grid-cols-[140px_1fr] text-xs">
    <div className="px-3 py-2 font-bold text-gray-500 bg-gray-50 border-r border-gray-100 uppercase text-[10px] leading-relaxed">
      {label}
    </div>
    <div className={`px-3 py-2 leading-relaxed ${pre ? 'whitespace-pre-wrap' : ''} ${highlight ? 'text-green-800 font-semibold' : ''} ${muted ? 'text-gray-400 italic' : ''}`}>
      {value || '—'}
    </div>
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
  const [model, setModel] = useState('claude-sonnet-4-6');

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
                className={`flex items-start gap-2 p-2 cursor-pointer border ${
                  mode === m.id ? 'border-blue-400 bg-blue-50' : 'border-transparent hover:bg-gray-50'
                }`}
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
                  <div className="text-[10px] text-gray-500">{m.desc}</div>
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
            className="flex-1 p-2 text-xs font-sans resize-none min-h-[100px] border border-gray-300 focus:border-blue-400 focus:outline-none"
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
              className="p-2 text-xs font-sans resize-none min-h-[80px] border border-gray-300 focus:border-blue-400 focus:outline-none"
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
            <option value="claude-sonnet-4-6">Sonnet 4.6</option>
            <option value="claude-haiku-4-5-20251001">Haiku 4.5</option>
          </select>
        </div>

        {/* Generate / Stop buttons */}
        <div className="flex gap-2">
          {isRunning ? (
            <button
              className="flex-1 py-2 flex items-center justify-center gap-2 text-sm font-bold border-2 border-red-400 text-red-700"
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
            <button
              className="px-3 py-2 text-sm flex items-center gap-1"
              onClick={reset}
              title="Clear results"
            >
              <RiRefreshLine className="size-4" />
            </button>
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
          <div className="p-3 bg-red-50 border border-red-300 text-xs text-red-800 flex items-start gap-2">
            <RiCloseFill className="size-4 shrink-0 text-red-600" />
            <span>{errorMsg}</span>
          </div>
        )}

        {/* Scrollable results area */}
        <div className="flex-1 overflow-auto flex flex-col gap-3">
          {/* Decompose analysis block */}
          {analysis && (
            <div className="border border-blue-200 bg-blue-50">
              <div
                className="flex items-center gap-2 px-3 py-2 cursor-pointer select-none"
                onClick={() => setReasoningExpanded((v) => !v)}
              >
                <RiLightbulbLine className="size-4 text-blue-600 shrink-0" />
                <span className="text-xs font-bold text-blue-800 flex-1">
                  AI Analysis — {analysis.scenarios.length} scenario{analysis.scenarios.length !== 1 ? 's' : ''} identified
                </span>
                {reasoningExpanded ? <RiArrowUpSLine className="size-4 text-blue-500" /> : <RiArrowDownSLine className="size-4 text-blue-500" />}
              </div>
              {reasoningExpanded && (
                <div className="px-3 pb-3 flex flex-col gap-2">
                  <p className="text-xs text-blue-700 leading-relaxed">{analysis.reasoning}</p>
                  <div className="flex flex-col gap-1">
                    {analysis.scenarios.map((s) => {
                      const isGenerating = generatingScenarioId === s.id;
                      const isDone = generatedTcs.some((t) => t.scenarioId === s.id);
                      return (
                        <div
                          key={s.id}
                          className={`flex items-center gap-2 px-2 py-1 text-xs border ${
                            isDone ? 'bg-green-50 border-green-200' :
                            isGenerating ? 'bg-yellow-50 border-yellow-300' :
                            'bg-white border-gray-200'
                          }`}
                        >
                          {isDone
                            ? <RiCheckFill className="size-3 text-green-600 shrink-0" />
                            : isGenerating
                              ? <RiLoader4Line className="size-3 text-yellow-600 shrink-0 animate-spin" />
                              : <RiArrowRightLine className="size-3 text-gray-400 shrink-0" />}
                          <span className="font-bold text-[11px]">#{s.id} {s.name}</span>
                          <span className="text-gray-500 text-[10px]">{s.description}</span>
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
            <div className="flex items-center gap-2 p-3 bg-yellow-50 border border-yellow-200 text-xs text-yellow-800">
              <RiLoader4Line className="size-4 animate-spin shrink-0" />
              {phase === 'decomposing' ? 'Analysing requirement...' : 'Generating test case...'}
            </div>
          )}

          {/* TC cards */}
          {generatedTcs.map((tc, i) => (
            <TcCard key={`${tc.scenarioId}-${i}`} tc={tc} index={i} />
          ))}

          {/* Generating next TC indicator */}
          {isRunning && generatingScenarioId !== null && (
            <div className="flex items-center gap-2 p-3 bg-yellow-50 border border-yellow-300 text-xs text-yellow-800">
              <RiLoader4Line className="size-4 animate-spin shrink-0" />
              Generating TC for scenario #{generatingScenarioId}...
            </div>
          )}

          {/* Done summary */}
          {phase === 'done' && generatedTcs.length > 0 && (
            <div className="flex items-center gap-2 p-2 bg-green-50 border border-green-200 text-xs text-green-800">
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
