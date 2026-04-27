'use client';

import React, { useCallback, useEffect, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import {
  fetchGroupingPreview,
  fetchMatchPreview,
} from '../../../services/jobAdapter';
import { useJobHistoryStore } from '../../../store/useJobHistoryStore';
import { ConfigureBottomBar } from './ConfigureBottomBar';
import { GroupingTab } from './GroupingTab';
import { OptionsTab } from './OptionsTab';
import { SpecMatchingTab } from './SpecMatchingTab';
import { TABS, estimateBudget } from './constants';
import type {
  ConfigureTabId,
  GroupPreviewState,
  MatchPreviewState,
} from './types';

/**
 * Configure module orchestrator — owns tab state, preview fetching, and
 * derived summary values. Renders focused tab panels that receive all
 * data via props.
 */
const ConfigureModule: React.FC = () => {
  const { tcRows, config, updateConfig, setTcRows, jobMetadata, accumulateStats } = useJobStore();
  const { openWindow, advanceWindow } = useWindowStore();
  const [groupingCostSpent, setGroupingCostSpent] = useState(0);

  const [activeTab, setActiveTab] = useState<ConfigureTabId>('tab1');

  const [groupPreview, setGroupPreview] = useState<GroupPreviewState | null>(null);
  const [matchPreview, setMatchPreview] = useState<MatchPreviewState | null>(null);
  const [groupError, setGroupError] = useState<string | null>(null);
  const [matchError, setMatchError] = useState<string | null>(null);
  const [isLoadingGroupPreview, setIsLoadingGroupPreview] = useState(false);
  const [isLoadingMatchPreview, setIsLoadingMatchPreview] = useState(false);

  const estimatedCalls = tcRows.length
    ? Math.ceil(tcRows.length / Math.max(config.batchSize, 1))
    : 0;
  const estimatedBudget = estimateBudget(tcRows.length, config.model, config.budgetLimit, groupingCostSpent);

  const loadGroupingPreview = useCallback(async (forceRegroup = false) => {
    if (!tcRows.length) {
      setGroupPreview(null);
      return;
    }
    setIsLoadingGroupPreview(true);
    setGroupError(null);
    setGroupPreview(null);
    try {
      const preview = await fetchGroupingPreview({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
        forceRegroup,
      });
      if (preview.cost > 0) {
        setGroupingCostSpent((value) => Number((value + preview.cost).toFixed(4)));
        accumulateStats({
          cost: preview.cost,
          inputTokens: preview.inputTokens,
          outputTokens: preview.outputTokens,
          cacheCreationTokens: preview.cacheCreationTokens,
          cacheReadTokens: preview.cacheReadTokens,
        });
        useJobHistoryStore.getState().appendRecord({
          id: `group-${Date.now().toString(36)}`,
          kind: 'group',
          model: preview.model || config.model,
          startedAt: Date.now(),
          finishedAt: Date.now(),
          rowsTotal: tcRows.length,
          rowsProcessed: preview.assignments.length,
          cost: preview.cost,
          inputTokens: preview.inputTokens,
          outputTokens: preview.outputTokens,
          cacheReadTokens: preview.cacheReadTokens,
          cacheCreationTokens: preview.cacheCreationTokens,
        });
      }
      setGroupPreview(preview);
    } catch (error) {
      setGroupError(
        error instanceof Error ? error.message : 'Failed to load grouping preview.',
      );
    } finally {
      setIsLoadingGroupPreview(false);
    }
  }, [tcRows, jobMetadata?.jobId, accumulateStats, config.model]);

  const loadMatchPreview = useCallback(async () => {
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
      setMatchError(
        error instanceof Error ? error.message : 'Failed to load spec matching preview.',
      );
    } finally {
      setIsLoadingMatchPreview(false);
    }
  }, [tcRows, jobMetadata?.jobId]);

  useEffect(() => {
    if (activeTab === 'tab1' && tcRows.length && !groupPreview && !isLoadingGroupPreview) {
      void loadGroupingPreview();
    }
    if (activeTab === 'tab2' && tcRows.length && !matchPreview && !isLoadingMatchPreview) {
      void loadMatchPreview();
    }
  }, [
    activeTab,
    tcRows,
    groupPreview,
    matchPreview,
    isLoadingGroupPreview,
    isLoadingMatchPreview,
    loadGroupingPreview,
    loadMatchPreview,
  ]);

  const applyGroupingPreview = useCallback(() => {
    if (!groupPreview) return;
    const assignments = new Map(
      groupPreview.assignments.map((entry) => [entry.id, entry.testSet]),
    );
    setTcRows(
      tcRows.map((row) => ({
        ...row,
        testSet: assignments.get(row.id) ?? row.testSet,
      })),
    );
  }, [groupPreview, tcRows, setTcRows]);

  const handleStartGenerate = useCallback(() => {
    if (!tcRows.length) return;
    if (groupPreview) {
      const assignments = new Map(
        groupPreview.assignments.map((entry) => [entry.id, entry.testSet]),
      );
      setTcRows(
        tcRows.map((row) => ({
          ...row,
          testSet: assignments.get(row.id) ?? row.testSet,
        })),
      );
    }
    advanceWindow('configure', 'generate', 'TC Generator - Generating...');
  }, [advanceWindow, groupPreview, tcRows, setTcRows]);

  const handleBack = useCallback(() => {
    advanceWindow('configure', 'upload', 'Upload Files');
  }, [advanceWindow]);

  const invalidateGroupPreview = useCallback(() => {
    setGroupPreview(null);
  }, []);

  return (
    <div className="flex flex-col h-full overflow-hidden">
      {/* 98.css native tab structure */}
      <div className="flex-1 flex flex-col overflow-hidden" role="tabpanel">
        <div className="flex items-end justify-between gap-2">
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
        </div>

        {/* Tab content panel */}
        <div
          className="window flex-1 overflow-hidden flex flex-col"
          style={{ zIndex: 2, position: 'relative' }}
        >
          <div className="window-body flex-1 overflow-auto p-2">
            {activeTab === 'tab1' && (
              <GroupingTab
                tcRows={tcRows}
                setTcRows={setTcRows}
                preview={groupPreview}
                isLoading={isLoadingGroupPreview}
                error={groupError}
                onRefresh={() => void loadGroupingPreview()}
                onForceRegroup={() => void loadGroupingPreview(true)}
                onApply={applyGroupingPreview}
                onInvalidatePreview={invalidateGroupPreview}
              />
            )}

            {activeTab === 'tab2' && (
              <SpecMatchingTab
                preview={matchPreview}
                isLoading={isLoadingMatchPreview}
                error={matchError}
                onRefresh={() => void loadMatchPreview()}
              />
            )}

            {activeTab === 'tab3' && (
              <OptionsTab config={config} onUpdateConfig={updateConfig} />
            )}
          </div>
        </div>
      </div>

      <ConfigureBottomBar
        estimatedCalls={estimatedCalls}
        estimatedBudget={estimatedBudget}
        strictValidation={config.strictValidation}
        canStartGenerate={tcRows.length > 0}
        onBack={handleBack}
        onStartGenerate={handleStartGenerate}
      />
    </div>
  );
};

export default ConfigureModule;
