# Audio Management — 下放包 03：Batch B1 生產指令

- Feature slug：`audio_mgmt`
- 日期：2026-08-26
- 裁定：Pei「1採 2採 B1准」（framework 已 LOCKED）
- 批次：B1 = Source Transition 全 34 葉 ＋ Audio Arbitration 前 16 葉，共 50 葉
- 執行層：Claude Code。本包為分析層下放；執行層機械套用，不自行裁量，
  查無之值一律 `PENDING: DR-{n}`（IN §8.4.3），禁止推斷。

---

## 一、前置（Pei 手動一次，執行層開工前確認存在）

將以下來源置入 `features/audio_mgmt/inputs/`（Git 操作與檔案放置屬 Pei）：
1. `SWE_1_Audio_Management_Pending_For_Review.xlsx`（需求主源）
2. `CFTS019AudioManagementPart1_released_20260415.xlsx`（錨源，R-AM2）
3. `CFTS_019_Part2_All_AcceptedExceptDTCrework.xlsx`（錨源，R-AM2）
4. `R1LR_Atl-H_..._CFTS_019_Audio_Management_20250910_1235.pdf`
   （注意：實為純文字，非 PDF；供章節上下文查閱）

執行層開工第一步：`list_directory` 確認四件在位；缺件即停，回報分析層。

## 二、工作簿（R-AM3）

- 依 R-G1 模板以 `scripts/new_feature.py` 產 scaffold；新簿空白起建。
- 既存 `SWQT_AudioAACP` 舊簿（50 條 NR1L_AudioMgnt_*）**不開啟、不續寫、不回修**。
- Test Group 欄一律 `Audio Management`；Test Set 依 §四表。
- TC ID：generator 依 IN §10.3 `{project}-AMM-{NNN}` 指派，project token
  循 repo 既有慣例；LLM 不產 tc_id。

## 三、內容規則（引用式，IN 為準；R-G13 引用替代抄錄）

1. English only（IN §1；新 feature 不得援引雙語例外）。
2. test_item 兩段式（IN §4.3.1 R-S4）：
   - 上半 verbatim 取 **SWE.1 之 Requirement Description**（≤50 token，
     超限摘句並以 specification_reference 指回）；
   - 下半 `(...)` 測試目的獨立成行；同 Requirement ID 多列括號內容不得逐字相同。
3. `Requirement or Design ID` 欄照抄 `SWE1_AMM_{NNN}` 底線式（R-AM7）。
   SWE1_AMM_076 不在 B1；B3 遇之依 R-AM6。
4. specification_reference：一 ID 一行、前綴逐行 `CFTS019-{ObjectID}`
   （IN §10.7），值取 §四表「CFTS 錨」欄；**執行層不得自行改錨**，
   認為錨有誤者記入 reasoning 回報，不改值。
5. 訊號寫法：IN §8.7.5 v3 全域預設（audio_mgmt 無 override）。
   `$MESSAGE.Signal$ = raw (label)`，label 逐字取 DBC `VAL_`（forms/ 查表）；
   CFTS 原文之 `$HUModeStatus$`、`$INFO1Active$`、`$INFO2Active$`、
   `$INFO1Type$`、`$SOSCallType$` 等如 DBC 查得 MESSAGE 歸屬則補全名，
   查無者依 (g)（R-13）保留原文名，DBC 缺漏登記 DR，不代換近似訊號。
6. 時序參數：`<Tent Ramp Up>` 等以 CFTS019-4867766~4867769 之 25–50ms
   實值入 TC（spec-sourced，IN §8.7.1）；其餘 `<...>` 參數查無實值者
   `PENDING: DR-{n} <parameter name> value not defined in available sources`。
7. Priority 依 §12 rubric：本批多屬音訊仲裁核心與轉換時序，P0/P1 為主。
8. 其餘：尾句號禁令、`"..."` 引號、ER 無情態動詞、Final Step 驗證主權、
   §9 自檢全項——依 IN，不重抄。

## 四、B1 葉清單與錨定（分析層已逐條語意核驗；R-AM2 產出）

對位方法揭露：全域單調序列對位（SWE.1 文序 × CFTS 文序）＋分析層逐條
語意核驗；SWE1_AMM_275–278 之 DP 誤配已人工改錨至 1.5.4 Variables。
DR-AM1（正式對照表）仍未結，回件後末站統一校驗回填。

