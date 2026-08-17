# 上繳 04 — User Profiles / 記載更正、條文入庫與四項實質查證

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`04a_rulings.md`（R-U13～R-U17）、`04b_rulings.md`（R-U18～R-U20、R-G4～R-G6）、`04c_tasks.md`（作業 1–7）

---

## 0. 結果一覽

| 作業 | 狀態 | 一句話 |
|---|---|---|
| 1 條文入庫 | ✅ | 十一條逐字；R-G4／R-G5／R-G6 另列全域段 |
| 2 R-G6 記載更正 | ✅ | 03 包 §8 之「git 未執行」已據實改為「執行了一次 `git checkout`」；§7.1 未動 |
| 3 ANOMALIES | ✅ | A-UP04 → RESOLVED（永久記載限制照錄）；A-UP09 維持 PENDING（R-U14）|
| 4 三閘反向驗證 | ✅ **6/6** | 三型注入各自轉紅並報出正確差額；037 原檔雜湊前後一致 |
| 5 `Service` 22 條 | ✅ 只出判讀 | **無一條符合 `[BLOCKED-NON-HMI]`**；另揪出兩條屬別的阻斷 |
| 6 14 節帶圖 | ✅ 逐節具名 | **不依賴 8／部分依賴 5／完全依賴 1**；`8.2` 為 DR 候選 |
| 7 R-G4 前置查證 | ✅ | home 兩讀者實為**第三種 schema**；改名不只安全，是**移除一個活的危害** |

**本輪未執行任何會改變 repo 狀態之 git 指令**（含 checkout／restore／stash／clean）；
唯讀之 `git status`／`diff`／`show`／`check-ignore` 有跑 —— **兩者分列於 §9**。

---

## 1. 作業 1 — 十一條入庫

R-U13～R-U20、R-G4～R-G6 逐字追加於 `RULINGS.md` §第三／四輪條文
（R19-2：原文貼入，不改寫、不摘要）。**R-G4／R-G5／R-G6 為全域條文**，
於該章內另立「全域條文」段落，與本 feature 條文分開。

**逐條之執行層回報**已附於同章之回報段，其中兩條為「明知而不做」：

- **R-U17 之刪除未執行** —— 屬 Pei，執行層不得代勞。`inputs/` 之 spec 副本仍在，
  `BASELINE.sha256` 之該列亦未動。
- **R-U14 之寫回未開工** —— x14 DV gate 未立，故不得開工。

---

## 2. 作業 2 — R-G6 記載更正

`docs/upstream/03_recon.md` §8 新增 **§8.1 git 動作**，把原句
「**git 未執行**」改為據實之：

| git 動作 | 對象 | 結果 |
|---|---|---|
| `git checkout <path>` | `data/spec_id_to_outline.tsv` | 還原至 01 輪版本；被丟棄者另存為 `data/recon_leaf_to_section.tsv` |
| `git status` / `diff` / `show` | 多處 | 唯讀 |

即：**執行了一次 `git checkout`（單一檔案）**，未執行 `commit`／`push`／`add`／
`reset`／`stash`／`clean`。

**§7.1 未動**（04c 明文：那段是對的）。更正段落內同時記下 R-G5 之判定 ——
**該次還原之作法為錯**，正確作法是兩版並存、上報、停手；
且 R-G5 明指這與 R-U13（`.gitignore` 那次）是**同一失效模式之第二次發生**：
以某條裁決之必然結果自推授權。**兩次都不是內容錯，是程序錯。**

---

## 3. 作業 3 — ANOMALIES 狀態

| 項 | 狀態 | 依據 |
|---|---|---|
| **A-UP04** | **RESOLVED** | R-U18，**永久記載限制已照錄並另加一段其效力** |
| **A-UP09** | **PENDING**（標題改記解除條件）| R-U14 —— 文字修補不構成 RESOLVED |
| A-UP02／A-UP06 | PENDING | 未動 |

A-UP04 之照錄後另加一段，講明其效力：

> **Phase 0 之 037 側數字沒有被複驗過，也永遠不會被複驗。**
> 那些數字量的對象是一份 Project 附件副本，該副本不在 repo，
> 本層無從對它算雜湊 ——「大小相同」不是「內容相同」。
> 03 輪所做的是**在一個有雜湊的物件上重新量一次**，
> 其結果恰好與 Phase 0 相符，**而「恰好相符」不等於「同一份檔」**。

