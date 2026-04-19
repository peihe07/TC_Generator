import React from 'react';
import type { DiffToken } from './diffTokens';

/**
 * 把 diffTokens() 產出的 token stream 渲染成一串 <span>：
 *   same → 一般文字
 *   add  → .diff-add（綠底）
 *   del  → .diff-del（紅底 + strikethrough）
 *
 * 純 presentational；真正的 diff 演算法在 ./diffTokens.ts。
 */
export const DiffText: React.FC<{ tokens: DiffToken[] }> = ({ tokens }) => (
  <span className="whitespace-pre-wrap">
    {tokens.map((t, i) =>
      t.type === 'same' ? (
        <span key={i}>{t.text}</span>
      ) : t.type === 'add' ? (
        <span key={i} className="diff-add">{t.text}</span>
      ) : (
        <span key={i} className="diff-del">{t.text}</span>
      ),
    )}
  </span>
);

export default DiffText;
