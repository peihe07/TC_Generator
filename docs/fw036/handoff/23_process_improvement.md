# 23 — 流程改善總綱 v2（P1–P7 條文化與工單）

日期：2026-08-24
層級：全域（docs/fw036），非單一 feature
取代：`22_process_improvement.md`（NN 22 與既有上繳包
`upstream/22_canon_sync_and_lint_profile.md`（2026-08-21，無下放對應）碰撞，
依「一次往返共用同一 NN」改編為 23；22 原檔保留並標 SUPERSEDED，不刪）

**裁定記錄**：Pei 2026-08-24 chat「是都修 然後其他的也看一下 整理流程
我覺得往返太多,然後規則不遵守的也很多」——
(1) P1–P7 方向與 §D 條文 R-G13~R-G21 視為追認；
(2) W-P1 第 7 步（Pei 過目 canon diff 後 commit）為第二道確認點，
措辭異議仍可於該點提出，屆時修訂以 diff 覆核為準。

**痛點對映**（Pei 具名之兩項）：
- 往返太多 → R-G13（引用制砍抄寫）、R-G14（綠色通道）、R-G16（預期數字自動化）
- 規則不遵守 → R-G17（閘登錄與除役）、R-G18（引用唯一可解析）、
  R-G19（prompt 指紋）、R-G20（規則副本同步）、R-G21（自查表機檢對映）

> §8.9 說明：本包新條文超過 3 條，係因方向已於 chat 一次裁定，
> 本包僅為已裁方向之條文化，追認一次過，不逐條往返。

---

## A. 禁區

- 全部 git 操作屬 Pei（R-G5）；執行層只準備 patch / 新檔，不 commit、不 restore
- 不得改動任何 feature 之已交付件與 done region
- 不得刪檔；取代者以 `[SUPERSEDED by …]` 標註或 `mv` 歸檔（R-G2）
- canon 修訂以「準備修訂版全文 + diff 摘要」交 Pei 過目後由 Pei commit
- xlsx 一律不碰（本案無 workbook 作業）
- **不得為使既有失敗測試轉綠而改動 `features/user_profiles/` 與 `_intake`**
  （該 8 項失敗為既有且與本案無關，處置見 §I-1）

## B. 背景

診斷（2026-08-24，chat，證據為當日實測）：

1. 往返失控 — vehicle_setting handoff 實測 90（Part 1）+ 29（VF230）份；
   一批一上繳使 Pei 成為每批同步點
2. 裁決逐字照錄成本隨條文數線性膨脹（§8.1），抄寫本身成為漂移源
3. canon 現有兩個 `## 9.` 章節，R-G1~G12 出現兩次且摘要有出入 —
   「canon §9.1」現為歧義引用
4. 規則面積單調成長，G-A 除役機制無實際運作記錄
5. pilot 無數字化退出準則（vehicle_setting 至少 6 次 pilot 事件）
6. 第二層檢驗（預期數字）為手工，A-PJ51 型事故之直接發生條件
7. （Pei 補充）TC 撰寫規則越來越容易偏離 — 規則散於
   canon / profile / RULINGS / Project 指令副本，且 prompt 與 exemplar
   之變更無指紋可稽
8. **規則副本不同步之活例（2026-08-24 實測）**：repo canon
   `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 已於 2026-08-21
   （上繳 22 §一）將 §8.7.5 改寫為 R-1 v3；Project 指令副本無 §8.7.5，
   其所載 sha `fa9833ae64c9092f` 為改寫前之值 — 此即 R-G20 要攔之形態，
   且為其首個執行對象（見 §I-2）

## C. 被修訂之既有條文（逐字照錄，現行 canon 文字）

C-1（§8.1，被 R-G13 取代之部分）：
> 裁決逐字 | 適用之裁決全文照錄，**不得摘要、不得以編號代替** | 執行層依編號猜內容

C-2（§8.8，被 R-G14 加註）：
> **一批一上繳**，前批未覆核不得開下批

C-3（§1.2 現行無數字化退出準則；R-G15 為新增，不取代既有文字）

C-4（G-A，併入 R-G17 管理）：
> 同一條待判連續三輪判為「不成立」者，須改判準或除役

## D. 新條文（已追認；由 W-P1 併入 canon）

> 編號自 R-G13 起。canon 現行最末為 R-G12（兩個 §9 皆同）；
> W-P1 執行時須先驗 RULINGS_LEDGER 與全 repo 無 R-G13+ 既用，
> 有碰撞即停並回報（§F 升級條件 1）。

### R-G13 — 裁決引用制（取代 §8.1「裁決逐字照錄」）

```
R-G13：裁決條文集中於各 feature 之 RULINGS.md 與 canon §9，每條具穩定
錨點（`### R-XX <slug>`）。`scripts/rulings_hash.py` 產生
`RULINGS.sha.tsv`（ruling_id → 條文本體 sha256），該 tsv 入版控。
下放包引用格式為 `R-XX@<sha8>`；執行層自 repo 讀取條文原文，
上繳包逐條回報所讀 sha8。sha 不符 = 停下回報，不自行調和（§8.4）。
未落檔之條文不得引用（§8.5-1 不變）。逐字照錄自本條生效起不再要求，
但下放包得於必要時仍附原文（附了不算錯）。
```

### R-G14 — 綠色通道（§8.8 之例外）

```
R-G14：post-pilot Phase 6 批次，連續 3 批同時滿足
（lint 全綠、預期數字全符、全簿基線重現、獨立判斷無新發現）者，
自第 4 批起執行層自動續批，每 5 批彙總一份上繳；Pei 抽樣覆核
（每彙總至少 1 批全查 + 其餘批各抽 1 parent）。三分法、掃描條件揭露、
獨立判斷每批照附於彙總。任一批任一條件不符即退出通道，回到一批一上繳，
重新累計。§8.8「一批一上繳」加註「除 R-G14 生效期間」。
```

### R-G15 — Pilot 退出準則（新增於 canon §1.2）

```
R-G15：pilot 判定以 done-region check 後之分類計：
- PASS：defect = 0 且 style-divergence ≤ 2（note 不計）
- PASS-with-corrections：defect ≤ 2 且皆為局部修正（非 corpus-wide
  規則錯誤），修正清單隨批落地
