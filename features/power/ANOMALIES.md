# ANOMALIES — FW036 Power HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PWnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

來源：下放包 01 §F（A-PW01–A-PW07）、02 §F（A-PW07 撤回、A-PW08；執行層新登 A-PW09–A-PW11）、
03 §F（A-PW12、A-PW13；執行層新登 A-PW14–A-PW16）、
04 §F（A-PW17、A-PW18；執行層新登 A-PW19、A-PW20）、
05 §F（A-PW21 ~ A-PW23；執行層新登 A-PW24、A-PW25）、
06 §F（A-PW26 ~ A-PW29）。
撤回列不刪、不重編號。

---

| ID | 內容 | 證據 | 狀態 |
|---|---|---|---|
| A-PW01 | `SWE-PM-089` 之 `Source Requirement ID` = `SWE1-PM-ANT-008`，為 037 自身另一套命名空間，非上游來源 | 全表 18 欄 × r8–r145 掃描，該 token 不存於任一 SYS2 匯出 | PENDING（DR-PW1；03 包 G3 再度復現：114/115，唯一失敗者即此 leaf） |
| A-PW02 | `Sys-RA-PM-0334` 之 source id `4942087` 於兩份 CFTS 本文皆不存在；`4942xxx` 為 CFTS010 號段但低於其首個 id `4942192` | SYS2 CFTS009 匯出 r325 | PENDING（DR-PW3）。**03 包實測全部證實**：`4942087` 為 439 個 token 中**唯一**既非需求錨點亦非章節錨點者（G6b）；CFTS010 首個 id 實測為 `4942192`（§1 Power Down），`4942087 < 4942192` 成立 |
| A-PW03 | 037 `Excluded NRLs (HW-only)` 26 筆全落 NRL-928xx–930xx（CFTS009 域），**不含** `NRL-99476`（`Sys-RA-PD_013`，HW） | 排除台帳涵蓋範圍不等於其名稱所宣稱 | **證據成立，且應加強**（03 包複驗）。26 筆號段實測 92882–93063，全落區間內，0 例外；`NRL-99476` 確不在其中，而該 NRL 於 SYS2 CFTS010 之 `SW/HW/System` 欄實測為 `HW`。**加強**：分頁名為 "(HW-only)" 但 26 筆之分類實測為 `HW` 18 / `Information` 4 / `Out of Scope` 2 / `Heading` 1 / 空白 1 —— 名稱在**分類**上亦不實，非僅涵蓋範圍。<br><br>**加註（R-P30，逐字）**：「加註（03 §六複驗）：分頁名為 Excluded NRLs (HW-only)，但 26 列之 SW/HW/System 欄實測為 HW 18 / Information 4 / Out of Scope 2 / Heading 1 / 空白 1。故『(HW-only)』在分類上亦不實，不僅是涵蓋範圍不足；原描述只指出後者。」 |
| A-PW04 | 037 `SYS2 Traceability` 33 列不含任何 `NRL-994xx` 或 `Sys-RA-PD` | CFTS010 全域未進追溯分頁 | **逐字成立**（03 包複驗）。33 列實測 `NRL-994xx` 出現 0 次、`Sys-RA-PD` 出現 0 次、`Sys-RA-PM-` 出現 76 次 |
| A-PW05 | **（依 R-P29 以指定文字整條替換）** 037 內部 id 命名空間不一致：SWE1 Requirements 分頁用 SWE-PM-001..115（115 筆連續）；SYS2 Traceability 分頁用 SWE1-PM-TLM-001..033（33 列，前綴分布單一）。該分頁 SWE-PM- 出現 0 次，兩套互不對應。實測附註：SWE1-PM-ANT- 命名空間不在本分頁，其唯一出處為 SWE-PM-089 之 Source Requirement ID 欄（見 A-PW01）。 | 03 包複驗：c1 前綴分布 `{SWE1-PM-TLM-: 33}`；含 `ANT` 者 0 筆；`SWE-PM-` 出現 0 次 | **已訂正（R-P29）**。原描述之 `-ANT-` 部分為假，證據出處誤植（見 A-PW18）。核心主張維持成立 |
| A-PW06 | 037 `Sub Categorization` 詞彙漂移：`HMI` 36 / `Service\nHMI` 35 / `Service` 27 / `HMI Service` 16 / `HMI/Service` 1 | 三種寫法指涉同一組合，不可作分批判準 | **逐字成立（R-P31 複驗，G18）**。實測值域恰為 5 值，計數逐一相符：`'HMI'` 36、`'Service\nHMI'` 35、`'Service'` 27、`'HMI Service'` 16、`'HMI/Service'` 1，合計 115。原描述無須訂正。`Service\nHMI` 之分隔為換行字元 U+000A，非空格 |
| A-PW07 | ~~三份 `.docx` 實為 Markdown 純文字，副檔名與內容不符~~ | ~~magic bytes 實測（R-P3）~~ | **撤回（R-P12）**。原始檔實測：CFTS009 `.docx` = OOXML、CFTS010 `.doc` = OLE2、SYS3 `.docx` = OOXML。副檔名與內容**實為相符** |
| A-PW08 | 01 下放包 §B 之「真實格式」欄與 `bytes` 欄與原始檔不符，源於以衍生物冒充原始檔。CFTS010 之原始檔副檔名為 `.doc` 非 `.docx` | 01 包記 412,654 / 81,064 / 51,264 bytes「純文字」；原始檔實測 154,588 / 245,248 / 3,474,091。三個宣稱之 SHA256 於整個家目錄內無符合檔案 | **已處置**（R-P9–R-P13） |
| A-PW09 | 01/02 包 §C 之 SYS2 CFTS009 讀取座標 `r2–r338` 漏一列：實際延伸至 **r339** | r339 = `NRL-142587`，`Type` 欄實測 `Heading`，`Sys-RA-Feature-ID` 欄為空，`Source Requirement items` 欄為空 | **已處置（R-P18）**。座標改 r2–r339；G6a = 337/338 |
| A-PW10 | §E Layer 3 未涵蓋 CFTS009 **§1.6.2.1.17**（1 leaf：`SWE-PM-057`）；§E 於 Power State 列出之 **§1.8.1** 主章節落點為 0 | 02 包 §E 重算 | §1.8.1 部分依 **R-P16 已刪除，惟前提須複核**（見 A-PW14）；§1.6.2.1.17 部分 **live**，B2 素材已備妥（§1.6.2.1.17 = `Proxi Parameters management`），待 Q1 裁定 |
| A-PW11 | CFTS009 與 CFTS010 之標題以不同機制表達粗體（`pStyle 1–8` vs run 層），單一序列化無法同時滿足 §C rule 1 與 rule 2 | 全粗體序列化：009 得 172/904、010 得 0/148；未標記序列化：009 得 196/0、010 得 92/0 | **已處置（R-P17）**，保留為文字層定義之理據 |
| A-PW12 | 01/02 包之 G6 期望值「336/337」將錨點鏈第一段（欄內 token 可抽取）與第三段（token 可解析至章節）混為一談 | 03 包實測：G6a（第一段）= 337/338；G6b（第三段，列層）= **336/337**，唯一失敗者 `Sys-RA-PM-0334` —— 舊值精確落在第三段上 | **已處置（R-P18）**。舊 G6 作廢，拆為 G6a / G6b |
| A-PW13 | §E 之 leaf 分布缺乏可重現之產生程序；主章節規則未書面化即產出數字 | 02 包重算得 62/24/16/8/3 + 未歸類 1，與 §E 之 64/24/16/7/3 不符 | **已處置（R-P15）**，惟 §E 定版本身仍待 Q1 裁定 |
| A-PW14 | **R-P16 刪除 §1.8.1 之前提「實測 0 leaf 落點」僅在 02 包主章節規則下成立** | `SWE-PM-057` 之章節集合實測含 CFTS009 **§1.8.1.1.1（ID 1 Description）**，出現 3 次，與 §1.6.2.1.17（3 次）、§1.6.3.1.1（3 次）同票。即 §1.8.1 有 leaf 觸及，只是在該規則下未勝出 | **新增（執行層 Tier 1 登記）**。依 R-P15(b)，`SWE-PM-057` 之歸屬待裁；若裁為 §1.8.1.1.1，R-P16 之刪除須撤回 → **已處置（R-P25）**：R-P16 撤回，§E 改記 §1.8.1.1.1。撤回理由經確認為「規則已廢止而其結論留存」，與 R-P18 所訂正之 G6 錯誤同型 |
| A-PW15 | SYS2 之 `Source Requirement items` 欄所填 id 並非全為需求錨點 id：**81 個為章節錨點 id**（Sys-RA 直接指向章節而非其下之需求） | 03 包 G6b：439 個 token 中 82 個無法經需求錨點路徑解析，其中 81 個實為 CFTS009 章節錨點 id（如 `4941006` = §1 Wake-up and Power-up），僅 1 個（`4942087`）兩路皆無 | **新增（執行層 Tier 1 登記）**。§C rule 3 稱該欄「即為上述 id」（rule 2 之需求錨點 id），與實測不符。已驗：兩種讀法對 G3（114/115）與跨章節 leaf 名單（11 個）**皆無影響**，故本包未擴張 rule 3；待分析層決定是否明文化第二條解析路徑 <br><br>**加註（04 §C(i)）下游影響**：此 81 個章節錨點 token 於 Phase 4 產生 `specification_reference` 時，其引用對象為章節而非需求，引用格式將與其餘 357 個需求錨點 token 不同。04 包不處理，僅登記 |
| A-PW16 | **跨章節 leaf 之次章節中有 9 章未被任何 leaf 之主章節覆蓋** —— 在現行主章節作法下，這 9 章不會產生任何 TC | 03 包 G14：被丟棄之相異次章節 10 個，僅 1 個被他 leaf 之主章節覆蓋。未覆蓋者：CFTS009 §1.6.2.1（TLM algorithm requirements）、§1.6.2.1.4（Stolen Vehicle Mode）、§1.6.2.1.9（Logistic Idle）、§1.6.2.1.10（Logistic Standby）、§1.6.2.1.11（Logistic Sleep）、§1.6.2.1.14（TLM modules and functionalities depending on operative state）、§1.6.2.1.15.1（ICS Wakeup Reasons by POWER Button Pressed）、§1.6.3.1.1（SwitchOff_Timeout_Setting.Req management）、§1.8.1.1.1（ID 1 Description） | **新增（R-P22 之閘門所捕獲）**。其中 `Stolen Vehicle Mode`、三個 `Logistic` 狀態、`ICS Wakeup Reasons by POWER Button Pressed` 為實質功能章節。Layer 3 之涵蓋宣稱在此 9 章上不成立 → **B2 v2 已完成（R-P38）**，判讀單位改為「被引用之錨點 vs leaf」。九章 31 個錨點中僅 18 個被引用；判定：涵蓋 2、涵蓋（一分支例外）1、部分涵蓋 5、未涵蓋 1、無法判定 1。**§1.6.2.1.15.1 由「部分涵蓋」改為「涵蓋」** —— v1 所據之兩個錨點未被引用。處置待裁 → **已處置（R-P43）**：（a）3 章無待辦；（b）5 章之未被引用錨點依 R-P42 不測，登於 A-PW27；（c）§1.6.2.1.4 → DR-PW5；（d）§1.6.2.1 → DR-PW6 |
| A-PW17 | R-P15（主章節判定規則）建立於「一 leaf 對一章節」之未驗前提上 | 該前提於 03 §九第 1 項提出質疑；04 包 R-P24 確認 Layer 3 無「一列一值」之約束（§4.1.5，Layer 3 不入工作簿），前提不成立 | **已處置（R-P24）**。Layer 3 改記全集（`data/layer3_full.tsv`，140 列／46 個相異章節）；R-P15(b) 之逐條裁定收窄為僅 Layer 2 Test Set 歸屬 |
| A-PW18 | 分析層將 A-PW01 之證據誤植於 A-PW05 | `SWE1-PM-ANT-008` 之唯一出處為 `SWE1 Requirements` 分頁 `SWE-PM-089` 之 `Source Requirement ID` 欄（A-PW01 所指者），而 A-PW05 稱其在 `SYS2 Traceability` 分頁 | **已處置（R-P29）**。A-PW05 已以指定文字整條替換 |
| A-PW19 | **R-P7 條文所載「CFTS009 本文未被引用之 547 條」與實測不符** | 04 包 G17 實測：CFTS009 904 個需求錨點中，被 037 引用者 **235**，未被引用者 **669**（非 547）。CFTS010 148 個中被引用 3、未被引用 145。舊值 547 出自 R-P10 已宣告失效之衍生物 | **新增（執行層 Tier 1 登記）**。R-P7 之**裁決效力不受影響**（「不追、不問、不列 RD-1」），僅其條文內嵌之數字為失效值。依「不得修改裁決條文」未動 R-P7，於此登記 → **已依 R-P36 以註記處置（05 包，G27 PASS）**：R-P7 原文位元組未變，於其下新增註記段落 |
| A-PW20 | **SYS3 SYSAD 之元件分解不攜帶可連結至 leaf 之 traceability** | 04 包 B3/G20 實測：SYS3 含 630 個 `Sys-RA-PM-` token 出現（272 相異），但 549 個歸屬中 444（81%）落在兩個分配矩陣節（§4.28 230、§4.3 214）；R-P32 所指定之切入點「動態行為」七個狀態子節（§4.30–§4.36）token 數**全為 0** | **新增（R-P32 之比對所產生）**。§E「不是交集、只由單一來源支撐」之弱點因此**確認成立且無法以 SYS3 消除** |

