import React from 'react';
import {
  RiArrowDownSLine,
  RiArrowGoBackLine,
  RiArrowUpSLine,
  RiCheckFill,
  RiCloseFill,
  RiDeleteBinLine,
  RiEditBoxLine,
  RiEditLine,
  RiFileTextLine,
  RiFlagFill,
  RiFlagLine,
  RiKey2Line,
  RiLightbulbLine,
  RiRefreshLine,
  RiSaveLine,
} from '@remixicon/react';
import { DESIGN_METHODS, TcRow } from '../../../lib/types';
import {
  Button,
  IconButton,
  StatusBadge,
  TitleBarMini,
  type StatusVariant,
} from '../../ui';
import { RegenDiff, type DiffFieldKey } from './RegenDiff';
import { StackedEditDropdown, StackedEditField, StackedReadField } from './StackedFields';

const PRIORITY_OPTIONS = ['P0', 'P1', 'P2', 'P3'] as const;

export interface EditValues {
  steps: string;
  expected: string;
  preConditions: string;
  inputTestData: string;
  designMethod: string;
  priority: string;
}

export interface ReviewRowProps {
  row: TcRow;
  isExpanded: boolean;
  isSelected: boolean;
  isActive: boolean;
  isEditing: boolean;
  editValues: EditValues;
  onToggleExpand: (id: string) => void;
  onToggleSelect: (id: string) => void;
  onSetActive: (id: string) => void;
  onStatusChange: (id: string, status: TcRow['status']) => void;
  onDelete: (id: string) => void;
  onStartEdit: (row: TcRow) => void;
  onEditValuesChange: (values: EditValues) => void;
  onSaveEdit: (id: string) => void;
  onCancelEdit: () => void;
  onToggleFlag: (id: string, currentStatus: string) => void;
  onApplyRegen: (id: string, fields: DiffFieldKey[]) => void;
  onDiscardRegen: (id: string) => void;
  /** Resolve a sibling row's tcId for the "重複於" badge. Returns undefined
   *  when the sibling row was deleted or never existed. */
  resolveSiblingTcId?: (rowId: string) => string | undefined;
}

/**
 * One table row + (optional) expanded detail panel. Handles view,
 * inline edit, and the regenerated-diff state per row.
 */
