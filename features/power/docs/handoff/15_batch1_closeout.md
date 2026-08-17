# 15 — 首批覆核收尾與誤讀清除

下放包 | 分析層 → 執行層 | 往返 NN = 15

前置：docs/upstream/14_final_step_intent.md 已覆核，判定 **ACCEPT**。
G77 修正前實測 9 / 10，高於分析層自六條推估之 5,
反向檢查未觸發停止條件，判定與閘門互相印證。

分析層已覆核 `001`–`007`、`010`（**8 / 10**），
以三條 `source_clause` 原文逐字對照，發現三項。

**寫回仍不開放。** 阻斷條件為 R-P105（剩 `008` / `009` 未覆核）
與 R-P107（誤讀殘留）。

**Q3（Final Step 措詞之 canon 與實務衝突）Pei 尚未裁定，
本包不代填、不自裁，見 §B5。**

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

[R-P107] **誤讀之修正須掃全部十三欄，不得只改主要欄位（G81）。**
        14 包依 R-P103 修正 `006` 之時序誤讀，
        已改 `tc_title`、`test_procedure`、`expected_result`
        及 leaf `reasoning` 四處，
        **而 `split_reason` 仍載「緩衝之事件於開機完成後依
        TLM_Status.Info setting 之轉換處理」** ——
        誤讀殘留於一個**會寫進工作簿之欄位**。
        改四處、漏第五處。

        往後任何語義層修正，須逐欄掃描全部十三欄
        （`tc_title` / `test_item` / `pre_conditions` /
         `input_test_data` / `test_procedure` / `expected_result` /
         `specification_reference` / `design_method` / `priority` /
         `split_flag` / `split_reason` / `functional_safety` / `remarks`）
        加上 leaf 層之 `reasoning` 與 `reasoning_note`，
        並逐欄回報「已檢查 / 已修正 / 無涉」。

        補設閘門 G81 —— 以本次誤讀之關鍵詞
        （`after boot completes` / `開機完成後` 等）為黑名單，
        掃全部欄位。此閘為**個案型**，其價值在於證明修正確已完成，
        不宣稱可攔下未來之其他誤讀。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 Q1 之 T6）。

[R-P108] **`006` 之 ER 不得斷言處理順序。**
        ER2 載「the TLM_Status transitions follow the injected order」，
        而 `4942338` 原文僅載
        `process them as soon as possible, depending on boot timings` ——
        **未載按注入順序處理**。FIFO 為推論，非規格。
        且 `TLM_Status.Info setting` 之轉換定義位於 CFTS009 §1.6.2.1.15，
        依 R-P42 不在本 leaf 之範圍內。
        （a）刪除該順序斷言；或
        （b）若 `4942338` 之完整原文確載順序，逐字引出並保留
        二擇一，須附依據。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 Q1 之 T7）。

[R-P109] **`source_clause` 之截斷不得遮蔽該 TC 所斷言之內容（R-P104 補述）。**
        `007` 之 ER3 斷言「the TLM is muted and the ICS module powers down」，
        而其 `source_clause` 之 `...` **恰好蓋住 mute 與 ICS 之條款**。
        截斷落在最需查證處，使 R-P104 之立意落空。
        規則：`source_clause` 得截斷，但**該 TC 之 `expected_result`
        所斷言之每一項行為，其規格依據必須完整出現於 `source_clause` 中**。
        若因此過長，須另附全文檔並於 `source_clause` 標明檔名與位移。
        **R-P104 依 R-P36 原文不改**，於其下加註指向本條。
        補設閘門 G82（若可機械化）：`expected_result` 中之關鍵名詞
        是否於 `source_clause` 有對應；不可機械化者明列理由。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 Q2）。

