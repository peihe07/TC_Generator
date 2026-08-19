"""G215 —— 歷史臨時號對照表（R-P304）。

R-P304：寫回時之「臨時號 → 最終號」對照表須涵蓋**自 09 包首批以來之
全部歷史臨時號**，而非僅現行號 —— 既往各包所引之號多為合併前、重編前之值
（45 包所引之號即為 44 包合併前者，45 包已自陳；
 46 包所引之 `…-175`/`176` 亦然，本包實測確認）。

**歷史重編事件共二次**（自 git 史實查）：

| # | 包 | 事件 | 腳本 |
|---|---|---|---|
| 1 | 27 | 補測插入中段致號段衝突 → **全域重編** | `renumber_tc_ids.py` |
| 2 | 44 | 四對合併 264 → 260 → **保留原序補缺口** | `apply_merge_44.py` |

**對照之鍵**：`(req_id, tc_title)` —— 其於重編中不變
（27 包之腳本明載「不改動任何 TC 之內容，僅改 `tc_id`」；
 44 包之合併只改被保留者之 procedure / ER，其 `req_id` 與 `tc_title` 不變）。
**合併時被併入者無現行號**，其對照欄標為 `—（已併入 …-NNN）`。

用法：
    python features/power/scripts/build_tcid_history.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GEN = "features/power/generated"

# 各階段之代表 commit（其後即為該階段之號）
STAGES = [
    ("27 包重編前", "289bc2a~1"),
    ("27 包重編後", "289bc2a"),
    ("44 包合併前", "b83f88a~1"),
]
# 44 包合併之對照（保留者 ← 被併入者），取自 `apply_merge_44.PAIRS`
MERGED_INTO = {"006": "005", "102": "100", "107": "104", "176": "175"}


def at(ref: str) -> list[dict]:
    out = []
    for name in ("batch_001_power_down", "batch_002_timeout_settings",
                 "batch_003_power_state_a", "batch_004_power_state_b",
                 "batch_005_startup_display", "batch_006_branding_theme"):
        r = subprocess.run(["git", "show", f"{ref}:{GEN}/{name}.json"],
                           capture_output=True, text=True, cwd=ROOT)
        if r.returncode:
            continue
        out += json.loads(r.stdout)["tcs"]
    return out


def key(t: dict) -> tuple[str, str]:
    return (t["req_id"], t["tc_title"])


def main() -> None:
    stages = [(label, {key(t): t["tc_id"][-3:] for t in at(ref)})
              for label, ref in STAGES]
    cur = {key(t): t["tc_id"][-3:] for t in
           (json.loads(p.read_text(encoding="utf-8"))["tcs"]
            for p in sorted((ROOT / GEN).glob("*.json")) for t in [None])} \
        if False else {}
    cur = {}
    for p in sorted((ROOT / GEN).glob("*.json")):
        for t in json.loads(p.read_text(encoding="utf-8"))["tcs"]:
            cur[key(t)] = t["tc_id"][-3:]

    keys = sorted(set().union(*[set(s[1]) for s in stages], set(cur)),
                  key=lambda k: (int(re.search(r"\d+", k[0]).group()), k[1]))

    n_moved = {label: 0 for label, _ in stages}
    rows = []
    for k in keys:
        vals = [s[1].get(k) for s in stages]
        c = cur.get(k)
        # 被併入者：其於 44 包合併前有號而現行無
        note = ""
        if c is None and vals[-1] in MERGED_INTO:
            note = f"—（已併入 `…-{MERGED_INTO[vals[-1]]}` 之現行號）"
        rows.append((k, vals, c, note))
        for i, (label, _) in enumerate(stages):
            if vals[i] and c and vals[i] != c:
                n_moved[label] += 1

    out = ["# G215 —— 歷史臨時號對照表（R-P304）\n",
           "\n> **對照之鍵**：`(req_id, tc_title)` —— 其於二次重編中皆不變。\n",
           "> 27 包之腳本明載「不改動任何 TC 之內容，僅改 `tc_id`」；\n",
           "> 44 包之合併只改被保留者之 procedure / ER，`req_id` 與 `tc_title` 不變。\n",
           "\n## 一、歷史重編事件\n\n| # | 包 | 事件 | 腳本 |\n|---|---|---|---|\n",
           "| 1 | 27 | 補測插入中段致號段衝突 → **全域重編** | `renumber_tc_ids.py` |\n",
           "| 2 | 44 | 四對合併 264 → 260 → **保留原序補缺口** | `apply_merge_44.py` |\n",
           f"\n## 二、各階段與現行號之差異\n\n| 階段 | 與現行號相異之條數 |\n|---|---|\n"]
    for label, _ in stages:
        out.append(f"| {label} | **{n_moved[label]}** |\n")
    out.append(f"\n**現行 TC 數：{len(cur)}**；被併入而無現行號者 "
               f"**{sum(1 for _, _, c, n in rows if c is None and n)}** 條。\n")

    out.append("\n## 三、逐條對照\n\n| req_id | "
               + " | ".join(l for l, _ in stages)
               + " | **現行** | `tc_title` |\n|---|"
               + "---|" * (len(stages) + 2) + "\n")
    for (req, title), vals, c, note in rows:
        cells = " | ".join(f"`…-{v}`" if v else "—" for v in vals)
        cur_cell = f"**`…-{c}`**" if c else (note or "—")
        out.append(f"| `{req}` | {cells} | {cur_cell} | {title[:56]} |\n")

    p = DATA / "tcid_history_46.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"現行 TC {len(cur)}；逐條 {len(rows)} 列")
    for label, _ in stages:
        print(f"  {label}：與現行號相異 {n_moved[label]} 條")
    print(f"  被併入而無現行號者：{sum(1 for _, _, c, n in rows if c is None and n)} 條")


if __name__ == "__main__":
    main()
