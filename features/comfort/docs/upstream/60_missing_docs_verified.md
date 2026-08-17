# 60 — Comfort HMI / 25 條之依據逐條回溯、七份候選文件之唯讀查證

- 產出層：執行層｜2026-08-16｜對象：分析層
- 對應：`docs/handoff/81_missing_docs_recheck.md`（撰寫中）；**接續上繳 59**
- **未生成 TC、未搬檔至 `inputs/`、未寫回、未改 RD-1 與交付說明。**

---

## 1. 25 條之判定依據與當時之搜尋範圍（R-C30）

**先講可回溯性**：25 條中，依據可事後重算者 **13 條**；依據為「129 節通讀後未見」者
**12 條** —— **通讀不是 pattern，其涵蓋範圍無法事後重算**。這一欄以「不可重算」
如實標示，不補一個看起來像 pattern 的東西上去。

| # | 單位 | 節 | 判定依據 | 當時之搜尋範圍 | 可重算 |
|---|---|---|---|---|---|
| 1 | `001-01` | 2.1 | 條文說 tab 組依配置而定，未給對照 | 129 節逐節通讀 | ✗ |
| 2 | `001-02` | 2.1 | 同上（顯示順序）| 同上 | ✗ |
| 3 | `006-04` | 2.5 | `as displayed in the table` **未指名節次**，全 129 節無該對照表 | **129 節逐節通讀**（上繳 35 §9 已載）| ✗ |
| 4 | `015-04` | 2.11 | 條文之可觀察端在後座，而**無條文說哪些車有後座氣候** | 129 節 | ✗ |
| 5 | `015-05` | 2.11 | 同上 | 129 節 | ✗ |
| 6 | `016-01` | 2.12 | 四模組（C13）**無適用車型之陳述** | 129 節；**未查 CFTS043／MCT** | ✗ |
| 7 | `016-02` | 2.12 | 同上 | 同上 | ✗ |
| 8 | `016-03` | 2.12 | 同上 | 同上 | ✗ |
| 9 | `018-01`…`-06` | 2.12.2 | 硬控循環依四模組，繼承其缺口 | 同上 | ✗ |
| 15 | `019-02` | 2.13 | **「VF HVAC document」不在素材內** | **`inputs/` ＋ `spec-index/`；未搜客戶目錄** | ✓ |
| 16 | `019-03` | 2.13 | 同上 | 同上 | ✓ |
| 17 | `039` | 9.1 | 條文只引入變體，**自身無可觀察量** | 條文閱讀（可重讀）| ✓ |
| 18 | `083` | 14.1 | **「pop-up list」不在素材內** | **`inputs/` ＋ `spec-index/`；未搜客戶目錄** | ✓ |
| 19 | `099` | 14.15 | 「depend on vehicle configuration」之對照不在本 spec | 129 節 | ✗ |
| 20 | `122-02` | 16.16 | `see Climate section` **未指名節次** | 129 節 | ✗ |
| 21 | `116-03` | 16.11 | 同 `015-04`（條文與 2.11 逐字相同）| 129 節 | ✗ |
| 22 | `116-04` | 16.11 | 同上 | 129 節 | ✗ |
| 23 | `129-01`…`-03` | 18.1 | 與 17.1 **逐字相同**，無可寫入 PC 之分辨 | **逐字比對（可重算）** | ✓ |
| 26 | `047` | 10.4 | 條文以 `and available` 設條件，**無節說明何時不可用** | 129 節 | ✗ |

**「文件不在手上」一類共 3 條（`019-02`／`019-03`／`083`）**，其搜尋範圍
**只到 `inputs/` 與 `spec-index/`** —— **從未搜過客戶目錄**。這是本輪之起點。

---

## 2. 七份候選文件之唯讀查證

**共通前提**：以下全為唯讀。未複製、未搬移、未加入 `inputs/`、未列入 `BASELINE.sha256`。

### 2.1 `Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021).xlsx`

