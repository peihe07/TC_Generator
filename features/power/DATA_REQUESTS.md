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
| DR-PW3 | **Medium（live）** | `Sys-RA-PM-0334` 引用之 `4942087` 屬何文件？ | A-PW02 | A-PW02 |
| DR-PW4 | **撤回** | 037 `Priority` 之 `High`/`Medium` 如何映射至 FW036 `P0`–`P3`？**（R-P8 撤回：priority 依 TC 測項判定）** | 已解除 | — |
| DR-PW5 | **High（live）** | **CFTS009 §1.6.2.1.4 Stolen Vehicle Mode —— 範圍內而未被涵蓋。** `SWE-PM-003`（Partial Operation）經 `Sys-RA-PM-0031` 引用該章之 `4941400`，其全文為「the R1 HU shall not enter stolen vehicle mode under any condition」（`Radio` 欄含本專案車型 `R1L`，`Model Year` 2021–2025）。而 `SWE-PM-003` 之 Requirement Description 全文為 Partial Operation 之電源政策（Display / audio / BT / Tuner / USB / AUX），**無一字涉及 stolen vehicle mode**。請上游澄清：此否定需求應由哪一個 SWE leaf 承接？或確認其不需 TC。 | `SWE-PM-003` 之 TC 是否須涵蓋該否定需求 | A-PW16、R-P43(c) |
| DR-PW6 | **Medium（live）** | **31 處懸空 `WrapperResource` 參照 —— 請補提供缺漏之 RTF 資源或其等效內容。** CFTS009 16 處、CFTS010 15 處，分布 **16 個章節**。二份文件經實測**皆無任何嵌入物件**（CFTS009 無 `word/embeddings/`、`w:object`/`w:drawing`/`w:pict`/`o:OLEObject` 各 0；CFTS010 之 OLE2 目錄無 `ObjectPool`、無 `\x01Ole`），故該等 `…inline.rtf WrapperResource` 為**純字面之懸空參照**，所指資源未隨文件匯出。**影響面（依 R-P45 先完成 leaf 層交叉）**：31 處中**僅 2 處**落在被引用之錨點下 —— 皆位於 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**（錨點 `4941354` / `4941355`），**觸及 9 個 leaf**（`SWE-PM-001`–`009`），全屬 **Power State**。其餘 29 處落在未被引用之錨點下，依 **R-P42** 不在測試範圍內。 | §1.6.2.1 之 9 個 leaf 其 TC 之 `specification_reference` 無可引之規格文字（B2 v2 判為「無法判定」） | A-PW23、A-PW26、R-P44、R-P45 |
| DR-PW7 | **Low（live）** | **`Verification Criteria` 欄品質。** G28 基線實測：VC 單欄不可執行 **2 / 115**、VM 單欄不可執行 **0 / 115**、**二欄合觀不可執行 0 / 115**。兩筆為 `SWE-PM-007`（「Vehicle not equiped with CAN or engineering line is active」）與 `SWE-PM-008`（「Vehicle equiped with CAN」），皆僅為泛稱環境陳述而無可操作條件。二者之 VM 欄均為可執行，故**不阻斷任何 leaf 之 TC 撰寫**。 | 不阻斷。僅影響該二 leaf 之 Pre-Conditions 欄品質 | A-PW28、R-P49 |

**本表現存 live 項：DR-PW1（High）、DR-PW3（Medium）、DR-PW5（High）、DR-PW6（Medium）、DR-PW7（Low）。**
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
