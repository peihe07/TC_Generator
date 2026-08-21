# 31 下放包 — 14 輪覆核：R-VS37′ 補分支、A-VS49、P18 證據完整、15 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/12_layer3_and_convergence.md`。

**覆核結論：接受。** 三項皆完成，且 §2.2 之 typo 追因是本輪最有價值者 ——
**從「差 1 條」追到「上游值域錯字，且已污染我方資料」。**

---

## 1. R-VS37′ —— 補上兩個缺分支（A-VS50）

執行層指出 R-VS37 之第二分支逐字為「跨越多個**同層**章節」，
而實測有 3 筆跨**異層**（`1.3.2.1.3` 四段 vs `1.3.3.3.6.1` 五段）、
1 筆**無 reqid**，**皆無條文依據**。指摘成立，分析層漏寫。

```
R-VS37′（取代 R-VS37；分析層裁定 2026-08-20）
Layer 3 不得純以 SWE ID 中段 token 機械切分。
一個 leaf 之 Layer 3 歸屬，依其 `reqid_list` 所跨之 CFTS044 章節判定，
四分支如下：

(1) 全部 reqid 落在**單一章節**
    → 依該章節之 Layer 3

(2) 跨越多個**同層**章節（章節號段數相同）
    → 歸 Layer 3 之跨區共通桶（名稱見 §2）
    理由：其為四側／多側共通需求

(3) 跨越**不同層**章節（段數不同）
    → 依**最深**（段數最多）之章節判定
    理由：淺章節為其所屬之上位分節，深章節才是其能力歸屬。
    實例：`HeatedSteeringWheelManagement-025/-026/-027` 跨
    `1.3.2.1.3`（4 段）與 `1.3.3.3.6.1`（5 段）→ 依後者，
    歸 `HeatedSteeringWheelManagement`（**與 token 判定一致**）

(4) **無 reqid**
    → 依 SWE ID 中段 token 之預設值，並於 `framework.md` 標
    `UNRESOLVED-SOURCE` ＋ 其待決之 DR 編號
    實例：`HeatedSteeringWheel-009`（其 Source 為 `SYS-RA-CFTS100`）
    → 歸 `HeatedSteeringWheel`，標 `UNRESOLVED-SOURCE / DR-11`

SWE ID 中段 token 於 (1)(2)(3) 僅作預設值，與章節判定衝突時以章節為準，
並逐筆記明原始 token 與改判依據。
```

**依 (3)，14 輪暫依「多章節即 Common Features」處理之 3 筆須改回
`HeatedSteeringWheelManagement`** —— 即其 token 判定原本就對，
不一致筆數由 6 降為 **3**（`LeftFrontHeatedSeat-004`／`-011` ＋
`HeatedSteeringWheel-009` 之標記）。

---

## 2. `Common Features` 名稱衝突之解

R-VS4 之 Layer 2 已有 `Common Features`；R-VS37 令跨區共通者亦歸此名，
致同名兩層。

```
分析層裁定 2026-08-20
Layer 3 之跨區共通桶定名為 **`CrossZone Common`**（逐字，含空白）。
其與 Layer 2 之 `Common Features` **不同名、不同層**：

  Layer 2 `Common Features`  = 037 檔界（Common Features.xlsx 之 46 leaf）
  Layer 3 `CrossZone Common` = 跨四側／多側之共通需求（現為 2 leaf，
                                隸屬 Layer 2 之 `Heated Seat`）

理由：Layer 3 不出工作簿（canon §4.1.5），其命名只需在 `framework.md`
內無歧義；但同名兩層會使覆蓋分析與 sibling 判定無法陳述。
```

---

## 3. A-VS49 —— 污染範圍須先掃全，再擬 DR

執行層查得 `4858393` 將通風座椅之值寫為 `HS_HI`（加熱前綴），
與 `4858394` 同文而值異；LF 對應條文一律 `VS_HI`。
**該錯值已入 `spec_variables.tsv`**（`$VentedSeatFR$` 3 個值、`$VentedSeatFL$` 1 個值）。

**但其自陳只掃了 `cfts044_include` 一欄、只查了 `Heated`/`Vented` 一對前綴。**
分析層不在污染範圍未明前擬 DR —— **先掃全，再一次問清**。

→ **W-47**。其結果出來後，DR-18 之問法才能涵蓋全部實例
（否則會像 DR-15 一樣，送出後才發現引用有誤）。

```
分析層裁定 2026-08-20（未清除之處置）
`spec_variables.tsv` 之交叉前綴值**保留不清除**，
增設 `suspect_prefix` 欄標記之，值為其疑似正確之前綴（如 `VS_`）。
**不改原值** —— 原值為 CFTS044 逐字，改之即失去與來源之可追溯性；
待 DR-18 答覆後再依 R-VS26(3) 之形態處理。
```

---

## 4. P18（R-VS7(a)′）—— 證據完整，建議定案

W-44 之實測：**完全收斂 0 / 174**，
剔除 24 個 comfort id 後每列仍剩 5／7／8 個。
且其成因已由 08 包之「資料無可收斂維度」（錯）更正為
「**維度存在，但 Comfort 側之粒度不足以逐 leaf 分辨**」（實測）。

