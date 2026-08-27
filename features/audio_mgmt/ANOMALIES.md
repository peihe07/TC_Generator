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

## [A-AM08] ~~`<vent off>` 全文未定義~~ — **本條前提錯誤，CLOSED**（見下方更正）

CFTS019-4866818 之 Main Audio 衰減量寫作 `<vent off>`。全文檢索：**出現 1 次
（即該錨本身），無定義列**。

與 A-AM04（`<Temp Ramp Down>` 出現 10 次無定義）同型但獨立：本件之參數僅
出現於單一物件，無「拼寫錯誤」之判讀空間 —— 08 包 §三.5 已明訂
`<vent off>` 與 `<Vent Nav Off>`（4867671／4867783，= **9 steps**）為
**不同參數，勿互代**，故不得以後者之值代入。

處置（原）：SWE1_AMM_287 之衰減量填 `PENDING: DR-AM8`，行為面照常驗證。

**結案（R-AM17）：** Pei 定 `<vent off>` = **−16 dB**，已回填 287，PENDING 撤除，
DR-AM8 撤回。ER 改為量測式：以起始位準為基準，Main Audio 較之低 16 dB。

**更正（2026-08-26，執行層自認）：本條之前提「全文未定義」係錯誤。**

錯因為**大小寫敏感檢索**：執行層只比對小寫 `<vent off>`（全文 1 筆，即錨文
本身），未比對首字大寫之 `<Vent off>`（**8 筆**）。定義列存在：

> **CFTS019-4867782**（1.5.4 Variables，[Radio: 含 R1L-R]）：`<Vent off> = -16 dB`

故 −16 dB **為 spec-sourced**，權威在文件而非裁定。R-AM17 降為對該規格值之
採認紀錄。287 之 reasoning 已改引 4867782（reasoning 非交付欄，交付欄摘要
比對前後一致，工作簿未重寫）。

**此錯之性質值得記：** 原註寫「以規格全文檢索此值者將查無」，用意是防止後人
誤判，實際效果卻相反 —— 會使後人放棄檢索一個確實存在的定義。**假留痕比無
留痕更糟**。檢索工具之大小寫敏感性，此後須於檢索類判定中一併聲明。

依 R-AM18 之回溯覆驗站範圍：287 之 spec_reference 補列 4867782、
312–317 補列 4867783，於 DR-AM3 回件後之同一次寫回併辦，不觸發即時回修。

對照：本批另兩個參數皆有實值並已入 TC —— `<Tdisp>` Max = 100 ms（VSIM 五葉）、
`<Vent Nav Off>` = 9 steps（314／316）。三者處置不同係因證據不同，非標準不一。

## [A-AM09] 寫回之 tc_id 逐批重新起算（已修）

B2 首次寫回時 `tc_id` 自 `NR1L-AMM-001` 起算，與 B1 已用之 001–070 全面碰撞。
根因：`write_rows` 以批次內 offset 計序（`fmt.format(n=offset + 1)`），
該式在單批交付下正確，跨批即失效。

修正：新增 `next_tc_seq()`，自**工作簿既有列**讀出最大序號後續接 ——
序號之權威為簿內既有資料，非批次之內部偏移。B2 因而為 071–136。

同時修正之相關項：`write_back.py` 原一律以 `paths.workbook`（母本）為來源，
B2 若照跑會自第 10 列重寫並靜默覆蓋 B1 之 70 列。新增 `--source`，
交付簿改為累積式。

驗證：累積簿 136 列（70 + 66），tc_id 001–136 無重複、無缺號，
dataValidation 計數不變。

## [A-AM10] ~~4867598 之池籍爭點~~ — **撤回，執行層之工具缺陷所致**（見 A-AM13）

包 16 §一 撤除 264 之「單源佐證」標記，理由為「匯出實有該物件」，
並稱已代行覆核（「匯出與全文同文」）。

**執行層複驗不支持該判定。** 方法：逐格掃描兩本 Basic Report 之**每一儲存格**
（非僅 ObjectID 欄），比對字串 `4867598` —— **零命中**。

```
sys1_export        (Part 1, 245 物件)  0 命中
sys1_export_part2  (Part 2, 566 物件)  0 命中
```

研判：包 16 之覆核所讀者為**全文 PDF** 之 4867598，非匯出。兩者同文係
因該物件本就只存在於全文；「匯出與全文同文」之觀察無法區分「兩處皆有且
一致」與「僅全文有」。

