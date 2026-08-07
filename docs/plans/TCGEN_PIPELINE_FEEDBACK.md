# tcgen 跑法回饋評估 — 對 TC Generator 既有流程與 code 的影響

撰寫日期：2026-08-07
評估對象：`tcgen_package/`（FW036 remaining 262 leaves 的一次性生成包）
對照對象：`backend/`（app pipeline）+ `frontend/`（upload → configure → generate → review → export）

---

## 0. 這份文件在回答什麼

FW036 這批用 `tcgen_package` 跑完，不是走 app 的 generate 流程，而是用一組
腳本 + Claude Code 逐 parent 生成。結果是 **277 TC lint 全過、262 leaves 全覆蓋、
2 個 blocked、7 個 assumption marker、33 條 anomaly 有案可查、write-back byte 可重現**。

問題是：這套跑法裡哪些東西是「這個專案剛好需要」，哪些是「app pipeline 本來就缺、
應該補進 code」。這份文件把兩者分開，並給出可執行的改動清單。

結論先講：**tcgen 真正的貢獻不在 prompt，而在「輸入組裝」與「輸出把關」兩端。**
中間那段（LLM 怎麼寫 TC）app 其實已經比 tcgen 完整（`prompt_builder.py` 的
規則注入、sibling 契約、split mode 都更成熟）。缺的是頭尾。

---

## 1. 兩條 pipeline 的實際差異

| 維度 | app pipeline（backend/） | tcgen 這次跑法 |
|---|---|---|
| 生成單位 | 一列 requirement（`--batch-size` 預設 5 列一次 API call） | 一個 RD parent（含其下所有 leaf），逐 parent 落檔 |
| Spec context | `spec_matcher` 語意/embedding 比對出前幾名 section 文字 | 用 037 的 outline number **確定性**取 SYS1 section 原文，再補抓未被 037 分配的 descendant section |
| 圖像 | 無。`providers/` 只送文字 | spec PDF 是掃描件，逐頁 render PNG 一起送；OCR 只用來建 section→page 索引，不當內容來源 |
| 外部參照 | 無 | 自動展開 spec 文字裡的 `PUxxxx`，從 Pop Up List 撈定義塞進 context |
| Few-shot | 無 exemplar 機制 | done-region exemplars + **人工審過的 curated anchors**（`anchors.json` 優先） |
| Test Set | LLM 分類（`classify_test_sets`，跑 gpt-5-mini） | `section_to_testset.json` 事先裁決，per-parent override，生成端不得發明 |
| 把關 | `validator.py` 逐欄檢查，回 warning/error 給 UI | `lint_tcs.py` 是**硬 gate**，exit code 決定能不能進 write-back，規則逐條對應 instruction 的 § 節號 |
| 未決事項 | 無型別。不確定就進 reasoning 文字 | 三種機器可讀 marker：`blocked` / `assumption` / `write_back.flags_pending`，各自要帶 anomaly id |
| 寫回 | `writer.write_generated_results`：`insert_rows` 就地插列，無保護區 | `write_back.py`：三個 invariant 未過就中止，不產出可疑檔案 |
| 可重現性 | 無。xlsx 兩次跑出不同 bytes | 正規化 zip entry timestamp 與 `docProps`，同內容同 SHA256，digest 記在 commit 上 |
| 續跑 | job 層有，生成內容無 per-unit 落檔 | 每個 parent 一個 `generated/<parent>.json`，可 diff、可 resume、可單獨重跑 |

---

## 2. 這次真正產生價值的六個機制

### M1 — Per-parent context 組裝（`make_batch_context.py`）

不是「把 spec 丟給模型」，而是**先決定模型該看到什麼**：該 parent 的 leaf、
sibling rows、section 原文、未被分配的 descendant section、PU 定義、Test Set、
anchor TC，一次組成一個 JSON。

關鍵是 A-001 那個修正：037 不會為每個 SYS1 sub-section 都配 leaf，
`11.3.1` 的內文只是抽象句，真正可測的行為在 `11.3.1.1`。原本只抓 leaf + parent
section，會讓 10 個 parent 在沒有可測內容的情況下生成。**這是輸入組裝的 bug，
不是模型能力問題** —— 而 app 的 `_get_spec_context` 今天有同樣的盲點，
只是靠 embedding 相似度碰運氣。

### M2 — 圖像是一等輸入

Media HMI PDF 零可抽取文字。anatomy layout、preset bank 大小、資料夾結構這些
只存在於圖裡。tcgen 的做法是 OCR 只負責建索引（item code → page），內容判讀交給
模型看圖。app 完全沒有這條路徑（`providers/` 沒有 image 支援），
遇到掃描件規格書就只能空轉。

### M3 — Curated anchors 勝過歷史 exemplars

