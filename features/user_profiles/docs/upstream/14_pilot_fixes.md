# 上繳 14 — pilot 覆核之修正（D-1～D-5、S-1、N-1～N-3）＋ 15 包之 052f67d 處置

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`14_pilot_review.md`（覆核判定，無裁決條文）＋
  `15_commit_disposition.md`（R-U55、R-G12）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）
- 產物：`generated/` 16 檔 / 16 條 TC（修正後全文見 §7）

## 0. 全閘現況（修正後複跑）

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 16 條，**違規 0** |
| `lint_tcs.py --self-test` | **37 / 37**（原 28 ＋ G15 五案 ＋ G16 三案 ＋ G9 子層一案）|
| `lint_variant_labels.py` 反向 | **9 / 9**（原 7 ＋ N-1 兩案）|
| `lint_variant_labels.py --check` | 16 條，**違規 0** |
| `build_batch_context.py --selfcheck` | **8 / 8** |
| tamper `drop`／`add`／**`misplace`** | **三向皆紅** |

---

## 1. D-1（阻塞）—— priority 依 R-U5 全批複核

**判準（本輪明訂，逐條套用）**：

1. 落在 R-U5 **核心五類**（profile 建立／切換／偏好之儲存與回復／
   Valet Mode 進出／**資料遺失風險項**）→ **P0**
2. 邊界、非主路徑分支、主要功能之次要或進階操作 → **P1**
3. 輔助功能，失敗對主功能影響有限 → **P2**
4. **037 之 High/Medium/Low 為先驗，不覆蓋 rubric**（R-U5 逐字）

### 1.1 TC-002（`PROF-002-03`）—— **P2 → P0**

| | 修正前 | 修正後 |
|---|---|---|
| priority | `P2` | **`P0`** |
| 理由欄 | 「回復預設之未確認分支；非主路徑，**037 先驗 Low**」| 「回復原廠之分支 —— **資料遺失風險項**（R-U5／canon §10.2）；**037 先驗 Low 不覆蓋 rubric**」|

**認錯**：原理由把 037 之先驗當成判準本身，而 R-U5 明文其僅為先驗。
`Restore Settings to Default` 即回復原廠，正是 R-U5 逐字所列之資料遺失風險項。

### 1.2 連帶複核（全 16 條）——**再改 2 條**

| tc_id | leaf | 前 | 後 | 理由 |
|---|---|---|---|---|
| TC-005 | `PROF-048` | P2 | **P1** | 觸發為建立新 profile（主要功能），受測者為其次要性質（預設 profile 之存續）→ 次要操作 |
| TC-006 | `PROF-053` | P2 | **P1** | setup flow 之**非主路徑分支**（無連網配置），非輔助功能 |

**其餘 13 條維持**，其中兩處判斷須具名（見 §8 第 1 項之未驗清單）：

- **TC-003／TC-009（邊界）維持 P1**：R-U5 明列邊界為 P1，
  雖其所屬功能（profile 建立）屬核心五類。
- **TC-015／TC-016（Valet）維持 P0**：兩者同為「邊界／負向」形態，
  卻判 P0 —— 因其失效之後果是 **Valet Mode 可被繞過**（完整性），
  而 TC-003／TC-009 之失效後果是輸入體驗降級。
  **此一「以失效後果分」之 tie-break 為本輪所立，非 R-U5 明文**，
  已列入未驗清單待覆核。

**修正後分布**：**P0×6、P1×6、P2×4**（原 P0×5、P1×4、P2×7）。

---

## 2. D-2（阻塞）—— TC-004 指名受測偏好

| 欄 | 修正前 | 修正後 |
|---|---|---|
| `input_test_data` | `NA` | `Preference under test: Memory Profiles (Seats, mirrors, steering wheel) (3.5)` |
| 步驟 2 | `Change a Profile-linked preference without pressing the memory seat set or save hard or soft control` | `Adjust the seat, mirror and steering wheel positions` |
| 步驟 3（新增）| —— | `Leave the memory seat set and save controls untouched` |
| 最終步 | `Read the changed preference and check that it retains the value set in step 2` | `Read the three positions and check that they match step 2` |
| ER | 4 條 | 5 條（與步驟數同） |

**受測項之選定**：取 PLP 表 **3.5** 之逐字列項
`Memory Profiles (Seats, mirrors, steering wheel)` ——
本 leaf（5.9）講的正是「不必按記憶座椅控制也會存」，
故受測偏好取記憶座椅那一項最能證其斷言。**取自 PLP 表逐字，未自擬。**

---

## 3. D-3（阻塞，2 條）—— ER 改列實際列項

### 3.1 TC-003（`PROF-021-01`，5.2）—— `note PRACC7.2` 展開

| | 內容 |
|---|---|
| 修正前 ER3 | `The Add New Profile button is not present, the icon and the string **described in note PRACC7.2** are not present, and “Max Profiles reached…” (PU0584) is displayed` |
| 修正後 ER3 | `The Add New Profile button is not present; the icon and the string **“This icon is associated to settings that are specific to your profile and are not shared across the vehicle”** are not present; and “Max Profiles reached. Delete to create a new one.” (PU0584) is displayed` |

