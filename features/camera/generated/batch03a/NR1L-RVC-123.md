# NR1L-RVC-123 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1674`（來源列 `SYS-RA-VF551_V2-480`）

## test_item 上半（verbatim，SYS2 逐字）

> · When the customer selects to enable the Rear view Camera Dynamic Gridlines, the HU shall send gridZoomRequest.DynamicGridRQSts = [ON] for two LVDS message cycles and then send gridZoomRequest.DynamicGridRQSts = [Default].

## reasoning

驗證目標為 `SYS-RA-VF551_V2-480` 之「使用者啟用 Dynamic Gridlines 時，HU 送 `DynamicGridRQSts = [ON]` **達兩個 LVDS 訊息週期**後再送穩態值」。**值切換之結果照寫、時序面 PENDING**（CAM-09 審閱 §一-4，DECISIONS 6-30 難點 A）——「一個 LVDS message cycle」之時間值於 SYS2 全本與 `forms/` 皆查無，標 `DR-CAM-p`。使用者之操作以其上游 CAN 訊號表達（該設定之 HMI 操作由 `NR1L-RVC-062`／`-063` 承接，本列只驗 LVDS 側之送出形態，§8.2.1）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-p the duration of one LVDS message cycle is not sourced
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON)
2. Read the recording of gridZoomRequest.DynamicGridRQSts from the moment of step 1 and check the values that are sent
```

## expected_result

```
1. IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) is sent
2. gridZoomRequest.DynamicGridRQSts = ON is sent and PENDING: DR-CAM-p it is sent for two LVDS message cycles before the steady value follows
```
