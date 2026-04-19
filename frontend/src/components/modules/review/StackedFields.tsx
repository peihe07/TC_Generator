import React from 'react';

/**
 * Excel-column style read-only field used in the expanded detail pane.
 * 標籤在上、值在下的「堆疊」版面，方便對照 Original vs Generated。
 */
export const StackedReadField: React.FC<{
  label: string;
  value: string;
  muted?: boolean;
}> = ({ label, value, muted }) => (
  <div style={{ borderTop: '1px solid var(--win95-gray-lighter)' }}>
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: '#e8e8e8',
        borderBottom: '1px solid #d0d0d0',
        fontSize: 10,
        color: 'var(--text-muted)',
        letterSpacing: 0.5,
      }}
    >
      {label}
    </div>
    <div
      className="selectable px-3 py-2 text-xs whitespace-pre-wrap"
      style={{
        color: muted ? 'var(--win95-gray-mid)' : 'var(--win95-black)',
        wordBreak: 'break-word',
        lineHeight: 1.5,
      }}
    >
      {value || '—'}
    </div>
  </div>
);

/**
 * 可編輯版：橘色 memo style，給 "Manual Edit" 模式使用。
 */
export const StackedEditField: React.FC<{
  label: string;
  value: string;
  onChange: (v: string) => void;
  minHeight?: number;
}> = ({ label, value, onChange, minHeight = 50 }) => (
  <div style={{ borderTop: '1px solid #fdba74' }} className="memo-edit">
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: '#fed7aa',
        borderBottom: '1px solid #fdba74',
        fontSize: 10,
        color: '#7c2d12',
        letterSpacing: 0.5,
      }}
    >
      {label}
    </div>
    <textarea
      className="w-full px-3 py-2 text-xs"
      style={{ minHeight, resize: 'vertical', lineHeight: 1.5 }}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  </div>
);
