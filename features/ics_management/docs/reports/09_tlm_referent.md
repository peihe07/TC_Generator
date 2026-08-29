# 下放包 09 作業 A —— `TLM` 於 CFTS020 之指涉量測

> 量測腳本：`features/ics_management/scripts/tlm_probe_09.py`（新開檔；
> 未改 `cfts020_probe.py`，僅以 `importlib` 唯讀載入其 `parse()`）。
> 本檔依 R-ICS33(b)／下放包 09 之紀律：**只列不裁**。
> 未改任何 TC JSON、未改任何 `specification_reference`、未對 DR-ICS13／DR-ICS18 作結案。
>
> **成因**：R-ICS35(b) 之判準以「TLM 非本 DUT」為前提，該前提從未經量測（A-ICS56）。
> **問題**：CFTS020 §1.18 所稱之 `TLM`，是否即本 DUT（即 §1.8 所稱之 `HU`）？

---

## §0 掃描條件

### §0-1 抽取法

| 文件 | 路徑 | 抽取法 |
|---|---|---|
| CFTS020 | `inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `importlib` 載入 `scripts/cfts020_probe.py` 之 `parse()`（逐物件結構，母數 **2180**）；行層級掃描另用其 `doc_lines()` |
| CFTS022 | `inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 Functional Specification_20260608-1205.docx` | 本腳本自解，同一法：`word/document.xml`、`</w:p>`→換行、`</w:tc>`→tab、去 XML 標籤、`html.unescape` |
| SYSAD | `inputs/SYS3_CFTS020_ICS_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | 同上（本輪臨時查核，非腳本常設項；逐字見 §3-3、§6） |

物件屬性頭、章節行、軸值之切法一律沿 `cfts020_probe.py` 檔頭所揭（未改動）。
適用性判定沿 **R-ICS2 v2(b)**。

### §0-2 詞界處理（**區分大小寫**）

```
TLM ：(?<![A-Za-z0-9_])TLM(?![A-Za-z0-9_])
HU  ：(?<![A-Za-z0-9_])HU(?![A-Za-z0-9_])
ICS ：(?<![A-Za-z0-9_])ICS(?![A-Za-z0-9_])
```

- 皆為 `re` 之預設**區分大小寫**比對（未加 `re.I`），故 `tlm`／`hu` 不計。
- 前後皆以 `[A-Za-z0-9_]` 之負向斷言封界，因此：
  - `HTML` **不會**被 `TLM` 抓到（`HTML` 中根本無 `TLM` 子字串；此為交辦所慮之案，實測確認無此風險）；
  - `LTM`／`ETM`／`RRM` 為**字面不同之詞**，本正則不抓（非「濾掉」，是根本不匹配）；
  - `TLM_ADspl`、`LTM_DDspl` 等帶底線之複合詞**被封界排除**；
  - `HU` 側排除 `HUD`、`HU_Video`、`_HU`、`Personal_HU` 等。
- **詞界之實效已量**（同一素材、有／無詞界二次掃描對照）：
  - `TLM`：帶詞界 47 次 ／ 無詞界 47 次 → 詞界濾掉 **0** 次（本詞在本文件無複合形）；
  - `HU`：帶詞界 1741 次 ／ 無詞界 1802 次 → 詞界濾掉 **61** 次。
  61 次之濾除證明詞界確實在作用，非空轉。
- **連字號**（`R1L-R` 之 `-`）不在 `[A-Za-z0-9_]` 內，故不影響本二詞之封界。

### §0-3 「出現」之計數單位

- **物件本文層級**（`parse()` 之 `text`）：用於 §1～§3、§5 之全部逐物件統計。
- **行層級**（`doc_lines()`）：另作對照，涵蓋章節標題、目次（`PAGEREF`）、表格 —— 用於補抓不落在物件本文內之逐字（如章節標題「TLM algorithm requirements」）。二者分列，不混計。

---

## §1 量測項 1 —— 全文出現面

### §1-1 `TLM` 之出現次數與章節分佈（物件本文層級）

| 項 | 實數 |
|---|---|
| 帶詞界命中總次數 | **47** |
| 帶詞界命中之物件數 | **20** |
| 無詞界（寬鬆）命中總次數 | 47（差 0） |

| 頂層節 | 次數 | 物件數 |
|---|---|---|
| §1.18 | 47 | 20 |

**`TLM` 於 CFTS020 全 2180 物件中，只出現於 §1.18，別無他處。**

行層級對照：`TLM` 命中 **22 行**，其中 1 行為目次（`1.18.1.2 TLM algorithm requirements {4821699} PAGEREF …`）、1 行為正文章節標題（同名）、其餘 20 行即上表之 20 個物件本文。

