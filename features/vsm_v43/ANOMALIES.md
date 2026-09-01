# ANOMALIES — FW036 vsm_v43（Vehicle Setup Management R1L TBM）

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format：`[A-VTnn]`（本線序列自 1 起，00 包 §五 W-6）。
PENDING entries block their batch until a Pei ruling lands；RESOLVED entries
record the ruling verbatim。Registration is Tier 1（record + propose）；
disposition is Tier 2。

> scaffold 模板將 marker 寫為 `[A-VSnn]`（vehicle_setting 之序列），
> 與本線 `R-VT`／`A-VT` 不符，已於本包改正 —— 見 A-VT4。

---

## A-VT1 — 投遞區 `_intake/Vehicle_Setup_VF665/` 為空；三件原檔全未投遞（PENDING）

- **實測**（2026-09-01，執行層）：`ls -la _intake/Vehicle_Setup_VF665/` →
  `total 0`，僅 `.`／`..` 兩項，無任何檔案。
  全庫 `find . -iname "*V43*"` 僅命中 `features/vsm_v43/`（本包 scaffold）與
  `features/vehicle_setting/docs/handoff/V43_writeback_unfreeze.md`（他線文件，非素材）。
  `sources/raw/` 現有三目錄 `core_hmi_lf_pdf`／`core_hmi_lf_sys1`／`popup_037_v0_2`，
  無 V43 之任何 doc_id。
- **缺件清單**（00 包 §三）：
  | # | doc_id（擬） | 檔名 | 狀態 |
  |---|---|---|---|
  | 1 | `vf665_v43_spec_r4` | `Vehicle Setup Management by VP - LTM (R1L) with TBM [VF665_V43_R4].docx` | **未投遞** |
  | 2 | `vf665_v43_sysra` | `FMWIFSM035A02_VF665_V43_STLA_SYSRA…_VF665_V43_Release.xlsx` | **未投遞** |
  | 3 | `vf665_sysad_sys3` | SYSAD SYS3 v1.0 docx（與 `vsm_v42` 共引） | **未投遞**（`sources/raw/` 亦無 `vsm_v42` 之落檔） |
- **影響**：W-2（sources 落檔／sha／R-G28）、W-3（recon）、W-4（SYSRA 分層預查）、
  W-5（訊號鏈預查）全部不可執行。00 包 §六 E1–E9 之九項預期數字**本包一項亦無法實測**。
- **處置**：依本包指示**停於 W-1**，僅完成 scaffold 與 `feature.yaml`，回報缺件。
  不以 Project 內之文字抽取本代原檔（R-VT5 明令 spec_mode D 之抽取須自原檔）。
  不以 SYSRA 或規格建 leaf 母體或生成 TC（R-VT4，本包禁區 §零-5）。
- **對應 FO §0 停下條款**：第 1 條「Spec lookup unresolved（missing file）」。
- **請求動作**：Pei 投遞 #1–#3 原檔至 `_intake/Vehicle_Setup_VF665/`。
  到齊後 W-2～W-6 可一次跑完。

## A-VT2 — `tc_id_prefix` 鍵名無腳本讀取；repo 慣例為 `tc_id_format`（PENDING）

- **實測**：`grep -rn "tc_id_prefix\|tc_id_format" scripts/*.py` →
  唯一命中 `scripts/recon.py:1103-1104`，讀 **`cfg["write_back"]["tc_id_format"]`**；
  `tc_id_prefix` 於 `scripts/` 全庫 0 命中。
  既有先例 `features/power/feature.yaml` 用**頂層 `tc_id_format`**，
  值為完整格式字串 `"NR1L-PowerManagement-{NNN}"`（非前綴）。
- **問題**：00 包 §五 W-1 明令 `tc_id_prefix: "NR1L-VSM43-"`。該鍵名與該形制
  （前綴 vs 完整格式）皆與 repo 兩處慣例不同，落檔後無任何工具會消費它。
- **處置**：**不自行改鍵名**（Tier 2 判斷，非機械套用）。依 00 包原文落
  `tc_id_prefix: "NR1L-VSM43-"`，並於 `feature.yaml` 就地註明本條。
  R-VT3 之條文本身（`NR1L-VSM43-{nnn}`）不受影響 —— 爭點僅在 yaml 鍵名／形制。
