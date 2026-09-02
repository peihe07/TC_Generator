# ANOMALIES — FW036 vsm_v42（Vehicle Setup Management R1 Low）

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format：`[A-VLnn]`（下放包 00 §五 W-6：A-VL 系列自 1 起）。
PENDING entries block their batch until a Pei ruling lands；
RESOLVED entries record the ruling verbatim.
Registration is Tier 1（record + propose）；disposition is Tier 2。

---

## A-VL1 —— `_intake/Vehicle_Setup_VF665/` 為空，五件原檔全缺（**RESOLVED** 2026-09-01，下放包 02 W-6）

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
- **解除條件**：#1–#5 原檔落入投遞區後重跑 W-2～W-6。
- **解除實測（2026-09-01，下放包 02 W-2）**：原檔改由 Pei 置於
  `features/vsm_v42/inputs/`（非 `_intake/`），5 件到齊共 16 MB；
  已依 R-VL11(a) `mv` 至 `sources/raw/`（sha 前後全等）並落 MANIFEST，
  `inputs/` 清空實測 0 項（E24）。**投遞路徑與 R-VL5 所定之投遞區不同，
  該落差記於本條，R-VL5 是否改寫交分析層。**

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

## A-VL3 —— W-0 之前提不成立：`RULINGS.sha.tsv` 仍為 `M`，且重生 diff 非 14 列（**RESOLVED** 2026-09-01，下放包 02 W-0）

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
- **解除實測（2026-09-01，下放包 02 W-0）**：Pei 已將 `RULINGS.sha.tsv` 連同
  `FEATURE_ONBOARDING.md`（R-G42 錨點）與 `RULINGS_LEDGER.md` 入庫（commit `b6668f4`）；
  `git status --short` 實測乾淨後重生，新增 **21 列**（R-VL1–R-VL11 11 ＋ R-VT1–R-VT10 10），
  修改 0、刪除 0 —— 依 R-VL10(b) 之性質判準 **E17′ 過**。
  E18′ 改比 `body_sha8`（R-VL10(a)），R-VL1–R-VL9 九條**逐字全同**，**E18′ 過**。
- **原解除條件**（三項，已由 R-VL10 與 Pei 之入庫滿足）：
  1. Pei 將 `docs/fw036/RULINGS.sha.tsv`（及其同批他線變更）入庫，使其為乾淨；
  2. E17 之預期數自 14 更新為**重生當下實測之 R-VT 條數 ＋ 9**，或改為
     「新增列全為 `R-VL*`／`R-VT*`，且修改 0、刪除 0」之**性質判準**
     （數值判準隨姊妹線落檔而失效，此為其第一次失效）；
  3. E18 之量測面裁定：改比 `body_sha8`（防條文遭改），或維持 `sha8`
     並將 R-VL2 之新值 `582d0c6d` 認列為基線。

> **處置（分析層 2026-09-01）**：2、3 依 R-VL10 裁（性質判準；body_sha8）；1 待 Pei 入庫。
> 本條於台帳重生成功（02 包 W-0）後轉 RESOLVED。A-VL1 之事實面已解（上繳 01 第 2 節），由 02 包執行層轉 RESOLVED。

---

## A-VL4 —— 分析層之誤（四項，01 下放包之預期數字）（RESOLVED）

- **登記日**：2026-09-01；**分析層之誤**。
- **(a) E17 跨線計數**：寫「14」時取 R-VT 當時條數 5，其後分析層自己又落 R-VT6–8，預期即陳舊。
  被數對象會動而用數值判準 —— 與「預配號」同族。→ R-VL10(b)。
- **(b) E18 比錯軸**：以 `sha8` 防「條文遭改」，而 `sha8` 含 R-TM13 加註；同包又命 R-VL6(d) 對 R-VL2 加註，
  兩條互斥。→ R-VL10(a)。（vsm_v43 之 E10 同誤，A-VT14。）
