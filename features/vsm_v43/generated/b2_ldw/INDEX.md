# INDEX — b2_ldw（Pei 直接指示（無下放包））

Test Group：`Vehicle Setup Management R1L TBM`｜Test Set：`Lane Departure Warning`（R-VT24 十九組之第 7 組）

leaf **18**（`chapter_for_vf = 01.11.01.01.26`）｜TC 總數 **18**｜PENDING **0**

| req_id | TC 數 | tc_title | PENDING |
|---|---|---|---|
| `Sys-RA-VF665_V43_VSM-420` | 1 | Lanse Sense Warning 1 menu offers 2 options at half level 3 | 0 |
| `Sys-RA-VF665_V43_VSM-421` | 1 | Lanse Sense Warning 1 request sent for early selection | 0 |
| `Sys-RA-VF665_V43_VSM-422` | 1 | Lanse Sense Warning 1 request sent for late selection | 0 |
| `Sys-RA-VF665_V43_VSM-423` | 1 | Lanse Sense Warning 1 display updated on reception of LDW_Sensibility message | 0 |
| `Sys-RA-VF665_V43_VSM-424` | 1 | Lanse Sense Warning 2 menu offers 3 options at half level 2 | 0 |
| `Sys-RA-VF665_V43_VSM-425` | 1 | Lanse Sense Warning 2 request sent for early selection | 0 |
| `Sys-RA-VF665_V43_VSM-426` | 1 | Lanse Sense Warning 2 request sent for med selection | 0 |
| `Sys-RA-VF665_V43_VSM-427` | 1 | Lanse Sense Warning 2 request sent for late selection | 0 |
| `Sys-RA-VF665_V43_VSM-428` | 1 | Lanse Sense Warning 2 display updated on reception of LDW_Sensibility message | 0 |
| `Sys-RA-VF665_V43_VSM-430` | 1 | Lanse Sense Strenght 1 menu offers 2 options at half level 3 | 0 |
| `Sys-RA-VF665_V43_VSM-431` | 1 | Lanse Sense Strenght 1 request sent for low selection | 0 |
| `Sys-RA-VF665_V43_VSM-432` | 1 | Lanse Sense Strenght 1 request sent for high selection | 0 |
| `Sys-RA-VF665_V43_VSM-433` | 1 | Lanse Sense Strenght 1 display updated on reception of LDW_Intensity message | 0 |
| `Sys-RA-VF665_V43_VSM-434` | 1 | Lanse Sense Strenght 2 menu offers 3 options at half level 2 | 0 |
| `Sys-RA-VF665_V43_VSM-435` | 1 | Lanse Sense Strenght 2 request sent for low selection | 0 |
| `Sys-RA-VF665_V43_VSM-436` | 1 | Lanse Sense Strenght 2 request sent for med selection | 0 |
| `Sys-RA-VF665_V43_VSM-437` | 1 | Lanse Sense Strenght 2 request sent for high selection | 0 |
| `Sys-RA-VF665_V43_VSM-438` | 1 | Lanse Sense Strenght 2 display updated on reception of LDW_Intensity message | 0 |

## 自檢彙總（IN §9 十七項之機讀部分 ＋ E38–E45／E51／E52）

| 項 | 實測 | 判 |
|---|---|---|
| E38 覆蓋（18 leaf 各 ≥1 TC） | 18/18 | PASS |
| E39 R-S4 括號下半（每 TC 有；同 req_id 內不逐字相同） | 18/18 有；重複 0 | PASS |
| E40 尾句號違規 | 0 | PASS |
| E41 [...]／'...'／<...> UI 標籤 | 0 | PASS |
| E42 $…$ 之列全數可回溯 v5 解得 | 4 名：['IPC_VEHICLE_SETUP2.LDW_Intensity', 'IPC_VEHICLE_SETUP2.LDW_Sensibility', 'TELEMATIC_VEHICLE_SETUP2.LDW_Intensity_Req', 'TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req'] | PASS |
| E43 PENDING 格式 | 0 處 | PASS（本批 0，理由見上繳 §PENDING） |
| E44 reasoning（每 req_id 一則、繁中、2–5 句、含切分依據） | 18 則；句數 [3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4] | PASS |
| E45 modal 於 ER／test_item 下半 | 0 | PASS |
| E51 Remarks provisional 註 | 18/18 | PASS |
| E56 test_item 上半逐字全等（對 leaves_interim_v2） | 18/18 | PASS |
| E-雙錨 spec 錨在前／Sys-RA 在後 | 18/18；前綴 ['Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4'] | PASS |
| 附 design_method 皆屬下拉詞彙 | {'決策表 (Decision Table Testing)': 4, '邊界值分析 (Boundary Value Analysis, BVA)': 8, '功能測試 (Functional based ; no specific technique)': 4, '等價劃分 (Equivalence Partitioning, EP)': 2} | PASS |
| 附 §10.5 每 TC ≥2 步 | 2 | PASS |
| 附 Procedure↔ER 1:1 | PASS |  |
| 附 input_test_data 全 NA | PASS |  |
| 附 D 欄（req_id）皆 Sys-RA 實名 | PASS |  |
| 附 spec_reference 末行為 Sys-RA 錨 | PASS |  |
