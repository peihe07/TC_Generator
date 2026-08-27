# 上繳包 02 — Popup 值來源接線 ＋ 工具修 ＋ Pilot 生成

日期：2026-08-27
對應下放包：`features/popup/docs/handoff/02_wiring_tooling_pilot.md`
執行層：Claude Code，repo `/Users/peihe/Work_Projects/TC_Generator`
分支：`feat/m1-stage7-scorecard`（HEAD `2df23ee`）

---

## 〇、一句話

§六-0 之兩項前置達成後起跑；§六-1～4 全數完成且四項預期數字全數相符；
§六-5 **生成 4 條而非 5–7 條** —— `-002-05` 觸發 §八 升級條件
（`search keyboard` 於納入之 Pop Up List 查無對應列，A-POP8），依明文
「不改用他例」停下不生成；`-002-02` 之 device 軸經判斷不拆（A-POP7）。
lint 全綠（21 項全 0）、`PENDING:` 佔位 0。

---

## 一、§六-0 前置確認

| 前置 | 判 | 證據（量測條件） |
|---|---|---|
| DECISIONS.md 已簽（P2）| **達** | `recon.read_signoff()` 實跑：`signed=True`、`reviewed_by='PeiPYHsu'`、`date='2026-08-27'`。**判準取 repo 自身之函式**，非目視 |
| 工作樹乾淨 | **達** | `git status --short features/popup sources scripts tests docs/fw036` 輸出為空（唯讀 git，未改狀態）|
| framework 已鎖定 | **達** | `features/popup/framework.md` Part I～V 齊；§六-5 所引之 Part IV 在第 79 行 |
| profile 已建（§六-5 之隱含前置）| **達** | `docs/runtime/profiles/FW036_R1L_Popup_Profile.md`，實測 **3,813 B**（= 3.72 KB）|

Sign-off 之 `Reviewed by`／`Date` 由執行層轉錄，值由 Pei 指定
（2026-08-27 指示逐字：「你只需填 Sign-off 之 Reviewed by 與 Date」），
形制沿 comfort 前例；轉錄事實已逐字記於該檔 Ruling notes。

---

## 二、預期數字對照（下放包 02 §預期數字表，相符者亦列）

| 項 | 預期 | 實測 | 判 | 量測條件 |
|---|---|---|---|---|
| PU 母體 | 1340 | **1340** | 相符 | `Main` r3 起，A 欄 `^PU\d`，逐列 |
| (a) timeout 純數值列 | 240 | **240** | 相符 | 同母體，C 欄 `.strip()` 後 `^\d+(\.\d+)?$` |
| (b) outside 列 | 102 | **102** | 相符 | 同母體，D 欄含 `outside`，不分大小寫、子字串 |
| (c) keyboard 列 | 15 | **15** | 相符 | 同母體，D／E／G 任一含 `keyboard`，同上 |
| RULINGS.sha.tsv 既有列 sha 變動 | 0 | **0** | 相符 | 246 列以 `(ruling_id, source, line)` 為鍵逐列比對前後版 |
| PENDING 佔位 | 0 | **0** | 相符 | `lint036.py --profile popup` 之 U 檢查，全簿全欄 |
| lint | 全綠 | **21 項全 0** | 相符 | 見 §六 |
| **生成 TC 數** | **5–7** | **4** | **不符** | 逐 TC。成因見 §五（`-002-05` 升級停下）與 §四（`-002-02` 不拆軸）。**不調和** |
| canon_refs 既存數 | 463 不增減 | **463** | 相符 | `gate_all.py` 實跑；本包新檔之 canon 引用一律帶 `FO`／`IN` 前綴 |

`Main` A 欄非空但不合 `^PU\d` 之列 **2**（G-D：被抑制條數，非零須報）——
r3 之 `A - Copied identical in PU0031.\nre` 與另一列，皆非 PU 登錄列。

---

## 三、§六-1 — R-POP11 rulings_hash 範圍擴充

`SCOPE_DEFAULT`（canon ＋ `vehicle_setting` 兩檔）改為 canon ＋
`features/*/RULINGS.md` 全掃；原兩檔範圍保留為 `SCOPE_W_P1`，
以新旗標 `--w-p1-only` 取用。`--all-features` 保留為 no-op，不破既有呼叫。

### invariant 逐列比對（R-POP11 明文：任一既有列變動即停）

