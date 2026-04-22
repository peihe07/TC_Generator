'use client';

import React, { useState } from 'react';
import { RiBarChartBoxLine } from '@remixicon/react';
import { useJobStore } from '../../store/useJobStore';
import CostDashboardPopup from './CostDashboardPopup';

const MODEL_PRICING: Record<string, { input: number; cachedInput: number; output: number; label: string }> = {
  'gpt-5.4':      { input: 2.50, cachedInput: 0.25,  output: 15.00, label: 'GPT-5.4' },
  'gpt-5.4-mini': { input: 0.75, cachedInput: 0.075, output: 4.50,  label: 'GPT-5.4 mini' },
  'gpt-5.4-nano': { input: 0.20, cachedInput: 0.02,  output: 1.25,  label: 'GPT-5.4 nano' },
  'gpt-5':        { input: 5.00, cachedInput: 0.50,  output: 15.00, label: 'GPT-5' },
  'gpt-5-mini':   { input: 0.25, cachedInput: 0.025, output: 2.00,  label: 'GPT-5 mini' },
  'gpt-4.1':      { input: 2.00, cachedInput: 0.20,  output: 8.00,  label: 'GPT-4.1' },
  'gpt-4.1-mini': { input: 0.40, cachedInput: 0.04,  output: 1.60,  label: 'GPT-4.1 mini' },
  'gpt-4o':       { input: 2.50, cachedInput: 1.25,  output: 10.00, label: 'GPT-4o' },
  'gpt-4o-mini':  { input: 0.15, cachedInput: 0.075, output: 0.60,  label: 'GPT-4o mini' },
};

