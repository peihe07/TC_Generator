"""W-VF45 —— VF230 之 Priority 預判與批次規劃（V16 §5；**不生成 TC**）。

**R-VS56 之 P0 二類係以 Part 1 之內容界定**（加熱元件、第三排頭枕下放），
VF230 **二者皆無**。故本腳本依其**原則**（canon §10.2 之七類）對映 VF230：

  P0(a) 實體致動且具傷害可能 —— 其驅動實體機構且乘員可能在其行程內
  P0(b) 熱源之啟用與失效     —— **VF230 無熱源功能，本類為空**
  P1    主要功能邏輯          —— 狀態同步、配置相依之控制項有無、顯示啟用
  P2    次要與診斷            —— 無效值、SNA、時序、前言型與適用性條件
  P3    不使用（R-VS56）

**P0(a) 之對映為本層之預判，非 R-VS56 之逐字**，逐簇列出待覆核
（W-VF45 第 1 項：預判與 TC 定稿後之判定不一致者於上繳具名）。

依 R-VF21／R-VF28 附三錨點，以內容定錨。

輸出：docs/reports/vf230_priority_batches.md ＋ data/_vf230_priority.json
"""
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# P0(a) 之簇 —— 逐簇具名，附「其驅動何機構、乘員何以可能在其行程內」
P0A: dict[str, str] = {
    "Power Tailgate": "電動尾門之開閉 —— 其行程內可能有人，夾傷可能",
    "Power Liftgate/Tailgate Alert": "電動尾門之警示 —— 同上，且警示失效即傷害可能",
    "Power Side Step": "電動側踏板之伸縮 —— 其行程貼近上下車者之足部",
    "Suspension Auto Entry or Exit": "上下車時車身自動升降 —— 實體升降且人正在其側",
    "Suspension Default Ride Height": "車身高度之致動 —— 同上",
    "Suspension Flash Lights With Lower": "車身降低之致動（其附隨閃燈）—— 同上",
    "Suspension Sound Horn With Lower": "車身降低之致動（其附隨鳴笛）—— 同上",
    "Suspension Service Mode": "維修模式之車身升降 —— 作業者可能在車下",
    "Driver Easy Exit Seat": "駕駛座椅之自動退移 —— 實體致動且人在座",
}
# P2 之形態（R-VS56：無效值、SNA、時序、前言與適用性條件）
P2_PAT = re.compile(
    r"\bSNA\b|invalid|<Tsend>|<Tdisplay>|shall ignore|are valid only if"
    r"|requirements in this section|This section (defines|applies)", re.I)


