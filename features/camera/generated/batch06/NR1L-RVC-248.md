# NR1L-RVC-248 — SWE-CAM-024

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`PENDING: DR-CAM-a the VF617_V5 anchor is not sourced`（來源列 `SYS-RA-VF617_V5-182`）

## test_item 上半（verbatim，SYS2 逐字）

> The NormalCamera App shall provide softkeys for AUX camera views, handle transitions without resetting timers (Ttime1/Ttime2), display a 4:3 aspect ratio, and show a blue screen if the camera is disconnected.

## reasoning

**R-CAM19(d) 真缺件佔位**（CAM-26 §2）：`SWE-CAM-024` 之十二個來源（`SYS-RA-VF617_V5-182`／`-197`／`-198`／`-200`／`-206`／`-219`／`-220`／`-221`／`-262`／`-264`／`-267`／`-270`）全在 SYS2 VF617_V5，該本未到（**DR-CAM-a**，A-CA01／A-CA05），故無 VF 錨、無可逐字之來源 `Description`。依 R-CAM19(d) 出一列 TC 取代原 D 欄空列（DECISIONS 6-52 作廢）：**六欄佔位** —— Pre-Conditions／Input Test Data／Test procedure／Expected Result／Specification Reference 五欄以 `PENDING: DR-CAM-a` 起首，Remarks 欄註 BLOCKED 之由。`test_item` 上半取 **037 之 Requirement Description 全文**（38 token；SYS-RA 原文不可得，此為本列唯一可逐字之文字），`source_object_id` 取十二來源之首（`-182`）。Test Set 依下放包 §2 與 `layer2_assign.tsv` 為 `AUX Camera`（R-CAM13(d) 保留之名）。車型依下放包 §2 指 **R-CAM18(a)** 之預設（五款已出資平台皆 `1`、598／5210 `0`）—— VF617 之平台維度未知，待 DR-CAM-a 到件後依 R-CAM3 重判。Procedure／ER 各兩行以滿 §10.5 之 ≥ 2 步；DR-CAM-a 到件後整列重寫。

## pre_conditions

```
1. PENDING: DR-CAM-a the preconditions are not sourced because SYS2 VF617_V5 is not received
```

## input_test_data

`PENDING: DR-CAM-a the input test data is not sourced`

## test_procedure

```
1. PENDING: DR-CAM-a the AUX camera trigger step is not sourced
2. PENDING: DR-CAM-a the observation step is not sourced
```

## expected_result

```
1. PENDING: DR-CAM-a the result of the trigger step is not sourced
2. PENDING: DR-CAM-a the expected AUX camera behavior is not sourced
```

## remarks

BLOCKED - DR-CAM-a: all 12 sources (SYS-RA-VF617_V5-182/-197/-198/-200/-206/-219/-220/-221/-262/-264/-267/-270) are in SYS2 VF617_V5, which is not received (R-CAM19(d))
