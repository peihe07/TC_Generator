# B4 — G28 `SIGNALS` 正則調校（R-P57 / G35）

> 依 R-P57：自 037 之 `Verification Criteria` / `Verification Method` 兩欄
> 抽取全部 token，統計命名形態分布，據此重新推導識別式。
> 產生指令：`python features/power/scripts/build_b4_signals.py`

## 1. 命名形態分布（母體：115 leaf 之 VC + VM）

| 形態 | token 數 | 樣本（前 6）|
|---|---|---|
| 全大寫 2–3 字 | **324** | `HU`×107、`SW`×21、`CAN`×19、`UI`×16、`HW`×15、`TLM`×15 |
| 點號分隔識別式 | **308** | `notification.`×14、`path.`×13、`actions.`×10、`displayed.`×9、`received.`×8、`shown.`×8 |
| `$SIGNAL$` | **105** | `$VC_VEH_BRAND$`×21、`$VC_VEH_LINE$`×15、`$VC_SpecialPKG$`×7、`$Themed_Sound$`×6、`$Day_Night_Mode$`×5、`$TBM_Present$`×5 |
| 底線識別式 | **72** | `Rear_Camera_Enable`×6、`LTM_OperationalModeSts`×6、`Recall_Last`×6、`Not_Active`×5、`Auto_SwitchOn`×5、`Not_Successful`×4 |
| 全大寫 4+ 字 | **43** | `ADAS`×7、`FOTA`×6、`GDPR`×5、`PROXI`×4、`BODY`×4、`SDARS`×4 |
| CamelCase | **18** | `RemStActvSts`×5、`CarPowerManager`×3、`RemStartFail`×2、`AtlLo`×2、`AtlMi`×2、`AtlHi`×2 |
| 字母尾接數字（如 `Timeout1`） | **12** | `Timeout1`×9、`Case1`×1、`Case2`×1、`Case3`×1 |
| 點號後接數字（如 `CS.00244`） | **1** | `CS.00244`×1 |

## 2. 調校前之漏網形態

調校前之 `SIGNALS` 涵蓋 `$SIGNAL$`、底線識別式、`大寫.識別式`、全大寫 4+ 字，
**漏掉三類**，恰為 06 包所見之 4 筆偽陰性：

| 漏網形態 | 實例 | 影響之 leaf |
|---|---|---|
| 字母尾接數字 | `Timeout1`（13 次）、`M240`（3）、`Case1`–`Case3` | `SWE-PM-065` |
| 點號後接數字 | `CS.00244`（1 次） | `SWE-PM-009` |
| 全大寫 2–3 字 | `HIL`、`TLM`、`ICS`、`RVC` … | `SWE-PM-071`、`SWE-PM-072` |

## 3. 調校內容

新增：

- `具名參數（字母尾接數字）` = `\b[A-Za-z]{3,}\d+\b`
- `具名訊號／參數` 之點號識別式放寬為 `\b[A-Za-z][A-Za-z0-9]*\.[A-Za-z0-9][A-Za-z0-9_.]*\b`
  （原式要求點號後為字母，故漏 `CS.00244`）
- `具名元件／畫面` 增列 `HIL`、`RVC`、`TBM`、`PDO`、`SOS`
- `操作動詞` 增列 `perform`、`observe`、`disconnect`、`log`

**同時新增排除規則 `DOMAIN_ONLY_ACRONYMS = {CAN, SW, HW, UI, EE, OEM}`** ——
此為調校之關鍵。全大寫 2–3 字共 324 個 token，若一律視為訊號，
判準所舉之反例「Vehicle equiped with CAN」會被誤判為可執行。
該類 token 命名了一個域或總線，**未陳述任何可設定之條件**，故不得單獨成為訊號。

## 4. G35 —— 調校前後之人工覆寫率

| | 覆寫筆數 | 覆寫率 |
|---|---|---|
| 調校前（06 包） | 6 / 115 | **5.2%** |
| **調校後（07 包）** | **0 / 115** | **0.0%** |

調校後之**純正則結果與含人工覆寫時完全相同** ——
4 筆偽陰性由新增之識別式自動命中，2 筆不可執行由 `DOMAIN_ONLY_ACRONYMS` 自動得出。
故 `OVERRIDES` 清空；原兩筆之判讀理由改存為 `NOTES`（**不影響判定**，僅供覆核）。

## 5. G28 基線是否改變

**未改變。**

| 判定層 | 調校前 | 調校後 |
|---|---|---|
| VC 單欄不可執行 | 2 / 115 | **2 / 115** |
| VM 單欄不可執行 | 0 / 115 | **0 / 115** |
| 二欄合觀不可執行 | 0 / 115 | **0 / 115** |

基線不變，故 **DR-PW7 之 Urgency 維持 Low**，G28 亦無須更新。

> 依 R-P57：基線在精度量化前維持有效，**但不得作為跨 feature 之通用基線**。
> 本次調校係依 037 之實際命名慣例推導，`DOMAIN_ONLY_ACRONYMS` 尤其是本案特有 ——
> 他 feature 之領域縮寫集合不同，套用前須重新推導。