| A-PW26 | **31 處懸空 `WrapperResource` 參照為規格交付缺陷** —— 參照存在而其所指資源未隨文件匯出 | CFTS009 16 處、CFTS010 15 處，分布 **16 章**（各 8 章）。二份文件皆實測零嵌入物件（CFTS009 無 `word/embeddings/`、四類 OOXML 物件標籤各 0；CFTS010 之 OLE2 目錄無 `ObjectPool`／`\x01Ole`）。B1 leaf 層交叉：**僅 2 處落在被引用錨點下**（CFTS009 §1.6.2.1 之 `4941354`/`4941355`），觸及 9 個 leaf 全屬 Power State；其餘 29 處依 R-P42 不在範圍內 | **新增（06 §F）**。已發 **DR-PW6**（Medium） |
| A-PW27 | **部分涵蓋 5 章之未被引用錨點依 R-P42 不測，逐一登記** | §1.6.2.1.4：`4941399`（進入條件，`Radio` 欄不含 R1L）；§1.6.2.1.9：`4941429`（`$Telematic_Power$` = [Logistic_On]）；§1.6.2.1.14：`4941452`、`4941454`–`4941459` 共 **7 個**；§1.6.2.1.15.1：`4941661`（ICS POWER 鍵 wakeup 路徑）、`4941662`；§1.8.1.1.1：`4941813`、`4941816`。合計 **13 個未被引用錨點** | **新增（06 §F）**。依 **R-P42** 一律不測、不發 DR、不於 `reasoning` 欄以「為求完整」納入。登記備查 |
| A-PW28 | **`Verification Criteria` 欄存在不可執行之內容** | G28 基線：VC 單欄不可執行 **2 / 115** —— `SWE-PM-007`「Vehicle not equiped with CAN or engineering line is active」、`SWE-PM-008`「Vehicle equiped with CAN」（後者為 R-P49 條文所舉之反例本身）。VM 單欄 **0 / 115**；**二欄合觀 0 / 115** | **新增（06 §F）**。已發 **DR-PW7**（Low）—— 二者之 VM 皆可執行，**不阻斷任何 leaf 之 TC 撰寫**，僅影響其 Pre-Conditions 欄品質 |
| A-PW29 | **G25 之 EE Architecture 分布為 Phase 4 填 FW036 c21–c27 七個車型欄之判準來源，非僅越界檢查** | 被引用 238 個 item 中 **`Atlantis Mid` 單值 13 個**（不適用 c21/c22 兩個 Atl-Hi 欄）、**`Atlantis High` 單值 1 個**（不適用 c23–c27 五個 Atl-Mi 欄）；逐 leaf 層級有 **2 個 leaf** 之 item 聯集僅含單一世代 | **新增（06 §F）**。此用途於 R-P40 立條時未預見。與既有政策 **R30-3 / R30-4（車型欄留白）** 之併存關係待裁 |

