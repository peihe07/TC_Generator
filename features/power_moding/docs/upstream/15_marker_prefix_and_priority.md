# 上繳包 15 —— marker 前綴之反向驗證、priority 之內部矛盾與 COVERED 自動化

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/15_marker_prefix_and_priority.md](../handoff/15_marker_prefix_and_priority.md)
- 前一包上繳：[14_marker_enumeration.md](14_marker_enumeration.md)
- **本包零寫回工作簿**；14／15 兩包之提交**未執行**（未授權）

---

## 一、§四三條之抄錄核對表（步驟 1）

抄錄方式：以程式自 handoff §四抽出三個 fenced block，**逐字**（含全形標點、
換行、`**` 標記）附加於 `RULINGS.md`，再**自 `RULINGS.md` 回讀**重新抽出，
與 handoff 側之字串直接比較 —— **驗其所欲之狀態，非其代理**（R-PMH41）。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH57 | marker 前綴清單須由反向掃描產生；先算後比抓不到共同前提之錯 | 450 | `24d7227229777e17` | `24d7227229777e17` | ✅ 逐字相符 |
| R-PMH58 | `COVERED` 須自檢查點自動彙集，不得手寫 | 263 | `5ab305927c4b7525` | `5ab305927c4b7525` | ✅ 逐字相符 |
| R-PMH59 | priority 之依據須批內互不矛盾 | 343 | `a95567765836a477` | `a95567765836a477` | ✅ 逐字相符 |

**命中數**：三條各命中 1 次（handoff 側抽出 3 塊、RULINGS 側回讀亦 3 塊，
逐位比對 `a == b` 皆 `True`）。

**既有條文之 SHA256 未動**（抽樣複驗，R-PMH44）：

```
R-PMH10  885070968235b262  ==  885070968235b262  True
R-PMH19  cbdeed8b8bc0774b  ==  cbdeed8b8bc0774b  True
R-PMH27  e6e14fc0a96c1ccc  ==  e6e14fc0a96c1ccc  True
```

---

## 二、marker 前綴之反向掃描（步驟 2，R-PMH57）

### 2.1 實作之形狀

`scripts/marker_coverage.py` 改為**兩段式**，前綴清單不再出現於原始碼之
枚舉式常數中：

1. **反向掃描** —— 以 `CANDIDATE = \b([A-Za-z][A-Za-z_ ]{0,8}?)\s?(\d+(?:\.\d+)?)\s?([.):])`
   掃 `sandbox/spec.txt` 全文，取每一命中之**末一個字詞**為候選前綴
   （`cycle SU9.)` 之前綴為 `SU`，非 `cycle SU`）；
2. **逐項判定** —— `VERDICT` 表對每一候選給三值之一：
   `req`（需求 marker）／`xref`（交叉參照）／`noise`（一般文句之偽命中），
   **並附其依據**；
3. **枚舉** —— marker 之正規式由判定為 `req` 者**組出**，非手寫。

**未在 `VERDICT` 表中之候選 → FAIL**（must-hit C 驗之）。此使新版規格引入
新前綴時**必然被攔下**，而非靜默漏掉整章。

### 2.2 前綴判定表（留檔）

