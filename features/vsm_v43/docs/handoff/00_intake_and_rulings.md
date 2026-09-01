# 下放包 00 — Vehicle Setup Management R1L TBM（VF665 V43）：進場、裁決落檔、P0/P1 指示

日期：2026-09-01
Feature slug：`vsm_v43`（R-VT1）　條號系列：`R-VT`　姊妹線：`vsm_v42`（獨立，本包不涉）
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 為空，取 00
觸發：同 `vsm_v42` 00 包；五題裁定「1 准 2 准 3 准 4 無其他 5 准」

**本線現況一句話：037 = 0，無 TC 母體（R-VT4）。本包只做 P0–P3 之前置；P4 以後待 DR-VT1。**

---

## 零、禁區（執行層不得為之）

1. **git 一律不動**。
2. 不得寫入 `features/vehicle_setting/`、`features/vsm_v42/` 之任何檔。
3. 不得寫入 `docs/runtime/profiles/`。
4. 不得對 `sources/raw/` 原檔改寫。
5. **不得以 SYSRA 或規格代 037 生成任何 TC 或 leaf 母體**（R-VT4）。
6. 不得自行送 DR。

## 一、背景（一段）

VF665 V43 為 Vehicle Setup Management by VP - LTM (R1L) with TBM 之版本，與 V42（R1 Low）分立為兩個 feature（Pei 裁）。素材：V43 規格 R4（docx）、V43 SYSRA（035，Polarion 匯出格式 `Basic Report`）、SYSAD（與 V42 共用）。**無 037**。訊號書寫依 canon §8.7.5 v3 與 PM 現行條文（R-VT2）。工作簿 BLANK 起建。

## 二、裁決引用（R-G13）

本線 `RULINGS.md` 於本包同時落檔，含 **R-VT1–R-VT5**。sha8 由執行層跑 `rulings_hash.py` 後回報。

| 條號 | 一句話 | sha8 |
|---|---|---|
| R-VT1 | 獨立 slug `vsm_v43`；BLANK 起建 | 待回報 |
| R-VT2 | 訊號依 IN §8.7.5 v3 ＋ R-P353／R-P355／R-P368；不承襲 R-VS52 | 待回報 |
| R-VT3 | Test Group `Vehicle Setup Management R1L TBM`；TC ID `NR1L-VSM43-{nnn}` | 待回報 |
| R-VT4 | 037 = 0，止於 P0–P3 | 待回報 |
| R-VT5 | 素材走 `sources/raw/<doc_id>/` | 待回報 |

全域：R-G1、R-G13／R-G14、R-G23、R-G24、R-G27、R-G28、R-G42。PM：R-P353、R-P355、R-P368。

## 三、素材清冊（intake 實測）

| # | doc_id（擬） | 檔名 | 型態 | 實測 | 用途 |
|---|---|---|---|---|---|
| 1 | `vf665_v43_spec_r4` | `Vehicle Setup Management by VP - LTM (R1L) with TBM [VF665_V43_R4].docx` | OOXML（**Project 內僅抽取本 2365 行；原檔待投遞**） | 待 sha | 母 spec（spec_mode D） |
| 2 | `vf665_v43_sysra` | `FMWIFSM035A02_VF665_V43_STLA_SYSRA…_VF665_V43_Release.xlsx` | xlsx（Polarion 匯出：`Basic Report`／`Polarion`／`_polarion`） | sha256 `4e8db108ad12d285…`；`Basic Report` 表頭列 1，資料 1280 列；Category：**Functional 507**／Information 492／Heading 182／`Out of scope` 55／`Out of Scope` 44；DocID `VF665_V43_R3` 951／**`VF655_V43_R3` 247**／空 82；EE ATL-Mi 1280；`Function (Level 1)` 全為 `A. 核心顯示管理` 506 ＋ 1 | 跨源驗核；**非母體** |
| 3 | `vf665_sysad_sys3` | SYSAD SYS3 v1.0 docx | OOXML | 與 `vsm_v42` 共引一份（R-VT5） | 架構參考 |

母體來源（037）：**無**。

## 四、Pei 之投遞動作

投遞區 `_intake/Vehicle_Setup_VF665/`（已建妥實測）—— 與 `vsm_v42` 同一投遞，#1、#2 原檔放此即可（`vsm_v42` 00 包 §四已列）。

## 五、執行層作業清單（P0 → P1，僅前置）

**W-1 scaffold**：`python3 scripts/new_feature.py vsm_v43 --adopt-existing`；`feature.yaml`：`feature: "Vehicle Setup Management R1L TBM"`、`tc_id_prefix: "NR1L-VSM43-"`（R-VT3）；`a03_report: null` 並註明 `DR-VT1`。

