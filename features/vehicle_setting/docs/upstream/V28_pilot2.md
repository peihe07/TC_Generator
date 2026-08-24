# 上繳 V28 —— W-VF68：四形態查證、pilot #2 十條、分類式錨點、A-VF21 修法

對應下放包：`docs/handoff/V28_batch_reform.md`
（4051 bytes，mtime 2026-08-24 10:59:45，sha256 前 16 碼 `4b17cc6cc238f18b`）。
**併入執行**：W-VF65／W-VF66／W-VF67（其下放包 V27 之落檔見上繳 `V27_rulings_landed.md`）。

**產出**：`generated/vf230_pilot2.json`（10 條，seq 258–267）。
**落檔**：R-VF74／R-VF75／R-VF76、A-VF22／A-VF23／A-VF24，A-VF21 關閉。

---

## 1. §2.1 範例查證（R-VF74）—— 五項，先於 TC 呈現

| # | 標的 | 實測 | 處置 |
|---|---|---|---|
| 1 | 訊號送出型之書寫式 | **有先例，154 例** | **不回退**（首答為偽，見 §4） |
| 2 | 訊號上行型之畫面斷言 | **有先例，353 行 `Send CAN:`** | 依先例 |
| 3 | 設定顯示與修改型 | **查無（0 行）** | 回退 pilot #1 v4 正向式，逐條具名 |
| 4 | 訊號送出型 318 條之二式比例 | 見下 | 本批涵蓋二式，**純 propId 之 22 條未涵蓋** |
| 5 | 「其他」殘餘 4 條之性質 | 見下 | 具名，未改分類式 |

### 1.1 第 1 項 —— 逐字實例（複查後）

書寫式為**單一步驟**，刺激與訊號斷言合併：

```
SWE1-VC-TwoStagesVentedSeatsManagement-045
  P: 3. Press the right front vented seat icon and check that
        TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is transmitted
  E: 3. TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is sent

SWE1-VC-TwoStagesHeatedSeat-058
  P: 3. Press the left front heated seat icon and check that
        TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 3 (Heated_seat_high) is transmitted
  E: 3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 3 (Heated_seat_high) is sent
```

全母體 **154 例**，其 procedure 起首動詞為 `Press` 134／`Read` 20。
**Android 屬性層之名詞（`propId`／`setProperty`／`CarPropertyManager`）Part 1 確為 0 行**
—— 該事實屬實，**惟其不蘊含「書寫式查無」**（§4）。

### 1.2 第 2 項 —— 逐字實例

```
SWE1-VC-Stop-StartSystem-005
  P: 3. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 7 (ENS disabled) and check that
        all heat and vent switches are greyed out
  E: 3. All heat and vent switches are greyed out

SWE1-VC-OneStageHeatedSeat-041
  P: 1. Send CAN: STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off)
     2. Press the left front heated seat icon and check that the icon status changes to high
  E: 1. STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off) is sent
     2. The icon status changes to high
```

### 1.3 第 3 項 —— 查無

`displayed and modifiable`／`allow … modify` 之斷言於 Part 1 **0 行**。
依 V28 §2.1 之表回退為 pilot #1 v4 之正向式，seq 266／267 之 remarks 逐條具名。

### 1.4 第 4 項 —— 二式比例

| 形態 | 條數 | 佔比 |
|---|---|---|
| `MESSAGE.Signal` 式 | 189 | 59% |
| **二式皆有** | 75 | 24% |
| 皆無（訊號名於他處） | 32 | 10% |
| **純 `propId` 式** | 22 | 7% |

本批 4 條之涵蓋：seq 260／261 **二式皆有**、seq 262／263 **`MESSAGE.Signal` 式**。
**未涵蓋者：純 `propId` 式之 22 條（7%）** —— 其條文只有 Android 屬性層之寫法，
**無 `TELEMATIC_*` 訊號名可取**，故其 TC 之訊號從何而來，本批未驗。
**本層判其為 pilot #2 之一個真缺口**（§6 第 1 項）。

### 1.5 第 5 項 —— 「其他」4 條逐條

四條**全為 `TimeandDateSettings`**（`-003`／`-006`／`-007`／`-008`），
皆用**第三種訊號命名空間** `<Name>.Info`：

```
-003  … send the selected values to the Date & Time Service using the signals
      Hour1_Setting.Info, Hour2_Setting.Info, Minute1_Setting.Info, Minute2_Setting…
-006  … shall update the GPS_Automatic_Time_Adj_Setup.Info signal based on the
      customer input from the LTM or ETM screen. When the customer chooses to disable…
-007  （同 -006，enable 方向）
-008  … shall default the GPS_Automatic_Time_Adj_Setup.Info signal to Off during
      initialization … send the default Off signal state to HW
```

