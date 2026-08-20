# 00I — 交付執行層之啟動指令 v2（**取代 00F**）

分析層寫入，2026-08-20，同一往返（NN = 00）。
**`00F_claude_code_prompt.md` 標為 SUPERSEDED by 本檔** —— 保留不刪，
其內容在 00G／00H 之後已於三處失真（DBC 語意、訊號權威、素材清單）。

前置：Pei 已裁定兩份新素材入 `inputs/`（見 §0 之 R-VS12）。
**檔案之實體搬移由 Pei 或執行層執行，分析層無法寫入二進位檔。**

---

## 0. 本輪之授權變更（貼入前先讀）

```
R-VS12（Pei 2026-08-20）
下列兩份素材授權入 features/vehicle_setting/inputs/：

  1. Logical Identifiers and CAN Mapping v1.76.xlsx
     用途：CAN 訊號逐字名、所屬 message、網段、值域之第一權威（00G）
  2. PDT25_E3A_R4_FDCAN8_vs_PDT25_E3A_R5_FDCAN8.xlsx
     用途：證據性素材，為「R4/R5 語意須由檔內屬性判定」之判準來源
     （00H §1.1）。與本 feature 之訊號無交集，入庫目的為存證非取值

入庫後 inputs/ 應為 14 檔。兩檔須列入 INPUTS.sha256。
本授權僅及於這兩檔；其餘素材補入仍須逐案授權。
```

---

## 1. 貼入 Claude Code 之內容

