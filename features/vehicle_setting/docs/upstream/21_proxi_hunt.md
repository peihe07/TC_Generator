# 上繳 21 —— PROXI Table 之唯讀搜尋、兩個掃描盲區、batch04

執行層寫入。依據：`docs/handoff/42_review_round22.md` §4。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 逐字轉錄 R-VS45 | ✅ |
| D-3 | 12 筆標型別；DR-22′ 改寫；DR-24 新開 | ✅ |
| D-4 | 依 R-VS35 列兩數 | ✅ 見 §5.1 |
| **W-65** | PROXI Table 唯讀搜尋 | ⚠ **正向升級：找到，惟為他車型** |
| **W-66** | 兩盲區 ＋ 補表過閘 | ⚠ **升級：閘有漏，4 組全數未攔** |
| **W-67** | batch04 生成 | ✅ **10 條，§9 檢查 0 違規** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-65 —— 唯讀搜尋之範圍與餘數（R-G10）

| 項 | 值 |
|---|---:|
| 搜尋根目錄 | `/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement` |
| **總檔數** | **5,304** |
| 主要檔型 | pdf 898／xlsx 684／mcf 538／docx 519／xls 494／dma 466／rtf 360／doc 242／reqifz 221 |
| 頂層目錄 | `CPAA_spec`／`Development Docs`／`R1LR SR26 ATL-H`／`VF` |
| **檔名含 `proxi` 者（全庫）** | **30** —— **全數為他車型**（VF603／DT27／DT28／HDCC27／HDCC28／637MCA／226MCA／363_376） |
| **R1LR 目錄下檔名含 `proxi` 者** | **0** |
| **R1LR 目錄下內容掃描之 xlsx/xlsm/docx** | **264 檔**，命中四參數者 **12 檔** |

**結論：R1LR 之 PROXI Table 不在客戶需求目錄中。**

### 1.2 W-65 —— **但找到了他車型之 PROXI Table，且四參數全數有值域**

`See Proxi Table` 位於 LID `Proxi & Configuration` 分頁之**欄 18**；
**欄 20 為 `VFs`，其值為 `664`**（即 CFTS044 屢見之 `{VF664}`）。

兩份獨立之他車型 PROXI 表，其 `Format` 分頁：

| 參數 | 值域（兩表**逐字一致**） | VF 引用 |
|---|---|---|
| `Cooled_Seats` | `0 = Absent`／`1 = Front Seats`／`2 = Front And Rear Seats`／`3 = Not Used` | `LTM (VF673_V4, **VF664_V2**); ETM (**VF664_V3**, …)` |
| `Heated_Seats` | 同上 | `LTM (VF230_V1, VF673_V4, **VF664_V2**); …` |
| `Heated_Steering_Wheel` | `0 = Absent`／`1 = Present` | `LTM (VF673_V4, **VF664_V2**); …` |
| `Heated_Seat_Levels` | `0 = 1  Level`／`1 = 2 Levels`／`2 = 3 Levels` | **`LTM (VF664_V2); ETM (VF664_V3);`** ← **僅引 VF664** |

**待解之三個值**：`Front Seats` = **1**（逐字命中）／`Present` = **1**（逐字命中）／
`One Level` vs `1  Level`（**需一小步**）。

**⚠ 正向升級條件命中**（「W-65 找到 PROXI Table —— 79 leaf 可解，須立即回報」）。
**本層不採用** —— 見 §2.1。

### 1.3 W-66(1) —— B4 之偵測

| 項 | 值 |
|---|---:|
| 措辭 | `invalid`／`all other states`／`any other value`／`unsupported`／`not defined` |
| **命中之 leaf** | **15** |
| 相異條文 | 15 |
| 措辭分布 | `invalid` 15／`all other states` 10 |
| 已知實例 `4858310`／`4858340` 是否在內 | **是／是** |

**15 ≤ 20 → 「B4 同型總數 > 20」之升級條件未命中。**

### 1.4 W-66(2) —— 時間符號之全量掃描

| 符號 | 出現次數 |
|---|---:|
| `<Tsend>` | **15** |
| **`<Tdisplay>`** | **28** |
| **引用之 leaf（去重）** | **43** |

**`<Tdisplay>` 為 42 包 §3.2 未預期之第二個符號，且引用數近 `Tsend` 之兩倍** → §2.3。

### 1.5 W-66(3) —— 補極性表後之閘測

