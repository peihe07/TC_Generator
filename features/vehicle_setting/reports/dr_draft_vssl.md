# Data Request —— VF230／BedLowering／VehicleCategory 三事

**狀態：草稿。DR 號由 Pei 於送出時依台帳取。**
提出層：Tier 1（執行層）　日期：2026-09-02
依據：`docs/fw036/handoff/down/20260902_VS-SL-03.md` §3

本文面三節可整體轉寄，亦可拆節分寄。每節之「查無」皆依 R-G13 三要件
（何處查／如何查／結果）書寫；未達三要件者一律記「未查得」，不寫成「無」。

---

## 一、9 個設定項顯示名於兩份上游皆無對應（VF230，涉 37 列）

### 查證方法（三要件）

| 要件 | 內容 |
|---|---|
| 何處查 | (1) `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` 分頁 `Settings`，攤平後 **517** 個設定項；(2) `R1L FIP 总控表 V1.1.0.xlsx` 分頁 `FeatureSet(Gen4-5)` D 欄 **278** 列 |
| 如何查 | 去 `*`、去括號註、非英數字轉空白、小寫、壓空白後**逐字相等**；另以空白不敏感之鍵作第二輪 |
| 結果 | 下列 9 名兩輪皆零命中。其餘 45 名已由 Tier 2 提出候選並經 Pei 2026-09-02 認可，不在本 DR 之列 |

### 標的

| # | 設定項顯示名 | 涉列 | TC 引用原句（首列） | 首列 `Requirement or Design ID` |
|---:|---|---:|---|---|
| 1 | `Rear Guidance Lighting with Approach` | 5 | `Read the Vehicle Settings menu and check that the "Rear Guidance Lighting with Approach" customer setting is not displayed` | `SWE1-VC-RearGuidanceLightingwithApproach-078` |
| 2 | `E-Save` | 2 | `… check that the "E-Save" customer setting is not displayed` | `SWE1-VC-E-Save-090` |
| 3 | `Charge Power Level` | 6 | `Set the "Charge Power Level" customer setting to Level1 and check that TELEMATIC_VEHICLE_SETUP.PwrLevReq = 0 (Level1) is transmitted` | `SWE1-VC-ChargePowerLevel-046` |
| 4 | `Warnings for Low Fuel Inverter Shutdown - Visual Warning` | 5 | `… check that the "… - Visual Warning" customer setting is not displayed` | `SWE1-VC-WarningsforLowFuelInverterShutdown - VisualWarning-115` |
| 5 | `Warnings for Low Fuel Inverter Shutdown - Audible Warning` | 5 | `… check that the "… - Audible Warning" customer setting is not displayed` | `SWE1-VC-WarningsforLowFuelInverterShutdown - VisualWarning-121` |
| 6 | `Enhanced Display Synchronization` | 6 | `… check that the "Enhanced Display Synchronization" customer setting is not displayed` | `SWE1-VC-EnhancedDisplaySynchronization-127` |
| 7 | `Max Power Level` | 4 | `… check that the "Max Power Level" customer setting is displayed` | `SWE1-VC-MaxPowerLevel140` |
| 8 | `Time and Date Settings` | 3 | `… check that the "Time and Date Settings" customer setting is displayed` | `SWE1-VC-TimeandDateSettings-002` |
| 9 | `Unit Energy` | 1 | `… check that the "Unit Energy" customer setting is displayed` | `SWE1-VC-UnitEnergy-039` |

兩名另有部分線索，一併列出以免上游重複查證：

- `Rear Guidance Lighting with Approach`：HMI `15. Lights` 分類**無同名項**；总控表
  No.272／No.275 分別為 `Cargo Lights`／`Light Status`，**非此項**。
- `Time and Date Settings`：HMI `7. Clock` 為**分類**（r355–r375），其下無單一同名項；
  总控表無對應列。**疑為分類級之引用**，請確認 TC 所指為該分類或其下某一項。