A-UP09 之條內另記：**02 輪本層自陳之獨立判斷，於 R-U14 得到裁定確認** ——
02 包 §6 第 1 項寫「現行防線是一段散文，沒有一道機器檢查會在有人再次
`wb.save()` 時出聲」，R-U14 把那句話變成了解除條件本身。

---

## 4. 作業 4 — 三閘之反向驗證：**6 / 6 PASS**

腳本：`scripts/verify_recon_gates.py`（可重跑）。

**量測條件**：對 `inputs/` 之 037 作**位元組複本**（`tempfile.mkdtemp`，repo 外），
以 openpyxl 改複本之 `Analysis Report`，再以與 recon 相同之判準
（col 7 `Categorization` 逐列計數，`.strip()` 後精確比對）重量。

| # | 向 | 結果 |
|---|---|---|
| 1 | 原檔未注入 → 三閘全綠 | PASS |
| 2 | **複製 ＋ openpyxl 重存但不改資料 → 仍全綠** | PASS |
| 3 | A 改一列 `Functional Requirement` → `Heading` | PASS：FR **−1**、Heading **+1** 同時轉紅，Out of scope 不動 |
| 4 | B 增一列 `Functional Requirement` | PASS：FR **+1** 轉紅，另二閘不動 |
| 5 | C 刪一列 `Out of scope` | PASS：Out of scope **−1** 轉紅，另二閘不動 |
| 6 | `inputs/` 原檔未被觸碰 | PASS：SHA256 前後皆 `9d176dde…` |

**第 2 向是刻意設計的**：若不先證明「複製＋重存而不改資料仍全綠」，
後面每一個紅燈都可能是 openpyxl 重存造成的，而不是注入造成的。
**沒有那一向，另外三向證明不了它們想證明的事。**

**差額之可讀性一併驗**：三閘不只轉紅，且各自報出正確之 `±n`
（A 案同時報 −1 與 +1，正是「一列從甲類被改成乙類」之形狀）。

### 4.1 標「未實測」而非 PASS（canon）

| 未實測項 | 何以 |
|---|---|
| `heading_count` 對「欄值為 `Heading ` 尾隨空白」之容忍度 | 判準以 `.strip()` 正規化，**該情形量不出差別**，故其行為未經注入證明 —— 不可能失敗者不標 PASS |
| 三閘對「`Categorization` 整欄空白」之反應 | 該情形下三閘皆為 0 而全數轉紅，惟其**報出之差額是否可讀**未經測；此情形在真實 037 上不會發生，故不注入 |

### 4.2 一項須講明之風險界線

本檔以 openpyxl 存回複本，而 **A-UP09 記 openpyxl 存回會摧毀 x14 DV**。
於此**無妨且刻意如此**：本檔之對象是 **037 之資料**，不是 **036 母本之結構**，
037 亦不在寫回路徑上。**該風險僅適用於 036 表單** —— 已寫入腳本 docstring，
以免日後有人讀到這裡以為 A-UP09 被繞過了。

---

## 5. 作業 5 — `Service` 22 條之類別查證（**只出判讀，不自裁**）

**量測條件**：`Sub Categorization` == `Service` 且 `Categorization` ==
`Functional Requirement` 之列，逐條讀其 `Requirement Description` 全文。
**實得 22 條**，與 03 輪之計數相符。

### 5.1 判讀：**無一條符合 `[BLOCKED-NON-HMI]`（R-C38）之判準**

R-C38 之判準為「既未委派予外部文件，**亦非任何介面可觀察之行為**，
於本 feature 全部 spec 內無可觀察端」。**22 條全部有可觀察端**，
其分別只在**要幾步才看得到**：

