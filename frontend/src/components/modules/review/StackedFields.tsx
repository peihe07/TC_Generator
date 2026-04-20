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
  // 視覺上與 edit mode（橘色框）一致的「每欄獨立區塊」骨架，
  // 只把強調色換成 Win95 海軍藍 header；這樣一展開就能看清楚
  // Pre-Cond / Procedure / Expected 各自的分界，不用等按編輯才出現框。
  <div style={{ borderTop: '2px solid var(--win95-navy)' }}>
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: 'var(--win95-navy)',
        color: 'var(--win95-white)',
        borderBottom: '1px solid var(--win95-navy)',
        fontSize: 10,
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
  <div
    style={{ borderTop: '1px solid var(--edit-accent-border)' }}
    className="memo-edit"
  >
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: 'var(--edit-accent-bg)',
        borderBottom: '1px solid var(--edit-accent-border)',
        fontSize: 10,
        color: 'var(--edit-accent-fg)',
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

/**
 * 下拉選單版：用在 Priority、Design Method 這類固定選項。
 * `options` 若不含目前的 `value`，會在最前面加一個「Custom: xxx」條目
 * 以免切換編輯模式時把 AI 回的 fuzzy 值直接丟掉。
 */
export const StackedEditDropdown: React.FC<{
  label: string;
  value: string;
  options: readonly string[];
  onChange: (v: string) => void;
  placeholder?: string;
}> = ({ label, value, options, onChange, placeholder }) => {
  const hasCustom = Boolean(value) && !options.includes(value);
  return (
    <div
      style={{ borderTop: '1px solid var(--edit-accent-border)' }}
      className="memo-edit"
    >
      <div
        className="px-2 py-1 font-bold uppercase"
        style={{
          background: 'var(--edit-accent-bg)',
          borderBottom: '1px solid var(--edit-accent-border)',
          fontSize: 10,
          color: 'var(--edit-accent-fg)',
          letterSpacing: 0.5,
        }}
      >
        {label}
      </div>
      <select
        className="w-full px-2 py-1 text-xs"
        style={{ lineHeight: 1.5 }}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        {!value && placeholder ? <option value="">{placeholder}</option> : null}
        {hasCustom ? (
          <option value={value}>Custom: {value}</option>
        ) : null}
        {options.map((opt) => (
          <option key={opt} value={opt}>
            {opt}
          </option>
        ))}
      </select>
    </div>
  );
};
