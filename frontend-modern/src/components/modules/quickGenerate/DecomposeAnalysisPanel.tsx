import React from 'react';
import {
  RiArrowDownSLine,
  RiArrowRightLine,
  RiArrowUpSLine,
  RiCheckFill,
  RiKey2Line,
  RiLightbulbLine,
  RiLoader4Line,
} from '@remixicon/react';
import type { DecomposeAnalysis } from './types';

export interface DecomposeAnalysisPanelProps {
  analysis: DecomposeAnalysis;
  /** Scenario id currently being generated, if any. */
  generatingScenarioId: number | null;
  /** Scenario ids already completed. */
  completedScenarioIds: Set<number>;
  expanded: boolean;
  onToggleExpanded: () => void;
}

/**
 * AI interpretation panel. Displays how the AI understands the requirement —
 * reasoning (驗證目標 / 關鍵概念 / 拆分判斷), keyword breakdown, and the
 * scenarios that emerge. Shown for every multi-TC job; when the AI decides
 * the requirement is atomic (single scenario), the scenario strip collapses
 * to a short "no split needed" note so the panel still carries value as a
 * sanity check on the AI's interpretation rather than reading as a hollow
 * "1 scenario identified" report.
 */
export const DecomposeAnalysisPanel: React.FC<DecomposeAnalysisPanelProps> = ({
  analysis,
  generatingScenarioId,
  completedScenarioIds,
  expanded,
  onToggleExpanded,
}) => {
  const isAtomic = analysis.scenarios.length <= 1;
  const headerLabel = isAtomic
    ? 'AI 的需求解讀（原子需求，不需拆分）'
    : `AI 的需求解讀 — 拆成 ${analysis.scenarios.length} 個情境`;
  return (
  <div className="border-sunken">
    <div
      className="flex items-center gap-2 px-2 py-1 cursor-pointer select-none"
      style={{ background: 'var(--win95-navy)', color: 'var(--win95-white)' }}
      onClick={onToggleExpanded}
    >
      <RiLightbulbLine className="size-3 shrink-0" />
      <span className="text-xs font-bold flex-1">{headerLabel}</span>
      {expanded ? (
        <RiArrowUpSLine className="size-3" />
      ) : (
        <RiArrowDownSLine className="size-3" />
      )}
    </div>

    {expanded && (
      <div
        className="p-2 flex flex-col gap-1"
        style={{ background: 'var(--win95-white)' }}
      >
        <p
          className="text-xs leading-relaxed"
          style={{ color: 'var(--text-muted)' }}
        >
          {analysis.reasoning}
        </p>

        {analysis.keywords.length > 0 && (
          <div className="mt-2">
            <div
              className="flex items-center gap-1 mb-1 text-[11px] font-bold"
              style={{ color: 'var(--win95-navy)' }}
            >
              <RiKey2Line className="size-3 shrink-0" />
              Keyword Breakdown
            </div>
            <table
              className="w-full text-[10px] border-collapse"
              style={{ border: '1px solid var(--win95-gray)' }}
            >
              <thead>
                <tr style={{ background: 'var(--win95-gray-lighter)' }}>
                  <th
                    className="text-left px-1 py-0.5 font-bold"
                    style={{ border: '1px solid var(--win95-gray)' }}
                  >
                    Keyword
                  </th>
                  <th
                    className="text-left px-1 py-0.5 font-bold"
                    style={{ border: '1px solid var(--win95-gray)' }}
                  >
                    Meaning
                  </th>
                  <th
                    className="text-left px-1 py-0.5 font-bold w-16"
                    style={{ border: '1px solid var(--win95-gray)' }}
                  >
                    Scenarios
                  </th>
                </tr>
              </thead>
              <tbody>
                {analysis.keywords.map((kw, i) => (
                  <tr key={`${kw.keyword}-${i}`}>
                    <td
                      className="px-1 py-0.5 font-bold align-top"
                      style={{ border: '1px solid var(--win95-gray)' }}
                    >
                      {kw.keyword}
                    </td>
                    <td
                      className="px-1 py-0.5 align-top"
                      style={{
                        border: '1px solid var(--win95-gray)',
                        color: 'var(--text-muted)',
                      }}
                    >
                      {kw.meaning}
                    </td>
                    <td
                      className="px-1 py-0.5 align-top"
                      style={{ border: '1px solid var(--win95-gray)' }}
                    >
                      {kw.scenarios.map((id) => `#${id}`).join(', ')}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {!isAtomic && (
          <div className="flex flex-col gap-1 mt-2">
            {analysis.scenarios.map((s) => {
              const isGenerating = generatingScenarioId === s.id;
              const isDone = completedScenarioIds.has(s.id);
              return (
                <div
                  key={s.id}
                  className="flex items-center gap-2 px-2 py-1 text-xs"
                  style={{
                    background: isDone
                      ? 'var(--status-accept-bg)'
                      : isGenerating
                        ? 'var(--status-edit-bg)'
                        : 'var(--win95-gray-lighter)',
                    border: '1px solid var(--win95-gray)',
                  }}
                >
                  {isDone ? (
                    <RiCheckFill
                      className="size-3 shrink-0"
                      style={{ color: 'var(--status-accept-dark)' }}
                    />
                  ) : isGenerating ? (
                    <RiLoader4Line className="size-3 shrink-0 animate-spin" />
                  ) : (
                    <RiArrowRightLine
                      className="size-3 shrink-0"
                      style={{ color: 'var(--win95-gray-mid)' }}
                    />
                  )}
                  <span className="font-bold text-[11px]">
                    #{s.id} {s.name}
                  </span>
                  <span
                    className="text-[10px]"
                    style={{ color: 'var(--text-muted)' }}
                  >
                    {s.description}
                  </span>
                </div>
              );
            })}
          </div>
        )}
      </div>
    )}
  </div>
  );
};

export default DecomposeAnalysisPanel;
