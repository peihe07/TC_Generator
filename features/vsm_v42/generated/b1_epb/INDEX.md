# b1_epb — pilot 產出索引（EPB Maintenance Mode）

下放包 05 生成／**下放包 06 修訂輪（R-VL21 REV-1／2／4）已套用**。
**產出止於文字形，未寫工作簿、未寫 delivered/。**

- req_id（＝leaf）：**17**　TC 總數：**17**
- PENDING 項：**6**
- Test Group：`Vehicle Setup Management R1 Low`　Test Set：`EPB Maintenance Mode`

**修訂輪之族內一致選擇（R-VL21(f) 末句）**：Fdbk 族九條之「回讀步」（`Read the signal … and check that it is <raw>`）**一律削去** —— 該步為測試員自送訊號後之回讀，
冗餘而不加值；全族一致，無例外。

| req_id | D 欄（Source Requirement ID） | 修訂 | TC 數 | tc_title | priority | design_method | PENDING |
|---|---|---|---|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-044` | `Sys-RA-VF665_V42_VSM-723` | —（逐字不動） | 1 | EPB Maintenance Mode menu hidden when PROXI is Absent | P2 | 負向測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-045` | `Sys-RA-VF665_V42_VSM-724` | —（逐字不動） | 1 | EPB Maintenance Mode menu shown when PROXI is Present | P2 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-046` | `Sys-RA-VF665_V42_VSM-725` | REV-1／2 | 1 | EPB Maintenance Mode enabled from HMI → request sent and Initializing popup shown | P1 | 情境 / 用例 | 0 |
| `SWE1-VC-EPBMaintenanceMode-047` | `Sys-RA-VF665_V42_VSM-728` | —（逐字不動） | 1 | IPC EPB_MaintenanceMode Off → On | P1 | 狀態轉換 | 0 |
| `SWE1-VC-EPBMaintenanceMode-048` | `Sys-RA-VF665_V42_VSM-729` | REV-4 | 1 | EPB Maintenance feedback = 2: Vehicle speed is not 0 mph | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-049` | `Sys-RA-VF665_V42_VSM-730` | REV-4 | 1 | EPB Maintenance feedback = 3: Vehicle is not in Park or Neutral | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-050` | `Sys-RA-VF665_V42_VSM-731` | REV-4 | 1 | EPB Maintenance feedback = 4: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-051` | `Sys-RA-VF665_V42_VSM-732` | REV-4 | 1 | EPB Maintenance feedback = 5: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-052` | `Sys-RA-VF665_V42_VSM-733` | REV-4 | 1 | EPB Maintenance feedback = 6: Brake pedal is currently pressed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-053` | `Sys-RA-VF665_V42_VSM-734` | —（逐字不動） | 1 | No IPC response before T_EPB_MM expires | P1 | 基礎故障注入 | 0 |
| `SWE1-VC-EPBMaintenanceMode-054` | `Sys-RA-VF665_V42_VSM-735` | REV-4 | 1 | EPB Maintenance feedback = 8: park brake retracted | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-055` | `Sys-RA-VF665_V42_VSM-736` | REV-4 | 1 | EPB Maintenance feedback = 9: vehicle speed not zero on exit | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-056` | `Sys-RA-VF665_V42_VSM-737` | REV-4 | 1 | EPB Maintenance feedback = 10: exit blocked while vehicle in motion | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-057` | `Sys-RA-VF665_V42_VSM-738` | REV-4 | 1 | EPB Maintenance feedback = 11: exit process completed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-058` | `Sys-RA-VF665_V42_VSM-739` | —（逐字不動） | 1 | EPB Maintenance Mode active state forwarded to the display controller | P2 | 功能測試 | 2 |
| `SWE1-VC-EPBMaintenanceMode-059` | `Sys-RA-VF665_V42_VSM-740` | —（逐字不動） | 1 | Vehicle speed crosses V_Car_Moving upward | P1 | 邊界值分析 | 2 |
| `SWE1-VC-EPBMaintenanceMode-060` | `Sys-RA-VF665_V42_VSM-741` | —（逐字不動） | 1 | Vehicle Setup menu updated on EPB_MaintenanceMode message reception | P2 | 狀態轉換 | 2 |

## §9 自檢彙總（機讀可判項，17 條全數；修訂後重跑）

| 項 | 結果 |
|---|---|
| 1 Test Set 名詞片語、與 framework 一致 | PASS |
| 2 tc_title 2–14 words、無 modal | PASS |
| 3 Pre-Condition 只收狀態 | PASS |
| 4 input_test_data = NA | PASS |
| 5 無禁用動詞（Procedure 可執行） | PASS |
| 6 步驟數 ≥2（§10.5） | PASS |
| 10 Procedure ↔ ER 1:1 | PASS |
| 12 traces to Req（spec_reference 非空） | PASS |
| 13 design_method 為下拉詞彙 | PASS |
| 14 四欄無尾句號 | PASS |
| 15 UI 標籤用 "..." | PASS |
| 16 spec_reference 列出所驗章節 | PASS |
| §10.2 priority ∈ P0–P3 | PASS |
| §10.1 十鍵齊全 | PASS |

**未過項：0。**

> 人判項（§9 之 7 標準片段／8 CLI／9 baseline／11 FP-FF）本批無適用對象，未列。

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-058` | test_procedure | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-058` | expected_result | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | test_procedure | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | expected_result | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
