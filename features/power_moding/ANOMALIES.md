# ANOMALIES — FW036 Power Moding HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PMHnn]`（R-PMH3(b) —— 本 feature 之異常前綴為 `A-PMH`，
不與 `features/power` 之 `A-PW` 共用序號）。PENDING entries block their batch
until a Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

## A-PMH01 — 037 `FROP` 相異值：分析層 13、執行層實測 12 · **RESOLVED**（02 包 §1.1）

**登記日**：2026-08-22（下放包 01 步驟 4）

**現象**：handoff §3.1 之 `FROP 相異值` 記為 **13**；執行層對
`features/power_moding/inputs/` 之複本（SHA256 `e896a32a…02e8cf9a`）獨立
重算得 **12**。

**證據與歸因**（已查明，非資料差異）：

| 量測口徑 | 結果 |
|---|---|
| 全 56 資料列（r8–r63）取 `set()`，**未排除空值** | 13（其一為 `None`，來自 8 個 Heading 列之空 `FROP` 欄） |
| 全 56 資料列取 `set()`，排除空值 | 12 |
| 48 個 `Functional Requirement` 列取 `set()`（未 strip） | 12 |
| 48 個 `Functional Requirement` 列取 `set()`（strip 後） | 12 |

即：`13 = 12 個實質 FROP 標籤 + 空值一類`。分析層 §3.1 所列之 FROP 分布
明細本身即為 **12 項**（Customizable 12 / Disclaimer screen 7 / Audio 7 /
Power Management 5 / Steering Wheel Controls 5 / Bluetooth 3 / FOTA 2 /
Rear View Camera 2 / Climate Control 2 / WiFi 1 / EV/PHEV 1 / e-call 1，
合計 48，餘數 0），與執行層實測**逐項逐數完全相符**。故此為分析層
§3.1 表格之量測口徑瑕疵（空值計入相異值），其分布明細無誤。

**影響**：R-PMH6 之「FROP 欄之 13 個相異值得作為 Layer 2 之候選輸入之一」
—— 該條文之數字須為 **12**。條文之實質（FROP 為 Layer 2 候選輸入、與規格
目次取交集後再判 granularity）不受影響。

**裁定（02 包 §1.1，分析層自裁，不上呈）**：採認執行層之更正，`FROP` 相異值
為 **12**；亦採認執行層所擬之口徑定義（見下方 (c)）。R-PMH6 原文不改字，
以勘誤附註承接（比照 R-P36）。**狀態 → RESOLVED。**

原提案處置（已獲採認）：
(a) R-PMH6 之「13 個相異值」更正為「12 個相異值」，以勘誤形式附註於
    `RULINGS.md` 之 R-PMH6 條後，**原條文不改字**（R19-2）；
(b) 往後凡引用 FROP 相異值一律以 12 為準；
(c) 量測口徑寫入本檔備查：`FROP` 相異值之定義為「`Categorization ==
    Functional Requirement` 之列，`FROP` 欄非空值之相異數」。

---

## A-PMH02 — scaffold 產生之 marker 前綴為 `A-PO`，與 R-PMH3(b) 不合 · RESOLVED

**登記日**：2026-08-22（下放包 01 步驟 1）

**現象**：`scripts/new_feature.py` 以 `feature[:2].upper()` 產生 marker
縮寫。本 feature 因 whitespace 檢查（A-TM04）須以 `Power_Moding` 為參數
scaffold，得 abbr `PO`，故 `ANOMALIES.md` 與 `PLAYBOOK.md` 之範例 marker
落為 `[A-POnn]`。

**處置**：已於本包就地改為 `[A-PMHnn]`（R-PMH3(b)）。腳本本身**未改**
（下放包 §四步驟 1：「不自行改腳本」）。此為 scaffold 之通則性瑕疵，非
本 feature 專屬 —— `time_management`（abbr `TI`／實用 `TM`）、
`vehicle_setting`（abbr `VE`／實用 `VS`）皆同型，供 canon 回饋參考。

---

## A-PMH03 — SYS1 匯出相對 PDF 之內文偏離（重排／重排式再流） · PENDING

**登記日**：2026-08-22（下放包 01 步驟 7）

