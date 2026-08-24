# 上繳包 17 —— 「只列不改」之界線、質疑型條文之母體與 A-PMH14 之修正

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/17_scope_of_inventory.md](../handoff/17_scope_of_inventory.md)
- 前一包上繳：[16_verdict_blindspot.md](16_verdict_blindspot.md)
- **本包零寫回工作簿**

**16 包之提交狀態**：已於 2026-08-24 經 Pei 授權並提交（`f5d8cc7`，9 路徑）。
本包之提交待授權。

---

## 一、§五三條之抄錄核對表（步驟 1）

抄錄後**自 `RULINGS.md` 回讀**重新抽出，與 handoff 側逐位比對（R-PMH41）。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH63 | 「只列不改」限於待辦盤點，不適用於已知不實之陳述 | 384 | `65ec9bce9abddb63` | `65ec9bce9abddb63` | ✅ 逐字相符 |
| R-PMH64 | 質疑型條文之機械判準（回溯自套之母體） | 374 | `368719384072aec8` | `368719384072aec8` | ✅ 逐字相符 |
| R-PMH65 | 下放包只得記載分析層自身之行為（擴充 R-PMH48） | 338 | `d6dd025abf3c1f50` | `d6dd025abf3c1f50` | ✅ 逐字相符 |

**命中數**：handoff 側 3 塊、RULINGS 側回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH60`／`R-PMH62` 三者 SHA256 皆相符。

---

## 二、A-PMH14 之修正（步驟 2，R-PMH63）

**原句一字未改** —— 「**改判**（R-PMH51）」四列原樣保留，
更正以獨立段落置於其後（R-PMH44 之形態）。

更正段之三項：

### (a) `9.1` 之「維持」**不成立**

原句稱「9.1／11.1 —— 條列再流，**維持**（本輪方向二未在其上查出新漏）」，
**與同一則之「新漏 2」直接衝突** —— 新漏 2 所查出者即 p9 之狀態矩陣全缺，
而 p9 對應之 outline **正是 9.1**（該則自載「5 個 leaf 引 `9.1`」）。

正確判定：散文部分之條列再流**成立**，**惟其章之狀態矩陣整表缺失** ——
二者並存，「未在其上查出新漏」一語**不實**。

### (b) `11.1` 之「維持」**成立，不受影響**

其依據為同一則之「p10 之 VRLP1 四個 outcome —— **非漏**」，
確為方向二之實測結果。

### (c) `8` **當時不得引用；本輪補做後成立，且其歸因須更精確**

見 §三。

---

## 三、章 8 之雙向複驗全表（步驟 3 —— 本包最高優先）

新增 `scripts/chapter_bidirectional.py`，可對任一建錨之章重跑。

```
=== 章 8 之雙向複驗（R-PMH51）===
PDF 段：836 字元；SYS1：7 則、843 字元
PDF 段起錨 `R1Low Only`／訖錨 `[DCR19385]`
PDF 段內 marker：6 個 —— ['SSND 1)', 'SSND 2)', 'SSND 2.1)', 'SSND 2.2)', 'SSND 2.3)', 'SSND 3)']

--- 方向一（SYS1 → PDF）：SYS1 之字是否出現於 PDF ---
outline     字數  逐字命中     覆蓋率
8           17  **否**    100.0%
8.1        259  是        100.0%
8.2         94  是        100.0%
8.2.1      123  是        100.0%
8.2.2      157  是        100.0%
8.2.3      101  是        100.0%
8.3         86  是        100.0%

--- 方向二（PDF → SYS1）：PDF 之字是否出現於 SYS1 ---
PDF 段切出 8 句（>= 25 字元）
  #  逐字命中         覆蓋率  句首
  1  是        100.0%  R1Low Only SSND 1) If start-up sounds are supported, it wi
  2  是        100.0%  If goodbye sounds are supported, it shall sync on start wi
  3  是        100.0%  Sounds will sync amongst all supported vehicle displays.
  4  是        100.0%  SSND 2) Start-up and goodbye sounds shall have a setting w
  5  是        100.0%  SSND 2.1) If the setting is Always, start-up and goodbye s
  6  是        100.0%  SSND 2.2) If the setting is Once a Day, start-up and goodb
  7  是        100.0%  SSND 2.3) If the setting is Never, start-up and goodbye so
  8  是        100.0%  SSND 3) Sound volume level shall match current entertainme

