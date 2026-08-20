# 00G 下放包補篇 — `Logical Identifiers and CAN Mapping v1.76` 之比對

分析層寫入，2026-08-20，同一往返（NN = 00）。
素材：Pei 於聊天提供之 `Logical_Identifiers_and_CAN_Mapping_v1_76.xlsx`
（沙箱副本 622,949 bytes，SHA256 `ffceac36…8ef4`）。
**尚未入 `inputs/`** —— 落檔與取雜湊屬 Tier 3，見 §6。

**本篇之前置警告**：canon §5a 第 9 條之首例即為此檔類
（R-P8′：`Logical Identifiers and CAN Mapping` 之列舉截斷於 `101 = WL`
被誤當作完整值域）。**本篇於 §3 實測該缺陷仍在，且正好落在本 feature
用得到的那一欄。**

---

## 1. 覆蓋率：30 個 token 命中 29

掃描條件：取 `CAN Mapping`（2,629 列）與 `Proxi & Configuration`（449 列）
兩表，表頭列 3、資料自列 4，A 欄 `Logical Identifier` 非空者為 LID，
**共 2,974 個相異 LID**。與 037 之 30 個 `$var$` token 作**不分大小寫**比對。

| 結果 | 數 |
|---|---|
| LID 逐字命中 | **27** |
| 近似命中（`HSW_StatFailSts`→`HSW_Stat`、`Heated_Seats_Levels`→`Heated_Seats`） | 2 |
| **完全無對應** | **1** —— `Heated_Steats_Levels` |

`Heated_Steats_Levels` 之無對應**佐證 A-VS05**：它是上游拼寫錯誤
（`Steats`），而非另一個參數。三種拼寫中只有 `Heated_Seat_Levels` 與
`Heated_Seats` 在 LID 表內有正身。

---

## 2. 這份檔給出了什麼 —— 訊號名與值域，逐 LID 可查

欄位結構：`LID Information`（1–5）／`Powernet`（6–10）／`CUSW`（11–15）／
`Atlantis`（16–20）／`Compact`（21–25）／**`Atlantis High`（26–30）**／
`Comments`（31–35）。每組含 `Signal Name` / `CAN` / `Format` / `SNA` / `VFs`。

**本 feature 之 EE Architecture 為 Atlantis High**，故第 26–30 欄為主。

節錄（執行層據此建 `data/lid_map.tsv`）：

| LID | Atlantis High 訊號 | CAN | 值域 |
|---|---|---|---|
| `HeatedSeatFL` | `STATUS_CSWM.FL_HS_STATSts` + `.FL_HS_STATFailSts` | CAN-B | 2 bit：`0 Heated_seat_off` `1 low` `2 medium` `3 high`；1 bit Fail：`0 Fail_Not_Present` `1 Fail_Present` |
| `VentedSeatFR` | `STATUS_CSWM.FR_VS_STATSts` + `.FR_VS_STATFailSts` | CAN-B | 2 bit：`0 Vented_seat_off` `1 low` `2 medium` `3 high` |
| `HSW_Stat` | `STATUS_CSWM.HSW_STATSts` + `.HSW_STATFailSts` | CAN-B | 1 bit：`0 OFF` `1 ON` |
| `HSW_Stat_2` | `STATUS_CLIMATE8.Tri_Level_HSW_StatSts` | CAN-B | `0 off` `1 low` `2 medium` `3 high` `7 SNA` |
| `PowerMode` | `STATUS_BH_BCM2.CmdIgnSts`／`BCM_FD_10.CmdIgnSts` | CAN-B／FD | 3 bit：`0 Initialization` `1 IGN_LK` `3 ACC` `4 RUN` `5 START` `7 SNA` |
| `FL_HS_RQ` | `TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm` | BH-CAN | `0 Not_Pressed` `1 Pressed` |
| `TGW_DISP_STAT` | `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`／`TELEMATIC_FD_4.TGW_DISP_…` | CAN-B／CAN-FD | `0 Display_off` … `9 Splashscreen_Display` `A Rear Entertainment HM…` |
| `DriverSide` | （Atlantis 欄）`Car_Configuration_1.Driver_Side` | — | `0 Left Side` `1 Right Side` |
| `Hybrid_Type` | （Atlantis 欄）`Hybrid_Type` | — | `0 N/A` `1 BEV` `2 HEV` `3 PHEV` `4 48V BSG` `5 12V BSG` `6 REPB` `7 FCEV` |
| `Stop_And_Start_cfg` | （Atlantis 欄）`Car_Configuration_1.Stop_And_Start` | — | `0 Absent` `1 Present` |
| `Heated_Steering_Levels` | （Atlantis 欄）`Heated_Steering_Wheel_Levels` | — | `0 = 1 Level` `1 = 2 Levels` `2 = 3 Levels` |
| `RVC_SK_PRSNT` | （Atlantis 欄）`Rear_View_Camera_Soft_Button` | — | `0 Absent` `1 Present` |

