# 00 下放包 — Vehicle Setting 進場、裁決落檔、Phase 0/1 作業

分析層寫入（Claude Desktop）。執行層讀本檔即可作業，**不需任何聊天脈絡**。
canon：`docs/fw036/FEATURE_ONBOARDING.md`；TC 內容規則：
`docs/runtime/ASPICE_SWE6_AI_Instruction.md`。

---

## 1. 禁區

1. **全部 git 操作屬 Pei**（R-G5）。含 `add` / `commit` / `checkout` /
   `restore` / `stash` / `clean` / `tag`。唯讀 git（`status`、`log`、`diff`）
   得執行，但須於上繳包**與改狀態之 git 分列**（R-G6）。
2. **不得寫入 036 母本或任何交付件**。本包無 write-back 作業。
3. **不得補入素材**。`inputs/` 之內容以 Pei 放入者為準；發現需要而未到之
   檔案，寫進 `DATA_REQUESTS.md` 並回報，不自行下載或搬移（§8.5-3）。
4. **不得代擬裁決條文**（§8.5-1）。本包未涵蓋之判斷一律回報。
5. **不得自行調和數字**（§8.5-2）。實測與本包預期不符時停下回報。
6. **不得以沙箱／副本之數字代替 repo 實測**（R-U16、G-L）。

---

## 2. 背景

- Feature：**Vehicle Setting**（Pei 2026-08-20 裁定之名稱，見 R-VS3）
- 上游規格：`CFTS_044 Vehicle Controls`（SR26, 25PI3.5）
- 涵蓋能力：Heated Seat／Vented Seat／Heated Steering Wheel／Common
  Features（Stop-Start、LHD/RHD、Screen OFF、Headrest Dump、PHEV 等）
- 交付母本：036-A01 SWQT，`CFTS044 Vehicle Controls` 版本
  （客戶端已存在一份 237 列之投影稿，見 R-VS1）
- **本 feature 之 037 散落四份**（Common Features / HeatedSeat /
  VentedSeat / Heated Steering Wheel），為前所未見之形態；四份合併後之
  leaf 全集為本 feature 之需求母體。

### 2.1 素材身分（**本包所有數字之來源與其效力**）

本包 §5 之預期數字，量自 **2026-08-20 聊天附件之沙箱副本**，
**非 repo 物件、無雜湊**。依 G-L／R-U16，其地位為「**被取代**」而非
「被複驗」。**執行層須於 `inputs/` 之實體檔上全部重測**；不符者依 §8.5-2
回報，不得沿用本包數字。

兩份 `.docx` 附件之檔頭實測**已非 PK zip**（分別為 UTF-8 中文字元與
`|` 表格字元）——**是轉檔後之文字，不是原始二進位**。故 spec 基線
（`spec_mode = D`）**必須以原始二進位重建**，見 DR-1。

---

## 3. 裁決逐字（Pei 2026-08-20；本包之權威條文，照錄不得摘要）

```
R-VS1（既有 036 內容之效力）
036 交付母本現有 237 列，其 D / H / I / N 四欄經逐列驗證為 037 之機械
投影（I == 037 Requirement Description、H == 037 Requirement Title、
N == 037 Source Requirement ID，各 237/237 逐字全等），L / M 為 17 種
樣板句、無編號步驟，作者欄、TC ID、Test Group、Pre-Conditions、
Input Test Data、Priority、Design Method 全為空。

依 canon §2 之 qualifying done row 三判準，qualifying = 0。
裁定：**該 237 列效力等同 BLANK**。

推論（binding）：
(a) style authority 走 BLANK fallback chain（canon §2）——
    done region 不存在，**且不得取本管線自身之產出為 style authority**
    （canon §9.1 第 4 項）。
(b) 全欄重生，含 H 與 N；I 欄之上半段因 R-VS6 本來就要照抄 037 原文，
    重生後之上半段與現況相同不構成「保留」。
(c) 既有 237 列不享有 done-region 之凍結保護；write-back 為
    **append from first data row**（canon §2 之 BLANK 綁定）。
(d) 既有列之 L / M 樣板句**不得作為 exemplar**，其中 10 列內容為
    「Requirement is not clear for HU and System handling part」，
    屬上游未決之陳述，不得轉寫為 TC 內容。
```

