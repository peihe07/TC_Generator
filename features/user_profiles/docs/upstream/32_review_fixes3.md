# 上繳 32 — V-1：覆寫之發生點與時序語自檢

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`32_review_batch03c.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第四批未生成**
- 語料：**108 條，未變動**（本輪修改其中 1 條之 procedure、ER 與 remarks）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 108 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 108 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／**V-1 13 待判**／U-2 0／U-1 3 待判／T-1 0／K-4b 0／Q-1 9 待判 |
| `audit_consistency.py --self-test` | **34 / 34**（＋2：V-1）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 13 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

---

## 1. V-1 —— `TC-091` 之序列更正

### 1.1 下放包之判定成立，且其診斷即為修法

| | 前 | 後 |
|---|---|---|
| 步驟 1 | `Switch the ignition off **and then on again**` | `Switch the ignition off` |
| 步驟 2 | `Select memory seat button 1` | `Select memory seat button 1 **and switch the ignition on**` |
| ER1 | `… and then on again **with Driver Profile B active**` | `The ignition is off **with Driver Profile B as the last known Profile**` |
| ER2 | `Memory seat button 1 is pressed` | `Memory seat button 1 is pressed **and the ignition is on**` |
| ER3 | `Driver Profile A is active` | `Driver Profile A is **the Profile loaded at key-on** and Driver Profile B **is not loaded**` |

**ER1 之改動是關鍵**：原 ER1 斷言 `Driver Profile B active` ——
**它把本 TC 要證明「不會發生」的那件事，寫成已經發生的事實**。
現改為「B 是**上次之** profile」（一個 key-on 前的狀態），
覆寫遂有發生之餘地。

序列比照同節之 `TC-090`（key fob）—— **兩個覆寫分支自此同構**。

### 1.2 實車限制之聲明（依下放包明令寫入 remarks）

> 若該車之記憶座椅鍵**僅能於 ignition on 之後**按下，
> 則「A 為該 key cycle 之起始 profile」**在該車上不可觀察** ——
> 屆時須**回報該不可觀察性**，
> **不得以「先開機再按」充當覆寫之驗證**（那正是本次所修正之形態）。

**本 TC 不假定該鍵可於 key-on 前按**，只要求其操作**不晚於** key-on ——
`Select memory seat button 1 and switch the ignition on` 之寫法對
「同時」與「先按後開」皆成立，**未對車輛能力作出 spec 未載之推定**（§8.4.1）。

### 1.3 為何原序列「測到的是別的東西」

原序列在步驟 2 之後所觀察者為「按座椅鍵 → profile 切為 A」——
**那是 `SWE1-HMI-PROF-004-03`（`TC-086`）已覆蓋之行為**（4.3 之回復途徑）。
故原 `TC-091` 不只是漏測 4.4 之覆寫，**它還與 `TC-086` 重複**。
修正後兩者之分野恢復：`086` 驗**切換途徑**，`091` 驗**起始載入之覆寫**。

---

## 2. 時序語之全批自檢 —— **命中 13 條，真缺陷 1**

判準：被引之節（`cited[0]`）之 `pdf_text` 含
`at the start of`／`before`／`upon`／`prior to`／`as soon as`／`at the next` 者。

### 2.1 逐條判

| tc_id | 節 | 時序語之身分 | 判 |
|---|---|---|---|
| **`091`** | 4.4 | `at the start of` —— **真時序**（覆寫之發生點）| **紅 —— 已修** |
| `089` | 4.4 | 同上 | 綠 —— 預設路徑，key cycle 後讀取，順序相符 |
| `090` | 4.4 | 同上 | 綠 —— key fob 與 key-on 同時 |
| `088` | 4.3.1 | `before`（存在載入之前）—— **真時序** | 綠 —— 31 輪已以 ER2 綁定順序 |
| `064` | 12.8.2 | `prior to activating Valet Mode` —— **真時序** | 綠 —— 步驟 1 先記錄、步驟 2 才啟用 |
| `015`／`065`／`066` | 12.9 | `before system cancels` —— **真時序** | 綠 —— 皆先嘗試後觀察取消／鎖定 |
| `051` | 12.3.2 | `at the next key on` —— **真時序** | 綠 —— 斷電 → 復電並 key on → 讀取 |
| `035` | 9.7.2 | `prior to the deleted one` —— **位置，非時間** | 綠（且其步驟 1 仍先記錄）|
| `003` | 5.2 | `before creating a new one` —— **在 popup 文字裡** | 綠 —— 不約束測試順序 |
| `005`／`106` | 6.2.1 | `does not need to customize before creating` | 綠 —— 兩條分驗該句之兩半，順序皆相符 |

### 2.2 **同一個詞，三種身分 —— 這是本掃描只能「待判」的理由**

| 身分 | 例 |
|---|---|
| **真時序**（約束測試順序）| 4.4 之 `at the start of`、12.8.2 之 `prior to activating` |
| **位置**（非時間）| 9.7.2 之 `prior to the deleted one` |
| **在 popup 文字內**（不約束測試）| 5.2 之 `before creating a new one` |

**機械判準分不出來。** 若硬判為紅，`035`／`003` 那種**正確**的會轉紅 ——
與 U-1 之理由同型（31 輪 §1.3）。故本掃描只負責**縮小人工範圍**：
13 條，逐條由人判，已記於 §2.1。

### 2.3 方向性案例（＋2，共 **34 / 34**）

| 案例 | 期望 |
|---|---|
| 被引之節含 `at the start of`（4.4）| **列入待判** |
| **護欄**：被引之節無時序語（4.2）| **不得列入** |

護欄之作用：**若它倒了，待判清單會等於全語料**，那就不是縮小範圍而是沒有範圍。

---

## 3. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **V-1 之母體只看 `cited[0]`** | 判準盲區 | 併列之第二個節（如 `TC-072` 之 12.3.1）其時序語看不見。現行語料之併列節皆非時序條文，**但這是巧合，不是判準保證** |
| 2 | **V-1 無法自動判定順序一致與否** | 設計選擇 | §2.2 —— 硬判會使 `035`／`003` 轉紅 |
| 3 | **`TC-091` 之實車可觀察性未經實機確認** | **note，已入 remarks** | §1.2。**這是本 TC 唯一無法由文件解決之處** |
| 4 | **`TC-093`～`095` 之 3 條未經覆核** | **分析層待辦** | 下放包已聲明 |
| 5 | **第四批取樣清單仍未經覆核** | **分析層待辦** | 29 輪提出，**已隔三輪**；下放包載明「讀畢後第四批方得開批」 |
| 6 | **U-1 3 處、Q-1 9 處、D-3 13 處黃** | 承前 | 判讀未變 |
| 7 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 8 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

### 3.1 三輪連續之形態（承 31 輪 §3.1）

| 輪 | 缺陷 | 形態 |
|---|---|---|
| 30（T-1）| ER 引用之基準線不存在 | **步驟與 ER 之對應** |
| 31（U-1／U-2）| popup 未綁分支／記錄無人引用 | **斷言與分支之對應**／**步驟與 ER 之對應（反向）** |
| 32（V-1）| 覆寫之發生點被序列錯過 | **步驟與條文時序之對應** |

**三者皆為「對應關係」之缺陷，而非單一欄位之錯。**
現行十支閘多為**欄位內**之檢查（字面值、方法、判級、引用），
**對應關係之檢查全部是本三輪才長出來的，且全部是人工覆核先發現**。

**這件事本身值得記**：閘擋得住「寫錯」，擋不住「兩處各自正確而彼此不對應」——
A-UP12（互指之委派）也是同一類。

---

## 4. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch03.py`（`TC-091` 之 procedure、ER1–ER3、remarks）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（**V-1 待判掃描** ＋2 方向性案例）| 否 |
| 3 | 檔案重生成 ×30 | `generated/`（batch03；**內容變動者 1 條**：`091`）| 否 |
| 4 | **檔案新建** | `docs/upstream/32_review_fixes3.md`（本檔）| 否 |
| 5 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 6 | 程式執行 | 時序語全批掃描、生成 ×1、全部閘、九支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第四批未生成**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
