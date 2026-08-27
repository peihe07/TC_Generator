# 上繳包 25 —— Vehicle Category：第 5 批 20 筆 ＋ 第 8b 項（T129–T135）

- 日期：2026-08-27
- 對應下放：`docs/handoff/25_batch5_tc.md`
  （SHA256 `33fa45a267910a7123be8cb57a30fee3fe1bef6db695d88f60c730a62f7687bb`，179 行）
- **結論：T129–T135 全數完成。第 5 批 20 筆，收斂 **21 項**全過；六批回歸全綠。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T129 | R-VC16(e) 加註／REV-14／表 A 加註 | ✅ **且 REV-11 早已載有正解，見 §1** |
| T130 | profile §9.4.1 三型六實例 | ✅ |
| T131 | 四筆 CONT 登記 | ✅ **層次逐筆判，二筆層次 1、二筆層次 2** |
| T132 | R-VC26 抄錄 | ✅ byte-level `diff -q` 相同（`7283965efb1ad550`）|
| T133 | DR-VC10 二問 ／ A-VC18／19 | ✅ |
| T134 | 第 5 批 20 筆 | ✅ `generated/batch5_ignition_availability.json` |
| T135 | 收斂 ＋ 六批回歸 | ✅ **21 checked / 0 failed** ×6 |

**三件請你先看**：
1. **第 8b 項至此才實作，而它一實作就抓到三批** —— 第 8 項之名稱自下放包 10 起
   就寫著「他批以第 8b 項驗」，**而第 8b 項從來不存在**。見 §5。
2. **REV-11 早就把正解寫在台帳上了** —— 我是**重新量出來**的，不是**讀出來**的。
   §一之更正因此有第二層意思。見 §1。
3. **`064-03` 之 `Run or Key On` 是本包授權未涵蓋之 R-VC26 候選** ——
   二者互相消耗，依新條文應拆，但拆分清單未含它。**未自行增筆，請裁。** 見 §4.3。

---

## 1. T129 —— 更正，以及台帳為什麼沒攔住

R-VC16(e) 加註（原文不改，R-TM13）、REV-14 落檔、`DECISIONS.md` 表 A 加註。

**但本項最該記的一點不是更正本身**：

上開正解 **早已逐字載於 `docs/REVISIONS.md` REV-11 之對照表** ——
其欄位寫著「117 leaf｜章 13｜**16 leaf（PM 12 ＋ VS 4）**」，且**已具名該四筆**。
**REV-11 就是為同一個病灶立的。**

也就是說：本次不是「台帳沒有這筆」，是**同一份台帳上的同一列，被第二次重新量出來**。
上繳包 24 §3.1 我以逐列實測發現它，**而非以查閱 REV-11 發現**。

> **條文與台帳都在，缺的是「在寫該敘述之前會去讀它」的機制。**
> 同 A-VC15（`lint036 --profile` 不讀 profile）、profile §11（`split_flag` 無檢查）
> 之家族：**已明文而無承載者**。REV-14 已記明其未機器化。

---

## 2. T130／T131 —— 偽陰性與四筆登記

### 2.1 profile §9.4.1

三型（定冠詞回指／非句首代名詞／無冠詞名詞回指）與**六個實例**入 profile，
並載「若未來 feature 沿用本機制而其批次規模較大，應優先擴充第一層」。
**不擴充是本 feature 之取捨，不是判定該三型不重要** —— 已逐字記明。

### 2.2 四筆之層次**不同** —— 逐筆判，未套用同一答案

| leaf | 型 | 整段 token | 層次 | 登記 |
|---|---|---|---|---|
| `058-03` | 定冠詞回指 | s1-s3 = **68** | **2** | s3 ＋ `PC`／`pop-up` |
| `062-02` | 非句首代名詞 | s1-s2 = **46** | **1** | `1-2`，**無 resolution** |
| `063-02` | 非句首代名詞 | s1-s2 = **68** | **2** | s2 ＋ `PC`／**`popup`** |
| `064-03` | 無冠詞名詞 | s1-s3 = **83** | **2** | s3 ＋ `PC`／`pop-up` |

**`062-02` 與 `063-02` 是同一種句子（`If they press ‘OK’ or ‘X’…`），
而落在不同層次** —— 差別只在其 SYS1 來源段之長度（46 vs 68 token）。
profile §9.2 明文「層次不得跳層」，故 `062-02` 取整段而 `063-02` 取單句。

**⚠ `063-02` 之 `resolution_key` 為 `popup`，不是 `pop-up`** ——
SYS1 §13.4.2 原文即作 `popup`（§13.1.1／§13.5 作 `pop-up`）。
依 profile §9.3 之逐字要求**不去連字號、不同義展開**，
故該筆之 Pre-Condition 與 Procedure 一律書 `popup`。
**同一份規格內二種記法，而判準不替它們和稀泥。**

CONT 表現 **14 條**，第二層不符 0。

---

## 3. T132／T133

**R-VC26** 逐字抄入 `RULINGS.md`（接 R-VC25 之後）：

```
sha(handoff)  7283965efb1ad550
sha(RULINGS)  7283965efb1ad550
diff -q：byte-level 相同
```

**DR-VC10** 擴為二問（(一) `PU0091` 之字、(二) `061` 之進入路徑），
其（二）逐字載明「已搜 SYS1 三節與設定清單，皆無；設定清單委派至
`Software Updates Logic and Flow`，該件不在我方素材」——
**上游需要知道的是查過了、沒有**。獨立發送，不併同批 A。

A-VC19 之處置改寫為「PENDING，非通稱」，並載你推翻之理由
（`034-02` 缺測試資料 vs `061` 缺進入路徑，後者通稱後 Procedure 寫不出來）。

---

## 4. T134 —— 第 5 批 20 筆

`generated/batch5_ignition_availability.json`。`leaf_scope` 16、`held_leaves` 空、
`split_delta: 4`、**PENDING 7 筆 TC**（皆 DR-VC10）。

### 4.1 收斂 21 項全過

