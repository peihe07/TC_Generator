# INDEX — FW036 Power Moding

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

feature 之交付夾為 `ASW-R2/Disclaimer screen/`（FROP 標籤），
身分為 `Power Moding`（規格標題模組名）—— R-PMH2，Comfort R-C6 同型。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-22 | 開案：骨架、裁決落檔、Phase 0 intake 實測 | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-PMH1–R-PMH6（分析層，逐字抄錄 6/6 相符） | A-PMH01–A-PMH05 | **步驟 1–8 全數執行；停止條件 2、4 觸發，已停於待裁** |

## 01 輪要點

**相符者**
- 037 `Functional Requirement` = **48**、`Heading` = **8**、
  R-G10 餘數 = **0**（56 − 48 − 8）
- 037 `HMI Source ID` 文件 stem 相異 = **1**
- 036 非空欄集合 `{B,D,G,H,I,L,M,N}` 各 48、`F`/`AB` 各 0、
  `L` 具編號步驟 0、5 個合併範圍、`D5` 空白、10 分頁 —— 逐項與下放包相符
- 素材四份 `shasum -c` 全 OK，搬入前後與來源複測三次雜湊一致

**不符者（一項）**
- 037 `FROP` 相異值：下放包 **13**／實測 **12**。成因為對全 56 列取
  `set()` 未排除 8 個 Heading 列之空值 → **A-PMH01**。
  下放包自身之分布明細即為 12 項且逐項相符。R-PMH6 之引用數待更正。

**新增實測（下放包未涵蓋者）**
- **036 版面為 A–AI 共 35 欄**，非 rev C 之 34 欄；`priority` 起每欄較
  rev C 右移一格（priority **Q**／design_method **S**／
  functional_safety **T**／author **AB**／remarks **AI**）。
  **AH 在本版面是 Defect ID** —— 誤用 rev C 之 AH 會寫錯欄。欄位對應 **16/16**。
- **R-PMH5 之機械搬運宣稱經 336 格逐字驗證，48×7 全部相符。**
- 037 之 48 id 與 036 D 欄 48 id **依序逐一相符**（1:1 實證）。
- **`workbook_state`：filled 48／qualifying done 0** → canon §2 四類皆不合，
  依停止條件 2 未自行歸類，記 `PENDING_RULING`。
- **spec_mode 提案 `A+B`**：PDF 文字層產出率 **11/11 = 100%** 但
  **可錨定編號章節 0**（Visio 流程圖冊，無目次）；SYS1 匯出 **52 outline**，
  037 引用之 **29 章節命中 29/29**。依通則 3 指定
  判讀基準 = PDF（內文面）、追溯用 = SYS1 匯出（結構面）。
- **canon §3 之 Home 型漏句於本 feature 未觀察到**：43 則可比對描述中
  **39 則逐字命中 PDF**；4 則之缺口為重排（7.1）、拼字（8）、
  `-layout` 條列再流（9.1／11.1）→ A-PMH03。
- **SYS1 匯出 6 則 outline 為圖片佔位**（2.1/3.1/4.1/5.1/6.1/12.4），
  內容僅存於 PDF p3–p7 流程圖；該六者不在 037 之 29 章節內 → A-PMH04。

**canon 層之衝突（停止條件 4）**
- **A-PMH05** —— scaffold 之 `.gitignore` 以 `inputs/` 整夾排除，
  使通則 9 所要求「須入版控之雜湊檔」被忽略。非本 feature 專屬。
  附帶：`sandbox/` 亦不在 `.gitignore` 內。**本包未動 `.gitignore`。**

**待裁**：Q1（`workbook_state` 新狀態名）／Q2（036 母本身分）／
Q3（`D5` 範圍欄）／A-PMH01（R-PMH6 引用數）／A-PMH05（雜湊檔落點）。

**下一包之首要建議**：讀 036 之 `Test Case Framework` 分頁 —— 其名稱直指
Phase 3 產物，可能已含客戶側之 Test Group／Test Set 期望，會改變 R-PMH6
之輸入集合。詳見上繳 §9（該驗而未驗者六項）。
