# 上繳包 08 —— granularity 判準之補正、分母口徑與盲區補查

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/08_criterion_repair.md`
- **併讀之補篇**：`08a_q11_and_git.md`（R-PMH36／R-PMH37）—— 不另佔往返編號，
  其上繳併入本檔 §11
- 前一包：[upstream/07_gap_widening.md](07_gap_widening.md)
- 執行狀態：**步驟 1–6 全部執行完畢；08a 增列之步驟 7、8 見 §11。
  九條停止條件全未觸發。**
  **零寫回工作簿**；改狀態 git 零次；**未修改任何他 feature 之檔案**。

---

## 0. ⚠ 先更正一項事實 —— 08 §5.1 已過時

08 §5.1 逐字：「**06 與 07 兩包之工作區異動至今未提交。**」

**該陳述於本包執行時已不成立** —— Pei 已於 08 落檔前指示提交，
兩包合併提交為 **`a345ca8`**
（`feat(power_moding): packages 06-07 — layer 2 verified, granularity pass, CFTS009 gap widened`，
8 檔 +1749/−14，帶 pathspec）。

`framework.md` 已入版控。**§5.1 所列之六個未提交檔案現皆已提交。**
（此為分析層撰包時點早於提交所致，非任何一方有誤。）

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH34 | 涵蓋率陳述之分母 | 332 | `3e895648a1294f2c` | `3e895648a1294f2c` | 逐字相符 |
| R-PMH35 | 判準須有可執行門檻 ＋ must-hit 錨點實跑 | 458 | `369e0e4c5849ccf2` | `369e0e4c5849ccf2` | 逐字相符 |

---

## 2. 步驟 2 —— `check_granularity.py` 與其自測

**程式路徑**：`features/power_moding/scripts/check_granularity.py`
（本 feature 專屬；未改任何共用腳本）。**門檻寫死於程式**，可重跑。

**自測**：`python scripts/check_granularity.py --feature . --self-test` → **exit 0**

### 2.1 五個 must-hit 錨點之實跑 —— **指定判準全部如期 FAIL**

```
--- A1 每個 outline 各成一組（29 組） ---
    G1 **FAIL**  組數/leaf = 29/48 = 0.6042 (門檻 <= 0.35)  ← 指定 FAIL ✅
    G2 **FAIL**  min(組規模) = 1 (門檻 >= 2)  ← 連帶 FAIL（不影響本錨點之成立）
    G3 PASS      收容簇命中 = 無
    G4 PASS      max/leaf = 5/48 = 0.1042
    G5 **FAIL**  逸出 [2, 24] 之組規模 = [1 ×21] (實測區間 [1, 5])  ← 連帶 FAIL
    隔離度：連帶 ['G2', 'G5'] —— **構造本質使然**：29 個 outline 分 48 leaf，
            必有單 leaf 組，故 G2／G5 必然一併 FAIL —— 無法隔離

--- A2 每個 leaf 各成一組（48 組） ---
    G1 **FAIL**  1.0000 > 0.35   ← 指定 FAIL ✅
    G2 **FAIL**  min = 1 < 2     ← 指定 FAIL ✅
    G5 **FAIL**  全部逸出         ← 連帶 FAIL
    隔離度：連帶 ['G5'] —— **構造本質使然**：全部組規模為 1，必然一併 FAIL

--- A3 Off Road Plus 拆為三個單 leaf 組（10 組） ---
    G2 **FAIL**  min = 1 < 2              ← 指定 FAIL ✅
    G5 **FAIL**  逸出 [2,24] = [1, 1, 1]  ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

--- A4 新增一組名為 Misc（2 leaf，以隔離 G3）（9 組） ---
    G3 **FAIL**  收容簇命中 = ['Misc']    ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

--- A5 八組併為一組（1 組） ---
    G4 **FAIL**  48/48 = 1.0000 > 0.5     ← 指定 FAIL ✅
    G5 **FAIL**  逸出 [2,24] = [48]       ← 指定 FAIL ✅
    隔離度：**隔離**（僅指定判準 FAIL）

