#!/usr/bin/env python3
"""Pilot 批之生成器（13 包作業 E）—— 16 leaf，各 1 條 TC。

## 本檔為 pilot 之單一來源

生成物落 `generated/<req_id>.json`，每檔一個 leaf，結構同 Comfort：
parent 層（`reasoning`／`keywords`／`must_carry_used`）＋ `tcs` 陣列。

## 遵循

- 欄位與形狀：canon §4.3（tc_title 2–14 字）、§4.4（pre-condition 只寫狀態）、
  §4.5（資料歸屬單一欄）、§5.1／§5.5（最終步須帶查核目標）、§5.7（一個目標）、
  §6（ER 與步驟對應）、§10.4（reasoning 繁中 2–5 句）、§12（design method 首匹配）
- `test_item` = §4.3 之 tc_title（**R-U6 明文**：BLANK 綁定 Test Item = 標準 tc_title）
- spec 內文一律取 `pdf_text`（R-U35 (a)），由 `build_batch_context.assemble()` 供給
- `specification_reference` 由 `spec_ref()` 產出；**逐條覆寫須具名理由**（見 `REF_EXTRA`）
- PLP 之 `3.1`–`3.5` 併列由 `PLP_LEAVES` 自動帶入（R-U46）

## 未做

- **不寫回工作簿**（R-U14）
- 不指派 TestRail 之 `tc_id_testrail`、不填 `author`／`test_vehicle` 等執行欄
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                      # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"

# 逐條之 specification_reference 增列（**須具名理由**，不得無故擴張）
# J-10（19 包）：每筆增 **`provides`** —— 該節提供給本 TC 之字面值。
# G17 會驗**該字面值確實出現在該 TC 之欄位內**；
# 登記一個不相干的節即轉紅。**「有登記」與「登記得對」是兩件事。**
REF_EXTRA = {
    # 9.3.2 之 "show the message specified above" 指 9.3.1 之 bonk 與訊息字串；
    # 該字串為本 TC 之 ER 內容，故其出處一併列入（§10.7）。
    "SWE1-HMI-PROF-091-01": [("9.3.1",
                              "Function not available while vehicle in Motion.")],
    # 作業 B 之發現（17 包）：8.4.1 只說「系統會儲存該 profile」，
    # **沒說它會出現在 Profile List 裡**。本 TC 之 ER5 以「列於 Profile List」
    # 作為「已儲存」之觀察點，而該行為出自 5.1.1
    # （"When on the All Profiles tab, all available users will be shown"）。
    # 依 F-1 之判準（驗證**或倚為 setup／觀察點**者須引用），補列 5.1.1。
    "SWE1-HMI-PROF-070": [("5.1.1", "Profile List")],
    # F-1（16 包）：**已移除 `11.5`。**
    # 併列之原理由為「該表印在 p17，而 p17 也掛 11.5」—— 那是**頁面共置**，
    # 不是章節歸屬（§10.7）。Table CPA2 屬 11.4（CPA2 為其引用者與所有者），
    # 本 TC 一句都沒驗到 11.5（CPA3 之刪除／更新／安裝範圍）。
    # must_carry 之 `p17 → ["11.4","11.5"]` 多節掛回**不動** —— 那管的是
    # context 注入，與追溯欄是兩個不同的問題。
    # D-3：PRACC7.2 之圖示與字串出自 5.1.2，本節（5.2）以註記號指之。
    "SWE1-HMI-PROF-021-01": [
        ("5.1.2", "This icon is associated to settings that are specific to "
                  "your profile and are not shared across the vehicle")],
}

# 037 之先驗 Priority 與 R-U5 之對映（**逐條具名，不機械換算**）
#   P0 僅給 R-U5 明列之核心主流程五類：
#     profile 建立、切換、偏好之儲存與回復、Valet Mode 進出、資料遺失風險項
#   其餘：邊界與分支 → P1／P2，依其對主功能之影響
PRIORITY = {
    "SWE1-HMI-PROF-001-01": ("P0", "偏好之儲存與回復 —— R-U5 核心五類之一"),
    # D-1：原判 P2（理由為「037 先驗 Low」）—— 以先驗覆蓋 rubric，方向與 R-U5 相反。
    # 「Restore Settings to Default」即回復原廠，屬 R-U5 明列之**資料遺失風險項**。
    "SWE1-HMI-PROF-002-03": ("P0", "回復原廠之分支 —— 資料遺失風險項"
                                   "（R-U5／canon §10.2）；037 先驗 Low 不覆蓋 rubric"),
    "SWE1-HMI-PROF-021-01": ("P1", "profile 建立之上限邊界 —— R-U5 定邊界為 P1"),
    "SWE1-HMI-PROF-032": ("P0", "偏好之自動儲存 —— R-U5 核心五類之一"),
    # D-1 連帶複核：原理由亦為「037 先驗」形態，改依 rubric 判
    "SWE1-HMI-PROF-048": ("P1", "建立新 profile 之次要性質（預設 profile 之存續）"
                                "—— 主要功能之次要操作"),
    "SWE1-HMI-PROF-053": ("P1", "setup flow 之非主路徑分支（無連網配置）"),
    "SWE1-HMI-PROF-059-01": ("P2", "welcome popup 之內容展示"),
    "SWE1-HMI-PROF-062-02": ("P2", "welcome popup 之逾時清除；輔助行為之邊界"),
    "SWE1-HMI-PROF-073-01": ("P1", "username 長度上限邊界 —— R-U5 定邊界為 P1"),
    "SWE1-HMI-PROF-070": ("P0", "profile 建立之儲存 —— R-U5 核心五類之一"),
    # K-1（21 包）：P1 → P0。本條之核心斷言為「進行中之受限工作**確實被中斷**」，
    # 即行車分心防線之成立本身（canon §10.2 safety）。
    # 對照：091-02（bonk 與訊息）為該防線之**回饋**，維持 P2。
    "SWE1-HMI-PROF-091-01": ("P0", "行車中之工作中斷 —— **防線成立本身**"
                                   "（§10.2 safety；D-UP16-01 附二）"),
    "SWE1-HMI-PROF-104": ("P2", "設定入口之導向；輔助功能"),
    "SWE1-HMI-PROF-111": ("P2", "說明頁之內容展示；037 先驗 Low"),
    "SWE1-HMI-PROF-112-01": ("P1", "app 刪除之範圍；037 先驗 High"),
    "SWE1-HMI-PROF-128-01": ("P0", "Valet Mode 進出 —— R-U5 核心五類之一"),
    "SWE1-HMI-PROF-132-02": ("P0", "Valet Mode 進出 —— R-U5 核心五類之一"),
}

FUNCTIONAL = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
BVA = "邊界值分析 (Boundary Value Analysis, BVA)"
SCENARIO = "情境 / 用例 (Scenario / Use Case Testing)"
NEGATIVE = "負向測試 (Negative / Invalid)"
FAULT = "基礎故障注入 (Fault Injection Lite)"

# ------------------------------------------------------------------ 內容


def steps(*lines) -> str:
    return "\n".join(f"{i}. {t}" for i, t in enumerate(lines, 1))


# 每個 leaf：tc_title／pre_conditions／input_test_data／procedure／ER／
# design_method／remarks／reasoning／keywords
TCS = {

    "SWE1-HMI-PROF-001-01": dict(
        title="Profile-linked preferences stored and recalled per Driver Profile",
        design=FUNCTIONAL,
        pre=steps(
            "Two Driver Profiles exist on the vehicle",
            "The features carrying the preferences under test are available "
            "for the vehicle and the region"),
        data="Preferences under test: Cluster Home screen (3.1), "
             "SiriusXM 360L Listener Profile (3.2), "
             "Nav Saved destinations (3.4)",
        proc=steps(
            "Activate Driver Profile A",
            "Set the three preferences listed in Input Test Data to values "
            "different from their current ones",
            "Record the values set in step 2",
            "Activate Driver Profile B, then activate Driver Profile A again",
            "Read the three preferences and check that they match the values "
            "recorded in step 3"),
        er=steps(
            "Driver Profile A is active",
            "The three preferences accept the new values",
            "The values set in step 2 are recorded",
            "Driver Profile A is active again",
            "The three preferences match the values recorded in step 3"),
        reasoning=(
            "驗證目標：4.1（PRACC1）要求系統對每個 Driver Profile 分別儲存並"
            "回復其 profile-linked preferences，本 TC 以「設值 → 切走 → 切回 → "
            "讀回」驗其儲存與回復。"
            "關鍵情境條件：受測之三項偏好取自 PLP 表 3.1／3.2／3.4 之逐字列項，"
            "非自擬（§8.4.1）；條文之「feature 不可用則忽略」以 pre-condition "
            "限定為該三項在本車與本區域可用。"
            "為什麼這樣切：037 對 4.1 切出三個 leaf，本 leaf（-01）之單位為"
            "「儲存與回復」，一葉一 TC（§8.2.1），未合併未拆分。"
            "刻意略過：-02（啟用時回復）與 -03（不可用之項目跳過）之行為由"
            "`SWE1-HMI-PROF-001-02`／`SWE1-HMI-PROF-001-03` 兩 leaf 承擔，本 TC 不代測。"),
        kw=["Driver Profile", "profile-linked preferences", "PLP table",
            "store", "recall"],
    ),

    "SWE1-HMI-PROF-002-03": dict(
        title="PU1088 displayed when default restoring is not confirmed",
        design=FAULT,
        pre=steps(
            "A Driver Profile is active",
            "The TBM confirmation path can be interrupted on the test bench"),
        data="Fault injected: the completion confirmation from HU or TBM is "
             "withheld",
        proc=steps(
            "Open the vehicle settings and select “Restore Settings to "
            "Default”",
            "Press “Yes” in PU_0118 to confirm the restore",
            "Withhold the completion confirmation from HU and TBM",
            "Read the popup shown on the head unit and check that PU1088 is "
            "displayed"),
        er=steps(
            "PU_0118 is displayed",
            "PU1087 is displayed",
            "The head unit does not receive the completion confirmation",
            "PU1088 is displayed"),
        remarks="PU1087／PU1088 之 popup 內文未載於 spec（DR #4）—— 本 TC 僅驗"
                "其是否顯示，不寫內文（R-U15／R-U27）",
        reasoning=(
            "驗證目標：4.1.1（PRACC1.2）之未確認分支 —— HU 或 TBM 未確認完成"
            "回復預設時顯示 PU1088，本 TC 以注入「不回覆確認」驗之。"
            "關鍵情境條件：須先走完 PU_0118 之 Yes 與 PU1087，故該兩者列為前段 ER；"
            "缺的只是確認訊號，屬可模擬之故障（§12 首匹配 → 基礎故障注入）。"
            "為什麼這樣切：037 對 4.1.1 切出之 -03 專指未確認之分支，"
            "成功回復之路徑屬 -01／-02，本 TC 不代測。"
            "刻意略過：**PU1088 之 popup 內文不寫**（R-U27）—— spec 給了觸發條件"
            "但未給內文，寫出來即造值（§8.4.1）；DR #4 待答。"),
        kw=["Restore Settings to Default", "PU1087", "PU1088", "TBM",
            "confirmation"],
    ),

    "SWE1-HMI-PROF-021-01": dict(
        title="Add New Profile removed at the five-Profile maximum",
        design=BVA,
        pre=steps(
            "Four Driver Profiles exist on the vehicle",
            "A Valet Mode Profile is present on the vehicle",
            # PRACC7.2 自陳「This logic is not applicable for 7” screens」——
            # 7 吋車上該圖示與字串本來就不存在，其「不存在」無從作為判準。
            "The vehicle does not have a 7-inch screen"),
        data="Driver Profile count: 4 (below the maximum) → "
             "5 (at the maximum)",
        proc=steps(
            "Open the Profile List and read the Add New Profile button",
            "Create one more Driver Profile so that five Driver Profiles exist",
            "Open the Profile List and check that the Add New Profile "
            "button is not present"),
        er=steps(
            "The Add New Profile button is present while four Driver Profiles "
            "exist",
            "The fifth Driver Profile is created",
            "The Add New Profile button is not present; the icon and the "
            "string “This icon is associated to settings that are "
            "specific to your profile and are not shared across the "
            "vehicle” are not present; and “Max Profiles reached. "
            "Delete to create a new one.” (PU0584) is displayed"),
        reasoning=(
            "驗證目標：5.2（PRACC8）之上限 —— 五個 Driver Profile 為邊界，"
            "達到時 Add New Profile 按鈕與 PRACC7.2 之圖示字串消失並改顯 PU0584。"
            "關鍵情境條件：以 4 個為基準線、第 5 個為邊界值，"
            "同一 TC 內取前後兩讀（§5.6），故 design method 為邊界值分析。"
            "**來源標示（J-4）**：ER1「未達上限時按鈕在」之權威為 "
            "**§5.6 之 BVA 界前基準線**，非條文 —— 5.2 只寫「達上限時不在」，"
            "未寫其反面。"
            "為什麼這樣切：Valet Mode Profile 不計入該五個之內，"
            "其存在列為 pre-condition 而非受測項，避免把兩個計數混為一談。"
            "刻意略過：刪除既有 profile 後按鈕是否回復，屬 5.2 之其他 leaf。"),
        kw=["Driver Profile", "maximum", "Add New Profile", "PU0584",
            "PRACC7.2"],
    ),

    "SWE1-HMI-PROF-032": dict(
        title="Preferences saved without pressing memory seat controls",
        design=FUNCTIONAL,
        pre=steps(
            "A Driver Profile is active",
            "The vehicle is equipped with memory seat hard and soft controls"),
        data="Preference under test: Memory Profiles (Seats, mirrors, "
             "steering wheel) (3.5)",
        proc=steps(
            "Activate Driver Profile A",
            "Adjust the seat, mirror and steering wheel positions",
            "Leave the memory seat set and save controls untouched",
            "Switch the ignition off and on",
            "Read the three positions and check that they match step 2"),
        er=steps(
            "Driver Profile A is active",
            "The seat, mirror and steering wheel positions are adjusted",
            "No memory seat set or save control is pressed",
            "The vehicle completes the ignition cycle",
            "The three positions match those set in step 2"),
        reasoning=(
            "驗證目標：5.9（PRACC15）—— 儲存 Driver Profile linked preferences "
            "不需按記憶座椅之 set／save 控制，且會自動存於車端。"
            "關鍵情境條件：其可驗形態為「不做那個動作也要存得住」，"
            "故以 ignition cycle 後讀回作為「已存於車端」之觀察點。"
            "**來源標示（J-4）**：ER4 之 ignition cycle **spec 從未提及**，"
            "其權威為 **R-U21**（Service B 群之設定→key cycle→讀回）。"
            "「已儲存」是狀態不是事件，觀察方式由裁決指定，不是條文給的。"
            "為什麼這樣切：本 leaf 只斷言儲存不依賴該控制，"
            "記憶座椅位置本身之回復屬 3.5 之 PLP 項目與其對應 leaf，不在此測。"),
        kw=["memory seat", "set", "save", "auto-save", "ignition cycle"],
    ),

    "SWE1-HMI-PROF-048": dict(
        title="Default Profiles remain after a new Profile is created",
        design=FUNCTIONAL,
        pre=steps(
            "The vehicle carries its default Profiles, including Driver 1",
            "No default Profile has been customized or deleted"),
        data="NA",
        proc=steps(
            "Open the Profile List and record the default Profiles present",
            "Create a new Driver Profile without customizing any default "
            "Profile",
            "Open the Profile List and check that the default Profiles "
            "recorded in step 1 are still present"),
        er=steps(
            "The default Profiles, including Driver 1, are recorded",
            "The new Driver Profile is created and no default Profile is "
            "customized",
            "The default Profiles recorded in step 1 are still present"),
        reasoning=(
            "驗證目標：6.2.1（NOPR1.1）之兩項斷言 —— 建新 profile 不需先客製化"
            "預設 profile，且 Driver 1 與其他預設 profile 會留在車上直到被客製化或刪除。"
            "關鍵情境條件：兩者為同一觸發（建立新 profile）之兩個結果，"
            "依 §5.7 併於一條 TC 之兩條 ER，不拆。"
            "為什麼這樣切：以步驟 1 之記錄作為基準線，步驟 3 比對其存續（§5.6）。"
            "**覆蓋缺口（A-UP13，23 包 M-2 掃出；25 包確認其歸屬）** ——"
            "**注意：R-U56 不適用於本項**。R-U56 關的是「SWE 未切 leaf」者，"
            "而本項之行為就寫在 `SWE1-HMI-PROF-048` **自己的 description 裡**"
            "（該 leaf SWE 有切、已取樣），只是本 TC 未驗其後半 ——"
            "**那是我方之覆蓋不足，不是範圍問題**。細節如下："
            "客製化或刪除後預設 profile 之消失，原稱「由 6.2 之其他 leaf 承擔」"
            "—— **該委派不成立**（6.2／NOPR1 只述 Welcome popup 與客製化提示）。"
            "該行為出自**本 leaf 自己之 description**（6.2.1 之 `will remain on "
            "the vehicle until a user customizes or deletes it`）之反面條件，"
            "而 **6.2.1 僅此一個 leaf**（`SWE1-HMI-PROF-048`）——"
            "**本 TC 只驗其前半（未客製化前仍在），後半無人驗**。"
            "**不可誤委派予 `SWE1-HMI-PROF-007-02`（4.5）**："
            "該 leaf 驗的是「客製化後刪除**全部** profile → Driver 1 **重建**」，"
            "與本處之「客製化後該預設 profile **不再是預設**」是兩件事。"
            "處置：於本 leaf 下補一條 TC（25 包 B 之附掛項）。"),
        kw=["default Profile", "Driver 1", "create", "customize"],
    ),

    "SWE1-HMI-PROF-053": dict(
        title="PU0585 shown on Get Started without vehicle connectivity",
        design=FUNCTIONAL,
        pre=steps(
            "The vehicle is not equipped with connectivity"),
        data="NA",
        proc=steps(
            "Open the Profile setup screen carrying the “Get Started” "
            "button",
            "Press “Get Started” and check that PU0585 is displayed "
            "and the Connected Account Login/Register screen is not displayed"),
        er=steps(
            "The “Get Started” button is displayed",
            "PU0585 is displayed and the Connected Account Login/Register "
            "screen is not displayed"),
        reasoning=(
            "驗證目標：6.4.1（NOPR3.1）—— 無連網配置之車輛按下 Get Started 時"
            "顯示 PU0585，且不顯示 Connected Account 之登入／註冊畫面。"
            "關鍵情境條件：車輛配置（無連網）為條件本身，故列 pre-condition；"
            "正反兩個觀察點（顯示 PU0585／不顯示登入畫面）為同一觸發之兩個結果，併為兩條 ER。"
            "為什麼這樣切：有連網之對應行為屬 6.4 之另一 leaf，"
            "本 TC 不代測，亦不自行擴充為配置對照組。"),
        kw=["connectivity", "Get Started", "PU0585", "Connected Account"],
    ),

    "SWE1-HMI-PROF-059-01": dict(
        title="Large welcome popup lists active and other Profiles",
        design=FUNCTIONAL,
        pre=steps(
            "Two Driver Profiles exist, each with a username, an avatar and a "
            "memory seat assignment",
            "Driver Profile A is the active Profile"),
        data="NA",
        proc=steps(
            "Activate Driver Profile A so that the large welcome popup is "
            "displayed",
            "Read the popup and check that the active and the other "
            "Profiles are listed"),
        er=steps(
            "The large welcome popup is displayed",
            "Driver Profile A’s username and avatar are displayed, and "
            "the other available Profile is displayed with its avatar, "
            "username and memory seat assignment"),
        reasoning=(
            "驗證目標：7.2.1（PRWEL2.1）之大型 welcome popup 內容 —— 現用 profile "
            "之 username 與 avatar，以及其他可用 profile 之 avatar、username 與"
            "記憶座椅指派。"
            "關鍵情境條件：記憶座椅指派為條件式（if applicable），"
            "故 pre-condition 明訂兩個 profile 皆有指派，使該欄位確實可觀察。"
            "為什麼這樣切：條文另有「More Options 進 Edit Profile tab」與"
            "「選了別的 profile 則顯示新的 welcome popup」兩項行為，"
            "屬不同觸發，依 §5.7 不併入本 TC。"
            "**委派更正二次（A-UP13；23 包 M-2 掃出，25 包定其歸屬）**："
            "兩項原稱「由 7.2 承擔」—— **該委派不成立**"
            "（7.2／PRWEL2 述的是**小型** welcome popup，其文無 `More Options`）。"
            "23 輪據此記為「兩項無人驗」，**該記載亦不準確** ——"
            "本節（7.2.1）之 leaf 有三：本 TC 為 `SWE1-HMI-PROF-059-01`，"
            "而兩項各有專屬 leaf：`SWE1-HMI-PROF-059-02`（More Options → "
            "Edit Profile tab）與 `SWE1-HMI-PROF-059-03`（切換 profile 後顯示"
            "新 welcome popup）承擔。"
            "**兩者尚未取樣**，故為 (b) 類之待兌現承諾，非覆蓋缺口。"),
        kw=["large welcome popup", "username", "avatar",
            "memory seat assignment"],
    ),

    "SWE1-HMI-PROF-062-02": dict(
        title="Welcome popup clears 30 seconds after display",
        design=BVA,
        pre=steps(
            "The vehicle is stationary",
            "A Driver Profile carrying a Welcome Popup is available"),
        data="Elapsed time readings: 29 s, 30 s",
        proc=steps(
            "Activate the Profile and start a timer",
            "Read the screen at 29 seconds without touching it",
            "Read the screen at 30 seconds and check that the Welcome Popup "
            "is cleared"),
        er=steps(
            "The Welcome Popup is displayed and the timer is started",
            "The Welcome Popup is still displayed at 29 seconds",
            "The Welcome Popup is cleared at 30 seconds"),
        reasoning=(
            "驗證目標：7.4（PRWEL4）之三個清除條件中之逾時條件 —— "
            "無其他動作時 Welcome Popup 於 30 秒後清除。"
            "關鍵情境條件：條文為「行車中／30 秒／使用者觸碰，三者先到者為準」，"
            "故 pre-condition 令車輛靜止、步驟 2 明訂不觸碰，"
            "把另外兩個條件排除，使 30 秒確為本次之生效條件。"
            "**來源標示（J-4）**：ER2「29 秒時仍在」之權威為 **§5.6 之 BVA "
            "界前基準線**，非條文 —— 7.4 只寫「30 秒後清除」，"
            "該句亦可讀為「不遲於 30 秒」，故界前之真值由方法要求而非條文明述。"
            "為什麼這樣切：29 秒與 30 秒兩讀構成邊界前後（§5.6），故取邊界值分析；"
            "行車中清除與觸碰清除屬 7.4 之其他 leaf，本 TC 不代測。"),
        kw=["Welcome Popup", "30 seconds", "clear", "stationary"],
    ),

    "SWE1-HMI-PROF-073-01": dict(
        title="Keyboard blocks input beyond 12 username characters",
        design=BVA,
        pre=steps(
            "The Profile setup flow is open at Step 2 “Enter a "
            "username”"),
        data="Username input: 11 characters → 12 characters → "
             "one further character",
        proc=steps(
            "Type 11 characters into the username field and read the field",
            "Type the 12th character and read the field",
            "Type one further character and check that the username field "
            "still shows 12 characters"),
        er=steps(
            "The username field shows the 11 characters typed",
            "The username field shows 12 characters",
            "The username field still shows 12 characters and the further "
            "character is not accepted"),
        remarks="spec 8.7 寫 “~12 characters”（約），037 leaf 寫 12 —— "
                "本 TC 取 12（較窄之解讀，且 037 為單位權威）",
        reasoning=(
            "驗證目標：8.7（NEWPR6）之 username 長度上限 —— 達上限後鍵盤不再接受輸入。"
            "關鍵情境條件：以 11／12／13 三讀構成邊界前後（§5.6），故取邊界值分析；"
            "spec 之「~12」為近似寫法，037 leaf 明寫 12，本 TC 取 12 並具名記於 remarks。"
            "為什麼這樣切：同節另有「最少 1 字元、未輸入前 Next 不可用」與"
            "「可含空白且空白計入長度」兩項，屬不同輸入條件，由 `SWE1-HMI-PROF-073-02`／`SWE1-HMI-PROF-073-03`（8.7）承擔。"),
        kw=["username", "12 characters", "keyboard", "maximum"],
    ),

    "SWE1-HMI-PROF-070": dict(
        title="Profile saved after username and avatar are entered",
        design=FUNCTIONAL,
        pre=steps(
            "The Profile setup flow is open at the username step"),
        data="NA",
        proc=steps(
            "Enter a username in the Profile setup flow",
            "Choose an avatar",
            "Switch the ignition off and on",
            "Open the Profile List",
            "Read the list and check that the Profile from steps 1 and 2 "
            "is listed"),
        er=steps(
            "The username is accepted",
            "The avatar is selected",
            "The vehicle completes the ignition cycle",
            "The Profile List is displayed",
            "The Profile carrying the username and avatar from steps 1 and 2 "
            "is listed"),
        reasoning=(
            "驗證目標：8.4.1（NEWPR3.1）—— 輸入 username 並選定 avatar 後系統儲存該 profile。"
            "關鍵情境條件：「已儲存」之可觀察形態取 ignition cycle 後仍列於 Profile List，"
            "不以畫面停留與否推定儲存。"
            "**來源標示（J-4）**：ER3 之 ignition cycle 其權威為 **R-U21**，spec 未提及；"
            "ER5 之「列於 Profile List」出自 **5.1.1**（8.4.1 只說系統會儲存），"
            "該節已於 17 輪補列於引用欄。"
            "為什麼這樣切：setup flow 之前後步驟（Get Started、記憶座椅指派等）"
            "屬 ch8 之其他 leaf，本 TC 只驗儲存這一件事。"),
        kw=["Profile setup", "username", "avatar", "save", "Profile List"],
    ),

    "SWE1-HMI-PROF-091-01": dict(
        title="Restricted Profile action interrupted when vehicle starts moving",
        design=STATE,
        # J-5（18 包）：**原本列了「R1 High」前提，本輪移除。**
        # 理由同 TC-023：該覆寫為列級（Table EDPR1 之 `Stellantis Account` 列），
        # 而本 TC 之 ER 不含帳號 label。
        pre=steps(
            "A Driver Profile is active and the Edit Profile tab is available",
            "The vehicle is stationary on a test track and can be brought "
            "into motion"),
        data="NA",
        proc=steps(
            "Open the Edit Profile tab and start editing the Profile username",
            "Bring the vehicle into motion",
            "Read the screen and check that the previous available page "
            "is displayed"),
        er=steps(
            "The username editing page is displayed",
            "The vehicle is in motion",
            "The previous available page is displayed, the bonk tone is "
            "played, and “Function not available while vehicle in "
            "Motion.” is displayed"),
        remarks="9.3.2 之變體覆寫為**列級**（PDF p14 之 Table EDPR1 該列），"
                "本 TC 不含帳號 label，故不設變體前提（J-5）",
        reasoning=(
            "驗證目標：9.3.2（EDPR3.2）—— 使用者正在進行受限項目時車輛轉為行進，"
            "系統須返回前一個可用頁面並播 bonk 與顯示訊息。"
            "關鍵情境條件：受測之受限項目取「編輯 username」一項即足以觸發，"
            "其判準為車輛由靜止轉入行進之狀態轉換（§12 首匹配 → 狀態轉換）。"
            "為什麼這樣切：訊息字串「Function not available while vehicle in Motion.」"
            "出自 9.3.1，條文以「the message specified above」指之，"
            "故 specification_reference 併列 9.3.1（§10.7），非自擬。"
            "刻意略過：9.3.1 之「行進中選取受限項目」為另一觸發（選取 vs 進行中），"
            "由 `SWE1-HMI-PROF-090`（9.3.1）承擔；本 TC 之字面值依 R-U35 (c) 用 Connected Account。"),
        kw=["vehicle in motion", "restricted items", "bonk", "Edit Profile",
            "Connected Account"],
    ),

    "SWE1-HMI-PROF-104": dict(
        title="More Settings opens My Profile without a back button",
        design=FUNCTIONAL,
        pre=steps(
            "A Driver Profile is active",
            "The Profile section is reachable from the vehicle menu"),
        data="NA",
        proc=steps(
            "Open the Profile section and press the vehicle “More "
            "Settings” button",
            "Read the page and check that the “My Profile” Settings "
            "section is displayed"),
        er=steps(
            "The “My Profile” Settings section is displayed",
            "No back button to the Profile section is present on the "
            "“My Profile” Settings section"),
        remarks="9.8 之 PU0609 句（設定變更時提示已對現用 profile 變更）"
                "在 037 無對應 leaf —— **依 R-U56 為 OUT-OF-SCOPE**"
                "（範圍上界為 037 之 180 leaf 母體）：不生成 TC、"
                "**不列覆蓋缺口、不向上游索取**。其為 xlsx 側掉句之事實仍留檔"
                "（補句表 must_carry；亦為 lint 之 PU 全集自檢案例）",
        reasoning=(
            "驗證目標：9.8（EDPR9）—— More Settings 直接連往 My Profile 設定區，"
            "且進入後不提供返回 Profile 區之返回鍵。"
            "關鍵情境條件：兩項為同一觸發之兩個結果，依 §5.7 併為一條 TC 之兩條 ER。"
            "為什麼這樣切：同節尚有一句「設定變更時以 popup 提示已對現用 profile 變更"
            "（PU0609）」—— 該句為 xlsx 側掉句（補句表 must_carry），"
            "其觸發為「變更設定」而非「按 More Settings」，屬不同觸發（§5.7），"
            "且 **037 未為其切出 leaf**。"
            "**依 R-U56（26 包，Pei 裁定）：SWE 有寫就有、沒寫就不理** ——"
            "該句為 OUT-OF-SCOPE，**不列缺口、不上報**；本 TC 不代測。"
            "（原述「該缺口具名上報」係 R-U56 之前之判讀，已改。）"),
        kw=["More Settings", "My Profile", "back button", "Settings section"],
    ),

    "SWE1-HMI-PROF-111": dict(
        title="Info icon opens the Local vs Connected Profile screen",
        design=FUNCTIONAL,
        pre=steps(
            "The vehicle is not an R1 High variant",
            # F-2：讀圖後更正 —— `****For China market only: do not show this
            # content` 之 `****` 標記掛在 **Connected Navigation 那一列**，
            # 不是整張表。仍列為 pre-condition 是為使「四列俱全」之預期成立，
            # **但其範圍是該列，不是該表**（見 remarks）。
            "The vehicle is not a China-market vehicle",
            "A Driver Profile is active and the Edit Profile tab is available"),
        data="NA",
        proc=steps(
            "Open the Edit Profile tab and read the Connected Account item",
            "Select the info icon and check that the Local vs Connected "
            "Profile screen is displayed"),
        er=steps(
            "An info icon is displayed next to Connected Account",
            "The screen titled “What are the benefits of creating an "
            "Connected account?” is displayed with two columns labeled "
            "Connected account and Local Profile, showing “Synchronize "
            "your profile between multiple vehicles. The cloud will remember "
            "your preferences” and “Create a profile specific to "
            "this vehicle. The vehicle will remember your preferences”, "
            "and the four rows of Table CPA2 with their column marks:\n"
            "   a. Personalization (Presets, Menu Bar Order, App Drawer "
            "Favorites, and more) — marked under **both** Connected Account "
            "and Local Profile\n"
            "   b. App Store Download — marked under Connected Account only\n"
            "   c. Marketplace (Access to Marketplace) — marked under "
            "Connected Account only\n"
            "   d. Connected Navigation (Personalized Favorites, Recents, "
            "and Predictive Navigation) — marked under Connected Account "
            "only"),
        remarks="標題之 “an Connected account” 為 spec 原文（含冠詞誤用），"
                "逐字照錄不修（§8.4.1）；spec 之示意圖仍寫舊名 "
                "“FCA account”，字面值以條文為準（§8.7.3）。"
                "中國市場之排除（****）掛在 Connected Navigation **該列**，"
                "非整張表 —— 本 TC 以 pre-condition 排除中國車，"
                "是為使四列俱全之預期成立",
        reasoning=(
            "驗證目標：11.4（CPA2）—— Edit Profile tab 之 Connected Account 旁"
            "資訊圖示開啟 Local vs Connected Profile 畫面，其標題、兩欄與各欄說明文字。"
            "關鍵情境條件：條文首句明載本註記不適用於 R1 High，"
            "另有星號註記載中國市場不顯示本內容，兩者皆列 pre-condition 之排除（§8.7.3）。"
            "為什麼這樣切：Table CPA2 之列項與其欄別**取自 PDF p17 之表格本體**"
            "（F-2 抽圖判讀，四列非五列 ——「Connected Profile App」是指向截圖之"
            "註解框，不是表列），ER 逐列載明其屬 Connected Account 或 Local Profile。"
            "刻意略過：**R1 High 無此資訊按鈕之反面情形未生成** —— "
            "pilot 之取樣單位為 16 leaf，加測即擴張範圍（§8.4.2），已具名上報。"),
        kw=["info icon", "Connected Account", "Local Profile", "Table CPA2"],
    ),

    "SWE1-HMI-PROF-112-01": dict(
        title="Deleted App Store app removed only for the uninstalling user",
        design=SCENARIO,
        pre=steps(
            "Two Driver Profiles exist on the vehicle, each with its own "
            "Connected Account",
            "The same App Store app is installed locally for both Profiles"),
        data="NA",
        proc=steps(
            "Activate Driver Profile A",
            "Record the App Store app shown in the app tray",
            "Delete the App Store app from Driver Profile A",
            "Activate Driver Profile B",
            "Open the app tray and check that the app recorded in step 2 "
            "is still present"),
        er=steps(
            "Driver Profile A is active",
            "The App Store app is recorded in Driver Profile A’s app tray",
            "The App Store app is removed from Driver Profile A’s app tray",
            "Driver Profile B is active",
            "The App Store app is still present in Driver Profile B’s "
            "app tray"),
        reasoning=(
            "驗證目標：11.5（CPA3）第一句 —— App Store app 被刪除時只對執行刪除"
            "之使用者失效，其他使用者不受影響。"
            "關鍵情境條件：須跨兩個 profile 觀察同一個 app，"
            "故以「A 刪除 → 切至 B 讀回」之端到端流程驗之（§12 首匹配 → 情境／用例）。"
            "為什麼這樣切：同節之更新（對所有已安裝者生效）與安裝（只出現在安裝者之 app tray）"
            "為不同觸發，屬 11.5 之 sibling leaf，本 TC 不代測。"
            "刻意略過：補句表所載之 Table CPA2 列項（Connected Navigation 等）"
            "為 11.4 之表格內容，與本 leaf 之刪除行為無關，故未寫入 ER。"),
        kw=["App Store", "delete", "app tray", "Connected Account",
            "Driver Profile"],
    ),

    "SWE1-HMI-PROF-128-01": dict(
        title="Valet Mode deactivation cancelled on the tenth incorrect PIN",
        design=BVA,
        pre=steps(
            "Valet Mode is active and a 4-digit PIN is set",
            "No PIN lockout is in effect"),
        data="PIN attempts: 9 incorrect attempts → 10th incorrect attempt",
        proc=steps(
            "Open the Valet Mode deactivation screen",
            "Enter an incorrect 4-digit PIN nine times",
            "Read the deactivation screen after the ninth attempt",
            "Enter an incorrect 4-digit PIN a tenth time and check that the "
            "deactivation is cancelled"),
        er=steps(
            "The Valet Mode deactivation screen is displayed",
            "Each of the nine incorrect PIN entries is rejected",
            "The deactivation screen still accepts a further PIN entry",
            "The deactivation is cancelled on the tenth incorrect attempt "
            "and a further PIN entry is not accepted"),
        remarks="條文之「30 分鐘後可再試」需 30 分鐘等待，本 TC 只驗第 10 次即"
                "取消且當下不再受理，未驗 30 分鐘後之解鎖",
        reasoning=(
            "驗證目標：12.9（PVAL9）—— 錯誤 PIN 之次數上限為 10，"
            "第 10 次錯誤時系統取消該次停用程序。"
            "關鍵情境條件：第 9 次（仍可續試）與第 10 次（取消）構成邊界前後（§5.6），"
            "故取邊界值分析。"
            "**來源標示（J-4）**：ER3「第 9 次後仍受理」之權威為 "
            "**§5.6 之 BVA 界前基準線**，非條文 —— 12.9 只寫「10 次後取消」。"
            "為什麼這樣切：條文之 activation 與 deactivation 共用同一上限，"
            "本 TC 取 deactivation 一側，activation 一側屬 12.9 之 sibling leaf。"
            "刻意略過：30 分鐘後可再試之驗證需等待 30 分鐘，"
            "其觸發為時間到期而非第 10 次錯誤，已具名記於 remarks。"),
        kw=["Valet Mode", "PIN", "10 attempts", "cancel", "lockout"],
    ),

    "SWE1-HMI-PROF-132-02": dict(
        title="SPAAK user blocked from exiting Valet Mode on the head unit",
        design=NEGATIVE,
        pre=steps(
            "Valet Mode is active under the SPAAK scenario",
            "The user at the head unit is the SPAAK user and not the vehicle "
            "owner",
            "The owner has an authorized app or website session available"),
        data="NA",
        proc=steps(
            "Open the head unit screens that offer a Valet Mode exit and "
            "attempt to exit Valet Mode",
            "Read the screen and check that the exit is blocked",
            "Deactivate Valet Mode remotely as the owner",
            "Read the head unit and check that Valet Mode is no longer "
            "active"),
        er=steps(
            "Any screen or popup that would allow a Valet Mode exit is "
            "blocked (PU0934)",
            "Valet Mode is still active after the SPAAK user’s attempt",
            "The owner’s remote deactivation is accepted",
            "Valet Mode is no longer active on the head unit"),
        reasoning=(
            "驗證目標：13.2（PVALSPK2）—— SPAAK 情境下 SPAAK 使用者不得於主機"
            "退出 Valet Mode，只有車主得以 app／網站等遠端方式停用。"
            "關鍵情境條件：受測之核心為「在主機上嘗試退出」此一不被允許之操作"
            "（§12 首匹配 → 負向測試），故以嘗試被阻擋為主要觀察點。"
            "為什麼這樣切：條文之兩半（主機不得退出、車主得遠端停用）互為對照，"
            "若只驗前半則「只有車主可以」無從成立，"
            "故遠端停用列為同一 TC 之末步，而非另切一條（§5.7 之例外已於上繳具名）。"
            "刻意略過：非 SPAAK 情境下之一般 Valet Mode 退出屬 ch12 之 leaf。"),
        kw=["SPAAK", "Valet Mode", "head unit", "remote deactivation",
            "PU0934"],
    ),
}


def sample_from_tsv() -> list:
    """版控之取樣清單（N-3）。"""
    return [ln.split("\t")[0] for ln in
            (FEATURE / "data" / "pilot_sample.tsv")
            .read_text(encoding="utf-8").splitlines()
            if ln and not ln.startswith(("#", "req_id"))]


def build() -> list:
    """依取樣順序組出 16 個 leaf 之產物。tc_id 依序指派（§10.3）。"""
    # 兩份清單並存就會有一天不一致 —— 生成前先比對，不一致即停。
    tsv = sample_from_tsv()
    if tsv != SAMPLE_IDS:
        raise SystemExit(f"取樣清單不一致：TSV {len(tsv)} 列 vs "
                         f"SAMPLE_IDS {len(SAMPLE_IDS)} 條\n"
                         f"  TSV 有而常數無：{[x for x in tsv if x not in SAMPLE_IDS]}\n"
                         f"  常數有而 TSV 無：{[x for x in SAMPLE_IDS if x not in tsv]}")
    sample = SAMPLE_IDS
    rows = B.leaf_rows()
    out = []
    for n, req_id in enumerate(sample, 1):
        ctx = B.assemble(req_id, rows[req_id])
        spec = TCS[req_id]
        refs = ctx["specification_reference"]
        for extra, _provides in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{extra}"
        prio, prio_why = PRIORITY[req_id]
        tc = {
            "req_id": req_id,
            "tc_id": B.TC_ID_FMT.format(n=n),
            "tc_title": spec["title"],
            "test_group": ctx["test_group"],
            "test_set": ctx["test_set"],
            # R-U6：BLANK 綁定 —— Test Item = 標準 §4.3 tc_title
            "test_item": spec["title"],
            "pre_conditions": spec["pre"],
            "input_test_data": spec["data"],
            "test_procedure": spec["proc"],
            "expected_result": spec["er"],
            "specification_reference": refs,
            "priority": prio,
            "priority_basis": prio_why,
            "design_method": spec["design"],
            "functional_safety": "NA",
            "estimated_test_time": "",
            "remarks": spec.get("remarks", ""),
            "split_flag": False,
            "split_reason": "",
        }
        out.append({
            "parent": req_id,
            "outline": ctx["section"],
            "batch": "pilot",
            "test_set": ctx["test_set"],
            "sub_categorization": ctx["sub_categorization"],
            "priority_prior_037": ctx["priority_prior_037"],
            "source_clause": ctx["spec_body"],
            "source_clause_origin": ctx["spec_body_source"],
            "leaf_desc_037": ctx["leaf_desc_037"],
            "must_carry_injected": ctx["must_carry"],
            "reasoning": spec["reasoning"],
            "keywords": spec["kw"],
            "duplicate_of": "",
            "tcs": [tc],
        })
    return out


SAMPLE_IDS = [
    "SWE1-HMI-PROF-001-01", "SWE1-HMI-PROF-002-03", "SWE1-HMI-PROF-021-01",
    "SWE1-HMI-PROF-032", "SWE1-HMI-PROF-048", "SWE1-HMI-PROF-053",
    "SWE1-HMI-PROF-059-01", "SWE1-HMI-PROF-062-02", "SWE1-HMI-PROF-073-01",
    "SWE1-HMI-PROF-070", "SWE1-HMI-PROF-091-01", "SWE1-HMI-PROF-104",
    "SWE1-HMI-PROF-111", "SWE1-HMI-PROF-112-01", "SWE1-HMI-PROF-128-01",
    "SWE1-HMI-PROF-132-02",
]


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    recs = build()
    for r in recs:
        (OUT / f"{r['parent']}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"寫出 {len(recs)} 個 leaf 檔，共 "
          f"{sum(len(r['tcs']) for r in recs)} 條 TC → {OUT}")