**故 27 包 §4 之三選項中，(b) 與 (c) 之前提皆已被實測排除**：
(b)「資料補足前懸置」——補足須待上游，且 W-44 證明即使補足階數與側別，
仍剩 5 個以上；(c)「向 Comfort 作者請求逐 leaf 標註」——
其代價為要求上游重寫 129 個 leaf 之屬性。

```
待 Pei 裁：R-VS7(a)′（分析層建議採 (a)，證據已完整）
委派句改為指名**功能群**而非單一 leaf id：
  reasoning 之委派句形如
  「加熱方向盤之畫面行為由 Comfort 擁有，見 SWE1-HVAC-062／063／…」
  並註明其為群層級（Layer 3）。

依據：W-44 實測完全收斂 0 / 174；階數與側別兩維度用盡後，
每列仍餘 5～8 個 Comfort leaf。逐 leaf 指名在現有資料上不可達。
```

---

## 5. 15 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/31_review_round14.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/13_contamination_and_symmetry.md，六節先留空。
D-2  逐字轉錄 31 包 §1 之 **R-VS37′** 入 RULINGS.md，
     並將 R-VS37 標為「經 R-VS37′ 取代」（保留原文，加註，不刪 —— R-TM13）。
D-3  依 R-VS37′(3) 將 `HeatedSteeringWheelManagement-025/-026/-027`
     之 Layer 3 改回 `HeatedSteeringWheelManagement`；
     依 (4) 將 `HeatedSteeringWheel-009` 標 `UNRESOLVED-SOURCE / DR-11`；
     依 31 包 §2 將跨區共通桶更名為 `CrossZone Common`。
     更新 `framework.md`，**仍不鎖定**。
     依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-47  交叉前綴污染之全掃（A-VS49）
      (1) 掃 `spec_variables.tsv` 之**全部**值域欄
          （`cfts044_include`／`cfts044_exclude`／`cfts044_other_arch`
            或其現行等價欄名），不限 include
      (2) 前綴對不限 `HS_`/`VS_`：對本 feature 之全部 token，
          建立「token 語意前綴 → 期望值前綴」對照
          （如 `$HeatedSeat*$`→`HS_`、`$VentedSeat*$`→`VS_`、
            `$HSW_*$`→`HSW_`），逐值檢查其前綴是否與其 token 相符
      (3) 回溯每個不符值之來源 reqid 與其對稱條文（如 LF vs RF），
          判其為 typo 或別名 —— **判據須具名**（對稱條文之值為何）
      (4) 於 `spec_variables.tsv` 增 `suspect_prefix` 欄標記，
          **不改原值**（31 包 §3）
      產出 `docs/reports/prefix_contamination.md`，逐筆列出

W-48  Vented 兩節之逐位內容對照（12 輪 §6-4）
      13 輪只對 HeatedSeat 兩節做過逐位對照，Vented 兩節未做。
      (1) §1.3.2.1.3.3 與 §1.3.2.1.3.4 逐位配對（各 28 條相異）
      (2) 比對其「是否被同側 leaf 引用」與「方括號值是否對稱」
      (3) **不得用 difflib 序列比對定位**（14 輪已證其在樣板文字上失效，
          差 1 卻算出 shift = 2）
      (4) 併：列出 `scripts/layer3_w46.py` 之 `SEC_L3` 全部 21 筆
          章節→Layer 3 對照，供分析層確認（12 輪 §6-3 自陳其未經確認）

W-49  framework 定稿前之最後檢查
      (1) 依 R-VS37′ 重判後，逐 Layer 3 列出：leaf 數／對應章節／
          委派狀態分布（yes／no／blocked／pending）
      (2) 檢查每個 Layer 2 之 leaf 數合計是否等於
          46／88／72／31（R-VS15）
      (3) 列出 `framework.md` 鎖定前尚未解之項目清單（含 §2.4 之名稱
          衝突已解、DR-11／DR-15／DR-17 未決者）
      **framework 仍不鎖定** —— 鎖定屬 Pei（P19）

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
**不得清除或改寫 `spec_variables.tsv` 之原值**（31 包 §3）。
**不得鎖定 framework。**
**不得自行修改 in-scope 判準或 R-VS19**（R-VS19′ 待 Pei，P20）。

## 升級條件

W-47(3) 之不符值有判為**別名**（非 typo）者 —— 其表示值域本身有雙軌命名；
W-48(2) 之 Vented 兩節出現與 Heated 兩節不同型之不對稱；
W-49(2) 之四數與 R-VS15 不符；
實測與 31 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。
```

---

## 6. 待 Pei

| # | 事項 | 狀態 |
|---|---|---|
| **P20** | 裁 **R-VS19′**（Atlantis Mid，112 leaf 佔 47%） | **證據完整，已掛兩輪** |
| **P18** | 裁 **R-VS7(a)′**（委派句精度） | **證據完整（§4），建議 (a)** |
| P19 | framework 簽核 | 俟 W-49 之未解項清單 |
| — | **DR-15／DR-17 送出** | 二者皆已定稿未送 |
| — | **DR-18**（交叉前綴 typo） | **俟 W-47 掃全後由分析層擬** |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS37′ | Layer 3 歸屬之四分支（補跨異層、無 reqid） | 分析層 |
| `CrossZone Common` | Layer 3 跨區共通桶之定名 | 分析層 |
| `suspect_prefix` 欄 | 污染值標記而不改原值 | 分析層 |
| R-VS7(a)′ | 委派句改指名功能群 | **待 Pei（P18）** |