### §1-2 `HU` 之出現次數與章節分佈（物件本文層級）

| 項 | 實數 |
|---|---|
| 帶詞界命中總次數 | **1741** |
| 帶詞界命中之物件數 | **940** |
| 無詞界（寬鬆）命中總次數 | 1802（詞界濾掉 61） |

| 頂層節 | 次數 | 物件數 |
|---|---|---|
| §1.2 | 9 | 2 |
| §1.3 | 1 | 1 |
| §1.4 | 45 | 40 |
| §1.5 | 144 | 81 |
| §1.6 | 6 | 3 |
| §1.7 | 7 | 4 |
| §1.8 | 376 | 210 |
| §1.9 | 10 | 5 |
| §1.10 | 7 | 4 |
| §1.11 | 178 | 90 |
| §1.12 | 6 | 3 |
| §1.13 | 4 | 2 |
| §1.14 | 60 | 42 |
| §1.15 | 884 | 451 |
| §1.16 | 4 | 2 |

**`HU` 出現於 §1.2～§1.16 共 15 個頂層節，而 §1.17、§1.18 為 0。**

### §1-3 二者是否曾於同一物件內出現且指涉不同實體

| 量測 | 實數 |
|---|---|
| 同一物件內 `TLM` 與 `HU` **併現**（帶詞界） | **0 個** |
| 同一物件內 `TLM` 與 `HU` 併現（**無詞界**，對照） | **0 個**（差 0） |

**查無**。全文 2180 物件中，`TLM` 與 `HU` **從未於同一物件內併現**。
故交辦所指「最強之區辨證據」——「二者於同一物件內指涉不同實體」——**實測不存在**。

實測所得之分佈形態為**互補分佈（complementary distribution）**：
`TLM` 只在 §1.18，`HU` 只在 §1.18 以外。二詞在本文件中**沒有任何一處需要同時區別**。

補充（反向，見 §5）：`TLM` 於 §1.8 之物件本文命中 **0**；`HU` 於 §1.18 之物件本文命中 **0**。

---

## §2 量測項 2 —— 職能對位

### §2-1 母數

| 側 | 範圍 | 物件數 | 主詞判為該名者 |
|---|---|---|---|
| §1.8 HU 側 | §1.8.1.1（Push Button Data Transfer）＋§1.8.1.2（Rotary Knob Data Transfer）含子樹 | 40 | 主詞＝`HU` 者 **20** |
| §1.18 TLM 側 | §1.18.1.2（`TLM algorithm requirements` {4821699}） | 17 | 主詞＝`TLM` 者 **17（100%）** |

「主詞」之判法（**已揭露，非語意判讀**）：取本文中 `TLM`／`HU`／`ICS` 三詞界正則**最先出現位置**者為主詞。此為機械規則，不作語法剖析；其局限見 §6-3。

### §2-2 同職能配對表

| 職能 | 判定條件（正則） | §1.8 HU 側物件 | §1.18.1.2 TLM 側物件 | 配對 |
|---|---|---|---|---|
| 按鍵訊號之接收／處理 | `[Bb]utton` | 4819544, 4819553, 4819554, 4819555, 4819557, 4819558, 4819559, 4819566, 4819567 | 4821704, 4821705, 4821706, 4821708, 4821709, 4821710, 4821711, 4821712, 4821713, 4821714, 4821715, 4821716 | **同職能、不同主詞名** |
| 旋鈕訊號之接收／處理 | `[Kk]nob\|KNOB` | 4819579, 4819585, 4819586 | 4821701, 4821702, 4821703 | **同職能、不同主詞名** |
| 畫面／HMI 之決定或管理 | `screen\|Screen\|HMI` | 4819554, 4819555, 4819558, 4819560, 4819561, 4819563, 4819567, 4819568, 4819572, 4819575, 4819576, 4819586 | 4821702, 4821704, 4821705, 4821706, 4821707, 4821709, 4821713, 4821716 | **同職能、不同主詞名** |
| browsing list 之管理 | `browsing` | 無 | 4821702, 4821704 | **僅一側（TLM 獨有）** |
| 音量輸出 | `[Vv]olume` | 4819553, 4819558, 4819559, 4819585 | 4821701, 4821709 | **同職能、不同主詞名** |
| Mute | `Mute\|mute` | 4819553, 4819558 | 4821709 | **同職能、不同主詞名** |
| `"Screen Off"` 模式 | `"Screen Off"\|Screen Off\|Screen On` | 4819558 | 4821705, 4821706, 4821707 | **同職能、不同主詞名** |

**配對數 6；未配對數 1。**

