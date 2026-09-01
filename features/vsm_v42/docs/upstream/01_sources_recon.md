# 上繳包 01 — vsm_v42：停於 W-0（台帳前提不成立）

日期：2026-09-01　執行層：Claude Code　對應下放包：`docs/handoff/01_sources_recon.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | 上繳 00 之一處自誤：`§9` 裸節號自我引用致 canon_refs 判 ambiguous，改為「本包第 9 節」（見第 12 節） |
| 核實無誤 | E19／E20／E21／E22 四項唯讀預檢全數相符；五件原檔到齊（16 MB） |
| 正確地不動 | **W-0～W-6 全數未執行** —— `docs/fw036/RULINGS.sha.tsv` 實測仍為 `M`，觸下放包 01 第 6 節升級條件第 1 條，該條明令「停下回報，**不覆寫**」；W-0 為本包首步且順序不得調換，故其後六步一併不動 |

**總判：停於 W-0。三項升級條件同時觸發（A-VL3）。**

---

## 0. W-0 之前置檢查與三項停下（本包唯一之實質結論）

### 停下 1 —— `RULINGS.sha.tsv` 非乾淨（第 6 節升級條件第 1 條）

```
$ git status --short docs/fw036/RULINGS.sha.tsv
 M docs/fw036/RULINGS.sha.tsv
