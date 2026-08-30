# 作業 A＋B — SYS2 主鍵對照表（R-ICS43(b)①、R-G41(c)）｜2026-08-30

**表本體**：`docs/reports/17_sys2_master_table.tsv` —— **333 資料列 × 14 欄**（含表頭 334 行）。
產表腳本：`scripts/sys2_master_table_17.py`（唯讀）。

**主鍵是 SYS2 之 333 個資料列，不是 CFTS020 之 2180 個物件。**

---

## §1 【E35 判定點】主鍵列數 —— **333，未觸發**

`Basic Report` 之資料列 **333**（xlsx 列 2–334），與 A-ICS86 相符。

### 1-1 四桶分佈 —— 與 A-ICS86 之 260／42／31／0 **逐項相符**

| 桶 | 實測 | A-ICS86 | 判 |
|---|---|---|---|
| 物件頭（∈ CFTS020 之 2180） | **260** | 260 | 相符 |
| 節標題錨（在 docx 內文但非物件頭）| **42** | 42 | 相符 |
| 來源空白 | **31** | 31 | 相符 |
| 指向他文件 | **0** | 0 | 相符 |

### 1-2 `Category` 分佈（**大小寫已正規化**）

| 類 | 列數 |
|---|---|
| Out of Scope | **123**（原始拼寫二種：`Out of Scope` 116 ＋ `Out of scope` 7）|
| Information | 85 |
| **Functional Requirement** | **80**（`Functional Requirement` 79 ＋ `Functional requirement` 1）|
| Heading | 45 |

**具名**：SYS2 之 `Category` 欄有大小寫不一致（二類各多一種拼寫）。
本表以正規化後計數；若以字面計數則為 116／7 與 79／1。

---

## §2 `tc_coverage` —— 本表之核心欄

| 判 | 列數 | 依據分佈 |
|---|---|---|
| **有** | **35** | 錨命中 31 ＋ 行為等值 4 |
| **部分** | **3** | 行為等值 3 |
| **無** | **295** | — |
| 合計 | **333** | |

### 2-1 `行為等值` 之七筆 —— 逐筆附理由（R-ICS50：不得整批標記）

| 列 | `src_id` | 判 | 理由 |
|---|---|---|---|
| 39 | `4821022` | 有 | b03「Power hardkey pressed while HU screen on」之步驟 1／ER 1 觀察 HU Screen ON 態下 `$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$` = 2 (Normal_mode)，即本條所述之持續發送行為 |
| 209 | `4819637` | 有 | 與 `4821022` 逐字相同之需求（§1.8 對應節），同一觀察即涵蓋 |
| 49 | `4821047` | 有 | b03「Three second period completed after screen off hardkey」驗三秒逾時後 = 0 (Display_off)，即本條之逾時行為 |
| 314 | `4819616` | 有 | b01／b02 之 Stuck button 四條驗 HU 判定實體按鍵卡住與其後續行為，即本條 |
| 184 | `4819558` | **部分** | b03 四條驗「回應」分支（screen on／off × Telematic Power 二態），**未驗「忽略」分支** |
| 190 | `4819571` | **部分** | b03 三條驗 SCREEN OFF 之回應分支，**未驗依 screen priority 忽略之分支** |
| 222 | `4819662` | **部分** | b03「Three second period completed」驗逾時後 DISP_OFF，**未驗 `$CCDMF_RQ_DISP_INTS$` 之 CFTS022-2145 條件分支** |

**判不出者一律 `無`，未以「可能涵蓋」充數。**

### 2-2 【本表最不預期之一列】我方已驗之列中，**14 列為 SYS2 判 `Out of Scope`**

覆蓋列（有＋部分，38 列）之 `Category` 分佈：

| Category | 列數 | 占 38 之比 |
|---|---|---|
| Functional Requirement | 22 | 58% |
| **Out of Scope** | **14** | **37%** |
| Information | 2 | 5% |

那 14 列涵蓋本線之核心 TC（Power hardkey、Knob 1／2、Two buttons、Tbutton 等），
`src_id` 為 `4819560`／`4819561`／`4819572`／`4819582`／`4819583`／`4819584`／
`4821688`／`4821689`／`4821693`~`4821698`。

**且其 `SYS2 MD Feedback` 欄 14／14 全部為空** —— 未載任何 Out of Scope 之理由。
全表 123 個 Out of Scope 列中，**116 列之 Feedback 為空**；
僅 7 列載明理由（如 `Out of scope reason: Responsibility for this functionality lies with DCSD firmware; …`）。