字串出自 **5.1.2（PRACC7.2）之 `pdf_text`，逐字**。
`specification_reference` 併列 `5.1.2`（具名理由記於 `REF_EXTRA`）。

**連帶發現（本輪新增之 pre-condition）**：PRACC7.2 末句自陳
「This logic is not applicable for **7” screens**」——
7 吋車上該圖示與字串**本來就不存在**，其「不存在」無從作為判準。
故加 pre-condition `The vehicle does not have a 7-inch screen`。
**若不加，這條 TC 在 7 吋車上會假通過**（§7 false pass）。

### 3.2 TC-013（`PROF-111`，11.4）—— Table CPA2 之列項展開

修正前 ER2 結尾：`…and **the list items of Table CPA2**`
修正後（§6.1 之 `a./b./c.` 子層，逐字取自 PDF p17）：

```
…and the rows of Table CPA2:
   a. Personalization — Presets, Menu Bar Order, App Drawer Favorites, and more
   b. App Store Download
   c. Marketplace — Access to Marketplace
   d. Connected Navigation — Personalized Favorites, Recents, and Predictive Navigation
   e. Connected Profile App (See Connected Personal Account HMI)
```

**未造值之處具名**：該表為兩欄（`Connected FCA Account` / `Local Profile`），
而 **PDF 文字層已把表格攤平**，各列究竟屬哪一欄**無法自文字層還原**。
故 ER 只列**列名與其說明**，**不宣稱欄別歸屬**（§8.4.1）。
欲坐實欄別，須讀該表之版面（圖），列為未驗項。

### 3.3 **本項揭出一個更深的問題 —— `p17` 掛錯了節**

D-3 假定 must_carry 之 `p17 → 11.5` 會把列項帶進 TC-013。**它不會。**
TC-013 是 **11.4**；`p17` 只掛 11.5，故 11.4 之 context **拿不到那些列項**。

對 PDF p17 複位（N-2）後可見兩件事並存：

- 該表**實體印於 p17**，與 `CPA3`（＝11.5）同頁 → R-U49 之判讀成立
- 該表之**引用者**是 `CPA2`（＝11.4）：`See table CPA2 for list items`

**即：需要那些列項的 TC 拿不到，拿到的 TC 不需要。**
處置：`PAGE_TO_SECTION` 改為**多節**——`p17 → ["11.4", "11.5"]`，
引用者與實體所在者各一。`p14 → ["9.1"]` 不變。

修正後 `--selfcheck` 第 2 項：`PROF-111`（11.4）由 1 條變 **2 條** must_carry。

---

## 4. D-4（補閘）—— §5.2 步驟長度，**先紅再修後綠**

### 步驟 1 — 補閘（**未動任何 TC**）

`G15`：一般步 ≤12 詞、最終步 ≤18 詞、§5.1 例外之 intent 步（帶 `to …`）≤18 詞。

### 步驟 2 — **紅**（實際輸出，節錄）

```
違規 15
  G15 NR1L-UserProfiles-003: 步驟 3（最終步）21 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-004: 步驟 2（一般步）20 詞 > 12（§5.2）
  G15 NR1L-UserProfiles-004: 步驟 4（最終步）19 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-007: 步驟 2（最終步）19 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-008: 步驟 1（一般步）14 詞 > 12（§5.2）
  G15 NR1L-UserProfiles-010: 步驟 3（最終步）**28 詞** > 18（§5.2）
  G15 NR1L-UserProfiles-011: 步驟 3（最終步）20 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-012: 步驟 2（最終步）22 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-013: 步驟 2（最終步）19 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-014: 步驟 1（一般步）15 詞 > 12（§5.2）
  G15 NR1L-UserProfiles-014: 步驟 3（最終步）20 詞 > 18（§5.2）
  G15 NR1L-UserProfiles-015: 步驟 1（一般步）14 詞 > 12（§5.2）
  G15 NR1L-UserProfiles-016: 步驟 2（一般步）16 詞 > 12（§5.2）
  G15 NR1L-UserProfiles-016: 步驟 3（最終步）20 詞 > 18（§5.2）
  G9  NR1L-UserProfiles-013: 步驟 2 條 vs ER 7 條（§6）
```

**14 處 G15**，非 14 包所列之 3 處 —— 該包列的是抽樣（其文為「以下未被攔下」）。
**實際受影響者為 12 條 TC 中之 14 個步驟。**

**同時紅的 G9 是判準問題，不是 TC 問題**：D-3 之 `a./b./c.` 子層被當成 ER 行數。
canon §6.1 明允子層，故 `_lines()` 改為**只計頂層編號行**（改判準，不改案例）。

### 步驟 3 — 修（14 個步驟改寫，形態三種）

