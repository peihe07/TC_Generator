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

---

## 參考素材庫條文（R-G12／R-G13／R-G14，Pei 2026-08-24，全域）

來源：`features/display/docs/handoff/04_reference_store.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄；核對表見節末。

```text
R-G12（參考素材庫之位置與 manifest —— 全域）
DBC、PROXI 表、LID 對照表一律置於 `forms/`，與 036 母本同目錄。
不另立 `reference/` 目錄（Pei 2026-08-24 裁定）。

`forms/*` 已由根 `.gitignore` 排除、`FORMS.md` 已 tracked，
形狀無須變更：檔案不入 git，manifest 入 git。

`FORMS.md` 新增一節 `## 參考資料庫（DBC / PROXI / LID）`，每檔一條目，
必填欄位六項：

  (a) 檔名、SHA256、bytes、mtime
  (b) **涵蓋範圍** —— DBC 記其匯流排與訊號定義列數、訊息數；
      LID 記其分頁、資料列數、架構欄組清單；PROXI 記其分頁與參數列數
  (c) 版次與其來源（檔名所載，非推定）
  (d) 已知不涵蓋者（如 BHCAN2 不含 FD-CAN 上之訊號）
  (e) 取代關係（本檔取代誰、被誰取代、或並存）
  (f) 首個採用之 feature 與日期

(b) 為必填之理由見 R-G13：無涵蓋範圍之登錄，「查無」不構成發現。
```

```text
R-G13（查無之成立要件 —— 全域）
「某訊號／參數查無」之陳述，僅在同時載明下列三項時成立：

  (1) 查了哪些檔（檔名 + SHA256）
  (2) 用什麼名字查（LID 名？CAN 訊號名？規格原文名？）
  (3) 該檔之涵蓋範圍是否本應包含之（匯流排、架構、版次）

三項缺一，該陳述一律記為「未查得」而非「查無」，且不得據以開 DR。

實例（2026-08-24，Display）：分析層先以 `PDT27_E2A_R5_FDCAN8.dbc` 查
`DCSD_DISP_STAT` 得 0，若逕報查無即為誤 —— 該訊號在 B-CAN 上，
FD-CAN 之 DBC 本就不含之。同日又以 LID 名 `ICSPowerButton` 查 DBC 得 0，
亦為誤 —— 其 CAN 訊號名為 `Radio_btn0`／`DCSD_Power`。
```

```text
R-G14（查無台帳 —— 全域）
`forms/LOOKUP_MISSES.md`（tracked）為全案唯一之查無台帳。
凡經 R-G13 三要件仍查無者，登記一列，欄位：

  query | 查詢用之名稱種類 | 查了哪些檔(含SHA256前16碼) | 涵蓋範圍是否應含
  | 結果 | 發現之feature | DR編號 | 狀態

目的為避免同一個 miss 被各 feature 重複發現、重複向上游提問。
新 feature 開案時須先讀本檔。

登記之同時，仍須於該 feature 之 `ANOMALIES.md` 登 anomaly、
`DATA_REQUESTS.md` 開 DR —— 三處各有其職，不互相取代：
台帳防重複發現，anomaly 綁該 feature 之批次，DR 綁上游提問。
```

### 抄錄核對表

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G12 | 528 | `c9fb52dea97b2edb` | 是 |
| R-G13 | 387 | `a1ba5e165f2ad121` | 是 |
| R-G14 | 363 | `0d18b275bc9428d6` | 是 |

首個適用之 feature：`display`（2026-08-24）。台帳實作見 `forms/FORMS.md` 之參考資料庫節與 `forms/LOOKUP_MISSES.md`。

---

## 參考資料庫之版本綁定（R-G15，2026-08-24，全域）

來源：`features/display/docs/handoff/05_proxi_and_values.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G15（參考資料庫之版本綁定 —— 全域）
每個 feature 之 `feature.yaml` 須新增 `reference:` 節，逐項記載其
所用之參考資料庫檔名與 SHA256：

  reference:
    dbc_b:   { file: ..., sha256: ... }
    dbc_fd:  { file: ..., sha256: ... }
    lid:     { file: ..., sha256: ... }
    proxi:   { file: ..., sha256: ... }

理由：`features/vehicle_setting/` 使用 LID v1_76，`features/display/`
使用 v1_78，而**沒有任何條文在追這件事**（執行層上繳 04 §8 第 4 項
指出）。兩版若對同一 Logical Identifier 給出不同之 CAN 訊號名，
跨 feature 之一致性即斷裂，且斷得無聲無息 ——
「看起來成功的輸出最需要對照其定義」（上繳 04 §5.3）。

