# Power — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案） | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-P1 ~ R-P8（該包步驟 5 未執行，於 02 包補抄） | A-PW01 ~ A-PW07（同上） | **停於步驟 2：素材台帳 7 份中 3 份雜湊不符（4 項待裁）** |
| 02 | 2026-08-17 | 素材重新定基（rebaseline） | [handoff/02_rebaseline.md](handoff/02_rebaseline.md) | [upstream/02_rebaseline.md](upstream/02_rebaseline.md) | R-P9 ~ R-P14；R-P3 撤回改立 R-P3′ | A-PW07 撤回；A-PW08 ~ A-PW11 | **停於步驟 7：§E leaf 分布重算不符；G6 / G12 亦不符（6 項待裁）** |
| 03 | 2026-08-17 | framework 定版所需輸入（B1/B2/B3 ＋ 四道補閘） | [handoff/03_framework_inputs.md](handoff/03_framework_inputs.md) | [upstream/03_framework_inputs.md](upstream/03_framework_inputs.md) | R-P15 ~ R-P23 | A-PW12 ~ A-PW16；A-PW03/04/05 複驗 | **PASS —— 十一步全完成，§D 十八項無 MISMATCH（8 項待裁）** |
| 04 | 2026-08-17 | framework 定版（Layer 3 全集、R-P16 撤回、SYS3 交叉比對） | [handoff/04_framework_lock.md](handoff/04_framework_lock.md) | [upstream/04_framework_lock.md](upstream/04_framework_lock.md) | R-P24 ~ R-P32；R-P16 撤回 | A-PW17 ~ A-PW20；A-PW05 訂正、A-PW03 加註、A-PW06 複驗 | **PASS —— 十四步全完成，§D 二十二項無 MISMATCH（8 項待裁）** |
| 05 | 2026-08-17 | Test Set 定版與判讀單位訂正 | [handoff/05_testset_lock.md](handoff/05_testset_lock.md) | [upstream/05_testset_lock.md](upstream/05_testset_lock.md) | R-P33 ~ R-P41（**R-P35 §E 定版**、**R-P36 條文不可變**） | A-PW21 ~ A-PW25；A-PW23 框架訂正 | **PASS —— 十二步全完成，G21–G27 無 MISMATCH（8 項待裁）** |
| 06 | 2026-08-17 | 錨點層範圍上界與懸空參照 DR | [handoff/06_scope_boundary.md](handoff/06_scope_boundary.md) | [upstream/06_scope_boundary.md](upstream/06_scope_boundary.md) | R-P42 ~ R-P51（**R-P42 錨點層範圍上界**） | A-PW26 ~ A-PW29 | **PASS —— 十二步全完成，G28–G31 無 MISMATCH；發 DR-PW5/6/7（6 項待裁）** |
| 07 | 2026-08-17 | Phase 4 前置閘門與量測工具強化 | [handoff/07_phase4_gates.md](handoff/07_phase4_gates.md) | [upstream/07_phase4_gates.md](upstream/07_phase4_gates.md) | R-P52 ~ R-P59（**R-P52 R-P42 執行期閘門**） | A-PW30 ~ A-PW32 | **PASS —— 九步全完成，G32–G36 無 MISMATCH；lint 就位（6 項待裁）** |
| 08 | 2026-08-17 | lint 閘門補齊與偽陽性量測 | [handoff/08_lint_parity.md](handoff/08_lint_parity.md) | [upstream/08_lint_parity.md](upstream/08_lint_parity.md) | R-P60 ~ R-P65（**R-P65 Phase 4 開始條件**） | A-PW33 ~ A-PW36 | **PASS —— 九步全完成，G37–G44 無 MISMATCH；lint 五閘就位（7 項待裁）** |
| 09 | 2026-08-17 | 補閘與 **Phase 4 首批** | [handoff/09_phase4_batch1.md](handoff/09_phase4_batch1.md) | [upstream/09_phase4_batch1.md](upstream/09_phase4_batch1.md) | R-P66 ~ R-P72 | A-PW37 ~ A-PW42 | **PASS —— 九步全完成；首批 9 條 TC 產出、真實檔案 lint 全閘 PASS（8 項待裁）** |
| 10 | 2026-08-17 | 欄位對應交叉驗證與首批 pilot 回覆 | [handoff/10_column_verify.md](handoff/10_column_verify.md) | [upstream/10_column_verify.md](upstream/10_column_verify.md) | R-P73 ~ R-P78 | A-PW43 ~ A-PW47 | **PASS —— 九步全完成；A-PW40 經第二來源佐證成立；首批 9→10 條全閘 PASS（8 項待裁）** |
| 11 | 2026-08-17 | 範本全屬性比對與首批全文覆核 | [handoff/11_template_verify.md](handoff/11_template_verify.md) | [upstream/11_template_verify.md](upstream/11_template_verify.md) | R-P79 ~ R-P85 | A-PW48 ~ A-PW52 | **PASS —— 十步全完成；Power DV 座標正確；查出 B 欄無編號公式（8 項待裁）** |
| 12 | 2026-08-17 | pilot 修正與閘門補強 | [handoff/12_pilot_fixes.md](handoff/12_pilot_fixes.md) | [upstream/12_pilot_fixes.md](upstream/12_pilot_fixes.md) | R-P86 ~ R-P95 | A-PW53 ~ A-PW58 | **PASS —— 十二步全完成；`Test Case Framework` 分頁實測為空、不與 §E 衝突；十條四項系統性違規全修；新增 G63–G72，G67 覆蓋率 88%** |
| 13 | 2026-08-17 | ER 品質修正與首批覆核完成 | [handoff/13_er_quality.md](handoff/13_er_quality.md) | [upstream/13_er_quality.md](upstream/13_er_quality.md) | R-P96 ~ R-P100 | A-PW59 ~ A-PW63 | **PASS —— 十步全完成；十條 ER 複述與時間相等表述全修；G73 / G74 具「合成＋真實」證據；**惟 G73 之判準與已交付件衝突，不得為阻斷閘** |
| 14 | 2026-08-17 | Final Step 驗證意圖與首批覆核收尾 | [handoff/14_final_step_intent.md](handoff/14_final_step_intent.md) | [upstream/14_final_step_intent.md](upstream/14_final_step_intent.md) | R-P101 ~ R-P106 | A-PW64 ~ A-PW68 | **PASS —— 十二步全完成；G77 修正前 9/10 FAIL；`006` 確係時序誤讀已改寫；`source_clause` 立為常規（G79）** |
| 15 | 2026-08-17 | 首批覆核收尾與誤讀清除 | [handoff/15_batch1_closeout.md](handoff/15_batch1_closeout.md) | [upstream/15_batch1_closeout.md](upstream/15_batch1_closeout.md) | R-P107 ~ R-P112 | A-PW69 ~ A-PW74 | **PASS —— 十一步全完成；`006` 殘留實為四處（分析層指出一處）；刪除無據之順序斷言；`source_clause` 補為完整原文；Arif 素材備妥待 Pei 裁定 Q3** |
| 16 | 2026-08-17 | 寫回排序規則與 dry-run | [handoff/16_write_order.md](handoff/16_write_order.md) | [upstream/16_write_order.md](upstream/16_write_order.md) | R-P113 ~ R-P117 | A-PW75 ~ A-PW79 | **PASS —— 九步全完成；dry-run 使 G66/G71/G72 升為「合成＋真實」；**DV 五條全數存活（含 x14）**；`SWE-PM-073` 補測五條（4→9）** |
| 17 | 2026-08-18 | 反向涵蓋、寫回路徑閘門與第二批前置 | [handoff/17_reverse_coverage.md](handoff/17_reverse_coverage.md) | [upstream/17_reverse_coverage.md](upstream/17_reverse_coverage.md) | R-P118 ~ R-P124 | A-PW80 ~ A-PW88 | **PASS —— 十一步全完成；反向涵蓋三透鏡（透鏡 1 單獨僅重現 1/3 已知缺口）；G89/G90 刻意弄壞證明全數如期；三項前置全備，第二批可開始** |
| 18 | 2026-08-18 | `source_clause` 保真度與第二批啟動 | [handoff/18_source_fidelity.md](handoff/18_source_fidelity.md) | [upstream/18_source_fidelity.md](upstream/18_source_fidelity.md) | R-P125 ~ R-P132 | A-PW89 ~ A-PW95 | **PASS —— 十一步全完成；G94 11/11 逐字相符；**第二批 8 leaf / 26 條 TC**；透鏡 3 盲測抓出 1 項事前未知之缺口（信噪比 0.7%）** |
| 19 | 2026-08-18 | 第二批覆核與錨點完整性 | [handoff/19_batch2_review.md](handoff/19_batch2_review.md) | [upstream/19_batch2_review.md](upstream/19_batch2_review.md) | R-P133 ~ R-P141 | A-PW96 ~ A-PW102 | **PASS —— 十一步全完成；G99 11/11 相等；**R-P135 三對屬性相異已停並上繳**；R-P133 之剝除使 overlap 降而判定未變（12→12）** |
| 20 | 2026-08-18 | 複述判準訂正與地基再下一層 | [handoff/20_falsifiability.md](handoff/20_falsifiability.md) | [upstream/20_falsifiability.md](upstream/20_falsifiability.md) | R-P142 ~ R-P147 | A-PW103 ~ A-PW111 | **PASS —— 十步全完成；R-P96 判準改為可證偽性；G103 11/11；**19 包之黏連陳述經實測更正為誇大**** |
| 21 | 2026-08-18 | SYS2 `Need rework`、git 禁區釐清、切片規則擴充 | [handoff/21_need_rework.md](handoff/21_need_rework.md) | [upstream/21_need_rework.md](upstream/21_need_rework.md) | R-P148 ~ R-P152 | A-PW121 | **補執行於 23 包（R-P164）—— G107 UNCHANGED、G108 三案如期、DR-PW9 已開；台帳缺口已填，R-P1–R-P160 連續無缺** |
| 22 | 2026-08-18 | 節奏重整、第二批發現與第三批啟動 | [handoff/22_batch3.md](handoff/22_batch3.md) | [upstream/22_batch3.md](upstream/22_batch3.md) | R-P153 ~ R-P160 | A-PW112 ~ A-PW119 | **PASS（範圍縮減）—— 第三批 22 / 32 leaf；**G103 首次真實命中**（`4941984` 不存在）；DR-PW6 阻斷九 leaf；盲測抓出 4 項事前未知缺口** |
| 23 | 2026-08-18 | OR 分支閘門、台帳補洞與第四批 | [handoff/23_or_branch.md](handoff/23_or_branch.md) | [upstream/23_or_branch.md](upstream/23_or_branch.md) | R-P161 ~ R-P168 | A-PW120 ~ A-PW127 | **PASS（第四批未啟動）—— G113 七項驗證僅 2/7 而 §D 期望為全數重現；**G113 現況資料真實命中 2 項**；G114 全量掃出 4 個文字層不存在之 item** |
| 24 | 2026-08-18 | G113 訂正、地基閘門時序與第四批 | [handoff/24_batch4.md](handoff/24_batch4.md) | [upstream/24_batch4.md](upstream/24_batch4.md) | R-P169 ~ R-P176 | A-PW128 ~ A-PW132 | **PASS（一項 MISMATCH）—— G113 五項 OR 實例 **5 / 5** 全數重現；分桶真陽性率 1.9%（前為 3.6%）並前瞻攔下**第十例**；`SWE-PM-025` 之 ECU 正規化後**仍相異**（真集合差 {ETM}），R-P167 不結案；**第四批 25 leaf / 50 條**（R-P174 載 31 leaf，**6 leaf 已於第二批產出** → G119 MISMATCH）|
| 25 | 2026-08-18 | 批次定義訂正、全量對帳與第五批 | [handoff/25_batch5.md](handoff/25_batch5.md) | [upstream/25_batch5.md](upstream/25_batch5.md) | R-P177 ~ R-P182 | A-PW133 ~ A-PW138 | **PASS —— G121 全量對帳 115 / 115，五個 Test Set 全數相符；**R-P178 之推導 6 實測為 10**，根因即 R-P177 所禁者（同包內再犯）；`SWE-PM-025` 觸發訊號原文已上繳（僅第一對含訊號，二、三對逐字相同）；**第五批 29 leaf / 66 條**；G113 真缺口 6 → 2 → 0（補測 9 條）；新開 **DR-PW12**（五對 leaf 共用錨點）|
| 26 | 2026-08-18 | 裁定積案、數字標註機制與末批 | [handoff/26_final_batch.md](handoff/26_final_batch.md) | [upstream/26_final_batch.md](upstream/26_final_batch.md) | R-P183 ~ R-P197 | A-PW139 ~ A-PW142 | **PASS —— Phase 4 產出面完成**：末批 16 leaf / 34 條，最終對帳 103 ＋ 11 ＋ 1 = **115** 相符；**批次四、五之 leaf `reasoning` 54 份補寫完畢**並補設 **G129**（103/103，fixture 四案如期）；G131 測得逗號列舉型缺口 **6 項未補待裁**；G133 重疊對 27；**§J 自檢於執行中失效一次**（§A 由 14 增為 15），已停並回報後以 15 條續行 |
| 27 | 2026-08-18 | 已知缺口補測、下放包凍結與實測訂正 | [handoff/27_gap_closure.md](handoff/27_gap_closure.md) | [upstream/27_gap_closure.md](upstream/27_gap_closure.md) | R-P198 ~ R-P203（**R-P198 為 26 包遺落者，依原編號補入**）| A-PW143 ~ A-PW147（A-PW139 訂正）| **PASS —— 六個已知缺口全數補測**（G134）；**G82 擴充至 `pre_conditions` / `input_test_data`**（G135，fixture 五案如期，現況觸發 25 項待裁）；A-PW139 之 §8.4.2 判定**撤回**（空白變體，經獨立重掃確認）；批次一至三 `reasoning` 重評 —— 第 2 項 **3 / 33 → 33 / 33**，補寫 31 份，**G129 門檻 20 → 130**；tc_id 全域重編 **001–264** |
| 28 | 2026-08-18 | pre_conditions 依據判準與追認 | [handoff/28_precondition_basis.md](handoff/28_precondition_basis.md) | [upstream/28_precondition_basis.md](upstream/28_precondition_basis.md) | R-P204 ~ R-P209 | A-PW148 ~ A-PW151 | **PASS —— G82 之 14 項逐項判定全為 (a) 非越界**，無 TC 需修正；G138 / G139 各以四案 fixture 證明 (a) 不觸發 / (b) 觸發、測試選用值排除而規格閾值仍觸發；**擴充欄觸發 25 → 2**；**批次層閘門分流缺陷之歷史影響經回查為零**（rule 集合交集為空）；R-P203 加註 **G141 UNCHANGED** |
| 29 | 2026-08-18 | 造值判準補洞與 Day_Night_Mode 裁定 | [handoff/29_fabricated_state.md](handoff/29_fabricated_state.md) | [upstream/29_fabricated_state.md](upstream/29_fabricated_state.md) | R-P210 ~ R-P214 | A-PW152 ~ A-PW155 | **PASS —— 264 條 `pre_conditions` 全掃**（G142：(a) 244 / **(b) 20**，逐條載選擇依據與行為是否隨狀態而異）；`SWE-PM-094` 唯一無法說明，標待查並**開 DR-PW14**；**`$Day_Night_Mode$` 判為真陽性，注入已移除**（擴充欄觸發 2 → 0）；**G145 閘門觸發數自動彙整**（批次層四項皆 0）；R-P204 加註 **G144 UNCHANGED** |
| 30 | 2026-08-18 | 台帳重複閘、涵蓋缺口登記與兩項複核 | [handoff/30_ledger_dup.md](handoff/30_ledger_dup.md) | [upstream/30_ledger_dup.md](upstream/30_ledger_dup.md) | R-P215 ~ R-P220 | A-PW156 ~ A-PW159 | **PASS —— G146 台帳重複閘補設**（四項重複皆 0，fixture 五案如期）；**20 項 (b) 型六欄逐項表已附供複核**（R-P217）；`091`/`092` 之涵蓋缺口判 **(b)** 並**開 DR-PW15**（未靜默消失）；G137 之 25/33 與 27 包之 33/33 查明為**口徑不同**（齊備率 vs 單項率），已明載；**R-P220 之重跑比對當場揭出二項產物陳舊** |
| 31 | 2026-08-18 | design_method 分布、分層取樣與陳舊產物全掃 | [handoff/31_design_method.md](handoff/31_design_method.md) | [upstream/31_design_method.md](upstream/31_design_method.md) | R-P221 ~ R-P225 | A-PW160 ~ A-PW164 | **PASS —— T24 成立且遠比推測嚴重**：`design_method` 253/264 = **95.8%** 為狀態轉換，四個 Test Set 各 100%；抽樣 43 走查 **不符 26（60.5%）**，**不逕行改值**；分層取樣備料 **211 條 / leaf 103-103**；產物全掃 66 份 —— **發現第三類「時點相依」，其重跑會摧毀產物**（二檔已還原）|
| 32 | 2026-08-18 | design_method 全數重判與時點相依產物 | [handoff/32_design_method_rejudge.md](handoff/32_design_method_rejudge.md) | [upstream/32_design_method_rejudge.md](upstream/32_design_method_rejudge.md) | R-P226 ~ R-P230 | A-PW165 ~ A-PW169 | **PASS —— 機械提案僅 22.7% 相符**（相異 8、無法判定 196）；**已裁 32、尚未裁 174**（成因為謂詞過窄，放寬對執行層有利故依 R-P187 未自行為之）；**G154 全批觸發 26 條**且三已知實例皆重現；**產物判類 (a) 52 / (b) 4 / (c) 12**，(c) 一律不得重跑；備份機制就緒 |
| 33 | 2026-08-18 | 正向轉換謂詞、050 裁定與不可再生產物 | [handoff/33_positive_predicate.md](handoff/33_positive_predicate.md) | [upstream/33_positive_predicate.md](upstream/33_positive_predicate.md) | R-P231 ~ R-P235 | A-PW170 ~ A-PW175 | **PASS —— `ROW3_RE` 不放寬，改建正向謂詞**：正向確認 81 / 落底第 9 列 173 / 矛盾 2（皆已裁），「機械無法判定」由 196 **降為 0**；`050` 依 R-P232 續判第 3 列**結案**；**(c) 型 12 份寫入保護就位**（fixture 四案）；備份擴至 **133 檔**；**P0 抽樣 38.2% 無法歸類**（Branding 5/5）|
| 34 | 2026-08-18 | 第 4–8 列判定、`priority` 全批重判、腳本自改方式改正 | [handoff/34_row_completion.md](handoff/34_row_completion.md) | [upstream/34_row_completion.md](upstream/34_row_completion.md) | R-P236 ~ R-P241 | A-PW176 ~ A-PW189 | **PASS —— 落底 173 → 85**（第 4 列 80 / 第 8 列 7 / 第 5 列 2；**第 7 列無謂詞，其 0 為「無從判定」**）；`priority` 全量 201 條重判，**93 條不成立**（Branding 提案 P3 **19**，與 33 包抽樣「5/5」不一致 → 抽樣不可推及全體）；**G165 AST 安全編輯器**就位並**發現第二處既存損壞**（`dryrun_write_back.py`，**G108 基線僅 7/59 = 11.9%**）；`SWE-PM-073` Fault Injection **成立**，惟第 2 列謂詞**偽陰性**；R-P241 之 (a) 停止規則與 (c) 前提**實測皆失效** ——首次深挖 `remarks` 3.4% / `split_flag` 4.9%；**七項實質性質無任何機制涵蓋**；**全程不改值**（`generated/` diff 為空）|
| 35 | 2026-08-18 | 人工確認、G108 擴充與謂詞驗證 | [handoff/35_manual_confirm.md](handoff/35_manual_confirm.md) | [upstream/35_manual_confirm.md](upstream/35_manual_confirm.md) | R-P242 ~ R-P247 | A-PW190 ~ A-PW200 | **PASS —— G108 涵蓋 11.9% → 100%**（63/63、728 符號，`WATCHED` 改動態 glob）；第 4 列 80 條逐條確認 → **79 成立 / 1 不成立**，**落底 85 → 86**；**第 7 列之 0 經反向查證實為 first-match 序之結構性結果**（9 對候選、6 對真組合，無一能抵達第 7 列 —— 須分析層裁定是否為死列）；第 2 列反向查**未見新故障注入**，盲區有界；`priority` 謂詞 **13 案自撰 fixture 全數如期**（含二對抗案直擊 v1 缺陷）；**G168 就位**（結構違規 0、C5 觸發 1 組經判為 `delta` 樣板缺陷而非重複 TC）；⚠ **§4.6 契約原文查無、`duplicate_of` 欄不存在** —— 列舉值未擬定；⚠ **「誇大本層發現」型偏誤連續二包各一次**（`COND_RE` 大小寫：37 → 12）；**全程不改值** |
| 36 | 2026-08-18 | axis 列舉值、死列裁定與樣式謂詞通則 | [handoff/36_axis_enum.md](handoff/36_axis_enum.md) | [upstream/36_axis_enum.md](upstream/36_axis_enum.md) | R-P248 ~ R-P252 | A-PW201 ~ A-PW209 | **PASS —— `axis` 現行違規 254 / 264 = 96.2%**（非法值**三種**：`behaviour` 245 / `branch` 6 / `trigger` 3 —— 條文漏列 `branch`）；全批重判提案（`input_data` 92 / `trigger_state` 68 / `mode` 42 / `timing` 17 / `boundary` 5 / **無對應 40**）；**發現 `SWE-PM-025` 二對 TC 四欄逐字全同**（`087`≡`091`、`088`≡`092`）—— **內文未實現其宣稱之觸發區分**，C5 抓不到；**first-match 壓抑實測：第 5 列 90.5%、第 8 列 56.3% 被吸收**，吸收者以第 4 列為主；R-P250 於本包**攔下三次真缺陷**（皆在產出結果前），另攔下二次**執行層未讀即推想之期望值**；既有 **82 個謂詞**回溯稽核（命中 0 者 7、大小寫敏感 9、空白敏感 21）；**G177 修正前 `66/66 exit 0` → 修正後 `63/66 exit 1`**；驗證邊界增列 `design_method` 值域三項；**全程不改值** |
| 37 | 2026-08-18 | 流程矯正與第一級改值 | [handoff/37_first_tier_edit.md](handoff/37_first_tier_edit.md) | [upstream/37_first_tier_edit.md](upstream/37_first_tier_edit.md) | R-P253 ~ R-P258 | A-PW210 ~ A-PW217 | **PASS —— 32 包以來首次改值：第一級 62 處**（`axis` 31 / `split_index` 4 / `split_flag` 9 / `remarks` 8 / `delta` 2 / `SWE-PM-025` 內文 8）；**G179 前後對照：17 閘門 15 個數值全同、新觸發 0**，變動 2 個皆為預期改善（違規 254→227、C5 1→0 組）；**G178 就位並查出跨 leaf 逐字全同 13 組 / 26 條 = 9.8%**（6 組連 title 亦同，列 38 包待裁）；**`GLUED_OR_RE` 之 2→2408 全為單詞字尾誤命中，真 OR 增量 0、返工面 0 條** —— G113 結論不須重估；R-P248 加註漏列 `branch`（原文 SHA256 UNCHANGED）|
| 38 | 2026-08-18 | 第 8 列謂詞訂正與第二級改值 | [handoff/38_second_tier_edit.md](handoff/38_second_tier_edit.md) | [upstream/38_second_tier_edit.md](upstream/38_second_tier_edit.md) | R-P259 ~ R-P264 | A-PW218 ~ A-PW229 | **PASS —— 第二級改值 204 處**：`design_method` 單一值集中度 **95.8% → 34.5%**（91/88/84 近乎均勻，未翻為反向偏向）、`priority` P0 **73.1% → 59.5%**、P3 0 → 40；**第 8 列謂詞改以功能數為判準（7 → 2）** —— 舊謂詞誤取 tie-break 之「≥3 steps」；**乾跑攔下一項回歸**（`…-008` 之明文裁定險被 first-match 覆寫）；**13 條因 §12 標籤缺漏而未改**（第 1/5/6/8 列與矛盾無既有標籤，不自行擬定）；**G154 未漏** —— 缺口在其產出被擱置五包；跨 leaf 重複 13 組判定（(a) 8 / (b) 5），**(a) 之 title 未改**（屬 DR-PW12 待答，改之即代 RD 作答）；G182 17 閘 15 個全同、新觸發 1（G150 人工走查表時點相依）|
| 39 | 2026-08-18 | §12 逐列核對、axis 收尾與反向重複掃描 | [handoff/39_row_audit.md](handoff/39_row_audit.md) | [upstream/39_row_audit.md](upstream/39_row_audit.md) | R-P265 ~ R-P270 | A-PW230 ~ A-PW240 | **PASS —— §12 九列核對：不一致 4 / 9**（第 2、4、6、9 列）—— **R-P259 之同型錯誤確實不只一處**；第 6 列裸詞 `limit` 已訂正改值（6 → 4，落底 90 → 92，**37 包已於他處修過同一缺陷而本檔未同步**）；第 2 列 `timeout` **不予加入**（語料 49 次全為設定名稱，加之得 26 偽陽性 0 真陽性）；第 9 列 catch-all vs `Single feature check` **17 條不符**；**`axis` 40 條依 §10.1 optional 與 §4.6 輸出條件省略該欄**（依據已直接查權威檔逐字確認），C2 訂正 ＋ C8 新增，違規 227 → **187**；第 4 列擴充 **80 → 141**（落底 92 中 59 條應改判，不改值）；**G188 反向掃補上 G178 盲區** —— 查出 DR-PW12 第五對（`056`/`097`）；閘門代表性盤點 8 項，**G162 之結論已對現值失效而報表不顯示**；DR-PW12 增列待答項 ＋ 交付說明驗證邊界增列三項 |