| 群 | 條數 | 可觀察端 | 例 |
|---|---|---|---|
| **A 直接可觀察** | 9 | 單一畫面或單一動作即可讀 | `PROF-002-03`（PU1088 顯示）、`PROF-056`（welcome popup 出現）、`PROF-124`（Valet 下按記憶座椅只動座椅）、`PROF-127`（手套箱狀態回復）、`PROF-131`／`132-02`（SPAAK）、`PROF-030-02`、`PROF-033`、`PROF-119` |
| **B 需來回一趟（round-trip）** | 13 | 「存」本身在內部，**而其結果讀得出來** —— 設定→key cycle／切換→讀回 | `PROF-001-01`／`004-01`／`004-03`／`004-04`／`005`／`006-01`～`-03`／`007-01`／`008`／`032`／`001-03`／`070` |
| **C 無可觀察端** | **0** | — | — |

> **`Service` 不等於 non-HMI。** 逐條讀完之後，該欄看起來標的是
> **「這件事由誰執行」**（背景服務之儲存／回復），**不是「這件事看不看得見」**。
> Comfort `[BLOCKED-NON-HMI]` 之唯一成員 `044-02`（ECO HVAC 之降耗）
> 是**物理量而非介面量**，本 feature 22 條**沒有一條是那個形狀**。
>
> **故 03 輪所擔心的「一整章返工」不會發生** —— ch4 之 12 條全屬 B 群，
> 其 TC 寫得出來，只是每一條都需要一個「設定 → key cycle → 讀回」之結構。
> **那是測法之形狀，不是阻斷。**

### 5.2 反而揪出兩條屬別的阻斷，逐條具名

| leaf | sec | 事由 |
|---|---|---|
| `PROF-002-03` | `4.1.1` | 其內容為 **`PU1088` 顯示** —— `PU1088` 正是 **DR #4 所缺之二者之一**，且 `4.1.1` 落在 **R-U15 所定之阻斷範圍**（spec 4.1.1 Profile Setup 之 popup 引用）。**DR #4 到齊前不生成。** |
| `PROF-001-01` | `4.1` | 「store all profile-linked preferences **listed in PLP table**」—— PLP 表為 spec `3.1`–`3.5`，即 **A-UP02 之無覆蓋條文**（本輪 03 側已證實無人引用）。其 ER 之「哪些偏好」無來源可回溯；**「有偏好被保存」可驗，「是哪些」不可** |

**兩條皆非 `Service` 欄所致** —— 它們是被別的東西擋住，而**恰好落在這 22 條裡**。
若只看 `Sub Categorization` 欄，這兩條看不出來。

**不自裁**：`Service` 之歸屬分類屬 Tier 2（04c 明文）。本節只出判讀與證據。

---

## 6. 作業 6 — 14 節帶圖條文之判讀依賴

**判準**（04c 逐字）：**不看圖能否寫出可執行的驗證步驟。**

| 分類 | 節數 | 節 |
|---|---|---|
| **不依賴** | **8** | `5.1`、`5.2`、`7.2`、`7.2.1`、`7.5`、`8.4`、`12.2`、`14.1` |
| **部分依賴** | **5** | `4.6`、`6.2`、`9.1`、`10.2`、`11.4` |
| **完全依賴** | **1** | **`8.2`** |

### 6.1 完全依賴（DR 候選）

**`8.2`（NEWPR1.）全文為**：

> See flow for setting up a New Profile **above**. Connecting an account or
> downloading an existing Connected account are not pictured here.

**該節之全部內容就是那張流程圖。** 扣掉「圖裡沒畫連線帳號」這句否定說明後，
**條文一個可驗之步驟都沒有給** —— 不看圖寫不出 procedure，也寫不出 ER。

> **列為 DR 候選**：索取 `8.2` 之流程圖內容（或其文字化）。
> **注意其與 R-U15 之交集**：`8.2` 屬 ch8（Setup Flow），
> 而 R-U15 已擋住 `4.1.1` 之 popup；兩者**不是同一個缺口** ——
> 一個缺 popup 清單，一個缺流程圖。

### 6.2 部分依賴 —— 逐節具名可寫與不可寫者

