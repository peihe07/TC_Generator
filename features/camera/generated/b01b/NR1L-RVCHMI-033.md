# NR1L-RVCHMI-033 — SWE1-RVC-021

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.1`（來源列 `NRL-142627`）

## test_item 上半（verbatim，SYS1 逐字）

> Gear = D and speed threshold is overcome or RVC timeout expired; ○ If the camera is activated above the speed threshold limit via the soft control (user input) it will remain on the screen for 10 seconds before disappearing

## reasoning

§7.5.1 含主句與一個 `○` 子項。主句之「D 檔 ＋ 速度逾門檻」即退出，而子項給出**例外**：以 soft control 於逾門檻時手動活化者，留 10 秒後才消失。兩者為同一條之正例與例外，合一列以決策表驗之（先驗例外成立、再驗 10 秒後退出）。`10 seconds` 為來源逐字；門檻值見 profile §9。與 `-030` 之分工：後者驗**軟鍵灰階**（未手動活化），本列驗**已手動活化後之 10 秒寬限**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Press the camera soft button on the HU and record the timestamp
3. Read the HU display and check that the RVC+PAM layout is displayed
4. Wait 10 seconds from the recorded timestamp without changing the gear or the speed
5. Read the HU display and check that the RVC+PAM layout is no longer displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent, which is above the threshold
2. The camera soft button registers the press and its timestamp is recorded
3. The RVC+PAM layout is displayed although the speed is above the threshold
4. The 10 second interval elapses
5. The RVC+PAM layout is no longer displayed and the last known HU display is shown again
```
