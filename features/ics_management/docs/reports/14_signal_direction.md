# 作業 B — 發收方向（A-ICS87／R-17(e)）｜2026-08-30

**前提**：作業 A 判二訊號皆為**同一物**，故二者皆進入本作業。

---

## §1 BHCAN2 之逐字

### `BO_` 定義行（逐字）

```
BO_ 1500 TELEMATIC_DISPLAY2: 8 ETM
BO_ 1470 STATUS_TELEMATIC: 8 ETM
BO_ 1445 DIS_CENTERSTACK: 8 SGW
BO_ 1282 RADIO_B2: 8 ETM
```

### `BO_TX_BU_` 列（逐字，**A 檔全部 14 條**）

```
BO_TX_BU_ 1478 : ETM,LTM;      BO_TX_BU_ 899 : ETM,LTM;
BO_TX_BU_ 2654208036 : ETM,LTM; BO_TX_BU_ 302 : ETM,LTM;
BO_TX_BU_ 303 : ETM,LTM;       BO_TX_BU_ 1282 : ETM,LTM;
BO_TX_BU_ 1283 : ETM,LTM;      BO_TX_BU_ 1284 : ETM,LTM;
BO_TX_BU_ 1285 : ETM,LTM;      BO_TX_BU_ 1470 : ETM,LTM;
BO_TX_BU_ 1500 : ETM,LTM;      BO_TX_BU_ 156 : ETM,LTM;
BO_TX_BU_ 158 : ETM,LTM;       BO_TX_BU_ 1291 : ETM,LTM;
```

### 收方清單（逐字）

- `SG_ TGW_DISP_STATSts` 於 `BO_ 1500` → 收方 **`SGW`**
- `SG_ PowerSts_Telematic` 於 `BO_ 1470` → 收方 **`FPDM,SGW`**

### `BU_` 節點表（逐字）

```
BU_: ETM FPDM LTM SGW
```

**`LTM` 在表內；`ICS` 不在表內。**

---

## §2 `BO_TX_BU_` 之語意 —— 佐證遠多於下放包所要之三個

下放包要求「取**至少三個**其他訊息作對照」。實測 A 檔共 **14 條** `BO_TX_BU_`，
**每一條的值都完全相同：`ETM,LTM`**，無一例外。

| 對照訊息 | `BO_` 名義發方 | `BO_TX_BU_` |
|---|---|---|
| `BO_ 1282 RADIO_B2` | `ETM` | `ETM,LTM` |
| `BO_ 1283`／`1284`／`1285` | `ETM` | `ETM,LTM` |
| `BO_ 2654208036 NWM_TELEMATIC` | `ETM` | `ETM,LTM` |
| `BO_ 302`／`303`／`156`／`158`／`899`／`1291`／`1478` | — | `ETM,LTM` |

**結論**：`BO_TX_BU_` 在本檔中**不是逐訊息客製的「追加發送方」**，
而是一致的**發送方替代集**（該訊息由 `ETM` **或** `LTM` 發送，依配置而定）。
其語意**不是本例特有之解讀** —— 14/14 一致，且 `BO_ 1500`／`1470` 之名義發方
`ETM` 亦與其餘 12 條同型。

**A-ICS87 之疑慮成立**：`LTM` 於 `BO_TX_BU_ 1500`／`1470` 為**發送側**，非收方。

### 規格側獨立佐證 —— 方向一致

CFTS020 逐字（**不是從 DBC 推來的**）：

| 物件 | 逐字 | 方向 |
|---|---|---|
| `4819561` | `... then the HU shall immediately send $TG...` | **HU 發送** `$TGW_DISP_STAT$` |
| `4819564` | `If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] ...` | **HU 發送** |
| `4819459` | `... the HU shall send $TGW_DISP_STAT$ = [DISP_OFF].` | **HU 發送** |
| `4819344` | `When the HU has a loss of communication condition with the ICS, the HU shall set TGW_DISP_STAT = [Fh: sna].` | **HU 設定** |