export const ReviewRow: React.FC<ReviewRowProps> = ({
  row,
  isExpanded,
  isSelected,
  isActive,
  isEditing,
  editValues,
  onToggleExpand,
  onToggleSelect,
  onSetActive,
  onStatusChange,
  onDelete,
  onStartEdit,
  onEditValuesChange,
  onSaveEdit,
  onCancelEdit,
  onToggleFlag,
  onApplyRegen,
  onDiscardRegen,
  resolveSiblingTcId,
}) => {
  const failureReason = row.validationErrors?.[0]?.message;
  const statusLabel =
    row.awaitingApply
      ? 'awaiting apply'
      : row.status === 'pending'
        ? 'awaiting review'
        : row.status === 'fail'
          ? 'failed'
          : row.status;

  return (
  <>
    <tr
      // §P12: `.selected` navy bg only responds to checkbox selection (isSelected),
      // not to "this row is the one synced to ValidationPanel" (isActive).
      // Expanding a row no longer hijacks the checkbox-selection visual.
      className={`cursor-pointer win95-row ${isSelected ? 'selected' : ''}`}
      style={
        row.awaitingApply && !isSelected
          ? { backgroundColor: 'var(--edit-accent-bg)' }
          : undefined
      }
    >
      <td
        style={{ cursor: 'pointer', width: 32, textAlign: 'center', verticalAlign: 'middle' }}
        onClick={(e) => {
          e.stopPropagation();
          onToggleSelect(row.id);
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            pointerEvents: 'none',
          }}
        >
          <input type="checkbox" id={`row-${row.id}`} checked={isSelected} onChange={() => {}} />
          <label htmlFor={`row-${row.id}`} style={{ margin: 0 }} />
        </div>
      </td>

      <td className="text-center py-2" onClick={() => onToggleExpand(row.id)}>
        {isExpanded ? <RiArrowUpSLine className="size-4" /> : <RiArrowDownSLine className="size-4" />}
      </td>

      <td
        className="px-3 py-2 font-mono text-xs"
        onClick={() => onToggleExpand(row.id)}
      >
        <span className="flex items-center gap-1">
          {row.status === 'flagged' && (
            <RiFlagFill className="size-3" style={{ color: 'var(--status-warn-dark)' }} />
          )}
          {row.awaitingApply && (
            <RiRefreshLine className="size-3" style={{ color: 'var(--status-edit-dark)' }} />
          )}
          {row.tcId || row.id}
          {row.splitDecision?.duplicateOf ? (
            <span
              className="inline-flex items-center font-bold"
              style={{
                fontSize: 9,
                padding: '0 4px',
                marginLeft: 2,
                background: 'var(--status-reject-bg-soft, #fde8e8)',
                color: 'var(--status-reject-dark, #7a1f1f)',
                border: '1px solid var(--status-reject-border, #d04444)',
                borderRadius: 2,
                whiteSpace: 'nowrap',
              }}
              title={`AI 嚴格判定本列與 row #${row.splitDecision.duplicateOf} 完全等價；展開可看完整訊息。`}
            >
              ⊕ DUP→{row.splitDecision.duplicateOf}
            </span>
          ) : null}
        </span>
      </td>
      <td
        className="px-3 py-2 font-mono text-xs"
        onClick={() => onToggleExpand(row.id)}
      >
        {row.reqId}
      </td>
      <td className="px-3 py-2" onClick={() => onToggleExpand(row.id)}>
        <div className="flex flex-col gap-1">
          <StatusBadge
            status={row.awaitingApply ? 'reviewing' : (row.status as StatusVariant)}
            style={row.status === 'generating' ? { animation: 'agent-pulse 1s ease-in-out infinite' } : undefined}
            title={row.status === 'fail' ? failureReason : undefined}
          >
            {statusLabel}
          </StatusBadge>
          {row.status === 'fail' && failureReason ? (
            <div
              className="text-[10px] leading-tight"
              // Post-§P12: `.selected` 現在只被 checkbox selection 觸發 (isSelected)。
              // expanded row 不再變 navy，所以大多數情況下 `var(--status-reject-dark)`
              // 紅字在白/灰底上對比 OK。此條件只剩 checkbox-selected 那個 edge case
              // (使用者勾選了某 FAILED row 做批次動作) 需要 white 文字對抗 navy bg。
              style={{
                color: isSelected
                  ? 'var(--text-inverse)'
                  : 'var(--status-reject-dark)',
              }}
              title={failureReason}
            >
              {failureReason}
            </div>
          ) : null}
        </div>
      </td>

      <td className="p-0 cell-center" onClick={(e) => e.stopPropagation()}>
        <div className="flex justify-center items-center gap-1 h-full min-h-[32px]">
          <IconButton
            label="Accept"
            variant="accept"
            onClick={() => onStatusChange(row.id, 'accepted')}
          >
            <RiCheckFill className="size-4" />
          </IconButton>
          <IconButton
            label="Reject"
            variant="reject"
            onClick={() => onStatusChange(row.id, 'rejected')}
          >
            <RiCloseFill className="size-4" />
          </IconButton>
          <IconButton
            label="Delete"
            style={{ color: 'var(--status-reject-dark)' }}
            onClick={() => onDelete(row.id)}
          >
            <RiDeleteBinLine className="size-4" />
          </IconButton>
        </div>
      </td>
    </tr>

    {isExpanded && (
      <tr>
        <td
          colSpan={6}
          className="p-4"
          style={{
            background: 'var(--win95-gray-mid)',
            boxShadow: 'inset 2px 2px 0 var(--win95-gray-dark), inset -2px -2px 0 var(--field-header-border)',
            borderBottom: '2px solid var(--win95-gray-darker)',
          }}
          onClick={() => onSetActive(row.id)}
        >
          {row.awaitingApply ? (
            <RegenDiff
              row={row}
              onApply={(fields) => onApplyRegen(row.id, fields)}
              onDiscard={() => onDiscardRegen(row.id)}
            />
          ) : (
            <div className="flex flex-col gap-3">
              {row.status === 'fail' && failureReason ? (
                <div
                  className="paper-card p-2 text-xs"
                  style={{
                    background: 'var(--status-error-bg-soft)',
                    border: '1px solid var(--status-error-border)',
                    color: 'var(--status-reject-dark)',
                  }}
                >
                  Generation failed for this row. Reason: {failureReason}
                </div>
              ) : null}
              {row.splitWarning ? (
                <div
                  className="paper-card p-2 text-xs leading-relaxed"
                  style={{
                    background: 'var(--status-warn-bg-soft, #fff8e1)',
                    border: '1px solid var(--status-warn-border, #e6a23c)',
                    color: 'var(--status-warn-dark, #7a5200)',
                  }}
                >
                  <span className="font-bold">Split warning：</span> {row.splitWarning}
                </div>
              ) : null}
              {(() => {
                // axis ⇔ duplicateOf 互鎖檢查：B 方案 prompt 規定
                // axis === 'none' 必須 ⇔ duplicateOf 有值。AI 違規時亮警告，
                // 讓 reviewer 知道 AI 自己邏輯打架，需要人工確認。
                const axis = row.splitDecision?.distinguishingAxis;
                const dup = row.splitDecision?.duplicateOf;
                const axisIsNone = axis?.axis === 'none';
                const hasDup = !!dup;
                const inconsistent = axis && (axisIsNone !== hasDup);
                if (!inconsistent) return null;
                const reason = axisIsNone
                  ? 'AI 宣告 axis="none"（真重複）但未填 duplicate_of —— 請人工確認是否真為重複。'
                  : `AI 宣告差異 axis="${axis?.axis}" 但同時填了 duplicate_of —— 兩者矛盾，請人工確認。`;
                return (
                  <div
                    className="paper-card p-2 text-xs flex items-start gap-2"
                    style={{
                      background: 'var(--status-warn-bg-soft, #fff8e1)',
                      border: '1px solid var(--status-warn-border, #e6a23c)',
                      color: 'var(--status-warn-dark, #7a5200)',
                    }}
                    title="B 方案互鎖規則：axis === 'none' ⇔ duplicate_of 有值。違反代表 AI 邏輯不一致。"
                  >
                    <span className="font-bold shrink-0">⚠ Sibling 判定不一致</span>
                    <span className="leading-relaxed">{reason}</span>
                  </div>
                );
              })()}
              {(() => {
                const axis = row.splitDecision?.distinguishingAxis;
                // axis === 'none' 走 duplicate badge，這裡跳過避免重複；無資料也跳過。
                if (!axis || axis.axis === 'none' || (!axis.axis && !axis.delta)) {
                  return null;
                }
                const AXIS_LABELS: Record<string, string> = {
                  trigger_state: '觸發狀態',
                  input_data: '輸入資料',
                  timing: '時序',
                  boundary: '邊界值',
                  mode: '模式',
                };
                const label = AXIS_LABELS[axis.axis] ?? axis.axis;
                return (
                  <div
                    className="paper-card p-2 text-xs flex items-start gap-2"
                    style={{
                      background: 'var(--win95-gray-light, #f0f0f0)',
                      border: '1px solid var(--win95-gray-dark)',
                      color: 'var(--win95-black)',
                    }}
                    title={`AI 對 sibling 差異的明確聲明（axis=${axis.axis}）；reviewer 可用此核對 tc_title 是否真有體現該差異。`}
                  >
                    <span className="font-bold shrink-0">⚖ 與 sibling 差異</span>
                    <span
                      className="font-bold shrink-0"
                      style={{ color: 'var(--win95-navy)' }}
                    >
                      ({label})
                    </span>
                    <span className="leading-relaxed">{axis.delta}</span>
                  </div>
                );
              })()}
              {row.splitDecision?.duplicateOf ? (
                (() => {
                  // backend 已把 AI 回的值解析成 row_num（純數字字串），對不到
                  // sibling 時 backend 直接清空 → 不會走到這個分支。
                  const siblingRowNum = row.splitDecision.duplicateOf;
                  const siblingTcId = resolveSiblingTcId?.(siblingRowNum);
                  return (
                    <div
                      className="paper-card p-2 text-xs flex items-start gap-2"
                      style={{
                        background: 'var(--status-reject-bg-soft, #fde8e8)',
                        border: '1px solid var(--status-reject-border, #d04444)',
                        color: 'var(--status-reject-dark, #7a1f1f)',
                      }}
                      title="AI 嚴格判定本列與 sibling 完全等價（相同 trigger / outcome / input bucket / 驗證目標）。建議刪除本列或合併到對方。"
                    >
                      <span className="font-bold shrink-0">⊕ 重複於</span>
                      <span className="font-bold">row #{siblingRowNum}</span>
                      {siblingTcId ? (
                        <span className="font-bold" style={{ color: 'var(--win95-gray-darker)' }}>
                          ({siblingTcId})
                        </span>
                      ) : null}
                      <span className="leading-relaxed">
                        — AI 嚴格判定與該列完全等價；請比對後決定是否刪除本列。
                      </span>
                    </div>
                  );
                })()
              ) : null}
              {row.splitDecision && (row.splitDecision.subIndex ?? 0) > 0 ? (
                // Sub TC：顯示小 badge，指回 primary（同一 req 的 TC 1/N）。
                <div
                  className="paper-card p-2 text-xs flex items-center gap-2"
                  style={{
                    background: 'var(--win95-gray-light, #f0f0f0)',
                    border: '1px solid var(--win95-gray-dark)',
                  }}
                >
                  <RiLightbulbLine className="size-3 shrink-0" />
                  <span>
                    屬於 <span className="font-bold">{row.splitDecision.reqId}</span> 的
                    {' '}TC {(row.splitDecision.subIndex ?? 0) + 1}
                    /{row.splitDecision.tcCount}
                    （完整拆分決策見第 1 筆 TC 的展開面板）
                  </span>
                </div>
              ) : row.splitDecision && (row.splitDecision.reasoning || row.splitDecision.keywords.length > 0) ? (
                // Primary：顯示完整 reasoning + keywords。
                // tcCount === 1（atomic）也要顯示，讓使用者看到 AI 如何理解這個需求。
                <div className="border-sunken">
                  <div
                    className="flex items-center gap-2 px-2 py-1 text-xs font-bold"
                    style={{ background: 'var(--win95-navy)', color: 'var(--win95-white)' }}
                  >
                    <RiLightbulbLine className="size-3 shrink-0" />
                    <span>
                      {row.splitDecision.tcCount > 1
                        ? `AI 的需求解讀 — 拆成 ${row.splitDecision.tcCount} 筆 TC（${row.splitDecision.reqId}）`
                        : `AI 的需求解讀 — 原子需求，不需拆分（${row.splitDecision.reqId}）`}
                    </span>
                  </div>
                  <div
                    className="p-2 flex flex-col gap-2 text-xs"
                    style={{ background: 'var(--win95-white)' }}
                  >
                    {row.splitDecision.reasoning ? (
                      <p className="leading-relaxed whitespace-pre-wrap selectable">
                        {row.splitDecision.reasoning}
                      </p>
                    ) : (
                      <p style={{ color: 'var(--text-muted)' }}>（AI 未提供需求解讀）</p>
                    )}
                    {row.splitDecision.keywords.length > 0 && (
                      <div className="flex flex-col gap-1">
                        <div
                          className="flex items-center gap-1 text-[11px] font-bold"
                          style={{ color: 'var(--text-muted)' }}
                        >
                          <RiKey2Line className="size-3" />
                          Keyword coverage (§10.2)
                        </div>
                        <ul className="flex flex-col gap-1 pl-1">
                          {row.splitDecision.keywords.map((k, idx) => (
                            <li key={`${k.keyword}-${idx}`} className="leading-snug">
                              <span className="font-bold">{k.keyword}</span>
                              {k.meaning ? <>：{k.meaning}</> : null}
                              {k.coveredBy.length > 0 ? (
                                <span style={{ color: 'var(--text-muted)' }}>
                                  {' '}
                                  → TC {k.coveredBy.join(', ')}
                                </span>
                              ) : null}
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                </div>
              ) : null}
              <div className="grid grid-cols-5 gap-3">
                {/* Left: Original (40%) */}
                <div className="col-span-2 flex flex-col">
                  <TitleBarMini
                    icon={<RiFileTextLine className="size-3" />}
                    title="Original Requirement"
                  />
                  <div
                    className="paper-card flex-1 p-3 text-xs leading-relaxed overflow-auto whitespace-pre-wrap break-words selectable"
                    style={{ minHeight: 140 }}
                  >
                    {row.testItem}
                  </div>
                </div>

                {/* Right: Generated / Editable (60%) */}
                <div className="col-span-3 flex flex-col">
                  <TitleBarMini
                    icon={<RiEditBoxLine className="size-3" />}
                    title={
                      isEditing ? 'Generated Test Case — EDIT MODE' : 'Generated Test Case'
                    }
                    variant={isEditing ? 'edit' : 'default'}
                  />
                  <div className={`paper-card ${isEditing ? 'edit-mode' : ''}`}>
                    {isEditing ? (
                      <div className="flex flex-col">
                        <StackedEditField
                          label="Pre-Conditions"
                          value={editValues.preConditions}
                          onChange={(v) => onEditValuesChange({ ...editValues, preConditions: v })}
                        />
                        <StackedEditField
                          label="Input Test Data"
                          value={editValues.inputTestData}
                          onChange={(v) => onEditValuesChange({ ...editValues, inputTestData: v })}
                        />
                        <StackedEditField
                          label="Test Procedure"
                          value={editValues.steps}
                          onChange={(v) => onEditValuesChange({ ...editValues, steps: v })}
                          minHeight={80}
                        />
                        <StackedEditField
                          label="Expected Result"
                          value={editValues.expected}
                          onChange={(v) => onEditValuesChange({ ...editValues, expected: v })}
                        />
                        <StackedEditDropdown
                          label="Design Method"
                          value={editValues.designMethod}
                          options={DESIGN_METHODS}
                          placeholder="— 選擇 ASPICE 設計方法 —"
                          onChange={(v) => onEditValuesChange({ ...editValues, designMethod: v })}
                        />
                        <StackedEditDropdown
                          label="Priority"
                          value={editValues.priority}
                          options={PRIORITY_OPTIONS}
                          placeholder="— 選擇優先級 —"
                          onChange={(v) => onEditValuesChange({ ...editValues, priority: v })}
                        />
                      </div>
                    ) : (
                      <div className="flex flex-col">
                        <StackedReadField
                          label="TC Title"
                          value={row.tcTitle ?? ''}
                        />
                        <StackedReadField label="Pre-Conditions" value={row.preConditions} />
                        <StackedReadField label="Input Test Data" value={row.inputTestData} muted />
                        <StackedReadField label="Test Procedure" value={row.steps} />
                        <StackedReadField label="Expected Result" value={row.expectedResults} />
                        <StackedReadField
                          label="Design Method"
                          value={row.designMethod ?? ''}
                          muted={!row.designMethod}
                        />
                        <StackedReadField
                          label="Priority"
                          value={row.priority ?? ''}
                          muted={!row.priority}
                        />
                        {row.specReference && (
                          <StackedReadField label="Spec Reference" value={row.specReference} muted />
                        )}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          )}

          {!row.awaitingApply && (
            <div className="mt-3 flex justify-end gap-2">
              {isEditing ? (
                <>
                  <Button
                    className="flex items-center gap-1 text-xs px-3 py-1"
                    onClick={onCancelEdit}
                  >
                    <RiArrowGoBackLine className="size-3" /> Cancel
                  </Button>
                  <Button
                    className="flex items-center gap-1 text-xs px-3 py-1 default"
                    onClick={() => onSaveEdit(row.id)}
                  >
                    <RiSaveLine className="size-3" /> Save Changes
                  </Button>
                </>
              ) : (
                <>
                  <Button
                    className="flex items-center gap-1 text-xs px-3 py-1"
                    onClick={() => onStartEdit(row)}
                  >
                    <RiEditLine className="size-3" /> Manual Edit
                  </Button>
                  <Button
                    className={`flex items-center gap-1 text-xs px-3 py-1 ${
                      row.status === 'flagged' ? 'font-bold' : ''
                    }`}
                    style={
                      row.status === 'flagged'
                        ? { background: 'var(--status-warn)', color: 'var(--win95-black)' }
                        : { color: 'var(--edit-accent-fg)' }
                    }
                    onClick={() => onToggleFlag(row.id, row.status)}
                  >
                    {row.status === 'flagged' ? (
                      <RiFlagFill className="size-3" />
                    ) : (
                      <RiFlagLine className="size-3" />
                    )}
                    {row.status === 'flagged' ? 'Unflag' : 'Flag for Human'}
                  </Button>
                </>
              )}
            </div>
          )}
        </td>
      </tr>
    )}
  </>
  );
};

export default ReviewRow;
