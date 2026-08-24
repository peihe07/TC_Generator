# 上繳包 13 —— batch 1 重寫、雙向複驗與 lint 擴充

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/13_batch1_rework.md`
- 執行狀態：**步驟 1–6 全部執行完畢。**
  **⚠ 停止條件 7 觸發** —— 雙向複驗查出 **7.1 以外之三處新漏**，
  其一使兩條需求**根本不在 48 leaf 內**（§3）。停止條件 8、9 未觸發。
  **零寫回工作簿**；**改狀態 git 零次**；未動 `docs/runtime/` 與他 feature。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH51 | 7.1 改判漏句；規格比對一律雙向 | 500 | `55d75bee47dedba9` | `55d75bee47dedba9` | 逐字相符 |
| R-PMH52 | lint 須具名未涵蓋節號 | 339 | `5abf94f6836df206` | `5abf94f6836df206` | 逐字相符 |
| R-PMH53 | 拆分後之交叉引用連帶更新 | 348 | `8520b02b6d6c5dc4` | `8520b02b6d6c5dc4` | 逐字相符 |

6 個 placeholder 各命中 1，共 6 次（預期 6）。

---

## 2. 步驟 2 —— A-PMH03 改判之落實

標題改為「**PENDING（13 包再度改判 —— 見 A-PMH14）**」。
12 包所加之「結論更正」段（含 01 包原文之保留引用）**未動**。

---

## 3. 步驟 3 —— 雙向複驗：**停止條件 7 觸發**

**程式**：`scripts/bidirectional_spec_diff.py`
**報告**：`docs/reports/bidirectional_spec_diff.md`

### 3.1 方法（含二級過濾）

| 項 | 值 |
|---|---|
| 比對單位 | 句（句號後空白切分），最短 25 字元 |
| 正規化 | 去 `_x000D_`、摺疊空白、統一彎引號／省略號／破折號 |
| 一級判定 | 該句是否為對方全文之子字串 |
| **二級判定** | 未命中者再求 **6-gram 覆蓋率**；`< 30%` 為真漏候選，`>= 30%` 判為 `-layout` 之切分假象 |

**二級過濾為必要**：`pdftotext -layout` 於多欄頁會把表格列與頁首黏成一句，
一級判定之「未命中」大量為切分假象而非漏句。

### 3.2 方向一（SYS1 → PDF）—— 複算 01 包

未命中之 outline：`2.1`／`3.1`／`4.1`／`5.1`／`6.1`（圖片佔位）、
`7.1`／`9.1`／`11.1`（A-PMH03 已記）、`12.4`（圖片佔位）。**與 01 包相符。**

### 3.3 方向二（PDF → SYS1）—— **本輪新增，抓漏句**

| PDF 頁 | 句數 | 命中 | 未命中 | 6-gram 過濾後之真漏候選 |
|---|---:|---:|---:|---:|
| p1 | 4 | 0 | 4 | 4 |
| p2 | 5 | 0 | 5 | **0** |
| p3–p7 | 19 | 0 | 19 | 19 |
| **p8** | 38 | 34 | 4 | **1** |
| **p9** | 15 | 0 | 15 | **9** |
| **p10** | 19 | 12 | 7 | **3** |
| **p11** | 3 | 2 | 1 | **1** |
| 合計 | 106 | 48 | 55 | **37** |

37 句中 **23 句在 p1–p7**（封面 ＋ 五張流程圖）—— **A-PMH04 已知之圖片佔位，
不計為新漏**。餘 **14 句在 p8–p11**，逐句查證後得**三處新漏**。

### 3.4 新漏 1 —— **`SU9.)` 與 `SU9.1)` 兩條需求整段缺失**

PDF p8 於 `SU8.)` 之後：

```
SU9.) Pressing "Screen Off" or "Power Off" hard key will not do anything when
      pressed during animation.
SU9.1) Pressing Power Off or Screen Off hard keys during the splash screen(s) or
       disclaimer will reset the timeout and the radio shall display the screen
       the next time the screen turns on. (DCR20015)
