# 上繳包 01 —— driver_distraction 開案：T-抄、T1–T7

- 日期：2026-08-27
- 對應下放：`docs/handoff/01_feature_open.md` ＋ **`02_rulings_q1q6.md`**
  （02 §四 明文「T1–T5 依包 01 §五 原文照跑」，故二包併於本上繳包）
  - 01 SHA256 未於本輪計（其於本 session 之前落檔）
  - 02 SHA256 `3fd233c8e06d13c5e03350209e40bc331bb0d36eeaf7979af92525637bd167f4`，138 行
- **結論：T-抄、T1–T7 全數完成。二個異常（A-DD1 複測成立、**A-DD2 新立**）、
  二筆 DR 已登記（皆 DRAFTED，待 Pei 發送）。**
- 未起草 framework、未寫 profile、未產任何 TC、未寫回、未進行任何 git 操作。

---

## 0. 三件請你先看

1. **`$PARK_BRK_EGD$` 四庫皆查無，而來源自己的欄位裡已經寫著它應該是 `PARK_BRK_EDG`**
   —— 供應商提出、上游回覆確認，**而規範欄與驗證欄未隨之更正，第二列完全沒動**。
   我**沒有自行採用 `EDG`**。見 §5。
2. **A-DD1 複測成立，且多得一項下放包文稿未載之證據**：
   同一作者在 12 列上一致地以 `-125` 為 HK 章閘，**唯獨最後 4 列**把它接到
   LATAM 章之需求上。見 §3。
3. **036 母本不在 `inputs/`** —— R-DD2 之「project 前綴權威為工作簿 D2」
   **本輪無從實測**。`feature.yaml` 之 `paths.workbook` 記 `null`。見 §6。

---

## 1. T-抄 —— R-DD1~R-DD5

逐字 append，**程式回讀逐字元核對，五條全部相符**：

```
R-DD1: 相符  sha c18997bc2d6e839c
R-DD2: 相符  sha e1a404b5d3047b7c
R-DD3: 相符  sha 49772cf8706b577d
R-DD4: 相符  sha 8208c4b4130b1418
R-DD5: 相符  sha 2cc26447b692a977
```

索引表依 R-SU8 同型建於檔首（**5 條現行、0 留存**）：

## 現行版索引（沿 R-SU8(b) 同型；本 feature 自始即建）

> 判準：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-DD1 | v1 | feature 身分：slug `driver_distraction`、Test Group `Driver Distraction`、前綴 R-DD／A-DD／DR-DD | 02 §一 |
| R-DD2 | v1 | tc_id_format `newR1L-DD-{n:03d}`；project 前綴權威為工作簿 D2 | 02 §一 |
| R-DD3 | v1 | ER 之斷言錨層級：HMI 現象為主錨；callback／Listener 依 reaction presence 降階 | 02 §一 |
| R-DD4 | v1 | SYSAD 為人讀參考，不入語料、不入 prompt 指紋 | 02 §一 |
| R-DD5 | v1 | 四庫綁 `vehicle_setting/inputs/` 原件；sha256 自實體檔重算；查無者逐項登 DR | 02 §一 |

---

## 2. T1／T2 —— 骨架與驗型

### 2.1 T1

`scripts/new_feature.py driver_distraction --adopt-existing`。

**`--adopt-existing` 為此情形而設**（其註解逐字：「fills the gaps and
NEVER overwrites: a scaffold that clobbered a signed handoff would destroy
the only copy of a ruling」）—— 目錄已存在（handoff ＋ inputs 已在場），
**無旗標則腳本拒跑**。實測 `docs/handoff/` 二包**未被覆蓋**。

### 2.2 T2 —— 五檔逐檔驗型 ＋ sha256