`forms/FORMS.md` 之各條目須反向記載「哪些 feature 使用本檔」。
版本差異之實測不在本條範圍；本條只要求**綁定可見**。
```

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G15 | 561 | `9b4512a26c552666` | 是 |

首個適用之 feature：`display`（2026-08-24，`feature.yaml` 之 `reference:` 節）。

---

## 量測與聚合分離（R-G16，2026-08-24，全域）

來源：`features/display/docs/handoff/06_glossary_anchor.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G16（量測與聚合分離 —— 全域）
量測正確而聚合錯誤，是本專案已重複三次之缺陷型態：

  上繳 04 §5.3  DBC 以字典序取首個含該訊號名者 → 匯流排接錯
  上繳 05 §2    TSV 以逗號串接 token，而 token 自身含逗號 → 59 塌成 44
  上繳 05 §6.1  LID 多值儲存格未拆、拆後未做欄內空白正規化 → 漏 107 列

三者之共同特徵：**擷取階段正確，其後的選取／序列化／正規化階段出錯，
且輸出「看起來合理」，不會自曝。**

拘束三項：
(a) 序列化之分隔符不得為資料中可能出現之字元。逗號、分號、頓號、
    空白一律不得作為多值分隔符；採資料中不出現之字元（如 ` ¦ `）
    並於檔頭載明。
(b) 多值儲存格一律**逐值一列**輸出，不合併；若必須合併，須另存
    未合併之原始欄供稽核。
(c) 凡「自多個候選中選定一個」之步驟（選 DBC、選 LID 列、選 PROXI 列），
    其選定判準須逐筆記錄於 `note` 欄，不得只留結果。

驗收方式：任一產出之筆數，須能由擷取階段之筆數與各階段之增減量還原。
還原不出，即為聚合階段有未申報之操作。
```


## R-G13 之補充（2026-08-24，全域）

併於 R-G13 原條之下；**原條全文不動**，見上方「參考素材庫條文」節。

```text
R-G13 補充（查詢鍵不限於 DBC —— 併入原條）
原條第 (2) 要件「用什麼名字查」之適用範圍，及於**任何以名稱為鍵之
查找**，不限 DBC：PROXI 之 `Parameter Name`、LID 之
`Logical Identifier`、CFTS 之條號、Polarion 之 Melco ID 皆同。

實例（上繳 05 §6.1）：以 Logical Identifier 查 PROXI `Parameter Name`
得 70/446；改以 LID `Atlantis & Atlantis High` 欄組之 `Signal Name`
為鍵得 177/446，漏 107 列（60%）。
兩次都是「查了同一個檔」，差別只在用什麼名字查。
```

### 抄錄核對表

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G16 | 527 | `14f1899d59fee11d` | 是 |
| R-G13 補充 | 337 | `fd7f12de1170bf84` | 是 |

首個適用之 feature：`display`（2026-08-24）。

---

## 匯出檔自帶字典之校驗（R-G17，2026-08-25，全域）

來源：`features/display/docs/handoff/07_pipeline_and_anchors.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G17（匯出檔之自帶字典須逐欄校驗 —— 全域）
Polarion 匯出之工作簿常帶一個列舉值字典分頁（本案為 `_polarion`）。
凡有此分頁者，須於 Phase 1 逐欄校驗主表之實際用值是否在字典內，
並將違規列數與違規值逐項登記。

校驗前須先分辨字典列與非字典列：本案 `_polarion` 之第一欄
**含 `:` 者才是欄位列舉字典**（2 個），其餘 340 列為工作項連結，
不是欄位字典。誤把後者計入會產生一個做不完的待辦。

向上游反映之措辭為「值未依匯出檔自帶之字典校驗」，
不得寫成「大小寫不一致」—— 後者聽起來像格式瑕疵，前者是資料
校驗缺口，二者之嚴重性與處置對象不同。

實例（本案）：`SYS2 分類 Category` 字典 5 值，主表用 6 值，
違規 117/333（35%），且違規之拼法（`Out of Scope`）是多數。
```

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G17 | 394 | `8e1a45c80c9a46a2` | 是 |

首個適用之 feature：`display`（2026-08-25，SYS2 `_polarion` 分頁）。

---

## `--scaffold` 搬移之後果（R-G18，2026-08-25，全域）

來源：`features/display/docs/handoff/08_recon_and_norm.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G18（`--scaffold` 之搬移使 intake 不可重現 —— 全域）
`intake.py --scaffold` 以 `shutil.move` 將素材自 `_intake/<Feature>/`
搬入 `features/<f>/inputs/`。搬移後該 `_intake/` 目錄為空，
**該 feature 之 intake 分類結果不再可重現**。

實測（上繳 07 §3.1）：`_intake/` 六個目錄中四個
（AMFM／Comfort／Privacy／Time_Management）之可分類檔為 **0**。

三項拘束：
(a) 凡於空目錄上執行之檢查，其 PASS 一律不成立，須標「未實測」
    （canon §5a：不可能失敗之檢查項不標 PASS）
