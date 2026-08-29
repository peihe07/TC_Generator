# 上繳包 07 — 解封、佔位回收、005／009／scroll／tune（2026-08-29）

對應下放包：`docs/handoff/07_unblock_and_recovery.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `c0e73a188501ec3cac7ce5c233a64fa857864632c1e2567234ec30480db68341`**
—— 與執行層自身記錄相符，未停。

**下放包 06 已作廢**（§0 明令），本包未依 06 執行任何作業；`06_placeholder_recovery_and_unlock.md`
保留不刪、標題未改，且**未納入上一次 commit**（刻意留為未追蹤，避免歷史看起來像已執行）。

**禁區遵守**：git 全數未執行；分析層四簿與 `ANALYSIS_LOCK.md`、`docs/handoff/**` 一字未寫；
未以 `<Tpress> = 500 msec` 組任何短／長按 TC；**`$TGW_DISP_STAT$` 12 處佔位未動**
（先決問題不成立，§4）；未引用 §1.5.1／§1.11.1／§1.14.1 之定義塊；
`ledger_guard.py` **只改作業 A 所令之掃法**，未順手改其他判準。

**並行執行**：作業 C／F／H 以三個並行執行層實例進行，可寫檔集合互斥；A／B／D／E／G 由主實例執行。

---

## §0 量測基礎

沿 upstream-05 §0 全部。另：符號一律搜 `<符號>` 與 `<符號>\s*=` 二式（R-ICS24(f)）；
DBC `latin-1`、邊界由下一個 `BO_`（A-ICS25）；PDF 去連字號＋壓平二式（A-ICS32）；
佔位以 `pending_census.py` 計數（A-ICS31，本包擴及 b05）；台帳掃描依作業 A 之新掃法。

---

## §1 裁決指紋（R-ICS1 ~ R-ICS30）

**33 錨點**（相異 30）。R-ICS1 ~ R-ICS21 與 upstream-04／05 逐項相同。

| 條 | sha8 | 條 | sha8 |
|---|---|---|---|
| R-ICS1 | `3e48552b` | R-ICS16 | `4d0eb301` |
| **R-ICS2 v1** | `4a8819f0` | R-ICS17 | `ed8d8f0c` |
| R-ICS3 | `b10318e0` | R-ICS18 | `ab6dc8ea` |
| R-ICS4 | `85de9871` | R-ICS19 | `1c841773` |
| R-ICS5 | `e6a4790d` | R-ICS20 | `b0e7170f` |
| R-ICS6 | `77478a91` | R-ICS21 | `bf7ae107` |
| R-ICS7 | `2c51cc80` | **R-ICS22 v1** | `f833c29d` |
| R-ICS8 | `bf473e9c` | **R-ICS22 v2** | `acfaff43` |
| R-ICS9 | `7e7aa921` | **R-ICS23 v1** | `d8d41b4a` |
| R-ICS10 | `a2cda337` | **R-ICS23 v2** | `997ae0ba` |
| R-ICS11 | `e16c88e3` | **R-ICS24** | `2cf6622a` |
| R-ICS12 | `558acc83` | **R-ICS25** | `eea2b263` |
| R-ICS13 | `273e1dbb` | **R-ICS26** | `f282ce2d` |
| **R-ICS2 v2** | `b6ddfe90` | **R-ICS27** | `8e301377` |
| R-ICS14 | `6f9e4686` | **R-ICS28** | `4857e29c` |
| R-ICS15 | `545928c0` | **R-ICS29** | `ff733567` |
| | | **R-ICS30** | `ac7b99ef` |

### 1.1 二條 sha8 不符 —— 依 R-ICS19(b) 取圍籬 diff，**未停**，但揭出一個程序缺口

| 條 | upstream-05 所載 | 本包實測 | 圍籬 diff | 處置 |
|---|---|---|---|---|
| R-ICS22 v1 | `81ac21cd` | `f833c29d` | **0 行**（與 commit `4c8e9bb` 之同名條文逐字相同）| **不停**（R-ICS19(b)）|
| R-ICS23 v1 | `57bc646f` | `d8d41b4a` | **4 行**（全為新增之 ⚠ 註記）| **不停**，理由見下 |

R-ICS23 v1 之 4 行 diff 逐字為：
```
⚠ **(a) 之事實描述有誤，已由 R-ICS23 v2 更正（2026-08-29）**；
結論（本 feature 不驗短長按）不變。(b)(c)(d) 仍為現行。
依 R-TM13 不刪不改字；指紋變動依 R-ICS19 處理。
```

**程序缺口（本包所揭）**：R-ICS19(b) 令「diff 非 0 行 → 條文已變，停下」，
而 R-ICS19(d) 令「本條之適用限於**改題與作廢註記**所致之指紋變動」。
本次之 4 行**正是作廢註記**，卻因**寫在圍籬之內**而使 (b) 之機械判準判為「條文已變」。
—— **R-ICS19(b) 之圍籬 diff 程序，預設註記寫在圍籬外。** 本包依 (d) 之實質判斷不停，
並具名此缺口（§9-4）：或令註記一律寫在圍籬外，或令 (b) 之 diff 排除註記行。

### 1.2 前提驗證 —— **P1～P4 全部相符**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | 相異 30、錨點 33 | **相異 30、錨點 33** | 相符（分析層自算而未經工具驗，本包實測與之一致）|
| P2 | A-ICS 至 45；DR 主登記表 17 列、相異 17、無缺口 | A-ICS **45**／相異 45；DR **17**／相異 17／無缺口 | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |
| P4 | CFTS022 26PI2.5 ＋ CFTS020 26PI1.5 Mar Release-Cabin | 二者皆在 `inputs/` | 相符 |

**P4 之檔名差異具名**（下放包 §0 明令）：CFTS020 之實體檔名為
`R1LR_Atl-H_26PI1.5 **Mar Release-Cabin**_CFTS_020 ICS and DCSD _20260310-1533.docx`，
而下放包 02～05 皆書近似之 `Feb Release` 式。**以實體檔名為準**；
本包所有引用皆用實體檔名。CFTS022 新版實體檔名為
`R1LR_Atl-H_26PI2.5 **Jun Release-Privacy**_CFTS_022 Functional Specification_20260608-1205.docx`。

---

## §2 作業 A — `ledger_guard.py` 掃法修正（解封）

依 R-ICS29(c)(d) 改三件，**只改掃法**：
1. **先剔除** `<!-- LEDGER-IGNORE-BEGIN -->`~`<!-- LEDGER-IGNORE-END -->` 區塊；
   剔除時以**等量換行取代**，保住原檔行號。
2. 於剩餘文本取登記列。
3. **合併列不計入**：判準為「首格去頭尾空白後**須恰等於**該編號」。

**docstring 已同步更新**，並於其中載明：舊 docstring 自稱「不掃內文引用」而舊實作為全檔取首格，
**該自稱與實作之不一致即 b06 封鎖事故之根**（A-ICS45）。

### 2-1 A-ICS45 之差額解釋，本包實測證實

分析層記「執行層報 11 筆、分析層實測 10 筆，差額為合併列」。本包逐行定位證實：
`| DR-ICS2、3、4、6、9、11、14 |` 一列，其首格為 `DR-ICS2、3、4、6、9、11、14`，
被舊之寬鬆正則 `^\| (DR-ICS\d+)` 讀為 `DR-ICS2` —— **11 = 真重號 10 ＋ 該合併列 1**。
新掃法下該列印為「合併列（不計入）」。

### 2-2 作業 A 後 `ledger_guard` **exit 0**（解封）

```
剔除 LEDGER-IGNORE 區塊 0 個；合併列（不計入）0 列 → A-ICS 登記列 45／相異 45／無缺口
剔除 LEDGER-IGNORE 區塊 1 個；合併列（不計入）0 列 → DR-ICS 登記列 17／相異 17／無缺口
錨點總數 33（相異 30）；R-ICS2／R-ICS22／R-ICS23 各 v1／v2 並存（合法）
總判：OK
```

（合併列於新掃法下顯示為 0 —— 因該列落在 `LEDGER-IGNORE` 區塊內，先被剔除。
二道防線各自有效，此為實測所得，非設計時所預期。）

---

## §3 作業 B — 符號值佔位回收 ＋ 節前定義塊全面掃查

### 3-1 六處回填（R-ICS27(b)(c)），錨各增 `CFTS020-4819541`

| TC | 欄位 | 原佔位 | 回填值 |
|---|---|---|---|
| I1（b02）| test_procedure | `DR-ICS10 <Tstuck_button value>` | **`120 seconds`** |
| I2（b02）| test_procedure | 同上 | **`120 seconds`** |
| V3（b01）| pre_conditions | `DR-ICS12 <detent counting time window>` | **`50 msec`** |
| B5（b04）| pre_conditions | 同上 | **`50 msec`** |
| B1（b04）| pre_conditions | `DR-ICS12 <no-change resend period>` | **`20 msec`** |
| B2（b04）| pre_conditions | 同上 | **`20 msec`** |

錨行排序依 IN §10.7：同文件內 ID 升冪，跨 CFTS 文件依文件號升冪
（例：V3 為 `CFTS020-4819541` ⏎ `CFTS022-4914975`）。

**`50 msec` 之 `initial value` 保留字已入 reasoning**（R-ICS27(c)）：
原文標 `parameter tuning process`，回填後其值仍為暫定，
故 **DR-ICS12 不結案**，改為「請上游確認調校後之定值」之追蹤件。

**副效具名**：`<TPeriodToSendNoChange> = 20 msec` **遠小於** B1／B2 所用之 2 秒觀察點 ——
upstream-04 §10-2-2 所具名之「觀察時點可能錯」之風險，至此實測為**不成立**。

### 3-2 節前定義塊全面掃查（R-ICS27(e)）

`scripts/predef_sweep_07.py`（新腳本，操作型定義與五組型樣寫於其檔頭）：
**2180 物件中候選 35，其中判適用者 6**。
工具自檢：`4819541` **命中**（若未命中即表示工具失效）。全文相異賦值符號 **14 個**。

**新揪出之適用候選二則**（前七包未讀）：
- **`4819628`（§1.8.2.1）／`4821013`（§1.15.3）**：逐字宣告 `$DCSD_DISP_STAT$` 之
  **valid values** —— 而 **b03 之 Pre-Condition 正引用該狀態**（`The DCSD screen is in
  the "DCSD Screen ON" state`）。該狀態之合法值域至今未被讀入。
- **`4819626`（§1.8.2）**：另一組時間變數（`<TBackChnlSend> = 20 msec` 等），DCSD 側。

---

## §4 作業 C — **E3 觸發，`ETM = DUT` 不成立**，12 處佔位維持

三路交叉逐路所據（`docs/reports/07_etm_dut_crosscheck.md`）：

| 路 | 結果 |
|---|---|
| **SYSAD** | 大小寫敏感掃 `ETM`／`LTM`／`SGW`／`TBM`／`node`／`DBC` → **0 命中**。縮寫表載 `TLM / Telematics Module`（**不是 ETM**）；系統分解表示 **TLM 為接收 DUT 輸出之他方 ECU**，方向與「ETM = DUT」**相斥** |
| **SWRA** | 三分頁全掃，`ETM`／`LTM`／`SGW`／`TBM` **各 0 命中**（子字串計數 `{'ICS':87,'HU ':2,'TGW_DISP_STAT':2,'Telemat':1}`）。通篇無任何 DBC 節點名 |
| **LID** | `TGW_DISP_STAT` 在列 2084，`CAN Mapping` **全欄無 Sender／Node 欄**；唯一 `ETM` 提及在 `Rev History` r98，談 `$EBL_Stat$`，與 DUT 識別無關 |

**決定性反證（母文件屬性軸，87 個單一-ECU 物件實測）**：
`LTM` 專屬者 **28 個全帶 `R1L`／`R1L-R`** 且無一帶 `R1M`／`R1H`；
`ETM` 專屬者 **59 個全帶 `R1M`／`R1H`** 且無一帶 `R1L`／`R1L-R`；**違例 0**。
本 DUT 為 R1L-R → 其 ECU 為 **`LTM`**，非 `ETM`。
且 CFTS022 之 Notation Convention 明列 `RRM, LTM, ETM, ICS` 為**四個不同 acronym**。

**三路皆未提供任何支持所據，而母文件屬性軸提供明確反證 → 判「不成立」而非「不足」。**

### 4-1 比原先設想更大的缺口（作業 C 附帶所揭）

1. **若 DUT 節點名為 `LTM`，則二 DBC 中根本沒有 `$TGW_DISP_STAT$` 之 DUT 發送側**
   —— FDCAN8 之 `BU_:` 宣告了 LTM 卻**發送 0 則**，BHCAN 無 LTM 節點。
   R-ICS22 v2(a) 之「取 DUT 自身為發送者之那一條」**在現有 DBC 上無對應物**；
   備援側（SGW）亦非 DUT。
2. **R-ICS22 v2 前言之「LTM 發送 0 則」量測為真，但其推論可反轉**：
   較合理之解讀為「該 DBC **未涵蓋 R1L／R1L-R（LTM）變體之發送側**」，
   而非「所以 DUT 是 ETM」。
3. **`Telematic_Power` 於二 DBC 全文查無**（`latin-1`、不分大小寫、三變體），
   R-ICS22 v2(b) 後半句缺實測基礎。

---

## §5 作業 D — **二條全數未生成**，二個不同機制各擋一條

### 5-1 009：其指定錨 `CFTS020-4819554` 依 R-ICS2 v2 判**不適用**

```
4819554  §1.8.1.1  Subsystem Functional Requirement  不適用
  Radio = ['VP4R84', 'VP384', 'VP484'] ∩ {R1L, R1L-R, allSys} = ∅
  EE    = ['PowerNet']                ∩ {Atlantis High, All}  = ∅
```
**二軸皆實值落空（非軸缺）。** R-ICS25 係以 **Market 軸**（NAFTA 在案）解鎖 009，
而 Market 於 R-ICS2 v2 之判準中**不是判準軸** —— 該物件在 Radio 與 EE 兩軸即已出局。

**已盡之查證**：全文含 `Back_Button` 之物件 **7 個**，判適用者僅 **2 個**
（`4821681` 為 LID 指向、`4821704` 主詞為 **TLM**），
**無一為 HU／ICS 側之 Back 行為母條**。
故依「判不適用即停下回報、**不得改錨他物件**」停下 —— 改錨至 TLM 條文即換一個 ECU 之行為。

### 5-2 005：作業 F 報 **E4 觸發**，但不符純為排序

| 覆驗項 | 結果 |
|---|---|
| 四句 verbatim（4914956／57／75／76）| **4/4 位元級相同**（連彎引號皆同）|
| 七物件三軸逐字（含列舉順序）| **0/7 相符** |
| 七物件三軸**值集合** | **7/7 相同** |
| v2(a) 判定 | **7/7 未改變**（全部「適用」）|
| `4914993` 本文 | **位元級相同**；三軸 `ECU = LTM, ETM`／`Radio = R1L, R1M, R1L-R, R1H`／`EE = All` → **判適用** |

**不符全部出在多值屬性之列舉順序**（如 `ECU: A, B` → `B, A`），
**無任何值之增、刪或改字**。全域佐證：新舊版共 336 物件，
三軸字串相異者 271 個，而**值集合真的變動者只有 5 個**（4914928／30／4914983／84／4915132），
本次七錨**不在其中**。

E4 之字面為「任一屬性不符即停」，而正規化五項**不含列舉順序** ——
**E4 因此在一個內容零變動之情況下觸發**。判準解釋屬分析層，執行層停下不自裁（§9-2）。

**另具名**：`4914993` 之 `Model Year` 由 `2025, 2023, 2024` 改為 `Default`
—— 不在三軸覆驗範圍，但**是本輪唯一真的改了值的屬性**。
另新版有 **28 個物件之本文逐字變動**（本次四錨七錨皆不在其中），改綁後屬「來源已變」。

### 5-3 改綁已完成（作業 F 之另一半）

`feature.yaml` 之 `paths.cfts022_fs` 與 `reference.cfts022_fs` 已改指本 feature `inputs/` 之
26PI2.5 版（sha256 `7acfa462…` 自實體檔算），**舊綁定路徑與舊 sha256 留記於註解供回溯**；
**privacy 之綁定未動**。

---

## §6 作業 E — scroll／tune 已生成（b05，2 條）

| # | tc_title | req_id | Test Set | 錨 | priority |
|---|---|---|---|---|---|
| — | Knob 2 rotated on a scrollable screen | SWE-ICS-004 | Browse Control | CFTS020-4819586 | P1 |
| — | Knob 2 rotated on a tuner source | SWE-ICS-004 | Browse Control | CFTS020-4819586 | P1 |

依 R-ICS30(a)：三操作同錨於 4819586（其原句同時載 Browse／Scroll／Tune），
畫面對應以 `PENDING: DR-ICS6` 承載，**未以 DR 未回為由不生成**。

**批號說明**：b01~b04 對應下放包 01~04；下放包 05 為補正、06 作廢，二者未新增 TC，
故本輪之新 TC 落 **b05**。**批號與輪次自此不同步**，已記於 `b05/manifest.json`。

---

## §7 作業 G — 未錨定斷言檢查（`docs/reports/07_pre_delivery_check.md`）

**ER 行總數 118**（25 條 TC）：**已錨 84／已標明（乙類）6／非斷言（記錄行）21／未錨定 7**。

判準、規則（R1~R7）與例外表**全部寫在 `scripts/gen_pre_delivery_07.py` 檔頭與常數表**，
可逐行覆核 —— **這是人工判，不偽裝成機械輸出**。

### 7-1 【E6 觸發】未錨定斷言 **7 行**，逐行具名，**未自行刪改**

| TC | ER 行 | 族 |
|---|---|---|
| B3 `Knob 2 held stationary` | 4 | (i) 不作為之可觀察化 |
| I1 `Press ignored during stuck condition` | 5 | (i) |
| I2 `Button responsive after release` | 5 | (i) |
| B6 `Knob 2 signals acted on by the HU` | 4 | (ii) `if any` 之逾越 |
| Scroll `Knob 2 rotated on a scrollable screen` | 4 | (ii) |
| Tune `Knob 2 rotated on a tuner source` | 4 | (ii) |
| N1 `Enter button pressed` | 4 | (ii) |

**兩族之性質不同：**
- **(i) 不作為之可觀察化**：來源句說「忽略」「no action taken」，TC 以「狀態不變／改變」承載。
  來源句**未承諾**該不作為必有可觀察之無變化。
- **(ii) `if any` 之逾越**：`4819555`／`4819586` 之原句**自帶 `if any`**，
  即規格明示可能無對應後果，而 TC 斷言必有可觀察之差異 ——
  **此四行為潛在 False Fail**（IN §7）。
  R-ICS30(b) 已裁「目標畫面未具名維持現狀」，但**該裁定治的是「不得自行指定畫面名」，
  未治本行之斷言逾越** —— 二者不是同一件事。

---

## §8 作業 H — Notifications 偵察（`docs/reports/07_notifications_recon.md`）

| 項 | 實測 |
|---|---|
| 檔名 | `Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf`（與下放包逐字一致；`sources/` 共 33 件）|
| 頁數 | **6**（`pdftotext` 與 `pdfplumber` 一致）|
| 文字層 | **有**，6/6 頁（二工具逐頁非空白字元數完全相同）|
| sha256 | `599f4ff680533099…` |

### 8-1 **不支持**其為 `Pop-up List Notification`（證據評估，非裁定）

- **自稱**：封面逐字 `R1L-R Notifications` / `HMI Logic and Flow`；全文掃三變體 **0 命中**
- **結構不對應**：無逐項 pop-up 清單；`timeout`／`duration`／`dismiss`／`priority`／
  `Cat.`／`X button`／`5 sec` **全數 0 命中**
- **決定性反證 —— 本本反向外指**：p.2 `Document Related Content` 列 `HMI Pop Up List — Pop Ups`；
  p.3 二處逐字「Notifications are popups that get stored (when applicable).
  **See HMI Popup List.**」→ **本本自認 pop-up 清單在別本，該本名為 `HMI Pop Up List`，
  不在 33 件內**

### 8-2 `VOLUME POP_UP` **查無**，**E5 未觸發**

四變體 ＋ 寬鬆 regex，於四式正規化（raw／去連字號／壓平換行／全壓平）逐頁逐式掃 → 0 命中。
**單詞 `volume` 全文 0 命中** —— 既然該詞於 6 頁完全不出現，任何斷行變體皆不可能潛藏。
**至此 `spec-index/sources/` 內已無未掃之候選。**

A-ICS32 於本本**再度應驗**：`Notifications HMI` 只在**壓平換行式**命中（封面二詞分屬兩行、無連字號）。

---

## §9 預期數字對照（下放包 §5，15 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | 作業 A 後 `ledger_guard` | exit 0；DR 17／45 | **exit 0**；DR 17／相異 17、A-ICS 45／相異 45 | 相符 |
| 2 | 錨點 | 相異 30、總數 33 | **相異 30、總數 33** | 相符 |
| 3 | DR-ICS10 佔位 | 2 → 0 | **2 → 0** | 相符 |
| 4 | DR-ICS12 佔位 | 4 → 0 | **4 → 0** | 相符 |
| 5 | `$TGW_DISP_STAT$` | 先決不成立 → 12 不變並停報 | **不成立；12 不變**（§4）| 相符 |
| 6 | 005 之 TC | ≥ 1 | **0**（E4 觸發，§5-2）| **不符** |
| 7 | 009 之 TC | ≥ 1 | **0**（錨判不適用，§5-1）| **不符** |
| 8 | scroll／tune 之 TC | ≥ 2 | **2** | 相符 |
| 9 | Test Set 相異值 | 5，不變 | **5** | 相符 |
| 10 | CFTS022 覆驗 | 4 句 ＋ 7 物件全數相符 | 四句 4/4 位元級相同；七物件三軸逐字 0/7、集合 7/7、判定 7/7 未變 | **不符（純排序）** |
| 11 | 未錨定斷言 | 逐條有判；已標明與未標明分列 | 118 行逐行有判；已標明 6／未錨定 7 | 相符 |
| 12 | 作業 H | 一節；TC 新增 0 | 一節；**0** | 相符 |
| 13 | 節前定義塊掃查 | 出清單 | 候選 35／適用 6；新揪出 2 則 | 相符 |
| 14 | `ledger_guard` 完工後 | exit 0；與作業 A 後比對 | **exit 0，逐字相同（`diff` 0 行）** | 相符 |
| 15 | 四支 gate | 差皆 0 | 差皆 0（`lint_paths` 基線外 2，皆 `driver_distraction`）| 相符 |

**不符 3 項（#6／#7／#10），皆不自行調和**，理由分見 §5-1／§5-2。

---

## §10 DR 狀態實測表（下放包 §7-5 明令；對主登記表 17 列逐條）

| DR | 授權狀態 | 本包是否已回收其全部佔位 | 實測 |
|---|---|---|---|
| DR-ICS1 | 降為帳面修正件 | — | 005 未生成（E4），其阻斷面**未如預期歸零** |
| DR-ICS2 | 維持 OPEN | — | 011／012 仍無 TC |
| DR-ICS3 | 維持 OPEN | — | 無新事實 |
| DR-ICS4 | 維持 OPEN | **否**，1 處佔位（V3）| 五包＋本包確認答案不在 repo |
| DR-ICS5 | 可結 | 無佔位 | **確可結**（檔在 `inputs/`，R-ICS9 已採用）|
| DR-ICS6 | 維持 OPEN | **否**，**4 處**佔位（B6／Scroll／Tune／N1）| 本包新增 2 處（scroll／tune）|
| DR-ICS7 | 可結 | 無佔位 | **確可結**（120 s 三源互證，本包再證第三源 `4819541`）|
| DR-ICS8 | 可結 | **否**，**12 處**佔位（`$TGW_DISP_STAT$`）| **不可結** —— 作業 C 判 E3，先決不成立 |
| DR-ICS9 | 維持 OPEN | — | 作業 C 之 87 物件實測**支持 DUT 之 ECU 為 `LTM`**，可供其收窄之參考 |
| DR-ICS10 | 可結 | **是**，2 處已回填 | **確可結** |
| DR-ICS11 | 維持 OPEN | — | `SIS-5161` 仍不在 repo |
| DR-ICS12 | 可結 | **是**，4 處已回填 | **不宜結**（R-ICS27(c)：`50 msec` 為 initial value，改追蹤件）|
| DR-ICS13 | 可結 | — | **不可結** —— 009 之阻斷面非 Market 而是 Radio／EE（§5-1）|
| DR-ICS14 | 維持 OPEN | — | 無新事實 |
| DR-ICS15 | 可結 | — | 2 解、2 併入 DR-ICS16，**確可結** |
| DR-ICS16 | 降為確認件 | — | **應升回阻斷件** —— 作業 C 判 ETM 不成立，12 處佔位無解（§4-1）|
| DR-ICS17 | 待 b06 偵察 | — | 作業 H 完成：**不支持**候選本，線索移轉至 `HMI Pop Up List`（不在 repo）|

**全批佔位 21 → 17**（回收 6、新增 2）。**b07 後已無「待回填」態之佔位**（R-ICS27(d)）——
現存 17 處全為「缺值」態。

---

## §11 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `ledger_guard` 掃法＋docstring；六處符號佔位回填與錨增；節前定義塊掃查；scroll／tune 2 條；CFTS022 改綁；未錨定斷言檢查與新體檢報告；`predef_sweep_07.py`／`gen_pre_delivery_07.py`／`etm_probe_07.py`／`cfts022_reverify_07.py`／`src_recon_07.py` 五支新腳本；`pending_census.py` 擴及 b05 |
| **核實無誤** | A-ICS45 之 11／10 差額（本包逐行證實為合併列）；R-ICS22 v1 圍籬 diff 0；四句 verbatim 位元級相同；七物件值集合與 v2 判定未變；`4914993` 判適用；`4819541` 為掃查工具之自檢命中 |
| **正確地不動** | `$TGW_DISP_STAT$` 12 處未動（E3）；009 未生成且未改錨（§5-1）；005 未生成（E4）；7 行未錨定斷言未刪改（E6）；未以 `<Tpress>` 組短長按 TC；未引用其餘三份定義塊；`ledger_guard` 只改掃法；分析層五簿一字未寫；未自取任何 A-／DR- 編號 |

---

## §12 待分析層裁定

1. **【最重】`$TGW_DISP_STAT$` 之出路（§4、§4-1）**：`ETM = DUT` 不成立，
   且若 DUT 為 `LTM`，**現有二 DBC 中根本無其發送側**。
   12 處佔位、Display 面 8 條之訊號面**在現有素材下無解**。
   DR-ICS16 建議**自「確認件」升回「阻斷件」**。
2. **E4 之判準補充（§5-2）**：多值屬性之比對以**逐字**或以**集合**？
   本次不符純為排序、內容零變動而 E4 觸發。補此一條後 005 即可生成。
3. **009 之出路（§5-1）**：R-ICS25 以 Market 軸解鎖，而實際阻斷在 Radio／EE 二軸。
   ICS／HU 側無 Back 行為母條 —— 是向上游要條文，或裁定 009 出案外。
4. **R-ICS19(b) 之程序缺口（§1.1）**：作廢註記寫在圍籬**內**時，
   圍籬 diff 必非 0，使 (b) 之機械判準與 (d) 之適用範圍衝突。
5. **§1.18「ICS Management」之地位（§13-2）** —— 見獨立判斷。
6. **7 行未錨定斷言之處置（§7-1）**：(ii) 族之四行為潛在 FF。
7. `4914993` 之 `Model Year` 改值、新版 28 個物件本文變動（§5-2）是否登異常。
8. `4819628`／`4821013` 之 `$DCSD_DISP_STAT$` valid values 是否納入（§3-2）。

---

## §13 獨立判斷

### 13-1 【下放包 §7-6 之一】17 條 DR 全無回覆時，哪幾條可現狀出貨（以本包後之實況更新）

**可出貨 17 條／不可 8 條**（前次為 13／10，總數自 23 增為 25）。

**可（17）**：b03 全 8 條（R-ICS22(b) 明裁不因佔位阻出貨，主錨為 HMI 現象）、
b01 之 S1／S2／S3、b02 之 **I1／I2**、b04 之 **B1／B2**、B3（弱）、B4。

**不可（8）**：V1／V2／V3、B5、B6、N1、Scroll、Tune。

**本包造成之變動有三：**
- **I1／I2 由「不可」轉「可」** —— 門檻已回填 `120 seconds`，台架可執行。
  其 ER 之「不作為」問題仍在（§7-1 之 (i) 族），屬**弱驗證**而非不可出貨。
- **B1／B2 由「不可」轉「可」** —— `20 msec` 已回填，且遠小於 2 秒觀察點。
- **B5 仍「不可」** —— `50 msec` 標 `initial value` 且待調校：**回填不等於定值**。
- 新增之 **Scroll／Tune 為「不可」** —— 主錨即 `PENDING: DR-ICS6`，
  且屬 §7-1 之 (ii) 族（`if any` 之潛在 FF）。

**最須留意者仍是 V1／V2** —— 無佔位而不可出貨。其 popup 顯示條件經六包追索、
六本 HMI L&F 掃遍，**本包確認 `spec-index/sources/` 內已無未掃之候選**。

### 13-2 【本包最重之附帶發現】§1.18 —— 一個七包未讀而與本 feature 同名之章節

追 009 之 `Back_Button` 時撞到：

```
1.18        Functional Requirements - AtlMi & AtlHi & AtlLo - ICS and Associated HU  {4821673}
1.18.1      ICS Management            {4821674}   ← 與本 feature 同名
1.18.1.1.2  Push Button Data Transfer {4821680}
1.18.1.1.3  Rotary Knob Data Transfer {4821690}
```

**37 個物件，29 個判適用。** 前七包全部錨在 §1.8（`PNet & AtlHi & AtlMi`），
而 §1.18（`AtlMi & AtlHi & AtlLo`）**同樣涵蓋 Atlantis High**。

**它比 §1.8 講得更具體：**
- `4821688` 逐字：`ICS shall send all the relative BH-CAN signals in **CLIMATIC_PANEL message**`
  —— **規格自己點名了 `CLIMATIC_PANEL`**，而那正是 b02／b03 靠 LID→DBC 才推出來的訊息名；
  §1.8 從頭到尾未點名。
- `4821694`／`4821696`／`4821697` 之旋鈕條文直接以
  `"Knob_no_change"`／`"Knob_increment"`／`"Knob_decrement"` 為引號值
  —— **與 DBC 之 `VAL_` 字面完全一致**。

**即：b02～b04 之訊號解析結論是對的，但我們是繞遠路推出來的，而規格裡本有直說的一節。**
哪一支為本 DUT 之權威（§1.8 vs §1.18）屬範圍問題，**本包不裁、不改錨**。

### 13-3 【下放包 §7-6 之二】未錨定斷言檢查是否應成為每包必跑之常設項

**應，但須分兩層，且不宜全機械化。**

- **可機械化者應入常設**：ER 行對「其 TC 之 `specification_reference` 所錨物件之本文」
  之詞彙涵蓋度（例如 ER 出現而來源句未出現之實詞），可作為**候選篩**每包必跑。
  它抓不到「未錨定」，但抓得到「明顯逾越」，且成本近零。
- **判斷本身不可機械化**：本包七行之所以判為未錨定，靠的是讀出
  `if any`／`no action taken` 這類**語意保留**，正則抓不到。
  故常設項應為「**候選篩每包必跑 ＋ 判斷每包人工複核**」，而非把判斷交給腳本。
- **理由**：本包之七行中有四行是潛在 FF，而它們**全數通過了 19 項機檢與逐字比對**。
  外觀完整、機檢全綠、逐字命中 —— 而其 ER 可能永遠判不出對錯。
  **這正是機檢抓不到的那一類**，也正是它值得每包花人工的理由。

---

## §14 未結 DR 與引用清單

**DR-ICS1 ~ DR-ICS17，17 條全開**（狀態實測見 §10）。

引用：R-ICS1 ~ R-ICS30（sha8 見 §1）；
A-ICS16、A-ICS25、A-ICS28、A-ICS29、A-ICS30、A-ICS31、A-ICS32、A-ICS34、A-ICS35、A-ICS41、
A-ICS42、A-ICS44、A-ICS45；DR-ICS1 ~ DR-ICS17；
R-G13、R-G23、R-G25；R-DD3 同族、R-DD25(a)、R-DD26 v2；R-TM13；R-4；R-6；R-S4；
FO §8.2、FO §8.4、FO §8.5、FO §8.8；
IN §4.3.1、IN §4.4、IN §5.5、IN §7、IN §8.2.1、IN §8.2.2、IN §8.4.1、IN §8.4.3、
IN §9、IN §10.7、IN §11、IN §12。

**本包未產生任何新裁決條文，亦未自取任何 A-／DR- 編號。**
建議登錄之 anomaly 五則（編號由分析層取）：
§1.1（R-ICS19(b) 之圍籬 diff 於註記寫在圍籬內時失效）、
§4-1（DUT 若為 LTM 則二 DBC 無其發送側）、
§5-2（E4 於內容零變動時因列舉順序觸發；`4914993` 之 `Model Year` 改值；新版 28 物件本文變動）、
§7-1（7 行未錨定斷言，其中 4 行為 `if any` 之潛在 FF）、
**§13-2（§1.18「ICS Management」七包未讀，且其條文較 §1.8 更具體）**。