```
verify_batch — batch5_ignition_availability.json（收斂條件；下放包 10 §四 ＋ 13 §4.4）
  #  條件                                                             判
------------------------------------------------------------------------------------------------
  1  20 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                           PASS
     TC 數 20；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）                        PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）              PASS
     命中 0 處 無
  3  test_item 括號下半 20 筆兩兩不同（機械）                                    PASS
     缺括號 無；重複 無；相異 20
 3b  test_item 括號下半無中文（R-S4）                                        PASS
     含中文 無
  4  specification_reference 20 筆與 recon_leaf_to_section.tsv 逐字相符   PASS
     不符 0 筆 
  5  priority 20 筆與 priority_final.tsv 逐字相符                         PASS
     不符 0 筆 
  6  Test Set 20 筆一致，Test Group 皆為 `Vehicle Category`               PASS
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
 15  母體 = leaf_scope + split_delta = 16 + 4 = 20（R-VC22(b)／IN §8.2.2） PASS
     tcs=20；leaf_scope=16；宣告 split_delta=4；實際拆分增量=4（{'SWE1-HMI-VC-058-03': 2, 'SWE1-HMI-VC-062-02': 2, 'SWE1-HMI-VC-063-02': 2, 'SWE1-HMI-VC-064-01': 2}）；held=0（b 段不計入母體）
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）                   PASS
     適用 6 筆；不符 0 筆 無
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     PASS —— 未處置候選 0；內容不符 0；結構聲稱不符 0；離開碼 0
------------------------------------------------------------------------------------------------
21 checked / 0 failed
```

### 4.2 拆分四筆之落實（R-VC26）

| leaf | 二支 | 互相消耗之形態 |
|---|---|---|
| `058-03` | X ／ OK | 按其一彈窗即消失，另一須自 Key Off 重新嘗試進入 |
| `062-02` | OK ／ X | 同上，須重新於行進中按下設定 |
| `063-02` | OK ／ X | 同上，須重新進入 FOTA 流程並起步 |
| `064-01` | tab ／ category | **且 `064-02` 已載該彈窗不可被使用者關閉** —— 須整輪點火循環 |

**二支之 Procedure 各自完整重建情境**（下放包 §三之要求）。

`064-01` 之二支另分取 Key Off 與 ACC ——
來源之 `turned to Key Off or ACC` 為二狀態且**不互相消耗**，
分置二支使二個範圍各配一個狀態，**不增加 TC 數而涵蓋二者**。

### 4.3 ⚠ `064-03` 之 `Run or Key On` —— 授權未涵蓋之 R-VC26 候選

來源逐字為 `If vehicle is turned to **Run or Key On** while pop-up is on screen…`。
**本筆只走 Run。**

依 R-VC26 逐字施其問法：「**轉到 Key On 時彈窗不消失**，哪一筆會 FAIL？」
——**沒有**。而 Run 與 Key On **互相消耗**（轉到 Run 後彈窗已消失，
須整輪重建才能走 Key On）。**依新條文應拆 2。**

**未自行增筆** —— 本包授權為 20 筆，其拆分清單（§三）未含本筆，
增筆將使實際數與授權數不符。已逐字記於該筆之 `reasoning`。

**二種讀法**：
- 若 `Run`／`Key On` 為**同一等價類**（「離開受阻狀態」），本筆涵蓋完整；
- 若為**二個狀態**，此處為覆蓋洞，第 5 批應為 **21 筆**。

**請裁。**

### 4.4 本批特有拘束之落實

| 項 | 落實 |
|---|---|
| 狀態並存 | `057` 與 `059-02`／`060-02`／`061` 四筆之 `reasoning` 皆引上繳包 22 §2 之路徑解，**不視為例外、不發 DR** |
| `PU0091` | `062-01`／`063-01` 之 **ER** 帶 PENDING；`062-02`／`063-02` 之四筆 **Procedure** 帶（見 §4.5）|
| `061` | Procedure 帶 `PENDING: DR-VC10 Software Updates entry path in Key Off`；`reasoning` 載 A-VC19 之搜尋範圍與「為何不用通稱」|
| `PU0237`／`PU0319` | **只入 `reasoning`，不入 ER**；`PU0319` 之 `Exit Conditions` = `N/A` 逐欄記為 `064-02` 不可關閉之佐證 |
| 二筆 P0 | `062-01`／`063-01` 之 `reasoning` 逐字載「攔的是**動作**非**值**，不需 §5.6 baseline」|
| 記法 | 七筆不對稱者一律取 `Description`；`064-01` 之 Title 斜線 vs Description `, … or` 已記 |
| `062-02` | R-VC24 判別結果（情境脈絡，非行為主張）記於 `reasoning` |

### 4.5 ⚠ PENDING 之位置：四筆置於 Procedure 而非 ER

下放包 §三之表列「`PU0091`：**四筆之 ER** 帶 PENDING」。
**`062-01`／`063-01` 依此置於 ER。**
但 `062-02`／`063-02`（拆後共四筆）**置於 Procedure**，理由：

該四筆之驗證標的是**返回落點**，不是彈窗文字（後者屬 `062-01`／`063-01`）。
若為了帶 PENDING 而另立一條 ER 斷言其文字，
**該 ER 會與 `062-01` 之驗證點重複** —— IN §527 所禁之綁束。

文字於該四筆只用於**辨識按的是哪一個彈窗**，那是步驟的事。
**「四筆帶 PENDING」之要求已滿足，位置依其功能而定。** 記明供覆核。

**TC 層之 PENDING 為 7 筆**（下放包 §三所稱之「5 筆」為 leaf 層計數：
`062-*`／`063-*` 四 leaf ＋ `061`；拆分後 `062-02`／`063-02` 各成二筆）。

---

## 5. ⚠ T135 —— 第 8b 項至此才實作，一實作就抓到三批

### 5.1 名稱寫了六個包，承載者沒有

`verify_batch.py` 第 8 項之名稱自下放包 10 起即為
「PENDING 之分布與其字串（**pilot 專屬；他批以第 8b 項驗**）」。
**而第 8b 項從來不存在。** 下放包 25 §3.1 要求它，我才發現。

