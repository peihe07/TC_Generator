# 上繳包 27 —— 落選即判定、切分以謂詞為準與 Pre-Condition 之納入

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/27_verdict_for_every_cell.md](../handoff/27_verdict_for_every_cell.md)
- 前一包上繳：[26_enumeration_over_keywords.md](26_enumeration_over_keywords.md)
- **本包零寫回工作簿；未改任何 TC**

**26 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`f56f71b`，11 路徑）。

---

## ⚠ 本包之三項須先看

1. **切分改以謂詞為準後，查出一個「先前完全未被掃描」之 SUT 斷言** ——
   `-003` ER2 之 `the disclaimer screen times out`，
   **26 包以 ` and ` 為據時被綁在 `No user input is given`（測試執行斷言）上，
   整條不入母體。**（§3）
2. **Pre-Condition 之 24 個斷言全部入母體，牴觸 0** —— 停止條件 7 未觸發。（§4）
3. **偽陰自此可檢查**：`--cell-must-hit` 令 `audio` 之謂詞域失效 →
   稽核報出分類錯誤；改造前該類錯誤**不存在於輸出**。（§2）

---

## 一、§五三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH100 | 落選即判定，消滅「落選」類別；偽陰自此可檢查 | 526 | `5ca9d19aee81fa98` | `5ca9d19aee81fa98` | ✅ |
| R-PMH101 | 斷言之切分以謂詞為準，兩層作法 | 395 | `74ca235020e7ce60` | `74ca235020e7ce60` | ✅ |
| R-PMH102 | 掃描母體及於 `pre_conditions` | 437 | `979ad49681c50b00` | `979ad49681c50b00` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH97`／`R-PMH99` SHA256 皆相符。

---

## 二、落選併入判定表（步驟 2，R-PMH100）

### 2.1 四斷言之 174 格全部入表

| 斷言 | 記法分布 | 其中「入選而列層未具名 → 須人讀」 | 分類錯誤之稽核 |
|---|---|---:|---:|
| `popup` | 未對照 174 | **21** | 0 |
| `audio` | 未對照 165／**牴觸 9** | 0 | 0 |
| `announcement` | 未對照 174 | 0 | 0 |
| `popup_after` | 未對照 174 | **21** | 0 |

**「落選」類別已消滅** —— 關鍵詞自此只決定人讀之先後。

**⚠ 一項須明說**：`popup`／`popup_after` 之 21 格記 `未對照`，
**其為「尚未作成之預設」而非「已判定」** —— 該二斷言之**列層記法存於
`matrix_vs_chapter.VERDICT` 之章別判定**（ch7 之 `r48` 為牴觸），非本檔。
**輸出已逐次具名此點**，不使 174 個 `未對照` 看起來像「無問題」。

`audio` 之**牴觸 9** 即 `r45`（`Mute Button Pressed`）之九格
（24 包所查出、25 包已以第 5～7 項限定排除者）。

### 2.2 must-hit —— **偽陰自此可檢查**

```
=== R-PMH100 之 must-hit（27 包步驟 2）===
**改造前之偽陰不可檢查**（某格不存在於輸出）；**改造後可檢查**（某格分類錯誤而得 `未對照`）。

  基線（現況 174 格）之分類錯誤 = **0**

  (a) 令 `audio` 之謂詞域失效（模擬分類錯誤）→ 稽核報 **47** 格分類有誤：True
        r16c13(blk1) 域=['power'] :: Radio Wakes Up and mutes
        r40c2(blk37) 域=['display', 'power'] :: Power press OFF > Mute Active, Screen display is Off (Power Button OFF
        r40c3(blk37) 域=['display', 'power'] :: Power press OFF> Mute Active, Screen display is Off (Power Button OFF 

  (b) 注入一格 `Event ignored`（確無 audio 用詞）→ 稽核仍為 **0** 格：True

==============================================================
(a) 分類錯誤被攔下: True；(b) 無用詞者不誤報: True；現況分類錯誤: 0
```

**(a)** 令 `audio` 之謂詞域失效（模擬分類錯誤）→ 稽核由 0 增為 47 格，**攔下**；
**(b)** 注入一格 `Event ignored`（確無 audio 用詞）→ 稽核仍為 0，**不誤報**。

**停止條件 8 未觸發。**

**其意義**：改造前，某格因用詞未被想到而**不存在於輸出**，
**無從構造任何錨點**；改造後，其錯誤形態變為「分類錯誤」，**可構造錨點**。
**R-PMH98 之實質不是消滅列舉，是使列舉之錯誤變成可檢查的** —— 條文所言於此兌現。

### 2.3 `verdict_form.py` 之母體隨之由 176 增為 **964**

```
=== 對照結論之記法（R-PMH91）===
母體：各檢查之判定表，共 **967** 項

  batch_er_vs_matrix.ER_VERDICT                 26 項  {'未對照': 23, '—': 2, '印證': 1}
  chapter_bidirectional.RESIDUE_VERDICT         20 項  {'未對照': 11, '印證': 9}
  matrix_vs_chapter.VERDICT                    150 項  {'待定義': 4, '未對照': 138, '牴觸': 2, '印證': 6}
  spec_assertion_scan.AFTER_LINE_VERDICT        25 項  {'未對照': 23, '—': 2}
  spec_assertion_scan.ANN_LINE_VERDICT           2 項  {'—': 2}
  spec_assertion_scan.AUDIO_CELL_VERDICT        10 項  {'未對照': 9, '牴觸': 1}
  spec_assertion_scan.AUDIO_LINE_VERDICT        13 項  {'—': 1, '未對照': 12}
  spec_assertion_scan.LINE_VERDICT              25 項  {'印證': 5, '未對照': 18, '—': 2}
  spec_assertion_scan.cell_verdicts[announcement] 174 項  {'未對照': 174}
  spec_assertion_scan.cell_verdicts[audio]     174 項  {'未對照': 165, '牴觸': 9}
  spec_assertion_scan.cell_verdicts[popup]     174 項  {'未對照': 174}
  spec_assertion_scan.cell_verdicts[popup_after] 174 項  {'未對照': 174}

  合計：{'未對照': 921, '印證': 21, '待定義': 4, '牴觸': 12, '—': 9}；**未以四詞之一作結 = 0**
```

**未以四詞之一作結者 = 0。**

---

## 三、斷言切分之複核（步驟 3，R-PMH101）

機器以**五連接詞**（` and `／` with `／` while `／`;`／`, `）產生候選，
**人讀複核**寫入 `SPLIT_REVIEW` 常數（**非只在上繳包**）。

### 3.1 複核結果

| 項 | 數 |
|---|---:|
| 26 包以 ` and ` 為據（`-007` 除外） | **23** |
| 五連接詞之機器候選（`-007` 除外） | **26** |
| **人讀複核後之斷言數** | **26** |
| 差異 | **+3（+13%）** |

**13% < 50% → 停止條件 9 未觸發。**

### 3.2 複核之逐項

| 候選 | 判定 | 理由 |
|---|---|---|
| `-002` ER1.2 `the "Accept" button` | **接受**（規範化為 `the "Accept" button is shown on that screen`） | `with` 所連接者為名詞片語而非命題，**惟其確指一個可各自為真為假之命題** |
| `-003` ER1.2 | **接受**（同上） | 同上 |
| **`-003` ER2.2 `the disclaimer screen times out`** | **接受** | **本輪最重要之一項** —— 見 §3.3 |
| `-005` PC2.2 `the lower comfort screen` | **不接受** | 切分產生 `The vehicle is not equipped` ／ `the lower comfort screen`，**二者皆不完整**；原句為單一命題 |
| `-006` PC2.2 | **不接受** | 同上 |
| `-002`／`-003`／`-004` PC 之 `the "Accept" button shown` | **接受**（規範化） | 同 ER1.2 |

### 3.3 ⚠ **`-003` ER2.2 —— 一個先前完全未被掃描之 SUT 斷言**

原 ER2 逐字：`No user input is given while the disclaimer screen times out`

- 以 ` and ` 為據 → **1 個斷言**，其類為**測試執行**（`No user input is given`）
  → 依 R-PMH97 **不入掃描母體**；
- 以謂詞為準 → **2 個斷言**，後半 `the disclaimer screen times out`
  為 **SUT 行為斷言** → **入母體**。

**故該 SUT 斷言先前不是「掃了而未發現」，是「從未被掃」。**
本輪之判定：矩陣無 `timeout`（0 命中），其 `Timer` 8 處全為 `Radio Off Delay`
→ **未對照**。

**該案例即 R-PMH101 之立條依據之實地兌現** ——
**連接詞決定切分時，一個 SUT 斷言可以整個消失在一個測試執行斷言背後。**

---

## 四、Pre-Condition 之掃描（步驟 4，R-PMH102）—— **牴觸 0**

```
=== 結果 ===
  **`pre_conditions` 之斷言 24**（R-PMH102 新入母體）／**`expected_result` 之斷言 26**（`-007` 另計）
  二分（R-PMH97）：SUT **48**／測試執行 **2**
  記法：牴觸 **0**／印證 **1**／未對照 **47**／待定義 **0**
  未具名 **0**
```

### 4.1 二分與記法

| 項 | 數 |
|---|---:|
| **`pre_conditions` 之斷言（新入母體）** | **24** |
| `expected_result` 之斷言（`-007` 另計） | **26** |
| 合計 | **50** |
| 二分：SUT 行為／狀態斷言 | **48** |
| 二分：測試執行斷言 | **2** |
| 記法：牴觸 | **0** |
| 記法：印證 | 1 |
| 記法：未對照 | 47 |
| 未具名 | **0** |

**停止條件 7 未觸發**（其為「發現**任一**牴觸」，不限於新的）。

### 4.2 三個最接近之 PC 斷言（皆為 `-008`）

| PC | 共同名詞 | 判定 |
|---|---|---|
| `The radio is in Power Button Off state` | `Power Button OFF`（矩陣之**欄軸**） | 未對照 —— **軸為「在此條件下」之限定，不斷言 SUT 是否可處於該狀態** |
| `The ignition has gone from the OFF position to ACC or RUN` | `Key-on`／`Key-off` | 未對照 —— 矩陣之 `Key-on` 為**事件列**，斷言其後果而非該轉換可否發生 |
| `No phone call scenario is in progress` | `Call Active`／`Call Not Active`（**欄軸**） | 未對照 —— 同上；且其恰對應 `Call Not Active` 欄（23 §5.1 之印證即由此） |

**R-PMH102 所慮之情形（素材斷言「SUT 不可能處於該狀態」→ TC 不可執行）
實測不存在。**

---

## 五、R-PMH99(a) 之機器檢查（步驟 5）

lint 增第 32 項：**每一 procedure 步驟所含之限定項數 ≤ 2**。

```
=== R-PMH99(c) 之 must-hit（26 包步驟 6）===
**七項限定得合併於同一步驟，故『某項被忽略』與『某項被刪去』在文本上難以分辨** —— 本錨點即驗其可分辨。

  刪去 `press the ON/OFF key` → FAIL 被攔下：True
  刪去 `turn key-off` → FAIL 被攔下：True
  刪去 `open any door` → FAIL 被攔下：True
  刪去 `adjust HVAC hard controls` → FAIL 被攔下：True
  刪去 `press the Mute key` → FAIL 被攔下：True
  刪去 `the Headunit Mode key` → FAIL 被攔下：True
  刪去 `change the headunit mode by voice recognition` → FAIL 被攔下：True

  重複 `press the Mute key` → FAIL 被攔下：True
  一步含三項 → R-PMH99(a) FAIL 被攔下：True

============================================================
刪去 7/7 皆 FAIL: True；重複 FAIL: True；一步三項 FAIL: True
```

**三項錨點全過**：刪去 7/7 皆 FAIL／重複 FAIL／**一步含三項 FAIL**。

**26 §12 第 4 項自陳「2/2/2/1 是我自己數的」自此由機器判定。**

---

## 六、規格側之母體界定（步驟 6）—— **只量不判**

```
=== 規格側全枚舉之母體界定（R-PMH98，27 包步驟 6）===
**本輪只界定母體並量其行數，不做判定** —— 規模未知，先量再做。

  頁    總行    空行    頁碼    標點    敘述行  在範圍
  1    11     0     1     0     10  —（圖／封面）
  2     8     0     1     0      7  —（圖／封面）
  3    56     0     1     0     55  —（圖／封面）
  4    83     0     1     0     82  —（圖／封面）
  5    48     0     1     0     47  —（圖／封面）
  6    56     0     1     0     55  —（圖／封面）
  7    11     0     1     0     10  —（圖／封面）
  8    39     0     1     0     38  ✅
  9   115     0     1     0    114  ✅
 10    28     0     1     0     27  ✅
 11    57     0     1     0     56  ✅

  PDF 全文行數 = **512**
  **母體（p8–p11 之敘述行）= 235**
  排除規則（**逐行可查**）：['空行', '純頁碼', '純標點或單字元', '封面／文件資訊（p1）', '流程圖頁之標籤（p2–p7、p11）']

  ⚠ **`p1–p7` 與 `p11` 之圖標籤以頁次排除，非以字樣** ——
    其依據為 A-PMH04（2.1–6.1 為圖片佔位）與 12.4（`Please refer to the diagram`）。
    **p11 之 `OFF1.)`～`OFF3.)` 在 p11 而 p11 在範圍內** —— 故該頁未被整頁排除。

  **每一斷言 × 235 行**之人讀規模已知；其分兩層（謂詞層粗篩 ＋ 落選即判定）之作法同矩陣側（R-PMH100）。
```

**PDF 全文 512 行；母體（p8–p11 之敘述行）= 235 行。**

**排除規則逐項具名**：空行／純頁碼／純標點／封面（p1）／流程圖頁（p2–p7）。
**p11 未被整頁排除** —— 其含 `OFF1.)`～`OFF3.)`。

**每一斷言 × 235 行之規模已知**；其分兩層之作法同矩陣側（R-PMH100）。
**本輪未做判定**（下放包明令）。

---

## 七、矩陣側全枚舉之輸出（複跑）

```
--- 矩陣側之**全枚舉**（R-PMH98）—— 斷言 `audio` ---

  母體 = 事件列之**全部有值格 174**（非關鍵詞命中之子集）
  入選（謂詞域 `audio`，判準 `\b(mute[sd]?|unmute[sd]?|audio|sounds?|volume|background)\b`）= **48** 格，分布於 **10** 列
  落選 = **126** 格 —— **逐格具名其落選理由**：

     41 格  該格之謂詞域為 ['state']，與 `audio` 不交
     28 格  該格之謂詞域為 ['power']，與 `audio` 不交
     25 格  該格之謂詞域為 ['display', 'power']，與 `audio` 不交
     10 格  該格之謂詞域為 ['display']，與 `audio` 不交
      9 格  該格無任何謂詞域之詞
      8 格  該格之謂詞域為 ['display', 'power', 'state']，與 `audio` 不交
      4 格  該格之謂詞域為 ['display', 'state']，與 `audio` 不交
      1 格  該格之謂詞域為 ['power', 'state']，與 `audio` 不交

  **R-PMH100：174 格全部入判定表** —— 記法分布 {'未對照': 165, '牴觸': 9}
  **「落選」類別已消滅** —— 關鍵詞自此只決定人讀之先後。
  分類錯誤之稽核（`AUDIT_CORE`）：**0** 格

  === 與關鍵詞篩選之對照（26 包停止條件 8）===
    關鍵詞篩選得 **48** 格；全枚舉入選 **48** 格
    **其所在之列是否相同：True**
