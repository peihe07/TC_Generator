# 上繳 23 —— DR-15 曝險之全量掃描、batch06、batch07

執行層寫入。依據：`docs/handoff/44_review_round24.md` §6。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | DR-22′ 改是非題；DR-8 → DR-8′ | ✅ |
| D-3 | profile 增列注入優先序 | ✅ |
| D-4 | BACKLOG 增 B-11／B-12／B-13 | ✅ |
| D-5 | 依 R-VS35 列兩數 | ✅ 見 §5.1 |
| **W-71** | DR-15 曝險全量掃 | ✅ **3 條（≤ 10）；含一條 pilot 已放行者** |
| **W-72** | batch06 | ✅ **選入 10、移出 1、交付 9**，0 違規 |
| **W-73** | batch07 | ⚠ **選入 10、移出 3、交付 7**；查出兩對嚴格等價 |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-71 —— DR-15 曝險之全量掃描

| 項 | 值 |
|---|---:|
| 已生成 TC 總數 | **42** |
| **曝險（斷言五個請求 token 之值）** | **3** |
| 44 包 §3 已知 | 2 |
| **本輪新增** | **1** |

| 批次 | leaf | 斷言 |
|---|---|---|
| `batch01_v3`（**pilot 已 PASS**） | `SwitchLHD/RHDConfiguration-009` | `$TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ is 1 (Pressed)` |
| `batch03` | `LeftFrontHeatedSeat-014` | `= 0 (Not_Pressed)`／`= 1 (Pressed)` |
| `batch04_v2` | `RightFrontHeatedSeat-031` | `= 1 (Pressed)` |

**3 ≤ 10 → 升級條件未命中。**
全部批次已增 `dr15_exposed` 欄；`TwoStagesHeatedSeat-057` 等標 `no` 並附理由（44 包 §3(2)）。

### 1.2 W-72／W-73 —— 兩批之選取與交付

| 批 | 餘量（四 Layer 2） | 配額 | 選入 | 移出 | **交付** | §9 違規 |
|---|---|---|---:|---:|---:|---:|
| `batch06` | 11／8／7／3 | 4／3／2／1 | 10 | **1** | **9** | **0** |
| `batch07` | 7／5／5／2 | 3／3／3／1 | 10 | **3** | **7** | **0** |

**四個 Layer 2 之餘量皆非 0 → 「某 Layer 2 餘量為 0」之升級條件未命中。**

移出之 4 條逐筆：

| leaf | 阻塞 | 理由 |
|---|---|---|
| `HeatedSteeringWheel-013` | DR-15（token 級） | `[NOT Pressed / NOT_PSD]` |
| `RightFrontVentedSeat-029` | DR-15（token 級） | `[Not Pressed / VS_NOT_PSD]` |
| `StopStartSystemBehavior-054` | DR-21（B2） | `ENS_DSBL` 無匯流排對應 |
| `StopStartSystemBehavior-055` | DR-21（B2） | 同上 |

### 1.3 累計產出

| 批次 | 交付 | 狀態 |
|---|---:|---|
| `batch01_v3` | 8 | **pilot PASS** |
| `batch02` | 6 | 待 review |
| `batch03` | 10 | 待 review |
| `batch04_v2` | 10 | 待 review |
| `batch05` | 8 | 待 review |
| **`batch06`** | **9** | 本輪 |
| **`batch07`** | **7** | 本輪 |
| **合計** | **58** | |
| 移出／未撰寫累計 | 12 | |

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **第三種引號形態：彎引號，兩次掃描都抓不到**

W-73 讀 `4859504` 時發現：

```
IF (STATUS_CCAN3.EngineSts == “Engine_Off” AND STATUS_CCAN3.ESS_ENG_ST != “ENS_DSBL”)
```

**引號為 U+201C／U+201D（彎引號），該條文中直引號 `"` 出現 0 次。**
20 輪之 `= [值]` 與 21 輪之 `== "值"` **兩式皆不匹配**。

全量重掃（`[“‘]…[”’]`）：

| token | leaf | 值 | 判 |
|---|---:|---|---|
| `EngineSts` | 3 | `Engine_Off`／`Engine_On` | **皆解** |
| **`ESS_ENG_ST`** | **2** | **`ENS_DSBL`** | **未解**（DBC 為 `ENS disabled`） |

