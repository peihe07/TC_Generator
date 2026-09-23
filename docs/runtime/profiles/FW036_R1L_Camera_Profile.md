# FW036 R1L Camera — Profile（骨架）

- 設立依據：下放包 **CAM-01 §4 任務 5**（`docs/fw036/handoff/down/20260916_CAM-01.md`）；
  **CAM-02 依 R-CAM4～R-CAM9 更新**（`down/20260916_CAM-02.md`）。
- 命名依既有慣例（CamelCase 無分隔，同 `VehicleCategory`／`PowerModing`）。
- 本檔為 **Phase 0–1 之骨架**：只寫已有實測依據者，未鎖定之項一律標
  `[PROPOSED]` 或 `[PEI]`，不預先設計未來條款。
- **母體標註**：本檔凡引用計數必標母體，限下列七者 ——
  A 本 `25 列`／B 本 `230 列`（`203 leaf`＋`27 umbrella`）／
  A 本來源引用 `541 項`（解析 `422`）／SYS1 HeadUnitCameraSystems `1044 列`
  ／SYS1 RVC+PAM（cache 本）`64 列`。

---

## 0. 適用範圍

| 項 | 值 | 權威 |
|---|---|---|
| feature | `Camera` | CAM-01 §4 任務 1 |
| slug | `camera` | 同上 |
| `test_group`（工作簿 G 欄）| A 本 `Camera`；B 本 `Camera` 或 `Camera HMI` | **[PEI]** R-CAM 未裁，見 DECISIONS §6 |
| Layer 2 Test Set（H 欄）| A 本 9 組／B 本 8 組（草案，實測後有出入）| **[PEI]** 見 §4 |
| ABBR（TC ID `NR1L-{ABBR}-{nnn}`，R-G42）| A、B 共用 `CAM`，或 B 本另取 `CAMH` | **[PEI]** 見 DECISIONS §6 |
| `spec_reference`（N 欄）| A 本引 CFTS092／VF551；B 本引 SYS1 HMI L&F 章節（RVC+PAM 取 **cache 本**）| **R-CAM1(c)**、**R-CAM6** |
| 生成順序 | A → B | **R-CAM1(b)** |
| 驗證母體 | A 本 25 leaf；B 本 203 leaf | 本包實測 |
| spec_mode | `A`（SYS1 spec export 齊備）| `intake.py` 判定 |

---

## 1. lint 啟用（R-G70／R-G71）

依 R-G71，新 feature 之 profile **一律啟用 `X` 與 `P`(v4)**。
`P=0`／`X=0` 在未啟用時是沉默，不是核可。

| 代號 | `lint036.CHECK_TITLES` 之現行標題 | 本 profile |
|---|---|---|
| `P` | 訊號寫法不合 R-1 v2（profile 下判準為 R-G70 v4.1）| **啟用** |
| `X` | 導航路徑無固定入口（§5.8／R-G71）| **啟用**（WARN 只報不改）|
| `Y` | PROXI 舊式（`$Param$ is set to` 為 VF230 同義舊式）| 隨 `P` 連動 |

呼叫形式：`python scripts/lint036.py --profile camera <xlsx…>`。
**現況如實回報**：`lint036.py` 之 `--profile` 只作真值使用，不讀本檔內容
（VehicleCategory profile §2 已實測並記錄同一事實）。故本檔 §2 之新檢查項
**必須另行實作於 `lint036.py`** 才會生效，不會因寫在本檔而自動啟用。

## 2. `[ADD]` Vehicle Model 七欄檢查（R-CAM2）—— **已實作**

判準逐字取 R-CAM2：

- (a) `Vehicle Model 車型` 七子欄每列填 `1` 或 `0`，**不留空、不用其他符號**。
  七欄為 `HDCC27 Atl-Hi`／`DT27 Atl-Hi`／`VF(ProMaster)637 Atl-Mi`／
  `Commander (598) Atl-Mi`／`Regengade (5210) Atl-Mi`／`Toro(2261) Atl-Mi`／
  `Fastack (376) Atl-Mi`。
- (b) `Commander (598)` 與 `Regengade (5210)` 兩欄 **一律 `0`**（Camera 兩本）。
- (c) 其餘五個有效車型欄，**每列至少一個 `1`**。

