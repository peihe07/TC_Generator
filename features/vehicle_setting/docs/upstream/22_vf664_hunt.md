# 上繳 22 —— VF664 與型 B 之一次搜尋、閘之修正、batch05

執行層寫入。依據：`docs/handoff/43_review_round23.md` §4。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 轉錄 R-VS44′；`OPEN_DR` 標級別 | ✅ |
| D-3 | DR-24 → DR-24′ | ✅ |
| D-4 | 增 `evidence_note`，8 列標 `VF664-inferred` | ✅ |
| D-5 | 依 R-VS35 列兩數 | ✅ 見 §5.1 |
| **W-68** | 型 B 一次搜尋 | ⚠ **VF664 找到但不帶值域；TLM HMI 確不存在** |
| **W-69** | 閘之修正與重驗 | ✅ **4/4 攔下且可失敗** |
| **W-70** | batch04_v2 ＋ batch05 | ⚠ **複檢逐字命中；batch05 交付 8 條** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-68 —— 搜尋範圍（R-G10 之餘數具名）

| 項 | 值 |
|---|---:|
| **R1LR 目錄下之 pdf／doc／rtf／xls 內容掃描** | **1,362 檔**（pdf 404／rtf 356／xls 378／doc 224） |
| 其中 **pdf 文字層不足（< 200 字元）** | **6**（`Core HMI Logic and Flow` 四份副本 ＋ 兩份 `CFTSMV033_CIP_R4` inline pdf） |
| 全庫檔名含 `664` 者 | **47** |
| 全庫檔名含 `proxi` 者（23 輪） | 30（全為他車型） |
| 檔名含 `*TLM*HMI*`／`*telematic*HMI*` | **0** |

**`Core HMI Logic and Flow` 之 OCR 探測（00D 之法）**：21 頁，`rot=0` 抽出亂碼、
**`rot=180` 抽出可讀英文**（首頁 `R1 Core HMI Logic and Flow Spec Release: SR24 Post 2A`）。
**00D 之「須旋轉 180° 方可讀」再次成立。**

### 1.2 W-68(1) —— VF664 找到了，**但它不定義值域**

`Vehicle_Controls_Management_by_VP_-_LTM_VF664_*`（docx／pdf，四車型五版本）為 VF664 本文。
逐檔抽文字層：

| 檔 | 文字量 | 四參數命中 |
|---|---:|---|
| `…VF664_V2_R2.docx`（HDCC28） | 8,936 | 4 個名稱皆命中 |
| `…VF664_V2_R1.docx`（DT27） | 13,663 | 4 個名稱皆命中 |
| `…VF664_V42_R3.docx`（Toro226） | 7,797 | **0** |

**命中之上下文為「本 VF 所用之 PROXI 參數清單」**，逐字如
`…Heated_SeatsHeated_Steering_WheelRear_ClimateHybrid_TypeVehicle_Line_ConfigurationCooled_Seats…`
—— **只有名稱，沒有任何 `0 = …／1 = …` 之值域**。

**W-68(1) 之正向升級條件（「找到 VF664 → 79 leaf 可解」）之前提不成立。**
值域之定義仍在 **PROXI 表**；**A-VS77 之裁定不因 VF664 之尋獲而改變。** → A-VS82

### 1.3 W-68(2) —— **`TLM HMI Document` 確不存在**

| 掃描 | 結果 |
|---|---|
| 檔名 `*TLM*HMI*`／`*telematic*` | **0**（`*telematic*` 之 11 筆全為 `Infotainment_and_Telematics_Steering_Wheel_Controls…VF465`） |
| **內容 `TLM HMI`** | **命中 15，全數為 CFTS 文件中之引用** |
| 內容 `informative popup` | 命中 4，皆為 `4859387` 本身（跨 PI 之四份副本） |
| 我方已持有之 `Comfort HMI Logic and Flow` PDF（64,978 字元） | `informative popup`／`Fail_Present`／`popup…fail` **皆 0** |
| 26PI2.5/HMI 之 89 份 PDF | `informative popup` **0**；6 份含其他功能之 failure popup，與座椅無關 |

**該文件確不在客戶需求目錄。W-68(2) 之正向升級條件未命中。**
DR-20／DR-23 之型 B 訴求成立且**無法以搜尋解除**。→ A-VS81