| # | 檔 | `file -b` | magic（前 8 byte）| sha256 | bytes |
|---|---|---|---|---|---|
| S1 037 `DD_SWE1_0807_EN.xlsx` | `Microsoft Excel 2007+` | `504b030414000600` | `f0acfbac68b1c7a49d8b406b426156d0…` | 47,018 |
| S2 CFTS022 SYSRA | `Microsoft Excel 2007+` | `504b030414000600` | `81052306af593bbe28326932557cf3aa…` | 180,225 |
| S3 SYS1 匯出 | `Microsoft Excel 2007+` | `504b030414000000` | `505a06ce6a9a35422411dad0219673e1…` | 29,980 |
| S4 HMI spec PDF | `**PDF document, version 1.5, 7 pages**` | `255044462d312e35` | `a7144602b7fb28df2dd5d0d6a0459553…` | 793,496 |
| S5 SYSAD docx | `**Microsoft Word 2007+**` | `504b030414000600` | `025ed9acbb263e8bf324c9fc552d6b5b…` | 5,412,577 |

### 2.3 ⚠ 包 01 §一之偽型態預警：**對 Pei 之原件不成立**

下放包 01 §一警告「S5 實為 UTF-8 純文字（非 zip/docx）、S4 實為頁影像＋
文字之封存檔（非真 PDF）」，並要求「執行層開檔前先驗型」。

**實測：五檔全部為真型態** —— S5 為真 docx（PK zip magic）、
S4 為真 PDF 1.5／7 頁（與 §一所述之頁數相符）。

**該預警針對的是分析層手上之轉換副本，不是 Pei 置入之原件。**
T2 之補位作用（§七所稱「分析層副本與 Pei 原件之同一性未驗」）**至此達成**。

---

## 3. T3／T4 —— recon 與 leaf 清單

### 3.1 assertion

```
functional_requirement_count: 28   實測 28 —— 閉合 ✅
```

**只宣告已實測者**（R-VC9 家族，下放包 01 T3 明文）；其餘鍵未宣告。

其他實測（未宣告為 assertion，僅記錄）：
- `Categorization` **28/28 = `Functional`**（無 Heading 列）
- `Sub Categorization` 28/28 = `Driver_Distraction `（**末有一個空白**，逐字）
- `Priority` 28/28 = `High`
- id `-001`~`-028` **連續無缺、無重複**
- `Source Requirement ID` **15 個相異**，其中 `-125` 被 **12 列**引用

### 3.2 T4 —— `data/leaf_inventory.tsv`

28 列，欄位形制沿 `bed_lowering`，**留原文欄**（`description_raw`／`vc_raw`／
`had_x000D`）。

**`_x000D_` 實測 0 / 28 列** —— 本 feature 之 037 無該殘留。
正規化仍照做並留原文欄，且**以「抹平空白後兩欄相等」證明其只動 `_x000D_`
與空白**（實測 ✅，無一列不符）。

<details><summary>28 列清單（req_id／source／title／description 首 60 字）</summary>

