# 上繳 03 — 部分執行：T1 / T7 完成，T2 / T3 / T4 / T5 停止

執行層 → 分析層。對應 `docs/handoff/03_signoff.md`。2026-08-20。

**本包未完整執行。** T1（條文登記）與 T7（RD-1 草案）已完成；
**T2、T3、T4、T5 停止並回報**，各有獨立理由，逐節說明。
T6 之七項驗證有兩項不符、兩項失效，見 §6。

---

## 1. T6 七項驗證結果

| # | 判準 | 期望 | 實際 | |
|---|---|---|---|---|
| 1 | `grep -c '^## R-TM' RULINGS.md` | 22 | **21** | ❌ §2.1 |
| 2 | `grep -c '^## Part ' docs/fw036/framework.md` | 7 | **6** | ❌ §2.2 |
| 3 | `grep -n '待簽'` 應已無 | 0 | **0** | ⚠️ 假通過，§2.2 |
| 4 | `grep -n 'B1（pilot）'` 應命中 | 命中 | **命中 2** | ⚠️ 假通過，§2.2 |
| 5 | `ls -d "features/vehicle setting"` 應已清 | 已清 | **已清** | ⚠️ **非我所為**，§4 |
| 6 | `archive/vehicle setting/WHY_ARCHIVED.md` | 存在 | **不存在** | ❌ §4 |
| 7 | `grep -c '^## A-TM' ANOMALIES.md` | 16 | **16** | ✅ |

## 2. T1 完成，但條數差一 —— **R-TM16 之來源不明**

R-TM17 / R-TM18 / R-TM19 已逐字追加。

### 2.1 條數落差

| 依據 | 追加前 | 追加後 |
|---|---|---|
| `02R` T1 明載 | 16 | **18**（+ R-TM14、R-TM15） |
| `03` T1 稱 | **19** | 22 |
| 執行層實測 | 18 | **21** |

**缺 R-TM16。** 執行層已收之全部下放包中，`R-TM16` 未曾以條文區塊出現；
`RULINGS.md` 現有 R-TM1…R-TM15、R-TM17…R-TM19，編號在 16 處斷開。

可能為：(a) 有一包未送達執行層；(b) 編號跳號；(c) `03` 之計數誤植。
**執行層不自行補號、不自行認定**，提請確認。

### 2.2 T2 停止 —— **目標不存在，且與 02R 直接矛盾**

**理由一：目標字串零命中。** `03` T2 指定改 `docs/fw036/framework.md`
之兩處，實測：

```
'下列七 Set 表待簽'                          → 0 命中
'**未定。** 待 Layer 2 經 Pei 簽核後另行起草' → 0 命中
'待簽'（任意出現）                            → 0 命中（全檔）
```

**理由二：Part VII 不存在。** 該檔實測僅 Part I–VI：

```
Part I — Media HMI          Part IV — SXM
Part II — Home HMI          Part V  — Projection
Part III — AMFM (CFTS024)   Part VI — Privacy (CFTS022)
```

T6 判準 3（`待簽` 應已無）因此為**假通過** —— 它從未存在，非本包清除。
判準 4（`B1（pilot）` 應命中）同為假通過 —— 命中之 2 處屬
**Part VI Privacy** 之批次表（`framework.md:1213` 一帶），與本 feature 無關。

**理由三：與 `02R` T3 直接矛盾。** `02R` T3 明令：

> **不寫入 `docs/fw036/framework.md`**（全域檔，跨 feature，待 Pei 裁
> 是否併入）

並指派建 `features/time_management/framework.md`。執行層已依 02R 照辦。
`03` T2 卻要求改該全域檔之 Part VII。**兩包對同一檔案給出相反指示。**

**處置**：依 02R（較早明令且理由完整）不動全域檔。R-TM17 之簽核**實質
內容已生效** —— 七組、Layer 1/3、三條界線均已載於
`features/time_management/framework.md`；受影響者僅其所在檔案。
R-TM17 條文已於 `RULINGS.md` 登記並附此註記。

**提請**：`docs/fw036/framework.md` 是否新增 Part VII 併入本 feature，
屬 `02R` §5 第 5 項所列之待裁事項，尚未有裁定。

