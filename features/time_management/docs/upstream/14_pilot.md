# 14 上繳 —— R-TM64/65 落檔、B1 四項修正、其餘 12 條自檢

執行層，2026-08-22。對應下放包 `docs/handoff/14_pilot.md`。

---

## 0. 執行結果一覽

| 任務 | 內容 | 狀態 |
|---|---|---|
| T1 | R-TM64 / R-TM65 入 `RULINGS.md` | 完成 |
| T2 | B1 四項修正 + 三項 style | 完成 —— **實改條數多於點名條數，見 §2.4** |
| T3 | 三個閘（B7 調整、A-TM26、write_back 啟動檢查） | 完成，**自驗 42/42 + 5/5** |
| T4 | 其餘 12 條自檢 | 完成 —— **發現 3 defect（皆同型）、10 style（其中 8 項為判準過粗，見 §4.2）** |
| T5 | 本包 | 完成 |

**增量（R-TM46）**：`## R-TM` **+2**（66 → 68）；`## A-TM` **0**（27）；
`## G-TM` **0**（3）。與下放包所訂增量相同。

**lint 對 `generated/B1.json` 之發現由 4 項降為 0 項。**

**本包三項須先看**：§2.4 之**我改的條數多於分析層點名的條數**（且造成
同類問題一部分改一部分沒改）、§4.2 之**我自己的自檢判準太粗**（10 項
style 中 8 項是判準缺陷不是 TC 缺陷）、§3.3 之 **write_back 紅向又一次
構造錯誤**。

---

## 1. T3 —— 三個閘

### 1.1 B7 依 R-TM64 調整

零真值之片以 `raw.strip() == ATL_HI_BARE_PLACEHOLDER` 放行。
**用 `==` 而非 `startswith`**，理由寫進註解：後者會放行「佔位 + 任何尾巴」，
**使 R-TM64 所廢止的 ` / ` 並列從這個豁免口溜回來**。紅向已證：

```
PASS 綠向 R-TM64 (spec_reference 恰為單一 DR-11 佔位 → 不報)
PASS 紅向 R-TM64 (佔位後綴任何尾巴 → 仍報)
PASS 紅向 R-TM64 (佔位帶物件 id —— 明細應在 Remarks)
```

### 1.2 A-TM26 閘（`lint_arch_column`）

含 LID 訊號之 TC，其 reasoning 須有 `Atlantis High (col 26-30)` **與該
訊號之來源列號**。後者為本層自加：只驗字樣存在，等於只驗「有寫」，
不驗「寫的是哪一筆」——加列號後可回溯至 tsv 的特定列。

```
PASS 紅向 (用 $DateTmHour$ 而 reasoning 無 ArchColumn)
PASS 紅向 (有 ArchColumn 但缺來源列號)
PASS 綠向 (ArchColumn 與來源列俱全 → 不報)
PASS 綠向 (未用任何 LID 訊號 → 不判)
```

**本閘之射程已寫在 docstring 內**：只驗記錄之存在，不驗其正確性 ——
記了 `Atlantis High (col 26-30)` 卻其實取自 Powernet 欄，本閘攔不住。
**該層由 context 之 `load_lid_table()` 單一來源保證**（值不由生成端自行
查表），兩者射程互補。此點刻意寫明，以免日後被當成「A-TM26 已全面自動化」。

### 1.3 write_back 啟動檢查（R-TM65）

```
PASS 綠向 (B1 19 條 → 全部 cols key 有著落)
PASS 紅向 (TC 用舊鍵 specification_reference → 攔下)
PASS 紅向 (TC 缺 test_item → 攔下)
PASS 綠向 (全批無 remarks → 豁免，不攔)
PASS 綠向 (空批次 → 不判)
                                     5 / 5
```

**判準為「至少一條 TC 有此鍵」而非「每條都有」**，並附豁免清單
`KEY_CHECK_EXEMPT`（六欄，逐欄附理由）。後者會誤攔 `remarks`
（條件性）與四個由條文決定之欄（`tc_id` / `author` / `tc_ref_id` /
`functional_safety`，write_rows 之迴圈本就明文排除）。

