# 58 — Comfort HMI / R-C27-1、25 vs 26 之標示、範本本體擴充、output 歸檔

- 產出層：執行層｜2026-08-16｜對象：分析層／Pei
- 覆核對象：`docs/handoff/80_rc27_1_delivery_note.md` ＋ Pei 2026-08-16 之二則追加裁定
- **先報一件計畫外之事**：ENTRY 023 之產出檔已被 Excel 重存，見 §7。

---

## 1. R-C27-1 —— 已貼入

`RULINGS.md` 新增 R-C27-1 區塊（原文照貼），並：

- **R-C27 原文保留**，其後加旁標：「首 60 字元」為假定值，其可見範圍從未量測，
  **該 60 不再引用**，本條之精神（依可見性排序）維持
- **R-C38／R-C39 之區塊內仍寫「首 60 字元」** —— 該二條為既簽之裁定，原文不改，
  各加旁標指向 R-C27-1
- profile 之 `[COVERED-BY]` 欄位規則改記實測可見字元數（約 11）
- `write_back.py` 之 assertion 標題改為「Remarks **前綴（檢查窗口 60 字元）**」——
  **那 60 是這個檢查自己的檢視窗口，不是對讀者可見範圍之宣稱**。二者同為 60 而
  意義不同，不改述會使下一個讀者以為 R-C27 還在被引用
- `gen_batch15.py` 之一條 reasoning 改述（doc 層欄位，**不寫入工作簿**；
  已實測現行產出之 429 列 × 14 欄與 JSON 仍 0 格不符）

---

## 2. 25 vs 26 —— 兩份文件各自具名其母體

| 文件 | 數字 | 其所量者 |
|---|---|---|
| RD-1（致需求方）| **26 units with an open question** | 有未答問題之單位，含部分涵蓋之 `047` |
| 交付說明（致評閱方）| **25 units with no test case** | 工作簿內無任何列之單位 |

二者皆已於其數字旁載明所量者，且**互相指向對方之數字**：
RD-1 之摘要說明「其中 25 條無任何測試案例，第 8 項為部分涵蓋」；
交付說明說明「問題文件計 26 條，本說明計 25 條，差額即下方那一條」。

`047` 之一句已加（§4 之全文第 70–75 行）。
`[BLOCKED` 之搜尋指路已加（第 96–97 行）。
RD-1 附錄之「NOT part of the 25」亦改為 **26**（其母體是問題數而非無列數）。

---

## 3. Pei 追加裁定一 —— A-CF02、基線標示、範本本體

### 3.1 A-CF02 **不轉 RESOLVED**

79 §3 之「移除 SR25 兩檔」**已被推翻**：兩檔不移除，`Device Manager` PDF 亦留置。
`ANOMALIES.md` 之 A-CF02 改記 **「已知不一致，以交付說明標示基線」**，
並保留前次裁定之全文而標明其被部分推翻。

**為何不是 RESOLVED**：不一致仍在，只是**被標示了**。
把「已標示」記成「已解決」，下一個讀這一列的人會以為夾裡只有 SR24。

### 3.2 交付說明之基線句（已加，見 §4 第 8–10 行）

> **Baseline**: the requirement baseline for this delivery is **SR24 CR24879
> (September 25 2023)**. The folder also contains an SR25 revision of the same
> document for reference; **it is not the baseline for these test cases**.

### 3.3 通用空白範本之擴充 —— **已執行**

**先答「多填了哪些格」一問**：對照 `forms/…_SWQT_20260121.xlsx`
（`cd876c202c71e74b…`）逐格比對，`_prepared_ext.xlsx` 相對於原範本
**沒有多填任何一格 —— 方向是相反的**：

| 差異 | 格數 | 內容 |
|---|---|---|
| B 欄 row 60–601 之編號公式 | **542** | 即擴充本身（601 − 60 + 1 = 542）|
| `D10`＝`xxx`／`D11`＝`xxx`／`F10`＝`NR1L-AntiTheft-001`／`G10`＝`AntiTheft`／`S10`＝`NA` | **5** | **原範本所帶之他 feature 範例列**，於 ext 版為空 |

