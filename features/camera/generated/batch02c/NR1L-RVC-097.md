# NR1L-RVC-097 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781652`（來源列 `SYS-RA-CAM-087`）

## test_item 上半（verbatim，SYS2 逐字）

> The HU shall continue to send the on-change $SVC_SoftBtn_Rq$ = [Not Pressed] signal until next keypress.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-087`（Surround View 節）之 `$SVC_SoftBtn_Rq$ = [Not Pressed]` 側。**該訊號於四本 DBC 零命中**，其承載 message、raw 與 `<Tsend>` 皆標 `PENDING: DR-CAM-j`；按鍵動作與其可判後果仍可執行，故不整列 BLOCKED。本列承「持續送至下一次按鍵」。**ER 避開不可判之 `until`** —— 以「保持 10 秒不按鍵後讀取」之定點觀察表達持續性（同 `NR1L-RVC-094`）；`10 s` 為觀察窗而非標定值，不入 test_item。本列來源屬 CFTS092 之 Cargo/CHMSL 或 Surround View 節，依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Connect a bus analyzer to the vehicle bus and start recording
2. Hold for 10 s without pressing any button on the HU
3. Read the bus analyzer recording and check the SVC_SoftBtn_Rq signal
```

## expected_result

```
1. The bus analyzer is recording the vehicle bus
2. No button is pressed for 10 s
3. PENDING: DR-CAM-j SVC_SoftBtn_Rq = Not Pressed is still sent after 10 s
```
