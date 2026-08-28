# 上繳包 03 — Popup pilot 修正、-002-05 補生成、工具二修、台帳一致性

日期：2026-08-28
Feature slug：`popup`
對應下放：[handoff/03_pilot_fixes.md](../handoff/03_pilot_fixes.md)
執行層：Claude（Opus 5）

**總判：作業面完成，交付面 5/5 條齊；`gate_all.py` 五支中三支我方相關者全綠，
兩支紅為本包外之既存紅（逐支歸因見 §八）。§十 升級條件命中一項（§六-2），
已停下回報未代改。§三第 1 項之標的不存在，未自為（§一）。**

---

## 一、下放包本身之三處與 repo 不符（先行揭露，未自行改寫指令）

### 1. §三「`feature.yaml` 之 `project` 模板殘值 `PROJ` → 正確值」—— 標的不存在

實測（2026-08-28）：

```
$ grep -rn 'PROJ' features/popup/feature.yaml
（命中 0）
$ grep -rn 'PROJ' features/popup/ --include='*.yaml' --include='*.json' --include='*.py'
（命中 0）
```

`features/popup/feature.yaml` **無 `project` 鍵**，全檔亦無 `PROJ` 字串。
repo 內 `PROJ` 之全部命中為三處**對此事之敘述本身**（`RULINGS.md:134`
R-POP13 條文、`ANOMALIES.md` A-POP9 主表列、下放包 03 §三／§八）。

**歸因**：此項承接 A-POP9 第 (4) 點所記之錯誤述值（上繳包 02 曾稱前綴為
`PROJ-POP-*`，語料實為 `newR1L-POP-*`）。R-POP13 之條文把該錯誤述值連同
處分一起寫了進去 —— **A-POP9 之錯誤在其自身之處分條文內再現一次**。

**處置**：未造 `project` 鍵，未改寫指令。已將本節之實測寫入
`ANOMALIES.md` 之 A-POP9 §四。`tc_id_format` 之改值照做（見 §三）。

### 2. §三「重排後全簿掃 `newR1L`／`PROJ`／`POP-`，命中須為 0」—— 後二項不可達成

全簿逐格掃（`openpyxl`，全 sheet 全格，字串子字串比對）：

| 字串 | 全簿命中 | 命中處 | 判 |
|---|---|---|---|
| `newR1L` | **1** | `Test Case Specification 測試用例規範!D2` | **母本自帶**，非本包寫入 |
| `PROJ` | 0 | — | 相符 |
| `POP-` | **5** | 同表 `D10:D14` | **req_id 本體**，須保留 |

- `D2` 之 `newR1L`：母本副本 `sandbox/base/` 實測 `C2 = "專案名稱 Project  Name："`
  ／ `D2 = "newR1L"` —— 即 **D2 為專案名稱欄，其值本來就是 `newR1L`**。
  本包未寫過 D2。清成 0 等於改動母本之專案名稱，逾越本包範圍。
  （順帶：這正說明下放包 02 誤以 D2 為 TC ID 前綴之權威 —— 它是專案名稱欄。）
- `D10:D14` 之 `POP-`：`SWE1-POP-002-01`～`-05`，即 037 之 req_id，
  掃到 0 就代表 req_id 被抹掉了。

**本包採之量測**：`newR1L`／`PROJ` 於**本包產出之語料與儲存格**（`generated/`
＋ `feature.yaml` ＋ 寫入之 F／D／G…AA 欄）命中 **0／0**；
`POP-` 於 **TC ID 欄（F10:F1411）** 命中 **0**。三者見 §八。

### 3. A-POP6 §甲 之計數與其自身表列不符

§甲 標題寫「**4 個 feature，5 筆**」，其表列為 **3 個 feature、4 筆**
（sxm 2 ＋ audio_mgmt 1 ＋ time_management 1）。改判後真陽性為
**2 個 feature、2 筆**（§六-2）。三個數字並陳，未自行改寫 A-POP6。

---

## 二、pilot 六件修正（R-POP15）—— 逐件、逐條

改於 `features/popup/scripts/gen_pilot.py` 之語料，重跑產生
`generated/pilot_01.json`（5 條）。

| # | 修正 | 施於 | 實測 |
|---|---|---|---|
| F1 | Final Step 補 check target | 五條之末步驟 | 5/5 含 `check that`（§八）|
| F2 | 按壓標的改 `"..."`；PU 記法只留 ER 引文段與 test_item；去 Markdown 記號 | POP-002 步驟 1／2、POP-004 步驟 2、全交付欄 | 五交付欄逐 item 掃反引號 **0**（§八）|
| F3 | 刪 `ignition in RUN` 類環境前提 | 四條之 pre_conditions | 全條掃（不分大小寫）**0**（§八）|
| F4 | `input_test_data` 一律 `NA` | POP-001／003／004（002 原即 `NA`）| 5/5 == `NA`（§八）|
| F5 | reasoning 之 anomaly 號 live 查後改寫 | POP-002 | 見下 |
| F6 | POP-002 之 reasoning 改為 R-POP12 之理由 | POP-002 | 見下 |

### F1 之逐條落法（不是同一句話貼五遍）

各條之 check target 取該條自己的可觀察結果，且**與該條 ER 3 同義**：

- POP-001：`… and check that the pop-up has closed by itself 5 seconds after
  it appeared, matching the Time-out defined by PU0942 Timeout (sec)`
- POP-002：`… and check that the pop-up is no longer displayed`
- POP-003：`… and check that the pop-up is no longer displayed, before the
  5-second Time-out defined by PU0580 Timeout (sec) has elapsed`
- POP-004：同形，`3-second` ／ `PU0949`
- POP-005：`… and check that the pop-up is still displayed`（**否定命題**）

