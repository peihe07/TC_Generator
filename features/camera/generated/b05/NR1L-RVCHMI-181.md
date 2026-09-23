# NR1L-RVCHMI-181 — SWE1-RVC-036

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_9.2`（來源列 `NRL-142646`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCF2) Display “Check Entire Surroundings” for 5 seconds for the following events, then display “Camera System Unavailable” / “Camera Out of Position”

## reasoning

§9.2 之**時序**：先 5 秒之 Check Entire Surroundings，再換為故障訊息。`“Camera System Unavailable” / “Camera Out of Position”` 之斜線為二擇一，本列取前者（其彈窗 `PU0169`／`PU0170` 已查得），後者由 `-184` 承接（該訊息查無，DR-CAM-h）。與 `-173`（§8.2）之分工：後者為**正常**轉入相機畫面之 5 秒訊息，本列為**故障**路徑之時序。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in R
4. A camera fault that prevents the feed has been injected
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and record the timestamp at which the camera image is requested
2. Read the HU display 4 seconds after the recorded timestamp and check the message text
3. Read the HU display 6 seconds after the recorded timestamp and check the message text
```

## expected_result

```
1. The camera display is requested and "Check Entire Surroundings" is shown
2. The message still reads "Check Entire Surroundings" 4 seconds after the request
3. The message reads "Camera System Unavailable" 6 seconds after the request
```