Browse Tab 在 done region 只有 1 個 exemplar，卻要撐 83 個 remaining leaf。
tcgen 改用這次審過的 COM-057 pair 當 anchor，因為它把 §8.5 的判斷
（catalog state 刻意不放 Pre-Condition、browse-supportedness 刻意放）**內建在例子裡**。
風格示範的價值來自「它示範了哪個判斷」，不是「它是舊的」。

### M4 — Lint 是硬 gate，不是建議

`lint_tcs.py` 每條規則都標出 instruction 的 § 節號，reviewer 可以直接跳到權威來源。
它已經 `import` 了 `backend/validator.py` 的 `VALID_DESIGN_METHODS` / `VALID_PRIORITIES`
—— 也就是說，**兩邊的合流已經開了一半，只是方向反了**：目前是專案腳本反向依賴 backend，
而不是 backend 擁有規則。

### M5 — 不確定性有型別

`blocked`（沒有可寫的東西）/ `assumption`（在未裁決的衝突上押了一個讀法）/
`flags_pending`（車型旗標待 Group 0 裁決）三種 marker，都強制帶 anomaly id 與
受影響 req_ids。因此 `docs/fw036/pending_passes.md` 才寫得出「裁決落地時這是工單，不是研究任務」，
每個 pass 都有檢索指令與驗收條件。

這是整套流程裡**最難用 prompt 取代的部分**：它是資料結構，不是措辭。

### M6 — Write-back 當成控制文件處理

三個 invariant 在寫之前就 assert：traceability（req_id 必須存在於 037）、
completeness（leaves 數 == rows 數）、done region（rows 10-332 前後 hash 相同）。
外加 ChangeHistory revision、framework sheet 同步、Remarks 欄承載 blocked 宣告。
blocked 的 leaf **仍然產生一列**，否則 ASPICE 稽核會看到一個沒人解釋的缺口。

對照 app 的 `writer.py`：直接 `insert_rows`，沒有保護區概念，沒有 completeness 檢查，
沒有 revision 紀錄。輸出是一個「看起來對」的 xlsx。

---

## 3. 回灌路徑分類

| 機制 | 歸屬 | 理由 |
|---|---|---|
| M1 context 組裝（descendant pull / PU 展開 / 確定性 section 取用） | **產品化進 code** | 與專案無關的通用缺陷；任何 SYS1 + spec 組合都會踩到 |
| M2 圖像輸入 | **產品化進 code** | 掃描件是常態不是例外；`providers/` 缺 capability |
| M3 anchors | **產品化進 code（機制）+ SOP（內容）** | 「reviewer 核可的 TC 成為 anchor」是機制；哪一筆是 anchor 是判斷 |
| M4 lint 硬 gate | **產品化進 code** | 規則已經有單一來源（instruction doc），只差把 gate 提到 backend |
| M5 blocked / assumption / flags_pending | **產品化進 code（schema）+ SOP（判斷）** | 型別進 schema；「什麼情況該 blocked」留給人 |
| M6 write-back invariants + 可重現 | **產品化進 code** | 這是 writer 該有的品質，與 FW036 無關 |
| RD-1 問題單 / framework 裁決 | **留在 SOP** | 是跨部門溝通產物，寫進 code 只會變過期常數 |
| Model 分派（Opus 給 ch11/13/14/23、Sonnet 給 ch16-18/21） | **留在 SOP** | 依 chapter 難度與額度動態調整，不該硬編 |
| Chapter 逐段 commit、pilot 先審再放量 | **留在 SOP** | 節奏是人的紀律 |
| `section_to_testset.json`、`anchors.json`、rows 10-332 邊界 | **專案一次性資產** | FW036 專屬；產品化時必須參數化，不可搬 |

---

## 4. 建議的 code 改動清單

### P0-1 — 把 lint 提為 backend 的 release gate

1. 將 `tcgen_package/scripts/lint_tcs.py` 的規則移入 `backend/`（例如 `backend/tc_lint.py`），
   讓 `validator.py` 與它共用同一份規則表，反向依賴解除
2. 移除硬編：`EXPECTED_TEST_GROUP = "MediaHMI"`、Test Set whitelist 來源改由 framework 注入
3. 在 export 前接上 gate；`--strict-validation` 改為「gate 是否阻擋」而非「warning 升級」
4. 每條 finding 保留 § 節號（tcgen 已經這樣做，別弄丟）

**驗收：** 對 `tcgen_package/generated/` 跑 backend 的新 gate，結果與 `lint_report.json`
完全一致（277 / 0 failed / 2 blocked / 7 assumption）。

### P0-2 — `writer.py` 加 invariants 與保護區

1. 新增 protected row range 概念（呼叫端指定，不硬編 10-332），寫前寫後 hash 比對
2. 加 traceability（req_id 必須在來源需求集合內）與 completeness（leaf 數 == row 數）assert
3. 加 xlsx 正規化（zip timestamp + `docProps`），讓輸出 byte 可重現
4. invariant 失敗時**不產出檔案**，而不是產出後警告

