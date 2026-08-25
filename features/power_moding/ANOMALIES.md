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

## A-PMH03 — SYS1 匯出相對 PDF 之內文偏離 · **PENDING**（**13 包再度改判 —— 見 A-PMH14**）

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

### ⚠ **結論更正（12 包步驟 5 之指名複核）—— 7.1 是漏句，不是重排**

01 包原記：「canon 所述之 Home 型漏句…**於本 feature 未觀察到** ——
本 feature 所見之偏離為**重排**（7.1）與**拼字**（8），非漏句。」
**該結論不成立。**

**成因（量測方法之限制）**：01 包之判定以「SYS1 該則描述是否為 PDF **全文**
之子字串」為之，未命中者再求共同片段覆蓋率。7.1 得「777 字 100% 覆蓋、
切成 2 段」，遂記為重排。**該量測看不見「PDF 有而 SYS1 無」之內容** ——
它只驗 SYS1 之字有沒有出現在 PDF，不驗 PDF 之字有沒有出現在 SYS1。

**12 包之逐句對照（SYS1 8 句 vs PDF 9 句）**：

| # | 對照 |
|---|---|
| 1 | **≠ 差異段** |
| | SYS1：`SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off after animation, screen is black.` |
| | PDF ：`SU1.) … presented (3 sec), `**`after the animation (3 sec) a splash screen is presented timeout (1.5 each).`** |
| | PDF ：`If ignition remains off after animation, screen is black.` |
| 2–8 | ＝ 逐句相同 |

**被漏之子句於 SYS1 全 52 則描述中完全不存在**（實測）：

| 檢索 | SYS1 全簿 |
|---|---|
| `after the animation (3 sec) a splash screen is presented timeout (1.5 each)` | **不存在** |
| `after the animation` | **不存在** |
| `splash screen is presented` | **不存在** |
| `1.5 each` | **不存在** |

**不是同義改寫，是整句消失。** SYS1 保留了另一句
`If ignition is turned on during animation, splash screen(s) are presented (1.5 sec timeout each).`
—— 其為**有條件**（點火於動畫期間開啟），而被漏者為**無條件**
（動畫結束後即呈現 splash）。**二者非同一敘述。**

**故：canon §3 之 Home 型 Mode A blind spot（export 靜默丟句）
在本 feature 確實發生，且落在 7.1。**

**其嚴重性**：被漏者為**時序子句**（動畫 3 sec → splash 1.5 each）——
正是 A-PW68（Power Management `006` 時序誤讀，歷經兩輪修正與多次 lint
全綠而未被察覺）之同一形態。**若以 SYS1 為判讀基準撰寫 7.1 之 TC，
該時序無從得知。**

**R-PMH50 因而得到直接佐證**：`source_clause` 取自 PDF 而非 SYS1
之規定，在本 feature 之第一批即被用上 —— batch 1 之 4 條 7.1 系 TC
其 `source_clause` 皆含該子句。

**原記之其餘三則（8 之拼字、9.1／11.1 之條列再流）不變。**
**缺口數仍為 4**（同一位置，性質更正），停止條件 9（新的偏離）未觸發。

---

**原文保留（01 包所記，供追溯）**：

> **與 canon §3 「Mode A blind spot」之關係**：canon 所述之 Home 型漏句
> （export 靜默丟句、item-code diff 看不見）**於本 feature 未觀察到** ——
> 逐則覆蓋率最低者為 84%，且其缺口全為 `-layout` 之條列再流。本 feature 所見
> 之偏離為**重排**（7.1）與**拼字**（8），非漏句。此為正向紀錄，不誇大。

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

## A-PMH09 — 客戶那份 036 之 `ChangeHistory` 第 C 版列為 **AMFM feature 之中繼寫回註記** · **RESOLVED**（R-PMH23）

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

### 結論更正（04 包 §2.3，分析層實測 AMFM 交付件後）

執行層原推論「客戶那份**衍生自 AMFM 交付件**」**不成立**。分析層對
`ASW-R2/AM:FM/…_SWQT_AMFM_20260810.xlsx` 唯讀實測：

| 項 | AMFM **交付件** | 客戶那份 |
|---|---|---|
| 欄數 | **34（rev C）** | 35 |
| `Cover!D6` 版本 | **`C`** | `A` |
| `ChangeHistory` ver C | **表單原文**（「新增欄位：預估測試時間(分鐘)」） | 被覆寫為寫回註記 |
| `D5` 範圍 Scope | **已填**（`SWE1_AMFM_FM-WI-FSM-037-A03 …_20260323`） | **空白** |
| 資料列 | 298 | 48 |

**AMFM 之交付件乾淨**：34 欄、履歷未被覆寫、`D5` 已填。二者不是同一份之複本。

**成立者**：客戶那份帶 AMFM 之**中繼產物**血緣 —— 某個寫回註記已寫入、
但該中繼態未進入交付；其後被清空內容並貼入 48 列 037 資料。
三項證據仍然成立，只是其來源指向**中繼態**而非交付態。

**故無須回報 AMFM feature**（其交付件無缺陷可報）。執行層原提案 (c) **不執行**。

**裁定（R-PMH23）**：客戶那份之 `Cover 封面`／`ChangeHistory 修訂履歷`／
`Product Document 記錄封面頁`／`Cover_old`／`ChangeHistory_old` **五頁一律
不得取用**；R-PMH7 所稱之「附屬分頁」明確限定為 `Reference`／
`QS Suggestion`／`Test Case Framework` 三頁。**狀態 → RESOLVED。**

---

原提案處置：
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

## A-PMH10 — `組合測試` 之字串不一致 · **證據更正（04 包步驟 5）** · PENDING

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

### 證據更正（04 包步驟 5 —— 全簿 DV 複掃後）

03 包稱「母本與客戶那份**兩檔皆同**，故為表單層瑕疵」。**該陳述不正確。**
全簿 DV 複掃揭出：**二檔之 x14 DV 指向不同的 source 範圍。**

