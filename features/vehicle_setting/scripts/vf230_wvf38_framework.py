"""W-VF38 —— VF230 之 Layer 1／2／3 寫入 `framework.md` 並鎖定（R-VF44）。

R-VF44 之四項附帶條件：
  1. Layer 3 對照須含 R-VF43 之標註 —— SWITCH 1–4 之 Power Mode 4 簇標明
     含兩種條文形態；**SWITCH 5／6 不加該標註**（W-VF36 實測其無兩種形態）
  2. `E-Save`／`CHMSL CAMERA DYNAMIC CENTERLINE` 之 Layer 3 **留空且可見**
     （R-VF34），不得以鄰近章名填充
  3. **Part 1 之既有 Layer 1／2／3 一律不動**
  4. 鎖定後 Test Set 名進入凍結

本腳本**只附加**一節於 `framework.md` 之末，不改其既有任何一行；
重跑時先移除自身所產之節再重生（冪等）。

依 R-VF21／R-VF28 附錨點，以內容定錨。
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FW = ROOT / "framework.md"
BEGIN = "<!-- VF230-BEGIN (W-VF38) -->"
END = "<!-- VF230-END -->"
# R-VF43：含兩種條文形態者（W-VF29 實測）—— 僅 SWITCH 1–4 之 Power Mode
DUAL_FORM = {f"SWITCH {i} Power Mode" for i in (1, 2, 3, 4)}


def main() -> None:
    enum = json.loads((ROOT / "data" / "_wvf35_enum.json").read_text(encoding="utf-8"))
    l2 = json.loads((ROOT / "data" / "_vf230_layer2.json").read_text(encoding="utf-8"))
    spec_path = {g["title"]: g["spec_path"] for g in l2["groups"]}
    no_spec = {g["title"] for g in l2["groups"] if g["match"] == "none"}
    final = enum["final"]
    ts_leaf = enum["ts_leaf"]
    total = enum["total"]

    # --- 錨點（R-VF21／R-VF28）---
    if total != 627:
        raise SystemExit(f"R-VF16：合計應為 627，實得 {total}")
    if len(ts_leaf) != 9:
        raise SystemExit(f"R-VF44：Test Set 應為 9，實得 {len(ts_leaf)}")
    if "Switch Power Mode" in ts_leaf or "Switch Type and State" in ts_leaf:
        raise SystemExit("R-VF44：二不成立之 Test Set 名未消失，停")
    if not no_spec >= {"E-Save"}:
        raise SystemExit("R-VF34 錨點：`E-Save` 應為無 spec 對應，停")
    # 鑑別錨點：`Power Unit` 須在 `Measurement Units`，非 Switch 相關
    pu = [t for t, c in final.items() if "Power Unit" in c]
    if pu != ["Measurement Units"]:
        raise SystemExit(f"鑑別錨點不符：`Power Unit` 在 {pu}，應在 Measurement Units")
    print(f"錨點：合計 {total} ✅／Test Set {len(ts_leaf)} ✅／"
          f"二名已消失 ✅／`Power Unit` 在 {pu[0]} ✅")

    L = [BEGIN, "",
         "---", "",
         "# Vehicle Setting / VF230（Part 2）—— framework（Layer 1–3）", "",
         "**狀態：已核可並鎖定。** 分析層依 **R-VF44** 核可（2026-08-23），"
         "依 **R-VF41** 之核可路徑（名單為已核可 11 名之子集者由分析層覆核）。", "",
         "**Part 1（CFTS044）之 Layer 1／2／3 一律不動**（R-VF44 附帶條件 3）——"
         "本節為附加，未改上方任何一行。", "",
         "## Layer 1", "",
         "`Vehicle Setting`（**R-VF9**：兩本 workbook 同值，明示排除 R-C6）。", "",
         f"## Layer 2 —— 9 個 Test Set，合計 {total}", "",
         "粒度為 **提案 C**（R-VF36／R-VF41）：以 037 之 11 份分報告族群為基底，"
         "語義明顯錯置之簇逐筆移至名實相符之 Test Set。",
         "**逐筆列舉之依據見 `docs/reports/wvf35_layer2_enumerated.md`**"
         "（19 移動／87 留置，各附條文主旨與雙向理由）。", "",
         "| # | Test Set | leaf | 簇 |", "|---:|---|---:|---:|"]
    order = sorted(ts_leaf.items(), key=lambda x: -x[1])
    for i, (t, n) in enumerate(order, 1):
        L.append(f"| {i} | **{t}** | {n} | {len(final[t])} |")
    L += ["", f"**合計 {total}**（自各 Test Set 重算 —— R-VF16 之母體）。", "",
          "**已消失之二名**：`Switch Power Mode`／`Switch Type and State` ——"
          "其名與其主要內容不符（V11 §7），內容各歸其實。", "",
          "**Test Set 名自本鎖定起凍結**（R-VF44 附帶條件 4）：其變更須經 Pei，"
          "不得由任一層自裁。", "",
          "### 已裁定接受之異質性（R-VF37；**不得作為 pilot review 之 defect**）", "",
          "下列簇之主旨與其所屬 Test Set 之名不完全相稱，而無更適當之既有 "
          "Test Set；依 R-VF41「不設通則」亦不得為其新設：", ""]
    named = {s["cluster"]: s for s in enum["stayed"] if s["note"]}
    for c, s in sorted(named.items(), key=lambda x: -x[1]["leaf"]):
        L.append(f"- `{c.replace(chr(92)+'n', ' ')}`（{s['leaf']} leaf，{s['ts']}）")

    L += ["", "## Layer 3 —— 各 Test Set 之 spec 章名", "",
          "**取自 spec 之自有章名，不自創標籤**（R-VF25 配套 3）。"
          "**不寫入工作簿**（canon §4.1.5）。", ""]
    for t, n in order:
        L += [f"### {t}（{n} leaf）", "", "| spec 章名 | leaf | 註 |", "|---|---:|---|"]
        for c, ln in sorted(final[t].items(), key=lambda x: -x[1]):
            disp = c.replace("\\n", " ")
            if c in no_spec:
                chap, note = "**（無 spec 對應）**", "R-VF34：留空且可見，不以鄰近章名填充"
            else:
                p = spec_path.get(c) or []
                chap = f"`{p[-1]}`" if p else "`—`"
                note = ("**R-VF43：含兩種條文形態**（顯示／HW 通知／HMI 送出）——"
                        "其 leaf 不得因同簇而逕作 sibling；`reasoning` 須具名其形態"
                        if c in DUAL_FORM else "")
            L.append(f"| {chap}（簇 `{disp}`） | {ln} | {note} |")
        L.append("")

    L += ["## 鎖定註記", "",
          "**一、Layer 2 之分組立於本層對條文主旨之判斷，非上游之切分準則**"
          "（R-VF47 二）。037 之 11 份分報告將同一功能之 6 條需求分置兩份"
          "（12 個功能如此），其切分依據**未經上游查證** —— 已開 DR 待覆。",
          "**本註記依 R-VF47 二只記一次，不逐輪重提。**", "",
          "**二、R-VF34 之 2 簇**（`E-Save` 6 leaf／`CHMSL CAMERA DYNAMIC CENTERLINE` "
          "5 leaf）之 Layer 3 留空 —— 其 leaf **仍計入 627 與其 Test Set**，"
          "Layer 3 為導航工具而非可測性之判準（canon §4.1.4／§4.1.5）。", "",
          "**三、SWITCH 5／6 不加 R-VF43 標註** —— W-VF36 實測其"
          "**完全無「HMI 送出」類需求**（1–4 各 2 條、5／6 各 0 條），"
          "故其無兩種形態。**其成因未查，已開 DR 待覆。**", "",
          END, ""]

    src = FW.read_text(encoding="utf-8")
    if BEGIN in src:                       # 冪等：先移除自身所產之節
        src = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "",
                     src, flags=re.S)
    FW.write_text(src.rstrip("\n") + "\n\n" + "\n".join(L), encoding="utf-8")
    print(f"framework.md 已附加 VF230 節（{len(L)} 行）；Part 1 之節未動")


if __name__ == "__main__":
    main()
