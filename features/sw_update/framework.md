# framework.md — SW Update

狀態：**分層效力（R-SU18，Pei 2026-08-28 裁丙）** ——
**Layer 1 定稿**／**Layer 2 全定稿（21 組，311 列，三重閉合全過）**／
**Layer 3 PROVISIONAL**。
Feature slug：`sw_update`
規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、
FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）、
R-SU1／**R-SU10 v2**／R-SU18／**R-SU19**

> **素材欄位全覽**（R-SU26）另存 **`SOURCE_COLUMNS.md`** ——
> 其射程為來源檔之欄位，非本檔之三層框架，故不並入本檔。
> 現況：58 欄中已用 27／不用 7／**未定 24**。

---

## 效力分級（R-SU18(d) 之揭露義務）

| 層 | 效力 | 進工作簿 | 變更成本 |
|---|---|:--:|---|
| **Layer 1**（Test Group） | **定稿** | ✅ | 須 Pei 裁 |
| **Layer 2**（Test Set） | **全定稿**（21 組，**無 provisional 列**） | ✅ | 須分析層裁並記依據；已寫回者視同修訂 |
| **Layer 3**（spec 章節分群） | **PROVISIONAL** | ❌（IN §4.1.5） | 階段二逐列人裁時就地修正，不須另發裁決；須記於該列 `reasoning` 並回寫本檔 |

> ⚠ **R-SU18(c) 之拘束**：Layer 3 之 provisional 狀態**不得外溢至
> `specification_reference`**。後者一律走階段二之逐列裁定（R-SU14 v5），
> **不得以 Layer 3 之章推定其錨**。
> 二者為導航與交付面之別 —— Layer 3 錯了只是導航繞路，
> `specification_reference` 錯了是交付缺陷。

## 觀測面來源之覆蓋（T42d，下放包 29）

> **T42d(iii) 令「`framework.md` 之 DR 註記同步」—— 本檔原無任何 DR 註記**
> （全檔 `DR-SU` 命中 0）。故本節為**新增**，非同步；
> 其射程限於「哪些 Test Set 因 `Error_Code_List.xlsx` 而有了觀測面來源」。

**Pei 裁 `Error_Code_List.xlsx` 可用**（R-SU35，2026-08-28）後，
下列 Test Set 之**負向路徑**有了具名之觀測面來源。**正向路徑不受影響**（R-SU35(d)）。

| Test Set | 對應階段（R-SU35(a)） | 碼數 | 覆蓋之路徑 |
|---|---|---:|---|
| `USB Update` | Precondition | 7 | **負向**（USB／SWDL） |
| `Integrity Verification` | Package Header check & unpack／Security check | 17 | **負向** |
| `Update Agent` | Rollback Protection | 3 | **負向** |
| `Interruption Handling`／`Update Agent` | Install（M-CPU／Redbend／V-CPU） | 31 | **負向** |
| （不用） | Install ( SXM ) | 17 | 非本 feature 範圍 |
| **— 未載** | `After HU start-up, suddenly`／`RedBend update engine` | **5** | **R-SU35(a) 無對照，待裁** |

**三項拘束須隨本表一併讀**：

1. **本表為 USB／SWDL 路徑**（R-SU35(c)1）—— `Wi-Fi Download`、`Silent Update`
   等 Wi-Fi FOTA session 之組**不得引用**，其正向狀態觀測仍為 DR-SU2 v2(b)。
2. **碼有了，看碼的地方還沒有**（R-SU35(b)3）—— 錯誤碼於 HU 上之呈現途徑為
   DR-SU2 v2(a) 之未解項；未答前觀測步驟掛 `PENDING: DR-SU2`。
3. **本表不改 Layer 2 之切分** —— 其為各組之材料供給狀態，非分組依據。
   以「某組有無錯誤碼」回頭調整分組即為循環（R-SU20(d)）。

詳見 `ERROR_CODES.md`（80 碼）與 `DATA_REQUESTS.md` 之 DR-SU2 v2。

---

**Layer 3 於 2026-08-28 之覆蓋狀態**：

| | 值 |
|---|---:|
| 21 組中有 **GT** 支持者 | **8 組 / 21** |
| 21 組中有值但非 GT（推定／標題重疊） | 2 組 / 21 |
| 21 組中 TBD 者 | 11 組 / 21 |
| 逐列已裁者（GT-A1 28 + GT-B 4） | **32 / 311（10.3%）** |
| PROVISIONAL（未裁之列） | 279 / 311 |