const CostMeter: React.FC = () => {
  const { stats, config, jobMetadata } = useJobStore();
  const [dashboardOpen, setDashboardOpen] = useState(false);

  const pricing = MODEL_PRICING[config.model] ?? MODEL_PRICING['gpt-5.4-mini'];
  const inputCost  = (stats.inputTokens  / 1_000_000) * pricing.input;
  const outputCost = (stats.outputTokens / 1_000_000) * pricing.output;
  const totalCost  = stats.cost > 0 ? stats.cost : inputCost + outputCost;

  const hasActivity = stats.total > 0 || stats.cost > 0;

  return (
    <div
      style={{
        position: 'absolute',
        top: 8,
        right: 8,
        zIndex: 50,
        minWidth: 240,
        background: 'var(--win95-gray)',
        border: '2px solid',
        borderColor: 'var(--win95-white) var(--win95-gray-mid) var(--win95-gray-mid) var(--win95-white)',
        boxShadow: '2px 2px 0 var(--win95-black)',
        userSelect: 'none',
      }}
    >
      {/* Title bar */}
      <div
        style={{
          background: 'var(--win95-navy)',
          color: 'var(--win95-white)',
          padding: '3px 8px',
          fontWeight: 'bold',
          fontSize: 14,
          display: 'flex',
          alignItems: 'center',
          gap: 4,
        }}
      >
        <span>API Usage</span>
        {hasActivity && stats.processed < stats.total && (
          <span style={{ marginLeft: 'auto', fontSize: 13, opacity: 0.8 }}>
            {stats.processed}/{stats.total}
          </span>
        )}
        <button
          type="button"
          className="cost-meter-dashboard-btn"
          aria-label="Open Cost Dashboard"
          title="Cost Dashboard（跨 job 統計）"
          onClick={() => setDashboardOpen(true)}
          style={{
            marginLeft: hasActivity && stats.processed < stats.total ? 4 : 'auto',
          }}
        >
          <RiBarChartBoxLine size={12} />
        </button>
      </div>

      {dashboardOpen && <CostDashboardPopup onClose={() => setDashboardOpen(false)} />}

      {/* Body */}
      <div style={{ padding: '6px 8px', display: 'flex', flexDirection: 'column', gap: 3 }}>
        {/* Model */}
        <Row label="Model" value={pricing.label} />

        {/* Tokens */}
        <div style={{ borderTop: '1px solid var(--win95-gray-mid)', marginTop: 2, paddingTop: 2 }}>
          <Row
            label="Input"
            value={stats.inputTokens > 0 ? `${stats.inputTokens.toLocaleString()} tok` : '—'}
            sub={stats.inputTokens > 0 ? `$${inputCost.toFixed(5)}` : undefined}
          />
          <Row
            label="Output"
            value={stats.outputTokens > 0 ? `${stats.outputTokens.toLocaleString()} tok` : '—'}
            sub={stats.outputTokens > 0 ? `$${outputCost.toFixed(5)}` : undefined}
          />
          {(stats.cacheCreationTokens > 0 || stats.cacheReadTokens > 0) && (
            <>
              <Row
                label="Cache W"
                value={`${stats.cacheCreationTokens.toLocaleString()} tok`}
                sub={`$${((stats.cacheCreationTokens / 1_000_000) * pricing.input).toFixed(5)}`}
              />
              <Row
                label="Cache R"
                value={`${stats.cacheReadTokens.toLocaleString()} tok`}
                sub={`$${((stats.cacheReadTokens / 1_000_000) * pricing.cachedInput).toFixed(5)}`}
              />
              {(() => {
                const totalIn = stats.inputTokens + stats.cacheCreationTokens + stats.cacheReadTokens;
                const hitRate = totalIn > 0 ? (stats.cacheReadTokens / totalIn) * 100 : 0;
                return (
                  <Row
                    label="Hit rate"
                    value={`${hitRate.toFixed(1)}%`}
                  />
                );
              })()}
            </>
          )}
        </div>

        {/* Total cost */}
        <div
          style={{
            borderTop: '1px solid var(--win95-gray-mid)',
            marginTop: 2,
            paddingTop: 3,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'baseline',
          }}
        >
          <span style={{ fontSize: 13, color: 'var(--text-muted)' }}>Total Cost</span>
          <span
            style={{
              fontFamily: 'monospace',
              fontWeight: 'bold',
              fontSize: 15,
              color: totalCost > 0 ? 'var(--status-reject-dark)' : 'var(--text-muted)',
            }}
          >
            ${totalCost.toFixed(4)}
          </span>
        </div>

        {/* Remaining credit — 只在使用者設定 creditBalance 時顯示 */}
        {config.creditBalance > 0 && (() => {
          const remaining = config.creditBalance - totalCost;
          const lowCredit = remaining < config.creditBalance * 0.2;
          const overBalance = remaining < 0;
          return (
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'baseline',
              }}
            >
              <span style={{ fontSize: 13, color: 'var(--text-muted)' }}>
                Remaining <span style={{ fontSize: 11, opacity: 0.7 }}>(of ${config.creditBalance.toFixed(2)})</span>
              </span>
              <span
                style={{
                  fontFamily: 'monospace',
                  fontWeight: 'bold',
                  fontSize: 13,
                  color: overBalance
                    ? 'var(--status-error-border)'
                    : lowCredit
                      ? 'var(--status-reject-dark)'
                      : 'var(--win95-navy)',
                }}
              >
                ${remaining.toFixed(4)}
              </span>
            </div>
          );
        })()}

        {/* Budget bar */}
        {config.budgetLimit > 0 && (
          <div>
            <div
              style={{
                height: 8,
                background: 'var(--win95-gray-mid)',
                border: '1px solid var(--text-muted)',
                marginTop: 2,
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${Math.min((totalCost / config.budgetLimit) * 100, 100).toFixed(1)}%`,
                  background: totalCost / config.budgetLimit > 0.8 ? 'var(--status-error-border)' : 'var(--win95-navy)',
                  transition: 'width var(--motion-progress)',
                }}
              />
            </div>
            <div style={{ fontSize: 11, color: 'var(--text-muted)', textAlign: 'right', marginTop: 2 }}>
              budget: ${config.budgetLimit}
            </div>
          </div>
        )}

        {/* Job ID */}
        {jobMetadata?.jobId && (
          <div
            style={{
              borderTop: '1px solid var(--win95-gray-mid)',
              marginTop: 2,
              paddingTop: 2,
              fontSize: 11,
              color: 'var(--text-muted)',
              fontFamily: 'monospace',
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap',
            }}
          >
            {jobMetadata.jobId}
          </div>
        )}
      </div>
    </div>
  );
};

const Row: React.FC<{ label: string; value: string; sub?: string }> = ({ label, value, sub }) => (
  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', gap: 8 }}>
    <span style={{ fontSize: 13, color: 'var(--text-muted)', flexShrink: 0 }}>{label}</span>
    <span style={{ fontFamily: 'monospace', fontSize: 13, fontWeight: 'bold', textAlign: 'right' }}>
      {value}
      {sub && <span style={{ fontWeight: 'normal', color: 'var(--text-muted)', marginLeft: 4 }}>{sub}</span>}
    </span>
  </div>
);

export default CostMeter;