代號 **`Z`**（DECISIONS §6-6 已裁）。實作位置
`scripts/lint036.py` —— 常數 `VEHICLE_MODEL_HEADERS`／`VEHICLE_MODEL_ZERO`／
`VEHICLE_MODEL_ALLOWED`、欄位對照 `build_vehicle_model_columns()`、
檢查 `check_vehicle_model()`，於 `lint_sheet()` 逐列施檢。
測試 `tests/test_lint036_z.py`（27 項）。

**啟用面 —— feature 專屬**：`Z` 不入 `PROFILE_CHECKS`（該表隨**任意**
`--profile` 值生效），而入新增之 `FEATURE_CHECKS = {"camera": ["Z"]}`，
`check_order(profile)` 僅於 `profile == "camera"` 時附加。
立此結構之由：既有交付本雖具七欄但**全空**，若併入 `PROFILE_CHECKS`，
他 feature 之 profile 執行即整本 FAIL（實測 10 本交付簿共 11,368 筆）。

| 施檢面 | 記錄粒度 | 違例文字 |
|---|---|---|
| (a) 值非 `1`／`0`（含空）| 每列每欄 | `R-CAM2(a)：七欄每列須填 1 或 0，不留空、不用其他符號` |
| (b) `Commander (598)`／`Regengade (5210)` 非 `0` | 每列每欄 | `R-CAM2(b)：… 已不支援，Camera 兩本一律 0` |
| (c) 五個有效欄無任何 `1` | 每列一筆 | `R-CAM2(c)：五個有效車型欄每列至少一個 1` |
| 七欄不齊 | **每 sheet 一筆**（不逐列複述）| `R-CAM2：本 sheet 無完整之 Vehicle Model 七子欄，Z 無法施檢` |

(a) 已命中之欄不再判 (b)；(a) 有任一命中時不判 (c) —— 值不合法即無從判
「至少一個 `1`」。欄位比對取標頭**首行**去空白（母本第 9 列 T–Z 為
`HDCC27\nAtl-Hi\n` 之形，第二行之 EE 不入比對鍵）。

## 3. `[ADD]` §5.3 常數候選 `ENTER_CAMERA_SETTINGS`

**[PROPOSED]**，未鎖定。現有證據：

- 第 1–2 hop 沿用既有常數 `ENTER_SETTINGS_APP`（§5.3，已鎖定）：
  `Press "Apps" on Menu Bar to open App Drawer` → `Select "Settings" in the App Drawer`。
- 第 3 hop 之標的為 Settings 內之 `Camera` 類別。
  來源：`forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`
  （sha16 `8d04e51a56d6391d`），分頁 `Settings`，**列 464** 逐字 `13. Camera`；
  其下 **13 項** 設定為列 465–479（含列 475 之 `10.1` 子項與列 479 之 `13` 重覆呈現）。
- ⚠ **第 3 hop 之 label 非出自 SYS1 匯出**。SYS1 HeadUnitCameraSystems
  §6.2 `Rear View Camera: Head Unit Settings`（NRL-187338）只給設定項內容
  （6.2.2.1～6.2.2.3），**不給導航 hop**。依 §5.8(d) 不得臆造 ——
  以 HMI Settings List 之類別列為權威是否足夠，**[PEI]**。

### 3.0 常數之定稿（R-CAM8）

```
ENTER_CAMERA_SETTINGS (3 hops, §5.3)
  Press "Apps" on Menu Bar to open App Drawer
  → Select "Settings" in the App Drawer
  → Select "Camera"
ER: The "Camera" settings screen is displayed
```

第 3 hop 之權威：canon **§5.8(c)** 明列 HMI Settings List 為路徑來源；
`Settings` 分頁 **row 464** 逐字 `13. Camera`（序號非 label）。DR-CAM-d 結案。

### 3.1 hop label 之星號 `*` —— 不入 hop（R-CAM5(a)）

`HMI Settings List` 分頁 `Settings` **列 2** 逐字：
「Refer to Brand-Specific Names tab for highlighted/starred settings.」
即 `*` 為「該 label 隨品牌而異」之標記，**非 label 之字元**。
`Brand-Specific Names` 分頁之 Camera 兩列逐字：