- **(c) E9（vsm_v43 00 包）「相異值 4」**：intake 時跡為 `Counter(...).most_common(4)` 之輸出列數，
  非相異值數。量測條件未揭露即寫成預期（R-G8 之反面）。→ vsm_v43 R-VT10(b)。
- **(d) E2（vsm_v43）措辭**：「Functional」指 `Functional Requirement` 全等，未寫全。→ R-VT10(b)。
- **通則**：預期數字逐項附量測條件（欄、判式、分母），不得只寫數；分析層自己的預期數字也適用 IN §8.4.1。


## A-VL5 —— 037 之 1 列 `Categorization` 為空（**併 DR-VL2(a)**，處置已落）

- **登記日**：2026-09-01（下放包 02 之 W-6）
- **實測**（掃描條件：`Analysis Report`，parksense 表頭列 7／sdw 表頭列 8，
  `SWE-Requirement ID` 非空為母體，`Categorization` 為 `None`）：**1 列**，逐列如下。

  | 檔 | SWE-Requirement ID | Requirement Title | Source Requirement ID |
  |---|---|---|---|
  | parksense | `SWE1-VC-IntelligentSpeedLimiterwithConfirmation-051` | Intelligent Speed Limiter with Confirmation | `Sys-RA-VF665_V42_VSM-845` |

- **問題**：該列既非 `Functional Requirement` 亦非 `Heading`，無從判其是否為 leaf。
  依 R-VL4，母體＝Functional leaf，故本列**不入母體**（128 不含之）。
- **本地處置**：`data/leaves.tsv` 該列 `tc_status` 標 `UNCATEGORIZED`，不生成 TC。
- **待裁**：若上游確認其為 Functional，母體由 128 增為 129，Layer 2 之
  `Speed Assist` 組由 4＋1 變 5。**本包不自行改判。**

---

## A-VL6 —— SYSRA Functional 318 列中 112 列 `EE Architecture` 為空（**併 DR-VL2(b)**）

- **登記日**：2026-09-01（下放包 02 之 W-6）
- **實測**（`Analysis Report`，表頭列 5，`分類 Category == 'Functional Requirement'`
  之 318 列中，同列 `EE Architecture (All, ATL-Hi, ATL-Mi)` 為 `None`）：**112 列**。
  該 318 列之 EE 分布：`ATL-Mi` **206**／空 **112**。
- **交叉觀察**：全簿 `文件識別碼 Document ID` 為空者 **249 列**，其 Category 分布為
  Functional 112／Heading 42／Information 39／Out of Scope 56 ——
  **Functional 之 112 與 EE 空之 112 為同一批**（兩欄同缺）。
  即缺的不是單一欄，是這 112 列的**適用性標註整組未填**。
- **影響**：本線 EE 為 ATL-Mi、DocID 為 `VF665_V42_P637MCA`（791 列）。
  該 112 列無從判其是否適用本線車型。其中被 037 覆蓋者才會進入母體。
- **本地處置**：`data/leaves.tsv` 已逐列帶出 `sysra_ee_architecture` 與
  `sysra_doc_id` 兩欄，空者可直接篩出。不自行補值（IN §8.4.1）。
- **與 DR-VL1 之關係**：DR-VL1 問的是「318 中 191 列無 037 覆蓋」，本條問的是
  「318 中 112 列無 EE／DocID 標註」，兩者交集未另計，**不合併**。

---

## A-VL7 —— 037 一 Functional leaf 之 Source ID 於 SYSRA 為 `Heading`（**併 DR-VL2(c)**，處置已落）

- **登記日**：2026-09-01（下放包 02 之 W-4 跨源對帳，**下放包未預期之發現**）
- **實測**：037 之 128 個 Functional leaf 其 `Source Requirement ID` 於 SYSRA
  `Sys-RA-Feature-ID` **命中 128／128（E16 相符）**；但將命中列之 SYSRA `分類 Category`
  取回後為 **Functional Requirement 127 ／ Heading 1**：

  | 037 檔 | SWE-Requirement ID | Source Requirement ID | 037 Categorization | SYSRA Category |
  |---|---|---|---|---|
  | parksense | `SWE1-VC-SurroundCameraGridlines-063` | `Sys-RA-VF665_V42_VSM-857` | Functional Requirement | **Heading** |

