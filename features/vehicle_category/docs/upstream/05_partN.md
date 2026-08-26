# 上繳包 05 —— Vehicle Category：DECISIONS 送簽稿 + Part N 提案覆核（T31–T34）

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層 / Pei
- 對應下放：`docs/handoff/05_partN.md`
  （SHA256 `693f7b8f44d115316bdb5322e36de2800578d0d5679f9f3dfd4e904f9c4bede3`，10,626 B）
- 前一包上繳：`docs/upstream/04_priority.md`（commit `ecee654`）
- **結論：T31／T32 完成。T33／T34 待簽，未執行。**
- 未產出任何 TC、未簽署、未合併 `DECISIONS.md`、未修 `recon.py`、
  未寫 `framework.md`、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | Tier | 結果 |
|---|---|---|---|
| T31 | A-VC11 登記 | 1 | ✅ 條文逐字（sha `6502cddb4dd8c9bc`）；跨 feature 範圍已查證 |
| T32 | `DECISIONS` 送簽稿 | 1 | ✅ `docs/DECISIONS_signoff_draft.md`（133 行），`DECISIONS.md` 未動 |
| T33 | `framework.md` + 二張 map | 2 | ⏸ **待簽，未執行** |
| T34 | `verify_partn.py` | 1 | ⏸ **隨 T33，待簽，未執行** |
| §四.4 | 8 組 leaf 數獨立重測 | — | ✅ **8/8 相符**，section 66/66，覆蓋無洞無重 |
| §四.5 | `Sub Categorization` 獨立重測 | — | ✅ 章 11 為唯一混章，切分連續、**切換次數 = 1** |

**一項須更正**：下放包 05 §2.3 之「章 13 全 16 筆…**恰等於** FROP =
Power Management 之 16 筆」—— 兩個 16 是**不同母體**的數字巧合。
其所導之結論（表 A ↔ Test Set #6 一對一）**仍然成立**，
但理由不成立。詳見 §4.3。

---

## 1. T31 —— A-VC11

條文逐字抄入 `ANOMALIES.md`。

```
$ diff -q <(sed -n '44,61p' docs/handoff/05_partN.md) <(自 ANOMALIES.md 取回 A-VC11 fence)
（無輸出）
A-VC11 逐字一致  bytes=920 lines=18 sha=6502cddb4dd8c9bc
```

同輪複驗前包之二筆，亦逐字一致：**A-VC9**、**A-VC10**。

### 跨 feature 範圍之查證（條文所稱「非本 feature 獨有」）

```
$ grep -n "spec_reference_template" features/*/feature.yaml
features/display/feature.yaml:110:spec_reference_template: null   # mode D：spec_reference 為查得，非構造（canon §3）
features/vehicle_category/feature.yaml:41:spec_reference_template: null
（其餘 10 個 feature 皆為非 null 之字串）
```

**12 個 feature 中恰有 2 個宣告 null** —— 條文所稱之範圍成立，且已窮舉。

症狀亦已在 display 上實測到：

```
$ grep -n "spec_reference" features/display/DECISIONS.new.md
33:- spec_reference: [PROPOSED: None]
```

### 一項前例，值得記入

`display` 遇到同一症狀時之處置記於 `features/display/DECISIONS.md:211`：

> `spec_reference` | `[PROPOSED: None]` | **`[PEI]`** | **維持 `[PEI]`，拒絕降格**。
> recon 之值係依 `spec_reference_template` 為 null 之機械讀出；
> 本檔之 `[PEI]` 係因 mode D 要求查得而 leaf → CFTS 條號無 id 橋樑（A-DM10b），
> **無法提案**。`[PROPOSED]` 未經修改即生效，會使該項在簽核時無聲通過（R-DM32）

該條所指之危險正是本項之核心：**`[PROPOSED]` 未經修改即生效**
（FO §4 明文），故一個字面 `None` 若無人動它，就會成為簽定值。

