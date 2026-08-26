# ANOMALIES — bed_lowering

| ID | 標題 | 證據 | 提議處置 | 狀態 |
|---|---|---|---|---|
| A-BLM1 | 規格 PDF 副本尺寸不一致 | 磁碟上兩份：`features/bed_lowering/inputs/…(June 21 2021).pdf` = 665,190 B；`spec-index/sources/…(June 21 2021).pdf` = 664,990 B。另有 Claude Project 附件副本 = 1,634,623 B（不在磁碟，未能驗） | **已裁 R-BLM4：以 `inputs/` 那份為準**（見 `docs/handoff/01_intake_recon.md` §二）。磁碟兩份經 sha256 + metadata + 全文 + 逐頁 render 比對：同一次輸出之同一文件（Title/Author `T6133SW`/Producer `Microsoft: Print To PDF`/CreationDate 2021-06-25 18:46:52 全等），pdftotext 全文 11,349 字元逐字元相同，21 頁中 20 頁像素相同。差異僅 p.3：`spec-index/sources/` 那份被作者 `SD63673` 於 2025-11-04 加了兩條紅色 Line 標註（斜跨 Change Log 頁，實為打叉）並重存線性化。故取無標註之 `inputs/` 原始輸出。**非版次衝突，勿記為版本問題** | RESOLVED（磁碟兩份已裁；Project 附件副本 1,634,623 B 之差異未驗，見下）|
| A-BLM2 | Analysis Report 封面日期早於來源規格發行日 | 037 封面 `Date：2020/09/05`；來源規格 `June 21 2021` | 疑為模板殘值，不影響 TC 內容。建議 ACCEPT 存查，不向上游查詢 | PENDING |
| A-BLM3 | 037 Source Requirement ID 於 SYS1 匯出無可見對應欄 | 037 之 `SYS-HMI-RA-BLM-nnn`（42 個相異值）不出現於 SYS1 任一欄；SYS1 用 `NRL-nnnnnn` + Outline 號 | **已驗：`_polarion` 分頁展開完畢（A3:F84），內容為 Polarion round-trip 元資料（NRL id、revision 11545、checksum、outline level、欄位→字段對照），**無 SYS-HMI-RA 對應**。對應缺口確認存在，後續並入 A-BLM4** | RESOLVED（驗證完成；問題本身轉 A-BLM4）|
| A-BLM4 | **spec_reference 無章節錨 —— 阻斷 Phase 4** | 037 `HMI Source ID` 相異值數 = **1**（218/218 列皆為純檔名，無章節號後綴）；SYS1 `SYSRE_HMI_Source ID` = `{檔名}_{章節號}` 70 列各異；兩者相交為空。IN §10.7(b) 要求章節號，上游正式欄給不出。176 條 leaf 全數受影響 | 三選一（甲 DR-2 索對照表／乙 沿用檔名級＋[OVERRIDE]／丙 [DERIVED] 逐條追認），詳 `framework.md` Part VI。**分析層無傾向，不代裁** | **PENDING — 阻斷** |
| A-BLM5 | SYS-HMI-RA-BLM 有 24 個缺號 | 001~066 中 037 僅引用 42 個；缺：3, 5, 6, 8, 12, 18, 19, 21, 23, 26, 28, 30, 32, 33, 35, 38, 39, 41, 42, 47, 53, 56, 61, 62 | **不先寫結論**。可能為 SYS 側非 HMI 項（底盤、電氣），亦可能為 037 未分解之項 —— 二者於手邊文件區別不出來，判定需 SYS 側原件（同 DR-2）| PENDING |

## 說明

- 狀態：PENDING / RESOLVED / ACCEPTED（ACCEPTED = 已知且不修，非已解決）
- 登錄屬 Tier 1（執行層可自行 register），**裁決屬 Tier 2**（FO §0）
- A-BLM1 之要點（2026-08-26 更新）：磁碟上兩份之位元組差異已驗畢並裁定（R-BLM4），
  原提議「指定 `spec-index/sources/` 版為 canonical」**已不採納**，其立論前提亦不成立 ——
  該提議稱「spec-index cache json 由其產生」，但實測 cache json 之 `source_file` 欄自陳來源為
  **xlsx** 而非 PDF（`entries` = 70，與 SYS1 Basic Report 之 70 個 Polarion 物件相符），
  cache 與 PDF 之 canonical 選擇彼此無關。
- 尚存之未驗項：Claude Project 附件副本 1,634,623 B（約為磁碟兩份的 2.46 倍）。
  該檔不在磁碟，無從跑 hash。尺寸差距過大，不宜比照磁碟兩份逕推為「重存差異」——
  可能為未經 print-to-PDF 壓縮之另一輸出，亦可能含磁碟版所無之內容。
  凡引用規格頁面者一律以 `inputs/` 那份為準，不取 Project 副本；
  若日後該副本落磁碟，依同法比對後併入本列。
