# 31 — Comfort HMI / provisional 回訪、deferred 入表、037 已讀

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 42
- 結果：六項全數落實。`pending_sibling.tsv` 由 689 列重建為 **1592 列**，
  加 `provisional` 欄；`provisional-sibling` gate 已就位並經**反向驗證五案全過**，
  於本輪**如設計般 FAIL（632 列）**。**037 已可讀**，25 個帶圖 leaf 名單重建
  —— 已生成者實為 **7 個而非 2 個**，補齊後全 12 條 TC 複查完畢。
  第三軸**三項條件缺第二項，未改**。DR 開至 **#30**。
  lint **41/42 gates PASS，81 條，1 finding**（即上述設計中之 FAIL）。**未寫回。**

---

## 0. 下放包八項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 加 `provisional` 欄，擴充 gate，反向驗證 | ✅ §1 —— gate 如設計 FAIL；**其觸發時點有一項設計問題**，見 §1.3 |
| 2 | 產生器改全量重建 ＋ 鍵合併，回報列數與分布 | ✅ §2 |
| 3 | 查第三軸第三值，三項齊備方改 | ✅ §3 —— **缺第二項，未改**；且預期之 gate 動作**不會發生**，見 §3.3 |
| 4 | 重試 037，失敗回報錯誤全文 | ✅ §4 —— **成功**。先前之「不可達」為我方搜尋深度不足，登 A-CF24 |
| 5 | 開五項 DR，tri-mode 交叉具名 | ✅ §5 —— 開 #25 ~ #30（四項新開＋兩項本輪查出），第五項為 #21 之方向訂正 |
| 6 | R-C36-1 加旁註（不改原文） | ✅ §6 |
| 7 | 全批重跑 lint 與 §9 自評；不寫回 | ✅ §7／§8 |
| 8 | 上繳 31 | 本件 |

---

## 1. `provisional` 欄與 `provisional-sibling` gate

### 1.1 欄之語意與其單向性

`pending_sibling.tsv` 加第四欄 `provisional`（`true`／`false`），
置於 `verdict` 之後。判定規則寫在 `sibling_candidates.py` 之
`provisional_of()`：

```
verdict ∈ {deferred, not-broken-by-3-samples (class)}  → 恆為 true
否則（已逐對判定者）：
    既有值為 false                                      → 維持 false
    否則                                                → 兩側皆已生成 ? false : true
```

兩項偏離下放包字面之處，理由如下：

**其一，類級 verdict 恆為 true。** 42 §1 之規則按兩側生成狀態決定，
而 `not-broken-by-3-samples (class)` **從未逐對判定過**（41 §4）。
若其兩側恰皆已生成即得 `false`，等於宣告「不必再看」——
與 41 §4「類級判定不因曾通過而免除」直接衝突。實測有 17 列落在此情形。

**其二，`false` 單向不可逆。** 全量重建每輪重算 `provisional`；
若照生成狀態無條件重算，人工重新確認後寫下的 `false`
會被下一次重建改回 `true`，**gate 因而永遠無法被滿足，而那份人工複核不留痕跡**。
故一旦為 `false` 即維持。

### 1.2 gate 與其反向驗證

`lint_tcs.py` 增 `provisional-sibling` gate（第 42 道）。判準：
某 Test Set 之全部節次皆已生成（＝該組完成）時，
凡任一側屬該組且 `provisional == true` 之列，FAIL，訊息列出對與現行 verdict。

**反向驗證**：`scripts/verify_provisional_gate.py`（新增，可重跑）。
它 import `lint_tcs` 本身，用的是**出貨的那個 map 與那份 generated/ 掃描**，
不是重寫一份判準。五個方向性案例：

```
PASS — provisional row touching a completed set: fired=True, expected=True
PASS — same row, provisional cleared by re-confirmation: fired=False, expected=False
PASS — provisional row touching NO completed set: fired=False, expected=False
PASS — sibling verdict is not exempt — the flag, not the verdict, decides: fired=True, expected=True
PASS — the completed set may be on EITHER side: fired=True, expected=True

5 / 5 directional cases PASS
```

