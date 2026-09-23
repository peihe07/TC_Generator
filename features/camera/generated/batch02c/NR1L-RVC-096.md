# NR1L-RVC-096 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781651`（來源列 `SYS-RA-CAM-086`）

## test_item 上半（verbatim，SYS2 逐字）

> The HU shall follow this signal with an on-change $SVC_SoftBtn_Rq$ = [Not Pressed] signal within a time period of <Tsend>.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-086`（Surround View 節）之 `$SVC_SoftBtn_Rq$ = [Not Pressed]` 側。**該訊號於四本 DBC 零命中**，其承載 message、raw 與 `<Tsend>` 皆標 `PENDING: DR-CAM-j`；按鍵動作與其可判後果仍可執行，故不整列 BLOCKED。本列承「放開後送 `[Not Pressed]`」，其按下側（`[Pressed]`）之來源 `SYS-RA-CAM-085` 承接列為 `SWE-CAM-016`（`NR1L-RVC-038`），兩者依 R-CAM10 各歸其列。本列來源屬 CFTS092 之 Cargo/CHMSL 或 Surround View 節，依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`。

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
2. Press and release the virtual Surround View Camera button on the HU display
3. Read the bus analyzer recording and check the SVC_SoftBtn_Rq signal after the release
```

## expected_result

```
1. The bus analyzer is recording the vehicle bus
2. The virtual Surround View Camera button registers the press and the release
3. PENDING: DR-CAM-j an on-change SVC_SoftBtn_Rq = Not Pressed is sent within Tsend of the release
```
