# NR1L-RVC-051 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_514`（來源列 `SYS-RA-VF551_V33-226`）

## test_item 上半（verbatim，SYS2 逐字）

> when the value of the STATUS_BH_BCM.RHatchSts =(equal)"Open", LTM overlaps the related message on the RVC images ("Camera Not in position" see LTM HMI specification document) for T_INITDISPLAY time.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-226` 之 2261 分支。`T_INITDISPLAY` 之標定值為 **5,0 sec**（V33 §1.14.1 `SYS-RA-VF551_V33-479` 名／`-480` 值／`-483` 單位；V42 同值 `-631`／`-632`／`-635`），與 V2／V3 之 `for five seconds` 同數，ER 因而以 5 秒書寫。訊息名依來源逐字為 `STATUS_BH_BCM`（V33 文面）—— `forms/proxi` 側無 2261 之 DBC，四本 DBC 中 `STATUS_BH_BCM1`（`BO_ 854`）為最近之同族訊息；**本列不代換**，依 §8.7.5(f) 保留來源名，2261 之 DBC 屬 DR-CAM-f 之範圍。與 `NR1L-RVC-052` 之分工：`-226` 為無 BedExtender 條件之基本式，`-228` 另加 `BedExtenderSts = Not_Active AND IncompleteBedExtenderSts = False` 兩前提，兩來源之條件集不同，依 §8.2.2 各出一 TC。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；§4.3.1 之逐字忠實優先於 `J` 之版面規則。交付語料實測有前例 —— `features/*/delivered/` 十本之 2223 筆 test_item 首行中，10 筆首字小寫（`power`／`vehicle_setting` 兩本，皆已交付）。見上繳包 §3-3。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. STATUS_BH_BCM.RHatchSts = 0 (Closed)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM.RHatchSts = 1 (Open)
2. Read the HU display within 5 s and check the message overlaid on the rear view camera image
```

## expected_result

```
1. STATUS_BH_BCM.RHatchSts = 1 (Open) is sent
2. The message "Camera Not in position" is overlaid on the rear view camera image for 5 s
```
