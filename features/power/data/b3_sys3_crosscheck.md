# B3 — SYS3 SYSAD §4.x 與 §E 之交叉比對（R-P32）

> 依 04 §I：**不得據本檔調整 §E**。比對結果為 05 包之裁定素材。

來源：`SYS3_CFTS_009_…_SYSAD_v1.1.0.docx`（3,474,091 B，`cb6bf7d81030abc8…`，G0 相符）
文字層：`data/textlayer/sys3_plain.txt`（46,850 B，`1470be41bc65df68…`）

## 1. 連結方式

03 包測得 G16 = 0（無字面章節號、無 `{polarion_id}` 後綴），
故無法經 §C 之錨點鏈連結。**但本包實測 SYS3 文字層含 `Sys-RA-PM-` token 630 個出現、
272 個相異值** —— 與 037 `Source Requirement ID` 同一命名軸，故可連結。

連結規則：token 歸屬於其位置之前最近之 `Heading1` / `Heading2`（與 §C rule 2 同構）。
章節號為依 Heading 階層推導值，非文件內文字。

實測：`Sys-RA-PD` **0 個**、`NRL-` **0 個**、6–8 位數字 **0 個**、`SWE-PM-` **0 個**。

## 2. §4.x 之 36 項元件分解（含 token 數）

| 推導章節號 | pStyle | 標題 | Sys-RA token 數 |
|---|---|---|---|
| §4 | Heading1 | 系統架構設計 System Architecture Design | 0 |
| §4.1 | Heading2 | 系統架構概述System Architecture Overview | 0 |
| §4.2 | Heading2 | 設計替代 Design Alternate | 0 |
| §4.3 | Heading2 | 系統需求 – 概述 System Requirements – Overview | **214** |
| §4.4 | Heading2 | Power States | 0 |
| §4.5 | Heading2 | Paramters | 0 |
| §4.6 | Heading2 | Special Mode Parameters | 0 |
| §4.7 | Heading2 | Timers | 0 |
| §4.8 | Heading2 | Feature Specific | 0 |
| §4.9 | Heading2 | 系統分解 System Decomposition | 0 |
| §4.10 | Heading2 | 假設與相依性Assumptions and Dependencies | 0 |
| §4.11 | Heading2 | Assumptions | **40** |
| §4.12 | Heading2 | 順序圖 Sequence Diagram | 0 |
| §4.13 | Heading2 | Start-Up sequence | 0 |
| §4.14 | Heading2 | Shutdown Sequence | 0 |
| §4.15 | Heading2 | Custom power state | 0 |
| §4.16 | Heading2 | Power State Transition | **21** |
| §4.17 | Heading2 | Power Mode Interruption Sequence | 0 |
| §4.18 | Heading2 | Phone Call | **2** |
| §4.19 | Heading2 | Disclaimer | 0 |
| §4.20 | Heading2 | Start-up Animation | **2** |
| §4.21 | Heading2 | Splash — Cold Boot | **3** |
| §4.22 | Heading2 | Splash — Warm Boot | **3** |
| §4.23 | Heading2 | Splash — Idle to Full Operation | **3** |
| §4.24 | Heading2 | Antitheft | **19** |
| §4.25 | Heading2 | Front Panel On Off Sequence | **12** |
| §4.26 | Heading2 | 系統架構設計System Architecture Design | 0 |
| §4.27 | Heading2 | 架構設計組件Architectural Design Components | 0 |
| §4.28 | Heading2 | 分配系統需求Allocate System Requirements | **230** |
| §4.29 | Heading2 | 動態行為 Dynamic Behavior | 0 |
| §4.30 | Heading2 | Sleep | 0 |
| §4.31 | Heading2 | Standby | 0 |
| §4.32 | Heading2 | Full Operation | 0 |
| §4.33 | Heading2 | Idle | 0 |
| §4.34 | Heading2 | Timed | 0 |
| §4.35 | Heading2 | Partial Operation | 0 |
| §4.36 | Heading2 | Bench | 0 |

**549 個 token 出現中，444（81%）集中於兩節** —— §4.28 分配系統需求（230）
與 §4.3 系統需求–概述（214）。此二節為分配矩陣，非分組。

## 3. 「動態行為 Dynamic Behavior」七個狀態子節 vs CFTS009 §1.6.2.1.1–.13

| SYS3 節 | 標題 | token 數 | CFTS009 對應 |
|---|---|---|---|
| §4.30 | Sleep | **0** | §1.6.2.1.7 Sleep |
| §4.31 | Standby | **0** | §1.6.2.1.6 Standby |
| §4.32 | Full Operation | **0** | §1.6.2.1.1 Full-Operation |
| §4.33 | Idle | **0** | §1.6.2.1.2 Idle |
| §4.34 | Timed | **0** | §1.6.2.1.5 Timed |
| §4.35 | Partial Operation | **0** | §1.6.2.1.3 Partial Operation |
| §4.36 | Bench | **0** | §1.6.2.1.8 Bench |

**七項名稱全部對得上，且七項之 Sys-RA token 數全為 0。**

**SYS3 有而 CFTS 無**：無。

**CFTS 有而 SYS3 無**（6 項）：

