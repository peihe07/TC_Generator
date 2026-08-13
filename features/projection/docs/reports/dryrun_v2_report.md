# Projection Phase 6 — Dry-run v2 報告

> 依 R-P53 檢查表 v2（R-P54 / R-P55 / R-P58 修訂）
> 執行日期：2026-08-12
> 腳本：`features/projection/scripts/dryrun_v6.py`（本輪為 `dryrun_v2.py`，其後
> 逐版演進為 v6；中間版未入庫且已刪除）
> 明細：`features/projection/data/dryrun_v6.audit.json`（本輪產出之 `dryrun_v2.json`
> 為中間版，含工作簿逐字內容故未入庫，已刪除）
> **未寫回 xlsx、未執行任何 git 操作。** 修訂後全簿於記憶體組成（原簿 + 11 批次 + 7 補列）。

## 總結

| 項 | 結果 | 關鍵數據 |
|---|---|---|
| D-1 diff 落點 | **PASS** | PRE 23 列、PROC 42 列、ER 6 列（窄口），聯集 **63 列**；非授權欄變更 0 |
| D-2 凍結欄雜湊 | **PASS** | 34 欄 × 559 列不符 **0**；8 分頁雜湊全數保留；例外 6 + 40 列 |
| D-3 列數列序 | **PASS** | **分支 A**；559 → 558 + 7 = **565 列**，末列 r568；被移動列 **0** |
| D-4 補列 | **PASS** | 7 條（5 條完整 TC + 2 條 BLOCKED 佔位）；未補 **0** |
| D-5 阻塞列對照 | **PASS** | 不重複 **75 列**，無編號可指 **0**（本輪新增 r177 / r188） |
| D-6 補列獨立驗證 | **PASS** | 7 條逐條驗，有誤 **0** |
| D-7 `proc_excerpt` 時效 | **PASS** | 35 列中更新 **29** 列 |
| D-8 artifact 時效標記 | **PASS** | **16 份**標記（包內記 13，差異見下） |
| D-9 `Test Case Framework` | **PASS** | 分頁存在但**完全空白**（`A1:A1`），未寫入 |
| D-10 八項基線 | **PASS** | 八項全數精確命中；補列納入後 **無一項位移** |

**整體：PASS。** 前次 FAIL 之兩項（D-4、D-1／D-2 條件衝突）皆已消解。

---

## 前置三步（§3 執行順序 1–3）

### 步驟 1 — R-P57 L-PJ1 優先序修正

`lint_defs.resolve_signal()` 改為 PROXI → DBC ∪ VF176 → ABORT。

執行中發現**修正解析式不足以達成 R-P57 之目的**：訊號指涉的**抽取式**先前散落
在三支腳本，三次寫法不同。要求點號左側全大寫的版本抽不到
`Car_Configuration_15.Vehicle_Line_Configuration`（PROXI 完整形式含小寫），
**PROXI 優先序因此永遠不被觸發** —— 解析對了也沒用。

已將抽取式收進 `lint_defs.RE_SIGREF` / `sigrefs()`（R-P49 同一理由）。

放寬左側大小寫後浮出 4 個非訊號假陽性，以**列舉式**豁免（不以樣式推斷，比照
R-P43 對 `PLACEHOLDER_WHITELIST` 之理由）：

| 字串 | 列 | 實際身分 |
|---|---|---|
| `bthci_cmd.opcode` | r481 | Wireshark 過濾式 |
| `tone_sin_1KHz.wav` | r521 | 音檔檔名 |
| `view.The` | r539 / r540 | 句號後未空格，非指涉 |

**全簿重跑（掃描範圍 = `SCAN_RISK` 六個文字欄，已移除 `$...$` 內容，含 5 條補列）**

| 權威 | 數 |
|---|---|
| FD | 27 |
| VF176 | 9 |
| PROXI | 5 |
| CAN-B | 2 |
| **ABORT** | **2** |

未解析二筆為 r151 / r152 之 `HCP_DISP2.Est_Range_BEV` —— DR#2／A-PJ03／R-P9
已登記之缺口，**正確地 ABORT**，非迴歸。

r270 / r271 之 `Car_Configuration_15.Vehicle_Line_Configuration` 現判為 PROXI，
交由 L-PJ2，L-PJ1 通過。

**負向驗證（6 項全過）**

