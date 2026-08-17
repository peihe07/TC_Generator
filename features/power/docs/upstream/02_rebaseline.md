# 02 — Power Management 素材重新定基（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 02
結果：**G0 通過，§D 十三項中十項相符、三項不符；§E 重算不符 → 停於步驟 7。**
步驟 1–6、8–10 全部完成。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| A 建立 `handoff/02_rebaseline.md` | DONE（原不存在，直接建立；strict UTF-8 通過，§A 六個 fenced block） |
| 1 實測七份原始檔填入台帳（R-P13） | DONE |
| 2 G0 前置閘 | **PASS 7 / 7** |
| 3 素材入 `inputs/` | DONE（`.gitignore` 已含 `inputs/`，未入版控） |
| 4 依 R-P3′ 抽文字層、驗 §C 正則 | DONE —— 匹配成立，但需一項文字層定義決策（A-PW11） |
| 5 重跑抽取，產出 leaf → (CFTS, 章節號, 章節標題) | DONE（`data/leaf_main_chapter.json`，114 筆） |
| 6 §D 自驗 | **G6 / G12 不符；G8 / G9 已填空** |
| 7 §E 重算比對 | **MISMATCH → 停**（實測 62 / 24 / 16 / 8 / 3 ＋ 未歸類 1） |
| 8 §A 裁決抄入 RULINGS.md、§F 入 ANOMALIES.md、§G 入 DATA_REQUESTS.md | DONE（並補抄 01 包 R-P1–R-P8，該包步驟 5 未執行） |
| 9 DECISIONS.md `[AUTO]` 項 | DONE（`[PROPOSED]` / `[PEI]` 留空待裁） |
| 10 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

**產出之可重現腳本**（皆為執行層新增）：

- `features/power/scripts/extract_textlayer.py` —— 文字層抽取（R-P3′）
- `features/power/scripts/verify_gates.py` —— §D 閃點自驗 ＋ §E 重算

兩者皆為純讀取，不寫回任何 xlsx。

---

## 一、下放包建立情形

`features/power/docs/handoff/02_rebaseline.md` **原不存在**，故為直接建立，
不涉及覆寫。實測：9,887 bytes，strict UTF-8 一次解碼通過，
U+FFFD = 0，§A 之 fenced block = 6，編號 `R-P9…R-P14` 無缺無重，
`R-P3′` 之 PRIME U+2032 完好。

> **登記一項自檢矛盾（未自行修正）**：§A 末句與 §H 步驟 8 皆寫「七條」，
> 但 §J 自檢清單列六條，且 §A 實際區塊數為 **6**（R-P9–R-P14）。
> 三處中兩處（§J、實測）一致為六。依「不得自行修改裁決條文」，
> 原文照錄未改，於此登記待分析層訂正。

---

## 二、素材台帳 —— 原始檔（R-P13 (a)）

目錄：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/`
（七份皆已複製至 `features/power/inputs/`，複製後重測與原始檔位元組相同。）

| 角色 | bytes | magic bytes | 真實格式 | SHA256（全 64 碼） | 檔名 |
|---|---|---|---|---|---|
| 交付標的（BLANK） | 78,607 | `50 4b 03 04` | ZIP/OOXML | `ce93174794d0d43c03d25dcd577c2811b85a8ebb2fd754a5201e5d6979297eda` | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx` |
| 需求母體（115 leaf） | 85,210 | `50 4b 03 04` | ZIP/OOXML | `2284abf5e6c17e4d1a082cf70d676b6551e16e023387c642f3fd1959c3478c8d` | `Power_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` |
| 上游需求（337 條） | 227,822 | `50 4b 03 04` | ZIP/OOXML | `6af7bfd314a28b3925636b642dc80c87918b50136fb8fa264563b3dc117eb592` | `SYS2_CFTS_009_Wake_Up_and_Power_Up_Polarion_uploaded_All_Accepted_04_13_2026.xlsx` |
| 上游需求（73 條） | 64,422 | `50 4b 03 04` | ZIP/OOXML | `f318b14623fcbf972c6d0428408a6cf5297cbe7d0a710c7fafb8a0e05f538e61` | `SYS2_CFTS_010_Power_down_Polarion_uploaded_All_Accepted_04_13_2026.xlsx` |
| 規格本文 | 154,588 | `50 4b 03 04` | ZIP/OOXML | `eb3eb0861363fc1d85c6127564355a7414ecd37eac0800336bb0d2e9b2911a26` | `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658.docx` |
| 規格本文 | 245,248 | `d0 cf 11 e0 a1 b1 1a e1` | **OLE2** | `47c402a01b1a2e3a537797843b968ad621fc2bbc6f7a416a33dfe490247ea505` | `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658.`**`doc`** |
| 架構文件（不具 TC 權威，未讀） | 3,474,091 | `50 4b 03 04` | ZIP/OOXML | `cb6bf7d81030abc8ce47a444b4cf90b6bf527816fde7887b9e9b872c22338ae4` | `SYS3_CFTS_009_Power_Management_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.1.0.docx` |

