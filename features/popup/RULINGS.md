# RULINGS — Popup（Pop-Up Queue and Priority Management 接手案）

取號依 R-G62′：落檔當下 live 取號（本檔建立時無既存 `### R-POP`，自 1 起）。

---

### R-POP1 — slug 與目錄（Pei 裁，2026-08-27）

```
Popup 立為獨立 feature，slug = `popup`。目錄 `features/popup/`，
投遞區 `_intake/Popup/`（TitleCase，R-G24 已建妥並實測）。
Feature 接手名稱「Pop-Up Queue and Priority Management」為工單稱謂；
目錄與 slug 不帶 queue/priority 字樣（現有 037 內容見 R-POP2）。
```

### R-POP2 — 生成範圍照 037 為準（Pei 裁，2026-08-27）

```
生成範圍以 `FMWIFSM037A03N1LSWE1PopupHMIV0.2` Analysis Report 現有
5 個 Functional Requirement leaf（SWE1-POP-002-01 ～ -002-05）為準。
Queue／priority 本體（GP2 = spec 5.4、HMI Popup List Priority Matrix
所定義之優先權行為）於 037 V0.2 無任何 SWE1 列 —— 此缺口以 RD-1
具名上報，不自行擴充（IN §8.2.1、IN §8.4.2）。缺口記入
`COVERAGE_GAPS.md`。
```

### R-POP3 — DR 三件開立（Pei 裁，2026-08-27）

```
DR-POP1（HMI Popup List）、DR-POP2（HMI Popup List Priority Matrix）、
DR-POP3（SWE1-POP-004 懸空引用之更正）開立，登錄於本 feature
`DATA_REQUESTS.md`。送出時點由 Pei 決定（Tier 3）。
```

### R-POP4 — 框架（Pei 裁，2026-08-27）

```
Test Group = `Popup`；Test Set 單一 `Pop-up Close`（5 leaf 同一
capability，IN §4.1.3 granularity test 通過）。Queue／priority 若日後
補件（037 增補或 RD-1 回覆）再增 Test Set。Layer 3 見 framework.md
Part N（落檔於 framework 鎖定時）。
```

### R-POP5 — Heading 列之台帳處置（分析層先裁；**Pei 追認 2026-08-28**）

```
覆蓋台帳收錄 Analysis Report 全部 7 列。Heading 2 列處置：
- SWE1-POP-002 標 `No TC — Heading; refer to child IDs -002-01..-05`
- SWE1-POP-001 標 `No TC — Heading; duplicated of SWE1-POP-002-02`
  （037 原文 K8 逐字：「Duplicated feature of SWE1-POP-002-02」）
```
沿 bed_lowering R-BLM2 前例形制。

**追認（2026-08-28，Pei「都裁過了」）**：照現裁確定，不再為 [DEFAULT]。

### R-POP6 — Pop Up List 納入為素材（Pei 裁，2026-08-27，A-POP2 甲半）

```
納入 `forms/Pop Up List HMI R1 (26PI).xlsx`（Main A1 逐字
`SR24 Post 2A CR25802`，與本 feature 規格基線同代）為 popup 素材，
**引用原位不搬**（既有共用件，sw_update A-SU3 前例；R-G27「既有檔案
不搬移」同精神）。feature.yaml `paths.popup_list` 指向之。DR-POP1 結案。

-002-01／-002-03／-002-05 之 TC 以該表實值填寫：選定 PU 逐字引值，
PU id 併記；PU 引文之控制記法（如 `<OK>`、`[OK, X]`）沿 IN §11
profile-scoped 例外（前例 Home A-H10）。

殘留兩點隨 RD-1 確認、不阻斷：
(a) CR25802（Pop Up List）vs CR22510（規格封面）之版位關係；
(b) 檔名 `(26PI)` 標記之車型／程式適用性。
```

### R-POP7 — Priority Matrix 不納入（Pei 裁，2026-08-27，A-POP2 乙半）

