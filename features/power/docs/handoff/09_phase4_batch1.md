# 09 — 補閘與 Phase 4 首批

下放包 | 分析層 → 執行層 | 往返 NN = 09

前置：docs/upstream/08_lint_parity.md 已覆核，判定 **ACCEPT**。
R-P65(c) 就此滿足，**Phase 4 起跑條件三項齊備**。

本包為八包以來第一次撰寫 TC。補閘與首批**並行**，不再串接。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P66] **§10.7 之閘門補設（G45）。**
        R-P62「不調 `MIN_FINGERPRINT`」之安全論證載明：
        「該 81 個仍受閘門 (a) 保護，且 §10.7 要求
         `specification_reference` 必填 —— 缺口實為
         『逐字抄錄內容』且『未列來源』二重違規之交集，非單一漏洞。」
        實測 §10.7 **無任何閘門**，故該論證所稱之「二重」
        實際僅一重具強制力。
        此非描述失準，係**裁決之論證前提不成立**，
        較 A-PW30 / A-PW32 之修飾語誤述嚴重。
        補設閘門：`specification_reference` 須非空，
        且每一項須符 `{spec_filename}_{section_id}` 形態。
        R-P62 依 R-P36 原文不改，於其下加註指向本條。
        裁決者 Pei，逐字依據：「出」（回應 08 Q2）。
```

```
[R-P67] **偽陽性之量測形態改變（取代事前估計）。**
        G41 之 22 條語料由本包撰寫者自撰，量測者與被量測對象同源；
        G42 之 1183 條雖獨立，但屬不同領域，其詞彙與 Power 重疊本即低，
        0 命中不足以證同領域安全。
        **不再要求造出獨立語料** —— 撰寫者為同一層，
        硬做僅為換裝之自證。
        改為：Phase 4 期間，閘門 R-P42(b) 之任何觸發
        **一律不得自動判 FAIL**，須人工裁決並逐條登記
        （判為「真違規」或「偽陽性」及其依據）。
        累積至首批完成後統計真實偽陽性率，據以再議 R-P62 之門檻。
        即：以真資料之持續量測，取代造不出來之事前估計。
        裁決者 Pei，逐字依據：「出」（回應 08 Q1）。
```

```
[R-P68] **G40 分布檢查改為子集檢查**（不追認 08 §1.2 之原讀法）。
        原實作僅於 `len(leaves) == 114` 時比對分布，
        致該項在 Phase 4 全程 99% 時間關閉。
        改為每批皆驗：
        （a）各 Test Set 之已產出 leaf 數 **≤** 定版數（63/24/16/8/3）
        （b）逐 leaf 之歸屬與 `data/leaf_testset.tsv` 相符
        （c）`len(leaves) == 114` 時，再驗完全相等
        （a）可攔下「整批一致地歸錯」——原讀法攔不下。
        裁決者 Pei，逐字依據：「出」（回應 08 Q3、Q6）。
```

```
[R-P69] **`feature.yaml` 更新，lint 權威仍取自裁決條文，另設一致性閘。**
        該檔自 scaffold 以來從未更新，與 R-P9 / R-P3′、R-P2 相牴觸
        （`spec_mode` 為 `A` 實為 `D`；`test_group` 為 `Power`
         實為 `Power Management`；`paths.*` 全為 placeholder；無 tc_id 格式欄），
        而其開宗明義稱「所有 feature 常數住在這裡」——
        該檔留置即為陷阱，Phase 4 寫回將直接使用 `workbook.columns`。
        （a）更新該檔使其與裁決條文一致，並補 tc_id 格式欄
        （b）**lint 之權威值仍取自裁決條文**，不改為讀該檔
        （c）新增閘門 G46 驗二者一致，以偵測未來漂移
        （d）盤點 `workbook.columns`、`done_region`、
             `spec_reference_template` 等其餘欄位是否與實測相符
        裁決者 Pei，逐字依據：「出」（回應 08 Q4）。
```

```
[R-P70] R-P63 之「同章且同一父節」讀法**追認**
        （tier 1 = 182 / tier 2 = 133 / tier 3 = 499）。
        併同採納執行層之自陳：該分層之有效性**目前無資料可驗**
        （「tier 1 真的比 tier 2 危險嗎」未經驗證），
        登記為已知限制，待 Phase 4 產生實際誤納樣本後回頭檢視。
        裁決者 Pei，逐字依據：「出」（回應 08 Q5）。