| 檔 | x14 DV `xm:sqref` | **`xm:f`（source）** | 第 6 項之值 |
|---|---|---|---|
| **母本 20260817_ext** | `R10:R1411` | **`下拉選單!$A$1:$A$9`** | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` |
| **客戶 20260819** | `S10:S221` | **`Reference!$C$4:$C$12`** | `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)` |

`Reference!C4:C12` 與 `下拉選單!A1:A9` 之九項中**八項逐字相同，僅第 6 項不同**
（實測 `==` 比對）。

**即：兩檔之 design_method 詞彙表在該項上實際生效值不同** —— 不是「同一份
表單有兩處寫法」，而是**兩個檔各自指向不同的來源分頁**。

**另一項**：客戶那份之 `下拉選單` 分頁存在，且其 A1:A9 與母本逐項相同
（03 包所測屬實），**但它不是該檔之 DV source** —— 是**孤兒分頁**。
03 包之「兩檔皆同」正是被這個孤兒分頁誤導。

**表單自身之修訂履歷（`ChangeHistory` ver A 第 5.g 項）作
`Pair-wise / N-wise`**，與 `Reference` 一致而與 `下拉選單` 相異 ——
此點 03 包所記正確，且現在更清楚：**`下拉選單` 是後來被改過的那一份**。

### 對本 feature 之效力

**lint 權威為母本之 `下拉選單!$A$1:$A$9`** —— R-PMH7 已定母本為交付基底，
其 x14 DV 指向該處，寫入其他字串會被 Excel 擋下。
`feature.yaml` 之 `design_method_vocabulary` 9 項取自該處，**維持不變**。

**不阻斷**：03 包之逸出檢查為 **0**（四份交付件之 996 個 R 欄值全部落在
母本 `下拉選單` 之 9 項內）—— 即**無任何交付件用過 `Pair-wise / N-wise`
那個字串**，故此差異在實務上未造成逸出。

**提案處置**（不裁定）：
(a) 維持母本 `下拉選單` 為 lint 權威，不改 `feature.yaml`；
(b) 本則**不再宣稱為「兩檔皆同之表單層瑕疵」** —— 實為兩檔之 DV source
    不同所致；是否回報表單維護者（張愷霏／劉安哲）屬 Pei 之判斷；
(c) 教訓與 R-PMH20 同型：03 包只讀了兩檔之 `下拉選單` **分頁內容**便下
    「兩檔皆同」之結論，**未查該分頁是不是各該檔之 DV source**。
    比對兩個值之前，要先確認兩邊指的是不是同一個東西。

---

## A-PMH11 — 量詞與量測範圍不一致：分頁層量測寫成全簿結論 · **RESOLVED**（R-PMH20）

**登記日**：2026-08-23（04 包 §2.1，分析層獨立複驗時發現）

**現象**：03 包上繳 §2.2 末句逐字為

> 「**母本之 DV 總數 = 4 組**（legacy 3 ＋ x14 1），**除此之外無其他 DV**。」

該量測之範圍是**單一分頁**（`xl/worksheets/sheet6.xml`），而該句之量詞是
**整本活頁簿**。

**執行層獨立重掃全簿（04 包步驟 5，先算後比）**：

| 分頁 | 型別 | sqref | formula1 |
|---|---|---|---|
| **`Product Document 記錄封面頁`** | legacy | **`B7:C7`** | **`"Confidential, Top Secret"`** |
| `Test Case Specification 測試用例規範` | legacy | `P10:Q1411` | `"P0,P1,P2,P3"` |
| `Test Case Specification 測試用例規範` | legacy | `T10:Z1411` | `"0,1"` |
| `Test Case Specification 測試用例規範` | legacy | `AF10:AF1411` | `"Pass, Fail, Pending,Block,NA"` |
| `Test Case Specification 測試用例規範` | x14 | `R10:R1411` | `下拉選單!$A$1:$A$9` |

**全簿實測為 5 組（legacy 4 ＋ x14 1）**，與分析層之複驗相符。
遺漏之一組即 `Product Document!B7:C7`。

**不是量錯，是量詞與量測範圍不一致**。分頁層之數字（4 組）本身正確。

**裁定（R-PMH20）**：任何帶全稱量詞之陳述，其量測範圍必須等同該量詞所
涵蓋之範圍；若量測範圍較小，二者擇一修正，**不得以「實務上不會有別的」
為由保留較大之量詞**。

**落實**：本上繳包 §5 之結論句改寫為分頁層陳述並另列全簿清單。
`Product Document!B7:C7` 之 DV 對本 feature 無影響（該分頁在母本為
「僅標籤、值全空」，且不在寫回範圍內），但**它在紙上了**。

**狀態 → RESOLVED**（成因為量詞用法，已由 R-PMH20 立條；證據已補齊）。

---

## A-PMH12 — `Q` 與 `AF` 兩欄之 DV 瑕疵，Phase 6／7 首次填值前必須處理 · PENDING

**登記日**：2026-08-23（04 包步驟 6，依 03 包上繳 §9 第 2 項）

母本之兩項 DV 瑕疵。二者皆因四份已交付件之該二欄**全空**而
**從未被實際檢驗過** —— 首次填值時才會浮現。

### (1) `Q`（Estimated Test Time (mins)）套用 `"P0,P1,P2,P3"` 下拉

母本之 priority DV 之 `sqref` 為 **`P10:Q1411`**，**跨 P、Q 兩欄**。
`Q` 欄之表頭為 `Estimated Test Time (mins)\n預估測試時間（分鐘）`，
其合法值應為分鐘數，卻套用 `P0/P1/P2/P3` 之清單。

**後果**：任何寫入 `Q` 之數值都會被 Excel 擋下。
`allowBlank=1` 故留白合法 —— 這正是它至今未被發現的原因。

### (2) `AF`（Test Result）之列舉字串含**前導空白**

`formula1` 逐字為 `"Pass, Fail, Pending,Block,NA"`，
以 `,` 切開後為：`Pass`／**` Fail`**／**` Pending`**／`Block`／`NA`
—— `Fail` 與 `Pending` 前各有一個空格，`Block` 與 `NA` 前沒有。

**後果**：寫入 `Fail`（無空格）會被擋下，必須寫 ` Fail`（有空格）。
任何對測試結果做 `.strip()` 的程式都會產生無法通過 DV 的值。

### 客戶那份之對應情形（供對照，非本 feature 之交付基底）

| 項 | 母本 | 客戶 20260819 |
|---|---|---|
| priority DV sqref | `P10:Q1411`（跨兩欄） | `Q10:Q221 R10:R11 P10:P11`（**三段破碎多範圍**） |
| test_result DV sqref | `AF10:AF1411`（1402 列） | **`AG10:AG13`（僅 4 列）** |

客戶那份之 test_result DV **只涵蓋 4 列**（r10–r13），其餘 44 列無 DV ——
另一項獨立瑕疵。**因 R-PMH7 已改用母本，此項對本 feature 無效力，僅登記。**

**本包不提解法**（下放包步驟 6 明載）。**已於 `DECISIONS.md` 標為
Phase 6／7 之前置阻斷項**：首次填 `Q` 或 `AF` 之前必須處理，
否則寫回會被 DV 擋下或產生逸出值。

---

## A-PMH13 — `SWE1-HMI-PM-028`（12.2）之行為定義在 CFTS009 · **RESOLVED（處置已定，R-PMH47）**

> **19 包更新（R-PMH72）**：Pei 2026-08-24 裁「DR-PMH1 拿掉」——
> `-028` **不寫入交付工作簿、不產出 TC、不以 `PENDING` 佔位**。
> R-PMH47 之 (b)（該列仍寫入並揭露）與 (c)（開 DR-PMH1）**撤回**；
> (a)（判為 out of scope）維持。`DR-PMH1` 標 `CLOSED-BY-RULING`。
> **本則之內部紀錄保留**（G-D：「不做」與「沒發現」須在紙上分得開）。
> 連帶：`Off Road Plus` 3 → **2** leaf；有 TC 之 leaf 48 → **47**。

**登記日**：2026-08-24（06 包 §六，查證見步驟 4）

**條文逐字**（SYS1 `Basic Report` outline `12.2` 之 `Description`）：

```
OFF2.)Please refer to CFTS009 for complete behavior.
```

該 leaf **本身不含任何可驗證之行為**，其行為定義在 **CFTS009** ——
而 CFTS009 正是已交付之 `features/power`（Power Management）之來源規格。

**惟該 leaf 確在本 feature 之 48 個 Functional Requirement 內**
（R-PMH1 之判準：`Categorization == Functional Requirement`），不能不涵蓋。
此為 canon §8.4.2（no scope fabrication）之典型情形。

### 查證（06 包步驟 4）—— **零命中**

**量測對象**：`ASW-R2/Power Management/…_PowerManagement_20260821.xlsx`
（R-PMH24 母體之 `Power Management` 交付件），分頁
`Test Case Specification&Result`，**唯讀開啟，未修改 `features/power` 之任何檔案**。

**實測 284 條 TC**（非 283 —— 見下方口徑註）。對其
`Test Case ID`／`Test Set`／`Test Item`／`Pre-Conditions`／`Test procedure`／
`Expected Result` 六欄之合併文字做大小寫不敏感之正規式搜尋：

| 標的（章 12 之三個 leaf） | 檢索式 | 命中 |
|---|---|---:|
| **12.2（`-028`）本身** | `OFF2` | **0** |
| 12.1（`-027`）：Off Road state 下按 Off Road+ 不喚醒 | `off[\s\-_]*road` | **0** |
| 同上 | `hard control` | **0** |
| 同上 | `Power Button On` | **0** |
| 同上 | `wake\s*up` | 1 → **經人工複核不相關**（`NR1L-PowerManagement-233`，其 Test Item 為「skip start-up animation…until the next CAN wakeup cycle」，屬 Startup Display，與 Off Road+ 無關） |
| 12.3（`-029`）：Power Off State 啟動 app 時靜音 | `Power Off State` | **0** |
| 同上 | `launch.*app` | **0** |
| 同上 | `\bmute` | 9 → **皆非本標的**（無一與「自 Power Off State 啟動 app」相關） |

**結論：`features/power` 之 284 條已交付 TC 中，`Off Road+` 之行為零命中。**

**佐證**：該 284 條之 `specification_reference` 相異前綴僅 **`CFTS009`／`CFTS010`**
二者，其 Test Set 為 `Power State`(148)／`Startup Display`(59)／
`Branding and Theme`(34)／`Timeout Settings`(26)／`Power Down`(16)
—— **無任何 Off Road 相關之 Test Set**。

**故 06 包 §六所設之前提「若已涵蓋，(ii) 成立且無缺口」不成立**：
未涵蓋，**這是一個真缺口**。

### 口徑註（R-G8）—— **已結案（07 包 §二）**

06 包 §六稱 283、執行層實測 284。**成因已由分析層之既有量測解明**
（03 包 §2 對同一檔之實測）：

| 口徑 | 值 |
|---|---|
| `D` 欄非空之**資料列數** | **284** |
| 其中具 `Test Group` 之列（＝ **TC 數**） | **283** |
| 留白列（`SWE-PM-089`，有 req id 無 TC） | **1** |

**兩個數字都對，量的是不同東西。** 本則之查證以「資料列」為分母
（284），其結論（零命中）不受此口徑影響 —— 留白列不含任何 TC 文字。
**未改動 `features/power` 之任何檔案。**

**本口徑註結案。** 〔**07 包當時之陳述**：本則之 PENDING 狀態僅繫於 `-028` 之處置。〕
**已於 12 包定案** —— R-PMH47 裁 (ii)＋(iii)，本則狀態為 **RESOLVED（處置已定）**，
其 (c) 項另立 `DR-PMH1`（`OPEN`）。

### 跨 feature 擴查（07 包步驟 2、08 包步驟 5）—— **零命中**

06 包之零命中僅限 `features/power` 之 284 列。07 包擴為全母體；
08 包再擴檢索欄位並依 **R-PMH34** 改寫分母。

#### 分母之三種口徑（R-PMH34(a)(b)）

| 口徑 | 交付件 | 資料列 | 說明 |
|---|---:|---:|---|
| 07 §3.3 原報 | 16 | 3,234 | **兩處灌水**，見下 |
| **(a) 排除無內容者** | **15** | 3,234 | `Vehicle Settings/VF230_V1_R5` 之資料列為 **0**（空白工作簿），**無從命中**，計入分母會使結論看起來比實際強 |
| **(a)+(b) 平手只計一份** | **15** | **3,023** | `Engineering Mode` 之兩候選（527 + 211）內容大量重疊，同時計入即重複計算；本表取 **527 列之 `_Rebuilt`**，另一候選為 **211 列**（若改取之則分母為 **2,707**） |

**採認之口徑：15 個有內容之交付件、3,023 資料列。**
零命中之結論在三種口徑下皆成立（各檔命中皆為 0）。

#### 檢索範圍與其盲區聲明（R-PMH34(c)）

| 輪次 | 檢索欄位 |
|---|---|
| 07 包 | `Test Case ID`／`Test Group`／`Test Item`／`Pre-Conditions`／`Test procedure`／`Expected Result`／`Specification Reference`（7 欄） |
| **08 包擴查** | **`Remarks`／`Test Case Design Methods`／`Test Case Reference ID`**（3 欄，依表頭文字定位，各檔欄位字母不同：`AH`/`AI`/`AG` 等） |

**仍未及之欄位（盲區，R-G11）**：`No.#`／`Requirement or Design ID (Polarion)`／
`Test Case ID (TestRail)`／`Test Set`／`Input Test Data`／`Estimated Test Time`／
`Functional Safety`／七個車型欄／`Test Version`～`Defect ID`。
**其中 `Test Set` 之未檢索為本則之最大盲區** —— 若某 feature 立了一個名為
`Off Road` 之 Test Set 而其 TC 文字未用該詞，本檢索看不到。
（惟 07 包已列出各檔之 Test Set 清單，人工檢視無 Off Road 相關者。）

