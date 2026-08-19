#!/usr/bin/env python3
"""第五批之生成器（40 包）—— ch5 之 `ALLPR` 群（5.12–5.16）＋ ch6 `NOPR`
（6.1–6.6），tc_id 135–156。

## 批界（40 包 §一，分析層自裁）

**第五批 ＝ 5.12–5.16 之 13 leaf ＋ ch6 Defaults 之 9 leaf ＝ 22 leaf。**

ch6 僅 9 leaf，單獨成批會多兩個往返；其條款家族線（`ALLPR` / `NOPR`）
於批內仍逐節具名，故併批不使批界失去意義。

## 條數：**22 條，額外造者 0**（下放包估 ≈24）

差額 2 條之來源，逐條具名：

1. **`041-04` 不是額外造者。** 38／40 兩包皆寫「22 leaf ＋ `041-04` 失敗路徑」，
   而 `041-04`（PU1091）**本身就是 037 之一個 leaf**，已計入 22 之內。
   該措辭承自我 29 輪之錯誤並列，34 輪已更正過一次（見 `gen_batch04` 檔頭），
   此處是同一個錯誤的第二次出現 —— **本批不再沿用**。
2. **`042` 之「不得啟用該 profile」不另立一條。** 條文之
   `(and will not result in that Profile being activated)` 與拖曳為
   **同一句之兩個斷言**，依 §5.7 併驗於同一條之 ER4；
   另立則兩條之 procedure 逐字相同，只 ER 差一行。

## 三項必含（比照前例）

| 項 | 本批之落點 |
|---|---|
| **反向／負向** | `045`（B profile 無 cloud icon 之對照）、`051`（B profile 之 popup 仍顯示）、`050-02`（不出現二次 popup） |
| **邊界／壓力** | `044`（過長 username 之截斷）、`042`（三個 profile 方能觀察順序位移） |
| **故障注入** | `041-04`（HU／TBM 不回報完成 → PU1091），`design_method` 為基礎故障注入 |

## 撰寫時已知之限制（生成前即具名）

- `044`：截斷規則在外部文件（Core HMI Logic and Flow），本 spec 未載 ——
  ER 只斷言「有截斷且依該文件」，**不自擬規則**（§8.4.1）
- `041-03`／`041-04`：PU1089／1090／1091 之**內文**未見於 spec ——
  只斷言其顯示與時機（R-U27 同型）
- `045`：其 label 依 RD #5 之答覆可能調整（39 包作業 2 之兩處命中之一）
- `037`：`(Ex: mem seat 1 + Driver 1)` 之編號出自條文本身，非測試設置
- `046`：`r1h-cpa-6.1` 之 R1 High 側；base 側於 037 無 leaf，
  依 R-U56 不造 —— 已於 `audit_variant_pairs.AXES` 由 `pending` 改為具名不配
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE,       # noqa: E402
                       NEGATIVE, SCENARIO, FAULT)
from gen_batch01 import _rec                           # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
TC_START = 135

SAMPLE = [
    # ── ch5 / ALLPR（5.12–5.16）
    "SWE1-HMI-PROF-036", "SWE1-HMI-PROF-037", "SWE1-HMI-PROF-038",
    "SWE1-HMI-PROF-039", "SWE1-HMI-PROF-040",
    "SWE1-HMI-PROF-041-01", "SWE1-HMI-PROF-041-02",
    "SWE1-HMI-PROF-041-03", "SWE1-HMI-PROF-041-04",
    "SWE1-HMI-PROF-042", "SWE1-HMI-PROF-043", "SWE1-HMI-PROF-044",
    "SWE1-HMI-PROF-045",
    # ── ch6 / NOPR（6.1–6.6）
    "SWE1-HMI-PROF-046", "SWE1-HMI-PROF-047", "SWE1-HMI-PROF-049",
    "SWE1-HMI-PROF-050-01", "SWE1-HMI-PROF-050-02",
    "SWE1-HMI-PROF-051", "SWE1-HMI-PROF-052",
    "SWE1-HMI-PROF-054", "SWE1-HMI-PROF-055",
]

PRIORITY = {
    "SWE1-HMI-PROF-036": ("P2", "All Profiles 之預設排序；清單之呈現順序"),
    "SWE1-HMI-PROF-037": ("P2", "預設 profile 依記憶座椅連結排序；呈現順序"),
    "SWE1-HMI-PROF-038": ("P3", "編輯座椅連結後順序不變；罕觸發之呈現穩定性"),
    "SWE1-HMI-PROF-039": ("P2", "回復預設時新增者之落點；順序規則之分支"),
    "SWE1-HMI-PROF-040": ("P2", "全清後回到預設順序；清除流程之後續狀態"),
    "SWE1-HMI-PROF-041-01": ("P1", "清除個人資料後之新現用 profile —— "
                                   "**資料刪除為不可逆**，落點錯即需重建全部設定"),
    "SWE1-HMI-PROF-041-02": ("P1", "無記憶座椅車型之落點；同上之另一分支"),
    "SWE1-HMI-PROF-041-03": ("P2", "清除流程之進度與完成 popup；流程可見性"),
    "SWE1-HMI-PROF-041-04": ("P1", "清除未完成時之失敗告知 —— "
                                   "**缺此則使用者以為已清而實未清**"),
    "SWE1-HMI-PROF-042": ("P2", "長按拖曳重排，且不得啟用該 profile"),
    "SWE1-HMI-PROF-043": ("P3", "username 之對齊與不重疊；純版面"),
    "SWE1-HMI-PROF-044": ("P3", "過長 username 之截斷；規則在外部文件"),
    "SWE1-HMI-PROF-045": ("P2", "connected 帳號之 cloud icon 標示"),
    "SWE1-HMI-PROF-046": ("P1", "R1 High 之流程分歧本身 —— "
                                "誤啟 CPA 即為錯誤變體行為"),
    "SWE1-HMI-PROF-047": ("P1", "入車之 Welcome popup 與自訂提示；ch6 之入口"),
    "SWE1-HMI-PROF-049": ("P1", "Welcome popup 之內容與兩個入口"),
    "SWE1-HMI-PROF-050-01": ("P2", "Remind me Later 之關閉範圍"),
    "SWE1-HMI-PROF-050-02": ("P3", "點擊外部關閉且不再詢問"),
    "SWE1-HMI-PROF-051": ("P1", "Don’t Show me Again 關閉該 profile 之設定 —— "
                                "**逐 profile 之範圍**"),
    "SWE1-HMI-PROF-052": ("P1", "Get Started 起始設定並沿用現有偏好"),
    "SWE1-HMI-PROF-054": ("P1", "Switch Users 之導向"),
    "SWE1-HMI-PROF-055": ("P2", "Avatar 與 Welcome 文字之導向（上次分頁）"),
}

# J-10 —— ER 逐字寫出他節之字面值時，其來源節須併列於引用欄。
REF_EXTRA = {
    # 5.13.1 只寫 `return to default order`，未定義該順序之內容；
    # 其內容在 5.12.1（記憶座椅連結順序）。ER 若不寫出該內容即不可證。
    "SWE1-HMI-PROF-040": [("5.12.1", "memory seat")],
    # 5.13.1 之「全清」以 5.13.2 之 Clear Personal Data 執行，
    # 其確認 popup PU0626 出現於本 TC 之 procedure（X-1 之處理）。
    # 兩個登記併於同一 leaf。
}
REF_EXTRA["SWE1-HMI-PROF-040"].append(("5.13.2", "PU0626"))

TCS = {

    # ── 5.12 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-036": dict(
        title="Profile order defaults to the order of creation",
        design=FUNCTIONAL,
        pre=steps("Only the default Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Create a new Driver Profile named Alex",
                   "Create a second new Driver Profile named Bea",
                   "Open the “All Profiles” tab and read the order of the "
                   "Profiles"),
        er=steps("Driver Profile Alex is created",
                 "Driver Profile Bea is created",
                 "The default Profiles are shown on the left, then Alex, "
                 "then Bea on the right"),
        remarks="**兩條新 profile 是必要的**：只造一條時，"
                "「新者在右」與「新者在最右」無從分辨，"
                "而一個把新 profile 插在最左之實作，單條測不出來。"
                "Alex／Bea 為測試設置（J-12）—— 條文未指定名稱。",
        reasoning=(
            "驗證目標：5.12（ALLPR1）—— profile 之預設順序依加入之先後，"
            "預設者在左、新增者依序往右。"
            "關鍵情境條件：起始須**只有預設 profile**，"
            "否則「預設者在左」之比較無基準。"
            "為什麼這樣切：本 leaf 之單位為**建立順序**；"
            "預設者彼此之順序屬 `SWE1-HMI-PROF-037`，"
            "編輯連結後之不變屬 `SWE1-HMI-PROF-038`。"),
        kw=["Profile order", "creation", "All Profiles", "default"],
    ),

    # ── 5.12.1 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-037": dict(
        title="Default Profiles ordered by their memory seat link",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with memory seats",
                  "Only the default Driver Profiles exist on the vehicle",
                  "Driver 1 is linked to memory seat 1",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the default Profiles and check their order from "
                   "the left"),
        er=steps("The “All Profiles” tab is displayed",
                 "Driver 1, linked to memory seat 1, is the first Profile "
                 "from the left"),
        remarks="**盲區（R-G11）**：能分辨「依座椅連結排序」與「依名稱排序」之"
                "設置，須有一個座椅連結順序**不同於**名稱順序之車輛；"
                "而 5.12.2 已定編輯連結不改順序，**故該設置無法以編輯造出**，"
                "出廠即如此之車輛亦不在手上。"
                "本條遂只驗條文自己舉的例（`Ex: mem seat 1 + Driver 1`）——"
                "**一個依名稱排序之實作會通過本條**，此為已知且不可避免之限制。"
                "編號 1 出自條文之例，非測試設置。",
        reasoning=(
            "驗證目標：5.12.1（ALLPR1.1）—— 預設 profile 依其記憶座椅連結排序。"
            "關鍵情境條件：車輛須有記憶座椅，否則連結不存在。"
            "為什麼這樣切：本 leaf 之單位為**預設者彼此之順序**；"
            "新增者之落點屬 `SWE1-HMI-PROF-036`。"
            "**刻意略過**：排序依據之判別力見 remarks 之盲區聲明 ——"
            "以現有可造之設置無法將其與名稱排序區分開。"),
        kw=["default Profiles", "memory seat", "order", "All Profiles"],
    ),

    # ── 5.12.2 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-038": dict(
        title="Editing a memory seat link leaves the order unchanged",
        # **K-4a 首跑判紅，改判之（40 輪）。** 原標狀態轉換。
        # 該掃描問的是「procedure 內有無造成狀態改變之步驟」，
        # 而本條之核心斷言是**順序在該改變下不變** —— 它驗的是**不變性**，
        # 不是 A→B 之遷移。比照 `SWE1-HMI-PROF-015`（28 包）之先例：
        # **改判方法，不為轉綠而把 `change` 收進詞表**
        # （收了之後，任何含「改某個設定」之條都會被算成狀態轉換）。
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist on the vehicle",
                  "The vehicle is equipped with memory seats",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and record the order of the "
                   "Profiles",
                   "Open the “Edit Profile” tab of the second Profile",
                   "Change the memory seat link of that Profile",
                   "Open the “All Profiles” tab and compare the order with "
                   "step 1"),
        er=steps("The order of the Profiles is recorded",
                 "The “Edit Profile” tab of the second Profile is displayed",
                 "The memory seat link of that Profile is changed",
                 "The order of the Profiles is unchanged from the order "
                 "recorded in step 1"),
        remarks="**取中間位置之 profile**：改第一個或最後一個時，"
                "「順序未變」與「往兩端移動被邊界擋住」不可分辨。"
                "三個 profile 為使中間位置存在（J-12 之測試設置）。",
        reasoning=(
            "驗證目標：5.12.2（ALLPR1.2）—— 編輯記憶座椅連結不改變 profile 之順序。"
            "關鍵情境條件：須先**記錄**原順序，否則「未變」無對照。"
            "為什麼這樣切：本 leaf 之單位為**編輯後之不變性**。"
            "`design_method` 取功能測試而非狀態轉換："
            "本條所驗者為一個狀態改變（座椅連結）之**旁效不發生**，"
            "受檢之順序本身並未遷移 —— 標狀態轉換會使該欄與斷言不符（K-4a）。"),
        kw=["memory seat link", "order", "unchanged", "All Profiles"],
    ),

    # ── 5.13 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-039": dict(
        title="Restored default Profiles are added to the right",
        design=FUNCTIONAL,
        pre=steps("Two custom Driver Profiles exist on the vehicle",
                  "Not all default Driver Profiles are present",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and record the order of the "
                   "Profiles",
                   "Restore the default Driver Profiles without clearing "
                   "all Profiles",
                   "Open the “All Profiles” tab and read where the "
                   "restored Defaults are"),
        er=steps("The order of the Profiles is recorded",
                 "The default Driver Profiles are restored and the custom "
                 "Profiles remain",
                 "The restored Defaults are to the right of the Profiles "
                 "recorded in step 1"),
        remarks="**ER2 併驗「自訂 profile 仍在」** —— 條文之適用條件為"
                "`without clearing all Profiles`；若回復連帶清掉自訂者，"
                "本條所測之情境根本沒有發生，而只驗順序不會發現。"
                "回復預設之**入口**條文未載，依 §8.4.1 不自擬 ——"
                "執行時依實車之回復入口，其位置記於執行紀錄。",
        reasoning=(
            "驗證目標：5.13（ALLPR2）—— 未清除全部 profile 而回復預設者時，"
            "回復之預設 profile 加在最右。"
            "關鍵情境條件：須有自訂 profile 留存，"
            "且**至少一個預設者不在**，回復方為可觀察之事件。"
            "為什麼這樣切：本 leaf 為「不清全部」之分支；"
            "「清全部」之分支屬 `SWE1-HMI-PROF-040`，兩者之結果相反，"
            "故不可併為一條。"),
        kw=["restore", "default Profiles", "right", "order"],
    ),

    # ── 5.13.1 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-040": dict(
        title="Clearing all Profiles returns Defaults to default order",
        design=SCENARIO,
        pre=steps("The vehicle is equipped with memory seats",
                  "Two custom Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the settings and select Clear Personal Data",
                   "Press Yes on each confirmation popup PU0626/PU_0129",
                   "Open the “All Profiles” tab and read the order of the "
                   "default Profiles"),
        er=steps("The Clear Personal Data setting is selected",
                 "All Profiles are cleared and the default Profiles are "
                 "restored",
                 "The default Profiles are ordered by their memory seat "
                 "link, from the left"),
        remarks="ER3 之「default order」其內容不在 5.13.1（該節只寫"
                "`return to default order`），故**併列 5.12.1** 於引用欄，"
                "並將其內容（依記憶座椅連結）逐字寫入 ER —— "
                "否則本條無從判定。"
                "PU0626 為 5.13.2 之確認 popup，本條之 procedure 須處理它，"
                "**故一併列 5.13.2**（X-1 之同型處置）。"
                "**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。"
                "清除後之**現用 profile 落點**屬 `SWE1-HMI-PROF-041-01`／"
                "`SWE1-HMI-PROF-041-02`，本條只驗**順序**。",
        reasoning=(
            "驗證目標：5.13.1（ALLPR2.1）—— 全部 profile 被清除且預設者回復後，"
            "回到預設順序。"
            "關鍵情境條件：須先存在自訂 profile 且其順序已偏離預設，"
            "否則「回到」無從觀察。"
            "為什麼這樣切：`design_method` 取情境／用例 ——"
            "本條走的是一條**跨節之流程**（5.13.2 之清除 → 5.13.1 之順序 →"
            "5.12.1 之順序內容），非單一功能點。"),
        kw=["clear", "default order", "restore", "memory seat"],
    ),

    # ── 5.13.2 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-041-01": dict(
        title="Active Profile after clearing follows the active memory seat",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with memory seats",
                  "Memory seat 2 is the currently active seat position",
                  "Two custom Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the settings and select Clear Personal Data",
                   "Press Yes on each confirmation popup PU0626/PU_0129",
                   "Read the status bar and check which Driver Profile is "
                   "active"),
        er=steps("The Clear Personal Data setting is selected",
                 "The custom Profiles are deleted and the defaults are "
                 "restored",
                 "Driver 2 is the active Driver Profile"),
        remarks="**取 memory seat 2 而非 1**：條文之例即為 seat 2 → Driver 2，"
                "且**一個永遠落到 Driver 1 之實作**（即 `041-02` 之無座椅行為）"
                "在 seat 1 之設置下與正確實作不可分辨。"
                "**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。"
                "編號出自 5.13.2 之條文（`if memory seat 2 is active, "
                "go to Driver 2`），非測試設置。",
        reasoning=(
            "驗證目標：5.13.2 —— 清除個人資料後，新的現用 profile 與"
            "**當前之記憶座椅位置**對應。"
            "關鍵情境條件：車輛須有記憶座椅，且其當前位置**不是第一個**，"
            "落點方具判別力。"
            "為什麼這樣切：037 對 5.13.2 切四個 leaf；本 leaf 之單位為"
            "**有座椅時之落點**，無座椅之落點屬 `SWE1-HMI-PROF-041-02`。"),
        kw=["Clear Personal Data", "memory seat", "active profile",
            "Driver 2"],
    ),

    "SWE1-HMI-PROF-041-02": dict(
        title="Active Profile defaults to Driver 1 without memory seats",
        design=FUNCTIONAL,
        pre=steps("The vehicle is not equipped with memory seats",
                  "Two custom Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the settings and select Clear Personal Data",
                   "Press Yes on each confirmation popup PU0626/PU_0129",
                   "Read the status bar and check which Driver Profile is "
                   "active"),
        er=steps("The Clear Personal Data setting is selected",
                 "The custom Profiles are deleted and the defaults are "
                 "restored",
                 "Driver 1 is the active Driver Profile"),
        remarks="與 `SWE1-HMI-PROF-041-01` 之差別只在**車型**（有無記憶座椅），"
                "而該差別為**條文自己切出之兩個分支**，非我方之變體對造："
                "兩者之預期結果不同，且各有 037 之 leaf。"
                "**PU0626 與 PU_0129 之關係條文未定**（RD #8）。**41 包 §四授權逕行修正**：步驟改為「於**每一個**確認 popup PU0626/PU_0129 按 Yes」—— 兩者若為同一個，該步驟即按一次；若為兩段確認，該步驟即按兩次。**兩種讀法下本條都不會假失敗**，且驗證目標未變（§四之界線）。"
                "編號 1 出自 5.13.2 之條文（`Driver 1 should be the new "
                "active profile`）。",
        reasoning=(
            "驗證目標：5.13.2 —— 無記憶座椅之車輛，清除後之現用 profile "
            "為 Driver 1。"
            "關鍵情境條件：車輛**無**記憶座椅 —— 這是本分支之成立條件本身。"
            "為什麼這樣切：與 `041-01` 同節不同分支；"
            "併為一條則兩個互斥之車型條件會落在同一個 pre-condition 內。"),
        kw=["Clear Personal Data", "no memory seats", "Driver 1"],
    ),

    "SWE1-HMI-PROF-041-03": dict(
        title="PU1089 on confirmation and PU1090 on successful clearing",
        design=FUNCTIONAL,
        pre=steps("Two custom Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the settings and select Clear Personal Data",
                   "Press Yes on each confirmation popup PU0626/PU_0129 and read "
                   "the popup shown",
                   "Wait until the clearing ends and read the popup shown"),
        er=steps("The Clear Personal Data setting is selected",
                 "PU1089 is displayed",
                 "PU1090 is displayed once the data have been cleared"),
        remarks="**PU1089／PU1090 之內文不寫**（R-U27 同型）—— spec 只給 id，"
                "未給文字；ER 只斷言其顯示與時機。"
                "**RD #8 —— 41 包 §四授權逕行修正**：5.13.2 之確認 popup 同時寫了 "
                "PU0626（`confirming from popup PU0626`）與 PU_0129"
                "（`pressing Yes/Ok in pop-up PU_0129`），"
                "**兩者之關係條文未定義**。本條之步驟 2 取 PU_0129 ——"
                "因條文把「按 Yes/Ok 觸發 PU1089」這件事綁在 PU_0129 上。"
                "**本條之步驟 2 改為「於每一個確認 popup PU0626/PU_0129 按 Yes」** ——"
                "兩者若為同一個即按一次，若為兩段確認即按兩次；**兩種讀法下皆不假失敗**。"
                "RD #8 仍照送（上游知情），但不作為修正之前提。",
        reasoning=(
            "驗證目標：5.13.2 —— 清除流程之進度 popup（PU1089）與"
            "完成 popup（PU1090）。"
            "關鍵情境條件：須有可清之自訂資料，否則「完成」之時點不可觀察。"
            "為什麼這樣切：本 leaf 之單位為**成功路徑之兩個 popup**；"
            "失敗路徑之 PU1091 屬 `SWE1-HMI-PROF-041-04`，"
            "其成立條件（HU／TBM 不回報完成）與本條互斥。"),
        kw=["PU1089", "PU1090", "Clear Personal Data", "progress"],
    ),

    "SWE1-HMI-PROF-041-04": dict(
        title="PU1091 shown when clearing is not confirmed complete",
        design=FAULT,
        pre=steps("Two custom Driver Profiles exist on the vehicle",
                  "The vehicle is equipped with a Telematics Box Module",
                  "The vehicle is stationary"),
        # K-4a 要求故障注入之標的明載於 `input_test_data` 或 procedure ——
        # 首跑判紅（procedure 之 `Suppress` 不在其詞表內）。
        # **不改詞表而改記載**：注入之對象與方式本來就該是一個欄位裡的事實，
        # 不是動詞措辭之副產物。
        data="Fault injected: the Telematics Box Module withholds its "
             "completion report for the data clearing",
        proc=steps("Open the settings and select Clear Personal Data",
                   "Press Yes on each confirmation popup PU0626/PU_0129",
                   "Suppress the completion report of the Telematics Box "
                   "Module",
                   "Read the screen and check which popup is displayed"),
        er=steps("The Clear Personal Data setting is selected",
                 "PU1089 is displayed",
                 "The Telematics Box Module does not report complete data "
                 "clearing",
                 "PU1091 is displayed"),
        remarks="**故障注入之對象為 TBM 之完成回報**，非 HU —— 條文寫的是"
                "`if HU or TBM do not confirm`，兩者為**析取**；"
                "注入其一即足以使該條件成立，"
                "**HU 側之注入本條不涵蓋**（其結果不由本條保證）。"
                "注入手段（拔線／模擬器／診斷指令）條文未載，"
                "依 §8.4.1 不自擬，執行時之手段記於執行紀錄。"
                "PU1091 之內文不寫（同 `041-03`）。",
        reasoning=(
            "驗證目標：5.13.2 —— HU 或 TBM 未回報完成時，顯示失敗 popup PU1091。"
            "關鍵情境條件：清除流程須**確實已開始**（故步驟 2 之 PU1089 為"
            "中途之錨點），否則「失敗」與「根本沒開始」不可分辨。"
            "為什麼這樣切：`design_method` 取基礎故障注入 ——"
            "本條之成立條件**無法以正常操作造出**，"
            "須主動使一個模組不回報；這是本批唯一之故障注入條。"),
        kw=["PU1091", "TBM", "failure", "Clear Personal Data"],
    ),

    # ── 5.14 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-042": dict(
        title="Long press on an avatar drags and reorders Profiles",
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist on the vehicle",
                  "The first Driver Profile from the left is the active one",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and record the order of the "
                   "Profiles",
                   "Press and hold the avatar of the second Profile",
                   "Drag that avatar to the leftmost position and release it",
                   "Read the tab and check the order and the active Profile"),
        er=steps("The order of the Profiles is recorded",
                 "The avatar of the second Profile becomes draggable",
                 "That Profile is placed leftmost and the others move right",
                 "The order differs from the one recorded in step 1 and the "
                 "active Profile is unchanged"),
        remarks="**ER4 併驗「未被啟用」** —— 條文之"
                "`(and will not result in that Profile being activated)` 與"
                "拖曳為**同一句之兩個斷言**，依 §5.7 併於本條；"
                "另立則兩條之 procedure 逐字相同，只 ER 差一行。"
                "**被拖者刻意取非現用之 profile**：若拖現用者，"
                "「未被啟用」恆真而無判別力。"
                "三個 profile 為使「其他人往右移」為可觀察之複數（J-12）。",
        reasoning=(
            "驗證目標：5.14（ALLPR3）—— 長按 avatar 可拖曳重排，"
            "且該操作**不得**啟用被按之 profile。"
            "關鍵情境條件：被拖者非現用者，且順序須先記錄。"
            "為什麼這樣切：兩個斷言同屬一句，§5.7 併驗；"
            "**壓力測試（§8.3）**：一個「長按即啟用並且順便可拖」之實作，"
            "只驗拖曳者會通過 —— ER4 之後半即為擋它而設。"),
        kw=["long press", "drag", "reorder", "not activated"],
    ),

    # ── 5.15 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-043": dict(
        title="Usernames are center justified and do not overlap",
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist on the vehicle",
                  "The usernames of the three Profiles differ in length",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read each username and check its position under its "
                   "avatar",
                   "Read the usernames and check that none overlaps another"),
        er=steps("The “All Profiles” tab is displayed",
                 "Each username is center justified under its associated "
                 "avatar",
                 "No username overlaps another username"),
        remarks="**username 長度刻意不同** —— 等長時，置中與靠左之版面"
                "在多數字型下差異極小，且重疊不會發生；"
                "長度不同才使兩個斷言各自可觀察。"
                "過長者之**截斷**屬 `SWE1-HMI-PROF-044`，本條不涉。",
        reasoning=(
            "驗證目標：5.15（ALLPR5）—— username 於 avatar 下置中，且不相互重疊。"
            "關鍵情境條件：多個 profile 且 username 長短不一。"
            "為什麼這樣切：置中與不重疊為**同一句之並列斷言**，§5.7 併為一條；"
            "但拆為兩個 ER 行，使失敗時可指出是哪一半。"),
        kw=["username", "center justified", "overlap", "All Profiles"],
    ),

    # ── 5.15.1 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-044": dict(
        title="Long usernames are truncated on the All Profiles tab",
        design=FUNCTIONAL,
        pre=steps("A Driver Profile whose username exceeds the All Profiles "
                  "username space exists",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the displayed username and compare it with the "
                   "stored username"),
        er=steps("The “All Profiles” tab is displayed",
                 "The username is shown truncated, following the Core HMI "
                 "Logic and Flow truncation rules"),
        remarks="**截斷規則不在本 spec** —— 5.15.1 只說「依 Core HMI Logic "
                "and Flow 之截斷規則」，該文件不在本 feature 之輸入內。"
                "依 §8.4.1 **不自擬規則**：ER 斷言「有截斷且依該文件」，"
                "**其逐條符合性須以該文件覆核**，本條不代為判定。"
                "此為**上游文件依賴**，已記於上繳之獨立判斷 ——"
                "與「037 未產出 leaf」之情形不同，不援引 R-U56。",
        reasoning=(
            "驗證目標：5.15.1（ALLPR5.1）—— 過長之 username 依 Core HMI "
            "之規則截斷。"
            "關鍵情境條件：username 須確實超出可顯示寬度，"
            "否則截斷不會發生而本條恆綠。"
            "為什麼這樣切：**可判定之部分只有「有沒有截斷」**；"
            "「截得對不對」之權威在外部文件，"
            "把它寫進 ER 等於把一個本文件無法判定之斷言偽裝成可判定。"),
        kw=["truncation", "username", "Core HMI", "All Profiles"],
    ),

    # ── 5.16 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-045": dict(
        title="Cloud icon marks Profiles linked to a Connected account",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with connectivity",
                  "Driver Profile A is connected with a Connected account",
                  "Driver Profile B is not connected with a Connected "
                  "account",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and read the avatars of "
                   "both Profiles",
                   "Open the “Edit Profile” tab of Driver Profile A and "
                   "read its avatar"),
        er=steps("A cloud icon is next to the avatar of Driver Profile A "
                 "and not next to Driver Profile B",
                 "A cloud icon is next to the avatar on the “Edit Profile” "
                 "tab"),
        remarks="**B profile 為對照** —— 只驗 A 有 icon 時，"
                "一個「所有 profile 都掛 cloud icon」之實作會通過；"
                "條文之 `if the profile is connected` 是**條件**，"
                "其判別力全在未連結者身上。"
                "**兩個分頁併驗**：條文一句列出 All Profiles 與 Edit Profile "
                "兩處，依 §5.7 併為一條之兩個 ER 行。"
                "**本條之 label 依 RD #5 之答覆可能調整**"
                "（39 包作業 2 之命中：本節寫 `Connected account`）。",
        reasoning=(
            "驗證目標：5.16（ALLPR6）—— 與 Connected 帳號連結之 profile，"
            "其 avatar 旁顯示 cloud icon。"
            "關鍵情境條件：須同時存在已連結與未連結之 profile。"
            "為什麼這樣切：條文之 `(See Connected Personal Account HMI)` "
            "指向他文件之**帳號連結流程**，本條不涉其如何連上，"
            "只驗**連上之後之標示**。"),
        kw=["cloud icon", "Connected account", "All Profiles",
            "Edit Profile"],
    ),

    # ── 6.1 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-046": dict(
        title="R1 High keeps preferences and begins Tutorials after avatar",
        design=SCENARIO,
        pre=steps("The vehicle is an R1 High variant",
                  "A New Profile Setup is in progress at the avatar step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the current preferences of the active Driver "
                   "Profile",
                   "Choose an avatar and press Save & Continue",
                   "Read the screen shown after the avatar step",
                   "Read the preferences of the active Driver Profile and "
                   "compare them with step 1"),
        er=steps("The current preferences are recorded",
                 "The avatar is chosen and the avatar step ends",
                 "Tutorials begin and no Connected Personal Account login "
                 "is launched",
                 "The preferences of the active Driver Profile are "
                 "unchanged from those recorded in step 1"),
        remarks="**變體 axis `r1h-cpa-6.1`**：本條為 R1 High 側。"
                "base 側（`Is CPA present?` 為是時啟動 CPA 登入）"
                "**在 037 內無 leaf** —— 它只出現於 PDF p9 之流程圖，"
                "依 R-U56 不造 —— 其不造之判定已於變體覆寫之登記表逐條實測。"
                "條文尚有 `it will be accessible from the Edit Profile "
                "screen only` 一句 —— 該全稱之**反向**（他處不得進入 CPA）"
                "本條不涵蓋，其入口清單不可窮舉，"
                "已記為 ch11 之覆蓋事項（`SWE1-HMI-PROF-110` 為其正向）。",
        reasoning=(
            "驗證目標：6.1（NOPR0）—— R1 High 上 CPA 不啟動；選完 avatar 後"
            "保留現有偏好並進入 Tutorials。"
            "關鍵情境條件：車型須為 R1 High —— 本條之全部內容皆以此為前提。"
            "為什麼這樣切：`design_method` 取情境／用例 ——"
            "本條驗的是**一段流程之走向**（avatar → 不進 CPA → 進 Tutorials），"
            "非單一畫面之功能點。"
            "**AB-1（45 包）之連帶**：ER4 之兩端**皆為現用 profile 之偏好**"
            "（設定前後兩個時點），故指名之 —— 與 `TC-154` 不同："
            "那一條之兩端是**兩個不同的 profile**。"
            "**本條之兩端同物不是恆真**：其間之事件（avatar 步驟）"
            "在 base 變體上正是 CPA 會介入之處。"
            "**ER4 之偏好比對不可省**：條文說的是 `keep current preferences`，"
            "一個「跳過 CPA 但把偏好重設為預設」之實作，"
            "只驗 Tutorials 有沒有開會通過（§8.3）。"),
        kw=["R1 High", "CPA", "Tutorials", "preferences"],
    ),

    # ── 6.2 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-047": dict(
        title="Welcome popup at vehicle entry prompts to customize",
        design=FUNCTIONAL,
        pre=steps("Only the default Driver Profiles exist on the vehicle",
                  "The Welcome popup setting is on for the active Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Switch the ignition on and read the screen",
                   "Read the popup and check the prompt to customize the "
                   "Profile"),
        er=steps("A Welcome popup is displayed upon vehicle entry",
                 "The popup prompts the user to customize the default "
                 "Driver Profile"),
        remarks="**條文列兩個觸發**（`At vehicle entry` 與 `initiation of a "
                "newly active Profile`）。本條取**入車**一側；"
                "**新啟用 profile 一側由 `SWE1-HMI-PROF-023`"
                "（`NR1L-UserProfiles-118`）承擔** —— 該 leaf 為 5.3.1 之"
                "「切換 profile 後顯示 welcome popup」。"
                "§7 之列舉配對於此以跨節委派完成，非漏測。"
                "自訂提示之**按下之後**屬 6.4（`SWE1-HMI-PROF-052`），"
                "本條只驗提示之存在。",
        reasoning=(
            "驗證目標：6.2（NOPR1）—— 入車或新 profile 啟用時顯示 Welcome "
            "popup，且其中含自訂預設 profile 之提示。"
            "關鍵情境條件：現用者須為**預設** profile ——"
            "自訂提示之對象即為預設 profile，自訂者身上不成立。"
            "為什麼這樣切：本 leaf 之單位為**提示之存在**；"
            "popup 之按鈕組成屬 6.3（`SWE1-HMI-PROF-049`），"
            "兩者同一個 popup 而斷言不同，依 037 之切法各自成條。"),
        kw=["Welcome popup", "vehicle entry", "customize", "default Profile"],
    ),

    # ── 6.3 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-049": dict(
        title="Welcome popup shows the Profile, Switch Users and Get Started",
        design=FUNCTIONAL,
        pre=steps("The active Driver Profile is a default Profile",
                  "The Welcome popup setting is on for that Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Switch the ignition on and read the popup shown",
                   "Read the popup and check the Profile name and the "
                   "buttons offered"),
        er=steps("A Welcome popup is displayed upon vehicle entry",
                 "The popup names the active Profile and offers Switch "
                 "Users and Get Started"),
        remarks="**Get Started 只在預設 profile 上出現**（條文之 `for default "
                "Profile(s)`）。本條取預設一側；**自訂 profile 一側之"
                "popup 組成屬 7.2（`SWE1-HMI-PROF-058`），於第六批生成** ——"
                "此處不宣稱其已被驗。"
                "`Until popups are turned off` 為適用條件（§8.7.3），"
                "以 pre-condition 固定為「開啟」；"
                "**關閉之後之行為屬 `SWE1-HMI-PROF-051`**。",
        reasoning=(
            "驗證目標：6.3（NOPR2）—— Welcome popup 告知現用 profile，"
            "並提供 Switch Users 與（預設 profile 時）Get Started。"
            "關鍵情境條件：popup 設定須為開啟，且現用者為預設 profile。"
            "為什麼這樣切：三個內容項為**同一畫面之並列斷言**，§5.7 併驗；"
            "兩個按鈕**按下之後**之行為分屬 6.4／6.5，"
            "本條只驗其存在與 profile 名稱之正確。"),
        kw=["Welcome popup", "Switch Users", "Get Started", "default"],
    ),

    # ── 6.3.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-050-01": dict(
        title="Remind me Later closes the popup until next activation",
        design=STATE,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The Welcome popup setting is off for Driver Profile B",
                  "The Welcome popup of Driver Profile A is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press X on the Welcome popup and read the popup shown",
                   "Select Remind me Later on that popup",
                   "Activate Driver Profile B",
                   "Activate Driver Profile A again and read the screen"),
        er=steps("A popup offering Remind me Later and Don’t Show me Again "
                 "is displayed",
                 "The Welcome popup is closed",
                 "Driver Profile B is active",
                 "The Welcome popup of Driver Profile A is displayed again"),
        remarks="**ER4 是本條之重點**：條文說的是「關到**該 profile 下次被啟用**"
                "為止」—— 只驗「按了會關」，一個永久關閉之實作會通過（§8.3）。"
                "**刻意不斷言 key cycle 內之顯示與否**："
                "「key-on 是否算一次 activation」條文未定義，"
                "依 §8.4.1 保留歧義，不以本條推定。"
                "`Don’t Show me Again` 之後果屬 `SWE1-HMI-PROF-051`。"
                "**X-1（切換 profile 觸發 5.3.1 之 PU0580）**："
                "步驟 3 切到 B 會顯示 B 之 welcome popup，"
                "故 pre-condition 指定 B 之 Welcome popup 設定為關閉 ——"
                "使步驟 4 所見之 popup 必屬 A，不會與 B 之 popup 混淆。",
        reasoning=(
            "驗證目標：6.3.1（NOPR2.1）—— 按 X 後之二次 popup，"
            "選 Remind me Later 關閉至該 profile 下次啟用。"
            "關鍵情境條件：須有第二個 profile，"
            "否則「切走再切回」這個唯一無歧義之 activation 造不出來。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "本條驗的是一個**壓抑狀態之建立與其解除**，"
            "而解除之條件正是條文所定之 activation。"),
        kw=["Remind me Later", "Welcome popup", "close", "activation"],
    ),

    "SWE1-HMI-PROF-050-02": dict(
        title="Clicking outside closes the popup without asking",
        design=FUNCTIONAL,
        pre=steps("The Welcome popup of the active Profile is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the screen outside the Welcome popup",
                   "Read the screen and check which popups are displayed"),
        er=steps("The Welcome popup is closed",
                 "No popup offering Remind me Later and Don’t Show me Again "
                 "is displayed"),
        remarks="**ER2 為缺席斷言** —— 條文之 `without asking` 只能以"
                "「那個 popup 沒有出現」證之。"
                "與 `SWE1-HMI-PROF-050-01` 同節不同分支："
                "按 X 與點擊外部之結果**相反**（一個問、一個不問），"
                "故 037 切為兩個 leaf，本條不與其併。",
        reasoning=(
            "驗證目標：6.3.1（NOPR2.1）末句 —— 點擊 popup 外部直接關閉，"
            "不出現 Remind me Later／Don’t Show me Again 之詢問。"
            "關鍵情境條件：Welcome popup 須在顯示中。"
            "為什麼這樣切：本條為**負向形態之斷言**，"
            "其判定不依賴二次 popup 之內容，"
            "故不因 RD 之 label 答覆而變（J-7）。"),
        kw=["click outside", "Welcome popup", "close", "no prompt"],
    ),

    # ── 6.3.2 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-051": dict(
        title="Don’t Show me Again turns the popup off for that Profile",
        design=STATE,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The Welcome popup setting is on for both Profiles",
                  "The Welcome popup of Driver Profile A is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press X on the Welcome popup and read the popup shown",
                   "Select Don’t Show me Again and read the Welcome popup "
                   "setting",
                   "Activate Driver Profile B and read the screen",
                   "Activate Driver Profile A again and read the screen"),
        er=steps("A popup offering Remind me Later and Don’t Show me Again "
                 "is displayed",
                 "The Welcome popup setting of Driver Profile A is off",
                 "Driver Profile B is active and its Welcome popup is "
                 "displayed",
                 "Driver Profile A is active and no Welcome popup is "
                 "displayed"),
        remarks="**ER3 是逐 profile 之隔離**：條文寫的是"
                "`turn off the setting … for that Profile`；"
                "一個把該設定存成**全域**之實作，只驗 A 不再顯示會通過"
                "（§8.3；同 `SWE1-HMI-PROF-018-02` 之 Z-1 形狀）。"
                "**ER4 與 `050-01` 之 ER4 相反** —— 兩條之判別力互為對照："
                "Remind me Later 再啟用時回來，Don’t Show me Again 不回來。"
                "**X-1（切換 profile 觸發 5.3.1 之 PU0580）**："
                "步驟 3 切到 B 所觸發之 welcome popup **即 ER3 所斷言者**，"
                "非未處理之干擾。",
        reasoning=(
            "驗證目標：6.3.2（NOPR2.2）—— 選 Don’t Show me Again 關閉"
            "**該 profile** 之 Welcome popup 設定。"
            "關鍵情境條件：須有第二個 profile 且其設定為開啟，"
            "逐 profile 之範圍方可觀察。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "本條驗的是一個**持久設定之翻轉**，"
            "其效力須跨一次 profile 切換仍成立。"),
        kw=["Don’t Show me Again", "Welcome popup", "setting", "per Profile"],
    ),

    # ── 6.4 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-052": dict(
        title="Get Started starts setup and carries over preferences",
        design=SCENARIO,
        pre=steps("The active Driver Profile is a default Profile",
                  "The Welcome popup with the Get Started button is "
                  "displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the current preferences of the active Driver "
                   "Profile",
                   "Press Get Started on the Welcome popup",
                   "Read the screen and check that the New Profile Setup "
                   "started",
                   "Complete the setup and read the preferences of the new "
                   "Driver Profile"),
        er=steps("The current preferences are recorded",
                 "The New Profile Setup is initiated",
                 "The first step of the New Profile Setup is displayed and "
                 "no confirmation popup appeared",
                 "The preferences of the new Driver Profile are the same as "
                 "those recorded in step 1"),
        remarks="**AB-1（45 包）**：步驟 4 與 ER4 原寫「讀偏好，與步驟 1 所記者"
                "**未改變**」而**未指明所讀者為誰之偏好** —— 若讀成「現用之"
                "預設 profile 之偏好沒被動到」，該斷言**在任何實作下皆真**，"
                "**包括一個起始設定但完全不帶入偏好之實作**（§7 之 false pass）。"
                "現指明所讀者為**設定流程所建之新 profile**，"
                "且 ER4 斷言其與步驟 1 所記者**相同**（carry-over 成立），"
                "非「未改變」。"
                "**三個斷言各有其失效方式**：起始設定（ER2／ER3 前半）、"
                "**無確認 popup**（ER3 後半，條文之 `without a popup to "
                "confirm`）、**偏好沿用**（ER4）。"
                "缺任一者，條文之一部分即無人驗。"
                "設定流程本身之各步驟屬 ch8（`SWE1-HMI-PROF-066` 以下），"
                "本條只驗其**被起始**與偏好之沿用。",
        reasoning=(
            "驗證目標：6.4（NOPR3）—— 按 Get Started 起始 New Profile Setup，"
            "沿用現用 profile 之全部偏好，且不出現確認 popup。"
            "關鍵情境條件：現用者為預設 profile（Get Started 只在其上出現），"
            "且偏好須先記錄。"
            "為什麼這樣切：`design_method` 取情境／用例 ——"
            "本條跨 popup 與設定流程兩個畫面族。"
            "**ER3 之缺席斷言不可省**：條文特別標明「不出現確認 popup」，"
            "那是與 6.3.1 之詢問行為刻意對比之設計。"
            "**ER4 之兩端各屬何物須明指（AB-1）**：一端為**步驟 1 所記之"
            "現用 profile 之偏好**，另一端為**新建 profile 之偏好** ——"
            "**兩端同物則恆真**，而條文所要者正是兩端不同物而值相同。"),
        kw=["Get Started", "New Profile Setup", "carry over", "preferences"],
    ),

    # ── 6.5 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-054": dict(
        title="Switch Users opens the All Profiles tab",
        design=FUNCTIONAL,
        pre=steps("The Welcome popup with the Switch Users button is "
                  "displayed",
                  "The last used tab of the active Profile is the “Edit "
                  "Profile” tab",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press Switch Users on the Welcome popup",
                   "Read the screen and check which tab of the Profile "
                   "section is shown"),
        er=steps("The Welcome popup is closed and the Profile section is "
                 "opened",
                 "The “All Profiles” tab is displayed"),
        remarks="**pre-condition 刻意把上次分頁設為 “Edit Profile”** ——"
                "否則 5.1 之 latch（上次分頁）與本條之「固定到 All Profiles」"
                "會給出相同結果，兩者不可分辨。"
                "此設置亦使本條與 `SWE1-HMI-PROF-055`（導向上次分頁）"
                "之判別力各自成立。",
        reasoning=(
            "驗證目標：6.5（NOPR4）—— 按 Switch Users 進入 Profile 區之"
            "“All Profiles” 分頁。"
            "關鍵情境條件：上次分頁須**不是** “All Profiles”。"
            "為什麼這樣切：本 leaf 為單一導向斷言；"
            "切換 profile 之後續行為屬 5.3（`SWE1-HMI-PROF-022`），"
            "本條只到達分頁為止。"),
        kw=["Switch Users", "All Profiles", "Profile section", "Welcome"],
    ),

    # ── 6.6 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-055": dict(
        title="Avatar and Welcome text open the last known tab",
        design=FUNCTIONAL,
        pre=steps("The Welcome popup of the active Profile is displayed",
                  "The last known tab of the active Profile is the “Edit "
                  "Profile” tab",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Avatar on the Welcome popup",
                   "Read the screen and check which tab is shown",
                   "Return to the Welcome popup and press the “Welcome "
                   "[username]” text",
                   "Read the screen and check which tab is shown"),
        er=steps("The Profile section is opened",
                 "The “Edit Profile” tab, the last known tab, is displayed",
                 "The Profile section is opened again",
                 "The “Edit Profile” tab, the last known tab, is displayed"),
        remarks="**條文列兩個入口**（Avatar 與 `Welcome [username]` 文字），"
                "依 §7 兩者皆須走到 —— 故本條四步而非兩步。"
                "方括號 `[username]` **逐字引自 6.6**（§11 之 profile-scoped "
                "例外，D-UP22-01；G19 對照來源列驗證）。"
                "上次分頁固定為 “Edit Profile”，"
                "使本條與 `SWE1-HMI-PROF-054`（固定到 All Profiles）"
                "之結果相反而可分辨。",
        reasoning=(
            "驗證目標：6.6（NOPR5）—— 按 Avatar 或 “Welcome [username]” 文字，"
            "進入 Profile 區之**上次分頁**。"
            "關鍵情境條件：上次分頁須**不是**預設分頁 “All Profiles”，"
            "否則與 5.1 之預設值不可分辨。"
            "為什麼這樣切：兩個入口為同一句之列舉，§7 要求皆走到；"
            "併為一條而非兩條，因其 ER 逐字相同、pre-condition 亦同 —— "
            "分立只會產生一對雙胞胎。"),
        kw=["Avatar", "Welcome text", "last known tab", "Profile section"],
    ),
}


def build() -> list:
    rows = B.leaf_rows()
    missing = [r for r in SAMPLE if r not in TCS]
    extra = [r for r in TCS if r not in SAMPLE]
    if missing or extra:
        raise SystemExit(f"取樣清單與內容不一致：缺 {missing}／多 {extra}")

    out, n = [], TC_START
    for req_id in SAMPLE:
        ctx = B.assemble(req_id, rows[req_id])
        spec = TCS[req_id]
        prio, why = PRIORITY[req_id]
        refs = ctx["specification_reference"]
        for sec, _provides in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{sec}"
        rec = _rec(req_id, ctx, spec, refs, prio, why, n)
        rec["batch"] = "batch05"
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
