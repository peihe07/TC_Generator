# 上繳包 22 —— #1 收斂為訊號側（pilot-01 rev3）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/22_pilot01_rev3.md`
- 步驟 1–6 全數執行。**五十八條停止條件全未觸發**（新增之 56／57／58 皆 PASS）
- **git 未執行**（§8 為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 1 R-DM49 抄錄 | 相符；`RULINGS.md` 之 R-DM 區塊累計 **51** 個，逐字元比對全數相符 |
| 2 #1 收斂 | ER 3／step 3 移除；`tc_title` 與括號下半改寫；deferred、覆蓋缺口、DR-DM10 皆已更新 |
| 3 §9 十七項 ＋ lint | lint **20 項行計皆 0**，I-sibling 0 為實測 |
| 4 R-DM49(c) | #4 之 `split_reason` 已補記證據強度差異 |
| 5(a) framework 閘 | **8／8**，無重複無遺漏，組名與簽核逐字相符（停止條件 56 未觸發） |
| 5(b) 訊號值閘 | `4 "DISP_HOT"` 重現（停止條件 57 未觸發） |
| 6 INDEX | 已更新 |

**退回項成立，且我同意其判斷比我自己的更嚴。** 21 包我判「#3 不受影響」
並就此收手，**沒有回頭檢 #1** —— 而 #1 之 ER 3 與被 deferred 的 #2
其實掛在同一個矛盾上。差別只在 #2 的問題出現在觸發條件（何時關），
#1 的問題出現在**可觀測性**（關了就看不見），形態不同故我沒有把它們
歸為一類。

---

## 一、R-DM49 之抄錄核對表

抄錄方式：`transcribe_rulings.py` 以 `^```(\w*)\n(.*?)^```\n` 自
`22_pilot01_rev3.md` 抽取，逐字元寫入 `features/display/RULINGS.md`
之「來源：下放包 22」節。**未經重打。**

## 抄錄核對表 — 22_pilot01_rev3.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 51 | R-DM49 | `features/display/RULINGS.md` | 582 | `f399e683a6d907dd` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **51** 個，與各下放包原檔逐字元比對 **全數相符**（51 vs 51）。

R-DM49 為 Display 專屬條文，依 §三之指定入 `features/display/RULINGS.md`，
不入 `docs/fw036/RULINGS_LEDGER.md`。本包無 R-G 條文。

---

## 二、收斂後之 #1 全文，及改寫理由

### 2.1 #1 全文（rev3）

| 欄 | 值 |
|---|---|
| `leaf_id` | `SWE1-DM-004` |
| `test_group` / `test_set` | `Display` / `Thermal Management` |
| `tc_title` | `Hot threshold exceeded → Hot state notified to HU` |
| `input_test_data` | `NA` |
| `specification_reference` | `CFTS020-4820282` / `CFTS020-4820289` |
| `design_method` | `狀態轉換 (State Transition Testing)` |
| `priority` / `functional_safety` | `P1` / `NA` |

```text
[test_item]
The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic. The software shall trigger warning popup requests when configured warning threshold conditions are satisfied.

(Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)

[pre_conditions]
1. The DCSD display temperature is 85 degrees C or below
2. No high priority screen (RVC) is active

[input_test_data]
NA

[test_procedure]
1. Raise the DCSD display temperature above 85 degrees C
2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 4 (DISP_HOT)

[expected_result]
1. The DCSD Display transitions to a Hot state
2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 4 (DISP_HOT) is received
```

### 2.2 `tc_title` 之改寫理由

rev2 之標題為 `Hot threshold exceeded → thermal warning popup displayed`。
**其結果側（`popup displayed`）已不在 ER 內** —— 標題承諾了 ER 不驗的東西，
即 canon §4.3 之違反。改為 `Hot threshold exceeded → Hot state notified to HU`：