| Settings List Category | Jeep / Chrysler / Ram / Dodge | Fiat / Fiat Commercial |
|---|---|---|
| Camera | `ParkView Backup Camera Delay` | `Rear View Camera Delay [CR14730]` |
| Camera | `ParkView Backup Camera Active Guidelines` | `Rear View Camera Active Guidelines [CR14730]` |

故建議：`*` **不入 hop**；帶星號之設定其 hop label 依受測車型之品牌
自 `Brand-Specific Names` 分頁取值。**[PROPOSED]** —— 裁定見 DECISIONS §6。

## 4. Pre-Condition 之定序（CAM-04 審閱 §一-3，實測 VF230-0819 457 列）

| 序位 | 內容 | 基準 |
|---:|---|---|
| 1 | **電源狀態** —— 已上電情境用 `The HU is in the Full-Operation state`（VF230-0819 457/457）；**開機類 TC 用 `The HU is in Standby state`**（`features/power/delivered/pm_29.xlsx`，19 列）| VF230／power |
| 2 | **PROXI 行** `PROXI <Param> = <raw> (<label>)`（v4.1 標準式，非 VF230-0819 之 `$…$ is set to` 舊式）| VF230-0902／VSM-0902 |
| 3 | **CAN source 行**（R-CAM3(e) 固定句式）| R-CAM3(e) |
| 4 | **品牌行**（R-CAM5(e) 固定句式）—— **只在操作品牌 label 之列出現** | R-CAM5(e) |
| 5 | **畫面／檔位／設定狀態行** | VF230-0819 |

`Full-Operation` 與 `ignition is off` 互斥，不得並列（§4.4；CAM-04 審閱 §二-2）。
每行一個條件（lint `R`）；不得以 `Insert`／`Press`／`Select`／`Set` 等動詞起首（lint `D`）。

### 4.1 開機類 TC 之判別（CAM-08 審閱 §二-1／§二-2）

**Procedure 步 1 為點火（`Send CAN: <MSG>.CmdIgnSts = 4 (RUN)`）者，
Pre-Condition 首行必為 `The HU is in Standby state`** —— `Full-Operation` 之定義已含 IGN RUN，
與「送點火使其開機」互斥。反之，首行為 `Standby` 而 Procedure 無點火步者，
其後各步不可執行。兩向皆由 `selfcheck_camera.py` **第 3 項（雙向）**施檢。

**點火動作一律 CAN 式**，不得以散文寫（`Cycle the ignition`／`Turn the ignition`／
`Power on the HU`／`Power cycle`）；其目的子句（`… so that the HU reads the PROXI
configuration`）移入 ER。施檢：**第 7 項**。
電池斷電（`Disconnect and reconnect the battery supply to the HU`）**不在此列** ——
其為 NVM 驗證所需之另一動作（`NR1L-RVC-064`），非點火。

## 5. `test_item` 上半逾 50 token 之摘句（§4.3.1）

**逾限不是改驗證點之理由**（CAM-04 審閱 §二-3）。摘句以「與括號下半之測試目的
直接相關之句」為限，須**同時保留條件子句與結果子句**，全文以
`specification_reference` 指回。摘後須為原句 token 之**保序子序列**
（不得改寫用字；句首字母轉大寫屬排版正規化，R-4）。

案例（`SYS-RA-VF551_V3-260`，V3 §1.10.2.2，51 → 33 token）：刪行首列點符號 `· `
與末尾逐字重複之 `a)` 子句，保留 `when STATUS_BH_BCM2.CmdIgnSts = [RUN] AND
Gear_Stat.info = [REVERSE] > Reverse_Deb` 與 `the Head Unit shall display the RVC
image … Automatic mode`。全量另五例見 `up/20260916_CAM-05.md` §2.3。

### 5.1 `J`（行首大寫）之豁免 —— 上半逐字（CAM-07 審閱 §一-2，Pei 准）

`test_item` 上半為來源逐字（§4.3.1），其首字若在 SYS2 `Description` 中本即小寫，
**`J` 不適用**。改為大寫將同時破壞兩件事：§4.3.1 之逐字忠實、
`selfcheck_camera.py` 第 4 項之「保序子序列」機器判準。

