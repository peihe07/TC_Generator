# 03 — Power Management framework 定版所需輸入（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 03
結果：**十一步全部完成，無停止。§D 十八項全數已量測，無 MISMATCH。**
B1 / B2 / B3 三項素材齊備，待 Pei 依 R-P15(b) 逐條裁定 11 條。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| A 訂正 02 包兩處條數（R-P19） | DONE |
| B 建立 `handoff/03_framework_inputs.md` | DONE（原不存在；自檢三處一致） |
| 1 訂正 02 包條數 | DONE |
| 2 G0 前置閘 | **PASS 7 / 7** |
| 3 §C 座標訂正 ＋ G6a / G6b | DONE —— **G6b 精確還原 01 包之 336/337** |
| 4 037 兩分頁座標 ＋ G15 ＋ 三條 anomaly 複驗 | DONE —— 一條成立、一條成立且應加強、**一條描述有誤** |
| 5 B1 跨多章節 leaf 清單 | DONE（11 條，`data/multi_chapter_leaves.md`，無建議歸屬） |
| 6 B2 §1.6.2.1.17 素材 | DONE |
| 7 B3 SYS3 SYSAD（R-P20） | DONE（`data/sys3_chapters.md`，47 heading） |
| 8 G14 次章節涵蓋（R-P22） | DONE —— **9 章未被任何 leaf 覆蓋** |
| 9 §D 全表自驗 | DONE（`scripts/verify_gates_03.py`） |
| 10 §A 九條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE |
| 11 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

**本包三項最重要之發現**（全部為新事實，非覆述）：

1. **§E 之全部差額由恰好兩顆 leaf 造成** —— `SWE-PM-008` 與 `SWE-PM-057`。
   算術完全閉合，見 §五。
2. **R-P16 刪除 §1.8.1 之前提有問題** —— `SWE-PM-057` 實際觸及 §1.8.1.1.1
   且為三方同票之一。見 §五、A-PW14。
3. **9 個章節在現行作法下不會產生任何 TC**，含 `Stolen Vehicle Mode`、
   三個 `Logistic` 狀態、`ICS Wakeup Reasons by POWER Button Pressed`。
   見 §八、A-PW16。

---

## 一、步驟 A —— 02 包條數訂正（R-P19）

| 位置 | 原 | 現 |
|---|---|---|
| §A 末句 | 以上**七**條裁決條文 | 以上**六**條裁決條文 |
| §H 步驟 8 | §A **七**條裁決逐字抄入 | §A **六**條裁決逐字抄入 |
| §J | 六條（**未動**） | 六條 |

訂正後重驗：檔案 9,887 bytes，strict UTF-8 通過，U+FFFD = 0，
**§A fenced block = 6**，編號 `R-P9…R-P14` 無缺無重，
全檔「七條」出現 **0** 次、「六條」**3** 處一致。

### 03 下放包自檢

11,025 bytes，strict UTF-8 通過，U+FFFD = 0，`R-P3′` PRIME 完好。
**§A 區塊數 = 9**（`R-P15…R-P23`）、**§J 列數 = 9**、**§H 步驟數 = 11**、
§D 列數 = 18。三處一致，與 §J 自檢所宣稱相符。

---

## 二、素材台帳第（d）欄（R-P23）

R-P13 之（a）（b）（c）欄見 02 上繳包 §二 / §三，內容不變。本包補（d）：

| 項目 | 實測值 |
|---|---|
| OS | macOS **26.5.2**（BuildVersion **25F84**）／Darwin **25.5.0** arm64 |
| `textutil` | `/usr/bin/textutil`，173,088 B，mtime 2025-06-25（系統二進位，無版本字串可查；`kMDItemVersion` 為 null，故以 OS build 為版本代理） |
| Python | 3.10.13 |
| openpyxl | 3.1.5 |

**跨機器可重現性仍未驗** —— `textutil` 無獨立版本號可鎖定，只能以 OS build
代理。此為 R-P23 所指之風險，登記不變。

### 本包新增之衍生物（SYS3，R-P20）