| 輸入 | 期望 | 實得 |
|---|---|---|
| `Car_Configuration_15.Vehicle_Line_Configuration` | PROXI | PROXI |
| `BCM_FD_27.DAY_LGT_MD_DISP` | FD | FD |
| `STATUS_BH_BCM1.LowFuelWarningSts` | CAN-B | CAN-B |
| `TELEMATIC_NAV_INFO.Direction` | VF176 | VF176 |
| `TELEMATIC_NAV_INFO.LastAnnouncement`（VF176 有定義但未登記） | ABORT | ABORT |
| `FAKE_MSG.FakeSig` | ABORT | ABORT |

第五項是關鍵：R-P51 之登記表為**手動維護**，未登記者仍 ABORT，gate 未被繞過。

### 步驟 2 — R-P56 L-PJ9 基線 17

`lint_defs.BASELINE["L-PJ9 generic tool"]` 由 15 改為 17，並於註解記錄成因
（B2 之 CAN 步驟改寫消去 `CAN tool`，使 r177／r188 之 `A screen capture tool`
浮現）。r177／r188 已加入 `d5_blocked_rows.json`，指向 R-P56 與 DR#13。

### 步驟 3 — D-4 補列與 R-P54 分支判定

**判定：走分支 A。** `SWE1-PROJ-227` 補列成功且通過全部 gate，故 r562 可刪。

227 之來源（037 CPAA Verification Criteria）要求「Customer provided dedicated
phone APP」。執行層判定**此為執行資源阻塞而非撰寫阻塞** —— 與既有列之
`Need to test in real car env` 同型，比照 R-P35 之先例。步驟與判準皆可依來源
寫定，只是執行時需要該 APP 到位；已於 `Remarks` 載明並開 DR#15。

---

## D-1｜diff 只落在可編輯欄 + 授權例外

**變更欄位分布**

| 欄 | 列數 |
|---|---|
| `Pre-Conditions (I)` | 23 |
| `Test procedure (K)` | 42 |
| `Expected Result (L)` | 6（全部落在窄口 r424–r429） |
| **聯集** | **63** |

PRE 與 PROC 同列同改者 8 列：r151, r152, r167, r168, r169, r170, r270, r271。
`23 + 42 = 65`，減去重疊 8 得 57，加上僅改 ER 之 6 列得 **63** —— 與批次記錄之
63 列相符。

非授權欄變更 **0**；ER 變更落在窄口外 **0**。

**窄口 6 列逐列 diff**（R-P55 要求逐列列出，不得僅以「見 log」代替）

| 列 | 被刪詞元 | 新增詞元 | 純刪除 |
|---|---|---|---|
| r424 | `correctly` | 無 | 是 |
| r425 | `correctly` | 無 | 是 |
| r426 | `correctly` | 無 | 是 |
| r427 | `correctly` | 無 | 是 |
| r428 | `correctly` | 無 | 是 |
| r429 | `correctly` | 無 | 是 |

被刪詞元集合 ⊆ `{correctly, normally, properly, successfully}`，六列皆成立。

> **本項的過程缺陷（我方）**：首次比對用 `str.count` 做子字串計數，把 `correctly`
> 之刪除誤報為連帶刪掉 `or`，六列全部誤判 FAIL。改為詞元多重集合比對後全過。
> **這與 A-PJ38（`inspect` 命中 `Car Inspector`）同型** —— 又一次子字串當詞元用。

## D-2｜凍結欄逐列雜湊

- 凍結欄 **34**（36 欄扣除 I、K），比對列 **559**，不符 **0**
- 其餘 **8 分頁**全表雜湊：`TestProgress` / `Cover_old` / `ChangeHistory_old` /
  `QS Suggestion` / `下拉選單` / `Reference` / `BugList` / `Test Case Framework`
  —— 皆未觸及（本輪未寫回 xlsx，雜湊記錄於 `dryrun_v2.json`）

**兩項授權例外逐列**

| 例外 | 列 | 依據 |
|---|---|---|
| `Expected Result` 窄口 | r424, r425, r426, r427, r428, r429 | R-P12 |
| `Test Case Author` 待補 | **41 列空白，待補 40 列**（r562 為追溯列不補） | R-P19 / R-P54 |

實測 `Test Case Author` 欄（**c26**，非先前假設之 c35）空白 **41** 列，與 R-P54
「Phase 0 記錄之 41 為含 r562 之計數」完全吻合，待補數 **40** 得證。

## D-3｜列數與列序