### §2-3 逐字對照（同一觸發、同一行為、同一外部引用，二節主詞名不同）

**Mute／音量**

- §1.8 `4819553`（適用）逐字：
  `When the HU receives $ICSMuteButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.`
- §1.18 `4821709`（適用）逐字：
  `TLM shall adjust the volume of the audio output according to signal $ICSMuteButton$.In particular, TLM shall set Mute.Req signal to the same value as $ICSMuteButton$.TLM has to use this signal for internal audio purposes. See TLM {CFTS019} and HMI Logic and Flow for Mute behavior.`

同一觸發訊號 `$ICSMuteButton$`、同一行為（音量／靜音）、**同一外部引用 `{CFTS019}`**。
§1.8 稱之為 `the HU`、其內部訊號為 `internal HU signal`；§1.18 稱之為 `TLM`、其 CFTS019 為 `TLM {CFTS019}`。

**旋鈕音量**

- §1.8 `4819585`（適用）逐字：
  `When the HU receives the $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$ signals it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Inf…`
- §1.18 `4821701`（適用）逐字：
  `TLM shall adjust the volume of the audio output according to signals $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$ signals.In particular, TLM shall set Volume_Knob_Val.Info and Volume_Knob_Dir.Info signals to the same values of $ICS_KNOB1_VAL$ and $ICS_KNOB1_DIR$ respectively.TLM has to use these signals for internal audio purposes.`

**ICS 側之送出句（同一句型，收件人名不同）**

- §1.8 `4819543`（適用）：`The ICS will send signals on the BH-CAN to communicate the status of the mechanical push buttons.`（未點名收件人）
- §1.18 `4821683`（適用）：`The ICS shall send signals on the BH-CAN to communicate the status of the mechanical push buttons **to TLM**.`

§1.18 明文把 ICS 之按鍵訊號的**收件人**指為 `TLM`。§1.8 之同一句不點名，但其下游接收句主詞為 `HU`（`4819553` 等）。

**§1.18 之另一句（ICS 側，逐字）**

- `4821679` 所在子樹：`Many of TLM commands are present on ICS node.`
- `Following requirements for ICS and TLM are valid for the Ignition Working Conditions:- Ignition Off- Ignition On- …`

§1.18 全節之行為方僅二：`ICS` 與 `TLM`。

---

## §3 量測項 3 —— 主機專屬職能之持有

掃描面：CFTS020 全文中含詞界 `TLM` 之 **20 個物件**。

| 主機專屬職能 | 判定正則 | 命中物件數 |
|---|---|---|
| 畫面（screen） | `screen`（`re.I`） | **7** |
| `"Screen Off"` 模式 | `Screen Off` | **3** |
| browsing lists | `browsing`（`re.I`） | **2** |
| 音量輸出（volume） | `volume`（`re.I`） | **2** |
| HMI | `HMI` | **4** |
| audio／media 來源 | `audio\|media\|source`（`re.I`） | **2** |

### §3-1 逐字證據（交辦所列三處已複驗，並補全）

交辦起點三處，**逐字複驗結果**：

| 交辦所指 | 複驗 | 逐字 |
|---|---|---|
| `4821704` | **相符** | `Depending on what TLM is currently showing on its screen, TLM shall manage its screens and/or browsing lists according to $Enter_Button$ and $Back_Button$ signals.See TLM CFTS and TLM HMI for details.` |
| `4821705` | **相符** | `IF TLM is in "Screen Off" modality AND it receives $ICSScreenOffButton$ passing from "Not_Pressed" to "Pressed", TLM has to set Screen On internal modality.` |
| `4821706` | **相符** | `IF TLM is in "Screen On" modality AND it receives $ICSScreenOffButton$ passing from "Not_Pressed" to "Pressed", TLM has to set Screen Off internal modality.` |
| `4821701` | **相符** | `TLM shall adjust the volume of the audio output according to signals $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$ signals.In particular, TLM shall set Volume_Knob_Val.Info and Volume_Knob_Dir.Info signals to the same values of $ICS_KNOB1_VAL$ and $ICS_KNOB1_DIR$ respectively.TLM has to use these signals for internal audio purposes.` |
| `4821709` | **相符** | `TLM shall adjust the volume of the audio output according to signal $ICSMuteButton$.In particular, TLM shall set Mute.Req signal to the same value as $ICSMuteButton$.TLM has to use this signal for internal audio purposes. See TLM {CFTS019} and HMI Logic and Flow for Mute behavior.` |

### §3-2 補全（交辦未列、本輪實測新增之逐字）