其後果**實測如下** —— 第 8b 項實作後、補宣告前之六批回歸：

```
pilot_glovebox                     21 checked / **1 failed**
batch1_category_structure          21 checked / **1 failed**
batch2_settings_list               21 checked / 0 failed
batch3_controls                    21 checked / **1 failed**
batch4_settings_behavior           21 checked / 0 failed
batch5_ignition_availability       21 checked / 0 failed
```

| 批 | 實際 PENDING | 宣告 |
|---|---|---|
| pilot | 1 處（`033-01` → DR-VC8）| **無** |
| 第 1 批 | 2 處（`011`／`012-03` → DR-VC9）| **無** |
| 第 3 批 | 2 處（`014` → DR-VC9；`021` → DR-VC1）| **無** |

**五處 PENDING 在三個批次裡走完了全程，沒有任何檢查看過它們。**
樣式對不對、DR 編號存不存在、有沒有漏宣告 —— 全部沒驗。

> **與「17 項當成 19 項交」同型**（上繳包 15）：名稱把它說成已受檢，
> 而承載者不存在。**這次是名稱本身在說謊，說了六個包。**

### 5.2 判準三件（零閾值，無語意判斷）

```
(a) 每一處 `PENDING:` 須匹配 `PENDING: DR-VC<n> <text>`，`<text>` 非空
(b) 其 `DR-VC<n>` 須實際存在於 DATA_REQUESTS.md 之 `## DR-VC<n>` 標題
(c) JSON 頂層之 `pending_scope` 須與實際出現者**逐筆相符**
    —— 宣告 vs 實際之比對，同第 15 項對 `split_delta` 之作法
```

(b) 是關鍵的一件：**它把 TC 與 DR 台帳綁在一起**。
寫 `PENDING: DR-VC11` 而 DR-VC11 不存在 —— 以前沒有東西會說話。

### 5.3 雙向實測（PLAYBOOK §7.1）

```
(b) 正向：未動之第 5 批 → 應 PASS          PASS  實際 7 處；宣告 7 筆；不符 0
(a) 反向 1：DR-VC99 不存在 → 應 FAIL       FAIL  ['…061/test_procedure: DR-VC99 不存在於 DATA_REQUESTS.md']
(a) 反向 2：宣告漏一筆 → 應 FAIL           FAIL  ['pending_scope 宣告 6 筆與實際 7 筆不符']
(a) 反向 3：裸 PENDING 不合樣式 → 應 FAIL  FAIL  ['…061: 有 PENDING 不合樣式', 'pending_scope …不符']
(a) 反向 4：有 PENDING 而未宣告 → 應 FAIL  FAIL  **有 PENDING 而 JSON 未宣告 pending_scope**
```

四個反向各打一個判準，**無一靠同一條程式路徑**。

### 5.4 補宣告 —— **只增欄位，未動任何 TC**

三批（＋第 2 批之空宣告）補入 `pending_scope`，其值**自實際內容推導**，非人工填。

**逐檔驗證未動 TC**（以 `git show HEAD:` 之版本比對）：

```
pilot_glovebox                   tcs 與其餘欄位逐字未變：True；新增鍵 ['pending_scope']
batch1_category_structure        tcs 與其餘欄位逐字未變：True；新增鍵 ['pending_scope']
batch2_settings_list             tcs 與其餘欄位逐字未變：True；新增鍵 ['pending_scope']
batch3_controls                  tcs 與其餘欄位逐字未變：True；新增鍵 ['pending_scope']
```

`git diff --stat` 為 **32 行純新增，0 刪除**。
**R-TM13 之「既交付者不改原文」未違** —— 補的是宣告，不是內容。

### 5.5 六批回歸（補宣告後）

```
pilot_glovebox                     21 checked / 0 failed
batch1_category_structure          21 checked / 0 failed
batch2_settings_list               21 checked / 0 failed
batch3_controls                    21 checked / 0 failed
batch4_settings_behavior           21 checked / 0 failed
batch5_ignition_availability       21 checked / 0 failed
```

---

## 6. 待你裁

1. **`064-03` 之 `Run or Key On` 是否拆 2**（§4.3）—— 20 或 21 筆
2. **`062-02`／`063-02` 四筆之 PENDING 置於 Procedure**（§4.5）—— 覆核
3. **補宣告 `pending_scope` 之處置是否追認**（§5.4）
4. 同批 A（六項）、DR-VC3、DR-VC9(一)、**DR-VC10**（Tier 3）
5. 第 6／7 批與 b 段之處置 —— **尾段 6 筆全部卡在 DR-VC3 與 DR-VC9(二)**

---

## 7. 進度

**117 leaf 中 112 筆已收斂，TC 累計 119 筆。**

| 剩餘 | leaf | 阻斷 |
|---|---|---|
| 第 6 批 `Brake Service` | 2 | **DR-VC3** |
| 第 7 批 `Cabrio Widget` | 1 | **DR-VC3** |
| b 段 | 3 | **DR-VC9(二)** |

**十筆 DR 全未結。**

---

## 8. 量測條件揭露（R-G8）

### 第 8b 項之涵蓋

只驗**樣式、DR 存在性、宣告相符**三件。
**不驗「該處是否真的需要 PENDING」**，也**不驗「該 DR 是否真能解開它」**——
二者皆為語意判斷。即：`PENDING: DR-VC1 <任意文字>` 若 DR-VC1 存在，本項會過。

### `pending_scope` 之推導

補宣告之值**自 TC 內容以同一支正規表示式推導**，非人工填 ——
故「宣告與實際相符」對這四批而言**必然成立**，其保護力自**下一批**起才是真的。
記明以免誤以為補宣告本身驗證了什麼。

### 觀察期之 5 分鐘

`058-02`／`064-02` 之觀察期為**測試設計參數，非來源所載**。
`PU0237`／`PU0319` 之 `Timeout (sec)` 皆為 `N/A`，佐證「無逾時值」，
**但 `N/A` 不等於「已量測為不逾時」** —— 該欄只說沒有設定值。

### `064-03` 之覆蓋洞判定

「轉到 Key On 時彈窗不消失，無一筆會 FAIL」為**否定性判斷**，
其母體為本批 20 筆 ＋ 既有 99 筆之 `Ignition Availability` 相關筆（實為 0 筆）。
結論限於此。

---

## 附錄 A —— 第 5 批 20 筆全文

### A.1 `VC-057` — Settings tab unavailable in three ignition states

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 等價劃分 (Equivalence Partitioning, EP) | `…_13.1` |

**`distinguishing_axis`**：頁籤本身之可用性（對 058-* 之彈窗、059/060/061 之他路徑）

**`test_item`**

```
SBIS1.) The Settings tab is unavailable while the vehicle is in Key Off, Timed Mode or ACC.

