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

## 5. `test_item` 上半逾 50 token 之摘句（§4.3.1）

**逾限不是改驗證點之理由**（CAM-04 審閱 §二-3）。摘句以「與括號下半之測試目的
直接相關之句」為限，須**同時保留條件子句與結果子句**，全文以
`specification_reference` 指回。摘後須為原句 token 之**保序子序列**
（不得改寫用字；句首字母轉大寫屬排版正規化，R-4）。

案例（`SYS-RA-VF551_V3-260`，V3 §1.10.2.2，51 → 33 token）：刪行首列點符號 `· `
與末尾逐字重複之 `a)` 子句，保留 `when STATUS_BH_BCM2.CmdIgnSts = [RUN] AND
Gear_Stat.info = [REVERSE] > Reverse_Deb` 與 `the Head Unit shall display the RVC
image … Automatic mode`。全量另五例見 `up/20260916_CAM-05.md` §2.3。

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

## 9. 車型軸（R-CAM3）與品牌軸（R-CAM5）

拆分判準逐字見 `features/camera/RULINGS.md` R-CAM3、R-CAM5。
平台 ↔ VF ↔ PROXI 對照表同檔；品牌對照見本檔 §3.2。
二軸同時成立時**以車型軸為外層**（R-CAM5(d)）。
`forms/proxi/` 六平台十檔**不得改名、不得移動**（CAM-01 §0）。

### 9.1 Ignition 前提之訊號（CAM-01 審閱 §二-1 更正，CAM-02 §2 任務 6）

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

## 10. 未決（本檔不得自行補齊）

CAM-01 之七項未決**全數已裁**（R-CAM4～R-CAM8、DECISIONS §6-6）。
CAM-02 新生之未決：

| # | 項 | 標記 |
|---|---|---|
| 1 | 車型 ↔ 品牌之權威來源（R-CAM5(c) 指定之 Market Config Table 無此欄；本檔 §3.2 以 PROXI 實測替代）| `[PROPOSED]` DR-CAM-e |
| 2 | Abarth（Fastack 376）無 Brand-Specific 欄，回落基礎 label 之讀法 | `[PEI]` A-CA19 |
| 3 | `SWE-CAM-025` 之畫面文字：037 作 `Camera Not in position`，SYS1 §9.2.3 作 `Camera Out of Position` | `[PEI]` A-CA20 |
| 4 | `SWE-CAM-023` 與 6 列之交集承接順位 | `[PEI]` —— 審閱 §三-10：待 framework 鎖定時定 |
| 5 | `VF617_V5` 缺件 | DR-CAM-a（**高**）|
