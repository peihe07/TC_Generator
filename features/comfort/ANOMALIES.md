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
| A-CF02 | note | 客戶交付夾之 spec 為 SR25，與 R-C1 基線不一致 | **已知不一致，以交付說明標示基線**（Pei 2026-08-16 追加裁定：**SR25 兩檔不移除**，推翻 79 §3 之「移除」；**不轉 RESOLVED**）| 無（不影響 pipeline 取材）；夾內同時存在 SR24 與 SR25，其分辨由交付說明承載 |
| A-CF03 | 結構 | 34 列 parent 形態卻為 Functional Requirement | RESOLVED by R-C3 | 無 |
| A-CF04 | 工具 | `intake.py` 只掃 drop folder，spec_mode 提案偏低 | OPEN（已知限制，非缺陷） | 無 |
| A-CF05 | 工具缺陷 | `intake.py` 需求清單靜默漏計 57 列（346 vs 403） | FIXED 2026-08-14 | 無 |
| A-CF06 | 環境 | `pymupdf` 未安裝 → recon 改用 `pdftotext` fallback；SR24 PDF 具 text layer | **CLOSED**（09 §4 授權，已實作） | 無 |
| A-CF07 | 範本殘留 | 空白範本第 10–11 列樣本資料須於 write-back 清除 | **CLOSED 2026-08-15**（Pei 於 Excel 四項確認通過） | 無 |
| A-CF08 | 覆蓋缺口 | SR24 **基線內** 51 節未被 037 引用；17 節 substantive 已判讀（4 in_scope／13 undetermined），4 節依 R-C16 為 RD-1 覆蓋缺口項 | OPEN（10 節 DEFERRED、3 節待 DR #6） | 無 |
| A-CF09 | 稽核（跨 feature） | **home／projection／privacy** 三者之 Sign-off 為空白範本（範圍已限縮） | OPEN（另案，不回溯補簽） | 無 |
| A-CF10 | 來源重複 | `inputs/` 曾存在 SR24 export 副本，依 R-C11 刪除 | CLOSED（已刪，已留痕） | 無 |
| A-CF11 | 判讀陷阱 | SR24 作 "Alternative"、CFTS043 作 "Alternate" —— 以客戶用詞搜尋得 0 命中，差點誤判 10 節為 out_of_scope | **已升格 R-C13**（案例保留） | 無 |
| A-CF12 | 上游矛盾 | CFTS043 4803259 之 NOTE 與同 item `Radio` 屬性矛盾（**主檔內部**矛盾；tree view 為索引層，不參與選邊） | **DEFERRED**（10 §2，Pei 直接向 RD 反應） | 無 |
| A-CF26 | **跨 feature（範本）** | 通用空白範本 `SWQT_20260121` 之資料工作表，**P 欄下拉（優先級）之 DV `sqref` 僅 `P10:Q11`**，`T–Z` 與 `AF` 同；B 欄編號公式與 R 欄下拉止於 row 59。**非 Comfort 之產物，凡以該範本為母本者皆然** —— **privacy 以同一份範本交付 11 條（row 10–20），其 row 12–20 之 P 欄同樣無下拉約束，且該檔已交付** | OPEN（**RD-1 候選**，DATA_REQUESTS #36，**High**）；依 R-C21 登於本帳並具名對象。**privacy 側已於 2026-08-15 唯讀實測**（`ad595ed0…`，11 列，`P10:Q11`，row 12–20 受影響），**未寫入該 feature 任何檔案** | Comfort：DR #35 之同源，寫回產物於範本擴充前不可交付。privacy：**處置由 Pei 決定是否回溯**，本 pipeline 未動其任何檔案 |
| A-CF25 | spec 內部瑕疵 | `16.2`（ICE1）之「with the exception of the recirculation led in climate off (**see ICE11.**)」—— **ICE11 為 `16.12`（Airflow Modes has 5 states），不含 recirculation LED 之任何規則**；該規則實在 **ICE9（`16.10`）**「When climate is OFF, the recirculation LED of the hard control is on」。**條文之交叉引用指錯節** | OPEN（**不列 RD-1** —— 與 A-CF13 同類之 spec 內部瑕疵，不阻塞）| `NR1L-ComfortHMI-083` 只驗 ICE1 自身所述之例外（畫面不反映該變更），不依該誤引取用 16.10 之內容（§8.2.1） |
| A-CF24 | 量測範圍 | 上繳 30 §5.3 以 `find . -maxdepth 3` 於 repo root 找 037 得零命中，據以記「不可達」；實際路徑 `features/comfort/inputs/…` 深度為 4。**pattern 對，深度不足** | **RESOLVED**（42 §4，037 已讀，名單已重建）| A-CF23 之 18 leaf 清單延後一輪；無 TC 受影響 |
| A-CF23 | 讀取能力 | **spec 內以圖承載之內容，本 pipeline 讀不到**（標題與範圍 2026-08-17 擴充，88 §6）：**037** 之 52 個圖片標記（25 leaf）；SYS1 export 之 `section_fulltext.tsv` 0 命中；**`15.1` 之 `chart below`**（profile §5.4 第五項成員）| OPEN（**不列 RD-1**；DR #23 為工具需求，Low）| 已生成之 7 條逐條複查完畢，見本條之影響清單；其餘 18 leaf 之檢查落為 `RUNBOOK.md` 生成時必答項 |
| A-CF22 | note | 3 旋鈕 ICS 車輛之 head unit 是否仍顯示座椅類 popup，spec 未述 | OPEN（**不列 RD-1** —— 在 Comfort spec 範圍外）| 無（`-002` 維持不補）|
| A-CF21 | 條文衝突 | `2.1` 之 037 leaf（3 tabs，無 Massage）與條文（4 tabs，含 Massage）不符 | **RESOLVED-BY-RULING**（R-C33，2026-08-15）；**DR #18 為其 RD-1 候選** | 內容依條文、單位依 037；`-01`／`-02` 另因 DR #17 未生成 |
| A-CF20 | note | `SWE1-HVAC-024-07` 拆後四條之 ER 逐字相同，僅 title 與 procedure 相異 | **維持**（32 §3；已知性質，非缺陷）| 無 |
| A-CF19 | 交付件呈現 | 多節 specification_reference 之儲存格呈現未實測（約 240 字元，列高 14.0） | OPEN（下次寫回時實測）| 無 |
| A-CF18 | 條文缺口 | `3.3` 未定義 `not available` 之可觀察形態 | OPEN（**RD-1 候選**）| `-030` 之 ER 停在 `are not available` |
| A-CF17 | 條文缺口 | `3.4` 之 `when configured` 無受詞 | OPEN（**RD-1 候選**）| 無（`-031` 已迴避該詞）|
| A-CF16 | 交付件呈現 | 14 列全部 `customHeight=True, height=14.0` 而 `wrapText=True` —— 折行但不長高，列表視圖只見首行 | **RESOLVED**（方向 3，Pei 2026-08-15）| 無 |
| A-CF15 | note（spec 缺口） | ch13 從未說明腰靠／側靠調整量顯示於何處 —— 可觀察量僅間接可得 | OPEN（RD-1 候選，不阻塞） | 無 |
| A-CF14 | 跨 feature 稽核 | `features/home/feature.yaml` 之 `done_region.author_value` 為 `Arif`，實際 done region 為 `ArifChen` —— 以前者選取得 0 列 | OPEN（另案，不逕改 home） | 無 |
| A-CF13 | spec 內部瑕疵 | **四項**：`C16.)` 跨 2.15／16.17；`W0.)` 跨 17.1／18.1／19.1；`HVS1/2/4/5/6` 跨 ch11／ch12；**12.1 之 `LEDs (.` 孤立左括號** | OPEN（RD-1 候選，非阻塞） | 無 |

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