```
`forms/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`
不納入為生成素材：版次 SR24 1A 早於基線（SR24 Post 2A）兩代，且
R-POP2 已將 queue／priority 排除於生成範圍。DR-POP2 保持開啟，
改記「repo 存 SR24 1A 舊版於 forms/，向上游索 SR24 Post 2A 現版」。
```

### R-POP8 — -002-02 之 spec_reference 併列兩節（Pei 裁，2026-08-27，A-POP3 採甲）

```
SWE1-POP-002-02 衍生 TC 之 specification_reference 併列兩行（升冪，
前綴逐行重述，IN §10.7）：
`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.5`
`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.6`
兩值皆為 037 C 欄逐字（C8／C10 起），非分析層推定之章節錨（與
bed_lowering R-BLM5 之 A-BLM4 情境不同，本 feature 不需 override）。
其餘 leaf 單行 `_5.6`。理由：GP3 與 GP4 第 2 途徑為同一行為之兩處敘述
```
（037 K8 之 duplicated 判定與規格對得上），該 TC 所直接驗證者含兩節
（IN §9-16）。

### R-POP9 — A-POP1 修正追認＋傳染性掃描（Pei 裁，2026-08-27）

```
追認 `scripts/extract_source.py` 之修正：`safe_name()` 只剝尾端、
加 casefold 撞名守衛（撞名即停）、兩支迴歸測試。
backlog 一項隨 02 包執行：抽取類腳本之同型名稱正規化函式傳染性掃描
（FO §5a-6：字串比對缺陷具傳染性），逐支回報有無同缺陷。
```

### R-POP10 — lint 跳號檢查改前綴自動抽取（Pei 裁，2026-08-27，A-POP4 處置）

```
`lint_docs036.py` 跳號檢查之前綴清單改為自動抽取（掃描台帳全文之
`(A|DR|R)-[A-Z]+` 前綴逐一檢查跳號），並接 G-B 餘數對照（抽得前綴集
與硬寫時代清單之差集回報）。迴歸要件（G-K／G-N）：已知案例 A-POP／
DR-POP 須轉為受檢，並以「注入跳號即 FAIL」實證其會轉紅。
不採「硬寫清單再加 POP」。**全域效力之工具政策，候升格 R-G。**
```

### R-POP11 — rulings_hash 範圍納 feature RULINGS（Pei 裁，2026-08-27）

