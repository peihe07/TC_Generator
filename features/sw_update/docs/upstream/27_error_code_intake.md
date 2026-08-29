# 上繳包 27 —— T42 執行結果（下放包 29，Error Code List intake 線）

- 日期：2026-08-28｜方向：執行層 → 分析層
- 對應下放包：`docs/handoff/29_error_code_intake.md`
- 並行線：T41（下放包 28）之結果在 `26_cross_check.md`
- **⚠ 二項須先裁**：見 §0

---

## 0. ⚠ 落檔驗證 —— 下放包 29 之二項不符

### 0.1 **R-SU35(a) 之階段對照表漏兩個階段，5 碼無落點**

`Error Code List` 分頁實測 **10 個階段標題**，§1.3 之階段鏈只列 7 個：

| 階段（實測，逐字） | 碼數 | R-SU35(a) |
|---|---:|---|
| `After HU start-up, suddenly` | **4** | **無** |
| `Precondition` | 7 | `USB Update` |
| `Package Header check & unpack` | 13 | `Integrity Verification` |
| `Rollback Protection *This function supports only user build.` | 3 | `Update Agent` |
| `Security check` | 4 | `Integrity Verification` |
| `Install ( M-CPU )` | 6 | `Interruption Handling`／`Update Agent` |
| `Install ( M-CPU: Redbend ) Note: These error code is not defined by melco` | 1 | 同上 |
| `Install ( V-CPU )` | 24 | 同上 |
| `Install ( SXM )` | 17 | 不用（非本 feature 範圍） |
| `RedBend update engine` | **1** | **無** |

**`After HU start-up, suddenly` 不是表首說明，它是帶 4 個碼之階段標題**
（`327680`／`393216`／`393217`／`393219`）。加上 `RedBend update engine` 之 1 碼，
**共 5 碼在對照表中無落點**。

**執行層不推定其歸屬** —— 依 **R-SU20(d)**，「階段名與組名字面相近」是循環，
不是依據。台帳該欄填 `—（R-SU35(a) 未載）`，待分析層補裁。

> 此事恰為 §五-6 所問之具體案例：**若我用字面填了，那正是 R-SU20(d) 所禁者。**

### 0.2 **T42b 之分頁預判漏兩頁**

預判為「`Error Code List` + 6 頁台架記錄」= 7 頁，實測 **9 頁**。
`Model Code`（47 列）與 `Issue Mapping Version`（2 列）不在預判內 ——
已逐頁陳報（§2），不阻斷。

---

## 1. T42a —— intake

| 項 | 值 |
|---|---|
| 落點 | `features/sw_update/inputs/Error_Code_List.xlsx` |
| sha256 | `4625753cdf90a6b0788e8da32448e8e6aef4ee987b6966bb9934f2ab49451aad` |
| 與 `forms/` 原件 | **位元相同** ✅ |
| 尺寸 | 56,234 bytes｜**9 分頁** |
| `feature.yaml` | `paths.error_code_list` + `reference.error_code_list`（含 sha256） |

## 2. T42b —— `Error_Code_List.xlsx` 欄位全覽（R-SU26(a)）

- 來源：`inputs/Error_Code_List.xlsx`｜sha256 `4625753c…`｜**9 分頁**
- **用途標記一律為陳報（`未定（本輪陳報）`），不是裁定** —— R-SU26(b) 由分析層裁

