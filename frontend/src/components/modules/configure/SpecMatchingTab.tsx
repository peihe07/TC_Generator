import React, { useMemo } from 'react';
import { RiLoader4Line, RiRefreshLine } from '@remixicon/react';
import { Button } from '../../ui';
import type { MatchPreviewState } from './types';

export interface SpecMatchingTabProps {
  preview: MatchPreviewState | null;
  isLoading: boolean;
  error: string | null;
  onRefresh: () => void;
}

/**
 * Tab 2 — Spec Matching. Shows traceability from TC rows to an optional
 * reference workbook, with exact / fuzzy / unmatched counts.
 */
export const SpecMatchingTab: React.FC<SpecMatchingTabProps> = ({
  preview,
  isLoading,
  error,
  onRefresh,
}) => {
  const exactMatchRatio = useMemo(() => {
    if (!preview?.summary.total) return 0;
    return Math.round((preview.summary.exact / preview.summary.total) * 100);
  }, [preview]);

  return (
    <>
      <div className="flex items-center justify-between mb-2">
        <div className="flex flex-col gap-1">
          <span>Exact traceability preview from the optional reference workbook.</span>
          {preview && (
            <span style={{ color: 'var(--text-muted)' }}>
              Exact matches: {preview.summary.exact}/{preview.summary.total} ({exactMatchRatio}%)
            </span>
          )}
        </div>
        <Button className="flex items-center gap-1" onClick={onRefresh}>
          {isLoading ? (
            <RiLoader4Line className="size-3 animate-spin" />
          ) : (
            <RiRefreshLine className="size-3" />
          )}
          Refresh
        </Button>
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
      {preview && (
        <div className="status-bar-field p-1 mb-2">
          {preview.summary.hasReferenceWorkbook
            ? `Reference workbook loaded. ${preview.summary.exact} exact, ${preview.summary.fuzzy} fuzzy (token similarity), ${preview.summary.unmatched} unmatched.`
            : 'No compatible reference workbook loaded.'}
        </div>
      )}

      <table className="w-full border-collapse">
        <thead>
          <tr>
            <th className="win95-th">Req ID</th>
            <th className="win95-th">Test Item</th>
            <th className="win95-th">Matched Spec</th>
            <th className="win95-th">Status</th>
          </tr>
        </thead>
        <tbody>
          {preview?.matches.length ? (
            preview.matches.map((row) => (
              <tr key={row.id}>
                <td className="p-1 font-mono">{row.reqId}</td>
                <td
                  className="p-1"
                  style={{
                    maxWidth: 220,
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {row.testItem}
                </td>
                <td className="p-1 font-mono">{row.specReference || '—'}</td>
                <td
                  className="p-1 font-bold"
                  style={{
                    color:
                      row.matchType === 'exact'
                        ? 'var(--status-accept-dark)'
                        : row.matchType === 'fuzzy'
                          ? 'var(--status-warn-dark)'
                          : 'var(--win95-gray-mid)',
                  }}
                >
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
              <td
                colSpan={4}
                className="p-4 text-center"
                style={{ color: 'var(--win95-gray-mid)', fontStyle: 'italic' }}
              >
                {isLoading
                  ? 'Loading spec matching preview...'
                  : 'No spec matching preview available yet.'}
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </>
  );
};

export default SpecMatchingTab;
