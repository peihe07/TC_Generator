# 上繳包 26 —— Vehicle Category：`064-03` 補拆 ＋ 第 18 項（T136–T141）

- 日期：2026-08-27
- 對應下放：`docs/handoff/26_batch5_close.md`
  （SHA256 `c8aec4c04829ee27646ce871d157e44d913e8adc179dd7cd092f58f0c4b1e1ef`，182 行）
- **結論：T136–T141 全數完成。第 5 批 20 → **21 筆**，收斂 **22 項**全過；六批回歸全綠。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T136 | 項號指涉檢查（第 18 項）| ✅ self-test 二斷言全過；**且回溯實測抓到那個歷史錯誤本身** |
| T137 | PLAYBOOK §7.3 台帳交叉檢 | ✅ 建議位階；已記明其無承載者 |
| T138 | R-VC26 適用說明加註 | ✅ 原文不改（R-TM13）|
| T139 | profile §7.2.1 PENDING 位置通則 | ✅ |
| T140 | `064-03` 拆 2 | ✅ `split_delta` 4 → 5，21 筆 |
| T141 | 收斂 ＋ 六批回歸 | ✅ **22 checked / 0 failed** ×6 |

**二件請你先看**：
1. **第 18 項不只通過 self-test —— 它對歷史狀態回跑，抓到的正是那張空頭支票本身。**
   見 §1.2。
2. **R-VC26 之適用說明擋掉的是一個我這一輪差點犯的錯** ——
   `057` 之三態我判不拆，理由寫的是「不互相消耗」；
   §3.1 給出的「一次性事件 vs 持續狀態」**才是那個判斷的真正依據**。見 §3。

---

## 1. T136 —— 第 18 項

### 1.1 判準

```
檢查之名稱／說明中凡出現 `第<id>項`（含範圍 `3–8` 與頓號列舉），
該 `<id>` 須存在於**本次執行之檢查清單**。不存在 → FAIL。零閾值。
```

範圍與頓號皆展開（`第 3–8、11、12 項` → 3,4,5,6,7,8,11,12）。
**只展開純數字之範圍** —— `8b` 之類帶字母者不參與範圍運算。

### 1.2 ⚠ 回溯實測 —— 它抓到的是真的那一筆

self-test 之外，另對**下放包 25 之前的真實狀態**回跑
（以現行 22 項為母體，移除第 8b 項）：

```
母體 21 項（移除 8b）→ 無主 1 處
    第8項 引用不存在之「第8b項」
```

**這不是構造的標的，是歷史上真的存在過六個包的那一筆。**
若本項當時就在，它會在下放包 10 之後的**第一次收斂**就叫出來。

### 1.3 self-test 前置（PLAYBOOK §7.1.1）

```
第 18 項 —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  (b) 已知標的 插入「見第 99 項」應 FAIL  PASS
  self-test 2  (a) 反向 現行全部名稱應全過          PASS
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     self-test 全過；掃描 21 項；引用之項號 ['11', '12', '3', '4', '5', '6', '7', '8', '8b']；無主 0 處 無
```

`(b)` 已知標的為**插入**（在某項名稱後加「見第 99 項」）、
`(a)` 反向為**現狀**。二者打的是同一支 `refcheck`，
但一個要求它出聲、一個要求它閉嘴。

### 1.4 本項之已知盲區

- **只掃檢查之名稱與說明**，不掃 `.py` 原始碼之註解。
  註解裡寫「見第 99 項」不會被抓到 —— 而第 8 項那張支票**正是寫在名稱裡**，
  故對該形態有效。
- **不驗被引之項是否真的驗了它宣稱的事** —— 那是語意判斷。
  第 8 項現在指得到第 8b 項，但「第 8b 項是否真的涵蓋他批之 PENDING」
  仍由人看。

---

## 2. T137 —— PLAYBOOK §7.3

台帳交叉檢入 §7（建議位階，非條文）。

**為什麼不是條文**：R-VC15（不可互援）與 `docs/REVISIONS.md`（這一筆已算過）
**都已存在**，而 REV-14 是在三道皆備之下發生的。
**二者都不治「寫之前會不會去翻」** —— 那是習慣，不是規則。

**已記明其無承載者**：現無腳本驗「新寫之母體敘述是否與台帳既載者相符」。
與 §7.1 之雙向實測同為紀律 —— 而 **§7.1.1 已示範紀律可以變成程式結構**，
本節暫無對應形態。記明以免誤以為 REV-14 之後同型不會再犯。