(b) 需要回歸驗證分類器時，須先自各 feature 之 `inputs/` 重建語料
    （hard link 即可，不複製位元），並於報告中載明語料為重建者
(c) 重建之臨時目錄用後刪除；`_intake/` 全域被 `.gitignore` 排除，
    不入 git

本條不要求改變 `--scaffold` 之行為 —— 搬移而非複製有其理由
（避免兩份來源）。本條要求的是**知道它的後果**。
```

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G18 | 564 | `f003d7f9833cb671` | 是 |

首個適用之 feature：`display`（2026-08-25，上繳 07 §3.1 之回歸語料重建）。

---

## R-G19 — 寫回作業規定全專案化（Pei, 2026-08-25）

來源：`features/time_management/docs/handoff/29_global_writeback.md` §1。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G19（Pei, 2026-08-25）—— 寫回作業規定全專案化

下列規定自即日起適用於全專案所有 feature 之一切工作簿寫回，
不限 time_management（升格來源：R-TM78／R-TM80／W-TM-26 之寫回實務；
Pei 指示原文：「這裡的寫回規定要套用到全專案」）：

1. dry-run 前置：`--write` 前必跑一次不帶 `--write` 之 dry-run，
   其逐列比對結果附於回繳包（R-TM78 升格）。
2. 輸出另檔：寫回指令一律明寫 `--out`，不得覆寫基準檔；
   輸出落於該 feature 之 output/（R-TM80 升格）。
3. 基準宣告：下放包所宣告之基準檔 SHA256 由腳本對「宣告路徑之檔案」
   實測產出，不得手抄、不得以 repo 內同名檔代替宣告路徑之檔；
   基準檔在 repo 外者，先取複本入 inputs/ 再實測
   （A-TM30／A-TM31 之教訓）。
4. 驗收判準：回繳之逐列 diff 須涵蓋全部欄；非受令欄之任何變更
   即退回。identifier 欄（TC ID、Test Group）之變更一律須先經裁定，
   未經裁定之改名視同缺陷登記 anomaly。
5. 樣式變更走衍生通道：不改既有 <xf>（避免連帶重掛共用該 id 之格），
   由現用 xf 衍生新 cellXfs 附於表尾、只重掛指名之格；通道須明示啟用
   （feature.yaml 鍵），未啟用者行為與變更前逐位元相同
   （W-TM-26 T5 之 surgical_restyle 升格）。
6. 容器完整性依 R18-3 常設規則（xlsx_surgical 為唯一寫回路徑；
   zip 成員集合與 classic/x14 DV 計數不等即 ABORT）——
   本項為既有全域規則之重申，非新增。

各 feature 之既有同義條文（R-TM78/80 等）保留為軌跡不刪；
新 feature 不再逐一另立，逕引本條。
```

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G19 | 882 | `fef0cad264e9ddd2` | 是 |

首個適用之 feature：`time_management`（2026-08-25，W-TM-26-A1）；
既有 R-TM78／R-TM80 保留為軌跡。`RULINGS.sha.tsv` 待執行層重生。

---

## 理由與數字、報告與量測（R-G19／R-G20，2026-08-25，全域）

來源：`features/display/docs/handoff/09_recon_crosscheck.md` §四。
抄錄方式：機器抽取原樣寫入，未經人工轉錄。

```text
R-G19（理由與數字須分別驗證 —— 全域）
一個正確的數字配一個未經驗證的理由，其危害大於一個明顯錯誤的數字：
數字會被引用一次，理由會被用來推論別的事。

凡於報告中對某一量測結果給出「為什麼是這個數」之解釋者，
該解釋本身須有其獨立之量測支持，或明白標記為「未驗之推測」。
兩者不得混寫。

實例（上繳 08 §4.1）：SYS2 側正規化加 0 個候選。
推測之理由為「散文中底線少見」；實測為 80 列中 66 列含底線（82.5%），
相異 token 40 個 —— **推測之理由完全錯誤，而數字正確**。
真正原因為 `DISP_REAR_CAMERA` 正規化後仍不等於 `Rear View Camera`。
```

```text
R-G20（報告中之摘要數字須為機器輸出 —— 全域）
上繳／下放包中所載之雜湊、列數、比率、命中數等一切量測結果，
一律自腳本輸出**複製**，不得憑記憶或憑印象謄寫。

理由：擷取正確、比對正確，而「把結果謄進報告」這一步**沒有任何
自動檢查**。R-G16 所列之三次缺陷皆在量測之後的處理階段，
本條所指者更後一步 —— 在報告階段。

實例（上繳 08 §1）：抄錄核對表之三個 SHA256 憑印象填寫，
與實算值皆不符，定稿前始以機器輸出覆蓋。逐字元比對本身自始由機器
執行且正確，錯的只有報告。

實作建議：核對表、統計表由腳本直接產出 markdown 片段，
撰稿時貼入而非重打。
```
