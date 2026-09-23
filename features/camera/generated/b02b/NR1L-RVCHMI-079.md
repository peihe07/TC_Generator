# NR1L-RVCHMI-079 — SWE1-RVC-089

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.8.3`（來源列 `NRL-188085`）

## test_item 上半（verbatim，SYS1 逐字）

> Selecting the “More AUX” again closes the popup

## reasoning

§27.8.3 逐字。ER 加「後視影像仍顯示」一項 —— 關閉彈窗不應連帶退出相機視角，該判準取同節 §27.8.1 之情境（彈窗自後視影像開啟）。來源之按鍵名於 §27.8.1 寫 `“More Aux”`、§27.8.3 寫 `“More AUX”`，兩處大小寫不一；各列之 verbatim 逐字照錄，Procedure 依其所屬列之拼法。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. Two wired AUX cameras are connected
4. The rear view camera image is displayed
5. The "More Aux" pop-up is open
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "More AUX" button again
2. Read the HU display and check that the pop-up is closed and the rear view camera image is still displayed
```

## expected_result

```
1. The "More AUX" button registers the press
2. The pop-up is closed and the rear view camera image is still displayed
```

## remarks

SYS1 27.8.1 spells the button "More Aux" and 27.8.3 spells it "More AUX".
