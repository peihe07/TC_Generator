# 上繳包 19a — 寫回 dry-run（2026-08-30）

對應下放包：`docs/handoff/19_writeback.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `6662b94b9a9418db0ae65d750998656ec96df8c1a056022d10b0ecf863088806`**
—— 與執行層自身記錄相符，未停。

**本包 git 執行次數 0**（含唯讀）。**作業 A／B／D／E 完成；作業 C 依令未做**（待分析層審本 dry-run）。
**【E42 觸發】**；E41／E43／E44／E9／E18 **未觸發**。

**repo 內未新增任何 xlsx；`sandbox/` 未由本包建立或修改。**

---

## §1 前提驗證＋圍籬 diff

### 1.1 P1～P6 —— **全部相符（E41 未觸發）**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | `## R-ICS` **61** 行、相異 **54** | **61 行、相異 54**；無 DUPLICATE | 相符（E18 未觸發）|
| P2 | A-ICS **130 列**、無缺口；DR **23／23** | **130／130／無缺口**；**23／23／無缺口** | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |
| P4 | 圍籬 diff +`R-ICS53`＋`R-ICS54`、刪 0 | **新增 124 行、刪除 0**；標題二條 | 相符 |
| P5 | `verify_reference_binding` 11／11 | **11／11 MATCH** | 相符 |
| P6 | 佔位 6／6；逐字 31／31；`selfcheck` FAIL 0 | **6 處／6 條**；**31／31**；**FAIL 0** | 相符 |

---

## §2 作業 A — 母本與 workbook_state

| 項 | 實測 |
|---|---|
| 母本 | `forms/…_SWQT_20260817_ext.xlsx` |
| sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| bytes | **200,650**（與 `FORMS.md` 登錄行相符）|
| 工作表 | **9 個**；目標表 `Test Case Specification 測試用例規範`，`max_row=1411`、`max_col=34` |
| 表頭列 | **第 9 列**（現場複驗）|
| 資料區起始 | **第 10 列**（與 memory 相符，**已現場複驗，非沿用**）|
| **既有資料列** | **0** —— 第 10 列僅 `B10="1"`（序號模板），其餘 33 欄全空；第 11～60 列全空 |

### 2-1 【E42 觸發】`generated/` 中**無 `tc_id`**

實測 31 條之 TC 欄位為：
`req_id`／`tc_title`／`test_group`／`test_set`／`test_item`／`pre_conditions`／`input_test_data`／
`test_procedure`／`expected_result`／`specification_reference`／`design_method`／`priority`／
`split_flag`／`split_reason`／`has_pending`／`reasoning`
—— **無 `tc_id`；31 條缺 31 個**（`manifest.json` 亦無 ID 欄）。

**現況之三項事實：**

1. **`feature.yaml` 已宣告格式**：`tc_id_format: "NR1L-ICS-{n:03d}"`，
   且欄位對映亦已宣告（`tc_id: "F"`、`tc_id_testrail: "E"`）。
   **格式在案，值從未生成。**
2. `feature.yaml` 另註明「全案之 project 前綴另有 `newR1L` 一式（工作簿 D2 儲存格實測）」
   —— **二式並存為既有實況**。
3. `req_id`（`SWE-ICS-001`~`010`）存在且逐條有值，但其為**需求 ID**（欄 D），
   **非 TC ID**（欄 F）。二者不可互代。

**依 E42 停下回報，未自行編號。**
`{n:03d}` 之 `n` 應依何序（生成順序？批次順序？Test Set 分組？）**本包不決定** ——
一旦編號即固定於交付件，其序之選擇屬分析層。

**因此欄 F 於本 dry-run 之投影為「待指派」，非空白約定欄。**

---

## §3 作業 B — dry-run（`docs/reports/19_writeback_dryrun.md`）

### 3-1 列數對帳

| 面 | before | after |
|---|---|---|
| 有 TC 內容之資料列 | **0** | **31** |

**0 ＋ 31 ＝ 31 ✓。** 第 10 列之既有序號 `1` 由第 1 條覆蓋（同為序號 1），不新增列。

