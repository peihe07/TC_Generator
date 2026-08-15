# ANOMALIES — FW036 Comfort HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-CFnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

**Standing rule**：任何新發現之外部引用，於登記當下同時建 ANOMALIES 條目
與 `DATA_REQUESTS.md` 列（下放包 01 §5.5）。

| # | 類型 | 標題 | 狀態 | 阻塞 |
|---|---|---|---|---|
| A-CF01 | note | SR25 CR29359 含 037 未分析之新章節 | RESOLVED by R-C5 | 無 |
| A-CF02 | note | 客戶交付夾之 spec 為 SR25，與 R-C1 基線不一致 | OPEN（Tier 3，Pei 決定是否回填） | 無（不影響 pipeline 取材） |
| A-CF03 | 結構 | 34 列 parent 形態卻為 Functional Requirement | RESOLVED by R-C3 | 無 |
| A-CF04 | 工具 | `intake.py` 只掃 drop folder，spec_mode 提案偏低 | OPEN（已知限制，非缺陷） | 無 |
| A-CF05 | 工具缺陷 | `intake.py` 需求清單靜默漏計 57 列（346 vs 403） | FIXED 2026-08-14 | 無 |
| A-CF06 | 環境 | `pymupdf` 未安裝 → recon 改用 `pdftotext` fallback；SR24 PDF 具 text layer | **CLOSED**（09 §4 授權，已實作） | 無 |
| A-CF07 | 範本殘留 | 空白範本第 10–11 列樣本資料須於 write-back 清除 | OPEN（P4 前處理） | P7 交付 |
| A-CF08 | 覆蓋缺口 | SR24 **基線內** 51 節未被 037 引用；17 節 substantive 已判讀（4 in_scope／13 undetermined），4 節依 R-C16 為 RD-1 覆蓋缺口項 | OPEN（10 節 DEFERRED、3 節待 DR #6） | 無 |
| A-CF09 | 稽核（跨 feature） | **home／projection／privacy** 三者之 Sign-off 為空白範本（範圍已限縮） | OPEN（另案，不回溯補簽） | 無 |
| A-CF10 | 來源重複 | `inputs/` 曾存在 SR24 export 副本，依 R-C11 刪除 | CLOSED（已刪，已留痕） | 無 |
| A-CF11 | 判讀陷阱 | SR24 作 "Alternative"、CFTS043 作 "Alternate" —— 以客戶用詞搜尋得 0 命中，差點誤判 10 節為 out_of_scope | **已升格 R-C13**（案例保留） | 無 |
| A-CF12 | 上游矛盾 | CFTS043 4803259 之 NOTE 與同 item `Radio` 屬性矛盾（**主檔內部**矛盾；tree view 為索引層，不參與選邊） | **DEFERRED**（10 §2，Pei 直接向 RD 反應） | 無 |
| A-CF13 | spec 內部標籤 | **三處**條款標籤衝突：`C16.)` 跨 2.15／16.17；`W0.)` 跨 17.1／18.1／19.1；`HVS1/2/4/5/6` 跨 ch11／ch12 | OPEN（RD-1 候選，非阻塞） | 無 |

---

## A-CF01 —— SR25 CR29359 存在且含 037 未分析之新章節（note）

**登記依據**：下放包 01 §5.4，照登。**處置**：R-C5，全部 out of scope ——
不產 TC、不入 coverage 分母、不列 BLOCKED。本條僅為存在性紀錄，供日後 037
升版時查考。

SR25 outline 共 187 節，其中 58 節未被 037 引用。扣除章級容器標題、1.x
Assumptions 與影像頁後，屬實質需求而 037 未分析者：

| 節次 | 內容 |
|---|---|
| 18.2 / 18.3 / 18.4 | BCW1、BCW2，10.25" Comfort Widget |
| 19.1 / 19.2 / 19.3 | W0、LCW1、LCW2，7" Home screen Comfort Widget |
| 20.1 ~ 20.4.3（10 項） | CRB1–CRB4.3，LATAM Alternative Rear Blower |
| 21.1 ~ 21.5 + 21.3.1（6 項） | L3H1–L3H5，L3 HVAC management |

**執行層複測範圍與其界線**：本包所建之 outline map 只對 **SR24** export 建立
（`paths.sys1_export` 僅指向 SR24，R-C1）。上表之 SR25 節次係分析層之量測，
執行層**未複測**，也不打算複測 —— 複測需載入 SR25 export，而 R-C1 禁止 SR25
作為查得依據。此處記錄的是「分析層說有」，不是「執行層查到有」；兩者於 037
升版、SR25 成為基線之日才需要合流。

執行層可獨立佐證者只有一件：SR24 export 之 outline 共 **180** 個 number，
037 引用其中 **129** 個，未引用 51 個。此數與 SR25 之 187/58 是不同文件之
不同統計，不得互推。

## A-CF02 —— 客戶交付夾之 spec 為 SR25（note）

**登記依據**：下放包 01 §5.4，照登。

客戶交付夾 `10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/
ComfortHMI/` 於 2026-08-14 實測放置之 spec 為 SR25 PDF（13.86 MB）與 SR25
SYS1 xlsx（72.80 KB），與 R-C1 所定之 SR24 基線不一致。

**不影響 pipeline 取材** —— pipeline 取 `spec-index/`，且 `feature.yaml` 之
`sys1_export` / `spec_pdf` 皆寫 SR24 全名（非萬用字元），取到 SR25 在結構上
不可能發生。交付時之附件一致性須由 Pei 決定是否回填 SR24（Tier 3）。

