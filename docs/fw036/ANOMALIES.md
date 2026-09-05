# ANOMALIES —— 全域線（GC 系列）

> 新建 2026-09-05（GC-01 審閱 §五-5，Pei 准）。收全域清理／來源集中線之分析層自報。
> feature 線之 A 條仍記各該 feature 之 `ANOMALIES.md`。編號 `A-GC{n}`。

| id | 內容 | 證據 | 形態 | 狀態 |
|---|---|---|---|---|
| A-GC1 | 下放包 GC-01 記 HMI Settings List 3 份 3 體，實為 **5 份 4 體** | `up/20260905_GC-01.md` 2-1 節 | 樣本代母體 | 已承認（`down/20260905_GC-01_review.md` §一）|
| A-GC2 | LID 異體只記 vehicle_setting，漏 time_management | 同上 | 樣本代母體 | 已承認 |
| A-GC3 | `_intake/SW_Update` 記 9 檔，實為 8 | 同上 2-2 節 | 未區分 meta | 已承認 |
| A-GC4 | `lint_reports/` 記 110，實為 106 | 同上 §5 | 估值未標估 | 已承認 |
| A-GC5 | 記 R-G40／41 兩側同題，實為台帳單邊；僅 R-G42 同題 | 同上 §3 | 一號推及三號 | 已承認 |
| A-GC6 | 模板誤值記三處，實為四處（`functional_safety` R→S） | 同上 §6 | 抄人寫之數（R-G20(LEDGER)）| 已承認 |
| A-GC7 | R-G44 條文以「大小相異」為判準，逆不成立 | 同上 2-1 節（295,635 三份二體）| 判準不對稱 | 條文已修（review §三）|
| A-GC8 | 「任何引用皆歧義」措辭過強；人讀 47.3% 可判 | 同上 §4 | 判準未載 | 已承認 |
| A-GC9 | R-G45 所附「待記者」為樣本值：記 1，實為 **5 feature／13 檔次** | 同上 11-3 節 | 樣本代母體 | 已承認（`down/20260905_GC-01_review2.md` §二）|

| A-GC10 | 「`Test Case Specification&Result` 該名不存在」為偽：它不在 R-G1 母本，但為另一真實變體，145 本中 24 本帶該名（含 `features/power` 在效輸入）；`backend/parser.py:77`、`writer.py:10`、`review_engine.py:1338` 硬編該名 | `up/20260905_GC-02.md` 6-2 節；`docs/reports/tc_sheetname_census_20260905.tsv` | 樣本代母體；**執行層（GC-01 §6 寫入）與分析層（審閱 §三據以下裁）同犯** | 已承認；審閱 §三「R-G48 之補充」之夾具改名裁決**撤回**（`down/20260905_GC-02_review.md`）；模板括號已改 |
| A-GC11 | 審閱 `down/20260905_GC-01_review.md` §三 內有裸節號（`§5`、`§0`～`§4`），違 PROTOCOL「文面引用」；已經 R-G36 機器抽取進台帳，`canon_refs` section ambiguous +1 | `up/20260905_GC-02.md` 9-1 節 | 審閱檔不受自己所定之規拘束 | 已承認；台帳逐字不改，下一輪 `rulings_hash` 後以註記指明其所指為 `up/20260905_GC-01.md` 5 節、`down/20260901_VS-SL-01.md` 各節 |

| A-GC12 | R-G43 之理由「台帳為 `rulings_hash.py` 之指紋源」未量測即斷言，**為偽** | `up/20260905_GC-03.md` 9-3 節：掃描面為 FO ＋ `features/*/RULINGS.md`（`scripts/rulings_hash.py:255-258`）；`RULINGS.sha.tsv` 698 列來源為台帳者 0；R-G12～R-G29 之指紋列全部來自 FO | 人寫之理由代量測 | 已承認（`down/20260905_GC-03_review.md` §一）。裁定 (A) 維持，理由以刪除線更正；掃描面缺口由 R-G43(b) 補。**同一事實解釋 R-G30–R-G41 之「缺列」——該十二條只在台帳，本就不在掃描面，非 Pei 漏跑** |

