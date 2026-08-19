# 交付說明 — FW036 User Profiles 測試用例（189 條）


<!-- fingerprint:begin -->
## 語料指紋（G-F，45 包）—— 標記輪次：**45**

> **本表是本檔之保鮮期。** 引用本檔前先跑：`stamp_static_doc.py --verify <本檔>`；
> **不符即「已過期，拒絕採信」**，須重出後再引。
> 指紋之範圍為**全欄**（保守）—— 誤判過期只是多重出一次，誤判新鮮則是拿舊資料下判斷。

| tc_id | digest |
|---|---|
| `NR1L-UserProfiles-002` | `9ac76f9f742c` |
| `NR1L-UserProfiles-082` | `a36c22f4b4b1` |
| `NR1L-UserProfiles-095` | `8dab76c9afdb` |
| `NR1L-UserProfiles-102` | `1f251cf01cf3` |
| `NR1L-UserProfiles-111` | `d4fd3ed6fe04` |
| `NR1L-UserProfiles-127` | `e50f5f385a9e` |
| `NR1L-UserProfiles-129` | `1b315bff0af8` |
| `NR1L-UserProfiles-134` | `477d04ade265` |
| `NR1L-UserProfiles-136` | `0011ec5d1d9a` |
| `NR1L-UserProfiles-138` | `b68bf11414e3` |
| `NR1L-UserProfiles-139` | `b4e94adced40` |
| `NR1L-UserProfiles-140` | `ce7c1d2e1213` |
| `NR1L-UserProfiles-141` | `bc9a4e380685` |
| `NR1L-UserProfiles-142` | `cbc421ff2ec9` |
| `NR1L-UserProfiles-143` | `1a922483286f` |
| `NR1L-UserProfiles-146` | `d1c8b027e53c` |
| `NR1L-UserProfiles-151` | `f3c4c3fb46ec` |
| `NR1L-UserProfiles-159` | `80f2cfc3ebfe` |
| `NR1L-UserProfiles-164` | `da177ac5f34b` |
| `NR1L-UserProfiles-166` | `758cb5dfdf95` |
| `NR1L-UserProfiles-169` | `1b9f5f9f5eaa` |
| `NR1L-UserProfiles-170` | `c417cc548e08` |
| `NR1L-UserProfiles-174` | `42069a956cd7` |
| `NR1L-UserProfiles-177` | `e61be46633a0` |
| `NR1L-UserProfiles-182` | `51da38dbd00e` |
| `NR1L-UserProfiles-183` | `e3cd36b3f0a4` |
| `NR1L-UserProfiles-184` | `26624dab8817` |
| `NR1L-UserProfiles-188` | `e3b27fbf3204` |
| `NR1L-UserProfiles-189` | `fbeb005e8255` |

<!-- fingerprint:end -->

- 產出層：執行層｜2026-08-19
- 產出件：`FM-WI-FSM-036-A01 …_SWQT_UserProfiles_20260819_full.xlsx`
- 台帳：`DELIVERY.sha256` **ENTRY 001**（`type: produced`）
- **本說明隨產出件同時存在**；產出件之位元組不因本說明而變動

## 1. 內容

| 項 | 值 |
|---|---|
| 測試用例 | **189 條**（row 10–198，無留空列）|
| 需求覆蓋 | **180 / 180 leaf**（來源：`FM-WI-FSM-037-A03` 之 Functional Requirement 葉節點）|
| 列序 | 依 `Requirement or Design ID` 遞增 |
| 優先級 | P0×38、P1×66、P2×71、P3×14 |
| 設計方法 | 功能測試 120、狀態轉換 33、負向測試 16、情境／用例 9、邊界值分析 8、基礎故障注入 3 |

## 2. 覆蓋率之讀法 —— **請與第 3 節同讀**

> **全覆蓋（180 / 180）說的是 037 之每個 leaf 都有一條 TC，
> 不是每個 leaf 都驗完了。覆蓋率是分母的性質，不是分子的品質。**

一條 TC 之 `specification_reference` 列了某節，**不等於該節已被驗證**：
例如 `4.1` 與 `5.9` 之引用欄併列 PLP 表五列（`3.1`–`3.5`），
依據是該二需求之對象本來就是整張表，**而兩條 TC 各只實際驗了其中三列與一列**。

**故覆蓋稽核之分子一律取「實際被驗之節／列」，不取引用欄。**

