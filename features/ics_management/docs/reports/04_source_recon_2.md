# 04_source_recon_2 —— 下放包 04 作業 D：二本新納偵察

> 本檔為下放包 04 作業 D 之偵察，依 **R-ICS21(c)**，**只列材料不判採用，不充 verbatim 來源、不充錨**。
> 本檔不新增 TC、不改任何 TC JSON、不動任何素材檔。所列章節與命中僅為材料清冊，
> 採用與否、是否可作為 verbatim 來源或錨，均待後續裁決，非本檔所能決定。

- 作業：D（二本新納偵察）
- 腳本：`features/ics_management/scripts/src_recon_04.py`（新建，唯讀）
- 執行日：2026-08-29

---

## §0 掃描條件

### 0.1 實際 `ls spec-index/sources/` 之對應結果

下放包所列二本，實際檔名與下放包**完全一致**（無出入）：

| # | 實際檔名 |
|---|---|
| 1 | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` |
| 2 | `HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf` |

二者皆位於 `spec-index/sources/`。

### 0.2 雙工具逐頁抽取

- 工具 A：`pdftotext -layout`（poppler，`/opt/homebrew/bin/pdftotext`），以 form feed（`\f`）切頁。
- 工具 B：`pdfplumber` 0.11.9，`page.extract_text()` 逐頁。
- 逐頁各自計算「非空白字元數」（`ns_pdftotext` / `ns_pdfplumber`）。
- **判定規則**：某頁二工具之非空白字元數**皆為 0** 時，該頁記 `NO_TEXT_LAYER`。
- **未做 OCR、未做強解**。無文字層即如實記為無，不以任何方式補齊。

### 0.3 去連字號重掃（三種正規化）

PDF 常見 `pop-\nup` 這類斷行連字號，以及 `Rear\nView` 這類純換行斷詞；逐行掃描會漏命中。
故每頁另備三種文本，關鍵詞在三者皆掃一次，記錄是哪一種正規化命中：

| 代號 | 產生方式 |
|---|---|
| `raw` | 二工具原文串接 |
| `dehyph` | 以 `-[ \t]*\n[ \t]*` → 空字串，移除斷行連字號 |
| `flat` | `dehyph` 後再把所有空白（含換行）壓成單一空格 |

另設一條寬鬆樣式，專掃 `VOLUME POP_UP` 之所有寫法變體：

```
volume[\s_\-]*pop[\s_\-]*up      （IGNORECASE，掃 flat 文本）
```

此樣式可同時涵蓋 `VOLUME POP_UP`、`VOLUME POP-UP`、`VOLUME POPUP`、`VOLUME POP UP`，
以及跨換行、跨連字號之各種斷行形態。

**重掃有效性佐證**：`HeadUnitCameraSystems` 之 p.14、p.92、p.93、p.269 四頁，
關鍵詞 `rear view` 僅在 `flat` 命中、在 `raw` 不命中（原文為跨行之 `Rear` / `View`）。
若只做逐行掃描，此四頁會被誤記為未命中。

### 0.4 關鍵詞清單（**一律大小寫不敏感**）

**Pop Up List Priority Matrix**：
`VOLUME POP_UP`、`VOLUME POP-UP`、`VOLUME POPUP`、`VOLUME POP UP`、
`volume`、`priority`、`popup`、`pop up`、`pop-up`、`mute`、`timeout`、`dismiss`、`duration`

**HeadUnitCameraSystems**：
`rear view`、`rearview`、`rear camera`、`backup cam`、`reverse`、`RVC`、
`camera transition`、`PAM`、`gear`、`park`

### 0.5 sha256 取得方式

以 `shasum -a 256` 實算，並以腳本內 `hashlib.sha256` 分流重算比對，二者一致。

---

## §1 二本之實際檔名／頁數／sha256／文字層有無

| 項目 | Pop Up List Priority Matrix | HeadUnitCameraSystems |
|---|---|---|
| 實際檔名 | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf` |
| 頁數（pdfinfo） | 10 | 276 |
| 頁數（pdftotext 切頁） | 10 | 276 |
| 頁數（pdfplumber） | 10 | 276 |
| 檔案大小（bytes） | 1,035,049 | 17,840,154 |
| sha256 | `dc078763c67b52388eba8edf5c461515cfd2d92dd3a78dba0ce4e365e43ccc2f` | `69884c963c08cac586e80102ea9ef8dcba080857e2a381f0a6fb0aa9190a4f8e` |
| 文字層 | **有**，10/10 頁皆有 | **有**，276/276 頁皆有 |
| `NO_TEXT_LAYER` 頁 | 無 | 無 |
| 二工具不一致頁 | 無（逐頁非空白字元數完全相同） | 無（無「僅 A 有／僅 B 有」之頁） |