| A-GC13 | GC-03 審閱 §四 之判準（key 級 grep）未先量其分母，對 comfort／time_management 兩線為**盲測** | `up/20260905_GC-04.md` 4-1 節：comfort 之工作簿引用 PU id **0/1340**、time_management 引用設定名 9/316、LID signal 1/2548；分母由執行層附上方顯 | 判準未量其覆蓋 | 已承認（`down/20260905_GC-04_review.md` §三）。13 判依分母修正五列 |
| A-GC14 | **judged.tsv 對 `A-BLM8` 之判側，係讀到截斷之 `context` 即援引該線宣告而定** | `up/20260905_GC-05.md` 4-2 節：row 7–16 判 `FO`（conf `M`），而該行即撞號紀錄本身，與判 `KEEP_ANNOTATE` 之 row 17–19 同質；執行層擋下。另：下放包所載 confidence 分布 H 105／L 6 與實測 H 104／L 7 差一（產表腳本之統計與寫檔不同源，同 R-G59）| 以規則代量測／人寫之數 | 已承認（`down/20260905_GC-05_review.md` §二）。row 7–16 由 GC-06 改為 `KEEP_ANNOTATE` |
| A-GC15 | **「指紋表重生後 `canon_refs` 之 ruling unresolved 即消」為未量測之因果，兩層轉抄** | 「`rulings_hash` 重生後 `canon_refs` 之 `ruling` unresolved 即消」——GC-05 上繳 7-1 節所斷、GC-05 審閱 §四照抄。實測重生後 786→788，**未消**。`canon_refs` 之輸出自證：`FO … R-G 編號 50／IN … R-G 編號 0`，即其 `ruling` 型只對 **FO 之 R-G 錨點**解析，不讀台帳…（全文見 `down/20260905_GC-06.md` §一）。GC-06 §二-1-2 實測：unresolved 963 處**全部**落在「台帳有錨、FO 無」，真懸空 0 | 轉抄未量測之因果（同 A-GC12）| 已承認。R-G43(d) 補解析面後實測 963 → **0** |
| A-GC16 | **下放包 GC-07 §一之三處補充計數為人工相加，與機器計數不符；同包 §四.3 之 lint 代號未查現況即指派** | (1) Home 本 `Press`／`Select` 之數：下放包載 158／135，執行層機器計數為 **186／154**（母體＝`archive/forms_superseded/…Home_20260809.xlsx` sha12 `1895fb2a2b44`，`lint036.P_FIELDS` 之 `proc` 欄，逐行去編號後取行首單詞）。`Navigate to` 65 與 VF230 之五項全數相符。(2) 同 §一之 SWC `PROXI` 標為「41 **列**」，實為 **41 次出現／26 行／3 相異行／1 相異參數名** —— 15 行寫作 `PROXI <Param> = <value> (PROXI-independent)`，該詞於同一行出現兩次（15×2＋11＝41）。該標籤經上繳 §1、審閱 §三**三度沿用**。(3) §四.3 指派 lint 新檢查代號 `Q`，而 `lint036.CHECK_TITLES["Q"]` 已為「不可見字元」（R-10(a)，21 包）。 | `up/20260905_GC-07.md` 1-2 節；台帳 R-G70 之「(e) 語料標籤更正」註；`up/20260905_GC-08.md` | 人寫之數代機器之數（同 A-GC13）／指派代號前未查現況 | 已承認（`down/20260905_GC-07_review.md` §二）。(1) 以執行層值 186／154 為準；(2) 於台帳 R-G70 註記更正，**不改變 (e) 之結論**；(3) 執行層改用次一未佔用代號 **X**，判準與粒度照下放包 |
| A-GC17 | **下放包 GC-07 §三之二處條文例示未查 HMI 來源即寫入，違其所立條文自身之 (c)(d)** | `Press "Vehicle" on Menu Bar` —— `Vehicle` 於 Menu Bar §4.1 命名表（`spec-index/cache/SYS1_HMI_Menu_Bar_and_App_Drawer_…xlsx` 分頁 `Basic Report` 列 22，NRL-127734）之 `Feature Name`／`Drawer Name`／`Shortened Name` 三欄命中 **0**，只出現於 `App Category` 欄；`Set "SWITCH 3 Hold Last State" = "Disable"` —— HMI Settings List 分頁 `Settings` 列 564–588 之實際結構為 `21. Aux Switches` → `Aux 1`…`Aux 6` → `Type`／`Power Source`／`Recall Last State`，該字串為 VF230 之 VF 名非 HMI 標籤 | `up/20260905_GC-07.md` 3-4 節 | 條文例示未經量測（人寫代量測）—— **由該條文自身之施作者抓出** | 已承認（`down/20260905_GC-07_review.md` §二）。二例已改為全數有來源者（`"Apps"` → `"Settings"` → `"Aux Switches"`／`Set "Type" = "Latching"`），§5.8 並增一句「例中每個 hop 皆須有來源」 |
| A-GC18 | **`down/` 唯讀目錄被同名覆寫**：`20260905_GC-07_review.md` 由 B session 於 21:22:48 寫入，覆蓋分析層 A 之原檔；原檔以 `_A` 重落為 `20260905_GC-07_review_A.md` | 二檔並存於 `down/`；Pei 2026-09-05 裁 B 版無效、`_A` 版為有效審閱。已寫入台帳之 R-G70(e) PROXI 方向即取自 B 版，與 Pei 之裁定相反（`up/20260905_GC-09_notice.md` §1）| 同名寫入無互斥 | **GC-10 §二-1 處置**：被覆寫檔不刪不改（PROTOCOL 目錄唯讀），`INDEX.md` 3-1 節加註版本判準；防再犯條文 R-G62(c) 入 PROTOCOL |

