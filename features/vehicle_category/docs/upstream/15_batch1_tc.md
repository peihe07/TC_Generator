# 上繳包 15 —— Vehicle Category：第 1 批 a 段 22 筆 —— **收斂第 14 項不過，停**

- 日期：2026-08-26
- 對應下放：`docs/handoff/15_batch1_tc.md`
  （SHA256 `5fc54331bd3e3e01b5b74aad63a8b357909f26ee113bb983530e05f8eae967c7`，233 行）
- **結論：T83–T87、T89 完成。T88 之第 14 項不過 → 依收斂條件「任一項不過即停
  並回報，不自行修補後續」，停於此。**
- 22 筆已產出（`generated/batch1_category_structure.json`），**未寫回工作簿**。
- 未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T83 | R-VC22 抄錄 | ✅ 逐字（1,336 B／25 行／`4de7914d5d383b54`）|
| T84 | profile §6 | ✅ 二則 Pre-Condition 常數；**與 §5 分立**之理由已記 |
| T85 | DR-VC9 雙標的分送 | ✅ |
| T86 | PLAYBOOK 擴為雙向 | ✅ |
| T87 | 生成 22 筆 | ✅ |
| T88 | 收斂 19 項 | ⚠️ **17 checked / 1 failed** |
| T89 | b 段列名 | ✅ 見 §6 |

**停點：第 14 項（setup 片語取自常數表）—— 2 筆之 Procedure 首步不在表中。
而那 2 筆之偏離是必要的，不是筆誤。** 詳見 §4。

---

## 1. T83–T86

- **R-VC22** 抄入 `RULINGS.md`，byte-level diff 逐字一致。
- **profile §6**（標準 Pre-Condition 措辭）新增，登記
  `DISPLAY_LANDSCAPE`／`DISPLAY_PORTRAIT`。**與 §5 分立**之理由已逐字記入：
  §5 之標的為 IN §5.3 之 Setup **Snippets**（Procedure 步驟），
  §6 之標的為 **Pre-Condition**（規制來源為 §4.4）——
  二者之判準與禁項不同，混為一表會使 §4.4 之三類禁項失去對應。
  另記其偽陰性：本表只驗「若涉方向，是否用表中措辭」，
  以其他措辭表達同一前提者看不到，**故第 11 項仍為主防線，本表為輔**。
- **DR-VC9** 已記雙標的與分送安排（(一) 規格作者獨立發、(二) 037 作者併同批 A），
  含「編號不拆」之理由。
- **PLAYBOOK §7.1** 擴為雙向，並記其由來（T52／T79 二次同型漏抓）。

> profile 之節號一度被擠成 `0,1,2,3,5,6,7`（§4 落到最後）。
> **未重編號** —— R-VC21 條文與 `verify_batch.py` 皆以「profile §5／§6」
> 指涉，重編號會使已落地之條文指錯。改將 §4 移回原位，節號回復連續。

---

## 2. T87 —— 22 筆 a 段

`generated/batch1_category_structure.json`。
`segment: "a"`，`held_leaves` 記 b 段 2 筆。

`segment_note` 逐字記入 R-VC22(b)(c)：
**收斂條件以 a 段之 22 為母體；收斂不等於 `Category Structure` 完成，
該 Test Set 之 leaf 數仍為 24，`framework.md` 不因分段而改動。**

### 2.1 本批特有拘束之落實

| 拘束 | 落實 |
|---|---|
| 句子片段 | `012-03`／`013-03` 之 `test_item` 上半取 **SYS1 完整句**；括號下半載本 leaf 之驗證範圍；`reasoning` 載取整句之理由 |
| 四欄表 | `007-02`~`-05` 之 ER 以「該列所載之 tab name 與 position」表述，值之權威為 SYS1 §2.4 之表 |
| `VC2.2.3` 黏連 | `007-02` 之 `reasoning` 逐字記其黏連（`OptionsDrive`／`DXROff`）與**不自行拆分**之處置 |
| 下界 | `012-02` 以「恰好兩個 feature」為 Pre-Condition 與 Procedure 之資料 |
| 外部委派 | `008` 之 `reasoning` 載明 Camera App 行為不在範圍（§8.4.2）|
| PENDING | `011`／`012-03` 各帶一處，字串依其阻斷內容分別為 `PENDING: DR-VC9 Dashboard content table`／`PENDING: DR-VC9 PDO graphics` |
| 方向前提 | `012-*`／`013-*` 取 profile §6 之常數（逐字）|

### 2.2 一處逾越範圍者，我沒有做

