# CFTS004 原始文件 —— 引言句其後之列表（R-DIAG26 T1(c)）

來源：`cfts004_general_diag_20260608`（`sources/MANIFEST.tsv` 第 239 列，sha16 `f68f60837fe88851`）——
`R1LR_Atl-H_26PI2.5 Jun Release-…_CFTS_004_General Diagnostic Requirements_20260608-1145.docx`，
取自 `1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/SubSystem/Activation and Configuration/`。

---

## 結論（先講）

**引言句其後之「列表」不是表格，而是各自獨立、各有 ObjectID 的 FR 段落 —— 且全數已在索引匯出內。**
索引匯出（`sys2_cfts004_general_diag`）**沒有丟掉任何列表內容**。

CDD-10 審閱 §三與 A35 之前提（「引言句之列表是索引匯出丟掉的內容」）**與原始文件實測不符**，詳見下表逐句核對。

---

## 逐句核對

### $5000 —— 「The following tones shall be selectable in this DID」（文件內 2 處）

其後緊接 **14** 個 FR 段落，其中 **14** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4940285` | 是 | The 200 Hz, 120 mV tone - Tool controlled tone shall be selectable in this DID. |
| `4940286` | 是 | The 1 kHz, 120 mV tone - Tool controlled tone shall be selectable in this DID. |
| `4940287` | 是 | The 200 Hz Radio controlled tone shall be selectable in this DID. |
| `4940288` | 是 | The 200 Hz Tool controlled tone shall be selectable in this DID. |
| `4940289` | 是 | The 60 Hz Radio controlled tone shall be selectable in this DID. |
| `4940290` | 是 | The 60 Hz Tool controlled tone shall be selectable in this DID. |
| `4940291` | 是 | The 7 kHz Radio controlled tone shall be selectable in this DID. |
| `4940292` | 是 | The 7 kHz Tool controlled tone shall be selectable in this DID. |
| `4940293` | 是 | The Externally generated tone - input signal shall be applied to the AV1 analog audio input (aux). Note: this  |
| `4940294` | 是 | The Tones off option shall be selectable in this DID. |
| … | | 其餘 4 段同式 |

### $5001 —— 「The following speaker outputs shall be selectable using this DID」（文件內 1 處）

其後緊接 **5** 個 FR 段落，其中 **5** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4940302` | 是 | The Front Left speaker outputs shall be selectable using this DID. |
| `4940303` | 是 | The Front Right speaker outputs shall be selectable using this DID. |
| `4940304` | 是 | The Rear Left speaker outputs shall be selectable using this DID. |
| `4940305` | 是 | The Rear Right speaker outputs shall be selectable using this DID. |
| `4940306` | 是 | If the external source is selected for buzzer control (DID $5000), the radio shall provide a negative response |

### $2841/$2842/$2843/$2844 —— 「report the status of the following items as reported by the Sirius XM chipset」（文件內 7 處）

其後緊接 **16** 個 FR 段落，其中 **16** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4939808` | 是 | When requested by this DID, the HU shall report the status of the Signal Strength. The status can be either "N |
| `4939809` | 是 | When requested by this DID, the HU shall report the Tuner status. |
| `4939810` | 是 | When requested by this DID, the HU shall report the ENSA Lock status. |
| `4939811` | 是 | When requested by this DID, the HU shall report the ENSB Lock status. |
| `4939812` | 是 | When requested by this DID, the HU shall report the BER S1. |
| `4939813` | 是 | When requested by this DID, the HU shall report the BER S2. |
| `4939814` | 是 | When requested by this DID, the HU shall report the BER T. |
| `4939815` | 是 | When requested by this DID, the HU shall report the C/N S1A. |
| `4939816` | 是 | When requested by this DID, the HU shall report the C/N S1B. |
| `4939817` | 是 | When requested by this DID, the HU shall report the C/N S2A. |
| … | | 其餘 6 段同式 |

### $2812 —— 「report the following information as provided by the internal GPS receiver」（文件內 1 處）

其後緊接 **14** 個 FR 段落，其中 **14** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4939715` | 是 | When requested via this DID, the radio shall report the Date - Year as provided by the internal GPS receiver. |
| `4939716` | 是 | When requested via this DID, the radio shall report the Date - Month as provided by the internal GPS receiver. |
| `4939717` | 是 | When requested via this DID, the radio shall report the Date - Day as provided by the internal GPS receiver. |
| `4939718` | 是 | When requested via this DID, the radio shall report the Time - UTC - Hours as provided by the internal GPS rec |
| `4939719` | 是 | When requested via this DID, the radio shall report the Time - UTC - Minutes as provided by the internal GPS r |
| `4939720` | 是 | When requested via this DID, the radio shall report the Time - UTC - Seconds as provided by the internal GPS r |
| `4939721` | 是 | When requested via this DID, the radio shall report the Latitude as provided by the internal GPS receiver. |
| `4939722` | 是 | When requested via this DID, the radio shall report the Longitude as provided by the internal GPS receiver. |
| `4939723` | 是 | When requested via this DID, the radio shall report the GPS Fix as provided by the internal GPS receiver. |
| `4939724` | 是 | When requested via this DID, the radio shall report the Speed as provided by the internal GPS receiver. |
| … | | 其餘 4 段同式 |