| # | 分頁 | 非空列 | 欄數 | 標頭（欄序） | 用途（陳報） |
|---:|---|---:|---:|---|---|
| 1 | `ProvideSW_final` | 129 | 10 | `Gen`／`SR`／`Carline`／`Vehicle type`／`SW version`／`Date` | 疑為台架作業記錄（下放包 29 T42b 之預判） |
| 2 | `Model Code` | 44 | 2 | `Model Code`／`Model Name` | **⚠ 不在下放包 29 T42b 之預判清單內** |
| 3 | `Flash Status` | 51 | 13 | `Gen`／`Radio Version`／`Dev/Release key`／`Secure/NonSecure`／`VCPU Version`／`Status` | 疑為台架作業記錄（同上） |
| 4 | `Error Code List` | 92 | 5 | `Error Code`／`Description`／`Root cause`／`Recovery`／`Contact to .. 1 > 2 > ...` | **已用** —— R-SU35：負向路徑之錯誤碼定義 |
| 5 | `Issue Mapping Version` | 2 | 1 | `https://shiftup.sharepoint.com/:x:/r/sites/R1LProject/_layouts/15/Doc.aspx?sourcedoc=%7B1D6A101D-2AAC-4EEB-9EB7-8D458C686F91%7D&file=R1L_GIMs_HighMedium_Apr2024_Jalen.xlsx&action=default&mobileredirect=true` | **⚠ 不在下放包 29 T42b 之預判清單內** |
| 6 | `R1L_Need_Machine` | 40 | 4 | `Gen`／`Vehicle type`／`Architecture (V-CPU SVN Repository)`／`Exist` | 疑為台架作業記錄（同上） |
| 7 | `Flash Record` | 11 | 17 | `Gen`／`MCPU Version`／`Key`／`Secure/NonSecure`／`VCPU Version`／`Parameter` | 疑為台架作業記錄（同上） |
| 8 | `MD_IMAGE` | 23 | 8 | `Gen`／`Version`／`Vehicle type`／`Architecture (V-CPU SVN Repository)`／`FTP Image Path`／`Purpose` | 疑為台架作業記錄（同上） |
| 9 | `PROD_Parameter_Compare` | 12 | 11 | `Prod Parameter`／`GEN1 Melco`／`GEN2 Melco`／`GEN3 Melco`／`GEN4 Melco`／`GEN5 Melco` | 疑為台架作業記錄（同上） |

### 逐頁之值型態摘要（**含實例** —— PLAYBOOK (29)）


#### `ProvideSW_final`（非空 129 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Gen` | 128 | 5 | 枚舉 | `Gen1` |
| 1 | `SR` | 128 | 4 | 枚舉 | `SR21` |
| 2 | `Carline` | 128 | 4 | 枚舉 | `LATAM` |
| 3 | `Vehicle type` | 128 | 42 | 自由文字 | `281(Strada) 226(Toro)` |
| 4 | `SW version` | 128 | 103 | 自由文字 | `R6.26.00.00` |
| 5 | `Date` | 127 | 44 | 自由文字 | `2020/Jan` |
| 6 | `Comment` | 127 | 36 | 自由文字 | `2020/Jan SOP` |
| 7 | `Architecture (V-CPU SVN Repository)` | 128 | 8 | 自由文字 | `281:Atl-Lo 226:Atl-Mi` |
| 8 | `V-CPU SVN Branch (version information is included in branch name)` | 128 | 65 | 自由文字 | `281-NonSec:REL/BRC_R1L_R6_26_VCPU_200402A102 281-Sec:REL…` |
| 9 | `Verify Target Version` | 8 | 1 | **常數欄** | `O` |

#### `Model Code`（非空 44 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Model Code` | 43 | 43 | 自由文字 | `B1` |
| 1 | `Model Name` | 41 | 41 | 自由文字 | `B1 - Jeep Renegade (Brazil)` |

