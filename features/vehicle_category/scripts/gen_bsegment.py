#!/usr/bin/env python3
"""b 段三筆之生成，併回原批（下放包 34 §二，T174）。

R-VC30（Pei 2026-08-27 裁定 (a)）：`007-01`／`013-04`／`025-01`
**裁為需求 leaf，維持於 117 母體，生成 TC**。

R-VC22(d)：補生成**併入原批** —— `007-01`／`013-04` → 第 1 批、
`025-01` → 第 3 批。故本檔**讀既有批檔、插入、寫回**，
既有各筆**逐字不動**（其為已收斂之產物）。

profile §8（短來源）：三筆之來源皆 < 60 字元，
**上半取來源之完整句**（非任意子串），且須人工複核。
  `007-01` 29 字元／`013-04` 22 字元／`025-01` 27 字元。

驗證定位（R-VC30，防與 sibling 重複，IN §8.2.1）：
  `007-01`／`025-01` —— **全集層**（表之全集相符、無表外多餘）；
                        `-02`~`-05` 為**逐列層**。
  `013-04` —— **殼 TC**，PDO graphics 不在素材（DR-VC9(一)）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"

FUNC = "功能測試 (Functional based ; no specific technique)"
TAB_C = 'Open the Vehicle Category screen and select the "Controls" tab'
TAB_C_ER = ('The Vehicle Category screen is displayed with the "Controls" '
            'tab active')

# 上半**自 037 取值**，不在此手抄（同 gen_batch4／5 之作法）——
# 手抄之逐字與來源之逐字是兩件事，第 7b 項只驗前者對得上後者。
SPEC = {
    "SWE1-HMI-VC-007-01": dict(
        batch="batch1_category_structure", after="SWE1-HMI-VC-007-05",
        title="Vehicle Tab set matches the mapping table as a whole",
        low="Whole-set layer -- the tab set as a whole against the mapping "
            "table, no table row missing and no tab outside it",
        pc=["The vehicle under test is equipped with the Specialty features "
            "listed in the mapping table"],
        data="The Vehicle Tab Labels and Order table of SYS1 section 2.4, "
             "whose rows are VC2.2.2 to VC2.2.11",
        pr=[TAB_C,
            "Record every Specialty tab that is present, with its name and its "
            "left-to-right position",
            "Compare the recorded set against the rows of the mapping table "
            "named in the test data"],
        er=[TAB_C_ER,
            "The recorded set is the baseline for the comparison in step 3",
            "Every table row whose Specialty feature the vehicle is equipped "
            "with has a tab present, and no tab is present that the table does "
            "not name"],
        axis="表之層次：全集（對 -02～-05 之逐列）",
        why="**驗證目標**：Vehicle Tab 之**全集**與 SYS1 §2.4 之對照表相符 ——"
            "表內該有的都在、表外不該有的都不在。"
            "**⚠ 本筆為 b 段，依 R-VC30（Pei 2026-08-27 裁定 (a)）生成** ——"
            "裁為需求 leaf，維持於 117 母體。"
            "**DR-VC9(二) 之查證維持發送**；若上游回覆與本裁定相反"
            "（確認為表頭誤登），依 `docs/RESUME_PLAN.md` §4.1 由 Pei 再裁。"
            "**⚠ 與 sibling 之層次分工（IN §8.2.1）**："
            "本筆為**全集層**（完整性與排他性）；`-02`~`-05` 為**逐列層**"
            "（各列之名稱與位置）。**二者為不同驗證點，不重複** ——"
            "逐列全對而少一列，逐列層不會 FAIL，本筆會。"
            "**取材（profile §8 短來源）**：037 `Description` 為 "
            "`Vehicle Tab Labels and Order.`，**29 字元** —— "
            "該長度下子串判準幾近無保護，故上半取其**完整句**，"
            "且依 profile §8 須人工複核。"
            "**測試資料之表為實測**：SYS1 §2.4 之 `VC2.2.x` 列實測為 "
            "**VC2.2.2–VC2.2.11 共 10 列**（無 VC2.2.1）。"),
    "SWE1-HMI-VC-013-04": dict(
        batch="batch1_category_structure", after="SWE1-HMI-VC-013-03",
        title="Portrait Dashboard layout follows the PDO graphics",
        low="Portrait Dashboard -- the layout as a whole against the PDO "
            "graphics reference",
        pc=["The vehicle is equipped with a portrait display",
            "The Dashboard tab holds features to display"],
        data="NA",
        pr=[TAB_C,
            "Select the Dashboard tab and record the layout as displayed",
            "Compare the recorded layout against PENDING: DR-VC9 PDO graphics"],
        er=[TAB_C_ER,
            "The Dashboard layout is displayed on the portrait display",
            "The recorded layout matches the PDO graphics reference"],
        axis="直向 Dashboard：版面整體對 PDO（對 -01～-03 之具體規則）",
        why="**驗證目標**：直向 Dashboard 之版面與 PDO graphics 相符。"
            "**⚠ 本筆為 R-VC30 所裁之殼 TC** —— PDO graphics **不在素材**"
            "（DR-VC9(一) 未結），故 Procedure 之比對標的以 "
            "`PENDING: DR-VC9 PDO graphics` 佔位（IN §8.4.3）。"
            "**其為三筆 b 段中唯一之殼** —— `007-01`／`025-01` 之表皆在 SYS1。"
            "**⚠ 與 sibling 之分工（IN §8.2.1）**：`013-01`~`-03` 驗**已載於"
            "規格之具體版面規則**（三則以下各一橫幅／四則以上之拆分／"
            "其餘以磚塊置於下方）；本筆驗**版面整體與 PDO 之相符**，"
            "即規格文字未載而委由圖說者。二者不重複。"
            "**Pre-Condition 之方向**：`DISPLAY_PORTRAIT`（profile §6 常數，"
            "逐字重用）—— 本 leaf 明載 `For portrait displays`。"
            "**取材（profile §8 短來源）**：037 `Description` 為 "
            "`Refer to PDO graphics.`，**22 字元**，上半取其完整句，須人工複核。"),
    "SWE1-HMI-VC-025-01": dict(
        batch="batch3_controls", after="SWE1-HMI-VC-025-05",
        title="Controls button set matches the button table as a whole",
        low="Whole-set layer -- the Controls button set as a whole against the "
            "button table, no table row missing and no button outside it",
        pc=["The vehicle under test is equipped with the Controls features "
            "listed in the button table"],
        data="The Controls Button Table of SYS1 section 3.9, whose rows are "
             "the 28 buttons from Rear Sunshade to Ambient Lighting",
        pr=[TAB_C,
            "Record every button that is present in the Controls tab",
            "Compare the recorded set against the rows of the button table "
            "named in the test data"],
        er=[TAB_C_ER,
            "The recorded set is the baseline for the comparison in step 3",
            "Every table row whose Controls feature the vehicle is equipped "
            "with has a button present, and no button is present that the "
            "table does not name"],
        axis="表之層次：全集（對 -02～-05 之逐列狀態語意）",
        why="**驗證目標**：Controls 按鈕之**全集**與 SYS1 §3.9 之 "
            "`Controls Button Table` 相符。"
            "**⚠ 本筆為 b 段，依 R-VC30 生成**（同 `007-01`，"
            "DR-VC9(二) 之查證維持發送）。"
            "**⚠ 與 sibling 之層次分工（IN §8.2.1）**："
            "本筆為**全集層**（成員之完整性與排他性）；"
            "`-02`~`-05` 為**逐列層**（各按鈕之**狀態語意**，"
            "如 `Activates Feature`／`Off, On (if unavailable – greyed out)`）。"
            "**二者為不同驗證點** —— 每個按鈕之狀態都對而少一個按鈕，"
            "逐列層不會 FAIL，本筆會。"
            "**取材（profile §8 短來源）**：037 `Description` 為 "
            "`C1.) Controls Button Table.`，**27 字元**，上半取其完整句，"
            "須人工複核。"
            "**測試資料之表為實測**：SYS1 §3.9 之按鈕列實測為 **28 列**，"
            "自 `Rear Sunshade` 至 `Ambient Lighting`。"
            "**⚠ 範圍（§8.4.2）**：本筆不驗各按鈕之狀態語意（屬 `-02`~`-05`），"
            "亦不驗表外項目於他處之行為。"),
}


def numbered(xs):
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def main():
    import openpyxl
    import csv
    a03 = ROOT / ("inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1"
                  " STLA 報告.xlsx")
    src = {}
    for r in list(openpyxl.load_workbook(a03, read_only=True, data_only=True)
                  ["Analysis Report"].iter_rows(values_only=True))[7:]:
        if r[0] not in (None, ""):
            src[str(r[0]).strip()] = (str(r[3]).strip(), str(r[4]).strip())
    recon = {r["req_id"]: r for r in csv.DictReader(
        (ROOT / "data/recon_leaf_to_section.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    prio = {r["req_id"]: r["final_p"] for r in csv.DictReader(
        (ROOT / "data/priority_final.tsv").open(encoding="utf-8"),
        delimiter="\t")}

    RE_P = re.compile(r'PENDING:\s*(DR-VC\d+)\s+([^\n"]*)')
    F = ("pre_conditions", "input_test_data", "test_procedure",
         "expected_result", "test_item", "tc_title")

    for batch in sorted({s["batch"] for s in SPEC.values()}):
        p = GEN / f"{batch}.json"
        d = json.loads(p.read_text("utf-8"))
        ts = {"batch1_category_structure": "Category Structure",
              "batch3_controls": "Controls"}[batch]
        for leaf, sp in SPEC.items():
            if sp["batch"] != batch:
                continue
            upper = src[leaf][1]                       # 037 Description，完整句
            tc = {
                "leaf_id": leaf,
                "test_group": "Vehicle Category",
                "test_set": ts,
                "tc_title": sp["title"],
                "test_item": f"{upper}\n\n({sp['low']})",
                "pre_conditions": numbered(sp["pc"]),
                "input_test_data": sp["data"],
                "test_procedure": numbered(sp["pr"]),
                "expected_result": numbered(sp["er"]),
                "specification_reference": recon[leaf]["spec_reference"],
                "design_method": FUNC,
                "priority": prio[leaf],
                "split_flag": False,
                "split_reason": "",
                "functional_safety": "NA",
                "reasoning": sp["why"],
                "distinguishing_axis": sp["axis"],
            }
            idx = next(i for i, x in enumerate(d["tcs"])
                       if x["leaf_id"] == sp["after"]) + 1
            d["tcs"].insert(idx, tc)
            if leaf not in d["leaf_scope"]:
                j = next((i for i, x in enumerate(d["leaf_scope"])
                          if x == sp["after"]), len(d["leaf_scope"]) - 1) + 1
                d["leaf_scope"].insert(j, leaf)
            d["held_leaves"] = [x for x in d.get("held_leaves", [])
                                if x != leaf]
        # b 段解除後之欄位更新
        d["segment"] = "a+b"
        d["segment_note"] = (
            "**b 段已併入**（R-VC30，Pei 2026-08-27 裁定 (a)；R-VC22(d) 補生成"
            "併入原批）。`held_leaves` 為空，母體即該 Test Set 之 leaf 全集。")
        d["pending_scope"] = [
            {"leaf": t["leaf_id"], "dr": m.group(1), "marker": m.group(2).strip()}
            for t in d["tcs"] for f in F for m in [RE_P.search(t[f])] if m]
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", "utf-8")
        print(f"{batch}: tcs={len(d['tcs'])} leaf_scope={len(d['leaf_scope'])} "
              f"held={d['held_leaves']} pending={len(d['pending_scope'])}")


if __name__ == "__main__":
    main()