```

**未執行 `python3 scripts/rulings_hash.py`（不帶 `--out`）**，該檔逐位元未動。

其未入庫變更之性質（`git diff --numstat` → `355  339`）：working 版相對 `HEAD`
多出 **16 個條號**，全為**他線**——

| 多出之條號 | 歸屬 |
|---|---|
| `R-G29`、`R-G42` | canon 第 9.2 節（全域） |
| `R-ICS45` – `R-ICS58`（14 條） | `features/ics_management/` |

working 版含 `R-V[LT]` 列數 **0**（即本線與姊妹線之條文均尚未入台帳）。
R-VL9 之前提「Pei 先將現行 working tree 入庫，避免與他線交疊」**尚未滿足**。

### 停下 2 —— E17 已知不可達（第 6 節升級條件第 1 條後半）

以 `--out <scratchpad>/sim_now.tsv` **模擬**重生（**未寫入 `docs/fw036/RULINGS.sha.tsv`**），
對現行 working 版逐行 diff：

| 項 | 預期（E17） | 實測 | 判 |
|---|---|---|---|
| 新增列 | 14 | **17** | **不符** |
| 修改列 | 0 | **0** | 相符 |
| 刪除列 | 0 | **0** | 相符 |

新增之 17 列逐一：
`R-VL1 R-VL2 R-VL3 R-VL4 R-VL5 R-VL6 R-VL7 R-VL8 R-VL9`（**9**，本線）
＋ `R-VT1 R-VT2 R-VT3 R-VT4 R-VT5 R-VT6 R-VT7 R-VT8`（**8**，姊妹線）。

**差之所在**：下放包 01 第 3 節寫「R-VT1–R-VT5（5）」，係依上繳 00 第 11 節丁
當時之實測所寫；其後 `vsm_v43` 續有落檔，現實測
`grep -n "^### R-VT" features/vsm_v43/RULINGS.md` 得 **8 個錨點**（R-VT1–R-VT8）。
**本包不自行把預期調成 17**（FO 第 8.2 節：不自行調和）。

> **本項為 FO 第 8.3 節「第二層」之一次真實命中**：預期數字攔下的不是簿子的錯，
> 而是**預期數字自身的陳舊**。其成因可具名：**E17 用的是數值判準，而其被數之對象
> （姊妹線條數）在兩包之間會動**。建議改為性質判準，見第 13 節第 2 項。

### 停下 3 —— E18 一項不同（第 6 節升級條件第 2 條）

| 條號 | 上繳 00 第 9 節所報 sha8 | 本包實測 sha8 | 判 | body_sha8（上繳 00 ↔ 本包） |
|---|---|---|---|---|
| R-VL1 | `2a3dd0b6` | `2a3dd0b6` | **相符** | `5897969a` ↔ `5897969a` |
| **R-VL2** | `d6a189ed` | **`582d0c6d`** | **不同** | `01c67a04` ↔ **`01c67a04`（相同）** |
| R-VL3 | `ec287e40` | `ec287e40` | **相符** | `e306aa75` ↔ `e306aa75` |
| R-VL4 | `49be4fb8` | `49be4fb8` | **相符** | `08cea35e` ↔ `08cea35e` |
| R-VL5 | `482a6990` | `482a6990` | **相符** | `1de01344` ↔ `1de01344` |

**不調和，但據實指出其性質**：R-VL2 之**條文本體未變**（`body_sha8` 逐字相同，
fenced block 未動，R-VL6(d)「R-VL2 原文不改，加註指向本條」確實被遵守）；
變的是**節**——節內、fenced block 之外新增了 R-VL6 之加註四行，`body_lines` 32 → 37。
`rulings_hash.py` 之 `sha8` 涵蓋整節（含加註），`body_sha8` 只涵蓋 fenced 本體。

即 **E18 之量測面（`sha8`）與其所欲防之事（條文遭改）不同軸**：
凡依 R-TM13 加註者必動 `sha8` 而不動 `body_sha8`，而 R-TM13 加註正是本專案之常規動作。
E18 若維持比 `sha8`，**每一次合法加註都會誤停一次**。裁決建議見第 13 節第 3 項。

---

## 1. W-1′ feature.yaml 修正（R-VL7／R-VL8(c)）

**未執行。** W-0 未過，順序不得調換。
`features/vsm_v42/feature.yaml` 現況維持上繳 00 之狀態：
`tc_id_prefix: "NR1L-VSM42-"` **仍在**、`write_back.tc_id_format` **未加**、
`done_region.author_value` 仍為 `"Arif"`、`spec_reference_template` 仍為執行層自填之構造式。

**下放包第 5 節所要之「W-1′ 後之 feature.yaml 三鍵實值」：無值可報。**

---

## 2. W-2 sources 落檔

**未執行。** `sources/raw/` 下無 `vf665_*` 任一目錄；`sources/extracted/` 未產；
`sources/MANIFEST.tsv` 未加列；`features/vsm_v42/sandbox/` **未建**；
`features/vsm_v42/inputs/` **未清空**（5 件原檔原封不動）。
R-G28 之嵌入物件清點**未執行**（其為 W-2 之末項）。

### 原檔到齊確認（第 6 節升級條件末條「原檔仍缺任一件」→ **未觸發**）

`features/vsm_v42/inputs/` 實測 **5 件**，`du -sh` 得 **16 MB**（下放包所載 16.46 MB）：

| # | 實檔名（MANIFEST 應記之名） | bytes | mtime |
|---|---|---|---|
| 1 | `Vehicle_Setup_Management_by_VP_-_LTM_(R1_Low)_VF665_V42_R6.docx` | 118,453 | 08-29 06:41 |
| 2 | `FM-WI-FSM-035-A02_VF665_V42_STLA 技術安全需求分析報告_SYSRA STLA Vehicle Setup Management Requirement Analysis Report_SYSRA_VF665_V42_Released.xlsx` | 352,682 | 08-28 01:41 |
| 3 | `FM-WI-FSM-037-A03_SWE1_VF665_STLA 報告_SWRA_STLA_Park_Sense_And_Restore Default Setting __Features_Report.xlsx` | 50,923 | 09-01 15:57 |
| 4 | `FM-WI-FSM-037-A03_SWE1_VF665_STLA 報告_SWRA_STLA_Side_Distance_Warning - Audio_Repetition Features_Report.xlsx` | 45,395 | 08-26 09:35 |
| 5 | `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | 16,694,938 | 08-16 06:32 |

