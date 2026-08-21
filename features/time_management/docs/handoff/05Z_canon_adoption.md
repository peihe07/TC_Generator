# 05Z — 階段 B 受理；canon 三節生效，D5 與 A-TM13 之處置隨之改變

分析層 → 執行層。覆核對象：`docs/upstream/05R_corrections.md`。**受理。**

**T1 之偏離正確，且改指之依據比我引的強。** 但本包最要緊的是 §5.4 之
三節新 canon —— 其中兩節**改變已裁定之處置**，見 §2。

---

## 1. T1 偏離 —— 受理，且我引的規則已不存在

`grep -c 'Use the SourceID format'` → **0**。canon §10.7 已由他方整節改寫。
執行層未照字面執行而改指新 §10.7(a)：

> CFTS 母文件 → `CFTS{nnn}-{ObjectID}`，ObjectID 為該物件之 Polarion
> 7 位號碼。短號需求 ID（如 CFTS015-824）不得作為錨，僅得於 reasoning 引用。

**新依據強於我引者，且強在兩處**：

1. 由「明文**允許**使用 SourceID 格式」變為「明文**規定** CFTS 母文件
   即用此格式」
2. **明文禁止短號作為錨**，且其舉例 `CFTS015-824` 恰為本 feature 短號家族
   之成員 —— canon 直接回答了 A-TM23 之疑問

**A-TM23 可據此結案**：兩套編號並存之事實不變，但「該採哪一套」已由
canon 明定，不再需要 RD-1 之 Q-TM4 來問。見 T3。

我在 `05R` §4.1 引 canon §10.7 時，讀的是 **Project 指令內之週期性副本**
而非 repo 現行檔。charter 明訂「repo 版本為權威」，我沒回查。
**這與 R-TM38（引用截斷）同族：前者引到一半，本次引了過期版本。**

## 2. **新 canon 三節 —— 全數於本 feature 生效，且兩節改變已裁定之處置**

執行層未逕行調整、提請分析層評估，**正確**（canon 之適用範圍屬 Tier 2）。

```
R-TM48（分析層裁定，2026-08-21）—— canon 新增三節於本 feature 生效

docs/runtime/ASPICE_SWE6_AI_Instruction.md 新增之 §4.3.1、§8.4.3、
§8.7.5 自即日起於本 feature 生效。

生效依據（三項，非僅「repo 版為權威」）：
1. charter 明訂 repo 版本為權威，Project 指令內之 §-rules 為週期性副本
2. §4.3.1（test_item 兩段式）與 §8.4.3（缺件佔位）與 Pei 既有之直接
   指示一致 —— 二者皆為 Pei 於本專案層級已表明之硬性要求，非草案
3. 三節皆為**收緊**（增加約束），非放寬。收緊條文提前適用之風險為
   「做了多餘的功」，放寬條文提前適用之風險為「交付件不合規」——
   兩者不對稱

**未 commit 之工作樹狀態不影響其效力** —— 條文之效力來自其內容與 Pei
之意思，不來自 git 狀態。
```

### 2.1 §8.4.3 —— **D5 與 A-TM13 之處置改變**

新節：欄位無法填寫時寫 `PENDING: DR-{n}`，**不得留空、不得填 NA**。

**這推翻了兩條既有裁定之處置部分**（結論方向不變，作法改變）：

```
R-TM9-A2 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）

原文第 2、3 點：「該值在 A-TM02a 裁定前無法取得。D5 維持空白。」
「空白是可見狀態；指向不存在文件之值不是。」

**訂正**：D5 不得留空。改填 `PENDING: DR-{n} 037 正式報告檔名`，
並於 features/time_management/DATA_REQUESTS.md 登記該 DR。

原理由（空白是可見狀態）之**意圖不變且被新規更好地實現** ——
`PENDING: DR-n` 比空白更可見，且直接指向缺件之登記處。
禁止「以 feature 名或類推形態組出字串填入」之部分**完全不變**。
```

