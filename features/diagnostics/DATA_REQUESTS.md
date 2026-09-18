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
| 1 | ~~**NRC 值之權威來源**~~ —— **CDD-13_A 內查結案**：`CS.00100.pdf` Annex A（NORMATIVE，p61–75）之 NRC 流程圖已取得並逐節點轉錄（`data/cs00100_annex_a.md`）。`-156` 依 Figure A-2 之 `Condition check` 取 `$22`；`-237` 依 Figure A-11 之 `Was correctly altered into server's memory` 取 `$72`；`-157` 本即 unsupported SID 型 | **CLOSED** | — | **PENDING 清零，lint `U` 由 3 → 0** | A-DIAG01 | **CLOSED** |
| 2 | `SYS3_CFTS_004…SYSAD.docx` 之 UDS 序列補件 —— 現本無 UDS 請求／回應位元組表、無 NRC 表，唯一序列表為 DTC 流程（037 之 DTC 列 = 0）| PARTIAL | 全 388 產出列之 `test_procedure` | 位元組步驟改自 037／CFTS004 逐列推出，成本升高；不阻斷 | DR-DIAG-2 | MED |
| 3 | CFTS004 未收之 **52** 條 FR（清單見 `data/cfts004_uncited_fr.tsv`；含 V1 (3) 刪列後回歸之 `SYS-RA-DIAG-167`／`-168`）—— 供 RD 回饋，非本 feature 產出對象（R-DIAG8(a)／R-DIAG8(amend)）| N/A（不需取得）| 0 | 無 | FB-DIAG-d | LOW |
| 4 | ~~**診斷 session 前提**~~ —— **CDD-03 T2 內查結案**：SYSAD §4.5 Assumptions 明載「ECU starts in Default Session」「Security access (0x27) is required for: Write DID / Routine execution / DTC clearing」；Hardware Dependencies 明載「Diagnostic connector (OBD-II)」。CFTS004 全欄 grep 13 筆全為假陽性 | **CLOSED** | — | 無 —— pilot PENDING 15 → 2 | DR-DIAG-3 | **CLOSED** |
| 5 | **各 I/O DID 之 `controlState` 編碼**（R-DIAG29(b) 改題；原題「`$5000` controlOptionRecord 編碼」）—— **IOCP 本身已解**：CS.00100 Table 51 明載 `00 Return Control to ECU`／`01 Reset to Default`／`02 Freeze Current State`／`03 Short Term Adjustment`，請求式定為 `2F <DID> 03 <controlState>`。**仍缺**：`03` 之後那個 `XX`（Table 51 NOTE 之 Control Option Record）對各 DID 各選項之實值 | MISSING | 15 個 I/O DID／114 個 037 列 | 不阻斷（佔位可執行，值待補）| DR-DIAG-4 | **HIGH** |
| 6 | **資料位元組之值域與 record 版面** —— `<brightness byte>`（$283F 值域）／`<AV Channel Number>`（$0312 通道號）／`<module version record>`（$2843 子欄位版面）／`<signal quality record>`（$2841）。CFTS004 載欄位名而未載編碼；依 R-DIAG5(b) 條文例示以 `<…>` 佔位書寫，非 PENDING | MISSING | 全部含資料位元組之 TC | 不阻斷（佔位可執行，值待補）| DR-DIAG-5 | MED |
| 7 | **`KeySense HMI Logic and Flow`** —— CFTS004-4940469（`$030A` Clear Key Sense PIN，`SWE1-Diagnostics-347`）明引該件為常式行為之定義來源，而該件不在來源集、CFTS004 亦未載其文件編號與版本。名稱逐字取自引用處 | MISSING | **1**（`NR1L-DIAG-290`）| 不阻斷 —— 依 R-DIAG19，到件前 ER 只斷言常式正回應與完成；到件後 Revise | A-DIAG43 | MED |
| 8 | **`SX-9830-0095 "Sirius XM Multi-Package Factory Activation OEM Requirements"`** ＋ ~~`CIP Radio Tables`（`MPFA Select Process`／`MPFA Validate Process` 流程圖）~~ —— **流程圖已到**：`forms/CIP_Radio_Tables_v6.7.xlsx`（2026-09-16 即在 `forms/`，CDD-12 登錄，doc_id `cip_radio_tables_v6_7`），逐節點轉錄見 `data/cip_mpfa_flowcharts.md`。**餘二項**：`SX-9830-0095` 本文、vehicle sales code → PkgIndex 對照表（兩者皆不在 CIP Radio Tables 內） | **PARTIAL** | 13（`$0307` 5 ＋ `$0309` 8）| 不阻斷 —— retry 五結局已依流程圖 NOTE 產出；`<Package Indication value>` 佔位維持（18 行）| A-DIAG48 | MED |
| 9 | **不支援之 SID 與 DID 清單**（R-DIAG22(amend) 改題；原題「不支援之 SID」）—— 本 ECU 不支援之 UDS 服務識別碼**至少一個**，**以及**不受支援之 DID **至少一個**。後者為 R-DIAG22(amend) 之讀類值域軸所需（請求 `22 <unsupported DID>`，ER `7F 22 31 requestOutOfRange`）。SYSAD §4.5 只正面列出支援之三個 SID（`0x22`／`0x2E`／`0x31`），未給不支援清單；DID 側三處來源皆未載 | MISSING | `<unsupported SID>` 184 行 ＋ `<unsupported DID>`（本包新增）| 不阻斷（佔位可執行，值待補）| DR-DIAG-6 | **HIGH** |
| 10 | ~~**`CS.00100` 原件**~~ —— **CDD-13_A 內查結案**：`1_Customer_Requirement/STLA Standard/CS.00100.pdf`（81 頁，Change Level D，sha16 `c1f9c6d7c5a5f0a2`），已登 MANIFEST `cs00100_uds_on_can_D`。Annex A 為向量文字，浮水印以字型（`Helvetica-Bold`）濾除後全文可讀 | **CLOSED** | — | Annex A 五圖已轉錄 | A-DIAG65 | **CLOSED** |
| 11 | **`SD.00049` 之附件 `Diagnostic Services Secure Access Rights 28JAN2026.xlsx`** —— **原件 `SD.00049.pdf` 已取得**（`STLA Standard/Update/`，Change Level F，sha16 `456413aba708fbdb`，已登 MANIFEST），其 §3 明言「The embedded Excel file (Section 4) defines the access rights for each UDS and KWP function and role」，**該 xlsx 未附於 PDF**（無 FileAttachment 註記）。矩陣本身仍缺 | MISSING | I/O 母節 114 列之 PC-3 判定 | 不阻斷（R-DIAG13 保守維持）| A-DIAG66 | MED |
| 12 | ~~**`CS.00102` 原件**~~ —— **CDD-13_A 內查結案**：`STLA Standard/CS.00102.pdf`（sha16 `da5caf89903bb53d`），已登 MANIFEST `cs00102_std_diag_data` | **CLOSED** | 0（037 未引標準 DID）| 供 DID 落區校核 | A-DIAG67 | **CLOSED** |