**01 包 §B 之舊表已整體作廢，本表不與其並列。**

### G0 素材身分前置閘（R-P14(a)）

`inputs/` 內七份之 SHA256 與上表逐一比對：**7 / 7，無缺無多。PASS。**
（`verify_gates.py` 於 G0 不通過時 `SystemExit`，G1 以後不執行、不回報。）

---

## 三、素材台帳 —— 衍生物（R-P13 (b)(c)）

| 衍生物 | bytes | SHA256（全 64 碼） | 來源原始檔 | 轉換工具與完整指令 |
|---|---|---|---|---|
| `data/textlayer/cfts009_plain.txt` | 398,293 | `2142717b9d7cf56e03c0eb227883a3552a37d9ee0157311283a1d7159972f67d` | CFTS009 `.docx`（`eb3eb086…`） | `python features/power/scripts/extract_textlayer.py` → `zipfile` 讀 `word/document.xml`，逐 `w:p` 串接 `w:t` |
| `data/textlayer/cfts009_bold.txt` | 405,729 | `9d1a9e40075977f97583da53940efbb0f1e06a87cb5db375435a577d54033b18` | 同上 | 同上，另對 `w:rPr/w:b` 之 run 加 `**` 標記 |
| `data/textlayer/cfts010_plain.txt` | 82,913 | `a7d274baae73ea522ff5de04b68f5ed4811934baf5e5872dfab0916aefb34463` | CFTS010 `.doc`（`47c402a0…`） | `python features/power/scripts/extract_textlayer.py` → `textutil -convert html -stdout <file>`，逐 `<p>` 去標籤 |
| `data/textlayer/cfts010_bold.txt` | 84,741 | `8a6f8445fc225dcebecd1aa79d663296452dd7e2da8d0c76df33cc7a60786427` | 同上 | 同上，另對 `<b>` / `<strong>` 內文加 `**` 標記 |

三欄齊備，可重現（重跑腳本得同一雜湊）。
SYS3 SYSAD 依 01 包 §B 不讀，無衍生物。

---

## 四、§C 正則在原始檔文字層之實際匹配情形（**上繳項一**）

### 4.1 單一序列化無法同時滿足兩條正則

| 序列化 | CFTS009 章節錨點 | CFTS009 需求錨點 | CFTS010 章節錨點 | CFTS010 需求錨點 |
|---|---|---|---|---|
| 全部粗體加 `**` | 172 | **904** | **0** | **148** |
| 完全不加標記 | **196** | **0** | **92** | **0** |

成因（登記為 **A-PW11**）：兩份 CFTS 之標題粗體機制不同。

```
[cfts009] 章節錨點行 plain : '1 Wake-up and Power-up [CFTSMV009_CIP_R4] {4941006}'
[cfts009] 同段 bold 版     : '1 Wake-up and Power-up [CFTSMV009_CIP_R4] {4941006}'      ← 無變化
[cfts010] 章節錨點行 plain : '1 Power Down [CFTSMV010_CIP_R3] {4942192}'
[cfts010] 同段 bold 版     : '**1 Power Down [CFTSMV010_CIP_R3] {4942192}**'            ← 尾隨 ** 破壞 $ 錨定
```