```
=== 反向掃描之前綴判定表（R-PMH57）===
候選形態 = `\b([A-Za-z][A-Za-z_ ]{0,8}?)\s?(\d+(?:\.\d+)?)\s?([.):])`；候選前綴 = 20 種

前綴           次數  判定     樣例                                 依據
SU           13  req    SU1. SU1.1) SU2. SU2.1)            Start Up，章 7 之需求 marker
PITA          7  req    PITA4: PITA5: PITA6: PITA6.1:      Power ITA，章 10
SSND          6  req    Only SSND 1) SSND 2) SSND 2.1) SSN Start Up Sounds，章 8
OFF           3  req    OFF1. OFF2. OFF3.                  Power Off，章 12
DS            1  req    DS4.1)                             章 7 之需求 marker；其編號 4.1 與 SU4.) 呈父子，前綴由 SU 變 DS，極可能為規格原文筆誤（15 包 §2.3，依 R-PMH26 只登記不開 DR，一律照原文處理）
PM            1  req    PM1)                               Power Moding，章 9
VRLP          1  req    VRLP1:                             Voice Recognition Long Press，章 11
DCR           5  xref   DCR20015) DCR20015) DCR19385) DCR1 變更申請單號，非本規格之需求
CFTS          3  xref   CFTS009. see CFTS009. see CFTS009. 他規格文件編號（`CFTS009`）
CTS           2  xref   See CTS009) See CTS009)            同上（`See CTS009)`，`CFTS009` 之另一寫法）
CR            1  xref   CR19385)                           同上（`CR19385)` 與 `DCR19385)` 同一單）
High          5  noise  High 8. High 10. High 10. High 14. 一般文句：`High` + 版面尺寸數字
Low           4  noise  Low 8. Low 10. Low 10. Low 12.     一般文句：`Low` + 版面尺寸數字
a             4  noise  with a 1. with a 1. with a 1. with 一般文句：`with a 1.`
and           4  noise  Last and 1. Last and 1. Last and 1 一般文句：`Last and 1.` 之類
sec           4  noise  sec 1. sec 1. sec 1. sec 1.        一般文句：`sec 1.` 之類
the           2  noise  of the 10. the 12.                 一般文句：`of the 10.`
expires       1  noise  expires 3.                         一般文句：`expires 3.`
of            1  noise  of 10.                             一般文句：`of 10.`
to            1  noise  up to 2.                           一般文句：`up to 2.`

  全部候選前綴皆已判定：True
```

**與分析層 §2.1 之差異，據實記載**：`SU` 本層計 13 次而分析層計 12、
`SSND` 計 6 而分析層計 6、`CFTS`＋`CTS` 本層分計 3＋2 而分析層併計。
**差異全在「同一 marker 之重複出現與交叉參照式出現如何計次」，
不影響任何前綴之判定值，亦不影響去重後之 marker 全集。**
判定結果與分析層**完全一致**：七個 `req`（含 `DS`）、四個 `xref`、九個 `noise`。

### 2.3 範圍向 —— **31／2**（與 §2.2 之對照向相符）

```
=== 範圍向（R-G9）—— 現行素材 ===

=== marker 覆蓋（R-PMH54）（範圍向） ===
PDF marker 全集 = **31**；SYS1 缺 = **2**

  章  PDF marker                                                       缺
  7  SU1.) SU1.1) SU2.) SU2.1) SU3.) SU4.) DS4.1) SU5.) SU6.) SU7.)   2
      SU8.) SU9.) SU9.1)
  8  SSND 1) SSND 2) SSND 2.1) SSND 2.2) SSND 2.3) SSND 3)            0
  9  PM1)                                                             0
 10  PITA4: PITA5: PITA6: PITA6.1: PITA8: PITA9: PITA10:              0
 11  VRLP1:                                                           0
 12  OFF1.) OFF2.) OFF3.)                                             0

缺漏清單：['SU9.)', 'SU9.1)']

  與分析層 15 包 §2.2 之 31／2 相符：True
```

### 2.4 must-hit 三項

**A —— 自 SYS1 側移除一個已知存在之 marker**（沿用 14 包）：

```
=== must-hit A —— 自 SYS1 側移除已知存在之 marker `SU1.)` ===

=== marker 覆蓋（R-PMH54）（must-hit A） ===
PDF marker 全集 = **31**；SYS1 缺 = **3**

  章  PDF marker                                                       缺
  7  SU1.) SU1.1) SU2.) SU2.1) SU3.) SU4.) DS4.1) SU5.) SU6.) SU7.)   3
      SU8.) SU9.) SU9.1)
  8  SSND 1) SSND 2) SSND 2.1) SSND 2.2) SSND 2.3) SSND 3)            0
  9  PM1)                                                             0
 10  PITA4: PITA5: PITA6: PITA6.1: PITA8: PITA9: PITA10:              0
 11  VRLP1:                                                           0
 12  OFF1.) OFF2.) OFF3.)                                             0

缺漏清單：['SU1.)', 'SU9.)', 'SU9.1)']

  缺漏由 2 增為 3，且 `SU1.)` 在缺漏清單內：True
```