#### `Flash Status`（非空 51 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Gen` | 50 | 5 | 枚舉 | `Gen1` |
| 1 | `Radio Version` | 50 | 26 | 自由文字 | `R6.80.00.00` |
| 2 | `Dev/Release key` | 50 | 2 | 枚舉 | `Dev` |
| 3 | `Secure/NonSecure` | 50 | 2 | 枚舉 | `NonSecure` |
| 4 | `VCPU Version` | 50 | 7 | 自由文字 | `Melco Precompiled` |
| 5 | `Status` | 50 | 7 | 自由文字 | `Pending` |
| 6 | `Error Code` | 9 | 3 | 枚舉 | `262147` |
| 7 | `Error Message` | 12 | 6 | 枚舉 | `Didn't detect usb update file. It opened e-fuse.` |
| 8 | `Propose` | 49 | 12 | 自由文字 | `Verify Radio image build by MD` |
| 9 | `Note` | 26 | 11 | 自由文字 | `Pending By right architecture machine` |
| 10 | `Machine Label` | 46 | 8 | 自由文字 | `STLA CN` |
| 11 | `Verify Target Version` | 16 | 1 | **常數欄** | `O` |
| 12 | `Done Date` | 17 | 11 | 自由文字 | `2025-01-09 00:00:00` |

#### `Error Code List`（非空 92 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Error Code` | 90 | 89 | 自由文字 | `After HU start-up, suddenly` |
| 1 | `Description` | 81 | 66 | 自由文字 | `General VCPU FW update error` |
| 2 | `Root cause` | 81 | 45 | 自由文字 | `In most cases it is triggered when no response received …` |
| 3 | `Recovery` | 77 | 11 | 自由文字 | `Most likely such behavior is caused by corrupted or inco…` |
| 4 | `Contact to .. 1 > 2 > ...` | 80 | 11 | 自由文字 | `Self Check SWDL team` |

#### `Issue Mapping Version`（非空 2 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `https://shiftup.sharepoint.com/:x:/r/sites/R1LProject/_layouts/15/Doc.aspx?sourcedoc=%7B1D6A101D-2AAC-4EEB-9EB7-8D458C686F91%7D&file=R1L_GIMs_HighMedium_Apr2024_Jalen.xlsx&action=default&mobileredirect=true` | 1 | 1 | **常數欄** | `https://shiftup.sharepoint.com/sites/R1LProject/_layouts…` |

#### `R1L_Need_Machine`（非空 40 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Gen` | 39 | 5 | 枚舉 | `Gen1` |
| 1 | `Vehicle type` | 39 | 35 | 自由文字 | `281(Strada)` |
| 2 | `Architecture (V-CPU SVN Repository)` | 39 | 8 | 自由文字 | `281:Atl-Lo` |
| 3 | `Exist` | 4 | 1 | **常數欄** | `✔` |

#### `Flash Record`（非空 11 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Gen` | 9 | 5 | 枚舉 | `Gen1` |
| 1 | `MCPU Version` | 9 | 7 | 自由文字 | `R6.62.00.00` |
| 2 | `Key` | 9 | 2 | 枚舉 | `Dev` |
| 3 | `Secure/NonSecure` | 9 | 2 | 枚舉 | `NonSecure` |
| 4 | `VCPU Version` | 9 | 7 | 自由文字 | `R6_60_VCPU_210800A201` |
| 5 | `Parameter` | 3 | 2 | 枚舉 | `Sign Release` |
| 6 | `(無標頭)` | 2 | 2 | 枚舉 | `Secure Boot` |
| 7 | `(無標頭)` | 10 | 3 | 枚舉 | `Variant` |
| 8 | `(無標頭)` | 10 | 3 | 枚舉 | `Format Version` |
| 9 | `Status` | 9 | 3 | 枚舉 | `Failed` |
| 10 | `Note` | 9 | 9 | 自由文字 | `02/06 : Didn't detect usb update file. It opened e-fuse.` |

#### `MD_IMAGE`（非空 23 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Gen` | 22 | 5 | 枚舉 | `Gen1` |
| 1 | `Version` | 22 | 18 | 自由文字 | `R6.62.00.00` |
| 2 | `Vehicle type` | 22 | 17 | 自由文字 | `281(Strada)` |
| 3 | `Architecture (V-CPU SVN Repository)` | 22 | 7 | 自由文字 | `Atl-Lo` |
| 4 | `FTP Image Path` | 22 | 22 | 自由文字 | `Dev: /mobiledrivetech/PROJECT/R1L/IMAGE/DEV_BUILD/00.06.…` |
| 5 | `Purpose` | 22 | 4 | 枚舉 | `Flash pending` |
| 6 | `Status` | 2 | 1 | **常數欄** | `O` |

