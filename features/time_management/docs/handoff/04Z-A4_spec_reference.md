# 04Z-A4 — spec_reference 格式裁定（R-TM40）及其連鎖後果

分析層 → 執行層。追發包，依 R-TM20 聲明：所依賴之 `04Z-A3` 尚未上繳。
追發理由：本包之裁定**改變 `spec_reference` 之取值來源**，若待 A-3 上繳
後才下放，A-3 之 `backend/` 續讀結論不受影響，但 B1 之欄位內容設計會多
繞一輪。本包與 A-3 之 T1–T5 互不相依，可同 session 依序執行。

`scripts/` 仍凍結，本包不下放修改腳本之指令。

---

## 1. 裁定

```
R-TM40（Pei, 2026-08-21）—— spec_reference 之格式

specification_reference 欄之每一條目格式為：

    CFTS{doc_num}-{Source Requirement item id}

本 feature 之 doc_num = 015，item id 取自 SYS2 匯出之
`SYS2 來源需求項目ID  Source Requirement items` 欄（Basic Report 第 5 欄）。

例：CFTS015-4813905、CFTS015-4813974

不採 `<Spec Filename>_{outline}`（章節號）形式。
feature.yaml 之 spec_reference_template 隨之改寫。
```

## 2. 連鎖後果（六項，逐項須處置）

### 2.1 `spec_reference` 不再依賴章節錨鏈 —— A-TM12 降為非阻塞

原設計為 `leaf → SYS-RA → 物件 id → CFTS 章節號`，最後一段（物件 id →
章節號）需 docx 解析。**R-TM40 之取值止於物件 id，最後一段不再需要。**

故：

- **A-TM12**（037 無章節引用欄、`build_outline_map` 產空表）由
  「B1 之欄位內容阻塞」降為**非阻塞**。其 `recon.py` 修法（R-TM19 階段三）
  不再是 B1 之前置。
- 錨鏈之工作**不作廢**：`data/leaf_to_section_probe.txt` 之
  leaf → 章節對映仍為 framework Layer 3 之依據（Part VII §Layer 2/3
  之主軸章節表），且為 R-TM23 兩條界線之 spec 依據。
  **改變的是它不再是交付欄位之來源，而是 framework 導航之依據。**

### 2.2 多物件儲存格 → 多條目

`03R` 上繳已實測：5 筆 SYS-RA 之 `Source Requirement items` 為多物件
儲存格（逗號／換行分隔），例
`SYS-RA-154 → '4814113,\n4814114,\n4814115,\n4814116'`。

canon §10.7 明訂 `specification_reference` 為 string list，
允許多條目（先例：R-VS14）。故該類展開為多條目：

```
CFTS015-4814113
CFTS015-4814114
CFTS015-4814115
CFTS015-4814116
```

**排序**：canon §10.7 之「most-specific → general」在本格式下無章節層級
可比，改採**物件 id 數值遞增**，使同一 leaf 之條目順序具決定性
（SWE.6 之可重現性要求）。

### 2.3 一片 leaf 之條目來自其全部 SYS-RA 引用

037 之每片 leaf 引用數筆 SYS-RA（`#SYS-RA` 欄，1–6 不等），
每筆 SYS-RA 對應一或多個物件 id。故一片 leaf 之 `spec_reference`
為**其全部引用之物件 id 之聯集**，去重後依 §2.2 排序。

**但 §10.7 另有拘束**：「List every spec section the TC directly verifies
or relies on as setup」「Do NOT cite specs only used as background context」。
故一片 leaf 產生多條 TC 時，**各 TC 只列該 TC 實際驗證之物件**，
非該 leaf 之全部物件。leaf 層之聯集是上限，非每條 TC 之預設值。

### 2.4 A-TM13 之兩片 —— **仍然阻塞，且理由變得更尖銳**

`SYS-RA-221 → 6151328`、`SYS-RA-224 → 6151331`，兩物件於 CFTS015
SR26（20250909-1851）全檔零命中（`615\d{4}` 形態零命中，本檔物件 id
全為 `481xxxx` 區段）。

新格式下這兩筆**在字面上是可寫的** —— `CFTS015-6151328` 組得出來。
**但那會是一個我方已實測為偽之陳述**：該字串斷言物件 6151328 在
CFTS015 內，而我方量測結果是它不在。

