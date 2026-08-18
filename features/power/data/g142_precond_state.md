# G142 —— `pre_conditions` 之狀態值依據（R-P210）

> 判準見 `scripts/audit_precond_state.py` docstring —— **先寫定後執行**。
> 比對採空白摺除與大小寫不敏感之**字面**正規化，非語義推定；
> 正規化後仍不命中者一律列為 (b)，由人判其依據。

## 計數

| 類 | 數 | 佔比 |
|---|---|---|
| (a) 狀態值逐字見於 clause | **244** | 92.4% |
| **(b) 有狀態值未見於 clause** | **20** | 7.6% |
| **合計** | **264** | 100% |

## (b) 型逐項表（G147 / R-P217）

> 欄位依 R-P217：`tc_id` / `leaf` / **前提行逐字** / 該狀態值是否見於 clause / 執行層所載之選擇依據 / 待驗行為是否隨該狀態而異。
> **前提行為逐字轉錄，未經改寫**；後二欄取自該 leaf 之 `reasoning`。

| # | tc_id | leaf | 前提行（逐字）| 見於 clause | 選擇依據 | 行為隨狀態而異 |
|---|---|---|---|---|---|---|
| 1 | `NR1L-PowerManagement-018` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 2 | `NR1L-PowerManagement-019` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 3 | `NR1L-PowerManagement-020` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 4 | `NR1L-PowerManagement-021` | `SWE-PM-060` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 5 | `NR1L-PowerManagement-022` | `SWE-PM-060` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 6 | `NR1L-PowerManagement-024` | `SWE-PM-061` | `1. The TLM is in Timed status` | **否**（`Timed`）| 否定側需一非 Full-Operation 狀態；`Timed` 為 §E 既有狀態 | **是，而本條所驗即該差異**；規格僅二分，取任一即足 |
| 7 | `NR1L-PowerManagement-025` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 8 | `NR1L-PowerManagement-026` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 9 | `NR1L-PowerManagement-027` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 10 | `NR1L-PowerManagement-030` | `SWE-PM-064` | `2. The TLM is in Timed state` | **否**（`Timed`）| 他 leaf 之定義 —— `Timeout1` 之計時與到期依 `SWE-PM-038` / `063` 發生於 Timed | **規格未載** —— 依據為他 leaf 明文而非推定，故不列待查（**R-P218 送複核**） |
| 11 | `NR1L-PowerManagement-076` | `SWE-PM-019` | `3. Rear_Camera_Enable.Info reads "False"` | **否**（`False`）| clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值 | **是**，二分支皆已成條 |
| 12 | `NR1L-PowerManagement-078` | `SWE-PM-019` | `3. Rear_Camera_Enable.Info reads "False"` | **否**（`False`）| clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值 | **是**，二分支皆已成條 |
| 13 | `NR1L-PowerManagement-098` | `SWE-PM-027` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| clause 之「set … **back to** `False`」蘊含起始為 `True` | **是** —— 起始若已為 `False` 則無可觀察變化 |
| 14 | `NR1L-PowerManagement-099` | `SWE-PM-027` | `3. Antitheft_Activation.Req reads "True"` | **否**（`True`）| clause 之「set … **back to** `False`」蘊含起始為 `True` | **是** —— 起始若已為 `False` 則無可觀察變化 |
| 15 | `NR1L-PowerManagement-100` | `SWE-PM-028` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 16 | `NR1L-PowerManagement-102` | `SWE-PM-028` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 17 | `NR1L-PowerManagement-104` | `SWE-PM-029` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 18 | `NR1L-PowerManagement-107` | `SWE-PM-029` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 19 | `NR1L-PowerManagement-110` | `SWE-PM-031` | `3. The TLM is in Standby state` | **否**（`Standby`）| 測試可執行性需一具體狀態；`Standby` 為 §E 既有狀態 | **否** —— clause 逐字載 `regardless of TLM_Status.Info and $Telematic_Power$ value` |
| 20 | `NR1L-PowerManagement-187` | `SWE-PM-094` | `2. The HU is in STANDBY MODE` | **否**（`STANDBY`、`MODE`）| 他 leaf 明文 —— `SWE-PM-093` 列三模式，此為其一 | **無法說明** —— clause 一字未載；已標待查並開 **DR-PW14** |
