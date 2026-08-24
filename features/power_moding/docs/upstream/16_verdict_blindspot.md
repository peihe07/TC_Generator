# 上繳包 16 —— `-002` 判錯之採認、萃取等同性判準與 VERDICT 之殘餘盲區

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/16_verdict_blindspot.md](../handoff/16_verdict_blindspot.md)
- 前一包上繳：[15_marker_prefix_and_priority.md](15_marker_prefix_and_priority.md)
- **本包零寫回工作簿**

**⚠ 下放包 §八／§十之前提須更正**：其記「14／15／16 三包之提交**未授權**」。
**14／15 兩包已於 2026-08-24 經 Pei 授權並提交**（`99b4269`，14 路徑，
14 files changed，2522 insertions）。**本包只餘 16 之提交待授權。**

---

## 一、§六三條之抄錄核對表（步驟 1）

抄錄後**自 `RULINGS.md` 回讀**重新抽出，與 handoff 側逐位比對（R-PMH41）。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH60 | 兩份萃取之等同性以 marker 集合驗，不以字元數 | 370 | `903b6b94a57e7b4d` | `903b6b94a57e7b4d` | ✅ 逐字相符 |
| R-PMH61 | `VERDICT` 誤判之偵測（需求語氣 ＋ 其 must-hit） | 357 | `6e47d9e94b073bd1` | `6e47d9e94b073bd1` | ✅ 逐字相符 |
| R-PMH62 | 自訂判準須雙向自套 | 310 | `e52b305c6074138b` | `e52b305c6074138b` | ✅ 逐字相符 |

**命中數**：handoff 側抽出 3 塊、RULINGS 側回讀 3 塊，`a == b` 皆 `True`。

**既有條文 SHA256 未動**：`R-PMH10` `885070968235b262`／
`R-PMH57` `24d7227229777e17`／`R-PMH59` `a95567765836a477`，三者皆相符。

---

## 二、R-PMH61 之實作與 13 個前綴之語氣檢查（步驟 2）

### 2.1 實作

`marker_coverage.py` 增 `tone_scan()`／`print_tone_report()`：
對判為 `noise`／`xref` 之前綴，取每一出現位置**其後** 180 字元
（需求 marker 之作用是**引領**其需求文句，故證據在其後而非其前），
以兩組判準檢之：

- **情態動詞**：`shall`／`should`／`must`／`will`／`needs? to`／`is required to`
- **祈使句起首**：容許一個 `If …,` 前置子句後，以原形動詞起首
  （`do not`／`show`／`display`／`jump`／`set`／…）

命中者**升為「須人讀確認」並具名**，**不自行改判**。

### 2.2 13 個前綴之逐一結果

```
=== 非需求前綴之需求語氣檢查（R-PMH61）===
受檢前綴 = 13 個（判為 `noise`／`xref` 者）

前綴         判定       語氣命中  證據
CFTS       xref        0  —
CR         xref        1  CR19385) → 情態動詞 `will`
CTS        xref        1  CTS009) → 情態動詞 `shall`
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

**須人讀確認之前綴**：['CR', 'CTS', 'DCR']
  （只具名，**不自行改判** —— 判定值之變更須另有依據）
```

**三個 `xref` 被旗標，`noise` 九個全數 0 命中。** 此分離本身是結果：

- `CR`／`CTS`／`DCR` 為**變更單號附於需求句首尾**，其後即為需求文句，
  故必然命中 —— **這是本檢查之已知偽陽形態，不是判定有誤**；
- 九個 `noise`（`High`／`Low`／`a`／`and`／`sec`／`the`／`to`／`of`／`expires`）
  **零命中**，即真正的文句偽命中不會被本檢查旗標。

**須據實說明其限度**：本檢查對「附於需求句旁之編號」無鑑別力。
若某日有一個真需求前綴恰好也總是出現在需求句尾（而非句首），
其語氣證據會落在**它之前**而非之後，**本檢查看不見**。
窗口取「其後」是刻意選擇（配合 marker 引領文句之性質），**其代價即在此**。

### 2.3 must-hit D（本條之驗收）