=== 結果 ===
  方向一未逐字命中：1 則
    outline 8（覆蓋 100.0%）：Starup R1Low Only
  方向二真漏候選（覆蓋 < 30%）：0 句

  **新漏句：0** —— 停止條件 7 未觸發
```

### 3.1 結論：**章 8 無漏句**，「拼字」之歸因成立

方向二 8/8 逐字命中、真漏候選 0；PDF 段內 `SSND 1)`～`SSND 3)` 共 6 個 marker，
與 SYS1 之 6 leaf（8.1／8.2／8.2.1／8.2.2／8.2.3／8.3）一一對應。
**停止條件 7 未觸發。**

### 3.2 **惟其歸因須更精確** —— 原記之 PDF 字串於 PDF 中不存在

A-PMH03 原記：「export 之標題為 `Starup R1Low Only`（缺 `t`）；
**PDF 為 `Startup R1Low Only`**。」

**PDF 中無 `Startup R1Low Only` 此一連續字串** —— `pdftotext -layout`
與 PyMuPDF 兩份萃取皆無。以 PyMuPDF 之 `get_text("blocks")` 查 p8：

| y | 區塊 |
|---:|---|
| **21.6** | `Startup` ← **頁眉** |
| 469.3 | `R1Low Only\nSSND 1) If start-up sounds are supported…` ← **本文之節標題** |

故 SYS1 之 `Starup R1Low Only` **並非單純之拼字錯誤**，
而是**頁眉（`Startup`）與節標題（`R1Low Only`）兩個獨立文字物件之串接**，
且串接時掉了一個 `t`。

**影響：無。** 該標題不對應任何 Functional Requirement leaf
（章 8 之 6 leaf 為 8.1～8.3），亦不入任何 TC 之 `source_clause`。
已登記其正確形態於 A-PMH14 之更正段。

### 3.3 R-PMH51 之未套用側自此結清

R-PMH51 明文「未複驗前其標題結論不得引用」，
**而「拼字」之結論被沿用了兩包**（12 包記「不變」、13 包未在其上具名結論）。
本包補做後方成立。

---

## 四、四支檢查之限度具名段（步驟 4）

R-PMH52 之措詞為「**任何** lint」，而 16 §5.3 查出其實際只施行於
`lint_batch.py`。本輪擴及**五支**（下放包點名四支，另加本包新增之
`chapter_bidirectional.py`），格式統一。

### 4.1 `check_granularity.py`

```
=== 本檢查未涵蓋之範圍（R-PMH52）===
  - G1–G5 五項**只看組數與組員數之分布**；**不看任何組之內容** —— 一組 3 個 leaf 是否真屬同一能力，本檢查不判
  - Layer 2 之**組名**（字面、大小寫、是否與 Test Group 重複）不看 —— 該屬 R-PMH13／R-PMH36／canon §4.2
  - **分母 `n_leaf` 為外部給定**（現行 48）；其是否正確不由本檢查驗 —— DR-PMH3 若確認，48 → 50 而本檢查不會察覺
  - leaf 到組之**指派**不看 —— 只要分布合格，指派錯誤仍全綠
  - `--check-doc-sync` 只驗門檻表與程式同源；**不驗該門檻本身是否恰當**
```

### 4.2 `check_write_back.py`

```
=== 本檢查未涵蓋之範圍（R-PMH52）===
  - 四項只驗**寫回之前提與列數**；**不看任何欄之值** —— 寫入之 TC 內容是否正確，本檢查不判
  - **x14 data validation 之存留不驗**（R-G3）—— 寫回若以 `openpyxl.save()` 破壞 DV，本檢查仍全綠
  - **接線狀態未驗**：本檢查目前不被任何寫回路徑呼叫（`feature.yaml` 之 `write_back_checks.wired: false`）—— 一段未被呼叫之正確程式碼，其效力等同文字修補（通則 8）
  - 母本 DV 之兩項既知瑕疵（A-PMH12：`Q` 欄 sqref 跨欄、`AF` 之前導空白）不驗
  - 寫回**之後**之複驗不做 —— 本檢查只跑於寫回前