**規模有界（2 token／3 leaf）** —— 故 21 輪 §6-2 之「第三種形態存在與否未知」
**就此關閉為「存在，且已量」**。`StopStartSystemBehavior-054`／`-055` 移出。→ A-VS84

> **但第四種形態仍未掃**（`'值'` 單引號、全形引號等）。
> 21 輪之五個候選第三式測的是**直引號與裸值**，**未含彎引號** ——
> 該次「(b) = 0」之結論，其涵蓋範圍比當時所稱者窄。

### 2.2 ⚠ **037 有兩個 leaf 承載同一需求，其 TC 為嚴格等價**

§4.6 之 sibling 比對查出**兩對**：

| 對 | CFTS044 條文 | 記法 |
|---|---|---|
| `HeatedSteeringWheel-021` ≡ **`-015`** | `4858544` ≡ `4858538` | `[1h: On]` vs `[On]` |
| `HeatedSteeringWheel-022` ≡ **`-016`** | `4858545` ≡ `4858539` | `[0h: Off]` vs `[Off]` |

**四條之觸發、結果、輸入、驗證對象全同** —— 依 §10.6 標 `duplicate_of`，
`distinguishing_axis.axis = none`。

**成因在 CFTS044**：`4858538` 與 `4858544` 為同一需求之兩次書寫。
**037 依 R-VS15 為母體，本層不得合併 leaf**（§8.2.1 之反向禁令：
TC 作者不得合併 RD sub-id）。**是否向上游反映屬分析層。** → A-VS85

### 2.3 ⚠ **pilot 已放行之批次中有一條 DR-15 曝險**

W-71 之曝險 3 條中，**`SwitchLHD/RHDConfiguration-009` 屬 `batch01_v3`，
其已於 2026-08-22 由 Pei 判 pilot PASS**。

其 ER 逐字：`$TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ is 1 (Pressed), the same as
recorded in step 2`。

**若 DR-15 覆為「承載階數」，該條之 ER 須改寫，而其已列為已放行。**
44 包 §3 之裁定為「不撤回、標記、覆後複檢」，本層**依此標記，未撤回**。→ A-VS86

### 2.4 `ScreenOFF-051` 之 ER 只斷言訊號有送出，不斷言其值

`4859108` 逐字：`the HU shall send the $TGW_DISP_STAT$ signal.
**See {CFTS020} for the signal value** the HU shall set it to.`

| 事實 | 處置 |
|---|---|
| 該值定義於 `{CFTS020}`（**具名**，非 B1） | 依 §8.4.2 **不吸收**其值 |
| `TGW_DISP_STAT` **於基線 DBC 中不存在** | 依 §8.7.5(g) 保留來源名，**不加 `$`** |

ER 寫為「a TGW_DISP_STAT signal is transmitted on CAN-B」——
**可觀察，且不斷言其值**。**該處置未經 review 確認。**

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | 五個批次增 `dr15_exposed` 欄並逐條標記；`DR-22′` 改為是非題全文；`DR-8` → `DR-8′`（前提失效之改寫）；型 B 標「搜尋已停止」；profile 增無效值注入優先序三項；`BACKLOG.md` 增 B-11／B-12／B-13；**`batch06` 9 條、`batch07` 7 條，皆 0 違規**；A-VS84／85／86 登記 |
| **核實無誤** | 曝險 3 ≤ 10；四個 Layer 2 餘量皆非 0；彎引號形態規模有界（2 token／3 leaf）；兩對嚴格等價之四項比對全同 |
| **正確地不動** | **未撤回 pilot 已放行之曝險 TC**（44 包 §3）；**未合併 `-015`/`-021` 兩個 leaf**（§8.2.1 反向禁令）；**未採用他車型 PROXI 表之值**；**未再執行型 B 之唯讀搜尋**（44 包 §2）；**未斷言 `TGW_DISP_STAT` 之值**（§8.4.2）；**ER 皆未以 `<Tsend>`／`<Tdisplay>` 為通過條件** |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| **W-71 曝險判準** | 對每條 TC 之 `test_procedure` ＋ `expected_result`，正則 `\$[A-Z0-9_]+\.(\w+)\$` 取 signal，命中 `{FL_HS_Tlm, FR_HS_Tlm, FL_VS_Tlm, FR_VS_Tlm, HSW_Tlm, FL_HS_RQ, FR_HS_RQ, FL_VS_RQ_TGW, FR_VS_RQ_TGW, HSW_RQ_TGW}` 者標 `yes` |
| **彎引號形態** | `(?:[A-Z0-9_]+\.)?(token)\s*(?:==\|=\|!=\|passes to)\s*[“‘]([^”’]{1,60})[”’]`，token 再經識別碼形態過濾；值域比對取 `spec_variables` ∪ **DBC `VAL_`** |
| W-72／W-73 選 leaf | `generatable.tsv` 之 `stable_core = yes`，扣已用／已移出者；逐 Layer 2 比例加權、每個至少 1；**選入後逐條過 `guard()`** |
| 無效值注入 | 依 profile 之優先序：本輪二條（`RightFrontVentedSeat-023`）取 (2) 配置相依（`4858363` 之二階列舉排除 `medium`） |
| `<Tdisplay>`／`<Tsend>` | procedure 保留來源逐字於 `test_item`；**ER 改寫為可觀察之終態，不以時限為通過條件** |
| sibling 嚴格等價 | §10.6 之四項：trigger ＋ outcome ＋ input ＋ verification target 全同者標 `duplicate_of`，並令 `distinguishing_axis.axis = "none"`（§4.6 之 `axis="none"` ⇔ `duplicate_of` set） |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS84** | **DR-21**（B2） | 第三種引號形態（彎引號）；`ENS_DSBL` 未解，2 leaf |
| **A-VS85** | — | 037 兩對 leaf 承載同一需求，TC 嚴格等價 |
| **A-VS86** | **DR-15** | pilot 已放行之 `batch01_v3` 中有一條曝險 |

