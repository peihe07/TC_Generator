"use client";

import { useState } from "react";
import { RiLoader4Line, RiRefreshLine, RiCheckLine } from "@remixicon/react";
import {
  fetchGroupingPreview,
} from "../../../../services/jobAdapter";
import { useJobHistoryStore } from "../../../../store/useJobHistoryStore";
import { useJobStore } from "../../../../store/useJobStore";
import type {
  GroupPreviewState,
} from "../../../modules/configure/types";
import { Section, StatusPill } from "./shared";

export default function ConfigureGrouping() {
  const tcRows = useJobStore((s) => s.tcRows);
  const setTcRows = useJobStore((s) => s.setTcRows);
  const accumulateStats = useJobStore((s) => s.accumulateStats);
  const config = useJobStore((s) => s.config);
  const jobMetadata = useJobStore((s) => s.jobMetadata);

  const [preview, setPreview] = useState<GroupPreviewState | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [costSpent, setCostSpent] = useState(0);

  const onGroup = async () => {
    if (!tcRows.length) {
      setPreview(null);
      return;
    }
    setIsLoading(true);
    setError(null);
    setPreview(null);
    try {
      const result = await fetchGroupingPreview({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
        forceRegroup: true,
      });
      if (result.cost > 0) {
        setCostSpent((v) => Number((v + result.cost).toFixed(4)));
        accumulateStats({
          cost: result.cost,
          inputTokens: result.inputTokens,
          outputTokens: result.outputTokens,
          cacheCreationTokens: result.cacheCreationTokens,
          cacheReadTokens: result.cacheReadTokens,
        });
        useJobHistoryStore.getState().appendRecord({
          id: `group-${Date.now().toString(36)}`,
          kind: "group",
          model: result.model || config.model,
          startedAt: Date.now(),
          finishedAt: Date.now(),
          rowsTotal: tcRows.length,
          rowsProcessed: result.assignments.length,
          cost: result.cost,
          inputTokens: result.inputTokens,
          outputTokens: result.outputTokens,
          cacheReadTokens: result.cacheReadTokens,
          cacheCreationTokens: result.cacheCreationTokens,
        });
      }
      setPreview(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Group request failed.");
    } finally {
      setIsLoading(false);
    }
  };

  const onApply = () => {
    if (!preview) return;
    const assignments = new Map(
      preview.assignments.map((a) => [a.id, a.testSet])
    );
    setTcRows(
      tcRows.map((row) => ({
        ...row,
        testSet: assignments.get(row.id) ?? row.testSet,
      }))
    );
    setPreview(null); // 套用後清掉 preview，避免重複套用
  };

  const updateTestSet = (id: string, value: string) => {
    setTcRows(tcRows.map((r) => (r.id === id ? { ...r, testSet: value } : r)));
    setPreview(null); // edit 後 invalidate
  };

  const existingTestSets = Array.from(
    new Set(tcRows.map((r) => r.testSet).filter(Boolean))
  );

  return (
    <Section
      title="Grouping"
      hint="Classify rows into Test Sets. Edit manually or let AI regroup."
    >
      <div className="space-y-3">
        <div className="flex items-center gap-2 flex-wrap">
          <button
            type="button"
            onClick={() => void onGroup()}
            disabled={isLoading || !tcRows.length}
            className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-50"
          >
            {isLoading ? (
              <RiLoader4Line size={14} className="animate-spin" />
            ) : (
              <RiRefreshLine size={14} />
            )}
            Group with AI
          </button>
          <button
            type="button"
            onClick={onApply}
            disabled={!preview || isLoading}
            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-md text-sm font-bold focus-ring disabled:opacity-40 transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            <RiCheckLine size={14} />
            Apply Preview
          </button>
          {costSpent > 0 && (
            <span className="text-xs text-muted">
              Spent ${costSpent.toFixed(4)} on grouping
            </span>
          )}
        </div>

        {error && (
          <div
            className="text-sm px-3 py-2 rounded-md"
            style={{
              color: "var(--color-brandy)",
              backgroundColor: "rgba(120, 41, 15, 0.08)",
            }}
          >
            {error}
          </div>
        )}

        {preview && (
          <div className="space-y-2">
            <StatusPill tone="warn">
              {preview.assignments.length} row(s) → {preview.groups.length}{" "}
              Test Set(s) (preview)
            </StatusPill>
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left text-xs uppercase tracking-wider text-muted">
                  <th className="font-normal py-1">Test Set</th>
                  <th className="font-normal py-1 w-16">Count</th>
                  <th className="font-normal py-1">Requirement IDs</th>
                </tr>
              </thead>
              <tbody>
                {preview.groups.map((g) => (
                  <tr key={g.testSet} className="row-hover">
                    <td className="py-1.5 text-primary font-bold">
                      {g.testSet}
                    </td>
                    <td className="py-1.5 text-secondary">{g.count}</td>
                    <td className="py-1.5 text-secondary text-xs truncate max-w-[400px]">
                      {g.reqIds.join(", ")}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {tcRows.length > 0 && (
          <div className="space-y-2">
            <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
              Manual Override
            </div>
            <datalist id="builder-existing-test-sets">
              {existingTestSets.map((ts) => (
                <option key={ts} value={ts} />
              ))}
              {preview?.groups.map((g) => (
                <option key={`grp-${g.testSet}`} value={g.testSet} />
              ))}
            </datalist>
            <div
              className="overflow-y-auto rounded-md"
              style={{
                maxHeight: 280,
                boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.15)",
              }}
            >
              <table className="w-full text-xs">
                <thead className="sticky top-0 z-10">
                  <tr
                    className="text-left text-[10px] uppercase tracking-wider text-muted"
                    style={{
                      backgroundColor: "rgba(255, 236, 209, 0.95)",
                      backdropFilter: "blur(8px)",
                    }}
                  >
                    <th className="font-normal px-3 py-2 w-32">Req ID</th>
                    <th className="font-normal px-3 py-2">Test Item</th>
                    <th className="font-normal px-3 py-2 w-48">Test Set</th>
                  </tr>
                </thead>
                <tbody>
                  {tcRows.map((row) => (
                    <tr key={row.id} className="row-hover">
                      <td className="px-3 py-1.5 text-secondary truncate">
                        {row.reqId}
                      </td>
                      <td
                        className="px-3 py-1.5 text-primary truncate max-w-0"
                        title={row.testItem}
                      >
                        {row.testItem}
                      </td>
                      <td className="px-3 py-1">
                        <input
                          type="text"
                          list="builder-existing-test-sets"
                          value={row.testSet}
                          onChange={(e) =>
                            updateTestSet(row.id, e.target.value)
                          }
                          className="w-full bg-transparent px-2 py-1 rounded text-xs text-primary focus-ring"
                          style={{
                            boxShadow:
                              "inset 0 0 0 1px rgba(21, 97, 109, 0.15)",
                          }}
                        />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </Section>
  );
}
