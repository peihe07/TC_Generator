# NR1L-RVC-113 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V4_PHDCC27_VF_523`（來源列 `SYS-RA-VF551_V4-119`）

## test_item 上半（verbatim，SYS2 逐字）

> · The warning text shall be available in each language used by the Head Unit and correspond to the Language signal, IPC_VEHICLE_SETUP.LanguageSelection.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-119` 之「警示文字須提供 HU 所用之各語言，並對應 `IPC_VEHICLE_SETUP.LanguageSelection`」。**觸發不走 CAN** —— `IPC_VEHICLE_SETUP.LanguageSelection` 依 **A-CA17** 不可注入（CameraEventHal 表：Atl-H、`Supported by Harman = N`、`MD fake CEH status = Not yet`），該項明令「以 **HMI 語言設定**為觸發（§5.8(e)），不走 CAN」。hop 取 `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁 **row 146** `Language`（`D` 欄 `>` 為次選單），其選項於 **row 147** 載為 `List items: 1) Language 1, 2) Language 2, 3) Language 3, …` —— 為**佔位式**而非實際語言名，故 procedure 只寫「選一個與現用不同之語言」而不指名（§8.4.1）。**CAM-12 之 `Send CAN: … LanguageSelection` 寫法作廢**，`PENDING: DR-CAM-o` 隨之撤除。各語言之逐字譯文亦無來源，ER 因而只驗「與語言設定一致」而不比對字串（§8.4.1）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

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
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Language"
4. Select a language other than the one in use
5. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
6. Read the warning text overlaid on the upper center of the display and check its language
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Language" screen is displayed with the selectable languages
4. The newly selected language is in use on the HU
5. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the warning text is overlaid
6. The warning text is shown in the newly selected language
```
