# 05R — 階段 A 受理，四項條文訂正，階段 B/C 放行

分析層 → 執行層。覆核對象：`docs/upstream/05_gates.md`（第一部分）。
**階段 A 六項全部受理。** 依 T4 停下回報正確。

**兩項自我訂正**：A5 之紅向構造是我沒想清楚層序（§1）；
條數期望 45 是我跨未確認執行之包累積（§2）。

---

## 1. A5 紅向構造不可行 —— 我的錯，且定性正確

> A1 之表頭複驗會在 `resolve_columns()` 先 raise，執行根本到不了 G-TM3。
> 此非缺陷，是兩閘門之正確層序。

**完全正確。** 我在同一包內指派 A1（設定層攔截）與 A5（結果層攔截），
卻設計了一個必須「設定錯誤能通過」才觸發得到 A5 的紅向構造。
**兩者互斥，而我沒想到。**

改以函式層構造（`copy.deepcopy(cfg)` / 直接改 `cols` dict，不寫檔案）
是正解，且紅向 2（`cols["tc_id"]` 位移一格）**直接模擬 column 層位移**
—— 那正是 `verify_structure` 三層全綠之情形，證明 A5 抓得到。

```
R-TM45（分析層自裁，2026-08-21）—— 同包內多項修法之驗證構造須考慮層序

同一下放包內指派多項閘門時，各項之驗證構造須先確認**該構造不會被同包
其他閘門先行攔截**。

具體作法：列出各閘門之攔截時點（設定層 / 執行層 / 結果層），
若紅向構造之壞輸入會被較早之閘門攔下，該構造無效，須改在被測閘門
之函式層直接構造。

依據：05 T4 建議以「暫改 feature.yaml 之 columns.tc_id」觸發 A5，
而同包之 A1 為設定層複驗，會先 raise —— 兩者互斥。

附帶：閘門層序本身是設計良好之表現（設定錯誤在前攔，結果錯誤在後攔），
不因其使測試構造失效而視為缺陷。
```

## 2. 條數 47 vs 45 —— 我的期望值跨包累積

`05` T1 寫「期望 45（＝`04Z-A5` 之 43 + 2）」，而該 43 建立在
「`04Z-A4` 未執行」之假設上。執行層實際依 `04Z-A4` → `04Z-A5` → `05`
順序補做，得 47。**算術無誤，錯在我用絕對值表達期望。**

且執行層另發現 `04Z-A4` 亦未執行（其 R-TM40/41 為 `04Z-A5` T1(d) 所依賴）
—— **這是 R-TM20 之後果第二次出現**：我連發追發包，執行順序由執行層
自行推導。

```
R-TM46（分析層自裁，2026-08-21）—— 條數期望以增量表示

下放包之條數驗證判準一律以**增量**表示（如「本包後 `## R-TM` 應較執行前
增加 2」），不以絕對值表達，除非該絕對值之基數於同一包內實測取得。

理由：絕對值之基數來自前包之期望值，而前包是否執行、以何順序執行，
分析層在下放時不能確知（R-TM20 之情形）。基數一錯，驗證判準即失效，
且失效方式是「數字對不上」而非「發現真問題」——製造雜訊，掩蓋訊號。