**其實質為訊號送出型**，未落入該類係因分類式之 `SIG_OUT` 只認
`TELEMATIC_VEHICLE_SETUP*` 與 `setProperty()`。
**本輪未改分類式** —— 其改動會動到 318／124 之分界，屬全池重算，
且該 4 條不在本批之內。**具名待裁**：`<Name>.Info` 是否併入訊號送出型。
**另具名一項未查**：`Hour1_Setting.Info` 等**是否為 CAN 訊號**（DBC 內查無同名），
其可能為 service 層之介面而非匯流排訊號 —— 若是，則其形態為第七種。

---

## 2. §2.2 pilot #2 —— 十條

`generated/vf230_pilot2.json`。取樣依上繳 V26 §3 之表（已核可），**未調整任一 leaf**。

| seq | leaf | 形態 | W | Pri | spec_ref | 值域來源 |
|---|---|---|---|---|---|---|
| 258 | Blind Spot with Trailer Detection-046 | PROXI 型 | **W1** | P0(c) | `…PDT27_VF_6579` | 0-CLAUSE ＋ `PENDING: DR-34` |
| 259 | ParkSense-085 | PROXI 型 | W0 | P0(c) | `…PDT27_VF_6676` | 0-CLAUSE |
| 260 | PowerLiftgate/TailgateAlert-018 | 訊號送出型 | W0 | P0(a) | `…PDT27_VF_5852` | 2-DBC |
| 261 | IlluminatedApproach-004 | 訊號送出型 | W0 | P1 | `…PDT27_VF_5838` | 2-DBC |
| 262 | SWITCH1Type-002 | 訊號送出型 | W0 | P2 | `…PDT27_VF_6132` | 2-DBC |
| 263 | BlindSpotAlert-004 | 訊號送出型 | W0 | P0(c) | `…PHDCC27_VF_5704` | 2-DBC |
| 264 | SuspensionServiceMode-006 | 訊號上行型 | W0 | P0(a) | `…PHDCC27_VF_5876` | 2-DBC |
| 265 | Blind Spot with Trailer Detection-049 | 訊號上行型 | W0 | P0(c) | `…PDT27_VF_6582` | 2-DBC |
| 266 | Language-059 | 設定顯示與修改型 | W0 | P2 | `…PHDCC27_VF_3608` | （條文無值） |
| 267 | TimeandDateSettings-002 | 設定顯示與修改型 | W0 | P2 | `…PHDCC27_VF_5461` | （條文無值） |

**spec_reference 10/10 全解**（R-VF68 之錨鏈）。
**priority 不寫死**（A-VF17 之教訓）：由 `vf230_wvf45_priority` 之判準推得，
檔頭之分布字串亦由逐條實測算出。

**六個訊號之 raw→label 全數取自 DBC 逐字**：
`PLGAlert_Req 0=Off`／`Illuminated_Approach_Req 0=Zero`／`AUX1_TYPE_Req 0=Latching`／
`BSDEnable_Req 0=Not_Enable`／`Susp_Tire_Jack 0=Off,1=On`／
`Trailer_detection_blind_spot 0=Auto,1=Max`。

**刻意不涵蓋者，逐條具名於 remarks**：
- seq 264：「within the defined system response time」**未定量** → 不斷言時間
- seq 265：`<TDisplay>` **未解之符號** → 不斷言時間
- seq 266：「according to the configured market/language settings」**無市場對映表**
  → 不斷言選項清單之內容
- seq 267：「Radio HMI L&F guidelines」**不在交付集內** → 不斷言外觀樣式

**一項推導須覆核**：匯流排前置之名。Part 1 之式為
`CAN-B is connected to the bus simulator with signal tracing enabled`（59 例）／
`BH-CAN …`（21 例），其命名依 DBC 檔名（`…R4_BHCAN.dbc` → `BH-CAN`）。
本批之訊號皆在 `PDT27_E2A_R5_FDCAN8.dbc`，依同一慣例推得 **`FD-CAN8`** ——
**此為推得而非交付本逐字**。

---

## 3. §2.3 分類式三錨點（R-VF21／R-VF28）—— 全過

```
必命中             SWE1-VC-SuspensionServiceMode-006      期望 訊號上行型   實得 訊號上行型   ✅
必不命中           SWE1-VC-BlindSpotAlert-004             期望 訊號送出型   實得 訊號送出型   ✅
鑑別（已知失效點） SWE1-VC-SuspensionAutoEntryorExit-090  期望 PROXI 型     實得 PROXI 型     ✅
```

