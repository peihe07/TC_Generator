# 上繳包 35 —— Vehicle Category：`065-02` ＋ 生成側終數（T178–T181）

- 日期：2026-08-27
- 對應下放：`docs/handoff/35_final_leaf.md`
  （SHA256 `be2b80dbbba412ec5fdaf469f59389a2ea5f7230b4d8dc001e715fd74fe460d1`，139 行）
- **結論：T178–T181 全數完成。117/117 leaf、TC 126 筆、八批回歸全綠。**
- 未寫回、未進行任何 git 操作。

---

## 0. ⚠ 先看這一件：新通則回溯抓到四筆既有 TC

profile §9.3.1（佔位剝除）之檢查器同步後，**第 5 批第 16 項 FAIL** ——
`058-03` 與 `064-03`（各拆 2，共**四筆**）之 `test_item` **上半含圖佔位**：

```
058-03  '…when attempting to enter the Settings tab.\n (image: image16.png)'
064-03  '…before pop-up was triggered.\n (image: image17.png)'
```

**四筆帶著 `(image: imageNN.png)` 交付了一整包，而當時 22 項全過。**

原因是第 16 項當時**以未剝除之句子為標的** —— 上半照抄該句即相符，
**檢查器與被檢查者一起錯**。§9.3.1 落地後二者分開，才顯出來。

**已依 §9.3.1 剝除**（尾部剝除，其餘欄位逐字未動，已逐欄比對確認）。
**全簿 126 筆重掃：上半仍含佔位者 0 筆。**

> 這是本輪最該記的一件：**新規則的第一個作用不是規範新產出，是照出舊產出**。
> 而它照出來的四筆，是在「22 項全過」的狀態下交付的。

---

## 1. T178 —— 取材通則 ＋ 檢查器同步

profile **§9.3.1** 逐字入檔（下放包 §2.2），`066` 註為先例
（其佔位在句號後，切分自然分離；`065-02` 黏句尾 —— **同一件事的兩種黏法**）。

**本條非純紀律，有機器承載者**：

| 承載者 | 位置 |
|---|---|
| `cont_guard.strip_image_tail()` | 新增，`sentence()` 各層次共用 |
| `verify_batch.py` 第 16 項之 `SENT` | **匯入並呼叫同一支函式** |

**二處共用同一支** —— 其分歧即為錯（同機讀行之原則）。

### 1.1 安全鎖之雙向實測（PLAYBOOK §7.1）

```
(b) 正向 §14.1 s2 剝除後：'If the user presses on the greyed out line they will
    receive a pop-up stating ‘Feature not available while vehicle is in motion’'
    含佔位？ False → PASS
(a) 反向 居中佔位不得剝：'Some text (image: x.png) more text' → 未動 → PASS
(b) 正向 §16.2 首句（佔位在句號後，原就分離）：
    'W0.) Widget title for this feature is Cabrio.' → PASS
```

**反向那一則是本條的要害**：居中剝除會把來源沒有相鄰的兩段文字接在一起 ——
**那是偽造 verbatim**。故只剝尾部，剩餘必為前綴，子串關係必然保住。

---

## 2. T179 —— `065-02`，全案最後一筆

### 2.1 全文

**`test_item`**

```
If the user presses on the greyed out line they will receive a pop-up stating ‘Feature not available while vehicle is in motion’

(In-motion lockout -- the press on the greyed line is answered with the pop-up)
```

**`pre_conditions`**：`1. The vehicle is in motion and the greyed out line for EPB Service mode is displayed`

**`input_test_data`**：NA

**`test_procedure`**

```
1. Press the greyed out line for EPB Service mode
2. Record whether the Service mode screen is entered, and record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The press on the greyed out line is registered
2. The Service mode screen is not entered and a pop-up is displayed whose text is PENDING: DR-VC10 PU0091 popup string
```

| `priority` | `design_method` | `distinguishing_axis` |
|---|---|---|
| **P1** | 負向測試 (Negative / Invalid) | 行進中之按下後果：彈窗（對 -01 之呈現） |

