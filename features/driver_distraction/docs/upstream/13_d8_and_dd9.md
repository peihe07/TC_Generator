# 上繳包 13 —— R-DD20／A-DD10 落地、DR-DD8／DD9 建檔、D8 修復（T22a）、Q1 之答案（T22b）、power 線傾印（T22c）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`16_dd9_d8.md` §八（T-抄／T-登／T22a／T22b／T22c）
- 本輪**未生成 `-001`／`-002`**（下放包 16 §八「不在本輪」，待包 17）、
  **未生成 `-025`~`-028`**、**未寫回**、**未執行 git**、**共用路徑未寫入一字**

> **三件事**：
> **D8 修好了，而且比 D8 所指的更壞** —— 檢 3／4／8／11／13 之 detail 行是 pilot 殘值，
> 這是已知的；**新查得檢 9 與檢 11 之「判斷本身」也是 pilot 硬編**
> （`leaf ∈ {010, 012}`），故 B1／B2 之九則 fail-safe **從未被檢過**；
> 檢 11 之條件更是**恆為偽**，該檢自建立起未攔過任何事（§三-2）。
> **T22b 二擇一取「寫明規則」** —— raw `0` 之特例移除，連續量標籤改為
> **R-DD9(b) 之 DBC factor／offset 覆算**；溯源標籤自 `profile §3.1` 改為
> `R-DD9(b) 覆算`。**附二組舊綠新紅之注入**（§四）。
> **T22c 之傾印查無所託之物** —— power 線 RULINGS／profile 之 `BODY OFF`
> 命中為 **0**（11 處皆為 `BODY OFF-TIMED`，另一具名狀態），
> 且 power 線之狀態進入步驟**全為通稱式，無一帶訊號名／值／格式**。
> **逐字同名確實存在**，但在 CFTS009 文字層錨點 `4941238`（§六）。

---

## 一、T-抄 —— R-DD20

| 條號 | 來源 | 字元數 | 落檔 | 逐字元差異 |
|---|---|---|---|---|
| R-DD20 | 下放包 16 §一 | **961** | 1 次 | **0** |

錨點依 R-DD14(a) 為裸 `## R-DD20`（現行版），置於圍籬上方；索引表新增一列。

**條數與停止值同步**：

| | 上輪 | **本輪** |
|---|---|---|
| 索引現行 | 19 | **20** |
| 索引留存 | 1 | 1 |
| 錨點（`^## R-DD`）| 20 | **21** |
| **停止條件 2 之值** | 20 | **21** |

### ⚠ 指紋台帳之落差 —— 上輪之 R-DD19 **未入 tsv**

`rulings_hash.py` 為**共用路徑之寫入**（`docs/fw036/RULINGS.sha.tsv`），
依 A-DD4／下放包 16 §八「不在本輪：tsv」，**本輪只試跑、不寫入**
（跑後已還原，`git status` 對該檔無變更）。試跑實測：

| | 試跑前（磁碟上之 tsv）| 試跑所得 |
|---|---|---|
| driver_distraction 之列數 | **19** | **21** |
| 新增 | — | `R-DD19` `e293c320`、`R-DD20` `00912428` |
| 既有 19 列之 `sha8` | — | **逐一比對全未變** |
| 非 DD 之列 | — | **diff 0 行** |

**`R-DD19` 之列本應於上輪即在** —— 上繳 12 §1 所報之
「唯一差異為新增之 `R-DD19 e293c320`」是**試跑結果**，該輪同樣未寫入，
故台帳自上輪起即落後一條。本輪之試跑值與其完全相符（`e293c320`），
**即條文本體未變，只是台帳未跟上**。

> **這是「量測做了但沒有落地」** ——
> 與 D8 之「detail 行不是這份產物的」同族：都是報告與狀態的脫節。
> **處置屬分析層**：若 tsv 應隨條文即時更新，則「不在本輪」之排除清單
> 須把它排除在排除之外；若確實延後，則**停止條件 2 之值**在 tsv 補齊前
> 應以 `RULINGS.md` 之錨點數（21）為準，不以 tsv 列數為準。本輪照後者報。

---

## 二、T-登

### 2.1 A-DD10 建條

`ANOMALIES.md` 新增 `## [A-DD10] 假設：Body OFF 之同一性`，
**條目逐字 197 字元，落檔 1 次，逐字元差異 0**。
同時把 `## Assumption markers` 之 `None yet.` 換為現行 marker 清單
（`A-DD2`／`A-DD6`／`A-DD7`／`A-DD8`／`A-DD9`／`A-DD10`）——
該處自建檔起未更新，已有六個 marker 在用而該節仍書「尚無」。

**條目內另載一節「⚠ 執行層之實測與所書不符」**，見 §六-1。

**適用範圍**：`-001`／`-002`。**本輪二則未生成**，故現無任何 TC 掛此 marker。

### 2.2 DR-DD8／DR-DD9 建檔

| DR | 來源 | 字元數 | 落檔 | 逐字元差異 | 狀態 |
|---|---|---|---|---|---|
| **DR-DD8** | 下放包 16 §二 | **1312** | 1 次 | **0** | **DRAFTED**（必發）|
| **DR-DD9** | 下放包 16 §三 | **1254** | 1 次 | **0** | **DRAFTED**（必發）|

二者各附形態說明、與台帳項之連結，並補入索引表與發送清單。

### 2.3 [CG-DD1] 連結 DR-DD8

`COVERAGE_GAPS.md` 之末節「本項未登 DR 之理由」原書
「是否另立 DR 索取，屬分析層」—— **分析層已裁（下放包 16 §二）**，
故該節改為刪除線保留 ＋ 承接說明，並列出三個解除條件與 DR-DD8 之對應：

| 解除條件 | 承接之 DR | 對應 |
|---|---|---|
| 甲（可機讀之表）| **DR-DD8** | 直接 —— Request 段即甲案 |
| 乙（分析層指定樣本）| — | 不需 DR |
| 丙（上游確認不屬驗證範圍）| **DR-DD8** | 間接 —— 回覆若為「表中無非 L/O 列」即丙 |

**狀態仍為 OPEN**（DR-DD8 未發送，甲、丙皆未成就）。

**另記明一件未逕改者**：本條首欄之「影響 leaf `-013`／`-015`」為 T20c 登記時之範圍，
而 DR-DD8 所引之 CFTS022 列為 `-120`／`-121`，其 037 衍生 leaf 為 `-021`~`-024`。
二組同源於同一張表 —— **範圍之認定屬分析層，執行層不逕改**，僅記明供包 17 併裁。