**影響**：264 若實為池外，則其佐證仍屬 R-AM18 之單源，不應入池內逕寫段。
執行層之交付**維持 264 為池外**並列入池外錨登記表（B4 池外 6 葉：
264、266、306、307、308、311），與包 16 §一 之 5 葉不同。

**待分析層裁定**：以何者為準。若包 16 之判定另有依據（例如讀的是本
`inputs/` 以外之匯出版本），請指明；否則建議依實測更正 §一，
並將 264 併回池外集合。

（包 16 §一 對 **311** 之指正執行層全面接受：15 包 §一 將 A 級 30 葉
整批掃入逕寫段，未先過池籍過濾，確違 R-AM20 除外條款。程序已改：
B4 之逕寫集合先過池籍過濾再併入。）

## [A-AM11] 第二路三次漏查之共通機理（020／024／146）

包 16 §三 推翻執行層對 C 級三葉「維持 PENDING」之建議，三葉皆有正解。
三次失誤之根因各異但同屬**檢索方法**層級，記錄以免重犯：

| 葉 | 正解 | 漏查原因 |
|---|---|---|
| 020 | 4865981 ⏎ 4866286 | **讀取截斷**。4865981 全文為「can be played on all channels, **but at a minimum shall be played on the front channels**」；執行層之輸出截於 135 字，只見前半「all channels」即判「範圍與葉之 front 不符」而駁回。**駁回理由建立在未讀完的句子上** |
| 024 | 4866001 | **未搜葉本身**。該葉之 SWE.1 描述原文即載 `CFTS019-4866001`；執行層搜遍規格語料卻未搜需求文字。另該物件為內嵌表格（匯出 Description 欄為 `(image: ….rtf)`），任何文字檢索皆不可達 |
| 146 | 4866498 | **詞形單一**。搜「remaining channel」單數，原文為「remaining **audio** channels」 |

與先前 A-AM08（`<Vent off>` 大小寫敏感）合計四例，共通處為
**以單一詞形／單一視窗之檢索結果作為否定結論之依據**。否定結論
（「查無」「不符」）比肯定結論脆弱：肯定只需一個命中，否定需窮盡。

改善（執行層自酌，不立條）：`route2_*.py` 之輸出改為全文不截斷；
檢索前先取葉之 SWE.1 描述掃 `CFTS019-\d+` 字樣；檢索詞加入單複數與
常見同義擴充；對匯出 Description 為 image/wrapper 者另行標記。

## [A-AM13] 池籍抽取漏 58 個多值格 —— **A-AM03 之根因判定作廢，A-AM10 撤回**

包 18 揭示池基準為**展開池 v2（891 ID，多值格逐一展開，A-AM12）**。
執行層據以複驗自身之抽取，確認缺陷：

`pool()` 以 `re.fullmatch(r"48\d{5}", cell)` 測試每格，**只認整格恰為單一
ID 者**。實測兩本匯出有 **58 個多值格**，該式因而漏掉 **86 個 ID**
（811 vs 891）。

### 連帶作廢之判定（三件）

**1. A-AM10 撤回。** 4867598 在展開池內。包 16 §一「匯出實有該物件」正確；
執行層之「逐格掃描零命中」係以有缺陷之正規式掃描，結論無效。
264 為**池內**，其 R-AM18 單源標記撤除。

**2. A-AM03 之根因判定作廢。** 原判「匯出系統性遺漏**圖表型**需求物件」，
證據為圖表型在池率 1/13＝7.7%。以展開池複驗：

| 母體 | 舊（嚴格池 811） | 新（展開池 891） |
|---|---|---|
| 圖表型物件池外率 | 12/13 ＝ **92%** | **0/13 ＝ 0%** |
| 非圖表 FR 池外率 | 982/1562 ＝ 63% | 911/1562 ＝ **58%** |
| 全體物件池外率 | 1059/1730 ＝ 61% | 974/1730 ＝ **56%** |

**圖表型物件 100% 在池內。** 該類物件恰好多落於多值格，遂被抽取缺陷
整批誤判為缺漏。**A-AM03 之標題主張因此完全不成立**。