- **為何 E16 仍相符**：E16 之判式為「Source ID ∈ SYSRA `Sys-RA-Feature-ID`」，
  **不含類別一致性**。128 全命中為真，而其中一列跨源類別不一致 —— 兩件事。
- **影響**：SYSRA Functional 318 之覆蓋計算受此影響 ——
  被 037 覆蓋之 SYSRA Functional 實為 **127**（非 128），未覆蓋為 **191**（非 190）。
  DR-VL1 之實數因此為 191，見 `DATA_REQUESTS.md`。
- **本地處置**：該 leaf 依 037 之 `Functional Requirement` 留在母體（037 為需求單位之
  權威，IN §8.2／R-VL4），**不因 SYSRA 之 Heading 而剔除**；`data/leaves.tsv` 之
  `sysra_category` 欄留有證據。
- **待裁**：是否併入 DR-VL1 一併向上游詢問（類別歧異），或另開 DR。**本包不自行送出。**

---

## A-VL8 —— 段 1（LID）對本線 CAN 訊號名幾近全不命中；`637MCA Specific Signals` 命中 0（**阻塞面已解除** 2026-09-02；段 1 命中率之問仍在）

- **登記日**：2026-09-01（下放包 02 之 W-5，**下放包未預期之發現**）
- **實測**（`data/signal_chain_v42.tsv`，251 名；段 1 入口為 forms 五個 xlsx 之
  全部分頁，比對式＝逐字／去 `.Req`_`.Info` 後綴／忽略底線空白大小寫）：

  | 段 1 命中之檔／分頁 | 涉及訊號名數 |
  |---|---|
  | `PROXI_HDCC27_R3` `Format` | 36 |
  | LID `CAN Mapping`（`Atlantis High` 欄組 Z 及名稱欄 A/B/C） | **9** |
  | LID `Proxi & Configuration` | 6 |
  | `HMI Settings List R1 SR25` `Settings` | 2 |
  | **LID `637MCA Specific Signals`** | **0** |
  | `SR26 Default Settings` | 0 |
  | `SR24 Market Configuration Table` | 0 |

- **R-VL6(c) 之二欄組實測結論**：`Atlantis High` 欄組 **9 名**、
  `637MCA Specific Signals` 分頁 **0 名**、兩者皆命中 **0 名**。
  故「二擇一」在本線為**空問題** —— 637MCA 分頁（22 列）與本線 251 個訊號名
  **無任何交集**。**不自選、不合併**，據實登記。
- **連帶之嚴重後果**：107 個 CAN 形訊號名中，**三段皆過者僅 3 名**；
  另 **32 名**為「段 1 未命中，而其規格原名本身已是 `MESSAGE.Signal` 形、
  段 3 於 DBC 逐字查得」。依 R-P368(a) 之字面，後者**不得**寫 `$MESSAGE.Signal$`
  （三段未皆過）；依其意旨（DBC 實名為準）則可。**本包不自行認定**，
  32 名於 tsv 中 `result=解得`、`result_detail=段1未命中…`，兩者分開可篩。
- **待裁**：(a) 段 1 未命中而段 3 逐字查得者，可否寫 `$...$`；
  (b) 若否，該 32 名之處置（`PENDING: DR-VL{n}` 或保留原名不加 `$`，R-P368(f)）。
- **2026-09-02 更新（下放包 03 補遺／R-VL14）**：本條之**阻塞面已解除**。
  ATL-Mi DBC 到件後以 `Atlantis` 欄組 ＋ 該 DBC 重跑（v3）：
  **解得 98 名**（CAN 95），「訊息名不符(R-13)」由 40 降為 **7**，
  「段3待ATL-Mi DBC」73 名歸零。原問之 (a)(b) 兩點（可否寫 `$…$`、32 名之處置）
  **由 R-VL14(d) 回答：解得者得寫**。
