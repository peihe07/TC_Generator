# 上繳包 06 — vsm_v43：SYSRA 暫代母體建檔、Layer 2 暫代材料

日期：2026-09-02　執行層　對應下放包：`docs/handoff/06_interim_mother.md`
sha8 報 **`body_sha8`**（樹外 `--out`）；台帳**不重生**；**DR 之發送屬 Pei，執行層不代發**。
**本包不生成任何 TC**（Layer 2 待 Pei 裁）。

---

## 〇、一句話結論

**W-1～W-4 全數執行，E37／E38 相符（分母未漂移），E39／E40 為觀測值，E41 相符。§四兩項升級條件皆未觸。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E37 | `leaves_interim.tsv` 列數 | **295** | **295** | ✅ |
| E38 | 兩隔離清單 | 171／41；三檔合計 507 | **171／41；合計 507** | ✅ |
| E39 | `chapter_for_vf` 完整值組數 | 觀測 | **72 組**（前二階彙總 `01.11` 39 組／`01.14` 30 組／`01.13` 3 組） | — |
| E40 | 295 列中描述含 v5「解得」訊號者 | 觀測 | 含 v5 訊號名 **263**；其中含**解得**訊號 **126** | — |
| E41 | R-VT18 `body_sha8` | 與現檔一致 | **`04399f1c`** | ✅ |

**§四升級條件**：分母未漂移（295／171／41，合計 507）；
**執行層產出中無任何聚類命名** —— 材料只列 `chapter_for_vf` 原值、逐字標題例、詞頻與計數。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | 暫代母體與兩張隔離清單建檔；Layer 2 材料四節；framework 與 DECISIONS 依 R-VT18 加註 |
| 核實無誤 | 295／171／41 三檔合計 **507** ＝ Functional 總數（分母定義與上繳 01 W-4 逐字相同，未重算亦未漂移）；framework Layer 2 節表列數實測 **0** |
| 正確地不動 | **不聚類、不命名**（06 包 §四）；**不生成 TC**；DECISIONS Sign-off **未動**（已簽）；DECISIONS 第 3 列「0，待 037」**不刪**（R-TM13），第 3′ 列並存；**DR 未代發**；台帳不重生 |

---

## 二、W-1 —— 暫代母體建檔

### 標題欄名實測（06 包明令回報）

**SYSRA `Basic Report` 無專用之需求標題欄。** 逐欄實測：

| 欄 | 表頭 | 於 295 列之非空 | 判 |
|---|---|---|---|
| B | `SYS2 Sys-RA-Feature-ID` | **295/295** | 唯一穩定之識別碼（`Sys-RA-VF665_V43_VSM-nnn`） |
| C | `SYS2 Melco ID` | **0/295** | **全空**（A-VT9），無法作標題 |
| D | `Description` | 295/295 | **需求全文**：中位 **191** 字元、最長 **438**；含 `_x000D_`（Excel 之 CR 編碼形） |
| V | `SYS2 子分類 Sub Category Function Name` | 295/295，**相異 2**（294 : 1） | 無分組鑑別力 |
| W／X／Y | 功能一／二／三階 | 295/295，各**相異 2**（294 : 1） | 無分組鑑別力 |
| K | `SYS2 VF章節 Chapter for VF` | 295/295，**相異 72** | **唯一有分組鑑別力者** |
| L | `SYS2 VF後綴 VF suffix` | 295/295，**相異 295** | 逐列唯一，不可分組 |

**故本包之「標題」一律取 `Description` 逐字**（`_x000D_` 正規化為空白），並於材料檔就地標明。

### `data/leaves_interim.tsv`（**295** 列）

欄位：`sheet_row | sys_ra_feature_id | title_source_description | chapter_for_vf | vf_suffix |
document_id | signal_names_in_description | n_signals | n_solved_signals | tc_status`