**執行層未複測**：該交付樹於本 session 之檔案系統不可達（已搜尋，無
`10_Reviewing` 路徑）。上列兩個檔案大小為分析層之量測，執行層照登而未驗證。
回填與否之決定不應僅以本條為依據，宜於可觸及交付樹時重測。

## A-CF03 —— 34 列 parent 形態卻為 Functional Requirement（結構）

**登記依據**：下放包 01 §5.4。**處置**：R-C3，已由 Categorization 判準涵蓋。
**登記供其他 feature 參照** —— 這是 naive leaf 判準之通用陷阱，不是 Comfort
獨有。

執行層實測（`recon.py`，非引用）：

| 判準 | 得數 |
|---|---|
| Categorization == "Functional Requirement"（**在用**） | **403** |
| ID 具 `-NN` 後綴（**禁用**） | 369 |
| 差額（parent 形態、自身即需求） | **34**（8.4%） |

全 34 列列於 `data/recon.json` 之 `parent_shape_functional`。條文所舉三例
（`SWE1-HVAC-011` row 66 Fan Speed Control、`-026` row 137 Rear Defrost
Control、`-037` row 183 On/ State）逐一比對，行號與標題皆相符，且三者確在
該 34 列內。

**為何它會靜默**：漏掉的 34 列不會讓任何腳本報錯 —— coverage 分母跟著變小，
於是「全部覆蓋」照樣成立。8.4% 的缺口以「100% 完成」的形式呈現，這是它危險
之處，也是 R-C3 明文要求機械強制而非文件約束的理由。`recon.py` 現同時輸出
兩個判準之得數，差額成為報表上的一個數字，而非讀者需自行察覺之事。

## A-CF04 —— `intake.py` 之 spec_mode 提案只反映 drop folder（工具／已知限制）

第一次執行 `intake.py Comfort` 提 **spec_mode E**（no spec source found），
因 `_intake/Comfort/` 只放 037，spec 素材依下放包 01 §5.2 留在 `spec-index/`。

**非缺陷，是範圍限制**：intake 之契約就是「分類 drop folder」。但其輸出
`## Proposed spec_mode: **E**` 措辭並未限定範圍，單看該行會誤以為全庫無 spec。

**處置**：不改 intake 之掃描範圍（擴及全庫會讓分類結果依賴無關檔案）。改以
兩項留痕：`_intake/Comfort/INTAKE.md` 頂端註明兩次執行之差異與其成因；
`feature.yaml` 之 `spec_mode: "A"` 依下放包裁定，非依 intake 提案。
以四份素材齊備之暫存 drop folder 重跑，intake 獨立提出 **A**，與裁定一致。

## A-CF05 —— `intake.py` 需求清單靜默漏計 57 列（工具缺陷，已修）

**現象**：第一次執行報「need list 346 leaves」，實為 **403**。

**成因**：`cited_documents()` 以 `re.search(r"_[\d.]+\s*$", s)` 判斷文件引用
形態，但 `s` 取整格。HMI Source ID 儲存格有 57 列（Functional Requirement
範圍內）在 section 之後另有 Polarion item id 行，`$` 錨點因而落在 item id 上，
匹配失敗 —— 那 57 列被當成「不是文件引用」而略過。

**為何危險**：它**不報錯**，且**仍指名正確的文件**。輸出看起來完全正常，只是
少了 14%。這正是 §5a 所指、需以已知全集覆核方能發現的一類缺陷；本次是因
R-C4 已獨立給出 129/403 兩個已知值，才在對數時暴露。

**同源第二處**：`_swra_profile()` 以 `"Source" in h` 取欄，命中 B 欄
`Source Requirement ID`（上游需求 id）而非 C 欄 `HMI Source ID`（文件引用），
因而把 Comfort 之來源形態描述為 "component/architecture ids (trace via
SYS3)" —— 與同檔下方 `cited_documents()` 實際採用之欄位互相矛盾。

**修正**（`scripts/intake.py`）：兩處皆改為取儲存格第一行；`_swra_profile()`
之取欄優先序改為與 `cited_documents()` 一致（`HMI Source` 優先）。
修正後 Comfort 得 403、形態報 "document citations (need-list derivable)"。
其餘 feature（home / amfm / sxm / projection / media / privacy）之 037 無
`HMI Source` 欄且為單行儲存格，實測輸出不變。

## A-CF06 —— `pymupdf` 未安裝，spec PDF text-layer 無法探測（環境）

`recon.py` 之 `survey_spec_text_layer()` 與 `intake.py` 之 `sniff_pdf()` 皆
依賴 `pymupdf`；本機未安裝，兩處輸出 `unknown (pymupdf not installed)`。

**未阻塞**：spec_mode A 之文字權威是 SYS1 export（`Basic Report`，180 節，
Description 欄即條文全文），PDF 之角色為圖面載體。SR24 PDF 6.16 MB 之
text layer 有無，不改變 129 節之查得結果 —— 該結果由 export 得出，已 PASS。

~~**未驗事項，不宜當成已驗**：目前**無法**陳述「SR24 PDF 具 text layer」。~~

**更新 2026-08-14（下放包 08 判讀期間附帶量測）**：改以 `pdftotext`
（`/opt/homebrew/bin/pdftotext`，已安裝）實測，**SR24 PDF 具 text layer**
—— 抽出 62,874 bytes 文字。「PDF 具 text layer」自此**可陳述**，前述禁止
假定之限制解除。