**二 feature 之情形不同，處置因而不同**：display 為 mode D 且**無值可填**，
故留 `[PEI]`；本 feature 為 mode A 且 R-VC4 已裁明其值（逐字取
`HMI Source ID`），故採**實值覆蓋**。二者皆非「照簽 `None`」。

**未修 `recon.py`** —— 依下放包 05 §一之三項理由（覆蓋是終局的、
R-VC8 之授權邊界已寫死、本項非本 feature 獨有故屬全域排程）。

---

## 2. T32 —— `DECISIONS` 送簽稿

檔：`features/vehicle_category/docs/DECISIONS_signoff_draft.md`（133 行）。
**`DECISIONS.md` 未動**（`git status --porcelain` 對該檔輸出為空）。

以上繳包 04 §6 之送簽內容為底，三處異動：

1. **§4 `spec_reference`** —— 改為 §一之覆蓋文字（實值 + 依據 + 資料件指向），
   並附 A-VC11 之說明與 display 之前例。
2. **新增 §6 Priority** —— 依上繳包 04 §6.4 之建議增列，指向
   `data/priority_final.tsv`，載明分布（P0 5 / P1 32 / P2 45 / P3 35）、
   三層判準、機械映射之禁令，以及 R-VC11(c) 於生成時之附帶義務。
3. **§3 `037 leaves: 145` 加註** —— 標明其為 `Categorization` 判準，
   非 R-VC3 之驗證母體 117；並揭露 117 與 17 無 assertion 實作（A-VC8），
   其守護非機器保證（R-VC9 之揭露義務）。若簽署者只讀決策表，
   這是唯一會看到該事實的地方。

另於 §8 附一則**建議而非提案**：若 8 組 Test Set 獲簽，pilot 宜取
`Glove Box`（12 筆，邊界清楚、含完整流程、無待補節），
不宜取 `Brake Service`（2）或 `Cabrio Widget`（1）。pilot 之選定屬 Tier 2。

送簽稿全文見該檔，不在此重貼（避免二處各改其一）。

---

## 3. T33 / T34 —— 待簽，未執行

下放包 05 §三明文：「T33 為 Tier 2，須 Pei 簽署 §二之邊界後始得執行。」
本輪**未收到簽署**，故：

- **未寫** `features/vehicle_category/framework.md`
- **未產出** `data/layer3_map.tsv`、`data/test_set_map.tsv`
- **未寫** `scripts/verify_partn.py`

§2.5 之理由亦支持此順序 ——「待邊界簽署後始得寫，否則驗算的是未定案之數字」。

**但 §二之提案已全數獨立覆核**（§4／§5），簽署所需之事實基礎已備齊：
若你回「Layer 2 邊界: 准」，T33／T34 可直接執行，無待補量測。

---

## 4. §2.2 之 8 組獨立重測（不引用下放包之數字）

**方法**：自 037 重數。分組規則以**可執行之判準**表述（章號 + 章 11 之
節界），**非硬編 leaf 清單** —— 硬編會使「重測」退化為抄寫。

```python
def assign(s):                      # s = HMI Source ID 尾段之章節號
    c = int(s.split(".")[0]); k = [int(x) for x in s.split(".")]
    if c == 2:  return "Category Structure"
    if c == 3:  return "Controls"
    if c in (4,5,6,7): return "Glove Box"
    if c == 11: return "Settings Behavior" if k[1] <= 6 else "Settings Presentation"
    if c == 12: return "Settings Presentation"
    if c == 13: return "Ignition Availability"
    if c == 14: return "Brake Service"
    if c == 16: return "Cabrio Widget"
    return "**未分派**"
```

### 4.1 結果

