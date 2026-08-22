# 24 上繳 —— 寫回已執行，G-TM3 正向驗證通過，交付說明落檔

執行層，2026-08-22。對應下放包 `docs/handoff/24_writeback.md`。

---

## 0. 逐 T 項對照表（R-TM74）

| T 項 | 內容 | 狀態 | 備註 |
|---|---|---|---|
| **T1** | dry-run（R-TM78） | **完成** | 六項全符，見 §1 |
| **T2** | 寫回 | **完成（一處偏離，已更正）** | 落點更正，見 §2 |
| **T3** | G-TM3 正向驗證 | **完成** | **PASS**，見 §3 |
| **T4** | 結構完整性複驗 | **完成** | member 48，見 §4 |
| **T5** | 交付說明落檔 | **完成** | DR 處數有變動，見 §5 |
| **T6** | 上繳 | **完成** | 本檔 |

**未做者：無。不適用者：無。**

**增量（R-TM46 + R-TM79）**：`## R-TM` **0**；`## A-TM` **0**；`## G-TM` **0**。
本包為執行，未生新條文（與下放包 §4 之自檢一致）。

**本包三項須先看**：
1. **§2 之落點偏離** —— 下放包所給之 T2 指令**不含 `--out`**，
   而腳本之預設落點為**來源檔同目錄（`inputs/`）**，非 `output/`。
   首次執行落在 `inputs/`，已刪除並以 `--out` 重跑至 `output/`。
   **兩次 SHA256 完全相同**（寫回為決定性），故無內容疑慮。
2. **§4 之 member 數 = 48** —— 下放包 §3 所指最可能出事之處**未出事**，
   R 欄之 x14 下拉存活（2 條 `x14:dataValidation`）。
3. **§5 之 DR-12b 處數 23 → 25** —— 017 拆分後之實測值，
   交付說明已依實測填入。

---

## 1. T1 —— dry-run 六項核對

| 核對項 | 期望 | 實測 | 判定 |
|---|---|---|---|
| `rows` | 59 | **59**（rows 10–68） | 符 |
| `skipped` | 4 份 `.pre-arch.json` | **B1/B2/B3/B4.pre-arch.json** | 符 |
| `tc_id` 區間 | `NR1L-TimeAndDate-001 … -059` | **同左** | 符 |
| `columns` | 十六欄 | **16**（D F G H I J K L M N O P R S AA AH） | 符 |
| `unresolved` | 空 | **空**（「內容常數全部已決」） | 符 |
| 來源 SHA256 | `6372fb6b…` | **`6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`** | 符 |

**六項全符，進 T2。**

---

## 2. T2 —— 寫回（一處落點偏離，已更正）

### 2.1 偏離之事實

下放包 T2 之指令為：

```bash
python3 features/time_management/scripts/write_back.py \
        --feature-dir features/time_management --write
```

而 `write_back.py:452` 之落點預設為：

```python
out = Path(args.out) if args.out else src.with_name(src.stem + "_regen-v1.xlsx")
```

`src.with_name(...)` 即**來源檔同目錄**，亦即 `features/time_management/inputs/`。
下放包同一節之要求為「輸出落 `features/time_management/output/`」——
**指令與要求不一致**。照指令執行之結果落在 `inputs/`。

**未觸及禁令**：落點仍在 feature 目錄內，未寫入任何交付路徑。
`output/` 於執行前並不存在（`ls` 回 No such file or directory）。

### 2.2 處置

1. `mkdir -p features/time_management/output`
2. 以 `--out` 指定 `output/` 下之同名檔重跑 `--write`
3. 刪除 `inputs/` 之誤落檔

**兩次輸出之 SHA256 相同**：
`2afd87be418e85599a99670db74457c3a629220583d39db195870a61093833c1`
——寫回為決定性，落點不影響內容。

`inputs/` 之誤落檔刪除前確認為 git 未追蹤
（`features/time_management/.gitignore:2` 已忽略 `inputs/`），
且為本次執行所生，非既有輸入。刪除後 `inputs/` 之 14 個既有輸入檔全在。

### 2.3 輸出檔記錄

| 項 | 值 |
|---|---|
| 路徑 | `features/time_management/output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext_regen-v1.xlsx` |
| SHA256 | `2afd87be418e85599a99670db74457c3a629220583d39db195870a61093833c1` |
| 大小 | 179,991 bytes |
| 列數 | 59（rows 10–68） |

### 2.4 給分析層之一項（不自行立條）

`write_back.py` 之落點預設與「輸出落 `output/`」之要求相衝。
本次靠 `--out` 補救，但**下次若照下放指令原樣執行，會再落一次 `inputs/`**。
處置屬分析層：或改腳本預設為 `feature-dir/output/`，或往後之下放包一律帶 `--out`。
**執行層本包未改任何腳本。**

---

## 3. T3 —— G-TM3 正向驗證

### 3.1 腳本內建之 G-TM3