CFTS009 之標題以**段落樣式** `pStyle 1–8` 表達（run 層無粗體屬性）；
CFTS010 之標題為 **run 層粗體**。而兩份的需求錨點段落**都是整段粗體**，
故「整段粗體視為標題、不加標記」之規則也不可行 —— 實測會把需求錨點一併殺光
（兩份皆得 0）。

### 4.2 執行層採用之統一定義（**待分析層追認**）

> 每段同時產出 `plain` 與 `bold` 兩種序列化；
> **rule 1（章節錨點）套用於 `plain`，rule 2（需求錨點）套用於 `bold`**，
> 兩者依段落索引對齊，故 rule 2 之「歸屬於其前最近之章節錨點」仍成立。

理據：`**` 是為 rule 2 而存在的人工標記，rule 1 是純文字樣式匹配，
兩者本就不需共用同一份序列化。此定義對兩份 CFTS **一致適用**，無需逐檔特例。

**正則本身一字未改**（§I 禁區）。改變的只是「文字層」這個名詞的所指。

### 4.3 該定義下之匹配結果

| | 章節錨點 total / unique | 需求錨點 total / unique | 可歸屬 item |
|---|---|---|---|
| CFTS009 | 196 / 196 | 904 / 904 | 904 |
| CFTS010 | 92 / 92 | 148 / 148 | 148 |

四數中三數與 01 包舊值相同（904、148、92）。唯一差異是
**CFTS009 章節錨點 172 → 196**。獨立佐證差額 24 項為真標題：

- 24 項之段落樣式全部為 `pStyle 7`（15 項）與 `pStyle 8`（9 項）
- 196 項之樣式分布：`pStyle 5`×83、`3`×38、`4`×34、`7`×15、`2`×9、`8`×9、`6`×7、`1`×1
  —— **196 項全部具 heading pStyle 1–8，無一例外**，等於用文件自身的樣式結構
  獨立驗證了「rule 1 套 plain 恰好選出標題段落」
- 樣本：`1.3.1.11.3.1.1 SLEEP MODE {4941074}`、`1.3.3.5.1.1.1 Branded Font {4941272}`
  —— 皆為深層小節，其標題文字為粗體，在全粗體序列化下被 `**` 破壞而漏算

結論：**172 是衍生物粗體處理造成的漏算，196 為正確值。**
依 R-P11，G8 之章節錨點期望值改為 196。

### 4.4 文字層樣本

依 §C 末之要求，四份序列化各取前 3000 字元，存於
`features/power/data/textlayer/SAMPLES_3000.md`（12,511 bytes）。

---

## 五、§D 各項實測值對照表（**上繳項二**）

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 素材身分：七份原始檔 SHA256 全數登記且可重現 | 7 / 7 | **7 / 7** | PASS |
| G1 | 037 leaf 數 | 115，`SWE-PM-001`–`115` 連續無斷點 | **115**，連續無斷點 | PASS |
| G2 | 037 Categorization 值域 | 單一值 `Functional Requirement` ×115 | `{'Functional Requirement': 115}` | PASS |
| G3 | leaf → CFTS 章節解析成功數 | 114 / 115，唯一失敗者 `SWE-PM-089` | **114 / 115**，失敗者 `SWE-PM-089` | PASS |
| G4 | leaf 域分布 | 111 / 3 / 1，三組互斥 | **111 / 3 / 1**，兩者皆有 = 0 | PASS |
| G5 | 需 CFTS010 之 leaf | `SWE-PM-071` `072` `073` | **恰為該三者** | PASS |
| G5b | 該三 leaf 之解析章節 | 落於 CFTS010 §1.7.1 與 §1.7.2 | `071`→**§1.7.1.1.1**、`072`→**§1.7.1.1.1**、`073`→**§1.7.2** | PASS（§1.7.1.1.1 為 §1.7.1 之子節；實際解析深度較期望值細三層，登記備查） |
| G6 | SYS2 CFTS009 全 id 可解析者 | 336 / 337（失敗者 `Sys-RA-PM-0334`） | **337 / 337**（§C 範圍 r2–r338） | **MISMATCH** |
| G7 | SYS2 CFTS010 全 id 可解析者 | 73 / 73 | **73 / 73** | PASS |
| G8 | CFTS009 需求錨點 / 章節錨點 unique | 【重測後填入】 | **904 / 196** | 已填空（R-P11） |
| G9 | CFTS010 需求錨點 / 章節錨點 unique | 【重測後填入】 | **148 / 92** | 已填空（R-P11） |
| G10 | FW036 workbook_state | BLANK（c2–c35 × r10–r221 非空 = 0） | 非空儲存格 **0** → **BLANK** | PASS |
| G12 | §C 三組 xlsx 讀取座標 | 實測與 §C 所載一致 | 037 相符；**SYS2 CFTS009 不符**；SYS2 CFTS010 相符；FW036 相符 | **MISMATCH** |

