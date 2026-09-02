# INDEX — b1_ambient（下放包 07 W-B）

Test Group：`Vehicle Setup Management R1L TBM`｜Test Set：`Interior Ambient Lighting`（R-VT19 十六組之第 10 組）

leaf **10**（`chapter_for_vf = 01.11.01.01.26`）｜TC 總數 **11**｜PENDING **0**

| req_id | TC 數 | tc_title | PENDING |
|---|---|---|---|
| `Sys-RA-VF665_V43_VSM-651` | 1 | Ambient Lights Level menu shown when function present and dimmer absent | 0 |
| `Sys-RA-VF665_V43_VSM-652` | 1 | Ambient lighting level 1 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-653` | 1 | Ambient lighting level 2 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-654` | 1 | Ambient lighting level 3 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-655` | 1 | Ambient lighting level 4 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-656` | 1 | Ambient lighting level 5 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-657` | 1 | Ambient lighting level 6 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-658` | 1 | Ambient lighting level 7 request sent on user selection | 0 |
| `Sys-RA-VF665_V43_VSM-659` | 1 | Ambient light information updated on reception of level message | 0 |
| `Sys-RA-VF665_V43_VSM-661` | 2 | Ambient Lights Level menu hidden when function absent<br>Ambient Lights Level menu hidden when dimmer switch present | 0 |

## 自檢彙總（IN §9 十七項之機讀部分 ＋ E38–E45／E51／E52）

| 項 | 實測 | 判 |
|---|---|---|
| E38 覆蓋（10 leaf 各 ≥1 TC） | 10 | 10/10 |
| E39 R-S4 括號下半（每 TC 有；同 req_id 內不逐字相同） | 11/11 有；重複 0 | PASS |
| E40 尾句號違規 | 0 | PASS |
| E41 [...]／'...'／<...> UI 標籤 | 0 | PASS |
| E42 $…$ 之列全數可回溯 v5 解得 | 2 名：['IPC_VEHICLE_SETUP.AmbientLightingLevel', 'TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req'] | PASS |
| E43 PENDING 格式 | 0 處 | PASS（本批 0，理由見上繳 §PENDING） |
| E44 reasoning（每 req_id 一則、繁中、2–5 句、含切分依據） | 10 則；句數 [4, 4, 4, 4, 4, 4, 4, 4, 5, 4] | PASS |
| E45 modal 於 ER／test_item 下半 | 0 | PASS |
| E51 Remarks provisional 註 | 10/10 | PASS |
| E52 W-A 對應結果 | 不成立（規格標題無字面章節號；推算 1.11.1.1.26 = 'Auto High  Beam'） | 僅寫 Sys-RA 錨 |
| 附 design_method 皆屬下拉詞彙 | {'決策表 (Decision Table Testing)': 1, '邊界值分析 (Boundary Value Analysis, BVA)': 2, '等價劃分 (Equivalence Partitioning, EP)': 5, '功能測試 (Functional based ; no specific technique)': 1, '負向測試 (Negative / Invalid)': 2} | PASS |
| 附 §10.5 每 TC ≥2 步 | 2 | PASS |
| 附 Procedure↔ER 1:1 | PASS |  |
| 附 input_test_data 全 NA | PASS |  |
| 附 D 欄皆 Sys-RA 實名 | PASS |  |