```

SYS1 之 `7.9` 逐字為 `SU8.) Show the splash screen and disclaimer screen once
per CAN BUS cycle`，**且 7.9 為 7.x 之最末則**。

| 探針 | SYS1 全 52 則 |
|---|---|
| `SU8` | 有 |
| **`SU9.1`** | **0** |
| **`SU9)`** | **0** |
| `reset the timeout` | **0** |
| `hard keys during the splash` | **0** |

**⚠ 其後果不只是 `source_clause` 缺料 —— 是 leaf 不存在。**
037 之 leaf 以 `HMI Source ID` 指向 outline；SYS1 既無該二 outline，
037 即無對應之 Functional Requirement 列，
**故該二需求不在 R-PMH1 所定之 48 leaf 之內**。

**其題材正落在 `Disclaimer Screen` 內**，且 **SU9.1 直接影響逾時語意**。
**已開 `DR-PMH3`。**

### 3.5 新漏 2 —— **p9 之 Power Moding 狀態矩陣表格全缺**

| 探針 | SYS1 全 52 則 |
|---|---|
| `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI` | **各 0** |
| `Power Button only is functional`／`Fully functional`／`ENGINE ON` | **各 0** |

SYS1 之 `9.1` 只有 `PM1)`–`PM4)` 之散文（1,265 字元）。
**5 個 leaf 引 `9.1`** —— 其判讀背景之狀態矩陣不在 SYS1 內。

### 3.6 新漏 3 —— **指向一份我們沒有之外部規格**

PDF p10：`POWER MODING STATE MATRIX: Power Moding behavior **shall not be
developed without following** the Power Moding State Matrix, which is in a
separate Excel document. …`

四組探針（`POWER MODING STATE MATRIX`／`State Matrix`／`separate Excel`／
`request a copy from the author`）於 SYS1 **皆 0 命中** ——
**若只讀 SYS1，連「有這份文件」都不會知道。已開 `DR-PMH2`。**

### 3.7 非新漏者（具名，避免誤計）

| 項 | 判定 |
|---|---|
| p1–p7 之 23 句 | **A-PMH04 已知**（圖片佔位 ＋ 封面） |
| p10 之 VRLP1 四個 outcome | **非漏** —— SYS1 之 11.1 有之，僅條列符號與順序不同 |
| p11 之 1 句 | **A-PMH04 已知**（12.4 圖片佔位） |

### 3.8 A-PMH03 之「四則缺口」框架本身不成立

該框架以「SYS1 之則」為單位計缺口，而**漏句沒有「則」可計** ——
`SU9`／`SU9.1` 在 SYS1 中不存在任何一則。三處新漏**不計入四則，另計**。
已登記為 **A-PMH14**。

---

## 4. 步驟 4 —— lint 擴充（R-PMH52）

原 20 項 → **28 項**。七項新檢查各以**未修正之 batch 1 為天然反例**
（`tests/fixtures/batch01_prerework.json`，已保全）。

### 4.1 must-hit 之實跑 —— **七項全部如期 FAIL**

```
canon §10.5 test_procedure >= 2 步            **FAIL**  [(-002, 1), (-003, 1), (-006, 1)]
canon §5.1 procedure 無禁用動詞                 **FAIL**  8 處
canon §5.2B/§5.5 Final Step 含驗證意圖          **FAIL**  8 條
canon §4.3.1 test_item 上半 ⊆ source_clause    **FAIL**  [-001,-002,-003,-004,-007,-008]
交付欄位無 markdown 標記                         **FAIL**  [-004,-005,-006]
canon §11 無彎引號                              **FAIL**  [-001]
canon §11 UI 標籤加直雙引號                       **FAIL**  [-001..-004]
R-PMH53 交叉引用存在且語意相容                      **FAIL**  4 處
20/28 PASS
```

**停止條件 8 未觸發。**

### 4.2 R-PMH53 之檢查須加強一次才 must-hit

**首版只驗存在性 → PASS**（`-004`／`-003` 確實存在，只是語意錯）。
依 R-PMH53 之「語意相容」加強：**被引用者之 `distinguishing_axis`
須與引用者自身之 axis 至少共用一個實詞**（長度 ≥2 之 CJK 詞或 ≥3 之英文字）。

加強後精準命中 4 處：`-005` 引 `-004`（`配備：未配備 lower comfort screen`
vs `變體：Maserati（無逾時）`，零共用）× 2、`-006` 引 `-003` × 2。

**R-PMH53 末段之「無法機械判定者逐處列出供人讀」亦已實作** ——
每次執行印出本批全部交叉引用及其出處。

### 4.3 未涵蓋節號之具名（R-PMH52 之義務）

lint 輸出末尾固定印出：

```
⚠ 本 lint 未涵蓋之 canon 節號（R-PMH52 之具名義務）：
    - §4.3 tc_title 之形態與字數
    - §4.4 Pre-Condition 不得含動作
    - §5.7 同一觸發之後果是否應合併
    - §7 負向案例之配置
    - §8.2/§8.3 拆分是否恰當
    - §8.4.1 造值（推論寫成斷言）
    - §8.5 Pre-Condition 範圍是否溢出
    - §8.7.3 變體條件是否逐字
    - §10.2 priority 之 rubric 是否切合內容
    以上皆須人讀。R-PMH52：lint 全綠不得作為 TC 可用之證據。