| 判準 | 結果 |
|---|---|
| §4.3 三形之一 | 「條件 → 結果」形 |
| 2–14 字 | **9 字**（機器計，§五） |
| sibling token 可見且與 #4 相異 | `Hot threshold exceeded` vs #4 之 `Temperature at 85 degrees C` |
| 無情態動詞 | 無 `shall`／`should`／`will` |
| 與 ER 相符 | ER 2 即「通知 HU」之訊號側 |

**未寫 `DISP_HOT` 於標題**：該 token 是值標籤，寫入標題會使標題帶
未經 §8.7.5 格式規範之訊號值。以 `Hot state notified` 表述其行為。

### 2.3 `test_item` 括號下半之改寫理由

rev2：`(Warning stage on crossing the Hot threshold — the popup that follows the DISP_HOT notification)`
rev3：`(Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)`

三點：

1. 原文以 popup 為主詞，同樣已不在 ER 內
2. 改後**明寫 `the warning popup is deferred`** —— 使閱讀 036 工作簿者
   在不看 `batch_context.md` 的情況下也看得見這個 TC 是收斂過的
3. 與 #4 之括號下半（`(Boundary at the Hot threshold — 85 degrees C is
   defined as non-Hot, so nothing is triggered)`）**逐字比對非重複**
   （lint I-sibling 0，機器輸出見 §五）

### 2.4 `test_item` 上半**不動**

上半仍逐字含 `The software shall trigger warning popup requests when
configured warning threshold conditions are satisfied.` —— 該句為 leaf
之需求文，依 §4.5 保留。

**保留即製造了一個可見的落差：`test_item` 宣告要測 popup，ER 不測。**
本層判**保留並揭露**優於刪句：刪句會使 036 工作簿上看不出 004 是部分覆蓋，
而 §2.4 明文要求該缺口不得以「#1 已涵蓋 004」帶過。落差之說明寫在
括號下半（讀者看得見之處）與 `batch_context.md` §7.3（完整表）。

### 2.5 `specification_reference` 維持不變

`{4820282}`（DISP_HOT 通知 → ER 2）與 `{4820289}`（門檻與 RVC 前提 →
PC／step 1）**皆仍為 #1 直接驗證之節**。移除 popup 側不影響此二節之地位。

---

## 三、`batch_context.md` 之 `deferred` 與已知覆蓋缺口

### 3.1 `deferred` 陣列（`generated/pilot-01.json` 之機器輸出）

```text
1. SWE1-DM-004 之 warning popup（PU0517）—— DR-DM10(a) 未結。組 B {4820289}
   於越過門檻時即關背光，使 popup 之顯示不可觀測；組 A {4820283} 則蘊含
   警示階段。兩組皆宣告適用於 R1H / Atlantis High
2. SWE1-DM-005 之保護性關閉（原 #2）—— 組 A／組 B 何者為準未裁定，
   且 {4820283} 之警示階段無時長；DR-DM10 開立；21 包 §2.1 分支 3
