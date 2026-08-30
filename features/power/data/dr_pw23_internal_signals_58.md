# DR-PW23 附表（重做）—— PM 內部訊號三段鏈解析（58 包 B4′ / R-P368 / R-P369）

> ⚠ **已由 62 包三度重做取代**：`data/dr_pw23_internal_signals_62.md`（R-P375(f)）。
> 本檔之段 1 僅入 LID `CAN Mapping`（R-P368(a) 原文），R-P375(a) 已擴為 `forms/` 全部參考檔，
> 重查後另得四個候選。本檔保留不刪，**其「未解得 11 名」之數不得引用**。

> **取代 `data/dr_pw23_internal_signals_55.md`**（該檔保留不刪，已加標）。
> 55 包版以**規格原名直查 DBC**、跳過段 1–2，其「DBC 對照 0 / 13」依 R-G13
> 為「未查」而非「查無」（A-PW355）。本檔依 R-P368(a) 之三段鏈重做。

## 0. 解析鏈與所用之檔（R-P368(a)、G0 參考資料庫段）

| 段 | 檔 | SHA256 |
|---|---|---|
| 1 | `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，`CAN Mapping` 分頁，資料自 r4，共 2,624 列；`Atlantis High` 欄組 c26 `Signal Name` / c27 `CAN` | `a01e1679…` |
| 3 | `forms/PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3…` |
| 3 | `forms/PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf…` |
| 旁證 | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`（R-P368(e)，**不得逕用其名**）| `9ef1ec98…` |

段 1 之比對面：`Logical Identifier`(c1) / `Function`(c2) / `Object Text`(c3)，
正規化為小寫去符號後取包含關係。**每一命中載明列號與欄**（R-P368(b)）。

## 1. 十三名之解析結果

| # | 規格原名 | 段 1（LID 列 / 欄 / 值）| 段 2（`MESSAGE.Signal`）| 段 3 | 結果 |
|---|---|---|---|---|---|
| 1 | `TLM_Status.Info`（素材恆與 `$Telematic_Power$` 成對）| **r2069 c1 `Telematic_Power`**（逐字）| `STATUS_TELEMATIC.PowerSts_Telematic`（CAN-BH）／`TELEMATIC_FD_4.PowerSts_Telematic`（CAN_FD）| BHCAN2 ✓／FDCAN8 ✓ | **解得** |
| 2 | `LTM_OperationalModeSts.Info` | **r1286 c1 `OperationalModeSts`**（前綴差異，R-P368(b)）| `STATUS_BH_BCM1.OperationalModeSts`（BCAN）／`BCM_FD_2.OperationalModeSts`（FD）| BHCAN2 ✓／FDCAN8 ✓ | **解得（附註）** |
| 3 | `Phone_Call.Info` | LID 無列（`PhoneCall` / `Phone Call` / `CallActive` 皆 0 命中；最近者 r869 `HandsFreePhoneStatus` → `STATUS_TELEMATIC.HFPSts`，**語意跳接，(b) 不許**）| — | — | **未解得（止於段 1）** |
| 4 | `PhoneCall.Info` | 同上 | — | — | **未解得（止於段 1）** |
| 5 | `Auto_SwitchOn_Setting.Req` | LID 無列（`AutoSwitch` / `Auto_Switch` / `RecallLast` 皆 0）| — | — | **未解得（止於段 1）** |
| 6 | `Antitheft_Activation.Req` | r76 c1 `AntiTheftStatus` —— **Activation ≠ Status，屬語意跳接，(b) 不許** | — | — | **未解得（止於段 1）** |
| 7 | `Antitheft_Result.Info` | r76 c1 同上 —— **Result ≠ Status，同不許** | — | — | **未解得（止於段 1）** |
| 8 | `RemStartFail` | LID 無列（`RemStart` 0 命中；r1578 `RemoteStartActive` 為 `RemStActvSts`，非本名）| — | — | **未解得（止於段 1）** |
| 9 | `SwitchOff_Timeout_Setting.Req` | LID 無列（`SwitchOff` / `Timeout` 皆 0）| — | — | **未解得（止於段 1）** |
| 10 | `SwitchOffSetting.Req` | 同上 | — | — | **未解得（止於段 1）** |
| 11 | `Rear_Camera_Enable.Info` | LID 無列（`RearCam` / `CameraEnable` 皆 0；r215 `CameraDisplaySts` 為顯示狀態非致能）| — | — | **未解得（止於段 1）** |
| 12 | `Front_Panel_OnOff.Req` | r1039 c1 `ICSPowerButton` —— **即 DR-PW24 之待確認假說，語意跳接，(b) 不許** | （若確認則為 `CLIMATIC_PANEL.Radio_btn0`／`DIS_CENTERSTACK.DCSD_Power`，二者段 3 皆 ✓）| — | **未解得（止於段 1，待 DR-PW24）** |
| 13 | `Audio_Data_Exchange.Info` | LID 無列（`AudioData` / `DataExchange` 皆 0）| — | — | **未解得（止於段 1）** |

