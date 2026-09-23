# NR1L-RVC-121 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1672`（來源列 `SYS-RA-VF551_V2-478`）

## test_item 上半（verbatim，SYS2 逐字）

> · When there is no user change to Dynamic Gridlines, the HU shall send the default value gridZoomRequest.DynamicGridRQSts = [Default] to the RVCM.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-478` 之「使用者未變更 Dynamic Gridlines 時，HU 送預設值 `[Default]`」。**與 `-119` 之分工**：`-119` 之 Default 係**來源訊號缺席**所致，本列之 Default 係**使用者未操作**所致 —— 兩者之前提不同（本列之 `IPC_VEHICLE_SETUP` 正常傳送），失效態亦不同（§8.2.1）。「未變更」以原廠預設之前提表達。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU has been restored to its factory default settings
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Read gridZoomRequest.DynamicGridRQSts without changing the Dynamic Gridlines setting
2. Read the recording and check the value of gridZoomRequest.DynamicGridRQSts
```

## expected_result

```
1. The LVDS link is recorded
2. gridZoomRequest.DynamicGridRQSts = Default is sent to the RVCM
```
