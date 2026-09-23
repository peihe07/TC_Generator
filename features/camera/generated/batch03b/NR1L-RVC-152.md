# NR1L-RVC-152 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1883`（來源列 `SYS-RA-VF551_V2-459`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate FD-CAN8 STEERING1.LwsAngle_SCCM to LVDS vehicleUpdate_2.LwsAngle

## reasoning

驗證目標為 `SYS-RA-VF551_V2-459` 之「HU 將 FD-CAN8 `STEERING1.LwsAngle_SCCM` gate 至 LVDS `vehicleUpdate_2.LwsAngle`」。**`STEERING1` 不在 `forms/` 四本 DBC**（`STEERING` 字面掃描零命中），raw 與 VAL label 標 `PENDING: DR-CAM-f`。**只勾 HDCC27** —— DT27 之同一驗證點其來源為 `V2-745`（`EPS_FD_1.LwsAngle`，`VF551_V2_PDT27` 前綴），另出 `-154`。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the STEERING1 message is not present in the four DBC files in forms
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STEERING1.LwsAngle_SCCM = PENDING (0 degrees)
a. PENDING: DR-CAM-f the raw value and VAL label for 0 degrees are not sourced
2. Read vehicleUpdate_2.LwsAngle and check that it reports the value sent in step 1
```

## expected_result

```
1. The LwsAngle_SCCM signal is reported as 0 degrees
2. vehicleUpdate_2.LwsAngle reports the same value and is sent over LVDS
```
