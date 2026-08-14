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
| A-CF06 | 環境 | `pymupdf` 未安裝，spec PDF text-layer 探測無法執行 | OPEN | 無（spec_mode A 之文字權威為 SYS1 export） |
| A-CF07 | 範本殘留 | 空白範本第 10–11 列樣本資料須於 write-back 清除 | OPEN（P4 前處理） | P7 交付 |
| A-CF08 | 覆蓋缺口 | SR24 **基線內** 51 節未被 037 引用；17 節 substantive 已判讀（10 in_scope／7 undetermined） | OPEN（處置待 D-C10） | 無 |
| A-CF09 | 稽核（跨 feature） | **home／projection／privacy** 三者之 Sign-off 為空白範本（範圍已限縮） | OPEN（另案，不回溯補簽） | 無 |
| A-CF10 | 來源重複 | `inputs/` 曾存在 SR24 export 副本，依 R-C11 刪除 | CLOSED（已刪，已留痕） | 無 |
| A-CF11 | 判讀陷阱 | SR24 作 "Alternative"、CFTS043 作 "Alternate" —— 以客戶用詞搜尋得 0 命中，差點誤判 10 節為 out_of_scope | OPEN（方法論，供全 feature 參照） | 無 |
| A-CF12 | 上游矛盾 | CFTS043 4803259 之 NOTE 稱「only applicable to R1H starting on SR22」，與同批 item 之 `Radio` 含 R1L-R 及 `Scope=Yes` 相矛盾 | OPEN（RD-1 候選，待 D-C10 一併處置） | 無 |

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

**未驗事項，不宜當成已驗**：目前**無法**陳述「SR24 PDF 具 text layer」。
若 Phase 4 需要自 PDF 取圖說或座標，此項先補（`pip install pymupdf` 後重跑
recon 即可，無需改碼）。專案無 requirements 檔宣告此相依，一併登記於
`DATA_REQUESTS.md`。

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

**本次判讀採結構化欄位**（`Scope=Yes` + `Radio` 含 R1L-R），理由：`Scope`
欄是該 workbook 為 R1L-R 專門建立之白名單（sheet `工作表1`，599 筆），是
本檔對「什麼在 R1L-R 範圍內」最直接的表態；而該 NOTE 之措辭
（"starting on SR22"）看似是歷史沿革註記，可能未隨 R1L-R 納入而更新。

**但這是選擇，不是推導。** 若 NOTE 為準，10 節應為 `out_of_scope`。
`data/sr24_substantive_applicability.tsv` 之 `in_scope` 判定即繫於此選擇，
D-C10 裁定前應知悉。

**RD-1 候選**（不阻塞，待 D-C10 一併處置）：請上游確認 4803259 之 NOTE
是否仍有效；若有效，`Radio` 屬性與 R1L-R scope 白名單為何含 R1L-R。
