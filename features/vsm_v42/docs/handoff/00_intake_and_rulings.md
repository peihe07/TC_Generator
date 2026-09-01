# 下放包 00 — Vehicle Setup Management R1 Low（VF665 V42）：進場、裁決落檔、P0/P1 指示

日期：2026-09-01
Feature slug：`vsm_v42`（R-VL1）　條號系列：`R-VL`　姊妹線：`vsm_v43`（獨立，本包不涉）
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 為空，取 00
觸發：Pei 於 Claude Project 下達「Vehicle_Settings_VF665接手，要把V42 V43線分開，然後訊號寫法要遵照power management最新的部分」；五題裁定「1 准 2 准 3 准 4 無其他 5 准」

---

## 零、禁區（執行層不得為之）

1. **git 一律不動**（add／commit／tag／stash／checkout）—— Pei 為唯一 git 操作者。
2. 不得寫入 `features/vehicle_setting/`、`features/vsm_v43/` 之任何檔（R-VL1：兩線與舊線不共用）。
3. 不得寫入或修改 `docs/runtime/profiles/`（profile 屬分析層，P3 方建）。
4. 不得對 `sources/raw/` 之原檔做任何改寫；`extracted/` 為衍生物，得重產。
5. 未經本包授權之裁決不得自立；遇 FO §0 六條停下條款即登記並停。
6. 不得自行送 DR（Pei 為 DR 送出者）。

## 一、背景（一段）

VF665 為 Vehicle Setup Management by VP - LTM 之 VF 規格，有 V42（R1 Low，P637MCA／ProMaster，ATL-Mi）與 V43（R1L with TBM）兩版。Pei 裁定兩版各立獨立 feature；本線為 V42。素材：V42 規格 R6（docx）、V42 SYSRA（035）、兩份 037（SWE1 分析報告）、SYSAD（SYS3，兩線共用）。訊號書寫不承襲 `vehicle_setting` 之 SWC 0708 式覆寫，改依 canon §8.7.5 v3 與 PM 現行條文（R-VL2）。工作簿 BLANK 起建。

## 二、裁決引用（R-G13 引用制）

本線 `RULINGS.md` 於本包同時落檔，含 **R-VL1–R-VL5**（全文在該檔，執行層讀原文）。
sha8 於執行層跑 `python3 scripts/rulings_hash.py`（路徑指向 `features/vsm_v42/RULINGS.md`）後回填本表並於上繳回報：

| 條號 | 一句話 | sha8 |
|---|---|---|
| R-VL1 | 獨立 slug `vsm_v42`；BLANK 起建 | 待回報 |
| R-VL2 | 訊號依 IN §8.7.5 v3 ＋ R-P353／R-P355／R-P368；不承襲 R-VS52 | 待回報 |
| R-VL3 | Test Group `Vehicle Setup Management R1 Low`；TC ID `NR1L-VSM42-{nnn}` | 待回報 |
| R-VL4 | 母體 = 037 Functional leaf（實測 128）；SYSRA 其餘 190 列不入範圍 | 待回報 |
| R-VL5 | 素材走 `sources/raw/<doc_id>/`；投遞區 `_intake/Vehicle_Setup_VF665/` | 待回報 |

引用之全域條文：R-G1（BLANK 模板）、R-G13／R-G14（引用制、LOOKUP_MISSES）、R-G23（取號）、
R-G24（路徑實在性）、R-G27（sources/）、R-G28（CFTS 嵌入物件檢查 —— 本線母件為 VF 非 CFTS，
檢查對象改為 VF665 docx 之嵌入物件，查無亦須記明）、R-G42（交付規格表）。
引用之 PM 條文（`features/power/RULINGS.md`）：R-P353、R-P355、R-P368；canon：IN §8.7.5 v3。

## 三、素材清冊（intake 實測，Claude Project 附件；原檔由 Pei 投遞）

