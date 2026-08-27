#!/usr/bin/env python3
"""第 6／7 批之生成（下放包 34 §3.3 ＋ 35 §2.3，T175／T179）。

**`065-02` 於下放包 35 §二解除留置** —— 裁為 profile §9.3.1 之
**佔位剝除取材通則**（非第四處置類）：`(image:)` 佔位不屬句子文字，
任何層次之取材其標的止於佔位之前。`066` 為先例（其佔位在句號後，
切分自然分離）；本條使二者同一處置。

原留置之理由（下放包 34 §3，保留為紀錄） —— 勘查命中停止條件 (b)：
SYS1 §14.1 之句子切分把 `(image: image18.png)` 黏在 s2 之尾
（其前無 `. ` 可切），故 CONT 之**層次 1（整段 s1-2）與層次 2（單句 s2）
之標的皆夾帶圖佔位** —— 三處置類皆不合（profile §9.2）。
詳見上繳包 34 §3。

第 6 批遂為 a 段 1 筆（`065-01`）＋ b 段 1 筆（`065-02`，留置）；
第 7 批 1 筆（`066`），無停止條件命中。
"""
import csv
import json
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
import cont_guard as _cg                                   # noqa: E402

# CONT 之上半取自 SYS1 指定句（第 16 項逐字比對之標的）
CONT_UPPER = {"SWE1-HMI-VC-065-02": ("14.1", "2")}
A03 = ROOT / ("inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1"
              " STLA 報告.xlsx")
FUNC = "功能測試 (Functional based ; no specific technique)"
NEG = "負向測試 (Negative / Invalid)"
TAB_C = 'Open the Vehicle Category screen and select the "Controls" tab'
TAB_C_ER = 'The Vehicle Category screen is displayed with the "Controls" tab active'