**一道從未見過紅燈的 gate，等於沒被驗過** —— 條件接錯與條件被滿足，
印出來的綠色是同一種綠色。故反向驗證同時斷言「該響時響」與「不該響時不響」。

### 1.3 gate 於本輪 FAIL —— **632 列**，且其中**可用新證據者為 0**

五組已完成：`ECO HVAC`／`Front Climate Anatomy`／`Seat Control Tab`／
`Temperature and Fan`／`Tri-Mode Climate`。應重新確認者 632 列：

| verdict | 列數 |
|---|---|
| `not-sibling`（逐對）| 399 |
| `not-broken-by-3-samples (class)` | 224 |
| `sibling` | 9 |

**但這 632 列之中，兩側皆已生成者為 0。**

這是本節最重要的一個量測，它指出 42 §1 之觸發時點有一項設計問題：

> `provisional == true` 的**成因**是「某一側未生成」。
> gate 卻在**任一側**之組完成時觸發。
> 而會觸發的那一側，正是**已經生成**的那一側 ——
> 缺的那一側仍然缺。

故此刻要求的「重新確認」，其可用證據與當初判定時**完全相同**。
再看一次不會看到新東西；能寫下的只有一個橡皮圖章。
**42 §1 明言「重新確認得維持原 verdict」，但那預設的是「有新東西可看而看完仍維持」，
不是「沒有新東西可看」。**

**可能之修正（未做，待裁）**：觸發條件改為
**「該列中原本未生成的那一側，其所屬組完成之日」**。
資料已足以判定（`provisional == true` 且兩側皆已生成 ⇔ 缺的那側已補上）。
此改動會使本輪之 632 降為 0，並在 `Climate Modes`／`Rear Climate` 等組完成時
按對造逐批到期 —— 那才是 42 §1 所要的那個時點。

**本輪未改**：42 §1 之措辭明確，改觸發條件是改裁定而非落實裁定。
lint 之紅燈如實留著。

### 1.4 能做的部分已做 —— 17 列已逐對判定並清旗

632 列中，**兩側皆已生成而 `provisional` 仍為 true 者共 17 列**，
全部是 §1.1 第一項所留的類級列。**它們正是唯一有新證據可用者**：
兩側都有 TC，而類級判定從未逐對看過。已逐對判完並清為 `false`。

**這 17 列查出兩項條文缺口與一項 §4.5 風險**，皆為類級判定看不見者：

| 對 | 所見 |
|---|---|
| **`2.7.1 ↔ 3.2`** | C20 把 MAX DEF 之最高風速寫死 `highest setting (7/7)`，而 C6.1 明載某些車輛為 `Off, **1-8**`。**已生成之 `NR1L-ComfortHMI-019` 之 ER 現寫 `(7/7)`** —— 若 1-8 車上應為 8/8，該 ER 為錯判。→ **DR #29（High）** |
| **`2.6 ↔ 2.14`** | C5 明寫 `for **ATC** systems`；C15 只說 MTC「缺離散溫度設定與 Auto 控制」，**未說 MTC 的溫度呈現是什麼**。第一軸之 MTC 值於全 feature 無行為條文。→ **DR #30** |
| **`2.2 ↔ 2.7`** | C1「according pop-ups are shown if NOT on climate screen」與 C6「Show pop-up when status is changed via hard control and currently shown screen is not climate screen」是**同一規則之通則與其風速特例**。非 sibling（無軸），**但驗 C6 popup 之 TC 同時滿足 C1 該句 —— 兩 leaf 共用一組可觀察量（§4.5 風險）** |

`2.7.1 ↔ 3.2` 這一項尤其值得記：它影響的是**一條已經寫好、已經 lint 通過的
TC 之 ER**。類級判定把它歸進 `FAN` 類、標「三對抽樣未破」，
就這樣蓋住了一個 High。**42 §1 的機制在啟用當天就抓到了一個實質缺陷。**

---

## 2. 全量重建 ＋ 鍵合併

`sibling_candidates.py` 加 `--rebuild`。三項設計：

1. **`--rebuild` 與 `--for` 互斥，同時給即 ABORT。** 受限的重建會寫出一份
   **被截斷**的表，而截斷後看起來就像「沒有候選」——
   與 39 §4.1 之「靜默丟棄」同一種失敗形態。
