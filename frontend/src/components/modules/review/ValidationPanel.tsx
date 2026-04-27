import React, { useState } from 'react';
import {
  RiAlertFill,
  RiCheckboxCircleFill,
  RiDownload2Line,
  RiErrorWarningFill,
  RiSparklingLine,
} from '@remixicon/react';
import { TcRow } from '../../../lib/types';
import { Button } from '../../ui';
import {
  requestReviewFixSuggestion,
  type ReviewFixSuggestion,
} from '../../../services/jobAdapter';

export interface ValidationPanelProps {
  selectedRow: TcRow | null;
  onExport: () => void;
  /**
   * Called when the reviewer accepts an AI-suggested reason. Parent should
   * write it into the Regenerate Reason input (the user still has to press
   * Regenerate explicitly — we never auto-trigger).
   */
  onApplySuggestedReason?: (reason: string) => void;
  /**
   * Panel width in px. Controlled by `useResizablePanel` in the parent
   * (`ReviewModule`). Defaults to 320 when omitted — that's the initial
   * width from the hook before it hydrates from localStorage. See
   * MIGRATION.md §P1 for the splitter spec.
   */
  width?: number;
}

type SuggestState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'ok'; data: ReviewFixSuggestion; editableReason: string }
  | { kind: 'error'; message: string };

/**
 * Right-hand panel: shows validation results for the currently active row
 * plus the primary "Export All" call-to-action. When validation errors
 * exist, exposes a single "Ask AI" action that returns a fix explanation
 * and a one-line reason ready to paste into Regenerate.
 */
