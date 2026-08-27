# 上繳包 02 —— T11–T14 結果、R-SU5 v2／R-SU7 抄錄、三項待裁

- 日期：2026-08-27
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/03_review_rulings.md`（T11–T14、T-抄）
- 未結 DR：**0 筆**（無變動）
- 新登 anomaly：**0 筆**
- **待裁三項**：VF747 第三家族（T11）、錨點池 565→574（T12 修正）、
  `spec_mode` A→A+B+D（T13，已依「不符即停」停手）

---

## 一、T11–T14 逐項結果

### T11 —— VF747 repo 原件結構探測

素材：`inputs/Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx`
sha256 `8970eb04dbc158e841108ac7003b82c7fab52dabbb0e9e1a23ca9cfa1855a416`
（865,472 B，真 OOXML；`word/` 下七份 XML part，無 customXml、無 itemProps）

`word/document.xml` 682,992 chars → 純文字 124,398 chars，段落 2,292 段。

#### (i) Artifact Type 宣告有無與分布

```
  [Artifact Type:…] 命中: 0     分布: 無
  [State:…]         命中: 0
```

**零。** CFTS_57 之 Polarion 物件宣告形態在本文件**完全不存在**。

#### (ii) 7 位 ObjectID 有無（brace／裸／bookmark 三路皆查）

| 查法 | 命中 | unique |
|---|---:|---:|
| brace 形 `{7位}` | **0** | 0 |
| 裸 7 位數 | **0** | 0 |
| `w:bookmarkStart/@w:name` 含 7 位數 | 1（`_Toc196216297`） | — |
| `PAGEREF` | **0** | — |

唯一命中之 bookmark 為 Word 自動產生之 TOC 錨（`_Toc` 前綴），非物件 id。
**本文件無任何 Polarion ObjectID。**

#### (iii) `SYS-RA-VF747`／V2／V6 字樣與 10 個目標 id 之可解性

| 字樣 | 命中 |
|---|---:|
| `SYS-RA-VF747` | **0** |
| `SYS-RA` | **0** |
| `VF747` | 2 |
| `\bV2\b` / `\bV6\b` | 0 / 0 |
| `V1_R3` | 1 |
| `Requirement ID` | **0** |

`VF747` 之兩處出現：

1. 文件標題行 —— `Entire Vehicle FOTA Management [VF747_V1_R3]`
2. 參考文件節 —— `The following documents shall have presedence over VF747`
   （原文拼寫如此）

**10 個目標 id 之可解性：全部 0 命中。**

| id | 命中 | id | 命中 |
|---|---:|---|---:|
| 1061 | **0** | 1067 | **0** |
| 1062 | **0** | 1348 | **0** |
| 1063 | **0** | 175 | **0** |
| 1064 | **0** | 183 | **0** |
| 1066 | **0** | 184 | **0** |

#### 文件自身之編號體系

style 分布：`51`×131、`31`×52、`41`×48、`21`×18、`1`×1、無 style×2,042。
heading 皆為**無編號之名稱**（`Vehicle Function Data`／`Revision Notes`／
`Introduction`／`Functional Diagram`／`External Interfaces`／`Control Unit`
／`ECU`／`I/O`／`Signal` …），**無任何需求層級 id**。

其他 id 形態掃描：`\b\d{4}\b` 50 次 unique 10（`1000, 1001, 4201, 4202,
4204, 4205…`，為訊號值／參數，非 id）；`[A-Z]{2,}-\d+` 僅 `FD-8` 1 次；
`CFTS057` 2 次；`NRL-\d+` 0 次。

#### T11 之結論（量測，不裁）

**在手之 VF747_V1_R3 無任何可承載 `SYS-RA-VF747_V2-1348` 形態之 id 體系。**
三項獨立事實同向：(a) 無 Polarion 物件宣告、(b) 無 7 位 ObjectID、
(c) 037 引用之 V2／V6 與在手之 V1_R3 為不同大版。

即：R-SU5 v2 (a) 對 VF747 族所稱之「版本落差 + 物件結構未經實測」，
經實測後**強化**而非緩解 —— 不僅版本不符，該版本根本無物件結構可對。

> **執行層另行回報（非 T11 範圍，供裁參考）**：本機另存有
> `~/Work/02_Project_R1LR/9_ASPICE/SYS.1 Requirement Elicitation/`
> `SYS1_VF_with source ID/HDCC27/VF747_V1_R3_PHDCC27.xlsx`
> 與 `SYS1_DT27_VF_Diff_HDCC27/VF747_V1_R3_PDT27_DiffHDCC27.xlsx`
> 二檔，其目錄名為 **"VF with source ID"**。若第三家族要成立，
> 該類 export（而非 .docx 本文）才可能是 source id 之載體。
> **執行層未開啟該二檔**（不在本包素材範圍，且開啟即構成新外部引用）。
> 是否納為素材、是否發 DR，請裁。

#### 併帶：037 Source ID 欄全集 FOTA id 之台帳數（R-SU5 v2）

| 抽取法 | 命中 | unique | 值域 | 重複引用 |
|---|---:|---:|---|---|
| **全集**（每格抽出所有 FOTA id） | **376** | **366** | 1–526 | **10 個**：43, 68, 69, 112, **334**, 395, 411, 444, 475, 480 |
| first-id-only（v1 法） | 373 | 364 | 1–526 | 9 個（無 334） |

差額：命中 +3、unique **+2**。併記格之第二 id 為 `361`、`507` 兩個新值；
`334` 因其已於他列以 first-id 出現，全集抽取後轉為**第 10 個重複引用者**。

VF747 族 10 格之內部分布：`VF747_V2` **7 格**、`VF747_V6` **3 格**。

**台帳值（後續一律引用此列）**：全集 FOTA id 命中 376、unique **366**、
值域 1–526、重複引用 10 個。

### T12 —— Description → 所屬物件對照

產出：`ANCHOR_POOL.md` **§六**（新增）+ **§七**（差異說明）。

判定法：依文件序維持「當前章節物件」與「當前需求物件」兩游標；
遇 heading style `1`–`4` 更新章節游標並**清空需求游標**（跨章不繼承）。
Description 歸同章節內其前方最近之需求物件；該章尚無需求物件者歸章節物件。

| 統計 | 數 |
|---|---:|
| Description 物件總數 | **137** |
| 歸需求物件 | 45 |
| 歸章節物件 | 92 |
| **不可解** | **0** |

**137 個全數有上位物件可歸，不可解 0 筆** —— R-SU7 配套之「對照不可解者
列表回報」為空表。

#### ⚠ T12 過程中發現 T10 之分類法缺陷（連帶修正錨點池）

T12 得 Description **137**，而上繳包 01 T10 報 **135**。追查成因：
T10 採「首見為準」（`recs.setdefault`），而部分 id 在文件 §4 區
**先以內文 `Requirement ID {id}` 形態出現**，其 `[Artifact Type:…]`
宣告排在後方，因而被誤歸「不可歸類」。

改採**宣告優先於文序**（凡文件任一處帶 `[Artifact Type:…]` 宣告者，
一律以該宣告定其類）後重建全檔，**11 個 id 自「不可歸類」移出**：

| 移動 | id |
|---|---|
| 不可歸類 → **需求物件**（9） | `4907244`, `4907397`, `4907816`, `4907830`, `4907832`, `4907839`, `4907850`, `4907851`, `4907907` |
| 不可歸類 → **Description 物件**（2） | `4907923`, `4907934` |

| 類型 | T10（首見為準） | 修正後（宣告優先） | 差 |
|---|---:|---:|---|
| 章節物件 | 87 | 87 | — |
| 需求物件 | 478 | **487** | **+9** |
| Description 物件 | 135 | **137** | **+2** |
| 不可歸類 | 21 | **10** | **−11** |
| 合計 | 721 | 721 | — |
| **錨點池** | **565** | **574** | **+9** |

`ANCHOR_POOL.md` 已改記修正值（§一、§三、§七）。
**裁決正本未改**（見 §四 待裁 2）。

### T13 —— `spec_mode` 之 FO §3 逐條核對

| Mode | FO §3 定義 | 本 feature 之事實 | 判定 |
|---|---|---|:--:|
| **A** | Polarion/SYS1 export；outline map from export；`{filename}_{outline}` | SYS1 export 在場，`Basic Report` 120 列有 `Outline Number`；`SYSRE_HMI_Source ID` 之值實測**恰為** `{檔名 stem}_{outline}`（T6：120/120 互證不符 0）。R-SU4 v2(b) 之 HMI 家族即走此路 | **成立** |
| **B** | PDF with text layer；pdftotext + section regex；`{filename}_{section}` | PDF 有完整文字層（68/68 頁、83,356 字元），且 **R-SU6 v2(b) 明令「規格內文一律機器抽取」** —— 文字管線確在使用（T5' 之 52 個 PU 即自此取得）。惟其 `spec_reference` 形態**不採** —— R-SU4 v2(b) 規定章節 token 逐字取 SYS1 欄原值，不由 PDF 構造 | **文字管線成立；spec_reference 形態不採** |
| **C** | Scanned PDF；OCR + PNG render | 非掃描件。R-SU6 v2(c) 之「圖形內容以頁圖 render 目視」屬 FO §3 之「Images are always rendered … regardless of mode」通則，**非 C 之主張** | **不成立** |
| **D** | CFTS / Word；doc extraction；reference is **looked up, never constructed** | CFTS_57 Reflash（真 OOXML）為 spec 主源之一，錨為 `CFTS057-{ObjectID}`。R-SU4 v2(a) 之 `spec_reference_template: null` 與「查得，非構造」**逐字對應 D 之定義**。T10 之 574 個池即此路之產物。另有 SYSAD、VF747 兩份 Word | **成立** |
| **E** | No spec（037/SWRA only） | 規格齊備 | **不成立** |

**逐條核對結論：本 feature 為 `A + B + D`。**
FO §3 明文允許組合（"A feature may combine modes"），repo 內既有前例：
`power_moding: "A+B"`、`projection: [A, B, D]`。

#### 現值 `"A"` 之來源與其結構性成因

`scripts/intake.py` 之 `propose_spec_mode()`：

```python
    sys1 = any(f["kind"] == "polarion_export" and "SYS1" in f["note"] ...)
    if sys1:
        pdf = "with figure PDF" if "spec_pdf" in kinds else "no PDF"
        return "A", f"SYS1 spec export present ({pdf})"
    if "cfts_doc" in kinds:
        return "D", ...