```
=== must-hit D —— 將 `SU` 之判定由 `req` 改為 `noise`（測試替身）===
  其鄰近文句必含需求語氣，**故須被升為須人讀並攔下**；
  攔不下者，本檢查對真正之誤判亦無效（R-PMH61）。

=== 非需求前綴之需求語氣檢查（R-PMH61）===
受檢前綴 = 14 個（判為 `noise`／`xref` 者）

前綴         判定       語氣命中  證據
CFTS       xref        0  —
CR         xref        1  CR19385) → 情態動詞 `will`
CTS        xref        1  CTS009) → 情態動詞 `shall`
DCR        xref        3  DCR20015) → 情態動詞 `will`；DCR19385) → 情態動詞 `shall`
High       noise       0  —
Low        noise       0  —
SU         noise      11  SU1.) → 情態動詞 `will`；SU2.) → 情態動詞 `will`
a          noise       0  —
and        noise       0  —
expires    noise       0  —
of         noise       0  —
sec        noise       0  —
the        noise       0  —
to         noise       0  —

**須人讀確認之前綴**：['CR', 'CTS', 'DCR', 'SU']
  （只具名，**不自行改判** —— 判定值之變更須另有依據）

  `SU` 被升為須人讀：True
```

**`SU` 之判定改為 `noise` 後被升為須人讀** —— 本檢查對真正之誤判有效。
（`SU` 13 個出現中 11 個命中語氣；兩個未命中者不影響旗標。）

**前綴全判定: True；範圍向 31／2: True；must-hit A: True；must-hit B: True；must-hit C: True；must-hit D: True**

---

## 三、`-007` 之 `reasoning` 補寫（步驟 3）

**級別不變（P1），只補級差來源。** 全文：

> **P1 —— 主要功能邏輯**（非 P0）：pop-up 抑制影響免責畫面之可讀性，而免責畫面為 legal 要求（`as defined by legal/CFTS009`）——**惟其失效不阻斷開機**，故不落 boot/recovery。依 profile §4／canon §5.7「同一觸發之多個必然後果不拆」 —— 「不顯示 pop-up」與「音訊照常播放」為同一觸發之兩個必然後果，寫為同條之多行 ER。⚠ R-PMH59 —— 本條與 -008（P0）之**級差來源**：**遮蔽 ≠ 未顯示**。-008 之失效使免責畫面**根本未出現**，系統以**未取得使用者確認**之狀態進入 last mode；本條之失效使 pop-up **疊在**免責畫面上，**畫面仍在、Accept 仍可按、確認仍可取得**。對 -001（P0）亦然：-001 之失效使 Accept 按鈕**永不出現**，主動路徑消失；本條之失效不影響任一離開路徑（16 包 §三）。§4.3.1：test_item 上半為 source_clause 之逐字整段。source_clause 取自 PDF p8 之 SU3.)（R-PMH50）。

**分析層 §三之逐對複驗（`-007` vs `-008`／`-001`）本層覆核後同意**，
其判定與本層 15 §10 第 4 項所列之未驗項一致，本包據以補寫。

---

## 四、R-PMH60 之落實（步驟 4）

### 4.1 `--verify-extraction` 之輸出

第二份獨立萃取以 **PyMuPDF 1.28.0**（與分析層同族工具）自
`inputs/…DCR22412 (January 24 2023).pdf` 產出，
落 `sandbox/spec_pymupdf.txt`（11 頁）。

```

=== 兩份萃取之等同性（R-PMH60）===
  A：`sandbox/spec.txt`
  B：`/Users/peihe/Work_Projects/TC_Generator/features/power_moding/sandbox/spec_pymupdf.txt`

  marker 全集：A = **31**；B = **31**
    章  7：A = 13；B = 13
    章  8：A =  6；B =  6
    章  9：A =  1；B =  1
    章 10：A =  7；B =  7
    章 11：A =  1；B =  1
    章 12：A =  3；B =  3

  **逐項相等 —— 等同性成立**（二者為同一份規格之同一版本）

  （字元數 A = 15171／B = 15420，差 249 —— **依 R-PMH21／R-PMH60 不作為判準**，列出僅為記錄）
```

### 4.2 **本步驟查出一項下放包未預期者：候選集合本身是萃取相依的**