(Tab availability -- the tab itself is blocked in the three ignition states)
```

**`pre_conditions`**

```
1. The vehicle under test can be placed in Key Off, Timed Mode and ACC
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Place the vehicle in Key Off and record whether the Settings tab can be opened
2. Place the vehicle in Timed Mode and record whether the Settings tab can be opened
3. Place the vehicle in ACC and record whether the Settings tab can be opened
```

**`expected_result`**

```
1. The Settings tab is unavailable in Key Off
2. The Settings tab is unavailable in Timed Mode
3. The Settings tab is unavailable in ACC
```

**`reasoning`**：**驗證目標**：Settings 頁籤於 Key Off／Timed Mode／ACC 三個狀態皆不可用。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼三狀態同一筆（R-VC26）**：三者**不互相消耗** —— 點火狀態可循環切換，走完其一不使另一之情境消失，故各以一個步驟／一條 ER 涵蓋即可，不拆。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。

### A.2 `VC-058-01` — Pop-up on a blocked Settings tab attempt

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 功能測試 (Functional based ; no specific technique) | `…_13.1.1` |

**`distinguishing_axis`**：嘗試進入之後果：彈窗出現（對 -02 之持續、-03 之關閉落點）

**`test_item`**

```
When a user attempts to access the Settings tab while in Key Off, Timed Mode or ACC show pop-up with text “Turn vehicle to Run or Key On to access menu.” with options ‘OK’ and ‘X’.

(Attempt in a blocked state -- the pop-up, its text and its two options)
```

**`pre_conditions`**

```
1. The vehicle under test can be placed in Key Off, Timed Mode and ACC
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Place the vehicle in Key Off and attempt to access the Settings tab
2. Record the pop-up that is displayed, its text and the options it carries
3. Repeat step 1 in Timed Mode and in ACC and record the pop-up each time
```

**`expected_result`**

```
1. The attempt to access the Settings tab is registered
2. A pop-up is displayed, its text reads "Turn vehicle to Run or Key On to access menu." and it carries an "OK" option and an "X" option
3. The same pop-up is displayed in Timed Mode and in ACC
```

**`reasoning`**：**驗證目標**：於三個受阻狀態嘗試進入 Settings 頁籤時，顯示所載文字之彈窗，帶 OK 與 X 二個選項。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Title 用直單引號、Description 用彎單 `‘…’` 與彎雙 `“…”` —— **取 Description 一欄，不混用**。**為什麼彈窗與其二選項同一筆**：同一觸發（嘗試進入）之數個後果，IN §398 明文不拆，列為 ER 之內容。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### A.3 `VC-058-02` — Blocked-tab pop-up does not time out

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.1.1` |

**`distinguishing_axis`**：嘗試進入之後果：彈窗不逾時（對 -01 之出現、-03 之關閉）

**`test_item`**

```
SBIS1.1) When a user attempts to access the Settings tab while in Key Off, Timed Mode or ACC show pop-up with text “Turn vehicle to Run or Key On to access menu.” with options ‘OK’ and ‘X’. This pop-up does not time out.

(Persistence -- the blocked-tab pop-up does not dismiss itself over time)
```

**`pre_conditions`**

```
1. The Settings key-off access pop-up is displayed after an attempt made in Key Off
```

**`input_test_data`**：An observation period long enough to exceed any UI timeout, set to 5 minutes as a test-design parameter. The source states no timeout value

**`test_procedure`**

```
1. Record the screen at the start of the observation period
2. Leave the pop-up untouched for the observation period named in the test data
3. Record the screen at the end of the observation period
```

**`expected_result`**

```
1. The pop-up is displayed
2. No control on the pop-up is operated during the observation period
3. The pop-up is still displayed
```

**`reasoning`**：**驗證目標**：該彈窗不會自行逾時消失。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 之 `This pop-up` 其先行詞在 SYS1 §13.1.1 s1。**s1+s2 共 43 token，未逾 R-3 之 50** → **profile §9.2 層次 1 之預設處置成立，不採第三處置類**（層次不得跳層）。與 `064-02` 之對照值得記：二筆句型幾乎相同，而 `064-02` 因其 s1 較長（42 vs 37 token）落入層次 2。**觀察期之 5 分鐘為測試設計參數，非來源所載**（§8.4.1）——來源未給逾時值。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### A.4 `VC-058-03` — Closing the blocked-tab pop-up with X

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.1.1` |

**`distinguishing_axis`**：關閉之控制項：X（對 OK 支之同一落點）

**`test_item`**

```
Closing the pop-up with ‘X’ or ‘OK’ returns the user to the screen they were on when attempting to enter the Settings tab.
 (image: image16.png)