```

`if sys1` 於命中即 `return`，**結構上不可能報出組合** —— 本 feature
三份 `cfts_doc` 在場卻未進入判斷。此非誤用，是該函式只設計為回報單一
提案值（其 docstring 亦作 "Proposes spec_mode"）。**不立 anomaly**：
FO §3 已言明組合由人判定，函式未逾其職。

#### 處置

依 T13「不符即停」，執行層**未改** `feature.yaml` 之 `spec_mode` 值，
僅於該鍵上方加註待裁標記，值仍為 `"A"`：

```yaml
# ⚠ T13（下放包 03）逐條核對結果：本 feature 實為 **A + B + D**，
# 現值 "A" 為 intake.py 之提案（其 propose_spec_mode() 於 sys1 命中即
# `return "A"`，結構上無法報出組合，見上繳包 02 §一 T13）。
# 依 T13「不符即停」，執行層**不逕改**，待分析層裁定後回填。
spec_mode: "A"                    # [待裁 —— 實測為 A+B+D]
```

`DECISIONS.md` 之 `- spec_mode: [AUTO] A` 亦未動（recon 產物，
待裁定後隨下輪 recon 重生）。

### T14 —— A-SU3 之 repo 側複證

對 `inputs/` 之 PDF（sha256 `faa58c3131df…`）第 46 頁：

- 文字層 PU 命中：`PU0298`、`PU0410`、`PU0411`、`PU0971`、`PU971`（頁長 1,911 字元）
- `PU971` **僅 1 見**，原句逐字：
  > `Available 2” (PU971) and “Scheduler” popup (PU0411), only`

  其前句為 `…‘Set Time’ button (PU0411). The same anti-theft behavior will
  apply for the “ROV Forced` —— 所指確為「ROV Forced Update Available 2」
- 同頁 `PU0971` **3 見**（L17、L27、L44），皆指同一彈窗；
  L44 為頁題 `Forced Update Available 2 (PU0971) for EMEA`
- 頁首：`LOGIC & FLOW: FOTA ROV Schedule Update`

**render 目視複證**：以 `page.get_pixmap(dpi=400)` 裁切該 token 矩形
（`Rect(482.54, 188.93, 518.77, 199.97)` ±邊界）放大檢視 ——
版面上原字面確為 `(PU971)` **三位數**；同一裁切區內之 `(PU0410)` 顯為
**四位數**，二者字距一致。**排除文字層抽取漏字之可能。**

處分之 (i)（同段落三處以 `PU0971` 指同名彈窗）與 (ii)（不在 1,341 個
unique PU 內、3 位形態逸出全清單型態）於 repo 側**完全複現**；
(iii) 所指之「repo 側複證交 T14」即本節。**證據鏈閉合。**

`lint.popup_ids` 維持 51 個（`PU0971` 已在內），未新增 id ✅。

---

## 二、T-抄 之逐字核對結果

核對法同上繳包 01：程式自下放包之 ``` 圍籬抽出區塊，寫入目標檔後
**回讀該檔**逐字元比對。