## 3. 已具名之留白清單

以下各條之 `Remarks` 欄**自己載明了它不保證什麼** ——
其成因為條文未述、條文歧義未決，或該側之判別力不可造。
**這些不是缺漏，是已知且已記錄之邊界**；其未涵蓋之側，其結果不由該條保證。

| tc_id | 節 | leaf | 已具名之留白 |
|---|---|---|---|
| `NR1L-UserProfiles-095` | 4.5.1 | `SWE1-HMI-PROF-008` | 座椅鍵 ≥ 3 之情形條文未述，依 §8.4.1 不推定。 |
| `NR1L-UserProfiles-102` | 4.6.1 | `SWE1-HMI-PROF-014` | 圖像 avatar 之情形條文只寫 with avatar，未另述其呈現，依 §8.4.1 不推定，故不另立 TC。 |
| `NR1L-UserProfiles-111` | 5.1 | `SWE1-HMI-PROF-018-03` | 已在該分頁時再按之行為條文未述，依 §8.4.1 不推定。 |
| `NR1L-UserProfiles-129` | 5.8 | `SWE1-HMI-PROF-031` | popup 之 PU id 條文未給，故 ER 只述其**內容要旨**，不寫 PU 編號（§8.4.1 不推定）。 |
| `NR1L-UserProfiles-134` | 5.7 | `SWE1-HMI-PROF-030-01` | **受檢之兩個畫面為抽樣（X-2）**，非窮舉；見 reasoning。 |
| `NR1L-UserProfiles-136` | 5.12.1 | `SWE1-HMI-PROF-037` | **盲區（R-G11）**：能分辨「依座椅連結排序」與「依名稱排序」之設置，須有一個座椅連結順序**不同於**名稱順序之車輛；而 5.12.2 已定編輯連結不改順序，**故該設置無法以編輯造出**，出廠即如此之車輛亦不在手上。 |
| `NR1L-UserProfiles-138` | 5.13 | `SWE1-HMI-PROF-039` | 回復預設之**入口**條文未載，依 §8.4.1 不自擬 ——執行時依實車之回復入口，其位置記於執行紀錄。 |
| `NR1L-UserProfiles-139` | 5.13.1 | `SWE1-HMI-PROF-040` | **PU0626 與 PU_0129 之關係條文未定**（RD #8）。 |
| `NR1L-UserProfiles-140` | 5.13.2 | `SWE1-HMI-PROF-041-01` | **PU0626 與 PU_0129 之關係條文未定**（RD #8）。 |
| `NR1L-UserProfiles-141` | 5.13.2 | `SWE1-HMI-PROF-041-02` | **PU0626 與 PU_0129 之關係條文未定**（RD #8）。 |
| `NR1L-UserProfiles-142` | 5.13.2 | `SWE1-HMI-PROF-041-03` | **RD #8 —— 41 包 §四授權逕行修正**：5.13.2 之確認 popup 同時寫了 PU0626（`confirming from popup PU0626`）與 PU_0129（`pressing Yes/Ok in pop-up PU_0129`），**兩者之關係條文未定義**。 |
| `NR1L-UserProfiles-143` | 5.13.2 | `SWE1-HMI-PROF-041-04` | **故障注入之對象為 TBM 之完成回報**，非 HU —— 條文寫的是`if HU or TBM do not confirm`，兩者為**析取**；注入其一即足以使該條件成立，**HU 側之注入本條不涵蓋**（其結果不由本條保證）。<br>注入手段（拔線／模擬器／診斷指令）條文未載，依 §8.4.1 不自擬，執行時之手段記於執行紀錄。 |
| `NR1L-UserProfiles-151` | 6.3.1 | `SWE1-HMI-PROF-050-01` | **刻意不斷言 key cycle 內之顯示與否**：「key-on 是否算一次 activation」條文未定義，依 §8.4.1 保留歧義，不以本條推定。 |
| `NR1L-UserProfiles-159` | 7.2 | `SWE1-HMI-PROF-058` | **「小版」與「大版」之選用條件條文未載** —— 7.2 與 7.2.1 各自描述其內容，未說何時用哪一個。<br>依 §8.4.1 不推定，以 pre-condition 具名為本車適用小版，**該條件本身不由本條驗**。 |
| `NR1L-UserProfiles-164` | 7.4 | `SWE1-HMI-PROF-062-04` | **盲區（R-G11）**：`for the duration of the current session` 之「session」條文未定義其邊界。<br>步驟 2 以一次畫面往返代表之，**那是抽樣而非窮舉** —— 更長之 session 內是否返回，本條不保證。 |
| `NR1L-UserProfiles-166` | 7.5 | `SWE1-HMI-PROF-064` | 本條取**互動**一側，**為抽樣而非窮舉**（§8.4.2）：另兩側之同型性不由本條保證。 |
| `NR1L-UserProfiles-170` | 8.3.1 | `SWE1-HMI-PROF-068` | **未驗「確認之後真的丟棄」** —— 條文只說「給另一個 popup 問」，丟棄之後果未述，依 §8.4.1 不推定。<br>**條文列兩處入口**（`main menu bar or status bar`）——本條取狀態列一側，**為抽樣**（§8.4.2）：主選單列一側之結果不由本條保證。<br>取狀態列之理由：其於設定 popup 顯示期間仍可見（4.6），主選單列是否可見條文未述。 |
| `NR1L-UserProfiles-174` | 8.6 | `SWE1-HMI-PROF-072` | **非連網車輛之第一步條文未述**，依 §8.4.1 不推定，亦不列為覆蓋缺口（037 未為其切 leaf）。 |
| `NR1L-UserProfiles-177` | 8.7.1 | `SWE1-HMI-PROF-074` | **未驗「無前一步時 Back 不出現」** —— 那是同一句之反向，037 未為其切 leaf，依 R-U56 不造。 |
| `NR1L-UserProfiles-182` | 8.8.1 | `SWE1-HMI-PROF-077` | 分類是否影響一次可見之數目，條文未述；本條之計數為**跨分類之總數**，已於 reasoning 具名。 |
| `NR1L-UserProfiles-183` | 8.8.2 | `SWE1-HMI-PROF-078` | **7 吋之獨立分類畫面未涵蓋**：條文寫 `7" will have a separate screen for category selection`，而 037 未為其另切 leaf —— 本條取 8.4 吋以上一側，**為抽樣，7 吋之分類畫面不由本條保證**。 |
| `NR1L-UserProfiles-184` | 8.9 | `SWE1-HMI-PROF-079` | **未走 `Create from Default` 一側**：條文只說選了 current 會沿用，未說選了 default 會如何（`Default` 之內容未定義），依 §8.4.1 不推定。 |
| `NR1L-UserProfiles-188` | 8.11 | `SWE1-HMI-PROF-083` | 條文列 username 與 avatar 兩個入口，本條取 avatar 一側（條文自己舉的例即為 avatar），**username 一側為同型**，其結果不由本條保證。 |
| `NR1L-UserProfiles-189` | 8.12 | `SWE1-HMI-PROF-084` | `(until canceled)` 之取消側未驗 —— 條文未說取消後選擇何時清除，依 §8.4.1 不推定。 |

