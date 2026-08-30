# 下放包 19b — 編號與 sandbox 產出（2026-08-30）

## §0 定案

**Pei 令「定案並把 ID 寫進 `generated/` 的 json」** → 分析層依 **R-ICS55(c)** 完成普查，落 **R-ICS56**。

**普查實測**（全案交付工作簿欄 F，五本 783 列）：

| feature | 前綴 | 列數 | 001..N 連續且與列序一致 |
|---|---|---|---|
| power（delivered）| `NR1L-PowerManagement` | 389 | ✓ |
| sxm | `NR1L-SXM` | 215 | ✓ |
| bed_lowering | `newR1L-BLM` | 151 | ✓ |
| display | `TC-DM` | 23 | ✓ |
| popup | `NR1L-Popup` | 5 | ✓ |

### 定案二項

| 項 | 定案 | 依據 |
|---|---|---|
| **前綴** | **`NR1L-ICS-{n:03d}`** | `NR1L` 占 609／783 列、3／5 本；最新（popup 08-28）與最舊（sxm 08-13）皆為 `NR1L` —— `newR1L`／`TC-` 為離群，非新舊之別。且與 `feature.yaml` 既宣告一致 |
| **`n` 之序** | **依工作簿列序，001 連續至 031**；列序即 19a dry-run 之投影序（`generated/` 現行順序，b01→b07，批內依 json 陣列序）| 五本**全數**為 001..N 連續且與列序逐一一致，**無一本重排**；R-ICS55(c)② 之備位規則（Test Set 分組）因此**不啟用** |

**具名三事**：

1. **R-ICS55(c)① 之 E45 條件字面上成立**（二式於已交付件中皆有），
   惟 **Pei 已逐字下放該裁定**，回頭上呈是退回一個已下放之事。已於 R-ICS56(f) 具名。
2. **R-ICS55(c)① 之先驗經實測推翻** —— 其料 `newR1L` 為全案式，實測僅 bed_lowering 一本。
   而該條自己已寫「這是先驗不是量測，不得據以編號」，**其自限正確**。
3. **全案三式並存**（`NR1L`／`newR1L`／`TC-`）已登 A-ICS137，
   **屬全案面，依 R-ICS54(c) 不在 ICS 線處理，不回改任何已交付件**。

### 撞號（A-ICS136）

本對話取現場號後落 `R-ICS55`，而寫入時該檔**已存一則 `R-ICS55`**（非本對話所寫）。
**同 A-ICS70 之形，第二次。** 已解：保留既存 `R-ICS55`，本對話之區塊改號 **`R-ICS56`**，
定位為「R-ICS55(c) 所令之普查之結果」——二條互補。

**執行層須知**：讀台帳一律 `grep` 取最大號；**寫入後須即重驗該號仍唯一**。

### 前提（量測時點 2026-08-30）

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `## R-ICS` **63** 行、相異 **56**；重號只有既有七組 v1／v2（`R-ICS2`／`19`／`22`／`23`／`25`／`33`／`35`）| `ledger_guard.py` |
| P2 | `ANOMALIES.md` **137 列**、相異 137、無缺口；DR **23／23** | 同上 |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | 圍籬 diff 對 `19_rulings_snapshot.md`：新增 `R-ICS55`＋`R-ICS56`、刪除 0 | 快照法，不碰 git |
| P5 | `verify_reference_binding` **11／11**；`verify_verbatim` **31／31**；佔位 **6／6**；`selfcheck` FAIL 0 | 執行 |

**P1 若出現七組以外之重號 → E18 停。** 其餘不符以實測為準並具名。

---

## §1 禁區

沿下放包 19 §1，並：

- **`tc_id` 只得依 R-ICS56(a)(b) 指派**；不得自行改前綴、不得重排、不得跳號。
- **除新增 `tc_id` 欄外，`generated/` 之任何其他欄一字不改**。
- **`tc_id_testrail`（欄 E）留空**（R-ICS55(d)）。
- **`sandbox/ics_management_00.xlsx` 不動、不用**（R-ICS55(e)）；作業 C 產於 `sandbox/v1/`。
- **不複製入 `delivered/`**；**`--write` 與 tag 屬 Pei**。
- R-G3：不得以 openpyxl 開啟寫入；用 `xlsx_surgical` splice。
- 分析層五簿一字不寫；不自取編號。

---

## §2 裁決引用

**R-ICS56(a)~(h)**、**R-ICS55(c)(d)(e)(f)(g)(h)**、**R-ICS54(a)(b)(c)(e)**、
R-G1、R-G3、FO §6、FO 路徑政策；IN §1、§8.4.3、§10.3、§10.7、§11。

---

## §3 作業清單

### 作業 0 — 指派 `tc_id`

