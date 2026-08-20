# W-15b′ — DBC ↔ LID 表逐屬性交叉

產物：`data/can_signal_map.tsv`（58 筆）。
目的：收 W-8 盲區 3 —— **橋接依賴 LID 表，其若錯則三來源一致地錯**。

## 通過條件（§5a 條 14）

> **與參照對象在所有可讀屬性上一致。**

可讀屬性列舉：`signal 名`／`message 名`／`CAN id`／`起始位元`／`長度`／
`factor`／`offset`／`VAL_ 值表`。DBC 側自 `BO_`／`SG_`／`VAL_` 三種語句解析
（BHCAN 155 message / 883 signal / 650 值表；FDCAN8 323 / 1755 / 1512）。

**不寫成「已知的幾項正確」** —— 下表之 `ALL_ATTR_MATCH` 即八項全數一致者。

## 結果

| 判定 | 數 | 意義 |
|---|---|---|
| `ALL_ATTR_MATCH` | **14** | 八項可讀屬性全數一致 |
| `VAL_DIFF` | **19** | 名稱與位置一致，**VAL_ 值表與 LID `Format` 欄有差異** |
| `NOT_IN_DBC` | **24** | LID 所載之 signal 名於兩份 DBC 皆不存在 |
| `MISMATCH` | **1** | **message 歸屬矛盾** |

## 1. 唯一之 message 矛盾（**升級條件命中**）

| token | LID 表所載 | DBC 實際 |
|---|---|---|
| **`$ESS_ENG_ST$`** | signal `ESS_ENG_ST` 位於 message **`ENGINE_FD_2`** | 該 signal 位於 **`STATUS_CCAN3`**；`ENGINE_FD_2` 於兩份 DBC 皆無此 signal |

**不自行調和。** 依 R-VS9(1) LID 表為 message 名之第一權威，
而依 R-VS9(3) 訊號斷言須指明 message —— **二者在此筆上給不出同一個答案**。
→ **A-VS26 新開，登記待判。**

## 2. 三筆大小寫差異 —— **推翻 00G §2 之一項陳述**

| token | LID 表 | DBC |
|---|---|---|
| `$HSW_Stat$` | `HSW_STATSts` | **`HSW_StatSts`** |
| `$HSW_Stat$` | `HSW_STATFailSts` | **`HSW_StatFailSts`** |

00G §2 逐字載：

> `$HSW_Stat$` 之匯流排名確為 `HSW_STATSts`（**LID 表與 DBC 一致**）

**該陳述為誤。** 二者**大小寫不同**：LID 作 `STAT`，DBC 作 `Stat`。

**其後果不是美觀問題**：依 R-VS9(1)，訊號逐字名以 LID 表為第一權威；
若照 LID 寫入 TC，即寫出一個**匯流排上不存在的 signal 名**
—— 與 R-VS9(5) 所防之 `$PowerMode$`／`PowerModeSts` 為同一形態，
只是這次錯的是第一權威本身。
→ **A-VS27 新開。**

> ⚠ 本輪首版比對為**區分大小寫**，故此三筆落入 `NOT_IN_DBC`；
> 補以不分大小寫重掃方分離出來。**若只跑不分大小寫，此差異會被吸收而看不見。**

## 3. 21 筆真正不存在於 DBC

分兩類：

| 類 | 例 | 判定 |
|---|---|---|
| **PROXI／配置參數**（非 CAN 訊號） | `Heated_Seats`／`Heated_Seat_Levels`／`Hybrid_Type`／`Driver_Side`／`Stop_And_Start`／`Vehicle_Line_Configuration`／`Rear_View_Camera_Soft_Button`／`Display_OFF_SoftKey_Prsnt` | **預期內** —— 其本就不在 DBC，值域來自 PROXI（DR-7）與 CFTS044 |
| **形似 CAN 訊號而 DBC 無者** | `FL_HS_Cmd_Tlm_Req`／`FR_HS_Cmd_Tlm_Req`／`FL_VS_Cmd_Tlm`／`HSW_Cmd_Tlm`／`HeatLeftSeatTgl`／`HeatRightSeatTgl`／`CmdIgn_FailSts`／`HDRstRelRq_3rdRow` | **待判** —— 此八者為**按鍵請求／命令類**訊號，procedure 之操作步驟需要它們；LID 表載其名而基線 DBC 無 → **A-VS28** |

## 4. 對 W-8 盲區 3 之回答

盲區原文：「橋接依賴 LID 表，**其若錯則三來源一致地錯**」。

**答案：LID 表確實有錯，且錯在三種不同的層面** ——
message 歸屬（1）、signal 名大小寫（3）、載有基線 DBC 所無之訊號（8）。
**故 W-19 之 DBC 欄（經 LID 橋接而得）其可靠度已量化：
58 筆中八項全符者 14。**

盲區**已收**，但收的結果是「橋接不可全信」，非「橋接可信」。

## 5. 本節之自我更正（先報自己的錯）

首版比對將 LID 儲存格內之**第一個** message 名，與該 signal 在 DBC 之
**每一個**出現處作交叉配對，於是 CAN-B 之 message 名對上 FD 之 DBC
出現處即報矛盾 —— 得 **MISMATCH 13**。

實際上 LID 儲存格同時載二個網段之變體
（如 `STATUS_CSWM.FL_HS_STATSts` ＋ `BCM_FD_22.FL_HS_STATSts`）。
改為**逐 (message, signal) 對配**後：**13 → 1**。

**12 / 13 為我方之配對缺陷** —— 與 W-8 之 33 → 1 同型。
