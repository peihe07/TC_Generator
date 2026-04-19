'use client';

import React, { useCallback, useEffect, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import {
  fetchGroupingPreview,
  fetchMatchPreview,
} from '../../../services/jobAdapter';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
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
  const { tcRows, config, updateConfig, setTcRows, jobMetadata } = useJobStore();
  const { openWindow } = useWindowStore();

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
  const estimatedBudget = estimateBudget(tcRows.length, config.model, config.budgetLimit);

  const loadGroupingPreview = useCallback(async () => {
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
      setGroupError(
        error instanceof Error ? error.message : 'Failed to load grouping preview.',
      );
    } finally {
      setIsLoadingGroupPreview(false);
    }
  }, [tcRows, jobMetadata?.jobId]);

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
    openWindow('generate', 'TC Generator - Generating...');
  }, [openWindow]);

  const handleBack = useCallback(() => {
    openWindow('upload', 'Upload Files');
  }, [openWindow]);

  const invalidateGroupPreview = useCallback(() => {
    setGroupPreview(null);
  }, []);

  const buildContext = useCallback(() => {
    const jobId = jobMetadata?.jobId ?? '未開啟 job';
    const count = tcRows.length;
    return `[context: 目前在 Configure Module, job=${jobId}]\n[Test Sets: ${count} 個]\n`;
  }, [jobMetadata?.jobId, tcRows.length]);

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
        onBack={handleBack}
        onStartGenerate={handleStartGenerate}
      />
    </div>
  );
};

export default ConfigureModule;