**B —— 自前綴清單移除 `DS`，即 14 包之人工列舉狀態**（本包所令）：

```
=== must-hit B —— 自前綴清單移除 `DS`（14 包之人工列舉狀態）===

=== marker 覆蓋（R-PMH54）（must-hit B） ===
PDF marker 全集 = **30**；SYS1 缺 = **2**

  章  PDF marker                                                       缺
  7  SU1.) SU1.1) SU2.) SU2.1) SU3.) SU4.) SU5.) SU6.) SU7.) SU8.)    2
     SU9.) SU9.1)
  8  SSND 1) SSND 2) SSND 2.1) SSND 2.2) SSND 2.3) SSND 3)            0
  9  PM1)                                                             0
 10  PITA4: PITA5: PITA6: PITA6.1: PITA8: PITA9: PITA10:              0
 11  VRLP1:                                                           0
 12  OFF1.) OFF2.) OFF3.)                                             0

缺漏清單：['SU9.)', 'SU9.1)']

  全集降為 30（期望 30）：True；`DS4.1)` 自全集消失：True
  **且缺漏數不變** —— 故若僅比對缺漏數，此錯不會被察覺；分母 30 vs 31 才是證據。
```

**此項之輸出即本輪最重要之一行**：移除 `DS` 後**缺漏數仍為 2**。
若當初只比對「缺漏數」，14 包之錯**永遠不會被察覺** ——
唯一之證據是分母由 31 降為 30。

**C —— 判定表缺一項時須攔下**（本層自加，非下放包所令）：

```
=== must-hit C —— 自判定表移除 `OFF` 之判定（模擬未判定之新前綴）===
  未判定清單 = ['OFF']；被攔下：True
```

**前綴全判定: True；範圍向 31／2: True；must-hit A: True；must-hit B: True；must-hit C: True**

### 2.5 `DS4.1)` 之登記

依 **R-PMH26**（只登記不開 DR），已於 `ANOMALIES.md` 立
**A-PMH15**，載其逐字原文、其與 `SU4.)` 之父子編號關係、
「極可能為規格原文筆誤」之判定，**及本 feature 一律照原文處理之處置**
（`marker_coverage.py` 保留 `DS4.1)`，不代為改寫為 `SU4.1)`）。

---

## 三、`COVERED` 之自動化（步驟 3，R-PMH58）

### 3.1 實作

`lint_batch.py` 之 `chk()` 增 `canon=` 具名參數；各檢查於**其呼叫處**
宣告所檢查之 canon 節號。`COVERED` 由 `_covered_from_source()` 以 `ast`
掃本檔自身之 `chk(...)` 呼叫彙集而得：

```python
COVERED = _covered_from_source()   # 掃 ast，取各 chk(..., canon=...) 之值
```

**宣告與檢查點自此為同一處，無從分岔** —— 這正是 14 包 §3.2 之錯
（宣告 `5.2` 而檢查未實作）在結構上不再可能發生之理由。

### 3.2 自動產生之集合與現行手寫之 10 節 —— **完全相同**

```
10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
```

**逐項差異：無。** 手寫版與自動版之集合相等。

**須說明者**：此「相同」是 14 包補完實作**之後**之狀態。
14 包當時之手寫版亦是這 10 節，**而 `5.2` 之檢查尚未存在** ——
即當時之自動版只會有 9 節。**故本次之「相同」不是自動化沒抓到東西，
是那個錯已於 14 包被修掉。** 自動化之價值在於**該類錯此後無從發生**，
不在於本次又抓到一個。

### 3.3 另設之執行期交叉核對（本層自加）

靜態彙集（`ast`）只證明「原始碼寫了」，不證明「該檢查點被執行到」。
故 `chk()` 於執行期另記 `executed`，`main()` 末尾比對二者：

```
（R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
```

**若某檢查落在條件分支內而該分支未被走到，此行即會具名之。**

---

## 四、priority 之矛盾處置（步驟 4，R-PMH59）

### 4.1 擇案：**（甲）—— `-003` 降 P1**