### 1.4 自驗 31 → 42

```
lint_tcs --self-test              42 / 42
write_back 啟動檢查（獨立腳本）     5 / 5
build_batch_context --self-test   13 / 13
```

---

## 2. T2 —— B1 之修正

### 2.1 R-TM64：四條 TC 之佔位移至 Remarks

```
TC#4 (003)  spec_reference: "CFTS015-4813923"
            remarks:  PENDING: DR-11 …（CFTS015-4814088 標為 Atlantis Mid）
                      PENDING: DR-11 …（CFTS015-4814089 標為 Atlantis Mid）
```

真值依 §10.7 重新排列（前綴一次、`, ` 續列、升冪）。
**` / ` 分隔符全批零殘留。**

### 2.2 R-TM65：鍵名統一

19 條 TC 之 `specification_reference` 鍵**全數移除**；lint 之 B7 與 arch
閘改讀 `spec_reference`。原始碼內 `specification_reference` 僅剩 1 處，
為 docstring 中引述 canon §10.1 之**輸出契約欄名**（R-TM65 明訂與 TC JSON
鍵名為兩件事），非鍵名使用。

### 2.3 defect-1（TC#3）—— 採「test_item 收斂為只主張外觀」

```
改前：(confirm the manual entry items are unavailable while GPS sync is enabled)
改後：(confirm the manual entry items are greyed out while GPS sync is enabled)
```

**理由（已寫入該 TC 之 reasoning）**：來源（HMI Settings List 之
`Greys out with sync option selected`）本身只敘述外觀，4813920 亦未述及
可操作性。**若 ER 增一步「嘗試操作並確認無效」，該主張沒有來源** ——
即 §8.4.2 之 scope fabrication。**主張不得超過來源**，故與 ER 一同收斂。

此與分析層所傾向者相同，但理由多一層：分析層說「來源只敘述外觀」，
執行層補「若改另一條路，新增的主張反而無來源」——**兩條路不對稱**。

### 2.4 **defect-2 我改了 3 條，分析層點名 2 條 —— 且造成不一致**

分析層點名 TC#4 / TC#5（003 兩條）。我用的規則是機械性的：
「`input_test_data` 以 `PENDING: DR-10 設定 GPS 位置` 開頭者」，
掃到 **3 條** —— 第三條是 TC#18（012 第一條），同型且在 T4 之覆核範圍內。

**但 010 之三條（TC#15/16/17）同樣違反 §4.5，卻未被改到** ——
因為其佔位字串是 `PENDING: DR-20 注入無效…`，字串不匹配。

**故現況是：GPS 位置類 3 條已改，注入類 3 條未改，而兩者是同一個問題。**
成因是我用了字串匹配而非判準（「該資料是否為互動操作」）。

**未逕行補改**，因 T4 明令「發現即列，不預先修正」，而 010 三條是 T4
之發現。**但這使同類問題呈現不一致狀態，非我所願** ——
**提請於 `15` 一併裁定**（§7.1）。

### 2.5 style —— S1 刪 4 條、S3 改 1 條、S2 保留

S1（`The HU main screen is displayed`）分析層點名 TC#1 / #7，
**實掃到 4 條**（另有 TC#8 / #10）。已全刪。

S3 依建議改為 `Read the state of "Set Time Hours" and "Set Time Minutes"
and record it`（與 TC#3 之寫法一致）。

S2（`Ignition is ON`）依裁定保留。

---

## 3. 兩項過程中的自我更正

### 3.1 自測仍用舊鍵，三個案例假性失敗

改完 B7 與 arch 閘之後自驗掉到 32/35。三個失敗是**自測之 `base_tc` 與
紅向構造仍用 `specification_reference`** —— 閘是對的，測試資料是舊的。
已一併統一（R-TM65 之射程本就及於此）。

### 3.2 **write_back 紅向構造錯誤 —— 第二次同型**

