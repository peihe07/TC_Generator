# G113 未覆蓋分支之分桶（R-P171）

> 判準見 `scripts/g113_buckets.py` docstring —— **先寫定後執行**。
> 前二桶給計數與抽樣例示（抽樣率 ≥ 16.7%）；`真缺口` 逐項完整理由並依 R-P118(d) 裁決。

## 計數

| 桶 | 數 | 佔比 |
|---|---|---|
| `規格未定義該支` | **27** | 36.5% |
| `已由他條或他 leaf 涵蓋` | **47** | 63.5% |
| `真缺口` | **0** | 0.0% |
| **合計** | **74** | 100% |

## 桶 `規格未定義該支` —— 27 支，抽樣 5 支（18.5% ≥ 16.7%）

| leaf | 組/支 | 分支文字 | 具名標的 | 觸發未覆蓋之詞 |
|---|---|---|---|---|
| `SWE-PM-071` | 1/1 | shown on TLM display (only if TLM has not to pass to Standby | **無** | `only`、`pas` |
| `SWE-PM-065` | 1/2 | BT streaming audio) staying still in Timed state. | `BT` | `bt`、`state.`、`stay`、`stream` |
| `SWE-PM-038` | 6/2 | at maximum until MaxCallTimeout expires. | **無** | `expires.`、`maximum` |
| `SWE-PM-025` | 1/2 | not (refer to TLM HMI Specification | `TLM HMI` | `hmi`、`refer`、`specification` |
| `SWE-PM-039` | 1/2 | Ignition Off event occurs, according to par | **無** | `accord`、`occur`、`par` |

## 桶 `已由他條或他 leaf 涵蓋` —— 47 支，抽樣 8 支（17.0% ≥ 16.7%）

| leaf | 組/支 | 分支文字 | 具名標的 | 觸發未覆蓋之詞 |
|---|---|---|---|---|
| `SWE-PM-073` | 1/2 | BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Cr | `BODY OFF-TIMED`、`STATUS_LIN.Batt_ST_Crit`、`[1h]` | `mimimize`、`only`、`receiv`、`withdraw` |
| `SWE-PM-057` | 3/1 | the user can select SwitchOff_Timeout_Setting.Req to "00 min | `SwitchOff_Timeout_Setting.Req`、`00` | `user` |
| `SWE-PM-057` | 6/2 | 180 minutes" respectively. | `180` | `respectively.` |
| `SWE-PM-057` | 9/1 | the user can select SwitchOff_Timeout_Setting.Req to "00 min | `SwitchOff_Timeout_Setting.Req`、`00` | `user` |
| `SWE-PM-057` | 12/2 | 60 minutes" respectively. | `60` | `respectively.` |
| `SWE-PM-014` | 2/1 | it passes to TLM Timed state.In this case, TLM has to stay i | `Phone_Call.Info`、`Not_Active` | `case`、`equal`、`state.in`、`thi` |
| `SWE-PM-018` | 1/2 | to "Ignition Off" valueTHENTLM has to set TLM_Status.Info | `TLM_Status.Info` | `set`、`valuethentlm` |
| `SWE-PM-046` | 1/2 | Not_Successfully", TLM shall provide audio | `Not_Successfully` | `provide` |

## 機械落入 `真缺口` 而經裁決改桶者 —— 1 支

| leaf | 組/支 | 缺之標的 | 改判為 | 理由 |
|---|---|---|---|---|
| `SWE-PM-031` | 1/1 | `PROXI` | `已由他條或他 leaf 涵蓋` | 缺之標的為 `PROXI`，係該參數之**類別名**而非獨立標的；其所指之參數 `Rear_View_Camera` 已逐字見於 `NR1L-PowerManagement-105` 前提第 2 條（`Rear_View_Camera reads "Present"`），而 `show or not` 兩支分別由該 TC 之 ER 1 / ER 2 承擔。 |

## 本包裁為 `真缺口` 並已補 TC 者 —— 1 支

- `SWE-PM-030` 組 1 支 2 —— `SWE-PM-030` 僅一條 TC（`NR1L-PowerManagement-104`），其前提為 `Auto_SwitchOn_Setting.Req reads "Active"` —— 即 OR 之**左支**。右支 `Auto_SwitchOn_Setting.Req == Recall_Last AND VPLastStatus == On` 無任何 TC 覆蓋。**此即「原文以 OR 並列而 TC 只取其一」之同型**，且係由 G113 於現況資料上前瞻攔下（承第八、第九例，為**第十例**）。依 R-P118(d) 裁為真缺口，**已補 `NR1L-PowerManagement-105`**（第三批 63 → 64；其後二條之臨時號順移）。

**補前分支總數 75、真缺口 1，真陽性率 1.3%**（23 包為 2 / 55 = 3.6%）。補後如上表。

## 桶 `真缺口` —— 0 支（逐項完整，無抽樣）

**無。**