- REGENERATE：任一 defect 屬規則層（影響全 corpus 之 prompt / lint /
  profile 規則錯誤）
同一 pilot 重跑上限 2 次；第 3 次觸發 Tier 2 檢討，檢討對象為規則與
prompt 本身而非語料。
```

### R-G16 — 預期數字自動生成

```
R-G16：下放包之預期數字表由 `scripts/expected_numbers.py` 自
feature.yaml + 批次清單 + lint_defs 推導產生；分析層覆核後簽入包內。
手算僅限工具未覆蓋之新指標，逐項標 `[MANUAL]`。工具產出與上繳實測
不符時，工具與語料兩側皆查（§5a-16），不得預設任一側為準。
```

### R-G17 — 閘登錄簿與除役

```
R-G17：`docs/runtime/GATES.tsv` 登錄每支 lint 閘：id、判準一句話、
來源裁決、生效日、近 10 輪命中數。上繳包附本批各閘命中統計。
連續 10 輪命中 0 之閘自動列入除役候選；Pei 於該 feature close-out
一次裁定。除役 = 移入 GATES.tsv `retired` 區段並於 lint_defs 停用，
不刪紀錄。G-A（三輪待判除役）併入本條管理，原文標
[SUPERSEDED by R-G17 — 管理機制部分]。
```

### R-G18 — canon 引用唯一可解析

```
R-G18：canon 之章節引用（「canon §X」「§5a 第 N 條」「R-Gn」）須全域
唯一可解析。`scripts/canon_refs.py` 掃描全 repo 引用並驗證每一引用
唯一命中；unresolved 或 ambiguous > 0 即 FAIL。本閘為每 feature
close-out 必跑項。
```

### R-G19 — prompt 指紋（TC 規則抗漂移之一）

```
R-G19：每批之批次 manifest 記錄本批實際使用之 prompt 模板 sha256 與
exemplar 集 sha256；上繳包照抄。與前批不符而下放包未宣告變更者，
該批退回。prompt 模板與 exemplar 集之任何變更為 Tier 2。
```

### R-G20 — 規則副本同步指紋（TC 規則抗漂移之二）

```
R-G20：每次 pilot review 與 feature close-out，執行層回報
`docs/runtime/ASPICE_SWE6_AI_Instruction.md` 現行 sha256；分析層與
Project 指令副本所載 sha 比對。不符 = 先 re-sync Project 副本再進行
審查；審查不得在已知不同步之規則副本上進行。
```

### R-G21 — 自查表機檢對映（TC 規則抗漂移之三）

```
R-G21：§9 自查表逐項標註其保證來源：有對應 lint 閘者記閘 id
（入 GATES.tsv），無者標「人工項」。pilot review 逐 TC 勾檢人工項。
使「機器保證」與「人力承擔」在紙上分得開（G-D、G-E 之精神）；
人工項清單之增減為 Tier 2。
```

---

## E. 工單（依序執行；一批一上繳照舊 — 綠色通道尚未生效）

### W-P1 — 裁決基礎設施 + canon 整併（先行，其餘皆引用之）

1. 驗證 R-G13~R-G21 編號無碰撞（掃全 repo `R-G1[3-9]|R-G2[01]`，
   詞界、區分大小寫）
2. canon 整併：合併兩個 `## 9.` 為一；R-G1~G12 單一落點，一句話摘要
   以較完整之一版為準並逐條與兩版原文比對，出入處列表回報；
   全文加逐條錨點；被移動之內容不刪，於原位標 [MOVED]
3. R-G13~R-G21 併入 canon §9
4. RULINGS.md 結構化（先做 canon §9 與 vehicle_setting、display 兩個
   活躍 feature；已 close-out 之 feature 延後）＋ `rulings_hash.py`
   ＋ `RULINGS.sha.tsv`