#### `PROD_Parameter_Compare`（非空 12 列）

| 欄 | 標頭 | 非空 | unique | 型態 | **實例（首個非空值）** |
|---:|---|---:|---:|---|---|
| 0 | `Prod Parameter` | 11 | 11 | 自由文字 | `BUILD_GL_TEST_TOOLS` |
| 1 | `GEN1 Melco` | 11 | 1 | **常數欄** | `X` |
| 2 | `GEN2 Melco` | 11 | 3 | 枚舉 | `True` |
| 3 | `GEN3 Melco` | 11 | 3 | 枚舉 | `True` |
| 4 | `GEN4 Melco` | 11 | 2 | 枚舉 | `False` |
| 5 | `GEN5 Melco` | 11 | 2 | 枚舉 | `False` |
| 6 | `GEN1 MD` | 11 | 1 | **常數欄** | `X` |
| 7 | `GEN2 MD` | 11 | 3 | 枚舉 | `True` |
| 8 | `GEN3 MD` | 11 | 3 | 枚舉 | `True` |
| 9 | `GEN4 MD` | 11 | 2 | 枚舉 | `False` |
| 10 | `GEN5 MD` | 11 | 2 | 枚舉 | `False` |

---

## 3. T42c —— `ERROR_CODES.md` 產出

- 碼數 **80**｜階段 **10**｜閉合檢查 **✅**（台帳 80 = 分頁 80）
- 平台限定 `*Not support at GEN1`：**4 碼**
- `Not an actual error`：**2 碼**

### ⚠ R-SU35(a) 未涵蓋之階段（**2** 個，共 5 碼）

- `After HU start-up, suddenly` —— 4 碼
- `RedBend update engine` —— 1 碼

**執行層不推定其歸屬**（R-SU20(d)：字面相近是循環，不是依據）。

`ERROR_CODES.md` 已產出（145 行，80 碼逐碼）。**閉合檢查為 `sys.exit` 型**
（PLAYBOOK (31)：不報錯的空結果之防線只有閉合檢查）——
台帳碼數 ≠ 分頁碼數即停，不輸出半份台帳。

台帳所載之引用拘束（自 R-SU35 抄）：碼值 verbatim、
`specification_reference` 不列本表、讀碼位置未定前掛 `PENDING: DR-SU2`、
平台限定須連同記、`458760`／`458763` 不作失敗判準、正向路徑不因本表而有觀測面。

> **一項執行層另記之事實**：`335890` 之 Description 原文為
> `Download not possible - last sessiion interrupted` —— **`sessiion` 為拼寫殘留**。
> R-SU35(b)1 令碼值與描述 verbatim，故台帳照抄未改正（同 D-4 之處置），
> 並於台帳檔首明記此點。**本表非 037，不入 `DESCRIPTION_DEFECTS.md`。**

---

## 4. T42d —— 台帳更新

### 4.1 `SOURCE_COLUMNS.md`

- **新增「已查・不用之來源」節**（R-SU26(d)：「掃了沒命中」與「沒掃到」須可分辨），
  登記診斷側三源之規模與 0 命中。
- **`Error_Code_List.xlsx` 入統計表**，標記為**陳報中**，
  其 9 分頁之用途本輪一律 `未定（本輪陳報）`，**不計入未定數** ——
  R-SU26(b) 之「不得跨輪留存」自其被裁定之輪次起算，**下一輪必裁**。
- **036 `C` 欄理由句更新**：依據由「無取值路徑」升級為
  **「Pei 確認不需填（2026-08-28）」**，「日後要填須新 DR」之但書**撤銷**；
  「不得以推定值填入」一句**維持有效**（其射程為「若有人日後想填」）。

### 4.2 ⚠ 執行層之覆核範圍（**須明記**）