**方法**：`pdftotext -layout` 之全文正規化（空白摺疊）為 15,167 字；SYS1
`Basic Report` 之 52 則 `Description` 各自去除 `_x000D_` 字面量後正規化，
逐則以「是否為 PDF 全文之子字串」判定，未命中者再以
`difflib.SequenceMatcher(autojunk=False)` 求共同片段覆蓋率。
**分子定義（R-G8）**：分母為「排除 6 則圖片佔位與 3 則長度 <15 字之標題後，
可比對之 43 則」；分子為「正規化後為 PDF 全文子字串之則數」。

**結果**：43 則中 **39 則逐字命中**、4 則未命中。四則之逐項歸因：

| outline | export 字數 | 共同片段覆蓋 | 歸因 |
|---|---|---|---|
| 7.1 | 777 | **777（100%），惟切成 2 段** | **重排** —— 內容未失，語句順序與 PDF 不同（PDF：「…presented (3 sec), **after the animation (3 sec) a splash screen is presented timeout (1.5 each).** If ignition remains off…」；export 將該子句移至後段並改寫為「splash screen(s) are presented (1.5 sec timeout each)」） |
| 9.1 | 1,265 | 1,145（91%） | 條列項於 PDF `-layout` 下被切成多欄，6 個 export 獨有片段皆為條列再流之產物（`'1. FOTA update available'`、`'Charge Now (if applicable).'` 等），非漏句 |
| 11.1 | 371 | 313（84%） | 同上；export 獨有者為 `- Screen ON and Audio OFF, - Screen Off, and Audio ON,` 四個條列項 |
| 8 | 17 | 0 | export 之標題為 `Starup R1Low Only`（缺 `t`）；PDF 為 `Startup R1Low Only`。**export 側之拼字錯誤** |

**與 canon §3 「Mode A blind spot」之關係**：canon 所述之 Home 型漏句
（export 靜默丟句、item-code diff 看不見）**於本 feature 未觀察到** ——
逐則覆蓋率最低者為 84%，且其缺口全為 `-layout` 之條列再流。本 feature 所見
之偏離為**重排**（7.1）與**拼字**（8），非漏句。此為正向紀錄，不誇大。

**提案處置**（不裁定）：
(a) 依 §9.1 通則 3 指定 `spec_pdf` 為判讀基準（內文面）、`sys1_export` 為
    追溯用（結構面，`{outline}` 之唯一來源）；已寫入 `feature.yaml`
    `spec_baseline`，其 `known_exceptions` 逐條載明本異常；
(b) 依通則 7「增欄，不取代」二者並存 —— PDF 之 `-layout` 誤切為已知之
    「誤切之來源」，export 之圖片佔位為已知之「少內容之來源」，任一方
    皆不得整份取代對方；
(c) 凡引用 7.1 之流程順序者，於 Phase 4 逐 leaf 以 PDF 複核（本 feature
    有 5 個 leaf 引 `_7.1`，為單一章節之最大宗）。

**02 包 §1.2 核可上列 (a)(b)(c)，並將 outline 7.1 之重排列為 Phase 4 之
指名複核項**；理由為被移位改寫之子句正是動畫／splash 之時序（3 sec／
1.5 each），而時序誤讀在 Power Management 出過一次（`006`，A-PW68，
歷經兩輪修正與多次 lint 全綠而未被察覺）。

**複核時點**：Phase 4（資料建置）之 leaf 級處理，對 `outline == "7.1"` 之
5 個 leaf 逐一以 `spec_pdf` p8 之原文複核語句順序。其 `pdf_page` 已由
`data/outline_map.json` 定出（5 筆全為 p8）。**狀態維持 PENDING 至該複核完成。**

---

## A-PMH04 — SYS1 匯出之 6 則 outline 為圖片佔位，內容僅存於 PDF 流程圖 · PENDING

**登記日**：2026-08-22（下放包 01 步驟 7）

**現象**：`Basic Report` 之 outline `2.1` / `3.1` / `4.1` / `5.1` / `6.1` /
`12.4` 六則，其 `Description` 全文為
`Please refer to the diagram_x000D_ (image: %E5%9C%96%E7%89%87_<n>.png)`，
無任何規格文字。對應 PDF p3–p7 之五張啟動流程圖
（Headunit Startup — Non-GDPR/NonMaserati、GDPR/Non-Maserati、
Maserati/Non-GDPR、GDPR/Maserati，及 Passenger Screen Startup）。