| 條／文 | 抄入位置 | 字元數 | 字面一致 | sha256[:12] |
|---|---|---:|:--:|---|
| R-SU5 v2 | `RULINGS.md`（append 於 R-SU5 v1 之後） | 931 | **OK** | `037742490af2` |
| R-SU7 | `RULINGS.md`（檔末追加） | 413 | **OK** | `c957b2d21f24` |
| A-SU3 處分 | `ANOMALIES.md`（A-SU3 節內） | 633 | **OK** | `1afaf3271485` |

**R-SU5 v1 不刪不改之確認**：回讀後其 sha256[:12] 為 `94791d3d5e0b`，
與上繳包 01 §二 所記**完全相同** ✅。

`RULINGS.md` 現有 8 個條文區塊，序：
`R-SU1` → `R-SU2` → `R-SU3` → `R-SU4 v2` → `R-SU5` → `R-SU5 v2`
→ `R-SU6 v2` → `R-SU7`。

`ANOMALIES.md` 狀態：A-SU1 **RESOLVED**、A-SU2 **形態面 RESOLVED／
家族面 PENDING**（掛 T11）、A-SU3 **RESOLVED**。

---

## 三、T11 量測表（供 Pei 裁第三家族）

| 判準 | CFTS_57（既有第一家族） | SYS1 export（既有第二家族） | **VF747_V1_R3（第三家族候選）** |
|---|---|---|---|
| 物件 id 體系 | Polarion 7 位，brace + Artifact Type 宣告 | `SYSRE_HMI_Source ID` 欄，120 值 | **無** |
| 037 引用之 id 可解 | 池 574 個可對 | 120/120 可對 | **0 / 10** |
| 版本相符 | CFTS_57 SR26 20251202 ↔ 037 引用 | `(Aug_30_2023)` ↔ 037 引用 | 037 引 **V2／V6**，在手 **V1_R3** |
| 錨形態 | `CFTS057-{ObjectID}`（查得） | `{stem}_{outline}`（查得） | **無形態可定** |
| 素材身分 | 真 OOXML，已實測 | 真 xlsx，已實測 | 真 OOXML，已實測 |

