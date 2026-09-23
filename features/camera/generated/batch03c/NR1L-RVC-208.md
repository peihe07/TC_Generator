# NR1L-RVC-208 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2396`（來源列 `SYS-RA-VF551_V42-301`）

## test_item 上半（verbatim，SYS2 逐字）

> stop to copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data set the internal signal RVC_ImageDefeat.Req to "Pressed" set the internal variable RVC_ACTIVE equal to "FALSE"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-301` 之「停止複製、設 `RVC_ImageDefeat.Req = "Pressed"`、`RVC_ACTIVE = "FALSE"`」。**與 `-205` 之分工**：`-205` 之來源（`-263`）為**條件式**（點火 ∧ ImageDefeat ∧ 排檔），本列之來源為該分支之**動作清單**；兩者為同一行為之條件側與動作側，惟**同屬 `SWE-CAM-006`**（無 R-CAM10(b) 之跨列問題），依 §8.2.2 各出一 TC。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rearview image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read the HU display and check that no rearview image is displayed
```

## expected_result

```
1. The "X" exit button registers the press
2. No rearview image is displayed and the copy of the cable video has stopped
```