實檔名與 00 包第 3 節所載之差異（下放包 01 已預告「以實檔為準」）：
#1 全名以底線取代空白且無方括號；#2 前綴為 `FM-WI-FSM-035-A02_`（非 `FMWIFSM035A02`）；
#3 `Restore Default Setting __Features` 為「空白＋雙底線」；
#4 `Side_Distance_Warning - Audio_Repetition`（空格連字號空格，非雙底線）。
**A-VL1 之缺件狀態已由本節之實測解除**（其登記時 `_intake/` 確為 0 files，記錄不追溯改寫）。

---

## 3. W-3 recon／4. W-4 leaf 母體／5. W-5 訊號解析預查／6. W-6 anomaly 登記

**四者皆未執行。**

- `RECON.md`：未產出。`DECISIONS.md`：仍為 scaffold 空白模板，未預填、未簽。
- `data/leaves.tsv`：未產出；跨源對帳無數；DR-VL1 之「約 190」**未回填**。
- `data/signal_chain_v42.tsv`：未產出。七檔各命中數、結果分布**皆無數**。
  **§K 衝突表**（下放包第 5 節要求「空亦列」）：

  | 規格原名 | 命中處 A（檔／分頁／欄／列） | 解得 A | 命中處 B | 解得 B | 交 Pei 之問 |
  |---|---|---|---|---|---|
  | （空 —— W-5 未執行，非「查無衝突」） |  |  |  |  |  |

  **本表為空之語意是「未查」，不是 E23 = 0。** E23 之判見第 7 節。
- `forms/LOOKUP_MISSES.md`：未新增任何列。
- W-6 之三項候選 anomaly（037 `Categorization` 空 1 列；SYSRA Functional 之 EE 空 112 列；
  SYSRA DocID 空 249 列）**仍未登記** —— 其登記以 E5／E9／E10 實測為前提，本包未測。

---

## 7. 預期數字逐項對照（00 包 E1–E16 ＋ 01 包 E17–E23）

