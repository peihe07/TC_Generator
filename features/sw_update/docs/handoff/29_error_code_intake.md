# 下放包 29 —— Pei 二裁之落地（Error Code List 可用、C 欄不填）、R-SU35、DR-SU2 縮編

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`28_cross_check.md`（T41 未回收，**本包與之並行，不取代**）
- 對應上繳：`docs/upstream/27_error_code_intake.md`
- 裁定狀態：**Pei 2026-08-28 二裁**（見 §一）；R-SU35 —— 分析層即裁

---

## 一、Pei 之裁定（二項，2026-08-28）

### 1.1 `C` 欄（Polarion）—— **確認不需填**

下放包 26 §2.1 之「留空」裁定，其依據由「無取值路徑」**升級為
「Pei 確認不需填」**。台帳之理由句更新（T42d），
「日後要填須新 DR」之但書**撤銷** —— 不需填即無日後之填。

### 1.2 `forms/DTCs Matrix Core List Rev. 1.6.xlsx` 等三源之查證 —— 診斷側窮舉完畢

Pei 指示查證三份診斷側文件，分析層直接實測（本次由分析層親測，
非經執行層 —— 素材由 Pei 上傳至分析層側）：

| 來源 | 規模 | FOTA／OTA／SW-update 觀測定義 |
|---|---|---:|
| `DTCs Matrix Core List Rev. 1.6.xlsx`（6 分頁） | 254 筆 DTC | **0**（Lead CFTS 無 CFTS057） |
| `CFTS_004 General Diagnostic Requirements`（Jun 2026）+ SYSAD | 554 物件／168 DID／112 routine | **0**（`FOTA` 僅見於 SYSAD 縮寫表；`OTA` 僅 SXM 換包 NRC） |
| `SWE1_Diagnostics_V1.xlsx`（037 A03，395 列） | 395 需求列 | **0**（唯一命中為 buzzer 列之偽陽性） |

**診斷側之窮舉完畢**（PLAYBOOK (26)）。此三筆為 DR-SU2 之舉證材料。

### 1.3 `Error_Code_List.xlsx` —— **Pei 裁：可用**（作 TC 引用來源）

其為軟體更新流程之分階段錯誤碼清單（9 分頁；核心分頁約 70+ 碼，
含 Description／Root cause／Recovery／Contact 欄），
階段：Precondition → Package Header check & unpack → Rollback Protection →
Security check → Install M-CPU（update_engine／Redbend）→
Install V-CPU（SWDL）→ Install SXM。

**此為本 feature 首個「負向路徑之觀測面」來源** —— 詳 §三 R-SU35。

---

## 二、對 DR-SU2 之影響 —— 縮編（不撤銷）

Error Code List 解掉的是**負向路徑**（失敗／中斷／拒絕之情形有碼可觀測）。
未解者三項，DR-SU2 據此縮編：

```
DR-SU2 v2（縮編，2026-08-28）：

(a) Error Code 之顯示途徑確認 —— 錯誤碼於 HU 上如何呈現
    （開機後畫面？彈窗？工程模式頁？）。Error_Code_List 表首
    「After HU start-up, suddenly…」暗示畫面顯示，但未明載途徑。
(b) Wi-Fi FOTA session 之正向狀態觀測 —— Error Code List 覆蓋
    USB／SWDL 路徑之失敗面；Wi-Fi 路徑之進行中狀態
    （session 建立、下載中、DD 解析）仍無觀測定義。
(c) 第三型之區辨手段 —— `179`（下載請求 vs 背景執行）、
    `181`（下載完成時點）。不變。

已不再請求者：「106 列全部之觀測手段」—— 其負向半已由
Error_Code_List 覆蓋（R-SU35）。

舉證附件：診斷側三源窮舉（§1.2 之表，含版本號與筆數，可覆核）。
```

**DR 文本由分析層備妥、Pei 發**（Tier 3 為 DR sender）。T42e 更新台帳。

---

## 三、R-SU35（新條，抄入 RULINGS.md，逐字）

