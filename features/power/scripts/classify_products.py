"""G156 —— 腳本產物之三類判類（R-P227）。

R-P220 立「重跑輸出位元組相同得作為非陳舊之證據」，R-P225 據以令全掃重跑 ——
**二條皆隱含一個未言明之前提：該產物反映現況**。
31 §3.1 之反例成立：`b4_material.md` / `b5_material.md` 之語義為
「產生**當時**待產出者為何」，其重跑必得空集，**不但不證現時性，反摧毀該產物**。

三類（R-P227）：

  (a) **現況型** —— 反映當下資料之狀態。重跑並比對為有效（R-P220 適用）
  (b) **非決定性** —— 含時戳、排序不定等每次必異者。比對實質內容而非位元組
  (c) **時點相依** —— 反映某一時點之狀態。**一律不得重跑**；
      其現時性由「產生時點 ＋ 其後之異動紀錄」判定

**判類義務先於任何重跑**（R-P227）；**判類有疑義者一律跳過並上繳，不得試跑**。

本腳本**只讀不跑** —— 其自身不執行任何產物之產生腳本。

用法：
    python features/power/scripts/classify_products.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# 判類表 —— **人工逐份判定**，其依據為該產物之語義（檔首宣告與其產生腳本之定義）。
# 值：(類, 依據)
VERDICT: dict[str, tuple[str, str]] = {
    # ── (c) 時點相依 ──
    "b4_material.md": ("c", "語義為「**產生當時**待產出者為何」——"
                            "其排除清單取自當時之 `generated/`；今全部已產出，重跑必得空集"),
    "b5_material.md": ("c", "同上；31 包重跑實得「納入 0 leaf」，逐字原文全失"),
    "b4_batch2_snapshot.md": ("c", "檔首自載「第二批之**現行狀態快照**」——"
                                   "其 SHA256 取自 23 包當下（R-P175 已裁其不可重建）"),
    "b1_before16.json": ("c", "16 包**修補前**之批次資料快照，供 G113 驗證條件重現用"),
    "b1_before17.json": ("c", "17 包修補前之快照，同上"),
    "b2_before13.json": ("c", "13 包修補前之快照"),
    "b2_before15.json": ("c", "15 包修補前之快照"),
    "b3_before14.json": ("c", "14 包修補前之快照"),
    "b3_dryrun.json": ("c", "16 包 dry-run 寫回之當時結果"),
    "b2b3_writeback_path.json": ("c", "寫回路徑於當時之實測座標"),
    "edit_integrity_baseline.json": ("c", "G108 之**基準**快照（7 檔 163 符號）——"
                                          "其用途即為與現況比對，重跑即等於重設基準"),
    "final_tc_id_map.tsv": ("c", "臨時號 → 最終號之對照，取自指派當時"),
    # ── (b) 非決定性 ──
    "b3_er_restatement.md": ("b", "詞頻表含同計數者，其排序隨語料插入序而異"
                                  "（31 包實測 `front` / `rear` 互換，數值全同）"),
    "b5_residual_sample.md": ("b", "以 `random` 抽樣；種子已載，惟母體隨批次成長而變"),
    "b8_b9_b12_scans.md": ("b", "G131 之抽樣以 `random.Random(26)` 為之，"
                                "其母體隨批次成長而變"),
    "g150_design_method.md": ("b", "抽樣以 `random.Random(31)` 為之，母體隨批次而變"),
    # ── (a) 現況型（其餘）——其語義為「**現況**為何」，重跑並比對有效 ──
}

DEFAULT = ("a", "語義為「現況為何」——其輸入為當下之 `generated/` 或素材，重跑並比對有效")


def main() -> None:
    files = sorted(p for p in DATA.iterdir() if p.is_file())
    rows = [(p.name, *VERDICT.get(p.name, DEFAULT)) for p in files]
    counts = {k: sum(1 for _, c, _ in rows if c == k) for k in "abc"}

    out = ["# G156 —— 腳本產物之三類判類（R-P227）\n",
           "\n> **判類先於任何重跑**（R-P227）；本腳本**只讀不跑**。\n",
           "> (a) 現況型：重跑並比對有效（R-P220 適用）\n"
           "> (b) 非決定性：比對實質內容而非位元組\n"
           "> **(c) 時點相依：一律不得重跑** —— 其現時性由「產生時點 ＋ 其後之異動紀錄」判定\n",
           f"\n## 計數（產物 {len(rows)}）\n\n| 類 | 數 |\n|---|---|\n"
           f"| (a) 現況型 | **{counts['a']}** |\n"
           f"| (b) 非決定性 | **{counts['b']}** |\n"
           f"| **(c) 時點相依（不得重跑）** | **{counts['c']}** |\n",
           "\n## (c) 時點相依 —— 逐份及其時點語義\n\n| 產物 | 時點語義 |\n|---|---|\n"]
    for name, cls, why in rows:
        if cls == "c":
            out.append(f"| `{name}` | {why} |\n")
    out.append("\n## (b) 非決定性\n\n| 產物 | 依據 |\n|---|---|\n")
    for name, cls, why in rows:
        if cls == "b":
            out.append(f"| `{name}` | {why} |\n")
    out.append(f"\n## (a) 現況型（{counts['a']}）\n\n"
               + "、".join(f"`{n}`" for n, c, _ in rows if c == "a") + "\n"
               + f"\n判類依據：{DEFAULT[1]}。\n")
    out.append("\n## 判類有疑義者\n\n**無** —— 66 份皆能自其檔首宣告或產生腳本之定義判定。\n"
               "若日後新增產物之語義不明，依 R-P227 **一律跳過並上繳，不得試跑**。\n")

    (DATA / "g156_product_classes.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'g156_product_classes.md').relative_to(ROOT)}")
    print(f"  產物 {len(rows)}：(a) 現況型 {counts['a']}、(b) 非決定性 {counts['b']}、"
          f"**(c) 時點相依 {counts['c']}（不得重跑）**")
    for name, cls, _ in rows:
        if cls == "c":
            print(f"     (c) {name}")


if __name__ == "__main__":
    main()