| A-GC19 | **執行層 A：逾「不寫表」明文寫 `RULINGS.sha.tsv`，且以無效審閱之方向落 R-G70(e)** | (1) GC-09 §一-1-4 明文「不寫表」，而 `RULINGS.sha.tsv` mtime 21:31:46 為 A 所寫（R-G50(c) 違規）；(2) R-G70(e) 之 PROXI 方向取自 `down/20260905_GC-07_review.md`（B 版，21:22:48 覆寫），該版經 Pei 裁定無效（A-GC18），方向與 Pei 之裁定相反 | 違反包內明文／引用無效審閱 | 已由 GC-10 矯正為 v4.1（台帳＋IN＋lint）；**本條由執行層 B 代登**（GC-10 審閱 §二 指定），非 B 之責 |
| A-GC20 | **`PROXI <Param> = <值>（41 列）` 之 41 為命中次數，非列數** | 停手線實測：41 次出現／**26 行**／3 相異行／**1 個參數名**（`RRM_VPx_Steering_Wheel_Command_Type`；15 行含 `(PROXI-independent)` 致同行出現兩次）。該標籤於 GC-07 下放 §一、GC-07 審閱 §三、GC-11 §一 四度沿用 | 命中次數代母體計數（R-G69）| **不推翻 SWC 式裁定**（Pei 原話）；R-G70 沿革之數字改標「26 行／1 參數名」。VF230「152」與 SWC「215」是否亦為次數，GC-11 補遺 §2 令複核 —— **本包未複核**，見上繳 7-3 節 |

二十筆之共同形態：以樣本代母體、以人寫之數代機器之數、以人寫之理由代量測、以判準代其覆蓋、以規則代量測、轉抄未量測之因果。
防再犯條文：R-G50（全稱斷言須附查詢式與命中數）、R-G50(b)（對照向須回報被移出／還原之檔數）、
R-G50(c)（列為「不跑」之工具只准 `--check`／`--out <工作區>`）、
R-G16 補充（`docs/reports/*_YYYYMMDD.tsv` 常設排除於一切母體）。
**A-GC10 與 A-GC12 為兩層同時犯**：分析層據執行層之未量測敘述下裁，兩層皆未先跑母體查詢。
**編號偏離（GC-08）**：審閱指定登 `A-GC15`／`A-GC16`，而 **A-GC15 已為 GC-06 之發現所佔**。
依 `features/power/DATA_REQUESTS.md` 之 standing rule「不覆寫、改取次一可用號」，登為 **A-GC16／A-GC17**。
內容逐字照審閱 §二表，僅編號不同。**此為本輪第二次撞號**（第一次為 lint 代號 Q，見 A-GC16(3)）。
