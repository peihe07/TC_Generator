# INDEX — b2_fcw（下放包 12）

Test Group：`Vehicle Setup Management R1L TBM`｜Test Set：`Forward Collision Warning`（R-VT24 十九組之第 9 組）

leaf **15**（`chapter_for_vf = 01.11.01.01.26`）｜TC 總數 **15**｜PENDING **0**

| req_id | TC 數 | tc_title | PENDING |
|---|---|---|---|
| `Sys-RA-VF665_V43_VSM-453` | 1 | FCW setting and sensitivity menus shown when mitigation configured | 0 |
| `Sys-RA-VF665_V43_VSM-455` | 1 | FCW Setting1 offers three options in NAFTA and LATAM markets | 0 |
| `Sys-RA-VF665_V43_VSM-456` | 1 | FCW Setting1 request sent for off selection | 0 |
| `Sys-RA-VF665_V43_VSM-457` | 1 | FCW Setting1 request sent for audio selection | 0 |
| `Sys-RA-VF665_V43_VSM-458` | 1 | FCW Setting1 request sent for audio brake selection | 0 |
| `Sys-RA-VF665_V43_VSM-459` | 1 | FCW Setting1 display updated on reception of setting message | 0 |
| `Sys-RA-VF665_V43_VSM-460` | 1 | FCW Setting2 offers three options outside NAFTA and LATAM markets | 0 |
| `Sys-RA-VF665_V43_VSM-461` | 1 | FCW Setting2 request sent for off selection | 0 |
| `Sys-RA-VF665_V43_VSM-462` | 1 | FCW Setting2 request sent for brake selection | 0 |
| `Sys-RA-VF665_V43_VSM-463` | 1 | FCW Setting2 request sent for audio brake selection | 0 |
| `Sys-RA-VF665_V43_VSM-464` | 1 | FCW Setting2 display updated on reception of setting message | 0 |
| `Sys-RA-VF665_V43_VSM-466` | 1 | FCW sensitivity request sent for near selection | 0 |
| `Sys-RA-VF665_V43_VSM-467` | 1 | FCW sensitivity request sent for med selection | 0 |
| `Sys-RA-VF665_V43_VSM-468` | 1 | FCW sensitivity request sent for far selection | 0 |
| `Sys-RA-VF665_V43_VSM-469` | 1 | FCW sensitivity display updated on reception of activation mode message | 0 |

## 自檢彙總（IN §9 十七項之機讀部分 ＋ E38–E45／E51／E52）

| 項 | 實測 | 判 |
|---|---|---|
| E38 覆蓋（15 leaf 各 ≥1 TC） | 15/15 | PASS |
| E39 R-S4 括號下半（每 TC 有；同 req_id 內不逐字相同） | 15/15 有；重複 0 | PASS |
| E40 尾句號違規 | 0 | PASS |
| E41 [...]／'...'／<...> UI 標籤 | 0 | PASS |
| E42 $…$ 之列全數可回溯 v5 解得 | 4 名：['IPC_VEHICLE_SETUP2.FSFCWPlusActivationMode', 'IPC_VEHICLE_SETUP2.FSFCWPlusSetting', 'TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req', 'TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req'] | PASS |
| E43 PENDING 格式 | 0 處 | PASS（本批 0，理由見上繳 §PENDING） |
| E44 reasoning（每 req_id 一則、繁中、2–5 句、含切分依據） | 15 則；句數 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] | PASS |
| E45 modal 於 ER／test_item 下半 | 0 | PASS |
| E51 Remarks provisional 註 | 15/15 | PASS |
| E56 test_item 上半逐字全等（對 leaves_interim_v2） | 15/15 | PASS |
| E-雙錨 spec 錨在前／Sys-RA 在後 | 15/15；前綴 ['Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4'] | PASS |
| 附 design_method 皆屬下拉詞彙 | {'決策表 (Decision Table Testing)': 3, '等價劃分 (Equivalence Partitioning, EP)': 7, '功能測試 (Functional based ; no specific technique)': 3, '邊界值分析 (Boundary Value Analysis, BVA)': 2} | PASS |
| 附 §10.5 每 TC ≥2 步 | 2 | PASS |
| 附 Procedure↔ER 1:1 | PASS |  |
| 附 input_test_data 全 NA | PASS |  |
| 附 D 欄（req_id）皆 Sys-RA 實名 | PASS |  |
| 附 spec_reference 末行為 Sys-RA 錨 | PASS |  |
