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

## [A-AM03] B1 之 50 錨有 7 個不在 R-AM2 錨源池內（圖表型物件遭匯出遺漏）— PENDING，阻塞 7 葉

2026-08-26 開工前置查核：以 03 包 §四 之 50 個錨值比對 R-AM2 所定之錨源池
（兩本 Basic Report，實測 811 個 ObjectID＝Part1 245＋Part2 566，與 01 包
§一 記載相符），**43/50 命中，7 個不在池內**：

| SWE ID | 錨 | Test Set |
|---|---|---|
| SWE1_AMM_138 | CFTS019-4866479 | Source Transition |
| SWE1_AMM_156 | CFTS019-4866520 | Source Transition |
| SWE1_AMM_157 | CFTS019-4866522 | Source Transition |
| SWE1_AMM_200 | CFTS019-4866839 | Source Transition |
| SWE1_AMM_205 | CFTS019-4866850 | Source Transition |
| SWE1_AMM_240 | CFTS019-4866956 | Source Transition |
| SWE1_AMM_241 | CFTS019-4866967 | Source Transition |

**這 7 個不是分析層錯配。** 七者於 CFTS019 全文 PDF 中均為
`[Artifact Type:Subsystem Functional Requirement] [State:Approved]` 之正式
需求，語意亦與各自 SWE 葉相符（例：4866479 = "Source Transition:
Entertainment Active -> Entertainment Active" 圖，對 SWE1_AMM_138
"Entertainment Source Transition Timing"）。錨本身正確，缺的是匯出。

根因（實測，非推測）：**兩本 Basic Report 系統性遺漏圖表型需求物件。**

- 圖表型物件（正文為 "Refer to the … figure" / "Following diagram refers to"）
  在池率 **1/13 = 7.7%**
- 非圖表型物件在池率 **670/1717 = 39.0%**
- 池外之圖表型物件共 12 個，本批 7 個全在其中

已排除之替代解釋：EE Architecture 過濾。其中 4 個僅掛 `Atlantis Mid`
（本案為 Atlantis High），一度疑為範圍過濾所致；但全文中僅掛 Atl-Mid 之
物件共 491 個、其中 229 個在池內，匯出並不依 EE Architecture 篩選。
另 3 個（4866479/4866520/4866522）本就掛 `Atlantis High`。假設推翻。

此即 FEATURE_ONBOARDING §3 所載之 **Mode A blind spot**（Polarion 匯出
靜默丟內容），canon 明訂處置為「packaged as ONE chapter-level re-export
request upstream」，不作逐物件修補。

**處置：待 Pei 裁定（Tier 2），執行層不自裁。** 三個選項：

1. 依 R-AM2 字面，7 葉填
   `PENDING: DR-AM1 SWE1-to-CFTS ObjectID mapping unresolved for this leaf`。
   代價：7 條 TC 之 specification_reference 空懸，且 DR-AM1 之回件（正式
   對照表）未必能解 —— 問題不在對照表缺失，而在匯出缺物件，回件後仍缺。
2. 錨值照 03 包 §四 寫入（值已於全文 PDF 逐一驗證為正確且 Approved），
   於 reasoning 註明「錨在 R-AM2 池外、經全文佐證」。代價：與 R-AM2
   「錨定物件池 = 兩本 Basic Report」之字面牴觸，需 Pei 明文放寬。
3. 7 葉暫緩，B1 先出 43 葉，待 DR-AM3 補件後補做。

執行層建議選項 2 併發 DR-AM3：錨值已具全文佐證，其可信度高於填 PENDING；
且選項 1 之 PENDING 指向 DR-AM1 屬誤導 —— 兩者根因不同。

---