**`reasoning`**：**驗證目標**：按下行進中呈灰之 EPB Service mode 列，操作被攔阻並顯示彈窗。**⚠ 取材為 CONT 層次 2 ＋ profile §9.3.1 之佔位剝除**：037 之 `the greyed out line` 為**定冠詞回指**（其先行詞「灰化之 Service mode 列」在 `065-01`），第一層特徵不命中（profile §9.4.1 第三型之已登記偽陰性）。SYS1 §14.1 之切分把 `(image: image18.png)` 黏在 s2 句尾，**層次 1（整段 s1-2，39 token 未逾 50）與層次 2（單句 s2）之標的原皆夾帶該佔位** —— 下放包 35 §二裁為佔位剝除通則，上半止於佔位之前。CONT 登記 `resolution=PC`／`resolution_key=greyed out line`，第三檢查點驗其 PC 確含該詞。**⚠ R-VC20 之四項揭露（爭議值之 verbatim）**：**(一) 二源逐字** —— SYS1 §14.1 與 037 作 `‘Feature not available while vehicle is in motion’`；`Pop Up List HMI R1 (26PI)` 第 93 列 `PU0091` 之 `String/Popup Message` 作 `Function not available while vehicle is in motion.`（含句末句點），`HMI Settings List` 第 150 列亦作 `Function`。**(二) 分歧點** —— `Feature` vs `Function`，及句末句點之有無。**(三) 取 SYS1 為 verbatim 上半之理由** —— R-S4 要**規格原句**，非採信其值；換取彈窗清單之值只是換一個爭議值（R-VC20(a)）。**(四) 阻斷之 DR** —— **DR-VC10(一)**，A-VC18。**依 R-VC20(c)，爭議值不入 ER 之判準位** —— ER 驗「未進入 ＋ 彈窗出現」，其文字判準以 `PENDING: DR-VC10 PU0091 popup string` 承載（位置在 ER：缺件影響「怎麼判」，profile §7.2.1）。**不需 baseline** —— 攔的是動作後果（是否進入、彈窗是否出現），非值比對（同 `062-01`／`063-01` 型）。**與 `065-01` 之分工（IN §8.2.1）**：`-01` 驗**呈現**（灰化），本筆驗**按下之後果**（攔阻＋彈窗）—— 二個不同驗證點。**未涵蓋**：§14.2 之彈窗優先序（037 未涵蓋，表 B 第 14 列）。

### 2.2 R-VC20 四項揭露之落實

下放包 §2.3 稱「reasoning 四項揭露（二源逐字、分歧點、取 SYS1 之理由、DR-VC10）」。
**R-VC20(b) 之原文為「二**欄**各自之逐字內容」**（037 之二欄）——
本筆之分歧不在 037 二欄，而在**二個來源檔**（SYS1／037 vs 彈窗清單／設定清單）。
**已依其實質適用，並於 reasoning 標為「二源逐字」**，記明此適用之調整。

四項齊備：
1. **二源逐字** —— SYS1 §14.1 與 037 作 `‘Feature not available…’`；
   `Pop Up List` 第 93 列 `PU0091` 作 `Function not available…**.**`；
   `HMI Settings List` 第 150 列亦作 `Function`
2. **分歧點** —— `Feature` vs `Function`，及句末句點之有無
3. **取 SYS1 之理由** —— R-S4 要**規格原句**，非採信其值；
   換取彈窗清單之值只是換一個爭議值（R-VC20(a)）
4. **阻斷之 DR** —— DR-VC10(一)，A-VC18

**R-VC20(c)**：爭議值**不入 ER 之判準位** ——
ER 驗「未進入 ＋ 彈窗出現」，其文字判準以
`PENDING: DR-VC10 PU0091 popup string` 承載（位置在 ER：缺件影響「怎麼判」，
profile §7.2.1）。

### 2.3 CONT 登記與收斂

```
065-02  reference  14.1  2  PC  greyed out line
```

`resolution_key` 依 §9.3 **逐字取 PC 之實際用詞**（`greyed out line`），
不和稀泥。第三檢查點驗其 PC 確含該詞 —— 第 17 項通過。

**上半為 SYS1 §14.1 s2 剝除後之文字**（非 037 `Description`——
後者多一個句末句點）；第 16 項逐字比對通過。

### 2.4 第 6 批收斂全輸出

```
第 18 項 —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  (b) 已知標的 插入「見第 99 項」應 FAIL  PASS
  self-test 2  (a) 反向 現行全部名稱應全過          PASS
verify_batch — batch6_brake_service.json（收斂條件；下放包 10 §四 ＋ 13 §4.4）
  #  條件                                                             判
------------------------------------------------------------------------------------------------
  1  2 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                            PASS
     TC 數 2；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）                        PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）              PASS
     命中 0 處 無
  3  test_item 括號下半 2 筆兩兩不同（機械）                                     PASS
     缺括號 無；重複 無；相異 2
 3b  test_item 括號下半無中文（R-S4）                                        PASS
     含中文 無
  4  specification_reference 2 筆與 recon_leaf_to_section.tsv 逐字相符    PASS
     不符 0 筆 
  5  priority 2 筆與 priority_final.tsv 逐字相符                          PASS
     不符 0 筆 
  6  Test Set 2 筆一致，Test Group 皆為 `Vehicle Category`                PASS
     test_set=['Brake Service']；test_group=['Vehicle Category']
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                                 PASS
     尾句號 0；單引號 0；方括號角括號 0；空白 0
 7b  test_item 上半為來源之逐字子串（R-VC23(c)；整段，不倚樣式表）                       PASS
     取材來源分布 {'Description': 2}；未對上來源 0 筆 無
  8  PENDING 之分布與其字串（pilot 專屬；他批以第 8b 項驗）                           PASS
     033-01 之 PENDING 數 None；字串相符 False；他筆帶 PENDING {'SWE1-HMI-VC-065-02': 2}
 8b  PENDING 之樣式、DR 存在性、與 pending_scope 之宣告相符                       PASS
     實際 1 處；宣告 1 筆；DR 分布 {'DR-VC10': 1}；不符 0 處 無
  9  `028-02`／`033-01` 之括號下半明載其流程（pilot 專屬）                         PASS
     未載者 無
 10  `VC-021` 之委派（pilot 專屬；本批不適用）                                   PASS
     N/A
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 步驟無 observe/verify 起首 PASS
     步數不足 無；1:1 不符 無；ER 含 modal 無；禁用起首動詞 無
 13  該批 Test Set 全筆一致且與 framework.md §2 逐字相符                        PASS
     批內 test_set=['Brake Service']；framework §2 之 8 組=8 個；相符=True
 14  常數之變體擴散（正規化後相等而原字不同 → FAIL；§5.3）                               PASS
     profile 常數（展開後）3 條；變體 0 處 無
 15  母體 = leaf_scope + split_delta = 2 + 0 = 2（R-VC22(b)／IN §8.2.2） PASS
     tcs=2；leaf_scope=2；宣告 split_delta=0；實際拆分增量=0；held=0（b 段不計入母體）
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）                   PASS
     適用 1 筆；不符 0 筆 無
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     PASS —— 未處置候選 0；內容不符 0；結構聲稱不符 0；離開碼 0
 18  檢查之名稱／說明所引之項號皆存在（下放包 26 §一）                                    PASS
     self-test 全過；掃描 21 項；引用之項號 ['11', '12', '3', '4', '5', '6', '7', '8', '8b']；無主 0 處 無
------------------------------------------------------------------------------------------------
22 checked / 0 failed
```

