# 04 — Power Management framework 定版（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 04
結果：**十四步全部完成，無停止。G13b、G17–G20 全數量測完成。**
§E 仍待定版 —— 阻斷項收窄為 `SWE-PM-008` / `SWE-PM-057` 兩條之 Test Set 歸屬。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| 建立 `handoff/04_framework_lock.md` | DONE（原不存在；§A 9 區塊 / §J 9 列 / §H 14 步，自檢一致） |
| 1 G0 前置閘 | **PASS 7 / 7** |
| 2 `layer3_full.tsv`（R-P24），驗 G13b | DONE —— 140 列，**G13b = 46 PASS** |
| 3 §E 訂正 §1.8.1 → §1.8.1.1.1（R-P25） | DONE |
| 4 B1（`SWE-PM-008` 素材） | DONE，無建議歸屬 |
| 5 B2（9 章判定素材） | DONE |
| 6 B3（SYS3 交叉比對），驗 G20 | DONE —— **G20 = 否** |
| 7 章節層反向缺口（R-P28），驗 G17 | DONE —— 242 章未觸及，其中 171 章含 499 個需求錨點 |
| 8 A-PW06 複驗（R-P31），驗 G18 | DONE —— **逐字成立** |
| 9 037 全欄空值率（§C(ii)），驗 G19 | DONE —— **18 欄皆 0 空值** |
| 10 R-P29 / R-P30 落實 | DONE，訂正前後全文見 §七 |
| 11 A-PW15 加註下游影響（§C(i)） | DONE |
| 12 §D 全表自驗 | DONE |
| 13 §A 九條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE（RULINGS 現含 R-P1–R-P32 連續無缺；ANOMALIES A-PW01–A-PW20） |
| 14 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

### 本包三項最重要之結果

1. **G20 結論為否，且是確定的否。** SYS3 之「動態行為」七個狀態子節
   （R-P32 指定之切入點）Sys-RA token 數**全為 0**。名稱七項全對得上，
   卻無任何 leaf 可被指派。§E 之「單一來源」弱點確認成立且無法以 SYS3 消除。
2. **R-P28 之章節層缺口完全內含於 R-P7 已裁定不追之需求層缺口。** 見 §六。
3. **執行層自陳一項錯誤**：03 §九第 4 項「七條 Requirement Title 為空」為誤。
   實測 037 全 18 欄零空值（G19）。詳見 §八。

---

## 一、下放包自檢與一項登記

11,025 → 13,561 bytes，strict UTF-8 通過，U+FFFD = 0。
**§A 區塊數 = 9**（`R-P24…R-P32`）、**§J 列數 = 9**、**§H 步驟數 = 14**
（其中步驟 13 寫「九條」），與 §J 自檢所稱三處一致。§D 新增列 = G13b / G17–G20。

> **登記一項事實（未自行修正）**：04 §前言稱「03 包所提之 R-P29（分析層未讀即裁准）
> 因此不再需要」。查 03 上繳包 §十一之待裁項為 Q1–Q8，**執行層並未提出任何
> 編號為 R-P29 之條文**，亦未提出「分析層未讀即裁准」之議題。
> 該敘述所指者不存在於 03 上繳包。本包之 R-P29 為 A-PW05 訂正，編號無衝突，
> 故不影響任何條文效力，僅於此登記。

---

## 二、§D 全表實測值對照（**上繳項二**）