### F2 之界（PU 記法保留與否，逐處）

| 處 | 保留 `<...>` | 實例 |
|---|---|---|
| test_item 下半 | **是** | `(Second press of the opening control <Trks>, PU0215)` |
| ER 引文段 | **是** | `The second press lands on the same "<Trks>" button …` |
| Procedure 按壓標的 | **否**，改雙引號 | `press the Track list button "Trks"` ／ `press "OK" inside the pop-up` |

反引號一律移除；原以反引號界定之引文改雙引號（`"<X>"`、`"Page added! [Reorder]"`、
`"Tracks List"`、`"No Phone is Connected.        <OK>    <X>"`）。
POP-003 之 ER 1 原引文自身即含雙引號（`"Welcome [username]", "X"`），
故只去反引號、不再加一層。

### F3 之連帶（逐條複驗，未機械套用）

| 條 | 刪後 pre_conditions | 是否足以執行 |
|---|---|---|
| POP-001 | 1 項（Home Screen 顯示中）| 足 —— 觸發路徑為新增 home screen 頁，無其他前提 |
| POP-002 | 2 項（有 track list 之媒體來源、Media 畫面）| 足 |
| POP-003 | 2 項（≥2 個 Profile、All Profiles tab 可達）| 足 —— **此二項保留**，係本 TC 之規格觸發前提，非環境穩定性 |
| POP-004 | 2 項（未配對手機、Shortcuts 畫面）| 足 —— 「未配對」是 PU0949 Description 明載之觸發條件 |

**無一條因 F3 而前提不足**（§十第 2 項升級條件未命中）。

### F4 之連帶

- POP-001：`Time-out = 5 s` 已於 Procedure 步驟 3 與 ER 3 具名並註明
  出處欄位（`PU0942 Timeout (sec)`），改 `NA` 不損失資訊
- POP-003／004：同形（`PU0580`／`PU0949`）
- 五條皆 `NA`，與 SWC 基準 285/286 同

### F5／F6（POP-002 之 reasoning）

**live 查之結果**（`features/popup/ANOMALIES.md`，2026-08-28）：
device 軸該件為 **A-POP7**，狀態 **RESOLVED（R-POP12）**。
原語料「登 A-POP7」寫在 A-POP7 本身之敘述裡，為參照循環。

改寫後之 reasoning **不再引任何 anomaly 號**，改以 R-POP12 之理由陳述：

> **device 軸不拆，理由為規格側無此分支**（R-POP12，2026-08-27）：
> SYS1 5.6 逐字 `pressing the button a second time`，未區分按鍵型別；
> 037 S11 之 `a physical hard button or a specific UI button on the screen`
> 是 VC 對「button」之列舉性註解，非規格分支，037 本身亦未拆為兩個 sub-id。
> 依 IN §8.2 與 §8.4.2，判一條 TC。
> **本條不主張「軸為真而缺實例」** —— 該說蘊含「欠一條待補件」，為 R-POP12 所否決。

「真軸但無實例」一說（含 PU0229 之候選推論）**全數刪除**。

---

## 三、TC ID 重排（R-POP13）

`feature.yaml`：`tc_id_format` 由 `"newR1L-POP-{n:03d}"` 改為
`"NR1L-Popup-{n:03d}"`，並改寫其上方註解 —— 原註解稱「project 前綴之權威
為工作簿 D2」，該說已由 §一-2 之實測否定（D2 是專案名稱欄），註解改記
R-POP13 之依據與「不取 D2」之理由。

重排結果（NNN 序不變）：

| 舊 | 新 | req_id |
|---|---|---|
| `newR1L-POP-001` | `NR1L-Popup-001` | SWE1-POP-002-01 |
| `newR1L-POP-002` | `NR1L-Popup-002` | SWE1-POP-002-02 |
| `newR1L-POP-003` | `NR1L-Popup-003` | SWE1-POP-002-03 |
| `newR1L-POP-004` | `NR1L-Popup-004` | SWE1-POP-002-04 |
| （未生成）| `NR1L-Popup-005` | SWE1-POP-002-05 |

工作簿 `F10:F14` 回讀實測即上表右欄。掃描結果見 §一-2 與 §八。

---

## 四、`-002-05` 補生成（R-POP14）

### 生成過程未遇造值，未停下

§十第 1 項升級條件（「生成須造值 → 停下」）**未命中**。全部欄位皆有來源：

| 欄 | 來源 |
|---|---|
| test_item 上半 | 037 `Analysis Report` 第 14 列 E 欄 **verbatim** |
| test_item 下半 | 作者生成之情境標籤（IN §4.3.1），見下 |
| pre_conditions | GP4-4 之 `allows the user to perform more than 1 task` ＋ 037 S11 Precondition `A functionality that will trigger pop-up with multi task is ready` |
| test_procedure | 037 S11 Action 逐字 `Tap the button (or interactive component) that is not suppose close pop-up` |
| expected_result | 037 S11 Expected Result 逐字 `The pop-up should not be closed` |
| input_test_data | `NA`（R-POP15 F4）|
| spec_reference | 單行 `…_5.6` |

037 第 14 列 E 欄逐字（本包所引之原句）：

> `Exceptions when the popup allows the user to perform more than 1 task- e.g in the search keyboard only X button 'close', any other buttons do not close the popup`

### 四項禁令之遵行，逐項

1. **不引 PU** —— `pu_citation` 為 `null`（§八 實測 1 條）。
   `verify_pu_quotes()` 對本條略過（無引文可驗），輸出明記
   `不引 PU 者 1 條：SWE1-POP-002-05`
