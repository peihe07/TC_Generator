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
