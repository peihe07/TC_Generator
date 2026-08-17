# B1 — `Test Case Framework` 分頁判讀（R-P92 / G68）

> 全程以 `zipfile` 直讀 `xl/*.xml`，**未經 openpyxl，未呼叫 `save()`**（R-G3）。

## 1. 為何本包才讀

該分頁自 01 包起即在交付標的內（A-PW56）。前十一包皆未讀取，本包依 R-P92 補讀。**「十一包未讀」本身為一項教訓，已登記於 A-PW56。**

## 2. 實測

| 項目 | 實測值 |
|---|---|
| XML part | `xl/worksheets/sheet8.xml` |
| part 位元組 | **1,024** |
| 分頁狀態 | `visible`（**非隱藏**）|
| `<dimension ref>` | `A1` |
| `<sheetData/>` 為空元素 | **是** |
| **非空儲存格數** | **0** |
| `_rels` 檔存在 | **否** |
| `<drawing>` 節點 | 0 |
| `dataValidation` 節點 | 0 |

### part 全文（1,024 bytes 以內，逐字）

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="x14ac xr xr2 xr3" xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr2="http://schemas.microsoft.com/office/spreadsheetml/2015/revision2" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" xr:uid="{00000000-0001-0000-0700-000000000000}"><dimension ref="A1"/><sheetViews><sheetView showGridLines="0" zoomScaleNormal="100" workbookViewId="0"/></sheetViews><sheetFormatPr baseColWidth="10" defaultColWidth="8.83203125" defaultRowHeight="15"/><sheetData/><phoneticPr fontId="3" type="noConversion"/><pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/></worksheet>
```

## 3. 三本工作簿之分頁清單

| # | Power | Comfort | Privacy |
|---|---|---|---|
| 1 | `Cover_old`（隱藏） | `Cover_old`（隱藏） | `Cover_old`（隱藏） |
| 2 | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） | `ChangeHistory_old`（隱藏） |
| 3 | `Cover 封面` | `Cover 封面` | `Cover 封面` |
| 4 | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` | `ChangeHistory 修訂履歷` |
| 5 | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` | `Product Document 記錄封面頁` |
| 6 | `Test Case Specification&Result` | `Test Case Specification 測試用例規範` | `Test Case Specification 測試用例規範` |
| 7 | `Reference`（隱藏） | `Reference`（隱藏） | `Reference`（隱藏） |
| 8 | `Test Case Framework` | `QS Suggestion`（隱藏） | `QS Suggestion`（隱藏） |
| 9 | `QS Suggestion`（隱藏） | `下拉選單`（隱藏） | `下拉選單`（隱藏） |
| 10 | `下拉選單`（隱藏） | — | — |

Power **10** 分頁、Comfort **9**、Privacy **9**。
**`Test Case Framework` 為 Power 獨有**，Comfort / Privacy 皆無同名分頁。

## 4. G68 —— 與 §E 之衝突判定

判定式：該分頁若載有 Test Group / Test Set 之名稱或列數，即構成第二個
權威來源，與 §E 之 63 / 24 / 16 / 8 / 3 = 114（R-P35）併存而生衝突，
應觸發停止條件。

**實測非空儲存格 0**。分頁內無任何字元資料、無公式、無資料驗證、
無繪圖、無 `_rels`。故：

> **G68 = PASS（不衝突）。該分頁不構成權威來源。§E 未動、R-P35 未受影響。**

依 R-P92 之明令，**未因該分頁自行調整 §E**。

## 5. 附帶觀察（不改變上述結論）

該分頁為空、可見、且僅 Power 獨有。三種可能：範本演進殘留、
預留未填、或由他人自 Power 之上游範本帶入。**執行層無資料可判別，
不臆測**，登記為觀察。此點不影響 G68 之結論 —— 空即為空。