### 2.4 順帶補正之一處過期狀態陳述

`DATA_REQUESTS.md` 索引表之 **DR-DD5／DD6 `Batch impact` 欄**仍書
「**該 8 leaf 不入批次**」—— 而 B2 八則已於上輪產出。
上繳 12 §2.3 改的是 **DR 文稿末行**，**本表之欄位當時未同步**。
依下放包 16 §七之拘束（不得陳述已失實之狀態）本輪補正，並於發送清單下記明成因。

> **同一過期陳述之第二處。** 上輪抓到文稿、漏了台帳 ——
> 「改了一處就以為改完了」本身是個形態，值得記。

---

## 三、T22a —— D8 修復（detail 行一律由 `SC_ARTIFACT` 導出）

### 3.1 D8 所指之五項，逐一之修法

| 檢 | 舊 detail（pilot 殘值）| **新 detail 之導出源** |
|---|---|---|
| 3 | `0 命中；4 則各 1 項且皆合 R-DD17 之形式` | `len(TCS)`、逐 TC 之 PC item 數與訊號源行數 |
| 4 | `4 則皆 NA=…` | `len(TCS)` 與實際 NA 則數 |
| 8 | `4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟` | 則數、步驟總數、`$ ` 指令行數、步驟起首動詞聯集 |
| 11 | `FF：010／012 之 fail-safe 皆先建立正常態…` | 由形態判出之 fault 集合＋逐則之注入步序 |
| 13 | `009/011 觸發為 A→B 狀態轉換…` | 由 `WANT` 分組導出，逐組附其命中理由 |

**三產物之新 detail 逐字（§3.3）皆隨產物而變** —— 4／10／8 則、
12／29／24 步驟、2／5／4 則 fault、分組各異。

### 3.2 ⚠ 修時查得三件比 D8 更壞的 —— **判斷本身也是硬編**

D8 說的是「detail 行不是這份產物導出的」。修的時候發現**三處是判斷本身的問題**：

| # | 項 | 舊碼 | 後果 |
|---|---|---|---|
| **甲** | 檢 9 | `if k in ("010", "012"):` | B1／B2 之 fault 列（`004`／`006`／`008`／`014`／`016`／`018`／`020`／`022`／`024`，共 **9 則**）**全走 else 分支**，被當成一般列驗「PC 有訊號源行」。**其 baseline 從未被檢** |
| **乙** | 檢 11 | `leaf in ("010","012") and not re.search(r"^1\.", items(...)[0])` | `items()` 之切分即以 `^\d+\.` 為界，故 `items(...)[0]` **恆以 `1.` 起首**，`not …` **恆為偽** —— 該集合**恆空**。**此檢自建立起未攔過任何事** |
| **丙** | 檢 8 | `cli = [… if "$ " in tc["test_procedure"]]` | 訊號記法 `$MSG.Sig$ = 129` 即含 `$ `，故該集合**恆非空**；因 verdict 硬寫 `"N/A"`，此偵測**從未影響結果** |

**三者皆為「綠而空轉」** —— 與 D8 同族，程度更深：
D8 是「證據不是這份產物的」，甲／乙／丙是「**根本沒有證據，只有一句話**」。

**修法**：立三個自產物導出之共用述詞，取代 leaf 號與字面：

```python
RE_FAULT  = re.compile(r"Stop transmitting|timeout", re.I)
RE_ACCESS = re.compile(r"\b(open|start|select|play|enter|launch)\b", re.I)

def is_fault(tc):   # simulated fault 之形態，非以 leaf 號判
    return bool(RE_FAULT.search(tc["test_procedure"]))

def fault_at(tc):   # 注入所在之步驟序（1-based）
    ...
```

- **檢 9**：fault 列改驗「注入之前已見正常行為」——
  **不限步驟 1**（B2 之注入在步驟 3，其前二步為送檔位＋開功能）。
  非 fault 列改驗「PC 有合 R-DD17 形式之訊號源行」，**值不硬編**
  （舊碼硬編字面 `"at 0 (0.0000 km/h)"`）。
- **檢 11**：`ff` 改為真檢 —— 注入步序 > 1 **且**其前諸步含存取動作。
  FP 面加一個列舉式支援項之偵測（`format`／`device`／`protocol`／`codec`／`container`），
  0 命中即記明「無配對義務」，不再以一句話代之。
- **檢 8**：偵測改為「item 去編號後有以 `$ ` 起首之行」；
  且 **verdict 隨之**（有 CLI 步驟時驗其描述部，非一律 N/A）。
- **檢 3**：`RE_SIGSRC` 之單位由硬編 `km/h` 改為 `\([^)]+\)`
  —— 標籤之正確性由檢 12 之覆算承擔，此處只驗行之形式（**職責不重疊**）。

### 3.3 三產物重跑 —— 五項之 detail 逐字（機器輸出）