## 3. T7 完成

`docs/fw036/RD1_questions_time_management.md` 已建（63 行），
Q-TM1 / Q-TM2 / Q-TM3 逐字，**狀態 DRAFT，未送出**。

## 4. T3 停止 —— **目標已被他方刪除，且違反 R-TM18 之「只 mv 不 rm」**

### 4.1 實測

```
ls -d "features/vehicle setting"        → 不存在
ls "archive/vehicle setting/"           → 不存在
全 repo os.walk 搜尋 'vehicle setting'  → 0 命中
git log --all -- "features/vehicle setting" → 無任何 commit
```

`features/` 現有 11 個目錄，含 `vehicle_setting`（底線版），
**無任何含空格者**。

### 4.2 判讀

**該目錄已從磁碟移除，且不在 `archive/`。** 依 R-TM18 之限制 1
（「只 mv，不 rm。移入後原路徑不得存在，**archive 內容須逐檔可讀**」），
現況只滿足前半、不滿足後半 —— 即**其形態為刪除，非封存**。

**執行層未執行 T3**：本 session 從未對該目錄執行任何 mv / rm。
本 session 對該路徑之全部動作僅為 `ls` 與 `git check-ignore`（唯讀）。

**不可復原**：該目錄從未進入 git（`git log --all` 零命中，且其父
`features/` 下該路徑於本 session 初始 `git status` 為 `??` untracked），
故無 blob 可取回。

### 4.3 併行作業之關聯

本 session 期間另有 session 於同一 repo 作業（證據見 §5.2）。
執行層**不推定**該刪除為其所為 —— 亦可能為 Pei 手動處置。
**登記事實，不認定行為者。**

### 4.4 對 A-TM01 之影響

**A-TM01 未轉 RESOLVED。** R-TM18 所定之處置（mv 入 archive + 建
`WHY_ARCHIVED.md`）並未發生，發生的是另一種結局。若逕標 RESOLVED，
等於以「處置條文 R-TM18」記載一件與該條文不符之事實。

**提請裁定**：A-TM01 應標為
(a) `RESOLVED — 目標已不存在，處置目的達成但方式不符 R-TM18`，或
(b) 維持 PENDING 並另立條記錄刪除事件，或
(c) 其他。

**執行層未自行選定**，A-TM01 維持 PENDING。

## 5. T4 / T5 停止 —— 共用腳本 × 併行 session

### 5.1 風險

T4 / T5 要改 `scripts/recon.py`、`scripts/new_feature.py`、
`scripts/intake.py` —— **三者皆為全 feature 共用**。

而 R-TM19 指定之回歸判準為：

> 對 `features/vehicle_setting` 實跑 `recon.py`，`RECON.md` 之內容須與
> 修改前逐位元相同；`DECISIONS.md` 之 mtime 與 SHA256 須不變。

**該目錄正由另一 session 作業中。**

### 5.2 併行作業之證據

| 事實 | 依據 |
|---|---|
| 本 session `git add` 後、`git commit` 前，他方執行了 commit | `554079e` 標題為 `feat(vehicle_setting): rounds 02-03`，內含 **25 個 time_management 檔 + 12 個 vehicle_setting 檔**，共 37 檔；本執行層之 commit message 未進入 git，`git commit` 回報 `nothing added to commit` |
| `vehicle_setting/` 檔案於本 session 期間持續變動 | `ANOMALIES.md` mtime 16:51、`data/` 16:49，均晚於本 session 開始 |
| 該目錄有本 session 未曾接觸之新產物 | `docs/handoff/04`–`08`、`docs/upstream/02_variables_and_sweep.md`、`data/_cfts_values*.json` 等 |

### 5.3 具體衝突

1. **回歸之受測物正在被第三方改動** —— 「`RECON.md` 逐位元相同」之判準
   在受測目錄同時被他人編輯時不可靠：diff 有輸出時無法區分是我的修法
   造成，或是他方的編輯造成。**判準失去鑑別力。**
