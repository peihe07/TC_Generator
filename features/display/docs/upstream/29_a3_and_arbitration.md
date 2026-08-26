# 上繳包 29 —— A3 之結果推翻了本批之門檻前提（停止條件 76 觸發）

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/29_a3_and_arbitration.md`
- **停止條件 76 觸發**：CFTS_013 §1.5.3 之 **13 條全部適用本專案**，
  其門檻為 **50／51–55／56–<60 degrees C**，與 CFTS_020 `{4820289}` 之
  **85 degrees C** 不符。**未併算、未判何者為準、未改任何 TC。**
- 停止條件 77／78 未觸發；1–75 亦全未觸發
- **步驟 6（D1／D2／D3）已於 28a 執行並 commit**（`73ac307`），見 §六
- **git 未執行**（§八為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 1 | R-DM55 抄錄相符；R-DM 區塊累計 **57**，順序驗證 exit 0 |
| 2 | A3 續行。**停止條件 76 觸發** —— 詳見 §二。過程中本層之適用性判準出錯一次（A-DM40） |
| 3 | `popup_priority.tsv` 已建（**1341 列 = PU 母體**，1272 已解析／69 `UNRESOLVED`），三項揭露俱全 |
| 4 | DR-DM12 開立；DR-DM2 補充、DR-DM4 重擬皆已寫入（標「待 Pei 發」） |
| 5 | `BACKLOG.md` 新增「DR-DM12 回覆後重審」節；A1 更新為「已建，帶三項揭露」 |
| 6 | **28a 輪已完成**（`73ac307`）—— 本輪複核其產出仍在，未重做 |
| 7 | INDEX 已更新 |

---

## 一、R-DM55 之抄錄核對表

## 抄錄核對表 — 29_a3_and_arbitration.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 57 | R-DM55 | `features/display/RULINGS.md` | 821 | `463ddfbcf09ab98c` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **57** 個，與各下放包原檔逐字元比對 **全數相符**（57 vs 57）。

置放依 R-G34：`RULINGS.md` 之新節「來源：下放包 29」。

---

## 二、A3 之續行 —— **停止條件 76 觸發**

### 2.1 取法：按內容取，非按號取

依 A-DM39，3 位條號在此檔不存在，故以**節標題**定位。
抽取式：`^(1\.\d+(?:\.\d+)*)\s+(.*?)\s*\{(\d{7})\}$`，
排除含 tab 者（目次項）。本文標題共 16 個，四個 DCSD 專節逐字如下：

```text
1.5   DCSD Display Hot Error Behavior {4943077}
1.5.1 Activating the DCSD Display Hot Algorithm {4943080}
1.5.2 Standard HU and DCSD DIsplay Hot', Screen Priority and HMI Event processing {4943082}
1.5.3 Multi-stage HU and DCSD Display Hot', Screen Priority and HMI Event processing {4943095}
```

### 2.2 【先報錯】本層之適用性判準出錯一次（A-DM40，已更正）

首算以 `"R1H" in Radio and "Atlantis High" in EE` 判適用性 ——
**該判準在 CFTS_020 上一直正確**（21／28 兩輪皆用它，該檔逐一列舉架構名）。

**而 CFTS_013 對 1.5.3 全節寫 `EE Architecture:All`。**

| | 首算（錯） | 更正後 |
|---|---:|---:|
| §1.5 | 0 | 0 |
| §1.5.1 | 1 | **1** |
| §1.5.2 | 0 | **0** |
| **§1.5.3** | **0** | **13** |

**首算之結論是「CFTS_013 之 DCSD Display Hot 全部不適用本專案」，
更正後是「Multi-stage 全節 13 條全部適用」。結論完全相反。**

**是不合理感觸發複驗，不是機器抓到的** —— 一份 CFTS_013 若對本專案
完全不適用，CFTS_020 不會五次轉指它。全檔 `EE Architecture` 之值域
實測（出現次數計）為 `All` **68**／`PowerNet` 16／`Atlantis Mid` 4／
`Small/Compact` 2／`CUSW` 2／**`Atlantis High` 1** —— 該分布本身就是線索。

**回溯檢查**：21／28 兩輪之適用性量測皆針對 CFTS_020，
該檔之 `EE Architecture` 值域**不含 `All`**，**故未受本項影響**。

> 形態同 A-DM29（子字串偽陽性）與上繳 26 §5.2（STALE 候選集）：
> **判準寫得像在量測，實際上編碼了一個未被檢查的假設。**
> R-G27 防的是**過寬**，本項是**過嚴** —— 兩者同源。

### 2.3 適用性（更正後）

| 節 | 條數 | 適用本專案 | 其 Radio／EE |
|---|---:|---:|---|
| §1.5（引言） | 2 | **0** | `{4943078}` EE=`PowerNet, Atlantis Mid`；`{4943079}` Radio=`VP384, VP3` |
| §1.5.1 | 1 | **1** | `{4943081}` Radio 含 `R1H`，EE=`Atlantis High, Atlantis Mid, PowerNet` |
| §1.5.2 Standard | 11 | **0** | 11 條之 Radio 全為 VP 系列，EE 全為 `PowerNet` |
| **§1.5.3 Multi-stage** | 13 | **13** | 13 條之 Radio 皆為 `R1L, R1H, R1L-R, R1M`，**EE 皆為 `All`** |

**即：對本專案而言，CFTS_013 所定之 DCSD Display Hot 演算法是
Multi-stage 那一套；Standard 那一套明文不適用。**

### 2.4 §1.5.1 逐字全文（適用，1 條）

```text
4943081: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, VP4R7, VP5R120, VP484, VP384, R1M, VP365, R1H, VP4R84, R1L-R, VP465, VP3, VP4] [EE Architecture:Atlantis High, Atlantis Mid, PowerNet]

