# 批 1 附件：PM 訊號對照表（DBC 實查，2026-08-21）

來源：`PDT27_E2A_R4_BHCAN.dbc`（155 msg／914 sig）、
`PDT27_E2A_R5_FDCAN8.dbc`（323 msg／2037 sig），Pei 提供，唯讀解析。
量測：PM 工作簿 283 列之 pre/input/proc/er 四欄，
`$X$` 22 種／228 次、`X.y` 20 種／430 次。

## 一、CAN 訊號層（R-1 三件組適用）—— 7 種

**網段判定原則**：以工作簿現有 message 名決定網段（現有 message 全屬
BH-CAN 側），不得改網段，僅補完三件組。

| 現行寫法 | 出現 | 三件組正確寫法 |
|---|---|---|
| `STATUS_BH_BCM2.RemStActvSts` | 10 | `RemStActvSts in STATUS_BH_BCM2 on BH-CAN` |
| `STATUS_LIN.Batt_ST_Crit` | 6 | `Batt_ST_Crit in STATUS_LIN on BH-CAN` |
| `STATUS_BH_BCM1.DriverDoorSts` | 4 | `DriverDoorSts in STATUS_BH_BCM1 on BH-CAN` |
| `STATUS_LIN.PN14_LS_Actv` | 4 | `PN14_LS_Actv in STATUS_LIN on BH-CAN` |
| `STATUS_LIN.PN14_LS_Lvl7` | 4 | `PN14_LS_Lvl7 in STATUS_LIN on BH-CAN` |
| `STATUS_BH_BCM1.PsngrDoorSts` | 1 | `PsngrDoorSts in STATUS_BH_BCM1 on BH-CAN` |
| `CLIMATIC_PANEL.Radio_Btn0` | 12 | `Radio_btn0 in CLIMATIC_PANEL on BH-CAN` ⚠ |

⚠ **A-PM01（新登記）**：`Radio_Btn0` 大小寫與 DBC 不符，
DBC 實為 `Radio_btn0`（小寫 b）。同 message 之 sibling 為
`Radio_btn1..4`、`Radio_Knob1_DIR/VAL`、`Radio_Knob2_DIR/VAL`。
12 列一併更正。

**補網段之實據（此即三件組存在之理由）**：上表 6 個 signal 於
**兩網段皆存在但 message 不同**，僅寫 signal 名無法定位：

| signal | BH-CAN | FD-CAN8 |
|---|---|---|
| RemStActvSts | STATUS_BH_BCM2 | BCM_FD_2 |
| Batt_ST_Crit | STATUS_LIN | BCM_FD_11 |
| DriverDoorSts | STATUS_BH_BCM1 | BCM_FD_9 |
| PN14_LS_Actv | STATUS_LIN | BCM_FD_11 |
| PN14_LS_Lvl7 | STATUS_LIN | BCM_FD_11 |
| PsngrDoorSts | STATUS_BH_BCM1 | BCM_FD_9 |

## 二、內部訊號層（`X.Info`／`X.Req`）—— 13 種，維持原記法

DBC 查無，確認為 HMI 內部訊號，**非缺件，不開 DR**：

`TLM_Status.Info`(177)、`Phone_Call.Info`(41)、
`Antitheft_Activation.Req`(39)、`Auto_SwitchOn_Setting.Req`(34)、
`Antitheft_Result.Info`(25)、`LTM_OperationalModeSts.Info`(20)、
`SwitchOff_Timeout_Setting.Req`(16)、`Front_Panel_OnOff.Req`(13)、
`Rear_Camera_Enable.Info`(11)、`SwitchOffSetting.Req`(5)、
`PhoneCall.Info`(5)、`TLM_Display.GUI`(2)、
`Audio_Data_Exchange.Info`(1)

⚠ **A-PM02（新登記）**：`Phone_Call.Info`(41) 與 `PhoneCall.Info`(5)
為同一訊號之兩種拼法。統一為 **`Phone_Call.Info`**（多數式，
且與 `Auto_SwitchOn_Setting` 底線風格一致）；5 列更正。

## 三、PROXI 層（`$X$`）—— 22 種，維持原記法

`$Telematic_Power$`(139)、`$VC_VEH_BRAND$`(19)、`$VC_VEH_LINE$`(11)
等 22 種。

⚠ **A-PM03（新登記）**：`$Radio_Theme$`(10) 於 DBC 亦存在同名
CAN signal（`RADIO_B4` on BH-CAN）。**維持 `$...$` 不改**——
PM 語境為 PROXI 參數；但改寫時不得誤判為 CAN 訊號而套三件組。

## 四、缺件（依 §8.4.3 走 PENDING，不阻塞本批）

CFTS009 引用之 VF570／VF601／VF665 三份未尋獲
（VF210 已確認 = `VP_Anti-Theft_Management.docx`，
內文自我識別 `[VF210_V6_R1]`）。
本批不涉此三份內容，如遇則標 `PENDING: DR-{n}`。