def main() -> None:
    lv = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (ROOT / "docs" / "reports" / "vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}

    rows = []
    for r in lv:
        leaf, title = r["swe_id"], r["title"].replace("\\n", " ")
        text = re.sub(r"\s+", " ", r["desc"])
        w = wr.get(leaf, {})
        if title in P0A:
            pri, why = "P0", f"P0(a) {P0A[title]}"
        elif P2_PAT.search(text):
            pri, why = "P2", "次要與診斷（無效值／SNA／時序／適用性條件）"
        else:
            pri, why = "P1", "主要功能邏輯（狀態同步、配置相依之控制項有無、顯示啟用）"
        rows.append({"leaf_id": leaf, "priority": pri, "why": why,
                     "test_set": w.get("test_set", ""), "layer3": title,
                     "writable": w.get("writable", ""),
                     "src_ref": r["src_ref"]})

    # --- 錨點（R-VF21／R-VF28）---
    a_p0 = next((x for x in rows if x["layer3"] == "Power Tailgate"), None)
    a_p1 = next((x for x in rows if x["layer3"] == "Speed Unit"), None)
    a_disc = next((x for x in rows if x["layer3"] == "Suspension Display Messages"), None)
    if not a_p0 or a_p0["priority"] != "P0":
        raise SystemExit("必命中錨點不符：`Power Tailgate` 應判 P0，停")
    if not a_p1 or a_p1["priority"] == "P0":
        raise SystemExit("必不命中錨點不符：`Speed Unit` 不應判 P0，停")
    if a_disc and a_disc["priority"] == "P0":
        raise SystemExit("鑑別錨點不符：`Suspension Display Messages` 為**訊息顯示**"
                         "而非車身致動，不應判 P0（一條以 `Suspension` 為鍵之"
                         "規則會誤判之），停")

    dist = Counter(x["priority"] for x in rows)
    # R-VS58 之選池優先序：P0→P1→P2；同序內逐 Test Set 輪流 ＋ reqid 升冪
    gen = [x for x in rows if x["writable"] in ("W0", "W1")]
    order = {"P0": 0, "P1": 1, "P2": 2}
    buckets: dict[tuple, list] = defaultdict(list)
    for x in gen:
        buckets[(order[x["priority"]], x["test_set"])].append(x)
    for v in buckets.values():
        v.sort(key=lambda z: int(re.sub(r"\D", "", z["src_ref"]) or 0))
    pool, i = [], 0
    while any(buckets.values()):
        for key in sorted(buckets):
            if buckets[key]:
                pool.append(buckets[key].pop(0))
        i += 1
        if i > 5000:
            raise SystemExit("選池迴圈未收斂，停")

    BATCH = 10
    nb = (len(pool) + BATCH - 1) // BATCH

    L = ["# W-VF45 —— VF230 之 Priority 預判與批次規劃（**不生成 TC**）", "",
         "## 0. 錨點（R-VF21 ／ R-VF28）", "",
         "| 錨點 | 簇 | 期望 | 實測 |", "|---|---|---|---|",
         f"| 必命中 | `Power Tailgate` | P0 | {a_p0['priority']} ✅ |",
         f"| 必不命中 | `Speed Unit` | 非 P0 | {a_p1['priority']} ✅ |",
         ("| **鑑別** | `Suspension Display Messages` | **非 P0** —— 其為訊息顯示"
          f"而非車身致動 | {a_disc['priority']} ✅ |" if a_disc else
          "| 鑑別 | `Suspension Display Messages` | — | 不存在 |"), "",
         "> **鑑別錨點之作用**：一條以 `Suspension` 為鍵之規則會把訊息顯示",
         "> 誤判為 P0。本方案逐簇具名，故不誤判。", "",
         "## 1. ⚠ R-VS56 之 P0 二類係以 Part 1 之內容界定，VF230 二者皆無", "",
         "R-VS56 之 P0(a) 為第三排頭枕下放、P0(b) 為加熱元件 ——"
         "**VF230 無頭枕下放、無加熱功能**。",
         "故本層依其**原則**（實體致動且具傷害可能／熱源）對映 VF230 之內容。",
         "**此對映為本層之預判，非 R-VS56 之逐字，逐簇列出待覆核。**", "",
         "### P0(a) 之簇（逐簇具名）", "",
         "| 簇 | leaf | 其驅動何機構、乘員何以可能在其行程內 |", "|---|---:|---|"]
    p0c = Counter(x["layer3"] for x in rows if x["priority"] == "P0")
    for t, n in p0c.most_common():
        L.append(f"| `{t}` | {n} | {P0A[t]} |")
    L += ["", f"**P0(b)（熱源）：0** —— VF230 無熱源功能。", "",
          f"## 2. 分布：P0 **{dist['P0']}** ／ P1 **{dist['P1']}** ／ "
          f"P2 **{dist['P2']}**（合計 {sum(dist.values())}）", "",
          "| Test Set | P0 | P1 | P2 | 合計 |", "|---|---:|---:|---:|---:|"]
    per = defaultdict(Counter)
    for x in rows:
        per[x["test_set"]][x["priority"]] += 1
    for t, c in sorted(per.items(), key=lambda x: -sum(x[1].values())):
        L.append(f"| {t} | {c['P0']} | {c['P1']} | {c['P2']} | {sum(c.values())} |")

    L += ["", "## 3. 選池順序（R-VS58）", "",
          "優先序 **P0 → P1 → P2**；同序內**逐 Test Set 輪流 ＋ reqid 升冪**。",
          f"可生成之池（`writable ∈ {{W0, W1}}`）= **{len(pool)}**"
          f"（627 − W2 {sum(1 for x in rows if x['writable']=='W2')} = {len(gen)}）。", "",
          "**前 20 條之順序**：", "",
          "| # | leaf | Pri | Test Set | writable |", "|---:|---|---|---|---|"]
    for i, x in enumerate(pool[:20], 1):
        L.append(f"| {i} | `{x['leaf_id']}` | {x['priority']} | {x['test_set']} | "
                 f"{x['writable']} |")

    L += ["", "## 4. 批次規劃（**待分析層核可，不得逕行生成**）", "",
          f"- 每批 **{BATCH}** 條（沿用 Part 1 之批量）",
          f"- 批數 **{nb}**（{len(pool)} 條）",
          f"- **pilot 批建議為第 1 批**：其含 P0 之前 10 條，"
          "涵蓋實體致動類 —— 風險最高者先驗其書寫形式",
          "", "**pilot 批之範圍與時點須待核可**（V16 §5 第 3 項）。"
          "**本輪未生成任何 TC。**", "",
          "## 5. 預判與定稿後判定之一致性", "",
          "**本表為選池時之預判**（R-VS58：以來源條文預判，非待 TC 寫成後）。",
          "**預判與 TC 定稿後之判定不一致者，須於其所屬批次之上繳具名**"
          "（W-VF45 第 1 項）。本輪無 TC，故無不一致可報。", ""]

    p = ROOT / "docs" / "reports" / "vf230_priority_batches.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_vf230_priority.json").write_text(json.dumps({
        "dist": dict(dist), "per_test_set": {k: dict(v) for k, v in per.items()},
        "pool": [x["leaf_id"] for x in pool], "batches": nb, "batch_size": BATCH,
        "p0_clusters": dict(p0c)}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Priority：{dict(dist)}；P0 簇 {len(p0c)} 個")
    print(f"選池 {len(pool)}；批數 {nb} × {BATCH}")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