補入 9 個漏詞之對偶後，**新增 derivable 4 組**（補表前 1 組）：

| token | 值 | leaf | 對偶（全文命中） | **過閘結果** |
|---|---|---:|---|---|
| `FL_HS_RQ` | `Heated Seat Pressed / HS_PSD` | 1 | `heated seat not pressed / …`（0） | **derivable** |
| `FR_HS_RQ` | 同上 | 1 | 同上（0） | **derivable** |
| `FL_VS_RQ_TGW` | `Vented Seat Pressed / VS_PSD` | 1 | `vented seat not pressed / …`（0） | **derivable** |
| `FR_VS_RQ_TGW` | 同上 | 1 | 同上（0） | **derivable** |

**`pressed` 相關者 4 組，被閘攔下 0 組。**
42 包 §3.1 之預期（全數 `DR-CONFLICT`）**不成立** → **⚠ 升級條件命中** → §2.2。

### 1.6 W-67 —— 四個 Layer 2 之穩定核心餘量與配額

| Layer 2 | 餘量 | 配額 |
|---|---:|---:|
| Common Features | 18 | 4 |
| Vented Seat | 14 | 3 |
| Heated Steering Wheel | 12 | 2 |
| Heated Seat | 5 | 1 |
| **合計** | **49** | **10** |

**四者餘量皆非 0 → 「某 Layer 2 穩定核心餘量為 0」之升級條件未命中。**
**每個 Layer 2 至少 1 條**（42 包 §3.3）已滿足。§9 機械檢查 **0 違規**。

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **正向升級：PROXI Table 找到了，但不是 R1LR 的**

**三項佐證指向「同一定義」**：

1. 兩份**獨立**之 PROXI 表（DT27／HDCC27），四參數值域**逐字一致**
2. `Heated_Seat_Levels` **僅引 `VF664`**（`LTM (VF664_V2); ETM (VF664_V3);`），
   而 R1LR LID 之欄 20 逐字為 **`664`**
3. R1LR LID **自身**之 `Heated_Steering_Levels` 有實 Format
   `0 = 1  Level`／`1 = 2 Levels`／`2 = 3 Levels`，
   **與 PROXI 表之 `Heated_Seat_Levels` 形態完全相同**

**但它們是 DT27 與 HDCC27 之表，不是 R1LR 之表。**

**本層不採用。** 跨車型代入是**裁定事項**，且其形態與 `IGN_START → START`
同類 —— **看起來極其顯然**。差別在於本案有三項獨立佐證，而 `IGN_START` 一項也沒有。
**該差別是否足以支持採用，不是執行層能定的。**

**若裁為可採**：79 個 leaf 之阻塞解除，`writable` 由 **91 回升**，
`generatable` 與穩定核心同步回升，**DR-22′ 不必送出**。

**若裁為不可採**：DR-22′ 照送，惟**其提問文可據本輪之發現改寫** ——
不必問「請提供 PROXI Table」，可直接問「R1LR 之這四個參數是否即 VF664_V2 之定義」，
**那是一個是非題，前置時間更短**。

### 2.2 ⚠ **升級：R-VS44 之閘有漏，且漏在它最該擋的地方**

42 包 §3.1 之設計是「以一個已知會撞的輸入去測閘」。**測出來閘沒擋。**

成因：`OPEN_DR["DR-15"]` 之值樣式為 `^\s*(high|low|medium|off)\s*$`，
而 `Heated Seat Pressed / HS_PSD` 不匹配。

**但 DR-15 問的是該訊號之編碼**（1 bit vs 承載階數），
其標的**涵蓋那五個 token 之全部值**，不只 High/Low/Medium。
把 `Pressed` 對映為 `1 (Pressed)` —— **即預設了 1 bit 那個答案**。

**本層之處置**：
- **未採用**該 4 組 derivable
- **未逕自放寬** `DR-15` 之範圍宣告 —— 其為 **DR 範圍之詮釋**，屬分析層
- **修法已具名**：`DR-15` 之值樣式改為 `.`（涵蓋該五 token 之全部值）

> **閘之設計缺陷在於「以值樣式宣告 DR 範圍」** ——
> 有些 DR 問的是**整個訊號**，不是某幾個值。**宣告粒度須容許 token 級。**

### 2.3 ⚠ **`<Tdisplay>` 是第二個時間符號，且比 `<Tsend>` 多用近一倍**