| # | Test Set | leaf（實測）| 包 05 | 判 | section | Sub Cat | 節範圍 |
|---|---|---|---|---|---|---|---|
| 1 | `Category Structure` | **24** | 24 | = | 13 | `{'HMI': 24}` | 2.2–2.6.3 |
| 2 | `Controls` | **17** | 17 | = | 12 | `{'HMI': 17}` | 3.1–3.9 |
| 3 | `Glove Box` | **12** | 12 | = | 8 | `{'HMI': 12}` | 4.1–7.1 |
| 4 | `Settings Behavior` | **15** | 15 | = | 6 | `{'Service': 15}` | 11.1–11.6 |
| 5 | `Settings Presentation` | **30** | 30 | = | 17 | `{'HMI': 30}` | 11.7–12.8 |
| 6 | `Ignition Availability` | **16** | 16 | = | 8 | `{'Service': 16}` | 13.1–13.5 |
| 7 | `Brake Service` | **2** | 2 | = | 1 | `{'HMI': 2}` | 14.1 |
| 8 | `Cabrio Widget` | **1** | 1 | = | 1 | `{'HMI': 1}` | 16.2 |
| | **合計** | **117** | 117 | = | **66** | | |

**8/8 相符。leaf 合計 117（期 117）、section 合計 66（期 66）。**

### 4.2 覆蓋完整性（即 T34 之四個 assertion 提前驗過）

```
落於二組者: 無
零組者    : 無
未分派    : 0
```

**無 leaf 落於二組或零組。** 且每組之 `Sub Categorization` **皆為單一值**
（表中第 7 欄），即分組未跨越上游之分群軸 —— 這不是提案所宣稱的，
是重測順帶查出的一致性。

### 4.3 **一項須更正 —— §2.3 之 #6 依據**

下放包 05 §2.3 稱：

> #6 之邊界 —— 章 13 全 16 筆為 `Sub Cat = Service`，且**恰等於
> FROP = Power Management 之 16 筆**。

**「恰等於」不成立 —— 兩個 16 是不同母體的數字巧合。**

| 母體 | 章 13 之量 | FROP = Power Management 之量 |
|---|---|---|
| **145 列**（全表）| 22 列（PM **16** ＋ VS 6）| **16 列**，全部在章 13 |
| **117 leaf**（驗證母體）| **16 leaf**（PM **12** ＋ VS **4**）| 12 leaf |

- 「章 13 全 16 筆」之 16 是 **leaf 數**。
- 「FROP = PM 之 16 筆」之 16 是 **列數**（含 4 個有子之父：
  `VC-058`／`059`／`060`／`064`，該四筆不入 leaf 集）。
- 於 leaf 母體上，章 13 為 PM 12 ＋ VS 4
  （VS 之 4 筆為 `VC-062-01`／`062-02`／`063-01`／`063-02`）。

**其所導之結論仍然成立**：`grep` 全表得 FROP = PM 之 16 列**全部**落在
章 13（章別分布 `{'13': 16}`），故表 A 之 16 列確實一對一映射到
Test Set #6，無需跨組拆解。**結論對，理由錯。**

`Audio Management` 之 1 筆（`VC-048-02`，§12.3.2）落於 **#5
`Settings Presentation`** —— 與下放包所述一致，表 A 須單獨標註。

> 本項不影響邊界提案，故**未停**。但既為 §2.3 所援之依據，
> 據實回報 —— 這與 REV-08（T5「16 列」之口徑）為同一種混淆：
> **145 列母體與 117 leaf 母體之數字不可互援**。
> 建議一併記入 `docs/REVISIONS.md`（本輪未記，待你確認後補）。

---

## 5. §2.1 之 `Sub Categorization` 獨立重測

### 5.1 逐章分布

