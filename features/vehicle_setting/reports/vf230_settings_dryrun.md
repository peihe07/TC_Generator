# VF230 設定項查找配方 dry-run 摘要（下放包 VS-SL-01 §2 任務 3）

日期：2026-09-01　層級：Tier 1（執行層）　性質：**dry-run，未寫回任何工作簿**
明細：`features/vehicle_setting/reports/vf230_settings_dryrun.tsv`（457 列）
產生器：`scripts/vs_sl01_dryrun.py`　查找器：`scripts/settings_lookup.py`

> 本摘要之數**全部為本輪實測**，未引用下放包所載之數。
> 與下放包不符者見 §A 之「與包內數之差」，逐項附證據。

---

## §A　命中統計

| 項 | 數 | 說明 |
|---|---:|---|
| 工作簿資料列 | **457** | `Test Case Specification 測試用例規範` r10–r466；表頭 r9 |
| 報告列 | **457** | 自檢 1 PASS（`scripts/vs_sl01_selfcheck.py`） |
| 相異 `"X" customer setting` 名 | **107** | 總命中 1,234 處 |
| 別名 `exact` | **51** | HMI 精確 20 ＋ FIP 精確 48，其中兩者皆中 17 |
| 別名 `manual` | **2** | 空白不敏感之候選（`Park Sense` ↔ `ParkSense`），**待 Pei 逐條認可** |
| 別名 `UNRESOLVED` | **54** | 開 `DR-49`；依 R-13 不以語意相近之名代入 |
| Settings List 攤平後之設定項 | **519** | 36 個分類標題、A/B/C 三層 |
| 总控表 `FeatureSet(Gen4-5)` 資料列 | **278** | 只讀 E 欄（Atlantis／DT） |
| `path_proposed` 產出 | **66** | 其餘因別名未解或該項不在 Settings List |
| `control_proposed` 產出 | **66** | 同上 |
| `proxi_now` 非空 | **152** | 全為舊形制 `PROXI $Param$ is set to "label"` |
| `proxi_proposed` 為 `PENDING: DR-49` | **207** | 需求原文與总控表皆無條件 |

### 与下放包所載之数的差

| 包內 | 實測 | 證據 |
|---|---|---|
| 相異名 **106** | **107** | 多出者為 `AUX Switches`（1 處命中，與 `4 AUX Switches`／`6 Aux Switches` 並存） |
| 非 NAFTA 列 **18** | **19** | r400–r418 連續 19 列，D 欄前綴一律 `SWE1-VC-TrafficSignAssistOffset - non-NAFTASetting-` |
| `OR_VALUE` **7** | **5**（現況）／**9**（含提議） | 現況 = `proxi_now` 之 label 含 `or` 者 r42/148/151/154/157；提議側再加 r141/142/147/150 |
| HMI 精確命中 **24** | **20** | 本層之 exact 定義為正規化後逐字相等（去 `*`、去括號註、壓空白）；`Park Sense` ↔ `ParkSense*` 之類歸 `manual` 而非 `exact` |
| FIP 精確命中 **48** | **48** | 相符 |

---

## §B　各 flag 計數與列清單

| flag | 列數 | 列 |
|---|---:|---|
| `PATH_ABSENT` | 365 | 現行 procedure 只有 `Open the Vehicle Settings menu`，**無逐層路徑**；另 92 列連該泛稱句都沒有 |
| `ALIAS_UNRESOLVED` | 281 | 別名 54 名所涉之列 |
| `PROXI_PENDING` | 207 | 二來源皆空 → `PENDING: DR-49` |
| `RAW_MISSING` | 26 | label 於 `_vf230_proxi_values.json` 查無 raw；不猜值 |
| `VARIANT_UNRESOLVED` | 19 | Settings List 同名多列而無 NAFTA 標記亦非單列 |
| `NON_NAFTA` | 19 | r400–r418（見 §A 差異表） |
| `OR_VALUE` | 9 | r42, r141, r142, r147, r148, r150, r151, r154, r157 |
| `ALWAYS_FALSE` | 8 | r319–r322（`Ready to Drive Pop-Up`）、r453–r456（`Surround View Camera Delay`／`Guidelines`）—— 見 §C |
| `ALIAS_MANUAL` | 6 | r125–r128, r463, r464 |
| `BRAND_NAME_UNVERIFIED` | 4 | r125–r128：Settings List 名帶 `*` 但 `Brand-Specific Names` B 欄無逐字對應 |
| `EP_SIBLING` | 3 | OR 列舉之提議取本列之值，兄弟另立（§4 形制） |
| `NEG_CONTRA` | **3** | **r150, r153, r156 —— 見下** |

### `NEG_CONTRA` 三列（真矛盾，非形式問題）