~~未解者僅剩工具面：`recon.py` 仍只試 `pymupdf`……**本輪未動**，列為建議。~~

**更新 2026-08-14（二）（下放包 09 §4 授權）—— CLOSED**：
`survey_spec_text_layer()` 已加 `pdftotext` fallback：優先 `pymupdf`，
不可用時改走 poppler 之 `pdftotext`；**兩者皆不可用**時才回報 unknown，
且訊息同時指名兩者。實測 `RECON.md` 現印
`text-layer: 62782 chars (via pdftotext)`。

依 R-C8 **未重跑任何既有 feature**（其 `RECON.md` 之 text-layer 行維持原狀，
下次各自重跑時自然更新）。

註：本條先前記 62,874 bytes（`pdftotext` 寫檔），recon 內測得 62,782 chars
（stdout 解碼後之字元數）。兩數皆為實測，差異來自「位元組 vs 字元」與
換行處理，非資料變動。

## A-CF07 —— 空白範本第 10–11 列樣本資料須清除（範本殘留）

`inputs/` 之 036 空白範本（rev C，SHA256 `cd876c202c71e74b…`，與 Privacy
同一份）第 10–11 列帶原廠樣本：row 10 之 D 欄 `xxx`、F 欄
`NR1L-AntiTheft-001`、G 欄 `AntiTheft`、S 欄 `NA`，row 11 之 D 欄 `xxx`
（B 欄兩列皆為 `=IF(ISBLANK($D..))` 公式，屬範本機制，不清除）。
recon 將該兩列分類為 2 列 DRAFT，故
`workbook_state` 仍判定為 **BLANK**（無 done region），此判定正確。

**副作用已顯現**：RECON.md「workbook req_ids ABSENT from 037」之 draft 區
報 1 筆 `['xxx']`。該筆是範本殘留，不是 traceability orphan；讀報表時勿
與真正之孤兒列混淆。

**處置**：比照 Privacy A-PV07，於 write-back 前清除該兩列。此處僅登記，
不動檔案 —— `inputs/` 為素材區，Phase 1 不改素材。

**下放包 03 §5 追加要求**：須於 **Phase 3 profile 明文**定其寫回時之處置
（覆寫或先清除），不得留到 write-back 當下臨時決定 —— BLANK 型之 write-back
為「append from first data row」，殘留列會位移首資料列。已記入 `RUNBOOK.md`
Phase 3 待辦。

## A-CF08 —— SR24 基線**內** 51 節未被 037 引用（覆蓋缺口）

**登記依據**：下放包 03 §3。**性質與 A-CF01 不同**：A-CF01／R-C5 處理的是
out-of-scope 文件（SR25）之內容；本條這 51 節在 **in-scope 的 SR24 基線裡**，
037 只是沒有分析它們。

實測：SR24 export 180 個 outline，037 引用 129，**未引用 51**。
分類清單 `data/sr24_uncited_sections.tsv`（由
`scripts/classify_uncited_sections.py` 產出，可重跑）：

| 分類 | 節數 | 說明 |
|---|---|---|
| `container` | 20 | 章級標題本身 |
| `assumption` | 9 | 1.1–1.8 範圍聲明 + 13.1 適用條件 |
| `figure` | 5 | 4.1 / 5.1 / 6.1 / 6.2 / 8.1，僅影像參照 |
| **`substantive`** | **17** | 含行為敘述而未被引用 |

`substantive` 全列：`16.1`、`18.2`、`18.3`、`18.4`、`19.1`、`19.2`、`19.3`、
`20.1`、`20.1.1`、`20.1.2`、`20.1.3`、`20.2`、`20.3`、`20.4`、`20.4.1`、
`20.4.2`、`20.4.3`。

**只分類，未做任何 TC 處置** —— 不產 TC、不入 coverage 分母、不列 BLOCKED、
不自行補 RD 項目（§8.2、§8.4.2）。處置屬 Pei 裁定（D-C10）。

### 判準之兩處說明（皆為判斷，非機械必然）

1. **`container` 之定義只滿足一半者有 6 節**：下放包定義為「章級容器標題，
   **其下層節已被引用**」。`1`、`4`、`5`、`8`、`19`、`20` 是章級標題，但其
   下層**全數未被引用**。四值必須取一，故仍歸 `container`（它們確實是標題，
   無行為敘述），但 TSV 逐列記 `cited_descendants` / `total_descendants`
   兩欄，使這 6 節可被一眼認出，不被平滑掉。
2. **`substantive` 之偵測不採 `will`**：下放包舉例含 `shall`／`will`／編號
   條款前綴。實作採「編號條款前綴 **或** `shall`／`must`」，**刻意排除
   `will` 與 `should`** —— 1.2「Differences between the radios **will** be
   specified」、1.4「the 12" Portrait UI **will** be a scaled up version」
   是對**文件本身**與縮放慣例的陳述，非系統行為。若採 `will`，全部 8 節
   Assumptions 會被歸為 substantive，分類即失去意義。
   `16.1` 是唯一靠 `must` 進入 substantive 者（「HC leds activation **must**
   always be coherent with the signal sent by the HVAC software」），非靠
   條款前綴，特此標明。

### 更新 2026-08-14（下放包 05／06）—— R-C5 衝突已由 R-C5-1 處置，並已完成適用性判讀

