# NR1L-RVC-135 — SWE-CAM-009

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_750`（來源列 `SYS-RA-VF551_V2-486`）

## test_item 上半（verbatim，SYS2 逐字）

> · When all of the below conditions hold true: - Vehicle speed below c_VEHSPD_MAX: BRAKE_FD_2.VehicleSpeedVSOSig < c_VEHSPD_MAX, the Head Unit shall perform following actions: e. send vehicleUpdate_2.ZoomViewReq = Not_Pressed as the default.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-486` 之 `e.` 子句。上半為摘句（§4.3.1）：原句 **80 token**，刪 `RVC active on the Radio` 之條件列（其已由 Pre-Condition 3 承載）與其餘四個子句後為 **32 token**，為原句之保序子序列，速度條件與本子句之結果皆保留。**本來源拆為五列而非一列**（§8.2.2「一個 sub-id 可需數個 TC」）——`a.`～`e.` 為五個不同輸入對應五個不同輸出之獨立驗證點；若併為一列，其摘句**無法在 50 token 內同時保留條件與五個結果子句**（CAM-10 §4 升級條件第 3 項），拆列為該條之正解而非規避。供試 raw 205 = 12.8125 km/h = 7.9614 mph（< `c_VEHSPD_MAX` 之 8 mph，profile §9）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
2. Read vehicleUpdate_2.ZoomViewReq without pressing the Zoom Button
3. Read the recording and check the value of vehicleUpdate_2.ZoomViewReq
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. The LVDS link is recorded
3. vehicleUpdate_2.ZoomViewReq = Not_Pressed is sent over LVDS
```
