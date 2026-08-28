# 上繳包 04 — F7 回調、判準改內容判準、台帳收斂

日期：2026-08-28
Feature slug：`popup`
對應下放：[handoff/04_f7_ledger_close.md](../handoff/04_f7_ledger_close.md)
執行層：Claude（Opus 5）

**總判：全項完成，§十 升級條件五項全部未命中。**
F7 回調後五條 Final Step 皆 ≤ 18 words 且皆保留 check target，ER 一字未減。
R-POP18 之內容判準四向迴歸全過，A-POP10 所記之丟棄真陽性 **74 筆全數回收**
（sxm 4／audio_mgmt 7／projection 63 → 0／0／0），並因此**新浮現三筆真缺陷**，
已只造清單入各該 feature 之 BACKLOG。§六 複驗確認 03 §十三 **僅第 9 項失準**，
無第二項。`gate_all` 五支中兩支綠、三支紅，**三支紅之中兩支非本包所致**，
逐支歸因見 §八-5。

---

## 一、承 §一：分析層兩處自認之誤，執行層之回應

下放包 04 §一已將上繳包 03 §一-1／§一-2 收為分析層之誤並修訂 R-POP13。
**本包確認該修訂已落 repo**：`features/popup/RULINGS.md` 之 R-POP13 現載
「**修訂（2026-08-28，上繳包 03 §一-1）**：原末句…**作廢**」與
「**量測界之訂正（同上，§一-2）**」兩段，且採用了執行層改定之量測界
（`newR1L`／`PROJ` 限本包產出、`POP-` 限 F10:F1411）。

R-POP13 之 sha8 因此變動（`9b835066` → `bcd97ba8`），屬 §七 所預期，
見 §八-4。

---

## 二、F7 回調（R-POP20）—— 本包主件

### 2.1 詞數算法之出入（先揭露）

R-POP20 之表寫「以空白切詞，`(sec)` 括弧不計」。**實測：唯有把 `(sec)`
當成一個詞計入，才重現得出該表之 31／19／29／29／17。**

| 算法 | 001 | 002 | 003 | 004 | 005 |
|---|---|---|---|---|---|
| 含 `N. ` 序號 | 32 | 20 | 30 | 30 | 18 |
| **去序號、`(sec)` 計為一詞** | **31** | **19** | **29** | **29** | **17** |
| 去序號、`(sec)` 不計 | 30 | 19 | 28 | 28 | 17 |

中列與 R-POP20 完全相符，故本包以**中列**為算法，並在 `gen_pilot.py`
之 `audit()` docstring 內記明此出入。**未改寫 R-POP20 之措辭**（不自為）。

### 2.2 逐條回調（回調後詞數為工具實測輸出）

| 條 | 回調前 | 回調後 | Final Step 本文（回調後） |
|---|---|---|---|
| NR1L-Popup-001 | 31 | **16** | `Read the pop-up display status and the elapsed time, and check that the pop-up has closed` |
| NR1L-Popup-002 | 19 | **17** | `Read the pop-up display status immediately after the second press and check that the pop-up is closed` |
| NR1L-Popup-003 | 29 | **16** | `Read the pop-up display status immediately after the tap and check that the pop-up is closed` |
| NR1L-Popup-004 | 29 | **16** | `Read the pop-up display status immediately after the press and check that the pop-up is closed` |
| NR1L-Popup-005 | 17 | **17** | （不動）`Read the pop-up display status immediately after the press and check that the pop-up is still displayed` |

**五條皆 ≤ 18，五條皆含 `check that`。**

001 之回調保留了「the elapsed time」—— R-POP20 之示例
（`Read the pop-up display status and check that the pop-up has closed by itself`）
把它一併拿掉了，但該條之受測量本就有二（顯示狀態＋經過時間），
只留其一會使步驟讀不出要量時間。加回後為 16 words，仍在界內。
**這是本包唯一一處未逐字照抄 R-POP20 示例之處，特此揭露。**

### 2.3 ER 一字未減（§十第 1 項升級條件之複驗）

回調把細節退回 ER —— 但 ER 本來就已載，故**本包未改動任何一條之 ER**。
逐條與上繳包 03 §十二 之 ER 全文比對，**五條全同**。關鍵細節之落點：

| 細節 | 回調前所在 | 回調後所在 |
|---|---|---|
| 001 之「5 秒 ＋ PU0942 Timeout (sec)」 | Final Step ＋ ER 3 | **ER 3**（`The pop-up closes by itself 5 seconds after it appeared, matching the Time-out defined by PU0942 Timeout (sec)…`）|
| 003 之「5-second Time-out ＋ PU0580」 | Final Step ＋ ER 3 | **ER 3** |
| 004 之「3-second Time-out ＋ PU0949」 | Final Step ＋ ER 3 | **ER 3** |