下方「與 R-C5 之衝突」一節所報之 16 節，經分析層以 **R-C5-1** 訂正：該 16 節
退出 R-C5 適用範圍，併入本條之 in-baseline substantive 集合。**現況未變**
（不產 TC、不入分母、不列 BLOCKED、不補 RD），改變的是理由。

17 節之適用性判讀（D-C10 前置）已產出
`data/sr24_substantive_applicability.tsv`：

| verdict | 節數 | 節次 |
|---|---|---|
| `in_scope` | **10** | 20.1、20.1.1、20.1.2、20.1.3、20.2、20.3、20.4、20.4.1、20.4.2、20.4.3 |
| `undetermined` | **7** | 16.1（EMEA 市場）、18.2–18.4（10.25"）、19.1–19.3（7"） |
| `out_of_scope` | **0** | —— |

> **上表已被下放包 07／08 取代。現行結果見下方「更新 2026-08-14（二）」。**
> 摘要：20.x 十節依 **R-C12** 降為 `undetermined`（pending DR #8）；
> 16.1 與 18.2–18.4 四節依 037 引用結構升為 `in_scope`；19.1–19.3 維持
> `undetermined`（pending DR #6）。合計 **4 in_scope／13 undetermined／
> 0 out_of_scope**。

- **20.x 判 `in_scope` 之依據**：SR24 §20 標題自身寫 "See CFTS043 for
  applicable vehicles"；CFTS043 對應節為 §1.3.5.1.22 *Alternate Rear Blower
  Control Softkeys*（items 4803257–4803286），該批於 tree view 自身之
  R1L-R 白名單（sheet `工作表1`，599 筆 ForeignID）中**全部 `Scope=Yes`**，
  且 `Radio` 含 `R1L-R`、`Market=All`。
  **`EE Architecture` 為 Atlantis Mid 而不構成排除** —— `Scope=Yes` 集合同時
  含 Atlantis High（264）與 Atlantis Mid（130），故 EE 不是本檔之 scope 閘。
  逐節條文對應可查：CRB3「Fan ranges: 1-4」↔ 4803264
  「`$R_BLW_Speed$` shall range from 1h-4h」；CRB2 REAR LOCK ↔ §1.3.5.1.22.3
  Lock Softkey；CRB4 power ↔ §1.3.5.1.22.1 Power Softkey。
- **variant_condition**：全 10 節皆受 PROXI 參數
  `$Indipendent_Rear_Fan$ = [Present]` 節制（CFTS043 4803260）。此為條件，
  非排除 —— 但意味著 TC 之前置條件必須寫明該參數，不可預設存在。
- **7 節判 `undetermined` 而非 `out_of_scope`**：CFTS043 是 HVAC controls
  規格，全篇無 `Comfort Widget`、無 `Home screen`、無 `10.25`、無 `EMEA`
  字串（442 頁主檔與 tree view 皆實測）。它**不涵蓋**這三類判準，而非
  **否定**它們。缺料清單已開列於 `DATA_REQUESTS.md`。

**仍未做任何 TC 處置**：不產 TC、不入 coverage 分母、不列 BLOCKED、
不補 RD、未改 R-C5 或 R-C5-1。判讀為量測，非處置（06 §3）。

### 更新 2026-08-14（二）（下放包 07／08）—— 現行判讀結果

`data/sr24_substantive_applicability.tsv`（欄位加 `pending_on`）：

| verdict | 節數 | 節次 | 所待 |
|---|---|---|---|
| `in_scope` | **4** | 16.1、18.2、18.3、18.4 | —— |
| `undetermined` | **13** | 20.1 ~ 20.4.3（10）、19.1 ~ 19.3（3） | DR #8／DR #6 |
| `out_of_scope` | **0** | —— | —— |

**20.x 十節（降級）**：依 R-C12，來源存在未解矛盾即記 `undetermined`。
依據全數保留，見上方 A-CF12 之層級訂正。

**16.1 與 18.2–18.4（升為 `in_scope`）—— 依據不是 Market Configuration
Table，是 037 自身之引用結構**：

| 章 | 標題 | 037 引用 | leaves |
|---|---|---|---|
| 16 | ICS CLIMATE EMEA – CARRYOVER | **18 / 19** | **99**（佔全 feature 25%） |
| 18 | 10.25" Home screen - Comfort Widget | **1 / 4**（18.1） | **3** |
| 19 | 7" Home screen - Comfort Widget | **0 / 3** | 0 |

- **16.1**：037 不可能在 EMEA 章產出 99 個 leaves 而該市場不在交付範圍內。
  16.1 是該章唯一未被引用之子節 —— 屬 in-scope 章內之**覆蓋缺口**，
  非範圍問題。
- **18.2–18.4**：037 引用 18.1，產出 `SWE1-HVAC-129-01/-02/-03`。
  注意 **18.1 與 19.1 條文文字相同**（皆為 `W0.)`），037 分析的是 10.25"
  那個實例。無論該選擇之解讀為「10.25" 是交付螢幕」或「作者對重複條款
  擇一分析」，**被分析的都是 10.25" 實例**，故本判定對兩種解讀皆成立。

**推論方向是單向的，這一點是關鍵**：

- **有引用 → 是證據**（不在範圍內就產不出那些 leaves）
- **無引用 → 不是證據** —— 「037 沒引用」正是 A-CF01／R-C5 之錯誤步驟，
  已由 R-C5-1 訂正。故 ch19 之沉默在任一方向皆不算數。

**19.1–19.3 維持 `undetermined`**：MCT 無螢幕尺寸軸；08 §3 之次要候選
已依該節要求先驗後用，**驗不過**（詳 DR #6）。