`013-02` 之 `test_item` 上半取 SYS1 完整句，該句同時涵蓋 `013-03` 之內容。
二筆之上半因而**逐字相同** —— R-S4 只禁括號下半逐字相同，未禁上半相同
（下放包 14 §2.2 之明文），故合規。`012-02`／`012-03` 同理。

---

## 3. T88 —— 收斂驗證：17 checked / 1 failed

### 3.1 母體之一般化

`verify_batch.py` 之硬編 `12` 已改為 `EXPECT_N = len(J["leaf_scope"])`
—— **依 R-VC22(b)，母體為本批 a 段之筆數**。
另將 pilot 專屬之第 8／9／10 項改為條件式（該批無對應 leaf 時報 N/A），
使同一腳本可跨批使用。批次檔由 `BATCH` 環境變數指定。

### 3.2 十六項通過

第 1、2、3、3b、4、5、6、7、7b、8、9、10、11、12、13、A 項全數 PASS。
其中：

- **第 4 項**：22 筆 `specification_reference` 與 `recon_leaf_to_section.tsv`
  **逐字相符 0 不符**
- **第 5 項**：22 筆 `priority` 與 `priority_final.tsv` **逐字相符 0 不符**
- **第 7b 項**：本批**保留 token 0 個** —— 22 筆之 verbatim 上半皆無
  `'...'`／`«...»`（037 §2.x 之 Description 未用該記法）。
  R-VC19 之例外**本批未觸發**。
- **第 11 項**：`pre_conditions` 三類禁項命中 0。方向前提之
  `The vehicle is equipped with a landscape display` 屬 hardware 類，未觸禁。

### 3.3 ⚠ 第 14 項 FAIL

```
 14  本批 setup 片語（Procedure 首步）皆取自 profile §5 常數表   **FAIL**
     profile 常數 1 條；批內相異首步 3 種；不在表中
     ['Open the Vehicle Category screen',
      'Open the Vehicle Category screen and select the "Settings" tab']
```

---

## 4. 停點 —— 第 14 項，且那 2 筆之偏離是必要的

### 4.1 二筆之首步與其必要性

```
SWE1-HMI-VC-001-02  |  Controls active on first entry
  1. Open the Vehicle Category screen
  2. Record which tab is active on entry

SWE1-HMI-VC-001-03  |  Last viewed tab restored on re-entry
  1. Open the Vehicle Category screen and select the "Settings" tab
  2. Leave the Vehicle Category screen
  3. Open the Vehicle Category screen again and record which tab is active
```

**二者皆不能用 `ENTER_CONTROLS_TAB`**：

- `001-02` 驗的是「首次進入時**預設**為 Controls」。
  若 setup 步驟先選了 Controls，**該 TC 即自我實現，驗不到任何東西**。
- `001-03` 驗的是「回復**上次瀏覽**之頁籤」。
  其 setup 必須把作用頁籤留在**非預設值**上，否則與 `001-02` 無法區辨。
  選 `"Settings"` 是為此。

**這不是措辭偏好，是測試語意上的必要。**

### 4.2 我沒有做的兩件事

1. **未加常數使其通過** —— 那會是「改被檢查之對象使檢查變綠」。
   profile §5 之常數表正是第 14 項的判準來源；由我單方擴充它，
   等於自己出題自己改答案。
2. **未放寬第 14 項** —— 同上，且該項本輪之 FAIL 是**正確的**：
   它確實抓到了三種不同的首步。

### 4.3 更深一層 —— 第 14 項假設了「首步 = setup」

第 14 項驗「Procedure **首步**是否為表中常數」。
該判準隱含「首步必為 setup」之假設。

而 `001-02` 之首步 `Open the Vehicle Category screen` **本身就是受測動作** ——
「進入」正是該需求之觸發。它不是 setup，是 test action。
對這類 TC，「首步取自 setup 常數表」這個要求本身不成立。

**故本項之修法不只是加常數，還牽涉判準之適用範圍。**

### 4.4 三條可能之出路（**未擇一，待裁**）

| 出路 | 內容 | 代價 |
|---|---|---|
| 甲 | profile §5 增 `ENTER_VEHICLE_CATEGORY: Open the Vehicle Category screen`；`001-03` 之首步視為 test action 而非 setup，第 14 項改為「**首步若為 setup 則須取自常數表**」，其判定另設 | 判準最貼近實情；但「是否為 setup」需語意判斷，機械化困難（同 §4.4 第三類之處境）|
| 乙 | 第 14 項改驗「Procedure **任一步**若與常數表之某條近似（編輯距離），則須逐字相同」—— 即由「首步必須是常數」改為「用到常數就不許走樣」 | 直接對準 §5.3 所防之變體；不需判斷 setup 與否 |
| 丙 | 常數表改為**帶參數**（`ENTER_VC_TAB(<tab>)`），`001-02` 以無參數形式登記 | 表達力最強，但常數表變成迷你 DSL，profile §5.2(c) 之凍結語意須重寫 |