首次比對時，B 側（PyMuPDF）出現**兩個 A 側沒有的候選前綴**：
`Loading` 與 `each` —— 二者皆為 **p9 流程圖之標籤**，
兩種萃取器之閱讀順序不同，致圖上相鄰之獨立標籤被併成不同字串
（`System Loading` ＋ `1.5 sec timeout` → 候選 `Loading 1.`；
`…with a 1.5 timeout each` ＋ `1.5 sec timeout` → 候選 `each 1.`）。

**其意義**：R-PMH57 之反向掃描保證「該萃取內沒有候選被漏看」，
**但候選集合本身隨萃取器而變**。若當初只用 PyMuPDF，`VERDICT` 表會
多兩列；只用 `pdftotext`，就少兩列。**兩者皆非錯，但「候選集合」不是
文件之固有屬性。**

二者已判為 `noise` 並具名入表（其依據載明其為萃取相依之產物）。
判定後 `--verify-extraction` 退出碼 0。

**這是同一形態往上退的第三階**：
14 包之前提是「前綴清單」→ 15 包移到「候選形態」→ 16 包移到「萃取器」。
**每一階都消滅了下一階的錯，也都留下自己這一階的前提。**

### 4.3 `DECISIONS.md` 之萃取來源記載

已增兩列（§7 Execution）：

- **規格 PDF 之文字萃取來源** —— `spec.txt` 由 `pdftotext -layout` 產出；
  `spec_pymupdf.txt` 由 PyMuPDF 1.28.0 產出；等同性以 marker 集合驗，
  全集皆 31、逐章 13／6／1／7／1／3 全同、缺漏皆 `SU9.)`／`SU9.1)`；
  附可重跑之指令。
- **⚠ 字元數不得作為等同性之依據** —— 明載 15,171／15,420／15,751 三數
  **不予採認為疑點**，並指出 R-PMH21 已明文排除該量。

**`sandbox/` 在 `.gitignore` 內**（`git check-ignore` 實測命中
`features/power_moding/.gitignore:24`），故兩份萃取皆不入版控；
PDF 本體之 SHA256 在 `inputs/MANIFEST.sha256`，可據以重製。

### 4.4 以字元數為據之陳述之處置

上繳 15 §10 第 3 項**原文一字未改**（R-PMH44），另於該檔末附
**勘誤 1**，載明：

- 以字元數提出該疑慮與以字元數消解它**同屬判準之誤用**（R-PMH21）；
- **該工具差異早於 03 包上繳 §6.2 即已記載**
  （`pymupdf` 15,618 vs `pdftotext -layout` 15,167，明載為
  「不同工具之差異，非衝突」）—— **15 包是未回查既有記載**；
- 正確判準之實測結果，**§10 第 3 項自此結清**。

---

## 五、步驟 5 —— 判準單向套用之清單（**只列不改**）

依 R-PMH62 回溯自套。**查得四項，其中一項為真正之未套用。**

### 5.1 R-PMH51（雙向比對）—— **部分未套用，且其記載自相矛盾**

R-PMH51 明文：A-PMH03 之其餘三則（8、9.1、11.1）**須以雙向法複驗；
未複驗前其標題結論不得引用**。

| 則 | 雙向複驗 | 現況 |
|---|---|---|
| 11.1 | **已做** | A-PMH14 明載「p10 之 VRLP1 四個 outcome —— **非漏**，SYS1 之 11.1 有之」 |
| 9.1 | **已做，且查出新漏** | **新漏 2 —— p9 狀態矩陣全缺，而 p9 對應之 outline 正是 9.1** |
| **8** | **未做** | 12 包記「原記之其餘三則…**不變**」，13 包方向二未在 p8 之該標題上具名任何結論 |

**且 9.1 之記載自相矛盾**：A-PMH14 之結語列「9.1／11.1 —— 條列再流，
**維持**（本輪方向二未在其上查出新漏）」，
**而同一份 A-PMH14 之新漏 2 查出的正是 9.1 之狀態矩陣全缺。**
「維持」與「新漏 2」指向同一個 outline。

**成因即 R-PMH62 所述**：12 包用新判準（雙向）推翻了 7.1，
**卻在同一段寫下「其餘三則不變」而未對它們套用同一判準**；
13 包補做了方向二，**但其結語沿用了 12 包那句「維持」**。

### 5.2 R-PMH41（驗命中數／驗所欲狀態）—— **已回頭套用**

