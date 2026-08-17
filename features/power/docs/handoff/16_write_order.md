# 16 — 寫回排序規則與 dry-run

下放包 | 分析層 → 執行層 | 往返 NN = 16

前置：docs/upstream/15_batch1_closeout.md 之覆核於本包併行進行。

**本包處理一項十五包以來未被任何裁決涵蓋之缺口**：
工作簿列之排序。分批依據為 Test Set（R-P72），
而 Test Set 與 SWE-PM ID 之順序不一致；
`§10.3` 僅規範 tc_id 單調遞增，未規範列序，
亦未規範 tc_id 與 SWE-PM ID 之關係。
**此為分析層於 framework 定版時應處理而未處理者。**

現況：**已寫回 0 列**，tc_id 尚未落於客戶檔案，重新指派無代價。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

[R-P113] **寫回排序規則（選項 B）。**
        （a）**產出**仍依 Test Set 分批 ——
             §4.1.3 之價值（同一 Test Set 共用 setup 與 UI 進入路徑）
             於撰寫階段成立，不放棄。
        （b）**tc_id 於各批產出時為「批次內臨時編號」**，
             格式仍為 `NR1L-PowerManagement-{NNN}`，
             但**不具最終效力**，JSON 內須以
             `tc_id_provisional` 標明，或於批次檔頭註明其為臨時值。
        （c）**最終 tc_id 於寫回時一次指派**，
             依 **SWE-PM ID 遞增序**排列全部 TC 後，自 001 起連號。
        （d）**寫回為單次操作**，於全部 114 leaf 之 TC 產出完成後為之；
             不分批寫回。
        （e）工作簿列序即最終 tc_id 序，亦即 SWE-PM ID 序。
        裁決者 Pei，逐字依據：「當然是B」。

[R-P114] **首批 dry-run 寫回（沙箱副本）。**
        G66（B 欄非空列數 = TC 列數）、G71（`workbook.columns` 對實測標頭）、
        G72（profile §2/§3.3/§3.4/§3.7）三閘**至今僅有合成證據**，
        而 07 / 09 / 10 / 12 已四次證明「合成 fixture 過、真實資料壞」
        （A-PW35 / A-PW39 / A-PW50 / A-PW58）。
        R-P113(d) 之單次寫回會使該三閘之真實實測推遲至最後，
        風險不可接受。

        故：以首批 10 條對 **FW036 之沙箱副本**執行一次 dry-run 寫回，
        專為實測該三閘。

        （a）副本置於 `features/power/sandbox/`，**不入版控**
        （b）**客戶樹與 `inputs/` 之原始檔一律不得觸碰**
        （c）寫回路徑須為 `xlsx_surgical.py`（唯一授權之寫回路徑）；
             **不得以 openpyxl `save()` 為之**（R16 / R-G3）
        （d）dry-run 後須驗證副本之 DV（含 x14）是否存活 ——
             此即 R-G3 所載之已知缺陷，本次為首度實測
        （e）dry-run 之 tc_id 使用臨時編號 001–010，
             不代表最終指派（R-P113(b)）
        裁決者 Pei，逐字依據：「當然是B」（配套）。

[R-P115] **同一 leaf 內多條 TC 之次序 —— 分析層自裁。**
        依 charter，「批次排序與分批邊界」屬分析層得自裁之範圍，
        且本項為技術性確定性選擇，非 R-P15 所禁之
        「模糊指派之演算法 tie-break」。

        規則：同一 `req_id` 之多條 TC，依其**規格原文子句出現序**排列；
        該序即產出時之拆分序，記於 `split_index`（自 1 起）。
        `split_index` 不寫入工作簿，僅供排序與稽核。

        排序鍵為 `(SWE-PM ID 數值, split_index)`，二者皆為整數，
        全序且可重現。

        本條為分析層自裁，**Pei 得隨時推翻**；
        推翻時依 R-P36 加註，不改原文。
        裁決者：分析層自裁（charter §觸點與自裁界線）。

[R-P116] **`SWE-PM-089` 於工作簿中佔不佔列 —— 待 Pei 裁定。**
        該 leaf 依 R-P1 留空待 DR-PW1。
        其 ID 位於 088 與 090 之間，故有二種處置：
          （甲）保留一列空白（僅填 `req_id`），維持 ID 序之連續性
          （乙）整列跳過，工作簿無其痕跡
        二者影響列數、B 欄序號、以及客戶比對 037 時之觀感。
        **屬交付形式，分析層不自裁。**
        本包**不實作任何一種**，僅備妥素材（見 §B4）。
        裁決者：**待 Pei**。

（以上**四條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。R-P115 須標明為分析層自裁，
 R-P116 須標明為待裁。）

## B. 本包須產出

### B1. tc_id 臨時化（R-P113(b)）

  `batch_001_power_down.json` 之批次檔頭增設
    `"tc_id_status": "provisional"` 或等效標記
  **不改動現有十條之 001–010 值**（dry-run 需用）
  於 profile 增訂 tc_id 之兩階段指派規則