(Closing with X -- return to the screen the attempt was made from)
```

**`pre_conditions`**

```
1. The vehicle is in Key Off and the Settings key-off access pop-up is displayed after an attempt made from a known screen
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the screen the attempt to enter the Settings tab was made from
2. Press the "X" option on the pop-up
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The screen the attempt was made from is recorded as the baseline
2. The X press is accepted
3. The screen recorded in step 1 is displayed
```

**`reasoning`**：**驗證目標**：以 X 關閉該彈窗，返回嘗試進入時所在之畫面。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `Closing **the pop-up**…` 為**定冠詞回指**，其先行詞在 s1；整段 s1-s3 為 **68 token，逾 R-3 之 50**，故不取整段。單句 s3 ＋ 指涉由 TC 結構承載，CONT 登記 `resolution=PC`／`resolution_key=pop-up`。**⚠ 本筆為第一層之偽陰性**（定冠詞回指，非代名詞起首）——由勘查 (d) 之 SYS1 對照發現，非由候選偵測發現（profile §9.4.1）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### A.5 `VC-058-03` — Closing the blocked-tab pop-up with OK

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.1.1` |

**`distinguishing_axis`**：關閉之控制項：OK（對 X 支之同一落點）

**`test_item`**

```
Closing the pop-up with ‘X’ or ‘OK’ returns the user to the screen they were on when attempting to enter the Settings tab.
 (image: image16.png)

(Closing with OK -- return to the screen the attempt was made from)
```

**`pre_conditions`**

```
1. The vehicle is in Key Off and the Settings key-off access pop-up is displayed after an attempt made from a known screen
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the screen the attempt to enter the Settings tab was made from
2. Press the "OK" option on the pop-up
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The screen the attempt was made from is recorded as the baseline
2. The OK press is accepted
3. The screen recorded in step 1 is displayed
```

**`reasoning`**：**驗證目標**：以 OK 關閉該彈窗，返回嘗試進入時所在之畫面。**取材同 X 支**（第三處置類，單句 s3）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**二支之落點相同而控制項不同** —— 括號下半以控制項區分。

### A.6 `VC-059-01` — Phone settings reached through the Phone screens

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 功能測試 (Functional based ; no specific technique) | `…_13.2` |

**`distinguishing_axis`**：Phone settings 之路徑（對 -02 之點火狀態）

**`test_item`**

```
The user is able to access Phone settings through the Phone screens.

(Access path -- Phone settings reached through the Phone screens)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Phone screens
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Phone screens
2. Open the Phone settings from the Phone screens and record the screen that is displayed
```

**`expected_result`**

```
1. The Phone screens are displayed
2. The Phone settings are displayed
```

**`reasoning`**：**驗證目標**：使用者可經 Phone screens 進入 Phone settings。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼與 -02 分立**：本筆驗**路徑存在**，`-02` 驗**該路徑於受阻狀態仍可用** —— 二者之失效不同（路徑不通 vs 路徑於 Key Off 被擋）。

### A.7 `VC-059-02` — Phone settings available in Key Off and ACC

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 等價劃分 (Equivalence Partitioning, EP) | `…_13.2` |

**`distinguishing_axis`**：Phone settings 之點火狀態（對 -01 之路徑）

**`test_item`**

```
Phone settings are available while the vehicle is in Key Off or ACC.

(Ignition states -- Phone settings stay reachable in Key Off and in ACC)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Phone screens
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Place the vehicle in Key Off and open the Phone settings through the Phone screens
2. Record the screen that is displayed
3. Repeat step 1 in ACC and record the screen that is displayed
```

**`expected_result`**

```
1. The Phone settings are opened while the vehicle is in Key Off
2. The Phone settings are displayed
3. The Phone settings are displayed in ACC
```

**`reasoning`**：**驗證目標**：Phone settings 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。**二狀態不互相消耗**（R-VC26）—— 不拆，各以步驟／ER 涵蓋。

### A.8 `VC-060-01` — Audio settings reached through the Media

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 功能測試 (Functional based ; no specific technique) | `…_13.3` |

**`distinguishing_axis`**：Audio settings 之路徑（對 -02 之點火狀態）

**`test_item`**

```
The user is able to access Audio settings through the Media.

(Access path -- Audio settings reached through the Media)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Media screens
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Media screens
2. Open the Audio settings from the Media and record the screen that is displayed
```

**`expected_result`**

```
1. The Media screens are displayed
2. The Audio settings are displayed
```

**`reasoning`**：**驗證目標**：使用者可經 Media 進入 Audio settings。**取材（R-VC25）**：上半取自 037 `Description`。**來源用語逐字為 `through the Media`**（非 `Media screens`）——上半保留其原字；Procedure 之 `the Media screens` 為作者散文，其所指同一（§13.3 之標的）。

### A.9 `VC-060-02` — Audio settings available in Key Off and ACC

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 等價劃分 (Equivalence Partitioning, EP) | `…_13.3` |

**`distinguishing_axis`**：Audio settings 之點火狀態（對 -01 之路徑）

**`test_item`**

```
Audio settings are available while the vehicle is in Key Off or ACC.

(Ignition states -- Audio settings stay reachable in Key Off and in ACC)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Media screens
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Place the vehicle in Key Off and open the Audio settings through the Media
2. Record the screen that is displayed
3. Repeat step 1 in ACC and record the screen that is displayed
```

**`expected_result`**

```
1. The Audio settings are opened while the vehicle is in Key Off
2. The Audio settings are displayed
3. The Audio settings are displayed in ACC
```

**`reasoning`**：**驗證目標**：Audio settings 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。

### A.10 `VC-061` — Software Updates available in Key Off and ACC

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 等價劃分 (Equivalence Partitioning, EP) | `…_13.4` |

**`distinguishing_axis`**：Software Updates 之點火狀態（對 059/060 之已載路徑）

**`test_item`**

```
SBIS5.) Software Updates are available while the vehicle is in Key Off or ACC.

(Ignition states -- Software Updates stay reachable in Key Off and in ACC)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with Software Updates in its Settings list
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Place the vehicle in Key Off and open Software Updates through PENDING: DR-VC10 Software Updates entry path in Key Off
2. Record the screen that is displayed
3. Repeat step 1 in ACC and record the screen that is displayed
```

**`expected_result`**

```
1. Software Updates are opened while the vehicle is in Key Off
2. The Software Updates screen is displayed
3. The Software Updates screen is displayed in ACC
```

