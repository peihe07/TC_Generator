# 作業 A — 同一物之判定（R-17(c)，A-ICS88）｜2026-08-30

## §0 候選集之重建 —— 【E25 觸發】repo 內 dbc 為**四支**，非三支

下放包 §3 令「三支 dbc（BHCAN2＝A、R4_BHCAN＝B、FDCAN8＝C）」，
並於 E25 令「`forms/` 之檔案清單須先列，不得預設只有三支」。**實測為四支：**

| 代號 | 路徑 | sha256（前 16）| 綁定狀態 | `BU_` 含 `LTM` |
|---|---|---|---|---|
| **A** | `forms/PDT27_E2A_R1_BHCAN2.dbc` | — | **未綁**（Pei 裁定之台架匯流排）| **是** |
| **B** | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` | — | 已綁 | **否** |
| **C** | `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071` | 已綁 | 是 |
| **D** | **`forms/PDT27_E2A_R1_FDCAN8.dbc`** | `2a86c4bf3e670d71` | **未綁** | 是 |

**D 為下放包未列之第四支，且含相關訊號**（`DISP`／`Telematic`／`Power` 命中 30、
其中含 `DISP_STAT`／`Telematic` 者 11）→ **E25 觸發**。

**且 D 不是 C 的複本**：sha256 不同、`SG_` 總數不同（D 1916／C 2037）。
**二者之差在平台世代**：D 為 **R1**、C 為 **R5**。本 DUT 為 **R1L** ——
**已綁之 C 為 R5，而未綁之 D 為 R1。** 同理 A（R1）未綁、B（R4）已綁。
**即：本 feature 現行綁定之二支 dbc 皆非 R1 世代，而 `forms/` 下的二支 R1 皆未綁。**
此事下放包未提，**只列不裁**。

（D 與 C 就本作業之 11 個相關訊號而言，發收方與位元佈局**逐項相同**，
故納入候選集後不改變本作業之判定；具名於此以免被讀成「四支各有一套答案」。）

## §1 候選盤點（自四檔重建，非轉抄 upstream-13）

### A 檔（BHCAN2，Pei 裁定之台架匯流排）—— 含 `DISP_STAT`／`Telematic` 者 13

| `SG_` | 承載 `BO_` | 起始位元 | 長度 | 發方 | 收方 |
|---|---|---|---|---|---|
| **`TGW_DISP_STATSts`** | `1500 TELEMATIC_DISPLAY2` | 0 | 4 | **ETM** | `SGW` |
| **`PowerSts_Telematic`** | `1470 STATUS_TELEMATIC` | 12 | 3 | **ETM** | `FPDM,SGW` |
| `DCSD_DISP_STAT` | `1445 DIS_CENTERSTACK` | 7 | 3 | `SGW` | `ETM,LTM` |
| `FPDM_DISP_STAT` | `1513 FPDM1` | 2 | 3 | `FPDM` | `ETM` |
| `TGW_FPDM_DISP_STATSts` | `1282 RADIO_B2` | 50 | 3 | `ETM` | `FPDM` |
| `AUDIOSts_Telematic` | `1470 STATUS_TELEMATIC` | 14 | 2 | `ETM` | `SGW` |
| 其餘 7 個 `*_Telematic` | `2654208036 NWM_TELEMATIC` | — | — | `ETM` | `SGW` |

`BU_` 節點表逐字：`ETM FPDM LTM SGW` —— **A 檔無 `ICS` 節點**（重要，見 §4）。

B／C／D 檔之對應清單見 §3 矩陣。

## §2 R-17(c) 三項判定表

### 規格側之依據 —— 先報二項「查無」

- **CFTS020 全文未載任何 CAN 訊息名**：`TELEMATIC_DISPLAY2`／`STATUS_TELEMATIC`／
  `DIS_CENTERSTACK`／`RADIO_B2` 命中物件**各 0 —— 確定之查無**。
  故 **項① 無規格側依據可比**。
- **CFTS020 全文未載位元位置或長度**（就本二訊號）。故 **項② 無規格側依據可比**。
- CFTS020 載 **`BH-CAN`**（54 個物件，例：`4819370` 逐字
  `The ICS will send signals on the BH-CAN to communicate the status of the mechanical push buttons.`），
  但 **`BHCAN2`／`CAN2` 命中各 0 —— 查無**。Pei 裁定之「BHCAN2」在規格中無同名對應物；
  `BH-CAN` 與 `BHCAN2` 是否同一條匯流排，**規格內無可判之依據，不調和**。

### 判定表

| 訊號 | 候選 | ① 承載 `BO_` | ② 位元／長度 | ③ `VAL_` 列舉 | 判 |
|---|---|---|---|---|---|
| `$TGW_DISP_STAT$` | **`TGW_DISP_STATSts`**（`BO_ 1500`）| **不可比** | **不可比** | **相符** | **同一物** |
| `$Telematic_Power$` | **`PowerSts_Telematic`**（`BO_ 1470`）| **不可比** | **不可比** | **相符** | **同一物** |

### 項③ 之逐項對應（唯一可比之項，故全文列出）

**`$TGW_DISP_STAT$`** —— `VAL_ 1500` 逐字：
`0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA"`