**影響範圍（已量測）**：此六則**不在** 037 所引用之 29 個章節內
（037 引 29 章節，於 export 命中 29/29，其中無此六者）。故**不阻斷**
本輪之 48 leaf。惟：
- 該五張流程圖為「開機至 Disclaimer screen」之狀態機全圖，是 §7.x 各
  leaf 之判讀背景；
- 依 canon §3「Images are always rendered for figure/table pages
  regardless of mode」，圖頁須另行 render，不以文字層代替。

**提案處置**（不裁定）：
(a) 登記為 Phase 4 之圖像 render 目標（PDF p3–p7，另 p11 Off Road+ 亦為
    純流程圖），render 產物入 `data/`，不入 `inputs/`；
(b) 不因其為圖片佔位而判 export「不可讀」—— 依 §9.1 通則 6，已跨 xlsx／
    PDF 兩形式試過，PDF 側可讀，故此為**分工**而非缺陷；
(c) 若 Phase 3 之 Layer 2 目次需用到 2.1–6.1，其標題取自 PDF 頁首
    （`Headunit Startup – …` 等），來源標註為 `spec_pdf p{n}`。

**02 包 §1.2 核可「不判 export 不可讀」**，並要求先補齊圖像形式之抽取
能力實測（§9.1 通則 6）—— 已於 02 包步驟 8 完成，判定為**可 render 且可辨讀**
（150 DPI 足供向量流程圖，300 DPI 方能辨讀內嵌 UI 截圖之內文）。

**複核時點**：Phase 4，於實際 render 並取用 p3–p7／p11 之圖內容時。
02 包步驟 10 另有一項互相印證之結果 —— 48 leaf 之 `pdf_page` **無一落在
p3–p7**，故本異常於本輪確定不阻斷任何 leaf。**狀態維持 PENDING。**

---

## A-PMH05 — 雜湊檔本身未入版控，與 §9.1 通則 9 衝突 · **RESOLVED**（R-PMH11）

**登記日**：2026-08-22（下放包 01 步驟 3／9）

**現象**：`scripts/new_feature.py` 之 `GITIGNORE` 以 `inputs/` **整夾**排除。
本包依 R-PMH4／通則 9 產生之 `inputs/MANIFEST.sha256` 因而一併被忽略。
實測（唯讀）：

```
$ git check-ignore -v inputs/MANIFEST.sha256
features/power_moding/.gitignore:2:inputs/	inputs/MANIFEST.sha256
```

§9.1 通則 9 逐字為：「**保住檔案與保住雜湊是兩件事。** 歸檔之檔案須有可執行之
`shasum -c`，且**該雜湊檔本身須入版控**」。二者直接衝突。

**非本 feature 專屬** —— 同一份 `GITIGNORE` 由 scaffold 寫給每一個 feature。

**裁定（R-PMH11）**：`inputs/MANIFEST.sha256` 須入版控，素材四份維持不入版控。
**已於 02 包步驟 2 實施並雙向實測通過**（詳見 A-PMH06 —— 條文所指定之寫法
無效，實際採用之寫法不同）。`scripts/new_feature.py` 之 `GITIGNORE` 樣板
未改（R-PMH11 明載其屬 canon 層，本條不及之）。**狀態 → RESOLVED。**

原提案處置：
(a) 於 feature 之 `.gitignore` 加否定規則 `!inputs/MANIFEST.sha256`；或
(b) 雜湊檔改置於 feature 根之 `BASELINE.sha256`（`user_profiles` 之
    `feature.yaml` 註解出現過 `BASELINE.sha256` 一詞，其實際落點與是否
    tracked **本輪未查核**，不以未查核之前例充當依據）；
(c) 擇一後回饋 `scripts/new_feature.py` 之 `GITIGNORE` 常數，使新 feature
    不再重蹈。腳本本身本包未改（下放包 §四步驟 1）。