補充中繼資料（`pdfinfo`）：

- Pop Up List Priority Matrix：Creator `Microsoft PowerPoint 2016`，Author `Paolo Visconti`，
  CreationDate `2021-05-04`，頁面 720x540 pts，PDF 1.5。
- HeadUnitCameraSystems：Creator `Microsoft PowerPoint for Microsoft 365`，Author `Ian Komisak`，
  CreationDate `2023-02-11`，ModDate `2025-11-05`，頁面 720x540 pts，PDF 1.7。

---

## §2 Pop Up List Priority Matrix

### 2.1 目次／章節（本檔無 TOC 頁，以下為逐頁投影片標題實抽）

| 頁 | 標題 |
|---|---|
| 1 | SR24 1° Pop-up Matrix — General Rules and Specifications |
| 2 | Change Log, Release updates |
| 3 | Pop-Up Definition |
| 4 | Pop-up Categories (Priorities) |
| 5 | Stacking of Window Pop-Ups |
| 6 | Background Blur |
| 7 | Type/categories, definitions, and examples 1/3 |
| 8 | Type/Categories, definitions, and examples 2/3 |
| 9 | Type/Categories, definitions, and examples 3/3 |
| 10 | New Matrix Table |

### 2.2 逐頁關鍵詞命中表

（`o` = 命中；空白 = 未命中。三種正規化之命中結果在本檔全數一致，故不分欄。）

| 頁 | volume | VOLUME POP_UP 系 | priority | popup | pop up | pop-up | mute | timeout | dismiss | duration |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | o | | | | |
| 2 | | | o | o | | o | | | | |
| 3 | | | o | o | | o | | o | o | |
| 4 | | | | | | o | | | | |
| 5 | | | o | | | o | | o | | |
| 6 | | | | o | | o | | | o | |
| 7 | | | o | | | o | | | | |
| 8 | | | o | o | | o | | | | |
| 9 | | | o | | | o | | | | |
| 10 | | | | o | | o | | o | | |

**合計**：
- `volume`：**0 頁命中**
- `VOLUME POP_UP` 系（含 `POP-UP` / `POPUP` / `POP UP` 變體與寬鬆樣式）：**0 頁命中**
- `mute`：**0 頁命中**
- `duration`：**0 頁命中**
- `pop up`（帶空格之獨立詞形）：0 頁（文中一律寫作 `pop-up` / `popup`）
- `priority` 6 頁、`popup` 5 頁、`pop-up` 10 頁、`timeout` 3 頁、`dismiss` 2 頁

### 2.3 `VOLUME POP_UP` 之明確結論

> **查無。**
> `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` **全篇 10 頁完整有文字層、
> 已 100% 抽出並人工通讀**，**不含 `VOLUME POP_UP`，亦不含 `volume` 一字之任何出現**，
> 因此**本文件內不存在 `VOLUME POP_UP` 的顯示條件**（何時出現／停留多久／何時消失皆無）。

**掃了什麼、怎麼掃的（可複驗）**：

1. 雙工具逐頁抽取（`pdftotext -layout` + `pdfplumber`），10 頁非空白字元數逐頁相同，
   最大單頁 1,748 字元（p.10 矩陣表），無 `NO_TEXT_LAYER` 頁。
2. 三種正規化（`raw` / `dehyph` / `flat`）各掃一次，並以寬鬆樣式
   `volume[\s_\-]*pop[\s_\-]*up`（IGNORECASE）掃 `flat`：**0 命中**。