以**內容**定錨，不以行號（R-VF28）；錨點不符即 `SystemExit`。
錨點之 leaf 不存在時亦判失敗（「其值恆為無，不構成錨點」）。

---

## 4. ⚠ §2.1 第 1 項首答為偽 —— 本層之錯（A-VF24）

**首答**：查 `propId`／`setProperty`／`CarPropertyManager` 字樣，Part 1 **0 行**，
判「查無 → 依 V28 §2.1 之表回退 `MESSAGE.Signal` 式」。

**其為查錯標的。** 條文之 `propId` 屬 Android 屬性層，**TC 本就不寫該層**，
故以其為搜尋鍵**必然得 0**，該 0 不含任何資訊。
真正該查者為「以顧客操作為刺激、斷言 HU 送出訊號」之**測試書寫式**，其有 **154 例**。

**其後果不止於記述**：本層據該偽「查無」自創了
`Monitor the CAN bus and check that … is transmitted` 一式，
而 **`monitor` 為 canon §5.1 之禁用動詞** ——
**在先例存在時自創，且自創之式違規**。

**其被攔之途徑**：`vf230_selfcheck_wvf62.py`（canon 判準），**非本層之查證**。

---

## 5. ⚠ 自檢判準與被驗內容同出一手（A-VF23）—— 本輪最重之方法缺陷

本層為 pilot #2 另寫 `vf230_wvf68_selfcheck.py`，11 項**全過**，
且依 A-VS106 之對治**逐項施以刻意破壞，11 項皆證明能失效**。

旋依 V28 §2.5 之令改跑既有之 `vf230_selfcheck_wvf62.py`，**報違規 17 筆**：

| 類 | 筆 | 內容 |
|---|---|---|
| §5.1 禁用動詞 | 4 | `monitor`（seq 260–263） |
| §4.3 標題長度 | 6 | 15–18 字，逾 2–14 |
| §R-VF70 前置分類 | 2 | `… = 0 (Off) is being received` 不可歸入 canon §4.4 四類 |
| §5a 檔頭計數 | 4 | `selection` 未載 priority 分布 |
| 其他 | 1 | 同上 |

**可失效測試救不了它。** 11 項皆能失效 —— 惟其**所驗之判準本身**
係本層依自己寫出之內容反推而得，故「內容合判準」為套套邏輯。
**與 A-VF17 同因異形**：A-VF17 是自檢驗證自己寫死之值，本項是自檢驗證自己訂出之**規範**。

**修法**：項 1 刪去自撰白名單，改**直接呼叫 `vf230_selfcheck_wvf62.check()`**
—— canon 判準不另立第二份。訊號斷言專屬之 10 項（canon 未涵蓋者）保留為增項。

**另修一項**：可失效測試之破壞字串會隨產出改寫而失效
（項 9 之破壞針對已被改掉的 `Monitor the CAN bus`，破壞未生效而報「該項無法失效」）。
**已加前置斷言**：破壞後之副本須與原檔不同，否則判「此測試本身無效，非該檢查項無效」。

**現況**：canon 判準 **0 筆違規**；增項 10 項 **0 筆**；
**11 項之可失效測試全過**（`vf230_pilot1.json` 定稿複跑亦為 0）。

---

## 6. §2.4 A-VF21 二項修法 —— 已執行

**一、W2(a) 補跑**（`vf230_wvf44_writability.py` 增 `NOTE_ONLY` 或全文 < 120 字元）：

| | 重跑前 | 重跑後 |
|---|---|---|
| W0 | 593 | **592** |
| W1 | 28 | 28 |
| W2 | 6 | **7** |

**逐級差異恰 1 筆**：`SWE1-VC-E-Save-095` W0 → W2，blocker `B7-no-testable-content`。
**同型者複驗數 1**（依 R-VF75 之令複驗，未沿用 V26 之數）。
**選池 621 → 620**。該 leaf 不在 pilot #2 之取樣內，故取樣表不受影響。

**二、條文委派語路徑**（`scripts/vf230_wvf68_delegphrase.py`）：

```
1 條命中（獨立表，既有 627 個 `no` 不動）
  SWE1-VC-E-Save-095  [managed in ] -> CFTS 088  在 features/ 之下：否
      「E-Save Note: This is not HMI setting in radio. This is managed in CFTS 088」
```