| 項 | 值 |
|---|---|
| 分支 | **A** |
| 刪除 | r562（唯一） |
| 559 → | 558 |
| 補列 | 7 |
| 最終列數 | **565** |
| 末列 | **r568** |
| 被移動列 | **0**（逐列 index-to-index 比對 `Requirement or Design ID`） |

## D-4｜補列（7 條）

| # | leaf | Test Group | Test Set | Priority | 型態 |
|---|---|---|---|---|---|
| 1 | SWE1-PROJ-133 | WiFi | Disconnection | P1 | 完整 TC |
| 2 | SWE1-PROJ-167-001 | Device Manager | Device Manager | P1 | 完整 TC |
| 3 | SWE1-PROJ-167-002 | Device Manager | Device Manager | P1 | 完整 TC |
| 4 | SWE1-PROJ-184 | Audio Management | Projection Audio | P1 | 完整 TC |
| 5 | SWE1-PROJ-190 | GPS | Cluster Navigation | P3 | **BLOCKED 佔位** |
| 6 | SWE1-PROJ-195 | GPS | Cluster Navigation | P3 | **BLOCKED 佔位** |
| 7 | SWE1-PROJ-227 | Carplay Wired and Wireless | Projection Apps | P2 | 完整 TC |

全欄內容見 `features/projection/batches/append_uncovered_leaves.json`。
`Test Case Author = PeiPYHsu`、`tc_ref_id = NEW`、既有列未重新編號。

**兩條 BLOCKED 佔位之理由（A-PJ54）**：190 與 195 之 037 Verification Criteria
逐字為 `Invalid demand, only need to display TBT` 與 `Mobile phone behavior does
not require development.` —— **來源明確地說「沒有東西可驗」**，非資料不足。
依 O-4 不編造，三欄寫 `BLOCKED - see Remarks`，`Remarks` 載明逐字原文。
不補列會違反 R-P14 之 every-leaf-gets-a-row；照字面編 TC 會違反 O-4；
BLOCKED 佔位同時滿足兩者。

**`SWE1-PROJ-184` 之可寫性**：037 寫 `[TGW_USB1_Sel]`，`TELEMATIC_FD_4.CurrentSource`
之 `VAL_` 實含 `19 = TGW_USB1_Selected`。依 R-P15 以 DBC 拼法為準，該列可寫定
數值與標籤。

**`SWE1-PROJ-133` 之設計選擇（須知悉）**：037 描述「無 ByeBye 之斷線」但**未指定
如何造成**。原稿寫 `A method to suppress the ByeBye message`，該句命中 A-PJ50
新增之 L-PJ9 樣式。改以「將手機關機使無線鏈路直接中斷」實現 —— 具體、不需工具，
但**此實現手段是我方的測試設計選擇，非來源逐字**，已於 `Remarks` 標明。

## D-5｜阻塞列 ↔ 編號

- 不重複列 **75**，無編號可指 **0**
- 本輪新增 r177 / r188 → R-P56、DR#13
- 逐列對照見 `features/projection/data/d5_blocked_rows.json`

首次執行時之「群組加總 86 vs 不重複 73」重疊差額 13 維持不變，本輪新增 2 列
使不重複數為 **75**。

## D-6｜補列之獨立驗證

7 條逐條驗，有誤 **0**。

| 驗證項 | 結果 |
|---|---|
| `Requirement or Design ID` 存在於 037 CPAA_0521 | 7/7 |
| `Priority` ∈ {P0, P1, P2, P3} | 7/7 |
| `Design Method` ∈ 下拉選單 9 值 | 7/7 |
| `Test Group` ∈ 既有 10 值 | 7/7 |
| `Test Set` ∈ 既有 18 值 | 7/7 |
| `Specification Reference` 錨點格式與可解析性 | 7/7 |
| Procedure ↔ ER 行數 1:1（L-PJ8） | 5/5（BLOCKED 兩條不適用） |
| L-PJ1 ~ L-PJ10 | 5/5 全綠 |

步數對齊：133 為 4/4，167-001／167-002／184／227 皆為 3/3。

## D-7｜`er_divergence.json` 內容時效

35 列中 **29 列**之 `proc_excerpt` 更新為修訂後內容；其餘 6 列之 Procedure
本輪未變更，內容仍為現況。

- 更新列：r151, r152, r167–r190（24 列連續）, r235, r270, r271
- 修訂前原文保留於新欄 `proc_excerpt_prerefine`，**未覆寫即丟棄**
- `er_excerpt` 全數維持（ER 凍結）
- 更新前後對照見 `features/projection/data/d7_proc_excerpt_diff.json`