### 更新 2026-08-14（三）（下放包 09 §3／10 §2）—— 處置類別與 DEFERRED

**四節 `in_scope` 者之處置已依 R-C16 §2 定案**（TSV 加 `disposition` 欄）：

> 16.1、18.2、18.3、18.4 為 **RD-1 覆蓋缺口項，不是 TC 工作項**。
> 該節屬交付範圍而 037 未對其產出需求 —— 請上游 037 補分析。
> **不得由 TC 作者自行補成 RD 項目或直接產 TC**（§8.2、§8.4.2）。
> 037 補分析並落版前：不入 coverage 分母、不列 BLOCKED、不指派 tc_id。

R-C16 同時澄清一件先前未被問到的事：**`in_scope` ≠「我們去寫 TC」**。
20.x 十節縱使日後解出 `in_scope`，處置亦同 —— 037 未引用者一律回上游。

**20.x 十節之 `pending_on` 改記 DEFERRED**（10 §2）：Pei 裁定 DR #8 由其
直接向 RD 反應，不由本 pipeline 追。依 R15-2（open PENDING 意為「待裁決」
非「待外部條件」），DR #8 自 open PENDING 移出、自「阻塞 D-C10」清單移除。

**DEFERRED 不移動 verdict**：矛盾未解這件事不因誰去問而改變，故十節依
R-C12 維持 `undetermined` —— 不升 `in_scope`，亦不降 `out_of_scope`。
「把問題交給別人問」不是「問題有了答案」。

**四節之 verdict 依 R-C15 維持 `in_scope`**：09 §2 裁定 R-C12 不擴及
「依據為間接」，判準是**蘊含**而非**直接**。上繳 04 §6.2 第 3 項所標之
界線由分析層畫定，執行層先前照條文字面執行並標明界線之處置獲追認。

**Market Configuration Table 未能解答本題，須明記**：該檔（25PI3.5，
SHA256 gate PASS）全 8 工作表對 `R1L-R` **0 命中**、對任何螢幕尺寸
**0 命中**。其 variant 軸是**市場別**（ROW／ECE／US-CAN／ROW+／CHN／JPN／
MEX／KOR），非**機型別**；地理分組為 EMEA 149／APAC 37／NAFTA 19／
LATAM 19 國。它回答「哪個國家屬哪個市場、拿到什麼設定」，不回答
「本次交付涵蓋哪些螢幕與市場」。依 R-C13，上述 0 命中僅為索引層事實。

### ⚠️ 與 R-C5 之衝突（須 Pei 裁定，執行層不自裁）

R-C5 列了 22 節「SR25 新增而 037 未分析」之實質需求，裁為 out of scope，
理由是「因 R-C1 定基線為 SR24」。逐節對 SR24 export 實測：

| | 節數 | 節次 |
|---|---|---|
| **存在於 SR24 基線** | **16** | 18.2、18.3、18.4、19.1、19.2、19.3、20.1、20.1.1、20.1.2、20.1.3、20.2、20.3、20.4、20.4.1、20.4.2、20.4.3 |
| 不存在於 SR24 | 6 | 21.1、21.2、21.3、21.3.1、21.4、21.5（SR24 最大 outline 為 20.4.3，無第 21 章） |

該 16 節**全數**被本次分類為 `substantive`，且與 R-C5 之列舉逐節相符
（含「20.1 ~ 20.4.3（10 項）」之項數）。

**衝突所在**：R-C5 之推論是「屬於 SR25 → 因基線為 SR24 → out of scope」。
對這 16 節，前提不成立 —— 它們同樣在 SR24 裡。「在 SR25 中出現」不使一個
**同時存在於基線**的節超出範圍。R-C5 對其餘 6 節（21.x）之結論不受影響。

**執行層未做也不會做的事**：不改 R-C5、不將該 16 節納入 coverage 分母、
不產 TC、不列 BLOCKED、不自行補 RD。本條只陳述實測與其與條文之關係。

**執行層可獨立佐證之界線**：以上全部只用 SR24 export 得出（R-C1 允許）。
「SR25 是否也含這 16 節」**未驗亦不驗** —— 複測需載入 SR25。R-C5 稱其為
SR25 內容，本條不否定該陳述，只指出**它們也在 SR24 裡**，而這一點足以
使 out-of-scope 之推論對它們失效。

## A-CF09 —— DECISIONS.md 簽署狀態於 repo 內不可考（稽核，跨 feature）

> **範圍已限縮 2026-08-14（下放包 05 §3）**：本條適用者為
> **`home`、`projection`、`privacy` 三個 feature**，非全部。
> **`amfm` 與 `sxm` 不在其列** —— 兩者 Sign-off 已填且有 repo 證據。
> `media` 無 `DECISIONS.md`，屬另一種狀態，於本條末段另記。
> Comfort 自身尚未簽署，屬 Phase 2 進行中之正確狀態，不列為異常。

**登記依據**：下放包 04 §2。**不回溯補簽**（補簽等於偽造當時之簽署行為）；
自 Comfort 起依 R-C10 執行。既有 feature 之簽署狀態如何補記，屬 Pei 裁定，
另案。

執行層以 `read_signoff()` **唯讀**掃描全 feature（**未重跑任何 recon**，
R-C8）實測：