**我的判斷是乙** —— 它避開了「什麼算 setup」這個語意判斷，
而 §5.3 所要防的本來就是變體（case／spacing／wording），不是位置。
`001-02` 之 `Open the Vehicle Category screen` 與常數之差別是**少了後半**，
不是走樣；乙案下它不觸發，因為它不是常數之近似變體而是另一個動作。

**但這是 Tier 2，我不自裁。**

---

## 5. T88 之新增項雙向實測（依 PLAYBOOK §7.1）

第 13／14 項於上繳包 13 §2.3 已做 (a) 反向實測。
本輪補 (b) **已知標的實測**：

| 項 | (b) 已知標的 | 結果 |
|---|---|---|
| 13 | pilot 之 `Glove Box`（framework §2 有此名）| **命中為 PASS**，且對本批之 `Category Structure` 亦 PASS —— 二個不同之合法名皆通過 |
| 14 | **本批之 2 筆偏離首步** | **命中為 FAIL** —— 即本節之停點。這正是 (b) 之作用：它抓到的不是我塞的反例，是真實產出裡的偏離 |

> 第 14 項是 PLAYBOOK §7.1 擴為雙向後**第一次由 (b) 抓到東西**，
> 而且抓到的是真的。若只做 (a)，本輪會以「22 筆全綠」交出去。

---

## 6. T89 —— b 段 2 筆（R-VC22(a)）

| leaf | § | priority | 阻斷之 DR | 保留理由 |
|---|---|---|---|---|
| `SWE1-HMI-VC-007-01` | 2.4 | P2 | **DR-VC9(二)** | `Description` 逐字為 `Vehicle Tab Labels and Order.`，SYS1 為 `VC2.2.) Vehicle Tab Labels and Order` 且其下即四欄表 —— **疑為表格題名之誤登**。若上游確認，該 leaf 整筆消失，其 TC 全數作廢 |
| `SWE1-HMI-VC-013-04` | 2.6.3 | P3 | **DR-VC9(二)** | `Description` 逐字為 `Refer to PDO graphics.`，引用後殘餘為**空** —— 無自身可測內容。同上，可能整筆消失 |

**分界線為「該 leaf 是否可能整筆消失」，非「是否帶 PENDING」**（R-VC22）。
`011`／`012-03` 雖帶 PENDING 仍在 a 段 —— 值或素材未到不影響其為需求。

---

## 7. 未結清單

**DR 九筆全未結**。同批 A 六項（含 DR-VC9(二)）；DR-VC9(一) 獨立發。
**A 十二筆未結**：A-VC2、A-VC3、A-VC4、A-VC8、A-VC9、A-VC10、A-VC11、
A-VC12、A-VC13（通則）、A-VC14、A-VC15、A-VC17。
已結五筆。

---

## 8. 待你裁

1. **第 14 項之修法** —— 甲／乙／丙（我建議乙）。
2. 修法後本批重驗，19 項全過始收斂。
3. 同批 A（六項）與 DR-VC3、DR-VC9(一) 之發送（Tier 3）。

**未自行修補後續。22 筆已在 `generated/batch1_category_structure.json`，
未寫回工作簿。**

---

## 9. 量測條件揭露（R-G8）

- **第 14 項之判準**為「Procedure 首步之字串是否為 profile §5.1 之常數之一」，
  **逐字比對，不做正規化**。其 FAIL 為真陽性（三種首步確實不同），
  但其**判準之適用範圍本身可議**（§4.3）—— 這不是量測誤差，是判準設計問題。
- **母體之一般化**：`EXPECT_N` 取自 JSON 之 `leaf_scope` 長度。
  **偽陰性**：若 `leaf_scope` 與 `tcs` 不一致（例如漏填），
  第 1 項會以錯的期望值比對。已於第 1 項同時驗 `len(TCS) == EXPECT_N`，
  但二者同源，**該檢查驗不到 `leaf_scope` 自身是否正確**。
- **第 7b 項本批為 0 token** —— 其 PASS 應讀作「**本批無保留記法**」，
  非「保留記法皆已驗證」。R-VC19 之例外於本批未觸發。
- **§5 之 (b) 實測**：第 13 項之已知標的取 pilot 之 `Glove Box`，
  屬**跨批複用**；第 14 項之 (b) 為本批之真實產出，非人造輸入。
  二者證據強度不同 —— 後者強於前者。
