# DESCRIPTION_DEFECTS — 037 描述缺陷台帳（SW Update）

上游 037 之 `Requirement Description` 本身之缺陷（缺字、殘句、佔位未填）。
**不改 037、不臆補**（IN §8.4.1）：撰寫該列 TC 時 `test_item` 上半仍
verbatim 抄其原文（含缺字），錨由其他路徑定，並於 `reasoning` 記明。

登記為 Tier 1（記錄 + 提案）；何者構成缺陷之判定屬 Tier 2。

| # | 037 列 | 形態 | 狀態 |
|---|---|---|---|
| D-1 | `SWE1-FOTA-319` | 缺字 —— 條件名脫落 | **已確認**（下放包 11 §3.2） |
| D-2 | `SWE1-FOTA-248` | 缺字 —— 受詞脫落 | **已確認**（下放包 12 §4.3） |
| D-3 | `SWE1-FOTA-128` | **贅餘殘留** —— `control from below` | 待判定 |
| D-4 | `SWE1-FOTA-180` | **拼寫殘留** —— `shalll` | **已確認**（下放包 26 §五 TC-6） |

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

## D-2 —— `SWE1-FOTA-248`：受詞脫落 —— **已確認**

T24d 語形掃描所得（形態「冠詞後直接接介詞」）。原句片段（逐字）：

> …forwarded from the OTA server through the TC communication channel,
> then notify **the to** start server initiated session.

`notify the to start` —— `the` 之後受詞脫落。與 D-1 同族（缺字）。

**裁定（下放包 12 §4.3）**：冠詞後直接接不定式，受詞脫落，形態明確，
**確認為缺陷**。處置同 D-1：不改 037、不臆補，TC 之 `test_item` 上半
仍 verbatim 抄原文。

---

## D-3 —— `SWE1-FOTA-128`：贅餘殘留 —— 待判定

出處：下放包 12 §4.1（`128` 之統攝型判定過程中另見）。

原句片段（逐字）：

> The SWMC shall use the extracted parameters and metadata from below
> mentioned parameters **to control from below and** execute the OTA update workflow.

`control from below` 為殘句，疑為 `to control the flow` 之類原句經編輯殘留。

**與 D-1／D-2 不同型**：後二者為**缺字**（成分脫落），本項為**贅餘殘留**
（多餘成分未刪淨）。二型之語形特徵相反 —— 缺字型可由「介詞後無名詞」
類形態偵測，贅餘型則語法完整而語意不通，**語形掃描對其無能為力**。

**同列另經裁定非統攝型**（下放包 12 §4.1）：`below mentioned parameters`
所指之十個參數逐一列於該列自身 Description 之內，非指涉他處定義之需求。

---

## D-4 —— `SWE1-FOTA-180`：拼寫殘留 —— **已確認**

出處：下放包 26 §五 TC-6（batch 1 起草時遇）。

原句（逐字，`upstream/24_batch1_relist.md` §2 之 Description 全文首句）：

> When the update type is identified as Silent Update, the WiFi Update Service
> **shalll** not trigger the SW Update HMI to display a download confirmation screen.

`shalll` —— `shall` 之三個 `l`。

**第三型，與 D-1／D-2（缺字）、D-3（贅餘殘留）皆不同**：
本項為**拼寫殘留**，其成分不缺不贅，**語意完全無損** ——
讀者一眼看懂它是 `shall`。

**處置（IN §8.4.1）**：`test_item` 上半 **verbatim 保留 `shalll`**。
R-4 僅允許句首大寫之正規化，拼寫不在其列。
`newR1L-SU-006` 之 `test_item` 已照原文寫入，**未改正**。

> ⚠ **本型之偵測性與前三型相反**：缺字型語形不穩（見下節）、贅餘型語法完整而語意不通，
> **拼寫型則是唯一一個拼字檢查抓得到的** —— 然而
> **037 之交付流程顯然沒有跑過拼字檢查**，否則它不會留到這裡。
> 即：本項之存在，其資訊量不在本列，**在於它揭示上游無此道關卡** ——
> 故同型缺陷應假設**尚有未發現者**，本台帳所載仍為下界。

---

## 掃描之能力界線（R-G8）

T24d 之六式語形掃描**漏掉了種子案例本身**：D-1 之 `of condition during`
因其後接 `during`（有後續詞）而不合式1 之 `(?!\s*\w)` 句尾條件。
以**寬鬆式**（去句尾條件）反向探測，全母體僅命中 1 列 —— 即 D-1 本身。

即：**缺字型缺陷之語形極不穩定**，其可偵測性取決於缺字後恰好接什麼。
本台帳所載為**下界**，非全集。詳見 `docs/upstream/10_block_anchor.md` §5.2。