**仍然成立者**：一般性遺漏為真（非圖表 FR 池外 58%），
且 **1.3.3.12 Reverse Mute 全章（4866821–4866826）以展開池複驗仍全數池外**。
故 DR-AM3 之請求不失其據，惟其**理由須全部改寫**：不是圖表，是普遍性缺漏。

**3. B1–B4 池外登記表誤標 10 筆（30 筆中 33%）。**

| 批 | 原登記 | 更正後 | 誤標葉 |
|---|---|---|---|
| B1 | 7 | **0** | 138、156、157、200、205、240、241 —— **全部** |
| B2 | 10 | 10 | 無 |
| B3 | 7 | 7 | 無（147 之雙錨中 4866878 確為池外） |
| B4 | 6 | **4** | 264、266 |

**B1 之七葉即 A-AM03 之原始證據，亦即 R-AM2′ 立法之事實基礎。**
該七葉從未在池外；R-AM2′ 對 B1 而言前提落空（該條對 B2／B3 之真池外葉
仍有效）。

### 更正之施行

- 四支工具之池抽取全部改為 `re.findall` 多值展開，且以 **ObjectID 欄**
  為母體（掃全欄位得 897，含 `{CFTS019-5129}` 型行內參照；參照非匯出物件）。
  修正後三支工具一致得 **891**，與包 18 相符。
- 四批 JSON 重生，**交付欄摘要逐批比對前後一致**（B1 `1385996c…`、
  B2 `bfe9e96c…`、B3 `583d098e…`、B4 `31d8c8e7…`），故**工作簿未重寫**。
- 誤標葉之 reasoning 中「池外錨，全文佐證（R-AM2′）」等語已改為更正敘述。

### 機理（併入 A-AM11 之系列）

本件與 A-AM08（大小寫敏感）、A-AM11（截斷讀／未搜葉本身／單數詞形）同屬
**檢索與抽取之形態假設未經檢驗**。A-AM11 所記「否定結論需窮盡」在此再現：
「不在池內」是否定結論，而支持它的是一個未驗證的格式假設
（每格恰一個 ID）。**抽取正規式亦須以資料反證，不得以直覺定形**。

## [A-AM14] 同文異錨之位置測試：已交付四批複掃，兩葉需裁

包 24 §三（D-B6-01）指出 R-AM15 之雙路獨立性在**同文異錨**場合失效——
兩路皆做文本核驗，文本真的一致，故必然一致；唯位置可區辨。

執行層據此新建 `scripts/same_text_anchors.py`（偵測文本孿生 ＋ 自動位置
夾定），回溯掃 B1–B5：

| 批 | 有孿生之錨 | 位置測試通過 | 需人讀 |
|---|---|---|---|
| B1 | 14 | 6 | **2** |
| B2 | 7 | 5 | 0 |
| B3 | 3 | 2 | 1（已裁，見下） |
| B4 | 2 | 1 | **1** |
| B5 | 0 | — | 0 |

**已裁者**：B3 之 141（4866490，孿生 4866467）——包 12 §四.2 已明裁
「141 取 4866490」，非新問題。

### 需裁一：SWE1_AMM_169（B1，已交付）

錨 4866603。孿生**三個**：4866617、4866630、4866660，四者本文逐字相同：

> `Then, HU shall Ramp Up the signal source on the indicated channels`

四者分屬四個信號源子章節（Park Assist／Side Distance／Blind Spot／BSIS）。
位置窗口為 (4866590, 4866715) —— 鄰葉 167 與 189 相距過遠，**四者皆在窗內**，
位置無法區辨。

與包 24 §一 所裁之 170／171／172 同族（同一批 store／recall／ramp 重複條列）。
**待裁**：169 是否確取首現（Park Assist 段），或該葉本為泛用需求而需
另行處置（如 §8.2.2 一 RD 多 TC）。

### 需裁二：SWE1_AMM_266（B4，已交付）

錨 4867604。孿生 4867602，兩者本文逐字相同：

> `ELSE it is not present and the user cannot activate neither deactivate
> surround sound`

**另有更直接之候選 4867599**：

> `IF $Surround$ = [0] THEN the HU shall **disable the HMI** for turning
> surround sound on/off in audio settings`

該句與 264 之錨 4867598（`IF $Surround$ = [1] THEN … enable the HMI`）
構成明確之 §7 列舉配對，而葉 266 之描述為
「disable the Surround Sound **menu** and prevent any configuration」——
**前半對 4867599、後半對 4867602／4867604**。