```

```
[R-P71] **首批上繳前須以真實檔案執行完整 lint 並回報。**
        現況所有閘門僅在合成 fixture 上驗證過，`generated/` 尚不存在。
        fixture 驗證了「邏輯正確」，未驗證「能讀真實檔案」——
        `load_tcs()` 之 JSON 解析、欄位缺漏容錯、大量 TC 之效能皆未測。
        07 包之 `\b` bug 即「邏輯看似正確而實際不觸發」之先例。
        裁決者 Pei，逐字依據：「出」（回應 08 Q7）。
```

```
[R-P72] **Phase 4 首批範圍：`Power Down`（3 leaf）。**
        擇此為首批之理由：
        （a）**最小**（3 leaf），首批之目的是驗證管線而非產量
        （b）**唯一橫跨 CFTS010 者**，可一併驗證雙 CFTS 之
             `specification_reference` 產生路徑（R-P4）
        （c）其三個 leaf（`SWE-PM-071/072/073`）之解析章節已由
             G5b 驗明（§1.7.1.1.1 ×2、§1.7.2 ×1），來源明確
        （d）不觸及任何懸空參照（DR-PW6 之影響面限於 §1.6.2.1，
             屬 Power State）
        首批**不得擴大範圍**；後續批次之切分於 10 包另議。
        裁決者 Pei，逐字依據：「出」。