3. 另以 `pdftotext -layout ... | grep -inE "volume|mute|duration|audio|vol"` 獨立複驗：
   **grep exit code = 1（無任何一行命中）**。
4. 全文 10 頁已完整輸出並逐頁通讀，確認全文為「pop-up 分類與疊層之通則」，
   通篇以類別（Cat. RVC / SL / 1P / 1T / 2 / 3 / X / VR）為粒度，
   **不含任何個別 pop-up 之逐項清單**，自然也不含音量相關條目。

**為何本文件不可能有該答案（材料面說明，不作裁決）**：

本文件 p.3 自述其為通則文件，並明文把「個別 pop-up 的 timeout 定義」外指到另一份文件——
p.3 逐字：

> "Popups with X button which do not have a timeout defined in the **Pop-up List Notification** will
> have a 5 sec timeout. Rationale: If you user has the option to press the X button without
> addressing the pop-up (selecting any other pop-up buttons), there will be no impact timing-out
> those pop-ups"
>
> "Exceptions would be incoming call/text message, or user initiated popups"

亦即：**逐項 pop-up 之清單與其 timeout，載於一份名為 `Pop-up List Notification` 的文件**，
該文件**不在 `spec-index/sources/` 之 33 件內**（已對 `ls` 全表比對，無同名或近名檔）。
本檔僅陳列此線索，不判其為應取素材，亦不代擬 DATA_REQUEST 條文。

**另有一項可能相干、但本檔不作判斷的材料**：p.8「Category X」逐字定義為

> "These popups only cover a small part of the screen in order to indicate activation of a
> area-specific function or climate settings."

以及 p.10 矩陣表中 Cat. X 列反覆出現之
"Type X remains visible in its small area till timeout"。
此處**未點名 volume**，本檔**不推定** `VOLUME POP_UP` 屬 Cat. X，僅列出供後續裁決取用。

---

## §3 HeadUnitCameraSystems

### 3.1 目次（p.16 實抽，逐字照錄，含其原標示之頁碼）

```
Table of Contents
 ▪ Radio Sales Codes and Screen Sizes……………………..……...…………....………...11
 ▪ Acronyms & Abbreviations……………………...……….………....................................15
 ▪ Backup Camera and General System Settings……………………...………………..…17
 ▪ Backup Camera Tailgate Down…………………………………………………………….21
 ▪ CHMSL/Cargo Camera (If Equipped)……………………….…………………………….24
 ▪ Trailer Hitch Zoom (If Equipped)…………...…………………………….……….............27
 ▪ Fault Conditions……………………………………………………….………………...…..31
 ▪ Surround View Camera System………………………………………….………………..34
 ▪ Rear View Camera with Swing Doors Check (If Equipped)………...……………….….46
 ▪ Forward Facing Camera with Tire Lines…………………………….………………….…52
 ▪ Camera Wash………………………………………………………………………………..65
 ▪ Deviations from General L&F………………………………………………..................…68
 ▪ Park Sense………………………………………………………………………...........…..80
 ▪ Vehicle Cameras App…………………………………………...…………..................…..84
 ▪ Multi View………………………………………………………………………………….....94
 ▪ Cargo Camera with Dynamic Centerline……………………….…………………...........94
 ▪ Trailer Reverse Guidance………………………………………………………………....117
 ▪ Auxiliary Cameras…………………………………………………………...……………..135
 ▪ Wireless Auxiliary Cameras.………………………………………………………………214
 ▪ Trailer Surround View……...………………………………………………………………249
```

**注意（只列不判）**：TOC 所標頁碼與 PDF 實際頁次**不一致**（TOC 本身在 PDF p.16）。
以實抽之投影片標題比對，實際章段起點約為：