| ObjectID | 判定 | 逐字 |
|---|---|---|
| `4821702` | 適用 | `Depending on what TLM is currently showing on its screen, TLM shall manage its screens and browsing lists according to $ICS_KNOB2_DIR$  and $ICS_KNOB2_VAL$  signals.See TLM CFTS and TLM HMI for details.` |
| `4821707` | 適用 | `See TLM HMI for details on Screen On and Screen Off modalities.` |
| `4821708` | 適用 | `Refer to par. "TLM Operative States management" for details on how TLM has to behave according to $ICSPowerButton$ signal.` |
| `4821700` | 適用 | `TLM shall acquire CLIMATIC_PANEL message and activate/deactivate internal functionalities depending on the values of the signals received.` |
| `4821703` | 適用 | `Every time TLM receives $ICS_KNOB<n>_DIR$ equal to "Knob_no_change", TLM has to ignore the value of $ICS_KNOB<n>_VAL$.` |
| `4821710` | 適用 | `TLM has to set signal Front_Panel_OnOff.Info to the same value of signal $ICSPowerButton$.` |
| `4821711`／`4821712` | 不適用 | `IF the TLM has detected that the $ICSLeftTemperatureUpButton$ and $ICSLeftTemperatureDownButton$ are in the pressed state for 5 seconds, and the TLM is (not) in Engineering Mode, the TLM shall enter/exit Engineering Mode.  For Engineering Mode behavior, refer to {CFTS011}.` |
| `4821713`／`4821716` | 不適用 | `… the TLM shall perform a **screen capture**.  For Engineering／Dealer Mode behavior, refer to {CFTS011}／{CFTS012}.` |
| `4821714`／`4821715` | 不適用 | `… the TLM shall enter/exit Dealer Mode.  For Dealer Mode behavior, refer to {CFTS012}.` |

**答（量測項 3）**：`TLM` **確實持有**畫面（`showing on its screen`、`manage its screens`）、`"Screen Off"`／`"Screen On"` internal modality、browsing lists、音量輸出（`adjust the volume of the audio output`）、HMI（`TLM HMI`）、Engineering／Dealer Mode 與 screen capture。
**全部為主機（Head Unit）職能，且與 §1.8 之 `HU` 側職能逐項對位（§2-2 之 6 個配對）。**

### §3-3 SYSAD（本 DUT 自身之系統架構文件）之逐字 —— **本輪新增之關鍵面**

`inputs/SYS3_CFTS020_ICS_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`，
帶詞界 `TLM` 命中 **29 行**；帶詞界 `LTM` 命中 **0 行**。逐字節錄：

1. **縮寫表**（逐字，二行相鄰）：
   ```
   TLM
   Telematics Module
   ```
2. **Table 6 — System Decomposition Table**（逐字，欄位依序）：
   ```
   SYSAD-TLM
   Telematics ECU
   Partial
   Sets Volume_Knob_Val.Info and Mute.Req
   reuse ECU add ICS handling
   ```
   同表之其餘列為 `SYSAD-HMI`／`SYSAD-ICSAPP`／`SYSAD-ICSCLIENTSERVICE`／
   `SYSAD-AUDIOMANAGERSERVICE`／`SYSAD-CPM`／`SYSAD-CARSERVICE`／
   `SYSAD-VHAL`（`Vehicle Hardware Abstraction Layer`）／`SYSAD-VCPU`（`Vehicle CPU`）。
3. **Table 11.9 — Architectural Design Components table for SYSAD-TLM**（逐字）：
   ```
   SYSAD_ID            SYSAD-TLM
   Component Version   v1.0
   Component Function  Applies Volume_Knob_Val.Info and Mute.Req
   Component Vendor    ECU Supplier
   Reuse Percentage    50%
   Reuse Reference     R1L
   ```
4. **資料流逐字**：
   ```
   Volume flow is defined as: ICS_KNOB1_VAL → VCPU → VHAL → CarService → CPM → AudioManagerService → HMI / TLM
   SYSAD-AUDIOMANAGERSERVICE generates ICS_Volume_Adjustment.Info (volume control signal).SYSAD-TLM sets Volume_Knob_Val.Info and Volume_Knob_Dir.Info
   At ECU Layer, SYSAD-TLM reads ICS_KNOB1_VAL and ICSMuteButton from CAN (audio input) and sets Volume_Knob_Val.Info and Mute.Req (audio output control). SYSAD-TLM reads ICSPowerButton and sets Front_Panel_OnOff.Info (panel state control).
   ```