must-hit 五錨點全部如期 FAIL: True；範圍向 PASS: True
```

**停止條件 7 未觸發。**

### 2.2 執行時所作之兩處修正（須回報）

| # | 下放包 §2.2 之內容 | 執行層之修正 | 理由 |
|---|---|---|---|
| 1 | A3 之「應 FAIL 之判準」列 **G2、G5** | 首版程式只寫 `{"G2"}` —— **執行層漏抄**，已補回 G5 | 下放包原文即列二者 |
| 2 | A4 未指定 `Misc` 之**規模** | 首版取 **1 leaf** → 連帶觸發 G2／G5；改為取 **2 leaf** | 取 1 使該錨點無法**單獨**證明 G3；取 2 即隔離 |

### 2.3 **連帶 FAIL 之處理 —— 一項方法上之決定，須追認**

首版之判定規則為「指定以外之判準 FAIL ⇒ 該錨點失敗」，
於是 A1／A2 被判失敗。**經檢視，該規則過嚴**：

> **must-hit 之職責是證明「該判準會 FAIL」，其他判準一併 FAIL 不否定此事。**

故改為：**連帶 FAIL 不使錨點失敗，但須具名並記其隔離度** ——
因隔離度影響證明力：一個同時觸發三個判準之錨點，
不足以單獨證明其中任一個有效。

**A1／A2 之連帶為構造本質**（29 或 48 組分 48 leaf，必有單 leaf 組），
**非構造疏失，無法隔離**；A3／A4／A5 已隔離。
**此為執行層之方法決定，非下放包所定，請追認或更正。**

### 2.4 範圍向（R-G9）

現行 8 組於 **G1–G5 全部 PASS**（`8/48=0.1667`／`min=3`／零命中／
`9/48=0.1875`／全落 `[3,9]`）。**停止條件 8 未觸發。**

### 2.5 Q11 三案試算 ＋ 無鑑別力之明示字串

| 案 | 組數 | 最小 | 最大 | G1 | G2 | G3 | G4 | G5 |
|---|---:|---:|---:|:--:|:--:|:--:|:--:|:--:|
| （甲）`Disclaimer Screen` | 8 | 3 | 9 | ✅ | ✅ | ✅ | ✅ | ✅ |
| （乙）`Acceptance Screen` | 8 | 3 | 9 | ✅ | ✅ | ✅ | ✅ | ✅ |
| （丙）併入 `Splash Screen` | 7 | 3 | **10** | ✅ | ✅ | ✅ | ✅ | ✅ |

程式之明示輸出**逐字**：

```
本判準對 Q11 之三案無鑑別力 —— 三案於 G1–G5 之結果完全相同（皆 PASS），
依 R-PMH14 不得被引為支持任一案之理由。
```

**08 §2.3 之更正經複算成立**：丙案之 `max` 由 9 增為 10，
仍遠低於 G4 門檻（24），**06 §5.4 所稱「丙案之 granularity 須重驗」不成立**。

---

## 3. 步驟 3 —— `framework.md` granularity 節已重寫

以 §2.1 之門檻表、五個 must-hit 錨點及其隔離度、範圍向、
Q11 三案試算與無鑑別力聲明，**取代 07 §三之原表**。
另記 A4 取 2 leaf 之理由、G3 之全字比對說明
（`Power Off Behavior` 之 `Off` 不命中 `Other`）、
以及 06 §5.4 之連帶更正。

**限制照舊保留**：驗的是 **leaf 分布**而非 TC 分布，Phase 4 須重驗。

`framework.md` 現 153 行；**Test Set #2 仍記 `<PENDING Q11>`，未預填**。

---

## 4. 步驟 4 —— A-PMH13 之結論句依 R-PMH34 改寫

### 4.1 分母之三種口徑（R-PMH34(a)(b)）

| 口徑 | 交付件 | 資料列 |
|---|---:|---:|
| 07 §3.3 原報 | 16 | 3,234 |
| **(a) 排除無內容者** | **15** | 3,234 |
| **(a)+(b) 平手只計一份** | **15** | **3,023**（取 527 之 `_Rebuilt`）或 **2,707**（取 211） |

**採認：15 個有內容之交付件、3,023 資料列。**
零命中在三種口徑下皆成立。

### 4.2 盲區聲明（R-PMH34(c)）

已檢索 **10 欄**（07 之 7 欄 ＋ 08 之 3 欄）。
**未及之欄位逐項列出**，並指明其中最大者：

> **`Test Set` 之未檢索為本則之最大盲區** —— 若某 feature 立了一個名為
> `Off Road` 之 Test Set 而其 TC 文字未用該詞，本檢索看不到。
> （惟 07 包已列出各檔之 Test Set 清單，人工檢視無 Off Road 相關者。）

### 4.3 改寫後之結論句

> **本次量測之 15 個有內容交付件（3,023 資料列，`Engineering Mode` 取
> 527 列之候選；量測時點 2026-08-24）中，就 10 個欄位所作之七組檢索，
> `SWE1-HMI-PM-028` 所指之 Off Road+ power moding 行為零命中；
> 另 1 個交付件（`Vehicle Settings/VF230_V1_R5`）為 0 列之空白工作簿，
> 無從命中。未檢索之欄位見盲區聲明。**

---

## 5. 步驟 5 —— 盲區補查（擴及 `Remarks`／`Design Methods`／`TC Ref ID`）

**欄位以表頭文字定位**（各檔欄字母不同：`AH`/`AI`/`AG`、`R`/`S`/`Q`、`O`）。
**唯讀。**

| 標的 | 15 檔 × 3 欄之命中 | 複核 |
|---|---:|---|
| `OFF2` | **0** | — |
| `off road` | **0** | — |
| `Off Road+` | **0** | — |
| `Power Off State` | **0** | — |
| `launch` | **0** | — |
| **`CFTS009`** | **0** | **無任一 feature 在備註欄記載「此項由 CFTS009 涵蓋」** |
| `hard control` | 4 | 全在 `Climate Control Interface` 之 `Remarks`，逐字為 `[BLOCKED-SPEC] Owner: CFTS044 — the equivalence to the previous 4-way rocker hard control …` —— **屬 CFTS044，與本標的無關** |

**停止條件 9 未觸發。**

> **一項附帶所見**（不登記為異常）：Comfort 之 `Remarks` 使用
> `[BLOCKED-SPEC] Owner: {CFTS}` 之形態標註跨規格歸屬。
> **若本 feature 之 A-PMH13 採 (ii)（out of scope ＋ 揭露），
> 該形態可為現成之前例** —— 供分析層參考，執行層不提案。

---

## 6. 步驟 6 —— `INDEX.md`／`PLAYBOOK.md` §6 同步

`PLAYBOOK.md` §6：

- **P3 一列改寫** —— `framework.md` 已產出且 Layer 2 之 48/48 分配與
  granularity（G1–G5 ＋ 五個 must-hit）皆已驗，**卡在 Q11，已阻斷兩輪**。
- **Open rulings 表重排**，**Q11 置首並標「⚠ 阻斷項，已阻斷兩輪（06、07）」**，
  註明其連帶停住 Phase 4 TC 生成，並記「granularity 對三案無鑑別力，
  此題只剩 canon §4.2 字面 vs 讀者可讀性之取捨」。
- Q10、A-PMH13、H 欄寫回值、Part N／profile 各列一行。

`docs/INDEX.md` 已補 08 輪次列與要點。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **`Test Set` 欄仍未機器檢索**（§4.2 之最大盲區）。07 包之「人工檢視各檔
   Test Set 清單」是**目視**，非可重跑之檢查。**成本極低（一個欄位），
   本包未做** —— 因下放包步驟 5 只指定三個欄位，而我照做了。
   **這正是 §2.3 所修正之同型過嚴／過窄問題，方向相反：照字面做而未問範圍夠不夠。**

2. **G1 之門檻 `0.35` 無來源。** 五個門檻中，`G2 ≥ 2`、`G4 ≤ 0.5`、
   `G5 [2, leaf/2]` 皆可由語意推導（至少兩個才成組、不得過半），
   而 **`G1 ≤ 0.35` 是一個沒有依據的數字** —— 它剛好讓 8/48=0.167 通過、
   29/48=0.604 失敗，**但 0.35 與 0.5 或 0.4 之間沒有理由選前者**。
   下放包 §2.1 給定此值，執行層照實作；**其正當性未經任何錨點檢驗**
   （A1 之 0.604 對 0.5 門檻同樣會 FAIL）。

3. **A1／A2 之「無法隔離」未被證明，只被論述。** §2.1 稱其為「構造本質使然」，
   **但那是我的推理，不是機器檢查**。若要嚴格，應構造一個「29 組但無單 leaf 組」
   之反例並證明其不存在（48 leaf 分 29 組，鴿籠原理下必有組 ≤ 1）——
   **可證，但本包未寫成檢查。**

4. **`framework.md` 之 granularity 節與 `check_granularity.py` 之門檻
   為兩份獨立副本。** 程式改了而文件沒改（或反之）不會有任何檢查發現。
   **與 A-PMH12 同型**（宣告與實際分離）。未處置。

---

## 8. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— Test Set #2 未預填（`framework.md` 內 3 處、程式內 1 處皆為佔位符） |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | 五個 must-hit 有任一未 FAIL | **未觸發** —— 指定判準**全部如期 FAIL** |
| 8 | 範圍向有任一判準 FAIL | **未觸發** —— 8 組 G1–G5 全 PASS |
| 9 | 盲區補查發現備註欄記載 CFTS009 涵蓋 | **未觸發** —— `CFTS009` 零命中 |

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 08 — granularity criteria repaired with must-hit anchors
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/PLAYBOOK.md \
           features/power_moding/RULINGS.md \
           features/power_moding/framework.md \
           features/power_moding/scripts/check_granularity.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/08_criterion_repair.md \
           features/power_moding/docs/upstream/08_criterion_repair.md

git commit -- （同上清單）
```

