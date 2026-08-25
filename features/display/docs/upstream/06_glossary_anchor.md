# 上繳包 06 —— 縮寫錨、聚合複查、037 精讀與 Polarion 分頁清償

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/06_glossary_anchor.md`
- 結果：**步驟 1–10 全數執行；十七條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §11 只備妥訊息與 pathspec，未執行

---

## 1. §四四條之抄錄核對表（步驟 1）

**Display 兩條 → `features/display/RULINGS.md`**：

| # | 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|
| 24 | R-DM22 | 909 | `cdb1b47b562eb2ba` | 是 |
| 25 | R-DM23 | 466 | `96a2c13ba4368e6f` | 是 |

**全域兩條 → `docs/fw036/RULINGS_LEDGER.md`**：

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G16 | 527 | `14f1899d59fe6b0f` | 是 |
| R-G13 補充 | 337 | `fd7f12de11704a94` | 是 |

**4/4 逐字元相符**；Display 累計 **25/25**。`R-G13 補充` 併於原條之下，
**R-G13 原文一字未動**。

### 1.1 R-DM22 之基礎已獨立複驗

條文所引之並列句，本輪自 `inputs/` 之 037 複本逐字讀出：

- r14（`SWE-DM-007`）：`The Display Management software shall transition
  display state to Rear View Camera (RVC) mode when reverse gear signal is
  detected under static vehicle condition.`
- r15（`SWE-DM-008`）：`...between operational HMI screen and Rear View
  Camera (RVC) display during runtime conditions.`

**逐字存在，非推定。** 八條中僅此二條含 `RVC`／`Rear View`。

---

## 2. `glossary.tsv` 全文與出處引句（步驟 2）

### 2.1 一處實作缺陷之自我更正 —— 我的擷取式製造了假衝突

首版以「括號前最多 6 個詞」為展開，得 25 個縮寫、142 處，且
**停止條件 16 報出六組衝突**，例如 `RVC` 同時得到
`'Rear View Camera'`、`'there is no high priority screen'`、
`'Upon dismissing high priority screen'`。

那些不是來源的分歧，是我的貪婪匹配。CFTS 之
`if a high priority screen (RVC) is active` 與
`Rear View Camera (RVC)` 有相同的括號形態。

改用逐字可驗之判準：**候選詞之首字母須逐一拼出該縮寫**
（`Rear View Camera` → R,V,C = RVC 收；`high priority screen` → h,p,s
≠ RVC 棄）。這是對來源字元本身的檢驗，不是相似度分數。
另允許 `of/and/the/for/with/to/a/an/in/on` 等小寫連接詞被跳過，
且**逐條記錄是否用到該讓步**（`initials_rule` 欄：strict／filler-skipped）。

修正後：**13 個縮寫、85 處出現、全部 strict、無任何衝突。**

> 若我沒有察覺而照報，會以「六組衝突」觸發停止條件 16，把一個
> 本不存在的問題送回分析層。**這是第四次同型缺陷：擷取階段過寬，
> 而輸出「看起來像個發現」。**

### 2.2 停止條件 16：**未觸發**（無縮寫有兩種展開）

```
## 逐條（每個縮寫取其首處出現為出處，出現次數另計）
| abbrev | expansion | 首字母判準 | usable(>=2 詞) | 出現處數 | source_file | source_locator |
|---|---|---|---|---|---|---|
| CCDMF | Comfort Controls Display Module Front | strict | Y | 11 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 32 [(前言)] |
| CCDMR | Comfort Controls Display Module Rear | strict | Y | 7 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 33 [(前言)] |
| DCSD | Disassociated Center Stack Display | strict | Y | 10 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 30 [(前言)] |
| DHCP | Dynamic Host Configuration Protocol | strict | Y | 1 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 2836 [1.8.6.1 Police PCs and Optional 2+ Port ] |
| DPU | Display Processing Unit | strict | Y | 2 | SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx | SYS3 para 95 [系統分解 System Decomposition] |
| ECC | Electronic Climate Control | strict | Y | 14 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 977 [1.5.1 ICS HMI Communication {4819357}] |
| FPDM | Front Passenger Display Module | strict | Y | 7 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 31 [(前言)] |
| HDCP | High-bandwidth Digital Content Protection | strict | Y | 4 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 2649 [1.8.5.1 Ethernet requirements {4819954}] |
| HU | Head Unit | strict | Y | 14 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 38 [(前言)] |
| ICS | Integrated Center Stack | strict | Y | 9 | SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx | SYS2 Basic Report r28c14 |
| LVDS | Low Voltage Differential Signal | strict | Y | 2 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 40 [(前言)] |
| RVC | Rear View Camera | strict | Y | 3 | Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx | 037 SWE1 Requirements r14c4 |
| UDS | Unified Diagnostic Services | strict | Y | 1 | R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx | CFTS_020 para 2605 [1.8.5.1 Ethernet requirements {4819954}] |

