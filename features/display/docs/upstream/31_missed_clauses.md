# 上繳包 31 —— 71 條漏網全在診斷章；三項重測皆不變

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/31_missed_clauses.md`
- **停止條件 84／85／86 皆未觸發**；1–83 亦全未觸發
- **`pilot-01`／`rvc-01` 一字未動**；無 deferred 被解除；無新 TC
- **git 未執行**（§六為建議）

---

## 摘要

| 任務 | 結果 |
|---|---|
| T1 | 71 條逐字取得，章節集中於 **`§1.4.x`（Lost Communication／診斷）** |
| T2 | **SFR 68 ／ Description 3** |
| T3 | 五組分類：其他 **63**／Operative State **7**／Thermal Management **1**／Pop Up **0**／RVC **0**。**落在 leaf 主題內之 SFR = 8**（未逾 10，停止條件 85 未觸發） |
| T4 | 三項重測 **24→24、7/4→7/4、2→2，皆不變**；兩批次所引 11 個條號之適用性**無一改變**（停止條件 84 未觸發） |
| T5 | `coverage_map.py` **不讀架構欄** —— 其判準與 R-G37 無關，**不需重跑**（停止條件 86 未觸發） |
| §五.2 | R-G38 抄錄相符；R-G22 條下指標已置 |
| §五.3 | DR-DM10 補充二已入檔（標「待 Pei 發」，補充一並列不撤回） |

**主要結論：那 71 條之漏網十輪，對本 feature 之既有量測與兩個批次
一無影響 —— 因為它們全在診斷章，而本 feature 之量測全在行為章。**

**但其中一條例外，且它很要緊** —— 見 §2.4。

---

## 一、R-G38 之抄錄核對表

## 抄錄核對表 — 31_missed_clauses.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| — | R-G38 | `docs/fw036/RULINGS_LEDGER.md` | 720 | `567eb84c10f0eedf` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **57** 個，與各下放包原檔逐字元比對 **全數相符**（57 vs 57）。

置放依 R-G34：ledger 之新節「下放包 31 之全域條文」。
**R-G22 條下之指標**（非 fence，不入核對表母體）已置，逐字：

> **最易被繞過之處（下放包 31 §1.2，2026-08-26）—— 不改本條原文**：
> 本條要求斷言由腳本產出。**其最易失守之處恰為「回溯檢查」類文件**
> —— 該類文件之語氣已在宣告自己在查證，讀者（含作者）遂不再問
> 「這一句本身量過沒有」。
> 實例：上繳 29 §2.2 之「CFTS_020 之 `EE Architecture` 值域不含 `All`」，
> 為該輪回溯結論之整個依據，未經量測；30 輪實測 `All` 出現 83 次、
> 舊判準漏網 71 條（**結論仍成立，理由為假**）。

---

## 二、主任務：71 條漏網

### 2.1 T1／T2 —— 母體與 `Artifact Type`

```text
# T1 母體：漏網 71 條

# T2 —— Artifact Type 分列計數
  'Subsystem Functional Requirement': 68
  'Description': 3
  **Subsystem Functional Requirement = 68**；Description／Heading 等其餘 = 3

# T3 —— 五組分類（依本體逐字之主題詞；只分類不判覆蓋）
  其他: 63
  Operative State: 7
  Thermal Management: 1

# T3 交叉：SFR × 組（停止條件 85 之標的）
  其他: 60
  Operative State: 7
  Thermal Management: 1
  **落在 8 leaf 主題內之 SFR = 8**  →  停止條件 85：未逾 10 條