The HU shall activate the HU Display Hot Algorithm based on 2 conditions:
1) The current System State is Body ON HU Audio Mode ON, BODY ON or BODY OFF-TIMED HU Audio Mode OFF, Body OFF HU System ON or Body OFF BENCH MODE.
2) The HU has finished displaying the complete set of Start-up Sequence screens (See {4943620} or {4944307} or {4944324} for the Startup Animation, Splash Screen, Disclaimer Screen and Rear/Surround View Camera Screen sequencing).
```

### 2.5 §1.5.3 逐字全文（13 條全部適用）

```text
# 1.5.3 Multi-stage HU and DCSD Display Hot', Screen Priority and HMI Event processing {4943095} —— 逐字全文（13 條全部適用本專案）
========================================================================

{4943096}  4943096: [Artifact Type:Description] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1H, R1L-R, R1M] [EE Architecture:All]
  In order to protect user when they touch the screen and it is in hot condition the HU will implement a 'Multi-stage HU and DCSD Display Hot Algorithm' as described in this section. In this case when the display touch screen surface has reached a temperature of 50 degrees C or higher the 'Multi-stage HU and DCSD Display Hot Algorithm' functionality shall be implemented.

{4943097}  4943097: [Artifact Type:Description] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L-R, R1L, R1H, R1M] [EE Architecture:All]
  The Multi-stage Display Hot algorithm shall not be implemented by the DCSD supplier. Follow other Component Technical Specification for further details.

{4943098}  4943098: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1L-R, R1H, R1M] [EE Architecture:All]
  After system bootup the DCSD shall begin monitoring its display touch screen surface temperature at a rate of once per minute.

{4943099}  4943099: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1H, R1M, R1L, R1L-R] [EE Architecture:All]
  When the display touch screen surface has reached a temperature >= 51 degrees C and <=55 degrees C the DCSD shall reduce the touch screen backlight intensity relative to the 'requested' intensity by 5% for each degree C above 50 degrees C as a slope function. See the $RQ_DISP_INTS$ signal for the 'requested' intensity. So at 50 degrees C or lower there is no backlight intensity adjustment. At 51 degrees C the intensity is reduced by 5% relative to the 'requested' backlight intensity. At 55 degrees C the intensity is reduced by 25% relative to the 'requested' backlight intensity. Note: The 'requested' backlight intensity sent in the $RQ_DISP_INTS$ signal is determined by the HU based on the User Display settings (Auto versus Manual, Display Brightness Headlights On/Off), current Day / Night Mode and the requested Instrument Panel setting (usually controlled using a thumbwheel switch) - see {VF041} - 'Instrument Lighting' or 'Backlight Management' or {VF668} - 'Backlight Actuation Management'.

{4943100}  4943100: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1L-R, R1M, R1H] [EE Architecture:All]
  When the display touch screen surface has reached a temperature >= 56 degrees C and <60 degrees C and no other higher priority screen is to be shown, the DCSD shall not lower the screen intensity any further, shall inform the HU that the DCSD screen is hot (see {4821587}) and the HU shall display the "Screen is Hot" warning (See the latest version of the referenced document [*HMI * Logic and Flow*] or [*Pop Up List*] for the "HU Display Hot" screen design).

{4943101}  4943101: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1L-R, R1H, R1M] [EE Architecture:All]
  While displaying the "Screen is Hot" warning the HU shall "limit" radio HMI functionality by ignoring any "limited" HMI events. See {4943102} for a definition of "limited" versus "non-limited" HMI events.

