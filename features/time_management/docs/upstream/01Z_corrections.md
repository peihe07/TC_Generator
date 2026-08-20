# 上繳 01Z — 指令集 T1–T6 之落檔回報

執行層 → 分析層。對應 `docs/handoff/01Z-A2_command_set.md`
（連帶 `01Z_naming_rulings.md`、`01Z-A1_amendment.md`）。
**僅回報差異，不重述前包。** 2026-08-20。

**索引表為 15 條，非指令集預期之 14 條。** 多出者為 A-TM15，
執行層於本包執行中發現，且其中包含執行層自身於 01 包之一項失誤。見 §6。

## 1. T1 — `test_group`

已改，逐字如指令：

```
改前：test_group: "Time Management"           # [PROVISIONAL] 見 R-TM2；framework-internal; workbook write per profile
改後：test_group: "Time and Date"             # R-TM8；framework-internal; workbook write per profile
```

`feature:` 未動，維持 `"Time Management"`（R-TM1）。

### 1.1 `git diff` 不是一行 —— 原因與釐清

指令要求「確認只動這一行」。實際 `git diff` 顯示 **12 insertions /
12 deletions**。**非 T1 造成。**

原因：**01 包對 `feature.yaml` 之更正尚未 commit**（git 全屬 Pei，
執行層自 Phase 0 以來未再 commit），故 `git diff` 之基準為 Phase 0 之
HEAD，涵蓋 01 包之全部更正（workbook 路徑、sheet 名、rev C 五欄、
done_region、fill_test_group_set、spec_pdf、popup_list）。

T1 本身只動 `test_group` 一行 —— 由 Python `assert old in t` ＋
`replace(o, n, 1)` 保證唯一且僅一次。diff 中屬於 T1 者僅：

```diff
-test_group: "Time Management"           # [PROVISIONAL] 見 R-TM2；framework-internal; workbook write per profile
+test_group: "Time and Date"             # R-TM8；framework-internal; workbook write per profile
```

其餘 11 行皆為 01 包已上繳並經 01R 受理之更正。

## 2. T2 — A-TM14 舉證：「確已不存」**成立**

### 2.1 三層舉證

| 層 | 方法 | 結果 |
|---|---|---|
| 目錄 | `ls -d features/home/output` | **ABSENT** |
| 檔名 | `command find`（繞過 shell function） | **0** |
| 檔名 | Python `os.walk` 獨立實作 | **0** |
| 檔名 | **陰性對照**：同掃描找「含 `Home` 之 xlsx」 | **35 筆** |
| **內容** | **150 筆 036/SWQT xlsx 逐一 SHA256 比對 `cfc007f3…`** | **0 / 150** |

`features/home/` 內容與 01Z-A1 §1 所列**完全相符**（無 `output/`、無 `inputs/`）。

**兩項方法學說明**：

1. **陰性對照為必要**。本 shell 之 `find` 是 Claude Code 包裝之 `bfs`
   function，非系統 `find`（`which find` 顯示其為 shell function 定義）。
   單一工具之 0 命中不足為據，故加 `command find` ＋ `os.walk` ＋
   35 筆陽性對照，證明掃描有效而非空掃。此為 R-TM7 精神之延伸。
2. **SHA256 全域比對為決定性**。檔名可能已變，故不依賴檔名：掃描兩個
   根目錄下**全部**檔名含 `036` 或 `SWQT` 之 xlsx（150 筆），逐一計算
   SHA256。**無一以 `cfc007f3` 開頭。** 縱使該檔被改名，其內容亦不存在。

**未複製任何檔案進 `inputs/`。**

### 2.2 執行層額外發現（分析層未知，登記不裁）

分析層之建議處置指定要查交付路徑 `/Users/peihe/Work/02_Project_R1LR/
10_Reviewing/…`。已查，**該處有 Home 工作簿，但不是 v2**：

