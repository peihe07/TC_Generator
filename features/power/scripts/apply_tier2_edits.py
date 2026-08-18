"""B2 —— 第二級改值：`design_method` ＋ `priority`（R-P261）。

其前提為分析層之抽樣複核，已於 37 / 38 包執行
（第 4 列 2 / 14、第 8 列 3 / 7）—— **涵蓋率不完整，代價由 R-P261 記明**。

### `design_method`

值＝ §12 之 first-match 結果（第 8 列已依 R-P259 訂正為功能數判準），
另加**三項逐條裁定**，其來源皆為條文或已完成之人工確認：

  `…-099`          → 第 9 列（35 包逐條人工確認：其 clause 僅單一條件）
  `…-026` / `…-027` → 第 4 列（**R-P260(a)**：結果由 `LTM High` 是否存在
                       與所選之值二條件共同決定；參數值之變更非第 3 列之狀態轉換）
  `…-028`          → 第 9 列（**R-P260(b)**，與機械結果一致）

**⚠ 標籤可用性之限制（停並回報，不自行擬定）**
§12 九列之標籤僅**四個**見於本語料：
第 2 列 `基礎故障注入 (Fault Injection Lite)`、
第 3 列 `狀態轉換 (State Transition Testing)`、
第 4 列 `決策表 (Decision Table Testing)`、
第 9 列 `功能測試 (Functional based ; no specific technique)`。
**第 1、5、6、8 列與「矛盾」無既有標籤**，而 §12 之完整標籤表不在本庫。
依 34 包 G167 與 36 包 §4.6 之先例，**執行層不自行擬定 canon 值** ——
該等 TC **本次不改**，逐條列出待分析層提供標籤。

### `priority`

依 G164 v2 之提案：**僅改「無 P0 類別命中而命中裝飾性／個人化」者 → P3**。
「無 P0 類別命中，亦非裝飾性」之 53 條為「提案人工裁決」，**非建議 P3**，
故**不改** —— R-P261(b) 之「建議 P3 40 條」即指前者。

用法：
    python features/power/scripts/apply_tier2_edits.py --dry-run
    python features/power/scripts/apply_tier2_edits.py --apply
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GEN = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_design_method import propose  # noqa: E402
from rejudge_priority import classify  # noqa: E402

# §12 列 → 標籤。**僅列出語料中已證實使用者**（見模組首段之限制）。
ROW_LABEL: dict[int, str] = {
    2: "基礎故障注入 (Fault Injection Lite)",
    3: "狀態轉換 (State Transition Testing)",
    4: "決策表 (Decision Table Testing)",
    9: "功能測試 (Functional based ; no specific technique)",
}

# 逐條裁定（來源見模組首段）。鍵為 tc_id 末三碼。
#
# `008` —— **R-P239（34 包）明裁「Fault Injection Lite 成立，維持」**。
# 其未由 first-match 之第 2 列命中，係 `ROW2_RE` 之**已知偽陰性**
# （A-PW178：該條之注入措詞為 `Stop the broadcast`，不含 `disconnect` /
#  `fault injection`），**非該值有誤**。
# 若不列入逐條裁定，first-match 會把一個經明文裁定為正確之值覆寫掉 ——
# 38 包乾跑實測：`基礎故障注入` 由 1 條變 **0** 條，即該回歸。
ADJUDICATED: dict[str, int] = {"099": 9, "026": 4, "027": 4, "028": 9, "008": 2}


def final_row(tc: dict) -> tuple[int | None, str]:
    """回傳（該 TC 之最終列, 依據）。"""
    tid = tc["tc_id"][-3:]
    if tid in ADJUDICATED:
        return ADJUDICATED[tid], "逐條裁定"
    row, _, hit = propose(tc)
    return row, f"first-match：{hit[:52]}"


def main() -> None:
    apply = "--apply" in sys.argv
    if not apply and "--dry-run" not in sys.argv:
        raise SystemExit("須指定 --dry-run 或 --apply")

    files = {p: json.loads(p.read_text(encoding="utf-8"))
             for p in sorted(GEN.glob("*.json"))}
    tcs = [t for d in files.values() for t in d["tcs"]]

    log, blocked, out_of_scope = [], [], []
    before_dm = collections.Counter(t["design_method"] for t in tcs)
    before_pr = collections.Counter(t["priority"] for t in tcs)

    for t in tcs:
        # ── design_method ──
        row, why = final_row(t)
        label = ROW_LABEL.get(row)
        if label is None:
            blocked.append((t["tc_id"], row, t["design_method"], why))
        elif t["design_method"] != label:
            log.append(("design_method", t["tc_id"], t["design_method"], label, why))
            t["design_method"] = label

        # ── priority ──
        # **受檢範圍即 G164 之範圍**：全部 P0 ＋ Branding and Theme 全 34 條。
        # 對全 264 條套用會多得 5 條（`…-156` / `157` / `200` / `201` / `226`，
        # 皆為 P1），惟其**不在 G164 之提案內**，
        # R-P261(b) 之「建議 P3 40 條」即指範圍內者 —— 逾範圍者不改，另行回報。
        in_scope = t["priority"] == "P0" or t["test_set"] == "Branding and Theme"
        hits, cosmetic = classify(t)
        if in_scope and not hits and cosmetic and t["priority"] != "P3":
            log.append(("priority", t["tc_id"], t["priority"], "P3",
                        "G164：無 §10.2 類別命中而命中裝飾性／個人化"))
            t["priority"] = "P3"
        elif not in_scope and not hits and cosmetic and t["priority"] != "P3":
            out_of_scope.append((t["tc_id"], t["priority"], t["tc_title"]))

    after_dm = collections.Counter(t["design_method"] for t in tcs)
    after_pr = collections.Counter(t["priority"] for t in tcs)
    by_field = collections.Counter(x[0] for x in log)

    print(f"{'（乾跑）' if not apply else '（套用）'}改動 {len(log)} 處：")
    for k, v in by_field.items():
        print(f"  {k}: {v}")
    print(f"  **標籤缺漏而未改：{len(blocked)} 條**")
    print(f"  **逾 G164 範圍而未改：{len(out_of_scope)} 條** "
          f"{[t[0][-3:] for t in out_of_scope]}")
    for tid, row, cur, why in blocked:
        print(f"     …-{tid[-3:]}  應為第 {row} 列（無既有標籤）  現值 {cur[:24]}")

    out = ["# B2 —— 第二級改值紀錄（R-P261）\n",
           f"\n> 模式：**{'套用' if apply else '乾跑'}**；改動 **{len(log)}** 處；"
           f"**標籤缺漏而未改 {len(blocked)} 條**。\n",
           "\n## 一、`design_method` 分布（前 → 後）\n\n| 值 | 前 | 後 |\n|---|---|---|\n"]
    for k in sorted(set(before_dm) | set(after_dm)):
        out.append(f"| {k} | {before_dm.get(k, 0)} | **{after_dm.get(k, 0)}** |\n")
    out.append("\n## 二、`priority` 分布（前 → 後）\n\n| 值 | 前 | 後 |\n|---|---|---|\n")
    for k in sorted(set(before_pr) | set(after_pr)):
        out.append(f"| {k} | {before_pr.get(k, 0)} | **{after_pr.get(k, 0)}** |\n")
    out.append(f"\n## 三、標籤缺漏而未改 —— **{len(blocked)}** 條\n\n"
               "> §12 之完整標籤表不在本庫；執行層**不自行擬定 canon 值**\n"
               "> （34 包 G167 / 36 包 §4.6 之先例）。待分析層提供。\n\n"
               "| tc | 應為 | 現值 | 依據 |\n|---|---|---|---|\n")
    for tid, row, cur, why in blocked:
        out.append(f"| `…-{tid[-3:]}` | 第 {row} 列 | {cur} | {why} |\n")
    out.append(f"\n## 三之二、逾 G164 受檢範圍而亦命中裝飾性者 —— **{len(out_of_scope)}** 條\n\n"
               "> 其不在 G164 之提案內（該提案之範圍為全部 P0 ＋ Branding and Theme），\n"
               "> 故**本包不改**；列出供分析層裁定是否納入下一輪。\n\n"
               "| tc | 現值 | `tc_title` |\n|---|---|---|\n")
    for tid, pr, title in out_of_scope:
        out.append(f"| `…-{tid[-3:]}` | {pr} | {title} |\n")
    out.append(f"\n## 四、逐條改動（{len(log)}）\n\n"
               "| 欄 | tc | 舊 | 新 | 依據 |\n|---|---|---|---|---|\n")
    for field, tid, old, new, why in log:
        out.append(f"| `{field}` | `…-{tid[-3:]}` | {old} | **{new}** | {why} |\n")
    (DATA / "tier2_edits.md").write_text("".join(out), encoding="utf-8")

    if apply:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                         encoding="utf-8")
        print(f"已寫回 {len(files)} 檔")
    else:
        print("未寫回（乾跑）")


if __name__ == "__main__":
    main()