**併陳之事實**：`ICS_Volume_Adjustment.Info` 於 CFTS020 §1.8 `4819553`／`4819585` 逐字被稱為
`the internal HU signal named ICS_Volume_Adjustment.Info`。
本 DUT 之 SYSAD 讓 `SYSAD-AUDIOMANAGERSERVICE` 產生該 **internal HU signal**，並直接交給 `SYSAD-TLM` 執行。
亦即：**本 DUT 之架構把「HU 之內部訊號」餵給 TLM** —— 二者位於同一 ECU 邊界之內。

---

## §4 量測項 4 —— ECU 屬性面

### §4-1 CFTS020 之 `ECU` 值域（實測，值：帶該值之物件數）

| ECU 值 | 物件數 |
|---|---|
| FPDM | 86 |
| CCDMF | 47 |
| **LTM** | **29** |
| **ETM** | **28** |
| CCDMR | 27 |
| VRM | 24 |
| TMM | 21 |
| DTV | 15 |
| ALL | 9 |
| CVPM | 9 |
| CVPAM | 6 |
| DCSD | 4 |

**`TLM` 於 CFTS020 之 `ECU` 值域：查無（0）。**
（附帶實測：`ICS` 亦不在 CFTS020 之 ECU 值域內 —— 此為 R-ICS2 v2(b) 之實況依據。）

### §4-2 CFTS022 之 `ECU` 值域（物件母數 336）

| ECU 值 | 物件數 |
|---|---|
| ETM | 295 |
| **LTM** | **244** |
| **RRM** | **95** |
| FPDM | 18 |
| DVD | 12 |
| ICS | 11 |
| TBM | 11 |
| TBM2 | 11 |
| AMP | 6 |
| CDM | 5 |
| ALL | 3 |
| CCDMR | 2 |
| CCDMF | 2 |
| SCCM | 1 |
| VES2 | 1 |
| VES3 | 1 |

**`TLM` 於 CFTS022 之 `ECU` 值域：查無（0）。**
**`TLM` 於 CFTS022 全文（含目次與表格）之詞界命中：0 次。**
同一文件之 `HU` 詞界命中：**340 次**。

> 即：CFTS022（ECU 軸含 `LTM`／`ETM`／`RRM` 之跨 ECU 文件）**全篇不用 `TLM` 一詞，只用 `HU`**。

### §4-3 `LTM`／`ETM`／`RRM` 與 `TLM` 之字面關係

- **`TLM` 不是 ECU 軸之枚舉值**（§4-1／§4-2 皆查無），而是**散文中之角色名**。
- `LTM`／`ETM`／`RRM` 是 ECU 軸之枚舉值。
- 逐字證據（CFTS020 `4819134`，§1.2 Introduction，`[ECU:ALL] [Radio:…]`）：
  > `Note: There are essentially 2 variants of the LTM and ETM Radio HUs; those with the touch screen integrated into the HU module are known as Associated variants while those HUs that interface to an external touch screen module (DCSD) are known as Disassociated variants (and are also referenced as a 'Silver Box' variants).  In order to distinguish between these two types of HUs we are using a '_ADspl' suffix on the Associated variants and '_DDspl' suffix on the Disassociated variants.`
- 逐字證據（CFTS020 `4819129`，§1.2）：
  > `This CFTS chapter discusses requirements for variants of the ICS and the DCSD modules that interact with the various LTM_ADspl, ETM_ADspl, LTM_DDspl andETM_DDspl Radio HUs and optional CVPM, CVPAM, DTV, VRM and TMM components when present.`
- 逐字證據（SYSAD 縮寫表）：`TLM` = `Telematics Module`。

**併陳 A-ICS47**：A-ICS47 實測「87 個單一-ECU 物件中 LTM 專屬 28 個全帶 R1L／R1L-R、ETM 專屬 59 個全帶 R1M／R1H，違例 0 → 本 DUT（R1L-R）之 ECU 為 **LTM**」。

**字面關係之結論（事實陳述）**：
`LTM`／`ETM` 為「**Radio HU**」之二個型號（CFTS020-4819134 逐字），而 `TLM` = `Telematics Module`（SYSAD 縮寫表逐字）。
`LTM` 與 `ETM` 是 Telematics Module 之**具體型號**（軸級枚舉值），`TLM` 是其**類名**（散文級角色名）。
本 DUT 之 ECU 為 `LTM` → 本 DUT **是一台 Telematics Module**。
`RRM` 同列於 CFTS022 之 ECU 值域，但**未於本輪任一逐字中與 `TLM` 建立字面關係**（查無）。

### §4-4 `TLM` 所設訊號於二綁定 DBC 之查核（補測）

