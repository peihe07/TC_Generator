# 00H 下放包補篇 — DBC 之 R4／R5 語意（**推翻 A-VS07 之前提，R-VS8 改寫**）

分析層寫入，2026-08-20，同一往返（NN = 00）。
素材：Pei 於聊天提供之 `PDT25_E3A_R4_FDCAN8_vs_PDT25_E3A_R5_FDCAN8.xlsx`
（沙箱副本 23,156 bytes，SHA256 `74d11e1b…02e2`），**尚未入 `inputs/`**。

---

## 0. 本篇撤回之陳述（**自我更正，canon §5a 第 15／16 條**）

00C §5-3 與 00E §2 之 `R-VS8` 寫：

> 兩份 DBC **分屬不同 release**，`HSW_StatFailSts` **只存在於 R4**；
> **選錯 DBC 會使 16 個 leaf 的訊號斷言落空** → 須裁定基線 DBC

**該陳述之前提為誤。** 兩份 DBC 之差異**不是 release，是匯流排**。

實測（對 `inputs/` 兩檔之原始文字）：

| 項 | `PDT27_E2A_R4_BHCAN.dbc` | `PDT27_E2A_R5_FDCAN8.dbc` |
|---|---|---|
| `BA_ "VersionYear"` | **25** | **25** |
| `BA_ "VersionWeek"` | **50** | **50** |
| `BA_ "BusType"` | （無此屬性） | **`"CAN FD"`** |
| messages | 155 | 323 |
| 名稱含 `_FD` 之 message | **0** | 多數 |

**兩檔之版本屬性完全相同（2025 年第 50 週）。**
`R4`／`R5` 不是 release 序號 —— 它是**匯流排／網段之代號**，
與檔名後段之 `BHCAN`／`FDCAN8` 同指一事。

集合關係亦與「同一內容之兩個版本」不相容：

| | 值 |
|---|---|
| 僅存於 BHCAN 之 message | **119** |
| 僅存於 FDCAN8 之 message | **287** |
| 共有 message | **36** |
| 僅存於 BHCAN 之 signal | 742 |
| 僅存於 FDCAN8 之 signal | 1,614 |
| 共有 signal | 141 |

**兩個 release 不會有 119／287 之互斥；兩條匯流排會。**

### 0.1 正確之讀法

本 feature 所需之 message 全部落在 **BH-CAN**，與 LID 表逐項相符：

| message | BHCAN | FDCAN8 | LID 表所載之 CAN |
|---|---|---|---|
| `STATUS_CSWM`（座椅／方向盤狀態與失效） | **有** | 無 | CAN-B |
| `STATUS_CLIMATE8`（Tri-Level HSW） | **有** | 無 | CAN-B |
| `TELEMATIC_DISPLAY2`（`TGW_DISP_STATSts`） | **有** | 無 | CAN-B |
| `TELEMATIC_VEHICLE_SETUP3`（按鍵請求） | **有** | 無 | BH-CAN |
| `STATUS_BH_BCM2`（`CmdIgnSts`） | **有** | 無 | CAN-B |
| `TELEMATIC_FD_4`（`TGW_DISP_STATSts` 之 FD 對應） | 無 | **有** | CAN-FD |
| `BCM_FD_10`（`CmdIgnSts` 之 FD 對應） | 無 | **有** | FD |

→ `HSW_StatFailSts` 不在 FDCAN8，**是因為它本來就在 CAN-B 上**
（LID 表 `HSW_Stat` 之 CAN 欄逐字為 `CAN-B`），**不是版本落差**。

**A-VS07 之描述作廢，改寫如 §2。**

---

## 1. Pei 提供之比對表說明了什麼

`PDT25_E3A_R4_FDCAN8` vs `PDT25_E3A_R5_FDCAN8`，`New Compare1` 表 16 列。

**注意其檔名為 `PDT25_E3A`，而 `inputs/` 之兩檔為 `PDT27_E2A`**
—— **平台碼與架構碼皆不同，非同一組檔案之比對。**

其內容（全 3 筆差異，逐筆照錄）：

| message | signal | 屬性 | R4 | R5 |
|---|---|---|---|---|
| `TELEMATIC_FD_19`（91h） | `Secure_Idle_Req` | `GenSigStartValue` | 1 | 0 |
| `ADAS_FD_HMI`（5B0h） | `HAS_TelltaleSts` | `Max` ／ `Value: 7` | 6 ／ `SNA` | 7 ／ `RED_HANDS_FREE` |
| `SPAAK_FD`（5C7h） | `PhoneKeyPair_Stat1` | `Value: 7` | `<Not Defined>` | `Key_Added_Success_Not_Activated` |

**三筆與本 feature 無交集**（Secure Idle、ADAS 手放偵測遙控、Phone Key）。

**但它提供了一項關鍵資訊**：該表第 3 列之 `VersionWeek` 為
**R4 = 18、R5 = 38** —— **在 `PDT25_E3A` 這一組裡，`R4`／`R5` 確實是
不同版本**（同為 FDCAN8 匯流排，週次不同）。

### 1.1 由此得到的判準（**本篇之主要產物**）

> **`R4`／`R5` 之語意不能由檔名決定，須由檔內 `VersionYear` +
> `VersionWeek` + `BusType` 三項屬性判定。**
>
> - 同匯流排、週次不同 → **是版本**（`PDT25_E3A` 之 R4/R5：週 18 vs 38）
> - 匯流排不同、週次相同 → **是網段**（`PDT27_E2A` 之 R4/R5：皆 25 年第 50 週）
>
> **同一組檔名慣例在兩個平台上表示兩件不同的事。**
> 這正是 canon §5a 第 9 條之形態：**版本標籤不識別內容**
> （同 AMFM 之 `CIP_Radio_Tables`、`Market Configuration v1.6`）。