| 節 | **可寫**（文字已給）| **不可寫**（在圖裡）|
|---|---|---|
| `4.6` | 狀態列預設有 Profile 鍵、可自訂移除、圖示隨登入者而變 | **圖示長什麼樣** —— ER 只能寫「與登入之 profile 相符」（Comfort 97 §2.8 前例）|
| `6.2` | 進車或啟用新 profile 時出 Welcome popup | **「prompts … within the default Welcome Popup (see above)」之 `see above` 指向圖** —— 有哪些提示不可知 |
| `9.1` | Tutorials 為列項；Connected Account／More Settings／Tutorials 之三個跳轉目標 | **「listed in the order according to Table EDPR1」之順序** —— 表即圖 |
| `10.2` | 觸發（點該行或 `i`）、「所有車輛移除 Memory Seat 段」之否定規則 | **該資訊頁之內容** —— `see example above` 指向圖 |
| `11.4` | 標題、兩欄名、兩段說明文字**皆逐字給定** | **「See table CPA2 for list items」之列項** |

> **`11.4` 值得單獨一提**：它把該畫面之**文案逐字寫在條文裡**，
> 只有列項在表中。**同一節裡，可驗與不可驗的界線畫得清清楚楚** ——
> 這是本批 14 節中唯一一個把界線寫明白的。

### 6.3 不依賴之 8 節，其共同形狀

八者皆為**行為條文帶一張示意圖**：`5.2` 連 popup 之文案與 id 都給
（`"Max Profiles reached. Delete to create a new one." (PU0584)`），
`7.2`／`7.2.1` 逐項列出 popup 上有什麼，`8.4` 給完整之 avatar 選取規則。
**圖是佐證，不是內容。**

> **03 輪只數了 14 這個數，沒問過這個問題。** 數完之後看起來像 14 個風險，
> **問完之後是 1 個真缺口、5 個要小心措辭、8 個沒事。**

---

## 7. 作業 7 — R-G4 之前置查證與實作

### 7.1 前置查證：home 兩讀者實際讀的是什麼

**這一步是 R-G4 明文要求的前置，其結果比預期更值得記。**

`features/home/data/spec_id_to_outline.tsv` —— **第三種 schema**：

| 檔 | 欄 | 列 | 產出者 |
|---|---|---|---|
| `features/home/data/…` | `spec_id / outline / desc`（3 欄）| 107 | home 之 `build_outline_map.py` |
| `features/user_profiles/data/…` | `section_id / outline_number / polarion_id / phys_row / chars`（5 欄）| 169 | 本 feature 之 `build_outline_map.py` |
| `scripts/recon.py` 之產物 | `req_id / outline / polarion_id / spec_reference / title`（5 欄）| 180 | recon |

**兩個讀者皆以位置取欄**：

| 讀者 | 取法 | 期待 |
|---|---|---|
| `lint_tcs.load_outlines` | `r[1]` | 第 2 欄 = outline |
| `make_batch_context.load_outline_to_chapter` | `CHAPTER_RE = ^([A-Z]{2,4})` 比對 `parts[0]`，映 `parts[1]` → chapter | 第 1 欄 = `HSD1`／`HSS4` 之類 |

### 7.2 結論：改名不只是安全，是**移除一個活的危害**

若 recon 之產物落在該檔名上：

| 讀者 | 後果 |
|---|---|
| `make_batch_context` | 第 1 欄變成 `SWE1-HMI-PROF-…`，而 **`^([A-Z]{2,4})` 會命中 `SWE`** —— 於是**每一個 outline 之 chapter 都變成 `"SWE"`**。**不是崩潰，是一個安靜的錯答案。** |
| `lint_tcs` | 第 2 欄仍是 outline 故不崩，惟其列集由「全 spec outline」變成「被引之子集」—— **沒被任何 leaf 引用的 outline 會開始 lint FAIL** |

> **兩個都不會出聲。** 一個給錯答案，一個給過嚴的檢查，
> 而 `git status` 只顯示一個 `M`。**R-G4 要的前置查證，查出來的正是這個。**

### 7.3 實作

| 改動 | 內容 |
|---|---|
| 輸出檔名 | `data/spec_id_to_outline.tsv` → **`data/recon_leaf_to_section.tsv`**（另二處文件字串一併改）|
| **新增前置檢查** | `write_data_file()` —— 目標存在且內容不同即 **`sys.exit` 中止**，**不備份、不還原**（R-G5：兩者皆屬 Pei；且一個偷偷留副本的腳本只是把同一個意外延後）|

**判準刻意不依賴 git**：**一個腳本不該需要版本控制才知道自己正要毀掉東西。**
內容相同即 no-op 通過（重跑安全），不同即停。