**三項交叉一致**：`STATUS_CSWM` / id 1169 / `Fail_Not_Present`–`Fail_Present`
在 **CFTS044、`PDT27_E2A_R4_BHCAN.dbc`、本 LID 表**三個來源上一致
（00C §4 已驗前兩者）。

**這解掉 R-VS9 的事實面**：`$HSW_Stat$` 之匯流排名確為 `HSW_STATSts`
（LID 表與 DBC 一致），`$PowerMode$` 為 `CmdIgnSts`（**不是** DBC 內
另一支 `PowerModeSts`）—— **R-VS9 之建議條文須據此修訂**：
訊號逐字名應以 **LID 表之 Atlantis High 欄**為第一權威、DBC 為佐證，
而非「DBC 逐字名」。原建議會在 `PowerMode` 這一項上寫錯訊號。

---

## 3. 這份檔**沒有**給出什麼 —— 兩個具名缺口

### 3.1 `See Proxi Table` —— 值域被轉指出去，共 6 個 LID

`Format` 欄之值為字串 `See Proxi Table` 者：

| LID | 是否為本 feature 所用 |
|---|---|
| `Heated_Seats` | **是**（037 引用 5 次） |
| `Heated_Seat_Levels` | **是**（5 次） |
| `Heated_Steering_Wheel` | **是**（6 次） |
| `DSP_SK_PRSNT` | **是**（3 次） |
| `Cooled_Seats` | 否 |
| `EC_Mirror_HK_Prsnt` | 否 |

→ **四個本 feature 用得到的 LID，其值域不在本檔內**，指向一份未持有之
**PROXI 表**。CFTS044 對 `$Heated_Seats$` 給的是 `[Present]` /
`[Front and Rear Seats]`，對 `$Heated_Seat_Levels$` 給的是 `[1] [2] [3]`
—— **規格側有值，LID 表側轉指**，兩者是否等價未經確認。

### 3.2 `VC_VEH_LINE` 之列舉截斷 —— **R-P8′ 之缺陷仍在**

`VC_VEH_LINE` 之 Atlantis Format 欄全長 491 字元，逐字結尾為：

```
… 100 = K8 (64 Hex) 101 = WL (65 Hex) # = Not Used
```

**與 R-P8′ 所記之截斷點完全相同（`101 = WL`）。**

而 CFTS044 對 `$VC_VEH_LINE$` 使用之值為 `[DT]`、`[WS]`、`[HDCC]`、
`[M240]`、`DS or DJ or D2 or DD or DP or DF or DX`、
`VEH_LA OR VEH_LD OR VEH_LX` —— **這些代號一個都不在該列舉裡**
（該列舉列的是 `343` / `327FL` / `K8` / `WL` 之類的數字車型碼）。

以詞界比對全簿：`DT` 命中 `CAN Mapping` 21 處、`M240` 34 處、`WS` 4 處、
`HDCC` 1 處 —— **散在各處之註記與分頁名，不是 `VC_VEH_LINE` 之值域定義。**

→ **`$VC_VEH_LINE$`（8 個引用）之值域仍未解。** 這正是 canon §5a 第 9 條
之形態：**手上唯一的那份 ≠ 該類文件的全部。**

---

## 4. 一個必須裁的結構問題：`Atlantis` 欄能不能當 `Atlantis High` 用

以本 feature 之 27 個逐字命中 LID 統計（`Signal Name` 或 `Format` 任一非空即計為有值）：

| 情形 | 數 |
|---|---|
| `Atlantis High` 欄有值 | **17** |
| **`Atlantis High` 欄空，而 `Atlantis` 欄有值** | **10** |
| 兩欄皆空 | 0 |

那 10 個為：`DriverSide`、`VC_VEH_LINE`、`Hybrid_Type`、`RVC_SK_PRSNT`、
`DSP_SK_PRSNT`、`Stop_And_Start_cfg`、`Heated_Seat_Levels`、
`Heated_Seats`、`Heated_Steering_Levels`、`Heated_Steering_Wheel`
—— **全部是 PROXI／配置類，一個 CAN 訊號都沒有。**