{4943102}  4943102: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1H, R1L, R1M, R1L-R] [EE Architecture:All]
  HMI functionality shall be "limited" as follows when the 'Screen is Hot' warning is displayed: - LIST/ENTER knob shall be disabled. - All touch screen behavior shall be ignored.

{4943103}  4943103: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1H, R1L, R1L-R, R1M] [EE Architecture:All]
  While displaying the "Screen is Hot" warning if an event occurs that results in the system transitioning to a state where a screen with higher priority (ex. Rear/Surround View Camera, SOS or Emergency Calls) than the "Screen is Hot" popup (Popup PU0130, a.k.a. 'Display is Hot') is to be shown, then the HU shall display that screen.

{4943104}  4943104: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1L-R, R1M, R1H] [EE Architecture:All]
  Once the DCSD has displayed the "Screen is Hot" popup for 10 seconds and no other higher priority screen is to be shown, the DCSD and HU shall send a sequence of messages/signals/values to implement the resulting behavior as defined in {4821589}, {4821590} and {4821591}. Note: Only DCSD shall implement 10 sec timer.

{4943105}  4943105: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1H, R1L, R1M, R1L-R] [EE Architecture:All]
  During the time that the DCSD display is in the OFF state, if a high priority screen is to be displayed the HU shall request the DCSD to turn the screen on at 'normal' intensity ({4821592}) and display the corresponding screen.

{4943106}  4943106: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1L, R1H, R1M, R1L-R] [EE Architecture:All]
  The DCSD shall display the high priority screen as long as it is possible to display without damaging itself.

{4943107}  4943107: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1H, R1M, R1L, R1L-R] [EE Architecture:All]
  When the DCSD Display transitions from a Hot state (> 50 degrees C) to a non-Hot state (<= 50 degrees C), the HU and DCSD shall resume 'Normal Screen Operation'.

{4943108}  4943108: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ALL] [Market:All] [Model Year:Default] [Radio:R1M, R1H, R1L-R, R1L] [EE Architecture:All]
  Figure {4943108} - 'Multi-stage HU and DCSD Display Hot' Logic & Flow
```

### 2.6 A3 之四項對照表 —— **只陳列，不判定**

| 項 | CFTS_013 §1.5.3（本專案適用） | 條號 |
|---|---|---|
| **(i) 分段變數** | **溫度**（`display touch screen surface … temperature`），監測頻率 `once per minute` | `{4943096}`／`{4943098}` |
| **(ii) 各級門檻與單位** | 啟動 `50 degrees C or higher`；`>= 51 且 <= 55 degrees C` → 背光每度降 5%（51→5%、55→25%）；`>= 56 且 < 60 degrees C` → 不再降亮度、通知 HU、顯示 `"Screen is Hot"` | `{4943096}`／`{4943099}`／`{4943100}` |
| **(iii) warning → off 之轉換條件** | **`Once the DCSD has displayed the "Screen is Hot" popup for 10 seconds and no other higher priority screen is to be shown`** → 依 `{4821589}`／`{4821590}`／`{4821591}` 送序列。**`Note: Only DCSD shall implement 10 sec timer.`** | `{4943104}` |
| **(iv) 回復條件** | `When the DCSD Display transitions from a Hot state (> 50 degrees C) to a non-Hot state (<= 50 degrees C), the HU and DCSD shall resume 'Normal Screen Operation'` | `{4943107}` |

### 2.7 與 CFTS_020 之關係 —— **只陳列，不判定**（停止條件 76）

| | CFTS_020 `{4820289}`／`{4820290}` | CFTS_013 §1.5.3 |
|---|---|---|
| 適用宣告 | `[Radio:R1H] [EE Architecture:Atlantis High]` | `[Radio:R1L, R1H, R1L-R, R1M] [EE Architecture:All]` |
| Hot 之門檻 | **`> 85 degrees C`** | **`> 50 degrees C`**（`{4943107}`） |
| non-Hot | **`<= 85 deg C`** | **`<= 50 degrees C`** |
| 量測對象之措辭 | `the DCSD Display transitions to a Hot state` —— **未名其量測何處之溫度** | `display touch screen surface … temperature` —— **明指觸控面** |
| 分段 | **無**（單一門檻，越過即四動作） | **有**（50／51–55／56–<60 三級） |
| warning → off | **未給時長**（21／26 輪之 DR-DM10(b) 即為此） | **`10 seconds`，且 `Only DCSD shall implement 10 sec timer`** |

**兩者之 Hot 門檻不符（85 vs 50）。依停止條件 76：停並回報，
不得逕改任何 TC。** `pilot-01` 三條之 `85 degrees C` **一字未動**。

**本層不判何者為準**（DR-DM10(a) 屬上游）。惟三項須具名：

1. **這正是 A-DM33 所預期之「第三種讀法」。** 21 輪本層曾判
   「組 A／組 B 兩組互斥」，並記「若答覆顯示存在第三種讀法，
   #4 之 ER 3 須重估」（`BACKLOG.md` DR-DM10 重審節首列）。**它出現了。**

2. **「量測對象不同故可並存」之解釋，經補驗後不成立。** 兩條並列：

   > `{4820290}`（CFTS_020）：`When the DCSD Display transitions from a Hot state (> 85 deg C) to a non-Hot state (<= 85 deg C), and then DCSD shall: …`
   >
   > `{4943107}`（CFTS_013 §1.5.3）：`When the DCSD Display transitions from a Hot state (> 50 degrees C) to a non-Hot state (<= 50 degrees C), the HU and DCSD shall resume 'Normal Screen Operation'.`

   **同一個主詞（`the DCSD Display`）、同一個句型、同一個轉換、
   不同的數字。** 我原先寫「CFTS_020 未名其量測何處，或許兩者量的是
   不同的東西」—— **補驗後該說法站不住**，此處具名更正（R-G19）。

3. **CFTS_020 之 `{4820289}`／`{4820290}` 為 `[Radio:R1H] [EE Architecture:Atlantis High]`
   之專條**（僅本專案），而 CFTS_013 §1.5.3 為 `[Radio:R1L, R1H, R1L-R, R1M]
   [EE Architecture:All]` 之通條。**兩者皆宣告涵蓋本專案**，
   其孰為特別法屬 Tier 2。

### 2.9 補驗：SYSRA 之同一組數字，其主詞是 **HU**，不是 DCSD

R-DM51 立於 24 輪，其禁止代入之依據為「CFTS013（SYSRA）之標的為
Associated Display（HU 側）」。**該依據本層此前未曾自行重算** ——
本輪補驗（`SYS2_CFTS013_…xlsx`，`Analysis Report`，逐列）：

```text
# SYSRA 中含溫度門檻之列（逐字），並標其主詞為 HU 或 DCSD

