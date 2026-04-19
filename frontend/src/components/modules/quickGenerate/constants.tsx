import React from 'react';
import {
  RiFileTextLine,
  RiFlashlightLine,
  RiListCheck2,
} from '@remixicon/react';
import type { GeneratedTc, Mode } from './types';

export const MODE_CONFIG: {
  id: Mode;
  label: string;
  icon: React.ReactNode;
  desc: string;
}[] = [
  {
    id: 'single',
    label: 'Single TC',
    icon: <RiFlashlightLine className="size-4" />,
    desc: 'One test item → one TC',
  },
  {
    id: 'with_context',
    label: 'With Context',
    icon: <RiFileTextLine className="size-4" />,
    desc: 'Test item + additional criteria or context',
  },
  {
    id: 'decompose',
    label: 'Decompose',
    icon: <RiListCheck2 className="size-4" />,
    desc: 'Full requirement → AI splits into multiple TCs',
  },
];

/** Column layout for the stacked TC card. */
export const COLUMN_HEADERS: {
  key: keyof GeneratedTc['tc'];
  label: string;
  muted?: boolean;
}[] = [
  { key: 'test_item_rewrite', label: 'Test Item' },
  { key: 'pre_conditions', label: 'Pre-Conditions' },
  { key: 'input_test_data', label: 'Input Test Data', muted: true },
  { key: 'test_procedure', label: 'Test Procedure' },
  { key: 'expected_result', label: 'Expected Result' },
];

// Saturated + sunken-inset look, matched to `.status-badge`.
export const PRIORITY_STYLE: Record<string, React.CSSProperties> = {
  High:   { background: 'var(--status-reject)', color: 'var(--win95-white)' },
  Medium: { background: 'var(--status-warn)',   color: 'var(--win95-black)' },
  Low:    { background: 'var(--win95-gray-mid)', color: 'var(--win95-white)' },
};

export const PRIORITY_FALLBACK: React.CSSProperties = {
  background: 'var(--win95-gray-mid)',
  color: 'var(--win95-white)',
};

export const PRIORITY_BASE: React.CSSProperties = {
  border: '2px solid',
  borderColor:
    'var(--win95-gray-dark) var(--win95-gray-light) var(--win95-gray-light) var(--win95-gray-dark)',
  boxShadow: 'inset 1px 1px 0 rgba(0,0,0,0.25)',
  fontWeight: 'bold',
  padding: '1px 6px',
  fontSize: 10,
  letterSpacing: 0.5,
  textTransform: 'uppercase',
};