---

## 2. 現況

### framework 已定版

**§E 定版：Power State 63 / Startup Display 24 / Branding and Theme 16 /
Timeout Settings 8 / Power Down 3 = 114**（＋ `SWE-PM-089` 留空 = 115）。
依 **R-P35**；標題已改為「已定版（R-P35）」。
兩條待裁 leaf 已由 **R-P33**（`SWE-PM-008` → Power State）與
**R-P34**（`SWE-PM-057` → Timeout Settings）裁定。
逐 leaf 指派見 `data/leaf_testset.tsv`；驗證 `scripts/build_testsets.py`（G21/G22 PASS）。

Layer 3 全集（R-P24）：`data/layer3_full.tsv`，140 列、46 個相異章節。

### 已完成

- **素材已驗明並就位**（G0 = 7/7，五包一致）。
- **裁決台帳**：`RULINGS.md` 含 **R-P1 ~ R-P41**，編號連續無缺
  （R-P3 撤回改立 R-P3′；R-P16 由 R-P25 撤回）。
  `ANOMALIES.md` 含 **A-PW01 ~ A-PW25**（A-PW07 撤回）。
- **R-P36「裁決條文不可變」已首次適用**（G27 PASS）——
  三處加註，原文 SHA256 完全相同。此後一切訂正走註記。