```
R-VS2（錨鏈：SYS-RA-CFTS044-N 之解析）
037 之 Source Requirement ID 形如 SYS-RA-CFTS044-NNN，該識別碼不出現於
SYS2 匯出之任何儲存格，亦不出現於 CFTS044 規格內文；SYS2 之
`SYS2 Sys-RA-Feature-ID` 欄 538 列全空。

實測所得之對應為：
    SYS-RA-CFTS044-N
      = SYS2 匯出 `Basic Report` 工作表之**第 N 筆資料列**
        （資料自工作表列 2 起算，故工作表列號 = N + 1）
      → 該列 A 欄之 Polarion 項目 ID（NRL-6xxxx）
      → 該列 `SYS2 來源需求項目ID Source Requirement items` 之 7 位數 ID
      → 該 7 位數 ID 出現於 CFTS044 規格內文，即為條款錨點

裁定：**採此鏈為本 feature 之 SWE.1 → SWE.6 錨鏈**。

推論（binding）：
(a) `specification_reference`（036 N 欄）依 §10.7 與 spec_mode D，
    **由本鏈查得，不得構造**。現況 N 欄之 SYS-RA 原樣為投影產物，
    依 R-VS1 一併重生。
(b) 位移為 +1 且僅為 +1：以 037 Requirement Description 與 SYS2
    Description 逐字全等（空白正規化、轉小寫）之 31 組對照驗證，
    offset 0 命中 31、offset -1 與 +1 各命中 0。
(c) 本鏈之最末一段（7 位數 ID → 條款）目前只驗到「該 ID 存在於規格
    文字中」，**尚未驗到章節／條款號**——章節號須待 DR-1 之原始二進位
    到位後建 outline map 方能給出。在此之前 `specification_reference`
    之最終字串形式為 PENDING，不得先行生成 TC 之 N 欄。
```

```
R-VS3（命名）
Test Group（036 G 欄）= `Vehicle Setting`（單數，逐字）。
feature 目錄 = `features/vehicle_setting`。
scaffold 呼叫 = `python scripts/new_feature.py "Vehicle Setting" --adopt-existing`。

註：CFTS / SYS2 / 036 檔名皆作 `Vehicle Controls`，SYS3 SYSAD 標題作
`Vehicle Settings`。三者並存為既成事實，本裁定只約束**寫入工作簿之
Test Group 值**與 repo 目錄名，不改任何來源檔名。
```

```
R-VS4（Test Set，framework Part Vehicle Setting 之 Layer 2）
Layer 2 = 四個 Test Set，與四份 037 檔一一對應，逐字如下：

    Common Features
    Heated Seat
    Vented Seat
    Heated Steering Wheel

`Common Features`（56 leaf，內含 Stop-Start、LHD/RHD、Screen OFF、
Headrest Dump、PHEV 等異質能力）**整包為單一 Test Set，不再細分**。

此為對 §4.1.3「too coarse」與 §4.2「Forbidden: `General` / `Misc` /
`Unclassified`」之 **[OVERRIDE]**，理由為 037 之檔界即上游作者選定之
能力叢集邊界，四份檔本身就是 Layer 2 的來源證據（§4.1.2 之
「spec 目次 ∩ RD 分析報告分群」在本 feature 退化為單一來源：037 檔界）。
本 [OVERRIDE] 須以 §4.2 之引用形式寫入
`docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md`。

Layer 3（framework 內部、不出工作簿）= 037 檔內之 SWE ID 中段 token
（如 `LeftFrontHeatedSeat`、`ThreeStagesVentedSeatsManagement`），
用於 §4.1.4 之四項下游用途。
```

```
R-VS5（Input Test Data 欄之處置）
036 之 `Input Test Data`（K 欄）**不獨立承載資料**。資料一律落在：
  - 環境／週邊／訊號前提 → `Pre-Conditions`（J 欄）
  - 測試者操作之互動值 → `Test procedure`（L 欄）
  - 可觀察之結果值      → `Expected Result`（M 欄）
K 欄一律填 `NA`。

此為 §4.5 在本 feature 之收斂（§4.5 原文即允許 `NA`，本裁定將其定為
本 feature 之預設）。lint 須以此為判準：K 欄出現 `NA` 以外之值即 FAIL。
```

