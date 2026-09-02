# b1_epb — pilot 產出索引（EPB Maintenance Mode）

## **b1 FROZEN (R-VL23)** — 2026-09-02

凍結後任何變更**須新裁決**（R-VL23(d)）。凍結時之狀態：
- req_id（＝leaf）：**17**　TC 總數：**17**　檔數：**35**
- PENDING 項：**6**（錨 DR-VL4）
- E38–E45／E53–E56 於凍結前重跑：**全過**（E56 = 17／17）
- **未寫工作簿、未建 `delivered/`**；寫回工法待另包（R-VL22(e)）

生成 05 ／ 修訂 06（REV-1／2／4）／ 微修 07（R-VL22）／ 收尾 08（R-VL23 A 路）。

**族內一致選擇（R-VL21(f)）**：Fdbk 族之回讀步一律削去，無例外。
**歸類（R-VL22(c)，量測後定）**：`-048`〜`-052` 進入側；`-055`〜`-057` 退出側；
**`-054` in-mode 狀態回報型**（段 1092–1096 掃 `entering|exiting|request` 命中 0；對照 1066／1099 有詞）。

| req_id | D 欄（Source Requirement ID） | 修訂輪 | TC | tc_title | prio | design_method | PEND |
|---|---|---|---|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-044` | `Sys-RA-VF665_V42_VSM-723` | — | 1 | EPB Maintenance Mode menu hidden when PROXI is Absent | P2 | 負向測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-045` | `Sys-RA-VF665_V42_VSM-724` | — | 1 | EPB Maintenance Mode menu shown when PROXI is Present | P2 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-046` | `Sys-RA-VF665_V42_VSM-725` | 06+07 | 1 | EPB Maintenance Mode enabled from HMI → request sent and Initializing popup shown | P1 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-047` | `Sys-RA-VF665_V42_VSM-728` | — | 1 | IPC EPB_MaintenanceMode Off → On | P1 | 狀態轉換 | 0 |
| `SWE1-VC-EPBMaintenanceMode-048` | `Sys-RA-VF665_V42_VSM-729` | 06 | 1 | EPB Maintenance feedback = 2: Vehicle speed is not 0 mph | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-049` | `Sys-RA-VF665_V42_VSM-730` | 06 | 1 | EPB Maintenance feedback = 3: Vehicle is not in Park or Neutral | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-050` | `Sys-RA-VF665_V42_VSM-731` | 06 | 1 | EPB Maintenance feedback = 4: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-051` | `Sys-RA-VF665_V42_VSM-732` | 06 | 1 | EPB Maintenance feedback = 5: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-052` | `Sys-RA-VF665_V42_VSM-733` | 06 | 1 | EPB Maintenance feedback = 6: Brake pedal is currently pressed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-053` | `Sys-RA-VF665_V42_VSM-734` | 07 | 1 | No IPC response before T_EPB_MM expires | P1 | 基礎故障注入 | 0 |
| `SWE1-VC-EPBMaintenanceMode-054` | `Sys-RA-VF665_V42_VSM-735` | 06+07 | 1 | EPB Maintenance feedback = 8: park brake retracted | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-055` | `Sys-RA-VF665_V42_VSM-736` | 06 | 1 | EPB Maintenance feedback = 9: vehicle speed not zero on exit | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-056` | `Sys-RA-VF665_V42_VSM-737` | 06 | 1 | EPB Maintenance feedback = 10: exit blocked while vehicle in motion | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-057` | `Sys-RA-VF665_V42_VSM-738` | 06 | 1 | EPB Maintenance feedback = 11: exit process completed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-058` | `Sys-RA-VF665_V42_VSM-739` | — | 1 | EPB Maintenance Mode active state forwarded to the display controller | P2 | 功能測試 | 2 |
| `SWE1-VC-EPBMaintenanceMode-059` | `Sys-RA-VF665_V42_VSM-740` | 08 | 1 | Vehicle speed crosses V_Car_Moving upward | P1 | 邊界值分析 | 2 |
| `SWE1-VC-EPBMaintenanceMode-060` | `Sys-RA-VF665_V42_VSM-741` | — | 1 | Vehicle Setup menu updated on EPB_MaintenanceMode message reception | P2 | 狀態轉換 | 2 |

## 凍結檔表（sha256 前 8 碼）

| 檔 | sha256[:8] |
|---|---|
| `SWE1-VC-EPBMaintenanceMode-044.json` | `02e1fb74` |
| `SWE1-VC-EPBMaintenanceMode-044.md` | `8e19a191` |
| `SWE1-VC-EPBMaintenanceMode-045.json` | `843fb429` |
| `SWE1-VC-EPBMaintenanceMode-045.md` | `e9ec541a` |
| `SWE1-VC-EPBMaintenanceMode-046.json` | `82091592` |
| `SWE1-VC-EPBMaintenanceMode-046.md` | `4f37e562` |
| `SWE1-VC-EPBMaintenanceMode-047.json` | `b112d9ba` |
| `SWE1-VC-EPBMaintenanceMode-047.md` | `112bb083` |
| `SWE1-VC-EPBMaintenanceMode-048.json` | `3b4303a1` |
| `SWE1-VC-EPBMaintenanceMode-048.md` | `268ebed7` |
| `SWE1-VC-EPBMaintenanceMode-049.json` | `e46408e1` |
| `SWE1-VC-EPBMaintenanceMode-049.md` | `4cb8d533` |
| `SWE1-VC-EPBMaintenanceMode-050.json` | `17114b92` |
| `SWE1-VC-EPBMaintenanceMode-050.md` | `1fe69be7` |
| `SWE1-VC-EPBMaintenanceMode-051.json` | `94dd9fed` |
| `SWE1-VC-EPBMaintenanceMode-051.md` | `bca8f736` |
| `SWE1-VC-EPBMaintenanceMode-052.json` | `0cb58c48` |
| `SWE1-VC-EPBMaintenanceMode-052.md` | `ae373d51` |
| `SWE1-VC-EPBMaintenanceMode-053.json` | `e87ffd3b` |
| `SWE1-VC-EPBMaintenanceMode-053.md` | `aba1ff41` |
| `SWE1-VC-EPBMaintenanceMode-054.json` | `8d23aaea` |
| `SWE1-VC-EPBMaintenanceMode-054.md` | `081104fc` |
| `SWE1-VC-EPBMaintenanceMode-055.json` | `1c573252` |
| `SWE1-VC-EPBMaintenanceMode-055.md` | `c9350796` |
| `SWE1-VC-EPBMaintenanceMode-056.json` | `0fa76d57` |
| `SWE1-VC-EPBMaintenanceMode-056.md` | `70c2038e` |
| `SWE1-VC-EPBMaintenanceMode-057.json` | `b0606d69` |
| `SWE1-VC-EPBMaintenanceMode-057.md` | `9ab06b5a` |
| `SWE1-VC-EPBMaintenanceMode-058.json` | `a1e0ff42` |
| `SWE1-VC-EPBMaintenanceMode-058.md` | `84d67318` |
| `SWE1-VC-EPBMaintenanceMode-059.json` | `7abc9589` |
| `SWE1-VC-EPBMaintenanceMode-059.md` | `638973e6` |
| `SWE1-VC-EPBMaintenanceMode-060.json` | `ca9ec0a0` |
| `SWE1-VC-EPBMaintenanceMode-060.md` | `86b23ea1` |

> `INDEX.md`（本檔）不入表 —— 其內容含本表，自指。

## §9 自檢彙總（機讀可判項，17 條；凍結前重跑）

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

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-058` | test_procedure | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-058` | expected_result | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | test_procedure | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | expected_result | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |

## 凍結時之未結（皆已具名，不阻塞凍結）

§K K-1（Fdbk 2–11 無 `VAL_` label，影響 9 條）／K-2（Fdbk 4 與 5 規格同文）／
K-3（`-059` ignition 分支無合法訊號名）／K-4（規格拼字瑕疵）／
K-5（退出側請求路徑規格未載）／K-6（`-054` 歸屬 —— 已由 R-VL22(c) 量測定案）。
DR-VL1／DR-VL2／DR-VL4 皆已登記未送出（Pei 裁先不送）。