**掃描條件揭露**：凡標「唯讀預檢」者，係對**原地檔案**之唯讀量測，未建立任何副本、
未寫入任何目標檔 —— 其不等於執行該步，僅為缺 W-0 時仍可提出之證據。

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| E1 | #3 有 SWE id 列數 | 82 | 未實測（W-3 未執行） | — |
| E2 | #4 有 SWE id 列數 | 70 | 未實測 | — |
| E3 | Functional leaf 合計 | 128 | 未實測 | — |
| E4 | Heading 合計 | 23 | 未實測 | — |
| E5 | `Categorization` 空列 | 1 | 未實測 | — |
| E6 | Functional Source ID 去重 | 128 | 未實測 | — |
| E7 | SYSRA 資料列 | 1040 | 未實測 | — |
| E8 | SYSRA Functional | 318 | 未實測 | — |
| E9 | SYSRA Functional 之 EE 空 | 112 | 未實測 | — |
| E10 | SYSRA DocID `VF665_V42_P637MCA` | 791 | 未實測 | — |
| E11 | 037 描述內 CAN 訊號名 | 71 ＋ 70 | 未實測 | — |
| E12 | 037 描述內 `PROXI` | 48 ＋ 23 | 未實測 | — |
| E13 | 037 描述內 `$token$` | 14 ＋ 16 | 未實測 | — |
| E14 | LID `CAN Mapping` 三詞命中列 | 65 | **65**（上繳 00 已測，本包未重測） | **相符** |
| E15 | LID `637MCA Specific Signals` 非空列 | 22 | **22**（同上） | **相符** |
| E16 | 037 之 E3 ↔ E8 命中 | 128 | 未實測 | — |
| **E17** | W-0 台帳 diff 新增／修改／刪除 | 14／0／0 | **17／0／0** | **不符**（見第 0 節停下 2） |
| **E18** | R-VL1–R-VL5 sha8 與上繳 00 第 9 節逐字相同 | 全同 | **4 同 1 異**（R-VL2） | **不符**（見第 0 節停下 3） |
| **E19** | sandbox/base 副本 sha256 = `6372fb6b…825b2`，cmp 全等 | — | **母本實測 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`（唯讀預檢，與 E19 所載逐字相同）；副本未建，cmp 未做** | **部分**（來源端相符；副本端未驗） |
| **E20** | 副本 r9 表頭：design_method／author 欄 = R／AA | R／AA | **R／AA**（唯讀預檢，對 forms/ 母本；副本未建） | **相符** |
| **E21** | #5 SYSAD 原檔 sha256 = `469162b8…` | 相同 | **`469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200`，兩檔逐字相同** | **相符** |
| **E22** | #1 docx magic bytes = `50 4B 03 04` | `50 4B 03 04` | **`504b 0304`**（`xxd -l 4`） | **相符** |
| **E23** | `signal_chain_v42.tsv` 之 B-1 衝突列 | 0 | **無數**（W-5 未執行） | — **不得記 0** |

### E20 之完整實測（先驗逐欄對照，非免測）

對 `forms/…_SWQT_20260817_ext.xlsx` 分頁 `Test Case Specification 測試用例規範` 第 9 列
（openpyxl `read_only=True, data_only=True`，逐格取非空值）：

| 先驗（R-VL8(b)，自 bed_lowering 同 sha 母本） | 實測 | 判 |
|---|---|---|
| sheet `Test Case Specification 測試用例規範` | 分頁清單第 6 個，逐字相同 | **相符** |
| priority = P | `P9 = 'Test Case Priority\n測試用例優先級別'` | **相符** |
| estimated_test_time = Q | `Q9 = 'Estimated Test Time (mins)…'` | **相符** |
| design_method = R | `R9 = 'Test Case Design \nMethods\n測試用例設計方法'` | **相符** |
| functional_safety = S | `S9 = 'Functional Safety\n功能安全'` | **相符** |
| author = AA | `AA9 = 'Test Case Author\n測試案例作者'` | **相符** |
| test_version = AB | `AB9 = 'Test Version\n測試版號'` | **相符** |

其餘欄一併實測（供 W-2 回填時直接採用，**仍須自副本重測**）：
`B` No.#／`C` Requirement or Design ID (Polarion)／`D` Requirement or Design ID／
`E` Test Case ID (TestRail)／`F` Test Case ID／`G` Test Group／`H` Test Set／`I` Test Item／
`J` Pre-Conditions／`K` Input Test Data／`L` Test procedure／`M` Expected Result／
`N` Specification Reference／`O` Test Case Reference ID／`T`–`Z` 七個車型欄
（`V9 = 'VF(ProMaster)637\nAtl-Mi'` —— **本線 P637MCA／ATL-Mi 對應 V 欄**）／
`AC` Test Vehicle (Bench)／`AD` Test Period／`AE` Tester／`AF` Test Result／
`AG` Defect ID／`AH` Remarks。

> **scaffold 模板值之誤已證實**（R-VL8(b) 所預告）：模板之
> `design_method: "Q"`、`author: "Z"` **皆錯**（實為 R／AA），
> 且模板之 `sheet: "Test Case Specification&Result"` 於本母本**不存在**
> （實為 `Test Case Specification 測試用例規範`）。上繳 00 之 feature.yaml
> 沿用了該三個模板值 —— 其為 W-2 待修，非本包可改（W-0 未過）。
> **另註**：模板未列 `estimated_test_time` 鍵，而母本 Q 欄有此欄；
> W-2 回填時是否納入該鍵，請分析層一併裁。

---

## 8. 新開 anomaly 與 DR 成對清單；未結 DR

| 編號 | 標題 | 阻塞 | 成對 DR |
|---|---|---|---|
| **A-VL3** | W-0 之前提不成立：`RULINGS.sha.tsv` 仍為 `M`，且重生 diff 非 14 列 | **是** | 無（理由同 A-VL1，分析層已裁可該型） |

全文落 `features/vsm_v42/ANOMALIES.md`。A-VL1（PENDING，缺件）之**事實面已解除**
（原檔 5 件到齊，見第 2 節），其狀態改判屬 Tier 2，本包不自行改為 RESOLVED，只記明。
A-VL2 為分析層自誤登（RESOLVED），本包未動。

### 未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中約 190 列無 037 覆蓋 | no | 已登記，未送出；**實數未回填**（W-4 未執行） |

本包未送出任何 DR（禁區第 6 條）。

---

## 9. R-VL6–R-VL9 之 sha8

下放包第 2 節要求「sha8 於本包 W-0 重生台帳後**自 `docs/fw036/RULINGS.sha.tsv` 讀取**回報」。
**該台帳未重生，故無法自該檔讀取。** 以下為**自 `features/vsm_v42/RULINGS.md` 原文直算**
（同一工具、同一量測條件，`--target features/vsm_v42/RULINGS.md --out <scratchpad>`），
**其來源不同於下放包所指定者，據實標明**：

| 條號 | 一句話 | sha8（自原文直算） | body_sha8 | body_kind | 行 |
|---|---|---|---|---|---|
| R-VL6 | R-VL2(b) 加註：段 1 入口依 R-P375 擴為 forms/ 全部參考檔 | `bba2d813` | `7321474a` | fenced | 112 |
| R-VL7 | TC ID 鍵名採全庫慣例 `write_back.tc_id_format` | `30ba05fa` | `afb452ed` | fenced | 131 |
| R-VL8 | sandbox/ 與 R-G1 母本之時點；欄位自母本 r9 實測 | `762824c8` | `3c02775c` | fenced | 140 |
| R-VL9 | `RULINGS.sha.tsv` 之重生歸屬 | `67a2d29b` | `5a0230ee` | fenced | 155 |

九條 R-VL 皆為 `fenced` 本體，無 `section` 型（R-G29 之要求）。

### 本包所讀之引用條文（自 repo 原文）

| 條號 | 來源檔:行 | 所讀要點 |
|---|---|---|
| R-P353 | `features/power/RULINGS.md:12143` | 可觀察目標白名單四類 |
| R-P355 | 同檔 :12198 | 內部訊號不得直接 Set |
| R-P368 | 同檔 :12443 | 三段鏈；(b) 須載明欄／列，不得語意跳接；(e) R4 降旁證，B-1 衝突 |
| R-P369(b) | 同檔 :12473 | 拼法不一致者二名皆入段 1；解至同一標的為同物，記等同 |
| R-P375 | 同檔 :12640 | 段 1 入口擴為 forms 全部參考檔；`.Req` 走 UI／PROXI；(d) 命中即候選非認定 |
| IN 第 8.7.5 節 v3 (a)–(g) | `docs/runtime/ASPICE_SWE6_AI_Instruction.md:517` | `$MESSAGE.Signal$`；PROXI 不加 `$`；(d)(g) 保留原名 |
| FO 第 8 節 | `docs/fw036/FEATURE_ONBOARDING.md:503` | 契約三層檢驗、結果三分法、執行層三不 |
| R-VL1–R-VL9 | `features/vsm_v42/RULINGS.md` | 全文 |

---

## 10. 獨立判斷：本包是否仍有該驗而未驗者

1. **在 W-0 阻塞之前提下：無。** W-1′～W-6 之每一步皆在 W-0 之後，順序不得調換。
   E19–E22 四項因其來源（forms/ 母本、inputs/ 原檔）已在位且量測為唯讀，已先行提出；
   E20 並做到**逐欄**而非只驗下放包點名之二欄。
2. **一項自我糾錯**：上繳 00 之第 328 行以裸 `§9` 自我引用，經 canon_refs 判為
   ambiguous（FO 與 IN 皆有第 9 節）而計入該閘之紅。**本包已改為「本包第 9 節」並複驗消除**
   （見第 12 節）。此為上繳 00 未察之自造紅，據實登出。
3. **一項未做而應由分析層裁**：E23 之「0」與「無數」在本上繳中被嚴格區分。
   若下一包沿用「E23 = 0（預期）」而執行層又未跑 W-5，容易被讀成「已驗無衝突」。
   建議 E23 之判準加一句「未執行 W-5 時記『無數』，不得記 0」。
4. **一項存疑，非本包可決**：`features/vsm_v42/inputs/` 之 5 件原檔於
   W-2 落 `sources/raw/` 後須清空。該目錄已 gitignored，但**其清空為不可逆之刪除**
   （原檔在 repo 內別無副本，`_intake/Vehicle_Setup_VF665/` 仍為 0 files）。
   建議 W-2 之次序改為「先落 `sources/raw/` ＋ 逐檔 `cmp` 全等 ＋ MANIFEST 落列，
   三者皆過後方清 `inputs/`」，並於下放包明文。本包不自行執行。

---

## 11. `python3 scripts/gate_all.py` 輸出

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 503
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
```

