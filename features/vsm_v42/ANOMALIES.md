# ANOMALIES — FW036 vsm_v42（Vehicle Setup Management R1 Low）

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format：`[A-VLnn]`（下放包 00 §五 W-6：A-VL 系列自 1 起）。
PENDING entries block their batch until a Pei ruling lands；
RESOLVED entries record the ruling verbatim.
Registration is Tier 1（record + propose）；disposition is Tier 2。

---

## A-VL1 —— `_intake/Vehicle_Setup_VF665/` 為空，五件原檔全缺（PENDING）

- **登記日**：2026-09-01（下放包 00 之 W-1 執行時）
- **依據**：FO §0 Escalation trigger 1（missing file）；
  下放包 00 §八末條「Pei 未投遞而執行層欲以 Project 抽取本代原檔 —— 不得代用，停下」
- **實測**（掃描條件：`ls -la _intake/Vehicle_Setup_VF665/` 與
  `find _intake -type f`，2026-09-01）：
  投遞區存在（`drwxr-xr-x`，R-G24 路徑實在），**內含 0 files**。
  同層其他投遞區（`_intake/SW_Update/`、`_intake/Display/` 等）皆有檔，
  故非 `find` 之掃描面問題。
- **缺件清單**（下放包 00 §三 #1–#5，全缺）：

  | # | doc_id（擬） | 檔名 | 型態要求 |
  |---|---|---|---|
  | 1 | `vf665_v42_spec_r6` | `Vehicle Setup Management by VP - LTM (R1 Low) [VF665_V42_R6].docx` | OOXML 原檔（非抽取本，R-VL5） |
  | 2 | `vf665_v42_sysra` | `FMWIFSM035A02_VF665_V42_…SYSRA…_VF665_V42_Released.xlsx` | xlsx 原檔 |
  | 3 | `vf665_037_parksense` | `FMWIFSM037A03_SWE1_VF665_…Park_Sense_And_Restore_Default_Setting__Features_Report.xlsx` | xlsx 原檔 |
  | 4 | `vf665_037_sdw` | `FMWIFSM037A03_SWE1_VF665_…Side_Distance_Warning__Audio_Repetition_Features_Report.xlsx` | xlsx 原檔 |
  | 5 | `vf665_sysad_sys3` | `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | OOXML 原檔 |

- **阻塞**：**是**。W-2（sources 落檔）、W-3（recon）、W-4（leaf 母體）、
  W-5（訊號解析預查之段 1 來源為 #1 之 docx）、W-6（三項候選 anomaly 之實測）
  全數不可執行；§六 之 E1–E13、E16 不可實測。
- **不代用之聲明**：Claude Project 內之文字抽取本與 SYSRA 附件抽取本
  **未被取用**，`sources/raw/` 未建立任何檔（R-VL5、下放包 00 §八末條）。
  `features/vehicle_setting/inputs/` 內之同名 SYSAD（#5）**亦未取用為代品**
  —— 其得作為 sha 比對之對照方，不得作為本線之原檔（R-G27「新 feature
  一律走 sources/」）。
- **本地處置**：停於 W-1。W-1 之可為部分（scaffold ＋ `feature.yaml`）已完成，
  不涉原檔。
- **未開 DR 之理由**：本項非上游資料疑義，而係下放包 §四 所載之 Pei 投遞動作
  尚未發生（內部流程步驟），無可向上游詢問之項；且 DR 送出權屬 Pei
  （禁區第 6 條）。故只登 anomaly，不成對開 DR，理由記於此。
- **解除條件**：#1–#5 原檔落入 `_intake/Vehicle_Setup_VF665/` 後重跑 W-2～W-6。

---

## A-VL2 —— 分析層之誤（三項，00 下放包與 R-VL2）（RESOLVED）

- **登記日**：2026-09-01（分析層於覆核上繳 00 時自報）
- **歸屬**：**分析層之誤**，非執行層。
- **(a) 鍵名自創**：00 包 W-1 指定 `tc_id_prefix`，而全庫 17 個 feature.yaml 一律用
  `tc_id_format`、`recon.py:1103` 亦只讀後者。一次 grep 可驗而未驗（G-H 型：答案在鄰近
  feature 之現況裡）。→ R-VL7。
- **(b) 引用未讀到底**：R-VL2(b) 引 R-P368 而未讀至 R-P375（其加註就在 R-P368 條文下方），
  致 Pei「PM 最新」之指示被窄讀，並衍生一個實則不存在之「欄組二擇一」待查項。
  與 R-G40 一案（未查台帳即斷言無條文）同族：**引用前須讀到該條之最後一個加註**。→ R-VL6。
- **(c) 共引項只記關係不記現況**：00 包 §三 #5 SYSAD 記「與 vsm_v43 共引一份」，未記其目標路徑
  `sources/raw/vf665_sysad_sys3/` 當時**不存在**，vsm_v43 上繳 §九-1 指出其會多耗一輪。
  以後共引項一律記「目標路徑 ＋ 已落／未落」。
- **附註**：上繳 00 §8「A-VL2 起之號保留給該三項」**不承認** —— R-G23 為落檔當下 live 取號，
  預配號正是撞號之源（R-BLM4 一案）。該三項候選 anomaly 於實測後自當時末號取。
- **處置**：R-VL6／R-VL7 已落；00 包原文不改（下放包為歷史文件），以 01 包取代。

---

## A-VL3 —— W-0 之前提不成立：`RULINGS.sha.tsv` 仍為 `M`，且重生 diff 非 14 列（PENDING）

- **登記日**：2026-09-01（下放包 01 之 W-0 執行時）
- **依據**：下放包 01 §三 W-0「先 `git status --short docs/fw036/RULINGS.sha.tsv`
  確認為乾淨（Pei 已入庫）；若仍 `M`，停下回報，**不覆寫**」；
  §六 升級條件第 1 條；R-VL9 之前提「Pei 先將現行 working tree 入庫」。
- **實測 A（前提不成立）**：`git status --short docs/fw036/RULINGS.sha.tsv`
  → ` M docs/fw036/RULINGS.sha.tsv`（**非乾淨**）。
  `git diff --numstat` → `355  339`（+355／−339 行）。
  working 版相對 HEAD 多出 **16 個條號**：`R-G29`、`R-G42`、
  `R-ICS45`–`R-ICS58`（14 條）—— 皆為**他線**（canon §9.2 與 ics_management）之
  未入庫變更。working 版含 `R-V[LT]` 列數 **0**。
- **實測 B（E17 已知不可達）**：以 `--out <scratchpad>` 模擬重生（**未寫入該檔**），
  對現行 working 版逐行 diff → **17 新增列、0 修改、0 刪除**：
  `R-VL1`–`R-VL9`（9）＋ `R-VT1`–**`R-VT8`**（**8**）。
  預期 E17 為 14（9 ＋ 5）—— 差在 `vsm_v43` 之 `RULINGS.md` 已自 R-VT5 增至
  **R-VT8**（實測 `grep -n "^### R-VT" features/vsm_v43/RULINGS.md` 得 8 個錨點）。
  下放包 01 §三之「R-VT1–R-VT5（5）」係依上繳 00 §11 丁當時之實測所寫，
  期間姊妹線續有落檔，該預期數已陳舊。**不自行調和為 17**。
- **實測 C（E18 一項不同，但條文本體未動）**：R-VL2 之節 sha8 由上繳 00 §9 所報之
  `d6a189ed` 變為 `582d0c6d`；然其 `body_sha8` 為 `01c67a04`，**與上繳 00 §9 所報相同**。
  差異源於 R-VL6(d)「R-VL2 原文不改，加註指向本條」—— 加註落在**節內、fenced block 外**，
  而 `rulings_hash.py` 之 `sha8` 涵蓋整節（含加註），`body_sha8` 只涵蓋 fenced 本體
  （量測條件見該工具 docstring）。R-VL1／R-VL3／R-VL4／R-VL5 之 sha8 逐字相同。
  即：**條文未變，節變了**；E18 之量測面（`sha8`）與其所欲防之事（條文遭改）不同軸。
- **阻塞**：**是**。W-0 為本包首步且順序不得調換，故 W-1′～W-6 全數未執行。
- **本地處置**：未寫入 `docs/fw036/RULINGS.sha.tsv`（不覆寫他線未入庫之變更）；
  未動 `features/vsm_v43/`；未執行 W-1′ 之後任一步。
- **未開 DR 之理由**：同 A-VL1 —— 本項為專案內部流程（Pei 入庫）與下放包預期數陳舊，
  非上游資料疑義；DR 送出權屬 Pei（禁區第 6 條）。
- **解除條件**（三項，請分析層／Pei 裁）：
  1. Pei 將 `docs/fw036/RULINGS.sha.tsv`（及其同批他線變更）入庫，使其為乾淨；
  2. E17 之預期數自 14 更新為**重生當下實測之 R-VT 條數 ＋ 9**，或改為
     「新增列全為 `R-VL*`／`R-VT*`，且修改 0、刪除 0」之**性質判準**
     （數值判準隨姊妹線落檔而失效，此為其第一次失效）；
  3. E18 之量測面裁定：改比 `body_sha8`（防條文遭改），或維持 `sha8`
     並將 R-VL2 之新值 `582d0c6d` 認列為基線。


## Assumption markers

None yet. Inline format in generated JSON reasoning：`[ASSUMPTION A-VLnn]`。