```

---

## 5. 步驟 5 —— batch 1 重寫：**28/28 PASS**（停止條件 9 未觸發）

### 5.1 §四六類違規之逐項修正

| § | 違規 | 修正 |
|---|---|---|
| 4.1 | §10.5 三條單步 | `-002`／`-003`／`-006` 各補 record／check 兩步 |
| 4.2 | §5.1 `observe` 8 處 | 全改 `Read … and check that …`／`Read … and record …` |
| 4.3 | §5.2B/§5.5 Final Step 無驗證意圖 | 八條之末步皆含 `check that …` |
| 4.4 | §4.3.1 上半非 verbatim（4 條） | **八條上半全部改為 `source_clause` 之逐字子句**；`-003` 之 `automatically equals Accept` **已刪除**（§8.4.1 造值） |
| 4.5 | markdown 粗體（3 條） | 全部移除 |
| 4.6 | §11 彎引號／UI 標籤 | 彎引號改直引號；`the Accept button` → `the "Accept" button` |
| 4.7 | 交叉引用 4 處錯 | `-005`↔`-006` 成對、`-002`↔`-003` 成對，並改寫 axis 使其語意可機械比對 |
| 4.8 | §8.5 PC 溢出 | `-001` 移除 `non-Maserati` 與 ignition 分支條件；`-002` 移除 `non-Maserati`；**`-003` 保留**（逾時本身即 Maserati 之差異點） |

### 5.2 `-003` 之造值已刪 —— 逐字對照

| | 修正前 | 修正後 |
|---|---|---|
| `test_item` 上半 | `The system allows the user to wait for the screen to timeout, **which automatically equals Accept**.` | `The user is able to either press the Accept to go directly to their last mode screen or wait for the screen to timeout.`（**source_clause 之逐字整句**） |
| ER step 2 | `… the last mode screen is displayed, **the same outcome as pressing Accept**` | `The disclaimer screen is removed without user input and the last mode screen is displayed` |

**規格逐字只有 `or wait for the screen to timeout`，未言逾時等同 Accept。**

### 5.3 **新漏 1 對 batch 1 之直接影響**（本輪自 PDF 補入）

`SU9.1` 載「按 Power Off／Screen Off 於 splash 或 disclaimer 期間**會重設逾時**」。
該子句**於 SYS1 不存在**，故：

- `-003`（逾時路徑）之 procedure step 2 改為
  **`Without pressing any hard key or the "Accept" button, wait for the
  disclaimer screen to time out …`**
- `-004`（Maserati 無逾時）同樣加該限定

**若依 SYS1 產出，此限定無從得知，該二條 TC 會在按鍵情境下給出錯誤結果。**
**R-PMH50 之第二次實證。**

### 5.4 lint 輸出

```
28/28 PASS
```

（另跑 `check_state_consistency.py` exit 0、`check_granularity.py --check-doc-sync` exit 0。）

---

## 6. 步驟 6 —— `tc_id` provisional 防護

`check_write_back.py` 新增 **(d) `tc_id_not_provisional`**。
**四項故意失敗全部攔下**：

```
[a] 攔下 ✅  blank_precondition
[b] 攔下 ✅  start_row_source（並認出該值來自 outline_map 之 row_036_customer）
[d] 攔下 ✅  (d) tc_id_not_provisional FAILED — 批次 'batch01' 之
             tc_id_status = 'provisional'。臨時編號不得寫回工作簿。