| 形態 | 例 | 處置 |
|---|---|---|
| 一步塞多個動作 | TC-010 步驟 3（28 詞：ignition cycle ＋ 開清單 ＋ 查核）| **拆為 3 步**，ER 同步由 3 條增為 5 條 |
| 最終步夾帶過多受查項 | TC-003／011／012 | 最終步對齊 `test_item` 之結果，其餘同觸發之結果留在 ER（§5.7）|
| 一般步帶多餘子句 | TC-004／008／014／015／016 | 拆步或去冗 |

> **中途一次自我修正**：曾把最終步改為 `check the X, Y and Z`（只說看哪裡），
> 觸發 G8。canon §5.1 之 preferred verb 是 **`check that …`**（帶預期），
> `check the …` 把判斷推回測試員。已全部改回 `check that`。

### 步驟 4 — **綠**（實際輸出）

```
掃 16 個 leaf 檔 / 16 條 TC
tc_id 範圍 NR1L-UserProfiles-001 … NR1L-UserProfiles-016
design_method 分布：功能測試×8, 基礎故障注入×1, 情境 / 用例×1, 狀態轉換×1, 負向測試×1, 邊界值分析×4
priority 分布：P0×6, P1×6, P2×4

違規 0
```

### 範圍向（R-G9，**含 D-4 明文要求之 12 詞案例**）

```
PASS — G15 注入：一般步 13 詞（上限 12）: 紅
PASS — G15 注入：最終步 19 詞（上限 18）: 紅
PASS — G15 範圍：一般步剛好 12 詞 → 綠
PASS — G15 範圍：最終步剛好 18 詞 → 綠
PASS — G15 範圍：intent 步帶 `to …` 得放寬至 18 詞 → 綠
PASS — G9  範圍：ER 帶 a./b./c. 子層 → 綠（§6.1）
```

> 其中「最終步 19 詞」之注入案例**第一次寫錯**：`Read and check that` 已 4 詞，
> 加 14 個字只有 18，不該紅。**這次是案例錯，不是判準錯** —— 改案例。

---

## 5. D-5、S-1、N-1～N-3

### 5.1 D-5 —— `feature.yaml` 之 popup_ids 改為 21（PDF 側）

`lint.popup_ids` 由 20 改為 **21**，量測條件改標 **`pdf_text`**；
原 20 之清單與其量測條件（xlsx 側 Description 欄）**完整保留於註記**
（R-U11 之形式：其數在其條件下為真，留為歷史記載）。

**並補一道守衛 `G16`**：`feature.yaml` 之定值與現測 `pdf_text` **不得分岔**。
13 輪之狀態正是「兩個數並存而無指引」，而**分岔時無人會發現**。
三個對照向：一致→綠、少一個（回到 13 輪之狀態）→紅、多一個→紅，**皆已證**。

### 5.2 S-1 —— PU id 記法：**兩者皆為 spec 原文，且同出一句**

逐條複位（`pdf_text`，sec 4.1.1）：

```
…PU1087 is displayed when users confirm Setting restore to default by
pressing Yes in pop-up PU_0118. PU1088 is displayed when settings have…
```

**`PU_0118` 與 `PU1087`／`PU1088` 出現在同一段、甚至同一句之內**，
寫法之差異**存在於 spec 本身**，非抽取造成之變體（S-1 所問即此）。

**故不統一** —— 統一即改寫 spec 之字面值（§8.4.1）。
`feature.yaml` 之 `popup_ids` 以正規化形式（`PU` + 4 位）記錄，
與 TC 內之逐字引用**分屬兩個用途**，不互相取代。

### 5.3 N-1 —— `variant_of()` 之否定判讀（**已修**）

```python
NEG_R1H = re.compile(r"\b(?:not|non|except|excluding)\s+(?:an?\s+)?R1\s*High\b", re.I)
# 推定前先剔除否定式，剔除後若仍有 R1 High 才判為 R1 High
```

| | 修正前 | 修正後 |
|---|---|---|
| 語料中判為 R1 High 者 | TC-011、**TC-013**（誤）| **僅 TC-011** |

新增兩個對照案例（反向驗證 7 → **9**）：

- `not an R1 High variant` ＋ 禁用字串 → **不得轉紅**（綠）✓
- 否定與肯定並存（`not an R1 High` ＋ 另一步 `on an R1 High vehicle`）→ **須紅** ✓

### 5.4 N-2 —— `p14`／`p17` 之 PDF 複位，並把「歸宿正確」納入自檢

**複位結果**（`fitz` 讀 PDF 第 N 頁文字層，非以裁定自證）：

| 條目 | PDF 頁上實見 | 判 |
|---|---|---|
| `p14` | `Table EDPR1` 之列項與 `EDPR1`～`EDPR3.2` 錨點 | **→ 9.1 成立** |
| `p17` | Table CPA2 之列項、`**Table CPA2.) Connected Account vs Local Profile` 標題、`CPA1`～`CPA3` 錨點 | **→ 11.4（引用者）＋ 11.5（同頁）** |

自檢第 7 項擴充：對每個 `p<N>` 之每個掛回節次，驗**該節條文確實印在第 N 頁上**。

