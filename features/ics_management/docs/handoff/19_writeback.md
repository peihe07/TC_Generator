# 下放包 19 — 寫回（2026-08-30）

## §0 這是寫回包，不是量測包

**Pei 逐字：「寫回吧 不要再繼續 pending 就 pending」** → **R-ICS54**。

| 裁 | 效果 |
|---|---|
| 寫回授權 | 31 條依現狀寫回 036 工作簿。**非出貨授權**——IN §8.4.3 不變 |
| PENDING 維持 | 6 處佔位原樣寫入 `PENDING: DR-{n} <缺件名>`；**不降轉、不留白、不臆填** |
| 硬性停止 | 寫回後 **非上游 DR 回覆不開窗**。掛帳全部入凍結記錄 |

**本包不量任何新東西。** 十八包來所有量測皆已在案；本包只把 31 條放進工作簿。
凡本包中發現之新事項，**登記入上繳包 §建議 anomaly 即止**，不得據以延伸作業（R-ICS54(c)）。

### 前提（量測時點 2026-08-30）

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：`## R-ICS` **61** 行、相異 **54**；無重複條號 | `ledger_guard.py` |
| P2 | `ANOMALIES.md` **130 列**、相異 130、號段無缺口（列序非遞增）；DR **23／23** | 同上 |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | 圍籬 diff 對 `18_rulings_snapshot.md`：新增 `R-ICS53`＋`R-ICS54` 二條、刪除 0 | 快照法，不碰 git |
| P5 | `verify_reference_binding` **11／11** | 執行 |
| P6 | `pending_census` **6 處／6 條**；`verify_verbatim` **31／31**；`selfcheck` FAIL 0 | 執行 |

不符以實測為準並具名；P1 重複條號 → E18；**P5／P6 任一不符 → 停下（E41），寫回之基礎不穩**。

---

## §1 禁區

- **git 全數不執行，唯讀亦不可。** `--write` 與 tag 屬 Pei（FO §6、R-ICS54(e)）。
- **R-G3：不得以 openpyxl 開啟寫入。** 寫回用 `xlsx_surgical` splice。
- **xlsx 只得於 `features/ics_management/sandbox/<tag>/` 修改**（FO 路徑政策）；`delivered/` 只進不改。
- **不改任何 TC 之內容**：31 條之 `generated/` json 為唯一來源，寫回是投影不是編輯。
  （A-ICS116 之補檢查點、A-ICS125 之加錨、三物件 —— **一律不做**，R-ICS54(d)。）
- **不降轉任何 PENDING、不臆填、不留白。**
- **工作簿欄位 English only**（IN §1）；中文備註不入交付欄。
- **`features/display/`、`features/vehicle_setting/`、`docs/runtime/GATES.tsv` 一字不改。**
- 分析層五簿一字不寫；不自取編號。

---

## §2 裁決引用

**R-ICS54(a)~(f)**、**R-G1**（036 母本）、**R-G3**（`xlsx_surgical`）、**FO §6**（dry-run → commit → --write → tag）、
FO 路徑政策（`sandbox/<tag>/`、`delivered/`＋MANIFEST.tsv）；IN §1、§8.4.3、§10.7、§11；
R-ICS38(a)、R-ICS17(e)(f)、R-ICS29(f)。

---

## §3 作業清單

### 作業 A — 母本與 workbook_state

1. **母本**：`forms/…_SWQT_20260817_ext.xlsx`（R-G1）。逐字列其檔名、sha256、`forms/FORMS.md` 之登錄行。
2. **workbook_state**：本 feature 無既有交付件，預期為「空白／自首資料列 append」（FO §2）。
   實測母本之資料區起始列（memory：工作表 `Test Case Specification 測試用例規範`，資料列自第 10 列）——**須現場複驗，不得沿用記憶**。
3. **TC ID 格式**：IN §10.3 `{project}-{abbr}-{NNN}`。`generated/` 中現行 tc_id 之前綴逐字列出；
   **若 json 中無 tc_id 或前綴不一致，停下回報（E42）** —— ID 由生成器指派，本包不得自行編號。

### 作業 B — dry-run

依 FO §6 之 dry-run review checklist，產出：

1. **逐段 before→after 列數**：母本資料列 0 → 31；算術對帳。
2. **31 條之寫回投影**：每條之 tc_id、test_set、test_item（上半 verbatim ＋ 下半括號）、
   pre_conditions、input_test_data、test_procedure、expected_result、specification_reference、
   design_method、priority —— 逐欄自 `generated/` json 投影，**不得改寫**。
3. **PENDING 列清單**：6 處，逐處列 tc_id、欄位、`PENDING: DR-{n} <缺件名>` 之逐字。
4. **不可出貨之 4 條**（V1／V2／V3／B5）：列出 tc_id，**於 dry-run 報告標明，不寫入工作簿**。
5. **specification_reference 之排列**：IN §10.7 一 ObjectID 一行、升序、CFTS020 行在 CFTS022 前（R-ICS40(c)）。
   **b12 之 15 條加錨與 b06 之跨家族混排須於投影中可見。**