- **未解除之部分（本條保留為 PENDING 之理由）**：段 1 之**命中率**問題仍在 ——
  112 個 CAN 名中段 1（LID）命中僅 **30**，其餘 82 名係依 R-VL12(c)「段 1 不適用」
  （規格原名已為 `MESSAGE.Signal` 形）直入段 3。`637MCA Specific Signals` 分頁
  命中仍只有 **2** 名。即：LID 對本線之覆蓋本身偏低，只是不再阻塞交付。
- **另記**：89 個訊號名有「前綴／後綴差異」之寬鬆候選而無嚴格命中，
  已存於 tsv 之 `loose_n`／`loose` 兩欄，**不驅動結果**（R-P375(d) 候選非認定；
  寬鬆比對曾試作為主判準，產生 68 筆假 B-1 衝突，屬 R-P368(b) 明禁之語意跳接，已撤）。

---

## A-VL9 —— 母 spec 之 Functional Diagram 為 WMF 圖，其訊號名不在文字層（**RESOLVED** 2026-09-01，R-VL12(e)）

- **登記日**：2026-09-01（下放包 02 之 W-2，R-G28 檢查）
- **實測**：`vf665_v42_spec_r6` docx zip members **25**；
  `word/embeddings/` **0 項**；`word/media/` **1 項** = `image1.wmf`（498,222 bytes）。
  該圖以 `r:embed="rId5"` 嵌於**段落 60**，其上一段（59）為標題
  `Functional Diagram`，再上一段（58）為 `This function describes the management of
  vehicle setup menu on the LTM`。
- **問題**：`Functional Diagram` 一節之內容**全在圖內**，docx 文字層於該處為空 ——
  正是 R-G28 所指「圖中載有未見於 docx 之數值與流程」之型態。
- **處置（已做）**：`soffice --convert-to svg` 將 WMF 轉為 SVG（向量，文字仍為文字），
  自 `<tspan>` 依 y／x 座標還原為 **240 行**，落
  `sources/extracted/vf665_v42_spec_r6/media/image1_text.tsv`；
  另存 `image1.png`／`image1.svg`／`image1.wmf`。
  W-5 之抽名以該 240 行為第四來源，**單獨貢獻 158 個訊號名**
  （其中 CAN 形 76、內部形 82）。
- **「由圖找列」**：該圖為單一 Functional Diagram，其文字已全數轉為可檢索之 tsv，
  故不逐張出二欄表，改以 `signal_chain_v42.tsv` 之 `sources` 欄標 `diagram`
  作為「由圖找列」之對映（可篩）。
- **裁決（R-VL12(e)，2026-09-01）**：Functional Diagram 之流向**不於 P3 文字化**；
  P4 逐 TC 需驗因果方向時依圖判，圖為來源（R-G28 型），不臆測。**本條 RESOLVED。**
- **下放包 03 執行時之補正（執行層自查）**：SVG 還原原以「同 y 即同行」接合，
  致圖上**相鄰但不同元件**之標籤被黏成一名，產生 **10 個偽名**
  （如 `IPC_VEHICLE_SETUP2.TyrePressureUnitClearPersonalData` ＝
  `IPC_VEHICLE_SETUP2.TyrePressureUnit` ＋ `ClearPersonalData.Info` 兩標籤）。
  已改為同 y 之內再依 x 間距（門檻 140 svg 單位）斷行，行數 240 → **786**，
  偽名 10 個全數消滅（重掃 `_VEHICLE_SETUP*.*SERVICE_SETUP` 型 → 0）。
  `image1_text.tsv` 已重產（該檔於上繳 02 已入庫，本包為修正）。