```
R-TM41（分析層裁定，2026-08-21）—— A-TM13 兩物件不得寫入 spec_reference

CFTS015-6151328 與 CFTS015-6151331 不得寫入 specification_reference。

理由：R-TM40 之格式使該二字串在字面上可組出，但組出來即為一個
我方已實測為偽之斷言（該二物件於 CFTS015 SR26 全檔零命中）。
§8.4.1 禁止捏造來源未述之值；「格式湊得出來」不等於「來源有此內容」。

處置：`SWE-RA-TIME&DATE-005` 與 `-002` 之受影響 TC，其
specification_reference 只列該 TC 實際驗證且確實存在於 CFTS015 之物件；
缺口於 Remarks 宣告（G-TM1 項 3 之 spec gap 閘門）。

**兩片仍留在 B2，不因格式改變而移入 B1。** B1 之零 A-TM13 曝險設計
（03 §3）不變。
```

### 2.5 `feature.yaml` 之 `spec_reference_template` 改寫

現值 `"<Spec Filename>_{outline}"` 已不適用。改為：

```yaml
spec_reference_template: "CFTS015-{source_item_id}"   # R-TM40
```

### 2.6 lint 層新增一項閘門

`spec_reference` 之每一條目須：

1. 形式符合 `CFTS015-\d{7}`
2. 其 `\d{7}` 部分**存在於 SYS2 第 5 欄之全集**（即真有這個物件 id
   被本 feature 之需求引用）
3. 且**存在於 CFTS015 docx**（R-TM41 —— 擋掉 6151328／6151331 一類）

第 3 項與現存 `lint_tcs.py` 之 `lint_spec_reference`（驗物件 id 實際
存在於 docx）**方向相同** —— 該閘門是 G-TM2 項 6「不得回退」之一，
本裁定使其從「額外保護」升為「格式正確性之必要條件」。

**G-TM1 項 4 之界線閘門與本項並存，不互相取代。**

## 3. 一項提請 Pei 確認（格式細節）

`CFTS{doc_num}` 之 `doc_num` 寫法有二可能，**分析層不猜**：

| 寫法 | 例 | 依據 |
|---|---|---|
| 三位零填 | `CFTS015-4813905` | 檔名為 `CFTS _015`、spec 標題為 `CFTS_015 Time and Date`；且 CFTS015-806 一類之既有寫法見於本文件修訂註記 |
| 不零填 | `CFTS15-4813905` | 無依據，僅列出以示已考慮 |

**分析層採前者**（`CFTS015`），依據為 CFTS 文件自身修訂註記中之既有寫法
（`CFTS015-806`、`CFTS015-1203`、`CFTS015-1520` 等）—— 即該文件本身
就以 `CFTS015-` 為前綴指涉其需求物件。**若 Pei 另有指定請明示**，
B1 生成前改之無成本。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM40 / R-TM41

標題行 `## R-TM40 — spec_reference 之格式`、
`## R-TM41 — A-TM13 兩物件不得寫入 spec_reference`，
內文為 §1 / §2.4 之區塊全文，並將 §2.1–§2.3、§2.5、§2.6 之連鎖後果
以「R-TM40 之連鎖後果」小節附於 R-TM40 條文之下。

追加後 `## R-TM` 條數應為 **44**（A-3 之 42 + 2）。
**若 A-3 尚未執行，則為 40 + 2 = 42，並於上繳註明兩包之執行順序。**

### T2 — `feature.yaml`：改 `spec_reference_template`（§2.5）

改前後各記 mtime 與 SHA256（R-TM31）。

```
改前：spec_reference_template: "<Spec Filename>_{outline}"
改後：spec_reference_template: "CFTS015-{source_item_id}"   # R-TM40
```

`assert` + `count==1` + `replace(...,1)`，改後複查該行。

### T3 — `ANOMALIES.md`：A-TM12 降級註記

於 A-TM12 條文末尾追加：

```markdown
**降為非阻塞（2026-08-21，依 R-TM40）**

spec_reference 之取值改為 `CFTS015-{Source Requirement item id}`，
止於物件 id，不再需要「物件 id → 章節號」之 docx 解析。
故本條由「B1 之欄位內容阻塞」降為**非阻塞**，其 recon.py 修法
（R-TM19 階段三）不再是 B1 之前置。

錨鏈工作不作廢：`data/leaf_to_section_probe.txt` 仍為 framework
Layer 3 主軸章節表之依據，亦為 R-TM23 兩條界線之 spec 依據。
改變者為其角色 —— 由交付欄位之來源，改為 framework 導航之依據。
```

**A-TM 條數不變。**

### T4 — 產出逐 leaf 之 `spec_reference` 候選表（唯讀，R-TM4：列全集不列計數）