工具實測「ER 3 含時限字樣之條數 = 3」，與回調前相同（§八-1）。

---

## 三、判準改內容判準（R-POP18）

### 3.1 實作

`scripts/lint_docs036.py`：

1. 新增 `register_tables()` —— **內容判準**：一張表格首欄有 **≥ 2 列**
   合 `^(A|DR|R)-[A-Z]+\d+$`（去 `[]`／粗體後）即登記表
2. **補一條門檻**：只有 1 列但佔該表首欄非空格之 **≥ 50%** 者亦算登記表。
   **理由**：power 之 `A-PW` 主表被空行切成多段，其中有單列續段；
   只用 ≥ 2 會把續段整段丟掉 —— 那是用另一種方式重蹈 A-POP10。
   兩條門檻都擋得住 `privacy` 之欄位值表（首欄 6 格僅 `S10` 一格合形態，
   1/6 = 17%）
3. `series_in()` 收兩種來源：登記表首欄（記表序）＋ 標題式
   `## A-XXn`／`## [A-XXn]`（表序記為 `HEAD_TABLE = -1`）
4. **標題式只作存在性佐證，不參與重複判定**
5. 同檔多張登記表之編號**合併為一序列**後才判跳號
6. 輸出之「略過」拆為兩欄：「首格不合系列形態」與「合系列形態但不在登記表」

### 3.2 第 4 點之必要性（兩個方向都會出錯，故用途分開）

| 若 | 則 | 實例 |
|---|---|---|
| 標題與表格一併算重複 | popup 之「主表一列 ＋ `## A-POPn` 明細節一節」→ **每一號都變成跨表同號**（11 筆 note）| 開發中實際觸發 |
| 有表格就不看標題 | sxm 之回顧表只列 `{15,16,17,20}`，完整登記在標題 → **A-SX18／19 又被判跳號** | 開發中實際觸發，**即 A-POP11 兩筆假陽性之重現** |

故：兩式都收，標題式不參與重複判定。此判準以三支測試釘住
（`test_表格式存在時標題式不重複計`、`test_標題式登記受檢_方括號式亦然`、
`test_標題式之跳號仍抓得到`）。

### 3.3 迴歸四向（G-K／G-N）

**(a) 放寬向 —— 仍成立**

```
power_moding  note（不判紅，R-POP16 乙）：4 項
  [DR-PMH_id] DR-PMH1／DR-PMH2／DR-PMH3／DR-PMH5：同號見於 2 個表格
  docs_structure：PASS   --gate exit=0
```

**(b) 注入向 —— 仍成立**（scratch 副本，於登記表內複製 `| A-POP9 | … |` 一列）

```
注入前 --gate exit=0
注入後   [A-POP_id] A-POP9：編號重複（同一表格內）      --gate exit=1
```

**(c) 假前綴向 —— 實證，未推定**

```
privacy  前綴（自 privacy 之 DR／ANOMALIES 登記表／標題式抽取）：['A-PV']
         首格不合系列形態而略過：86　合系列形態但不在登記表而略過：1
```

`S` **不在前綴集**；被排除之 1 筆即 `ANOMALIES.md:194` 之
`| S10 | \`NA\`（Functional Safety）|`，且**計入「不在登記表」之數**而非
靜默吞掉。該表逐字（首欄 6 格：`cell`／`B10 / B11`／`D10 / D11`／`F10`／
`G10`／`S10`）已逐字釘入 `tests/test_lint_docs036.py` 之
`PRIVACY_FIELD_TABLE`（G-N）。

**(d) 回收向（本包新增）—— 74 筆全數回收**

| feature | 改前「略過」 | 改後「略過」 | 改前前綴集 | 改後前綴集 |
|---|---|---|---|---|
| sxm | **4** | **0** | （無）| `['A-SX']` |
| audio_mgmt | **7** | **0** | （無）| `['A-AM', 'DR-AM']` |
| projection | **63** | **0** | （無）| `['A-PJ', 'R-P']` |
| privacy | 1 | 1（`S10`，應排除）| （無）| `['A-PV']` |
| power | 0 | 0 | `['A-PW','DR-PW']`（僅第 1 段）| `['A-PM','A-PW','DR-PW']`（全段合併）|
| power_moding | 0 | 0 | `['DR-PMH']` | `['A-PMH','DR-PMH']` |
| amfm | 0 | 0 | （無）| `['A-AM']` |
| home | 0 | 0 | （無）| `['A-H']` |
| user_profiles | 0 | 0 | （無）| `['A-UP']` |
| media | 0 | 0 | （無）| （無）—— **仍為真盲區**，明印 `no series detected` |
| popup | 0 | 0 | `['A-POP','DR-POP']` | `['A-POP','DR-POP']` |