### 3-2 欄位對映 —— 34 欄逐欄，**空白約定欄 14 項**（`T~Z` 計一項含 7 欄）

有來源者 10 欄（`D`／`G`～`N`／`P`／`R`）；序號欄 `B`；**待指派 1 欄（`F`，E42）**；
其餘為空白約定（`C`／`E`／`O`／`Q`／`S`／`T~Z`／`AA`～`AH`），逐欄具名於報告。

### 3-3 PENDING **6 處逐字**（**全部在 `pre_conditions`**）

| # | tc_title | DR | 缺件 |
|---|---|---|---|
| 1 | Three detents rotated clock-wise | **DR-ICS4** | `CFTS019 volume level range` |
| 2 | Knob 2 signals acted on by the HU | **DR-ICS6** | `HMI Logic and Flow browse mapping for ICS_KNOB2` |
| 3 | Enter button pressed | DR-ICS6 | `HMI Logic and Flow screen mapping for Enter_Button` |
| 4 | Knob 2 rotated on a scrollable screen | DR-ICS6 | `HMI Logic and Flow scroll mapping for ICS_KNOB2` |
| 5 | Knob 2 rotated on a tuner source | DR-ICS6 | `HMI Logic and Flow tune mapping for ICS_KNOB2` |
| 6 | Back button pressed | DR-ICS6 | `HMI Logic and Flow screen mapping for Back_Button` |

**原樣寫入，不降轉、不留白、不臆填**（R-ICS54(a)）。

### 3-4 不可出貨之 4 條

**V1**（VOLUME knob rotated clock-wise）／**V2**（counter clock-wise）／
**V3**（Three detents rotated clock-wise）→ **DR-ICS9**；
**B5**（Three detents counted in one rotation）→ **DR-ICS2**。

標號對映取自 `upstream/01` §表（V1~V3）與 `upstream/04` §表（B5），**非本包自行指派**。
**四條依令仍寫入工作簿，工作簿內不加任何註記；於清單標明。**

### 3-5 `specification_reference` 之排列 —— **違規 0**

逐行一 ObjectID、格式合式（`CFTS\d{3}-\d{7}`）、升序：**違規 0**。
**跨家族混排 3 條**（CFTS020 行皆在 CFTS022 前，R-ICS40(c)）：

- `Three detents rotated clock-wise`：`CFTS020-4819541` ⏎ `CFTS020-4821701` ⏎ `CFTS022-4914975`
- `Mute hardkey pressed while audio unmuted`／`muted`：`CFTS020-4821709` ⏎ `CFTS022-4914993`

**錨行 ≥3 者 6 條**（b12 加錨於投影中可見）。錨行總計 **65**、Test Set 相異 **5**。

### 3-6 【E43 判定點】R 欄之 x14 DV —— **保留，未觸發**

母本 `sheet6`（目標表）之 DV：**classic 3**（`P10:Q1411`／`T10:Z1411`／`AF10:AF1411`）
＋ **x14 1**，其 `xm:sqref` 為 **`R10:R1411`** —— 即 R-G1 所警告之設計方法欄。

以 `xlsx_surgical.surgical_save(verify=True)` 作單格試改，`verify_structure` **通過**：

- zip 成員 **48 個前後一致**；
- **DV 計數前後完全相同**；
- **僅 `xl/worksheets/sheet6.xml` 有差異**，其餘 47 成員 byte 相同。

**輸出寫於 session scratchpad 並於驗畢後刪除；repo 內未新增任何 xlsx。**

併記：`openpyxl.load_workbook` 載入時發出
`UserWarning: Data Validation extension is not supported and will be removed`
—— **此即 R-G3 禁止以 openpyxl 寫入之原因**；`surgical_save` 自母本 zip 逐成員複製，故不受影響。

### 3-7 done-region hash

母本目標表既有資料列 **0**，**無 done region → `N/A`**（具名，非略過）。

### 3-8 【E44 判定點】—— **未觸發**