---

## Part I — Layer 1（Test Group）—— 定稿

```
SW Update
```

依 IN §4.1.1 與 **R-SU1**：Layer 1 = feature 名。
037 檔名作 `SoftwareUpdate`、SYSAD 作 `Software Update`、CFTS 母件為
CFTS_57 Reflash —— 交付面統一取 `SW Update`（Pei 2026-08-27 裁定 Q6）。
依 **R-SU2** 之 `fill_test_group_set = true`，寫入工作簿 Test Group 欄，
全簿逐字一致。**變更須 Pei 裁**（R-SU18(a)）。

---

## Part II — Layer 2（Test Set，寫入工作簿）—— 全定稿

分群鍵為 **Heading id**；**跨章之 Heading 群，其鍵細化為
(Heading id, 037 列區間)**（**R-SU10 v2(a)**）。
本表逐組列出其所轄之 (Heading id, 列區間) 與該 Heading 之標題原文
（R-SU10 v2(c)），俾碰撞與跨章皆可見。
依 IN §4.2：英文名詞片語、不重複 Test Group 前綴、
**不設 `Misc`／`General`／`Unclassified`**（IN §4.1.3）。

### 切分原則

1. 分群鍵為 Heading id；跨章群細化為 (Heading id, 列區間)（R-SU10 v2(a)）
2. **跨章之 Heading 群必拆** —— 已實證者 `309`（7 組）、`170`（2 組）。
   **其射程為 Heading 群，不比照 R-SU19 及於 Test Set**（**R-SU21(a)**）
   —— Test Set 之跨章若出於「同一能力在規格中散於數章」，
   那是規格編排之事實，不是切分缺陷
3. 純 Service 群之健康判準為「共同觸發面與共同觀察面」
   （下放包 06 §3.3；IN §4.1.3 之 UI 入口路徑只在 17 個含 HMI 列之群成立）
4. **逾 40 列者須檢視其是否實為多能力，射程及於 Test Set**（**R-SU19**）
   —— 40 為檢視之觸發值，非上限
5. 不設 `Misc`／`General`／`Unclassified`（IN §4.1.3）
6. **孤島列檢查為正確性之最低機器化檢查，每次切分或變更後必跑**（**R-SU20 v2**）
   —— 三重閉合全屬**完整性**維度，不證明分得對。
   **評估範圍採 strict**：僅就群內部列評估（前後鄰皆存在且皆不同組者為孤島），
   群首／群尾／單列群不評估。
   ⚠ **已知盲區**：**本檢查不覆蓋群邊界之錯分** —— 位於 Heading 群首尾之列
   若被錯置，孤島檢查不會報警。**此為採 strict 之代價，非疏漏**（R-SU20 v2(a)）

### 定稿之 21 組（311 列，45 群）

