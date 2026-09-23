# NR1L-RVC-103 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1679`（來源列 `SYS-RA-VF551_V2-514`）

## test_item 上半（verbatim，SYS2 逐字）

> If BCM_FD_10.CmdIgnSts = RUN AND the soft key button control for the rear view camera is activated, then the Head Unit display shall transition to the rear view camera image video within the duration Transition_time.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-514` 之「`CmdIgnSts = RUN` 且軟鍵被啟用時，畫面於 `Transition_time` 內切至相機影像」。**`CmdIgnSts = RUN` 之前提由 `The HU is in the Full-Operation state` 承載**（其定義已含 IGN RUN，profile §4.1），不另送點火。`Transition_time` 之值取同本之 `-513`（< 1000 ms），ER 因而可判。與 `-102` 之分工：`-102` 驗自動模式（排檔）之切換時間，本列驗手動模式（軟鍵）之切換時間。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Measure the time between step 2 and the moment the rear view camera image video is fully displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera soft key control is activated
3. The measured time is less than 1000 ms
```