| 章段（依實抽標題） | PDF 實際起始頁 |
|---|---|
| Change Log | 2 |
| Table of Contents | 16 |
| Radio Sales Codes and Screen Sizes | 17 |
| Acronyms & Abbreviations | 19 |
| General Logic & Flow | 20 |
| Rearview Camera and General System | 22 |
| Activation & Deactivation Methods (All Head Units) | 23 |
| "Check Entire Surroundings" | 26 |
| Fault Conditions | 28 |
| General Screen Layouts | 31 |
| **Rear View Camera** | **39** |
| Trailer Hitch Zoom (If Equipped) | 50 |
| Standalone CHMSL/Cargo Camera (If Equipped) | 56 |
| Rear View Camera with Tailgate in Down Position | 60 |
| Rear View Camera with Swing Doors | 62 |
| Cargo Camera with Dynamic Centerline | 69 |
| Forward Facing Camera with Tire Lines | 88 |
| Camera Wash | 101 |
| Vehicle Surround View Camera System | 105 |
| Park Sense & Side Distance Warning | 120 |
| Vehicle Cameras App | 137 |
| "Enhanced Camera App" Camera View | 157 |
| Front Tire to Curb View | 180 |
| Trailer Reverse Guidance | 188 |
| Trailer Reverse Guidance with Jack-Knife Warning | 199 |
| Wired & Wireless Auxiliary Cameras | 210 |
| R1 Low Wired AUX Cameras | 245 |
| Trailer Surround View | 257 |

### 3.2 逐頁關鍵詞命中表

共 276 頁，其中 **129 頁**有至少一個關鍵詞命中。逐頁命中如下
（詞序：`rear view` / `rearview` / `rear camera` / `backup cam` / `reverse` / `RVC` /
`camera transition` / `PAM` / `gear` / `park`）：

| 頁 | 命中詞 |
|---|---|
| 2 | rear view, rear camera, backup cam, reverse, RVC |
| 3 | rear view, rearview, park |
| 4 | reverse, RVC |
| 5 | reverse, RVC |
| 6 | backup cam, reverse |
| 8 | reverse, park |
| 9 | rear view, reverse, park |
| 10 | reverse, gear |
| 11 | park |
| 12 | park |
| 14 | rear view *(僅 flat 命中)* |
| 16 | rear view, backup cam, reverse, park |
| 19 | rear view, backup cam, reverse, RVC |
| 21 | reverse |
| 22 | rearview |
| 23 | reverse, gear, park |
| 24 | reverse, RVC |
| 25 | reverse, RVC, park |
| 29 | park |
| 30 | park |
| 34 | PAM, park |
| 36 | RVC, park |
| 37 | rear view, RVC, park |
| 38 | RVC |
| 39 | rear view |
| 40 | rear view |
| 41 | rear view, reverse |
| 42 | rear view, reverse |
| 43 | rear view, reverse, park |
| 44 | rear view |
| 45 | rear view, reverse |
| 46 | rear view |
| 47 | rear view |
| 48 | rear view |
| 49 | rear view, reverse |
| 51 | rear view, backup cam, reverse, gear, park |
| 54 | reverse |
| 55 | rear view |
| 58 | backup cam, reverse |
| 59 | backup cam, reverse |
| 60 | rear view |
| 62 | rear view |
| 63 | rearview |
| 68 | rear view |
| 71 | rear view, reverse, park |
| 72 | gear |
| 91 | rear view, reverse, park |
| 92 | rear view *(僅 flat 命中)* |
| 93 | rear view *(僅 flat 命中)*, reverse |
| 106 | rear view, park |
| 107 | park |
| 108 | rear view, reverse, park |
| 109 | rear view, reverse, gear, park |
| 110 | backup cam |
| 111 | reverse |
| 113 | park |
| 114 | rear view |
| 116 | rear view |
| 117 | reverse |
| 118 | reverse |
| 119 | park |
| 120 | park |
| 121 | park |
| 122 | park |
| 125 | park |
| 126 | reverse, park |
| 128 | park |
| 129 | park |
| 130 | park |
| 131 | rear view, reverse, RVC, gear, park |
| 132 | gear, park |
| 133 | gear, park |
| 134 | reverse, park |
| 135 | park |
| 136 | gear, park |
| 138 | rear view, RVC |
| 142 | reverse |
| 149 | rear view |
| 150 | rear view, reverse |
| 152 | backup cam, reverse |
| 153 | rear view, reverse |
| 154 | reverse |
| 155 | rear view, reverse, gear |
| 156 | reverse |
| 159 | rear view, reverse, gear |
| 160 | backup cam, reverse, gear, park |
| 161 | rear view, reverse, gear, park |
| 163 | rear view, reverse, gear, park |
| 164 | rear view, reverse, gear, park |
| 165 | gear, park |
| 166 | gear, park |
| 167 | reverse, gear, park |
| 168 | reverse, gear, park |
| 169 | reverse, gear, park |
| 170 | reverse, gear, park |
| 171 | reverse, park |
| 172 | reverse, park |
| 175 | rear view, backup cam, reverse, park |
| 177 | rear view, reverse, park |
| 178 | rear view, reverse, gear, park |
| 179 | rear view, reverse, gear |
| 185 | park |
| 186 | reverse |
| 188 | reverse |
| 190 | reverse |
| 192 | reverse |
| 193 | reverse |
| 194 | reverse |
| 198 | reverse, gear, park |
| 199 | reverse |
| 202 | reverse |
| 203 | reverse |
| 204 | reverse |
| 208 | reverse |
| 209 | reverse, gear, park |
| 213 | rear view, reverse |
| 219 | rear view |
| 220 | reverse |
| 225 | reverse |
| 226 | reverse |
| 246 | rearview |
| 248 | backup cam, reverse |
| 249 | backup cam, reverse |
| 250 | backup cam |
| 251 | reverse |
| 252 | reverse |
| 258 | rear view |
| 261 | rear view |
| 263 | rear view, park |
| 267 | rear view, park |
| 268 | rear view |
| 269 | rear view *(僅 flat 命中)* |
| 270 | backup cam, reverse, gear |
| 276 | gear |