G0–G16 由 `python features/power/scripts/verify_gates_03.py` 產出，
G13b 由 `build_layer3.py`，G17–G20 由本包之量測（見各節）。

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | **7 / 7** | PASS |
| G1 | 037 leaf 數 | 115，連續無斷點 | 115，連續=True | PASS |
| G2 | Categorization 值域 | `Functional Requirement` ×115 | 相同 | PASS |
| G3 | leaf → CFTS 章節解析成功數 | 114 / 115，失敗 `SWE-PM-089` | 相同 | PASS |
| G4 | leaf 域分布 | 111 / 3 / 1，互斥 | 相同 | PASS |
| G5 | 需 CFTS010 之 leaf | `071` `072` `073` | 相同 | PASS |
| G5b | 該三 leaf 之解析章節 | 071/072→§1.7.1.1.1、073→§1.7.2 | 相同 | PASS |
| G6a | SYS2 CFTS009 token 可抽取率 | 337 / 338 | **337 / 338** | PASS |
| G6b | token 可解析至章節之比率 | 列層 336 / 337 | **列層 336 / 337；token 層 438 / 439** | PASS |
| G7 | SYS2 CFTS010 全 id 可解析者 | 73 / 73 | 相同 | PASS |
| G8 | CFTS009 需求 / 章節錨點 unique | 904 / 196 | **904 / 196** | PASS |
| G9 | CFTS010 需求 / 章節錨點 unique | 148 / 92 | **148 / 92** | PASS |
| G10 | FW036 workbook_state | BLANK | 非空 0 → BLANK | PASS |
| G12 | §C 各組讀取座標 | 與 §C 一致 | 六組全數相符 | PASS |
| G13 | 跨多章節 leaf 數 | 11 | **11** | PASS |
| G14 | 次章節涵蓋 | 丟棄 10 / 未覆蓋 9 | 相同 | PASS |
| G15 | 037 兩分頁座標與列數 | Traceability r2–r34＝33；Excluded r2–r27＝26 | 相同 | PASS |
| G16 | SYS3 章節錨點數 | 0 | **0** | PASS |
| **G13b** | Layer 3 全集之相異章節總數 | **46** | **46** | **PASS** |
| **G17** | 章節層反向缺口 | 【實測填入】 | 288 章中未觸及 **242**；其中含需求錨點 **171 章 / 499 錨點**，純標題殼 71 章 | 已填空 |
| **G18** | A-PW06 複驗 | 【實測填入】 | 值域恰 5 值，計數逐一相符（36/35/27/16/1 = 115）→ **逐字成立** | 已填空 |
| **G19** | 037 全 18 欄空值率 | 【實測填入】 | **18 欄皆 115/115 非空，零空值**。`Requirement Title` 空值數 = **0** | 已填空 |
| **G20** | SYS3 交叉比對結論 | 【實測填入】 | **否** —— SYS3 不構成第二來源。四種失敗形態見 §五 | 已填空 |

**十八項有明確期望值者全數 PASS；四項填空項已填。無 MISMATCH。**

---

## 三、Layer 3 全集（R-P24，G13b）

`features/power/data/layer3_full.tsv`，產生指令
`python features/power/scripts/build_layer3.py`。

結構（逐 `(leaf, 章節)` 一列，一 leaf 可多列）：
`leaf / cfts / chapter_num / chapter_title / hit_count / item_ids / tokens`。
排序為 leaf 數字序 → 章節號數字序，故可重現、可 diff。

| 指標 | 實測 |
|---|---|
| 總列數 | **140** |
| 涵蓋 leaf | 114 / 115（`SWE-PM-089` 無列，R-P1） |
| **相異章節總數（G13b）** | **46** |
| 每 leaf 章節數分布 | 1 章 ×103、2 章 ×1、3 章 ×7、4 章 ×2、6 章 ×1 |

**A-PW16 之 9 章因 R-P24 已全部進入 Layer 3。** 該 9 章之問題因此從
「Layer 3 是否記錄」轉為「其行為是否被 leaf 之 Description 涵蓋」—— 即 B2 所答者。

---

## 四、B1 —— `SWE-PM-008` 之 Test Set 裁定素材（**上繳項一之一**）

全文見 `features/power/data/b1_swepm008.md`（8,362 bytes）。**無建議歸屬。**

| 項目 | 實測 |
|---|---|
| Requirement Title | **`Logistic Mode`** ——「03 §四實測為空」之說法為誤，見 §八 |
| Source Requirement ID | 13 個 token（`Sys-RA-PM-0013/0014/0040`–`0045/0056/0184`–`0187`） |
| 六個相異章節命中數 | §1.6.2.1 ×2、§1.6.2.1.9 ×3、§1.6.2.1.10 ×2、§1.6.2.1.11 ×2、§1.6.2.1.14 ×1、**§1.6.7.1 ×4** |
| Description | 「HW supplier shall notify Logistic state (Logistic Idle/ Logistic Standby / Lgistic Sleep) though custom power state interface / subcomponents shall ensure no features are availabel and prepare to shutdown」 |
| Verification Method | 「Change signal `STATUS_BH_BCM1.PowerModeSts` to "Logistic_Mode_On" / HU shall shutdown and no functionalities available」 |

