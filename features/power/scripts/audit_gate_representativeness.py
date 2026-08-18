"""G189 —— 以交集或抽樣為基礎之閘門盤點（R-P268）。

38 §九第 3 項：G150 之 `WALK` 交集自 38 包起持續縮小（本次 2 / 4 未走查），
**往後每次改值皆會再縮，該閘門之有效性將逐步歸零而不會報錯**。

此與 A-PW219（閘門有效而結果被擱置）**互為鏡像** ——
一者為閘門有效而輸出未用，一者為閘門形式存在而實質失效；
**二者於報表上皆呈現為「無異常」。**

R-P268(c) 令盤點所有屬此類之閘門。**判準二項**：

  甲 **抽樣型**：以 `random.Random(seed)` 自母體取樣 ——
     其結論僅對樣本有效，母體變動時樣本代表性隨之改變。
  乙 **硬編表型**：以人工產出之對照表（`WALK` / `ADJUDICATION` / `CLASSIFY`）
     逐條比對 —— **該表不可機械重生**（R-P214），
     母體變動時其交集縮小而**不會報錯**。

用法：
    python features/power/scripts/audit_gate_representativeness.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# （腳本, 閘門, 型, 母體與樣本之來源, 現況, 風險）
GATES: list[tuple[str, str, str, str, str, str]] = [
    ("audit_design_method.py", "G150", "**甲＋乙**",
     "自 `design_method` 最集中值之母體抽樣（種子 31），"
     "再以硬編之 `WALK`（32 包人工走查）逐條比對",
     "**有效樣本 2 / 4（50.0%）** —— 38 包改值後母體變動",
     "**最高** —— 二型兼具；母體每改一次交集即縮，且不報錯"),
    ("audit_priority.py", "G162", "**甲＋乙**",
     "自 P0 抽樣（種子 33），以硬編之 `CLASSIFY`（34 條人工歸類）比對",
     "38 包 `priority` 改值後 P0 由 193 降為 157 —— **母體已變動**",
     "**高** —— 同 G150 之形態，且其母體已於 38 包改變"),
    ("rejudge_design_method.py", "G154 / G155", "乙",
     "`ADJUDICATION` 為 33 包之逐條裁決表",
     "其鍵為 tc_id，不隨母體變動而失配；**惟其裁決內容係對舊值所作**",
     "中 —— 不會靜默失效，惟其裁決之前提（舊值）已改"),
    ("g113_buckets.py", "G113", "乙",
     "三個分桶之硬編清單（23 包逐項裁決）",
     "其標的為 `source_clause` 之 OR 分支，**不隨 TC 值改變**",
     "低 —— 母體為規格側，TC 改值不影響"),
    ("classify_products.py", "G156", "乙（惟有預設值）",
     "`VERDICT` 為 (b) / (c) 之例外表；**其餘由 `DEFAULT = (\"a\", …)` 自動歸類**",
     "39 包實測：`data/` 88 檔**全數已分類**（(a) 72 / (b) 4 / (c) 12）",
     "**低（訂正）** —— 初判為「未補者不報錯」係**誤判**："
     "其有預設值，新產物自動歸 (a)，無靜默缺口。"
     "**惟其反向風險為預設過寬** —— 新增之 (c) 型產物若未入 `VERDICT` "
     "會被誤歸 (a) 而遭重跑"),
    ("scan_clause_patterns.py", "G131–G133", "甲",
     "重疊對之 Jaccard 抽樣（種子 27）",
     "母體為 `source_clause`，**不隨 TC 值改變**",
     "低"),
    ("build_review_material_36.py", "—（備料）", "甲",
     "第 4 列抽樣 14 / 79（種子 36）",
     "備料非閘門，惟**其抽樣結論被 R-P261 用作改值之前提**",
     "**高** —— 2 / 14 之複核率被當作 79 條之前提（R-P261 已明載其限度）"),
    ("build_axis_review_38.py", "—（備料）", "甲",
     "三群各抽 ≥ 16.7%（種子 38）",
     "同上，備料非閘門",
     "中 —— 其複核尚未執行"),
]


def main() -> None:
    high = [g for g in GATES if g[5].startswith("**高") or g[5].startswith("**最高")]
    out = ["# G189 —— 以交集或抽樣為基礎之閘門盤點（R-P268）\n",
           "\n> **判準**：甲＝抽樣型（母體變動則樣本代表性隨之改變）；\n",
           "> 乙＝硬編表型（人工產出之對照表，不可機械重生，交集縮小而不報錯）。\n",
           f"\n## 一、彙總\n\n盤點 **{len(GATES)}** 項，其中風險**高或最高**者 **{len(high)}** 項。\n",
           "\n| 腳本 | 閘門 | 型 | 母體與樣本 | 現況 | 風險 |\n|---|---|---|---|---|---|\n"]
    for s, g, k, src, now, risk in GATES:
        out.append(f"| `{s}` | {g} | {k} | {src} | {now} | {risk} |\n")

    out.append("\n## 二、R-P268(a)(b) 之落實\n\n"
               "**(a) G150 已改為回報有效樣本數與母體數** —— 38 包即已實作"
               "（`{n} / {m} 條不在 32 包之人工走查表內`）。\n\n"
               "**(b) 50% 門檻之現況**：G150 本次有效樣本 **2 / 4 = 50.0%**，"
               "**恰在門檻上** —— 依 R-P268(b)「低於 50% 標為代表性不足」，"
               "本次尚未低於，惟**下次改值即會跌破**。\n\n"
               "**(c) 推及之結果**：上表 8 項中，\n"
               "- **G162 之母體已於 38 包變動**（P0 193 → 157）而**其 `CLASSIFY` 未更新**"
               " —— 與 G150 同型，且尚未加裝有效樣本之回報；\n"
               "- **G156 經查為誤判，已訂正** —— 其有 `DEFAULT = (\"a\", …)`，"
               "新產物自動歸類，`data/` 88 檔全數已分類，**無靜默缺口**；"
               "**其反向風險為預設過寬**（新增之 (c) 型若未入 `VERDICT` 會被誤歸 (a) 而遭重跑）；\n"
               "- 備料類（`build_review_material_36` / `build_axis_review_38`）雖非閘門，"
               "**其抽樣結論已被用作改值之前提**，風險等同。\n")

    p = DATA / "g189_gate_representativeness.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"盤點 {len(GATES)} 項；風險高或最高 {len(high)} 項：")
    for s, g, k, src, now, risk in GATES:
        print(f"  {g:12s} 型{k.replace('*','')}  {risk[:40]}")


if __name__ == "__main__":
    main()
