# DR-PW23 附表 —— PM 內部訊號對照總表（55 包 B4 / R-P355(a)）

> ⚠ **已由 58 包 B4′ 取代**：`data/dr_pw23_internal_signals_58.md`（R-P369(a)）。
> 本檔之「DBC 對照 0 / 13」係以**規格原名直查 DBC**、跳過 R-DM17 三段鏈之段 1–2，
> 依 R-G13 為「**未查**」而非「查無」（A-PW355）。本檔保留不刪（R-P329 之慣例），
> **其結論不得引用**。

> 母體：現行 corpus `generated/batch_00{1..7}.json`（283 條）全六欄機器掃描。
> 判準：`<Name>.Info` / `<Name>.Req` / `RemStartFail`。
> DBC 實查：BH-CAN `PDT27_E2A_R4_BHCAN.dbc`（sha256 `9ef1ec98…`）
> 與 FD-CAN8 `PDT27_E2A_R5_FDCAN8.dbc`（`51c8fd60…`），**逐名 grep**。

## 1. 總表（13 個相異名，845 次出現）

| # | 內部訊號名 | 出現 | 涉及 TC | 素材出處 | DBC 對照 | 處置（R-P355） |
|---|---|---|---|---|---|---|
| 1 | `TLM_Status.Info` | 382 | 97 | CFTS009 / 010、SYS3、SYS2、037 | **無** | **(b) 之例外** —— 其與 `$Telematic_Power$` 成對出現，語義即 TLM 電源狀態，對應 `$STATUS_TELEMATIC.PowerSts_Telematic$`（`VAL_ 1470`）。作前置者依 **R-P354(f)** 改 `Apply ENTER_<STATE>`，**不落 PENDING** |
| 2 | `Phone_Call.Info` | 82 | 32 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING: DR-PW23** |
| 3 | `Auto_SwitchOn_Setting.Req` | 76 | 26 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING** |
| 4 | `Antitheft_Activation.Req` | 67 | 26 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING** |
| 5 | `RemStartFail` | 65 | 15 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING** —— DR-PW23 原案即此名 |
| 6 | `LTM_OperationalModeSts.Info` | 39 | 16 | CFTS009、SYS2、037 | **無** | **(c) PENDING**。⚠ 相近之 `STATUS_BH_BCM1.OperationalModeSts` 存在於 DBC（`VAL_ 854`），惟前綴 `LTM_` 指 ECU 側，二者是否同一由上游認定（§8.4.1），**本層不代認** |
| 7 | `Antitheft_Result.Info` | 36 | 25 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING** |
| 8 | `SwitchOff_Timeout_Setting.Req` | 35 | 19 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING**。與 DR-PW25 之 HMI 條目名問題相連 |
| 9 | `Rear_Camera_Enable.Info` | 21 | 9 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING** |
| 10 | `Front_Panel_OnOff.Req` | 20 | 11 | CFTS009、SYS2 | **無** | **(c) PENDING**。即 DR-PW24 之標的 |
| 11 | `PhoneCall.Info` | 11 | 6 | CFTS009、SYS3、SYS2、037 | **無** | **(c) PENDING**。⚠ 見 §2 拼法 |
| 12 | `SwitchOffSetting.Req` | 8 | 2 | CFTS009、SYS2、037 | **無** | **(c) PENDING**。⚠ 見 §2 拼法 |
| 13 | `Audio_Data_Exchange.Info` | 3 | 1 | CFTS009、SYS2、037 | **無** | **(c) PENDING** |

**DBC 對照 0 / 13。** 十三個名在兩份 DBC 內**一次都沒有出現**（逐名 `grep -c` 實測）。
故 R-P355(b)「已有 DBC 對照者改 `$MESSAGE.Signal$`」在本 feature 上**無適用對象**，
除第 1 項循 R-P354 之路徑外，其餘十二項全數落 (c)。

**十三個名全數在素材內有出處** —— 非自造，是規格自身以內部變數描述行為。

## 2. ⚠ 素材自身之拼法不一致（非執行層所生）

| 對 | 出現 | 二者皆見於 |
|---|---|---|
| `Phone_Call.Info`（82）／`PhoneCall.Info`（11） | 93 | CFTS009、SYS3、SYS2、037 |
| `SwitchOff_Timeout_Setting.Req`（35）／`SwitchOffSetting.Req`（8） | 43 | CFTS009、SYS2、037 |

R-7 令以單一拼法為準，惟**二者皆為素材原文**，本層不得擇一（擇一即代上游認定）。
請上游確認各對是否同一物；若是，指定正式名。並入 DR-PW23 之詢問項。

## 3. 施作後之 PENDING 量（56 包 §L 之未估項）

| 量 | 值 |
|---|---|
| C3 家族（內部訊號作前置） | **111 / 283** |
| 其中僅含 `TLM_Status.Info`，依 R-P354 可解者 | **45** |
| 其中含其他內部訊號，必落 PENDING 者 | **66** |
| **全 corpus 任一欄含非 `TLM_Status.Info` 內部訊號者** | **105 / 283（37.1%）** |

**56 包 §L 之「逾百條 PENDING」為真，精確值 105 條。**
惟其中 45 條 C3 由 R-P354 吸收而非落 PENDING —— 分析層之擔憂方向正確而量偏高。

⚠ **與 S6「含 PENDING 不得出貨」之衝突於此定量**：
現行 corpus 之 I 家族為 0；施作後將為 **105**（37%）。
55 包 §E／56 包 §E 已將寫回順延至 57 包，衝突不在本包爆發，
**但 57 包之寫回在 DR-PW23 未結前不可能成立** —— 見 56 包 §K-2，須先裁。