實例（batch02a 五列）：`-051`／`-052`（`when`）、`-055`（`a)`）、`-056`（`implement`）、
`-070`（`a.`）。**交付語料前例**：`features/*/delivered/` 之 test_item 首行 2223 筆中
10 筆首字小寫（`power`／`vehicle_setting`，兩本皆已交付）。

本豁免為 **profile 側之判讀**，lint 側仍會報 `J`；其根治見 `GC_BACKLOG.md` **GCB-07**。
逐列之 reasoning 須具名該豁免（五列已具名）。

## 6. CFTS092 疊層同句之取錨（R-CAM12）

CFTS092 之 Camera 節界：`SYS-RA-CAM-060`(4781625) Cargo/CHMSL、
**`-070`(4781635) Rear Camera**、`-083`(4781648) Surround View、
`-094`(4781659) Forward Facing、`-100`(4781665) Clearpath。
Test Group = `Rear View Camera` 之 TC 一律取 **Rear Camera 節**（`-070`～`-082`）之
ObjectID 為錨；其他節之逐字同句不得作錨（實測全本只有 `-062` ↔ `-075` 一組逐字同句）。

## 7. Layer 1–3（未鎖定）

Layer 1／Layer 2 之名稱歸 Pei（CAM-01 §4 任務 4 明文「不自行改 Layer 2 名稱」）。
本包只回填 leaf 數與逐列歸屬，見 `features/camera/data/layer2_assign.tsv`
與上繳包 `up/20260916_CAM-01.md` §5。

Layer 3（**不入工作簿**，IN §4.1.5）：

- **A 本** —— 以 SYS2 `VF章節` 欄逐字為 Layer 3。
  CFTS092 來源（33 列）該欄全空，依 §5 草案改以 §1.3.x 章名為 Layer 3。
  **VF551_V4 之補判見 §4.1。**
- **B 本** —— 以 SYS1 `Outline Number` 逐字為 Layer 3；B 本 `HMI Source ID`
  已內建該號，對映率 **100%**（母體：**cache 本** RVC+PAM，**R-CAM6**）。

### 7.1 VF551_V4 之 Layer 3 替代判法（DR-CAM-b）

V4 之 `VF章節`(I) 欄 **321/321 全空**。本包實測其 `Description`(D) 欄
**自帶前導章節號**（`1.1.1\tVehicle Function Area` 形態，60 列為 heading），
其餘列沿用最近之前一個 heading 號。以此向下繼承可得 **321/321 章節號、
60 個相異章節**；A 本實際引用之 44 列 V4 全數落在 5 個章節
（`1.10`／`1.10.2`／`1.10.2.1`／`1.10.2.2`／`1.10.2.3`）。

此法**毋須回查 docx**，較下放包所擬之 anchor 回查為輕。
交叉驗證：與結構同型之 V3（其 I 欄有值）比對同文字列，183 筆可比者中
**163 筆一致（89%）**，不一致者係兩份 VF 文件章節編號本不相同所致。
**[PROPOSED]** —— 採此法或仍回查 docx，見 DECISIONS §6。

### 7.2 訊號 raw 之查證順序（CAM-08 審閱 §一-6）

**第一步：以來源措辭逐字掃 PROXI 表／以訊號名（非訊息名）掃 DBC。**

- **PROXI**：來源之參數措辭常與 PROXI 表之參數名**逐字相同** ——
  `CAN node 27 (ASM/ASCM)`（`NR1L-RVC-138`）與 `Steering_Ratio_Rack_Pinion_Type`
  （`NR1L-RVC-164`）皆為其例，兩者初稿都誤判為「查無」。
- **DBC**：以**訊號名**掃，不以訊息名 —— 訊息名於 SYS2 與 DBC 常不同
  （`TRANSM2` ↔ `STATUS_CCAN5`、`ENGINE1` ↔ `STATUS_CCAN4`、`GE` ↔ `STATUS_CCAN5`，
  `batch03b` 三例），以訊息名掃會得到假的「查無」。
  大小寫亦須放寬（`LwsAngle` ↔ `LWSAngle`）。
  訊號名查得而訊息名不同者：**verbatim 逐字不改**（R-13），procedure／ER 改以 DBC 之承載訊息書寫，
  `Remarks` 欄註明兩者之差。訊號名本身查無者才標 `PENDING`。