**理由**：分析層 §3.1 之矛盾指認成立。`-004` 已載明 Maserati 之正常設計
即為「無逾時、須按 Accept」且判該情形**可接受**（P1）；
則 `-003` 之逾時失效，其結果**恰等同 Maserati 之正常運作**，
「永遠停在免責畫面」不成立。二者不能並存，而**降 `-003` 者只需撤回一個
不成立之後果描述**，升 `-004` 者則須額外主張「Maserati 之正常設計本身
構成 P0 級風險」—— 後者於規格無據（規格明載其為設計意圖，非缺陷）。

### 4.2 **`-002` 之依據亦須改寫** —— 本層自查所得，非下放包所令

分析層 §3.3 判 `-002` 之 P0「依據成立」。**本層不同意，據實回報。**

`-002` 原依據為「Accept 為開機序列離開免責畫面之**唯一主動路徑**，
其失效即無法進入 last mode screen」。**該句於非 Maserati 不成立** ——
逾時路徑仍在（`-003` 所驗者），Accept 失效後車輛仍會自行離開免責畫面。
**這與 `-003` 原依據犯的是同一個錯：各自把對方的路徑當作不存在。**
只改 `-003` 而留 `-002`，批內仍有一條依據不成立之 P0。

**`-002` 之 P0 結論維持，其依據換為變體差異**：Accept **於 Maserati 為
唯一路徑**（`-004` 已載明 Maserati 不提供逾時），故其失效使 Maserati
車輛之開機序列無法完成。**級差之來源自此可一句說完**：

> Accept 之失效**有無替代路徑視變體而定**（Maserati 無）；
> 逾時之失效則**恆有 Accept 可替**。

三條之依據自此互不矛盾，且**不再依賴任何一條把另一條的路徑當作不存在**。

### 4.3 改寫後之 `reasoning` 全文

**`-002`（P0，維持）**：

> **P0 —— boot/recovery**：Accept 為離開免責畫面之主動路徑，且**於 Maserati 為唯一路徑** —— -004 已載明 Maserati 不提供逾時，故 Accept 失效使 Maserati 車輛之開機序列無法完成。⚠ R-PMH59：本條與 -003（逾時路徑，P1）之級差**來源在此** —— Accept 之失效有無替代路徑**視變體而定**（Maserati 無），逾時之失效則恆有 Accept 可替。前一輪之依據「唯一主動路徑，其失效即無法進入 last mode screen」**於非 Maserati 不成立**（逾時仍在），已改寫（15 包 §3.1）。依 profile §4「不同觸發即拆分」自 leaf 001-04 拆出 —— 「按 Accept」與「等待逾時」為兩個觸發（見 -003）。§4.3.1：test_item 上半為 source_clause 之逐字整句。§8.5：不設 Maserati 條件 —— Accept 按壓於 Maserati 亦成立（13 包 §4.8）。source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。

**`-003`（P0 → **P1**）**：

> **P1 —— 主要功能邏輯**（非 P0）：逾時為離開免責畫面之被動路徑；其失效使自動離開路徑失效，**惟 Accept 路徑仍在**（-002 已驗），**開機仍可完成**，故不落 boot/recovery 之射程。⚠ R-PMH59 —— 前一輪判 P0，其依據為「無人操作之車輛永遠停在免責畫面」，**該依據與 -004 相矛盾**：-004 已載明 Maserati 之正常設計即為無逾時、須按 Accept，且判該情形為可接受（P1）；則逾時失效之結果**恰等同 Maserati 之正常運作**，「永遠停住」不成立。採 15 包 §3.2 之案（甲）降 P1。同 leaf 之第二條（profile §4 之不同觸發，見 -002）。設計方法 STATE —— 標的為逾時所引發之狀態離開。⚠ §8.4.1 不造值：**規格未載逾時之秒數**，亦**未言逾時等同 Accept** —— 本條只斷言「畫面移除並顯示 last mode screen」，**不斷言其等同 Accept**（13 包 §4.4 之更正）。⚠ §8.5：pre-condition 之 non-Maserati **是必要的** —— 逾時本身即 Maserati 之差異點。步驟 2 之「不按任何硬鍵」係因 PDF SU9.1 載按 Power Off／Screen Off 會重設逾時，而該子句於 SYS1 缺失（A-PMH14），故自 PDF 取之。source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。

