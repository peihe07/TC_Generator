'use client';

import React, { useEffect, useState } from 'react';
import { RiRobot2Line, RiCloseLine } from '@remixicon/react';
import { useAgentStore } from '../../store/useAgentStore';
import { useJobStore } from '../../store/useJobStore';

const DISMISS_MS = 6000;

const TOOL_LABELS: Record<string, string> = {
  parse_workbook: '重新解析了 workbook',
  group_tests: '重新分組了 test set',
  match_spec: '重新跑了 spec matching',
  generate_tc: '生成了測試案例',
  regenerate_tc: '重生了測試案例',
  write_excel: '寫出了 Excel 檔',
  validate_tc: '跑了 validator',
};

/**
 * 右下角浮現的 toast：當 Agent 動到目前 GUI 開著的 job 時提示使用者刷新。
 * 自動在 DISMISS_MS 後消失，也可以點擊 × 立刻關掉。
 */
export default function AgentStateUpdateToast() {
  const lastStateUpdate = useAgentStore((s) => s.lastStateUpdate);
  const activeJobId = useJobStore((s) => s.jobMetadata?.jobId);
  const [dismissedTs, setDismissedTs] = useState<number | null>(null);

  const isVisible =
    !!lastStateUpdate &&
    !!activeJobId &&
    lastStateUpdate.jobId === activeJobId &&
    lastStateUpdate.ts !== dismissedTs;

  useEffect(() => {
    if (!isVisible || !lastStateUpdate) return;
    const t = setTimeout(() => setDismissedTs(lastStateUpdate.ts), DISMISS_MS);
    return () => clearTimeout(t);
  }, [isVisible, lastStateUpdate]);

  if (!isVisible || !lastStateUpdate) return null;

  const label = TOOL_LABELS[lastStateUpdate.tool] ?? `執行了 ${lastStateUpdate.tool}`;

  return (
    <div
      className="agent-state-toast"
      role="status"
      aria-live="polite"
    >
      <RiRobot2Line size={16} className="agent-state-toast-icon" />
      <div className="agent-state-toast-body">
        <div className="agent-state-toast-title">Agent 剛動到這個 job</div>
        <div className="agent-state-toast-detail">
          {label}（{lastStateUpdate.jobId.slice(0, 8)}…）。建議重新載入以看到最新資料。
        </div>
      </div>
      <button
        type="button"
        className="agent-state-toast-close"
        aria-label="Dismiss"
        onClick={() => setDismissedTs(lastStateUpdate.ts)}
      >
        <RiCloseLine size={12} />
      </button>
    </div>
  );
}
