# INDEX — b2_sdw（下放包 13）

Test Group：`Vehicle Setup Management R1L TBM`｜Test Set：`Side Distance Warning`（R-VT24 十九組之第 12 組）

leaf **10**（`chapter_for_vf = 01.11.01.01.26`）｜TC 總數 **10**｜PENDING **0**

| req_id | TC 數 | tc_title | PENDING |
|---|---|---|---|
| `Sys-RA-VF665_V43_VSM-440` | 1 | Side Distance Warning menu hidden when parameter absent | 0 |
| `Sys-RA-VF665_V43_VSM-441` | 1 | Side Distance Warning setting and chime volume menus shown when present | 0 |
| `Sys-RA-VF665_V43_VSM-443` | 1 | Side distance warning request sent for off selection | 0 |
| `Sys-RA-VF665_V43_VSM-444` | 1 | Side distance warning request sent for sound selection | 0 |
| `Sys-RA-VF665_V43_VSM-445` | 1 | Side distance warning request sent for sound plus display selection | 0 |
| `Sys-RA-VF665_V43_VSM-446` | 1 | Side distance warning display updated on reception of setting message | 0 |
| `Sys-RA-VF665_V43_VSM-448` | 1 | Side distance warning chime volume request sent for low selection | 0 |
| `Sys-RA-VF665_V43_VSM-449` | 1 | Side distance warning chime volume request sent for medium selection | 0 |
| `Sys-RA-VF665_V43_VSM-450` | 1 | Side distance warning chime volume request sent for high selection | 0 |
| `Sys-RA-VF665_V43_VSM-451` | 1 | Side distance warning display updated on reception of chime volume message | 0 |

## 自檢彙總（IN §9 十七項之機讀部分 ＋ E38–E45／E51／E52）

| 項 | 實測 | 判 |
|---|---|---|
| E38 覆蓋（10 leaf 各 ≥1 TC） | 10/10 | PASS |
| E39 R-S4 括號下半（每 TC 有；同 req_id 內不逐字相同） | 10/10 有；重複 0 | PASS |
| E40 尾句號違規 | 0 | PASS |
| E41 [...]／'...'／<...> UI 標籤 | 0 | PASS |
| E42 $…$ 之列全數可回溯 v5 解得 | 4 名：['IPC_VEHICLE_SETUP.Sdw', 'IPC_VEHICLE_SETUP.SdwChimeVolume', 'TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req', 'TELEMATIC_VEHICLE_SETUP.Sdw_Req'] | PASS |
| E43 PENDING 格式 | 0 處 | PASS（本批 0，理由見上繳 §PENDING） |
| E44 reasoning（每 req_id 一則、繁中、2–5 句、含切分依據） | 10 則；句數 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4] | PASS |
| E45 modal 於 ER／test_item 下半 | 0 | PASS |
| E51 Remarks provisional 註 | 10/10 | PASS |
| E56 test_item 上半逐字全等（對 leaves_interim_v2） | 10/10 | PASS |
| E-雙錨 spec 錨在前／Sys-RA 在後 | 10/10；前綴 ['Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4'] | PASS |
| 附 design_method 皆屬下拉詞彙 | {'負向測試 (Negative / Invalid)': 1, '決策表 (Decision Table Testing)': 1, '等價劃分 (Equivalence Partitioning, EP)': 4, '功能測試 (Functional based ; no specific technique)': 2, '邊界值分析 (Boundary Value Analysis, BVA)': 2} | PASS |
| 附 §10.5 每 TC ≥2 步 | 2 | PASS |
| 附 Procedure↔ER 1:1 | PASS |  |
| 附 input_test_data 全 NA | PASS |  |
| 附 D 欄（req_id）皆 Sys-RA 實名 | PASS |  |
| 附 spec_reference 末行為 Sys-RA 錨 | PASS |  |