| 量 | 值 |
|---|---|
| 舊 tsv 列數 | 246 |
| 新 tsv 列數 | **548**（+302）|
| 既有列消失 | **0** |
| **既有列 `sha256` 變動** | **0** |
| 既有列其他欄（kind／source／line／body_lines／ancestor／slug）變動 | **0** |

比對之身分鍵為 `(ruling_id, source, line)` 三元組 —— 只用 `ruling_id`
會在跨檔重名時（本次即有 10 組）把兩條不同條文對成一條。
另以 `--w-p1-only` 重產並與擴充前之 tsv `diff`：**逐位元組相同**，
即擴範圍未改變舊範圍內任何一條之計算。

### 新增 302 列之來源分佈

| 列數 | 來源檔 |
|---:|---|
| 153 | `features/power_moding/RULINGS.md` |
| 88 | `features/time_management/RULINGS.md` |
| 40 | `features/comfort/RULINGS.md` |
| **11** | **`features/popup/RULINGS.md`（R-POP1～R-POP11，與預期 11 相符）** |
| 7 | `features/audio_mgmt/RULINGS.md` |
| 3 | `features/user_profiles/RULINGS.md` |

他 feature 之新增列數為實測值，下放包已明言不預估（分母未量測）。

**同時浮現之既有狀況（不阻斷，登錄）**：跨檔／同檔重複 `ruling_id`
**10 組，本體皆不同** —— `R-C27`／`R-C42`（comfort 同檔兩處）、
`R-PMH13`、`R-TM9`（兩組）／`R-TM10`／`R-TM40`／`R-TM41`、
`R-G4`／`R-G7`（canon 與 `user_profiles/RULINGS.md` 各一）。
`collect()` 保留全部列而不擇一，故 tsv 未因此遺漏任何條文；
`--gate` 會對「本體不同之重複」判紅，但 `gate_all.py` 走 `--check`
不帶 `--gate`，故 gate 不因此轉紅。**是否處置屬各該 feature，本包不代改。**

`rulings_hash --check` PASS（548 條）；`tests/test_rulings_hash.py` 26 passed。

---

## 四、§六-2 — R-POP10 lint 跳號檢查改自動抽取

前綴改為自語料抽取 `(A|DR|R)-[A-Z]{1,6}`；硬寫時代之
`("DR-PW", "A-PW", "A-PM")` 保留為 `LEGACY_PREFIXES`，**不再參與判斷**，
只作 G-B 差集之被減數。

順帶修一個回報缺陷：`gaps()` 原以 `f"{prefix}-{n}"` 組編號，
複合前綴會印出 `A-POP-4` 這種語料裡不存在、grep 不到的字串。
改為以該前綴在語料中實際的寫法（`SEPARATORS`，首見者為準）重組。

### G-K 迴歸兩向（scratch 副本，`scratchpad/inject/`）

| 向 | 操作 | 結果 |
|---|---|---|
| (a) 已知案例轉受檢 | 對現行 popup 台帳實跑 | 受檢前綴集 `['A-POP', 'DR-POP']`，兩者皆列於「新受檢（硬寫清單外）」 |
| (b) 注入向 | scratch 副本內 `A-POP4` → `A-POP9` | **exit 1**，5 筆 `A-POP_series` finding：`A-POP4`～`A-POP8` |
| (b) 修回 | `A-POP9` → `A-POP4` | **exit 0**，`docs_structure：PASS` |

### G-N 字面釘入之測試（`tests/test_lint_docs036.py`，新增 5 支）

fixture 逐字寫死 `A-POP1/2/9` 與 `DR-POP1/2`，**不讀 repo 語料** ——
popup 台帳日後如何改寫都不影響其證明力。五支涵蓋：
缺陷本體命中、修正後不得再命中、硬寫時代前綴不因改制漏檢、
G-B 差集、單字母系列（`R-27`／`S3`）不被複合前綴吞掉。
`tests/test_lint_docs036.py` 17 passed。

### G-B 差集：對 19 個 feature 全跑

**`--feature power`（`gate_all.py` 之預設）維持 PASS，gate 不因本改動轉紅。**
其餘結果三分，全文與逐筆佐證見 `ANOMALIES.md` A-POP6：

- **真陽性 4 筆**（sxm `A-SX18/19`、audio_mgmt `DR-AM7`、time_management
  `A-TM2`）—— 各該 feature 之台帳確有跳號，本包不代改
