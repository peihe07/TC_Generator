# 上繳 01b：機制文件建置（S1／S5／S3）

執行層：Opus5（Claude Code）｜日期：2026-08-21｜純文件建置，新規 0 條

## 1. 各檔變更清單

### S1 — 舊規標 superseded（repo 外，`/Users/peihe/Work/09_作業流程與單位規範/02_TC Design Flow & Standard/`）

5 檔**全數存在，全數已標**，無跳過者：

| 檔案 | 原首行 | 處置 |
|---|---|---|
| `ASPICE_SWE6_Test_Case_Writing_Rules_v2.md` | `# ASPICE SWE.6 Test Case 撰寫規則` | 檔首插入 |
| `ASPICE_SWE6_Test_Case_Writing_Rules.md` | `# ASPICE SWE.6 Test Case 撰寫規則` | 檔首插入 |
| `ASPICE_SWE6_AI_Instruction.md` | `## 0. Purpose` | 檔首插入 |
| `ASPICE_SWE6_AI_Instruction_20260507.md` | `## 0. Purpose` | 檔首插入 |
| `ASPICE_SWE6_AI_Instruction_mygpt.md` | `## 0. Purpose` | 檔首插入 |

- 逐字照抄下放包之 6 行區塊，僅加標頭，**內文一字未動、未刪檔**
- 具冪等保護：偵測首行已為 `> **SUPERSEDED` 則跳過，重跑不重複插入
- 5 檔 mtime 皆變為 `Aug 21 14:41`；同目錄 `Test Case Design Method 判斷規則.md`
  不在清單內，未動（mtime 仍為 `Apr 21 10:02`）
- 此路徑非 repo、非交付物，變更可逆（刪除檔首 7 行即復原）

### S5 — 裁決台帳

| 檔案 | 變更 |
|---|---|
| `docs/fw036/RULINGS_LEDGER.md` | **新建**。12 筆裁決（R-1～R-5、S1～S6、N-1）照下放包表格逐字落檔 |
| `docs/fw036/FEATURE_ONBOARDING.md` | 新增 `### 8.9 包規模與裁決引用（S5）`，8 行 |

台帳除下放包指定之表格外，另加一節「條文落檔位置」，將 12 筆編號對應到
條文全文所在（canon 章節／`FEATURE_ONBOARDING.md` §8.9／`lint036.py` docstring），
以落實「條文全文僅落檔一次，各包引用編號不重抄」之規則 —— 無此對照則
「引用編號」無從查證。此為表格之索引補充，未新增任何條文。

### S3 — gate 政策

| 檔案 | 變更 |
|---|---|
| `scripts/lint036.py` | module docstring 增 4 行：`--gate` 保留但尚不啟用、啟用時機為尾批、現階段啟用將使既有交付本 exit 1、條文指向 `RULINGS_LEDGER.md` |

`--gate` 旗標行為未改（預設關閉，本包未啟用）。

## 2. 章節編號之偏離（1 項）

下放包指定插入 `FEATURE_ONBOARDING.md` **§7 handoff contract 末**，
但該檔 §7 實為 `RD-1 packaging (Phase 7)`，內容為 RD-1 交付文件之排序；
**handoff 契約實際位於 §8「下放包與上繳包契約」**（§8.0～§8.8）。

依內容而非編號插入，落於 §8 末、§8.8 節奏之後，編為 **§8.9**。
未動 §7。若分析層本意確為 §7，請於下批指正。

## 3. pytest 結果

```
$ .venv/bin/python -m pytest tests/test_lint036.py -q
56 passed in 0.12s

$ .venv/bin/python -m pytest -q
8 failed, 1004 passed, 15 skipped, 69 warnings in 31.55s
```

**8 項失敗經證實為既存，與 01a／01b 無關。** 證明方式：將本包三處
tracked 變更（canon、FEATURE_ONBOARDING、lint036）`git stash` 後重跑
相同測試檔，得**完全相同之 8 項失敗**。失敗內容為
`features/user_profiles/scripts/` 三檔之 openpyxl save 呼叫未登錄於
`KNOWN_VIOLATIONS`（`test_single_write_path`）與 `test_intake_scaffold`
之 subprocess 失敗，皆位於本包未觸及之路徑。

`scripts/lint036.py` 本身仍為 openpyxl save 零呼叫，未列入該基線。

## 4. 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項：**

1. **N-1 已落檔為 ACTIVE，但 lint 實作尚未跟上 —— 本包最重要之缺口。**
   台帳 N-1 與 01a 寫入之 canon §11 均明訂「item 之尾句號落於**續行**時，
   該 item 仍屬違規」。現行 `lint036.py:n_exempt()` 仍豁免無 `a./b.` 標記
   之縮排續行，故 HFP 之 `duplicate contact entry is created.` 未被計入，
   全語料 N=6,703 而非 N-1 所蘊含之 6,704。00c 之 1 行差額由此正式解消：
   **答案為 6,704**。本包為純文件建置，未改 lint 程式碼；此變更（移除
   `n_exempt()` 之續行豁免分支）連同 8 本重跑須另包執行 —— 已見
   `docs/fw036/handoff/00d_n_continuation.md` 到位，惟本次未受指派執行，
   故 lint 現值與 N-1／canon §11 之落差**於本包交付時點仍然存在**。
2. **S1 標記僅涵蓋 5 檔，同目錄其他素材未評估。** 同目錄尚有
   `Test Case Design Method 判斷規則.md`（2026-04-21）與
   `Common Mistakes in Test Case Design_20260120.pptx`；下放包未列，
   本包未動。前者與 canon §12 Design Method 表格主題重疊，是否亦
   superseded 未經判斷。另，`09_` 目錄下其他子目錄未搜尋。
3. **台帳未回頭涵蓋既有裁決體系。** `RULINGS_LEDGER.md` 僅載本輪 12 筆；
   而 `FEATURE_ONBOARDING.md` §9.2 已有全域條文 R-G1～R-G12、§9 有
   G-A～G-N 常規，各 feature 另有 `RULINGS.md`，00～00c 亦引用了
   R-TM7／R-TM13／R-VS18／§5a 等未落於本台帳之編號。S5 稱「引用未落檔
   編號 = 包退回」，但依此標準，本包自身引用之 R-TM13（見 01a §4）
   即未落檔。台帳之涵蓋範圍與併入既有編號體系之計畫尚缺。
4. **S3 之啟用條件無可判之觸發點。** 「尾批（全數回修完成後）」未定義
   為何種可查證狀態（8 本 lint 全綠？某 workbook_state？某 tag？），
   亦無人負責在該時點翻開旗標。現況為政策存於 docstring，無機制保證執行。

另聲明：本包未 commit（屬 Pei）、未改任何 xlsx、未啟用 gate。

## 5. 引用之既有裁決

S1、S3、S5（本包執行之裁決本體）；N-1（見 §4 項 1）；
R-TM13（保留不刪之精神，用於 01a §4 之 hash 處置）；
R-1～R-5、S2、S4、S6（本包僅將編號落檔，條文本體由 01a 寫入 canon）。
台帳：`docs/fw036/RULINGS_LEDGER.md`。
