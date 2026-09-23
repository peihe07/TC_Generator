# NR1L-RVCHMI-124 — SWE1-RVC-127-01

- **Test Group**：Rear View Camera｜**Test Set**：Wireless Camera Pairing
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_33.1.2`（來源列 `NRL-188147`）

## test_item 上半（verbatim，SYS1 逐字）

> If the ‘enable wireless cameras’ setting is not enabled, a wireless projection session is active and the user selects the ‘Add camera’ button, a popup is displayed to the user.

## reasoning

彈窗逐字取 **`PU1519`**（module `Camera`；觸發欄逐字 `Displayed when the user tries to add a new wireless camera if there is an active wireless projection (CP/AA) session`）——與本條之情境完全對應，且與 `PU1518`（**啟用設定**／**選取相機**之情境，B02a `-064`／`-072`）為**不同**之彈窗。按鈕欄 `<X>`／`<Yes>`／`<No>` 與 §33.1.2 之 `Pressing YES`／`Pressing NO` 相符。本列只驗彈窗之出現與文字；兩鍵之後果由 `-125`／`-126` 承接。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. The Aux Cameras list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the 'Add camera' button
2. Read the pop-up text on the HU display
```

## expected_result

```
1. The 'Add camera' button registers the selection
2. The pop-up reads "Do you want to disconnect Apple CarPlay and add a wireless camera? Apple CarPlay can be connected using the USB port when Wireless Cameras are enabled." with <Yes> and <No> (PU1519)
```
