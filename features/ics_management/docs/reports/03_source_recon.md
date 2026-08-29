# 03_source_recon — 下放包 03 作業 F 偵察報告

> 本檔為下放包 03 作業 F 之偵察（補做下放包 02 §8 追補未執行者）。
> **只列材料，不判採用**，依 R-ICS11。
> 本作業 TC 新增 0；本報告所列任何片段**不得用來解 `PENDING` 佔位、不得充 verbatim 來源**（版本未經確認）。
> 未搬移或複製任何素材檔（R-ICS10）。
>
> 偵察日期：2026-08-29
> 偵察腳本：`features/ics_management/scripts/src_recon_03.py`（本次新建，唯讀）

---

## §0 掃描條件

### 0.1 工具實測

| 工具 | 有無 | 版本／路徑 |
|---|---|---|
| `pdftotext` | 有 | `/opt/homebrew/bin/pdftotext`（poppler） |
| `pdfplumber` | 有 | 0.11.9（`.venv`） |
| `pypdf` | **無** | `ModuleNotFoundError` |
| `openpyxl` | 有 | 3.1.5（`.venv`） |

### 0.2 抽取法（載明）

- **PDF**：主抽取用 `pdfplumber.Page.extract_text()`（逐頁）。文字層有無以 `pdftotext -layout` 與 `pdfplumber` **雙工具交叉驗證**（兩者皆取非空白字元數）。
- **XLSX**：`openpyxl.load_workbook(read_only=True, data_only=True)`，逐 sheet 逐 cell 掃字串型儲存格，命中記 `[sheet]座標`。
- **DOCX**：`zipfile` 直讀 `word/document.xml`，以 `</w:p>` 切段後剝除 XML tag，命中記段落序號。
- **未做 OCR**。無文字層者一律記 `NO_TEXT_LAYER`，不強解。
- PDF 頁面文字有換行斷字（`pop-\nup`），F-2 之 pop-up 掃描另做**去連字號＋單行化**（`re.sub(r'-\n','',t)`）後重掃，避免漏命中。

### 0.3 關鍵詞清單（**一律大小寫不敏感**，`re.IGNORECASE`）

- **F-1**：`knob`、`volume`、`browse`、`tune`、`screen off`、`power`、`enter`、`back`、`menu bar`、`app drawer`、`camera`、`rear view`、`reverse`
- **F-2**：`VOLUME POP_UP`、`volume level`、`volume step`、`detent`、`pop-up`、`popup`、`pop up`、`timeout`、`volume range`、`max volume`、`0-63`、`0~63`
- **F-2 補掃**：`\b(0|1)\s*(-|–|~|to)\s*(63|64|40|39|38|32|30|31|20|22)\b`、`\b63\b`、`volume\s*(range|scale)`、`(maximum|max|total|number of)\s+volume`、`TABLE\s*34`、`volume control curve`

### 0.4 `ls` 實測結果

- `spec-index/sources/`：**33 個檔**（32 PDF ＋ 1 XLSX，見 §1）。與下放包所述「33 本」一致。
- `features/audio_mgmt/inputs/`：**10 個檔**，其中檔名含 `CFTS019` / `CFTS 019` 者 **7 件**（見 §3）。與下放包所述「7 件」一致。

---

## §1 `spec-index/sources/` 總數與四本之實測

### 1.1 總數：33

完整清單（`ls` 原序）：

```
ARABIC mirroring HMI L&F 1.0 R1L-R (February 12 2026).pdf
Announcements HMI Logic and Flow R1 SR24 1A (May 3, 2021).pdf
Bed Lowering Mode HMI Logic and Flow R1 SR24 1A (June 21 2021).pdf
Car Door Open Alert HMI Logic and Flow R1 SR 24 1A.pdf
Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf
Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf
Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf
DAB HMI Logic and Flow R1 SR24 Post1A CR19504 (September 1 2021).pdf
Head Unit Video Player HMI Logic and Flow R1 SR24 1A (May 24 2021).pptx.pdf
HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf
Home Screen HMI Logic and Flow R1 SR25 Post 2A (March 10 2023).pdf
Keyboards HMI Logic and Flow R1L-R (June 6 2022).pdf
Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf
Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023).pdf
Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf
Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf
Personal Assistant HMI Logic and Flow R1 SR24 2A CR20893(May 12, 2022).pdf
Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022).pdf
Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf
Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023).pdf
Projection Device R1L-R HMI Logic and Flow (February 5 2026).pdf
RVC+PAM R1 Low SR24 1A (June 25 2021).pdf
Remote Diagnosis Assistant R1 HMI Logic and Flow SR24 2A (March 11th 2022).pdf
Selectable Tire Fill Assist HMI Logic and Flow R1 SR24 1A (June 1 2021).pdf
SiriusXM 360L SAT Only HMI Logic and Flow R1 SR24 1A (May 24 2021).pdf
Software Updates FOTA HMI Logic and Flow R1 SR24 post 2A (Aug 30 2023).pdf
Status Bar HMI Logic and Flow R1L-R (Feb 13 2026).pdf
Steering Wheel Controls HMI Logic and Flow SR24 DCR21423 (august 3 2022).xlsx
TBM Errors HMI Logic and Flow R1 SR24 1A (May 27 2021).pdf
TBM FOTA HMI Logic and Flow R1 SR24 1A (May 05 2021 ).pdf
TBM HU In Vehicle Messaging R1 HMI Logic and Flow SR 24 post 2A (November, 28th, 2023).pdf
TBM In-Vehicle Help R1 HMI Logic and Flow SR 24 1A (June 25 2021).pdf
Vehicle Category HMI Logic and Flow R1 SR24 Post 2A (December 27 2023).pdf
```