紅向「TC 用舊鍵 → 應攔下」首次未 raise。成因：

```python
{**r, "specification_reference": r.pop("spec_reference","x")}
```

`{**r}` 先展開（此時 `spec_reference` 已被複製進去），`r.pop` 後執行 ——
**結果兩個鍵都在**，自然攔不住。改為先建無舊鍵之 dict 再加新鍵，
並加一行構造複驗（`改名後之 TC 含 spec_reference 者 0 條`）後才判紅綠。

**這是 R-TM56 所記形態的第二次實例**（`13` §1.3 之 `4814035` 是第一次）：
構造錯誤與守衛失效在現象上相同。**兩次都是我在寫紅向時出的**，
故本包起於每個紅向加一行「構造複驗」——先證明壞值真的壞，再看守衛反應。

---

## 4. T4 —— 其餘 12 條自檢

判準取自下放包 §4 所用之同一組。**逐條列出，未預先修正。**

### 4.1 發現總表

| TC# | leaf | 類別 | 內容 |
|---|---|---|---|
| 8 | 007 | — | OK |
| 9 | 007 | style | `The VES screens are powered on` 疑為系統預設狀態 |
| 10 | 007 | style | 步驟 1 與 ER 1 無共同實詞 |
| 11 | 008 | style | `The CAN bus is awake` 疑為系統預設狀態 |
| 12 | 008 | style ×2 | `The CAN bus is asleep`；步驟 1 ↔ ER 1 無共同實詞 |
| 13 | 008 | style | `The CAN bus is awake` |
| 14 | 008 | style | `The CAN bus is awake` |
| **15** | **010** | **defect** | **§4.5 `input_test_data` 與 procedure 重複（`PENDING: DR-20 注入無…`）** |
| 15 | 010 | style | `The VES screens are powered on` |
| **16** | **010** | **defect** | **§4.5 同上** |
| 16 | 010 | style | `The VES screens are powered on` |
| **17** | **010** | **defect** | **§4.5 同上（`恢復有效…`）** |
| 17 | 010 | style | `The VES screens are powered on` |
| 18 | 012 | — | OK |
| 19 | 012 | — | OK |

**合計 13 項：defect 3、style 10。**

### 4.2 **10 項 style 中，8 項是我的判準過粗，不是 TC 之問題**

**(a) 「系統預設狀態」之誤判（7 項）**

我把 `The VES screens are powered on` / `The CAN bus is awake` /
`The CAN bus is asleep` 列入預設狀態清單。**逐項複核後認為皆應保留**：

| 前置條件 | 複核 |
|---|---|
| `The VES screens are powered on` | **4813966 逐字含 `when the screens are powered on`** —— spec 明文條件，非預設 |
| `The CAN bus is asleep` | 匯流排睡眠**絕非預設狀態**，是刻意造出之前提（008 之 wakeup 測試） |
| `The CAN bus is awake` | 與 `Ignition is ON` 同屬分析層 S2 之邊界情形：對「週期性送出」之驗證而言是必要前提 |

**(b) 「步驟 ↔ ER 無共同實詞」之誤判（2 項）**

TC#12 之 `Wake the CAN bus` ↔ `The CAN bus is awake` —— **語意對應完美**，
判為不符是因為我過濾了長度 ≤3 的字（`bus` 被濾掉），只剩 `wake` vs `awake`
兩個不同的字串。TC#10 之 `Read the date shown on the HU display` ↔
`The HU main screen shows the current day, month and year` 同理。

**「共同實詞」不是語意對應之有效代理。** 此判準本身即
「以結構特徵代替內容判斷」——本 feature 一路在記的那個形態，
這次出現在我為檢查它而寫的判準裡。

**(c) 真正成立者 2 項**：TC#12 之 `The CAN bus is asleep` 我判為保留，
故 (a) 7 項全數不成立；**10 項 style 中實際成立者 0 項**。

上表原樣保留（未預先修正），但**執行層之複核結論為：10 項 style 皆不成立**，
提請分析層獨立抽驗以定案。