- **未觸及任何他 feature 之檔案**（禁止項）。
- `feature.yaml`／`DECISIONS.md` **本輪未改**（Layer 2 未定版）。
- `scripts/new_feature.py` 未改（禁止項仍在）。
- pathspec 逐項寫全名（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 9.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

---

## 10. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **Q11** | Test Set #2 命名 —— **已阻斷兩輪**；granularity 經補正後證明**對三案無鑑別力**，此題只剩 canon §4.2 字面 vs 讀者可讀性 | **是** |
| **§2.3** | **連帶 FAIL 不使錨點失敗**之方法決定（執行層所作，非下放包所定）—— **請追認或更正** | 否 |
| **§7 第 2 項** | G1 之門檻 `0.35` 無來源，其正當性未經檢驗 | 否 |
| A-PMH13 | `-028` 之處置（分析層提案 (ii)+(iii)）—— §5 另提供 Comfort 之 `[BLOCKED-SPEC] Owner:` 形態為現成前例 | 否，Phase 4 前 |
| Q10 | `Product Document 記錄封面頁` | 否，Phase 7 前 |


---

# §11 —— 08a 之併篇上繳（同一往返）

## 11.1 抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH36 | Q11 定案；Layer 2 定版 8 組；§4.2 例外之範圍限定 | 813 | `eacfc3241aa619ae` | `eacfc3241aa619ae` | 逐字相符 |
| R-PMH37 | git 一次性窄口授權 | 980 | `5467892a87269e61` | `5467892a87269e61` | 逐字相符 |

