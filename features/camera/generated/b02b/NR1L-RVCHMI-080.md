# NR1L-RVCHMI-080 — SWE1-RVC-090

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.8.4`（來源列 `NRL-188086`）

## test_item 上半（verbatim，SYS1 逐字）

> Signal strength and battery for each wireless camera is indicated below More AUX button

## reasoning

§27.8.4 之 `for each wireless camera` 須以**兩台**驗得，故前提佈兩台無線相機。兩項指示（訊號強度、電量）各一步，因兩者為相異之可觀察項。`below More AUX button` 為位置之逐字。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. Two wireless AUX cameras are connected
7. PROXI Rear_View_Camera = 1 (Present)
8. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the area below the "More AUX" button and check that a signal strength indication is shown for each connected wireless camera
2. Read the area below the "More AUX" button and check that a battery indication is shown for each connected wireless camera
```

## expected_result

```
1. A signal strength indication is shown for each of the two connected wireless cameras
2. A battery indication is shown for each of the two connected wireless cameras
```