**觀測（不判採用）**：清單中另有兩本檔名與本次四本目標相干、下放包未點名者 ——
`Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`（檔名直指 pop-up 優先權矩陣）與
`HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf`（相機系統）。
本次未掃這兩本（不在下放包指定範圍內），僅記錄其存在。

### 1.2 四本之實測檔名／sha256／文字層

| # | 實際檔名 | 大小 (bytes) | sha256 | 頁數 | 文字層（非空白字元數） |
|---|---|---|---|---|---|
| 1 | `Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf` | 2,401,440 | `dabf34286e9de40509aad57f37a24e8dc13fc19929f278c9f084ec9a10495dca` | 45 | 有（pdftotext 59,708／pdfplumber 59,282） |
| 2 | `Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf` | 5,705,314 | `a9d0be2f13e4c44cc1f5086865d7f6bf0eb2a738a88640523ccf01737fca9c75` | 21 | **`NO_TEXT_LAYER`**（pdftotext 0／pdfplumber 0，21 頁逐頁皆 0） |
| 3 | `Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023).pdf` | 1,792,120 | `c917461bb610b192f11efe18d99e2f593e150283cb94c093fb2b404570350c9a` | 13 | 有（pdftotext 20,494／pdfplumber 20,390） |
| 4 | `RVC+PAM R1 Low SR24 1A (June 25 2021).pdf` | 1,649,300 | `d16ac02e61c20a63c8252e9919b1cc34b5230cc032bbaefd2b22687afe5d97cf` | 15 | 有（pdftotext 10,882／pdfplumber 10,726） |

**檔名與下放包描述之差異（實測為準）**：
- 第 2 本下放包寫「`Core HMI Logic and Flow ... (February 2 2023)`」→ 實際完整檔名為 `Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`。
- 第 3 本下放包寫「`Menu Bar and App Drawer ... (September 11 2023)`」→ 實際為 `Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023).pdf`。
- 第 1、4 本檔名與下放包描述完全一致（含 `Febuary` 之原始拼寫）。

**目次頁存在性**：四本皆為簡報式（pptx export）版面，**均無獨立的正式目次／TOC 頁**，唯 RVC+PAM p.2 標題為 `Index ATTENTION`（該頁 pdfplumber 僅抽出標題行，無條目文字）。故 §2 之「章節」以**每頁投影片標題**（該頁抽出文字之首行）代之，並於表中載明頁次。

---

## §2 四本之目次／章節命中

### 2.1 `Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf`（45 頁，命中 31 頁）

