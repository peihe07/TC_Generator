# DATA REQUESTS — Power (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/power/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

來源：下放包 01 §G、02 §G、06 §G。撤回列不刪、不重編號，保留作為裁決跡證。

| DR | Urgency | 內容 | 阻斷何物 | Anomaly |
|---|---|---|---|---|
| DR-PW1 | **High（live）** | `SWE-PM-089` 之真實上游來源為何？（`SWE1-PM-ANT-008` 非 SYS2 id） | 該 leaf 之 TC 及其 `specification_reference` | A-PW01 |
| DR-PW2 | **撤回** | SYS2 匯出之**收錄規則**為何？—— 包含（a）CFTS009 `Sys-RA-PM-0197`–`0206` 連續十條缺失；（b）CFTS009 本文 904 條需求中未被引用之 547 條內，有 **140 個需求錨點**標 `EE Architecture: Atlantis High/Mid`（`Atlantis High, Atlantis Mid` 73 + `Atlantis Mid, Atlantis High` 67，二者為同一集合之不同排序寫法），似不應被濾掉。**（R-P7 撤回：範圍 = 037 之 115 leaf）** | 已解除 | — |
| DR-PW3 | **Medium（live）** | `Sys-RA-PM-0334` 引用之 `4942087` 屬何文件？ **交叉指引（R-P151，23 包）**：本 DR 與 **A-PW02**、**G103 / G114**（layer3 靜默丟棄）、**DR-PW11**（四個文字層不存在之 item）為同一形態之四處記載。 | A-PW02 | A-PW02、A-PW120 |
| DR-PW4 | **撤回** | 037 `Priority` 之 `High`/`Medium` 如何映射至 FW036 `P0`–`P3`？**（R-P8 撤回：priority 依 TC 測項判定）** | 已解除 | — |
| DR-PW5 | **High（live）** | **CFTS009 §1.6.2.1.4 Stolen Vehicle Mode —— 範圍內而未被涵蓋。** `SWE-PM-003`（Partial Operation）經 `Sys-RA-PM-0031` 引用該章之 `4941400`，其全文為「the R1 HU shall not enter stolen vehicle mode under any condition」（`Radio` 欄含本專案車型 `R1L`，`Model Year` 2021–2025）。而 `SWE-PM-003` 之 Requirement Description 全文為 Partial Operation 之電源政策（Display / audio / BT / Tuner / USB / AUX），**無一字涉及 stolen vehicle mode**。請上游澄清：此否定需求應由哪一個 SWE leaf 承接？或確認其不需 TC。 | `SWE-PM-003` 之 TC 是否須涵蓋該否定需求 | A-PW16、R-P43(c) |
| DR-PW6 | **Medium（live）** | **31 處懸空 `WrapperResource` 參照 —— 請補提供缺漏之**嵌入資源（RTF / 試算表 / Word 文件）**或其等效內容。** CFTS009 16 處、CFTS010 15 處，分布 **16 個章節**。二份文件經實測**皆無任何嵌入物件**（CFTS009 無 `word/embeddings/`、`w:object`/`w:drawing`/`w:pict`/`o:OLEObject` 各 0；CFTS010 之 OLE2 目錄無 `ObjectPool`、無 `\x01Ole`），故該等 `… WrapperResource` 為**純字面之懸空參照**，所指資源未隨文件匯出。**型別實測（07 包 G34）**：`.rtf` 14、`.xls` 15、`.xlsx` 1、`.doc` 1 —— 試算表為多數（原稱「RTF 資源」為誤，見 A-PW32）。**影響面（依 R-P45 先完成 leaf 層交叉）**：31 處中**僅 2 處**落在被引用之錨點下 —— 皆位於 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**（錨點 `4941354` / `4941355`），**觸及 9 個 leaf**（`SWE-PM-001`–`009`），全屬 **Power State**。其餘 29 處落在未被引用之錨點下，依 **R-P42** 不在測試範圍內。 | §1.6.2.1 之 9 個 leaf 其 TC 之 `specification_reference` 無可引之規格文字（B2 v2 判為「無法判定」） | A-PW23、A-PW26、R-P44、R-P45 |
| DR-PW7 | **Low（live）** | **`Verification Criteria` 欄品質。** G28 基線實測：VC 單欄不可執行 **2 / 115**、VM 單欄不可執行 **0 / 115**、**二欄合觀不可執行 0 / 115**。兩筆為 `SWE-PM-007`（「Vehicle not equiped with CAN or engineering line is active」）與 `SWE-PM-008`（「Vehicle equiped with CAN」），皆僅為泛稱環境陳述而無可操作條件。二者之 VM 欄均為可執行，故**不阻斷任何 leaf 之 TC 撰寫**。 | 不阻斷。僅影響該二 leaf 之 Pre-Conditions 欄品質 | A-PW28、R-P49 |
| DR-PW8 | **High（live）** | **`4942354` 之 `voltage out of range conditions` 未載電壓門檻值。** 該錨點載「Unless defined otherwise, TLM shall stay in this state until either **voltage out of range conditions are satisfied** or shall go back to normal behavior 10 seconds after `STATUS_LIN.Batt_ST_Crit` becomes [0h]」——**僅載條件之名稱，未載電壓值或其判準**。依 §8.4.1 不得造容差／門檻值，依 R-P42 不得赴其他未被引用之錨點取值。請上游提供該條件之定義（電壓上下界、持續時間、或其所引之文件與章節）。 | `NR1L-PowerManagement-015`（Battery Critical 之第一回復分支）**可撰寫而不可執行** —— 該條已於 `remarks` 標明此狀態，使其於工作簿內可見 | A-PW83、R-P121 |
| DR-PW10 | **Medium（live）** | **`SWE-PM-038` 三對成對錨點之 `Model Year: 2017` / `State: Under Review` 是否適用本案。** `4941728` / `4941730` / `4941736`（含 `RemStartFail` 處置之一側）**全部帶 `Model Year: 2017` 且 `State: Under Review`**，而其對造（`4941727` / `4941729` / `4941735`）或無 `Model Year`、或 `State: New`。二項疑點：（a）`Model Year: 2017` 出現於 25PI3.5 專案，需解釋；（b）`State: Under Review` 非最終狀態，而 SYS2 匯出**無 `State` 欄**（20 §2.1 已證），**故本專案之範圍判定從未看過此欄**。 | 不阻斷撰寫。`037` / `039` / `042` 三條之最終內容（是否保留）待此澄清；三條之 `remarks` 已標記 | A-PW112、R-P153 |
| DR-PW11 | **High（live）** | **`SWE-PM-010` 之被引用錨點 `4941984` 不存在於 CFTS 本文。** 037 之 `Source Requirement ID` 經 SYS2 解析得 8 個 item id，其中 `4941984` **於 CFTS009 / CFTS010 之文字層皆無內文段落、亦無所屬章節**（鄰近之 `4941983` / `4941985` 皆存在）。`layer3_full.tsv` 因其無法解析至章節而**靜默丟棄**該 item，致 `source_anchor` 僅 7 個。請上游確認：該 item 是否應存在於 CFTS009？或 SYS2 之對應有誤？ **（23 包 G114 全量掃描擴大）**：115 leaf 中不相等者共 **2** —— `SWE-PM-010` 缺 `4941984`、**`SWE-PM-008` 缺 `4941425` / `4941430` / `4941433`**；**四個 item 於兩份 CFTS 文字層皆無內文段落**。與 A-PW02 / DR-PW3（`4942087`）同型。 | **`SWE-PM-010` 與 `SWE-PM-008` 之 TC 全部**（其 `source_clause` 無法完整，反向涵蓋於原理上不成立）——二 leaf 皆已自第三批排除 | A-PW113、R-P144、**A-PW120** |
| DR-PW9 | **High（live）** | **SYS2 CFTS009 匯出之 `HARMAN Status` 含 4 列 `Need rework`，而其檔名為 `All_Accepted` —— 檔名與內容不符。** 四列為 `Sys-RA-PM-0021` / `0291` / `0292` / `0293`。（a）該匯出之收錄條件究竟為何？`All_Accepted` 所指者為哪一欄？（b）037 引用其中之 `Sys-RA-PM-0293`（其 `HARMAN Status` 逐字為 `Need rework`、`MD Status` 為空），對應 `SWE-PM-112` —— 該 leaf 是否仍在範圍內？ | `SWE-PM-112` 之範圍歸屬。**不阻斷已產出之 33 leaf**（該四 token 皆不在其中）| A-PW110、R-P148 |

