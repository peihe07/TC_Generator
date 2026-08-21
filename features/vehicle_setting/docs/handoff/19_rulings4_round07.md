# 19 下放包 — R-VS27／R-VS28 裁定與 07 輪指令

分析層寫入，2026-08-20。Pei 裁定兩條，並指出分析層近數輪之流程漂移。

> **流程更正（記於此以免再漂）**：下放包之作業指示屬分析層自裁範圍
> （Operating Charter「分析層得自裁 …… 下放包之作業指示」）。
> 近數輪分析層於覆核末尾改為「要指令跟我說」，形同把已完成之設計
> 再送一次徵詢 —— 該徵詢無新資訊，只增加一次往返。
> **自本包起恢復：覆核與指令同包出，不另問。**
> 需 Pei 裁者僅為條文與 Tier 3 動作，二者於包末具名列出即可。

---

## 1. 裁決正文（執行層逐字轉錄入 `RULINGS.md`）

### 1.1 R-VS27

```
R-VS27（Pei 2026-08-20）
歸因類別 C4（規格引用子集）不得單以「CFTS 側為他來源之真子集」成立。
須加一項必要條件：

  C4 成立 ⟺ 單向子集 **且** 該值域所在之 CFTS044 條文
            **不含窮舉宣告**

窮舉宣告之判準（字面，區分大小寫）：條文內含
    `Valid values for the`
  或 `All other states shall be considered invalid`

若條文**含**窮舉宣告而其值集合仍為他來源之真子集 →
**不歸 C4，一律進待判**，並登記為疑似真漏列。

理由：窮舉宣告是規格作者對「這就是全部」之明示；
在其之下的子集不是引用，是矛盾。

配套：C4 之輸出須附 `exhaustive_marker` 欄（true／false／not_found），
`not_found` 者（無法定位其來源條文）**亦進待判**，不得預設為 false。

實測基數：CFTS044 全文 `Valid values for the` 49 處、
`All other states shall be considered invalid` 48 處，
其中 in-scope（含 Atlantis High）者 15 條。
```

### 1.2 R-VS28

```
R-VS28（Pei 2026-08-20）
一項作業連續**四輪**未執行者，下輪成為**該輪唯一作業**，
不得與任何其他作業同輪，亦不得有前置插隊。
若其確有未完成之前置，則該前置本身成為該輪唯一作業，
且下放包須具名說明其為前置之依據。

理由：R-VS21 保證排序、R-VS25 保證長度，二者併用仍不能保證出清 ——
一項只要每輪都有前置，就能無限期延後。本 feature 已出現兩次
（W-27 兩度成為頭部並各自用掉整輪，W-9 因而延至第五輪）。
```

---

## 2. 07 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/18_review_round06.md 本輪依據
  features/vehicle_setting/docs/handoff/19_rulings4_round07.md 裁決與本指令
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入作業數）

D-1  依 R-VS18 建立 docs/upstream/06_comfort_overlap.md，六節先留空，
     逐項完成即填。
D-2  逐字轉錄 19 包 §1 之 R-VS27 與 R-VS28 入 RULINGS.md。
D-3  ANOMALIES.md：
     - 新開 A-VS31：LID 表 `VentedSeatFL` 之 Format 內
       `1= Fail Present`（缺空格、`Fail_Present` 之底線遺漏），
       與 `HeatedSeatFL` 之 `1 = Fail_Present` 不一致；
       足以使字面比對誤判為不同值。RD-1 FYI 類。
     - 於 W-27 條目補記錨點 (a) 之措辭更正（18 包 §1 之 W-27(a)′）：
       判準為**條目數 = 11**，鍵值對 10 為附帶量。

## 作業（**本輪唯一作業，R-VS28**）

W-9  Comfort 逐條對照 → docs/reports/comfort_overlap.md

     來源：features/comfort/inputs/
           FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx
           （498 leaf；`Analysis Report` 表、表頭列 7、資料自列 8）

     (1) Comfort 側：逐條列出命中座椅加熱／通風／方向盤加熱之
         SWE1-HVAC-* leaf。00D 之上界為 43（子字串、無詞界）——
         **本輪須以詞界重測並列出兩種計數**，差額逐筆說明。

     (2) 本 feature 側：母體為 **237 個 Functional leaf**（R-VS15），
         **非 271**。以 data/leaves.tsv 之 Functional 子集為準。

     (3) 逐條配對：每個 Comfort leaf 對應本 feature 之哪些 leaf
         （得為 0、1 或多）。配對依據須具名（共同之訊號名／
         共同之 CFTS044 章節／共同之 UI 元件），**不得只憑關鍵詞相同**。

     (4) 另附 CFTS044 內文以 `{CFTS043}` 引用 Comfort 規格之 3 處上下文
         （各前後 200 字元），作為 R-VS7 分層委派之文件層佐證。

     產出為 R-VS7 委派句之來源表：TC 撰寫時於 reasoning 指名
     Comfort 對應 leaf id 者，即查本表。

     **必停已由 R-VS7 解除**，做完併入本輪上繳。

**W-22 排 08 輪**，且依 R-VS27 之新判準執行。
**W-17／W-24／DR-14′ 追問、`unesc()` 併入 lid_parse.py 模組排 09 輪。**

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
衍生檔之刪除屬 Pei（R-VS26(3)）；.gitignore 之修改屬 Pei。

## 升級條件

W-9 之詞界重測與 00D 之 43 差距過大而無法逐筆歸因；
配對依據無法具名（僅關鍵詞相同）之 leaf 超過三成；
實測與 18／19 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
本輪無「必停」項。

## 完成後

W-9 為 framework 之最後前置。其完成後、且 DR-15 有答覆時，
framework Part Vehicle Setting ＋ profile（Tier 2）方可開始。
**本輪不做 framework。**
```

---

## 3. 待 Pei（**僅此二項**）

| # | 事項 |
|---|---|
| — | 03／04／05 三輪產物入庫；推送（分支領先 origin 11+） |
| — | **DR-15 之 RD-1 提問送出**（17 包 §2.3，18 包 §2 之佐證已使其更精確） |

**無待裁條文。** R-VS7～R-VS28 全數裁定完畢。

---

## 4. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS27 | C4 須加窮舉宣告之必要條件（裁定） | ✔ §1.1 |
| R-VS28 | 連續四輪未執行者成為唯一作業（裁定） | ✔ §1.2 |