| 衍生物 | bytes | SHA256（全 64 碼） | 來源 | 轉換 |
|---|---|---|---|---|
| `data/textlayer/sys3_plain.txt` | 46,850 | `1470be41bc65df68ef030b6eb8abe67cb1b7cf7bb0b7557741aaf0355879ddbb` | SYS3 `.docx`（`cb6bf7d8…`） | `zipfile` 讀 `word/document.xml`，依 R-P17 之 plain 序列化 |
| `data/textlayer/sys3_bold.txt` | 47,222 | `d0ce231958a054a7744692f1a8102b2437097b440d5299f3981218fa72c67641` | 同上 | 同上，bold 序列化 |

SYS3 原始檔 bytes / SHA256 依 B3 之指示不重測，僅驗 G0 相符 —— **相符**。

---

## 三、§D 全表實測值對照（**上繳項二**）

產生指令：`python features/power/scripts/verify_gates_03.py`

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | **7 / 7** | PASS |
| G1 | 037 leaf 數 | 115，連續無斷點 | **115**，連續=True | PASS |
| G2 | Categorization 值域 | `Functional Requirement` ×115 | `{'Functional Requirement': 115}` | PASS |
| G3 | leaf → CFTS 章節解析成功數 | 114 / 115，失敗者 `SWE-PM-089` | **114 / 115**，失敗=`['SWE-PM-089']` | PASS |
| G4 | leaf 域分布 | 111 / 3 / 1，三組互斥 | **111 / 3 / 1**，兩者皆有=0 | PASS |
| G5 | 需 CFTS010 之 leaf | `071` `072` `073` | **恰為該三者** | PASS |
| G5b | 該三 leaf 之解析章節 | 071→§1.7.1.1.1、072→§1.7.1.1.1、073→§1.7.2 | **完全相符** | PASS |
| G6a | SYS2 CFTS009 欄內 token 可抽取率（r2–r339） | 【實測填入】 | **337 / 338** | 已填空（R-P18） |
| G6b | token 可解析至 CFTS 章節之比率 | 【實測填入】 | **列層 336 / 337；token 層 438 / 439**；唯一未解析 = `Sys-RA-PM-0334` → `4942087` | 已填空（R-P18） |
| G7 | SYS2 CFTS010 全 id 可解析者 | 73 / 73 | **73 / 73** | PASS |
| G8 | CFTS009 需求錨點 / 章節錨點 unique | 904 / **196**（R-P17） | **904 / 196** | PASS |
| G9 | CFTS010 需求錨點 / 章節錨點 unique | 148 / 92 | **148 / 92** | PASS |
| G10 | FW036 workbook_state | BLANK（非空 = 0） | 非空 **0** → **BLANK** | PASS |
| G12 | §C 各組讀取座標 | 實測與 §C 一致（含 r2–r339） | 六組全數相符，見 §3.2 | PASS |
| G13 | 跨多章節 leaf 數 | 11，ID 清單與 B1 一致 | **11**，清單與 B1 逐一相符 | PASS |
| G14 | 次章節涵蓋（R-P22） | 【實測填入】 | 被丟棄次章節 **10** 個，**未被覆蓋 9 個** | 已填空 |
| G15 | 037 兩分頁座標與列數（R-P21） | 【實測填入】 | Traceability r1／r2–r34＝33 列；Excluded r1／r2–r27＝26 列 | 已填空 |
| G16 | SYS3 SYSAD 章節錨點數 | 【實測填入】 | **0**（§C rule 1 於本文件不匹配，成因見 §七） | 已填空 |

**十四項有明確期望值者全數 PASS，四項填空項已填。無 MISMATCH。**

### 3.1 G6a / G6b —— R-P18 之診斷獲得實測確證

- **G6a = 337 / 338**。r2–r339 共 338 列全非空；唯一無 token 者為 **r339**。
  該列實測 `ID` = `NRL-142587`、**`Type` = `Heading`**、`Sys-RA-Feature-ID` 欄為空、
  `Source Requirement items` 欄為空 —— 與 R-P18 之描述**逐字相符**。