**`-004`（P1，一字未動）** —— 其原依據即為本次判斷之支點，無須改寫。

### 4.4 分布之變化

| | 14 包 | 本包 |
|---|---:|---:|
| P0 | 4 | **3** |
| P1 | 3 | **4** |
| P2 | 1 | 1 |

**本層對 14 包 §8 第 4 項自陳之回應**：分析層謂 `-006` 之 P2「動機雖可疑，
判斷不受污染」，本層接受該分析。**而本輪之結果本身即是該自陳之驗證** ——
真正受污染者確實是 `-003`，且它與 `-002` 是一對，兩條都受污染。
**「分布看起來合理」之壓力所產生的痕跡，出現在 P0 那一側，不在 P2 那一側。**

### 4.5 一致性自檢已落為程式之固定步驟

14 包所自加之「`pri` 欄 vs `reasoning` 首句級別」一致性複驗，
本輪寫入 `gen_batch01.py` 之 `self_check()`，於 `main()` 起首執行，
不一致即 `SystemExit`。must-hit 實跑：

```
must-hit（pri 改 P0 而 reasoning 稱 P1）: ['-003 pri=P0 而 reasoning 稱 P1']
復原後: 無不一致
```

---

## 五、`canon_coverage.py` 之非數字標題差集（步驟 5）

```
canon：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
節號全集 = **58**；lint 宣告涵蓋 = **10**；**未涵蓋 = 48**

=== 未涵蓋之 canon 節號（R-PMH56，程式產生）===
  §0        Purpose
  §1        Language
  §2        Core Principles
  §3        Workflow (Generate)
  §4        Field Rules
  §4.1      Framework Establishment (prerequisite for Test Set)
  §4.1.1    Three Layers
  §4.1.2    Establishment Workflow
  §4.1.3    Layer 2 Granularity — anti-patterns
  §4.1.4    Why Layer 3 matters (even though it's not in the workbook)
  §4.1.5    Workbook export
  §4.2      Test Set
  §4.3      Test Item / tc_title — three acceptable shapes
  §4.4      Pre-Condition
  §4.5      Input Test Data — field ownership
  §4.6      Sibling Awareness
  §5        Step Design
  §5.3      Standard Setup Snippets
  §5.4      Tooling / CLI Step Format
  §5.6      Baseline Comparison
  §5.7      One Objective
  §6        Expected Results
  §6.1      Multi-Phase ER Layout
  §7        False Pass / False Fail
  §8        Requirement Alignment
  §8.1      Test Item ↔ Requirement
  §8.2      RD Decomposition Discipline
  §8.2.1    Do not expand scope into sibling Reqs
  §8.2.2    Do not consolidate — RD sub-id ≠ TC count
  §8.3      Keyword Decomposition (sibling axes — each = 1 TC)
  §8.4      No Fabrication
  §8.4.1    No data fabrication
  §8.4.2    No scope fabrication
  §8.5      Pre-Condition Scope Drift
  §8.6      Spec Reference Hierarchy
  §8.7      Cross-Domain Behavioral Patterns
  §8.7.1    Spec-sourced thresholds
  §8.7.2    Disambiguate similar operations
  §8.7.3    Variant label overrides
  §8.7.4    Selectable-but-styled
  §8.7.5    訊號與參數寫法（R-1 v3）
  §9        Self-Check (before emitting each TC)
  §10       Tool-Specific Output Contract (workbook export, not ASPICE rules)
  §10.1     Required output keys (snake_case)
  §10.4     `reasoning` field (Traditional Chinese, 2–5 sentences)
  §10.6     `duplicate_of` encoding
  §12       Design Method (assign AFTER TC finalized, first-match)
  §13       Final Rule

=== 抽取判準之盲區：無數字編號之標題 = 1（15 包步驟 5）===
  下列標題不具數字節號，**自始不入節號全集**，故其未被 lint 檢查一事不會出現於上方清單。
  ##### 沿革（R-TM13：不刪除，加註保留）
  **只回報，不改判準** —— 是否納入母體屬判準之變更，須另立條文。
```