3. SWE1-DM-005 之 multi-stage 分級門檻 —— DR-DM4 未結（CFTS_013 未取得）
```

第 2 項之措辭本輪亦更正：rev2 寫「其出處為 `{CFTS013-XXX}`（未填佔位符）」，
而 21 包已查明主因是組 A／B 之矛盾與 `{4820283}` 之無時長，
`{CFTS013-XXX}` 所在條為 `Radio:noSys`。**依 R-G19 一併更正。**

### 3.2 已知覆蓋缺口（`batch_context.md` §7.3 全文）

> leaf `SWE1-DM-004` 之需求文逐字含 **`shall trigger warning popup requests`**。
> `test_item` 上半依 §4.5 保留該需求文全文，**但本批之 ER 不再驗證該面向**。
>
> | 面向 | 本批狀態 |
> |---|---|
> | 監測熱狀態、評估 Hot 門檻 | **已驗**（#1 ER 1／ER 2、#4） |
> | `trigger warning popup requests` | **未驗** —— DR-DM10(a) 未結 |
>
> **004 之覆蓋為部分覆蓋。** 交付時不得以「004 有 TC」表述。

### 3.3 `DR-DM10` 之阻斷範圍已增列

「阻斷範圍」欄增列 **`SWE-DM-004 之 popup 側（PU0517，22 包 §二）`**，
「影響」欄增列組 B 使 `PU0517` 不可觀測之敘述。原列之 005 與 `PU0130` 不變。

---

## 四、三條之 §9 自檢十七項

判讀慣例同上繳 21：**「符」＝已逐項對照 canon 該節；「NA」＝該項之前提
不存在（非「略過」）。** 凡判準為機器可測者，輸出見 §五。
**與 rev2 相異之格皆以粗體標示。**

### 4.1 #1（`SWE1-DM-004` 訊號側）

| # | 項 | 判定 | 依據 |
|---|---|---|---|
| 1 | Test Set 與 `framework.md` 一致 | 符 | `Thermal Management`；**本輪另驗 framework 對 037 之 8／8**（§六(a)）—— 21 包 §八第 1 項之自陳已閉合 |
| 2 | tc_title 三形、2–14 字、sibling token、無情態 | **符（已改寫）** | 「條件 → 結果」形；**9 字**；`Hot threshold exceeded`；與 #4 相異 |
| 3 | PC 僅狀態／環境 | 符 | 兩項皆自 `{4820289}` 之觸發子句；無動作動詞（§五） |
| 4 | Input Test Data 欄位歸屬 | 符 | `NA` |
| 5 | 步驟可執行、無禁用動詞、Final Step 承載驗證 | **符（已收斂）** | `Raise`／`Read`；**step 2 為 Final Step 且承載全部驗證** |
| 6 | 步驟長度與意圖層級 | 符 | 兩步皆單一動作；step 2 為 necessary-intent |
| 7 | 標準 setup 片語 | NA | 本 feature 無已核定之片語庫 |
| 8 | CLI 步驟格式 | NA | 無 CLI 步驟 |
| 9 | baseline | NA | 單向轉換 |
| 10 | Procedure ↔ ER 1:1、可觀測、無情態、涵蓋完整結果 | **符（2:2）** | **「涵蓋完整結果」之範圍已隨 deferred 收窄** —— 本 TC 之標的為訊號通知，popup 不在其內（§三之覆蓋缺口已揭露） |
| 11 | 無 FP／FF；supported 配負向 | 符 | 其負向為 **#4** |
| 12 | 追溯、不擴入 sibling、無捏造 | 符 | `4 (DISP_HOT)` **本輪重跑重現**（§六(b)）—— 21 包 §八第 2 項之自陳已閉合 |
| 13 | Design Method 於步驟定稿後指派 | 符 | 步驟收斂後複核仍為 `狀態轉換`（跨 non-Hot → Hot） |
| 14 | 四欄無行尾句號 | 符 | 0（§五） |
| 15 | UI 標籤用 `"…"` | **NA（改變）** | rev2 為「符」（有 popup 文字）；**rev3 之四欄已無 UI 標籤**，方括號 0 |
| 16 | `specification_reference` 列出所有直接驗證之節 | 符 | `{4820282}`（ER 2）＋`{4820289}`（PC／step 1）；見 §2.5 |
| 17 | 來源規格勝過索引匯出；門檻為 spec 具體值 | 符 | 門檻取 CFTS 本文（SYS2 r30–r34 無溫度值）；`degrees C` 依 `{4820289}` |

### 4.2 #4（`SWE1-DM-004` 邊界負向）

| # | 項 | 判定 | 依據 |
|---|---|---|---|
| 1 | Test Set | 符 | 同 #1 |
| 2 | tc_title | 符 | 10 字；`Temperature at 85 degrees C`；3 of 3 相異（§五） |
| 3 | PC | 符 | `below 85 degrees C` 為 `{4820289}` 之 non-Hot 側 |
| 4 | Input Test Data | 符 | `NA` |
| 5 | 步驟／禁用動詞／Final Step | 符 | `Raise`／`Read`／`Read`；lint A 0 |
| 6 | 步驟長度與意圖層級 | 符 | 三步皆單一動作，step 2／3 為 record 型 |
| 7 | setup 片語 | NA | 同 #1 |
| 8 | CLI | NA | 無 |
| 9 | baseline | NA | 驗「不發生」，前後同態 |
| 10 | 1:1、可觀測、無情態 | 符 | **3:3**（§五） |
| 11 | 無 FP／FF；supported 配負向 | 符 | 本條即 #1 之負向；`split_flag = True` |
| 12 | 追溯、無捏造 | 符 | 85 為 spec 明載之 `<=` 側 |
| 13 | Design Method 後指派 | 符 | `邊界值分析 (BVA)` |
| 14 | 行尾句號 | 符 | 0（§五） |
| 15 | UI 標籤 | NA | 無 UI 標籤 |
| 16 | `specification_reference` | 符 | 僅 `{4820289}` |
| 17 | 門檻為 spec 具體值 | **符（已補記）** | **`split_reason` 依 R-DM49(c) 補記 ER 3 之證據強度差異**（全文見下） |

#4 之 `split_reason` 全文（rev3）：

```text
§8.3 boundary 軸：`{4820289}` 之 `> 85 degrees C` 與 `<= 85 degrees C` 使 85 恰屬 non-Hot，為 spec 明載之邊界；與正向條之失效可獨立發生（§9 第 11 項之 negative）；R-DM49(c)：ER 3 之 `No popup is shown on the display` 係自「觸發條件未成立」推得 —— `{4820289}` 只載越過門檻時做四件事，未載未越過時不做。其證據強度與 ER 1／ER 2 不同（後二者有逐字支撐），依 R-DM49(a)(b) 判其可寫：所否定之行為其正向出處逐字存在，且該否定未引入任何新的值
```

**R-DM49(a) 之逐項核對**：所否定之行為（popup 顯示）其正向出處為
`PU0517` 之 Description 與 `{4820282}`／`{4820289}` 之觸發條件，逐字存在 → 滿足。
**(b)**：ER 3 為 `No popup is shown on the display`，**未引入任何值** → 滿足。
**(c)**：已記於 `split_reason` → 滿足。

> **一項須具名之緊張**：#4 之 ER 3 所否定者，正是 #1 於本輪被 deferred
> 的那個 popup。即 **popup 之「會顯示」不可驗，而其「不顯示」可驗。**
> 這不矛盾 —— 前者被 deferred 是因為組 B 下**看不見**，後者驗的是
> 「畫面上沒有東西」，在兩組下皆成立（組 A 未觸發故無 popup；
> 組 B 未觸發故背光仍亮且無 popup）。**但兩者不對稱這件事本身值得記明。**

### 4.3 #3（`SWE1-DM-005` 回復）

十七項與上繳 21 §4.3 **全同，無一格改變**（本輪未動 #3）。要點複述：
第 9 項「符」（step 1／ER 1 為 §5.6 baseline）；第 16 項三節俱列；
第 17 項 `85 deg C` 依 `{4820290}` 之逐字寫法，與 #1／#4 之 `degrees C`
不統一係規格自身之差異。

### 4.4 三條共通之「未取」（rev3 更新）

| 項 | 未取之物 | 理由 |
|---|---|---|
| `estimated_test_time`／`vehicle_models`／`remarks` | 空 | B 欄／Q 欄「辨識但不寫入」 |
| `tc_id` | `null` | 編號屬 036 母本，未寫回 |
| ER 中之 raw 值（`[DISP_OFF]`／`[DISP_ON]`） | 未寫 | R-DM48；DR-DM9 未結 |
| **`PU0517` 之顯示與停留時間** | **本輪起未寫** | **DR-DM10(a) 未結；組 B 下不可觀測** |
| 亮度降低之數值 | 未寫 | 規格未給（§8.4.1）；**本輪起該項已無所附麗**（popup ER 已移除） |

---

## 五、`lint036.py` 全文輸出（整批，附母體；I-sibling 具名）

### 5.1 母體與方法

| 項 | 值 |
|---|---|
| 受檢母體 | `features/display/generated/pilot-01.json` 之 `tcs`，**3 筆**（rev3） |
| 受檢方式 | 三筆寫入 036 母本之**拋棄式複本**（scratchpad），資料列 10–12，其餘資料列清空 |
| profile | `display`（P 採 R-1 v3；另跑 Q／R／T） |
| 036 母本 sha256（前後） | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`（**未變**） |
| 寫回母本 | **否**（`write_back.written = false`） |
| 欄位映射 | D=leaf_id, G/H=group/set, I=test_item, J=PC, K=ITD, L=proc, M=ER, N=spec_ref, O=NEW, P=priority, R=design_method, S=functional_safety, AA=author |

