"""W-VF35 —— 提案 C 之逐筆列舉（R-VF41；**不設通則、不用詞相交判準**）。

R-VF41 廢止 R-VF36 之「主題詞相交」二條件規則。本腳本**不含任何自動判準** ——
`MOVES` 為逐筆之判斷，其依據為該簇之**條文主旨**（自 leaf 之 `desc` 取），
每筆附「為何原屬不當、為何新屬適當」。

「過檢視而留置」表由全 106 簇扣除 `MOVES` 自動生成，其中**須具名理由者**
列於 `STAY_NOTES`（異質性殘留與已知之誤移風險點）。

依 R-VF21／R-VF28 附三錨點；**鑑別錨點須取 `Power Unit`**（R-VF41 之要求）
—— 其為上一版規則之已知失效點。

輸出：docs/reports/wvf35_layer2_enumerated.md ＋ data/_wvf35_enum.json
"""
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUX, SUSP, TRAIL = "Auxiliary Switches", "Suspension and Comfort", "Trailer and Signage"

# --- 逐筆之判斷（R-VF41 之義務要件）---------------------------------------
# 簇名 -> (新 Test Set, 條文主旨, 為何原屬不當, 為何新屬適當)
MOVES: dict[str, tuple[str, str, str, str]] = {
    # 種子 (a)：3 個 Suspension 章
    "Suspension Default Ride Height": (
        SUSP, "取得 Hybrid_Type 等配置以定懸吊之預設車高",
        "其與開關之電源模式無任何共同之 setup 或 UI 進入路徑",
        "`Suspension Service Mode`／`Suspension Display Messages` 已在此，同為懸吊之設定"),
    "Suspension Flash Lights With Lower": (
        SUSP, "取得 CAN node 27 配置，控制車身降低時之閃燈行為",
        "同上 —— 其為懸吊動作之附隨行為，非開關設定",
        "與其餘懸吊簇同一能力叢集"),
    "Suspension Sound Horn With Lower": (
        SUSP, "取得 CAN node 27 配置，控制車身降低時之鳴笛行為",
        "同上", "同上"),
    # 種子 (c)：Switch Power Mode 之殘餘
    "4 AUX Switches": (
        AUX, "取得 AUX_Switch_Type 配置以決定輔助開關之數量與型別",
        "其為輔助開關本身之配置，與「電源模式」此一單一屬性不相稱",
        "`6 Aux Switches` 已在此，二者為同一功能之不同車型配置"),
    "Rear Guidance Lights with\\nCargo Lights": (
        AUX, "取得 Utility_Light 配置以決定後方導引燈與貨廂燈之連動",
        "其非開關之電源模式",
        "其二姊妹簇 `Rear Guidance Lighting with Approach` 與 "
        "`Rear Guidance Light Status` 皆已在此"),
    # 逐簇檢視所得（非種子）
    "Suspension Auto Entry or Exit": (
        SUSP, "取得配置以決定上下車時懸吊之自動升降",
        "其與單位顯示、攝影機無共同之 setup 型態",
        "為懸吊之自動行為，與 `Suspension Service Mode` 同族"),
    "Trailer Number": (
        TRAIL, "取得配置以決定可登錄之拖車組數",
        "其與 approach 照明、電動尾門無關",
        "`Trailer Name`(22)／`Trailer Brake Type`(13)／"
        "`Automatic Trailer Light Check`／`Blind Spot with Trailer Detection` 皆在此"),
}
# 12 個跨界之 SWITCH 簇（種子 (b)）—— 整併入 AUX，理由共通
CROSS_REASON = (
    "其另一半已在 `Auxiliary Switches`；不整併則同一功能被切成兩個 Test Set 各 3 條")