§1.6.7.1 之標題實測為 **`TLM algorithm requirements`**（與 §1.6.2.1 同名），
其首段為「When the Logistic Mode is active (signal `PowerModeSts_Telematic` ==
"Logistic_Mode_On"), …」。

**歸屬後果**（以 `SWE-PM-057` 歸 Power State 為基準）：

| 情形 | Power State | Startup Display | Branding | Timeout Settings | Power Down |
|---|---|---|---|---|---|
| 歸 Power State | 63 | 24 | 16 | 7 | 3 |
| 歸 Timeout Settings | 62 | 24 | 16 | 8 | 3 |

---

## 五、B2 / B3（**上繳項一之二、之三**）

### B2 —— A-PW16 之 9 章判定（`data/b2_uncovered_chapters.md`，27,357 bytes）

| 章節 | 標題 | 所屬 leaf | 判定 |
|---|---|---|---|
| §1.6.2.1 | TLM algorithm requirements | `SWE-PM-001`~`009` | **無法判定** |
| §1.6.2.1.4 | Stolen Vehicle Mode | `SWE-PM-003` | **未涵蓋**（但見下） |
| §1.6.2.1.9 | Logistic Idle | `SWE-PM-008` | 部分涵蓋 |
| §1.6.2.1.10 | Logistic Standby | `SWE-PM-008` | 部分涵蓋 |
| §1.6.2.1.11 | Logistic Sleep | `SWE-PM-008` | 部分涵蓋 |
| §1.6.2.1.14 | TLM modules … operative state | `SWE-PM-001`~`009` | 部分涵蓋 |
| §1.6.2.1.15.1 | ICS Wakeup Reasons by POWER Button Pressed | `SWE-PM-004` | 部分涵蓋 |
| §1.6.3.1.1 | SwitchOff_Timeout_Setting.Req management | `SWE-PM-057` | 涵蓋（一分支例外） |
| §1.8.1.1.1 | ID 1 Description | `SWE-PM-057` | **涵蓋** |

三項須特別呈報：

- **§1.6.2.1 判定「無法判定」** —— 其文字層僅含兩個 inline RTF 之
  `WrapperResource` 參照（`CFTSMV009_CIP_R4_O829_4_inline.rtf` 等），
  無任何可判讀之行為敘述。實質內容為嵌入物件，**不在文字層內**。
- **§1.6.2.1.4 Stolen Vehicle Mode —— A-PW16 之描述需修正。**
  該章有兩個需求錨點，`SWE-PM-003` 經 `Sys-RA-PM-0031` **只引用 `4941400`**
  （`layer3_full.tsv` 該列 `hit_count=1`）。`4941399`（進入條件，`Radio` 欄
  `VP4R7, VP4R84` 不含 R1L）**未被任何 leaf 引用**。
  而 `4941400` 逐字為「**the R1 HU shall not enter stolen vehicle mode
  under any condition**」，`Radio` 欄含 `R1L`。
  故本章在範圍內之唯一需求是一條**否定需求**，不是「防盜功能」。
  A-PW16 稱其為「實質功能章節」在此一點上不準確。
- **§1.6.2.1.10 與 §1.6.2.1.11 之唯一差異為 network active / network off**，
  而 `SWE-PM-008` 之 Description 不含 `network` 一詞，故無法據以區分此二章。

### B3 —— SYS3 交叉比對（`data/b3_sys3_crosscheck.md`，8,250 bytes）

**連結方式**：03 包測得 G16 = 0（無字面章節號），但本包實測 SYS3 文字層
含 **`Sys-RA-PM-` token 630 個出現、272 個相異** —— 與 037 同一命名軸，故可連結。
token 歸屬於其前最近之 `Heading1`/`Heading2`（與 §C rule 2 同構）。
另實測 `Sys-RA-PD` 0 個、`NRL-` 0 個、6–8 位數字 0 個、`SWE-PM-` 0 個。

**§4.x 之 36 項中僅 11 節帶 token**，且高度集中：