- **B2 v2 已重做**（R-P38）：判讀單位改為「被引用之錨點 vs leaf」。
  九章 31 個錨點中僅 18 個被引用；**§1.6.2.1.15.1 判定由「部分涵蓋」改為「涵蓋」**。
- **嵌入物件已清點**（R-P39）：CFTS009 **零嵌入物件** ——
  `…inline.rtf WrapperResource` 是**懸空參照**，所指資源未隨文件匯出。
  合計 **31 處 / 16 章**。
- **EE Architecture 已量測**（R-P40）：238 個被引用 item 全帶此欄，
  無一落在兩世代之外；14 個為單世代專屬。
- **可重現腳本**（皆純讀取）：`extract_textlayer.py`、`build_layer3.py`、
  `build_testsets.py`、`build_b1.py`、`build_b2.py`、`build_b3.py`、
  `build_b4_b5.py`、`verify_gates_03.py`、`verify_gates.py`。

### 閃點現況

PASS：G0–G16、G13b、G18、G19、G20、**G21、G22、G23、G27**
已填空：**G24**（31 處懸空參照 / 16 章）、**G25**（EE Architecture 值域）、
**G26**（相異值 = 1 者 3 欄、≥ 100 者 4 欄）
已停止：**G17**（R-P37，自 06 包移除）
已移除：G11（R-P14(b)）、G6（R-P18 拆為 G6a/G6b）

**無 MISMATCH。**

### Phase 4 —— **六批已產出，產出面完成**（**103 leaf / 264 條**）

| 批 | Test Set | leaf | TC | 臨時 tc_id | CFTS |
|---|---|---|---|---|---|
| 1 | `Power Down` | 3 | **17** | 001–017 | 010 |
| 2 | `Timeout Settings` | 8 | **26** | 018–043 | **009（首次）** |
| 3 | `Power State` | 22 | **68** | 044–111 | 009 |
| 4 | `Power State` / `Startup Display` | 25 | **50** | 112–161 | 009 |
| 5 | `Startup Display` / `Power State` | 29 | **69** | 162–230 | 009 |
| 6 | `Branding and Theme` | 16 | **34** | 231–264 | 009 |

**27 包補測 7 條**（`SWE-PM-013` 3、`SWE-PM-103` 3 —— 逗號列舉型缺口；
`SWE-PM-026` 1 —— `Brand_Configuration_2` 之否定側，R-P198），
並依 `scripts/renumber_tc_ids.py` **全域重編 tc_id 為 001–264**（臨時號，R-P113(b)）。

**最終對帳（G126）**：已產出 **103** ＋ 受阻斷 **11** ＋ `SWE-PM-089` 留空 **1** = **115**。
五個 Test Set 之「未產出且未阻斷」全部為 0。

**leaf `reasoning`**：G129 **103 / 103**，門檻經 R-P203 重校為 **130 字**（26 包為 20）。
G137 重評批次一至三之 33 份 —— 「關鍵情境條件」由 **3 / 33** 補至 **33 / 33**。

**寫回仍未開放** —— 26 / 28 / 29 包之阻斷條件均已解除；
30 包之阻斷條件為 **R-P217 之複核結果**（20 項 (b) 型逐項表已附上繳供分析層複核）
與 **R-P216 之處置**（已判 (b) 並開 DR-PW15）。
**現行待裁項見 `RULINGS.md` §待裁** —— 另含 `SWE-PM-064` 之 Timed 判斷（R-P218，裁定於 31 包）。

**台帳完整性**：G146 自 30 包起為常設閘門 —— `RULINGS.md` 條號 220、
`ANOMALIES.md` 列 159、`DATA_REQUESTS.md` 列 15、`docs/INDEX.md` 輪次 30，
**重複皆 0**（無斷點檢查與之併行，不取代）。

**閘門現況**：G129 **103 / 103**（門檻 130）、G137 **25 / 33**（§10.4 四項齊備）——
**二者判準不同，依 R-P209 不得合稱「完整」**。
G138 / G139 為 G82 之欄位別判準（`pre_conditions` 以「是否斷言行為或時序」為準，
`input_test_data` 之測試選用值排除而規格閾值仍觸發）。

**264 條之內容分析層目視者仍為少數**（R-P159 之分層取樣未完整執行，連續七包積欠）。

### 第一批 —— 首批已產出並已修正（**17 條**）

`features/power/generated/batch_001_power_down.json` —— **15 條 TC，3 個 leaf**
（`SWE-PM-071/072/073`，Test Set `Power Down`），臨時 tc_id `001`–`015` 連號
（**`tc_id_status: provisional`**，R-P113(b)）。
16 包依 R-P117 補測五條（`011`–`015`）、17 包依 R-P118(d) 再補二條（`016`/`017`）——
`SWE-PM-073` 由 4 增為 **11**，**leaf 數始終為 3**。

依 §8.2.2 拆分：071→**4**（F1 後 Standby / Bench 再拆）、072→2、073→4。
priority **P0 ×3 / P1 ×5 / P2 ×2**（依測項內容判定，R-P8）。

**12 包四項修正（R-P86 ~ R-P89），修正前之違規率**：
`req_id` 加後綴 **10/10**、Procedure↔ER 不符 **10/10**、
環境穩定性前提 **6/10**、`input_test_data` 跨欄重複 **5/10**（A-PW53 / A-PW54）。
現全數修正：`req_id` 去後綴（G69 **10/10**）、proc↔ER 全 1:1、
六條移除環境前提、五條改 `NA`。TC 數與 leaf 數不變（修正非拆分，G70）。
**真實檔案 lint：`exit=0`、阻斷類 PASS、R-P42(b) 0 觸發，0.22 秒。**