- **G6b 列層 = 336 / 337**，唯一失敗者 `Sys-RA-PM-0334`（`4942087`）。
  **此數精確還原 01 包之「336/337，失敗者 Sys-RA-PM-0334」。**
  即該數字本身正確，錯的是它被掛在第一段（G6）而非第三段。R-P18 之診斷成立。
- **G6b token 層 = 438 / 439**。439 個 token 中 82 個無法經需求錨點路徑解析，
  分類實測：**81 個為 CFTS009 之章節錨點 id**（Sys-RA 直接指向章節，
  例 `4941006` = §1 Wake-up and Power-up），**1 個兩路皆無**（`4942087`）。
  → 登記為 **A-PW15**。已驗：兩種讀法對 G3（114/115）與跨章節 leaf 名單
  （11 個，逐一相同）**皆無影響**，故本包未擴張 §C rule 3。

### 3.2 G12 / G15 —— 六組座標實測

| 座標 | §C 所載 | 實測 | 判定 |
|---|---|---|---|
| 037 `SWE1 Requirements` | 表頭 r7；r8–r145 | 138 列，非空 115；sheet max_row=244（r146 以後全空） | 相符 |
| 037 `SYS2 Traceability` | **本包實測填入** | 表頭 **r1**；資料 **r2–r34** = 33 列，全非空；sheet max_row=34 | 新填（G15） |
| 037 `Excluded NRLs (HW-only)` | **本包實測填入** | 表頭 **r1**；資料 **r2–r27** = 26 列，全非空；sheet max_row=27 | 新填（G15） |
| SYS2 CFTS009 `Basic Report` | 表頭 r1；r2–**r339**（R-P18） | 338 列，全非空；sheet max_row=340（r340 空） | 相符 |
| SYS2 CFTS010 `Basic Report` | 表頭 r1；r2–r74 | 73 列，全非空；sheet max_row=75（r75 空） | 相符 |
| FW036 `Test Case Specification&Result` | 表頭 r9；r10–r221 | 212 列，非空 0；sheet max_row=221 | 相符 |

---

## 四、B1 —— 跨多章節 leaf 清單（**上繳項一之一**）

全文見 `features/power/data/multi_chapter_leaves.md`（18,718 bytes，11 條）。
產生指令：`python features/power/scripts/build_b1.py`。
**依 R-P15(b)，該檔不含任何建議歸屬。**

概覽（相異章節集合）：

| # | leaf | Requirement Title | 相異章節集合（含出現次數） |
|---|---|---|---|
| 1 | `SWE-PM-001` | Full-Operation | §1.6.2.1(2)、§1.6.2.1.1(3)、§1.6.2.1.14(1) |
| 2 | `SWE-PM-002` | Idle | §1.6.2.1(2)、§1.6.2.1.2(7)、§1.6.2.1.14(1) |
| 3 | `SWE-PM-003` | — | §1.6.2.1(2)、§1.6.2.1.3(5)、§1.6.2.1.4(1)、§1.6.2.1.14(1) |
| 4 | `SWE-PM-004` | — | §1.6.2.1(2)、§1.6.2.1.5(5)、§1.6.2.1.14(1)、§1.6.2.1.15.1(1) |
| 5 | `SWE-PM-005` | — | §1.6.2.1(2)、§1.6.2.1.6(4)、§1.6.2.1.14(1) |
| 6 | `SWE-PM-006` | — | §1.6.2.1(2)、§1.6.2.1.7(4)、§1.6.2.1.14(1) |
| 7 | `SWE-PM-007` | — | §1.6.2.1(2)、§1.6.2.1.8(2)、§1.6.2.1.14(1) |
| 8 | **`SWE-PM-008`** | — | §1.6.2.1(2)、§1.6.2.1.9(3)、§1.6.2.1.10(2)、§1.6.2.1.11(2)、§1.6.2.1.14(1)、**§1.6.7.1(4)** |
| 9 | `SWE-PM-009` | — | §1.6.2.1(2)、§1.6.2.1.13(8)、§1.6.2.1.14(1) |
| 10 | **`SWE-PM-057`** | Proxi Parameter management | **§1.6.2.1.17(3)、§1.6.3.1.1(3)、§1.8.1.1.1(3)** —— 三方同票 |
| 11 | `SWE-PM-093` | — | §1.3.5(1)、§1.9.8(1) —— 兩方同票 |