```

### 2.3 出處引句（cooccurrence_quote）

```
## 引句（cooccurrence_quote）

### CCDMF = Comfort Controls Display Module Front
  [CFTS_020 para 32 [(前言)]] 4 Comfort Controls Display Module Front (CCDMF) - Lost Communication With Body Control Module {4819170} 16

### CCDMR = Comfort Controls Display Module Rear
  [CFTS_020 para 33 [(前言)]] 5 Comfort Controls Display Module Rear (CCDMR) - Lost Communication With Body Control Module {4819177} 17

### DCSD = Disassociated Center Stack Display
  [CFTS_020 para 30 [(前言)]] 2 Disassociated Center Stack Display (DCSD) - Lost Communication With Body Control Module {4819156} 15

### DHCP = Dynamic Host Configuration Protocol
  [CFTS_020 para 2836 [1.8.6.1 Police PCs and Optional 2+ Port ]] The DCSD shall contain a DHCP (Dynamic Host Configuration Protocol) server.

### DPU = Display Processing Unit
  [SYS3 para 95 [系統分解 System Decomposition]] The DRM driver programs the Display Processing Unit (DPU) to generate the final RGB display data.

### ECC = Electronic Climate Control
  [CFTS_020 para 977 [1.5.1 ICS HMI Communication {4819357}]] In the CIP A&T architecture a VP2 System that uses an HU with integrated Volume and Scroll knobs does not make use of an ICS component and the HVAC related hardkeys and knobs that are in the CIP VP3 System and VP4 System interface directly to the Electronic Climate Control (ECC) component.

### FPDM = Front Passenger Display Module
  [CFTS_020 para 31 [(前言)]] 3 Front Passenger Display Module (FPDM) - Lost Communication With Body Control Module {4819163} 16

### HDCP = High-bandwidth Digital Content Protection
  [CFTS_020 para 2649 [1.8.5.1 Ethernet requirements {4819954}]] The HU shall support High-bandwidth Digital Content Protection (HDCP) v1.

### HU = Head Unit
  [CFTS_020 para 38 [(前言)]] 10 Head Unit (HU) - Lost Communication with ICS {4819212} 20

### ICS = Integrated Center Stack
  [SYS2 Basic Report r28c14] pdf FastBack: DTC Code and details section for Lost Communication with ICS (Integrated Center Stack): U175087 Reference file: D3208_LTM-R1Low_8.

### LVDS = Low Voltage Differential Signal
  [CFTS_020 para 40 [(前言)]] 12 Disassociated Center Stack Display (DCSD) - Low Voltage Differential Signal (LVDS) Video Cable {4819226} 21

### RVC = Rear View Camera
  [037 SWE1 Requirements r14c4] The Display Management software shall transition display state to Rear View Camera (RVC) mode when reverse gear signal is detected under static vehicle condition.

### UDS = Unified Diagnostic Services
  [CFTS_020 para 2605 [1.8.5.1 Ethernet requirements {4819954}]] 00043 Standard Unified Diagnostic Services (UDS) on Ethernet CS.

```

### 2.4 下放包指名之九個縮寫 —— 逐一回報

```
## 下放包 06 步驟 2 指名之縮寫 —— 逐一回報
  DCSD: 查得並列 → 'Disassociated Center Stack Display'（10 處，usable=Y）
  ICS: 查得並列 → 'Integrated Center Stack'（9 處，usable=Y）
  HU: 查得並列 → 'Head Unit'（14 處，usable=Y）
  FPDM: 查得並列 → 'Front Passenger Display Module'（7 處，usable=Y）
  LVDS: 查得並列 → 'Low Voltage Differential Signal'（2 處，usable=Y）
  SK: **查無並列** —— 依 R-DM22 不建條目
  TGW: **查無並列** —— 依 R-DM22 不建條目
  SGW: **查無並列** —— 依 R-DM22 不建條目
  ETM: **查無並列** —— 依 R-DM22 不建條目
  RVC: 查得並列 → 'Rear View Camera'（3 處，usable=Y）