**13 包二次修正（R-P96 / R-P97）**：12 包為湊 1:1 而將 procedure 動作複述為 ER，
修正前 G73 tier1 觸發 **7** 條、tier2 **4** 條（含分析層所舉之全部五例，
另發現 `006` / `010` 亦命中）；`001` / `004` 之 ER 寫「time **equals** …Time」，
嚴格執行必然 fail（A-PW60）。現全數修正 —— 複述行改為可觀察結果**或合併該步驟**
（procedure 步數 3–4 降為 **2–3**，G63 之 1:1 仍 10/10，§10.5 未違），
`equals` 改為「到期前不顯示 / 到期後顯示」之行為描述，**未造任何容差值**。

**14 包三度修正（R-P101 / R-P102 / R-P103）**：13 包之合併步驟**剝除了 Final Step 之
驗證意圖**，末步僅剩「Read the TLM display through SplashScreen_Time」——
所讀者為**載體**而非**標的**。G77 對 13 包版實測 **9 / 10 FAIL**，
而 **G63 / G73 / G70 當時全綠**（A-PW64，「閘門覆蓋不等於品質」之直接實例）。
現十條末步皆含 §5.2B 之驗證意圖，14–18 字。

**`006` 確係時序誤讀（A-PW68）**：`4942338` 逐字為「process it ... **while the boot is
still completing**」，而 13 包作「processed **after boot completes**」。
`tc_title` / procedure / ER 三欄與 **leaf `reasoning`（誤讀源頭）**已一併改正。
**該誤讀自 09 包首批產出即存在，歷經兩輪修正與多次 lint 全綠而未被察覺** ——
語義錯誤無任何閘門可及，查出它的是 `source_clause` 原文比對。

**分析層首批覆核進度 8 / 10**（`001`–`007`、`010`）。
**剩 `008` / `009` 兩條**（R-P112）—— 已置於 15 包上繳最前。
R-P98 / R-P105 / R-P112 為現行寫回阻斷條件。

**15 包三項清除**：
（一）**`006` 之誤讀殘留實為四處**（`test_item` / `split_reason` / `expected_result` /
`distinguishing_axis.delta`）—— 分析層指出一處，執行層全欄掃描另查出三處（A-PW69）。
R-P107 所列之十三欄清單**不足以涵蓋 JSON 之實際欄位**，故 G81 改為掃全部欄位（A-PW73）。
（二）**`006` 之 ER 曾斷言處理順序而規格未載** —— `4942338` 完整原文僅二句，
載「as soon as possible」，**未載按注入順序**。依 R-P108 (a) 刪除（A-PW70）。
（三）**`SWE-PM-073` 之 `source_clause` 截斷恰好蓋住 mute / ICS / 故障 / 回復四款** ——
即 `007` / `008` / `010` 之 ER 所斷言者。已補為 `4942354` 完整原文 1,568 字元（A-PW71）。

### 範本全屬性 —— 已比對（R-P79）

10 包已以 Comfort + Privacy 之已交付件佐證 `workbook.columns`（A-PW40 成立）。
11 包再比對 r9 以外之六項屬性：

- **DV：Power 之四條逐條落在自身正確欄位**（`Q` priority、`U–AA` 車型、
  x14 `S` design_method、`AG` Test Result）—— **未沿用 Comfort 座標**
- **公式：Power 0 / Comfort 592 / Privacy 11** ——
  **Power 之 B 欄無自動編號公式**（另二者帶 `IF(ISBLANK($D10),"",ROW()-9)`）。
  寫回時 No.# 欄不會自動填入 → **寫回前唯一須先裁者**
- Power 獨有：多一個 `Test Case Framework` 分頁、合併 `D5:F5`、
  條件式格式 `H10:H145` colorScale
- A-PW52：Power 之 DV 覆蓋不齊（三欄僅 2–4 列）

### A-PW46 之前提有誤（11 包 B2）

Comfort **並未決定填車型欄**：其 profile §3.9 明訂「T–Z 一律留白（Privacy R30-4）」、
`write_back.py` 將 T–Z 列入 `NEVER_WRITE`、baseline 該欄非空數為 0、
全 Comfort 腳本無一呼叫 `.save()`。
**已交付件之 466 個 `1` 非由其管線產生**（A-PW51，來源不明）。
二 feature 之政策實為一致（皆留白）。Power 依 R-P54 / R-P81 維持留白。

### Power profile 已建立（R-P82）

`docs/runtime/profiles/FW036_R1L_Power_Profile.md` ——
Power 原為八個 feature 中唯一無 profile 者（A-PW49）。
G50 之方括號豁免已改為**引用 profile §3.1 / §3.2**，
並以 `PROFILE_PATH.exists()` 為條件；G59 雙向實測。

### 第二批 —— `Timeout Settings` 已完成（18 包）

| 項目 | 值 |
|---|---|
| leaf | **8**（§E 定版值）|
| TC | **26**（臨時 tc_id `018`–`043`）|
| `specification_reference` | **26 / 26 指向 CFTS009** —— **首次跨 CFTS009，路徑全程無異常** |
| G94 保真度 | **8 / 8 逐字相符** |
| lint | `exit=0`；阻斷類 PASS；待裁類 12 項（見 A-PW92）|

**`SWE-PM-057` 之歸屬經實際撰寫檢驗為正確（R-P34 成立），無須停並上繳** ——
其九個錨點原文**全部**述及 `SwitchOff_Timeout_Setting.Req` 與 `Timeout1`；
037 之 Title 雖為 `Proxi Parameter management`，行為確屬 Timeout Settings。

**A-PW92 —— G77 與 G73 之結構性張力**：26 條中 **12 條**觸發 R-P96(a)，
**全為訊號／參數之狀態回讀**。原因非閘門瑕疵，而是**兩條裁決彼此拉扯** ——
R-P101 要求末步指名所檢查者，ER 述及同一標的即抬高 G73 之 overlap（三條達 1.00）。
執行層依 R-P76 全數列待裁並判為偽陽性，**未改動任一閘門、未為降低觸發數而改寫 ER**。

### G113 —— OR 分支涵蓋閘門（23 包，R-P161）

「原文以 OR 並列而 TC 只取其一」已重複七次而無閘門。G113 為其處置。

**驗證條件實測 2 / 7**（§D 期望為全數重現）：

| 實例 | 結果 | 形態 |
|---|---|---|
| 16 包 `BODY OFF-TIMED`、18 包 `Ignition Pre Off` | **重現** | —— |
| 17 包 `greater`、22 包 VR 長按 | **未重現** | **根本不是 OR 結構**（`and if` / `both … and`）|
| 22 包 LTM High ×3 | **未重現** | OR 右運算元以 `( If …` 起首，`IF` 在分隔符集合內 → 運算元被截斷丟棄 |

**首版更為 0 / 7**（定界以反轉字串搜尋，正向詞樣式永不匹配）——
**實作瑕疵，判準未改**，已修正（A-PW124）。
**後三項可由分隔符集合之調整達成重現，執行層依 23 §I 未為之，呈請裁定。**

> **G113 於現況資料首次真實命中 —— 第八、第九例**（A-PW125）：
> `SWE-PM-014`（`4941504`）與 `SWE-PM-018`（`4941548`）之
> 「`Ignition Pre Off` **OR** `Ignition Off`」只取後者。
> **本次係由閘門攔下，非事後由反向涵蓋抓到。** 已補二條，第三批 61 → **63**。

**噪音**：未覆蓋分支 **55**，真陽性 **2**（**3.6%**，A-PW126）；未調整判準降噪。

### 第四批 —— **未啟動**（23 包）

R-P161 明訂 G113 為第四批之前置，而 §D 期望為七項全數重現、實測 2 / 7。
**於此啟動即為「前置未達而照樣前進」**，故停並上繳。

**範圍已備妥**：依 R-P165 逐一比對全部 live DR 之影響面 ——
**Power State 剩餘 31 leaf（`SWE-PM-033`–`063`）不受任何 live DR 影響**。
裁定 G113 之處置後即可啟動。

### G114 —— G103 全量掃描（23 包，R-P162）

115 leaf 全掃：**不相等 2** —— `SWE-PM-008` 缺 `4941425` / `4941430` / `4941433`、
`SWE-PM-010` 缺 `4941984`。**四個 item 於兩份 CFTS 文字層皆無內文段落**
—— 非章節解析失敗，而是 037 → SYS2 所指之 id 在文件裡沒有對應錨點（A-PW120）。

**G94 與 G99 皆會全綠**（二者皆以 layer3 為準）。已併入 **DR-PW11**（1 → **4 item / 2 leaf**），
與 A-PW02 / DR-PW3 三處互相標註（R-P151）。

### 台帳缺口 —— 下放包 21 **已於 23 包補執行**（R-P164）

`docs/handoff/21_need_rework.md` **存在**而 `docs/upstream/21_need_rework.md` **不存在**。
22 包 §前言載其五條裁決（**R-P148 ~ R-P152**）維持有效，
**惟條文未經抄錄**，`RULINGS.md` 自 `R-P147` 直接跳至 `R-P153`。
執行層於 22 包**未代為抄錄**（抄錄會使未執行之 §H 看似已做），僅記明缺口。
**23 包依 R-P164 補執行其 §H 步驟 3–9**，五條依原編號抄入 ——
**`RULINGS.md` 現為 R-P1 – R-P160 連續無缺**（A-PW122）。

補執行之產出：**DR-PW9（High）已開**；**R-P7 加註，G107 UNCHANGED**（388 bytes）；
**`check_edit_integrity.py`（G108）** 三層檢查（語法 / 載入 / **符號**），
以 20 包之實際損壞形態為 fixture —— **語法仍 True 而符號層攔下**；
A-PW02 / DR-PW3 / R-P151 三處交叉指引已加；第二批狀態快照已產。

**惟 G108 不保證「同一步內完成」** —— 何時執行仍靠執行者，紀律加工具而非機制。
**B4 快照之 SHA256 取自 23 包當下，非 21 包當時之值**（22 包已改動第二批），已標明。

其中 **R-P149**（自造損壞不得以 git 修復）與 **R-P150**（切片編輯後須立即語法／載入層檢查）
**為對執行層之直接拘束，22 包已遵行**。

### 第三批 —— Power State 前半，**範圍由 32 縮為 22 leaf**（22 包）

| 項目 | 值 |
|---|---|
| leaf | **22**（`SWE-PM-011`–`032`）|
| TC | **61**（臨時 tc_id `044`–`104`）|
| `specification_reference` | **61 / 61 指向 CFTS009** |
| lint | `exit=0`；阻斷類 PASS；**累計 TC 104、leaf 33** |

**兩項排除，皆有明確依據**：