**附帶實測**：`sandbox/` **不在** `.gitignore` 內（`git check-ignore` 對
`sandbox/spec.txt` 無命中）。本包之 commit pathspec 逐項寫全名，故該檔不會
被提交；但依賴 pathspec 而非 `.gitignore` 是較弱之保護。併入本條之提案 (c)：
`GITIGNORE` 常數宜同時加入 `sandbox/`。

---

## A-PMH06 — R-PMH11 所指定之 `.gitignore` 寫法無效（git 不遞迴進入已排除目錄） · **RESOLVED**（R-PMH15／R-PMH17）· 附 **PENDING-CANON**

**登記日**：2026-08-23（02 包步驟 2）

**現象**：R-PMH11 逐字指定之實施方式為

> 於 `features/power_moding/.gitignore` 之 `inputs/` 排除規則後增列否定規則
> `!inputs/MANIFEST.sha256`，並以 `git check-ignore -v` 對該路徑實測其不再被忽略

照此實施後，**實測仍被忽略**：

```
$ git check-ignore -v features/power_moding/inputs/MANIFEST.sha256
features/power_moding/.gitignore:2:inputs/	features/power_moding/inputs/MANIFEST.sha256
```

**成因**：git 之既有行為 —— 一個目錄被排除後，git **不再遞迴進入該目錄**，
故其內任何否定規則都不會被求值。`inputs/` 排除的是「目錄」，
`inputs/*` 排除的才是「目錄內容」，後者才留得住其後之否定規則。
**R-PMH11 之目的可達成，其所述之方法不可行。**

**執行層之處置（已實施，須追認）**：改寫為

```
inputs/*
!inputs/MANIFEST.sha256
```

雙向實測（R-G7-1 之對照向）：

| 向 | 對象 | 結果 |
|---|---|---|
| 正向 | `inputs/MANIFEST.sha256` | 命中 `.gitignore:7:!inputs/MANIFEST.sha256` → **不再被忽略** |
| 反向 | 四份素材（3 xlsx + 1 pdf） | 全數命中 `.gitignore:6:inputs/*` → **仍被忽略** |
| 反向 | `features/power/inputs` | 命中其自身 `.gitignore:2:inputs/` → **未受影響** |
| 實效 | `git add --dry-run -- inputs/`（唯讀） | 僅輸出 `add 'features/power_moding/inputs/MANIFEST.sha256'` 一筆 |

**裁定**：R-PMH15（03 包）將上列等效寫法立為條文；**R-PMH17（03a）由 Pei 於
2026-08-23 追認**。R-PMH11 之目的未變，其所指定之無效寫法由 R-PMH15 取代，
原文不改字（附註已置於 `RULINGS.md` R-PMH11 條後）。**狀態 → RESOLVED。**

### canon 層成因未解 · **PENDING-CANON**

`scripts/new_feature.py` 之 `GITIGNORE` 常數對每個 feature 都寫 `inputs/`
（目錄形態）。**任何新 feature 照樣板產出之 `.gitignore`，其雜湊檔都會被忽略。**

Pei 之「A-PMH06 追認」（R-PMH17）就其字面**只及於本 feature 之 `.gitignore`
寫法，未及於樣板**。故：

- 本項標 **PENDING-CANON**，`scripts/new_feature.py` **本 feature 不改**；
- 執行層不得順手改之（03a §四明載）；
- 待 Pei 決定是否另開 canon 層工作包。

> 記此一項之理由（03a §四逐字）：「A-PMH06 在本 feature 已 RESOLVED，
> 若不另立 PENDING-CANON，下一個 feature 會再踩一次而沒有任何紀錄指向它。
> 這正是 G-D 之精神（「不做」與「沒發現」必須在紙上分得開）。」

---

## A-PMH07 — R-PMH2 所引之 Comfort R-C6 前例，於實際交付件上未實現 · **RESOLVED**（R-PMH13）· 交叉指引 `features/comfort/ANOMALIES.md` A-CF-EXT-02

**登記日**：2026-08-23（02 包步驟 9，Q7 語料實測之副產物）

**R-PMH2 之依據**逐字為：「依據：Comfort R-C6 之同型處置（交付夾
`Climate Control Interface`，`test_group` 為 `Comfort`）。」

**R-C6 之原文**（`features/comfort/RULINGS.md:128`）逐字為：