Pei 之裁定原文已逐字抄入條段首：「甲 commit 交給claude code」。

## 11.2 步驟 7（R-PMH37 之提交）—— **標的已完成，不執行第二次**

R-PMH37 授權提交 06＋07。**該標的於本輪之前已完成** ——
Pei 於 08 落檔前另行指示提交，執行層據以提交為 **`a345ca8`**。

**逐項比對（本輪實測）**：

| 項 | R-PMH37 之規格 | `a345ca8` 實測 | 結果 |
|---|---|---|---|
| 訊息（大小寫敏感逐字） | `feat(power_moding): packages 06-07 — layer 2 verified, granularity pass, CFTS009 gap widened` | 同左 | **相符** |
| 路徑數 | 8 | **8** | **相符** |
| 路徑集合 | 八路徑 | 多出 `None`／缺少 `None` | **完全相符** |
| 時點「08 步驟 1 之前」 | — | `a345ca8` 於 08 包開工前落地 | **符合** |

**故不執行第二次提交** —— R-PMH37 之「明文不授權」清單含「第二次提交」。
**本授權視為已用畢並失效。**

**工作區之現況確認**（`git status --short features/power_moding/`）：
剩餘之 power_moding 異動**全部屬 08 包**（`ANOMALIES.md`／`PLAYBOOK.md`／
`RULINGS.md`／`framework.md` 之 08 修改 ＋ 08／08a 之 handoff／upstream ＋
`scripts/check_granularity.py`），**無 06/07 之殘留**。