---

## 3. T138 —— R-VC26 之適用說明，擋掉的是我這輪差點犯的錯

加註（fence 外，原文不改）：一次性事件 → 拆；持續狀態 → 不拆。

**這一條對我有實際作用，不是補充說明**：

上繳包 25 §4.2 我判 `057` 之三態不拆，理由寫「三者**不互相消耗** ——
點火狀態可循環切換」。**那個理由是對的，但它是從結果反推的** ——
我當時沒有一個判準能說明「為什麼點火狀態可循環，而彈窗不行」。

§3.1 給的區分是：**標的之性質**。`057` 之標的是**持續狀態**（tab 不可用），
情境不因觀察而消耗；`064-03` 之標的是**一次性事件**（彈窗消失），
走完即消耗。**同樣是點火狀態之列舉，判決相反，而依據是標的不是列舉項。**

若無此加註，R-VC26 被讀成「凡 `or` 列舉皆拆」是很自然的 ——
本批 `057`（3 態）、`059-02`／`060-02`／`061`（各 2 態）
**四筆共會多出 5 筆 TC，而其中無一對應任何覆蓋洞**。

---

## 4. T139 —— profile §7.2.1

`PENDING` 之位置依其所影響之欄位而定（怎麼做 → Procedure／
怎麼判 → ER／前提 → Pre-Condition）；下放包之表列為預設值，
執行層依實際功能判定並記明理由者以實際功能為準。

併記**計數之母體為 TC 層而非 leaf 層**（第 8b 項即以 TC 層計），
以及**本節未機器化** —— 第 8b 項只驗樣式、DR 存在性與宣告相符，**不驗位置**。

---

## 5. T140／T141 —— `064-03` 拆 2

| 支 | 括號下半 | Procedure 之目標狀態 |
|---|---|---|
| Run | `Leaving the blocked state via Run -- …` | `Turn the vehicle to Run` |
| Key On | `Leaving the blocked state via Key On -- …` | `Turn the vehicle to Key On` |

**Key On 支自 Pre-Condition 完整重建情境**，不接續 Run 支之結果 ——
互相消耗之直接後果（下放包 25 §三）。

二筆之 `reasoning` 各載：拆分裁定之由來、互相消耗之形態、
**以及與 `057` 之界線**（一次性事件 vs 持續狀態），
並記明「R-VC26 不得被讀成凡 `or` 列舉皆拆」。

### 5.1 收斂 22 項全過

```
第 18 項 —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  (b) 已知標的 插入「見第 99 項」應 FAIL  PASS
  self-test 2  (a) 反向 現行全部名稱應全過          PASS
verify_batch — batch5_ignition_availability.json（收斂條件；下放包 10 §四 ＋ 13 §4.4）
  #  條件                                                             判
------------------------------------------------------------------------------------------------
  1  21 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                           PASS
     TC 數 21；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）                        PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）              PASS
     命中 0 處 無
  3  test_item 括號下半 21 筆兩兩不同（機械）                                    PASS
     缺括號 無；重複 無；相異 21
 3b  test_item 括號下半無中文（R-S4）                                        PASS
     含中文 無
  4  specification_reference 21 筆與 recon_leaf_to_section.tsv 逐字相符   PASS
     不符 0 筆 
  5  priority 21 筆與 priority_final.tsv 逐字相符                         PASS
     不符 0 筆 
  6  Test Set 21 筆一致，Test Group 皆為 `Vehicle Category`               PASS
     test_set=['Ignition Availability']；test_group=['Vehicle Category']
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                                 PASS
     尾句號 0；單引號 0；方括號角括號 0；空白 0
 7b  test_item 上半為來源之逐字子串（R-VC23(c)；整段，不倚樣式表）                       PASS
     取材來源分布 {'Description': 12, 'SYS1': 4}；未對上來源 0 筆 無
  8  PENDING 之分布與其字串（pilot 專屬；他批以第 8b 項驗）                           PASS
     033-01 之 PENDING 數 None；字串相符 False；他筆帶 PENDING {'SWE1-HMI-VC-061': 1, 'SWE1-HMI-VC-062-01': 1, 'SWE1-HMI-VC-062-02': 1, 'SWE1-HMI-VC-063-01': 1, 'SWE1-HMI-VC-063-02': 1}
 8b  PENDING 之樣式、DR 存在性、與 pending_scope 之宣告相符                       PASS
     實際 7 處；宣告 7 筆；DR 分布 {'DR-VC10': 7}；不符 0 處 無
  9  `028-02`／`033-01` 之括號下半明載其流程（pilot 專屬）                         PASS
     未載者 無
 10  `VC-021` 之委派（pilot 專屬；本批不適用）                                   PASS
     N/A
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 步驟無 observe/verify 起首 PASS
     步數不足 無；1:1 不符 無；ER 含 modal 無；禁用起首動詞 無
 13  該批 Test Set 全筆一致且與 framework.md §2 逐字相符                        PASS
     批內 test_set=['Ignition Availability']；framework §2 之 8 組=8 個；相符=True
 14  常數之變體擴散（正規化後相等而原字不同 → FAIL；§5.3）                               PASS
     profile 常數（展開後）3 條；變體 0 處 無
 15  母體 = leaf_scope + split_delta = 16 + 5 = 21（R-VC22(b)／IN §8.2.2） PASS
     tcs=21；leaf_scope=16；宣告 split_delta=5；實際拆分增量=5（{'SWE1-HMI-VC-058-03': 2, 'SWE1-HMI-VC-062-02': 2, 'SWE1-HMI-VC-063-02': 2, 'SWE1-HMI-VC-064-01': 2, 'SWE1-HMI-VC-064-03': 2}）；held=0（b 段不計入母體）
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）                   PASS
     適用 6 筆；不符 0 筆 無
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     PASS —— 未處置候選 0；內容不符 0；結構聲稱不符 0；離開碼 0
 18  檢查之名稱／說明所引之項號皆存在（下放包 26 §一）                                    PASS
     self-test 全過；掃描 21 項；引用之項號 ['11', '12', '3', '4', '5', '6', '7', '8', '8b']；無主 0 處 無
------------------------------------------------------------------------------------------------
22 checked / 0 failed
```

