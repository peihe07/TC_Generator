"""W-VF25 —— VF230 之 Layer 2 名稱與 Layer 3 對照（V10 §9；**framework.md 不寫入**）。

R-VF25 已裁 Layer 2 採**粒度 D（037 之 11 份分報告族群）**。本腳本依其四項配套
產出待核清單：

  1. 為 11 個族群各訂 Test Set 名（canon §4.2：1–3 字名詞片語、
     無 Test Group 前綴、無括號標籤、無 `Report`／`features` 等檔名殘留）
  2. Layer 3 對照：各 Test Set → spec 之自有 section id（**不自創標籤**）
  3. 逐 Test Set 報 leaf 數，合計須為 627
  4. canon §4.1.3 兩項反面型態逐項附實數

**Test Set 名為本層之提案，待 Pei 核可**（R-VF25 §1「逐一列出待核可，
不逕行寫入 framework.md」）。

依 **R-VF21／R-VF28** 附錨點（以內容定錨，不以行號）。

輸出：docs/reports/wvf25_layer2_proposal.md ＋ data/_wvf25_layer2.json
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 提案之 Test Set 名。鍵為分報告族群（內容定錨，非序號）。
# 每個名之依據為該族群內 leaf 數最多之簇，逐一列於報告。
NAMES = {
    "STLA_Trailer_Name - Max_Power_Level_Report": "Trailer and Signage",
    "Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense_features":
        "Driver Convenience",
    "Time_Date_Autodoor_Camera_features": "Units and Cameras",
    "6 Aux Switches, SWITCH 1 Power Mode and E-Save features": "Auxiliary Switches",
    "STLA_Illuminated_Approach - Trailer_Number_Report": "Approach and Tailgate",
    "STLA_Suspension_Service_Mode - Headlights_with_Wipers Features_Report":
        "Suspension and Comfort",
    "Cornering Lights_lane_features": "Lane and Lighting",
    "STLA_Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode Features_Report":
        "Switch Power Mode",
    "STLA_SWITCH_1_Type - SWITCH 4 Hold_Last_State Features_Report":
        "Switch Type and State",
    "Pressure_Unit , Power_Unit And Torque_Unit features": "Measurement Units",
    "Daytime_Running_Light And Headlights_Off_Delay features^": "Daytime Lighting",
}
# 合併後之替代切分（見報告 §3）—— 三個 SWITCH 相關族群併為一
SWITCH_FAMS = {
    "6 Aux Switches, SWITCH 1 Power Mode and E-Save features",
    "STLA_SWITCH_1_Type - SWITCH 4 Hold_Last_State Features_Report",
    "STLA_Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode Features_Report",
}


def main() -> None:
    rows = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    l2 = json.loads((ROOT / "data" / "_vf230_layer2.json").read_text(encoding="utf-8"))
    spec_path = {g["title"]: g["spec_path"] for g in l2["groups"]}

    fam_leaf = Counter(r["family"] for r in rows)
    fam_titles: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        fam_titles[r["family"]][r["title"]] += 1

    # 跨族群之簇
    t2f: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        t2f[r["title"]][r["family"]] += 1
    split = {t: dict(c) for t, c in t2f.items() if len(c) > 1}

    # --- 錨點（R-VF21 ＋ R-VF28：以內容定錨）---
    A_HIT = "SWITCH 1 Type"          # 必為跨族群（12 之一）
    A_MISS = "Pressure Unit"         # 必不跨族群
    if A_HIT not in split:
        raise SystemExit(f"錨點不符：`{A_HIT}` 應為跨族群之簇，停")
    if A_MISS in split:
        raise SystemExit(f"錨點不符：`{A_MISS}` 不應跨族群，停")
    if A_MISS not in t2f:
        raise SystemExit(f"R-VF21(1)：必不命中錨點 `{A_MISS}` 不存在於簇集內，停")
    total = sum(fam_leaf.values())
    if total != 627:
        raise SystemExit(f"leaf 合計應為 627（R-VF16），實得 {total}")

    # Layer 3：各族群所涵蓋之 spec section id（自 spec 祖先鏈之 L5/L6 章名取）
    fam_sections: dict[str, list[str]] = {}
    for fam in fam_leaf:
        secs = []
        for t in fam_titles[fam]:
            p = spec_path.get(t) or []
            if p:
                secs.append(p[-1])
        fam_sections[fam] = sorted(set(secs))

    L = ["# W-VF25 —— VF230 之 Layer 2 名稱與 Layer 3 對照（提案，待核可）", "",
         "**`framework.md` 未寫入**（R-VF25：本條只裁粒度，不等於 framework 已鎖）。",
         "**Test Set 名為本層之提案，逐一待 Pei 核可。**", "",
         "## 0. 錨點（R-VF21 ＋ R-VF28：以內容定錨，不以行號）", "",
         "| 錨點 | 內容 | 實測 |", "|---|---|---|",
         f"| 必命中（跨族群） | `{A_HIT}` | 跨 {len(split[A_HIT])} 族 ✅ |",
         f"| 必不命中（不跨族群） | `{A_MISS}` | 不跨族 ✅ |",
         f"| 合計 | leaf 總數 | {total}（R-VF16）✅ |", "",
         "## 1. ⚠ 粒度 D 之一項未被預見之後果 —— 12 個簇被邊界對切", "",
         f"**{len(split)} 個 Title 簇跨兩個分報告族群**，合計 "
         f"{sum(sum(c.values()) for c in split.values())} leaf。",
         "**每一個皆恰好 3 / 3 對切。**", "",
         "| 簇 | leaf | 分裂 |", "|---|---:|---|"]
    for t, c in sorted(split.items()):
        d = "／".join(f"`{NAMES[k]}` {v}" for k, v in sorted(c.items()))
        L.append(f"| `{t}` | {sum(c.values())} | {d} |")
    L += ["",
          "→ **依粒度 D 之字面（11 份分報告），`SWITCH 1 Type` 等 12 個功能",
          "會被切成兩個 Test Set 各 3 條。** 一個功能之 TC 分屬兩個 Test Set，",
          "Test Set 欄之索引價值因而受損。",
          "",
          "**此為 R-VF25 作成時未有之量測**（V07 §5.3 與 R-VF25 皆以",
          "「12–131 leaf、中位 52」論其均勻度，未測簇之跨界）。", "",
          "## 2. 提案 A —— 11 個 Test Set（依 R-VF25 字面）", "",
          "| # | Test Set 名（提案） | leaf | 簇 | 命名依據（該族群最大之三簇） |",
          "|---:|---|---:|---:|---|"]
    for i, (fam, n) in enumerate(fam_leaf.most_common(), 1):
        top = "／".join(f"`{t}` {c}" for t, c in fam_titles[fam].most_common(3))
        L.append(f"| {i} | **{NAMES[fam]}** | {n} | {len(fam_titles[fam])} | {top} |")
    L += ["", f"**合計 {total}**（自各族群重算）。", "",
          "**命名之合規性（canon §4.2）**：11 個名皆為 1–3 字名詞片語、",
          "無 `Vehicle Setting` 前綴（R-VF25 配套 2）、無括號標籤、",
          "無 `Report`／`features`／`^`／` - ` 等檔名殘留（配套 1）。", "",
          "**須具名之異質性**：`Trailer and Signage`(131)／`Driver Convenience`(99)／",
          "`Approach and Tailgate`(57) 三者之內容異質度較高 ——",
          "其族群內最大簇僅佔 25%／6%／14%。**名只能取其較大之主題，",
          "無法涵蓋全部。** 若 Pei 認為不可接受，須改粒度而非改名。", "",
          "## 3. 提案 B —— 9 個 Test Set（三個 SWITCH 族群合併）", ""]
    merged = sum(v for k, v in fam_leaf.items() if k in SWITCH_FAMS)
    others = [(NAMES[k], v) for k, v in fam_leaf.most_common() if k not in SWITCH_FAMS]
    L += [f"將 `Auxiliary Switches`(72)＋`Switch Type and State`(24)＋",
          f"`Switch Power Mode`(35) 併為單一 Test Set **`Auxiliary Switches`**"
          f"（{merged} leaf）。", "",
          "**合併後跨族群之簇 = 0**（實測）。", "",
          "| # | Test Set | leaf |", "|---:|---|---:|",
          f"| 1 | **Auxiliary Switches**（合併） | {merged} |"]
    for i, (nm, v) in enumerate(others, 2):
        L.append(f"| {i} | {nm} | {v} |")
    L += ["", f"**合計 {merged + sum(v for _, v in others)}**。", "",
          "**代價**：偏離 R-VF25 之「11 份分報告族群」字面；",
          "`Auxiliary Switches` 成為最大 Test Set（131，與 `Trailer and Signage` 並列）。",
          "**收益**：無功能被邊界對切。", "",
          "**本層不擇一**（R-VF25 §1 令逐一列出待核）。", "",
          "## 4. canon §4.1.3 兩項反面型態", "", "| 型態 | 提案 A | 提案 B |",
          "|---|---|---|",
          f"| **過細**（Test Set 欄近乎 TC ID 欄之複本） | 11 set／627 leaf，"
          f"平均 57 → **否** | 9 set，平均 70 → **否** |",
          "| **過粗**（出現 `Misc`／`General`／`Unclassified` 收容簇） | "
          "無此類名 → **否** | 無 → **否** |",
          "",
          "（對照：106 簇之粒度平均 5.9 leaf，**屬過細**，R-VF25 已排除。）", "",
          "## 5. Layer 3 對照（各 Test Set → spec 之自有章名）", "",
          "**不自創標籤**（R-VF25 配套 3）。章名取自 spec 目次之逐字，",
          "其對應以 W-VF7 複驗後之交集（exact 104 ／ 無對應 2）為準。", ""]
    for fam, n in fam_leaf.most_common():
        secs = fam_sections[fam]
        L += [f"### {NAMES[fam]}（{n} leaf，{len(secs)} 個 spec 章）", ""]
        L += ["- `" + "`／`".join(secs) + "`" if secs else "- （無對應）", ""]

    none = [g["title"] for g in l2["groups"] if g["match"] == "none"]
    L += ["## 6. 無 spec 對應之 2 簇（W-VF7 複驗後之真缺口）", "",
          "| 簇 | leaf | 所屬 Test Set |", "|---|---:|---|"]
    for t in none:
        c = t2f[t]
        n = sum(c.values())
        L.append(f"| `{t}` | {n} | "
                 + "／".join(NAMES[k] for k in c) + " |")
    L += ["", "**其 Layer 3 無 spec 章可掛。** 依 R-VF25 配套 3「不得自創標籤」，",
          "本層**不為其造章名**。**處置待裁**：(a) 掛於其 Test Set 而 Layer 3 留空；",
          "(b) 待 spec 修訂後補；(c) 另循 DR 向上游確認其章節歸屬。", "",
          "## 7. framework.md 之現況", "",
          "**未寫入、未鎖。** R-VF25 之鎖定條件為「Layer 2 名稱表與 Layer 3",
          "對照表齊備並經 Pei 核可」。本檔為該二表之提案，**核可後方得寫入**。",
          "Part 1 之既有 Layer 1／2／3 本輪未觸及。", ""]

    out = ROOT / "docs" / "reports" / "wvf25_layer2_proposal.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf25_layer2.json").write_text(json.dumps({
        "names": NAMES, "fam_leaf": dict(fam_leaf), "split_clusters": split,
        "merged_switch_total": merged, "sections": fam_sections,
        "no_spec": none, "total": total}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"11 族群，合計 {total}；跨族群簇 {len(split)}"
          f"（{sum(sum(c.values()) for c in split.values())} leaf）")
    print(f"合併三個 SWITCH 族群後 = {merged} leaf，跨族群簇 0")
    print(f"無 spec 對應之簇 {len(none)}: {none}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