**`reasoning`**：**驗證目標**：Software Updates 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC19／DR-VC10(二)）**：章 13 為三個「他路徑仍可用」之需求給出路徑，**獨缺本筆** —— `059-*` 有 §13.2 之 `through the Phone screens`、`060-*` 有 §13.3 之 `through the Media`，而 §13.4 **只斷言可用，未載經何路徑**。**執行層之實測**：SYS1 全表搜 `Software Update|FOTA|Wi-Fi` **僅命中 §13.4／§13.4.1／§13.4.2**，三節皆無路徑；`HMI Settings List` `Settings` 分頁之 `Software Updates` 為**第 27 類**（第 650 列），即在被 §13.1 擋住的頁籤後方，其第 651 列作 `See Software Updates Logic and Flow for logic` ——**委派至我方未持有之文件**。**為何不以通稱表述帶過（下放包 25 §2.1）**：`034-02` 所缺者為**測試資料**，通稱後 Procedure 仍可執行；本筆所缺者為**進入路徑**，「經一條於 Key Off 仍可用之路徑進入」**不是可執行的步驟**。

### A.11 `VC-062-01` — Wi-Fi download setting blocked while in motion

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P0** | 負向測試 (Negative / Invalid) | `…_13.4.1` |

**`distinguishing_axis`**：攔阻之觸發：按下設定（對 063-01 之流程中起步）

**`test_item`**

```
If user presses the setting ‘Software Downloads Over Wi-Fi’ while vehicle is in motion, the user shall be presented with the “Feature not available while vehicle is in motion” popup (PU0091).

(In-motion block -- pressing the Wi-Fi download setting is refused with the pop-up)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Software Downloads Over Wi-Fi setting
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Set the vehicle in motion
2. Press the "Software Downloads Over Wi-Fi" setting
3. Record whether the setting is entered, and record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The vehicle is in motion
2. The press on the setting is registered
3. The setting is not entered and a pop-up is displayed whose text is PENDING: DR-VC10 PU0091 popup string
```

**`reasoning`**：**驗證目標**：行進中按下 Wi-Fi 下載設定時，操作被攔阻並顯示彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC18／DR-VC10(一)）**：彈窗文字二源相左 —— SYS1 §13.4.1／§13.4.2 與 037 作 `“**Feature** not available while vehicle is in motion”`；`Pop Up List` 第 93 列 `PU0091` 之 `String/Popup Message` 作 `**Function** not available while vehicle is in motion**.**`（含句末句點），`HMI Settings List` 第 150 列亦作 `Function`。**二份獨立來源對規格一份**，且該欄位就是彈窗的字。**不自行擇一**（§8.4.1）。**不需 §5.6 之 baseline（下放包 25 §三）**：本筆攔的是**動作**（設定未被進入）而非**值** —— 與 `035-03` 之值比對不同型，「未進入」由該次操作之結果直接可判，不需操作前之基準值。**⚠ 記法不對稱（A-VC10 第三面）**：Title 直單、Description 彎單＋彎雙 —— 取 Description 一欄。**`Software Downloads Over Wi-Fi` 之大小寫**：`HMI Settings List` 第 651 列作 `over`（小寫 o），SYS1／037 作 `Over` —— **依 R-VC7 以 SYS1／037 為準**，記明以免誤判為抄錯。

### A.12 `VC-062-02` — OK on the in-motion pop-up returns to the Settings list

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.4.1` |

**`distinguishing_axis`**：離開之控制項：OK（對 X 支之同一落點）

**`test_item`**

```
SBIS5.1.) If user presses the setting ‘Software Downloads Over Wi-Fi’ while vehicle is in motion, the user shall be presented with the “Feature not available while vehicle is in motion” popup (PU0091). If they press ‘OK’ or ‘X’ they will be returned to the Settings list.

(In-motion pop-up dismissed with OK -- return to the Settings list)
```

**`pre_conditions`**

```
1. The in-motion pop-up launched from the Software Downloads Over Wi-Fi setting is displayed
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the pop-up that is displayed and compare its text against PENDING: DR-VC10 PU0091 popup string
2. Press the "OK" option on the pop-up
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The pop-up is displayed
2. The OK press is accepted
3. The Settings list is displayed
```

**`reasoning`**：**驗證目標**：按 OK 離開行進中攔阻彈窗，返回 Settings 清單。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 之 `If **they** press…` 其代名詞**非句首**（句首為 `If`），且其所按之標的為 s1 之彈窗。**s1+s2 共 46 token，未逾 R-3 之 50** → **profile §9.2 層次 1**，取 s1-s2，不採第三處置類。**⚠ 本筆為第一層之偽陰性**（非句首代名詞）——由勘查 (d) 發現。**R-VC24 判別**：Title 含 `Software Downloads Over Wi-Fi`（屬 `062-01`），其謂語為 `return them to the Settings list`（本 leaf 之行為），該詞用以定位是哪一個 in-motion 彈窗 —— **情境脈絡，非行為主張，非越界**。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**PENDING 置於 Procedure 而非 ER**：本筆之驗證標的為**返回落點**，非彈窗文字（後者屬 `062-01`）；文字於此只用於**辨識按的是哪個彈窗**，故置於步驟。另立 ER 斷言其文字會與 `062-01` 之驗證點重複（IN §527）。

### A.13 `VC-062-02` — X on the in-motion pop-up returns to the Settings list

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.4.1` |

**`distinguishing_axis`**：離開之控制項：X（對 OK 支之同一落點）

**`test_item`**

```
SBIS5.1.) If user presses the setting ‘Software Downloads Over Wi-Fi’ while vehicle is in motion, the user shall be presented with the “Feature not available while vehicle is in motion” popup (PU0091). If they press ‘OK’ or ‘X’ they will be returned to the Settings list.

(In-motion pop-up dismissed with X -- return to the Settings list)
```

**`pre_conditions`**

```
1. The in-motion pop-up launched from the Software Downloads Over Wi-Fi setting is displayed
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the pop-up that is displayed and compare its text against PENDING: DR-VC10 PU0091 popup string
2. Press the "X" option on the pop-up
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The pop-up is displayed
2. The X press is accepted
3. The Settings list is displayed
```