~~**執行層未複測**：該交付樹於本 session 之檔案系統不可達（已搜尋，無
`10_Reviewing` 路徑）。~~ —— **該判斷為搜尋範圍所致之誤判**，見下 §「零命中之
成因」。

---

### 現況（Pei 追加裁定，2026-08-16）—— **不轉 RESOLVED**

79 §3 曾裁「移除交付夾內之 SR25 兩檔」，執行層據以回報其檔名與 bytes
（`…SR25 Post 3A CR29359 (Feb 24 2025).pdf` 14,538,298；
`SYS1_…_SR25_…xlsx` 74,545）。**該裁定於 2026-08-16 被推翻：兩檔不移除。**
同夾之 `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf`
（3,560,705 bytes）亦留置。

故本項**不轉 RESOLVED**，改記為 **「已知不一致，以交付說明標示基線」**：
夾內同時存在 SR24 與 SR25，而**本次交付之基線是 SR24 CR24879
(September 25 2023)** —— 該事實由交付說明之一句承載，
使評閱方不必自檔名推測（見 `docs/Comfort_HMI_delivery_note.md`）。

**其重審條件不變**：若日後基線改採 SR25，須先推翻 R-C1。

**為何不是 RESOLVED**：不一致仍在，只是**被標示了**。
把「已標示」記成「已解決」，會使下一個讀這一列的人以為夾裡只有 SR24。

---

### 前次裁定（選項 1，Pei 2026-08-15；下放包 27）—— 已被上節部分推翻

**裁定**：交付夾之 spec 附件改為 SR24 CR24879，與 037 及工作簿一致。

037 之 HMI Source ID 於 2026-08-15 重測（`Analysis Report` row 8–505，
A 欄非空 498 列）：相異檔名 stem **僅 1 個**，即
`SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`。
無 SR25、無空值、無例外。**037 本身沒有模稜兩可**；矛盾只在交付夾之附件。

**執行層已做（增量、可逆）**：複製兩檔至交付夾，保留原檔名，複製後以
`cmp` **逐位元組**比對來源與目的地（不以檔名或大小標籤代替，R-C14）：

| 檔案 | 來源 | bytes | cmp |
|---|---|---|---|
| SR24 PDF | `spec-index/sources/` | 6,462,311 | identical |
| SR24 SYS1 export | `spec-index/cache/` | 70,040 | identical |

**待 Pei 執行（Tier 3，客戶樹之移除）**：

- `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf`
- `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx`

兩份**非資料遺失** —— `spec-index/sources` 與 `cache` 皆留有其副本。
採**先放後移**：任一時點交付夾內至少有一份完整之 spec。

**`BASELINE.sha256` 不變** —— 其涵蓋範圍為 pipeline 之來源檔（R-C20），
交付夾附件不在其列。已複驗 8 檔全 OK。

### 零命中之成因（登記供他案參照）

原條目寫「該交付樹於本 session 之檔案系統不可達（已搜尋）」。**該搜尋只掃
了 repo 內**（`find .` 自 `TC_Generator/`）。交付樹實際位於
`~/Work/02_Project_R1LR/10_Reviewing/…`，**在 repo 之外**，本輪擴大搜尋範圍
後一次命中。

**零命中被當成「不存在」，而它其實只是「不在我搜的地方」** —— 與 R-C13
同一形態。原條目自己寫了「宜於可觸及交付樹時重測」，那句是對的；錯的是
「不可達」這個結論下得太早。

### 重審條件

**若日後基線改採 SR25**（需先推翻 **R-C1**），本項須同步重做 ——
交付夾附件、`feature.yaml` 之 `sys1_export`／`spec_pdf`、
`data/section_fulltext.tsv` 與全批 `specification_reference` 皆須一併換基線。
本項之處置繫於 R-C1，**不獨立成立**。

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

**2026-08-15 由 `ch16_mirror_map.tsv` 獨立復現**（下放包 37 §7）：
逐節建鏡射表時再次撞見同一撞號 —— 該表以 `16.17 ↔ 2.16` 為 `mirrored`
（全句逐字相同），而 `16.17` 掛 `C16.` 與 `2.15` 相同。
**不新登 anomaly**，於此增記。

**復現本身是證據**：同一撞號在**兩條不相干的作業路徑**上各被撞一次
——第一次由 Layer 3 map 之標籤掃描（下放包 20），第二次由 ch16 鏡射之
逐節比對（本輪）。表示它不是邊緣情形，**Phase 4 全面展開時會反覆出現**。

故本項之處置（**一律以 outline 節次為引用鍵，不以條款標籤為準**）
更應被機械強制。**已列為候選 gate；本包不加** —— 目前無任何一條 TC 以
條款標籤為引用鍵（實測 65 條之 `specification_reference` 皆為
`{STEM}_{outline}` 形式），無實例違反，加 gate 即為對尚未發生之事設檢查。

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

### 第四項（新增 2026-08-15）—— `12.1` 之 `LEDs (.` 孤立左括號

前三項為**標籤**衝突，本項為**字元**層級之瑕疵，一併登記於此，因其同樣
只有讀全文才看得見。

`12.1`（`SWE1-HVAC-067`，`HVS1.`）之原文片段：

