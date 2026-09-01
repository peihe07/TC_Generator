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

## A-VT6 — scaffold 之 `workbook.sheet` 模板值於 R-G1 母本不存在（RESOLVED，執行層）

- **實測**（2026-09-01，W-2）：`sandbox/base/` 副本之分頁為
  `['Cover_old','ChangeHistory_old','Cover 封面','ChangeHistory 修訂履歷',
  'Product Document 記錄封面頁','Test Case Specification 測試用例規範','Reference',
  'QS Suggestion','下拉選單']` —— **無** `Test Case Specification&Result`。
- **影響**：scaffold 模板值會於 `scripts/recon.py:431`／`survey_workbook` 直接 `sys.exit`。
- **處置**：`feature.yaml` 改為實測值 `Test Case Specification 測試用例規範`。
  同型於 A-VT4（模板值），屬 FO §0 Tier 0「照抄不是判斷」，逕改並記錄。
- **併同改正之模板欄位**（R-VT8(b)，自 r9 表頭逐欄實測）：
  `design_method` Q→**R**、`functional_safety` R→**S**、`author` Z→**AA**；
  新增 `tc_id` **F**、`estimated_test_time` **Q**、`test_version` **AB**。
  `priority` P、`remarks` AH 與 D–O 各欄**核實無誤**。

## A-VT7 — `scripts/extract_source.py` 不支援 `.docx`（PENDING）

- **實測**：`scripts/extract_source.py:137-142` 只認 `.xlsx`／`.pdf`，其餘
  `raise ValueError(...不支援之型別...)`；跑 `--doc-id vf665_v43_spec_r4` 與
  `--doc-id vf665_sysad_sys3` 皆輸出「跳過 …：不支援之型別 .docx」。
- **影響**：#1（母 spec，spec_mode D）與 #3（SYSAD）**無 `sources/extracted/`**。
  R-G27 之「raw 為權威、extracted 為衍生物」仍成立，故不阻塞：W-5 直讀 `raw/` 之
  docx（`zipfile` + `word/document.xml` 段落抽取，1781 段），量測條件已於 RECON §6 揭露。
- **處置**：**不改共用腳本**（同 A-VT3 之界線）。登記並交上游。
- **提請裁決**：`.docx` 之抽取是否納入 `extract_source.py`（spec_mode D 之 feature
  將持續遇到），或本線一律以直讀 raw 為之並於各包揭露量測條件。

## A-VT8 — `extract_source.py` §F-6 自驗對 SYSRA 誤報，抽取被中止（PENDING）

- **實測**：`python3 scripts/extract_source.py --doc-id vf665_v43_sysra` →
  `FAIL（§F-6 抽取失真）: … sheet 'Basic Report'：行數／非空儲存格
  原檔 (1282, 30816)，抽取物 (1282, 30817)` —— 行數相符，非空儲存格 **+1**。
