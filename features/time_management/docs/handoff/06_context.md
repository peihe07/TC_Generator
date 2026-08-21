# 下放包 06 — 三項更正、context 層編碼、R-TM49 判準

分析層 → 執行層。往返編號 `06`。對應上繳 `docs/upstream/06_context.md`。
`05Z` 受理，`05` 往返結案。

**§1 之自我更正是本輪最有價值的一項**，且其後果落在我的條文上（G-TM1）。

---

## 1. `build_batch_context.py` 亦被覆蓋 —— 受理，且 G-TM1 須更正

三方 SHA256 比對（快照 = git HEAD = `7344b995d0b4faf2`，工作樹僅差來源標記
2 行）**證據充分**。`SPEC_GAP` 與 `BOUNDARIES` 兩表從未存在於任何已保存
之版本。

### 1.1 自我定性正確，且我要補一層

> 我在 `03Z-A1` 上繳如此描述自己在 01 包之失誤，然後在 `04` 輪犯了同一個。
> 差別在於這次它被我引用了三輪，成為後續判斷之基礎。

**「判定後未複查」與「寫入後未複查」是同一件事的兩個位置**，而前者更難
察覺：寫入有產出物可比對，判定只留下一句話。

**分析層之責任**：該陳述我在 `04Z` §4 寫入 G-TM1 之條文本體
（「現存之 `build_batch_context.py`（執行層版）已含 `SPEC_GAP` 與
`BOUNDARIES` 兩表，故 3、4 在 context 層有編碼，僅 lint 層缺」），
**我未要求任何佐證即據以立條**。上繳之陳述受查證義務拘束（`00Z` §2 已立），
而我對它免除了那道義務。

```
G-TM1 更正（2026-08-21，依 05Z 上繳 §1）

原條文末段：「現存之 build_batch_context.py（執行層版）已含 SPEC_GAP 與
BOUNDARIES 兩表，故 3、4 在 context 層有編碼，僅 lint 層缺。」

**經 SHA256 三方比對（快照 09:15:18 = git HEAD = 7344b995d0b4faf2）
證實為偽** —— 該兩表從未存在於任何已保存版本，三支腳本皆非本 session
之產出。

**訂正**：context 層目前**無任何** A-TM13 缺口編碼與界線編碼。
G-TM1 項 3、4 現僅有 lint 層（B3 / B4）之事後攔截，無生成時之指示。

原條文之「context 層之編碼不能取代 lint 層 —— 前者是給生成看的，
後者是驗生成的」一句**不變且更形重要**，因其反向亦成立：
**lint 層不能取代 context 層。** 現況正是只有事後攔截而無事前指示，
其後果為模型必然生成錯誤內容再被攔下，而非一開始就被導向正確內容。

補回屬 `06` 之範圍（本包 §3）。
```

### 1.2 A-TM20 之記載更正

```
A-TM20 記載更正（2026-08-21，依 05Z 上繳 §1.2）

原記「write_back.py、lint_tcs.py 為另一 session 覆蓋所得；
build_batch_context.py 為本 session 執行層產出」。

**經 SHA256 三方比對證實為偽**：三支腳本**全部**為另一 session 之產出，
本 session 執行層原產出之三份皆已失落，無備份。

`data/scripts_snapshot_20260821/` 保全的是**覆蓋後**之狀態，非本 session
之產出。其 README 之混合來源說明須隨之更正（本包 T2）。

A-TM20 之 RESOLVED 狀態不變（歸屬已由 R-TM44 裁定）；更正者為其事實記載。
```

### 1.3 未受影響者 —— 執行層之判定正確

階段 A / B 之修改基於實讀全文，A-TM21 六項基於 `04R` T4 之唯讀全文評估
—— **三者皆讀現存版本身，與歸屬判定無關**。此區辨正確，
不需重做任何已完成之修法。

## 2. §6.4 依據 1 —— **我引的是執行層看不到的東西**

執行層記 R-TM48 依據 1（charter 明訂 repo 版為權威）「可驗而未驗」。

**實情是它不可驗** —— 該句出自 **Project 層之 Operating Charter**，
即分析層之系統指令，**執行層無法讀取**。我引它時未意識到這一點。

其逐字內容為：

> The §-rules below are a periodic copy of
> `docs/runtime/ASPICE_SWE6_AI_Instruction.md`; the repo version is
> authoritative and evolves there. Re-sync at each feature close-out.

```
R-TM50（分析層自裁，2026-08-21）—— 引用 Project 層 charter 須逐字引入

分析層以 Project 層 Operating Charter（分析層之系統指令）為裁決依據時，
須將所引之句**逐字寫入下放包**，不得僅稱「charter 明訂……」。

理由：執行層無法讀取 Project 層指令，故該類引用對其為**結構性不可複驗**。
不逐字引入，等於要求對造接受一個它原則上無法查證之前提 ——
與 R-TM4（斷言須附完整元素清單）之精神相同，只是不可驗之成因是
權限而非省略。

執行層對該類引用之正確標示為「**結構性不可複驗**」，非「可驗而未驗」。

依據：05Z 上繳 §6.4 將 R-TM48 依據 1 標為「可驗而未驗（未讀 charter
原文）」，而該原文不在 repo 內。
```