```

### 4.3 `marker_coverage.py`

```
=== 本檢查未涵蓋之範圍（R-PMH52）===
  - marker 之**內容**不看 —— 只驗其標記字串是否出現於 SYS1；該 marker 之需求文句是否完整（如 7.1 之漏句）屬 `bidirectional_spec_diff.py`
  - `VERDICT` 之判定值仍為人工 —— must-hit C 只攔「未判定」，**不攔「判錯」**；R-PMH61 之語氣檢查為部分補救，且其窗口只取 marker 之後
  - **候選集合隨萃取器而變**（16 §4.2：PyMuPDF 多出 `Loading`／`each`）—— 本檢查之候選以 `sandbox/spec.txt` 為準
  - 候選形態 `CANDIDATE` 仍是一個正規式 —— 若規格改用 `[A-3]` 或 `Req 4.1 -` 之類形態，反向掃描一樣看不見
  - SYS1 側只讀 `Basic Report` 之 `Description` 欄；**其餘欄不看**
```

### 4.4 `check_state_consistency.py`（已有 `EXCLUDED`，補齊格式）

```
=== 本檢查未涵蓋之範圍（R-PMH52）===
  - **互斥對 8 組為列舉而非全集** —— 未列舉之互斥形態不會被發現
  - 有效範圍只及三個狀態板（`framework.md`／`feature.yaml`／`PLAYBOOK.md`）；`RULINGS.md`／`ANOMALIES.md`／`DECISIONS.md` 已具名排除（散文檔，按條號切分之判準實測不可用）
  - **只驗同檔內之互斥**；**跨檔之矛盾不看** —— 如 `framework.md` 稱定版而上繳包稱未定版，本檢查全綠
  - 只比對**字面**之狀態詞；語意等價之不同措詞（「已鎖」vs「定版」）不視為同一狀態
  - 被排除之散文檔中之矛盾（如 16 包所查出之 A-PMH14）**須人讀**，本檢查看不見
```

### 4.5 `chapter_bidirectional.py`（本包新增）

```
=== 本檢查未涵蓋之範圍（R-PMH52）===
  - **`ANCHORS` 之起訖錨為人工指定** —— 錨取錯則整章比對落空；現只有章 8 建錨
  - 只比對 PDF **文字層**；**圖表不看** —— p9 之狀態矩陣即以圖呈現（A-PMH14 新漏 2）
  - 比對單位為句（>= 25 字元）；**短於 25 字元之句一律不入母體**，章 8 之標題 `Starup R1Low Only` 即屬之
  - 6-gram 覆蓋率 < 30% 之門檻為 13 包沿用值；**該門檻本身未經本輪重驗**
  - **只驗字之有無，不驗語意** —— 同義改寫會被判為漏句，改寫錯誤會被判為命中
```

### 4.6 **本步驟連帶觸發 R-PMH42，據實記載**

為 `check_granularity.py` 加上 `LIMITS` 後，`--check-doc-sync` **立即 FAIL**：

```
doc-sync **FAIL** — **門檻表已與程式分岔（雜湊）** ——
文件記 `eada46d05ea268f0…`，程式現值 `6d9fdbc53ddcd274…`。
```

**R-PMH42 之檢查確實會攔下**（此為其第二次實地兌現）。
依 R-PMH40 重跑 `--emit-thresholds` 並重貼門檻節、更新 SHA256 行後 PASS：

```
doc-sync PASS — 文件與程式同源 —— SHA256 `6d9fdbc53ddcd274…`（命中 1 處）＋ 門檻表 7 列逐字相同
```

**惟須具名其粗度**：該檢查以**整支程式之 SHA256** 為錨，
故**任何編輯（含純註解、含本次之 `LIMITS` 常數）皆會使文件失效**，
而門檻本身一字未動。**「文件與程式同源」之保證強，其代價是誤報率高。**
本輪之 FAIL 即為此類 —— 不是門檻分岔，是程式被改了。

---

## 五、R-PMH64 之回溯（步驟 5，母體版）

新增 `scripts/challenge_rulings.py`。

### 5.1 判準之命中

```
=== 質疑型條文之候選清單（R-PMH64）===
`RULINGS.md` 之條文總數 = **65**；判準標記 = 15 個；**候選 = 23**
命中率 = 35.4%

