# NR1L-RVC-234 — SWE-CAM-023

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_523`（來源列 `SYS-RA-VF551_V3-253`）

## test_item 上半（verbatim，SYS2 逐字）

> · The warning text shall be available in all languages supported by the Head Unit and text display shall correspond to the Language signal, IPC_VEHICLE_SETUP.LanguageSelection.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-253` 之「警示文字須提供 HU 之各語言，並對應 `IPC_VEHICLE_SETUP.LanguageSelection`」。**觸發不走 CAN** —— 該訊號依 **A-CA17** 不可注入（CameraEventHal：Atl-H、`N`／`Not yet`），明令以 **HMI 語言設定**為觸發（§5.8(e)）。hop 取 `HMI Settings List` `Settings` 分頁 **row 146** `Language`；其選項於 **row 147** 為佔位式 `1) Language 1, 2) Language 2, …`，故只寫「選一個與現用不同之語言」而不指名（§8.4.1，DR-CAM-o）。Atl-Mi 本之措辭為 `all languages supported by` 而非 `each language used by`，逐字相異故分列；依 R-CAM15(b)，V42 於本驗證點無對應條文而 V4 有（`-119`），V3 列承其母體 376。

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
5. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
6. Read the warning text overlaid on the upper center of the display and check its language
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Language" screen is displayed with the selectable languages
4. The newly selected language is in use on the HU
5. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the warning text is overlaid
6. The warning text is shown in the newly selected language
```
