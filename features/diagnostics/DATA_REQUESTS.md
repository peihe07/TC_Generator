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
| 1 | **NRC／SID 值之權威來源** —— CFTS004 未載之 205 列 NRC 與 114 列 I/O Control SID（`0x2F`）。可為 (i) Harman 之 UDS 實作規格／NRC 對照表，(ii) CFTS004 之後續版本，或 (iii) Pei 對 R-DIAG5(c) 之適用裁定（DECISIONS §2 甲／乙／丙）| MISSING | 230（negative 135 ＋ unsupported 95）＋ I/O 母節 114 | **阻斷 CDD-02 pilot 之 negative／unsupported 全部批次**；positive 型 165 列不受影響 | DR-DIAG-1 | **HIGH** |
| 2 | `SYS3_CFTS_004…SYSAD.docx` 之 UDS 序列補件 —— 現本無 UDS 請求／回應位元組表、無 NRC 表，唯一序列表為 DTC 流程（037 之 DTC 列 = 0）| PARTIAL | 全 394 產出列之 `test_procedure` | 位元組步驟改自 037／CFTS004 逐列推出，成本升高；不阻斷 | DR-DIAG-2 | MED |
| 3 | CFTS004 未收之 50 條 FR（清單見 `data/cfts004_uncited_fr.tsv`）—— 供 RD 回饋，非本 feature 產出對象（R-DIAG8(a)）| N/A（不需取得）| 0 | 無 | FB-DIAG-d | LOW |