| # | Test Set | 能力叢集 | 所轄 (Heading id, 列區間) | 列數 | HMI | Service |
|---:|---|---|---|---:|---:|---:|
| 1 | `Wi-Fi Download` | Wi-Fi 下載路徑：連線建立、經 Wi-Fi 之軟體下載、非關鍵更新 | (`SWE1-FOTA-038`, 全群)、(`SWE1-FOTA-055`, 全群)、(`SWE1-FOTA-058`, 全群) | 29 | 12 | 17 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：038 OTA download via Wi-Fi；055 Non-Critical Updates；058 Connection to Wi-Fi network | | | | |
| 2 | `Update Policy` | 更新之關鍵性政策：Critical／Regular／Silent 之分級與其套用 | (`SWE1-FOTA-009`, 全群)、(`SWE1-FOTA-024`, 全群) | 17 | 4 | 13 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：009 Critical Updates；024 Critical Updates | | | | |
| 3 | `Silent Update` | 靜默更新之執行與其通知限制 | (`SWE1-FOTA-170`, 175–177)、(`SWE1-FOTA-178`, 全群) | 9 | 2 | 7 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：170 Deployment Package Security；178 For a silent update, the OTA client follows these steps for the download | | | | |
| 4 | `Deployment Flow` | 部署流程本體（037 `137` 群） | (`SWE1-FOTA-137`, 全群) | 26 | 9 | 17 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：137 Deployment flow | | | | |
| 5 | `Session Flows` | 各類 session 之總覽與流程骨架 | (`SWE1-FOTA-018`, 全群)、(`SWE1-FOTA-168`, 全群)、(`SWE1-FOTA-185`, 全群)、(`SWE1-FOTA-188`, 全群)、(`SWE1-FOTA-271`, 全群)、(`SWE1-FOTA-278`, 全群)、(`SWE1-FOTA-287`, 全群)、(`SWE1-FOTA-016`, 0 列)、(`SWE1-FOTA-017`, 0 列) | 16 | 2 | 14 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：016 Session Flows；017 Deployment Flow；018 Installation and Download Conditions；168 Vehicle-Initiated Session Flow；185 OTA client sessions；188 User initiated sessions；271 OTA server initiated sessions；278 User initiated sessions；287 OTA client Flows | | | | |
| 6 | `Client Architecture` | OTA client 架構面：介面定義、匯流排、組態選項、車輛屬性、效能 | (`SWE1-FOTA-192`, 全群)、(`SWE1-FOTA-200`, 全群)、(`SWE1-FOTA-202`, 全群)、(`SWE1-FOTA-251`, 全群)、(`SWE1-FOTA-259`, 全群)、(`SWE1-FOTA-263`, 全群)、(`SWE1-FOTA-266`, 全群)、(`SWE1-FOTA-280`, 全群)、(`SWE1-FOTA-285`, 全群)、(`SWE1-FOTA-072`, 0 列)、(`SWE1-FOTA-073`, 0 列) | 35 | 4 | 30+1 blank |
| | | *Heading 標題原文*（R-SU10 v2(c)）：072 OTA Client Architecture；073 Operating Environment；192 Bus communications；200 OTA Client Configuration options；202 OTA Architecture Requirements；251 High Level FOTA Diagram；259 Vehicle Properties；263 OTA Architecture Requirements；266 OTA Client Configuration options；280 Interface Definitions；285 OTA Client Performance Requirements | | | | |
| 7 | `Bearer Selection` | 承載選擇：網路優先序組態與網路選擇 | (`SWE1-FOTA-291`, 全群) | 16 | 0 | 16 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：291 Bearer selection: | | | | |
| 8 | `ROV Installation` | ROV 安裝三階段：安裝前、安裝進度、安裝後 | (`SWE1-FOTA-086`, 全群)、(`SWE1-FOTA-091`, 全群)、(`SWE1-FOTA-096`, 全群)、(`SWE1-FOTA-085`, 0 列) | 20 | 16 | 4 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：085 FOTA ROV Reflash Requirements；086 Post-Installation；091 Installation Progress；096 Pre-Installation | | | | |
| 9 | `TBM Reflash` | TBM 自身之 FOTA reflash | (`SWE1-FOTA-110`, 全群) | 14 | 11 | 3 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：110 TBM FOTA Reflash | | | | |
| 10 | `HU FOTA via TBM` | HU 經 TBM 路徑之 FOTA | (`SWE1-FOTA-214`, 全群) | 36 | 20 | 16 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：214 HU FOTA with TBM | | | | |
| 11 | `USB Update` | 本地／媒體部署路徑（USB reflash） | (`SWE1-FOTA-078`, 全群)、(`SWE1-FOTA-020`, 0 列)、(`SWE1-FOTA-074`, 0 列)、(`SWE1-FOTA-076`, 0 列) | 5 | 0 | 5 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：020 Re-Flashing Requirements；074 Over The Air (OTA) Deployment of Software；076 Local Deployment of Software；078 Media Reflash Requirements | | | | |
| 12 | `Update HMI` | 更新之使用者體驗與 HMI 呈現 | (`SWE1-FOTA-129`, 全群) | 6 | 5 | 1 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：129 User Experience (UX)/HMI | | | | |
| 13 | `Configurable Parameters` | 可組態參數與 Download Descriptor 格式 | (`SWE1-FOTA-125`, 全群)、(`SWE1-FOTA-127`, 全群) | 2 | 0 | 2 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：125 Appendix B Configurable Parameters；127 Download Descriptor Format | | | | |
| 14 | `FOTA Overview` | FOTA 總覽層之需求 | (`SWE1-FOTA-001`, 全群) | 6 | 2 | 4 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：001 Firmware Over-the-air Updates (FOTA) | | | | |
| 15 | `Integrity Verification` | 驗證與加密：OMA-DM 訊息完整性、DM Tree 加密、部署包完整性與簽章 | (`SWE1-FOTA-170`, 171–174)、(`SWE1-FOTA-309`, 310–312/338)、(`SWE1-FOTA-022`, 0 列) | 8 | 0 | 8 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：022 Communication Security；170 Deployment Package Security；309 OMA-DM Security | | | | |
| 16 | `Interruption Handling` | 中斷處理與續傳：六種中斷、復原、儲存、併發 | (`SWE1-FOTA-309`, 313/315–329/357/359–360) | 19 | 0 | 19 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 17 | `Status Reporting` | 回報：session 完成／重試／重送、backchannel 狀態 | (`SWE1-FOTA-309`, 330–334/339/358) | 7 | 0 | 7 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 18 | `Deployment Conditions` | 部署前條件：可組態安裝條件、評估、車輛條件提供 | (`SWE1-FOTA-309`, 336–337/340–341/343–346) | 8 | 0 | 8 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 19 | `Session Management` | 輪詢與 session 管理：間隔、前提、伺服器發起流程、佇列 | (`SWE1-FOTA-309`, 347–356/361/368–369) | 13 | 0 | 13 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 20 | `Telematics Client` | TC 介接：通訊建立、訂閱、session 接收與轉送 | (`SWE1-FOTA-309`, 363–367) | 5 | 0 | 5 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 21 | `Update Agent` | Update Agent：目標選擇、相依序、API、A/B、failsafe、差分 | (`SWE1-FOTA-309`, 370–383) | 14 | 0 | 14 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| | **小計** | | **21 組／45 群** | **311** | **87** | **223**（+1 blank） |