```text
你是 FW036 TC 生成管線的執行層。專案根目錄：
/Users/peihe/Work_Projects/TC_Generator

本輪為 Vehicle Setting 之 Phase 0/1（進場與偵察）。
本輪不生成任何 TC，不寫回任何工作簿。

## 先讀（依序，全部讀完再動手）

1. docs/fw036/FEATURE_ONBOARDING.md            ← 流程權威（tier、gate、§5a 數字紀律、§8 契約）
2. docs/runtime/ASPICE_SWE6_AI_Instruction.md  ← TC 內容規則（本輪僅供理解，不套用）
3. features/vehicle_setting/docs/handoff/00_intake_and_rulings.md
4. features/vehicle_setting/docs/handoff/00A_data_requests_refined.md
5. features/vehicle_setting/docs/handoff/00B_named_documents.md
6. features/vehicle_setting/docs/handoff/00C_inputs_verification.md
7. features/vehicle_setting/docs/handoff/00D_tlm_hmi_document_search.md
8. features/vehicle_setting/docs/handoff/00E_open_items.md
9. features/vehicle_setting/docs/handoff/00G_lid_mapping.md
10. features/vehicle_setting/docs/handoff/00H_dbc_release_semantics.md
11. features/vehicle_setting/docs/handoff/00I_claude_code_prompt_v2.md   ← 本檔

00F 已作廢（SUPERSEDED），不要照它作業。

各篇在數處互相修正，**衝突時之優先序**：
    00H > 00G > 00E > 00D > 00C > 00B > 00A > 00
00 包 §3 之六條裁決（R-VS1～R-VS6）為權威條文，逐字適用，未被任何補篇取代。

已作廢之陳述（**不得沿用，讀到時視為錯誤**）：
- 00A §2 第 4 項「$HSW_StatFailSts$ 需外部 CAN 字典」→ 00B §0 已更正
- 00C §5-3 與 00E §2 之 R-VS8「兩份 DBC 分屬不同 release」→ 00H §0 已推翻
- 00E §2 之 R-VS9 建議「以 DBC 逐字名為第一權威」→ 00G §2 已修訂為 LID 表
- A-VS07 原描述作廢，改為 A-VS07'（00H §2）

## 禁區

- **全部 git 寫入性操作一律不執行**（add/commit/checkout/restore/stash/
  clean/tag）。唯讀 git 可跑，但上繳時須與改狀態之 git 分列。
  需要入庫者，在上繳包內「準備好指令」給 Pei 執行，且一律帶 pathspec。
- 不寫入 036 母本或任何交付件。
- **不補入素材，惟 R-VS12 明列之兩檔除外**（見作業 W-0b）。其餘發現需要
  而未到之檔案 → 寫進 DATA_REQUESTS.md 並回報，不自行下載、複製或搬移
  （含自 /Users/peihe/Work/ 之客戶目錄）。
- 不代擬裁決條文：引用之裁決若無正文，回報而不自行補寫。
- 不自行調和數字：實測與預期不符時停下回報。

## 作業

### A 組（可立即並行，不等任何裁定）

W-0   python scripts/new_feature.py "Vehicle Setting" --adopt-existing
      （docs/handoff/ 之既有檔案不得被覆寫；--adopt-existing 即為此設計）

W-0b  依 R-VS12 將兩檔複製入 features/vehicle_setting/inputs/：
        Logical Identifiers and CAN Mapping v1.76.xlsx
        PDT25_E3A_R4_FDCAN8_vs_PDT25_E3A_R5_FDCAN8.xlsx
      來源路徑若不在預期位置，**回報而不四處搜尋**。
      複製後 inputs/ 應為 14 檔；不是 14 則停下回報。

W-1   對 inputs/ 全部檔案逐檔 shasum -a 256 → inputs/INPUTS.sha256
      格式須可直接 shasum -c 驗證。

W-2   四份 037 合併 leaf 全集 → data/leaves.tsv
      欄位：swe_id / family / src_ref / title / desc
      取 'Analysis Report' 表、表頭列 7、資料自列 8、A 欄非空者為 leaf

W-3   036 現況重測 → docs/reports/036_baseline.md
      資料列 10–246、逐列、逐欄填充率；逐列驗 I/H/N 是否等於 037 之
      desc/title/src（R-VS1 之依據是否成立）

W-4   錨鏈對照表 → data/sysra_to_polarion.tsv
      SYS-RA-CFTS044-N → SYS2 'Basic Report' 第 N 筆資料列（工作表列 N+1）
      → A 欄 NRL id → 'Source Requirement items' 7 位數

W-4b  outline map → data/outline_map.tsv
      自 CFTS044 原始 docx 之 word/styles.xml 解出 styleId 1-7 = heading 1-7，
      取 body heading，需求段落以 '[Artifact Type' 錨定，
      以位置法歸屬 → leaf → CFTS044 章節號

W-5   反向驗證 W-4/W-4b：須含「什麼都沒做」之對照向；
      並證明 offset -1 / +1 之命中為 0（R-G7-1）

W-6   覆蓋差：leaf 全集 − 036 現有 D 欄值

W-7   異常登記（登記，不裁定）→ ANOMALIES.md
      A-VS01（SYS-RA 指向 SYS2 之 Heading/Information 列，25 leaf）
      A-VS03（四份 037 封面完全相同，無法區分）
      A-VS04（CFTS044 內未填佔位 {CFTS044-xxxx}）
      A-VS05（Heated_Seat_Levels / Heated_Seats_Levels / Heated_Steats_Levels
              三種拼寫；第三種在 2,974 個 LID 中無對應，確為 typo）
      A-VS06（body heading 270 對相異 {7位數} 254，差額 16 未追因）
      A-VS07'（DBC 檔名 R4/R5 在 PDT27_E2A 組指網段、在 PDT25_E3A 組指
              版本週次，同一慣例兩種語意；FYI 類）
      A-VS08（PDO Graphics Release PDF 車型與主題皆與本 feature 無交集）
      A-VS09（26PI 版 Pop Up List 較 Comfort/User Profiles 基線新）
      A-VS10（CFTS044 指名之 TLM HMI Document 於客戶 HMI 目錄無同名檔）
      A-VS11（無 PDT27_E2A 組之跨版本比對表）

W-8   $變數$ 三來源對照 → data/spec_variables.tsv
      正則 \$[A-Za-z0-9_]+\$（區分大小寫），逐 token 附三欄來源：
        (a) CFTS044 內嵌值域，兩式並用：
            `$var$ = [值]` 與 `路徑.名稱 == "值"`
        (b) DBC 之 VAL_ 值表（兩份 DBC 皆掃）
        (c) LID 表之 Format 欄（Atlantis High 優先，空則記 Atlantis 欄
            並標記來源為哪一欄）
      **三者不一致者逐項列出並停下回報，不自行調和。**
      已知一致者三項（STATUS_CSWM / id 1169 / Fail_Not_Present-Fail_Present），
      其餘尚未系統性比對。

W-14  LID 對照表 → data/lid_map.tsv
      來源：Logical Identifiers and CAN Mapping v1.76.xlsx
      取 'CAN Mapping'（2,629 列）與 'Proxi & Configuration'（449 列），
      表頭列 3、資料自列 4、A 欄 Logical Identifier 非空者為 LID。
      欄位：lid / sheet / row / function / atlantis_high_signal /
            atlantis_high_can / atlantis_high_format /
            atlantis_signal / atlantis_can / atlantis_format / flags
      flags 須至少標記三種：
        SEE_PROXI_TABLE   —— Format 欄為 'See Proxi Table'（已知 6 個 LID）
        TRUNCATED_ENUM    —— 列舉以 '# = Not Used' 結尾而規格所用之值不在
                             其中（已知 VC_VEH_LINE 截斷於 '101 = WL'）
        ATL_HIGH_EMPTY    —— Atlantis High 欄空而 Atlantis 欄有值
      **另須掃 'Usage Comment'（第 31 欄）尋找其他措辭之轉指**
      （如 refer to PROXI / see config table），00G 未掃該欄。
      **另須將十張車型專屬分頁納入比對**（Atlantis Low Specific Signals、
      M240 Specific Signals、332BEV、M182BEV、250MCA、965、ALFAMCA、
      637MCA、356MCA、BSEGMENT，合計約 200 列）——00G 未納入，
      故其 ATL_HIGH_EMPTY 計數 10 為上界。

W-15  DBC 身分與訊號逐屬性比對 → data/can_signal_map.tsv
      (a) 對兩份 DBC 各記：檔名、SHA256、BA_ "VersionYear"、
          BA_ "VersionWeek"、BA_ "BusType"（無此屬性者明記「無」）
      (b) 對本 feature 所用之 message／signal，**逐屬性**比對 DBC 與
          LID 表：signal 名、message 名、CAN id、起始位元、長度、
          factor／offset、VAL_ 值表。
          通過條件寫成「與參照對象在所有可讀屬性上一致」，
          不寫成「已知的幾項正確」（canon §5a 第 14 條）。
      (c) 名稱相同而定義不同者，逐項列出 —— 00H 只比名稱，未比定義。

W-11  DATA_REQUESTS.md 依 00E §1 + 00G §5 填實（每項含路徑與 SHA）：
        5-A  Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359
             (Feb 24 2025).pdf —— 未入，待 Pei 授權
        5-B  失效彈窗 + 圖示左右駕鏡像 —— RD-1 提問
        7    PROXI 表（Heated_Seats / Heated_Seat_Levels /
             Heated_Steering_Wheel / DSP_SK_PRSNT 之值域）
        8    $VC_VEH_LINE$ 之完整車型碼對照（DT / WS / HDCC / M240
             皆不在 LID 表之列舉內）
      並記一句：「已查 features/comfort/inputs/ 三份與 26PI2.5/HMI 四份，
      本 feature 條文不引用者不取用」——查過而不用須留痕（G-D）

W-12  scripts/recon.py → RECON.md + DECISIONS.md + recon.json；
      feature.yaml 填 spec_mode = D

W-13  對 /Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/
      'R1LR SR26 ATL-H'/26PI2.5/HMI/ 之全部 PDF 與 XLSX（約 112 檔）
      跑全文掃描，關鍵詞：Fail_Present / STATFailSts /
      'Heated Steering Wheel Icon' / 'Left Side' / 'Right Side'
      目的：以餘數驗證 00D「失效彈窗不在該目錄」之結論（R-G10）
      **唯讀掃描，不複製任何檔案入 inputs/**
      PDF 須先驗文字層產出量；抽不到者標「未解析」不猜（§5a 第 12 條）

### B 組（做完必停）

W-9   Comfort 重疊逐條對照 → docs/reports/comfort_overlap.md
      來源：features/comfort/inputs/
      FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx
      逐條列出命中座椅加熱／通風／方向盤加熱之 Comfort leaf
      （00D 之上界為 43，子字串無詞界）與其對應之本 feature leaf。
      另附 CFTS044 內文以 {CFTS043} 引用 Comfort 規格之 3 處上下文。
      **產出後停止，不得繼續。** 等 R-VS7 裁定（三選項見 00A §3）。

### 附帶查驗

- 讀 00_intake_and_rulings.md 之 §1 第 6 點，以位元層確認其中是否有
  多位元組字元毀損（分析層讀回時顯示為 '沙??'）。
  若確有毀損，回報並提出修正字串，**不逕行改寫**。

## 預期數字（逐項重測，相符者亦須列出）

00 包 §5.2 有 24 項預期值，**全部量自沙箱副本**。另加下列各篇之實測值：

CFTS044 原始 docx（00C）
  PK zip、28 個 zip member、body heading 270、需求段落 2030
  leaf → 章節：245 解析 / 25 有 id 無章節 / 1 無 id
  245 leaf 落在 20 個相異章節
  檔名式正則命中全簿僅 1 個（RAR_LTM-R1L_SR21_1A_r8.xlsx，在 Revision Notes）
  TLM HMI Document 24 處、PDO graphics 2 處、DBC 13 處

DBC（00C／00H）
  R4_BHCAN  883 signals / 155 messages / VersionYear 25 / VersionWeek 50 / 無 BusType
  R5_FDCAN8 1755 signals / 323 messages / VersionYear 25 / VersionWeek 50 / BusType "CAN FD"
  僅存 BHCAN 之 message 119、僅存 FDCAN8 287、共有 36
  HSW_StatFailSts 僅於 R4_BHCAN（STATUS_CSWM, id 1169）
  TGW_DISP_STATSts 於 TELEMATIC_DISPLAY2(1500) 與 TELEMATIC_FD_4(1427)

LID 表（00G）
  相異 LID 2,974（CAN Mapping 2,629 列 + Proxi & Configuration 449 列）
  30 個 token：逐字命中 27 / 近似 2 / 無對應 1（Heated_Steats_Levels）
  Format = 'See Proxi Table' 之列 6（其中本 feature 用得到 4）
  VC_VEH_LINE 之 Format 全長 491 字元，結尾為 '101 = WL (65 Hex) # = Not Used'
  Atlantis High 空而 Atlantis 有值者 10（上界，未納車型專屬分頁）

Comfort HMI L&F（00D）
  pdftotext 64,978 字元；Fail 命中 0；Left Side / Right Side 各 0；TLM 0
Pop Up List 26PI（00D）
  Main 表 1,344 列；座椅／方向盤相關 6 列（PU0226/0297/0364/0573/0574/1557）
  座椅或方向盤 ∩ fail/malfunction/service 命中 7 列，逐列檢視後全部無關

## 上繳

寫入 features/vehicle_setting/docs/upstream/00_intake_and_rulings.md，須含：

1. 預期 vs 實測逐項對照（相符者亦列）
2. 不符項目逐項說明（不調和）
3. 結果三分法分類：改對了／核實無誤／正確地不動
4. 本輪實際使用之掃描條件揭露（欄位範圍、大小寫、詞界）
5. W-5 之反向驗證實測（含對照向）
6. W-8 之三來源不一致清單（若為空，須說明比對涵蓋了哪些 token）
7. 新開 anomaly 與 DATA_REQUESTS 條目，成對
8. 未預期之發現（本包未涵蓋而執行時撞到者）
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
10. 給 Pei 之 git 指令草稿（帶 pathspec，不執行）

並更新 features/vehicle_setting/docs/INDEX.md（分析層不寫此檔）。

## 升級條件（撞到即停，其餘不受影響之作業繼續）

1. 任一實測與預期不符
2. 錨鏈在任一 leaf 上不成立（offset 非 +1、指向列不存在、章節歸屬矛盾）
3. W-8 出現三來源不一致
4. W-9 完成（必停）
5. W-0b 後 inputs/ 不是 14 檔
6. 037 四檔間出現同一 SWE ID，或同一 SYS-RA 被兩 leaf 共用
7. 036 母本結構與 forms/…_SWQT_20260817_ext.xlsx 不一致
8. 撞到 §8.4.1 之編造壓力
9. 需要判斷而 canon／本包皆無條文

## 尚未裁定（本輪不得預設答案）

R-VS7  Comfort 43 leaf 之委派界線（三選項見 00A §3）
R-VS9  CAN 訊號書寫形式（條文草案見 00H §3）
R-VS10 Pop Up List 基線版本
R-VS11 LID 表之 Atlantis 欄能否代 Atlantis High（三選項見 00G §4）

R-VS8 已依實測改寫為「兩份 DBC 並用」（00H §2），待 Pei 追認；
在追認前依改寫版作業，**但不得據此更動任何交付內容**。

四項待裁皆不影響 A 組。遇到需要它們的判斷 → 登記待判，繼續其他作業。
```

---

## 2. 使用說明（不屬貼入內容）

- 貼入後執行層應先回報「已讀十一份、禁區已知、A 組開始」再動手
- **A 組完成即上繳一次**；W-9 之停點在 B 組，不與 A 組合併上繳
- MCP 或檔案讀取逾時：自動重試一次，連兩次失敗才回報
- W-14／W-15 為本版新增，其產物是 TC 生成階段寫訊號斷言之唯一依據；
  若這兩項未完成而進入生成，會回到「以 `$var$` 寫出匯流排上不存在之
  名字」之風險（00G §2 之 `$PowerMode$` 案例）