```

（以上**七條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. 補閘（R-P66 / R-P68 / R-P69(c)）

  G45 —— §10.7：`specification_reference` 非空，
          每項符 `{spec_filename}_{section_id}` 形態
  G40 改為 R-P68 之三項子集檢查
  G46 —— `feature.yaml` 與裁決條文一致

  三者皆須合成 fixture，違規案例須**實際觸發**（同 G33 之要求）。

### B2. `feature.yaml` 更新與盤點（R-P69(a)(d)）

  更新四項不符欄位，補 tc_id 格式欄
  盤點 `workbook.columns` / `done_region` / `spec_reference_template`
    與實測之相符情形，逐欄回報
  `workbook.columns` 須與 03 包 G12 所測之 FW036 座標對照
    （表頭 r9、資料 r10–r221、c2–c35）

### B3. R-P62 之加註（R-P66）

  依 R-P36 原文不改，於 R-P62 下加註：
    「註記（R-P66，09 包）：本條所稱『§10.7 要求
     `specification_reference` 必填』於立條時**無任何閘門**，
     故所稱之『二重違規之交集』實際僅一重具強制力。
     此為論證前提不成立，非描述失準。
     閘門已由 R-P66 補設（G45）。原文保留。」
  加註後須以雜湊佐證原文位元組未變

### B4. Phase 4 首批 —— `Power Down` 3 條 TC（R-P72）

對 `SWE-PM-071` / `072` / `073` 產生 TC，**嚴格遵循 §1–§13 之 TC 內容規則**。
特別注意：

  §4.2 Test Set = `Power Down`（定版，R-P35）
  §10.3 tc_id = `NR1L-PowerManagement-{NNN}`，自 001 起連號
  §10.2 priority 依 §10.2 rubric 自**測項內容**判定，
        **不得**自 037 `Priority` 欄推導（R-P8）
  §10.7 `specification_reference` 須列該 TC 直接驗證之全部章節，
        格式 `{spec_filename}_{section_id}`；
        三條皆源自 CFTS010，檔名以 `inputs/` 內之實際檔名為準
  §12 design_method 於 procedure 定稿後指派，
      值須為 `下拉選單!A1:A9` 九詞條之一（A-PV10 / R23-6）
  §11 無 trailing period；UI 標籤用雙引號不用方括號
  §5.1 禁用 `observe` / `verify` 等主動詞
  §10.5 至少兩個編號步驟
  **R-P42：不得測試未被引用之錨點**

輸出至 `features/power/generated/batch_001_power_down.json`。

### B5. 真實檔案 lint（R-P71）

  對 B4 之產出執行完整 lint（含 G33、G37–G40、G45、G46）
  回報：各閘結果、執行時間、任何 `load_tcs()` 之解析問題
  若 R-P42(b) 觸發，依 R-P67 **不得自動判 FAIL**，
    須人工裁決並登記（真違規 / 偽陽性 ＋ 依據）

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G44 沿用（G17 已移除），期望值不變。
G40 依 R-P68 改為三項子集檢查。

| # | 項目 | 期望值 |
|---|---|---|
| **G45** | §10.7 閘門（R-P66） | fixture 正常 PASS、違規實際 FAIL（空值一例、格式錯誤一例） |
| **G46** | `feature.yaml` 一致性（R-P69(c)） | fixture 正常 PASS、違規實際 FAIL |
| **G47** | 首批 TC 數與 leaf 涵蓋 | 3 個 leaf（`SWE-PM-071/072/073`）；TC 數 ≥ 3（依 §8.2.2 得 > 3） |
| **G48** | 首批 lint 全閘 | 全數 PASS；R-P42(b) 若觸發，依 R-P67 人工裁決後登記 |
| **G49** | 首批 `specification_reference` | 全部指向 CFTS010，且所引章節皆在 §1.7.1 / §1.7.2 之內 |

G45 / G46 之驗證條件同 G33：**須確認其在該階段確實可能失敗**。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  A-PW33 → 依 R-P66 更新：其安全論證所依賴之 §10.7 閘門已補設
  A-PW36 → 依 R-P69 處置，`feature.yaml` 已更新
  新增 A-PW37：R-P62 之安全論證前提不成立（§10.7 無閘門），
               為分析層首次**論證前提**層級之錯誤，
               有別於 A-PW30 之修飾語誤述
  新增 A-PW38：G43 分層之有效性無資料可驗，
               待 Phase 4 實際誤納樣本後回頭檢視（R-P70）

## G. DATA_REQUESTS

  DR-PW1 → live，High（`SWE-PM-089` 留空，不影響首批）
  DR-PW3 → live，Medium
  DR-PW5 → live，High（影響 `SWE-PM-003`，屬 Power State，不影響首批）
  DR-PW6 → live，Medium（影響面限 §1.6.2.1，不影響首批）
  DR-PW7 → live，Low
  DR-PW2、DR-PW4 → 維持撤回

  **五張 live DR 皆不阻斷首批** —— 此為 R-P72 擇 `Power Down` 之附帶效益。

## H. 作業指示

  1. G0 前置閘
  2. 依 R-P66 補 G45，依 R-P68 改 G40，依 R-P69(c) 補 G46；fixture 驗證
  3. 依 R-P69(a)(d) 更新並盤點 `feature.yaml`
  4. 依 R-P66 為 R-P62 加註（B3），驗雜湊未變
  5. 依 R-P72 產出首批 3 leaf 之 TC（B4）
  6. 依 R-P71 對真實檔案執行完整 lint（B5），驗 G48
  7. 以 §D 全表自驗
  8. §A 七條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
  9. 上繳 features/power/docs/upstream/09_phase4_batch1.md，更新 docs/INDEX.md

## I. 禁區

  不得寫回 FW036 workbook（首批僅產出 JSON，寫回於後續包另議）
  不得執行任何 git 操作（全數屬 Pei）
  不得以 openpyxl save 寫任何 xlsx（R16 凍結）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  不得變更 §E 之分布數字（R-P35）
  不得以 A-PW29 之存在逕行填寫車型欄（R-P54）
  不得調整 `MIN_FINGERPRINT`（R-P62）
  **不得擴大首批範圍超出 `Power Down` 3 leaf（R-P72）**
  **R-P42(b) 之觸發不得自動判 FAIL（R-P67）**
  **不得以 repo 現況作為任何 fixture 之測試對照**
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P66 §10.7 補閘（G45）；R-P62 論證前提不成立
  R-P67 偽陽性改為 Phase 4 期間之持續量測，(b) 觸發須人工裁決
  R-P68 G40 改為子集檢查，每批有效
  R-P69 `feature.yaml` 更新，lint 權威仍取自裁決條文，另設 G46
  R-P70 R-P63 分層讀法追認；有效性登記為無資料可驗
  R-P71 首批上繳前須以真實檔案執行完整 lint
  R-P72 首批範圍 = `Power Down` 3 leaf，不得擴大

  逐條確認：**七條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 7、§J 列數 = 7、§H 步驟 8 寫「七條」，三處一致。