### 1.4 W-68(3) —— 車型碼：DR-8 之訴求部分可改

`\bHDCC\b…\bM240\b` 交叉 **命中 0**。
惟 `VC_VEH_LINE` 於 R1LR 之 CFTS 文件中 **命中 103**，其值形態為
`[332]`／`[VEH_M182 OR VEH_M189]`／`[M182]`／`[M189]` ——
**與 DR-8 所列之 `DT`／`WS`／`HDCC`／`M240` 不同**。

**DR-8 之提問文可據此收斂**（其為型 B，訴求應為「完整對照表」；
惟實測顯示規格側之實際用碼為另一組）。**改寫屬分析層。**

### 1.5 W-69 —— 閘之修正與重驗

`OPEN_DR` 已改為 **(級別, token 集合, 值樣式, 狀態)** 四元組，逐筆標級別：

| DR | 級別 | token 數 | 值樣式 |
|---|---|---:|---|
| **DR-15** | **token** | 5 | `.`（全部） |
| DR-17 | clause | 0 | —— |
| DR-19 | value | 1 | `IDLE_STBL\|UNLIMITED\|LIMITED\|\bRUN\b` |
| DR-21 | value | 2 | `IGN_START\|IGN_OFF_ACC` |
| **DR-22′** | **token** | 5 | `.` |
| DR-18 | value | 2 | `HS_HI\|HS_OFF` |
| DR-8 | token | 1 | `.` |
| **DR-24′** | value | 5 | `Tsend\|Tdisplay` |

**驗收**：23 輪之 4 組 `Pressed` derivable 重跑 → **4 / 4 輸出 `DR-CONFLICT: DR-15`**。
**可失敗性**：移除交叉檢查後 → **4 / 4 判回 `derivable`**；還原後復為 `DR-CONFLICT`。

**「有任一組未被攔下」之升級條件未命中。**
W-69(5) 全量重跑：**新增被攔下者 4**（即該 4 組）；`DriverSide` 之 `Right Drive` 維持 `derivable`。

### 1.6 W-70(2) —— batch05

| 項 | 值 |
|---|---:|
| 四個 Layer 2 餘量 | Common Features 14／Vented Seat 11／Heated Steering Wheel 10／Heated Seat 4 |
| 配額 | 3／3／3／1 |
| 選入 | **10** |
| **經閘攔下而移出** | **2** |
| **實際交付** | **8** |
| §9 機械檢查違規 | **0** |

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **W-70(1) 之複檢：逐字讀為命中，惟其為 43 包自己認可之處置**

升級條件逐字為「W-70(1) 之複檢發現 batch01–03 **亦有誤用已定義編碼者**」。

實測 batch01–04 之四條 `Negative / Invalid` TC，其注入值：

| leaf | 注入值 | DBC 已定義？ | 判 |
|---|---|---|---|
| `LeftFrontHeatedSeat-008` | `2 (Heated_seat_medium)` | **是** | **配置相依無效值**（`4858307` 之二階列舉） |
| `RightFrontHeatedSeat-026` | `2 (Heated_seat_medium)` | **是** | 同上 |
| `LeftFrontVentedSeat-006` | `2 (Vented_seat_medium)` | **是** | 同上（`4858363`） |
| `HeatedSteeringWheel-006` | `7 (SNA)` | **是** | **誤用** —— SNA 語意為「訊號不可用」 |

**43 包 §3.2 自己明訂之替代路徑即為「配置相依無效值（如 `4858307` 之二階配置下
`medium` 為無效）」** —— 故前三條**非誤用**。

**逐字讀命中、實質讀未命中。不自行調和** —— 若分析層認為前三條亦須改，
其須改為「DBC 中未定義之編碼」，而 `FL_HS_STATSts` 為 **2 bit，0–3 全數已定義**，
**屆時無可注入之值**，該三條須改標 `PENDING`。

`HeatedSteeringWheel-006` **已修正**：改注入 `4`（`Tri_Level_HSW_StatSts` 之
`VAL_` 為 0/1/2/3/7，**4／5／6 未定義**），產出 `batch04_v2.json`，v1 保留。

> **未定義編碼無 `(<label>)` 可寫**，故該步驟寫作 `= 4`。
> 為其編造標籤即違 §8.4.1；`= <raw> (<label>)` 之形式**預設該值已定義**。