[R-P110] **`reasoning_note` 欄位追認並定義。**
        R-P102 令「於各該 TC 之 `reasoning` 逐字記載」，
        而 TC 層原無 `reasoning` 欄（僅 leaf 層有），
        執行層自行新增 `reasoning_note` 並同時寫入 leaf `reasoning`。
        該處置合理，**追認**，但須有名分：
        寫入 Power profile，定義其用途為
        「TC 層之個案判斷記錄，補 leaf 層 `reasoning` 之不足；
         不寫入工作簿，僅供覆核」。
        並明訂其與 `split_reason` 之分工：
        `split_reason` 述拆分理由（寫入工作簿），
        `reasoning_note` 述判斷依據（不寫入工作簿）。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 §七(甲)5）。

[R-P111] **18 字上限與「末步須揭示所檢查者」之衝突登記為
        可預見之結構問題，不預先開例外。**
        十條中 `006` / `008` / `010` 三條已頂到 §5.2B 之 18 字上限。
        若後續 leaf 之驗證標的更多，該上限將與 §5.5 直接衝突。
        **本包不預設例外條款** —— 待實際撞上時，
        以該具體案例為據裁定，避免以假想情境放寬 canon。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 §七(甲)4）。

[R-P112] **首批覆核之剩餘範圍：`008` / `009`。**
        分析層已覆核 `001`–`007`、`010`，共 8 / 10。
        本包上繳須附 `008` / `009` 全文，**置於最前**。
        R-P98 / R-P105 於分析層完成十條覆核前維持有效。
        另記 14 §七(甲)2 之自陳：`005` 判無誤者與寫出 `006` 誤讀者
        為同一判斷來源 —— 該風險由分析層之獨立覆核承擔，
        T6 / T7 即為其生效之實證。
        裁決者 Pei，逐字依據：「出 15 包」（回應 14 Q4）。

（以上**六條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. `008` / `009` 全文 —— **置於上繳包最前**

十三欄逐條，含 `reasoning`、`reasoning_note`（如有）與 leaf `source_clause`。
**不得節錄、不得省略換行。**

### B2. `006` 之誤讀清除（R-P107）

  修正 `split_reason`
  逐欄掃描十三欄 ＋ leaf `reasoning` / `reasoning_note`，
    **逐欄回報「已檢查 / 已修正 / 無涉」**
  對其餘九條同樣執行一次全欄掃描，回報有無同型殘留
  實作 G81 並回報實測

### B3. `006` ER 之順序斷言處置（R-P108）

  取 `4942338` **完整原文**（不截斷）
  判定其是否載有處理順序
  依 (a) 或 (b) 處置，附逐字依據
  修正後重跑 lint

### B4. `source_clause` 截斷規則（R-P109）

  依 R-P36 為 R-P104 加註，雜湊佐證原文未變
  逐條檢查十條之 `expected_result` 所斷言之行為，
    其規格依據是否完整出現於 `source_clause`
  不足者補齊 `source_clause`（或另附全文檔）
  評估 G82 之可機械化程度；不可機械化者明列理由

### B5. Q3 待裁素材 —— **不得自行裁定**

Pei 尚未裁定 Final Step 措詞之 canon 與實務衝突
（canon §5.2B 要求驗證意圖措詞；已交付語料實測 **0 / 472**）。

本包**不改變現行實作**（G77 依 canon），僅備妥裁定素材：

  取 **Arif 之 144 列 done region**（Home feature 工作簿）之
    `test_procedure` 末步，逐條列出
  統計其中含驗證意圖措詞者之比例
  與 Comfort / Privacy 之 472 條末步分別比較
  列出 Arif 版末步之典型措詞形態（前 10 種）

理由：記憶中 Arif 之 144 列為全案格式權威，
較 Comfort / Privacy 之整體統計更直接。

輸出至 `features/power/data/b5_arif_final_step.md`。
**不得據此改動 G77 或任何 TC** —— 素材備妥後由 Pei 裁定。