`Volume_Knob_Val.Info`／`Volume_Knob_Dir.Info`／`Mute.Req`／`Front_Panel_OnOff.Info`
於 `PDT27_E2A_R4_BHCAN.dbc` 與 `PDT27_E2A_R5_FDCAN8.dbc` 之 `SG_` 定義：**查無（0）**。
掃法：`LC_ALL=C grep -ain "Front_Panel\|Volume_Knob\|Mute"` 二檔全文。
（二檔僅有 `DCSD_Mute`、`AMP_MUTEDSts`、`MuteSts` 三個字面不同之訊號。）
故**無法**以 DBC 發送節點反推 `TLM` 之 ECU 身分 —— 該路徑在現有素材上無對應物（與 A-ICS47 之 `$TGW_DISP_STAT$` 同型之空缺）。此為**查無**，不作推定。

---

## §5 量測項 5 —— 反向查核

| 量測 | 實數 |
|---|---|
| §1.18 物件總數 | **37**（適用 29） |
| §1.18 中含詞界 `HU` 之物件 | **0** |
| §1.18 中主詞為 `HU` 之物件 | **0** |
| （反向）§1.8 中含詞界 `TLM` 之物件 | **0** |

**§1.18 節內部無任何以 `HU` 為主詞之物件，故「`TLM ≠ HU` 於該節內部即成立」之提前收斂路徑 —— 實測不成立。**
量測**不能**由此提前收斂；必須依 §1～§4 之證據判。

### §5-1 章節標題面（行層級補測，非物件本文）

CFTS020 頂層章節標題逐字（至二層，實測）：

| 節 | 標題逐字 |
|---|---|
| 1.5／1.6／1.7 | `Functional Requirements／Diagnosis and recovery／Function properties - PNet - ICS and Associated HU` |
| **1.8** | `Functional Requirements - PNet & AtlHi & AtlMi- ICS, Silver Box HU, DCSD, FPDM, CCDMF, and CCDMR` |
| 1.11 | `Functional Requirements - PNet & AtlHi - VP5R120 Silver Box HU and DCSD120_wICS_Port` |
| 1.14／1.16／1.17 | `… - CUSW - ICS and Associated HU` |
| 1.15 | `Functional Requirements - CUSW and Disassociated HU` |
| **1.18** | `Functional Requirements - AtlMi & AtlHi & AtlLo - ICS and Associated HU` |

§1.18 之子節標題逐字：

```
1.18   Functional Requirements - AtlMi & AtlHi & AtlLo - ICS and Associated HU {4821673}
1.18.1     ICS Management {4821674}
1.18.1.1     ICS algorithm requirements {4821677}
1.18.1.1.1     ICS Logistic Mode ON {4821678}
1.18.1.1.2     Push Button Data Transfer {4821680}
1.18.1.1.3     Rotary Knob Data Transfer {4821690}
1.18.1.2     TLM algorithm requirements {4821699}
```

**§1.18 之標題只點名二個行為方：`ICS` 與 `Associated HU`。而其二個 algorithm 子節為 `ICS algorithm requirements` 與 `TLM algorithm requirements`。**
即：在 §1.18 之標題結構中，**`TLM` 佔的正是 `Associated HU` 的位置**。

### §5-2 §1.18 之 Radio 軸分佈（補測，供分析層參考）

| Radio 值 | 物件數 |
|---|---|
| **allSys** | **29** |
| R1M／R1H／VP2R5／VP2R7／VP2R84／VP4R7／VP4R84 | 各 7 |
| R1L | 1 |
| R1L-R | 1 |
| noSys | 1 |

§1.18 判適用之 29 個物件，其 Radio 軸命中全部經由 **`allSys`**（非經 `R1L`／`R1L-R` 之點名）。
對照 §1.8.1：`R1L-R` 明列於 **58** 個物件、`R1L` 58 個。
（此項為事實陳述，非裁；其對 R-ICS35(c)「敘述較具體者」之意義屬分析層。）

### §5-3 §1.18 是否提及 DCSD

§1.18 全 37 物件中含 `DCSD` 者：**0**。（與 §5-1 之標題「Associated HU」一致 —— Associated 變體即畫面整合於 HU、不外接 DCSD。）

### §5-4 外部 CFTS 引用之對稱性（用以檢驗「TLM 有自己的 CFTS ⇒ TLM 是外部件」之推論）

| 量測 | 實數 |
|---|---|
| §1.8 中「本文含詞界 `HU` 且引用 `{CFTSxxx}`」之物件 | **24** |
| §1.18 中引用 `{CFTSxxx}` 之物件 | **7** |

即：CFTS020 對 `HU` 之行為同樣大量外引其他 CFTS 章（`{CFTS019}`、`{CFTS009}`、`{CFTS010}` 等，24 處）。
故「§1.18 說 `See TLM CFTS and TLM HMI for details`／`See TLM {CFTS019}`」**不構成 `TLM` 為外部件之區辨證據** —— 該文件對本 DUT 之 `HU` 用的是同一種外引法，且**外引的是同一份 `{CFTS019}`**（§2-3 逐字）。