```
######### pilot_group3.json（4 TC）
[PASS]   3 禁式 0 命中；4 則之 PC item 數 {'009': 1, '010': 1, '011': 1, '012': 1}；
           其中訊號源行 {'009': 1, '010': 1, '011': 1, '012': 1}，共 4 行皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 4 則中 NA 4 則（全數=True）；回指 無；跨欄重複 無
[N/A ]   8 4 則、共 12 步驟，以 `$ ` 起首之指令行 0 —— 無適用對象；
           步驟起首動詞 ['Open', 'Read', 'Select', 'Send', 'Start', 'Stop']
[PASS]  11 FF：本產物 2 則為 simulated fault（010(步驟 2/3)✓／012(步驟 2/3)✓），
           皆先建立正常態再注入，未假設隱藏狀態；FP：列舉式支援項命中 無，無配對義務
[PASS]  13 010／012 → 基礎故障注入 (Fault Injection Lite)（simulated fault（停送／逾時），於 State Transition 前命中）；
           009／011 → 狀態轉換 (State Transition Testing)（同一訊號於 PC 與 procedure 得二相異值（A→B），於 Scenario 前命中）；
           不符 first-match 無；皆為下拉選單實值 True

######### batch_b1.json（10 TC）
[PASS]   3 禁式 0 命中；10 則之 PC item 數 {'003': 1, '004': 1, '005': 1, '006': 1, '007': 1,
           '008': 1, '013': 1, '014': 1, '015': 1, '016': 1}；其中訊號源行（同上，各 1），
           共 10 行皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 10 則中 NA 10 則（全數=True）；回指 無；跨欄重複 無
[N/A ]   8 10 則、共 29 步驟，以 `$ ` 起首之指令行 0 —— 無適用對象；
           步驟起首動詞 ['Open', 'Select', 'Send', 'Stop']
[PASS]  11 FF：本產物 5 則為 simulated fault（004(步驟 2/3)✓／006(步驟 2/3)✓／008(步驟 2/3)✓／
           014(步驟 2/3)✓／016(步驟 2/3)✓），皆先建立正常態再注入，未假設隱藏狀態；
           FP：列舉式支援項命中 無，無配對義務
[PASS]  13 004／006／008／014／016 → 基礎故障注入 (Fault Injection Lite)（…）；
           003／005／007／013／015 → 狀態轉換 (State Transition Testing)（…）；
           不符 first-match 無；皆為下拉選單實值 True

######### batch_b2.json（8 TC）
[PASS]   3 禁式 0 命中；8 則之 PC item 數 {'017': 3, '018': 3, '019': 3, '020': 3, '021': 3,
           '022': 3, '023': 3, '024': 3}；其中訊號源行（各 1），
           共 8 行皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 8 則中 NA 8 則（全數=True）；回指 無；跨欄重複 無
[N/A ]   8 8 則、共 24 步驟，以 `$ ` 起首之指令行 0 —— 無適用對象；
           步驟起首動詞 ['Open', 'Send', 'Stop']
[PASS]  11 FF：本產物 4 則為 simulated fault（018(步驟 3/4)✓／020(步驟 3/4)✓／
           022(步驟 3/4)✓／024(步驟 3/4)✓），皆先建立正常態再注入，未假設隱藏狀態；
           FP：列舉式支援項命中 無，無配對義務
[PASS]  13 018／020／022／024 → 基礎故障注入 (Fault Injection Lite)（…）；
           017／019／021／023 → 決策表 (Decision Table Testing)（條件 ≥2（PC 之組態列 ＋
           procedure 之施加）且無二值轉換）；不符 first-match 無；皆為下拉選單實值 True
```

**三產物之總計**：

| 產物 | 檢數 | 結果 |
|---|---|---|
| pilot（4 TC）| **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |
| B1（10 TC）| **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |
| B2（8 TC）| **26** | **24 PASS ／ 2 N/A ／ 0 FAIL** |

**產物本體未動一字**（本輪只改自檢腳本；`generated/*.json` 之 mtime 與內容不變）。

> **D8 所定之「重跑前該五項視為未證」已解除** ——
> 但**解除之範圍要說準**：解除的是「這份輸出證不了那五項」，
> 不是「那五項本來就對」。實際上 §3.2 甲／乙查出 **B1／B2 之九則 fault 列
> 從未被檢**，本輪首次檢到，**全數通過**。**先前是不知道，現在知道了。**

---

## 四、反向對照 —— 七種注入，舊檢／新檢並列

新檢是綠的，綠不代表它在工作。注入七種壞值（暫存於 `generated/inj_*.json`，
**跑完即刪**，正式產物未動），**同一注入同時餵舊檢與新檢**：

| # | 注入 | **舊檢** | **新檢** |
|---|---|---|---|
| **A** | 檢 11／9：fail-safe 之注入置於步驟 1，其前無正常態之建立 | **全綠（漏放）** | **FAIL 2**（檢 9／11）|
| **B** | T22b：列舉訊號 `GearEngagedForDisplay_PT` 掛連續量標籤 `0 (0.0000 km/h)` | **全綠（漏放）** | **FAIL 1**（檢 12）|
| C | T22b：`129` 之標籤改 `8.0630 km/h`（factor 0.0625 覆算得 8.0625）| FAIL 2（檢 12／17）| FAIL 2（檢 12／17）|
| D | 檢 3：PC 增一兼述環境之訊號源行（違 R-DD17 形式）| FAIL 2（檢 3／+）| FAIL 2（檢 3／+）|
| E | 檢 4：`input_test_data` 非 NA | FAIL 1（檢 4）| FAIL 1（檢 4）|
| F | 檢 8：加一裸 `$` 指令行（item 內無描述部）| FAIL 1（**檢 +**，空白項）| **FAIL 2（檢 8／+）** |
| G | 檢 13：fail-safe 列之 `design_method` 改為 Scenario | FAIL 1（檢 13）| FAIL 1（檢 13）|

**A 與 B 為舊綠新紅** —— 即下放包 16 所要之「使其變紅之注入」。

- **A** 之意義：舊檢對 fail-safe 之隱藏狀態假設**完全無防**（§3.2 乙之恆偽條件）。
  新檢同時由檢 9 與檢 11 兩路攔下（baseline 與 FF 各自成立）。
- **B** 之意義：**這就是 raw `0` 之後門**。舊檢之 `PROFILE_RAW` 含 `0: "0.0000 km/h"`，
  **不問是哪一個訊號** —— 故把一個列舉量（檔位，`VAL_ 0 = "Initialize"`）
  寫成 `0 (0.0000 km/h)` 也照樣過。新檢因 `0` 在該訊號之 `VAL_` 內而要求逐字，
  且覆算得 `"0 "`（factor 1、無單位）與 `km/h` 不符 → 紅。
- **F** 之意義：舊檢之檢 8 恆為 N/A，該注入只被一個空白格式項順手抓到；
  新檢由檢 8 本身正面攔下。

---

## 五、T22b —— `0 (0.0000 km/h)` 之溯源歸類（**取「寫明規則」，不留特例**）

### 5.1 舊碼之特例，逐字

```python
PROFILE_RAW = {129: "8.0625 km/h", 77: "4.8125 km/h", 0: "0.0000 km/h"}
```

**profile §3.1 之表只有兩列**（`129` = 8.0625 km/h、`77` = 4.8125 km/h）。
`0` **不在該表**，卻被寫進了以該表為名的常數，且**溯源標籤報為 `profile §3.1`**。
下放包 16 §五所問「它是怎麼過檢的」之答案：**它是被手加進去的**。
且該表**不問訊號** —— 任何訊號之 raw `0` 掛 `0.0000 km/h` 皆過（§四-B 已證）。

### 5.2 取甲案 —— 把規則寫明並機械化