| 符號 | 次數 | DR-24 涵蓋？ |
|---|---:|---|
| `<Tsend>` | 15 | **是** |
| **`<Tdisplay>`** | **28** | **否** |

42 包 §3.2 只以 `<Tsend>` 為訴求。**若照現行提問文送出，答覆只解 15 次引用，
留下 28 次。** 二者同受 canon §8.7.1「門檻須為具體值」之規制。

**提問文之修訂屬分析層**，本層不代擬 → A-VS79。

### 2.4 LID 版本落後兩版 —— 就本輪之四參數無差異，其餘未掃

我方用 **v1_76**（`26PI1.5`），客戶目錄已有 **v1_78**（`26PI2.5`）。

逐欄實測 v1_78 之四參數列：**欄 18 同為 `See Proxi Table`、欄 20 同為 `664`**
—— **就本輪之問題而言，升版無助益**，故 A-VS77 之結論不受影響。

**惟其他 token 是否有差異未掃。** 素材更新屬 Pei，本層不補入 → A-VS80。

### 2.5 `4858516` 之 `$HSW_StatS` 再次出現，本輪未再登記

22 輪 A-VS68 已登記其 `$` 不對稱。本輪 W-67 讀 `4858516`／`4858517` 取
加熱方向盤之有效值時再次遇到，**內容與 A-VS68 所記一致，不重複登記**。
`batch04` 之 `HeatedSteeringWheel-006` 取 `4858517`（三階）之列舉為依據，
**未取 `4858516`**（其 token 名毀損）。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | R-VS45 轉錄；`DATA_REQUESTS.md` **12 筆逐筆標型別**、DR-22 改寫為 **DR-22′（型 B）**、新開 **DR-24**；`generated/batch04.json` **10 條 0 違規**（首次依逐 Layer 2 輪流選 leaf）；A-VS77～80 登記 |
| **核實無誤** | 唯讀搜尋 5,304 檔 ／ R1LR 下 264 檔內容掃描；B4 同型 **15**（≤ 20）；四個 Layer 2 餘量皆非 0；已知實例 `4858310`／`4858340` 皆被 B4 偵測命中 |
| **正確地不動** | **未採用他車型 PROXI 表之值**（跨車型代入屬裁定）；**未複製任何檔案入 `inputs/`**（唯讀）；**未採用 4 組過閘之 derivable**；**未逕自放寬 DR-15 之範圍宣告**；**未代擬 DR-24 之 `<Tdisplay>` 修訂**；**ER 未以 `within <Tsend>` 為通過條件**；v1/v2/v3 保留 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| **W-65 檔名掃描** | `find <root> -type f -iname '*proxi*'`（全庫 5,304 檔），另以 `*664*`、`*R1L*`＋`*config*` 交叉 |
| **W-65 內容掃描** | R1LR 目錄下全部 `.xlsx/.xlsm/.docx`（**264 檔**），以 `zipfile` 讀其 `.xml`／`.rels`（單檔 < 12 MB）後正則 `Cooled_Seats\|Heated_Seat_Levels\|Heated_Steering_Wheel\|Heated_Seats\b\|Proxi Table\|PROXI Table`（不分大小寫） |
| **W-65 之已知界線** | **pdf／xls／doc／rtf／reqifz／mcf／dma 未作內容掃描** —— 僅檔名。其中 pdf 898、xls 494、doc 242 為大宗。**未驗其文字層產出量**（§5a 條 12：抽不到者標「未解析」不猜）。故「不在客戶目錄中」之結論**限於 xlsx/xlsm/docx 之內容 ＋ 全型別之檔名** |
| W-65 PROXI 表之取值 | `Format` 分頁逐列，取同列中 `\d\s*=` 之儲存格為值域、含 `VF664` 之儲存格為 VF 引用 |
| **W-66(1) B4** | `\b(invalid\|all other states\|any other value\|unsupported\|not defined)\b`，不分大小寫，掃 237 leaf 所引條文 |
| **W-66(2) 時間符號** | `&lt;(T[A-Za-z_]*)&gt;\|<(T[A-Za-z_]*)>` —— **須同時匹配 HTML 實體與裸角括號**（docx 文字層中二者並存） |
| **W-66(3) 極性表** | 42 包 §3.1 之 9 詞補入後共 **20 個對映**（含反向）：`right↔left`／`on↔off`／`present↔absent`／`active↔inactive`／`enabled↔disabled`／`pressed→not pressed`／`high↔low`／`start↔stop`／`lock↔unlock`／`true↔false`／`valid↔invalid` |
| W-67 配額 | 比例加權 `round(10 × 餘量 / 總餘量)`，**每個 Layer 2 至少 1**；總數溢出時自最大者減、不足時自「餘量−配額」最大者加；批內依最小 reqid 升冪 |
| W-67 無效值之依據 | 通風座椅取 **`4858363`**（`VS_OFF`／`VS_LO`／`VS_HI`）→ `2 (Vented_seat_medium)` 於二階下無效；加熱方向盤取 **`4858517`**（三階之有效值列舉）→ `7 (SNA)` 不在其內。**未取 `4858516`**（其 token 名 `$HSW_StatS` 毀損，A-VS68） |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS77** | **DR-22′**（俟裁定；若可採則不必送） | PROXI Table 找到但為他車型；三項佐證指向同一定義。⚠ 正向升級 |
| **A-VS78** | — | R-VS44 之閘有漏；DR-15 之範圍以值樣式宣告，涵蓋不到 `Pressed`。⚠ 升級 |
| **A-VS79** | **DR-24**（須併入 `<Tdisplay>`） | 第二個時間符號 `<Tdisplay>`，28 次引用，DR-24 未涵蓋 |
| **A-VS80** | — | LID 落後兩版（v1_76 vs v1_78）；就本輪四參數無差異，其餘未掃 |

