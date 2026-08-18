# 45 上繳 — AB-1 修正與全批自檢、靜態轉錄之指紋、上繳格式

- 產出層：執行層｜2026-08-18｜對象：分析層
- 來源包：`docs/handoff/45_fingerprints.md`（作業 1–5）
- **git 未執行**；**未產出交付件**；**未寫入他 feature 任何檔**；
  交付與 RD 寄出屬 Pei

## 0. 一頁摘要

| 作業 | 結果 |
|---|---|
| 1 | AB-1：`TC-154` 已改；**全批自檢命中 16 處**，逐條判定 —— 其中 **`TC-148` 為同型而未被下放包點名者，一併修正** |
| 2 | G-F：`27_rd_queries_v2`／`28_provenance4`／`34_provenance5` 加指紋（新閘 `stamp_static_doc.py`，5 / 5）；`26_rd_queries` **不標**，具名理由 |
| 3 | G-G：上繳格式加四份 pack 之 `--verify`（見 §5）—— **本輪它立刻抓到我自己弄過期的一份** |
| 4 | G-H：母本同一之邊界寫入 profile §7.4 |
| 5 | 全閘重跑：**13 支自我測試全過**，語料違規 0 |

### 0.1 本輪最值得記的一件事

**44 輪建立的過期檢查，在 45 輪就抓到了它的第一個真陽性 —— 而那是我自己造成的。**

AB-1 之修正動了 `TC-148`／`TC-154`，兩者都在 `44_review_pack_24b.md` 內。
G-G 所要求的「上繳時附 `--verify` 結果」跑出來是：

```
44_review_pack_24b.md：相符 9 條，不符 2 條
  AA-1 NR1L-UserProfiles-148: 指紋 `dba357deee2e` 與現況 `aaab1ed1b11c` 不符
  AA-1 NR1L-UserProfiles-154: 指紋 `34a1a6828e79` 與現況 `4e07e5f42f7a` 不符
```

**若無 G-G，我這一輪會把一份已被自己改過的 pack 當成有效的交上去。**
已於同輪重出為 `45_review_pack_24b.md`，舊檔加警語保留。

---

## 1. 作業 1 —— AB-1

### 1.1 `TC-154`（`052`，6.4）之修正

| | 原 | 現 |
|---|---|---|
| 步驟 4 | `Read the preferences and compare them with those recorded in step 1` | `Complete the setup and read the preferences of the new Driver Profile` |
| ER4 | `The preferences are unchanged from those recorded in step 1` | `The preferences of the new Driver Profile are the same as those recorded in step 1` |

**兩端現各屬何物已明指**：A 端為**新建 profile** 之偏好，
B 端為步驟 1 所記之**現用 profile** 之偏好；ER 斷言其**相同**
（carry-over 成立），而非「未改變」。

### 1.2 全批自檢：**命中 16 處，逐條判定**

判準：ER 行含比對語（`unchanged from`／`remains the same`／`is/are the same as`／
`differs from`／`match(es) those|the value`）**且**帶 `step N` 之回溯互參者。

**本掃描把兩端並排列出，不硬判** —— 因為「兩端同物」本身不是缺陷：

> `TC-084`（跨 key cycle 之保留）、`TC-137`（編輯連結後順序不變）之兩端
> 都是同一個東西，**其判別力來自中間那個事件**。
> 而「中間那個事件改不改得動它」要讀條文才知道。

| tc_id | 判定 | 理由（摘） |
|---|---|---|
| `085`／`086`／`087` | 成立 | 主詞已指名 `Driver Profile B's own value`，兩端不同物 |
| `130`／`184` | 成立 | 主詞已指名（`stored for Driver Profile B`／`The new Profile's`） |
| `101`／`144`／`187` | 成立 | ER 為 **differs**（要求它變）—— 恆真之反面 |
| `004`／`084`／`088`／`129`／`137`／`045` | 成立 | 兩端同物而中間事件為 key cycle／profile 切換／編輯／Valet 進出 —— 判別力在該事件 |
| **`148`** | **修正** | 見 §1.3 |
| **`154`** | **修正** | 見 §1.1 |

全 16 條之逐條理由已入 `data/pending_judgements.tsv`（AB-1 段）。

### 1.3 **`TC-148` 為第二種失效形態，下放包未點名，本輪一併修正**