> …the soft button highlights red and the control displays 3 arrows, HI
> and/or LEDs **(.** The next button press sets the seat to MED…

對照 `11.1` 之同位置：

> …the control displays 3 arrows, HI and/or LEDs**.** The next button press…

**`(` 為孤立左括號**，其後直接接句點；實測全節左括號 1 個、右括號 0 個。判為誤植 ——
最可能是編輯時刪去括號內文字而漏刪左括號本身。

**影響評估**：

- **對 TC 內容：無。** 該字元不改變條文語意，`12.1` 之行為敘述與 `11.1`
  在此處相同（皆為「顯示 3 arrows、HI 與／或 LED」後結束該句）。
- **對逐字比對：有。** 它是 `11.1` vs `12.1` 三處差異之一，若以字串相等
  判斷兩節是否等價，此節會被判為不等。本次比對已將其與實質差異
  （`opens popup and`）分開陳述，未混為一談。
- **對 Phase 4 之引用：需注意。** 若 TC 之 reasoning 逐字引用該句，
  應**照錄原文**（含該括號）或明確標示為節錄，不得靜默修正 ——
  修正 spec 原文不是 TC 作者之權限（§8.4.2）。

**RD-1 候選**（不阻塞）：與前三項併同回報，請上游確認是否為誤植。

### 四項之共通歸納

| # | 項目 | 層級 | 唯有讀全文／逐字比對可見？ |
|---|---|---|---|
| 1 | `C16.)` 跨 2.15／16.17 | 標籤 | 否（標題即可見） |
| 2 | `W0.)` 跨 17.1／18.1／19.1 | 標籤 | 否 |
| 3 | `HVS1/2/4/5/6` 跨 ch11／ch12 | 標籤 | 否 |
| 4 | `12.1` 之 `LEDs (.` | 字元 | **是** —— 位於第 174 字元，遠在 60 字截斷之後 |

第 4 項是 R-C18 之另一個佐證：它不在標題裡，任何以截斷欄位為輸入的比對
都看不到它。前三項可由標籤發現，第四項不能。

## A-CF07 —— CLOSED 2026-08-15

`output/…_SWQT_Comfort_20260815_prepared.xlsx`（SHA256 `b68117a211b08009…`）
經 **Pei 於 Excel 開啟**，四項確認全數通過（下放包 18 §1）：

1. 無修復提示
2. R 欄下拉可用且為九項
3. D5 Scope 正確
4. 第 10–11 列已清且無殘留列號

程式層檢查（48 members、DV counts、五格清空、B 欄公式完整）已於上繳 09b
記載，**但那些不能代替 Excel 自身之檔案完整性判定** —— 兩端俱備方為完整。
此為 Comfort 首次確認 zip-level surgical path 於本 feature 可行。

## A-CF14 —— `features/home/feature.yaml` 之 author_value 與實際不符（跨 feature 稽核）

**登記依據**：下放包 17 §1（G-1 執行時發現）。

| 項 | 值 |
|---|---|
| `features/home/feature.yaml` | `done_region.author_value: Arif` |
| 實際（`forms/…_Home_20260809.xlsx` Z 欄） | **`ArifChen`** |
| 以 `Arif` 選取 | **0 列** |

**危險形態**：0 列之母體會產出「全數不含 modal」之結論 —— 一個看起來像
結論的空集合。G-1 之母體列數 assertion（== 144）擋下此事，此為
「檢查項須確認其在該階段確實可能失敗」之正例。

**FORMS.md 已獨立記載同一事實**（其 provenance warning 第 2 點：
「`Z` = `ArifChen` breaks the Home done-region selector … 這是 feature.yaml
變更加上新基準雜湊，不是靜默編輯」）—— 兩處各自發現，結論一致。

**不逕改 home**（17 §5.3）。**執行層另回報一項路徑問題**：17 §5.3 要求
「於 `features/home/DATA_REQUESTS.md` 開列」，但**該檔不存在**，開列即須
新建檔案，而同句又要求「不逕改 home 之任何檔案」。兩者衝突，故本輪
**未動 home 任何檔案**，擬列之內容備於上繳 10 §2.3，待裁示後補。

## A-CF15 —— ch13 未說明腰靠／側靠狀態顯示於何處（note）

**登記依據**：下放包 20 §5。

13.2 ~ 13.6 命名了 `Seat Control Popup`、`Seats tab`、`level`、`greyed out`、
`error tone`，**但未指明調整量顯示於何處**。

| 已命名之可觀察量 | 出處 |
|---|---|
| `Seat Control Popup`、`Seats tab` | 13.2 |
| `the selected option` | 13.3.1 |
| `level`、`grey out`、`error tone` | 13.6 |
| **調整量之顯示位置** | **無任何節提及** |

**與 19 §4.2 之關係**：13.5 之級距**量值**由 CFTS044 擁有（已判 out of
scope）；本條所指者不同 —— 是**顯示位置**，而該資訊**無任何 spec 明載**，
CFTS044 亦未被指為其擁有者。

**不阻塞**：20 §4 之修法已使 ER 不依賴該資訊 —— ER 之主詞改用各節自身之
動詞（13.3 之 `reflected`、13.5 之 `increase`／`decrease`），
`level` 僅保留於 13.6（該節唯一使用該詞者）。

**RD-1 候選**：請上游確認腰靠／側靠之調整狀態是否有規定之呈現位置。

**界線（R-C22）**：若日後實機驗證顯示確無任何可讀之狀態呈現，
13.5 方回到 BLOCKED 之候選 —— 屆時之理由才是「本 ECU 無任何可觀察端」，
而非「值不知道」。

## A-CF16 —— 交付件列高：列表視圖只見首行（RESOLVED 2026-08-15）

**現象**：目標列 row 10–23 全部 `customHeight=True, height=14.0`，
而 I／J／L／M／AH 皆 `wrapText=True`。Excel 於此組合下**折行但不長高**，
故多行內容於列表視圖只見首行。**儲存格值完整，點選即見。**

**成因非本 pipeline** —— 空白範本 `SWQT_20260121` 原本即如此；
A-CF07 之清列只動五格值，未動列高。

### 判定規則之兩半（23 §2）

| | 內容 | 結果 |
|---|---|---|
| 前半（可證，執行層實測） | 既有交付件是否同樣受限 | **是** —— Privacy 與 Comfort 同用空白範本、欄寬完全相同、皆 `height=14.0`。Privacy 之受限檔即其實際交付件（`DELIVERY.sha256` ENTRY 003 標「已交付」，hash 與量測對象逐位元組相符）。home／SXM 起自已調版 instance，不構成反例 |
| 後半（repo 外，執行層無從驗證） | 是否未見客戶反映 | **是** —— Pei 2026-08-15 答「沒有」：Privacy 交付件交出後，評閱方未曾就列高或內容需點選儲存格方能閱讀提出意見 |

**兩半皆滿足 → 採方向 3（維持現狀）。** 不改動範本列高、不清除
`customHeight`、不逐列設定顯式高度。

**依據（不對稱錯誤成本）**：方向 1／2 改動範本呈現，影響及於日後所有
feature，而本案無支撐該擴大之證據；方向 3 之代價為一項已知、已記錄、
且有同範本已交付前例之可讀性損失。

**R-C27 已消除其中最嚴重的一段**：BLOCKED row 之 Remarks 首行現為
`[BLOCKED-SPEC] Owner: …`，marker 與擁有者皆在可見範圍內。餘留者為長
procedure／ER 之列表視圖只見首行。

### ⚠️ 重審條件

**本裁定成立於一個當下為真的事實，非永久性質。**

**若評閱方日後就列高、或就「內容需點選儲存格方能閱讀」提出意見，
本裁定即需重審** —— 屆時方向 1／2 之取捨須重新衡量，且其影響及於
所有以空白範本 `SWQT_20260121` 產出之 feature（現含 Privacy 與 Comfort）。

重審之觸發者為外部意見，**不由本 feature 自行判斷**；執行層於察覺該類
意見時登記並回報，不逕行改動。

## A-CF17 —— `3.4` 之 `when configured` 無受詞（條文缺口，RD-1 候選）

**登記依據**：下放包 31 §3.1；來源為執行層上繳 19 §11 第 1 項。

條文（`data/section_fulltext.tsv`，未截斷）：

> C22.) For soft top vehicles such as JL/JT, **when configured**, the rear
> defrost button will not appear when not present in the vehicle.