| SWE ID | Source ID | Title | Test Set | CFTS 錨 | 核驗 |
|---|---|---|---|---|---|
| SWE1_AMM_132 | SYS-RA-AMM-359 | Active Media Operation Cancellation | Source Transition | CFTS019-4866468 | 語意核驗通過 |
| SWE1_AMM_133 | SYS-RA-AMM-360 | Entertainment Audio Ramp-Down | Source Transition | CFTS019-4866469 | 語意核驗通過 |
| SWE1_AMM_134 | SYS-RA-AMM-361 | Entertainment Source Activation | Source Transition | CFTS019-4866470 | 語意核驗通過 |
| SWE1_AMM_135 | SYS-RA-AMM-362 | Entertainment Mute Hold Timing | Source Transition | CFTS019-4866471 | 語意核驗通過 |
| SWE1_AMM_136 | SYS-RA-AMM-363 | Entertainment Source Status Update | Source Transition | CFTS019-4866472 | 語意核驗通過 |
| SWE1_AMM_137 | SYS-RA-AMM-364 | Entertainment Audio Ramp-Up | Source Transition | CFTS019-4866477 | 語意核驗通過 |
| SWE1_AMM_138 | SYS-RA-AMM-365 | Entertainment Source Transition Timing | Source Transition | CFTS019-4866479 | 語意核驗通過 |
| SWE1_AMM_142 | SYS-RA-AMM-374 | Entertainment Media Pause Handling | Source Transition | CFTS019-4866492 | 語意核驗通過 |
| SWE1_AMM_143 | SYS-RA-AMM-375 | Active Media Function Cancellation | Source Transition | CFTS019-4866493 | 語意核驗通過 |
| SWE1_AMM_144 | SYS-RA-AMM-376 | Entertainment Audio Ramp-Down During Deactivation | Source Transition | CFTS019-4866494 | 語意核驗通過 |
| SWE1_AMM_154 | SYS-RA-AMM-390 | Information Audio Ramp-Up | Source Transition | CFTS019-4866512 | 語意核驗通過 |
| SWE1_AMM_156 | SYS-RA-AMM-397 | Entertainment to Information Transition Timing | Source Transition | CFTS019-4866520 | 語意核驗通過 |
| SWE1_AMM_157 | SYS-RA-AMM-398 | Information 1 to Information 2 Transition Timing | Source Transition | CFTS019-4866522 | 語意核驗通過 |
| SWE1_AMM_159 | SYS-RA-AMM-402 | Information Source Ramp-Down | Source Transition | CFTS019-4866528 | 語意核驗通過 |
| SWE1_AMM_169 | SYS-RA-AMM-453 | Signal Source Ramp-Up | Source Transition | CFTS019-4866603 | 語意核驗通過 |
| SWE1_AMM_200 | SYS-RA-AMM-530 | Non-Arbitrated Source Transition | Source Transition | CFTS019-4866839 | 語意核驗通過 |
| SWE1_AMM_201 | SYS-RA-AMM-532 | Initial Audio Ramp-Up | Source Transition | CFTS019-4866842 | 語意核驗通過 |
| SWE1_AMM_203 | SYS-RA-AMM-534 | Source Ramp Down on Deactivation | Source Transition | CFTS019-4866844 | 語意核驗通過 |
| SWE1_AMM_205 | SYS-RA-AMM-537 | Entertainment-to-Entertainment Source Transition | Source Transition | CFTS019-4866850 | 語意核驗通過 |
| SWE1_AMM_206 | SYS-RA-AMM-539 | Entertainment Source Ramp Down Before Switching | Source Transition | CFTS019-4866853 | 語意核驗通過 |
| SWE1_AMM_208 | SYS-RA-AMM-541 | Entertainment Source Transition Delay | Source Transition | CFTS019-4866855 | 語意核驗通過 |
| SWE1_AMM_209 | SYS-RA-AMM-542 | Entertainment Source Ramp Up After Transition | Source Transition | CFTS019-4866856 | 語意核驗通過 |
| SWE1_AMM_212 | SYS-RA-AMM-549 | Entertainment Source Activation | Source Transition | CFTS019-4866874 | 語意核驗通過 |
| SWE1_AMM_213 | SYS-RA-AMM-550 | TA/PTY31 Source Activation | Source Transition | CFTS019-4866875 | 語意核驗通過 |
| SWE1_AMM_216 | SYS-RA-AMM-553 | Entertainment Source Deactivation | Source Transition | CFTS019-4866880 | 語意核驗通過 |
| SWE1_AMM_223 | SYS-RA-AMM-565 | Passenger Side Entertainment Activation After Inform | Source Transition | CFTS019-4866895 | 語意核驗通過 |
| SWE1_AMM_224 | SYS-RA-AMM-568 | Information Source Transition | Source Transition | CFTS019-4866898 | 語意核驗通過 |
| SWE1_AMM_225 | SYS-RA-AMM-570 | Restore Entertainment After Information Source Ends | Source Transition | CFTS019-4866900 | 語意核驗通過 |
| SWE1_AMM_240 | SYS-RA-AMM-614 | Arbitrated Signal Source Transition | Source Transition | CFTS019-4866956 | 語意核驗通過 |
| SWE1_AMM_241 | SYS-RA-AMM-616 | Arbitrated Information Source Transition | Source Transition | CFTS019-4866967 | 語意核驗通過 |
| SWE1_AMM_275 | SYS-RA-AMM-840 | Entertainment Ramp-Up Timing | Source Transition | CFTS019-4867766 | 人工改錨（1.5.4 Variables） |
| SWE1_AMM_276 | SYS-RA-AMM-841 | Entertainment Ramp-Down Timing | Source Transition | CFTS019-4867767 | 人工改錨（1.5.4 Variables） |
| SWE1_AMM_277 | SYS-RA-AMM-842 | Information Source Ramp-Up Timing | Source Transition | CFTS019-4867768 | 人工改錨（1.5.4 Variables） |
| SWE1_AMM_278 | SYS-RA-AMM-843 | Information Source Ramp-Down Timing | Source Transition | CFTS019-4867769 | 人工改錨（1.5.4 Variables） |
| SWE1_AMM_123 | SYS-RA-AMM-345 | Signal Source Priority Selection | Audio Arbitration | CFTS019-4866451 | 語意核驗通過 |
| SWE1_AMM_124 | SYS-RA-AMM-346 | Higher Priority Source Arbitration | Audio Arbitration | CFTS019-4866452 | 語意核驗通過 |
| SWE1_AMM_129 | SYS-RA-AMM-351 | Deferred Source Activation | Audio Arbitration | CFTS019-4866457 | 語意核驗通過 |
| SWE1_AMM_130 | SYS-RA-AMM-356 | Audio Source Queue Management | Audio Arbitration | CFTS019-4866465 | 語意核驗通過 |
| SWE1_AMM_139 | SYS-RA-AMM-370 | Audio Request Queue Management | Audio Arbitration | CFTS019-4866488 | 語意核驗通過 |
| SWE1_AMM_166 | SYS-RA-AMM-411 | Next Priority Source Activation | Audio Arbitration | CFTS019-4866538 | 語意核驗通過 |
| SWE1_AMM_167 | SYS-RA-AMM-443 | Next Priority Source Re-Mix | Audio Arbitration | CFTS019-4866590 | 語意核驗通過 |
| SWE1_AMM_189 | SYS-RA-AMM-513 | TBM Priority-Based Source Muting | Audio Arbitration | CFTS019-4866715 | 語意核驗通過 |
| SWE1_AMM_198 | SYS-RA-AMM-523 | SOS Call Audio Priority Handling | Audio Arbitration | CFTS019-4866726 | 語意核驗通過 |
| SWE1_AMM_199 | SYS-RA-AMM-524 | Restore Audio After SOS Call | Audio Arbitration | CFTS019-4866727 | 語意核驗通過 |
| SWE1_AMM_211 | SYS-RA-AMM-548 | Source Activation Conditions | Audio Arbitration | CFTS019-4866873 | 語意核驗通過 |
| SWE1_AMM_215 | SYS-RA-AMM-552 | Source Activation Arbitration | Audio Arbitration | CFTS019-4866879 | 語意核驗通過 |
| SWE1_AMM_218 | SYS-RA-AMM-555 | SOS Call Priority Mute | Audio Arbitration | CFTS019-4866885 | 語意核驗通過 |
| SWE1_AMM_219 | SYS-RA-AMM-556 | Restore Audio After SOS Call | Audio Arbitration | CFTS019-4866886 | 語意核驗通過 |
| SWE1_AMM_226 | SYS-RA-AMM-572 | Cancel TA/Navigation During Phone or VR Request | Audio Arbitration | CFTS019-4866902 | 語意核驗通過 |
| SWE1_AMM_227 | SYS-RA-AMM-573 | Cancel TA on Incoming Call | Audio Arbitration | CFTS019-4866903 | 語意核驗通過 |