| feature | Sign-off | Amendment | `[PROPOSED]` | 狀態 |
|---|---|---|---|---|
| home | 空白範本 | 0 | 有 | **不可考** |
| amfm | `PeiPYHsu` / 2026-08-09 | 0 | 有 | 已簽（有 repo 證據） |
| sxm | `PeiPYHsu` / 2026-08-10 | 11 | 有 | 已簽（兩種形態皆備） |
| projection | 空白範本（`____________`） | 0 | 有 | **不可考** |
| media | — | — | — | **無 `DECISIONS.md`** |
| privacy | 空白範本 | 0 | 有 | **不可考** |
| comfort | 空白範本 | 0 | 有 | 未簽（正確狀態，Phase 2 進行中） |

**對下放包 04 §2 之一處訂正**：該節稱「全部 feature 之該區塊都是空白範本，
偵測器永遠回報未簽署，護欄形同虛設」。實測 **amfm 與 sxm 兩者已填**，
R-C9 之護欄對它們**今日即有效**。04 加 R-C10 之裁決結論不受影響（另外三個
確為空白範本），但該理由中「一次也不會觸發」一句不成立。此訂正使 R-C8
之份量上升：amfm／sxm 若被重跑，覆蓋的是有 repo 證據的簽署。

**第三種狀態**：`media` 無 `DECISIONS.md`，既非已簽亦非空白範本。其是否
應有該檔、或本就不走 FW036 決策流程，未查，不臆測。

**執行層先前之錯誤陳述**：上繳包 01 §6 稱「Privacy 之 `DECISIONS.md` 已
簽署」。實測其 Sign-off 為 `- Reviewed by: ____  Date: ____`，**未簽署**。
該陳述無 repo 證據支持，係誤信聊天脈絡。不重跑 Privacy 之結論不變（R-C8
之理由為「無數字更正」，與簽署與否無關），但理由已改正。

## A-CF10 —— `inputs/` 曾存在 SR24 export 副本，依 R-C11 刪除（來源重複）

**登記依據**：下放包 06 §1，條文明文要求登記此事實。

`features/comfort/inputs/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_
CR24879_(September_25_2023).xlsx`，**70,040 bytes**，SHA256
`6982d37db81b36e4bd3643ca1356c12d3837fb5843ba9cd06c4ee3317a073969`，
於 2026-08-14 依 R-C11 刪除。

**刪除前之確認（刪除不可逆，故先驗後刪）**：

| 前提 | 實測 | 結果 |
|---|---|---|
| `spec-index/cache/` 該份仍在 | 存在 | ✅ |
| 大小為 70,040 bytes | 70,040 | ✅ |
| （自加）兩份內容相同 | SHA256 皆 `6982d37db81b36e4…` | ✅ |

第三項為執行層自加。條文只要求確認在且大小相符，但**「大小相同」不蘊含
「內容相同」**，而刪除的正當性取決於後者。兩份逐位元組相同，故刪除不損失
任何內容。若兩者曾分歧，本次比對是唯一會發現它的時機 —— 這正是 R-C11 立條
的理由：兩份副本分歧時，**無任何機制會報錯**。

**刪後複測**：`spec-index/` 該份仍在且仍為 70,040 bytes；`recon.py` 四個
assertion 全 PASS（129/129 outline 查得，miss=0）；`feature.yaml` 之
`../../spec-index/…` 路徑照常解析，未改為 `inputs/`（R-C11 明文）。

**注意**：`inputs/` 列於 `.gitignore`，該副本從未進版控，故此刪除無 git
歷史可回溯。可回溯者為 `spec-index/cache/` 之同內容檔案與本條紀錄。

## A-CF11 —— "Alternative" vs "Alternate"：以客戶用詞搜尋得 0 命中（判讀陷阱）

> **已升格為條文 R-C13**（下放包 07 §1，Pei 裁定 2026-08-14）。
> 07 §2 明載：06 §3 所防形態（讀不到 → 判 out_of_scope）**不涵蓋本例**，
> 條文有洞，以 R-C13 補。R-C13 與 Privacy **R22-2 同構**，合併處置於下次
> canon re-sync。本條保留為該條文之案例紀錄，適用全 feature。
>
> **升格後之再次應用**：2026-08-14 DR #6／#7 判讀時，Market Configuration
> Table 對 `R1L-R` 與螢幕尺寸皆 0 命中。依 R-C13 換路徑（結構化欄位 →
> 全表 token 掃描 → 037 引用結構），第三路才得出結論。若依零命中下結論，
> 7 節會全判 `out_of_scope`。

**方法論條目，登記供全 feature 參照。**

SR24 §20 標題作 `LATAM Alternative Rear Blower (See CFTS043 for applicable
vehicles)`。依該指示查 CFTS043：

| 搜尋字串 | 主檔（442 頁）命中 | tree view 命中 |
|---|---|---|
| `Alternative Rear Blower` | **0** | **0** |
| `Alternate Rear Blower` | 7 | 10 |
| `LATAM`（該功能相關） | 0 | 0 |

CFTS043 全篇作 "Altern**ate**"，且**從不以 LATAM 標示該功能** —— 其適用性
由 PROXI 參數 `$Indipendent_Rear_Fan$` 決定，非由市場決定。

**若就此收手會發生什麼**：以客戶自己在 SR24 寫的字串搜尋客戶自己的 CFTS043，
得 0 命中，結論會是「CFTS043 未涵蓋此功能」→ 10 節判 `out_of_scope`。
該結論會有完整的依據外觀（查了指定文件、用了文件指定的名稱、留了搜尋紀錄），
而方向完全相反 —— 實測是 10 節全部 `Scope=Yes` 且 `Radio` 含 R1L-R。

