# 上繳 04Z-A5 — R-TM42、G-TM3 訂正、R-TM40 依據訂正、A-TM23，及 R-TM38 回溯自查

執行層 → 分析層。對應 `docs/handoff/04Z-A5_numbering_correction.md`。2026-08-21。

T1–T4 全數完成。**三項須先講**：

1. **本包依賴 `04Z-A4`，而該包未執行，且本包未依 R-TM20 聲明** —— 見 §1.1
2. **T3 之回溯自查有實質發現**：canon §10.7 被引用兩次，**兩次都漏掉其中
   最相關的一條規則**，而那條正是 R-TM40 偏離 canon 預設格式之**正當依據**
   —— 即：正確的依據一直就在同一節裡。見 §3
3. R-TM 條數為 **45**，非本包期望之 43 —— 成因見 §1.1

---

## 1. 執行順序與條數

### 1.1 `04Z-A4` 未執行，本包 T1(d) 依賴之 R-TM40 不存在

本包 T1(d) 要求「於 R-TM40 條文末尾追加依據訂正」。執行前實測：

```
grep -n '^## R-TM4[012]' RULINGS.md   → 無命中（R-TM40/41/42 皆不存在）
ls docs/upstream/ | grep 'A4'          → 僅 01Z-A4_corrections.md
```

即 **`04Z-A4_spec_reference.md` 從未執行**，其 R-TM40 / R-TM41 未落檔。

**本包未依 R-TM20 聲明此依賴** —— 該條要求追發包須「於首節明列其所依賴
之前包編號與該前包尚未上繳之事實」並「將被依賴之指令原文併入本包」。
本包首節僅載「覆核對象：`04Z-A3_corrections.md`」，未提 `04Z-A4`。

**處置**：`04Z-A4` 自身**是自足的**（其首節依 R-TM20 明確聲明依賴
`04Z-A3` 未上繳，並載「本包與 A-3 之 T1–T5 互不相依，可同 session
依序執行」）。故執行層**先補做 `04Z-A4` 全部 T1–T6，再執行本包**，
兩份上繳分立。

**此與 `02R → 02R-A1 → 03` 三包連發之情形同型**（R-TM20 之依據事件），
差別在本次執行層於執行前發現，未產生錯誤動作。

### 1.2 條數：45，非本包期望之 43

| 階段 | `## R-TM` |
|---|---|
| 本包執行前 | 42 |
| `04Z-A4` 加 R-TM40 / R-TM41 | **44** |
| 本包加 R-TM42 | **45** |

本包 T1 期望 43 —— 該值假設 `04Z-A4` 未執行（42 + R-TM42）。
**實際為 45。** `## G-TM` 3、`## A-TM` 23，兩者與期望相符。

## 2. T4 驗證（依 R-TM31，列明細）

```
R-TM42          RULINGS.md:1503
同源之三種形態    RULINGS.md:1307（R-TM38 條末註記）
依據訂正         RULINGS.md:1430（R-TM40 條末）
G-TM3 訂正       RULINGS.md（原理由段加刪除線 + 條末訂正區塊）
A-TM23 索引      ANOMALIES.md:35

R-TM 45（見 §1.2）   G-TM 3   A-TM 23
scripts/ mtime  09:15:18 / 09:13:36 / 09:14:32（凍結未破）
```

## 3. **T3 — R-TM38 回溯自查：canon §10.7 被引兩次，兩次都漏掉關鍵一條**

### 3.1 掃描範圍與限縮

`grep -n 'canon §\|FORMS.md\|docstring' docs/handoff/*.md` 得 **108 處**。
依執行層先前之提請（限縮於「以引用作為裁決依據」者）逐一判讀後，
**符合「以引用作為裁決依據且附具體引文」者僅二**：

| 位置 | 被引 | 狀態 |
|---|---|---|
| `04Z_closure.md:141-147` | canon §10.3 | **已知截斷**（本輪已由 R-TM38 訂正）|
| `04Z-A4_spec_reference.md:53` 與 §2.3 | canon §10.7 | **見 §3.2 —— 新發現** |

