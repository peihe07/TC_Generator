# 37 — Comfort HMI / 目的版判準、軸 2 複驗、鏡面除霜、批次 11

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 54／55
- 結果：五項全數落實。`axis-type-reverse-test` 之 FAIL 判準已改目的版，
  措辭版降為次要回報行，反向驗證兩版並增第七案。
  **軸 2 之 `none` 聲明已由「未實測之主張」改為「實測之 live PASS」**：
  9 條 TC 之可觀察量在 SYNC 指示上，**0 條未陳述該軸之值**。
  鏡面除霜三條件**第一項不成立，不增軸**，登 DR #40。
  `judged-at-tc-count` 已分兩欄，13 軸記 `unknown` 並具名其判定出處。
  批次 11 產 **36 條**（`-167`…`-202`），停下 6 leaf。
  lint **43/43 PASS，202 條**。ENTRY 008 已產出，3 項 FAIL 同源，不可交付。

---

## 0. 下放包五項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | FAIL 判準改目的版，措辭版降次要回報行；profile 同步並註明訂正出處；反向驗證兩版 | ✅ §1 |
| 2 | 對軸 2 逐條回報目的版結果，不先行改判類別 | ✅ §2 —— **0 違反**，類別未改判 |
| 3 | 查鏡面除霜之三條件，回報結論 | ✅ §3 —— 第一項不成立，DR #40 |
| 4 | `judged-at-tc-count` 分兩欄，無可考者記 `unknown` 並具名下放包編號 | ✅ §4 |
| 5 | 執行批次 11；`14.16.1` 後就 `122-02` 條件三逐句比對；先判 `15.1` 之性質 | ✅ §5 |
| — | 上繳 37 | 本件 |

---

## 1. 判準改為目的版

`lint_tcs.py` 之 `axis-type-reverse-test`：

```
FAIL   —— 任一條 TC，其可觀察量所在之介面會因某軸之某值而不存在，
           而該 TC 未陳述該軸之值。          ← 54 §1 目的版
次要行 —— 上列命中之中，其功能亦為該軸所轄者。 ← 52 §3 原措辭版
```

實作上只是把 function 過濾器由 FAIL 條件移到報告條件。
profile 之區塊說明已同步改寫並註明訂正出處（54 §1）與其理由
（35 §1.1 之目的 vs 52 §3 之措辭）。

**兩版並列而非擇一**，理由已寫入 profile：**日後若再發散，差異即是發現**。
本輪兩版皆為 0，其相等本身也是一項資訊。

### 1.1 反向驗證增第七案 —— 「措辭版是目的版之子集」

`verify_axis_type_gate.py` 增一案：對每個 live 軸，斷言
**措辭版命中 ⊆ 目的版命中**。這是「目的版為何是判準」的機械表述 ——
較寬者才能當 FAIL 判準；若哪天措辭版命中了目的版沒命中的東西，
那不是兩版之差，是實作錯了。

### 1.2 §7.2 之系統性複查由 gate 承擔

54 §1.1 裁定不另立一次性掃描。已照辦：目的版每次對全部 TC 執行。
本輪 202 條，0 違反。

**執行層自陳「運氣參與了 `-115`／`-117` 之發現」屬實**；
而 54 §1.1 指出「修正之後，運氣不再是必要條件」—— 這一句值得記，
因為它是「把一次修正做成一道 gate」的全部收益。

---

## 2. 軸 2 —— 目的版逐條結果：**0 違反，類別未改判**

依 54 §2「不先行改判類別」，本輪只做兩件事：**讓目的版跑得起來**，
然後**逐條回報**。

**讓它跑得起來**需要先宣告該軸所移除之介面。原區塊寫
`removed-interface: none`，而 `2.11` 之「Sync is not shown for single zone
climate configurations」確為介面後果，故改宣告為 **SYNC 指示**
（`"SYNC" button` / `SYNC button` / `Sync button` / `SYNC is on` /
`SYNC is off`），`axis-pc-keywords` 為 `not a single zone climate configuration`。

**逐條結果**（全 202 條，可觀察量含 SYNC 指示者 **9 條**）：