**新判準（IN §8.4.1 ＋ R-DD9）**：四交付欄中每一個 `= <raw> (<label>)`：

| 情形 | 判準 | 溯源標籤 |
|---|---|---|
| 該訊號之 DBC `VAL_` **涵蓋**此 raw | `label` 須與 `VAL_` **逐字相同** | `DBC VAL_` |
| 該訊號之 `VAL_` **未涵蓋**此 raw（含全無 `VAL_`）| **依 R-DD9(b) 覆算**：`raw × factor + offset`，小數位數取 **factor 字串之小數位**，附 DBC 單位（單位比對不分大小寫）| **`R-DD9(b) 覆算`** |
| PROXI 參數 | `PROXI Format` r443 之 Table 列舉 | `PROXI Format r443` |
| 裸 raw（無括號標籤）| 一律不可溯（R-DD9 要求帶標籤）| — |

實作：`_dbc_meta(sig)` 自二綁定 DBC 之 **該 `BO_` 區塊內**讀 `SG_` 行之
`(factor, offset)` 與單位字串（**限定於該訊息之區塊**，避免同名訊號跨訊息誤取）；
`_rdd9b(raw, sig)` 覆算並格式化。

**本件之實值**：`STATUS_CCAN3.VehicleSpeedVSOSig`，`BO_ 994`，
`47|13@0+ (0.0625,0) [0|511.9375] "Km/h"` →

| raw | 覆算 | 產物所書 | 判 |
|---|---|---|---|
| `0` | 0 × 0.0625 + 0 = **0.0000** | `0 (0.0000 km/h)` | ✓ |
| `77` | 77 × 0.0625 = **4.8125** | `77 (4.8125 km/h)` | ✓ |
| `129` | 129 × 0.0625 = **8.0625** | `129 (8.0625 km/h)` | ✓ |
| `8191` | `VAL_ 8191 "SNA"` 涵蓋 → 走逐字支 | `8191 (SNA)` | ✓（R-DD9(c)）|

**小數位數不由本檔選定**：factor 之字串 `0.0625` 有 4 位小數，故書 4 位。
**單位取 DBC 之 `"Km/h"`，比對不分大小寫**（產物依 profile §3.1 書 `km/h`）——
此為本次唯一之寬鬆處，**明記於此**，其餘皆嚴格逐字。

### 5.3 歸類標籤隨之改（下放包 16 §五所要求者）

| 產物 | 舊溯源分布 | **新溯源分布** |
|---|---|---|
| pilot | `{'profile §3.1': 6}` | `{'R-DD9(b) 覆算': 6}` |
| B1 | `{'profile §3.1': 18}` | `{'R-DD9(b) 覆算': 18}` |
| B2 | `{'profile §3.1': 8, 'PROXI Format r443': 8, 'DBC VAL_': 16}` | `{'R-DD9(b) 覆算': 8, 'PROXI Format r443': 8, 'DBC VAL_': 16}` |

**`profile §3.1` 不再是任何標籤之溯源出處。**
它仍是**「取哪一個 raw」之權威**（門檻選值；由檢 17 與 `[ASSUMPTION A-DD6]` 承擔）——
**選值與書值是兩件事，先前混在一格裡，這是它能藏住一個特例的原因。**

### 5.4 該規則之變紅注入

§四之 **B**（列舉訊號掛 km/h 標籤，**舊綠新紅**）與 **C**（覆算差一位，舊新皆紅）。
B 是規則改變所新增之防護，C 是規則改變後仍保有之防護 —— **二者都附，方能說明沒有換出漏洞。**

---

## 六、T22c —— power 線 Body OFF 程序之傾印（唯讀；**只傾印，不判同一性、不代擬 TC**）

### 6.1 先報一件與下放包 §一(a) 所書不符者 —— 「78 處命中」未能重現

R-DD20(a) 之採認基礎書：「CFTS022 r114 與 **power 線 RULINGS 之 78 處命中**」。
**逐檔實測**（命令與母體見 §九-2）：

| 標的 | 條文所書 | **實測** |
|---|---|---|
| `features/power/RULINGS.md` 之 `BODY OFF`（去 `-TIMED`）| 78 | **0** |
| 同檔之 `BODY OFF-TIMED` | — | **11** |
| `docs/runtime/profiles/FW036_R1L_Power_Profile.md` 之 `Body OFF` | — | **0** |
| `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` | — | **0** |
| `features/power_moding/RULINGS.md` | — | **0** |
| **power 線全線**（含 `data/`、`generated/`、`scripts/`）之 `Body OFF`（去 `-TIMED`）| — | **86** |

**`BODY OFF-TIMED` 是另一個具名狀態**（見 CFTS010 之
`While in BODY ON or BODY OFF-TIMED mode`），**非 `BODY OFF`**。

**依 T22c 之拘束，本輪不判同一性**，只報三件事實：
（i）所書之計數與位置在該二檔查無；
（ii）逐字同名**確實存在**，但在 CFTS009 之文字層（§6.2 之 `4941238`）；
（iii）此差異已記入 A-DD10 之條目，**A-DD10 之狀態未動**（改條屬分析層）。

### 6.2 進入 Body OFF ／ sleep ／喚醒之**施加式** —— 逐字傾印

**唯讀來源**：`features/power/data/textlayer/cfts009_plain.txt`
（CFTS009 之文字層，power 線之綁定來源；**該線之 RULINGS／profile 無此內容**）。

**(a) Body OFF 之定義 —— 這是唯一帶訊號名與值格式者（錨點 `4941028`）**

```
4941028: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ALL]
[Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:PowerNet, CUSW]
The Body OFF is defined as $PowerMode$ = [IGN_LK] or $PowerMode$ = [IGN_OFF] or
$PowerMode$ = [IGN_START] or $PowerMode$ = [undefined] or $PowerMode$ = [SNA].
```

**(b) 其對照之 Body ON（錨點 `4941027`，同節）**

```
4941027: […]
The body power mode defines whether the A&T system would perform it's normal
operation or sub/no-operation. The sleep and wake activities are controlled by
the CAN network only unless specified. The HU will control the audio modules
system power that is on body CAN using HU power state. The Body ON mode is
defined as $PowerMode$ = [IGN_ACC] or $PowerMode$  = [IGN_OFF_ACC] or
$PowerMode$ = [IGN_RUN].
```

