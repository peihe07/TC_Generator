# 上繳包 19b — 編號與 sandbox 產出（2026-08-30）

對應下放包：`docs/handoff/19b_writeback_sandbox.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `eb0d95c908a8c37da70838f37bb32a6ed01fb6d583b22faac2e631956b2e0116`**
—— 與執行層自身記錄相符，未停。

**本包 git 執行次數 0**（含唯讀）。
**E18／E46／E47／E48／E9 全部未觸發。作業 0／C／D／E 全數完成。**

**工作簿已產出：`features/ics_management/sandbox/v1/ics_management_v1.xlsx`。**

---

## §1 前提驗證＋圍籬 diff

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | `## R-ICS` **63** 行、相異 **56**；重號僅既有七組 | **63 行、相異 56**；並存七組 `R-ICS2`／`19`／`22`／`23`／`25`／`33`／`35`，**皆判合法** | 相符（**E18 未觸發**）|
| P2 | A-ICS **137 列**、無缺口；DR **23／23** | **137／137／無缺口**；**23／23／無缺口** | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |
| P4 | 圍籬 diff +`R-ICS55`＋`R-ICS56`、刪 0 | **新增 126 行、刪除 0**；標題二條 | 相符 |
| P5 | 讀者 11／11；逐字 31／31；佔位 6／6；`selfcheck` FAIL 0 | **全數相符** | 相符 |

**撞號（A-ICS136）已於本包確認落地**：`R-ICS55` 與 `R-ICS56` 二條並存且各自唯一，
`ledger_guard` 未報 DUPLICATE。

---

## §2 作業 0 — `tc_id` 指派

### 2-1 【E46 判定點】投影列序 ＝ `generated/` 現行順序 —— **未觸發**

19a 之投影序係以 `sorted(glob('generated/b*/b*_tcs.json'))` ＋ 批內 json 陣列序產生，
**與本包指派所用之迭代為同一式**，無隱含排序。逐批：
b01 6／b02 2／b03 8／b04 7／b05 2／b06 2／b07 4 ＝ **31**。

### 2-2 寫入後驗

| 檢查 | 結果 |
|---|---|
| 個數 | **31** |
| 相異 | **31** |
| 重號 | **無** |
| 連續 `001..031` | **是** |
| 前綴唯一 | `NR1L-ICS`（單一）|
| `verify_verbatim` | **31／31** |
| `selfcheck` | 19 項 **FAIL 0** |
| `pending_census` | **6 處／6 條** |
| `manifest.json` | 七批皆增 `tc_ids` 並與 json 逐一相符 |

**其他欄一字未改之自證**：TC 欄位集合較指派前**僅多 `tc_id` 一鍵**。
（併記：`distinguishing_axis` 存在於 **27 條**，**為既有欄，非本包新增** ——
b19b 僅插入 `tc_id`，插於 `req_id` 之後以保欄序可讀。）

### 2-3 31 個 `tc_id` 與 `tc_title` 對照