| 頁次 | 投影片標題（＝章節） | 命中關鍵詞 |
|---|---|---|
| 1 | R1 Media | — |
| 2 | Disclaimer | — |
| 3 | Assumptions | — |
| 4 | Reference Documentation | tune, menu bar, app drawer |
| 5 | Acronyms and Abbreviations | — |
| 6 | Media Notes | browse, menu bar |
| 7 | Media Notes (cont) | browse |
| 8 | Media Notes (cont) | **knob**, tune, power |
| 9 | Playing Tab | tune, menu bar |
| 10 | Source Specific Button Bank | **knob**, browse, enter, back |
| 11 | Source Specific Button Bank (cont.) | — |
| 12 | Metadata | — |
| 13 | Metadata (cont.) - Messages | tune |
| 14 | **Tuning Controls** | **knob**, **tune**, enter, back |
| 15 | Play Controls | **knob**, tune, back |
| 16 | Play Controls (cont.) | browse, back |
| 17 | Source Tab | **knob**, tune, back |
| 18 | Source Tab (cont.) | back |
| 19 | Sources Notes | browse, tune, back |
| 20 | Sources Notes (cont.) | browse, enter, app drawer |
| 21 | Sources Notes (cont.) | browse, back |
| 22 | Pinned Sources Bank | — |
| 23 | Source Secondary Menu Pop up | menu bar |
| 24 | **Browse Tab** | **knob**, **browse**, tune, enter, back |
| 25 | Browse Tab (cont.) | browse, tune, enter |
| 26 | Browse Tab (cont.) | browse |
| 27 | Station Scan Flow | — |
| 28 | Mixed Presets | browse, tune, back |
| 29 | Mixed Presets Bank | back |
| 30 | All Presets Pop up | — |
| 31 | USB Folder Browse | browse, enter |
| 32 | USB/Disc Folder Filtering | — |
| 33 | **Audio Settings** | **volume**, enter, back |
| 34 | Audio Settings (cont.) | **volume**, power |
| 35 | Audio Settings (cont.) | **knob**, tune |
| 36 | Audio Settings - AutoPlay Setting | back |
| 37 | Audio Settings - AutoPlay Setting (cont.) - Use Cases | back |
| 38 | Media Widget | back |
| 39–42 | Cluster Audio ／ Cluster Audio Display (1–2 of 2) | — |
| 43 | App Store (1 of 3) – R1 HIGH ONLY | browse, back |
| 44 | App Store (2 of 3) – R1 HIGH ONLY | back |
| 45 | App Store (3 of 3) – R1 HIGH ONLY | back |

逐字片段（節錄，不判採用）：
- p.24：`BT1.9.1) Pressing them plays rejection tone and displays 10s popup: TITLE: "Browse", BODY: "Browse list is being built. Larger media collections can ..."`

### 2.2 `Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`（21 頁）

**`NO_TEXT_LAYER`** —— pdftotext 與 pdfplumber 雙工具、21 頁逐頁抽出之非空白字元數皆為 **0**。
依作業約束不強解、不 OCR。**目次命中：無法取得（0 章節可列）**。

### 2.3 `Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023).pdf`（13 頁，命中 12 頁）

| 頁次 | 投影片標題（＝章節） | 命中關鍵詞 |
|---|---|---|
| 1 | R1 Menu Bar and App Drawer | menu bar, app drawer |
| 2 | Assumptions | menu bar, app drawer |
| 3 | R1 Main Menu Bar | menu bar, app drawer |
| 4 | R1 Menu Bar & App Drawer Customization | back, menu bar, app drawer |
| 5 | **App Drawer Content** | **knob, tune, screen off, back, app drawer, camera, rear view, reverse**（13 詞中命中 8） |
| 6 | App Drawer Content cont. | power, app drawer, camera |
| 7 | R1 App Drawer - Favorites | enter, app drawer, camera |
| 8 | R1 App Drawer - Recent | app drawer |
| 9 | R1 App Drawer – Categories All | enter, app drawer |
| 10 | R1 App Drawer - All | app drawer |
| 11 | R1 App Drawer - Projection | app drawer |
| 12 | Dedicated Bottom Control Bar | menu bar, reverse |
| 13 | Dedicated Bottom Control Bar cont. | — |

逐字片段（節錄，不判採用）：
- p.5（`screen off` 唯一命中處，App Drawer Content Table 之一列）：
  `Screen Off  Screen Off  Off  Controls Feature  Vehicle, System  Y/N`
- p.5（`Backup Cam` 一列）：`Backup Cam  Rear View Camera  Backup Cam  Rear View Camera  Backup Cam  Rear Cam  Camera  Vehicle  Y/N`
- p.5（`knob` 命中，RMB12）：`RMB12.) (R1 Low Only) While app screen is open, turning the tune/ scroll knob = TUNE up/ down (if listening to AM/FM/SXM/DAB) or SKIP to previous/ next (if listening to Media). Presses of the tune/ scroll knob are ignored when the app screen is open.`
- p.7（`enter` 命中，AD1）：`AD1.) Pressing the "Apps" button on the main category bar will open the app drawer which includes Favorites, Recent, and Categories, and All Categories tabs. ... The system should latch on the last used tab when re-entering the app drawer.`
- p.12（`reverse` 命中，MHC2）：`MHC2.) Trailer Reverse Steering Control On/Off button will be located on the bottom of the screen. ...`