**與 06 §3 所防形態之差別**：條文防的是「讀不到 → 判 out_of_scope」。
本例更隱蔽：**不是讀不到，是用錯字串去讀而讀不到**，且錯的字串是文件自己
給的。零命中被當成陰性結果使用，而它其實是索引層事實 —— 與 Privacy R22-2
「以檔名為索引之比對，其陰性結果只能陳述索引層事實」同構。

**可推廣之作法**：跨文件追指標時，不以單一字串定生死。本次改以三路交叉
（功能語義 `Rear Blower` 全列舉 → 篩 `Radio` 含 R1L-R → 讀該批所屬節），
才撞見 "Alternate"。零命中應觸發換路徑，不應觸發下結論。

## A-CF12 —— CFTS043 4803259 之 NOTE 與其自身 metadata 矛盾（上游矛盾）

CFTS043 §1.3.5.1.22 之開頭說明 item **4803259** 全文：

```
The Alternate Rear Blower is a climate system that allows the user to control
the rear fan speed without depending on a Rear HVAC module. Please refer to
{R1 Comfort HMI Logic and Flow} document for HMI requirements.
NOTE: The requirements below are only applicable to R1H starting on SR22.
```

**矛盾三處**：

| 來源 | 陳述 |
|---|---|
| 該 NOTE（散文） | 「below 之需求**只**適用 R1H」 |
| 同一 item 之 `Radio` 屬性 | `R1L-R, R1L, R1H` —— 含 R1L-R |
| tree view 之 `Scope` 欄 | 該節 30 個 item **全部 `Scope=Yes`**（R1L-R 白名單） |

散文說只有 R1H，結構化欄位說含 R1L-R 且在 R1L-R scope 內。**兩者不可能同時
為真。**

### 層級訂正 2026-08-14（下放包 07 §3）—— 上表第三列不得參與選邊

上繳 03 §3.4 曾以「`Scope` 欄是本檔對『什麼在 R1L-R 範圍內』最直接的表態」
為由採結構化欄位。**該理由與 §8.6 不合，已訂正。**

`SYS1_CFTS043-…Tree view_R1L-R scope.xlsx` 是 **SYS.1 階段之 traceability
index export**，非原始 spec 來源；CFTS043 主檔 `.doc` 才是。§8.6：index
export 與原始來源不一致時，**原始來源勝出**。故 `Scope` 欄之地位為
**索引層佐證**，不得凌駕主檔散文。

排除索引層後，矛盾之正確描述是 **CFTS043 主檔內部之矛盾**：

| 層級 | 來源 | 陳述 |
|---|---|---|
| 原始．散文 | 4803259 NOTE | below 之需求只適用 R1H |
| 原始．屬性 | 同 item `Radio` | `R1L-R, R1L, R1H` |
| ~~索引層~~ | ~~tree view `Scope`~~ | 佐證，不參與選邊 |

**同一原始來源內「散文 vs 屬性欄」之矛盾，canon 未涵蓋此形態，無既有規則
可援。**

**後果（07 §3 明載）**：若今日被迫選邊，canon 之重心偏向散文（原始來源之
明文陳述），即偏向 **`out_of_scope`** —— 與上繳 03 所選方向**相反**。
故 R-C12 之降級不只是形式上的保守，而是**修正了一個實質上偏錯方向的暫定值**。

執行層之**行動**全部正確（採結構化欄位、標示為選擇、開 DR、建議緩裁），
判讀結果不必重做；訂正者僅「最直接之表態」一語。

### 現況

10 節 verdict 依 **R-C12** 自 `in_scope` 降為 `undetermined`，
`pending_on` = DR #8。降級**不推翻依據、不否定其結論可能為真**；
`basis` 欄原有依據一字未刪。

**RD-1 候選**（不阻塞，待 D-C10 一併處置；**送出屬 Tier 3**，依 07 §4 宜與
A-CF12 併入 Comfort 之 RD-1 草稿，不單獨發函）：請上游確認 4803259 之 NOTE
是否仍有效；若有效，`Radio` 屬性與 R1L-R scope 白名單為何含 R1L-R。

## A-CF13 —— spec 內部條款標籤碰撞與同條款重複分析（Part N 之輸入）

Layer 3 map 建立時實測所得，兩件皆與 Part N 之切分直接相關，故登記。
**非阻塞**；不改任何 spec、不產 TC。

### 一、`C16.)` 標籤被兩節使用，內容不同

| 節 | 標籤 | 內容 |
|---|---|---|
| 2.15 | `C16.)` | EXTERIOR REAR-VIEW MIRROR DEFROST has on/off state… |
| 16.17 | `C16.)` | If blower reduction occurs automatically due to an… |

ch16 其餘 17 節一律用 `ICE` 前綴（ICE1–ICE15），且 16.17 之內容對應
ch2 的 **`C18.)`**（2.16，同為 blower reduction）。故 16.17 掛 `C16.)`
最可能是誤植，應為 `ICE16.)` 之類。

**影響**：TC 若於 test item 或 reasoning 引用條款標籤，`C16.)` 會指向兩個
不同行為，traceability 出現二義。Phase 4 撰寫 ch16 TC 時須以 **outline
節次**為準、不以條款標籤為準。RD-1 候選（請上游確認標籤）。

### 二、`W0.)` 由三節共用，其中兩節經 037 分析為兩個獨立需求