- **假陽性 2 筆**（power_moding `DR-PMH1`、projection `A-PJ37`）——
  `編號重複` 不分表，回顧／狀態彙整表之同一 id 被判重複。
  **此非新增缺陷**，該邏輯在硬寫時代即如此，只是未曾套用到這兩個前綴
- **抽取盲區 4 個 feature**（amfm／home／media／user_profiles 抽得前綴集為空）
  ＋ privacy 之假前綴 `S`（來源為欄位值表 `| S10 | NA（Functional Safety）|`）

依 §八「lint 新規誤傷既有台帳（差集含非預期前綴）」，本項**登記為升級事項**
（A-POP6，PENDING），提案兩條：`編號重複` 限同表內；前綴抽取限主登記表。
判準精修屬 Tier 2，不自裁。

---

## 五、§六-3 — R-POP9 sanitizer 傳染性掃描（只掃只報）

**首版判準過鬆已作廢重寫**：初版把裸 `.strip()` 當成「剝前導字元集」，
於 `scripts/` 得 40 個 DEFECT，絕大多數是假陽性。一個判準錯的掃描
會給出很有信心的錯答案（G-K 之命題）。收緊後之兩支獨立偵測器與結果
全文見 `ANOMALIES.md` A-POP1 §四，摘要：

| 範圍 | 檔數 | D1 | D2 | **D1 ∧ D2（A-POP1 同型）** |
|---|---|---|---|---|
| `scripts/`（明定範圍）| 24 | 1 | 2 | **1** —— `extract_source.py`，**已修** |
| `backend/` ＋ `features/*/scripts/`（範圍外，順帶）| 470 | 3 | 185 | **0** |

半具備而登記備查者三支（`power/scripts/g113_buckets.py`、
`power/scripts/or_branch_coverage.py`、`time_management/scripts/tm_rulings.py`）。
**掃描器之漏報方向已具名揭露**（不認 `open(...,"w")`／`json.dump`／
`shutil.copy`／`to_csv`；D1 僅認有型別註記者）—— G-D。

---

## 六、§六-4／§六-5 — 值來源接線與 Pilot

### 6.1 接線

`feature.yaml`：`paths.popup_list = "../../forms/Pop Up List HMI R1 (26PI).xlsx"`
（glob 自 feature 目錄實測命中 1）。另補 `tc_id_format: "newR1L-POP-{n:03d}"`
—— project 前綴之權威為工作簿 D2，`sandbox/base/` 副本實測
`C2 = "專案名稱 Project  Name："` ／ `D2 = "newR1L"`。

`features/popup/data/popup_list_candidates.tsv`：345 列（三類聯集；
240+102+15 = 357，重複歸屬 12 列），首三行帶 `source` / `source_sha256`
`ff47b7be63e5824c…` / `baseline Main!A1 = SR24 Post 2A CR25802`（G-F）。

### 6.2 生成之 4 條

| TC ID | leaf | 引用 PU | spec_reference | 選定理由（摘）|
|---|---|---|---|---|
| `newR1L-POP-001` | -002-01 time-out | **PU0942** Home Screen，`Timeout (sec)=5` | `…_5.6` | (a) 類 240 列中，C 欄為純數值 `5`（非 `5 seconds` 帶單位），觸發純屬 HMI（新增 home screen 頁），台架不需車動／外接／雲端 |
| `newR1L-POP-002` | -002-02 press second time | **PU0215** Media，`Exit Conditions=<Trks>` | `…_5.5` ＋ `…_5.6`（R-POP8，兩行升冪）| 全表唯一「Exit Conditions 即開啟鍵本身」者；037 E 欄自舉 `eg. Tracks popups`，來源與例證對得上 |
| `newR1L-POP-003` | -002-03 touch outside | **PU0580** Personal Account，`Exit Conditions=Timeout, Touch outside of popup, X` | `…_5.6` | (b) 類 102 列中 Exit Conditions 僅三項、無雲端往返無 keyboard，台架以切換 Profile 重現 |
| `newR1L-POP-004` | -002-04 selection | **PU0949** Home Screen，`Exit Conditions=<OK>\n<X>` | `…_5.6` | 取 `<OK>` 而非 `<X>`：037 VC 逐字舉例為 `tap an option or press a "Confirm"/"Cancel" button`，`<X>` 是關閉鍵不是選項 |