### B2. 排序腳本（R-P113(c) / R-P115）

  `scripts/assign_final_tc_id.py`
  輸入：全部批次 JSON
  排序鍵：`(int(req_id 之數字部分), split_index)`
  輸出：最終 tc_id 對照表 `data/final_tc_id_map.tsv`
  **本包僅以首批 10 條驗證其邏輯**，不指派最終值
  須含回歸斷言（R-P55）：首批 10 條之排序結果須為
    071×4 → 072×2 → 073×4，且 split_index 於各 leaf 內自 1 連號

### B3. dry-run 寫回（R-P114）—— **本包最重要之產出**

  建立沙箱副本，記錄其 SHA256 與來源
  以 `xlsx_surgical.py` 寫入首批 10 條
  寫回後逐項實測並回報：
    G66 —— B 欄非空列數 = 10
    G71 —— 17 組欄位對應之實際落點（逐欄回報寫入了哪一格）
    G72 —— profile §2/§3.3/§3.4/§3.7 之工作簿層檢查
    **DV 存活檢查** —— 四條 DV（含 x14 `S10:S221`）於寫回後
      之 `sqref` 與 type 是否與寫回前逐字相同（R-G3 首度實測）
    合併儲存格、條件式格式、分頁清單是否未變
  **與寫回前之工作簿做 XML 層 diff**，列出所有變動之 part

  **驗證條件**：三閘須確認其在該階段確實可能失敗 ——
  以刻意寫錯之副本（例如 B 欄留空、欄位偏移一格）證明其會 FAIL。

### B4. R-P116 之裁定素材

  Comfort 之已交付件中，是否存在僅填 `req_id` 而其餘欄留空之列？
    （`read_only=True`，依 R-P80 僅取結構性事實）
  037 之 SWE-PM-088 / 089 / 090 三筆之 `Requirement Title` 與
    `Categorization`，供判斷 089 之顯著性
  二種處置對列數、B 欄序號之具體影響（以 114 leaf 推算）

  **不得實作任何一種**，不得建議。

### B5. 15 包上繳之覆核回應（併行）

  分析層已讀 `001`–`007`、`010` 及 15 包修正後之 leaf 層資料。
  **`008` / `009` 全文仍未讀** —— 若 15 包上繳已附，
  本包無須重附；若未附，須於本包上繳補附，置於最前。

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G84 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G85** | 排序腳本邏輯（R-P113 / R-P115） | 首批排序結果 071×4 → 072×2 → 073×4；split_index 各 leaf 內自 1 連號 |
| **G86** | dry-run DV 存活（R-P114(d)） | 【實測填入】四條 DV 之 sqref 與 type 寫回前後是否逐字相同；**含 x14** |
| **G66** | B 欄非空列數 = TC 列數 | **10 / 10（真實）**；並以刻意留空之副本證明其會 FAIL |
| **G71** | `workbook.columns` 對實測標頭 | **17 / 17（真實）**；並以偏移一格之副本證明其會 FAIL |
| **G72** | profile 條款之工作簿層檢查 | **（真實）**；並證明其會 FAIL |
| **G87** | dry-run 之 XML 層 diff | 【實測填入】變動之 part 清單；非預期變動須逐項說明 |

G66 / G71 / G72 之證據型別於本包後應由「合成」升為「合成＋真實」（R-P99(c)）。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  新增 A-PW73：工作簿列序與 tc_id 對 SWE-PM ID 之關係
               自 01 包起至 15 包止未被任何裁決涵蓋；
               分批依 Test Set 而 §10.3 僅規範 tc_id 單調遞增，
               二者組合會使 SWE-PM-001 落於工作簿後段。
               **為分析層於 framework 定版時應處理而未處理者**
  新增 A-PW74：G66 / G71 / G72 三閘至 15 包止僅有合成證據，
               而「合成過、真實壞」已發生四次（R-P114）
  新增 A-PW75：R-G3（openpyxl `save()` 破壞 x14 DV）於本 feature
               為首度實測（G86）

## G. DATA_REQUESTS

  DR-PW1 → live，High（併 R-P116 之待裁）
  DR-PW3 / DR-PW6 → live，Medium
  DR-PW5 → live，High
  DR-PW7 → live，Low
  DR-PW2、DR-PW4 → 維持撤回
  無新增