#### 08 包擴查之結果 —— **`CFTS009` 於三個擴查欄位零命中**

| 標的 | 15 檔 × 3 欄之命中 | 複核 |
|---|---:|---|
| `OFF2` | 0 | — |
| `off road` | 0 | — |
| `Off Road+` | 0 | — |
| `Power Off State` | 0 | — |
| `launch` | 0 | — |
| **`CFTS009`** | **0** | **無任一 feature 在備註欄記載「此項由 CFTS009 涵蓋」** |
| `hard control` | 4 | 全在 `Climate Control Interface` 之 `Remarks`，逐字為 `[BLOCKED-SPEC] Owner: CFTS044 — the equivalence to the previous 4-way rocker hard control …` —— **屬 CFTS044，與本標的無關** |

**停止條件 9 未觸發。**

#### 結論句（R-PMH20 之量詞限定 ＋ R-PMH34 之分母口徑）

> **本次量測之 15 個有內容交付件（3,023 資料列，`Engineering Mode` 取
> 527 列之候選；量測時點 2026-08-24）中，就 10 個欄位所作之七組檢索，
> `SWE1-HMI-PM-028` 所指之 Off Road+ power moding 行為零命中；
> 另 1 個交付件（`Vehicle Settings/VF230_V1_R5`）為 0 列之空白工作簿，
> 無從命中。未檢索之欄位見上方盲區聲明。**

**故 A-PMH13 為全案缺口之判定成立。停止條件 8（07）／9（08）皆未觸發。**

### 裁定（R-PMH47，Pei 2026-08-24「上繳了 兩項都核可」）—— **(ii)＋(iii) 併行**

**(a) 判為 out of scope**（canon §8.4.2）—— 其內文逐字為
`OFF2.) Please refer to CFTS009 for complete behavior.`，本身無可驗證行為；
其行為定義於 CFTS009，屬他規格。**不得為其撰寫驗證 CFTS009 行為之 TC。**

**(b) 該列仍寫入工作簿並揭露**，不靜默丟棄（比照 R-VF12）。欄位處置：

| 欄 | 值 |
|---|---|
| `Test Set` | `Off Road Plus`（維持 R-PMH36 之分組） |
| `Test Item` | 037 之 `Requirement Title` 逐字（`CFTS009 Behavior Reference`）＋ 括號下半（profile §3.1 硬規則） |
| `Test Procedure` / `Expected Result` | `PENDING: DR-PMH1 CFTS009 所定之 Off Road+ power moding 行為`（§8.4.3 之缺件佔位，**不得留空、不得填 NA**） |
| `Remarks` | `[BLOCKED-SPEC] Owner: CFTS009 — behavior defined in an external specification; no coverage found in any delivered workbook.`（形態沿用 Comfort 之既有慣例，**非自創**） |

**(c) 開 `DR-PMH1`** —— 已登記於 `DATA_REQUESTS.md`（本 feature 首筆，狀態 `OPEN`）。

**⚠ 含 PENDING 之工作簿不得出貨**（§8.4.3）—— 交付前須 DR-PMH1 結案，
或由 Pei 裁定降轉。已記於 `DECISIONS.md` 之交付前阻斷項。

**連帶修改（已落實）**：profile §0 與 §2 之「48 leaf」已加註
「其中 1 條（`SWE1-HMI-PM-028`）為揭露列」；**48 之總數不變** ——
該 leaf 仍在 R-PMH1 之範圍內。

**本則狀態 → RESOLVED（處置已定）。** 其執行落在 Phase 4 之
`Off Road Plus` 批次；`DR-PMH1` 之結案另計（見 `DATA_REQUESTS.md`）。

---

### 原三種處置之並列（06 包 §六原文保留，供追溯）

- **(i)** 撰寫一條僅驗證「該行為存在且與 CFTS009 一致」之 TC，
  `specification_reference` 同時列 12.2 與 CFTS009 之對應節；
- **(ii)** 依 §8.4.2 判為 out of scope，於 `reasoning` 記為 coverage gap
  並指向 `features/power` 之對應 TC —— **查證後此案之後半不可行**
  （無對應 TC 可指）；
- **(iii)** 開 DR 詢問上游該 leaf 是否應存在於本報告。

**執行層之補充（不提案）**：查證結果使 (ii) 之形態改變 ——
原設想為「已被他 feature 涵蓋，故本 feature 不重複」，
而實測為「**兩邊都沒有**」。若仍採 (ii)，其記載須為
「out of scope 且 `features/power` 亦未涵蓋 → 全案缺口」，
而非「已由他 feature 涵蓋」。

**連帶**：`-027`（12.1）與 `-029`（12.3）**本身含可驗證行為**
（前者為「不喚醒」、後者為「靜音」），不受本則影響，
仍在 Test Set `Off Road Plus` 內正常生成。**本則只涉 `-028` 一個 leaf。**

---

## A-PMH14 — 雙向複驗查出 **三處 7.1 以外之新漏句**，其一使兩條需求根本不在 48 leaf 內 · PENDING

**登記日**：2026-08-24（13 包步驟 3，**停止條件 7 觸發**）

依 **R-PMH51** 補做方向二（PDF → SYS1）。方向一（SYS1 → PDF，01 包已做）
**看不見漏句** —— 漏句不顯示為「不符」，只顯示為「沒有這一則」。

### 方法

