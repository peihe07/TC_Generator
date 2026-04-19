'use client';

import React, { useEffect, useRef, useState } from 'react';
import { useJobHistoryStore } from '../../store/useJobHistoryStore';

function fmtDate(ts: number): string {
  const d = new Date(ts);
  return d.toLocaleString([], { month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' });
}

function fmtDuration(ms: number): string {
  const s = Math.round(ms / 1000);
  if (s < 60) return `${s}s`;
  const m = Math.floor(s / 60);
  const rem = s % 60;
  return `${m}m${rem}s`;
}

const JobHistoryMenu: React.FC = () => {
  const { records, loaded, loadFromStorage, clearHistory } = useJobHistoryStore();
  const [open, setOpen] = useState(false);
  const popRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  useEffect(() => {
    const h = (e: MouseEvent) => {
      if (popRef.current && !popRef.current.contains(e.target as Node)) setOpen(false);
    };
    if (open) document.addEventListener('mousedown', h);
    return () => document.removeEventListener('mousedown', h);
  }, [open]);

  const totalCost = records.reduce((s, r) => s + (r.cost || 0), 0);
  const totalTokens = records.reduce((s, r) => s + (r.inputTokens || 0) + (r.outputTokens || 0), 0);

  const handleClear = () => {
    if (!window.confirm(`Clear all ${records.length} history entries?`)) return;
    clearHistory();
  };

  return (
    <div ref={popRef} style={{ position: 'relative' }}>
      <button
        style={{ height: 22, padding: '0 8px', maxWidth: 180 }}
        onClick={() => setOpen((v) => !v)}
        title={`Job history — total spent $${totalCost.toFixed(4)}`}
      >
        📊 ${totalCost.toFixed(4)}
      </button>

      {open && (
        <div
          style={{
            position: 'absolute',
            bottom: 26,
            right: 0,
            width: 380,
            maxHeight: 400,
            background: 'var(--win95-gray)',
            border: '2px solid',
            borderColor: 'var(--win95-white) var(--win95-gray-mid) var(--win95-gray-mid) var(--win95-white)',
            boxShadow: '2px 2px 0 var(--win95-black)',
            padding: 4,
            zIndex: 10000,
            display: 'flex',
            flexDirection: 'column',
            gap: 4,
          }}
        >
          {/* Aggregate header */}
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '4px 6px',
            background: 'var(--win95-navy)',
            color: 'var(--win95-white)',
            fontWeight: 'bold',
            fontSize: 12,
          }}>
            <span>Job History ({records.length})</span>
            <span style={{ fontFamily: 'monospace' }}>
              ${totalCost.toFixed(4)} · {totalTokens.toLocaleString()} tok
            </span>
          </div>

          <div style={{ display: 'flex', gap: 4 }}>
            <button onClick={handleClear} disabled={records.length === 0} style={{ flex: 1 }}>
              Clear History
            </button>
          </div>

          {/* Records */}
          <div style={{
            overflowY: 'auto',
            maxHeight: 300,
            background: 'var(--win95-white)',
            border: '1px solid var(--win95-gray-mid)',
          }}>
            {records.length === 0 && (
              <div style={{ padding: 12, fontSize: 11, color: 'var(--text-muted)', textAlign: 'center' }}>
                No jobs recorded yet. Run Generate or Quick TC to build history.
              </div>
            )}
            {records.map((r) => {
              const totalIn = r.inputTokens + r.cacheCreationTokens + r.cacheReadTokens;
              const hitRate = totalIn > 0 ? (r.cacheReadTokens / totalIn) * 100 : 0;
              return (
                <div
                  key={r.id + r.startedAt}
                  style={{
                    padding: '4px 6px',
                    borderBottom: '1px solid var(--win95-gray-lighter)',
                    fontSize: 11,
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontWeight: 'bold' }}>
                    <span style={{ color: 'var(--win95-navy)' }}>{r.model}</span>
                    <span style={{ fontFamily: 'monospace', color: 'var(--status-reject-dark)' }}>${r.cost.toFixed(5)}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', marginTop: 1 }}>
                    <span>{fmtDate(r.startedAt)} · {fmtDuration(r.finishedAt - r.startedAt)}</span>
                    <span>{r.rowsProcessed}/{r.rowsTotal} rows</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-muted)', fontSize: 10, marginTop: 1, fontFamily: 'monospace' }}>
                    <span>in {r.inputTokens.toLocaleString()} · out {r.outputTokens.toLocaleString()}</span>
                    {hitRate > 0 && <span>cache {hitRate.toFixed(0)}%</span>}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};

export default JobHistoryMenu;