寫 `<MSG>.<Signal> = <raw> (<label>)` 前，**先以訊號名自身**查四本 DBC 之 `VAL_`，
再決定寫法；**不得以同名近似之訊號代查**。

反例（CAM-08 §5-2 自報）：因先查了 `TGW_DISP_STATSts`（`BO_ 1500 TELEMATIC_DISPLAY2`）
而認定 `TGW_CAMERA_DISP_STAT` 無 `VAL_`，遂只寫 label，lint `P` 攔下 5 筆。
實測 `TGW_CAMERA_DISP_STAT` 自有其 `VAL_` ——
`TELEMATIC_FD_14`（`BO_ 1465`，FDCAN8）與 `RADIO_B2`（`BO_ 1282`，P363／637MCA）皆載
`0 "DISP_NON_CAMERA" 1 "DISP_DIGITAL_RVC_CAMERA" 2 "DISP_ANALOG_RVC_CAMERA" …`。

**LVDS 訊號（`vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation`）無 DBC**，
其值一律以來源 label 逐字書寫（§8.7.5(f)），不套 `<raw> (<label>)`。

### 7.3 無命令句式可抄時之書寫（CAM-09 審閱 §一-5，Pei 2026-09-23）

本 feature 有兩類觀察**於全語料查無可抄之命令句式**，一律以散文書寫，**不造命令**：

| 類 | 書寫 | 實測依據 |
|---|---|---|
| **DTC 之讀取** | `Read the DTC list with the diagnostic tool and check that …` | 交付語料 17 本之 275 條 `$ ` 命令行中與 `DTC` 同格者 **0**；`features/*/generated/` 全部 json 之 `$ ` 命令行共 **9 條，全在 camera 本身**（`adb logcat`／`dumpsys media.camera`）。Diagnostics 線之交付本不在本 repo |
| **LVDS 訊息之觀察** | `Read <message>.<Signal> and check that it is <label>`，Pre-Condition 先置 `A bus analyzer is connected to the LVDS link between the HU and the RVCM` | A-CA27 之加註：LVDS 相關之 `$ ` 命令行為 0（交付語料與 `sources/raw/*sysad*` 十本 docx 皆然）|

Pei 日後若提供 Diagnostics 線之交付本，DTC 側改抄其句式（記 DECISIONS）。
`adb` 兩行式（§5.4）只用於 **daemon／camera service 狀態**之觀察，其句式沿 pilot02 之既有用例。

### 7.4 摘句不可行時之處置（CAM-10 審閱 §一-1，Pei 2026-09-23）

下放包之升級條件「任一摘句無法在 50 token 內保留條件與結果子句」，
自 CAM-11 起改讀為 **「摘句不可行且*不可拆*時停」**：

1. 先試 **§8.2.2 之拆列** —— 來源之多個結果子句（`a.`／`b.`／…）為多個獨立驗證點時，
   拆為多列，每列之摘句 ＝ 共同條件 ＋ 該子句。拆列是正解，非規避。
2. 拆後每列仍逾 50 token 者，才是該條所指之「不可行」，停於回報。

實例：`SYS-RA-VF551_V2-486`（80 token，五個結果子句）——
併為一列時條件段約 39 token，任一子句 10～13 token，僅保留一個即已 51；
拆為五列後每列 32～35 token，皆為原句之保序子序列（`NR1L-RVC-131`～`-135`）。

**查表對映不適用等價類**（CAM-10 審閱 §一-4）：`V42-326` 型之「每個 PROXI 值 → 每個 LVDS 值」
為規格明定之獨立輸出，任一項錯即漏網（§7），故**全覆蓋、每項一列**，
不以 §8.3 之邊界＋代表值取代。

### 7.5 `PENDING` 與 lint `P` 之調和形制（CAM-11 審閱 §一-1，Pei 2026-09-23）

CAN 賦值步之值缺來源時，**不得**把 `PENDING` 寫成該步之開頭 ——
`P`（R-1 v2(a)）要求 Procedure 之 CAN 賦值行為 `Send CAN: <MSG>.<Sig> = <raw> (<label>)`；
而 selfcheck 第 8a 項要求 `PENDING:` 置於項或子項之行首。兩者之調和形制為：