**新開 DR：DR-24**（型 A，`<Tsend>` 之具體值，42 包 §3.2 已擬）。
**DR-22 改寫為 DR-22′**（型 B），原文保留加註。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **4**（A-VS77／78／79／80） | **79**（相異編號；最大號 A-VS80，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **1**（DR-24）；另 DR-22 → DR-22′ 改寫 | 未結 **13** |

§5 表列 4 筆，登記簿逐筆核對皆在，**差額 0**。

**分析層側核對（42 包）**：42 包開立 anomaly **0 筆**、DR **1 筆**（DR-24）；
登記簿現有 DR-24 **1 筆**，**差額 0**。

### 5.2 未結 DR 之型別分布（R-VS45，本輪首次標記）

| 型 | DR | 數 |
|---|---|---:|
| **型 A（規格缺陷）** | DR-11／DR-12／DR-14′／DR-15／DR-17／DR-18／DR-19／DR-21／**DR-24** | **9** |
| **型 B（素材缺件）** | DR-8／DR-20／**DR-22′**／DR-23 | **4** |

**型 B 之四筆皆應先做唯讀搜尋**（R-VS45(1)）——
本輪只做了 DR-22′ 之搜尋；**DR-8／DR-20／DR-23 之搜尋未做** → §6-1。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **型 B 之其餘三筆未做唯讀搜尋。**
   R-VS45(1) 令型 B **先搜尋**。本輪只搜了 DR-22′ 之 PROXI Table。
   **DR-20／DR-23（`TLM HMI Document`、未具名之 HMI 需求）與 DR-8
   （完整車型碼對照）未搜。** 其中 **`TLM HMI Document` 影響 17 個 leaf**
   （R-VS17 之 DR-5-B），**若其亦在客戶目錄中，可一併解除。**

2. **W-65 之內容掃描只涵蓋 xlsx/xlsm/docx，未涵蓋 pdf／xls／doc／rtf。**
   後四型於全庫合計 **1,994 檔**（pdf 898／xls 494／doc 242／rtf 360）。
   本層只掃了其**檔名**。
   **故「不在客戶目錄中」之結論有此界線** ——
   PDF 之文字層產出量亦未驗（§5a 條 12 之要求）。

3. **`One Level` vs `1  Level` 之最後一步未定。**
   即使裁定可採他車型之 PROXI 表，`Heated_Seat_Levels` 之待解值
   `One Level` 與表中之 `0 = 1  Level`（**兩個空格**）仍非逐字相同。
   其是否過 **R-VS43** 之三條件（三值域，非二值）**本輪未判**。

4. **batch04 之 `HeatedSteeringWheel-006` 以 `7 (SNA)` 為無效值注入。**
   其依據為 `4858517` 之「All other states shall be considered invalid」，
   而 `SNA` 在 DBC 中是**已定義之編碼**，語意為「訊號不可用」。
   **「不可用」是否等同該條文所指之「invalid state」，本層未經 review 確認。**
   若判為不等同，該條之注入值須改，**而 DBC 之 0–3 已全數為有效值** ——
   屆時其處境與 A-VS76 相同。