## r27  CFTS013-950   主詞=['（無 shall 主詞）']
   門檻=['50']
   In order to protect user when they touch the screen and it is in hot condition the HU will implement a 'Multi-stage Display Hot Algorithm' as described in this section. In this case when the display touch screen surface has reached a temperature of 50 degrees C or higher the 'Multi-stage Display Hot Algorithm' functionality shal

## r29  CFTS013-951   主詞=['HU shall']
   門檻=['>=51', '<=55', '50', '50', '51', '55']
   When the display touch screen surface has reached a temperature >= 51 degrees C and <=55 degrees C the HU shall reduce the 'normal' touch screen backlight intensity by 5% for each degree C above 50 degrees C. So at 50 degrees C or lower there is no backlight intensity adjustment. At 51 degrees C the intensity is reduced by 5% re

## r30  CFTS013-933   主詞=['HU shall']
   門檻=['>=56', '<60']
   When the display touch screen surface has reached a temperature >= 56 degrees C and <60 degrees C and no other higher priority screen is to be shown, the HU shall not lower the screen intensity any further and the HU shall display the "Screen is Hot" warning (See the latest version of the referenced document [*HMI * Logic and Fl

## r34  CFTS013-938   主詞=['HU shall']
   門檻=['>=60']
   When the display touch screen surface has reached a temperature >= 60 degrees C and no other higher priority screen is to be shown, the HU shall 'turn off' the screen (output a 'blank' video screen with the backlight intensity at zero).

## r36  CFTS013-942   主詞=['（無 shall 主詞）']
   門檻=['>50', '<=50']
   When the HU Display transitions from a Hot state (> 50 degrees C) to a non-Hot state (<= 50 degrees C), the radio shall resume 'Normal Screen Operation'.

# 全檔 'DCSD shall' 與 'HU shall' 之列數
  含 'the DCSD shall': 0
  含 'the HU shall'  : 6
```

**SYSRA 全檔 `the DCSD shall` 0 列、`the HU shall` 6 列**；
其回復條規定 `When the **HU Display** transitions from a Hot state (> 50 …)`。

**故 R-DM51 之依據成立且經本層重算確認** —— SYSRA 之
50／51–55／56–<60／60 確為 **HU 顯示器**之門檻。

**而本輪之新事實是**：CFTS_013 **docx** §1.5.3 以
`the DCSD shall`／`the DCSD Display` 為主詞，給了**同一組數字**。

| 來源 | 主詞 | 50／51–55／56–<60 | 適用本專案 |
|---|---|---|---|
| CFTS013 **SYSRA** | `the HU shall`／`the HU Display` | 有 | （R-DM51：Associated，不得代入 DCSD） |
| CFTS013 **docx §1.5.3** | `the DCSD shall`／`the DCSD Display` | **有** | **13/13 條適用** |
| CFTS_020 `{4820289}`/`{4820290}` | `DCSD shall`／`the DCSD Display` | **無 —— 為 85** | 專條，僅本專案 |

**即：R-DM51(a) 之禁止（不得以 SYSRA 之 HU 門檻代入 DCSD）仍然有效
且未被違反；但「DCSD 側沒有 50 這組數字」這件事，本輪起不再為真。**

**本輪不改 R-DM51，不改任何 TC，不解除任何 deferred。**

### 2.8 DR-DM10(b) 之問法，其答案形狀已現（**不據以行動**）

26 輪本層將 DR-DM10(b) 由「時長為何」改問「是否為溫度分段？
若是，其第二門檻為何？」。**§1.5.3 對此兩問皆有逐字答案** ——
分段變數是溫度，第二門檻是 `>= 56 且 < 60`，且 warning → off
另有 `10 seconds` 之計時器（`{4943104}`）。

**但這是 Associated／Disassociated 之外的另一層問題**：本節之標的
為 DCSD（Disassociated），與 R-DM51 所規制之 CFTS013 SYSRA
（Associated Display）**不是同一份文件、不是同一個標的** ——
SYSRA 之 50／51–55／56–<60 是 **HU 顯示器**，本節之同一組數字是
**DCSD 觸控面**。**兩處數字相同而標的不同，這件事本身須具名。**

**本輪不據此改動 DR-DM10(b) 之文字，亦不解除任何 deferred。**

---

## 三、`popup_priority.tsv`

### 3.1 產出

腳本 `features/display/scripts/popup_priority.py`（本輪新增），
入口呼叫 `verify_reference_binding.py`（R-G23）。

```text
# popup_priority —— 以類別碼為鍵之仲裁順序（R-G36 機器抽取）
binding: entries: 13
母體   : `Main` 之 PU 列 **1341**
已解析 : **1272**   UNRESOLVED: **69**

| rank | ladder_label（矩陣 p4 逐字） | code | 列數 |
|---|---|---|---:|
| 1 | RVC | `RVC` | 29 |
| 2 | Cat. X | `X` | 9 |
| 3 | Cat. SL **← PENDING** | `SL` | 26 |
| 4 | Anti-Theft  (Keypad and Anti-Theft pop-ups) | （清單欄 5 無對應寫法） | — |
| 5 | Cat. 1 | `1` | 1 |
| 5 | Cat. 1 —— 子類（矩陣 p7 逐字） | `1P` | 6 |
| 5 | Cat. 1 —— 子類（矩陣 p7 逐字） | `1T` | 3 |
| 6 | Display off (black curtain, which is not a pop-up but a window layer) | （清單欄 5 無對應寫法） | — |
| 7 | Cat. 2  and Cat. VR | `2` | 1110 |
| 8 | Cat. 2  and Cat. VR | `VR` | 15 |
| 9 | Cat. 3 | `3` | 73 |
| — | （未覆蓋） | `UNRESOLVED` | 69 |

**合計 1341 列 = PU 母體 1341 列**（相符）

-> features/display/data/popup_priority.tsv
-> popup_priority.tsv.meta.json
```

**合計 1341 列 = PU 母體 1341 列（相符）** —— 無遺漏、無重複計。
`PU0517` 與 `PU0130` 皆為 `1T` → rank **5**（`Cat. 1`）。

### 3.2 sidecar（R-DM30）

```json
{
 "data_file": "popup_priority.tsv",
 "columns": [
  "popup_id",
  "category_raw",
  "category_code",
  "priority_rank",
  "ladder_label",
  "note"
 ],
 "data_rows": 1341,
 "generated_by": "features/display/scripts/popup_priority.py",
 "generated_at": "2026-08-25",
 "inputs": [
  "Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf (reference: popup_priority_matrix)",
  "Pop Up List HMI R1 (26PI).xlsx (reference: popup_list)"
 ],
 "measurement_conditions": "序來源：矩陣 page 4 之 `Window Pop-up priorities (higher to lower)` 明序清單，逐字九列；對應來源：`Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁**欄 5（無表頭）**；popup 列之判準為欄 0 以 `PU` 起始；`1P`/`1T` 依矩陣 page 7 之逐字定義併入 `Cat. 1`；綁定檢查 entries: 13",
 "rulings": [
  "R-G36",
  "R-DM30",
  "R-G23",
  "R-G26",
  "R-G33"
 ],
 "notes": "**三項強制揭露（29 包 §三.2），缺一不得交付：**\n(1) **B17 —— `Cat. SL` 之位置未裁定**：矩陣 page 4 之明序清單置其於 `Cat. X` 之下；page 9 逐字稱其 `This category is maximum priority`；page 10 稱 `Cat. SL is stacked under RVC`。**三處說法不同。** 本表暫依 page 4 給 rank 3，並於該 26 列之 `note` 標 `PENDING: DR-DM2 Cat SL precedence`。凡涉 SL 之仲裁不得逕用本表。\n(2) **B18 —— 類別語意漂移未測**：本表之效力以「2021 SR24 1A 之類別定義於 26PI 仍適用」為前提。**該前提未經證明** —— 逐字比對只能證明六個類別 token 之詞彙未漂移，不能證明同一個 `1T` 在 2021 與 2026 指同一件事。\n(3) **B19 —— 69 列未覆蓋**，於表中標 `UNRESOLVED`，未省略。其值為 `---`／`RVC-X`／空／`2 SL`／`Custom`／`RVC\\n2`／`-`；**複合值須另定解析規則，本輪不定**。\n\n**本表之鍵為類別碼，非 popup id** —— 矩陣全篇 0 個 PU 編號。",
 "ladder_verbatim": [
  "Pop-up Categories (Priorities)",
  "Window Pop-up priorities (higher to lower):",
  "RVC",
  "Cat. X",
  "Cat. SL",
  "Anti-Theft  (Keypad and Anti-Theft pop-ups)",
  "Cat. 1",
  "Display off (black curtain, which is not a pop-up but a window layer)",
  "Cat. 2  and Cat. VR",
  "Cat. 3",
  "Activity Pop-up",
  "Activity pop-ups are all in the same category and can be overlaped by Window pop-ups.",
  "4"
 ]
}
```

### 3.3 三項強制揭露（§三.2，缺一不得交付）

| # | 缺口 | 落實之處 |
|---|---|---|
| **B17** | `Cat. SL` 位置三處不一致（p4 在 `Cat. X` 之下／p9 `is maximum priority`／p10 `stacked under RVC`） | sidecar `notes` (1) ＋ **表中 26 列 SL 之 `note` 欄逐列標 `PENDING: DR-DM2 Cat SL precedence`** |
| **B18** | 類別語意漂移未測 | sidecar `notes` (2)：本表效力以「2021 之類別定義於 26PI 仍適用」為前提，**該前提未經證明** |
| **B19** | 69 列未覆蓋 | sidecar `notes` (3) ＋ **表中該 69 列標 `UNRESOLVED`，未省略**，其 `note` 欄記「複合／無類別；解析規則未定」 |

**停止條件 77 未觸發。**

一項本層加寫者：sidecar 另存 `ladder_verbatim` 欄，
逐字保留矩陣 page 4 之九列明序清單 —— **序之來源與表分離即不可查**，
故隨表存放。

### 3.4 三項須具名之判斷

1. **`1P`／`1T` 併入 `Cat. 1`（rank 5）** —— 依矩陣 page 7 逐字
   （`1P (Phone). Incoming call pop-ups/metadata`／
   `1T (Temperature). Overheating related pop-ups (screen, system, speaker...)`）。
   **矩陣之明序清單只寫 `Cat. 1`，未區分 1P／1T 之先後**，故兩者同 rank。
2. **`Anti-Theft` 與 `Display off` 兩列無對應寫法** —— 清單欄 5 之值域
   不含此二者，故其 rank 存在而列數為 `—`。**不視為缺口**：
   矩陣之階梯本就包含非 popup 之層（`Display off` 逐字即
   `which is not a pop-up but a window layer`）。
3. **本表之鍵為類別碼，非 popup id** —— 矩陣全篇 0 個 PU 編號。
   `popup_id` 欄之存在是為了可用，其**權威來自類別欄之對應**，
   不是矩陣直接給了該 popup 之序。

---

## 四、DR-DM2 補充／DR-DM4 重擬／DR-DM12（全文）

三者皆已寫入 `DATA_REQUESTS.md`，**標「待 Pei 發」**。

### 4.1 DR-DM12（新開，HIGH，收件方同 DR-DM8）

> `SWE1-DM-007` 之 `static vehicle condition` 與 `SWE1-DM-008` 之
> `dynamic vehicle state transition`，**其區分軸為何**？三個候選：
> (i) 車輛靜止 vs 行進；(ii) 顯示器前態穩定 vs 過渡；(iii) 其他。
> **附本層現行切分之對照表**（007＝前態 `DCSD Screen ON`、釋放後還原回 ON，
> `{4819642}`／`{4819645}`；008＝前態非 ON 或過渡畫面、釋放後目的態不同，
> `{4819668}`／`{4819671}`／`{4820265}`），請確認或更正。
> 實測依據：CFTS_020 全文 `static` **0 命中**、`dynamic` **1 命中**；
> SYS2 之 12 列 RVC **同時錨到兩個 leaf 且錨據完全相同**。

### 4.2 DR-DM2 之補充函（§3.3 全文已入檔）

兩問：(a) `Cat. SL` 之優先位置三處說法不同，請裁定；
(b) 2021 SR24 1A 矩陣對 26PI 是否仍為權威（附「詞彙未漂移、
語意無從以逐字證明」之佐證）。

並記 **本 DR 之狀態自此由「索件」降為「確認」**。

### 4.3 DR-DM4 之重擬（§3.4 全文已入檔）

標的改為 §1.5.1／§1.5.3 是否即 `{CFTS013-629}`／`{-633}`／`{-952}`，
附 7 位 vs 3 位之實測，並**追加本輪 A3 之結果**：

> §1.5.3 之 13 條全部適用本專案，其門檻為 50／51–55／56–<60 degrees C，
> 與 CFTS_020 `{4820289}` 之 85 degrees C 不符。**本層未併算、未判何者為準。**

---

## 五、`BACKLOG.md` 之兩個重審節

### 5.1 新增「DR-DM12 回覆後重審（007／008 之切分軸）」

四列：`rvc-01` 六條之 `leaf_id`（全批重審）、`batch_context.md` §二之
切分表、各交付面之標明（R-DM55 之拘束）、`framework.md` 第四組
（若區分軸為車速，Test Set 分組理由須複核）。

節首逐字記 R-DM55 之「**錯誤可逆 —— 受影響者僅 `leaf_id` 一欄，
TC 內容不受影響**」。

### 5.2 既有「DR-DM10 回覆後重審」

**未動**，惟其首列（#4 之 ER 3 之論據須重估）**於本輪已被觸發** ——
第三種讀法出現（§2.7）。列於 §七 A 類。

### 5.3 A 類 A1 之更新

由「未做；DR-DM2 OPEN」改為「**已建**（1341 列：1272 已解析／
69 `UNRESOLVED`）—— DM2 自『索件阻斷』降為『確認』。
**惟帶三項強制揭露，凡涉 `Cat. SL` 之仲裁不得逕用**」。

---

## 六、步驟 6（D1／D2／D3）—— **28a 輪已執行，本輪複核**

下放包 29 §五.6 記「上繳 28 未見其產出」。**實為時序差**：
28a 之三步已於其本輪執行並 commit（`73ac307`，2026-08-26），
其產出併入上繳 28 之 **§三之二**（該節於 28a 執行時才追加，
29 包成稿時所見之上繳 28 尚無此節）。

本輪複核其仍在，未重做：

| 項 | 現況（實測） |
|---|---|
| D1 十筆 `SENT (2026-08-25)` | `DATA_REQUESTS.md` 實測 **10 筆** SENT；`DR-DM11` 仍 OPEN；**本輪新開 DR-DM12 為「待 Pei 發」** |
| D2 A-DM36 結案 | 標題實測為 `[CLOSED]`，結案註記在；B14 以 `B7` 續列於 BACKLOG |
| D3 DR-DM7 對帳 | 四項資料與判定在上繳 28 §D3；**判定為全案結案而非部分結案**，停止條件 78 未觸發 |

**A11（R-DM44 之台帳動作十二輪未執行）仍為 A 類**，本輪未處置
（其處置屬分析層）。

---

## 七、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A／組 B 何者為準 —— **本輪出現第三種讀法**（CFTS_013 §1.5.3 之 50 vs CFTS_020 之 85） | 004／005 全部門檻；**`pilot-01` 三條之 `85 degrees C`** | DR-DM10(a)（**建議併入第三種讀法**） |
| A2 | DCSD 側 warning → off | 原 pilot #2 | DR-DM10(b)（**答案形狀已現，未據以行動**） |
| A3 | 長拼法標籤與 HU 側值 | `{4820287}`；`rvc-01` 之 HU 側 | DR-DM9 |
| A4 | `popup_priority.tsv` 之 `Cat. SL` 位置 | 凡涉 SL 之仲裁 | DR-DM2(a)（**表已建，SL 標 PENDING**） |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| A9 | 倒車檔訊號 | 007 之觸發面向 | DR-DM11 |
| A10 | DR-DM4 之標的 | DR-DM4 之答覆 | **本輪已重擬，待 Pei 發** |
| A11 | R-DM44 之台帳動作十二輪未執行 | DR-DM7 之真實狀態 | 待分析層裁定 |
| **A12** | **007／008 之區分軸** | `rvc-01` 六條之 `leaf_id`（**非 TC 內容**） | **DR-DM12（新）** |

A12 為本輪新增。**A1 之份量本輪大幅增加** —— 它現在直接壓在
`pilot-01` 三條已寫好的 `85 degrees C` 上。

### B 類

| 編號 | 項 | 狀態 |
|---|---|---|
| B1–B16 | 見上繳 25–27 | 不變 |
| B17 | `Cat. SL` 三處不一致 | **已升為 A4 之索取內容**；表中 26 列標 PENDING |
| B18 | 類別語意漂移未測 | 不變，已入 sidecar |
| B19 | 69 列複合／無類別 | 不變，表中標 `UNRESOLVED` |
| B20 | CFTS_013 §1.5.1 未讀 | **本輪解除**（A3 續行） |
| B21 | BACKLOG 之 B 編號與分流編號兩套 | 已更正（`B6`／`B7`） |
| **B22** | **CFTS_013 §1.5.2（Standard，11 條）未抽其內容** | 實測 0 條適用本專案，故未抽。**若 DR-DM10(a) 裁定「本專案走 Standard」，須回頭抽** |
| **B23** | **`{4821589}`／`{4821590}`／`{4821591}`／`{4821587}`／`{4821592}` 未追** | `{4943104}` 等所轉指之條號，其內容為 warning → off 之訊號序列。**本輪停手範圍內，未追** |

B22／B23 為本輪新增。

---

## 八、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/RULINGS.md \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/scripts/popup_priority.py \
  features/display/data/popup_priority.tsv \
  features/display/data/popup_priority.tsv.meta.json \
  features/display/docs/handoff/29_a3_and_arbitration.md \
  features/display/docs/upstream/29_a3_and_arbitration.md
```

```text
feat(display): read the CFTS_013 algorithm, and find it disagrees with 85 degrees

- extract sections 1.5 to 1.5.3 by heading, since the three-digit clause
  numbers DR-DM4 asks for do not exist in that document
- all thirteen multi-stage clauses apply to this project, and they stage by
  temperature at 50, 51 to 55 and 56 to below 60 degrees, where CFTS_020
  states a single threshold of 85 for the same transition of the same
  display, so no test case was touched and the conflict is reported
- record A-DM40: the applicability predicate required the architecture to be
  named, and this document writes All, so thirteen applicable clauses were
  first read as none
- verify that the SYSRA workbook says HU throughout, which is what R-DM51
  rests on, while the specification body says DCSD for the same numbers
- build popup_priority.tsv keyed by category, covering all 1341 pop-ups with
  69 left unresolved and every Cat. SL row marked pending
- add R-DM55 and open DR-DM12: nothing in the material distinguishes static
  from dynamic, so the split is a classification and only leaf_id is at risk
- reword DR-DM4 and add the supplement to DR-DM2
```

> `generated/pilot-01.json`／`generated/rvc-01.json` **一字未動**
> （停止條件 76），不入。`batches/` 由 `.gitignore` 排除。
> 036 母本未變更，亦不入。

---

## 九、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **A-DM40 是本輪最該記住的一件事，而它不是被機器抓到的。**
   一個用了兩輪都正確的判準，換一份文件就編碼了錯誤的假設
   （「架構欄一定逐一列舉」）。**抓到它的是「一份被 CFTS_020 轉指五次的
   文件不可能完全不適用」這個不合理感。** 若當時我沒有那個感覺，
   本輪會以「CFTS_013 對本專案完全不適用」結案 ——
   **而那個結論會讓 DR-DM4 被錯誤地關掉。**

2. **我補驗了 SYSRA 的主詞，但沒有補驗 24 包對 SYSRA 之其餘量測。**
   §2.9 只查了「五列門檻之主詞是 HU」這一項。24 包還斷言了
   `{CFTS013-930}` 定義 Associated／Disassociated 之區分（R-DM51 之
   立條依據）—— **那一條我仍未自行讀過**。

3. **`{4821589}` 等五個轉指條號我沒追**（B23）。
   它們正是 warning → off 之訊號序列，**也就是 pilot-01 原 #2 被
   deferred 的那個東西**。本輪停手範圍內未追是對的，
   **但它們現在是已知位置、可取得、且直接對應一個開了四輪的 DR。**
