# 上繳包 09 —— must-hit 隔離度、G1 門檻之推導與門檻單一來源

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/09_threshold_derivation.md`
- 前一包：[upstream/08_criterion_repair.md](08_criterion_repair.md)
- 執行狀態：**步驟 1–6 全部執行完畢。九條停止條件全未觸發。**
  **零寫回工作簿**；**改狀態 git 零次**；**未修改任何他 feature 之檔案**。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH38 | must-hit 之隔離度三級，結構性連帶須有算式 | 556 | `a5fccf32d6dc67d3` | `a5fccf32d6dc67d3` | 逐字相符 |
| R-PMH39 | G1 門檻改 `1/3` 並附推導；`0.35` 作廢 | 462 | `5d7333930b591c6c` | `5d7333930b591c6c` | 逐字相符 |
| R-PMH40 | 判準門檻之單一來源 | 408 | `c0a3a3cbfc7c711b` | `c0a3a3cbfc7c711b` | 逐字相符 |

---

## 2. 步驟 2 —— G1 改 `1/3`、A6、結構性連帶之算式

### 2.1 六錨點之實跑（`--self-test` → **exit 0**）

```
--- A1 每個 outline 各成一組（29 組） ---
    G1 **FAIL**  組數/leaf = 29/48 = 0.6042 (門檻 <= 1/3 = 0.3333)  ← 指定 FAIL ✅
    G2 **FAIL**  min(組規模) = 1 (門檻 >= 2)  ← **結構性連帶**（算式可推）
    G3 PASS      收容簇命中 = 無
    G4 PASS      max/leaf = 5/48 = 0.1042 (門檻 <= 1/2 = 0.5)
    G5 **FAIL**  逸出 [2, 24] = [1 ×21]  ← **結構性連帶**（算式可推）
    隔離度：**結構性連帶** ['G2', 'G5']
        G2 之算式：鴿籠：k=29 > floor(n/2)=24 ⇒ 每組規模 >= 2 須 n >= 2k = 58 > n = 48，故必有單 leaf 組
        G5 之算式：（同上）；該單 leaf 組必逸出 [2, 24]

--- A2 每個 leaf 各成一組（48 組） ---
    G1 **FAIL**  1.0000 > 0.3333   ← 指定 FAIL ✅
    G2 **FAIL**  min = 1           ← 指定 FAIL ✅
    G5 **FAIL**  全部逸出           ← **結構性連帶**（算式可推）
    隔離度：**結構性連帶** ['G5']
        G5 之算式：鴿籠：k=48 > floor(n/2)=24 ⇒ n >= 2k = 96 > n = 48，故必有單 leaf 組；該單 leaf 組必逸出 [2, 24]

--- A3 Off Road Plus 拆為三個單 leaf 組（10 組） ---
    G2 **FAIL**  min = 1                  ← 指定 FAIL ✅
    G5 **FAIL**  逸出 [2,24] = [1, 1, 1]  ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

--- A4 新增一組名為 Misc（2 leaf，以隔離 G3）（9 組） ---
    G3 **FAIL**  收容簇命中 = ['Misc']    ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

--- A5 八組併為一組（1 組） ---
    G4 **FAIL**  48/48 = 1.0000 > 0.5     ← 指定 FAIL ✅
    G5 **FAIL**  逸出 [2,24] = [48]       ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

--- A6 48 leaf 分 20 組（8×3 + 12×2）—— G1 之隔離錨點（20 組） ---
    G1 **FAIL**  組數/leaf = 20/48 = 0.4167 (門檻 <= 1/3 = 0.3333)  ← 指定 FAIL ✅
    G2 PASS      min(組規模) = 2 (門檻 >= 2)
    G3 PASS      收容簇命中 = 無 (門檻 = 零命中)
    G4 PASS      max/leaf = 3/48 = 0.0625 (門檻 <= 1/2 = 0.5)
    G5 PASS      逸出 [2, 24] 之組規模 = 無 (實測區間 [2, 3])
    隔離度：**隔離**（僅指定判準 FAIL）
