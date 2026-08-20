# 00F — 交付執行層之啟動指令（Claude Code）

> **[SUPERSEDED by 00I_claude_code_prompt_v2.md —— 全文]**
> 2026-08-20。本檔於 00G（LID 表）與 00H（DBC 語意）之後於三處失真：
> DBC 之 R4/R5 語意、CAN 訊號之第一權威、素材清單（12 檔 → 14 檔）。
> **不得照本檔作業**；保留作為當時判斷之記錄。


分析層寫入，2026-08-20，同一往返（NN = 00）。
本檔即 Pei 貼入 Claude Code 之文字；落檔以免只存在於聊天（A-PJ62／A-PJ78）。

貼入時機：**12 檔素材已在 `features/vehicle_setting/inputs/`（已確認）。**
`5-A`（Comfort HMI L&F）尚未入 `inputs/` 亦可啟動 —— 本輪不生成 TC。

---

```text
你是 FW036 TC 生成管線的執行層。專案根目錄：
/Users/peihe/Work_Projects/TC_Generator

本輪為 Vehicle Setting 之 Phase 0/1（進場與偵察）。本輪不生成任何 TC，
不寫回任何工作簿。

## 先讀（依序，全部讀完再動手）

1. docs/fw036/FEATURE_ONBOARDING.md            ← 流程權威（tier、gate、§5a 數字紀律、§8 契約）
2. docs/runtime/ASPICE_SWE6_AI_Instruction.md  ← TC 內容規則（本輪僅供理解，不套用）
3. features/vehicle_setting/docs/handoff/00_intake_and_rulings.md
4. features/vehicle_setting/docs/handoff/00A_data_requests_refined.md
5. features/vehicle_setting/docs/handoff/00B_named_documents.md
6. features/vehicle_setting/docs/handoff/00C_inputs_verification.md
7. features/vehicle_setting/docs/handoff/00D_tlm_hmi_document_search.md
8. features/vehicle_setting/docs/handoff/00E_open_items.md

**五篇補篇在數處互相修正。衝突時以 00E 為準**，其餘保留作為證據。
00 包之 §3 六條裁決（R-VS1～R-VS6）為本輪之權威條文，逐字適用。

## 禁區

- **全部 git 寫入性操作一律不執行**（add/commit/checkout/restore/stash/
  clean/tag）。唯讀 git 可跑，但上繳時須與改狀態之 git 分列。
  需要入庫者，在上繳包內「準備好指令」給 Pei 執行，且一律帶 pathspec。
- 不寫入 036 母本或任何交付件。
- 不補入素材：發現需要而未到之檔案 → 寫進 DATA_REQUESTS.md 並回報，
  不自行下載、複製或搬移（含自 /Users/peihe/Work/ 之客戶目錄）。
- 不代擬裁決條文：引用之裁決若無正文，回報而不自行補寫。
- 不自行調和數字：實測與預期不符時停下回報。

## 作業

### A 組（可立即並行，不等任何裁定）

W-0  python scripts/new_feature.py "Vehicle Setting" --adopt-existing
     （docs/handoff/ 之六個檔案不得被覆寫；--adopt-existing 即為此設計）
W-1  對 inputs/ 12 檔逐檔 shasum -a 256 → inputs/INPUTS.sha256
W-2  四份 037 合併 leaf 全集 → data/leaves.tsv
     欄位：swe_id / family / src_ref / title / desc
     取 'Analysis Report' 表、表頭列 7、資料自列 8、A 欄非空者為 leaf
W-3  036 現況重測 → docs/reports/036_baseline.md
     資料列 10–246、逐列、逐欄填充率；逐列驗 I/H/N 是否等於 037 之
     desc/title/src（R-VS1 之依據是否成立）
W-4  錨鏈對照表 → data/sysra_to_polarion.tsv
     SYS-RA-CFTS044-N → SYS2 'Basic Report' 第 N 筆資料列（工作表列 N+1）
     → A 欄 NRL id → 'Source Requirement items' 7 位數
W-4b outline map → data/outline_map.tsv
     自 CFTS044 原始 docx 之 word/styles.xml 解出 styleId 1-7 = heading 1-7，
     取 body heading（應為 270 個，全部帶章節號與 {7位數}），
     需求段落以 '[Artifact Type' 錨定（應為 2030 個），
     以位置法歸屬 → leaf → CFTS044 章節號
W-5  反向驗證 W-4/W-4b：須含「什麼都沒做」之對照向；
     並證明 offset -1 / +1 之命中為 0（R-G7-1）
W-6  覆蓋差：leaf 全集 − 036 現有 D 欄值
W-7  異常登記（登記，不裁定）→ ANOMALIES.md
     已知待登記：A-VS01（SYS-RA 指向 SYS2 之 Heading/Information 列）、
     A-VS03～A-VS10（見 00B §4、00C §7、00D §7）
W-8  $變數$ 全集 → data/spec_variables.tsv
     正則 \$[A-Za-z0-9_]+\$（區分大小寫），逐 token 附：
     037 出現次數、所屬 family、CFTS044 內之值域（兩式：
     `$var$ = [值]` 與 `路徑.名稱 == "值"`）、DBC 內對應 signal 名與
     message 名與 VAL_ 值表
W-11 DATA_REQUESTS.md 依 00E §1 填實（每項含路徑與 SHA）
     並記一句：「已查 features/comfort/inputs/ 三份與 26PI2.5/HMI 四份，
     本 feature 條文不引用者不取用」——查過而不用須留痕（G-D）
W-12 scripts/recon.py → RECON.md + DECISIONS.md + recon.json；
     feature.yaml 填 spec_mode = D
W-13 對 /Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/
     'R1LR SR26 ATL-H'/26PI2.5/HMI/ 之全部 PDF 與 XLSX（約 112 檔）
     跑全文掃描，關鍵詞：Fail_Present / STATFailSts /
     'Heated Steering Wheel Icon' / 'Left Side' / 'Right Side'
     目的：以餘數驗證 00D「失效彈窗不在該目錄」之結論（R-G10）
     **唯讀掃描，不複製任何檔案入 inputs/**
     PDF 須先驗文字層產出量；抽不到者標「未解析」不猜（canon §5a 第 12 條）

### B 組（做完必停）

W-9  Comfort 重疊逐條對照 → docs/reports/comfort_overlap.md
     來源：features/comfort/inputs/
     FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx
     逐條列出命中座椅加熱／通風／方向盤加熱之 Comfort leaf 與其對應之
     本 feature leaf。
     **產出後停止，不得繼續。** 等 R-VS7 裁定（三選項見 00A §3）。

### 附帶查驗

- 讀 00_intake_and_rulings.md 之 §1 第 6 點，以位元層確認其中是否有
  多位元組字元毀損（分析層讀回時顯示為 '沙\ufffd\ufffd'）。
  若確有毀損，回報並提出修正字串，**不逕行改寫**。

## 預期數字

00 包 §5.2 列有 24 項預期值，**全部量自沙箱副本，非 repo 物件**。
逐項在 inputs/ 實體檔上重測並於上繳包列出「預期 vs 實測」，**相符者亦列出**。
不符者逐項說明，不自行調和。

00C／00D 另有以下實測值可作對照：
- CFTS044 docx：PK zip、28 member、body heading 270、需求段落 2030
- leaf → 章節解析：245 / 25（有 id 無章節）/ 1（無 id）
- 245 leaf 落在 20 個相異章節
- 兩份 DBC：R4_BHCAN 883 signals / 155 messages；R5_FDCAN8 1755 / 323
- HSW_StatFailSts 僅存在於 R4_BHCAN（STATUS_CSWM, id 1169）

## 上繳

寫入 features/vehicle_setting/docs/upstream/00_intake_and_rulings.md，須含：

1. 預期 vs 實測逐項對照（相符者亦列）
2. 不符項目逐項說明（不調和）
3. 結果三分法分類：改對了／核實無誤／正確地不動
4. 本輪實際使用之掃描條件揭露（欄位範圍、大小寫、詞界）
5. W-5 之反向驗證實測（含對照向）
6. 新開 anomaly 與 DATA_REQUESTS 條目，成對
7. 未預期之發現（本包未涵蓋而執行時撞到者）
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
9. 給 Pei 之 git 指令草稿（帶 pathspec，不執行）

並更新 features/vehicle_setting/docs/INDEX.md（分析層不寫此檔）。

## 升級條件（撞到即停，其餘不受影響之作業繼續）

1. 任一實測與預期不符
2. 錨鏈在任一 leaf 上不成立（offset 非 +1、指向列不存在、章節歸屬矛盾）
3. W-9 完成（必停）
4. 037 四檔間出現同一 SWE ID，或同一 SYS-RA 被兩 leaf 共用
5. 036 母本結構與 forms/…_SWQT_20260817_ext.xlsx 不一致
6. 撞到 §8.4.1 之編造壓力
7. 需要判斷而 canon／00 包皆無條文

## 尚未裁定（本輪不得預設答案）

R-VS7  Comfort 43 leaf 之委派界線
R-VS8  基線 DBC（R4_BHCAN vs R5_FDCAN8）
R-VS9  CAN 訊號書寫形式（$var$ vs DBC 逐字 signal 名）
R-VS10 Pop Up List 基線版本

四項皆不影響 A 組。遇到需要它們的判斷 → 登記待判，繼續其他作業。
```

---

## 使用說明（不屬貼入內容）

- 貼入後執行層應先回報「已讀八份、禁區已知、A 組開始」再動手
- A 組完成即上繳一次；**W-9 之停點在 B 組**，不與 A 組合併上繳
- 若 MCP 或檔案讀取逾時：自動重試一次，連兩次失敗才回報