- **提請裁決**：是否於 P3 改為 `write_back.tc_id_format: "NR1L-VSM43-{NNN}"`
  （recon.py 可讀者）或頂層 `tc_id_format`（power 形制），或兩者併存。

## A-VT3 — `scripts/recon.py` 不支援 `a03_report: null`（亦不支援 `workbook: null`）（PENDING）

- **實測**（原始碼判讀，未跑 —— 本線無工作簿亦無 037，跑不起來）：
  - `scripts/recon.py:1150-1163`：`p = resolve_glob(...) if pat else None`，
    路徑為 null 時 `paths[key] = None`，**不 guard**。
  - `scripts/recon.py:1164` `survey_workbook(cfg, paths["workbook"])` →
    `:430 openpyxl.load_workbook(wb_path)`，`wb_path=None` 即 TypeError。
  - `scripts/recon.py:1165` `survey_a03(paths["a03_report"], …)` →
    `:582 openpyxl.load_workbook(a03_path, read_only=True)`，同上。
  - 兩函式皆無 `if path is None` 分支；`--help` 亦無「缺 037」相關旗標。
- **結論**：`recon.py` **需改碼方能於 037 = 0 之 feature 上執行**。
- **處置**：依 00 包 §五 W-3，**不改腳本**；改出人工 `RECON.md`。
  惟人工 `RECON.md` 之三項內容（workbook_state BLANK、素材 sha、SYSRA 計數）
  其中**素材 sha 與 SYSRA 計數皆待 A-VT1 之原檔**，故本包**亦未產出人工 RECON.md**，
  僅登記本條。原檔到齊後補。
- **觸發**：00 包 §八 升級條件第 3 條「`recon.py` 需改碼方能跑」→ 已停並回報。
- **提請裁決**：(a) 是否核可改 `recon.py`（加 null guard，走「無 037」路徑）；
  或 (b) 本線一律走人工 `RECON.md`，不動共用腳本。

## A-VT4 — scaffold 之 ANOMALIES 模板序列標記錯置（RESOLVED，執行層）

- **實測**：`scripts/new_feature.py --adopt-existing` 產出之 `ANOMALIES.md`
  檔頭寫 `Marker format: [A-VSnn]`、末段 `[ASSUMPTION A-VSnn]`。
  `A-VS` 為 `vehicle_setting` 之序列（模板硬寫，非本 feature 之值）。
- **處置**：本包改為 `[A-VTnn]`。屬 FO §0 Tier 0「工作簿欄位字串與 framework 表之
  逐字一致／照抄不是判斷」之同型，逕改並記錄。
- **附帶**：同一 scaffold 產出之 `feature.yaml` 亦帶模板值
  （`spec_mode: "A"`、`done_region.author_value: "Arif"`、欄位映射 D…AH），
  已於 W-1 就地改正或標為未實測，見 `feature.yaml` 內註。
  欄位映射**未改**（無工作簿可測），僅標註 power A-PW37 之錯位先例。

## A-VT5 —— 分析層之誤（三項，00 下放包與 R-VT2）（RESOLVED）

- **登記日**：2026-09-01（分析層於覆核上繳 00 時自報）；**分析層之誤**。
- **(a)** 00 包 W-1 指定 `tc_id_prefix`，全庫慣例為 `tc_id_format`（A-VT2 之根因）。一次 grep 可驗而未驗。→ R-VT7。
- **(b)** R-VT2(b) 引 R-P368 而未讀至其下方加註 R-P375，窄讀 Pei「PM 最新」之指示。
  **引用前須讀到該條之最後一個加註**。→ R-VT6。
- **(c)** 00 包 §三 #3 SYSAD 記「與 vsm_v42 共引一份」而未記目標路徑當時不存在（上繳 00 §九-1）。
  以後共引項一律記「目標路徑 ＋ 已落／未落」。
- **處置**：R-VT6／R-VT7／R-VT8 已落；00 包原文不改，以 01 包取代。A-VT2 轉 RESOLVED（R-VT7）。
  A-VT3（recon.py 改碼）屬共用腳本，交 Pei。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning：`[ASSUMPTION A-VTnn]`。