### 所求

上列 9 名之正式對應名（HMI Settings List 之項名與其路徑、FIP 总控表之 `No`），
或確認其於 R1L 不存在。**在收到回覆前，該 37 列之 PROXI 前置一律填 `PENDING`，不猜值**（R-13）。

### 附帶請上游一併確認之二處疑似筆誤（非本 DR 主體）

1. `SWE1-VC-WarningsforLowFuelInverterShutdown - **Visual**Warning-121` 之
   `Test Item` 與步驟所述皆為 **Audible Warning**，ID 之字樣與內容不符。
2. `SWE1-VC-MaxPowerLevel140` 缺序號前之連字號（他列皆為 `…-140` 形制）。

---

## 二、VehicleCategory：`Camera App` 之需求與架構相衝（涉 2 列）

### 需求側（037／TC 原文，逐字）

```
r23  SWE1-HMI-VC-008
     VC3.) If the vehicle has the Camera App (see Camera HMI Logic and Flow),
     Cameras will appear as a tab.
     （括號下半：Presence of the Cameras tab, delegating the Camera App behaviour itself）

r24  SWE1-HMI-VC-009
     VC3.1.) If the Camera tab is present, remove Cameras from the Controls tab.
     （括號下半：Suppression inside the Controls list, the second consequence of the same trigger）
```

### 架構側（`R1L FIP 总控表 V1.1.0.xlsx` `FeatureSet(Gen4-5)`，逐字）

```
No.196  Cam App        Atlantis（DT）欄： Always false
No.7    Backup Cam     Atlantis（DT）欄： If ”Rear_View_Camera" is [Set] ,
                                          return value is true.
                                          Other return values are false
```

### 執行層之判定與其限度

原文逐字寫 `the Camera App`，與总控表 **No.196 `Cam App`** 同名，且明指
`see Camera HMI Logic and Flow`（App 層），`Backup Cam`／`Rear_View_Camera`
**在該 2 列原文中未出現** —— 故判為 `Cam App`。

**惟 `Cam App` 之 Atlantis 欄為 `Always false`**：若其成立，Cameras tab 於 DT 永不出現，
`VC3.)` 之前提即不可能滿足，`VC3.1.)` 亦無從觸發。

### 所求

1. `VC3.)` 所稱之 `Camera App` 是否即总控表 No.196 `Cam App`？
2. 若是，`No.196 = Always false` 與 `VC3.)` 何者為準？（前者成立則該 2 條 TC 應除役）
3. 若否，請示其正確之 PROXI 參數與值。

---

## 三、BedLowering：DT 車型適用性，需求側與架構側直接衝突（涉 23 列）

執行層已依 `down/20260902_VS-SL-02.md` §1 查證 **8 檔**，結論為
**有 1／無 1／未提及 6**；8 檔中**無任何一檔同時陳述兩者並作出取捨**。
全文見 `features/bed_lowering/reports/bl_dt_applicability.md`。

### 需求側（`FM-WI-FSM-037-A03-N1L-SWE1-BedLoweringMode-HMI-V0.1 STLA 報告.xlsx`，SHA256 前 16 `8d09ab46e69da3ad`）

分頁 `Analysis Report`，`Requirement Title`／`Description` 逐字：

```
r8   DT Bed Lowering Control
r9   DT Bed Lowering Entry
     The system shall provide a Bed Lowering feature entry for DT vehicle configuration
     in the head unit, so that the user can request the Bed Lowering function through the HMI.
r10  Front Suspension Raise Request
     When the user triggers the DT Bed Lowering feature entry from the head unit, the system
     shall issue a control request to raise the front suspension.
r11  Rear Suspension Lower Request
     When the user triggers the DT Bed Lowering feature entry from the head unit, the system
     shall issue a control request to lower the rear suspension.
r12  Coordinated Lowering Operation
     The system shall coordinate the front-suspension raise action and rear-suspension lower
     action as one Bed Lowering operation for DT.
```