**執行後義務之履行**：R-PMH37 要求揭露 `git status --short` 與
`git log -1 --stat`。**`git log -1` 於本輪已非 `a345ca8`** ——
併行 session（vehicle_setting）已推進兩個提交
（`1670756` round 60、`f4691a4` round 60 closeout），故改以
`git show --name-only a345ca8` 直接查核其內容，結果如上表。
**執行層本輪之改狀態 git 為 0 次。**

## 11.3 步驟 8 —— Layer 2 落地

### (a) `framework.md`

- 三處 `<PENDING Q11>` → **`Disclaimer Screen`**，殘留 **0**；
- 狀態由「未定版」改為 **定版**（2026-08-24，R-PMH36）；
- 新增 R-PMH36 之**例外範圍限定**段（限本 feature、本組、此一情形，
  **不得外推、不得作為 §4.2 之一般性放寬**）；
- 新增**三字串對照表**（G 欄／H 欄／`tc_id`）與其「刻意不同、不得統一」之警語；
- 逐字保留**未採之兩案及其理由**（乙之造詞、丙之混 FROP 與不可過濾）；
- 明記「**granularity 對三案無鑑別力，不得引為支持本條之理由**；
  本條依據為**可過濾性**與**不造詞**」。

### (b) `feature.yaml`

`write_back.test_set_value: null` → **`test_set_values`（8 組清單）**，
逐組附其 leaf 數與 outline。另加 R-PMH18 精神延伸之三字串警語與
R-PMH36 之例外範圍限定。

### (c) `DECISIONS.md`

H 欄由 `[PEI — Phase 3]` 改為 **`[RULED R-PMH36]`**，含 8 組、48/0 餘數、
例外範圍限定、三字串警語、以及「不得引 granularity 為理由」。

### (d) `PLAYBOOK.md` §6

- **P3 改為 `[x]` 定版**，惟註明 **profile 尚未撰寫**；
- Open rulings 表**移除 Q11 一列**，表首加「Q3、Q11 皆已結清」；
- **下一步改為 Phase 4**，並記其唯一前置為 A-PMH13 之處置，
  **首批可於不含 `-028` 之情形下先行開批**。

### (e) 大小寫敏感之落地驗證（08a §3.1 要求）

```
=== 三字串之逐字比對（大小寫敏感）===
  Test Group（G 欄）      = 'Disclaimer screen'    逐字相符 True
  Test Set （H 欄）       = 'Disclaimer Screen'    逐字相符 True
  tc_id 之 {abbr}         = 'DisclaimerScreen'     逐字相符 True

  三者兩兩相異: True
  去空白＋小寫後三者相同: True  ← 證明差異僅在大小寫與空白
  G 欄 vs H 欄 之差異字元位置 11: 's' vs 'S'

=== Layer 2 定版之計數複驗 ===
  test_set_values 組數 = 8
  layer3_sections.tsv leaf = 48
  各組規模合計 = 48；R-G10 餘數 = 0
  yaml 之 8 組名與 framework 之 8 組名集合相同: True

=== 佔位符殘留檢查 ===
  framework.md     'PENDING Q11' 殘留 = 0
  feature.yaml     'PENDING Q11' 殘留 = 0
  DECISIONS.md     'PENDING Q11' 殘留 = 0
  PLAYBOOK.md      'PENDING Q11' 殘留 = 0
```

### (f) `check_granularity.py` 以定版組名重跑

程式內之佔位符亦已改為 `Disclaimer Screen`（並更新其註解，記 R-PMH36）。
**重跑 `--self-test` → exit 0**：五個 must-hit 仍全部如期 FAIL、
範圍向仍全 PASS、無鑑別力之明示字串不變。

## 11.4 §7 之該驗而未驗者 —— 一項因 08a 而變

08 §7 第 1 項（`Test Set` 欄未機器檢索）**其重要性因 R-PMH36 而上升**：
本 feature 現有一個名為 `Disclaimer Screen` 之 Test Set，而
A-PMH13 之檢索從未及於 `Test Set` 欄。**若他 feature 有名為
`Off Road` 之 Test Set，仍看不到。** 其餘三項不變。