**訊息分三支，講明是哪一種不同** —— 第一版只寫 "different content"，
**而它第一次觸發時，資料其實完全相同、只差註解行**，讀者會去找一個不存在的
「另一個表」。現行三支：

```
the DATA IS IDENTICAL — only comment lines differ … 手工註解會被重跑靜靜抹掉
the COLUMNS DIFFER    — 另一個表恰好同名，正是 R-G4 存在的理由
the DATA DIFFERS      — 來源移動了
```

### 7.4 反向驗證：**5 / 5 PASS**

| 向 | 結果 |
|---|---|
| 目標不存在 → 寫入，不中止 | PASS |
| 內容完全相同 → no-op 通過 | PASS |
| 僅註解行不同 → 中止，判為「資料相同」 | PASS |
| 欄名不同 → 中止，判為「另一個表」 | PASS |
| 資料列不同 → 中止，判為「來源移動」 | PASS |

`recon.py` 已於本 feature 實跑，三閘仍 PASS，`recon complete: leaves=180`。

### 7.5 一個順帶之處置

`data/recon_leaf_to_section.tsv` 原帶有本層 03 輪手寫之表頭（解釋當時的碰撞）。
**該表頭已移除** —— R-G4 落地後，那段說明屬條文與上繳包，不屬一個生成檔；
留著它會使 recon 每次重跑都被自己的 guard 擋下（實測如此）。
**說明未遺失**，見 R-G4 條文與 03 包 §7.1。

---

## 8. R-U19 與 R-U20 之落地

| 條 | 落地 |
|---|---|
| **R-U19** | 新建 `data/generation_sections.tsv`（**133 列**，含 `test_set` 欄）；`expected_cited_sections.tsv` **未改**（仍 135 列）。`feature.yaml` 以 `cited_sections` / `generation_sections` 兩鍵分列，各具名其用途 |
| **R-U20** | `feature.yaml` 新增 `layer2`，八組。**逐組以 037 之 180 leaf 實測，八組全部相符，合計 180** |

**八組之實測（量測條件：`Categorization == Functional Requirement` 之列，
依其 `HMI Source ID` 之章別歸組）**：

| Test Set | 裁定 | 實測 | 133 集合中之節數 |
|---|---|---|---|
| Preference Storage | 28 | **28** | 16 |
| Profile List | 40 | **40** | 27 |
| Defaults | 11 | **11** | 10 |
| Welcome Flow | 14 | **14** | 9 |
| Setup Flow | 25 | **25** | 20 |
| Editing | 25 | **25** | 24 |
| Connected Account | 6 | **6** | 4 |
| Valet Mode | 31 | **31** | 23 |
| **合計** | **180** | **180** | **133** |

---

## 9. 動作清單 —— 與「未執行 git」逐項對照（R-G6）

逐項列出本輪所有會改變 repo 狀態之動作 ——
**其中 git 欄一律為「否」**：

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案追加 | `RULINGS.md`（＋十一條）| 否 |
| 2 | 檔案編輯 | `docs/upstream/03_recon.md`（＋§8.1）| 否 |
| 3 | 檔案編輯 | `ANOMALIES.md`（A-UP04／A-UP09）| 否 |
| 4 | 檔案新建 | `scripts/verify_recon_gates.py` | 否 |
| 5 | 檔案編輯 | `scripts/recon.py`（R-G4）| 否 |
| 6 | 檔案新建 | `data/generation_sections.tsv` | 否 |
| 7 | 檔案編輯 | `data/recon_leaf_to_section.tsv`（移除手寫表頭）| 否 |
| 8 | 檔案追加 | `feature.yaml`（`layer2`／兩個 section 集合）| 否 |
| 9 | 檔案新建 | `docs/upstream/04_verification.md`、`docs/INDEX.md` 編輯 | 否 |
| 10 | **暫存目錄之建立與刪除** | `tempfile.mkdtemp()` 之 037 複本 ×4 | 否（repo 外，用完即刪）|
| 11 | 唯讀讀取 | `inputs/` 之 037（SHA 前後一致）、`features/home/scripts/*`、`spec-index/` | 否 |

**未執行任何會改變 repo 狀態之 git 指令**：`git commit`／`push`／`add`／
`checkout`／`restore`／`reset`／`stash`／`clean`／`rm`。

