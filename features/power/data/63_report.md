# 63 包 —— 執行層回報

§H 第 1–4 步完成，依第 4 步「停，待覆核」停在 R-P372 複查之後。

## 1. G255 —— 本包條文數字與重算結果（R-P379(c)）

依 R-P379(b)，**抄錄前**逐一重跑條文所引之機讀來源，**3 / 3 相符**：

| 條文所引 | 機讀來源 | 重算 | 符 |
|---|---|---|---|
| 2 條（丁案適用，R-P376(b)）| 現行 corpus 中 `test_item` 含 `RemStartFail` 且 `reasoning_note` 引 `4941504` 者 | **2**（`-057` / `-065`；母體 14）| ✓ |
| 45 名（R-P378(b) 之複查對象）| `proxy_reachability_55.md` 無錨名 51 − 逐字含 `antitheft` 者 6 | **45** | ✓ |
| 16（G251 之 ITD 非 `NA`，R-P378(a)）| `family_k_disposition_55.tsv` class ∈ {b, c} | **16**（b=14、c=2）| ✓ |

**三個數字皆相符，依 R-P379(b) 逕行抄錄。**

## 2. 抄錄

- `RULINGS.md`：**R-P376–R-P379** 逐字抄入（4 / 4）。§J 重驗：4/4/四條，一致。
- R-P36 加註三處：**R-P372(b)**（「11 名／40」作廢 → 6 名／45）、
  **R-P373(c)**（「(c)=0／G251=15」作廢 → (c)=2／16）、
  **R-P375(b)**（示例作廢 → 改 `SwitchOff_Timeout_Setting.Req`）。
- **R-P379 自本包起適用**；新增 G255（本節即其產出）。

## 3. R-P376 —— 丁案二條入 corpus

`python features/power/scripts/apply_r_p376_63.py`（先 `--dry-run` 再落）。
改動落在 `generated/batch_003_power_state_a.json`；JSON 序列化經 round-trip
驗過**與原檔逐位元組一致**，故 diff 僅二條 TC。

| | `-057` | `-065` |
|---|---|---|
| 點火值 | `2 (Ignition_Off)` | `10 (Ignition_Pre_Off)` |
| 三步 Procedure | `OperationalModeSts` → `RemStActvSts = 0` → 讀 `PowerSts_Telematic = 1 (Standby)` | 同 |
| ITD | `NA` | `NA` |
| 括號下半 | `(read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby)` | 同 |
| Remarks | `(R-P376 丁案；原驗 RemStartFail 內部值，改驗其下游效果)` | 同 |

驗證：
- 二條之 **Procedure / ER / Pre-Condition 已無 `RemStartFail`**；`test_item` 上半 verbatim 未改 ✓
- 二條之**五欄鍵仍相異**（差在 `test_procedure` / `expected_result` 之點火值）✓
- 全 corpus 五欄逐字相同對 **11**（與 58 包同，未因本次改寫增減）✓

`pattern_d_trial_61.md` 已加標「已採（R-P376(b)）」。
R-P376(d) 之代價（「該二條不覆蓋 `RemStartFail` 內部值本身」）已寫入二條之
`reasoning_note`，交付說明待寫回時併入。

## 4. ⚠ R-P377(a) 與 R-P375(c) 衝突 —— 9 條中 6 條不成立

R-P377(a) 令強、中候選撤 PENDING。機讀重算：**PENDING 102 → 93**（`pending_recount_63.tsv`）。

**但其中 6 條不應撤。**

R-P375(c) 明文：`.Info` 類致能狀態命中 PROXI／Default Settings 之**存在性參數**者，
**僅為 Pre-Condition**；「**其運行時狀態仍須 CAN／UI 觀察面，另查**」。

R-P377(a) 解除 PENDING 之 9 條逐條檢視：

