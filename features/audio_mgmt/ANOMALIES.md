# ANOMALIES — FW036 Audio Management HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-AMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

## [A-AM01] 01/03 包所記檔名與交付實際檔名不符 — CLOSED（R-AM11，分析層自訂正 2026-08-26）

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

**結案（R-AM11）：** 分析層採認並溯源 —— 包 01／03 之檔名取自 Claude Project
掛載副本，該介面對空白與點號做了正規化而失真。今後包內來源指涉一律以
`inputs/` 實名為準，掛載名僅作內容識別。執行層改取實名之處置獲追認。

## [A-AM02] 01 包 §一 對檔 2（CFTS019 全文）之格式判定有誤 — CLOSED（R-AM12，分析層自訂正 2026-08-26）

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

**結案（R-AM12）：** 分析層採認並釐清落差之根源 —— 雙方讀的不是同一件工件。
分析層讀掛載副本（介面抽取後之產物，確為純文字），其 234 為大括號包裹之
**章節級標題 ID**；執行層讀 `inputs/` 原件，為真 PDF、文字層完好、1,964 個
ObjectID、上界 4867784。分析層明認「作為對來源工件之判定，包 01 寫錯」
（以量失真之副本屬性寫成原件屬性），以執行層實測為準。

**B3 之落點（本條之實際效力）：** 篩選以全 ID 集、上界 **4867784**，
不得沿用 4867749。與 R-AM11 同根 —— 掛載副本不可代表原件。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-AMnn]`.

## [A-AM03] B1 之 50 錨有 7 個不在 R-AM2 錨源池內（圖表型物件遭匯出遺漏）— RESOLVED（R-AM2′，Pei 2026-08-26）

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

**裁定（Pei 2026-08-26：「2採 R-AM2′准 DR-AM3發」）：採選項 2。** 七葉之錨
照 §四 寫入，reasoning 逐條註明「池外錨，全文佐證」，上繳包附池外錨登記表
（七列，由 `scripts/gen_b1.py` 產於 `generated/B1.json` 之
`out_of_pool_anchors` 鍵）。七葉屬「Refer to figure」型，行為序列以圖說附文
＋SWE.1 Description 為據；時序值仍循 IN §8.4.1 不造值 —— 僅於具名參數可解者
（4867766／4867767／4867768／4867769／4867773）引用，其餘只驗相位順序。
B1 因此回到完整 50 葉，無葉暫緩。

---

## [A-AM04] CFTS019 以 `<Temp Ramp Down>` / `<Temt Ramp Down>` 指涉一個從未定義的參數 — 待分析層採認

全文實測：`<Temp Ramp Down>` 與 `<Temt Ramp Down>` 於 CFTS019 出現 10 次
（含 4866844、4866853、4866855 三個 B1 錨），但**全文無其定義列**。
1.5.4 Variables 章只定義 `<Tent Ramp Down>`（4867767，Max 50ms／Min 25ms）。

判讀：`Temp` / `Temt` 幾乎確定為 `Tent` 之拼寫錯誤 —— 三者字母僅差一位，
語境（entertainment 來源之 ramp down）亦完全吻合。

**執行層未代換。** 包 03 前言明訂「機械套用，不自行裁量，查無之值一律
`PENDING: DR-{n}`，禁止推斷」。故 SWE1_AMM_203／206／208 三條 TC 之時序
以 `PENDING: DR-AM5` 交付，判讀僅記於此並上呈，不入交付欄。

影響：3 條 TC 之時序界值待補。行為面（ramp down 先於新來源、輸出全程靜音）
不依賴該值，已正常驗證。若分析層採認拼寫錯誤之判讀，三條 TC 可直接以
4867767 之 25–50ms 回填，無須重寫。

## [A-AM05] 供應之 DBC 缺 `$HUModeStatus$` 與 `$VolumeENT$` — 依 R-13 (g) 保留原文名

包 03 §三.5 要求訊號寫成 `$MESSAGE.Signal$ = raw (label)`，label 逐字取
DBC `VAL_`。本批涉及之訊號實測結果：

| CFTS 原文訊號 | DBC 查詢結果 | 處置 |
|---|---|---|
| `$SOSCallType$` | **查得** —— `TBM_FD_1.SOSCallType`，`VAL_` 標籤與 CFTS 原文逐字相符（2=Manual_SOS_call、3=Automatic_SOS_call、4=Callback_SOS_call） | 補全名，依 §三.5 全式寫入 |
| `$HUModeStatus$` | 查無，且無任何命名變體（已掃 FDCAN8 1,916 訊號＋BHCAN2 344 訊號） | 依 R-13 (g) 保留原文名，記 DR-AM4 |
| `$VolumeENT$` | 查無；兩本 DBC **無任何 volume 類訊號** | 同上 |

未以近似訊號代換（§三.5 明令禁止）。`HU_Off` / `DAB_Selected` / `FM_Selected`
等 label 因 DBC 無對應項可核，逐字取自 CFTS019 原文並加引號。

附帶一致性註記：4866880 之 label 為 `"HU_Off"`，而 SWE.1 描述寫 `HU_OFF`
（全大寫）。交付採 CFTS019 之拼法，因 R-AM2 定 CFTS019 為錨且 DBC 無第三
來源可裁。

## [A-AM06] `backend.xlsx_surgical.verify_structure` 不計 `<conditionalFormatting>` — 本 feature 自補，建議上收

`verify_structure` 驗三件事：zip 成員集不變、classic `<dataValidation>` 與
`x14:dataValidation` 計數不變、非 patched 成員不得有位元組差異。

缺口：**`<conditionalFormatting>` 不在計數之列**，且該缺口無法由既有三項
補起 —— 目標 sheet 本來就在 patched 集合內、允許位元組差異，故 CF 元素若於
patch 過程被剝除，三項檢查**全數通過**。

處置：`features/audio_mgmt/scripts/write_back.py` 之
`check_conditional_formatting` 於 feature 端自補此計數，寫回前後比對，
不符即 raise。

**未逕改共用模組。** `backend/xlsx_surgical.py` 為十五個 feature 共用，
新增一道 raise 型硬 gate 可能使其他 feature 之既有寫回失敗（若其 CF 計數
本就會合法變動）。建議由掌握全案者評估後上收為通案，本 feature 先行自保。

附註：本次寫回之母本 CF 計數為 0，故該檢查**實際上未被考驗**（vacuously
true）。其價值在於未來換用含 CF 之母本時能攔下，不宜以本次綠燈為其有效性
之佐證。

## [A-AM07] CFTS019-4866123 將行為本體外包至 `{CFTS020}`，該文件不在 `inputs/`

SWE1_AMM_061（Power Button Mute Handling）之錨 4866123 全文為：

> `IF the HU receives the signal/value $ICSPowerButton$ = [pressed] THEN the
> HU shall apply the mute logic as described in {CFTS020}.`

錨定本身無誤 —— 該物件是 CFTS019 中唯一述及 `$ICSPowerButton$` 者。問題在
**行為本體不在本 feature 之來源範圍內**：葉描述之音量/靜音狀態評估、
螢幕 On/Off 狀態、螢幕優先權判斷，於 CFTS019 全文（1,730 物件）皆無對應文字。

處置：錨照定，TC 之行為步驟就 CFTS019 可佐證者撰寫，外包部分掛
`PENDING: DR-AM6`，不臆造 CFTS020 之內容（IN §8.4.1）。已開 DR-AM6 請補件。

附註：此為**跨文件外包**型缺口，與 A-AM03（匯出遺漏）、A-AM04（參數未定義）
根因均不同 —— 前二者之內容在 CFTS019 內，本件不在。三者不可混為一談。