| SYS3 節 | token 數 |
|---|---|
| §4.28 分配系統需求 Allocate System Requirements | **230** |
| §4.3 系統需求–概述 System Requirements – Overview | **214** |
| §4.11 Assumptions | 40 |
| §4.16 Power State Transition | 21 |
| §4.24 Antitheft | 19 |
| §4.25 Front Panel On Off Sequence | 12 |
| §4.21/§4.22/§4.23 Splash — Cold/Warm Boot、Idle to Full Operation | 3 / 3 / 3 |
| §4.18 Phone Call、§4.20 Start-up Animation | 2 / 2 |

**七個狀態子節（§4.30–§4.36）token 數全為 0**，其父節 §4.29「動態行為」亦為 0。

七項名稱與 CFTS009 之對照：Sleep→§1.6.2.1.7、Standby→§1.6.2.1.6、
Full Operation→§1.6.2.1.1、Idle→§1.6.2.1.2、Timed→§1.6.2.1.5、
Partial Operation→§1.6.2.1.3、Bench→§1.6.2.1.8。**七項全對得上。**
SYS3 有而 CFTS 無：**無**。CFTS 有而 SYS3 無：**6 項** —— Stolen Vehicle Mode、
Logistic Idle / Standby / Sleep、Init、TLM initialization: Init state。
（其中前四項正是 A-PW16 之 9 章中的四項；此為觀察，非處置建議。）

**與 §E 之交叉**：可經 SYS3 分節之 leaf 111/115（`071/072/073` 與 `089` 無對應）；
僅 21 個 leaf 對到單一節，53 個對到 2 節、23 個對到 3 節、最多 6 節。
去除兩個大宗表格節後之分歧：`Splash — Cold/Warm Boot/Idle to Full Operation`
共 8 個 leaf 出現，**全落 §E 之 Power State**，而 §E 將 Splash Screen
（§1.6.2.1.16）歸 **Startup Display** —— 兩軸對 Splash 之歸屬相反。
`Antitheft` 10 個 leaf 全落 Power State，§E 無對應項。
`Branding and Theme` 16 leaf 除大宗表格外無任何特徵節對應
（SYS3 全篇無 Branding / Theme 標題）。

**G20 = 否。** 四種失敗形態：（1）無 leaf 對應 —— 指定切入點 token 全 0；
（2）分類軸不同 —— 549 個歸屬中 444（81%）落在兩個分配矩陣節，以之分群等同不分群；
（3）粒度不符 —— 僅 21/111 對到單一節；（4）覆蓋面不足 —— CFTS010 全域無對應。

→ 登記為 **A-PW20**。**§E「不是交集、只由單一來源支撐」之弱點確認成立，
且無法以 SYS3 消除。** 這是一個確定的結論，非懸而未決。

---

## 六、G17 —— 章節層反向缺口（R-P28）及一項須並陳之重疊

| 指標 | 實測 |
|---|---|
| 全部章節 | **288**（CFTS009 196 + CFTS010 92） |
| 被 leaf 觸及 | **46**（16.0%） |
| 未觸及 | **242** |
| ├ 含需求錨點者 | **171 章，共 499 個需求錨點** |
| └ 無需求錨點（純標題／定義殼） | **71 章** |
| 被觸及之 46 章所含錨點 | 553 |
| 全部需求錨點 | 1052（904 + 148） |

未觸及者依結構分類：被觸及章節之祖先 20、後代 19、無祖裔關係 203。
深度分布：1 層 5、2 層 37、3 層 59、4 層 43、5 層 66、6 層 10、7 層 14、8 層 8。

未觸及且錨點最多者前五：CFTS009 §1.3.3.5 `Power up Sequence`（23）、
CFTS010 §1.4.1.3 `High Voltage Behavior`（22）、CFTS010 §1.4.2 / §1.4.3
`System Power Down Conditions`（13 / 12）、CFTS010 §1.7.1.1.2 `TLM Shutdown`（12）。

### 須並陳：本缺口與 R-P7 已免除者重疊

未觸及章節之 499 個錨點，依定義**全部**屬「未被 037 引用」者
（若其中任一被引用，該章即成為被觸及章節）。實測未被 037 引用之錨點總數為
**814**（CFTS009 669 + CFTS010 145）。即：

