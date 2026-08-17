# ANOMALIES — FW036 Power HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PWnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

來源：下放包 01 §F（A-PW01–A-PW07）、下放包 02 §F（A-PW07 撤回、A-PW08 新增）。
撤回列不刪、不重編號。

---

| ID | 內容 | 證據 | 狀態 |
|---|---|---|---|
| A-PW01 | `SWE-PM-089` 之 `Source Requirement ID` = `SWE1-PM-ANT-008`，為 037 自身另一套命名空間，非上游來源 | 全表 18 欄 × r8–r145 掃描，該 token 不存於任一 SYS2 匯出 | PENDING（DR-PW1；02 包 G3 實測復現：114/115，唯一失敗者即此 leaf） |
| A-PW02 | `Sys-RA-PM-0334` 之 source id `4942087` 於兩份 CFTS 本文皆不存在；`4942xxx` 為 CFTS010 號段但低於其首個 id `4942192` | 01 包記為 G6 失敗項 | PENDING（DR-PW3）。**02 包訂正證據來源**：`Sys-RA-PM-0334` 位於 SYS2 CFTS009 匯出 r325，其 `Source Requirement items` = `4942087`，**可被 `\d{6,8}` 正常解析**，故非 G6 之失敗項。其異常在於該 item id 無法解析至任一 CFTS 章節，屬解析鏈第三段之缺口，非第一段之 token 缺失。 |
| A-PW03 | 037 `Excluded NRLs (HW-only)` 26 筆全落 NRL-928xx–930xx（CFTS009 域），**不含** `NRL-99476`（`Sys-RA-PD_013`，HW） | 排除台帳涵蓋範圍不等於其名稱所宣稱 | PENDING |
| A-PW04 | 037 `SYS2 Traceability` 33 列不含任何 `NRL-994xx` 或 `Sys-RA-PD` | CFTS010 全域未進追溯分頁 | PENDING |
| A-PW05 | 037 內部 id 命名空間不一致：`SWE1 Requirements` 用 `SWE-PM-001..115`，`SYS2 Traceability` 用 `SWE1-PM-TLM-001..033` / `-ANT-` | 兩套互不對應 | PENDING |
| A-PW06 | 037 `Sub Categorization` 詞彙漂移：`HMI` 36 / `Service\nHMI` 35 / `Service` 27 / `HMI Service` 16 / `HMI/Service` 1 | 三種寫法指涉同一組合，不可作分批判準 | PENDING |
| A-PW07 | ~~三份 `.docx` 實為 Markdown 純文字，副檔名與內容不符~~ | ~~magic bytes 實測（R-P3）~~ | **撤回（R-P12）**。原始檔實測：CFTS009 `.docx` = `50 4B 03 04`（OOXML）、CFTS010 `.doc` = `D0 CF 11 E0`（OLE2）、SYS3 `.docx` = `50 4B 03 04`（OOXML）。副檔名與內容**實為相符**。不刪列、不重編號。 |
| A-PW08 | 01 下放包 §B 之「真實格式」欄與 `bytes` 欄與原始檔不符，源於以衍生物冒充原始檔。另記：CFTS010 之原始檔副檔名為 `.doc`，非 `.docx`；01 包中「三份 .docx」之表述在檔名層即為錯誤 | 01 包記 412,654 / 81,064 / 51,264 bytes「純文字」；原始檔實測 154,588（OOXML）／245,248（OLE2）／3,474,091（OOXML）。三個宣稱之 SHA256 於整個 `/Users/peihe` 家目錄內無任何符合檔案 | **新增（R-P12）**。導致 01 包停於步驟 2；已由 R-P9–R-P13 處置 |
| A-PW09 | 01 包 §C 之 SYS2 CFTS009 讀取座標 `r2–r338` 漏一列：實際資料延伸至 **r339**（`NRL-142587`，其 `Source Requirement items` 為空） | 02 包 G12 實測。r340 起為空 | **新增（執行層 Tier 1 登記）**。若採 r2–r339，G6 變為 337/338（失敗者 `NRL-142587`）；若採 §C 之 r2–r338，則為 337/337。舊期望值 336/337 兩者皆不符 |
| A-PW10 | §E Layer 3 章節清單未涵蓋 CFTS009 **§1.6.2.1.17**，該章節有 1 個 leaf（`SWE-PM-057`）；另 §E 於 Power State 列出之 **§1.8.1** 實測 0 leaf | 02 包 §E 重算。`§1.6.2.1.x` 分布：.1×1 .2×3 .3×2 .5×1 .6×2 .7×2 .8×1 .13×2 .15×35 .16×7 **.17×1** | **新增（執行層 Tier 1 登記）**。與 §E leaf 分布不符（62/24/16/8/3 + 未歸類 1）互為因果之一 |
| A-PW11 | CFTS009 與 CFTS010 之標題段落以不同機制表達粗體：CFTS009 用段落樣式 `pStyle 1–8`（run 層無粗體），CFTS010 之標題為 run 層粗體。故單一「全部粗體加 `**`」之序列化無法同時滿足 §C rule 1 與 rule 2 | 全部粗體序列化下：CFTS009 得 172/904、CFTS010 得 0/148；未標記序列化下：CFTS009 得 196/0、CFTS010 得 92/0 | **新增（執行層 Tier 1 登記）**。執行層採「rule 1 套未標記文字、rule 2 套粗體標記文字、依段序對齊」之統一定義，待分析層追認。此即 01 包舊值 G8 章節錨點 172 之成因 |

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PWnn]`.