### 升級說明（FO 第 8.2 節）

**四支與上繳 00 同批，逐支歸因如下；`rulings_hash` 之不過本包為刻意。**

**(甲) `canon_refs` 503（上繳 00 時為 501，+2）** —— 本包做了**逐檔逐行**歸因，
工具為 `canon_refs.py --emit-waiver <scratchpad>/allrefs.tsv`（**輸出落 scratchpad，
未寫入 repo 之 waiver 表**），全表 946 列，其中路徑含 `vsm_v4` 者**僅 4 列**：

| source | kind | target | line | reason | 歸屬 |
|---|---|---|---|---|---|
| `features/vsm_v42/ANOMALIES.md` | ruling | `R-G40` | 57 | active-backlog | **分析層**所寫之 A-VL2 內 |
| `features/vsm_v42/RUNBOOK.md` | section | `§3` | 9 | active-backlog | **`new_feature.py` 之 skeleton** |
| `features/vsm_v43/RUNBOOK.md` | section | `§3` | 9 | active-backlog | 同上（姊妹線） |
| `features/vsm_v42/docs/upstream/00_intake_recon.md` | section | `§9` | 328 | historical-record | **本執行層之誤 → 已改，見第 12 節** |

改後複驗（`--emit-waiver <scratchpad>/allrefs2.tsv`）：含 `vsm_v4` 之列**由 4 降為 3**，
第四列消失。餘 501 之組成與上繳 00 同（unresolved 之 21 個 target 全為
`R-G31`–`R-G41`，站點集中於 `docs/fw036/RULINGS_LEDGER.md` 與 `features/display/`）。