**執行層之量測結論**：以在手素材，第三家族**無法成立** ——
非「暫緩」而是「無可對之物」。R-SU5 v2 (a) 對 (iii) 之暫行維持，
在本量測下可轉為確定維持。若分析層仍欲成立第三家族，須先取得
V2 或 V6 之 export（見 §一 T11 之 "VF with source ID" 線索），
屆時為新素材、新 DR。

---

## 四、待裁項

| # | 項 | 現況 | 執行層建議 |
|---|---|---|---|
| 1 | **VF747 第三家族** | T11 量測完成，10/10 不可解 | R-SU5 v2 (a) 對 (iii) 由「暫行維持」轉「確定維持」；VF747 不立為錨點家族。若欲保留可能性，另發 DR 索 V2／V6 export |
| 2 | **錨點池 565 → 574** | `ANCHOR_POOL.md` 已改記；**裁決正本未改** | R-SU7 條文載「池維持 565 = 章節 87 + 需求 478」與「Description 135」二數，應改為 **574 = 87 + 487** 與 **137**。成因為分類法修正，非素材變動 |
| 3 | **`spec_mode` A → A+B+D** | 依「不符即停」未改，僅加註 | 回填為組合形態（前例：`power_moding: "A+B"`、`projection: [A, B, D]`）。建議取 `[A, B, D]` 之 list 形態，與 projection 一致 |