**R-TM48 之三項依據現況**：依據 1 逐字引入（見上），依據 2 仍為結構性
不可複驗（聊天層歷史），依據 3 已由執行層獨立驗證。
**依據 1 與 3 成立即足以支撐 R-TM48。**

## 3. R-TM49 例外條款之判準 —— 本包補

執行層記「『確認其為該訊號之網段而非上下文提及者』之可操作判準未定」。
**提請成立。**

```
R-TM51（分析層裁定，2026-08-21）—— R-TM49 例外之可操作判準

CAN 訊號斷言之 segment 得直接填寫，當且僅當下列兩項同時成立：

(a) **同物件**：該網段之敘述與該訊號名出現於**同一個 CFTS015 物件**
    （同一個 7 位 id 之內文），非鄰近物件、非同章節之他物件。
(b) **同述語**：該敘述之句法上，網段為該訊號（或其所屬 MESSAGE）之
    修飾語，非另一句之主題。

  ✓ 物件 4814098：`use a GPS.data internal signal to set a BH-CAN
    message with correct UTC time and date.` 其後列 $GPSDateTm*$ 六訊號
    —— 同物件、且 BH-CAN 修飾該 message，該六訊號得填 `BH-CAN`
  ✗ 某物件提及 `C-CAN` 而訊號列於另一物件 —— 不得跨物件引用

兩項有一不成立即標 `PENDING: DR-6`。

**填寫時須於 reasoning 註明來源物件 id**，使該判定可被覆核
（否則「有來源」與「杜撰」在成品上無法區分）。

不得以「CFTS015 全文出現過該網段名」為依據 —— 那是詞彙存在，
非該訊號之網段。
```

## 4. context 層編碼 —— 本包主要工作

`build_batch_context.py` 現無 A-TM13 缺口與界線之編碼。**補回不是還原**
（原版已失落且結構不同），是依現行條文重新設計。

### 4.1 須進入 context 之項（六類）

| # | 內容 | 依據 |
|---|---|---|
| C-1 | **五條 §8.2.1 界線**，每條含 owns / not_ours 之訊號名與物件 id | R-TM17 + R-TM25 |
| C-2 | **A-TM13 兩片之缺口指示**：005 / 002 之受影響條目須寫 `PENDING: DR-5`，不得留空、不得填偽值 | R-TM41 訂正 + canon §8.4.3 |
| C-3 | **spec_reference 之候選清單**（v2 格式，前綴僅一次、升冪、無 `;`），逐 leaf | R-TM40 + canon §10.7(a) |
| C-4 | **test_item 兩段式**：上半 verbatim ≤ 50 token 取自 `leaf_descriptions.txt`，下半 `(...)` 測試目的 | canon §4.3.1 + R-TM24 |
| C-5 | **訊號三件組**：Signal / MESSAGE 取自 CFTS015；segment 依 R-TM51 判定，不合即 `PENDING: DR-6` | canon §8.7.5 + R-TM49 + R-TM51 |
| C-6 | **Test Set 值**：該 leaf 所屬之七組之一 | R-TM17 / Part VII |

**不進入 context 者**：`tc_id`（canon §10.3 明訂 generator 賦號，
LLM 不得 emit）、`functional_safety`（A-TM24 未決，且由條文定）、
`priority` 分佈（`TODO(內容裁決)`）。

### 4.2 設計要求

- **C-1 與 C-2 之內容須與 lint 層之 `BOUNDARY_SIGNALS`、`lint_spec_gap`
  取自同一來源**，不得各寫一份 —— 兩份會漂移，且漂移時 lint 全綠
  （context 說 A、lint 驗 B，生成照 A 寫則被 B 攔，看起來像模型出錯）。
  **建議抽為共用模組或共用資料檔，實作方式由執行層定，但須回報其
  單一來源之所在。**
- 檔頭來源標記（R-TM33）
- **self-test**：至少證明六類各自出現於產出之 context 中
  （紅向：抽掉某一類之來源資料，context 產生器應報錯而非靜默略過）

---

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM50 / R-TM51，更正 G-TM1

標題行 `## R-TM50 — 引用 Project 層 charter 須逐字引入`、
`## R-TM51 — R-TM49 例外之可操作判準`，內文為 §2 / §3 之區塊全文。

**G-TM1 之末段依 §1.1 之區塊更正** —— 原文加刪除線保留（R-TM13），
訂正文置於其下。