```
R-VS6（test_item 之兩段結構）
`Test Item`（036 I 欄）分上下兩段：
  上半段 = 來源條文**逐字**（本 feature 為 037 之 Requirement
           Description；不得改寫、不得摘要、不得補主詞）
  下半段 = 作者自訂之測試定義，**全部置於括號 ( ) 內**

裁定：**凡作者自己產生的文字，一律在括號內；括號外只能是來源逐字。**

推論（binding）：
(a) 上下兩段之間以單一空行分隔。
(b) 括號外出現任何非來源字串（含連接詞、補述、條件標籤）即 FAIL。
(c) 條款標籤（如 `HVS6.`）不是合法之上半段內容。
(d) 037 Requirement Description 內之 `$變數$` 記號（如 `$VentedSeatFL$`）
    屬來源逐字之一部分，於上半段原樣保留；下半段若需具體值，該值須
    有出處（§8.4.1），無出處者維持變數形式，不得填入猜測值。
```

---

## 4. 作業清單（Phase 0 → Phase 1）

前置：**Pei 將六份素材放入 `features/vehicle_setting/inputs/`**（Tier 3）。
未到位前 W-1 以後全部不啟動。

| # | 作業 | 依據 | 產出 |
|---|---|---|---|
| W-0 | `python scripts/new_feature.py "Vehicle Setting" --adopt-existing` | R-VS3 | feature 骨架；**本檔不得被覆寫** |
| W-1 | 對 `inputs/` 六檔逐檔 `shasum -a 256`，寫入 `inputs/INPUTS.sha256` | G-L | 每項含路徑與 SHA |
| W-2 | 四份 037 合併 leaf 全集：逐檔取 `Analysis Report`、表頭列 7、資料自列 8、A 欄非空者為 leaf | — | `data/leaves.tsv`，含 `swe_id / family / src_ref / title / desc` |
| W-3 | 036 現況重測：資料列 10–246、逐列、逐欄填充率；並逐列驗 I/H/N 是否等於 037 之 desc/title/src | R-VS1 | `docs/reports/036_baseline.md` |
| W-4 | 建 SYS-RA → SYS2 → Polarion 對照表：`SYS-RA-CFTS044-N` → `Basic Report` 第 N 筆資料列 → A 欄 NRL id → `Source Requirement items` 7 位數 | R-VS2 | `data/sysra_to_polarion.tsv` |
| W-5 | 反向驗證 W-4：含「什麼都沒做」之對照向；並證明 offset -1／+1 之命中為 0 | R-G7-1 | 上繳包附實測 |
| W-6 | 覆蓋差：leaf 全集 − 036 現有 D 欄值 | — | 未覆蓋 leaf 清單 |
| W-7 | 異常登記：SYS-RA 落在 SYS2 `Category = Heading` / `Information` 之 leaf 逐條列出 | Tier 1 registration only | `ANOMALIES.md` A-VS01（**登記，不裁定**） |
| W-8 | `$變數$` 全集抽取（037 desc 欄，正則 `\$[A-Za-z0-9_]+\$`），逐 token 統計出現次數與所屬 family | R-VS6(d)、§8.4.1 | `data/spec_variables.tsv` |
| W-9 | 跨 feature 重疊檢查：`features/comfort/` 之 037 與交付件中，是否已有 heated seat／vented seat／heated steering wheel 之 leaf 或 TC | §8.2.1、G-H、G-M | `docs/reports/comfort_overlap.md` |
| W-10 | 既有素材先查再要：`features/comfort/inputs/` 之 `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`、`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`、`SR24 R1 Market Configuration Table v1.6.xlsx` 是否覆蓋本 feature 之 UI／彈窗／市場配置需求 | G-H、G-M | 併入 `DATA_REQUESTS.md` |
| W-11 | `DATA_REQUESTS.md` 依 §6 之表填實（含路徑與 SHA 欄） | G-L | — |
| W-12 | `recon.py` 產 `RECON.md` + `DECISIONS.md` + `recon.json`；`feature.yaml` 填 `spec_mode = D` | canon §1 | — |

