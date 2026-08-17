# B5 — 037 `SWE1 Requirements` 各欄相異值數（R-P41(b)）

> G19 已證 18 欄皆 115/115 非空。**非空不等於有鑑別力** ——
> 相異值數 = 1 者與空欄之實際效果相同；≥ 100 者近乎逐列唯一，同樣無分群價值。
> 母體：r8–r145 之 115 個 leaf。
> 產生指令：`python features/power/scripts/build_b4_b5.py`

## 逐欄相異值數

| 欄 | 標頭 | 相異值數 | 鑑別力 | 值域 |
|---|---|---|---|---|
| c1 | SWE-Requirement ID | **115** | **無（近乎逐列唯一）** | `SWE-PM-001` ×1；`SWE-PM-002` ×1；`SWE-PM-003` ×1；`SWE-PM-004` ×1；…（共 115 值） |
| c2 | Source Requirement ID | **112** | **無（近乎逐列唯一）** | `Sys-RA-PM-0141` ×2；`Sys-RA-PM-0143` ×2；`Sys-RA-PM-0264` ×2；`Sys-RA-PM-0013
Sys-RA-PM-0` ×1；…（共 112 值） |
| c3 | Requirement  Title | **99** | 弱 | `Timeout` ×7；`Phone Call` ×5；`Splash Screen logo visuali` ×4；`Power down` ×3；…（共 99 值） |
| c4 | Requirement  Description | **115** | **無（近乎逐列唯一）** | `* HW supplier shall notify` ×1；`* HW supplier shall notify` ×1；`* HW supplier shall notify` ×1；`* HW supplier shall notify` ×1；…（共 115 值） |
| c5 | Release Version | **1** | **無（單一值）** | `1.0.0` ×115 |
| c6 | Categorization | **1** | **無（單一值）** | `Functional Requirement` ×115 |
| c7 | Sub Categorization | **5** | 可分群 | `HMI` ×36；`Service
HMI` ×35；`Service` ×27；`HMI Service` ×16；`HMI/Service` ×1 |
| c8 | Feasibility | **1** | **無（單一值）** | `Yes` ×115 |
| c9 | Description/Action for Feasibility | **54** | 弱 | `Feasible to implement by s` ×51；`Achievable via standard Ca` ×9；`HW supplier provides API t` ×4；`Settings Service can read ` ×1；…（共 54 值） |
| c10 | Impact | **3** | 可分群 | `Yes` ×53；`High` ×37；`No` ×25 |
| c11 | Description/Action for  Impact | **80** | 弱 | `Impacts user experience` ×35；`Standard registration patt` ×2；`NVM restoration at Init ex` ×1；`SW sub-components must sup` ×1；…（共 80 值） |
| c12 | Risk Factor | **2** | 可分群 | `Low` ×63；`Medium` ×52 |
| c13 | Description/Action for Risk Factor | **67** | 弱 | `Already implemented in oth` ×35；`Standard AAOS power state ` ×13；`Standard AAOS power state ` ×2；`Depends on correct retriev` ×2；…（共 67 值） |
| c14 | Reusable | **3** | 可分群 | `High` ×86；`None` ×22；`Low` ×7 |
| c15 | Description/Action for Reusable | **74** | 弱 | `Most of the code can be re` ×35；`Power state registration a` ×8；`NVM settings restoration p` ×1；`New custom power state. No` ×1；…（共 74 值） |
| c16 | Priority | **2** | 可分群 | `High` ×91；`Medium` ×24 |
| c17 | Verification Criteria | **74** | 弱 | `HU in Sleep or Standby sta` ×5；`HU in "Full-Operation"` ×4；`HU in standby or sleep sta` ×4；`HU in Partial operation` ×4；…（共 74 值） |
| c18 | Verification Method | **114** | **無（近乎逐列唯一）** | `User shall be able to sele` ×2；`Change Ingition from Off t` ×1；`Pres front panel on-off bu` ×1；`Change STATUS_BH_BCM2.RemS` ×1；…（共 114 值） |

## 相異值數 = 1 之欄位（3 欄）

| 欄 | 標頭 | 唯一值 |
|---|---|---|
| c5 | Release Version | `1.0.0` |
| c6 | Categorization | `Functional Requirement` |
| c8 | Feasibility | `Yes` |

**此類欄位在分批、優先級、追溯上與空欄實際效果相同。**

## 相異值數 ≥ 100 之欄位（4 欄）

| 欄 | 標頭 | 相異值數 |
|---|---|---|
| c1 | SWE-Requirement ID | 115 / 115 |
| c2 | Source Requirement ID | 112 / 115 |
| c4 | Requirement  Description | 115 / 115 |
| c18 | Verification Method | 114 / 115 |

**近乎逐列唯一，無分群價值**（作為內容來源仍有價值 —— 例如 Description 用於判讀）。

## 附：`Requirement Title` 與 §E「本分組之已知弱點」之對照

§E 該節稱：「037 `Requirement Title` 於 115 leaf 中出現 **20+ 種**，多數僅出現 1 次（`Timeout` 7、`Phone Call` 5 為**僅有例外**）」。

實測：相異值 **99** 種，僅出現 1 次者 **94** 種。出現 > 1 次者：

| 值 | 次數 |
|---|---|
| `Timeout` | 7 |
| `Phone Call` | 5 |
| `Splash Screen logo visualization` | 4 |
| `Power down` | 3 |
| `FOTA` | 2 |

即「20+ 種」大幅低估（實為 99 種），且「僅有例外」為誤 —— 除 `Timeout` 與 `Phone Call` 外另有 3 組重複值。
**§E 該節之結論（`Requirement Title` 無分組價值）不受影響，反而更強。**
