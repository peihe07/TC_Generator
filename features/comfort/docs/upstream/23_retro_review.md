# 23 — Comfort HMI / 回溯複查：既有 31 條，補出 18 行 PC

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 34
- 結果：**31 條中 18 條須補 PC**（Tri-Mode Climate 全部 17 ＋ pilot 之 `-003`）。
  補行不重寫內容、不改 tc_id。`-045` 拆為二條（**後續無條需順移**）。
  lint **37/37 PASS，0 finding，46 條**。**未寫回。**

---

## 1. 回溯複查 —— 實質問句施於 31 條

問句（34 §1.1）：

```
在哪一種車輛配置下，這條 TC 沒有可操作的對象？
```

### 1.1 結果

| 批 | 條數 | 須補 | tc_id |
|---|---|---|---|
| `Seat Control Tab`（13.x）| 14 | **1** | `-003` |
| `Tri-Mode Climate`（3.x）| 17 | **17（全部）** | `-015` … `-031` |
| 計 | 31 | **18** | |

補行（附於各條 PC 之末，既有各行編號不動）：

```
N. [spec-derived] The vehicle does not have 3 knob HVAC controls with ICS,
   for which no HVAC screens or pop ups are displayed (2.14)
```

`specification_reference` 各併入 `2.14`（R-C29 義務一，本節領頭）。
**`test_item`／`test_procedure`／`expected_result` 逐字未動；tc_id 未改。**

### 1.2 `Tri-Mode Climate` 全部 17 條 —— 實質理由

2.14：`For MTC with ICS … no HVAC menu bar icons, no HVAC screens and no HVAC
pop ups will be displayed`。

3.x 之**每一條**其可觀察量皆在 HVAC 畫面上，逐條實測：

| 節 | 條 | 觀察位置 |
|---|---|---|
| 3.1 | `-015` | `The Tri-Mode Climate screen shows the "Windshield", "Face" and "Feet" mode buttons` |
| 3.1 | `-016`／`-017` | 硬鍵操作，但 ER 之 `Only the Face mode is active` 讀於同一畫面 |
| 3.2 | `-018` | `The "MAX DEF" button is shown in place of the "FRONT DEF" button` |
| 3.2 | `-019` … `-028` | 皆讀 `"MAX DEF"` 按鈕之作用狀態 |
| 3.3 | `-029`／`-030` | 步驟明寫 `on the climate screen` |
| 3.4 | `-031` | `Read the climate screen for the rear defrost button` |

**在 3 旋鈕 ICS 之車上，這 17 條沒有一條有可操作的對象。**
既有之三個 PC（tri-mode／MAX DEF／MAX A/C 有無）**皆未排除該配置** ——
它們說的是「有沒有這個功能」，不是「這個功能有沒有介面可按」。

**`-016`／`-017` 特別要說**：它們操作**硬鍵** MODE 按鈕，看起來不需要畫面。
但其 ER 讀的是哪些 airflow mode 為 active，而該狀態顯示於 Tri-Mode Climate
screen。**操作端在硬鍵不等於觀察端在硬鍵。**

### 1.3 `Seat Control Tab` 只有 `-003` —— 實質理由

**其餘 13 條不須補，理由具名如下**（34 §1.1 要求「答案為不存在者，
於上繳包具名其實質理由」）：

**（a）2.14 之排除範圍限於 HVAC。** 條文逐字為
`no **HVAC** menu bar icons, no **HVAC** screens and no **HVAC** pop ups`。
13.x 之操作對象為**座椅控制**（Seats tab、Seat Control Popup、腰靠／側靠
級距），非 HVAC。3 旋鈕 ICS 移除的是氣候介面，不是下螢幕的座椅頁。

**（b）6.3 不適用於 13.x 之車輛。** 6.3 之觸發條件為
**`non-foldable`** secondary lower screen；而 13.2 之下螢幕有
`stowed position`（`-001`／`-002`／`-003` 之 PC 逐條明寫），**是可收合的**。
兩者互斥，故 6.3 之「comfort section 自 head unit 移除」不落在 13.x 上。

**（c）`-003` 是唯一的例外，因為它讀 head unit 的 climate section。**
其 PC4 為 `The user is already in the climate section on the main head unit`，
ER1 為 `The tab shown in the climate section is not the Seats tab`。
**climate section 就是 HVAC 畫面** —— 3 旋鈕 ICS 車上不存在，
故該條在該配置下沒有可操作的對象。

**（d）`-002` 為何不補，須說明，因為它也用 head unit。**
`-002` 之 ER 為 `The Seat Control Popup is displayed on the head unit`。
2.14 移除的是 **HVAC pop ups**，而 Seat Control Popup 是座椅控制的 popup，
不是 HVAC popup。**這一條我判為不補，但它是本次判斷中最接近邊界者** ——
若分析層認為 head unit 在該配置下連 comfort popup 都不顯示，`-002` 須補。

### 1.4 未發現「無 PC 可排除」之條 —— 未觸發停下條件

34 §1.2 之停下條件為「某條在某配置下完全無法執行且**無 PC 可排除**」。
18 條皆可由一行排除式 PC 處理，**未觸發**。