**搜尋範圍（R-C30）**：根目錄 `features/comfort/data/section_fulltext.tsv`
（129 節全文），pattern `configured`，**命中 3 處**：

| 節 | 用法 | 可否還原受詞 |
|---|---|---|
| 3.4 | `when **configured**,` | **否 —— 無受詞** |
| 6.3 | `**configured** with a non-foldable secondary lower screen` | 是（配備該螢幕）|
| 11.11 | `**configured** with hard buttons for comfort controls` | 是（配備硬鍵）|

另兩處皆為 `configured with X`（配備 X）之形式；3.4 之 `when configured`
**無受詞**，無法以同一讀法還原。

**處置**：登記，**不推測其所指**。`-031` 之 PC 不寫入任何配置步驟
（§8.4.1），該 TC 內容不因本項變動 —— 它已迴避該詞。

**RD-1 候選**：若該詞實質改變適用條件（例如「僅在某選配開啟時才適用」），
本 TC 之適用範圍即需收窄。**不阻塞生成**，但需上游澄清。

## A-CF18 —— `3.3` 未定義 `not available` 之可觀察形態（條文缺口，RD-1 候選）

**登記依據**：下放包 31 §3.2；來源為執行層上繳 19 §11 第 2 項。

`3.3`（C21）全文僅一句，只說 `available`，**未說不可用時之外觀**。
`greyed out` 之描述在 **2.10**（C11），屬 `Climate Modes` 這個 Test Set，
依 §8.2.1 不得於 3.3 之 TC 內驗證。

故 `-030` 之 ER 停在 `are not available`，**其判定實際仰賴測試員對
「不可用」之理解**。

**取捨**：寫得更具體就會踩進 2.10。**越界之害大於措辭之弱** —— 前者是
驗證了不屬於本節之行為（且 2.10 之明文與初稿之寫法相牴觸，見上繳 19 §3），
後者是判定粒度不足但範圍正確。

**處置**：登記；`-030` 之 `reasoning` 具名 2.10 為該外觀之擁有者。
列 RD-1 候選 —— 上游若補明 3.3 之不可用外觀，本 TC 之 ER 即可收緊。

## A-CF19 —— 多節 `specification_reference` 之儲存格呈現未測（交付件呈現）

**登記依據**：下放包 31 §3.3；來源為執行層上繳 19 §11 第 3 項。

`-029`／`-030`（3.3 之兩條）之 N 欄為**三段以 `; ` 分隔、各帶完整 stem**
之字串，長度約 **240 字元**。而交付件之列高為 `14.0` 且 `wrapText=True`
（[[A-CF16]]），即折行但不長高。

**本項現為未測，非已測** —— 本批不寫回，故該欄在 Excel 內之實際呈現
無人看過。R-C29 之多節格式是本輪才出現的，A-CF16 當時之量測不涵蓋它。

**處置**：**於下次寫回時一併實測**該欄之呈現（列高、可見字元數、
是否須點選儲存格方能讀完），結果併入 A-CF16 之重審依據。

**與 A-CF16 之關係**：A-CF16 之裁定（方向 3，維持現狀）成立於
「同範本已交付前例受同樣限制且未見評閱方意見」。**本欄比當時量測過的
任何一欄都長**，故它可能是 A-CF16 重審條件之第一個觸發者。

## A-CF20 —— 拆後四條之 ER 逐字相同（note，維持）

**登記依據**：下放包 32 §3；來源為執行層上繳 20 §11 第 2 項自報。

`SWE1-HVAC-024-07` 依 §8.2.2 之控制實體判準拆為四條
（`NR1L-ComfortHMI-024` … `-027`）。四條之 `expected_result` **逐字相同**：

```
1. The "MAX DEF" button is active
2. The "MAX DEF" button is no longer active and the system is in the
   previous manual mode with A/C on
```

**係條文使然** —— 四個破壞源之後果在 C20 為同一句
（`... breaks MAX DEF (turns MAX DEF off) and the system goes back to the
previous manual mode with the A/C on`）。

區別由 `tc_title`（帶破壞源 token）與 `test_procedure` 第 2 步承擔。

**不改**：§4.3 之 sibling-distinction 要求 `tc_title` 可區分，已滿足；
§6 要求 ER 涵蓋完整結果，而結果本就相同。**強行使 ER 相異即為造值**
（§8.4.1）。

**登記之目的**：供日後**只掃 ER 欄之審閱者**查考 —— 四列 ER 一模一樣，
在工作簿內看起來像複製貼上的疏漏，實際是條文的形狀。

**相關**：[[A-CF16]]（列高使長欄只見首行）在此處反向作用 —— 四條之 ER
短且相同，列表視圖反而看得完整，而看得完整正是它容易被誤讀成疏漏的原因。

## A-CF21 —— `2.1` 之 037 leaf 與條文數字不符（條文衝突，RD-1 候選）

**登記依據**：執行層批次 3 實測，上繳 21 §3.2。

| 來源 | 內容 |
|---|---|
| 條文（`data/section_fulltext.tsv`，來自 SYS1 export）| `The comfort category will have **up to 4 tabs** …` 順序 `Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati), **Massage**, Rear` |
| 037 leaf `SWE1-HVAC-001-01` | `up to **3** tabs displayed depending on vehicle configuration` |
| 037 leaf `SWE1-HVAC-001-02` | `tabs displayed in order: Front, Seats, Rear`（**無 Massage**）|

037 之兩個 leaf **系統性地少了 Massage tab**。

**現行條文未涵蓋此衝突**：§8.6 定「source spec wins over index export」，
但 **037 不是 index export，它是 SWE.1 之分析報告**，而 R-C1 所定之驗證
單位正是 037 之 leaf。spec 與其索引之優先序有規則；**spec 與上游分析之
優先序沒有**。

**執行層未自行取捨**，因為兩種取法產生不同的 TC 數與不同的 `test_item`：
取條文須驗 4 個 tab 含 Massage，取 leaf 則 3 個。