條號         命中之標記
R-PMH8     撤回
R-PMH9     作廢
R-PMH10    取代
R-PMH13    撤回
R-PMH15    取代
R-PMH16    不符
R-PMH17    取代
R-PMH23    矛盾
R-PMH24    取代／撤回
R-PMH26    不成立
R-PMH27    作廢／取代
R-PMH39    作廢／取代
R-PMH41    不符
R-PMH42    不符
R-PMH50    由…查出
R-PMH51    不符／改判
R-PMH55    不成立
R-PMH59    矛盾
R-PMH60    誤用
R-PMH61    判錯
R-PMH62    不成立／之錯／由…查出
R-PMH63    矛盾
R-PMH64    不成立／不符／之瑕疵／之缺陷／之錯／作廢／判錯／取代／推翻／撤回／改判／未套用／由…查出／矛盾／誤用
```

### 5.2 逐條確認：**候選 23 → 偽陽 6、質疑型 17**

**偽陽 6 條**：

| 條號 | 偽陽之成因 |
|---|---|
| **R-PMH64** | **判準之自命中** —— 該條**列舉了標記清單本身**，故必然全部命中。此為結構性偽陽，無法以判準排除 |
| R-PMH10 | 其「取代」為**被質疑者**之標記（由 R-PMH27 換依據），非質疑主體 |
| R-PMH16 | 「不符」指其自保之已知反例（Comfort），非質疑他條 |
| R-PMH17 | 追認型，其「取代」為引用 R-PMH15 |
| R-PMH26 | 「不成立」出現於其 (d) 之條件句，非質疑既有結論 |
| R-PMH55 | 「不成立」指 ER 之斷言條件，非質疑既有結論 |

**質疑型 17 條**，其中**已雙向自套 11 條**、**未套用或未查明 6 條**。

### 5.3 已雙向自套者（正面記錄）

| 條號 | 其回頭套用之對象 |
|---|---|
| R-PMH8／R-PMH9 | 同一「舊基底之量測作廢」判準，由 R-PMH8 套於 `workbook_state`、R-PMH9 套於欄位對應 —— **成對出現** |
| **R-PMH13** | **條文內明寫**：撤回 R-PMH2 之後半，同時檢驗其前半並判其「維持有效 —— 其為 repo 內部識別，不進入任何交付欄位」 |
| R-PMH15 | 明寫「R-PMH11 之目的未變，本條僅取代其所指定之寫法」 |
| **R-PMH24** | **條文自身即要求雙向**：「新增反向驗證義務 —— 套用任何母體規則後，須逐項列出被排除之檔案」 |
| R-PMH41 | 10 包「替換殘留回掃」逐項複驗同批之其餘替換（16 §5.2 已確認） |
| R-PMH42 | 同一「宣告≠落實」判準已套於 `write_back_checks.wired: false`（`DECISIONS.md` 具名為 KNOWN-INCOMPLETE） |
| **R-PMH51** | **未套用側（outline `8`）於本包步驟 3 結清** |
| R-PMH59 | 未套用側（`-002`）於 15 §4.2 結清、`-005`～`-007` 於 16 §三結清 |
| R-PMH61 | 窗口方向之未驗面於本包步驟 6 對照 |
| R-PMH62 | 本步驟即其執行 |

### 5.4 **未套用或未查明者 6 條（只列不改）**

| # | 條號 | 其判準 | **未套用之一側** |
|---|---|---|---|
| 1 | **R-PMH50** | 「SYS1 匯出相對 PDF 有偏離，故 `source_clause` 取自 PDF」 | **`data/layer3_sections.tsv` 之 `section_title`／`chapter_title` 全部取自 SYS1**（`build_layer3_sections.py` 之 `outline_title`）。若某 leaf 之 SYS1 描述漏句，該 TSV 亦漏，**而 lint 之 §3.4 檢查正是拿 TSV 之 outline 對照**。TSV 之來源已於程式 docstring 具名，**非不實陳述**，故屬「待決定之事」 |
| 2 | **R-PMH39** | 「`0.35` 係湊得，且現有錨點對其無鑑別力，依 R-PMH14 不足以支持」 | **同一判準未回頭套用於 G3 與 G5**。G2（`>=2`）／G4（`<=1/2`）有 canon §4.1.3 之明文，**而 G3 之收容簇清單（`general`／`misc`／`other`／`unclassified`／`雜項` 五個字串）與 G5 之區間端點，其來源未受同一檢驗** |
| 3 | **R-PMH60** | 「字元數為代理量，不得作為判準」 | **未回頭套用於其他代理量** —— A-PMH03 之「43 則中 39 則命中」覆蓋率、雙向 diff 之「6-gram < 30%」門檻、granularity 之比例門檻，**皆為代理量而未受同一檢驗** |
| 4 | R-PMH23 | 「客戶那份之 ChangeHistory 已被他 feature 之寫回污染，該五頁不得取用」 | **其所放行之三頁（`Reference`／`QS Suggestion`／`Test Case Framework`）是否受同一污染，條文未查** |
| 5 | R-PMH27 | 「R-PMH10 之依據母體未定義」 | **未回頭掃其他以舊母體（「語料 5/5」）為據之結論** —— 是否尚有他條建於同一未定義母體，未查 |
| 6 | R-PMH63 | 「下放包不得以措詞暫停既有條文」 | **未回頭掃其他下放包**是否有同型措詞（如「本輪不動」「維持現狀」）實質暫停既有條文者 |

### 5.5 依 R-PMH63 須立即更正者：**本步驟所列 6 項皆無**

逐項判別「待決定之事」vs「檔案中已知不實之陳述」：

- 第 1 項之 TSV 來源**已於 `build_layer3_sections.py` 之 docstring 逐字具名**
  （「`outline_number` 與其所屬『章』皆取自 SYS1 匯出之 `Outline Number`」）
  —— **無不實陳述**，該用不該用屬待決定；
- 第 2～6 項皆為「同一判準是否應擴及某處」之待決定，**非現存之錯誤陳述**。

**本包唯一之立即更正為步驟 2 之 A-PMH14**（16 包已指認者），已完成。

---

## 六、語氣檢查之雙窗口對照（步驟 6）

```
窗口取 marker 其前）===
受檢前綴 = 13 個（判為 `noise`／`xref` 者）