```
`scripts/rulings_hash.py` 預設範圍納入 `features/*/RULINGS.md`，
重產 `docs/fw036/RULINGS.sha.tsv`。invariant：既有 R-G 條之 sha 不得
因本次擴範圍而變（變動即停下回報）。理由：R-G13 明定條文落各 feature
```
之 RULINGS.md，tsv 不涵蓋則引用制半殘。
**全域效力之工具政策，候升格 R-G。**

### R-POP12 — -002-02 不拆，軸不存在（分析層裁 [DEFAULT]，2026-08-27，**A-POP7**）

```
SWE1-POP-002-02 **不拆** device 軸，理由採「**規格側無此分支**」一說：
SYS1 5.6 逐字為 `pressing the button a second time`，未區分按鍵型別；
037 S11 之 `a physical hard button or a specific UI button on the screen`
是 VC 對「button」之列舉性註解，非規格分支；037 本身亦未拆為兩個
sub-id。依 IN §8.2（RD 為需求單位之權威）與 §8.4.2（規則定義地測試），
判一條 TC。

**本裁同時否決語料 reasoning 之另一套理由**（「是真軸，但 Pop Up List
無 hard-button 實例可填」）—— 那套理由蘊含「欠一條待補件」之結論，
與本裁不相容。語料之 reasoning 須改寫為本裁之理由（下放包 03 F6）。
不開 DR。037 VC 之措辭仍記 Remarks 供 RD-1 順帶確認（不阻斷）。

Pei 得於審查時否決改裁；若改採「真軸缺件」說，則須開 DR 並將
-002-02 視為未完成（欠 hard-button 一條）。
```

### R-POP13 — TC ID 前綴定值（分析層裁 [DEFAULT]，2026-08-27，**A-POP9**）

```
TC ID 採 `NR1L-Popup-{NNN}`。依據：分析層 2026-08-27 實測五本交付／
```
產出簿之欄 F（Test Case ID）：

| 簿 | 前綴 | 列數 |
|---|---|---|
| `features/power/delivered/pm_29.xlsx` | `NR1L-PowerManagement` | 389 |
| SXM 20260813 | `NR1L-SXM` | 215 |
| UserProfiles 20260819 | `NR1L-UserProfiles` | 189 |
| TimeManagement 20260825 | `NR1L-TimeManagement` | 59 |
| Display 20260826 | `TC-DM` | 23 |

```
4/5 為 `NR1L-{FeatureName}-{NNN}`，Display 為離群（不取為基準）。
pilot 現值 `newR1L-POP-{NNN}` 兩處皆錯（`newR1L`≠`NR1L`；
縮寫 `POP`≠全名 `Popup`），全數重排，NNN 序不變。

**修訂（2026-08-28，上繳包 03 §一-1）**：原末句「feature.yaml 之 `project`
模板殘值 `PROJ` 同步修正」**不再適用，此句撤回** —— `features/popup/feature.yaml` 無
`project` 鍵，全檔亦無 `PROJ` 字串（執行層 grep 實測命中 0）。
該句係分析層將 A-POP9(4) 所記之**錯誤述值**連同處分寫入本條，
致 A-POP9 之錯誤於其自身之處分條文內再現 —— **分析層之誤**。
實際標的為 `tc_id_format`，已由 `"newR1L-POP-{n:03d}"` 改為
`"NR1L-Popup-{n:03d}"`。

**量測界之訂正（同上，§一-2）**：下放包 03 §三「全簿掃 `newR1L`／
`PROJ`／`POP-` 命中須為 0」**不可達成且不應達成**：
`D2` 為專案名稱欄（母本自帶 `newR1L`，清成 0 等於改動專案名稱）；
`D10:D14` 為 req_id `SWE1-POP-002-0n`（掃到 0 即 req_id 被抹）。
正確量測界採執行層之改定：`newR1L`／`PROJ` 限**本包產出之語料
與儲存格**；`POP-` 限 **TC ID 欄 F10:F1411**。
順帶：`D2` = `newR1L`（專案名稱）與交付簿欄 F = `NR1L-*`（TC ID）
為不同層之值，**不得以 D2 為 TC ID 前綴之權威**。
```

### R-POP14 — -002-05 採規格原句生成（分析層裁 [DEFAULT]，2026-08-27，**A-POP8**）

```
**A-POP8** 三案採**乙案改良**：-002-05 照 GP4-4 規格原句生成，
`spec_reference` 單行 `_5.6`，**不引 PU**。理由：GP4-4 為規格自載之行為
```
陳述，`e.g in the search keyboard` 是規格自己的舉例，**不是向 Pop Up List
之委派**（對照 GP4-1 逐字 `timeout is defined in Pop-up List document`
```
才是委派）。故不適用 R-POP6 之值引用規則，亦無須 PENDING。
另開 **DR-POP4** 索 multi-task popup 之完整例外清單（不阻斷；
回覆前不得自行列舉 search keyboard 以外之實例，IN §8.4.1）。
```

### R-POP15 — Pilot 修正六件之判準（分析層裁，2026-08-27）

```
分析層於 pilot 覆核所立之判準，逐件適用於本 feature 全簿：

- **F1** Final Step 須含 check target：`Read <對象> and check that <可觀察結果>`
  （IN §5.5；形制取 canon §8.7.5(b) 之 `Read the signal ... and check that ...`）。
  單寫 `Read <對象> status` 而將判斷全數推給 ER，不合格。
  **且受 IN §5.2B ≤ 18 words 拘束（R-POP20）** —— 細節留 ER。
- **F2** Procedure 之按壓標的一律 `"..."` 雙引號；PU 控制記法
  （`<OK>`、`<Trks>`）之保留**僅及於 ER 引文段與 test_item**
  （profile §2 自訂之界）。反引號等 Markdown 記號不得進交付欄（IN §11）。
- **F3** `The vehicle is stationary with the ignition in RUN` 類前提句**刪除**：
  popup 關閉行為之規格側無運動狀態觸發，屬 IN §8.5 之環境穩定性前提。
  （Home profile §3.2 得寫是因 HSD2/HSS2 使其成為規格觸發，本 feature 無此依據。）
- **F4** timeout 值單一欄位歸屬（IN §4.5）：內聯於 Procedure／ER，
  `input_test_data` 一律 `NA`（SWC 基準 285/286）。不得同值兩欄並存。
- **F5** 語料 reasoning 引用之 anomaly 號須與 ANOMALIES.md 一致（本例
  `pilot_01.json` 之 POP-002 reasoning 寫「登 A-POP7」但引用之事實屬
  A-POP7 本身，參照循環）。**號碼一律 live 查 ANOMALIES.md 後再寫，
  不得轉抄上繳包摘要之號碼**（分析層於 2026-08-27 即因轉抄而誤將
  R-POP12／13／14 掛錯 anomaly，已更正 —— 分析層之誤）。
- **F6** 語料 reasoning 與上繳包回報之理由不得為兩套；不一致時以裁定
  （本例 R-POP12）為準，語料改寫。
```

### R-POP16 — lint 新規命中之三分法處置（分析層裁 [DEFAULT]，2026-08-27，A-POP6）

```
A-POP6 三類逐類處置：

- **甲（真陽性 5 筆，sxm／audio_mgmt／time_management）**：屬各該 feature
  之台帳，**本 feature 不代改**（R-G 之單一擁有者原則）。逐筆登入各該
  feature 之 BACKLOG，於其下一次開工時處理。本包只造清單不碰檔。
- **乙（誤傷 2 筆，power_moding／projection）**：採其提案 1＋2。
  「編號重複」改為**同一表格內**重複才判紅，跨表重複降為 note；
  前綴抽取限定於**檔內首個表格**（辨識方式定為此 —— 不採「表頭首欄
  字面」，因各 feature 表頭不一致，而首個表格為三簿體例之不變量）。
- **丙（盲區 4 feature，amfm／home／media／user_profiles）**：登為 G-D
  盲區，**不強制統一版面**。lint 須於抽得前綴集為空時
  **明示回報「no series detected」而非靜默 PASS**（G-D：PASS 不得
  與「已驗」混同）。`privacy` 之假前綴 `S` 於改限首個表格後自然排除，
  需實證。
```

### R-POP17 — 上繳回報與 repo 台帳不符之登記（分析層裁，2026-08-27，A-POP9）

```
下放包 02 之上繳回報與 repo 台帳實況於四點不符（anomaly 編號錯置、
A-POP5 未提、傳染性掃描結論相反、TC ID 前綴述值與語料不同）。
登為 **A-POP9**（詳 ANOMALIES.md）。處置：

1. 上繳包之摘要須自 repo 台帳 live 產，不得手寫重述；號碼與狀態兩項
   尤其。
2. `ledger_xref.py` 增一檢：下放包／上繳包內之 `A-\w+\d+`／`DR-\w+\d+`
   引用，與該 feature 台帳之實存號碼及其標題對不上即回報。
   這正是 `ledger_xref` 設計目的內而未涵蓋之型態。
3. 分析層同受此規（見 R-POP15 F5 之註）。
```

### R-POP18 — 主表辨識改內容判準（分析層裁，2026-08-28，A-POP10）

```
**R-POP16 乙之「首個表格為三簿體例之不變量」一語經實測不成立**，本條取代
其中「抽取限於檔內首個表格」一項（其餘兩項不變）。依據：上繳包 03
§七 A-POP10 實測 —— sxm／audio_mgmt／projection／privacy 之首個表格
皆非登記表，power 之登記表又被空行切段；因此丟棄之真陽性為
**sxm 4／audio_mgmt 7／projection 63**。

**改採內容判準**（不以位置辨識）：一張表格若其**首欄有 ≥ 2 列
匹配 `^(A|DR|R)-[A-Z]+\d+$`**（去除包覆之 `[]`、粗體記號後），
即視為登記表，受跳號檢查；一檔可有多張登記表（power 之切段情形），
同檔各登記表之編號收為一個序列後再判跳號。
非登記表（指紋表、計數表、欄位值表）自然排除 —— `privacy` 之假前綴
`S` 以本判準亦排除（需實證，不得推定）。

另採標題式登記：`## A-XXn` 與 `## [A-XXn]` 兩式皆認
（audio_mgmt／driver_distraction／sxm 之體例）。

**本條不及於 `ledger_xref.py`** —— 存在性檢查不需先認定主表，
該工具跨全檔收集之現行作法正確，二者分野維持（已記於其檔頭）。

**實作二項追認（2026-08-28，上繳包 04 §三）**：

1. **第二條門檻：單列但佔該表首欄非空格 ≥ 50% 者亦算登記表**。
   理由正確：power 之 `A-PW` 主表被空行切段，其中有單列續段；
   只用 ≥ 2 列會把續段丟掉 —— 那是以另一種方式重蹈 A-POP10。
   兩條門檻皆擋得住 privacy 之欄位值表（`S10` 1/6 = 17%）。
2. **標題式登記只作存在性佐證，不參與重複判定**。
   執行層已實證兩個方向皆會出錯：一併算重複 → popup 之
   「主表一列 ＋ `## A-POPn` 明細節一節」每號皆變跨表同號（11 筆 note）；
   有表格就不看標題 → sxm 之 A-SX18／19 又被判跳號（A-POP11 之重現）。
   先證偽兩方向再定案，而非定案後找支持。
```

### R-POP19 — A-POP6 甲類之 sxm 兩筆撤回（分析層裁，2026-08-28，A-POP11）

```
A-POP6 甲類之 `A-SX18`／`A-SX19` **為假陽性，撤回**：sxm 以標題式
登記，`A-SX` 實存集為 1–30 連續零跳號，兩號皆實存且皆 RESOLVED。
執行層未寫入 sxm BACKLOG、未建該檔、未代改，處置正確。

A-POP6 甲類之訂正後數字：**2 個 feature／2 筆**
（audio_mgmt `DR-AM7`、time_management `A-TM2`），已入兩本 BACKLOG。
A-POP6 §甲 原標題「4 個 feature，5 筆」與其自身表列「3 個 feature、4 筆」
亦不符 —— 三個數字並陳，以本條之 **2／2** 為準。
```

### R-POP20 — F1 修正過長之回調（分析層裁，2026-08-28，編號 F7）

```
F1 之實作使四條之 Final Step 超出 IN §5.2B 之 **≤ 18 words**。
分析層逐條數詞（以空白切詞，`(sec)` 之括弧不計）：

| 條 | Final Step 詞數 | 判 |
|---|---|---|
| NR1L-Popup-001 | 31 | 超 |
| NR1L-Popup-002 | 19 | 超 |
| NR1L-Popup-003 | 29 | 超 |
| NR1L-Popup-004 | 29 | 超 |
| NR1L-Popup-005 | 17 | 合格 |

**回調原則**：Final Step 只留「動作 ＋ check that ＋ 主要可觀察結果」；
**時限、PU 欄位出處、時窗對照等細節全數留於 ER**（ER 已載，不損資訊）。
例：001 之 Final Step 改為
`Read the pop-up display status and check that the pop-up has closed by itself`（13 words），
「5 秒、PU0942 Timeout (sec)」由 ER 3 承載（現行 ER 3 即已具足，不需改）。

本條不推翻 F1 —— check target 仍必須；只限制其長度。
R-POP15 F1 之條文需同步加註「且受 IN §5.2B ≤ 18 words 拘束」。

**詞數算法之訂正（2026-08-28，上繳包 04 §二-1）**：上表措辭
「`(sec)` 括弧不計」**有誤** —— 執行層三種算法實測顯示，唯將
`(sec)` **計為一詞**方重現得出 31／19／29／29／17。
正確算法：**去 `N. ` 序號後 `str.split()`，`(sec)` 計為一詞**。
```
分析層之誤 —— 寫條文時未回測自身所列數字之可重現性。
執行層揭露出入而不自改條文，處置正確。

```
**001 之例外追認**：回調後保留 `the elapsed time`（未逐字照抄
本條示例）**正確** —— 該條之受測量本就有二（顯示狀態 ＋ 經過時間），
只留其一會使步驟讀不出要量時間。本條之示例為形制，非逐字模板。
```

### R-POP21 — 節號列舉不得省略 canon 前綴（分析層裁，2026-08-28）

```
下放包／上繳包／台帳內列舉多個節號時，**每一個節號皆須冠 canon
前綴**（`IN §4.5`、`IN §5.2B`…）。縮寫式 `IN §4.5／§5.2B／§5.5`
之第二個以後成為**裸引用**，`canon_refs` 判為 FO／IN 兩 canon
共用之歧義引用而計入未解決數。

來源：上繳包 04 §八-5 —— 執行層於作業中自產此錯（canon_refs 471）
並自修回 470，一併記錄。這是可複製之寫作陷阱，不是一次性筆誤；
分析層寫包同受此規。**全域效力之寫作規約，候升格 R-G。**
```

### R-POP22 — Estimated Test Time（Q 欄）留空（分析層裁 [DEFAULT]，2026-08-28）

```
Q 欄（`Estimated Test Time`）**留空，不寫入**。
```
依據：分析層 2026-08-28 實測五本交付／產出簿（以表頭含
`Estimated` 定位得欄序 16，逐列，以 TC ID 欄非空為母體）：

| 簿 | Q 欄非空列 | 母體列數 |
|---|---|---|
| `features/power/delivered/pm_29.xlsx` | 0 | 389 |
| SXM 20260813 | 0 | 215 |
| UserProfiles 20260819 | 0 | 189 |
| TimeManagement 20260825 | 0 | 59 |
| Display 20260826 | 0 | 23 |
| **合計** | **0** | **875** |

```
875/875 留空、零例外 —— 此為既定實務而非待決政策，不需上呼。
P 欄（Priority，欄序 15）照常寫入（IN §10.2）。Pei 得否決改裁。
```

### R-POP23 — -002-05 之 design_method 維持狀態轉換（Pei 追認，2026-08-28）

```
`NR1L-Popup-005` 之 `design_method` **維持 `狀態轉換 (State Transition
Testing)`**，不改負向測試。理由：受測者為同一台 popup 狀態機於
```
**合法輸入下不發生轉移**，仍屬 state-change focus；IN §12 之
Negative / Invalid 指**非法輸入或非法操作**，而 GP4-4 所述之按鍵
是合法操作。五條同法亦便對讀。

執行層於上繳包 03 §四 已將本選擇及其候補（負向測試）揭露備查，
揭露處置正確。

### R-POP24 — `scripts/ledger_xref.py` 之存續與接入（Pei 追認，2026-08-28）

```
1. **不合併** —— `scripts/ledger_xref.py`（跨 feature 機械對照）與
   `features/vehicle_category/scripts/ledger_xref.py`（同一標的多處記載
   並列供人判讀）**用途不同**，各自存續。同名之混淆風險以兩檔檔頭
   各自聲明其問題形態化解。
2. **不接入 `gate_all.py`** —— 跨 feature 實測 6 綠／6 紅
   （power_moding 7、driver_distraction 7、projection 24、
   time_management 29、audio_mgmt 43、vehicle_setting 473），
   接入即全 repo 轉紅。**接一支已知會紅而被容忍之閘，等於讓該閘失效**。
   待各 feature 台帳收斂至可接受水位後再議，屆時需先定基線。
3. 現階段以 `--feature <f>` 手動調用為主，各包之收斂複驗必跑。
```

### R-POP25 — `forms/` 落點政策（分析層裁 [DEFAULT]，2026-08-28）

```
**取號與權限聲明**：Pei 於 2026-08-28 之「都裁過了」未攜帶本項之
方向（分析層於下放包 05 §九-4 亦未提意見）。為不再以同一問題
上呼，分析層以 [DEFAULT] 裁之，Pei 得隨時否決。

`forms/` 實存 12 項，而 R-G2 字面只允 `…_SWQT_20260817_ext.xlsx`
一件。二者之差以**承認現狀、補登記**解，不以搬檔解：

1. **不搬入 `sources/raw/`**。`sources/` 之組織單位為 doc_id，
   `MANIFEST.tsv` 綁 feature intake；而 `forms/` 之 12 項為**跨 feature
   共用參考件**（DBC、PROXI、HMI Settings List、LID、Pop Up List…）。
   搬檔將斷掉至少 popup（`paths.popup_list`）、sw_update（A-SU3）、
   display／vehicle_category（`inputs/` 副本）之現行路徑，
   改動面遠大於所解之問題。
2. **`forms/` 定位為「跨 feature 共用參考件之單一落點」**；
   R-G2 字面之範圍陳述已不符實務，**候升格 R-G 時一併修辭**。
3. **每一項須登錄於 `forms/FORMS.md`**，至少載檔名、sha256、
   版次／基線、引用之 feature。**現有兩件 Pop Up 未登錄**
   （`grep -i "pop up" forms/FORMS.md` 命中 0），須補。
4. **feature 專用檔不得放 `forms/`** —— 歸該 feature 之 `inputs/`
   或 `sources/`。

本條之實作限於「登錄」，**不移動、不刪除任何檔**。
```

### R-POP26 — 升級條件命中即停；條件不得以可過期之白名單寫成（分析層裁，2026-08-28）

**緣起**：上繳包 05 §六 —— 下放包 05 §八-4 之升級條件
「除 R-POP18、R-POP20 外之既有 sha 變動」命中（R-POP5、R-POP13），
執行層**未停下**，以「成因已具名且可以 git diff 證之」為由照常完包。

```
**實質判斷正確，程序判斷錯誤。兩層分別裁定：**

**一、實質：採納**。R-POP5（追認標記）與 R-POP13（措辭訂正）
之 sha 變動確為分析層本輪自身落檔所致，非語料漂移亦非工具異常；
R-POP23／24／25 之新增同理。交付物未受影響。

**二、程序：不採**。升級條件是**停止信號**，不是可供爭執之題。
允許「說得出成因就可以不停」，等於將停止門檻交給執行層自定，
而執行層對自身成因之說明正是該條件要驗證的對象。
**此理即 R-POP24 第 2 點之理**：接一支已知會紅而被容忍之閘，
等於讓該閘失效；一個命中後可以被論理推翻之升級條件，同樣失效。
正確作法：**停下，連同成因分析一併上繳**，由分析層一句放行；
本例之成本僅一個往返。
```

**三、分析層之缺陷（本條之主因）**：該升級條件以
**枚舉式白名單**（「除 X、Y 外」）寫成，而白名單寫於下放包 §九
四項裁定**之前** —— R-POP23／24／25 與 R-POP5 之追認正是那四項之處分。
白名單於執行時已過期，而仍以它作為停止判準。

```
**今後寫法**：升級條件不得枚舉具體條號作白名單，改以**性質**寫定，
例：「`RULINGS.sha.tsv` 出現**無法以本輪分析層落檔或本包作業解釋**
之 sha 變動」。如此則新增之裁定不會變成偽陽性，而真正的漂移仍會命中。

**本例不追究**，交付物照收；程序之裁自下一包起適用於雙方。
```
