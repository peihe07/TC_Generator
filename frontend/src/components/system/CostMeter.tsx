'use client';

import React from 'react';
import { useJobStore } from '../../store/useJobStore';

const MODEL_PRICING: Record<string, { input: number; output: number; label: string }> = {
  'gpt-5':        { input: 5.00, output: 15.00, label: 'GPT-5' },
  'gpt-5-mini':   { input: 0.25, output: 2.00,  label: 'GPT-5 mini' },
  'gpt-4.1':      { input: 2.00, output: 8.00,  label: 'GPT-4.1' },
  'gpt-4.1-mini': { input: 0.40, output: 1.60,  label: 'GPT-4.1 mini' },
  'gpt-4o':       { input: 2.50, output: 10.00, label: 'GPT-4o' },
  'gpt-4o-mini':  { input: 0.15, output: 0.60,  label: 'GPT-4o mini' },
};

const CostMeter: React.FC = () => {
  const { stats, config, jobMetadata } = useJobStore();

  const pricing = MODEL_PRICING[config.model] ?? MODEL_PRICING['gpt-4.1'];
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
        background: '#c0c0c0',
        border: '2px solid',
        borderColor: '#ffffff #808080 #808080 #ffffff',
        boxShadow: '2px 2px 0 #000000',
        userSelect: 'none',
      }}
    >
      {/* Title bar */}
      <div
        style={{
          background: '#000080',
          color: '#ffffff',
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
      </div>

      {/* Body */}
      <div style={{ padding: '6px 8px', display: 'flex', flexDirection: 'column', gap: 3 }}>
        {/* Model */}
        <Row label="Model" value={pricing.label} />

        {/* Tokens */}
        <div style={{ borderTop: '1px solid #808080', marginTop: 2, paddingTop: 2 }}>
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
                sub={`@1.25x`}
              />
              <Row
                label="Cache R"
                value={`${stats.cacheReadTokens.toLocaleString()} tok`}
                sub={`@0.10x`}
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
            borderTop: '1px solid #808080',
            marginTop: 2,
            paddingTop: 3,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'baseline',
          }}
        >
          <span style={{ fontSize: 13, color: '#444' }}>Total Cost</span>
          <span
            style={{
              fontFamily: 'monospace',
              fontWeight: 'bold',
              fontSize: 15,
              color: totalCost > 0 ? '#8b0000' : '#555',
            }}
          >
            ${totalCost.toFixed(4)}
          </span>
        </div>

        {/* Budget bar */}
        {config.budgetLimit > 0 && (
          <div>
            <div
              style={{
                height: 8,
                background: '#808080',
                border: '1px solid #555',
                marginTop: 2,
              }}
            >
              <div
                style={{
                  height: '100%',
                  width: `${Math.min((totalCost / config.budgetLimit) * 100, 100).toFixed(1)}%`,
                  background: totalCost / config.budgetLimit > 0.8 ? '#cc0000' : '#000080',
                  transition: 'width 0.3s',
                }}
              />
            </div>
            <div style={{ fontSize: 11, color: '#555', textAlign: 'right', marginTop: 2 }}>
              budget: ${config.budgetLimit}
            </div>
          </div>
        )}

        {/* Job ID */}
        {jobMetadata?.jobId && (
          <div
            style={{
              borderTop: '1px solid #808080',
              marginTop: 2,
              paddingTop: 2,
              fontSize: 11,
              color: '#666',
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
    <span style={{ fontSize: 13, color: '#444', flexShrink: 0 }}>{label}</span>
    <span style={{ fontFamily: 'monospace', fontSize: 13, fontWeight: 'bold', textAlign: 'right' }}>
      {value}
      {sub && <span style={{ fontWeight: 'normal', color: '#666', marginLeft: 4 }}>{sub}</span>}
    </span>
  </div>
);

export default CostMeter;