### 5.2 六批回歸

```
pilot_glovebox                     22 checked / 0 failed
batch1_category_structure          22 checked / 0 failed
batch2_settings_list               22 checked / 0 failed
batch3_controls                    22 checked / 0 failed
batch4_settings_behavior           22 checked / 0 failed
batch5_ignition_availability       22 checked / 0 failed
```

---

## 6. 進度

**117 leaf 中 112 筆已收斂，TC 累計 120 筆。**

| 剩餘 | leaf | 阻斷 |
|---|---|---|
| 第 6 批 `Brake Service` | 2 | **DR-VC3** |
| 第 7 批 `Cabrio Widget` | 1 | **DR-VC3** |
| b 段 | 3 | **DR-VC9(二)** |

**十筆 DR 全未結。生成側已無可自行推進之項目** ——
尾段 6 筆全部卡在 DR-VC3 與 DR-VC9(二)。

---

## 7. 待你裁

1. 同批 A（六項）、DR-VC3、DR-VC9(一)、DR-VC10（Tier 3）—— **五筆之發送**
2. 尾段 6 筆之處置：等 DR，或先做**出貨門檻二表**（表 A FROP 跨域、
   表 B 覆蓋落差）與工作簿寫回之前置

> §7.2 之提問理由：**生成側已經停了**，而表 A／表 B 為 R-VC3 所裁之
> 出貨門檻，其編製不倚賴那二個 DR（表 B 之**最終措辭**待 DR-VC3，
> 但其結構與 17 節之清單可先備）。若要讓這條路繼續有事做，那是下一段。

---

## 8. 量測條件揭露（R-G8）

### 第 18 項之母體

**本次執行之檢查清單**（22 項），非 `verify_batch.py` 之原始碼全文。
故只涵蓋 `chk()` 之 `name` 與 `detail` 二個字串。
`.py` 註解、profile、RULINGS 中之項號引用**皆不在母體內**。

### 回溯實測之構造

§1.2 之「移除 8b」是**自現行輸出解析後移除該列**，
非真的把第 8b 項自腳本刪除再跑。二者對 `refcheck` 而言等價
（該函式之輸入就是 `(id, name, detail)` 三元組之清單），
**但這是等價性主張，不是同一次執行** —— 記明。

### `064-03` 二支之等價性

依下放包 26 §三，Run 與 Key On 是否同一等價類**未判**，
亦不需判 —— 互相消耗之判準已足以定拆分。
**故本包未產出任何關於該二狀態語意關係之結論。**

---