---

## 3. T180 —— NN 檢查擴充

PLAYBOOK **§7.7**：二項（既有之碰撞檢查 ＋ **前一主號之上繳包存在**），
字母後綴包（20a 型）豁免第 (2) 項。

**其所以有效**：**上繳包只有執行層會寫** —— 它存在即證明該包被執行過。

**併記執行層側之對應動作**：收到編號包時，若前一主號之上繳包不存在，
**先回報「前包疑未執行」再動手** ——
本 feature 於下放包 34 即應如此，**實際是做到一半才發現**
（`RESUME_PLAN.md` 不存在、R-VC29 未抄錄）。

**已記明其只有一半承載者**：`list_directory` 可查二項，
但**沒有腳本在包落檔時自動跑它**，其執行仍靠人記得。

---

## 4. T181 —— `RESUME_PLAN` 更新

- `065-02` 標 ✅ 已解，**生成側自此無任何待辦**
- PENDING 母體 **13 → 14 處**（＋`065-02` 之 DR-VC10）
- 新增 §4.5 生成側終數

**待辦剩四項**：PENDING 結案（DR）、表 B 定稿（DR-VC3）、
**Excel 驗收（Pei）**、寫回授權（分析層，待前項）。

---

## 5. 八批回歸 ＋ 側檔

```
pilot_glovebox                     22 checked / 0 failed
batch1_category_structure          22 checked / 0 failed
batch2_settings_list               22 checked / 0 failed
batch3_controls                    22 checked / 0 failed
batch4_settings_behavior           22 checked / 0 failed
batch5_ignition_availability       22 checked / 0 failed
batch6_brake_service               22 checked / 0 failed
batch7_cabrio_widget               22 checked / 0 failed
```

```
對應驗證：鍵 126 個（其中拆分之第 2 筆以上 9 個）；PASS
```

**全簿掃描**：126 筆中上半含 `(image:)` 者 **0 筆**。

---

## 6. 生成側終數

```
117 / 117 leaf 全數處置
TC 126 筆
八批回歸 22 checked / 0 failed ×8
PENDING 14 處（DR-VC10 8／DR-VC9 4／DR-VC1 1／DR-VC8 1）
```

**與下放包預估相符**（126 筆）。

---

## 7. 量測條件揭露（R-G8）

- **§0 之剝除為尾部剝除**，已逐欄比對確認其餘欄位逐字未動
  （`test_item` 以外之 15 個欄位全等）。
- **`065-02` 之上半取自 SYS1 §14.1 s2**，非 037 `Description`
  —— 二者差一個句末句點，第 16 項要求前者。
- **下放包 §2.3 之上半以直單引號 `'…'` 書寫**，
  而**來源實為彎單引號 `‘…’`** —— 依 R-VC23 取來源之逐字，
  非下放包之轉寫。**該差異為下放包之排版，非裁定內容。**
- **`(image:` 之樣式為字面比對**（`\(image:[^)]*\)`）——
  若匯出另有他種插圖標記（如 `[image]`、`WrapperResource`），本函式看不到。
  **未掃全簿確認是否另有他種形態。**
- **§0 之四筆為第 5 批**；其餘七批之上半**已由全簿掃描確認無佔位**，
  但該掃描為**剝除之後**所做 —— 剝除前之全簿狀態未量。

---

## 8. 待你裁

1. **Excel 人工驗收**（Pei）—— **掛五包了，是寫回前唯一未過之門**
2. 寫回授權（分析層，待第 1 項）
3. Tier 3：十筆 DR、`QS Suggestion` 第 4 項

> **生成側到此結束。** 之後無任何生成側工作。