**解得 2 / 13；未解得（止於段 1）11 / 13；段 3 查無 0。**

### R-P370(d) 加註 —— 八名為 HU 內部變數，LID 不收錄

> **訂正（59 包，A-PW358）**：58 包回報 §5 記「十一名中九名在 LID 完全無列」為筆誤，
> 實測為**八名**。十三個完整規格原名在 LID c1/c2/c3 **零命中 13 / 13**；
> 十一名未解得者中**三名**有語意近似列而依 R-P368(b) 拒收（#6 / #7 → r76、#12 → r1039），
> **八名**連近似列亦無。R-P370(d) 之加註標的為下列八名。
> ⚠ **原記「九名」為筆誤**，59 包實測訂正為**八名**（A-PW358）：十三個完整規格原名在 LID 零命中 13 / 13；十一名未解得者中三名有語意近似列而依 R-P368(b) 拒收。結論（PENDING 102、S6 衝突之結構）不受影響。


| 名 | 加註（R-P370(d)）|
|---|---|
| `Phone_Call.Info` | **HU 內部變數，LID 不收錄**；解消途徑僅餘上游回覆或 Pei 裁 |
| `PhoneCall.Info` | 同上 |
| `Auto_SwitchOn_Setting.Req` | 同上 |
| `RemStartFail` | 同上；SYSAD 逐字載其為 `The internal variable to manage the success or failure of remote start` |
| `SwitchOff_Timeout_Setting.Req` | 同上 |
| `SwitchOffSetting.Req` | 同上 |
| `Rear_Camera_Enable.Info` | 同上 |
| `Audio_Data_Exchange.Info` | 同上 |

另三名（`Antitheft_Activation.Req` / `Antitheft_Result.Info` / `Front_Panel_OnOff.Req`）
**有語意近似之 LID 列**，其解消途徑除上游回覆外，尚有「上游確認該近似列即同一物」
（後者即 DR-PW24 之既有問法）—— 故**不加「LID 不收錄」之註**。

### 為何無一筆記「查無」

R-G13 之三要件中，第 2 項（用什麼名字查）在十一筆上不成立 ——
**段 1 未過即無 CAN 訊號名可查**，故段 3 從未執行。
依 R-P368(d)，此為「未解得（止於段 1）」，**不得登 `LOOKUP_MISSES.md`**
（該檔只收段 3 之查無）。本輪不新增 M-n。

### 第 2 項之附註（不得省）

`LTM_OperationalModeSts.Info` 之 `LTM_` 前綴指 ECU 側（LTM 模組自身之
operational mode），LID r1286 之 `OperationalModeSts` 解得者為
`STATUS_BH_BCM1.OperationalModeSts`（**BCM 側車輛點火狀態**）。
R-P368(b) 容許前綴差異，惟**二者是否同一物屬上游職權**（§8.4.1，
與 DR-PW21 同形態）。本表記為「解得（附註）」，TC 施作時
以 `$STATUS_BH_BCM1.OperationalModeSts$` 書寫並標 `(DR-PW26)`。

## 2. 附帶解得 —— `$PwrAccDelayAct$`（DR-PW26 第 4 問）