| # | doc_id（擬） | 檔名 | 型態 | 實測 | 用途 |
|---|---|---|---|---|---|
| 1 | `vf665_v42_spec_r6` | `Vehicle Setup Management by VP - LTM (R1 Low) [VF665_V42_R6].docx` | OOXML（**Project 內僅文字抽取本 2824 行；原檔待投遞**） | 待 sha | 母 spec（spec_mode D） |
| 2 | `vf665_v42_sysra` | `FMWIFSM035A02_VF665_V42_STLA 技術安全需求分析報告_SYSRA…_VF665_V42_Released.xlsx` | xlsx | sha256 `72411efdd597482b…`；`Analysis Report` 表頭列 5，資料 1040 列；Category：Information 557／**Functional 318**／Heading 109／Out of Scope 56；DocID `VF665_V42_P637MCA` 791、空 249；EE ATL-Mi 791、空 249 | 跨源驗核（A-VS134 型）；非母體 |
| 3 | `vf665_037_parksense` | `FMWIFSM037A03_SWE1_VF665_STLA 報告_SWRA_STLA_Park_Sense_And_Restore_Default_Setting__Features_Report.xlsx` | xlsx | sha256 `be55d8978f9472f3…`；表頭列 7；有 SWE id 82 列 = Heading 13 ＋ Functional 68 ＋ 空 1；Source ID 全為 `Sys-RA-VF665_V42_VSM-nnn` | **母體來源** |
| 4 | `vf665_037_sdw` | `FMWIFSM037A03_SWE1_VF665_STLA 報告_SWRA_STLA_Side_Distance_Warning__Audio_Repetition_Features_Report.xlsx` | xlsx | sha256 `c98909e2c15eb0a0…`；表頭列 8；70 列 = Heading 10 ＋ Functional 60；Source ID 全 V42 | **母體來源** |
| 5 | `vf665_sysad_sys3` | `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | OOXML（原檔待投遞）| `features/vehicle_setting/inputs/` 已有同名檔，sha256 待比對；相同則 `sources/raw/` 一份、兩線共引 | 架構參考 |

Project 內 sha 為附件抽取本之 sha，**非原檔 sha**；原檔 sha 於 intake 實測後為準（G-L）。

**037 兩份合計**：Functional **128**（Source ID 去重 128，兩檔無交集）；Heading 23；`Categorization` 空 1 列
（Park Sense 檔 `Intelligent Speed Limiter with Confirmation` 家族，待查是否漏標 → 候選 anomaly）。
`Verification Method` 三種值（含 `\xa0` 前導之變體），recon 正規化時記錄。

## 四、Pei 之投遞動作（路徑已建妥並實測，R-G24）

投遞區：`_intake/Vehicle_Setup_VF665/`（2026-09-01 `create_directory` 後 `list_directory` 實測存在，0 files）。
請放入上表 #1、#2、#3、#4、#5 之**原檔**（#1、#5 須為 OOXML `.docx`，非抽取本）。
V43 之三件（規格 R4、SYSRA V43）同放此區，由 `vsm_v43` 之 00 包取用；投遞區兩線共用，落點分開。

## 五、執行層作業清單（P0 → P1）

**W-1 scaffold**
`python3 scripts/new_feature.py vsm_v42 --adopt-existing`
—— `features/vsm_v42/` 已存在（本包與 `RULINGS.md`／`DATA_REQUESTS.md` 先落），`--adopt-existing` 只補缺不覆寫；上繳列出 `kept existing` 清單，須含 `RULINGS.md`、`DATA_REQUESTS.md`。
`feature.yaml`：`feature: "Vehicle Setup Management R1 Low"`、`test_group` 同值（R-VL3）；`tc_id_prefix: "NR1L-VSM42-"`（R-VL3；若模板無此鍵則新增並註明依據）；paths 改以 doc_id 引用（R-G27）。

**W-2 sources 落檔**（Pei 投遞後）
依 R-G27：`sources/raw/<doc_id>/` 放原檔、`sources/extracted/<doc_id>/` 放抽取形、`sources/MANIFEST.tsv` 逐檔加列（doc_id／檔名／sha256／版本／features=`vsm_v42`；#5 若與 `vehicle_setting/inputs/` 同 sha 則 features 欄記 `vsm_v42,vsm_v43`，note 記「與 vehicle_setting/inputs/ 同 sha」）。
docx 之型態依 magic bytes 判讀（R-P3′）：`50 4B 03 04` → zipfile 讀 `word/document.xml`；非此者停下回報。
R-G28：檢查 VF665 V42 docx 是否含嵌入物件（`word/embeddings/`、`word/media/`）；有者清點並出「由圖找列」表，無者記「已查、無」。

**W-3 recon**
`python3 scripts/recon.py`（依 `feature.yaml`）。本線 037 為兩檔，`a03_report` 鍵須 glob 恰 1 檔（`feature_config.resolve_path` 之限制，見 `vehicle_setting/feature.yaml` 註）—— 兩檔以具名鍵 `a03_report_parksense`／`a03_report_sdw` 各掛一檔，leaf 全集另建 `data/leaves.tsv`（W-4）。recon 之代表檔取 #3。

**W-4 leaf 母體建檔**
`data/leaves.tsv`：自兩份 037 逐列取 `SWE-Requirement ID`／`Source Requirement ID`／`Requirement Title`／`Categorization`／`Sub Categorization`／`Verification Method`／`來源檔`。Functional 為 leaf；Heading 標 `No TC — Heading`；`Categorization` 空之列另標 `UNCATEGORIZED` 並登 anomaly。
跨源對帳：每一 `Source Requirement ID` 須於 #2 SYSRA `Sys-RA-Feature-ID` 欄命中，命中數上繳；未命中者逐列列出。

**W-5 R-VL2 之訊號解析預查（不生成 TC）**
自 #1 docx 之 Functional Diagram／External Interfaces 節抽全部 CAN 訊號名（`IPC_VEHICLE_SETUP*`／`TELEMATIC_VEHICLE_SETUP*` 等）、內部訊號（`*.Req`／`*.Info`／`*.GUI`）、PROXI 參數名，各去重計數；對 CAN 訊號跑 R-P368 三段鏈，出 `data/signal_chain_v42.tsv`（`規格原名 | 段1 LID 列與欄 | 段2 MESSAGE.Signal | 段3 DBC 檔 | 結果`，結果 ∈ {解得, 未解得(止於段1), 未解得(止於段2), 查無, B-1 衝突}）。
**段 1 之欄組**：同時對 `Atlantis High` 欄組與 `637MCA Specific Signals` 分頁查，兩者命中分開計數，**不自行選定**，交分析層裁（R-VL2 末段之待查項）。

**W-6 anomaly／DR 登記**
候選 anomaly：037 `Categorization` 空 1 列；SYSRA Functional 中 EE Architecture 空 112 列；SYSRA DocID 空 249 列。逐項實測後登 `ANOMALIES.md`（A-VL 系列自 1 起）。
DR-VL1 已登記於 `DATA_REQUESTS.md`，其「190 列」於 W-4 對帳後回填實數（318 − 命中數）。

## 六、預期數字（上繳逐項對照，相符者亦列）

| # | 項 | 預期 | 掃描條件 |
|---|---|---|---|
| E1 | #3 有 SWE id 列數 | 82 | `Analysis Report`，表頭列 7，`SWE-Requirement ID` 非空 |
| E2 | #4 有 SWE id 列數 | 70 | 同上，表頭列 8 |
| E3 | Functional leaf 合計 | 128 | `Categorization == 'Functional Requirement'`，strip 後全等 |
| E4 | Heading 合計 | 23 | 同法 |
| E5 | `Categorization` 空列 | 1 | 有 SWE id 而 Categorization 為 None |
| E6 | Functional Source ID 去重 | 128 | 兩檔聯集 |
| E7 | SYSRA `Analysis Report` 資料列 | 1040 | 表頭列 5，任一欄非空 |
| E8 | SYSRA Functional | 318 | `分類 Category` 欄，全等 |
| E9 | SYSRA Functional 之 EE 空 | 112 | 同列 EE 欄為 None |
| E10 | SYSRA DocID `VF665_V42_P637MCA` | 791 | 全等 |
| E11 | 037 描述內 CAN 訊號名（`[A-Z_]+_VEHICLE_SETUP\d*\.\w+`）| 71 ＋ 70 | regex，`Requirement Description` 欄，不去重 |
| E12 | 037 描述內 `PROXI`（不分大小寫）| 48 ＋ 23 | 同欄 |
| E13 | 037 描述內 `$token$` | 14 ＋ 16 | `\$[A-Za-z_]+\$` |
| E14 | LID v1_78 `CAN Mapping` 含 `IPC_VEHICLE_SETUP`／`TELEMATIC_VEHICLE_SETUP`／`RainSensor` 之列 | 65 | 全列串接後 substring |
| E15 | LID `637MCA Specific Signals` 非空列 | 22 | 任一欄非空 |
| E16 | 037 之 E3 ↔ E8 命中 | 128（預期全命中）| Source ID ∈ SYSRA `Sys-RA-Feature-ID` |

不符者**回報不調和**（FO §8.2）。

## 七、上繳要求（`docs/upstream/00_intake_recon.md`）

1. W-1 之 scaffold 輸出全文（含 `kept existing`）
2. sources/ 三處落檔清單 ＋ 原檔 sha256（G-L）；#5 與 `vehicle_setting/inputs/` 同名檔之 sha 比對結果
3. R-G28 嵌入物件檢查結果
4. `RECON.md` ＋ 預填 `DECISIONS.md`（未簽）
5. §六 E1–E16 逐項對照表
6. `data/leaves.tsv` 列數與分類計數；W-4 跨源對帳之命中／未命中
7. `data/signal_chain_v42.tsv` 之結果分布（五類各幾筆），**兩欄組分開**
8. 新開 anomaly（A-VL）與 DR 成對清單；未結 DR 清單（現 DR-VL1）
9. 五條 R-VL 之 sha8
10. 獨立判斷：本包是否仍有該驗而未驗者
11. `python3 scripts/gate_all.py` 輸出（exit code）

## 八、升級條件（停下回 chat）

- docx magic bytes 非 `50 4B 03 04`
- E3／E6／E8 任一不符
- W-4 跨源對帳未命中 > 0
- R-P368 段 3 出現 B-1 衝突（forms 二本查無而 R4／R5 查得）
- `new_feature.py` 拒絕（whitespace／既存衝突）
- Pei 未投遞而執行層欲以 Project 抽取本代原檔 —— **不得代用**，停下

## 九、三層框架草案（Layer 2 待 Pei 裁，未鎖；framework.md 於裁後落檔）

Layer 1：`Vehicle Setup Management R1 Low`（R-VL3）。
Layer 2 草案自 037 之 24 個 Requirement Title 家族聚合（括號為 Functional leaf 數）：

| Layer 2（草案） | 037 家族（Layer 3 於 framework 對映至規格章節） |
|---|---|
| Park Sense | PARK SENSE w/o HC.1 and HC.2 (5)、Rear Park Sense Volume (6)、Front Park Sense Volume (7) |
| Camera Gridlines | Dynamic Gridlines (4)、Surround Camera Gridlines (6) |
| Lighting | Auto High Beam (5)、Headlight Sensitivity (6) |
| Speed Assist | Traffic Sign Recognition (5)、Traffic Sign Assist Warning (6)、Intelligent Speed Limiter with Confirmation (4＋1 未分類)、New Speed Zone (6) |
| Driver Warning | Side Distance Warning (10)、Audio Repetition (3) |
| Wiper and Sensor | Rain Sensor (5) |
| Units | Units (1)、Distance (5)、Fuel Consumption (9) |
| EPB Maintenance Mode | EPB Maintenance Mode (17) |
| Personal Data and Defaults | Personal Profile Management (3)、Clear Personal Data (3)、Restore Default Setting (3)、Geolocation (5) |
| Time and Navigation | GPS Automatic Time Adjustment (2)、Nav Turn by Turn (2) |

合計 128（含 1 未分類列）。`Wiper and Sensor`（5）與 `Time and Navigation`（4）偏小，鎖定時得併入鄰組；`EPB Maintenance Mode`（17）單家族成組，符合 §4.1.3「同 Test Set 蘊含共用 setup」。

## 十、下一步

1. Pei 投遞原檔至 `_intake/Vehicle_Setup_VF665/`（§四）
2. 執行層 W-1～W-6，上繳 00
3. Pei 裁 Layer 2；分析層落 `framework.md`、建 profile `FW036_R1L_VSM_V42_Profile.md`（R-VL2 落條文）
4. DECISIONS 簽核 → P4 資料建置 → P5 pilot（預設取 `EPB Maintenance Mode` 或 `Park Sense`，framework 鎖定後併裁）

## 十一、未結 DR 清單（IN §8.4.3）

| DR | 項目 | 阻塞 | 狀態 | 送出日 |
|---|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中約 190 列無 037 覆蓋（覆蓋揭露） | no | 已登記，未送出 | |