| 項 | 值 |
|---|---|
| 比對單位 | 句（句號後空白切分），最短 25 字元 |
| 正規化 | 去 `_x000D_`、摺疊空白、統一彎引號／省略號／破折號 |
| 一級判定 | 該句是否為對方全文之子字串 |
| **二級判定** | 未命中者再求 **6-gram 覆蓋率**；`< 30%` 者列為真漏候選，`>= 30%` 者判為 `pdftotext -layout` 之切分假象 |
| 產出 | `docs/reports/bidirectional_spec_diff.md` |

**方向二原始未命中 55 句**，經 6-gram 過濾後真漏候選 **37 句**，
其中 **23 句在 p1–p7**（封面 ＋ 五張流程圖頁）—— **屬 A-PMH04 已知之
圖片佔位，不計為新漏**。餘 **14 句在 p8–p11**，逐句查證後得**三處新漏**。

### 新漏 1 —— **`SU9.)` 與 `SU9.1)` 兩條需求整段缺失**（p8）

PDF p8 逐字（緊接 SU8 之後）：

```
SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle
SU9.) Pressing "Screen Off" or "Power Off" hard key will not do anything when
      pressed during animation.
SU9.1) Pressing Power Off or Screen Off hard keys during the splash screen(s) or
       disclaimer will reset the timeout and the radio shall display the screen
       the next time the screen turns on. (DCR20015)
```

SYS1 之 `7.9` 逐字為 **`SU8.) Show the splash screen and disclaimer screen once
per CAN BUS cycle`**，且 **7.9 為 7.x 之最末則**。

| 探針 | SYS1 全 52 則 |
|---|---|
| `SU8` | 有 |
| **`SU9.1`** | **0** |
| **`SU9)`** | **0** |
| `reset the timeout` | **0** |
| `hard keys during the splash` | **0** |

**⚠ 其後果不只是 `source_clause` 缺料 —— 是 leaf 不存在。**
037 之 leaf 以 `HMI Source ID` 指向 outline 編號；SYS1 既無 SU9／SU9.1 之
outline，**037 即無對應之 Functional Requirement 列**，故該二需求
**不在 R-PMH1 所定之 48 leaf 之內**。

**其題材正落在 `Disclaimer Screen` 之內**（按 Power Off／Screen Off 於
splash 或 disclaimer 期間之行為），且 **SU9.1 直接影響逾時語意** ——
batch 1 之 `-003`（逾時路徑）與 `-004`（Maserati 無逾時）之 pre-condition
因而須加「不按任何硬鍵」，該限定**只能自 PDF 取得**。

### 新漏 2 —— **p9 之 Power Moding 狀態矩陣表格全缺**

PDF p9 為兩欄狀態矩陣（`HEADUNIT POWER OFF` / `ON` × `ICS Hard Controls`／
`HVAC Knobs`／`Climate GUI`／`Headunit`，另分 `KEY ON ENGINE ON`／
`KEY OFF (ACC)`／`KEY OFF (No ACC)` 三列）。

| 探針 | SYS1 全 52 則 |
|---|---|
| `ICS Hard Controls` | **0** |
| `HVAC Knobs` | **0** |
| `Climate GUI` | **0** |
| `Power Button only is functional` | **0** |
| `Fully functional` | **0** |
| `ENGINE ON` | **0** |

SYS1 之 `9.1` 只有 `PM1)`–`PM4)` 之散文（1,265 字元）。
**5 個 leaf 引 `9.1`** —— 其判讀所需之狀態矩陣不在 SYS1 內。
（該表為表格形態，與 A-PMH04 之圖片佔位同類，惟**其所在之 ch 9 有 leaf**，
而 2.1–6.1 無，故性質不同。）

### 新漏 3 —— **指向一份我們沒有之外部規格**（p10）

PDF p10 逐字：

```
POWER MODING STATE MATRIX: Power Moding behavior shall not be developed without
following the Power Moding State Matrix, which is in a separate Excel document.
If this document is not available, please request a copy from the author of this
logic and flow document.
```

| 探針 | SYS1 全 52 則 |
|---|---|
| `POWER MODING STATE MATRIX` | **0** |
| `State Matrix` | **0** |
| `separate Excel` | **0** |
| `request a copy from the author` | **0** |

**這是一條規範性陳述**（`shall not be developed without following …`），
指向一份**獨立 Excel 文件**，而該文件**不在本 feature 之四份素材內**。
**已開 `DR-PMH2`。**

### 非新漏者（具名，避免誤計）

| 項 | 判定 |
|---|---|
| p1–p7 之 23 句 | **A-PMH04 已知** —— SYS1 之 2.1–6.1 為圖片佔位，封面頁無對應 outline |
| p10 之 VRLP1 四個 outcome（`Screen ON and Audio OFF` 等） | **非漏** —— SYS1 之 11.1 有之，僅條列符號與順序不同（A-PMH03 原記之「條列再流」） |
| p11 之 1 句 | **A-PMH04 已知** —— 12.4 為圖片佔位 |

### 對 A-PMH03 之影響

A-PMH03 原記「四則缺口」（7.1 重排、8 拼字、9.1／11.1 條列再流）。
**該框架本身不成立** —— 它以「SYS1 之則」為單位計缺口，
而**漏句沒有「則」可計**（SU9／SU9.1 在 SYS1 中不存在任何一則）。

**改判**（R-PMH51）：
- 7.1 —— **漏句**（12 包已證）
- 8 —— 拼字（`Starup`），維持
- 9.1／11.1 —— 條列再流，**維持**（本輪方向二未在其上查出新漏）
- **新增：SU9／SU9.1 整段缺失、p9 狀態矩陣全缺、p10 STATE MATRIX 註記缺**
  —— **此三者不對應任何 SYS1 之則，故不計入「四則」，另計。**

### ⚠ 結語之更正（17 包步驟 2，R-PMH63）—— **上段原句一字未改**

上段「**改判**（R-PMH51）」四列中，**第二、三列不成立或不完整**。
依 R-PMH44，原句保留於上，更正載於此。

#### (a) `9.1` 之「維持」**不成立**

原句：「9.1／11.1 —— 條列再流，**維持**（本輪方向二未在其上查出新漏）」。

**與同一則之「新漏 2」直接衝突** —— 新漏 2 所查出者即
**p9 之 Power Moding 狀態矩陣全缺**，而 p9 對應之 outline **正是 9.1**
（本則自載：「SYS1 之 `9.1` 只有 `PM1)`–`PM4)` 之散文（1,265 字元）。
**5 個 leaf 引 `9.1`** —— 其判讀所需之狀態矩陣不在 SYS1 內。」）。

**故 9.1 之正確判定為**：`SSND`／`PM` 散文部分之條列再流**成立**，
**惟其章之狀態矩陣整表缺失**（新漏 2）—— 二者並存，
「未在其上查出新漏」一語**不實**。

**成因**（R-PMH62 之形態）：12 包以雙向法推翻 7.1 時，
於同一段寫下「原記之其餘三則…**不變**」而未對其套用同一判準；
13 包補做了方向二**卻沿用了 12 包那句「維持」**，
致該句與同一份文件中自己剛查出的結果相衝突。
由執行層於 16 包 §5.1 指出。

#### (b) `11.1` 之「維持」**成立，不受影響**

其依據為本則「非新漏者」表中之
「p10 之 VRLP1 四個 outcome —— **非漏**，SYS1 之 11.1 有之」，
**該項確為方向二之實測結果**（16 包 §5.1 覆核確認）。

#### (c) `8` 之「拼字，維持」**當時不得引用；本輪補做後成立，且其歸因須更精確**

R-PMH51 明文：其餘三則「**須以雙向法複驗；未複驗前，其標題結論
不得引用**」。**`8` 至今未做** —— 12 包記「不變」、13 包方向二未在
p8 之該標題上具名任何結論，**而「拼字」之結論仍被沿用了兩包**。

**17 包步驟 3 補做**（`scripts/chapter_bidirectional.py 8`）：

| 方向 | 結果 |
|---|---|
| 一（SYS1 → PDF） | 7 則中 6 則逐字命中；**未命中者僅 outline `8` 之標題**（覆蓋率 100%） |
| **二（PDF → SYS1）** | PDF 章 8 段切 8 句，**8/8 逐字命中，真漏候選 0** |
| marker | PDF 段內 `SSND 1)`～`SSND 3)` 共 6 個，與 SYS1 之 6 leaf 一一對應 |