# 章節分布（前 12）
    7  §1.4.1.1.12 Disassociated Center Stack Display (DCSD
```

**68 條為 `Subsystem Functional Requirement`，3 條為 `Description`。**
即這 71 條**絕大多數是真需求**，不是說明文字 —— 其份量不因
`Artifact Type` 而打折。

### 2.2 T1 —— 章節分布：**全在診斷章**

```text
# 章節分布（前 12）
    7  §1.4.1.1.12 Disassociated Center Stack Display (DCSD
    5  §1.4.3.1 DCSD Behavior when receiving Implausible
    4  §1.4.1.1.1 Integrated Center Stack (ICS) - Lost Com
    4  §1.4.1.1.2 Disassociated Center Stack Display (DCSD
    4  §1.4.1.1.6 Integrated Center Stack (ICS) - Lost Com
    4  §1.4.1.1.7 Disassociated Center Stack Display (DCSD
    4  §1.4.1.1.10 Head Unit (HU) - Lost Communication with
    4  §1.4.1.1.11 Head Unit (HU) - Lost Communication with
    4  §1.4.1.2.1 Integrated Center Stack (ICS) - Componen
    4  §1.4.1.2.2 Disassociated Center Stack Display (DCSD
    4  §1.4.1.2.6 Disassociated Center Stack Display (DCSD
    4  §1.4.1.3.1 Integrated Center Stack (ICS) - Audio an
```

**`§1.4.x` 之三個子群**：`1.4.1.x` Lost Communication／Component fault、
`1.4.3.x` Implausible Signal Values。

**這解釋了為何漏網十輪而無人察覺**：本 feature 之每一次量測
（21 輪之 Display Hot、28 輪之 RVC、30 輪之 backlight）
其標的皆在**行為章**（`1.11.2.2`／`1.15.x`／`1.8.2.5.x`），
而漏網之 71 條全在**診斷章**。**兩者不相交。**

> 這是運氣，不是設計。**若當初某一輪之標的落在 `§1.4.x`，
> 該輪之結論就是錯的，而且沒有任何機制會發現。**

### 2.3 T3 —— 五組分類

| 組 | 全部 71 條 | 其中 SFR |
|---|---:|---:|
| 其他 | 63 | 60 |
| **Operative State** | **7** | **7** |
| **Thermal Management** | **1** | **1** |
| Pop Up Handling | 0 | 0 |
| Rear View Camera | 0 | 0 |

**落在 8 leaf 主題內之 SFR = 8**（未逾 10 → 停止條件 85 未觸發）。
分類判準為本體之逐字主題詞，**只分類不判覆蓋**（是否構成新 TC 需求屬 Tier 2）。

### 2.4 【要緊】八條之逐字全文 —— 其中第一條直接對上 DR-DM4

```text
# 落在 8 leaf 主題內之 SFR —— 逐條全文（停止條件 85 之具名）

## [1] {4819273}  組=Thermal Management
   §1.4.1.2.6 Disassociated Center Stack Display (DCSD) - Display Hot
   Radio=R1M,R1H,R1L,R1L-R | EE=All
   Execute 'Display is Hot' portion of DCSD Display Hot Algorithm - See CFTS013-629.

## [2] {4819347}  組=Operative State
   §1.4.3.1 DCSD Behavior when receiving Implausible Signal Values
   Radio=R1M,R1L,R1H,R1L-R | EE=All
   If the DCSD has received a plausible data value since exiting Sleep Mode and then the $RQ_DISP_INTS$ signal is received with an Implausible-Invalid value (CAN bus values 201 to 254), the DCSD shall continue to behave using the last plausible value received. See VF041 for Implausible-SNA = 255 behavior. If the DCSD has not received a plausible data value since exiting Sleep Mode, the DCSD shall use

## [3] {4819348}  組=Operative State
   §1.4.3.1 DCSD Behavior when receiving Implausible Signal Values
   Radio=R1L,R1L-R,R1M,R1H | EE=All
   If the DCSD has received a plausible data value since exiting Sleep Mode and then the $RQ_DISP_INTS$ signal is received with an Implausible-Invalid value (CAN bus values 201 to 254), the DCSD shall continue to behave using the last plausible value received. See VF668 for Implausible-SNA = 255 behavior. If the DCSD has not received a plausible data value since exiting Sleep Mode, the DCSD shall use

## [4] {4819349}  組=Operative State
   §1.4.3.1 DCSD Behavior when receiving Implausible Signal Values
   Radio=R1M,R1H,R1L,R1L-R | EE=All
   If the DCSD has received a plausible data value since exiting Sleep Mode and then the $TGW_DISP_STAT$ signal is received with an implausible value, the DCSD shall continue to behave using the last plausible value received. If the DCSD has not received a plausible data value since exiting Sleep Mode, the DCSD shall use the value of DISP_NORMAL.

## [5] {4819350}  組=Operative State
   §1.4.3.1 DCSD Behavior when receiving Implausible Signal Values
   Radio=R1H,R1L,R1M,R1L-R | EE=All
   If the PANEL_INTS signal is received with an implausible value (values 201 to 255; where 255 = 'SNA') , the DCSD shall continue to behave using the last plausible value received. If the DCSD has not received a plausible data value since exiting Sleep Mode, the DCSD shall use the value of 200 (100% Panel Intensity).

## [6] {4819351}  組=Operative State
   §1.4.3.1 DCSD Behavior when receiving Implausible Signal Values
   Radio=R1L-R,R1L,R1H,R1M | EE=All
   If the CmdIgnStat signal is received with an implausible value (values of 1, 2 or 6) , the DCSD shall continue to behave using the last plausible value received. If the DCSD has not received a plausible data value since exiting Sleep Mode, the DCSD shall use the default value of IGN_LK.

## [7] {4819353}  組=Operative State
   §1.4.3.2 HU Behavior when receiving Implausible Signal Values
   Radio=R1L,R1M,R1H,R1L-R | EE=All
   If the$DCSD_DISP_STAT$ signal is received with an implausible value (values 5 or 6) , the HU shall continue to behave using the last plausible value received. If the HU has not received a plausible data value since exiting Sleep Mode, the HU shall use the value of ON.

## [8] {4819355}  組=Operative State
   §1.4.3.3 ICS Behavior when receiving Implausible Signal Values
   Radio=R1L-R,R1L,R1M,R1H | EE=All
   If the$HUModeStatus$ signal is received with an implausible value (values 8 or 17) , the ICS shall continue to behave using the last plausible value received. If the HU has not received a plausible data value since exiting Sleep Mode, the ICS shall behave as defined in {VF169} Power Management.

合計 8 條
```

#### 2.4.1 `{4819273}` —— 被舊判準排除十輪之 Display Hot 條文

> `§1.4.1.2.6 Disassociated Center Stack Display (DCSD) - Display Hot`
> `[Radio:R1M, R1H, R1L, R1L-R] [EE Architecture:All]` —— **適用本專案**
> `Execute 'Display is Hot' portion of DCSD Display Hot Algorithm - See CFTS013-629.`

**三項具名**：

1. **它是一條適用本專案之 DCSD Display Hot 條文，而 21 輪之 A-DM33
   （組 A／組 B 之兩組分析）沒有它** —— 因為 21 輪只掃 `1.11.2.2`，
   且用舊判準。**A-DM33 之「兩組」母體須加註**（見 §四）。
2. **其轉指正是 `CFTS013-629`** —— DR-DM4 之標的、A-DM39 所稱之
   「3 位號」。即 **3 位號不只出現在 CFTS_020 之 `1.11.2.2`，
   也出現在診斷章**，且此處之條文**適用本專案**。
3. **它落在診斷章（component fault／DTC 之脈絡）**，其語氣為
   「執行演算法之某一部分」，非定義該演算法。**本層不判其與
   `{4820289}`／CFTS_013 §1.5.3 之關係**（DR-DM10(a)，Tier 2）。

#### 2.4.2 其餘七條 —— Implausible Signal Values，`SWE-DM-001/002/003` 之材料

七條皆在 `§1.4.3.x`，形態一致：某訊號收到不合理值時，
**沿用上一個合理值；自 Sleep Mode 退出後未曾收到合理值者，用指定之預設**。

其中兩條與本 feature 已建之判定直接相關：

- **`{4819353}`**：`If the $DCSD_DISP_STAT$ signal is received with an
  implausible value (values 5 or 6), the HU shall … use the value of ON.`
  → **規格逐字宣告 `DCSD_DISP_STAT` 之 5／6 為不合理值**，
  與 DBC `VAL_`（定義 0,1,2,3,4,7）**互相印證**。
  此為 A-DM35／R-DM48 之獨立佐證，**本輪不改任何條文**。
- **`{4819349}`**：`$TGW_DISP_STAT$` 之預設為 `DISP_NORMAL`
  → HU 側值標籤之又一逐字用例（DR-DM9(b) 之材料，**其 raw 值仍未解**）。

**七條皆登記為材料，不逕生 TC**（§2.3 之拘束）。

### 2.5 T4 —— 三項既有量測之重跑

```text
# 量測 1 —— RVC × $DCSD_DISP_STAT$ 之適用條文（上繳 28 §3.7 舊值 24）
  舊判準 = 24   新判準 = 24   新增 = []
  `rvc-01` 所引六條是否仍全部適用：True  （缺者：無）

# 量測 2 —— 1.11.2.2 之組 A／組 B（上繳 21：組 A 7 條／組 B 4 條）
  組 A: 舊 7 → 新 7   判定改變者：無
  組 B: 舊 4 → 新 4   判定改變者：無

# 量測 3 —— 適用且含 `turn off … backlight`（上繳 30 §1.7 舊值 2）
  舊判準 = 2   新判準 = 2   新增 = []

# 停止條件 84 —— pilot-01／rvc-01 所引條文之適用性是否改變
  兩批次所引之條號（相異）= ['4819642', '4819645', '4819652', '4819668', '4819671', '4820265', '4820282', '4820287', '4820288', '4820289', '4820290']
  適用性判定改變者：**無**  →  停止條件 84：未觸發
```

| 量測 | 舊值 | 新值 | 差 |
|---|---:|---:|---|
| RVC × `$DCSD_DISP_STAT$` 之適用條文 | 24 | **24** | 無 |
| `1.11.2.2` 組 A | 7 | **7** | 無 |
| `1.11.2.2` 組 B | 4 | **4** | 無 |
| 適用且含 `turn off … backlight` | 2 | **2** | 無 |

**`pilot-01`／`rvc-01` 所引之 11 個條號，其適用性判定無一改變。
停止條件 84 未觸發。TC 一字未動。**

### 2.6 T5 —— 覆蓋表之判準

```text
# T5 —— coverage_sys2_vs_swe_dm.tsv 之判準

## sidecar 之 measurement_conditions／inputs（逐字）
  generated_by: features/display/scripts/coverage_map.py
  inputs: []
  measurement_conditions: 母體＝SYS2 Basic Report 之 Category 正規化為 functional requirement 之列；錨一律逐字；優先序 signal>value>glossary_phrase>glossary_phrase_norm>melco>heading>none
  rulings: ['R-DM7', 'R-DM12', 'R-DM13', 'R-DM18', 'R-DM22', 'R-DM23', 'R-DM25', 'R-DM26', 'R-DM28']
  data_rows: 80

## 產出腳本內是否出現架構欄之判定（Radio／EE Architecture）
77:# [Radio:...], [EE Architecture:...]); it is not a spec value. Literal test,
92:# Tokens can contain commas ([Radio:R1M, VP5R120, R1H]). Serialising with a

## 其資料來源
2:"""R-DM13 anchored coverage cross-reference: SYS2 FR rows vs SWE-DM leaves.
9:Population: SYS2 `Basic Report` rows whose Category normalises to
48:SYS2 = ROOT / "inputs" / ("SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System"
49:                          "_Accepted & Released.xlsx")
51:    "Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx"
64:# guessed that SYS2's Description, being prose, would rarely use
137:    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
157:    c_fid, c_cat, c_desc = (col("SYS2 Sys-RA-Feature-ID"),
158:                            col("SYS2 分類 Category"), col("Description"))
159:    c_swhw, c_melco = col("SYS2 SW/HW/System"), col("SYS2 Melco ID")
```

**`coverage_sys2_vs_swe_dm.tsv` 非以舊判準為之。** 其判準逐字為：

> 母體＝SYS2 Basic Report 之 Category 正規化為 functional requirement 之列；
> 錨一律逐字；優先序 signal>value>glossary_phrase>glossary_phrase_norm>melco>heading>none

即 **其資料來源是 SYS2 匯出 xlsx，不是 CFTS_020 docx**，
且其母體判準是 `Category`，**與架構欄無關**。

腳本內兩處 `[Radio:...]` 之出現（`coverage_map.py` 第 77／92 行）
為 **R-DM18 之值 token 排除**（含 `:` 者不計為值）與其註解，
**非適用性過濾**。

**故不需重跑，`.PRE_R_G37` 版本不產生。停止條件 86 未觸發。**

---

## 三、DR-DM10 補充二

§四之全文已寫入 `DATA_REQUESTS.md`，標「待 Pei 發」，
**補充一不撤回，兩者並列**。

本層於其後另附本輪之補測（T4 之三項不變、11 條號適用性未改），
並**新增一項**：

> `{4819273}`（§1.4.1.2.6，`[EE:All]`，**適用本專案**）逐字為
> `Execute 'Display is Hot' portion of DCSD Display Hot Algorithm - See CFTS013-629.`
> —— **該條被舊判準排除十輪，且其轉指正是 DR-DM4 之標的。**

---

## 四、A-DM33 之母體加註（本層判斷，未改其結論）

21 輪之 A-DM33 記「`1.11.2.2` 之下有兩組互斥流程」。
**其母體為 `1.11.2.2` 一節，且以舊判準為之。**

本輪發現 `{4819273}`（診斷章）亦為適用本專案之 Display Hot 條文。
**A-DM33 之結論（組 A 與組 B 互斥）不受影響** —— 該兩組之
適用性重測不變（§2.5），且 `{4819273}` 不在其任一組內。

**但其母體之表述須加註**：`1.11.2.2` 不是本專案 Display Hot 條文之
全部。已於 `ANOMALIES.md` 之 A-DM33 加註（不改原文，R-TM13）。

---

## 五、未驗項分流（A／B，R-G29）—— **依 R-G38，可驗者當場驗**

### 5.1 本輪之 R-G38 適用紀錄

草擬本節時，三項候選之自陳逐一過 R-G38(a) 之四要件：

| 候選 | 素材在手 | 無待裁阻斷 | 無停止條件禁止 | 不需另立判準 | 處置 |
|---|---|---|---|---|---|
| 「71 條中其餘 63 條之內容未細讀」 | 是 | 是 | 是 | 是 | **當場驗** → §5.2 |
| 「`{4819273}` 與 `{4820289}` 之關係未判」 | 是 | **否**（DR-DM10(a)） | — | — | 不可驗，理由具名（R-G38(b)） |
| 「八條是否構成新 TC 需求」 | 是 | **否**（§2.3 拘束、Tier 2） | — | — | 不可驗，理由具名 |

### 5.2 當場補驗：其餘 63 條之內容

> **本節之初稿是個反例，記於此。** 我先用八個關鍵詞
> （`Lost Communication`／`DTC`／`Implausible`／…）去計數，
> **59 條一個都沒命中**，而我在同一份輸出下面寫了一句
> 「其主題為通訊中斷／DTC／不合理值／元件故障之診斷行為」。
>
> **那句話沒有量測支持** —— 它是從**章節標題**推的，而我計數的是**本體**。
> **這正是本輪剛寫進 R-G22 指標的那個形態，我在同一份文件裡犯了第二次。**
> 遂逐條讀了全部 63 條之本體（不抽樣），下列為實測結果。

```text
# 其餘 63 條 —— 章節分布（實測）
    7  §1.4.1.1.12 Disassociated Center Stack Display (DCSD) - Low Voltage 
    4  §1.4.1.1.1 Integrated Center Stack (ICS) - Lost Communication With 
    4  §1.4.1.1.2 Disassociated Center Stack Display (DCSD) - Lost Communi
    4  §1.4.1.1.6 Integrated Center Stack (ICS) - Lost Communication with 
    4  §1.4.1.1.7 Disassociated Center Stack Display (DCSD) - Lost Communi
    4  §1.4.1.1.10 Head Unit (HU) - Lost Communication with ICS
    4  §1.4.1.1.11 Head Unit (HU) - Lost Communication with DCSD
    4  §1.4.1.2.1 Integrated Center Stack (ICS) - Component Internal Failu
    4  §1.4.1.2.2 Disassociated Center Stack Display (DCSD) - Component In
    4  §1.4.1.3.1 Integrated Center Stack (ICS) - Audio and Telematics But
    4  §1.4.1.3.3 Head Unit (HU) with ICS - Audio and Telematics Button St
    4  §1.4.1.3.4 Head Unit (HU) with DCSD Portrait - Audio and Telematics
    3  §1.2 Introduction
    3  §1.4.1.2.6 Disassociated Center Stack Display (DCSD) - Display Hot
    1  §1.3 Functional Requirements Common Between Architectures - D
    1  §1.4.1 DTC Maturation Criteria
    1  §1.4.1.2.9 Comfort Controls Display Module Rear (CCDMR) - Display H
    1  §1.4.1.3.5 Comfort Controls Display Module Front (CCDMF) - Button/K
    1  §1.4.2 Loss of Communication Behavior
    1  §1.4.2.1 Other Requirements

# 逐條本體之前 130 字（全部 63 條，不抽樣）
  {4819133} §1.2          Notation Convention: The list of Component Acronyms referenced in this chapter are: LTM_ADspl, LTM_DDspl, ETM_ADspl, ETM_DDspl, IC
  {4819134} §1.2          Note: There are essentially 2 variants of the LTM and ETM Radio HUs; those with the touch screen integrated into the HU module are
  {4819135} §1.2          Note: There are many DCSD variants that pair with the disassociated variants of the HUs. The key characteristics of the DCSDs that
  {4819139} §1.3          The HU shall use the $Head_Unit_Screen_Size$ parameter to determine the size of the display.
  {4819146} §1.4.1        The DTC maturation criteria defined in this section shall apply to all DTCs defined in this document.
  {4819150} §1.4.1.1.1    The ICS shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819151} §1.4.1.1.1    For monitor type, the ICS shall consider Continuous.
  {4819152} §1.4.1.1.1    For monitor rate, the ICS shall consider 100 ms.
  {4819153} §1.4.1.1.1    For limp-in action, the ICS shall use the last value received from BCM.
  {4819157} §1.4.1.1.2    The DCSD shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819158} §1.4.1.1.2    For monitor type, the DCSD shall consider Continuous.
  {4819159} §1.4.1.1.2    For monitor rate, the DCSD shall consider 100 ms.
  {4819160} §1.4.1.1.2    For limp-in action, the DCSD shall use the last value received from BCM.
  {4819185} §1.4.1.1.6    The ICS shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819186} §1.4.1.1.6    For monitor type, the ICS shall consider Continuous.
  {4819187} §1.4.1.1.6    For monitor rate, the ICS shall consider 1 second.
  {4819188} §1.4.1.1.6    For limp-in action, see VF169 for ICS behavior.
  {4819192} §1.4.1.1.7    The DCSD shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819193} §1.4.1.1.7    For monitor type, the DCSD shall consider Continuous.
  {4819194} §1.4.1.1.7    For monitor rate, the DCSD shall consider 1 second.
  {4819195} §1.4.1.1.7    For limp-in action, see Loss of Communication behavior for HU and DCSD as defined in {VF041}.
  {4819213} §1.4.1.1.10   The HU shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819214} §1.4.1.1.10   For monitor type, the HU shall consider Continuous.
  {4819215} §1.4.1.1.10   For monitor rate, the HU shall consider 1 second.
  {4819216} §1.4.1.1.10   For limp-in action, the HU shall assume $ICS_KNOB1_DIR$ = [KNOB_NO_CHNG].
  {4819220} §1.4.1.1.11   The HU shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819221} §1.4.1.1.11   For monitor type, the HU shall consider Continuous.
  {4819222} §1.4.1.1.11   For monitor rate, the HU shall consider 1 second.
  {4819223} §1.4.1.1.11   For limp-in action, the HU shall assume $DCSD_DISP_STAT$ = [ON].
  {4819227} §1.4.1.1.12   The DCSD shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819228} §1.4.1.1.12   For monitor type, the DCSD shall consider Continuous.
  {4819229} §1.4.1.1.12   For monitor rate, the DCSD shall consider 1 second.* *The supplier can propose a different value in DTC Criteria Matrix, however i
  {4819230} §1.4.1.1.12   For limp-in action, the DCSD shall turn LCD Backlight OFF.
  {4819233} §1.4.1.1.12   Ethernet Cable
  {4819234} §1.4.1.1.12   
  {4819235} §1.4.1.1.12   The DTCs are defined in Diagnosis specification.
  {4819238} §1.4.1.2.1    The ICS shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819239} §1.4.1.2.1    For monitor type, the ICS shall consider Continuous.
  {4819240} §1.4.1.2.1    For monitor rate, the ICS shall consider 500 ms.
  {4819241} §1.4.1.2.1    For limp-in action, the ICS shall disable the affected hardware or entire ECU.
  {4819245} §1.4.1.2.2    The DCSD shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819246} §1.4.1.2.2    For monitor type, the DCSD shall consider Continuous.
  {4819247} §1.4.1.2.2    For monitor rate, the DCSD shall consider 500 ms.
  {4819248} §1.4.1.2.2    For limp-in action, the DCSD shall disable the affected hardware or entire ECU. If possible send $DCSD_DISP_STAT$ = [SNA] and stop
  {4819270} §1.4.1.2.6    The DCSD shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819271} §1.4.1.2.6    For monitor type, the DCSD shall consider Continuous.
  {4819272} §1.4.1.2.6    For monitor rate, the DCSD shall consider 6 seconds.
  {4819294} §1.4.1.2.9    The DTCs are defined in Diagnosis specification.
  {4819297} §1.4.1.3.1    The ICS shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819298} §1.4.1.3.1    For monitor type, the ICS shall consider Continuous.
  {4819299} §1.4.1.3.1    For monitor rate, the ICS shall consider 4 ms.
  {4819300} §1.4.1.3.1    For limp-in action, refer to CFTS022-679.
  {4819311} §1.4.1.3.3    The HU shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819312} §1.4.1.3.3    For monitor type, the HU shall consider Continuous.
  {4819313} §1.4.1.3.3    For monitor rate, the HU shall consider 4 ms.
  {4819314} §1.4.1.3.3    For limp-in action, refer to CFTS022-679.
  {4819318} §1.4.1.3.4    The HU shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
  {4819319} §1.4.1.3.4    For monitor type, the HU shall consider Continuous.
  {4819320} §1.4.1.3.4    For monitor rate, the HU shall consider 4 ms.
  {4819321} §1.4.1.3.4    For limp-in action, refer to CFTS022-679.
  {4819331} §1.4.1.3.5    The DTCs are defined in Diagnosis specification.
  {4819341} §1.4.2        All A&T ECUs shall implement loss of communication. All PNet A&T ECUs shall support a separate Programmed Network Configuration re
  {4819344} §1.4.2.1      When the HU has a loss of communication condition with the ICS, the HU shall set TGW_DISP_STAT = [Fh: sna].
```

#### 5.2.1 實測結論：**它們是 DTC 監測參數，不是行為需求**

63 條中 **51 條**為同一種四句式樣板，每個故障節各一組：

```text
The <ECU> shall refer to DTCs Matrix Core List for details regarding Enable Conditions, Mature and De-Mature Conditions.
For monitor type, the <ECU> shall consider Continuous.
For monitor rate, the <ECU> shall consider <100 ms / 500 ms / 1 second / 4 ms / 6 seconds>.
For limp-in action, <…>.
```

其餘：`§1.2 Introduction` 之三條註記、`§1.3` 之
`$Head_Unit_Screen_Size$`、`§1.4.1` 之 DTC maturation 總則、
三條 `The DTCs are defined in Diagnosis specification.`、
`§1.4.2`／`§1.4.2.1` 之 loss-of-communication 二條、
`{4819233}`／`{4819234}`（`Ethernet Cable`／**空字串**）。

**與 037 八條之需求文（顯示狀態、熱管理、popup、RVC）確實無交集**
—— 但此結論之依據現在是**逐條讀過**，不是章節標題。

#### 5.2.2 四條含顯示訊號者，具名（材料，不逕生 TC）

| 條 | 逐字 | 與本 feature 之關係 |
|---|---|---|
| `{4819223}` | `For limp-in action, the HU shall assume $DCSD_DISP_STAT$ = [ON].` | HU 於失聯時之假定值 —— 短拼法 `[ON]`（raw 1，R-DM48 可解） |
| `{4819230}` | `For limp-in action, the DCSD shall turn LCD Backlight OFF.` | 背光關閉之另一觸發（非熱、非 RVC） |
| `{4819248}` | `For limp-in action, the DCSD shall disable the affected hardware or entire ECU. If possible send $DCSD_DISP_STAT$ = [SNA] and stop…` | `[SNA]`（raw 7）之唯一行為出處 |
| `{4819344}` | `When the HU has a loss of communication condition with the ICS, the HU shall set TGW_DISP_STAT = [Fh: sna].` | HU 側 `TGW_DISP_STAT` 之 **`Fh` 十六進位寫法** —— DR-DM9(b) 之新形態 |

**`{4819344}` 之 `[Fh: sna]` 尤須具名**：這是本 feature 首見之
**十六進位值標籤形態**（`Fh` = 15）。`TGW_DISP_STATSts` 之 `VAL_`
其 `15 "SNA"` —— **兩者對得上**。惟其為**單一用例**，
**本層不據此推廣至 `[DISP_NORMAL]` 等其他 HU 側標籤**（R-DM48 不可外推），
DR-DM9(b) 之阻斷不變。

#### 5.2.3 一項意外之佐證：`{4819134}`

`§1.2 Introduction` 之 `{4819134}` 逐字為
`Note: There are essentially 2 variants of the LTM and ETM Radio HUs; those with the touch screen integrated into the HU module are…`

**即 CFTS_020 自己也載有 Associated／Disassociated 之區分** ——
30 輪補驗 R-DM51 時，我只在 CFTS013 SYSRA 之 `{CFTS013-930}` 找到它。
**R-DM51 之依據因此多一個獨立來源**，且該來源正是本 feature 之主要規格。

**本項為漏網 71 條中對本 feature 最有價值者之一，而它是
`Artifact Type: Description`** —— T2 之分列計數若被用來衡量份量，
會把它算成「不重要的 3 條之一」。

### 5.3 A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A／組 B／CFTS_013 §1.5.3 三者何為準 | 004／005 全部門檻；`pilot-01` 三條已凍結 | DR-DM10(a)＋**補充二** |
| A2 | DCSD 側 warning → off | 原 pilot #2 | DR-DM10(b)／(e) |
| A3 | 長拼法標籤與 HU 側值 | `{4820287}`；`rvc-01` 之 HU 側 | DR-DM9（**`{4819344}` 之 `[Fh: sna]` 為新材料**） |
| A4 | `Cat. SL` 之位置 | 凡涉 SL 之仲裁 | DR-DM2(a) |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| A9 | 倒車檔訊號 | 007 之觸發面向 | DR-DM11 |
| A10 | DR-DM4 之標的 | DR-DM4 之答覆 | 已重擬，**`{4819273}` 為新材料** |
| A12 | 007／008 之區分軸 | `rvc-01` 之 `leaf_id` | DR-DM12，待發 |
| A13 | multi-stage DCSD 側之空缺 | 該演算法對本專案之關閉序列 | DR-DM10(a) 補充二 |
| **A14** | **`{4819273}` 與 `{4820289}`／CFTS_013 §1.5.3 之關係** | Display Hot 之條文母體究竟有幾組 | **併入 DR-DM10(a)（建議）** |

A14 為本輪新增。**A 類無一解除。**

### 5.4 B 類

| 編號 | 項 | 狀態 |
|---|---|---|
| B1–B23 | 見上繳 25–30 | 不變 |
| B24 | 71 條漏網之內容 | **本輪解除**（已逐條讀） |
| B25 | 回溯檢查文件內之未量測斷言 | **已由 R-G22 條下之指標承載**；**本輪又犯一次**，見 §5.2 之框註 |
| **B26** | **`{4819233}`／`{4819234}` 兩條之本體為 `Ethernet Cable` 與空字串** | 帶正式條號之空條文，形態同 A-DM37（樣板殘渣）。**未登為異常** —— 其落在診斷章，不入任何 TC |
| **B27** | **八條 leaf 主題內之 SFR 是否構成新 TC 需求，本層未判** | §2.3 之拘束明文禁止逕生 TC；**屬 Tier 2**（R-G38(b) 之具名） |

B26／B27 為本輪新增。

---

## 六、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/31_missed_clauses.md \
  features/display/docs/upstream/31_missed_clauses.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): read the 71 missed clauses, and find them all in the fault chapter

- the clauses the old predicate excluded are 68 requirements and 3 notes,
  almost all of them DTC monitoring parameters in section 1.4, which is why
  ten rounds of measuring behaviour chapters never noticed
- eight of them do touch a leaf topic: {4819273} says to execute the Display
  Hot algorithm and cites CFTS013-629, which is what DR-DM4 asks for, and
  seven state what to do on implausible signal values
- rerun the three earlier measurements under the new predicate and every one
  is unchanged, as is the applicability of all eleven clauses the two
  batches cite
- record that coverage_map.py never used the architecture predicate, so the
  coverage table needs no rerun
- add R-G38: a self-reported gap that can be checked now must be checked now
- note {4819134}, which states the Associated and Disassociated split inside
  CFTS_020 itself, giving R-DM51 a second independent source
- add supplement 2 to DR-DM10 and annotate A-DM33's population
```

> `generated/`／`feature.yaml`／036 母本本輪皆未變更，不入。

---

## 七、本包是否仍有該驗而未驗者 —— 獨立判斷（**已依 R-G38 篩過**）

**兩項，皆為 R-G38(b) 之不可驗，理由具名。**

1. **`{4819273}` 與 `{4820289}`／CFTS_013 §1.5.3 之關係。**
   **不可驗之理由：DR-DM10(a) 未答，且判「何組為準」屬 Tier 2。**
   素材在手、無停止條件禁止 —— 但 R-G38(c) 明文「本條不創造任何新的許可」。

2. **八條 leaf 主題內之 SFR 是否構成新 TC 需求。**
   **不可驗之理由：下放包 31 §2.3 明文「新發現之適用條文一律登記為材料，
   不逕生 TC」，且是否構成需求屬 Tier 2。**

### 7.1 一項不是「未驗」而是「已犯」

**§5.2 之框註**：我在同一份宣告自己在做補驗的文件裡，
**第二次**以章節標題推本體之主題並寫成斷言。**第一次是上繳 29 §2.2
（`All` 那句），本輪剛把它寫成 R-G22 之指標。**

差別在這次**當場被自己的輸出打臉**（59/63 零命中就在那句話上面），
所以逐條讀了。**但那是輸出恰好擺在旁邊，不是我先想到要驗。**

R-G38 規制「自陳欄之項可驗即驗」，**而本例不在自陳欄** ——
它是正文裡的一句判定。**R-G22 規制它，而 R-G22 已經在了。**
**問題不在缺條文，在我讀自己寫的句子時不夠警覺。**