2. **不落 PENDING** —— 全簿 `PENDING:` 命中 0（§八）
3. **不列舉 search keyboard 以外之實例** —— 全條文字內
   `PU0022`／`PU0023`／`PU0861` 命中 0；procedure 之措辭為
   `the pop-up that allows the user to perform more than 1 task`，
   **不指名任何具體 popup**
4. **不宣稱鍵盤實例為某具名 PU** —— `search keyboard` 只出現於
   pre_conditions 之 `the search keyboard being the example given in the
   requirement` 與 test_item 之 037 原句內，兩處皆以「規格之舉例」措辭呈現

### test_item 下半之可區分性（IN §4.3.1）

五條之括號段兩兩相異：

| 條 | 下半 |
|---|---|
| 001 | `(Time-out closure of PU0942, 5 s)` |
| 002 | `(Second press of the opening control <Trks>, PU0215)` |
| 003 | `(Touch outside the pop-up bounds, PU0580)` |
| 004 | `(Selection <OK> inside the pop-up, PU0949)` |
| 005 | `(Non-closing control inside a multi-task pop-up; no PU cited)` |

005 之下半刻意寫 `no PU cited` —— 其餘四條皆以 PU id 收尾，本條沒有，
若不寫明，讀者會以為漏了。

### 一項獨立判斷（揭露，非裁定）

`design_method` 取 **狀態轉換** 而非 **負向測試**。理由：受測者是同一台
popup 狀態機在特定輸入下**不發生轉移**，與 -002-01～04 同機同族，五條同法
可對讀。**負向測試曾列為候補**，此處記明以備 Pei 改裁。

---

## 五、工具二修

### 5.1 `scripts/lint_docs036.py`（R-POP16 乙／丙）

**改動**：

1. `Finding` 增 `severity`（`red`／`note`）；`--gate` 只計 red
2. `series_in()` 前綴抽取限定**檔內首個表格**，編號仍跨全檔收集並併記表序；
   回傳值增第三項「合系列形態但前綴不在主表而略過之數」
3. `check_series()` 之 `編號重複`：同表內重複 → red；跨表同號 → note。
   **降 note 後仍算「該號存在」**，不因此生出新的跳號誤報
4. `main()` 於抽得前綴集為空時明示 `no series detected …（G-D 盲區；PASS ≠ 已驗）`，
   且 PASS 那一行加註「**未涵蓋任何條目**」

**迴歸 (a)（放寬向，G-K）—— 三者逐一實證：**

| 對象 | 改前 | 改後 |
|---|---|---|
| `power_moding` `DR-PMH1` | `[DR-PMH_id] DR-PMH1：編號重複`（red，1 項）| **note**，`--gate` exit **0**（另 DR-PMH2／3／5 同型，共 4 note）|
| `projection` `A-PJ37` | `[A-PJ_id] A-PJ37：編號重複`（red）| **消失**（該檔主表非登記表，整檔不受檢，明示 `no series detected`）|
| `privacy` 假前綴 `S` | 前綴集 `['S']` | 前綴集 `（無）` —— **`S` 已排除**，明示 `no series detected` |

**迴歸 (b)（注入向，G-N）—— 只放寬跨表，真重複仍紅：**

於 scratch 副本（`$SCRATCH/inj/`，`popup` 三簿）之 **ANOMALIES.md 主表內**
複製 `| A-POP9 | … |` 一列（第 19 行後），其餘不動：

```
== 注入前 ==  docs_structure：PASS（台帳＋popup 之 DR／ANOMALIES）        --gate exit=0
== 注入後 ==  docs_structure：1 項
              [A-POP_id] A-POP9：編號重複（同一表格內）                   --gate exit=1
```

**判準未過寬**（§十第 3 項升級條件未命中）。

**單元測試**：`tests/test_lint_docs036.py` 增 6 支（fixture 逐字釘死，G-N）——
跨表降 note／同表仍紅／降 note 不生跳號／假前綴不入集且報數／
`no series detected` 兩向。**17 → 23 支全綠。**

### 5.2 `scripts/ledger_xref.py`（R-POP17 第 2 項）—— **新建，非改既有**

**判斷揭露**：既有 `features/vehicle_category/scripts/ledger_xref.py` 之
`ROOT` 硬綁該 feature，且其標的是「同一標的之多處記載並列供人判讀」
（自陳不偵測矛盾）。本檢要的是**機械可判之對照**且須跨 feature 通用。
改它 = 把 popup 之需求塞進他 feature 之腳本（違 R-POP16 甲之單一擁有者
原則），故**另立 `scripts/ledger_xref.py`**。二者是否合併屬全域政策，留待 Pei。

**三檢**：

| 檢 | 判準 |
|---|---|
| `unknown_id` | 下放／上繳包與 `RULINGS.md` 內之 `A-<F>n`／`DR-<F>n` 引用，須實存於該 feature 台帳 |
| `pairing` | `RULINGS.md` **條文標題列**所掛之 anomaly／DR 號，其台帳列之處分欄須回指同一條 |
| `ledger_shape` | 於採明細節體例之台帳內，每一號須有 `## <id>` 節，反之亦然 |

**盲區明說**（寫在檔頭）：`pairing` 只掃 `RULINGS.md` 之 `### R-…` 標題列。
下放／上繳包正文常在同一行並列多個無隸屬關係之號碼（如下放包 03 §一之
「已更正為 A-POP7／A-POP9／A-POP8…寫入 R-POP15 F5」），以行配對即爆假陽性。
他 feature 之號碼一律不對照，只報數。

**G-N 固定案例（缺陷原文字面入測）**：`tests/test_ledger_xref.py` 之
`RULINGS_DEFECT` 逐字釘入

```
### R-POP12 — -002-02 不拆，軸不存在（分析層裁 [DEFAULT]，2026-08-27，**A-POP6**）
```

