# FW036 R1L Camera — Profile（骨架）

- 設立依據：下放包 **CAM-01 §4 任務 5**（`docs/fw036/handoff/down/20260916_CAM-01.md`）。
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
| `spec_reference`（N 欄）| A 本引 CFTS092／VF551；B 本引 SYS1 HMI L&F 章節 | **R-CAM1(c)** |
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

## 2. `[ADD]` Vehicle Model 七欄檢查（R-CAM2(c)）

判準逐字取 R-CAM2：

- (a) `Vehicle Model 車型` 七子欄每列填 `1` 或 `0`，**不留空、不用其他符號**。
  七欄為 `HDCC27 Atl-Hi`／`DT27 Atl-Hi`／`VF(ProMaster)637 Atl-Mi`／
  `Commander (598) Atl-Mi`／`Regengade (5210) Atl-Mi`／`Toro(2261) Atl-Mi`／
  `Fastack (376) Atl-Mi`。
- (b) `Commander (598)` 與 `Regengade (5210)` 兩欄 **一律 `0`**（Camera 兩本）。
- (c) 其餘五個有效車型欄，**每列至少一個 `1`**。

違例等級：**ERROR**（(a)(b) 為硬條件）／**ERROR**（(c) 空列無意義）。
代號指派：`lint036.CHECK_TITLES` 現已佔用至 `Y`；本項候選代號
**`Z`**（2026-09-16 現查 `CHECK_TITLES` 無 `Z`）—— 指派前須依 A-GC16 之教訓
再查一次現況，不得沿用本檔之記載。**[PROPOSED]**

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

### 3.1 hop label 之星號 `*` —— 本包已查明，建議不入 hop

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

## 4. Layer 1–3（未鎖定）

Layer 1／Layer 2 之名稱歸 Pei（CAM-01 §4 任務 4 明文「不自行改 Layer 2 名稱」）。
本包只回填 leaf 數與逐列歸屬，見 `features/camera/data/layer2_assign.tsv`
與上繳包 `up/20260916_CAM-01.md` §5。

Layer 3（**不入工作簿**，IN §4.1.5）：

- **A 本** —— 以 SYS2 `VF章節` 欄逐字為 Layer 3。
  CFTS092 來源（33 列）該欄全空，依 §5 草案改以 §1.3.x 章名為 Layer 3。
  **VF551_V4 之補判見 §4.1。**
- **B 本** —— 以 SYS1 `Outline Number` 逐字為 Layer 3；B 本 `HMI Source ID`
  已內建該號，對映率 100%（母體：**cache 本** RVC+PAM，見上繳包 §3）。

### 4.1 VF551_V4 之 Layer 3 替代判法（DR-CAM-b）

V4 之 `VF章節`(I) 欄 **321/321 全空**。本包實測其 `Description`(D) 欄
**自帶前導章節號**（`1.1.1\tVehicle Function Area` 形態，60 列為 heading），
其餘列沿用最近之前一個 heading 號。以此向下繼承可得 **321/321 章節號、
60 個相異章節**；A 本實際引用之 44 列 V4 全數落在 5 個章節
（`1.10`／`1.10.2`／`1.10.2.1`／`1.10.2.2`／`1.10.2.3`）。

此法**毋須回查 docx**，較下放包所擬之 anchor 回查為輕。
交叉驗證：與結構同型之 V3（其 I 欄有值）比對同文字列，183 筆可比者中
**163 筆一致（89%）**，不一致者係兩份 VF 文件章節編號本不相同所致。
**[PROPOSED]** —— 採此法或仍回查 docx，見 DECISIONS §6。

## 5. 車型軸（R-CAM3）

拆分判準逐字見 `features/camera/RULINGS.md` R-CAM3。
平台 ↔ VF ↔ PROXI 對照表同檔。
`forms/proxi/` 六平台十檔**不得改名、不得移動**（CAM-01 §0）。

---

## 6. 未決（本檔不得自行補齊）

| # | 項 | 標記 |
|---|---|---|
| 1 | ABBR：A／B 共用 `CAM` 或 B 本另取 | `[PEI]` |
| 2 | B 本 Test Group = `Camera` 或 `Camera HMI` | `[PEI]` |
| 3 | `*` 入 hop 與否（§3.1 已備證據與建議）| `[PEI]` |
| 4 | RVC+PAM 同名異體用 REF 本或 cache 本（§4 依 cache 本量得 100%）| `[PEI]` |
| 5 | V4 Layer 3 用 D 欄推導或 docx 回查（§4.1）| `[PEI]` |
| 6 | `ENTER_CAMERA_SETTINGS` 第 3 hop 之權威（§3）| `[PEI]` |
| 7 | Vehicle Model 檢查之 lint 代號（§2 候選 `Z`）| `[PROPOSED]` |