**改前有 4 個 feature 抽不到任何前綴（G-D 盲區），改後只剩 `media` 一個。**
另 `driver_distraction`／`vehicle_setting`／`sw_update`／`bed_lowering`／
`display`／`vehicle_category` 六者本輪首次納入掃描（見 §四-3）。

### 3.4 單元測試

`tests/test_lint_docs036.py`：**23 → 29 支全綠**。

- **改寫 2 支**：原 `test_前綴抽取限於首個表格_假前綴不入集` 與
  `test_盲區於_main_明示_no_series_detected` 之 fixture 編碼的是
  R-POP16 乙之**已被取代**行為（其 `ANOM_BLIND` 的第二張表其實是登記表，
  在新判準下**應該**被抽到）。改為真盲區 fixture，並把「假前綴不入集」
  獨立為 `test_假前綴_S_之欄位值表不算登記表`
- **新增 6 支**：內容判準（不以位置）、假前綴排除、標題式受檢（方括號式）、
  標題式跳號仍抓得到、多張登記表合併為一序列、表格式存在時標題式不重複計

---

## 四、R-POP18 回收後新浮現之缺陷（§三-(d)：只造清單、不代改）

### 4.1 已逐筆複驗並寫入 BACKLOG（3 筆，2 個 feature）

| feature | 號 | 複驗（逐字） | 落點 |
|---|---|---|---|
| audio_mgmt | `A-AM12` 缺登記節 | 實存 `## [A-AM01]`～`## [A-AM11]`、`## [A-AM13]`～`## [A-AM20]`；`A-AM12` 全檔**僅一處散文引用**（`ANOMALIES.md:311`「展開池 v2（891 ID，多值格逐一展開，A-AM12）」）| `features/audio_mgmt/BACKLOG.md` **B2**（append）|
| projection | `A-PJ46` 跳號 | 全檔 `A-PJ` 實存 `A-PJ01`～`A-PJ79`（補零式折算為整數後逐號比對），**僅缺 46** | `features/projection/BACKLOG.md` **B1**（新建）|
| projection | `A-PJ06` 同表重複 | `:2152` `\| A-PJ06 \| **CLOSED** \| 0 \| R-P33 — Layer 2 定案… \|`；`:2197` `\| A-PJ06 \| ↑ 見上 \| \| Projection Audio 一結案即可關 \|`。**2150–2197 間無空行**（實測），故為同一張 markdown 表格 —— 依 R-POP16 乙判紅而非降 note | 同上 **B2** |

三筆皆**未代改該 feature 之 ANOMALIES.md／DATA_REQUESTS.md 本體**。
`features/projection/BACKLOG.md` 為新建，體例沿 03 包所建兩本。

### 4.2 **未寫入者（vehicle_setting，30+ 筆）—— 停下回報**

`--feature vehicle_setting` 本輪浮現 31 項（`A-VF32` 跳號、`A-VS` 系列
28 筆跳號、`ANOMALIES.md:204` 表格列缺結尾 `|`）。**未寫入其 BACKLOG**，
兩個理由：

1. **未能複驗為真**：該 feature 之 `A-VS` 為補零式（`A-VS01`～`A-VS04`），
   而其登記表只收部分號，其餘為散文引用 —— 「跳號」清單在複驗前
   不能斷定為真。逐筆複驗需深入他 feature 之台帳，**逾越本包範圍**
2. **該 feature 正由另一 session 施工中**（工作樹有其未提交之
   `RULINGS.md`、`data/vf230_*.tsv`、`scripts/vf230_wvf91_*.py`
   與三份 handoff／upstream）。寫入其 `BACKLOG.md` 會與其在製品衝突

依 §禁區「不代改他 feature 之台帳」與 R-POP16 甲之單一擁有者原則，
**只在此回報，不落任何檔**。原始輸出見 §四-3。

### 4.3 全 feature 掃描結果（唯讀，18 個 feature）

| feature | 判 | 內容 |
|---|---|---|
| power | PASS | — |
| power_moding | PASS | 4 note（DR-PMH1／2／3／5 跨表）|
| privacy | PASS | 略過 1（`S10`，應排除）|
| sxm | **PASS** | **A-SX18／19 之假陽性已消失**（R-POP19 之機械佐證）|
| amfm | PASS | 本輪首次抽到 `A-AM` |
| user_profiles | PASS | 本輪首次抽到 `A-UP` |
| popup | PASS | — |
| driver_distraction | PASS | 首次納掃 |
| sw_update | PASS | 首次納掃 |
| bed_lowering | PASS | 首次納掃 |
| display | PASS | 首次納掃 |
| vehicle_category | PASS | 首次納掃 |
| projection | 2 項 | `A-PJ06` 同表重複、`A-PJ46` 跳號 → **已入其 BACKLOG** |
| audio_mgmt | 2 項 | `DR-AM7`（03 包已入）、`A-AM12` → **已入其 BACKLOG** |
| time_management | 1 項 | `A-TM2`（03 包已入）|
| home | 1 項 | `DATA_REQUESTS.md` 不存在（既存，非本輪浮現）|
| media | 1 項 | `DATA_REQUESTS.md` 不存在；且 `no series detected`（**唯一剩餘之 G-D 盲區**）|
| vehicle_setting | 31 項 | **未複驗、未寫入**，見 §四-2 |