6. **設計方法欄之 DV**：R-G1 註明母本 R 欄之 DV 為 x14 擴充，openpyxl 讀取即丟棄 ——
   `xlsx_surgical` 是否保留？**實測並報**；若丟失，停下回報（E43）。
7. **空白約定欄**：逐欄命名（FO §6 checklist 末項）。
8. **done-region hash**：母本無 done region（0 列），報 `N/A` 並具名。

**dry-run 報告出 `docs/reports/19_writeback_dryrun.md`。分析層審過之前不進作業 C。**

> **本包分二段**：作業 A／B 完成即上繳（**上繳包 19a**）。分析層審 dry-run 後另下一字，
> 執行層再做作業 C。**這是 FO §6「dry-run reviewed → commit」之序，不是新開窗。**

### 作業 C — sandbox 產出（**待分析層審 dry-run 後**）

1. 於 `features/ics_management/sandbox/v1/` 以 `xlsx_surgical` splice 產出工作簿。
2. 產出 `.sha256` sidecar；工作簿依 FO §6 正規化（zip timestamps、dcterms dates）後取 sha。
3. **自檢**：以 `read_only=True, data_only=True` 讀回，逐條逐欄與 `generated/` json 比對，**31／31 逐字相同**；
   PENDING 6 處原樣；Test Set 相異值 5；`specification_reference` 錨行總數 65。
4. **Excel GUI 驗證為 Pei 之交付清單手動項**（memory：openpyxl 寫入後之 extLst／printerSettings／xmlns:xr 修補），
   執行層具名其未做。
5. `lint_docs036` 對本 feature 之結果（既有紅在 `features/power/`，具名不修）。
6. **不複製入 `delivered/`** —— 那是 `--write` 之後、tag 之前，屬 Pei。

### 作業 D — 交付清單與凍結記錄

1. **`DELIVERY_CHECKLIST.md`（全案）之本 feature 條目**：逐項對照現況，出 `docs/reports/19_delivery_checklist_ics.md`。
   須含：PENDING 6 處及所繫 DR；不可出貨 4 條及所繫 DR（ICS9／ICS2）；
   Excel GUI 驗證（手動，Pei）；並行寫入對 sha 可信度之影響（R-ICS54(f)）。
2. **凍結記錄 `13_freeze_record.md` 之掛帳表**：依 R-ICS54(d) 增列
   A-ICS116／125／118②／109／130，及 b17／b18 後所有 OPEN 項；解凍條件改為單一句「上游 DR 回覆」。
   （**此為執行層唯一得改之既有報告**，限掛帳表與解凍條件二節。）

### 作業 E — 常設自檢集

圍籬 diff（對 `18_rulings_snapshot.md`，預期 +2 條）；候選篩；未錨定斷言 3＋6；
五支 gate ＋ 讀者一支；開工 sha256；完工存 `19_rulings_snapshot.md`。

---

## §4 停下回報條件

- **E41**：P5／P6 任一不符 → 停。寫回之基礎不穩。
- **E42**：`generated/` 中 tc_id 缺失或前綴不一致 → 停。本包不得自行編號。
- **E43**：`xlsx_surgical` 丟失母本 R 欄 DV → 停。
- **E44**：dry-run 之 31 條投影與 json 有任一欄不逐字相同 → 停。寫回是投影不是編輯。
- **E9**：條文互斥 → 停。

---

## §5 預期數字

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` | 61 行（相異 54）、A-ICS 130、DR 23／23 |
| 2 | 圍籬 diff | +2 條（`R-ICS53`＋`R-ICS54`）、刪 0 |
| 3 | 母本資料列 → 寫回後 | **0 → 31** |
| 4 | PENDING | **6 處／6 條**，逐字原樣 |
| 5 | 不可出貨之條 | **4**（V1／V2／V3／B5），於清單標明、工作簿不加註 |
| 6 | 讀回比對 | **31／31 逐字相同** |
| 7 | Test Set 相異值 | **5** |
| 8 | 錨行 | **65** |
| 9 | `verify_verbatim` | **31／31** |
| 10 | **TC 內容變動** | **0** |
| 11 | R 欄 DV | 保留（若丟 → E43）|
| 12 | git | **0** |
| 13 | 快照 | `19_rulings_snapshot.md` |

---

## §6 上繳包要求

**19a**（作業 A／B／D／E）：`docs/upstream/19a_writeback_dryrun.md`。
**19b**（作業 C）：`docs/upstream/19b_writeback_sandbox.md`，待分析層審 19a 後另一字。

各須含：裁決指紋＋前提＋圍籬 diff；結果三分法；**未結 DR 清單（23 條）**；
建議 anomaly（編號由分析層取）；**獨立判斷只答一題：本 dry-run 是否可進 sandbox**。

---

## §7 一句話

十八包，31 條，54 條裁決，130 則 anomaly，23 條 DR。**現在把它放進工作簿。**
剩下的等上游。
