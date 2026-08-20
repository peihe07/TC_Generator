# 01Z-A2 — 指令集（R-TM8 / R-TM9-A1 / R-TM10-A1 / A-TM13 / A-TM14 之執行）

分析層 → 執行層。取代 `01Z_naming_rulings.md` §「執行層本包待辦」之
條列形式，該節之第 3、4 項已由 `01Z-A1_amendment.md` 作廢改寫。
本件為可直接執行之指令集。上繳仍寫入 `docs/upstream/01Z_corrections.md`。

## R-TM7 之履行聲明（哪些經實測、哪些沒有）

- `recon.py --feature` —— 已讀 argparse 實測（`recon.py:1090`）。本包不再用它
- `openpyxl` —— 已證存在（`recon.py` 匯入之且本 feature recon 實跑成功）
- **T4 之解析刻意只用 Python 標準庫（`zipfile` / `re` / `html`）**，
  不用 `python-docx`。分析層無法在該機實測其是否安裝，依 R-TM7
  不得假設；改用標準庫即無此問題
- `shasum` / `find` / `ls` —— macOS 內建，**分析層未在該機實測**。
  若不存在，以 `python3 -c "import hashlib…"` 代之並回報

---

## T0 — 工作目錄

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

## T1 — R-TM8：`feature.yaml` 之 `test_group`

手動編輯，逐字：

```
改前：test_group: "Time Management"           # [PROVISIONAL] 見 R-TM2；framework-internal; workbook write per profile
改後：test_group: "Time and Date"             # R-TM8；framework-internal; workbook write per profile
```

`feature:` 之值 **不動**，維持 `"Time Management"`（R-TM1）。
改完 `git diff` 確認只動這一行（**看，不 commit**）。

## T2 — A-TM14：Home v2 交付件之存在性舉證

```bash
ls -d features/home/output 2>/dev/null || echo "ABSENT: features/home/output"

find /Users/peihe/Work /Users/peihe/Work_Projects \
     -name "*Home_20260720*" -type f 2>/dev/null
```

- 命中 0 筆 → A-TM14 之「確已不存」成立，如實登記
- 有命中 → 對每一命中執行 `shasum -a 256`，與 FORMS.md 所載
  `cfc007f3…` 比對，**回報全 64 字元雜湊**，不得只報前 8 碼相符

**不論結果為何，本步驟都不得把任何檔案複製進本 feature 之 `inputs/`。**
是否採用該檔為樣式來源屬 R-TM10-A1 之解除條件，Pei 裁。

## T3 — R-TM9-A1：讀 archive 版 Home 之 `D5`（**只讀字面，不組值**）

```bash
python3 - <<'PY'
import openpyxl
p = ("archive/forms_superseded/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
     "STLA Test Case Specification & Result_SWQT_Home_20260809.xlsx")
wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
print("sheets:", wb.sheetnames)
for sn in wb.sheetnames:
    if "Test Case Specification" not in sn:
        continue
    ws = wb[sn]
    for row in ws.iter_rows(min_row=5, max_row=5, values_only=True):
        for i, v in enumerate(row, 1):
            if v not in (None, ""):
                print(f"  {sn} row5 col{i}: {v!r}")
wb.close()
PY
```

回報 `C5` 標籤與 `D5` 值之 **`repr()` 原樣**（含前後空白與換行），
並標出你認為前綴段與 feature 識別段之切分點。

**不得組成本 feature 之 D5 值，不得填入任何工作簿。**
切分經分析層覆核後才進下一步。A-TM11 維持 PENDING。

## T4 — A-TM13 + 錨鏈：對 `inputs/` 原始 docx 重跑

分析層之量測跑在 Project 附件之轉換文字副本，**非基線**。本步驟對原始
binary 重測，六項數字須逐項與下表對差。

期望值（分析層量測，沙箱副本）：

| # | 量 | 沙箱值 |
|---|---|---|
| 1 | SYS2 第 5 欄非空列數 / 總列數 | 227 / 227 |
| 2 | 78 筆被引用 SYS-RA 缺來源物件 id 者 | 0 |
| 3 | docx 章節標題數 | 88 |
| 4 | 物件 id → 章節之對映數 | 358 |
| 5 | 78 筆中直接可達 / 未直接可達 | 71 / 7 |
| 6 | 可達之相異章節數 | 21 |