## H. 作業指示

  1. G0 前置閘
  2. 依 R-P113(b) 標記 tc_id 為臨時（B1）
  3. 實作 B2 排序腳本，驗 G85
  4. 執行 B3 dry-run 寫回，驗 G66 / G71 / G72 / G86 / G87 —— **最重要**
  5. 備妥 B4 之 R-P116 裁定素材 —— **不得實作、不得建議**
  6. 依 B5 補附 `008` / `009` 全文（若 15 包未附）
  7. 以 §D 全表自驗
  8. §A 四條裁決逐字抄入 RULINGS.md（R-P115 標自裁、R-P116 標待裁）；
     §F 入 ANOMALIES.md
  9. 上繳 features/power/docs/upstream/16_write_order.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回客戶樹之 FW036，亦不得寫回 `inputs/` 之原始檔**
  **dry-run 僅得對 `features/power/sandbox/` 之副本為之（R-P114(a)(b)）**
  **不得以 openpyxl `save()` 寫任何 xlsx —— dry-run 亦然（R16 / R-G3）**
  **不得指派最終 tc_id（R-P113(c) 於全部 114 完成後方為之）**
  **不得實作或建議 R-P116 之任一處置**
  不得執行任何 git 操作（全數屬 Pei）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得自行調整 §E（R-P35）
  不得因 A-PW46 / A-PW51 改變車型欄之留白處置（R-P54、R-P81）
  不得依 15 包 §B5 之 Arif 素材自行改動 G77 或任何 TC（Q3 屬 Pei）
  不得擴大批次範圍超出 `Power Down` 3 leaf
  不得以 repo 現況作為任何 fixture 之測試對照
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P113 寫回排序規則（選項 B）：Test Set 分批產出、
         tc_id 寫回時依 SWE-PM ID 序一次指派、單次寫回
  R-P114 首批 dry-run 寫回，實測 G66 / G71 / G72 與 DV 存活
  R-P115 同一 leaf 內多條 TC 依規格子句出現序（**分析層自裁**）
  R-P116 `SWE-PM-089` 佔不佔列（**待 Pei 裁定**，本包不實作）

  逐條確認：**四條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 4、§J 列數 = 4、§H 步驟 8 寫「四條」，三處一致。

---

## 上繳包必附

  一、B3 dry-run 之完整實測（G66 / G71 / G72 / G86 / G87），
      含三閘之「刻意寫錯即 FAIL」證明
  二、**DV 存活之逐條前後對照（含 x14）** —— R-G3 首度實測
  三、B2 排序腳本與 G85 結果
  四、B4 之 R-P116 裁定素材（不得含建議）
  五、`008` / `009` 全文（若 15 包未附）
  六、§D 全表實測值對照（含 G85–G87）
  七、「本包是否仍有該驗而未驗者」之獨立判斷。

---

## 追加條文（隨下放包一併發出）

[R-P117] **`SWE-PM-073` 之涵蓋缺口補測。**
        R-P109 補齊 `4942354` 完整原文後，
        分析層以其 13 項行為與現有四條 TC 對照，發現三項未測：
        （a）**Load Shed 之回復分支** —— 原文載
             `the last values ... shall be used until load shed signal
             broadcast resumes`，而 `008` 僅測「不恢復→維持整個
             ignition key cycle」，未測「恢復→回正常」。
             對照 Battery Critical 有 `009`（進入）與 `010`（回復），
             Load Shed 有進入、有故障、**無回復**。
        （b）**通話轉移** —— 原文於 Load Shed 與 Battery Critical
             兩處皆載 `The TLM shall transfer the call
             (not-Ecall/ACN call) to the head set in case a continuing
             call is still active`，**兩處皆未測**。
        （c）**BODY OFF-TIMED 與 voltage out of range** ——
             原文載 `While in BODY ON **or BODY OFF-TIMED** mode`，
             而 `009` 之 pre-condition 僅 `BODY ON`；
             原文之回復條件為 `until either **voltage out of range**
             conditions are satisfied or ... 10 seconds after ...`，
             而 `010` 僅測後者。

        依 §7（獨立分支須拆）與 §8.3（mode 為拆分軸）補測。
        補出之 TC 沿用臨時 tc_id，接續 011 起編（R-P113(b)）。
        `SWE-PM-073` 之 TC 數因此增加，**leaf 數仍為 3，
        不構成 R-P72 所禁之範圍擴大**。

        另記：此三項於 14 包不可見 —— 當時 `source_clause` 之 `...`
        恰好蓋住相關條款。R-P109 之實際效用因此超出其立條理由
        （立條理由為「ER 斷言之依據須可查」，
         實際另用於「查出規格說了而 TC 沒測者」），
        比照 A-PW31 登記。
        裁決者 Pei，逐字依據：「看一下上繳 確認之後我一起下放16」。

### B6. `SWE-PM-073` 涵蓋缺口補測（R-P117）

  以 `4942354` 完整原文逐句拆出全部行為項，編號列表
  逐項標明：已由哪一條 TC 覆蓋 / 未覆蓋
  對未覆蓋者補寫 TC，臨時 tc_id 自 011 起
  補寫後重跑完整 lint（含 G63 / G73 / G77 / G79 / G81 / G45）
  **對 `SWE-PM-071` / `SWE-PM-072` 之 `source_clause` 亦做同樣之
  逐句行為項對照**，回報有無同型缺口