```
1. Send CAN: BED_EXTENDER.BedExtenderSts = PENDING (Active)
a. PENDING: DR-CAM-f the raw value and VAL label for Active are not sourced
```

賦值行維持 `= <raw> (<label>)` 之形（`<raw>` 以 `PENDING` 佔位、`<label>` 為來源之逐字值），
說明移至 `a.` 子項之行首。兩項因而同時為 0。

沿革：CAM-11 初稿寫成 `1. PENDING: DR-CAM-f set X to Y`，`P` 由 0 升為 4；
改為本形制後兩者皆 0（CAM-11 上繳 §4-1）。

### 7.6 生成前之 ANOMALIES 預掃（CAM-13 審閱 §一-3，Pei 2026-09-23）

每批步驟 A 判軸之前，**先掃該 SWE 列相關之 `features/camera/ANOMALIES.md`**，
以免把已裁為「不可注入」之訊號再寫成 `Send CAN:` 步。
沿革：CAM-13 之 `-113` 用 `Send CAN: IPC_VEHICLE_SETUP.LanguageSelection`，
而 A-CA17（2026-09-16）已裁該訊號不走 CAN、觸發須改由 HMI 語言設定；自查後改寫。

掃法（逐列，母體為 `features/camera/ANOMALIES.md`）：

```
grep -n -i -e "<SWE-CAM-nnn>" -e "<該列所涉之訊號名>" features/camera/ANOMALIES.md
```

命中之項若其處置為「不走 CAN／不可注入」，該訊號**不得**出現於 `Send CAN:` 步；
改以 ANOMALIES 指定之替代觸發（HMI hop、治具、PROXI 設定）書寫，
無替代者以 §7.5 之形制掛 `PENDING`。

**selfcheck 第 9 項**為其機械化後衛，判準為兩條件**皆**成立：

1. 該訊號於 `sources/raw/camera_event_hal_status/*.xlsx` 之
   `Supported by Harman` 欄為 `N` **且** `MD fake CEH status` 欄含 `Not yet`
   —— 即 A-CA16 所稱之「兩者皆是」。只有 `N` 而 CEH 註 `could emulate`
   （如 `STATUS_BH_BCM2.CmdIgnSts`，profile §11.1 之 Atl-Mi 點火訊號）者**可**注入，不命中；
   註 `verified` 者（如 `IPC_VEHICLE_SETUP.DynamicGrid`）亦不命中。
2. `ANOMALIES.md` 有**同一列**同時提及該訊號名與「不可注入」或「不走 CAN」者。

兩條件取交集之由：CEH 表單獨為據時偽陽過多（初版判準 `N` **或** `Not yet`
＋ 訊號名出現於 ANOMALIES 任一處，240 列掃得 58 命中，經核幾乎全為可注入之訊號）；
收緊後 240 列命中 0（CAM-14 上繳 §1-1 之證據表）。

### 7.7 逐字母體須取全文（CAM-15 審閱 §一-5，Pei 2026-09-23）

**R-CAM17 之延伸**：`test_item` 上半之逐字母體、以及任何「來源如此寫」之主張，
其讀取**須取該列 `Description` 之全文**；不得以截斷輸出（`print(desc[:N])`、
終端折行、表格欄寬）判斷來源之內容。

沿革：CAM-15 之 `NR1L-RVCHMI-037` 初稿把 verbatim 寫成
`“X” soft control is presse`，並在 reasoning 裡斷言「來源末字缺 `d`」——
該截斷出自 CAM-14 時執行層自己的 `print(desc[:300])`，**來源本身完整**
（`“X” soft control is pressed (PU0361). In ANY OTHER GEAR, …`）。
重讀全文後改正（CAM-15 上繳 §6-3(a)）。

作法：讀 `Description` 時一律不切片；需要摘要輸出時，
**先把全文長度與 token 數印出來**，再決定摘句，且摘句之依據為全文而非輸出。

### 7.8 彈窗文字之 ER 形制（CAM-16 審閱 §一-6，Pei 2026-09-23）

來源條文轉指 Pop Up List 時，ER **陳述逐字文字並以括號附 PU 號**，
**不寫比較句** —— `matches`／`is the same as`／`is identical to` 皆為 lint `H`
（關係模糊語）與 `W`（比較關係而 test_item 上半無數值）之命中詞。