```

`SK`／`TGW`／`SGW`／`ETM` 四者在四份素材中**查無並列**，依 R-DM22
不建條目 —— 不以領域常識填入（canon §8.4.1）。

---

## 3. 重跑後之覆蓋對照，`glossary_phrase` 單獨列示（步驟 3）

舊檔依 R-TM13 保留為 `data/coverage_sys2_vs_swe_dm.PRE_GLOSSARY.tsv`
（檔頭加註），未刪除。

```
## candidate_from 分布（哪一種錨產生了候選）
  heading only      : 4
  glossary only     : 12
  兩者皆有          : 0
  無候選            : 64

## anchor_kind 分布（最高優先之現存錨）
  signal: 43
  heading: 37

## candidate_leaf 分布（候選，非裁定）
  SWE-DM-001 (State Management): 0
  SWE-DM-002 (Wake-up Management): 0
  SWE-DM-003 (Startup & Wake-up Handling): 0
  SWE-DM-004 (Thermal Management): 4
  SWE-DM-005 (Thermal Protection Management): 4
  SWE-DM-006 (HMI Popup Management): 0
  SWE-DM-007 (RVC Management): 12
  SWE-DM-008 (Dynamic Display Arbitration): 12
  有候選之列: 16
  無候選之列: 64　—— R-DM23 語意別 **(3) 方法之界線**（兩錨皆施用而未接上），非查無、非未追查
