# NR1L-RVCHMI-069 — SWE1-RVC-079

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.5`（來源列 `NRL-188071`）

## test_item 上半（verbatim，SYS1 逐字）

> If the Enable Wireless Cameras setting is enabled (setting ON) and the user plugs in a projection device (CarPlay/Android Auto) that must launch CP/AA screen focus for a wired connection then a popup will be displayed.

## reasoning

§27.4.5 之 56 token 條文逐字載彈窗文字 `"Wireless Cameras disabled.“` 並轉指 popup list。實測 `PU1517`（module `Camera`，Timeout 欄 `3`）之文字欄逐字 `Wireless Cameras disabled.` ＋ 按鈕 `<OK>`，觸發欄逐字 `Displayed if the Enable Wireless Cameras setting is enabled and the user plugs in a projection device (CP/AA) that must launch CP/AA screen focus for wired connection` —— 與本條完全對應。`CarPlay/Android Auto` 兩者之差異僅為彈窗註之字串替換（`*Note: For Android Auto, replace "Apple CarPlay" text with "Android Auto"`），可觀察結果相同，**不拆軸**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No projection device is plugged in
```

## input_test_data

`NA`

## test_procedure

```
1. Plug in a CarPlay projection device via the USB port
2. Read the pop-up text on the HU display
3. Read the Aux Cameras list and check that "Enable Wireless Cameras" is Off
```

## expected_result

```
1. The CarPlay screen takes focus
2. The pop-up reads "Wireless Cameras disabled." with <OK> (PU1517)
3. The "Enable Wireless Cameras" setting is Off
```