### 4.1 結構事實（非建議歸屬）

- **#1–#9 共用同一雜訊組合**：九條全部同時命中 `§1.6.2.1`（父章節，
  `TLM algorithm requirements`）與 `§1.6.2.1.14`
  （`TLM modules and functionalities depending on operative state`）。
  九條之差異只在各自的一個 `§1.6.2.1.x` 子章節。
  即 `§1.6.2.1` 與 `§1.6.2.1.14` 是**跨 leaf 的共同背景**，
  不是任何單一 leaf 的特徵。
- **#11 之兩章節同屬 Startup Display**（§1.3.5、§1.9.8），
  無論怎麼裁，Test Set 分布不變。
- **只有 #8 與 #10 之裁定會改變 Test Set 分布。** 見 §五。

---

## 五、§E 差額之完整算術閉合（新發現）

02 包實測 62 / 24 / 16 / **8** / 3 ＋ 未歸類 1，對 §E 之 64 / 24 / 16 / **7** / 3。
本包查明差額**全部**來自 §四表中的兩顆 leaf：

| leaf | 02 規則指派 | 落入 | 對分布之影響 |
|---|---|---|---|
| `SWE-PM-008` | §1.6.7.1（4 次，最高票） | **Timeout Settings** | Power State **−1**，Timeout **+1** |
| `SWE-PM-057` | §1.6.2.1.17（三方同票，取最深） | **未歸類**（§E Layer 3 無此章節） | Power State **−1**，未歸類 **+1** |

- Power State：64 − 1 − 1 = **62** ✓
- Timeout Settings：7 + 1 = **8** ✓
- 未歸類：0 + 1 = **1** ✓
- 其餘三個 Test Set 未受影響 ✓

**算術完全閉合。** §E 之 64 / 24 / 16 / 7 / 3 與實測之差，
不是分組規則的系統性歧異，而是**這兩顆 leaf 的歸屬判斷**。
依 R-P15(b)，此二條之裁定即決定 §E 能否回到 64 / 24 / 16 / 7 / 3。

**執行層不就此提出任何建議歸屬。**

### 5.1 R-P16 之前提須複核（A-PW14）

R-P16 以「§1.8.1 實測 0 leaf 落點」為由刪除該章節。實測：

- `SWE-PM-057` 之章節集合含 **CFTS009 §1.8.1.1.1（`ID 1 Description`）**，
  出現 **3 次**，與 §1.6.2.1.17（3 次）、§1.6.3.1.1（3 次）**完全同票**。
- 「0 leaf 落點」只在 02 包之 tie-break（取最深）下成立 ——
  §1.6.2.1.17 深度 5 勝過 §1.8.1.1.1 深度 4。
- 換言之：**§1.8.1 有 leaf 觸及，只是在一條已被 R-P15 廢止的規則下未勝出。**

R-P16 之刪除已依指示套用於 §E，但**前提以刪除線與註記並存保留**，
待 Q1 裁定 `SWE-PM-057` 後回頭確認。若裁為 §1.8.1.1.1，R-P16 須撤回。

---

## 六、A-PW03 / A-PW04 / A-PW05 複驗結果（**上繳項三**）

座標：`SYS2 Traceability` r2–r34（33 列）、`Excluded NRLs (HW-only)` r2–r27（26 列）。

### A-PW03 —— **證據成立，且應加強**