**W-2 sources 落檔**：同 `vsm_v42` W-2（R-G27）；#3 若 sha 與 `vsm_v42` 已落者相同則不重存，MANIFEST features 欄加 `vsm_v43`。R-G28 嵌入物件檢查對 #1。

**W-3 recon**：`recon.py` 於 `a03_report = null` 之行為未知 —— 先以 `--help` 或原始碼確認是否允許缺 037；不允許則**不改腳本**，改出人工 recon（`RECON.md` 手寫：workbook_state BLANK、素材 sha、SYSRA 計數），並登 anomaly 記「recon.py 不支援無 037 之 feature」。

**W-4 SYSRA 分層預查**（供 P3 framework 草案用，非母體）：自 #2 取 Functional 507 列之 `Chapter for VF`、`Melco ID`（標題）、`Document ID`，出 `data/sysra_v43_functional.tsv`；`VF655` 247 列與 DocID 空 82 列**分別標記、不入分母**（DR-VT2）。`Out of scope`／`Out of Scope` 二拼法合計 99，正規化後計數並登 anomaly（上游拼法不一）。

**W-5 R-VT2 訊號解析預查**：自 #1 docx 抽 CAN 訊號名／內部訊號／PROXI 參數，跑 R-P368 三段鏈，出 `data/signal_chain_v43.tsv`；段 1 對 `Atlantis High` 欄組與 `637MCA Specific Signals` 分頁分別計數，不自行選定。另出 V42 ↔ V43 訊號名集合之差（新增／刪除），供 framework 與 DR-VT1 之「差異列」請求用。

**W-6 anomaly／DR**：A-VT 系列自 1 起；DR-VT1／DR-VT2 已登記。

## 六、預期數字

| # | 項 | 預期 | 掃描條件 |
|---|---|---|---|
| E1 | `Basic Report` 資料列 | 1280 | 表頭列 1，任一欄非空 |
| E2 | Functional | 507 | `SYS2 分類 Category` 全等 |
| E3 | `Out of scope` ＋ `Out of Scope` | 55 ＋ 44 | 全等，分開計 |
| E4 | DocID `VF665_V43_R3`／`VF655_V43_R3`／空 | 951／247／82 | 全等 |
| E5 | Functional 中 DocID `VF655_V43_R3` | 171 | 同列 |
| E6 | EE ATL-Mi | 1280 | 全等 |
| E7 | 037 兩檔內 `V43` 字串命中 | 0 | 全欄串接 substring |
| E8 | V43 Functional 描述 ↔ V42 Functional 描述逐字相同（空白正規化、小寫） | 30／398 去重 | `re.sub(r'\s+',' ').strip().lower()` |
| E9 | `Verification Method` 之相異值 | 4（含 `verified by in-vehicle testing` 47、`internal signal stimulation test…` 28） | 正規化後 |

## 七、上繳要求（`docs/upstream/00_intake_recon.md`）

scaffold 輸出；sources 落檔與 sha；R-G28 結果；`RECON.md`（機器或人工，註明何者）；E1–E9 對照；
`data/sysra_v43_functional.tsv` 計數；`data/signal_chain_v43.tsv` 分布與 V42↔V43 訊號差集；
anomaly／DR 成對清單；R-VT sha8；獨立判斷；`gate_all.py` 輸出。

## 八、升級條件

docx magic bytes 非 OOXML；E2／E4 不符；`recon.py` 需改碼方能跑；R-P368 段 3 B-1 衝突；
任何試圖自 SYSRA 建 leaf 母體之需求（一律停）。

## 九、三層框架（僅 Layer 1 定，Layer 2 待 037）

Layer 1：`Vehicle Setup Management R1L TBM`（R-VT3）。
Layer 2 於 037 到齊後自 037 家族聚合（沿 `vsm_v42` 00 包 §九之做法）；W-4 之 SYSRA 分層僅作對照，不作 Layer 2 依據。

## 十、下一步

1. Pei 投遞原檔；決定 DR-VT1（建議送出）／DR-VT2 之送出
2. 執行層 W-1～W-6，上繳 00
3. 分析層落 profile `FW036_R1L_VSM_V43_Profile.md`（R-VT2 條文化），framework Layer 1 先鎖
4. 037 到齊 → 母體建檔 → Layer 2 裁 → P4

## 十一、未結 DR 清單（IN §8.4.3）

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 已登記，建議送出 |
| DR-VT2 | SYSRA DocID `VF655` 疑誤植；R3 vs R4 版次 | no | 已登記，未送出 |