> **未預期之發現（1）—— `new_feature.py` 之 skeleton 自帶一個 canon_refs 紅**：
> `scripts/new_feature.py` 之 `RUNBOOK_SKELETON` 第 9 行寫
> `- [ ] spec_mode classified: ___  (FEATURE_ONBOARDING §3)`。
> 裸 `§3` 為 FO／IN 共用節號（canon_refs 自報「兩 canon 共用之節號 17 個」含 `3`），
> 故**每一個以本腳本 scaffold 出來的新 feature 都會帶進一列 ambiguous**
> —— 本次一口氣兩列（vsm_v42 ＋ vsm_v43）。
> 修法一行：改為 `FEATURE_ONBOARDING.md §3`。
> **本包未改**：`scripts/` 為共用檔，改之即分析層 FO 第 8.6 節第 4 項所戒之
> 「先改共用檔」。請分析層裁由誰改。

**(乙) `gates_tsv`** —— 與本線無關，先在。差異 6 列全為 sw_update／driver_distraction／
ics_management 之閘與 canon `body_kind` 列，與上繳 00 所報同。`features/vsm_v42/scripts/` 為空。

**(丙) `lint_paths` = 4** —— 與本線無關，先在，四筆與上繳 00 逐字相同
（driver_distraction 兩本工作簿落點、ics_management 與 sw_update 之 delivered sha）。
`features/vsm_v42/` 下**仍無任何 xlsx**（sandbox 未建、inputs/ 之 4 個 xlsx 位於
gitignored 目錄且 lint_paths 對 `inputs/` 為合法落點）。