| 來源 | 主張 | 執行層可覆核？ |
|---|---|:--:|
| `forms/DTCs Matrix Core List Rev. 1.6.xlsx` | 0 命中 | **✅ 已實測覆核** |
| `CFTS_004` + SYSAD | 0 命中 | ❌ **不在 repo** |
| `SWE1_Diagnostics_V1.xlsx` | 0 命中 | ❌ **不在 repo** |

**已覆核者**：以 `FOTA|OTA|CFTS057|software update|SW update` 正則掃全簿全頁 ——
**0 命中，主張成立**。（另記：§1.2 記其為 6 分頁，實測 **7**，多一頁僅 1 列之
`Sheet1`；不影響結論。）

**未覆核者**：後二源之素材由 Pei 上傳至分析層側，此側無跡證。
而下放包 29 §二將該表列為 DR 附件並稱「**可覆核**」——
**對上游可覆核，對本 repo 不可**。DR 發出前宜將該二份原件或其掃描輸出一併落檔。

### 4.3 `framework.md`

**T42d(iii) 令「DR 註記同步」—— 本檔原無任何 DR 註記**（全檔 `DR-SU` 命中 0）。
故新增「**觀測面來源之覆蓋**」一節，記各 Test Set 因本表而有之**負向路徑**來源，
並隨表載三項拘束（USB／SWDL 限定、讀碼位置未定、**本表不得回頭改 Layer 2 切分**
—— 後者即 R-SU20(d) 之循環）。

### 4.4 `DATA_REQUESTS.md` —— 二線併寫

T41d(ii)（三段式）與 T42f（v2 縮編）**改的是同一節**，故併寫：

| 段 | 內容 | 現況 |
|---|---|---|
| (a) 已確認・第二型 | 無外部後果 → 求**觀測手段** | **5 列**（`363`–`367`） |
| (b) 未確認之母群 | 語形 ∪ 人裁 —— **僅對第二型有意義** | **106 列** |
| (c) 已確認・第三型 | 不可區辨／限定詞不可量 → 求**區辨手段** | **2 列**（`179`／`181`） |

**(c) 段無上界可報** —— 第三型之母群未經盤點，且不可由語形估計（`181` 為證）。
**106 是第二型之上界，不是全體之上界。**

DR-SU2 v2 之縮編全文逐字入檔，並附診斷側三源之舉證表（含 §4.2 之覆核狀態）。
母群沿革表增一列，記本輪三個成因。

---

## 5. 未結 DR 清單（**2 筆**，二線併計）

| DR | 標的 | 狀態 | 進度 |
|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | **OPEN**｜High | `176` facet B；`newR1L-SU-003` 三個 PENDING |
| **DR-SU2 v2** | (a) Error Code 之**顯示途徑**／(b) Wi-Fi session 之**正向狀態**觀測／(c) **第三型之區辨手段** | **OPEN**｜High | 第二型 **5 / 106**；**第三型 2 列（母群未知）** |

**已不再請求**：「106 列全部之觀測手段」—— 其負向半由 `Error_Code_List.xlsx` 覆蓋（R-SU35）。
**縮編不是撤銷。**

**PENDING 總計 5 行**（`newR1L-SU-009` 3 + `newR1L-SU-010` 2），
另 pilot 之 `newR1L-SU-003` 3 行屬 DR-SU1。

---

## 6. T42e —— DR 文本

`docs/upstream_requests/DR-SU1_SU2_request.md`（138 行，**英文，可直接轉發**）。

結構：背景一段 → DR-SU1 → DR-SU2 v2 三項 → **§4 舉證（診斷側三源窮舉）**
→ 附件清單 → §6 一頁摘要表。

**三處刻意之措辭**：

1. §3.1 明寫 **"This request is therefore reduced, not withdrawn."** ——
   縮編易被上游讀成「他們自己解決了」。