| | |
|---|---|
| 是否為所指 | **本 spec 未指向它** —— 它不是任何一條之委派對象，是為 RD-1 問句 9 而查 |
| 相關句 | `Last Mode Table` 工作表 359 列，操作別分區。COMFORT 三見：r14 `From Radio Off (deep sleep or Suspend to RAM) to Radio On｜COMFORT｜Any Screen｜**Return to Comfort Main / Front Comfort Screen**`；r48 `…｜COMFORT｜Any Screen｜**Maintain Mode**`；r77 `…｜COMFORT｜**Return to Front Comfort Tab**`。Logic Reference 欄皆寫 `Comfort HMI Logic & Flow` |
| **餘留** | **它管的是「回到哪個畫面」，不是「設定值留不留」** —— 全表無 fan speed／temperature／seat level 之保持陳述 |

**對 RD-1 問句 9 之影響**：**該問不可全撤，但須改寫** ——
畫面狀態之保持**已有擁有者**（Last Mode Table），
設定值之保持**仍無**。原問句把兩者混在一起問。

### 2.2 `Hard Controls HMI Logic and Flow R1L-R (February 12 2026).pdf`（DR #37）

| | |
|---|---|
| 相關句 | 硬控清單具名列出 `CLIMATE: 1) Auto, 2) AC, 3) Recirc, 4) Front Defrost, 5) Rear Defrost, 6) Temp (driver), 7) Temp (passenger), 8) Fan, 9) Climate off/on 10) Mode`；`HC02.) Rear steering wheel controls layout, **region dependent**`；`H5.) Functionality of power button **changes based on whether vehicle has an integrated climate system**` |
| 是否答 DR #37 | **部分**。它證實**硬控之型態確實隨配置而變**（整合式氣候系統之有無、區域），但**未給逐車型之硬控對照**。`rocker`／`4-way` **0 命中** |
| 餘留 | DR #37 之核心問（各硬控之型態是否逐車型可變）**得到肯定之一半**：可變是確定的，**變成什麼仍未定義** |

### 2.3 `HMI Read Me R1 SR24 Post 1A (September 27 2021).pdf` —— **不是 12.6 所指之 HMI Notes**

`12.6` 之條文（逐字）：

> HVS6. Refer to **HMI Notes** for the details on the Auto Comfort Settings
> options for heated/vented seats.

該 PDF 之內容為**全域慣例**：Disclaimer／Format Key／Acronyms／Terminology／
各顯示器之 Anatomy。搜 `Auto Comfort` **0 命中**。

**判定：不是。** 其首頁另有一句值得記：

> NOTE: All graphics are place holders. **See PDO release for official graphics,
> animations, and layout.** Use HMI logic and flow for all official text strings.

**這一句給了 icon 類三條（`006-04`／`122-02`／`099`）一個具名擁有者：PDO release。**

### 2.4 `HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx` —— **是 11.5 所指者**

`11.5` 條文：`HVS6. Refer to **HMI Settings List** for the details on the
Auto Comfort Settings options for heated/vented seats.`

`Settings` 工作表（1,015 列）之相關句：

```
r107  30    Auto-On Driver
r108  30.1  Heated Seat            Heated_Seat
r109  30.2  Heated Steering Wheel  Heated_Steering_Wheel
r110  30.3  Vented Seat            Vented Seat
r111  31    Auto-On Passenger
r112  31.1  Heated Seat
r113  31.2  Vented Seat
```

**餘留：不為空。** 選項可逐項列出，**且其命名與 11.5 之
「Auto Comfort Settings options for heated/vented seats」對得上**。
另 r536 `18. Seats & Comfort｜This section is not shown when vehicle is not
equipped with comfort controls (heated / vented seats, heated steering wheel)`
—— 與 `099` 有關（見 §4）。

### 2.5 `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` —— **是 14.1 所指者**

`14.1` 條文：`HVACP1.) HVAC pop-ups should follow the **pop-up list**.`

`Main` 工作表之相關列：

```
r52   HVAC            Pop-up when HVAC hard key for Passenger or Driver
                      Temperature is selected.   → Comfort HMI Logic and Flow
r110  Climate Comfort When Climate is set Off using Hard Key and the radio is
                      not in climate screen.
```