配一本 A-POP6 由 R-POP16 處分、A-POP7 由 R-POP12 處分之台帳，
`pairing` 須命中且訊息含 `R-POP12`／`A-POP6`／`R-POP16`；
同 fixture 改掛 `A-POP7` 後須沉默。**9 支全綠。**

**首跑即抓到兩件 repo 現行缺陷（非造出來的案例）**：

```
[ledger_shape] A-POP9：台帳有列（下放包 02 之上繳回報與 repo 台帳於四點…）而無 `## A-POP9` 明細節
[pairing]      features/popup/RULINGS.md:118：R-POP13 之標題掛 A-POP9，
               但台帳 A-POP9 之處分欄載為 R-POP17 —— 兩處不相認
```

處置見 §七。修後 `ledger_xref --feature popup`：**PASS**。

**開發中被本工具逼出之三次判準修正**（記錄，因為每一次都是差點出貨的誤報）：

1. 處分條號原自整列取 → 「內容」欄裡順帶提到的條號被當成處分。改為**只自
   狀態欄取**，欄位以表頭字面定位（各 feature 欄序不一）
2. 號碼原只自首個表格取 → `features/power/ANOMALIES.md` 之 A-PW 主表被空行
   切成多段，一次生出 **640 筆假 `unknown_id`**。改為**跨全檔所有表格收集**
   —— 存在性不需要先認定哪張是主表（與 `lint_docs036` 之限主表刻意不同，
   兩者問的問題不同，檔頭已記其分野）
3. 只認 `## A-POPn` 式標題 → `audio_mgmt`／`driver_distraction` 之
   `## [A-AM01]` 式整本抽不到，129／101 筆假 `unknown_id`。改為兩式皆認，
   並加「該類台帳整本抽不到號碼時不判 `unknown_id`，改報 G-D 盲區 note」

**跨 feature 唯讀掃描（僅供參考，未代改任何 feature）**：

| feature | 結果 | feature | 結果 |
|---|---|---|---|
| popup | **PASS** | power | **PASS** |
| privacy | **PASS** | sxm | **PASS** |
| sw_update | **PASS** | bed_lowering | **PASS** |
| power_moding | 7 | driver_distraction | 7 |
| projection | 24 | time_management | 29 |
| audio_mgmt | 43 | vehicle_setting | 473 |

**本工具未接入 `gate_all.py`** —— 下放包未令，且以上數字表示接入即全 repo 轉紅。
是否接入、以哪些 feature 為基線，屬全域政策，待 Pei。

---

## 六、R-POP16 甲之清單（只造不改）

### 6.1 已寫入（2 筆，逐筆先複驗）

寫入前對各該 feature 之台帳複驗（表格首格 ＋ `## [A-XXnn]` 標題式兩式併計）：

| feature | 號 | 複驗 | 落點 |
|---|---|---|---|
| audio_mgmt | `DR-AM7` | 實存 1–6、8，**缺 7**；`RULINGS.md:238` 另有「A-AM07 ／ DR-AM7（分析層提出，Pei 裁發）」→ 該號曾被使用而未回登 | **新建** `features/audio_mgmt/BACKLOG.md` B1 |
| time_management | `A-TM2` | 全檔字串命中 **0** | **新建** `features/time_management/BACKLOG.md` B1 |

兩檔皆註明「由 popup R-POP10 之前綴自動抽取浮現，2026-08-27，未代改」。
**兩該 feature 之 `ANOMALIES.md`／`DATA_REQUESTS.md` 本體未動。**

### 6.2 **未寫入（2 筆）—— §十第 5 項升級條件命中**

§十：「甲類清單寫入時發現該 feature 之台帳與 popup 側所見不符（勿代改，回報）」。

| 號 | popup 側所見（A-POP6 甲）| sxm 台帳實況 |
|---|---|---|
| `A-SX18` | 跳號 | `features/sxm/ANOMALIES.md:710` 逐字 ``## [A-SX18] `4872919` restates leaf 120's score-update branch and contradicts it — RESOLVED: 4872918 governs (2026-08-11)`` |
| `A-SX19` | 跳號 | `features/sxm/ANOMALIES.md:526` 逐字 `## [A-SX19] Five clauses carry a VR trigger path their 037 titles also declare — RESOLVED: …` |

sxm 之 `A-SX` 實存集為 **1–30 連續，零跳號**。
**兩筆為假陽性** —— A-POP6 甲類係以「只認表格首格」之抽取器所得，
sxm 以標題式登記，整本抽不到，於是表格首格所見之 `{15,16,17,20}` 被當成全集。

**處置**：未寫入 sxm 之 BACKLOG（無事可登），**未建該檔**，未代改 sxm 任何檔。
登記為 **A-POP11**（Tier 1：登記＋提案，不自裁）。

---

## 七、本輪新登之 anomaly（Tier 1，登記＋提案，皆不自裁）

### A-POP10 —— 「首個表格」判準使數個 feature 之台帳整本脫檢

R-POP16 乙之理由逐字為「首個表格為三簿體例之不變量」。**實測不成立**：

| feature | 首個表格之表頭（前 3 欄）| 主表位置 |
|---|---|---|
| popup／power／time_management／power_moding | 登記表 | 第 1 張（成立）|
| sxm | `token group`／`searched in`／`result` | 不在第 1 張 |
| audio_mgmt | `包內所記`／`inputs/ 實際` | 不在第 1 張 |
| projection | `family`／`count`／`leaf id 範圍` | 不在第 1 張 |
| privacy | `SHA256（前 8）`／`size`／`路徑` | 不在第 1 張 |
| power（ANOMALIES）| 是登記表，**但被空行切成多段** | 第 1 段只到 `A-PW99` |