> **處置（分析層 2026-09-01）**：A-VL5／6／7 併 DR-VL2；A-VL8 由 R-VL12 接手（根因見 A-VL10），待 ATL-Mi DBC 後重判；
> A-VL9 依 R-VL12(e)（流向 P4 逐 TC 依圖判）RESOLVED。

---

## A-VL10 —— 分析層之誤：對 ATL-Mi 線承接 Atlantis High 之段 1 欄組與段 3 DBC（RESOLVED → R-VL12）

- **登記日**：2026-09-01；**分析層之誤**。
- **事實**：R-VL2(b) 逐字承接 PM 之 R-P368（段 1 LID `Atlantis High` 欄組，段 3 `PDT27_E2A_R1_*`）。分析層於同條末段
  **已寫下** SYSRA EE = ATL-Mi 與 `Atlantis High` 欄組之不合，卻標「待 recon」後連續三包令執行層只對 `Atlantis High` 欄組與
  `637MCA` 分頁分開計數 —— **從未令其看 LID `CAN Mapping` r2 之欄組表頭**。一次 `iter_rows(max_row=2)` 即可見
  `Atlantis`（P–T）與 `Atlantis High`（Z–AD）為兩個欄組。
- **後果**：V43 上繳 01–03 之「訊息名不符 28」、DR-VT3 之「DBC 版次對應」提問、K-1（LTM 匯流排）、A-VT16（兩弧主旁）、
  本線 A-VL8（段 1 幾近全不命中），**同源於此**：都是拿 Atlantis High 之欄組與 DBC 去解 ATL-Mi 之規格。
  實測（分析層自測，LID v1_78 × V43 v3 TSV）：Atlantis 欄逐字命中 21 vs Atlantis High 10；R-13 28 列中 Atlantis 命中 6 vs 0；
  `VehicleSpeedVSOSig` 於 Atlantis 欄為 `STATUS_CCAN3.*`（無 `BRAKE_FD_2`）。
- **同族**：A-VL2(b)（引用未讀到底）—— 這次是「實測已排入待辦卻把待辦當作已完成」；IN §8.4.1 之反面。
- **處置**：R-VL12（段 1 Atlantis 欄組；段 3 待 ATL-Mi DBC，DR-VL3）；vsm_v43 同記 A-VT22／R-VT13。DR-VT3 送出前須重寫。


## A-VL11 —— ATL-Mi DBC 之 `SG_` 驗收數與 R-VL14(a) 所載不符（**RESOLVED** 2026-09-02，R-VL14 加註）

- **登記日**：2026-09-02（下放包 03 補遺之 W-5′ 段 3 驗收）
- **條文所載**（R-VL14(a)／補遺）：`BO_ 139／SG_ 5568／VAL_ 619`
- **執行層實測**（`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`，
  latin-1 讀，CRLF；sha256 `5cac2abcecdf37e2f07991e26dc4cf748fe24874fde93af77a85ea8936d3ed16`）：

  | 項 | 條文 | 實測 | 判 | 掃描條件 |
  |---|---|---|---|---|
  | `BO_` | 139 | **139** | **相符** | `^BO_ ` 行首 |
  | `VAL_` | 619 | **619** | **相符** | `^VAL_ ` 行首 |
  | **`SG_`** | **5568** | **844** | **不符** | `^\s*SG_ ` 行首（訊號定義行）；去重後 **794** 個相異訊號名 |

- **不符之成因（實測歸因，非推測）**：以其他計法量測 ——
  「全檔出現 `SG_` 字串」**5572**、「含 `SG_` 之行數」**5571**；
  而全檔 `^BA_ ` 屬性行有 **5349** 行，其多數形如 `BA_ "..." SG_ <msgid> <signal> ...`。
  即 **5568 應為「`SG_` 字串出現數」而非「訊號定義數」**，差在 `BA_` 屬性行之引用。