本 dry-run 之每一欄皆自 json **直接讀取並原樣輸出**，無 strip／正規化／換行轉換。
**「投影非編輯」在本報告中以「不經手」保證。**
作業 C 之讀回逐條逐欄比對為其真正驗證點，**本包未做**。

---

## §4 【下放包未預料】`sandbox/` 已有一個既有檔

下放包 §3 作業 A-2 稱「本 feature **無既有交付件**」。實測：

`features/ics_management/sandbox/ics_management_00.xlsx` —— **存在**，
mtime `2026-08-29 12:25`（第 01 輪落點修正時所產），200,650 bytes。

**其 sha256 ＝ `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`
—— 與母本逐字相同。** 讀回實測：目標表**有內容之資料列 0**，第 10 列僅序號 `1`。

**即：它是母本之未改動複本，不是交付件。**
「無既有交付件」之判斷**結論正確，但前提敘述不精確**（有既有檔，只是內容為空）。

**本包未動該檔。** 作業 C 若產於 `sandbox/v1/`，**與其並存**；
是否清理、是否改用該檔為底，**屬分析層**。

---

## §5 作業 D

### 5-1 交付清單對照（`docs/reports/19_delivery_checklist_ics.md`）

逐項對照已出。**唯一標為「阻斷」者為 TC ID（E42）**；
GUI 驗證與 `delivered/`＋MANIFEST 標為「待」（屬 Pei）。

**並行寫入對 sha 可信度之影響（R-ICS54(f)）—— 三項實證**：

1. `canon_refs` 於本 session 內由 **445 → 486**，
   而執行層每輪之新檔於其報表中**皆 0 命中**（b16／b17／b18／b19 各驗一次）；
2. 掃描檔數由 **2523 → 2591**；
3. 分析層五簿之數輪變更於 `git status` 中已不顯示為未提交
   —— 由並行 session 先行提交。

**含意**：作業 C 之工作簿 sha256 只對其自身有效，
**不保證 repo 其他部分於 tag 時仍相同**。
`verify_reference_binding` 之 11／11 是對 **11 個參考件**之保證，非對 repo 全域。
**建議（不裁）：`--write` 與 tag 之間若相隔任何時間，tag 前應重跑一次該讀者。**

### 5-2 凍結記錄之更新（**執行層唯一得改之既有報告**）

`docs/reports/13_freeze_record.md` 依 R-ICS54(d) 改二節：

- **§3 掛帳表：11 → 18 項**。新增 #12 A-ICS116（列 39 檢查點缺口，b18 因 E40 停）、
  #13 A-ICS125（`4819578` 未加錨，相似度 0.97）、#14 A-ICS118②（三物件維持上呈）、
  #15 A-ICS109、#16 A-ICS130 及 b17／b18 後之其餘 OPEN、#17 CFTS022 無 SYS2（DR-ICS22）、
  #18 寫回後之交付狀態（非出貨授權）。既有 11 項全數保留並更新現況。
- **§4 解凍條件**：收斂為**單一句「上游 DR 回覆」**，並附八個 DR 之逐條對映。
  明載「其餘一切（新量測、新生成、補檢查點、加錨、三物件）**皆不構成解凍理由**」。

**其餘各節（§1／§2／§5／§6／§7）一字未改。**

---

## §6 作業 E — 常設自檢集

| 項 | 結果 |
|---|---|
| 圍籬 diff | **+124／−0**；新增 `R-ICS53`、`R-ICS54`（P4 相符）|
| 候選篩 | 原始 **140**／殘餘 **68**／**殘餘率 49%**（前十包 …／49／49%）|
| 未錨定斷言 | **3＋6**，不變 |
| `selfcheck_b01.py` | PASS —— 19 項 FAIL 0 |
| `verify_verbatim_b01.py` | PASS —— **31／31** |
| `pending_census.py` | **6 處／6 條** |
| `ledger_guard.py` | 前後 exit 0，**逐字相同** |
| `verify_reference_binding.py` | **11／11 MATCH** |
| 五支 gate | **`canon_refs` +8（478 → 486）** —— 見下 |
| 快照 | `docs/reports/19_rulings_snapshot.md` **已產出**，61 行 |