```
R-TM41 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）

原文：「CFTS015-6151328 與 CFTS015-6151331 不得寫入 specification_reference。」

**訂正**：該二字串仍不得寫入（理由不變 —— 已實測為偽之斷言）。
但受影響之條目**不得因此留空**，改填 `PENDING: DR-{n} CFTS015 缺件物件
6151328 / 6151331`，並登記 DR。

即：**不寫偽值，也不留空，寫佔位。** 三者是三種狀態，新規要求第三種。

B3（lint_spec_gap）之判準隨之改變：由「Remarks 為空即報」改為
「Remarks 未含 `PENDING: DR-` 佔位即報」。
```

**`NA` 之界線**：新規明訂 `NA` 僅限「確認不適用」。故
`input_test_data` 之 `NA`（canon §4.5：資料已屬 PC/Procedure 者設 NA）
**仍為合法**，因其為「確認不適用」而非「缺件」。**兩者不可混用**，
B5 之必填檢查須能區分。

### 2.2 §4.3.1 —— `test_item` 兩段式

上半 verbatim 上限 **50 token**、超限須摘句；下半 `(...)` 測試目的，
**缺括號 = FAIL**。

與 B2（leaf 文字來源隔離）**相容且互補**：B2 管上半之文字來源，
§4.3.1 管其長度與下半之存在。**B2 須加兩項判準**（見 T4）。

### 2.3 §8.7.5 —— 訊號三件組，對 B4 衝擊最大

CAN 訊號斷言須 `<Signal> in <MESSAGE> on <segment>`；
**網段須有 DBC 或架構文件依據，查無者標 PENDING 不得杜撰**。

本 feature **無 DBC，亦無架構文件**（intake 之素材為 CFTS docx + SYS2 +
037 三份，見 A-TM02a 之清單）。故：

- B4 之 `BOUNDARY_SIGNALS` 現以單 token（`$DateTmFormat$` 等）比對 ——
  **該用法不變**，因 B4 是**偵測用**（找出 TC 內文命中鄰片訊號），
  非 TC 內容本身。偵測子字串不受記法規範拘束
- **但 TC 之 ER／Procedure 內容須依新規寫三件組**，而網段查無依據
  → 依 §8.4.3 標 `PENDING: DR-{n}`
- **CFTS015 內確有 MESSAGE 名**（`TELEMATIC_TIME_DATE`、`TIME_DATE`、
  `TELEMATIC_FD_1`、`EcuCfg3` 等），故三件組之前兩件有來源，
  **只有 segment 一件缺**

```
R-TM49（分析層裁定，2026-08-21）—— 訊號三件組之缺件處理

本 feature 之 CAN 訊號斷言依 canon §8.7.5 寫三件組。
Signal 與 MESSAGE 取自 CFTS015 內文（有來源）；
**segment 一律標 `PENDING: DR-{n} CAN 網段依據（無 DBC／架構文件）`**，
不得杜撰（如「B-CAN」「BH-CAN」等縱使 CFTS 內文出現，
亦須確認其為該訊號之網段而非上下文提及者方可用）。

例外：若 CFTS015 內文對某訊號明確敘明其網段（如 4814098 之
「set a BH-CAN message」），該敘述即為來源，得直接用，
並於 reasoning 註明其物件 id。

B1 生成時對每一訊號斷言逐項判定「有無明確網段來源」，
不得一律標 PENDING，亦不得一律填。
```

## 3. §4.3 綠向抓到真問題 —— 本包最有價值的一段

> 首次執行為 16/17，唯一失敗者為**綠向**：`remarks` 被誤列必填。
> 若無綠向，此誤報不會被發現，且其後果是 20 片正常 leaf 全部誤報 ——
> 一個把真發現淹沒在雜訊裡的閘門。

**這是「紅向全過不代表閘門正確」之實例**，且其後果比漏抓更惡劣：
漏抓是少一道防線，誤報是**主動製造雜訊使其他防線失效**。

且成因值得記：`remarks` 之必要性是**條件式**的（僅 A-TM13 兩片與 BLOCKED
列需填），而 B5 之必填清單是**無條件**的。**把條件式必填放進無條件清單**
——與「值域 vs 分佈」（C2）、「形式 vs 操作」（R-TM38）同一形態：
**兩種不同性質的東西被放進同一個判準。**