**各詞命中頁數合計**：

| 關鍵詞 | 命中頁數 |
|---|---|
| `reverse` | 77 |
| `park` | 57 |
| `rear view` | 54 |
| `gear` | 27 |
| `backup cam` | 15 |
| `RVC` | 11 |
| `rearview` | 4 |
| `rear camera` | 1（p.2） |
| `PAM` | 1（p.34） |
| `camera transition` | **0** |

**`camera transition` 0 命中之補掃**：另以單詞 `transition`（IGNORECASE，掃 `flat`）
重掃全 276 頁，僅 **p.21、p.27、p.91** 三頁出現，逐字如下：

- p.21 / p.27（同一句，分見 "Head Unit Requirements/Assumptions" 與
  "Check Entire Surroundings Message"）：

  > "When the Head Unit (HU) **transitions** the display to any camera image, a message stating
  > "Check Entire Sur..."（該句於本頁續行）

- p.91（"General Information: Activation & Deactivation"，FFCTL 章）：

  > "...changed to REVERSE after FFCTL is currently activate, the Head Unit will **transition**
  > to [Top View + Rear View]"
  > "Shifting from REVERSE to PARK, NUETRAL or DRIVE will **transition** to FFCTL"
  > "If FFCTL is activated while in reverse, the FFCTL view wil..."（該句於本頁續行）

亦即本文件**不使用 `camera transition` 這個複合術語**，相關語意以 `transition to ...` 之
動詞形態表達，且僅 3 頁。

### 3.3 與 SWRA `SWE1-ICS-012`（Rear View Camera Transition）相干之章節（**只列，不判**）

前置事實（實測）：repo 內 `grep -rln "SWE1-ICS-012"` **無任何檔命中**；
`grep -rln "SWE1-ICS"` 僅命中 `features/ics_management/ANOMALIES.md` 與
`features/ics_management/DATA_REQUESTS.md`。其中 `DATA_REQUESTS.md` DR-ICS2 記載
SYS2 Traceability 列有 SWE1-ICS-011 / 012，**需求分頁缺列**，狀態 OPEN。
**故 `SWE1-ICS-012` 目前無可比對之需求本文**，以下相干性僅依其標題字面
"Rear View Camera Transition" 判讀章節主題，**不作採用判斷，不充錨**。