BATCHES = [
 dict(name="batch6_brake_service", test_set="Brake Service",
      scope=["SWE1-HMI-VC-065-01", "SWE1-HMI-VC-065-02"], held=[],
      note="**本批無 b 段**（`065-02` 於下放包 35 §二解除留置）。"
           "其原留置之理由為 CONT 之二層次標的皆夾帶 `(image: image18.png)`；"
           "裁定為 profile §9.3.1 之佔位剝除取材通則，非第四處置類。",
      reasoning="**驗證目標**：EPB Service mode 於行進中之灰化（`-01`）"
                "與按下該灰化列之後果（`-02`）。"
                "**`065-02` 之取材**：profile §9.3.1 之佔位剝除通則，"
                "CONT 層次 2（`resolved-by-structure`）。"
                "**未涵蓋**：§14.2（EPB 彈窗優先序）與 §15（EPB 彈窗）"
                "為 037 未涵蓋之待補節（表 B 第 14／15 列，待 DR-VC3）——"
                "**其內容不得預納**（§8.4.2）。",
      tcs=[dict(leaf="SWE1-HMI-VC-065-01", dm=FUNC,
           title="Service mode greys out while the vehicle moves",
           low="In-motion lockout -- the Service mode option is rendered grey",
           pc=["The vehicle under test is equipped with the EPB Service mode option"],
           data="NA",
           pr=[TAB_C,
               "Open the Brake Service screen while the vehicle is stationary "
               "and record how the Service mode option is rendered",
               "Set the vehicle in motion and record how the Service mode "
               "option is rendered"],
           er=[TAB_C_ER,
               "The Service mode option is rendered as normal while stationary",
               "The Service mode option is rendered grey while the vehicle is "
               "in motion"],
           axis="行進中之呈現：灰化（對 -02 之按下後果，留置）",
           why="**驗證目標**：車輛行進中，EPB Service mode 選項呈灰。"
               "**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）——"
               "`Service mode option will be greyed out if the vehicle is in "
               "motion.`，**非 CONT**（其為完整可讀句，無指涉）。"
               "**ER 之 baseline（§5.6）**：「行進中呈灰」須有靜止時之呈現可比 ——"
               "否則「一直都是灰的」與「因行進而變灰」不可分。"
               "**P0 之依據**：行進中之攔阻屬 safety 型（同 `062-01`／`063-01`）。"
               "**與 `065-02` 之分工（IN §8.2.1）**：本筆驗**呈現**（灰化），"
               "`-02` 驗**按下之後果**（彈窗）—— 二個不同驗證點。"
               "**未涵蓋**：§14.2 之彈窗優先序（037 未涵蓋，表 B 第 14 列）。"),
       dict(leaf="SWE1-HMI-VC-065-02", dm=NEG,
           title="Pressing the greyed Service mode line is refused",
           low="In-motion lockout -- the press on the greyed line is answered with the pop-up",
           pc=["The vehicle is in motion and the greyed out line for EPB "
               "Service mode is displayed"],
           data="NA",
           pr=["Press the greyed out line for EPB Service mode",
               "Record whether the Service mode screen is entered, and record "
               "the pop-up that is displayed and its text"],
           er=["The press on the greyed out line is registered",
               "The Service mode screen is not entered and a pop-up is "
               "displayed whose text is PENDING: DR-VC10 PU0091 popup string"],
           axis="行進中之按下後果：彈窗（對 -01 之呈現）",
           why="**驗證目標**：按下行進中呈灰之 EPB Service mode 列，"
               "操作被攔阻並顯示彈窗。"
               "**⚠ 取材為 CONT 層次 2 ＋ profile §9.3.1 之佔位剝除**："
               "037 之 `the greyed out line` 為**定冠詞回指**（其先行詞"
               "「灰化之 Service mode 列」在 `065-01`），"
               "第一層特徵不命中（profile §9.4.1 第三型之已登記偽陰性）。"
               "SYS1 §14.1 之切分把 `(image: image18.png)` 黏在 s2 句尾，"
               "**層次 1（整段 s1-2，39 token 未逾 50）與層次 2（單句 s2）"
               "之標的原皆夾帶該佔位** —— 下放包 35 §二裁為佔位剝除通則，"
               "上半止於佔位之前。CONT 登記 `resolution=PC`／"
               "`resolution_key=greyed out line`，第三檢查點驗其 PC 確含該詞。"
               "**⚠ R-VC20 之四項揭露（爭議值之 verbatim）**："
               "**(一) 二源逐字** —— SYS1 §14.1 與 037 作 "
               "`‘Feature not available while vehicle is in motion’`；"
               "`Pop Up List HMI R1 (26PI)` 第 93 列 `PU0091` 之 "
               "`String/Popup Message` 作 "
               "`Function not available while vehicle is in motion.`（含句末句點），"
               "`HMI Settings List` 第 150 列亦作 `Function`。"
               "**(二) 分歧點** —— `Feature` vs `Function`，及句末句點之有無。"
               "**(三) 取 SYS1 為 verbatim 上半之理由** —— R-S4 要**規格原句**，"
               "非採信其值；換取彈窗清單之值只是換一個爭議值（R-VC20(a)）。"
               "**(四) 阻斷之 DR** —— **DR-VC10(一)**，A-VC18。"
               "**依 R-VC20(c)，爭議值不入 ER 之判準位** —— "
               "ER 驗「未進入 ＋ 彈窗出現」，其文字判準以 "
               "`PENDING: DR-VC10 PU0091 popup string` 承載"
               "（位置在 ER：缺件影響「怎麼判」，profile §7.2.1）。"
               "**不需 baseline** —— 攔的是動作後果（是否進入、彈窗是否出現），"
               "非值比對（同 `062-01`／`063-01` 型）。"
               "**與 `065-01` 之分工（IN §8.2.1）**：`-01` 驗**呈現**（灰化），"
               "本筆驗**按下之後果**（攔阻＋彈窗）—— 二個不同驗證點。"
               "**未涵蓋**：§14.2 之彈窗優先序（037 未涵蓋，表 B 第 14 列）。")]),
 dict(name="batch7_cabrio_widget", test_set="Cabrio Widget",
      scope=["SWE1-HMI-VC-066"], held=[],
      note="**本批無 b 段**，1 leaf → 1 TC。勘查五項停止條件皆未命中。",
      reasoning="**驗證目標**：本 feature 之 widget 標題為 `Cabrio`。"
                "**為什麼只有 1 筆**：framework §2 之 #8 `Cabrio Widget` 現為 "
                "1 leaf（§16.2）。"
                "**未涵蓋**：§16.2.1／§16.2.2（widget 所開啟之 Cabrio 車頂與"
                "擋風板操作）為 037 未涵蓋之待補節（表 B 第 16／17 列，"
                "待 DR-VC3）——**其內容不得預納**（§8.4.2）。",
      tcs=[dict(leaf="SWE1-HMI-VC-066", dm=FUNC,
           title="Cabrio widget carries its title",
           low="Widget title -- the literal string shown as this feature's widget title",
           pc=["The vehicle under test is equipped with the Cabrio feature",
               "The widget for this feature is placed where widgets are displayed"],
           data="NA",
           pr=["Display the screen that holds this feature's widget",
               "Record the title text shown on that widget"],
           er=["The widget for this feature is displayed",
               'The widget title reads "Cabrio"'],
           axis="widget 之標題文字（本組唯一 leaf）",
           why="**驗證目標**：該 widget 之標題文字為 `Cabrio`。"
               "**取材（R-VC25）**：上半取自 037 `Description` 之**首句**"
               "`W0.) Widget title for this feature is Cabrio.` ——"
               "其後之 `(image: image23.png)` 為圖佔位，**不入上半**"
               "（上半仍為 Description 之逐字子串，第 7b 項通過）。"
               "**非 CONT** —— 該句完整可讀，無指涉。"
               "**⚠ 委派之兩態（下放包 34 §3.3）**：widget 所開啟之 Cabrio "
               "功能（車頂開闔、擋風板）屬**章 8／9**，037 未涵蓋，"
               "見表 B 第 1–7 列。"
               "**若 DR-VC3 回覆「應補」，章 8／9 另立 `Cabrio Rooftop` 組"
               "（R-VC16(c)），本委派之標的即改指該組** ——"
               "二態預先寫明，回覆後只需確認，不需改寫本欄。"
               "**範圍（§8.4.2）**：本筆只驗標題文字，"
               "不驗 widget 之開啟行為、不驗其所開啟之功能。")]),
]


