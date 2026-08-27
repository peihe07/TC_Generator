#!/usr/bin/env python3
"""Popup pilot 批（下放包 02 §六-5）—— 全量一批。

**R-G3**：全程不呼叫 `openpyxl` 之 `save()`；工作簿以
`backend/xlsx_surgical.surgical_save` 之 zip 層外科寫入。
母本 R10:R1411 之設計方法下拉為 **x14 擴充**，openpyxl 讀不到，
`save()` 會靜默刪除它（A-POP5）——故本路徑不是偏好，是唯一合法路徑。

**R-G25**：輸出落 `features/popup/sandbox/<tag>/`。

值一律逐字取自 `forms/Pop Up List HMI R1 (26PI).xlsx`（R-POP6），
引用時併記 PU id 與欄名（profile §2）。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[3]
FEAT = ROOT / "features/popup"
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import surgical_save  # noqa: E402

SPEC = "SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)"
GROUP, TEST_SET = "Popup", "Pop-up Close"
DESIGN_METHOD = "狀態轉換 (State Transition Testing)"

# 每條 TC 之 PU 引用 —— `pu` 欄之值於落檔前逐格對 Pop Up List 原檔複驗
# （verify_pu_quotes()），不符即停：靜態轉錄與其來源分家是 G-F 之標的。
TCS = [
    {
        "req_id": "SWE1-POP-002-01",
        "pu": {"id": "PU0942",
               "Timeout (sec)": "5",
               "String/Popup Message": "<X>\nPage added! [Reorder]",
               "Module": "Home Screen"},
        # 上半 = 037 E 欄 verbatim；下半 = 作者生成之情境標籤（IN §4.3.1）
        "test_item": [
            "Pop-ups can be closed after time-out "
            "(timeout is defined in Pop-up List document)",
            "(Time-out closure of PU0942, 5 s)",
        ],
        "pre_conditions": [
            "The vehicle is stationary with the ignition in RUN",
            "The Home Screen is displayed",
        ],
        "input_test_data":
            "Time-out = 5 s, as defined by PU0942 Timeout (sec)",
        "steps": [
            "Enter the Home Screen page-management view and add a home screen page",
            "Leave the screen and all buttons untouched for 10 seconds after the "
            "pop-up appears",
            "Read the pop-up display status and the elapsed time at the moment the "
            "pop-up disappears",
        ],
        "expected": [
            "The pop-up is displayed showing `<X>` and `Page added! [Reorder]`, "
            "as defined by PU0942 String/Popup Message",
            "No user interaction is registered during the 10-second window",
            "The pop-up closes by itself 5 seconds after it appeared, matching the "
            "Time-out defined by PU0942 Timeout (sec), and the Home Screen is shown "
            "without the pop-up",
        ],
        "spec_sections": ["5.6"],
        "reasoning":
            "驗證目標單一：GP4 第 1 途徑（time-out 自動關閉）。"
            "PU 之選定理由 —— (a) 類 240 列中取 PU0942：Timeout (sec) 為純數值 `5`"
            "（非 `5 seconds` 之帶單位寫法，量測不需再解析），觸發路徑純屬 HMI"
            "（新增 home screen 頁），台架上不需車輛運動、外接裝置或雲端連線即可重現。"
            "步驟 2 之觀察窗設為 10 秒（2× 標稱值）而非剛好 5 秒 —— 只看到 5 秒時仍在，"
            "分不出「還沒關」與「不會關」。timeout 值不落 PENDING：DR-POP1 已由 "
            "R-POP6 結案，值有來源可引。",
    },
    {
        "req_id": "SWE1-POP-002-02",
        "pu": {"id": "PU0215",
               "Exit Conditions": "<Trks>",
               "String/Popup Message": "Tracks List",
               "Description": "Display when user is in Media screen and presses Track list button",
               "Module": "Media"},
        "test_item": [
            "Pop-ups can be closed after pressing button that opened pop-up again "
            "(eg. Tracks popups)",
            "(Second press of the opening control `<Trks>`, PU0215)",
        ],
        "pre_conditions": [
            "The vehicle is stationary with the ignition in RUN",
            "A media source containing at least one track list is available",
            "The Media screen is displayed",
        ],
        "input_test_data": "NA",
        "steps": [
            "On the Media screen, press the Track list button `<Trks>`",
            "Press `<Trks>` a second time while the pop-up is displayed",
            "Read the pop-up display status immediately after the second press",
        ],
        "expected": [
            "The `Tracks List` pop-up is displayed, as defined by "
            "PU0215 String/Popup Message",
            "The second press lands on the same `<Trks>` button that opened the pop-up",
            "The pop-up is closed and the Media screen is shown without the pop-up",
        ],
        "spec_sections": ["5.5", "5.6"],
        "reasoning":
            "驗證目標單一：GP4 第 2 途徑（再按開啟鍵關閉）。"
            "spec_reference 併列 `_5.5`＋`_5.6`（R-POP8）—— 5.5（GP3）與 5.6 第 2 途徑"
            "為同一行為之兩處敘述，037 K8 逐字 `Duplicated feature of SWE1-POP-002-02`。"
            "PU0215 為全表唯一 Exit Conditions 即開啟鍵本身者（`<Trks>`），"
            "且 037 E 欄自舉 `eg. Tracks popups`，來源與例證對得上。"
            "input_test_data = `NA`：`<Trks>` 屬互動資料，依 IN §4.5 歸 Procedure，"
            "不重複列於本欄。"
            "**device 軸未拆，理由如下**：037 S11 逐字 "
            "`a physical hard button or a specific UI button on the screen` 是真軸"
            "（IN §8.3），但 Pop Up List 全表僅 PU0215 之開啟鍵為 UI 按鍵可用；"
            "hard-button 分支之最近候選 PU0229 之 Exit Conditions 雖為 "
            "`Press of VR button again`，其 Description 為 "
            "`Displayed when the user asks to call for a number` —— 開啟者是語音請求"
            "而非該按鍵，把它指派給 hard-button 分支是來源沒有承載的推定（IN §8.4.1）。"
            "拆成兩條會有一條無實例可填。登 A-POP7，待補件或 RD-1 回覆後再拆。",
    },
    {
        "req_id": "SWE1-POP-002-03",
        "pu": {"id": "PU0580",
               "Exit Conditions": "Timeout, Touch outside of popup, X",
               "Timeout (sec)": "5 seconds",
               "String/Popup Message": '"Welcome [username]", "X"',
               "Module": "Personal Account/Driver Profiles"},
        "test_item": [
            "Pop-ups can be closed when touching screen outside of pop-up",
            "(Touch outside the pop-up bounds, PU0580)",
        ],
        "pre_conditions": [
            "The vehicle is stationary with the ignition in RUN",
            "At least two driver Profiles exist on the head unit",
            "The All Profiles tab is reachable from the current screen",
        ],
        "input_test_data":
            "Time-out = 5 s, as defined by PU0580 Timeout (sec)",
        "steps": [
            "Open the All Profiles tab and switch manually to another Profile",
            "Within 5 seconds of the pop-up appearing, tap an area of the screen "
            "outside the pop-up window frame",
            "Read the pop-up display status immediately after the tap",
        ],
        "expected": [
            'The pop-up is displayed showing `"Welcome [username]", "X"`, '
            "as defined by PU0580 String/Popup Message",
            "The tap lands outside the pop-up window frame and activates no "
            "pop-up control",
            "The pop-up is closed, and the closure occurs before the 5-second "
            "Time-out defined by PU0580 Timeout (sec) elapses",
        ],
        "spec_sections": ["5.6"],
        "reasoning":
            "驗證目標單一：GP4 第 3 途徑（點 popup 外關閉）。"
            "037 K12 自陳該機制 `default to disable, requester should call the API "
            "to enable`，故受測 popup 必須是**明載已啟用**者 —— (b) 類 102 列即以 "
            "`Exit Conditions` 含 `outside` 為判準，PU0580 在列。"
            "選它而非其他 101 列：其 Exit Conditions 僅 `Timeout, Touch outside of "
            "popup, X` 三項，無雲端往返、無 keyboard，台架以切換 Profile 即可重現。"
            "步驟 2 之「5 秒內」與 ER 3 之「早於 time-out」為必要設計 —— "
            "PU0580 同時具 time-out，不設時窗則觀察到的關閉分不出是哪一條途徑造成。",
    },
    {
        "req_id": "SWE1-POP-002-04",
        "pu": {"id": "PU0949",
               "Exit Conditions": "<OK>\n<X>",
               "Timeout (sec)": "3",
               "String/Popup Message": "No Phone is Connected.        <OK>    <X>",
               "Description": 'This popup will be displayed if user presses the grayed out "Make a Call" button on Shortcuts when there is no connected phone.',
               "Module": "Home Screen"},
        "test_item": [
            "Pop-ups can be closed after making a selection inside the pop-up "
            "if applicable",
            "(Selection `<OK>` inside the pop-up, PU0949)",
        ],
        "pre_conditions": [
            "The vehicle is stationary with the ignition in RUN",
            "No mobile phone is paired with the head unit",
            "The Home Screen Shortcuts view is displayed",
        ],
        "input_test_data":
            "Time-out = 3 s, as defined by PU0949 Timeout (sec)",
        "steps": [
            'On the Home Screen Shortcuts view, press the grayed out "Make a Call" '
            "button",
            "Within 3 seconds of the pop-up appearing, press `<OK>` inside the pop-up",
            "Read the pop-up display status immediately after the press",
        ],
        "expected": [
            "The pop-up is displayed showing "
            "`No Phone is Connected.        <OK>    <X>`, as defined by "
            "PU0949 String/Popup Message",
            "The `<OK>` press is registered while the pop-up is still displayed",
            "The pop-up is closed, and the closure occurs before the 3-second "
            "Time-out defined by PU0949 Timeout (sec) elapses",
        ],
        "spec_sections": ["5.6"],
        "reasoning":
            "驗證目標單一：GP4 第 4 途徑（選擇後關閉）。"
            "受測對象取 `<OK>` 而非 `<X>`：037 S11 之 VC 逐字舉例 "
            "`tap an option or press a \"Confirm\"/\"Cancel\" button inside the pop-up`，"
            "`<X>` 是關閉鍵不是選項，測 `<X>` 測不到本 leaf 的命題。"
            "PU0949 之 Exit Conditions 逐字含 `<OK>` 與 `<X>` 兩者，故「選 `<OK>` 會關」"
            "有來源明載，非推定。時窗設計同 -002-03：PU0949 之 time-out 為 3 秒，"
            "不設時窗則關閉原因不可辨。",
    },
]

# -002-05 —— **不生成**。下放包 02 §六-5／§八：search keyboard 於 Pop Up List
# 查無對應列即停下回報，不改用他例。實測見上繳包 02 §五。


def cell(row, i):
    return "" if i >= len(row) or row[i] is None else str(row[i]).strip()


def verify_pu_quotes(src: Path) -> list[str]:
    """每一個 PU 引文對原檔逐格複驗（G-F）。不符即回報，由呼叫端停。"""
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    rows = list(wb["Main"].iter_rows(values_only=True))
    wb.close()
    header = [str(v).replace("\n", " ").strip() if v else "" for v in rows[1]]
    index = {h: i for i, h in enumerate(header)}
    by_id = {cell(r, 0): r for r in rows[2:] if re.match(r"^PU\d", cell(r, 0))}

    bad = []
    for tc in TCS:
        pu = tc["pu"]
        row = by_id.get(pu["id"])
        if row is None:
            bad.append(f"{pu['id']}：Main 查無此 id")
            continue
        for field, quoted in pu.items():
            if field == "id":
                continue
            i = index.get(field)
            if i is None:
                bad.append(f"{pu['id']}：Main 無欄 {field!r}")
                continue
            actual = cell(row, i)
            if actual != quoted:
                bad.append(f"{pu['id']} {field}：引文 {quoted!r} ≠ 原檔 {actual!r}")
    return bad


def render(tc: dict, n: int, cfg: dict) -> dict:
    return {
        "tc_id": cfg["tc_id_format"].format(n=n),
        "req_id": tc["req_id"],
        "test_group": GROUP,
        "test_set": TEST_SET,
        "test_item": "\n".join(tc["test_item"]),
        "pre_conditions": "\n".join(f"{i}. {s}" for i, s
                                    in enumerate(tc["pre_conditions"], 1)),
        "input_test_data": tc["input_test_data"],
        "test_procedure": "\n".join(f"{i}. {s}" for i, s
                                    in enumerate(tc["steps"], 1)),
        "expected_result": "\n".join(f"{i}. {s}" for i, s
                                     in enumerate(tc["expected"], 1)),
        "spec_reference": "\n".join(f"{SPEC}_{s}" for s in tc["spec_sections"]),
        "tc_ref_id": cfg["write_back"]["tc_ref_id_value"],
        "priority": "P1",
        "design_method": DESIGN_METHOD,
        "functional_safety": "NA",
        "author": cfg["write_back"]["author_value"],
        "pu_citation": tc["pu"],
        "reasoning": tc["reasoning"],
    }


def main() -> int:
    cfg = yaml.safe_load((FEAT / "feature.yaml").read_text(encoding="utf-8"))
    src_list = sorted(FEAT.glob(cfg["paths"]["popup_list"]))
    if len(src_list) != 1:
        sys.exit(f"paths.popup_list 命中 {len(src_list)} 檔")
    bad = verify_pu_quotes(src_list[0])
    if bad:
        print("FAIL（G-F：引文與原檔不符，停）", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 2
    print(f"PU 引文複驗：{sum(len(t['pu']) - 1 for t in TCS)} 格全數相符")

    tcs = [render(tc, i, cfg) for i, tc in enumerate(TCS, 1)]
    out = FEAT / "generated/pilot_01.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(tcs, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    print(f"寫入 {out.relative_to(ROOT)}：{len(tcs)} 條")

    # --- 工作簿 ---------------------------------------------------------
    wb_src = sorted(FEAT.glob(cfg["paths"]["workbook"]))[0]
    col = cfg["workbook"]["columns"]
    sheet = cfg["workbook"]["sheet"]
    first = cfg["workbook"]["first_data_row"]

    wb = openpyxl.load_workbook(wb_src)          # **不 save()**（R-G3）
    ws = wb[sheet]
    def idx(letter):
        n = 0
        for ch in letter:
            n = n * 26 + (ord(ch) - 64)
        return n
    for k, tc in enumerate(tcs):
        r = first + k
        ws.cell(r, idx("F")).value = tc["tc_id"]
        for key in ("req_id", "test_group", "test_set", "test_item",
                    "pre_conditions", "input_test_data", "test_procedure",
                    "expected_result", "spec_reference", "tc_ref_id",
                    "priority", "design_method", "functional_safety", "author"):
            ws.cell(r, idx(col[key])).value = tc[key]

    dst = FEAT / "sandbox/pilot01" / wb_src.name
    report = surgical_save(wb, wb_src, dst)
    print(f"工作簿 → {dst.relative_to(ROOT)}")
    print("  patched:", report["sheets_patched"])
    for k, v in report.items():
        if k not in ("sheets_patched", "members_patched"):
            print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
