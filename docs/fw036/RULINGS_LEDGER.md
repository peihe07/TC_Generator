# 裁決台帳（FW036 全案）
欄位：編號｜日期｜標題｜狀態｜出處包｜適用範圍
狀態：ACTIVE / [DEFAULT] / SUPERSEDED / WITHDRAWN
規則：條文全文僅於本台帳落檔一次，各包引用編號不重抄。
撤銷之裁決以刪除線保留並附區塊引註，不得刪除（R-TM13）。

| 編號 | 日期 | 標題 | 狀態 | 出處 | 範圍 |
|---|---|---|---|---|---|
| ~~R-1 v1~~ | 2026-08-21 | ~~訊號記法三層（CAN 採三件組）~~ | **SUPERSEDED** | 01a | 全案 |
| ~~R-1 v2~~ | 2026-08-21 | ~~CAN 訊號採 `Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`，PROXI 加 `$`~~ | **SUPERSEDED** | 09 | 全案 |
| R-1 v3 | 2026-08-21 | 訊號一律 `$<MESSAGE>.<Signal>$ = <raw> (<label>)`，label 取自 DBC `VAL_`；PROXI 作 `PROXI <Param> = <值>` 不加 `$`；內部訊號 DBC 查無對應者保留來源名不加 `$`，並於 PROC 寫出應設定或應觀察之值 | ACTIVE | 12、17 | 全案 |
| R-2 | 2026-08-21 | spec_reference 家族分流 | ACTIVE | 01a | 全案 |
| R-3 | 2026-08-21 | test_item 上半 50 token | ACTIVE | 01a | 全案 |
| R-4 | 2026-08-21 | verbatim 首字轉大寫 | ACTIVE | 01a | 全案 |
| R-5 | 2026-08-21 | 雙語制合法化不回修 | [DEFAULT] | 01a | BT/Projection |
| S1 | 2026-08-21 | 舊規 superseded | ACTIVE | 01b | 09_ 目錄 |
| S2 | 2026-08-21 | §11 收斂 | ACTIVE | 01a | 全案 |
| S3 | 2026-08-21 | lint 出貨 gate | ACTIVE | 01b | pipeline |
| S4 | 2026-08-21 | test_item 括號下半 | ACTIVE | 01a | 全案 |
| S5 | 2026-08-21 | 裁決台帳制 | ACTIVE | 01b | 流程 |
| S6 | 2026-08-21 | 缺件 PENDING 佔位。**併見 R-14**：`PENDING` 說明之語言一律英文，中文描述置於 `DATA_REQUESTS.md` | ACTIVE | 01a | 全案 |
| N-1 | 2026-08-21 | N 規制單位為 item，子步驟與續行同受規制 | ACTIVE | 00c/00d | lint |
| R-6 | 2026-08-21 | verbatim 上半豁免 P（訊號記法） | ACTIVE | 03 | lint／全案 |
| R-6b | 2026-08-21 | verbatim 上半豁免 C（hedge）；作者用語品質類檢查僅施於括號下半 | ACTIVE | 06 | lint／全案 |
| R-7 | 2026-08-21 | 值之語意標籤取自 DBC `VAL_` 列舉 | ACTIVE | 09 | 全案 |
| R-8 | 2026-08-21 | spec_reference 一值一行、前綴逐行重述、禁串接；CFTS 列不附檔名章節 | ACTIVE | Pei 直接裁定 | 全案 |
| R-9  | 2026-08-21 | Pre-Condition 一條件一行一編號 | ACTIVE | 13 | 全案 |
| R-10 | 2026-08-21 | 空白與字元正規化（分區適用） | ACTIVE | 13 | 全案 |
| R-11 | 2026-08-21 | 一觀察點一步驟／須寫出應觀察值／Input 一律 NA | ACTIVE | 14 | 全案 |
| R-12 | 2026-08-21 | Pre-Condition 句式與排序（工具行置末） | ACTIVE | 15 | 全案 |
| R-13 | 2026-08-21 | 規格訊號名與 DBC 不符之處置：規格原文所載之訊號名，即使 DBC 查無同名，一律保留原文名稱，不得代以語意相近之他訊號；DBC 對應缺漏登記 DR 向上游查詢 | ACTIVE | 19 | 全案 |
| R-14 | 2026-08-21 | PENDING 佔位說明一律英文 | ACTIVE | 20 | 全案 |
| R-15 | 2026-08-21 | 台帳條文之完整性：下放包要求「逐字寫入」台帳之條文必須為條文全文，分析層不得為版面或欄寬簡寫；若原條文過長，改列摘要欄並保留全文於同列，不得以摘要取代全文 | ACTIVE | 21 | 全案 |
| R-16 | 2026-08-24 | test_item 括號下半為**需求側摘要**，自 b19 原列語意推導，**與 proc 現行文字無需逐字同調**；proc／er 之內容改寫不因此觸發括號重推導 | ACTIVE | 30（29 包上繳 §七-1 之就地裁決） | 全案 |

> **R-12 加註**：R-12(b)（spec_ref 條數上限 4）已於
> `features/power/docs/specref_anchor_chain_verified.md` 撤銷；
> R-12 現行僅存 (a) Pre-Condition 句式與排序。