**注意（不判採用）**：本冊 `enter`／`back` 之命中，實測多為 `re-entering`／`Backup`／`bar` 等**詞內子字串命中**，非「Enter 鍵／Back 鍵」之導航語意。此為關鍵詞比對之天然雜訊，記於此供裁決層知悉。

### 2.4 `RVC+PAM R1 Low SR24 1A (June 25 2021).pdf`（15 頁，命中 8 頁）

| 頁次 | 投影片標題（＝章節） | 命中關鍵詞 |
|---|---|---|
| 1 | ATTENTION | — |
| 2 | Index ATTENTION（本冊唯一目次頁；抽出文字僅標題行，無條目） | — |
| 3 | RVC+PAM - High Level Visual HMI Scope | enter, back（子字串命中：`CENTER`） |
| 4 | RVC+PAM - Functional automation level | — |
| 5 | RVC+PAM - Functional automation level | — |
| 6 | RVC+PAM – Head Unit Wireframes (Landscape) | camera |
| 7 | RVC+PAM – Head Unit Wireframes (Portrait) | camera |
| 8 | PAM Visualization Requirements | — |
| 9 | **RVC+PAM - Activation and Deactivation** | **camera, reverse** |
| 10 | **RVC Visualization Requirements** | back, **camera, rear view, reverse** |
| 11 | RVC Fault / Special Conditions | camera |
| 12 | PAM Visualization Signals Logic | enter |
| 13 | PAM Possible Feature Configurations | — |
| 14 | PAM Fault / Special Conditions | — |
| 15 | Backup | back（子字串命中：`Backup`） |

---

## §3 CFTS019 七件之清單（`features/audio_mgmt/inputs/`）

目錄共 **10 件**；檔名含 `CFTS019` / `CFTS 019` 者 **7 件**（＝下放包所稱之七件）：

| # | 檔名 | 副檔名 | 大小 (bytes) | sha256 | 型態／可抽性 |
|---|---|---|---|---|---|
| 1 | `CFTS 019_Part2 -All Accepted-Except-DTC-rework.xlsx` | .xlsx | 346,866 | `b2c8e22fd9715ecf49886d546969ff8e07ec95bd178f8fe94468b7be55782f33` | Polarion 匯出；sheets: `Basic Report`(607×78)、`Polarion`(86×2)、`_polarion`(640×6) |
| 2 | `CFTS019-AudioManagement-Part1_released_20260415.xlsx` | .xlsx | 166,386 | `2aae3ed71a9efb1c492a5a20303e8d49712349e2627b1de7e248c9a00cbecc84` | Polarion 匯出；sheets: `Basic Report`(252×78)、`Polarion`、`_polarion` |
| 3 | `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.pdf` | .pdf | 3,015,554 | `2db186009a44848dac0036af41107b30f34158159022c677a558281cfc3e6ca2` | **227 頁 PDF，有文字層**（CFTS019 規格本文，含目次） |
| 4 | `SYS2-CFTS019-CIP_Radio_DSPPP_Accepted-5reqsRARs.xlsx` | .xlsx | 97,297 | `93f63499d5b88a69078a8972701f02b5507c745c3cf78d15357acf036ebb8839` | sheets: 封面／修訂履歷／`Product Document 記錄封面頁`／`Analysis Report`(119×64)／`Attachments`／`Instructions` |
| 5 | `SYS2-CFTS019-PF R1L-R v1 _RadioPerformanceStandard_Part-1_Released.xlsx` | .xlsx | 76,470 | `c67725b786786a66a1ba4b040d61884a588d47c0430f18dbda78cbc24f19345b` | sheets: 封面／修訂履歷／記錄封面頁／`Analysis Report`(38×64)／`Instructions` |
| 6 | `SYS2-CFTS019-R1 Series Radio EQ Document Version 1.8_Accepted-oneRAR.xlsx` | .xlsx | 591,806 | `0845d35756620b42d0c8741b236323ed33755aa9dfb798f7d5e47a1591ab6969` | sheets: 封面／修訂履歷／記錄封面頁／`Analysis Report`(46×64)／`EQ-Filter specs`(172×2)／`Instructions` |
| 7 | `SYS3_CFTS019-Audio_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD.docx` | .docx | 12,964,371 | `1cc6849939bfbde3f52fb3ebf217a3ec8baf4d57e3ce8204d1e211a099f71a83` | DOCX，抽出 **1,763** 段落 |

目錄中另 3 件**非** CFTS019 命名、本次未列為七件（僅記錄）：
`FM-WI-FSM-036-A01 ... _SWQT_20260817_ext.xlsx`、
`FM-WI-FSM-036-A01 ... _SWQT_Audio(AACP)_20260624.xlsx`、
`SWE.1_Audio_Management_Pending_For_Review.xlsx`。