---

## §6 結論

## 【`TLM` = DUT】

**理由（依證據強度排序，全部為 §1～§5 之實測）**：

1. **定義面（最強）**。SYSAD 縮寫表逐字：`TLM` = `Telematics Module`。
   CFTS020 `4819134` 逐字：`LTM` 與 `ETM` 是 `Radio HUs` 之二個變體型號。
   A-ICS47 實測：本 DUT（R1L-R）之 ECU 為 `LTM`。
   → 本 DUT 是一台 Telematics Module；`TLM` 是 Telematics Module 之類名。

2. **本 DUT 自身架構文件之直證**（§3-3）。`SYS3_CFTS020_ICS … SYSAD_v1.0.docx` 之
   **System Decomposition Table** 把 `SYSAD-TLM`（`Telematics ECU`，`Reuse Reference: R1L`）列為
   **本系統之分解組件**，與 `SYSAD-HMI`／`SYSAD-VHAL`／`SYSAD-CarService`／`SYSAD-VCPU` 同表；
   其職責逐字為 `Sets Volume_Knob_Val.Info and Mute.Req` —— 即 CFTS020 `4821701`／`4821709` 之要求。
   且該架構把 CFTS020 §1.8 明文稱為 **`the internal HU signal named ICS_Volume_Adjustment.Info`** 的訊號
   餵給 `SYSAD-TLM`。**「HU 之內部訊號」流向 TLM ⇒ 二者在同一 ECU 邊界之內。**

3. **逐字對位之三重同一**（§2-3）。`4819553`（HU）與 `4821709`（TLM）：
   **同一觸發訊號** `$ICSMuteButton$`、**同一行為**（音量／靜音）、**同一外部引用** `{CFTS019}`。
   §1.8 稱 `the HU`、`internal HU signal`；§1.18 稱 `TLM`、`TLM {CFTS019}`。
   旋鈕側 `4819585` 與 `4821701` 同型。

4. **章節結構之槽位對應**（§5-1）。§1.18 標題只點名 `ICS and Associated HU` 二方；
   其二個 algorithm 子節為 `ICS algorithm requirements` 與 `TLM algorithm requirements`。
   **`TLM` 佔的就是 `Associated HU` 的槽位。** §1.18 提及 DCSD 者 0（§5-3），與 Associated 變體相符。

5. **主機專屬職能之完整持有**（§3）。畫面 7、`"Screen Off"` 模式 3、browsing lists 2、
   音量輸出 2、HMI 4、Engineering／Dealer Mode 與 screen capture 6。**無一項是非主機件所能持有。**

6. **職能對位之量**（§2-2）。7 個受測職能中 **6 個為「同職能、不同主詞名」**，未配對 1（browsing lists，TLM 側獨有）。

7. **互補分佈**（§1）。2180 物件中 `TLM` 只出現於 §1.18（47 次／20 物件）、`HU` 只出現於 §1.18 以外（1741 次／940 物件），
   **併現 0**，§1.18 內 `HU` 為 0，§1.8 內 `TLM` 為 0。
   二詞在本文件中**從未需要互相區別**，此為同一指涉之異名分佈，非二實體並存之分佈。

8. **跨文件之異名同指**（§4-2）。CFTS022（ECU 軸含 `LTM`／`ETM`／`RRM`）全篇 `TLM` **0 次**、`HU` **340 次**。
   同一角色在 CFTS022 叫 `HU`、在 CFTS020 §1.18 叫 `TLM`。

### §6-1 反證之逐項處置