**已執行之唯讀 git 指令**：`git status`／`git diff`／`git show`／
`git check-ignore`（查 §7.1 之三種 schema 與各檔現況時用）。
**它們不改工作區、不改 index、不改 history。**

> **本節原寫「亦未讀取 git 狀態（本輪連 `git status` 都未跑）」—— 該句為誤，
> 於本輪覆核時自查發現並更正。** 唯讀 git 指令確實跑過。
> **這正是 R-G6 所防之形態**：摘要寫得比內文乾淨。
> R-G5 之禁令針對「改變狀態」之操作（含 checkout／restore／stash／clean），
> **而「未執行 git」若被寫成連唯讀都沒跑，那是另一個不實陳述** ——
> 兩者都不該出現。故本節自此分兩欄列，不再以一句「未執行 git」概括。

**未動之檔**：`inputs/` 任何檔（含 R-U17 之 spec 副本 —— 刪除屬 Pei）、
`BASELINE.sha256`、`data/expected_cited_sections.tsv`、`data/outline_map.json`、
`data/spec_id_to_outline.tsv`、`data/spec_popup_ids.tsv`、`DECISIONS.md`、
`docs/handoff/*`、`spec-index/`、`.gitignore`、他 feature 之任何檔案。

> `scripts/recon.py` 為**全域**檔而非本 feature 檔，本輪動了它 ——
> R-G4 明文授權，且其前置查證（§7.1）已先完成。

---

## 10. 本包是否仍有該驗而未驗者 —— 獨立判斷（不得省略）

**有，五項。**

| # | 該驗而未驗 | 性質 |
|---|---|---|
| 1 | **R-G4 之改名未在 `features/home` 上實跑驗證** —— 本層只讀了 home 兩讀者之程式碼，**沒有真的對 home 跑一次 recon** 看它是否仍正常 | **真缺口**。§7.2 之危害是**推導**出來的（regex 會命中 `SWE`），不是**觀察**到的。要證實它，須對 home 跑一次 recon —— 而那會覆寫 home 之檔，**本輪不做**（不在授權範圍）。建議由分析層決定是否值得一驗 |
| 2 | **`comfort`／`sxm`／`amfm`／`projection` 之 `spec_id_to_outline.tsv` 現況未掃** | **真缺口**。若其中任一份已是 recon 之形狀，那個 feature 現在就帶著 §7.2 之錯答案。本輪只查了 R-G4 點名之 home |
| 3 | **`Service` 22 條之 B 群「來回一趟」測法未實際寫過一條 TC** | 記載限制。判讀是「寫得出來」，而**沒有真的寫一條出來證明它** |
| 4 | **`8.2` 之圖確實讀不到 —— 但本層沒試過讀** | 記載限制。判讀依據是 `outline_map.json` 之文字欄只有 `(image: …)` 標記；**未嘗試自 xlsx 抽出內嵌圖片**。Comfort A-CF23 之結論是「不是缺件，是缺讀取能力」，本 feature 未做到那一步 |
| 5 | **A-UP09 之 x14 DV gate 仍未立**（R-U14）| 已知，**且它擋著寫回開工**。本輪不在授權範圍，記於此以免下一包誤以為可以開工 |

**另記一件不在作業項內、本輪順帶查到的**：作業 4 之第 2 向
（「複製＋重存但不改資料仍全綠」）**原本不在我的設計裡**，
是寫到一半才意識到 —— **沒有它，另外三向證明不了任何事**，
因為每個紅燈都可能是 openpyxl 重存造成的。
**一組反向驗證需要一個「什麼都沒做」的對照組**，這一點值得寫進往後的慣例。

---

## 11. 待裁

1. **`Service` 之歸屬分類**（§5，Tier 2）—— 本層判讀為「無一條符合 R-C38」，
   但分類本身不自裁。
2. **`8.2` 之 DR** —— 是否開列（§6.1）。
3. **`PROF-002-03` 與 `PROF-001-01` 之處置**（§5.2）—— 前者落 R-U15 阻斷範圍，
   後者依賴 A-UP02 之 PLP 表。
4. **§10 第 1／2 項**是否值得一驗（對 home 實跑 recon、掃其餘四個 feature）。