前綴         判定       語氣命中  證據
CFTS       xref        0  —
CR         xref        0  —
CTS        xref        2  CTS009) → 情態動詞 `shall`；CTS009) → 情態動詞 `should`
DCR        xref        3  DCR20015) → 情態動詞 `will`；DCR19385) → 情態動詞 `shall`
High       noise       0  —
Low        noise       0  —
a          noise       0  —
and        noise       0  —
expires    noise       0  —
of         noise       0  —
sec        noise       0  —
the        noise       0  —
to         noise       0  —

**須人讀確認之前綴**：['CTS', 'DCR']
  （只具名，**不自行改判** —— 判定值之變更須另有依據）
```

```
=== 兩窗口之旗標對照（17 包步驟 6）===
  取其後（現行）：['CR', 'CTS', 'DCR']
  取其前（對照）：['CTS', 'DCR']
  只在其後：['CR']
  **只在其前：無**  ← 此集合非空即表示現行窗口看不見之語氣證據確實存在
  **只回報，不改現行窗口之選擇**（16 §10 第 1 項之自提項）。
```

### 6.1 結果：**「只在其前」為空集**

現行（取其後）旗標 `['CR', 'CTS', 'DCR']`；對照（取其前）`['CTS', 'DCR']`。
**其前之旗標為其後之真子集** —— 本規格中**不存在**任何前綴，
其需求語氣證據只落在 marker 之前。

**故 16 §10 第 1 項所擔憂之情形（句尾型 marker 之證據落在窗外），
於本規格未實際發生。**

**惟須明說其限度**：這證明的是「**在這份規格裡**沒發生」，
不是「窗口方向之選擇無關緊要」。判準之限度仍在（已寫入
`marker_coverage.py` 之 `LIMITS` 第 2 項）。

**只回報，未改現行窗口之選擇。**

---

## 七、`shasum -c` 之輸出（步驟 7）

```
FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx: OK
FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerModingHMI_20260819.xlsx: OK
FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1 STLA 報告.xlsx: OK
SYS1_HMI_Power_Moding_HMI_Logic_and_Flow_R1_SR24_2A.xlsx: OK
Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023).pdf: OK
```

**5/5 OK。** 下放包記「四份素材」——
`MANIFEST.sha256` 實為**五筆**（036 母本 ＋ 036 客戶複本 ＋ 037 ＋ SYS1 ＋ PDF）。
**PDF 本體自 01 包搬入後未變**，故 16 §10 第 2 項所指之風險
（「PDF 被換過，兩份萃取一致地錯」）**經此複驗排除**。

---

## 八、lint 全跑輸出（步驟 6 之延續）

**本輪未動 `generated/batch01.json`。**

```
batch = batch01；TC 數 = 8；leaf 數 = 7

  R-PMH50 每 leaf 有 source_clause 且非空                       PASS
  R-PMH50 source_clause 取自 PDF（非 SYS1）                     PASS
  profile §3.1 test_item 具下半括號（硬規則）                        PASS
  profile §3.3 design_method ∈ 下拉選單 9 詞條                   PASS
  profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符  PASS
  profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）             PASS
  profile §3.6 estimated_test_time 留白                      PASS
  profile §3.8 vehicle_models 留白                           PASS
  profile §3.7 functional_safety = NA                      PASS
  R-PMH18 test_group = 'Disclaimer screen'（小寫 s）           PASS
  R-PMH36 test_set = 'Disclaimer Screen'（大寫 S）             PASS
  R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}             PASS
  test_set ∈ Layer 2 定版 8 組                                PASS
  canon §11 方括號禁止（本 feature 無 profile 例外）                  PASS
  procedure 與 ER 步數一致                                      PASS
  必填欄無空                                                    PASS
  ER 未以 NA 充當未知                                            PASS
  canon §10.5 test_procedure >= 2 步                        PASS
  canon §5.1 procedure 無禁用動詞                               PASS
  canon §5.2B/§5.5 Final Step 含驗證意圖                        PASS
  canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）      PASS
  交付欄位無 markdown 標記（**／__／`）                               PASS
  canon §11 無彎引號                                           PASS
  canon §11 UI 標籤加直雙引號                                     PASS
  canon §5.2 步驟字數（normal <=12／final <=18）                  PASS
  R-PMH53 交叉引用存在且語意相容                                      PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

30/30 PASS

⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：
    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 `COVERED` 產生，**不手寫**。
    執行：`python scripts/canon_coverage.py`
    本 lint 宣告涵蓋 10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**
    R-PMH52：lint 全綠不得作為 TC 可用之證據。

⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。
  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  本檢查只保證覆核所需之材料存在，不保證覆核已做。
```