2. **鍵為無方向對** `(節A, 節B)`（依節次數值排序）。舊表由不同輪次寫入，
   兩側順序不一致；有方向鍵會把同一對複製成兩列。
3. **已判定之列若不再是候選，不刪、保留並具名回報。** 判定是人的工作，
   它的消失不該是無聲的。

### 2.1 重建結果

```
rebuilt pending_sibling.tsv: 1592 rows
  carried over (no longer a candidate)   1
  kept                                   688
  new deferred                           903
```

| verdict | 列數 |
|---|---|
| `deferred` | **903** |
| `not-sibling` | **454** |
| `not-broken-by-3-samples (class)` | **224** |
| `sibling` | **11** |
| 合計 | **1592** |

| `provisional` | 列數 |
|---|---|
| `true` | **1537** |
| `false` | **55** |

（`not-sibling` 454 = 437 ＋ §1.4 之 17；類級 224 = 241 − 17。）

**冪等性已實測**：連跑兩次，檔案 md5 相同（`16cc3298…`），
且 §1.4 人工寫下之 17 個 `false` 於重建後保留。

### 2.2 那 1 列「不再是候選」者 —— `3.2 ↔ 10.3`

舊表有此列（`not-sibling`，理由記「僅高頻詞 AUTO 重疊」），
新候選集 1591 對中沒有它。實測其成因：

```
3.2  之 token: A/C AUTO FAN FRONT DEF HI MAX A/C MAX DEF MODE REAR DEF RECIRC SYNC TEMPERATURE
10.3 之 token: AUTO ECO
交集: []
```

`VOCAB` 之 alternation 把 `AUTO ECO` 排在 `AUTO` 之前，
故 `10.3`（EH3「Button label will read AUTO ECO」）全句**只吐出 `AUTO ECO` 一個 token，
不吐 `AUTO`**。於是任何「AUTO 相關語句只寫 `AUTO ECO`」之 ch10 節，
與任何寫 `AUTO` 之 ch2／ch3 節，**在詞彙層永遠不會配成對**。

**這是 R-C37 所警告的不完備性，第一次量到具體實例。**
可能之修正是讓 `AUTO ECO` 同時發出 `AUTO`（層級關係而非同義詞），
**未改** —— 改詞彙集會改變整個候選集，屬裁定形狀之變更，不自取。

### 2.3 `deferred` 903 列之意義

規則三現在有對象了。903 列皆為「兩節皆未生成」之對 ——
上繳 30 §3.1 所說「不在表中因而不可見」的那些，現在在表中。
它們與 689 列時代的差別不是判定，是**可見性**：
`sibling_candidates.py` 之輸出現在對每一對都印一個 verdict，
而 `UNJUDGED` 這個狀態消失了 —— 因為沒有一對是表外的。

---

## 3. 第三軸之第三值 —— **三項缺第二項，未改**

### 3.1 逐項核對