`TC-148`（`046`，6.1）原 ER4：`The preferences are unchanged from those
recorded in step 1` —— 與 `TC-154` 之原形**逐字相同**。

**但它不是恆真，而是歧義**：6.1 之情境是「New Profile Setup 進行中」，
畫面上同時存在**現用 profile** 與**正在建立之 profile** 兩個候選，
而該句沒說是哪一個。

**判定：兩端皆為現用 profile 之偏好（設定前後兩時點），
其間之事件（avatar 步驟）在 base 變體上正是 CPA 會介入之處，故非恆真。**
修正為指名 `the active Driver Profile`。

**兩條之差別值得記**：同一句英文，在 6.4 是**恆真**（該比的是兩個 profile），
在 6.1 是**歧義**（該比的是同一個 profile 之兩個時點）。
**下放包點名的是前者；後者是自檢的產物。**

### 1.4 掃描已入閘與登記表

`audit_consistency.ab1_compare_ends`，四個方向性案例
（`TC-154` 之原形須列入、其修正後之形**仍列入**（本掃描不硬判）、
無比對語者不列、有比對語而無 `step` 互參者不列）。
`audit_consistency` 之方向性案例 **48 → 52**。
16 條全數入 `audit_pending` 之登記表並判定，抑制數 43 → **59**。

---

## 2. 作業 2 —— G-F：靜態轉錄之指紋

### 2.1 新閘 `scripts/stamp_static_doc.py`（5 / 5）

`--stamp` 插入指紋區塊，`--verify` 比對，**無指紋者一律判過期**。
標的之辨識同時吃 `NR1L-UserProfiles-NNN` 與 `SWE1-HMI-PROF-…`
（leaf id 映射為其 TC）—— RD 查詢單只寫 leaf id，不寫 tc_id。

| 檔 | 標記條數 | `--verify` |
|---|---|---|
| `27_rd_queries_v2.md` | 11 | 不符 0 |
| `28_provenance4.md` | 30 | 不符 0 |
| `34_provenance5.md` | 26 | 不符 0 |

### 2.2 指紋範圍取**全欄**，與 review pack 不同 —— 具名其理由

review pack 之指紋只取「pack 印出來的欄位」，因為那份文件印了什麼是明確的。
本輪三份**各印各的**（RD 單印條文與處置、出處對照印字面值）。
逐份定義範圍會產生三套判準，而**三套判準只要有一套劃錯，
那份文件就會在該欄變動時靜靜地維持「新鮮」**。

故一律取全欄：**保守之方向是安全的** ——
誤判過期只是多重出一次，誤判新鮮則是拿舊資料下判斷。**代價不對稱。**

### 2.3 `26_rd_queries.md` **不標指紋**

該檔已 `WITHDRAWN`（27 輪，三處缺陷）且**從未寄出**。

> 指紋標的是「**仍供人據以判斷**之文件」；
> 標了指紋反而會使它看起來像一份可用之現行文件。

已於其 WITHDRAWN 段內加註此處置，並指向現行版 `27_rd_queries_v2.md`。

---

## 3. 作業 3／4 —— G-G 與 G-H

**G-G**：寫入 profile **§7.5.1** —— 每輪上繳一律附現行四份 pack 之
`--verify` 結果；**若當輪有 TC 變動而致某份過期，於同輪重出，不留給下一輪**
（本輪即依此重出 `24b`）。

**G-H**：寫入 profile **§7.4** ——

> 他 feature 之先例可用，前提是**兩者用的是同一份表單母本**。
> 若其用的是別的表單，其填法不構成先例，只是參考。

並具名其所以然：欄位字母、DV 範圍與 `allowBlank` **皆隨 revision 變動**
（rev A/B 之 Q 欄尚未插入，其後各欄左移一格）。
Comfort 之 T:Z 先例成立，是因為兩者同用 `…_SWQT_20260817_ext.xlsx`（rev C）。

---

## 4. 作業 5 —— 全閘重跑

