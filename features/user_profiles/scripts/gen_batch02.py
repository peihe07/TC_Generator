#!/usr/bin/env python3
"""第二批之生成器（19 包作業 5）—— ch12→13→14，29 leaf，tc_id 045–073。

## 本批之三件特殊處置

1. **`128-03` 需 30 分鐘等待**（J-8）：照寫、不縮時、不刪除，
   於 `remarks` 具名其執行成本，使排程者看得見。
2. **`134`（14.1）之 R-U51 判讀首次受檢**：其 `above` 之指涉對象經複位後
   **不在 ch14**（ch14 只有 14.1／14.2，14.1 即首條）——
   實際指 12.3.1／12.6 之退出流程，故併列該二節。詳見上繳 19 §4。
3. **12.8／12.8.1 之 037 標題與描述錯位**：依 **description** 生成
   （其與條文對齊），標題僅供索引。已開 A-UP11。

## 來源標示（J-4／J-12 之四類）

`spec`／`方法`（§5.6 等）／`裁決`（R-U21 等）／`測試設置`（編號、數量）——
凡非 spec 者於 `reasoning` 具名其權威。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE, BVA,  # noqa: E402
                       NEGATIVE, FAULT)
from gen_batch01 import _rec                           # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
SAMPLE_TSV = FEATURE / "data" / "batch02_sample.tsv"
TC_START = 45

REF_EXTRA = {
    # 12.2.1 之 PU0091 與 12.5 之鎖頭圖示於本 TC 之 ER 內
    "SWE1-HMI-PROF-134": [
        # `Exit Valet Mode process above` 之實際指涉。
        # **原本併列 12.6，由 G17 之 provides 驗證抓出：**
        # 12.6 給的是「按狀態列 Profile 鍵→詢問停用」那條路徑，
        # 而本 TC 走的是 welcome popup 之按鈕 —— **12.6 沒被用到，屬多引**。
        ("12.3.1", "4 digit PIN"),
    ],
}

PRIORITY = {
    "SWE1-HMI-PROF-113": ("P0", "Valet 進出時之偏好儲存與重設 —— 核心五類之二者交會"),
    "SWE1-HMI-PROF-114": ("P2", "狀態列之預設版面；呈現層"),
    "SWE1-HMI-PROF-115": ("P1", "啟用入口之限制；非主路徑分支"),
    # K-1：P1 → P0（21 包明列）。行車中不得啟用 = safety 防線本身。
    "SWE1-HMI-PROF-116": ("P0", "行車中不得啟用 Valet Mode —— **防線成立本身**"
                                "（§10.2 safety）"),
    "SWE1-HMI-PROF-117": ("P0", "啟用之 PIN —— Valet Mode 之防護本身"),
    "SWE1-HMI-PROF-118": ("P0", "停用之 PIN —— 同上"),
    "SWE1-HMI-PROF-119": ("P1", "斷電後之重設與 profile 接續；spec 明訂之行為，非漏洞"),
    "SWE1-HMI-PROF-120": ("P1", "退出後之 profile 接續"),
    "SWE1-HMI-PROF-121": ("P2", "PIN 輸入之取消路徑"),
    "SWE1-HMI-PROF-122": ("P2", "狀態列之 Valet 指示；呈現層"),
    "SWE1-HMI-PROF-123": ("P2", "Valet 中按 Profile 鍵之提示"),
    "SWE1-HMI-PROF-124": ("P0", "**Valet 下不得載入車主 profile** —— 失效即隔離被繞過"),
    # K-1：P1 → P0。Valet 之隔離即車主資產（配對裝置）之防線。
    "SWE1-HMI-PROF-125-01": ("P0", "Device Manager 之鎖定 —— 車主資產之防線本身"),
    "SWE1-HMI-PROF-125-02": ("P0", "Projection／HFP／VR 之停用 —— "
                                   "阻擋 valet 使用者觸及車主之手機連線"),
    "SWE1-HMI-PROF-125-03": ("P0", "狀態列互動之限制 —— 隔離之邊界本身"),
    "SWE1-HMI-PROF-125-04": ("P2", "不可互動項之變灰呈現"),
    "SWE1-HMI-PROF-126-01": ("P2", "手套箱鎖之進入提示（PU0832）"),
    # **P-1（24 包）：兩條之判級對調 —— 21 輪之 K-1 判反了。**
    #
    # 21 輪寫「變灰即該防線之執行手段 —— 未變灰則按下可解鎖手套箱」。
    # **該推論正是 canon §8.7.4 逐字所否定者**：
    #   `A visual state (greyed-out, dimmed) does NOT imply non-operability`
    # 變灰是**指示**，不是機制。一個變灰、按下卻仍解鎖之實作，126-02 會通過 ——
    # 它證不了手套箱鎖得住。
    #
    # 且與 D-UP16-01 附二之自訂分野方向相反（防線本身 → P0／其呈現 → P2），
    # 又與同形之 125-04（不可互動項變灰，P2）不一致 —— **同形不同級**。
    #
    # 改：126-02 → P2（同 125-04）；126-03 → P0（其 ER1 `the press is not
    # accepted and the glove box lock state does not change` 才是防線本身）。
    "SWE1-HMI-PROF-126-02": ("P2", "手套箱鎖按鈕之變灰呈現（同 TC-060）——"
                                   "§8.7.4：視覺狀態不蘊含不可操作，故本條非防護機制"),
    "SWE1-HMI-PROF-126-03": ("P0", "按下已變灰之按鈕**不生效**、鎖定狀態未變 ——"
                                   "實體資產之防護成立本身（D-UP16-01 附二）"),
    "SWE1-HMI-PROF-127": ("P1", "手套箱狀態之還原；退出後之狀態接續"),
    "SWE1-HMI-PROF-128-02": ("P0", "鎖定期間不得輸入 PIN —— 防暴力嘗試之機制本身"),
    "SWE1-HMI-PROF-128-03": ("P1", "鎖定屆滿後之可用性回復"),
    "SWE1-HMI-PROF-129": ("P2", "Go 鍵之可用性與其提示"),
    "SWE1-HMI-PROF-130": ("P3", "輸滿 4 碼後數字鍵變灰 —— 呈現細節"),
    "SWE1-HMI-PROF-131": ("P0", "SPAAK 之自動啟用（免 PIN）—— Valet 進出"),
    "SWE1-HMI-PROF-132-01": ("P0", "SPAAK 下主機退出之全面阻擋 —— 隔離被繞過即失效"),
    "SWE1-HMI-PROF-133": ("P2", "SPAAK 下按 Profile 圖示之提示（PU1573）"),
    "SWE1-HMI-PROF-134": ("P1", "Valet welcome popup 之內容與退出入口"),
    "SWE1-HMI-PROF-135": ("P0", "**行車中不得停用** —— 失效即 Valet 可於行進中被解除"),
}

TCS = {

    "SWE1-HMI-PROF-113": dict(
        title="Valet Mode starts from defaults and restores on exit",
        design=STATE,
        pre=steps("A Driver Profile with customized preferences is active",
                  "Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the preferences of the active Profile",
                   "Activate Valet Mode",
                   "Read the preferences and change one of them",
                   "Exit Valet Mode",
                   "Read the preferences and check that they match those "
                   "recorded in step 1"),
        er=steps("The preferences of the active Profile are recorded",
                 "Valet Mode is active and its preferences are the default "
                 "ones, not those recorded in step 1",
                 "The changed preference is stored while Valet Mode is active",
                 "Valet Mode is exited",
                 "The preferences match those recorded in step 1"),
        reasoning=(
            "驗證目標：12.1（PVAL1）—— 啟用 Valet Mode 視同以預設偏好建立新 profile，"
            "退出視同刪除該 profile；期間之變更只存到退出為止。"
            "關鍵情境條件：須有一個已客製化之 profile 作為基準線，"
            "否則「預設 vs 客製」分不出來（§5.6）。"
            "為什麼這樣切：進入與退出雖為兩個觸發，但條文以「像建立／像刪除」"
            "成對定義，**只驗一半則另一半之語意不成立** —— 同 13.2 之處置（§5.7 之例外，具名）。"),
        kw=["Valet Mode", "default preferences", "exit", "store"],
    ),

    "SWE1-HMI-PROF-114": dict(
        title="Status bar returns to its default setup in Valet Mode",
        design=FUNCTIONAL,
        pre=steps("The status bar is configured away from its default setup",
                  "Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the current status bar setup",
                   "Activate Valet Mode",
                   "Read the status bar and check that it shows the default "
                   "setup with the Profile icon visible"),
        er=steps("The current status bar setup is recorded",
                 "Valet Mode is active",
                 "The status bar shows the default setup and the Profile "
                 "icon is visible"),
        reasoning=(
            "驗證目標：12.1.1（PVAL1.1）—— Valet Mode 啟用時狀態列須回到預設版面，"
            "使 Profile 圖示恆可見。"
            "關鍵情境條件：pre-condition 要求狀態列先偏離預設，"
            "否則「回到預設」與「本來就是預設」無從分辨。"
            "為什麼這樣切：預設版面之細節條文委派 Core HMI Logic and Flow，"
            "本 TC 只驗其回到預設且 Profile 圖示可見（§8.4.1 不代擬他份文件之內容）。"),
        kw=["status bar", "default", "Profile icon", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-115": dict(
        title="Valet Mode activates only from the All Profiles tab",
        # K-4a（21 包）：原掛負向測試 —— 但本 TC **沒有非法操作**，
        # 它做的是「到兩個地方看，那裡沒有該控制」。§12 之負向為
        # `Invalid input / illegal op`，找不到一個東西不是非法操作。
        # 首匹配落在「單一功能檢查 → 功能測試」。
        design=FUNCTIONAL,
        pre=steps("Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab and read the option "
                   "list",
                   "Open the vehicle settings and read the option list",
                   "Open the “All Profiles” tab and check that the "
                   "Valet Mode button is present there"),
        er=steps("No Valet Mode activation control is present on the "
                 "“Edit Profile” tab",
                 "No Valet Mode activation control is present in the vehicle "
                 "settings",
                 "The Valet Mode button is present on the “All "
                 "Profiles” tab"),
        reasoning=(
            "驗證目標：12.2（PVAL2）—— Valet Mode 只能經 All Profiles 分頁之按鈕啟用。"
            "關鍵情境條件：「只能」之驗證須同時看兩側 ——"
            "別處沒有（步驟 1、2）與該處有（步驟 3）；"
            "**只驗該處有，一個到處都能啟用之實作也會通過**（§7）。"
            "為什麼這樣切：受檢之他處取 Edit Profile 分頁與車輛設定兩個最可能之位置；"
            "**窮舉所有畫面不可行**，此為抽樣，已於上繳具名。"),
        kw=["Valet Mode", "All Profiles tab", "activation", "only"],
    ),

    "SWE1-HMI-PROF-116": dict(
        title="Valet Mode button greyed out while the vehicle is in motion",
        design=STATE,
        pre=steps("Valet Mode is not active",
                  "The vehicle is stationary on a test track and can be "
                  "brought into motion"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and read the Valet "
                   "Mode button",
                   "Bring the vehicle into motion",
                   "Read the Valet Mode button and press it",
                   "Read the screen and check that the unavailability popup "
                   "is displayed"),
        er=steps("The Valet Mode button is selectable while stationary",
                 "The vehicle is in motion",
                 "The Valet Mode button is greyed out",
                 "PU0091 indicates that the function is not available"),
        reasoning=(
            "驗證目標：12.2.1（PVAL2.1）—— 行車中 Valet Mode 按鈕變灰；"
            "按下已變灰之按鈕時顯示 PU0091。"
            "關鍵情境條件：以靜止時可選為基準線（§5.6），"
            "判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換）。"
            "為什麼這樣切：變灰與按下之提示為同一條件下之兩個結果，"
            "037 未再切分，故併為一條（§5.7）。"),
        kw=["Valet Mode", "greyed out", "in motion", "PU0091"],
    ),

    "SWE1-HMI-PROF-117": dict(
        title="Four-digit PIN required to activate Valet Mode",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is not active",
                  "The vehicle is stationary"),
        data="PIN: a 4-digit one-time PIN chosen at activation",
        proc=steps("Open the “All Profiles” tab and press the Valet "
                   "Mode button",
                   "Read the screen and check that a 4-digit PIN entry is "
                   "required",
                   "Enter a 4-digit PIN and confirm",
                   "Read the screen and check that Valet Mode is active"),
        er=steps("The Valet Mode activation is started",
                 "A 4-digit PIN entry is requested before activation",
                 "The 4-digit PIN is accepted",
                 "Valet Mode is active"),
        reasoning=(
            "驗證目標：12.3（PVAL3）—— 啟用 Valet Mode 須輸入 4 位一次性 PIN。"
            "關鍵情境條件：ER2 明寫「在啟用之前」要求 PIN ——"
            "若寫成「輸入 PIN 後啟用」，一個先啟用再問 PIN 之實作也會通過（§7）。"
            "為什麼這樣切：停用側之同一 PIN 屬 12.3.1，"
            "PIN 錯誤之次數上限屬 12.9，皆不在本條。"),
        kw=["Valet Mode", "4 digit PIN", "one-time", "activate"],
    ),

    "SWE1-HMI-PROF-118": dict(
        title="Same four-digit PIN required to leave Valet Mode",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active and was activated with a known "
                  "4-digit PIN",
                  "The vehicle is stationary"),
        data="PIN: the same 4-digit PIN used at activation; "
             "one differing 4-digit PIN",
        proc=steps("Start the Valet Mode deactivation",
                   "Enter a 4-digit PIN that differs from the activation PIN",
                   "Enter the same 4-digit PIN used at activation",
                   "Read the screen and check that Valet Mode is no longer "
                   "active"),
        er=steps("The PIN entry for deactivation is displayed",
                 "The differing PIN is rejected and Valet Mode is still "
                 "active",
                 "The same PIN as at activation is accepted",
                 "Valet Mode is no longer active"),
        reasoning=(
            "驗證目標：12.3.1（PVAL3.1）—— 退出 Valet Mode 須輸入**與啟用時相同**之 PIN。"
            "關鍵情境條件：「相同」之驗證須有一個不同之 PIN 作對照（§7）——"
            "只驗正確 PIN 可退出，一個任何 4 位數都接受之實作也會通過。"
            "為什麼這樣切：錯誤次數之上限屬 12.9，本條只驗「須相同」。"),
        kw=["Valet Mode", "same PIN", "deactivate", "4 digit"],
    ),

    "SWE1-HMI-PROF-119": dict(
        title="Battery disconnect resets Valet Mode at the next key on",
        design=FAULT,
        pre=steps("Valet Mode is active",
                  "The last known Driver Profile before Valet Mode is "
                  "recorded",
                  "The vehicle is stationary and the battery can be "
                  "disconnected on the bench"),
        data="Fault injected: battery disconnected while Valet Mode is active",
        proc=steps("Disconnect the vehicle battery",
                   "Reconnect the battery and switch the key on",
                   "Read the active Profile and check that Valet Mode is no "
                   "longer active"),
        er=steps("The battery is disconnected",
                 "The vehicle powers up at key on",
                 "Valet Mode is not active and the last known Driver Profile "
                 "is loaded"),
        reasoning=(
            "驗證目標：12.3.2（PVAL3.2）—— 斷開電瓶會覆寫並重設 Valet Mode，"
            "下次 key on 時載入最後已知之 Driver Profile。"
            "關鍵情境條件：斷電為可模擬之故障（§12 首匹配 → 基礎故障注入）；"
            "「最後已知 profile」須於 pre-condition 先記錄，否則無比對對象。"
            "**來源標示（J-4）**：`key on` 之觀察點與 `ignition cycle` 同屬 **R-U21** 之"
            "「設定→key cycle→讀回」形態，惟本條之 key on 為**條文明述**（`at the next key on`），"
            "故其權威為 spec 而非裁決。"),
        kw=["battery", "disconnect", "reset", "Valet Mode", "key on"],
    ),

    "SWE1-HMI-PROF-120": dict(
        title="Previous Profile restored after Valet Mode is exited",
        design=STATE,
        pre=steps("Driver Profile A is active and Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the active Profile",
                   "Activate Valet Mode",
                   "Deactivate Valet Mode",
                   "Read the active Profile and check that it matches the "
                   "one recorded in step 1"),
        er=steps("Driver Profile A is recorded as active",
                 "Valet Mode is active",
                 "Valet Mode is deactivated",
                 "Driver Profile A is active again"),
        reasoning=(
            "驗證目標：12.3.3（PVAL3.3）—— 退出 Valet Mode 後回到先前之 profile。"
            "關鍵情境條件：以步驟 1 之記錄為基準線（§5.6）。"
            "為什麼這樣切：Valet Mode 期間之偏好處置屬 12.1，"
            "本條只驗退出後之 profile 接續。"),
        kw=["Valet Mode", "exit", "previous Profile", "restore"],
    ),

    "SWE1-HMI-PROF-121": dict(
        title="Pressing elsewhere cancels the Valet PIN entry",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Start the Valet Mode activation so that the PIN entry is "
                   "displayed",
                   "Press another portion of the screen outside the PIN entry",
                   "Read the screen and check that the PIN entry is cancelled"),
        er=steps("The PIN entry is displayed",
                 "The press outside the PIN entry is treated as a cancel "
                 "command",
                 "The PIN entry is closed and Valet Mode is not active"),
        reasoning=(
            "驗證目標：12.4（PVAL4）—— PIN 輸入期間按畫面他處視為取消。"
            "關鍵情境條件：條文涵蓋啟用與停用兩側之 PIN，本條取啟用側；"
            "停用側之取消行為相同，未另切 TC（037 未為其切 leaf）。"
            "為什麼這樣切：ER3 併驗「未進入 Valet Mode」—— "
            "只驗畫面關閉，一個關掉畫面卻已啟用之實作會通過（§7）。"),
        kw=["PIN entry", "cancel", "press elsewhere", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-122": dict(
        title="Lock symbol shown with the Profile icon in Valet Mode",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the Profile icon in the status bar",
                   "Activate Valet Mode",
                   "Read the status bar and check that the lock symbol is "
                   "combined with the Profile icon"),
        er=steps("The Profile icon is shown without a lock symbol",
                 "Valet Mode is active",
                 "The status bar shows a lock symbol combined with the "
                 "Profile icon"),
        reasoning=(
            "驗證目標：12.5（PVAL5）—— Valet Mode 於狀態列以鎖頭圖示結合 Profile 圖示表示。"
            "關鍵情境條件：以啟用前之圖示為基準線（§5.6），"
            "否則「有鎖頭」與「本來就有」分不出。"
            "為什麼這樣切：狀態列之預設版面屬 12.1.1，本條只驗該指示。"),
        kw=["status bar", "lock symbol", "Profile icon", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-123": dict(
        title="Profile button in Valet Mode offers to deactivate",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Profile button in the status bar",
                   "Read the popup and check that it offers to deactivate "
                   "Valet Mode"),
        er=steps("The Profile button is pressed",
                 "A popup indicates “Function not available while in "
                 "Valet Mode. Do you want to deactivate Valet Mode”"),
        reasoning=(
            "驗證目標：12.6（PVAL6）—— Valet Mode 中按狀態列之 Profile 鍵時，"
            "以 popup 告知功能不可用並詢問是否停用。"
            "關鍵情境條件：popup 文字逐字取自條文，含其未加問號之原樣（§8.4.1）。"
            "為什麼這樣切：按下「是」之後續退出流程屬 12.3.1／12.9，本條只驗該提示。"),
        kw=["Profile button", "Valet Mode", "popup", "deactivate"],
    ),

    "SWE1-HMI-PROF-124": dict(
        title="Memory seat buttons move the seat without loading a Profile",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with memory seats",
                  "Driver Profile A is linked to memory seat 1 and its "
                  "position differs from the current seat position",
                  "Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the active Profile and the seat position",
                   "Press the memory seat 1 button",
                   "Read the seat position and the active Profile and check "
                   "that only the seat position changed"),
        er=steps("The active Profile is the Valet Mode Profile and the seat "
                 "position is recorded",
                 "The memory seat 1 button is pressed",
                 "The seat moves to the memory seat 1 position and the "
                 "active Profile is still the Valet Mode Profile"),
        remarks="**來源標示（J-12）**：`memory seat 1` 之編號為測試設置，"
                "條文只說 `the memory seat buttons`",
        reasoning=(
            "驗證目標：12.7（PVAL7）—— Valet Mode 中按記憶座椅鍵只改座椅位置，"
            "不載入其所連之 Driver Profile。"
            "關鍵情境條件：pre-condition 要求該座椅所連 profile 之位置與現況不同，"
            "否則座椅有沒有動看不出來。"
            "為什麼這樣切：失效之後果是 **Valet 使用者載入了車主之 profile**，"
            "即隔離被繞過，故依 D-UP16-01 判 P0。"),
        kw=["memory seat", "Valet Mode", "seat position", "Profile"],
    ),

    "SWE1-HMI-PROF-125-01": dict(
        title="Device Manager locked out inside Media in Valet Mode",
        design=NEGATIVE,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the Media section",
                   "Select Device Manager",
                   "Read the screen and check that Device Manager is locked "
                   "out"),
        er=steps("The Media section is available in Valet Mode",
                 "The Device Manager entry is greyed out",
                 "Device Manager cannot be opened"),
        reasoning=(
            "驗證目標：12.8（PVAL8）之 Media 例外 —— Media 區可用，"
            "惟其中之 Device Manager 被鎖住。"
            "關鍵情境條件：ER1 併驗 Media 本身可用 —— **那是本條之對照組**"
            "（§7）：若整個 Media 都打不開，Device Manager 打不開就沒有意義。"
            "為什麼這樣切：037 為 12.8 切出四個 leaf，本條依其 description 之單位"
            "（Device Manager 之例外）生成；**該 leaf 之標題與描述錯位，見 A-UP11**。"),
        kw=["Device Manager", "Media", "locked out", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-125-02": dict(
        title="Projection, native HFP and VR disabled in Valet Mode",
        design=NEGATIVE,
        pre=steps("A projection-capable device is connected to the head unit",
                  "Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Attempt to start projection mode from the head unit",
                   "Attempt to place a call over native HFP",
                   "Press the voice recognition control",
                   "Open the Media section and check that it is available"),
        er=steps("Projection mode is disabled and does not start",
                 "Native HFP is disabled and no call is placed",
                 "Voice recognition is not active",
                 "The Media section is available"),
        reasoning=(
            "驗證目標：12.8（PVAL8）—— Valet Mode 中 Projection、native HFP 停用，"
            "VR 不啟動。"
            "關鍵情境條件：三者為條文並列之停用項，同一條件下之三個結果，"
            "依 §5.7 併為一條 TC 之三條 ER。"
            "為什麼這樣切：**ER4 為 §7 之對照** —— 以「Media 仍可用」證明"
            "本條測到的是選擇性停用，而非整機不可用。"
            "**未另切負向 TC**：對照置於同一 TC（§5.6），理由見上繳 19 §6。"),
        kw=["Projection", "HFP", "VR", "disabled", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-125-03": dict(
        title="Status bar interaction limited to Valet Profile and HVAC",
        design=NEGATIVE,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press a status bar item other than Valet Profile or "
                   "HVAC",
                   "Read the screen and check that the item does not respond",
                   "Press the HVAC icon in the status bar and check that it "
                   "responds"),
        er=steps("The other status bar item is pressed",
                 "The item does not respond and no screen change occurs",
                 "The HVAC icon responds"),
        reasoning=(
            "驗證目標：12.8（PVAL8）—— Valet Mode 中狀態列不可互動，"
            "**惟 Valet Profile 與 HVAC 圖示為例外**。"
            "關鍵情境條件：ER3 為 §7 之對照 —— 例外項須仍可用，"
            "否則「不可互動」與「整條狀態列壞掉」分不出。"
            "為什麼這樣切：本條依 037 之 description 生成（狀態列互動限制）；"
            "**該 leaf 之標題寫的是手套箱提示，與描述錯位，見 A-UP11**。"),
        kw=["status bar", "interaction", "Valet Profile", "HVAC"],
    ),

    "SWE1-HMI-PROF-125-04": dict(
        title="Non-interactable items greyed out in Valet Mode",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open a screen that contains locked-out items",
                   "Read the locked-out items and check that they are greyed "
                   "out"),
        er=steps("The screen with locked-out items is displayed",
                 "All non-interactable items are greyed out"),
        reasoning=(
            "驗證目標：12.8（PVAL8）末句 —— 所有不可互動之項目一律變灰。"
            "關鍵情境條件：本條驗的是**呈現之一致性**，"
            "不是哪些項目被鎖（那屬 125-01～03）。"
            "為什麼這樣切：依 037 之 description 生成；**標題與描述錯位，見 A-UP11**。"),
        kw=["greyed out", "non interactable", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-126-01": dict(
        title="PU0832 shown when prompting to enter Valet Mode",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with an electronic Glove Box Lock",
                  "Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and press the Valet "
                   "Mode button",
                   "Read the prompt and check that PU0832 is displayed"),
        er=steps("The Valet Mode entry prompt is displayed",
                 "PU0832 informs the user that the glove box will be locked"),
        reasoning=(
            "驗證目標：12.8.1（PVAL8.1）—— 配備電子手套箱鎖之車輛，"
            "在提示進入 Valet Mode 時顯示 PU0832。"
            "關鍵情境條件：車輛配置為條文明列之條件，列 pre-condition。"
            "為什麼這樣切：未配備手套箱鎖之車輛不顯示該提示，"
            "其對照未生成（取樣單位為 leaf，§8.4.2）。"
            "**本條依 037 之 description 生成；標題與描述錯位，見 A-UP11。**"),
        kw=["Glove Box Lock", "PU0832", "Valet Mode", "prompt"],
    ),

    "SWE1-HMI-PROF-126-02": dict(
        title="Glove Box Lock button greyed out while Valet Mode is active",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with an electronic Glove Box Lock",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the Glove Box Lock button before Valet Mode is "
                   "activated",
                   "Activate Valet Mode",
                   "Read the Glove Box Lock button and check that it is "
                   "greyed out"),
        er=steps("The Glove Box Lock button is selectable",
                 "Valet Mode is active",
                 "The Glove Box Lock button is greyed out"),
        reasoning=(
            "驗證目標：12.8.1（PVAL8.1）—— Valet Mode 啟用時手套箱鎖按鈕變灰。"
            "關鍵情境條件：以啟用前可選為基準線（§5.6）。"
            "為什麼這樣切：按下已變灰之按鈕之行為屬 `SWE1-HMI-PROF-126-03`，"
            "本條只驗其變灰。"
            "**判級（P-1，24 包）**：本條驗的是**呈現** —— canon §8.7.4 逐字載"
            "「視覺狀態（greyed-out）**不蘊含**不可操作」，"
            "故「變灰即防線之執行手段」之推論不成立："
            "**一個變灰而按下仍解鎖之實作，本條會通過**。"
            "判 P2，與同形之 `SWE1-HMI-PROF-125-04`（不可互動項變灰）同級；"
            "防護本身由 `SWE1-HMI-PROF-126-03` 之 ER1 承擔。"
            "**依 description 生成 —— description 為需求單位（P-4 之判準），"
            "標題僅為索引；見 A-UP11。**"),
        kw=["Glove Box Lock", "greyed out", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-126-03": dict(
        title="PU0833 shown when the greyed Glove Box Lock button is pressed",
        design=NEGATIVE,
        pre=steps("The vehicle is equipped with an electronic Glove Box Lock",
                  "Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the greyed-out Glove Box Lock button",
                   "Read the screen and check that PU0833 is displayed"),
        er=steps("The press is not accepted and the glove box lock state "
                 "does not change",
                 "PU0833 indicates that the function is not available while "
                 "in Valet Mode"),
        reasoning=(
            "驗證目標：12.8.1（PVAL8.1）末句 —— 按下已變灰之手套箱鎖按鈕時顯示 PU0833。"
            "關鍵情境條件：受測動作為對已變灰項目之按壓（§12 首匹配 → 負向測試）。"
            "為什麼這樣切：ER1 併驗「鎖定狀態未變」——"
            "只驗 popup 出現，一個顯示 popup 卻仍執行動作之實作會通過（§7）。"
            "**判級（P-1，24 包）**：本條之 ER1 即**防護成立本身**"
            "（按下不生效、鎖定狀態未變），依 D-UP16-01 附二判 **P0**；"
            "ER2 之 PU0833 為其呈現，**不因與防線併於一條而拉低判級** ——"
            "一條 TC 之判級取其**核心斷言**，非取其各 ER 之平均"
            "（21 輪之「兩者各半，取中」為誤，24 包 P-1 指出）。"),
        kw=["Glove Box Lock", "PU0833", "greyed out", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-127": dict(
        title="Glove box returns to its previous state after Valet Mode",
        design=STATE,
        pre=steps("The vehicle is equipped with an electronic Glove Box Lock",
                  "The glove box is unlocked",
                  "Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the glove box lock state",
                   "Activate Valet Mode",
                   "Deactivate Valet Mode",
                   "Read the glove box lock state and check that it matches "
                   "the state recorded in step 1"),
        er=steps("The glove box is recorded as unlocked",
                 "Valet Mode is active and the glove box is locked",
                 "Valet Mode is deactivated",
                 "The glove box is unlocked again"),
        reasoning=(
            "驗證目標：12.8.2（PVAL8.2）—— 手套箱於退出 Valet Mode 後回到進入前之狀態。"
            "關鍵情境條件：pre-condition 取「未上鎖」，"
            "使 ER2 之「Valet 中變為上鎖」與 ER4 之「回到未上鎖」皆可觀察；"
            "若進入前即上鎖，整條 TC 之三個狀態相同，什麼都驗不到。"
            "為什麼這樣切：Valet Mode 啟用手套箱鎖之行為屬 12.8.1，本條驗其還原。"),
        kw=["glove box", "restore", "state", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-128-02": dict(
        title="PIN entry blocked during the 30-minute lockout",
        design=NEGATIVE,
        pre=steps("Valet Mode is active and a 4-digit PIN is set",
                  "The vehicle is stationary"),
        data="PIN attempts: 10 incorrect attempts, then a further attempt",
        proc=steps("Open the Valet Mode deactivation screen",
                   "Enter an incorrect 4-digit PIN ten times",
                   "Attempt to enter a PIN again immediately",
                   "Read the screen and check that the PIN entry is not "
                   "accepted"),
        er=steps("The Valet Mode deactivation screen is displayed",
                 "The tenth incorrect attempt cancels the deactivation",
                 "A further PIN entry is attempted",
                 "The PIN entry is not accepted and Valet Mode is still "
                 "active"),
        remarks="鎖定期為 30 分鐘；本 TC 只驗**鎖定生效**（不需等待），"
                "屆滿後之回復屬 128-03（需 30 分鐘等待）",
        reasoning=(
            "驗證目標：12.9（PVAL9）之鎖定側 —— 10 次錯誤後之 30 分鐘內不受理 PIN。"
            "關鍵情境條件：本條刻意只驗「立刻再試不受理」，**不涉時間長度**，"
            "故無須等待 30 分鐘；長度之驗證由 `SWE1-HMI-PROF-128-03`（12.9）承擔。"
            "為什麼這樣切：第 10 次取消本身屬 pilot 之 TC-015（12.9），"
            "本條為其後之狀態。"),
        kw=["lockout", "30 minutes", "PIN", "blocked"],
    ),

    "SWE1-HMI-PROF-128-03": dict(
        title="PIN entry restored after the 30-minute lockout elapses",
        design=BVA,
        pre=steps("Valet Mode is active and a 4-digit PIN is set",
                  "The vehicle is stationary and can remain powered for the "
                  "duration of the test"),
        data="Elapsed time after the tenth incorrect attempt: 29 min, 30 min",
        proc=steps("Enter an incorrect 4-digit PIN ten times to trigger the "
                   "lockout",
                   "Attempt a PIN entry after 29 minutes",
                   "Attempt a PIN entry after 30 minutes",
                   "Enter the correct PIN and check that Valet Mode is no "
                   "longer active"),
        er=steps("The lockout is in effect after the tenth incorrect attempt",
                 "The PIN entry is not accepted at 29 minutes",
                 "The PIN entry is accepted at 30 minutes",
                 "Valet Mode is no longer active"),
        remarks="**執行成本：本 TC 需 30 分鐘等待**（J-8：照寫、不縮時、不刪除）。"
                "縮時屬測試實作之手段（bench 上如何撥時鐘），非 TC 內容之決定；"
                "排程時須計入。",
        reasoning=(
            "驗證目標：12.9（PVAL9）末句 —— 30 分鐘後可再試。"
            "關鍵情境條件：以 29 分（仍鎖定）與 30 分（可再試）構成邊界前後（§5.6）。"
            "**來源標示（J-4）**：ER2「29 分鐘時仍不受理」之權威為 **§5.6 之 BVA "
            "界前基準線**，非條文 —— 12.9 只寫「30 分鐘後可再試」。"
            "為什麼這樣切：鎖定之生效屬 128-02，本條驗其屆滿與計數重置"
            "（ER4 以正確 PIN 成功退出證明計數已重置）。"),
        kw=["lockout", "30 minutes", "elapsed", "PIN", "restored"],
    ),

    "SWE1-HMI-PROF-129": dict(
        title="Go button greyed out until four digits are entered",
        design=NEGATIVE,
        pre=steps("The Valet Mode PIN entry popup is displayed",
                  "The vehicle is stationary"),
        data="PIN digits entered: 3, then 4",
        proc=steps("Enter three digits and read the Go button",
                   "Press the Go button while it is greyed out",
                   "Read the screen and check the tone and the popup",
                   "Enter a fourth digit and read the Go button"),
        er=steps("The Go button is greyed out with three digits entered",
                 "The press is not accepted",
                 "A Bonk tone is played and the popup “PIN must be 4 "
                 "digits” is displayed",
                 "The Go button is available with four digits entered"),
        reasoning=(
            "驗證目標：12.10（PVAL10）—— 未滿 4 碼前 Go 鍵變灰；"
            "此時按下播 Bonk 並顯示指定 popup。"
            "關鍵情境條件：ER4 為對照 —— 輸滿 4 碼後 Go 須可用，"
            "否則「未滿時變灰」與「永遠變灰」分不出（§7）。"
            "**來源標示（J-12）**：3 碼為測試設置（條文只說「未滿 4 碼」）。"
            "為什麼這樣切：兩個結果同屬「未滿 4 碼」此一條件，依 §5.7 併為一條。"),
        kw=["Go button", "greyed out", "4 digits", "Bonk"],
    ),

    "SWE1-HMI-PROF-130": dict(
        title="Numeric buttons greyed out once four digits are entered",
        design=FUNCTIONAL,
        pre=steps("The Valet Mode PIN entry popup is displayed",
                  "The vehicle is stationary"),
        data="PIN digits entered: 4",
        proc=steps("Enter three digits and read the numeric buttons",
                   "Enter a fourth digit",
                   "Read the numeric buttons and check that they are greyed "
                   "out"),
        er=steps("The numeric buttons are available with three digits "
                 "entered",
                 "The fourth digit is entered",
                 "All numeric buttons are greyed out"),
        reasoning=(
            "驗證目標：12.10.1（PVAL10.1）—— 輸滿 4 碼後所有數字鍵變灰。"
            "關鍵情境條件：以 3 碼時可用為基準線（§5.6）。"
            "**來源標示（J-12）**：3 碼為測試設置。"
            "為什麼這樣切：Go 鍵之可用性屬 12.10，本條只管數字鍵。"),
        kw=["numeric buttons", "greyed out", "4 digits", "PIN"],
    ),

    "SWE1-HMI-PROF-131": dict(
        title="SPAAK key activates Valet Mode without a PIN",
        design=FUNCTIONAL,
        pre=steps("A SPAAK key with Valet Mode permissions is available",
                  "Valet Mode is not active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Present the SPAAK key with Valet Mode permissions to the "
                   "vehicle",
                   "Read the screen and check that Valet Mode is active "
                   "without a PIN entry"),
        er=steps("The SPAAK key with Valet Mode permissions is detected",
                 "Valet Mode is active and no PIN entry was requested"),
        reasoning=(
            "驗證目標：13.1（PVALSPK1）—— SPAAK 啟用之 Valet Mode 不需 PIN，"
            "偵測到具 Valet 權限之 SPAAK 鑰匙時自動啟用。"
            "關鍵情境條件：ER2 明寫「未要求 PIN」——"
            "只驗「已啟用」，一個仍要求 PIN 之實作也會通過。"
            "為什麼這樣切：SPAAK 下之退出限制屬 13.2，提示屬 13.3。"),
        kw=["SPAAK", "Valet Mode", "no PIN", "auto activate"],
    ),

    "SWE1-HMI-PROF-132-01": dict(
        title="All head unit Valet exit paths blocked for the SPAAK user",
        design=NEGATIVE,
        pre=steps("Valet Mode is active under the SPAAK scenario",
                  "The user at the head unit is the SPAAK user",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Valet Profile icon in the status bar",
                   "Open the “All Profiles” tab and look for a "
                   "deactivation control",
                   "Read the screen and check that no head unit path exits "
                   "Valet Mode"),
        er=steps("The Valet Profile icon does not open a deactivation flow",
                 "No deactivation control is available on the “All "
                 "Profiles” tab",
                 "Valet Mode is still active and the PU0934 exit popup is "
                 "not shown"),
        remarks="sibling 軸：本條驗**主機各入口皆被阻擋**（窮舉入口）；"
                "pilot 之 TC-016 驗**車主遠端停用可行**（同節之另一 leaf）",
        reasoning=(
            "驗證目標：13.2（PVALSPK2）之阻擋側 —— SPAAK 使用者無法自主機退出。"
            "關鍵情境條件：本條之單位是「**所有**主機路徑」，"
            "故步驟逐一走過狀態列圖示與 All Profiles 分頁兩個入口。"
            "為什麼這樣切：037 為 13.2 切出兩個 leaf —— "
            "本條（阻擋）與 pilot 之 132-02（車主遠端停用）；一葉一 TC（§8.2.1）。"
            "**ER3 之收斂（P-2，24 包）**：原 ER3 為 `any popup that would "
            "allow an exit is blocked` —— **全稱斷言，而 procedure 只走兩個入口**，"
            "測試者無從據以判定通過與否（§6）。"
            "現收斂為 spec 所點名之 `PU0934`（13.2 逐字："
            "`must be blocked (PU0934, etc)`）。"
            "**「所有入口皆被阻擋」之全稱留在此處，不入 ER** —— "
            "條文之 `etc` 本身即表示該集合未列盡，"
            "**spec 沒列盡的東西，ER 不可能驗得完**。"
            "刻意略過：**入口之窮舉不可能完備** —— 取兩個最可能者，已具名。"),
        kw=["SPAAK", "head unit", "exit", "blocked", "Valet Mode"],
    ),

    "SWE1-HMI-PROF-133": dict(
        title="PU1573 shown when the SPAAK user presses the locked icon",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active under the SPAAK scenario",
                  "The user at the head unit is the SPAAK user",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Profiles icon with the lock in the status bar",
                   "Read the screen and check that PU1573 is displayed"),
        er=steps("The Profiles icon with the lock is pressed",
                 "PU1573 is displayed"),
        reasoning=(
            "驗證目標：13.3（PVALSPK3）—— SPAAK 使用者按下帶鎖之 Profiles 圖示時顯示 PU1573。"
            "關鍵情境條件：帶鎖之圖示即 12.5 所述之呈現，本條以其為操作對象。"
            "為什麼這樣切：非 SPAAK 情境下按同一圖示之行為屬 12.6（PU 不同），"
            "兩者之 pre-condition 互斥。"
            "刻意略過：PU1573 之內文未載於 spec，本 TC 只驗其顯示（同 R-U27 之處置）。"),
        kw=["SPAAK", "PU1573", "Profiles icon", "lock"],
    ),

    "SWE1-HMI-PROF-134": dict(
        title="Valet welcome popup indicates Valet Mode with an exit button",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Trigger the welcome popup",
                   "Read the popup and check its Valet indication and "
                   "button",
                   "Press the “Exit Valet Mode” button and check that "
                   "the PIN entry for deactivation is displayed"),
        er=steps("The welcome popup is displayed",
                 "The popup indicates that the vehicle is in Valet mode and "
                 "shows a button to deactivate it",
                 "The 4 digit PIN entry for deactivating Valet Mode is "
                 "displayed"),
        remarks="條文之「the Exit Valet Mode process **above**」其指涉對象"
                "**不在 ch14**（ch14 僅 14.1／14.2，本節即首條）—— "
                "複位後為 **12.3.1**（同一 PIN 退出）與 **12.6**（停用詢問）兩處。"
                "**引用欄只列 12.3.1，不列 12.6（P-3，24 包）**："
                "本 TC 之 procedure 只走 welcome popup 之「Exit Valet Mode」"
                "按鈕這一路，未走狀態列 Profile 鍵那一路，"
                "而 12.6 所述之詢問 popup 屬**後者** —— 其字面值不在本 TC 任何欄位內，"
                "依 J-10 之判準（登記之節其 `provides` 字面值須真的出現）列之即為**多引**。"
                "19 輪之 G17 首跑即以此擋下 12.6，"
                "**而 remarks 當時未同步改，遂與引用欄互相矛盾**。見上繳 19 §4",
        reasoning=(
            "驗證目標：14.1（PVALEX1）—— Valet Mode 中之 welcome popup 須指出"
            "車輛處於 Valet Mode 並提供停用按鈕，按下後進入退出流程。"
            "關鍵情境條件：ER3 之「退出流程」以 12.3.1 之 PIN 輸入為其可觀察形態；"
            "**該指涉之複位為本輪之查證結果**（R-U51 之判讀首次受檢）。"
            "為什麼這樣切：狀態列圖示亦可觸發同一流程（條文並列），"
            "本 TC 取 popup 之按鈕一側；圖示側之觸發屬 12.6 之 leaf。"),
        kw=["welcome popup", "Valet Mode", "Exit Valet Mode", "deactivate"],
    ),

    "SWE1-HMI-PROF-135": dict(
        title="Valet Mode cannot be deactivated while the vehicle moves",
        design=NEGATIVE,
        pre=steps("Valet Mode is active",
                  "The vehicle is stationary on a test track and can be "
                  "brought into motion"),
        data="NA",
        proc=steps("Bring the vehicle into motion",
                   "Attempt to access the Profile section",
                   "Read the screen and check that the unavailability popup "
                   "is displayed and Valet Mode is still active"),
        er=steps("The vehicle is in motion",
                 "The Profile section is not accessible",
                 "PU0394 is displayed and Valet Mode is still active"),
        reasoning=(
            "驗證目標：14.2（PVALEX2）—— 行車中不得停用 Valet Mode；"
            "行車中嘗試進入 Profile 區時顯示 PU0394。"
            "關鍵情境條件：受測動作為行進中之停用嘗試，屬不被允許之操作"
            "（§12 首匹配 → 負向測試）。"
            "為什麼這樣切：ER3 併驗「Valet Mode 仍啟用」——"
            "只驗 popup 出現，一個顯示 popup 卻仍解除之實作會通過（§7）。"
            "**本條之失效後果為行進中 Valet 可被解除** —— "
            "R-U5 之 rubric 無安全帶，依 D-UP16-01 就近判 P0，見上繳 19 §7。"),
        kw=["Valet Mode", "in motion", "deactivate", "PU0394"],
    ),
}


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
        for extra, _prov in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{extra}"
        prio, why = PRIORITY[req_id]
        rec = _rec(req_id, ctx, spec, refs, prio, why, n)
        rec["batch"] = "batch02"
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