| # | `tc_id` | `tc_title` | 批 |
|---|---|---|---|
| 1 | `NR1L-ICS-001` | Stuck button held over 120 s | b01 |
| 2 | `NR1L-ICS-002` | Stuck fault held until de-bounced not-pressed | b01 |
| 3 | `NR1L-ICS-003` | Button held exactly 120 s | b01 |
| 4 | `NR1L-ICS-004` | VOLUME knob rotated clock-wise **[V1]** | b01 |
| 5 | `NR1L-ICS-005` | VOLUME knob rotated counter clock-wise **[V2]** | b01 |
| 6 | `NR1L-ICS-006` | Three detents rotated clock-wise **[V3]** | b01 |
| 7 | `NR1L-ICS-007` | Press ignored during stuck condition | b02 |
| 8 | `NR1L-ICS-008` | Button responsive after release | b02 |
| 9 | `NR1L-ICS-009` | Power hardkey pressed while HU screen on | b03 |
| 10 | `NR1L-ICS-010` | Power hardkey pressed at Telematic Power full operation | b03 |
| 11 | `NR1L-ICS-011` | Power hardkey pressed while HU screen off | b03 |
| 12 | `NR1L-ICS-012` | Power hardkey pressed at Telematic Power idle | b03 |
| 13 | `NR1L-ICS-013` | Screen off hardkey starts the three second timer | b03 |
| 14 | `NR1L-ICS-014` | Screen off hardkey pressed again within three seconds | b03 |
| 15 | `NR1L-ICS-015` | Three second period completed after screen off hardkey | b03 |
| 16 | `NR1L-ICS-016` | Screen off hardkey pressed while HU screen off | b03 |
| 17 | `NR1L-ICS-017` | Knob 2 rotated clock-wise | b04 |
| 18 | `NR1L-ICS-018` | Knob 2 rotated counter clock-wise | b04 |
| 19 | `NR1L-ICS-019` | Knob 2 held stationary | b04 |
| 20 | `NR1L-ICS-020` | Knob 2 no change sent periodically | b04 |
| 21 | `NR1L-ICS-021` | Three detents counted in one rotation **[B5]** | b04 |
| 22 | `NR1L-ICS-022` | Knob 2 signals acted on by the HU | b04 |
| 23 | `NR1L-ICS-023` | Enter button pressed | b04 |
| 24 | `NR1L-ICS-024` | Knob 2 rotated on a scrollable screen | b05 |
| 25 | `NR1L-ICS-025` | Knob 2 rotated on a tuner source | b05 |
| 26 | `NR1L-ICS-026` | Mute hardkey pressed while audio unmuted | b06 |
| 27 | `NR1L-ICS-027` | Mute hardkey pressed while audio muted | b06 |
| 28 | `NR1L-ICS-028` | Back button pressed | b07 |
| 29 | `NR1L-ICS-029` | Two ICS buttons pressed at the same time | b07 |
| 30 | `NR1L-ICS-030` | Button event change reported within Tbutton | b07 |
| 31 | `NR1L-ICS-031` | Knob 1 status sent on BH-CAN | b07 |

**四條不可出貨者之 ID**：**V1 = `-004`／V2 = `-005`／V3 = `-006`／B5 = `-021`**。

---

## §3 作業 C — sandbox 產出

### 3-1 產出

| 項 | 值 |
|---|---|
| 路徑 | `features/ics_management/sandbox/v1/ics_management_v1.xlsx` |
| bytes | **177,187** |
| **sha256** | **`d31d81d211d11593cfbc6878e89fb87b3f9fcf3cbf33621a761857f4b2e2ddea`** |
| sidecar | `ics_management_v1.xlsx.sha256`（同值）|
| 母本 | `…_SWQT_20260817_ext.xlsx`，sha `6372fb6b…fb825b2`（19a 已驗）|
| 寫入法 | `xlsx_surgical.surgical_save(verify=True)` —— **未以 openpyxl 寫出**（R-G3）|
| patched cells | **403** ＝ 31 條 × 13 欄 |

**欄位對映取自 `feature.yaml` 之 `columns:` 宣告**（非本包自訂）：
`B` no／`D` req_id／`F` tc_id／`G` test_group／`H` test_set／`I` test_item／
`J` pre_conditions／`K` input_test_data／`L` test_procedure／`M` expected_result／
`N` spec_reference／`P` priority／`R` design_method。
**`E`（TestRail）留空**（R-ICS55(d)）；其餘為空白約定欄。

### 3-2 【E48 判定點】zip 結構與 DV —— **未觸發**

| 面 | 母本 | 輸出 | 判 |
|---|---|---|---|
| zip 成員數 | 48 | **48** | 相同 |
| 成員集合 | — | — | **相同** |
| 成員順序 | — | — | **相同** |
| zip timestamps | — | — | **不同者 0** |
| `docProps/core.xml` | — | — | **byte 相同**（`dcterms:created 2020-01-02T13:24:14Z`／`modified 2026-08-17T01:46:09Z` 原樣）|
| `docProps/app.xml` | — | — | **byte 相同** |
| DV 計數 `sheet5` | (1, 0) | **(1, 0)** | 相同 |
| DV 計數 `sheet6` | (3, **1**) | **(3, 1)** | 相同（**x14 `R10:R1411` 保留**）|
| 內容有差之成員 | — | **`xl/worksheets/sheet6.xml` 一個** | 與 19a 實測一致 |