**`reasoning`**：**驗證目標**：按 X 離開行進中攔阻彈窗，返回 Settings 清單。**取材同 OK 支**（層次 1，s1-s2）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### A.14 `VC-063-01` — Motion during a FOTA via Wi-Fi flow raises the block

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P0** | 負向測試 (Negative / Invalid) | `…_13.4.2` |

**`distinguishing_axis`**：攔阻之觸發：流程中起步（對 062-01 之按下設定）

**`test_item`**

```
If the user is in the middle of any of the logic for FOTA via Wi-Fi and the vehicle starts moving, the user shall be presented with the “Feature not available while vehicle is in motion” popup (PU0091).

(Motion starts mid-flow -- the FOTA via Wi-Fi flow is interrupted by the pop-up)
```

**`pre_conditions`**

```
1. The vehicle under test is stationary and the user is part way through the FOTA via Wi-Fi flow
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the step of the FOTA via Wi-Fi flow that is on screen
2. Set the vehicle in motion
3. Record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. A step of the FOTA via Wi-Fi flow is displayed
2. The vehicle is in motion
3. A pop-up is displayed whose text is PENDING: DR-VC10 PU0091 popup string
```

**`reasoning`**：**驗證目標**：FOTA via Wi-Fi 流程中車輛起步時，顯示攔阻彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC18／DR-VC10(一)）**：彈窗文字二源相左 —— SYS1 §13.4.1／§13.4.2 與 037 作 `“**Feature** not available while vehicle is in motion”`；`Pop Up List` 第 93 列 `PU0091` 之 `String/Popup Message` 作 `**Function** not available while vehicle is in motion**.**`（含句末句點），`HMI Settings List` 第 150 列亦作 `Function`。**二份獨立來源對規格一份**，且該欄位就是彈窗的字。**不自行擇一**（§8.4.1）。**與 `062-01` 之區分**：`062-01` 之觸發為**使用者按下設定**（先靜後動之進入嘗試），本筆之觸發為**車輛開始移動**（先進入後起步）—— 二個不同觸發，IN §402 之既有判準即足，不需援引 R-VC26。**不需 baseline**（同 `062-01`）—— 攔的是動作。**範圍（§8.4.2）**：`any of the logic for FOTA via Wi-Fi` 之流程內容屬 Software Updates 側，本筆只驗**起步時之攔阻**，不驗流程本身。

### A.15 `VC-063-02` — OK on the FOTA in-motion popup returns to the pre-flow screen

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.4.2` |

**`distinguishing_axis`**：離開之控制項：OK（對 X 支之同一落點）

**`test_item`**

```
If they press ‘OK’ or ‘X’ they will be returned to the screen which was in context before they interacted with the popup to enter FOTA via Wi-Fi logic.

(FOTA popup dismissed with OK -- return to the screen in context before the flow)
```

**`pre_conditions`**

```
1. The in-motion popup raised during a FOTA via Wi-Fi flow is displayed, and the screen that was in context before the flow was entered is known
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the popup that is displayed and compare its text against PENDING: DR-VC10 PU0091 popup string
2. Press the "OK" option on the popup
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The popup is displayed
2. The OK press is accepted
3. The screen that was in context before the FOTA via Wi-Fi flow was entered is displayed
```

**`reasoning`**：**驗證目標**：按 OK 離開該彈窗，返回進入 FOTA via Wi-Fi 流程前之畫面。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `If **they** press…` 為非句首代名詞，其標的為 s1 之彈窗；**s1+s2 共 68 token，逾 R-3 之 50**，故不取整段，單句 s2 ＋ CONT 登記 `resolution=PC`。**⚠ `resolution_key` 為 `popup` 而非 `pop-up`** —— SYS1 §13.4.2 原文即作 `popup`（§13.1.1／§13.5 作 `pop-up`），依 profile §9.3 **逐字不寬鬆**：不去連字號、不同義展開。故本筆之 Pre-Condition 與 Procedure 一律書 `popup`。**與 `062-02` 之落點不同**：`062-02` 返回 Settings 清單，本筆返回**進入流程前之畫面** —— 二者非同一落點，故非重複。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### A.16 `VC-063-02` — X on the FOTA in-motion popup returns to the pre-flow screen

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_13.4.2` |

**`distinguishing_axis`**：離開之控制項：X（對 OK 支之同一落點）

**`test_item`**

```
If they press ‘OK’ or ‘X’ they will be returned to the screen which was in context before they interacted with the popup to enter FOTA via Wi-Fi logic.

(FOTA popup dismissed with X -- return to the screen in context before the flow)
```

**`pre_conditions`**

```
1. The in-motion popup raised during a FOTA via Wi-Fi flow is displayed, and the screen that was in context before the flow was entered is known
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Record the popup that is displayed and compare its text against PENDING: DR-VC10 PU0091 popup string
2. Press the "X" option on the popup
3. Record the screen that is displayed
```

**`expected_result`**

```
1. The popup is displayed
2. The X press is accepted
3. The screen that was in context before the FOTA via Wi-Fi flow was entered is displayed
```

**`reasoning`**：**驗證目標**：按 X 離開該彈窗，返回進入流程前之畫面。**取材同 OK 支**（第三處置類，單句 s2，`resolution_key=popup`）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### A.17 `VC-064-01` — Transition to Key Off with the Settings tab open

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 狀態轉換 (State Transition Testing) | `…_13.5` |

**`distinguishing_axis`**：開啟之範圍：Settings 頁籤（對 category 支）

**`test_item`**

```
If Settings tab or a Settings category is opened which is not available in Key Off, Timed Mode or ACC and vehicle is turned to Key Off or ACC, show “Turn vehicle to Run or Key On to access menu.” pop-up.

(Settings tab open then transition -- the pop-up appears over the tab)
```

**`pre_conditions`**