- **不調和之聲明**：本包**不改判**，兩數並列。**檔案本身確為正件** ——
  `BO_` 與 `VAL_` 兩數逐字相符，且 R-VL14(b) 之六個爭議訊息
  （`TELEMATIC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP3`／
  `SERVICE_SETUP`／`TELEMATIC_SERVICE_SETUP`／`STATUS_CCAN3`，含 `VehicleSpeedVSOSig`）
  **經執行層逐一複驗全數在內**。
- **影響**：無。段 3 之解析以 `^\s*SG_ ` 之 844 行為索引，正確。
- **裁決（2026-09-02，R-VL14 加註）**：條文之 `SG_ 5568` 為字串出現數，訊號定義數為 **844**（去重 794）。**RESOLVED。**

## A-VL12 —— 規格原文拼字歧異，其一拼法段 3 查得、另一查無（**RESOLVED** 2026-09-02，R-VL16(a)）

- **登記日**：2026-09-02（下放包 03 W-5′-1／R-P369(b)）
- **實測**：規格原文有三對近似拼法，依 R-P369(b) **二名皆入段 1 查、未合併**；
  以 ATL-Mi DBC 實查後，各對之**一方解得、另一方查無**：

  | 對 | 拼法 A（段 3 結果） | 拼法 B（段 3 結果） |
  |---|---|---|
  | RestoreDefaultSetting | `SERVICE_SETUP.RestoreDefaultSetting`（**解得**） | `SERVICE_SETUP.RestoreDefaulSetting`（少一 `t`，**未解得(止於段3)**） |
  | RestoreDefaultSettingReq | `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettingReq`（**解得**） | `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq`（`Settimg`，**未解得(止於段3)**） |
  | TelematicSetupAck | `SERVICE_SETUP.TelematicSetupAck`（**解得**） | `SERVICE_SETUP.TelematicSetupACK`（**訊息名不符(R-13)**：`SG_ TelematicSetupACK` 在 `BO_ IPC_VEHICLE_SETUP`） |

- **判讀（執行層不裁，僅陳述）**：前二對之 B 拼法幾可確定為**規格之筆誤**
  （少字母／`n`→`m`），第三對之 A／B 為大小寫差異而**分屬不同 BO_**，非筆誤。
- **本地處置**：三對六名各自一列，**未合併、未以其一代其二**（R-P369(b)：
  解至同一 `MESSAGE.Signal` 者方為同物；本案未解至同一標的）。
- **裁決（2026-09-02，R-VL16(a)）**：新增結果值域 `未解得（規格拼字疑誤）`。
  **規格原名不改**（R-13／R-6），備註記正確拼法與佐證位置，佐證留檔不送；
  P4 遭遇時該列保留原名**不加 `$`**。**RESOLVED。**
- **本包全掃之增補（下放包只知兩例，實測為三例）**：依 R-VL16(a) 對
  v3 全表之「未解得(止於段3)」逐列做編輯距離 ≤ 2 之 DBC 近似名比對，
  除已知二例外另得**第三例**：

  | 規格原名 | 主 DBC 之近似名 |
  |---|---|
  | `SERVICE_SETUP.RestoreDefaulSetting`（少 `t`） | `RestoreDefaultSetting` |
  | `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq`（`Settimg`） | `RestoreDefaultSettingReq` |
  | **`TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req`** | **`SVC_Guidelines_Req`** |

  **第三例之方向與前二例相反，須指出**：`Gridlines`（格線）為攝影機領域之正確用語，
  而 DBC 寫 `Guidelines`（指引）—— **看起來是 DBC 拼錯，不是規格拼錯**。
  R-VL16(a) 之條件（「規格原名於正確拼法下於主 DBC 存在」）字面仍成立，
  故三列同記該值域；但其**成因方向不同**，據實記明，交分析層判是否分立值域。
  `TelematicSetupACK`／`Ack` 一對為大小寫差異而**分屬不同 `BO_`**，非拼字疑誤，
  維持「訊息名不符(R-13)」，不入本表。


## Assumption markers

None yet. Inline format in generated JSON reasoning：`[ASSUMPTION A-VLnn]`。
