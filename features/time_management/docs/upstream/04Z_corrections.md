# 上繳 04Z — 兩節：04Z（R-TM33/34、G-TM2、A-TM21、verify_structure 評估）＋ 04Z-A1（快照保全、git 歸屬明答）

執行層 → 分析層。2026-08-21。執行順序依 `04Z-A1` §5：
先 `04Z-A1` T1（保全，最急），再 `04Z` T1–T6，最後 `04Z-A1` T3。

**兩項先講**：`verify_structure()` 之評估結果使 **A-TM21(b) 降級**
（保護實際存在，缺的只是 docstring 誠實性）；git 歸屬之明答為 **(a)**。

---

# ═══ 第一節：04Z-A1 ═══

## 1. T1 — `scripts/` 快照保全（R-TM35）

**先於 `04Z` 任何步驟執行。** 來源端全程唯讀。

### 1.1 來源狀態（複製前）

```
7344b995d0b4faf244894c867fa13fc35df1794590c12f4efb235b06bd58c466  build_batch_context.py   2026-08-21 09:15:18
a1626e4c9062cd20669aa6b2ab37ae25f834350d9c40a721742fc1638e880b5a  lint_tcs.py              2026-08-21 09:13:36
b7fb2aab13e1e749e474f0cb5df3b5a34a2f48a5c5e290d0a641562de7416c2c  write_back.py            2026-08-21 09:14:32
```

### 1.2 複製後 SHA256 —— **三支逐支相同**

```
7344b995…58c466  data/scripts_snapshot_20260821/build_batch_context.py
a1626e4c…e880b5a  data/scripts_snapshot_20260821/lint_tcs.py
b7fb2aab…7416c2c  data/scripts_snapshot_20260821/write_back.py
```

### 1.3 來源 mtime 複驗 —— **未變**

```
09:15:18  scripts/build_batch_context.py
09:13:36  scripts/lint_tcs.py
09:14:32  scripts/write_back.py
```

**凍結之 mtime 證據鏈未被破壞。** `cp -p` 使快照亦保留同一 mtime，
故快照與來源在時間上可對齊。

`README.md` 已載混合來源（哪一支是本 session 之產出、哪兩支不是、
本 session 原產出已失落無備份）、為何用複製而非 commit、以及
A-TM20 / A-TM21 / G-TM1 / G-TM2 之連結。`SOURCE_STATE.txt` 為 §1.1 全文。

### 1.4 執行層接受本條對其原提議之修正

原提議「單獨開 commit 收進三支」會將另一 session 之產出納入版本史並附
commit 作者 —— **那正是執行層排除 `scripts/` 於 `34e2da6` 之同一理由**。
自相矛盾之處由 R-TM35 指出，接受。複製無此問題且不必等待。

## 2. T3 — git 歸屬之明答：**(a) 依 Pei 指示**

**擇一明答：(a)。** 四次 `git commit`（`5fb0713`、`2062acb`、`4b00d33`、
`34e2da6`）全部發生於 **Pei 於聊天層直接輸入 `git commit` 之後**，
執行層從未自行發起任何 git 寫入操作。

### 2.1 執行層對「不動 git」之理解（供分析層核對）

| 來源 | 效力 |
|---|---|
| 下放包「不得執行者」之「不動 git」 | **分析層之指令不授權執行層動 git** |
| Pei 於聊天層之直接輸入 | **Pei 之直接指示，為 git 操作之唯一授權來源** |

二者不衝突：前者約束的是「分析層指令能授權什麼」，後者是常設分工中
「git 屬 Pei」之行使。**下放包無權授權 git 操作，亦無權撤銷 Pei 之直接
指示。**

此理解與本專案 `CLAUDE.md` 之既有規則一致：

> ❌ 不要自動執行 git commit
> ❌ 除非使用者明確要求，否則不要執行 git commit 或 git push

執行層每次皆待 Pei 明確輸入後才執行，且四次皆未 push
（`git push` 從未執行，分支現 ahead 14）。

**故無 A-TM22 之登記需要。** 若分析層認為上述理解仍有偏差，請明示，
執行層改依新界線。

### 2.2 一項執行層之補充

`34e2da6` 之 commit message 由執行層草擬，Pei 未逐字審閱即由執行層送出。
**若「依 Pei 指示」之範圍應限於「執行 commit 動作」而不含「決定 message
內容」**，則 message 之草擬屬執行層自裁，宜有明文。現行作法為：執行層
草擬、於回報中完整呈現、Pei 事後可要求改寫（未 push 故可重寫）。
**提請確認此作法是否即為所期。**

---

# ═══ 第二節：04Z ═══