```

**A6 使 G1 單獨 FAIL，G2/G3/G4/G5 全 PASS —— 停止條件 7 未觸發。**
**六錨點之指定判準全部如期 FAIL —— 停止條件 8 之前半未觸發。**

### 2.2 隔離度總表（R-PMH38 三級）

| 錨點 | 隔離度 | 連帶 | 算式 |
|---|---|---|---|
| A1 | **結構性連帶** | G2、G5 | `k=29 > floor(48/2)=24`，`2k=58 > 48` |
| A2 | **結構性連帶** | G5 | `k=48 > 24`，`2k=96 > 48` |
| A3 | **隔離** | — | — |
| A4 | **隔離** | — | — |
| A5 | **隔離** | — | — |
| **A6** | **隔離** | — | — |

**每一判準之錨點覆蓋**（R-PMH38 末段：無「隔離」或「結構性連帶」錨點者
須標「未實測」）：

| 判準 | 支持之錨點 | 級別 | 是否須標「未實測」 |
|---|---|---|---|
| **G1** | **A6** | **隔離** | **否** ← 08 包之缺口已補 |
| G2 | A3 | 隔離 | 否 |
| G3 | A4 | 隔離 | 否 |
| G4 | A5 | 隔離 | 否 |
| G5 | A3、A5 | 隔離 | 否 |

**五項判準全部有隔離錨點，無一須標「未實測」。**

### 2.3 A1／A2 之連帶已由**程式算式**判定，非文字論述

`structural_collateral()` 以鴿籠原理計算：`k > floor(n/2)` ⇒ G2、G5 必 FAIL。
**08 包 §7 第 3 項自陳「只被論述、未被證明」之缺口已補** ——
該判定現由程式輸出，且錨點之隔離度若出現「無算式可推之連帶」，
程式會判該錨點 **未隔離** 並回傳失敗。

### 2.4 範圍向（R-G9，`1/3` 門檻下）

```
--- 現行提案（8 組） ---
    G1 PASS      組數/leaf = 8/48 = 0.1667 (門檻 <= 1/3 = 0.3333)
    G2 PASS      min(組規模) = 3 (門檻 >= 2)
    G3 PASS      收容簇命中 = 無 (門檻 = 零命中)
    G4 PASS      max/leaf = 9/48 = 0.1875 (門檻 <= 1/2 = 0.5)
    G5 PASS      逸出 [2, 24] 之組規模 = 無 (實測區間 [3, 9])
    範圍向 PASS ✅
```

**停止條件 8 之後半未觸發。** G1 之餘裕為 2 倍（`0.1667` vs `0.3333`）。

---

## 3. 步驟 3 —— 門檻單一來源（R-PMH40）：**採「`--emit-thresholds` ＋ 程式 SHA256」**

二擇一中採**前者**（輸出門檻表供文件貼入），理由：一致性檢查需要
「文件中之數值」有可解析之結構，而 `framework.md` 之門檻散在敘述句中；
由程式產出整張表則**文件不再持有獨立副本**，從根上消除分岔。

**實施**：`check_granularity.py` 新增 `THRESHOLDS` 常數（**唯一來源**）
與 `--emit-thresholds`。`evaluate()` 亦改讀該常數，**判準與門檻表同源**。

**驗證輸出**（`python scripts/check_granularity.py --emit-thresholds`）：

| id | 量 | 關係 | 門檻 | 來源 |
|---|---|:--:|---|---|
| **G1** | 組數 / leaf | `<=` | **`1/3`** | canon §4.1.3 決策測試之平均意義：平均每組不足 3 個 leaf 時，過濾結果多為 1–2 列，索引價值與逐條列舉無異（R-PMH39） |
| **G2** | min(組規模) | `>=` | **`2`** | canon §4.1.3「不是一條」之單組下限 —— 至少兩個才成組 |
| **G3** | 組名命中收容簇清單之數 | `==` | **`0`** | 收容簇清單 `['general', 'misc', 'other', 'unclassified', '雜項']`；全字比對、大小寫不敏感 |
| **G4** | max(組規模) / leaf | `<=` | **`1/2`** | canon §4.1.3「不是整本」—— 單組不得吃掉過半 |
| **G5** | 逸出 `[2, floor(leaf/2)]` 之組規模數 | `==` | **`0`** | G2 之下限與 G4 之上限所夾之區間，逐組適用 |

`framework.md` 之門檻節即由此輸出貼入，並附**產生時之程式 SHA256**。
**程式一改而文件未重貼，SHA256 即對不上** —— 該不一致因而可見。

> **本方式之限制須明說**：SHA256 之比對目前**須人工執行**
> （文件中記著一個雜湊，沒有任何程式會去驗它）。
> **這仍是「宣告」而非「檢查」** —— 與 08 §7 第 4 項所指之形態同族，
> 只是把分岔從「兩份數值」縮為「一個雜湊」。**列為未竟事項（§7 第 1 項）。**

---

## 4. 步驟 4 —— `Test Set` 欄之機器檢索（清償 08 §7 第 1 項）

**量測範圍**：母體 16 交付夾（平手取 `_Rebuilt`），**3,023 資料列**；
`Test Set` 欄以表頭文字 `test set` 精確定位，**16/16 皆為 `H` 欄**。**唯讀。**

| 標的 | 命中 | 複核 |
|---|---:|---|
| `OFF2` | 0 | — |
| `off road` | **1** | **本 feature 自身**之草稿列 —— 其 H 欄為 037 之 `Requirement Title`（R-PMH5 之機械搬運），值為 `Wake Up Prevention in Off Road State`。**是來源自身，不是覆蓋。** |
| `Off Road+` | 0 | — |
| `Power Off State` | **5** | 全部為本 feature 自身之草稿列（`Backup Camera Display in Power Off State`／`HVAC Pop-ups Display in Power Off State`／`Display Phone Call Popups over Power Off State`／`Return to Power Off State Post-Call`／`Return to Power Off State on Call Ignore`） |
| `launch` | **2** | 1 為本 feature 之 `Head Unit Muted on App Launch from Power Off`；1 為 MBAD 之 **`Launch/Exit`**（app 啟動/退出，與 power moding 無關） |
| `hard control` | 0 | — |
| `CFTS009` | **1** | 本 feature 自身之草稿列，值為 **`CFTS009 Behavior Reference`** —— 即 `-028` 之 037 `Requirement Title` |

**他 feature 之真命中：0。** **停止條件 9 未觸發。**

### 4.1 全數 166 個相異 Test Set 之人工核對

母體 15 個有內容交付件之 `Test Set` 相異值共 **166** 個，已全數列出核對。
**除本 feature 自身之草稿列外，無任一他 feature 之 Test Set 與
Off Road+ power moding 相關。** 最接近者為 MBAD 之 `Launch/Exit`
與 Power Management 之 `Power Down`／`Power State`，經檢視皆非本標的。

### 4.2 更新後之盲區聲明（R-PMH34(c)）

已檢索欄位增為 **11 欄**（07 之 7 欄 ＋ 08 之 3 欄 ＋ **09 之 `Test Set`**）。

**08 §7 第 1 項所指之「最大盲區」已關閉。** 仍未及者：
`No.#`／`Requirement or Design ID (Polarion)`／`Test Case ID (TestRail)`／
`Input Test Data`／`Estimated Test Time`／`Functional Safety`／七個車型欄／
`Test Version`～`Defect ID`。**其中 `Input Test Data` 為現存最大者**
（若某 TC 以輸入資料描述 Off Road 情境而未在其他欄提及），
惟該欄之語意為輸入值而非行為描述，命中機率低。