| 章 | Sub Categorization | 混章 |
|---|---|---|
| 2 | `{'HMI': 24}` | 否 |
| 3 | `{'HMI': 17}` | 否 |
| 4 | `{'HMI': 4}` | 否 |
| 5 | `{'HMI': 3}` | 否 |
| 6 | `{'HMI': 3}` | 否 |
| 7 | `{'HMI': 2}` | 否 |
| **11** | **`{'Service': 15, 'HMI': 5}`** | **是** |
| 12 | `{'HMI': 25}` | 否 |
| 13 | `{'Service': 16}` | 否 |
| 14 | `{'HMI': 2}` | 否 |
| 16 | `{'HMI': 1}` | 否 |

**章 11 為唯一混章** —— 與下放包 §2.1 之表相符（該表另列章 13 為
`Service` 16、其餘全 HMI，本測一致）。全表 HMI 101 ＋ Service 16 = 117。

> 註：上繳包 01 §3.3 所載之 `HMI 103 / Service 42` 為 **145 列**母體之
> 分布；本表為 **117 leaf** 母體。二者不可互援 —— 同 §4.3 之提醒。

### 5.2 章 11 之切分：連續且零交錯

以章節號升冪排序章 11 之 20 筆 leaf，逐筆讀其 `Sub Categorization`：

```
§11.1    Service   VC-034-01        §11.5    Service   VC-038-03
§11.1    Service   VC-034-02        §11.5    Service   VC-038-04
§11.2    Service   VC-035-01        §11.5    Service   VC-038-05
§11.2    Service   VC-035-02        §11.6    Service   VC-039
§11.2    Service   VC-035-03        ──────── 切換 ────────
§11.3    Service   VC-036-01        §11.7    HMI       VC-040
§11.3    Service   VC-036-02        §11.7.1  HMI       VC-041
§11.4    Service   VC-037-01        §11.8    HMI       VC-042-01
§11.4    Service   VC-037-02        §11.8    HMI       VC-042-02
§11.5    Service   VC-038-01        §11.8.1  HMI       VC-043
§11.5    Service   VC-038-02
```

**`Sub Categorization` 之切換次數 = 1。**

- Service 之節：`11.1, 11.2, 11.3, 11.4, 11.5, 11.6`（15 leaf）
- HMI 之節：`11.7, 11.7.1, 11.8, 11.8.1`（5 leaf）

**連續、零交錯，且切點恰在 11.6 / 11.7 之間** —— 與下放包 §2.1 所述
逐字相符。該切點即 Test Set #4 / #5 之分界。

### 5.3 對「二來源交集」之效力評估（承下放包 §2.1 之自陳弱點）

下放包已自陳：「除章 11 外，`Sub Categorization` 與章節邊界完全重合，
未提供額外資訊。」**本測證實此點** —— 十一章中十章之
`Sub Categorization` 為章內單一值且與章界重合。

故 IN §4.1.2 之二來源交集，在本 feature 之實際效力為：

| Test Set 邊界 | 支撐來源 |
|---|---|
| #4 / #5 之分界（11.6 \| 11.7）| **二來源**（規格目次 ＋ `Sub Categorization`）|
| 其餘 7 個邊界 | **單一來源**（規格目次）|

**8 組之中只有 1 個邊界有交叉驗證。** 這是提案之主要弱點，
下放包已據實揭露，本測既未放大也未縮小之。

---

## 6. 未結清單

### DR —— 七筆全未結

DR-VC1 ~ DR-VC7。同批 A ＝ DR-VC2 ＋ DR-VC7 ＋ A-VC2 ＋ A-VC10。

### A —— 七筆未結

| A | 狀態 | 待 |
|---|---|---|
| A-VC2 | PENDING | 同批 A |
| A-VC3 | PENDING | 併入 DR-VC3 |
| A-VC4 | PENDING | 全域排程 |
| A-VC8 | PENDING | 全域排程 |
| A-VC9 | PENDING | DR-VC7 |
| A-VC10 | PENDING | 同批 A |
| **A-VC11** | **PENDING** | **全域排程** |

已結四筆：A-VC1（撤銷）、A-VC5 / A-VC6 / A-VC7（RESOLVED）。