```
—— 歸宿正確性（PDF 複位，N-2）——
p14 → 9.1：該節條文確實印於 PDF p14 ✓
p17 → 11.4：該節條文確實印於 PDF p17 ✓
p17 → 11.5：該節條文確實印於 PDF p17 ✓
```

**並證其會紅**（新增 `--selfcheck-tamper misplace`：把 `p14` 改掛 `11.5`）：

```
**複位失敗 = ['p14 → 11.5：**PDF p14 上找不到該節條文**']**（須為空）
<8 / 8 self-check items FAIL
```

**這正是 14 包 N-2 所指之洞**：舊版第 7 項對「p14 誤填 9.1」會綠，加了複位才紅。

### 5.5 N-3 —— 取樣清單落為 `data/pilot_sample.tsv`

版控載體已建（16 列，欄位 `req_id／section／test_set／sub_categorization／
priority_prior_037／leaf_title／reason`）。
`build_batch_context.py --selfcheck` 與 `gen_pilot.py` **皆改讀本檔**，
`/tmp/sample.json` 不再是任何程式之輸入。

**並防兩份清單靜靜地不一致**：`gen_pilot.build()` 於生成前比對
TSV 與 `SAMPLE_IDS`，不一致即 `SystemExit` 並列出兩向差集。

---

## 6. 15 包 —— `052f67d` 之處置與 R-G12

### 6.1 條文入庫

`RULINGS.md` 新增「第十五輪條文」段：**R-U55 逐字**（feature 條文）、
**R-G12 逐字**（全域條文，另立小節）。自檢：本包列 2 條，入庫 2 條，**餘數 0**。

### 6.2 `ANOMALIES.md` —— **A-UP10，狀態 ACCEPTED**

新開 `A-UP10 — 052f67d 之 commit 歸屬不準（ACCEPTED，R-U55）`，並於檔頭
之標記說明加入 ACCEPTED 之定義：

> **ACCEPTED**（15 輪起）：狀態**未改變**，是被裁定接受 ——
> 與 RESOLVED 不同，後者指問題已消失。兩者不得互換使用。

條目內明記：**問題未消失**，那個 commit 至今仍寫著 `feat(power)` 而承載
user_profiles 之 8 檔；**是它被裁定接受，不是它被修好**。
「第二次發生」之事實（`645e55f` → `cc04aa1`）已照錄。
末段並記：**本項不因 R-G12 之防線改記 RESOLVED** —— 防線防的是下一次。

### 6.3 R-G12 之跨 feature 通知

寫入 `docs/fw036/FEATURE_ONBOARDING.md` **§9.2 全域條文表**
（標題由「R-G1～R-G9」改為「R-G1～R-G12」；同時補入先前已裁而未升表之
**R-G10／R-G11**），並於表下增一段來源說明。

**未寫入他 feature 之 `RULINGS.md`** —— R-U24／R-U30／R-U44 之界線不變；
他 feature 於下次開輪次時依 R-U44 對 canon §9 自檢即可。

**本輪對 `docs/` 之寫入僅此一處**（canon 為共用文件，非他 feature 之檔）。

---

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **P0 之 tie-break 為本輪自立** | **待覆核** | 「邊界／負向形態，但失效後果為完整性被繞過 → 仍 P0」使 TC-015／016 為 P0，而同為邊界之 TC-003／009 為 P1。**此規則不在 R-U5 明文內**，是我為了讓 16 條一致而立的。若分析層不採，改判成本僅為兩個欄位 |
| 2 | **Table CPA2 之欄別歸屬無法自文字層還原** | **永久限制（除非讀圖）** | ER 只列列名與說明，**不宣稱哪一列屬 Connected 欄或 Local 欄**。若該欄別是可驗內容，須讀該表之版面圖 —— 05 輪已證本 spec 之圖在 PDF 側可抽 |
| 3 | **TC-004 只驗 PLP 表 3.5 一項** | note | 5.9 之條文說的是「**任何** Driver Profile linked preference 都不需按該控制」。取一項為代表，**未驗其全稱**。全稱之驗證需 5 列 PLP 表逐項，屬批次規模問題 |
| 4 | **16 條之 spec 內容正確性仍未逐字複核** | —— | 本輪修的是 14 包點名者；**其餘 ER 之字面是否確為該條 spec 所述，仍是覆核之工作**。lint 到 G16 為止都只驗形狀 |
| 5 | **G15 之詞數以空白切分** | note（判準盲區，R-G11）| `4-digit`、`“Get Started”` 各算一詞；中文步驟會整句算一詞。本批全英文故無影響，**但這個判準不能直接搬給有中文步驟之 feature** |
| 6 | **`p17 → 11.4` 之加掛未回頭檢查其他 `p<N>`** | note | 補句表現有 `p14`／`p17` 兩個 `p<N>`。若日後新增，須同樣問「引用者是誰」而非只問「印在哪頁」 |
| 7 | **`PROF-111` 之 R1 High 反面未生成** | note（依 14 包作業 6）| 已列入第一批正式批次之取樣待辦，本輪不生成 |
| 8 | **A-UP10 為 ACCEPTED，其代價會持續存在** | ACCEPTED | 日後任何人追 03 輪之落點都會撞到它。**這不是可以忘記的事，是選擇承擔的事** |
| 9 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01 | 承前 | 擋 Phase 6 寫回，不擋本批 |