| | 交付路徑 | `archive/forms_superseded/` |
|---|---|---|
| 檔名 | `…_SWQT_Home_20260809.xlsx` | `…_SWQT_Home_20260809.xlsx`（**同名**） |
| SHA256 | `469b2f6d346d0b1ddd8c86b597760c60a643b3a6beab2036a358b1e288f6c3df` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` |
| bytes | 120,639 | 119,885 |
| mtime | 2026-08-19 12:01 | 2026-08-09 22:22 |
| `cmp` | **differ: char 2534, line 3** | |

**兩份同名、不同內容、差 754 bytes、mtime 差 10 天。**

**這使 A-TM14 之問題比 01Z-A1 所述更深一層**：不只基準（v2）不可覆驗，
**FORMS.md provenance warning 之受測物身分本身即有歧義** —— 該 warning
描述「archive 內之 Home 複本」有四項污染，但磁碟上有兩份同名檔案，
warning 所測者為何份，現已無從得知。

**執行層未認定交付路徑該份可用**：它既非 v2（SHA 不符），亦不能因
「不是 R-TM10-A1 明文禁止的那一份」就推定乾淨。**解除須 Pei 裁**（R-TM10-A1）。
未複製、未援引、未採用。

## 3. T3 — archive 版 Home 之 `D5`

### 3.1 `repr()` 原樣

```python
'Test Case Specification&Result' row5 col3: '範圍 Scope：'
'Test Case Specification&Result' row5 col4: 'FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告'
'Test Case Specification&Result' row5 col9: '日期 Date：2026'
'Test Case Specification&Result' row5 col33: 'FM-WI-FSM-036-A01'
```

`C5` 標籤 `'範圍 Scope：'`、`D5` 值如上，**無前後空白、無換行**。
與 FORMS.md 所載之 A-H26 未修正值相符（`…AppDrawer-Projection-SWE1HMI-V0.1`）。

**注意該檔之分頁名為 `Test Case Specification&Result`（rev A/B 版面），
與本 feature 母本之 `Test Case Specification 測試用例規範`（rev C）不同。**
其 `Test Case Framework` 分頁存在，亦為 rev A/B 特徵。

### 3.2 切分點提議 —— 並附一個**獨立第二樣本**

提議之切分：

```
FM-WI-FSM-037-A03-N1L-SWE1-  |  AppDrawer-Projection-SWE1HMI-V0.1  |   STLA 報告
└──────── 前綴段 ────────┘     └──── feature 識別段 ────┘     └─ 後綴 ─┘
```

**R-TM9-A1 步驟 3 擱置之問題為「前綴段是否亦受 A-H26 缺陷影響」。
執行層於 T2 之搜尋中取得可回答該問題之獨立證據。**

交付路徑 `…/Core HMI/HomeHMI/` 同一目錄下另有：

```
FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx
```

**該檔名之結構與 D5 值完全同構**：

| | 前綴段 | feature 識別段 | 後綴 |
|---|---|---|---|
| archive D5（缺陷件） | `FM-WI-FSM-037-A03-N1L-SWE1-` | `AppDrawer-Projection-SWE1HMI-V0.1` | ` STLA 報告` |
| Home 037 檔名（獨立樣本） | `FM-WI-FSM-037-A03-N1L-SWE1-` | `Home-HMI-V0.1` | ` STLA 報告` |

**兩者前綴段逐字相同。** 且後者之識別段 `Home-HMI-V0.1` 正是 R-TM9 所
指之「Home v2 正確值形態」。

**由此可作之判讀（提請分析層覆核，執行層不自行認定）**：

1. A-H26 之缺陷**侷限於 feature 識別段**（該寫 `Home` 而寫成
   `AppDrawer-Projection`），**前綴段未受影響**
2. 缺陷可能不只一處：archive D5 之識別段為 `…-SWE1HMI-V0.1`，
   而正確形態為 `…-HMI-V0.1` —— **`SWE1HMI` vs `HMI` 亦不同**。
   即該值除 feature 名錯置外，識別段之尾段形態亦與正確樣本不一致

**執行層未組本 feature 之 D5 值，未填入任何工作簿。A-TM11 維持 PENDING。**
上列第 2 點尤須分析層裁定 —— 若逕以 archive 值之形態套用，會複製
`SWE1HMI` 這個可能同屬缺陷之寫法。

## 4. T4 — 錨鏈六項數字

**六項全數相符，無差異可報。** 證據檔 `data/anchor_probe.txt` 已保留。

| # | 量 | 沙箱值 | **原始 binary** | 差異 |
|---|---|---|---|---|
| 1 | SYS2 第 5 欄非空 / 總列 | 227 / 227 | **227 / 227** | 無 |
| 2 | 78 筆缺來源物件 id | 0 | **0**（`[]`） | 無 |
| 3 | docx 章節標題數 | 88 | **88** | 無 |
| 4 | 物件 id → 章節對映 | 358 | **358** | 無 |
| 5 | 直接可達 / 未直接可達 | 71 / 7 | **71 / 5 + 2** | 無 |
| 6 | 可達之相異章節 | 21 | **21** | 無 |

SYS2 第 5 欄表頭實測：`'SYS2 來源需求項目ID  Source Requirement items'`
（`ID` 與 `Source` 之間為兩個空格）。

### 4.1 交叉驗證 —— 兩種獨立解析法得到相同結果

執行層於 **01R 上繳**時已用**不同判準**做過同一組量測：以 docx 之
`w:pStyle` ∈ {`1`…`6`} 取真標題（並排除 style `10`…`50` 之目次條目）。
本包則照指令集之腳本，以 `"\t" in t` 排除目次、`^(\d{6,8})\s*:` 取物件行。

**兩法之六項數字完全一致。** 兩者對「什麼是標題」的判準不同
（樣式 vs 字面），卻收斂到同一結果 —— 此為比單次量測更強之證據。

### 4.2 split cells 逐筆（R-TM4）

**5 筆全數可達，且每筆之多物件皆落在同一章節（無章節歧義）。**

| SYS-RA | 物件 id | 章節 |
|---|---|---|
| `-139` | `4814088` `4814089` | `1.5.2.4` |
| `-145` | `4814096` `4814097` `4814099` | `1.5.2.5` |
| `-147` | `4814100` `4814101` `4814102` | `1.5.2.5` |
| `-148` | `4814103` `4814104` `4814105` | `1.5.2.5` |
| `-154` | `4814113` `4814114` `4814115` `4814116` | `1.5.2.6` |

**同章節性之意義**：`spec_reference` 取值不需在多個候選章節間裁決。

### 4.3 UNRESOLVED 逐筆 —— A-TM13 獨立確認

```
SYS-RA-221 -> ['6151328']
SYS-RA-224 -> ['6151331']
```

與分析層量測一致。全檔 `615\d{4}` 形態搜尋零命中（已於 01R 上繳複驗）。

## 5. T5 — 登記與索引

| 項 | 狀態 |
|---|---|
| A-TM13 登記 | 已於 01R 上繳時完成 |
| **A-TM14 登記** | 已完成，附 §2 之三層舉證與額外發現 |
| **A-TM15 登記** | **新增，見 §6** |
| R-TM8 / R-TM9 / R-TM9-A1 / R-TM10 / R-TM10-A1 逐字 | 已寫入 `RULINGS.md`，計 **12 條** |
| `DECISIONS.md` 條目 | 已建 §0，見 §6 |
| 索引表 | **15 條**（指令集預期 14 + A-TM15） |
| A-TM11 | **維持 PENDING**（R-TM9-A1） |

R-TM9 與 R-TM10 之原文均已保留為軌跡，並在條首標明其已被 A1 撤銷步驟 /
暫停生效，避免日後誤讀原文。

## 6. A-TM15（新登記）—— `recon.py` 沖掉 `DECISIONS.md` 之裁決引用段

**本條含執行層自身之一項失誤，如實記錄。**

### 6.1 事實

`recon.py:294` 註解自陳「recon.py rewrites DECISIONS.md whole. That is
fine for an unsigned sheet」。實測：僅**已簽核**之本檔受保護（改寫入
`DECISIONS.new.md`）；未簽核者**整份重寫，無備份、無警告**。

### 6.2 與流程要求直接衝突

`00` §4(1)、`01` §1、`01Z-A2` T5(4) 三包均要求於 `DECISIONS.md` 建裁決
引用條目；而 `01` §5 又要求跑 `recon.py`。**後者必然沖掉前者，且在同一
個下放包內互相抵銷。** 失敗形態靜默：recon 僅印 `DECISIONS.md written.`。

### 6.3 執行層之失誤

執行層於 01 包**先寫 §0 裁決引用與 §1 Intake 詳細，後跑 recon，未於
recon 後複查該檔**，故未察覺內容已被沖掉。

01 包上繳 §5 稱「`DECISIONS.md` §2 / §3 已由 recon 結果填實」—— 字面無誤，
但**遺漏「先前寫入之內容已消失」**，整體上構成誤導。**特此更正。**

**失誤性質**：完成動作後未確認結果仍然成立。與 A-TM09 首版（未驗證解析
正確性）、A-TM12 首版（未驗證連結存在性）同族；前二者是未驗證**前提**，
本例是未驗證**後果**。

**發現時機**：本包 T5(4) 欲改 `DECISIONS.md` 時 `str.replace` 目標字串
不存在、替換靜默失敗而暴露。**若非本包恰好要改同一處，此事不會被發現。**

### 6.4 處置

**已執行（Tier 1）**：重建 §0 裁決引用段，節首以區塊引言標示警告與
「每次重跑 recon 後必須手動補回」，並列出 recon `[AUTO]` 預填值與既有
裁決之**四項覆寫關係**：`test_group`（R-TM8 已實裁）、覆蓋分母
（R-TM6 定 126，非 recon 之 leaves 22）、`exemplar source`
（R-TM10-A1 已 SUSPENDED recon 預填之 cross-feature 路徑）、
`spec_reference`（`{outline}` 來源 map 為空，A-TM12）。

**未動（Tier 2）**：`recon.py` 修法。三個方向見 A-TM15 條文。

**損害有限之唯一理由**：條文全文之權威在 `RULINGS.md`，該檔不受 recon
影響，故無條文遺失。`DECISIONS.md` §0 僅為引用索引。**此為運氣，非流程健全。**

## 7. T6(7) — 該驗而未驗者之獨立判斷

### 7.1 盤點所用之全集（明列）

四個全集之聯集：

1. **指令集 T1–T5 之每一項指示**，逐項問「做了沒、結果複查了沒」
2. **本包所觸及之每一個檔案**（`feature.yaml` / `RULINGS.md` /
   `ANOMALIES.md` / `DECISIONS.md` / `DATA_REQUESTS.md` /
   `data/anchor_probe.txt`），逐檔問「寫入後複查了沒」
   —— **此全集為本包新增，直接源於 A-TM15 之教訓**
3. **本包引用之每一個外部事實**，逐項問「實測或轉述」
4. **每一個「不存在 / 0 命中」之結論**，逐項問「有無陰性對照」

### 7.2 依全集 2 —— 寫入後複查（新增之全集）

| 檔案 | 寫入後複查 | 方式 |
|---|---|---|
| `feature.yaml` | ✅ | `git diff` 檢視全文 |
| `RULINGS.md` | ✅ | `grep -c '^## R-TM'` = 12 |
| `ANOMALIES.md` | ✅ | `grep -c '^## A-TM'` = 15 |
| `DECISIONS.md` | ✅ | `grep -n '^## '` 列出全部節名 |
| `DATA_REQUESTS.md` | ✅（01R 包時） | 表格列數 |
| `data/anchor_probe.txt` | ✅ | `cat` 全文 |

**本包無「寫入未複查」者。**

### 7.3 仍未驗、本包範圍外者

| 項 | 為何未驗 | 建議時機 |
|---|---|---|
| `write_back.author_value` / `tc_ref_id_value` | 模板值，BLANK 下無比對對象 | Phase 3（01R §5 已接受此排程） |
| `spec_reference_template` 之可行性 | 依賴 A-TM12 路線裁定 | A-TM12 裁後 |
| 交付路徑 Home 複本之內容是否受污染 | **不得自行檢查** —— R-TM10-A1 SUSPENDED，檢查即已在事實上採用該來源 | Pei 裁解除條件後 |
| FORMS.md 之標註修改（A-TM14 建議處置） | 屬 `forms/`，跨 feature | Tier 2 |
| `recon.py` 之四項修法（A-TM04/05/10/12/15） | 全部 Tier 2 | 併為一次處理 |

第三列須特別說明：執行層**刻意未**開啟交付路徑之 Home 複本檢查其
K / G / F / Z 欄污染狀況。理由是 R-TM10-A1 暫停期間不得援引他 feature
樣式，而「檢查其是否乾淨」在實質上已是把它當作候選樣式來源評估。
**僅記錄其存在與 SHA256，不評估其內容。**

### 7.4 依全集 4 —— 「不存在」之陰性對照

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| Home v2 不在磁碟 | 同掃描找到 35 筆含 Home 之 xlsx | ✅ |
| SHA `cfc007f3…` 不存在 | 同批 150 筆皆成功算出 SHA | ✅ |
| `615xxxx` 零命中 | 同檔 `481xxxx` 命中 358 | ✅（01R 包） |
| PU 編號零命中 | — | ⚠️ **見下** |

**`popup_list: null` 之 0 命中，其陰性對照為弱。** 01 包所做者為
「PU-number 與 popup 字樣皆 0」，但未證明該掃描方法對一份**確實含**
PU 編號之文件會命中。本 feature 無此對照物可用（他 feature 之 spec 不在
本包範圍）。

**執行層判斷：此為可接受之殘餘風險，但應如實標示而非略過。** 理由：
CFTS docx 之解壓全文掃描已在同一份文件上成功命中 358 個物件 id 與 88 個
標題，證明**文字提取本身有效**；未被證明的僅是「PU 編號若存在會被該
正則捕獲」。若日後取得含 PU 之 CFTS 樣本，應補做一次陽性對照。

## 8. 本包未動之事項

未動 git（未 commit、未 tag）。未改任何腳本。未複製任何檔案進 `inputs/`。
未填 `D5`、未組 Scope 值。未援引任何他 feature 樣式。未以 openpyxl 存回
任何工作簿（本包對 archive 複本與母本複本皆 `read_only=True`，無 save）。
未跑 `recon.py`。未產出 `leaf_to_section.tsv`。未進入 Phase 3。
