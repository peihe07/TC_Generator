# NR1L-RVCHMI-193 — SWE1-RVC-040

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_11.1`（來源列 `NRL-142653`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM Visualization graphics are feature dependent and should adapt based on vehicle proxy configuration:

## reasoning

§11.1 之 `adapt based on vehicle proxy configuration` —— 以**三個 proxy 狀態**驗其適配（Rear → Front And Rear → 無 PAM）。第三態之結果（RVC-only layout）與 B01b `-025`（§7.3.1，`vehicle do no offer any PAM capability`）一致，兩列之來源章與承接列不同（**R-CAM10**）。該列之 `*` 註（`When SDW is not capable of detecting ...`）為圖之腳註，圖不可抽，依 **DECISIONS 6-69** 不造其內容。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. PROXI PAM_Configuration = 0 (Rear)
5. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the PAM visualization and record which zones are drawn
2. Set PROXI PAM_Configuration = 1 (Front And Rear)
3. Read the PAM visualization and record which zones are drawn
4. Set PROXI CVPAM_Presence = 0 (Absent)
5. Read the HU display and check that no PAM visualization is drawn
```

## expected_result

```
1. Only the rear zones are drawn
2. PROXI PAM_Configuration = 1 (Front And Rear) is applied
3. The front and the rear zones are both drawn
4. PROXI CVPAM_Presence = 0 (Absent) is applied
5. No PAM visualization is drawn and the RVC-only layout is displayed
```