---

## §4 音量階數域（volume level range／最大階數／值域）之所在

### 4.0 結論（材料層）

**未在七件中找到任何「明示宣告」音量階數值域的條文**（形如 `0-63`、`volume range 0..N`、`maximum volume step = N`）。
補掃 `\b63\b`、`0-63`、`0~63`、`volume range`、`volume scale`、`max/maximum/total/number of volume` 於七件**全數 0 命中**（PDF 中唯一 `63` 命中為頁碼字串 `Page 63/227`）。

以下為**實際找到的、與階數域相關之間接材料**，逐件列出。

### 4.1 件 3 — CFTS019 PDF（227 頁）

**目次所在**（p.2–3，抽出之目次行）：

```
1.3.2.10 Volume Gain {4866096}.................................................................................. 36
1.3.2.10.4 Confirmation Tones {4866197}................................................................. 47
1.3.2.10.5 Entertainment and Information Alerts {4866204} ...................................... 48
1.3.2.10.6 Speed Controlled Volume {4866211} ....................................................... 49
1.3.2.12 Speed Volume Control functionality {4866229} .............................................. 51
```

**§1.3.2.10 Volume Gain {4866096}（p.36 起）**——階數域最相干之章節。逐字片段：

- p.36，`1.3.2.10 Volume Gain {4866096}` 之首條 `4866097`：
  `The HU shall be capable of independently adjusting the amplitude of Entertainment, Information 1, and Information 2 sources in non-amplified and in booster-amplified audio systems.`
- p.38，`4866112`（**值域被外部引用之處**）：
  `Refer to {Radio Performance Standard} for details regarding independent volume controls.`
- p.38，`1.3.2.10.1 Entertainment Sources {4866116}` 之 `4866117`：
  `On CAN bus wake-up the recalled Entertainment volume shall be no higher than volume step 20.`
- p.39，`4866125`（**唯一提及 pop-up 且與音量上限有關者**，見 §5）：
  `IF $TeenKeyPresent$ = [True] THEN the HU shall enforce an upper limit of <ENT Key Vol> on the audio level of all Entertainment sources. Refer to HMI for appropriate pop-up display when this limit is reached.`
- p.39，`4866126`（**volume knob 訊號**）：
  `In any "Ignition Working Conditions" IF TLM_Status.Info == "Full-Operation" OR "Timed" THEN only IF an entertainment source is currently active on HU, user can set the volume of entertainment audio output through signals Volume_Knob_Val.Info and Volume_Knob_Dir.Info.`

**§1.3.2.10.4 Confirmation Tones {4866197}（p.47–48）**——出現具體階數值：
- `... audio output at volume step 6, whichever is greater. Confirmation tone volume shall be limited to a maximum of volume step 22. If multiple sources are simultaneously active, the source with the higher volume step setting shall be used.`
- `... the default confirmation tone volume level shall be 4 volume steps below ... equivalent to the audio output at volume step 8, whichever is greater. Confirmation tone volume shall be limited to a maximum of volume step 22.`

**§1.3.2.10.5 Entertainment and Information Alerts {4866204}（p.48–49）**：
- `While cabin audio is active, the default alerts volume level shall be 15 dB below the current audio level or equivalent to the audio output at volume step 6, whichever is greater.`
- `While cabin audio is not active (HU is off), the default alert volume level shall be equivalent to the audio output at volume step 6.`

**其他具體階數值**：
- p.118（Accessibility）：`Accessibility Responses shall be played back at volume step 15 OR the current Entertainment volume step, whichever is greater.`
- p.119：`The volume control shall not be adjustable below step 15 while an accessibility response prompt ...`
- p.46，`4866184`／`4866185`「Chime Volume」表（ObjectID `4866185`）——以**相對步數**表達：
  ```
  CAN Signal Value    Volume Level
  [LOW]               SPL level - 4 steps
  [MED]               SPL level as defined in {CIP Radio DSPPP}
  [MED]               SPL level as defined in {Amplifier EQ Parameters}
  [HIGH]              SPL level + 4 steps
  [SNA]               Last used value
  ELSE use [MED]
  ```

### 4.2 件 1 — `CFTS 019_Part2` xlsx

**目前七件中對階數域上界最直接的材料**（列舉式，非宣告式）：