| 條件 | 結果 | 依據 |
|---|---|---|
| 一、第三值在條文中**逐字出現**，具名節次與句 | ✅ | `2.12`（C13）「There are **4 Airflow Mode** displayed in this order (1) Face, (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield」／`2.12.1`（C13.0）「In some non-tri mode equipment types, airflow modes has **5 states** (1.Face, 2.Mix of Face & Feet, 3.Feet, 4.Mix of Feet & Windshield, 5. Windshield)」／`3.1`（C19）「On vehicles with Tri-Mode climate, there are **3 airflow mode buttons** … which provides **7 possible distribution modes**」 |
| 二、與現有二值**互斥且窮盡**，或條文明示其為**第三種並列情形** | ❌ | 見 §3.2 |
| 三、三值皆非由推論補齊 | ✅ | 三句皆為條文原文，無一項為推得 |

### 3.2 第二項為何不成立

現行第三軸為 **「tri-mode 有無」**，其二值為 `有`／`無`——**一個布林軸**。

而 C13.0 之「5 states」開頭即寫 `In some **non-tri mode** equipment types`：
**它是 `無` 這個值的下位切分，不是 `有`／`無` 的第三個並列項。**
以它作第三值，等於把一個子集和它的父集並列。

- **互斥**：❌ —— `5 states 非 tri-mode` ⊂ `tri-mode 無`
- **明示為第三種並列情形**：❌ —— 條文明示的是「它在 non-tri-mode 之內」，
  恰恰是並列的反面

**故真正的發現不是「這個軸多了一個值」，而是「這個軸問錯了問題」。**
可觀察量是**氣流模式集合**，其值為三：4 模式／5 狀態／tri-mode 7 組合。
把它寫成 `tri-mode 有無` 的布林，就沒有位置可以放 C13.0。

**這不是加值，是換軸。** 42 §3 授權的是「三項齊備即自行增值（客觀條件）」，
換軸不在其內，故**不改**，回報。

（旁證：`16.12`（ICE11）之 EMEA ICS 側同樣是 `Airflow Modes has 5 states`，
`ch16_mirror_map.tsv` 記 `16.12 ↔ 2.12.1` 為 `mirrored`。
5 狀態這個配置橫跨兩套介面，更說明它不是「tri-mode 有無」的一個值。）

### 3.3 更要緊的一項：預期之 gate 動作**不會發生**

42 §3 預告「`axis-value-count` gate 屆時將 FAIL，65 條 negation users 必須複核」。
實測**兩項前提皆不成立**：

**其一，`axis-values` 區塊盯的是第十三軸，不是第三軸。**
profile 內 ```` ```axis-values ```` 區塊全檔**只有一個**，其首行為
`axis: 13  HVAC 實體控制型式`。那 65 條 `negation-users` 是
`does not have 3 knob HVAC controls with ICS` 的使用者，**與 tri-mode 無關**。
改第三軸不會使該 gate 有任何反應。

**其二，第三軸根本沒有否定式 PC。** 實測全 81 條之 235 行 pre_conditions：

| 否定式 PC | 條數 |
|---|---|
| `does not have 3 knob HVAC controls with ICS`（軸 13）| 65 |
| `is not an EMEA ICS vehicle`（EMEA 軸）| 40 |
| `not configured with a non-foldable secondary lower screen`（軸 9）| 9 |
| `is not a single zone climate configuration`（軸 2）| 2 |
| 其餘（test-setup 與單節事實）| 4 |

tri-mode 出現於 PC 者只有三行，且**全為肯定式**：
`[spec-verbatim] The vehicle is equipped with Tri-Mode climate (3.1)`
（`-015`／`-016`／`-017`）。

35 §4 所治的是「否定式 PC 的涵蓋隨軸值增加而悄悄變動」。
**第三軸沒有否定式 PC，該失敗形態在此軸上沒有附著點。**

> 42 §3 稱該 FAIL 為「本輪最值得看的一次 gate 動作」。
> 實測結果是：**它不會動**。而這件事本身比它動了更值得看 ——
> 一個為「軸增值」而設的機制，只接了 15 條軸裡的 1 條。
> 其餘 14 條軸增值時，沒有任何東西會響。

**未改 profile、未動 `negation-reviewed-at-value-count`、未複核 65 條**
（無觸發理由；65 條屬第十三軸，本輪該軸未變）。
是否把 `axis-values` 機制推廣到其他有否定式 PC 之軸（EMEA 40 條、軸 9 的 9 條、
軸 2 的 2 條），**待裁**。

---

## 4. 037 —— 已讀，先前之「不可達」是我方搜尋深度不足

`features/comfort/inputs/FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
**143,292 bytes，與下放包所載一致**。`openpyxl` 開啟成功，
`Analysis Report` 工作表 571 列 × 20 欄，資料自第 8 列起。
**無錯誤訊息可報 —— 本輪讀取成功。**

### 4.1 先前為何零命中（A-CF24）

上繳 30 §5.3 記：「`find . -maxdepth 3 -name "*037-A03*"` 於 repo root 零命中」。
**pattern 正確，深度不足**：實際路徑為
`./features/comfort/inputs/…`，深度為 **4**。
另一次嘗試是在 repo root 執行 `ls inputs/`，而 `feature.yaml` 之 `paths`
以 **feature 目錄**為起點。兩次都錯在位置，不在檔案。

**R-C30 的價值在這裡實測到了**：因為當初把根目錄與 pattern 都寫進上繳包，
現在一眼就看得出錯在深度而不是檔名，不必重猜一輪。
登 **A-CF24**（RESOLVED）。

### 4.2 名單重建 —— 已生成者是 **7 個**，不是 2 個

實測 037 之 129 個 parent 列（圖片標記位於 section 級 Requirement
Description，與 outline 節次 1:1）：**25 個 leaf、52 個標記**
—— 與 29 §5 之數字一致。但**「已生成者為 `-023` 與 `-076` 兩個」是錯的**：

| leaf | 圖 | 節 | Test Set | 先前是否複查 |
|---|---|---|---|---|
| `SWE1-HVAC-023` | 6 | 3.1 | Tri-Mode Climate | ✅ |
| `SWE1-HVAC-001` | 3 | 2.1 | Front Climate Anatomy | ❌ **漏** |
| `SWE1-HVAC-044` | 3 | 10.1 | ECO HVAC | ❌ **漏** |
| `SWE1-HVAC-045` | 3 | 10.2 | ECO HVAC | 部分（A-CF23 已載 `-068`）|
| `SWE1-HVAC-010` | 1 | 2.7 | Temperature and Fan | ❌ **漏** |
| `SWE1-HVAC-053` | 1 | 10.9.1 | ECO HVAC | ❌ **漏** |
| `SWE1-HVAC-076` | 1 | 13.2 | Seat Control Tab | ✅ |

**已生成之帶圖 leaf 共 7 個、18 張圖、12 條 TC。** 本輪補齊四個漏掉者：

| TC | 答 | 依據 |
|---|---|---|
| `-042`（2.1）| 否 | 所驗者為「tab 一個都不顯示」，判讀只需認得 tab 之有無 |
| `-059`…`-063`（2.7）| 否 | `fan segment`／`one bar highlighted`／`all FAN bars grayed out`／`main category control`／`pop-up` **五個可觀察量全是 C6 自己的字** |
| `-067`（10.1）| 否 | 「AUTO ECO 為作用中」之判讀依據在 **10.3**（EH3「Button label will read AUTO ECO」，已由 `-069` 涵蓋），是條文非圖片 |
| `-081`（10.1）| 不適用 | `[BLOCKED-NON-HMI]` row，procedure 與 ER 皆空 |
| `-079`／`-080`（10.9.1）| 否 | ER 驗 EH9.1 書名號內兩段文字**逐字出現**，文字在條文內 |

**`-042` 之答另有一層，值得記**：`2.1` 的三張圖對**已生成**的 `-03` 不構成
依賴，但對**未生成**的 `-01`（tab 數）與 `-02`（順序）極可能是關鍵 ——
那兩者所缺的正是「哪一種配置產生哪一組 tab」（DR #17）。
**圖片之影響不隨 leaf 均勻分布，同一節之內即可分歧**，
故生成時之必答項掛在每條 TC 上，不掛在節上。

其餘 **18 個未生成之帶圖 leaf（34 張圖）** 之具名清單已寫入
`ANOMALIES.md` A-CF23 與 `data/image_leaves.json`（25 筆，含已生成者）。
分布最重者為 `Heated Vented Seats`（5 leaf）與 `Climate Popups`（5 leaf）。

---

## 5. DR —— 開至 #30

30 §6 之五項，處置如下（每項含所在節、缺什麼、**為何不由本 feature 補**）：

| 30 §6 | DR | 處置 |
|---|---|---|
| a AUTO ECO 是否及於後排 | **#25** | 新開，Medium |
| b widget 顯示中之 AUTO ECO 回饋 | **#26** | 新開，Medium |
| c tri-mode 車上 AUTO 與七組合之互斥 | **#27** | 新開，Medium，**交叉具名** |
| d 後排 A/C 與 AUTO 之關係 | **#28** | 新開，Medium |
| e 前排 long press 門檻無值 | — | **已為 #21，不重複開**；於 #21 內補「方向訂正」段 |

**第五項不另開，是因為開了就會有兩個編號問同一件事。**
#21 原記「後排有值可參考」；`ch2_ch7_mirror_map.tsv` 建成後看清楚的是
**前排缺值** —— `7.4` 是同一需求在後排側的完整陳述，`2.6.1` 才是不完整的
那一側。問題不是「要不要借後排的值」，而是「前排為何沒有值」。
該段已寫入 #21。

另新開兩項，皆由 §1.4 之 17 列重新確認查出：

| DR | 內容 | Urgency |
|---|---|---|
| **#29** | `MAX DEF` 之「最高風速」於 `Off, 1-8` 車輛為 7/7 抑或 8/8 —— **影響已生成之 `-019` 之 ER 正確性** | **High** |
| **#30** | MTC 車輛之溫度呈現行為全 spec 未述 —— 第一軸之 MTC 值無附著點 | Medium |

### 5.1 #27 之交叉具名

DR #27 內明載：本項與 `data/pending_sibling.tsv` 之
`2.12 ↔ 3.1`／`2.12.1 ↔ 3.1`／`2.12.2 ↔ 3.1` 三對 `sibling`
**為同一事之兩面** —— 既然氣流模式集合是同一需求的三個配置值
（C13 四模式／C13.0 五狀態／C19 tri-mode），
C2 對「四模式」宣告的互斥就應有 tri-mode 側的對應物，而條文沒有。
兩者**不分開登**：sibling 判定說的是「這三節在講同一件事」，
DR #27 說的是「那件事的一個面向只在其中一節被講到」。

本項亦與 §3.2 之軸判定同源，已於 DR 文字內指出。

---

## 6. R-C36-1 之旁註

依 42 §6 寫入 `RULINGS.md` R-C36-1 條文區塊之後，**原文一字未改**，
以引言區塊標示為旁註：

> R-C36-1 適用於**任何**以節級對應強度支持 TC 級判定之情形，
> 含 `ch2_ch7_mirror_map.tsv` 及日後新建之任何對應表。
> 節級強度提供預設與證據出處；TC 級問句不因之免除。
>
> 理由：R-C36-1 之措辭為「不論節級鏡射強度為何」，其約束對象是
> **「以節級強度支持 TC 級判定」這個動作**，不是 ch16 這張表。
> **條文之適用範圍由其理由決定，不由其首次適用之對象決定。**

並具名三列受影響者：`7.2↔2.3`、`7.7↔2.11`、`7.8↔2.12`，
於 `Rear Climate` 生成時須逐條問。

---

## 7. lint 與 §9 自評

```
41 / 42 gates PASS; 1 finding(s) across 81 TCs
[FAIL] provisional-sibling: 632 provisional row(s) touch a completed Test Set …
```

gate 數由 41 增為 **42**。唯一之 FAIL 即 §1.3 所述，**是本輪新裝之 gate 依
42 §1 之字面條件如實觸發**，非既有缺陷。TC 81 條、leaf 76，**數量未變**。

**§9 十七項之變動**：本輪**未新增、未刪除、未修改任何 TC 之內容** ——
PC／procedure／ER／test_item 全數未動。變動僅及四個 `reasoning`
（`SWE1-HVAC-001`／`-010`／`-044`／`-053`，各補一段 A-CF23 逐條複查之答）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 12 | 溯源、§8.2.1、§8.4.2 | 變 | 四個 `reasoning` 依 §8.4.2 具名圖片依賴之有無；`-044` 另具名 10.3 為 AUTO ECO 判讀之出處（跨節取據之陳述，非驗證範圍擴張）|
| 其餘 16 項 | — | 不變 | 無 TC 內容變動 |

**未寫回**（42 §7）。`write_back.py` 未執行，工作簿未動。

---

## 8. 「本包是否仍有該驗而未驗者」（R-C30）

1. **`provisional-sibling` 之觸發時點錯邊**（§1.3）。632 列到期而 0 列有新
   證據。**這是本包最大的未決項**，且它是裁定層之措辭問題，不是落實問題。
2. **632 列未清旗。** 能清的 17 列已清；其餘 615 列若無 §1.3 之修正，
   只能以橡皮圖章清除，而那會使旗標失去意義。**刻意不清。**
3. **第三軸未改，且應改的可能是「換軸」而非「增值」**（§3.2）。
   換軸之影響未評估：`-015`／`-016`／`-017` 之肯定式 PC 是否需改寫、
   `2.12`／`2.12.1` 生成時之 PC 形態為何，皆未做。
4. **`axis-values` 機制只接了 15 條軸中的 1 條**（§3.3）。
   EMEA（40 條否定式 PC）、軸 9（9 條）、軸 2（2 條）皆無此保護。**未擴充。**
5. **`AUTO ECO` 不吐 `AUTO`**（§2.2）。候選產生器對「只寫 AUTO ECO 之節」
   與「寫 AUTO 之節」永遠配不成對。已量到，**未改**。
6. **903 列 `deferred` 全未判定。** 依 41 §3 規則三，其所屬組生成之日判。
   本輪只讓它們可見，沒有讓它們變少。
7. **18 個未生成帶圖 leaf 之圖片內容仍讀不到**（A-CF23 / DR #23）。
   名單有了，圖還是沒有。
8. **DR #29 影響一條已交付之 ER**（`-019` 之 `(7/7)`）。
   本輪依 §8.4.1 未改該 ER（改成 8/8 或「最高設定」皆為造值或弱於條文），
   **風險留在表上，未消除**。

---

## 9. 建議 commit message（git 未執行）

```
feat(comfort): provisional flag, full-rebuild sibling table, 037 re-read

- add a `provisional` column: a verdict reached against a section that had
  no TCs is flagged, and clearing it is by hand. Class-level verdicts are
  永遠 provisional (they were never judged pair-by-pair) and a cleared flag
  survives rebuilds, or the gate could never be satisfied
- new gate `provisional-sibling` (42nd), with verify_provisional_gate.py
  asserting BOTH directions — a gate never seen red has not been tested
- it FAILs on 632 rows, as designed. Measured: 0 of them have both sides
  generated, so the re-confirmation it asks for has no new evidence. The
  trigger should be the counterpart's set completing, not either side's
- sibling_candidates.py --rebuild: whole-corpus, merged on an undirected
  key, idempotent. 689 -> 1592 rows, 903 of them the deferred pairs that
  rule three had no way to reach. One judged pair survives as no-longer-a-
  candidate: 3.2<->10.3, because "AUTO ECO" never emits "AUTO"
- judge the 17 class rows whose both sides are generated. Two spec gaps and
  one §4.5 risk fall out, including MAX DEF's hard-coded 7/7 against C6.1's
  Off,1-8 — which makes a shipped ER (-019) wrong on those vehicles
- third axis NOT changed: C13.0's "5 states" is a subdivision of "not
  tri-mode", not a third peer. And the axis-value-count gate watches axis
  13, not axis 3, which has no negated PC at all — the predicted FAIL
  cannot fire
- 037 is readable at features/comfort/inputs/ (143,292 bytes). The earlier
  "unreachable" was a maxdepth-3 find against a depth-4 path — A-CF24.
  Rebuilt the image list: 7 generated leaves, not 2; all 12 TCs reviewed
- open DR #25..#30; #21 gains a direction correction instead of a duplicate
- side-note on R-C36-1: it binds the ACT, not the ch16 table
- lint 41/42 PASS across 81 TCs; no write-back
```

---

## 10. 待分析層

1. **§1.3** —— `provisional-sibling` 之觸發改為「對造側之組完成之日」？
   （改後本輪 632 → 0，並在對造組完成時按批到期。）
2. **§2.2** —— `AUTO ECO` 是否應同時發出 `AUTO`（層級而非同義）。
3. **§3.2** —— 第三軸為「換軸」而非「增值」：
   是否把「tri-mode 有無」改為「氣流模式集合（4／5／tri-mode）」三值軸。
4. **§3.3** —— `axis-values` 機制是否推廣至其餘有否定式 PC 之軸
   （EMEA 40／軸 9 的 9／軸 2 的 2）。
5. **DR #29（High）** —— 在其解答前，`-019` 之 ER 維持 `(7/7)` 是否可接受。
6. **批次 6 之授權**（42 §8 末）。