**FO §6 之正規化（zip timestamps、dcterms dates）為結構性保證**：
`surgical_save` 自母本 zip 逐成員複製並沿用原 `ZipInfo`，**故無需另行正規化步驟** ——
實測 timestamps 與 dcterms 皆逐字未變。

**檔案大小 200,650 → 177,187 之差，成因為 zip 重壓縮之壓縮率**，
**非內容遺失** —— 成員集合、順序、timestamps 與 47 個成員之 byte 皆一致。**具名。**

### 3-3 【E47 判定點】讀回逐條逐欄比對 —— **未觸發**

以 `openpyxl.load_workbook(read_only=True, data_only=True)` 讀回：

| 檢查 | 結果 |
|---|---|
| **31 條 × 13 欄 ＝ 403 格** | **不符 0 —— 逐字相同（含 `tc_id`）** |
| 序號欄 `B` | 1..31 逐一相符 |
| 工作簿內 PENDING | **6 處**（原樣，未降轉）|
| Test Set 相異值 | **5** |
| 錨行總數 | **65** |
| 第 41 列（第 32 條之位置）| **無此列**（未溢寫）|

### 3-4 未做之項（具名）

- **Excel GUI 驗證**：**未做，屬 Pei 之手動項**。須以 GUI 確認者：
  R 欄 x14 下拉是否可展開（DV 計數檢查只驗數量與 sqref，**不驗 GUI 可用性**）、
  P／Q／T~Z／AF 欄之 classic 下拉、多行儲存格之呈現、中英混排之欄寬。
- **`delivered/`**：**未動**（該目錄不存在）。**`--write` 與 tag 屬 Pei。**
- **`sandbox/ics_management_00.xlsx`**：**未動、未用**（R-ICS55(e)）——
  其 sha 仍為 `6372fb6be02f48dc3a3e091a…`（與母本相同）、mtime 仍為 `08-29 12:25`。

---

## §4 作業 D

### 4-1 【下放包指定】A-ICS135 之觀測來源 —— 具名

19a §5-1 第 3 項稱「分析層五簿之數輪變更於 `git status` 中已不顯示為未提交」。

**該觀測來自使用者授權之 `git commit` 回合，不是來自任何一包之執行。**

具體而言：Pei 於各包完工後逐次下「git commit」，執行層於**該回合**內執行
`git status --short` 以決定 pathspec —— b17 與 b18 之 commit 回合皆見
`ANOMALIES.md`／`DATA_REQUESTS.md` 未列於變更清單，而 `ledger_guard` 同時讀到其最新內容。
**二者並置即得該觀測。**

**與「本包 git 0 次」不衝突**：禁區之射程為**下放包之執行**；
`git commit` 為 Pei 另行下達之指令，屬另一回合。
b17／b18 之上繳包亦已於其 commit 回合中具名此事。

**非推定為違規** —— 執行層於包內未執行任何 git。

### 4-2 交付清單更新（`docs/reports/19_delivery_checklist_ics.md`）

- **TC ID 由「阻斷」改為 PASS**：`NR1L-ICS-001` ~ `-031`；
- 增列 sandbox 工作簿路徑與 sha、讀回 403／403、zip 結構三列；
- 新增 §6：tc_id 已指派；**tag 前須重跑 `verify_reference_binding`**（R-ICS55(h)）；
  工作簿 sha 之可信度受並行寫入影響（A-ICS135／136）；`--write` 與 tag 屬 Pei。

---

## §5 作業 E — 常設自檢集

| 項 | 結果 |
|---|---|
| 圍籬 diff | **+126／−0**；新增 `R-ICS55`、`R-ICS56`（P4 相符）|
| 候選篩 | 原始 **140**／殘餘 **68**／**殘餘率 49%** |
| 未錨定斷言 | **3＋6**，不變 |
| `selfcheck_b01.py` | PASS —— 19 項 FAIL 0 |
| `verify_verbatim_b01.py` | PASS —— **31／31** |
| `pending_census.py` | **6 處／6 條** |
| `ledger_guard.py` | 前後 exit 0，**逐字相同** |
| `verify_reference_binding.py` | **11／11 MATCH** |
| 五支 gate | **`canon_refs` +2（486 → 488）**；其餘四支**逐字相同** |
| **`lint_paths`** | **未變**（仍為「基線外違規 + delivered 不符 = 2」）—— **`sandbox/v1/` 之新產出未使其惡化** |
| 快照 | `docs/reports/19b_rulings_snapshot.md` **已產出**，63 行 |