**無新開 DR。** `DR-22′` 改為是非題全文；**`DR-8` → `DR-8′`**（前提失效）；
型 B 四筆標「搜尋已停止（44 包 §2）」。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS84／85／86） | **85**（相異編號；最大號 A-VS86，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0 新開**；DR-22′ 改寫、DR-8 → DR-8′ | 未結 **13** |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。

**分析層側核對（44 包）**：44 包開立 anomaly **0 筆**、DR **0 筆**（DR-8′／DR-22′ 為改寫）；**差額 0**。

### 5.2 五份即刻可送之 DR（44 包 §7）

| DR | 型 | 影響 leaf | 本輪之變動 |
|---|---|---:|---|
| **DR-22′** | B | 79 | **改為是非題，已落檔** |
| DR-20／DR-23 | B | 17 ／ 3 | 標「搜尋已停止」 |
| **DR-8′** | B | 8 引用 | **改寫，已落檔** |
| DR-24′ | A | 43 | 已定稿 |
| DR-21／DR-18／DR-11 | A | 65／160／1 | 已定稿；**DR-21 之實例增 `ENS_DSBL` 2 leaf** |

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **21 輪之「第三式 (b) = 0」其涵蓋範圍比當時所稱者窄。**
   該次測了五個候選（單引號 `'值'`、`is set to`、`shall be set to`、
   `shall be <大寫>`、裸值），**未含彎引號** —— 而彎引號正是本輪找到的那一種。
   **第四種形態（全形引號 `「」`、`= <值>` 帶單位等）仍未掃。**
   **每次「已窮盡」之宣稱，其涵蓋範圍須逐式列出方能檢驗。**

2. **`ScreenOFF-051` 之處置未經 review。**
   其 ER 只斷言訊號有送出、不斷言值。
   **「訊號有送出」是否構成該需求之完整驗證，屬 TC 內容層之判斷。**
   同型者（引用外部 spec 之值）尚有幾條未掃。

3. **A-VS85 之兩對嚴格等價，其在 237 母體中之總數未量。**
   已知 2 對（4 條 leaf）。**CFTS044 中「同一需求兩次書寫」之總數未掃** ——
   若尚有多對，覆蓋率之分母（237）會虛高，而 TC 之實際獨立驗證點少於 58。

4. **`dr15_exposed` 之判準只看 `$MESSAGE.Signal$` 形態。**
   若某 TC 以**畫面行為**間接驗證請求訊號（如按壓圖示 → 期望某狀態），
   其不含 `$…$` 而仍可能受 DR-15 之答覆影響。
   **`TwoStagesHeatedSeat-057`／`ThreeStagesHeatedSeat-080`／
   `TwoStagesVentedSeatsManagement-039` 三條即此類**，本輪標 `no` 並附理由，
   **惟該理由（按壓與請求訊號可分離）未經 review 確認**（24 輪 §6-4 已提，仍未解）。