export const ValidationPanel: React.FC<ValidationPanelProps> = ({
  selectedRow,
  onExport,
  onApplySuggestedReason,
  width = 320,
}) => {
  const [suggest, setSuggest] = useState<SuggestState>({ kind: 'idle' });

  // Re-key suggestion state by row so switching rows resets the panel.
  const activeRowKey = selectedRow?.id ?? null;
  const [activeKey, setActiveKey] = useState<string | null>(null);
  if (activeKey !== activeRowKey) {
    setActiveKey(activeRowKey);
    if (suggest.kind !== 'idle') setSuggest({ kind: 'idle' });
  }

  const errors = selectedRow?.validationErrors ?? [];
  const hasErrors = errors.length > 0;

  const handleAsk = async () => {
    if (!selectedRow || !hasErrors) return;
    setSuggest({ kind: 'loading' });
    try {
      const data = await requestReviewFixSuggestion({
        tc: {
          tc_id: selectedRow.tcId,
          req_id: selectedRow.reqId,
          tc_title: selectedRow.tcTitle,
          pre_conditions: selectedRow.preConditions,
          input_test_data: selectedRow.inputTestData,
          test_procedure: selectedRow.steps,
          expected_result: selectedRow.expectedResults,
          design_method: selectedRow.designMethod,
          priority: selectedRow.priority,
        },
        errors: errors.map((err) => ({
          severity: err.severity,
          field: err.column,
          message: err.message,
        })),
      });
      setSuggest({ kind: 'ok', data, editableReason: data.suggestedReason });
    } catch (err) {
      setSuggest({
        kind: 'error',
        message: err instanceof Error ? err.message : 'Suggestion request failed.',
      });
    }
  };

  const handleApplyReason = () => {
    if (suggest.kind !== 'ok' || !onApplySuggestedReason) return;
    const reason = suggest.editableReason.trim();
    if (!reason) return;
    onApplySuggestedReason(reason);
  };

  const handleEditableReasonChange = (value: string) => {
    setSuggest((current) =>
      current.kind === 'ok' ? { ...current, editableReason: value } : current,
    );
  };

  return (
    <div
      className="flex flex-col gap-2"
      style={{ width, flexShrink: 0 }}
    >
      <fieldset className="flex-1 flex flex-col overflow-hidden">
        <legend className="text-sm">Validation Results</legend>
        <div className="flex-1 overflow-auto p-2 flex flex-col gap-2">
          <div className="text-[11px]" style={{ color: 'var(--win95-gray-dark)' }}>
            Showing validation for the currently expanded row only.
          </div>
          {!selectedRow ? (
            <div className="sys-log-entry" style={{ color: 'var(--win95-gray-dark)' }}>
              <span className="sys-log-tag info">INFO</span>
              Expand a row to view validation.
            </div>
          ) : hasErrors ? (
            errors.map((err, i) => (
              <div key={i} className="sys-log-entry selectable">
                <div className="flex items-start gap-2">
                  {err.severity === 'error' ? (
                    <RiErrorWarningFill
                      className="size-4 shrink-0 mt-0.5"
                      style={{ color: 'var(--status-reject)' }}
                    />
                  ) : (
                    <RiAlertFill
                      className="size-4 shrink-0 mt-0.5"
                      style={{ color: 'var(--status-warn)' }}
                    />
                  )}
                  <div className="flex-1 min-w-0">
                    <div>
                      <span
                        className={`sys-log-tag ${err.severity === 'error' ? 'critical' : 'warn'}`}
                      >
                        {err.severity === 'error' ? 'CRITICAL' : 'WARNING'}
                      </span>
                      <span className="font-bold text-[11px]">
                        {err.severity === 'error' ? 'Logic Conflict' : 'Quality Warning'}
                      </span>
                    </div>
                    <div className="text-[11px] mt-1" style={{ color: 'var(--win95-gray-darker)' }}>
                      {err.message}
                    </div>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="sys-log-entry selectable">
              <div className="flex items-start gap-2">
                <RiCheckboxCircleFill
                  className="size-4 shrink-0 mt-0.5"
                  style={{ color: 'var(--status-accept)' }}
                />
                <div className="flex-1">
                  <div>
                    <span className="sys-log-tag info">PASS</span>
                    <span className="font-bold text-[11px]">All Checks Passed</span>
                  </div>
                  <div className="text-[11px] mt-1" style={{ color: 'var(--win95-gray-darker)' }}>
                    This test case meets all AI quality standards.
                  </div>
                </div>
              </div>
            </div>
          )}

          {hasErrors && (
            <div className="border-sunken p-2 flex flex-col gap-2">
              <div className="flex items-center justify-between gap-2">
                <span className="text-[11px] font-bold flex items-center gap-1">
                  <RiSparklingLine className="size-3" />
                  AI 修法建議
                </span>
                <Button
                  onClick={handleAsk}
                  disabled={suggest.kind === 'loading'}
                  title="呼叫 AI 一次性產生修法說明與 Regenerate Reason 草稿"
                >
                  {suggest.kind === 'loading' ? '查詢中…' : '詢問 AI'}
                </Button>
              </div>

              {suggest.kind === 'error' && (
                <div className="text-[11px]" style={{ color: 'var(--status-reject-dark)' }}>
                  {suggest.message}
                </div>
              )}

              {suggest.kind === 'ok' && (
                <div className="flex flex-col gap-2">
                  <div
                    className="text-[11px] whitespace-pre-wrap"
                    style={{ color: 'var(--win95-gray-darker)' }}
                  >
                    {suggest.data.suggestion}
                  </div>
                  <div className="text-[11px] flex flex-col gap-1">
                    <span className="font-bold">
                      Regenerate Reason（可編輯，中/英皆可）：
                    </span>
                    <textarea
                      className="border-sunken p-1"
                      style={{
                        background: 'var(--win95-white)',
                        minHeight: 56,
                        resize: 'vertical',
                        fontFamily: 'inherit',
                        fontSize: 11,
                      }}
                      value={suggest.editableReason}
                      onChange={(event) =>
                        handleEditableReasonChange(event.target.value)
                      }
                      placeholder="可改寫或自由描述問題，AI 會以此為主要修正目標"
                    />
                  </div>
                  <Button
                    onClick={handleApplyReason}
                    disabled={
                      !onApplySuggestedReason ||
                      !suggest.editableReason.trim()
                    }
                    title="把上方 reason 寫入下方 Regenerate Reason 欄位（不會自動觸發 Regenerate）"
                  >
                    套用為 Regenerate Reason
                  </Button>
                </div>
              )}
            </div>
          )}
        </div>
      </fieldset>

      <Button
        className="w-full py-3 flex items-center justify-center gap-2 default"
        onClick={onExport}
      >
        <RiDownload2Line className="size-5" /> Export All
      </Button>
    </div>
  );
};

export default ValidationPanel;
