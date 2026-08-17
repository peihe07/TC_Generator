# 01 — Power Management Phase 0 Intake

下放包 | 分析層 → 執行層 | 往返 NN = 01

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P1] SWE-PM-089 之來源對應先留空。
       不臆測、不套用鄰近 leaf 之來源、不以 SWE1-PM-ANT-008 反查填補。
       該 leaf 仍計入 115 母體，列為 RD-1 待決。
       裁決者 Pei，逐字依據：「那題記得先留空 其他可以繼續」。
```

```
[R-P2] 命名。feature 目錄 = features/power；
       workbook Test Group = "Power Management"；
       tc_id 方案 = NR1L-PowerManagement-{NNN}。
       裁決者 Pei，逐字依據：「是繼續」（回應 #5 提案）。
```

```
[R-P3] spec_mode = B（純文字層 + 章節 regex）。
       三份 .docx 經 magic bytes 實測皆非 OOXML 亦非 OLE，
       為 Markdown 純文字轉檔。禁止以 python-docx / olefile /
       zipfile 讀取；一律以 UTF-8 文字讀入。
```

```
[R-P4] Power Management 之規格來源為兩份 CFTS：
       CFTS009 Wake-up and Power-up、CFTS010 Power Down。
       任何宣稱「規格來源」之陳述必須同時涵蓋兩份，
       單引一份即為不完整。
```

以下四條為第二輪裁決，於本包上繳前就地增補。

```
[R-P5] Layer 2 之 `Power State` 與 `Power State Reporting` 合併，
       為單一 Test Set `Power State`，64 leaf。
       Layer 3 隨之合併，含 CFTS009 §1.6.2.1.15
       （`TLM_Status.Info` / `$Telematic_Power$` 訊號上報）。
       裁決者 Pei，逐字依據：「E-1 合併」。
```

```
[R-P6] Layer 2 之 `Power Down`（3 leaf）**保留獨立 Test Set**，
       不因低於 §4.1.3 健康門檻而合併。
       裁決者 Pei，逐字依據：「E-2 保留獨立 Test Set」。
```

```
[R-P7] 範圍界定：037 之 115 leaf 為本 feature 唯一驗證母體。
       SYS2 反向缺口（未被 037 引用之 SW/System 需求）
       與 SYS2 匯出之收錄規則（`Sys-RA-PM-0197`–`0206` 斷點、
       CFTS009 本文未被引用之 547 條）**不追、不問、不列 RD-1**。
       DR-PW2 撤回。
       裁決者 Pei，逐字依據：「#1/#3 不需」。
```

```
[R-P8] Priority 之判定來源：依 **TC 實際所寫之測項內容**
       套 §10.2 之 rubric 判定 P0–P3。
       037 `Priority` 欄之 `High` / `Medium`（91 / 24）
       **不具映射權威**，不得以之推導 priority。
       DR-PW4 撤回。
       裁決者 Pei，逐字依據：「#4 依照所寫測項去判定」。