```

### 3.1 先算後比之結果

分析層 §2.3 之對照值為「SYS2 `Description` 含 `Rear View Camera` 者 24 列」。
本輪先算，得 **12**。差異已查明並**非不符**：

| 母體 | 含 `Rear View Camera` |
|---|---|
| `Basic Report` 全 333 資料列 | **24** |
| 其中 `Category = functional requirement`（本對照之母體 80 列） | **12** |
| 其中 `Category = heading` | **0** |

分析層之 24 是全表之數，本對照之母體是 80 列 FR。**兩數皆對，母體不同。**
`SWE-DM-007`／`008` 各得 12 列候選（同一批列，兩 leaf 皆用 `RVC`）。

### 3.2 一項須回報之設計後果：`glossary_phrase` 在 `anchor_kind` 中永不出現

下放包指定其優先序置於 `heading` 之後。但**每一列都有 heading 祖先**
（80/80），故 `anchor_kind` 之最高優先者永遠輪不到 `glossary_phrase`：

```
anchor_kind 分布：signal 43 / heading 37 / glossary_phrase 0
```

錨**確實生效**（候選由 4 列增為 16 列），只是在 `anchor_kind` 欄看不見。
本輪另立 **`candidate_from`** 欄承載此資訊：

```
heading only 4 / glossary only 12 / 兩者皆有 0 / 無候選 64
```

依 R-DM12，引用候選時須連同 `candidate_from` 一併引用；
單看 `anchor_kind` 會得出「glossary 錨沒作用」之相反結論。
**優先序是否要改（如置於 heading 之前），請裁示。**

---

## 4. `proxi_candidates.tsv` 之 `related_leaf` 更新（步驟 4）

**仍然全空。** `glossary_phrase` 在 446 列中 0 命中。

成因與 SYS2 側不同 —— 逐字檢查 LID `Proxi & Configuration` 分頁：

| 字串 | 出現次數 |
|---|---|
| `Rear View Camera`（空格） | **0** |
| `Rear_View_Camera`（底線） | 2 |
| `Rear Camera` | 1 |

展開後之 `Rear View Camera` 與 `Rear_View_Camera` **逐字不等**。
依 **R-DM22(c)**「展開後仍不逐字相符者，即為不相符，不得再放寬一層」，
執行層**未**加入底線↔空格之正規化。已以 **A-DM19** 登記並提請裁示。

> 縮寫錨解開了 SYS2 側（0 → 12），但 PROXI 側的阻塞從來就不是縮寫，
> 是分隔符。兩者都是「封閉且可稽核之逐字規則」，但我不能自己把第二條
> 也開了 —— 那正是 R-DM22(c) 所禁之「再放寬一層」。

---

## 5. R-DM23 之三處語意別補註（步驟 5）

| 輸出 | 空值／`none` 之列數 | 語意別 | 依據 |
|---|---|---|---|
| `coverage_sys2_vs_swe_dm.tsv` | 64 列無候選 | **(3) 方法之界線** | heading 與 glossary 兩錨皆已施用而未接上；未經任何「不存在」之查證 |
| `proxi_candidates.tsv` | `related_leaf` 空 446 列 | **(2) 本輪未追查** | 只追了 A-DM16 指名之三個起點，其餘從未被調查 |
| `signal_resolution.tsv` | `resolved = N` 2 列 | **(1) 已查證不存在** | R-G13 三要件齊備，已登入 `LOOKUP_MISSES.md` M-1／M-2 |

三者各自新增欄位承載（`empty_semantics`／`n_semantics`），
**不共用同一個表示**。腳本之統計輸出亦同步印出其語意別。

> `proxi_candidates.tsv` 之 446 全部標 (2)，包括那 176 列已在 PROXI
> 查得定義者 —— 「查得其值域」與「追查過它是否與 leaf 相關」是兩件事，
> 前者做了，後者沒有。

---

## 6. R-G16 對自有腳本之複查（步驟 6）

`features/display/scripts/` 現有 **14 支**（前輪報 10 支，本輪新增
`read_037_leaves.py`／`build_glossary.py`，加上 04／05 輪之三支）。
其中**寫檔者 6 支**，逐支複查 (a)(b)(c)：

| 腳本 | (a) 分隔符 | (b) 多值處理 | (c) 選定判準留痕 | 處置 |
|---|---|---|---|---|
| `coverage_map.py` | `values`/`signals`/`documents` 已用 ` ¦ `；**`candidate_leaf`／`melco` 仍用逗號** | 候選多值合併於一格，但 `note` 欄逐 leaf 保留未合併之依據 | heading 祖先為位置性；glossary 命中逐條記於 `note` | **改用 ` ¦ `** |
| `proxi_candidates.py` | **`proxi_row`／`related_leaf`／`keyword_note` 用逗號** | 多值鍵已逐值嘗試並記於 `lookup_key` | `lookup_key` 記命中之查詢鍵 | **改用 ` ¦ `** |
| `signal_resolution.py` | 無多值串接（逐值一列） | 已逐值一列 | **僅記結果，未記選定判準** | **補記** `選定判準：MESSAGE.Signal 兩半皆相等 → <DBC>` |
| `sys2_heading_tree.py` | **`child_rows` 用逗號** | 子列本為多值 | 位置性規則已於 docstring 載明 | **改用 ` ¦ `** |
| `lid_version_diff.py` | 列號用逗號；訊號名已用 ` ¦ ` | 已 frozenset 逐值比對 | 三分判準已載明 | **列號改用 ` ¦ `** |
| `build_glossary.py` | 單值欄，無串接 | 逐條一列 | `initials_rule` 欄記 strict／filler-skipped | 無須修 |

### 6.1 還原檢查（R-G16 驗收方式）—— 停止條件 17 **未觸發**

修正前後之筆數：

| TSV | 修正前 | 修正後 |
|---|---|---|
| `coverage_sys2_vs_swe_dm.tsv` | 80 | **80** |
| `proxi_candidates.tsv` | 446 | **446** |
| `signal_resolution.tsv` | 26 | **26** |
| `sys2_heading_tree.tsv` | 45 | **45** |
| `glossary.tsv` | 13 | **13** |
| `lid_v178_vs_v176.tsv` | 2548 | **2548** |

**六份全部一致**，且各自可由其擷取階段之母體還原：
80 = SYS2 FR 母體；446 = LID Proxi 資料列；26 = 15 個訊號經 LID 展開後之
`MESSAGE.Signal` 值數；45 = SYS2 Heading 列數；13 = 通過首字母檢驗之縮寫數；
2548 = 兩版 LID 之 Logical Identifier 聯集。

> 逗號串接在本輪之六份中**恰好都不會出錯**（串的是 id 與列號，皆不含
> 逗號）。改掉不是因為它壞了，是因為 R-G16(a) 要求分隔符不得為資料中
> 可能出現之字元 —— 上一次它壞掉時，也是「恰好不會出錯」直到不是。

---

## 7. PROXI 兩個 NODE 欄之實測與可用性判定（步驟 7）

| 欄 | 非空 | 相異值 | 形態 | 判定 |
|---|---|---|---|---|
| `Used by NODE(VFXXX)` | **500 / 1058** | 311 | `BSM (VF381_V1); TBM (VF684_V3);` | **結構上可用，但缺鑰匙** |
| `Checked by NODE(CHECK)` | **6 / 1058** | 4 | `All nodes (1,4)`／`IPC(2), BCM(2)`／`DMSM (6)` | **不可用** |

- `Checked by NODE(CHECK)`：6/1058 之覆蓋率下，空值不帶任何資訊 ——
  依 R-G13 之涵蓋範圍要件，以其空值推論任何事都不成立。
- `Used by NODE(VFXXX)`：形態規整（節點名 + 括號內 VF 清單，分號分隔），
  切分後 155 個形如 `VFnnn(_Vn)` 之 token。**要用它篩「本專案適用」，
  須先知道本專案是哪個 VF —— 該資訊不在四份素材內。** 開 **DR-DM7**。

本 feature 三個已查得之 PROXI 列，其 `Used by` **皆含 `ETM`**，
而 `ETM` 正是 BHCAN2 中三個顯示訊號之發送節點（A-DM14）。
**此為觀察，非「本專案為 ETM 架構」之認定。**

> r401 之 VF 清單含 `VF230_V1`，而 `features/vehicle_setting/` 之產出檔名
> 為 `_vf230_*`。**未推定 VF230 即本專案之 VF** —— 那是跨 feature 推定，
> 且 vehicle_setting 之 VF 未必等於 Display 之 VF。

---

## 8. 037 八條之逐條精讀（步驟 8，積欠四輪）

全文見 `scripts/read_037_leaves.py` 之輸出。結構性實測：

| 項 | 八條之實測 |
|---|---|
| 數值＋單位（門檻之形態） | **0 / 8**（逐條皆 0） |
| `$Signal$` token | **0 / 8** |
| 外部文件／id 引用 | **0 / 8** |
| 句號後缺空格之併句（`x.Y`） | **8 / 8**（每條恰 1 處） |
| `SYS2 Traceability` 之 `Source NRL ID(s)` | 8/8 空（複驗 A-DM3） |

三項後果（已以 **A-DM18** 登記）：

1. **R-DM8 只列四處缺值（003/004/005/006），實際八條全無具體值。**
   例 `SWE-DM-001` 之描述含 `based on system operational requests and
   **timeout conditions**` —— timeout 之值未載，而該條不在 R-DM8 之四處中。
2. **R-DM14／R-DM17 之「037 不含訊號層資訊」由抽樣升為全稱**：8/8 皆 0。
3. **八條皆為兩句併寫**，第二句多為「回復／還原」語意
   （restore／resume／ensure）。以句號斷句之實作會把兩句併為一句，
   使回復語意附著於第一句之條件之下。

另記命名落差：037 用 `DISPLAY_ON`／`DISPLAY_OFF`（001、002），
SYS2 與 DBC 用 `DISP_ON`／`DISP_OFF`。逐字不等，且**無 `(...)` 並列可引**，
故 R-DM22 之 glossary 無法建條目。

### 8.1 本步驟未做之事

未產出 TC、未作範圍裁定（步驟 8 明文）。
`Verification Criteria` 欄雖已一併列出，但依 R-DM8 末段
**僅作參考輸入，本輪未用於任何判斷**。

---

## 9. SYS2 `Polarion`／`_polarion` 兩分頁（步驟 9，積欠四輪）

### 9.1 兩分頁之內容與用途

| 分頁 | dims | 非空列 | 內容 |
|---|---|---|---|
| `Polarion` | 88 × 2 | 87 | `Property/Value` 與 `Column/Field` 兩段：工作項型別、註解欄式樣，以及**每個中文欄名對應之 Polarion field id**（如 `SYS2 DT27 Atl-Hi` → `20217`） |
| `_polarion` | 372 × 6 | 368 | **欄位合法值之字典**：`Type / Label / ID / Field`，涵蓋 **341 個欄位**之列舉值 |

### 9.2 這是四輪來最有價值的一次補課 —— A-DM4 因此升級

`_polarion` 載 `SYS2 分類 Category` 之合法值逐字為五個：

```
Heading / Information / Functional Requirement /
Non Functional Requirement / Out of scope
```

以此複驗 `Basic Report` 之 333 列實際用值：

| 實際值 | 列數 | 在字典中 |
|---|---|---|
| `Out of Scope` | **116** | **否** |
| `Information` | 85 | 是 |
| `Functional Requirement` | 79 | 是 |
| `Heading` | 45 | 是 |
| `Out of scope` | 7 | 是 |
| `Functional requirement` | **1** | **否** |

**117 列（35%）之 Category 值不在該匯出檔自己的合法值清單中，
且違規的是多數拼法。**

三項後果：

1. A-DM4 原提案「一律正規化大小寫」**取得逐字之權威依據** ——
   字典說 `Out of scope` 才合法，不再只是執行層之便宜行事。
2. **`Non Functional Requirement` 合法但 0 列** —— 由此可確認 R-DM7 之
   覆蓋母體（`Functional Requirement` 80 列）**未遺漏 NFR**。
   此前四輪無人驗過這件事。
3. 向上游反映之措辭應改為「值未依 `_polarion` 字典校驗」，
   而非「大小寫不一致」——後者聽起來像格式瑕疵，前者是資料校驗缺口。

**兩分頁皆不含本 feature 之需求內容**，其價值在於**校驗**而非追溯。

---

## 10. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 6 項。**

1. **PROXI 之 269 列（現標 (2) 未追查）仍無人排程。** R-DM23 讓它的狀態
   誠實了，但沒有讓它被追。DR-DM7 若到齊，母體可望大幅收斂 ——
   在那之前，追或不追都缺一個判準。
2. **底線↔空格之錨（A-DM19）未裁示。** 這與縮寫錨是同一類問題
   （封閉、可稽核、逐字），若裁示開放，PROXI 側之 `related_leaf`
   會立刻從 0 變成非 0；若裁示不開放，PROXI 對照就永遠只有值域而無 leaf。
3. **`DISPLAY_ON` ↔ `DISP_ON` 無任何橋樑**（A-DM18 末段）。它不是縮寫、
   沒有並列出處，glossary 建不了條目，而它出現在 037 八條中的兩條。
4. **`_polarion` 之其餘 340 個欄位字典完全未用。** 本輪只查了 `Category`。
   `SW/HW/System`、`Priority`、`ASIL` 等欄是否也有大量違規值，未知 ——
   而我已經知道這份匯出檔的值不被校驗。
5. **`Polarion` 分頁之欄名→field id 對照未用。** 若日後要回寫 SYS2 或
   與 Polarion 交換，那張表就是鍵；本輪只記其存在。
6. **`recon.py` 仍未跑通**（A-DM8）。Q5 已由下放包 06 §三正式提交 Pei
   裁定並提案 B，**尚未裁**。本輪十四支腳本仍全為自寫；
   §2.1 之假衝突是本 feature **第四次**同型自我更正
   （04 §5.3 DBC 選錯、05 §2 分隔符、05 §6.1 查詢鍵、06 §2.1 擷取過寬），
   四次全靠事後自查。**沒有獨立管線交叉檢查這件事，本身就是最大的
   未驗項。**

另記本輪**已驗而下放包未要求**者：037 八條之併句缺陷（8/8）；
`DISPLAY_ON`／`DISP_ON` 之命名落差；`_polarion` 對 `Category` 之
校驗結果與 `Non Functional Requirement` 之 0 列；PROXI 三列之
`Used by` 皆含 `ETM`；`glossary_phrase` 在 `anchor_kind` 中永不出現
之設計後果。

---

## 11. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): glossary anchor, aggregation audit, 037 close-read

- R-DM22/23 + R-G16 and the R-G13 supplement verbatim (4/4, 25/25)
- glossary.tsv: 13 abbreviations, each with a same-sentence source quote;
  accepted only when the words' initials spell the abbreviation. A looser
  first pass produced six phantom conflicts and was corrected
- coverage: SWE-DM-007/008 go from 0 to 12 candidates each; the handoff's
  24 is over all 333 rows, 12 over the 80-row FR population
- glossary_phrase never surfaces in anchor_kind (heading is always
  present), so candidate_from records which anchor fired
- proxi related_leaf stays empty: LID/PROXI write Rear_View_Camera with
  underscores, and R-DM22(c) forbids relaxing further (A-DM19)
- R-DM23 semantics: coverage 64 rows are (3), proxi 446 are (2),
  signal_resolution 2 are (1) — separate columns, never one symbol
- R-G16 audit of 6 writers: comma joins replaced with U+00A6; all six row
  counts unchanged, so the reconstruction check passes
- 037 close-read (4 rounds overdue): 0 values, 0 signals, 0 external refs,
  8/8 run-on sentences (A-DM18)
- _polarion is the field value dictionary: 117 of 333 Category values are
  not in it, and the illegal spelling is the majority one (A-DM4 upgraded)
- A-DM20 and DR-DM7: Used by NODE(VFXXX) needs this project's VF code
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

本輪未改 `.gitignore`、未改 `forms/`（`FORMS.md`／`LOOKUP_MISSES.md`
本輪無變更）。四份參考素材仍不入 git。