**結論：章 8 無漏句**，「拼字」之歸因成立。**惟其歸因須更精確** ——

PDF **本文之節標題只有 `R1Low Only`**（p8，`get_text("blocks")` 之 y=469.3
區塊）；`Startup` 為**頁首之頁眉**（同頁 y=21.6 之獨立區塊）。
`pdftotext -layout` 與 PyMuPDF 兩份萃取**皆無 `Startup R1Low Only` 此一連續字串**。

故 SYS1 之 `Starup R1Low Only` **並非單純之拼字錯誤** ——
它是**頁眉（`Startup`）與節標題（`R1Low Only`）兩個獨立文字物件之串接**，
且串接時掉了一個 `t`。原記「PDF 為 `Startup R1Low Only`」**於 PDF 中無此字串**。

**影響**：無。該標題不對應任何 Functional Requirement leaf
（章 8 之 6 leaf 為 8.1～8.3），亦不入任何 TC 之 `source_clause`。
**登記其正確形態，供日後引用。**

---

### 提案處置（不裁定）

(a) `source_clause` 一律取自 PDF —— **R-PMH50 已定，本輪再獲佐證**；
(b) **SU9／SU9.1 之 leaf 缺口**：其不在 48 leaf 內，**開 DR 詢問上游
    037 是否應含該二需求**（與 A-PMH13 之形態相反 —— 那是 leaf 存在而
    行為在他處，這是**行為存在而 leaf 不存在**）；
(c) p9 狀態矩陣：Phase 4 撰寫 ch 9 之 5 個 leaf 時，**須自 PDF p9 render
    圖像判讀**（A-PMH04 之 render 能力實測已證 300 DPI 可辨讀）；
(d) `DR-PMH2` 索取 Power Moding State Matrix Excel。

---

## A-PMH15 — 規格原文之 marker 前綴斷裂：`DS4.1)` 夾於 `SU4.)`／`SU5.)` 之間 · **登記，不開 DR**（R-PMH26）

**所見**（15 包 §2.1／§2.3，執行層以反向掃描複驗）：

PDF 章 7 之 marker 序為

```
… SU3.)  SU4.)  DS4.1)  SU5.)  SU6.) …
```

`DS4.1)` 之編號 `4.1` 與其上文 `SU4.)` 呈父子關係（比照 `SU1.)`／`SU1.1)`、
`SU2.)`／`SU2.1)` 之既有慣例），**而其前綴由 `SU` 變為 `DS`**。
本規格全文除此一處外無任何 `DS` 前綴。

逐字（`sandbox/spec.txt`）：

```
DS4.1) If doors are removed/not present and ignition is turned to ACC, RUN, or
       START, do not show Start Up Animation and jump directly to Splash screen.
```

**判定**：極可能為規格原文之筆誤（應為 `SU4.1)`）。

**處置**：依 **R-PMH26**，**只登記，不開 DR**；本 feature 一律照原文處理 ——
`marker_coverage.py` 之判定表將 `DS` 列為 `req`，其 marker 逐字保留為
`DS4.1)`，不代為改寫為 `SU4.1)`。

**其所致之量測錯誤**（已修正，見 R-PMH57）：14 包以**人工列舉**之六前綴
枚舉 marker，`DS` 不在列，致 PDF marker 全集被算為 **30** 而非 **31**。
`DS4.1)` 於 SYS1 命中（outline 7.5.1），**故缺漏數 2 不變、
「截斷非系統性」之結論不變 —— 錯的是分母**。

**本項之意義不在該筆誤，而在其暴露之量測形態**：該錯為分析層與執行層
**各自獨立算出之同一值**，因二者用了同一份人工前綴清單。
**先算後比（R-G7-1）只能抓「算法不同而結果不同」，抓不到
「前提相同而前提本身錯」** —— 前提本身須另有反向驗證。

**狀態**：登記完成。不阻斷。

---

## A-PMH16 — **SYS1 之 `9.1` 散文本身漏字，其一為時序子句** · 18 包步驟 2 查出 · PENDING

**登記日**：2026-08-24（18 包步驟 2，依 **R-PMH66** 之殘餘人讀）

### 所見

A-PMH14 之新漏 2 已載「p9 之狀態矩陣**表格**全缺」。
**本輪另查出：SYS1 之 `9.1` 所保留之 `PM1)` 散文，其本身亦非逐字。**

量測方式：以 PyMuPDF `get_text("blocks")` 取 PDF p9 之 `PM1)` **單一文字區塊**
（658 字元，未與矩陣交錯），對 SYS1 `9.1`（1,265 字元）做**字級** diff。

| # | PDF p9 之 `PM1)` 區塊 | SYS1 `9.1` | 判定 |
|---|---|---|---|
| **1** | `the head unit should 'stay awake'` **`for 60 seconds`** `up to 2.5 minutes` | `the head unit should 'stay awake up to 2.5 minutes` | **漏 —— 時序子句 ＋ 收尾單引號** |
| **2** | `interact with the popup within 60` **`seconds`** `the timeout` | `interact with the popup within 60 the timeout` | **漏 —— 時序單位**（SYS1 之句因而不成句） |
| **3** | `pop-up list,` **`the radio should shut Off the`** `popup should close` | `pop-up list, the popup should close` | **漏 —— 整個子句** |
| 4 | `popup should close` **`aofnd`** `if no other popups` | `popup should close if no other popups` | **非漏** —— `aofnd` 為 PDF 原文之 typo，SYS1 逕改為 `if`（**未經授權之改寫，登記但不視為漏**） |

### 其嚴重性 —— **與 A-PMH03 之 7.1 完全同型**

被漏之 (1)(2) **皆為時序**（60 秒之 stay-awake 窗、60 秒之互動逾時），
正是 **A-PW68**（Power Management `006` 時序誤讀，歷經兩輪修正與多次 lint
全綠而未被察覺）之形態。**7.1 漏的是動畫／splash 之時序，9.1 漏的是
popup stay-awake 之時序 —— 同一份 SYS1 匯出，同一類內容，兩處。**

**5 個 leaf 引 `9.1`** —— 若以 SYS1 為判讀基準撰寫其 TC，該二時序無從得知。
**R-PMH50（`source_clause` 取自 PDF）於此第三度獲得直接佐證。**

### **為何 13 包之全簿雙向 diff 沒查出**

13 包方向二以 `pdftotext -layout` 之 PDF 全文切句，
**而 p9 之文字層是兩欄矩陣與 `PM1)` 散文交錯**，切出之「句」皆為
矩陣格與散文之混合串。該等混合串之 6-gram 覆蓋率多 >= 30%，
**遂被門檻自動判為「`-layout` 之切分假象」而濾掉。**

**這正是 R-PMH66 所禁止之事** —— 門檻不得決定結論。
本輪依 R-PMH66(b)(c) 令殘餘逐句人讀，該四處即於第 9、11 句浮現。

**且其修法亦已具名**：p9 之比對不得用 `-layout` 之交錯文字，
須用 **block 層**之萃取（PyMuPDF `get_text("blocks")`），其 `PM1)` 為單一區塊。

### 另一項（同輪、較輕）

`Please refer to Power Moding State Matrix for further specifications.`
—— 章 9 之**首句指標句**，SYS1 全 52 則命中 **0**。
屬新漏 2 之範圍（同一矩陣），**惟 A-PMH14 未具名此句**，本輪補記。
與新漏 3（p10 之 `POWER MODING STATE MATRIX:` 段）同形態、不同位置。

### 處置（提案，不裁定）

(a) **不阻斷 batch 1** —— 章 9 之 5 leaf 不在 `Disclaimer Screen` 組內；
(b) 撰寫 ch 9 之 5 leaf 時，`source_clause` **須取自 PDF p9 之 block 層萃取**，
    不得取自 SYS1，亦不得取自 `-layout` 之交錯文字；
(c) **`DR-PMH2` 之理由再增一項** —— 該矩陣不僅表格缺，其散文亦已失真；
(d) `chapter_bidirectional.py` 之 PDF 來源**現仍為 `-layout`**，
    章 9 之殘餘結論係以 block 層另行查證後寫入 `RESIDUE_VERDICT`。
    **改用 block 層為預設來源，屬判準變更，須另立條文。**

**狀態**：PENDING。不阻斷本包。

---

## A-PMH14 之三則新漏 —— 19 包之狀態更新（R-PMH73／R-PMH74）

**原文一字未改**，狀態更新如下（R-PMH44）。