### $2840 —— 「report the status of the following items:」（文件內 1 處）

其後緊接 **5** 個 FR 段落，其中 **5** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4939800` | 是 | When requested by this DID, the HU shall report the status of the Signal. The Signal status is reported as a s |
| `4939801` | 是 | When requested by this DID, the HU shall report the status of the Antenna. The Antenna status is reported as " |
| `4939802` | 是 | When requested by this DID, the HU shall report the status of the Satellite signal. The Satellite signal statu |
| `4939803` | 是 | When requested by this DID, the HU shall report the status of the Terrestrial signal. The Terrestrial signal s |
| `4939804` | 是 | When requested by this DID, the HU shall report the status of the Audio decoder bitrate. The Audio decoder bit |

### $280C —— 「The following data shall be readable from and writeable to this DID」（文件內 1 處）

其後緊接 **6** 個 FR 段落，其中 **6** 個在索引匯出內（**全數在內**）。

| ObjectID | 在索引匯出 | 原文（節錄） |
|---|:-:|---|
| `4939684` | 是 | The Clock Defeat data shall be readable from and writeable to this DID. The Clock Defeat shows the status of t |
| `4939685` | 是 | The Automated Loudness data shall be readable from and writeable to this DID. The Automated Loudness shows the |
| `4939686` | 是 | The Anti-Theft Enable Status data shall be readable from and writeable to this DID. The Anti-Theft Enable Stat |
| `4939687` | 是 | The 12/24 Time Selection data shall be readable from and writeable to this DID. The 12/24 Time Selection displ |
| `4939688` | 是 | The Front Seat Video Playback data shall be readable from and writeable to this DID. The Front Seat Video Play |
| `4939689` | 是 | The Cabin EQ Curve Number Currently Used By Radio shall be readable from and writeable to this DID. The number |

---

## 位元組編碼之查證（DR-DIAG-4／DR-DIAG-5 之關鍵）

對原始文件全文（262,103 字）之機械搜尋：

| 樣式 | 命中 |
|---|--:|
| `controlOptionRecord` | **0** |
| `controlEnableMask` | **0** |
| `byte <n>`（版面） | **0** |
| `bit <n>`（位元定義） | **0** |
| `0xXX` | **0** |
| `$XX` | 60 —— 全為 `$0307`／`$0309` 之 Indication Code 與 `$FF` padding，**已在索引匯出內** |

**原始文件不含任何位元組編碼或 record 版面。**
故 `DR-DIAG-4`（controlOptionRecord／controlEnableMask 全表）與 `DR-DIAG-5`（資料位元組值域與 record 版面）
**不可能由 CFTS004 解決** —— 該等編碼不在本文件之範圍內，須另求來源（DID 資料字典／CIP Radio Tables）。

---

## 索引匯出與原始文件之差集

| 方向 | 數 | 內容 |
|---|--:|---|
| 原始文件有、索引匯出無 | **410**（318 FR ＋ 92 Description）| 內部 cell modem 訊號／CDMA IMSI／HD Sub-channel 等 —— **未被 SYS2 收入本案範圍**之他 ECU／他機種要件。037（SWE1）自 SYS2 已收範圍導出，故不在母體（R-DIAG8(a)）|
| 索引匯出有、原始文件無 | **13** | 11 個 `Out of  Scope` 類（`$1801` 節之 loss-of-communication 要件）＋ 2 個 `$0301` 節之未引用列。其中 `SYS-RA-DIAG-248` 即本 feature 之 OOS 列 `-057`（`NR1L-DIAG-014`），已依 R-DIAG3(amend) 處置 |

## R-G67 嵌入物件檢查

docx 內共 32 個 part，嵌入媒體僅 `word/media/image1.png`（250×80，3,253 bytes）——
**Stellantis 商標圖**，無承載資料之嵌入物件（無 oleObject／無嵌入試算表）。

## 版本一致性（下放包 §5 條件 2）

原始文件與索引匯出之 ObjectID 空間相同（根節點 `4939389 General Diagnostic Requirements` 一致，
抽驗 `4939801`／`4940456` 皆在），**版本一致，條件 2 不命中**。
