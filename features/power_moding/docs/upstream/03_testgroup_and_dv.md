# 上繳包 03 —— Test Group 欄值改判、DV 列舉值實測與 Phase 1 啟動

- 日期：2026-08-23
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/03_testgroup_and_dv.md` ＋ `03a_pei_rulings.md`（併讀）
- 前一包：[upstream/02_baseline_switch.md](02_baseline_switch.md)
- 執行狀態：**03 步驟 1–8 全部執行完畢，03a 四條併入步驟 1。**
  九條停止條件全未觸發。**零寫回工作簿**；改狀態 git 零次。

---

## 1. 抄錄核對表（步驟 1，03 三條 ＋ 03a 四條）

抄錄方式同前：`re.findall` 自 handoff 之 fenced block 直接取字串寫入，
未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立再抽取**
後計 SHA256。

| 來源 | 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|---|
| 03 | R-PMH13 | G 欄填交付夾名；撤回 R-PMH2 後半 | 544 | `6e163ef260ff31e6` | `6e163ef260ff31e6` | 逐字相符 |
| 03 | R-PMH14 | 語料之鑑別力口徑 | 232 | `6d4b62eca4fb8279` | `6d4b62eca4fb8279` | 逐字相符 |
| 03 | R-PMH15 | `.gitignore` 之 `inputs/*` 形態與四項雙向驗證 | 368 | `8c7e1e9140c9575f` | `8c7e1e9140c9575f` | 逐字相符 |
| 03a | R-PMH13 之生效 | 核可生效，G 欄停止條件解除 | 204 | `5c2d8191265d14af` | `5c2d8191265d14af` | 逐字相符 |
| 03a | R-PMH16 | `tc_id_format` = `NR1L-DisclaimerScreen-{NNN}` | 441 | `b5c1dca6cebb18b6` | `b5c1dca6cebb18b6` | 逐字相符 |
| 03a | R-PMH17 | A-PMH06 之追認，RESOLVED | 179 | `8d9e34596fe21d01` | `8d9e34596fe21d01` | 逐字相符 |
| 03a | R-PMH18 | 兩個字面常數之大小寫保真 | 273 | `8ec7e2b9cf2f794d` | `8ec7e2b9cf2f794d` | 逐字相符 |

Pei 之裁定原文（2026-08-23，逐字）「R-PMH13 核可、Q7 乙、A-PMH06 追認」
已抄入 `RULINGS.md` 之 03a 段首。

### 1.1 R-PMH11 附註之落實證明（原文 SHA256 未變）

附註以引用段落置於 R-PMH11 之 fenced block **之外**，並含 03a §四所要求之
**PENDING-CANON** 標記。落地後獨立再抽取：

| 條號 | SHA256（前 16） | 與 02 包所記 |
|---|---|---|
| R-PMH11 | **`bbba2810887e6e96`** | **相同** |

前 12 條（R-PMH1–R-PMH12）於本輪落檔後全數複驗，SHA256 逐條與 01／02 包
上繳所記**完全相同**：`468fc431`／`19f57d23`／`84acd49a`／`04d87eb1`／
`e589281f`／`5bb6ebe3`／`78b740e4`／`533aac08`／`e3212132`／`88507096`／
`bbba2810`／`e56341f8`。

---

## 2. DV 全量清單（步驟 2，legacy／x14 分列，二證同值）

量測對象：`forms/…_20260817_ext.xlsx`，分頁
`Test Case Specification 測試用例規範`。**未以 `openpyxl` 存回**（停止條件 9）。

**證一**：`zipfile` 直讀 `xl/worksheets/sheet6.xml` 之
`<dataValidation>` 與 `<x14:dataValidation>` 原始 XML。
**證二**：`openpyxl` 之 `ws.data_validations.dataValidation`（僅 legacy）。

### 2.1 legacy `<dataValidation>` —— 3 組

| sqref | type | `formula1` 原文 | allowBlank | 二證同值 |
|---|---|---|---|---|
| `P10:Q1411` | `list` | `"P0,P1,P2,P3"` | `1` | ✅ |
| `T10:Z1411` | `list` | `"0,1"` | `1` | ✅ |
| `AF10:AF1411` | `list` | `"Pass, Fail, Pending,Block,NA"` | `1` | ✅ |

`operator`／`showDropDown`／`errorStyle` 三屬性在三組上皆未設定。

⚠ **`AF` 之列舉字串含前導空白** —— 逐字為 `Pass`／` Fail`／` Pending`／
`Block`／`NA`（`Fail` 與 `Pending` 前各有一個空格）。Phase 6／7 若要寫入
測試結果，**必須連空格一起寫**，否則會被 DV 擋下。本輪四份交付件之 AF 欄
皆為空，故未實際踩到。

⚠ **`P10:Q1411` 之 sqref 跨 P、Q 兩欄** —— `Q` 為
`Estimated Test Time (mins)`，卻套用 `"P0,P1,P2,P3"` 之下拉。
四份交付件之 Q 欄**全部為空**（`allowBlank=1` 故合法）。
**若日後要填分鐘數，將無法通過 DV。** 此為表單層之瑕疵，非本 feature 之。

### 2.2 x14 `<x14:dataValidation>` —— 1 組

| `xm:sqref` | type | `xm:f` | allowBlank |
|---|---|---|---|
| `R10:R1411` | `list` | `下拉選單!$A$1:$A$9` | `1` |

`openpyxl` **讀不到**此組（載入時即丟出
`Data Validation extension is not supported and will be removed` 警告）——
故此組**只有證一**，二證同值不適用；已於本表明示。這正是 R-G3 之成因：
以 `openpyxl` 存回會把它整組刪掉。

**目標範圍之逐項值（`下拉選單!A1:A9`，9 項全集）**：

| # | 字串（逐字） |
|---|---|
| 1 | `功能測試 (Functional based ; no specific technique)` |
| 2 | `狀態轉換 (State Transition Testing)` |
| 3 | `決策表 (Decision Table Testing)` |
| 4 | `等價劃分 (Equivalence Partitioning, EP)` |
| 5 | `邊界值分析 (Boundary Value Analysis, BVA)` |
| 6 | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` |
| 7 | `情境 / 用例 (Scenario / Use Case Testing)` |
| 8 | `負向測試 (Negative / Invalid)` |
| 9 | `基礎故障注入 (Fault Injection Lite)` |

`A10`／`A11` 為空（`dims` 上界大於內容），DV 明載 `$A$1:$A$9`，故無外溢。

**母本之 DV 總數 = 4 組（legacy 3 ＋ x14 1）**，除此之外無其他 DV。

---

## 3. `priority` 欄之三方衝突判定（步驟 3）

### (a) 母本 `P10:P1411` 之 DV

**有 DV，列舉為 `"P0,P1,P2,P3"`**（`type=list`，`allowBlank=1`，
sqref 實為 `P10:Q1411`）。二證同值。

### (b) 四份已交付件之 `P` 欄實際值分布

| 交付件 | 資料列 | P0 | P1 | P2 | P3 | 空 | 逸出 |
|---|---|---|---|---|---|---|---|
| User Profiles 20260820 | 189 | 38 | 66 | 71 | 14 | 0 | **0** |
| Comfort 20260817 | 466 | 325 | 132 | 8 | 0 | 1 | **0** |
| Time Management 20260822 | 59 | 30 | 27 | 2 | 0 | 0 | **0** |
| Power Management 20260821 | 284 | 180 | 59 | 7 | 37 | 1 | **0** |

**四份 998 個非空值，全部落在 `{P0, P1, P2, P3}` 內，逸出 0。**

### (c) 三方之交集與差集 —— **不是三方衝突**

| 來源 | 值域 | 與 canon §10.2（`P0/P1/P2/P3`） |
|---|---|---|
| 母本 `P` 欄 DV | `{P0, P1, P2, P3}` | **完全相同** |
| 四份已交付件 `P` 欄實際值 | `{P0, P1, P2, P3}` | **完全相同**（逸出 0） |
| `QS Suggestion!B5` | 「高High／中Medium／低Low／不適用NA」 | 不同 —— **但它是「建議」不是現況** |
| 037 之 `Priority` 欄 | `{High, Medium, Low}` | 不同 —— **但它是 037 的欄，不是 036 的 P 欄** |

**交集** = `{P0, P1, P2, P3}`（母本 DV ∩ 交付件實際值 ∩ canon §10.2，三者相等）。
**差集** = 空。

**判定：條文與交付件之衝突不存在。** 三方中真正描述「036 之 P 欄現況」者
只有前兩項，二者與 canon §10.2 三方一致。後兩項是我在 02 包 §11 第 1 項
把不同對象並列所造成的假衝突：

- `QS Suggestion` 分頁之標題逐字為「**25/10/15 QS確認後建議**」——
  其 B5 是**尚未落實之改版建議**（建議把 036 之 Priority 改成與 SWRA 一致），
  不是現況描述。母本 rev C 之 ChangeHistory 亦無此項，**該建議未被採納**。
- 037 之 `Priority` 欄屬 **FM-WI-FSM-037-A03（SWRA 報告）**，與 036 之
  `Test Case Priority` 是兩張表的兩個欄。B5 之「Priority與SWRA分法統一呈現」
  一語，正說明二者**現在不同**，這才是它被提為建議的理由。

**故停止條件 7（母本 DV 與 canon §10.2 不一致）未觸發。**

> **執行層之自我更正**：02 包 §11 第 1 項稱此為「六項中最可能造成實際寫回
> 失敗者」，**該評估過高**。成因是把「建議」與「現況」、「037 的欄」與
> 「036 的欄」並列成三方。教訓與 R-PMH12 同型：**比較之前先確認兩邊是不是
> 同一個對象**。

---

## 4. 各 DV 欄之逸出檢查（步驟 4）

分母為「四份已交付件 × 各 DV 欄之非空儲存格」；`allowBlank=1`，
故空值不計逸出（R-G8：分子分母定義）。

| 欄 | DV 列舉 | UP | Comfort | TM | PM | 非空合計 | **逸出** |
|---|---|---|---|---|---|---|---|
| `P` priority | `P0,P1,P2,P3` | 189 | 465 | 59 | 283 | 996 | **0** |
| `Q` estimated_time | 同上（sqref 跨 P:Q） | 0 | 0 | 0 | 0 | 0 | **0** |
| `R` design_method | `下拉選單!$A$1:$A$9`（9 項） | 189 | 465 | 59 | 283 | 996 | **0** |
| `T–Z` vehicle_models | `0,1` | 0 | 3262 | 0 | 0 | 3262 | **0** |
| `AF` test_result | `Pass, Fail, Pending,Block,NA` | 0 | 0 | 0 | 0 | 0 | **0** |

### **有 DV 而交付件逸出其列舉之欄位：零。**

（本節不省略 —— 下放包 §七第 4 項要求「無則明言零」。）

**附帶觀察三項**：
1. `T–Z` 僅 Comfort 填寫（3262 = 466 × 7，全為 `1`）；其餘三份全空。
   此與 `features/comfort/ANOMALIES.md` A-CF-EXT-01 所記之「T–Z 之 466 個 `1`
   非由 Comfort 管線產生」相符 —— 本輪由另一路徑（DV 逸出檢查）再次看到同一現象。
2. `Q` 與 `AF` 在四份中皆全空，故其 DV 從未被實際檢驗過。
   §2.1 所指出之兩項瑕疵（`Q` 套用 P0–P3 下拉、`AF` 列舉含前導空白）
   **在 Phase 6／7 首次填值時才會浮現**。
3. `R` 欄之 996 個值全部落在 9 項內 —— 即 A-PMH10 之字串不一致
   （`Pairwise / t-wise` vs `Pair-wise / N-wise`）在實務上未造成任何逸出。

---

## 5. A-PMH07 之連帶回報（步驟 5）

**已於 `features/comfort/ANOMALIES.md` 新增 `A-CF-EXT-02`**
（編號依該 feature 現行序，前一則為 A-CF-EXT-01，形態比照之）。

該則之內容為：R-C6 條文原文、Comfort 交付件 `G` 欄 466/466 =
`Climate Control Interface` 之實測、四份交付件之同批對照表、
以及三種可能成因之並列。**只記事實與證據，不判定成因、不提案修改
Comfort 之任何條文，未修改 Comfort 之任何交付物。**

回報之緣由亦寫入該則：R-PMH2 逐字引 R-C6 為其唯一依據，查證該前例時
發現不符，致 R-PMH2 之後半被撤回。

**本側交叉指引已加**：`ANOMALIES.md` 之 A-PMH07 標題列增列
「交叉指引 `features/comfort/ANOMALIES.md` A-CF-EXT-02」，
內文增列裁定段落（R-PMH13、分析層 4/4 複驗、連帶回報已發出）。
A-PMH07 → **RESOLVED**（本 feature 側；Comfort 側之處置由該 feature 自行判斷）。

---

## 6. Phase 1 recon（步驟 6）

`python scripts/recon.py --feature features/power_moding --root .`

```
assertions:
- PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
         — 29 cited / 52 outline entries in the export
recon complete: state=BLANK, leaves=48, sections=29, targets=48
0 failed / 1 checked.
```

### 6.1 leaf 全集之獨立重算（先算後比）

recon 依 `Categorization == Functional Requirement` 重算得 **48**，
與 01 包之 48 相符。**停止條件 9（≠48）未觸發。**

recon 另報一項對照向（R-G7-1）：若改用 `-NN` 子項形態之 id-suffix 判準，
只得 **27** leaf —— 會丟掉 21 個「父形態但自身即為 Functional Requirement」
之列（`SWE1-HMI-PM-002`／`-003`／`-004`／`-005`／`-007`／`-010` … 等）。
**R-PMH1 所定之判準（Categorization 全集）是對的，且此對照向證明另一個
看似合理的判準會漏 21 個。**

### 6.2 recon 之其餘要點

| 項 | 值 |
|---|---|
| `workbook_state` | **BLANK**（依 R-PMH8，未重判） |
| form layout revision | **C**（has Estimated Test Time） |
| 欄位對應 | 15 欄 ＋ `estimated_test_time` = 16，**由表頭文字解析**（recon 視 `feature.yaml` 之欄字母為 prior 而非權威）；**與 `feature.yaml` 零衝突** |
| done rows / draft rows | 0 / 0 |
| ambiguous rows | none |
| design-method vocabulary | 9 strings |
| regen targets | **48**（= 全部 leaf，BLANK 下之預期） |
| 037 之 traceability orphans | 0 |
| parent/child both-leaf duplications | none |
| safety attributes（ASIL/FTTI） | **ABSENT** —— 安全分析層在這些 leaf 上無附著點，不進 trace chain |
| spec text layer | 15,618 chars（recon 用 `pymupdf`；02 包用 `pdftotext -layout` 正規化後為 15,167 —— **不同工具之差異，非衝突**） |
| 章節分布 | leaf 章分布 7(19)／8(6)／9(5)／10(10)／11(5)／12(3) |

**欄位對應之第三方佐證**：recon 由表頭文字獨立解析所得之 16 欄，
與 02 包之手測、以及四方交叉佐證三者一致。

### 6.3 `DECISIONS.md` 之合併

recon 依 A-TM15 之防護未覆寫既有檔，另寫 `DECISIONS.new.md`。
原 `DECISIONS.md` 為 scaffold 模板，**全部欄位皆為未填之 placeholder，
無任何人工內容**（已逐節確認）。故合併方式為「以 recon 產出為底，
逐項補上 recon 不讀之 `RULINGS.md` 既裁條文」，**未丟棄任何既有內容**；
`DECISIONS.new.md` 已刪除。

補入之 `[RULED …]` 共 8 項：spec 基線分工（通則 3）、A-PMH03 指名複核項、
R-PMH10 前言三欄、DV 全量、R-G3 寫回機制、R-PMH13 之 G 欄值、
R-PMH16 之 `tc_id_format`、R-PMH18 之字面常數保真。
另將 H 欄標為 `[PEI — Phase 3]`（R-PMH6 之延後不受 R-PMH13 核可影響）。

**`RECON.md` 與合併後之 `DECISIONS.md` 全文見同目錄之該二檔。**

### 6.4 recon 另揭之一項（本包未處置）

RECON.md「Uncited baseline sections」節：baseline 52 項中
**23 項未被任何 leaf 引用**，且註明
「classification: **not produced** — `data/sr24_uncited_sections.tsv` absent;
run the feature's classify_uncited_sections.py」。

本 feature **無** `classify_uncited_sections.py`（`scripts/` 為空）。
23 項之組成已於 §7 分析（12 個章節層節點 ＋ ch1 之 5 個子節 ＋
5 個圖片佔位 ＋ `12.4`）。**是否需要該分類產物，本包不自行決定**，
列入 §9 之該驗而未驗者。

---

## 7. framework Layer 2 之候選輸入備料（步驟 7）

**只備料、只列交集與分歧；不擬 Test Set 名、不定 granularity。**

### 7.1 (a) 037 `FROP` —— 12 個相異值及其 leaf 分布

| leaf 數 | FROP | 涉及章 | outline |
|---|---|---|---|
| 12 | `Customizable Splash Screen / Animations` | 7 | 7.1, 7.5, 7.5.1, 7.6, 7.7, 7.8, 7.9 |
| 7 | `Disclaimer screen` | **7, 10** | 7.1, 7.2, 7.3, 7.4, 10.4 |
| 7 | `Audio Management` | **8, 12** | 8.1, 8.2, 8.2.1, 8.2.2, 8.2.3, 8.3, 12.3 |
| 5 | `Power Management` | **7, 9, 10, 12** | 7.1.1, 9.1, 10.5, 12.1, 12.2 |
| 5 | `Steering Wheel Controls` | 11 | 11.1 |
| 3 | `Bluetooth` | 10 | 10.6 |
| 2 | `FOTA Via Wi-fi` | 9 | 9.1 |
| 2 | `Rear View Camera` | 10 | 10.1, 10.2 |
| 2 | `Climate Control` | 10 | 10.3, 10.4 |
| 1 | `WiFi` | 9 | 9.1 |
| 1 | `EV/PHEV Pages` | 9 | 9.1 |
| 1 | `e-call (private)` | 10 | 10.7 |

合計 48，相異 12（口徑：A-PMH01 所採認之定義）。

### 7.2 (b) SYS1 `Outline Number` —— 52 項章節結構

層級分布：第 1 層 12 項、第 2 層 35 項、第 3 層 5 項。

| 章 | 標題 | 子節 | 引用 leaf |
|---|---|---|---|
| 1 | `Assumptions` | 5 | **0** |
| 2 | `Headunit Startup – Non-GDPR/NonMaserati` | 1 | **0** |
| 3 | `Headunit Startup – GDPR/Non-Maserati` | 1 | **0** |
| 4 | `Headunit Startup – Maserati/Non-GDPR` | 1 | **0** |
| 5 | `Headunit Startup – GDPR/Maserati` | 1 | **0** |
| 6 | `Passenger Screen Startup` | 1 | **0** |
| 7 | `Startup` | 11 | 19 |
| 8 | `Starup R1Low Only` | 6 | 6 |
| 9 | `Power Moding` | 1 | 5 |
| 10 | `Additional Power Moding Behavior Notes:` | 7 | 10 |
| 11 | `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS` | 1 | 5 |
| 12 | `Power Moding – Off Road+` | 4 | 3 |

### 7.3 交集與分歧

**A. FROP → 章：3 個 FROP 跨章**

| FROP | 章 |
|---|---|
| `Power Management` | **7, 9, 10, 12（跨 4 章）** |
| `Disclaimer screen` | **7, 10（跨 2 章）** |
| `Audio Management` | **8, 12（跨 2 章）** |

其餘 9 個 FROP 皆為單章。

**B. 章 → FROP：4 個章混合多個 FROP**

| 章 | FROP 數 | FROP |
|---|---|---|
| 7 | **3** | Customizable Splash Screen / Animations、Disclaimer screen、Power Management |
| 9 | **4** | EV/PHEV Pages、FOTA Via Wi-fi、Power Management、WiFi |
| 10 | **6** | Bluetooth、Climate Control、Disclaimer screen、Power Management、Rear View Camera、e-call (private) |
| 12 | **2** | Audio Management、Power Management |

章 8（Audio Management）與章 11（Steering Wheel Controls）為單一 FROP。

**分歧之結論（描述，非提案）**：FROP 與規格章節為**多對多**關係 ——
3 個 FROP 跨章、4 個章混 FROP。**兩項輸入單獨任一項都切不出乾淨的分割**：
- 只用 FROP → 章 7／10 之 leaf 會被拆到不同 Test Set；
- 只用章 → `Disclaimer screen` 之 7 個 leaf 會被拆成 5(ch7) + 2(ch10)，
  而本 feature 之交付夾名恰為 `Disclaimer screen`。

**唯一之完全一致區**：章 8 ↔ `Audio Management`、章 11 ↔ `Steering Wheel
Controls` —— 二者互為單一對應。

**C. 未被 leaf 引用之 outline（23 項）**

`1`, `1.1`–`1.5`（Assumptions 及其 5 子節）、
`2`, `2.1`, `3`, `3.1`, `4`, `4.1`, `5`, `5.1`, `6`, `6.1`（五張啟動流程圖之章與節）、
`7`, `8`, `9`, `10`, `11`, `12`（六個章節層節點本身）、`12.4`（Off Road+ 之流程圖）。

即：**未引用者恰為「章節層節點」＋「Assumptions 全章」＋「6 個圖片佔位」**
（A-PMH04 之六者全在其中）。無一項是帶實質需求文字而被漏引的。

---

## 8. 02 包 §11 之逐項處置（步驟 8）

> 下放包稱「五項」，**02 包 §11 實為六項**。六項全部處置如下，未略。

| # | 02 §11 之項 | 本包之處置 |
|---|---|---|
| 1 | 母本 `P10:Q1411` DV 列舉值未實測 | **已清償** —— §2.1／§3。`"P0,P1,P2,P3"`，二證同值；四份交付件逸出 0。**且原評估過高，已自我更正**（§3 末段） |
| 2 | `T10:Z1411`／`AF10:AF1411` 列舉值未讀 | **已清償** —— §2.1。`"0,1"` 與 `"Pass, Fail, Pending,Block,NA"`；`allowBlank=1` 故留白合法。另揭 `AF` 列舉含前導空白（§2.1 ⚠） |
| 3 | 母本封面三頁未讀 | **已清償，且有意外收穫** —— 見 §8.1。母本三頁登記如下；客戶那份之同三頁揭出 **A-PMH09** |
| 4 | `outline_map.json` 之 `row_036_customer` 語意風險未防呆 | **已處置** —— `feature.yaml` 之 `workbook` 節增列警語：該欄記客戶那份之列號，**不是寫回目標列**；母本為 BLANK，目標由 `write_back.first_row` 起之 append 決定。任何以該欄定位寫回之程式即為缺陷 |
| 5 | 步驟 8 之可辨讀性判定為人工目視，無機器判準（通則 8） | **維持未做，理由明載** —— 03 包未指派此工作，且 A-PMH04 仍為 PENDING，其解除須待 Phase 4 實際 render 取用時。屆時之機器判準提案：對 render 圖跑 OCR，比對已知字串（如 `IMPORTANT`、`Loading…`、`Drive Modes`）之命中率。**本包不自行實施** |
| 6 | `Reference!C9` vs `下拉選單!A6` 字串不一致未立條（自陳「判斷可能過輕」） | **已補登為 A-PMH10** —— 且證據較 02 包更強：**表單自身之 `ChangeHistory` ver A 第 5.g 項亦作 `Pair-wise / N-wise`**，即三處中兩處一致，不一致者恰是實際生效之 DV source。lint 權威仍取 `下拉選單`（實務逸出 0） |

### 8.1 母本封面三頁之登記（清償 01 §9 第 4 項 ＋ 02 §11 第 3 項）

| 分頁 | 母本實測 |
|---|---|
| `Cover 封面` | `C4` 文件名；**`D6` 版本 = `C`**；`D7` 核准者 = `劉安哲 AllenACLiu`；`D8` 審查者 = `張愷霏 ErinKFChang`；**`C9` 作者欄之值為空**（只有標籤，無值）；`H30` = `FM-WI-FSM-036-A01` |
| `ChangeHistory 修訂履歷` | 三列 A／B／C，修訂人皆 `張愷霏 ErinKFChang`、核准者皆 `劉安哲 AllenACLiu`；ver C（2026-01-21）逐字為「新增欄位：預估測試時間(分鐘)／Add new column: Estimated Test Time (mins)」 |
| `Product Document 記錄封面頁` | **僅標籤，值全空**（`B3`–`B8`、`A13` 起之修訂歷史列皆無值） |

**01 包 §9 第 4 項所記之「核准者 劉安哲、審查者 張愷霏、作者欄空白」
於母本複驗屬實。**

### 8.2 意外收穫 —— A-PMH09（客戶那份帶 AMFM 血緣）

讀客戶那份之同三頁時發現：其 `ChangeHistory` **ver C 列已被覆寫**為

```
Added 143 test cases covering the 102 leaves of FM-WI-FSM-037-A03, appended from row 168.
The 158 existing rows are unchanged — verified by an ordered content hash over columns D..AG, not by row position.
Corrected the header 範圍 Scope field (D5), which named the superseded requirement report: FM-WI-SW-RAD-SWRA-A02 -> SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323.
```

修訂人 `PeiPYHsu`，日期 `2026-08-10`。

**這是 AMFM feature 之寫回註記**，三項證據：字串含 **`SWE1_AMFM`**；
數字 143 TC／102 leaf／自 r168 append／既有 158 列，**與本 feature 之
48 leaf、0 TC、r10–57 無一相符**；其所述之 `ordered content hash over
columns D..AG` 為本管線 `PARTIAL_INTERLEAVED` 之 done invariant 作法。

**此可解釋 01／02 包所測之三項離群**：35 欄版面、`Cover!D6` 版本為 `A`
（而其 ChangeHistory 有 A/B/C 三列 —— **檔案自相矛盾**）、多出之 `D5:F5` 合併。
另一項自相矛盾：該註記聲稱已把 `D5` 修正為指向 `SWE1_AMFM_…`，
而 01 包實測客戶那份之 **`D5` 為空白** —— 註記所述之修改在檔案中不存在。

**影響為零**（R-PMH7 已改用母本），但這是 **R-PMH7 之回溯性佐證**：
該判準所排除的，確實是一份帶著他 feature 血緣與自相矛盾中繼資料之檔案。
**若 02 包沿用了它，Phase 7 會把 AMFM 之修訂履歷一併交給客戶。**

`feature.yaml` 之 `customer_source_copy` 註解已據此收緊：**其封面三頁
不得取用**；R-PMH7 所稱之「附屬分頁」僅指 `Reference`／`QS Suggestion`／
`Test Case Framework`。

A-PMH09 之提案 (c)（是否回報 AMFM feature）**未逕行** —— 本 feature 只看到
衍生物，未查 AMFM 之交付件本身，請分析層判斷是否值得一查。

---

## 9. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **`data/sr24_uncited_sections.tsv` 未產出**（RECON.md 明點）。
   23 項未引用 outline 之組成已於 §7.3 分析（全為章節層節點、Assumptions
   全章、6 個圖片佔位），**看似無實質遺漏**，但這是我讀出來的結論，
   不是機器分類的結果。本 feature 無 `classify_uncited_sections.py`
   （`scripts/` 為空）。**是否需要該產物，本包不自行決定。**

2. **`Q` 與 `AF` 兩欄之 DV 從未被實際檢驗過**（四份交付件皆全空）。
   §2.1 指出之兩項瑕疵（`Q` 套用 P0–P3 下拉、`AF` 列舉含前導空白）
   **要到 Phase 6／7 首次填值時才會浮現**。本包只登記，未提解法。

3. **A-PMH09 之推論未經 AMFM 側查證。** 「客戶那份衍生自 AMFM 交付件」
   之三項證據皆取自該檔自身，**未開啟 AMFM 之任何交付件比對**
   （欄數、`Cover!D6`、`D5:F5` 合併是否相符）。若要把推論升為結論，
   需要那一步。本包未做 —— 那份不在本 feature 之素材範圍內。

4. **`RECON.md` 之 `spec text layer` 為 15,618 chars（pymupdf），
   02 包為 15,167（pdftotext -layout 正規化後）。** 我於 §6.2 稱其為
   「不同工具之差異，非衝突」—— **但未實測驗證此說**。差 451 字元（3%）
   之成因未追。若日後有人以字元數當作 spec 完整性之判準，這 3% 需要解釋。

5. **`write_back` 之 `mode: append` 與 `first_row: 10` 尚未有任何機器檢查。**
   R-PMH8 裁定自 r10 起 append，`feature.yaml` 已記，但**沒有任何 lint 或
   assertion 會在寫回時驗證它**。§8 第 4 項所加之 `row_036_customer` 警語
   同樣只是註解 —— **通則 8 明言「文字修補不構成 RESOLVED」**，
   這兩項目前都只是文字修補。

---

## 10. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 —— recon assertion 1/1 PASS，29/29 命中 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 —— `BLANK`（R-PMH8），recon 複現，ambiguous rows = none |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 —— A-PMH09／A-PMH10 皆為登記型，未需新規則 |
| 5 | 造值壓力 | 未觸發 —— §7 只列交集與分歧，未擬任何 Test Set 名或 granularity |
| 6 | done region 與規格矛盾 | 未觸發 —— 無 done region |
| 7 | 母本 `priority` DV 與 canon §10.2 不一致 | **未觸發** —— 二者皆為 `{P0,P1,P2,P3}`，完全相同（§3） |
| 8 | 任一欄之交付件實際值逸出母本 DV | **未觸發** —— 五組 DV × 四份交付件，**逸出 0**（§4） |
| 9 | leaf 全集重算 ≠ 48 | **未觸發** —— recon 獨立重算得 **48**（§6.1） |

---

## 11. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 03 — test group ruled, DV audit, phase 1 recon
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/RECON.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/data/recon_leaf_to_section.tsv \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/03_testgroup_and_dv.md \
           features/power_moding/docs/handoff/03a_pei_rulings.md \
           features/power_moding/docs/upstream/03_testgroup_and_dv.md \
           features/comfort/ANOMALIES.md

git commit -- features/power_moding/ANOMALIES.md \
              features/power_moding/DECISIONS.md \
              features/power_moding/RECON.md \
              features/power_moding/RULINGS.md \
              features/power_moding/feature.yaml \
              features/power_moding/data/recon_leaf_to_section.tsv \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/03_testgroup_and_dv.md \
              features/power_moding/docs/handoff/03a_pei_rulings.md \
              features/power_moding/docs/upstream/03_testgroup_and_dv.md \
              features/comfort/ANOMALIES.md
```

- **`features/comfort/ANOMALIES.md` 在 pathspec 內** —— 步驟 5 之連帶回報。
  這是本輪唯一觸及本 feature 目錄以外之檔案，特此標明。
- `data/recon.json` 依 `.gitignore` 不入版控；`data/outline_map.json` 與
  `data/recon_leaf_to_section.tsv` 入版控（後者為 R-G4-1 所定，
  其三個讀者為 `lint_tcs.py`／`make_batch_context.py`／`extract_exemplars.py`）。
- `DECISIONS.new.md` 已刪除，不入 pathspec。
- pathspec 逐項寫全名，未用萬用字元（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 11.1 git 動作揭露（R-G6，唯讀／改狀態分列）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

本輪未執行任何 git 指令（02 包之 `check-ignore` 與 `add --dry-run` 屬該輪）。

---

## 12. 本輪之全部工作區動作

| # | 動作 | 對象 |
|---|---|---|
| 1 | heredoc 追加 ＋ 就地改寫 | `RULINGS.md` —— 03 三條 ＋ 03a 四條 ＋ 核對表 ＋ R-PMH11 附註（原文未動） |
| 2 | Python 就地改寫 | `feature.yaml` —— `test_group` → `Disclaimer screen`、新增 `tc_id_format`、`write_back.test_group_value`／`test_set_value`、A-PMH09 與 `row_036_customer` 之警語 |
| 3 | `python scripts/recon.py` | 產出 `RECON.md`／`DECISIONS.new.md`／`data/recon.json`／`data/recon_leaf_to_section.tsv` |
| 4 | Python 寫檔 ＋ `unlink` | `DECISIONS.md` 合併，刪除 `DECISIONS.new.md` |
| 5 | heredoc 追加 | **`features/comfort/ANOMALIES.md`** —— A-CF-EXT-02（本 feature 目錄以外之唯一異動） |
| 6 | heredoc 寫檔 | `ANOMALIES.md` —— A-PMH06／07 改 RESOLVED（06 附 PENDING-CANON）、新增 A-PMH09／10 |
| 7 | heredoc 寫檔 | `docs/upstream/03_testgroup_and_dv.md`（本檔） |
| 8 | heredoc 寫檔 | `docs/INDEX.md` 補本輪次列 |

**對任何工作簿之儲存格寫入：無。**
**對唯讀來源（`forms/`、四個 ASW-R2 交付夾）之寫入：無。**
**`scripts/new_feature.py` 未改**（03a §四之禁止項）。

---

## 13. 03a §六之增列二項

### 13.1 03a 四條之抄錄核對表

見 §1 之表（後四列）。**R-PMH13 加註之原文 SHA256 未變之證明**：
03a 之第一個區塊為「`R-PMH13 之生效`」，係**獨立新條**而非對 R-PMH13
原文之修改；03 包之 R-PMH13 原文區塊落地後獨立再抽取，SHA256 為
**`6e163ef260ff31e6`**，與其 handoff 原文相同。二者在 `RULINGS.md` 中
各自成節，原條文一字未動。

### 13.2 `feature.yaml` 落地後之大小寫敏感驗證（R-PMH18）

```
test_group    = 'Disclaimer screen'
  逐字相符（大小寫敏感，vs 'Disclaimer screen'）      : True
tc_id_format  = 'NR1L-DisclaimerScreen-{NNN}'
  逐字相符（大小寫敏感，vs 'NR1L-DisclaimerScreen-{NNN}'): True

G 欄值去空白        = 'DisclaimerScreen'
tc_id abbr          = 'DisclaimerScreen'
二者是否刻意不同     : True   （'Disclaimer screen' != 'DisclaimerScreen'）
去空白後大小寫不敏感是否相同 : True   ← 證明差異僅在大小寫，非拼字
write_back.test_group_value 與 test_group 一致 : True
write_back.test_set_value                      : None（R-PMH6 待 Phase 3）
```

**R-PMH18 之要求滿足**：二字串逐字相符於其裁定值，且**確實不同**
（差異僅在空白與 `s`／`S` 之大小寫），未被任何正規化統一。