```bash
python3 - <<'PY' > features/time_management/data/spec_reference_candidates.txt
# ported from 04Z-A4 T4 under R-TM33; analysis round 04Z-A4
import re, openpyxl, pathlib, zipfile, html
F = pathlib.Path("features/time_management/inputs")
a03  = next(F.glob("SWE1*.xlsx"))
sys2 = next(F.glob("SYS2*.xlsx"))
docx = next(F.glob("*.docx"))

# CFTS 物件 id 全集（用於 R-TM41 之存在性判定）
xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
paras = ["".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
         for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S)]
blob = html.unescape(re.sub(r"<[^>]+>", "", "\n".join(paras)))
in_docx = set(re.findall(r"\b(\d{7})\b", blob))

wb = openpyxl.load_workbook(sys2, read_only=True, data_only=True)
n2src = {}
for r in wb["Basic Report"].iter_rows(min_row=2, values_only=True):
    m = re.search(r"-(\d{3})\s*$", str(r[1] or ""))
    if m:
        n2src[int(m.group(1))] = [x.strip() for x in
                                  re.split(r"[,\n]+", str(r[4] or "")) if x.strip()]
wb.close()

wb = openpyxl.load_workbook(a03, read_only=True, data_only=True)
for r in wb["Analysis Report"].iter_rows(min_row=9, values_only=True):
    if not r[0]:
        continue
    t = str(r[1]).replace("\u2013", "-").replace("\u2014", "-")
    nums = set()
    for a, b in re.findall(r"(\d{3})\s*-\s*(\d{3})", t):
        nums |= set(range(int(a), int(b) + 1))
    nums |= {int(n) for n in re.findall(r"\d{3}", re.sub(r"\d{3}\s*-\s*\d{3}", "", t))}
    ids = sorted({i for n in nums for i in n2src.get(n, [])})
    ok  = [f"CFTS015-{i}" for i in ids if i in in_docx]
    bad = [f"CFTS015-{i}" for i in ids if i not in in_docx]
    print(f"{str(r[0]).strip()}")
    print(f"    OK ({len(ok)}): {', '.join(ok)}")
    if bad:
        print(f"    BLOCKED (R-TM41): {', '.join(bad)}")
wb.close()
PY
cat features/time_management/data/spec_reference_candidates.txt
```

回報全 22 列。**期望**：`BLOCKED` 只出現於
`SWE-RA-TIME&DATE-005`（`CFTS015-6151328`）與 `-002`（`CFTS015-6151331`），
其餘 20 片全數 OK。**若出現第三片 BLOCKED，回報並停** —— 那代表
A-TM13 之範圍比既有記載大。

### T5 — 驗證（依 R-TM31，列明細）

```bash
grep -n '^## R-TM4[01]' features/time_management/RULINGS.md
grep -n 'spec_reference_template' features/time_management/feature.yaml
grep -n '降為非阻塞' features/time_management/ANOMALIES.md
grep -c '^## R-TM' features/time_management/RULINGS.md
grep -c 'BLOCKED' features/time_management/data/spec_reference_candidates.txt   # 期望 2
stat -f '%Sm %N' -t '%H:%M:%S' features/time_management/scripts/*.py
```

末項期望仍為 **09:13:36 / 09:14:32 / 09:15:18**。

### T6 — 上繳

`docs/upstream/04Z-A4_corrections.md`。須含 T5 全部輸出、T4 之 22 列全表、
T2 之兩組 SHA/mtime、**本包是否仍有該驗而未驗者之獨立判斷**。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不寫入、不修改 `scripts/` 任一行**（A-TM20 凍結）
- 不改 `backend/`
- 不生成任何 TC
- **不將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位**（R-TM41）
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 5. 呈報 Pei

1. **`CFTS015` 之零填寫法**（§3）—— 分析層採三位零填，依據為 CFTS 文件
   自身修訂註記之既有寫法（`CFTS015-806` 等）。若另有指定請明示。
2. **`features/time_management/` 之歸屬** —— 第六次。
   本裁定不論由哪一方持有皆適用，已可併入交接單。

## 6. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM40 | 裁決（Pei），spec_reference 格式 | §1 + §2 | ✅ T1 + T2 |
| R-TM41 | 分析層裁定，A-TM13 兩物件不得寫入 | §2.4 | ✅ T1 + T4 |
| A-TM12 降為非阻塞 | anomaly 註記，條數不變 | §2.1 | ✅ T3 |

分析層本包未動 git、未改任何腳本、未觸 `scripts/`、未改 `backend/`。