### 2.2 ⚠ **DR-15 之標的涵蓋已生成之三條 TC**

R-VS44′ 令 DR-15 改為 token 級後，五個請求 token 之**任何值**皆在其範圍內。

**實測**：CFTS044 **自載**該五個 token 之 `1h: pressed`／`0h: not pressed` 錨點，
**而他處條文（`4858325` 等）又述循環降階值** —— **該內部矛盾正是 DR-15 之提問標的**。

| TC | 批次 | 狀態 |
|---|---|---|
| `LeftFrontVentedSeat-012` | batch05 選入 | **已由閘攔下並移出** |
| `HeatedSteeringWheel-012` | batch05 選入 | **已由閘攔下並移出** |
| **`LeftFrontHeatedSeat-014`** | **batch03（已生成）** | **斷言 `FL_HS_Tlm` 之 0/1** |
| **`RightFrontHeatedSeat-031`** | **batch04_v2（已生成）** | **斷言 `FR_HS_Tlm` 之 0/1** |

**後二者在 R-VS44′ 生效前產出。是否須一併移出，屬裁定事項** ——
**本層不逕自撤回已生成之 TC。** → A-VS83

### 2.3 W-68(1) 之正向升級「找到 VF664」成立，但其推論不成立

43 包 §1.1 之升級條件為「**找到 VF664 → 79 leaf 可解，立即回報**」。

**VF664 找到了（47 筆檔名命中，四車型五版本之本文皆已抽文字層），
但它只列參數名，不定義值域。**

故：**條件之前件成立、後件不成立**。79 個 leaf **未解**，
A-VS77（他車型 PROXI 表是否可採）**仍待裁**，且其論據不變。

### 2.4 `Toro226` 之 VF664 版本（V42_R3）四參數命中 0

同名文件之三個版本中，`VF664_V42_R3`（Toro226）**完全未提及該四參數**，
而 `V2_R1`（DT27）／`V2_R2`（HDCC28）皆提及。

**即 VF664 之內容隨版本而異。** 我方需要的是 **R1LR 所用之版本**，
而 R1LR 目錄下**無 VF664**。**該事實使「以他車型之 VF664 推定」更不可靠。**

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | R-VS44′ 轉錄；`dr_conflict.py` 改為三級宣告並逐筆標級別，**DR-15 改 token 級、驗收 4/4 且可失敗**；`DR-24` → `DR-24′`（併入 `<Tdisplay>`，43 leaf）；`writability.tsv` 增 `evidence_note`（8 列 `VF664-inferred`）；`batch04_v2.json`（`-006` 改注入未定義編碼 4）；`batch05.json` **8 條 0 違規**；A-VS81／82／83 登記 |
| **核實無誤** | R1LR 下 1,362 檔內容掃描；`Core HMI` 之 rot=180 OCR 可讀（**00D 再次成立**）；`TLM HMI Document` 確不存在（15 處引用、0 份本體）；VF664 找到（47 筆）但不帶值域 |
| **正確地不動** | **未採用他車型 PROXI 表之值**（A-VS77 仍待裁）；**未複製任何檔案入 `inputs/`**；**未撤回 batch03／batch04 已生成之兩條 DR-15 相關 TC**；**未改 batch01–03 之三條配置相依無效值**（43 包 §3.2 自己認可者）；**未代擬 DR-8 之改寫**；v1/v2/v3 保留 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| **W-68 內容抽取** | pdf → `pdftotext -q`；doc／rtf → `textutil -stdout -cat txt`；xls → `strings`。**xlsx／docx 於 23 輪已以 `zipfile` 掃過** |
| **文字層判準** | pdf 抽出 < **200 字元**者判為「文字層不足」，不計入命中母體，另列其檔名 |
| **OCR（00D 之法）** | `pdftoppm -r 150 -png` → `PIL.Image.rotate(0/180, expand=True)` → `tesseract --psm 3 -l eng`；**兩種角度皆試並比較抽出字元數** |
| W-68(1) | 檔名 `*664*`（全庫）；命中之 docx 以 `zipfile` 讀 `word/document.xml` 去標籤後正則四參數名與 `Front Seats`／`Front And Rear Seats` |
| W-68(2) | 檔名 `*TLM*HMI*`／`*HMI*TLM*`／`*telematic*`；內容 `TLM HMI\|Telematic HMI Document`、`informative popup` |
| W-68(3) | 內容 `\bHDCC\b.{0,40}\bM240\b\|\bM240\b.{0,40}\bHDCC\b`（雙向）、`VC_VEH_LINE` |
| **W-69 閘之宣告** | `OPEN_DR: dict[str, tuple[級別, token 集合, 值正則, 狀態]]`；`guard()` 於輸出階段攔截，回傳 `("DR-CONFLICT", 註記)` |
| **W-69 可失敗性** | `OPEN_DR.clear()` → 重跑 → 復原，三段輸出並列（negative control） |
| W-70(1) 複檢 | 對四批之 `design_method == "Negative / Invalid"` 者，正則 `\$[A-Z0-9_]+\.(\w+)\$\s*=\s*(\d+)\s*\(([^)]+)\)` 取 (signal, raw, label)，查 `DBC_VALS[signal][raw]` 是否存在 |
| W-70(2) 選 leaf | 同 23 輪之逐 Layer 2 輪流；**選入後逐條過 `guard()`**，`DR-CONFLICT` 者移出並記於 `held_out` |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS81** | **DR-20／DR-23** | `TLM HMI Document` 確不存在；15 處引用、0 份本體。型 B 訴求成立且無法以搜尋解除 |
| **A-VS82** | **DR-22′** | VF664 找到但不定義值域；A-VS77 之裁定不因此改變 |
| **A-VS83** | **DR-15** | DR-15 改 token 級後，其標的涵蓋 batch03／batch04_v2 已生成之兩條 TC |

