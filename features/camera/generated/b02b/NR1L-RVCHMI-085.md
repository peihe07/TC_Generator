# NR1L-RVCHMI-085 — SWE1-RVC-133

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.1.5.1`（來源列 `NRL-188163`）

## test_item 上半（verbatim，SYS1 逐字）

> RearView Camera, Cargo Camera, and Apps Page

## reasoning

§34.1.5.1 為 `Accessible from`（§34.1.5）節下之列舉，與 R1 High 之 §27.2.6.1（`NR1L-RVCHMI-056`，五款）相對 —— **R1 Low 只有三項**（`RearView Camera, Cargo Camera, and Apps Page`），無 TRG／FFCTL／SVC。`Apps Page` 即 App Drawer，故以其為入口驗前兩項之並存。`Digital_CHMSL_Camera_Prsnt`（Cargo/CHMSL）只存在於 Atl-Hi 三本 → **R-CAM18(b)** 三個 Atl-Mi 欄判 `0`。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the App Drawer and check that the RearView Camera and the Cargo Camera are both offered
3. Select the Cargo Camera soft control
4. Read the HU display and check that the Cargo Camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The RearView Camera and the Cargo Camera are both offered in the App Drawer
3. The Cargo Camera soft control registers the selection
4. The Cargo Camera view is displayed
```