| 新漏 | 內容 | 19 包之狀態 | 依據 |
|---|---|---|---|
| **1** | `SU9.)`／`SU9.1)` 兩條需求整段缺失 | **`ACCEPTED（經裁定不補）`** | **R-PMH74** —— Pei「037 沒有納入就不放」。事實不變（PDF 有而 SYS1／037 無），惟不補入 leaf 母體。**R-PMH55 之適用因而繼續成立** |
| **2** | p9 之狀態矩陣表格全缺 | **`PENDING（來源已到，惟內容不對應）`** | 見 **A-PMH18** —— Pei 所提供之 State Matrix，其軸與 p9 之軸**逐字探針全 0**。**故不改為 `RESOLVED`** |
| **3** | p10 之 `POWER MODING STATE MATRIX:` 段缺失 | **`RESOLVED（來源已補）`** | **R-PMH73** —— 該段之內容即「矩陣存在於一份獨立 Excel」，該 Excel 確已到齊（`shasum -c` 6/6 OK），其前提成立 |

**新漏 2 與新漏 3 之處置不同，其理由須明說**：新漏 3 缺的是**一句指標**，
指標所指之物已到 → 結清；新漏 2 缺的是**矩陣之內容**，
而已到之物**不含該內容** → 不得結清。**二者不可一併處理。**

---

## A-PMH16 之改判 —— 19 包（R-PMH75）

**原文一字未改**（R-PMH44）。其三處判定**逐條被 R-PMH75 推翻**：

| # | A-PMH16 原判 | R-PMH75 之改判 |
|---|---|---|
| 1 | `for 60 seconds` 為**時序漏失** | **舊文字，已刪，不驗** |
| 2 | `seconds`（`within 60 seconds`）為**時序漏失** | **舊文字，已刪，不驗** |
| 3 | `the radio should shut Off the` 為**獨立行為結果**（19 包 §2.2 之加碼） | **舊文字，已刪，不驗** |

**狀態改為 `RESOLVED（PDF 側為未刪淨之舊文字）`。**

Pei 於 2026-08-24 裁「**以刪掉之後的為主**」→ outline `9.1` 之權威文本為
**SYS1 匯出**，R-PMH50 於該處反轉（其 `source_clause` 取自 SYS1，
`source_clause_origin` 記 `sys1_export 9.1` 並註 `R-PMH75`）。

**⚠ 承擔之風險（R-PMH75 已具名，此處重述）**：
`the radio should shut Off`（逾時後收音機關機）**不會有任何一條 TC 驗到**。
若上游日後主張該行為仍屬需求，ch 9 之覆蓋即有缺口。

**本則之量測本身不撤銷** —— 「PDF 與 SYS1 於該三處不同」之事實不變，
改變的是**何者為權威**。

---

## A-PMH17 — PDF 章 10 之全大寫分節標籤於 SYS1 全缺 · 19 包步驟 2 查出 · PENDING（低）

**登記日**：2026-08-24（19 包步驟 2，章 10 之殘餘人讀）

PDF 章 10 內以**全大寫標籤**分節，該等標籤於 SYS1 全簿命中 **0**：

| 標籤 | SYS1 全 52 則 |
|---|---|
| `POWER BUTTON:` | **0** |
| `KEY OFF, HEADUNIT POWER ON:` | **0** |

**與章 11 之對照**：章 11 之 `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS`
**於 SYS1 有**（即 outline `11` 本身）。**故並非所有全大寫標籤都被丟掉** ——
章 11 之標籤成了一個 outline，章 10 之兩個沒有。

**影響：低。** 二者為**分組標籤而非需求**，其下之 `PITA4:`／`PITA8:` 本文
於 SYS1 之 `10.1`／`10.5` 皆逐字存在（19 包步驟 2 實測）。
**不對應任何 leaf，不入任何 `source_clause`。**

**惟須登記之理由**：它是「SYS1 之結構化過程會丟東西」之第三個實例
（前二為 A-PMH03 之 7.1 漏句、A-PMH14 之三則），
**且此次丟的是「分節結構」而非「句」** —— 形態與前二者不同。

**狀態**：PENDING（低）。不阻斷。

---

## A-PMH18 — **Pei 所提供之 State Matrix 與 PDF p9 之矩陣不對應** · 19 包步驟 8 查出 · **停手上呈**

**登記日**：2026-08-24（19 包步驟 8，依 R-PMH73 之明文「不一致即停」）

### 素材

| 項 | 值 |
|---|---|
| 檔名 | `Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421 (August 3 2022).xlsx` |
| 台帳 | 已入 `inputs/MANIFEST.sha256`，`shasum -c` **6/6 OK** |
| 分頁 | `Title`／`State Matrix`／`SR24 Change Log` |
| `State Matrix` | 43 非空列、362 非空格 |

### 逐字探針 —— **PDF p9 之標籤於該 Excel 命中全 0**

`HEADUNIT POWER`／`ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／
`ENGINE ON`／`ENGINE OFF`／`Power Button only is functional`／`Fully functional`／
`Power Accessory Delay`／`accessory delay`／`FOTA`／`Charge Now`／`stay awake`
—— **十三個探針全部 0 命中**。

### 二者為兩個不同的矩陣

| | 軸 | 列 |
|---|---|---|
| **PDF p9** | `HEADUNIT POWER OFF`／`ON` × `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit` | `KEY ON ENGINE ON`／`KEY OFF (ACC)`／`KEY OFF (No ACC)` |
| **Excel** | `Key-on`／`Key-off`／`Key On Gear≠Reverse` 三區塊 × `Turn Off @ door opening Enabled/Disabled` × `HU on/off` × `Call Active/Not Active` × `Door Open/Closed` | 事件（`ON/OFF button Pressed`／`Door opened`／`Incoming Call`／`Call Ended` …） |

### 版本落差（R-PMH73 明文要求具名）

| 文件 | DCR | 日期 |
|---|---|---|
| Excel State Matrix | `DCR21421` | **2022-08-03**（Title 分頁自載） |
| 規格 PDF | `DCR22412` | 2023-01-24 |

**Excel 較早。** 且其 `SR24 Change Log` 之**末筆為 2021-10-20**，
**未及其自稱之 2022-08-03** —— 該檔之變更紀錄與其自稱日期亦不一致。

### 處置 —— **不自行取捨**（R-PMH73 明文）

**未執行之事，逐項具名**：

1. **A-PMH14 新漏 2 未改為 `RESOLVED（來源已補）`** ——
   R-PMH73 之該項結論建於「內容在另一份素材裡」之前提，**而實測不在**。
   逕改會使本檔出現一句不實陳述（R-PMH43／R-PMH63）。
2. **ch 9 之 TC 未以該 Excel 為判讀背景撰寫** ——
   R-PMH73 定其為「ch 9 之規範性判讀背景」，
   **惟其內容不涵蓋 p9 之四個維度**，無從據以撰寫該五條。

### ⚠ 20 包之補記 —— **語意層對照亦不涵蓋，A-PMH18 不動搖；且 R-PMH73 之定位錯誤已更正**

19 包 §14 第 1 項自陳只做了**標籤層**（逐字探針）之比對，
未做語意層對照，且指出 `HU on`／`HU off` 確實在該 Excel 內。
**分析層於 20 包 §2.1 做了語意層對照，結論相同**：

| | **PDF p9 之矩陣** | **Excel `State Matrix`** |
|---|---|---|
| 型別 | **靜態能力表** | **事件驅動之狀態轉移表** |
| 列軸 | 電源狀態 | **事件** |
| 欄軸 | 受控對象 × `HEADUNIT POWER OFF/ON` | **情境條件**（`Turn Off @ door opening` × `HU on/off`／`Power Button OFF` × `Call` × `Door`） |
| 格 | **是否可用** | **轉移後之結果** |

**`HU on`／`HU off` 於 Excel 中是「情境條件」，不是 p9 之「受控對象在該電源
狀態下是否可用」** —— Excel 全簿無任何一格描述 `ICS Hard Controls`／
`HVAC Knobs`／`Climate GUI` 三者之可用性。
**逐字不對應與語意不涵蓋，二者皆已驗。**

**R-PMH73 之定位錯誤已由 R-PMH76 更正**：該 Excel 之真正效力範圍為
**ch 12（Off Road+）**與 **ch 10 之一部**（見 20 包上繳 §三、§四），
**非 p9 之能力矩陣**。

**A-PMH18 維持 `PENDING`**，其狀態不因該 Excel 到齊而改變。
**已開 `DR-PMH5`** 索取 p9 能力矩陣之來源文件。

### 21 包補記 —— **矩陣之對照涵蓋，逐項留下數字**（21 包步驟 7）

20 包只逐格讀了與 ch 10／ch 12 相關之 **9 列**；21 包對 **ch 7** 做了全對照。
現況以數字記之：

| 項 | 數 |
|---|---:|
| `State Matrix` 分頁之非空列 | **43** |
| 其中之**事件列**（有列標籤且至少一格有值） | **30** |
| 非空格總數 | **362** |
| 其中 `-`／`'-` 佔位 | **93** |
| **事件列之有值格**（＝可對照之母體） | **174** |
| 其餘（區塊名、欄軸、列軸、標題） | **95** |

