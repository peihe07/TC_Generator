# b2_park_sense — 產出索引（Park Sense，18 leaf）

下放包 11 生成／**下放包 12 錨層修訂（R-VL26(b) 雙錨）／本輪 J・R 兩缺陷修訂**。
**已寫入累積簿 `sandbox/b2/vsm42_b1b2.xlsx`（b1＋b2 共 35 列），未出貨。**

- req_id：**18**　TC：**18**　PENDING：**6**（錨 DR-VL4）
- 工作簿列 **10–27**（037 leaf 序在前，EPB 之 b1 移至 28–44）

| req_id | 列 | TC ID | 家族 | tc_title | prio | design_method | spec_ref | PEND |
|---|---|---|---|---|---|---|---|---|
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-002` | 10 | `NR1L-VSM42-001` | PARK SENSE w/o HC.1 and  | Park Sense Setting menu shown when PAM node is Present | P2 | 功能測試 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-003` | 11 | `NR1L-VSM42-002` | PARK SENSE w/o HC.1 and  | PAM Alert Mode set to Sound | P2 | 等價劃分 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-004` | 12 | `NR1L-VSM42-003` | PARK SENSE w/o HC.1 and  | PAM Alert Mode set to Sound+Display | P2 | 等價劃分 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | 13 | `NR1L-VSM42-004` | PARK SENSE w/o HC.1 and  | Alert Mode display follows the IPC reported value | P2 | 狀態轉換 | 章節號 | 2 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-006` | 14 | `NR1L-VSM42-005` | PARK SENSE w/o HC.1 and  | Park Sense Setting menu shown when PAM node is Present | P2 | 功能測試 | 章節號 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-008` | 15 | `NR1L-VSM42-006` | Rear Park Sense Volume/  | Rear Park Sense Volume menu shown for the matching PAM configuration | P2 | 決策表 | 雙錨 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-009` | 16 | `NR1L-VSM42-007` | Rear Park Sense Volume/  | Rear Park Sense Volume set to Low | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-010` | 17 | `NR1L-VSM42-008` | Rear Park Sense Volume/  | Rear Park Sense Volume set to Med | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-011` | 18 | `NR1L-VSM42-009` | Rear Park Sense Volume/  | Rear Park Sense Volume set to High | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | 19 | `NR1L-VSM42-010` | Rear Park Sense Volume/  | Rear volume display follows the IPC reported value | P2 | 狀態轉換 | 雙錨 | 2 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-013` | 20 | `NR1L-VSM42-011` | Rear Park Sense Volume/  | Rear Park Sense Volume menu hidden when unsupported | P2 | 負向測試 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-015` | 21 | `NR1L-VSM42-012` | Front Park Sense Volume | Front Park Sense Volume menu shown for the matching PAM configuration | P2 | 決策表 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-016` | 22 | `NR1L-VSM42-013` | Front Park Sense Volume | Front Park Sense Volume set to Low | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-017` | 23 | `NR1L-VSM42-014` | Front Park Sense Volume | Front Park Sense Volume set to Med | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-018` | 24 | `NR1L-VSM42-015` | Front Park Sense Volume | Front Park Sense Volume set to High | P2 | 等價劃分 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-019` | 25 | `NR1L-VSM42-016` | Front Park Sense Volume | Front volume display follows the IPC reported value | P2 | 狀態轉換 | 雙錨 | 2 |
| `SWE1-VC-FrontParkSenseVolume-020` | 26 | `NR1L-VSM42-017` | Front Park Sense Volume | Front Park Sense Volume menu hidden when unsupported | P2 | 負向測試 | 雙錨 | 0 |
| `SWE1-VC-FrontParkSenseVolume-021` | 27 | `NR1L-VSM42-018` | Front Park Sense Volume | All three Park Sense menu items hidden when PAM node is Absent | P2 | 負向測試 | 雙錨 | 0 |

## 自檢（18 條，本輪重跑）

| 項 | 結果 |
|---|---|
| E38 覆蓋 18/18 | PASS |
| E39 R-S4（含全批不重複） | PASS |
| E40 尾句號 | PASS |
| E41 `[..]`/`'..'`/`<..>` | PASS |
| E42 `$..$` 皆解得 | PASS |
| E43 PENDING 格式 | PASS |
| E44 reasoning | PASS |
| E45 modal | PASS |
| C hedge | PASS |
| **E56 逐字全等 18/18** | PASS |
| E86′ 雙錨結構（Volume 13 條） | PASS |
| **J 行首大寫（含 `test_item` 兩半，本輪新增涵蓋）** | PASS |
| **R Pre-Condition 版面（本輪新增涵蓋）** | PASS |

## 本輪修訂（lint 實跑所揭，文字形預檢未涵蓋）

| req_id | 檢查 | 舊 | 新 |
|---|---|---|---|
| `-020`／`-021` | **J 行首大寫** | `test_item` 上半首字 `if`（自 037 句中起抄） | `If`（R-4 明許之排版正規化；E56 仍 18/18） |
| `-013` | **R Pre-Condition 多條件並列** | `PROXI PAM_Configuration = 1 (Front And Rear) is not set and the rear configuration is absent` | `The Rear Park Sense Volume feature is not supported by the vehicle configuration` |

> `-013` 之改法另揭一項**規格邏輯缺口**（§K K-9）：規格段 1217 之條件為
> `node 24 = Present AND (PAM_Configuration = Rear OR Front And Rear)`，而 `PAM_Configuration`
> 之值域**恰為該二值**，故該 AND 無法僅由 `PAM_Configuration` 否定 —— 其 ELSE 分支（段 1227–1228）
> 只能經 `node 24 ≠ Present` 到達，而那與 `-021` 之總 ELSE 重疊。037 只述「feature availability」
> 未指名 PROXI 值，故本條以功能可用性狀態表達，**不臆測 PROXI 組合**。

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-FrontParkSenseVolume-019` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-FrontParkSenseVolume-019` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