| tc_id | 訊號 | 用法 | 依 R-P375(c) 是否可撤 |
|---|---|---|---|
| `-062` / `-076` / `-077` | `SwitchOff_Timeout_Setting.Req` / `Rear_Camera_Enable.Info` | Pre-Condition 之靜態組態 | **可撤** |
| `-017` / `-018` / `-019` | `SwitchOff_Timeout_Setting.Req` | Procedure／ER 之運行時讀取 | **不可撤** |
| `-070` / `-081` / `-107` | `Rear_Camera_Enable.Info` | 運行時轉移（`passes to "False"`、`"False" then "True"`）| **不可撤** |

三名之全案用法分布：

| 訊號 | 靜態組態 | 運行時 |
|---|---|---|
| `SwitchOff_Timeout_Setting.Req` | 8 | 7 |
| `SwitchOffSetting.Req` | 0 | **2** |
| `Rear_Camera_Enable.Info` | 5 | 4 |

**故 PENDING 之正確值為 99 而非 93** —— 撤除者僅 3 條。
`SwitchOffSetting.Req` 之二條**全為運行時**，該名實際上一條都不能撤。

**本層不自行取捨**（R-P377 為分析層之裁定），照 R-P377(a) 產出 93 之機讀值，
**同時據實回報 99 之依據**。請裁：
- 甲：R-P377(a) 之撤除限於靜態組態用法 → PENDING **99**
- 乙：R-P377(a) 之撤除及於全部用法（等於對 R-P375(c) 開例外，須明文）→ PENDING **93**

## 5. R-P372 複查（§H 第 4 步）

落檔 `data/proxy_reachability_63.md`。
產生指令：`python features/power/scripts/proxy_recheck_63.py`。

對象 **45 名**（51 − 逐字含 `antitheft` 之 6；6 名併入 DR-PW23）。
查詢名稱種類改為**規格用語**（取自各名所屬 TC 之 `test_item` 上半 verbatim），
與 59 包之「TC 措辭」為**不同之查詢名**（R-G13 第 2 項）。

| 判定 | 數 |
|---|---|
| **有錨** | **39** |
| 查無 | 6 |
| 未覆蓋 | 0 |

### ⚠ 誠實揭露：本輪仍非「人讀」

R-P372(a) 令「**人讀**」。本檔所做者為**第二次機器掃描、改以規格用語為查詢名**，
**不是人讀**。機器仍以內容詞交集為鍵，故 TC 措辭之殘留
（`after`、`each`、`again`、`one`）會混入查詢詞。

**故 6 個「查無」仍不足以登記為 R-G13 意義下之查無** —— 其查詢名非純規格用語。
六者為：`call audio routing and the TLM state`、`remote start outcome flag and the TLM state`、
`HU behavior and the stored logs`、`shown wording`、`TLM_Status.Info after each one`、
`TLM state again after Timeout1 has elapsed`。

**本層不為該 6 名開 DR、不登 M-n**，理由同 59 包 §3（未達要件者不得向上游提問，
A-PW355 之教訓）。**G252 之「查無者全有 DR 號與 M-n」本包仍無法滿足。**

### 39 個「有錨」為可用之正面結果

其查詢詞全部落在規格用語內，命中之錨點為 G0 台帳內之 `{ObjectID}` 段落，
**可直接補入代理量表**。59 包之 51 名無錨中，**39 名（76.5%）經改查詢名即得錨** ——
與 A-PW361（forms/ 窄讀）同一教訓：**查不到多半是查詢範圍或查詢名之問題，
不是對象不存在。**

## 6. 待裁

1. **R-P377(a) × R-P375(c) 之衝突**（§4）：PENDING 為 **99**（甲）或 **93**（乙）。
2. **G252 之「查無者有 DR 號」**（§5）：6 名仍未達 R-G13 要件；
   是否安排真正之人讀，或改寫 G252 之期望值。
3. **39 個有錨名是否即可填代理量表**（R-P367 令可及性報告覆核後始填）。

**B5 依 R-P374(a) 續凍。**
