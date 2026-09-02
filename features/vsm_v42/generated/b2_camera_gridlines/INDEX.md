# b2_camera_gridlines — 產出索引（Camera Gridlines，10 leaf）

下放包 13／R-VL27(f)。**綠色通道計數第二批。** 產出止於文字形，未寫工作簿。

- req_id：**10**　TC：**10**
- PENDING 項：**15**
- spec_reference **單錨章節號，二節各歸各**：Dynamic Gridlines → `…_1.11.1.1.31`（4 條）；Surround Camera Gridlines → `…_1.11.1.1.38`（6 條）

| req_id | D 欄 | 家族 | tc_title | prio | design_method | 章節 | PEND |
|---|---|---|---|---|---|---|---|
| `SWE1-VC-DynamicGridlines-029` | `Sys-RA-VF665_V42_VSM-817` | Dynamic Gridlines | Dynamic Grid setting hidden when rear camera PROXI is Absent | P2 | 負向測試 | 1.11.1.1.31 | 0 |
| `SWE1-VC-DynamicGridlines-030` | `Sys-RA-VF665_V42_VSM-818` | Dynamic Gridlines | Dynamic Grid setting shown when rear camera PROXI is Present | P2 | 功能測試 | 1.11.1.1.31 | 0 |
| `SWE1-VC-DynamicGridlines-031` | `Sys-RA-VF665_V42_VSM-819` | Dynamic Gridlines | Dynamic Grid set to Off | P2 | 等價劃分 | 1.11.1.1.31 | 2 |
| `SWE1-VC-DynamicGridlines-032` | `Sys-RA-VF665_V42_VSM-820` | Dynamic Gridlines | Dynamic Grid set to On | P2 | 等價劃分 | 1.11.1.1.31 | 2 |
| `SWE1-VC-SurroundCameraGridlines-063` | `Sys-RA-VF665_V42_VSM-857` | Surround Camera Gridline | Surround Camera Gridlines requirement text absent upstream | P3 | 功能測試 | 1.11.1.1.38 | 5 |
| `SWE1-VC-SurroundCameraGridlines-064` | `Sys-RA-VF665_V42_VSM-858` | Surround Camera Gridline | SVC Gridlines setting hidden when surround camera PROXI is Absent | P2 | 負向測試 | 1.11.1.1.38 | 0 |
| `SWE1-VC-SurroundCameraGridlines-065` | `Sys-RA-VF665_V42_VSM-859` | Surround Camera Gridline | SVC Gridlines setting shown when surround camera PROXI is Present | P2 | 功能測試 | 1.11.1.1.38 | 0 |
| `SWE1-VC-SurroundCameraGridlines-066` | `Sys-RA-VF665_V42_VSM-860` | Surround Camera Gridline | SVC Gridlines set to Off | P2 | 等價劃分 | 1.11.1.1.38 | 2 |
| `SWE1-VC-SurroundCameraGridlines-067` | `Sys-RA-VF665_V42_VSM-861` | Surround Camera Gridline | SVC Gridlines set to On | P2 | 等價劃分 | 1.11.1.1.38 | 2 |
| `SWE1-VC-SurroundCameraGridlines-068` | `Sys-RA-VF665_V42_VSM-862` | Surround Camera Gridline | SVC Gridlines display follows the IPC reported value | P2 | 狀態轉換 | 1.11.1.1.38 | 2 |

## 自檢（10 條，全項）

| 項 | 結果 |
|---|---|
| E38 覆蓋 10/10 | PASS |
| E39 R-S4（含全批不重複） | PASS |
| E40 尾句號 | PASS |
| E41 `[..]`/`'..'`/`<..>` | PASS |
| E42 `$..$` 皆解得 | PASS |
| E43 PENDING 格式 | PASS |
| E44 reasoning 2–5 句 | PASS |
| E45 modal | PASS |
| C hedge | PASS |
| **E56 逐字全等 10/10** | PASS |
| E86 型 spec_ref（4／6 各歸各節） | PASS |
| J（含 test_item 兩半）／K／Q／V／M | PASS |
| R PC 版面 | PASS |
| P↔ER 1:1／步驟≥2／tc_title 2–14w | PASS |
| bus-error 限測試員送出步 | PASS |
| §4.6 axis=none ⇔ duplicate_of | PASS |

**未過項：0。**

## 一列 BLOCKED（`-063`）

`SWE1-VC-SurroundCameraGridlines-063` 之 037 `Requirement Description` **只有家族標題**
「Surround Camera Gridlines」一句，**無需求文本**。依 §8.4.1 不造需求；依 privacy R34-3 之先例
**寫入一列而非略過** —— leaf 自交付件消失會在追溯表留下無說明之洞。
四欄全為 `PENDING: DR-VL2 …`，`priority` P3，`remarks` 記 BLOCKED 與其佐證
（其 Source ID 於 SYSRA 之 Category 為 `Heading`，A-VL7，兩者互相印證為上游誤標）。

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-DynamicGridlines-031` | test_procedure | `PENDING: DR-VL4 DynamicGrid.Req` | DR-VL4 |
| `SWE1-VC-DynamicGridlines-031` | expected_result | `PENDING: DR-VL4 DynamicGrid.Req` | DR-VL4 |
| `SWE1-VC-DynamicGridlines-032` | test_procedure | `PENDING: DR-VL4 DynamicGrid.Req` | DR-VL4 |
| `SWE1-VC-DynamicGridlines-032` | expected_result | `PENDING: DR-VL4 DynamicGrid.Req` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-063` | pre_conditions | `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` | DR-VL2 |
| `SWE1-VC-SurroundCameraGridlines-063` | test_procedure | `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` | DR-VL2 |
| `SWE1-VC-SurroundCameraGridlines-063` | test_procedure | `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` | DR-VL2 |
| `SWE1-VC-SurroundCameraGridlines-063` | expected_result | `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` | DR-VL2 |
| `SWE1-VC-SurroundCameraGridlines-063` | expected_result | `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` | DR-VL2 |
| `SWE1-VC-SurroundCameraGridlines-066` | test_procedure | `PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-066` | expected_result | `PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-067` | test_procedure | `PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-067` | expected_result | `PENDING: DR-VL4 TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-068` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-SurroundCameraGridlines-068` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