| leaf | source | title | description |
|---|---|---|---|
| `001` | SYS-RA-Driver_Distraction-113 | Body OFF | AC1:\nWhen the vehicle exits Body OFF sleep, DD Service prov… |
| `002` | SYS-RA-Driver_Distraction-113 | Body OFF | AC2:\nWhen the DD process is terminated during Body OFF slee… |
| `003` | SYS-RA-Driver_Distraction-114 | Speedometer | AC1:\nWhen DD Service receives a valid $Speedometer$ value t… |
| `004` | SYS-RA-Driver_Distraction-114 | Speedometer | AC2:\nWhen DD Service can no longer obtain a valid $Speedome… |
| `005` | SYS-RA-Driver_Distraction-115 | Speedometer | AC1:\nWhen DD Service receives a valid $Speedometer$ value t… |
| `006` | SYS-RA-Driver_Distraction-115 | Speedometer | AC2:\nWhen DD Service can no longer obtain a valid $Speedome… |
| `007` | SYS-RA-Driver_Distraction-116 | Speedometer | AC1:\nWhen DD Service receives a valid $Speedometer$ value t… |
| `008` | SYS-RA-Driver_Distraction-116 | Speedometer | AC2:\nWhen DD Service can no longer obtain a valid $Speedome… |
| `009` | SYS-RA-Driver_Distraction-117 | Locked Out State | AC1:\nWhen the signal simulation tool sends vehicle signals … |
| `010` | SYS-RA-Driver_Distraction-117 | Locked Out State | AC2:\nWhen the signal simulation tool stops transmitting a v… |
| `011` | SYS-RA-Driver_Distraction-118 | Locked Out State | AC1:\nWhen the signal simulation tool sends vehicle signals … |
| `012` | SYS-RA-Driver_Distraction-118 | Locked Out State | AC2:\nWhen the signal simulation tool stops transmitting a v… |
| `013` | SYS-RA-Driver_Distraction-120 | Locked Out State | AC1:\nWhen the signal simulation tool sends vehicle signals … |
| `014` | SYS-RA-Driver_Distraction-120 | Locked Out State | AC2:\nWhen the signal simulation tool stops transmitting a v… |
| `015` | SYS-RA-Driver_Distraction-121 | Locked Out State | AC1:\nWhen the signal simulation tool sends vehicle signals … |
| `016` | SYS-RA-Driver_Distraction-121 | Locked Out State | AC2:\nWhen the signal simulation tool stops transmitting a v… |
| `017` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-126 | VC_Trans_Equipped
PresentGear | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `018` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-126 | VC_Trans_Equipped
PresentGear | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |
| `019` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-127 | VC_Trans_Equipped
PresentGear | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `020` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-127 | VC_Trans_Equipped
PresentGear | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |
| `021` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-128 | VC_Trans_Equipped
PARK_BRK_EGD | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `022` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-128 | VC_Trans_Equipped
PARK_BRK_EGD | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |
| `023` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-129 | VC_Trans_Equipped
PARK_BRK_EGD | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `024` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-129 | VC_Trans_Equipped
PARK_BRK_EGD | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |
| `025` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-132 | Speedometer | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `026` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-132 | Speedometer | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |
| `027` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-133 | Speedometer | AC1:\nWhen Country_Code is Hong Kong\nAnd DD Service obtains… |
| `028` | SYS-RA-Driver_Distraction-125; SYS-RA-Driver_Distraction-133 | Speedometer | AC2:\nWhen Country_Code is Hong Kong\nAnd DD Service cannot … |

</details>

---

## 4. A-DD1 之複測（§0 第 2 件）

**下放包之主張逐項成立**，CFTS022 章結構實測：

```
-123 [Heading]      Hong Kong Market Regulations
-125 [FR]           …shall be implemented if $Country_Code$ = [Hong Kong].
-126 ~ -129 [FR]    ← HK 章之需求
-130 [Heading]      LATAM Market Regulations
-131 [Information]  …apply to the LATAM market only.
-132 / -133 [FR]    ← LATAM 章之需求
```

### 4.1 補充證據（下放包文稿未載）

| 037 列 | 所引 source | 章歸屬 | 一致？ |
|---|---|---|---|
| `-017`~`-024`（8）| `-125` ＋ `-126`~`-129` | 全在 HK 章 | ✅ |
| **`-025`~`-028`（4）** | `-125` ＋ `-132`／`-133` | **跨二章** | ❌ |

**這使「配錯」之可能高於「有意雙市場」** —— 但**該判斷屬上游**，
本包只列量測。建議 DR-DD1 發送時附此表（已寫入 `DATA_REQUESTS.md`）。

---

## 5. ⚠ T6 —— 五訊號查對，與 A-DD2

### 5.1 彙總

| 訊號 | LID | DBC | PROXI | 判 |
|---|---|---|---|---|
| `$Speedometer$` | ✅ | — | ✅ | 查得 |
| `$VC_Trans_Equipped$` | ✅ | — | — | 查得 |
| `$PresentGear$` | ✅ | — | — | 查得 |
| **`$PARK_BRK_EGD$`** | **✗** | **✗** | **✗** | **查無** |
| `$Country_Code$` | ✅ | — | ✅ | 查得 |