（`$PowerMode$  = [IGN_OFF_ACC]` 之二個空格為原文，逐字保留。）

**(c) `Body Off HU System Sleep Mode` —— 與 CFTS022 `-113` 逐字同名之處（錨點 `4941238`）**

```
4941238: [Artifact Type:Subsystem Functional Requirement] [State:New] [ECU:ALL]
[Market:All] [Model Year:2017] [Radio:allSys] [EE Architecture:PowerNet, CUSW]
In the system transitions to the Body OFF mode, the A&T system shall go into
Standby Mode and then if there is no CAN-I and no CAN-C activity, the A&T system
shall go to Body Off HU System Sleep Mode.
```

**(d) BODY OFF MODE GROUP 之二子態（§1.3.1.11.3.1，錨點 `4941073`~`4941077`）**

```
1.3.1.11.3.1 BODY OFF MODE GROUP {4941073}
1.3.1.11.3.1.1 SLEEP MODE {4941074}

4941075: […]
The system is connected to power. All network connections are not active.The HU
and A&T module shall keep the CAN transceiver in “standby mode” to detect CAN
activity.
1.3.1.11.3.1.2 STANDBY MODE {4941076}

4941077: […]
This mode shall exist for all modules when the Body CAN is active or awake but
the system is still in Body OFF mode. If the system detects low voltage, the
system shall be active in this state as long as the module's main CPU and the
connected hardware is operating.If the CAN transceiver detects CAN activity on
Body CAN, the HU CPU shall wake up.
```

**(e) 喚醒之條件（§1.3.3，錨點 `4941096`~`4941100`）**

```
1.3.3 System Wake Up and Power Up Conditions {4941096}

4941098: [Artifact Type:Description] […]
There are several conditions that will cause the A&T system to transition from
Sleep Mode to Standby Mode. The following sections define the conditions.
1.3.3.1 STANDBY MODE {4941099}

4941100: […]
With the Body Off mode and CAN bus activity is initiated by any CAN module, all
modules shall wake up and shall initiate a transition to Standby Mode.

4941103: […]
Within 400 msec of wakeup mode, each module shall broadcast all periodic messages
with the determined states that have been either recalled or detected.
```

**(f) TLM 側之 Sleep（§1.6.2.1.7，錨點 `4941415`~`4941420`）**

```
1.6.2.1.7 Sleep {4941415}

4941416: […] In the following "Ignition Working Conditions": Ignition Pre Off,
Ignition Off,
4941417: […] This status is related to TLM OFF with Network off
4941418: […] No TLM, FPDM AMP, ICS, and DTV functionality is available.
4941419: […] Entering this state, TLM has to set Antitheft_Activation.Req to
"False" value.
4941420: […] Audio and Telematic modules shall be in this mode when they receive
$Telematic_Power$ = [Sleep].
```

### 6.3 ⚠ power 線**已裁之施加式**：查無

R-DD20(b) 書「只得**逐字取自 power 線已裁之施加式**（含訊號名、值、格式）」。
**逐字傾印該線七批已產出 TC 之全部 `test_procedure` 步驟**（母體見 §九-2），
狀態進入之步驟**全為通稱式，無一則帶訊號名／值／格式**：

```
  7  Bring the HU to Timed mode while the event listed in Input Test Data holds
  5  Bring the TLM to the status related to TLM audio is OFF
  4  Bring the HU through a startup that plays the animation
  4  Bring the HU through the event listed in Input Test Data
  3  Bring the HU through the startup sequence
  2  Bring the TLM through the switch on sequence
  2  Bring the TLM to the status related to TLM OFF with Network on
  2  Bring the TLM to the status related to TLM OFF with Network off
  2  Bring the HU through an Ignition On
  1  Bring the HU through a normal power down sequence
  1  Power up the TLM for the first time
  1  Set the boot target status to Standby and start the suspend-resume boot sequence
  1  Set the boot target status to Bench and start the suspend-resume boot sequence
```

**且 `Body OFF` 之 sleep／wake 在該線無任何施加步驟。**
`Body OFF` 於該線之七則 TC 中**只作為狀態陳述**（`pre_conditions`），逐字：

```
1. A LIN and CAN simulation tool is connected
2. The HU transitions to Standby mode as the vehicle enters Body OFF mode
```

**結論（僅陳述，不裁）**：**R-DD20(b) 目前無可逐字取用之施加式。**
可取者為 §6.2 之 CFTS009 原文（`$PowerMode$` 之五值），
但那是**規格定義**，非 power 線**已裁之步驟寫法** —— 二者不同，
**本輪不代分析層決定可否等同**。包 17 之規格須據此重定。

### 6.4 **觀察式** —— `TLM_Status.Info` 之讀式（逐字，含出現次數）

power 線七批已交付 TC 中之全部形式（`test_procedure` 之讀式 ／ `expected_result` 之斷言）：

```
── pre_conditions（起始狀態之陳述式）
 19  TLM_Status.Info and $Telematic_Power$ read "Timed"
 13  TLM_Status.Info and $Telematic_Power$ read "Idle"
 11  TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
  8  TLM_Status.Info and $Telematic_Power$ read "Standby"
  5  TLM_Status.Info and $Telematic_Power$ read "Sleep"
  4  TLM_Status.Info and $Telematic_Power$ read "Partial Operation"
  2  TLM_Status.Info reads "Full-Operation" entered through a call
  2  TLM_Status.Info was equal to "Full-Operation"

── test_procedure（讀式）
  7  Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
  4  Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
  4  Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
  4  Read TLM_Status.Info to check that Timed state is kept
  3  Read TLM_Status.Info and the TLM state to check the transition to Standby
  3  Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
  3  Read the active functionality and TLM_Status.Info to check the transition to Standby
  2  Read TLM_Status.Info and the screen to check that the transition is ignored
  2  Read the screen, VPLastStatus and TLM_Status.Info to check the transition
  2  Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition
  2  Read TLM_Status.Info and $Telematic_Power$ to check the transition
  2  Read TLM_Status.Info and $Telematic_Power$ to check the resulting state
  1  Read TLM_Status.Info and the state machine to check the starting state
  1  Read TLM_Status.Info to check whether the transition of this clause occurs
  1  Read TLM_Status.Info to check that Full-Operation state is kept
  1  Read TLM_Status.Info and the screen content to check what the screen shows
  1  Read TLM_Status.Info, $Telematic_Power$ and the active source to check the transition to Timed
  1  Read TLM_Status.Info and $Telematic_Power$ to check the return to Idle
  1  Read RemStartFail and TLM_Status.Info to check the resulting values
  1  Read VPLastStatus, RemStartFail and TLM_Status.Info to check the resulting values
  1  Read the active functionality, RemStartFail, TLM_Status.Info and $Telematic_Power$ to check the transition

── expected_result（斷言式）
  6  TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
  5  TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
  4  VPLastStatus reads "OFF", TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
  4  TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
  4  TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
  4  TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
  3  TLM_Status.Info reads "Standby" and the TLM is in Standby state
  3  RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
  3  VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
  2  TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
  2  TLM_Status.Info and $Telematic_Power$ read "Timed" and the current active source is maintained
  2  TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
  2  TLM_Status.Info still reads "Idle" and no Splash Screen is shown
  1  TLM_Status.Info reads "Sleep" and the TLM starts from Sleep state
  1  TLM_Status.Info reads "Logistic Idle", $Telematic_Power$ reads "Logistic_On" and the TLM passes to Logistic Idle state
  1  TLM_Status.Info does not pass to "Standby" through the transition of this clause
  1  TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM stays there until Phone_Call.Info becomes "Not_Active"
  1  RemStartFail reads "False", TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM is in Standby state
```