- `[Basic Report]C17`（ID `NRL-149964`，欄 `Description`）：
  `For CAN amplified audio systems, while cabin audio is active, the default confirmation tone volume level shall be mixed with the cabin audio flow (at 4Vrms): - from cabin volume 7 to cabin volume 38 -> 1,26Vrms (4Vrms-10dB). - cabin volume 6 -> 1,79Vrms (4Vrms-7dB). - cabin volume 5 -> 2,52Vrms (4Vrms-4dB). - cabin volume 4 -> 3,18 Vrms (4Vrms-2dB). - from cabin volume 1 to cabin volume 3 -> 4Vrms. Refer to plot CFTS019-788 for further details`
- `[Basic Report]J17`（同列，欄 `SYS2 System-HW`）：同上文，惟末段作
  `- from cabin volume 0 to cabin volume 3 -> 4Vrms. STLA confirms approval to proceed with this configuration.`
- `[Basic Report]C19` / `J19`（ID `NRL-149966`，alerts 版）：同樣的 `cabin volume 7 to cabin volume 38` 與 `1 to 3`（C 欄）／`0 to 3`（J 欄）分歧。

> **不符（照錄，不調和）**：同一列的 `Description`(C) 寫 `from cabin volume 1`，`SYS2 System-HW`(J) 寫 `from cabin volume 0`。兩者下界不一致。本報告不判定何者為準。
> **不判採用之觀測**：上述列舉之最大出現值為 `cabin volume 38`；此為**列舉端點**，非「最大階數」之宣告條文。`38` 是否即階數域上界，本次偵察無法確認。

- `[Basic Report]C222`：`On CAN bus wake-up the recalled Entertainment volume shall be no higher than volume step 20.`（與 PDF `4866117` 同源）
- `[Basic Report]K24`（`SYS2 System-SW`）：`SW supplier shall allow the user to select Speed Controlled Volume levels below from HU HMI OFF Level 1 Level 2 Level 3 ...`（此為 SDVC 之 4 檔位，非主音量階數域）

### 4.3 件 2 — `CFTS019-AudioManagement-Part1` xlsx

- `[Basic Report]C222`：`On CAN bus wake-up the recalled Entertainment volume shall be no higher than volume step 20.`
- `[Basic Report]BA208`（Test/Verify 欄）：`Verify that the volume level of each source group ($\text{ENT}$, $\text{INFO1}$, $\text{INFO2}$) can be independently adjusted without affecting the volume levels of the other two groups ...`
- `[Basic Report]AW231`／`AW244`：AAOS `CarAudioService` 之 `volume step logic`／`volume group` 實作敘述，**無數值域**。
- 全檔 `volume range`／`max volume`／`63` 命中 0。

### 4.4 件 4 — `SYS2-CFTS019-CIP_Radio_DSPPP` xlsx

- `[Analysis Report]C41`：`Loudness compensation behavior can be shifted up or down 4 volume steps.`
- `[Analysis Report]M41`：`HW supplier shall apply loudness compensation with an adjustment range of up to ±4 volume steps.`
- `[Analysis Report]M53`：`... "Default" Cabin Equalization ... Loudness Offset = 0 volume steps ... Volume curve as defined in the HU Component Specification (variable output.)`
- `[Analysis Report]C61`／`M61`：warning chime 可調參數含 `Volume step` / `Chime volume (in volume steps)` / `Maximum audio volume during a chime event`。
- **無階數域數值**。M53 將 volume curve 外指至 **HU Component Specification**（該文件不在本七件內）。

### 4.5 件 5 — `SYS2-CFTS019-PF ... RadioPerformanceStandard_Part-1` xlsx

CFTS019 PDF `4866112` 明言值域細節「Refer to {Radio Performance Standard}」，故本件為最應命中處。實測：

- `[Analysis Report]C25`：`A volume change shall affect the current active source. The volume level of an audible background source shall not be changed. The LTM shall satisfy (within tolerance) the volume control curve defined in TABLE 34 at +23 degrees C.`
- `[Analysis Report]M25`／`N25`：同上，HW／SW supplier 版本，同樣只指向 `TABLE 34`。
- `[Analysis Report]M34`：`... the SDVC volume level can be 0, 1, 2, or 3. Shall store gains between 0.0 dB and 10.0 dB for 8 speeds ...`（**SDVC 檔位域 `0..3`，非主音量階數域**）

> **關鍵缺口**：`TABLE 34`（volume control curve）**本體不在此 xlsx 內**。本件僅有 `Analysis Report`(38 列) 與 `Instructions` 等 sheet，無附表 sheet、無 attachments sheet。全檔搜 `TABLE 34` 僅得上述三個「引用」，無表格內容。

