# 02 — Power Management 素材重新定基（rebaseline）

下放包 | 分析層 → 執行層 | 往返 NN = 02

前置：docs/upstream/01_intake.md 已覆核，判定 ACCEPT。
停於步驟 2 為正確行為，發現之 defect 全部位於分析層之 01 下放包。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P9]  R-P3 撤回。其事實前提為假 —— 分析層所測之「三份純文字」
        係 Project 附件之轉換產物，非磁碟上之原始文件。
        改立 R-P3′：spec_mode = D（二進位文件抽取）。
        讀取方式依實測 magic bytes 決定：
          50 4B 03 04（OOXML .docx）→ zipfile 或 python-docx
          D0 CF 11 E0（OLE2 .doc）  → macOS 內建 textutil 轉換
        R-P3 對 python-docx / olefile / zipfile 之禁令一併解除。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q1）。
```

```
[R-P10] 三份純文字衍生物明示為不可得：無版本、無產生紀錄、
        無法重現，一律不得再作為任何量測之來源。
        CFTS 本文相關之一切數字，均須自原始檔重新產生。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q2）。
```

```
[R-P11] G8 / G9 四數（CFTS009 需求錨點 904 / 章節錨點 172；
        CFTS010 需求錨點 148 / 章節錨點 92）作廢。
        自原始檔重測後改寫 §D 期望值，不視為停止條件。
        理由：原值非 baseline，係自失效來源量得，
        改寫不構成「自行調參數遷就」。
        此例外僅適用於本次 rebaseline，不得類推。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q3）。
```

```
[R-P12] A-PW07 撤回（「三份 .docx 實為 Markdown 純文字」為假；
        副檔名與內容實為相符）。
        改登 A-PW08：01 下放包 §B 之「真實格式」欄與 bytes 欄
        與原始檔不符，源於以衍生物冒充原始檔。
        另記：CFTS010 之原始檔副檔名為 .doc，非 .docx；
        01 包中「三份 .docx」之表述在檔名層即為錯誤。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q4）。
```

```
[R-P13] 台帳通則（跨 feature 適用，canon 候選）：
        凡經任何轉換之素材，台帳須同時登記
        （a）原始檔之完整路徑、bytes、SHA256 全 64 碼
        （b）衍生物之 bytes、SHA256 全 64 碼
        （c）轉換工具與完整轉換指令
        三者缺一，該素材不得作為量測來源。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q5）。
```

```
[R-P14] 閃點表結構修正：
        （a）新增 G0「素材身分驗證」為前置閘 ——
             全部素材之原始檔 SHA256 相符方得進入 G1 以後。
             G0 不通過時，G1 以後一律不執行、不回報。
        （b）G11 移除。其期望值與 §E 同源，
             以 G11 驗 §E 為循環論證，不構成獨立驗證。
        （c）§E 之「已定版」與「本表實際只由單一來源支撐、
             不是交集」並存之張力，維持登記，不由實測覆蓋。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q6）。