## D-8｜`data/` artifact 時效標記

清單見 `features/projection/data/d8_artifact_manifest.json`。

| 類別 | 份數 | 檔 |
|---|---|---|
| `pre-refine`（快照，不更新） | 2 | `recon.json`, `pcts_evidence.json` |
| `analysis`（分析產物，凍結） | 5 | `protocol_axis`, `sub_x_testset`, `layer2_x_layer3`, `layer2_isomorphism`, `layer3_gate` |
| `source-index`（來源索引，與修訂無關） | 4 | `cfts085_sections`, `huig_sections`, `sysad_sections`, `carplay_addendum_sections` |
| `must-sync`（已更新） | 3 | `er_divergence`, `er_narrow_gate.log`, `d5_blocked_rows` |
| `stable`（欄位凍結，無需同步） | 1 | `testgroup_matrix`（Test Group × Test Set 皆為凍結欄） |
| `mixed`（拆欄處理） | 1 | `signal_map` |
| **合計** | **16** | |

> **數字差異（不自行調和）**：下放包 D-8 寫「13 份 artifact 逐份標記」，
> `data/` 實有 **16** 份 JSON（另有 `pcts_ui/` 截圖目錄）。本輪產出之
> `dryrun_v2.json` / `d7_proc_excerpt_diff.json` / `d8_artifact_manifest.json` /
> `lpj1_resolution.json` 未計入。**16 為實測值，13 之組成不明。**

**`signal_map.json` 之 `workbook_rows`（A-PJ55）** —— D-8 要求歸類其語意，查核
時發現該欄有兩個問題，第二個先前未被察覺：

1. 語意混用（包內已指出）
2. **掃描範圍未載明**（新發現）：`$VC_Veh_Brand$` 記 12，以可編輯三欄量測得 3，
   以六個文字欄量測得 15（= 12 + 3，兩種拼法之聯集）。**原值採全六欄且僅計
   主拼法**，兩個條件皆未寫在檔內。

處置：拆為三欄，**範圍寫進欄名**，原欄移除。

| token | `_prerefine_scanrisk` | `_postrefine_scanrisk` |
|---|---|---|
| `$Day_Night_Mode$` | 22 | 22 |
| `$VC_Veh_Brand$` | 15 | 14 |
| `$VC_Veh_Line$` | 19 | 18 |
| `$HUModeStatus$` | 4 | 4 |
| `$FuelLvlLow$` | 2 | 2 |
| `$Screen_Size$` | 3 | 2 |
| `$HCP_DISP2.Est_Range_BEV$` | 2 | 2 |

`$Day_Night_Mode$` 修訂前後皆為 22：B2 雖把 Procedure 內的 token 換成具名 CAN
訊號，該 token 仍存在於 `Test Item` 與 `Expected Result`（凍結欄）。
**token 消失於可編輯欄不等於消失於全簿。**

## D-9｜`Test Case Framework` 分頁

- 分頁存在，**維度 `A1:A1`，非空儲存格 0** —— 完全空白
- 未寫入（`fill_test_group_set: false`）
- 雜湊 `e3b0c44298fc...`（空字串之雜湊），已含於 D-2 之 8 分頁比對

**回報不修改**：該分頁與 framework Part V 之 Layer 1／Layer 2 無從比對 ——
它沒有內容可比。若原意是該分頁應載有框架，則這是一個**空表**而非不一致；
欄位凍結，本輪不寫入。

## D-10｜八項全簿基線

| Gate | 期望 | 既有列（4–561） | 含補列 | 位移 |
|---|---|---|---|---|
| L-PJ5 禁詞 | 1 | **1** | 1 | 無 |
| L-PJ6 模糊語 | 4 | **4** | 4 | 無 |
| L-PJ9 泛稱工具 | 17 | **17** | 17 | 無 |
| L-PJ10 缺陷類 | 5 | **5** | 5 | 無 |
| L-PJ10 參數類 | 8 | **8** | 8 | 無 |
| 步驟交叉指涉 | 30 | **30** | 30 | 無 |
| 步數 != ER 例外 | 3 | **3** | 3 | 無 |
| 前向循環指涉 | 0 | **0** | 0 | 無 |

**八項全數精確命中，補列納入後無一項位移** —— 依 R-P56「基線變動須有裁決」，
本輪無需裁決。

### R-P41 掃描條件揭露