## 五、sibling 提示（prompt builder 注入 `## Sibling Rows` 用）

- Source Transition 內三個轉換家族互為 sibling 軸（IN §8.3 之 state/trigger 軸）：
  Ent→Ent（205–209, 212）、Ent→Info（156, 224）、Info1→Info2（157, 241）；
  132–138 與 142–144 為同章節之啟動/停用序列 sibling。
- 198/199 與 218/219 為 SOS 靜音/回復之近重複雙組（CFTS 兩處同文）；
  非 duplicate（錨不同物件），tc_title 之 sibling 區分 token 必須可辨。
- 130 與 139 同文異錨（queue 判定於兩子章節重複）；同上處理。
- 275–278 為 Boundary Value 候選（25ms/50ms 界值，IN §12）。

## 六、產出與上繳

- 產出：TC JSON（IN §10.1 十鍵全備）＋寫回新簿；50 葉估產 60–75 TC。
- 上繳包 04 需附：本批 reasoning 彙整、未結 DR 清單（現況見下）、
  §9 自檢通過聲明、lint 報告（lint P 之 profile 注意事項見 IN §8.7.5 末）。
- 上繳檔名 NN 先查 `docs/upstream/` 既有編號防碰撞（NN collision 防範）。

## 七、未結 DR（現況）

| DR | 內容 | 狀態 |
|---|---|---|
| DR-AM1 | SWE1↔CFTS ObjectID 正式對照表缺失；過渡採 R-AM2 內容對位 | 待 Pei 送出 |
| DR-AM2 | SWE1_AMM_076 編號碰撞（-242/-246 同號），請上游改號 | 待 Pei 送出 |
