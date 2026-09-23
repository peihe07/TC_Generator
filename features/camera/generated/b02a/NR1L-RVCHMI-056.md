# NR1L-RVCHMI-056 — SWE1-RVC-065

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.6.1`（來源列 `NRL-188049`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear View Camera, CHMSL/Cargo Camera, Trailer Reverse Guidance, FFCTL, and Vehicle Surround View when equipped

## reasoning

§27.2.6.1 列舉五款配備。五個 PROXI 旗標之平台覆蓋實測（`forms/proxi/` 六本）：`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）與 `Auxiliary_Trailer_Camera`（byte 211 bit 2，TRG）**只有 Atl-Hi 三本有**，三本 Atl-Mi 各 0 → 依 **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`。本列取**全部配備皆present**之組合以驗該列舉之完整性；各款之個別行為由其所屬節之 TC 承接，本列不重複。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
4. PROXI Auxiliary_Trailer_Camera = 1 (Present)
5. PROXI Forward_Facing_Camera = 1 (Present)
6. PROXI Surround_View_Camera = 1 (Present)
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read the Camera app home page and check that all five equipped camera features are offered
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. Rear View Camera, CHMSL/Cargo Camera, Trailer Reverse Guidance, FFCTL and Vehicle Surround View are all offered on the Camera app home page
```