| 宣稱 | 實測 | 判定 |
|---|---|---|
| 26 筆 | 26 列全非空 | 成立 |
| 全落 NRL-928xx–930xx | 號段 **92882 – 93063**，區間外 **0** 筆 | 成立 |
| 不含 `NRL-99476` | 確不在 26 筆之中 | 成立 |
| `NRL-99476` 為 `Sys-RA-PD_013`，HW | SYS2 CFTS010 實測：`ID`=`NRL-99476`、`Sys-RA-Feature-ID`=`Sys-RA-PD_013`、`SW/HW/System`=**`HW`**、`Document ID`=`CFTS010` | 成立 |

**應加強**：分頁名為 `Excluded NRLs (HW-only)`，但 26 筆之
`SW/HW/System` 欄實測為 `HW` **18** / `Information` **4** / `Out of Scope` **2** /
`Heading` **1** / 空白 **1**。即「(HW-only)」在**分類**上亦不實，
不僅是涵蓋範圍不足。原描述只指出後者。已於 ANOMALIES.md 補記。

### A-PW04 —— **逐字成立**

33 列全部儲存格串接後實測：`NRL-994xx` 出現 **0** 次、`Sys-RA-PD` 出現 **0** 次、
`Sys-RA-PM-` 出現 **76** 次。CFTS010 全域確未進追溯分頁。無須修正。

### A-PW05 —— **描述有誤，須修正**

| 宣稱 | 實測 | 判定 |
|---|---|---|
| `SWE1 Requirements` 用 `SWE-PM-001..115` | 115 筆連續 | 成立 |
| `SYS2 Traceability` 用 `SWE1-PM-TLM-001..033` | c1 實測 `SWE1-PM-TLM-001` … `SWE1-PM-TLM-033`，前綴分布 `{SWE1-PM-TLM-: 33}` | 成立 |
| `SYS2 Traceability` **亦用 `-ANT-`** | **33 列中含 `ANT` 者 0 筆**；`SWE1-PM-ANT-008` 於該分頁任一儲存格皆**不存在** | **不成立** |
| 兩套互不對應 | 該分頁 `SWE-PM-` 出現 **0** 次 | 成立 |

`SWE1-PM-ANT-` 命名空間之來源被誤植 —— 它只出現在 `SWE1 Requirements` 分頁
`SWE-PM-089` 之 `Source Requirement ID` 欄（即 A-PW01 所指者），
不在 `SYS2 Traceability`。**核心主張仍成立**，僅證據出處需訂正。
建議修正後描述已寫入 ANOMALIES.md。

---

## 七、B2 / B3（**上繳項一之二、之三**）

### B2 —— CFTS009 §1.6.2.1.17

| 項目 | 實測 |
|---|---|
| §1.6.2.1.17 標題 | **Proxi Parameters management**（`{4941690}`） |
| 父章節 §1.6.2.1 標題 | TLM algorithm requirements（`{4941353}`） |
| §1.6.2.1.15 標題（對照） | TLM_Status.Info and `$Telematic_Power$` signal setting（`{4941460}`） |
| §1.6.2.1.16 標題（對照） | Splash Screen logo visualization（`{4941664}`） |
| `SWE-PM-057` Requirement Title | **Proxi Parameter management** |
| `SWE-PM-057` Source Requirement ID | `Sys-RA-PM-0146` `0147` `0148` `0216` `0217` `0218` `0158`（7 個 token） |
| 其解析結果 | §1.6.2.1.17（3）、§1.6.3.1.1（3）、§1.8.1.1.1（3）——三方同票 |

`SWE-PM-057` Requirement Description（節錄）：

> The System UI shall read the PROXI parameter `Switch_Off_Time` using the
> interface provided by the hardware supplier and shall use the hardware
> supplier's interface to set the user-selected value to
> `SwitchOff_Timeout_Setting.Req`. …
> Case1 / Case2 / Case3：`SwitchOff_Timeout_setting.Req` 可選 00 / 20 / 60 / 180 min。

三個候選章節之標題（供裁定參考，非建議）：
§1.6.2.1.17 `Proxi Parameters management`、
§1.6.3.1.1 `SwitchOff_Timeout_Setting.Req management`、
§1.8.1.1.1 `ID 1 Description`。