---

## 2. `-045` 拆為二條

| | tc_id | PC 之第十三軸值 | ER |
|---|---|---|---|
| 主情形 | **`-045`** | `The vehicle has 3 knob HVAC controls with ICS` | 無 icon／無畫面／無 popup |
| 例外 | **`-046`** | `The vehicle is one zone MTC with push button TEMPERATURE and hard controls that would not create a mismatch between hard controls` | 有 icon／有 popup |

兩條同溯 `SWE1-HVAC-020-04`，`split_flag` 皆真，`split_reason` 具名
§8.2.2（independent partial failures）與 §7（negative pairing），
**寫在兩列上**。

**例外條之 PC 具名軸值，未用否定式**（34 §4）。

### 2.1 新舊 tc_id 對照 —— 後續無條需順移

| 舊 | 新 | req_id | 說明 |
|---|---|---|---|
| `-001` … `-044` | 同 | — | **未動**（`-003` 之內容未動，僅補一行 PC）|
| `-045` | **`-045`** | 020-04 | 主情形，內容未動，加 split 兩欄 |
| — | **`-046`** | 020-04 | 例外，**新增** |

**`-045` 原為最後一條**（gen_batch3 之發射順序為 2.2 → 6.3 → 2.1 → 2.14），
故拆分後**沒有任何既有 tc_id 改變**。與批次 2 之 `-024` 拆分不同 ——
那次後續四條各順移 +3。

下放包 34 §2 之「後續順移」在本案為空集合，據實回報而非虛列一張全等的表。

---

## 3. `-044` 之 `reasoning` 補句

2.14 之 doc `reasoning` 增：

> **`-03` 之 037 描述「no mismatch occurs」係條文之目的子句
> `in order to prevent a mismatch`，目的不是可觀察量，故被驗證者為其機制句**
> （R-C22；且 3 旋鈕 ICS 車上無螢幕，mismatch 於該配置本就無從觀察，
> 以它為 ER 將產生永遠無法判定之 TC）。

同段併記 `-04` 之拆分依據（§8.2.2 ＋ §7）。

---

## 4. profile 第十三軸之否定式限制

第十三軸增一段引用區塊：

> - 否定式**僅得用於「只需排除某一值」之情形**，且該 PC 須可辨識為排除式
> - **凡 TC 之行為隨軸值而異者，PC 一律具名該值**，不得用否定式
>   —— 首個案例為 `NR1L-ComfortHMI-046`
>
> 理由：**否定式之涵蓋範圍取決於軸現有幾個值，而軸會增值。**
> 今日正確之否定式，會在增值當日靜默地變成錯誤，且無任何 gate 會報。

**現況實測**：全 46 條中，**26 條**帶否定式排除 PC
（`Tri-Mode Climate` 17、`Front Climate Anatomy` 之 2.2 八條、pilot `-003`），
**1 條**（`-046`）具名軸值。26 條之行為皆不隨軸值而異（三值中之後兩值皆
顯示 HVAC UI），故合乎限制。

---

## 5. `RUNBOOK.md` —— 失敗形狀陳述

逐字寫入 §3.3 之自述，並加一段界定它所定義的那類缺陷：

> **gate 檢查的是 TC 寫得對不對**（欄位、格式、溯源、1:1、主詞），
> **不是 TC 在哪種車上有沒有東西可以操作。**

末句：**那 18 條在被問之前，全部是綠的。**

---

## 6. lint

```
37 / 37 gates PASS; 0 finding(s) across 46 TCs
```

`tc_id` 001–046 連號無缺（實測）。三個 generator 連續重跑，輸出不變。

---

## 7. §9 self-check —— 僅列變動項（R-C23）

### 7.1 回溯補行之 18 條

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | PC 僅 state/env 且為 spec trigger | **變** | 18 條各增一行裝備類排除項，附於末且既有行號不動。實測 PC 內無動作動詞 → 0 命中 |
| 12 | 溯源、§8.2.1、無造值 | **變** | 引 2.14 之**裝備事實**而不驗其行為 —— 2.14 之行為由 `-042` … `-046` 驗證。18 條之 `req_id` 未動，coverage 分母未變 |
| 16 | `specification_reference` | **變** | 18 條各併入 `2.14`，本節領頭。全 46 條中現有 **26 條**為多節 |

**其餘 14 項未變** —— 因為內容逐字未動。這正是「補行不重寫」之意義：
**變動項可以被窮舉，且窮舉出來只有三項。**

### 7.2 `-045`／`-046`

