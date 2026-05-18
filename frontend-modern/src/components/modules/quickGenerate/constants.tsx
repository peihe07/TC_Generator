import React from 'react';
import type { GeneratedTc } from './types';

// 原本的 MODE_CONFIG（single / with_context / decompose 三擇一）已移除。
// Quick Generate 統一走 auto-split 流程，由 AI 判斷要拆幾筆 TC。

/** Column layout for the stacked TC card. */
export const COLUMN_HEADERS: {
  key: keyof GeneratedTc['tc'];
  label: string;
  muted?: boolean;
}[] = [
  { key: 'tc_title', label: 'Test Item' },
  { key: 'pre_conditions', label: 'Pre-Conditions' },
  { key: 'input_test_data', label: 'Input Test Data', muted: true },
  { key: 'test_procedure', label: 'Test Procedure' },
  { key: 'expected_result', label: 'Expected Result' },
];

// Saturated + sunken-inset look, matched to `.status-badge`.
export const PRIORITY_STYLE: Record<string, React.CSSProperties> = {
  P0: { background: 'var(--status-reject)',   color: 'var(--win95-white)' },
  P1: { background: 'var(--status-warn)',     color: 'var(--win95-black)' },
  P2: { background: 'var(--win95-gray-mid)',  color: 'var(--win95-white)' },
  P3: { background: 'var(--win95-gray-light)', color: 'var(--win95-black)' },
};

export const PRIORITY_FALLBACK: React.CSSProperties = {
  background: 'var(--win95-gray-mid)',
  color: 'var(--win95-white)',
};

export const PRIORITY_BASE: React.CSSProperties = {
  border: '2px solid',
  borderColor:
    'var(--win95-gray-dark) var(--win95-gray-light) var(--win95-gray-light) var(--win95-gray-dark)',
  boxShadow: 'var(--shadow-badge-inset)',
  fontWeight: 'bold',
  padding: '1px 6px',
  fontSize: 10,
  letterSpacing: 0.5,
  textTransform: 'uppercase',
};