| 項 | 條件 |
|---|---|
| 列範圍 | 實體列 4–561（558 列）。r562 為追溯列，分支 A 將刪除，不計入基線 |
| L-PJ5 | 範圍 I + K；**計數單位＝次**；詞界 `\b` + `re.I` |
| L-PJ6 | 範圍 I + K + L；**計數單位＝次**（r520 一列命中兩次）；詞界 + `re.I` |
| L-PJ9 | **計數單位＝列**；條件為「PRE 命中泛稱樣式」且「PROC 無具名工具路徑」兩者同時成立 |
| L-PJ10 | 範圍 **I + K + L**；**計數單位＝列**；參數類以列舉白名單排除，不以樣式推斷 |
| 步驟交叉指涉 | 範圍 K；**計數單位＝列**；`\bsteps?\s+\d+` + `re.I` |
| 步數 != ER | 範圍 K vs L；僅比對兩邊皆有編號步驟之列 |
| 前向循環指涉 | 範圍 K；被指涉步號 > 當前步號 |
| L-PJ1 | 範圍 `SCAN_RISK` 六個文字欄；先移除 `$...$`；豁免清單 3 項 |
| `CAN` 字樣 | **大小寫敏感**（A-PJ37：`re.I` 會命中英文助動詞 can） |

**L-PJ10 之掃描範圍必須含 ER**：參數類 8 列中 r60／r61 之 `<Device Name>` 只
出現在 `Expected Result`，只掃可編輯兩欄會得到 6。

> **本項的過程缺陷（我方）**：首次量測 L-PJ10 以「次」計且只掃 I + K，得
> 缺陷類 5／參數類 6，誤判 FAIL。改為以「列」計且含 ER 後，兩類同時命中 5／8。
> **同一個 gate 的兩類用了同一個單位假設，其中一類是錯的。**

---

## 我方過程缺陷彙整

本輪 dry-run 首跑 FAIL 兩項、次跑 FAIL 兩項，**四項全部是驗證腳本自身的缺陷，
無一項是工作簿或修訂內容的缺陷**：

| # | 缺陷 | 症狀 | 同型前例 |
|---|---|---|---|
| 1 | 批次欄位為 `{before, after, changed}` 巢狀結構，被當字串套用 | 63/63 列虛假變更；基線退回修訂前值 | 新型 |
| 2 | `Test Case Author` 欄位置假設為 c35，實為 c26 | 待補列數 532 vs 41 | 新型 |
| 3 | 窄口 diff 用 `str.count` 做子字串計數 | `correctly` 之刪除被誤報連帶刪 `or`，6 列全誤判 | **A-PJ38** |
| 4 | L-PJ10 計數單位與掃描範圍雙重假設錯誤 | 參數類 6 vs 8 | **A-PJ27**（單位）+ **A-PJ19/30/37**（範圍） |

第 3、4 項是既有 anomaly 的同型再現。**`lint_defs` 收編了「比較條件」，但沒有
收編「量測條件」** —— 計數單位、掃描範圍、欄位索引三者仍分散在各腳本裡，
每寫一支就重新假設一次。R-P49 解決了前者，後者仍是開放缺口（見下方第 8 項）。

---

---

## 上繳第 8 項｜本包是否仍有該驗而未驗者（執行層獨立判斷）

前輪此項提出的五點全數成立並成為 D-6 ~ D-10。本輪提出六點，依嚴重度排序。

### N-1｜D-2 之「8 分頁雜湊不變」在 dry-run 階段是同義反覆，且與 Phase 7 相衝突

**最重要的一項。**

`TestProgress` 分頁含 **99 個公式參照 `TestResults`**，範圍為
`TestResults!$F$4:$F$597` 與 `$AD$4:$AD$597`（另有一處 `$F$4:$F$2566`）。

兩個後果：

1. **好消息**：補列落在 r562–r568，仍在 `$597` 範圍內，統計會自動涵蓋，
   不需改公式。
2. **問題**：一旦 Phase 7 真的寫回，`TestProgress` 的**計算值必然改變**
   （分母由 559 變 565、`Test Group` 計數改變）。D-2 要求「8 分頁雜湊不變」，
   而 `TestProgress` 的值雜湊**注定會變**。

我這輪用 `data_only=True` 讀取（取快取值），且根本沒開寫入，所以雜湊當然不變
—— **這一項 PASS 得沒有意義**。

**判斷**：D-2 的「雜湊」需區分**公式雜湊**與**值雜湊**。應驗的是公式雜湊不變
（分頁邏輯未被動到），值雜湊改變是寫回的正確後果而非缺陷。此區分須在
Phase 7 下放前定明，否則寫回當天必然撞上一個假 FAIL。