**驗收：** 移植 `tests/test_write_back.py` 的跨秒 idempotency 測試到 `writer` 層並通過。

### P0-3 — Context assembler 產品化

1. 抽出 `backend/context_builder.py`：以 requirement 為單位組裝 context
2. 補上 descendant section pull（A-001 的修正邏輯）
3. 補上外部參照展開（PU / 表格 / 交叉引用），來源以 config 宣告，不寫死 Pop Up List
4. `spec_matcher` 保留為 fallback：**有 outline number 就用確定性對應，沒有才用相似度**

**驗收：** 對 FW036 的 10 個 A-001 受影響 parent，assembler 產出的 section 集合
與 `batches/*.json` 一致。

### P1-1 — Provider 層支援圖像

`providers/base.py` 的訊息型別擴充為多模態，`anthropic_provider` / `openai_provider`
各自實作；上游加 PDF → PNG 的 render step 與 OCR 索引（只索引，不當內容）。

### P1-2 — 未決狀態進 schema

1. `tools/schemas.py` 加 `blocked` / `assumption` / `flags_pending` 三型別，各自強制 anomaly id 與 req_ids
2. Writer 把 blocked 列寫成 Remarks 帶原因、P/R 留白的真實列（不是跳過）
3. Review UI 顯示這三類 marker，並允許 reviewer 直接開 anomaly

### P1-3 — 生成單位改為 requirement parent + checkpoint

現在 `--batch-size 5` 是成本折衷，代價是 sibling 判斷跨批不穩、失敗要整批重跑。
改為 per-parent 生成 + `generated/<parent>.json` 落檔，可 diff、可 resume、可單點重跑。

### P2-1 — Anchor 管理

Review UI 加「設為此 Test Set 的 anchor」動作，寫進 framework 旁的 anchors store，
下次生成同 Test Set 時優先注入。這把 review 的產出從「這批對不對」升級成「下批更好」。

### P2-2 — Scorecard 接 lint gate

`first_pass_rate` 目前算的是 findings；改成「進 gate 前未修改即通過的比例」，
才是可對外報的數字。

### P2-3 — Pending passes 產生器

從 marker 自動生成 `pending_passes.md` 形式的工單（含檢索指令與驗收條件），
而不是手寫維護。

---

## 5. 風險與注意事項

1. **tcgen 是 FW036 專用的**：`EXPECTED_TEST_GROUP`、rows 10-332、column map（D/G/H/I…AH）、
   9 個 dropdown 字串都硬編。直接搬進 backend 會把一次性專案假設變成產品限制。
   每一項產品化前都要先問「這是規則還是這個 workbook 的形狀」。
2. **規則來源會漂移**：目前規則同時活在 `docs/runtime/ASPICE_SWE6_AI_Instruction.md`（prompt）、
   `backend/validator.py`（欄位檢查）、`lint_tcs.py`（gate）三處。合流時必須指定
   單一事實來源，否則 gate 與 prompt 會各自演化。
3. **兩種 schema**：generator 產的是 generation contract（`tc_title`、`split_flag`…），
   lint 檢的是 workbook-facing shape（`test_item`、`req_id`…）。這層 adapter 目前
   隱含在 tcgen 的落檔慣例裡，產品化時必須顯性化，否則兩邊欄位會慢慢對不上。
4. **anchors 會腐化**：anchor 是「被審過的判斷」，判斷會隨 RD 裁決改變。
   需要 anchor 失效機制（例如綁 anomaly id，裁決翻盤時自動標記待重審）。
5. **P-5 的教訓**：done region 的已知錯誤（A-005 等）被刻意延後，是為了讓
   「done region 不動」在整段生成期間維持為硬 invariant。**這個取捨值得保留成產品慣例**：
   一次修改只動一個區域，混修會讓 diff 失去證明力。

---

## 6. 建議節奏

| 階段 | 內容 | 產出 |
|---|---|---|
| 第一段 | P0-1 + P0-2 | export 前有真 gate，輸出可重現。這兩項不動 LLM，風險最低、對稽核收益最大 |
| 第二段 | P0-3 + P1-2 | context 組裝與未決狀態進 code，app 才有能力跑第二個專案 |
| 第三段 | P1-1 + P1-3 | 圖像與 per-parent 生成，讓 app 有能力接掃描件規格 |
| 第四段 | P2-* | anchors、scorecard、工單產生器，把 review 的產出變成下一輪的輸入 |

---

## 7. 一句話結論

這次 tcgen 證明的不是「Claude Code 比 app 會寫 TC」，而是
**「決定模型看到什麼」與「決定什麼准出門」這兩件事，目前只存在於一次性腳本裡**。
把 M1、M4、M5、M6 產品化，app 才會從「能生成」變成「能交付受稽核的文件」；
把 RD-1、framework 裁決、model 分派留在 SOP，是因為那些本來就是人的判斷，
寫進 code 只會變成明年沒人敢動的常數。
