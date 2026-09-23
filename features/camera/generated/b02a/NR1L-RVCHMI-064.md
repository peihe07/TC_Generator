# NR1L-RVCHMI-064 — SWE1-RVC-074

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.2`（來源列 `NRL-188066`）

## test_item 上半（verbatim，SYS1 逐字）

> If a wireless projection session is active while selecting the setting, a popup is displayed.

## reasoning

§27.4.2 只寫「顯示一個 popup」而未載其文字；逐字取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 之 **`PU1518`**（module `Camera`，觸發欄逐字 `Displayed when the user tries to enable wireless cameras if there is an active wireless projection session`）—— 其按鈕欄為 `<X>`／`<Yes>`／`<No>`，與 §27.4.2.1／§27.4.2.2 之 `presses yes`／`presses no` 相符。本列只驗**彈窗出現且文字相符**；兩個按鍵之後果由 `-065`／`-066` 承接。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Select "Enable Wireless Cameras"
6. Read the pop-up text on the HU display
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" list is displayed
5. A pop-up is displayed
6. The pop-up reads "Do you want to disconnect Apple CarPlay and enable Wireless Cameras? Apple CarPlay can be connected using the USB port when Wireless Cameras are enabled." with <Yes> and <No> (PU1518)
```