1. 依 **`NR1L-ICS-{n:03d}`**，`n` 依 19a dry-run 之投影列序，**001 → 031**。
2. 寫入 `generated/` 各批 json 逐條之 `tc_id` 欄；`manifest.json` 同步。
   **不改其他任何鍵。**
3. **寫入後驗**：31 個相異、無重號、無缺號、與投影列序一致；
   `verify_verbatim` 仍 **31／31**；`selfcheck` FAIL 0。
4. **列出 31 個 ID 與其對應之 tc_title**，供分析層核。

**E46**：若投影列序與 `generated/` 之現行順序不一致 → 停下回報。
（19a 之投影序須與 json 序逐一相同；不同表示投影時有隱含排序。）

---

### 作業 C — sandbox 產出

1. 以 `xlsx_surgical` splice 於 `features/ics_management/sandbox/v1/` 產出工作簿。
   母本：`forms/…_SWQT_20260817_ext.xlsx`（sha `6372fb6b…`，19a 已驗）。
2. 產出 `.sha256` sidecar；依 FO §6 正規化（zip timestamps、dcterms dates）後取 sha。
3. **讀回逐條逐欄比對**（`read_only=True, data_only=True`）：
   - 31／31 逐字相同（含 `tc_id`）；
   - PENDING **6 處**原樣；Test Set 相異 **5**；錨行 **65**；
   - **DV 保留**：48 成員一致、DV 計數不變、僅 sheet6 有差（19a 已驗，此處為回歸）。
4. **Excel GUI 驗證為 Pei 之手動項**，執行層具名其未做。
5. **不進 `delivered/`。**

**E47**：讀回比對有任一欄不逐字相同 → 停。**寫回是投影不是編輯。**
**E48**：DV 計數或 zip 成員數與 19a 之實測不同 → 停。

---

### 作業 D — 二件收尾

1. **A-ICS135 之具名來源**：19a §5-1 第 3 項稱「分析層五簿之數輪變更於 `git status` 中
   已不顯示為未提交」，而本包自報 git 0 次。**該觀測由何而來？**
   （他實例之報告？檔案 mtime 推斷？其他？）**具名即可，不推定為違規。**
2. **交付清單更新**：`19_delivery_checklist_ics.md` 增
   ① tc_id 已指派（`NR1L-ICS-001`~`031`）；
   ② **tag 前須重跑 `verify_reference_binding`**（R-ICS55(h)）；
   ③ 工作簿 sha 之可信度受並行寫入影響（A-ICS135／136）。

---

### 作業 E — 常設自檢集

圍籬 diff（對 `19_rulings_snapshot.md`，預期 +2 條）；候選篩；未錨定斷言 3＋6；
五支 gate ＋ 讀者一支；開工 sha256；完工存 `19b_rulings_snapshot.md`。

---

## §4 停下回報條件

- **E18**：`ledger_guard` 報七組以外之重號 → 停。
- **E46**：投影列序 ≠ `generated/` 現行順序 → 停。
- **E47**：讀回比對任一欄不逐字相同 → 停。
- **E48**：DV 計數或 zip 成員數與 19a 不同 → 停。
- **E9**：條文互斥 → 停。

---

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` | 63 行（相異 56）、A-ICS 137、DR 23／23；重號僅既有七組 |
| 2 | 圍籬 diff | +`R-ICS55`＋`R-ICS56`、刪 0 |
| 3 | `tc_id` | **31 個**，`NR1L-ICS-001`~`031`，無重號無缺號 |
| 4 | `generated/` 其他欄變動 | **0** |
| 5 | 讀回比對 | **31／31 逐字相同** |
| 6 | PENDING | **6 處／6 條** |
| 7 | Test Set 相異值 | **5** |
| 8 | 錨行 | **65** |
| 9 | `verify_verbatim` | **31／31** |
| 10 | zip 成員／DV 計數 | 與 19a 相同（48／不變）|
| 11 | `delivered/` | **未動** |
| 12 | git | **0** |
| 13 | 快照 | `19b_rulings_snapshot.md` |

---

## §6 上繳包要求

`docs/upstream/19b_writeback_sandbox.md`。須含：裁決指紋＋前提＋圍籬 diff；
**31 個 tc_id 與其 tc_title 對照表**；作業 C 之讀回比對結果與工作簿 sha；
結果三分法；未結 DR（23 條）；建議 anomaly；
**獨立判斷只答一題：本工作簿是否可交由 Pei 執行 `--write` 與 tag**。

---

## §7 一句話

**工作簿那一側已經驗完了。缺的只是 31 個編號。** 這包做完，ICS 的東西就都在檔案裡了，
剩下的是 Pei 的 git 與四份上游回覆。