**（一）`SWE-PM-001`–`009`（9 leaf）—— DR-PW6 停**（A-PW118）。
該九 leaf 即 DR-PW6 之影響面；其阻斷欄逐字為
「§1.6.2.1 之 9 個 leaf 其 TC 之 `specification_reference` 無可引之規格文字」。
於此撰寫將產出 R-P121 所指之「**可撰寫而不可執行**」類。
另 `SWE-PM-003` 尚受 DR-PW5（High）影響。
**R-P124(d) 當初擇 Timeout Settings 正為避開此二 DR，而第三批之範圍直接撞上。**

**（二）`SWE-PM-010`（1 leaf）—— G103 首次真實命中**（A-PW117）。

### G103 之首次真實命中 —— `4941984` 不存在於 CFTS 本文

`SWE-PM-010` 之 037 經 SYS2 解析得 **8 個** item id，而 layer3 僅載 **7 個**。
`4941984` **於 CFTS009 / CFTS010 之文字層皆無內文段落、亦無所屬章節**
（鄰近之 `4941983` / `4941985` 皆存在）；`build_layer3` 因無法解析至章節而**靜默丟棄**。

| 閘 | 結果 |
|---|---|
| G94（`source_clause` 對 `source_anchor`）| **全綠** |
| G99（`source_anchor` 對 layer3）| **全綠** |
| **G103（layer3 對 037 獨立重算）** | **FAIL —— 缺 `4941984`** |

依 R-P144(b) 停並上繳；**已開 DR-PW11（High）**。
**惟 G103 之比對範圍僅及已產出 TC 之 leaf —— 其餘 81 leaf 是否亦有靜默丟棄，尚未測。**

### 「原文以 OR 並列而 TC 只取其一」—— 已重複七次

| # | 包 | 缺口 |
|---|---|---|
| 1 | 16 | `BODY OFF-TIMED`（R-P117(c)）|
| 2 | 17 | `and if the volume was greater` 之負分支（A-PW87）|
| 3 | 18 | `Ignition Pre Off`（A-PW94）|
| 4–7 | **22** | VR 長按、Behaviour 1 / 2 之 LTM High 形態、`028` 之 LTM High 形態（A-PW119）|

**七次皆由反向涵蓋事後抓到，至今無任何閘門可攔。**
該形態有明確語法特徵（`or` / `OR` 連接之並列條件），**可機械化性值得評估**
—— 執行層不自行立閘，提請分析層評估。

### G109 —— 評估為不可行（22 包，R-P157）

所提判準為「ER 之具名標的若不出現於本 leaf 之 `source_clause` 即為候選」——
**該判準即現行之 G82，而 G82 對全批實測為 0**。
以 `038` 為例，`MaxCallTimeout` **確實出現**於其 `source_clause`；
**越界者不是標的，而是該標的之規則**（出自 `4941718`，屬 `SWE-PM-064`）。
**token 層無法辨識，故不實作。**

### 複述判準改為可證偽性（20 包，R-P142）—— R-P96 之判準有誤

**A-PW103**：R-P96 載「若某 ER 行在『該步驟被執行』之外不含任何額外資訊，即為複述」——
**而回讀含有額外資訊，即該值本身**（`TLM_Status.Info reads "Standby"` 讀到他值即 fail）。
**overlap 對末步為錯誤工具**（A-PW104：R-P133 之剝除使 overlap 1.00→0.80 而判定 12→12）。

**新判準：可證偽性** —— 該 ER 行能否在其 procedure 步驟成功執行之情形下仍然失敗。

| 項 | 處置 |
|---|---|
| 19 §6.3 之十二條 | **全數裁為偽陽性，ER 一字未改** |
| 末步 ER 行 | **不再計 overlap**，一律入 R-P76 待人工裁決類（**永久**）|
| 非末步 ER 行 | overlap 判定不變 |
| R-P133 剝除邏輯 | **已移除**（該條後段撤回）|

R-P96 / R-P133 依 R-P36 加註，**原文位元組未變**
（`5bcbe45e…cb54` 1499 bytes、`fd3c7c25…5c30` 993 bytes）。

**改動後之 lint**：阻斷類 PASS；**待裁 44 項 = R-P142 43（每條 TC 末步各一）
＋ R-P96(a) 1（`028` 非末步）**。**43 項已依 R-P142(d) 逐條裁決，全為非複述** ——
惟**裁決者仍為撰寫者**，「沉默不算裁決」防得了漏裁，防不了自我背書。

### G103 —— layer3 之 token 層完整性（20 包，R-P144）

**A-PW105**：G99 驗 `source_anchor` 等於 layer3，而 layer3 之正確性係 03–06 包所驗；
**若建表時漏了一個 `Sys-RA-*` token，G94 與 G99 皆全綠而該錨點從頭到尾無人看過**。

G103 自 **037 獨立重算** token → SYS2 → item id，§C 正則獨立宣告，
**未讀 layer3 之任何中間產物**。**11 / 11 相等**，unresolved **0**。

**A-PW109 —— fixture 期望值寫錯反而查出真漏洞（第二例）**：
第四案原寫「多一個不存在之 token → 應 FAIL」而實測為「相等」——
不可解析之 token 不產生任何 item。**那是我的期望值寫錯，但它暴露了
「037 引用 SYS2 未載之 token 時錨點形同消失而閘門全綠」**。
已將 `unresolved` 併入判定。

> **至此三閘齊備：G94 抄對了、G99 抄全了 layer3 所載者、G103 layer3 載全了 037 所引者。**
> **惟 037 之上是空的** —— 三閘只保證該鏈**內部一致**，
> 不能排除「037 本身引錯了 token」。A-PW110 之 `Need rework` 即為此層之提醒。

### R-P143 之屬性資料（20 包 B2）—— 未裁定

**`State` 相異者為二對，非三對**（19 包所報為逐對聯集）：
`4941727`/`4941728` 皆 `Under Review`（**相同**，僅 `Model Year` 相異）；
另二對為 `New` vs `Under Review`。

**A-PW110 —— `All_Accepted` 非 `State` 過濾**：
SYS2 匯出**無 `[State:…]` 對應欄**，其狀態欄為 `HARMAN Status` / `MD Status`；
CFTS009 之 `HARMAN Status` 有 **`Accepted` 168、`Need rework` 4**
（`Sys-RA-PM-0021`/`0291`/`0292`/`0293`）——
**檔名之 `All_Accepted` 於 CFTS009 並非字面為真**。
範圍已查：僅 `SWE-PM-112` 引用 `0293`，**不在已產出之 11 leaf 內**。

### 殘差詞第二桶與並存信噪比（20 包 B4 / B5）

**A-PW106**：「已由他條涵蓋」桶 20 項**全數列出（覆核率 100%）**。

**A-PW107 —— 19 包之陳述經實測更正為誇大**：

| 口徑 | 分子 | 分母 | 信噪比 |
|---|---|---|---|
| 原值（19 包）| 1 | 145 | **0.7%** |
| 黏連正規化後 | 1 | **138** | **0.7%** |

**黏連僅 7 項（2 個相異詞），比值不動。**
19 §八(乙)6 所稱「0.7% 有一部分是抽取層造成的」為誇大，執行層更正之。
黏連辨識啟發式歷三版（23 → 10 → 7），**專案判準一字未改**。

### G99 —— 錨點清單完整性（19 包）

**A-PW96**：G94 比對 `source_clause` 與**執行層所填之** `source_anchor` ——
**若某個該被引用之錨點根本未被列進去，G94 一樣全綠**。

G99 逐 leaf 比對 `source_anchor` 與 `layer3_full.tsv` 之 `item_ids`（跨章節聯集）。
**11 / 11 相等**（`SWE-PM-038` 13/13、`057` 9/9、`065` 2/2、其餘 1/1），
無「該抄未抄」亦無「抄了不該抄」（R-P42）。fixture 五案如期。

> **G94 驗「抄對了」、G99 驗「抄全了該抄的」—— 反向涵蓋之地基兩側至此齊備。**
> **惟 layer3 本身未在 19 包被驗** —— 若建表時就漏了一個 `Sys-RA-*` token，
> 二閘皆會全綠而該錨點從頭到尾沒人看過。

### 成對／重複錨點之屬性查證（19 包 B3）

| 條 | 對象 | 結果 | 處置 |
|---|---|---|---|
| **R-P135** | `SWE-PM-038` 三組成對錨點（含／不含 `RemStartFail`）| **三對之 `Model Year` 皆相異**，其中二對另有 `Radio` / `State` 相異 | **(b) 變體登載 —— 已停並上繳，待 Pei 裁定是否合併。執行層未合併亦未拆分**（A-PW97）|
| **R-P136** | 跨章節逐字相同三對（§1.8.1.1.1 vs §1.6.2.1.17）| **七項屬性全同且內文逐字相同** | **(a) 重複登載成立，維持未另拆條**（A-PW98）—— 18 包自陳之「無證據」於此取得證據 |

若 R-P135 裁定合併，將**減少三條**（現為 `036`/`037`、`038`/`039`、`041`/`042`）。

### G73 剝除 R-P101 子句（19 包，R-P133）—— 前提只成立一半

| 條 | 剝除前 overlap | 剝除後 |
|---|---|---|
| `036` / `038` / `041` | **1.00** | **0.80** |
| `037` / `039` / `042` | 0.86 | 0.71 |

> **觸發數 12 → 12，無一條脫離**（A-PW101）。
> overlap 確有一部分是 R-P101 之產物，**主因卻是「末步讀 X、ER 述 X 之值」之回讀形態本身**。

依 R-P133 後段十二條應判真複述；**執行層評估其與 A-PW62 之已交付慣例同型**，
二種讀法並陳於上繳 §六之逐項裁決表，**未改動閘門、未改寫任一條 ER**。
**若採前者，十二條之 ER 須改寫，而該改寫會使末步所檢查之標的無法於 ER 中指名 ——
與 R-P101 直接衝突。**

### `SWE-PM-063` 之委出清單（19 包，R-P137 / §8.2.1）

五項行為逐項指出承擔之 leaf 與 TC：
`057`（018–020）、`062`（025–027）、`064`（029/030）、`065`（031/032）、`038`（033–043）。
本 leaf 自身保留可獨立觀察面（`028`）。**五項皆可指出，故為已由他 leaf 涵蓋**（A-PW99）。

### 殘差詞抽樣覆核（19 包，R-P138）

母體 **120**（候選 125 － 依 R-P42 委由他節者 5），`random.seed(19)` 抽 **20**，
**抽樣率 16.7%**，種子載明於報告與程式碼，可重現（A-PW100）。
**執行層未自我覆核該 20 項 —— 覆核屬分析層。**
一項自陳：母體含相當比例之**抽取層排版黏連**（`minutesand` / `thentlm`），
**它們拉高分母也就拉低了信噪比** —— 0.7% 不全是透鏡 3 的問題。

### R-P141 —— `SWE-PM-089` 保留一列空白（R-P116 已裁定，甲案）

理由為**待決狀態須於交付物本身可見**（與 R-P121 對 `015` 同一邏輯），
**非基於先例** —— 693 列素材只證「已交付件中無此形態」，不證「此形態不被接受」。
DR-PW1 獲解後依當時裁決填寫或移除。