| # | 項目 | 判 | 獨立依據（非 lint 覆述）|
|---|---|---|---|
| 2 | tc_title | PASS | `-045` 帶 `3 knob ICS controls`、`-046` 帶 `one zone MTC with push button temperature`，兩者互斥且各自帶其配置 token；字數 11／12 |
| 3 | PC 為 spec trigger | PASS | 兩條各 2 行，皆 `spec-verbatim` 且逐字取自 2.14（`3 knob HVAC controls`／`one zone MTC with push button TEMPERATURE and hard controls that would not create a mismatch between hard controls`）|
| 10 | 1:1、ER 可觀察 | PASS | **依 R-C23 明說：依據不是 `er-subject-net`**。兩條各 3/3，ER 主詞為 `The head unit menu`／`No HVAC menu bar icon`／`An HVAC menu bar icon`／`An HVAC pop up` —— 皆系統側 |
| 11 | supported 配 negative | **變，且本項為拆分之主因之一** | `-046` 即 `-045` 之負向對照，且**有條文明文支撐**（`this exception does not apply`）—— 不同於 `-035` 之無支撐而未配對 |
| 12 | §8.2.2 | **變** | 由「一條涵蓋不了故留缺口」改為「拆二條同溯」。依 R-C23，本項依據為我逐條讀了兩個 `split_reason` 之內容，非 `req-id-unique` gate 之 PASS |
| 13 | design_method | PASS | 兩條皆 `功能測試` —— 各為單一配置下之讀取，無遷移、無條件表。**拆分前若寫決策表亦不成立**，因兩個配置無法在同一 TC 內切換 |

其餘項未變。

---

## 8. 未寫回

依 34 §7 第 6 項，**未寫回**。`output/` 仍 2 檔。

A-CF19 之待測樣本現為 **26 條**多節 `spec_ref`（原 10 條）。
最長者仍為批次 2 之 `-029`／`-030`（三節）。

---

## 9. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **42** |
| 已生成（TC）| **46** |
| 阻塞（leaf）| 2（DR #17）|
| 未開始（leaf）| 359 |

---

## 10. 「本包是否仍有該驗而未驗者」

依 R-C30，陰性陳述附搜尋範圍。

1. **本次複查只問了一個配置維度：第十三軸。**
   問句是「在哪一種配置下沒有可操作的對象」，而我實際上只掃了
   **3 旋鈕 ICS** 這一種。
   **搜尋範圍**：`2.14` 與 `6.3` 兩節之 full_text ＋ 31 條之 PC／ER。
   **未做**：對其餘十二軸逐一問同一問句。例如 —— 單區車上是否有些
   雙區行為無對象？MTC 車上是否有些 ATC 行為無對象（`-036` 已有 ATC PC，
   但 3.x 全批沒有）？**第十三軸是被下放包點名的那一個，我沒有自己去找
   第二個。**
2. **`-002` 之判斷是本次最接近邊界者**（§1.3(d)）。
3. **`-016`／`-017` 我判為「觀察端在畫面」，但條文沒有明說。**
   3.1 只說 tri-mode 車有 3 個 airflow mode 按鈕在 Tri-Mode Climate screen 上，
   **沒說 MODE 硬鍵之循環結果只能從該畫面讀**。若硬鍵本身有 LED 指示，
   這兩條在無畫面之車上仍可執行，補的 PC 就過嚴。
   **搜尋範圍**：3.1 全文。pattern `LED` → **0 命中**。故條文未提供另一個
   觀察位置，我採畫面 —— 但這是「條文沒說」而非「條文說了不是」。
4. **補行一律置於 PC 之末，未依語意排序。**
   結果是裝備類排除項出現在執行期狀態之後（如 `-003` 之第 5 行在
   「使用者已在 climate section」之後）。**不影響判讀，但讀起來是倒的**，
   且它使「哪些行是回溯補的」一眼可見 —— 我判後者之價值大於前者之代價。
5. **26 條之否定式 PC 現在全部繫於「第十三軸只有三值」這個事實。**
   §4 之限制已寫入 profile，但**沒有 gate 會在增值時提醒這 26 條**。
   增值當日，這 26 行會靜默地變成錯誤 —— profile 記了，但記錄不是機制。

---

## 11. 建議 commit message（git 未執行）

```
fix(comfort): retrospective review adds 18 exclusion pre_conditions

- ask every existing TC "in which vehicle configuration does this have no
  operable object?"; 18 of 31 need excluding from 3-knob-ICS vehicles
- Tri-Mode Climate all 17: every observable sits on an HVAC screen
- Seat Control Tab only 076-03: it reads the head unit's climate section;
  seat controls are not HVAC and 6.3 needs a non-foldable screen
- lines appended, content and tc_ids untouched; 2.14 joins spec_ref
- split 020-04 into -045 (main) and -046 (exception); no tc_id shifts
  because -045 was last
- 044's reasoning: "no mismatch" is a purpose clause, the mechanism is what
  gets verified
- profile: a negated axis value may only exclude, never distinguish
- RUNBOOK: no mechanical check asks which vehicle a TC cannot run on
- lint 37/37 PASS, 0 findings across 46 TCs
```

---

## 12. 待分析層

1. **§10.1** —— 其餘十二軸是否須各跑一次同一問句（我判「應該要」，未做）。
2. **§10.2** —— `-002` 是否也須補。
3. **§10.3** —— `-016`／`-017` 之觀察位置判斷。
4. **§10.5** —— 否定式 PC 之增值風險目前只有文件記錄，無機制。
5. 批次 4 之授權（34 §7 末段之前置條件已滿足：複查確實找到須補之 PC，
   故其成因**可能同樣存在於未生成之 359 leaf**）。