**條文自身另有一句指向委派**：`Refer to separate HMI Logic and Flow
documentation for Massage Seats logic` —— Massage 之**邏輯**確實委派他處，
但 tab **是否存在**是 2.1 自己說的。**委派的是行為，不是存在。**

**阻塞範圍**：`SWE1-HVAC-001` 之 3 個 leaf。該 3 個 leaf 另有一項獨立的
軸問題（`only Front climate is available` 不在十一軸內，見上繳 21 §3.1），
**兩者須各自裁定，解其一不足以解除阻塞**。

---

### RESOLVED-BY-RULING（R-C33，2026-08-15；下放包 33 §1）

**處置已定，不再等待答案**：

```
一、何者算一個需求單位（leaf 之切分、數量、id）—— 037 為權威（§8.2）
二、該需求說了什麼（數值、列舉、順序、條件）—— spec 條文勝（§8.1），
    並列 RD-1 呈報該落差
三、內容依 spec 而 leaf 依 037 時，該 leaf 之 TC 依 spec 內容撰寫，
    req_id 仍為該 leaf；reasoning 須具名此落差與其 RD-1 編號
```

**適用於本項**：leaf 維持 `-01`／`-02`／`-03` 三個（037 之切分），
內容依條文之 **4 tabs 含 Massage**。

**我原判「現行條文未涵蓋」，對 §8.6 而言正確而不完整** —— §8.6 管 spec
與其索引導出，不管 spec 與上游分析；但 **§8.1「Conflict → Req wins;
flag RD」**與 §8.2 併讀即得分工，我當時未把兩條併起來讀。

**RD-1 候選為 `DATA_REQUESTS.md` #18**（037 與 spec 對齊），**不阻塞**
—— 呈報之目的為使兩者對齊，非等待答案才能開工。

### 仍未解者，與本項不同一件事

`-01`／`-02` 之不可生成**不是**本項所致。即使 037 與條文完全一致，
條文仍只寫 `depending on vehicle configuration` 而未述**何種配置產生
何種 tab** —— 那是**內容不足**（`DATA_REQUESTS.md` **#17**，High，
阻塞該 2 leaf），與本項之**內容衝突**是兩回事。

**解 A-CF21 不解 #17。** `-03` 於第十二軸增列後已生成
（`NR1L-ComfortHMI-041`）。

相關：[[A-CF17]]、[[A-CF18]]（同為條文缺口類）。

## A-CF22 —— 3 旋鈕 ICS 車輛之座椅類 popup，spec 未述（note）

**登記依據**：下放包 35 §3；來源為執行層上繳 23 §1.3(d) 自陳「本次判斷中
最接近邊界者」。

`NR1L-ComfortHMI-002` 之 ER 為 `The Seat Control Popup is displayed on the
head unit`。2.14 之逐字範圍為
`no **HVAC** menu bar icons, no **HVAC** screens and no **HVAC** pop ups`
—— Seat Control Popup 非 HVAC popup，故 **`-002` 維持不補**。

**把 2.14 讀成「head unit 什麼都不顯示」是反向的範圍造值**（§8.4.2）——
以外部條文擴張出一個它沒說的限制，與以外部條文擴張測試範圍同性質。

**未述者**：3 旋鈕 ICS 車輛之 head unit 是否仍顯示座椅類 popup。
spec 未述，本 pipeline 不推測。若日後實機顯示不然，`-002` 須補一行排除式 PC。

**不列 RD-1** —— 該問題屬 head unit 整體行為，在 Comfort spec 範圍外，
問了也不在 037 之權責內。登記之目的為使該判斷可覆核，非為索取答案。

相關：[[A-CF17]]、[[A-CF18]]（同為 spec 未述類，但那兩者在 Comfort 範圍內
故列 RD-1）。

## A-CF23 —— **spec 內以圖承載之內容，本 pipeline 讀不到**（讀取能力）

**標題與範圍於 2026-08-17 擴充（下放包 88 §6）**。原標題為
「SYS1 export 之圖片內容不可讀」，其字面只涵蓋 037／export 之圖片標記。
盤點 129 節之外部參照時（上繳 67 §1.4）冒出第四種情形 ——
`15.1` 之 `follow the **chart below**` 指向**本 spec 內之圖**，
既非「外部文件未取得」，亦非「遍尋不著」，原標題容不下它。

**現行範圍**：

| 成員 | 內容 |
|---|---|
| 037 之 Requirement Description | **52 個圖片標記，涉 25 個 leaf** |
| `section_fulltext.tsv`（SYS1 export）| 圖片標記 **0 個** —— 圖根本沒有進到文字裡 |
| **`15.1` 之 chart** | 條文明寫 `follow the chart below`，該 chart 為圖；其對照（某功能進入／退出 → 顯示哪一個 popup）**無任何 TC 驗證**，且不得由 TC 作者自行補（profile §5.4 之第五項成員，56 §3 已記）|
| `12.7` | `images should be shown in full…` —— **呈現要求而非對照表**，不構成缺口 |

**其性質與「外部文件缺件」相反，此區分須明記**：
東西就在我方所引之 spec 裡，**缺的是讀取能力而非文件**。
不記這一句，它會被誤讀為又一件缺件，而缺件是上游之事、讀不到是我方之事。



**登記依據**：下放包 40 §5；來源為執行層上繳 28 §10.5。

**登記時須先訂正一項事實**：上繳 28 §10.5 與下放包 40 §5 皆記為
「`10.2` 之三張圖片於 `section_fulltext.tsv` 僅存檔名」。**實測不然** ——

| 來源 | `(image:` 命中 |
|---|---|
| `data/section_fulltext.tsv`（SYS1 export 導出）| **0** |
| **037 之 Requirement Description**（`SWE1-HVAC-045` 等）| **52 個標記，分布於 25 個 leaf** |

**圖片標記在 037（SWRA 分析報告）內，不在 SYS1 export 之條文內。**
我當初讀到那三個檔名是在 037 之 leaf 描述裡，卻寫成 `section_fulltext`
—— 兩份文件混記。**現況為 037 之圖片內容不可讀。**

**影響**：`NR1L-ComfortHMI-068` 只驗三狀態之存在與循環，**不驗其視覺呈現**。
若圖片載有各狀態之圖示規格（如 AUTO ECO 之圖形與 AUTO ON 之差異），
**該部分現無任何 TC 涵蓋**。

**不得以「圖片可能只是示意」為由略過** —— 那是未經查證之假定。
現況為**不可讀**，如實記之（下放包 40 §5 明示此點）。

**不列 RD-1** —— 圖片存在於 spec 內，**非上游遺漏**；問題在本 pipeline 之
讀取能力。列 `DATA_REQUESTS` **#23**（Low）：SR24 PDF 之圖片擷取工具。