**形態（僅描述，不裁）**：讀式一律 `Read TLM_Status.Info …（＋ $Telematic_Power$）to check …`；
斷言式一律 `TLM_Status.Info … read "<狀態>" and the TLM passes to <狀態> state`
（維持不變者用 `still reads`，不轉換者用 `does not pass to`）。
**`TLM_Status.Info` 不加 `$` 而 `$Telematic_Power$` 加 `$`** —— 二者於該線一貫如此。

### 6.5 狀態值域全表（逐字）

**(a) power 線 profile §3.3 之 first-match 走查基準（`FW036_R1L_Power_Profile.md`）**

```
**§12 之 first-match 走查須以 TLM 之具名 status 為準** ——
即 CFTS009 §1.6.2.1.1–.13 所列者（Full-Operation / Idle / Partial Operation /
Stolen Vehicle Mode / Timed / Standby / Sleep / Bench / Logistic Idle / Logistic
Standby / Logistic Sleep / Init ×2）。
不在該清單者（如 Load Shed、Battery Critical）**不構成 State Transition**，
應續往「multiple conditions → outcome」判為決策表。
```

**(b) CFTS009 §1.6.2 之節次（TOC 逐字）**

```
1.6.2.1.1  Full-Operation {4941356}
1.6.2.1.2  Idle {4941363}
1.6.2.1.3  Partial Operation {4941390}
1.6.2.1.4  Stolen Vehicle Mode {4941398}
1.6.2.1.5  Timed {4941401}
1.6.2.1.6  Standby {4941409}
1.6.2.1.7  Sleep {4941415}
1.6.2.1.8  Bench {4941421}
1.6.2.1.9  Logistic Idle {4941425}
1.6.2.1.10 Logistic Standby {4941430}
1.6.2.1.11 Logistic Sleep {4941433}
1.6.2.1.12 Init {4941436}
1.6.2.1.13 TLM initialization: Init state {4941440}
1.6.2.1.15 TLM_Status.Info and $Telematic_Power$ signal setting {4941460}
```

**(c) §1.3.1 之 A&T 系統電源模式節次（TOC 逐字）**

```
1.3.1.1  BODY OFF and BODY ON MODE GROUPS {4941023}
1.3.1.2  SLEEP MODE {4941031}
1.3.1.3  STANDBY MODE {4941036}
1.3.1.4  IDLE MODE {4941038}
1.3.1.5  FULL OPERATION MODE {4941041}
1.3.1.6  PARTIAL OPERATION MODE {4941043}
1.3.1.7  STOLEN VEHICLE MODE {4941050}
1.3.1.8  TIMED MODE {4941053}
1.3.1.9  BENCH MODE {4941060}
1.3.1.10 LOGISTICS MODE {4941062}
1.3.1.11 HU State Chart (Common Power Management State-Chart) {4941066}
```

> **⚠ 一件要說清楚的**：`BODY OFF` 在 CFTS009 中是**車輛側之 body power mode**
> （由 `$PowerMode$` 定義，§6.2-a），
> 而 §6.5(a)(b) 之十三個具名 status 是 **TLM 之 operative state**。
> **`Body OFF` 不在該十三個之內。**
> 本輪**不判**二者是否為 R-DD20(a) 所稱之「同一電源域概念」——
> 只指出**它們在來源中分屬兩個層級的清單**，供分析層於包 17 前一併看。

### 6.6 本節之拘束遵行

- **只讀**：power 線與 profile 之檔**未寫入一字**（`git status` 對 `features/power/`
  與 `docs/runtime/profiles/` 無變更）。
- **不判同一性**：§6.1 只報計數與位置，§6.5 只指出層級之別，**未下任何等同或不等同之結論**。
- **不代擬 TC**：本節無任何 `test_procedure`／`expected_result` 之草擬；
  §6.3／§6.4 所列者**全為 power 線既有產物之逐字傾印**，非本線所編。

---

## 七、未結 DR 清單（DD1–DD9）

| DR | 標的 | 狀態 | 等級 | 阻斷之範圍 | 台帳項 |
|---|---|---|---|---|---|
| **DR-DD1** | 037 作者／上游 | **DRAFTED**（改稿含 SYSAD 引文）| **必發** | `-025`~`-028`（4）**仍凍結** | A-DD1 |
| DR-DD2 | 上游（CFTS022 作者）| DRAFTED（格式更正件）| 緩發 | 不阻斷（R-DD18 已採勘誤）| A-DD2 |
| ~~DR-DD3~~ | — | **RESOLVED**（包 13 §二）| — | — | ~~A-DD5~~ |
| DR-DD4 | 上游 | PARTIALLY ANSWERED／縮為一問 | 緩發 | 不阻斷 | A-DD6 |
| **DR-DD5** | LID 維護者 | **DRAFTED** | **必發** | **已由 R-DD19 乙案解凍**；回覆不符 → 8 TC 機械換值 | A-DD8 |
| **DR-DD6** | CFTS022 作者 | **DRAFTED** | **必發** | 同上；`MTA(2)`／`DDCT(3)` 仍為硬邊界 | A-DD9 |
| DR-DD7 | 037 作者 | DRAFTED（品質旗標）| 緩發 | 不阻斷 | A-DD7 |
| **DR-DD8** | CFTS022 作者／素材 | **DRAFTED（本輪建檔）** | **必發** | `-120`／`-121` 之負向側 | **[CG-DD1]** |
| **DR-DD9** | CFTS022／037 作者 | **DRAFTED（本輪建檔）** | **必發** | `-001`／`-002` 之施加識別碼與 process 名 | **A-DD10** |