| TC | 節 | 帶軸 2 之 PC？ |
|---|---|---|
| `-053`／`-054` | 2.6.1 | ✅ |
| `-085` | 16.2 | ✅ |
| `-103`／`-104`／`-105` | 16.6／16.6.1 | ✅ |
| `-149`／`-150`／`-151` | 2.11 | ✅ |

**9/9 皆已陳述該軸之值，0 條違反。**

**故軸 2 之功能型判定獲實測支持** —— 但支持它的不是原本的理由。
原理由是「功能與觀察端同時消失」，那只對**以 SYNC 為功能**之 TC 成立；
目的版問的是**以 SYNC 指示為可觀察量而功能是別的**之 TC，
而 54 §2 點名的候選 `-053`／`-054`（其功能為**溫度連動**）**恰好早已帶著該 PC**。

> **一個「無」之聲明，其依據若只是判定者未想到反例，即非實測**（R-C37）。
> 現在它是實測了：9 條、0 違反、每次 lint 重跑。

`judged-at` 欄已記「`removed-interface` 於 54 §2 由 `none` 改為實測值」，
**類別欄未動**。

---

## 3. 鏡面除霜 —— 三條件第一項不成立，不增軸（DR #40）

實測（R-C30，全 129 節 pattern `MIRROR DEFROST|mirror defrost`，**5 句／4 節**）：

| 節 | 句 |
|---|---|
| `2.9` C8 | 「Rear Defrost automatically turns on EXTERIOR REAR-VIEW MIRROR DEFROST **if this feature available**」|
| `2.15` C16. | 「EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off state」／「… is independent of any other climate functions」|
| `16.15` ICE14 | 同 `2.15` 之兩句（其第二句拼作 `REAR-VIEWMIRROR`）|
| `16.9` ICE8 | **完全沒有鏡面除霜之句子** |

| 條件 | 結果 |
|---|---|
| 一、兩值逐字出現 | **❌** —— 正向值之字面只出現**一次**（2.9 之 `if this feature available`）；**否定值全語料零字面**（pattern `not (available\|present\|equipped).{0,40}mirror` 零命中）|
| 二、互斥且窮盡 | ✅（有／無為邏輯窮盡）|
| 三、非推論補齊 | ❌ —— 第二個值須由推論補齊 |

**不增軸。** 形態與 DR #38（dual airflow modes）**完全相同**。

### 3.1 不對稱是條文之實然抑或疏漏 —— 證據指向後者，但不代裁

54 §3 要求具名該不對稱之性質。實測所見：

- **擁有該功能之節**（`2.15`／`16.15`）**兩側皆無條件式陳述**
- **條件式只出現在引用它的那一節**（`2.9`），且**其 ch16 對造 `16.9` 連引用都沒有**

> 一個「可選配備」通常會在**定義它的那一節**帶配置條件，
> 而不是只在**引用它的那一節**帶。此處恰恰相反。

**這是指向「疏漏」的證據，但不是證明** —— 也可能該功能確為標配，
而 C8 之 `if this feature available` 是作者對「不是每台車都接了鏡面加熱」
的謹慎措辭。**兩者之處置不同**（前者須增軸並回補 `-165`／`-166` 之值，
後者維持現狀），故列 DR #40 待答，**不代裁**。

本輪處置維持：`-162` 帶該條件為 PC（條文自帶之情境條件，§8.5／R-C28 第二問），
`-165`／`-166`（2.15）**不補值**。

---

## 4. `judged-at-tc-count` 分兩欄

| 欄 | 語意 |
|---|---|
| `judged-at-tc-count` | **判定當時**之語料規模。無可考者記 `unknown` |
| `declared-at-tc-count` | **本聲明寫下時**之語料規模（現為 202）|
| `judged-at-provenance` | 無可考者，具名其判定所在之下放包 |

現況：**軸 16 記 124**（50 §1 判定當時，確實可考）；
**其餘 13 軸記 `unknown`**，各具名其出處 ——
軸 3 為 `43 §3`、軸 10／11 為 `29 §2`、軸 14 為 `37 §4`、軸 15 為 `39 §2`、
機型軸為 `14 §1`，其餘（軸 1／2／4／5／6／7／8）為
`profile §3.2 建檔時（15／16 §1），無單獨裁定包`。