### 孤島列檢查（R-SU20）—— 5 個，3 處聚集

實測 2026-08-28，`python3 scripts/layer2_close.py 30c`（種子回測 5/5 通過，
**種子外 0 個新發現**）。評估範圍採 **strict**（R-SU20 v2(a)）——
loose 得 13 列，其多出之 8 列為 Test Set 之正常邊界，非證據。

⚠ **已知盲區**：本檢查**不覆蓋群邊界之錯分**（R-SU20 v2(a)）。

| 037 列 | 標題 | 其組 | 前鄰 | 後鄰 | 記名依據（下放包 18 §二） |
|---|---|---|---|---|---|
| `338` | Pre-Deployment Package Authenticity Verification | `Integrity Verification` | 337 `Deployment Conditions` | 339 `Status Reporting` | 其述「verify the **authenticity of the deployment package**」與 `312`「**integrity verification of the deployment package**」為**同一驗證對象**之一對；前鄰 `337` 之對象為工作流而非驗證。**從對象走，不從流程走** |
| `339` | OTA Status Reporting via Backchannel | `Status Reporting` | 338 `Integrity Verification` | 340 `Deployment Conditions` | 其**對象**為回報訊息之通道，與 `330`–`334` 同一觀察面 |
| `357` | Installation Interruption State Management | `Interruption Handling` | 356 `Session Management` | 358 `Status Reporting` | 首句 save→resume 與 `360`（detect→save→resume）、`325`（suspend→record→wait）為**同一三段結構** |
| `358` | Update Status Reporting to SWMC | `Status Reporting` | 357 `Interruption Handling` | 359 `Interruption Handling` | 對象為對 SWMC 之狀態回報 |
| `361` | Server-Initiated OTA Background Execution | `Session Management` | 360 `Interruption Handling` | 363 `Telematics Client` | 其約束對象為 **server-initiated OTA update flows**，與 `351`／`368`／`369` 同一流程族；「背景執行不阻斷前景」為該流程之執行約束，非獨立能力 |

**每列之依據皆取自 Description 之內容，非其標題關鍵詞**（R-SU20(d)）。

**聚集**：5 個孤島聚為 **3 處**（`338`–`339`、`357`–`358`、`361`）。

**改組前後**（`359` 自 `Session Management` 改置 `Interruption Handling`）：

| | 列數 | 037 列 |
|---|---:|---|
| 改組前（上繳包 15 §6.1） | 7 | `338`、`339`、`357`、`358`、`359`、`360`、`361` |
| **改組後（本輪）** | **5** | `338`、`339`、`357`、`358`、`361` |
| 解除 | 2 | `359`、`360`（二者互為鄰居且同組，孤島身分同時解除） |
| **新產生** | **0** | **無** |