**餘留：不為空。** 且 r52 之 Logic Reference 欄**回指 Comfort HMI Logic and Flow**
—— 兩份文件互指，**是同一組需求之兩半**，這是「確為所指」之強證據。

### 2.6 Core HMI Logic and Flow —— **13.4 所指之 `N0` 未能查得，但這不是陰性**

`13.4` 條文：`LS3.) …long press… (See **HMI Core Logic and Flow, requirement N0**.)`

| 來源 | 結果 |
|---|---|
| `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A.xlsx`（169 列）| 搜 `N0` **0 命中**；惟該檔**只有 169 列**，取自 Media 之 REF 夾，**應為部分匯出** |
| `Core HMI Logic and Flow … .pdf`（5.7 MB）| **無文字層**（`pdftotext` 僅得 21 bytes）—— **不可文字搜尋** |

**其他長按條文確在該 export 內**，例如
`PECD3.) Long Press: When long press behavior is applicable, pressing the button
for more than 500ms, will increment/decrement 1 step every 200ms`。

**判定：文件確在手上，且確有長按之可測條文；但 `13.4` 具名之 `N0` 這一條
本輪未查得。** 其未查得之成因是 **PDF 無文字層 ＋ export 疑為部分**，
**不是「該條不存在」**（R-C13）。**上繳 59 §3 說 `010` 之判定「會改變」，
該話說早了 —— 現訂正為「取決於 `N0` 是否即 `PECD3`」，此為文件身分之判斷，
屬分析層。**

### 2.7 CFTS044 —— **文件在手，13.5 之等效基準未見**

`13.5` 條文：`LS4.) A short press… equivalent to a short press of the previous
**4-way rocker hard control** (See **CFTS044**).`

| 查 | 結果 |
|---|---|
| `rocker`／`4-way`／`four way` | **0 命中**（26PI1.5 版，781 KB 文字）|
| `lumbar`／`bolster` | **有**：`1.3.2.1.5 CCDMF Lumbar/Bolster Controls`、`1.3.2.1.6 HU Lumbar/Bolster Controls`，含 `When $VC_VEH_LINE$ = [WS] the CCDMF shall display Seat Control HMI…`、`$CCDMF_LumbarUpDown_P_Req$` 等 |
| 短按之**增量**（13.5 所需者）| **未見** —— 所見皆為訊號之送出與持續，非「一次短按移動多少」|

**餘留：仍為空**（就 13.5 所需之等效基準而言）。
**惟所查者為 26PI1.5 版（2026-03），非 SR24 同期版** —— 版本落差已記。

---

## 3. CFTS043 ＋ Market Config Table 之重查（9 條 ＋ 2 條）

**結論與上繳 59 §4 相同，此處只列數**：

| 題 | 實測 | 判定 |
|---|---|---|
| 氣流模式組（9 條）| CFTS043 有 `$VC_VEH_LINE$ = [637MCA] OR $Country_Code$ = [LATAM related countries] → 5 airflow modes` **4 列，惟 `Scope` = `None`、`Radio` = `R1M, R1H`**；tri-mode 之 PROXI 4 列亦 `Scope` = `None`；**四模組之正面陳述 0 命中** | **不變** |
| tab 組（2 條）| CFTS043 R1L-R tree view `tab`／`Massage`／`heated wheel` **各 0 列**；MCT 8 工作表之資料頁 HVAC 類關鍵詞 **0 命中**（僅 ReadMe 3 句）| **不變** |

**MCT 之正確用途已記**：CFTS043 寫
`*Refer to Market Configuration Table to determine LATAM related countries` ——
**它是國別表，不是配置表**。以 HVAC 關鍵詞掃它會得到一個正確而無用的零。

---

## 4. 判定會改變者 —— 訂正版

