# ANOMALIES — FW036 Audio Management HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-AMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

## [A-AM01] 01/03 包所記檔名與交付實際檔名不符 — RESOLVED（執行層自處，無需裁定）

四件客戶來源之實際檔名在點／連字號／空白處與 01 包 §一、03 包 §一 所記
不同（包內為正規化寫法）。照包抄入 `feature.yaml` 則 `resolve_path` 四鍵
全部 glob 到 0 檔。

| 包內所記 | inputs/ 實際 |
|---|---|
| `SWE_1_Audio_Management_Pending_For_Review.xlsx` | `SWE.1_Audio_Management_Pending_For_Review.xlsx` |
| `CFTS019AudioManagementPart1_released_20260415.xlsx` | `CFTS019-AudioManagement-Part1_released_20260415.xlsx` |
| `CFTS_019_Part2_All_AcceptedExceptDTCrework.xlsx` | `CFTS 019_Part2 -All Accepted-Except-DTC-rework.xlsx` |
| `R1LR_..._CFTS_019_Audio_Management_20250910_1235.pdf` | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.pdf` |

處置：`feature.yaml` 之 `paths` 一律取**實際檔名**（檔案系統為事實基準），
五鍵均已驗證恰好 glob 到 1 檔。此為本地路徑，非錨值，不觸及「執行層不得
自行改錨」之禁令。包內敘述未改（分析層文件之修訂屬分析層）。

## [A-AM02] 01 包 §一 對檔 2（CFTS019 全文）之格式判定有誤 — 待分析層更正

01 包 §一 記檔 2「實為純文字（Requirement Specification Report 匯出，
非 PDF）」「副檔名 .pdf 與內容不符」，並記「章節 ObjectID 共 234 個，
範圍 4865821–4867749」。

2026-08-26 實測（`file` + `pdftotext`）：

- 確為**真 PDF**（PDF 1.5），非純文字；副檔名與內容相符。
- 文字層完好，`pdftotext` 抽出 13,887 行。
- 唯一 ObjectID **1,964 個**（非 234），範圍 **4865821–4867784**
  （上界非 4867749）。

影響評估：

1. **不推翻 R-AM8（spec_mode D）**。D 之判準為「reference is looked up,
   never constructed」，本 feature 之錨值仍逐葉取自 03 包 §四表、不由
   outline 構造，故 D 成立。文字層之存在使 B 成為技術上可行，但不改變
   錨定機制，無須改判。
2. **正面影響**：全文可程式化查閱，03 包 §三.6 所需之 `<Tent Ramp Up>` 等
   時序實值已於 4867766–4867769 驗得 `Max = 50ms; Min = 25ms`，與 03 包
   所述 25–50ms 相符；且四者依序為 Tent Ramp Up／Tent Ramp Down／
   Tinfo Ramp Up／Tinfo Ramp Down，正對應 §四表之 SWE1_AMM_275／276／
   277／278，該組「人工改錨至 1.5.4 Variables」獨立驗證通過。
3. 234 vs 1,964 之落差建議分析層複核其 F1 之統計基礎（234 疑為僅計
   Heading 類或僅計 TOC 條目）。ObjectID 上界 4867784 亦高於 01 包所記，
   B3 若依 4867749 為界篩選會漏件。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-AMnn]`.
