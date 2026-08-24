# x14 下拉之修復與驗收（W-168，58 輪）—— A-VS153

> **本檔為新建。** 87 包 §3 載「其驗收指令已備於 `x14_fix_prep.md`（41 輪）」——
> **該檔於 repo 不存在**；41 輪之內容在 `docs/upstream/41_writeback.md` §2.2。
> 本檔自該節取其實質，依**現行 243 列**更新，並補其未涵蓋之項（見 §3）。

母本：`c72b95560cefb06e94380e795ac6e1eff0c23546f817509060c116314be1221c`
分頁：`Test Case Specification 測試用例規範`（`xl/worksheets/sheet6.xml`）
資料列：**10–252**（243 列）

---

## 1. 現況（本輪實測）

| 項 | 現值 | 應有 |
|---|---:|---|
| `x14:dataValidation`（擴充） | **0** | **2**（41 輪實測之原值） |
| 一般 `dataValidation` | 4 | 4 |

**R 欄（Design Method）之下拉已不存在。** 其為 48 輪以 openpyxl 存檔時失去
（openpyxl 之已知限制：`Data Validation extension is not supported and will be removed`）。
本 repo 其後改採外科式 emit（**R-VS70**），**不會再失之，亦不會將其復原**。

**資料本身不受影響** —— R 欄 243 列全數落在受控 9 值內
（`selfcheck_w53.py` 之 `CONTROLLED_DOMAIN` 每輪驗之，出域 0）。

## 2. 修復（屬 Pei，於 Excel 內為之）

1. 開啟母本，切至 `Test Case Specification 測試用例規範`
2. 選取 **`R10:R252`**
3. 資料 → 資料驗證 → 清單，來源 **`=Reference!$C$4:$C$12`**
4. 存檔（**以 Excel 存，不得以 openpyxl**）

> `Reference` 分頁為隱藏分頁（`state="hidden"`），其存在已確認。
> **範圍之沿革**：原始為 `R10:R132`；41 輪建議 `R10:R152`（其時 143 列）；
> **現行須為 `R10:R252`**（243 列）。

## 3. **同一分頁另有三處下拉亦僅至第 132 列**（本輪新測，41 輪未涵蓋）

| `sqref` | 欄 | 涵蓋 | 缺 |
|---|---|---|---|
| `P10:P132` | P（Priority） | 列 10–132 | **列 133–252** |
| `Q10:Q11` | Q | 列 10–11 | —（其本即二列） |
| `T10:Z132` | T–Z | 列 10–132 | **列 133–252** |

**P 欄之受控值域與 R 欄同屬交付檢查之標的**（`selfcheck_w53.py` 檢 P1/P2、
R-VS56 檢其所依類別），**而其下拉自第 133 列起不存在**。

**本層不改**（禁區：不改動母本；且 R-VS70 禁 openpyxl 存檔，
一般 `dataValidation` 之範圍亦不得以 raw XML 手改 —— A-VS153 即該教訓）。

**88 包 §2.2 已裁定併入 A-VS153**：

```
修復範圍併為 `R10:R252` ＋ `P10:P252` ＋ `T10:Z252`。
```

> **「檢查驗的是 JSON 裡的值，不是工作簿裡有沒有讓人選對值的機制。」**（88 包 §2.2）

其來源沿用各欄現行之公式。**三者須一併修，A-VS153 方得關閉。**

## 4. 修復後之驗收判準

```bash
cd features/vehicle_setting
python3 - <<'PY'
import zipfile, re, sys
sys.path.insert(0, 'scripts')
from writeback_036 import BOOK
with zipfile.ZipFile(BOOK) as z:
    d = z.read('xl/worksheets/sheet6.xml')
print('x14:dataValidation 計數 :', d.count(b'<x14:dataValidation'), ' (須 >= 2)')
for m in re.finditer(rb'<x14:dataValidation.*?</x14:dataValidation>', d, re.S):
    b = m.group(0)
    sq = re.search(rb'<xm:sqref>([^<]+)</xm:sqref>', b)
    f1 = re.search(rb'<xm:f>([^<]+)</xm:f>', b)
    print('  sqref =', sq.group(1).decode() if sq else '—',
          '| 來源 =', f1.group(1).decode() if f1 else '—')
print('一般 dataValidation :')
for m in re.finditer(rb'<dataValidation [^>]*sqref="([^"]+)"', d):
    print('  ', m.group(1).decode())
PY
```

**三項須同時成立**：

| # | 判準 |
|---|---|
| 1 | `x14:dataValidation` 計數 **≥ 2** |
| 2 | 其 `xm:sqref` **涵蓋 `R10:R252`**（得為更大之範圍） |
| 3 | 其 `xm:f` 為 **`Reference!$C$4:$C$12`** |

**另（§3 若一併修）**：一般 `dataValidation` 之 `sqref` 含 `P10:P252` 與 `T10:Z252`。

## 5. 修復後之後續

1. 取新 sha256，記入 `DELIVERY.md` §6 之沿革
2. 重跑 `scripts/fullwrite2_w155.py` 之七項比對**不需要** ——
   本次修復由 Excel 為之，其為**基準之更新**，非本 repo 之寫回
3. **A-VS153 於三項判準全數成立後方得關閉**
