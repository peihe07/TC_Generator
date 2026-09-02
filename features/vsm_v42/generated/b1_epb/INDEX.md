# b1_epb — pilot 產出索引（EPB Maintenance Mode）

下放包 05 生成／06 修訂（REV-1／2／4）／**07 微修（R-VL22）**。
**產出止於文字形，未寫工作簿、未寫 delivered/。**

- req_id（＝leaf）：**17**　TC 總數：**17**
- PENDING 項：**6**
- Test Group：`Vehicle Setup Management R1 Low`　Test Set：`EPB Maintenance Mode`

**族內一致選擇（R-VL21(f) 末句）**：Fdbk 族之回讀步一律削去，無例外。

**歸類（R-VL22(c)，量測後定）**：`-048`〜`-052` 進入側（發起步 `= "On"`）；
`-055`〜`-057` 退出側（發起步 `= "Off"`）；**`-054` in-mode 狀態回報型（無發起步）** ——
規格段 1092–1096 掃 `entering|exiting|request` 命中 0（對照段 1066 有 `entering`、1099 有 `exiting`）。

| req_id | D 欄（Source Requirement ID） | 修訂輪 | TC 數 | tc_title | priority | design_method | PENDING |
|---|---|---|---|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-044` | `Sys-RA-VF665_V42_VSM-723` | —（逐字不動） | 1 | EPB Maintenance Mode menu hidden when PROXI is Absent | P2 | 負向測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-045` | `Sys-RA-VF665_V42_VSM-724` | —（逐字不動） | 1 | EPB Maintenance Mode menu shown when PROXI is Present | P2 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-046` | `Sys-RA-VF665_V42_VSM-725` | 06 REV-1／2＋07 | 1 | EPB Maintenance Mode enabled from HMI → request sent and Initializing popup shown | P1 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-047` | `Sys-RA-VF665_V42_VSM-728` | —（逐字不動） | 1 | IPC EPB_MaintenanceMode Off → On | P1 | 狀態轉換 | 0 |
| `SWE1-VC-EPBMaintenanceMode-048` | `Sys-RA-VF665_V42_VSM-729` | 06 REV-4 | 1 | EPB Maintenance feedback = 2: Vehicle speed is not 0 mph | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-049` | `Sys-RA-VF665_V42_VSM-730` | 06 REV-4 | 1 | EPB Maintenance feedback = 3: Vehicle is not in Park or Neutral | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-050` | `Sys-RA-VF665_V42_VSM-731` | 06 REV-4 | 1 | EPB Maintenance feedback = 4: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-051` | `Sys-RA-VF665_V42_VSM-732` | 06 REV-4 | 1 | EPB Maintenance feedback = 5: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-052` | `Sys-RA-VF665_V42_VSM-733` | 06 REV-4 | 1 | EPB Maintenance feedback = 6: Brake pedal is currently pressed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-053` | `Sys-RA-VF665_V42_VSM-734` | 07 | 1 | No IPC response before T_EPB_MM expires | P1 | 基礎故障注入 | 0 |
| `SWE1-VC-EPBMaintenanceMode-054` | `Sys-RA-VF665_V42_VSM-735` | 06 REV-4＋07 | 1 | EPB Maintenance feedback = 8: park brake retracted | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-055` | `Sys-RA-VF665_V42_VSM-736` | 06 REV-4 | 1 | EPB Maintenance feedback = 9: vehicle speed not zero on exit | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-056` | `Sys-RA-VF665_V42_VSM-737` | 06 REV-4 | 1 | EPB Maintenance feedback = 10: exit blocked while vehicle in motion | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-057` | `Sys-RA-VF665_V42_VSM-738` | 06 REV-4 | 1 | EPB Maintenance feedback = 11: exit process completed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-058` | `Sys-RA-VF665_V42_VSM-739` | —（逐字不動） | 1 | EPB Maintenance Mode active state forwarded to the display controller | P2 | 功能測試 | 2 |
| `SWE1-VC-EPBMaintenanceMode-059` | `Sys-RA-VF665_V42_VSM-740` | —（逐字不動） | 1 | Vehicle speed crosses V_Car_Moving upward | P1 | 邊界值分析 | 2 |
| `SWE1-VC-EPBMaintenanceMode-060` | `Sys-RA-VF665_V42_VSM-741` | —（逐字不動） | 1 | Vehicle Setup menu updated on EPB_MaintenanceMode message reception | P2 | 狀態轉換 | 2 |

## §9 自檢彙總（機讀可判項，17 條；07 後重跑）

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

**未過項：0。** 人判項（§9 之 7／8／9／11）本批無適用對象，未列。

## 已知未結（凍結前須裁）

- **E56 = 16／17**：`-059` 之 `test_item` 上半非逐字（ignition 子句被剪接），修法已備妥，
  惟該條不在下放包 07 之修訂範圍（E53：其餘 diff = 0），故未改。詳見 `docs/upstream/07_b1_freeze.md`。

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-058` | test_procedure | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-058` | expected_result | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | test_procedure | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | expected_result | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