**被丟棄之條數**（新輸出之「合系列形態但前綴不在主表而略過」）：
sxm **4**、audio_mgmt **7**、projection **63**、其餘 0。

**與 §五-1 所令之迴歸三項無牴觸** —— 那三項全數達成；本條是那三項
**沒有涵蓋到的第四件事**：同一判準也丟掉了真陽性。
**非靜默失效** —— 受影響者現在都會明說 `no series detected`。
提案三案見 `ANOMALIES.md` A-POP10 §五。

### A-POP11 —— A-POP6 甲類之 sxm 兩筆為假陽性

見 §六-2。與 A-POP10 同一根因（抽取器對登記體例之假設過窄），
只是那裡表現為漏檢，這裡表現為誤報。

### 台帳一致性之三項訂正（由 `ledger_xref` 實測浮現，非人工複讀）

1. **補寫 `## A-POP9` 明細節** —— R-POP17 明文「詳 ANOMALIES.md」，
   而落檔時只有主表一列。內容為四點之逐點對照 ＋ 傳染 ＋ 處分 ＋
   §三第 1 項之連帶回報
2. **A-POP9 主表列之處分欄補列 R-POP13** —— 其第 (4) 點（TC ID 前綴）
   由 R-POP13 處分，原只寫 R-POP17，與 R-POP13 之標題兩處不相認
3. **A-POP2／3／4／6／7／8 之明細節標題由 `PENDING` 改為 `RESOLVED（R-POPnn）`**
   —— 主表早已全數 RESOLVED，明細節標題未同步；同一件事在同一檔內兩種狀態

三項皆為**簿記對齊**（把已裁之結果寫進落後的那一處），未新裁任何事。

---

## 八、預期數字對照（§八，相符者亦列）

### 8.1 語料層（`gen_pilot.py --audit` 自 `generated/pilot_01.json` 實測）

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| TC 總數 | 5 | **5** | 相符 |
| PENDING 佔位 | 0 | **0** | 相符 |
| `newR1L` 殘留（語料）| 0 | **0** | 相符 |
| `PROJ` 殘留（語料）| 0 | **0** | 相符 |
| tc_id 含 `POP-` | 0 | **0** | 相符 |
| Markdown 反引號（五交付欄逐 item）| 0 | **0** | 相符 |
| `input_test_data` = `NA` 之條數 | 5 | **5** | 相符 |
| pre_conditions 含 `ignition in RUN` | 0 | **0** | 相符 |
| Final Step 含 `check that` | 5 | **5** | 相符 |
| spec_reference 兩行者 | 1（POP-002）| **1** | 相符 |
| `pu_citation` 為 null 者 | 1（POP-005）| **1** | 相符 |

### 8.2 工作簿層

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| `newR1L` 全簿 | 0 | **1（D2，母本自帶）** | **不符 —— 見 §一-2，不調和** |
| `PROJ` 全簿 | 0 | **0** | 相符 |
| `POP-` 於 TC ID 欄 F10:F1411 | 0 | **0** | 相符（全簿 5 筆皆 req_id，見 §一-2）|
| x14 DV | 1，存活 | **1，存活** | 相符 |

x14 DV 之 `zipfile` 直讀複驗（母本 vs 產出，逐字）：

```
母本 xl/worksheets/sheet6.xml: x14 dataValidation 1 個
   f      = ['下拉選單!$A$1:$A$9']
   sqref  = ['R10:R1411']
產出 xl/worksheets/sheet6.xml: x14 dataValidation 1 個
   f      = ['下拉選單!$A$1:$A$9']
   sqref  = ['R10:R1411']
```

`surgical_save` 報告：`differing: ['xl/worksheets/sheet6.xml']`（僅一支 sheet xml
改動）、`dv_counts: {'…sheet5.xml': (1, 0), '…sheet6.xml': (3, 1)}`。

### 8.3 條文指紋（`rulings_hash.py`）

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| 既有列 sha 變動 | 0 | **0** | 相符 |
| 新增列 | 6（R-POP12～17）| **6** | 相符 |
| 總列 | — | 549 → **555**（錨點 548 → 554）| — |

`diff`（前後各取 `ruling_id`／`sha8`／`source` 三欄排序後比對）之**全部**輸出：

```
> R-POP12  e323360d  features/popup/RULINGS.md
> R-POP13  9b835066  features/popup/RULINGS.md
> R-POP14  e025ab99  features/popup/RULINGS.md
> R-POP15  298237c3  features/popup/RULINGS.md
> R-POP16  36e1ed0a  features/popup/RULINGS.md
> R-POP17  7b7868ec  features/popup/RULINGS.md
```

**無任何 `<` 列** —— 既有 R-G 條與其餘全部條文之 sha 一列未變（§十第 4 項
升級條件未命中）。

### 8.4 lint／gate

`lint036.py --profile popup`（21 項判準）：

```
行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
     N=0 P=0 Q=0 R=0 T=0 U=0 V=0
```

報告落 `features/popup/reports/popup_20260817_ext__popup_3df1e1d1_20260828.md`。

`gate_all.py` 五支（**逐支歸因**）：

| 閘 | exit | 本包前 | 本包後 | 歸因 |
|---|---|---|---|---|
| `lint_docs036 --gate` | **0** | PASS | PASS | — |
| `canon_refs --waiver --gate` | **1** | 464 | **467** | **本包 +3** —— 兩本新建 BACKLOG ＋ 本上繳包，各一處 `R-G29` 引用；`R-G29` 為既存 unresolved target（全 repo 48 處，`features/display/BACKLOG.md:3` 同式）。**實測隔離**：暫移該三檔重跑 → **464**，放回 → **467** |
| `rulings_hash --check` | **0** | FAIL | **PASS** | 本包重產 tsv 後轉綠 |
| `gates_tsv --check` | **0** | PASS | PASS | — |
| `lint_paths --gate` | **1** | 1 | **1** | **非本包** —— `features/driver_distraction/workbook/driver_distraction_00.xlsx` 落點違規，屬他 feature 之在製品 |

