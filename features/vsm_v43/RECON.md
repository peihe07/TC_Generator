# RECON — vsm_v43（Vehicle Setup Management R1L TBM，VF665 V43）

> **本檔為人工 RECON，非 `scripts/recon.py` 之輸出。**
> 依 A-VT3：`recon.py` 於 `a03_report` 為 null 時於 `:582` TypeError（`survey_a03`
> 直接 `openpyxl.load_workbook(None)`），改碼權屬 Pei（01 包 §四），裁前不改腳本。
> 下列每一數字皆由本執行層自 `sources/raw/` 之原檔實測，量測條件逐項列明（R-G8）。
> 日期：2026-09-01　執行層　對應下放包：`docs/handoff/01_sources_recon.md` W-3

---

## 1. workbook_state

| 項 | 值 | 量測條件 |
|---|---|---|
| workbook_state | **BLANK** | `sandbox/base/` 副本，分頁 `Test Case Specification 測試用例規範`，第 10 列起、**B 欄除外**（B 為 `=IF(ISBLANK($D10),"",ROW()-9)` 序號公式）之非空儲存格列數 = **0**（掃 max_row 1411） |
| 母本身分 | `forms/…_SWQT_20260817_ext.xlsx`（R-G1） | `cmp` 與 forms/ 原件全等；sha256 `6372fb6b…825b2`（E11） |
| 表頭列 | 9 | 逐列讀取，第 9 列有 33 個非空表頭，佔 B–AH |
| openpyxl 存回 | **未曾為之** | 全程 `read_only=True`；母本 R 欄 x14 DV 之保全（R-G1 註／A-UP09） |

`workbook_state = BLANK` 亦與 R-VT1（「自 BLANK ＋ R-G1 模板起建」）一致。

## 2. 素材與 sha256（R-G27 落點）