**落實排程於寫回包**：`assign_final_tc_id.py` 現以 `tcs` 為輸入，
**不含無 TC 之 leaf**，須於當時補（A-PW102）。

### G94 —— `source_clause` 保真度（18 包，第二批前置）

**A-PW89**：G79 只驗該欄存在，不驗其正確 —— 反向涵蓋建立其上，
**若某條規格句根本未被抄進去，反向涵蓋於原理上看不見它**。

以 `anchor_bodies()`（R-P17 文字層定義）取原文逐字比對，
**正規化僅限 NBSP／連續空白，未擴大**（R-P125(a)）。
**11 / 11 逐字相符**；fixture 五案如期（刪句、截斷、改一字皆 FAIL）。

**實作補述**：第二批之 leaf 多錨點（`SWE-PM-038` 13 個），
`source_anchor` 改逗號分隔並依序串接 —— **若無此修改，第二批會全數誤判為「錨點原文為空」**。

**惟 G94 證明的是「抄對了」，不是「抄全了該抄的」** ——
若某個該被引用之錨點沒被列進 `source_anchor`，G94 一樣全綠；
錨點清單之完整性來自 layer3，非本閘所驗。

### 反向涵蓋 —— R-P118 已實作（報告 ＋ 人工裁決，非 pass/fail）

**A-PW80**：G82 只問「ER 之標的在不在 `source_clause` 裡」，
**不問「`source_clause` 裡有而 TC 裡沒有的是什麼」**。
R-P117 之三項缺口於閘門覆蓋率 100% 之日依然零觸發 —— 覆蓋率與品質正交之**第三次**實證。

`reverse_coverage.py` 設**三道透鏡**，其驗證條件之結果須明記：

| R-P117 之缺口 | 透鏡 1（行為項 overlap）| 透鏡 2（具名標的）| 透鏡 3（逐項殘差詞）|
|---|---|---|---|
| Load Shed 回復分支 | **漏檢**（0.80）| —— | **捕獲** `resum` |
| 通話轉移（兩處）| **捕獲**（0.40）| —— | 捕獲 |
| BODY OFF-TIMED | **漏檢**（0.72）| **捕獲** | 捕獲 |
| voltage out of range | **捕獲**（0.43）| —— | 捕獲 |

**三項全數可重現，惟透鏡 1 單獨只重現其中一項**（A-PW86）。
漏檢形態：**缺失部分只是一個詞時 overlap 仍很高** —— 為重疊率判準之結構性弱點，
非門檻調得不對。**依 17 §I 未調整拆句規則或門檻**，改為加設透鏡 2 / 3；
**透鏡 3 係於發現漏檢後才加，此順序已明載。**

**透鏡 3 另使兩項新缺口現形**（A-PW87）：
音訊類別範圍（裁為措詞不足，已於 `007`/`009`/`014` 之 ER 明列，未另拆條）；
**`and if the volume was greater` 之負分支（裁為真缺口，補 `016`/`017`）**——
透鏡 1 對該項判 overlap **0.86 已覆蓋**。

三 leaf 行為項 **20**，已覆蓋 17，無對應 3，**已逐項裁決**（R-P118(e)：沉默不算裁決）。

### 寫回路徑之閘門 —— G89 / G90（17 包）

**A-PW81**：`surgical_save` 為唯一授權之寫回路徑，至 16 包止無任何閘門在驗它。

| 閘 | 案例 | 實測 |
|---|---|---|
| **G89** | 位元組複製 | **不誤拋** |
| | 刪一個 zip member | **拋** `zip member set changed` |
| | 抹去一條 `dataValidation` | **拋** `data-validation counts changed` |
| | 改動未寫入之 `xl/styles.xml` | **拋** `members differ that were not written` |
| **G90** | 既有 5 列 80 格 | 快照**逐格相同** |
| | 新列自 r15 起 | 改動之既有格 **0** |
| | B 欄序號 | **1–22 連續** |
| | 刻意自 r13 起（重疊）| 既有格被改動 **15** —— 確實可能失敗 |

**A-PW82 之限制**：(d) 之偵測由腳本之快照比對得出；
**`surgical_save` 自身不會因覆蓋既有列而拋錯** ——
它只保證「除目標分頁外一切不變」，**append 起始列之正確性仍靠呼叫端**。

### 透鏡 3 之首次盲測（18 包，R-P128）—— 抓出 1 項事前未知之缺口

第二批之 26 條係**逐 leaf 依錨點原文直接撰寫，撰寫時未跑反向涵蓋**。

> **`4941731`（Case 4）之觸發為「passes to "Ignition Pre Off" OR to "Ignition Off"」，
> 而 `040` 僅取 "Ignition Off"** —— **透鏡 1 判 overlap 0.62「已覆蓋」，
> 是透鏡 3 之殘差詞 `pre` 使其現形**（A-PW94）。已補 `043`。

**與既有兩例同型** —— A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）：
**三者皆為「原文以 OR 並列而 TC 只取其一」，且三者透鏡 1 皆判已覆蓋。**

**R-P127 信噪比**：殘差詞 **145**（機械可判「已由他條涵蓋」20 ＋ 候選 125），
人工判別後 **真缺口 1**、措詞差異 123、已由他 leaf 涵蓋 1 ——
> **信噪比 ＝ 1 / 145 ≒ 0.7%。產出量大而命中率極低，惟其所命中者為透鏡 1 判「已覆蓋」者。**

**限度**：本次盲測只證明「透鏡 3 至少抓到一項人漏掉的」，**不證明它抓到了全部**。

**A-PW93**：反向涵蓋為 **per-leaf** —— 跨 leaf 之涵蓋會顯示為「無對應」
（`SWE-PM-063` 之細部邏輯由 `064`/`065`/`038` 承載即為一例）。

### 第一批 —— 三項前置全備已開始（17 包裁定）

R-P124 之四項理由：次小批、**首次跨 CFTS009**、含 R-P34 之爭議 leaf `SWE-PM-057`、
不觸及 DR-PW5 / DR-PW6。
**R-P118 / R-P119 / R-P120 三項前置經 17 包實測全備 —— 第二批可以開始。**

**執行層之保留**：R-P118 之產物是報告與人工裁決，不是閘門；
其效力取決於**有人真的逐項讀並裁決**。首批 20 個行為項，第二批將數倍於此。
**「沉默不算裁決」是紀律，不是機制。**

### 寫回排序 —— R-P113 已裁定（選項 B）

**A-PW75**：工作簿列序與 tc_id 對 SWE-PM ID 之關係，**自 01 包至 15 包止未被任何裁決涵蓋**
—— 分批依 Test Set（R-P72）而 §10.3 僅規範 tc_id 單調遞增，二者組合會使
`SWE-PM-001` 落於工作簿後段。現況**已寫回 0 列，重新指派無代價**。

| 階段 | tc_id | 效力 |
|---|---|---|
| 產出（依 Test Set 分批）| 批次內**臨時**編號 | 無最終效力；批次檔頭載 `tc_id_status: provisional` |
| 寫回（114 leaf 完成後，**單次**）| 依 `(SWE-PM ID, split_index)` 序自 001 連號 | 最終值；**工作簿列序即此序** |

`split_index`（R-P115，**分析層自裁**）= 同一 leaf 內依規格原文子句出現序，不寫入工作簿。
腳本 `assign_final_tc_id.py`（G85 五案如期，**只產對照表不改寫 JSON**）。

**A-PW78**：若逕以排序鍵重排 JSON 陣列，**G38 / §10.3 實測 3 項 FAIL** ——
故 JSON 陣列序與寫回列序**刻意分離**，未放寬 G38。

### dry-run 寫回 —— 三閘升為「合成＋真實」，R-G3 首度實測（16 包 B3）

沙箱 `features/power/sandbox/`（不入版控）；**來源 SHA256 前後相同，未被觸碰**；
路徑為 `backend/xlsx_surgical.py` 之 `surgical_save()`，**全程無 `Workbook.save()`**。

| 閘 | 實測 | 失敗證明 |
|---|---|---|
| **G66** | B 欄 **10 / 10** | B 欄留空 → 0 / 10 FAIL |
| **G71** | **17 / 17** 欄落點正確 | 右移一格 → 6 欄 FAIL |
| **G72** | 十列逐列相符 | 右移一格 → `design_method` 變 `None` |
| **G86** | **五條 DV（含 x14 `S10:S221`）逐字相同，全數存活** | —— |
| **G87** | **僅 `xl/worksheets/sheet6.xml` 相異**；members/sheets/merges/cf 皆同 | —— |

**A-PW77 之區辨（不得混稱）**：DV 存活**不表示 R-G3 之缺陷不存在** ——
`surgical_save` 之設計正為繞開它（不呼叫 `save()`，改以貼回原始 sheet XML
＋ 其餘 member 位元組照抄）。**本次證明繞道有效，未證明 `save()` 可安全使用。**

§3.6 / §3.8 之留白檢查（14 包 G67 所稱「須待寫回方能檢查」之二項）本包一併完成。

### `SWE-PM-073` 涵蓋缺口補測（R-P117）—— TC 由 4 增為 9

`4942354` 完整原文之 **13 項行為**逐項對照，三項未測：
（a）Load Shed **回復分支**（`008` 僅測不恢復側）→ `011`
（b）**通話轉移**（Load Shed 段與 Battery Critical 段**兩處皆未測**）→ `012` / `013`
（c）**BODY OFF-TIMED**（`009` 僅 BODY ON）與 **voltage out of range**
（`010` 僅測 10 秒逾時）→ `014` / `015`

**leaf 數仍為 3**，未構成 R-P72 所禁之範圍擴大。
`071` 4/4、`072` 4/4（其中一項受 R-P42 限縮）—— **無同型缺口**。

**A-PW79**：`015` 所測之 `voltage out of range`，**該錨點未載電壓門檻值** ——
依 §8.4.1 不造值、依 R-P42 不得赴他錨點取值，
**該條在取得門檻前不可實際執行**。是否開 DR 待分析層裁定。

**此三項缺口在閘門覆蓋率 100% 之今日依然無任何閘門會發現** ——
查出它們的是人讀規格原文逐句對照。**規格 → TC 之反向涵蓋檢查尚未成為閘門。**

### lint 現況 —— 二十二閘（`remarks` 已入 §11 視野）

G33（R-P42 a/b）、G37（R-P1）、G38（R-P2）、G39（R-P8）、G40（R-P35）、
G45（§10.7）、G46（feature.yaml）、G50（§11，12 包併入表格檢查）、G51（§4.4）、
**G63（§6 Procedure↔ER 1:1）、G64（§4.4/§8.5 環境穩定性前提）、
G65（§4.5 input_test_data 歸屬）、G66（B 欄非空列數 = TC 列數，僅合成驗證）、
G71（workbook.columns 對 r9 實測標頭）、G72（profile §2/§3.3/§3.4/§3.7）、
G73（§6 ER 複述偵測，**待人工裁決類**）、G74（§8.4.1 時間量測 ER 不得寫數值相等）、
G77（§5.2B/§5.5 Final Step 驗證意圖，**阻斷類**）、G79（R-P104 `source_clause` 必附）、
G81（R-P107 誤讀關鍵詞全欄掃描，**個案型**）、G82（R-P109 ER 標的須見於 `source_clause`）、
**G96（R-P131 —— `remarks` 已補入 G50 之 `LONG_FIELDS`，A-PW88 之判準空洞解除）**。