08a 步驟 8 之替換靜默未命中一案，其**同批之其餘替換**已於
10 包「替換殘留回掃」逐項複驗（`docs/INDEX.md` 第 10 列）。
**本項無未套用之一側。**

### 5.3 R-PMH52／R-PMH56（須具名未涵蓋者）—— **只套用於 lint 一支**

R-PMH52 要求「任何 lint 之輸出須具名其未涵蓋之 canon 節號」，
R-PMH56 要求該清單由程式產生。**二者實際只施行於 `lint_batch.py`。**

其餘四支檢查**皆未具名其未涵蓋之範圍**：

| 檢查 | 未具名之涵蓋限度 |
|---|---|
| `check_granularity.py` | G1–G5 五項之外，granularity 尚有哪些面向未被檢查，未具名 |
| `check_write_back.py` | 四項之外未具名；且其**接線狀態**（`wired: false`）雖已於 `DECISIONS.md` 揭露，該檔輸出本身不提 |
| `check_state_consistency.py` | `EXCLUDED` 三檔**有**具名（唯一有做的一支） |
| `marker_coverage.py` | 本包已補（§2.2 之限度、§4.2 之萃取相依），**但非以程式輸出之形式** |

**判定**：R-PMH52 之條文措詞為「任何 lint」，範圍即不限於 `lint_batch.py`。
**此為單向套用。**

### 5.4 R-PMH59（priority 依據互不矛盾）—— **已於 15 包補足**

分析層單向套用（驗 `-003` 未驗 `-002`），由本層於 15 §4.2 查出；
`-005`／`-006`／`-007` 之逐對複驗由分析層於 16 §三補做。
**本項已結清**，且它正是 R-PMH62 之立條依據。

---

## 六、lint 全跑輸出（步驟 6）

**本輪未動 `generated/batch01.json` 之 procedure／ER 文字**，
只改 `-007` 之 `reasoning`（步驟 3）。

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

**must-hit 兩份 fixture 仍 FAIL**：
`batch01_prerework.json` 21/30（9 FAIL）／`batch01_r2.json` 29/30（1 FAIL）。

---

## 七、六支檢查之總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| `marker_coverage.py --self-test` | **PASS** —— 前綴全判定／31／2／must-hit **A・B・C・D** |
| `marker_coverage.py --verify-extraction` | **PASS** —— 兩份萃取 marker 集合逐項相等 |
| `canon_coverage.py` | **PASS** —— 58 節／涵蓋 10／未涵蓋 48 |
| `check_state_consistency.py` | **PASS** |
| `check_granularity.py --check-doc-sync` | **PASS** |
| `check_write_back.py --self-test` | **PASS** |

---

## 八、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | 否 |
| 2 | 判準衝突未決 | 否 |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是（既有）** —— DR-PMH1 阻斷交付 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 步驟 2 之 must-hit（`SU` 改判 `noise`）未攔下 | 攔下（`SU` 升為須人讀，11 處語氣命中） | **否** |
| 8 | 步驟 4 之兩份萃取 marker 集合不相等 | 逐項相等（31 = 31，逐章全同） | **否** |
| 9 | 步驟 5 發現任一判準曾被單向套用**且其未套用之一側已產出對外交付內容** | 見下 | **否** |

**條件 9 之逐項判定**：

| 未套用之一側 | 是否已產出對外交付內容 |
|---|---|
| A-PMH03 之 outline `8`（拼字歸因未經雙向複驗） | **否** —— batch 1 只涵蓋 outline 7.1／7.2／7.3／7.4／10.4；工作簿 `workbook_state = BLANK`，**至今零寫回** |
| A-PMH03 之 outline `9.1`（記載矛盾） | **否** —— 同上，且 9.1 引 5 leaf 皆不在 batch 1 |
| R-PMH52 未及之四支檢查 | **否** —— 該四支之輸出只供本流程內部判斷，未進任何交付件 |

**故條件 9 未觸發 —— 惟其未觸發之唯一理由是「還沒交付」。**
一旦 batch 涵蓋 9.x／11.x，或工作簿開始寫回，該三項即同時變成阻斷項。
**本層建議將 §5.1、§5.3 排入 Phase 5 之前。**

---