**不以一個數字兼表兩義**（54 §4）。上一輪把補登時之 152 填進
`judged-at-tc-count`，那個數字讀起來像「以 152 條驗過」，而實際上
那 13 軸的類別是在語料只有十幾條時判的 —— **`unknown` 比一個好看的數字誠實**。

---

## 5. 批次 11 —— `Climate Popups`

### 5.1 產 36（`-167`…`-202`），停 6

23 節 / 42 leaf（framework.md 與 037 相符）。停下者四種成因，無一為新：

| leaf | 成因 |
|---|---|
| `14.1`（1）| 「follow the **pop-up list**」—— **外部文件**且從未入 `inputs/`（DR #11）。`[BLOCKED-SPEC]` 形態，白名單須裁（R-C26），形態同 `080-02` |
| `14.12`（3）| DR #37 之三問 |
| `14.14`（1）| **同時卡在兩個未登記之軸**：dual airflow modes（DR #38）＋ 螢幕尺寸（DR #6）|
| `14.15`（1）| 「Available comfort controls … **depend on vehicle configuration**」—— DR #32 之第四個成員 |

**`14.15` 值得單記**：它的 leaf 停下了，**而它的句子仍被引為第十六軸之出處**
（`14.16`～`14.18` 之 PC）。**一個 leaf 停下，不代表該節之句子不可作為他條
之出處**（R-C29）—— 兩者是不同層次的事，寫明以免日後誤刪該引用。

### 5.2 `15.1` 之性質 —— 先判再處置

**兼具兩種性質**：其「the HVAC pop ups displayed will **follow the chart
below**」為**對照表**（該表為圖片，A-CF23），而「all pop ups should display
current state of the HVAC systems (**not the exact pictures below**…)」為
**可驗之行為條文**。

**037 已把兩者分開**：其兩個 leaf（`105-01` 顯示當前狀態／`105-02` 圖為示例）
**皆屬後者**，**對照表本身沒有 leaf**。

故：**兩條皆生成**（`-201`／`-202`），而**對照表之缺口為 R-C16 形態**
（037 未產出該 leaf → 不產 workbook 列、不指派 tc_id、不入 coverage 分母）。
依 55 §1.1「**不得將表格內容當作行為驗證**」，本批**無任何一條**驗
「某功能進入時顯示某 popup」—— 那正是缺的對照。

### 5.3 `122-02` 之 R-C39 條件三 —— 逐句比對，**不成立**；但不升等

`14.16.1` 已生成，其三條 TC 之 ER 逐句比對：

| TC | ER 之內容 | 是否為 `configuration → icon` 之對照 |
|---|---|---|
| `-189` | 三態循環：both seat back and cushion → back only → cushion only | ❌ 狀態之循環 |
| `-190` | 圖示標為 `Zone` | ❌ 標籤文字 |
| `-191` | 座椅關閉時圖示變灰 | ❌ 關閉時之呈現 |

**無一句述及配置與圖示之對照。R-C39 條件三對本候選不成立。**

**惟 47 §1 之預裁觸發條件為「該二節生成後」，而另一候選 `12.3`
（Heated Vented Seats）尚未生成** —— 故**本輪不升 DR #32 之等級、不改
`122-02` 之處置**，其維持 `deferred`、不產列。已寫入 DR #32。

> 兩個候選中一個已測且失敗，另一個未測。
> **「一個失敗」不等於「兩個都失敗」**，而預裁寫的是後者。

### 5.4 第九軸首次以證據放下 —— 而非沿襲

本批 36 條中 **35 條不補第九軸之排除式 PC**，這是自 19 §2.1 立該軸以來第一次。

理由是條文自己給的：6.3 之移除對象為 head unit 之 comfort section，
**而其明文例外正是 `except for comfort popups`**。本批之可觀察量幾乎全是
popup，故在配備下螢幕之車上**仍然存在** —— 補排除即為過嚴（35 §1 之形態）。