- CFTS009 §1.6.2.1.4 — Stolen Vehicle Mode
- CFTS009 §1.6.2.1.9 — Logistic Idle
- CFTS009 §1.6.2.1.10 — Logistic Standby
- CFTS009 §1.6.2.1.11 — Logistic Sleep
- CFTS009 §1.6.2.1.12 — Init
- CFTS009 §1.6.2.1.13 — TLM initialization: Init state

> **並陳一項事實**：上列 6 項中，`Stolen Vehicle Mode`、`Logistic Idle`、
> `Logistic Standby`、`Logistic Sleep` 四項，正是 A-PW16 之 9 個未覆蓋章節中的四項
> （見 `data/b2_uncovered_chapters.md`）。即架構文件之狀態分解同樣未涵蓋它們。
> 此為觀察，非處置建議。

## 4. 以 SYS3 節為獨立分組軸，對 114 leaf 重新聚類

可經 SYS3 分節之 leaf：**111 / 115**（4 條無對應：`SWE-PM-071/072/073`
即 CFTS010 域之 Power Down 三條，加 `SWE-PM-089`）。

每 leaf 對應之 SYS3 節數分布：

| 對應節數 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| leaf 數 | 4 | 21 | 53 | 23 | 6 | 6 | 2 |

**僅 21 個 leaf 對到單一 SYS3 節**；53 個對到兩節，其餘更多。

## 5. 與 §E 現行五個 Test Set 之交叉表

（列 = §E Test Set，欄 = SYS3 節；一個 leaf 可計入多節，故橫向總和大於 leaf 數）

| §E Test Set | SYS3 節分布 |
|---|---|
| Power State | 分配系統需求 61、系統需求–概述 60、Assumptions 15、Power State Transition 12、**Antitheft 10**、Front Panel On Off Sequence 8、**Splash — Cold Boot 3**、**Splash — Warm Boot 3**、**Splash — Idle to Full Operation 2**、Phone Call 2 |
| Startup Display | 分配系統需求 24、系統需求–概述 22、Assumptions 2、Power State Transition 1、**Start-up Animation 1** |
| Branding and Theme | 分配系統需求 16、系統需求–概述 1 |
| Timeout Settings | 分配系統需求 8、系統需求–概述 5、Assumptions 3、Front Panel On Off Sequence 1、Power State Transition 1 |
| Power Down | **（SYS3 無對應）3** |

**一致者**：無任一 Test Set 與單一 SYS3 節形成一對一或近一對一之對應。

**分歧者**（去除兩個大宗表格節後之特徵節）：

- `Splash — Cold Boot` / `Warm Boot` / `Idle to Full Operation` 共 8 個 leaf 出現，
  **全部落在 §E 之 Power State**，而 §E 將 Splash Screen（CFTS009 §1.6.2.1.16）
  歸於 **Startup Display**。兩軸對 Splash 的歸屬相反。
- `Start-up Animation` 僅 1 個 leaf，落在 Startup Display。
- `Antitheft` 10 個 leaf 全部落在 Power State；§E 五個 Test Set 中無 Antitheft 對應項。
- `Branding and Theme`（16 leaf）除兩個大宗表格節外**無任何特徵節對應** ——
  SYS3 全篇無 Branding / Theme 相關標題。

**SYS3 無對應者**：CFTS010 域之 Power Down 三條（`SWE-PM-071/072/073`）。
SYS3 為 CFTS009 之架構文件，其文字層 `Sys-RA-PD` 出現 0 次。
另 `SWE-PM-089` 因其來源 id 非 SYS2 命名空間（A-PW01），亦無對應。

## 6. G20 結論 —— **SYS3 不構成 §4.1.2 所要求之「第二來源」**

四種失敗形態，逐項為實測：

1. **無 leaf 對應（致命）** —— R-P32 所指定之切入點「動態行為 Dynamic Behavior」
   其七個狀態子節（§4.30–§4.36）之 Sys-RA token 數**全為 0**；
   連同其父節 §4.29，整個動態行為分支零 traceability。
   名稱對得上，但**沒有任何 leaf 能被指派到它們**。
2. **分類軸不同** —— 549 個 token 出現中 444（81%）集中於 §4.28
   「分配系統需求」與 §4.3「系統需求–概述」。此二節是分配矩陣
   （把全部需求列一遍），不是元件分組；以之分群等同不分群。
3. **粒度不符** —— 111 個可對應之 leaf 中僅 21 個對到單一節，
   53 個對到兩節、23 個對到三節、最多 6 節。無法產生互斥分組。
4. **覆蓋面不足** —— CFTS010 全域（Power Down 三條）無對應；
   `Branding and Theme` 16 條除大宗表格外無特徵節對應。

**故 §E「本表實際只由 CFTS 章節單一來源支撐，不是交集」之弱點，
在完成本比對後結論為：確實無第二來源可用，該弱點成立且無法以 SYS3 消除。**

R-P20 所設之期待（「§4.x 為目前唯一可能提供獨立分組來源之文件」）
經實測不成立 —— 但這是一個**確定的結論**，非懸而未決：
SYS3 之元件分解未攜帶可連結至 leaf 的 traceability。
