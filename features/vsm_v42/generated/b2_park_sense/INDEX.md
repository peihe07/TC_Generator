# b2_park_sense — 產出索引（Park Sense，18 leaf）

下放包 11／R-VL25(a)。**綠色通道計數之第一批。** 產出止於文字形，未寫工作簿。

- req_id（＝leaf）：**18**　TC 總數：**18**
- PENDING 項：**6**（錨 DR-VL4）
- Test Group：`Vehicle Setup Management R1 Low`　Test Set：`Park Sense`

**spec_reference 二型（R-VL19(b)）**：PARK SENSE 家族 5 條用章節號 `…_1.11.1.1.29`；
Volume 二家族 13 條用上游實名 `Sys-RA-VF665_V42_VSM-{nnn}`（規格無該二家族之章節標題）。

| req_id | D 欄（Source Requirement ID） | 家族 | TC | tc_title | prio | design_method | spec_ref 型 | PEND |
|---|---|---|---|---|---|---|---|---|
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-002` | `Sys-RA-VF665_V42_VSM-790` | PARK SENSE w/o HC.1 and PA | 1 | Park Sense Setting menu shown when PAM node is Present | P2 | 功能測試 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-003` | `Sys-RA-VF665_V42_VSM-791` | PARK SENSE w/o HC.1 and PA | 1 | PAM Alert Mode set to Sound | P2 | 等價劃分 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-004` | `Sys-RA-VF665_V42_VSM-792` | PARK SENSE w/o HC.1 and PA | 1 | PAM Alert Mode set to Sound+Display | P2 | 等價劃分 | 章節號 | 0 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | `Sys-RA-VF665_V42_VSM-793` | PARK SENSE w/o HC.1 and PA | 1 | Alert Mode display follows the IPC reported value | P2 | 狀態轉換 | 章節號 | 2 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-006` | `Sys-RA-VF665_V42_VSM-794` | PARK SENSE w/o HC.1 and PA | 1 | Park Sense Setting menu shown when PAM node is Present | P2 | 功能測試 | 章節號 | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-008` | `Sys-RA-VF665_V42_VSM-796` | Rear Park Sense Volume/ Pa | 1 | Rear Park Sense Volume menu shown for the matching PAM configuration | P2 | 決策表 | Sys-RA | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-009` | `Sys-RA-VF665_V42_VSM-797` | Rear Park Sense Volume/ Pa | 1 | Rear Park Sense Volume set to Low | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-010` | `Sys-RA-VF665_V42_VSM-798` | Rear Park Sense Volume/ Pa | 1 | Rear Park Sense Volume set to Med | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-011` | `Sys-RA-VF665_V42_VSM-799` | Rear Park Sense Volume/ Pa | 1 | Rear Park Sense Volume set to High | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | `Sys-RA-VF665_V42_VSM-800` | Rear Park Sense Volume/ Pa | 1 | Rear volume display follows the IPC reported value | P2 | 狀態轉換 | Sys-RA | 2 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-013` | `Sys-RA-VF665_V42_VSM-801` | Rear Park Sense Volume/ Pa | 1 | Rear Park Sense Volume menu hidden when unsupported | P2 | 負向測試 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-015` | `Sys-RA-VF665_V42_VSM-803` | Front Park Sense Volume | 1 | Front Park Sense Volume menu shown for the matching PAM configuration | P2 | 決策表 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-016` | `Sys-RA-VF665_V42_VSM-804` | Front Park Sense Volume | 1 | Front Park Sense Volume set to Low | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-017` | `Sys-RA-VF665_V42_VSM-805` | Front Park Sense Volume | 1 | Front Park Sense Volume set to Med | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-018` | `Sys-RA-VF665_V42_VSM-806` | Front Park Sense Volume | 1 | Front Park Sense Volume set to High | P2 | 等價劃分 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-019` | `Sys-RA-VF665_V42_VSM-807` | Front Park Sense Volume | 1 | Front volume display follows the IPC reported value | P2 | 狀態轉換 | Sys-RA | 2 |
| `SWE1-VC-FrontParkSenseVolume-020` | `Sys-RA-VF665_V42_VSM-808` | Front Park Sense Volume | 1 | Front Park Sense Volume menu hidden when unsupported | P2 | 負向測試 | Sys-RA | 0 |
| `SWE1-VC-FrontParkSenseVolume-021` | `Sys-RA-VF665_V42_VSM-809` | Front Park Sense Volume | 1 | All three Park Sense menu items hidden when PAM node is Absent | P2 | 負向測試 | Sys-RA | 0 |

## 自檢彙總（機讀，18 條）

| 項 | 結果 |
|---|---|
| E38 覆蓋 18/18 | PASS |
| E39 R-S4 括號下半（含全批不重複） | PASS |
| E40 尾句號 | PASS |
| E41 [..]/'..'/<..> | PASS |
| E42 $..$ 皆可回溯 v3 解得 | PASS |
| E43 PENDING 格式 | PASS |
| E44 reasoning 2–5 句繁中 | PASS |
| E45 ER／下半 modal | PASS |
| **C hedge（b1 教訓，本批新增）** | PASS |
| **E56 逐字全等 18/18** | PASS |
| E86 Volume 13 條 spec_ref 全為 Sys-RA | PASS |
| J 行首大寫／K CJK／Q 不可見字元／V 行首空白／M 空欄 | PASS |
| Procedure↔ER 1:1／步驟數 ≥2／tc_title 2–14 words | PASS |
| bus-error 式限測試員送出步 | PASS |

**未過項：0。**

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-RearParkSenseVolume/ParkSenseVolume-012` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-FrontParkSenseVolume-019` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-FrontParkSenseVolume-019` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
