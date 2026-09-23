# NR1L-RVC-213 — SWE-CAM-019

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1119`（來源列 `SYS-RA-VF551_V33-243`）

## test_item 上半（verbatim，SYS2 逐字）

> the LTM stops to copy the Rear_Camera.Data into Rear_Camera_Repetition.Data (The rearview image shall not be displayed ). Refers for the details to the LTM Algorithm Requirements paragraph and the FMVSS 111 regulation.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-243` 之「LTM 停止將 `Rear_Camera.Data` 複製入 `Rear_Camera_Repetition.Data`，rearview 影像不再顯示」。`SYS-RA-VF551_V33-248` 與本列**逐字同句**（同本之另一節），依同義列不另出 TC，plan 記 covered_by。**來源之時限值未載，不造**（下放包 §3）—— Delay 設為 Off 使「立即停止」可判，ER 以影像消失為唯一可判面。末句之 `Refers … to the LTM Algorithm Requirements paragraph and the FMVSS` 為轉指，不展開（§8.4.2）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
2. Read the HU display and check that no rearview image is displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent
2. No rearview image is displayed
```