| 判定 | 單位／列 | 依據 | 較上繳 59 之變動 |
|---|---|---|---|
| **改變（證據強）** | `SWE1-HVAC-083` | Pop Up List 之 r52／r110，且兩文件互指 | 不變 |
| **改變（證據強）** | `NR1L-ComfortHMI-382`（11.5）| Settings List 之 30／31 節 | 不變 |
| **很可能改變** | `015-04`／`015-05`／`116-03`／`116-04` | CFTS043 之 `$Rear_HVAC_cfg$ = [Present]` 48 列、`Scope`=Yes、`Radio` 含 R1L | 不變 |
| **取決於文件身分** | `NR1L-ComfortHMI-010`（13.4）| `N0` 未查得；PDF 無文字層 | **自「會改變」下修** |
| **取決於文件身分** | `019-02`／`019-03` | VF727 只有訊號層 | 不變 |
| **部分改變** | `099` | Settings List r536 之顯示規則（非配置對照）| 不變 |
| **不改變** | `NR1L-ComfortHMI-383`（12.6，HMI Notes 不存在）、`012`（13.5 等效基準未見）、`006-04`／`122-02`（icon 表未見）、`016`×3／`018`×6、`001-01`／`-02`、`129`×3、`039`、`047` | §2／§3 | 不變 |

---

## 5. RD-1 之哪幾問可撤

| 問 | 阻塞數 | 處置 |
|---|---|---|
| 1 tab 組 | 2 | **維持** |
| 2 氣流模式組 | 9 | **維持，但改寫** —— 改問「`637MCA / LATAM → 5 modes` 何以標為 R1L-R 範圍外，R1L 之模式組由何者決定」。**附上該列之 Scope 與 Radio 欄實測** |
| 3 icon 對照 | 3 | **維持，但收窄** —— 已有具名擁有者（**PDO release**，出自 HMI Read Me 之明文）。改問「請提供載有車型別 recirc／seat icon 之 PDO 釋出件」；我方現有者僅為釋出封面（`PDO Graphics Release` 之文字層 489 字元，內容為 Receiving Organization: Harman 等） |
| 4 後座氣候之有無 | 4 | **可撤（待裁）** —— `$Rear_HVAC_cfg$ = [Present]` 為具名、可引、且在 R1L-R 範圍內；本 pipeline 已有引 CFTS043 為 PC 之前例（`039` 之七條）|
| 5 CFTS043 之車輛群 | 1 | **維持** |
| 6 被委派之文件 | 3 | **拆為二**：`083` **可撤**（Pop Up List 已得）；`019-02`／`-03` **維持但改寫** —— 改問「`VF727 Climate_Controls_2_Zone` 是否即 2.13 所指之 VF HVAC document；若是，MAX A/C 之 on/off **HMI 邏輯**在何處」|
| 7 ch18 對 ch17 | 3 | **維持** |
| 8 AUTO 何時不可用 | 1 | **維持** |
| 9 設定之保持 | 0 | **維持但拆為二** —— **畫面狀態之保持已有擁有者**（Last Mode Table，含三列 COMFORT 之明文）；**設定值之保持仍無**。原問把兩者混為一問 |

**若第 4 問與 `083` 獲裁可撤：26 → 21 條有未答問題，25 → 20 條無任何列。**

---

## 6. 待分析層裁定（同上繳 59 §8，不重複展開）

1. **文件範圍**：Core HMI L&F／HMI Settings List／Pop Up List／VF727／CFTS043／
   Last Mode Table／Hard Controls 是否得作為本交付件之依據 ——
   **R-C1 只定 spec 之基線版本，未定可引用哪些文件**
2. `N0` 是否即 `PECD3`（13.4）
3. VF727 是否即 VF HVAC document（2.13）
4. 版本落差之容忍度：Settings List 有 SR24 與 SR25 兩版、CFTS044 為 26PI 版、
   Hard Controls 為 R1L-R (2026-02)、Last Mode Table 為 SR24 1A (2021)
5. **HMI Notes 確定不存在** —— `383` 之處置是否改為
   「擁有者具名而該文件於本專案不存在」，其措辭與現行 BLOCKED row 不同

**未做**：未生成 TC、未搬任何檔案至 `inputs/`、未改 `BASELINE.sha256`、
未寫回、未改 RD-1 與交付說明。git 未執行。
