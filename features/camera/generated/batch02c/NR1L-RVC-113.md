# NR1L-RVC-113 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V4_PHDCC27_VF_523`（來源列 `SYS-RA-VF551_V4-119`）

## test_item 上半（verbatim，SYS2 逐字）

> · The warning text shall be available in each language used by the Head Unit and correspond to the Language signal, IPC_VEHICLE_SETUP.LanguageSelection.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-119` 之「警示文字須提供 HU 所用之各語言，並對應 `IPC_VEHICLE_SETUP.LanguageSelection`」。**訊號存在**（`IPC_VEHICLE_SETUP` 於三本 BH-CAN 皆有，`LanguageSelection` 16 命中），惟**各語言之 raw 對照與 HU 所支援之語言清單於本 feature 之素材查無** ——供試語言之 raw 標 `PENDING: DR-CAM-o`（新開）。各語言之逐字譯文亦無來源，ER 因而只驗「與語言設定一致」而不比對字串（§8.4.1）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: IPC_VEHICLE_SETUP.LanguageSelection = PENDING (a second language)
a. PENDING: DR-CAM-o the raw value and VAL label for a second language are not sourced
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Read the warning text overlaid on the upper center of the display and check its language
```

## expected_result

```
1. The language selection is changed to the second language
2. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the warning text is overlaid
3. The warning text is shown in the second language that was selected in step 1
```