- **PU 引文複驗（G-F）**：16 格（PU id × 欄）於落檔前逐格對原檔比對，
  不符即 `exit 2` 停。**16/16 相符**。此驗在 `gen_pilot.py` 內，
  非事後人工核 —— 靜態轉錄與其來源分家是 G-F 的標的
- **時窗設計**：`-002-03`／`-002-04` 之受測 popup 同時具 time-out，
  故步驟明訂「N 秒內」動作、ER 明訂「早於 time-out 前關閉」。
  不設時窗則觀察到的關閉分不出是哪一條途徑造成 —— 會測成 `-002-01`
- **`-002-01` 觀察窗 10 秒（2× 標稱）**：只看到 5 秒時仍在，
  分不出「還沒關」與「不會關」

### 6.3 `-002-02` device 軸：**不拆**（A-POP7）

037 S11 逐字 `a physical hard button or a specific UI button on the screen`
是 IN §8.3 之真軸。以 `again|second time|re-?press|toggle` 掃 Pop Up List
`Exit Conditions`（不分大小寫）命中 13 列，逐列判讀後只有兩列與本命題有關：

- UI 分支 `PU0215`：`Exit Conditions=<Trks>`，`Description=Display when user
  is in Media screen and presses Track list button` —— 開啟鍵＝關閉鍵，**成立**
- hard-button 分支最近候選 `PU0229`：`Exit Conditions=Press of VR button again`，
  但 `Description=Displayed when the user asks to call for a number` ——
  **開啟者是語音請求而非該按鍵**。指派給 hard-button 分支是來源沒有承載
  的推定（IN §8.4.1），**不做**

拆成兩條會有一條無實例可填。故出一條 TC，procedure／ER 只說
「開啟該 pop-up 的那個按鍵」，不宣稱其實體型別；理由逐字入該 TC 之
`reasoning`。hard-button 實例併入 RD-1 索取，到件後補一條同引 -002-02
（IN §8.2.2）。

### 6.4 `-002-05`：**停下不生成**（A-POP8，§八 升級）

| 量（三 sheet 全欄，不分大小寫子字串）| Main | Templates | Drop Down Fields |
|---|---|---|---|
| `search keyboard`（連續詞組）| **0** | 0 | 0 |
| 同列兼含 `keyboard` 與 `search` 之 PU 列 | **0** | — | — |
| `keyboard` ／ `search` ／ `qwerty` ／ `keypad` | 22／44／1／5 | 0 | 0 |

以 D／E／G 三欄判準與 A–Q 全欄判準所得之 `keyboard` PU 列**完全相同
（15 = 15，差集空）** —— §六-4 之三欄判準在此未失分。

依 §六-5 明文「不改用他例」，**未**以 PU0022／PU0023（Media 字母鍵盤）
或 PU0861（Camera App 全鍵盤）替代 —— 那需要先認定「該列即 search
keyboard」，正是被禁止的替代。依 IN §8.4.1 亦**不落 `PENDING:` 佔位、
不造值**。三個提案見 `ANOMALIES.md` A-POP8，**開哪一個屬 Pei**。

### 6.5 工作簿

| 項 | 值 |
|---|---|
| 來源 | `sandbox/base/…_SWQT_20260817_ext.xlsx`，sha `6372fb6be02f48dc…`（**跑完後重測未變**）|
| 輸出 | `sandbox/pilot01/`（同名），R-G25 |
| 手段 | `backend/xlsx_surgical.surgical_save` —— **全程未呼叫 `openpyxl.save()`**（R-G3）|
| 改動 | 4 列 × 15 欄 = **60 格**；`differing` 僅 `xl/worksheets/sheet6.xml`，48 個 zip member 其餘逐一原樣複製 |
| B 欄公式 | `=IF(ISBLANK($D10),"",ROW()-9)` 等四式**逐字未變**（以公式形回讀比對）|
| x14 下拉 | 輸出實測 `sqref=R10:R1411`、`f=下拉選單!$A$1:$A$9`，**與來源逐字相同** —— 見 A-POP5 |

**A-POP5（本包新開，已 RESOLVED）**：上繳包 01 §五-3 之 N3 稱
「design_method 欄（R）無 data validation」為**誤述** ——
`openpyxl` 只讀 `<dataValidations>`，不讀 `<extLst>` 內之
`<x14:dataValidation>`，載入時逐字警告 `Data Validation extension is not
supported and will be removed`。亦即 **`save()` 會刪掉全簿唯一的設計方法
下拉且不報錯**。此即 R-G3 之具體理由，非偏好。