```bash
mkdir -p features/time_management/scripts
python3 - <<'PY' > features/time_management/data/anchor_probe.txt
import zipfile, re, html, openpyxl, pathlib
F = pathlib.Path("features/time_management")
docx = next(F.joinpath("inputs").glob("*.docx"))
sys2 = next(F.joinpath("inputs").glob("SYS2*.xlsx"))
a03  = next(F.joinpath("inputs").glob("SWE1*.xlsx"))
print("docx :", docx.name)
print("sys2 :", sys2.name)
print("a03  :", a03.name)

# --- docx -> paragraph texts (stdlib only; no python-docx)
xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
paras = []
for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
    t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
    paras.append(html.unescape(re.sub(r"<[^>]+>", "", t)).strip())

HEAD = re.compile(r"^(\d+(?:\.\d+)*)\s+.*\{(\d+)\}$")
OBJ  = re.compile(r"^(\d{6,8})\s*:")
cur, obj2sec, nsec = None, {}, 0
for t in paras:
    if "\t" in t:                     # TOC rows carry a tab + page number
        continue
    m = HEAD.match(t)
    if m:
        cur, nsec = m.group(1), nsec + 1
        obj2sec.setdefault(m.group(2), cur)
        continue
    m2 = OBJ.match(t)
    if m2 and cur:
        obj2sec.setdefault(m2.group(1), cur)
print(f"[3] headings          : {nsec}")
print(f"[4] objects mapped    : {len(obj2sec)}")

# --- SYS2: SYS-RA number -> source requirement item id(s)
wb = openpyxl.load_workbook(sys2, read_only=True, data_only=True)
ws = wb["Basic Report"]
hdr = next(ws.iter_rows(min_row=1, max_row=1, values_only=True))
print("    SYS2 col5 header  :", repr(hdr[4]))
n2src, total, nonblank = {}, 0, 0
for r in ws.iter_rows(min_row=2, values_only=True):
    m = re.search(r"-(\d{3})\s*$", str(r[1] or ""))
    if not m:
        continue
    total += 1
    v = str(r[4] or "").strip()
    if v:
        nonblank += 1
    n2src[int(m.group(1))] = v
wb.close()
print(f"[1] SYS2 col5 nonblank: {nonblank} / {total}")

# --- 037 referenced SYS-RA numbers (range-expanded)
wb = openpyxl.load_workbook(a03, read_only=True, data_only=True)
refs = set()
for r in wb["Analysis Report"].iter_rows(min_row=9, values_only=True):
    if not r[0]:
        continue
    t = str(r[1]).replace("\u2013", "-").replace("\u2014", "-")
    nums = set()
    for a, b in re.findall(r"(\d{3})\s*-\s*(\d{3})", t):
        nums |= set(range(int(a), int(b) + 1))
    t2 = re.sub(r"\d{3}\s*-\s*\d{3}", "", t)
    nums |= {int(n) for n in re.findall(r"\d{3}", t2)}
    refs |= nums
wb.close()
print(f"    referenced ids    : {len(refs)}")
print(f"[2] refs lacking src  : {[n for n in sorted(refs) if not n2src.get(n)]}")

# --- resolve, splitting multi-object cells on comma / newline
direct, split_ok, unresolved, sections = [], [], [], set()
for n in sorted(refs):
    ids = [x.strip() for x in re.split(r"[,\n]+", n2src.get(n, "")) if x.strip()]
    hits = [obj2sec[i] for i in ids if i in obj2sec]
    if len(ids) == 1 and hits:
        direct.append(n)
    elif hits:
        split_ok.append((n, ids, sorted(set(hits))))
    else:
        unresolved.append((n, ids))
    sections |= set(hits)
print(f"[5] direct / needed split / unresolved : "
      f"{len(direct)} / {len(split_ok)} / {len(unresolved)}")
print(f"[6] distinct sections : {len(sections)}")
print("    split cells:")
for n, ids, hits in split_ok:
    print(f"      SYS-RA-{n:03d} -> {ids} -> {hits}")
print("    UNRESOLVED (A-TM13 candidates):")
for n, ids in unresolved:
    print(f"      SYS-RA-{n:03d} -> {ids}")
PY
cat features/time_management/data/anchor_probe.txt
```

回報：

1. 六項數字與上表逐項對差。**任一項不符即回報差異並停**，不得逕自
   採用新值 —— 沙箱副本與原始 binary 若在章節結構上不同，那本身是發現
2. `[5]` 之 split cells 逐筆列出（R-TM4：不得只給計數）
3. `[2]`／UNRESOLVED 之結果即 A-TM13 之舉證。分析層量測為
   `SYS-RA-221 → 6151328`、`SYS-RA-224 → 6151331`，兩者於 docx 命中 0。
   原始 binary 之結果須獨立確認
4. `data/anchor_probe.txt` 為證據檔，保留

**本步驟不產出 `leaf_to_section.tsv`**，不寫任何工作簿欄位。
錨鏈之正式建置待 A-TM12 之路線經 Pei 裁定後另行下放。

## T5 — 登記與索引

1. A-TM13（2 筆來源物件不在 CFTS 基線內）登記，PENDING，Tier 2 + RD-1 候選
2. A-TM14（Home v2 不在磁碟）登記，PENDING，Tier 2，附 T2 之舉證
3. R-TM8 / R-TM9 / R-TM9-A1 / R-TM10 / R-TM10-A1 逐字寫入 `RULINGS.md`
4. `DECISIONS.md` 建對應條目
5. 索引表 → **14 條**。A-TM11 維持 PENDING（R-TM9-A1）

## T6 — 上繳

`docs/upstream/01Z_corrections.md`，僅差異，不重述前包。須含：

- T1 之 `git diff` 片段（只該一行）
- T2 之 find 結果與（若有命中）全 64 字元雜湊
- T3 之 `repr()` 原樣與切分點提議
- T4 之六項對差 + split cells 逐筆 + UNRESOLVED 逐筆
- T5 之登記確認，索引 14 條
- **本包是否仍有該驗而未驗者之獨立判斷**，並明列盤點所用之全集

## 不得執行者

- 不 commit、不 tag、不動 git（全部 git 屬 Pei）
- 不複製任何檔案進 `inputs/`（T2 明列）
- 不填 `D5`、不組 Scope 值（R-TM9-A1）
- 不援引任何他 feature 樣式（R-TM10-A1 SUSPENDED）
- 不以 openpyxl 存回任何工作簿（母本 x14 DV；R18-3）
- 不跑 `recon.py`（本包無 recon 動作）

## 本包產生之新條文清單（自檢）

無新條文。本件為 R-TM8 / R-TM9-A1 / R-TM10-A1 與 A-TM13 / A-TM14 之
執行指令，不新增裁決。