---

## 五、未結 DR 清單

**空表。** 本輪 0 筆、無變動。

§一 T11 所提之 "VF with source ID" 二檔為**線索**，執行層未開啟、
未納入素材、未登記 —— standing rule 之觸發條件為「新發現之外部引用」，
本項為執行層主動檢索之本機檔案，非 037／規格所引用，故不入
`DATA_REQUESTS.md`。若分析層裁定納入，屆時登記。

---

## 六、獨立自評

**應驗而未驗者：一項。**

1. **T10 之分類法未在上繳包 01 自我覆核。** T12 之所以能發現 11 個
   id 誤歸，是因為它從**另一個方向**（Description 側）重數一次而對不上。
   上繳包 01 交付 T10 時，執行層只做了「章節物件 87 = TOC PAGEREF 87」
   一路交叉驗證 —— 該路只守章節物件，對「需求物件」與「不可歸類」
   之邊界完全沒有獨立覆核。若非 R-SU7 恰好要求 Description 對照，
   565 這個錯數會一路帶進 Phase 2/3。
   **教訓**：分類型產出應對**每一類**都有一路獨立計數，不能只驗最好驗的那類。
   本包已對修正後之數補上兩路（宣告數 vs 文序走訪數、Description
   對照數 137 vs 分類數 137）。

**另聲明兩項處置，避免被誤讀：**

- T13 之 `feature.yaml` 加註：依「不符即停」未改值，但保留一個已知
  不正確的值而不加標記會使後續讀者誤用，故加註而不改值。
  若分析層認為加註本身已逾「停」之範圍，可於下輪令其撤回。
- §一 T11 之 "VF with source ID" 線索：執行層**只列路徑、未開檔**。
  列出是因為它直接決定待裁 1 的可行性；不開是因為開啟即構成
  新外部引用之取用。

---

## 七、量測條件揭露（R-G8）

| 項 | 方法／工具 | 偽陽性風險 |
|---|---|---|
| VF747 結構（T11） | `zipfile` 讀 `word/document.xml`，正則去標籤取純文字；brace／裸數／`w:bookmarkStart@w:name` 三路查 id | 若 id 存於 `customXml` 或 `docProps` 而非 document.xml 會漏 —— 已列該 docx 之 `word/*.xml` 全部七份，無 customXml part，風險已閉合 |
| 目標 id 可解性（T11） | `(?<!\d){id}(?!\d)` 逐一掃純文字 | 3 位數之 `175/183/184` 較易誤命中他處數字 —— 實測為 **0 命中**，即連偽陽性都沒有，結論更強 |
| 全集 FOTA id（T11） | `re.findall(r"SYS-RA-FOTA-(\d+)")` 逐格（非 `re.search`） | 與 v1 之 first-id 法並列回報，差額已逐項閉合（+3 命中／+2 unique／+1 重複者） |
| Description 對照（T12） | 文件序雙游標（章節／需求），跨章清空 | **以文序鄰接為依據，非 Polarion parent 欄** —— 該欄不存在於本 docx 任何 XML part。表格內 Description 若宿主需求排在表後會誤歸前一需求；已以跨章清空限制誤差不越章。已於 `ANCHOR_POOL.md` §六 逐字揭露 |
| 分類法修正（T12） | 宣告優先於文序；兩路獨立計數交叉驗證 | 若同一 id 帶**兩個不同** Artifact Type 宣告則 `setdefault` 取首個 —— 已查：137 + 487 + 87 = 711，加不可歸類 10 = 721 = unique 總數，無重複宣告 |
| spec_mode 核對（T13） | FO §3 表格逐 Mode 比對本 feature 之素材與裁決條文 | 判定含解讀成分（B 之「文字管線用、reference 形態不用」為部分成立）—— 已逐 Mode 列出判定理由，供分析層覆核 |
| PU971 複證（T14） | PyMuPDF `get_text()` 逐行 + `search_for()` 定位 + `get_pixmap(dpi=400)` 裁切 render 目視 | 文字層與 render 同源於同一 PDF，若字型嵌入本身錯誤則二者同錯 —— 已以同區 `(PU0410)` 為對照（同字型、四位數正常顯示），排除字型層面成因 |