```

---

## 八、由程式產生之檢查總表（R-PMH92）

| 檢查 | must-hit | 退出碼 | 期望 | **結果** | 備註 |
|---|---|---:|---:|---|---|
| `lint_batch.py generated/batch01.json` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `lint_batch.py <fixture prerework>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py <fixture r2>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py --limit-must-hit` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `check_granularity.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --check-doc-sync` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --doc-sync-must-hit` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_write_back.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 三項故意失敗全被攔下 |
| `marker_coverage.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --verify-extraction` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --window-compare` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `canon_coverage.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其只做差集，無刻意構造之反例 |
| `check_state_consistency.py` | ✅ | 0 | 0 | **PASS** | `--self-test` 之故意注入 |
| `challenge_rulings.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其判準為標記列舉，R-PMH67 之抽樣非 must-hit |
| `tsv_vs_pdf.py --truncation` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 只做逐字比對之量測 |
| `chapter_bidirectional.py 7..12` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --partition` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --source-must-hit` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --export-residue` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `matrix_vs_chapter.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 8` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 11` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 12` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 7` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`r48` × `SU3.)`）→ 退出碼 1 為設計 |
| `matrix_vs_chapter.py 10` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`10.3` × `r48c10`，已登記 R-PMH80）→ 退出碼 1 為設計 |
| `spec_assertion_scan.py --assertion popup` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --assertion audio` | ✅ | 1 | 1 | **PASS** | **查出牴觸 1**（`r45` × `-007` ER4(b)，24 包）—— **25 包已以第 5～7 項限定排除之，其牴觸記錄保留** |
| `spec_assertion_scan.py --assertion announcement` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --assertion popup_after` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --cell-must-hit` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --spec-population` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `batch_er_vs_matrix.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入 |
| `verdict_form.py` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |
| `verdict_form.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |

**未註冊 must-hit 而標「未實測」者 = 4**  ← R-PMH92：其不得標 PASS

> 本表由 `python scripts/check_table.py` 產生。**手寫之結果欄不予採認**（R-PMH92）。

**「未實測」由 8 降為 4** —— `spec_assertion_scan` 已註冊 must-hit
（`--cell-must-hit`），其四個模式自此標 PASS。
**餘四支**（`canon_coverage`／`challenge_rulings`／`tsv_vs_pdf`／
`batch_er_vs_matrix`）仍無 must-hit。

---

## 九、lint 全跑輸出

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
  R-PMH99(c) `-007` 之七項限定字串各出現一次                           PASS
  R-PMH99(a) `-007` 每步之限定項數 <= 2                           PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

32/32 PASS

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

---

## 十、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— `DR-PMH5`／`DR-PMH7` |
| 2 | 判準衝突未決 | **是** —— `10.3` × `r48c10`（已登記，`DR-PMH6`） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | Pre-Condition 掃描發現**任一**牴觸 | 24 個 PC 斷言，牴觸 **0** | **否** |
| 8 | 步驟 2 之 must-hit（含 `mute` 而分為 `state`）未 FAIL | 令謂詞域失效 → 稽核報 47 格，**攔下** | **否** |
| 9 | 複核後斷言數與 23 相差逾 50% | 26 vs 23，**+13%** | **否** |

---

## 十一、未結 DR 清單（R-PMH82）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | p9 矩陣之來源 | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義 ＋ `Else: Mute Active` ＋ `Note:` 之範圍（三問） | **`DRAFT`** | **（待填）** | 矩陣對照之四列 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第六次空著。**

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **`popup`／`popup_after` 之 21 格記 `未對照` 而其實是「尚未判定」。**
   我在輸出裡具名了，**但 `verdict_form.py` 之 964 項統計把它們算成
   已作結之 `未對照`** —— **一個「待判定」被計入了「已判定」之總數。**

2. **切分之連接詞清單仍是列舉**（五個）。
   **以無連接詞之並置表達之複合命題不會被切開** ——
   如 `The controls displayed on the disclaimer screen are recorded`
   其實含「控制項有顯示」與「已記錄」兩層，**我判為 1 個**。

3. **`SPLIT_REVIEW` 之八項複核是我做的，沒有第二個來源。**
   R-PMH101(b) 令「人讀複核」，**而我既是產生候選之人也是複核之人。**

4. **PC 之 24 個斷言全判 `未對照`，其中 21 個之依據是同一句
   「矩陣無 `disclaimer`／`Accept`／`Maserati`／`comfort`／`timeout`」。**
   **那組零命中探針是我列的**（與 26 §12 第 1 項同一問題）——
   **PC 側之全枚舉尚未做**，只做了關鍵詞式之否定。

5. **規格側之全枚舉只量了母體（235 行），未做判定。**
   **故 R-PMH98 於規格側仍為 0%。**

6. **`test_procedure` 依 R-PMH97 全數歸為測試執行斷言而不入母體 ——
   該歸類我未逐條驗證。** `-007` 之步驟 5 `Deliver a traffic announcement…`
   其主語為測試員，**但其隱含「SUT 能接收該報導」之前提**；
   **該前提是否為 SUT 斷言，我沒有逐條看。**

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 27 — verdict for every cell, predicate-based splitting, pre-condition scan
```