[c] 攔下 ✅  row_count_delta
範圍向 PASS ✅
```

> **實作時之一處自錯**：首版於 `self_test()` 內用了 `ROOT`，
> 而該檔無模組層 `ROOT`（`NameError`）。已改為 `feature_dir`，
> 修正時依 R-PMH41 驗命中數（1 處）。**自測因而 exit 1，是它自己攔下自己。**

---

## 7. 未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | **OPEN** | **交付**（§8.4.3） |
| **DR-PMH2** | **Power Moding State Matrix Excel**（新） | **OPEN** | `Power Transitions` 批之 ch 9 部分 |
| **DR-PMH3** | **`SU9.)`／`SU9.1)` 是否應在 037**（新） | **OPEN** | `Disclaimer Screen` 之覆蓋完整性 |

**合計未結 3 筆**（本輪 +2）。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，六項。**

1. **重寫後之 batch 1 仍未經人讀覆核。** 28/28 只證明**已編碼之規則**通過；
   §4.3 之新檢查（`test_item` ⊆ `source_clause`）確保上半為 verbatim，
   **但不保證選對了子句** —— 例如 `-001` 取 `SU1.)` 之載入/Accept 兩句，
   是否應含前面之 splash 時序，**須人讀**。

2. **6-gram 覆蓋率之 30% 門檻無來源。** 與 08 包 G1 之 `0.35` 同型 ——
   它剛好把 p8 之 4 句分成 1 真漏 ＋ 3 假象。**未以錨點檢驗其鑑別力**，
   亦未做 must-hit（若門檻取 20% 或 50%，分類會不會變，未測）。

3. **方向二只做到句級，未做段落級。** 若 PDF 有一整段被改寫為不同措辭
   （非逐句可比），本法看不見。p9 之狀態矩陣是**因表格切分**才被抓到，
   屬僥倖而非設計。

4. **`DR-PMH3` 所指之 leaf 母體缺口，其影響面未量。** 若 SYS1 對 7.x 漏了
   SU9／SU9.1，**其他章是否也漏了「最末幾條」，未查** ——
   本輪只發現 7.x 之末尾被截斷，未系統性檢查每章之末則是否對得上 PDF。
   **這是本輪最該追而未追者。**

5. **`-003`／`-004` 之「不按任何硬鍵」是我自 PDF 補入之限定，而該限定
   在 037 中無對應 leaf。** 依 §8.4.2，**以無 leaf 之規格內容限縮 TC 之
   條件，是否越界**，本包未判 —— 我判斷其為「使既有 leaf 之驗證正確」
   而非「新增涵蓋」，故補入；**但這是我的判斷，須覆核。**

6. **lint 之 28 項仍無 must-not-hit 之完整對照。** 七項新檢查之 must-hit
   已跑，**但「正確之 TC 不得被誤判」只由重寫後之 28/28 間接證明** ——
   未構造「刻意合法但接近邊界」之案例（R-G9 之範圍向）。

---

## 9. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— `-003` 之造值已刪，三處不造值具名 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | 雙向複驗發現**任一新漏句**（除 7.1 外） | **⚠ 觸發** —— **三處**（§3.4–3.6），其一使兩條需求不在 48 leaf 內。已登記 A-PMH14、開 `DR-PMH2`／`DR-PMH3` |
| 8 | 任一新檢查之 must-hit 未 FAIL | **未觸發** —— 七項全 FAIL（R-PMH53 加強一次後） |
| 9 | 重寫後 lint 仍有 FAIL | **未觸發** —— **28/28 PASS** |

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 13 — batch 1 reworked, bidirectional spec diff finds 3 new gaps
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DATA_REQUESTS.md \
           features/power_moding/RULINGS.md \
           features/power_moding/generated/batch01.json \
           features/power_moding/tests/fixtures/batch01_prerework.json \
           features/power_moding/scripts/bidirectional_spec_diff.py \
           features/power_moding/scripts/check_write_back.py \
           features/power_moding/scripts/gen_batch01.py \
           features/power_moding/scripts/lint_batch.py \
           features/power_moding/docs/reports/bidirectional_spec_diff.md \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/13_batch1_rework.md \
           features/power_moding/docs/upstream/13_batch1_rework.md
```

- **未動 `docs/runtime/`**（profile 已落檔，本輪不再動）。
- **未動任何他 feature 之檔案。**
- `feature.yaml`／`DECISIONS.md`／`PLAYBOOK.md`／`framework.md` 本輪未改。
- pathspec 逐項寫全名（R-PMH3(c)）。
- ⚠ 上次提交時 index 內有併行 session 之 20 個 `vehicle_setting` 檔，
  已由 pathspec 隔開；**本次仍須帶 pathspec**。

### 10.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short`／`git diff --cached --name-only` | 3 |
| **改狀態 git** | `git add` ＋ `git commit`（**12 包**，Pei 指示，帶 pathspec） | 2 |

**12 包已提交為 `a6bb7a1`**（依 R-PMH48 由執行層回報）。**13 包尚未授權。**

---

## 11. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **`DR-PMH3`** | `SU9.)`／`SU9.1)` 是否應在 037 —— **若應而未含，48 leaf 之母體即為低估** | `Disclaimer Screen` 之覆蓋完整性 |
| **`DR-PMH2`** | Power Moding State Matrix Excel（規格稱 `shall not be developed without following`） | `Power Transitions` 批之 ch 9 |
| **§8 第 4 項** | **每章末則是否系統性被截斷** —— 本輪只發現 7.x 之末尾被截，未全查。**本輪最該追而未追者** | 建議：優先 |
| **§8 第 5 項** | 以無 leaf 之規格內容（SU9.1）限縮既有 TC 之條件，是否越界 §8.4.2 | 否 |
| 重寫後 batch 1 之人讀覆核 | 28/28 只證已編碼之規則通過 | 下一批之前 |
| 13 包之 commit 授權 | pathspec 見 §10（13 路徑） | 否 |