延伸：`openpyxl` 寫回時對公式與快取值的處理需先驗證 —— 以 `data_only=True`
載入再儲存會**把全簿公式替換成當時的快取值**，那是不可逆的破壞。Phase 7 的
寫回路徑必須用 `data_only=False`，且此點目前無任何檢查項涵蓋。

### N-2｜量測條件未被 `lint_defs` 收編，R-P49 只解決了一半

本輪 dry-run 四次 FAIL **全部是驗證腳本自身的缺陷**（見上節），其中兩項是既有
anomaly 的同型再現。原因不是不小心：

`lint_defs` 收編了**比較條件**（regex、詞界、大小寫），但**量測條件**——
計數單位（次／列）、掃描範圍（哪些欄）、欄位索引（`Test Case Author` 是 c26
還是 c35）——**仍分散在各腳本裡，每寫一支就重新假設一次**。

`RE_SIGREF` 是最尖銳的例子：解析式（`resolve_signal`）在 `lint_defs` 裡，
抽取式卻不在。R-P57 把解析式修對了，但抽取式在三支腳本裡有三種寫法，其中
兩種抽不到 PROXI 的完整形式，**修正因此完全不生效**。這不是實作瑕疵，是
R-P49 那句話的直接推論：**條件正確但實作在多處，等於沒有修**。

**判斷**：`lint_defs` 應增設每個 gate 的量測規格（單位、範圍、欄索引），
與比較式並列為單一事實來源。這是規則變更，我不自行實施，提請裁決。

### N-3｜BLOCKED 佔位列進入工作簿後會污染統計，且覆蓋率語意未定義（A-PJ54 待裁）

190／195 兩條 BLOCKED 佔位列一旦寫回，`TestProgress` 會把它們算進分母，
但它們**永遠不會有測試結果**。覆蓋率、通過率都會被稀釋。

執行層認為應計入「已處置」而不計入「已驗證」，但**本專案尚未定義這個二分**，
工作簿也沒有可承載它的欄位（`Test Result` 的值域未含「不適用」）。

**判斷**：這是 A-PJ54 待裁的實質內容。在裁決之前，補列已產出但 Phase 7 是否
寫回這兩條，應由分析層決定。

### N-4｜補列的 `No.#` 與 `Test Case ID` 編號規則未定義

補列填了 `seq = 559…565`，但：

- `Test Case ID`（c5）我**留空**。既有 558 列中 555 個相異值，命名為
  `NR1L-PROJ-nnn`，最大到 `NR1L-PROJ-540` 附近，且**已知有 2 個重複值**
  （`NR1L-PROJ-415`、`NR1L-PROJ-540`）加 1 個空值。
- 續編規則（接最大號？補空洞？重複值怎麼辦？）**沒有任何來源定義**。

依 O-4 不編造，故留空並在此提出。**判斷**：需要一條編號規則，否則 Phase 7
寫回時只能留空，而留空會使補列在 `Test Case ID` 上不可追溯。

### N-5｜D-3 的「列序不變」原本驗不出同 leaf 內的重排（已自行修正，但條件應入檢查表）

`Requirement or Design ID`（c4）558 列**僅 163 個相異值** —— 用它當列身分，
同一 leaf 底下的列互換偵測不到。已改用 `No.#`（c2，連號且唯一）並加註。

**判斷**：D-3 只寫「逐列 index-to-index 比對」而未指定**用哪一欄當身分**。
檢查表應寫明必須用唯一鍵。這與 canon §5a 第四條（須言明掃描範圍）同型 ——
比對也要言明比對鍵。

### N-6｜`Test Case Framework` 分頁是空表，D-9 的設計前提不成立

D-9 假設該分頁「有內容、可能與 framework Part V 不一致」。實測維度 `A1:A1`、
非空格 0 —— **它是空的**。

**判斷**：D-9 在本專案退化為「確認它仍是空的」。若原意是該分頁應載有
Layer 1／Layer 2 框架，那是一件**待辦事項**而非一致性問題，且
`fill_test_group_set: false` 明文不寫入。兩種讀法差很多，提請確認哪一種
是本意。

---

## 本輪未觸及者

- **未寫回 xlsx**（Phase 7 另行下放）
- **未執行任何 git 操作**
- **未修改任何既有 TC** —— 本輪只新增補列，既有 63 列之修訂沿用前批次結果
- **未修改來源原檔**