**feature 專屬之值：0 格。** 9 個工作表全檔搜尋 `Comfort`／`HVAC`／`AntiTheft`
等字樣 **0 命中**；`D5`（範圍 Scope）**兩版皆為空**（其標籤在 `C5`，
`D5` 本身從未被填），`D2` = `newR1L` 為原範本既有。

**故「清除 feature 專屬之值」一步無事可清** —— 該清除早在 Comfort 之
ENTRY 001 清列時就做過了，清掉的是 AntiTheft 之範例資料。

**產出**：`forms/FM-WI-FSM-036-A01 … _SWQT_20260816_ext.xlsx`，
**123,717 bytes**，SHA256 `6d53056e559bd0c13d26d38f16754536ede0230a5ce69c8596cce8e8b28b9d4c`。
**原範本未覆寫**，仍在 `forms/`，仍為 `BASELINE.sha256` 之對象。

**驗**（除 DV 範圍外逐格相同）：

- 逐格差異 **547 格 = 542（B 欄公式擴充）＋ 5（上表之他 feature 範例值）**
- DV：`P10:Q11`→`P10:Q601`、`T10:Z11`→`T10:Z601`、`AF10:AF11`→`AF10:AF601`；
  x14 `R10`＋`R11:R59`→`R10:R601`（來源統一為 `$A$1:$A$9`）
- zip member **48 = 48**

**那 5 格是本版唯一之非擴充性差異，且未通過「除 DV 外逐格相同」之字面。**
本層判其為**應留之偏離**（他 feature 之範例資料不宜留在共用範本），
**但這是本層的判斷而非裁定** —— 若分析層要求逐格相同，填回五格即可，
單一動作可逆。

`forms/FORMS.md` 已記其版本、來源、擴充範圍與上述全部差異。

**DR #36 條目**：(b) 母本範本一次修正 —— **已執行並記其產物**；
(a) privacy 已交付件是否回溯 —— **仍待 Pei**，且明載
**本項不使已交付件變好**，privacy 之 9 列不因新版範本而改變。

---

## 4. 交付說明全文（80 §4 —— 供覆核）

以下為 `docs/Comfort_HMI_delivery_note.md` 之**全文**，未經節錄。
紀律自查：grep `R-C`／`A-CF`／`§`／gate 名／下放包編號／ENTRY —— **0 命中**。

---

# Comfort HMI — Test Case Delivery Note