§1.6.2.1.17 章節內文首段為 `4941691`：
「The value of the `Switch_Off_Time` parameter is defined by PROXI in TLM node」。

### B3 —— SYS3 SYSAD 章節結構（R-P20）

全文見 `features/power/data/sys3_chapters.md`。

**G16 = 0** —— §C rule 1 於本文件之匹配數為零。成因：SYS3 之標題**不含字面章節號**
（Word 自動編號），故無 `^\d+(\.\d+)* … \{id\}$` 可匹配，
且全篇無 `{polarion_id}` 後綴。**非序列化問題** —— 與 R-P17 之定義無關。

改以文件自身 heading style 取得結構（此為 B3 所要求之「章節號 + 標題 + pStyle」，
非調整正則）：**47 個 heading**，`Heading1` ×9、`Heading2` ×38。
章節號為依階層推導值，非文件內文字。

九個 Heading1：§1 目的 Purpose／§2 範圍 Scope／§3 縮寫與定義／
**§4 系統架構設計 System Architecture Design**／§5 接口說明 Interface Description／
§6 IVI Power Mode through Custom Vehicle Property／§7 Discrete Data Interface／
§8 參考文檔／§9 工具。

**§4.x 元件分解共 36 項**，其中與 Layer 2 邊界直接相關者：

- `系統分解 System Decomposition`、`架構設計組件 Architectural Design Components`、
  `分配系統需求 Allocate System Requirements`
- `動態行為 Dynamic Behavior` 及其七個狀態子節：
  **Sleep／Standby／Full Operation／Idle／Timed／Partial Operation／Bench**
- `Power States`、`Paramters`（原文拼字）、`Special Mode Parameters`、`Timers`
- `順序圖 Sequence Diagram` 及 `Start-Up sequence`／`Shutdown Sequence`／
  `Custom power state`／`Power State Transition`／`Power Mode Interruption Sequence`／
  `Phone Call`
- `Start-up Animation`、`Splash — Cold Boot`／`Warm Boot`／`Idle to Full Operation`
- `Antitheft`、`Front Panel On Off Sequence`、`Disclaimer`、`Assumptions`

**依 B3 禁區，未據此調整 §E 之任何分組。** 僅登記素材。

---

## 八、G14 次章節涵蓋（R-P22）—— 結果嚴重

被丟棄之相異次章節 **10** 個；其中僅 **1** 個被其他 leaf 之主章節覆蓋。
**9 個未被任何 leaf 之主章節覆蓋** —— 在現行主章節作法下，這 9 章不產生任何 TC：

| 章節 | 標題 | 來自 leaf |
|---|---|---|
| CFTS009 §1.6.2.1 | TLM algorithm requirements | `SWE-PM-001`–`009`（9 條） |
| CFTS009 §1.6.2.1.4 | **Stolen Vehicle Mode** | `SWE-PM-003` |
| CFTS009 §1.6.2.1.9 | **Logistic Idle** | `SWE-PM-008` |
| CFTS009 §1.6.2.1.10 | **Logistic Standby** | `SWE-PM-008` |
| CFTS009 §1.6.2.1.11 | **Logistic Sleep** | `SWE-PM-008` |
| CFTS009 §1.6.2.1.14 | TLM modules and functionalities depending on operative state | `SWE-PM-001`–`009`（9 條） |
| CFTS009 §1.6.2.1.15.1 | **ICS Wakeup Reasons by POWER Button Pressed** | `SWE-PM-004` |
| CFTS009 §1.6.3.1.1 | SwitchOff_Timeout_Setting.Req management | `SWE-PM-057` |
| CFTS009 §1.8.1.1.1 | ID 1 Description | `SWE-PM-057` |

主章節相異數 37；連同被丟棄者，全部出現過之相異章節 46。
即 **114 個 leaf 觸及 46 個章節，但只有 37 個進入 Layer 3**。

粗體五項為實質功能章節（防盜模式、三個 Logistic 狀態、POWER 鍵喚醒原因），
不是標題殼。**Layer 3 之涵蓋宣稱在這 9 章上不成立。** 登記為 **A-PW16**。

