# 上繳 01a：canon 條文回寫

執行層：Opus5（Claude Code）｜日期：2026-08-21｜純文件編輯，新規 0 條

## 1. diff 摘要

```
docs/runtime/ASPICE_SWE6_AI_Instruction.md | 61 ++++++++++++++++++++++--------
1 file changed, 46 insertions(+), 15 deletions(-)
```

`git diff --stat` 於本包範圍內僅此 1 檔（另二檔屬 01b，見該上繳）。
行數 604 → 635。

## 2. sha256

| | 值 |
|---|---|
| 編輯前 | `fa9833ae64c9092fb1fb10cbce303c0eaba7239b055e1505ce141c35ad1b147a` |
| **編輯後** | **`f265b17236370cd56c3c680426eba2fde3aa8cf9ce4a37db66dfa339a5064177`** |

## 3. 各區塊插入位置（編輯後行號）

| # | 區塊 | 裁決 | 插入位置 | 起始行 | 手法 |
|---|---|---|---|---:|---|
| 1 | `### 4.3.1 test_item 兩段式` | R-S4／R-3／R-4 | §4.3 末（Sibling-distinction 段後、§4.4 前） | 148 | 插入 |
| 2 | `#### 8.4.3 缺件佔位` | S6 | §8.4 末（§8.4.2 後、§8.5 前） | 439 | 插入 |
| 3 | `#### 8.7.5 訊號記法` | R-1 | §8.7 末（§8.7.4 後、§9 前） | 502 | 插入 |
| 4 | `### 10.7 specification_reference` | R-2 | §10.7 全節 | 583 | **替換**（原 16 行 → 新 11 行） |
| 5 | §11 收斂段 | S2／N-1 | §11「No trailing period」段後、「UI element labels」段前 | 599 | 插入 |
| 6 | `[OVERRIDE-R5][DEFAULT]` | R-5 | §1 末（§2 前） | 7 | 插入 |

六個區塊均逐字照抄下放包，未增刪字元。錨點皆以「唯一命中」斷言驗證
（`assert s.count(anchor) == 1`），避免誤插。

區塊 4 為唯一刪除來源：原 §10.7 之英文 15 行（`{spec_filename}_{section_id}`
格式與 6 條 Rules）全數由家族分流條文取代，此即 diff 之 15 deletions。

## 4. 舊 sha256 引用處之處置

全庫搜尋舊 hash `fa9833ae…` 得 2 處，**均未更新**，理由如下：

| 檔案 | 性質 | 處置 |
|---|---|---|
| `features/projection/docs/upstream/21_canon_s8_and_charter.md:100` | 歷史上繳包之比對紀錄（「L99–EOF vs canon｜hash｜**相同**」） | 保留原值 |
| `features/projection/docs/upstream/22_rp99_and_git.md:84` | 同上（L102–EOF） | 保留原值 |

兩者記錄的是**當時**之比對事實，非現行權威值；改寫將使歷史紀錄失真
（同 R-TM13「撤銷之裁決保留不刪」之精神）。

下放包所稱「Project 指示內註記」不在 repo 內 —— `docs/runtime/PROJECT_INSTRUCTION.md`
與 `OPERATING_CHARTER.md` 均無 canon 之 sha256 pin（僅第 94 行有「涉及檔案狀態者
一律對 repo 查證」之通則）。**該註記應位於 Pei 之 Claude Project 自訂指示，
執行層無法存取，須由 Pei 手動更新為 `f265b172…`。**

## 5. 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項：**

1. **新條文與既有條文之衝突未逐條掃描。** 已知一處：§4.3 訂 tc_title
   長度 **2–14 words**，新增之 §4.3.1 訂 test_item 上半 **50 token** 上限。
   canon 中 `test_item` 與 `tc_title` 於 §4.3 標題並列（`Test Item / tc_title`），
   兩者是否為同一欄位未明；若同一欄位則 14 words 與 50 token 併存需釐清適用層級
   （建議：§4.3 管標題型，§4.3.1 管 verbatim 型，但此為推論，未經裁定）。
   其餘章節之交互作用（§8.6 Spec Reference Hierarchy vs 新 §10.7）未逐條比對。
2. **§10.7 替換後之下游引用未追。** 原 §10.7 之格式範例
   （`Media_HMI_Logic_and_Flow_R1_..._4.1`）可能被 profiles、prompt builder
   或既有 feature 文件引用；本包未搜尋 `specification_reference` 之下游消費點，
   亦未驗證 `docs/runtime/profiles/` 是否有依賴舊格式之 override。
3. **新條文未經 lint 實作對應。** R-3（50 token）對應 lint L、S4（括號下半）
   對應 lint I／I-sibling、S6（PENDING）對應 lint M、R-5（雙語豁免）對應
   lint K —— 四者之 lint 端配置**均未依新條文調整**（尤以 R-5 明訂
   「lint K 對此二本配置豁免」，現行 lint 無 feature 層豁免機制，
   BT K=1043、Projection K=648 仍全額計入）。本包為純文件編輯，
   未觸 lint 程式碼，此為跨包缺口，非本包遺漏，但須有人接手。
4. **canon 生效日之語意未定義。** §11 新段稱「自 canon 生效日起適用」，
   但 canon 本身無版本或生效日欄位；何日、對哪些既有交付本適用，
   文件內無可判之依據。

## 6. 引用之既有裁決

R-1、R-2、R-3、R-4、R-5[DEFAULT]、S2、S4、S6（條文本體即本包所寫入者）；
N-1（§11 新段之「續行同受規制」與其一致）；R-TM13（歷史紀錄保留，見 §4）。
編號落檔見 `docs/fw036/RULINGS_LEDGER.md`（01b 建置）。