**canon_refs 之 463 對不上**：下放包 §八 稱「既存 463 不增減」，
本包開工前實測即為 **464**（工作樹含他 session 之未提交改動）。
本包之增量為 **+3**，已隔離實證（移除三檔即回到 464）。
**不調和** —— 未把自己的三列塞進 `CANON_REFS_WAIVER.tsv`
（那正是「接一支已知會紅而被容忍之閘」之反面教材），
亦未為了湊數字而把 `R-G29` 之引用從三檔刪掉 —— 那是把出處抹掉換一個綠燈。

### 8.5 單元測試

`python3 -m pytest tests/ -q` → **1255 passed, 8 failed, 15 skipped**。

八項失敗**全數在本包之改動面外**，逐項歸因：

| 測試 | 成因 | 是否本包 |
|---|---|---|
| `test_single_write_path.py`（2 支）| `features/time_management/scripts/lint_tcs.py`、`features/user_profiles/scripts/verify_dv_integrity.py`、`features/vehicle_category/scripts/probe_writeback_c*.py` 等呼叫 `openpyxl.save()` 而未列入 `KNOWN_VIOLATIONS` | **否** |
| `test_intake_scaffold.py`（6 支）| `scripts/new_feature.py` 於 tmp root 找不到 `docs/fw036/templates/DECISIONS.md` 而 exit 2 | **否** |

`git status scripts/` 顯示 `scripts/` 下僅 `lint_docs036.py`（M）與
`ledger_xref.py`（??）為本包所改；上列失敗涉及之檔一個都不在其中。
`new_feature.py` 亦未 import 任何本包改動之模組（其 import 只有
`argparse`／`sys`／`pathlib`）。

本包新增／改動之測試：`test_lint_docs036.py` **23 支全綠**（17 → 23）、
`test_ledger_xref.py` **9 支全綠**（新建）。

---

## 九、三分法（本包所為之分類）

| 類 | 內容 |
|---|---|
| **照裁定執行** | F1～F6、TC ID 重排、-002-05 生成、lint 二修、ledger_xref 新檢、兩本 BACKLOG、tsv 重產 |
| **實測後回報而不自為** | §三第 1 項之 `PROJ`（標的不存在）、§三第 3 項之 `POP-` 全簿掃（不可達成）、sxm 兩筆假陽性（§六-2）、A-POP6 甲類計數三異 |
| **獨立判斷（已揭露）** | (a) `design_method` 取狀態轉換而非負向測試（§四）；(b) `ledger_xref` 另立於 `scripts/` 而不改 vehicle_category 之同名檔（§五-2）；(c) `ledger_xref` 之號碼收集跨全檔而不限主表（§五-2，與 `lint_docs036` 刻意分野）；(d) 兩本 BACKLOG 沿 `features/display/BACKLOG.md` 之體例（含其 `R-G29` 引用，代價見 §八-4）|

### 掃描條件揭露（R-G8）

| 掃 | 條件 |
|---|---|
| 工作簿字串掃 | `openpyxl` 全 sheet 全格，`str(cell.value)` 子字串比對，區分大小寫 |
| `ignition in RUN` | 五條 `pre_conditions` 全文，`.lower()` 後比對，**不**分大小寫 |
| 反引號 | 五交付欄（test_item／pre_conditions／input_test_data／test_procedure／expected_result），按 `\n` 切 item 後逐 item |
| PU 引文複驗 | Pop Up List `Main` sheet，以 A 欄 `^PU\d` 建索引，逐欄名逐格 `str.strip()` 後等值比對；16 格全符 |
| x14 DV | `zipfile` 直讀 `xl/worksheets/sheet*.xml`，正則取 `<xm:f>`／`<xm:sqref>` |
| tsv 前後比對 | `cut -f1,3,5 \| sort` 後 `diff`（id／sha8／source 三欄）|
| lint_docs036 跨 feature | `--feature <f>` 逐 feature 各跑一次，改判準前後各一輪，共 11 feature |

---

## 十、R-G13 引用表（sha8 取自重產後之 `docs/fw036/RULINGS.sha.tsv`）

| 條 | sha8 | 標題 |
|---|---|---|
| R-POP12 | `e323360d` | -002-02 不拆，軸不存在 |
| R-POP13 | `9b835066` | TC ID 前綴定值 |
| R-POP14 | `e025ab99` | -002-05 採規格原句生成 |
| R-POP15 | `298237c3` | Pilot 修正六件之判準 |
| R-POP16 | `36e1ed0a` | lint 新規命中之三分法處置 |
| R-POP17 | `7b7868ec` | 上繳回報與 repo 台帳不符之登記 |

另引 R-G3、R-G5、R-G8、R-G13、R-G25、R-G29、G-B、G-D、G-F、G-K、G-N。

---

## 十一、台帳現況（**自 repo live 產**，R-POP17-1）

以下表由 `python3 scripts/ledger_xref.py --feature popup --live` 直接輸出，
**未經手寫重述**：

