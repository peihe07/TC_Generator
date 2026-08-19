#!/usr/bin/env python3
"""第三批之生成器（28 包）—— **ch4 剩餘 26 leaf ＋ A-UP13 附掛 3**，tc_id 079–108。

## 批界（R-4，28 包）

批次記錄一律寫成 **「第三批 ＝ ch4 剩餘 26 ＋ A-UP13 附掛 3」**，
**不寫「第三批 ＝ ch4」** —— 附掛之三項落在 ch6／ch7，
批界是**被修訂**，不是被稀釋。

## 本批之四項先具名處置（下放包於生成前指出，故先寫在此）

1. **`002-02` 之 popup 內文不寫（R-U27）**：DR #4 仍缺 `PU1087`／`PU1088` 之
   popup **內文**。其觸發條件 spec p6 已載，故該 TC 得生成 ——
   **ER 只寫「該 popup 顯示」，不寫它上面寫什麼**（§8.4.1 不推定內容）。
   **本批唯一帶上游未決事項生成者。**
2. **`005` 之順序斷言須可區分**（見該條 reasoning）。
3. **委派一律指名 leaf id**（D-1）。
4. **PLP 併列之代價聲明隨引用欄同讀**（J-1／D-UP17-01）——
   `001-02`／`001-03`／`005`／`012` 四條之引用欄自動併列 `3.1`–`3.5`
   （`build_batch_context.PLP_LEAVES`），其 remarks 一律帶該聲明。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE,       # noqa: E402
                       NEGATIVE)
from gen_batch01 import _rec                           # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
TC_START = 79

# PLP 併列之代價聲明（J-1／D-UP17-01）—— **隨引用欄同讀**，不得只寫在別處
PLP_COST = ("引用欄併列 `3.1`–`3.5`（PLP 表，R-U22／R-U46）。"
            "**併列不等於該五列皆已被驗證** —— 覆蓋率不得以引用欄推定"
            "（J-1／D-UP17-01）；本 TC 實際受測之列項見 input_test_data。")

# 取樣清單（28 包核可）。順序即 tc_id 之指派順序。
SAMPLE = [
    "SWE1-HMI-PROF-001-02", "SWE1-HMI-PROF-001-03",
    "SWE1-HMI-PROF-002-01", "SWE1-HMI-PROF-002-02",
    "SWE1-HMI-PROF-003",
    "SWE1-HMI-PROF-004-01", "SWE1-HMI-PROF-004-02",
    "SWE1-HMI-PROF-004-03", "SWE1-HMI-PROF-004-04",
    "SWE1-HMI-PROF-005",
    "SWE1-HMI-PROF-006-01", "SWE1-HMI-PROF-006-02", "SWE1-HMI-PROF-006-03",
    "SWE1-HMI-PROF-007-01", "SWE1-HMI-PROF-007-02", "SWE1-HMI-PROF-007-03",
    "SWE1-HMI-PROF-008", "SWE1-HMI-PROF-009",
    "SWE1-HMI-PROF-010-01", "SWE1-HMI-PROF-010-02",
    "SWE1-HMI-PROF-011", "SWE1-HMI-PROF-012",
    "SWE1-HMI-PROF-013", "SWE1-HMI-PROF-014",
    "SWE1-HMI-PROF-015", "SWE1-HMI-PROF-016",
]

PRIORITY = {
    "SWE1-HMI-PROF-001-02": ("P0", "偏好之回復機制本身 —— R-U5 核心五類之一"),
    "SWE1-HMI-PROF-001-03": ("P2", "不可用項目之略過 —— 例外處理，非儲存機制本身"),
    "SWE1-HMI-PROF-002-01": ("P0", "回復預設時**不得波及他 profile 與 username／avatar**"
                                   " —— 資料遺失風險項"),
    "SWE1-HMI-PROF-002-02": ("P2", "回復進度之提示（PU1087／PU1088）；呈現層"),
    "SWE1-HMI-PROF-003": ("P1", "未設定 profile 仍可使用主機 —— 主要功能之可用性"),
    "SWE1-HMI-PROF-004-01": ("P0", "偏好跨 key cycle 之儲存 —— 核心五類之一"),
    "SWE1-HMI-PROF-004-02": ("P0", "自主機選取後之回復 —— 回復機制本身"),
    "SWE1-HMI-PROF-004-03": ("P1", "記憶座椅鍵之回復途徑；主要功能之另一入口"),
    "SWE1-HMI-PROF-004-04": ("P1", "key fob 偵測之回復途徑；主要功能之另一入口"),
    "SWE1-HMI-PROF-005": ("P0", "切換前先存 —— 失效即已變更之偏好遺失（資料遺失風險）"),
    "SWE1-HMI-PROF-006-01": ("P0", "key cycle 起始之 profile 載入 —— 切換機制本身"),
    "SWE1-HMI-PROF-006-02": ("P1", "key fob 之覆寫分支"),
    "SWE1-HMI-PROF-006-03": ("P1", "記憶座椅鍵之覆寫分支"),
    "SWE1-HMI-PROF-007-01": ("P0", "預設 profile 之存在保證 —— profile 建立之底線"),
    "SWE1-HMI-PROF-007-02": ("P0", "全部刪除後之預設重建 —— 資料遺失後之回復"),
    "SWE1-HMI-PROF-007-03": ("P1", "重建後之單一 profile 形態；其座椅數條件為分支"),
    "SWE1-HMI-PROF-008": ("P1", "每個記憶座椅位置之預設 profile；配置相依之分支"),
    "SWE1-HMI-PROF-009": ("P1", "記憶座椅偏好之互換；主要功能之進階操作"),
    "SWE1-HMI-PROF-010-01": ("P1", "刪除時之座椅自動改派；非主路徑分支"),
    "SWE1-HMI-PROF-010-02": ("P1", "無可用 profile 時之預設自動建立"),
    "SWE1-HMI-PROF-011": ("P1", "刪除後之新現用 profile 判定"),
    "SWE1-HMI-PROF-012": ("P0", "預設回復時全部偏好歸零 —— 資料遺失風險項"),
    "SWE1-HMI-PROF-013": ("P2", "狀態列按鈕之預設存在與其圖示變化；呈現層"),
    "SWE1-HMI-PROF-014": ("P2", "客製 profile 之圖示內容；呈現層"),
    "SWE1-HMI-PROF-015": ("P3", "開啟時之 highlight 狀態；UI 強化"),
    "SWE1-HMI-PROF-016": ("P3", "移除後 highlight 於他處之保留；罕用情境"),
}

TCS = {

    # ── 4.1 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-001-02": dict(
        title="Stored preferences recalled when a Driver Profile is activated",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The features carrying the preferences under test are "
                  "available for the vehicle and the region"),
        data="Preferences under test: Cluster Home screen (3.1), "
             "SiriusXM 360L Listener Profile (3.2)",
        proc=steps("Activate Driver Profile A and record the two preferences",
                   "Activate Driver Profile B",
                   "Activate Driver Profile A and check that the two "
                   "preferences match the values recorded in step 1"),
        er=steps("Driver Profile A is active and the two preference values "
                 "are recorded",
                 "Driver Profile B is active",
                 "Driver Profile A is active and the two preferences match "
                 "the values recorded in step 1"),
        remarks=PLP_COST + " 本 leaf 之單位為**啟用時之回復**；"
                "儲存側由 `SWE1-HMI-PROF-001-01` 承擔（pilot 之 TC-001）。",
        reasoning=(
            "驗證目標：4.1（PRACC1）之回復側 —— profile 啟用時回復其已儲存之偏好。"
            "關鍵情境條件：受測偏好取自 PLP 表 3.1／3.2 之逐字列項，非自擬（§8.4.1）；"
            "條文之「feature 不可用則忽略」以 pre-condition 限定該二項在本車可用。"
            "為什麼這樣切：037 對 4.1 切三個 leaf，本 leaf（-02）之單位為"
            "**啟用時之回復**，一葉一 TC（§8.2.1）。"
            "**中間切至 Profile B 是必要的** —— 若不切走，「回復」與「值本來就在畫面上」"
            "無從分辨。"
            "刻意略過：不可用項目之略過屬 `SWE1-HMI-PROF-001-03`；"
            "儲存側屬 `SWE1-HMI-PROF-001-01`。"),
        kw=["recall", "profile activation", "PLP", "preferences"],
    ),

    "SWE1-HMI-PROF-001-03": dict(
        title="Unavailable features skipped when storing and recalling",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "At least one preference in the PLP table belongs to a "
                  "feature not available for this vehicle or region"),
        data="Preference under test: a PLP item whose feature is absent "
             "on this vehicle",
        proc=steps("Activate Driver Profile A and record the option list of "
                   "profile-linked preferences",
                   "Activate Driver Profile B, then activate Driver Profile A",
                   "Read the option list and check that the unavailable item "
                   "is neither stored nor recalled"),
        er=steps("Driver Profile A is active and the option list is recorded",
                 "Driver Profile A is active again",
                 "The unavailable item is absent from the list and no error "
                 "is raised for it"),
        remarks=PLP_COST + " 本條驗**略過**，故其受測列項為「該車不具備之功能」"
                "—— 其為配置相依，pre-condition 以能力而非以特定列項指定。",
        reasoning=(
            "驗證目標：4.1（PRACC1）末句 —— feature 於本車或本區域不可用時，"
            "略過該項之儲存與回復。"
            "關鍵情境條件：受測對象是「不存在之功能」，"
            "故 pre-condition 以**能力**描述而非指定某一列 —— "
            "指定列會使本 TC 只能在特定車上跑。"
            "為什麼這樣切：**ER 併驗「不報錯」** —— 只驗「該項不在」，"
            "一個略過該項但同時拋出錯誤之實作會通過，而條文說的是 ignore。"
            "刻意略過：可用項目之儲存與回復屬 `SWE1-HMI-PROF-001-01` 與 "
            "`SWE1-HMI-PROF-001-02`。"),
        kw=["unavailable feature", "skip", "PLP", "region"],
    ),

    # ── 4.1.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-002-01": dict(
        title="Restore Settings to Default affects only the active Profile",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist, each with a username and an "
                  "avatar",
                  "Both Profiles have at least one vehicle setting changed "
                  "from its default"),
        data="NA",
        proc=steps("Activate Driver Profile A and record its setting, "
                   "username and avatar",
                   "Select “Restore Settings to Default” and confirm it",
                   "Read Driver Profile A and check its setting, username "
                   "and avatar",
                   "Activate Driver Profile B and check that its setting is "
                   "unchanged"),
        er=steps("Driver Profile A is active and its values are recorded",
                 "The restore completes for Driver Profile A",
                 "The setting of Driver Profile A is back to default while "
                 "its username and avatar are unchanged",
                 "The setting of Driver Profile B is unchanged"),
        remarks="條文有三個斷言：只回復現用 profile、不重設全部 profile、"
                "不刪 username 與 avatar —— **三者為同一操作之三個結果**，"
                "依 §5.7 併為一條 TC。步驟 4 之 Profile B 即「不重設全部」之觀察點。",
        reasoning=(
            "驗證目標：4.1.1（PRACC1.2）—— 「Restore Settings to Default」"
            "只回復現用 profile 之設定，不重設其他 profile，且不刪 username 與 avatar。"
            "關鍵情境條件：pre-condition 要求**兩個** profile 皆有偏離預設之設定 ——"
            "**只有一個 profile 時，「不重設全部」無從觀察**。"
            "為什麼這樣切：三個斷言同屬一次操作之結果（§5.7）；"
            "**若只驗「A 回到預設」，一個把全部 profile 都重設之實作會通過**。"
            "刻意略過：回復過程之提示 popup 屬 `SWE1-HMI-PROF-002-02`。"),
        kw=["Restore Settings to Default", "active Profile", "username",
            "avatar"],
    ),

    "SWE1-HMI-PROF-002-02": dict(
        title="Progress popups shown during Restore Settings to Default",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile is active with at least one setting "
                  "changed from its default",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Select “Restore Settings to Default”",
                   "Press Yes on the confirmation popup and check that "
                   "PU1087 is displayed",
                   "Wait for the restore to end and check that PU1088 is "
                   "displayed"),
        # **U-1（31 包）**：ER3 原為 `PU1088 is displayed` —— 而 4.1.1 有**兩句**
        # 都指向 PU1088（成功回復／HU 或 TBM 未確認）。**同一個 popup，兩個分支。**
        # 本 leaf（`002-02`）之 description 為 `PU1088 shows when restore
        # completes`，其單位是**成功分支**；只驗 popup 顯示，
        # **一個根本沒回復成功、只是未確認而顯示 PU1088 之實作會通過**（§7）。
        # 併驗「該設定確已回到預設」以綁定成功分支 ——
        # pre-condition 已有「至少一項設定偏離預設」，該觀察點取得到。
        er=steps("The confirmation popup PU0118 is displayed",
                 "PU1087 is displayed",
                 "PU1088 is displayed and the setting under test is back to "
                 "its default value"),
        remarks="**本批唯一在上游素材未齊之情形下生成者（R-U27）**：DR #4 所缺為 "
                "`PU1087`／`PU1088` 之 popup **內文**，而其**觸發條件**已載於 "
                "spec（p6）。故本 TC 之 ER 只斷言該二 popup **顯示**，"
                "**不寫其上之文字** —— 不得以鄰近 PU id 推定內容（§8.4.1）。"
                "DR #4 到齊後，ER 得補其逐字內容。",
        reasoning=(
            "驗證目標：4.1.1 之後三句 —— 於 PU0118 按 Yes 後顯示 PU1087，"
            "回復完成後顯示 PU1088。"
            "關鍵情境條件：須有可回復之設定，否則流程不會被觸發。"
            "為什麼這樣切：本 leaf 之單位為**流程提示**，"
            "回復之實際效果屬 `SWE1-HMI-PROF-002-01`。"
            "**寫作限制（R-U27）**：popup 之內文未到齊，"
            "本 TC 只驗其顯示與時序，**不驗其文字** —— 已於 remarks 具名。"
            "刻意略過：條文另有「HU 或 TBM 未確認完成時亦顯示 PU1088」一句，"
            "其觸發為**異常路徑**，需注入未確認之情境（§12 之故障注入），"
            "與本條之正常路徑不同觸發（§5.7）。"
            "**該句由 `SWE1-HMI-PROF-002-03`（`NR1L-UserProfiles-002`）承擔** ——"
            "037 **確實為其切了 leaf**，且已生成。"
            "（原記「037 未為其另切 leaf，依 R-U56 為 OUT-OF-SCOPE」**係誤用**，"
            "38 包 Z-1 之全批自檢查出；**該句是有 leaf 的，不是範圍外**。）"),
        kw=["PU1087", "PU1088", "PU0118", "restore progress"],
    ),

    # ── 4.2 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-003": dict(
        title="Head unit usable without setting up a Profile",
        design=FUNCTIONAL,
        pre=steps("The vehicle is on its default Profile with no username or "
                  "avatar entered",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the Profile section and read the setup entry point",
                   "Leave the Profile section without entering a username or "
                   "an avatar",
                   "Operate Media and Climate and check that both respond "
                   "without a profile setup prompt"),
        er=steps("An entry point for entering a username and an avatar is "
                 "available",
                 "The Profile section is left with no setup performed",
                 "Media and Climate respond and no setup prompt blocks them"),
        remarks="條文之兩半（可設定／設定非必要）為同一節之正反兩面，"
                "**併為一條**：ER1 驗其可設定，ER3 驗其非必要。"
                "受測之兩個功能（Media、Climate）為**測試設置之選擇**（J-12），"
                "非條文所指定 —— 條文寫的是 use/interact with the head unit。",
        reasoning=(
            "驗證目標：4.2（PRACC2）—— 使用者**得**以 username 與 avatar 設定 profile，"
            "但設定**非**使用主機之前提。"
            "關鍵情境條件：pre-condition 明訂尚未輸入 username 與 avatar，"
            "否則「非必要」無從觀察。"
            "為什麼這樣切：**只驗「可設定」則條文之重點（非必要）未被測** ——"
            "而那一半才是會被實作漏掉的。"
            "來源標示：Media 與 Climate 為**測試設置**（J-12），非 spec 指定。"),
        kw=["optional setup", "username", "avatar", "head unit"],
    ),

    # ── 4.3 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-004-01": dict(
        title="Profile preferences remembered across a key cycle",
        design=STATE,
        pre=steps("A Driver Profile is active",
                  "The vehicle is stationary"),
        data="Preference under test: Cluster Home screen (3.1)",
        proc=steps("Set the preference under test to a new value and record it",
                   "Switch the ignition off and then on again",
                   "Read the preference and check that it matches the "
                   "recorded value"),
        er=steps("The preference accepts the new value and it is recorded",
                 "The ignition is off and then on again with the same "
                 "Driver Profile active",
                 "The preference matches the value recorded in step 1"),
        remarks="`key cycle` 之操作定義取 R-U21（設定 → key cycle → 讀回）——"
                "**其權威為裁決而非 spec**；4.3 之條文只寫 remembered over key "
                "cycles，未定義該循環之操作方式。",
        reasoning=(
            "驗證目標：4.3（PRACC3）之儲存側 —— 偏好跨 key cycle 保留。"
            "關鍵情境條件：**同一 profile 全程作用中** —— "
            "若中途切換 profile，測到的會是 4.3.1 之切換前儲存，不是跨 key cycle。"
            "為什麼這樣切：037 對 4.3 切四個 leaf，本 leaf（-01）之單位為"
            "**跨 key cycle 之保留**；三條回復途徑分屬 -02／-03／-04。"
            "來源標示：`key cycle` 之操作定義出自 **R-U21（裁決）**，非 spec（J-4）。"),
        kw=["key cycle", "preferences", "remembered", "PLP"],
    ),

    "SWE1-HMI-PROF-004-02": dict(
        title="Preferences restored when a Profile is chosen on the head unit",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each with a different value of "
                  "the preference under test",
                  "The vehicle is stationary"),
        data="Preference under test: Cluster Home screen (3.1)",
        proc=steps("Activate Driver Profile A and record the preference",
                   "Activate Driver Profile B from the “All Profiles” tab",
                   "Read the preference and check that it matches Driver "
                   "Profile B's own value"),
        er=steps("Driver Profile A is active and its preference is recorded",
                 "Driver Profile B is active",
                 "The preference matches Driver Profile B's own value and "
                 "differs from the value recorded in step 1"),
        remarks="三條回復途徑（主機選取／記憶座椅鍵／key fob）為 037 之三個 leaf，"
                "分屬 `SWE1-HMI-PROF-004-02`／`-03`／`-04`；"
                "本條為**主機選取**一途。",
        reasoning=(
            "驗證目標：4.3（PRACC3）之回復側，途徑為**自主機選取 profile**。"
            "關鍵情境條件：pre-condition 要求兩個 profile 之該偏好**值不同** ——"
            "值相同則「有回復」與「沒動過」無從分辨。"
            "為什麼這樣切：**ER3 併驗「與步驟 1 所記之值不同」** ——"
            "只驗「等於 B 之值」，一個根本不切換 profile 之實作若兩值恰同也會通過。"
            "刻意略過：另二途徑屬 `SWE1-HMI-PROF-004-03`（記憶座椅鍵）與 "
            "`SWE1-HMI-PROF-004-04`（key fob）。"),
        kw=["restore", "head unit selection", "profile switch", "PLP"],
    ),

    "SWE1-HMI-PROF-004-03": dict(
        title="Preferences restored when activated by a memory seat button",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each linked to a different "
                  "memory seat button",
                  "The two Profiles hold different values of the preference "
                  "under test"),
        data="Preference under test: Cluster Home screen (3.1)",
        proc=steps("Activate Driver Profile A and record the preference",
                   "Select memory seat button 2, which is linked to Driver "
                   "Profile B",
                   "Read the preference and check that it matches Driver "
                   "Profile B's own value"),
        er=steps("Driver Profile A is active and its preference is recorded",
                 "Driver Profile B is active",
                 "The preference matches Driver Profile B's own value and "
                 "differs from the value recorded in step 1"),
        remarks="記憶座椅鍵之編號（2）為**測試設置**（J-12），非條文指定 ——"
                "4.3 只寫 through memory seat buttons。"
                "座椅與 profile 之連結規則屬 4.5.1／9.5.x，本條以其為前提。",
        reasoning=(
            "驗證目標：4.3（PRACC3）之回復側，途徑為**記憶座椅鍵**。"
            "關鍵情境條件：兩 profile 各連一個座椅鍵且該偏好值不同，"
            "使切換之效果可觀察。"
            "為什麼這樣切：三途徑各為一 leaf；本條不代測另二者。"
            "來源標示：座椅鍵編號為測試設置（J-12），非 spec 指定。"),
        kw=["memory seat button", "restore", "profile switch", "PLP"],
    ),

    "SWE1-HMI-PROF-004-04": dict(
        title="Preferences restored when a Profile is detected by key fob",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each associated with a "
                  "different key fob",
                  "The two Profiles hold different values of the preference "
                  "under test"),
        data="Preference under test: Cluster Home screen (3.1)",
        proc=steps("Activate Driver Profile A and record the preference",
                   "Present the key fob associated with Driver Profile B",
                   "Read the preference and check that it matches Driver "
                   "Profile B's own value"),
        er=steps("Driver Profile A is active and its preference is recorded",
                 "Driver Profile B is active",
                 "The preference matches Driver Profile B's own value and "
                 "differs from the value recorded in step 1"),
        remarks="key fob 與 profile 之關聯機制 spec 未於本節詳述，"
                "本條以其為 pre-condition；**其建立方式不在本 TC 之範圍**。",
        reasoning=(
            "驗證目標：4.3（PRACC3）之回復側，途徑為 **key fob 偵測**。"
            "關鍵情境條件：兩 profile 各關聯一支 key fob 且偏好值不同。"
            "為什麼這樣切：三途徑各為一 leaf；本條不代測另二者。"
            "刻意略過：key fob 關聯之建立流程 spec 於本節未述，不推定（§8.4.1）。"),
        kw=["key fob", "detection", "restore", "PLP"],
    ),

    # ── 4.3.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-005": dict(
        title="Changed preferences saved before the next Profile loads",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each with a recorded value of "
                  "the preference under test",
                  "The two recorded values are different from each other"),
        data="Preference under test: Cluster Home screen (3.1)",
        proc=steps("Activate Driver Profile A and change the preference to a "
                   "new value, then record it",
                   "Activate Driver Profile B and read the preference",
                   "Activate Driver Profile A and check that the preference "
                   "matches the value recorded in step 1"),
        er=steps("Driver Profile A is active and the changed value is recorded",
                 "Driver Profile B is active and its preference is its own "
                 "value, not the value recorded in step 1",
                 "Driver Profile A is active and the preference matches the "
                 "value recorded in step 1"),
        remarks=PLP_COST + " **ER2 是順序之判別點**：若儲存發生在 Profile B "
                "載入**之後**，A 之變更會落到 B 上 —— ER2 即在排除該實作。"
                "ER3 單獨只能證「有存到」，證不了「存在載入之前」。",
        reasoning=(
            "驗證目標：4.3.1（PRACC3.1）—— 同一 key cycle 內切換 profile 時，"
            "已變更之偏好**在新 profile 載入之前**先行儲存。"
            "關鍵情境條件：兩 profile 之該偏好值不同，且步驟 1 之新值與 B 之值不同。"
            "為什麼這樣切：**條文之重點是「先後」，而先後不能只用「回來還在」證明** ——"
            "「A 回來還在」（ER3）與「存在載入之前」相容，也與「載入之後才存」相容。"
            "**能分開兩者的是 ER2**：若實作在 B 載入後才寫入，"
            "那筆變更會被寫進 B（或覆蓋 B 之值）；"
            "故 ER2 斷言 **B 顯示的是 B 自己的值，不是步驟 1 所記之值**。"
            "兩條 ER 併存才構成順序之斷言 —— 這是本條與 4.3 之 -01 的分野。"
            "來源標示：受測偏好取自 PLP 表 3.1（§8.4.1）。"),
        kw=["save before load", "profile switch", "key cycle", "ordering"],
    ),

    # ── 4.4 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-006-01": dict(
        title="Last known Profile loaded at the start of a key cycle",
        design=STATE,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "No key fob associated with another Profile is present and "
                  "no memory seat button is pressed at key-on"),
        data="NA",
        proc=steps("Activate Driver Profile B and record which Profile is "
                   "active",
                   "Switch the ignition off and then on again",
                   "Read the active Profile and check that it matches the "
                   "Profile recorded in step 1"),
        er=steps("Driver Profile B is active and is recorded as the last "
                 "known Profile",
                 "The ignition is off and then on again",
                 "Driver Profile B is active"),
        remarks="pre-condition 明列「無 key fob 偵測、未按記憶座椅鍵」——"
                "**該二者為條文所載之覆寫條件**，不排除則本條測不到預設路徑。"
                "覆寫側分屬 `SWE1-HMI-PROF-006-02`／`SWE1-HMI-PROF-006-03`。",
        reasoning=(
            "驗證目標：4.4（PRACC4）之預設路徑 —— 新 key cycle 起始載入上次之 profile。"
            "關鍵情境條件：**兩個覆寫條件皆須排除**（§8.7.3）；"
            "不排除則失敗時分不出是預設路徑壞了還是覆寫誤觸發。"
            "為什麼這樣切：037 對 4.4 切三個 leaf —— 預設路徑與兩個覆寫各一。"
            "刻意略過：覆寫由 `SWE1-HMI-PROF-006-02`（key fob）與 "
            "`SWE1-HMI-PROF-006-03`（記憶座椅鍵）承擔。"),
        kw=["key cycle", "last known Profile", "load", "key-on"],
    ),

    "SWE1-HMI-PROF-006-02": dict(
        title="Key fob detection overrides the last known Profile at key-on",
        design=STATE,
        pre=steps("Two Driver Profiles exist and Driver Profile B was the "
                  "last active one",
                  "A key fob associated with Driver Profile A is available"),
        data="NA",
        proc=steps("Switch the ignition off",
                   "Present the key fob for Driver Profile A and switch on",
                   "Read the active Profile and check that it is Driver "
                   "Profile A rather than the last known one"),
        er=steps("The ignition is off with Driver Profile B as the last "
                 "known Profile",
                 "The ignition is on and the key fob is detected",
                 "Driver Profile A is active"),
        remarks="§7 之列舉配對：正向為 `SWE1-HMI-PROF-006-01`（無覆寫則載入上次）。"
                "**兩條並存才擋得住一個永遠載入上次之實作**。",
        reasoning=(
            "驗證目標：4.4（PRACC4）之覆寫側，觸發為 **key fob 偵測**。"
            "關鍵情境條件：上次作用中之 profile 與 key fob 所指者**必須不同** ——"
            "相同則覆寫與否無從分辨。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-006-01` 構成 §7 之配對。"
            "刻意略過：記憶座椅鍵之覆寫屬 `SWE1-HMI-PROF-006-03`。"),
        kw=["key fob", "override", "key-on", "last known Profile"],
    ),

    "SWE1-HMI-PROF-006-03": dict(
        title="Memory seat button overrides the last known Profile at key-on",
        design=STATE,
        pre=steps("Two Driver Profiles exist and Driver Profile B was the "
                  "last active one",
                  "Driver Profile A is linked to memory seat button 1"),
        data="NA",
        # **V-1（32 包）之序列更正。** 原序列為「熄火 → 開機（**B 已載入**）→
        # 按座椅鍵」—— **覆寫在 ER1 那一刻就已經沒有發生**；
        # 其後所測到的是「按座椅鍵可切換 profile」，
        # 而那是 `SWE1-HMI-PROF-004-03`（`TC-086`）已覆蓋之行為。
        # 4.4 之覆寫發生點為 **key cycle 之起始**，故座椅鍵之操作
        # **不得晚於 key-on**。改為與 key-on 同時，比照同節之 `TC-090`（key fob）。
        proc=steps("Switch the ignition off",
                   "Select memory seat button 1 and switch the ignition on",
                   "Read the active Profile and check that it is Driver "
                   "Profile A rather than the last known one"),
        er=steps("The ignition is off with Driver Profile B as the last "
                 "known Profile",
                 "Memory seat button 1 is pressed and the ignition is on",
                 "Driver Profile A is the Profile loaded at key-on and "
                 "Driver Profile B is not loaded"),
        remarks="§7 之列舉配對：正向為 `SWE1-HMI-PROF-006-01`。"
                "座椅鍵編號（1）為**測試設置**（J-12）—— 4.4 只寫 memory seat buttons。"
                "**V-1（32 包）**：原序列先開機再按鍵，**B 已被載入，覆寫遂無從發生**；"
                "現要求座椅鍵之操作**不晚於 key-on**，ER3 斷言 A 為該 key cycle "
                "之**起始** profile，而非「B 載入後被切走」。"
                "**實車限制之聲明**：若該車之記憶座椅鍵僅能於 ignition on **之後**"
                "按下，則「A 為起始 profile」**在該車上不可觀察** —— "
                "屆時須回報該不可觀察性，**不得以「先開機再按」充當覆寫之驗證**"
                "（那正是本次所修正之形態）。"
                "本 TC **不假定**該鍵可於 key-on 前按，只要求其操作不晚於 key-on。",
        reasoning=(
            "驗證目標：4.4（PRACC4）之覆寫側，觸發為**記憶座椅鍵**。"
            "關鍵情境條件：上次作用中者與座椅鍵所連者不同。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-006-01` 構成 §7 之配對；"
            "與 `SWE1-HMI-PROF-006-02` 之差別在觸發來源，兩者不合併（§5.7）。"
            "來源標示：座椅鍵編號為測試設置（J-12）。"),
        kw=["memory seat button", "override", "key-on", "Profile"],
    ),

    # ── 4.5 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-007-01": dict(
        title="Default non-connected Profile present when none is set up",
        design=FUNCTIONAL,
        pre=steps("The vehicle has no custom Driver Profile set up",
                  "The vehicle has fewer than 2 memory seat buttons"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the Profile list and check that a default Profile "
                   "named “Driver 1” is present"),
        er=steps("The “All Profiles” tab is displayed",
                 "A default Profile named “Driver 1” is present and it is "
                 "not a connected Profile"),
        remarks="**ER2 併驗 non-connected** —— 條文寫的是 a default, "
                "non-connected profile；只驗「有一個叫 Driver 1 的 profile」，"
                "一個把它建成連網 profile 之實作會通過。"
                "座椅數之 pre-condition 為排除 4.5.1 之多預設情形。",
        reasoning=(
            "驗證目標：4.5（PRACC5）首句 —— 未設定任何自訂 profile 時，"
            "車上恆有一個預設、非連網之 profile，首次使用時名為 “Driver 1”。"
            "關鍵情境條件：座椅鍵少於 2 個 —— 否則 4.5.1 會使預設 profile 有多個，"
            "與本條之「單一預設」情境混淆。"
            "為什麼這樣切：037 對 4.5 切三個 leaf；本 leaf 之單位為**預設之存在**。"
            "刻意略過：刪除後之重建屬 `SWE1-HMI-PROF-007-02`；"
            "重建後之單一形態屬 `SWE1-HMI-PROF-007-03`。"),
        kw=["default Profile", "Driver 1", "non-connected", "first time use"],
    ),

    "SWE1-HMI-PROF-007-02": dict(
        title="Default Driver 1 recreated after all Profiles are deleted",
        design=FUNCTIONAL,
        pre=steps("The default Profile has been customized and its name is "
                  "still “Driver 1”",
                  "The vehicle has fewer than 2 memory seat buttons"),
        data="NA",
        proc=steps("Delete every Profile from the head unit",
                   "Open the “All Profiles” tab",
                   "Read the Profile list and check that a default “Driver "
                   "1” Profile is present again"),
        er=steps("Every Profile is deleted",
                 "The “All Profiles” tab is displayed",
                 "A default “Driver 1” Profile is present and its "
                 "preferences are at their default values"),
        remarks="**ER3 併驗「偏好為預設值」** —— 條文之 default 指的是"
                "**重建出一個預設 profile**，不是把原客製 profile 改名留下；"
                "只驗名稱，一個保留原客製內容之實作會通過。"
                "回復之範圍細節屬 `SWE1-HMI-PROF-012`（4.5.4）。",
        reasoning=(
            "驗證目標：4.5（PRACC5）第三句 —— 客製過之 Driver 1 於全部 profile "
            "被刪除後，預設 “Driver 1” 重新出現。"
            "關鍵情境條件：**pre-condition 明訂該預設曾被客製** ——"
            "條文特別寫 even if the name was maintained as Driver 1，"
            "即「名稱沒變」不等於「沒被客製」。"
            "為什麼這樣切：本 leaf 之單位為**重建**；"
            "重建後只有一個 profile 之形態屬 `SWE1-HMI-PROF-007-03`。"),
        kw=["delete all", "default Driver 1", "recreate", "customized"],
    ),

    "SWE1-HMI-PROF-007-03": dict(
        title="Recreated Driver 1 is the single Profile on the vehicle",
        design=FUNCTIONAL,
        # **W-1（33 包）**：pre-condition 原為 `Every Profile has been deleted`
        # —— **4.5 逐字載「全部刪除後系統恆有一個預設 profile」**，
        # 故測試開始那一刻該狀態**已經是假的**（Driver 1 早已被重建）。
        # 它描述了一個系統不允許存在之穩態，且其蘊含之結果（車上只剩 Driver 1）
        # **正是本 TC 要驗的東西** —— §4.4 禁止以受測特性為前提。
        # 刪除移入 procedure（比照 `SWE1-HMI-PROF-007-02`），
        # pre-condition 改述刪除**前**之狀態。
        pre=steps("The default Profile has been customized and its name is "
                  "still “Driver 1”",
                  "The vehicle has fewer than 2 memory seat buttons"),
        data="NA",
        proc=steps("Delete every Profile from the head unit",
                   "Open the “All Profiles” tab",
                   "Read the Profile list and check that “Driver 1” is the "
                   "only Profile present"),
        er=steps("Every Profile is deleted",
                 "The “All Profiles” tab is displayed",
                 "“Driver 1” is present and no other Driver Profile is "
                 "listed"),
        remarks="條文之 `(unless there are 2 or more memory seat buttons)` "
                "為**適用條件**，以 pre-condition 固定為少於 2 個；"
                "座椅鍵 ≥ 2 之情形由 `SWE1-HMI-PROF-008`（4.5.1）承擔。"
                "**W-1（33 包）**：刪除動作原置於 pre-condition，"
                "而 4.5 明載全部刪除後**系統立即重建預設** —— "
                "該前提所述之穩態不存在，且其蘊含之結果即本條之 ER。"
                "已移入 procedure（比照 `SWE1-HMI-PROF-007-02`）。"
                "**與該 leaf 之分野不變**：`007-02` 驗**重建發生**"
                "（且其偏好為預設值），本條驗**重建後只有一個**。",
        reasoning=(
            "驗證目標：4.5（PRACC5）第三句之後半 —— 重建之 “Driver 1” 為車上"
            "**唯一**之 profile。"
            "關鍵情境條件：條文自帶之例外（座椅鍵 ≥ 2）以 pre-condition 排除，"
            "使「唯一」之斷言成立。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-007-02` 之分野在斷言對象 ——"
            "-02 驗**重建發生**，本條驗**重建後只有一個**。"
            "**ER2 為缺席斷言（無其他 profile）**，"
            "只驗 Driver 1 在，一個留下殘餘 profile 之實作會通過。"),
        kw=["single Profile", "Driver 1", "memory seat buttons", "default"],
    ),

    # ── 4.5.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-008": dict(
        title="One default Profile per memory seat button",
        design=FUNCTIONAL,
        pre=steps("The vehicle has 2 memory seat buttons",
                  "No custom Driver Profile is set up on the vehicle"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the seat links and check that each button has "
                   "its own default Profile"),
        er=steps("The “All Profiles” tab is displayed",
                 "Two default Profiles are present: “Driver 1” linked to "
                 "memory seat button 1 and “Driver 2” linked to memory seat "
                 "button 2"),
        remarks="條文以「2 個座椅鍵」為例（e.g.），本 TC 以其為 pre-condition ——"
                "**該數字取自條文之例，非自擬**。座椅鍵 ≥ 3 之情形條文未述，"
                "依 §8.4.1 不推定。",
        reasoning=(
            "驗證目標：4.5.1（PRACC5.1）—— 有記憶座椅鍵時，每個座椅位置各有"
            "一個預設 Driver Profile。"
            "關鍵情境條件：座椅鍵數以條文之例（2）固定，"
            "且無自訂 profile —— 否則預設之數目會被自訂者干擾。"
            "為什麼這樣切：**ER 逐一指名兩個連結**（Driver 1 ↔ 鍵 1、Driver 2 ↔ 鍵 2）；"
            "只驗「有兩個預設 profile」，一個把兩者都連到同一鍵之實作會通過。"
            "刻意略過：座椅鍵三個以上之情形條文未述（§8.4.1 保留）。"),
        kw=["memory seat button", "default Profile", "Driver 2", "link"],
    ),

    # ── 4.5.2 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-009": dict(
        title="Memory seat preferences swapped between Driver Profiles",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each linked to its own memory "
                  "seat position",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read and record which Profile is linked to each memory "
                   "seat position",
                   "Swap the memory seat preferences between the two Profiles",
                   "Read the links and check that each Profile now holds the "
                   "other's seat position"),
        er=steps("The two Profile-to-seat links are recorded",
                 "The swap is accepted",
                 "Each Profile is linked to the seat position recorded for "
                 "the other Profile in step 1"),
        remarks="§7 之列舉配對：反向為 `NR1L-UserProfiles-105`（同一座椅位置"
                "不得連上第二個 profile）。條文之後半「**永遠只有一個** Driver "
                "Profile per memory seat position」為全稱，"
                "**只驗互換成功不足以證之** —— 故另立反向。",
        reasoning=(
            "驗證目標：4.5.2（PRACC5.2）前半 —— 記憶座椅偏好可於 profile 間互換。"
            "關鍵情境條件：兩 profile 各有其座椅位置，互換之效果方可觀察。"
            "為什麼這樣切：條文有兩個斷言（可互換／每位置恆只有一個），"
            "**後者為全稱且為限制**，其失效形態與前者相反 ——"
            "併於一條則失敗時分不出是哪一個沒生效（§7）。"
            "反向由 `NR1L-UserProfiles-105` 承擔"
            "（**36 包自檢更正：原寫 `104`，而 `104` 是 4.6.3 之 `016`，"
            "與本條無關 —— tc_id 於寫 remarks 時尚未指派**）。"),
        kw=["swap", "memory seat", "Driver Profile", "link"],
    ),

    # ── 4.5.3 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-010-01": dict(
        title="Memory seat reassigned to the next available Profile on delete",
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist and only one of them is "
                  "linked to a memory seat position",
                  "The two unlinked Profiles are ordered left to right on "
                  "the “All Profiles” tab"),
        data="NA",
        proc=steps("Read and record the order of the unlinked Profiles",
                   "Delete the Profile linked to the memory seat position",
                   "Read the seat link and check that it moved to the "
                   "leftmost unlinked Profile"),
        er=steps("The order of the unlinked Profiles is recorded",
                 "The linked Profile is deleted",
                 "The memory seat position is linked to the leftmost "
                 "unlinked Profile recorded in step 1"),
        remarks="條文之優先順序為 prioritizing from left to right based on the "
                "order of the Profiles on the All Profiles Tab —— "
                "**ER 指名「最左」而非「任一」**：只驗「改派給某個 profile」，"
                "一個隨機挑選之實作會通過。",
        reasoning=(
            "驗證目標：4.5.3（PRACC5.3）前半 —— 刪除已連座椅之 profile 時，"
            "該座椅自動改派給下一個可用 profile，順序由左至右。"
            "關鍵情境條件：**須有兩個以上未連座椅之 profile** ——"
            "只有一個時，「由左至右」之優先順序無從觀察。"
            "為什麼這樣切：本 leaf 之單位為**有可用 profile 時之改派**；"
            "無可用 profile 之情形屬 `SWE1-HMI-PROF-010-02`。"),
        kw=["reassign", "memory seat", "delete", "left to right"],
    ),

    "SWE1-HMI-PROF-010-02": dict(
        title="Default Profile created when no Profile can take the seat",
        design=FUNCTIONAL,
        pre=steps("One Driver Profile exists and it is linked to a memory "
                  "seat position",
                  "No other Driver Profile is available on the vehicle"),
        data="NA",
        proc=steps("Delete the Profile linked to the memory seat position",
                   "Open the “All Profiles” tab",
                   "Read the Profile list and check that a default Profile "
                   "for that seat position is present"),
        er=steps("The linked Profile is deleted",
                 "The “All Profiles” tab is displayed",
                 "A default Profile associated with that seat position is "
                 "present"),
        remarks="§7 之列舉配對：正向為 `SWE1-HMI-PROF-010-01`（有可用 profile 則改派）。"
                "兩條之 pre-condition 互斥（有／無其他可用 profile），不重複覆蓋。",
        reasoning=(
            "驗證目標：4.5.3（PRACC5.3）後半 —— 無可用 profile 可連該座椅位置時，"
            "系統自動建立或回復一個與該位置關聯之預設 profile。"
            "關鍵情境條件：**車上只有一個 profile 且已連座椅** ——"
            "此為使條件成立之最小情境。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-010-01` 構成 §7 之配對，"
            "兩者之 pre-condition 互斥。"),
        kw=["default Profile", "auto create", "memory seat", "delete"],
    ),

    # ── 4.5.3.1 ───────────────────────────────────────────────────────
    "SWE1-HMI-PROF-011": dict(
        title="Newly assigned Profile becomes active after the linked one is deleted",
        design=STATE,
        pre=steps("Two Driver Profiles exist and Driver Profile A is linked "
                  "to the current memory seat position",
                  "Driver Profile A is the active Profile"),
        data="NA",
        proc=steps("Delete Driver Profile A",
                   "Read and record which Profile now holds the seat "
                   "position",
                   "Read the active Profile and check that it is the Profile "
                   "recorded in step 2"),
        er=steps("Driver Profile A is deleted",
                 "The current seat position is now linked to Driver Profile B",
                 "Driver Profile B is the active Profile"),
        remarks="本條與 `SWE1-HMI-PROF-010-01` 之分野：後者驗**座椅改派給誰**，"
                "本條驗**改派後誰成為現用 profile** —— 同一觸發之兩個結果，"
                "037 切為兩個 leaf（4.5.3 與 4.5.3.1），故不合併。",
        reasoning=(
            "驗證目標：4.5.3.1（PRACC5.3.1）—— 已連座椅之 profile 被刪除後，"
            "新現用 profile 為現在被指派到該座椅位置者。"
            "關鍵情境條件：被刪者須**同時是現用 profile 且連著現在的座椅位置** ——"
            "否則「新現用 profile」之判定與本條無關。"
            "為什麼這樣切：步驟 2 先讀出改派結果再於步驟 3 比對現用者，"
            "**使本條不依賴 `SWE1-HMI-PROF-010-01` 之改派規則是否正確** ——"
            "改派給誰由那條驗，本條只驗「改派給誰，誰就變成現用」。"),
        kw=["active Profile", "delete", "seat position", "reassign"],
    ),

    # ── 4.5.4 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-012": dict(
        title="All linked preferences reset when default Profiles are restored",
        design=FUNCTIONAL,
        # 出處對照（28 輪）抓到：`“Driver 2”` 溯不到 4.5.4 —— 該節寫的是
        # `default **Driver 1-2** Profiles`，`Driver 2` 單獨出現在 4.5.1。
        # **G18 只掃 ER，掃不到 pre_conditions**，故此處靠出處對照才發現。
        # 改用本節自己的寫法，不另引 4.5.1（那會是多引，G17）。
        pre=steps("The vehicle has 2 memory seat buttons with the default "
                  "“Driver 1-2” Profiles",
                  "Both default Profiles have several profile-linked "
                  "preferences changed from their defaults"),
        data="Preferences under test: Cluster Home screen (3.1), "
             "SiriusXM 360L Listener Profile (3.2), "
             "Nav Saved destinations (3.4)",
        proc=steps("Record the changed values of the three preferences for "
                   "both default Profiles",
                   "Restore the default Driver Profiles",
                   "Read the three preferences for both Profiles and check "
                   "that each is at its default value"),
        er=steps("The changed values are recorded for both default Profiles",
                 "The default Profiles are restored",
                 "The three preferences of both Profiles are at their "
                 "default values and none holds a value recorded in step 1"),
        remarks=PLP_COST + " 條文之 as if the vehicle was just purchased "
                "為**程度描述**，本 TC 以「三項 PLP 偏好皆回到預設值」為其"
                "可觀察之形式；**未宣稱已驗盡全部 PLP 列項**。",
        reasoning=(
            "驗證目標：4.5.4（PRACC5.4）—— 預設 Driver 1–2 profile 被回復時，"
            "所有 profile-linked 偏好回到預設狀態。"
            "關鍵情境條件：**兩個預設 profile 皆須有偏離預設之值** ——"
            "否則「回到預設」與「本來就是預設」無從分辨。"
            "為什麼這樣切：**ER3 併驗「無一項仍持步驟 1 所記之值」** ——"
            "只驗「等於預設值」，一個把預設值也改掉之實作可能仍通過。"
            "**代價聲明**：本條驗三項 PLP 列項，**非全部** ——"
            "全稱以單例驗證之限制見 D-UP16-02，其分母不得以引用欄推定（J-1）。"),
        kw=["restore defaults", "PLP", "Driver 1", "Driver 2"],
    ),

    # ── 4.6 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-013": dict(
        title="Profile button present in the status bar by default",
        design=FUNCTIONAL,
        pre=steps("The status bar is at its default configuration",
                  "Two Driver Profiles exist with different avatars"),
        data="NA",
        # **T-1（30 包）**：步驟 1 原為 `check that a Profile button is present`
        # —— 它只查按鈕在不在，**沒有讀也沒有記錄圖示**，
        # 而 ER3 卻以「步驟 1 所讀之圖示」為比較基準。**該基準不存在。**
        # §5.6：記錄步驟與比較步驟須成對。改為記錄式（同批 `103` 之作法）。
        proc=steps("Read the status bar and record the Profile button icon",
                   "Activate the other Driver Profile",
                   "Read the status bar button and check that its icon "
                   "changed with the active Profile"),
        er=steps("A Profile button is present in the status bar and its icon "
                 "is recorded",
                 "The other Driver Profile is active",
                 "The Profile button icon differs from the icon recorded in "
                 "step 1"),
        remarks="條文之括號句（狀態列可被客製以移除該按鈕）為**另一觸發**，"
                "其行為由 `SWE1-HMI-PROF-016`（4.6.3）承擔；本條驗預設狀態。"
                "圖示之**內容**（avatar／首字母）屬 `SWE1-HMI-PROF-014`（4.6.1）。",
        reasoning=(
            "驗證目標：4.6（PRACC6）—— Profile 按鈕預設存在於狀態列，"
            "且其圖示隨作用中之 profile 改變。"
            "關鍵情境條件：兩 profile 之 avatar 不同，否則「圖示改變」無從觀察。"
            "為什麼這樣切：兩個斷言（預設存在／圖示隨 profile 變）為同一節之"
            "兩個結果，依 §5.7 併為一條之兩段。"
            "**ER3 以「與步驟 1 所讀不同」表述** —— 圖示之具體內容屬 4.6.1，"
            "本條只斷言其**改變**。"),
        kw=["status bar", "Profile button", "icon", "default"],
    ),

    "SWE1-HMI-PROF-014": dict(
        title="Profile button icon shows the active customized Profile",
        design=FUNCTIONAL,
        pre=steps("A customized Driver Profile is active",
                  "The avatar of that Profile is a plain colour with no "
                  "picture"),
        data="NA",
        proc=steps("Read the status bar Profile button",
                   "Read the button icon and check that it carries the first "
                   "character of the username"),
        er=steps("The status bar Profile button is displayed",
                 "The button icon shows the coloured circle with the first "
                 "character of the username in its centre"),
        remarks="條文有兩種 avatar 形態（圖像／純色）；**本 TC 取純色一側**，"
                "因其斷言最具體（首字母置中）。圖像 avatar 之情形條文只寫 "
                "with avatar，未另述其呈現，依 §8.4.1 不推定，故不另立 TC。",
        reasoning=(
            "驗證目標：4.6.1（PRACC6.1）—— 客製 profile 作用中時，"
            "狀態列按鈕圖示指出登入者；avatar 為純色時，"
            "username 之首字元顯示於色圈中央。"
            "關鍵情境條件：**avatar 須為純色** —— 那是條文唯一給出具體呈現之分支。"
            "為什麼這樣切：**取條文最具體之一側** ——"
            "圖像 avatar 之呈現條文未述，寫進 ER 會是推定（§8.4.1）。"
            "刻意略過：按鈕之存在與圖示會變屬 `SWE1-HMI-PROF-013`。"),
        kw=["avatar", "first character", "coloured circle", "icon"],
    ),

    "SWE1-HMI-PROF-015": dict(
        title="Profile button highlighted while the Profile section is open",
        # **design_method 改過一次（K-4a 首跑轉紅）。**
        # 初判為狀態轉換（區段關閉 → 開啟）。複核後改**功能測試**：
        # 本條之受測對象是**按鈕之 highlight 呈現**，其隨區段開闔而變 ——
        # 那是**條件式呈現**，不是系統狀態機之遷移。
        # 與 `SWE1-HMI-PROF-011`（現用 profile 由 A 變 B）對照即明：
        # 後者變的是**持續存在之系統狀態**，本條變的是畫面上的一個樣式。
        # 沿 P-1 之同一分野（§8.7.4：視覺狀態不等於機制）。
        design=FUNCTIONAL,
        pre=steps("The status bar is at its default configuration",
                  "The Profile section is closed"),
        data="NA",
        proc=steps("Read the status bar Profile button and record its state",
                   "Open the Profile section",
                   "Read the Profile button and check that it is in the "
                   "active state"),
        er=steps("The Profile button state is recorded",
                 "The Profile section is open",
                 "The Profile button is highlighted"),
        remarks="以關閉狀態為基準線（§5.6）—— 只讀開啟後之狀態，"
                "一個永遠 highlight 之實作會通過。",
        reasoning=(
            "驗證目標：4.6.2（PRACC6.2）—— Profile 區開啟時，按鈕為 active "
            "（highlighted）狀態。"
            "關鍵情境條件：pre-condition 明訂 Profile 區起始為關閉，"
            "使開啟前後之對照成立。"
            "為什麼這樣切：**步驟 1 之基準線是必要的** ——"
            "無基準線則「highlight」與「本來就 highlight」無從分辨（§5.6）。"
            "刻意略過：按鈕被移除後之 highlight 屬 `SWE1-HMI-PROF-016`。"),
        kw=["highlight", "active state", "Profile section", "status bar"],
    ),

    "SWE1-HMI-PROF-016": dict(
        title="Highlight states kept after the Profile button is removed",
        design=FUNCTIONAL,
        pre=steps("The Profile button has been removed from the status bar "
                  "through status bar customization",
                  "The Profile section is closed"),
        data="NA",
        proc=steps("Open the status bar edit mode drawer and record its "
                   "state",
                   "Open the Profile section from the app drawer",
                   "Read the Profile button in both the edit mode drawer and "
                   "the app drawer and check its highlight"),
        # **U-2（31 包）**：步驟 1 記錄了按鈕狀態，而原 ER **從未引用它** ——
        # 判為 **ER 漏斷言**，非多餘步驟：該記錄是 §5.6 之基準線，
        # **缺了它，一個「永遠 highlight」之實作會通過**（同 `103` 之理由）。
        er=steps("The Profile button is shown in the status bar edit mode "
                 "drawer and its highlight state is recorded",
                 "The Profile section is open",
                 "The Profile button is highlighted in the status bar edit "
                 "mode drawer and in the app drawer, differing from the "
                 "state recorded in step 1"),
        remarks="條文指名**兩個**位置（status bar edit mode drawer 與 app drawer），"
                "故 ER3 兩處併驗 —— 只驗其一，另一處失效不會被發現。"
                "**U-2（31 包）**：步驟 1 之記錄原無任一 ER 引用，"
                "已於 ER1 補其記錄、ER3 補其比對 —— **基準線與比較須成對**（§5.6）。",
        reasoning=(
            "驗證目標：4.6.3（PRACC6.3）—— Profile 按鈕自狀態列移除後，"
            "其 highlight 狀態仍適用於 status bar edit mode drawer 與 app drawer。"
            "關鍵情境條件：**按鈕須先被移除**（§8.7.3），否則本條與 4.6.2 同情境。"
            "為什麼這樣切：條文指名兩個位置，ER 逐一斷言。"
            "刻意略過：狀態列客製化之操作流程屬他 feature（Home），本條以其結果為前提。"),
        kw=["removed", "edit mode drawer", "app drawer", "highlight"],
    ),
}

# ── 附加條目（非 037 之新 leaf，或掛在既有 leaf 之下）────────────────
EXTRAS = [
    # 105 —— 4.5.2 之反向配對（§7；25 包 §B.2.2 具名須額外造）
    dict(
        suffix="neg",
        req_id="SWE1-HMI-PROF-009",
        prio=("P1", "同一座椅位置不得連上第二個 profile —— 全稱限制之反向"),
        spec=dict(
            title="Second Profile refused on an occupied memory seat position",
            design=NEGATIVE,
            pre=steps("Two Driver Profiles exist and Driver Profile A is "
                      "linked to memory seat position 1",
                      "Driver Profile B is linked to another seat position"),
            data="NA",
            proc=steps("Read and record which Profile holds memory seat "
                       "position 1",
                       "Attempt to link Driver Profile B to memory seat "
                       "position 1 as well",
                       "Read the seat links and check that position 1 still "
                       "holds exactly one Profile"),
            er=steps("Memory seat position 1 is recorded as linked to Driver "
                     "Profile A",
                     "The attempt is not accepted as an additional link",
                     "Memory seat position 1 is linked to exactly one Driver "
                     "Profile"),
            remarks="§7 之列舉配對：正向為 `NR1L-UserProfiles-096`"
                    "（`SWE1-HMI-PROF-009`，互換成功）。"
                    "條文之「**there will always be one** Driver Profile per "
                    "memory seat position」為全稱限制 —— "
                    "**只驗互換成功不足以證之**，故另立本條。"
                    "座椅位置編號（1）為測試設置（J-12）。",
            reasoning=(
                "驗證目標：4.5.2（PRACC5.2）後半之全稱限制 ——"
                "每個記憶座椅位置**恆只有一個** Driver Profile。"
                "關鍵情境條件：該位置已被 A 佔用，B 另有其位 ——"
                "使「再連一個」成為明確之非法操作。"
                "為什麼這樣切：**全稱之限制只能以反向證之** ——"
                "正向（互換成功）與「允許一位置連兩個」相容，"
                "故 `SWE1-HMI-PROF-009` 之正向不足以擋下該實作（§7）。"
                "**ER3 斷言「恰好一個」而非「B 沒連上」** ——"
                "後者容許實作把 A 踢掉再連 B，那同樣違反條文。"),
            kw=["memory seat position", "single Profile", "refused",
                "always one"],
        ),
    ),
    # 106 —— A-UP13 行為 1：6.2.1 之後半（掛既有 leaf，非新 leaf）
    dict(
        suffix="del",
        req_id="SWE1-HMI-PROF-048",
        prio=("P1", "預設 profile 於客製或刪除後之消失 —— 預設之生命週期"),
        spec=dict(
            title="Default Profile no longer default after it is customized",
            design=STATE,
            pre=steps("The vehicle is on its default Profiles with no custom "
                      "Profile set up",
                      "The vehicle is stationary"),
            data="NA",
            proc=steps("Open the “All Profiles” tab and record the default "
                       "Profiles present",
                       "Customize one default Profile with a username and "
                       "an avatar",
                       "Read the Profile list and check that the customized "
                       "one is no longer listed as a default"),
            er=steps("The default Profiles present are recorded",
                     "The chosen Profile carries the entered username and "
                     "avatar",
                     "The customized Profile is no longer a default Profile "
                     "while the other recorded defaults remain"),
            remarks="**A-UP13 行為 1（23 包 M-2 掃出，25 包定歸屬）**："
                    "6.2.1 之條文為 `Driver 1 and any other default Profiles "
                    "will remain on the vehicle **until a user customizes or "
                    "deletes it**`，而 `NR1L-UserProfiles-005` 只驗其前半"
                    "（未客製化前仍在）。本條驗其後半 —— **兩條同一 leaf**。"
                    "**不得與 `SWE1-HMI-PROF-007-02`（4.5）混淆**："
                    "該 leaf 驗「刪除全部後 Driver 1 重建」，"
                    "本條驗「客製後該 profile 不再是預設」—— 兩件事。",
            reasoning=(
                "驗證目標：6.2.1（NOPR1.1）之後半 —— 預設 profile 留在車上，"
                "**直到使用者將其客製化或刪除**。"
                "關鍵情境條件：起始須為純預設狀態，"
                "且**保留另一個未被客製之預設**作為對照（ER3 之後半）。"
                "為什麼這樣切：**ER3 併驗「其餘預設仍在」** ——"
                "只驗「被客製者不再是預設」，一個把全部預設都清掉之實作會通過。"
                "本條與 `NR1L-UserProfiles-005` 同屬 `SWE1-HMI-PROF-048`，"
                "分驗該 description 之前後兩半。"),
            kw=["default Profile", "customize", "no longer default",
                "remain"],
        ),
    ),
    # 107 —— A-UP13 行為 2：7.2.1 之 More Options（新 leaf）
    dict(
        suffix=None,
        req_id="SWE1-HMI-PROF-059-02",
        prio=("P2", "自 welcome popup 進入 Edit Profile 之導向；呈現層之入口"),
        spec=dict(
            title="More Options on the welcome popup opens the Edit Profile tab",
            design=FUNCTIONAL,
            pre=steps("The large welcome popup is displayed for the active "
                      "Driver Profile",
                      "The vehicle is stationary"),
            data="NA",
            proc=steps("Press “More Options” on the large welcome popup",
                       "Read the screen and check that the “Edit Profile” "
                       "tab of the active Profile is displayed"),
            er=steps("The “More Options” button is pressed",
                     "The “Edit Profile” tab of the active Driver Profile is "
                     "displayed"),
            remarks="**A-UP13 行為 2**：23 輪記為「無人覆蓋」，"
                    "25 輪查 037 後更正 —— 本行為有專屬 leaf "
                    "（`SWE1-HMI-PROF-059-02`），當時只是尚未取樣。"
                    "**ER2 併驗「現用 profile 之」分頁** —— "
                    "只驗「Edit Profile 開了」，一個開到別的 profile 之實作會通過。",
            reasoning=(
                "驗證目標：7.2.1（PRWEL2.1）之 `Choosing "
                "“More Options” will take user to Edit Profile tab`。"
                "關鍵情境條件：須為**大型** welcome popup —— "
                "小型 popup（7.2）無此按鈕。"
                "為什麼這樣切：037 對 7.2.1 切三個 leaf，"
                "本 leaf 之單位即此一導向；popup 之內容屬 "
                "`SWE1-HMI-PROF-059-01`（`NR1L-UserProfiles-007`）。"),
            kw=["More Options", "Edit Profile", "welcome popup", "navigate"],
        ),
    ),
    # 108 —— A-UP13 行為 3：7.2.1 之切換後新 popup（新 leaf）
    dict(
        suffix=None,
        req_id="SWE1-HMI-PROF-059-03",
        prio=("P1", "自 welcome popup 切換 profile 並顯示新 popup —— 切換路徑之一"),
        spec=dict(
            title="Selecting another Profile switches and shows its welcome popup",
            design=STATE,
            # **37 包作業 4**：ER3 之 `applicable welcome popup` 是否出現，
            # 取決於 5.3.1 之 `(if turned on for that Profile)` ——
            # 未指定則結果不可重現（§2），故固定為「已開啟」。
            pre=steps("The large welcome popup is displayed for Driver "
                      "Profile A and lists Driver Profile B",
                      "The welcome popup is turned on for Driver Profile B",
                      "The vehicle is stationary"),
            data="NA",
            proc=steps("Read and record the active Profile shown on the "
                       "large welcome popup",
                       "Select Driver Profile B from the list on the popup",
                       "Read the screen and check that Driver Profile B is "
                       "active with its own welcome popup"),
            er=steps("Driver Profile A is recorded as the active Profile",
                     "Driver Profile B is selected",
                     "Driver Profile B is the active Profile and the "
                     "applicable welcome popup for it is displayed"),
            remarks="**A-UP13 行為 3**：同行為 2，有專屬 leaf "
                    "（`SWE1-HMI-PROF-059-03`）而尚未取樣，25 輪更正記載。"
                    "**ER3 併驗「切換」與「新 popup」兩者** —— "
                    "只驗 popup 換了，一個顯示 B 之 popup 卻未真正切換之實作會通過。"
                    "popup 之尺寸取決於 7.2／7.2.1 之條件，"
                    "故 ER 寫 the applicable welcome popup，不指定大小。",
            reasoning=(
                "驗證目標：7.2.1（PRWEL2.1）之 `If a different Profile is "
                "selected, show the applicable welcome popup for the new "
                "active profile`。"
                "關鍵情境條件：popup 須列出另一個 profile，否則選取無從發生。"
                "為什麼這樣切：**條文之 applicable 指其形態由別處決定** ——"
                "ER 照錄該不確定性，不推定為大型或小型（§8.4.1）。"
                "刻意略過：welcome popup 之尺寸判準屬 7.2／7.2.1 之其他斷言。"),
            kw=["switch Profile", "welcome popup", "applicable", "select"],
        ),
    ),
]


def build() -> list:
    rows = B.leaf_rows()
    missing = [r for r in SAMPLE if r not in TCS]
    if missing:
        raise SystemExit(f"取樣清單與內容不一致，TSV 有而 TCS 無：{missing}")
    extra = [r for r in TCS if r not in SAMPLE]
    if extra:
        raise SystemExit(f"TCS 有而取樣清單無：{extra}")

    out, n = [], TC_START
    for req_id in SAMPLE:
        ctx = B.assemble(req_id, rows[req_id])
        spec = TCS[req_id]
        prio, why = PRIORITY[req_id]
        rec = _rec(req_id, ctx, spec, ctx["specification_reference"],
                   prio, why, n)
        rec["batch"] = "batch03"
        out.append(rec)
        n += 1

    for item in EXTRAS:
        rid = item["req_id"]
        ctx = B.assemble(rid, rows[rid])
        rec = _rec(rid, ctx, item["spec"], ctx["specification_reference"],
                   *item["prio"], n)
        rec["batch"] = "batch03"
        if item["suffix"]:
            rec["parent"] = f"{rid}-{item['suffix']}"
            rec["note"] = (
                f"與 `{rid}` 同一 leaf，**非新 leaf**；"
                f"檔名加 `-{item['suffix']}` 以免覆寫該 leaf 之既有產物")
        out.append(rec)
        n += 1
    return out


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    recs = build()
    for r in recs:
        (OUT / f"{r['parent']}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"寫出 {len(recs)} 個檔，共 {sum(len(r['tcs']) for r in recs)} 條 TC "
          f"（{recs[0]['tcs'][0]['tc_id']} … {recs[-1]['tcs'][0]['tc_id']}）")
