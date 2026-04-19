'use client';

import React, { useEffect, useMemo, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { fetchGroupingPreview, fetchMatchPreview } from '../../../services/jobAdapter';
import {
  RiArrowLeftLine,
  RiLoader4Line,
  RiPlayFill,
  RiRefreshLine,
} from '@remixicon/react';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';

type GroupPreviewState = {
  groups: Array<{
    testSet: string;
    count: number;
    reqIds: string[];
  }>;
  assignments: Array<{
    id: string;
    reqId: string;
    testSet: string;
    source: 'existing' | 'derived';
  }>;
};

type MatchPreviewState = {
  summary: {
    total: number;
    exact: number;
    fuzzy: number;
    unmatched: number;
    hasReferenceWorkbook: boolean;
  };
  matches: Array<{
    id: string;
    reqId: string;
    testItem: string;
    specReference: string | null;
    matchType: 'exact' | 'fuzzy' | 'unmatched';
    matchScore?: number | null;
  }>;
};

const ConfigureModule: React.FC = () => {
  const {
    tcRows,
    config,
    updateConfig,
    setTcRows,
    jobMetadata,
  } = useJobStore();
  const { openWindow } = useWindowStore();
  const [activeTab, setActiveTab] = useState('tab1');
  const [groupPreview, setGroupPreview] = useState<GroupPreviewState | null>(null);
  const [matchPreview, setMatchPreview] = useState<MatchPreviewState | null>(null);
  const [groupError, setGroupError] = useState<string | null>(null);
  const [matchError, setMatchError] = useState<string | null>(null);
  const [isLoadingGroupPreview, setIsLoadingGroupPreview] = useState(false);
  const [isLoadingMatchPreview, setIsLoadingMatchPreview] = useState(false);

  const estimatedCalls = tcRows.length ? Math.ceil(tcRows.length / Math.max(config.batchSize, 1)) : 0;
  const estimatedBudget = Math.min(
    config.budgetLimit,
    Number((tcRows.length * (
      config.model === 'gpt-5' ? 0.03 :
      config.model === 'gpt-4.1' ? 0.015 :
      config.model === 'gpt-4.1-mini' ? 0.004 :
      config.model === 'gpt-4o' ? 0.02 :
      config.model === 'gpt-4o-mini' ? 0.002 : 0.01
    )).toFixed(2)),
  );

  const exactMatchRatio = useMemo(() => {
    if (!matchPreview?.summary.total) {
      return 0;
    }
    return Math.round((matchPreview.summary.exact / matchPreview.summary.total) * 100);
  }, [matchPreview]);

  const loadGroupingPreview = async () => {
    if (!tcRows.length) {
      setGroupPreview(null);
      return;
    }

    setIsLoadingGroupPreview(true);
    setGroupError(null);
    try {
      const preview = await fetchGroupingPreview({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
      });
      setGroupPreview(preview);
    } catch (error) {
      setGroupError(error instanceof Error ? error.message : 'Failed to load grouping preview.');
    } finally {
      setIsLoadingGroupPreview(false);
    }
  };

  const loadMatchPreview = async () => {
    if (!tcRows.length) {
      setMatchPreview(null);
      return;
    }

    setIsLoadingMatchPreview(true);
    setMatchError(null);
    try {
      const preview = await fetchMatchPreview({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
      });
      setMatchPreview(preview);
    } catch (error) {
      setMatchError(error instanceof Error ? error.message : 'Failed to load spec matching preview.');
    } finally {
      setIsLoadingMatchPreview(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'tab1' && tcRows.length && !groupPreview && !isLoadingGroupPreview) {
      void loadGroupingPreview();
    }
    if (activeTab === 'tab2' && tcRows.length && !matchPreview && !isLoadingMatchPreview) {
      void loadMatchPreview();
    }
  }, [activeTab, tcRows, groupPreview, matchPreview, isLoadingGroupPreview, isLoadingMatchPreview]);

  const applyGroupingPreview = () => {
    if (!groupPreview) {
      return;
    }
    const assignments = new Map(groupPreview.assignments.map((entry) => [entry.id, entry.testSet]));
    setTcRows(
      tcRows.map((row) => ({
        ...row,
        testSet: assignments.get(row.id) ?? row.testSet,
      })),
    );
  };

  const handleStartGenerate = () => {
    openWindow('generate', 'TC Generator - Generating...');
  };

  const TABS = [
    { id: 'tab1', label: 'Grouping' },
    { id: 'tab2', label: 'Spec Matching' },
    { id: 'tab3', label: 'Options' },
  ] as const;

  const buildContext = () => {
    const jobId = jobMetadata?.jobId ?? '未開啟 job';
    const count = tcRows.length;
    return `[context: 目前在 Configure Module, job=${jobId}]\n[Test Sets: ${count} 個]\n`;
  };

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="flex justify-end pb-1">
        <HelpFromAgentButton contextPrompt={buildContext()} title="求助 AI" />
      </div>
      {/* 98.css native tab structure */}
      <div className="flex-1 flex flex-col overflow-hidden" role="tabpanel">
        <menu role="tablist" style={{ paddingLeft: 3, marginBottom: -2 }}>
          {TABS.map(({ id, label }) => (
            <li
              key={id}
              role="tab"
              aria-selected={activeTab === id}
              style={{ cursor: 'pointer' }}
              onClick={() => setActiveTab(id)}
            >
              <a onClick={(e) => e.preventDefault()}>{label}</a>
            </li>
          ))}
        </menu>

        {/* Tab content panel */}
        <div className="window flex-1 overflow-hidden flex flex-col" style={{ zIndex: 2, position: 'relative' }}>
          <div className="window-body flex-1 overflow-auto p-2">

            {/* Tab 1 — Grouping */}
            {activeTab === 'tab1' && (
              <>
                <div className="flex items-center justify-between mb-2">
                  <p>Current test set preview for imported requirements.</p>
                  <div className="flex items-center gap-2">
                    <button className="flex items-center gap-1" onClick={() => void loadGroupingPreview()}>
                      {isLoadingGroupPreview ? <RiLoader4Line className="size-3 animate-spin" /> : <RiRefreshLine className="size-3" />}
                      Refresh
                    </button>
                    <button onClick={applyGroupingPreview} disabled={!groupPreview}>
                      Apply To Rows
                    </button>
                  </div>
                </div>

                {groupError && (
                  <div className="status-bar-field p-1 mb-2" style={{ color: 'var(--status-reject-dark)', background: '#fff0f0' }}>
                    {groupError}
                  </div>
                )}
                {groupPreview && (
                  <div className="status-bar-field p-1 mb-2">
                    {groupPreview.groups.length} group(s) prepared for {groupPreview.assignments.length} row(s).
                  </div>
                )}

                <table className="w-full border-collapse mb-3">
                  <thead>
                    <tr>
                      <th className="text-left p-1 border-r">Test Set</th>
                      <th className="text-left p-1 border-r">Count</th>
                      <th className="text-left p-1">Requirement IDs</th>
                    </tr>
                  </thead>
                  <tbody>
                    {groupPreview?.groups.length ? (
                      groupPreview.groups.map((group) => (
                        <tr key={group.testSet} className="border-b">
                          <td className="p-1 border-r font-mono">{group.testSet}</td>
                          <td className="p-1 border-r font-mono">{group.count}</td>
                          <td className="p-1">{group.reqIds.join(', ')}</td>
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td colSpan={3} className="p-4 text-center" style={{ color: 'var(--win95-gray-mid)', fontStyle: 'italic' }}>
                          {isLoadingGroupPreview ? 'Loading grouping preview...' : 'No grouping preview available yet.'}
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>

                {/* Per-row manual override — write directly to tcRows */}
                {tcRows.length > 0 && (
                  <>
                    <div className="flex items-center justify-between mb-1 mt-3">
                      <p className="font-bold text-xs uppercase" style={{ color: 'var(--text-muted)' }}>
                        Manual Override — edit any row's test set directly
                      </p>
                      <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>
                        Changes are saved immediately. Use the datalist for existing sets or type a new one.
                      </span>
                    </div>
                    <datalist id="existing-test-sets">
                      {[...new Set(tcRows.map((r) => r.testSet).filter(Boolean))].map((ts) => (
                        <option key={ts} value={ts} />
                      ))}
                      {groupPreview?.groups.map((g) => (
                        <option key={`grp-${g.testSet}`} value={g.testSet} />
                      ))}
                    </datalist>
                    <div
                      style={{
                        maxHeight: 260,
                        overflowY: 'auto',
                        border: '2px solid',
                        borderColor: 'var(--win95-gray-mid) var(--win95-white) var(--win95-white) var(--win95-gray-mid)',
                        background: 'var(--win95-white)',
                      }}
                    >
                      <table className="w-full border-collapse text-xs">
                        <thead className="sticky top-0" style={{ background: '#e8e8e8', zIndex: 1 }}>
                          <tr>
                            <th className="text-left p-1 border-r" style={{ width: 120 }}>Req ID</th>
                            <th className="text-left p-1 border-r">Test Item</th>
                            <th className="text-left p-1" style={{ width: 160 }}>Test Set</th>
                          </tr>
                        </thead>
                        <tbody>
                          {tcRows.map((row) => (
                            <tr key={row.id} className="border-b">
                              <td className="p-1 border-r font-mono">{row.reqId}</td>
                              <td
                                className="p-1 border-r"
                                style={{
                                  maxWidth: 0,
                                  overflow: 'hidden',
                                  textOverflow: 'ellipsis',
                                  whiteSpace: 'nowrap',
                                }}
                                title={row.testItem}
                              >
                                {row.testItem}
                              </td>
                              <td className="p-0">
                                <input
                                  type="text"
                                  list="existing-test-sets"
                                  value={row.testSet}
                                  onChange={(e) => {
                                    const v = e.target.value;
                                    setTcRows(
                                      tcRows.map((r) => (r.id === row.id ? { ...r, testSet: v } : r)),
                                    );
                                  }}
                                  onBlur={() => { setGroupPreview(null); }}
                                  style={{ width: '100%', border: 'none', padding: '2px 4px', fontSize: 11 }}
                                />
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </>
                )}
              </>
            )}

            {/* Tab 2 — Spec Matching */}
            {activeTab === 'tab2' && (
              <>
                <div className="flex items-center justify-between mb-2">
                  <div className="flex flex-col gap-1">
                    <span>Exact traceability preview from the optional reference workbook.</span>
                    {matchPreview && (
                      <span style={{ color: 'var(--text-muted)' }}>
                        Exact matches: {matchPreview.summary.exact}/{matchPreview.summary.total} ({exactMatchRatio}%)
                      </span>
                    )}
                  </div>
                  <button className="flex items-center gap-1" onClick={() => void loadMatchPreview()}>
                    {isLoadingMatchPreview ? <RiLoader4Line className="size-3 animate-spin" /> : <RiRefreshLine className="size-3" />}
                    Refresh
                  </button>
                </div>

                {matchError && (
                  <div className="status-bar-field p-1 mb-2" style={{ color: 'var(--status-reject-dark)', background: '#fff0f0' }}>
                    {matchError}
                  </div>
                )}
                {matchPreview && (
                  <div className="status-bar-field p-1 mb-2">
                    {matchPreview.summary.hasReferenceWorkbook
                      ? `Reference workbook loaded. ${matchPreview.summary.exact} exact, ${matchPreview.summary.fuzzy} fuzzy (token similarity), ${matchPreview.summary.unmatched} unmatched.`
                      : 'No compatible reference workbook loaded.'}
                  </div>
                )}

                <table className="w-full border-collapse">
                  <thead>
                    <tr>
                      <th className="p-1 border-r text-left">Req ID</th>
                      <th className="p-1 border-r text-left">Test Item</th>
                      <th className="p-1 border-r text-left">Matched Spec</th>
                      <th className="p-1 text-left">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {matchPreview?.matches.length ? (
                      matchPreview.matches.map((row) => (
                        <tr key={row.id} className="border-b">
                          <td className="p-1 border-r font-mono">{row.reqId}</td>
                          <td className="p-1 border-r" style={{ maxWidth: 220, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{row.testItem}</td>
                          <td className="p-1 border-r font-mono">{row.specReference || '—'}</td>
                          <td className="p-1 font-bold" style={{
                            color: row.matchType === 'exact' ? 'var(--status-accept-dark)'
                              : row.matchType === 'fuzzy' ? '#7d4e00'
                              : 'var(--win95-gray-mid)',
                          }}>
                            {row.matchType === 'exact'
                              ? 'Exact'
                              : row.matchType === 'fuzzy'
                                ? `Fuzzy ${row.matchScore != null ? `(${(row.matchScore * 100).toFixed(0)}%)` : ''}`
                                : 'Unmatched'}
                          </td>
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td colSpan={4} className="p-4 text-center" style={{ color: 'var(--win95-gray-mid)', fontStyle: 'italic' }}>
                          {isLoadingMatchPreview ? 'Loading spec matching preview...' : 'No spec matching preview available yet.'}
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </>
            )}

            {/* Tab 3 — Options */}
            {activeTab === 'tab3' && (
              <div className="flex flex-col gap-4">
                <fieldset>
                  <legend>AI Model</legend>
                  <div className="field-row">
                    <input type="radio" id="m-gpt5" name="model"
                      checked={config.model === 'gpt-5'}
                      onChange={() => updateConfig({ model: 'gpt-5' })}
                    />
                    <label htmlFor="m-gpt5">GPT-5 (Top Quality)</label>
                  </div>
                  <div className="field-row">
                    <input type="radio" id="m-gpt41" name="model"
                      checked={config.model === 'gpt-4.1'}
                      onChange={() => updateConfig({ model: 'gpt-4.1' })}
                    />
                    <label htmlFor="m-gpt41">GPT-4.1 (Quality, Stable)</label>
                  </div>
                  <div className="field-row">
                    <input type="radio" id="m-gpt41m" name="model"
                      checked={config.model === 'gpt-4.1-mini'}
                      onChange={() => updateConfig({ model: 'gpt-4.1-mini' })}
                    />
                    <label htmlFor="m-gpt41m">GPT-4.1 mini (Balanced)</label>
                  </div>
                  <div className="field-row">
                    <input type="radio" id="m-gpt4om" name="model"
                      checked={config.model === 'gpt-4o-mini'}
                      onChange={() => updateConfig({ model: 'gpt-4o-mini' })}
                    />
                    <label htmlFor="m-gpt4om">GPT-4o mini (Cheapest)</label>
                  </div>
                </fieldset>

                <fieldset>
                  <legend>Generation Limits</legend>
                  <div className="flex flex-col gap-3">
                    <div className="field-row-stacked">
                      <label htmlFor="batch-size">Batch Size: {config.batchSize}</label>
                      <input id="batch-size" type="range" min="1" max="10"
                        value={config.batchSize}
                        onChange={(e) => updateConfig({ batchSize: parseInt(e.target.value, 10) })}
                      />
                    </div>
                    <div className="field-row-stacked">
                      <label htmlFor="budget">Max Budget (USD): ${config.budgetLimit}</label>
                      <input id="budget" type="range" min="1" max="50"
                        value={config.budgetLimit}
                        onChange={(e) => updateConfig({ budgetLimit: parseInt(e.target.value, 10) })}
                      />
                    </div>
                    <div className="field-row">
                      <input type="checkbox" id="strict-validation"
                        checked={config.strictValidation}
                        onChange={(e) => updateConfig({ strictValidation: e.target.checked })}
                      />
                      <label htmlFor="strict-validation">Strict Validation</label>
                    </div>
                  </div>
                </fieldset>

                <fieldset>
                  <legend>Target Columns</legend>
                  <div className="flex flex-col gap-1">
                    {[
                      { key: 'preConditions', label: 'Pre-Conditions' },
                      { key: 'inputTestData', label: 'Input Test Data' },
                      { key: 'steps', label: 'Test Procedure' },
                      { key: 'expectedResults', label: 'Expected Result' },
                    ].map(({ key, label }) => (
                      <div key={key} className="field-row">
                        <input type="checkbox" id={key}
                          checked={config.targetColumns.includes(key)}
                          onChange={(e) => {
                            const cols = e.target.checked
                              ? [...config.targetColumns, key]
                              : config.targetColumns.filter((c) => c !== key);
                            updateConfig({ targetColumns: cols });
                          }}
                        />
                        <label htmlFor={key}>{label}</label>
                      </div>
                    ))}
                  </div>
                </fieldset>
              </div>
            )}

          </div>
        </div>
      </div>

      {/* Bottom bar */}
      <div className="flex justify-between items-center pt-2 mt-1" style={{ borderTop: '1px solid var(--win95-gray-mid)' }}>
        <button className="flex items-center gap-1" onClick={() => openWindow('upload', 'Upload Files')}>
          <RiArrowLeftLine className="size-4" /> Back
        </button>
        <div style={{ color: 'var(--text-muted)', fontSize: 11 }}>
          Est. calls: <strong>{estimatedCalls}</strong>
          {' | '}Est. cost ceiling: <strong>${estimatedBudget.toFixed(2)}</strong>
          {' | '}Validation: <strong>{config.strictValidation ? 'strict' : 'warn only'}</strong>
        </div>
        <button className="flex items-center gap-1 font-bold default" onClick={handleStartGenerate}>
          Start Generate <RiPlayFill className="size-4" style={{ color: 'var(--status-accept-dark)' }} />
        </button>
      </div>
    </div>
  );
};

export default ConfigureModule;