---

## 5. 步驟 5 —— profile 備料（唯讀，**未撰寫本 feature 之 profile**）

### 5.1 檔名清單與行數（`docs/runtime/profiles/`，10 個 profile ＋ 1 個整合說明）

| 檔 | 行數 | `[OVERRIDE]` | `[ADD]` |
|---|---:|---:|---:|
| `FW036_R1L_Home_Profile.md` | 143 | 5 | 10 |
| `FW036_R1L_VehicleSetting_Profile.md` | 163 | 3 | 6 |
| `FW036_R1L_BT_Profile.md` | 179 | 6 | 10 |
| `FW036_R1L_AMFM_Profile.md` | 217 | 5 | 9 |
| `FW036_R1L_SXM_Profile.md` | 268 | 5 | 11 |
| `FW036_R1L_Power_Profile.md` | 285 | 3 | 22 |
| `FW036_R1L_Privacy_Profile.md` | 478 | 5 | 17 |
| `FW036_R1L_UserProfiles_Profile.md` | 531 | 5 | 24 |
| `FW036_R1L_Projection_Profile.md` | 707 | 3 | 12 |
| `FW036_R1L_Comfort_Profile.md` | 1466 | 5 | 20 |
| （`PROFILE_INTEGRATION.md`） | 100 | — | — |

**中位數 276 行**；`[OVERRIDE]` 3–6 個、`[ADD]` 6–24 個。

### 5.2 節結構 —— **八個之中有六個共用同一骨架**

`AMFM`／`BT`／`Home`／`Privacy`／`SXM`／`UserProfiles`（另 `Comfort`／`Power`
為其擴充）採同一骨架：