`tc_status` 全列 = `interim_leaf`。
`signal_names_in_description` 為該列 `Description` 中出現之 v5 事實表訊號名（子串比對，
母體為 v5 排除旗標以外之 219 名）；`n_solved_signals` 為其中結果＝`解得` 者之數。

### 兩張隔離清單（同欄位，`tc_status = ISOLATED (DR-VT2)`）

| 檔 | 列數 | 條件 |
|---|---|---|
| `data/isolated_vf655.tsv` | **171** | `Document ID` = `VF655_V43_R3` |
| `data/isolated_nodocid.tsv` | **41** | `Document ID` 空 |

**三檔合計 295 ＋ 171 ＋ 41 = 507 ＝ Functional 總數**（E38 ✅，分母未漂移）。

---

## 三、W-2 —— Layer 2 暫代材料（`data/layer2_material_v43.md`）

**執行層只出材料，不聚類、不命名。** 四節：

### 1. `chapter_for_vf` 完整值分組 —— **72 組**

| 組大小 | 組數 |
|---|---|
| 1 列 | **32** |
| 2–4 列 | 12 |
| 5–9 列 | 22 |
| 10 列以上 | **6** |

最大組 `01.14.01` = **38** 列。前二階彙總：`01.11` **39** 組／`01.14` **30** 組／`01.13` **3** 組。

> **供分析層注意（材料層之觀察，非聚類建議）**：72 組中 **32 組僅 1 列**，
> 而 `chapter_for_vf` 之階數不一（`01.14.01` 三階 vs `01.11.01.01.08.03` 六階）。
> 若直接以完整值作 Test Set，將得 32 個單列組；若截至某一階，組數與粒度會大幅改變。
> **截幾階是聚類決策，屬分析層／Pei，本包不做。**

### 2. 每組 3 個標題例（首／中／末列，逐字取 `Description`）

72 組全數列出，各附 `sheet_row` 與 `Sys-RA-Feature-ID`。單列組則只列 1 例。

### 3. 標題詞頻前 30

正規化：小寫、取 `[A-Za-z][A-Za-z_]{2,}` 詞元、去停用詞
（the/of/and/for/to/is/in/a/be/shall/if/or/on/when/with/as/this/that/it/by）。

前 10：`tlm` 280／`signal` 237／`then` 214／`can` 173／`equal` 167／`user` 165／
`proxi` 156／`internal` 140／`req` 106／`sends` 103。

> 詞頻以 `TLM`／`signal`／`CAN`／`PROXI`／`internal`／`Req` 為首 ——
> 即**需求文本以訊號動作為主體**，而非以功能名為主體。這使「以標題詞聚類」之效果可疑；
> 併第 1 節之階數不一，**分組訊號主要仍在 `chapter_for_vf`**。此為觀察，不是建議。

### 4. 295 列 ∩ v5「解得」訊號之分組分布（P4 可執行度預估）

| 項 | 列數 | 占 295 |
|---|---|---|
| `Description` 含 v5 訊號名 | **263** | 89% |
| 其中含**「解得」**訊號（可寫 `$MESSAGE.Signal$`） | **126** | **43%** |
| 完全不含 v5 訊號名 | **32** | 11% |

逐組之 `列數／含訊號／含解得／含解得占比` 表列於材料檔第四節。

> **這是 P4 最該先看的數字**：暫代母體 295 列中，只有 **43%** 之需求描述提到了
> 「已解得」之訊號。其餘者之 TC 若要寫 `$MESSAGE.Signal$`，
> 其訊號或落在 `訊息名不符(R-13)`／`CAN-C 未到件`／**內部訊號 88 名全未解**（R-P355(c) → `PENDING: DR-VT4`）。
> **DR-VT4 之代價在此具體化**：近六成之暫代 leaf 之驗證面尚未落地。

---

## 四、W-3／W-4 —— 加註

### `framework.md` Layer 2 節（**未填任何 Test Set**）