> **註記（R-P36，05 包加註）**：本條原描述之 `-ANT-` 證據出處為誤植，來源實為 A-PW01（`SWE-PM-089` 之 `Source Requirement ID` 欄）。見 A-PW18。（本條內文已於 04 包依 R-P29 之逐字指定替換；R-P36 自 05 包起生效，此後之訂正一律走註記。）
| A-PW21 | 分析層於 04 下放包 §前言將自身未落檔之草稿誤稱為「03 包所提之 R-P29」 | 03 上繳包之待裁項為 Q1–Q8，未提出任何編號 R-P29 之條文，亦未提出「分析層未讀即裁准」之議題 | **新增（05 §F）**。為第三次來源誤植（前二次：A-PW18 分析層、A-PW19 失效數值）。已依 R-P36 於 04 下放包 §前言下加註，原文不改（G27 PASS） |
| A-PW22 | 執行層於 03 §九第 4 項將自身概覽表之排版簡寫「—」讀為實測值，致生「七條 `Requirement Title` 為空」之誤述 | 04 包 G19 實測 037 全 18 欄零空值；`data/multi_chapter_leaves.md`（03 包 B1 本體）自始載有正確標題 | **新增（05 §F）**。已於 04 上繳包 §八自陳並於 `data/b1_swepm008.md` 就地訂正。**與 A-PW18/19/21 併觀：雙方各有來源誤植，非單方問題** |
| A-PW23 | ~~G8 = 904 所代表之規格覆蓋率無上界保證，因 CFTS 本文含嵌入物件而文字層不可見~~ | ~~R-P39~~ | **框架依 05 包實測訂正**。CFTS009 `.docx` 實測**無 `word/embeddings/`**、`w:object`/`w:drawing`/`w:pict`/`o:OLEObject` 各 **0** 個、`word/media/` 僅 1 個頁首圖。`…inline.rtf WrapperResource` **是純字面文字，非嵌入物件之錨**，其所指資源**未隨文件匯出**。**訂正後描述**：CFTS009 16 處、CFTS010 15 處，合計 **31 處懸空參照**，分布於 **16 個章節**（各 8 章），其中 8 章之非錨點內文 < 200 字元。904 個需求錨點本身完整存在；不可得者為這些參照所指之外部資源。詳見 `data/b3_embedded_objects.md` → **上界已測（R-P48 / G30）**：CFTS010 之 OLE2 目錄實測 14 項，無 `ObjectPool`、無 `\x01Ole`、無 `_`-起始 storage → **嵌入物件數 0，確定值非下界**。二份 CFTS 皆零嵌入物件，訂正形態確立 |
| A-PW24 | §E Layer 3 清單未涵蓋 CFTS009 **父章節 `§1.6.2.1`**（`TLM algorithm requirements`）與 **`§1.6.2.1.17`** | 05 包 G21 指派時實測：`§1.6.2.1` 被 **9 個 leaf** 觸及（`SWE-PM-001`–`009`）、`§1.6.2.1.17` 被 1 個 leaf 觸及（`SWE-PM-057`）。§E 之 Power State 列僅載 `§1.6.2.1.1–.15` | **新增（執行層 Tier 1 登記）**。二者於 Test Set 指派時作為「非 Test Set 候選」登記，**不影響 R-P35 之定版分布**（相關 leaf 之其餘章節皆指向單一 Test Set）。待裁 → **已處置（R-P46）**：§E Power State 增列 `§1.6.2.1`、Timeout Settings 增列 `§1.6.2.1.17`；G13b 複驗仍為 46，G21 複驗 63/24/16/8/3 未變 |
| A-PW25 | §E「本分組之已知弱點」段所載之 `Requirement Title` 統計為失效值 | 該段稱「出現 **20+ 種**，多數僅出現 1 次（`Timeout` 7、`Phone Call` 5 為**僅有例外**）」。05 包 G26 實測：相異值 **99** 種、僅出現 1 次者 **94** 種；出現 > 1 次者除 `Timeout` 7、`Phone Call` 5 外，另有 `Splash Screen logo visualization` 4、`Power down` 3、`FOTA` 2 | **新增（執行層 Tier 1 登記）**。該段結論（`Requirement Title` 無分組價值）**不受影響，反而更強**。該敘述位於 §E 之弱點段而非裁決條文，是否依 R-P36 精神走註記待裁 → **已依 R-P47 以註記處置（G31 PASS）**：§E 弱點段原文位元組未變（SHA256 `1f737d7c…7d1ca6` 前後同值），註記為新增段落 |

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PWnn]`.
