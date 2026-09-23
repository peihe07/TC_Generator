# NR1L-RVC-207 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2372`（來源列 `SYS-RA-VF551_V42-268`）

## test_item 上半（verbatim，SYS2 逐字）

> stop to copy the ADAS_LVDS_RRCamera_Cable into Rear_Camera_Repetition.Data set Rear_Camera_Enable.Info equal to "False" set the internal variable RVC_ACTIVE equal to "False"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-268` 之「停止複製、`Rear_Camera_Enable.Info = "False"`、`RVC_ACTIVE = "False"`」。與 `-206` 成續顯／停止一對。Delay 設為 Off 使「立即停止」可判。兩個內部旗標不可觀察，以影像消失為後果（§6）。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. The rearview image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 1 (P)
2. Read the HU display and check that no rearview image is displayed
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 1 (P) is sent
2. No rearview image is displayed
```