## 3. T5 驗證（依 R-TM31，全部列明細）

```
R-TM33   RULINGS.md:1026      R-TM34   RULINGS.md:1058
R-TM35   RULINGS.md:1079      G-TM1    RULINGS.md:997
G-TM2    RULINGS.md:1104
A-TM21   ANOMALIES.md:33      | A-TM21 | 現存 write_back.py / lint_tcs.py 六項實質缺陷 | PENDING | Tier 2（凍結中不修）|
tc_id    feature.yaml:24      tc_id: "F"        # Test Case ID；R-TM34
tc_id_format  feature.yaml:50 tc_id_format: "NR1L-TimeAndDate-{n:03d}"   # R-TM32

R-TM 條數 38   期望 38（04Z 之 37 + R-TM35）   OK
G-TM 條數  2   期望 2                          OK
A-TM 條數 21   期望 21                         OK

scripts/ mtime（凍結證據，非 git status）
  09:15:18  build_batch_context.py
  09:13:36  lint_tcs.py
  09:14:32  write_back.py
```

三支 mtime 與 `04R` 上繳所記完全相同，**本包全程未動 `scripts/`**。

## 4. T3 — `feature.yaml` 之兩組快照（R-TM31：覆蓋可被發現）

| | SHA256 | mtime |
|---|---|---|
| 改前 | `868c84ea61ac3f468afecafa542e7f8aa3f5f05fa5ab705bcf93fcaca8e0606f` | 2026-08-21 09:42:01 |
| 改後 | `41b4efa5c8fbfedef5bdfe054428de5366a8fd24f186fefb69fbe1e2d5ba5a4d` | 2026-08-21 10:05:44 |

改前 mtime `09:42:01` 與執行層上次寫入該檔之時點一致（`04R` T3 加
`tc_id_format`），**無第三方於其間寫入之跡象**。

插入位置：`req_id: "D"` 之後（`workbook.columns` 段內），逐字
`    tc_id: "F"        # Test Case ID；R-TM34`。
`assert` + `count==1` + `replace(...,1)` 前置。

## 5. T4 — `verify_structure()` 唯讀評估：**A-TM21(b) 之缺口完全被涵蓋**

`backend/xlsx_surgical.py:250-278`，唯讀，未改。

### 5.1 其實際比對範圍 —— 三層

**第一層（`:252-259`）zip member 名稱集合**

```python
src_members, out_members = set(a.namelist()), set(b.namelist())
lost, added = sorted(src_members - out_members), sorted(out_members - src_members)
if lost or added:
    raise StructureError(...)
```

**第二層（`:261-266`）DV 計數 —— x14 下拉之實際保護點**

```python
before, after = _dv_counts(src), _dv_counts(out)
bad = {m: (before[m], after[m]) for m in before if before[m] != after[m]}
if bad:
    raise StructureError(f"data-validation counts changed (classic, x14): {bad}. ...")
```

此即 R-G3 之執行點：母本 R 欄 x14 擴充下拉若被 openpyxl 丟棄，
`x14` 計數由 1 變 0，此處 raise。

**第三層（`:268-275`）逐 member 內容比對 —— 決定性的一層**

```python
with zipfile.ZipFile(src) as a, zipfile.ZipFile(out) as b:
    differing = sorted(m for m in src_members if a.read(m) != b.read(m))
unexpected = [m for m in differing if m not in patched]
if unexpected:
    raise StructureError(f"members differ that were not written: {unexpected}. "
                         "Only the target sheets' XML may change")
```

**`a.read(m) != b.read(m)` 為逐 member 之位元組比對**，且限制「只有列於
`patched` 之 member 得有差異」。

### 5.2 A-TM21(b) 之判定：**完全涵蓋**

| | `check_other_sheets()` | `verify_structure()` 第三層 |
|---|---|---|
| 比對對象 | member **名稱集合** | member **內容**（位元組）|
| 涵蓋範圍 | 名稱變動 | 名稱變動（第一層）＋ 任何非預期之內容變動 |
| 對「內容改而名稱不變」 | **全綠** | **raise** |

且 `write_back.py:run()` 確實呼叫
`verify_structure(src, out, set(report["members_patched"]))`，
順序在 `check_other_sheets()` 之後 —— 前者通過與否不影響後者執行。

**結論：A-TM21(b) 所指之保護實際存在，且比 docstring 所承諾者更嚴格**
（`verify_structure` 連目標分頁以外之任何 member 內容變動都攔，
`check_other_sheets` 之 docstring 只承諾「目標分頁以外」）。

### 5.3 嚴重性降級與處置變更

依 `04Z` T4(3) 之判準：