| 章段 | PDF 頁範圍（實抽） | 相干理由（字面） |
|---|---|---|
| Rearview Camera and General System (Settings) | 22 | RVC 一般系統與設定 |
| Activation & Deactivation Methods (All Head Units) | 23 | RVC 進入／退出方法之通則 |
| General RVC Activation/Deactivation w/o Camera Delay | 24 | RVC 進出（無延遲）之 transition |
| General RVC Activation/Deactivation with Camera Delay | 25 | RVC 進出（有延遲）之 transition |
| "Check Entire Surroundings" / Message | 26–27 | **p.27 為 `transition` 三處命中之一**，述 HU 切換至任一 camera image 時之訊息 |
| Fault Conditions | 28–30 | RVC 故障時之行為 |
| Rear View Camera（專章） | 39–49 | 含 Head Unit Settings（41）、General RVC Automatic（42–43）、Manual Activation（44–48）、Non-SVC 車輛存取（49） |
| Rear View Camera with Tailgate in Down Position | 60–61 | RVC 特例態 |
| Rear View Camera with Swing Doors | 62–68 | 含 Camera Delay OFF（64–65）／ON（66–67） |
| Forward Facing Camera with Tire Lines — Activation & Deactivation | 91 | **p.91 為 `transition` 命中頁**，明文述 REVERSE ↔ P/N/D 之視圖 transition |
| Vehicle Surround View Camera System | 105–119 | 含 Surround View Logic – Camera Delay ON（111）、Automatic Activation（117–118） |
| Park Sense & Side Distance Warning | 120–136 | 含 ParkSense Based Camera Activation（125） |
| Vehicle Cameras App — Reverse 行為 | 155–156 | Reverse 進入時之 camera view 切換 |
| "Enhanced Camera App Feature" Entry/Exit、Latching、Manual activation | 160–172、179 | 各檔位（P/N/D/R）下之進出與駐留行為 |
| Auxiliary Cameras — Reverse Behavior | 225–226 | Reverse 時 AUX camera 行為 |

**Camera Delay 相干頁彙整（供後續取用參考，不判）**：24、25、54、64、65、66、67、111。

---

## §4 未命中／無文字層者之具名清單

### 4.1 `NO_TEXT_LAYER` 具名清單

**空**。二本共 286 頁，**無任何一頁**在 `pdftotext` 與 `pdfplumber` 二者皆得 0 非空白字元。
故本次無 OCR 需求，亦未執行 OCR。

### 4.2 關鍵詞 0 命中之具名清單

**Pop Up List Priority Matrix**（全 10 頁 0 命中之關鍵詞）：

- `VOLUME POP_UP`
- `VOLUME POP-UP`
- `VOLUME POPUP`
- `VOLUME POP UP`
- 寬鬆樣式 `volume[\s_\-]*pop[\s_\-]*up`
- `volume`
- `mute`
- `duration`
- `pop up`（帶空格之獨立詞形；本文一律作 `pop-up` / `popup`）

**HeadUnitCameraSystems**（全 276 頁 0 命中之關鍵詞）：

- `camera transition`（補掃單詞 `transition` 僅得 p.21 / p.27 / p.91 三頁）

### 4.3 其他 0 命中之交叉查核

- `HeadUnitCameraSystems` 全 276 頁，寬鬆樣式 `volume[\s_\-]*pop[\s_\-]*up`：**0 命中**。
  （非下放包指定項目，為 b01 `VOLUME POP_UP` 議題順帶查核，一併記錄。）

### 4.4 已列出但不在 `spec-index/sources/` 之被引文件

- `Pop-up List Notification`（Pop Up List Priority Matrix p.3 逐字引用之外部文件名）。
  已對 `spec-index/sources/` 33 件全表比對，**無同名或近名檔**。
  本檔僅具名記錄此缺口，**不判其為應取素材，不代擬 DATA_REQUEST 條文**。

---

## §5 複驗指令

```bash
cd /Users/peihe/Work_Projects/TC_Generator
shasum -a 256 "spec-index/sources/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf"
shasum -a 256 "spec-index/sources/HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf"
python3 features/ics_management/scripts/src_recon_04.py > /tmp/recon04.json
pdftotext -layout "spec-index/sources/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf" - \
  | grep -inE "volume|mute|duration|audio|vol"   # 預期 exit code 1（無命中）
```

腳本 `src_recon_04.py` 為唯讀：不寫入任何檔，僅將結構化結果輸出至 stdout。