`gate_all.py` 之 `lint_docs036` 用預設 `--feature power` → **PASS**，
故本次判準改動**不使 gate 轉紅**。

---

## 五、A-POP6 甲類訂正與台帳收斂（R-POP19）

### 5.1 A-POP6 §甲（加註保留，不刪原數；R-TM13 形制）

標題改為 `甲、真陽性（~~4 個 feature，5 筆~~ → **訂正為 2 個 feature／2 筆**）`，
其下新增三數並陳表（原標題 4/5 ／ 原表列 3/4 ／ 訂正後 **2/2**）。
表內 sxm 一列**劃線保留**，並改寫其佐證欄為撤回理由
（「首格所見編號集為 `{15,16,17,20}`」正是缺陷本身）。

### 5.2 主表與明細節之狀態同步

| 號 | 主表狀態 | 明細節標題 |
|---|---|---|
| A-POP10 | **RESOLVED（R-POP18）** | 同步 |
| A-POP11 | **RESOLVED（R-POP19）** | 同步 |
| A-POP6 | 處分欄補列 R-POP18／R-POP19 | — |

A-POP6 處分欄之補列**是被工具逼出來的**：改完 A-POP10／11 後
`ledger_xref --feature popup` 立刻報

```
[pairing] features/popup/RULINGS.md:237：R-POP19 之標題掛 A-POP6，
          但台帳 A-POP6 之處分欄載為 R-POP16 —— 兩處不相認
```

R-POP19 確實訂正了 A-POP6 甲類，故補列為實情。補後 `ledger_xref` **PASS**。

---

## 六、上繳包 03 §十三 之複驗（12 項逐項，非只查第 9 項）

§十 第 5 項令「若發現第二項失準，回報，勿逕改上繳包 03 之歷史文」。
**逐項複驗結果：只有第 9 項失準，無第二項。上繳包 03 之歷史文未改。**

| # | 03 §十三 所稱 | 複驗方法 | 結果 |
|---|---|---|---|
| 1 | A-POP10 待裁 | 台帳 | 準（本包由 R-POP18 結案）|
| 2 | A-POP11 待裁 | 台帳 | 準（本包由 R-POP19 結案）|
| 3 | `ledger_xref` 合併／接入待裁 | 下放包 04 §五 | 準，仍開 |
| 4 | `canon_refs` +3 | 隔離實測（移三檔 → 464）| 準 |
| 5 | Q 欄未寫入 | 回讀 `Q10:Q14` | 準 —— `[None, None, None, None, None]`；`P10:P14 = ['P1']×5` |
| 6 | pilot review 未做 | 下放包 04 §九-9 | 準（分析層已於 2026-08-28 覆核，除 F7 外無發現）|
| 7 | `sources/` 版控條文未取號 | `INDEX.md:43／54／65` | 準，仍「未」|
| 8 | R-POP5 待追認 | `RULINGS.md:36` 標題仍為「分析層先裁，待 Pei 追認」| 準 |
| **9** | **DECISIONS.md 未簽、Sign-off 未填** | 逐行讀 | **失準** —— 見下 |
| 10 | `forms/` 落點政策待裁 | `ls forms/` | 準 —— 除 `…_ext.xlsx` 外另有 HMI Settings List、LID、PROXI、兩支 DBC、Pop Up List、Priority Matrix、Market Config、Default Settings 等共 12 項 |
| 11 | `-002-05` design_method 待裁 | 下放包 04 §九-2 | 準，仍開（分析層意見：維持狀態轉換）|
| 12 | `lint_paths` 紅（driver_distraction）| 實跑 | 準 —— `features/driver_distraction/workbook/driver_distraction_00.xlsx` 落點違規，仍 1 筆 |

### 第 9 項之實測（逐字）

```
features/popup/DECISIONS.md:48  ## Sign-off
                           :50  - Reviewed by: PeiPYHsu  Date: 2026-08-27
                           :51  - Overridden items: none — 8 `[PROPOSED]` left untouched, binding as proposed
                           :40  - Test Set table (Part N): [PEI 2026-08-27] …
                           :41  - profile [OVERRIDE] clauses: [PEI 2026-08-27] …
                           :57  - **本簽署由執行層轉錄，`Reviewed by` 與 `Date` 之值由 Pei 指定**
```

