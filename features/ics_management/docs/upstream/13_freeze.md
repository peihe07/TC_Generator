# 上繳包 13 — 收尾包：probe 三值化、SYS2 反向掃、凍結記錄（2026-08-30）

對應下放包：`docs/handoff/13_freeze.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `f10af8bd35766180661d0a63d7ed46bf74ae9ab0619bea0b5cacba5d44f9d108`**
—— 與執行層自身記錄相符，未停。

**本包 git 執行次數 0**（含唯讀；主實例與二並行實例皆然）。
**E19 觸發**（作業 B）。E20／E21／E1／E9／E18 皆未觸發。

---

## §1 裁決指紋＋前提驗證＋圍籬 diff

### 1.1 前提驗證 —— **P1～P3 全部相符**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | 相異 42、錨點 49；無重複 ruling_id | **相異 42、錨點 49**；無 DUPLICATE | 相符（**E18 未觸發**）|
| P2 | A-ICS 至 83、相異 83、無缺口；DR 20／20 | **A-ICS83**／83／無缺口；**DR 20**／20／無缺口 | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |

### 1.2 圍籬 diff（對 `12_rulings_snapshot.md`，未動用 git）

| 項 | 實測 |
|---|---|
| 快照自證 | 檔頭載 `f18d66f7565239ca`＝本文實算 `f18d66f7565239ca`，**相同** |
| 現行 `RULINGS.md` | `a10e25e21d1010ec` |
| diff | **新增 61 行、刪除 0 行** |
| 新增 `##` 標題 | **`R-ICS42`**（唯一）|
| 刪除 `##` 標題 | **無** |
| `R-ICS42` 於快照中 | **不存在**（與本輪新增相符）|

與預期 #2（新增非 0、刪除 0）**完全相符**。
**不同於 b12 之 `R-ICS40`**：本輪之新增條文在快照中確不存在，時序乾淨，無時序疑義。

---

## §2 作業 A — probe 三值化與全域三層交叉重算（R-ICS42(b)）

### 2-1 【E20 檢查】軸層回歸 —— **未觸發**

2180 個物件之軸層欄位（`id`／`section_no`／`artifact_type`／`ecu`／`radio`／`ee`／
`v1`／`v2`／`verdict`／`strength`／三組 `reasons`／`text`）序列化後與改前**逐字相同**（byte 相同）。
`variant` 欄值域改變者 **0**、`scope` 欄改變者 **0** —— 三值化只動 `variant_fits_dut` 一欄。

### 2-2 舊布林桶之拆解

| 舊值 | 數 | 三值化後 |
|---|---|---|
| `True` | 1734 | `Disassociated` 1734（原封不動）|
| `False` | **446** | **`Associated` 262 ＋ `Unclassified` 184** |

**A-ICS81 之診斷完全成立** —— 舊 `False` 桶正是二者合桶。

### 2-3 全域三層交叉表（v2(b) 適用 **254** 個）
**upstream-11 §4-3 之 138／29／87 三分作廢**，改為四格：

| 變體層 | 範圍層 | 實數 | 章節分佈 |
|---|---|---|---|
| `Disassociated` | 隨變體層 | **138** | §1.8 × 92、§1.15 × 29、§1.9 × 17 |
| **`Unclassified`** | 隨變體層 | **86** | **§1.4 × 86** |
| `Associated` | 算數（R-ICS39，裁決）| **29** | §1.18 × 29 |
| `Associated` | 隨變體層 | **1** | §1.5 × 1 |
| | **合計** | **254** | |

**舊「87」＝ 86 `Unclassified` ＋ 1 `Associated`**，與預期 #7（§1.4 × 86 落於 `Unclassified`）相符。

### 2-4 `4819353` 之覆蓋 —— **無（完全未覆蓋）**

`§1.4.3.2`／`Subsystem Functional Requirement`／v2 適用／`Unclassified`。逐字：

> If the $DCSD_DISP_STAT$ signal is received with an implausible value (values 5 or 6) , the HU shall continue to behave using the last plausible value received. If the HU has not received a plausible data value since exiting Sleep Mode, the HU shall use the value of ON.