原「留白為裁決結果」段**保留**，其下加 R-VT18(e) 加註：改走 SYSRA 暫代線、
暫代母體 295 與兩隔離清單之落點、Layer 2 材料之落點與分工（材料歸執行層／草案歸分析層／鎖定歸 Pei）、
重錨條款全文。**實測該節表列數 = 0。**

### `DECISIONS.md`（Sign-off **未動**）

於 P3 節之表**新增第 3′ 列**「母體（暫代）＝ 295（SYSRA），重錨條款生效」，標 `[AUTO]`（落實 R-VT18，非新裁）。
**第 3 列「0，待 037」不刪**（R-TM13），兩列並存並就地說明銜接方式。
「Layer 2 不在本表」一句改記暫代線之材料落點與分工。

---

## 五、E 對照與 sha

E37–E41 見 §〇。補充量測條件：
- E37／E38 之分類條件為 `Document ID` **全等**（`VF655_V43_R3`／空字串），與上繳 01 W-4 同；
- E39 之「完整值」指 `chapter_for_vf` 原字串未截階；
- E40 之比對為**子串包含**（訊號名出現於 `Description` 之任一位置），
  母體為 v5 之非排除名 219 個 —— **子串式會把 `X.Foo` 誤配到 `X.FooBar`**，
  故 263／126 為**上界**；下包若要精確值，須改詞界比對。此揭露依 R-G8。

| 條號 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 |
|---|---|---|---|---|
| R-VT17 | `4155a111` | `16377de4` | `RULINGS.md`:252 | 9 |
| **R-VT18** | **`04399f1c`** | `7d08d3f6` | 同上:264 | 16 |

`RULINGS.md` 現檔共 18 條 R-VT；台帳內 10 條（R-VT11–R-VT18 **八條**未入，待 Pei 重生）。

---

## 六、anomaly／DR 狀態

**本包無新登 anomaly。** 三處觀察（組數 72 中 32 組單列、詞頻以訊號動作為主、
含解得僅 43%）皆為**材料層之事實**，其處置屬聚類決策（分析層／Pei），
依 06 包 §四不得由執行層作成，故不立 A 號。

### DR

| DR | 狀態 | 本包實測 |
|---|---|---|
| DR-VT1 | **Pei 裁定送出，待發**（發送屬 Pei，**執行層未代發**） | 暫代母體已建，本線不等回覆 |
| DR-VT2 | 建議併送 | **隔離清單已成檔**：`VF655` 171 列、DocID 空 41 列，各帶完整欄位可直接附 DR |
| DR-VT3 | 暫持 | 2 名，未變 |
| DR-VT4 | 先不送 | **代價具體化**：暫代 295 列中僅 43% 含已解得訊號（§三-4） |
| DR-VT5 | 結案 | — |

---

## 七、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **506**（上繳 05 時 505）。將本包產出移除（`framework.md`／`DECISIONS.md` 還原至 `HEAD`、本檔移出樹外）後重跑**仍為 506** → 貢獻 0。+1 來自他線（`features/vehicle_setting/`、`features/vsm_v42/` 於本包執行期間多處未提交） |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT18 八條未入台帳；依 R-VT14(c) 重生歸 Pei 提交前一次 |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/`。本包新增之 `data/*.tsv`／`*.md` 未判紅 |

---

## 八、獨立判斷

1. **暫代母體最大的風險不在「暫代」，在 `chapter_for_vf` 撐不撐得起 Layer 2。**
   72 組裡 **32 組只有 1 列**，而階數從三階到六階不等。
   若照完整值切，會得到 32 個單列 Test Set —— 那不是 Test Set，是 leaf 的別名。
   若截階，截幾階直接決定粒度。**這是本包交給分析層的核心問題**，
   材料檔第一節已把每組列數與前二階都列齊，但**截階與命名我不做**（06 包 §四）。