**成因**：上繳包 03 §十三 為人工清單，其第 9 項轉抄自下放包 02 §4
之「仍未結」表，未 live 複驗 —— **正是 R-POP17 第 1 項所禁之手寫重述**。
依下放包 04 §六「不新開 anomaly 號」（A-POP9 已管轄此型），
**未新開號**；本包 §十一 之待裁清單改為**逐項複驗後重寫**（上表即其產物）。

---

## 七、寫回與 gate

- `sandbox/pilot01/` 作業，`surgical_save` 寫回
- `patched: {'Test Case Specification 測試用例規範': 75}`、
  `differing: ['xl/worksheets/sheet6.xml']`（僅一支 sheet xml 改動）

x14 DV `zipfile` 直讀複驗（母本 vs 產出）：

```
母本 xl/worksheets/sheet6.xml: 1 個  f=['下拉選單!$A$1:$A$9']  sqref=['R10:R1411']
產出 xl/worksheets/sheet6.xml: 1 個  f=['下拉選單!$A$1:$A$9']  sqref=['R10:R1411']
```

`lint036.py --profile popup`（21 項）：

```
行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
     N=0 P=0 Q=0 R=0 T=0 U=0 V=0
```

報告落 `features/popup/reports/popup_20260817_ext__popup_dc0963d7_20260828.md`。

`ledger_xref --feature popup`：**PASS**（掃 8 檔、本 feature 引用 201 處、
他 feature 引用 37 處不對照、補零不一 0 處）。

---

## 八、預期數字對照（§八，相符者亦列）

### 8.1 語料層（`gen_pilot.py` 之 `audit()` 自 `generated/pilot_01.json` 實測）

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| Final Step 詞數 ≤ 18 之條數 | 5/5 | **5** | 相符 |
| Final Step 含 `check that` | 5 | **5** | 相符 |
| ER 3 含時限字樣之條數 | 3（001／003／004）| **3** | 相符 |
| TC 總數 | 5 | **5** | 相符 |
| PENDING 佔位 | 0 | **0** | 相符 |
| `input_test_data` = `NA` | 5 | **5** | 相符 |
| （續 03 包）`newR1L`／`PROJ` 殘留（語料）| 0 | **0／0** | 相符 |
| （續 03 包）反引號（五交付欄逐 item）| 0 | **0** | 相符 |
| （續 03 包）`pre_conditions` 含 `ignition in RUN` | 0 | **0** | 相符 |
| （續 03 包）`spec_reference` 兩行者 | 1 | **1** | 相符 |
| （續 03 包）`pu_citation` 為 null 者 | 1 | **1** | 相符 |

### 8.2 lint 判準層

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| 略過數 sxm／audio_mgmt／projection | 0／0／0 | **0／0／0** | 相符 |
| `privacy` 前綴集含 `S` | 否 | **否**（`['A-PV']`）| 相符 |

### 8.3 工作簿層

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| x14 DV | 1，存活 | **1，存活** | 相符 |

### 8.4 條文指紋（`rulings_hash.py`）

| 項 | 預期 | 實測 | 判 |
|---|---|---|---|
| 新增列 | 3（R-POP18／19／20）| **3** | 相符 |
| 變動列 | 2（R-POP13／R-POP15）| **2** | 相符 |
| 其餘既有列 sha 變動 | 0 | **0** | 相符 |
| 錨點總數 | — | 554 → **557** | — |

`diff`（`cut -f1,3,5 | sort`）之**全部**輸出：

```
< R-POP13  9b835066  features/popup/RULINGS.md
> R-POP13  bcd97ba8  features/popup/RULINGS.md
< R-POP15  298237c3  features/popup/RULINGS.md
> R-POP15  2c712b56  features/popup/RULINGS.md
> R-POP18  18ddf460  features/popup/RULINGS.md
> R-POP19  5d9764bc  features/popup/RULINGS.md
> R-POP20  7ac862b3  features/popup/RULINGS.md
```

只有 R-POP13／R-POP15 兩個 `<`／`>` 配對，**無第三個** ——
§十 第 4 項升級條件未命中。

### 8.5 gate_all（逐支歸因）

| 閘 | exit | 03 包後 | 04 包後 | 歸因 |
|---|---|---|---|---|
| `lint_docs036 --gate` | **0** | PASS | PASS | 判準改動**不使 gate 轉紅**（預設 `--feature power` 為 PASS）|
| `canon_refs --waiver --gate` | **1** | 467 | **470** | **本包 +2**，另 +1 非本包 —— 見下 |
| `rulings_hash --check` | **0** | PASS | PASS | — |
| `gates_tsv --check` | **1** | PASS | **FAIL** | **非本包** —— 見下 |
| `lint_paths --gate` | **1** | 1 | **1** | **非本包** —— driver_distraction 在製品，未變 |