### 5.2 輸出全文

```text
# lint036 報告：lint_scratch.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_scratch.xlsx`（唯讀）
- 資料列數：3
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**二十項行計皆 0；「明細」節為空。**

### 5.3 I-sibling 之具名複驗（步驟 3 之特別要求）

`I-sibling` 檢查「同 Requirement ID 之括號行逐字重複」。本批中
**#1 與 #4 同為 `SWE1-DM-004`** —— 該檢查於本批**有母體**，0 為實測。
兩者之括號下半（機器輸出，§5.4）：

```text
  SWE1-DM-004: 2 筆
    TC#1 (Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)
    TC#2 (Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered)
    逐字重複 = 0
```

> `TC#2` 為 JSON 陣列索引（`tcs[1]`），即本文之 **#4**。
> 陣列依 leaf 排序為 `[#1, #4, #3]`，故索引與編號不一致 —— 具名以免誤讀。

### 5.4 canon 側之機器檢查（lint 未涵蓋者，含停止條件 54／55／58）

```text
population: features/display/generated/pilot-01.json, tcs = 3
revision: rev3（22 包）：#1 收斂為訊號側（ER 3／step 3 移除，popup 側 deferred）；R-DM49 立條並於 #4 記明證據強度

--- stop condition 58: #1 之 ER／procedure 是否含依賴「顯示為亮」之觀測 ---
  TC#1 tc_title = Hot threshold exceeded → Hot state notified to HU
  hits = 0

--- stop condition 54: unresolved value labels in expected_result ---
  hits = 0
--- stop condition 55: action verbs in pre_conditions ---
  hits = 0

--- tc_title: 字數（canon 4.3: 2-14）與相異 ---
  TC#1 words=9 :: Hot threshold exceeded → Hot state notified to HU
  TC#2 words=10 :: Temperature at 85 degrees C → Hot state not entered
  TC#3 words=11 :: Temperature falls back to non-Hot → backlight on and touch enabled
  distinct = 3 of 3

--- I-sibling: 同 leaf 之 test_item 括號下半逐字比對 ---
  SWE1-DM-004: 2 筆
    TC#1 (Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)
    TC#2 (Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered)
    逐字重複 = 0
  SWE1-DM-005: 1 筆
    TC#3 (Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown)
    逐字重複 = 0

--- test_item 上半 tokens（lint L 閾值 50）---
  TC#1 tokens=34
  TC#2 tokens=20
  TC#3 tokens=16

--- procedure / expected_result 1:1 ---
  TC#1 proc=2 er=2 match=True
  TC#2 proc=3 er=3 match=True
  TC#3 proc=4 er=4 match=True

--- canon 11: 行尾句號／方括號（四欄）---
  行尾句號 hits = 0   方括號 hits = 0

--- deferred 陣列 ---
  - SWE1-DM-004 之 warning popup（PU0517）—— DR-DM10(a) 未結。組 B {4820289} 於越過門檻時即關背光，使 popup 之顯示不可觀測；組 A {4820283} 則蘊含警示階段。兩組皆宣告適用於 R1H / Atlantis High
  - SWE1-DM-005 之保護性關閉（原 #2）—— 組 A／組 B 何者為準未裁定，且 {4820283} 之警示階段無時長；DR-DM10 開立；21 包 §2.1 分支 3
  - SWE1-DM-005 之 multi-stage 分級門檻 —— DR-DM4 未結（CFTS_013 未取得）
```

