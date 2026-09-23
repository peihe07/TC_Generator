# NR1L-RVC-056 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2197`（來源列 `SYS-RA-VF551_V42-230`）

## test_item 上半（verbatim，SYS2 逐字）

> implement a warning text overlay that displays the text "Check Entire Surroundings" for a time equal to T_INITDISPLAY since the LTM displays the Rear View Camera image.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-230` 之 637 分支 —— 與 V2／V3 之差別在**計時起點**：V42 寫 `for a time equal to T_INITDISPLAY since the LTM displays the Rear View Camera image`（自影像顯示起算），V2／V3 寫 `for five seconds`（未明起點），故 ER 之時窗寫法相異，不可折。`T_INITDISPLAY` 之標定值為 **5,0 sec**（V33 §1.14.1 `SYS-RA-VF551_V33-479` 名／`-480` 值／`-483` 單位；V42 同值 `-631`／`-632`／`-635`），與 V2／V3 之 `for five seconds` 同數，ER 因而以 5 秒書寫。`SYS-RA-VF551_V42-258` 與本列來源逐字同句（V42 之另一節），依同義列不另出 TC，plan 已記 covered_by。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；§4.3.1 之逐字忠實優先於 `J` 之版面規則。交付語料實測有前例 —— `features/*/delivered/` 十本之 2223 筆 test_item 首行中，10 筆首字小寫（`power`／`vehicle_setting` 兩本，皆已交付）。見上繳包 §3-3。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the HU display within 5 s of the image appearing and check the warning text
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. The text "Check Entire Surroundings" is overlaid for 5 s from the moment the image is displayed
```