**已對照者**：

| 章 | 範圍 | 結果 | 出處 |
|---|---|---|---|
| **7** | **30 事件列全部** | 牴觸 0／印證 0／**未對照 30** | 21 包 §3（`scripts/matrix_vs_chapter.py 7`） |
| 10 | `r40`／`r41`／`r42`／`r43`／`r44`／`r45`／`r48` 等 7 列（部分欄） | **牴觸 1**（`10.3` vs `r48c10`）／其餘見 20 §4 | 20 包 §4 |
| 12 | `r16`（12 欄逐欄） | 互補，不衝突 | 20 包 §3 |
| **8** | **未對照** | —— | —— |
| **9** | **未對照** | —— | **A-PMH18 之主體：p9 之能力矩陣本不在此 Excel 內** |
| **11** | **未對照** | —— | —— |

**仍未對照者具名**：章 **8**（`Startup Sounds`，6 leaf）與章 **11**
（`Voice Assistant Key`，5 leaf）之 outline **完全未與矩陣對照**。
矩陣之 `VR button long press without/at Projection`（`r11`／`r12`／`r28`／`r29`）
與 ch 11 之 `VRLP1` 顯有共同主題，**而該對照本包未做**。

**該二章之開批前應先完成其對照** —— 形態同於本包對 ch 7 所做者。

**待 Pei**：p9 之矩陣是否另有一份文件？
或 p9 之矩陣本即 PDF 自身之摘要、而該 Excel 為另一主題
（開機／關機之事件轉移）之矩陣，二者本不對應？

**狀態**：**停手上呈。** 不阻斷本包其餘工作；**阻斷 ch 9 開批**。

---

## A-PMH19 — `-007` 加事件層限定後之**覆蓋缺口三項** · 22 包步驟 9 · PENDING

**登記日**：2026-08-25（依 **R-PMH55(b)**／**R-PMH87** 之連帶）

`-007` 依 R-PMH87 於 procedure 加「不按 ON/OFF 鍵、不轉 key-off、
不開啟車門、不操作 HVAC 硬控」四項限定後，下列行為**不被任何 TC 涵蓋**：

| # | 未涵蓋之行為 | 來源（矩陣） | 是否有 leaf |
|---|---|---|---|
| 1 | 免責畫面顯示期間**按 ON/OFF 鍵**（通話中）→ `Pop-up: Cannot Power Off System during active phone call.` | `r6` c2／c3／c6／c7（皆 `Call Active`） | **無** |
| 2 | 免責畫面顯示期間**轉 key-off**（通話中，**僅 R1High**）→ `VP display pop-up: "Power OFF System. Continue call on mobile phone? Yes or NO"` | `r15` c2／c3／c6／c7（皆 `Call Active`） | **無** |
| 3 | 免責畫面顯示期間**調整 HVAC 硬控** → `Show Pop-Up …` | `r48` c2／c3／c4／c5（`Gear != Reverse`） | **無**（其相關者 `PITA6`／10.3 已由 R-PMH80 處置） |

**另二列之格不列為缺口**：`r24`（`Key-off` 區塊之 `ON/OFF button Pressed`）
與 `r25`（`Door opened`）之情境為 **key 已 off**，
**而免責畫面出現於開機序列（key-on）** —— 其與免責畫面期間之重疊性最低。
**惟此為本層之判斷，非量測**（矩陣未斷言其不重疊），故一併記於此供覆核。

**依 R-PMH55(b)**：三者皆「只在矩陣有、規格未載」，**不得為其撰寫 TC**。

**歸屬**：依 22a §五，二擇一 ——
（甲）`DR-PMH6` **尚未發出** → 直接增補其全文；
（乙）`DR-PMH6` **已發出** → 另開 `DR-PMH8` 承接。
**Pei 已表明三筆 DR 由其自行處理，故其是否已發出執行層無從得知** ——
**本輪依 R-PMH82 記 `DR-PMH6` 為 `DRAFT`（發出日期欄空白），故採（甲）**，
已將三項增補入 `DR-PMH6` 之全文。**若 Pei 實際已發出，請改採（乙）。**

**狀態**：PENDING。**不阻斷 batch 1**（其為揭露而非待答）。

---

## A-PMH20 — 規範性素材使用規格未定義之術語 `VP` · 22 包 §二 · PENDING

**登記日**：2026-08-25（依 **R-PMH85(a)**）

| 來源 | `VP` 之命中 |
|---|---|
| **規格 PDF（全 11 頁）** | **0** |
| Excel `State Matrix` | **30 格** |

**其三種用法（逐字）**：

```
VP Stays ON / VP Turns OFF / VP turns Off / VP standby mode
VP display pop-up: "Power OFF System. Continue call on mobile phone? Yes or NO"
(R1Low) VP Stays ON  (R1High) VP display pop-up: …
If Radio Off Delay = 0 minutes then VP turns OFF Else VP stays ON
```

**由用法可知其功能**：`VP` 是**會開關、且會顯示 pop-up 之物**。
**其指涉未定義** —— 規格未定義該縮寫，本 feature 之**六筆素材**亦無定義。

### 其影響 —— 直接及於 21／22 包之對照判定

若 `VP` 即 head unit 之顯示螢幕，則 `VP display pop-up` 與 `SU3.)` 之
`No pop-ups will appear` **為同一謂詞**。

**依 R-PMH85(c)**，凡倚賴 `VP` 指涉之判定一律標「**待定義**」：
`r6`／`r15`／`r24`／`r25` 四列已改標（22 包步驟 2）。
**`r48` 不倚賴 `VP`**（其格逐字為 `Show Pop-Up`，未用該詞），
故其**牴觸獨立成立**。

**已開 `DR-PMH7`**（`DRAFT`）。**在其 `ANSWERED` 前，該四列不得轉為其他記法。**

**狀態**：PENDING。**阻斷該四列之判定，不阻斷 batch 1**
（`-007` 之限定已依 R-PMH87 排除全部四列之事件）。

---

## A-PMH21 — **規格內部之牴觸**：`SU3.)`（p8）× p9 能力矩陣之 `Pop-ups still shown` · 23 包 · PENDING

**登記日**：2026-08-25（依 **R-PMH89**，分析層 23 包 §三查出，執行層複驗並更正其列位）

### 兩造逐字

**一造 —— `SU3.)`（PDF p8，outline 7.4，`Disclaimer Screen` 組之 `-007` 所依）**：

> `No pop-ups will appear until the disclaimer screen has been removed. If an item
> like a traffic announcement is received like on this screen the user will begin
> hearing the announcement in the background but will not see the pop-up until the
> disclaimer screen is removed.`

**全稱否定**，其範圍為「免責畫面移除前之所有時刻」。

**另一造 —— PDF p9 之能力矩陣，`HVAC Knobs` 格（出現兩次）**：

> `HVAC Knobs: Fully functional. `**`Pop-ups still shown.`**

**無條件肯定。**

### ⚠ 其列位與分析層所報不同 —— 執行層以座標複驗後更正

分析層 23 §3.2 記其為「`KEY OFF (ACC)` 與 `KEY OFF (No ACC)` 兩列之
`HEADUNIT POWER OFF` 欄」。**實測不然**（`fitz` `get_text("blocks")` 之座標）：

| 出現 | 座標 | 所屬列（列標籤之座標） | 欄 |
|---|---|---|---|
| 第 1 次（L332） | x=428, y=**81** | **`KEY ON ENGINE ON`**（y=114） | `HEADUNIT POWER OFF` |
| 第 2 次（L348） | x=428, y=**180** | **`KEY ON ENGINE OFF (ACC or RUN)`**（y=197） | `HEADUNIT POWER OFF` |