## 附錄 A —— `064-03` 拆後二筆全文

### A.1 `VC-064-03`(1) — Returning to Run clears the transition pop-up

| `priority` | `design_method` | `distinguishing_axis` |
|---|---|---|
| **P1** | 狀態轉換 (State Transition Testing) | 解除之目標狀態：Run（對 Key On 支） |

**`test_item`**

```
If vehicle is turned to Run or Key On while pop-up is on screen, close pop-up and show Settings screen user was in before pop-up was triggered.
 (image: image17.png)

(Leaving the blocked state via Run -- the pop-up clears and the prior Settings screen returns)
```

**`pre_conditions`**

```
1. The Key Off transition pop-up is displayed, and the Settings screen the user was on before the transition is known
```

**`test_procedure`**

```
1. Record the Settings screen the user was on before the pop-up was triggered
2. Turn the vehicle to Run
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The Settings screen before the transition is recorded as the baseline
2. The vehicle is in Run
3. The pop-up is no longer displayed and the Settings screen recorded in step 1 is displayed
```

**`reasoning`**：**驗證目標**：車輛回到 Run 時彈窗自動關閉，並回到轉換前之 Settings 畫面。**⚠ 取材為第三處置類**：037 之 `while **pop-up** is on screen` 為**無冠詞名詞回指**；整段 s1-s3 為 **83 token，逾 R-3 之 50** → 單句 s3 ＋ `resolution=PC`／`resolution_key=pop-up`。**⚠ 本筆為第一層之偽陰性**（無冠詞名詞回指）——由勘查 (d) 發現。**ER 之 baseline（§5.6）**：「回到轉換前之畫面」須先記錄那是哪一個。**⚠ 拆 2（下放包 26 §三之裁定）**：來源作 `turned to **Run or Key On**`。上繳包 25 §4.3 我已施 R-VC26 之問法（「轉到 Key On 時彈窗不消失，哪一筆會 FAIL？」——沒有）但**未自行增筆**，因授權為 20 筆而拆分清單無本筆；分析層裁定拆，第 5 批 21 筆。**互相消耗之形態**：轉到 Run 後彈窗已消失，須整輪點火循環重建才能走 Key On。**⚠ 與 `057` 之界線（R-VC26 之適用說明，下放包 26 §3.1）**：本筆之標的為**一次性事件**（彈窗消失）故拆；`057` 之標的為**持續狀態**（tab 不可用），情境不因觀察而消耗，切換狀態即可續驗，故其三態不拆。**R-VC26 不得被讀成「凡 or 列舉皆拆」。****追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### A.2 `VC-064-03`(2) — Returning to Key On clears the transition pop-up

| `priority` | `design_method` | `distinguishing_axis` |
|---|---|---|
| **P1** | 狀態轉換 (State Transition Testing) | 解除之目標狀態：Key On（對 Run 支） |

**`test_item`**

```
If vehicle is turned to Run or Key On while pop-up is on screen, close pop-up and show Settings screen user was in before pop-up was triggered.
 (image: image17.png)

(Leaving the blocked state via Key On -- the pop-up clears and the prior Settings screen returns)
```

**`pre_conditions`**

```
1. The Key Off transition pop-up is displayed, and the Settings screen the user was on before the transition is known
```

**`test_procedure`**

```
1. Record the Settings screen the user was on before the pop-up was triggered
2. Turn the vehicle to Key On
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The Settings screen before the transition is recorded as the baseline
2. The vehicle is in Key On
3. The pop-up is no longer displayed and the Settings screen recorded in step 1 is displayed
```

**`reasoning`**：**驗證目標**：車輛回到 Key On 時彈窗自動關閉，並回到轉換前之 Settings 畫面。**取材同 Run 支**（第三處置類，單句 s3，`resolution=PC`／`pop-up`）。**本筆即下放包 26 §三所補之覆蓋洞** —— 拆前「轉到 Key On 時彈窗不消失」無任何一筆會 FAIL。**Procedure 自 Pre-Condition 完整重建情境**：本支不接續 Run 支之結果，其彈窗須重新觸發（互相消耗之直接後果，下放包 25 §三）。**等價性不需另判**（下放包 26 §三）：Run 與 Key On 是否同一等價類，不改互相消耗之判準所定之拆分結論。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

---

> 第 5 批 21 筆。收斂 22 項全過，六批回歸全綠。
> 未寫回工作簿、未進行任何 git 操作。