```
1. The vehicle is in Run and the Settings tab is open
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Turn the vehicle to Key Off
2. Record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The vehicle is in Key Off
2. A pop-up is displayed and its text reads "Turn vehicle to Run or Key On to access menu."
```

**`reasoning`**：**驗證目標**：Settings 頁籤開啟中車輛轉入 Key Off 時，顯示彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 拆 2 依 R-VC26（下放包 25 §2.3）**：`tab` 與 `category` 為二個**範圍**，且 `064-02` 已載該彈窗**不可被使用者關閉** ——走完其一須**整輪點火循環**才能重建另一之情境，即互相消耗。**⚠ 記法不對稱（A-VC10 第三面）**：Title 作 `Key Off/Timed Mode/ACC`（斜線），Description 作 `Key Off, Timed Mode or ACC` —— 取 Description 一欄，其形態隨之。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### A.18 `VC-064-01` — Transition to ACC with a Settings category open

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 狀態轉換 (State Transition Testing) | `…_13.5` |

**`distinguishing_axis`**：開啟之範圍：Settings 類別（對 tab 支）

**`test_item`**

```
If Settings tab or a Settings category is opened which is not available in Key Off, Timed Mode or ACC and vehicle is turned to Key Off or ACC, show “Turn vehicle to Run or Key On to access menu.” pop-up.

(Settings category open then transition -- the pop-up appears over the category)
```

**`pre_conditions`**

```
1. The vehicle is in Run and a Settings category that is not available in Key Off is open
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Turn the vehicle to ACC
2. Record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The vehicle is in ACC
2. A pop-up is displayed and its text reads "Turn vehicle to Run or Key On to access menu."
```

**`reasoning`**：**驗證目標**：不可用之 Settings 類別開啟中車輛轉入 ACC 時，顯示彈窗。**取材同 tab 支**。**§13.5 之 `tab **or a Settings category**` 是本拆分之依據** ——該措辭明文承認 category 可獨立於 tab 被開啟（上繳包 22 §2.2 之旁證）。**二支之點火目標狀態分取 Key Off 與 ACC**：來源之 `turned to Key Off or ACC` 為二個狀態，二者**不互相消耗**（可循環），本可同筆涵蓋；分置二支使二個範圍各配一個狀態，**不增加 TC 數而涵蓋二者**。

### A.19 `VC-064-02` — Transition pop-up neither times out nor closes

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 功能測試 (Functional based ; no specific technique) | `…_13.5` |

**`distinguishing_axis`**：轉換彈窗之持續：不逾時且不可關（對 -03 之自動解除）

**`test_item`**

```
This pop-up does not timeout and cannot be closed by the user.

(Persistence -- the transition pop-up neither times out nor yields to the user)
```

**`pre_conditions`**

```
1. The Key Off transition pop-up is displayed and the vehicle remains in Key Off
```

**`input_test_data`**：An observation period long enough to exceed any UI timeout, set to 5 minutes as a test-design parameter. The source states no timeout value

**`test_procedure`**

```
1. Leave the pop-up untouched for the observation period named in the test data and record the screen
2. Press the pop-up and each area around it where a close control would normally be, and record the screen after each press
```

**`expected_result`**

```
1. The pop-up is still displayed at the end of the observation period
2. The pop-up is still displayed after each press
```

**`reasoning`**：**驗證目標**：該彈窗不逾時，且使用者關不掉。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `This pop-up` 先行詞在 s1；**s1+s2 共 54 token，逾 R-3 之 50** →單句 s2 ＋ `resolution=PC`／`resolution_key=pop-up`。**與 `058-02` 之對照**：二筆句型幾乎相同，而 `058-02` 之 s1 較短（37 vs 42 token）使其整段未逾限、落在層次 1。**層次不得跳層** —— 差別只在來源句之長度。**為什麼二個斷言不拆（R-VC26）**：「不逾時」與「不可關」**不互相消耗** —— 同一個彈窗可連續觀察，走完其一另一之情境仍在。沿 `045`（不逾時＋選取後不關閉）之既有處置，以二條 ER 涵蓋。**觀察期之 5 分鐘為測試設計參數，非來源所載**。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### A.20 `VC-064-03` — Returning to Run clears the transition pop-up

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P1** | 狀態轉換 (State Transition Testing) | `…_13.5` |

**`distinguishing_axis`**：轉換彈窗之解除：回到 Run（對 -02 之持續）

**`test_item`**

```
If vehicle is turned to Run or Key On while pop-up is on screen, close pop-up and show Settings screen user was in before pop-up was triggered.
 (image: image17.png)

(Return to Run -- the pop-up clears itself and the prior Settings screen comes back)
```

**`pre_conditions`**

```
1. The Key Off transition pop-up is displayed, and the Settings screen the user was on before the transition is known
```

**`input_test_data`**：NA

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

**`reasoning`**：**驗證目標**：車輛回到 Run 時彈窗自動關閉，並回到轉換前之 Settings 畫面。**⚠ 取材為第三處置類**：037 之 `while **pop-up** is on screen` 為**無冠詞名詞回指**；整段 s1-s3 為 **83 token，逾 R-3 之 50** →單句 s3 ＋ `resolution=PC`／`resolution_key=pop-up`。**⚠ 本筆為第一層之偽陰性**（無冠詞名詞回指）——由勘查 (d) 發現。**ER 之 baseline（§5.6）**：「回到轉換前之畫面」須先記錄那是哪一個。**⚠ 未涵蓋者，請上游注意**：來源作 `turned to Run **or Key On**` ——本筆只走 Run。二者**互相消耗**（轉到 Run 後彈窗已消失，須整輪重建才能走 Key On），依 R-VC26 應拆 2；**惟本包授權為 20 筆，其拆分清單未含本筆**，故不自行增筆。若上游認 Run 與 Key On 為同一等價類（「離開受阻狀態」），則本筆之涵蓋完整；若認為二個狀態，則此處為覆蓋洞。**請裁。****追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

---

> 以上 20 筆。收斂 21 項全過，六批回歸全綠。
> 未寫回工作簿、未進行任何 git 操作。