依據：05 T1 期望 45，實際 47；差異全部來自 04Z-A4 是否已執行之假設。
```

## 3. A1 / A4 之二擇一 —— 兩項決定與理由皆受理

**A1 取實作複驗**，理由（「改 docstring 只是讓文件誠實，不消除該盲區」）
成立。紅向 2 以整體位移一格模擬 rev A/B → rev C 之實際漂移形態，
比單欄改動更貼近真實風險 —— **測試構造選得比我給的好**。

**A4 取「接上寫入」**，理由尤其值得記錄：

> S 欄為交付欄位，其值應由**條文**決定而非由 TC 資料決定。若移除該常數
> 而讓 `tc.get("functional_safety")` 決定，等於把欄位值之決定權下放給
> 生成端 —— 與 canon §10.3 對 tc_id 之處理精神相反。

**此推論正確且可一般化**：交付欄位若其值由條文固定，則該值不得經由
TC JSON 傳遞，否則生成端即取得該欄之實質決定權。tc_id 與
functional_safety 為同一形態。

**但此決定使一件事浮上檯面**（§5）。

## 4. 三項訂正

### 4.1 R-TM40 之依據 —— 改為 canon §10.7 Rules 第 2 條

執行層於 `04Z-A5` 上繳 §3.4 提請（本包 §6.3 項 4 記為未獲回覆）。
分析層複驗 canon §10.7 原文，其 Rules 段第 2 條為：

> Use the SourceID format from SYS1 / Polarion when available

**SYS2 之 `Source Requirement items` 欄即 Polarion SourceID。**
故 R-TM40 之正當依據為此句，而非 CFTS 文件內之寫法先例。

**提請成立，本包採納。** 此依據比原依據強 —— 它是 canon 對本格式之
明文授權，而非對文件慣例之推論。A-TM23 之「本專案新定之形式」一語
須隨之修正為「canon §10.7 明文允許之 SourceID 形式，惟文件內無同形寫法」。

### 4.2 R-TM43(a) 之「交付說明」落點 —— 本包指定

執行層指出 `05` §1 之 R-TM43(a) 寫「於交付說明註明」而未指定落點，
且該落點影響 B1 之 Remarks 設計（每列帶或僅首列帶）。**提請成立。**

```
R-TM47（分析層裁定，2026-08-21）—— R-TM43(a) 之落點

「本工作簿之 spec_reference 採 7 位物件 id 家族」之說明，
落點為 **docs/fw036/framework.md Part VII 之 `### Workbook sync` 節**。

**不寫入工作簿任何儲存格**，理由有二：
1. Remarks 欄（AH）已由 G-TM1 項 3 保留給 spec gap 宣告（A-TM13）。
   逐列註記編號家族會與缺口宣告混列，使兩種訊息互相稀釋。
2. 該說明為工作簿層級之事實，非逐列事實。逐列重複 22×N 次
   不增加資訊，且任一列漏寫即成不一致。

B1 之 Remarks 設計因此確定：**Remarks 只承載逐列事實**
（spec gap、BLOCKED 標示），不承載工作簿層級之說明。
```

### 4.3 A-TM23 之措辭修正

依 §4.1，A-TM23 條文中「`CFTS015-<7 位>` 之寫法於 CFTS015 全文出現 0 次，
故為本專案新定之形式，非沿用文件既有慣例」一句，其**前半（實測）保留**，
**後半（推論）修正** —— 該形式為 canon §10.7 明文允許之 SourceID 形式。
Q-TM4 之問法隨之調整（見 T4）。

## 5. **functional_safety 之值 —— A4 之決定使其成為新的實質阻塞項**

A4 既定「值由條文決定、不由 TC 資料決定」，則該值必須有一個裁定來源。
現況：`CONST_FUNCTIONAL_SAFETY = None`，標 `TODO(R-TM10-A1)`。

**但該標記掛錯了條文。** R-TM10-A1 管的是**跨 feature 樣式參照**
（步驟措辭、ER 句式、標點慣例）；functional_safety 是**交付欄位之內容值**，
不是樣式。掛在 R-TM10-A1 之下有兩個後果：

1. 它會隨 R-TM10-A1 之解除而被誤以為一併解決 —— 實則不會
2. 它使人以為「等到有樣式參照就能抄」—— 但抄他 feature 之
   functional_safety 值正是 R-TM10(b) 明列之**不得援引**（內容體系）

```
A-TM24（PENDING，Tier 2 —— B1 寫回前必決）

write_back.py 之 CONST_FUNCTIONAL_SAFETY 現為 None，標 TODO(R-TM10-A1)。

**標記掛錯條文**：R-TM10-A1 管跨 feature 樣式參照；functional_safety
為交付欄位之內容值。抄他 feature 之值屬 R-TM10(b) 明列之不得援引。