### 5.1 G6 不符 —— 期望值本身有誤，非資料有誤

`Sys-RA-PM-0334` 位於 SYS2 CFTS009 匯出 **r325**，其
`SYS2 來源需求項目ID  Source Requirement items` 欄 = `4942087`，
**可被 `\d{6,8}` 正常解析**。它不是 rule 3 的失敗項。

它真正的異常（A-PW02）是：`4942087` 在兩份 CFTS 本文中都不存在，
因此無法解析至任何章節 —— 那是錨點鏈**第三段**的缺口，
而 G6 量的是**第一段**（欄內 token 是否可抓）。01 包把兩者混為一談。

§C 範圍 r2–r338 內 337 列全部非空，且全部可解析 → **337 / 337**。
ANOMALIES 之 A-PW02 已訂正證據描述；DR-PW3 之問題本身不變，仍為 live。

### 5.2 G12 不符 —— §C 之 SYS2 CFTS009 列範圍漏一列

| 座標 | §C 所載 | 實測 | 判定 |
|---|---|---|---|
| 037 `SWE1 Requirements` | 表頭 r7；資料 r8–r145 = 138 列，其中 23 列全空 → 115 實體 | **138 / 23 / 115**，且 r146 以後非空列 = 0 | 相符 |
| SYS2 CFTS009 `Basic Report` | 表頭 r1；資料 r2–r338 | 表頭 r1 相符（80 欄）；**資料實際延伸至 r339** —— r339 = `NRL-142587`，其 Source Requirement items 為空；r340 起為空 | **不符** |
| SYS2 CFTS010 `Basic Report` | 表頭 r1；資料 r2–r74 | r2–r74 = 73 列全非空，r75 為空 | 相符 |
| FW036 `Test Case Specification&Result` | 表頭 r9；資料 r10–r221 | 表頭 r9（c2–c35 共 34 欄具標頭，c1 無標頭無資料）；max_row = 221 | 相符 |

影響：若採實測範圍 r2–**r339**，G6 變為 **337 / 338**（失敗者 `NRL-142587`）；
若採 §C 之 r2–r338，則為 **337 / 337**。
**兩者皆非舊期望值 336 / 337。** 登記為 **A-PW09**。
本包之 G3 / G5b / §E 一律採 §C 所載之 r2–r338（未自行擴張座標）。

### 5.3 附帶登記 —— §C 引述之欄名與實測不符

§C rule 3 引欄名為「`SYS2 來源需求項目ID Source Requirement items`」（單空格），
實測標頭為「`SYS2 來源需求項目ID  Source Requirement items`」（**ID 後兩個空格**）。
以字串等值取欄會取不到。本包以子字串比對繞過，不影響結果，於此登記。

---

## 六、§E 重算之 Test Set leaf 分布（**上繳項三**）—— **MISMATCH，停**

主章節判定規則：每 leaf 取其解析到之章節中出現次數最多者，同數時取章節號最深者。
（**此規則為執行層自訂 —— §E 只寫「每 leaf 只計主章節」，未定義何謂主章節。見 §七第 1 項。**）

| Test Set | 實測 | §E | 判定 |
|---|---|---|---|
| Power State | **62** | 64 | **MISMATCH（−2）** |
| Startup Display | 24 | 24 | PASS |
| Branding and Theme | 16 | 16 | PASS |
| Timeout Settings | **8** | 7 | **MISMATCH（+1）** |
| Power Down | 3 | 3 | PASS |
| **未歸類** | **1**（`SWE-PM-057` @ 009 §1.6.2.1.17） | — | **§E Layer 3 未涵蓋** |
| 合計 | **114** | 114 | 總數相符 |