| 號 | 狀態 | 處分條 |
|---|---|---|
| A-POP1 | RESOLVED（R-POP9 追認；傳染性掃描已於下放包 02 §六-3 執行） | R-POP9 |
| A-POP2 | RESOLVED（甲半 R-POP6 納入、DR-POP1 結案；乙半 R-POP7 不納入、DR-POP2 續開） | R-POP6／R-POP7 |
| A-POP3 | RESOLVED（R-POP8：-002-02 之 spec_reference 併列 _5.5＋_5.6） | R-POP8 |
| A-POP4 | RESOLVED（R-POP10：改前綴自動抽取） | R-POP10 |
| A-POP5 | RESOLVED（更正＋寫入路徑改 xlsx_surgical；輸出實測 x14 存活） | — |
| A-POP6 | RESOLVED（R-POP16：甲／乙／丙三分處置） | R-POP16 |
| A-POP7 | RESOLVED（R-POP12：不拆，理由改採「規格側無此分支」） | R-POP12 |
| A-POP8 | RESOLVED（R-POP14：照 GP4-4 規格原句生成、不引 PU；另開 DR-POP4） | R-POP14 |
| A-POP9 | RESOLVED（R-POP17；其 (4) 另由 R-POP13 處分） | R-POP13／R-POP17 |
| **A-POP10** | **PENDING** | — |
| **A-POP11** | **PENDING** | — |
| DR-POP1 | RESOLVED（2026-08-27）：標的已在 repo，經 Pei 納入（R-POP6） | R-POP6 |
| DR-POP2 | 已登記，未送出 | — |
| DR-POP3 | 已登記，未送出 | — |
| DR-POP4 | 已登記，未送出 | — |

未結 DR 三件（DR-POP2／3／4）皆「已登記，未送出」，皆不阻斷本包（IN §8.4.3）。

---

## 十二、五條 TC 全文

（`generated/pilot_01.json` 之回讀輸出；工作簿 `sandbox/pilot01/` 之
`row 10`～`row 14` 與此逐格相同）

### NR1L-Popup-001 — SWE1-POP-002-01

- **Test Group／Set**：Popup ／ Pop-up Close
- **Test Item**：
  `Pop-ups can be closed after time-out (timeout is defined in Pop-up List document)`
  `(Time-out closure of PU0942, 5 s)`
- **Pre-conditions**：`1. The Home Screen is displayed`
- **Input Test Data**：`NA`
- **Test Procedure**：
  `1. Enter the Home Screen page-management view and add a home screen page`
  `2. Leave the screen and all buttons untouched for 10 seconds after the pop-up appears`
  `3. Read the pop-up display status and the elapsed time and check that the pop-up has closed by itself 5 seconds after it appeared, matching the Time-out defined by PU0942 Timeout (sec)`
- **Expected Result**：
  `1. The pop-up is displayed showing "<X>" and "Page added! [Reorder]", as defined by PU0942 String/Popup Message`
  `2. No user interaction is registered during the 10-second window`
  `3. The pop-up closes by itself 5 seconds after it appeared, matching the Time-out defined by PU0942 Timeout (sec), and the Home Screen is shown without the pop-up`
- **Spec Reference**：`…_(February_2_2023)_5.6`
- **PU**：PU0942（Home Screen；Timeout (sec) = `5`）
- **TC Ref ID／Priority／Design Method／Functional Safety／Author**：
  `NEW` ／ `P1` ／ `狀態轉換 (State Transition Testing)` ／ `NA` ／ `PeiPYHsu`

### NR1L-Popup-002 — SWE1-POP-002-02

- **Test Item**：
  `Pop-ups can be closed after pressing button that opened pop-up again (eg. Tracks popups)`
  `(Second press of the opening control <Trks>, PU0215)`
- **Pre-conditions**：
  `1. A media source containing at least one track list is available`
  `2. The Media screen is displayed`
- **Input Test Data**：`NA`
- **Test Procedure**：
  `1. On the Media screen, press the Track list button "Trks"`
  `2. Press "Trks" a second time while the pop-up is displayed`
  `3. Read the pop-up display status immediately after the second press and check that the pop-up is no longer displayed`
- **Expected Result**：
  `1. The "Tracks List" pop-up is displayed, as defined by PU0215 String/Popup Message`
  `2. The second press lands on the same "<Trks>" button that opened the pop-up`
  `3. The pop-up is closed and the Media screen is shown without the pop-up`
- **Spec Reference**（**兩行**，R-POP8）：
  `…_(February_2_2023)_5.5`
  `…_(February_2_2023)_5.6`
- **PU**：PU0215（Media；Exit Conditions = `<Trks>`）
- 其餘欄同 001

### NR1L-Popup-003 — SWE1-POP-002-03

- **Test Item**：
  `Pop-ups can be closed when touching screen outside of pop-up`
  `(Touch outside the pop-up bounds, PU0580)`
- **Pre-conditions**：
  `1. At least two driver Profiles exist on the head unit`
  `2. The All Profiles tab is reachable from the current screen`
- **Input Test Data**：`NA`
- **Test Procedure**：
  `1. Open the All Profiles tab and switch manually to another Profile`
  `2. Within 5 seconds of the pop-up appearing, tap an area of the screen outside the pop-up window frame`
  `3. Read the pop-up display status immediately after the tap and check that the pop-up is no longer displayed, before the 5-second Time-out defined by PU0580 Timeout (sec) has elapsed`
- **Expected Result**：
  `1. The pop-up is displayed showing "Welcome [username]", "X", as defined by PU0580 String/Popup Message`
  `2. The tap lands outside the pop-up window frame and activates no pop-up control`
  `3. The pop-up is closed, and the closure occurs before the 5-second Time-out defined by PU0580 Timeout (sec) elapses`
- **Spec Reference**：`…_5.6`
- **PU**：PU0580（Personal Account/Driver Profiles）
- 其餘欄同 001

### NR1L-Popup-004 — SWE1-POP-002-04

- **Test Item**：
  `Pop-ups can be closed after making a selection inside the pop-up if applicable`
  `(Selection <OK> inside the pop-up, PU0949)`