**gate 之基線具名**：本輪開工時未另存 gate 快照，
故以 **b18 完工之輸出（478）** 為對照基線。**其餘四支逐字相同。**

`canon_refs` 之 **+8**：本包三份新／改檔（`19_writeback_dryrun.md`／
`19_delivery_checklist_ics.md`／`13_freeze_record.md`）於 `--report` 清單中**皆 0 命中**；
掃描檔數由 2574 升至 **2591（+17）**。**成因為並行寫入（A-ICS121），不修，具名不調和。**

---

## §7 預期數字對照（下放包 §5，13 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` | 61 行（相異 54）、A-ICS 130、DR 23／23 | 全數相符 | 相符 |
| 2 | 圍籬 diff | +2 條、刪 0 | **+124 行／−0，二條** | 相符 |
| 3 | 母本資料列 → 寫回後 | 0 → 31 | **0 → 31**（dry-run 投影）| 相符 |
| 4 | PENDING | 6 處／6 條逐字原樣 | **6 處／6 條**，逐字已列 | 相符 |
| 5 | 不可出貨之條 | 4（V1／V2／V3／B5）| **4**，已標明 | 相符 |
| 6 | 讀回比對 31／31 | — | **作業 C 未做** | 未到執行點 |
| 7 | Test Set 相異值 | 5 | **5** | 相符 |
| 8 | 錨行 | 65 | **65** | 相符 |
| 9 | `verify_verbatim` | 31／31 | **31／31** | 相符 |
| 10 | **TC 內容變動** | **0** | **0** | 相符 |
| 11 | R 欄 DV | 保留 | **保留**（E43 未觸發）| 相符 |
| 12 | **git** | **0** | **0** | 相符 |
| 13 | 快照 | `19_rulings_snapshot.md` | **已產出** | 相符 |

**11 項相符、1 項未到執行點（#6）、另有 E42 觸發（下放包 §5 未列為預期項）。**

---

## §8 未結 DR 清單（23 條；DR-ICS8 已 CLOSED，不計）

| DR | 現況 | 本包 |
|---|---|---|
| DR-ICS1／3／11／14／17／19／21 | OPEN | — |
| **DR-ICS2** | OPEN | **B5 所繫**；Camera Transition 29 物件 |
| **DR-ICS4** | OPEN | **1 處佔位**（V3 之 pre_conditions）|
| DR-ICS5／7／10／13／15 | 可結／已標可結 | — |
| **DR-ICS6** | OPEN | **5 處佔位** |
| **DR-ICS9** | OPEN | **V1／V2／V3 所繫；無佔位故不會自行浮出** |
| DR-ICS12 | 追蹤件 | — |
| DR-ICS16 | 匯流排軸已結 | 讀者 11／11 |
| DR-ICS18 | 告知／追認件 | — |
| DR-ICS20 | OPEN | G2／G3 效力所繫 |
| DR-ICS22 | OPEN | CFTS022 之 SYS2 |
| DR-ICS23 | OPEN | SYS2 三項品質事實 |

---

## §9 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `19_writeback_dryrun.md`（34 欄對映、31 條投影、6 處 PENDING 逐字、排列檢查、DV 實測）；`19_delivery_checklist_ics.md`；`13_freeze_record.md` §3／§4（依 R-ICS54(d) 授權）；`19_rulings_snapshot.md` |
| **核實無誤** | 母本 sha 與 `FORMS.md` 登錄相符；表頭第 9 列／資料自第 10 列（現場複驗）；既有資料列 0；x14 DV `R10:R1411` 經 `surgical_save` 保留（48 成員一致、DV 計數不變、僅 sheet6 有差）；錨行 65／Test Set 5／逐字 31／31；`sandbox/ics_management_00.xlsx` 與母本 sha 逐字相同且資料列 0；本包三檔對 `canon_refs` 貢獻 0 |
| **正確地不動** | **作業 C 未做**（待審）；**未自行指派 tc_id**（E42）；repo 內未新增任何 xlsx、`sandbox/` 未動；四條不可出貨者依令仍投影且工作簿內不加註記；6 處 PENDING 未降轉；未修 `canon_refs` 之紅；`display`／`vehicle_setting`／`GATES.tsv` 零變動；五簿一字未寫；`13_freeze_record.md` 僅改 §3／§4，餘節一字未動；**git 0 次** |

