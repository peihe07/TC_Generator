# framework — FW036 Power Moding HMI（Layer 1 / 2 / 3）

- 產出日：2026-08-24（下放包 06 步驟 3）
- 資料來源：`data/layer3_sections.tsv`（48 leaf，執行層 05 包產出）
- Layer 2 提案來源：下放包 06 §5，**經執行層以 TSV 機器複算，48/48 相符、
  各 Test Set 計數與 §5.1 逐項相符、R-G10 餘數 0**
- **狀態：定版**（2026-08-24，**R-PMH36** —— Pei 裁「甲」）。Layer 2 為 **8 組**，
  第 2 組名為 `Disclaimer Screen`。逐 leaf 歸屬以 `data/layer3_sections.tsv` 為權威。

---

## Layer 1 —— Test Group

**`Disclaimer screen`**（R-PMH13，Pei 2026-08-23 核可）

⚠ **R-PMH18** —— `screen` 為**小寫 s**，為交付夾名之原樣。
與 `tc_id` 之 `DisclaimerScreen`（大寫 S）**刻意不同，不得統一**。

依據：四份已交付件之 G 欄實測 4/4 皆為交付夾名（06 包前之 03 包 §5）。
**非規格模組名** —— R-PMH2 之後半已撤回。

---

## Layer 2 —— Test Set（8 組，**定版**）

**R-PMH36（Pei 2026-08-24 裁「甲」）** —— 第 2 組名為 `Disclaimer Screen`。

⚠ **本組名與 Test Group `Disclaimer screen` 字面重複，為 canon §4.2
「不得重複 Test Group 字樣」之明示例外**，其範圍**嚴格限定為：本 feature、
本組、此一情形**（Test Group 取交付夾標籤而非能力名，致交付夾名恰等於
其中一個能力群之名稱）。**不得外推至他 feature，亦不得作為 §4.2 之
一般性放寬。**

⚠ **R-PMH18 之精神延伸** —— 三個字串刻意不同，**不得統一**：

| 用途 | 值 | 關鍵 |
|---|---|---|
| Test Group（G 欄） | `Disclaimer screen` | **小寫 s**（交付夾名原樣） |
| **Test Set（H 欄）** | **`Disclaimer Screen`** | **大寫 S**（能力群名） |
| `tc_id` 之 `{abbr}` | `DisclaimerScreen` | **大寫 S、無空白** |

**未採之兩案及其理由（隨 R-PMH36 保留）**：
（乙）`Acceptance Screen` —— `Acceptance` 非規格用語（規格自 7.1 SU1 至
10.4 PITA6.1 一律用 `disclaimer`），屬造詞，違 §8.4.1 之精神；
（丙）併入 `Splash Screen` —— 合 §4.2 字面，但該 10 leaf 混兩個 FROP、
兩種觸發情境，且客戶無法以 H 欄過濾出 disclaimer 之 7 條。

**granularity 判準對三案全部 PASS，對本題無鑑別力**（08 §2.3），
**不得引之為支持本條之理由**。本條之依據為**可過濾性**與**不造詞**二者。

| # | Test Set | leaf | Layer 3（規格章節） | 主要 FROP |
|---|---|---:|---|---|
| 1 | **`Splash Screen`** | 3 | 7.1, 7.9 | Customizable Splash Screen / Animations(3) |
| 2 | **`Disclaimer Screen`** | 7 | 7.1, 7.2, 7.3, 7.4, 10.4 | Disclaimer screen(7) |
| 3 | **`Startup Animation`** | 9 | 7.5, 7.5.1, 7.6, 7.7, 7.8 | Customizable Splash Screen / Animations(9) |
| 4 | **`Startup Sounds`** | 6 | 8.1, 8.2, 8.2.1, 8.2.2, 8.2.3, 8.3 | Audio Management(6) |
| 5 | **`Power Transitions`** | 7 | 7.1.1, 9.1, 10.5 | Power Management(3)／FOTA Via Wi-fi(2)／WiFi(1)／EV/PHEV Pages(1) |
| 6 | **`Power Off Behavior`** | 8 | 10.1, 10.2, 10.3, 10.4, 10.6, 10.7 | Bluetooth(3)／Rear View Camera(2)／Climate Control(2)／e-call (private)(1) |
| 7 | **`Voice Assistant Key`** | 5 | 11.1 | Steering Wheel Controls(5) |
| 8 | **`Off Road Plus`** | 3 | 12.1, 12.2, 12.3 | Power Management(2)／Audio Management(1) |

**48 = 3 + 7 + 9 + 6 + 7 + 8 + 5 + 3，R-G10 餘數 0。**

### 三處切法之依據（06 §5.3，執行層複驗相符）

1. **7.1 之五個 leaf 拆入兩個 Test Set**（`001-01/02` → Splash、
   `001-03/04/05` → #2）。依據為 **037 `FROP` 欄之既有分群** ——
   上游 RD 之切法，非 TC 作者重新分解（canon §8.2）。
   TSV 複驗：`001-01/02` 之 FROP 為 `Customizable Splash Screen / Animations`、
   `001-03/04/05` 為 `Disclaimer screen`。