**合計 24 條帶留白聲明**（全語料 189 條之 12%）。

### 3.0 上游文件所述而本次未涵蓋者（52 輪補入）

以下由**被引用之外部規範**所述，而 `FM-WI-FSM-037-A03` 未為其產出需求項，
**本次交付未涵蓋**：

| 出處 | 內容 | 本次之狀態 |
|---|---|---|
| Tutorials HMI Logic and Flow `INTR2.)` | 下載既有 profile 時 Tutorials 不顯示 | **未涵蓋** —— 037 未為其產出需求項 |

**列此不是為了聲明免責，是為了讓看的人自己判斷要不要補。**

### 3.1 三類留白之分別

| 類 | 意思 | 例 |
|---|---|---|
| **條文未述** | spec 沒寫，依 §8.4.1 不代其推定 | `095`（座椅鍵 ≥ 3）、`174`（非連網車輛之第一步）|
| **條文歧義未決** | spec 兩處寫法不一致，已開查詢單 | `139`–`143`（`PU0626` 與 `PU_0129` 之關係，RD #8）|
| **判別力不可造** | 兩種實作在可造出之設置下不可分辨 | `136`（座椅連結排序 vs 名稱排序 —— 5.12.2 已定編輯不改順序，故該設置造不出來）|

**第三類最值得注意**：它不是寫得不夠好，是**可測性之上界**。

## 3.5 上游文件之記載不一致（A-UP14）

**兩份上游文件對三個 popup id 之角色記載不同，本次交付依本 feature 之
spec（`Personal Account HMI Logic and Flow` §5.13.2）生成：**