G79 / G81 / G82 為**批次層**閘門（以 `leaves` ＋ `tcs` 整批為單位），
由 `run_batch_gates()` 併入阻斷類。

G64 之詞彙依 R-P88 取自 canon 逐字原文（§4.4 之 `HU is powered on.`、§8.5），
非憑印象；偽陽性 0。G71 使 A-PW40 之人工盤點升格為機械檢查。

**G51 之動詞判準已改以經驗基礎導出**（R-P83）：自 Comfort + Privacy 之已交付
`test_procedure` 取行首動詞，人工清單漏列 12 個；對 1823 行已交付 `pre_conditions`
之偽陽性**二者皆為 0**，故採聯集（32 個動詞）。

**findings 已分流**（R-P76）：R-P42(b) **與 R-P96(a)/(b)** 之觸發列為「待人工裁決類」，
**不使 exit=1**。
`--self-test`：**35 個 TC fixture ＋ G46 皆如期**。

**G67 profile 條款閘門覆蓋率 = 15 / 17 = 88%**（20 條中 3 條不可機械檢查）。
未覆蓋之 2 項（§3.6 estimated_time 留白、§3.8 車型欄留白）**須待寫回方能檢查**。

### G73 之判準與已交付件衝突（13 包 B3）—— 待裁

G73 之判準以 Comfort + Privacy 已交付件之 **1076 組 (procedure 步驟, ER 行)** 語料導出。
套用該判準於同一語料：**tier1 觸發 69（6.4%）、tier2 觸發 120（11.2%）**，
形如「Select the rear Feet mode → The rear Feet mode is selected」——
即 §6 之「prove condition established」狀態回讀。
**已交付 Privacy 之 ER 更含「The output volume is read」、
「The state of the speed controlled volume is recorded」，與 R-P96 所舉之 `001` ER2 同形。**

故 G73 **全部列為待人工裁決類，不得阻斷**（A-PW62）。
若分析層認為該 6.4% / 11.2% 亦屬缺陷，結論相反，且影響及於已交付件 —— **須分析層裁定**。

### 閘門證據型別（R-P99(c)）

| 閘 | 證據 |
|---|---|
| G73 / G74 | **合成＋真實**（修正前 tier1 7 / tier2 4 / G74 2 → 修正後 0 / 0 / 0）|
| G64 | 合成＋真實（已交付 `pre_conditions` 1823 行，偽陽性 **0**）—— 惟**完備性在原理上不可驗**（A-PW63）|
| G66 / G71 / G72 | **僅合成**（A-PW61）—— 依 R-P99(b) 於寫回包一次補齊 |
| G77 / G79 | **合成＋真實**（G77 修正前 9/10 → 修正後 0；G79 3/3）|
| G81 / G82 | **合成＋真實**（G81 修正前 4 → 0；G82 補齊前 2 → 0）|
| **G66 / G71 / G72** | **合成＋真實**（16 包 dry-run；A-PW76 已結）|
| G85 | 合成（真實批次已跑但無斷言 —— 須待 114 leaf 完成）|
| G86 / G87 | **真實**（dry-run）|
| **G89 / G90** | **合成＋真實**（17 包刻意弄壞證明；A-PW81 / A-PW82 已結）|
| G91 | 真實（對修補前資料重現三項已知缺口）—— **非 pass/fail，為報告 ＋ 人工裁決** |
| G92 | ~~判準空洞~~ → **已由 G96 解除**（R-P131）|
| **G94** | **合成＋真實**（11/11 逐字相符；刪句／截斷／改一字皆 FAIL）|
| **G95** | **合成＋真實（4/5）** —— 凍結窗格一類**未實測**：本工作簿無 `<pane>`（A-PW95）|
| G97 / G98 | **真實**（第二批 8 leaf / 26 條；盲測 1 項命中）|
| **G99** | **合成＋真實**（11/11 相等；刪錨點／多錨點／空清單皆 FAIL）|
| G100 / G101 / G102 | **真實**（屬性查證、剝除實測、抽樣）|
| **G103** | **合成＋真實**（11/11 相等；刪 token／空列／未載 token 皆 FAIL）|
| G104 / G105 / G106 | **真實**（R-P142 落實後之 lint、第二桶 100% 覆核、並存信噪比）|
| G110 / G111 / G112 | **真實**（承接查證、第三批 22 leaf / 61 條、盲測 4 項命中）|
| G109 | **不實作** —— 評估為不可行（判準即 G82，越界者為規則而非標的）|
| **G113** | 合成＋真實（七項驗證 **2/7**；現況資料真實命中 **2**）|
| G114 / G115 | **真實**（115 leaf 全掃；21 包補執行）|
| **G107 / G108** | 真實 / **合成＋真實**（刪四函式時語法 True 而符號層攔下）|

### Q3 —— Final Step 措詞（15 包 B5 素材已備妥，**Pei 尚未裁定**）

**三個母體之實測，指向兩個不同的事實：**

| 母體 | 末步條數 | `check` 出現 | §5.2B 完整措詞命中 |
|---|---|---|---|
| **Arif done region（Home）** | 144 | **77（53.5%）**，且 77 條以 `Check` 起首 | **18（12.5%）** |
| Comfort + Privacy 已交付 | 472 | 0 | **0（0.0%）** |

即：**驗證意圖確為 Arif 之慣例，但其形態為祈使句 `Check the ...` 而非 `check that ...`。**
**現行 G77 之正則要求完整措詞，對 Arif 之 59 條祈使式末步亦會判 FAIL。**
執行層依 15 §I **未據此改動 G77 或任何 TC**。素材：`features/power/data/b5_arif_final_step.md`。

**一項一般性警訊**：本專案多次以 Comfort + Privacy **兩個母體**推論「全案慣例」
（G51 動詞、G64 詞彙、G73 判準、G77 語料皆然）。
B5 一加入 Home，G77 之結論即從「0 / 472」翻轉為「53.5% 有驗證意圖」。
**其餘各閘之語料是否也會因加入第三個母體而翻轉，尚未驗。**

### Final Step 慣例之分歧（14 包 B4）—— 併入 Q3

§5.2B 之驗證意圖措詞（`check that` / `to verify` / `confirm that`）
於 Comfort + Privacy 已交付之 **472 條末步中命中 0**
（`check` 0、`verify` 0、`confirm` 0、`ensure` 0、`observe` 0）；
其慣例為「Read <具體可觀察標的>」（`read` 243，51.5%）。

Power 依 R-P101 採 canon 措詞並列**阻斷類** —— 與 G73 不同，
此處判準明確可機械判定，非「無法與合法回讀區分」。
**惟 Power 之末步慣例將與該二 feature 分歧**（A-PW67），須由分析層知悉並認可。

### 寫回狀態 —— 現行阻斷為 R-P98 / R-P105 / R-P112

R-P73（欄位對應）、R-P79（範本全屬性）、R-P92（`Test Case Framework` 分頁）
之阻斷條件皆已解除；R-P90（B 欄）已明寫裁定、G66 已實作。
**現行阻斷條件為 R-P98 / R-P105 / R-P112 —— 分析層須完成 `008` / `009` 之覆核**（已覆核 8 / 10）。
R-P96 / R-P97（13 包）、R-P101 ~ R-P104（14 包）、R-P107 ~ R-P111（15 包）之處置皆已完成。
**執行層無其他新增阻斷條件。Q3 待 Pei 裁定，素材已備妥而實作未動。**

寫回包設計提醒（非阻斷）：G66 迄今僅合成驗證；G67 未覆蓋之 2 項恰只能在寫回時補齊；
Power 之 `NEVER_WRITE` 須與 `feature.yaml` 逐欄對讀，勿重蹈 Comfort O 欄之矛盾（A-PW57）。

### DATA_REQUESTS（live **6** 張）

DR-PW1（High）、DR-PW5（High）、**DR-PW8（High，17 包新開）**、
DR-PW6（Medium）、DR-PW3（Medium）、DR-PW7（Low）。

**DR-PW8** —— `4942354` 未載 `voltage out of range` 之電壓門檻值。
`015` 因此為**可撰寫而不可執行**之 TC（A-PW83），
該狀態已於其 `remarks` 標明，使其於工作簿內可見而非僅存於 DR 檔。
**此類 TC 較缺一條 TC 危險** —— 它使涵蓋率報表為真而測試無法執行。

### 11 包 8 項待裁 —— 12 包已結 6 項

| # | 事項 | 12 包處置 |
|---|---|---|
| Q1 | `B` 欄之處置 | **已裁（R-P90）**，G66 已實作（僅合成驗證）|
| Q2 | `Test Case Framework` 分頁未讀 | **已讀（R-P92 / G68）—— 非空儲存格 0，不衝突** |
| Q3 | colorScale `H10:H145` 之語義 | **未查**，依 R-P95 登記不阻斷，可與寫回並行 |
| Q4 | A-PW51 是否回報 Comfort | **已回報（R-P94）** —— `features/comfort/ANOMALIES.md` A-CF-EXT-01 |
| Q5 | §11 表格檢查補入 G50 | **已補（R-P93）**，fixture 實際觸發 |
| Q6 | profile 條款無閘門對應 | **已補 G71 / G72（R-P91）**，覆蓋率 88% |
| Q7 | Power 範本 DV 覆蓋不齊 | **登記不阻斷（R-P95）** —— 三欄依 profile 皆留空 |
| Q8 | 首批 10 條之全文覆核 | **形式面已覆核並修正；技術正確性仍未覆核**（見下）|

### 12 包八項待驗 —— 13 包已分派

| 12 §七 | 事項 | 13 包處置 |
|---|---|---|
| (甲)1 | 十條技術正確性無人覆核 | **R-P98** —— 分析層須完成覆核，寫回於完成前不開放 |
| (甲)2 | G66 從未真正失敗過 | **R-P99(b)** —— 與 G71 / G72 於寫回包一次補齊 |
| (甲)3 | G64 完備性未驗 | **R-P99(a)** —— 已補測：偽陽性 0 / 1823；**完備性不可驗**（A-PW63）|
| (甲)4 | `Test Case Framework` 之來由 | **R-P100** —— 登記不阻斷，維持不臆測 |
| (甲)5 | colorScale 語義 | **R-P100 / R-P95** —— 登記不阻斷 |
| (乙)6 | B6 範圍限定之代價 | **R-P100** —— 接受並明載，不擴大範圍 |
| (乙)7 | 合成證據不足 | **R-P99** —— 逐字採納；往後須標明證據型別 |
| (丙)8 | 作業瑕疵 | 無 |

