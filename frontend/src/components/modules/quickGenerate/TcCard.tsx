import React from 'react';
import { RiFlashlightLine } from '@remixicon/react';
import { TitleBarMini } from '../../ui';
import type { GeneratedTc } from './types';
import {
  COLUMN_HEADERS,
  PRIORITY_BASE,
  PRIORITY_FALLBACK,
  PRIORITY_STYLE,
} from './constants';

export interface TcCardProps {
  tc: GeneratedTc;
  /** 0-based index → rendered as "TC N+1". */
  index: number;
}

/** One generated TC, rendered as a Win95 paper card with stacked fields. */
export const TcCard: React.FC<TcCardProps> = ({ tc, index }) => {
  const priorityColor = PRIORITY_STYLE[tc.tc.priority] ?? PRIORITY_FALLBACK;
  return (
    <div className="flex flex-col">
      <TitleBarMini
        icon={<RiFlashlightLine className="size-3" />}
        title={
          <>
            TC {index + 1}
            {tc.scenarioName ? ` — ${tc.scenarioName}` : ''}
          </>
        }
      >
        <span style={{ ...PRIORITY_BASE, ...priorityColor }}>{tc.tc.priority}</span>
        <span className="text-[10px] opacity-75 ml-2">{tc.tc.design_method}</span>
      </TitleBarMini>
      <div className="paper-card">
        <div className="flex flex-col">
          {COLUMN_HEADERS.map((c) => {
            const raw = tc.tc[c.key] as string;
            return (
              <div
                key={c.key}
                style={{ borderTop: '1px solid var(--win95-gray-lighter)' }}
              >
                <div
                  className="px-2 py-1 font-bold uppercase"
                  style={{
                    background: 'var(--field-header-bg)',
                    borderBottom: '1px solid var(--field-header-border)',
                    fontSize: 10,
                    color: 'var(--text-muted)',
                    letterSpacing: 0.5,
                  }}
                >
                  {c.label}
                </div>
                <div
                  className="selectable px-3 py-2 text-xs whitespace-pre-wrap"
                  style={{
                    color: c.muted ? 'var(--win95-gray-mid)' : 'var(--win95-black)',
                    fontStyle: c.muted ? 'italic' : 'normal',
                    wordBreak: 'break-word',
                    lineHeight: 1.5,
                  }}
                >
                  {raw || '—'}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export const TcList: React.FC<{ tcs: GeneratedTc[] }> = ({ tcs }) => (
  <div className="flex flex-col gap-3">
    {tcs.map((tc, i) => (
      <TcCard key={`${tc.scenarioId}-${i}`} tc={tc} index={i} />
    ))}
  </div>
);

export default TcCard;