> **R-1 v2 撤銷加註（R-TM13）**：經 CR30580/30581 參考本查證，
> `$` 為訊號之標記而非 PROXI 之標記；v2(c)(d) 之指派相反。
> 由 **R-1 v3** 取代（12 包）。v2(a)(b)(e)(f) 之內容併入 v3。

> **R-1 v3(d) 修訂沿革**：12 包原條文為「內部訊號必須轉為可觀察之 CAN 訊號，
> 查無對應者**不得留內部訊號名**」。17 包 §三修訂 —— DBC 查無對應者
> **保留來源名稱**（不加 `$`），並依 R-11(b) 於 PROC 寫出應設定或應觀察之值；
> 理由為強令改寫為「HMI 現象」將失去追溯性且該現象常無來源明載，反致造值。
> **原「不得留來源名」之表述作廢。**

## 條文落檔位置

> **本表不得使用「同上」串接指涉**（A-PM17）—— 插入列會靜默改變其後各列之
> 指涉對象且無檢查可攔。各列一律書寫完整路徑。

| 編號 | 條文全文所在 |
|---|---|
| ~~R-1 v1~~ | 已撤銷，見下方撤銷紀錄 |
| ~~R-1 v2~~ | 已撤銷，見上方 R-1 v2 撤銷加註（原 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5） |
| R-1 v3 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5（沿革含 12 包原文與 17 包 §三之 (d) 修訂） |
| R-6 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5 末段＋`scripts/lint036.py` 檢查 P 之範圍 |
| R-6b | `scripts/lint036.py` 檢查 C 之範圍 |
| R-7 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5(a) |
| R-8 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §10.7 之「排列」段 |
| R-2 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §10.7 |
| R-3 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §4.3.1 |
| R-4 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §4.3.1 |
| R-5 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §1（`[OVERRIDE-R5][DEFAULT]`） |
| R-9 | `docs/fw036/handoff/13_r9r10_layout_whitespace.md` §R-9 |
| R-10 | `docs/fw036/handoff/13_r9r10_layout_whitespace.md` §R-10 |
| R-11 | `docs/fw036/handoff/14_r11_samples.md` §R-11 條文 |
| R-12 | `docs/fw036/handoff/15_r12_precondition_specref.md` §一 |
| R-13 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5(g) |
| R-14 | `docs/fw036/handoff/20_pm_closeout.md` §一 |
| R-15 | `docs/fw036/handoff/21_ledger_fix.md` §一 |
| R-16 | `docs/fw036/handoff/30_pm_final_review.md` §一（就地裁決第 1 項） |
| S1 | 本檔（標記行為見 `docs/fw036/upstream/01b_mechanism_setup.md`） |
| S2 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |
| S3 | `scripts/lint036.py` module docstring |
| S4 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §4.3.1 |
| S5 | `docs/fw036/FEATURE_ONBOARDING.md` §8.9 ＋ 本檔 |
| S6 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.4.3 |
| N-1 | `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §11 |

## 撤銷紀錄（R-TM13：不刪除，加註保留）

~~**R-1 v1**：CAN 訊號斷言採三件組 `<Signal> in <MESSAGE> on <segment>`，
例 `RemStActvSts in STATUS_BH_BCM2 on BH-CAN`。~~

> **撤銷（2026-08-21，Pei 裁定「都是照我 SWC 怎麼樣寫就這樣寫」）**：
> v1 係分析層自「同一 signal 於 BH-CAN 與 FD-CAN8 皆存在且 message 不同」
> 推導網段必要性而立，**未先查證 Pei 既有交付之實際寫法**。
> 執行層複驗：三件組於 SWC 0708 之 286 列中出現 **0 次**；
> `Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)` 式出現 **546 次／273 列**。
> message 名本身即可判別網段（`BCM_FD_14` → FD-CAN），無須另書。
> 依 v1 已改動之 PM 42 格須回改（下放包 10a §A1）。
>
> **程序原則（09 §五）**：格式類裁決應先窮舉 Pei 既有交付之實際寫法，
> 以語料為權威，分析層僅負責歸納與一致化。

~~**17 包 §五**：`PowerModeSts_Telematic` 係 `PowerSts_Telematic` 與
`PowerModeSts` 之名稱混合、非 DBC 實有，故一律採 `PowerSts_Telematic`，
`PowerModeSts` 不使用。~~

> **撤銷（2026-08-21，下放包 19 §一）**：原裁定基於分析層之錯誤前提 ——
> 僅查 DBC 未查 CFTS 原文即斷為「名稱混合」。
> `CFTS009-4941562` 逐字載 `signal PowerModeSts_Telematic`，
> **為規格原文之訊號名，非 036 之筆誤**。
> 執行層於上繳 17 §五所報之二後果（`Standard_Power` 無對應 VAL_、
> 觸發與觀察塌縮為同一訊號）**皆為該錯誤裁定之必然結果**，
> 已於 19 包回復規格原文寫法（row 72），並立 **R-13**、開 **DR-PW21**。
