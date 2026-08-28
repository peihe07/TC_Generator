# RULINGS — Popup（Pop-Up Queue and Priority Management 接手案）

取號依 R-G23′：落檔當下 live 取號（本檔建立時無既存 `### R-POP`，自 1 起）。

---

### R-POP1 — slug 與目錄（Pei 裁，2026-08-27）

Popup 立為獨立 feature，slug = `popup`。目錄 `features/popup/`，
投遞區 `_intake/Popup/`（TitleCase，R-G24 已建妥並實測）。
Feature 接手名稱「Pop-Up Queue and Priority Management」為工單稱謂；
目錄與 slug 不帶 queue/priority 字樣（現有 037 內容見 R-POP2）。

### R-POP2 — 生成範圍照 037 為準（Pei 裁，2026-08-27）

生成範圍以 `FMWIFSM037A03N1LSWE1PopupHMIV0.2` Analysis Report 現有
5 個 Functional Requirement leaf（SWE1-POP-002-01 ～ -002-05）為準。
Queue／priority 本體（GP2 = spec 5.4、HMI Popup List Priority Matrix
所定義之優先權行為）於 037 V0.2 無任何 SWE1 列 —— 此缺口以 RD-1
具名上報，不自行擴充（IN §8.2.1、IN §8.4.2）。缺口記入
`COVERAGE_GAPS.md`。

### R-POP3 — DR 三件開立（Pei 裁，2026-08-27）

DR-POP1（HMI Popup List）、DR-POP2（HMI Popup List Priority Matrix）、
DR-POP3（SWE1-POP-004 懸空引用之更正）開立，登錄於本 feature
`DATA_REQUESTS.md`。送出時點由 Pei 決定（Tier 3）。

### R-POP4 — 框架（Pei 裁，2026-08-27）

Test Group = `Popup`；Test Set 單一 `Pop-up Close`（5 leaf 同一
capability，IN §4.1.3 granularity test 通過）。Queue／priority 若日後
補件（037 增補或 RD-1 回覆）再增 Test Set。Layer 3 見 framework.md
Part N（落檔於 framework 鎖定時）。

### R-POP5 — Heading 列之台帳處置 [DEFAULT]（分析層先裁，待 Pei 追認）

覆蓋台帳收錄 Analysis Report 全部 7 列。Heading 2 列處置：
- SWE1-POP-002 標 `No TC — Heading; refer to child IDs -002-01..-05`
- SWE1-POP-001 標 `No TC — Heading; duplicated of SWE1-POP-002-02`
  （037 原文 K8 逐字：「Duplicated feature of SWE1-POP-002-02」）
沿 bed_lowering R-BLM2 前例形制。Pei 得於審查時否決改裁。

### R-POP6 — Pop Up List 納入為素材（Pei 裁，2026-08-27，A-POP2 甲半）

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

### R-POP7 — Priority Matrix 不納入（Pei 裁，2026-08-27，A-POP2 乙半）

`forms/Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`
不納入為生成素材：版次 SR24 1A 早於基線（SR24 Post 2A）兩代，且
R-POP2 已將 queue／priority 排除於生成範圍。DR-POP2 保持開啟，
改記「repo 存 SR24 1A 舊版於 forms/，向上游索 SR24 Post 2A 現版」。

### R-POP8 — -002-02 之 spec_reference 併列兩節（Pei 裁，2026-08-27，A-POP3 採甲）

SWE1-POP-002-02 衍生 TC 之 specification_reference 併列兩行（升冪，
前綴逐行重述，IN §10.7）：
`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.5`
`SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.6`
兩值皆為 037 C 欄逐字（C8／C10 起），非分析層推定之章節錨（與
bed_lowering R-BLM5 之 A-BLM4 情境不同，本 feature 不需 override）。
其餘 leaf 單行 `_5.6`。理由：GP3 與 GP4 第 2 途徑為同一行為之兩處敘述
（037 K8 之 duplicated 判定與規格對得上），該 TC 所直接驗證者含兩節
（IN §9-16）。

### R-POP9 — A-POP1 修正追認＋傳染性掃描（Pei 裁，2026-08-27）

追認 `scripts/extract_source.py` 之修正：`safe_name()` 只剝尾端、
加 casefold 撞名守衛（撞名即停）、兩支迴歸測試。
backlog 一項隨 02 包執行：抽取類腳本之同型名稱正規化函式傳染性掃描
（FO §5a-6：字串比對缺陷具傳染性），逐支回報有無同缺陷。

### R-POP10 — lint 跳號檢查改前綴自動抽取（Pei 裁，2026-08-27，A-POP4 處置）