**只登記，不推定** ——「Out of Scope」是對 HW 供應商而言、對 SW 測試而言、
抑或係批次標記之殘留，本包無可判之依據，**不調和**。

---

## §3 四個總數（各附分母）

| 問 | 數 | 分母 | 比 |
|---|---|---|---|
| SYS2 在案且已有 TC 覆蓋 | **38**（有 35 ＋ 部分 3）| 333 | **11.4%** |
| SYS2 在案而**無** TC 覆蓋 | **295** | 333 | **88.6%** |
| **有 TC 覆蓋而不在 SYS2** | **7** | 38（TC 之相異錨）| **18.4%** |

**若只計 `Functional Requirement`（80 列）**：

| 問 | 數 | 比 |
|---|---|---|
| FR 已覆蓋 | **22**（有 19 ＋ 部分 3）| **27.5%** |
| FR 未覆蓋 | **58** | **72.5%** |
| FR 且軸層適用（57 列）之覆蓋 | 22 | **38.6%** |

### 3-1 對帳關係

- 31 條 TC 之 `specification_reference` 共 **65 錨行**、**38 個相異 ObjectID**。
- 38 個相異錨中，**31 個**於 SYS2 之來源欄命中（＝ `錨命中` 之 31 列）；
- **7 個未命中** → 見 §4（E33）。
- 另 7 列由 `行為等值` 判入（4 有 ＋ 3 部分），其 `src_id` 不在 TC 之錨中。
- 故覆蓋列 38 ＝ 錨命中 31 ＋ 行為等值 7；與 §2 之表相符。

---

## §4 【E33 觸發】有 TC 覆蓋而不在 SYS2 者 ＝ **7**

| ObjectID | 文件族 | 涉及之 TC |
|---|---|---|
| `4914956` | **CFTS022** | Stuck button held over 120 s／Button held exactly 120 s |
| `4914957` | CFTS022 | Stuck fault held until de-bounced not-pressed |
| `4914958` | CFTS022 | 同上 |
| `4914974` | CFTS022 | VOLUME knob rotated clock-wise／counter clock-wise |
| `4914975` | CFTS022 | VOLUME knob rotated clock-wise／Three detents rotated clock-wise |
| `4914976` | CFTS022 | VOLUME knob rotated counter clock-wise |
| `4914993` | CFTS022 | Mute hardkey pressed while audio unmuted／muted |

**七者全部屬 CFTS022。** 而本 feature 所綁之 SYS2 匯出檔名為
`SYS2_CFTS_020_DISP_TCH_ICS_20260616_...` —— **是 CFTS020 範圍之匯出**。

**故其結構性含意是**：本主鍵表**在設計上就無法回答 CFTS022 側之覆蓋**，
因為 **repo 內查無 CFTS022 之 SYS2 匯出**。

**依 E33 停下回報**：未作任何範圍判斷，未生成、未改錨。
**執行層不將此逕行解釋為「無問題」** —— 該七條 TC 是否驗了上游未列為在案需求之行為，
取決於 CFTS022 是否另有其 SYS2，而該件不在 repo。**屬範圍事項。**

---

## §5 作業 B — ER 與 `Verification Criteria` 之對照

### 5-1 可對照面

| 面 | 數 |
|---|---|
| 全表 `Verification Criteria` 非空 | **75／333** |
| 覆蓋列（38）中 Criteria 非空 | **22** |
| 覆蓋列中 Criteria 為空 → `不可比` | **16** |

### 5-2 【本節最重之事實】75 列 Criteria 中 **37 列為逐字相同之樣板**

樣板逐字：

> `Check $DCSD_DISP_STAT$ in the external tool. If this is 5 or 6, this should be replaced with last palusible value or ON.`

（原文拼字錯誤 `palusible` 原樣保留。）

該句之內容是 **`$DCSD_DISP_STAT$` 不合理值（5 或 6）之處置**，
即 `CFTS020-4819353`／`4819349` 之需求。**它被逐字貼在 37 個互不相干之列上** ——
包括 Power hardkey、Knob、Stuck button、Enter button 等。

**覆蓋列之 22 個 Criteria 中，20 個是此樣板**；只有 **2 個**是該列專屬之驗證標準。

### 5-3 `er_match` 五類之實數