> **DBC 欄之 `—` 為預期狀態**：`$…$` 為**邏輯識別碼**（LID 之標的），
> 非 CAN 訊號名。**不因此登異常。**

### 5.2 近似拼法之實測

LID `CAN Mapping` **r1310** = **`PARK_BRK_EDG`**
（→ `STATUS_BH_BCM1.ParkBrakeSts` CAN-B／`BCM_FD_9.ParkBrakeSts` CAN-FD）。

**`EDG` vs `EGD` —— 二字母倒置。**

### 5.3 ⚠ 來源自身已記載，但只改了一半

CFTS022 r129（`-128`）：

| 欄 | 拼法 |
|---|---|
| `Description`（**規範欄**）| `EGD` |
| `SYS2 System-HW` | **`EDG`** |
| `SYS2 System-SW` | **`EDG`** |
| `SYS2 HARMAN Comments` | **`EDG`** —— *"…looks incorret. Does the expected LID name is \"PARK_BRK_EDG\"."* |
| `SYS2 MD Feedback` | **`EDG`** —— *"The LID which is referred here is $PARK_BRK_EDG$"* |
| 驗證標準／方法 | `EGD` |

**r130（`-129`）未被更正** —— 其 `System-SW` 仍作 `EGD`。

### 5.4 我沒有自行採用 `EDG`

理由三：**規範欄與註記欄位階不同**；**`-129` 未更正故「已定案」不成立**；
**R-DD5 明文查無者登 DR、不得代以語意相近之他訊號**（R-13）。

`-021`~`-024` 保留 `$PARK_BRK_EGD$` 原名，**不阻斷生成**。已登 **A-DD2**／**DR-DD2**。

<details><summary>T6 原始輸出</summary>