**唯一之例外是 `14.13`**，它取該軸之**另一個值**：條文明文
「For vehicles with **a lower hvac screen**」，故其 PC 為**有**下螢幕。
**同一軸在同一批次內同時出現「不補」與「取正值」兩種用法**，
而兩者都不是排除式 —— 記此以免被讀成不一致。

### 5.5 R-C36-1 —— 全批同一答案，逐條記

`ch16_mirror_map.tsv` 之 **ch14 側全無列**（ch16 十八節無 popup 專章），
故 36 條之 `emea_ics_review` 皆為 `no-counterpart` / `yes`。

**仍逐條記而非節級記** —— R-C36-1 之要求是「預設不等於免答」，
一個全批相同的答案，其相同本身要看得見才算答過。

### 5.6 一項 037 之缺口，具名不吸收

`14.19` 之 `104-02` 只寫 `fan Speed Pop-up: **show**`，而條文為
「show for R1Low, **do not show for R1H**」—— **R1H 側沒有 leaf**。
依 R-C33 單位歸 037、依 §8.2.2 不自行增列，該缺口依 §8.4.2 於
`reasoning` 具名。`-196` 之 PC 因此取機型軸之 R1Low 值。

### 5.7 249 列 provisional 重新確認

批次 11 使 19 節落地，249 列到期（101 `deferred`／83 類級／65 `not-sibling`），
**全部逐對判完並清旗，verdict 全為 `not-sibling`**，無新 sibling。

ch2↔ch14 之 104 對佔最大宗，其分界一句話講得完：
**ch2 定功能於 climate 主畫面上之行為，ch14 定其 popup 之呈現條件** ——
本批之 ER 一律停在「popup 顯示／不顯示／自何處顯示」，
**刻意不驗該功能之行為規則**（§8.2.1），故與對造之 ER 無共用可觀察量。

`provisional` 現 `false` **536**／`true` 1132。

---

## 6. lint 與 §9 自評

```
43 / 43 gates PASS; 0 finding(s) across 202 TCs
```

TC 166 → **202**；leaf 161 → **197**；已生成節 50 → **69**。

**§9 十七項**：新增 36 條（批次 11）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition | 變 | 第九軸**取正值**（`14.13`）／第十六軸（`14.16`～`14.18`，出處 14.15）／機型軸 R1Low（`-196`）／`14.19` 之 widget 情境條件；＋軸 13＋EMEA。**第九軸之排除 35 條不補** |
| 5–8 | 步驟 | 變 | 每條 2–4 步，末步持驗證 |
| 9 | Baseline | 變 | `-167`／`-179`／`-185`／`-193`／`-201`／`-202` 需前後對照 |
| 10 | Procedure ↔ ER 1:1 | 變 | 36 條全數 1:1 |
| 11 | FP／FF | 變 | `-168`／`-176`／`-181`／`-197`～`-199` 為否定式（不顯示），各配正向步驟；`14.11` 兩條為同一規則之正反兩側 |
| 12 | 溯源、§8.2.1、§8.4 | 變 | 36 leaf 各溯其 037 req_id；6 leaf 停下；`14.19` 之 R1H 缺口與 `15.1` 之對照表缺口依 §8.4.2 具名 |
| 13 | Design Method | 變 | 35 條功能測試、`-189` 狀態轉換（三態循環）|
| 16 | `specification_reference` | 變 | 各條含自身節次＋2.14＋16.2；`14.16`～`14.18` 加 14.15（R-C29）|
| 17 | §8.6／§8.7 | 變 | `14.18` 之 5 秒為明值照用；`14.5` 之 `when permitted` 未定義故 ER 不宣稱許可條件 |
| 其餘 | — | 不變 | |

---

## 7. 「本包是否仍有該驗而未驗者」（R-C30）

1. **批次 11 之 36 條未經 §7 之 FP／FF 人工複核**，只經 lint。
2. **本批有六節之步驟含未定義之入口**（RVC 畫面、simulated off/idle 模式、
   第三方 App、intro 動畫、「另一個 popup」、Climate widget 之顯示）。
   前四者已併入 DR #34 之 `entry` 子類**於 reasoning 具名**，
   **但未逐一補入 DR #34 之成員清單** —— 該清單現仍只列三例。