| 類 | 列數（覆蓋列 38 之內）|
|---|---|
| **我方較寬** | **21** |
| 一致 | **1** |
| 不一致 | 0 |
| 我方較嚴 | 0 |
| 不可比 | 16 |

### 5-4 【E34 觸發】`我方較寬` ＝ 21，非 0

**二種成因，必須分開讀：**

**成因一（20 列）：樣板文所要求之檢查點，我方 31 條一次也沒做。**
樣板要求 `Check $DCSD_DISP_STAT$ in the external tool`；
實測 **31 條之交付欄對 `DCSD_DISP_STAT` 命中 0 次**。
**依字面，這 20 列皆為「我方較寬」。**
但該樣板之內容與該 20 列之需求本體無關（§5-2），
**故此 20 之成因可能在 SYS2 之樣板貼錯，而非我方之缺口 —— 不調和，二讀並呈。**

**成因二（1 列，實質）：列 39 `4821022`。**
其 Criteria 為該列專屬，逐字：

> `* Simulate the condition to make HU Dispaly ON. * Check HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ != [0% Intensity]) by using e…`

（原文拼字錯誤 `Dispaly` 原樣保留。）

實測我方：`$RADIO_B3.RQ_DISP_INTS$` 於 31 條中出現 **6 行**（3 條 TC），
**全部是「screen OFF 之後檢查 = 0 (0 %)」**；
**無任何一條在 HU Screen ON 態檢查 `!= 0%`**。

**即：Criteria 要求之「screen ON 態下亮度非零」這個檢查點，我方確實未做。**
**這一列是實質之驗證缺口。** 依 R-ICS50(c)：**登記，不逕改 ER。**

### 5-5 唯一 `一致` 之列

列 49 `4821047`，Criteria 逐字：

> `* Check "TOUCH SCREEN TO TURN ON" screen times out in the HU logs. * Check HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity]`

我方「Three second period completed after screen off hardkey」ER 3 檢查
`= 0 (Display_off)`、ER 4 檢查 `$RADIO_B3.RQ_DISP_INTS$ = 0 (0 %)` —— **二個檢查點皆有，判一致。**

---

## §6 `Verifiability` 欄之分佈（A-ICS85 之後續）

| 值 | 全表（333）| FR（80）|
|---|---|---|
| `Y` | 75 | **71** |
| `NA` | 8 | 2 |
| 空白 | **250** | 7 |

**FR 之 71／80（89%）被 SYS2 標為可驗證**，而我方只覆蓋 22 列（27.5%）。
`Verifiability = Y` 與 `Verification Criteria` 非空之列數皆為 **75** —— 二者同集合。

---

## §7 下放包未預料之事

1. **§4：那 7 個未命中之錨全屬 CFTS022，而本表所據之 SYS2 是 CFTS020 範圍之匯出。**
   **repo 內查無 CFTS022 之 SYS2** —— 本表結構性地無法回答 CFTS022 側之覆蓋。
2. **§2-2：我方已驗之 38 列中，14 列為 SYS2 判 `Out of Scope`**，
   且其理由欄 14／14 全空（全表 123 個 OoS 中 116 個理由為空）。
3. **§5-2：75 個 Criteria 中 37 個是逐字相同之樣板**，貼在互不相干之列上。
   **這使 R-G41(c) 之對照在 37 列上失去意義。**
4. **§1-2：`Category` 欄有大小寫不一致**（`Out of Scope`／`Out of scope`、
   `Functional Requirement`／`Functional requirement`）。若以字面分桶會多出二類。
5. `Verifiability = Y` 與 `Criteria` 非空為**同一集合**（皆 75 列）——
   二欄實際上是同一個判斷之二面，非獨立資訊。

## §8 已知局限

- `行為等值` 之七筆為人工判，各附一句理由；**其判準未經分析層核可**，
  屬執行層之判斷，可推翻。
- `無` 之 295 列未逐列查其是否可由既有 TC 部分涵蓋 ——
  只在 FR 且軸層適用之 57 列上作過人工判（其餘 276 列為 Heading／Information／
  OoS／軸層不適用，未逐列人工判）。**故 295 為上限、38 為下限。**
- `er_match` 之判定以 Criteria 之文字檢查點與我方 ER 之檢查點逐項比對；
  語意等價而措辭不同者可能被判為「我方較寬」。
- 本表未涵蓋 CFTS022 側（§7-1），故「以 SYS2 為主鍵之覆蓋率」實為
  **「以 CFTS020 之 SYS2 為主鍵」之覆蓋率**。