**W-9 為本包最可能改變範圍之項目**：Comfort HMI 已交付，若其已覆蓋座椅
加熱／通風之 HMI 行為，本 feature 之對應 leaf 須依 §8.2.1 委派而非重寫。
發現重疊即停下升級（見 §7）。

---

## 5. 預期數字（沙箱實測；執行層須於 `inputs/` 重測並逐項對照，相符者亦列出）

### 5.1 掃描條件

- 037：`Analysis Report` 工作表；表頭列 7；資料列 8 起；A 欄非空 = leaf；
  比對逐字全等，**先做空白正規化（`\s+` → 單一空格）並轉小寫**者另行標明
- 036：`Test Case Specification 測試用例規範`；表頭列 9；資料列 10–246；
  **逐列**（非逐引用）；空字串與純空白計為空
- SYS2：`Basic Report`；表頭列 1；資料列 2 起；**「第 N 筆資料列」以資料
  序號計，非工作表列號**
- 正則：`SYS-RA-CFTS\d+-\d+`（不分大小寫）、`\b\d{7}\b`（7 位數 Polarion
  ID，**有詞界**）、`\$[A-Za-z0-9_]+\$`

### 5.2 預期值

| 項目 | 預期 |
|---|---|
| 037 leaf 總數 | **271** |
| ── Common Features | 56 |
| ── HeatedSeat | 99 |
| ── VentedSeat | 81 |
| ── Heated Steering Wheel | 35 |
| 完整 SWE ID 跨四檔重複數 | **0**（271 uniq / 271） |
| 尾碼 `-001` 之出現次數 | **4**（四檔各自重起；最大尾碼 99） |
| 037 之 SYS-RA 引用（distinct） | **273**，全部指向 CFTS044 |
| 被兩個以上 leaf 共用之 SYS-RA | **0** |
| SYS-RA 編號域 | 19–336，區間內缺 **45** 號 |
| 036 資料列 | **237** |
| 036 qualifying done row | **0** |
| 036 填充：B / D / H / I / N | 各 **237** |
| 036 填充：L / M | 各 **191** |
| 036 填充：C/E/F/G/J/K/O/P/Q/R/S/T–Z/AA/AH | 各 **0** |
| I == 037 desc ／ H == 037 title ／ N == 037 src | **237 / 237 / 237** |
| L 之相異值數 ／ M 之相異值數 | **17** ／ **44** |
| L 為 `Requirement is not clear…` 系列之列數 | **12**（三種措辭：10 / 1 / 1） |
| 036 D 欄值全部落在 leaf 全集內 | **是**（237/237，0 未匹配，0 重複） |
| 未被任何 036 列覆蓋之 leaf | **34**（Common 10 / HeatedSeat 11 / VentedSeat 9 / HSW 4） |
| SYS2 `Basic Report` 資料列 | **538** |
| SYS2 `Sys-RA-Feature-ID` 欄非空列 | **0** |
| SYS2 全表 `SYS-RA-CFTS…` 命中 | **0** |
| 037 desc ↔ SYS2 desc 逐字全等之對照組 | **31**；offset 0 命中 31，offset −1／+1 各 **0** |
| 271 leaf 之 SYS-RA 全部落在 SYS2 資料列範圍內 | **是** |
| SYS-RA 指向列之 `Category`（逐引用，273） | Functional Requirement **239** ／ Heading **25** ／ Information **9** |
| 其 7 位數 Polarion ID 出現於 CFTS044 文字者 | **270 / 271** |
| 例外 | `SWE1-VC-HeatedSteeringWheel-009`（SYS2 該列 `Source Requirement items` 為空） |
| CFTS044 文字中 7 位數 ID（distinct） | **2302** |
| 037 desc 含 `$變數$` 之 leaf | **196 / 271**；相異 token **30** |
| 出現最多之 token | `$VentedSeatFR$` 89、`$VentedSeatFL$` 80、`$HSW_Stat$` 48 |

### 5.3 已聲明之盲區（R-G11）

1. **7 位數 ID 之比對跑在轉檔文字上**，非原始 docx。轉檔可能吞掉表格欄位
   或改變數字周邊字元；`\b\d{7}\b` 亦可能命中非 ID 之七位數字。
   **DR-1 到位後須在原始二進位上重跑，本項數字在那之前為暫定。**
