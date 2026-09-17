# DATA REQUESTS — Diagnostics (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/diagnostics/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | **NRC 值之權威來源** —— R-DIAG5(amend) 落地後之**殘餘 3 列**：`SWE1-Diagnostics-156`／`-157`（row 163/164，`$0312` AV Signal Detection，Description 為標題複製、未述失效型態）／`SWE1-Diagnostics-237`（row 244，`$2847`，只書「an appropriate NRC」，其 CFTS004 來源 `SYS-RA-DIAG-056` 亦只書「shall provide a negative response」）| MISSING | **3**（原 205） | **非阻斷** —— 226 列中 223 列已由 R-DIAG5(amend)(c′)(d) 解出；3 列於 pilot 寫 `PENDING: DR-DIAG-1` | A-DIAG01 | MED（原 HIGH）|
| 2 | `SYS3_CFTS_004…SYSAD.docx` 之 UDS 序列補件 —— 現本無 UDS 請求／回應位元組表、無 NRC 表，唯一序列表為 DTC 流程（037 之 DTC 列 = 0）| PARTIAL | 全 388 產出列之 `test_procedure` | 位元組步驟改自 037／CFTS004 逐列推出，成本升高；不阻斷 | DR-DIAG-2 | MED |
| 3 | CFTS004 未收之 **52** 條 FR（清單見 `data/cfts004_uncited_fr.tsv`；含 V1 (3) 刪列後回歸之 `SYS-RA-DIAG-167`／`-168`）—— 供 RD 回饋，非本 feature 產出對象（R-DIAG8(a)／R-DIAG8(amend)）| N/A（不需取得）| 0 | 無 | FB-DIAG-d | LOW |