| 閘 | 自我測試 | 語料 |
|---|---|---|
| `lint_tcs.py` | **64 / 64** | 189 條，違規 0 |
| `audit_consistency.py` | **52 / 52**（＋4，AB-1）| 待判見 §5.2 |
| `audit_pending.py` | **5 / 5** | 違規 0；抑制 **59 條** |
| `audit_enums.py` | **7 / 7** | 違規 0 |
| `audit_verbs.py` | **5 / 5** | 違規 0 |
| `audit_variant_pairs.py` | **7 / 7** | 違規 0 |
| `audit_assignment.py` | **6 / 6** | 違規 0 |
| `audit_delegation.py` | **8 / 8** | 紅 0 |
| `lint_variant_labels.py` | **11 / 11** | —— |
| `lint_outbound_doc.py` | **8 / 8** | 本輪各檔違規 0 |
| `verify_dv_integrity.py` | **6 / 6** | —— |
| `build_review_pack.py` | **4 / 4** | 見 §5.1 |
| **`stamp_static_doc.py`** | **5 / 5** | 見 §2.1 |
| `write_back.py` | **10 / 10** | 未產出 |
| `build_batch_context.py` | 8 / 8 | —— |
| `render_spec_region.py` | 7 / 7 | —— |
| `scan_override_notes.py` | 與 TSV 一致 | —— |

---

## 5. 附件（G-G 之常規）

### 5.1 現行四份 review pack 之 `--verify`

```
44_review_pack_24a.md：相符 11 條，不符 0 條
45_review_pack_24b.md：相符 11 條，不符 0 條
44_review_pack_33a.md：相符 17 條，不符 0 條
44_review_pack_33b.md：相符 16 條，不符 0 條
```

**被取代者**（不得作覆核依據，已加警語）：`40_24a`／`40_24b`／`41_33a`／
`41_33b`／**`44_24b`**。

### 5.2 待判現況

**新命中 0**；抑制 59 條（AB-1 16、Q-1 13、U-1 7、V-1 18、W-1 4、Y-1 1）。

依 profile §7.1 之讀法：**「抑制 59 條」是六支掃描仍活著的證據。**

---

## 6. 現況

| 項 | 值 |
|---|---|
| TC | 189 ／ leaf 180 / 180 |
| 已覆核 | 147 / 189（餘 42）；**其中 `148`／`154` 已因本輪修正而須重讀** |
| 閘 | **17 支**（新增 `stamp_static_doc`）|
| 產出 | 無 |
| 擋交付者 | 無 |

---

## 7. 獨立判斷

1. **AB-1 之兩條，是同一句英文在兩節裡的兩種病 —— 而只有一種被點名。**
   `The preferences are unchanged from those recorded in step 1`
   在 6.4 是恆真（該比兩個 profile），在 6.1 是歧義（該比同一 profile 之兩時點）。
   **下放包從條文讀出前者；我從字串比對讀出後者。**
   這一次兩層剛好互補，但它提示一件事：
   **以「句型」為線索之自檢，抓得到同型而抓不到同因** ——
   16 條命中裡有 14 條是好的，其判別力全在「中間那個事件」，
   而那是句型看不見的。**故本掃描只能是待判，不能是紅。**

2. **G-G 在建立的當輪就證明了自己，而那是因為我自己弄壞了一份 pack。**
   若 AB-1 之修正發生在別輪，`44_24b` 會帶著兩條過時的轉錄躺到下一輪 ——
   而分析層正打算讀 `24b` 前段（餘 42 條裡有 5 條在那裡）。
   **這不是運氣好，是「附上結果」這個要求把時間差壓成了零。**
   建議把同一形式推廣到 `stamp_static_doc` 所管之三份：
   目前它們的 `--verify` 只在我方標記時跑過一次，
   **而它們不像 pack 會每輪被附上** —— 具名此缺口。

3. **17 支閘裡，有 3 支的標的是「我方自己的產出物是否過期」。**
   `audit_pending`（待判登記）、`build_review_pack --verify`（pack）、
   `stamp_static_doc --verify`（RD 單與出處對照）。
   **這個比例值得注意**：它說明本專案現在的主要風險已經不是「寫錯 TC」，
   而是**「拿舊東西下判斷」**。
   前者有 13 支閘守著且本輪全綠；後者是這三輪才開始有工具的。

4. **餘 42 條之覆核，其中 5 條在 `24b` 前段（`146`–`150`）。**
   `148` 屬該段且本輪剛改 —— **請以 `45_review_pack_24b.md` 讀**，
   `44_review_pack_24b.md` 已被本輪之 `--verify` 判過期。