**must-hit 兩份 fixture 仍 FAIL**：`batch01_prerework` 21/30／`batch01_r2` 29/30。

---

## 九、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| **`chapter_bidirectional.py 8`** | **PASS** —— 方向二 8/8 命中，新漏 0 |
| `marker_coverage.py --self-test` | **PASS** —— must-hit A・B・C・D |
| `marker_coverage.py --verify-extraction` | **PASS** |
| `marker_coverage.py --window-compare` | **PASS** —— 「只在其前」為空集 |
| **`challenge_rulings.py`** | **PASS** —— 65 條、候選 23（非 0，判準未失效） |
| `canon_coverage.py` | **PASS** |
| `check_state_consistency.py` | **PASS** |
| `check_granularity.py --check-doc-sync` | **PASS**（先 FAIL、重貼門檻節後 PASS —— §4.6） |
| `check_write_back.py --self-test` | **PASS** |

---

## 十、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | 否（`shasum -c` 5/5 OK） |
| 2 | 判準衝突未決 | 否 |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是（既有）** —— DR-PMH1 阻斷交付 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 章 8 雙向複驗發現任一新漏句 | 方向二 8 句 8/8 逐字命中，真漏候選 **0** | **否** |
| 8 | 候選清單為 0（判準失效） | 候選 **23**／65 條，命中率 35.4% | **否** |
| 9 | `shasum -c` 有任一份不符 | **5/5 OK** | **否** |

**本包無新觸發之停止條件。**

---