---

## 2. 條文與異常之淨變動

```
R-VS8（改寫，取代 00C §5-3 與 00E §2 之版本）
本 feature 之 CAN 基線為「兩份並用」，非二擇一：

  PDT27_E2A_R4_BHCAN.dbc   —— BH-CAN／CAN-B 網段。本 feature 之
      STATUS_CSWM（座椅與方向盤狀態、*_STATFailSts）、STATUS_CLIMATE8
      （Tri-Level HSW）、TELEMATIC_DISPLAY2（TGW_DISP_STATSts）、
      TELEMATIC_VEHICLE_SETUP3（按鍵請求）、STATUS_BH_BCM2（CmdIgnSts）
      全部在此。**主要來源。**

  PDT27_E2A_R5_FDCAN8.dbc  —— CAN-FD 網段（BA_ "BusType" = "CAN FD"）。
      承載同一批邏輯訊號之 FD 對應（TELEMATIC_FD_4、BCM_FD_10）。
      **僅於 TC 需指明 FD 網段時引用。**

兩檔之 VersionYear = 25、VersionWeek = 50，完全相同 —— 不存在
「選錯版本」之風險。R4／R5 在本組檔名中指網段，不指 release。

配套判準（適用於日後任何 DBC 之入庫）：
DBC 之身分由檔內 BA_ "VersionYear" / "VersionWeek" / "BusType" 三項
屬性判定，不由檔名之 R 碼判定。入庫時須記錄該三項屬性與 SHA256。
```

| 異常 | 變動 |
|---|---|
| **A-VS07** | **作廢**（前提為誤）。改記為 **A-VS07′**：DBC 檔名之 `R4`／`R5` 在 `PDT27_E2A` 組指網段、在 `PDT25_E3A` 組指版本週次 —— **同一慣例兩種語意**，屬上游命名缺陷，列 RD-1（FYI 類，不需上游動作，我方以檔內屬性判定即可） |
| **A-VS11（新）** | Pei 提供之比對表為 `PDT25_E3A` 組，與 `inputs/` 之 `PDT27_E2A` 組**非同一平台**；本 feature 目前**沒有** `PDT27_E2A` 組之跨版本比對表。若日後基線升版，須另取該組之比對表 |

---

## 3. 對 R-VS9 之影響（訊號書寫形式）

00G §2 已將第一權威由 DBC 改為 LID 表。本篇再加一層：

**LID 表之 `CAN` 欄（`CAN-B`／`CAN-FD`／`BH-CAN`）與兩份 DBC 之
message 歸屬完全一致**（§0.1 之七列逐項相符）。
→ **三來源（CFTS044／LID 表／DBC）在訊號名與網段上互相印證，無矛盾。**

建議 R-VS9 之條文形式：

```
R-VS9（修訂建議，待裁）
TC 中書寫 CAN 訊號時：
(1) 訊號逐字名與所屬 message 以 Logical Identifiers and CAN Mapping
    之 Atlantis High 欄為第一權威；該欄為空者依 R-VS11 之裁定處理
(2) 值域以同表 Format 欄為準，並與對應 DBC 之 VAL_ 表交叉核對；
    兩者不一致時停下回報，不自行調和
(3) 網段（CAN-B／CAN-FD）依 LID 表 CAN 欄註明，並對應至
    PDT27_E2A_R4_BHCAN.dbc 或 PDT27_E2A_R5_FDCAN8.dbc
(4) $var$ 形態僅出現於 test_item 上半段之來源逐字內，
    不出現於 procedure／expected_result 之作者自撰文字
理由：$PowerMode$ 之匯流排名為 CmdIgnSts，而 DBC 內另有一支
PowerModeSts；以 DBC 名稱檢索會抓到錯的訊號。
```

---

## 4. 素材落檔（Tier 3）

建議一併入 `features/vehicle_setting/inputs/`：

| 檔 | 理由 | 沙箱 SHA256 |
|---|---|---|
| `Logical Identifiers and CAN Mapping v1.76.xlsx` | 訊號名與值域之第一權威（00G） | `ffceac36…8ef4` |
| `PDT25_E3A_R4_FDCAN8_vs_PDT25_E3A_R5_FDCAN8.xlsx` | **證據性素材**：R4/R5 語意判準之來源（本篇 §1.1）。**與本 feature 之訊號無交集**，入庫目的為存證而非取值 | `74d11e1b…02e2` |

兩者之沙箱 SHA 僅證明副本自洽，**權威值由執行層於 `inputs/` 實體檔重取**。

---

## 5. 本篇之盲區（R-G11）

1. **`BusType` 屬性只有 FDCAN8 那份有**；BHCAN 那份無此屬性，
   其「BH-CAN 網段」之身分係由**檔名 + message 命名 + LID 表 CAN 欄**
   三者推得，**非檔內自述**。若上游之 BHCAN 檔實為他網段，本篇會錯
2. `VersionYear`／`VersionWeek` 取 `BA_` 之首次命中；**若檔內有多筆
   同名屬性（分節不同值），本篇只讀到第一筆**
3. 集合比對以 message／signal **名稱**為單位，未比對 id、長度、
   起始位元、factor／offset。**同名不同定義之情形本篇看不到** ——
   建 `data/can_signal_map.tsv` 時須逐屬性比對（canon §5a 第 14 條：
   通過條件應寫成「與參照對象在所有可讀屬性上一致」）
4. Pei 提供之比對表為**他人產出之靜態轉錄**，本篇未複驗其比對過程；
   依 G-F，靜態轉錄之時效性須以指紋管理 —— 已記其 SHA