**本層對步驟 5 之一項擴充，須具名**：下放包令「列出 canon 中所有
`^#{2,4}` 標題」。**若反向檢查沿用與判準相同之層級範圍，則層級本身之盲區
（H1／H5+）仍照不到** —— 而該正是本步驟所欲防之形態。
故反向掃描之範圍取 `^#{1,6}`。實測：**H1 = 0；H5 = 1**
（`##### 沿革（R-TM13：不刪除，加註保留）`，屬條文沿革註記而非規則節）。

若沿用 `#{2,4}`，該行輸出會是「無數字編號之標題 = 0」——
**一個看起來完美而實際上沒看那一層的答案。**

**只回報，不改判準**：`HEAD` 之抽取範圍未動，節號全集仍為 58。

---

## 六、lint 全跑輸出（步驟 6 之機械可查部分）

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

**步驟 6 所令之「procedure 與 ER 之編號逐條對齊」已落為 lint 之第 30 項**
（`procedure／ER 編號自 1 起連號且逐位對齊`），**不宣告任何 canon 節號** ——
它是人讀之前置，非 canon 條文之實作，**不得使 `COVERED` 虛胖**。

**「一步一意圖」與「ER 是否真對應該步之意圖」不可機械判定**，
依下放包 §5 步驟 6 由分析層於下一輪人讀。

**must-hit 兩份 fixture 仍 FAIL（判準未鬆動之證據）**：

| fixture | 結果 |
|---|---|
| `tests/fixtures/batch01_prerework.json`（13 包） | **21/30 PASS，9 項 FAIL** |
| `tests/fixtures/batch01_r2.json`（14 包 §5.2） | **29/30 PASS，1 項 FAIL**（步驟字數） |

---

## 七、六支檢查之總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| `marker_coverage.py --self-test` | **PASS**（前綴全判定／31／2／must-hit A・B・C） |
| `canon_coverage.py` | **PASS** —— 58 節，涵蓋 10，未涵蓋 48；無數字編號標題 1 |
| `check_state_consistency.py` | **PASS** —— `framework.md`／`feature.yaml`／`PLAYBOOK.md` |
| `check_granularity.py --check-doc-sync` | **PASS** —— SHA256 `eada46d05ea268f0…`（命中 1 處）＋ 門檻表 7 列逐字相同 |
| `check_write_back.py --self-test` | **PASS** —— 四項，三項故意失敗全被攔下 |

---

## 八、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | 否 |
| 2 | 判準衝突未決 | 否 |
| 3 | 須寫回而工作簿狀態不明 | 否（本包零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論將建於臆測 | **是（既有）** —— DR-PMH1 阻斷**交付**，不阻斷本包 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | marker 全集 ≠ 31 或缺漏 ≠ 2 | 31／2 | **否** |
| 8 | must-hit（移除 `DS`）未 FAIL | 全集 31 → 30，`DS4.1)` 自全集消失，實跑具名 | **否** |
| 9 | 自動產生集合與手寫 10 節不同且差異未查明 | 兩者**完全相同**，差異為空集 | **否** |

**本包無新觸發之停止條件。**

---

## 九、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為（`SWE1-HMI-PM-028`／12.2） | `OPEN` | **阻斷交付** |
| DR-PMH2 | Power Moding State Matrix Excel（p9 矩陣於 SYS1 全缺） | `OPEN` | 否（阻斷 ch 9 判讀） |
| DR-PMH3 | `SU9.)`／`SU9.1)` 是否應在 037 | `OPEN` | 否，**惟若確認，`Disclaimer Screen` 由 7 leaf 增為 9，48 leaf 母體亦須重算** |

**三筆皆尚未發出。** 本包第三度重申：**不發則 48 leaf 之母體與
ch 9 之判讀背景無人在追。**

---

## 十、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，五項。**

1. **`VERDICT` 表本身仍是人工判定，只是它的「母體」不再是人工的。**
   反向掃描保證了**沒有候選被漏看**，但每一候選是 `req` 還是 `noise`
   仍由我判。若我把某個真需求前綴誤判為 `noise`，該章一樣靜默消失，
   **且 must-hit C 抓不到**（它只抓「未判定」，不抓「判錯」）。
   **此為 R-PMH57 之殘餘盲區，本包未解。**
   可行之下一步：對判為 `noise`／`xref` 者，檢查其鄰近文句是否具需求語氣
   （`shall`／`should`／祈使句），有者升為須人讀。