R-P22 設此閘的判斷是對的 —— 若無此閘，這 9 章會在整個 Phase 4 靜默消失。

---

## 九、獨立判斷：本包是否仍有該驗而未驗者（**上繳項四**）

02 上繳包 §七之六項，本包處置如下：第 1 項→R-P15（B1 已備妥，待裁）；
第 2 項→R-P22（G14 已驗，查出 9 章缺口）；第 3 項→R-P18（G6a/G6b 已拆已驗）；
第 4 項→R-P23（（d）欄已填，跨機器仍未驗，屬工具本身限制）；
第 5 項→R-P20（SYS3 已讀）；第 6 項→R-P21（兩分頁已驗，一條 anomaly 描述有誤）。
**六項全部落地。**

**以下為執行層自判之新增未驗項，共六項。**

### 1.（最重）「章節」作為 Layer 3 之單位，其粒度從未被檢視

G14 揭露 114 個 leaf 觸及 46 個章節。但 §四之結構事實顯示：
`§1.6.2.1`（父）與 `§1.6.2.1.14` 被**九個** leaf 同時命中 ——
它們不是任何 leaf 的特徵，而是共同背景。
反之 `§1.6.2.1.9/.10/.11`（三個 Logistic 狀態）只被 `SWE-PM-008` 一條命中，
卻是三個彼此獨立的功能。

**「一個 leaf 對一個章節」這個假設本身未經驗證。**
現行結構同時存在「多 leaf 對一章節」與「一 leaf 對多章節」，
而 §E 的 Layer 3 只能表達前者。R-P15 解決的是「怎麼挑一個」，
未觸及「是否應該只挑一個」。**若 `SWE-PM-008` 實際涵蓋
Logistic Idle / Standby / Sleep 三個狀態，它在 Phase 4 應產生三組 TC 還是一組？
此問題無任何條文、無任何閘。**

### 2. Layer 3 之反向完整性未驗：CFTS 本文有多少章節從未被任何 leaf 觸及

已驗的是「leaf 觸及哪些章節」（46 個）。未驗的是反向：
CFTS009 有 **196** 個章節、CFTS010 有 **92** 個，合計 288。
被觸及的 46 個佔 **16%**。其餘 242 個章節之中，
有多少是本 feature 應涵蓋而未涵蓋？
R-P7 已裁定「不追 SYS2 反向缺口」，但那指的是**需求**層；
**章節層的反向缺口不在 R-P7 的射程內，且從未量測。**
G14 只查了「被丟棄的次章節」，沒查「從未出現過的章節」。

### 3. A-PW06（`Sub Categorization` 詞彙漂移）仍未複驗

R-P21 補驗了 A-PW03 / A-PW04 / A-PW05 三條，但 A-PW06 同樣是 01 包時期
的宣稱（`HMI` 36 / `Service\nHMI` 35 / `Service` 27 / `HMI Service` 16 /
`HMI/Service` 1，合計 115），同樣從未由執行層複驗。
它宣稱「不可作分批判準」—— 而分批規劃就在 DECISIONS.md §7，即將用到。
**本包漏掉它，因為 R-P21 只點名了三條。**

### 4. B1 之 Requirement Title 欄有空值，未列入任何閘

§四表中 #3–#9 七條之 `Requirement Title` 為空。
G1 只驗 `SWE-Requirement ID` 非空，G2 只驗 `Categorization`。
**037 其餘 16 個欄位的空值率從未量測**，而 `Requirement Title` 正是
§E「本分組之已知弱點」所依賴的欄位（該節稱其「出現 20+ 種」）。
若七條為空，那個「20+ 種」的統計基礎也需重算。

### 5. §C rule 3 之字面文字與實測不符，本包選擇不擴張，但未閉合

A-PW15：SYS2 之 `Source Requirement items` 欄有 81 個 token 是章節錨點 id，
而 §C rule 3 稱該欄「即為上述 id」（rule 2 之需求錨點 id）。
本包已驗兩種讀法對 G3 與跨章節 leaf 名單無影響，故未擴張。
**但「目前無影響」不等於「日後無影響」** —— Phase 4 產生
`specification_reference` 時，這 81 個 token 指向章節而非需求，
引用格式會不同。此處未設閘。