本檔第 5 欄之表頭註明「For this column Atlantis = Atlantis High unless
otherwise noted」，**但該註記寫在第 5 欄（Transfer Function）上，
不是全表通則**。空欄有兩種讀法：

- (a) 「與 Atlantis 相同，故不重複填」→ 10 項可用 Atlantis 欄
- (b) 「Atlantis High 不適用此項」→ 10 項在本 feature 無值域

**兩種讀法在本表上長得一模一樣。** 未裁定前，以 Atlantis 欄之值填入
TC，等同賭 (a)。

```
待裁 R-VS11（Atlantis 欄之可代用性）
`Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis High` 欄，於本
feature 所用之 27 個 LID 中有 10 個為空而 `Atlantis` 欄有值，且該 10 個
全為 PROXI／配置類參數。空欄之語意（「同 Atlantis」抑或「不適用」）
在本表內無法區分。

裁定選項：
(a) 視為「同 Atlantis」——可用，於 profile 載明此讀法為假設，並列入 RD-1
(b) 視為「未定義」——該 10 項之值域改採 CFTS044 內嵌值，LID 表僅作佐證
(c) 逐項向上游確認後再用

分析層建議 (b)：CFTS044 對其中多數已內嵌給值（如 $Hybrid_Type$ =
[PHEV]、$Stop_And_Start_cfg$ = [Present]/[Absent]），以規格為準不需
仰賴本表之空欄推定；LID 表之角色定為「訊號名之權威、值域之佐證」。
```

---

## 5. 對 DR 表與待裁項之淨變動

| 項 | 變動 |
|---|---|
| **DR-7（新）** | **PROXI 表** —— `Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel`／`DSP_SK_PRSNT` 四個 LID 之值域被本表轉指出去。Urgency **Medium**（CFTS044 有內嵌值可用，此為佐證） |
| **DR-8（新）** | **`$VC_VEH_LINE$` 之完整車型碼對照** —— 本表列舉截斷於 `101 = WL`，CFTS044 所用之 `DT`／`WS`／`HDCC`／`M240` 全不在內。Urgency **Medium**（8 個引用） |
| **R-VS9** | **建議修訂** —— 第一權威改為 LID 表之 Atlantis High 欄，非 DBC。理由：`$PowerMode$` 之匯流排名為 `CmdIgnSts`，照原建議會寫成 `PowerModeSts`（DBC 內另一支訊號） |
| **R-VS11（新）** | `Atlantis` 欄能否代 `Atlantis High`（§4） |
| **A-VS05** | **獲得佐證** —— `Heated_Steats_Levels` 在 2,974 個 LID 中無對應，確為拼寫錯誤 |

---

## 6. 素材落檔（Tier 3，請 Pei 決定）

本檔目前**只存在於聊天附件之沙箱副本**。依 G-L，「沒有路徑的到齊不算到齊」。

建議：`Logical Identifiers and CAN Mapping v1.76.xlsx` 入
`features/vehicle_setting/inputs/`，由執行層取 `shasum -a 256` 寫入
`INPUTS.sha256`；本篇之 SHA `ffceac36…8ef4` 僅證明副本自洽，**不作為權威值**。

**入庫後 W-8 應擴充為三欄來源**：CFTS044 內嵌值 ／ DBC VAL_ ／ LID 表，
**三者不一致者逐項列出**（不自行調和）。目前已知一致者三項（§2 末），
不一致者尚未系統性比對 —— **這是入庫後第一件該做的事。**

---

## 7. 本篇之盲區（R-G11）

1. **本表版本為 v1.76，來源不明**。AMFM 之教訓（`CIP_Radio_Tables`、
   `Market Configuration v1.6` 四個 release 四個雜湊）指出：**版本標籤
   不識別內容**。須確認 v1.76 是否對應 25PI3.5／SR26 基線
2. **`See Proxi Table` 之偵測以字面比對**，若他列以其他措辭轉指
   （如 `refer to PROXI`、`see config table`）本篇會漏。實測僅掃
   `Format` 兩欄（17／27），**未掃 `Usage Comment`（31 欄）**
3. **十個車型專屬分頁未進入比對**（`Atlantis Low Specific Signals`、
   `M240 Specific Signals`、`332BEV`…共 10 張、合計約 200 列）。
   若某 LID 之 Atlantis High 值定義在專屬分頁，§4 之「10 個空欄」會高估
4. 值域字串以 `Format` 欄原文照錄，**未解析為結構化鍵值**；
   `0 = Heated_seat_off` 這類寫法在不同列有 `0 =`／`0=`／`0 :` 之變體，
   建 `lid_map.tsv` 時須以已知全集驗抽取（canon §5a 第 12 條）