2. **候選形態 `CANDIDATE` 本身仍是一個正規式。** 它假設 marker 必為
   「字母 + 數字 + `.`／`)`／`:`」。**若規格用了 `[A-3]` 或 `Req 4.1 –` 之類
   形態，反向掃描一樣看不見。** 這與 14 包之錯是同一層級，只是往上退了一階。
   **反向掃描把「前提」從前綴清單移到了候選形態，並未消滅前提。**

3. **`sandbox/spec.txt` 與 PDF 之等同性未於本包重驗。** 全部 marker 量測
   都建在該文字檔上。分析層之字元數為 15,751，本層 `norm()` 後為 15,167 ——
   **差 584 字元**。該差極可能來自空白正規化，**但我沒有證明它是。**
   若二者非同一份萃取，31 這個數字之基礎即不穩。

4. **`-005`／`-006`／`-007` 三條之依據未依 R-PMH59 逐對複驗。**
   本包只處理了分析層指出的 `-003`／`-004`，並自查了 `-002`。
   **R-PMH59 要求的是「批內成對之 TC 逐對檢驗」，我只驗了 001–004 這一組。**
   `-005`（P1，能力存在）與 `-006`（P2，能力抑制）是明確的一對，
   分析層已覆核；**但 `-007`（P1）與 `-001`／`-008`（P0）之間有無同型矛盾，
   本包未查。**

5. **`ast` 靜態彙集之涵蓋範圍，只及於呼叫名為 `chk` 之直接呼叫。**
   若日後有人以別名或間接方式呼叫（`c = chk; c(...)`），
   `_covered_from_source()` 會漏掉它。**目前無此寫法，但該假設未被檢查。**

**另須明說者**：本包最大之收穫不是修好了 30 → 31，
而是 §2.4 must-hit B 之輸出證明了**「缺漏數不變」這件事本身**
——一個錯的分母可以完全不改變任何看起來重要的數字。
**14 包之六支檢查全綠、對照向相符，而分母是錯的。**
這對「全綠即可用」之推論是又一次否證（R-PMH52 之同一方向）。

---

## 十一、建議之 commit 與 pathspec（**不執行**）

14／15 兩包之異動合併為一次提交（14 之提交本即未執行）。

**訊息**：

```
feat(power_moding): packages 14-15 — marker prefix reverse scan, COVERED automation, priority contradiction fixed
```

**pathspec（14 路徑，R-G12 —— 逐一具名，不用 `git add .`／`-A`）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DECISIONS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/14_marker_enumeration.md \
  features/power_moding/docs/handoff/15_marker_prefix_and_priority.md \
  features/power_moding/docs/upstream/14_marker_enumeration.md \
  features/power_moding/docs/upstream/15_marker_prefix_and_priority.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/canon_coverage.py \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/lint_batch.py \
  features/power_moding/scripts/marker_coverage.py \
  features/power_moding/tests/fixtures/batch01_r2.json
```

（`docs/upstream/15_marker_prefix_and_priority.md` 即本檔。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py` | **未動** |
| `docs/runtime/` 下之檔案 | **未動**（`canon_coverage.py` 只讀 canon） |
| `PROFILE_INTEGRATION.md` | **未動**（明文不授權） |
| 工作簿寫回 | **無**（本包零寫回） |
| 已執行之 git 狀態變更指令 | **無** —— 本包未執行 `add`／`commit`／任何狀態變更 |
| 併行 session（`vehicle_setting`）之檔案 | **未動**；其暫存之檔案不在上列 pathspec 內 |

---

## 十二、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出**（DR-PMH1／2／3） | **DR-PMH1 阻斷交付** |
| 2 | 14／15 之 commit 授權（14 路徑，見 §11） | 否 |
| 3 | Q10、`PROFILE_INTEGRATION.md` | 否 |
| 4 | 第三輪 batch 1 之人讀覆核（分析層下一輪） | Phase 5 前 |