### 6.6 欄位值與其依據

| 欄 | 值 | 依據 |
|---|---|---|
| Test Group／Test Set | `Popup`／`Pop-up Close`，逐列寫入 | R-POP4；BLANK ＝ FILL（FO §2.1）|
| Test Case Reference ID | `NEW` | feature.yaml `write_back` |
| Test Case Priority | **`P1`（四條同）** | 見下 |
| Design Method | `狀態轉換 (State Transition Testing)`（四條同）| IN §12 first-match：四條皆為「popup displayed → closed」之狀態變化；profile §3 令逐字取 `下拉選單` 9 字串之一 |
| Functional Safety | `NA` | 037 無 ASIL／FTTI 欄（recon 實測），SYS2／SYSRA 不入追溯鏈 |
| Estimated Test Time (Q) | **留空** | 本 feature 無此欄之政策，填任何數字都是造值。**另註**：母本之 DV `P10:Q1411 = "P0,P1,P2,P3"` 把 Q（分鐘數）一併綁上優先級詞彙，為母本既有瑕疵，未動 |
| Author | `PeiPYHsu` | feature.yaml `write_back` |

**Priority 之 P1 為執行層判斷，列為 pilot review 之待確認項**：
TCP 之 P1 定義為「主要功能的次要／進階操作，主要功能之邏輯分支」，
而 GP4 將四條途徑並列為 `the following ways`，無一者為「主流程」；
037 R 欄對五 leaf 一律 `Medium`（非 High）。
**惟 TCP 亦載「功能的核心主流程預設就是 P0」** —— 若 Pei 認
「popup 會關」即 Popup feature 之核心主流程，四條應為 P0。
執行層取 P1 並揭露另一讀法，不自行認定。

### 6.7 lint

`python3 scripts/lint036.py <輸出簿> --profile popup`：

```
行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0
     J=0  K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=0  V=0
```

**21 項全 0。** 報告落 `features/popup/reports/`。

**首跑並非全綠，59 筆，逐項改寫後才綠**（過程據實記載，非事後修飾）：
N 行尾多餘句號 46、A 禁用動詞 `Observe` 5、D PC 通電前提 4、
I test_item 缺括號下半 4。四項皆為執行層未照屋規落筆：
去行尾句號；procedure 之 `Observe …` 改為具體動作（`Read …`／`Leave …
untouched`），觀察歸 ER；pre-condition 移除 `The head unit is powered on`
（IN §4.4 明列為 forbidden 之 system default）；test_item 改兩段式
（上半 037 E 欄 verbatim，下半英文情境標籤，四條互異）。

---