**Feature**: Comfort HMI (newR1L)
**Requirement under test**: `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
**Analysis document**: `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`
**Workbook**: `FM-WI-FSM-036-A01 … _SWQT_Comfort_<date>.xlsx`
**Date**: 2026-08-16
**Baseline**: the requirement baseline for this delivery is **SR24 CR24879
(September 25 2023)**. The folder also contains an SR25 revision of the same
document for reference; **it is not the baseline for these test cases**.
**Version**: this is **one version of an ongoing delivery**, not a final one. See
"What is still open" below; a later version will add rows rather than correct
these.

---

## What is covered

**429 test cases covering 378 of the 403 verification units** in the analysis
document.

A verification unit is one testable statement identified in the requirement
analysis. Several units are verified by more than one test case where the
requirement lists more than one way to trigger the same behaviour — for
example, a clause that names three separate actions that each break AUTO mode
is verified by three test cases, one per action.

---

## What is not covered — 25 units with no test case

These 25 units have **no row in the workbook**. Each depends on information the
requirement text refers to but does not contain, and a question document has
been prepared for the requirements owner (see the last section).

A **26th** unit has a test case that covers only part of it; it is described
after the table. The question document counts **26 units with an open
question**; this note counts **25 units with no test case**. Both numbers are
stated with what they count, and the unit below is the difference between
them.

| Unit | Section | What is missing |
|---|---|---|
| `SWE1-HVAC-001-01` | 2.1 | The clause says the comfort tab set depends on vehicle configuration, but not which configuration produces which set. |
| `SWE1-HVAC-001-02` | 2.1 | As above, for the display order of the tabs. |
| `SWE1-HVAC-016-01` | 2.12 | The four-mode airflow set does not state which vehicles it applies to; the other two airflow sets do. |
| `SWE1-HVAC-016-02` | 2.12 | As above. |
| `SWE1-HVAC-016-03` | 2.12 | As above. |
| `SWE1-HVAC-018-01` | 2.12.2 | The hard-control cycle depends on the four-mode set above, so it inherits the same gap. |
| `SWE1-HVAC-018-02` | 2.12.2 | As above. |
| `SWE1-HVAC-018-03` | 2.12.2 | As above. |
| `SWE1-HVAC-018-04` | 2.12.2 | As above. |
| `SWE1-HVAC-018-05` | 2.12.2 | As above. |
| `SWE1-HVAC-018-06` | 2.12.2 | As above. |
| `SWE1-HVAC-006-04` | 2.5 | The recirculation icon is specified "as displayed in the table"; that table is not in the document. |
| `SWE1-HVAC-099` | 14.15 | The available comfort controls are said to depend on vehicle configuration; the mapping is not in the document. |
| `SWE1-HVAC-122-02` | 16.16 | The seat off-icon is specified by reference to the "Climate section"; no section carries that mapping. |
| `SWE1-HVAC-015-04` | 2.11 | The clause's observable effect is on the rear passengers; the document does not state which vehicles have rear climate. |
| `SWE1-HVAC-015-05` | 2.11 | As above. |
| `SWE1-HVAC-116-03` | 16.11 | As above (the clause is word-for-word identical to 2.11). |
| `SWE1-HVAC-116-04` | 16.11 | As above. |
| `SWE1-HVAC-039` | 9.1 | The clause introduces a vehicle variant by reference to another document and specifies no observable behaviour of its own. |
| `SWE1-HVAC-019-02` | 2.13 | The clause hands its on/off logic to a VF HVAC document that is not available here. |
| `SWE1-HVAC-019-03` | 2.13 | As above. |
| `SWE1-HVAC-083` | 14.1 | The clause hands its content to a pop-up list that is not available here. |
| `SWE1-HVAC-129-01` | 18.1 | The sentence is word-for-word identical to section 17.1; nothing in either chapter tells a tester which vehicle each applies to. |
| `SWE1-HVAC-129-02` | 18.1 | As above. |
| `SWE1-HVAC-129-03` | 18.1 | As above. |

### One unit is covered only in part

`SWE1-HVAC-047` (section 10.4) **has a row**. The requirement makes the
behaviour conditional on AUTO being "available", and no section states when
AUTO is unavailable. The available case is tested; the unavailable case has no
test case, because there is no stated way to put the vehicle in it.

---

## Five rows that carry no test procedure

Five rows in the workbook state a requirement and deliberately carry no
procedure or expected result. They are in the workbook so that the gap is
visible in the same place as the coverage, rather than only in this note.

| Row | Section | Why there is no procedure |
|---|---|---|
| `NR1L-ComfortHMI-010` | 13.4 | The long-press logic is defined in the HMI Core Logic and Flow requirement; with that delegation removed, nothing in the clause is verifiable against this specification alone. |
| `NR1L-ComfortHMI-012` | 13.5 | The equivalence to the previous 4-way rocker hard control is defined in CFTS044; same shape as above. |
| `NR1L-ComfortHMI-382` | 11.5 | The Auto Comfort Settings options for heated and vented seats are defined in the HMI Settings List. |
| `NR1L-ComfortHMI-383` | 12.6 | As above, for the HMI Notes document. |
| `NR1L-ComfortHMI-081` | 2.14 | The requirement states a reduction in climate-control power consumption, which no Comfort HMI screen, pop-up or indicator displays. |

Each of these rows names the owning document and states that no test case in
this delivery covers it.

They are identified in the workbook by the marker at the start of the Remarks
column; searching that column for `[BLOCKED` finds all five.

---

## Screen and widget sizes

Five test cases carry a screen or widget size taken word-for-word from the
requirement. If any of those configurations is not part of this programme, the
corresponding test cases apply to nothing and should be withdrawn rather than
executed.

---

## What is still open

A question document covering the 25 units above, and the partly covered unit,
has been prepared for the requirements owner — **26 units with an open
question** in total. **It has not yet been issued.** When answers arrive:

- units that can then be written will be added to a later version of this
  workbook, identified by its own delivery record;
- units that turn out not to apply to this programme will be recorded as such
  rather than left as untested.

Two further questions have been recorded that block nothing: whether the two
heated-and-vented-seat chapters (11 and 12) describe one requirement or two,
and whether comfort settings are expected to survive an ignition cycle — the
requirement document does not say, and no test asserts either way.


---

## 5. Pei 追加裁定二 —— `output/` 之歷史產出歸檔

### 5.1 已搬入 `output/archive/`：**19 檔**（非 17）

裁定寫「ENTRY 002～021 之 17 份」，**實測為 19 份**：
`pilot`／`blocked2`／`batch7`～`batch16`（10 檔）／`rc42_1`／`registry`／
`verbatim`／`sourceclass`／`readability`／`split151`／`enumsplit`。
`output/` 現留三份：`20260815_prepared`（ENTRY 001 之對象）、
`20260816_prepared_ext`（現行母本）、`20260816`（現行產出）。

### 5.2 台帳之處理 —— append-only 未破

- 既有 checksum 行**一字不改**
- 各於其後插入 `#   archived : output/archive/<檔名>` 註記，**19 行**
- 文末新增「歸檔後之可驗路徑」段落，追加 19 條**新路徑之 checksum 行**

**第三步不可省**：只做註記的話，舊路徑於 `shasum -c --ignore-missing` 下
會被**靜靜跳過**，而「歸檔後仍可驗」就只是一句宣稱 ——
**這正是 R-C43 所防之形態：失效不出聲者不算檢查。**

### 5.3 逐檔複驗

`shasum -c --ignore-missing`：**46 OK／1 FAILED**。
**19 份歸檔檔全部 OK。** 那 1 FAILED 不是歸檔造成的，見 §7。

### 5.4 `write_back.py` 增 §3.4

assertion **全數 PASS 後**自動歸檔前一份產出，並以上述三步更新台帳
（含一項 append-only 之自我 assertion：既有行不得消失或換序）。
**assertion 未全過則不歸檔** —— 前一份要留在原地供逐項比對。
`output/STATUS.md` 已記該規則與三份留存檔之理由。

---

## 6. 仍未做

**未複製任何檔案至交付夾；未移除任何檔案**（SR25 兩檔與 Device Manager PDF
皆留置）。未改 prepared 檔與 ext 母本。git 未執行。

---

## 7. 計畫外之發現 —— ENTRY 023 之產出檔已被 Excel 重存

歸檔後之 `shasum -c` 出現 **1 FAILED**，對象為 `…_Comfort_20260816.xlsx`。
**該 FAIL 是台帳在做它該做的事：檔案變了而記錄沒變，它就出聲。**

| | |
|---|---|
| 台帳（ENTRY 023）| `c37e572f…`，寫回當時 |
| **現況** | **`8d17ceca…`，180,081 bytes，mtime 22:36** |

**內容之唯讀比對**：429 列 × 14 個寫入欄與 `generated/*.json`
**逐格比對，不符 0 格**；DV `P10:Q601`／`T10:Z601`／`AF10:AF601`、
x14 `R10:R601`、B 欄公式、48 個 zip member、9 個工作表、`max_row` 601
**全部在**。→ **內容未變，變的是位元組**，為 Excel 開啟後重存之典型結果。

已登 **ENTRY 024**（`type: observed`）記此，**ENTRY 023 不改**。

**待 Pei 明示二事**：

1. 那次開啟是否即 profile §0.1 之 Excel 四項確認？**其結果尚未回報** ——
   本層只記「檔案被重存」這件事實，不代該確認宣告通過
2. **交付之對象為何者**：(a) 本層產出之 `c37e572f…`（**已不在磁碟**），
   或 (b) Excel 重存後之 `8d17ceca…`（現行檔）

**其副作用須先講明**：`write_back.py` 之前置 gate 要求
「`DELIVERY.sha256` 全數 OK」，現有 1 FAILED，**下一次寫回會被擋住**。
這是台帳設計如此，不是故障；解法是 Pei 就上述第 2 點裁定後補登一則 ENTRY。
**本層不自行處置** —— 那條 FAILED 記錄的是「本 pipeline 交出的位元組已不在磁碟上」，
由本層自己抹掉它，等於自己判自己無事。