> `R-C6  Test Group`
> `workbook Test Group 欄一律填 "Comfort"。`
> …「客戶交付路徑中之 "Climate Control Interface" 為資料夾分類，非 spec 標題，
> 不作為 Test Group 來源。」

**實測**（唯讀，未寫入）：客戶交付夾之
`…_SWQT_Comfort_20260817.xlsx`，分頁 `Test Case Specification 測試用例規範`，
`G` 欄（Test Group）r10 起 **466 列，相異值只有一個：`Climate Control Interface`**。

即：**已交付給客戶之工作簿，其 Test Group 欄填的是交付夾名，
不是 R-C6 所裁定的 `Comfort`。**

**兩種可能之解讀**（執行層不判定）：
(a) R-C6 立於 2026-08-14，而交付件出於 2026-08-17 —— 條文未被落實，
    或落實後被回改；
(b) `feature.yaml` 之 `test_group` 本即註明「framework-internal;
    workbook write per profile」，即**宣告值與寫回值本就分離**，
    R-C6 管的是前者，交付件呈現的是後者。若為此解，則 R-C6 之
    「workbook Test Group 欄一律填」一語與該分離不一致。

**對本 feature 之影響**：R-PMH2 裁定 `test_group` 為 `Power Moding` 且
「交付夾名 `Disclaimer screen` 不進入 `test_group`、不進入任何 TC 欄位」。
若依 Comfort **交付件**之實況類推，G 欄應填 `Disclaimer screen` ——
**與 R-PMH2 相反**。

**不阻斷本輪**：R-PMH6 已將 G/H 兩欄之最終值延後至 Phase 3。
**但須在 Phase 3 開始前裁定**，否則 Layer 1 之定版會建立在一個
未經核對的前例上。

**裁定（03 包 R-PMH13，Pei 2026-08-23 核可）**：分析層獨立複驗四份交付件，
**4/4 皆為交付夾名，無一例外**。G 欄一律填交付夾名 `Disclaimer screen`；
**R-PMH2 之後半撤回**，其前半（`feature`／`slug`）維持有效。
A-PMH07 → **本 feature 側已處置**（狀態隨 R-PMH13 生效）。

**連帶回報已發出**：`features/comfort/ANOMALIES.md` 之
**`A-CF-EXT-02`**（比照 A-CF-EXT-01 之形態）—— 只記 R-C6 條文與其交付件
466/466 之不一致與其證據，**不判定成因、不提案修改 Comfort 之條文、
未修改 Comfort 之任何交付物**。三種可能成因於該則內並列。

---

## A-PMH08 — outline→PDF 頁次之定位：兩種先驗方法皆產生錯誤或未解 · RESOLVED（方法已更換並驗證）

**登記日**：2026-08-23（02 包步驟 10）

本條記錄 `data/outline_map.json` 之 `pdf_page` 欄在定案前被否決的兩種方法，
以免日後重蹈。**兩次失敗都不是靜默的** —— fail-loud 各自攔下。

| # | 方法 | 結果 | 否決理由 |
|---|---|---|---|
| 1 | 章 `Description` **逐字等於** PDF 頁首 | 48 leaf 中 **21 未解** | SYS1 之 ch 8／10／11 是**頁內小標**而非頁首（`Starup R1Low Only`、`Additional Power Moding Behavior Notes:`、`VR HARD KEY FOR SIRI/…`），PDF 頁首只有 11 個而 SYS1 有 12 章 |
| 2 | 章 `Description` **子字串包含**於頁文字 | 48 leaf **全解，但其中有錯** | 短通用詞誤命中：ch 7 `Startup` 命中 p3（頁首 `Headunit Startup – Non-GDPR/NonMaserati`）而實為 p8；ch 9 `Power Moding` 命中 p1（`R1 ‐ Power Moding HMI Logic and Flow`）而實為 p9。**assert 通過但資料是錯的** —— 此即 G103 前例之形狀 |

**定案之方法**：以**該節自身** `Description`（去 `_x000D_`、空白正規化）之
首 N 字於各頁文字中求命中，**要求唯一命中**；N 依 `80 → 60 → 40` 遞減，
取首個唯一命中者；命中 >1 頁即判未解，**不取首個**。