5. `canon_refs.py` 引用解析器，首跑輸出 unresolved / ambiguous 全清單
6. §8.1、§8.8、§1.2 修訂文字併入（見 §C / §D）
7. Pei 過目 diff → Pei commit（pathspec 明列，R-G12）

預期數字（量測條件：對 `docs/fw036/FEATURE_ONBOARDING.md` 現行檔，
逐行掃描，區分大小寫）：
- `## 9.` 標題數：現 2 → 整併後 1
- `R-G1` 表格落點數：現 2 → 1
- canon_refs 首跑 unresolved 數：未知 — 首跑即基線，回報實測值，
  不預設目標（§5a-11：本項於首跑不可能 PASS/FAIL，只能建基線）

### W-P2 — expected_numbers.py + GATES.tsv + 二項既有缺陷

1. `expected_numbers.py`：以 vehicle_setting 最近一批之下放包手算值為
   已知全集驗證（§5a-12）：工具重算須逐項與該包相符，不符處逐項追因
2. `GATES.tsv`：自 lint_defs 生成閘清單；近輪命中數可自既有上繳包回填者
   回填，不可者標「未知，自本輪起算」— 不得以 0 代替未知（G-D）
3. **`--gate` 接入**（上繳 22 §三-5）：`lint_docs036.py` 現為 PASS，
   為接入之最佳時點（S3 之啟用）；接入點與觸發時機於上繳包提案，
   接入本身為 Tier 2，**準備而不啟用**，Pei 裁定後生效
4. **`report_stem()` 同 tag 覆寫**（上繳 22 §三既有項）：兩本不同
   feature 產生同一 tag（`20260817_ext`）致報告互相覆寫。修法：tag
   併入 feature 名；以該兩本已知碰撞檔實測「修正後不再覆寫、
   其餘檔案之報告檔名不變」（G-N：以字面案例釘入測試）

### W-P3 — prompt 指紋 + 自查表對映

1. `make_batch_context.py` 輸出 prompt/exemplar sha 入批次 manifest
2. §9 自查 17 項逐項對映閘 id 或標人工項，產出對映表入 GATES.tsv
3. 對映表之驗證：對已知案例（Home A-H10 之引號規則）確認其對映之閘
   確實會轉紅（G-K）

## F. 升級條件（停下回 chat）

1. R-G 編號碰撞
2. canon 兩版 §9 內容有無法調和之實質矛盾（非摘要措辭差異）
3. canon_refs 首跑發現引用指向已不存在之條文
4. RULINGS.md 結構化遇到單條無法逐條切分者（一條包數事，通則 11）
5. expected_numbers 重算與既有手算包不符且追因後指向手算包錯誤
   （= 既有記錄須更正，Tier 2）
6. 任何工作觸及 `features/user_profiles/` 或 `_intake`（§A 禁區）

## G. 上繳要求

每工單一份上繳包（`docs/fw036/upstream/23a_wp1.md` / `23b_wp2.md` /
`23c_wp3.md`）：預期數字對照（相符者亦列）、不符項目不自行調和、
canon diff 摘要、canon_refs / rulings_hash 實跑輸出、掃描條件揭露、
獨立判斷（本包是否仍有該驗而未驗者）、本包引用之既有裁決編號清單。

## H. 本包產生之新條文清單（自檢表）

- [x] R-G13 裁決引用制 — 區塊已列
- [x] R-G14 綠色通道 — 區塊已列
- [x] R-G15 pilot 退出準則 — 區塊已列
- [x] R-G16 預期數字自動生成 — 區塊已列
- [x] R-G17 閘登錄簿與除役 — 區塊已列
- [x] R-G18 canon 引用唯一可解析 — 區塊已列
- [x] R-G19 prompt 指紋 — 區塊已列
- [x] R-G20 規則副本同步指紋 — 區塊已列
- [x] R-G21 自查表機檢對映 — 區塊已列

本包引用之既有裁決 / 條文：§8.1、§8.8、§8.9、§1.2、§5a-11/12/16、
G-A、G-D、G-E、G-K、G-N、R-G2、R-G5、R-G12、S3、通則 11、A-PJ51、
上繳 22 §一 / §三。

## I. 開放事項（Pei 另裁，不阻塞本案）

1. **user_profiles 8 項既有測試失敗**（`test_single_write_path.py` +
   `test_intake_scaffold.py`，上繳 22 §三登記；含 `features/user_profiles/`
   內 openpyxl save 呼叫點三處 — R-G3 風險形態）。待 Pei 指示：
   立案修復，或標 ACCEPTED 記入 ANOMALIES
2. **Project 指令副本 re-sync**（R-G20 首例）：W-P1 canon 整併 commit 後，
   Pei 重貼 Project 指令之 §-rules 區段並更新所載 sha。現行副本已確認
   落後（§B-8），在此之前 pilot review 不得僅憑 Project 副本judge訊號寫法
3. **R-G14 綠色通道生效起點**：建議 vehicle_setting 產線批次
   （batch 21 起）即適用，pilot #4 verdict 後起算連續綠批
