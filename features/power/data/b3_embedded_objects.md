# B3 — CFTS 本文嵌入物件清點（R-P39）

> 依 R-P39 與 05 §I：**不解 RTF、不改 R-P17 之文字層定義**。本檔只清點。
> 產生指令：`python features/power/scripts/build_b3.py`

## 1. 總計

| 文件 | 型別 | 數量 |
|---|---|---|
| CFTS009 `.docx`（OOXML） | `WrapperResource（文字層字樣）` | **16** |
| CFTS010 `.doc`（OLE2） | `<img>` | **0** |
| CFTS010 `.doc`（OLE2） | `<object>` | **0** |
| CFTS010 `.doc`（OLE2） | `WrapperResource（文字層字樣）` | **15** |

### CFTS009 之部件與關聯

- `word/embeddings/` 檔案數：**0**
- `word/media/` 檔案數：**1**
- `document.xml.rels` 之關聯型別分布：

| 型別 | 數量 |
|---|---|
| `header` | 3 |
| `footer` | 3 |
| `customXml` | 2 |
| `endnotes` | 1 |
| `numbering` | 1 |
| `footnotes` | 1 |
| `theme` | 1 |
| `webSettings` | 1 |
| `settings` | 1 |
| `fontTable` | 1 |
| `styles` | 1 |

> CFTS010 為 OLE2 `.doc`，無 OOXML 部件可查。上表之數量係以 `textutil -convert html` 輸出計得，為**下界**。

## 2. 含嵌入物件之章節


### CFTS009（8 章含嵌入物件）

| 章節 | 標題 | 物件 | 需求錨點數 | 非錨點內文字元數 |
|---|---|---|---|---|
| §1.3.1.1 | BODY OFF and BODY ON MODE GROUPS | `WrapperResource（文字層字樣）` ×2 | 7 | 1425 |
| §1.3.2 | ECU CAN Architecture Configuration (If E | `WrapperResource（文字層字樣）` ×1 | 1 | 226 |
| §1.3.3.5 | Power up Sequence | `WrapperResource（文字層字樣）` ×2 | 23 | 6481 |
| §1.6.2.1 | TLM algorithm requirements | `WrapperResource（文字層字樣）` ×2 | 2 | 101 |
| §1.6.4.1 | TLM algorithm requirements | `WrapperResource（文字層字樣）` ×4 | 29 | 4950 |
| §1.9.1 | Loss of Communication Behavior | `WrapperResource（文字層字樣）` ×1 | 8 | 5600 |
| §1.9.7 | Passenger Display Power Moding | `WrapperResource（文字層字樣）` ×2 | 4 | 139 |
| §1.9.16 | Contextual Theme | `WrapperResource（文字層字樣）` ×2 | 20 | 2691 |

### CFTS010（8 章含嵌入物件）

| 章節 | 標題 | 物件 | 需求錨點數 | 非錨點內文字元數 |
|---|---|---|---|---|
| §1.1 | Revision Notes | `WrapperResource（文字層字樣）` ×1 | 3 | 859 |
| §1.4.1.1 | Voltage Level Behavior | `WrapperResource（文字層字樣）` ×1 | 3 | 710 |
| §1.5.2.2.1.1 | System Voltage | `WrapperResource（文字層字樣）` ×2 | 2 | 112 |
| §1.5.2.2.1.2 | ECU Local Voltage | `WrapperResource（文字層字樣）` ×2 | 2 | 112 |
| §1.5.3.2.1.1 | System Voltage | `WrapperResource（文字層字樣）` ×3 | 4 | 168 |
| §1.5.3.2.1.2 | ECU Local Voltage | `WrapperResource（文字層字樣）` ×2 | 2 | 112 |
| §1.8.2.1.1 | System Voltage | `WrapperResource（文字層字樣）` ×2 | 2 | 112 |
| §1.8.2.1.2 | ECU Local Voltage | `WrapperResource（文字層字樣）` ×2 | 2 | 112 |

## 3. 文字層內容為空或近乎為空、卻含嵌入物件之章節

判準：該章之**非錨點內文字元數 < 200**，且含至少一個嵌入物件。

| 文件 | 章節 | 標題 | 非錨點內文字元數 | 需求錨點數 | 物件 |
|---|---|---|---|---|---|
| CFTS009 | §1.6.2.1 | TLM algorithm requirements | 101 | 2 | `WrapperResource（文字層字樣）` ×2 |
| CFTS009 | §1.9.7 | Passenger Display Power Moding | 139 | 4 | `WrapperResource（文字層字樣）` ×2 |
| CFTS010 | §1.5.2.2.1.1 | System Voltage | 112 | 2 | `WrapperResource（文字層字樣）` ×2 |
| CFTS010 | §1.5.2.2.1.2 | ECU Local Voltage | 112 | 2 | `WrapperResource（文字層字樣）` ×2 |
| CFTS010 | §1.5.3.2.1.1 | System Voltage | 168 | 4 | `WrapperResource（文字層字樣）` ×3 |
| CFTS010 | §1.5.3.2.1.2 | ECU Local Voltage | 112 | 2 | `WrapperResource（文字層字樣）` ×2 |
| CFTS010 | §1.8.2.1.1 | System Voltage | 112 | 2 | `WrapperResource（文字層字樣）` ×2 |
| CFTS010 | §1.8.2.1.2 | ECU Local Voltage | 112 | 2 | `WrapperResource（文字層字樣）` ×2 |

## 4. 與 G8 / G9 之交叉

| 指標 | CFTS009 | CFTS010 |
|---|---|---|
| 全部章節數 | 196 | 92 |
| 含嵌入物件之章節數 | 8 | 8 |
| 全部需求錨點數 | 904 | 148 |
| 落在含嵌入物件章節內之需求錨點數 | 94 | 20 |


## 5. 結論 —— 不是「藏在嵌入物件裡」，是「根本不在檔案裡」

CFTS009 `.docx` 之部件清單實測（`zipfile.namelist()`）：

- **無 `word/embeddings/` 目錄**（0 個檔案）
- `word/media/` 僅 `image1.png`（3,253 B），由 `header2.xml.rels` 引用，屬頁首圖
- `word/document.xml` 內 `w:object` / `w:drawing` / `w:pict` / `o:OLEObject`
  各 **0 個**
- `document.xml.rels` 之關聯型別中無 `oleObject`、無 `package`

即 `CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource` 這類字串
**是純字面文字**，不是任何嵌入物件的錨。它是 Polarion 匯出時留下的
**懸空參照** —— 其所指之 RTF 資源並未隨文件一同匯出。

**故 04 §九第 3 項之推測（「規格內容藏於文字層看不見之處」）方向正確但形態不同**：
內容不是看不見，是**不存在於交付文件之中**。

實測範圍：CFTS009 **16 處**、CFTS010 **15 處**，合計 **31 處**，
分布於 **16 個章節**（各 8 章）。其中 8 章之非錨點內文 < 200 字元，
即該章之可讀內容幾乎只剩這些懸空參照。

受影響最嚴重者為 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**
（非錨點內文 101 字元、2 個需求錨點、2 處懸空參照）——
該章正是 A-PW16 九章之一，且被九個 leaf 共同引用。
其兩個被引用錨點 `4941354` / `4941355` 之內文即為該二懸空參照，
故 B2 v2 判為「無法判定」。

**R-P39 之問題「G8 = 904 之規格覆蓋率有無上界保證」，答案為：**
904 個需求錨點本身完整存在於文字層；
但其中落在含懸空參照章節內者，其部分內容不可得。
本包依 R-P39 只清點，不解 RTF、不改 R-P17。