為何需要階梯：`pdftotext -layout` 在多欄頁會於句中插入斷點。outline `9.1`
之 80 字探針命中 0 頁、60 字探針唯一命中 p9 —— 固定長度探針會把它判成未解。

**結果**：48/48 全解，0 未解。探針長度分布 80 字 39 筆／60 字 7 筆／40 字 2 筆。
反推之章↔頁對照自洽：ch7→p8、ch8→p8、ch9→p9、ch10→p10、ch11→p10、ch12→p11。

**盲區聲明（R-G11）**：探針縮至 40 字時，理論上可能在別頁產生偶然唯一命中。
使用 40 字探針之 2 筆已逐筆記於 JSON 之 `probe_len`，可人工複核。
**未以「多數命中」通過任何一筆**（R-G7-1）。

**附帶結果**：48 leaf 全部落在 **p8–p11**（文字頁），**無一落在 p3–p7 之
流程圖頁** —— 與 A-PMH04「6 則圖片佔位 outline 不在 037 引用之 29 章節內」
互相印證，兩者由不同路徑得出。

---

## A-PMH09 — 客戶那份 036 之 `ChangeHistory` 第 C 版列為 **AMFM feature 之寫回註記** · PENDING

**登記日**：2026-08-23（03 包步驟 8，清償 02 §11 第 3 項時發現）

**現象**：客戶交付夾之 `…_SWQT_PowerModingHMI_20260819.xlsx`，
分頁 `ChangeHistory 修訂履歷` 之 `r7`（版本 `C`）逐字為：

```
Added 143 test cases covering the 102 leaves of FM-WI-FSM-037-A03, appended from row 168.
The 158 existing rows are unchanged — verified by an ordered content hash over columns D..AG, not by row position.
Corrected the header 範圍 Scope field (D5), which named the superseded requirement report: FM-WI-SW-RAD-SWRA-A02 -> SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323.
```

修訂人 `PeiPYHsu`，日期 `2026-08-10`。

**這是 AMFM feature 之寫回註記**，證據三項：
1. 字串內含 **`SWE1_AMFM`**；
2. 數字 **143 test cases / 102 leaves / 自 r168 append / 既有 158 列** ——
   本 feature 為 **48 leaf、0 test case、資料列 r10–57**，無一相符；
3. 其所述之 `ordered content hash over columns D..AG` 為本管線
   `PARTIAL_INTERLEAVED` 之 done invariant 作法（canon §2）。

**母本之同一格**（`forms/…_20260817_ext.xlsx` r7 ver `C`）逐字為
「新增欄位：預估測試時間(分鐘) / Add new column: Estimated Test Time (mins)」，
修訂人 `張愷霏 ErinKFChang`，日期 `2026-01-21`。

即：**客戶那份把表單自身之 rev C 修訂履歷覆寫成某一 feature 之交付註記**，
表單之版本沿革在該檔中已遺失。

**推論（證據支持，非臆測）**：客戶那份之 036 係自 **AMFM 之已交付工作簿**
衍生而來（沿用其檔案、清掉其資料列、填入本 feature 之 48 列）。此可解釋
01／02 包所測之三項離群：

| 離群現象 | 本推論之解釋 |
|---|---|
| 35 欄（A–AI）、`Estimated Test Time` 兩次 | 承自 AMFM 那份之版面，非 rev C 母本 |
| `Cover 封面!D6` 版本為 **`A`**，而母本為 `C` | 封面版本未隨 ChangeHistory 之 A/B/C 三列更新，**檔案自相矛盾** |
| 合併範圍多出 `D5:F5` | 承自該註記所稱「Corrected the header 範圍 Scope field (D5)」之操作 |

**另一項自相矛盾**：該註記聲稱已修正 `D5` 範圍欄使其指向
`SWE1_AMFM_FM-WI-FSM-037-A03 …`，然 01 包實測客戶那份之 **`D5` 為空白**。
即**註記所述之修改在檔案中不存在**（或事後被清除）。

**影響**：**零** —— R-PMH7 已將交付基底改為 forms 母本，客戶那份僅供
leaf 對應查核與附屬分頁取得。本則為**回溯性佐證**：R-PMH7 之判準
（34 欄、`Estimated Test Time` 恰一次）所排除的，確實是一份帶著他 feature
血緣與自相矛盾中繼資料的檔案。**若 02 包沿用了它，Phase 7 交付時
會把 AMFM 之修訂履歷一併交給客戶。**