| 規格側所用之值 | 出處 | DBC 側 | 對應 |
|---|---|---|---|
| `[DISP_OFF]` | `4819459`／`4819466`／b03 | `0 "Display_off"` | 相符 |
| `[DISP_NORMAL]` | `4819564`／b03 | `2 "Normal_mode"` | 相符 |
| `[ON_BLANK]` | `4819466` | `8 "On_blanked_screen"` | 相符 |
| `[DISP_REAR_CAMERA]` | `4819475` | `7 "Rear_Camera_Display"` | 相符 |
| `[SNA]`／`[Fh: sna]` | `4819466`／`4819344` | `15 "SNA"`（Fh ＝ 15）| 相符 |

**規格側所用之值全部有對應，無落空者 → 項③ 相符。**

**`$Telematic_Power$`** —— `VAL_ 1470` 逐字：
`0 "Sleep" 1 "Standby" 2 "Timed" 3 "Idle" 4 "Full_Operation" 5 "Logistic_On" 6 "Bench" 7 "Partial_Operation"`

| 規格側所用之值 | 出處 | DBC 側 | 對應 |
|---|---|---|---|
| `[Idle]` | `4819144`／`4819564`／`4820117`／b03 | `3 "Idle"` | 相符 |
| `[Full_Operation]` | `4819144`／`4819561`／`4820117`／b03 | `4 "Full_Operation"` | 相符 |
| `[BO_OFF_TGW_OFF]` | `4820075`（**v2 不適用**）| **無對應** | **落空** |

**落空之一項出自 v2(b) 判不適用之物件**，故不入本 DUT 之可比集；
但**具名列出，不隱去** —— 若日後該物件之適用性改判，項③ 須重評。

### 候選是否多於一而不能分辨 —— 否

A 檔另有三個 `*DISP_STAT*` 候選，**皆由項③ 清楚分辨**：

| 候選 | `VAL_` | 與 `$TGW_DISP_STAT$` 之規格值集 |
|---|---|---|
| `DCSD_DISP_STAT` | `0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA"` | 不符（規格另以 `$DCSD_DISP_STAT$ = [ON]/[OFF]` 指之，見 `4819561`／`4820075`）|
| `FPDM_DISP_STAT` | 同上六值 | 不符 |
| `TGW_FPDM_DISP_STATSts` | 同上六值 | 不符 |

## §3 三分結論

| 訊號 | 結論 | 依據 |
|---|---|---|
| `$TGW_DISP_STAT$` → `TGW_DISP_STATSts` | **同一物** | 可比項僅①③之③，且相符；候選可分辨 |
| `$Telematic_Power$` → `PowerSts_Telematic` | **同一物** | 同上 |

**【E23 未觸發】** —— 二訊號皆不落入 R-17(d) 之三情形
（非「全無對應」、非「候選多於一不能分辨」、非「僅語意相近而三項不符」）。

**但須明白記載本判定之強度**：三項中**二項不可比**（規格側既未載訊息名亦未載位元佈局），
**同一物之認定僅繫於項③ 一項**。後綴 `Sts` 之差依 R-17 既不構成證據亦不構成反證，
故未列入。**若日後取得載有訊息名或位元佈局之規格件，本判定須重驗。**

## §4 下放包未預料之事

1. **【E25】第四支 dbc 存在，且 R1／R4／R5 世代錯配**（見 §0）——
   本 DUT 為 R1L，而已綁之二支為 R4／R5，未綁之二支為 R1。
2. **CFTS020 全文不載任何 CAN 訊息名**（四個訊息名命中皆 0）——
   這使 R-17(c) 項① 對本線**永遠不可比**，不只本二訊號。
   R-17(c) 之三項判準在本語料上實際只有一項可用。
3. **`BHCAN2` 在 CFTS020 中查無**，規格只載 `BH-CAN`（54 個物件）。
   Pei 之裁定與規格用語之對應關係，規格內無可判之依據。
4. **A 檔（BHCAN2）之 `BU_` 無 `ICS` 節點**（只有 `ETM FPDM LTM SGW`），
   而 B 檔（R4）之 `PowerSts_Telematic` 收方明列 `ICS`。詳見作業 B §4。

## §5 已知局限

- 項①②之「不可比」係就 **CFTS020** 而言；若 SYSAD 或其他未掃件載有訊息名／位元佈局，
  本判定可再強化。**A-ICS78 之掃描起點盲區在此直接生效** —— 本作業只掃了 CFTS020。
- `VAL_` 比對以字面對應為之；未驗證實際位元值與規格語意之一致性（規格未給位元值）。
- 四檔之 `BO_ 2654208036 NWM_TELEMATIC` 為網管訊息，本作業列入候選但未深究。