其餘 106 處為「提及條號」而非「引原文」（如「§8.4.1 禁止捏造來源未述
之值」），其陳述與條文要旨相符，不構成 R-TM38 所指之截斷。

### 3.2 canon §10.7 之完整原文與兩次引用之落差

**原文**（`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §10.7）：

```
### 10.7 `specification_reference` (workbook column)
String list of source spec references that anchor this TC. Required when
TC content depends on spec content (almost always).

**Format per entry**: `{spec_filename}_{section_id}`
- e.g. `Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_4.1`
- e.g. `Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023)_2.5`

**Rules:**
- List every spec section the TC directly verifies or relies on as setup
- Use the SourceID format from SYS1 / Polarion when available
- Order from most-specific (lowest section number) to general
- Multiple specs allowed when TC spans multiple spec files
- Do NOT cite specs only used as background context (those go in `reasoning`)
- Do NOT cite RD analysis docs (SWE.1 / SWE.5) — those are not spec sources
```

`04Z-A4` 之兩次引用：

| 處 | 所引 | 所漏 |
|---|---|---|
| §2.2 | 「§10.7 明訂為 string list，允許多條目」 | Format per entry、六條 Rules |
| §2.3 | Rules 第 1 條、第 5 條 | **Rules 第 2 條**、第 3、4、6 條 |

**兩次引用都沒有引到 Rules 第 2 條**：

> **Use the SourceID format from SYS1 / Polarion when available**

### 3.3 **這條正是 R-TM40 偏離 canon 預設格式之正當依據**

R-TM40 明文「不採 `<Spec Filename>_{outline}`（章節號）形式」——
而 `{spec_filename}_{section_id}` 正是 §10.7 之 **Format per entry**。
即 R-TM40 是一個**對 canon 預設格式之偏離**。

`04Z-A4` §3 為該偏離找的依據是「CFTS 文件自身修訂註記之既有寫法
（`CFTS015-806` 等）」—— 而該依據已由本包 §4（分析層自我訂正）證實
**取錯類別**（短號家族 vs 7 位家族，`CFTS015-<7 位>` 全文 0 次）。

**但 canon §10.7 Rules 第 2 條本身就授權該偏離**：SYS2 之
`Source Requirement items` 欄即 Polarion 側之 SourceID；
「when available」在本 feature 成立（SYS2 227 列該欄 227/227 非空，
`01R` 上繳已實測）。

**故 R-TM40 之正當依據一直就在它所引用的同一節裡，只是兩次都沒引到。**

這比單純的「句末截斷」更進一層 —— 前者是引了一句只引一半，
本例是**引了同一節而漏掉其中唯一能支持自己主張的那一條**。

### 3.4 對 R-TM40 之影響：結論不變，依據應改

- **R-TM40 之裁定不變**（Pei 所裁，且現有 canon 依據）
- **其依據應改為 canon §10.7 Rules 第 2 條**，取代已證偽之「文件既有
  寫法」依據
- A-TM23 之風險陳述（兩套編號字面不互通、審閱者搜尋會零命中）**不受
  影響** —— 那是可讀性問題，與格式是否有 canon 授權無關

**執行層未自行改寫 R-TM40 之依據訂正段**（該段為本包 T1(d) 逐字指定，
且條文修改屬分析層）。**提請以新註記補入。**

### 3.5 另一條值得注意者：Rules 第 6 條

> Do NOT cite RD analysis docs (SWE.1 / SWE.5) — those are not spec sources

037（`SWE1_Secure_Date&Time.xlsx`）為 **SWE.1** 分析報告。
R-TM40 之取值來自 **SYS2**（Polarion export）而非 037，**故不違反**。
但此條說明了為何 `spec_reference` 不能直接引 037 之 leaf id ——
執行層記錄於此，因該區辨在本 feature 之錨鏈設計中從未被明文寫下。

## 4. §4 之依據訂正 —— 執行層接受，並補一項

分析層自我訂正（短號家族 vs 7 位家族）**成立**。執行層另補：

A-TM13 之兩個 BLOCKED 物件（`6151328` / `6151331`）為 **`615xxxx` 區段**，
既非短號亦非本檔之 `481xxxx`。即就本 feature 之資料而言，
**SYS2 側可見三個區段**：

| 區段 | 數量 | 性質 |
|---|---|---|
| `481xxxx` | 270 | CFTS015 本文之需求物件 |
| `456xxxx` | 3 | `WrapperResource`（內嵌 RTF），非需求物件（A-TM13 末節）|
| `615xxxx` | 2 | **不在 CFTS015 內**（A-TM13 主體）|

不影響 A-TM23 之結論。但 RD-1 若依 (c) 併問參照寫法，
**宜一併問及 `615xxxx` 區段之歸屬** —— 那與 Q-TM2 是同一問題的兩面。
已記入 A-TM23 條末。

## 5. T5(3) — 該驗而未驗者

### 5.1 依全集 1–2

T1–T4 完成。寫入後複查見 §2。四處 `str.replace` 前置 `assert` + `count==1`。

### 5.2 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **其餘 106 處「提及條號」之逐一比對** | §3.1 判定其為提及而非引原文，**該判定本身是抽樣讀過後之歸類，非逐處比對條文原文**。若要完全排除截斷，須逐處讀 canon 對應節 —— 成本高，未做 |
| 2 | canon §10.7 Rules 第 3 條之適用 | 「Order from most-specific (lowest section number) to general」—— 本格式無章節號，R-TM40 連鎖後果 2 改採物件 id 遞增。**該替代是否為 canon 所許，未驗** |
| 3 | `04Z-A4` §2.2 所引之先例 R-VS14 | 未查證（屬 vehicle_setting，A-TM20 下不碰該目錄）|
| 4 | A-TM21 / A-TM22 之實跑 | 凍結中 |
| 5 | PU 陽性對照、A-TM12 / A-TM19 | 續掛 |

**第 1 項須說明**：§3.1 之「其餘 106 處為提及而非引原文」是**歸類判斷**，
依據為該等處之行文形態（無引號、無區塊、無逐字標記）。**未逐處回查
canon 原文確認其陳述與條文相符。** 若分析層認為須做，建議再限縮 ——
例如只查「以該提及作為某項裁定之唯一依據」者。

### 5.3 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| §10.7 兩次引用皆漏 Rules 第 2 條 | 同一比對確認 Rules 第 1、5 條**有**被引 → 非一律判漏 | 有 |
| 108 處中僅 2 處符合「引原文作為裁決依據」 | 該 2 處確實各有具體引文與區塊 → 篩選有效 | 有 |
| BLOCKED 恰 2 筆（A-4 T4） | 其餘 20 片全 OK → 非一律 BLOCKED | 有 |

### 5.4 依全集 5（設計說明之可驗性）

本包 §4 之分析層自我訂正，其實測數字（短號 26 個相異值、7 位 270 個、
`CFTS015-<7位>` 0 次）**執行層未獨立複驗** —— 但其中「`615\d{4}` 零命中」
與「`481xxxx` 為本檔區段」兩項已於 `01R` / `03Z-A1` 多次實測相符，
且 A-4 T4 之 BLOCKED 恰 2 筆為間接佐證。**短號家族之 26 個相異值未驗。**

## 6. 本包未動之事項

未動 git。**未寫入、未修改 `scripts/` 任一行**（mtime 為證）。
未改 `backend/`。**未修改任何既有下放包**（T3 只讀）。未生成任何 TC。
**未將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位**（R-TM41）。
未碰 `features/vehicle_setting/`。未 rm 任何檔案。未送出 RD-1。
未填 `D5`、未組 Scope 值。未以 openpyxl 存回任何工作簿。
**未自行改寫 R-TM40 之依據訂正段**（§3.4 之提請留待分析層）。