| 列 | D 欄 | `test_item` 說 | `Pre-Condition` 卻設 |
|---|---|---|---|
| r150 | `ForwardCollisionWarning-034` | `Forward_Collision_Mitigation != [3], [2], [1]` → **不顯示** | `= "Full Speed Forward Collision Warning with Mitigation"`（raw 3，**在排除集內**） |
| r153 | `ForwardCollisionWarningSensitivity-041` | 同上 | 同上 |
| r156 | `PedestrianEmergencyBrakingorWarning&ActiveBraking-048` | `!= [2] or [1]` → **不顯示** | `= "Full Speed FCW with Pedestrian Emergency Braking"`（raw 2，**在排除集內**） |

依 §4「負向 TC 取 raw 0 (Absent)」，三列之 `proxi_proposed` 一律改為
`PROXI Forward_Collision_Mitigation = 0 (Absent)`。**此為寫回動作，本包不執行。**

### `PATH_ABSENT` 之意義

現行 457 列**沒有任何一列帶逐層導覽路徑**。§4 之參考輸出要求
`Press "Settings" → Select "<Category>" → Select "<Parent>" → Check "<Item>"`。
本配方對 66 列可直接產出該路徑；其餘 391 列卡在別名或 Settings List 無該項。

---

## §C　`Always false` 明細（R-VS{live+1}，**登記，非裁定用**）

总控表 Atlantis 判為 `Always false` 者全 278 列中共 **110** 項；其中與 VF230 之
設定項對得上者 **3 名 8 列**：

| 設定項 | 总控表 | 涉及列 | 現況 |
|---|---|---|---|
| `Ready to Drive Pop-Up` | Atlantis `Always false` | r319, r320, r321, r322 | 正向列，保留其需求追溯不刪 |
| `Surround View Camera Delay` | Atlantis `Always false` | r453, r454 | 同上 |
| `Surround View Camera Guidelines` | Atlantis `Always false` | r455, r456 | 同上 |

**此三名（8 列）不新增「不顯示」之負向 TC**；其正向列之 PROXI 前置只依需求原文（來源優先序 (1)），
总控表對此類不提供任何條件。

---

## §D　DR 草稿與待 Pei 決之事項

### DR-49（草稿，**登記，未送出**）

> **開號依據**：全庫最大已用 DR 號實測為 **DR-48**（`features/*/DATA_REQUESTS.md` 標題掃描），故取 **DR-49**。

**標的**：VF230 之 54 個設定項顯示名，於 HMI Settings List 與 FIP 总控表
`FeatureSet(Gen4-5)` **二者皆無逐字對應**，致其 PROXI 前置無據可取。
全文見 `features/vehicle_setting/DATA_REQUESTS.md` 之 `DR-49`。

### 待 Pei 決（本層不自裁）

1. **裁定之編號命名空間**　本包令記為 `R-VS{live}`，本層依台帳現況取 **R-VS84–R-VS88**（主線最大實測 `R-VS83`）。
   **惟 `R-VS63` 已將 VF230 線之 ruling 空間定為 `R-VS100` 起、其後又改用 `R-VF` 前綴（實測最大 `R-VF142`）**，
   而本五條之適用範圍為 VF230／VF665，屬 VF230 線。
   **若應改記為 `R-VF143`–`R-VF147`，請裁；本層不自行搬號。**
   同一問題適用於本輪三筆 anomaly（本層取 `A-VS166`–`A-VS168`，主線實測最大 `A-VS165`）。

2. **非 NAFTA 之 19 列移除**　R-VS{live}(4) 令移除，**移除屬寫回動作**，
   本包不執行。標的：r400–r418（`Traffic Sign Assist Offset - non-NAFTA Setting`）。**請確認後執行。**

3. **PROXI 形制改寫 152 處**　R-VS{live+2} 令 `PROXI $Param$ is set to "label"`
   → `PROXI <Param> = <raw> (<label>)`。實測 **152 處**，涉 **152 列**。同屬寫回動作，待確認。

4. **`NEG_CONTRA` 三列**　見 §B。改法明確（取 `raw 0 (Absent)`），仍屬寫回，待確認。

5. **別名 `manual` 2 條之認可**　R-VS{live+4} 令逐條認可後方綁入配方。
   清單見 `data/settings_alias.tsv` 之 `match_type = manual` 兩列。

6. **選項字串之空白**　Settings List r249 之 E 欄逐字為 `Off/ Only Warning/Warning+ Active Braking`，
   與 §4 參考輸出之 `Warning + Active Braking` 差一空格。**本層保留原文不修**，請裁以何者為準。

7. **`Test Case ID`（F 欄）全 457 列為空**　本報告之 `tc_id` 欄一律填 `(F 欄空)`。
   R-G42 二令 F 欄須為 `NR1L-{ABBR}-{nnn}`，此本尚未取號。與本包無涉，登記備忘。
