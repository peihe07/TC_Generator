'use client';

import React, { useEffect, useMemo, useState } from 'react';
import * as Tabs from '@radix-ui/react-tabs';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { fetchGroupingPreview, fetchMatchPreview } from '../../../services/jobAdapter';
import {
  RiArrowLeftLine,
  RiLinkM,
  RiLoader4Line,
  RiNodeTree,
  RiPlayFill,
  RiRefreshLine,
  RiSettings4Line,
} from '@remixicon/react';

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
    unmatched: number;
    hasReferenceWorkbook: boolean;
  };
  matches: Array<{
    id: string;
    reqId: string;
    testItem: string;
    specReference: string | null;
    matchType: 'exact' | 'unmatched';
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
    Number((tcRows.length * (config.model === 'claude-3-haiku' ? 0.008 : 0.02)).toFixed(2)),
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

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <Tabs.Root
        className="flex-1 flex flex-col"
        value={activeTab}
        onValueChange={setActiveTab}
      >
        <Tabs.List className="tabs" aria-label="Configuration steps">
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab1">
            <RiNodeTree className="size-4" /> Grouping
          </Tabs.Trigger>
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab2">
            <RiLinkM className="size-4" /> Spec Matching
          </Tabs.Trigger>
          <Tabs.Trigger className="tabs-tab flex items-center gap-1" value="tab3">
            <RiSettings4Line className="size-4" /> Options
          </Tabs.Trigger>
        </Tabs.List>

        <div className="flex-1 mt-2 overflow-hidden flex flex-col">
          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-2" value="tab1">
            <div className="flex items-center justify-between mb-3">
              <p className="text-sm">Current test set preview for imported requirements.</p>
              <div className="flex items-center gap-2">
                <button className="text-xs flex items-center gap-1" onClick={() => void loadGroupingPreview()}>
                  {isLoadingGroupPreview ? <RiLoader4Line className="size-3 animate-spin" /> : <RiRefreshLine className="size-3" />}
                  Refresh
                </button>
                <button
                  className="text-xs font-bold"
                  onClick={applyGroupingPreview}
                  disabled={!groupPreview}
                >
                  Apply To Rows
                </button>
              </div>
            </div>

            {groupError && (
              <div className="status-bar-field p-2 mb-2 bg-red-50 text-red-800 text-xs">
                {groupError}
              </div>
            )}

            {groupPreview && (
              <div className="status-bar-field p-2 mb-2 bg-blue-50 text-blue-900 text-xs">
                {groupPreview.groups.length} group(s) prepared for {groupPreview.assignments.length} row(s).
              </div>
            )}

            <table className="w-full text-sm border-collapse">
              <thead>
                <tr className="bg-gray-200 border-b border-gray-400">
                  <th className="text-left p-1 border-r border-gray-300">Test Set</th>
                  <th className="text-left p-1 border-r border-gray-300">Count</th>
                  <th className="text-left p-1">Requirement IDs</th>
                </tr>
              </thead>
              <tbody>
                {groupPreview?.groups.length ? (
                  groupPreview.groups.map((group) => (
                    <tr key={group.testSet} className="border-b border-gray-200 hover:bg-blue-50">
                      <td className="p-1 border-r border-gray-300 font-mono">{group.testSet}</td>
                      <td className="p-1 border-r border-gray-300 font-mono">{group.count}</td>
                      <td className="p-1 text-gray-600">{group.reqIds.join(', ')}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={3} className="p-4 text-center text-gray-400 italic">
                      {isLoadingGroupPreview ? 'Loading grouping preview...' : 'No grouping preview available yet.'}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </Tabs.Content>

          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-2" value="tab2">
            <div className="flex items-center justify-between mb-3">
              <div className="flex flex-col gap-1">
                <span className="text-sm">Exact traceability preview from the optional reference workbook.</span>
                {matchPreview && (
                  <span className="text-xs text-gray-600">
                    Exact matches: {matchPreview.summary.exact}/{matchPreview.summary.total} ({exactMatchRatio}%)
                  </span>
                )}
              </div>
              <button className="text-xs flex items-center gap-1" onClick={() => void loadMatchPreview()}>
                {isLoadingMatchPreview ? <RiLoader4Line className="size-3 animate-spin" /> : <RiRefreshLine className="size-3" />}
                Refresh
              </button>
            </div>

            {matchError && (
              <div className="status-bar-field p-2 mb-2 bg-red-50 text-red-800 text-xs">
                {matchError}
              </div>
            )}

            {matchPreview && (
              <div className="status-bar-field p-2 mb-2 bg-blue-50 text-blue-900 text-xs">
                {matchPreview.summary.hasReferenceWorkbook
                  ? `Reference workbook loaded. ${matchPreview.summary.exact} exact match(es), ${matchPreview.summary.unmatched} unmatched.`
                  : 'No compatible reference workbook loaded. Exact matching preview is unavailable.'}
              </div>
            )}

            <table className="w-full text-xs border-collapse">
              <thead>
                <tr className="bg-gray-200 border-b border-gray-400">
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
                      <td className="p-1 border-r max-w-[220px] truncate">{row.testItem}</td>
                      <td className="p-1 border-r font-mono">
                        {row.specReference || '—'}
                      </td>
                      <td className={`p-1 font-bold ${row.matchType === 'exact' ? 'text-green-700' : 'text-gray-500'}`}>
                        {row.matchType === 'exact' ? 'Exact' : 'Unmatched'}
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={4} className="p-4 text-center text-gray-400 italic">
                      {isLoadingMatchPreview ? 'Loading spec matching preview...' : 'No spec matching preview available yet.'}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </Tabs.Content>

          <Tabs.Content className="flex-1 overflow-auto bg-white border-2 border-sunken p-4" value="tab3">
            <div className="flex flex-col gap-6">
              <fieldset>
                <legend>AI Model Settings</legend>
                <div className="flex flex-col gap-2">
                  <div className="field-row">
                    <input
                      type="radio" id="m1" name="model"
                      checked={config.model === 'claude-3-5-sonnet'}
                      onChange={() => updateConfig({ model: 'claude-3-5-sonnet' })}
                    />
                    <label htmlFor="m1">Claude 3.5 Sonnet (High Accuracy)</label>
                  </div>
                  <div className="field-row">
                    <input
                      type="radio" id="m2" name="model"
                      checked={config.model === 'claude-3-haiku'}
                      onChange={() => updateConfig({ model: 'claude-3-haiku' })}
                    />
                    <label htmlFor="m2">Claude 3 Haiku (Fast & Cheap)</label>
                  </div>
                </div>
              </fieldset>

              <fieldset>
                <legend>Generation Limits</legend>
                <div className="flex flex-col gap-4">
                  <div className="field-row-stacked">
                    <label htmlFor="batch-size">Batch Size: {config.batchSize}</label>
                    <input
                      id="batch-size"
                      type="range"
                      min="1"
                      max="10"
                      value={config.batchSize}
                      onChange={(e) => updateConfig({ batchSize: parseInt(e.target.value, 10) })}
                    />
                  </div>
                  <div className="field-row-stacked">
                    <label htmlFor="budget">Max Budget (USD): ${config.budgetLimit}</label>
                    <input
                      id="budget" type="range" min="1" max="50"
                      value={config.budgetLimit}
                      onChange={(e) => updateConfig({ budgetLimit: parseInt(e.target.value, 10) })}
                    />
                  </div>
                  <div className="field-row">
                    <input
                      type="checkbox"
                      id="strict-validation"
                      checked={config.strictValidation}
                      onChange={(e) => updateConfig({ strictValidation: e.target.checked })}
                    />
                    <label htmlFor="strict-validation">Strict Validation</label>
                  </div>
                </div>
              </fieldset>

              <fieldset>
                <legend>Target Columns</legend>
                <div className="grid grid-cols-2 gap-2">
                  {['preConditions', 'steps', 'expectedResults'].map((col) => (
                    <div key={col} className="field-row">
                      <input
                        type="checkbox"
                        id={col}
                        checked={config.targetColumns.includes(col)}
                        onChange={(e) => {
                          const cols = e.target.checked
                            ? [...config.targetColumns, col]
                            : config.targetColumns.filter((current) => current !== col);
                          updateConfig({ targetColumns: cols });
                        }}
                      />
                      <label htmlFor={col}>{col.charAt(0).toUpperCase() + col.slice(1)}</label>
                    </div>
                  ))}
                </div>
              </fieldset>
            </div>
          </Tabs.Content>
        </div>
      </Tabs.Root>

      <div className="flex justify-between items-center pt-4 border-t border-gray-400 mt-2">
        <button className="flex items-center gap-1" onClick={() => openWindow('upload', 'Upload Files')}>
          <RiArrowLeftLine className="size-4" /> Back
        </button>
        <div className="text-xs text-gray-500">
          Est. calls: <span className="text-black font-bold font-mono">{estimatedCalls}</span>
          {' '}| Est. cost ceiling: <span className="text-black font-bold font-mono">${estimatedBudget.toFixed(2)}</span>
          {' '}| Validation: <span className="text-black font-bold">{config.strictValidation ? 'strict' : 'warn only'}</span>
        </div>
        <button className="flex items-center gap-1 font-bold default" onClick={handleStartGenerate}>
          Start Generate <RiPlayFill className="size-4 text-green-700" />
        </button>
      </div>
    </div>
  );
};

export default ConfigureModule;