三個構成要件於 31 條中之命中：implausible／values 5 or 6 → **0**；last plausible value → **0**；
Sleep 後預設 ON → **0**。錨中含 `4819353` 者 **0**。
**依令登記為覆蓋缺口，未生成。**

**下放包未問而發現者**：31 條中提及 `DCSD_DISP_STAT` 者 **0 條**，
提及 `TGW_DISP_STAT` 者 **8 條**。而作業 C 量得 PDT27 dbc 中承載 `DCSD_DISP_STAT` 者
收方明列 `ETM,LTM`。二者是否同一訊號之不同側命名 —— **不調和，列為待查**。

---

## §3 作業 B — SYS2 反向掃（`docs/reports/13_sys2_reverse_scan.md`）

### 3-1 「23」複數成立

來源欄空白之列 **31**，其中 `Category` = FR **23** —— 與 upstream-12 §3-5 一致，無差異。

| 面 | 分佈 |
|---|---|
| 層 | HW 供應商介面 **22**／HMI 軟體側行為 **0**／不可判 **1** |
| 介面位置 | HU↔DCSD **17**／DCSD 內部 **5**／不可判 **1** |
| HMI 軟體側可驗證 | **是 1**／否 21／不可判 1 |

23 列之四欄已逐字引入報告（`_x000D_`、彎引號、尾隨空白、原文拼字錯誤
`signle`／`Continously`／`Certfication`／`GPOI-0` 皆原樣保留）。

### 3-2 【E19 觸發】

觸發列 **1** 筆：**`NRL-180522`**（xlsx 列 76），逐字：

> Do not filter out duplicate touch (same coordinates) events during continuous press specifically during dragging/swipe.  Needed for Apple CarPlay™ Certfication

另 1 列判「不可判」（`NRL-180512`，列 66）一併具名。
**已依 E19 停下**：未作任何範圍判斷、未生 TC、未動錨、未結 DR、未自取編號。

### 3-3 擴掃 —— **與下放包前提不符一項，未調和**

下放包令「列其來源文件為何（CFTS019？HMI L&F？）」。
**實測：SYS2 來源欄從不含文件名** —— 302 個非空儲存格全部只含 7 位數字；
含 `CFTS020`／`CFTS022`／`CFTS019`／`HMI L&F`／`SYSAD` 字串之列數 **0，查無**。
故該問在此欄上無法回答，**改以「7 位 ID 解析回文件」作等價量測並具名此代換**。

### 3-4 掃描起點盲區之完整盤點

`Basic Report` 資料列 **333**（xlsx 列 2–334）：

| 桶 | 列數 | 十二包以來掃過？ |
|---|---|---|
| ID ∈ CFTS020 之 2180 物件頭 | 260 | 已掃過 |
| ID ∈ CFTS020 但為**節標題錨**（非物件頭）| **42** | **從未掃過** |
| ID ∈ CFTS022 | **0** | — |
| 來源欄空白 | **31**（其中 FR 23）| **從未掃過**（A-ICS78）|
| 合計 | **333** | |

**盲區合計 73 列 ＝ 21.9%**，其中在案 FR **23**（42 列之 FR 數為 **0**，全為 Heading 41 ＋ Information 1）。
42 列已查實非另一來源文件：其 ID 皆在 CFTS020 docx 內文但非物件頭
（docx 全文 2645 種 7 位 token，物件頭僅 2180 種）。

### 3-5 【本包最重之未預料】SYS2 早已自帶逐列之可驗證性判定

**已由主實例獨立複驗欄位存在**：`SYS2 驗證性 Verifiability (Y/N/NA)`（欄 33）、
`SYS2 驗證標準 (Verification Criteria)`（欄 56）、`SYS2 驗證方法 (Verification Method)`（欄 57）。

那 23 列中 **14 列 `Verifiability` = `Y`**、2 列 `NA`、7 列空白；
前 16 列之 `Verification Method` 逐字皆為 `1. System validation`；
`Verification Criteria` 寫的是 HU 側檢查語句
（如 `* Check HU shall with interface with 8.4" display according to the requirement.`）。
此三欄之空白斷點與 `Document ID`／子分類之斷點**完全對齊在 xlsx 列 80**。