```
# Project Profile — FW036 / R1L SWE1 {FEATURE} ({來源規格}, {平台})
## 0. Project identity [ADD]
   ### 0.1 Template preparation state [ADD]        （部分檔有）
## 1. Requirements authority chain [ADD]
   ### 1.1 {feature 專屬之權威補充}                 （部分檔有）
## 2. Test Set vocabulary [OVERRIDE — replaces …]
## 3. FW036 {FEATURE} house style (field rules)
   ### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]
   ### 3.2 Pre-Conditions [ADD — {feature} applicability triggers]
   ### 3.3 Design Method [OVERRIDE — restricts §12 output strings]
   ### 3.4 Signal / CAN citations [ADD]
   ### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]
   ### 3.6 Remarks [ADD]
   ### 3.7 Estimated Test Time (column Q) [ADD]     （Privacy／SXM 有）
## 4. Split policy [ADD]
## 5. {FEATURE} step-writing conventions [ADD]
## 6. Known anomalies register [ADD]
```

**兩個例外**：`Projection`（以 `## N. [MARKER] 主旨` 為節名，標記在前）與
`VehicleSetting`（**全檔皆為 `## [MARKER §n] 主旨`，無 0–6 之編號骨架**，
且末節為「未寫入本檔者（即依 canon 通則）」—— **一個明示的否定清單**）。

### 5.3 `[OVERRIDE]`／`[ADD]` 之寫法（186 個標記之實測）

| 形態 | 數 | 例 |
|---|---:|---|
| `[X]` 無尾綴 | **135** | `## 0. Project identity [ADD]` |
| `[X — 說明]` 破折號接說明 | **48** | `[OVERRIDE — replaces §4.3 tc_title-only cell content]` |
| `[X §n]` 直接接節號 | 3 | `## [OVERRIDE §11] test_item 上半段之方括號 token 予以保留` |

**引用 canon 節號之格式**：一律 `§{數字}[.{數字}]`，**無空格**。
標記內所引之節號分布：`§12`(8)／`§10.7`(6)／`§4.3`(5)／`§11`(3)／
`§10.2`(1)／`§4.1.3`(1)／`§4.2`(1)／`§8.7.5`(1)。

> **與本 feature 相關之觀察（不提案）**：`§4.2` 僅被引用 **1 次**
> （`VehicleSetting` 之 `[OVERRIDE §4.1.3／§4.2] Layer 2 = Common Features
> 之粗粒度`）。**本 feature 之 R-PMH36 亦為 §4.2 之例外**，
> 其形態與該前例相同（皆為 profile 層之 `[OVERRIDE §4.2]`），
> 惟 R-PMH36 已明載「不得外推、不得作為一般性放寬」，
> 而 VehicleSetting 之該條未見同等限定。

### 5.4 `PROFILE_INTEGRATION.md` 之結構

`## Files`／`## Activation (FW036 batch)`／`## Changes applied`／
`## Deliberately NOT changed`／`## Verification`／`## Residual watch items`
—— **六節，其中「Deliberately NOT changed」為明示之否定清單**，
與 `VehicleSetting` 末節同一形態。

**本 feature 之 profile 尚未撰寫**（`FW036_R1L_PowerModing_Profile.md` 不存在）。
其草擬屬分析層，Pei 核可。

---

## 6. 步驟 6 —— `framework.md` 之更新

- **門檻節改由 `--emit-thresholds` 產出並附程式 SHA256**（R-PMH40）；
- G1 之門檻改 `1/3` 並記其推導與 `0.35` 之作廢理由（R-PMH39）；
- **六錨點表**（含 A6）與其隔離度三級（R-PMH38），A1／A2 之算式逐字列出；
- 新增「**每一判準之錨點覆蓋**」段，證明無一須標「未實測」；
- Q11 無鑑別力節保留並更新為「已由 R-PMH36 定案，**惟不得引本判準為理由**」。

### 6.1 ⚠ 順帶修正一處 08a 之未命中替換 —— **我的缺陷**

`framework.md` 第 79 行仍為
`### ⚠ Test Set #2 之命名待裁（Q11，**阻斷 Layer 2 定版**）`。

**成因**：08a 步驟 8 中，我先把全檔之 `<PENDING Q11>` 換成
`Disclaimer Screen`，**再**去替換該節（其原文含 `<PENDING Q11>`）——
第二個 `.replace()` 因目標字串已被第一步改掉而**靜默未命中**，
而我**未驗證替換結果**。

08a 之上繳 §11.3(a) 稱「三處 `<PENDING Q11>` → `Disclaimer Screen`，殘留 0」
—— **該陳述本身正確**（佔位符確實清零），但**該節之標題與內文仍是舊的**，
我當時只驗了佔位符數而未驗節標題。

**已於本包修正**該節為
`### Test Set #2 之命名 —— **已定案**（R-PMH36，見本節首）`。