故本項不會隨 R-TM10-A1 解除而解決，須獨立裁定。

可用之來源，依優先序：
1. 母本 S 欄之 DV —— 若存在，值域即為候選集（Tier 1，可實測）
2. FM-WI-FSM-036-A01 之填寫規範或 SWQT 團隊之既定慣例（Tier 3，問 Pei）
3. 若二者皆無，屬範圍界定，Tier 2 → Pei 裁

**現況為安全的**：run() 之 unresolved 檢查會在 --write 前 raise，
故不會靜默寫入 None。但 B1 之寫回將因此被攔。

本包 T3 指派實測第 1 項。
```

---

## 6. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM45 / R-TM46 / R-TM47，並訂正 R-TM40 依據

三條標題行：

```
## R-TM45 — 同包內多項修法之驗證構造須考慮層序
## R-TM46 — 條數期望以增量表示
## R-TM47 — R-TM43(a) 之落點
```

內文為 §1 / §2 / §4.2 之區塊全文。

**R-TM40 之依據訂正**（於其既有之「依據訂正」段之後再追加，
依 R-TM13 不刪前文）：

```markdown
**依據再訂正（2026-08-21，依 04Z-A5 上繳 §3.4 之提請）**

本條之正當依據為 canon §10.7 Rules 第 2 條：
`Use the SourceID format from SYS1 / Polarion when available`。
SYS2 之 `Source Requirement items` 欄即 Polarion SourceID。

此依據強於前次所引之文件寫法先例 —— 它是 canon 對本格式之明文授權，
非對文件慣例之推論。前兩段之訂正記載保留（R-TM13）。
```

**驗證以增量表示（R-TM46）**：本包執行後 `## R-TM` 應較執行前 **+3**；
`## G-TM` 不變；`## A-TM` **+1**。

### T2 — `ANOMALIES.md`：新增 A-TM24，A-TM23 措辭修正

A-TM24 內容為 §5 之區塊全文，索引追加：

```markdown
| A-TM24 | functional_safety 之值未裁定，且 TODO 標記掛錯條文 | PENDING | Tier 2（B1 寫回前必決）|
```

A-TM23 條文中「故為本專案新定之形式，非沿用文件既有慣例」一句，
依 R-TM13 加刪除線保留，其下加：

```markdown
> **修正（2026-08-21，R-TM40 依據再訂正）**：該形式為 canon §10.7
> Rules 第 2 條明文允許之 SourceID 形式（`Use the SourceID format from
> SYS1 / Polarion when available`）。實測結論（文件內 0 次）不變，
> 但其意義為「文件內無同形寫法」，非「無依據」。
```

### T3 — 母本 S 欄 DV 實測（A-TM24 來源 1）

```bash
python3 - <<'PY'
# ported from 05R T3 under R-TM33; analysis round 05R
import zipfile, re, pathlib
wb = next(pathlib.Path("features/time_management/inputs").glob("*SWQT*.xlsx"))
z = zipfile.ZipFile(wb)
xml = z.read("xl/worksheets/sheet6.xml").decode("utf-8")
for m in re.finditer(r"<dataValidation\b([^>]*)>(.*?)</dataValidation>", xml, re.S):
    attrs, body = m.group(1), m.group(2)
    sqref = re.search(r'sqref="([^"]*)"', attrs)
    f1 = re.search(r"<formula1>(.*?)</formula1>", body, re.S)
    print("sqref:", sqref.group(1) if sqref else None,
          "| formula1:", (f1.group(1)[:120] if f1 else None))
# x14 擴充
for m in re.finditer(r"<x14:dataValidation\b.*?</x14:dataValidation>", xml, re.S):
    s = re.search(r"<xm:sqref>(.*?)</xm:sqref>", m.group(0), re.S)
    f = re.search(r"<xm:f>(.*?)</xm:f>", m.group(0), re.S)
    print("x14 sqref:", s.group(1) if s else None, "| f:", f.group(1) if f else None)
PY
```