**即：本線十三包一路自行推導「可驗證性」，而 SYS2 早已逐列標了答案。**

另：31 個空白列為 **xlsx 列 58–88 之單一連續區塊**（非零星漏填），
主題為 LVDS Backchannel／I2C 觸控介面，其真實出處由報告 §1 #8／#10 逐字指名為
`DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf` —— **該檔全 repo 查無**。
且同區塊內 SYS2 已對 3 列作出 `Out of scope`
（理由逐字：`Responsibility for this functionality lies with DCSD firmware`），
**卻對這 23 列 FR 未作此裁定**。

---

## §4 作業 C — PDT27 dbc 對 DR-ICS16 之填補（`docs/reports/13_pdt27_dbc_vs_dr16.md`）

### 4-1 訊號拼法 —— **佔位字面在三支 dbc 中查無**

`SG_` 名精確等於 `TGW_DISP_STAT` 或 `Telematic_Power` 者**各 0 筆，查無**。實名：

| 實名 | 承載 | 發 | 收（逐字）|
|---|---|---|---|
| **`TGW_DISP_STATSts`** | `BO_ 1500 TELEMATIC_DISPLAY2: 8 ETM` | ETM | `SGW` |
| **`PowerSts_Telematic`** | `BO_ 1470 STATUS_TELEMATIC: 8 ETM` | ETM | `FPDM,SGW` |
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK: 8 SGW` | SGW | **`ETM,LTM`** |

### 4-2 三 DBC 發收方矩陣 ——【E21 未觸發】

| 訊號 | A（PDT27_R1_BHCAN2）| B（R4_BHCAN）| C（FDCAN8）|
|---|---|---|---|
| `TGW_DISP_STATSts` | `ETM`→`SGW` | `SGW`→`DCSD` | `BO_ 1427 TELEMATIC_FD_4` `ETM`→`Vector__XXX` |
| `DCSD_DISP_STAT` | `SGW`→`ETM,LTM` | `DCSD`→`SGW` | **未載** |
| `PowerSts_Telematic` | `ETM`→`FPDM,SGW` | `SGW`→`AMP,ANC,DCSD,ICS` | `ETM`→`TBM` |

三訊號之發收方首尾相接，**全部由 SGW 閘道轉發可解釋**，無矛盾 → **E21 未觸發**。

### 4-3 是否足以定台架觀察點 —— **部分**

1. **下放包預設之「LTM 明列為收方」對二目標訊號不成立**：LTM 只出現於
   `BO_TX_BU_ 1500 : ETM,LTM;` 與 `BO_TX_BU_ 1470 : ETM,LTM;`，語意為**追加發送方**。
2. 收方明列 `ETM,LTM` 者是 `DCSD_DISP_STAT` —— **另一個訊號**。
3. 值名不符：b03 書 `[DISP_OFF]`／`[DISP_NORMAL]`，`VAL_ 1500` 為 `"Display_off"`／`"Normal_mode"`。
4. **該檔未綁定本 feature、`FORMS.md` 登為 `display`、A-DM14 未裁。**
5. 但 A 檔是唯一同時具備 `LTM` 節點、二訊號、且刺激面同檔可見者。

**不採認。** 綁定待 A-DM14。

### 4-4 潛在回收數（**明標為估**）

`$TGW_DISP_STAT$`：上限 **8**、下限 **0**、最可能 **8**（**條數**，非佔位處數）。
`$Telematic_Power$`：**3**（值名 `"Idle"`／`"Full_Operation"` 與 b03 逐字相符）。

### 4-5 【執行層對作業 C 之更正】「12 處佔位不可複現」之質疑**不成立**

作業 C 報「`b03` 全檔 24 次、8／13／24 皆非 12、無任何欄位組合得 12」，
並稱該數自 b05 起被逐包轉抄而原始量測條件查無。

**主實例已獨立複驗，該質疑不成立：**

- `pending_census.py` 之 DR-ICS8 為 **12 處／涉 8 條 TC**；
- 12 個 `PENDING:` 佔位**全數落在 `test_procedure` 欄**（census 口徑為六個交付欄）——
  **作業 C 漏計 `test_procedure`**；
- 其所數之 24，是**訊號名 `$TGW_DISP_STAT$` 之字面出現次數**，非 PENDING 佔位數
  （全檔 `TGW_DISP_STAT` 出現 36 次、`$TGW_DISP_STAT$` 24 次）——
  **兩個不同的量被當成同一個**。

**該數字無誤，不需登記 anomaly，亦未回改任何文件。**

### 4-6 【作業 C 之真發現，與 upstream-07 相對】

**已綁定之 FDCAN8 檔本身即載 `BO_TX_BU_ 1427 : ETM,LTM;`** ——
即**不必採認 PDT27**，已綁之 DBC 中 LTM 已是載該二訊號之 `TELEMATIC_FD_4` 的追加發送方。
這與 **upstream-07「二 DBC 中根本沒有 DUT 發送側」之 E3 依據相對**。**未調和。**

另：A 檔 `BU_` 無 `ICS` 卻仍有 `BO_ 1050 CLIMATIC_PANEL: 8 SGW`，
其 `Radio_btn0` 收方**僅** `LTM` —— 刺激與回應同匯流排可觀察。

---

## §5 作業 D — 凍結記錄（`docs/reports/13_freeze_record.md`）

五節齊備：§1 現況數字（含逐 DR 佔位分佈）、§2 不可現狀出貨之條（逐條附阻因與所繫 DR）、
§3 掛帳十一項、§4 解凍觸發條件（逐 DR 對映）、§5 解凍時第一件事、
§6 交班給 PM／SU／DD 之一句話。

**§2 特別交班之一點**：V1／V2 **無佔位**，故 `pending_census` 不會提醒、`selfcheck` 全綠 ——
**只有凍結記錄會提醒**。連續十包無進展。

---

## §6 作業 E — 常設自檢集

| 項 | 結果 |
|---|---|
| 圍籬 diff | **+61／−0**，唯一新增 `R-ICS42`（見 §1.2）|
| 候選篩 | 原始 **140**／殘餘 **66**／**殘餘率 47%**（前四包 53／53／43／52%）|
| R-ICS34(c) | 五包皆 ≤ 60%，未須重議 |
| 未錨定斷言 | **3（弱驗證）＋ 6（已標明）**，不變 |
| `selfcheck_b01.py` | PASS —— 機檢 19 項 FAIL 0 |
| `verify_verbatim_b01.py` | PASS —— **31／31** |
| `pending_census.py` | **18 處／14 條**，不變 |
| `ledger_guard.py` | 開工前／完工後 exit 0，**逐字相同** |
| 四支 gate | 開工前／完工後**逐字相同**，差**皆 0** |
| 快照 | `docs/reports/13_rulings_snapshot.md` **已產出（凍結基準）**，49 錨點 |

---

## §7 預期數字對照（下放包 §5，17 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；49（相異 42）、A-ICS 83、DR 20／20 | 全數相符 | 相符 |
| 2 | 圍籬 diff | 新增非 0、刪除 0 | **+61／−0** | 相符 |
| 3 | 錨變動／TC 新增／reasoning 變動 | 0／0／0 | **0／0／0** | 相符 |
| 4 | TC 總數 | 31 | **31** | 相符 |
| 5 | 佔位總數 | 18 | **18** | 相符 |
| 6 | 軸層回歸 | 逐字相同 | **逐字相同（E20 未觸發）** | 相符 |
| 7 | 三層交叉表 | §1.4 × 86 落於 `Unclassified` | **§1.4 × 86 於 `Unclassified`** | 相符 |
| 8 | `4819353` 覆蓋 | 有／無／部分＋逐字 | **無**，附逐字 | 相符 |
| 9 | 作業 B | 23 列四欄；擴掃列數 | 23 列齊；盲區 **73 列／21.9%** | 相符（**且 E19 觸發**）|
| 10 | 作業 C | 三 DBC 矩陣；足／不足／部分；回收數 | 矩陣齊；**部分**；估 8 ＋ 3 | 相符 |
| 11 | 作業 D | 五節齊備 | **六節**（多 §6 交班句）| 相符 |
| 12 | 候選篩 | 二數並報＋殘餘率 | 140／66／**47%** | 相符 |
| 13 | 未錨定斷言 | 3＋6 | **3＋6** | 相符 |
| 14 | Test Set 相異值 | 5 | **5** | 相符 |
| 15 | 四支 gate | 差皆 0 | **差皆 0** | 相符 |
| 16 | **git 執行次數** | **0** | **0** | 相符 |
| 17 | 快照 | 已產出 | **已產出** | 相符 |

**17 項全數相符。**（下放包 §3 之一項前提不成立已於 §3-3 具名：SYS2 來源欄不含文件名。）

---

## §8 未結 DR 清單（20 條）

| DR | 現況 | 本包新事實 |
|---|---|---|
| DR-ICS1／3 | OPEN | — |
| DR-ICS2 | OPEN | B5 所繫 |
| DR-ICS4 | OPEN | 1 處佔位 |
| DR-ICS5／7／10／15 | 可結 | — |
| DR-ICS6 | OPEN | 5 處佔位 |
| **DR-ICS8** | OPEN | **12 處佔位之出處已複驗**（`test_procedure` 欄）；作業 C 之質疑不成立（§4-5）|
| **DR-ICS9** | OPEN | V1／V2／V3 所繫；**無佔位故不會自行浮出**，已寫入凍結記錄 §2 |
| DR-ICS11／14／17／19 | OPEN | — |
| DR-ICS12 | 追蹤件 | — |
| DR-ICS13 | 分析層已標「可結」 | 執行層未動 |
| **DR-ICS16** | OPEN（上游急件）| **判「部分」**：LTM 對二目標訊號為**追加發送方非收方**；實名為 `TGW_DISP_STATSts`／`PowerSts_Telematic`；值名不符；**未採認**（§4-3）|
| **DR-ICS18** | 告知／追認件 | 否認則 009 ＋ 15 條加錨退回（凍結記錄掛帳 #3）|
| DR-ICS20 | OPEN | G2／G3 效力所繫 |

---

## §9 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `cfts020_probe.py` 三值化（`variant_fit()`，軸層零變動）；全域三層交叉表重算（254 = 138／86／29／1）；`13_sys2_reverse_scan.md`／`13_pdt27_dbc_vs_dr16.md`／`13_freeze_record.md` 三份報告；`sys2_reverse_scan_13.py`／`pdt27_probe_13.py` 二支腳本；**凍結基準快照** |
| **核實無誤** | E20 軸層逐字回歸；舊 `False` 桶 446 = 262＋184 拆解；「23」複數成立；「12 處佔位」複驗成立（**推翻作業 C 之質疑**）；SYS2 三欄 `Verifiability`／`Criteria`／`Method` 存在（主實例獨立複驗欄索引 33／56／57）；快照自證 sha 相同；圍籬 diff 之 `R-ICS42` 時序乾淨 |
| **正確地不動** | 未生成任何 TC；未改任何錨或 reasoning；`4819353` 登記缺口而不生成；未對 23 列作範圍判斷（E19 停下）；PDT27 只讀不綁定（`feature.yaml`／`FORMS.md` 未動）；未調和 §3-3 之前提不符、§4-6 之與 upstream-07 相對、`DCSD_DISP_STAT` 與 `TGW_DISP_STAT` 之命名關係；未對任何 DR 結案；五簿一字未寫；**git 0 次** |

---

## §10 建議登錄之 anomaly（編號由分析層取）

1. **【重】§3-2 E19：`NRL-180522` 為 HMI 軟體側可驗證之行為**（觸控去重／dragging／swipe，
   Apple CarPlay 認證所需），落在從未掃過之 31 列空白區塊內。範圍屬分析層。
2. **【重】§3-5：SYS2 自帶 `Verifiability`／`Verification Criteria`／`Verification Method` 三欄，
   本線十三包從未量過**，卻自行推導可驗證性。
3. **§3-4：掃描起點盲區 73 列（21.9%）**，其中 42 列為節標題錨、31 列來源欄空白。
4. **§4-6：已綁 FDCAN8 檔載 `BO_TX_BU_ 1427 : ETM,LTM;`，與 upstream-07 之 E3 依據相對。**
5. §4-1：佔位字面 `TGW_DISP_STAT`／`Telematic_Power` 在三支 dbc 中**查無**，
   實名為 `TGW_DISP_STATSts`／`PowerSts_Telematic`，且值名亦不符。
6. §3-3：SYS2 來源欄從不含文件名，下放包 §3 之該項前提不成立。
7. §2-4：`4819353` 未覆蓋；31 條中提及 `DCSD_DISP_STAT` 者 0 條。
8. §3-5：`DCSD_and_HU_LVDS_Backchannel_Protocol_v4.1.pdf` 為 23 列之真實出處，**全 repo 查無**。

**本包未產生任何新裁決條文，未自取任何編號。**

---

## §11 獨立判斷

### 11-1 本包是否仍有該驗而未驗者 —— **有，二項**

1. **`DCSD_DISP_STAT` 與 `TGW_DISP_STAT` 是否同一訊號之不同側命名，未查。**
   若是，b03 之 12 處佔位可能繫錯訊號 —— 這會同時動到 DR-ICS8 與 DR-ICS16。
2. **SYS2 之 `Verification Criteria` 欄與本線 31 條之對照未做**（§3-5）。
   本包只證其存在，未量其與我方 ER 之異同。

### 11-2 【下放包 §6 指定】凍結記錄是否足以讓不曾讀過十三包之人接手

**大致足夠，但缺三件，且其中一件是結構性的。**

**足夠之處**：§1 之數字全部附量法而非轉抄，接手者可逐項自行複算；
§2 逐條列出不可出貨之條與所繫 DR；§4 給了「上游回覆後該做什麼」的對映；
§5 給了開機四步。**尤其 V1／V2 之「無佔位故不會自行浮出」已明白交班** ——
這是自動化工具無法提醒、只能靠文件傳遞的一件。

**缺者三件**：

1. **缺「為何是這 31 條、而不是別的 31 條」的選取邏輯。**
   記錄講了現況與缺口，沒講當初 254 個適用物件如何收斂到 31 條。
   接手者要判斷「還該補哪些」時，沒有可依循的收斂軌跡 —— 這要回讀 b01～b07 才有。
2. **缺失敗史。** 十三包裡有多次自我更正（時間符號三包誤、b03 DCSD 誤、NBSP 因果誤、
   87 個分佈誤、本包作業 C 之 12 處誤）。凍結記錄只寫現況為真，
   沒寫**哪些地方本線特別容易出錯**。接手者很可能重蹈同型之誤 ——
   尤其「節前定義塊要搜、不能只搜需求句」與「布林旗標會合桶」二件。
3. **結構性的一件：記錄本身仍以 CFTS020 為敘事骨架。**
   §6 那句交班說「開工第一件事應盤點掃描起點漏了什麼」，
   但 §1～§5 的組織方式（章節號、ObjectID、錨行）**全部預設了 CFTS020 起點**。
   接手者若照 §5 的四步開機，會**再一次從 CFTS020 進場**。
   要真正治這件，凍結記錄需要一張**以 SYS2 為主鍵**的對照表 —— 本包未做。

**建議**：解凍前補上第 3 件（以 SYS2 333 列為主鍵、標明各列是否已有 TC 覆蓋），
第 1、2 件以附錄形式補齊即可。三件皆不依賴上游。

---

## §12 引用清單

R-ICS1 ~ R-ICS42（七組 v1／v2；實測錨點 49／相異 42）；
A-ICS16、A-ICS31、A-ICS60、A-ICS70、A-ICS74、A-ICS76、A-ICS78、A-ICS80、A-ICS81、A-ICS83；
A-DM14；DR-ICS1 ~ DR-ICS20；R-G13、R-G17、R-G18、R-G25；
FO §8.2、FO §8.4、FO §8.5；IN §7、IN §9、IN §10.7。