> **R-P28 之章節層缺口（499）完全內含於 R-P7 已裁定「不追、不問、不列 RD-1」
> 之需求層缺口（814）。**

R-P28 之前提「章節層不在 R-P7 射程內」形式上成立 —— R-P7 的確只寫需求層。
但其**內容**與 R-P7 所免除者重疊，差別僅在聚合單位。
本包依指示完成量測，不作處置；是否續行為裁決事項（見 §十）。

**另登記 A-PW19**：R-P7 條文內嵌之「CFTS009 本文未被引用之 547 條」，
實測為 **669**。該值出自 R-P10 已宣告失效之衍生物。
R-P7 之裁決效力不受影響，僅其條文數字為失效值；依「不得修改裁決條文」未動 R-P7。

---

## 七、R-P29 / R-P30 之訂正前後全文（**上繳項三**）

### A-PW05（R-P29，整條替換）

**訂正前**：

> 037 內部 id 命名空間不一致：`SWE1 Requirements` 用 `SWE-PM-001..115`，
> `SYS2 Traceability` 用 `SWE1-PM-TLM-001..033` / `-ANT-`

**訂正後**（依 R-P29 逐字）：

> 037 內部 id 命名空間不一致：SWE1 Requirements 分頁用
> SWE-PM-001..115（115 筆連續）；SYS2 Traceability 分頁用
> SWE1-PM-TLM-001..033（33 列，前綴分布單一）。
> 該分頁 SWE-PM- 出現 0 次，兩套互不對應。
> 實測附註：SWE1-PM-ANT- 命名空間不在本分頁，
> 其唯一出處為 SWE-PM-089 之 Source Requirement ID 欄（見 A-PW01）。

證據欄同步更新為 03 包複驗值。新增 **A-PW18** 登記誤植本身。

### A-PW03（R-P30，加註）

原描述與證據欄未動，於狀態欄末加註（逐字）：

> 加註（03 §六複驗）：分頁名為 Excluded NRLs (HW-only)，
> 但 26 列之 SW/HW/System 欄實測為 HW 18 / Information 4 /
> Out of Scope 2 / Heading 1 / 空白 1。
> 故『(HW-only)』在分類上亦不實，不僅是涵蓋範圍不足；
> 原描述只指出後者。

**A-PW04 未動**（複驗逐字成立）。

### A-PW06（R-P31，G18）—— 逐字成立，無須訂正

| 值 | 01 包所稱 | 實測 |
|---|---|---|
| `HMI` | 36 | **36** |
| `Service\nHMI` | 35 | **35** |
| `Service` | 27 | **27** |
| `HMI Service` | 16 | **16** |
| `HMI/Service` | 1 | **1** |
| 合計 | 115 | **115**，相異值恰 5 個 |

附註：`Service\nHMI` 之分隔為換行字元 U+000A，非空格 —— 匯入時若正規化空白會併入 `Service HMI`。

### A-PW15（§C(i)，加註下游影響）

於狀態欄末加註：81 個章節錨點 token 於 Phase 4 產生 `specification_reference` 時，
其引用對象為章節而非需求，引用格式將與其餘 357 個需求錨點 token 不同；04 包不處理，僅登記。

---

## 八、執行層自陳一項錯誤 —— 03 §九第 4 項為誤

03 上繳包 §九第 4 項稱「§四表中 #3–#9 七條之 `Requirement Title` 為空」，
並據以主張「037 其餘 16 個欄位的空值率從未量測」。

**該陳述為錯。** G19 實測：

| 欄 | 非空 / 115 |
|---|---|
| 全 18 欄（`SWE-Requirement ID` … `Verification Method`） | **115 / 115，逐欄零空值** |

`Requirement Title` 之空值數為 **0**。11 條跨章節 leaf 之標題實測為
`Full-Operation` / `Idle` / `Partial Operation` / `Timed` / `Standby` / `Sleep` /
`Bench` / **`Logistic Mode`** / `Init state` / `Proxi Parameter management` /
`Start-Up Animation Playback and Skip Logic - Suspend-Resume`。

**成因**：03 上繳包 §四之概覽表以「—」代替 #3–#9 之標題，係執行層排版時之簡寫；
`data/multi_chapter_leaves.md`（03 包 B1 本體）自始即載有正確標題，
其中第 8 條逐字為「**Requirement Title**：Logistic Mode」。
執行層在撰寫 §九時誤將概覽表之「—」讀為實測值。