2. **43% 這個數字比 295 更該進交付說明。**
   暫代母體 295 列中，只有 126 列之描述提到已解得之訊號。
   其餘 169 列若照樣生成 TC，其 Procedure／ER 之觀察對象大量會落在
   `PENDING: DR-VT4` 或保留原名不加 `$`。
   R-VT18(d) 已令「交付說明須揭露暫代構型」——
   **建議該揭露不只寫「SYSRA 錨定」，也寫「43% 訊號可執行度」**，
   否則讀者會以為 295 列都是可執行的 TC。

3. **重錨條款的返工量現在可以估了，建議 P4 開始前先估。**
   R-VT18(c) 令 037 到件後逐 TC 重錨、對不上者作廢或重寫。
   295 列 SYSRA 需求對上 037 需求單位之對映率無人知道 ——
   但 V43 ↔ V42 之 Functional 描述逐字重疊實測僅 **30/398**（上繳 01 E8）。
   若 037 之切分接近 V42 之形制，重錨對映率可能不高。
   **這不是反對 Pei 的裁決**（返工已是知情採認之代價），
   而是建議在 P4 生成量放大之前，先以少量批次驗證重錨可行性。

4. **E40 之 263／126 是上界，我用的是子串比對。**
   `X.Foo` 會被 `X.FooBar` 的描述誤配。要精確值須改詞界比對。
   本包未改，因 06 包只要「有無訊號名」之計數，且上界對「可執行度預估」之用途足夠；
   但若該數字要進交付說明（§八-2），**應先重算**。

5. **本包未驗而下放包亦未要求者**：
   (a) 隔離之 171 ＋ 41 列與 295 列之 `chapter_for_vf` 是否重疊 ——
       若重疊，DR-VT2 澄清後之增補批會落進既有組，影響 Layer 2 粒度；
   (b) `Sys-RA-VF665_V43_VSM-nnn` 之編號連續性未查（是否有跳號＝上游刪除痕跡）；
   (c) `GenSigSendType` 列舉定義仍未得（R-VT17(d)：037 到件後之首包併查）。

---

## 九、禁區遵守聲明（00 包 §零，第 5 條依 R-VT18(b) 改寫）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫、未讀 |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 全程唯讀 |
| 5′ | **得且僅得**以 SYSRA 295 列建暫代母體：已為之；`VF655` 171 ＋ DocID 空 41 **未入母體**，隔離成檔。**TC 仍未生成**（`generated/`／`batches/` 空） |
| 6. 不自行送 DR | **未代發 DR-VT1**（Pei 裁定送出，發送屬 Pei）；`DATA_REQUESTS.md` 未動 |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`data/leaves_interim.tsv`（新）、`data/isolated_vf655.tsv`（新）、`data/isolated_nodocid.tsv`（新）、
`data/layer2_material_v43.md`（新）、`framework.md`（加註）、`DECISIONS.md`（加註）、
`docs/upstream/06_interim_mother.md`（新）。
`RULINGS.md`、`DATA_REQUESTS.md`、`ANOMALIES.md`、v1–v5 TSV、`RECON.md`、`feature.yaml` **未動**。

---

## 十、下一步

1. **分析層**：自 `data/layer2_material_v43.md` 出 Layer 2 草案 —— 核心決策為
   **`chapter_for_vf` 截幾階**（完整值 72 組含 32 個單列組，§八-1）
2. **Pei**：裁 Layer 2 並鎖；**發送 DR-VT1**（併 DR-VT2，隔離清單已備）；
   commit；台帳重生（R-VT11–R-VT18 八條）
3. **P4 生成包之前建議**：以少量批次驗證重錨可行性（§八-3）；
   E40 若要進交付說明則改詞界比對重算（§八-4）
4. P4 生成時：D 欄用 SYSRA 實名 ＋ Remarks 逐列 provisional 註（R-VT18(c)）；
   交付說明揭露暫代構型**與 43% 訊號可執行度**（§八-2）