**`gates_tsv` 由綠轉紅 —— 非本包**。重產後與現行檔 `diff` 之**全部**輸出為一列：

```
> features/driver_distraction/scripts/selfcheck_pilot_group3.py  feature
  **未拆之閘集合** —— 該腳本內各支檢查之 id 尚未逐支盤點  …  未入簿之前為未登錄
```

即他 feature 之新腳本未登錄於 `docs/runtime/GATES.tsv`。
**未代其重產 GATES.tsv**（登錄屬該 feature 之事，且重產會把他 session 之
在製品寫進共用簿）。本包新增之 `scripts/ledger_xref.py` **不在 diff 內**
—— `gates_tsv` 之偵測未把它認作閘，與 03 包當時 `gates_tsv` 仍 PASS 一致。

**`canon_refs` 之 +3 拆解（三次隔離量測）**：

| 來源 | 量 | 實測 |
|---|---|---|
| `features/projection/BACKLOG.md:3` 之 `R-G29` | **+1** | 暫移該檔 → 468，放回 → 469 |
| 本上繳包 §十 引用表之 `R-G29` | **+1** | 暫移本檔 → 469，放回 → 470 |
| 他 session 之 commit `97adbd4 feat(sw_update): …` | +1（**非本包**）| 本包開工基線 467，未動任何 sw_update 檔 |

**另有 +1 於作業中被自己修掉**：本上繳包 §十 原寫
`IN §4.5／§5.2B／§5.5／§8.5／§11／§12`，第二個以後之節號成為**裸引用**，
`canon_refs` 判為 FO／IN 兩 canon 共用之歧義（471）。
改為逐一冠 `IN` 後降回 470。**此為本包自產自修，一併記錄** ——
縮寫式列舉節號會製造歧義引用，是可複製的寫作陷阱。

**不調和**：未塞 `CANON_REFS_WAIVER.tsv`、未刪 `R-G29` 引用、
未代改他 feature 之 `GATES.tsv`。

### 8.6 單元測試

`python3 -m pytest tests/ -q` → **1261 passed, 8 failed, 15 skipped**
（03 包為 1255 passed／8 failed；+6 即本包新增之 lint 測試）。

**八項失敗與 03 包完全相同，逐項仍在本包改動面外**：
`test_single_write_path`（2 支，指向 time_management／user_profiles／
vehicle_category 之腳本）、`test_intake_scaffold`（6 支，`new_feature.py`
於 tmp root 找不到 `docs/fw036/templates/DECISIONS.md`）。

本包相關：`tests/test_lint_docs036.py` **29 支全綠**（23 → 29）、
`tests/test_ledger_xref.py` **9 支全綠**（未改）。

---

## 九、三分法

| 類 | 內容 |
|---|---|
| **照裁定執行** | F7 逐條回調、R-POP18 內容判準、A-POP6 甲類訂正、A-POP10／11 狀態同步、兩本 BACKLOG 之新條目、tsv 重產、§六 逐項複驗 |
| **實測後回報而不自為** | (a) R-POP20 之詞數算法與其自身數字不符（§二-1）；(b) vehicle_setting 31 項未複驗未寫入（§四-2）；(c) 03 §十三 第 9 項失準已由 §六 確認為**唯一**一項，歷史文未改 |
| **獨立判斷（已揭露）** | (a) 001 之回調保留「the elapsed time」，未逐字照抄 R-POP20 示例（§二-2）；(b) 內容判準加第二條門檻「單列但佔 ≥ 50%」以接住 power 之切段續段（§三-1）；(c) 標題式登記只作存在性佐證、不參與重複判定（§三-2）；(d) `projection/BACKLOG.md` 沿 display 體例含 `R-G29`，代價 `canon_refs` +1（§八-5）|

### 掃描條件揭露（R-G8）

| 掃 | 條件 |
|---|---|
| Final Step 詞數 | 取 `test_procedure` 末行，去 `N. ` 序號後 `str.split()`；`(sec)` 計為一詞（§二-1）|
| ER 時限字樣 | `expected_result` 全文含 `5-second`／`5 seconds`／`3-second`／`3 seconds` 任一 |
| lint 跨 feature | `--feature <f>` 逐一實跑，判準改動前後各一輪，共 **18** feature |
| 他 feature 台帳複驗 | 表格首格 ＋ `## A-XXn`／`## [A-XXn]` 兩式併計，補零式折算為整數 |
| 表格邊界 | 以 `awk` 掃該區間之空行／非表格行，確認 `A-PJ06` 兩列間無空行 |
| tsv 前後比對 | `cut -f1,3,5 \| sort` 後 `diff` |
| x14 DV | `zipfile` 直讀 `xl/worksheets/sheet*.xml`，正則取 `<xm:f>`／`<xm:sqref>` |
| canon_refs 歸因 | 暫移待測檔 → 重跑 → 放回，三次量測 |