### 4.6 件 6 — `SYS2-CFTS019-R1 Series Radio EQ Document Version 1.8` xlsx

- `[Analysis Report]C27`：`... The following parameters shall be adjustable for each warning chime for each EQ profile. - Frequency of chime (Hz) - Waveform of chime (Square or Sine) - Volume of chime (in volume steps) - Max volume of audio ...`
- `[Analysis Report]M27`：`... - Chime volume (in volume steps) - Maximum audio volume during a chime event`
- `[EQ-Filter specs]B3`：`"Default" Cabin Equalization shall be defined as variable output audio with no offsetting parameters: Loudness Offset = 0 volume steps ... Volume curve as defined in the HU Component Specification (variable output.)`
- **無階數域數值**；同樣外指 HU Component Specification。

### 4.7 件 7 — `SYS3_CFTS019-Audio ... SYSAD.docx`

F-2 關鍵詞逐段掃描 **0 命中**（`volume level`／`volume step`／`detent`／`popup` 等皆無）。
以較寬的 `volume|音量` 掃描，命中之處全為 AAOS 架構敘述（`VolumeShaper`、`volume group`、`CarAudioService`、ramp-up/down、ducking），**無任何階數域數值**。
其目次段落中與音量相關者：
```
4.10.1. Volume Change Behavior ......... 51
4.10.6. Speed Controlled Volume Behavior ......... 56
```
該兩節內文以 VolumeShaper／ramp 時序描述為主，未見階數域。

---

## §5 `VOLUME POP_UP` 顯示條件之所在

### 5.0 結論（材料層）

**七件中，字面 `VOLUME POP_UP` 命中數為 0。**（大小寫不敏感、含 `VOLUME POP-UP`／`VOLUME POPUP`／`VOLUME POP UP` 變體）

進一步以 `pop[ _-]?up`（大小寫不敏感、PDF 另做去連字號重掃）掃全部七件：

| # | 件 | `pop-up` 家族命中數 |
|---|---|---|
| 1 | `CFTS 019_Part2` xlsx | **0** |
| 2 | `CFTS019-AudioManagement-Part1` xlsx | **0** |
| 3 | CFTS019 PDF（227 頁） | **2**（見下） |
| 4 | `SYS2-CFTS019-CIP_Radio_DSPPP` xlsx | **0** |
| 5 | `SYS2-CFTS019-PF ... RadioPerformanceStandard` xlsx | **0** |
| 6 | `SYS2-CFTS019-R1 Series Radio EQ` xlsx | **0** |
| 7 | `SYS3_CFTS019-Audio ... SYSAD.docx` | **0** |

### 5.1 件 3（CFTS019 PDF）之 2 處 pop-up 命中（逐字，含所在章節）

**(1) p.39 — §1.3.2.10.1 Entertainment Sources {4866116} 內，ObjectID `4866125`**

> `4866125: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [ECU:ETM, RRM, LTM] [Market:All] [Radio:allSys] [EE Architecture:PowerNet]`
> `IF $TeenKeyPresent$ = [True] THEN the HU shall enforce an upper limit of <ENT Key Vol> on the audio level of all Entertainment sources. Refer to HMI for appropriate pop-up display when this limit is reached.`

材料層記述：此處提及之 pop-up 為 **Teen Key 音量上限觸及**時之提示，且條文**明白將顯示條件外推給 HMI 文件**（`Refer to HMI for appropriate pop-up display`）。CFTS019 本身**未定義**該 pop-up 之出現時機、停留時長或消失條件。此條 EE Architecture 限 `PowerNet`。

**(2) p.121 — §1.3.3.13 Emergency Vehicle Alert System (EVAS) {4866827} 內，ObjectID `4866830` 之續行**

> `4866830: ... An EVAS event is considered finished when one of the following occurs:`
> `1) waiting five seconds`
> `2) waiting for the event to finish`
> `3) the popup is dismissed by the user`

材料層記述：此處之 popup 屬 **EVAS 事件**（`[Radio:R1H]`、`[Model Year:2023/2024/2025]`），非音量 pop-up。其「五秒」與「使用者關閉」是 **EVAS 事件結束條件**，不是音量彈窗之顯示條件。

### 5.2 判定範圍外之明確聲明

- 七件中**查無** `VOLUME POP_UP` 之顯示條件（何時出現／停留多久／何時消失）。
- 唯一與「音量相關之 pop-up」有關者為 `4866125`，且該條**把顯示條件指向 HMI 文件**，本身不含條件。
- 掃描方式已載明於 §0.2／§0.3；xlsx 為全 sheet 全 cell、docx 為全 1,763 段落、PDF 為全 227 頁（含去連字號重掃）。**查無為實測結果。**