**pathspec（8 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/27_verdict_for_every_cell.md \
  features/power_moding/docs/upstream/27_verdict_for_every_cell.md \
  features/power_moding/scripts/batch_er_vs_matrix.py \
  features/power_moding/scripts/check_table.py \
  features/power_moding/scripts/lint_batch.py \
  features/power_moding/scripts/spec_assertion_scan.py \
  features/power_moding/scripts/verdict_form.py
```

（實為 **9 路徑**。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json`／`ANOMALIES.md`／`DATA_REQUESTS.md` | **未動** —— 本包未改 TC、未新增 anomaly、未動 DR |
| State Matrix xlsx／規格 PDF | **只讀** |
| 暫存檔 | `tests/fixtures/_limit_must_hit.json` 於 must-hit 中建立後**即刪**（`finally` 保證） |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT` |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session | **未動** —— 惟本輪期間 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 被他 session 修改（節號全集仍 58，`canon_coverage.py` 仍 PASS）；**本層未觸碰該檔** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出 ＋ 日期與對象**（`DR-PMH7` 含三問） | `DR-PMH5` 阻斷 ch 9 |
| 2 | **§12 第 1 項** —— 21 個「待判定」被計入「已判定」之總數 | 否 |
| 3 | §12 第 4 項 —— PC 側之全枚舉未做，只做了關鍵詞式之否定 | batch 1 之寫回 |
| 4 | §12 第 6 項 —— `test_procedure` 之歸類未逐條驗證 | 否 |
| 5 | 規格側之全枚舉（母體 235 行已量） | Phase 5 |
| 6 | 章 9 × 矩陣（待 `DR-PMH5`）；9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |
