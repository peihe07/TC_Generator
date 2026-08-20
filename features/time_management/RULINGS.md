# RULINGS — Time Management (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Time Management 之裁決權威；
跨 feature 條文承接時註明來源包。

來源包：`docs/handoff/00_intake_scaffold.md`（rev B, 2026-08-20）§1。

---

## R-TM1（Pei, 2026-08-20）—— feature 定名

```
R-TM1（Pei, 2026-08-20）—— feature 定名

feature 目錄 slug = `time_management`
feature.yaml `feature` = "Time Management"

素材四種名稱並存：
  - Pei 指定之 feature 名 = "Time Management"（本條採用）
  - spec 文件標題        = "CFTS_015 Time and Date"
  - SWRA 檔名            = "SWE1_Secure_DateTime"
  - 需求 ID family       = "TIME&DATE"（SYS-RA-TIME&DATE-* / SWE-RA-TIME&DATE-*）

「Time and Date」「Secure DateTime」「TIME&DATE」均為別名，不進目錄路徑。
ID family 之字面值當然照原樣使用於 req_id 欄與 traceability。

slug 一律小寫加底線，不得含空格 —— 依據 A-TM01 / A-TM04（見 §5）。
```

**執行層回報（2026-08-20）**：已套用。`features/time_management/` 建成，
無空格孿生目錄（下放包 §3 步驟 5 驗證通過）。`feature.yaml` 之 `feature:`
已由腳本產出值 `"Time_Management"` 手動改為 `"Time Management"`。

**執行層回報 —— 本條所列 SWRA 檔名與實測不符**：本條記為
`SWE1_Secure_DateTime`，repo 內實際檔名為 `SWE1_Secure_Date&Time.xlsx`
（含 `&`）。屬別名之字面差異，不影響本條之裁定內容（該名本就不進目錄路徑），
但該字面值已寫入 `feature.yaml` 之 `a03_report:`，其 `&` 之下游風險登記為
A-TM06。

---

## R-TM2（Pei, 2026-08-20）—— test_group 暫定值與其推翻條件

```
R-TM2（Pei, 2026-08-20）—— test_group 暫定值與其推翻條件

feature.yaml `test_group` 暫定 = "Time Management"。

本值為 [PROVISIONAL]，非最終。推翻條件（recon 時自動判定，Tier 0）：
  若 036 工作簿之 Test Group 欄（G 欄，實測為準）已存在非空值，
  則以工作簿實測值為準，直接覆寫本欄，不需再問。

理由：canon §4.1.1 之通則為 Test Group 等同 spec 文件標題（本例即
"Time and Date"），與 R-TM1 之 feature 名不同。工作簿既有值優先於兩者，
因為那是客戶已接受之欄位內容。三者若三不相同，於 Phase 2 升 Tier 2。
```

**執行層回報（2026-08-20）**：已套用，`feature.yaml` `test_group:` =
`"Time Management"`，行內註記 `# [PROVISIONAL] 見 R-TM2`。

**推翻條件目前無法判定**：036 工作簿缺件（見 DATA_REQUESTS #1 / A-TM07），
故 G 欄實測值不存在，本值維持 [PROVISIONAL]。036 落地後於 recon 自動判定。

---

## R-TM3（分析層自裁，2026-08-20）—— CLI 參數字面值與 anomaly 縮寫

```
R-TM3（分析層自裁，2026-08-20）—— CLI 參數字面值與 anomaly 縮寫

1. `intake.py` / `new_feature.py` 之 feature 參數一律使用 `Time_Management`
   （底線，非空格）。理由見 A-TM04：兩支腳本之目錄名推導為
   `feature.lower()`，無 slugify，空格會原樣進路徑。
2. 因 (1)，scaffold 產生之 `feature.yaml` 之 `feature:` 值會是
   `"Time_Management"`，與 R-TM1 不符 —— 執行層須於 scaffold 後手動改為
   `"Time Management"`（見 §3 步驟 5）。
3. anomaly 縮寫固定為 **TM**，不用腳本推導之 `TI`
   （`abbr = feature[:2].upper()`）。理由：本包已以 A-TM01…A-TM05 落檔，
   縮寫換寫會使既有編號失效。同一形態之先例：`home` 用 `A-H`、
   `user_profiles` 用 `A-UP`，皆非腳本推導值。

本條屬「量測與作業之技術性選擇」，分析層自裁範圍；其判準與風險已於本節揭露。
```

**執行層回報（2026-08-20）**：三項全數套用。

1. 兩支腳本均以 `Time_Management` 呼叫，未產生空格目錄。
2. `feature.yaml` 之 `feature:` 已手動改正（見 R-TM1 回報）。
3. 縮寫已由腳本產出之 `A-TInn` 改為 `A-TMnn`，改動點三處：
   `ANOMALIES.md` L4、L14，`PLAYBOOK.md` L97。改後全庫 `grep "A-TI"`
   無殘留。

---

## R-TM4（分析層自裁，2026-08-20）—— 解析結果之舉證形式

來源包：`docs/handoff/00Z_closure.md` §3.2。**雙向適用。**

```
R-TM4（分析層自裁，2026-08-20）—— 解析結果之舉證形式

凡以解析／抽取結果立論者（覆蓋率、缺口數、命中集、篩選結果），
除計數外須一併公布展開後之完整元素清單，供對造逐筆反驗。
只給計數者，覆核方一律退回，不進入實質討論。

本條對分析層與執行層雙向適用。00R §2 之 78 筆人工點數與本包 §2 之
regex 復現，即為分析層側之履行形態。
```

**執行層回報（2026-08-20）**：已知悉並套用。A-TM09 §B 之 78 筆與 48 筆
完整 id 清單即為履行。本 feature 往後凡涉解析結果之回報，一律附完整清單。

---

## R-TM5（Pei, 2026-08-20）—— 036 工作簿以母本為之

```
R-TM5（Pei, 2026-08-20）—— 036 工作簿以母本為之

本 feature 不索取客戶預填之 036 工作簿。036 以 R-G1 之全域母本
forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx 為之。

直接後果：workbook_state = BLANK。
A-TM07（036 缺件 → workbook_state 無法判定）由本條解消，轉 RESOLVED。
```

**執行層回報（2026-08-20）**：已套用。母本複本落於 `inputs/`，SHA256
與母本相同（雙向實測 + `cmp` 逐位元組比對 identical，見上繳包 01 §3）。
`feature.yaml` `paths.workbook` 已指向該複本。A-TM07 已轉 RESOLVED。

**連鎖後果已一併處置**：母本為 rev C 版面，而 scaffold 模板為 rev A/B，
兩者不相容。`feature.yaml` 之 `workbook` 段依 FORMS.md 實測值更正五處
（sheet 名、design_method Q→R、functional_safety R→S、author Z→AA、
remarks 確認 AH），`done_region` 改 `detection: "none"`，
`write_back.fill_test_group_set` 改 `true`。逐項對照見上繳包 01 §2。

---

## R-TM6（Pei, 2026-08-20）—— 覆蓋稽核分母，並分拆 A-TM02

```
R-TM6（Pei, 2026-08-20）—— 覆蓋稽核分母，並分拆 A-TM02

1. 覆蓋稽核之分母取 SYS2 之 Functional Requirement 全集 = 126，
   不取 SWE leaf 數 22。取 22 會得出「已全覆蓋」之假象。

2. A-TM02 拆為兩條，各自獨立處置：
   A-TM02a（版本身分）— SWE1_Secure_Date&Time.xlsx 是否為權威 037。
                        Tier 3，隨 RD-1 上問。
   A-TM09（內容缺口）— 48 筆 SYS2 FR 無對應 SWE leaf。
                        縱使 A-TM02a 裁定手上這件即權威 037，本缺口依然存在。

3. 48 筆缺口之處置為「宣告」，非「補生成」：
   TC 生成單位仍為 037 之 22 筆 SWE leaf。48 筆既無 leaf，
   即不得為其自行創設 leaf 或自行分解 SYS2 條文以湊覆蓋 ——
   §8.2「TC 作者不得重新分解、合併或發明 RD 項目」，
   §8.4.1「不得捏造來源未述之值」。
   缺口以 RD-1 上問，並於交付件之覆蓋稽核中明列。
```

**執行層回報（2026-08-20）**：已知悉。分母 126 已記入 `DECISIONS.md`。
A-TM02 已拆為 A-TM02a（版本身分，Tier 3）與 A-TM09（內容缺口）。
48 筆缺口之完整 id 清單見 A-TM09 §B，供 RD-1 引用。

**第 3 項之約束已理解並記錄**：48 筆不得補生成、不得創設 leaf、不得
自行分解 SYS2 條文。TC 生成單位維持 037 之 22 筆 SWE leaf。本條將於
Phase 3 framework 與 Phase 4 生成時逐批複查。

---

## R-TM7（分析層自裁，2026-08-20）—— 下放包之指令須經實測

來源包：`docs/handoff/01R_review_of_upstream.md` §1。

```
R-TM7（分析層自裁，2026-08-20）—— 下放包之指令須經實測

下放包所載之任何指令，其 CLI 介面（參數名、必填性、參數語意）須先讀該
腳本之 argparse 定義後方可寫入，不得依既有印象或他腳本之慣例類推。
無法實測時，寫「指令待執行層依 argparse 確認」，不得寫一條看似可執行
但未經查證之指令。

依據：01 包 §5（recon.py 之 --feature）與 00 包 rev A 之同型缺失。
```

**執行層回報（2026-08-20）**：已知悉。本條主要拘束分析層，執行層側之
對應義務為：遇指令不可執行時，先讀 argparse 再修正並回報實際失敗訊息，
而非猜測參數形態反覆試誤。01 包之兩次失敗訊息已逐字回報於上繳 01 §0。

**執行層補充**：本條所指之失誤形態（以「應該長什麼樣」代替「實際長什麼樣」）
與 A-TM09 首版之代理判準、01 包 §4(4) 之雙空格誤判同族。執行層側之防範
已立為作業慣例：**驗證他人規則時，用該規則自身之比對函式，不用外觀相近
之自製比對。**

---

## R-TM8（Pei 授權分析層裁定，2026-08-20）—— test_group = "Time and Date"

來源包：`docs/handoff/01Z_naming_rulings.md`。

```
R-TM8（Pei 授權分析層裁定，2026-08-20）—— test_group = "Time and Date"

workbook Test Group 欄（G）之值定為 "Time and Date"。
feature.yaml `test_group` 由 [PROVISIONAL] "Time Management" 改為
"Time and Date"，並移除 [PROVISIONAL] 標記。

理由：
1. R-TM2 之推翻條件（工作簿既有非空值優先）在 BLANK 下永不觸發，
   故落回 canon §4.1.1 之通則：Test Group 等同 spec 文件標題。
   本 feature 之 spec 文件標題為 CFTS_015 Time and Date。
2. 交付件之讀者為客戶。客戶側之三個識別（spec 標題、req id family
   TIME&DATE、CFTS 編號 015）全部指向 "Time and Date"。
3. "Time Management" 不出現於任何上游文件，僅為 Pei 之內部稱謂。
   採之等於在交付件中新增第四個名稱。

R-TM1 不受影響：feature 名與目錄 slug 維持 "Time Management" /
`time_management`。R-TM1 已言「別名不進路徑」；本條為其反向 ——
路徑名亦不必進工作簿。內部識別與交付識別本即兩層。
```

**執行層回報（2026-08-20）**：已套用。`feature.yaml`：

```
改前：test_group: "Time Management"           # [PROVISIONAL] 見 R-TM2；…
改後：test_group: "Time and Date"             # R-TM8；…
```

`feature:` 未動，維持 `"Time Management"`（R-TM1）。**R-TM2 之
[PROVISIONAL] 標記至此解除**，其推翻條件經確認為死條件（母本 BLANK，
G 欄永無既有值），由本條實裁取代。

---

## R-TM9（Pei 授權分析層裁定，2026-08-20）—— 母本 Scope 欄（`D5`）之值

**注意：本條步驟 1 已由 R-TM9-A1 撤銷改寫，見下條。原文保留為軌跡。**

```
R-TM9（Pei 授權分析層裁定，2026-08-20）—— Scope 欄值

D5 之 feature 識別段定為 "Time-and-Date-HMI-V0.1"，與 R-TM8 一致。

前綴段不在本條裁定範圍：分析層本次無法對 Home v2 交付件實測，
故不得書寫其字面（§8.4.1，不得捏造來源未述之值）。

執行層須：
1. 開啟 features/home/output/…_Home_20260720.xlsx（FORMS.md 記載其
   SHA256 為 cfc007f3…、tag fw036-home-regen-v2），實測其 D5 全字串
2. 以該字串之前綴段 + 本條之 "Time-and-Date-HMI-V0.1" 組成本 feature 之
   D5 值，回報組成前後之兩個字串
3. 若該檔不存在或 D5 為空，停止並回報，不得自行擬前綴

禁止來源：archive/forms_superseded/…_SWQT_Home_20260809.xlsx。
FORMS.md 之 provenance warning 已載明該複本之 D5 為未修正之
"…AppDrawer-Projection-SWE1HMI-V0.1"（A-H26 缺陷本身）。

A-TM11 於上列三步完成並回報後轉 RESOLVED。
```

---

## R-TM9-A1（分析層，2026-08-20）—— Scope 值之前綴段改為待決

來源包：`docs/handoff/01Z-A1_amendment.md` §2。

```
R-TM9-A1（分析層，2026-08-20）—— Scope 值之前綴段改為待決

R-TM9 之「D5 之 feature 識別段 = Time-and-Date-HMI-V0.1」不變。

其步驟 1 之來源 features/home/output/…_Home_20260720.xlsx 經實測不存在，
該步驟不可執行，撤銷。改為：

1. 執行層開啟 archive/forms_superseded/…_SWQT_Home_20260809.xlsx，
   讀出其 D5 全字串。該值為 A-H26 之未修正值
   （FORMS.md 載為 "…AppDrawer-Projection-SWE1HMI-V0.1"），
   **不得採為本 feature 之值**，僅用以取得前綴段之字面。
2. 回報該全字串，並標出前綴段與 feature 識別段之切分點。
3. 切分正確與否須經分析層覆核後，方得組成本 feature 之 D5 值。
   —— 因來源本身即缺陷件，其前綴段是否亦受該缺陷影響，
   在切分被覆核前不能假定。

在覆核完成前，D5 維持空白。空白是可見狀態，錯值不是。
A-TM11 維持 PENDING，不因本件轉 RESOLVED。
```

**執行層回報（2026-08-20）**：三步已執行，**未組值、未填 D5**。
實測全字串與切分提議見上繳包 `01Z_corrections.md` §3。

**執行層取得獨立第二樣本**，可回答本條所擱置之「前綴段是否亦受 A-H26
影響」—— 詳見上繳 §3.2 與 A-TM14 末節。**該證據僅供分析層覆核，
執行層未據以組值。**

---

## R-TM10（Pei 授權分析層裁定，2026-08-20）—— 跨 feature 樣式參照

**注意：本條已由 R-TM10-A1 全條暫停生效（SUSPENDED），見下條。
原文保留為軌跡，暫停期間不得援引。**

```
R-TM10（Pei 授權分析層裁定，2026-08-20）—— 准以 Home 為樣式參照，三重限縮

准。canon §0 之 cross-feature exemplar admissibility 於本 feature 成立，
但受下列三項限縮，缺一即不得援引：

(a) 來源唯一且須實測
    僅 features/home/output/…_Home_20260720.xlsx
    （tag fw036-home-regen-v2，FORMS.md 載 SHA256 cfc007f3…）。
    援引前須實測該檔之 SHA256 並與 FORMS.md 記載比對，記錄於上繳包。

    明文禁止 archive/forms_superseded/…_SWQT_Home_20260809.xlsx。
    依 FORMS.md provenance warning，該複本相對 Home v2 有四項編輯污染：
    D5 Scope 未修正、F 欄 216 列全填 tc_id、G 欄 216 列全填 "CoreHMI"、
    K 欄 216 列全填 "NA"、Z 欄 author 為 "ArifChen" 而非 "Arif"。
    以其為樣式來源會把 K 欄全 NA 與 G 欄 CoreHMI 一併帶入。

(b) 只及於樣式，不及於內容體系
    可援引：步驟措辭與動詞選用、ER 句式、標點與空白慣例、
            UI 標籤引號慣例、baseline 比對之寫法。
    不得援引：spec_reference 格式（Home 為 spec_mode A 之
            文件名_章節；本 feature 之章節經 SYS2 來源物件 id 錨鏈取得，
            兩者來源不同）、test_group / test_set 值、priority 分佈、
            tc_id 體系、Input Test Data 之填法。

(c) 樣式參照不是證據仲裁者
    canon §1.1 第三層在本 feature 依然不存在，本條不回復之。
    Home 樣式為「可援引之先例」，非「爭議之裁決依據」。
    - pilot 發現不得以「Home 這樣寫」為由駁回
    - 亦不得以「Home 沒這樣寫」為由逕定為 defect
    爭議一律回到條文（§4–§12）與本 feature 之 profile。

連帶：因第三層缺席，pilot review 之發現分類（canon §1.2 之
defect / style-divergence / note）少了 done-region check 這一道過濾，
分類結果直接成立。reviewer 之發現門檻因此相對較低，
pilot 之爭議應預期多於 Home 與 AMFM。
```

---

## R-TM10-A1（分析層，2026-08-20）—— 樣式參照暫停生效

來源包：`docs/handoff/01Z-A1_amendment.md` §3。

```
R-TM10-A1（分析層，2026-08-20）—— 樣式參照暫停生效

R-TM10 之三重限縮不變，但其 (a) 所指定之唯一來源經實測不存在，
故 R-TM10 全條 暫停生效（SUSPENDED），非撤銷。

暫停期間：pilot review 與 TC 生成一律僅依條文（§4–§12）與本 feature
之 profile，不得援引任何他 feature 之既成樣式。

解除條件（二者擇一，均須 Pei 裁）：
(a) Home v2 交付件被取回磁碟，實測 SHA256 = FORMS.md 所載 cfc007f3…，
    R-TM10 原文即生效；或
(b) Pei 另裁一個替代之樣式來源。
    此時 R-TM10(b)(c) 之限縮原文照套於新來源，(a) 改寫其路徑與雜湊。

明文重申：archive/forms_superseded/…_SWQT_Home_20260809.xlsx
不得作為 (b) 之替代來源。它在磁碟上而 v2 不在，正是最容易被順手取用
之路徑；FORMS.md 之 provenance warning 已列其四項污染
（D5 未修正、F 欄全填、G 欄全填 CoreHMI、K 欄全填 NA、author 為 ArifChen），
其中 K 欄與 G 欄之污染會直接汙染 TC 內容而非僅樣式。
```

**執行層回報（2026-08-20）**：已知悉，**SUSPENDED 狀態下未援引任何他
feature 樣式**。

**執行層於 T2 之搜尋中發現一個分析層未知之候選來源**（交付路徑之
`…_SWQT_Home_20260809.xlsx`，SHA `469b2f6d…`，與 archive 同名但**不同
內容**）。依本條，該檔**不自動成為解除條件 (b) 之來源** —— 解除須 Pei 裁。
執行層僅登記事實於 A-TM14，未援引、未複製、未採用。

---

## R-TM9-A2 — 撤回 R-TM9 之 D5 內容，改綁 A-TM02a

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A3_review.md` §3.2）

R-TM9 及 R-TM9-A1 關於 D5 值之全部內容撤回，包括
「feature 識別段 = Time-and-Date-HMI-V0.1」與前綴段之切分作業。
撤回理由：D5 之語意為「本工作簿所依據之 037 報告之文件識別」，
非 feature 標籤，故不可由 feature 名組成。

證據（交付路徑實測，2026-08-20）：
  Core HMI/HomeHMI/            → FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx
  Core HMI/Menu Bar and AppDrawer/ → FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx
  User Profiles/               → FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx
  Time Management/             → 無任何符合該形態之檔案

新規定：
1. D5 之值 = 本 feature 所依據之 037 報告之檔名（去副檔名），逐字照抄。
2. 該值在 A-TM02a（037 身分）裁定前無法取得。D5 維持空白。
3. 空白是可見狀態；指向不存在文件之值不是。任何情況下不得以
   feature 名、spec 標題或類推形態組出一個字串填入（§8.4.1）。
4. A-TM11 之解除條件改為：A-TM02a 裁定 + 037 檔名逐字實測。
   不再綁 Home 之前綴段切分。

R-TM8（test_group = "Time and Date"）不受本條影響 —— 該欄語意為功能
模組名，與 D5 之文件識別語意不同，兩者本不必一致。

## R-TM11 — 驗收條件不得預設 commit 節奏

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A3_review.md` §2）

下放包之驗收條件不得以 `git diff` 之範圍為判準。本專案全部 git 操作屬
Pei，執行層之工作樹持續累積跨往返之未提交更正，故 `git diff` 反映的是
「自上次 commit 以來」而非「本包」。

單行修改之正確驗收方式為：修改前 assert 目標字串存在且唯一、
以 count=1 取代、修改後複查該行。

依據：01Z-A2 T1 之驗收條件不可能成立。與 R-TM7 同族 —— 前者是指令
未經實測，本條是驗收條件未經可行性檢查。

## R-TM12 — 下放包一律附可執行指令段

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A4_command_set.md`）

每一個下放包末尾須有「指令」節，內容為執行層可直接照做之動作：
shell 指令、或逐字之貼入區塊與其插入位置。不得以「執行層下一步」之
散文條列代替。

R-TM7（指令須經實測）之射程限於有 CLI 之指令；檔案編輯、條文登記、
索引更新無 CLI 可查，一律直接寫死逐字內容與插入位置。

依據：00 rev A（無指令）、01（指令錯誤）、01Z-A3（散文條列）三次同型
缺失；01Z-A2 為唯一正確形態。

## R-TM13 — 條文之作廢一律加註保留，不刪除

（分析層自裁，2026-08-20。上游包 `docs/handoff/02_framework.md` §1.1）

任何已寫入 RULINGS.md／ANOMALIES.md 之條文、提案或推理，經證否或撤銷後
一律保留原文，加刪除線並以區塊引言標明作廢時點、依據包、與作廢理由。
下放包不得使用「整段換為」「刪除該段」等措辭。

被證否的推理本身是證據：它記錄了誤讀曾經發生，而誤讀之可重複性
（不同人在有對照樣本時仍犯同一錯）是判斷該問題嚴重性的訊號。

依據：01Z-A4 T4 之措辭與本專案既有作法矛盾（A-TM09 §D、R-TM9／R-TM10、
A-TM12 首版、T6 自身）。執行層於 01Z-A4 上繳 §3 指出之。
本條與 R-TM11／R-TM12 同族：三者皆為下放包自身之缺陷。

**執行層回報（2026-08-20）**：已登記。**本條之登記未見於 02 包 §3 之
T1–T4 指派**，執行層依歷來常規義務（每一新裁決逐字寫入 `RULINGS.md`）
逕行，並於上繳標示。本包無「不自行調整」之限制措辭，故與 `01Z-A4`
§4 之 A-TM02a 情形不同（該次有明文限制，故僅提請未逕改）。

**本條已於本包即時適用**：A-TM11 之舊提案段依此保留（該處置早於本條
成文，本條為其追認）。