| 節 | 章 | 037 | 條文 |
|---|---|---|---|
| 17.1 | Home screen - Comfort Widget | 引用，3 leaves（`SWE1-HVAC-124`） | W0 + 交叉參照句 |
| 18.1 | 10.25" Home screen - Comfort Widget | 引用，3 leaves（`SWE1-HVAC-129`） | W0（純句） |
| 19.1 | 7" Home screen - Comfort Widget | **未引用** | W0（與 18.1 **逐字相同**） |

18.1 與 19.1 之 Description **逐位元組相同**；17.1 多一句交叉參照
（指向 Front Comfort/Climate 與 Heated/Vented Seats 兩節）。

037 對 17.1 與 18.1 各產出一個 parent 需求，合計 **6 個 leaves 覆蓋同一條
規範句**（「Comfort widget 有 Comfort 與 Seats 兩個畫面」）。

**影響（Part N）**：若 Layer 2 依章切，ch17 與 ch18 會各得一個 Test Set，
而兩者的首節測的是同一件事。這是分析層起草 Layer 2 時需要知道的事實。
**執行層不就此提出任何 Test Set 主張**（Tier 2，10 §4.3）—— 僅陳述量測。

**與 R-C17 之關係**：R-C17 已定 ch17／ch18 所擁有者僅「Comfort widget 自身
之內容與行為」，首頁管理行為屬 Home Screen spec。本條所指之重複在
**Comfort 自身兩節之間**，不是 Comfort 與 Home Screen 之間，兩者是不同的
問題，勿混。

### 第三項（新增 2026-08-14，下放包 12 §1）—— `HVS1／HVS2／HVS4／HVS5／HVS6` 跨 ch11／ch12 重複

分析層查證 ch11／ch12 是否合併時實測所得。五個條款標籤跨兩章重複，開頭文字
近乎逐字相同：

| ch11 R1 Heated/Vented Seats | ch12 Heated/Vented Seats - CARRYOVER |
|---|---|
| 11.1 `HVS1.` Multi-Level 加熱座椅按壓 | 12.1 `HVS1.` 同 |
| 11.2 `HVS2.` 通風 | 12.2 `HVS2.` 同 |
| 11.3 `HVS4.` climate OFF 時狀態列 | 12.4 `HVS4.` 同 |
| 11.4 `HVS5.` 加熱鍵亮紅 | 12.5 `HVS5.` 同 |
| 11.5 `HVS6.` 參照 HMI Settings List | 12.6 `HVS6.` 參照 HMI Notes |

**與前兩項合計，本 feature 共三處條款標籤衝突。** 三者形態一致：**條款標籤
在 SR24 內不是唯一鍵**，故不可作為 traceability 之引用鍵。

**Part N 之處置（已生效）**：ch11／ch12 **合併**為單一 Test Set
`Heated Vented Seats`（59 leaves）。合併之副效果為正向 —— 近似重複落於同一
Test Set，Phase 4 之 sibling 判定（§4.6）與 `duplicate_of` 得以見效；分立
則兩者分屬兩組，審閱者看不到彼此。

**Phase 4 之一般規則（三項共通）**：TC 之 traceability 一律以 **outline
節次**為引用鍵，不以條款標籤為引用鍵。`specification_reference` 依 §10.7
本就用 `{spec_filename}_{section_id}`，故此問題**不影響工作簿輸出**，
只影響 `reasoning` 與 `test_item` 之敘述（11 §6）。

**RD-1 候選**（不阻塞）：請上游確認三處標籤是否為誤植，特別是 16.17 之
`C16.)`（該章其餘 17 節皆為 `ICE` 前綴，且其內容對應 ch2 之 `C18.)`）。

### 第三項之後續事實（2026-08-15，上繳 07 §4）—— ch11／ch12 全文差異

13 §3 自承：原「無證據顯示進入路徑不同」之結論係讀 `layer3_map.tsv` 之
**60 字截斷標題**得出，違反 R-C18，且屬「以缺席為證據」（R-C13 同構）。
執行層依 13 §4.1 抽出全文並回報事實，**不下結論**：

| 對 | 相似度（`autojunk` 關閉） | 差異 |
|---|---|---|
| 11.1 vs 12.1 | 0.9556 | ① `seats,` → `seats` ② **`opens popup and` → （無）** ③ `LEDs.` → `LEDs (.`（孤立左括號，疑錯字） |
| 11.2 vs 12.2 | 0.9579 | ① `seats,` → `seats` ② **`opens popup and` → （無）** ③ `HI ,` → `HI,` |

**四節之唯一實質差異，是同一個片語 `opens popup and`**：ch11 有、ch12 無。
其餘皆為標點與空白。

操作元件與顯示位置之描述**逐字相同**：皆為 `a press of the heated/vented
seat button`（soft button），循環 HI → MED → LO → OFF，按鈕變色並顯示
arrows/fan 與 LED。**兩者皆未提及任何實體鍵，亦未提及 status bar。**

**判定屬 Tier 2，執行層未判**。`opens popup` 可能表示不同進入路徑（中介
彈窗）、可能是同一入口下之回饋、也可能是 carryover 章漏寫；三者無法由措辭
斷定。**關鍵缺料為 HMI Pop Up List**（`paths.popup_list` 為 null），
已登 `DATA_REQUESTS.md` #11。

若複核後結論翻轉，`Heated Vented Seats`（59 leaves）拆回兩組，屬 Part N
變更，回分析層重簽（13 §3）。**該項僅阻塞此組，不阻塞 pilot**
（`Seat Control Tab`）。