**無新開 DR。** `DR-24` 改寫為 **`DR-24′`**（併入 `<Tdisplay>`，43 leaf），原文保留加註。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS81／82／83） | **82**（相異編號；最大號 A-VS83，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0 新開**；DR-24 → DR-24′ 改寫 | 未結 **13** |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。

**分析層側核對（43 包）**：43 包開立 anomaly **0 筆**、DR **0 筆**（DR-24′ 為改寫）；**差額 0**。

### 5.2 已生成之 TC 累計

| 批次 | 條數 | 狀態 |
|---|---:|---|
| `batch01_v3` | 8 | **pilot PASS（2026-08-22）** |
| `batch02` | 6 | 待 review |
| `batch03` | 10 | 待 review |
| `batch04_v2` | 10 | 待 review（v1 保留） |
| **`batch05`** | **8** | **本輪產出** |
| **合計** | **42** | |
| 移出／未撰寫 | 8 | `blocked_pending_dr.json` ＋ batch05 之 `held_out` 2 條 |

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **`Core HMI Logic and Flow` 只 OCR 了前 3 頁（共 21 頁），未全文抽取。**
   本輪只做**探測**以確認其須旋轉 180°。
   **其餘 18 頁未抽，故「`informative popup` 不在該檔中」未經證實** ——
   本輪之 `informative popup` 命中 4 全來自有文字層之 CFTS 文件。
   **另 5 份文字層不足之 pdf（含兩份 `CFTSMV033_CIP_R4` inline）完全未 OCR。**

2. **W-68 之內容掃描限於 R1LR 目錄（1,362 檔）。**
   `VF`／`Development Docs`／`CPAA_spec` 三個頂層目錄之 pdf/doc/rtf/xls
   **未作內容掃描**（僅 23 輪之檔名掃描 ＋ 本輪之 `*664*` 檔名命中後抽取）。
   全庫 5,304 檔中，**本輪內容掃描涵蓋 1,362 ＋ 23 輪之 264 = 1,626 檔**。

3. **A-VS83 之兩條已生成 TC，其影響範圍未量。**
   已知 batch03 之 `-014`、batch04_v2 之 `-031` 斷言請求訊號之 0/1。
   **尚未逐條掃 42 條已生成 TC 中還有幾條觸及該五個 token** ——
   若 DR-15 之答覆為「承載階數」，須逐條回溯者不止那兩條。

4. **`TwoStagesHeatedSeat-057` 之 ER 只斷言畫面圖示狀態，未斷言其驅動。**
   條文為 `press the heated seats icons … status shall follow (off -> high -> low -> off)`。
   本層將其寫為純畫面層驗證以避開 DR-15。
   **惟「按壓圖示」與「請求訊號送出」之因果是否可分離，未經 review 確認** ——
   若不可分離，該條亦落在 DR-15 之標的內。