**依 §E 末與 §I 禁區，不逕行改寫 §E，停並上繳。**

### 6.1 三項具體差異

1. **§E Layer 3 未涵蓋 CFTS009 §1.6.2.1.17**（§E 只列到 `.16`）。
   實測 `§1.6.2.1.x` 分布：`.1`×1 `.2`×3 `.3`×2 `.5`×1 `.6`×2 `.7`×2 `.8`×1
   `.13`×2 `.15`×**35** `.16`×**7** **`.17`×1**。
   唯一落在 `.17` 者為 `SWE-PM-057`。→ **A-PW10**
2. **§E 於 Power State 列出之 CFTS009 §1.8.1 實測 0 leaf。** → **A-PW10**
3. **Timeout Settings 多 1 leaf**。實測八項：
   `SWE-PM-008`(§1.6.7.1)、`038`(§1.6.4.1)、`060`(§1.6.3.1)、`061`(§1.6.3.1)、
   `062`(§1.6.3.1.2)、`063`(§1.6.4.1)、`064`(§1.6.4.1)、`065`(§1.6.4.1)。
   八項全部落在 §E 自己列的 §1.6.3 / §1.6.4 / §1.6.7 三章之下，
   無一可歸至他處 —— 故 §E 的「7」與其自己的 Layer 3 章節清單互不自洽。

### 6.2 §E 之張力維持登記（R-P14(c)）

§E 自承「本表實際只由 CFTS 章節單一來源支撐，**不是交集**」，
而同節標題寫「**已定版**」。本包未以實測覆蓋此一張力，僅照 R-P14(c) 維持登記。
**惟本次重算顯示：單一來源支撐的那一個來源（CFTS 章節），
在執行層獨立重跑下並不產生 §E 所載之分布。**
「已定版」目前缺乏可重現的產生程序。

---

## 七、獨立判斷：本包是否仍有該驗而未驗者（**上繳項四**）

01 上繳包 §6.2 之五項，本包處置如下：第 1 項（素材身分）→ G0，**已驗**；
第 2 項（閃點未驗素材身分）→ G0 之立意，**已解決**；
第 3 項（§E／G11 循環）→ R-P14(b)(c)，**G11 已移除，張力維持登記**；
第 4 項（G5 驗得淺）→ G5b，**已驗**；第 5 項（§C 座標）→ G12，**已驗且查出一處不符**。

**以下為執行層自判之新增未驗項，共六項。**

### 1.（最重）「主章節」之定義從未寫下，而 11 / 114 個 leaf 取決於它

§E 只寫「每 leaf 只計主章節」。當一個 leaf 解析到多個章節時，
哪一個是「主」？§E、§C、§D 三處皆無定義。

實測每 leaf 解析到之**相異章節數**分布：
`1 章`×103、`2 章`×1、`3 章`×7、`4 章`×2、`6 章`×1 —— **11 個 leaf 跨多章節**。
（其上游 token 數分布：1 個×90、2 個×7、3 個×2、4 個×7、5 個×1、6 個×2、
7 個×1、8 個×2、9 個×1、13 個×1。）

本包採「出現次數最多、同數取最深」。換一條同樣合理的規則
（取第一個 token、取章節號最小、按 token 順序、平均分攤……）
會得到**不同的 leaf 分布**。§E 的 64 / 24 / 16 / 7 / 3 與本包的 62 / 24 / 16 / 8 / 3
差距恰為 ±2 / ±1，完全落在這 11 個 leaf 的擺盪範圍內。

**這比 §1.6.2.1.17 更可能是 §E 不符的真正成因，且它不在任何閃點表上。**
建議下一包把主章節規則寫成裁決條文，並增設閃點驗證「跨多章節 leaf 數」。

### 2. §E 丟棄的次章節資訊未經任何登記

11 個跨多章節 leaf 的非主章節被靜默丟棄。Layer 3 若要宣稱涵蓋規格，
這些被丟掉的章節是否已被其他 leaf 覆蓋，**未驗**。
（極端例：某 leaf 解析到 6 個相異章節，只留 1 個。）

### 3. `SWE-PM-089` 以外，是否另有 leaf 之上游 token 解析不到 SYS2 —— 未驗