**pilot 覆核之三分類（本輪自陳）**：
14 包判定之 defect 5 已全數處置（D-1～D-5）、style-divergence 1 已具名結論（S-1 不統一）、
note 3 已全數處置（N-1～N-3）。**本輪新增 defect 0、note 6**（上表第 1～6 項）。

---

## 9. 待執行之 git 指令清單 —— **依 R-G12 全部帶 pathspec**（15 包作業 2）

**執行層不執行**（R-G5）。以下為 10–14 輪之累積，合併為一組：

```
# 1) 加入索引 —— 一律帶明確路徑，不用 `git add .` / `-A`（R-G12）
git add features/user_profiles/.gitignore
git add features/user_profiles/BASELINE.sha256
git add features/user_profiles/feature.yaml
git add features/user_profiles/RULINGS.md
git add features/user_profiles/DECISIONS.md
git add features/user_profiles/ANOMALIES.md
git add features/user_profiles/data/outline_map.json
git add features/user_profiles/data/pilot_sample.tsv
git add features/user_profiles/docs/INDEX.md
git add features/user_profiles/docs/handoff
git add features/user_profiles/docs/upstream
git add features/user_profiles/scripts
git add features/user_profiles/generated
git add docs/fw036/FEATURE_ONBOARDING.md

# 2) 提交 —— **一律帶 pathspec**（R-G12）；分兩次，因兩者歸屬不同
git commit -m "<user_profiles 之訊息>" -- features/user_profiles
git commit -m "<canon 之訊息>"          -- docs/fw036/FEATURE_ONBOARDING.md
```

**分兩次之理由**：`docs/fw036/FEATURE_ONBOARDING.md` 是**跨 feature 之 canon**，
不屬 user_profiles。把它併進 `feat(user_profiles)` 的 commit，
**正是 A-UP10 那個病的輕症版本** —— 一個 message 承載不屬於它的東西。

**已入版控者不重列**：10 輪之三行標的與 11–13 輪之產物已分別於
`f653cb0`、`2b3bd4b` 帶 pathspec 提交（後者提交後逐檔驗證無他 feature 混入）。

---