---

## §10 建議登錄之 anomaly（編號由分析層取）

1. **【E42】`generated/` 之 31 條無 `tc_id`**，而 `feature.yaml` 已宣告
   `tc_id_format: "NR1L-ICS-{n:03d}"` 與欄位對映（`tc_id: "F"`）——
   **格式在案，值從未生成**。`{n:03d}` 之序（生成序／批次序／Test Set 分組）須裁。
2. **`feature.yaml` 自載「全案 project 前綴另有 `newR1L` 一式」**（工作簿 `D2` 實測）
   —— 二式並存為既有實況，編號前須先定。
3. **下放包稱「本 feature 無既有交付件」，實測 `sandbox/ics_management_00.xlsx` 存在**
   （第 01 輪所產，與母本 sha 逐字相同、資料列 0）。**結論正確而前提敘述不精確。**
4. `openpyxl` 載入母本即發出 `Data Validation extension … will be removed` 警告
   —— R-G3 之禁令有直接實證，建議併入 R-G3 之案例。
5. `canon_refs` 於本 session 由 445 升至 **486**，掃描檔數 2523 → **2591**；
   執行層每輪新檔皆 0 命中。**並行寫入之規模已達可影響任何全域計數之程度。**

**本包未產生任何新裁決條文，未自取任何編號。**

---

## §11 獨立判斷（下放包 §6 指定：只答一題）

### **本 dry-run 是否可進 sandbox —— 建議：不可，缺一件，且那一件不是我能補的。**

**可進之部分已全部就緒**：母本已驗（sha 相符、DV 保留、48 成員結構不變）、
投影已備（34 欄對映、31 條、錨行 65、排列違規 0）、
PENDING 6 處逐字在案、不可出貨 4 條已標明、done-region `N/A` 已具名。
**若只論工作簿之結構與內容，作業 C 現在就可以執行。**

**缺的是 TC ID。** 欄 `F`（`Test Case ID 測試用例ID`）是交付件之主鍵 ——
沒有它，寫出去的 31 列**無法被 TestRail 或任何後續流程指認**，
且日後補上等同**改動已交付件之主鍵**，代價遠高於現在停一次。

**而它不是我能補的**：`{n:03d}` 之 `n` 依何序，會固定進交付件而難以回頭。
生成序（b01→b07）、批次內序、Test Set 分組序 —— 三者給出三組不同的 ID，
**且 `feature.yaml` 自己就記載了 `NR1L` 與 `newR1L` 二式前綴並存**。
下放包已明令「ID 由生成器指派，本包不得自行編號」，**我依令停下**。

**建議之最小解**：分析層裁定 (a) 前綴取 `NR1L` 抑或 `newR1L`、(b) `n` 之排序依據，
二者定案後由生成器或另一包寫入 `generated/` 之 json，
**再進作業 C**。二件都不需要上游回覆，**不違反「非上游 DR 回覆不開窗」** ——
因為它們是 b19 自身之未完項，不是新開之量測。

---

## §12 引用清單

R-G1、R-G3、FO §6、FO 路徑政策；R-ICS54(a)~(f)、R-ICS53、R-ICS38(a)、R-ICS17(e)(f)、
R-ICS29(f)、R-ICS32(c)、R-ICS34、R-ICS40(c)、R-ICS42(d)(i)(j)、R-ICS48(c)；
A-ICS60、A-ICS78、A-ICS80、A-ICS109、A-ICS116、A-ICS118、A-ICS121、A-ICS125、A-ICS130；
A-DM14；DR-ICS1 ~ DR-ICS23；IN §1、§8.4.3、§10.3、§10.7、§11。
