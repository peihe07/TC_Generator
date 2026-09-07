# DATA REQUESTS — Phone (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`_intake/Phone/`；本 feature 依 R-G66 走 `sources/`，**不落 `inputs/`**。
each landing closes or advances the linked anomaly. Ordered by when a batch
actually needs it.

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

**取號**：依 `down/20260901_VS-SL-01_review.md` §2.2 —— **未送出前不佔號**；
DR 號依 Pei 送出時之台帳取。下表之 `DRAFT-PH-*` 為本 feature 之內部草稿標籤，
**不是 DR 號**。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| `DRAFT-PH-a` | SYS1 Phone 匯出之**權威版本**（見下 §1） | **OPEN — 阻斷** | 754（全部） | **Phase 2 起全阻**：`spec_reference` 無來源 | A-PH01 | **P0** |
| `DRAFT-PH-b` | 037 之 26PI 增補（MPA11／MPA12）或其不適用之裁示 | OPEN | 143（Multiphone 相關） | 不阻斷本輪；影響增補輪 | A-PH07 | P2 |
| `DRAFT-PH-c` | `ENTER_HOME_SCREEN` 之入口逐字（見下 §2） | OPEN — 承接自 GC-07 | 7＋（第 25 章 Phone Widget） | 不阻斷；PENDING 標記 | — | P1 |

---

## §1　`DRAFT-PH-a` —— SYS1 之權威版本（**本包之升級項**）

### 標的

repo 內同檔名之兩份 SYS1 匯出，**擇一為權威**（或告知第三份為正）：

| 來源 | sha256 | docProps modified |
|---|---|---|
| `_intake/Phone/SYS1_HMI_Phone_HMI_Logic_and_Flow_R1_SR24_Post 2A_(June_21_2022).xlsx` | `e6d58766cf6ddb19e6cdfc93bea01d77c03037123f65fa95386f6238782edd8a` | 2026-05-19 |
| `spec-index/cache/SYS1_HMI_Phone_HMI_Logic_and_Flow_R1_SR24_Post 2A_(June_21_2022).xlsx` | `61c3a6a022f8dd18c0e724b411c492fbeafc153e4f814880ace16ed2e278d2f7` | 2026-03-16 |

### 為何不能由執行層擇一

`spec_reference` 為 `{檔名}_{章節號}`（IN §10.7(b)）。兩份之章節號在
`5.17`～`17.5` 區間**整段錯位一格**（124 列），擇錯者即 124 列追溯錯指，
而其在簿面上**與正確者長得完全一樣**。詳見 `ANOMALIES.md` A-PH01。

### 本層已量得而供裁決之事實（不含建議以外之處置）

1. **037 之引用鍵在 `cache` 版命中率較高**：以 037 `HMI Source ID` 對
   SYS1 `SYSRE_HMI_Source ID` 直接鍵接，`cache` **212/213（99.5%）**、
   `intake` **211/213（99.1%）**；命中後去標籤逐字比對，`cache` 精確 208＋近似 2，
   低相似僅 **2** 列；`intake` 精確 202＋近似 3，低相似 **6** 列
   （其 5.17–5.20 四列為前述錯位所致之系統性錯指）。
   全表見 `data/parent_to_sys1_cache.tsv`／`data/parent_to_sys1_intake.tsv`。
2. **兩份皆非 037 之來源**：037 引用 `_5.16.2`（`PHCC8.`）—— `intake` 置於 `5.17`、
   `cache` 無此需求；037 亦引用 `_17.9` —— 只有 `cache` 有。
   **上游至少存在第三份匯出**，其 `PHCC8.` 為 `5.16` 之子項。
3. `intake` 版另有一處**儲存格併格失真**：`NRL-128107` 之正文被併入
   `NRL-128106` 之格內，該版遂無 `NRL-128107` 之獨立列。
4. 兩份列數皆 273、頂層章皆 27 —— **列數與章數檢查對本項一律沉默**。

### 所求（擇一即可）

- (a) 裁示以 `cache` 版為權威，並容忍 `_5.16.2` 一列無來源（該列以 PENDING 出）；或
- (b) 裁示以 `_intake` 版為權威，並接受 5.17–5.20 之章節號與 037 不一致；或
- (c) **向上游索取 037 V0.1 實際據以撰寫之那一份匯出**（推薦：其 `PHCC8.` 應在 `5.16.2`，
  且第 17 章應有 `17.9`）。

### 本層之處置

`feature.yaml` `paths.sys1_export: null`、`sources.sys1_export` 不登錄；
`sources/raw/` 只登錄其餘 4 件。`recon.py` 之
「SYS1 export available for outline lookup」斷言**如實留為 FAIL**，
`DECISIONS.md` 因該斷言未由 `recon.py` 產出（本檔之 DECISIONS.md 為人工補寫，
其首節已具名此事）。**不臆造、不擇一、不繼續 Phase 2。**

---

## §2　`DRAFT-PH-c` —— `ENTER_HOME_SCREEN`（承接自 GC-07，FO §4 [ADD] 第二項）

### 承接聲明

`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §5.3 之 `ENTER_HOME_SCREEN`
現為 `PENDING`。依 FO §4 [ADD] 第二項，**不得複製 PENDING 而不登 DR**，
本節即本 feature 之承接登記。前案之查詢式與命中數見
`features/vehicle_setting/DATA_REQUESTS.md`「DR 草稿 —— HMI entry path」節
（`SYS1_HMI_Home_Screen…` 104 entries 掃 `home button`／`Home icon`／
`return to the home`／`access the home` 命中 0；Menu Bar §4.1 命名表無 `Home` 列）。

### 本 feature 是否需要（下放包 §任務 4 所交付之判斷）

**需要。** 依 037 實測：

| 查詢（037 全欄，`re.I`） | 命中列 |
|---|---:|
| `home\s*screen` | **7**（`SWE1-HMI-144`、`-144-09`、`SWE1-HMI-199`、`-199-03`、`-199-04`、`-199-05`、`SWE1-HMI-204`） |
| `\bwidget\b` | 46 |
| `menu\s*bar` | 621 |

第 25 章（Phone Widget，`SWE1-HMI-199`～`-204`，25.6.1／25.9）之多列以
**Home Screen 上之 widget** 為前提，其 setup 無法只以 Menu Bar 之
`Phone` 入口表達。故 `ENTER_HOME_SCREEN` 於本 feature **確有標的**，
不得以「Phone 之入口為 Menu Bar」為由結案。

### 本 feature 之主要入口（已查得，非本 DR 之標的）

`037` 之 `menu bar` 命中 621 列，`main category bar` 1 列（`SWE1-HMI-016`：
`PHCAT4.) If Android Auto or Apple CarPlay are active, they will take over the
Phone Category section and the Phone category icon on the Main Category Bar.`）。
→ Phone 之固定入口為 **Menu Bar 之 `Phone`**；其逐字標籤於 profile §5.3 落定
（**待 `DRAFT-PH-a` 後自 SYS1 取逐字**，本包不臆造）。

### 所求

回到 Home Screen 之**入口逐字**（Menu Bar 按鈕？實體鍵？手勢？）。

### 本層之處置

**不阻斷撰寫**。該常數於本 feature profile §5.3 以
`PENDING: DR-{n} HMI entry path Home Screen` 標記（R-G71(d) 格式），
`{n}` 待 Pei 送出時取號。