```

## B. 素材台帳

SHA256 為分析層沙箱副本實測值（前 16 碼）。**執行層須於素材落入
`features/power/inputs/` 後重測全 64 碼**，不一致即停。

| SHA256(16) | bytes | 真實格式 | 檔 |
|---|---|---|---|
| `ce93174794d0d43c` | 78607 | ZIP/OOXML | FW036-A01 …PowerManagement_20260816.xlsx |
| `2284abf5e6c17e4d` | 85210 | ZIP/OOXML | Power_Management_FMWIFSM037A03_STLA_Report_SWRA.xlsx |
| `6af7bfd314a28b39` | 227822 | ZIP/OOXML | SYS2_CFTS_009_…_All_Accepted_04_13_2026.xlsx |
| `f318b14623fcbf97` | 64422 | ZIP/OOXML | SYS2_CFTS_010_…_All_Accepted_04_13_2026.xlsx |
| `691e5ca17bcfa112` | 412654 | 純文字 | …CFTS_009_Wake-up_and_Power-up_SR26_20250909-1658.docx |
| `d13919341c810b15` | 81064 | 純文字 | …CFTS_010_Power_Down__SR26_20250909-1658.docx |
| `019b3d7a51211cd3` | 51264 | 純文字 | SYS3_CFTS_009_…_SYSAD_v1_1_0.docx |

SYS3 SYSAD 為 SWE.2 架構文件，**對 TC 內容不具權威**（§8.1）。
本階段不讀，僅入台帳。

## C. 抽取規格（執行層據此重跑，不得沿用本包數字）

三段錨點鏈：`Sys-RA-* → Polarion item id → CFTS 章節號`

1. CFTS 本文之**章節錨點**：行首正則
   `^\s*(\d+(?:\.\d+)*)\s+(.{0,90}?)\s*\{(\d+)\}\s*$`（MULTILINE）
   同一 id 多次出現時取**最後一次**（前面的是目錄頁）。
2. CFTS 本文之**需求錨點**：`\*\*(\d{6,8}):\s*\[Artifact Type:`
   每個需求錨點歸屬於其位置之前最近的章節錨點。
3. SYS2 匯出之 `SYS2 來源需求項目ID Source Requirement items` 欄
   即為上述 id；單格可含多個，以換行分隔，需 `\d{6,8}` 全抓。
4. 037 `SWE1 Requirements` 之 `Source Requirement ID` 欄 token：
   `Sys-RA-PM-\d{4}`（CFTS009 域）與 `Sys-RA-PD[_-]\d+`（CFTS010 域）。
   **區分大小寫**。

### 各檔讀取座標

- 037 `SWE1 Requirements`：表頭 r7，資料 r8–r145（138 實體列，
  其中 23 列全空）
- SYS2 兩份 `Basic Report`：表頭 r1；CFTS009 資料 r2–r338，
  CFTS010 資料 r2–r74
- FW036 `Test Case Specification&Result`：表頭 r9，資料 r10–r221

## D. 閃點（實測十一項不符即停，不得自行調參數遷就）

| # | 項目 | 期望值 |
|---|---|---|
| G1 | 037 leaf 數（`SWE-Requirement ID` 非空） | 115，`SWE-PM-001`–`115` 連續無斷點 |
| G2 | 037 `Categorization` 值域 | 單一值 `Functional Requirement` ×115 |
| G3 | leaf → CFTS 章節解析成功數 | **114 / 115**，唯一失敗者為 `SWE-PM-089` |
| G4 | leaf 需 CFTS009 / CFTS010 / 皆無 | 111 / 3 / 1，**三組互斥** |
| G5 | 需 CFTS010 之 leaf | 恰為 `SWE-PM-071` `072` `073` |
| G6 | SYS2 CFTS009 條目全 id 可解析者 | 336 / 337（失敗者 `Sys-RA-PM-0334`） |
| G7 | SYS2 CFTS010 條目全 id 可解析者 | 73 / 73 |
| G8 | CFTS009 本文需求錨點 unique | 904；章節錨點 172 |
| G9 | CFTS010 本文需求錨點 unique | 148；章節錨點 92 |
| G10 | FW036 workbook_state | `BLANK`（c2–c35 × r10–r221 非空儲存格 = 0）|
| G11 | Layer 2 Test Set 數與 leaf 分布 | 5 個；64 / 24 / 16 / 7 / 3，合計 114 |

G3/G4/G5 三項共同構成 R-P1 與 R-P4 之可驗證形式。
若 G3 出現 115/115，代表 `SWE-PM-089` 被錯誤填補 —— 違反 R-P1，停。

## E. framework Layer 2 / Layer 3（**已定版**）

Layer 1 Test Group = `Power Management`（R-P2）。

Layer 2 與其 Layer 3 對應（每 leaf 只計主章節）：

| Test Set | leaf | Layer 3（CFTS 章節） |
|---|---|---|
| Power State | 64 | 009 §1.6.2.1.1–.15、§1.7.1、§1.8.1、§1.9.3–.5、§1.9.12 |
| Startup Display | 24 | 009 §1.3.5、§1.6.2.1.16、§1.9.8、§1.9.9、§1.9.10 |
| Branding and Theme | 16 | 009 §1.9.15–.17 |
| Timeout Settings | 7 | 009 §1.6.3、§1.6.4、§1.6.7 |
| Power Down | 3 | **010** §1.7.1、§1.7.2 |

合計 114 + `SWE-PM-089` 留空（R-P1）= 115。
本表已經 R-P5（合併）與 R-P6（Power Down 保留獨立）裁定，
**已定版，無待裁項**。

### 本分組之已知弱點（不得省略之登記）

§4.1.2 要求取「規格目錄」與「RD 分析報告分組」之交集。
本案中後者**無分組價值**：037 `Requirement Title` 於 115 leaf 中
出現 20+ 種，多數僅出現 1 次（`Timeout` 7、`Phone Call` 5 為僅有例外）。
因此上表實際只由 CFTS 章節單一來源支撐，**不是交集**。

## F. Anomaly 登記（執行層寫入 ANOMALIES.md）

| ID | 內容 | 證據 |
|---|---|---|
| A-PW01 | `SWE-PM-089` 之 `Source Requirement ID` = `SWE1-PM-ANT-008`，為 037 自身另一套命名空間，非上游來源 | 全表 18 欄 × r8–r145 掃描，該 token 不存於任一 SYS2 匯出 |
| A-PW02 | `Sys-RA-PM-0334` 之 source id `4942087` 於兩份 CFTS 本文皆不存在；`4942xxx` 為 CFTS010 號段但低於其首個 id `4942192` | G6 失敗項 |
| A-PW03 | 037 `Excluded NRLs (HW-only)` 26 筆全落 NRL-928xx–930xx（CFTS009 域），**不含** `NRL-99476`（`Sys-RA-PD_013`，HW） | 排除台帳涵蓋範圍不等於其名稱所宣稱 |
| A-PW04 | 037 `SYS2 Traceability` 33 列不含任何 `NRL-994xx` 或 `Sys-RA-PD` | CFTS010 全域未進追溯分頁 |
| A-PW05 | 037 內部 id 命名空間不一致：`SWE1 Requirements` 用 `SWE-PM-001..115`，`SYS2 Traceability` 用 `SWE1-PM-TLM-001..033` / `-ANT-` | 兩套互不對應 |
| A-PW06 | 037 `Sub Categorization` 詞彙漂移：`HMI` 36 / `Service\nHMI` 35 / `Service` 27 / `HMI Service` 16 / `HMI/Service` 1 | 三種寫法指涉同一組合，不可作分批判準 |
| A-PW07 | 三份 `.docx` 實為 Markdown 純文字，副檔名與內容不符 | magic bytes 實測（R-P3） |

已有政策涵蓋、**不得重新立規**者（§5a 第 17 條）：

- FW036 c21 車型欄標頭 `HDCC27 Atl-Hi` → 沿用 **A-PV15**（世代落差、
  入 RD-1、不自行對應）與 **R30-3 / R30-4**（Functional Safety 欄 `NA`、
  車型欄留白）
- `Cover_old` / `ChangeHistory_old` 殘留分頁 → 沿用 **A-PV12 / R23-8**
  （原樣保留，不進 lint、不進 trace、不寫回）
- `下拉選單` A10/A11 為空 → 沿用 **A-PV10 / R23-6**
  （design_method 權威為 `下拉選單!A1:A9` 九詞條）；
  本 feature 實測與該紀錄一致，同一範本同一缺陷

## G. DATA_REQUESTS（執行層寫入 DATA_REQUESTS.md）

| DR | Urgency | 內容 | 阻斷何物 |
|---|---|---|---|
| DR-PW1 | High | `SWE-PM-089` 之真實上游來源為何？（`SWE1-PM-ANT-008` 非 SYS2 id） | 該 leaf 之 TC 及其 `specification_reference` |
| DR-PW2 | **撤回** | SYS2 匯出之**收錄規則**為何？—— 包含（a）CFTS009 `Sys-RA-PM-0197`–`0206` 連續十條缺失；（b）CFTS009 本文 904 條需求中未被引用之 547 條內，有 **140 個需求錨點**標 `EE Architecture: Atlantis High/Mid`（`Atlantis High, Atlantis Mid` 73 + `Atlantis Mid, Atlantis High` 67，二者為同一集合之不同排序寫法），似不應被濾掉。**（R-P7 撤回：範圍 = 037 之 115 leaf）** | 已解除 |
| DR-PW3 | Medium | `Sys-RA-PM-0334` 引用之 `4942087` 屬何文件？ | A-PW02 |
| DR-PW4 | **撤回** | 037 `Priority` 之 `High`/`Medium` 如何映射至 FW036 `P0`–`P3`？**（R-P8 撤回：priority 依 TC 測項判定）** | 已解除 |

**本表現存 live 項僅 DR-PW1 與 DR-PW3，兩者皆不阻斷 framework 定版。**
撤回列不刪、不重編號，保留作為裁決跡證。

## H. 作業指示

1. `python scripts/new_feature.py Power --adopt-existing`
   —— `features/power/` 及其 `docs/handoff/` 已由分析層建立，
   靠 `--adopt-existing` 吸收，**不得覆寫本檔**。
2. 素材入 `features/power/inputs/`（不入版控），
   重測全 64 碼 SHA256 並與 §B 對照。
3. 依 §C 重跑抽取，產出 `leaf → (CFTS, 章節號, 章節標題)` 對照表。
4. 以 §D 十一項閃點自驗；任一不符即停並上繳。
5. 將 §A 八條裁決逐字抄入 `RULINGS.md`；§F 入 `ANOMALIES.md`；
   §G 入 `DATA_REQUESTS.md`（含兩條撤回註記）。
6. 填 `DECISIONS.md` 之 `[AUTO]` 項；`[PROPOSED]` 項留空待裁。
7. 上繳 `features/power/docs/upstream/01_intake.md`，並更新 `INDEX.md`。

## I. 禁區

- **不得寫回 FW036 workbook**。本包為 Phase 0，無任何寫回動作。
- **不得執行 git 操作**（全數屬 Pei）。
- **不得以 openpyxl save 寫任何 xlsx**（R16 凍結）。
- **不得補齊 `SWE-PM-089`**（R-P1）。
- **不得以 python-docx / olefile / zipfile 讀三份 `.docx`**（R-P3）。
- 素材補入超出 `features/power/inputs/` 需 Pei 裁定。

## J. 本包產生之新條文清單（自檢）

| 條文 | 已以區塊形式出現於 §A |
|---|---|
| R-P1 SWE-PM-089 留空 | ✓ |
| R-P2 命名（features/power / Power Management / NR1L-PowerManagement-{NNN}） | ✓ |
| R-P3 spec_mode = B，禁 OOXML/OLE 讀取器 | ✓ |
| R-P4 規格來源為 CFTS009 + CFTS010 兩份 | ✓ |
| R-P5 Power State 與 Power State Reporting 合併 | ✓ |
| R-P6 Power Down 保留獨立 Test Set | ✓ |
| R-P7 範圍 = 037 之 115 leaf，DR-PW2 撤回 | ✓ |
| R-P8 priority 依 TC 測項判定，DR-PW4 撤回 | ✓ |

逐條確認：**八條**皆以可直接貼入之 fenced block 形式出現於 §A，
未夾於敘述中。R-P1–R-P4 為第一輪，R-P5–R-P8 為第二輪就地增補。

## K. 本包是否仍有該驗而未驗者（分析層自判）

**有，三項。**

1. **SYS3 SYSAD 完全未讀**。只做了淺層探測（50,296 字元、
   40 個章節號、零個 `CFTS009-nnnn` token）。它不具 TC 權威，
   但 §4.x 之元件分解可能影響 Layer 2 邊界。**未驗。**
2. **§G DR-PW2(b) 之 140 個 `Atlantis High/Mid` 未引用錨點
   未做 ECU × EE 聯合過濾**。
   我只數了單軸標籤分布，未逐條判定它們是否真的應在範圍內。
   此為 DR-PW2(b) 之證據強度上限 —— 現階段只能說「可疑」，
   不能說「遺漏」。（R-P7 後已無追查必要，保留作為當時判斷之紀錄）
3. **§E 之 Layer 2 聚類規則為我手寫之章節前綴對應**，
   未以獨立方法交叉驗證。執行層重跑時若得出不同聚類，
   **以執行層之實測為準**，並上繳差異。