**本表現存 live 項：DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、**DR-PW9（High）**、**DR-PW11（High）**、DR-PW3（Medium）、DR-PW6（Medium）、**DR-PW10（Medium）**、DR-PW7（Low）。**
22 包新增 **DR-PW10**（R-P153）與 **DR-PW11**（R-P144 之首次真實命中）。
**`DR-PW9` 已於 23 包補執行 21 包時開立**（R-P164）。
17 包新增 **DR-PW8**（R-P121）—— 首張因「TC 可撰寫而不可執行」而開之 DR。
06 包新增 DR-PW5 / DR-PW6 / DR-PW7（R-P43(c)、R-P44、R-P45、R-P49）。

> 註（02 包）：DR-PW3 之證據描述已於 ANOMALIES A-PW02 訂正 ——
> `Sys-RA-PM-0334` 之 `4942087` **可被 `\d{6,8}` 正常解析**，
> 其缺口在於該 item id 無法解析至任一 CFTS 章節，非 token 缺失。
> DR 本身之問題（`4942087` 屬何文件）不變，仍為 live。
>
> **（06 包更新）§E 已由 R-P35 定版，framework 不再有阻斷項。**
> DR-PW1 阻斷 `SWE-PM-089` 一個 leaf；DR-PW6 影響 `SWE-PM-001`–`009` 九個 leaf 之
> `specification_reference`；DR-PW5 影響 `SWE-PM-003` 一個 leaf 之涵蓋判定；
> DR-PW3、DR-PW7 不阻斷任何 leaf。