**教訓**：`str.replace()` 無命中時不報錯。**凡替換皆須驗其命中數**
—— 與 A-PMH08（子字串法靜默誤命中）同族，方向相反：一個是**誤命中**，
一個是**未命中**，兩者都不會報錯。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **R-PMH40 之落實仍是「宣告」而非「檢查」**（§3 末段自陳）。
   文件記著程式之 SHA256，**但沒有任何程式會去驗它** ——
   程式改而文件未重貼，仍須人工發現。**分岔由「兩份數值」縮為「一個雜湊」，
   但未消除。** 徹底之作法是加一個檢查（讀文件中之雜湊、比對程式現值），
   本包未做。

2. **`.replace()` 未驗命中數之問題只修了這一處。** §6.1 所述之形態
   （替換靜默未命中）在本 feature 之歷次作業中可能還有 ——
   **本包未回頭掃描前八包所做之全部就地替換**。

3. **`Test Set` 欄之檢索用了與前兩輪相同的七組檢索式。**
   若某 feature 之 Test Set 名為 `Terrain Mode`／`Trail`／`4x4` 之類
   而不含 `off road` 字樣，仍看不到。**166 個相異值已全數人工核對**，
   此項之殘餘風險低，但**「人工核對」不可重跑**。

4. **profile 備料未讀各 profile 之**內容**，只讀其結構。**
   §5 所報為節名、標記形態、行數與引用格式；
   **各節之實際規則內容（例如 `Test Item` 之兩段式怎麼寫）未摘要** ——
   若分析層草擬 profile 時需要那些內容，須另行一輪。

5. **A6 之構造未驗其「符合 R-PMH39 §3.2 所述之組態」。**
   R-PMH39 稱該組態為「48 leaf 分 20 組，每組 2–3」，
   我的 A6 為 8 組 ×3 ＋ 12 組 ×2 = 24 + 24 = 48 ✅，
   **但這只是諸多滿足該描述之組態之一** —— 我未驗是否所有此類組態
   皆使 G1 單獨 FAIL（雖由算式可知 `20/48` 固定，故 G1 必 FAIL；
   而 G2/G4/G5 之通過則依賴「每組 2–3」之限定）。**未寫成一般性證明。**

---

## 8. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— profile 只備料未撰寫 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | A6 未使 G1 單獨 FAIL | **未觸發** —— G1 FAIL 而 G2/G3/G4/G5 **全 PASS** |
| 8 | 六錨點有任一指定判準未 FAIL，或範圍向有任一 FAIL | **未觸發** —— 六錨點全 FAIL 其指定判準；範圍向 G1–G5 全 PASS |
| 9 | `Test Set` 欄檢索發現他 feature 有 Off Road 相關 Test Set | **未觸發** —— 他 feature 真命中 **0**；166 個相異值已全數核對 |

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

> ⚠ **08 包亦尚未提交。** 下列 pathspec **含 08＋08a＋09** 三包之檔案。
> **R-PMH37 已用畢失效，本次提交尚未授權**（09 §七第 2 列）。

```
feat(power_moding): packages 08-09 — granularity criteria repaired, layer 2 finalized, thresholds derived
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/PLAYBOOK.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/framework.md \
           features/power_moding/scripts/check_granularity.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/08_criterion_repair.md \
           features/power_moding/docs/handoff/08a_q11_and_git.md \
           features/power_moding/docs/handoff/09_threshold_derivation.md \
           features/power_moding/docs/upstream/08_criterion_repair.md \
           features/power_moding/docs/upstream/09_threshold_derivation.md
```

- **未觸及任何他 feature 之檔案**（禁止項）。
- `scripts/new_feature.py` 未改（禁止項仍在）。
- pathspec 逐項寫全名（R-PMH3(c)）。

### 9.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

---

## 10. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **A-PMH13** | `-028` 之處置 —— **Phase 4 之唯一前置**。分析層提案 (ii)＋(iii) 併行；現成前例為 Comfort 之 `[BLOCKED-SPEC] Owner: {CFTS}`。**本輪另查得**：該 leaf 之 037 `Requirement Title` 逐字為 **`CFTS009 Behavior Reference`** —— 上游自己就把它命名為「參照」 | **是**（首批可先行，不含 `-028`） |
| **08／09 之 commit 授權** | R-PMH37 已用畢。**是否逐包窄口授權，或改為常規授權** | 否 |
| **§7 第 1 項** | R-PMH40 之落實仍是宣告而非檢查 —— 是否加一致性檢查 | 否 |
| Q10 | `Product Document 記錄封面頁`（提案不填） | 否，Phase 7 前 |
| — | profile `FW036_R1L_PowerModing_Profile.md` 尚未撰寫；§5 已備料（骨架、標記形態、引用格式） | Phase 4 前 |