```
R-SU35（Error_Code_List 之地位與引用方式）

Pei 裁（2026-08-28）：`Error_Code_List.xlsx` **可用**作 TC 之引用來源。

(a) **地位**：軟體更新流程各階段之錯誤碼定義，為
    **負向路徑（失敗／中斷／拒絕）之觀測面來源**。
    其分階段結構與 Test Set 之對應：
      Precondition／USB 檢查      → `USB Update`
      Package Header／unpack      → `Integrity Verification`
      Rollback Protection          → `Update Agent`
      Security check               → `Integrity Verification`
      Install M-CPU／V-CPU        → `Interruption Handling`／`Update Agent`
      Install SXM                  → （非本 feature 範圍，不用）

(b) **引用方式**：
    1. ER 得寫「對應之 error code 被報告」並具體列碼
       （如 `error code 335890 is reported`）；
       **碼值 verbatim 取自本表，不得自造或改寫**。
    2. `specification_reference` **不列本表** —— 錨仍走 CFTS057
       （R-SU4 v2 不變）；本表之引用記於 `reasoning`，
       格式 `Error_Code_List.xlsx <分頁> <碼>`。
    3. 觀測步驟之「在哪裡讀到該碼」**依 DR-SU2 v2(a) 之答案而定**；
       未答前，該讀取步驟掛 `PENDING: DR-SU2` ——
       **碼有了，看碼的地方還沒有**，二者不得混同。

(c) **範圍拘束**：
    1. 本表為 **USB／SWDL 路徑**之錯誤碼；
       **不得引用以充當 Wi-Fi FOTA session 之觀測面**（DR-SU2 v2(b) 未解）。
    2. 標註 `*Not support at GEN1` 等平台限定之碼，引用時須連同限定一併記。
    3. 「Not an actual error」之二碼（458760／458763）不作失敗判準。

(d) **正向路徑不因本表而有觀測面** —— 本表解的是「失敗時看什麼」，
    不是「成功進行中看什麼」。正向列之處置維持 R-SU25(c)。
```

---

## 四、任務（T42）—— 與 T41 並行，不互相阻斷

| # | 任務 |
|---|---|
| T42a | **intake**：Pei 將 `Error_Code_List.xlsx` 置入 `features/sw_update/inputs/` 後（或自 Pei 指定路徑複製），執行 intake 慣例：SHA、尺寸、分頁清單入 `feature.yaml`／`RECON` 慣行處 |
| T42b | **R-SU26 全覽**：9 分頁逐頁之欄序、標頭、非空列數、值型態摘要（**含實例**，PLAYBOOK (28)）、用途標記。預判：`Error Code List` 分頁已用；`ProvideSW_final`／`Flash Status`／`Flash Record`／`MD_IMAGE`／`R1L_Need_Machine`／`PROD_Parameter_Compare` 疑為台架作業記錄——**逐頁陳報，分析層裁** |
| T42c | **錯誤碼台帳**：自 `Error Code List` 分頁抽出全部碼 → `features/sw_update/ERROR_CODES.md`：碼、Description verbatim、階段、平台限定註記、對應 Test Set 候選（依 R-SU35(a)，**候選非裁定**）。閉合檢查：台帳碼數 = 分頁碼數 |
| T42d | **台帳更新**：(i) `SOURCE_COLUMNS.md`：新增 Error_Code_List（依 T42b）；診斷側三源登記為「已查·不用（無 FOTA 內容）」含 §1.2 之數字；(ii) 036 `C` 欄理由句更新為「Pei 確認不需填（2026-08-28）」，撤「日後要填須新 DR」但書；(iii) `framework.md` 之 DR 註記同步 |
| T42e | **DR 文本備妥**：`docs/upstream_requests/DR-SU1_SU2_request.md` —— DR-SU1 全文 + DR-SU2 v2（§二）+ 診斷側三源舉證表。**格式為可直接轉發上游之獨立文件**（含背景一段、請求條列、附件清單）；**發送者為 Pei，執行層只落檔** |
| T42f | **T-抄**：R-SU35 逐字 append；索引表同步（T41e 後應為 34 條 → 本條入列為 **35 條**；若 T41 尚未跑，依實際現況記，**以現場為準不以推算為準**）。`DATA_REQUESTS.md`：DR-SU2 改 v2（§二全文），沿革保留 |

**不在本輪**：據 error code 撰寫 TC（待 T42c 對照表 + DR-SU2 v2(a) 途徑答案）、寫回、git。

---

## 五、上繳包要求（`docs/upstream/27_error_code_intake.md`）

1. T42f 核對結果 + 索引表（條數以現場為準）
2. T42b 之 9 分頁全覽 —— 含各分頁「疑為台架記錄」之陳報
3. T42c 之 `ERROR_CODES.md` 與閉合檢查
4. T42d／T42e 之落檔
5. 未結 DR 清單（DR-SU1 + DR-SU2 v2）
6. 獨立自評 —— 特別回答：**T42c 之「對應 Test Set 候選」一欄，
   其判斷依據若只是階段名與組名之字面相近，即為 R-SU20(d) 所禁之循環 ——
   執行層以什麼依據填該欄而不落入循環**