**待裁**：266 維持 4867604、改錨 4867599、或併列 4867599 ⏎ 4867604。
若改錨或併列，`spec_reference` 為交付欄，需重寫回。

### 方法學

位置測試將 26 個孿生錨窄化至 4 個需人讀，其中 2 個為真問題、1 個已裁、
1 個為窗口反轉之工具限制（鄰葉引 1.5.4 Variables 物件，其文件位置遠離
需求本身，窗口因而失效——已於工具中標示而非誤報為錯置）。

**位置測試不是萬能**：鄰葉相距過遠時（169 之 (4866590, 4866715)）窗口
過寬而失去區辨力。此為第三個已知之雙路／位置法邊界，
繼 R-AM18（池外同源）與 D-B6-01（同文獨立性失效）之後。

## [A-AM15] SWE1_AMM_268 之錨與其鄰葉位置序不合（包 24 §一 之定案，生成後由工具攔下）

CFTS019 於 1.5.2.19 段有**兩份逐字平行之 Loudness 區塊**：

| 前段（copy A） | 後段（copy B） | 本文 |
|---|---|---|
| 4867639 | 4867646 | `loudness menu item is present on HU IF $AudioSystemType$ == "Base"…` |
| **4867640** | **4867647** | `In this case loudness shall be performed on entertainment sources only.` |
| 4867641 | 4867648 | `loudness menu item is not present on HU IF … == "Fiat Booster"…` |

包 24 之定案為：**267→4867639（A）、268→4867647（B）、269→4867641（A）、
271→4867648（B）**。

位置序因而斷裂：267@4867639 → 268@**4867647** → 269@4867641。
`same_text_anchors.py` 之位置測試據此標記
`anchor outside its window (4867639, 4867641)`，且**孿生 4867640 在窗內**。

**觀察（非主張）**：若 268 取 4867640（copy A），則 267／268／269 三葉
落在同一份區塊且位置單調；271 取 4867648 作為 269 之同文異錨對亦不受影響。
惟如此則 4867646 無對應葉。

**執行層未改**：R-AM15 禁單路定案，且本件為分析層已裁之錨；
**依裁定生成並交付**（B6 已寫回，350 列）。
**待裁**：維持 4867647，或改 4867640。若改，`spec_reference` 為交付欄，
建議併入 R-AM18 回溯站（連同 264 之改錨、169 之 reasoning 補註）。

### 工具改良（本件促成）

位置窗口原僅取**批內**鄰葉，131 因其鄰葉 130／132 在 B1 而窗口開放、
誤標為需人讀。已改為**跨批全域**葉→錨對照：B6 之需人讀數自 3 降至
5（母體亦自 5 升至 23），131 之誤報消除，其餘四件皆為已裁或已知
工具限制（098 為 A-AM14-b 之刻意反序、139 為窗口反轉、141 與 266 已裁）。

## [A-AM16] SWE1_AMM_221 之錨與位置及文本雙不合 — 留置回送

包 26 §二 定 221 → CFTS019-**4866489**。第二路兩項測試皆不支持：

**位置**：221 之 SYS-RA 為 **563**，夾於 220（561，錨 4866891）與
222（564，錨 4866894）之間；4866489 遠在該窗之外。
對照組：139／140／141 之 SYS-RA 為 370／371／372、錨 4866488／4866489／
4866490，**完全單調** —— 同一區塊之單調性成立，故 221 之偏離非隨機。

**文本**：4866489 為 `The HU shall store the current mode settings (…)` 單句。
葉 221 為「儲存**座艙音訊設定與顯示設定**」兩者。

**正解 CFTS019-4866893**（池內），逐字涵蓋兩者：

> `If an entertainment source is in use as a cabin audio source, when the
> second source becomes active, the following shall apply: The HU shall store
> the current cabin mode settings (HU volume, HU tone controls, mode, last
> tuned station…). **The HU shall store the current display settings.**`

且 4866893 落於 220@4866891 與 222@4866894 之間 —— **位置與文本雙合**。

**連帶**：4866489 若非 221 之錨，則其位置所指者為 **140**（SYS-RA-371），
即包 24 因「store／restore 矛盾」掛 DR-AM10 之葉。本件之裁定將影響
DR-AM10 之問法：若 221 改錨 4866893，則 140 與 4866489 之矛盾回到原點，
仍待上游澄清；若維持，則 140 之位置候選已被佔用，其 PENDING 之理由需改寫。