G3 只回報「解析成功 / 失敗」的 leaf 層結果。
一個 leaf 若有 13 個 token 而其中 12 個解析失敗、1 個成功，G3 仍記為成功。
**token 層的解析成功率從未量測。** A-PW02 之 `4942087` 正是這類漏網
（它屬 `Sys-RA-PM-0334`，而該 Sys-RA 是否被任何 037 leaf 引用亦未查）。

### 4. CFTS010 之 `textutil` 轉換為不可逆之外部工具，其版本未入台帳

R-P13 要求登記「轉換工具與完整轉換指令」，本包已登記指令，
但 `textutil` 之版本隨 macOS 更新而變，**同一指令在不同機器上未必產生同一雜湊**。
本包之衍生物雜湊在本機可重現，跨機器**未驗**。
建議台帳增登 OS 版本（本機 Darwin 25.5.0）。

### 5. SYS3 SYSAD 仍完全未讀（01 §K 第 1 項，本包未處置亦未設閘）

02 包 §D 未給它任何閃點，§H 未給它任何步驟。它已入台帳（3,474,091 bytes，
OOXML，`cb6bf7d8…`），R-P3′ 也已解除讀取禁令 —— 讀它的技術障礙已消失，
但**仍未讀**。§4.x 之元件分解是否影響 Layer 2 邊界，仍是開放問題，
且此問題正好與 §六之 Test Set 分布爭議直接相關。

### 6. 037 `SYS2 Traceability` 與 `Excluded NRLs (HW-only)` 兩分頁從未被任何閘讀過

A-PW03 / A-PW04 / A-PW05 三條 anomaly 全部宣稱這兩分頁的內容
（26 筆排除、33 列追溯、命名空間不一致），但 §C 沒有它們的讀取座標，
§D 沒有對應閃點。**三條 anomaly 的證據自 01 包以來從未由執行層複驗**，
且其原始量測是否也來自失效衍生物，無從判斷（它們是 xlsx，雜湊已驗明，
故風險低於 CFTS，但「低風險」不等於「已驗」）。

---

## 八、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | 僅以 `read_only=True` 開啟，未寫入 |
| 不得執行任何 git 操作 | 未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()`；所有 workbook 皆 `read_only=True` 並 `close()` |
| 不得補齊 `SWE-PM-089`（R-P1） | G3 實測 114/115，該 leaf 留空，未填補 |
| 不得沿用三份純文字衍生物之任何數字（R-P10） | 全部 CFTS 數字自原始檔重新產生；舊值 172 經實測推翻為 196 |
| 不得自行調整 §C 正則 | 兩條正則一字未改（見 `extract_textlayer.py` 之 `SEC_RE` / `REQ_RE`）。改變的是「文字層」之序列化定義，已於 §四明列並待追認 |
| 不得逕行改寫 §E | §E 未動。重算結果僅上繳，並停於步驟 7 |
| 素材補入超出 `features/power/inputs/` 需 Pei 裁定 | 僅複製 §B 所列七份至 `inputs/`，未補入任何額外素材 |

---

## 九、待裁

- **Q1（阻斷 framework）§E leaf 分布重裁。** 需一併裁定：
  （a）**主章節之判定規則**（§七第 1 項 —— 建議優先，11 個 leaf 取決於它）；
  （b）§1.6.2.1.17 歸屬哪個 Test Set（A-PW10）；
  （c）§E Layer 3 之 §1.8.1 實測 0 leaf，是否刪除該章節。
- **Q2** §四之文字層統一定義是否追認為條文？（rule 1 套 plain、rule 2 套 bold）
- **Q3** G6 期望值改為 337/337（採 §C 之 r2–r338）或 337/338（採實測 r2–r339）？
  §C 之 SYS2 CFTS009 座標是否改為 r2–r339（A-PW09）？
- **Q4** §A 條數「七條」vs §J「六條」之訂正（§一）。
- **Q5** 是否讀 SYS3 SYSAD（§七第 5 項）？R-P3′ 後技術障礙已消失。
- **Q6** 是否補設閘驗證 037 `SYS2 Traceability` / `Excluded NRLs` 兩分頁（§七第 6 項）？