**(丁) `rulings_hash`** —— **本包刻意不使其轉綠**。使其轉綠之唯一動作即 W-0
（重生台帳），而 W-0 之前提（該檔為乾淨）不成立，下放包明令「停下回報，**不覆寫**」。
若逕自重生，將把他線 16 條未入庫之新條號（`R-G29`、`R-G42`、`R-ICS45`–`R-ICS58`）
連同本線一併壓進同一份輸出，**正是 R-VL9 之前提所欲避免的「與他線交疊」**。
故此紅為**依令而紅**，非漏做。

**結論**：四支之中三支先在於本線之外，一支為依令暫留；
本包唯一自造之紅（canon_refs 之 `§9`）已改正並複驗消除。

---

## 12. 本包之寫入清單（逐檔）

| 檔 | 動作 | 授權 |
|---|---|---|
| `features/vsm_v42/ANOMALIES.md` | 新增 A-VL3 | 00 包禁區第 5 條「遇停下條款即登記並停」 |
| `features/vsm_v42/docs/upstream/00_intake_recon.md` | 一處字面修正：`已於 §9 全數提出` → `已於本包第 9 節全數提出` | 第 10 節第 2 項所述之自造 canon_refs 紅；改的是本執行層自己的上繳文字，未動任何數字、結論或 sha |
| `features/vsm_v42/docs/upstream/01_sources_recon.md` | 新建（本檔） | 下放包 01 第 5 節 |
| `features/vsm_v42/docs/INDEX.md` | 加 01 列 | FO 第 8.7 節 |

**未動**（逐項聲明）：
`docs/fw036/RULINGS.sha.tsv`（**W-0 之標的，依令不覆寫**）、`docs/runtime/GATES.tsv`、
`docs/fw036/CANON_REFS_WAIVER.tsv`、`scripts/`（含 `new_feature.py`）、
`features/vsm_v42/feature.yaml`（W-1′ 未執行）、`features/vsm_v42/inputs/`（未清空、未改）、
`features/vsm_v42/sandbox/`（未建）、`sources/`、`forms/`（含 `LOOKUP_MISSES.md`）、
`features/vsm_v43/`、`features/vehicle_setting/`、`docs/runtime/profiles/`、
`features/vsm_v42/docs/handoff/`（分析層之檔）、`features/vsm_v42/{RULINGS.md,DATA_REQUESTS.md}`。
**git**：本包未執行任何 git 寫入指令（`status`／`diff`／`show` 為唯讀，用於 W-0 前置檢查與歸因）。

---

## 13. 待 Pei／分析層之五項

1. **Pei 將 `docs/fw036/RULINGS.sha.tsv`（及其同批他線變更：`R-G29`、`R-G42`、
   `R-ICS45`–`R-ICS58`）入庫**，使該檔為乾淨 —— A-VL3 之解除條件其一，阻塞 W-0～W-6。
2. **E17 改為性質判準**：現行數值判準「14」已隨姊妹線自 R-VT5 增至 R-VT8 而失效。
   建議改為「新增列之 `ruling_id` 全數 ∈ {`R-VL*`, `R-VT*`}，且修改 0、刪除 0」，
   並將實際條數列為觀測值而非門檻。
3. **E18 之量測面**：R-TM13 加註必動 `sha8` 而不動 `body_sha8`。
   建議 E18 改比 `body_sha8`（防的是條文遭改），或維持 `sha8` 而將 R-VL2 之
   `582d0c6d` 認列為新基線。二者擇一即可解除 A-VL3 之該項。
4. **W-2 之 `inputs/` 清空次序**（第 10 節第 4 項）：建議明文為「落檔 ＋ cmp ＋ MANIFEST
   三者皆過後方清」。另 `estimated_test_time`（母本 Q 欄）是否納 `workbook.columns`。
5. **`new_feature.py` skeleton 之裸 `§3`**（第 11 節甲之未預期發現 1）：由誰改。