---

## 十、R-G13 引用表（sha8 取自重產後之 `docs/fw036/RULINGS.sha.tsv`）

| 條 | sha8 | 標題 | 備註 |
|---|---|---|---|
| R-POP13 | `bcd97ba8` | TC ID 前綴定值 | **本輪修訂**（舊 `9b835066`）|
| R-POP15 | `2c712b56` | Pilot 修正六件之判準 | **本輪修訂**（舊 `298237c3`，F1 加註 ≤ 18 words）|
| R-POP18 | `18ddf460` | 主表辨識改內容判準 | 新立 |
| R-POP19 | `5d9764bc` | A-POP6 甲類之 sxm 兩筆撤回 | 新立 |
| R-POP20 | `7ac862b3` | F1 修正過長之回調 | 新立 |
| R-POP12 | `e323360d` | -002-02 不拆，軸不存在 | 未變 |
| R-POP14 | `e025ab99` | -002-05 採規格原句生成 | 未變 |
| R-POP16 | `36e1ed0a` | lint 新規命中之三分法處置 | 未變（其乙之一項由 R-POP18 取代）|
| R-POP17 | `7b7868ec` | 上繳回報與 repo 台帳不符之登記 | 未變 |

另引 R-G2、R-G3、R-G5、R-G8、R-G13、R-G25、R-G29、R-TM13、
IN §4.5、IN §5.2B、IN §5.5、IN §8.5、IN §11、IN §12、G-B、G-D、G-K、G-N。
（各節號逐一冠 `IN` —— 以「IN §4.5／§5.2B／…」之縮寫寫法列舉時，第二個以後之節號成為裸引用，`canon_refs` 判為 FO／IN 兩 canon 共用之歧義。）

---

## 十一、台帳現況（**自 repo live 產**，R-POP17-1）

`python3 scripts/ledger_xref.py --feature popup --live` 之直接輸出：

| 號 | 狀態 | 處分條 |
|---|---|---|
| A-POP1 | RESOLVED（R-POP9 追認）| R-POP9 |
| A-POP2 | RESOLVED（甲半 R-POP6、乙半 R-POP7）| R-POP6／R-POP7 |
| A-POP3 | RESOLVED（R-POP8）| R-POP8 |
| A-POP4 | RESOLVED（R-POP10）| R-POP10 |
| A-POP5 | RESOLVED（寫入路徑改 xlsx_surgical）| — |
| A-POP6 | RESOLVED（R-POP16；乙之「首個表格」已由 R-POP18 取代，甲類筆數已由 R-POP19 訂正）| R-POP16／R-POP18／R-POP19 |
| A-POP7 | RESOLVED（R-POP12）| R-POP12 |
| A-POP8 | RESOLVED（R-POP14）| R-POP14 |
| A-POP9 | RESOLVED（R-POP17；(4) 另 R-POP13）| R-POP13／R-POP17 |
| A-POP10 | **RESOLVED（R-POP18）** | R-POP18 |
| A-POP11 | **RESOLVED（R-POP19）** | R-POP19 |
| DR-POP1 | RESOLVED（2026-08-27）| R-POP6 |
| DR-POP2 | 已登記，未送出 | — |
| DR-POP3 | 已登記，未送出 | — |
| DR-POP4 | 已登記，未送出 | — |

**A-POP 全 11 件、DR-POP 全 4 件皆已處分或已登記；本包未新開任何號。**

---

## 十二、五條 TC 全文（回調後）

回調只動 `test_procedure` 之末步驟；其餘欄與上繳包 03 §十二 逐字相同。
以下只列**變動之末步驟**與**未變之 ER**，以免同文再抄一遍造成兩份語料。

### NR1L-Popup-001 — SWE1-POP-002-01

- Procedure 1／2：不變
- **Procedure 3（新）**：`Read the pop-up display status and the elapsed time, and check that the pop-up has closed`
- ER 1／2／3：不變（ER 3 仍載 `5 seconds … PU0942 Timeout (sec)`）

### NR1L-Popup-002 — SWE1-POP-002-02

- Procedure 1／2：不變（`press the Track list button "Trks"` ／ `Press "Trks" a second time…`）
- **Procedure 3（新）**：`Read the pop-up display status immediately after the second press and check that the pop-up is closed`
- ER：不變；`spec_reference` 仍為 `_5.5` ＋ `_5.6` 兩行

### NR1L-Popup-003 — SWE1-POP-002-03