**範圍已實測**：037 全 403 leaf 掃 `(image:` —— **25 個 leaf、52 個標記**，
遠不止 `10.2` 之三張。命中最多者為 `SWE1-HVAC-023`（6）、`-055`（5）、
`-001`／`-044`／`-045`／`-083`（各 3）。

**其中已生成者，登記時記為 2 個（`-023`／`-076`），42 §4 重測為 7 個**
（`-001`／`-010`／`-023`／`-044`／`-045`／`-053`／`-076`）—— 即現有 TC 中
已有 12 條，其上游 leaf 描述帶有讀不到的圖片。此範圍遠大於登記時所知。
**圖片標記位於 037 之 129 個 parent 列**（section 級 Requirement
Description），與 outline 節次 1:1。

### 影響清單（41 §5 之逐條複查，名單於 42 §4 重建）

問句：**該 TC 所驗之行為，是否有任何部分依賴圖片所載之內容？**

> **事實訂正（2026-08-15）**：上繳 29 §5 與 30 §5 皆記為「已生成者為
> `-023` 與 `-076` 兩個」。**實測不然：已生成者為 7 個**（下表）。
> 037 於本 session 已可讀（路徑見本條末），25 個帶圖 leaf 之名單已重建，
> 其中 `-001`／`-010`／`-044`／`-045`／`-053` 五個先前未被列入複查對象。
> 本輪補齊，全 12 條 TC 逐條複查完畢。

| TC | leaf | 節 | 答 | 依據 |
|---|---|---|---|---|
| `NR1L-ComfortHMI-015` | `SWE1-HVAC-023-01` | 3.1 | **部分為是** | 個別 toggle 之邏輯由 C19 明載；**ON 態之呈現形式未定義** |
| `NR1L-ComfortHMI-016` | `SWE1-HVAC-023-02` | 3.1 | **部分為是** | 七組合之循環順序由 C19 逐項列出；**「active」之判讀方式未定義** |
| `NR1L-ComfortHMI-017` | `SWE1-HVAC-023-03` | 3.1 | **部分為是** | UP/RIGHT 前進、DOWN/LEFT 後退由 C19 明載；同上之判讀缺口 |
| `NR1L-ComfortHMI-068` | `SWE1-HVAC-045` | 10.2 | **部分為是** | 三狀態之存在與循環由 EH2 明載；各狀態之圖示規格未定義 |
| `NR1L-ComfortHMI-042` | `SWE1-HVAC-001-03` | 2.1 | 否 | 所驗者為「tab 一個都不顯示」，判讀只需認得 tab 之有無 |
| `NR1L-ComfortHMI-059`…`-063` | `SWE1-HVAC-010-01`…`-05` | 2.7 | 否 | `fan segment`／`one bar highlighted`／`all FAN bars grayed out`／`main category control`／`pop-up` 五個可觀察量**全是 C6 自己的字** |
| `NR1L-ComfortHMI-067` | `SWE1-HVAC-044-01` | 10.1 | 否 | 「AUTO ECO 為作用中」之判讀依據在 **10.3**（EH3「Button label will read AUTO ECO」），是條文非圖片 |
| `NR1L-ComfortHMI-081` | `SWE1-HVAC-044-02` | 10.1 | 不適用 | `[BLOCKED-NON-HMI]` row，procedure 與 ER 皆空 |
| `NR1L-ComfortHMI-079`／`-080` | `SWE1-HVAC-053-01`／`-02` | 10.9.1 | 否 | ER 驗 EH9.1 書名號內兩段文字**逐字出現**，文字在條文內 |
| `NR1L-ComfortHMI-001`…`-003` | `SWE1-HVAC-076-01`…`-03` | 13.2 | 否 | 分頁切換與 popup 之出現／逾時，皆為 LS1 明載之事件 |

**新增之具體缺口（tri-mode）**：C19 未定義三個 airflow mode 按鈕之 ON 態
如何呈現。C13（`2.12`）之「highlighting the button and increasing button
size」屬四模式配置，於 tri-mode 車不適用。故 `-015`／`-016`／`-017` 三條之
ER 雖以「toggled ON」／「active」陳述，**其判讀依據不在條文內**。

**形態值得記**：同一 leaf 之三條 TC，**行為邏輯不依賴圖，而狀態之判讀方式
依賴圖**。問句若寫成「這條依不依賴圖」只會得到一個是非；寫成「**哪一部分**
依賴圖」才會得到一個分界。

**`-042` 之答另有一層**：`2.1` 之三張圖對**已生成**之 `-03` 不構成依賴，
但對**未生成**之 `-01`（tab 數）與 `-02`（順序）極可能是關鍵 ——
那兩者所缺的正是「哪一種配置產生哪一組 tab」（`DATA_REQUESTS` #17）。
**圖片之影響不隨 leaf 均勻分布，同一節內即可分歧。**

### 其餘 18 個未生成之帶圖 leaf —— 名單已重建（42 §4）

| leaf | 圖 | 節 | Test Set |
|---|---|---|---|
| `SWE1-HVAC-055` | 5 | `11.2` | Heated Vented Seats |
| `SWE1-HVAC-100` | 4 | `14.16` | Climate Popups |
| `SWE1-HVAC-083` | 3 | `14.1` | Climate Popups |
| `SWE1-HVAC-127` | 3 | `17.4` | Home Screen Widget |
| `SWE1-HVAC-007` | 2 | `2.5.1` | Climate Modes |
| `SWE1-HVAC-054` | 2 | `11.1` | Heated Vented Seats |
| `SWE1-HVAC-067` | 2 | `12.1` | Heated Vented Seats |
| `SWE1-HVAC-098` | 2 | `14.14` | Climate Popups |
| `SWE1-HVAC-125` | 2 | `17.2` | Home Screen Widget |
| `SWE1-HVAC-004` | 1 | `2.3.1` | Climate Modes |
| `SWE1-HVAC-017` | 1 | `2.12.1` | Airflow and Defrost |
| `SWE1-HVAC-038` | 1 | `7.10` | Rear Climate |
| `SWE1-HVAC-041` | 1 | `9.3` | Rear Climate |
| `SWE1-HVAC-042` | 1 | `9.4` | Rear Climate |
| `SWE1-HVAC-060` | 1 | `11.6.1` | Heated Vented Seats |
| `SWE1-HVAC-074` | 1 | `12.8` | Heated Vented Seats |
| `SWE1-HVAC-097` | 1 | `14.13` | Climate Popups |
| `SWE1-HVAC-105` | 1 | `15.1` | Climate Popups |