另 `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021).xlsx`
（SHA256 前 16 `487354fa935dbc53`）`Basic Report` r3／r4 逐字：

```
r3  DT : An App/Control which raises the front suspension and lowers the rear suspension
        to allow the truck bed to be sprayed out and for the debris and water to run out …
r4  DJ/D2 : An App/Control which lowers the rear suspension only for the same use cases.
```

### 架構側（`Sys3_ProSys_SoftwareSystem-Architecture_Specification_Appendix_BV.xlsx`，SHA256 前 16 `41ce5544e1a8c8e7`）

分頁 `FeatureSet list(Gen4_Gen5)` r41（`No` = 36，`Feature Name` = `Bed Lowering Mode`）。
欄頭經合併儲存格解出後為：`O` = Atlantis「in DT」、`Q` = PNet「in DT」、`R` = PNet「in D2/DJ」。

```
N  CAN node 27 (ASM/ASCM)
   Body_Types
O  If "CAN node 27 (ASM/ASCM)" is [Present] and "Body_Types" is ([Type 1] or [Type 4])
   , return value is true.
   Other return values are false.
P  BLM_PRSNT (Bed Lowering Mode Softkey present)
Q  Always false
R  If "BLM_PRSNT (Bed Lowering Mode Softkey present)" is [Set], return value is true.
   Other return values are false.
S  Same as DT
```

`Body_Types` 之值表（`PROXI_HDCC27_R3_20250424.xlsx` `Format` r1019，逐字）：

```
 0 = Absent    1 = Type 1 - D2    2 = Type 2 - DD    3 = Type 3 - DF
 4 = Type 4 - DJ    5 = Type 5 - DP    6 = Type 6 - DX    7 = Type 7 - DT
```

**即：Atlantis 之 DT 欄不含 `Type 7`，PNet 之 DT 欄為 `Always false`，兩者皆排除 DT；
`R1L FIP 总控表 V1.1.0.xlsx` 三張 FeatureSet 表與此一致。**

### 所求

1. SWE1（037，r8–r12 五條 DT 專屬 `shall`）與 Sys3（Appendix BV r41）對 **DT 是否具備
   Bed Lowering Mode**，以何者為準？
2. 若以需求為準，請示 Appendix BV r41 之 `Body_Types` 條件是否應補入 `Type 7`。
3. 請示 BedLowering 交付本車型欄 **T（`HDCC27 Atl-Hi`）** 與 **U（`DT27 Atl-Hi`）** 之應填值
   —— 該二欄現於 151 列**全空**（V–Z 五欄亦同），為交付前必補項。

### 本層現況（未確認前之處置）

- 23 列（DT 專屬 7 ＋「DT 或 DJ/D2」16）**保留不刪**，其追溯之 `shall` 仍在（canon §8.1）
- 151 列之 Pre 已加 `PROXI CAN node 27 (ASM/ASCM) = 1 (Present)`
- `Body_Types` 行一律 `PENDING`，車型欄**不填**，待本 DR 回覆

---


## 四、9 個設定項之顯示條件於 FIP 总控表未載（VF230，涉 25 列）

**本節於 2026-09-02 補入，同日依 `down/20260902_VS-SL-04_review.md` §2 縮節。**
原列 11 名 32 列；其中 `Engine Off Power Delay`（4 列）與 `Automatic Trailer Light Check`（3 列）
之否定式條件已由**規格值表內之 EP 代表值**解決（FO §8.3），**自本節移除，不再問上游**。
既有一～三節不動。

與第一節之別：**第一節問的是「名字對不上」，本節問的是「名字對得上、但顯示條件沒人寫」。**
本節 9 名**全部於 HMI Settings List 有逐字或已認可之對應項**，
僅 FIP 总控表 `FeatureSet(Gen4-5)`（278 列）無其顯示條件。

