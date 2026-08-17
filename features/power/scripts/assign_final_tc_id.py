"""B2 —— 最終 tc_id 之指派與列序（R-P113(c) / R-P115）。

R-P113：產出依 Test Set 分批，各批之 `tc_id` 為**批次內臨時編號**；
**最終 tc_id 於寫回時一次指派**，依 SWE-PM ID 遞增序排列全部 TC 後自 001 起連號。
工作簿列序即最終 tc_id 序。

R-P115（分析層自裁）：同一 `req_id` 之多條 TC 依其**規格原文子句出現序**排列，
該序記於 `split_index`（自 1 起）。排序鍵為 `(SWE-PM ID 數值, split_index)`，
二者皆為整數，全序且可重現。

**本腳本只產出對照表，不改寫任何批次 JSON** ——
R-P113(c) 明訂最終指派於全部 114 leaf 產出完成後方為之（16 §I）。

用法：
    python features/power/scripts/assign_final_tc_id.py            # 產表
    python features/power/scripts/assign_final_tc_id.py --self-test  # G85
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

TC_ID_FORMAT = "NR1L-PowerManagement-{:03d}"
REQ_NUM_RE = re.compile(r"SWE-PM-(\d+)$")


def sort_key(tc: dict) -> tuple[int, int]:
    """排序鍵 (SWE-PM ID 數值, split_index)。缺 split_index 即為錯誤，不預設。"""
    m = REQ_NUM_RE.match(str(tc.get("req_id", "")))
    if not m:
        raise ValueError(f"req_id 形態不符：{tc.get('req_id')!r}（R-P86 要求無後綴）")
    if "split_index" not in tc:
        raise ValueError(f"{tc.get('tc_id')} 缺 split_index —— R-P115 之排序鍵不完整")
    return int(m.group(1)), int(tc["split_index"])


def collect(directory: Path) -> list[dict]:
    rows = []
    for path in sorted(directory.glob("*.json")):
        batch = json.loads(path.read_text(encoding="utf-8"))
        for tc in batch.get("tcs", []):
            rows.append({**tc, "_file": path.name,
                         "_provisional": batch.get("tc_id_status") == "provisional"})
    return rows


def assign(rows: list[dict]) -> list[dict]:
    ordered = sorted(rows, key=sort_key)
    out = []
    for i, tc in enumerate(ordered, 1):
        out.append({
            "row": i,
            "final_tc_id": TC_ID_FORMAT.format(i),
            "provisional_tc_id": tc["tc_id"],
            "req_id": tc["req_id"],
            "split_index": tc["split_index"],
            "file": tc["_file"],
            "is_provisional": tc["_provisional"],
        })
    return out


def self_test() -> int:
    """G85 —— R-P55 回歸斷言。合成資料，不以 repo 現況為對照（16 §I）。"""
    failures = 0

    def check(label: str, got, want) -> None:
        nonlocal failures
        ok = got == want
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G85 {label}")
        print(f"          期望 {want}；實際 {got}")

    # 亂序輸入 —— 排序後須為 071×4 → 072×2 → 073×9
    synth = [{"tc_id": f"X-{i:03d}", "req_id": r, "split_index": s}
             for i, (r, s) in enumerate(
                 [("SWE-PM-073", 9), ("SWE-PM-071", 2), ("SWE-PM-073", 1),
                  ("SWE-PM-072", 2), ("SWE-PM-071", 4), ("SWE-PM-073", 5),
                  ("SWE-PM-071", 1), ("SWE-PM-072", 1), ("SWE-PM-073", 3),
                  ("SWE-PM-071", 3), ("SWE-PM-073", 2), ("SWE-PM-073", 8),
                  ("SWE-PM-073", 4), ("SWE-PM-073", 6), ("SWE-PM-073", 7)], 1)]
    for tc in synth:
        tc["_file"] = "synth.json"
        tc["_provisional"] = True
    got = assign(synth)
    check("排序後之 req_id 序", [r["req_id"] for r in got],
          ["SWE-PM-071"] * 4 + ["SWE-PM-072"] * 2 + ["SWE-PM-073"] * 9)
    check("各 leaf 內 split_index 自 1 連號",
          [r["split_index"] for r in got],
          [1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    check("final_tc_id 自 001 起連號",
          [r["final_tc_id"] for r in got][:3] + [got[-1]["final_tc_id"]],
          ["NR1L-PowerManagement-001", "NR1L-PowerManagement-002",
           "NR1L-PowerManagement-003", "NR1L-PowerManagement-015"])

    # 缺 split_index 須報錯而非預設為 0
    try:
        assign([{"tc_id": "X", "req_id": "SWE-PM-071",
                 "_file": "s", "_provisional": True}])
        check("缺 split_index 應報錯", "未報錯", "ValueError")
    except ValueError:
        check("缺 split_index 應報錯", "ValueError", "ValueError")

    # 帶後綴之 req_id 須報錯（R-P86）
    try:
        assign([{"tc_id": "X", "req_id": "SWE-PM-071-01", "split_index": 1,
                 "_file": "s", "_provisional": True}])
        check("帶後綴之 req_id 應報錯（R-P86）", "未報錯", "ValueError")
    except ValueError:
        check("帶後綴之 req_id 應報錯（R-P86）", "ValueError", "ValueError")

    print(f"\n  G85 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    rows = assign(collect(GENERATED))
    header = ("row\tfinal_tc_id\tprovisional_tc_id\treq_id\tsplit_index"
              "\tfile\tis_provisional\n")
    body = "".join(
        f"{r['row']}\t{r['final_tc_id']}\t{r['provisional_tc_id']}\t{r['req_id']}"
        f"\t{r['split_index']}\t{r['file']}\t{r['is_provisional']}\n" for r in rows)
    path = DATA / "final_tc_id_map.tsv"
    path.write_text(header + body, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {len(rows)} 列")
    print("**本表為預覽，未改寫任何批次 JSON**（R-P113(c)：最終指派於 114 leaf 完成後）")
    for r in rows:
        print(f"  {r['row']:3}  {r['final_tc_id']}  ← {r['provisional_tc_id']}"
              f"  {r['req_id']}  split_index={r['split_index']}")


if __name__ == "__main__":
    main()