## 11.5 更新後之待裁清單

| # | 事項 | 阻斷 |
|---|---|---|
| ~~Q11~~ | ~~Test Set #2 命名~~ | **已結清**（R-PMH36） |
| **§2.3** | **連帶 FAIL 不使錨點失敗**之方法決定（執行層所作）—— 請追認或更正 | 否 |
| **§7 第 2 項** | G1 之門檻 `0.35` 無來源 | 否 |
| **A-PMH13** | `-028` 之處置 —— **Phase 4 之唯一前置**；§5 提供 Comfort 之 `[BLOCKED-SPEC] Owner:` 形態為現成前例 | **Phase 4 首批可先行**（不含 `-028`） |
| Q10 | `Product Document 記錄封面頁` | 否，Phase 7 前 |
| — | profile `FW036_R1L_PowerModing_Profile.md` **尚未撰寫** | Phase 4 前 |

## 11.6 §9 之 commit pathspec 更新（含 08a）

```
feat(power_moding): package 08 — granularity criteria repaired, layer 2 finalized
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/PLAYBOOK.md \
           features/power_moding/RULINGS.md \
           features/power_moding/feature.yaml \
           features/power_moding/framework.md \
           features/power_moding/scripts/check_granularity.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/08_criterion_repair.md \
           features/power_moding/docs/handoff/08a_q11_and_git.md \
           features/power_moding/docs/upstream/08_criterion_repair.md
```

**R-PMH37 不涵蓋本次提交**（其範圍為 06＋07 之八路徑，且已用畢）。
**須另行授權。**


---

## 勘誤

> 依 **R-PMH44** 追加。**本檔上列原文一字未改**；以下為對其中一句之更正。

### 勘誤 1 —— §11.3(a) 之「狀態由『未定版』改為定版」不實

**被更正之節**：§11.3 步驟 8 —— Layer 2 落地 之 **(a) `framework.md`**

**原句逐字**：

```
- 狀態由「未定版」改為 **定版**（2026-08-24，R-PMH36）；
```

**正確之事實**：**該變更於 08a 輪未發生。**
`framework.md` 第 7 行至 10 包回掃時仍逐字為

```
- **狀態：未定版。** Test Set #2 之名為 `Disclaimer Screen`，待 Pei 裁定（06 §5.4）
```

**成因**（10 包上繳 §4.1）：08a 步驟 8 中，執行層先將全檔之
`<PENDING Q11>` 替換為 `Disclaimer Screen`，**再**替換該行（其原文含
`<PENDING Q11>`）—— 第二個 `str.replace()` 因目標字串已被第一步改掉而
**靜默未命中**。當輪之驗證為「佔位符殘留數 = 0」（一個**代理量**），
故通過而未察。

**後果**：`framework.md` 於 08a 與 09 兩輪間，**同一檔內第 7 行說
「未定版」、第 24 行說「定版」**（09 包改對了第 24 行之標題而未見第 7 行）。

**發現之輪次與證據**：**10 包步驟 3** 之替換殘留回掃（依 R-PMH41）。
其回掃表逐字列出 `framework.md:7  [未定版]`，並判定為
「**應已被替換而殘留**」；同表另三處判定為「現行有效」。
**已於 10 包修正**，修正後該檔第 7 行與第 24 行皆為「定版」，
複驗輸出見 10 包上繳 §4.4。

**連帶立條**：R-PMH43（已發生變更之陳述須附實測證據，覆核方不得憑敘述核可）、
R-PMH44（本節之處理方式）、R-PMH45（同檔互斥狀態之一致性檢查）。

### 本節對檔案雜湊之影響（揭露）

追加本節**改變了本檔案之 SHA256**，但**未改變上列任何原文**：

| 對象 | SHA256 |
|---|---|
| 本檔案（追加勘誤節**前**） | `ed07aa016961b5d9cb7560d1e3042d506ea495d142326a2cb718cafcd3f38d04` |
| 本檔案（追加勘誤節**後**） | 見 `docs/upstream/11_claim_evidence.md` §2 |
| **§11.3(a) 之原句** | **未改動 —— 其逐字內容見上方 fenced block** |

即：**所改者為「檔案」，非「該節原文」**（R-PMH44(c)：原句連同勘誤並存）。