2. **修法失敗之損害落在他人身上** —— T4 之修法若有誤，第一次回歸實跑
   即沖掉 `features/vehicle_setting/DECISIONS.md`。R-TM19 自己指出
   「回歸動作本身會造成它要防止的那種損害」，該風險在併行狀態下由
   **另一 session 承擔**，非本 feature。
3. **他方可能正在執行這些腳本** —— 對共用腳本做非原子性寫入，可能使
   其讀到改到一半的檔案。

### 5.4 執行層之判斷

R-TM19 之階段順序設計（A-TM15 最先修）已正確識別「回歸會造成它要防止
的損害」這一風險，**但該設計假設 repo 為單一作業者**。在併行狀態下，
即使順序正確，第 1 點之判準失效與第 2 點之損害外溢仍然成立。

**故停止，不執行。** 此非對 R-TM19 之異議 —— 修法內容（三處改法）
本身已逐字讀過且無疑義。停止的是**執行時機**。

### 5.5 解除條件（建議）

以下任一成立即可執行：

1. 確認另一 session 已停止作業，且 `features/vehicle_setting/` 工作樹
   靜止；或
2. 改以其他 feature 為回歸對象（`features/media`、`features/home`、
   `features/sxm` 等本 session 期間未見變動者）—— 但須先確認該 feature
   之 `DECISIONS.md` 現況並取基線；或
3. Pei 明示承擔該風險並指示執行

**執行層建議 2**，成本最低且不需協調：回歸判準之實質是「recon.py 之
輸出不變」，任何既有 feature 皆可充當受測物，不必是 `vehicle_setting`。

## 6. T8(5) — 該驗而未驗者（續用五全集）

### 6.1 依全集 1（指令逐項）

| T | 狀態 | 複查 |
|---|---|---|
| T1 | 完成 | 條數 21，**與期望 22 不符**，已回報（§2.1） |
| T2 | **停** | 目標零命中 + 與 02R 矛盾（§2.2） |
| T3 | **停** | 目標已被他方刪除（§4） |
| T4 | **停** | 併行風險（§5） |
| T5 | **停** | 同上 |
| T6 | 完成 | 七項結果見 §1，含兩項假通過之標示 |
| T7 | 完成 | 63 行，DRAFT |

### 6.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | `grep -c '^## R-TM'` | 21 ✅（附落差回報） |
| `docs/fw036/RD1_questions_time_management.md` | 行數 + 內容 | 63 行 ✅ |
| `framework.md`（02R T3） | 行數 | 57 行 ✅ |

### 6.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **037 leaf 描述全文** | **仍未讀** —— 02R §2 之語意複核與三條界線仍為單方實測。R-TM17 已將三條界線定為 §8.2.1 拘束條款，**將於 B1 生成時逐條適用**，其未經雙方確認一事應在生成前解決。已於 `02R_corrections.md` §3.3 提請 |
| 2 | R-TM16 之存否 | 見 §2.1，不自行認定 |
| 3 | `features/vehicle setting` 之刪除者與時點 | **不查** —— 屬他方作業與 git 歷史，非本 feature 範圍；且 §4.3 已言不推定行為者 |
| 4 | 交付路徑 Home 複本內容 | 刻意不驗（R-TM10-A1） |
| 5 | PU 陽性對照 | 待 Pei 裁 |
| 6 | `write_back` 兩值 | Phase 3 |

### 6.4 依全集 4（「不存在」之陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| `待簽` 全檔零命中 | 同檔 `B1（pilot）` 命中 2、`Batch plan` 命中 2 → 掃描有效 | ✅ |
| `vehicle setting` 全 repo 零命中 | 同一 `os.walk` 列出 `features/` 下 11 個目錄含 `vehicle_setting` | ✅ |
| Part VII 不存在 | 同一 grep 列出 Part I–VI 共 6 個 | ✅ |

## 7. 本包未動之事項

未動 git（`554079e` 之情形見 §5.2，非本 session 所為）。
**未 mv / rm 任何檔案或目錄。** 未改任何腳本。未生成任何 TC。
未送出 RD-1。未填 `D5`。未援引他 feature 樣式。未以 openpyxl 存回任何
工作簿。未跑 `recon.py`。未改 `docs/fw036/framework.md`。
未將 A-TM01 標為 RESOLVED。