`canon_refs` 之 +2：本包未新增任何 `.md` 引用面之檔（僅改二份既有報告與 json／xlsx）；
掃描檔數持續增長（2591 起算）。**成因為並行寫入（A-ICS121／135），不修，具名不調和。**

---

## §6 預期數字對照（下放包 §5，13 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` | 63 行（相異 56）、A-ICS 137、DR 23／23；重號僅七組 | 全數相符 | 相符 |
| 2 | 圍籬 diff | +二條、刪 0 | **+126／−0，二條** | 相符 |
| 3 | `tc_id` | 31 個，`-001`~`-031`，無重號無缺號 | **31／連續／唯一前綴** | 相符 |
| 4 | `generated/` 其他欄變動 | **0** | **0**（欄集合僅多 `tc_id`）| 相符 |
| 5 | 讀回比對 | 31／31 逐字相同 | **403／403 格不符 0** | 相符 |
| 6 | PENDING | 6 處／6 條 | **6 處／6 條** | 相符 |
| 7 | Test Set 相異值 | 5 | **5** | 相符 |
| 8 | 錨行 | 65 | **65** | 相符 |
| 9 | `verify_verbatim` | 31／31 | **31／31** | 相符 |
| 10 | zip 成員／DV 計數 | 48／不變 | **48／不變** | 相符 |
| 11 | `delivered/` | 未動 | **未動**（不存在）| 相符 |
| 12 | **git** | **0** | **0** | 相符 |
| 13 | 快照 | `19b_rulings_snapshot.md` | **已產出** | 相符 |

**13 項全數相符。**

---

## §7 未結 DR 清單（23 條；DR-ICS8 已 CLOSED，不計）

| DR | 現況 | 所繫之 tc_id |
|---|---|---|
| **DR-ICS2** | OPEN | **`-021`（B5）**；Camera Transition 29 物件 |
| **DR-ICS4** | OPEN | **`-006`** 之 1 處佔位 |
| **DR-ICS6** | OPEN | **`-022`／`-023`／`-024`／`-025`／`-028`** 之 5 處佔位 |
| **DR-ICS9** | OPEN | **`-004`／`-005`／`-006`（V1／V2／V3）**；**無佔位故不會自行浮出** |
| DR-ICS18 | 告知／追認件 | 否認則 009 ＋ 15 條加錨退回 |
| DR-ICS20 | OPEN | G2／G3 效力所繫 |
| DR-ICS22 | OPEN | CFTS022 之 SYS2 |
| DR-ICS23 | OPEN | SYS2 三項品質事實 |
| DR-ICS1／3／11／14／17／19／21 | OPEN | — |
| DR-ICS5／7／10／13／15 | 可結／已標可結 | — |
| DR-ICS12 | 追蹤件 | — |
| DR-ICS16 | 匯流排軸已結 | 讀者 11／11 |

---

## §8 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | 31 條之 `tc_id` 指派（`NR1L-ICS-001`~`-031`）＋七批 `manifest.json` 同步；**`sandbox/v1/ics_management_v1.xlsx`** ＋ sidecar；`19_delivery_checklist_ics.md` 更新；`19b_rulings_snapshot.md` |
| **核實無誤** | E46（投影序＝json 序，同一迭代）；讀回 **403／403 逐字相同**；zip 48 成員／順序／timestamps／`docProps` 皆與母本一致；**x14 DV `R10:R1411` 保留**；工作簿內 PENDING 6／Test Set 5／錨行 65；第 41 列未溢寫；`distinguishing_axis` 為既有欄（27 條）非本包新增；`ics_management_00.xlsx` 之 sha 與 mtime 未變；`lint_paths` 未因新產出而惡化 |
| **正確地不動** | 6 處 PENDING 原樣未降轉；四條不可出貨者仍寫入且工作簿內無註記；欄 `E` 留空；**未複製入 `delivered/`**；**未執行 `--write`、未 tag**；未動 `ics_management_00.xlsx`；未做 GUI 驗證（具名屬 Pei）；未修 `canon_refs` 之紅；五簿一字未寫；`display`／`vehicle_setting`／`GATES.tsv` 零變動；**git 0 次** |

