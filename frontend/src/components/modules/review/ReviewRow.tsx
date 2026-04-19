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
  RiRefreshLine,
  RiSaveLine,
} from '@remixicon/react';
import { TcRow } from '../../../lib/types';
import {
  Button,
  IconButton,
  StatusBadge,
  TitleBarMini,
  type StatusVariant,
} from '../../ui';
import { RegenDiff, type DiffFieldKey } from './RegenDiff';
import { StackedEditField, StackedReadField } from './StackedFields';

export interface EditValues {
  steps: string;
  expected: string;
  preConditions: string;
  inputTestData: string;
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
}) => (
  <>
    <tr
      className={`cursor-pointer win95-row
        ${isActive || isSelected ? 'selected' : ''}
        ${row.status === 'flagged' && !isActive && !isSelected ? 'bg-orange-50' : ''}
        ${row.pendingRegenerated && !isActive && !isSelected ? 'bg-yellow-50' : ''}
      `}
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
        className="px-3 py-2 border-r font-mono text-xs"
        onClick={() => onToggleExpand(row.id)}
      >
        <span className="flex items-center gap-1">
          {row.status === 'flagged' && <RiFlagFill className="size-3 text-orange-600" />}
          {row.pendingRegenerated && <RiRefreshLine className="size-3 text-yellow-600" />}
          {row.id}
        </span>
      </td>
      <td
        className="px-3 py-2 border-r font-mono text-xs"
        onClick={() => onToggleExpand(row.id)}
      >
        {row.reqId}
      </td>
      <td className="px-3 py-2 border-r" onClick={() => onToggleExpand(row.id)}>
        <StatusBadge
          status={row.pendingRegenerated ? 'reviewing' : (row.status as StatusVariant)}
          style={row.status === 'generating' ? { animation: 'agent-pulse 1s ease-in-out infinite' } : undefined}
        >
          {row.pendingRegenerated ? 'awaiting apply' : row.status}
        </StatusBadge>
      </td>

      <td className="p-0 border-r cell-center" onClick={(e) => e.stopPropagation()}>
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
          {row.pendingRegenerated ? (
            <RegenDiff
              row={row}
              onApply={(fields) => onApplyRegen(row.id, fields)}
              onDiscard={() => onDiscardRegen(row.id)}
            />
          ) : (
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
                    </div>
                  ) : (
                    <div className="flex flex-col">
                      <StackedReadField
                        label="Test Item Rewrite"
                        value={row.testItemRewrite ?? ''}
                      />
                      <StackedReadField label="Pre-Conditions" value={row.preConditions} />
                      <StackedReadField label="Input Test Data" value={row.inputTestData} muted />
                      <StackedReadField label="Test Procedure" value={row.steps} />
                      <StackedReadField label="Expected Result" value={row.expectedResults} />
                      {row.specReference && (
                        <StackedReadField label="Spec Reference" value={row.specReference} muted />
                      )}
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}

          {!row.pendingRegenerated && (
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
                    className="flex items-center gap-1 text-xs px-3 py-1 font-bold default"
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

export default ReviewRow;