**規格與 DBC 二側獨立地同指一個方向：`$TGW_DISP_STAT$` 由 HU（本 DUT）發出。**

---

## §3 三 dbc 方向矩陣（自檔案重算，非轉抄 upstream-13 §4-2）

| 訊號 | **A：BHCAN2**（裁定）| B：R4_BHCAN（已綁）| C：R5_FDCAN8（已綁）| D：R1_FDCAN8（第四支）|
|---|---|---|---|---|
| `TGW_DISP_STATSts` | `BO_1500` **ETM**→`SGW`；`BO_TX_BU_`＝`ETM,LTM` | `BO_1500` `SGW`→`DCSD` | `BO_1427` `ETM`→`Vector__XXX` | 同 C（逐項相同）|
| `PowerSts_Telematic` | `BO_1470` **ETM**→`FPDM,SGW`；`BO_TX_BU_`＝`ETM,LTM` | `BO_1470` `SGW`→**`AMP,ANC,DCSD,ICS`** | `BO_1427` `ETM`→`TBM` | 同 C |
| `DCSD_DISP_STAT` | `BO_1445` `SGW`→**`ETM,LTM`** | `BO_1445` `DCSD`→`SGW` | **未載** | 未載 |

**與 upstream-13 §4-2 之差異**：upstream-13 未列 `BO_TX_BU_`，亦未列 D 檔。
發收方之記載本身**逐項相符**，無矛盾 → **與 E21 之前次判定一致**。

三訊號首尾相接，**由 SGW 閘道轉發可解釋**：
`DCSD` --(B)--> `SGW` --(A)--> `ETM,LTM`；`ETM/LTM` --(A)--> `SGW` --(B)--> `DCSD`。

---

## §4 【本作業最重之發現】`$Telematic_Power$` 在裁定之匯流排上，本 DUT 收不到

CFTS020 逐字（`4819144`、`4820117`，二者**皆 v2 適用**）：

> Regarding Enable Condition 1, when the ICS **receives** $Telematic_Power$ = [Idle] the ICS shall disable all Diagnostics and when the ICS **receives** $Telematic_Power$ = [Full_Operation] the ICS shall enable all Diagnostics.

**規格說 ICS 接收 `$Telematic_Power$`。** 而實測：

| 檔 | `PowerSts_Telematic` 之收方 | `ICS` 在收方？ | `ICS` 在 `BU_`？ |
|---|---|---|---|
| **A：BHCAN2（Pei 裁定）** | `FPDM,SGW` | **否** | **否**（`BU_: ETM FPDM LTM SGW`）|
| B：R4_BHCAN（已綁）| `AMP,ANC,DCSD,ICS` | **是** | 是 |

**即：規格所述之「ICS 接收 `$Telematic_Power$`」，在 Pei 裁定之 BHCAN2 上不成立，
而在未被裁定之 R4_BHCAN 上成立。**

且於 A 檔，`BO_TX_BU_ 1470 : ETM,LTM` 表示本 DUT 是該訊息之**發送側**——
**本 DUT 在裁定之匯流排上是 `$Telematic_Power$` 的發出者，不是接收者。**

**不調和。** 這是 Pei 之裁定與規格語句之間的一個實測落差，屬範圍事項。

---

## §5 對 b03 八條之影響（逐條）

### 八條之現行寫法為「讀匯流排軌跡」，非「HU 收到」

八條之步驟一律為
`Read the display status signal on the CAN trace ...`，
ER 一律為 `The display status signal reports the "..." value on the CAN trace (supporting observation)`。

**無一條斷言「HU 接收該訊號」**。「讀 CAN trace」對發／收兩側皆成立 ——
只要訊號出現在該匯流排上即可讀取。

### 逐條判定

