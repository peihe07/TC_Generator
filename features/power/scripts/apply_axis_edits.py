"""B2 —— `axis` 187 條重判提案之套用（R-P278(a)）。

38 包已備複核素材（`input_data` 16 / `trigger_state` 12 / `mode` 8，共 36 條，
種子 38），而分析層迄未讀。
依 R-P253(a) 其前提（素材已備）具備，不得再推遲；
依 R-P272 之先例，**改值先於複核，抽樣素材同包呈出**。

**套用範圍**：有 `distinguishing_axis` 欄之 224 條中，
其現值**不在 §4.6 六值內**者 **187** 條。
合法而與提案相異者（37 條中之一部分）**不動** ——
其現值已合法且係 37 包經「依據逐字可見」之嚴格判準所改，
本包之提案不優於之（R-P236(b)：代理判準不凌駕實質判準）。

**⚠ 風險（R-P278(d)）**：其判準所依之描述欄與內文出自同一次撰寫；
若當初即誤解區分軸，二者會一致地錯（37 §G179 自陳）——
**抽樣複核為唯一之外部檢查**。

用法：
    python features/power/scripts/apply_axis_edits.py --dry-run
    python features/power/scripts/apply_axis_edits.py --apply
"""

from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GEN = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_axis import propose_axis  # noqa: E402
from verify_axis import AXIS_ENUM  # noqa: E402

BASE = re.compile(r"(SWE-PM-\d+)")


def main() -> None:
    apply = "--apply" in sys.argv
    if not apply and "--dry-run" not in sys.argv:
        raise SystemExit("須指定 --dry-run 或 --apply")

    files = {p: json.loads(p.read_text(encoding="utf-8"))
             for p in sorted(GEN.glob("*.json"))}
    tcs = [t for d in files.values() for t in d["tcs"]]
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)

    before = collections.Counter(
        t["distinguishing_axis"]["axis"] for t in tcs
        if t.get("distinguishing_axis"))
    log, skipped, unmapped = [], [], []

    for t in tcs:
        d = t.get("distinguishing_axis")
        if d is None:
            continue                                  # 40 條已依 R-P265 省略
        cur = d["axis"]
        leaf = BASE.match(t["req_id"]).group(1)
        prop, ev = propose_axis(t, by_leaf[leaf])
        if prop is None:                              # 理應不發生（無欄者已排除）
            unmapped.append(t["tc_id"])
            continue
        if cur in AXIS_ENUM:
            # 現值已合法 —— 不動（見模組首段之理由）
            if prop != cur:
                skipped.append((t["tc_id"], cur, prop, ev))
            continue
        log.append((t["tc_id"], cur, prop, ev))
        d["axis"] = prop

    after = collections.Counter(
        t["distinguishing_axis"]["axis"] for t in tcs
        if t.get("distinguishing_axis"))

    print(f"{'（乾跑）' if not apply else '（套用）'}套用 {len(log)} 條；"
          f"現值已合法而與提案相異者 {len(skipped)} 條（不動）")
    print(f"  改後非法者：{sum(v for k, v in after.items() if k not in AXIS_ENUM)}")

    out = ["# B2 —— `axis` 187 條重判提案之套用（R-P278）\n",
           f"\n> 模式：**{'套用' if apply else '乾跑'}**；改動 **{len(log)}** 條。\n",
           "> **套用範圍**：現值不在 §4.6 六值內者。\n",
           "> 現值已合法而與提案相異者 **不動** —— 其係 37 包經"
           "「依據逐字可見」之嚴格判準所改，本包之提案不優於之（R-P236(b)）。\n",
           "\n## 一、`axis` 值分布（前 → 後）\n\n| 值 | 合法 | 前 | 後 |\n|---|---|---|---|\n"]
    for k in sorted(set(before) | set(after)):
        out.append(f"| `{k}` | {'是' if k in AXIS_ENUM else '**否**'} | "
                   f"{before.get(k, 0)} | **{after.get(k, 0)}** |\n")
    out.append(f"\n## 二、現值已合法而與提案相異者 —— **{len(skipped)}** 條（不動）\n\n"
               "| tc | 現值 | 提案 | 依據 |\n|---|---|---|---|\n")
    for tid, cur, prop, ev in skipped:
        out.append(f"| `…-{tid[-3:]}` | `{cur}` | `{prop}` | {ev} |\n")
    out.append(f"\n## 三、逐條套用（{len(log)}）\n\n"
               "| tc | 舊 | 新 | 依據 |\n|---|---|---|---|\n")
    for tid, cur, prop, ev in log:
        out.append(f"| `…-{tid[-3:]}` | `{cur}` | **`{prop}`** | {ev} |\n")
    (DATA / "axis_edits_41.md").write_text("".join(out), encoding="utf-8")

    if apply:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                         encoding="utf-8")
        print(f"已寫回 {len(files)} 檔")
    else:
        print("未寫回（乾跑）")


if __name__ == "__main__":
    main()