2. §3.3 明寫 106 為 **"an upper bound on this category, not a count of confirmed cases"**，
   §3.4 另立 **"Note on scope"** 說明 `181` 不在該 106 內 ——
   即 R-SU32 v2(e) 之正交，用上游讀得懂的話寫。
3. §3.4 明寫 **"We are not merging requirements on our own initiative."** ——
   R-SU32(d) 之對外表述。

**發送者為 Pei（Tier 3），執行層只落檔，未發送。**

---

## 7. T42f —— 抄錄與索引

| 條文 | 逐字相符 |
|---|:--:|
| `R-SU35（Error_Code_List 之地位與引用方式）` | **True** |

**索引以現場為準**（T42f 之明令）：抄錄前實測 32 條 →
補 R-SU32 v2（版本升級，不佔列）→ +R-SU33／R-SU34（T41e）→ +R-SU35 =
**35 條現行**、**19 條留存**，`R-SU1` – `R-SU35` 無缺號無重複。
與 T42f 之推算（34 → 35）相符。

---

## 8. 獨立自評 —— §五-6 所問：`Test Set 候選`欄以什麼依據填而不落入 R-SU20(d) 之循環

**答：本輪之依據是「R-SU35(a) 抄錄」，而它之所以不循環，是因為那張表不是我做的。**

**(甲) 循環長什麼樣。** R-SU20(d) 禁的是：以「標題關鍵詞與組名相符」作為歸屬依據。
在本任務中它會長成：看到階段名 `Package Header check & unpack`，
看到 Test Set `Integrity Verification`，覺得「都是在講檢查」，於是填上去。
**那不是依據，那是同義詞查詢。**

**(乙) 本輪之實作。** `scripts/error_codes.py` 之 `STAGE_MAP` 是
**R-SU35(a) 之逐字抄錄**，且比對用**前綴**（因分頁之階段標題帶尾註）。
**條文未載之階段一律填 `—（R-SU35(a) 未載）`** ——
於是 §0.1 之 5 碼變成一個**顯式的洞**，而不是一個看起來填好了的欄位。

**這就是不循環之處**：我沒有判斷任何一個階段屬於哪個組，
**我只是把分析層已裁之對照套上去，套不上的就報出來。**

**(丙) 但這只是把循環往上推了一層，沒有消滅它。**
R-SU35(a) 那張表本身**是怎麼定的**？下放包 29 未載其依據。
若它也是照字面對的，**則循環仍在，只是發生在分析層而非執行層**，
而我這一層無從分辨 —— 我看到的只是一張表。

**故本欄之真正保證只有一句**：**它與台帳中任何實測數字無關。**
碼數、階段數、平台限定數皆為實測；**`Test Set 候選`欄是引用**，
**且台帳已標明其為「候選非裁定」**（下放包 29 T42c 之明文）。
**讀者不會把它當實測讀。**

**(丁) 若要真正解除循環**，該欄之依據應為
**「該階段之錯誤碼所描述之失敗，落在哪個 Test Set 之測試範圍內」** ——
即從碼之 Description 讀出其失敗情境，再對照該 Test Set 所轄之 037 列。
**那是逐碼之工作（80 碼），且需要 037 側之對照**，本輪未做，亦未被要求。
**現行之階段級對照是一個粗粒度之代理，其粒度差異須隨表陳述。**

---

## 9. 待裁事項

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **R-SU35(a) 補兩階段之落點**（`After HU start-up, suddenly` 4 碼、`RedBend update engine` 1 碼） | §0.1 |
| 2 | **`CFTS_004`／`SWE1_Diagnostics_V1.xlsx` 是否入 repo** —— 否則 DR 附件三分之二無跡證 | §4.2 |
| 3 | `Error_Code_List.xlsx` 9 分頁之用途裁定（本輪陳報，下輪必裁） | §2 |
| 4 | **`Test Set 候選`欄是否升級為逐碼依據**（現為階段級代理） | §8(丁) |
| 5 | DR 文本是否照發（發送者為 Pei） | §6 |