```
✗  The pop-up text matches PU0459 in the R1 HMI pop-up list
✓  The pop-up reads "No camera connected. Camera unavailable. Make sure camera is
   ON and within range" (PU0459 of the R1 HMI pop-up list)
```

**比對之判準只在 ER**，Procedure 只寫讀取動作（`Read the pop-up text on the HU display`），
不寫 `compare it word for word with …` —— 該句既是判準又在 Procedure，違 §5.4 之動作／判準分離。

彈窗文字**查無**者依 §7.5 之形制掛 `PENDING: DR-CAM-h`（該條已於 CAM-17 擴為
「Pop Up List 之 camera 相關缺件」兩項）。

沿革：CAM-16 之 B02a 初稿四列命中 `H`、三列命中 `W`，改為本形制後兩類皆 0（CAM-16 上繳 §4-1）。

## 8. framework 重開之 sha16 量測法（CAM-06 審閱 §一-1，Pei 2026-09-23）

`features/camera/framework.md` 之狀態行自載其重開後 sha16 —— 該值**自指**
（寫入即改變被量測之檔面），故量測法須明文且可複驗：

> 取本檔全文，將**狀態行中最後一個 sha16 欄位**以 16 個 `0` 代入，
> 對該字串取 UTF-8 sha256，前 16 碼即為所載之值。

複驗：

```bash
python3 - <<'EOF'
import hashlib
s = open('features/camera/framework.md', encoding='utf-8').read()
print(hashlib.sha256(s.replace('<所載之 sha16>', '0'*16).encode()).hexdigest()[:16])
EOF
```

沿革：`c4fc9d2e5b7d1f44`（重開前，非自指，為一般檔案 sha16）→
`ee74d26960d6c281`（CAM-06 重開落檔）→ `8569aa484b552b7c`（CAM-07 §1-8 例外註擴充）。
**重開前之值不適用本量測法** —— 該時狀態行尚無 sha 欄位。

`rulings_hash.py` 之條文指紋不適用於本檔（framework 非 ruling 錨點檔），
兩者之量測口徑不可混用。

---

## 9. 標定常數表（實測，CAM-06／CAM-07 查得；CAM-07 審閱 §一-9 記入）

逐格實測之值，**交付前之複驗以本表為準**；TC 之 ER 不再留符號。

| 常數 | 值 | 單位 | 適用 | 座標（SYS-RA id：名／值／單位）|
|---|---|---|---|---|
| `c_VEHSPD_MAX` | **8** | `mph` | Atl-Hi（V2）、376（V3）| V2 §1.8.13 `-139`／`-138`／`-135`；V3 §1.14.1 `-607`／`-608`／`-611` |
| `MAX_SPEED` | **13,0** | `Km/h` | 2261（V33）、637（V42）| V33 §1.14.1 `-503`／`-504`／`-507`；V42 §1.14.1 `-655`／`-656`／`-659` |
| `T_INITDISPLAY` | **5,0** | `sec` | 2261（V33）、637（V42）| V33 §1.14.1 `-479`／`-480`／`-483`；V42 `-631`／`-632`／`-635` |
| `Tpower` | **5** | `sec` | Atl-Hi（V2）、Atl-Mi（V3）| V3 §1.14.1 `-583`／`-584`／`-587`；V2 §1.8.13 `-163`／`-162` |
| `Reverse_Deb` | **750** | `ms` | Atl-Hi（V2）| V2 §1.8.13 `-151`／`-150`／`-147` |
| `TIME_W_RVC` | **2,5** | `sec` | 2261（V33）、637（V42）| V33 §1.14.1 `-515`／`-516`／`-519` |
| `TIME_W_RVC2` | **50** | `ms` | 2261（V33）| V33 §1.14.1 `-587`／`-588`／`-591`（範圍 `[50;100]`、容差 `10`）|
| `RESPONSE_TIME` | **2,0** | `sec` | 637（V42）| V42 §1.14.1 `-679`／`-680`／`-683` |
| `Time_POWER` | **500** | `ms` | 637（V42）| V42 §1.14.1 `-739`／`-740`／`-743` |
| `Tpower`（V42）| **5** | `sec` | 637（V42）| V42 §1.14.1 `-703`／`-704`／`-707` —— 與 V2／V3 同值 |

