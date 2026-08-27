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