`write_back.py:457` 之 `check_written_back(out, sheet, cols, plan["expected"])`
於 `--write` 路徑中執行且**未 raise**。
`surgical_save` 之寫入路徑至此為首次實際執行。

### 3.2 獨立重開之取樣比對（唯讀，本層另行為之）

以 `openpyxl.load_workbook(read_only=True)` 重開輸出檔，
對 `generated/B1–B4.json`（59 條，排除 4 份 `.pre-arch.json`）比對：

| 取樣 | 列 | `tc_id` | `test_item` | `design_method` |
|---|---|---|---|---|
| 首列 | 10 | OK `NR1L-TimeAndDate-001` | OK | OK `功能測試 (Functional based ; no specific technique)` |
| 中間列 | 39 | OK `NR1L-TimeAndDate-030` | OK | OK `邊界值分析 (Boundary Value Analysis, BVA)` |
| 末列 | 68 | OK `NR1L-TimeAndDate-059` | OK | OK `負向測試 (Negative / Invalid)` |

**補強（依 G-TM3 訂正之「tc_id 逐列互異」性質）**：
`F10:F68` 共 59 值**全數互異**，且與 `NR1L-TimeAndDate-{001..059}`
之序列**逐列相等**——排除「兩欄值恰同」之偽陰性。

**T3 判定：PASS。**

---

## 4. T4 —— 結構完整性複驗

```
src member 數: 48   out member 數: 48
member 增: []       減: []
內容相異之 member: ['xl/worksheets/sheet6.xml']
```

- **member 數 48**（非 47）——下放包 §3 所指之判別點通過。
- `xl/workbook.xml` 之 `rId6` 對映 `worksheets/sheet6.xml`，
  其分頁名為 `Test Case Specification 測試用例規範`
  ——**唯一相異之 member 即目標分頁**，無連動變更。
- **x14 下拉存活**：`sheet6.xml` 內 `<x14:dataValidation` 計 **2 條**。

**寫回確走 `surgical_save`。**

---

## 5. T5 —— 交付說明落檔

`features/time_management/output/DELIVERY_NOTE.md`，
標題與檔首皆標 **[PROPOSED]**。內容依下放包 §1 之草案，**未改一字**，
僅依 T5 之指示以實測值替換 DR 處數。

### 5.1 DR 處數實測（掃 `generated/B1–B4.json` 之 `PENDING: DR-{n}`）

| DR | 21 之數 | **本次實測** | 涉及 TC 數 |
|---|---|---|---|
| DR-5 | 4 | **4** | 4 |
| DR-6 | 1 | **1** | 1 |
| DR-8 | 1 | **1** | 1 |
| DR-9 | 1 | **1** | 1 |
| DR-10 | 10 | **10** | 9 |
| DR-12b | 23 | **25** | 25 |
| DR-20 | 9 | **9** | 7 |
| **合計** | 49 | **51** | — |

**唯一變動為 DR-12b：23 → 25**，成因為 017 之跨架構拆分
（14 → 16 條，見 `21` 上繳 §4）——新增之 2 條同樣涉及設定頁名。
交付說明之表已填 25，並加註合計 51。

**§1 草案之兩處請 Pei 特別看者，執行層未動**：
「未及事項」第一點（7/59 獨立覆核）**原文保留**；
48 筆之措辭**原文保留**（仍指名 SWE.1 未補件）。
二者之取捨屬 Pei。

---

## 6. 不得執行者 —— 自檢

| 禁令 | 遵守 |
|---|---|
| 不動 git、不 tag、不寫 `DELIVERY.sha256` | **是**（本包未執行任何 git 指令） |
| 不寫入任何交付路徑 | **是**（未觸及 `/Users/peihe/Work/02_Project_R1LR/`） |
| 不以 openpyxl 存回 | **是**（唯一寫入路徑為 `xlsx_surgical.py`，T4 之 member 48 為證） |
| 不刪除 `.pre-arch.json` | **是**（4 份俱在，dry-run 之 `skipped` 仍列出） |
| 不改 `Clock` 之頁名 | **是**（DR-12b 標記原樣保留 25 處） |
| 不改 §1 之交付說明內容 | **是**（僅替換 DR 處數，為 T5 明文所令） |
| 不碰 `features/vehicle_setting/` | **是** |

**一項需揭露**：本包刪除了 `inputs/` 之誤落輸出檔（§2.2）。
該檔為本次執行所生，非既有輸入，且刪除前後 `inputs/` 之既有 14 檔不變。

---

## 7. 現況與待 Pei

`features/time_management/output/` 內：

- 可交付之工作簿（SHA256 `2afd87be…`，179,991 bytes，59 條，member 48）
- `DELIVERY_NOTE.md`（**[PROPOSED]**）

**其後全部屬 Pei**：交付路徑之複製、git、tag、`DELIVERY.sha256`、
以及 §5 所列草案兩處之定稿。
