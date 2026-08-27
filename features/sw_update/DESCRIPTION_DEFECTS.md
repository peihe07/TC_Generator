# DESCRIPTION_DEFECTS — 037 描述缺陷台帳（SW Update）

上游 037 之 `Requirement Description` 本身之缺陷（缺字、殘句、佔位未填）。
**不改 037、不臆補**（IN §8.4.1）：撰寫該列 TC 時 `test_item` 上半仍
verbatim 抄其原文（含缺字），錨由其他路徑定，並於 `reasoning` 記明。

登記為 Tier 1（記錄 + 提案）；何者構成缺陷之判定屬 Tier 2。

| # | 037 列 | 形態 | 狀態 |
|---|---|---|---|
| D-1 | `SWE1-FOTA-319` | 缺字 —— 條件名脫落 | **已確認**（下放包 11 §3.2） |
| D-2 | `SWE1-FOTA-248` | 缺字 —— 受詞脫落 | 待判定 |

---

## D-1 —— `SWE1-FOTA-319`：條件名脫落 —— 已確認

出處：下放包 11 §3.2（分析層裁定）。

原句（逐字）：

> The WiFiUpdateService shall coordinate the handling of **condition** during
> OTA server communication, flashing, or software component update by
> interacting with SWMC and the appropriate installer component.

`the handling of condition` —— **條件之名稱脫落**。
其 `Requirement Title` 為 `Power Loss Handling`，其兄弟區塊對位物件為
CFTS `4907671`（4.12 之第 5 項）`5. Loss of power(battery disconnect)`。

**037 之描述漏了「power loss」，文本路遂無詞可共** —— 其正解
`4907671` 為累計 27 列地面真值中**唯一不在前 20 候選內**者（T24b 實測）。

**處置**：不改 037、不臆補。錨由 R-SU16 兄弟區塊定（三證：`313` 之自證
邊界、`315`–`318` 四列之文本路對位、位序齊一）。
撰 TC 時 verbatim 抄原文含缺字，`reasoning` 記明本項。

**此為上游文件之缺陷，非本管線之缺陷。**

---

## D-2 —— `SWE1-FOTA-248`：受詞脫落 —— 待判定

T24d 語形掃描所得（形態「冠詞後直接接介詞」）。原句片段（逐字）：

> …forwarded from the OTA server through the TC communication channel,
> then notify **the to** start server initiated session.

`notify the to start` —— `the` 之後受詞脫落。與 D-1 同族（缺字），
惟未經分析層裁定，**列為待判定**。

**執行層不裁定何者構成缺陷**（下放包 11 §五 T24d）。

---

## 掃描之能力界線（R-G8）

T24d 之六式語形掃描**漏掉了種子案例本身**：D-1 之 `of condition during`
因其後接 `during`（有後續詞）而不合式1 之 `(?!\s*\w)` 句尾條件。
以**寬鬆式**（去句尾條件）反向探測，全母體僅命中 1 列 —— 即 D-1 本身。

即：**缺字型缺陷之語形極不穩定**，其可偵測性取決於缺字後恰好接什麼。
本台帳所載為**下界**，非全集。詳見 `docs/upstream/10_block_anchor.md` §5.2。
