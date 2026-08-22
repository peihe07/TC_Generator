# ANOMALIES — FW036 Power Moding HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PMHnn]`（R-PMH3(b) —— 本 feature 之異常前綴為 `A-PMH`，
不與 `features/power` 之 `A-PW` 共用序號）。PENDING entries block their batch
until a Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

## A-PMH01 — 037 `FROP` 相異值：分析層 13、執行層實測 12 · PENDING

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

**提案處置**（不裁定）：
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

---

## A-PMH05 — 雜湊檔本身未入版控，與 §9.1 通則 9 衝突 · PENDING

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

**提案處置**（不裁定，且**本包未動 `.gitignore`**）：
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