| doc_id | 檔名 | sha256 | extracted/ |
|---|---|---|---|
| `vf665_v43_spec_r4` | `Vehicle_Setup_Management_by_VP_-_LTM_(R1L)_with_TBM_VF665_V43_R4.docx` | `c922b4763eec45ca0c294e354788591ededc5d4189387332061288de9b00edbe` | **無**（A-VT7：`.docx` 不支援） |
| `vf665_v43_sysra` | `FM-WI-FSM-035-A02_VF665_V43_STLA_SYSRA…_VF665_V43_Release.xlsx` | `4e8db108ad12d28508419571b56e0dab8475982ac74eee8018f857142e45fb49` | **無**（A-VT8：§F-6 自驗誤報中止） |
| `vf665_sysad_sys3` | `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_…_SYSAD_v1.0.docx` | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` | **無**（A-VT7） |
| `vf665_037_parksense` | `FM-WI-FSM-037-A03_SWE1_VF665_…_Park_Sense_And_Restore Default Setting __Features_Report.xlsx` | `be55d8978f9472f3b7bae8643eee139525f2c455b8bddce24f3911c4128e9d05` | 有（`Analysis Report` 152 列／1324 格、`Instructions` 20／39） |
| `vf665_037_sdw` | `FM-WI-FSM-037-A03_SWE1_VF665_…_Side_Distance_Warning - Audio_Repetition Features_Report.xlsx` | `c98909e2c15eb0a02e1ab99f25c4c7bd77226fbd5f29842088bbe06f9f0f2afd` | 有（`Analysis Report` 97 列／1166 格、`Instructions` 20／39） |

sha 於 `features/vsm_v43/inputs/` → `sources/raw/` 之搬移前後逐檔比對，**五件全等**。
`inputs/` 已清空（實測 0 項）。

**三方 sha 比對（01 包前提）**：
- 037 兩份 vs `features/vsm_v42/inputs/` 同名檔：**逐位元全等**（`be55d897…`／`c98909e2…`）→ 不另建 doc_id，取 vsm_v42 之 `vf665_037_parksense`／`vf665_037_sdw`。
- SYSAD vs `features/vsm_v42/inputs/` vs `features/vehicle_setting/inputs/`：**三方全等**（`469162b8…`）→ 取 `vf665_sysad_sys3`。本線先落（01 包「誰先跑誰落」）。

## 3. 母體（037）

```
a03_report = null   （DR-VT1）
```

V43 之 037 **不存在**（R-VT4）。`sources/raw/` 之兩份 037 為 **vsm_v42 之母體**，
其 `Source Requirement ID` 非空 82 ＋ 70 = **152**，`V42` 命中 152／152，`V43` 命中 **0**（E7）。
本線 leaf 母體 = **0**，不得以 SYSRA 或規格代之（R-VT4，禁區 §零-5）。

| 項 | 值 |
|---|---|
| 037 leaf 數 | **0**（無 037） |
| done region 覆蓋 | 不適用（BLANK） |
| regen targets | **0** |
| 無處覆蓋之 leaf | 不適用 |

## 4. SYSRA 計數（`Basic Report`，表頭列 1）

量測條件：`openpyxl` `read_only=True, data_only=True`；資料列 = 第 2 列起、任一欄非空者；
欄以表頭文字定位（`SYS2 分類 Category` = M、`SYS2 文件識別碼 Document ID` = I、
`SYS2 EE Architecture` = J、`SYS2 驗證方法 (Verification Method)` = BH、`Description` = D）。

| 項 | 實測 |
|---|---|
| 資料列（E1） | **1280** |
| Category（全等，E2／E3） | `Functional Requirement` **507**／`Information` 492／`Heading` 182／`Out of scope` **55**／`Out of Scope` **44** |
| Category 正規化後 `out of scope`（E14） | **99** |
| Document ID（全等，E4） | `VF665_V43_R3` **951**／`VF655_V43_R3` **247**／空 **82** |
| Functional 中 Document ID（E5） | `VF665_V43_R3` 295／`VF655_V43_R3` **171**／空 41 |
| EE Architecture（全等，E6） | `ATL-Mi` **1280**（單一值） |
| Function (Level 1) 於 Functional | `A. 核心顯示管理(Core Display Management)` **506** ＋ `2. 系統特定診斷(System-Specific Diagnostics)` **1** |
| Verification Method 相異值（正規化，E9） | 全 1280 列：**61**（含空白，空白 750）；Functional 507 列內：**57**（含空白）／**56** 非空 |
| `Melco ID`（C 欄）非空 | **0 / 507** —— 全 Functional 列該欄皆空（A-VT9） |

**分母之處置（DR-VT2）**：Functional 507 列中，`VF655_V43_R3` **171** 列與
Document ID 空 **41** 列**分別標記、不入分母**；分母 = **295**。
逐列標記見 `data/sysra_v43_functional.tsv` 之 `denominator`／`mark` 兩欄。

## 5. 跨源對照（E8）

V43 Functional 描述（`Description`，`re.sub(r'\s+',' ').strip().lower()`）507 條、去重 **398**；
V42 SYSRA（`features/vsm_v42/inputs/`，分頁 `Analysis Report`，表頭列 5，
Category 第 10 欄、Description 第 3 欄）Functional 318 條、去重 **308**。
**去重交集 = 30 / 398**（E8）。

> V42 SYSRA 之版面與 V43 **不同**：V43 為 Polarion `Basic Report` 匯出（分頁
> `Basic Report`／`Polarion`／`_polarion`），V42 為 035 表單版面（分頁 `封面`／`修訂履歷`／
> `Product Document 記錄封面頁`／`Analysis Report`／`Instructions`／`下拉選單設定處`）。
> 兩者不可以同一組欄位座標讀取；本檔之 V42 欄位為自其表頭實測所得。

## 6. spec 文字層

`spec_mode = D`（二進位文件抽取）。#1 docx magic bytes `50 4B 03 04`（E13，OOXML）。
`word/document.xml` 段落抽取得 **1781** 個非空段落。
zip members **25**，其中媒體／內嵌物件 **1** 件：`word/media/image1.wmf`。

## 7. 未決（2026-09-02 依下放包 04 補遺更新）

| 項 | 現況 | 依據 |
|---|---|---|
| **段 1 欄組綁定** | **已定**：本線 EE = ATL-Mi（1280/1280），段 1 取 LID `CAN Mapping` 之 **`Atlantis`（P–T）**欄組；`Atlantis High`（Z–AD）降旁證 | R-VT13(a) |
| **段 3 DBC** | **已到件、已綁定**：`forms/P363_BH-CAN [07338]_3A_R2.dbc`（latin-1／CRLF；實測 BO_ **99**、SG_ 定義 **688**／相異 **655**、VAL_ **503**、有 VAL_ 之訊號 **496**）。**「解得」自此合法**；R1 DBC 降旁證。**DR-VT5 結案** | R-VT15(a)(d)；A-VT28 |
| **K-1（LTM 匯流排）** | **結案並二度印證**：P363 之 `SG_ VehicleSpeedVSOSig` 落於 `BO_ STATUS_CCAN3`，無 `BRAKE1` → `STATUS_CCAN3.*` 為 LTM 觀察弧、`BRAKE1.*` 為上游弧 | R-VT13(c)；A-VT27 |
| **DR-VT3（原 28 列）** | **26 列轉解得，餘 2 列**（`SERVICE_SETUP.TelematicSetupACK`／`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock`，`SG_` 皆落 `IPC_VEHICLE_SETUP`）。DR-VT3 之實際名單為此 2 名；**暫持不送** | R-VT15(b)；E31 = 2 |
| **CAN-C DBC** | **未到件**：**8 列**記「未解得（CAN-C DBC 未到件）」 | R-VT15(c) |
| 內部訊號 | **83 名止於段 1，第五輪擴充零變動**（規則→欄→檔→欄組→**DBC**）。DBC 到件對其毫無作用 —— 缺的是對照表不是 DBC。唯一出路 **DR-VT4**（Pei 裁先不送） | A-VT25 |
| 內部訊號之 5 名「解得」 | **判準待裁**：係跳過段 1／2 之 DBC 直查（LID 不收 `X.Info` 形），R-P368(a) 三段鏈僅段 3 過 | A-VT26 |
| 結果值域 | `解得 \| 訊息名不符(R-13) \| 未解得（CAN-C DBC 未到件） \| 未解得(止於段1) \| 未解得(止於段2) \| B-1 衝突 \| UI路徑(R-P375b) \| PROXI路徑(R-P375b/c) \| UI+PROXI 雙路徑 \| 查無(R-G13)`；`段3待ATL-Mi DBC` 隨到件作廢 | R-VT14(a)／R-VT15(d) |
| HMI Settings 候選集 | `Technical Reference` 含 `VF665` **字面 3 列**／含 `665` **247 列**（`VF230/665` 佔 235）—— 兩讀法並列待裁 | R-VT14(b) |
| 第六規則（重音） | 已採，命中三名，備註記「重音正規化」 | R-VT13(e) |
| 抽名偽陽性 | A-VT21 六名（已標排除）＋ A-VT23 四名（標記，排除旗標待裁）＝ **10**；PROXI 母體應由 49 降為 39 | A-VT21／A-VT23 |
| 台帳重生 | 由 **Pei 提交前一次**（R-VL13(a) 已獲追認）；本線不重生 | R-VT14(c) |
| Layer 2 母體 | **待 037（DR-VT1，Pei 裁先不送）** —— 本線續止於 P0–P3 | R-VT4 |
| `spec_reference_template` | null，待 P3 | R-VT8(c) |