| # | tc_title | 現行 `$TGW_DISP_STAT$` 語句之性質 | 依 R-17(e) 改寫後之驗證目標 | 判 |
|---|---|---|---|---|
| 1 | Power hardkey pressed while HU screen on | 讀 trace，佐證 | 不變（主目標為畫面狀態變化）| **可改寫** |
| 2 | Power hardkey pressed at Telematic Power full operation | 同上 | 不變 | **可改寫**（但見下方前提問題）|
| 3 | Power hardkey pressed while HU screen off | 同上 | 不變 | **可改寫** |
| 4 | Power hardkey pressed at Telematic Power idle | 同上 | 不變 | **可改寫**（但見下方前提問題）|
| 5 | Screen off hardkey starts the three second timer | 同上 | 不變 | **可改寫** |
| 6 | Screen off hardkey pressed again within three seconds | 同上 | 不變 | **可改寫** |
| 7 | Three second period completed after screen off hardkey | 同上 | 不變 | **可改寫** |
| 8 | Screen off hardkey pressed while HU screen off | 同上 | 不變 | **可改寫** |

**八條皆判「可改寫」，驗證目標不變。**

### 【E22】依其字面 —— **未觸發**

E22 之判準為「任一條 b03 TC 之**驗證目標**會因方向改寫而改變」。
八條之驗證目標皆為「DUT 於受刺激後將顯示狀態驅動至值 V」，
改寫方向敘述（`Read ... on the CAN trace` → `... transmitted by the DUT`）**不改變該目標**。
故依 E22 之字面**未觸發**。

**方向澄清反而使八條變強**：既然本 DUT 是 `$TGW_DISP_STAT$` 之發出者，
該 ER 就不只是 `supporting observation`，而是**對 DUT 輸出之直接觀察**。
八條現皆標記為 `(supporting observation)` —— **此標記在方向確立後可能不再正確**，
但改標記非本包之事（禁區：零 ER 改寫）。**只列不改。**

### 但另有一件屬範圍事項，E22 之字面涵蓋不到 —— 具名呈報

**TC 2 與 TC 4 之前提可能在裁定之匯流排上無法建立。**

二者之前提分別為 `Telematic Power = Full Operation` 與 `= Idle`。
依 §4，於 A 檔（BHCAN2）本 DUT 是 `PowerSts_Telematic` 之**發送側**，
`ICS` 既非收方亦不在 `BU_` 內 —— **台架無法在該匯流排上「餵給 DUT」這個前提值**。

此非「驗證目標改變」（故 E22 字面未觸發），而是「**前提之可建立性**」。
**屬範圍事項，須由 Pei 裁。** 本作業**不調和、不改寫、不推定可行**。

---

## §6 下放包未預料之事

1. **§4：規格之「ICS 接收 `$Telematic_Power$`」在裁定之 BHCAN2 上不成立**，在未裁定之 R4 上成立。
2. **§5：TC 2／TC 4 之前提可能無法在 BHCAN2 上建立** —— E22 字面涵蓋不到之範圍事項。
3. **§5：八條之 `(supporting observation)` 標記在方向確立後可能不再正確**（可升為直接觀察）。
4. **§2：`BO_TX_BU_` 在 A 檔為 14/14 一致之發送方替代集**，非逐訊息之追加 ——
   語意比 A-ICS87 所述更強。
5. A 檔無 `ICS` 節點，但 upstream-13 曾報 A 檔有 `BO_ 1050 CLIMATIC_PANEL: 8 SGW`
   且 `Radio_btn0` 收方僅 `LTM` —— **刺激面（按鍵）在 A 檔可觀察，前提面（Telematic_Power）不可餵**。
   二者在同一檔上一可一不可，此不對稱下放包未預料。

## §7 已知局限

- 本作業未量 `RQ_DISP_INTS`（八條之另一佐證訊號）於四檔之發收方；
  若其方向亦有問題，八條之判定須重評。
- 「驗證目標不變」之判定基於八條**現行文字**；
  若 Pei 認為 ER 應由 `supporting observation` 升為主要斷言，該判定須重評。
- `BO_TX_BU_` 之語意結論建立在 A 檔內部之一致性（14/14），
  未與 Vector DBC 規格文件對照 —— 該文件不在 repo。