3. **`14.6`／`14.7`／`14.8` 三節之「另一個 popup」不指名**，
   故三條之可執行性依賴測試員自行挑一個 popup。
   **若不同測試員挑到不同 popup，三條之結果可能不可比** —— 未開 DR。
4. **`15.1` 之對照表缺口記為 R-C16 形態，但未登入任何 DR** ——
   R-C16 之覆蓋缺口項清單（profile §5.4）現仍只列 `16.1`／`18.2`–`18.4`。
5. **軸 2 之目的版依賴我所選之五個關鍵詞**（`"SYNC" button` 等）。
   若某條 TC 以別的措辭描述同一指示，該條不會被找到 —— **關鍵詞法之固有限制**，
   與 R-C37 同源，記之。
6. **`declared-at-tc-count` 全批一律更新為 202**，包括那些聲明內容未變者 ——
   該欄現在記的是「最近一次全量更新之時點」而非「該聲明寫下之時點」，
   **與 §4 所定之語意有落差**。

---

## 8. 建議 commit message（git 未執行）

```
feat(comfort): batch 11 Climate Popups; purpose-version reverse test

- axis-type-reverse-test's FAIL criterion becomes the PURPOSE version (54
  §1): any TC whose observable sits on an interface some axis value removes
  and which does not state that value. The 52 §3 wording version drops to a
  named report line — kept, not deleted, so a future divergence is visible
- its reverse validation gains a seventh case: the wording version must be a
  SUBSET of the purpose version. That is the mechanical statement of why the
  wider one is the criterion
- axis 2 declared its removed interface (the SYNC indicator) so the purpose
  version could actually run: 9 TCs observe it, 0 without the axis value.
  The `none` claim becomes a measured live PASS. Class NOT re-judged, per
  54 §2 — and note the original reason ("function and observable vanish
  together") only covered TCs whose function IS SYNC, which is not what the
  purpose version asks
- mirror defrost is NOT registered as an axis: its positive value appears
  once (2.9's "if this feature available") and its negative nowhere in 129
  sections. The asymmetry points at an omission — the section that DEFINES
  the feature carries no condition while the one that CITES it does — but
  that is evidence, not proof, so DR #40 asks rather than decides
- judged-at-tc-count splits in two. 13 axes now read `unknown` with their
  handoff named: the class was judged when the corpus was a dozen TCs, and
  `unknown` is more honest than a tidy 152
- batch 11: 36 TCs, -167..-202, 6 leaves stopped. 15.1 was CLASSIFIED before
  its leaves were decided: it is both a chart and a behaviour clause, and
  037 already split them — its two leaves are the residue, the chart has no
  leaf, so the chart is an R-C16 gap and no TC verifies the mapping
- 122-02's R-C39 condition three tested against 14.16.1 at last: it fails.
  DR #32 is NOT escalated, because 12.3 — the other candidate — does not
  exist yet, and "one failed" is not "both failed"
- axis 9's exclusion is dropped on evidence for the first time: 6.3's own
  wording excepts comfort popups, which is what this batch observes. 14.13
  takes the axis's other value instead, in the same batch
- lint 43/43 PASS across 202 TCs; ENTRY 008, same three template FAILs. The
  P-column gap is now 200 rows — DR #35's cost grows per batch, not once
```

---

## 9. 待分析層

1. **§7.2** —— 本批六節之未定義入口是否逐一補入 DR #34 之成員清單。
2. **§7.3** —— 「另一個 popup」不指名，三條之結果可比性；是否開 DR。
3. **§7.4** —— `15.1` 之對照表缺口是否登入 profile §5.4 之 R-C16 清單。
4. **§7.6** —— `declared-at-tc-count` 之語意（最近更新 vs 寫下時點）。
5. **DR #40** —— 鏡面除霜之不對稱屬實然抑或疏漏。
6. **DR #35 / A-CF26** —— 範本容量：現 202 列，200 列無 P 下拉。
   **缺口隨批次線性成長**，不是固定成本。
7. **批次 12 之授權**；剩餘最大者為 `Heated Vented Seats`（59 leaf，
   其存廢待 DR #11）與 `Rear Climate`（46 leaf，待 DR #31 使 ch2 到位）。
