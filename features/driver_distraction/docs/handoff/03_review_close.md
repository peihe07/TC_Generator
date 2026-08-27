# 下放包 03 —— 上繳包 01 審結、編號歸屬處分、036 母本補位（T8）、framework 鎖定提案

- 日期：2026-08-27
- 方向：分析層 → 執行層 ＋ Pei（§五 framework 鎖定待裁）
- 前一包：`02_rulings_q1q6.md`；對應上繳：`docs/upstream/01_scaffold_recon.md`
- 裁定狀態：編號歸屬（§二）、`_x000D_` 候選作廢（§二）—— 分析層即裁並自認一誤；
  framework 鎖定 —— **提案，待 Pei**

---

## 一、上繳包 01 審查判定

**收。T-抄 5/5 逐字元相符、T1–T7 全數完成，閉合檢查通過。** 逐項：

1. **T1 `--adopt-existing`** —— 採認。「答案已在 repo 裡」再添一例；
   讀腳本再動手之順序正確。
2. **T2 五檔真型態** —— 採認。包 01 §一之偽型態預警本就標明「針對分析層
   轉換副本」，執行層據實解除而非沿襲，補位作用達成。
3. **A-DD1 複測 + §4.1 補充表** —— 採認。「複測才寫、量測與結論分離、
   判斷歸上游」三項皆正確；補充表併 DR-DD1 發送。
4. **A-DD2（PARK_BRK）之三理由不代換** —— **採認，並記入案例**。
   自評 #1 所述「`-129` 未被更正是寫理由時才注意到的」值得留：
   **寫理由這道工序本身把真正站得住的證據逼了出來** ——
   R-13 之紀律不是只擋錯，它會產出證據。此為制度之作用，非個人克制。
5. **自評 #4 `Sub Categorization` 尾空白** —— 採認留原樣。
   加一條拘束：**日後任何以該欄為鍵之比對一律 verbatim 含尾空白**，
   或於比對端明文 rstrip 並揭露；不得靜默修資料。

## 二、編號歸屬處分（含分析層一誤）

台帳（ANOMALIES.md）**先登先得**，包 01 §二文中之候選編號依台帳修正：

1. **A-DD2 = PARK_BRK 件**（執行層所登）—— 定案。
2. 包 01 候選「狀態命名兩制」（CFTS `Locked/Unlocked` vs 037
   `RESTRICTED/NOT_RESTRICTED`）→ **補登 A-DD3**，狀態 **RESOLVED**：
   R-DD3 已定 ER 主錨為 HMI 現象，**兩列舉皆不得出現於 ER**；
   test_item 上半 verbatim 照 037 原文（含 RESTRICTED 措辭），
   不改字。登記即結案，無待決。
3. 包 01 候選「A-DD3 `_x000D_` 正規化」→ **作廢，不登異常**。
   **分析層之誤**：該候選之前提為「test_item 上半 verbatim 取 CFTS 描述文」，
   實則上半取 037 Requirement Description（生成主驅動），而 037 實測
   `_x000D_` 0/28。CFTS 側之殘留（`-120`/`-121`）只在引用 CFTS 內文時
   才需正規化，本 feature spec_reference 為 ObjectID、無引文需求。
   T4 之原文欄照留（無害），正規化條款不入 canon。

執行層：ANOMALIES.md 補登 A-DD3（§二-2 逐字），並於 A-DD2 條目上方
加一行註記「包 01 §二 之候選編號 A-DD2/A-DD3 已由本包 §二 重配，
以台帳為準」。

## 三、036 母本補位 —— T8（含分析層一誤之更正）

**包 01 T2 漏列工作簿母本為分析層之誤**，本包補位：

| # | 任務 |
|---|---|
| T8a | 自 `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`（已 list_directory 驗在場）複製為 `features/driver_distraction/workbook/driver_distraction_00.xlsx`。**`cmp` 逐位元全等 + sha256 雙驗**；此副本**自始不得經 openpyxl 存回**（R 欄 x14 下拉摧毀，A-UP09 同族） |
| T8b | 開副本實測 D2 儲存格，**R-DD2 之閘於此補跑**：`newR1L` 相符即回填 `feature.yaml` `tc_id_format` 生效註記；不符即停並回報 |
| T8c | `feature.yaml` 回填：`paths.workbook`、`workbook_state`（實測 BLANK/DONE-REGION 判定附依據）、`workbook.sheet`/`header_row`/`columns` 逐項自副本表頭實測（bed_lowering 為 row 9 起，**本 feature 以實測為準，不轉錄**）、`reference.workbook_master` sha |

## 四、下一輪之分析層預告（非執行層任務）

- **priority 對映草案**：037 為 28/28 High，IN §10.2 須落 P0–P3。
  Driver Distraction 屬行車安全域（鎖定失效 = 行駛中可操作受禁 feature），
  草案傾向 P0/P1 為主，逐 leaf 表下包出，交 Pei 裁。
- **profile 起草**（R-DD3(c)）：逐 leaf 之 HMI 錨對照（Fullscreen Lockout
  流程圖、Standard Lockout Popup、Lockout Tables 之 R1L 適用欄），
  以 S3/S4 為據。pilot 前定稿。

## 五、framework 鎖定提案（待 Pei 裁）

包 01 §三草案經 T3/T4/T6 實測後**無需改動**，提請鎖定：

- Layer 1：`Driver Distraction`（R-DD1 已定）
- Layer 2：六組，閉合 2+6+4+4+8+4 = 28 ✅
- 組 6 `Market Speed Gating`（leaf 025–028）：**PENDING 標記隨鎖**——
  該 4 leaf 已凍結（A-DD1），組名為中立佔位，DR-DD1 回覆後
  依裁併組 5 或更名 `LATAM Market`，屆時 framework 重出該表即可，
  不影響其餘五組之批次規劃
- Layer 3：CFTS Heading 母號承載（-110/-119/-123/-130）

**准則執行層落 `framework.md`（LOCKED，組 6 除外標 PENDING），
並開 pilot 規劃**；不准則指示改法。

---

## 六、任務彙總

| # | 任務 |
|---|---|
| T-登 | §二 之 A-DD3 補登 + A-DD2 條目註記 |
| T8a–c | §三 之母本補位三項 |
| （待裁後）| framework.md 落檔（§五 准後） |

**不在本輪**：profile、priority 表、任何 TC、寫回、git。

## 七、上繳包要求（`docs/upstream/02_workbook_binding.md`）

1. T-登 結果
2. T8a cmp/sha 雙驗輸出；T8b D2 實測值；T8c feature.yaml diff
3. 未結 DR 清單（DR-DD1、DR-DD2，狀態隨 Pei 發送與否更新）
4. 獨立自評
5. 量測條件揭露（R-G8）