### 6. SYS3 SYSAD 已讀，但其與 §E 的關係仍完全未驗

R-P20 的理由是「§4.x 為目前唯一可能提供**獨立**分組來源之文件」。
本包依 B3 禁區只取得素材，**未做任何比對**。
於是 §E 的「不是交集、只由單一來源支撐」這個 02 包登記的弱點，
在本包結束時**仍然成立** —— 素材有了，交叉驗證還沒做。
B3 的禁區是對的（避免執行層搶裁），但它也意味著
**R-P20 所要解決的問題，在 04 包之前不會被解決**。
建議 04 包明確安排這項比對，否則 R-P20 只完成了一半。

---

## 十、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | 僅 `read_only=True` 開啟，未寫入 |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | G3 = 114/115，該 leaf 留空 |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重新產生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改。SYS3 之 G16 = 0 係如實回報，未為求匹配而改動；B3 之章節清單另以 heading style 取得，並已明示章節號為推導值 |
| **不得以任何演算法指派跨章節 leaf 之主章節（R-P15(b)）** | B1 未做任何指派。`verify_gates_03.py` 內之主章節計算**僅用於 G14 之次章節判定與 B1 之「02 包所採規則指派之結果」歷史紀錄欄**，未產生任何新的 §E 數字 |
| **不得於 B1 附上建議歸屬** | `multi_chapter_leaves.md` 全檔無任何建議。§五之算術閉合與 §4.1 之結構事實為實測陳述，均未指出應歸何處 |
| 不得據 SYS3 SYSAD 自行調整 §E 分組 | B3 僅列章節清單，未與 §E 做任何比對或調整 |
| 不得重算或改寫 §E | §E 之 64/24/16/7/3 未動。**惟須揭露**：`verify_gates.py`（02 包腳本）仍含 §E 重算段，本包執行過程中曾執行，輸出與 02 包完全相同，未據以修改 §E 任何數字。03 版之 `verify_gates_03.py` 已移除該段 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材；`inputs/` 仍為 02 包之七份 |

### §E 之異動（依 03 §E 指示，非重算）

套用於 `docs/handoff/01_intake.md` §E（§E 實體所在處）：
標題「已定版」→「**待定版 —— 依 R-P15(b) 逐條裁定後於 04 包定版**」；
Power State 之 Layer 3 章節清單中 `§1.8.1` 加刪除線（R-P16）；
「已定版，無待裁項」加刪除線並附 03 包異動註記。
**leaf 分布數字一字未動。**

---

## 十一、待裁

- **Q1（阻斷 framework）11 條跨章節 leaf 之歸屬**（R-P15(b)）。
  素材：`data/multi_chapter_leaves.md`。
  **實務上只有 `SWE-PM-008` 與 `SWE-PM-057` 兩條會改變 Test Set 分布**（§五）；
  其餘九條之裁定影響 Layer 3 章節指向，不影響數字。
- **Q2 `SWE-PM-057` 裁定後，R-P16（刪除 §1.8.1）是否撤回**（A-PW14）。
- **Q3 A-PW05 描述訂正是否採納**（§六）；A-PW03 是否加註分類不實。
- **Q4 A-PW16 之 9 個未覆蓋章節如何處置** —— 併入既有 Test Set、
  另立 Test Set、或明示不涵蓋並登記理由。此項直接決定 Layer 3 是否完整。
- **Q5 §九第 1 項：一個 leaf 是否得對應多個 Layer 3 章節**（現行結構不支援）。
- **Q6 §九第 2 項：是否量測章節層之反向缺口**（288 章中僅 46 章被觸及）。
- **Q7 §九第 3 項：A-PW06 是否補驗**（分批規劃即將用到）。
- **Q8 §九第 6 項：04 包是否安排 SYS3 §4.x 與 §E 之交叉比對**（R-P20 之後半）。