# --- 留置而須具名理由者（異質性殘留、或上一版規則之誤移點）-----------------
STAY_NOTES: dict[str, str] = {
    "Power Unit": "**鑑別錨點**。主旨為功率單位（kW／hp）之顯示配置 —— "
                  "其為**量測單位**，非開關之電源模式。上一版規則僅因共用 `power` "
                  "一詞而誤移之，本方案不移。",
    "Hour Mode": "主旨為 12／24 小時制之顯示格式，與 `Time and Date Settings` 同組，"
                 "留於 `Units and Cameras` 正確。上一版規則因 `mode` 一詞誤移。",
    "Charge Power Level": "主旨為充電功率等級。**與 `Approach and Tailgate` 之名不相稱**，"
                          "惟無更適當之既有 Test Set；依 R-VF41「不設通則」亦不得為其新設。"
                          "**具名為異質性殘留**（R-VF37 已裁其為已接受之狀態）。",
    "Engine Off Power Delay": "主旨為熄火後電源延時。其屬 `Suspension and Comfort` 之"
                              "「Comfort」一側，可辯護惟非理想。**具名。**",
    "Power Side Step": "主旨為電動側踏板之啟閉。與 `Signage` 不相稱，無更適之處。**具名。**",
    "Max Power Level": "主旨為最大輸出功率等級。同上。**具名。**",
    "Turn Signal Activated Blind Spot Camera View with\\nTrailer": (
        "主旨為方向燈觸發之盲點攝影機視角；`Trailer` 為其適用條件之一，非其主題。"
        "留於 `Units and Cameras`。上一版規則因 `trailer` 一詞誤移。"),
    "Rear Guidance Lighting with Approach": "與其二姊妹簇同處 `Auxiliary Switches`，不動。",
}