```

（以上六條裁決條文，抄入 RULINGS.md 時須逐字保留，
 每條以獨立區塊呈現，不得夾於敘述中。）

## B. 素材台帳 —— 由執行層實測填入

分析層不轉抄任何雜湊值。原因：分析層之 MCP 讀取路徑經證實會
靜默損壞多位元組字元（01 上繳包已獨立驗證磁碟端乾淨），
故不得作為雜湊等精確值之來源。

執行層依 R-P13 之三欄格式，對下列目錄之原始檔實測並填入：

  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/

七份素材，每份登記：
  完整路徑 / bytes / SHA256 全 64 碼 / magic bytes / 真實格式 / 角色

角色欄依 01 包 §B：
  FW036-A01 …PowerManagement… .xlsx        → 交付標的（BLANK）
  Power_Management_FMWIFSM037A03… .xlsx    → 需求母體（115 leaf）
  SYS2_CFTS_009_… .xlsx                    → 上游需求（337 條）
  SYS2_CFTS_010_… .xlsx                    → 上游需求（73 條）
  …CFTS_009_Wake-up and Power-up… .docx    → 規格本文
  …CFTS_010_Power Down… .doc               → 規格本文
  SYS3_CFTS_009_…SYSAD… .docx              → 架構文件（不具 TC 權威）

01 包 §B 之舊表整體作廢，不保留、不並列。

## C. 抽取規格

三段錨點鏈維持不變：Sys-RA-* → Polarion item id → CFTS 章節號

正則維持 01 包 §C 之四條，但**適用對象改為自原始檔抽出之文字層**：
  1. 章節錨點：^\s*(\d+(?:\.\d+)*)\s+(.{0,90}?)\s*\{(\d+)\}\s*$（MULTILINE）
     同一 id 多次出現取最後一次
  2. 需求錨點：\*\*(\d{6,8}):\s*\[Artifact Type:
     每個需求錨點歸屬於其位置之前最近的章節錨點
  3. SYS2 匯出之「SYS2 來源需求項目ID Source Requirement items」欄
     即為上述 id，單格可含多個，需 \d{6,8} 全抓
  4. 037「Source Requirement ID」欄 token：
     Sys-RA-PM-\d{4}（CFTS009 域）與 Sys-RA-PD[_-]\d+（CFTS010 域）
     區分大小寫

重要：正則第 1、2 條係在失效衍生物上設計。
自原始檔抽出之文字層，其換行、粗體標記、章節編號呈現方式
可能與衍生物不同，正則可能完全不匹配。
若匹配數為 0 或顯著偏離，**不得自行調整正則**，
上繳實際文字層樣本（各取前 3000 字元）由分析層重新設計。

xlsx 讀取座標維持 01 包 §C（四份 xlsx 雜湊已驗明相符）：
  037「SWE1 Requirements」：表頭 r7，資料 r8–r145
  SYS2 兩份「Basic Report」：表頭 r1；CFTS009 r2–r338、CFTS010 r2–r74
  FW036「Test Case Specification&Result」：表頭 r9，資料 r10–r221
此三組座標於 01 包中未經實測（上繳包 §6.2 第 5 項），本包須實測。

## D. 閃點

G0 為前置閘，不通過則其後一律不執行、不回報。

| # | 項目 | 期望值 |
|---|---|---|
| G0 | 素材身分：七份原始檔 SHA256 全數登記且可重現 | 7 / 7 |
| G1 | 037 leaf 數（SWE-Requirement ID 非空） | 115，SWE-PM-001–115 連續無斷點 |
| G2 | 037 Categorization 值域 | 單一值 Functional Requirement ×115 |
| G3 | leaf → CFTS 章節解析成功數 | 114 / 115，唯一失敗者為 SWE-PM-089 |
| G4 | leaf 需 CFTS009 / CFTS010 / 皆無 | 111 / 3 / 1，三組互斥 |
| G5 | 需 CFTS010 之 leaf | 恰為 SWE-PM-071 / 072 / 073 |
| G5b | 該三 leaf 之解析章節 | 落於 CFTS010 §1.7.1 與 §1.7.2 |
| G6 | SYS2 CFTS009 條目全 id 可解析者 | 336 / 337（失敗者 Sys-RA-PM-0334） |
| G7 | SYS2 CFTS010 條目全 id 可解析者 | 73 / 73 |
| G8 | CFTS009 本文需求錨點 / 章節錨點 unique | 【重測後填入，R-P11】 |
| G9 | CFTS010 本文需求錨點 / 章節錨點 unique | 【重測後填入，R-P11】 |
| G10 | FW036 workbook_state | BLANK（c2–c35 × r10–r221 非空儲存格 = 0） |
| G12 | §C 三組 xlsx 讀取座標 | 實測與 §C 所載一致 |

G11 已依 R-P14(b) 移除，編號不遞補。
G5b 為新增：CFTS010 域是全案唯一跨文件分支，風險最高而 01 包驗得最淺
（上繳包 §6.2 第 4 項）。

## E. framework

維持 01 包 §E 之五個 Test Set（64 / 24 / 16 / 7 / 3，合計 114），
但其 leaf 分布係自失效衍生物量得，**須於 G3 通過後重新計算並比對**。
若重算結果與 64/24/16/7/3 不同，停並上繳，不得逕行改寫 §E ——
§E 已由 R-P5 / R-P6 裁定，變更需 Pei 重裁。

依 R-P14(c)，§E「已定版」與「只由單一來源支撐、不是交集」
之張力維持登記，不由實測覆蓋。

## F. Anomaly 異動

  A-PW07 → 撤回（R-P12），標註撤回理由，不刪列、不重編號
  A-PW08 → 新增（R-P12）
  A-PW01～A-PW06 → 不動

## G. DATA_REQUESTS

  DR-PW1（SWE-PM-089 來源）→ live，High
  DR-PW2、DR-PW4 → 維持撤回
  DR-PW3（Sys-RA-PM-0334 之 4942087 歸屬）→ live，Medium
  無新增

## H. 作業指示

  1. 依 §B 實測七份原始檔並填入台帳（R-P13 三欄格式）
  2. G0 前置閘：七份全數登記且可重現，方得繼續
  3. 素材入 features/power/inputs/（不入版控）
  4. 依 R-P3′ 自原始檔抽出文字層；先驗 §C 正則是否匹配，
     匹配數為 0 或顯著偏離則停並上繳文字層樣本
  5. 依 §C 重跑抽取，產出 leaf → (CFTS, 章節號, 章節標題) 對照表
  6. 以 §D 自驗（G8/G9 為填空，其餘為比對）
  7. 依 §E 重算 Test Set leaf 分布並與 64/24/16/7/3 比對
  8. §A 六條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md；
     §G 入 DATA_REQUESTS.md
  9. 填 DECISIONS.md 之 [AUTO] 項
 10. 上繳 features/power/docs/upstream/02_rebaseline.md，更新 docs/INDEX.md

## I. 禁區

  不得寫回 FW036 workbook
  不得執行任何 git 操作（全數屬 Pei）
  不得以 openpyxl save 寫任何 xlsx（R16 凍結）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用三份純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則（見 §C 末）
  不得逕行改寫 §E（見 §E 末）
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P9  R-P3 撤回，改立 R-P3′ spec_mode = D
  R-P10 純文字衍生物不可得，一切數字自原始檔重生
  R-P11 G8/G9 作廢，重測後改寫 §D，不視為停止條件
  R-P12 A-PW07 撤回，改登 A-PW08
  R-P13 台帳雙雜湊通則（canon 候選）
  R-P14 閃點表結構修正：加 G0 前置閘、移除 G11、§E 張力維持登記

  逐條確認：六條皆以獨立區塊呈現於 §A，未夾於敘述中。