**八筆未發送**（DD1／DD2／DD4／DD5／DD6／DD7／DD8／DD9）；**DD3 已結案**。

### 7.1 阻斷疊圖（本輪後）

| leaf | 狀態 | 未結之阻斷 |
|---|---|---|
| `-001`／`-002` | **未生成**（下放包 16 §八，待包 17 規格）| DR-DD9（marker 生成已裁准，惟施加式無來源 —— §6.3）|
| `-003`~`-016` | 已產出（pilot 4 ＋ B1 10）| 無阻斷；DD4 為品質旗標 |
| `-017`~`-024` | 已產出（B2 8）| DD5／DD6（marker）、**DD8**（`-021`~`-024` 之負向側）|
| `-025`~`-028` | **凍結** | **DR-DD1**（乙案／丁案皆不及於此）|
| `-013`／`-015` | 已產出 | **[CG-DD1] ＋ DD8**（負向側未涵蓋）|

**28 leaf 中 22 則已產出、2 則待包 17、4 則凍結。**

---

## 八、獨立自評

### 8.1 我做對的

1. **D8 修到判斷層，不只修字串。** 下放包只要求 detail 由 `SC_ARTIFACT` 導出。
   照字面做就是把五行 f-string 改掉、三產物重跑、全綠交差。
   **但改檢 11 的 detail 時必須知道 `ff` 是怎麼算的，一看就發現那個條件恆為偽。**
   `items()` 以 `^\d+\.` 切分，故 `items(...)[0]` 必以 `1.` 起首，`not re.search(r"^1\.", …)`
   永遠是 `False`。**那個檢從寫下的那天起沒攔過任何東西。**
2. **舊檢／新檢並列跑同一注入。** 只報「新檢紅了」證不了修復有價值 ——
   **要證的是「這個紅是新的」**。七組並列跑下來，A 與 B 是舊綠新紅，
   其餘五組舊新皆紅（即修復未換出漏洞）。**兩個方向都要證。**
3. **T22b 取甲案而非乙案。** 使 `0` 變紅（乙案）比較省事，但那是把一個**正確的產物**
   判成錯的 —— `0 (0.0000 km/h)` 依 R-DD9(b) 本來就對。
   **問題不在那個值，在那個值是靠白名單過的。** 甲案把規則寫明後，
   129／77／0 三者由同一條規則涵蓋，而不是「兩個在表裡、一個在後門」。
4. **T22c 沒有把查無報成查到。** R-DD20(b) 要「逐字取自 power 線已裁之施加式」，
   而該線**根本沒有帶訊號名的狀態進入步驟**。此時最省事的是把 CFTS009 §6.2 的
   `$PowerMode$ = [IGN_LK]` 當成「已裁之施加式」交上去 —— **但那是規格定義，
   不是該線裁過的步驟寫法**。二者之別正是 R-DD20(b) 立條的理由（不繞過其裁定史）。
5. **A-DD10 之採認基礎與實測不符，照報。** 條文剛落、marker 剛立就報「其依據數不對」，
   讀起來像在拆自己剛做的事。但 §6.1 之三個計數是機械可覆算的。
   **記在 A-DD10 條目裡而非只寫在上繳包**，是因為將來讀該 marker 的人未必讀這份包。

### 8.2 我做糙的

1. **`RE_ACCESS` 之動詞聯集是我列的，不是量出來的。**
   `(open|start|select|play|enter|launch)` —— power 線之 profile §3.1 對同類判準
   是「自已交付 `test_procedure` 取行首動詞聯集，再以 1823 行量偽陽性」。
   我沒做那個量。本 feature 三產物之步驟起首動詞只有 `Open`／`Read`／`Select`／
   `Send`／`Start`／`Stop`（見 §3.3 檢 8 之 detail），故現況無偽陰性；
   **但這是「碰巧夠用」，不是「量過」。**
2. **檢 8 之「描述部」判準偏弱。** 現只驗「item 之首行不得即為 `$` 指令」，
   未驗描述部之內容。因本 feature 至今 0 個 CLI 步驟，此檢仍為 N/A，
   **等於是為 `-002` 之 `PENDING: DR-DD9 <…>` 預先鋪的路，尚未被真正行使過。**
3. **單位比對放寬為不分大小寫。** DBC 為 `"Km/h"`、產物依 profile 書 `km/h`。
   嚴格逐字會讓三產物全紅。放寬是對的，**但它是本次唯一的寬鬆處，
   而寬鬆處就是下一個後門的位置** —— 故明記於 §5.2 而非藏在程式碼裡。
4. **`RE_ENUM`（FP 之列舉支援項偵測）同樣是列的。**
   `format|device|protocol|codec|container` 五詞，0 命中。
   **0 命中之檢與不存在之檢，在輸出上長得一樣。** 這是它比前一版好、但仍不夠好的地方。

### 8.3 我拒絕做的

1. **不判 `Body OFF` 與 `Body Off HU System Sleep Mode` 是否同一。**
   T22c 明文「不判同一性」。材料在 §6.2／§6.5，判斷屬分析層。
2. **不代擬 `-001`／`-002`。** 即使 §6.2 之 `$PowerMode$ = [IGN_LK]` 看起來足以寫出步驟。
3. **不改 A-DD10 之狀態、不改 R-DD20 之條文。** 採認基礎之計數不符是事實，
   **但改條是分析層的事**；執行層只記明。
4. **不寫 `docs/fw036/RULINGS.sha.tsv`。** 那是共用路徑，且「tsv」在下放包 16 §八之
   排除清單內。試跑後已還原（§一）。
5. **不逕改 [CG-DD1] 之影響 leaf 範圍。** `-013`／`-015` 與 `-021`~`-024` 同源於一張表，
   但範圍之認定屬分析層。

### 8.4 一件我原本會漏的

**檢 9 走錯分支這件事，我原本只會改檢 11。**