**提案處置**（不裁定）：
(a) 本則登記為 R-PMH7 之事後佐證，不改任何條文；
(b) `feature.yaml` 之 `customer_source_copy` 註解增列「其 `Cover`／
    `ChangeHistory`／`Product Document` 三頁帶他 feature 血緣，**不得取用**」
    —— R-PMH7 原已限定用途為二項（leaf 對應、附屬三頁），本項使該限定
    更緊：**附屬三頁指 `Reference`／`QS Suggestion`／`Test Case Framework`，
    不含封面三頁**；
(c) 建議回報 AMFM feature：其交付件之 ChangeHistory 覆寫了表單自身之
    rev C 沿革。**惟本 feature 未查 AMFM 之交付件本身**（只看到這份衍生物），
    故不逕行回報，先請分析層判斷是否值得一查。

---

## A-PMH10 — `組合測試` 之字串在三處不一致，`下拉選單` 與表單自身之修訂履歷相左 · PENDING

**登記日**：2026-08-23（03 包步驟 8，清償 02 §11 第 6 項）

02 包 §11 第 6 項自陳「執行層之判斷可能過輕」，本包補齊證據後正式登記。

**三處實測**（母本與客戶那份**兩檔皆同**，故非任一交付件之瑕疵）：

| 出處 | 字串 |
|---|---|
| `下拉選單!A6`（**x14 DV 之 source**） | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` |
| `Reference!C9`（說明頁） | `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)` |
| **`ChangeHistory!B5` 版本 A 之第 5.g 項**（表單自身之修訂履歷） | `組合測試（Pair-wise／N-wise） — Combinatorial (Pair-wise / N-wise)` |

即：**表單之修訂履歷明載此項應為 `Pair-wise / N-wise`，`Reference` 頁與之
相符，而實際生效之下拉選單為 `Pairwise / t-wise`。** 三處中兩處一致，
不一致的那一處恰是 Excel 真正會驗的那一處。

**lint 之權威仍取 `下拉選單`** —— 它是 x14 DV 之 source 範圍，寫入其他
字串會被 Excel 擋下。`feature.yaml` 之 `design_method_vocabulary` 9 項
已取自該處，維持不變。

**不阻斷**：四份已交付件之 R 欄逸出檢查為 **0**（996 個非空值全部落在
`下拉選單` 之 9 項內），故實務上此不一致未造成任何問題。

**提案處置**（不裁定）：
(a) 維持 `下拉選單` 為 lint 權威，不改 `feature.yaml`；
(b) 登記為**表單層之瑕疵**，非任一 feature 之瑕疵 —— 母本與客戶那份皆同；
(c) 是否回報表單維護者（張愷霏／劉安哲），屬 Pei 之判斷，本 feature 不逕行。

---

## 開案時之介面實測記錄（非異常，供追溯）

`scripts/new_feature.py` 之實際介面與本 slug 之相合情形：

- 參數為 feature **名稱**，目錄取 `feature.lower()`；名稱含空白即 `sys.exit`
  拒絕（A-TM04 之防護）。
- 故 `Power Moding` 不可直接傳入；以 `Power_Moding` 傳入得目錄
  `features/power_moding/`（= R-PMH2 之 slug），`feature.yaml` 之 `feature:`
  欄再依 R-PMH2 修為 `Power Moding`。
- **前例**：`time_management/feature.yaml` 之標頭仍為
  `# feature.yaml — pipeline configuration for Time_Management` 而
  `feature: "Time Management"`，即同一手法。本 feature 照此辦理，未立新慣例。
- `--adopt-existing` 旗標之語意為「填補缺檔，永不覆寫既有檔」；已用之，
  `docs/handoff/01_intake.md` 之 SHA256 於 scaffold 前後同為
  `0f11160c…0b914838`，未被覆寫（停止條件 7 未觸發）。
- scaffold 之 `DIRS` 不含 `sandbox/`，`docs/` 下亦不建 `upstream/`；
  二者已由本包手動補建。

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PMHnn]`.