**全域排程現有三筆同源之工具修法**：A-VC4（`new_feature.py` 之 abbr
推導）、A-VC8（`recon.py` 缺 `leaf_count` assertion）、
A-VC11（`recon.py` 之 DECISIONS 顯示層）。三者標的各異，
依既有裁定**不得併案**，但可同批排程。另 A-TM04 亦同源於 A-VC4。

---

## 7. 待你回覆（下放包 05 §五之格式）

```
DECISIONS spec_reference: 准（簽時覆蓋）/ 改修腳本
Layer 2 邊界: 准 / 甲 / 乙 / 丙 / 其他
Test Set 名稱: 准 / 改（列出）
```

另二項本輪新生，一併請裁：

4. **§4.3 之更正是否記入 `docs/REVISIONS.md`**（145 列母體 vs 117 leaf
   母體之數字互援，與 REV-08 同型）。本輪未記。
5. **`DECISIONS.md` 之簽署**（Tier 3）。送簽稿已備於
   `docs/DECISIONS_signoff_draft.md`。

---

## 8. 量測條件揭露（R-G8）

### 通則

同前包（openpyxl `read_only=True, data_only=True`；U+00A0 先轉半形再
strip；集合比對逐字）。leaf 集之構造一律為「子需求 ∪ 無子之父」，
與 T4／T12／T24／T28 同法。

### §4（8 組重測）

- **分組以可執行之判準表述，非硬編 leaf 清單。** 若改以清單比對，
  「重測」會退化為抄寫下放包之答案 —— 那不是獨立重測。
  本法之輸入只有 037 之 `HMI Source ID` 與章節號，
  下放包之數字僅用於最後一欄之比對。
- **偽陽性風險**：分組規則本身係依下放包 §2.2 之邊界描述所寫。
  若該描述與其意圖有落差（例如 §2.2 寫「11.7–11.8.1」而實際想切在別處），
  本測只能驗出「規則之輸出與其宣稱之數字一致」，
  **不能驗出「該邊界是不是好的切分」**。後者屬 Tier 2 判斷，非量測。
- 章號取 `sec.split(".")[0]`，章 11 之次級判準取 `k[1] <= 6`。
  **偽陽性風險**：若章 11 日後新增 `11.9`（該節現在 037 未涵蓋，
  在表 B 之 17 節內），`k[1] <= 6` 會把它歸入 #5 `Settings Presentation`。
  依 §2.1 之語意（11.9 為「設定通則邏輯」，屬行為而非呈現），
  **屆時應歸 #4**。此規則對未來之補節不成立，已記於此。

### §5（`Sub Categorization` 重測）

- 「混章」以值集合大小 > 1 判定，非以眾數 —— 單一例外即會顯現。
- 「連續、零交錯」以章節號升冪排序後計算相鄰值之變化次數；
  **切換次數 = 1 等價於「二段各自連續」**。
  若為交錯（如 Service, HMI, Service），切換次數必 ≥ 2。
- **偽陽性風險**：排序鍵為 `[int(x) for x in s.split(".")]`，
  對 `11.7` 與 `11.7.1` 之相對序正確；若日後出現非數字之章節號段
  （如 `11.7a`），該鍵會拋例外而非靜默排錯 —— 這是刻意的。

### T31（A-VC11 範圍查證）

- `grep -n "spec_reference_template" features/*/feature.yaml` 為**窮舉**
  （12 個 feature 全覆蓋），非抽樣。
- display 之症狀為直接讀其 `DECISIONS.new.md:33` 所得，非推論。
- **未查**其餘 10 個 feature 之 `DECISIONS.new.md` 是否存在其他形態之
  顯示層洩漏 —— 本項只驗證 A-VC11 所述之範圍，未擴大掃描。

---

**T31／T32 完成。T33／T34 待簽，未執行。未簽署、未合併、未進入 Phase 3。**