`lint_docs036.py` 跳號檢查之前綴清單改為自動抽取（掃描台帳全文之
`(A|DR|R)-[A-Z]+` 前綴逐一檢查跳號），並接 G-B 餘數對照（抽得前綴集
與硬寫時代清單之差集回報）。迴歸要件（G-K／G-N）：已知案例 A-POP／
DR-POP 須轉為受檢，並以「注入跳號即 FAIL」實證其會轉紅。
不採「硬寫清單再加 POP」。**全域效力之工具政策，候升格 R-G。**

### R-POP11 — rulings_hash 範圍納 feature RULINGS（Pei 裁，2026-08-27）

`scripts/rulings_hash.py` 預設範圍納入 `features/*/RULINGS.md`，
重產 `docs/fw036/RULINGS.sha.tsv`。invariant：既有 R-G 條之 sha 不得
因本次擴範圍而變（變動即停下回報）。理由：R-G13 明定條文落各 feature
之 RULINGS.md，tsv 不涵蓋則引用制半殘。
**全域效力之工具政策，候升格 R-G。**

### R-POP12 — -002-02 不拆，軸不存在（分析層裁 [DEFAULT]，2026-08-27，**A-POP7**）

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

### R-POP13 — TC ID 前綴定值（分析層裁 [DEFAULT]，2026-08-27，**A-POP9**）

TC ID 採 `NR1L-Popup-{NNN}`。依據：分析層 2026-08-27 實測五本交付／
產出簿之欄 F（Test Case ID）：

| 簿 | 前綴 | 列數 |
|---|---|---|
| `features/power/delivered/pm_29.xlsx` | `NR1L-PowerManagement` | 389 |
| SXM 20260813 | `NR1L-SXM` | 215 |
| UserProfiles 20260819 | `NR1L-UserProfiles` | 189 |
| TimeManagement 20260825 | `NR1L-TimeManagement` | 59 |
| Display 20260826 | `TC-DM` | 23 |

4/5 為 `NR1L-{FeatureName}-{NNN}`，Display 為離群（不取為基準）。
pilot 現值 `newR1L-POP-{NNN}` 兩處皆錯（`newR1L`≠`NR1L`；
縮寫 `POP`≠全名 `Popup`），全數重排，NNN 序不變。
feature.yaml 之 `project` 模板殘值 `PROJ` 同步修正。

### R-POP14 — -002-05 採規格原句生成（分析層裁 [DEFAULT]，2026-08-27，**A-POP8**）

**A-POP8** 三案採**乙案改良**：-002-05 照 GP4-4 規格原句生成，
`spec_reference` 單行 `_5.6`，**不引 PU**。理由：GP4-4 為規格自載之行為
陳述，`e.g in the search keyboard` 是規格自己的舉例，**不是向 Pop Up List
之委派**（對照 GP4-1 逐字 `timeout is defined in Pop-up List document`
才是委派）。故不適用 R-POP6 之值引用規則，亦無須 PENDING。
另開 **DR-POP4** 索 multi-task popup 之完整例外清單（不阻斷；
回覆前不得自行列舉 search keyboard 以外之實例，IN §8.4.1）。

### R-POP15 — Pilot 修正六件之判準（分析層裁，2026-08-27）

分析層於 pilot 覆核所立之判準，逐件適用於本 feature 全簿：

- **F1** Final Step 須含 check target：`Read <對象> and check that <可觀察結果>`
  （IN §5.5；形制取 canon §8.7.5(b) 之 `Read the signal ... and check that ...`）。
  單寫 `Read <對象> status` 而將判斷全數推給 ER，不合格。
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

### R-POP16 — lint 新規命中之三分法處置（分析層裁 [DEFAULT]，2026-08-27，A-POP6）

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

### R-POP17 — 上繳回報與 repo 台帳不符之登記（分析層裁，2026-08-27，A-POP9）

下放包 02 之上繳回報與 repo 台帳實況於四點不符（anomaly 編號錯置、
A-POP5 未提、傳染性掃描結論相反、TC ID 前綴述值與語料不同）。
登為 **A-POP9**（詳 ANOMALIES.md）。處置：

1. 上繳包之摘要須自 repo 台帳 live 產，不得手寫重述；號碼與狀態兩項
   尤其。
2. `ledger_xref.py` 增一檢：下放包／上繳包內之 `A-\w+\d+`／`DR-\w+\d+`
   引用，與該 feature 台帳之實存號碼及其標題對不上即回報。
   這正是 `ledger_xref` 設計目的內而未涵蓋之型態。
3. 分析層同受此規（見 R-POP15 F5 之註）。