- **根因（已定位，非推測）**：`Basic Report` **第 480 列第 16 欄（P 欄）** 之值為
  **恰好一個換行字元** `'\n'`。
  - 原檔側 `measure()`（`:67-70`）判 `str(v).strip() != ""` → `''` → **不計**。
  - 抽取物側 `cell_text()`（`:57-62`）將 `\n` 轉義為字面兩字元 `\` ＋ `n`，
    回讀時 `cell.strip()` 非空 → **計入**。
  - 故 +1 為**自驗兩側對「空白」定義不一致**所致，**不是抽取失真**。
    全庫掃該檔三分頁，此型儲存格**僅此一格**。
- **影響**：`sources/extracted/vf665_v43_sysra/` 未產出（腳本於寫入後 `unlink` 並中止）。
  W-4／RECON §4 之計數改自 `raw/` 直讀，結果不受影響。
- **處置**：**不改共用腳本**，不放寬自驗（FO §8.3 第一層之完整性優先）。登記並交上游。
- **提請裁決**：修法二擇一 —— (a) `cell_text()` 對「轉義後才非空」之情形回寫空字串；
  (b) 回讀側之計數改以反轉義後之值判空。**(b) 較穩**：它修的是比較基準，不動輸出內容。

## A-VT9 — SYSRA `Melco ID` 欄於 Functional 507 列全空（PENDING）

- **實測**：`Basic Report` C 欄 `SYS2 Melco ID`，Functional Requirement 507 列
  非空 **0 / 507**（全 1280 列亦同型，未見標題用值）。
- **問題**：00 包 §五 W-4 令 `data/sysra_v43_functional.tsv` 取
  `Chapter for VF`、**`Melco ID`（標題）**、`Document ID` 三欄。`Melco ID` 無值可取，
  該欄於本線不具標題功能。`Chapter for VF` 507/507 非空，可用。
- **處置**：TSV 仍保留 `melco_id` 欄（全空），不以他欄頂替、不留白於文件外。
- **提請裁決**：P3 之 leaf 標題來源改採 `Chapter for VF` ＋ `Description`，或另索 Melco ID。

## A-VT10 — E2 之判準字面與實值不符（`Functional` vs `Functional Requirement`）（PENDING）

- **實測**：00 包 §六 E2 之掃描條件為「`SYS2 分類 Category` 全等」、預期值「Functional 507」。
  該欄之實際值為 **`Functional Requirement`**，計 **507**；以 `Functional` 全等計 = **0**。
- **判定**：**計數相符（507），判準字面不符**。依 FO 之第 8.5 節第 2 條**不自行調和**，
  兩讀法並列回報，不擇一寫成「相符」。
- **影響**：E5 隨之 —— 以 `Functional` 全等計 0，以 `Functional Requirement` 計 **171**（＝預期）。
  00 包 §八「E2／E4 不符」之升級條件因此觸發，已依 FO §0「Filing 後續行不受影響之工作」處理。
- **旁證（支持「僅為簡稱」之讀法，但不由執行層據以判定）**：E1／E3／E4／E5／E6／E7／E8
  七項於 `Functional Requirement` 讀法下全部逐字相符，含 E5 之 171 與 E8 之 30／398。
- **提請裁決**：確認 E2／E5 之掃描條件應寫作 `Functional Requirement` 全等。

## A-VT11 — E9 `Verification Method` 相異值遠多於預期（PENDING）

- **實測**（正規化 `re.sub(r'\s+',' ').strip().lower()`）：
  - 全 1280 列：相異 **61**（含空白；空白 750 列）
  - Functional 507 列內：相異 **57**（含空白）／**56** 非空
- **預期**：**4**。**不符，差距一個數量級。**
- **對照**：預期所舉之兩個具名值中，`verified by in-vehicle testing` = **47** ✅ 逐字相符；
  `internal signal stimulation test…` 預期 28，實測**以該串開頭者共 30 列、相異 13 種**
  （尾段各異），無任一單一值為 28。
- **可能成因（不據以調和）**：預期值疑似取自某一子集合或某一截斷長度之計數，
  下放包未載其掃描範圍（全表 vs Functional）與是否截斷。
- **處置**：據實回報兩個範圍之數字，不擇一、不調和。
- **提請裁決**：補明 E9 之掃描範圍與正規化條件後重測。

## A-VT12 — 段 3 訊息名與規格訊息名不符之 B-1 型衝突 29 列（PENDING，E15 停）

- **實測**：`data/signal_chain_v43.tsv` 結果欄 `B-1 衝突` = **29**（E15 預期 0）。
  依 01 包 §七「E15 ≥ 1（停該部分）」，**W-5 之訊號實名指派就此停下**，列 §K 交 Pei。
- **型態一（22 列，主群）**：規格之 `*_SETUP2` 訊息，其訊號名於 forms DBC 落在**無 `2`** 之
  同名訊息下 ——
  - `IPC_VEHICLE_SETUP2.<X>` 9 列 → `FDCAN8:IPC_VEHICLE_SETUP`
  - `TELEMATIC_VEHICLE_SETUP2.<X>_Req` 9 列 → `FDCAN8:TELEMATIC_VEHICLE_SETUP`
  - `TELEMATIC_SERVICE_SETUP.<X>Req` 4 列 → `FDCAN8:TELEMATIC_VEHICLE_SETUP`
  **關鍵反證**：`IPC_VEHICLE_SETUP2` **確實存在**於 FDCAN8（34 個 `SG_`，皆為
  `AUX*_HLEnbl`／`AUX*_PWRMD`／`AUX*_TYPE` 型），**但不含**上列九個訊號名；
  而 `TELEMATIC_VEHICLE_SETUP2` 於兩本 DBC **完全不存在**（存在者為
  `TELEMATIC_VEHICLE_SETUP` 與 `TELEMATIC_VEHICLE_SETUP3`）。
  故此非「同名訊息之版本差異」可一語帶過者。
- **型態二（6 列）**：`SERVICE_SETUP.<X>` 5 列 → `FDCAN8:TBM_SCHEDULE_FD_2`／
  `IPC_VEHICLE_SETUP`；`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` → `IPC_VEHICLE_SETUP`。
- **型態三（1 列）**：`BRAKE1.VehicleSpeedVSOSig` → `BHCAN2:STATUS_CCAN3` ＋ `FDCAN8:BRAKE_FD_2`
  （**兩本 DBC 解至不同訊息**，R-VT6(c) 之「解至不同標的」字面型）。
- **量測條件與其 Tier 2 性質（R-G8／FO §0）**：R-VT6(c) 只定義「同一規格原名多處命中而
  解至不同標的者為 B-1」，**未定義「段 3 之 `SG_` 所屬 `BO_` 與規格訊息名不符」是否為 B-1**。
  本包將後者操作化為 B-1（型態一、二），此一技術選擇**改變了 E15 之結論**（0 → 29），
  依 FO §0 Tier 0 末句即為 **Tier 2**，故不逕行採認，全數列 §K 交裁。
  若僅採 R-VT6(c) 之字面（多處命中解至不同標的），B-1 = **1**（型態三），
  其餘 28 列改記「未解得（訊息名待確認）」。**兩種讀法並列，不擇一。**
- **提請裁決**：(a) B-1 之判準是否含「訊息名不符」；(b) `TELEMATIC_VEHICLE_SETUP2` 於
  forms DBC 全無 —— 是 DBC 版次落後於 R4 規格，或規格訊息名有誤？此題宜併 DR 上問。

## A-VT13 — `docs/fw036/RULINGS.sha.tsv` 仍無 R-VT 列，E10 之前提不成立（PENDING）

- **實測**：`grep -c "R-VT\|R-VL" docs/fw036/RULINGS.sha.tsv` → **0**。
  `features/vsm_v42/docs/upstream/01_sources_recon.md` 載該線**停於 W-0**，
  R-VL9 之台帳重生**未執行**。
- **影響**：R-VT8(a) 令本線 sha8「自重生後之台帳讀取」，01 包 §二同旨；
  **台帳無可讀之列**，E10 依其字面**不可判**。
- **處置**：**不代 vsm_v42 重生台帳**（R-VT8(a) 明令本線不重生）。
  改以 `rulings_hash.py --out <scratchpad>` 於樹外重生後讀取，**明示此為替代量測**，
  並與上繳 00 §七之值逐字比對（見上繳 01 §E10）。
- **提請裁決**：R-VT8(a) 之依賴鏈已阻塞兩包；是否改由本線或由 Pei 直接重生台帳。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning：`[ASSUMPTION A-VTnn]`。