```
## T6 —— 五訊號對四庫之逐項查對

- LID：`Logical Identifiers and CAN Mapping v1_76.xlsx`
- DBC：`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`
- PROXI：`PROXI_HDCC27_R3_20250424.xlsx`
- **四庫皆綁 `features/vehicle_setting/inputs/` 之原件**（R-DD5），未複製入本 feature

### `$Speedometer$`

**DBC**：0 處 —— **查無**

**LID**：2 處
  - `CAN Mapping` r1738: Speedometer | Vehicle speed | VehicleSpeedVSOSig | Pnet | CUSW
GW_C1.VEH_SPEED = STATUS_B_BSM.Vehi | GW_C1.VEH_SPEED | CAN-B | Powernet
16 bit signal          
0 - +51 | FFFFh | 174
451
551
651
673
68
  - `Proxi & Configuration` r181: Speedometer_Range | Feature present | Speedometer_Range | PROXI | see proxi file | CFTS053 | • See V1.53 revision note (3)

**PROXI**：4 處
  - `Revision Notes` r113: 2024-01-19 00:00:00 | The following components/VFs were added: | Instrument_Panel_Cluster_Configuration_1 | 73 - 73 | 0 - 7 | Speedometer_Tolerance | CHIRAPATSAKUL, PAT | CADM 
  - `Revision Notes` r263: 2024-05-16 00:00:00 | The following components/VFs were added: | Instrument_Panel_Cluster_Configuration_1 | 73 - 73 | 0 - 7 | Speedometer_Tolerance | CHIRAPATSAKUL, PAT | TCM 
  - `Revision Notes` r348: 2024-06-07 00:00:00 | The following components/VFs were remove | Instrument_Panel_Cluster_Configuration_1 | 73 - 73 | 0 - 7 | Speedometer_Tolerance | CHIRAPATSAKUL, PAT | CADM 
  - `Revision Notes` r431: 2025-03-12 00:00:00 | The following components/VFs were remove | Instrument_Panel_Cluster_Configuration_1 | 73 - 73 | 0 - 7 | Speedometer_Tolerance | CHIRAPATSAKUL, PAT | TCM 

**小結**：LID／PROXI

### `$VC_Trans_Equipped$`

**DBC**：0 處 —— **查無**

**LID**：2 處
  - `Proxi & Configuration` r420: VC_Trans_Equipped | VC_Trans_Equipped | VC_Trans_Equipped | CAN-C | Not Applicable | Not Applicable
  - `Proxi & Configuration` r421: VC_Trans_Equipped | Transmission manual or automatic | VC_Trans_Equipped | Pnet | VehCfg7.VC_Trans_Equipped | CAN-B | Transmission equipped: 0 = Automatic & 1 | Gear_Box_Type | Gear_Box_Type

**PROXI**：0 處 —— **查無**

**小結**：LID

### `$PresentGear$`

**DBC**：0 處 —— **查無**

**LID**：4 處
  - `Rev History` r102: 1.73 | Jun 30,2025 | (1) SR25 CR30252 | (1)  SR25 CR30252
>CR ticket:  SRXX-1888 | Baruch Pérez
  - `CAN Mapping` r1397: PresentGear | Current Gear | Pnet | See tables to right
Powernet 0-6 = CUSW  | GW_C1.Gr | CAN-B | Powernet
4 bit signal
0=Current gear "N" | Fh | 673
651 | GEARMOT3.ActualGear | CAN-C | CUSW
4 bit sig
  - `332BEV Specific Signals` r32: This signal is used to launch the "Lock  | PresentGear | TRANSM2.ShiftLeverPosition
  - `M182BEV Specific Signals` r3: This signal is used to launch the "Lock  | PresentGear | VDCM_PWT2.GearEngagedForDisplay_VDCM

**PROXI**：0 處 —— **查無**

**小結**：LID

### `$PARK_BRK_EGD$`

**DBC**：0 處 —— **查無**

**LID**：0 處 —— **查無**

**PROXI**：0 處 —— **查無**

**小結**：**四庫皆查無**

### `$Country_Code$`

**DBC**：0 處 —— **查無**

**LID**：3 處
  - `CAN Mapping` r1996: TBM_COUNTRY_CODE | TBM_FD_1.SLI_CS_COUNTRY_CODE | FD | see dbc file | see dbc | See V1.49 revision note (9)
  - `Proxi & Configuration` r43: Country_Code | Country Code | Proxi_Country_Code | Refer to CUSW Proxi | ECUCfg3.EC_AudTel1b-<DEST> | See latest version of 'CIP Market Config |   | Car_Configuration_16.Country_Code | PROXI | Car_Con
  - `Proxi & Configuration` r250: VC_COUNTRY | Vehicle Configuration by Destination Cou | UNhxn by Destination Country (this has a | PNet | CUSW = Atlantis

Powernet (0) = CUSW N/A | VehCfg1.VC_COUNTRY | CAN-B | 0 = ROW
2 = USA
3 = EU

**PROXI**：4 處
  - `Revision Notes` r17: 2023-12-05 00:00:00 | The following components/VFs were added: | Car_Configuration_16 | 107 - 107 | 0 - 7 | Country_Code | CHIRAPATSAKUL, PAT | BCM 
  - `Revision Notes` r55: 2024-01-19 00:00:00 | The following components/VFs were added: | Car_Configuration_16 | 107 - 107 | 0 - 7 | Country_Code | CHIRAPATSAKUL, PAT | BCM CADM CVADAS ECC ECM EVCU2 IPC PAM 
  - `Revision Notes` r141: 2024-04-09 00:00:00 | The following components/VFs were remove | Car_Configuration_16 | 107 - 107 | 0 - 7 | Country_Code | CHIRAPATSAKUL, PAT | IPC ECM BCM 
  - `Revision Notes` r207: 2024-05-13 00:00:00 | The following components/VFs were added: | Car_Configuration_16 | 107 - 107 | 0 - 7 | Country_Code | CHIRAPATSAKUL, PAT | BCM ECM IPC 

**小結**：LID／PROXI

---

## 彙總

| 訊號 | 查得於 | 判 |
|---|---|---|
| `$Speedometer$` | LID／PROXI | 查得 |
| `$VC_Trans_Equipped$` | LID | 查得 |
| `$PresentGear$` | LID | 查得 |
| `$PARK_BRK_EGD$` | — | **查無 —— 須登 DR** |
| `$Country_Code$` | LID／PROXI | 查得 |

**查無 1 / 5** —— 查無者依 IN §8.7.5(d)(g) 保留來源名稱並逐項登 DR，**不得代以語意相近之他訊號**（R-13）。
```