---

## §6 未命中／無文字層者之具名清單

### 6.1 `NO_TEXT_LAYER`（無文字層，本次無法取得任何章節）

1. `spec-index/sources/Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`
   （21 頁；pdftotext 與 pdfplumber 皆 0 非空白字元；未 OCR）
   → **Screen Off／電源鍵 UI 面之目次命中：本次無法產出。**

### 6.2 `VOLUME POP_UP` 顯示條件——查無之具名清單（全七件）

1. `CFTS 019_Part2 -All Accepted-Except-DTC-rework.xlsx`
2. `CFTS019-AudioManagement-Part1_released_20260415.xlsx`
3. `R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.pdf`（有 2 處 pop-up，但皆非音量彈窗顯示條件）
4. `SYS2-CFTS019-CIP_Radio_DSPPP_Accepted-5reqsRARs.xlsx`
5. `SYS2-CFTS019-PF R1L-R v1 _RadioPerformanceStandard_Part-1_Released.xlsx`
6. `SYS2-CFTS019-R1 Series Radio EQ Document Version 1.8_Accepted-oneRAR.xlsx`
7. `SYS3_CFTS019-Audio_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD.docx`

### 6.3 音量階數域「明示值域宣告」——查無之具名清單（全七件）

同 §6.2 之七件。七件皆無形如 `0-63` / `0..N` / `maximum volume step = N` 之宣告條文。
間接材料見 §4（最高出現值 `cabin volume 38`、上限規則 `volume step 20` / `volume step 22`）。

### 6.4 外指但不在七件內之文件（供裁決層決定是否另立 DR）

| 被引用之文件名 | 引用出處 | 被引用內容 |
|---|---|---|
| `{Radio Performance Standard}` 之 **TABLE 34**（volume control curve） | CFTS019 PDF p.38 `4866112`；`SYS2-CFTS019-PF` `Analysis Report` C25/M25/N25 | 音量控制曲線 —— **表本體不在件 5 內** |
| **HU Component Specification** | `SYS2-CFTS019-CIP` `Analysis Report` M53；`SYS2-...EQ Document` `EQ-Filter specs` B3 | `Volume curve as defined in the HU Component Specification` |
| **HMI 文件**（未具名） | CFTS019 PDF p.39 `4866125` | `Refer to HMI for appropriate pop-up display when this limit is reached` |
| `{CIP Radio DSPPP}` / `{Amplifier EQ Parameters}` | CFTS019 PDF p.44、p.46 `4866185` | Signal source volume levels / SPL level |
| `"Table for CFTS019- 4866516"`（在 attachments sheet） | `CFTS 019_Part2` `[Basic Report]K146/K147` | Information Source Handling Table |

> **不判採用**：以上僅為「引用鏈斷點」之列舉。是否納源、是否開 DR，屬裁決層。

---

## 附錄 A：本次未觸及但相干之 sources（僅記錄，未掃）

- `spec-index/sources/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` —— 檔名直指 pop-up 清單優先權矩陣。若 `VOLUME POP_UP` 屬 HMI 層彈窗，此冊為候選查處，但**不在下放包 03 作業 F 指定之四本內**，本次未掃。
- `spec-index/sources/HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf` —— 相機系統，與 (012) Rear View Camera Transition 相干，同樣不在指定四本內，未掃。
- `spec-index/sources/Steering Wheel Controls HMI Logic and Flow SR24 DCR21423 (august 3 2022).xlsx` —— 33 件中唯一非 PDF。

## 附錄 B：重現指令

```bash
cd /Users/peihe/Work_Projects/TC_Generator

# F-1
.venv/bin/python3 features/ics_management/scripts/src_recon_03.py f1 \
  "spec-index/sources/Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf" \
  "spec-index/sources/Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf" \
  "spec-index/sources/Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023).pdf" \
  "spec-index/sources/RVC+PAM R1 Low SR24 1A (June 25 2021).pdf"

# F-2（七件）
.venv/bin/python3 features/ics_management/scripts/src_recon_03.py f2 \
  features/audio_mgmt/inputs/CFTS*019*.xlsx \
  "features/audio_mgmt/inputs/R1LR_Atl-H_25PI3.5_Multimedia - Radio and Audio_CFTS 019_Audio Management_20250910_1235.pdf" \
  features/audio_mgmt/inputs/SYS2-CFTS019-*.xlsx \
  features/audio_mgmt/inputs/SYS3_CFTS019-*.docx
```