回報：**S 欄（`functional_safety`）是否落在任一 DV 之 `sqref` 範圍內**；
若是，列出其 `formula1` 之完整值域。若否，明講「S 欄無 DV，來源 1 不成立」，
A-TM24 轉由來源 2/3 處理。

**唯讀，不得存回。**

### T4 — Q-TM4 措辭調整（依 §4.3）

`docs/fw036/RD1_questions_time_management.md` 之 Q-TM4，
將「為本專案新定之形式」改為
「依 canon §10.7 Rules 第 2 條（`Use the SourceID format from SYS1 /
Polarion when available`）採 Polarion SourceID 形式」。

`assert` + `count==1` + `replace(...,1)`，改後複查。**狀態仍 DRAFT。**

### T5 — 階段 B（八項）

依 `05` §3 階段 B 之表逐項實作，每項附 red-green（紅向須實跑）。
B7(iii) 之紅綠兩向必測。

**階段 B 完成後停下回報，不逕入階段 C。**

### T6 — 驗證（依 R-TM31 列明細；依 R-TM46 以增量表示）

```bash
grep -n '^## R-TM4[567]' features/time_management/RULINGS.md
grep -n '依據再訂正' features/time_management/RULINGS.md
grep -n '^| A-TM24' features/time_management/ANOMALIES.md
grep -n '修正（2026-08-21，R-TM40' features/time_management/ANOMALIES.md
grep -n 'SourceID' docs/fw036/RD1_questions_time_management.md
grep -n 'modified by TC_Generator analysis round 05' features/time_management/scripts/lint_tcs.py
```

條數以增量回報：`## R-TM` +3、`## A-TM` +1、`## G-TM` 0，
並附**執行前與執行後之兩個實測值**。

### T7 — 上繳

`docs/upstream/05R_corrections.md`。須含 T6 全部輸出、T3 之 DV 實測結果、
階段 B 八項之 red-green 實際輸出（標已實測／未實測）、
**本包是否仍有該驗而未驗者之獨立判斷**。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不執行階段 C**（待階段 B 覆核）
- 不生成任何 TC
- 不改 `backend/`
- **不對母本或任何工作簿存回**（T3 唯讀）
- 不刪除 `data/scripts_snapshot_20260821/`
- 不修改任何既有下放包或上繳包
- 不將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位
- 不填 `functional_safety` 之值（A-TM24 未決）
- 不碰 `features/vehicle_setting/`
- 不填 `D5`、不組 Scope 值
- 不送出 RD-1

---

## 7. 呈報 Pei

1. **A-TM24 —— `functional_safety` 之值。** A4 之決定（值由條文定、
   不由 TC 資料定）使此項成為 B1 寫回前之硬阻塞。T3 先測母本 S 欄有無 DV；
   若無，則需你裁（036 填寫規範或 SWQT 既定慣例）。
   **注意其 TODO 標記原掛在 R-TM10-A1 之下是錯的** —— 它不會隨樣式參照
   解除而解決。
2. **R-TM10-A1** 仍無候選，維持 SUSPENDED。步驟措辭常數與 ER 樣板
   仍為 B1 之另一阻塞項。
3. RD-1 Q-TM1–4 已備齊，送出屬你。
4. 分支 ahead 14 未 push。

## 8. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM45 | 分析層自裁，驗證構造之層序 | §1 | ✅ T1 |
| R-TM46 | 分析層自裁，條數期望以增量表示 | §2 | ✅ T1 + T6 |
| R-TM47 | 分析層裁定，R-TM43(a) 落點 | §4.2 | ✅ T1 |
| R-TM40 依據再訂正 | 改為 canon §10.7 Rules 第 2 條 | §4.1 | ✅ T1 |
| A-TM23 措辭修正 | 依 R-TM13 加註 | §4.3 | ✅ T2 + T4 |
| A-TM24 | anomaly，PENDING，B1 寫回前必決 | §5 | ✅ T2 + T3 |

分析層本包未動 git、未改任何腳本、未改 `backend/`。