**兩個速度門檻為同一門檻之兩種標定**：8 mph ＝ 12.874752 km/h，與 13,0 km/h 相差
0.125 km/h，落在 V33／V42 所載之 ±`0,5` 容差內（`-506`／`-658`）。
其可判性之差異見 A-CA30／A-CA31：Atl-Hi 側「恰等於 8 mph」之 raw 不存在
（12.874752 非 0.0625 之倍數），2261／637 側 13.0 ÷ 0.0625 ＝ 208 為整數點，存在。

V33／V42 之表以**逗號為小數點**（`13,0`／`5,0`），TC 之 Pre-Condition 逐字照錄該寫法，
procedure 之 raw 換算則以小數點書寫（`13.0625 km/h`）。

---

## 10. `remarks` 欄之用途（CAM-12 審閱 §二-6，Pei 2026-09-23）

json 之可選 `remarks` 欄寫入工作簿之 **`AH` 欄（Remarks 備註）**，
其用途**限下列三類**，不得作一般註解：

| 類 | 句式 | 實例 |
|---|---|---|
| **來源與 DBC 名稱差異** | `Source names the message X; the DBC carries <Sig> in Y (BO_ n). See DR-CAM-f.` | `-175`／`-176`／`-178`／`-201`／`-239`／`-240` |
| **疑似誤植** | `Condition per source text; suspected typo, see RDF-nn` | `-170` |
| **需特殊治具** | 該列之執行需模擬器／量測治具者（與 `bench_verify.md` 對應）| —— |

`remarks` **不取代 reasoning** —— reasoning 為生成之依據（不入工作簿），
`remarks` 為執行者於工作簿上所需之提醒（入工作簿）。

---

## 11. 車型軸（R-CAM3）與品牌軸（R-CAM5）

拆分判準逐字見 `features/camera/RULINGS.md` R-CAM3、R-CAM5。
平台 ↔ VF ↔ PROXI 對照表同檔；品牌對照見本檔 §3.2。
二軸同時成立時**以車型軸為外層**（R-CAM5(d)）。
`forms/proxi/` 六平台十檔**不得改名、不得移動**（CAM-01 §0）。

### 11.1 Ignition 前提之訊號（CAM-01 審閱 §二-1 更正，CAM-02 §2 任務 6）

`SWE-CAM-002` 之 Ignition 前提**不得用 `BCM_FD_9.PowerModeSts`**
（CameraEventHal 表：Atl-H、`Supported by Harman = N`、`MD fake CEH status
= Not yet`，不可注入）。依 EE 分列：

| EE | 訊號 | CEH 表之狀態 |
|---|---|---|
| Atl-Hi | `BCM_FD_10.CmdIgnSts` | `Y`／`verified` |
| Atl-Mi | `STATUS_BH_BCM2.CmdIgnSts` | `N`／`Could emulate` |

CAM-01 上繳 §3.9 曾記「Atl-Hi 側無對應之 `CmdIgnSts` 列」—— **不成立**，
`CameraEventHal status.xlsx` 第 7 資料列即 `BCM_FD_10.CmdIgnSts | input |
Atl-H | Y | verified`。該未結項關閉。

---

## 12. 未決（本檔不得自行補齊）

CAM-01 之七項未決**全數已裁**（R-CAM4～R-CAM8、DECISIONS §6-6）。
CAM-02 新生之未決：

| # | 項 | 標記 |
|---|---|---|
| 1 | 車型 ↔ 品牌之權威來源（R-CAM5(c) 指定之 Market Config Table 無此欄；本檔 §3.2 以 PROXI 實測替代）| `[PROPOSED]` DR-CAM-e |
| 2 | Abarth（Fastack 376）無 Brand-Specific 欄，回落基礎 label 之讀法 | `[PEI]` A-CA19 |
| 3 | `SWE-CAM-025` 之畫面文字：037 作 `Camera Not in position`，SYS1 §9.2.3 作 `Camera Out of Position` | `[PEI]` A-CA20 |
| 4 | `SWE-CAM-023` 與 6 列之交集承接順位 | `[PEI]` —— 審閱 §三-10：待 framework 鎖定時定 |
| 5 | `VF617_V5` 缺件 | DR-CAM-a（**高**）|