### 13 包七項待驗 —— 14 包已分派

R-P101（Final Step）、R-P105（`006`–`009` 覆核）、R-P106（其餘六項之處置：
「對著閘門改」與「先看答案再定門檻」登記為**結構性限制，不另設機制**；
G73 判準衝突登記不阻斷；G75 維持「不可驗」；G74 維持強度明載）。

### 23 包新提之待驗（執行層獨立判斷，見 [upstream/23_or_branch.md](upstream/23_or_branch.md) §七）

- **G113 之三項不重現我知道怎麼修而依 §I 未修** ——
  交出去的是一個**我知道可以更好而刻意沒改**的閘門；克制是否正確，呈請裁定
- **G113 真陽性 3.6%（2 / 55），55 項全要人裁** ——
  R-P166 才把透鏡 1 之裁決負擔降下來，**G113 立刻又加回一份**
- **`SWE-PM-008` 缺三個 item 而該 leaf 早因 DR-PW6 排除** ——
  **若無 DR-PW6，22 包就會用一份缺三錨點之 `source_clause` 去寫它，而 G94/G99 全綠**；
  第一、二批未踩到是靠本次回頭掃描確認，**那是運氣不是流程**
- **21 包 B4 快照之原始用途已失效**（SHA256 為 23 包當下之值）
- **`SWE-PM-025` 三對僅 `ECU` 相異，執行層無能力判斷該差異是否重要** ——
  若 `ECU` 相異即為變體登載，則與 R-P135 之三對同型，**兩件事可能該一起裁**
- **「第四批 31 leaf 不受任何 live DR 影響」係逐一比對 DR 表之「阻斷何物」欄得出** ——
  若某 DR 之實際影響面大於其欄位所寫（如 DR-PW6），此查核會漏
- **作業瑕疵**：G113 首版定界邏輯明顯錯誤（0 / 7），
  **若無 R-P161(d) 之七項驗證條件，該版本會安靜回報「未覆蓋 0」而看起來像通過**

### 22 包新提之待驗（執行層獨立判斷，見 [upstream/22_batch3.md](upstream/22_batch3.md) §八）

- **DR-PW6 不解，`SWE-PM-001`–`009` 永遠無法產出** —— 不只是第三批的問題
- **layer3 之「靜默丟棄」是普遍機制，而 G103 只驗了已產出 TC 之 33 leaf** ——
  其餘 81 leaf 未測（一次全量掃描即可得，超出本包範圍故未做）
- **「OR 並列只取其一」已七次，看似可機械化** —— 執行層不自行立閘，提請評估
- **第三批 61 條全出自執行層一人，R-P159 後僅 57 條會被讀到**
- **`SWE-PM-014` 八錨點拆八條、`SWE-PM-025` 六錨點拆八條，無第二人覆核** ——
  尤其 `SWE-PM-025` 之二組文字幾乎逐字相同僅差觸發訊號，
  若其實為同一行為之兩個入口，本 leaf 就多了四條
- **透鏡 1 連續兩批零命中** —— 四項真缺口全來自透鏡 3 之殘差詞；
  透鏡 1 之 14 項「無對應」全裁為已涵蓋或範圍外，**其存續價值應予檢討**

### 20 包新提之待驗（執行層獨立判斷，見 [upstream/20_falsifiability.md](upstream/20_falsifiability.md) §八）

- **R-P142 之 43 項裁決，裁決者就是撰寫者** ——
  「沉默不算裁決」防得了漏裁，**防不了自我背書**
- **十二條中之一條（`028`）走非末步路徑，仍用已知有誤之 overlap 判準** ——
  R-P142(c) 之直接後果，本包照做，惟不一致為事實
- **G94 / G99 / G103 三閘只保證鏈路內部一致** ——
  **不能排除「037 本身引錯了 token」**；A-PW110 之 `Need rework` 即此層之提醒
- **B2 附了標頭原字串使人「能」覆核，而覆核仍未發生** ——
  分析層讀不到 CFTS 本文，抽取者即執行層
- **作業瑕疵二項**：寬切片誤刪 `lint_tcs.py` 四個函式（**第三次**，A-PW111，
  當場由 `NameError` 攔下並自 HEAD 還原）；黏連啟發式改了三版，
  **與「先看答案再定門檻」同型**，惟只影響報告附帶數字而非專案判準

### 19 包新提之待驗（執行層獨立判斷，見 [upstream/19_batch2_review.md](upstream/19_batch2_review.md) §八）

- **G99 驗 `source_anchor` 等於 layer3，而 layer3 本身未在本包被驗** ——
  建表時若漏了一個 `Sys-RA-*` token，G94 與 G99 皆全綠而該錨點從頭到尾沒人看過
- **R-P135 之屬性比對，執行層是唯一讀過原始屬性字串的人**；
  且「這七項就是全部的屬性」亦出自執行層 —— `ATTR_RE` 只抓 `[名:值]` 形態
- **B5 抽樣只覆核了「措詞差異」那一桶** ——
  若某個真缺口被誤分進機械判定之「已由他條涵蓋」桶（20 個），它進不了抽樣母體
- **R-P133 之剝除未解決 A-PW92** —— 12 條處於待裁，二種讀法導向相反處置
- **「一個 leaf 委出到只剩一條」是否為 §8.2.1 所預期之用法，執行層無依據**
- **作業瑕疵**：R-P141 之回報先寫了推估之 A-PW98 而實際落號 A-PW102，
  校對時更正 —— **與 16 包編號衝突同型：先寫號、後查號**

### 17 包新提之待驗（執行層獨立判斷，見 [upstream/17_reverse_coverage.md](upstream/17_reverse_coverage.md) §七）

- **`016` / `017` 是執行層自己裁決、自己補的，無人覆核** ——
  連分析層都尚未看過；裁決者與被裁決之工作出自同一人
- **透鏡 3 之信噪比未量測** —— 本包列出數十個殘差詞，判定其中兩項為問題，
  其餘「無妨」之理由未逐一寫下；第二批之量將大得多
- **反向涵蓋建立在執行層所抄之 `source_clause` 上** ——
  **若某條規格句根本沒被抄進去，反向涵蓋在原理上看不見它**（G79 不驗抄得對不對）
- **G90 (d) 只證明「重疊會改動既有格」，未證明有東西會攔下它** ——
  真實寫回若起始列算錯，`surgical_save` 會照寫不誤
- **G92 實質未驗到東西** —— DR-PW8 之標記在工作簿內可見與否靠人看，不靠閘門
- **G89 驗的是「會不會拋」，不是「拋得對不對」** ——
  目標分頁內之 `<mergeCell>` / `<conditionalFormatting>` 若被改動，`verify_structure` 不會攔

### 15 包新提之待驗（執行層獨立判斷，見 [upstream/15_batch1_closeout.md](upstream/15_batch1_closeout.md) §七）

- **`Test Case Framework` 分頁並非 Power 獨有 —— Home 亦有（A-PW74）**。
  12 包之「獨有」判定母體只有兩個 feature。R-P92 之結論不受影響（建立於實測 0 非空儲存格），
  但 A-PW56 之敘述本身有誤。**兩母體推論全案慣例之風險，本包已有第二個實例。**
- **`005` 之「count equals」等量斷言，規格同樣未逐字載明** ——
  執行層判其為 `buffer` 之必然蘊含，惟該區分之強度與當初判 `006` 無誤時相同
- **G81 為個案型，其黑名單只涵蓋已知的兩次誤讀** ——
  下一次語義誤讀，G81 依然零觸發；本包新增之二閘對「查出下一個誤讀」貢獻接近零
- **`071` / `072` 之 `source_clause` 若抄漏以一般措詞表述之句子，本包方法查不到**
- **`distinguishing_axis.delta` 與 `split_reason` 為同一句話存兩份** ——
  即 A-PW69 得以發生的結構原因；本包未去重（超出下放包範圍）
- **B5 之前提「Arif 144 列為全案格式權威」執行層無法從資料驗證**
- **`make_tc` 至今仍產生後綴式 `req_id`（`SWE-PM-073-01`）** ——
  對合成 fixture 無害，惟任何以 `req_id` 對 leaf 之新閘門，其 fixture 都會踩到同一個坑

### 14 包新提之待驗（執行層獨立判斷，見 [upstream/14_final_step_intent.md](upstream/14_final_step_intent.md) §七）

- **`006` 之誤讀說明「多輪閘門全綠」不能作為任何品質證據** ——
  它不是邊角，是整條 TC 在測錯的東西；查出它的是人讀規格，不是閘門
- **同型誤讀是否只有 `006` 一處，本包未能證明** ——
  比對者與寫出誤讀者為同一判斷來源，R-P105 之獨立覆核是唯一能否證它的機制
- **`007` / `009` 之步數在 13 / 14 兩包間來回一次（3→2→3）** ——
  兩次都是為了讓閘門歸零，而非對測試設計有新的認識
- **§5.2B 之 18 字上限已有三條頂到上限** —— 若後續驗證標的更多，
  18 字與「末步須揭示所檢查者」會直接衝突，為可預見之下一個結構性問題
- **`reasoning_note` 為執行層自行新增之欄位**，非裁決條文所定介面，須分析層明示
- **G77 之判準來自 canon 而非語料**（語料實測結果與之相反，0 / 472）——
  非 R-P101 所要求之「經驗導出」，已明說而未混稱
- **G79 只驗欄位存在，不驗 `source_clause` 抄得對不對**

### 13 包新提之待驗（執行層獨立判斷，見 [upstream/13_er_quality.md](upstream/13_er_quality.md) §七）

- **步驟合併使十條之技術正確性覆核更為必要** —— 本包主動改動 procedure 結構，
  合併後是否仍完整測到該 leaf 之行為，**只有執行層一人判斷過**
- **`008` 之 procedure 未變更，且 G73 前後皆 0 觸發** —— 該條品質完全靠人工判斷
- **`007` / `009` 之 ER1 改過兩次才使 tier2 歸零** ——
  「對著閘門改而非對著規則改」之風險，改動與歸零為同一次，無法互相佐證
- **G74 之形態基礎僅兩個實例**（R-P97 所引），四種形態中兩種為執行層擴充，
  **非經驗導出**，強度低於 G73 / G64 / G51
- **G73 之門檻調整過三次**（0.833 → 0.75 → 0.50）——
  過程確為「先看答案再定門檻」，三次數字皆留於 B3 與程式碼註解供檢驗

### 長期已知限制（非待辦）

**Layer 3 之邊界由 SYS2 收錄規則決定，非獨立界定。** R-P7 裁定不追 SYS2 收錄規則，
R-P37 停止章節層調查 —— 二者合起來即：本 feature 之規格涵蓋範圍由上游決定。
若日後有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。
見 [upstream/05_testset_lock.md](upstream/05_testset_lock.md) §八之一。

### 尚未進入

Phase 4 以降全部未開始。FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