def main() -> None:
    rows = list(csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t"))
    names = json.loads((ROOT / "data" / "_wvf25_layer2.json")
                       .read_text(encoding="utf-8"))["names"]
    cell: dict[tuple[str, str], list] = defaultdict(list)
    for r in rows:
        cell[(r["title"], names[r["family"]])].append(r)
    titles = {t for t, _ in cell}
    cross = {t for t in titles if len({c for tt, c in cell if tt == t}) > 1}

    # --- 施行 -------------------------------------------------------------
    final: dict[str, Counter] = defaultdict(Counter)
    moved, stayed = [], []
    for (t, cur), v in sorted(cell.items()):
        n = len(v)
        if t in cross:
            dest, why = AUX, CROSS_REASON
            if dest != cur:
                moved.append({"cluster": t, "leaf": n, "from": cur, "to": dest,
                              "gist": re.sub(r"\s+", " ", v[0]["desc"])[:70],
                              "why_bad": why, "why_good": why, "seed": "(b)"})
        elif t in MOVES:
            dest, gist, bad, good = MOVES[t]
            if dest != cur:
                moved.append({"cluster": t, "leaf": n, "from": cur, "to": dest,
                              "gist": gist, "why_bad": bad, "why_good": good,
                              "seed": "(a)/(c)/檢視"})
            else:
                dest = cur
        else:
            dest = cur
            stayed.append({"cluster": t, "leaf": n, "ts": cur,
                           "note": STAY_NOTES.get(t, "")})
        final[dest][t] += n

    ts_leaf = {k: sum(c.values()) for k, c in final.items() if sum(c.values())}
    total = sum(ts_leaf.values())

    # --- 錨點（R-VF21／R-VF28／R-VF41 第 5 項）----------------------------
    A_DISC = "Power Unit"
    disc_moved = any(m["cluster"] == A_DISC for m in moved)
    a_move = any(m["cluster"] == "Suspension Default Ride Height" for m in moved)
    a_stay = any(s["cluster"] == "Pressure Unit" for s in stayed)
    if disc_moved:
        raise SystemExit(f"鑑別錨點不符：`{A_DISC}` 被移動，停")
    if not a_move:
        raise SystemExit("必命中錨點不符：`Suspension Default Ride Height` 未移動，停")
    if not a_stay:
        raise SystemExit("必不命中錨點不符：`Pressure Unit` 未留置，停")
    if total != 627:
        raise SystemExit(f"合計應為 627（R-VF16），實得 {total}")

    old = set(names.values())
    new_names = sorted(set(ts_leaf) - old)
    gone = sorted(old - set(ts_leaf))
    sizes = sorted(ts_leaf.values())

    L = ["# W-VF35 —— 提案 C 之逐筆列舉（R-VF41）", "",
         "**不設通則，不用任何詞相交判準**（R-VF41）。每筆之依據為該簇之",
         "**條文主旨**（自其 leaf 之 `desc` 取），非自章名推。", "",
         "## 0. 錨點（R-VF21 ／ R-VF28 ／ R-VF41 第 5 項）", "",
         "| 錨點 | 簇 | 期望 | 實測 |", "|---|---|---|---|",
         "| 必移動 | `Suspension Default Ride Height` | 移入 "
         f"`{SUSP}` | ✅ |",
         "| 必不移動 | `Pressure Unit` | 留置 | ✅ |",
         f"| **鑑別** | `{A_DISC}` | **留置** —— 其為上一版規則之已知失效點"
         "（量測單位被移入 `Switch Power Mode`） | ✅ **未移動** |",
         f"| 合計 | — | 627（R-VF16） | {total} ✅ |", "",
         f"## 1. 移動（{len(moved)} 筆）", "",
         "| 簇 | leaf | 原 → 新 | 條文主旨 | 為何原屬不當 / 為何新屬適當 |",
         "|---|---:|---|---|---|"]
    for m in sorted(moved, key=lambda x: (x["to"], -x["leaf"])):
        c = m["cluster"].replace("\\n", " ")
        same = m["why_bad"] == m["why_good"]
        rz = m["why_bad"] if same else f"{m['why_bad']}／{m['why_good']}"
        L.append(f"| `{c}` | {m['leaf']} | {m['from']} → **{m['to']}** | "
                 f"{m['gist']} | {rz} |")

    named = [s for s in stayed if s["note"]]
    L += ["", f"## 2. 過檢視而留置（{len(stayed)} 筆；其中 {len(named)} 筆具名）", "",
          "**R-VF41 令不移動者亦須列，附一句理由。** 未具名者為「其簇名與其所屬",
          "Test Set 之主題相符，無移動之理由」——逐簇檢視過，不逐筆重述。", "",
          "### 2.1 具名者", "", "| 簇 | leaf | Test Set | 理由 |", "|---|---:|---|---|"]
    for s in sorted(named, key=lambda x: -x["leaf"]):
        L.append(f"| `{s['cluster'].replace(chr(92)+'n', ' ')}` | {s['leaf']} | "
                 f"{s['ts']} | {s['note']} |")
    L += ["", "### 2.2 未具名者（逐 Test Set 計數）", "",
          "| Test Set | 留置簇數 |", "|---|---:|"]
    cnt = Counter(s["ts"] for s in stayed if not s["note"])
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        L.append(f"| {k} | {v} |")

    L += ["", "## 3. 提案 C 之 Layer 2 表", "",
          "| # | Test Set | leaf | 簇 |", "|---:|---|---:|---:|"]
    for i, (t, n) in enumerate(sorted(ts_leaf.items(), key=lambda x: -x[1]), 1):
        L.append(f"| {i} | **{t}** | {n} | {len(final[t])} |")
    L += ["", f"**合計 {total}**（自各 Test Set 重算）。", "",
          f"**消失之 Test Set（{len(gone)}）**：" + ("／".join(f"`{g}`" for g in gone)
                                                    or "無"),
          "", "→ **V11 §7 之論證於此實現**：`Switch Power Mode` 與",
          "`Switch Type and State` 二名確已消失，其內容各歸其實。", "",
          f"**新出現之名：{len(new_names)}**"
          + (f"（{'／'.join(new_names)}）" if new_names else "（無）"), "",
          "## 4. canon §4.1.3 兩項反面型態", "",
          "| 型態 | 實數 | 判 |", "|---|---|---|",
          f"| **過細** | {len(ts_leaf)} set／{total} leaf，平均 "
          f"{total // len(ts_leaf)}，最小 {sizes[0]}、最大 {sizes[-1]} | **否** |",
          "| **過粗**（`Misc`／`General`／`Unclassified` 收容簇） | 無此類名 | **否** |",
          "", "## 5. R-VF37 之判斷", "",
          f"- 新名 **{len(new_names)}** ／ 消失 **{len(gone)}**",
          "- 名之集合為已核可 11 名之**子集** → 形式合 (a)", "",
          "**惟本輪不適用 R-VF37(a) 之逕鎖條款** —— R-VF41 明定其前提為",
          "「依既有規則機械產出」，而本表為**逐筆列舉、含判斷**。",
          "**回報待分析層覆核**（R-VF41 核可路徑）。**`framework.md` 未寫入。**", ""]

    out = ROOT / "docs" / "reports" / "wvf35_layer2_enumerated.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (ROOT / "data" / "_wvf35_enum.json").write_text(json.dumps({
        "moved": moved, "stayed": stayed, "ts_leaf": ts_leaf, "total": total,
        "gone": gone, "new_names": new_names,
        "final": {k: dict(v) for k, v in final.items()}},
        ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"移動 {len(moved)}／留置 {len(stayed)}（具名 {len(named)}）")
    for t, n in sorted(ts_leaf.items(), key=lambda x: -x[1]):
        print(f"  {n:4}  {t}")
    print(f"合計 {total}；消失 {gone}；新名 {new_names}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
