# NR1L-RVCHMI-087 — SWE1-RVC-135

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.4.1`（來源列 `NRL-188169`）

## test_item 上半（verbatim，SYS1 逐字）

> CHMSL cam only configuration does not exist

## reasoning

§34.4.1 為**配置存在性**之否定命題：不存在「只有 CHMSL 而無後視」之配置。其可觀察形制取該否定之直接後果 —— 以 PROXI 佈成該配置（RVC Absent ＋ CHMSL Present）後，系統不提供任何相機入口。**§34.6.1（`SWE1-RVC-139`）與本列逐字全等**（連同 §34.3.1 共三列全等，見上繳 §3 證據 2）→ `-139` 委派本列，零 TC。取 §34.4.1 而非 §34.6.1 為承接列之由：**章節號較小**（沿 R-CAM10(b) 之「最小者承接」）。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 0 (Absent)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the App Drawer and check that no camera entry is offered
```

## expected_result

```
1. The App Drawer is displayed
2. No camera entry is offered, which shows that a CHMSL camera only configuration is not supported
```