## 10. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_pilot.py`（D-1 priority ×3、D-2、D-3 ×2、D-4 步驟改寫 ×14、N-3 比對）| 否 |
| 2 | 檔案編輯 | `scripts/lint_tcs.py`（**新閘 G15／G16**、G9 判準、9 個新對照案例）| 否 |
| 3 | 檔案編輯 | `scripts/lint_variant_labels.py`（N-1 否定判讀 ＋ 2 案例）| 否 |
| 4 | 檔案編輯 | `scripts/build_batch_context.py`（N-2 多節掛回＋PDF 複位＋`misplace` tamper、N-3 改讀 TSV）| 否 |
| 5 | **檔案編輯** | `feature.yaml`（D-5：popup_ids 20 → 21，原記載保留於註記）| 否 |
| 6 | **檔案新建** | `data/pilot_sample.tsv`（N-3）| 否 |
| 7 | 檔案重生成 ×16 | `generated/SWE1-HMI-PROF-*.json` | 否 |
| 8 | 檔案追加 | `RULINGS.md`（R-U55／R-G12 逐字＋回報）、`ANOMALIES.md`（**A-UP10 ACCEPTED** ＋檔頭定義）| 否 |
| 9 | **檔案編輯（canon）** | `docs/fw036/FEATURE_ONBOARDING.md` §9.2（**R-G12 升格**，並補列先前已裁之 R-G10／R-G11）| 否 |
| 10 | 檔案新建／編輯 | `docs/upstream/14_pilot_fixes.md`（本檔）、`docs/INDEX.md` | 否 |
| 11 | 程式執行 | 生成 ×1、`lint_tcs`（語料＋self-test）、`lint_variant_labels`（反向＋check）、`--selfcheck`（正向＋三向 tamper）| 否 |
| 12 | 唯讀 | `fitz` 讀 spec PDF p14／p17（N-2 複位）；`git` **未執行任何指令** | 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` **皆無**，**連唯讀之 `git status` 亦未跑**
（本輪無查證 git 狀態之需要；13 輪之 §1.4 查證已足）。

**未動**：工作簿（**未寫回**，R-U14）、`inputs/`、`forms/`、`framework.md`、
`data/` 之其餘檔（`outline_map.json`／`xlsx_missing_clauses.tsv` **皆未動** ——
D-3 與 N-2 都是改程式與改 TC，不改素材）、`BASELINE.sha256`、`.gitignore`、
**他 feature 之任何檔**（`docs/fw036/FEATURE_ONBOARDING.md` 為共用 canon，
非他 feature 之檔，且係 15 包作業 3 明文指示）。

---

## 7. 16 條 TC 全文（修正後）

> `test_group` 皆為 `User Profiles`；`test_item` 依 R-U6 等同 `tc_title`；
> `functional_safety` 全批 `NA`；`estimated_test_time` 全批留空；`split_flag` 全批 false。
> **粗體之 priority 為本輪依 R-U5 複核後之值。**


### NR1L-UserProfiles-001 — SWE1-HMI-PROF-001-01（4.1 / Preference Storage）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile-linked preferences stored and recalled per Driver Profile |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The features carrying the preferences under test are available for the vehicle and the region |
| input_test_data | Preferences under test: Cluster Home screen (3.1), SiriusXM 360L Listener Profile (3.2), Nav Saved destinations (3.4) |
| test_procedure | 1. Activate Driver Profile A<br>2. Set the three preferences listed in Input Test Data to values different from their current ones<br>3. Record the values set in step 2<br>4. Activate Driver Profile B, then activate Driver Profile A again<br>5. Read the three preferences and check that they match the values recorded in step 3 |
| expected_result | 1. Driver Profile A is active<br>2. The three preferences accept the new values<br>3. The values set in step 2 are recorded<br>4. Driver Profile A is active again<br>5. The three preferences match the values recorded in step 3 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P0** — 偏好之儲存與回復 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-002 — SWE1-HMI-PROF-002-03（4.1.1 / Preference Storage）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1088 displayed when default restoring is not confirmed |
| pre_conditions | 1. A Driver Profile is active<br>2. The TBM confirmation path can be interrupted on the test bench |
| input_test_data | Fault injected: the completion confirmation from HU or TBM is withheld |
| test_procedure | 1. Open the vehicle settings and select “Restore Settings to Default”<br>2. Press “Yes” in PU_0118 to confirm the restore<br>3. Withhold the completion confirmation from HU and TBM<br>4. Read the popup shown on the head unit and check that PU1088 is displayed |
| expected_result | 1. PU_0118 is displayed<br>2. PU1087 is displayed<br>3. The head unit does not receive the completion confirmation<br>4. PU1088 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1.1 |
| priority | **P0** — 回復原廠之分支 —— 資料遺失風險項（R-U5／canon §10.2）；037 先驗 Low 不覆蓋 rubric |
| design_method | 基礎故障注入 (Fault Injection Lite) |
| remarks | PU1087／PU1088 之 popup 內文未載於 spec（DR #4）—— 本 TC 僅驗其是否顯示，不寫內文（R-U15／R-U27） |

### NR1L-UserProfiles-003 — SWE1-HMI-PROF-021-01（5.2 / Profile List）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Add New Profile removed at the five-Profile maximum |
| pre_conditions | 1. Four Driver Profiles exist on the vehicle<br>2. A Valet Mode Profile is present on the vehicle<br>3. The vehicle does not have a 7-inch screen |
| input_test_data | Driver Profile count: 4 (below the maximum) → 5 (at the maximum) |
| test_procedure | 1. Open the Profile List and read the Add New Profile button<br>2. Create one more Driver Profile so that five Driver Profiles exist<br>3. Open the Profile List and check that the Add New Profile button is not present |
| expected_result | 1. The Add New Profile button is present while four Driver Profiles exist<br>2. The fifth Driver Profile is created<br>3. The Add New Profile button is not present; the icon and the string “This icon is associated to settings that are specific to your profile and are not shared across the vehicle” are not present; and “Max Profiles reached. Delete to create a new one.” (PU0584) is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.1.2 |
| priority | **P1** — profile 建立之上限邊界 —— R-U5 定邊界為 P1 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | （空） |

### NR1L-UserProfiles-004 — SWE1-HMI-PROF-032（5.9 / Profile List）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Preferences saved without pressing memory seat controls |
| pre_conditions | 1. A Driver Profile is active<br>2. The vehicle is equipped with memory seat hard and soft controls |
| input_test_data | Preference under test: Memory Profiles (Seats, mirrors, steering wheel) (3.5) |
| test_procedure | 1. Activate Driver Profile A<br>2. Adjust the seat, mirror and steering wheel positions<br>3. Leave the memory seat set and save controls untouched<br>4. Switch the ignition off and on<br>5. Read the three positions and check that they match step 2 |
| expected_result | 1. Driver Profile A is active<br>2. The seat, mirror and steering wheel positions are adjusted<br>3. No memory seat set or save control is pressed<br>4. The vehicle completes the ignition cycle<br>5. The three positions match those set in step 2 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.9<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | **P0** — 偏好之自動儲存 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-005 — SWE1-HMI-PROF-048（6.2.1 / Defaults）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Profiles remain after a new Profile is created |
| pre_conditions | 1. The vehicle carries its default Profiles, including Driver 1<br>2. No default Profile has been customized or deleted |
| input_test_data | NA |
| test_procedure | 1. Open the Profile List and record the default Profiles present<br>2. Create a new Driver Profile without customizing any default Profile<br>3. Open the Profile List and check that the default Profiles recorded in step 1 are still present |
| expected_result | 1. The default Profiles, including Driver 1, are recorded<br>2. The new Driver Profile is created and no default Profile is customized<br>3. The default Profiles recorded in step 1 are still present |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.2.1 |
| priority | **P1** — 建立新 profile 之次要性質（預設 profile 之存續）—— 主要功能之次要操作 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-006 — SWE1-HMI-PROF-053（6.4.1 / Defaults）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0585 shown on Get Started without vehicle connectivity |
| pre_conditions | 1. The vehicle is not equipped with connectivity |
| input_test_data | NA |
| test_procedure | 1. Open the Profile setup screen carrying the “Get Started” button<br>2. Press “Get Started” and check that PU0585 is displayed and the Connected Account Login/Register screen is not displayed |
| expected_result | 1. The “Get Started” button is displayed<br>2. PU0585 is displayed and the Connected Account Login/Register screen is not displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.4.1 |
| priority | **P1** — setup flow 之非主路徑分支（無連網配置） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-007 — SWE1-HMI-PROF-059-01（7.2.1 / Welcome Flow）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Large welcome popup lists active and other Profiles |
| pre_conditions | 1. Two Driver Profiles exist, each with a username, an avatar and a memory seat assignment<br>2. Driver Profile A is the active Profile |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A so that the large welcome popup is displayed<br>2. Read the popup and check that the active and the other Profiles are listed |
| expected_result | 1. The large welcome popup is displayed<br>2. Driver Profile A’s username and avatar are displayed, and the other available Profile is displayed with its avatar, username and memory seat assignment |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2.1 |
| priority | **P2** — welcome popup 之內容展示 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-008 — SWE1-HMI-PROF-062-02（7.4 / Welcome Flow）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup clears 30 seconds after display |
| pre_conditions | 1. The vehicle is stationary<br>2. A Driver Profile carrying a Welcome Popup is available |
| input_test_data | Elapsed time readings: 29 s, 30 s |
| test_procedure | 1. Activate the Profile and start a timer<br>2. Read the screen at 29 seconds without touching it<br>3. Read the screen at 30 seconds and check that the Welcome Popup is cleared |
| expected_result | 1. The Welcome Popup is displayed and the timer is started<br>2. The Welcome Popup is still displayed at 29 seconds<br>3. The Welcome Popup is cleared at 30 seconds |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4 |
| priority | **P2** — welcome popup 之逾時清除；輔助行為之邊界 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | （空） |

### NR1L-UserProfiles-009 — SWE1-HMI-PROF-073-01（8.7 / Setup Flow）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Keyboard blocks input beyond 12 username characters |
| pre_conditions | 1. The Profile setup flow is open at Step 2 “Enter a username” |
| input_test_data | Username input: 11 characters → 12 characters → one further character |
| test_procedure | 1. Type 11 characters into the username field and read the field<br>2. Type the 12th character and read the field<br>3. Type one further character and check that the username field still shows 12 characters |
| expected_result | 1. The username field shows the 11 characters typed<br>2. The username field shows 12 characters<br>3. The username field still shows 12 characters and the further character is not accepted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7 |
| priority | **P1** — username 長度上限邊界 —— R-U5 定邊界為 P1 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | spec 8.7 寫 “~12 characters”（約），037 leaf 寫 12 —— 本 TC 取 12（較窄之解讀，且 037 為單位權威） |

### NR1L-UserProfiles-010 — SWE1-HMI-PROF-070（8.4.1 / Setup Flow）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile saved after username and avatar are entered |
| pre_conditions | 1. The Profile setup flow is open at the username step |
| input_test_data | NA |
| test_procedure | 1. Enter a username in the Profile setup flow<br>2. Choose an avatar<br>3. Switch the ignition off and on<br>4. Open the Profile List<br>5. Read the list and check that the Profile from steps 1 and 2 is listed |
| expected_result | 1. The username is accepted<br>2. The avatar is selected<br>3. The vehicle completes the ignition cycle<br>4. The Profile List is displayed<br>5. The Profile carrying the username and avatar from steps 1 and 2 is listed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.4.1 |
| priority | **P0** — profile 建立之儲存 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

### NR1L-UserProfiles-011 — SWE1-HMI-PROF-091-01（9.3.2 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Restricted Profile action interrupted when vehicle starts moving |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and start editing the Profile username<br>2. Bring the vehicle into motion<br>3. Read the screen and check that the previous available page is displayed |
| expected_result | 1. The username editing page is displayed<br>2. The vehicle is in motion<br>3. The previous available page is displayed, the bonk tone is played, and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1 |
| priority | **P1** — 行車限制之中斷分支；037 先驗 High |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | R1 High 之 label 為 Connected Account —— spec 9.3.2 之變體覆寫（PDF p14，xlsx 側掉句），R-U35 (c)／§8.7.3 |

### NR1L-UserProfiles-012 — SWE1-HMI-PROF-104（9.8 / Editing）

| 欄 | 值 |
|---|---|
| tc_title / test_item | More Settings opens My Profile without a back button |
| pre_conditions | 1. A Driver Profile is active<br>2. The Profile section is reachable from the vehicle menu |
| input_test_data | NA |
| test_procedure | 1. Open the Profile section and press the vehicle “More Settings” button<br>2. Read the page and check that the “My Profile” Settings section is displayed |
| expected_result | 1. The “My Profile” Settings section is displayed<br>2. No back button to the Profile section is present on the “My Profile” Settings section |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.8 |
| priority | **P2** — 設定入口之導向；輔助功能 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 9.8 之 PU0609 句（設定變更時提示已對現用 profile 變更）在 037 無對應 leaf —— 未納入本 TC，已列上繳 13 之覆蓋缺口 |

### NR1L-UserProfiles-013 — SWE1-HMI-PROF-111（11.4 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Info icon opens the Local vs Connected Profile screen |
| pre_conditions | 1. The vehicle is not an R1 High variant<br>2. The vehicle is not a China-market vehicle<br>3. A Driver Profile is active and the Edit Profile tab is available |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and read the Connected Account item<br>2. Select the info icon and check that the Local vs Connected Profile screen is displayed |
| expected_result | 1. An info icon is displayed next to Connected Account<br>2. The screen titled “What are the benefits of creating an Connected account?” is displayed with two columns labeled Connected account and Local Profile, showing “Synchronize your profile between multiple vehicles. The cloud will remember your preferences” and “Create a profile specific to this vehicle. The vehicle will remember your preferences”, and the rows of Table CPA2:<br>   a. Personalization — Presets, Menu Bar Order, App Drawer Favorites, and more<br>   b. App Store Download<br>   c. Marketplace — Access to Marketplace<br>   d. Connected Navigation — Personalized Favorites, Recents, and Predictive Navigation<br>   e. Connected Profile App (See Connected Personal Account HMI) |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.4<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.5 |
| priority | **P2** — 說明頁之內容展示；037 先驗 Low |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 標題之 “an Connected account” 為 spec 原文（含冠詞誤用），逐字照錄不修（§8.4.1） |

### NR1L-UserProfiles-014 — SWE1-HMI-PROF-112-01（11.5 / Connected Account）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Deleted App Store app removed only for the uninstalling user |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle, each with its own Connected Account<br>2. The same App Store app is installed locally for both Profiles |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A<br>2. Record the App Store app shown in the app tray<br>3. Delete the App Store app from Driver Profile A<br>4. Activate Driver Profile B<br>5. Open the app tray and check that the app recorded in step 2 is still present |
| expected_result | 1. Driver Profile A is active<br>2. The App Store app is recorded in Driver Profile A’s app tray<br>3. The App Store app is removed from Driver Profile A’s app tray<br>4. Driver Profile B is active<br>5. The App Store app is still present in Driver Profile B’s app tray |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.5 |
| priority | **P1** — app 刪除之範圍；037 先驗 High |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| remarks | （空） |

### NR1L-UserProfiles-015 — SWE1-HMI-PROF-128-01（12.9 / Valet Mode）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode deactivation cancelled on the tenth incorrect PIN |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. No PIN lockout is in effect |
| input_test_data | PIN attempts: 9 incorrect attempts → 10th incorrect attempt |
| test_procedure | 1. Open the Valet Mode deactivation screen<br>2. Enter an incorrect 4-digit PIN nine times<br>3. Read the deactivation screen after the ninth attempt<br>4. Enter an incorrect 4-digit PIN a tenth time and check that the deactivation is cancelled |
| expected_result | 1. The Valet Mode deactivation screen is displayed<br>2. Each of the nine incorrect PIN entries is rejected<br>3. The deactivation screen still accepts a further PIN entry<br>4. The deactivation is cancelled on the tenth incorrect attempt and a further PIN entry is not accepted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | **P0** — Valet Mode 進出 —— R-U5 核心五類之一 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | 條文之「30 分鐘後可再試」需 30 分鐘等待，本 TC 只驗第 10 次即取消且當下不再受理，未驗 30 分鐘後之解鎖 |

### NR1L-UserProfiles-016 — SWE1-HMI-PROF-132-02（13.2 / Valet Mode）

| 欄 | 值 |
|---|---|
| tc_title / test_item | SPAAK user blocked from exiting Valet Mode on the head unit |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user and not the vehicle owner<br>3. The owner has an authorized app or website session available |
| input_test_data | NA |
| test_procedure | 1. Open the head unit screens that offer a Valet Mode exit and attempt to exit Valet Mode<br>2. Read the screen and check that the exit is blocked<br>3. Deactivate Valet Mode remotely as the owner<br>4. Read the head unit and check that Valet Mode is no longer active |
| expected_result | 1. Any screen or popup that would allow a Valet Mode exit is blocked (PU0934)<br>2. Valet Mode is still active after the SPAAK user’s attempt<br>3. The owner’s remote deactivation is accepted<br>4. Valet Mode is no longer active on the head unit |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.2 |
| priority | **P0** — Valet Mode 進出 —— R-U5 核心五類之一 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