**執行層處置**：**留置 221，不交付**（B7 為 17 葉而非 18）。
R-AM15 禁單路定案，且交付一個位置與文本雙不合之錨，其代價高於延後一葉。

## [A-AM17] SWE1_AMM_293 之補交遺漏（葉集終核攔下）

293 之裁定於 B5 交付審即下達（錨 4866193、池外、部分覆蓋，RULINGS
2026-08-26 「B5 交付審三件」第 1 項），惟**補交從未執行**。
包 26 首段之葉集核對記「已交付∪B7 = 317，差集 0」係以 293 已補交為前提。

執行層之葉集終核（`data/leaves.tsv` 全集對已交付 req_id）實測
**315／317，差集為 {221, 293}**，因而攔下。

已補：293 寫入 B5（B5 遂為 51 條／50 葉，池外登記 12 筆，與裁定所述相符），
寫回鏈自 B4 產出重建。

**機理**：裁定與執行之間無自動勾稽 —— 一件「已裁但未執行」之項目
在下一次葉集核對前不可見。葉集差集核對（包 12 §七 之防線）證明有效，
惟其執行時機為**批次下放前**；本件為**交付後**才被發現。
建議將差集核對同時列為**每批上繳前**之檢查，而非僅下放前。

## [A-AM18] ~~B7 寫回未完成~~ — **已解**：`diff_cells` 於可寫 worksheet 上實體化空儲存格

**狀態：已解。** B7 之 17 條已寫入，交付簿為
`SWQT_AudioMgmt_B1-B7.xlsx`，**368 列**，tc_id 001–368 無重複無缺號。

### 量測

| 階段 | 耗時 |
|---|---|
| `load_workbook`（第一次） | 0.3 s |
| 寫入 17 列儲存格 | 0.0 s |
| `load_workbook`（第二次，供 diff 之原件） | **未於 10 分鐘內完成** |

根因（初判「走訪成本」，複查後更精確）：
`Test Case Specification` 分頁之 `max_row` 為 **1411**（母本模板帶約 1,400 列
預格式化空列），非資料列數 377。`diff_cells` 以
`old.cell(r, c)` 逐格取值——**而該呼叫在可寫 worksheet 上並非純讀取，
它會建立儲存格**。故每次比對在兩份 workbook 各**實體化約 35,000 個空儲存格**。
成本不只是走訪，是物件配置。

**該成本與本批寫入幾列無關** —— 每次寫回都全額支付，且隨批次累積不變。
B1–B6 得以完成係因當時仍在可承受範圍；至 B7 已越過臨界。

### 執行層之操作失誤（記錄，與根因無關）

診斷過程中我以 `pkill -f write_back.py` 清理殘留進程，該樣式**會匹配到
我自己輪詢指令之 shell wrapper**（其命令列含同一字串），因而
(a) 殺掉進行中之寫回、(b) 殺掉自己的等待指令（多次 exit 144）、
(c) 守衛 `pgrep -f` 同理誤判為「已有執行中」而略過啟動，或反致重複啟動
兩個並行寫入同一輸出檔之進程。此為排查噪音之來源，**非本件根因**。

### 解法（feature 端，共用模組未動）

openpyxl 本即以稀疏字典 `ws._cells` 存放儲存格。`write_back.py` 內以
`_sparse_diff_cells` 取代之：走**兩邊既有座標之聯集**，兩邊皆無之座標
其值必為 None、不可能是變更，語意完全等價，且不實體化任何儲存格。

**等價證明（非宣稱）**：以新實作重建 B1–B6 交付簿，得
sha256 `9c6a274f0834d40bb4daa9714d6f10149925176f5f2fc1c086a1736a3fe9d5df`
——與既交付檔**逐位元相同**。耗時自「10 分鐘未完成」降至 **1.0 秒**。

**共用模組之建議維持**：`backend/xlsx_surgical.py` 為十五個 feature 共用，
同一缺陷對其餘 feature 同樣成立（凡母本帶大量預格式化空列者）。
比照 A-AM06，登記並建議，不由本 feature 逕改。

**回溯站不再受阻**：R-AM18 之六項寫回（上繳包 25 §八）已無此阻塞。