| # | 反證 | 實測 | 處置 |
|---|---|---|---|
| R1 | 「`TLM` 有自己的 CFTS（`See TLM CFTS`／`See TLM {CFTS019}`）⇒ TLM 是外部件」 | §5-4：§1.8 中「主詞含 `HU` 且外引 `{CFTSxxx}`」者 **24 個**；且外引的是**同一份 `{CFTS019}`** | **不成立為區辨證據**。本文件對本 DUT 之 `HU` 用同一種外引法。外引只表示「行為細節寫在別章」，不表示「行為者是別人」 |
| R2 | 「`TLM` 不在 CFTS020／CFTS022 之 `ECU` 值域 ⇒ TLM 不是本文件所轄之 ECU」 | §4-1／§4-2：`TLM` 於二文件 ECU 值域皆查無；但 `ICS` 亦不在 CFTS020 之 ECU 值域 | **不成立為反證**。`TLM` 是散文級類名，`LTM`／`ETM` 是軸級型號。類名不入枚舉軸是命名層級之事，非實體有無之事 |
| R3 | **「§1.8 標題為 `Silver Box HU`（＝Disassociated 變體），§1.18 標題為 `Associated HU` ⇒ 二節之 HU 是不同變體」** | §5-1 實測二標題確實如此；`4819134` 逐字確立 Associated／Disassociated 之別 | **最強之反證，但不推翻本結論**。它指向的是**變體層級**（`LTM_ADspl` vs `LTM_DDspl`）之別，而非**指涉層級**（TLM 是不是本 DUT）之別。二者仍同為 `LTM`／`ETM` Radio HU，本 DUT 之 ECU 為 `LTM`（A-ICS47），落在該族內。**惟此項須上呈分析層**：R-ICS35 已裁二節並存，若本 DUT 之變體歸屬（AD/DD）另有定論，§1.18 與 §1.8 之適用面本身（非只主詞名）都需重議。本報告不對此作裁。 |
| R4 | 「§1.18 之 29 個適用物件全靠 `allSys` 命中，未點名 `R1L-R`」 | §5-2 實測：allSys 29、R1L-R 僅 1、R1L 僅 1 | **不影響指涉之判定**（`allSys` 依 R-ICS2 v2(b)(i) 為正面命中）。但列記供分析層於 R-ICS35(c)「敘述較具體者」時參用 |
| R5 | 「量測項 1 所期之最強證據（同物件併現且指涉不同）」 | §1-3：**查無（0）** | **查無是有效結果**。其不存在，等於本文件從未在任何一處把 `TLM` 與 `HU` 當作需要區別的二個實體 |
| R6 | 「以 DBC 發送節點反推 TLM 之 ECU」 | §4-4：`Volume_Knob_Val.Info` 等四訊號於二綁定 DBC **查無** | 該路徑**無對應物**，不採；不以其空缺作任一方向之推定 |

### §6-2 若本結論被推翻所需之證據（記於此以備複核）

本結論可被下列**任一項**推翻，本輪皆已掃而**查無**：

1. CFTS020 任一物件內 `TLM` 與 `HU` 併現且顯為二個行為方 → 查無（0／2180）。
2. §1.18 內任一以 `HU` 為主詞之物件 → 查無（0／37）。
3. CFTS020／CFTS022 之 `ECU` 值域出現 `TLM` 而與 `LTM` 並列 → 查無。
4. 任一逐字明言 `TLM` 與 `HU`（或 `LTM`）為不同 ECU → 查無。
5. SYSAD 將 `SYSAD-TLM` 標為系統邊界外之外部件 → 反之，其列於 System Decomposition Table 內。

### §6-3 本量測之已知局限（如實揭露）

- **主詞判別為機械規則**（§2-1）：取 `TLM`／`HU`／`ICS` 三者最先出現位置者。
  複合句（如 `The ICS shall send … to TLM`）會被判為主詞 `ICS`；本報告於 §2-3 已對關鍵句逐字併陳原文，讀者可自行複核，未以主詞欄之機械值取代逐字。
- **§3-3 之 SYSAD 為本輪臨時查核**，未寫入 `tlm_probe_09.py` 之常設量測項（腳本 §4 只掃 CFTS020／CFTS022 之 ECU 值域）。其逐字已全數載於本報告，可依 §0-1 之抽取法複現。
- **R3（Associated vs Disassociated 變體）本輪未判**，且**不在交辦範圍內**。本報告只把它列為反證並記其處置。

---

## §7 交辦所定之升級旗標

```
========================================================================

                        【 E5 觸發 】

    量測結果為 `TLM = DUT`。

    依交辦：該結論會改寫 R-ICS35(b)，屬**分析層**之事。
    本包因此：
      · **未生成 009**，亦未生成任何其他 TC；
      · **未改任何錨**，未改任何 `specification_reference`；
      · 未對 DR-ICS13／DR-ICS18 作結案；
      · 未寫入 RULINGS.md／ANOMALIES.md／DATA_REQUESTS.md／
        framework.md／ANALYSIS_LOCK.md／docs/handoff/**／feature.yaml。

    附帶上呈（下放包未預料，見 §6-1 之 R3）：
    §1.8 標題之 HU 為 `Silver Box HU`（Disassociated 變體），
    §1.18 標題之 HU 為 `Associated HU`。
    二節之 HU 側**變體歸屬不同**。此非本次交辦之量測項，
    但它同時影響 R-ICS35(a) 之「二節並存」與 (b) 之「取何者為錨」，
    建議分析層一併處置。

========================================================================
```
