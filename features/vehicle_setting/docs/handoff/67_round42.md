# 67 下放包 — 42 輪：pilot sheet、writeback dry-run、batch18

分析層寫入，2026-08-23。**本包為單一完整下放，執行層讀本檔即可作業。**

**目標**：把 129 條推到可貼回之狀態。三項作業，一項不生成新內容（W-120 只 dry-run）。

---

## 貼入 Claude Code 之內容

```text
你是 FW036 TC 生成管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator
本輪為 Vehicle Setting 之第 42 輪。

## 先讀

  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  docs/runtime/ASPICE_SWE6_AI_Instruction.md                TC 內容規則
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md feature override
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/65_review_round41.md 前輪覆核
  features/vehicle_setting/docs/handoff/66_writeback_procedure.md 貼回程序
  features/vehicle_setting/docs/handoff/67_round42.md         本輪依據（本檔）

現況：交付 **129 條**／母體 237／池 **16**。
未經任何 pilot 者 **43 條**；pilot #3 已出 sheet（13 條）未分類。

## 禁區

- **全部 git 寫入性操作不執行**。需入庫者備指令給 Pei（帶 pathspec）。
- **不寫回 036 工作簿** —— W-120 只做 dry-run，**實寫待 Pei 核可**。
- 不補素材、不代擬條文、不自行調和數字。各版保留不刪。
- 不得將「行為未抽出」計入「查無」（65 包 §2）。
- 不得合併 A-VS119／A-VS123 之 leaf。
- **不得動 036 母本之列 1–9、其他分頁、或 §3 表以外之欄。**

## 文書

D-1  依 R-VS18 建 docs/upstream/37_pilot_and_writeback.md，六節先留空。
D-2  逐字轉錄 65 包 §1 之 **R-VS62′**、§2 之 **R-VS55(2)** 入 RULINGS.md；
     R-VS62 標「經 R-VS62′ 取代」（原文保留）。
D-3  DATA_REQUESTS.md：**DR-8′ 標「撤回，R-VS62′」**（原文保留）；A-VS140 關閉。
D-4  delegation_lookup.tsv 同步 R-VS59：**廢除 `blocked` 之值**
     （36 輪 §4 記其尚未同步）。
D-5  ANOMALIES.md 依 R-VS35 **分線列**兩數（主線／VF230 線分開）。
D-6  本輪結束前以骨架 ⬜／✅ 對照各節實際內容，空節而標 ✅ 者列為不一致。

## 作業（三項，R-VS25）

### W-118  pilot #3＋#4 之合併 review sheet

母體 **43 條**（batch14 10／15 13／16 10／17 10）。

pilot #4 之抽樣（**15 條**）：
  **必檢 8**（新形態，不抽樣）：batch16／17 之 `Fail_Present` 類各取 4
    —— 其畫面層全為 `PENDING`、Priority 為 R-VS56 之 P0(b)，二者皆首次交付
  **分層 7**：維度 = batch（14／15／16／17）× `dr_dependent`（有／無）
    交叉格內各取 reqid 最小者；不足 7 時自條數最多之格補足

產 `docs/reports/pilot4_sheet.md`：每條含十欄全文 ＋ `dr_dependent` ＋
`priority` 及其所依類別 ＋ `screen_source` ＋ 來源條文逐字節錄。
**另附 `pilot3_sheet.md` 之 13 條清單**（只列 leaf_id ＋ 批次，不重出全文）。
**列抽樣之交叉格矩陣**使抽法可複現。

### W-120  `writeback_036.py` ＋ dry-run（**不實寫**）

母本：
```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/
Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT
STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx
```
分頁 `Test Case Specification 測試用例規範`；表頭列 9；資料列 10 起。

**欄位對映**（66 包 §3；只寫下列欄，其餘一格不動）：
```
B  No.#                     流水號自 1
C  Requirement or Design    037 之 Requirement Title
D  Requirement or Design ID swe_id
F  Test Case ID             {project}-{abbr}-{NNN}，生成器指派，單調遞增
G  Test Group               Vehicle Setting（全表同值）
H  Test Set                 四值之一
I  Test Item                上半 037 逐字 ＋ 空行 ＋ 下半括號內（R-VS6）
J  Pre-Conditions           pre_conditions
K  Input Test Data          一律 NA（R-VS5）
L  Test procedure           test_procedure
M  Expected Result          expected_result
N  Specification Reference  CFTS044-{7位數}，**一個一行**，禁 , ; 串接
P  Test Case Priority       P0／P1／P2（R-VS56，不用 P3）
R  Test Case Design         受控 9 值之「中文 (English)」形態
AA Test Case Author         （Pei 之姓名，本輪以 <AUTHOR> 佔位，實寫前由 Pei 指定）
AH Remarks                  畫面層 PENDING 者寫 BLOCKED: DR-{n} ＋ 待補來源
```
`reasoning` **不入工作簿**。E／O／Q／S／T–Z／AB–AG 留空。

**dry-run 之輸出**（`docs/reports/writeback_dryrun.md`）：
  (1) 將寫入之列數，與 129 之對照
  (2) 逐欄之非空數（16 欄），與 JSON 側之逐欄非空數並列
  (3) **N 欄之多值列**：其行數分布（1 行者幾列、2 行者幾列…）
  (4) **I 欄之上下段結構**：含空行者幾列、括號成對者幾列 —— **應為 129/129**
  (5) K 欄非 `NA` 者之列數 —— **應為 0**
  (6) P 欄之三級計數；R 欄不在受控 9 值內者之列數 —— **應為 0**
  (7) AH 欄非空者之列數 —— **應為 21**（`delivery_disclosure.md` 之數）
  (8) 現有 237 列將被清空之欄範圍（B–AH），及其清空前之非空數

**錨點（R-VS54，須可失敗）**：
  以一份**刻意違規之 JSON**（K 欄非 NA／N 欄逗號串接／I 欄無空行／
  R 欄用純英文）餵入 dry-run，(4)(5)(6) 三項須各自報出違規；
  與正常輸入同批執行並列回報。

**實寫之閘**：dry-run 通過且 Pei 核可後，方得執行實寫。
**本輪不得實寫。**

### W-119  batch18 —— 10 條

自現行池（16）依 R-VS58 優先序選取。**池不足 10 時取全部並回報其數。**
套 profile ＋ canon §8.7.5（依 R-VS52 之 profile override）＋
R-VS43／R-VS48′／R-VS49／R-VS51／R-VS56／R-VS57／R-VS59～R-VS62′ ＋
Sibling Rows ＋ 無效值優先序。
§9 十七項自檢 ＋ DBC／LID 值表核對 ＋ R-VS54 之錨點。

**併**：A-VS138 之 4 條已交付未更正者（通風／方向盤節內誤引
`*_HS_STATFailSts`），本輪一併更正，產 `_v{n+1}`，原版保留。

## 升級條件

W-120 之錨點三項有任一未報出違規；
W-120(4) 之上下段結構非 129/129，或 (5) 非 0，或 (6) 非 0，或 (7) 非 21；
W-119 之池不足 10（**預期命中** —— 池 16，取 10 後餘 6）；
§9 出現新型違規。

## 完成後

分析層出 pilot #3＋#4 共 28 條之合併建議分類，Pei 覆核；
覆核通過 ＋ dry-run 通過 ＋ 母本備份完成（66 包 §2 之三道 gate）後，
方進實寫。**本輪不進實寫。**
```

---

## 待 Pei（**與本輪並行，不互相等待**）

| # | 事項 |
|---|---|
| 1 | **母本備份 ＋ sha256**（66 包 §4 步驟 0）—— G3 |
| 2 | **`AA` 欄之作者姓名** —— dry-run 以 `<AUTHOR>` 佔位，實寫前須指定 |
| 3 | **DR-25′（解 23）／DR-19（7）／DR-15′ 補送** —— 池兩輪見底，此三份是唯一活路 |
| 4 | pilot #3＋#4 之 28 條覆核 —— 分析層於 W-118 產出後出分類 |
