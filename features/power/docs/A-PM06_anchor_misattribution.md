# A-PM06：anchor_attribution 跨文件錯配（2026-08-21）

分析層為執行 spec_reference 收斂（M16／R-12(b)）而對 69 列分類，
過程中查出錨點來源本身之缺陷。**本異常推翻 DR-PW19 之前提。**

## 一、分類結果（69 列超過 4 條者）

| 類 | 列數 | 特徵 |
|---|---|---|
| determined=True | 38 | f1=1.0，但 spec_ref 仍列 6–10 條 |
| determined=False | 31 | f1 0.428–0.576，候選 8–13 個 |

**全 283 列之對應關係（決定性）**：

| attribution | 列數 | spec_ref 條數 | 列數 |
|---|---|---|---|
| determined（候選 1） | 125 | 1 條 | 125 |
| 候選 2 | 40 | 2 條 | 40 |
| 候選 4 | 41 | 4 條 | 41 |
| 候選 8 | 15 | 8 條 | 15 |
| 候選 13 | 11 | 13 條 | 11 |

**逐級吻合。** 證實 spec_ref 條數 = attribution 候選數，
即「候選全集」被寫入欄位以代替「選定一條」。

## 二、錨點本身錯配（比條數問題更嚴重）

實測：**125/125 determined 列與 155/155 undetermined 列，
其 attribution anchor 皆不在該列現有 spec_ref 清單內。**

追查具體案例 —— `NR1L-PowerManagement-001`（row 10）：

| 項目 | 內容 |
|---|---|
| req_id | SWE-PM-071，determined=**True**，f1=**1.0**，候選 1 |
| attribution anchor | **4942337** |
| anchor 所在文件 | **CFTS010 Power Down**（CFTS009 內 0 次出現） |
| anchor 內容 | `TLM boot requires following timings: After SplashScreen_Time the splash screen is loaded and shown…` |
| 現有 spec_ref | CFTS009-4941354／4941355／4941357／4941358／**4941360**／4941453 |
| 4941360 內容 | `All TLM, AMP/ICS/DTV functionalities are available.` |
| 該列 ER | 1. The TLM is ON／2. All TLM, AMP, ICS and DTV functionalities are available |

**該列 ER 與 CFTS009-4941360 逐字對應；與 anchor 4942337 之
splash screen timing 無關。** 即：f1=1.0 之最高信心錨點指向
**另一份文件的另一個主題**。

全案 **16 筆 TC 之 anchor 落在 CFTS010，而 spec_ref 標 CFTS009**
（含 PowerManagement-001～006 等 determined 列）。

## 三、判定

1. **`anchor_attribution_53.json` 不得作為 spec_reference 之收斂依據。**
   determined／f1 並非正確性指標 —— f1=1.0 仍可跨文件錯配。
   （f1 係文字相似度，非語意對應；相似度高不蘊含指涉同一需求。）
2. **現有 spec_ref 之內容方向正確**（CFTS009 清單與 036 內容吻合），
   問題僅在**條數未收斂**。
3. **DR-PW19 之前提修正**：問題非「上游未提供權威對照」，
   而是「本地 attribution 演算法產生跨文件錯配」。DR 內容須改寫。
4. 執行層 10a 保留 A5 之決定**正確**，且理由應升級：
   非「44% determined 不足」，而是「determined 亦不可信」。

## 四、收斂之可行方法（提案，待 Pei 裁定）

不倚賴 attribution，改以 **036 實際內容 ↔ CFTS 原文逐條比對**：
對每列取 `test_item` 上半 verbatim 與 ER，於 spec_ref 現有候選
清單內比對文字重疊，選出直接對應之 object，其餘刪除。
此法之來源為 036 自身內容與 CFTS 原文（皆為權威），
不引入第三方推定。

作業量：283 列，其中 125 列已為單條（僅需驗證非錯配）、
158 列需收斂。屬分析層內容判斷，不下放。

## 五、暫定處置

spec_reference（M16／R-12(b)）**全案凍結**，不列入本次下放。
其餘七項（R-1 v3 訊號可觀察化、R-9 PC 編號、R-10 空白、
R-11 拆步補值與 Input 內聯、R-12(a) PC 句式）不受影響，照常進行。
