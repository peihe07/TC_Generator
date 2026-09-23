# NR1L-RVC-052 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1624`（來源列 `SYS-RA-VF551_V33-228`）

## test_item 上半（verbatim，SYS2 逐字）

> when the value of the BED_EXTENDER.BedExtenderSts =(equal) "Not_Active" AND BED_EXTENDER.IncompleteBedExtenderSts =(equal) "False" AND STATUS_BH_BCM.RHatchSts =(equal)"Open", LTM overlaps the related message on the RVC images ("Camera Not in position" see LTM HMI specification document) for T_INITDISPLAY time.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-228` —— 與 `-226` 同一疊加訊息，但條件集多出 `BedExtenderSts = Not_Active` 與 `IncompleteBedExtenderSts = False` 兩項（即「貨斗延伸桿未展開」之情形；展開側由 `NR1L-RVC-032`／`-033` 承接之抑制行為相對）。**`BED_EXTENDER` 不在四本 DBC**（A-CA29／DR-CAM-f），raw 與 VAL label 標 PENDING，寫法沿 `NR1L-RVC-032` 之前例。`T_INITDISPLAY` 之標定值為 **5,0 sec**（V33 §1.14.1 `SYS-RA-VF551_V33-479` 名／`-480` 值／`-483` 單位；V42 同值 `-631`／`-632`／`-635`），與 V2／V3 之 `for five seconds` 同數，ER 因而以 5 秒書寫。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；§4.3.1 之逐字忠實優先於 `J` 之版面規則。交付語料實測有前例 —— `features/*/delivered/` 十本之 2223 筆 test_item 首行中，10 筆首字小寫（`power`／`vehicle_setting` 兩本，皆已交付）。見上繳包 §3-3。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the BED_EXTENDER message is not present in the four DBC files in forms
4. The rear view camera image is displayed
5. STATUS_BH_BCM.RHatchSts = 0 (Closed)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BED_EXTENDER.BedExtenderSts = PENDING (Not_Active)
a. PENDING: DR-CAM-f the raw value and VAL label for Not_Active are not sourced
2. Send CAN: BED_EXTENDER.IncompleteBedExtenderSts = PENDING (False)
a. PENDING: DR-CAM-f the raw value and VAL label for False are not sourced
3. Send CAN: STATUS_BH_BCM.RHatchSts = 1 (Open)
4. Read the HU display within 5 s and check the message overlaid on the rear view camera image
```

## expected_result

```
1. The bed extender status is reported as Not_Active
2. The incomplete bed extender status is reported as False
3. STATUS_BH_BCM.RHatchSts = 1 (Open) is sent
4. The message "Camera Not in position" is overlaid on the rear view camera image for 5 s
```