共 **34 張**圖分布於 18 個 leaf（25 個帶圖 leaf 扣除已生成之 7 個）。
生成時之必答項見 `RUNBOOK.md`。清單由
`features/comfort/inputs/FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
（143,292 bytes）之 `Analysis Report` 工作表實測重建，
另存 `data/image_leaves.json`（25 筆，含已生成者）。

**先前「不可達」之成因（R-C30）**：上繳 30 §5.3 記
`find . -maxdepth 3 -name "*037-A03*"` 於 repo root 零命中。
**該 pattern 正確，深度不足** —— 實際路徑為
`./features/comfort/inputs/…`，深度 4。
`feature.yaml` 之 `paths` 以 feature dir 為起點，我卻在 repo root 執行
`ls inputs/`。**R-C30 要求載明搜尋範圍，本例即其價值**：範圍寫下來了，
所以錯在哪一眼就看得出來，不必重猜。登為 **A-CF24**。

## A-CF26 —— 通用空白範本之 DV 涵蓋不足（跨 feature）

**發現於**：第二次寫回（ENTRY 004）之 assertion 13（上繳 33 §9.3）。

**Comfort 側 RESOLVED（2026-08-16）**：母本已由 Pei 擴充至 row 601
（`…_20260816_prepared_ext.xlsx`，ENTRY 022），五項涵蓋逐項實測通過；
ENTRY 023 之 assertion 14 項全數 PASS。
**跨 feature 之本體仍 OPEN** —— 修的是 Comfort 這一份母本之副本，
**通用空白範本 `SWQT_20260121` 本身未變**，故 privacy 已交付之 9 列
與日後任何以該範本為母本之 feature 仍受同一性質影響（DR #36）。
**一份被修好的副本不會使原件變好** —— 記此以免日後把 ENTRY 022
讀成本項已全案結案。

### 實測

對象：`inputs/FM-WI-FSM-036-A01 …_SWQT_20260121.xlsx`（SHA256
`cd876c202c71e74b…`）之資料工作表，以及自其產出之 prepared 檔
（`b68117a2…`）—— 兩者於此性質上相同。

| 項 | 涵蓋範圍 | 缺口 |
|---|---|---|
| B 欄編號公式 | row 10–59 | row 60 起無列號 |
| R 欄 x14 下拉（design_method 九項）| `R10` ＋ `R11:R59` | row 60 起無下拉 |
| **P 欄 DV（priority）** | **`P10:Q11`** | **row 12 起無下拉** |
| `T–Z` DV | `T10:Z11` | row 12 起無下拉 |
| `AF` DV | `AF10:AF11` | row 12 起無下拉 |

### 為何是跨 feature —— **已實測，不再是轉述**

**該範本是通用空白母本，不是 Comfort 產生的。** 凡以其為母本者，
其交付件於 row 12 之後皆無 P 欄下拉約束。

**privacy 側之實測（50 §5 授權唯讀量測；本 pipeline 未寫入該 feature 任何檔案）**：

| 項 | 實測值 |
|---|---|
| 檔 | `features/privacy/output/…_Privacy_20260813_regen-v1.xlsx`（63,001 bytes）|
| SHA256 | `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f` |
| 身分 | 與 privacy `DELIVERY.sha256` 所記**已置入客戶交付夾**之副本 hash 相同 |
| 資料工作表 | `Test Case Specification 測試用例規範`，`dimension A1:AH59` |
| **已填列** | **row 10–20，共 11 列**（`NR1L-Privacy-001` ～ `-011`）|
| **P 欄 DV `sqref`** | **`P10:Q11`** |
| R 欄 x14 `sqref` | `R10` ＋ `R11:R59` —— **11 列全在範圍內**，故 design_method 側無缺口 |
| `T–Z` / `AF` DV | `T10:Z11` / `AF10:AF11` |

**故 privacy 已交付件之 `row 12–20`（9 列）確實無 P 欄下拉約束，
且其 R 欄下拉完好。** 上繳 34 §9.6 自陳該句為「轉述分析層陳述」，
本輪已改為實測，數字與 46 §2 所述相符。

> **一份未經實測之 anomaly 陳述，正是本 pipeline 反覆指出的問題**（50 §5）。
> R-C21 禁的是代他 feature 建檔與修改其既有檔案，**唯讀量測不在其列**。

### 性質 —— 內容正確而約束缺失

**已寫入之值不受影響**：priority 由 generator 產出並經 lint 之
`priority` gate 檢查（`P0`–`P3`），故交付件之**內容不是錯的**。
缺的是**下拉約束**，其作用在於保護**後續之人工編輯** ——
評閱者或測試員於 Excel 內改 P 欄時，row 12 之後不會有任何阻擋。

**故本項不是「已交付之內容有誤」，是「已交付之防呆缺一段」。**
兩者之緊急度不同，處置亦不同，記明以免被讀成前者。

### 處置

依 **R-C21**（跨 feature 之發現登於發現者之帳並具名對象）：
登於 Comfort 之 `ANOMALIES.md` 與 `DATA_REQUESTS.md` **#36（High）**，
具名對象為 **privacy** 及其他以 `SWQT_20260121` 為母本之 feature。

**不代改 privacy 之任何檔案** —— 是否回溯由 Pei 決定。
本 pipeline 於本輪未讀寫 `features/privacy/` 之任何檔案。

**為何當初沒被發現**：ENTRY 002 之 pilot 寫 14 列（row 10–23），
其 assertion 九項**完全沒有檢查 DV 涵蓋**；profile §0.1 之 Excel 四項確認
問「R 欄下拉可用且為九項」，而 **R10 恰在範圍內**，故人與程式兩端都通過了。
**一個檢查沒問的問題，不會因為別的檢查通過而變成已答**（上繳 33 §9.3）。
今已補為 assertion 13。

---

## A-CF25 —— `ICE1` 之交叉引用指向錯誤條款（spec 內部瑕疵）

**發現於**：批次 6（`ICS Anatomy`）生成時逐句讀 `16.2`。

`ICE1` 末於其例外子句附一個具名引用：

> these changes are reflected in both locations **with the exception of the
> recirculation led in climate off (see ICE11.)**

實測三節：

| 條款 | 節次 | 內容 | 含 recirculation LED 規則？ |
|---|---|---|---|
| **ICE11** | `16.12` | `Airflow Modes has 5 states (1.Face, 2.Mix of Face & Feet …)` | **否** —— 全句無 `recirc` 字樣 |
| **ICE9** | `16.10` | `When climate is OFF, the recirculation LED of the hard control is on. Action on the recirculation hard control will not turn system back on; it simply opens the recirculation and turns led off.` | **是** |

**故 ICE1 之 `see ICE11.` 應為 `see ICE9.`。**

**與 A-CF13 同類**（條款標籤之可靠性問題），但形態相反：A-CF13 之四項是
**同一標籤跨多節**（`C16.)` 跨 2.15／16.17 等），本項是**引用指向錯誤標籤**。
兩者合看，同一結論再次成立 —— **條款標籤不是唯一鍵，traceability 一律以
outline 節次為鍵**（profile §1）。

**處置**：`NR1L-ComfortHMI-083`（`SWE1-HVAC-106-02`）只驗 ICE1 自身所述之
例外（climate off 時該變更不反映於畫面），**不依該誤引去取用 16.10 之
LED 規則**（§8.2.1：引用另一節之事實不等於驗證另一節之行為）。
`16.10` 亦未列入該條之 `specification_reference`。

**不列 RD-1**：spec 內部之引用錯誤，不影響本 feature 之取材，且該行為之
正確規則在本 feature 範圍內（`16.10`，`ICS Climate Modes` 組，尚未生成）。

---

## A-CF-EXT-01 — 已交付件之 `NEVER_WRITE` 欄位帶值（由 Power feature 回報）

> **來源**：Power feature 之 11 / 12 包（`features/power/docs/upstream/11_template_verify.md` §二、
> `12_pilot_fixes.md`）。依 Power R-P94 回報，**範圍限定於
> `write_back.py` 之 `NEVER_WRITE` 所列各欄**，未做全欄位稽核，
> **未修改 Comfort 之任何交付物**。

**事實**：`FM-WI-FSM-036-A01 …_SWQT_Comfort_20260817.xlsx`（已交付，466 資料列）
之 `NEVER_WRITE` 十八欄中，**九欄帶值**：

| 欄 | 標頭 | 非空 / 466 | 研判 |
|---|---|---|---|
| B | No.# 序號 | 466 | **可解釋** —— 範本自帶公式 `IF(ISBLANK($D10),"",ROW()-9)`；`NEVER_WRITE` 之註解即說明此機制 |
| O | Test Case Reference ID | 466（全為 `NEW`） | **與設定矛盾** —— 值恰為 `feature.yaml` 之 `write_back.tc_ref_id_value: "NEW"`，即意圖是寫入，卻同時列於 `NEVER_WRITE` |
| T–Z | 七個 Vehicle Model 欄 | 466（全為 `1`） | **無法解釋** —— 見下 |
| C / E / Q / AB–AG | 其餘九欄 | 0 | 符合 `NEVER_WRITE` |

**T–Z 之三項反證**（三者一致指向「應留白」）：

1. Comfort profile draft §3 逐字：「**T–Z 欄 Vehicle Model：一律留白（Privacy R30-4）**。
   **A-PV15 同樣適用於 Comfort**：範本七欄止於 27 世代，本專案平台為 HDCC28，
   **不得將 27 世代欄位對映至 28 平台**。」
2. `scripts/write_back.py`：`NEVER_WRITE = ["B","C","E","O","Q","T","U","V","W","X","Y","Z", …]`
3. `features/comfort/inputs/` 之 baseline 工作簿：T 欄非空數 **0**

另：全 Comfort 腳本**無一呼叫 `.save()`**（`grep -rln '\.save('` 結果為空）。

**結論**：T–Z 之 466 個 `1` **非由 Comfort 管線產生**，來源不明
（可能為客戶端或人工於管線外填入）。O 欄之 `NEW` 則指向
`NEVER_WRITE` 與 `feature.yaml` 之設定互相矛盾。

**本回報不含處置建議** —— 交由 Comfort 自行判斷。

---

## A-CF-EXT-02 — `R-C6` 之條文與其自身已交付件不一致（由 Power Moding feature 回報）

> **來源**：Power Moding feature 之 02／03 包
> （`features/power_moding/docs/upstream/02_baseline_switch.md` §10.2、
> `03_testgroup_and_dv.md` §5）。執行層實測後由分析層獨立複驗，
> 依 03 包步驟 5 回報。**只記事實與證據，不判定成因、不提案修改 Comfort
> 之任何條文，未修改 Comfort 之任何交付物。**

**回報之緣由**：Power Moding 之 `R-PMH2`（feature 身分與 `test_group`）
逐字引 Comfort `R-C6` 為其唯一依據。查證該前例時發現條文與交付件不符，
致 `R-PMH2` 之後半於 Power Moding 側被撤回（`R-PMH13`）。
本則為該查證之回報。

**條文原文**（`features/comfort/RULINGS.md:128`）：

```
R-C6  Test Group
workbook Test Group 欄一律填 "Comfort"。

