import React from 'react';
import { RiLoader4Line, RiRefreshLine } from '@remixicon/react';
import { Button } from '../../ui';
import type { TcRow } from '../../../lib/types';
import type { GroupPreviewState } from './types';

export interface GroupingTabProps {
  tcRows: TcRow[];
  setTcRows: (rows: TcRow[]) => void;
  preview: GroupPreviewState | null;
  isLoading: boolean;
  error: string | null;
  onGroup: () => void;
  onApply: () => void;
  /** Called when a row's Test Set is edited inline so the preview can invalidate. */
  onInvalidatePreview: () => void;
}

/**
 * Tab 1 — Grouping. Shows the derived test-set preview table plus a
 * scrollable manual override grid that writes directly to `tcRows`.
 */
export const GroupingTab: React.FC<GroupingTabProps> = ({
  tcRows,
  setTcRows,
  preview,
  isLoading,
  error,
  onGroup,
  onApply,
  onInvalidatePreview,
}) => (
  <>
    <div className="mb-2">
      <div className="mb-2">
        <p className="font-bold">Test Sets — review, edit, then apply before generation.</p>
        <p className="text-[11px]" style={{ color: 'var(--text-muted)' }}>
          Upload 後不會自動分組。按 Group 會依現有內容與 hints 重新分類全部列；想改就在「Manual Override」直接編輯。
          生成完的 TC 會沿用這裡的 Test Set。
        </p>
      </div>
      <div
        className="flex flex-wrap items-center justify-between gap-2 border-sunken p-2"
        style={{ background: 'var(--win95-gray-lighter)' }}
      >
        <div className="flex flex-wrap items-center gap-2 min-w-0">
          <Button
            className="flex items-center justify-center gap-1 min-w-[118px]"
            onClick={onGroup}
            disabled={isLoading}
            title="Send existing test sets as hints and regroup every row"
          >
            {isLoading ? (
              <RiLoader4Line className="size-3 animate-spin" />
            ) : (
              <RiRefreshLine className="size-3" />
            )}
            Group
          </Button>
        </div>
        <Button onClick={onApply} disabled={!preview || isLoading} className="default min-w-[112px]">
          Apply
        </Button>
      </div>
    </div>

    {error && (
      <div
        className="status-bar-field p-1 mb-2"
        style={{
          color: 'var(--status-reject-dark)',
          background: 'var(--status-error-bg-soft)',
        }}
      >
        {error}
      </div>
    )}
    {isLoading && (
      <div className="status-bar-field p-1 mb-2 flex items-center gap-1">
        <RiLoader4Line className="size-3 animate-spin" />
        Group is regrouping all rows...
      </div>
    )}
    {preview && (
      <div className="status-bar-field p-1 mb-2">
        Grouped {preview.assignments.length} row(s) into {preview.groups.length} Test Set(s).
        Apply once you&apos;re happy with the labels below.
      </div>
    )}

    <table className="w-full border-collapse mb-3">
      <thead>
        <tr>
          <th className="win95-th">Test Set</th>
          <th className="win95-th">Count</th>
          <th className="win95-th">Requirement IDs</th>
        </tr>
      </thead>
      <tbody>
        {preview?.groups.length ? (
          preview.groups.map((group) => (
            <tr key={group.testSet}>
              <td className="p-1 font-mono">{group.testSet}</td>
              <td className="p-1 font-mono">{group.count}</td>
              <td className="p-1">{group.reqIds.join(', ')}</td>
            </tr>
          ))
        ) : (
          <tr>
            <td
              colSpan={3}
              className="p-4 text-center"
              style={{ color: 'var(--win95-gray-mid)', fontStyle: 'italic' }}
            >
              {isLoading ? 'Loading grouping preview...' : 'No grouping preview yet. Click Group or edit Test Set manually.'}
            </td>
          </tr>
        )}
      </tbody>
    </table>

    {/* Per-row manual override — writes directly to tcRows */}
    {tcRows.length > 0 && (
      <>
        <div className="flex items-center justify-between mb-1 mt-3">
          <p
            className="font-bold text-xs uppercase"
            style={{ color: 'var(--text-muted)' }}
          >
            Manual Override — edit any row&apos;s test set directly
          </p>
          <span className="text-[10px]" style={{ color: 'var(--text-muted)' }}>
            Changes are saved immediately. Use the datalist for existing sets or type a new one.
          </span>
        </div>
        <datalist id="existing-test-sets">
          {[...new Set(tcRows.map((r) => r.testSet).filter(Boolean))].map((ts) => (
            <option key={ts} value={ts} />
          ))}
          {preview?.groups.map((g) => (
            <option key={`grp-${g.testSet}`} value={g.testSet} />
          ))}
        </datalist>
        <div
          className="border-sunken"
          style={{
            maxHeight: 260,
            overflowY: 'auto',
            background: 'var(--win95-white)',
          }}
        >
          <table className="w-full border-collapse text-xs">
            <thead className="sticky top-0" style={{ zIndex: 1 }}>
              <tr>
                <th className="win95-th" style={{ width: 120 }}>
                  Req ID
                </th>
                <th className="win95-th">Test Item</th>
                <th className="win95-th" style={{ width: 160 }}>
                  Test Set
                </th>
              </tr>
            </thead>
            <tbody>
              {tcRows.map((row) => (
                <tr key={row.id}>
                  <td className="p-1 font-mono">{row.reqId}</td>
                  <td
                    className="p-1"
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
                      onBlur={onInvalidatePreview}
                      style={{
                        width: '100%',
                        border: 'none',
                        padding: '2px 4px',
                        fontSize: 11,
                      }}
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
);

export default GroupingTab;
