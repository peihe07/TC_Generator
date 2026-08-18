# 上繳 33 — W-1：pre-condition 之循環與完成式自檢

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`33_review_close3.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第四批未開**
- 語料：**108 條，未變動**（本輪修改其中 1 條之 pre-condition、procedure、ER 與 remarks）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 108 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 108 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／**W-1 4 待判**／V-1 13 待判／U-2 0／U-1 3 待判／T-1 0／K-4b 0／Q-1 9 待判 |
| `audit_consistency.py --self-test` | **36 / 36**（＋2：W-1）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 13 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

---

## 1. W-1 —— `TC-094` 之修正

### 1.1 判定成立，且其成因比「違反 §4.4」更具體

`TC-094` 之 pre-condition 原為 `Every Profile **has been deleted** from the
head unit`。而 4.5（PRACC5）逐字：

> `If no custom Profile is set up, **or all profiles are deleted**, there will
> **always** be a default, non-connected profile in the vehicle.`

**該前提所描述的是一個系統不允許存在之穩態** —— 「全部 profile 都被刪除」
之後，條文保證車上**立刻**有一個預設 profile。
故測試員讀到 pre-condition 時，其所述之狀態**已經是假的**。

且其蘊含之結果（車上只剩 Driver 1）**正是本 TC 之 ER 要斷言者** ——
兩重問題疊在同一句上。

### 1.2 修正（比照同 leaf 群之 `TC-093`）

| 欄 | 前 | 後 |
|---|---|---|
| pre 1 | `Every Profile has been deleted from the head unit` | `The default Profile has been customized and its name is still “Driver 1”` |
| procedure | 1. 開分頁　2. 讀清單並確認唯一 | **1. `Delete every Profile from the head unit`**　2. 開分頁　3. 讀清單並確認唯一 |
| ER | 2 條 | **3 條**（ER1 `Every Profile is deleted`）|

**pre 2（座椅鍵少於 2）不動** —— 那是條文自帶之例外
（`unless there are 2 or more memory seat buttons`），非受測結果。

### 1.3 **兩條之分野不變，且修正後更清楚**

`093` 與 `094` 現在 **procedure 相同**、**ER3 不同**：

| tc_id | 其 ER3 | 驗什麼 |
|---|---|---|
| `093`（`007-02`）| `A default “Driver 1” Profile is present **and its preferences are at their default values**` | **重建發生**，且重建出的是**預設**而非改名留下之客製 profile |
| `094`（`007-03`）| `“Driver 1” is present **and no other Driver Profile is listed**` | **重建後只有一個** |

**同一個操作、兩個不同的斷言** —— 037 切成兩個 leaf，故不合併（§8.2.1）。

---

## 2. 完成式 pre-condition 之全批自檢 —— **命中 4 處，循環 1**

判準：pre-condition 含 `has／have／had been + 過去分詞` 者。

| tc_id | 節 | pre-condition | 該狀態是否即本 TC 之 ER 所斷言者 | 判 |
|---|---|---|---|---|
| **`094`** | 4.5 | ~~`Every Profile has been deleted`~~ | **是** —— 蘊含「只剩 Driver 1」，即其 ER | **循環 → 已移入 procedure** |
| `093` | 4.5 | `The default Profile has been customized…` | **否** —— ER 斷言的是**刪除後之重建**；客製化是使該重建有意義之佈署 | **保留** |
| `104` | 4.6.3 | `The Profile button has been removed…` | **否** —— ER 斷言的是 highlight 於他處仍適用；移除是 **4.6.3 之適用條件本身**（§8.7.3），且該操作屬 Home feature，本 TC 以其結果為前提（§8.4.2）| **保留** |
| `005` | 6.2.1 | `No default Profile has been customized or deleted` | **否** —— ER 斷言的是「**建立新 profile 之後**預設仍在」；本句只是起始狀態 | **保留** |

### 2.1 **修正後 `094` 之 pre 仍是完成式，且那是對的**

改後之 pre 1 為 `The default Profile **has been customized**…`（同 `093`）。
**它仍會被本掃描列出，而那不是問題** ——
判準是「**該狀態是不是本 TC 的 ER 要斷言的東西**」，不是「有沒有用完成式」。
客製化是**佈署**，重建後只剩一個才是**斷言**，兩者不同，故非循環。

**這一點正是本掃描只能「待判」的理由**：完成式本身無罪，
**四處中三處（現為三處保留 ＋ 一處修正後仍保留）都是正當的佈署描述**。
硬判為紅會把它們全部誤殺 —— 與 V-1／U-1 同型（32 輪 §2.2、31 輪 §1.3）。

### 2.2 方向性案例（＋2，共 **36 / 36**）

| 案例 | 期望 |
|---|---|
| pre 以完成式述動作結果（`has been deleted`）| **列入待判** |
| **護欄**：pre 為狀態描述（`is active`／`exists`）| **不得列入** |

護欄之作用同 V-1：**若它倒了，待判清單會等於全語料**。

---

## 3. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **W-1 只認完成式** | 判準盲區 | 以**主動完成句**寫成之同型（`The user deleted every Profile`）或**名詞化**（`With all Profiles deleted`）看不見。現行語料無此形態，**但那是巧合** |
| 2 | **循環與否仍靠人判** | 設計選擇 | §2.1 —— 四處中三處為正當佈署，硬判會全部誤殺 |
| 3 | **第四批取樣清單仍未經覆核** | **分析層待辦** | 29 輪提出，**已隔四輪**；下放包載明第四批待其覆核 |
| 4 | **V-1 13 處、U-1 3 處、Q-1 9 處、D-3 13 處黃** | 承前 | 判讀未變 |
| 5 | **`TC-091` 之實車可觀察性** | 承前（32 輪）| 已入 remarks，待實機 |
| 6 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 7 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

### 3.1 四輪連續之形態（承 32 輪 §3.1）

| 輪 | 缺陷 | 對應關係 |
|---|---|---|
| 30（T-1）| ER 引用之基準線不存在 | 步驟 ↔ ER |
| 31（U-1／U-2）| popup 未綁分支／記錄無人引用 | 斷言 ↔ 分支、步驟 ↔ ER（反向）|
| 32（V-1）| 覆寫之發生點被序列錯過 | 步驟 ↔ 條文時序 |
| **33（W-1）** | **前提蘊含被測結果** | **前提 ↔ ER** |

**四輪四種對應關係，四處都是人工覆核先發現。**
本輪之 W-1 補上了最後一組常見對應（前提↔斷言）——
連同 T-1（步驟↔ER）、U-2（其反向）、V-1（步驟↔條文），
**一條 TC 之四個欄位間的兩兩對應現在都有掃描在看**。

**但四支掃描有三支是「待判」而非「紅」**（V-1／U-1／W-1）——
因為它們要判的都是**語意關係**，而語意關係機械判不了。
**這是本 feature 之閘所能到達的界線**：可測的是「有沒有」，
不可測的是「指的是不是同一件事」。

---

## 4. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch03.py`（`TC-094` 之 pre／procedure／ER／remarks）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（**W-1 待判掃描** ＋2 方向性案例）| 否 |
| 3 | 檔案重生成 ×30 | `generated/`（batch03；**內容變動者 1 條**：`094`）| 否 |
| 4 | **檔案新建** | `docs/upstream/33_review_close3.md`（本檔）| 否 |
| 5 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 6 | 程式執行 | 完成式 pre-condition 全批掃描、生成 ×1、全部閘、九支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第四批未開**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