依 §4.1.1：Layer 1 Test Group 等同 spec 文件標題之模組名；spec 標題為
"Comfort HMI Logic and Flow"，故模組名為 Comfort。客戶交付路徑中之
"Climate Control Interface" 為資料夾分類，非 spec 標題，不作為 Test Group
來源。
```

**實測**（唯讀，`openpyxl` `data_only=True`；未寫入）：

檔案：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/
Climate Control Interface/FM-WI-FSM-036-A01 …_SWQT_Comfort_20260817.xlsx`
分頁：`Test Case Specification 測試用例規範`，r10 起 `D` 欄非空之列

| 項 | 實測 |
|---|---|
| 資料列數 | 466 |
| `G`（Test Group）欄相異值 | **1** |
| 該值 | **`Climate Control Interface`** |
| 覆蓋 | **466 / 466（100%）** |
| 值為 `Comfort` 之列 | **0** |

即：**已交付之工作簿，其 Test Group 欄 466 列全填交付夾名
`Climate Control Interface`，恰為 R-C6 明文排除者；填 `Comfort` 者零列。**

**同批對照**（四份已交付件，同一量測條件）：

| 交付件 | 交付夾名 | `G` 欄實測值 | 覆蓋 |
|---|---|---|---|
| **Comfort 20260817** | `Climate Control Interface` | **`Climate Control Interface`** | **466 / 466** |
| User Profiles 20260820 | `User Profiles` | `User Profiles` | 189 / 189 |
| Time Management 20260822 | `Time Management` | `Time Management` | 59 / 59 |
| Power Management 20260821 | `Power Management` | `Power Management` | 283 / 283 |

四份皆為交付夾名，無一例外。**Comfort 是四份中唯一「交付夾名 ≠ 規格模組名」
者，也因此是唯一能分辨兩種取法之語料** —— 其餘三份之二者恰好相同，
對本題無鑑別力（Power Moding `R-PMH14`）。

**三種可能之成因，本 feature 無從判定，不選擇**：

(a) R-C6 立於 2026-08-14 而交付件出於 2026-08-17，條文未被落實或落實後被回改；
(b) `features/comfort/feature.yaml` 之 `test_group` 註明
    「framework-internal; workbook write per profile」，即**宣告值與寫回值
    本即分離**，R-C6 管前者而交付件呈現後者 —— 若為此解，則 R-C6 之
    「**workbook** Test Group 欄一律填」一語與該分離不一致；
(c) 該欄由管線以外之他人填寫（比照 A-CF-EXT-01 之 T–Z 情形）。

**Power Moding 側之處置（僅供參照，不要求 Comfort 比照）**：
依四份交付件之實測立 `R-PMH13`，G 欄填交付夾名 `Disclaimer screen`，
並撤回 `R-PMH2` 之後半。Pei 於 2026-08-23 核可。

**本回報不含處置建議** —— 交由 Comfort 自行判斷。