- **Pre-conditions**：
  `1. No mobile phone is paired with the head unit`
  `2. The Home Screen Shortcuts view is displayed`
- **Input Test Data**：`NA`
- **Test Procedure**：
  `1. On the Home Screen Shortcuts view, press the grayed out "Make a Call" button`
  `2. Within 3 seconds of the pop-up appearing, press "OK" inside the pop-up`
  `3. Read the pop-up display status immediately after the press and check that the pop-up is no longer displayed, before the 3-second Time-out defined by PU0949 Timeout (sec) has elapsed`
- **Expected Result**：
  `1. The pop-up is displayed showing "No Phone is Connected.        <OK>    <X>", as defined by PU0949 String/Popup Message`
  `2. The "<OK>" press is registered while the pop-up is still displayed`
  `3. The pop-up is closed, and the closure occurs before the 3-second Time-out defined by PU0949 Timeout (sec) elapses`
- **Spec Reference**：`…_5.6`
- **PU**：PU0949（Home Screen；Timeout (sec) = `3`）
- 其餘欄同 001

### NR1L-Popup-005 — SWE1-POP-002-05（**本輪新生成，不引 PU**）

- **Test Item**：
  `Exceptions when the popup allows the user to perform more than 1 task- e.g in the search keyboard only X button 'close', any other buttons do not close the popup`
  `(Non-closing control inside a multi-task pop-up; no PU cited)`
- **Pre-conditions**：
  `1. A pop-up that allows the user to perform more than 1 task is available, the search keyboard being the example given in the requirement`
  `2. That pop-up is displayed`
- **Input Test Data**：`NA`
- **Test Procedure**：
  `1. Trigger the pop-up that allows the user to perform more than 1 task`
  `2. Inside the displayed pop-up, press a button other than the "X" button`
  `3. Read the pop-up display status immediately after the press and check that the pop-up is still displayed`
- **Expected Result**：
  `1. The pop-up is displayed and allows the user to perform more than 1 task`
  `2. The button pressed is a button other than the "X" button of that pop-up`
  `3. The pop-up is not closed by that press and remains displayed`
- **Spec Reference**（**單行**）：`…_(February_2_2023)_5.6`
- **PU**：**null**（R-POP14）
- 其餘欄同 001

---

## 十三、待 Pei 之未決項（本包未處理，逐項）

| # | 事項 | 出處 |
|---|---|---|
| 1 | **A-POP10** —— 主表辨識方式（三案）| 本包新登 |
| 2 | **A-POP11** —— A-POP6 甲類改列 2 筆、sxm 兩筆撤回 | 本包新登 |
| 3 | `scripts/ledger_xref.py` 是否與 `features/vehicle_category/scripts/ledger_xref.py` 合併；是否接入 `gate_all.py`（接入即全 repo 轉紅）| §五-2 |
| 4 | `canon_refs` +3（兩本新 BACKLOG ＋ 本上繳包之 `R-G29`）：修 `R-G29` 之可解析性、或改寫兩檔之引用、或維持 | §八-4 |
| 5 | Priority P1／P0、Estimated Test Time 欄之政策（Q 欄本包**未寫入**）| 下放包 02 §3b-4 |
| 6 | pilot review（唯一人工閘，無 done region 可仲裁）| 下放包 02 §3b-5 |
| 7 | `sources/` 版控條文之 R- 取號 | 待分析層 |
| 8 | R-POP5（Heading 列之台帳處置 [DEFAULT]）追認 | 下放包 02 §4 |
| 9 | `DECISIONS.md` 之 [PROPOSED]／[PEI] 未裁、Sign-off 未填 | 下放包 02 §4 |
| 10 | A-POP2 §四-3：`forms/` 之落點政策（全域）| 下放包 03 §十二 |
| 11 | `-002-05` 之 `design_method`：狀態轉換（本包所取）vs 負向測試 | §四 |
| 12 | `lint_paths` 之紅（driver_distraction 之在製品）—— 他 feature | §八-4 |

---

## 十四、git

**未執行任何 git 操作**（R-G5）。建議之 commit：

```
feat(popup): land handoff 03 - pilot fixes F1-F6, -002-05 generated, 5 TCs green
```

改動之檔（`git status` 可見者）：

```
M  features/popup/feature.yaml
M  features/popup/ANOMALIES.md
M  features/popup/scripts/gen_pilot.py
M  features/popup/generated/pilot_01.json
M  scripts/lint_docs036.py
M  docs/fw036/RULINGS.sha.tsv
M  features/popup/docs/INDEX.md
?? scripts/ledger_xref.py
?? tests/test_ledger_xref.py
M  tests/test_lint_docs036.py
?? features/audio_mgmt/BACKLOG.md
?? features/time_management/BACKLOG.md
?? features/popup/docs/upstream/03_pilot_fixes.md
?? features/popup/sandbox/pilot01/FM-WI-FSM-036-A01…_ext.xlsx
?? features/popup/reports/popup_20260817_ext__popup_3df1e1d1_20260828.md
```

**非本包所改而 `git status` 亦顯示為 M 者**：`features/popup/RULINGS.md`
（R-POP12～17，分析層本輪落檔）、`features/popup/DATA_REQUESTS.md`
（DR-POP4 登記 ＋「分析層裁示（2026-08-27）」段，分析層本輪落檔）。
本包**未動此二檔**。

**注意**：工作樹另有他 session 之未提交改動（`features/vehicle_setting/`、
`features/driver_distraction/`、`features/sw_update/`、`features/bed_lowering/`、
`features/time_management/docs/`、`docs/runtime/` 等）。
commit 時**務必帶 pathspec**，勿 `git add -A`。