2. **10.4 之兩個 leaf 拆入兩個 Test Set**（`022-01` → Power Off Behavior、
   `022-02` → #2）。同上，依 FROP。
   TSV 複驗：`022-01` 為 `Climate Control`、`022-02` 為 `Disclaimer screen`。
3. **章 9 之五個 leaf 全歸 `Power Transitions`**，雖其 FROP 有四值 ——
   因同屬 9.1 一節、共用「IGN OFF 時之 popup 與 Power Accessory Delay」
   之同一觸發情境（canon §4.2「同一 Test Set 應共用 setup 與 UI 進入路徑」）。
   TSV 複驗：9.1 之 5 leaf 之 FROP 為 Power Management／FOTA Via Wi-fi(2)／
   WiFi／EV/PHEV Pages，**pdf_page 皆為 p9**。

### Test Set #2 之命名 —— **已定案**（R-PMH36，見本節首）

---

## Layer 3 —— 規格章節對照

Layer 3 取**規格自身之 section id**（canon §4.1.1），不自創標籤。
全表見 `data/layer3_sections.tsv`（48 列 × 7 欄）。章層對照：

| 章 | 章標題（SYS1 `Outline Number` 之 Description 逐字） | leaf | PDF 頁 |
|---:|---|---:|---:|
| 7 | `Startup` | 19 | p8 |
| 8 | `Starup R1Low Only` | 6 | p8 |
| 9 | `Power Moding` | 5 | p9 |
| 10 | `Additional Power Moding Behavior Notes:` | 10 | p10 |
| 11 | `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS` | 5 | p10 |
| 12 | `Power Moding – Off Road+` | 3 | p11 |

**未被任何 leaf 引用之 outline 23 項**見 `data/uncited_sections.tsv`
（`chapter_node` 12／`image_placeholder` 6／`assumptions` 5／**`other` 0**）。

---

## Layer 2 之 granularity 檢查（canon §4.1.3）—— **PASS**

**本節於 08 包重寫**（R-PMH35）。07 §三之原表六列**全為 must-not-hit**
且門檻不可執行（「≈ TC/leaf 數」「過半」），依 R-PMH35(a)(c) 不得標 PASS。

**判準之實作**：`scripts/check_granularity.py`（門檻寫死於程式，可重跑）。
**自測指令**：`python scripts/check_granularity.py --feature . --self-test`

### 五項判準與其門檻 —— **由程式產出（R-PMH40）**

**R-PMH40 —— 門檻只有一個來源：`scripts/check_granularity.py` 之 `THRESHOLDS`。**
下表由 `python scripts/check_granularity.py --emit-thresholds` 產出後貼入，
**不另行維護副本**。

| id | 量 | 關係 | 門檻 | 來源 |
|---|---|:--:|---|---|
| **G1** | 組數 / leaf | `<=` | **`1/3`** | canon §4.1.3 決策測試之平均意義：平均每組不足 3 個 leaf 時，過濾結果多為 1–2 列，索引價值與逐條列舉無異（R-PMH39） |
| **G2** | min(組規模) | `>=` | **`2`** | canon §4.1.3「不是一條」之單組下限 —— 至少兩個才成組 |
| **G3** | 組名命中收容簇清單之數 | `==` | **`0`** | 收容簇清單 ['general', 'misc', 'other', 'unclassified', '雜項']；全字比對、大小寫不敏感 |
| **G4** | max(組規模) / leaf | `<=` | **`1/2`** | canon §4.1.3「不是整本」—— 單組不得吃掉過半 |
| **G5** | 逸出 [2, floor(leaf/2)] 之組規模數 | `==` | **`0`** | G2 之下限與 G4 之上限所夾之區間，逐組適用 |

> 產生時之程式 SHA256：`6d9fdbc53ddcd27426fe907700fc74697f83a06f5390a2c0e4173c76075c65a7`
> 重新產生：`python scripts/check_granularity.py --emit-thresholds`

**G1 之門檻由 `0.35` 改為 `1/3`（R-PMH39）** —— `0.35` 係湊得，且現有錨點
對 `0.35` 與 `0.5` 無鑑別力（A1 之 `0.6042` 對兩者皆 FAIL），依 R-PMH14
不足以支持之。`1/3` 之來源為 canon §4.1.3 決策測試之**平均意義**：
G2 之 `min ≥ 2` 承接「不是一條」之單組下限，**G1 承接其平均** ——
平均每組不足 3 個 leaf 時，過濾結果多為 1–2 列。

**G1 不可省** —— 存在 G2／G4／G5 全通過而仍過細之組態（48 leaf 分 20 組，
每組 2–3），即隔離錨點 **A6**。

### 現行 8 組之實測

| id | 實測 | 門檻 | 結果 |
|---|---|---|---|
| G1 | `8/48 = 0.1667` | `≤ 1/3 = 0.3333` | **PASS**（餘裕 2 倍） |
| G2 | `min = 3` | `≥ 2` | **PASS** |
| G3 | 零命中 | `= 0` | **PASS** |
| G4 | `9/48 = 0.1875` | `≤ 1/2` | **PASS** |
| G5 | 逸出 0（區間 `[3, 9]`） | `= 0` | **PASS** |