| 段 | 結果 |
|---|---|
| 1 | **LID r1458 c1 `PwrAccDelayAct`**（逐字），`Function` = `Power accessory delay time` |
| 2 | `BODY_CNTRL3.Comfort_Enable_Time`，`CAN` 欄 = `B-CAN` |
| 3 | **BHCAN2 ✗**／FDCAN8 有同名訊號惟訊息為 `BCM_FD_27`／**R4 有 `BODY_CNTRL3.Comfort_Enable_Time`** |

→ **B-1 型衝突**（A-PW357）。依 R-P368(e) **不得逕用 R4 名**，列 §K 交 Pei。
DR-PW26 第 (4) 問由「兩份 DBC 查無」訂正為
「LID 解得；B-CAN 側僅 R4 有，forms/BHCAN2 無；FD 側訊息名不同」。

同列另有 `AccDelayAct`（LID r29），其 `Atlantis High` `Signal Name` 欄為
**`N/A`**、`CAN` 欄為 `None` → **未解得（止於段 1）**，非查無。

## 3. 拼法不一致二對之處置（R-P369(b)）

| 對 | 二名皆入段 1 之結果 | 判定 |
|---|---|---|
| `Phone_Call.Info` / `PhoneCall.Info` | 二者皆 LID 無列 | **無法判同異**，維持 DR-PW23 詢問 |
| `SwitchOff_Timeout_Setting.Req` / `SwitchOffSetting.Req` | 二者皆 LID 無列 | **無法判同異**，維持 DR-PW23 詢問 |

R-P369(b) 之「解至同一 `MESSAGE.Signal` 則為同物」在本輪**無適用對象**。

## 4. PENDING 重算（R-P369(d)）

55 包 B4 之「105 條」作廢。重算結果 —— **105 → 102，只少 3 條。**

| 量 | 條數 | 佔 283 |
|---|---|---|
| 含任一內部訊號 | 131 | 46.3% |
| 含非 `TLM_Status.Info` 者（55 包所報之 PENDING 數）| 105 | 37.1% |
| 全部內部訊號皆經 R-P368 解得者（`TLM_Status.Info` ＋ `LTM_OperationalModeSts.Info`）| 29 | 10.2% |
| **施作後仍帶 `PENDING: DR-PW23` 者** | **102** | **36.0%** |

機讀：`data/pending_recount_58.tsv`。

### 仍 PENDING 之訊號別

| 訊號 | TC 條數 |
|---|---|
| `Phone_Call.Info` | 32 |
| `Auto_SwitchOn_Setting.Req` | 26 |
| `Antitheft_Activation.Req` | 26 |
| `Antitheft_Result.Info` | 25 |
| `SwitchOff_Timeout_Setting.Req` | 19 |
| `RemStartFail` | 15 |
| `Front_Panel_OnOff.Req` | 11 |
| `Rear_Camera_Enable.Info` | 9 |
| `PhoneCall.Info` | 6 |
| `SwitchOffSetting.Req` | 2 |
| `Audio_Data_Exchange.Info` | 1 |

### ⚠ 據實回報：三段鏈之方法正確，實益極小

R-P368 之判斷成立 —— 55 包之「0 / 13」確為未查，段 1 一做即推翻。
**但重做後解得 2 / 13，PENDING 由 105 降至 102（−3 條，−2.9%）。**

原因不在方法而在 LID 之涵蓋：十一名中有**八**名在 LID `CAN Mapping`
之三個比對欄**完全無列**（非「有列而解不出 CAN 名」）。
LID 收錄的是有 CAN 對應之 Logical Identifier；
PM 之這些名是 **HU 內部變數**（DR-PW23 原案對 `RemStartFail` 之判斷即如此：
SYSAD 載其為 `The internal variable to manage the success or failure of remote start`），
**本來就不會進 LID**。

**故 57 包 §K-1 之三選項（甲等 DR / 乙分兩段寫回 / 丙逐名審）
其量化前提由 105 改為 102 而結構不變** —— S6 衝突未因 forms/ 而解消。