### 4.3 3 項 defect 全部成立且同型

TC#15/16/17（010 三條）之 `input_test_data` 為
`PENDING: DR-20 注入無效 $DateTmHour$ 之操作方式`，
而 procedure 第 1 步為同一字串。**與分析層在 TC#4/#5 發現者完全同型**：
注入操作是互動操作，依 §4.5 屬 Procedure，`input_test_data` 應為 `NA`。

**未改**（T4 明令）。見 §2.4 之不一致說明。

---

## 5. 驗證輸出

```
lint（對 generated/B1.json）        檔 1；發現 0 項      ← 由 4 項降為 0
lint_tcs --self-test               42 / 42              ← 35 → 42
write_back check_keys_present       5 / 5
build_batch_context --self-test    13 / 13
grep -c '^## R-TM' RULINGS.md      68
generated/B1.json                  19 條；' / ' 零殘留；specification_reference 零殘留
```

---

## 6. 未驗清單（R-TM54 三分）

### A. 可驗而未驗

| # | 項目 |
|---|---|
| A1 | **§4.3 之 3 項 defect 未改**（T4 明令），且與已改之 3 條同型 —— 現況不一致 |
| A2 | 19 條之**內容正確性**仍未經獨立人工覆核（分析層覆核 7 條，執行層自檢 12 條 —— **自檢不等於覆核**） |
| A3 | A-TM26 閘只驗記錄存在，不驗記錄正確（§1.2 已說明射程） |
| A4 | R-TM64 使 Remarks 成為缺口宣告單一落點 —— **B2 之 002 將同時承載 DR-5 與 DR-11 兩種佔位**，其排列與可讀性未定 |
| A5 | `10`–`13` 遺留：G1（讀 CAN 訊號，9 片）、G2、G4、PROXI 設定方式、89 筆 docx 無標籤物件、`section` 未與 Part VII 交叉驗證 |
| A6 | 07/08/09 遺留六項 |

### B. 待 Pei

| # | 項目 |
|---|---|
| B1 | 常數表 v3（`SET_TIME_MANUAL` 依 HMI Settings List 改寫；缺 `Read <signal> in <MESSAGE> on <segment>` 一類，9 片受影響） |
| B2 | A-TM25；`DateTmFormat2`；A-TM26 判準擴充（含分頁名） |
| B3 | DR-8/9/10/11/12/20 之答覆；RD-1 送出 |
| B4 | B1 pilot 之最終放行 |

### C. 已解決

| # | 項目 | 解決於 |
|---|---|---|
| C1 | B7 與 R-TM63 之衝突（`13` §4，4 項 lint 發現） | 本包 T1/T2/T3（R-TM64），lint 歸零 |
| C2 | 鍵名不一致（`13` §5.1，write_back 靜默失效） | 本包（R-TM65）+ 啟動檢查 5/5 |
| C3 | A-TM26 無 lint 閘（`13` §5.3） | 本包 T3（`lint_arch_column`） |

---

## 7. 提請裁定

1. **§2.4 —— 同類問題現處於不一致狀態**：`input_test_data` 之 §4.5 違反，
   GPS 位置類 3 條已改、注入類 3 條未改，成因是我用字串匹配而非判準。
   請一併裁定（建議：三條一併改 `NA`，理由與 §4.2 之裁定完全相同）。
2. **§4.2 —— 我的自檢判準有兩處過粗**（「系統預設狀態」清單過寬、
   「共同實詞」不是語意對應之有效代理），致 10 項 style 全部為誤報。
   **請以獨立抽驗覆核我的複核** —— 我既寫判準又判其成立與否，
   兩者同源。
3. **§3.2 —— 紅向構造錯誤已第二次發生**。本包起每個紅向加「構造複驗」。
   是否值得立為條文（紅向須先證明壞值真的壞）。
4. **A4 —— B2 之 002 將同時有 DR-5 與 DR-11 兩種佔位於 Remarks**，
   其排列與可讀性請於 B2 前定。