> G3 之比對單位為**整詞**（以空白與 `/` 切分），故 `Power Off Behavior`
> 之 `Off` 不命中 `Other`。

### must-hit 錨點之實跑（R-PMH35(c)）—— **六個全部如期 FAIL**

隔離度依 **R-PMH38** 之三級標示；**結構性連帶須有算式，不得以文字論述代替**。

| 錨點 | 構造 | 指定 FAIL | 實跑 | **隔離度** |
|---|---|---|---|---|
| **A1** | 每 outline 各成一組（29 組） | G1 | `0.6042 > 0.3333` ✅ | **結構性連帶** `[G2, G5]` |
| **A2** | 每 leaf 各成一組（48 組） | G1、G2 | `1.0 > 0.3333`；`min=1` ✅ | **結構性連帶** `[G5]` |
| **A3** | `Off Road Plus` 拆為三個單 leaf 組（10 組） | G2、G5 | `min=1`；逸出 `[1,1,1]` ✅ | **隔離** |
| **A4** | 新增一組名為 `Misc`（**取 2 leaf**） | G3 | 命中 `['Misc']` ✅ | **隔離** |
| **A5** | 八組併為一組（1 組） | G4、G5 | `1.0 > 0.5`；逸出 `[48]` ✅ | **隔離** |
| **A6** | 48 leaf 分 **20 組**（8×3 ＋ 12×2） | **G1** | `0.4167 > 0.3333` ✅ | **隔離** —— G2/G3/G4/G5 全 PASS |

**A1／A2 之結構性連帶算式**（由程式判定，非註解）：

> 鴿籠：`n` 個 leaf 分 `k` 組，每組規模 ≥ 2 須 `n ≥ 2k`。
> 故 `k > floor(n/2)` 時**必有**單 leaf 組 ⇒ G2 必然 FAIL；
> 且該單 leaf 組必逸出 `[2, floor(n/2)]` ⇒ G5 亦必然 FAIL。
> A1：`k=29 > 24`，`2k=58 > 48`；A2：`k=48 > 24`，`2k=96 > 48`。

**每一判準至少有一個「隔離」或「結構性連帶」之錨點**（R-PMH38 末段）：
G1 → **A6（隔離）**；G2 → A3（隔離）；G3 → A4（隔離）；
G4 → A5（隔離）；G5 → A3／A5（隔離）。**無任一判準須標「未實測」。**

**範圍向（R-G9）**：現行 8 組於 **G1–G5 全部 PASS**。

### ⚠ 本判準對 Q11 之三案**無鑑別力**（R-PMH14 / R-PMH35 末段）

Q11 已由 **R-PMH36** 定案為（甲）。惟其定案**不得引本判準為理由** ——
三案於 G1–G5 之結果完全相同（`1/3` 門檻下重跑仍同）：

| 案 | 組數 | 最小 | 最大 | G1 | G2 | G3 | G4 | G5 |
|---|---:|---:|---:|:--:|:--:|:--:|:--:|:--:|
| （甲）`Disclaimer Screen` ← **已採** | 8 | 3 | 9 | ✅ | ✅ | ✅ | ✅ | ✅ |
| （乙）`Acceptance Screen` | 8 | 3 | 9 | ✅ | ✅ | ✅ | ✅ | ✅ |
| （丙）併入 `Splash Screen` | 7 | 3 | **10** | ✅ | ✅ | ✅ | ✅ | ✅ |

程式之明示輸出逐字：

> 本判準對 Q11 之三案無鑑別力 —— 三案於 G1–G5 之結果完全相同（皆 PASS），
> 依 R-PMH14 不得被引為支持任一案之理由。

**R-PMH36 之依據為可過濾性與不造詞二者，非 granularity。**

**連帶更正**：06 §5.4 曾將「丙案之 granularity 須重驗」列為丙案代價 ——
**該陳述不成立**（丙案 G1–G5 全 PASS，`max` 由 9 增為 10，遠低於門檻 24）。

### 本檢查之限制（07 §三明載，仍有效）

**它驗的是 leaf 分布，不是 TC 分布。** TC 生成後若某組 TC 數暴增，
**granularity 須以 TC 分布重驗** —— 列為 Phase 4 之複驗項。

---

## 未決與待驗

| 項 | 狀態 |
|---|---|
| ~~Q11 —— Test Set #2 之命名~~ | **已結清**（R-PMH36，2026-08-24） |
| **A-PMH13** —— `SWE1-HMI-PM-028`（12.2）指向 CFTS009 | 見 `ANOMALIES.md`；`features/power` 之涵蓋查證見上繳 06 §4 |
| A-PMH03 —— outline 7.1 之重排 | Phase 4 指名複核（該節 5 leaf，分屬 Splash 2 ／ #2 3） |
| A-PMH04 —— 6 則圖片佔位 outline | Phase 4；**48 leaf 無一落在 p3–p7**，不阻斷 |
| **granularity 之重驗** | **Phase 4** —— 本檢查驗的是 leaf 分布；TC 生成後須以 TC 分布重驗 |