**影響**：04 下放包 §B1 據此寫「Requirement Title（03 §四實測為空，如實回報）」，
§C(ii) 亦以此為量測動機之一。G19 之量測本身有價值（確立 037 無空值），
但其前提之一為執行層之錯誤陳述。已於 `data/b1_swepm008.md` 就地標註訂正。

---

## 九、獨立判斷：本包是否仍有該驗而未驗者（**上繳項四**）

03 上繳包 §九之六項，本包處置：第 1 項→R-P24（Layer 3 記全集，G13b=46）；
第 2 項→R-P28（G17 已量測）；第 3 項→R-P31（G18 逐字成立）；
第 4 項→§C(ii)/G19（**該項本身為執行層之誤，見 §八**）；第 5 項→§C(i)（已加註）；
第 6 項→R-P32（G20 已得確定結論）。**六項全部落地。**

**以下為執行層自判之新增未驗項，共六項。**

### 1.（最重）B2 之九項判讀為執行層之自然語言比對，無任何獨立驗證

本包全部產出中，只有 B2 的「涵蓋 / 部分涵蓋 / 未涵蓋 / 無法判定」
不是機械量測，而是**執行層讀規格與 Description 後的判斷**。
它沒有可重現的判準、沒有第二意見、沒有腳本。
而 R-P27 正是要用它決定 9 章是否為真實 coverage hole。

本包自己就示範了這種判讀的脆弱：§1.6.2.1.4 初判「未涵蓋」，
補查 `layer3_full.tsv` 後才發現該章只有 `4941400` 被引用，
且它是一條否定需求 —— 判定結論未變，但**其意義完全改變**。
其餘八章未做同等深度的引用層複查。
**建議：把「該 leaf 實際引用了該章的哪幾個錨點」作為 B2 的必填欄位，
而非事後補查。** 現行 B2 是「章 vs leaf」比對，正確的單位應是「被引用之錨點 vs leaf」。

### 2. Layer 3 之邊界仍由副作用定義，非由設計定義

R-P24 解決了「一 leaf 多章節」，`layer3_full.tsv` 記了 46 章。
但**為什麼是這 46 章**？答案是「因為有 leaf 觸及」——
這是錨點鏈的副作用，不是任何人對「本 feature 的規格範圍」所做的決定。
G17 顯示另有 171 個含需求錨點的章節未被觸及。
Layer 3 目前無準則可回答「某章是否屬於 Power Management 的規格範圍」，
只能回答「某章是否碰巧被引用」。R-P28 觸及了這個問題但停在量測。

### 3. §1.6.2.1 之實質內容不在文字層內，而類似情形未被普查

§1.6.2.1 之文字層僅有兩個 `WrapperResource` inline RTF 參照。
換言之 CFTS 本文中有**嵌入物件承載規格內容**，而 R-P17 之文字層定義
（plain / bold 兩種序列化）完全看不到它們。
**全文有多少個這類 `WrapperResource` / 嵌入物件，從未清點。**
若數量可觀，則「G8 = 904 個需求錨點」所代表的規格覆蓋率被高估。

### 4. 車型適用性過濾已驗為無虞，但 `EE Architecture` 軸未驗

本包因 §1.6.2.1.4 順帶量測：1052 個錨點中，`Radio` 欄不含 `R1L` 且非 `allSys` 者
有 **309** 個；但**被 037 引用之 238 個 item 全部為 `allSys`(151) 或含 `R1L`(87)，
零例外** —— SYS2 匯出已完成車型過濾，此軸無虞。

**惟 `EE Architecture` 軸（Atlantis High / Mid）未做同等檢查。**
01 包 §K 第 2 項曾提及 140 個 Atlantis 錨點，但那是在未被引用的池子裡，
且已由 R-P7 免除。**被引用的 238 個 item 之 EE Architecture 分布從未量測**，
而 FW036 workbook 有 `HDCC27 Atl-Hi` / `DT27 Atl-Hi` / 五個 `Atl-Mi` 車型欄
（03 包 G12 實測 c21–c27），Phase 4 要填這些欄。