## 九、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為（`SWE1-HMI-PM-028`／12.2） | `OPEN` | **阻斷交付** |
| DR-PMH2 | Power Moding State Matrix Excel（p9 矩陣於 SYS1 全缺） | `OPEN` | 否（阻斷 ch 9 判讀） |
| DR-PMH3 | `SU9.)`／`SU9.1)` 是否應在 037 | `OPEN` | 否（若確認，7 leaf → 9，48 母體須重算） |

**三筆皆尚未發出。第四度重申。**

**且本包新增一項與 DR-PMH2 直接相關之證據**：§5.1 查出 A-PMH14 對
outline 9.1 之記載自相矛盾 —— 結語稱「條列再流，維持」，
而其新漏 2 查出的正是 9.1 之狀態矩陣全缺。**DR-PMH2 所索取者即該矩陣。**

---

## 十、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，四項。**

1. **語氣檢查之窗口方向是一個未經檢驗之假設。**
   §2.2 已具名其限度（取「其後」使句尾型 marker 之證據落在窗外），
   **但我沒有檢驗這份規格裡有沒有句尾型 marker。**
   若有，本檢查對它就是無效的，而 must-hit D 用的是 `SU`（句首型），
   **驗不到這一面**。可行之下一步：加一個取「其前」之對照窗口，
   比較兩者之旗標集合是否相同。

2. **`--verify-extraction` 只跑過一組（`pdftotext` vs PyMuPDF）。**
   R-PMH60 之條文說的是「不同工具、不同正規化策略」之兩份萃取，
   **而這兩份共用同一份 PDF 檔**。若 PDF 本身被換過（同名不同版），
   兩份萃取會一致地錯。`inputs/MANIFEST.sha256` 有 PDF 之雜湊，
   **但本包未跑 `shasum -c` 複驗它。**

3. **§5.1 所查出之 A-PMH14 記載矛盾，本包只列不改（依步驟 5 之令）** ——
   **而它是一個現存於檔案中之錯誤陳述，不是一個待辦事項。**
   `ANOMALIES.md` 現在同時寫著「9.1 條列再流維持」與「9.1 之狀態矩陣全缺」。
   **只列不改使該矛盾繼續留在檔案裡**，任何人下次讀 A-PMH14 之結語
   都會讀到那句「維持」。我依令未改，**但據實記明我認為它該改。**

4. **R-PMH62 之回溯只查了下放包點名之三條（R-PMH41／51／59）＋ 我自查之
   R-PMH52。** `RULINGS.md` 現有 62 條，**其中由分析層提出以質疑某項結論者
   遠不止四條**（如 R-PMH25／R-PMH40／R-PMH45／R-PMH53）。
   **我沒有做全量掃描，也沒有一個可以自動判定「哪些條文屬於質疑型」之判準。**
   本包所交之清單，其完整性我無法主張。

---

## 十一、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 16 — verdict misjudgement detection, extraction equivalence by marker set
```

**pathspec（8 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/DECISIONS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/16_verdict_blindspot.md \
  features/power_moding/docs/upstream/15_marker_prefix_and_priority.md \
  features/power_moding/docs/upstream/16_verdict_blindspot.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/marker_coverage.py
```

（實為 9 路徑；`docs/upstream/15_*.md` 之異動為本包所附之**勘誤節**，
其 §10 原文一字未改。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py` | **未動** |
| `docs/runtime/` 下之檔案 | **未動** |
| `PROFILE_INTEGRATION.md` | **未動** |
| 工作簿寫回 | **無** |
| 已執行之 git 狀態變更指令 | **無**（14／15 之提交 `99b4269` 為上一輪經授權執行者） |
| 新增之未入版控檔案 | `sandbox/spec_pymupdf.txt`（`.gitignore` 內，刻意不入版控） |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十二、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出**（DR-PMH1／2／3）—— **第四度重申** | **DR-PMH1 阻斷交付** |
| 2 | 16 之 commit 授權（9 路徑，見 §11） | 否 |
| 3 | §8 條件 9 之三項（A-PMH03 之 `8`／`9.1` 記載、R-PMH52 未及之四支檢查）是否排入 Phase 5 前 | Phase 5 |
| 4 | Q10、`PROFILE_INTEGRATION.md` | 否 |
