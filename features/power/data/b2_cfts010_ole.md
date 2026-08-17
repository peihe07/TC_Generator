# B2 — CFTS010 之 OLE2 目錄清點（R-P48 / G30）

檔案：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658.doc`（245,248 bytes，OLE2）

> 依 **R-P48**：R-P39「不得解 RTF」指不解析 RTF **內容**，不涵蓋檢視 OLE2 之 storage 目錄結構。
> **本檔只列目錄項（名稱、型別、大小），未讀任何 stream 之內容位元組。**
> `olefile` 未安裝；依 CLAUDE.md「優先用內建函式庫」，以標準函式庫自行解析 MS-CFB 之標頭、FAT 與目錄鏈（`scripts/build_ole_census.py`），解析範圍僅及目錄樹。

## 1. 容器標頭

| 項目 | 值 |
|---|---|
| sector size | 512 bytes |
| mini sector size | 64 bytes |
| FAT 扇區數 | 4 |
| DIFAT 延伸 | 無（109 筆表頭內 DIFAT 已足） |

## 2. 目錄項總計

| 型別 | 數量 |
|---|---|
| stream | **10** |
| storage | **3** |
| root | **1** |
| **合計** | **14** |

## 3. 全部目錄項

| 名稱 | 型別 | 大小 (bytes) |
|---|---|---|
| `Root Entry` | root | 896 |
| `MsoDataStore` | storage | 0 |
| `ÂOÒÖKØ3IJÔÂÆÒQ0ÆÌÀ1KÄÐ==` | storage | 0 |
| `ÐÎD×F4DMKÄGÎÓ2ÃQS11UÊA==` | storage | 0 |
| `\x01CompObj` | stream | 114 |
| `\x05DocumentSummaryInformation` | stream | 7,416 |
| `\x05SummaryInformation` | stream | 4,096 |
| `1Table` | stream | 17,067 |
| `Data` | stream | 36,952 |
| `Item` | stream | 15,651 |
| `Item` | stream | 219 |
| `Properties` | stream | 201 |
| `Properties` | stream | 201 |
| `WordDocument` | stream | 156,320 |

## 4. 疑似嵌入物件

| 判準 | 數量 |
|---|---|
| `ObjectPool` storage 是否存在 | **否** |
| 名稱以 `_` 起始之 storage（MS-DOC 之物件容器慣例） | **0** |
| `\x01Ole` / `\x01CompObj` / `\x01Ole10Native` 等 OLE 標記 stream | 1（其中 root 層之 `\x01CompObj` 為容器自身之標記，任何 OLE2 文件皆有，非嵌入物件） |
| 其中 `\x01Ole`（每個嵌入 OLE 物件必有一個） | **0** |

## 5. 與 05 包下界之對照（G30）

| 來源 | 數量 |
|---|---|
| 05 包下界（`textutil -convert html` 之 `WrapperResource` 字樣） | **15** |
| 本包上界（OLE2 目錄之嵌入物件容器） | **0** |
| 差額 | **-15** |

### 差額成因

**OLE2 容器內無任何嵌入物件容器**（無 `ObjectPool`、無 `\x01Ole` 標記 stream、無 `_`-起始之物件 storage）。

即 CFTS010 之 15 處 `WrapperResource` 與 CFTS009 之 16 處**性質相同**：
**皆為純字面文字之懸空參照，非嵌入物件之錨**。

上界 0 < 下界 15 並非矛盾 —— 二者量的不是同一件事：
下界 15 量的是**文字層中的參照字樣**，上界 0 量的是**容器中實際存在的嵌入物件**。
兩數併觀所得之結論即 **A-PW23 之訂正形態**：參照存在，而其所指之資源不存在於交付文件中。

**故 CFTS010 之嵌入物件數為 0，此為確定值而非下界。**