D8 列的是「檢 3／4／8／11／13」，檢 9 明文列在「已導出」那一側 ——
因為它的 detail **確實**是逐 TC 生成的（`d9.append(f"{k}: …")`）。
改檢 11 時要判 fault 集合，順手把 `leaf in ("010","012")` 搜了一遍，
才看到檢 9 用的是同一個硬編。

**它的 detail 是導出的，它的分支是硬編的。**
於是 B1／B2 的九則 fault 列全部落到 else 分支，被當成一般列去驗
「PC 有 `at 0 (0.0000 km/h)`」—— **而它們的 PC 確實有那一行，所以全綠。**

> **「detail 導出」與「判斷正確」是兩個獨立的性質。**
> D8 之判準抓的是前者，而前者為真時後者仍可為假 ——
> 檢 9 就是這個組合。**下一次的分類，判準要分兩欄，不能只問 detail 從哪來。**

---

## 九、量測條件揭露（R-G8）

### 9.1 本包所書比率與計數之分子與分母

| 所書 | 分子 | 分母 | 命令／方法 |
|---|---|---|---|
| 「24 PASS ／ 2 N/A ／ 0 FAIL」×3 | 各檢之 verdict | 26 檢（IN §9 十七項 ＋ 追加 9 項）| `SC_ARTIFACT=<檔> python3 scripts/selfcheck_tcs.py` |
| 「B1／B2 之九則 fault 列」 | `is_fault(tc)` 為真者 | B1 10 則 ＋ B2 8 則 | `RE_FAULT = Stop transmitting\|timeout`（不分大小寫）對 `test_procedure` |
| 「錨點 21」 | `^## R-DD` 之行數 | `features/driver_distraction/RULINGS.md` | `grep -c '^## R-DD'` |
| 「索引現行 20」 | `^\| R-DD` 之行數 | 同上 | `grep -c '^\| R-DD'` |
| 「逐字元差異 0」×4 | 落檔字串 vs 下放包字串 | R-DD20 961／A-DD10 197／DR-DD8 1312／DR-DD9 1254 字元 | Python 字串全等比對 |
| 溯源分布（§5.3）| `prov` 之 `Counter` | 四交付欄中所有 `= <raw> (<label>)` 命中 | 檢 12 之 detail |

### 9.2 §6.1 之計數 —— 命令與母體

```
# RULINGS 之 BODY OFF（去 -TIMED）
grep -oiE 'body off(-timed)?' features/power/RULINGS.md | grep -vi timed | wc -l      → 0
grep -oiE 'body off-timed'     features/power/RULINGS.md                     | wc -l  → 11
# profile
grep -oiE 'body off(-timed)?' docs/runtime/profiles/FW036_R1L_Power_Profile.md | wc -l → 0
# power 線全線（遞迴，含 data/ generated/ scripts/ docs/）
grep -rhoiE 'body off(-timed)?' features/power | grep -vi timed | wc -l               → 86
```

**母體之界**：`features/power/` 之全部檔（不含 `.git`），
`features/power_moding/`、`docs/runtime/profiles/` 之二個 power profile 另計。
**未包含**：`features/power/inputs/` 之二進位規格檔本身（`.docx`／`.pdf`／`.xlsx`）——
其文字層已轉出於 `data/textlayer/`，本次以文字層為母體。

### 9.3 §6.3／§6.4 之母體

power 線 `generated/*.json` 之 **7 檔**（`batch_001`~`batch_007`），
取每檔 `tcs[]` 之 `pre_conditions`／`test_procedure`／`expected_result`，
逐行去編號後計數。**未含該線 `data/` 之取樣檔與 `delivered/`**（避免同一 TC 重複計）。

### 9.4 §四之注入條件

- 注入檔寫於 `features/driver_distraction/generated/inj_*.json`，**每組跑完即 `os.remove`**；
  跑後 `ls generated/` 僅餘三個正式產物（已核）。
- 舊檢之副本置於 `scripts/_sc_old_tmp.py`，**跑完即刪**（已核）。
- 二者皆以同一 `SC_ARTIFACT` 值餵入，**除腳本外無其他差異**。

### 9.5 本輪未量測者

1. **`RE_ACCESS`／`RE_ENUM` 之偽陽／偽陰率**（§8.2-1／8.2-4）—— 未量。
2. **`-001`／`-002` 之任何面** —— 本輪未生成，故無量測。
3. **寫回工作簿之任何面** —— 本輪未寫回。
4. **power 線之 `delivered/`** —— 未納入 §6.3／§6.4 之母體。
5. **CFTS022 r114 之逐字**（R-DD20(a) 之另一半採認基礎）——
   §6.1 只測了 power 線那一半；**CFTS022 側未測**，故該表無此列。

---

## 十、待分析層／Pei

| # | 事項 | 為何須分析層 |
|---|---|---|
| **10-1** | **R-DD20(a) 之「power 線 RULINGS 之 78 處命中」與實測不符**（§6.1）—— 逐字同名在 CFTS009 文字層 `4941238`，非在 RULINGS | 條文之修訂屬分析層；A-DD10 之採認基礎是否隨之改述，須裁 |
| **10-2** | **R-DD20(b) 目前無可逐字取用之施加式**（§6.3）—— power 線之狀態進入步驟全為通稱式 | 包 17 之規格前提；可否改以 CFTS009 §6.2 之 `$PowerMode$` 五值為施加式，須裁（執行層不代決） |
| **10-3** | **`Body OFF` 不在 TLM 十三個具名 status 之內**（§6.5）—— 二者分屬車輛側 body power mode 與 TLM operative state | 同一性之判斷屬分析層（T22c 明文不判）|
| **10-4** | **`RULINGS.sha.tsv` 落後一條**（§一）—— R-DD19 自上輪起未入台帳 | 「tsv 不在本輪」與「停止條件 2 之值須同步」二拘束相衝，須裁孰先 |
| **10-5** | **[CG-DD1] 之影響 leaf 範圍**（§2.3）—— `-013`／`-015` 與 `-021`~`-024` 同源於同一張表 | 範圍之認定屬分析層 |
| 10-6 | §8.2 之四項自認（動詞聯集未量、檢 8 判準偏弱、單位放寬、`RE_ENUM` 未量）| 是否要求補量，屬分析層 |

**本輪未動**：`generated/*.json`（產物本體）、工作簿、git、`docs/fw036/`、
`features/power/`、`docs/runtime/profiles/`。