→ `docs/reports/vf230_deleg_phrase.tsv`。
**既有 `vf230_delegation.tsv` 627 列全數 `no` 零改動**（`git diff` 為空，已複核）。
判準之四式（`managed in`／`defined|specified|described|covered in`／
`refer to`／`handled|implemented by`）**為已知集合，非全集**（R-VF71 三）。

---

## 7. 落檔與清理

**條文**：R-VF74、R-VF75（V27）、R-VF76（V28），皆逐字轉錄並附執行層註。
**異常**：A-VF22（PROXI 參數名二式）、A-VF23（自檢判準同出一手）、
A-VF24（查證標的錯置）；**A-VF21 記其處置與關閉**。

**R-VF76 之執行層註**：其生效前提為 pilot #2 通過，**現尚未生效**。
**量產選池為 620**（非 621），扣 pilot #1／#2 之 20 條後餘 **600**，
依 50 條／批為 **12 批**、3 批一上繳為 **4 次上繳**
（V28 §3 之「13 批、5 次上繳」係以 621 池未扣 pilot 計）。

**檔案清理（V28 §3，Pei 已允）**：
- `vf230_pilot1_v4.json` → **`vf230_pilot1.json`**（`git mv -f`，覆蓋舊 v2）
- `vf230_pilot1_v3.json`（`git rm`）／`vf230_batch01.json`（未入版控，`rm`）
- 二個 `*.HEAD_V19` sidecar（未入版控，`rm`）
- **另修二個仍指向舊檔名之活腳本**：`vf230_selfcheck_wvf62.py` 之預設路徑、
  `vf230_wvf64_select.py` 之 pilot #1 排除來源。二者複跑正常。
- **具名一處斷鏈**：`vf230_wvf63_pilot1v4.py` 之輸入 `vf230_pilot1_v3.json` 已刪，
  **該腳本已不可重跑** —— 即 **R-VS53（產物須可自 driver 重製）之一處斷鏈**，
  已於該檔檔頭具名。**其為執行 V28 §3 之必然代價，非疏漏**；
  若分析層認 R-VS53 不可讓，則該刪除須撤回。

**共用檢查點**（`grade_overrides.py --check`）：
2 PASS／2 FAIL —— `R-VF10 編號唯一性` 9 項（已知 A-VF10，含 R-VF70 之作廢重號）、
`R-VF48 引用而無定義` 2 項（`A-VS2` 於 `docs/INDEX.md`、`DR-11` 於 `framework.md`）。
**二者皆非本輪新增**（本輪未動該二檔）。**未抑制，exit code 非 0**。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有五項，其中二項本層判為 blocking。**

1. **⚠ 純 `propId` 式之 22 條，pilot #2 未涵蓋。**
   其條文**只有** Android 屬性層之寫法，**無 `TELEMATIC_*` 訊號名**。
   本批 4 條之訊號名皆由條文直接帶出；該 22 條之訊號名**從何而來，本批未驗**。
   若其須由 propId 反查 DBC，則其依賴上繳 V27 §6 第 1 項之未解對映。
   **本層判其為 blocking**：量產若含該 22 條，其書寫式**未經任何 pilot**。
   **建議**：量產前補一條該式之 pilot，或將該 22 條先行隔離。

2. **⚠ 「其他」4 條之 `<Name>.Info` 於 DBC 查無同名。**
   其可能為 service 層介面而非 CAN 訊號 —— 若是，則為**第七種形態**，
   且其 TC 無法以 `Send CAN:` 書寫。**本層判其為 blocking**（對該 4 條而言）。
   **本輪未查**其於 LID 或他來源之歸屬。

3. **匯流排名 `FD-CAN8` 為推得，非交付本逐字。**
   其影響 pilot #2 之 6 條前置。**若交付本另有命名，6 條須改。**

4. **PROXI 參數名之二式（A-VF22）未裁。**
   pilot #1 定稿內部即不一致，pilot #2 取條文逐字 —— **三種寫法現同時存在於交付物**。

5. **R-VF74「二者皆無 → 停手」之分支從未被觸發，其行為未經實測。**
   四種形態皆得先例或有可回退之式。**一個從未執行過之分支，
   其行為與其不存在不可分辨** —— A-VS106 之同一形態。本層無法自證其會停手。

**另附一項非缺口之觀察**：seq 258 判 W1 而其被驗之值 `"Present"` 由條文逐字帶出。
依 R-VS47／R-VS71 之字面，W1 成立（未解者為值域全集，非驗證標的），
**惟該 TC 實際上完全可執行** —— W1 之標記在此**不指示任何執行障礙**。
本層依既有分級照寫、未自行改判，具名之。