**增量（R-TM46）**：`## R-TM` **+2**；`## G-TM` **0**；`## A-TM` **0**。

### T2 — `ANOMALIES.md` 與快照 README 之記載更正

A-TM20 條末追加 §1.2 之區塊全文（狀態仍 RESOLVED，更正者為事實記載）。

`data/scripts_snapshot_20260821/README.md` 之混合來源段，
**原文加刪除線保留**，其下加：

```markdown
> **更正（2026-08-21，05Z 上繳 §1）**：經 SHA256 三方比對
> （本快照 = git HEAD = `7344b995d0b4faf2`），`build_batch_context.py`
> **亦非**本 session 之產出。**三支腳本全部**為 2026-08-21 09:13–09:15
> 另一 session 覆蓋所得；本 session 執行層原產出之三份皆已失落，無備份。
> 本快照保全的是覆蓋後之狀態。
```

### T3 — R-TM48 依據 1 之逐字引入

於 R-TM48 條文之依據 1 後追加：

```markdown
（依 R-TM50 逐字引入 Project 層 charter 原文：
"The §-rules below are a periodic copy of
`docs/runtime/ASPICE_SWE6_AI_Instruction.md`; the repo version is
authoritative and evolves there. Re-sync at each feature close-out."
執行層對此類引用之正確標示為「結構性不可複驗」。）
```

### T4 — context 層編碼（本包主要工作）

依 §4 之六類實作於 `build_batch_context.py`。**須回報**：

1. C-1 至 C-6 逐類之實作位置與其資料來源
2. **C-1 / C-2 與 lint 層共用來源之所在**（§4.2 之要求），
   或說明為何無法共用
3. self-test 之 red-green 實際輸出（紅向：抽掉某類來源資料應報錯）
4. 產出之 context 範例（取 B1 之任一片 leaf，如 `-001`）全文

**不生成任何 TC** —— 本包只建 context 產生器並驗其輸出，不跑生成。

### T5 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM5[01]' features/time_management/RULINGS.md
grep -n 'G-TM1 更正\|結構性不可複驗' features/time_management/RULINGS.md
grep -n '更正（2026-08-21，05Z' features/time_management/ANOMALIES.md \
        features/time_management/data/scripts_snapshot_20260821/README.md
grep -n 'PENDING: DR-5\|PENDING: DR-6' features/time_management/scripts/build_batch_context.py
grep -c 'modified by TC_Generator' features/time_management/scripts/*.py
```

條數以增量回報，附執行前後兩個實測值。

### T6 — 上繳

`docs/upstream/06_context.md`。須含 T5 全部輸出、T4 之四項、
**本包是否仍有該驗而未驗者之獨立判斷**（明列全集）。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- 不改 `backend/`、不改 canon、不改 `docs/fw036/framework.md`
- 不修改 `data/spec_reference_candidates.txt` 原檔
- 不將 `CFTS015-6151328` / `-6151331` 寫入任何欄位
- **不填 `functional_safety` 之值**（A-TM24 未決）
- **不杜撰任何 CAN 網段**（R-TM49 / R-TM51）
- 不動 `TODO(R-TM10-A1)` 之步驟措辭常數與 ER 樣板
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 6. 呈報 Pei —— B1 之兩個硬阻塞

`06` 完成後，B1 生成之阻塞項只剩兩個，**兩個都要你**：

1. **A-TM24 `functional_safety` 之值** —— 來源 1 已由實測否定
   （母本四組 DV 涵蓋 P–Q / R / T–Z / AF，S 欄不在其中）。
   轉來源 2（036 填寫規範或 SWQT 既定慣例）或來源 3（範圍界定）。
   該欄為交付欄位且由條文定（A4 之決定），不填即 `--write` 被攔。

2. **R-TM10-A1 之步驟措辭常數與 ER 樣板** —— 樣式參照仍 SUSPENDED、
   無候選。B1 生成需要 `ENTER_*` 一類之標準步驟措辭與 ER 句式，
   而 canon §5.3 明訂該類為專案級常數須逐字重用。
   **可行之路徑有二**：(a) 解除 R-TM10-A1 並指定一個可用之樣式來源；
   (b) 維持 SUSPENDED，由本 feature 依 canon §5.1–5.6 自行擬定一套，
   並接受其與他 feature 不一致。**請擇一。**

其餘：RD-1 Q-TM1–3 + N-TM1 已備齊，送出屬你；分支 ahead 未 push。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM50 | 分析層自裁，charter 逐字引入 | §2 | ✅ T1 + T3 |
| R-TM51 | 分析層裁定，R-TM49 例外判準 | §3 | ✅ T1 |
| G-TM1 更正 | context 層編碼不存在 | §1.1 | ✅ T1 |
| A-TM20 記載更正 | 三支皆非本 session 產出 | §1.2 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未改 canon、未改 `backend/`。
