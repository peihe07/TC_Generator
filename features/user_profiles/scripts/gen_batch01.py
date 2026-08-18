#!/usr/bin/env python3
"""第一批正式批次之生成器（17 包作業 C）—— ch9→10→11，27 leaf ＋ 1 條負向配對。

## 與 `gen_pilot.py` 之關係

同一套形狀與同一組欄位；**取樣清單與 tc_id 起點不同**：

| | pilot | 本批 |
|---|---|---|
| 取樣清單 | `data/pilot_sample.tsv`（16 leaf）| `data/batch01_sample.tsv`（27 leaf）|
| tc_id | 001–016 | **017–044** |
| 額外 TC | 無 | `PROF-111` 之 R1 High 反面（§7 負向配對，**非新 leaf**）|

**共用之判準一律引用 pilot 之落點，不重寫**：R-U6（test_item＝tc_title）、
R-U5 ＋ D-UP16-01（priority 與其 tie-break）、§12（design method 首匹配）、
R-U35 (a)（spec 內文取 `pdf_text`）。

## 本批之三項已知風險（16 輪 §6.5，17 包作業 C 要求逐項回報）

1. `PROF-085` 之 must_carry 含 `Stellantis Account` —— R1 High 之 TC 須寫
   `Connected Account`（R-U35 (c)）；本檔以 R1 High 為 pre-condition，
   字面值用 `Connected Account`，並由 `lint_variant_labels` 把關。
2. `9.5.x` 四條座椅交換之 sibling 軸見各條 `axis` 註記。
3. ch10 三條之 037 先驗全為 Low —— **逐條依 rubric 判**，見 `PRIORITY`。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                      # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE, BVA, SCENARIO,   # noqa: E402
                       NEGATIVE)

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
SAMPLE_TSV = FEATURE / "data" / "batch01_sample.tsv"
TC_START = 17

REF_EXTRA = {
    # 9.3.1 之受限項目清單出自 9.3（EDPR3），該清單即本 TC 之受測對象
    "SWE1-HMI-PROF-090": ["9.3"],
    # 9.3.2 之 "the message specified above" 指 9.3.1（同 pilot 之 091-01）
    "SWE1-HMI-PROF-091-02": ["9.3.1"],
    # 10.3 之「show the same page as from the Edit Profiles tab」指 10.2 之頁面
    "SWE1-HMI-PROF-107": ["10.2"],
}

# 037 先驗 → R-U5 rubric（**逐條具名**；D-UP16-01 之 tie-break 於下方註明）
PRIORITY = {
    "SWE1-HMI-PROF-085": ("P2", "Edit Profile 清單之順序；呈現層"),
    "SWE1-HMI-PROF-086": ("P2", "8.4 吋版面之呈現差異"),
    "SWE1-HMI-PROF-087": ("P2", "未配備時之呈現隱藏"),
    "SWE1-HMI-PROF-088": ("P1", "區域／車型配置之非主路徑分支"),
    "SWE1-HMI-PROF-089": ("P1", "行車中之限制分支 —— **rubric 無安全帶，見上繳 17 §3**"),
    "SWE1-HMI-PROF-090": ("P2", "限制之回饋（音效與訊息）呈現"),
    "SWE1-HMI-PROF-091-02": ("P2", "同上；本條之單位為回饋本身"),
    "SWE1-HMI-PROF-092": ("P2", "avatar 選擇畫面之開啟"),
    "SWE1-HMI-PROF-093": ("P2", "avatar 畫面之呈現細節"),
    "SWE1-HMI-PROF-094": ("P1", "未存即離開不得改動 avatar —— **失效即使用者資料被意外變更**"),
    "SWE1-HMI-PROF-095": ("P0", "記憶座椅連結＝PLP 3.5 之偏好；本條為其規則本身"),
    "SWE1-HMI-PROF-096": ("P1", "同上之分支（前置已連結）—— 依 D-UP16-01，分支歸 P1"),
    "SWE1-HMI-PROF-097": ("P1", "同上之分支（前置未連結）"),
    "SWE1-HMI-PROF-098": ("P2", "「none」選項之可用性邊界；呈現層"),
    "SWE1-HMI-PROF-099": ("P0", "座椅位置之儲存與其歸屬 —— 偏好之儲存與回復"),
    "SWE1-HMI-PROF-100": ("P2", "welcome popup 尺寸之預設值"),
    "SWE1-HMI-PROF-101": ("P0", "刪除前之確認 —— **資料遺失風險之防線本身**"),
    "SWE1-HMI-PROF-102": ("P2", "刪除後之導覽落點"),
    "SWE1-HMI-PROF-103": ("P1", "刪除後之 active profile 接續；失效即無現用 profile"),
    "SWE1-HMI-PROF-105": ("P3", "單頁最多 6 行 —— 版面上限，失效僅影響該頁可讀性"),
    "SWE1-HMI-PROF-106": ("P2", "linked-info 頁之開啟（**037 先驗 Low，本判為 P2**）"),
    "SWE1-HMI-PROF-107": ("P3", "同一頁之**第二入口**；失效時仍可由 Edit Profile 進入"),
    "SWE1-HMI-PROF-108": ("P2", "linked-info 頁之內容（**037 先驗 Low，本判為 P2**）"),
    "SWE1-HMI-PROF-109": ("P1", "連網配置之非主路徑分支"),
    "SWE1-HMI-PROF-110": ("P2", "Connected Account 之導向"),
    "SWE1-HMI-PROF-112-02": ("P1", "app 更新之範圍；跨使用者之分支"),
    "SWE1-HMI-PROF-112-03": ("P1", "app 安裝之範圍；跨使用者之分支"),
}
PRIORITY_NEG = ("P2", "R1 High 變體之呈現（資訊按鈕不存在）")

TCS = {

    "SWE1-HMI-PROF-085": dict(
        title="Edit Profile tab lists options in Table EDPR1 order",
        design=FUNCTIONAL,
        pre=steps("The vehicle is an R1 High variant",
                  "A Driver Profile is active and setup assistant is not "
                  "completed for it"),
        data="NA",
        proc=steps("Open the Profile section and select the “Edit "
                   "Profile” tab",
                   "Read the option list and check that the items appear in "
                   "the Table EDPR1 order"),
        er=steps(
            "The “Edit Profile” tab is displayed",
            "The options are listed in the Table EDPR1 order: Resume Setup "
            "(only if not complete), Edit Name, Edit Avatar, Connected "
            "Account, Memory Seat (if applicable), Welcome Pop Up, Delete "
            "Profile, What is linked to my Profile?, Tutorials, More "
            "Settings; and a circled number 1 is shown next to Resume "
            "Tutorials"),
        # `remarks` 是測試員看得到的工作簿欄（AH）——
        # 在裡面寫出被禁用之 label 字面值本身就違反 R-U35 (c)，
        # 即使語氣是「不要用那個」。**lint 擋下的正是這個寫法。**
        remarks="R1 High：清單第四項之 label 依 spec 9.3.2 之變體覆寫，"
                "採 Connected Account（R-U35 (c)）。"
                "列項順序取自 must_carry 之 Table EDPR1（PDF p14）",
        reasoning=(
            "驗證目標：9.1（EDPR1）—— Edit Profile 分頁之選項須依 Table EDPR1 "
            "之順序列出，且 Resume Tutorials 旁有圈號 1。"
            "關鍵情境條件：圈號 1 之顯示以「setup assistant 未完成」為前提，"
            "故列 pre-condition；列項字串取自補句表之 Table EDPR1（PDF p14），非自擬。"
            "為什麼這樣切：本 leaf 之單位為「順序」，各項之連結去向"
            "（Connected Account → app、More Settings → My Profile）屬 9.1 之"
            "其他斷言與 11.3.1／9.8 之 leaf，本 TC 不代測。"
            "刻意略過：**本 TC 以 R1 High 為條件**，故 label 用 Connected Account；"
            "非 R1 High 車上該項為 Stellantis Account，其對照未生成（取樣單位為 leaf）。"),
        kw=["Edit Profile", "Table EDPR1", "order", "Resume Tutorials"],
    ),

    "SWE1-HMI-PROF-086": dict(
        title="Username and avatar hidden left of the 8.4-inch edit list",
        design=FUNCTIONAL,
        pre=steps("The vehicle has an 8.4-inch screen",
                  "A Driver Profile with a username is active"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Read the screen and check that no username or avatar is "
                   "shown left of the list"),
        er=steps("The “Edit Profile” tab is displayed",
                 "No username or avatar is shown to the left of the Edit "
                 "Profile List, and the username appears in the Edit "
                 "Username line as “Edit username: [username]”"),
        reasoning=(
            "驗證目標：9.1.1（EDPR1.1）—— 8.4 吋螢幕不在清單左側顯示 username "
            "與 avatar，改於 Edit Username 該行顯示。"
            "關鍵情境條件：螢幕尺寸為條件本身，列 pre-condition；"
            "兩個觀察點（左側不顯示／該行顯示）為同一條件之兩個結果，併為一條 ER。"
            "為什麼這樣切：其他尺寸之版面屬 9.1 之常態，本 leaf 只管 8.4 吋之差異。"),
        kw=["8.4 inch", "username", "avatar", "Edit Profile List"],
    ),

    "SWE1-HMI-PROF-087": dict(
        title="Memory seat status hidden when seats are not equipped",
        design=FUNCTIONAL,
        pre=steps("The vehicle is not equipped with memory seats",
                  "A Driver Profile is active"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Read the option list and check that no memory seat "
                   "status is shown"),
        er=steps("The “Edit Profile” tab is displayed",
                 "No memory seat status is available in the list"),
        reasoning=(
            "驗證目標：9.1.2（EDPR1.2）—— 未配備記憶座椅之車輛不顯示記憶座椅狀態。"
            "關鍵情境條件：車輛配置為條件本身，列 pre-condition。"
            "為什麼這樣切：已配備車輛之記憶座椅狀態與其操作屬 9.5.x 之 leaf，"
            "本 TC 只驗其不存在。"),
        kw=["memory seat", "not equipped", "Edit Profile"],
    ),

    "SWE1-HMI-PROF-088": dict(
        title="Connected Account hidden for unsupported regions",
        design=FUNCTIONAL,
        pre=steps("The vehicle is in a region without the brand app",
                  "A Driver Profile is active"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Read the option list and check that no Connected "
                   "Account button or Connected Profile info is shown"),
        er=steps("The “Edit Profile” tab is displayed",
                 "No Connected Profile options or info and no Connected "
                 "Account button are shown"),
        remarks="R1 High：label 為 Connected Account（spec 本節寫 "
                "Stellantis Connected Account）—— R-U35 (c)",
        reasoning=(
            "驗證目標：9.2（EDPR2）—— 無 <Brand> app 之區域不顯示 Connected "
            "Profile 之選項／資訊與 Connected Account 按鈕。"
            "關鍵情境條件：條文有兩個獨立條件（區域無 app／車輛不支援），"
            "本 TC 取「區域」一側；車輛不支援一側之條件相同而觸發不同，"
            "由 11.3（CPA1）之 leaf 承擔（其文為 do not show if the vehicle does "
            "not support connectivity）。"
            "為什麼這樣切：兩個條件若併於一條 TC，失敗時分不出是哪一個條件沒生效。"),
        kw=["Connected Account", "region", "brand app", "hidden"],
    ),

    "SWE1-HMI-PROF-089": dict(
        title="Edit options greyed out while the vehicle is in motion",
        design=STATE,
        pre=steps("A Driver Profile is active and the “Edit Profile” "
                  "tab is displayed",
                  "The vehicle is stationary on a test track and can be "
                  "brought into motion"),
        data="NA",
        proc=steps("Read the option list and record which items are "
                   "selectable",
                   "Bring the vehicle into motion",
                   "Read the option list and check that the restricted items "
                   "are greyed out"),
        er=steps(
            "The options recorded in step 1 are selectable while stationary",
            "The vehicle is in motion",
            "Deleting a Profile, editing username, editing avatar, "
            "Tutorials, Resume Setup, and viewing info of what is linked to "
            "a Profile are greyed out and cannot be selected"),
        reasoning=(
            "驗證目標：9.3（EDPR3）—— 行車中六個項目變灰且不可選取。"
            "關鍵情境條件：判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換），"
            "故以步驟 1 之靜止狀態為基準線（§5.6）。"
            "為什麼這樣切：六個項目為同一觸發之同一結果，依 §5.7 併為一條 ER；"
            "選取時之 bonk 與訊息屬 9.3.1、進行中被中斷屬 9.3.2，兩者觸發不同。"),
        kw=["in motion", "greyed out", "Edit Profile", "restricted items"],
    ),

    "SWE1-HMI-PROF-090": dict(
        title="Bonk tone and message when a restricted item is selected",
        design=NEGATIVE,
        pre=steps("A Driver Profile is active and the “Edit Profile” "
                  "tab is displayed",
                  "The vehicle is in motion on a test track"),
        data="NA",
        proc=steps("Select the greyed-out “Delete Profile” item",
                   "Read the screen and check that the bonk tone and the "
                   "message are presented"),
        er=steps("The selection is not accepted",
                 "A bonk tone is played and “Function not available "
                 "while vehicle in Motion.” is displayed"),
        reasoning=(
            "驗證目標：9.3.1（EDPR3.1）—— 行車中選取受限項目時播放 bonk 音"
            "並顯示指定訊息。"
            "關鍵情境條件：受測動作為對已變灰項目之選取，屬不被允許之操作"
            "（§12 首匹配 → 負向測試）；受限項目之清單出自 9.3，故併列該節。"
            "為什麼這樣切：本 leaf 之單位為「回饋」，項目是否變灰屬 9.3、"
            "進行中被中斷屬 9.3.2。"),
        kw=["bonk", "message", "in motion", "restricted"],
    ),

    "SWE1-HMI-PROF-091-02": dict(
        title="Bonk tone and message accompany the interruption in motion",
        design=STATE,
        pre=steps("The vehicle is an R1 High variant",
                  "The vehicle is stationary on a test track and can be "
                  "brought into motion"),
        data="NA",
        proc=steps("Open the Edit Profile tab and start editing the Profile "
                   "username",
                   "Bring the vehicle into motion",
                   "Read the screen and check that the bonk tone and the "
                   "message are presented"),
        er=steps("The username editing page is displayed",
                 "The vehicle is in motion and the task is interrupted",
                 "A bonk tone is played and “Function not available "
                 "while vehicle in Motion.” is displayed"),
        remarks="R1 High：label 依 9.3.2 之變體覆寫採 Connected Account"
                "（R-U35 (c)）。sibling 軸：本條驗**回饋**，"
                "091-01 驗**返回前一頁** —— 同一觸發之兩個結果，"
                "分屬兩個 037 leaf（§8.2.1）",
        reasoning=(
            "驗證目標：9.3.2（EDPR3.2）之回饋部分 —— 進行中被中斷時播 bonk "
            "並顯示訊息。"
            "關鍵情境條件：同 091-01 之狀態轉換（靜止→行進），"
            "差別在觀察點：091-01 觀察頁面返回，本條觀察音效與訊息。"
            "為什麼這樣切：037 為 9.3.2 切出兩個 leaf，一葉一 TC（§8.2.1）；"
            "訊息字串出自 9.3.1，故併列該節。"),
        kw=["bonk", "message", "interrupt", "in motion"],
    ),

    "SWE1-HMI-PROF-092": dict(
        title="Avatar selection screen opens from avatar or Change Avatar",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile is active and the “Edit Profile” "
                  "tab is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press anywhere on the avatar",
                   "Read the screen and check that the avatar selection "
                   "screen is displayed",
                   "Return to the “Edit Profile” tab",
                   "Press anywhere on the “Change Avatar” line and "
                   "check that the same screen is displayed"),
        er=steps("The avatar is pressed",
                 "The avatar selection screen is displayed",
                 "The “Edit Profile” tab is displayed",
                 "The avatar selection screen is displayed"),
        reasoning=(
            "驗證目標：9.4（EDPR5）—— 按 avatar 或按「Change Avatar」該行"
            "皆開啟 avatar 選擇畫面。"
            "關鍵情境條件：條文明列兩個入口，兩者為**不同觸發同一結果**，"
            "故於一條 TC 內各驗一次（非拆兩條 —— 拆了會產生兩條除入口外全同之 TC）。"
            "為什麼這樣切：該畫面之內容屬 9.4.1、離開不存之行為屬 9.4.2。"),
        kw=["avatar", "Change Avatar", "selection screen"],
    ),

    "SWE1-HMI-PROF-093": dict(
        title="Current avatar highlighted among the available avatars",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile with a selected avatar is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the avatar selection screen from the “Edit "
                   "Profile” tab",
                   "Read the screen and check that the current avatar is "
                   "highlighted"),
        er=steps("The avatar selection screen is displayed",
                 "The currently selected avatar is highlighted and all other "
                 "available avatars are offered"),
        reasoning=(
            "驗證目標：9.4.1（EDPR5.1）—— 選擇畫面須標示目前 avatar，"
            "並提供其餘可用 avatar。"
            "關鍵情境條件：pre-condition 要求該 profile 已有 avatar，"
            "否則「目前之 avatar」無從觀察。"
            "為什麼這樣切：畫面之開啟屬 9.4，本 leaf 只管其內容。"),
        kw=["avatar", "highlighted", "available avatars"],
    ),

    "SWE1-HMI-PROF-094": dict(
        title="Avatar unchanged when the screen is exited without saving",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile with a selected avatar is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the avatar selection screen and record the current "
                   "avatar",
                   "Select a different avatar without saving",
                   "Exit the screen without saving",
                   "Read the “Edit Profile” tab and check that the "
                   "avatar recorded in step 1 is still in use"),
        er=steps("The avatar selection screen is displayed and the current "
                 "avatar is recorded",
                 "The different avatar is selected on the screen",
                 "The screen is exited without saving",
                 "The avatar recorded in step 1 is still in use"),
        reasoning=(
            "驗證目標：9.4.2（EDPR5.2）—— 未儲存即離開不得造成 avatar 變更。"
            "關鍵情境條件：須先在畫面上選了別的 avatar 才有「未存即離開」可言，"
            "故步驟 2 為必要之設置，非多餘。"
            "為什麼這樣切：儲存後之變更屬 9.4 之正向路徑，本 leaf 只管未儲存之路徑；"
            "失效之後果是使用者資料被意外變更，故判 P1 而非 P2。"),
        kw=["avatar", "exit without saving", "unchanged"],
    ),

    "SWE1-HMI-PROF-095": dict(
        title="Active Profile linked to the swapped memory seat position",
        design=STATE,
        pre=steps("The vehicle is equipped with memory seats",
                  "Two Driver Profiles exist and Profile A is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab and read the memory "
                   "seat linked to Profile A",
                   "Swap the memory seat preference to another position",
                   "Read the memory seat status and check that Profile A is "
                   "linked to the new position"),
        er=steps("The memory seat currently linked to Profile A is recorded",
                 "The memory seat preference is swapped",
                 "Profile A is linked to the newly selected memory seat "
                 "position"),
        remarks="sibling 軸（9.5.x 四條）：本條＝**交換之通則**；"
                "9.5.1＝前置**已**連結之分支；9.5.2＝前置**未**連結之分支；"
                "9.5.3＝「none」選項之可用性",
        reasoning=(
            "驗證目標：9.5（EDPR6）—— 交換記憶座椅偏好後，現用 profile 連結至"
            "該座椅位置，直到下一次變更。"
            "關鍵情境條件：判準為連結狀態之轉換（§12 首匹配 → 狀態轉換），"
            "以步驟 1 之原連結為基準線（§5.6）。"
            "為什麼這樣切：本條為通則，9.5.1／9.5.2 為其依前置狀態分出之兩個分支，"
            "037 已為三者各切一 leaf，一葉一 TC（§8.2.1）。"),
        kw=["memory seat", "swap", "linked", "active Profile"],
    ),

    "SWE1-HMI-PROF-096": dict(
        title="Seat preferences swapped when the active Profile was linked",
        design=STATE,
        pre=steps("The vehicle is equipped with memory seats",
                  "Profile A is active and linked to memory seat 1",
                  "Profile B is linked to memory seat 2",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Select memory seat 2 for Profile A",
                   "Read the memory seat status of both Profiles and check "
                   "that the two preferences are swapped"),
        er=steps("The “Edit Profile” tab is displayed",
                 "Memory seat 2 is selected for Profile A",
                 "Profile A is linked to memory seat 2 and Profile B is "
                 "linked to memory seat 1"),
        remarks="sibling 軸：前置狀態＝active Profile **已**連結座椅（對照 9.5.2）",
        reasoning=(
            "驗證目標：9.5.1（EDPR6.1）—— 現用 profile 原已連結座椅時，"
            "與新座椅之原持有者**互換**。"
            "關鍵情境條件：pre-condition 明訂兩個 profile 各有連結，"
            "否則「互換」無從成立 —— 這也是本條與 9.5.2 之唯一分野。"
            "為什麼這樣切：前置未連結之情形由 9.5.2 承擔，"
            "兩者之 pre-condition 互斥，不會重複覆蓋。"),
        kw=["memory seat", "swap", "previously linked", "two Profiles"],
    ),

    "SWE1-HMI-PROF-097": dict(
        title="Previous Profile unlinked when the active Profile had none",
        design=STATE,
        pre=steps("The vehicle is equipped with memory seats",
                  "Profile A is active and is not linked to any memory seat",
                  "Profile B is linked to memory seat 2",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Select memory seat 2 for Profile A",
                   "Read the memory seat status of both Profiles and check "
                   "that Profile B is no longer linked"),
        er=steps("The “Edit Profile” tab is displayed",
                 "Memory seat 2 is selected for Profile A",
                 "Profile A is linked to memory seat 2 and Profile B is not "
                 "linked to any memory seat position"),
        remarks="sibling 軸：前置狀態＝active Profile **未**連結座椅（對照 9.5.1）",
        reasoning=(
            "驗證目標：9.5.2（EDPR6.2）—— 現用 profile 原無連結時，"
            "直接接管該座椅，原持有者變為無連結。"
            "關鍵情境條件：pre-condition 明訂 Profile A 無連結 ——"
            "此即與 9.5.1 之分野；兩條之其餘設置刻意保持相同，"
            "使失敗時可歸因於前置狀態而非別的差異。"
            "為什麼這樣切：037 已為兩個前置狀態各切一 leaf。"),
        kw=["memory seat", "unlink", "not previously linked"],
    ),

    "SWE1-HMI-PROF-098": dict(
        title="None option greyed out until Profiles outnumber memory seats",
        design=BVA,
        pre=steps("The vehicle is equipped with two memory seats",
                  "Two Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="Profile count vs memory seat count: 2 vs 2 (equal) → "
             "3 vs 2 (exceeds)",
        proc=steps("Open the memory seat option list and read the "
                   "“none” option",
                   "Create a third Driver Profile",
                   "Open the memory seat option list and check that the "
                   "“none” option is available"),
        er=steps("The “none” option is greyed out and not available "
                 "while two Profiles exist",
                 "The third Driver Profile is created",
                 "The “none” option is available"),
        reasoning=(
            "驗證目標：9.5.3（EDPR6.3）——「none」在 profile 數超過記憶座椅數"
            "之前不可用。"
            "關鍵情境條件：以 2 vs 2（相等，仍不可用）與 3 vs 2（超過，可用）"
            "構成邊界前後（§5.6），故取邊界值分析；"
            "條文之「exceeds」為嚴格大於，相等時仍不可用即為本 TC 之界前基準線。"
            "為什麼這樣切：座椅連結之交換規則屬 9.5–9.5.2，本 leaf 只管該選項之可用性。"),
        kw=["none", "greyed out", "memory seats", "Profile count"],
    ),

    "SWE1-HMI-PROF-099": dict(
        title="Saved seat position updates the Profile linked to that seat",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with memory seats",
                  "Profile A is active and Profile B is linked to memory "
                  "seat 2",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Change the seat position",
                   "Save the position to memory seat 2",
                   "Read the popup and check that it names the Profile the "
                   "seat was saved to"),
        er=steps("The seat position is changed",
                 "The position is saved to memory seat 2 and the seat "
                 "position stored for Profile B is updated",
                 "PU0588 is displayed and informs the user that the seat was "
                 "saved to Profile B"),
        reasoning=(
            "驗證目標：9.6（EDPR7）—— 儲存座椅位置會更新**該座椅所連 profile** "
            "之位置；若該座椅非現用 profile 所連，儲存時顯示 PU0588 告知存到誰。"
            "關鍵情境條件：pre-condition 令現用者為 A 而該座椅連 B，"
            "否則 PU0588 之觸發條件不成立。"
            "為什麼這樣切：兩項為同一觸發（按儲存）之兩個結果，依 §5.7 併為一條 TC。"
            "刻意略過：座椅連結之變更屬 9.5.x，本條之連結關係固定不動。"),
        kw=["memory seat", "save", "PU0588", "linked Profile"],
    ),

    "SWE1-HMI-PROF-100": dict(
        title="Welcome popup size defaults to small and can be turned off",
        design=FUNCTIONAL,
        pre=steps("A newly created Driver Profile exists and has not had its "
                  "Welcome Popup size changed",
                  "The vehicle is stationary"),
        data="Welcome Popup size setting: default → Off",
        proc=steps("Open the “Edit Profile” tab and read the Welcome "
                   "Popup size setting",
                   "Set the Welcome Popup size to Off",
                   "Activate another Profile and then reactivate this "
                   "Profile",
                   "Read the screen and check that no welcome popup is "
                   "shown"),
        er=steps("The Welcome Popup size setting reads Small",
                 "The Welcome Popup size is set to Off",
                 "The Profile becomes active again",
                 "No welcome popup is shown for that Profile"),
        reasoning=(
            "驗證目標：9.6.1（EDPR7.1）—— 尺寸設定預設為 small；設為 off 後"
            "該 profile 成為現用時不顯示 welcome popup。"
            "關鍵情境條件：預設值須在未被改過之 profile 上讀，"
            "故 pre-condition 明訂為新建且未調整過。"
            "為什麼這樣切：兩項為同一設定之兩個面向（預設值與關閉後之效果），"
            "且第二項須先讀第一項才有基準線。"
            "刻意略過：large 為全螢幕 popup 之呈現屬 7.2.1 之 leaf。"),
        kw=["Welcome Popup", "default", "small", "off"],
    ),

    "SWE1-HMI-PROF-101": dict(
        title="Verification popup shown before a Profile is deleted",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist and Profile A is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab and select "
                   "“Delete Profile”",
                   "Read the screen and check that a verification popup is "
                   "displayed before any deletion"),
        er=steps("“Delete Profile” is selected",
                 "A verification popup asking to confirm the delete is "
                 "displayed and the Profile is not yet deleted"),
        reasoning=(
            "驗證目標：9.7（EDPR8）—— 選擇刪除後、實際刪除前須有確認 popup。"
            "關鍵情境條件：ER 明寫「尚未刪除」—— 若只驗 popup 出現而不驗"
            "資料仍在，一個「先刪再問」之實作也會通過（§7 false pass）。"
            "為什麼這樣切：刪除後之導覽屬 9.7.1、刪除後之 active profile 屬 9.7.2；"
            "本條為資料遺失風險之防線本身，故判 P0。"),
        kw=["Delete Profile", "verification popup", "confirm"],
    ),

    "SWE1-HMI-PROF-102": dict(
        title="All Profiles tab shown after a Profile is deleted",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist and Profile A is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab and delete Profile A",
                   "Confirm the deletion in the verification popup",
                   "Read the screen and check that the “All "
                   "Profiles” tab is displayed"),
        er=steps("The deletion of Profile A is started",
                 "The deletion is confirmed",
                 "The “All Profiles” tab is displayed"),
        reasoning=(
            "驗證目標：9.7.1（EDPR8.1）—— 自 Edit Profile 分頁刪除 profile 後"
            "回到 All Profiles 分頁。"
            "關鍵情境條件：須先通過 9.7 之確認 popup 才會真的刪除，"
            "故確認列為步驟 2 而非略過。"
            "為什麼這樣切：哪一個 profile 成為現用屬 9.7.2，本條只管導覽落點。"),
        kw=["delete", "All Profiles tab", "navigation"],
    ),

    "SWE1-HMI-PROF-103": dict(
        title="User 1 or the last known Profile becomes active after deletion",
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist and Profile A is active",
                  "Profile A is not linked to any memory seat",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record which Profile was active before Profile A",
                   "Delete Profile A and confirm the deletion",
                   "Read the Profile List and check which Profile is active"),
        er=steps("The Profile active before Profile A is recorded",
                 "Profile A is deleted",
                 "“User 1” or the Profile recorded in step 1 is "
                 "active"),
        reasoning=(
            "驗證目標：9.7.2（EDPR8.2）—— 刪除未連結記憶座椅之 profile 後，"
            "「User 1」或前一個已知 profile 成為現用。"
            "關鍵情境條件：pre-condition 明訂被刪者未連結座椅 ——"
            "已連結者之行為條文未述，不在本 TC。"
            "為什麼這樣切：條文以「或」給出兩個可接受結果，ER 照錄其二擇一，"
            "不自行選定其一（§8.4.1）。"),
        kw=["delete", "User 1", "last known Profile", "active"],
    ),

    "SWE1-HMI-PROF-105": dict(
        title="Edit Profile tab shows at most six lines per page",
        design=BVA,
        pre=steps("A Driver Profile is active with all optional items "
                  "available",
                  "The vehicle is stationary"),
        data="Line count per page: 6 (limit)",
        proc=steps("Open the “Edit Profile” tab",
                   "Count the information lines shown and check that no more "
                   "than six are on the page"),
        er=steps("The “Edit Profile” tab is displayed",
                 "At most six lines of information are shown on the page"),
        reasoning=(
            "驗證目標：9.9（EDPR10）—— Edit Profile 分頁每頁最多 6 行資訊。"
            "關鍵情境條件：須在選項最多之情況下才驗得到上限，"
            "故 pre-condition 要求各選用項目皆可用。"
            "為什麼這樣切：清單之順序屬 9.1，本 leaf 只管每頁行數之上限。"),
        kw=["Edit Profile", "six lines", "per page", "maximum"],
    ),

    "SWE1-HMI-PROF-106": dict(
        title="Profile linked info page opens from the info line",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile is active and the “Edit Profile” "
                  "tab is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the “What is linked to my Profile” line",
                   "Read the screen and check that the linked info page is "
                   "displayed"),
        er=steps("The “What is linked to my Profile” line is pressed",
                 "A page of general info of what is linked to a Driver "
                 "Profile is displayed and no “Memory Seat” section "
                 "is shown"),
        reasoning=(
            "驗證目標：10.2（PRINFO1）—— 按該行（含「i」圖示）開啟 linked-info 頁，"
            "且該頁移除「Memory Seat」段。"
            "關鍵情境條件：條文之 Remove “Memory Seat” section for all vehicles "
            "為無條件要求，故列為 ER 之一部分而非另條。"
            "為什麼這樣切：該頁之文字內容屬 10.3.1、All Profiles 分頁之入口屬 10.3。"
            "刻意略過：條文之「see example above」指頁內示意圖，"
            "依 R-U51 之口徑（指涉所指之物）不併列 PLP 表。"),
        kw=["What is linked to my Profile", "info page", "Memory Seat"],
    ),

    "SWE1-HMI-PROF-107": dict(
        title="Info button on the All Profiles tab opens the same page",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the info button on the “Edit Profile” tab",
                   "Record the page shown",
                   "Open the “All Profiles” tab",
                   "Press the info button and check that the page recorded "
                   "in step 2 is displayed"),
        er=steps("The linked info page is displayed",
                 "The page is recorded",
                 "The “All Profiles” tab is displayed with an info "
                 "button",
                 "The same page as recorded in step 2 is displayed"),
        reasoning=(
            "驗證目標：10.3（PRINFO2）—— All Profiles 分頁亦有資訊按鈕，"
            "且顯示與 Edit Profile 分頁相同之頁面。"
            "關鍵情境條件：「相同」須以比對驗之，故步驟 1 先記錄另一入口之頁面。"
            "為什麼這樣切：該頁之內容屬 10.3.1；本條之單位是「第二入口與其同一性」，"
            "故判 P3 —— 失效時仍可由 Edit Profile 進入。"),
        kw=["info button", "All Profiles tab", "same page"],
    ),

    "SWE1-HMI-PROF-108": dict(
        title="Driver Profile info page shows the intro text and examples",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with Navigation",
                  "A Driver Profile is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the Driver Profile info page",
                   "Read the page and check that the intro text and the "
                   "applicable examples are shown"),
        er=steps("The Driver Profile Info Page is displayed",
                 "The page reads “Your Driver Profile will remember "
                 "your personal preferences for many of the features you use "
                 "in your vehicle everyday. Below are some examples.” "
                 "followed by the applicable examples, including the "
                 "Navigation examples"),
        remarks="條文之「the info in the chart above」指**頁內之 chart**"
                "（R-U51 口徑，D-UP12-02），非 PLP 表；"
                "Navigation 之有無為條文明列之適用條件，故列 pre-condition",
        reasoning=(
            "驗證目標：10.3.1（PRINFO2.1）—— 資訊頁之引言字串與其後之適用範例。"
            "關鍵情境條件：條文明言「若車輛無 Navigation 則不顯示 Navigation 範例」，"
            "故 pre-condition 指定為有 Navigation 之車，使該範例確實可觀察。"
            "為什麼這樣切：R1 High 之 Connected Account 類別描述為變體覆寫，"
            "屬同節之另一斷言，未併入本 TC。"
            "刻意略過：無 Navigation 車輛之對照未生成 —— 取樣單位為 leaf（§8.4.2）。"),
        kw=["Driver Profile Info Page", "intro text", "examples",
            "Navigation"],
    ),

    "SWE1-HMI-PROF-109": dict(
        title="Connected Account line shown when the vehicle has connectivity",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with connectivity",
                  "A Driver Profile is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab",
                   "Read the option list and check that the Connected "
                   "Account line item is displayed"),
        er=steps("The “Edit Profile” tab is displayed",
                 "The Connected Account line item is displayed"),
        remarks="不支援連網之對照（條文第二句）屬同節之反面，"
                "其覆蓋由 9.2（EDPR2）之 leaf 承擔",
        reasoning=(
            "驗證目標：11.3（CPA1）—— 具連網能力之車輛，Edit Profile 分頁"
            "一律顯示 Connected Account 項目。"
            "關鍵情境條件：車輛配置為條件本身，列 pre-condition。"
            "為什麼這樣切：條文另有「不支援則不顯示」之反面，"
            "其形態與 9.2 之區域／車型隱藏相同，由該 leaf 承擔，本條不重複。"),
        kw=["Connected Account", "connectivity", "Edit Profile"],
    ),

    "SWE1-HMI-PROF-110": dict(
        title="Connected Account opens the Connected Account App",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with connectivity",
                  "A Driver Profile is active and the “Edit Profile” "
                  "tab is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Connected Account line item",
                   "Read the screen and check that the Connected Account App "
                   "is displayed"),
        er=steps("The Connected Account line item is pressed",
                 "The Connected Account App is displayed"),
        reasoning=(
            "驗證目標：11.3.1（CPA1.2）—— 按下 Connected Account 進入其 App。"
            "關鍵情境條件：需具連網能力之車輛，否則該項目不存在（11.3）。"
            "為什麼這樣切：該 App 內之連線／存取行為條文以 etc. 帶過，"
            "無可驗之明文，故 ER 只驗其開啟（§8.4.1 不造值）。"),
        kw=["Connected Account", "app", "Edit Profile"],
    ),

    "SWE1-HMI-PROF-112-02": dict(
        title="App Store update applies to every user with it installed",
        design=SCENARIO,
        pre=steps("Two Driver Profiles exist, each with its own Connected "
                  "Account",
                  "The same App Store app is installed locally for both "
                  "Profiles",
                  "An update for that app is available"),
        data="NA",
        proc=steps("Activate Driver Profile A and record the app version",
                   "Update the app from Driver Profile A",
                   "Activate Driver Profile B",
                   "Read the app version and check that it matches the "
                   "updated version"),
        er=steps("The app version in Driver Profile A is recorded",
                 "The app is updated for Driver Profile A",
                 "Driver Profile B is active",
                 "The app in Driver Profile B is at the updated version"),
        remarks="sibling 軸（11.5 三條）：刪除＝只對執行者（112-01）／"
                "更新＝對全部已安裝者（本條）／安裝＝只對安裝者（112-03）",
        reasoning=(
            "驗證目標：11.5（CPA3）第二句 —— app 更新對所有本機已安裝之使用者生效。"
            "關鍵情境條件：兩個 profile 皆須先裝有該 app，否則「對全部生效」無從觀察。"
            "為什麼這樣切：037 為 11.5 切出三個 leaf（刪除／更新／安裝），"
            "三者觸發不同，一葉一 TC（§8.2.1）；三條合起來即該列舉之完整覆蓋（§7）。"),
        kw=["App Store", "update", "all users", "installed locally"],
    ),

    "SWE1-HMI-PROF-112-03": dict(
        title="Installed App Store app appears only in the installer app tray",
        design=SCENARIO,
        pre=steps("Two Driver Profiles exist, each with its own Connected "
                  "Account",
                  "The App Store app under test is not installed for either "
                  "Profile"),
        data="NA",
        proc=steps("Activate Driver Profile A and install the app from the "
                   "App Store",
                   "Read the app tray of Driver Profile A",
                   "Activate Driver Profile B",
                   "Open the app tray and check that the app is not present"),
        er=steps("The app is installed for Driver Profile A",
                 "The app is present in Driver Profile A’s app tray",
                 "Driver Profile B is active",
                 "The app is not present in Driver Profile B’s app tray"),
        remarks="sibling 軸：安裝＝只對安裝者（對照 112-01 刪除、112-02 更新）",
        reasoning=(
            "驗證目標：11.5（CPA3）第三句 —— 安裝之 app 只出現在安裝者之 app tray。"
            "關鍵情境條件：pre-condition 明訂兩者皆未安裝，"
            "否則 B 之 app tray 有該 app 時分不出是本次安裝造成還是原本就有。"
            "為什麼這樣切：正反兩個觀察點（A 有、B 無）為同一觸發之兩個結果，"
            "併於一條 TC（§5.7）。"),
        kw=["App Store", "install", "app tray", "local user"],
    ),
}

# §7 負向配對 —— `PROF-111` 之 R1 High 反面（**非新 leaf**）
NEG_111 = dict(
    req_id="SWE1-HMI-PROF-111",
    section="11.4",
    title="No info button next to Connected Account on R1 High",
    design=FUNCTIONAL,
    pre=steps("The vehicle is an R1 High variant",
              "A Driver Profile is active and the “Edit Profile” tab "
              "is available"),
    data="NA",
    proc=steps("Open the “Edit Profile” tab",
               "Read the Connected Account line and check that no info "
               "button is shown next to it"),
    er=steps("The “Edit Profile” tab is displayed with the Connected "
             "Account line",
             "No info button is shown next to the Connected Account button, "
             "and the Local vs Connected Profile screen cannot be opened"),
    remarks="§7 之負向配對：正向為 NR1L-UserProfiles-013（非 R1 High）。"
            "依據為 Table CPA2 之表級註記「**R1 High Only: This table "
            "(Table CPA2) is not applicable. There will be no info button "
            "showed nextto the Connected Account button.」（PDF p17）",
    reasoning=(
        "驗證目標：11.4 之 R1 High 變體 —— 該表不適用，且 Connected Account "
        "旁沒有資訊按鈕。"
        "關鍵情境條件：變體為條件本身（§8.7.3），列 pre-condition。"
        "為什麼這樣切：本條與 TC-013 構成 §7 之列舉配對 —— "
        "TC-013 驗「非 R1 High 有該畫面與其四列」，本條驗「R1 High 沒有入口」。"
        "**只有正向會使一個「永遠顯示該畫面」之實作通過**。"
        "刻意略過：R1 High 之其他變體差異（如 9.3.2 之 label 覆寫）屬各自之 leaf。"),
    kw=["R1 High", "info button", "Connected Account", "not applicable"],
)


def sample() -> list:
    return [ln.split("\t")[0] for ln in
            SAMPLE_TSV.read_text(encoding="utf-8").splitlines()
            if ln and not ln.startswith(("#", "req_id"))]


def build() -> list:
    ids = sample()
    if sorted(ids) != sorted(TCS):
        raise SystemExit(
            f"取樣清單與內容不一致：TSV {len(ids)} vs TCS {len(TCS)}\n"
            f"  TSV 有而 TCS 無：{[x for x in ids if x not in TCS]}\n"
            f"  TCS 有而 TSV 無：{[x for x in TCS if x not in ids]}")
    rows = B.leaf_rows()
    out, n = [], TC_START
    for req_id in ids:
        ctx = B.assemble(req_id, rows[req_id])
        spec = TCS[req_id]
        refs = ctx["specification_reference"]
        for extra in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{extra}"
        prio, why = PRIORITY[req_id]
        out.append(_rec(req_id, ctx, spec, refs, prio, why, n))
        n += 1

    # 負向配對 —— 掛在既有 leaf 之下，另存一檔以免覆寫 pilot 之產物
    ctx = B.assemble(NEG_111["req_id"], rows[NEG_111["req_id"]])
    rec = _rec(NEG_111["req_id"], ctx, NEG_111,
               ctx["specification_reference"], *PRIORITY_NEG, n)
    rec["parent"] = NEG_111["req_id"] + "-neg"
    rec["note"] = ("§7 負向配對 —— 與 pilot 之 NR1L-UserProfiles-013 同一 leaf，"
                   "**非新 leaf**；檔名加 `-neg` 以免覆寫該 leaf 之 pilot 產物")
    out.append(rec)
    return out


def _rec(req_id, ctx, spec, refs, prio, why, n) -> dict:
    tc = {
        "req_id": req_id,
        "tc_id": B.TC_ID_FMT.format(n=n),
        "tc_title": spec["title"],
        "test_group": ctx["test_group"],
        "test_set": ctx["test_set"],
        "test_item": spec["title"],          # R-U6
        "pre_conditions": spec["pre"],
        "input_test_data": spec["data"],
        "test_procedure": spec["proc"],
        "expected_result": spec["er"],
        "specification_reference": refs,
        "priority": prio,
        "priority_basis": why,
        "design_method": spec["design"],
        "functional_safety": "NA",
        "estimated_test_time": "",
        "remarks": spec.get("remarks", ""),
        "split_flag": False,
        "split_reason": "",
    }
    return {
        "parent": req_id,
        "outline": ctx["section"],
        "batch": "batch01",
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
    }


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    recs = build()
    for r in recs:
        (OUT / f"{r['parent']}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"寫出 {len(recs)} 個檔，共 {sum(len(r['tcs']) for r in recs)} 條 TC "
          f"（{recs[0]['tcs'][0]['tc_id']} … {recs[-1]['tcs'][0]['tc_id']}）")