**停止條件 58 之判準**：對 #1 之 `test_procedure` 與 `expected_result`
逐行搜 11 個「依賴顯示為亮」之詞（`popup`／`pop up`／`screen`／
`displayed`／`display shows`／`shown`／`brightness`／`icon`／`message`／
`text`／`warning`，`\b` 邊界、忽略大小寫）→ **hits = 0**。

> 該詞表是我自訂的，**不是規格或 canon 給的**。它涵蓋本批已知的形態，
> 但不保證窮盡 —— 例如 `visible`、`lit`、`animation` 未列。
> 本 TC 收斂後僅 2 步 2 ER 且已人工逐行複讀，故判其足夠；
> **若日後有 TC 之 ER 較長，該詞表須先擴充再用。**

### 5.5 綁定檢查（R-G23，產出前執行）

```text
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 11

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| a03_report | `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` | `ab3198e81fb21d21…` | MATCH |
| cfts_doc | `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `8696d1f596e33677…` | `8696d1f596e33677…` | MATCH |
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| popup_list | `Pop Up List HMI R1 (26PI).xlsx` | `ff47b7be63e5824c…` | `ff47b7be63e5824c…` | MATCH |
| popup_priority_matrix | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `dc078763c67b5238…` | `dc078763c67b5238…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| sys2_export | `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | `421c8eef3f5cb01a…` | `421c8eef3f5cb01a…` | MATCH |
| sys3_sysad | `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | `be9c97af0211a703…` | `be9c97af0211a703…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**11 of 11 match.**
```

本輪產出用到 `cfts_doc`、`popup_list`、`dbc_b`、`lid`、`a03_report`、
`workbook_master` 六項，皆 MATCH。

---

## 六、步驟 5 兩項閘之輸出

**兩項閘皆閉合了上繳 21 §八之自陳。** 本輪執行，**仍不寫回 036 母本**。

### 6.1 閘 (a) —— `framework.md` Layer 2 對 037 之 8 leaf

抽取式：`framework.md` 之 `### Layer 2` 至 `### Layer 3` 區間，
以 `^\|\s*`([^`]+)`\s*\|\s*([0-9, ]+)\s*\|` 取「組名 → leaves」；
037 側以 `read_037_leaves.py` 之實測輸出取 `SWE-DM-\d{3}`。

```text
framework.md Layer 2 之組（機器抽取）：
  Operative State      -> ['001', '002', '003']
  Thermal Management   -> ['004', '005']
  Pop Up Handling      -> ['006']
  Rear View Camera     -> ['007', '008']
  groups = 4

037 leaves（read_037_leaves.py 實測）：['SWE-DM-001', 'SWE-DM-002', 'SWE-DM-003', 'SWE-DM-004', 'SWE-DM-005', 'SWE-DM-006', 'SWE-DM-007', 'SWE-DM-008']  n=8

covered      = ['001', '002', '003', '004', '005', '006', '007', '008']  n=8
distinct     = 8
duplicates   = []
missing      = []
extra        = []

8／8 逐字相符：PASS（停止條件 56）

DECISIONS.md 簽核第 2 項之組名（機器抽取）：['Operative State', 'Thermal Management', 'Pop Up Handling', 'Rear View Camera']
與 framework.md 逐字相符：PASS
```

**8／8，無重複、無遺漏、無多餘；四組名與 `DECISIONS.md` 簽核第 2 項
逐字相符。停止條件 56 未觸發。**

> 21 包 §八第 1 項自陳「只驗了 TC 與 framework 一致，未驗 framework
> 與 037 一致」。**本輪補上後者。** 兩者現皆為實測。
>
> 仍須記明其**未**涵蓋者：本閘驗的是 **leaf 之集合相等**，
> 不驗「某 leaf 被分到的那一組是否恰當」。後者（`Pop Up Handling`
> 單 leaf 是否為 genuine outlier）仍只有 `framework.md` §4.1.3 之
> 人工論述，**未被任何腳本檢查**。

### 6.2 閘 (b) —— `4 (DISP_HOT)` 之重跑

`signal_resolution.py`（exit 0）：

```text
| DCSD_DISP_STAT | 420 | DIS_CENTERSTACK.DCSD_DISP_STAT | B-CAN | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y | 選定判準：MESSAGE.Signal 兩半皆相等→ BHCAN2-R1 |
```

`dbc_probe.py`（exit 0）：

```text
### DCSD_DISP_STAT
  BHCAN2-R1: BO_ 1445 DIS_CENTERSTACK | tx=SGW
      SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" ETM,LTM
      VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA";
  FDCAN8-R1: 0 命中
  BHCAN-R4: BO_ 1445 DIS_CENTERSTACK | tx=DCSD
      SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" SGW
      VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA";
  FDCAN8-R5: 0 命中
```

**`4 "DISP_HOT"` 重現，與 #1 之 ER 2 逐字相符。停止條件 57 未觸發。**

#### 6.2.1 一項本輪才看見的事：`DISP_HOT` 在別的訊號上是 **3**

同一次重跑之輸出另含：

```text
### FPDM_DISP_STAT  (在 BHCAN-R4: 無)
  BO_ 1513 FPDM1 | tx=FPDM
  SG_ FPDM_DISP_STAT : 2|3@0+ (1,0) [0|3] "" ETM
  VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "DISP_HOT" 7 "SNA";

### TGW_FPDM_DISP_STATSts  (在 BHCAN-R4: 無)
  BO_ 1282 RADIO_B2 | tx=ETM
  SG_ TGW_FPDM_DISP_STATSts : 50|3@0+ (1,0) [0|3] "" FPDM
  VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "DISP_HOT" 7 "SNA";
```

**同一個標籤 `DISP_HOT`，在 `DCSD_DISP_STAT` 上是 raw 4，
在 `FPDM_DISP_STAT` 與 `TGW_FPDM_DISP_STATSts` 上是 raw 3。**

本輪之比對未被污染，因為 `signal_resolution.py` 之選定判準是
**`MESSAGE.Signal` 兩半皆相等**（04 輪之修正）—— 若仍用「第一個含該
訊號名之 DBC」，此處極可能取到 FPDM 側。

**這是 R-DM48「不可外推」之第二個實證**（第一個是
`[DISP_REAR_CAMERA]` 對 `RR_CMRA`）：R-DM48 原以「同一訊號之六個值裡
規則就不一致」立論，本輪加上一條更強的 —— **同一標籤跨訊號亦不一致**。

已登 **A-DM34**（LOW，非阻塞：本批未用到 FPDM 側任何值）。

---

## 七、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A 與組 B 何者為本架構之準 | **004 之 popup 側（本輪新增）**；005 之關閉側全部 TC | DR-DM10(a) |
| A2 | `{4820283}` 警示階段之時長／終止準據 | 原 #2；`PU0130` | DR-DM10(b) |
| A3 | `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]` 之 raw 值 | 現行 ER 只驗行為不寫值；007／008 之訊號欄 | DR-DM9 |
| A4 | `popup_priority.tsv` | `SWE-DM-006` | DR-DM2 |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |

**A1 之阻斷範圍於本輪擴大** —— 21 包時只列 005，現含 004 之 popup 側。
`DATA_REQUESTS.md` 已同步。

### B 類 —— 不阻斷交付

| 編號 | 項 | 為何不阻斷 |
|---|---|---|
| B1 | `{CFTS013-XXX}` 之實際條號 | 其所在條為 `Radio:noSys`，不適用本專案 |
| B2 | `{CFTS013-967}` 與 DR-DM4 三號不同 | 同上，出現於 Multi-stage 節 |
| B3 | multi-stage 分級門檻（DR-DM4） | 單級 85 °C 行為可獨立驗 |
| B4 | 亮度降低之數值 | **本輪起已無所附麗** —— popup ER 已 deferred |
| B5 | `degrees C` 與 `deg C` 寫法不一致 | 規格自身之差異，逐字沿用 |
| B6 | DTC `B1429-00` 之 mature／de-mature 時間門檻 | 本批之 TC 未驗 DTC —— **未取而非漏取** |
| B7 | **`DISP_HOT` 跨訊號之 raw 值不一致（A-DM34）** | 本批未用到 FPDM 側任何值；判準已足以隔離 |
| B8 | **Test Set 分組之「恰當性」未被腳本檢查** | 集合相等已驗（§6.1）；分組恰當性屬 Tier 2 之人工論述 |
| B9 | **停止條件 58 之詞表非窮盡** | 本 TC 僅 2 步 2 ER 且已人工複讀；日後 ER 較長時須先擴充 |

B7／B8／B9 為本輪新增。

---

## 八、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/generated/pilot-01.json \
  features/display/RULINGS.md \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/22_pilot01_rev3.md \
  features/display/docs/upstream/22_pilot01_rev3.md
```

```text
feat(display): pilot-01 rev3 — converge TC #1 to the signal side

- drop the popup expected result from TC #1: clause group B ({4820289}) turns
  the backlight off on crossing the threshold, so a popup shown for ten
  seconds is not observable and the TC would always fail against that group
- rewrite its title and test-item note to match the narrowed expected result,
  and record the partial coverage of SWE-DM-004 explicitly
- extend DR-DM10 to cover the popup side of SWE-DM-004
- add R-DM49: a negative expected result may be inferred from an unmet
  trigger, provided the positive source is verbatim, no new value is
  introduced, and the weaker evidence is recorded
- record A-DM34: the DISP_HOT label is raw 4 on DCSD_DISP_STAT but raw 3 on
  FPDM_DISP_STAT
- gates before write-back: framework covers all eight 037 leaves, and the
  DISP_HOT raw value reproduces
- lint036 --profile display: all twenty checks report zero
```

> `batches/pilot-01/batch_context.md` 不入 pathspec（`.gitignore` 已排除）。
> 036 母本未變更，亦不入。

---

## 九、本包是否仍有該驗而未驗者 —— 獨立判斷

**上繳 21 之三項自陳，本輪閉合兩項（§六），第三項由 R-DM49 定為規則。
另有兩項新的。**

1. **`#4` 之 ER 3 與 `#1` 之被 deferred 不對稱，我判其成立但未被任何
   腳本檢查。** 「popup 不顯示」可驗而「popup 顯示」不可驗 —— 這個判斷
   是我人工做的（§4.2 之緊張），其論據是「未觸發時兩組皆無 popup」。
   **該論據為真，但它與 #1 被 deferred 的論據來自同一份互相矛盾的規格。**
   若 DR-DM10(a) 裁定後發現組 A／B 之外還有第三種讀法，#4 之 ER 3
   須重審。

2. **停止條件 58 之詞表是我自訂的**（§5.4 已具名）。它擋住了本批，
   但它不是從 canon 或規格導出的判準，**其完備性沒有證據**。

3. **`test_item` 上半保留 popup 句而 ER 不驗，此落差目前只靠文字揭露。**
   `lint036` 沒有、也不容易有一個「test_item 所述是否被 ER 涵蓋」的檢查。
   **這是本批最可能被下游誤讀的一處** —— 讀 036 工作簿的人若只看
   `test_item` 上半，會以為 popup 已被測。括號下半之
   `the warning popup is deferred` 是唯一的防線。

> 第 3 項我判斷值得一條條文，但**不自行立條**（Tier 2）。
> 提請分析層考慮：是否應規定「TC 之 `test_item` 上半若含未被該 TC 之 ER
> 涵蓋之需求面向，須於括號下半明寫其未涵蓋」—— 本輪是自發做的，
> 沒有規則要求。