### 查證方法（三要件）

| 要件 | 內容 |
|---|---|
| 何處查 | (1) HMI Settings List `Settings`（攤平 517 項）；(2) 总控表 `FeatureSet(Gen4-5)` D 欄 278 列；(3) TC 之需求原文（`Test Item` 欄） |
| 如何查 | 先以設定名逐字比對；名不同者以 Pei 2026-09-02 認可之別名綁定所指之列為準；三者皆查畢方判 |
| 結果 | 下列 9 名之 HMI 項確定，**FIP 无對應列或其參數於值表查無**；需求原文亦無 `$var$ = [label]` 之 PROXI 條件式 |

### (a) FIP 无對應列（8 名，22 列）

| 設定項 | 列 | HMI 對應（本層已驗） | TC 引用原句（首列） |
|---|---:|---|---|
| `Park Sense Rear Volume` | 4 | Settings r311 `Safety & Driving Assistance > Rear ParkSense Volume` | `Set the "Park Sense Rear Volume" customer setting to Low and check that TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req = 0 (Low) is transmitted` |
| `Park Sense Front Volume` | 4 | Settings r310 `… > Front ParkSense Volume` | `Set the "Park Sense Front Volume" customer setting to Low and check that TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req = 0 (Low) is transmitted` |
| `New Speed Zone Indication` | 4 | Settings r281（逐字命中） | `Set the "New Speed Zone Indication" customer setting to Off and check that TELEMATIC_VEHICLE_SETUP.New_Spd_Zone_Ind_Req = 0 (Off) is transmitted` |
| `Navigation Turn by Turn` | 3 | Settings r179 `Display > Navigation Turn-by-Turn Displayed in Cluster` | `Set the "Navigation Turn by Turn" customer setting to Off and check that TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req = 1 (Off) is transmitted` |
| `Suspension Service Mode` | 3 | Settings r562 `Suspension > Service Mode` | `Set the "Suspension Service Mode" customer setting to Off and check that TELEMATIC_VEHICLE_SETUP.Susp_Tire_Jack_Req = 0 (Off) is transmitted` |
| `Language` | 2 | Settings r23（逐字命中） | `Read the Vehicle Settings menu and check that the "Language" customer setting is displayed` |
| `Signature Lighting` | 1 | Settings r506（逐字命中） | `Read the Vehicle Settings menu and check that the Signature Lighting setting is displayed as DISABLE`（原文未加引號，逐字照錄） |
| `Hour Mode` | 1 | Settings r359 `Clock > Time Format`（Pei 2026-09-02 認可之近義綁定） | `Read the Vehicle Settings menu and check that the "Hour Mode" customer setting is displayed` |

### (b) FIP 有列但其參數名於 PROXI 值表查無（1 名，3 列）

| 設定項 | 列 | 总控表 | Atlantis 欄逐字 |
|---|---:|---|---|
| `Driver Easy Exit Seat` | 3 | No.148 | `If Easy_Entry_Menù is [Present], return value is true.` `Other return values are false.` |

**問題**：`PROXI_HDCC27_R3_20250424.xlsx` `Format` 之參數表**無 `Easy_Entry_Menù`**，
但有 **`Easy_Entry_Menu`**（無重音，`{0: Absent, 1: Present}`）。
二者僅差一個重音符號，疑為总控表之筆誤 —— **惟依 R-13 不得以語意相近之名代入，本層不自行對應。**

**所求**：請確認总控表 No.148 之 `Easy_Entry_Menù` 是否即 PROXI 之 `Easy_Entry_Menu`。
若是，建議上游修正总控表之字樣。

### 本層之處置

此 25 列之 `proxi_proposed` 一律 `PENDING`，沙盒稿之 Pre-Condition 亦寫 `PENDING`，不猜值。
逐列見 `features/vehicle_setting/reports/_v4_branch3_resolution.tsv`（`resolution = R3`）。
