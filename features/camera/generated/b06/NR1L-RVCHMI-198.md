# NR1L-RVCHMI-198 — SWE1-RVC-065

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.6.1`（來源列 `NRL-188049`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear View Camera, CHMSL/Cargo Camera, Trailer Reverse Guidance, FFCTL, and Vehicle Surround View when equipped

## reasoning

**補生成之由**：拆解審計 **CAM-22 §5 #1**（`confidence = H`）—— §27.2.6.1 逐字列舉五款配備，而母列 `NR1L-RVCHMI-056` 以單一 ER 概括五款；依 **CAM-10 審閱 §一-4**「查表對映每項一列」應每款一列。母列改留 `Rear View Camera` 一款之驗證（其 ER 不動，見上繳 §2-2），本列承接其中一款。**既有 197 列不改**（DECISIONS 6-74），本列為新列。本列取 **CHMSL/Cargo Camera** 一款，其配備旗標為 `Digital_CHMSL_Camera_Prsnt`。`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）與 `Auxiliary_Trailer_Camera`（byte 211 bit 2）於 `forms/proxi/` 六本中**只有 Atl-Hi 三本有** → **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`（CAM-14 證據 5 已定）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read the Camera app home page and check that the CHMSL/Cargo Camera is offered
4. Select the CHMSL/Cargo Camera soft control
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The CHMSL/Cargo Camera is offered on the Camera app home page
4. The CHMSL/Cargo Camera view is displayed
```