§4.4 之 B5 紅向構造（只留一欄空，不用全空 TC）亦正確 ——
全空 TC 同時觸發多閘，看不出是哪一閘抓到的。

## 4. 三項提請 —— 逐項處置

| 提請 | 處置 |
|---|---|
| §2.2 候選表是否需依新 §10.7 重排 | **需要，但不改原檔**。原 `data/spec_reference_candidates.txt` 保留為軌跡（R-TM13），另產 `spec_reference_candidates_v2.txt` 依新排列規則。見 T5 |
| §5.3 B1 於 `generated/` 為空時被跳過 | **確為缺陷**，本包指派修正。B1 為工作簿層檢查，與是否已生成 TC 無關 |
| §5.4 新 canon 三節 | 見 §2，全數生效 |

---

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM48 / R-TM49，並訂正 R-TM9-A2 / R-TM41

三處新增／訂正，標題行：

```
## R-TM48 — canon 新增三節於本 feature 生效
## R-TM49 — 訊號三件組之缺件處理
```

R-TM9-A2 與 R-TM41 之處置訂正，依 §2.1 之兩個區塊，
**原文加刪除線保留**（R-TM13），訂正文置於其下。

**增量（R-TM46）**：`## R-TM` **+2**；`## G-TM` **0**；`## A-TM` **0**。
回報執行前後之兩個實測值。

### T2 — `DATA_REQUESTS.md`：登記三筆 DR

依 canon §8.4.3，`PENDING: DR-{n}` 之 `n` 須有登記。於
`features/time_management/DATA_REQUESTS.md` 登記（編號接續既有，
**回報所配之實際號碼**）：

| 缺件 | 阻塞欄位 | 對應 anomaly | Urgency |
|---|---|---|---|
| 037 正式報告（檔名符合 FM-WI-FSM-037-A03 形態） | D5 範圍 Scope | A-TM02a / A-TM11 | High |
| CFTS015 缺件物件 6151328 / 6151331 之來源文件 | 005 / 002 之 spec_reference | A-TM13 | High |
| CAN 網段依據（DBC 或架構文件） | 訊號三件組之 segment | R-TM49 | High |

### T3 — `ANOMALIES.md`：A-TM23 結案

依 §1，canon §10.7(a) 已明定該採 7 位家族並禁短號為錨。
A-TM23 由 AWAITING_UPSTREAM 轉 **RESOLVED**，條末追加：

```markdown
**結案（2026-08-21，依 canon §10.7(a) / R-TM48）**

canon §10.7(a) 明定 CFTS 母文件之錨為 `CFTS{nnn}-{ObjectID}`（Polarion
7 位號碼），且明文禁止短號需求 ID 作為錨（其舉例 `CFTS015-824` 恰為本
feature 短號家族之成員），短號僅得於 reasoning 引用。

兩套編號並存之事實不變；「該採哪一套」已由 canon 明定，不需 RD-1 回答。
Q-TM4 隨之改為僅供上游知悉之說明，不列為待答問題（T4）。
```

**A-TM 條數不變。**

### T4 — Q-TM4 降級為說明

`docs/fw036/RD1_questions_time_management.md` 之 Q-TM4，
標題改為 `## N-TM1 — spec_reference 之參照體系（說明，非提問）`，
內文末段之「**問**：」段改為：

```markdown
**說明（非提問）**：依 canon §10.7(a)，本工作簿採 `CFTS015-{Polarion
7 位 ObjectID}`，短號需求 ID 不作為錨、僅於 reasoning 引用。
此處記載供上游知悉，不需回覆。
```

### T5 — 候選表 v2（依新 §10.7 排列規則）

**不改原檔**。另產 `data/spec_reference_candidates_v2.txt`，
排列規則：一來源文件一行；同文件內多 ObjectID 以 `, ` 續列且
**前綴僅敘明一次**；禁用 `;`；同文件內 ID 升冪。

A-TM13 之兩片，其 BLOCKED 條目依 R-TM41 訂正改為
`PENDING: DR-{n}` 形式（`n` 取 T2 所配之號）。

檔頭加來源標記（R-TM33）。