---

## §9 建議登錄之 anomaly（編號由分析層取）

1. **工作簿大小 200,650 → 177,187**，成因為 zip 重壓縮之壓縮率；
   成員集合／順序／timestamps／47 成員 byte 皆一致。**若交付方以檔案大小作校驗，須先知此事。**
2. **`distinguishing_axis` 存在於 27 條而非 31 條** —— 既有欄，b19b 未動；
   其於工作簿無對應欄位，**未投影**。是否應有對應欄，未裁。
3. `canon_refs` 於本 session 由 445 升至 **488**；掃描檔數 2523 → 2591 以上。
   並行寫入之規模已達可影響任何全域計數之程度（沿 A-ICS121／135）。
4. **A-ICS135 之觀測來源已具名**（§4-1）：來自 Pei 授權之 `git commit` 回合，
   非包內執行。建議 A-ICS135 補記此點以免日後被讀為違規。

**本包未產生任何新裁決條文，未自取任何編號。**

---

## §10 獨立判斷（下放包 §6 指定：只答一題）

### **本工作簿是否可交由 Pei 執行 `--write` 與 tag —— 建議：可，但有二個前置與一項限制。**

**可之理由**：機檢面已全綠且無一項待驗 ——
讀回 **403／403 逐字相同**；zip 48 成員／順序／timestamps／`docProps` 與母本一致；
**x14 DV（`R10:R1411`）保留**，僅 `sheet6.xml` 一個成員有差；
PENDING 6 處原樣、Test Set 5、錨行 65、第 41 列未溢寫；
`tc_id` 31 個連續唯一；`verify_reference_binding` 11／11。
**E47／E48 皆未觸發，且其判定點涵蓋了「投影非編輯」之全部機械面。**

**二個前置（皆屬 Pei，執行層無法代做）**：

1. **Excel GUI 驗證。** DV 計數檢查只驗數量與 sqref，**不驗 GUI 可用性** ——
   R 欄之 x14 下拉在 GUI 中能否展開，只有開啟過才知道。
   本 feature 之 `test_procedure`／`expected_result` 皆為多行，其呈現亦須目視。
2. **tag 前重跑 `verify_reference_binding`**（R-ICS55(h)）。
   本包完工時 11／11，但該保證只在當下有效 —— 本 session 內 `canon_refs` 由 445 升至 488、
   掃描檔數增逾 68 檔，**並行寫入之規模已足以在 `--write` 與 tag 之間改變任何東西**。

**一項限制（須寫進 tag 之說明，不寫會被誤讀）**：

**這不是出貨授權。** IN §8.4.3 不變（R-ICS54(a)）。工作簿內有 **6 處 PENDING**，
且 **4 條不可出貨**（`-004`／`-005`／`-006` 繫 DR-ICS9，`-021` 繫 DR-ICS2）——
而**那 4 條在工作簿內沒有任何記號**（依令不加註）。
**`pending_census` 不報它們、`selfcheck` 全綠、工作簿本身看不出來** ——
**只有 `19_delivery_checklist_ics.md` §3 與凍結記錄 §3 會提醒。**

**故建議 tag 之說明須明載那四個 ID。** 這是十九包以來反覆出現的同一個形狀：
**外觀完整而阻因不可見。** 現在它有了編號，第一次可以被具名地寫下來。

---

## §11 引用清單

R-ICS56(a)~(h)、R-ICS55(c)(d)(e)(f)(g)(h)、R-ICS54(a)(b)(c)(e)、R-ICS38(a)、R-ICS17(e)(f)、
R-ICS29(f)、R-ICS32(c)、R-ICS34、R-ICS40(c)；R-G1、R-G3、FO §6、FO 路徑政策；
A-ICS121、A-ICS135、A-ICS136、A-ICS137；DR-ICS1 ~ DR-ICS23；
IN §1、§8.4.3、§10.3、§10.7、§11。
