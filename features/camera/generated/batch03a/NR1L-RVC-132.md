# NR1L-RVC-132 — SWE-CAM-009

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_750`（來源列 `SYS-RA-VF551_V2-486`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the below conditions hold true: - Vehicle speed below c_VEHSPD_MAX: BRAKE_FD_2.VehicleSpeedVSOSig < c_VEHSPD_MAX, the Head Unit shall perform following actions: b. display '-' on the Zoom Button when systemStatus.ZoomViewRes = [4X].

## reasoning

驗證目標為 `SYS-RA-VF551_V2-486` 之 `b.` 子句。上半為摘句（§4.3.1）：原句 **80 token**，刪 `RVC active on the Radio` 之條件列（其已由 Pre-Condition 3 承載）與其餘四個子句後為 **35 token**，為原句之保序子序列，速度條件與本子句之結果皆保留。**本來源拆為五列而非一列**（§8.2.2「一個 sub-id 可需數個 TC」）——`a.`～`e.` 為五個不同輸入對應五個不同輸出之獨立驗證點；若併為一列，其摘句**無法在 50 token 內同時保留條件與五個結果子句**（CAM-10 §4 升級條件第 3 項），拆列為該條之正解而非規避。供試 raw 205 = 12.8125 km/h = 7.9614 mph（< `c_VEHSPD_MAX` 之 8 mph，profile §9）。**`systemStatus.ZoomViewRes` 為 RVCM → HU 之 LVDS 訊號**（四本 DBC 零命中），其注入須以 LVDS 模擬器；本 feature 之 bench 是否具備該能力未知 —— 於上繳包 §4 具名為可執行性風險。`SYS-RA-VF551_V2-578`／`-580` 為 Out of Scope（R-CAM9），本包只取其「RVC display active on the Radio」之措辭作 Pre-Condition，不作錨。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The RVC display is active on the Radio
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
2. Set the LVDS signal systemStatus.ZoomViewRes = 4X
3. Read the HU display and check the symbol shown on the Zoom Button
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. The LVDS signal systemStatus.ZoomViewRes = 4X is received by the HU
3. The Zoom Button shows '-'
```