**`KEY OFF` 兩列之 `HVAC Knobs` 格逐字為 `OFF`，並無 pop-up 之敘述**
（21 包 §3 之章 9 殘餘已錄其逐字：`HVAC Knobs: OFF HVAC Knobs: OFF
Climate GUI: OFF Climate GUI: Forced OFF`）。

**該更正使牴觸更強而非更弱** —— 免責畫面之相位**正是 `KEY ON`**
（`SU1.)`：駕駛門關閉 → 開機動畫 → splash → 免責畫面；
`PITA6.1`：ignition 由 OFF 轉 ACC 或 RUN）。
**二者之條件不僅「未證互斥」，而是高度可能重疊。**

### 判定（R-PMH79／R-PMH84）

- **共同謂詞**：pop-up 是否顯示；
- **取相反值**：`SU3.)` 不顯示／p9 顯示；
- **條件互斥？未證，且證據指向重疊。**

→ **牴觸。**

### ⚠ **不得以「以規格為權威」解之**（R-PMH89 明文）

先前之 `10.3`（R-PMH80）與 `r48`（R-PMH87）皆為**規格 vs 素材**，
其處置得以「規格與素材各在其條件下成立」了結。
**本處兩造皆是規格**（同一份 PDF，p8 與 p9），該原則在此**無分辨力**。

### 處置

依 R-PMH89（同 R-PMH80 之形態）：**限縮 ＋ 揭露，不裁權威**。

`-007` 之四項事件限定已含「**不操作 HVAC 硬控**」，
而 p9 之該格所述之情境即 HVAC 旋鈕之操作 —— **限定不必增加**；
其 `reasoning` 之依據已擴為「矩陣之 17 格 ＋ 規格 p9 之 2 行」（23 包步驟 4）。

### 連帶

**`DR-PMH5` 之問題全文須增列此項** —— p9 之能力矩陣不只「無來源」，
**其自身之內容與 p8 之 `SU3.)` 相衝**。已增補（其狀態仍為 `DRAFT`）。

**狀態**：PENDING。**不阻斷 batch 1**（限定已涵蓋）。

### ⚠ **24 包之改判 —— 牴觸不成立，改為「未對照」**（原文一字未改，R-PMH44）

**成因**：24 包 §2.3 指出「**欄位沒有人驗過，而欄位決定這個牴觸有多強**」。
執行層以 **`get_pixmap` 4x 渲染 p9 之矩陣區**（`fitz.Rect(340, 40, 760, 260)`）
實地判讀，該問題**由量測回答**：

| 項 | 實見 |
|---|---|
| `HVAC Knobs: Fully functional. Pop-ups still shown.` 之欄 | **`HEADUNIT POWER OFF`**（左欄） |
| 其列 | `KEY ON ENGINE ON` 與 `KEY ON ENGINE OFF (ACC or RUN)` |
| 右欄（`HEADUNIT POWER ON`）之同位格 | `HVAC Knobs: Fully functional`（**無 pop-up 之敘述**） |

**條件互斥自此成立，且其依據為量測而非推定**（R-PMH84 之要件）：

1. **免責畫面為 head unit 所顯示之畫面** —— 其相位必為 head unit **開機中**；
2. 而 `Pop-ups still shown` 所在之欄為 **`HEADUNIT POWER OFF`**；
3. **同一欄之 `Climate GUI` 格逐字為 `Not Visibile due to power off`**
   —— **該欄之語意即「頭端電源關閉」，其時無任何畫面可顯示免責內容。**

**故 `SU3.)` 與該格之條件互斥，二者不在同一時刻，非同一命題之相反值。**

**記法由 `牴觸` 改為 `未對照`**（R-PMH79／R-PMH84）。
`spec_assertion_scan.py` 之 `LINE_VERDICT` L332／L348 已同步改判，
其全檔之牴觸數由 **2 降為 0**。

**⚠ 本則不撤銷** —— 「p9 之能力矩陣有 `Pop-ups still shown` 而 p8 之 `SU3.)`
為全稱否定」之事實不變，改變的是**二者之條件已證互斥**。
**其登記價值在於：該互斥曾被三包（22／23／24）當成未證。**

### 25 包 —— **互斥之依據更換（R-PMH96）**：由常識改為規格逐字

24 包之改判其互斥證明繫於「**免責畫面必為 head unit 開機中所顯示**」，
而執行層自陳「**它是常識而非引文**」（24 §10 第 4 項）。

**引文存在** —— `PITA6.1`（outline 10.4）逐字：

> `Upon pressing power button to On state disclaimer screen shall be displayed
> (see SU6.) unless certain phone call scenarios have occurred.`

**免責畫面之顯示條件即 head unit 轉為 On**，故其不可能出現於
`HEADUNIT POWER OFF` 欄所述之狀態。**互斥之依據自此為規格文字。**

### 25 包 —— **欄位以字級座標確認，不再倚賴渲染判讀**

24 包以 `get_pixmap` 渲染判讀。本輪以 `get_text("words")` 取字級座標複驗
（**先算後比，與分析層 25 §2.1 逐項相符**）：

| 詞 | x | 欄 |
|---|---:|---|
| `HEADUNIT` ＋ `OFF`（y=65.8） | 467.9／**490.5** | 左欄 = `HEADUNIT POWER OFF` |
| `HEADUNIT` ＋ `ON`（y=65.8） | 641.4／**665.3** | 右欄 = `HEADUNIT POWER ON` |
| **`Pop-ups`（兩處，y=114.2／213.3）** | **483.0** | **左欄** |
| `Visibile`（`Not Visibile due to power off`） | 442.5 | **左欄，與 `Pop-ups` 同欄** |
| `Knobs:`（每列兩次） | 448.5／**596.6** | 左／右欄之 x 基準 |

**`Pop-ups`（483.0）< 右欄基準（596.6），且與同欄之 `Visibile`（442.5）同側。**
**其論證自此不需要人眼判圖。**

---

## A-PMH22 — 矩陣之 `Else: Mute Active` 記法未定義 · 25 包 · PENDING（低）

**登記日**：2026-08-25（依 **R-PMH95**，24 包 §4.3／§10 第 1 項自陳）

`State Matrix` 之 `r46`（`Headunit Mode Button Pressed`）與 `r47`
（`Headunit Mode Change via VR`）其格逐字為：

```
Screen Off Inactive If Radio/Media, Mute --> Inactive. Else: Mute Active
```

**同一格內有兩種記法**：`Mute --> Inactive`（**有箭頭**）與
`Mute Active`（**無箭頭**）。

| 讀法 | `Else: Mute Active` 之意 | 後果 |
|---|---|---|
| （甲）**維持** | 靜音狀態不變 | 與 `-007` ER4(b) **未對照** |
| （乙）**使之靜音** | 靜音由否轉是 | 與 `-007` ER4(b) **牴觸** |

**矩陣未定義其記法** —— 24 包以「箭頭之有無」判為（甲），
**其依據為本層之判讀而非素材之定義**。

### 處置（R-PMH95）—— **不判讀，改以涵蓋兩讀之限定**

`r46`／`r47` 之觸發（`Headunit Mode Button Pressed`／
`Headunit Mode Change via VR`）**皆為測試員可控之事件**，
故 `-007` 之限定納入該二事件（第 6、7 項，25 包 §3.4）——
**無論該詞作何解，該二列皆不適用。**

**本則不因此結清** —— `Else: Mute Active` 之語意仍未定；
**本則只記其「本 feature 之判定已不再倚賴它」**。

**影響**：低。**不阻斷**。
**惟若日後有 TC 之斷言涉及 headunit mode 之靜音行為，本則即復活。**

**未開 DR** —— 其為記法之歧義而非缺件，且已由限定涵蓋；
**若上游另有機會詢問，可併入 `DR-PMH7`（`VP` 之定義）之同一封**。



**連帶**：
- **`-007` 之限定與 ER 不受影響**（其四項限定本即涵蓋 HVAC 硬控）；
  其 `reasoning` 之依據須自「矩陣 17 格 ＋ 規格 p9 之 2 行**牴觸**」
  改為「矩陣 17 格 ＋ 規格 p9 之 2 行**未對照（條件已證互斥）**」。
- **`DR-PMH5` 之第三問已由量測回答** —— 其欄為 `OFF`。
  該問**保留於 DR 中供上游確認**，惟已附本量測之答案。
- **R-PMH89（規格內部之牴觸）之條文不撤銷** —— 其判準與處置方式仍然有效；
  **只是本 feature 目前沒有它的實例了。**

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