</details>

---

## 6. ⚠ 036 母本不在 `inputs/`

下放包 01 T2 列 S1–S4（＋S5 依 Q5），**未列 036 工作簿母本**。

後果：
- `feature.yaml` `paths.workbook` = **`null`**、`workbook_state` = **`null`**
- **R-DD2 之「project 前綴之權威為工作簿 D2 儲存格；執行層開副本時實測確認為
  `newR1L`」本輪無從執行** —— 該實測待母本到位
- 已於 `feature.yaml` 逐字記明，非靜默留空

---

## 7. T7 —— DATA_REQUESTS 建檔

| DR | 狀態 | 標的 | 阻斷 |
|---|---|---|---|
| **DR-DD1** | **DRAFTED** | 037 作者／上游 | `-025`~`-028` 四 leaf **凍結** |
| **DR-DD2** | **DRAFTED** | 上游（CFTS022 作者）| **不阻斷**；`-021`~`-024` 之訊號名待定 |

**二筆皆待 Pei 發送。** DR-DD1 之文稿逐字保留下放包 02 §三 原文，
另附 §4.1 之複測表。

---

## 8. 獨立自評

1. **§5.3 之發現讓我很想直接用 `EDG`。** 來源自己的兩個欄位都說了、
   LID 也對得上、CAN 訊號也接得起來 —— 一個字改下去，這條線就通了。
   **沒改，是因為 R-DD5 明文寫了不准**，不是因為我看出什麼別的理由。
   **而 `-129` 未被更正這件事，是我在寫理由時才注意到的** ——
   它把「已定案」這個推定擋掉了，那才是真正站得住的理由。
2. **A-DD1 我複測了才寫。** 下放包給了結論，我沒有直接抄；
   複測之後多出 §4.1 那張表，那是抄不會得到的。
3. **T1 差一點沒做成。** `new_feature.py` 直接拒跑，我先想到的是「複製骨架再搬」
   —— 讀了腳本才發現 `--adopt-existing` 正是為此而設，且其註解就寫著理由。
   **又是一次「答案已在 repo 裡」。**
4. **`Sub Categorization` 之末尾空白（`Driver_Distraction `）我照原樣留了。**
   若日後有比對用到該欄，那個空白會咬人；已於 §3.1 記明。

---

## 9. 量測條件揭露（R-G8）

- **五檔之型別以 `file -b` ＋ 前 8 byte magic 雙驗**；sha256 自實體檔重算，
  **未抄任何宣告值**（R-DD5 明文）。
- **四庫綁 `features/vehicle_setting/inputs/` 之原件**，未複製入本 feature；
  其 sha256 亦自實體檔重算。
- **T6 之查對為字面比對**（`SG_`／`VAL_`／逐格 `in` 比對，大小寫不敏感）——
  **非語意比對**。§5.2 之近似拼法掃描為**另一次字面掃描**（8 種樣式），
  **其結果為候選，非對應**。
- **DBC 之 `BO_` 反查**以正則跨行匹配，若某 `SG_` 與其 `BO_` 之間隔有
  非 `SG_` 行則匹配不到 —— 本輪五訊號在 DBC 皆零命中，**該限制未生效**。
- **recon 之 assertion 只宣告 1 條**（`functional_requirement_count`）——
  其餘量測值（Categorization／Priority 分布等）**記錄但未宣告**，
  故不會在日後 recon 重跑時被檢查。
- **未做**：framework 定稿、profile、錨定協定、任何 TC —— 皆不在本輪。
