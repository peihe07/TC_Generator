import React, { useState } from 'react';
import {
  RiArrowGoBackLine,
  RiCheckFill,
  RiCheckboxBlankLine,
  RiCheckboxLine,
  RiEditBoxLine,
  RiFileTextLine,
  RiRefreshLine,
} from '@remixicon/react';
import { TcRow } from '../../../lib/types';
import { Button, TitleBarMini } from '../../ui';
import { diffTokens } from './diffTokens';
import { DiffText } from './DiffText';

export type DiffFieldKey = 'preConditions' | 'inputTestData' | 'steps' | 'expectedResults';

const DIFF_FIELDS: { key: DiffFieldKey; label: string }[] = [
  { key: 'preConditions', label: 'Pre-Conditions' },
  { key: 'inputTestData', label: 'Input Test Data' },
  { key: 'steps', label: 'Test Procedure' },
  { key: 'expectedResults', label: 'Expected Result' },
];

export interface RegenDiffProps {
  row: TcRow;
  onApply: (fields: DiffFieldKey[]) => void;
  onDiscard: () => void;
}

/**
 * Side-by-side diff for a regenerated row. User can cherry-pick which
 * fields to apply from `row.pendingRegenerated` back into the row.
 */
export const RegenDiff: React.FC<RegenDiffProps> = ({ row, onApply, onDiscard }) => {
  const [selected, setSelected] = useState<Set<DiffFieldKey>>(
    new Set(['preConditions', 'inputTestData', 'steps', 'expectedResults']),
  );

  const toggle = (field: DiffFieldKey) => {
    setSelected((prev) => {
      const next = new Set(prev);
      next.has(field) ? next.delete(field) : next.add(field);
      return next;
    });
  };

  return (
    <div
      className="paper-card p-3 mt-2"
      style={{
        borderColor:
          'var(--status-edit) var(--status-edit) var(--status-edit) var(--status-edit)',
      }}
    >
      <TitleBarMini
        variant="edit"
        className="-mx-3 -mt-3 mb-3"
        style={{ padding: '4px 10px' }}
        icon={<RiRefreshLine className="size-3" />}
        title="New Version Ready — Select fields to apply"
      >
        <Button
          className="text-xs"
          style={{ minHeight: 20, padding: '1px 8px' }}
          onClick={onDiscard}
        >
          <RiArrowGoBackLine className="size-3 inline mr-1" />
          Discard
        </Button>
        <Button
          className="text-xs font-bold default"
          style={{ minHeight: 20, padding: '1px 10px' }}
          onClick={() => onApply([...selected])}
          disabled={selected.size === 0}
        >
          <RiCheckFill className="size-3 inline mr-1" />
          Apply Selected
        </Button>
      </TitleBarMini>

      <div className="flex flex-col gap-2">
        {DIFF_FIELDS.map(({ key, label }) => {
          const oldVal = row[key] || '';
          const newVal = row.pendingRegenerated?.[key] || '';
          const changed = oldVal !== newVal;
          const isSelected = selected.has(key);
          const { left, right } = changed ? diffTokens(oldVal, newVal) : { left: [], right: [] };

          return (
            <div
              key={key}
              style={{
                border: '2px solid',
                borderColor: isSelected
                  ? 'var(--win95-gray-mid) var(--win95-white) var(--win95-white) var(--win95-gray-mid)'
                  : 'var(--win95-gray) var(--win95-gray-lighter) var(--win95-gray-lighter) var(--win95-gray)',
                background: 'var(--win95-white)',
                opacity: isSelected ? 1 : 0.55,
              }}
            >
              <div
                className="flex items-center gap-2 px-2 py-1 cursor-pointer"
                style={{
                  background: 'var(--field-header-bg)',
                  borderBottom: '1px solid var(--win95-gray)',
                }}
                onClick={() => toggle(key)}
              >
                {isSelected ? (
                  <RiCheckboxLine className="size-4 text-orange-600 shrink-0" />
                ) : (
                  <RiCheckboxBlankLine className="size-4 text-gray-400 shrink-0" />
                )}
                <span className="text-[10px] font-bold uppercase text-gray-700">{label}</span>
                {changed ? (
                  <span
                    className="ml-auto text-[9px] px-1 font-bold uppercase"
                    style={{
                      background: 'var(--edit-accent-bg)',
                      color: 'var(--edit-accent-fg)',
                      border: '1px solid var(--status-edit)',
                    }}
                  >
                    Changed
                  </span>
                ) : (
                  <span
                    className="ml-auto text-[9px] px-1 uppercase"
                    style={{
                      background: 'var(--win95-gray-lighter)',
                      color: 'var(--win95-gray-dark)',
                      border: '1px solid var(--win95-gray)',
                    }}
                  >
                    Unchanged
                  </span>
                )}
              </div>
              {changed ? (
                <div
                  className="grid grid-cols-2"
                  style={{ borderTop: '1px solid var(--win95-gray-lighter)' }}
                >
                  <div
                    className="p-2 text-[11px] leading-relaxed selectable"
                    style={{
                      borderRight: '1px solid var(--win95-gray-lighter)',
                      background: 'var(--diff-remove-bg)',
                    }}
                  >
                    <div
                      className="text-[9px] font-bold uppercase mb-1"
                      style={{ color: 'var(--diff-remove-fg)' }}
                    >
                      <RiFileTextLine className="size-3 inline mr-1" />
                      Current (strikethrough = removed)
                    </div>
                    <DiffText tokens={left} />
                  </div>
                  <div
                    className="p-2 text-[11px] leading-relaxed selectable"
                    style={{ background: 'var(--diff-add-bg)' }}
                  >
                    <div
                      className="text-[9px] font-bold uppercase mb-1"
                      style={{ color: 'var(--diff-add-fg)' }}
                    >
                      <RiEditBoxLine className="size-3 inline mr-1" />
                      New (highlighted = added)
                    </div>
                    <DiffText tokens={right} />
                  </div>
                </div>
              ) : (
                <div
                  className="p-2 text-[11px] text-gray-600 selectable whitespace-pre-wrap"
                  style={{ borderTop: '1px solid var(--win95-gray-lighter)' }}
                >
                  {oldVal || '—'}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default RegenDiff;