- **降為「docstring 與實作不符」**，非「保護缺失」
- **處置由「補實作」改為「改 docstring 使其與實作相符」** ——
  或直接移除該函式（其功能已被 `verify_structure` 完全涵蓋，
  且其存在使讀者誤以為有第二道獨立檢查）

**G-TM2 項 2 之處置應據此調整。** 執行層**未自行改 G-TM2**（凍結中，
且條文修改屬分析層），提請於下一包訂正。

### 5.4 A-TM21(a) 不因此降級 —— 兩者不同

(a) 之 `resolve_columns()` 無任何其他機制涵蓋：`verify_structure` 保護的是
**檔案結構**，不驗**欄位對映是否取對**。若 `feature.yaml` 之字母與實例
表頭分歧，寫入會落在錯欄，而結構檢查全綠（錯欄仍在目標分頁內，
屬 `patched` 之 member）。

**(a) 維持「保護缺失」，G-TM2 項 1 不變。**

## 6. T6(5) — 該驗而未驗者（五全集）

### 6.1 依全集 1（指令逐項）

`04Z-A1` T1 / T3、`04Z` T1–T5 全數完成。T2（即 `04Z` 全體）已執行。

### 6.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + 五條位置 | 38；:997 / :1026 / :1058 / :1079 / :1104 |
| `ANOMALIES.md` | 條數 + A-TM21 索引位置 | 21；:33 |
| `feature.yaml` | 兩組 SHA/mtime + 兩處 tc_id 位置 | :24 / :50 |
| 快照 | 三支 SHA 逐支比對 + 來源 mtime | 相同；未變 |
| `scripts/` | mtime | 09:13–09:15，未動 |

四處 `str.replace` 全部前置 `assert` + `count==1`。

### 6.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **A-TM21 (a)(f) 之實跑證實** | 凍結中不執行。(b) 已由 T4 之讀碼評估**降級**，(a)(f) 仍為讀碼推得 |
| 2 | `_dv_counts()` 之實作 | **未讀** —— T4 只指派 `verify_structure`。其第二層之保護強度依賴該函式，未代為聲稱 |
| 3 | `patch_sheet_xml()` 之正確性 | 未讀。其為 `surgical_save` 之核心，但不在本包指派內 |
| 4 | `build_batch_context.py` 全文複查 | 執行層自己所寫，`04R` 起未再重讀 |
| 5 | A-TM05 / A-TM10 之實跑 | 續掛（需 drop folder 素材）|
| 6 | PU 陽性對照 | 待 Pei 裁 |
| 7 | A-TM12 / A-TM19 | 併後續批次 |

**第 2 項須說明**：§5.1 第二層之結論「此即 R-G3 之執行點」依賴
`_dv_counts()` 正確回報 classic 與 x14 兩者。該函式本包未讀，
故該句應讀為「**此處是 DV 保護之所在**」而非「**該保護經確認有效**」。
成本低（同檔案內），未獲指派故未讀。

### 6.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| 快照三支 SHA 與來源相同 | 三支 SHA 彼此互異，非全部相同之退化情形 | 有 |
| `scripts/` 未被本包寫入 | 同期 `feature.yaml` mtime 由 09:42 變 10:05，證明本包確有寫入能力 | 有 |
| A-TM21(b) 被 `verify_structure` 涵蓋 | (a) 經同一分析判定**未**被涵蓋 → 該分析非一律判涵蓋 | 有 |

### 6.5 依全集 5（設計說明之可驗性）

`04Z` §4 之 R-TM32 依據 1（canon §10.3）由分析層補驗並附原文 ——
**執行層未獨立複驗 canon 原文**。其三項確認（形式相符、alphanumeric
無長度限制、monotonically increasing）在邏輯上自洽，但依 R-TM4 之雙向
適用，該原文之引用本身仍為單方。**成本低（讀 canon §10.3 一節），
未獲指派故未做。** 不影響 R-TM32 之結論（另二項依據獨立支持）。

## 7. 本包未動之事項

未動 git（**未 push**；分支 ahead 14 之處置屬 Pei）。
**未寫入、未覆蓋、未修改 `features/time_management/scripts/` 任一行**
（mtime 09:13–09:15 為證；T1 為唯讀複製）。**未修 A-TM21 任何一項。**
**未改 `backend/` 任何檔**（T4 唯讀）。未執行任何腳本。未生成任何 TC。
未碰 `features/vehicle_setting/`。未 rm 任何檔案。未送出 RD-1。
未填 `D5`、未組 Scope 值。未以 openpyxl 存回任何工作簿。
**未自行修改 G-TM2**（§5.3 之訂正提請分析層處理）。