2. **「ID 存在於文字中」不等於「條款號已解析」**（R-VS2(c)）。
3. **31 組對照組偏向描述未被 SWE.1 改寫者**，其代表性未證。offset 結論
   之強度來自「另兩個位移皆為 0」，不來自樣本量。
4. 036 之 237 列以 D 欄非空為判準；若母本另有隱藏列或篩選，本數字未涵蓋。

---

## 6. `DATA_REQUESTS.md` 初始內容（W-11 據此填入，**每項須補路徑與 SHA**）

| # | 檔案 | 為何需要 | 阻塞什麼 | Urgency |
|---|---|---|---|---|
| 1 | **CFTS044 原始 `.docx` 二進位**（`R1LR_Atl-H_25PI3.5_…CFTS_044_Vehicle Controls_SR26_20250909-1816.docx`） | 建 outline map、解析條款號；轉檔文字不得為基線 | `specification_reference` 全欄、spec 切分、TC 生成 | **High** |
| 2 | **SYS3 SYSAD 原始 `.docx` 二進位**（`SYS3_Vehicle Settings_FM-WI-FSM-011-A01…v1.0`） | 架構面對照、確認 Vehicle Setting 之範圍界定 | 範圍問題之佐證 | Medium |
| 3 | 六份素材落入 `inputs/` 並取 SHA | G-L：沒有路徑的「到齊」不算到齊 | 全部 | **High** |
| 4 | `$變數$` 30 個 token 之值域來源（CAN 訊號字典／DBC／PROXI 或等價文件） | ER 需具體可觀察值；無出處不得填（§8.4.1） | 196 leaf 之 ER 具體性 | **High** |
| 5 | 座椅／方向盤加熱之 HMI L&F 與彈窗文字 | 畫面文字保真度 | UI 類 leaf | Medium（**先查 W-10 之三份既有檔**） |
| 6 | Comfort HMI 037 與其交付件（repo 內已有） | §8.2.1 委派判斷 | 範圍界定 | Medium（**repo 內，非缺件**） |

**Standing rule（沿用 AMFM）**：任何新發現之外部引用，於登記當下就在本表
開一列，而不只開一條 anomaly——anomaly 記錄缺口，本表提出要求。

---

## 7. 升級條件（撞到即停，回報後續作不受影響之部分）

1. W-4／W-5 之對照在任一 leaf 上不成立（offset 非 +1、或指向列不存在）
2. W-9 發現 Comfort 已覆蓋本 feature 之 leaf
3. 036 母本結構與 `forms/…_SWQT_20260817_ext.xlsx` 不一致（R-G1 之母本身分）
4. 037 四檔之間出現同一 SWE ID 或同一 SYS-RA 被兩 leaf 共用
5. 任何實測與 §5.2 之預期不符（§8.5-2：回報，不調和）
6. 需要之判斷在本包無條文

---

## 8. 上繳要求（`docs/upstream/00_intake_and_rulings.md`）

1. §5.2 逐項「預期 vs 實測」對照，**相符者亦列出**
2. 不符項目逐項說明，不自行調和
3. §8.4 結果三分法分類（改對了／核實無誤／正確地不動）
4. 本包實際使用之掃描條件揭露（欄位範圍、大小寫、詞界）
5. W-5 之反向驗證實測（含對照向）
6. 新開 anomaly 與 DR **成對**
7. 未預期之發現
8. **「本包是否仍有該驗而未驗者」之獨立判斷**（不得省略）
9. 更新 `docs/INDEX.md`（分析層不寫）

---

## 9. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS1 | 既有 237 列效力等同 BLANK | ✔ §3 |
| R-VS2 | SYS-RA → SYS2 → Polarion 錨鏈 | ✔ §3 |
| R-VS3 | Test Group = `Vehicle Setting`；目錄 `vehicle_setting` | ✔ §3 |
| R-VS4 | 四個 Test Set；`Common Features` 整包（§4.1.3／§4.2 之 [OVERRIDE]） | ✔ §3 |
| R-VS5 | Input Test Data 欄一律 `NA`，資料落 J／L／M | ✔ §3 |
| R-VS6 | test_item 上半逐字、下半作者自撰且全在括號內 | ✔ §3 |

逐條確認：六條皆以獨立可貼入之區塊呈現，未夾在敘述中。