| id | 本交付件所依據者（我方 spec）| Pop Up List HMI R1 SR24 Post 2A（Dec 15, 2023）|
|---|---|---|
| `PU1089` | 使用者確認清除時顯示（進行中）| `Displayed if HU or TBM do not confirm complete default restoring`（失敗）|
| `PU1090` | 清除成功後顯示（完成）| `Displayed when users confirm data clearing …`（進行中）|
| `PU1091` | HU／TBM 未確認完成時顯示（失敗）| `Displayed when data have been succesfully cleared`（完成）|

**三者之角色整體錯開一位。** 受影響者為 `NR1L-UserProfiles-142`／`143`。

**本次未自行裁決何者為準** —— 已列入查詢。
**若以 Pop Up List 為準，該兩條之三個 id 須對調。**

## 4. 外部文件依賴

以下三處之規則權威在本 spec 之外，ER 只驗其形態，不代其判定內容：

| 條 | 依賴 |
|---|---|
| `NR1L-UserProfiles-146`（5.15.1）| 截斷規則在 **Core HMI Logic and Flow** |
| `NR1L-UserProfiles-169`（8.3）| 設定流程各步驟之 popup 對映在 **HMI Pop Up List** |
| `NR1L-UserProfiles-082`（4.1.1）| `PU1087`／`PU1088` 之 popup **內文**不在現有 Pop Up List（其**觸發條件**已載於 spec，故本條仍可判定）|

## 4.1 尚缺之上游素材（3 項）

| # | 缺什麼 | 卡住哪幾條 | 我方之替代作法 |
|---|---|---|---|
| 1 | `PU1087`／`PU1088` 之 popup **內文** | `NR1L-UserProfiles-002`／`082`（4.1.1）| 兩條之 ER 只斷言**觸發條件與顯示**，不寫內文 —— **兩條現在即可執行**；得內文後可再加一句文字斷言 |
| 2 | R1 High 之 label 覆寫是否及於整個 Editing 章 | `017`／`074`（9.1）、`020`／`077`（9.2）| **兩種讀法各造一條**（`017` 用 Connected Account、`074` 用 Stellantis Account）；`020`／`077` 為缺席斷言，其判定不依 label |
| 3 | 「有 app 之區域 × 不支援 connected profile 功能」之車輛組合是否可佈署 | `077`（9.2）| ER 為**缺席斷言**（該按鈕不顯示），其判定不依賴該組合是否存在 |

**三項皆不擋執行** —— 各條之替代作法已如上。

## 5. 欄位之填寫範圍

**已填（14 欄）**：`D F G H I J K L M N P R S AH`

**留空，逐欄具名理由**：

| 欄 | 為何留空 |
|---|---|
| `B` | 母本自身之序號公式（shared formula），寫入即破壞其機制 —— **原樣保留** |
| `C`／`E` | 上游系統（Polarion／TestRail）之 id，我方無 |
| `O`（Test Case Reference ID）／`AA`（Author） | 依同表單之既有交付件實測：該兩欄逐列為空 |
| `Q`（預估測試時間）／`AB`（Test Version） | 同上；且我方未估過，**不編** |
| `T:Z`（七個車型） | 同上（466 列全空），且母本該區之資料驗證自帶 `allowBlank`。**本 feature 189 條之 pre-condition 無一條提及車型** —— 其適用車型須由更上層決定 |
| `AC`–`AG` | 執行階段之欄位，交付時應為空 |
| `AH`（Remarks）| **本次交付全欄留空**（客戶端決定）。各條之設計理由與其限制**改由本說明之第 3 節承載** —— 該節逐條列出「哪一條不保證什麼」|

## 6. 尚未完成者

- **12 條**（`163`–`165`、`174`–`182`）之第二人覆核未完；
  其所生之修正於下一次重寫回落地
- 版本以 `DELIVERY.sha256` 之 **ENTRY 編號**區分，**不以「最終版」名之**
- 查詢單 **RD #5／#6／#8** 未寄出

## 7. 完整性

產出件與母本之差異**僅限於資料列之內容欄**：
zip member 集合 48 = 48、`x14 dataValidation` 節點 1 = 1、
其 `sqref` `R10:R1411` 未變、legacy 資料驗證 4 = 4。
**下拉選單、列印設定、共用字串表、公式與版面皆與母本一致。**