def main():
    global _sys1
    _sys1 = _cg.load_sys1()
    src = {}
    for r in list(openpyxl.load_workbook(A03, read_only=True, data_only=True)
                  ["Analysis Report"].iter_rows(values_only=True))[7:]:
        if r[0] not in (None, ""):
            src[str(r[0]).strip()] = (str(r[3]).strip(), str(r[4]).strip())
    recon = {r["req_id"]: r for r in csv.DictReader(
        (ROOT / "data/recon_leaf_to_section.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    prio = {r["req_id"]: r["final_p"] for r in csv.DictReader(
        (ROOT / "data/priority_final.tsv").open(encoding="utf-8"),
        delimiter="\t")}

    for b in BATCHES:
        tcs = []
        for sp in b["tcs"]:
            leaf = sp["leaf"]
            desc = src[leaf][1]
            # 上半自來源取值。`065-02` 為 CONT，其上半須為 SYS1 之指定句
            # （第 16 項逐字比對）；餘者取 037 Description 之首句
            # （其後若為圖佔位，依 profile §9.3.1 不入上半）。
            if leaf in CONT_UPPER:
                sec, idx = CONT_UPPER[leaf]
                upper = _cg.sentence(_sys1[sec], idx)
            else:
                upper = _cg.strip_image_tail(desc.split("\n")[0].strip())
            tcs.append({
                "leaf_id": leaf, "test_group": "Vehicle Category",
                "test_set": b["test_set"], "tc_title": sp["title"],
                "test_item": f"{upper}\n\n({sp['low']})",
                "pre_conditions": "\n".join(f"{i}. {x}" for i, x
                                            in enumerate(sp["pc"], 1)),
                "input_test_data": sp["data"],
                "test_procedure": "\n".join(f"{i}. {x}" for i, x
                                            in enumerate(sp["pr"], 1)),
                "expected_result": "\n".join(f"{i}. {x}" for i, x
                                             in enumerate(sp["er"], 1)),
                "specification_reference": recon[leaf]["spec_reference"],
                "design_method": sp["dm"], "priority": prio[leaf],
                "split_flag": False, "split_reason": "",
                "functional_safety": "NA",
                "reasoning": sp["why"], "distinguishing_axis": sp["axis"],
            })
        doc = {"batch": b["name"], "feature": "vehicle_category",
               "test_group": "Vehicle Category", "test_set": b["test_set"],
               "handoff": "docs/handoff/34_tail_batches.md",
               "ruling": "R-VC22／R-VC25／R-VC26／R-VC30",
               "segment": "a" if b["held"] else "a（無 b 段）",
               "segment_note": b["note"],
               "split_delta": 0, "tc_id_status": "provisional",
               "leaf_scope": b["scope"], "held_leaves": b["held"],
               "pending_scope": [],
               "write_back": "凍結 —— 本輪只產出 JSON，不寫回工作簿",
               "reasoning": b["reasoning"], "tcs": tcs}
        p = ROOT / "generated" / f"{b['name']}.json"
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
                     "utf-8")
        print(f"{p.relative_to(ROOT)} —— {len(tcs)} TC / "
              f"{len(b['scope'])} leaf / held {len(b['held'])}")


if __name__ == "__main__":
    main()