### B6. `reasoning_note` 入 profile（R-P110）

  Power profile 增訂該欄位之定義與其與 `split_reason` 之分工

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G80 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G81** | 誤讀關鍵詞全欄掃描（R-P107） | 修正前 `006` 之 `split_reason` 應觸發；修正後十條 0 findings |
| **G82** | ER 斷言之規格依據完整性（R-P109） | 【實測填入】可機械化程度；十條之不足數與補齊後結果 |
| **G83** | `006` ER 順序斷言（R-P108） | 【實測填入】`4942338` 完整原文是否載順序；處置為 (a) 或 (b) |
| **G84** | R-P104 加註後原文位元組未變（B4） | UNCHANGED |
| **G63 / G73 / G77 / G79** | 沿用 | 修正後仍全數 PASS |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 仍 3；TC 仍 10 |

G81 之驗證條件：**須以修正前之 `006` 實證該閘確實會觸發**，
不得僅以修正後 0 findings 宣稱 PASS。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  A-PW68 → 依 R-P107 更新：該誤讀之清除本身亦不完整，
           `split_reason` 殘留一輪
  新增 A-PW69：語義誤讀之修正改四處漏第五處，
               而漏掉者為會寫入工作簿之欄位（R-P107）
  新增 A-PW70：`006` ER 斷言處理順序，規格未載（R-P108）
  新增 A-PW71：`source_clause` 之截斷恰好遮蔽待驗證內容，
               使 R-P104 之立意落空（R-P109）
  新增 A-PW72：canon §5.2B 與已交付實務（0 / 472）衝突，
               待 Pei 裁定；現行實作依 canon（R-P101 / Q3）

## G. DATA_REQUESTS

  DR-PW1 → live，High
  DR-PW3 → live，Medium
  DR-PW5 → live，High
  DR-PW6 → live，Medium
  DR-PW7 → live，Low
  DR-PW2、DR-PW4 → 維持撤回
  無新增

## H. 作業指示

  1. G0 前置閘
  2. 輸出 B1 `008` / `009` 全文 —— **置於上繳包最前**
  3. 依 R-P107 清除 `006` 誤讀殘留並全欄掃描十條（B2），驗 G81
  4. 依 R-P108 處置順序斷言（B3），驗 G83
  5. 依 R-P109 為 R-P104 加註並補齊 `source_clause`（B4），驗 G82 / G84
  6. 依 §B5 備妥 Arif 末步素材 —— **不得據以改動任何實作**
  7. 依 R-P110 將 `reasoning_note` 寫入 profile（B6）
  8. 修正後重跑完整 lint，驗 G63 / G70 / G73 / G77 / G79
  9. 以 §D 全表自驗
 10. §A 六條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
 11. 上繳 features/power/docs/upstream/15_batch1_closeout.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回 FW036 workbook（R-P98 / R-P105 未完成前一律不開放）**
  **不得對任何 workbook 呼叫 `save()`**（R-G3）
  不得執行任何 git 操作（全數屬 Pei）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  不得自行調整 §E（R-P35）
  不得因 A-PW46 / A-PW51 改變車型欄之留白處置（R-P54、R-P81）
  不得修改 Comfort / Home / Privacy 之任何交付物；B5 一律 `read_only=True`
  不得調整 `MIN_FINGERPRINT`（R-P62）
  不得擴大批次範圍超出 `Power Down` 3 leaf
  **不得依 B5 之素材自行改動 G77 或任何 TC（Q3 屬 Pei 之裁定）**
  **不得為 18 字上限預先開設例外（R-P111）**
  不得以 repo 現況作為任何 fixture 之測試對照
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P107 誤讀修正須掃全部十三欄（G81）
  R-P108 `006` ER 不得斷言處理順序
  R-P109 `source_clause` 截斷不得遮蔽 ER 所斷言之內容（R-P104 補述）
  R-P110 `reasoning_note` 追認並定義
  R-P111 18 字上限衝突登記，不預先開例外
  R-P112 首批覆核剩餘範圍 `008` / `009`

  逐條確認：**六條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 6、§J 列數 = 6、§H 步驟 10 寫「六條」，三處一致。