> **R-SU20(e) 之限度**：孤島列指出「該處之依據需高於相鄰之先驗」，
> **不是「該處錯了」**。規格作者確有可能在連續數列中交替寫數種能力。

### 五列定案之記錄（下放包 18 §二）

| 037 列 | 前 | 後 | 變動 |
|---|---|---|---|
| `338` | `Integrity Verification` | `Integrity Verification` | 維持 |
| `357` | `Interruption Handling` | `Interruption Handling` | 維持。⚠ **雙職**：其次句「report the installation status … to the SWMC」屬回報 —— 撰寫 TC 時依 IN §8.2.2 得拆為 2 TC，二者皆 trace 本列 |
| `359` | `Session Management` | **`Interruption Handling`** | **改置** —— 與 `323`（作用中 session 期間之外來請求／不中斷現行 session）同一觸發面與保護目標，差別僅在處置動作（ignore vs queue） |
| `360` | `Interruption Handling` | `Interruption Handling` | 維持 |
| `361` | `Session Management` | `Session Management` | 維持 |

**`PROVISIONAL-ROW` 全數解除。Layer 2 自下放包 18 起無 provisional 列，
R-SU20(f)（不得帶入寫回）之要求已滿足。**

### 0 列 Heading 群（**9 群**）—— R-SU21 v2(b)(c)

**本清單由程式產生並與本檔比對**（`scripts/layer2_close.py 31d`，不符即停）——
R-SU21 v2(b)：**寫「關於零之條文」時，其列舉須以程式產生，不得人手列**。

| Heading id | 標題原文 | 所屬 Test Set |
|---|---|---|
| `SWE1-FOTA-016` | Session Flows | `Session Flows` |
| `SWE1-FOTA-017` | Deployment Flow | `Session Flows` |
| `SWE1-FOTA-020` | Re-Flashing Requirements | `USB Update` |
| `SWE1-FOTA-022` | Communication Security | `Integrity Verification` |
| `SWE1-FOTA-072` | OTA Client Architecture | `Client Architecture` |
| `SWE1-FOTA-073` | Operating Environment | `Client Architecture` |
| `SWE1-FOTA-074` | Over The Air (OTA) Deployment of Software | `USB Update` |
| `SWE1-FOTA-076` | Local Deployment of Software | `USB Update` |
| `SWE1-FOTA-085` | FOTA ROV Reflash Requirements | `ROV Installation` |

> **R-SU21 v1(c) 之加註（逐字）**：「0 列群之歸屬依據為標題字面，無列證據，
> **不具交付效力**，亦**不得作為其他歸屬之類比依據**。」
>
> R-SU21 v1(b) 誤載為 8 群並漏列 `SWE1-FOTA-085`，**v2(b) 更正為 9 群**
> （上繳包 16 §6.1）。

---

### R-SU19 之套用記錄（本輪拆分）

| 原組 | 列數 | 拆為 | 拆後列數 |
|---|---:|---|---|
| `TBM Update` | 50 | `TBM Reflash` + `HU FOTA via TBM` | 14 + 36 |
| `Session Flows` | 42 | `Deployment Flow` + `Session Flows` | 26 + 16 |

拆後之最大組為 `HU FOTA via TBM`（36 列）與 `Client Architecture`（35 列），
**皆未逾 40**。

### 命名之偏離記錄

`HU FOTA via TBM` 為 4 token，逾 IN §4.2 之「典型 1–3 字」。
依據（下放包 16 §4.2）：`110`（TBM 自身之 reflash）與 `214`
（HU 經 TBM 路徑之 FOTA）之區別即在 `via TBM`，縮短會使二組不可分。
IN §4.2 之「典型」為傾向非硬限，本例記其依據後採用。

### 三重閉合（R-SU10 v2）—— 全過

實測 2026-08-28，`python3 scripts/layer2_close.py`（不符即非零碼退出）：

| 判準 | 實測 | 應為 | |
|---|---:|---:|:--:|
| **(i) 列數**：21 組列數和 | **311** | 311（R-SU3） | ✅ |
| **(ii) 群數**：所涵蓋 Heading id 之聯集 | **45** | 45 | ✅ |
| ＿未被任何組涵蓋之群 | 0 | 0 | ✅ |
| ＿組中出現而不存在之群 | 0 | 0 | ✅ |
| **(iii) 列 id 集合**：聯集大小 | **311** | 311 | ✅ |
| ＿母體有而 Layer 2 無（漏） | 0 | 0 | ✅ |
| ＿Layer 2 有而母體無（溢） | 0 | 0 | ✅ |
| ＿**相交之組對** | **0** | 0 | ✅ |

