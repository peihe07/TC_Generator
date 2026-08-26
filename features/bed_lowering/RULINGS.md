# RULINGS — Bed Lowering Mode (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄，不改寫、不摘要。
本檔為 Bed Lowering Mode 之裁決權威。裁決前綴 `R-BLM`、異常前綴 `A-BLM`、
資料請求前綴 `DR-BLM`，不與任何既有 feature 共用序號。

來源：`docs/handoff/01_intake_recon.md` §二（下放包 01，Pei 2026-08-26 裁定
Q1 甲／Q2 Heading 納入但註明不寫測項／Q3 裁），及同日 chat 之三次追裁。

**取號警語（本檔自身之撞號實例）**：本檔 2026-08-26 14:34 建立時，
分析層未依 R-G23′ live 取號，自記憶推定「R-BLM3 之後接 4」，
而 `R-BLM4`（PDF 來源本）已於同日 13:15 由執行層落於
`01_intake_recon.md` §二。**號碼簿在那份檔，不在本檔** ——
而分析層因為那份檔是自己 11:21 寫的，就以為自己知道最大號。
同日 15:0x 修正：原 `R-BLM4`（spec_reference）→ `R-BLM5`，
原 `R-BLM5`（SYS 缺號）→ `R-BLM6`，PDF 來源本那條逐字補入為 `R-BLM4`。
**先落檔者優先。** 日後取號一律於落檔當下 grep 本檔與
`docs/handoff/` 全目錄，不得自記憶推定。

---

```
R-BLM1（feature 身分與結構歸屬）

（Pei 2026-08-26 裁定 Q1 甲。）

Bed Lowering Mode 立為獨立 feature。slug = `bed_lowering`，
test_group = `Bed Lowering Mode`。自有工作簿與
`features/bed_lowering/docs/{handoff,upstream}/` 目錄。

不併入 `features/vehicle_setting/`，不附掛 VF230 工作簿 —— 該本 438 TC
已寫回、處於 Pei 手動收尾階段，追加有污染風險。

037 之 `FROP = Vehicle Settings` 為上游程式歸類標籤，不構成目錄歸屬依據，
不進入 test_group、不進入任何 TC 欄位。
```

---

```
R-BLM2（驗證範圍與 Heading 列之處置）

（Pei 2026-08-26 裁定 Q2：「Heading 列納入但註明不寫測項」。）

覆蓋台帳收錄 037 `Analysis Report` 全部 218 列。

42 個 Heading 列（`SWE1-HMI-BLM-001` ~ `-042` 母號）納入台帳並標註
`No TC — Heading; refer to child IDs`，不作為 TC 生成對象。其
Verification Criteria 原文即為 "Please refer to the following IDs:"。

176 個 leaf（Categorization = Functional Requirement）為 TC 生成對象。

人因／可視性群（BLM-013 ~ BLM-017）之處置：可功能化改寫為 HMI 可觀察
行為者生成 TC；純設計驗證性質者不生成，列入 coverage gap disclosure
table 隨工作簿交付。
```

---

```
R-BLM3（036 母本與 workbook_state）

（Pei 2026-08-26 裁定 Q3 裁，從屬 Q1 甲案自動成立。）

036 母本套用 R-G1 全域條文：
`forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
Specification & Result_SWQT_20260817_ext.xlsx`

`workbook_state = BLANK`。不沿用任何既有 036 本，無既有 done region。

母本之 R 欄 design_method 下拉為 x14 擴充。任何以 openpyxl 存回母本之
操作都會摧毀該下拉（R-G1 註）。寫回一律採 XML 外科式修改。
```

---

```
R-BLM4（PDF 來源本）

（Pei 授權 analysis 層裁定，2026-08-26；逐字照錄自
`docs/handoff/01_intake_recon.md` §二。）

裁：以 `features/bed_lowering/inputs/` 那份為準。

實測依據：二者 metadata 同源（Title、Author `T6133SW`、Producer
`Microsoft: Print To PDF`、CreationDate 2021-06-25 18:46:52 全等），
確為同一次輸出之同一份文件。差異來自後手處理——`spec-index/sources/`
那份 ModDate 為 2025-11-04，被線性化（`Optimized: yes`）、加了
metadata stream 與 AcroForm，且 p.3「Change Log」頁被作者 `SD63673`
於 2025-11-04 12:16 加上兩條紅色 Line 標註（寬 3.0，斜跨整頁，
實為一個打叉）。`inputs/` 那份無任何 annotation，
是未經觸碰的原始輸出。

裁定理由：來源本應取未經後手標註者（標註是他人閱讀痕跡，
非交付內容的一部分，且該打叉之意圖無從查證，不得當作規格語意）。
檔案大小之差（665,190 vs 664,990 bytes）純為重存所致，非版次差異
—— 本 feature **不存在 PDF 版次問題**，勿誤記為版本衝突。
```

---

```
R-BLM5（specification_reference 之錨定 —— 採乙案）

（Pei 2026-08-26 裁定「乙」，回應 A-BLM4 之三選一。）

`specification_reference`（工作簿 N 欄）逐字取 037 `HMI Source ID` 欄
原值，不構造、不補章節號：

    SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)

單行。全簿 176 列該欄同值。

本條為 IN §10.7(b) 之 [OVERRIDE]，其啟動載於
`docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` §1。

override 之理由為**上游正式欄無章節錨**（A-BLM4 之實測：037
`HMI Source ID` 218/218 列相異值數為 1，無章節號後綴），
**非分析層省略**。追溯粒度因而為文件級，交付時於 coverage 說明揭露。

本條與 Vehicle Category 之 R-VC4 為同一條文（「逐字取 037 HMI Source ID
欄原值，不構造」），但**兩者之結果不同** —— Vehicle Category 之 037 該欄
帶章節號，展開得 66 section；本 feature 之 037 該欄不帶，展開得單一常數。
**條文相同而結果相異，其差異來自上游 037 本身，不是條文之歧義。**
```

---

```
R-BLM6（SYS-HMI-RA-BLM 之 24 個缺號 —— 不寫）

（Pei 2026-08-26 裁定：「是 SYS 側本就含非 HMI 項（底盤、電氣）
沒列在 037 就不寫」。）

`SYS-HMI-RA-BLM` 之 001~066 中，037 僅引用 42 個。缺號 24 個：
3, 5, 6, 8, 12, 18, 19, 21, 23, 26, 28, 30, 32, 33, 35, 38, 39, 41, 42,
47, 53, 56, 61, 62。

該 24 號判定為 SYS 側之非 HMI 項（底盤、電氣），未列於 037 即不在
SWE.6 範圍。不生成 TC、不列 coverage gap、不登 DR 向上游查詢。

**本裁定之依據為 Pei 之領域判斷，非自手邊文件驗得。**
分析層先前之實測結論為「二者（SYS 側非 HMI 項／037 未分解之項）在手邊
文件上區別不出來」，該結論不因本裁定而改變 —— 改變的是**由誰承擔該判斷**。
留此註記使日後稽核讀得出本條之來源。
```