## 七、gate 實跑

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 463
PASS      exit 0   rulings_hash     OK: docs/fw036/RULINGS.sha.tsv 與現行條文相符（548 條）
PASS      exit 0   gates_tsv        OK: docs/runtime/GATES.tsv 相符（45 閘）
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 1
```

**兩支 FAIL 皆非本包所致，逐支具名：**

- `canon_refs` **463** —— 與上繳包 01 同值，本包未使其增減
  （下放包 §預期數字表要求「不因本包增減」，**相符**）
- `lint_paths` **1 筆，具名為
  `features/driver_distraction/workbook/driver_distraction_00.xlsx`**
  （`.xlsx` 之合法落點為 `delivered`／`inputs`／`sandbox`，實為 `workbook/`）
  —— 屬另一 session 同期之 driver_distraction 作業，**非 popup 產出**。
  本包之 popup 產出物落點全數合法：`sandbox/pilot01/*.xlsx`、
  `generated/*.json`、`data/*.tsv`、`reports/*.md`

`pytest tests/`：**8 failed / 1240 passed / 15 skipped**。
8 failed 與上繳包 01 為同一組、同一成因（`test_single_write_path` 之
`KNOWN_VIOLATIONS` 基線未涵蓋 11 個既有 `openpyxl` save 呼叫點；
`test_intake_scaffold` 之 `new_feature.py` 於暫存 repo exit 2）。
本包新增 7 支測試（extract_source 2 ＋ lint_docs036 5）全綠，
**未使任一支由綠轉紅**。

---

## 八、R-G13 引用表（sha8 取自**重產後**之 tracked tsv）

| 條 | sha8 | 落點 | 本包如何用到 |
|---|---|---|---|
| R-POP1 | `61145b5f` | `popup/RULINGS.md:7` | slug／目錄 |
| R-POP2 | `93a0e937` | `:14` | 生成範圍 5 leaf |
| R-POP3 | `6f6a3531` | `:23` | DR 三件 |
| R-POP4 | `1555a8f1` | `:29` | Test Group／Test Set 逐列寫入 |
| R-POP5 | `896b4b84` | `:36` | Heading 台帳標記 |
| R-POP6 | `66f64b48` | `:44` | Pop Up List 納入、`paths.popup_list`、四條 TC 之實值 |
| R-POP7 | `f6d6e22c` | `:59` | Priority Matrix 不納入，DR-POP2 續開 |
| R-POP8 | `7425f059` | `:66` | `-002-02` 之 spec_reference 併列兩行 |
| R-POP9 | `a899c245` | `:78` | A-POP1 追認 ＋ 傳染性掃描 |
| R-POP10 | `a2237932` | `:85` | lint 前綴自動抽取 ＋ 迴歸兩向 |
| R-POP11 | `a6b5301b` | `:93` | rulings_hash 範圍擴充 ＋ invariant |
| R-G3 | `79860d4a` | `FEATURE_ONBOARDING.md:736` | 全程未 `openpyxl.save()` |
| R-G5 | `9814d24c` | `:747` | 未執行改狀態之 git |
| R-G10 | `2b51c522` | `:771` | framework 餘數驗證（分析層已跑，本包引用其結論，未自行重跑）|
| R-G13 | `abdc56e3` | `:788` | 本表本身 |
| R-G25 | `50be5127` | `:1012` | 輸出落 `sandbox/`；`lint_paths` 實跑 |
| R-G27 | `2bd39a12` | `:1049` | Pop Up List 引用原位不搬 |

> 全表 17 個 sha8 皆自**本包重產後**之 `docs/fw036/RULINGS.sha.tsv` 逐列取得
> （`grep -P "^R-XX\t"`），非沿用上繳包 01 之值。R-POP1～R-POP5 之 sha8
> 與上繳包 01 以 `--all-features` 對 scratch 實測者相同 —— 擴範圍未改變
> 其計算，與 §三 之 invariant 結果一致。

---

## 九、三分法清單

### defect（已修）

| # | 內容 | 處置 |
|---|---|---|
| D1 | pilot 首跑 lint 59 筆（N 46／A 5／D 4／I 4）—— 執行層未照 IN §4.3.1／§4.4／屋規落筆 | 逐項改寫，21 項全 0 |
| D2 | `gaps()` 對複合前綴印出 `A-POP-4` 這種語料裡不存在、grep 不到的編號 | `SEPARATORS` 取語料實際寫法重組 |
| D3 | 傳染性掃描首版判準過鬆（裸 `.strip()` 誤判），得 40 個假 DEFECT | 判準重寫為 D1／D2 兩支，作廢首版 |

### style-divergence

| # | 內容 | 處置 |
|---|---|---|
| S1 | `--all-features` 旗標於 R-POP11 後語意落空 | 保留為 no-op 並改寫 help 字串，不移除（移除會破既有呼叫）|
| S2 | Estimated Test Time (Q) 欄無政策 | 留空並揭露；不填造值 |

### note

| # | 內容 |
|---|---|
| N1 | `rulings_hash` 擴範圍後浮現 10 組本體不同之重複 `ruling_id`（comfort 2、power_moding 1、time_management 4、canon↔user_profiles 2）—— tsv 未遺漏任何條文，`gate_all` 不轉紅；屬各該 feature |
| N2 | 母本 DV `P10:Q1411 = "P0,P1,P2,P3"` 把 Q（分鐘數）綁上優先級詞彙 —— 母本既有瑕疵，未動 |
| N3 | Pop Up List `Main` A 欄非空而不合 `^PU\d` 之列 2 筆，非 PU 登錄列 |
| N4 | (c) 類 15 列中 8 列同時屬 (b)（Personal Account 之 keyboard 輸入 popup），`class` 欄以 `b+c` 併記 |

---

## 十、獨立判斷 —— 本包是否仍有該驗而未驗者

**有，六項。**

1. **四條 TC 一次都沒有在真機或台架上跑過。** 本包驗的是「TC 寫得對不對」
   （lint、引文複驗、欄位對映），不是「照著做會不會過」。
   `-002-01` 之「5 秒」、`-002-03` 之「5 秒內」、`-002-04` 之「3 秒內」
   都假設人手操作跟得上；3 秒時窗在真機上是否可靠地做得到，**未驗**。
2. **`PU0580` 之 touch-outside 是否真的啟用，只有 Pop Up List 的
   `Exit Conditions` 字串為證。** 037 K12 自陳該機制
   `default to disable, requester should call the API to enable` ——
   亦即真正的啟用狀態在**程式碼**裡，不在該表。表上寫了不等於實作打開了。
   這條 TC 若在台架上不重現，第一個要懷疑的是這裡，不是 TC。
3. **`spec_reference` 之值只驗了「取自 037 C 欄逐字」與 SYS1 outline 有這節，
   沒驗「這節的內容真的涵蓋該 TC 所測的行為」。** `_5.6` 對四條都成立
   是因為 GP4 一條涵蓋四途徑；但這是我讀出來的，不是機器驗的。
4. **規格 PDF 之 21 頁圖面仍完全未讀**（spec_mode C 之管線一次未跑）。
   上繳包 01 §十一-3 記的同一項，本包未動。GP4 若有圖面補充敘述，未納入。
5. **`lint036` 之 21 項全綠不等於 TC 對。** lint 是機械層；
   canon §1.2 之三層品質為 lint → **pilot 人工閘** → done region 仲裁，
   本 feature **無 done region**（BLANK），第三層不存在 ——
   亦即 **pilot review 是唯一的人工閘，沒有第二道**。
6. **Priority 之 P1 與 Design Method 之四條同值，都是單人判斷。**
   四條 TC 拿到同一個設計方法，可能是因為它們真的同型，
   也可能是因為我沒有分辨。IN §12 之 first-match 我走了一遍，
   但「時間到自動關」要不要算 Fault Injection（該列字面含 `timeout`）
   是個我判了而沒有第二人覆核的岔路。

---

## 十一、待裁清單

| 項 | 問題 | 影響 |
|---|---|---|
| **A-POP8** | `-002-05` 之 search keyboard 查無對應列 —— 三提案（認 PU0022/0023／改以 multi-task 為判準／向上游索件）擇一 | **第 5 條 TC 生不生得出來** |
| **A-POP7** | `-002-02` 之 hard-button 分支是否併入 RD-1 索取 | 是否補第 6 條 TC |
| **A-POP6** | `編號重複` 是否限同表內；前綴抽取是否限主登記表 | 兩個 feature 之假陽性；四個 feature 之抽取盲區 |
| Priority | 四條 TC 為 P1 或 P0（TCP 兩讀法俱在，見 §6.6）| 全批優先級 |
| Estimated Test Time | Q 欄之政策（留空／估值／NA）| 交付欄位完整性 |
| pilot review | 四條 TC 之內容審查（唯一人工閘，無 done region 可仲裁）| P6 能否起跑 |

## 十二、本包產生／修改之檔

```
scripts/rulings_hash.py                      （修，R-POP11）
scripts/lint_docs036.py                      （修，R-POP10）
tests/test_lint_docs036.py                   （+5 支測試）
docs/fw036/RULINGS.sha.tsv                   （重產，246 → 548 列）
features/popup/DECISIONS.md                  （Sign-off 轉錄）
features/popup/feature.yaml                  （popup_list 接線、tc_id_format）
features/popup/ANOMALIES.md                  （A-POP1/2/3/4 處分；新開 A-POP5~8）
features/popup/DATA_REQUESTS.md              （執行層回報段）
features/popup/data/popup_list_candidates.tsv（345 列，帶來源 sha）
features/popup/scripts/gen_pilot.py          （新）
features/popup/generated/pilot_01.json        （4 條，含 reasoning 與 pu_citation）
features/popup/sandbox/pilot01/…_ext.xlsx     （4 列 × 15 欄）
features/popup/reports/popup_…_20260827.md    （lint 報告）
features/popup/docs/upstream/02_…md           （本檔）
features/popup/docs/INDEX.md                  （第 02 列）
```

**未執行任何改狀態之 git**（R-G5、R-G6）。唯讀之 `git status` 於 §一
之前置確認執行一次，輸出為空。