### T6 — `lint_tcs.py`：三項調整

| # | 依據 | 動作 |
|---|---|---|
| L1 | §5.3 | **B1（`lint_d5_scope`）移至 `if not gen: return 0` 之前** —— 其為工作簿層檢查，與是否已生成 TC 無關 |
| L2 | R-TM9-A2 / R-TM41 訂正 | B1 之判準改為「D5 未含 `PENDING: DR-` 且非合法 037 檔名 → 報」；B3 之判準改為「Remarks 未含 `PENDING: DR-` 佔位 → 報」 |
| L3 | canon §4.3.1 | B2 加兩項：上半 verbatim **> 50 token 未摘句** → 報；**下半缺 `(...)` 括號** → 報（缺括號 = FAIL）|

**三項各附 red-green，紅向須實跑。** L3 之紅向以「無括號之 test_item」
與「51 token 之上半」兩個構造分別觸發。

### T7 — 階段 C 收尾

C3 剩餘：`build_batch_context.py` 加來源標記（R-TM33）。
其餘 `TODO(R-TM10-A1)`（步驟措辭常數、ER 樣板）**維持不動**。

### T8 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM4[89]' features/time_management/RULINGS.md
grep -n '處置訂正' features/time_management/RULINGS.md
grep -n '^| A-TM23' features/time_management/ANOMALIES.md      # 應 RESOLVED
grep -n 'PENDING: DR-' features/time_management/DATA_REQUESTS.md
grep -n 'N-TM1' docs/fw036/RD1_questions_time_management.md
grep -n 'lint_d5_scope' features/time_management/scripts/lint_tcs.py   # 應在 early return 之前
grep -c 'modified by TC_Generator' features/time_management/scripts/*.py  # 三支皆應有
head -3 features/time_management/data/spec_reference_candidates_v2.txt
```

### T9 — 上繳

`docs/upstream/05Z_corrections.md`。須含 T8 全部輸出、T2 所配之 DR 號碼、
T6 三項之 red-green 實際輸出、
**本包是否仍有該驗而未驗者之獨立判斷**。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- 不生成任何 TC（B1 為 `06`）
- 不改 `backend/`、不改 canon、不改 `docs/fw036/framework.md`
  （R-TM47 之落點寫入待他方 canon 變更穩定後另包）
- **不修改 `data/spec_reference_candidates.txt` 原檔**（軌跡）
- 不將 `CFTS015-6151328` / `CFTS015-6151331` 寫入任何欄位
- 不填 `functional_safety` 之值（A-TM24 未決）
- 不杜撰 CAN 網段（R-TM49）
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 6. 呈報 Pei

1. **A-TM24 `functional_safety` —— 來源 1 已否定**（S 欄無 DV，實測四組
   DV 涵蓋 P–Q / R / T–Z / AF）。轉來源 2（036 填寫規範或 SWQT 慣例）
   或來源 3（範圍界定），**兩者皆須你裁**。這是 B1 寫回前之硬阻塞。
2. **canon 三節之生效我已裁定**（R-TM48）。若你認為該三節仍為草案、
   不應於本 feature 提前適用，請即示 —— 已依其調整之項為
   D5 處置、A-TM13 Remarks、訊號記法三處。
3. **R-TM10-A1** 仍無候選。步驟措辭常數與 ER 樣板為 B1 之另一阻塞項。
4. RD-1 現為 Q-TM1–3 + N-TM1（說明），送出屬你。
5. 分支 ahead 14 未 push。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM48 | 分析層裁定，canon 三節生效 | §2 | ✅ T1 |
| R-TM49 | 分析層裁定，訊號三件組缺件處理 | §2.3 | ✅ T1 |
| R-TM9-A2 處置訂正 | D5 改填 PENDING: DR-n | §2.1 | ✅ T1 + T6(L2) |
| R-TM41 處置訂正 | 兩物件改填 PENDING: DR-n | §2.1 | ✅ T1 + T5 + T6(L2) |
| A-TM23 → RESOLVED | anomaly 結案 | §1 | ✅ T3 + T4 |

分析層本包未動 git、未改任何腳本、未改 canon、未改 `backend/`。