- Procedure 1／2：不變
- **Procedure 3（新）**：`Read the pop-up display status immediately after the tap and check that the pop-up is closed`
- ER 3：不變（仍載 `before the 5-second Time-out defined by PU0580 Timeout (sec) elapses`）

### NR1L-Popup-004 — SWE1-POP-002-04

- Procedure 1／2：不變
- **Procedure 3（新）**：`Read the pop-up display status immediately after the press and check that the pop-up is closed`
- ER 3：不變（仍載 `before the 3-second Time-out defined by PU0949 Timeout (sec) elapses`）

### NR1L-Popup-005 — SWE1-POP-002-05

- **全條不變**（Final Step 17 words，本即合格）；`pu_citation` 仍為 `null`

五條之 `test_group`／`test_set`／`tc_ref_id`／`priority`／`design_method`／
`functional_safety`／`author` 均為
`Popup` ／ `Pop-up Close` ／ `NEW` ／ `P1` ／ `狀態轉換 (State Transition Testing)` ／
`NA` ／ `PeiPYHsu`；`estimated_test_time`（Q 欄）**未寫入**（§六-5）。

---

## 十三、待 Pei（逐項複驗後重寫，非轉抄）

| # | 事項 | 現況（本包實測）|
|---|---|---|
| 1 | R-POP5（Heading 台帳處置 [DEFAULT]）追認 | 仍待 —— `RULINGS.md:36` 標題為「分析層先裁，待 Pei 追認」|
| 2 | `-002-05` 之 `design_method`：狀態轉換 vs 負向測試 | 仍待 —— 分析層意見為維持狀態轉換（下放包 04 §九-2），執行層無異議 |
| 3 | `scripts/ledger_xref.py` 與 vehicle_category 同名檔是否合併；是否接入 `gate_all.py` | 仍待 —— 本包續用其 `--feature popup`，**未接入 gate_all**（照 §禁區）|
| 4 | `canon_refs` 之 `R-G29` 引用（現三本 BACKLOG ＋ 兩份上繳包）| 仍待 —— 分析層意見為維持；本包再 **+2**（projection/BACKLOG ＋ 本上繳包）|
| 5 | Priority／Estimated Test Time 欄之政策 | 仍待 —— Q 欄實測 `[None]×5`，P 欄 `['P1']×5` |
| 6 | `forms/` 落點政策（全域）| 仍待 —— `forms/` 現有 12 項，R-G2 字面只允 `…_ext.xlsx` 一件 |
| 7 | `sources/` 版控條文之 R- 取號 | 仍待（分析層）|
| 8 | `lint_paths` 之紅（driver_distraction 在製品）| 仍待 —— 他 feature |
| 8b | **`gates_tsv` 之紅** —— `features/driver_distraction/scripts/selfcheck_pilot_group3.py` 未登錄 | **新增** —— 他 feature，未代其重產 `GATES.tsv`（§八-5）|
| 9 | **vehicle_setting 之 31 項**（`A-VF32`／`A-VS` 28 筆／`ANOMALIES.md:204` 表格列缺尾管）| **新增** —— 未複驗未寫入，理由見 §四-2 |
| 10 | **`media` 為唯一剩餘之 G-D 盲區** | **新增** —— 其 `ANOMALIES.md` 抽不到登記表或標題式登記，`DATA_REQUESTS.md` 不存在 |
| 11 | pilot review | **已結** —— 分析層 2026-08-28 覆核，除 F7 外無發現；F7 本包已修 |

**已自 03 §十三 移除**：原第 9 項「DECISIONS.md 未簽」（§六 實測已簽）。

---

## 十四、git

**未執行任何 git 操作**（R-G5）。建議之 commit：

```
feat(popup): land handoff 04 - F7 rollback, content-based register criterion, ledger close
```

本包改動之檔：

```
M  features/popup/scripts/gen_pilot.py
M  features/popup/generated/pilot_01.json
M  features/popup/sandbox/pilot01/…_ext.xlsx
M  features/popup/ANOMALIES.md
M  features/popup/docs/INDEX.md
M  scripts/lint_docs036.py
M  tests/test_lint_docs036.py
M  docs/fw036/RULINGS.sha.tsv
M  features/audio_mgmt/BACKLOG.md
?? features/projection/BACKLOG.md
?? features/popup/docs/handoff/04_f7_ledger_close.md
?? features/popup/docs/upstream/04_f7_ledger_close.md
?? features/popup/reports/popup_20260817_ext__popup_dc0963d7_20260828.md
```

**非本包所改而顯示為 M 者**：`features/popup/RULINGS.md`
（R-POP13／R-POP15 之修訂與 R-POP18／19／20，分析層本輪落檔）。

**注意**：工作樹另有他 session 之未提交改動（vehicle_setting、bed_lowering、
docs/runtime 等）。commit 時**務必帶 pathspec，勿 `git add -A`**。