跨章群之內部分割：

| Heading 群 | 列數 | 分屬之 Test Set | 各組列數和 |
|---|---:|---|---:|
| `SWE1-FOTA-309` | 70 | `Integrity Verification`(4)、`Interruption Handling`(18)、`Status Reporting`(7)、`Deployment Conditions`(8)、`Session Management`(14)、`Telematics Client`(5)、`Update Agent`(14) | **70** ✅ |
| `SWE1-FOTA-170` | 7 | `Silent Update`(3)、`Integrity Verification`(4) | **7** ✅ |

> (i) 對 0 列群無感、(ii) 對跨章群之內部錯分無感 —— **三者缺一不可**
> （R-SU10 v2）。`SWE1-FOTA-022`（0 列）已納入 `Integrity Verification`
> （下放包 16 §二 #1），`UNASSIGNED` 標記解除。

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

```
PROVISIONAL — 得於階段二逐列人裁時就地修正（R-SU18(c)）
```

依 IN §4.1.5：Layer 3 僅存本檔。其值為現階段之最佳推定。
**不得用以推定任何 `specification_reference`**（R-SU18(c)）。

| Test Set | Layer 3 provisional（CFTS 章） | 依據強度 |
|---|---|---|
| `Silent Update` | `4.7.3.2` | **GT**（`176`,`179`,`180`） |
| `Interruption Handling` | `4.12`, `4.12.1`, `4.12.2` | **GT**（`313`,`315`–`324`,`328`,`329`,`332`） |
| `Integrity Verification` | `4.8.2`, `4.8.3` | **GT**（`310`,`311`,`312`） |
| `Client Architecture` | `4.4`, `4.4.1`, `4.5` | **GT**（`257`,`260`,`261`,`262`） |
| `Bearer Selection` | `4.6`, `4.6.1`, `4.7.3` | **GT**（`292`，信度 M） |
| `Update Policy` | `4.7.3`, `4.7.3.1` | **GT**（`034`；GT-B `030`,`031`） |
| `Session Management` | `4.10.2`, `4.10.3`；**`361` 另併列 `4.7.1` 之可能** | **GT**（`347`）+ 推定 |
| `TBM Reflash` | `5`（TBM FOTA Reflash Requirements） | 標題全詞重疊（下放包 07 §1.4） |
| `HU FOTA via TBM` | `4.2.3` + `5` | **GT**（`215`,`216`） |
| `USB Update` | `3`（Media Reflash Requirements） | 推定 |
| 其餘 11 組 | **TBD** | 待階段二 |

**覆蓋狀態（2026-08-28）**：本表 10 組有值，其中**標為 GT 者 8 組**
（`TBM Reflash` 為標題全詞重疊、`USB Update` 為推定，二者非 GT）；
**TBD 11 組**。10 + 11 = 21 ✅。
逐列已裁者 GT-A1 28 列 + GT-B 4 列 = **32／311（10.3%）**。

> ⚠ 下放包 16 §五 之結語稱「有 GT 支持者 **9** 組／21；TBD **11** 組」——
> 逐列數其表中標 **GT** 者為 **8** 組（上繳包 15 §3.1）。本檔採 **8**。

### GT 材料之現況

| 來源 | 已裁 | 用途拘束 |
|---|---:|---|
| GT-A1（定向人裁） | 28 列 | 不得單獨用於任何比率之估計（R-SU17 v1(a)） |
| GT-A2（分層隨機，材料 30 列） | **0** | 回測之比率以本帳為準（R-SU17 v2(a)） |
| GT-C（CFTS 側反向，材料 50 物件） | **0** | 偵測路徑 A 系統性看不見之區塊（R-SU17 v2(d)） |
| GT-B（區塊導出） | 4 列 | 不得用於路徑 A 之回測（R-SU16 v2(h)） |

台帳見 `GROUND_TRUTH.md`。

> **R-SU17 v2(e) 之揭露**：GT-A2 與 GT-C 現無一列經裁，
> **本 feature 現無任何合法之比率估計**；GT-A1 上所得之各比率
> 一律為描述性數字，不得作為母體之估計。