## 十一、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | `OPEN` | **阻斷交付** |
| DR-PMH2 | Power Moding State Matrix Excel | `OPEN` | 否（阻斷 ch 9 判讀） |
| DR-PMH3 | `SU9.)`／`SU9.1)` 是否應在 037 | `OPEN` | 否（若確認，48 母體須重算） |

**三筆皆尚未發出。第五度重申。**
**DR-PMH2 本輪再獲佐證**：A-PMH14 對 9.1 之矛盾已於步驟 2 更正，
其正確判定即「狀態矩陣整表缺失」—— DR-PMH2 所索取者正是該矩陣。

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，五項。**

1. **章 8 之錨（`ANCHORS`）是我自己指定的，而錨錯了整章會落空得很安靜。**
   我以「PDF 段內 marker 數 = 6，與 SYS1 之 6 leaf 一一對應」為佐證，
   **但那只證明錨之間有 6 個 marker，不證明錨之外沒有第 7 個**。
   若章 8 之某句落在起錨之前，本次比對看不見它。
   **可行之下一步**：以相鄰兩章之錨互為邊界，驗全 PDF 被章覆蓋且無重疊。

2. **`chapter_bidirectional.py` 只對章 8 建了錨；R-PMH51 所涉之 9.1／11.1
   仍倚賴 13 包之全簿 diff，未經本檔逐章重跑。**
   §5.3 把 R-PMH51 記為「已結清」，**其依據是章 8 補做完成** ——
   9.1／11.1 之結論仍建於 13 包之判準（6-gram 30% 門檻），
   **而該門檻本身正是 §5.4 第 3 項所列之未受檢驗代理量**。
   **此二者互相指涉，我未能切斷該循環。**

3. **§5.2 之「偽陽 6 / 質疑型 17」是我逐條讀出來的判斷，沒有第二個來源。**
   R-PMH64 明令「輸出為候選清單，逐條由人確認」——
   **我就是那個「人」，而我同時也是寫判準的人。**
   `VERDICT` 至少還有 must-hit D 能驗其誤判，**本項沒有等價之驗證**。

4. **§5.4 六項之完整性，仍受判準之偽陰限制。**
   以其他措詞表達之質疑（如 R-PMH27 之「其依據更換如下」）不會命中標記，
   **而 R-PMH27 恰好因另一個標記（`作廢`）才進了候選** —— 那是運氣。
   **判準之偽陰率我沒有量測，因為量測它需要一份已知正解之清單。**

5. **§4.6 所述之 doc-sync 粗度，我具名了但沒改。**
   任何編輯（含純註解）皆使文件失效 —— 這會訓練出「重跑 emit 再貼上」
   之反射動作，**而該反射正是使 R-PMH42 失效之途徑**：
   若某日門檻真的變了，重貼之動作與本次完全相同，**沒有任何東西會提醒
   那次不一樣**。

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 17 — chapter 8 bidirectional verify, checker limits named, challenge-ruling scan
```

**pathspec（10 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/RULINGS.md \
  features/power_moding/framework.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/17_scope_of_inventory.md \
  features/power_moding/docs/upstream/17_scope_of_inventory.md \
  features/power_moding/scripts/challenge_rulings.py \
  features/power_moding/scripts/chapter_bidirectional.py \
  features/power_moding/scripts/check_granularity.py \
  features/power_moding/scripts/check_state_consistency.py \
  features/power_moding/scripts/check_write_back.py \
  features/power_moding/scripts/marker_coverage.py
```

（實為 **12 路徑**。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py` | **未動** |
| `docs/runtime/` 下之檔案 | **未動** |
| `PROFILE_INTEGRATION.md` | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **未動**（本輪不改 TC） |
| `framework.md` 之改動 | **僅門檻節之重貼＋SHA256 行**（R-PMH40／R-PMH42 所令），門檻值一字未變 |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出** —— **第五度重申** | **DR-PMH1 阻斷交付** |
| 2 | 17 之 commit 授權（12 路徑，見 §13） | 否 |
| 3 | §5.4 六項之處置（尤其第 1 項 —— TSV 之 SYS1 來源，與 lint §3.4 直接相關） | Phase 5 |
| 4 | Q10、`PROFILE_INTEGRATION.md` | 否 |
