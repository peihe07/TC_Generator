# NR1L-RVCHMI-212 — SWE1-RVC-086

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.7.3`（來源列 `NRL-188081`）

## test_item 上半（verbatim，SYS1 逐字）

> For details about wireless cameras connection please refer to ‘Wireless cameras connection’ pages

## reasoning

**R-CAM19(c) 追溯補齊**（CAM-26 §2）：§27.7.3 全文為交叉引用句（`refer to ‘Wireless cameras connection’ pages`，A-CA36），其標的為 §27.5／§27.6（`Wireless AUX Camera Connection …`，`NRL-188072`／`NRL-188075`）。依下放包 §2，以被引章節之行為在**本列之情境**下驗（引用句本身即前提）—— 本列之父 §27.7 為 `Accessing Aux Cameras – App Drawer/Controls Page`（`NRL-188078`），故入口取 **App Drawer**（Controls 頁之入口缺來源，DR-CAM-g，不取）；行為取 **§27.5.2**（無投影、設定 OFF 時選取無線相機即自動啟用、無彈窗），**被引列 TC `NR1L-RVCHMI-071`**。`-071` 自 `Aux Cameras` 清單選取，本列自 App Drawer 之 soft control 選取（§27.5.2 之 `from any location`；§27.7.1 載無線 AUX 可自 apps drawer 存取，`NR1L-RVCHMI-075`）。App Drawer 之入口句式沿 `NR1L-RVCHMI-057`。設定之自動啟用以「相機視角得以顯示」判之，不另入設定清單（該觀察已由 `-071` 承接）。無 PROXI 配備旗標，R-CAM18(a) 五款全 `1`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. No wireless projection session is active
7. A wireless AUX camera is within range and powered on
8. The shift lever is in P
9. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the wireless AUX camera soft control in the App Drawer
3. Read the HU display and check that no pop-up is displayed
4. Read the HU display and check that the wireless AUX camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The wireless AUX camera soft control registers the selection
3. No pop-up is displayed
4. The wireless AUX camera view is displayed, which shows that the "Enable Wireless Cameras" setting was enabled automatically
```
