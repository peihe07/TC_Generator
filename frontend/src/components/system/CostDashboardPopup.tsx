'use client';

import React, { useEffect, useState } from 'react';
import { RiCloseLine, RiRefreshLine } from '@remixicon/react';

interface AggregateMetrics {
  jobCount: number;
  totalRowCount: number;
  totalCostUsd: number | null;
  avgCostUsd: number | null;
  avgRowCount: number | null;
  matchRate: number | null;
  jobsWithCost: number;
  jobsWithMatch: number;
}

interface Props {
  onClose: () => void;
}

/**
 * 跨 job 成本觀測面板。讀 `GET /api/metrics/aggregate`（背後呼叫
 * `aggregate_metrics_tool`）。fetch-on-mount；手動 refresh。
 */
export default function CostDashboardPopup({ onClose }: Props) {
  const [data, setData] = useState<AggregateMetrics | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const load = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/metrics/aggregate');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const json: AggregateMetrics = await res.json();
      setData(json);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, []);

  return (
    <div className="cost-dashboard-popup" role="dialog" aria-label="Cost Dashboard">
      {/* Title bar */}
      <div className="cost-dashboard-titlebar">
        <span>Cost Dashboard</span>
        <div className="cost-dashboard-actions">
          <button
            type="button"
            className="cost-dashboard-btn"
            aria-label="Refresh"
            onClick={load}
            disabled={loading}
          >
            <RiRefreshLine size={12} className={loading ? 'spin' : ''} />
          </button>
          <button
            type="button"
            className="cost-dashboard-btn"
            aria-label="Close"
            onClick={onClose}
          >
            <RiCloseLine size={12} />
          </button>
        </div>
      </div>

      {/* Body */}
      <div className="cost-dashboard-body">
        {error && (
          <div className="cost-dashboard-error">
            讀取失敗：{error}
          </div>
        )}
        {!error && loading && !data && (
          <div className="cost-dashboard-hint">載入中…</div>
        )}
        {data && (
          <>
            <MetricRow label="Jobs" value={data.jobCount.toString()} />
            <MetricRow label="Total Rows" value={data.totalRowCount.toLocaleString()} />
            <MetricRow
              label="Avg Rows/Job"
              value={data.avgRowCount !== null ? data.avgRowCount.toFixed(1) : '—'}
            />

            <div className="cost-dashboard-divider" />

            <MetricRow
              label="Total Cost"
              value={
                data.totalCostUsd !== null
                  ? `$${data.totalCostUsd.toFixed(4)}`
                  : '—'
              }
              emphasis
            />
            <MetricRow
              label="Avg Cost/Job"
              value={
                data.avgCostUsd !== null
                  ? `$${data.avgCostUsd.toFixed(4)}`
                  : '—'
              }
              sub={
                data.jobsWithCost > 0 && data.jobsWithCost < data.jobCount
                  ? `(${data.jobsWithCost}/${data.jobCount} 有 cost 資料)`
                  : undefined
              }
            />

            <div className="cost-dashboard-divider" />

            <MetricRow
              label="Spec Match Rate"
              value={
                data.matchRate !== null
                  ? `${(data.matchRate * 100).toFixed(1)}%`
                  : '—'
              }
              sub={
                data.jobsWithMatch > 0
                  ? `(${data.jobsWithMatch} jobs 有 match 資料)`
                  : undefined
              }
            />
          </>
        )}
      </div>
    </div>
  );
}

const MetricRow: React.FC<{
  label: string;
  value: string;
  sub?: string;
  emphasis?: boolean;
}> = ({ label, value, sub, emphasis }) => (
  <div className="cost-dashboard-row">
    <span className="cost-dashboard-row-label">{label}</span>
    <span
      className={`cost-dashboard-row-value ${emphasis ? 'cost-dashboard-row-value-emphasis' : ''}`}
    >
      {value}
      {sub && <span className="cost-dashboard-row-sub">{sub}</span>}
    </span>
  </div>
);