### 5. B1 / B2 / B3 三份輸出無腳本，破壞了本 feature 一路建立的可重現性

`layer3_full.tsv` 有 `build_layer3.py`、文字層有 `extract_textlayer.py`、
閘門有 `verify_gates_03.py`、03 包 B1 有 `build_b1.py`。
但本包之 `b1_swepm008.md`、`b2_uncovered_chapters.md`、`b3_sys3_crosscheck.md`
係以一次性指令產生，**未留腳本**。
R-P13 之精神（可重現）適用於素材，這三份是裁定素材卻不可重現。
B2 因含人工判讀，本就無法全自動；但其**事實部分**（章節全文、引用錨點、
leaf Description）應可腳本化，只留判讀欄為人工。

### 6. 037 全欄零空值已驗，但欄位之「資訊量」未驗

G19 證明 18 欄皆非空。但非空不等於有資訊 ——
例如 `Description/Action for Feasibility` 是否 115 筆同值？
`Release Version` 是否全為 `1.0.0`？
若某欄為單一值，它在分批、優先級、追溯上就沒有鑑別力，
與空欄的實際效果相同。本包只數了非空，**未量測各欄之相異值數**。
（已知 `Categorization` 為單一值 —— 那正是 G2 的內容，且被當作 PASS。）

---

## 十、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | 僅 `read_only=True` 開啟 |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補；`layer3_full.tsv` 中該 leaf 無列 |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生；並查出 R-P7 條文內嵌之 547 為失效值（A-PW19） |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改。SYS3 之連結改用 `Sys-RA-PM-` token（037 同軸），非修改 §C 正則 |
| **不得為 `SWE-PM-008` 之 Test Set 歸屬附建議** | `b1_swepm008.md` 全檔無建議。§四僅列兩種情形之分布數字 |
| **不得為 A-PW16 之 9 章建議處置** | `b2_uncovered_chapters.md` 全檔無處置建議。判定欄僅「涵蓋／部分涵蓋／未涵蓋／無法判定」＋逐字依據 |
| 不得據 SYS3 交叉比對結果調整 §E | §E 未因 B3 有任何變動。B3 結論僅登記為 A-PW20 |
| 不得重算或改寫 §E 之 leaf 分布數字 | **64/24/16/7/3 一字未動。** 本包未執行 `verify_gates.py`（02 包版，含 §E 重算段）；所用之 `verify_gates_03.py` 無該段 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

### §E 之異動（依 04 §E 指示）

`docs/handoff/01_intake.md` §E：Power State 之 Layer 3 章節清單中
`~~§1.8.1~~` → **`§1.8.1.1.1`**（R-P25）；標題維持「待定版」；
註記更新為 04 包異動（R-P24 全集、R-P25 撤回、R-P26 待裁範圍）。
**leaf 分布數字未動。**

---

## 十一、待裁

- **Q1（阻斷 §E 定版）`SWE-PM-008` 與 `SWE-PM-057` 之 Test Set 歸屬**（R-P26(b)）。
  素材：`data/b1_swepm008.md`、03 上繳包 §七。四種組合之分布見 04 下放包 §E。
- **Q2 A-PW16 之 9 章處置**（R-P27）。素材：`data/b2_uncovered_chapters.md`。
  併請裁定 §1.6.2.1.4 之描述訂正（其在範圍內之唯一需求為否定需求，非防盜功能）。
- **Q3 §1.6.2.1「無法判定」如何處置** —— 其內容在 inline RTF 內，
  現行文字層看不見。是否解 RTF、或宣告不涵蓋。
- **Q4 R-P28 之章節層缺口與 R-P7 重疊（§六），是否續行。**
  若續行，續行的判準為何（現行只有「未被觸及」，那是錨點鏈的副作用）。
- **Q5 R-P7 條文內嵌之「547 條」（實測 669）是否訂正**（A-PW19）。
- **Q6 §九第 1 項：B2 之判讀單位是否改為「被引用之錨點 vs leaf」並重做九章。**
- **Q7 §九第 3 項：是否清點 CFTS 本文之嵌入物件（`WrapperResource`）數量。**
- **Q8 §九第 4 項：是否量測被引用 238 個 item 之 `EE Architecture` 分布**
  （FW036 有七個車型欄待填）。
