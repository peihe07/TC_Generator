'use client';

import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  useJobHistoryStore,
  type JobRecord,
  type JobRecordKind,
} from '../../store/useJobHistoryStore';
import { Button } from '../ui';

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

const KIND_LABEL: Record<JobRecordKind, string> = {
  generate: 'Generate',
  quick: 'Quick TC',
  group: 'Grouping',
  regenerate: 'Regenerate',
  rerun: 'Re-run',
  'suggest-fix': 'Suggest-Fix',
  export: 'Export',
};

interface Subtotal {
  cost: number;
  inputTokens: number;
  outputTokens: number;
  count: number;
}

function aggregate<K extends string>(
  records: JobRecord[],
  keyFn: (r: JobRecord) => K,
): Array<[K, Subtotal]> {
  const map = new Map<K, Subtotal>();
  for (const r of records) {
    const k = keyFn(r);
    const cur = map.get(k) ?? { cost: 0, inputTokens: 0, outputTokens: 0, count: 0 };
    cur.cost += r.cost || 0;
    cur.inputTokens += r.inputTokens || 0;
    cur.outputTokens += r.outputTokens || 0;
    cur.count += 1;
    map.set(k, cur);
  }
  return [...map.entries()].sort((a, b) => b[1].cost - a[1].cost);
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
  const totalCacheRead = records.reduce((s, r) => s + (r.cacheReadTokens || 0), 0);

  // Per-kind / per-model 累計，給 reviewer 看「錢花在哪」。
  const byKind = useMemo(
    () => aggregate(records, (r) => r.kind),
    [records],
  );
  const byModel = useMemo(
    () => aggregate(records, (r) => r.model || '(unknown)'),
    [records],
  );

  const handleClear = () => {
    if (!window.confirm(`Clear all ${records.length} history entries?`)) return;
    clearHistory();
  };

  return (
    <div ref={popRef} style={{ position: 'relative' }}>
      <Button
        style={{ height: 22, padding: '0 8px', maxWidth: 180 }}
        onClick={() => setOpen((v) => !v)}
        title={`Job history — total spent $${totalCost.toFixed(4)}`}
      >
        📊 ${totalCost.toFixed(4)}
      </Button>

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
            <Button onClick={handleClear} disabled={records.length === 0} style={{ flex: 1 }}>
              Clear History
            </Button>
          </div>

          {/* Per-kind / per-model breakdown — only render when there is anything
              to summarise so empty workspaces stay clean. */}
          {records.length > 0 && (
            <div
              style={{
                background: 'var(--win95-white)',
                border: '1px solid var(--win95-gray-mid)',
                padding: '4px 6px',
                fontSize: 11,
                display: 'flex',
                flexDirection: 'column',
                gap: 4,
              }}
            >
              <div
                style={{
                  fontWeight: 'bold',
                  color: 'var(--text-muted)',
                  fontSize: 10,
                  textTransform: 'uppercase',
                  letterSpacing: 0.5,
                }}
              >
                By Kind
              </div>
              {byKind.map(([kind, sub]) => (
                <div
                  key={`kind-${kind}`}
                  style={{ display: 'flex', justifyContent: 'space-between', fontFamily: 'monospace' }}
                  title={`${KIND_LABEL[kind] ?? kind}: ${sub.count} call(s), in ${sub.inputTokens.toLocaleString()} / out ${sub.outputTokens.toLocaleString()}`}
                >
                  <span>{KIND_LABEL[kind] ?? kind} ({sub.count})</span>
                  <span style={{ color: 'var(--status-reject-dark)' }}>${sub.cost.toFixed(4)}</span>
                </div>
              ))}
              <div
                style={{
                  fontWeight: 'bold',
                  color: 'var(--text-muted)',
                  fontSize: 10,
                  textTransform: 'uppercase',
                  letterSpacing: 0.5,
                  marginTop: 2,
                }}
              >
                By Model
              </div>
              {byModel.map(([model, sub]) => (
                <div
                  key={`model-${model}`}
                  style={{ display: 'flex', justifyContent: 'space-between', fontFamily: 'monospace' }}
                  title={`${model}: ${sub.count} call(s)`}
                >
                  <span>{model} ({sub.count})</span>
                  <span style={{ color: 'var(--status-reject-dark)' }}>${sub.cost.toFixed(4)}</span>
                </div>
              ))}
              <div
                style={{
                  fontWeight: 'bold',
                  color: 'var(--text-muted)',
                  fontSize: 10,
                  textTransform: 'uppercase',
                  letterSpacing: 0.5,
                  marginTop: 2,
                }}
              >
                Tokens
              </div>
              <div
                style={{ display: 'flex', justifyContent: 'space-between', fontFamily: 'monospace' }}
              >
                <span>Total in/out</span>
                <span>{totalTokens.toLocaleString()}</span>
              </div>
              {totalCacheRead > 0 && (
                <div
                  style={{ display: 'flex', justifyContent: 'space-between', fontFamily: 'monospace' }}
                >
                  <span>Cache read</span>
                  <span>{totalCacheRead.toLocaleString()}</span>
                </div>
              )}
            </div>
          )}

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
                    <span style={{ color: 'var(--win95-navy)' }}>
                      {KIND_LABEL[r.kind] ?? r.kind} · {r.model}
                    </span>
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
