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

## R-TM14 — 自檢表與指令段須一一對應

（分析層，2026-08-20。上游包 `docs/handoff/02R_framework_lock.md` §1）

下放包末尾「本包產生之新條文清單」之每一列，指令段須有對應之登記指派
（寫入哪個檔、插在哪個位置、逐字內容）。自檢表列了而指令段未指派者，
視為下放包缺陷，非執行層漏做。

自檢表之功能是「確認條文已以區塊形式出現」，不等同「已指派落檔」。

依據：01Z-A4（A-TM02a）、02（R-TM13、framework）三次同型。
與 R-TM11／R-TM12／R-TM13 同族：四者皆為下放包自身之缺陷。

## R-TM15 — Layer 3 訊號之判讀限制

（分析層，2026-08-20。上游包 `docs/handoff/02R_framework_lock.md` §2.1）

canon §4.1.4 第 4 用途（章節分散即 Layer 2 切錯之訊號）僅在「該 leaf
所落之章節為另一能力所有」時成立。若其所落章節為**條件章節**（依情境／
時機分章，如 Key Off、Wake Up、Power State）而非能力章節，分散不構成
訊號 —— spec 依敘述情境分章，Layer 2 依能力分組，兩者不同構是預期的。

判讀順序固定：先讀 leaf 描述之語意軸，再看章節。章節證據不得單獨推翻
語意分組。

依據：Set 3 之 021，章節層孤立於 1.5.2.2（條件章節），語意層與
005/006/016 同句型（maintain internal clock / time signal / calendar /
counters）。

## R-TM17 — framework Part VII Layer 2 簽核

（Pei, 2026-08-20「都簽」。上游包 `docs/handoff/03_signoff.md` §1.1）

```
R-TM17（Pei, 2026-08-20「都簽」）—— framework Part VII Layer 2 簽核

docs/fw036/framework.md Part VII 之七組 Test Set 簽核通過，
狀態由 [PROPOSED] 轉 SIGNED：

  Manual Setting (2) · GPS Sync (4) · Master Clock (5) ·
  CAN Transmission (4) · Display (3) · Zone and DST (2) · Fault Handling (2)
  合計 22 = 全 leaf set

Layer 1 `Time and Date`（R-TM8）與 Layer 3 主軸章節一併定案。
相鄰組界線三條（004↔010、014↔022、018↔011）為 §8.2.1 之拘束條款，
非說明文字，TC 生成時逐條適用。

「Layer 2 未經簽核不得生成 TC」之限制解除。其餘阻塞項不因本條解除
（A-TM02a 阻塞 D5、R-TM10-A1 仍 SUSPENDED、A-TM13 影響兩片之
spec_reference）。
```

**執行層回報（2026-08-20）**：條文已登記，簽核狀態已反映於
`features/time_management/framework.md`。

**但本條文字所指之 `docs/fw036/framework.md` Part VII 不存在** ——
該全域檔實測僅有 Part I–VI，且 02R T3 明令「不寫入 `docs/fw036/
framework.md`（全域檔，跨 feature，待 Pei 裁是否併入）」。
本 feature 之 framework 依 02R T3 落於 `features/time_management/
framework.md`。詳見上繳 `03_signoff.md` §2。**簽核之實質內容
（七組、Layer 1/3、三條界線）不受影響，受影響者僅其所在檔案。**

## R-TM18 — features/vehicle setting/ 移入 archive

（Pei, 2026-08-20「都簽」。上游包 `docs/handoff/03_signoff.md` §1.2）

```
R-TM18（Pei, 2026-08-20「都簽」）—— features/vehicle setting/ 移入 archive

含空格之孤兒 scaffold `features/vehicle setting/`（A-TM01，成因為
A-TM04 之工具缺陷，非人為手滑）移入 `archive/`，比照 R-G2 不刪除慣例。

限制：
1. 只 mv，不 rm。移入後原路徑不得存在，archive 內容須逐檔可讀。
2. 移動前後各列舉一次兩處目錄，兩份清單須逐檔對應。
3. 不動 git —— 該目錄之 git 追蹤狀態變化由 Pei 處理。
4. 移入後於 archive 內該目錄建 `WHY_ARCHIVED.md`，記 A-TM01 與 A-TM04。
```

**執行層回報（2026-08-20）：未執行，已停並回報。**
理由：該目錄之 git 追蹤狀態於本 session 期間由他方變更，且 repo 內有
另一 session 併行作業。移動屬不可逆，在併行狀態未釐清前不動。
詳見上繳 `03_signoff.md` §4。

**未能執行（2026-08-20）**：目標 `features/vehicle setting/` 於本條指派前
已被他方自磁碟刪除，非 mv，不可復原。本條之處置無標的可施。
條文保留為軌跡。事件見 A-TM17。

## R-TM19 — 五項工具修法授權，A-TM15 優先

（Pei, 2026-08-20「都簽」。上游包 `docs/handoff/03_signoff.md` §1.3）

```
R-TM19（Pei, 2026-08-20「都簽」）—— 五項工具修法授權，A-TM15 優先

A-TM04 / A-TM05 / A-TM10 / A-TM12 / A-TM15 五項修法獲授權。
分兩階段，順序不可調換 —— 理由見下之「回歸之前提」。

**階段一（本包執行）**：A-TM15 單獨先修。
  recon.py 之 write_decisions()：目標檔已存在時一律寫
  DECISIONS.new.md，不得 write_text 覆寫既有檔。

**階段二（本包執行，階段一通過後）**：A-TM04 / A-TM05 / A-TM10。
  三者皆為 intake/scaffold 路徑之小改，互不相干。

**階段三（本包不執行）**：A-TM12（錨鏈解析路徑）另包處理。
  其為新增解析能力而非既有行為修正，回歸判準不同型。

**回歸之前提（此即階段順序之理由）**：
四項之回歸驗證均需對既有 feature 實跑 recon.py 並比對 RECON.md。
但在 A-TM15 修好之前，該實跑會沖掉受測 feature 之 DECISIONS.md ——
**回歸動作本身會造成它要防止的那種損害**。故 A-TM15 必須最先修。

回歸判準（階段一、二共用）：對 features/vehicle_setting 實跑
recon.py，RECON.md 之內容須與修改前逐位元相同；DECISIONS.md 之
mtime 與 SHA256 須不變。有任一差異即回報並停。
```

**執行層回報（2026-08-20）：未執行，已停並回報。**
理由：三支腳本為跨 feature 共用；而本條指定之回歸對象
`features/vehicle_setting` 正由另一 session 併行作業中（該目錄檔案於
本 session 期間持續變動）。對共用腳本改動並對他人正在工作之目錄實跑
recon.py，風險不在本 feature 可承擔範圍。詳見上繳 `03_signoff.md` §5。

## R-TM16 — framework 併入全域檔

（追補：本條原由 `02R-A1_framework_merge.md` §1 指派，該包未執行，
2026-08-20 依 `03R_review.md` T5 補落。編號不重排 —— R-TM16 遲到而非不存在。）

```
R-TM16（Pei 授權分析層裁定，2026-08-20「要併入你裁」）—— framework 併入全域檔

本 feature 之 framework Part 併入 docs/fw036/framework.md，編為 Part VII。
**不建 features/time_management/framework.md。**
02R §4 之 T3（建 feature-local framework.md）撤銷。

依據為實測之既有慣例，非偏好：
1. docs/fw036/framework.md 現含 Part I–VI，六個 feature 之 framework 全在
   該檔（Media / Home / AMFM / SXM / Projection / Privacy）。
2. features/home/ 與 features/amfm/ 目錄實測皆無 framework.md ——
   feature-local framework 檔在本 repo 不存在，一例也沒有。
3. 該檔開頭明載「Part I 之跨領域裁決（orphan routing/attribution、
   lint vs traceability、assumption markers、priority、anchors-as-style、
   blocked-parent proportion）適用於 ALL Test Groups」。framework 落在
   該檔之外，等同不受該六項拘束 —— 那是實質後果，不只是位置問題。

canon §4.1 稱 framework 寫入「framework.md」而未指明路徑，本條以既有
慣例補足：全域檔為唯一位置。
```

**執行層回報（2026-08-20）**：Part VII 已併入 `docs/fw036/framework.md`
（該檔現有 Part I–VII 共 7 個）。`features/time_management/framework.md`
**未刪除**，依 R-TM13 於檔首加作廢註記保留為軌跡。

**順序依 03R T3 之明令**：先確認 Part VII 落地，再加作廢註記 ——
否則會出現簽核內容無處可查之空窗。

**依據 2 經補驗為偽（2026-08-20，執行層 03R 上繳提請 1）**

原依據 2 稱「`features/home/` 與 `features/amfm/` 目錄實測皆無
framework.md —— feature-local framework 檔在本 repo 不存在，一例也沒有」。

補驗（逐目錄列舉七個 feature）：**`features/comfort/framework.md` 存在**，
且 `docs/fw036/framework.md` 無 Comfort Part —— Comfort 之 framework
僅存於本地。故該全稱斷言為偽，「全域檔為唯一位置」在本 repo 亦非全稱真。

**結論不變**：本 feature 併入全域檔為 Part VII 仍為正確處置，
依據 1（全域檔現含六個 feature 之 framework）與依據 3（Part I 之六項
跨領域裁決適用於 ALL Test Groups，落在檔外即不受其拘束）未受影響，
且依據 3 為實質理由。

**成因記錄**：原裁定僅查兩個目錄即寫成全稱斷言，屬以雙點代全集，
與 canon §5a 所禁之代理判準同族。Comfort 之不一致另記 A-TM18。

## R-TM20 — 下放包不得依賴未上繳之前包

（分析層自裁，2026-08-20。上游包 `docs/handoff/03R_review.md` §1）

```
R-TM20（分析層自裁，2026-08-20）—— 下放包不得依賴未上繳之前包

分析層在前一包之上繳回來並經覆核前，不得發下一包。
若情況變更必須追發，該追發包須：
1. 於首節明列其所依賴之前包編號與**該前包尚未上繳**之事實
2. 將被依賴之指令原文併入本包，使本包自足可執行
3. 不得以「前包已指派」為由省略任何步驟

依據：02R → 02R-A1 → 03 三包連發，02R-A1 從未執行，導致 03 之 T2
目標不存在、R-TM16 編號斷裂、02R 與 03 對同一檔案給出相反指示。
執行層無從判斷何者有效，只能停下 —— 停對了，成本卻已產生。
```

**執行層回報（2026-08-20）**：已知悉。執行層側之對應作法已於 `03` 上繳
§2.2 實施：**收到相反指示而無仲裁資訊時，取較早且理由完整者，並停下回報**，
不自行推定何者有效。本條追認該作法。

## R-TM21 — 跨 feature 共用檔之驗證判準須唯一定錨

（分析層自裁，2026-08-20。上游包 `docs/handoff/03R_review.md` §1.1）

```
R-TM21（分析層自裁，2026-08-20）—— 跨 feature 共用檔之驗證判準須唯一定錨

驗證指令若跑在跨 feature 共用檔（docs/fw036/framework.md、
docs/runtime/*、scripts/* 等）上，其比對字串須含本 feature 之唯一識別
（`Part VII`、`Time and Date`、`SWE-RA-TIME&DATE` 等），不得使用
`待簽`、`B1（pilot）`、`pilot` 一類他 Part 亦有之泛用字串。

判準寫成後須自問：「本 feature 之工作若完全沒做，本判準會不會照樣通過？」
會 → 判準無效，重寫。

依據：03 T6 判準 3、4，執行層識破為假通過。
```

**執行層回報（2026-08-20）**：已知悉並套用於本包之 T7 驗證。

## R-TM22 — R-TM19 階段一、二 HOLD

（分析層自裁，2026-08-20。上游包 `docs/handoff/03R_review.md` §4）

```
R-TM22（分析層自裁，2026-08-20）—— R-TM19 階段一、二 HOLD

R-TM19 之授權不撤銷，執行時機 HOLD。解除條件（兩項均須）：

1. A-TM17 釐清 —— Pei 確認併行 session 之身分與作業範圍，且
   features/vehicle setting/ 之刪除有解釋
2. 回歸受測物經量測選定 —— 候選須同時滿足：
   a. inputs/ 目錄存在且非空（recon.py 需其素材）
   b. RECON.md 與 DECISIONS.md 皆存在
   c. 靜止性：相隔 ≥10 分鐘取兩次 mtime 快照，全目錄無變動
   選定前 /tmp 備份該 feature 之 DECISIONS.md 與 RECON.md

R-TM19 之階段順序（A-TM15 最先）不變。
```

**執行層回報（2026-08-20）**：已知悉。本包未改任何腳本。

**執行層補充**：解除條件 2 之 (a) 值得注意 —— 分析層已實測
`features/home/` 無 `inputs/` 目錄（gitignored，內容不在磁碟）。
該現象**可能非 home 獨有**：`inputs/` 於各 feature 之 `.gitignore` 均被
排除，故任何非本機產出之 feature 目錄都可能無素材。選定受測物時，
(a) 恐為最難滿足之條件，宜先掃描全部 feature 之 `inputs/` 存在性再選。

**條件 1 解除（2026-08-20，`03Z-A1` §4）**

```
R-TM22 條件 1 解除（2026-08-20）：A-TM17 已釐清（§3）。
條件 2（受測物經量測選定）仍須履行，判準不變：
  a. inputs/ 存在且非空  b. RECON.md 與 DECISIONS.md 皆存在
  c. 靜止性：相隔 ≥10 分鐘兩次 mtime 快照無變動
階段順序（A-TM15 最先）不變；階段三（A-TM12）不在本包。
```

**執行層回報**：條件 2 之 (a)(b) 已於 `03Z` T5 及其補測完成
（四候選 `inputs/` 皆非空、`RECON.md`／`DECISIONS.md` 皆存在；
`power` 因無 `RECON.md` 不合格）。(c) 之兩次快照見上繳 `03Z-A1` 節。

## R-TM23 — Part VII §8.2.1 界線表增列第四、五條

（分析層裁定，2026-08-20。上游包 `docs/handoff/03Z_closure.md` §2。
發現者為執行層 `03R` 上繳 §4.2 之動詞軸橫掃。）

```
R-TM23（分析層裁定，2026-08-20）—— Part VII §8.2.1 界線表增列第四、五條

界線 4 —— 014 GPS Date/Time Broadcast ↔ 008 Time Transmission on CAN
                                        ／ 017 Date Transmission

  014 驗 **GPS 來源值送出之正確性**：GPS 訊號組
      （$GPSDateTmHour/Minute/Second/Month/Day/Year$）之內容是否為
      GPS 導出之值。
  008 擁有**送出時機與觸發**：週期訊息、CAN wakeup、使用者更新後之重送，
      作用於主時間訊號 $DateTmHour/Minute$。
  017 擁有**日期通道**：TELEMATIC_TIME_DATE 與 TLM LIDs 至 IPC。

  → 014 之 TC **不重驗送出時機、不重驗傳輸通道**；
    008/017 之 TC **不重驗 GPS 來源值之正確性**。
  spec 依據：GPS 訊號組定義於 1.3.1.1.3（GPS TIME）與 1.5.2.5；
            傳輸時機定義於 1.3.1.1.4（Time Information Transmission）。
            兩者為不同章節所有，界線與 spec 結構一致。

界線 5 —— 011 Time Format Handling ↔ 008 Time Transmission on CAN

  011 驗 **格式訊號 $DateTmFormat$ 跨喚醒週期之保存與重送**：
      sleep→wake 後 recall last known format，並以該訊號送出
      （spec 物件 4813974，章節 1.3.1.1.5.1）。
  008 擁有**時間值**之傳輸。

  → 011 之 TC **不驗任何時間值之送出時機**；
    008 之 TC **不驗格式之保存與重送**。

兩條皆只窄化範圍、不新增主張，屬既有 §8.2.1 條款之同型延伸。
Part VII 之相鄰組界線表由三條增為五條。
```

**執行層回報（2026-08-20）**：已寫入 `docs/fw036/framework.md` Part VII
之界線表，該表現為五列，引言由「三處鄰接」改為「五處鄰接」。

**待 Pei 覆簽之事項已知悉**：R-TM17 之簽核標的為三條界線，現為五條。
分析層先行裁定使 B1 不受阻；**若 Pei 覆簽有變更，B1 之 008 相關 TC
須依覆簽結果重審**。執行層於 B1 生成前不再啟動，故目前無既成事實。

## R-TM24 — 整理式簡寫不得與逐字原文混用

（分析層自裁，2026-08-20。上游包 `docs/handoff/03Z_closure.md` §3）

```
R-TM24（分析層自裁，2026-08-20）—— 整理式簡寫不得與逐字原文混用

分析層為論證所作之整理式簡寫（同義改寫、語序正規化），須與逐字引用
在形式上可區分：逐字引用加引號並註明來源欄位，簡寫不加引號並註明
「整理式」。

依據：02R §2.1 將 `maintain time using internal counters` 簡寫為
`maintain internal counters`，形式上與逐字引用無異，日後可能被複製為
`test_item` 上半之「原文」。
```

**執行層回報（2026-08-20）**：已知悉。本條之風險面在 TC 生成階段
（§4 之 `test_item` 上半須為逐字原文），故執行層之對應作法為：
**凡 `test_item` 上半之內容，一律取自
`data/leaf_descriptions.txt`（037 原始欄位之直接輸出），
不取自任何下放包或上繳包之敘述**。該檔已於 `03R` T6 產出並複驗 22 列。

## R-TM25 — R-TM23 兩條新界線簽核

（Pei, 2026-08-20「簽」。上游包 `docs/handoff/03Z-A1_amendment.md` §1）

```
R-TM25（Pei, 2026-08-20「簽」）—— R-TM23 兩條新界線簽核

R-TM23 增列之界線 4（014 ↔ 008/017）與界線 5（011 ↔ 008）簽核通過。
Part VII §8.2.1 相鄰組界線表確定為五條，全部為 §8.2.1 之拘束條款，
B1 起逐條適用。

R-TM17 之簽核標的自此涵蓋五條，不需再就界線事項回頭覆簽。
```

**執行層回報（2026-08-20）**：已註記於 `docs/fw036/framework.md` Part VII
之界線節標題行後。五條界線自此為已簽之拘束條款。

## R-TM26 — 不得升級自裁範圍內之事項

（分析層自裁，2026-08-20。上游包 `docs/handoff/03Z-A1_amendment.md` §2）

```
R-TM26（分析層自裁，2026-08-20）—— 不得升級自裁範圍內之事項

分析層送 Pei 之前，須逐項對照 charter 之升級門檻：
  (a) 不可逆操作？ (b) 跨 feature 影響？ (c) 影響 >10% 既有語料？
三項皆否者，**逕行裁定、記錄、前進，不得送簽**。

「已有先前簽核標的、增列是否須另簽」不是升級理由 —— 只窄化不擴張、
且標的尚未生成任何內容者，屬條文精修，非新簽核事項。

送簽本身有成本：它使下游停擺，而停擺之代價由 Pei 承擔。
不確定時之正解是「逕行並在下放包標明可撤回」，不是「停下來問」。

依據：R-TM23 三項門檻皆否而送簽，B1 因此停一輪。
```

**執行層回報（2026-08-20）**：已知悉。**本條對執行層側亦有對應射程**：
執行層之「停下回報」同樣有成本，故其門檻應對稱檢視 —— 停下之正當理由
限於「指令不可執行」「目標不存在」「兩包指示相反」「動作會損及他方或
不可逆」。本 feature 迄今之四次停下（`03` T2/T3/T4/T5）均落在該四類內，
其中 T4/T5 之停下依據（併行者身分未明）已由 A-TM17 解除，本包即執行。

**反面自檢**：凡屬「我不確定該怎麼做」而非上列四類者，正解為
「取保守預設逕行 + 在上繳標明可撤回」，不是停下。

## R-TM27 — A-TM15 修法範圍追認為三分支

（分析層裁定，2026-08-20。上游包 `docs/handoff/04_scripts.md` §1）

```
R-TM27（分析層裁定，2026-08-20）—— A-TM15 修法範圍追認為三分支

A-TM15 之修法確定為三分支（見上表），非 03Z-A1 T4 字面之
「目標存在即改寫路徑」。原字面指令會使既有 feature 之 recon 一律
REFUSED 退出並誤報簽核狀態 —— 該缺陷源自分析層只讀 write_decisions()
未讀其回傳值之消費點（recon.py:1135）。

一般化：修改一個函式之回傳語意前，須讀遍其全部消費點。
與 R-TM7（指令須經實測）同族：前者是介面未讀，本條是消費點未讀。
```

三分支之確定內容：

| 情境 | 行為 |
|---|---|
| 目標存在 + 已簽核 | divert + REFUSED 非零退出（R-C9 原樣保留）|
| 目標存在 + 未簽核 | divert + `NOTE (A-TM15)` + 正常退出（A-TM15 之標的）|
| 目標不存在 | 寫 `DECISIONS.md`（新 feature 路徑不變）|

**執行層回報（2026-08-21）**：已於 `4b00d33` 落檔。本條之一般化規則
（改回傳語意前須讀遍消費點）已納為作業慣例；本次即因先讀 `recon.py:1135`
而發現字面指令之缺陷。

## R-TM28 — R-TM22 條件 2 收緊（宣告路徑齊全 + signed=False）

（分析層裁定，2026-08-20。上游包 `docs/handoff/04_scripts.md` §2）

```
R-TM28（分析層裁定，2026-08-20）—— R-TM22 條件 2 收緊

R-TM22 之受測物判準 2(a) 由「inputs/ 存在且非空」改為：

  2(a) feature.yaml 宣告之每一個輸入路徑皆實際存在於磁碟
       （非僅 inputs/ 非空 —— sxm 之 inputs/ 有 4 檔而宣告之 SYS1
        檔不在其中，實跑即 input not found）

新增 2(d)：受測物之 signoff.signed 必須為 False。
       已簽核者走 divert 路徑受 R-C9 保護，A-TM15 修法前後行為相同，
       以其為受測物則判準無鑑別力（R-TM21 同型）。

依本條，四候選之適格性為：
  privacy        signed=False  宣告路徑齊全  → 適格（本次選用）
  user_profiles  signed=False  未驗宣告路徑  → 待驗
  sxm            signed=True   宣告路徑缺件  → 不適格
  comfort        signed=True   且為 A-TM18 主體 → 不適格
```

**執行層回報（2026-08-21）**：已知悉。本條之 2(d) 為 R-TM21 判準之延伸
應用 —— 受測物之選擇本身也須通過「本工作若完全沒做，判準會不會照樣通過」。

## R-TM29 — R-TM10-A1 之射程限於 TC 內容，不及於工具腳本

（分析層裁定，2026-08-20。上游包 `docs/handoff/04_scripts.md` §3）

```
R-TM29（分析層裁定，2026-08-20）—— R-TM10-A1 之射程限於 TC 內容

R-TM10-A1 之 SUSPENDED「不得援引任何他 feature 之既成樣式」，
其射程限於 TC 內容，不及於工具腳本、資料結構與管線形式。

依據（條文自身，非新解釋）：R-TM10(b) 明列之可援引／不得援引兩表，
全部為 TC 內容項目 —— 步驟措辭、ER 句式、標點慣例、spec_reference 格式、
test_group / test_set 值、priority 分佈、tc_id 體系、Input Test Data
填法。無一項涉及工具腳本。R-TM10(c) 之語境為「爭議之裁決依據」，
亦屬內容判準。

故：features/time_management/scripts/ 之各腳本得自由參照他 feature
之對應腳本（結構、參數、呼叫慣例、錯誤處理）。

且此處參照是必要的而非便利的：write_back.py 須正確呼叫
backend/xlsx_surgical.py 之 surgical_save，從零寫反而升高母本 R 欄
x14 下拉被摧毀之風險（R-G3）—— 該風險為不可逆且發生在交付件上。
以「不得援引樣式」為由強迫從零寫工具，會用一個內容層的限制去製造
一個交付層的風險，非該條之目的。

界線：腳本內若含 TC 內容之常數（步驟措辭常數、ER 樣板字串、
Test Set 值），該常數仍受 R-TM10-A1 拘束，須依本 feature 之條文重新
決定，不得照抄。參照結構，不繼承內容。
```

**執行層回報（2026-08-21）**：已依本條建立 `scripts/`，逐支腳本之來源與
差異見上繳 `04_scripts.md` §5。**界線之落實方式**：凡屬 TC 內容之常數
一律留空並標 `TODO(R-TM10-A1)`，不從來源腳本繼承任何字面值。

## R-TM30 — 回歸測試遺留物移入本 feature，不刪除

（分析層裁定，2026-08-20。上游包 `docs/handoff/04_scripts.md` §6）

```
R-TM30（分析層裁定，2026-08-20）—— 回歸測試遺留物移入本 feature，不刪除

features/privacy/ 之兩個新增檔為本 feature 回歸測試之產物：
  DECISIONS.new.md（2372 B）—— A-TM15 修法正確運作之現場證據
  data/recon_leaf_to_section.tsv（48 B）

處置：mv 至 features/time_management/data/regression_evidence/，
不 rm。理由：
1. 刪除不可逆；mv 可逆
2. 證據價值屬本 feature（A-TM15 之驗證），不屬 Privacy
3. 鄰居目錄不留來歷不明之檔案

移動後 features/privacy/ 應與本次動它之前完全一致（RECON.md 與
DECISIONS.md 已於 03Z-A1 §5 還原並經 SHA 驗證）。
```

**執行層回報（2026-08-21）**：已 mv，`features/privacy/` 之
`git status` 無殘留。`regression_evidence/README.md` 已記來源與緣由。

## R-TM31 — 驗證判準須輸出可歸屬之明細，不只計數

（分析層自裁，2026-08-21。上游包 `docs/handoff/04R_review.md` §2。
發現者為執行層 `04` 上繳 §6.2。）

```
R-TM31（分析層自裁，2026-08-21）—— 驗證判準須輸出可歸屬之明細，不只計數

驗證步驟之輸出須足以判斷「命中者是不是我方產出」，不得只給計數。
凡以 `grep -c`、`wc -l`、`count=` 形式收尾之判準，一律改為列出命中位置
或內容片段。

理由：計數對「內容被替換但數量相同」完全不敏感。本包之 13 處
TODO(R-TM10-A1) 計數通過，而其中 11 處來自另一份非我方所寫之檔案。

本條為 R-TM4（斷言須附完整元素清單）在**驗證步驟**上之延伸：
前者管主張，本條管檢查。
```

**執行層回報（2026-08-21）**：已知悉並套用於本包 T5 之全部判準。

**執行層補充 —— 本條有一項自身之盲區**：列出位置或片段，只在「我方知道
自己產出長什麼樣」時才足以歸屬。本次能判定歸屬，靠的是執行層版本帶有
特徵字串 `Structure ported from`，而該字串是偶然存在的，非刻意設計。

**故執行層自訂一項對應作法**：凡本 feature 產出之腳本，其 docstring 首段
須含一句可 grep 之來源標記（形如 `ported from <path> under R-TM29`），
使歸屬判定不依賴偶然。本次未及套用於已被覆蓋之兩支。

## R-TM32 — tc_id 格式

（分析層裁定，2026-08-21。上游包 `docs/handoff/04R_review.md` §3）

```
R-TM32（分析層裁定，2026-08-21）—— tc_id 格式

write_back.tc_id_format = "NR1L-TimeAndDate-{n:03d}"

依據：
1. canon §10.3 —— `{project}-{abbr}-{NNN}`，alphanumeric project +
   alphanumeric module abbreviation + 零填三位序號
2. project 段取 `NR1L`，與 privacy 之 `NR1L-Privacy-{n:03d}`（R-PV02）
   同 —— 此為格式結構之參照，非 TC 內容之援引，R-TM29 界線內
3. module 段取 `TimeAndDate`，來自 R-TM8 之 Test Group `Time and Date`
   去空格。不取 `TimeManagement` —— 該名為內部識別，不進交付件
   （R-TM1 / R-TM8 之同一區分）

序號自 001 起，於 22 片 leaf 之全部 TC 上單調遞增，跨批次連續
（B1 用完接 B2，不重設）。

本條可撤回：B1 未生成前改之無成本。
```

**執行層回報（2026-08-21）**：已寫入 `feature.yaml` 之 `write_back:` 段。
**未動 `scripts/`**（A-TM20 凍結）—— 故現存 `write_back.py` 是否讀取該鍵
未經驗證，見上繳 `04R_corrections.md` §3。

## G-TM1 — B1 生成前 lint 層須具備四項閘門

（閘門，2026-08-21。上游包 `docs/handoff/04R_review.md` §4。
G-series 與 R-series 同檔。）

```
G-TM1（閘門，2026-08-21）—— B1 生成前，lint 層須具備四項閘門

無論最終由哪一方寫 lint_tcs.py，下列四項須存在且經 self-test 證明
可 fire（R-TM21：不能失敗的閘門不是閘門）：

1. D5 Scope 守衛 —— 寫回後 D5 仍為空，具名失敗，不與 header drift 混列
   （R-TM9-A2、A-TM02a）
2. leaf 文字來源隔離 —— test_item 上半之文字只認
   data/leaf_descriptions.txt，22 筆全集數量不符即報錯（R-TM24）
3. spec gap 閘門 —— 005 / 002 之 Remarks 為空即報 spec-gap（A-TM13）
4. 界線閘門 —— 011 / 008 / 014 各自 owns / not_ours 之訊號名表，
   TC 全文命中 not_ours 即報 boundary。訊號名一律取自 T3 已複驗之錨點
   （R-TM23、R-TM25）

現存之 build_batch_context.py（執行層版）已含 SPEC_GAP 與 BOUNDARIES
兩表，故 3、4 在 context 層有編碼，僅 lint 層缺。
context 層之編碼不能取代 lint 層 —— 前者是給生成看的，後者是驗生成的。
```

**執行層回報（2026-08-21）**：已登記。四項對現存版之逐項評估
（有／無／部分，附位置證據）見上繳 `04R_corrections.md` §3。
**本包未實作任一項**（A-TM20 凍結）。

## R-TM33 — 產出物須帶可 grep 之來源標記

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z_closure.md` §1。
發現者為執行層 `04R` 上繳 §2.1。）

```
R-TM33（分析層自裁，2026-08-21）—— 產出物須帶可 grep 之來源標記

本 feature 產出之每一支腳本，其 docstring 首段須含一句可 grep 之來源
標記，形如：

    ported from <path> under R-TM29; authored by TC_Generator analysis
    round <NN>

使歸屬判定不依賴偶然字串。R-TM31 要求驗證輸出可歸屬，本條使該歸屬
成為可能 —— 兩條合用方完整。

適用範圍：腳本、資料檔（data/*.tsv、data/*.txt）之檔頭註解。
不適用於 TC 工作簿欄位（§1 語言規則，且交付件不帶內部標記）。

依據：04R 上繳 §2.1。本次之歸屬判定依賴 `Structure ported from`，
該字串為執行層偶然寫入而非刻意設計。
```

**執行層回報（2026-08-21）**：已知悉。**本條現無法套用於 `scripts/`**
（A-TM20 凍結，不得寫入任一行），故三支現存腳本皆未帶本條所定之標記。
凍結解除後，無論由哪一方持有，套用本條應與 G-TM2 之十二項一併處理。

**已套用之處**：`data/scripts_snapshot_20260821/README.md` 與
`SOURCE_STATE.txt` 已載逐檔之產出者與 SHA256，即以快照側之標記補足
來源端不可寫之缺口。

## R-TM34 — columns 補 tc_id

（分析層裁定，2026-08-21。上游包 `docs/handoff/04Z_closure.md` §3）

```
R-TM34（分析層裁定，2026-08-21）—— columns 補 tc_id

feature.yaml 之 workbook.columns 補：

    tc_id: "F"        # Test Case ID；R-TM34

依據：FORMS.md 之 rev C 母本實測欄位對映，F 欄為 Test Case ID
（Home 複本之 provenance warning 亦載「F 欄 216 列全填 tc_id」，
為同一欄之獨立佐證）。

本條只補欄位對映；實際寫入須待 A-TM21 (c)(d) 修畢（G-TM2 項 3）。
```

**執行層回報（2026-08-21）**：已補入 `feature.yaml`，改前／改後之
SHA256 與 mtime 見上繳 `04Z_corrections.md` §3。**未動 `scripts/`**。

## R-TM35 — 凍結中之產出物以複製保全，不以 commit

（分析層裁定，2026-08-21。上游包 `docs/handoff/04Z-A1_preservation.md` §2）

```
R-TM35（分析層裁定，2026-08-21）—— 凍結中之產出物以複製保全，不以 commit

凍結期間之檔案若未進版本控制且有覆蓋風險，一律以複製至本 feature 之
data/ 下留存快照，不以 commit 保全。

理由：commit 屬 Pei，複製不屬；風險為現時，等待有成本。
且 commit 會將歸屬未定之產出納入版本史並附作者，複製不會。

快照須含來源路徑、複製時點、來源 mtime 與 SHA256，使日後可判定
「快照對應的是哪一個版本」（R-TM31 / R-TM33 同一精神）。
```

**執行層回報（2026-08-21）**：已執行，快照於
`data/scripts_snapshot_20260821/`。三支 SHA256 逐支相同，來源 mtime
複製後仍為 09:13:36 / 09:14:32 / 09:15:18 —— **凍結之證據鏈未被破壞**。

**執行層接受本條對其原提議之修正**：原提議「單獨開 commit 收進三支」
會將另一 session 之產出納入版本史並附 commit 作者，正是排除 `scripts/`
於 `34e2da6` 之同一理由。複製無此問題，且不必等待。

## G-TM2 — B1 生成前之必修項與不得回退項

（閘門，2026-08-21。上游包 `docs/handoff/04Z_closure.md` §2）

```
G-TM2（閘門，2026-08-21）—— B1 生成前之必修項與不得回退項

無論最終由哪一方持有 scripts/，下列須在 B1 生成前成立：

【必修】
1. A-TM21 (a) —— resolve_columns() 實作 docstring 所述之表頭複驗，
   或改寫 docstring 使其與實作相符。**不得留下承諾與實作不符之狀態。**
2. ~~A-TM21 (b) —— check_other_sheets() 同上處置~~  ← **見條末訂正**
3. ~~A-TM21 (c)+(d) —— tc_id 自 feature.yaml 讀取並實際寫入 F 欄~~  ← **見條末訂正**
4. A-TM21 (f) —— 必填欄位檢查須及於空值
5. read_design_methods() 加數量驗證（期望 9，取自 $A$1:$A$9）

【不得回退 —— 現存版優於被覆蓋版，須保留】
6. lint_spec_reference 驗物件 id 實際存在於 CFTS015 docx
   —— 被覆蓋之執行層版本無此閘門。Privacy R30-1 曾因偏移量推算 id
   而產生兩個錯誤 id，此閘門正為該形態而設
7. self-test 之紅綠雙向（綠向證明不誤報，紅向證明抓得到）
8. load_authorities 之「任何一項讀不到即 raise，不以預設值頂替」

【TODO 標記訂正】
9. TC_ID_FORMAT 之 TODO 撤除 —— R-TM32 已裁定
10. C 欄（Polarion ID）之 TODO 撤除 —— 非未定；SYS2 export 經 intake
    分類為 polarion_export，Part VII 明載其角色為錨鏈中介而非逐列 id 來源
11. Test Set 值域閘門之 TODO 撤除 —— framework Part VII 七組已由
    R-TM17 簽核（2026-08-20），可立即實作
12. priority 閘門之 TODO 拆分 —— **值域** P0–P3 為母本 P 欄 DV 內嵌，
    可自母本讀，非 TC 內容裁決；**分佈**才是內容裁決。兩者不得混為一談

G-TM1 之四項閘門仍全數有效，本條為其外加。
```

**執行層回報（2026-08-21）**：已登記，**本包未實作任一項**（凍結）。

**執行層補一項本條未列者**：G-TM2 項 3 補齊後，`write_rows()` 之
`cols` 迴圈會因 `feature.yaml` 新增 `tc_id` 鍵而嘗試寫 `tc.get("tc_id")`
—— 即**若生成之 TC JSON 不含 `tc_id` 鍵，該欄仍為空**。tc_id 應由
`tc_id_format` 依位置產生（Privacy 之作法），非由生成端提供。
故項 3 之修法須同時確保：**tc_id 不從 TC 資料讀，而由寫回端依序號賦予**
（canon §10.3 之 monotonically increasing 亦要求由單一處統一賦號）。

### G-TM2 項 2 訂正（2026-08-21，依據包 `docs/handoff/04Z-A2_backend_review.md` §1.1）

**原文加刪除線保留於上（R-TM13），訂正如下：**

```
G-TM2 項 2 訂正（2026-08-21，依 04Z 上繳 §5.3）

原文：「A-TM21 (b) —— check_other_sheets() 同上處置（實作 docstring
所述之保護，或改寫 docstring 使其與實作相符）」

訂正為：

  2. A-TM21 (b) —— **移除 check_other_sheets()**，並於 run() 之該處
     加一行註解指向 backend/xlsx_surgical.py:268-275 之 verify_structure
     第三層。

     理由：該函式之功能已被 verify_structure 完全涵蓋且後者更嚴格
     （逐 member 位元組比對，且限定僅 patched 者得異）。保留一個
     更弱且被完全涵蓋之檢查，只會製造「有兩道獨立防護」之假象。

     若持有者堅持保留，則須改寫 docstring 使其誠實描述「僅比對 member
     名稱集合」，且不得再使用「逐位元相同」字樣。
     **不得留下承諾與實作不符之狀態** —— 此點與原文相同。

G-TM2 項 1（A-TM21(a)）**不變**。其 resolve_columns() 之欄位對映無任何
其他機制涵蓋：verify_structure 保護檔案結構，不驗欄位對映是否取對；
寫入落在錯欄時，錯欄仍在目標分頁內屬 patched，結構檢查全綠。
執行層 §5.4 之區辨正確。
```

**執行層回報（2026-08-21）**：訂正已落檔，**本包未實作**（凍結）。
分析層取「移除」而非「改 docstring」，並採執行層之理由
（「其存在使讀者誤以為有第二道獨立檢查」）—— 執行層同意該取捨：
一個更弱且被完全涵蓋之檢查，其唯一作用是製造備援之假象。

## R-TM36 — git 授權之唯一來源

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z-A2_backend_review.md` §2。
依據為執行層 `04Z` 上繳 §2.1 之二分。）

```
R-TM36（分析層自裁，2026-08-21）—— git 授權之唯一來源

下放包「不得執行者」所列之「不動 git」，其意義為
**分析層之指令不授權執行層執行任何 git 寫入操作**，
非「執行層在任何情況下不得執行 git」。

git 操作之唯一授權來源為 Pei 於聊天層之直接指示。下放包無權授權，
亦無權撤銷該指示。

執行層收到 Pei 之直接 git 指示時逕行執行，並於上繳完整回報
（指令、commit hash、變更檔數、排除清單、是否 push）。

依據：04Z 上繳 §2.1 之二分。本條為既有分工之明文化，非新規則。
```

**執行層回報（2026-08-21）**：已知悉，且本條即執行層現行作法之明文化。
迄今四次 commit（`5fb0713` / `2062acb` / `4b00d33` / `34e2da6`）皆在
Pei 於聊天層直接輸入後執行，**`git push` 從未執行**（分支現 ahead 14）。

## R-TM37 — commit message 之草擬與其查證義務

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z-A2_backend_review.md` §2.1。
依據為執行層 `04Z` 上繳 §2.2 之提請。）

```
R-TM37（分析層自裁，2026-08-21）—— commit message 之草擬與其查證義務

commit message 之草擬屬執行層自裁（Pei 之指示為「執行 commit」，
不含逐字審閱 message），現行作法（執行層草擬、回報中完整呈現、
Pei 事後可要求改寫）確認為所期。

但 message 內之任何數字或狀態陳述受與其他斷言相同之查證義務
（canon §5a）：`rulings 35, anomalies 20` 一類必須為**實測值**，
不得取自下放包之期望值或前次回報。message 是會被日後引用的記載，
其錯誤與文件內之錯誤同級。

未 push 前 message 可重寫，故錯誤可逆 —— 但可逆不免除查證義務。
```

**執行層回報（2026-08-21）**：已知悉。**回溯自查**：`34e2da6` 之 message
所載 `rulings 35, anomalies 20` 為 commit 前以
`git show HEAD:...RULINGS.md | grep -c '^## R-TM'` 對**已入庫之內容**
實測所得（見 `04R` 上繳前之驗證步驟），非取自下放包期望值。
`4b00d33` 之 message 所載 `Rulings 29, anomalies 18` 同。**符合本條。**

**執行層補一項本條未涵蓋者**：message 內之**因果陳述**（如
「sxm was rejected on two counts」）亦應受同一義務。本次該句之兩項
理由（已簽核、宣告輸入缺件）皆有實測支持，但條文只提「數字或狀態陳述」，
未及因果。**提請是否納入。**

### G-TM2 項 3 訂正（2026-08-21，依據包 `docs/handoff/04Z-A3_positive_verification.md` §1.1）

**原文加刪除線保留於上（R-TM13），訂正如下：**

```
G-TM2 項 3 訂正（2026-08-21，依 04Z-A2 上繳 §1）

原文：「A-TM21 (c)+(d) —— tc_id 自 feature.yaml 讀取並實際寫入 F 欄」

訂正為：

  3. A-TM21 (c)+(d) —— tc_id 由**寫回端依列位置賦號**，格式取自
     feature.yaml 之 write_back.tc_id_format（R-TM32），寫入 F 欄。

     **TC JSON 不得攜帶 tc_id** —— canon §10.3 末句：
     `the generator handles assignment, the LLM does not emit tc_id`
     （ASPICE_SWE6_AI_Instruction.md:521-525）。

     故 write_rows() 之 tc.get(key) 迴圈**不得**用於 tc_id：
     - tc_id 須在迴圈外由序號計算，不從 tc 取
     - lint 層須增一項：TC JSON 若含 tc_id 鍵即報錯
       （生成端違反 canon §10.3 之偵測點）

     序號依 R-TM32 跨批連續不重設，故賦號需要一個跨批次之起點來源
     （既有列數或明文起點），該來源須為單一且可查 —— 實作時明示之。
```

**執行層回報（2026-08-21）**：訂正已落檔，**本包未實作**（凍結）。

**執行層補一項實作面之提請**：訂正末段要求「跨批次之起點來源須單一且
可查」。本 feature 為 **BLANK workbook**（R-TM5），首批寫回前工作簿無
任何既有資料列，故「既有列數」在 B1 時恆為 0。**B2 起始序號之來源有二
候選**：(i) 重新讀工作簿既有列數；(ii) 讀 `generated/` 之累計 TC 數。
二者在正常情形一致，**但若某批曾被撤回或重生成即分歧**。屬實作決定，
提請於解凍後之修法指令中明示取何者。

## R-TM38 — 引用條文須引至規範性句末

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z-A3_positive_verification.md` §1。
依據為執行層 `04Z-A2` 上繳 §4.2。）

```
R-TM38（分析層自裁，2026-08-21）—— 引用條文須引至規範性句末

引用 canon、FORMS.md、feature profile 或任何規範文件作為裁決依據時，
須引至該句之句末（`.` / `。`），不得於分號、逗號、破折號處截斷。

理由：規範文件常以分號銜接「形式要求」與「操作要求」，前半描述成品
長什麼樣，後半描述由誰、以何方式產生。截斷於分號會保留形式而丟失
操作，而丟失的那半通常才是實作時真正需要的。

引用時一併標明來源檔與行號區間，使截斷可被對造發現。

依據：04Z §4 引 canon §10.3 止於 `... group.`，切掉
`; the generator handles assignment, the LLM does not emit tc_id.`
—— 該句為三項判定中唯一影響實作方式者。
（原文位置：docs/runtime/ASPICE_SWE6_AI_Instruction.md:521-525）
```

**執行層回報（2026-08-21）**：已知悉。**本條對執行層之射程尤須注意** ——
執行層之上繳同樣大量引用條文，且本 feature 之引用密度高。

**執行層自查**：本 feature 迄今之上繳中，引用 canon / FORMS.md 之處
是否有同型截斷，**本包未逐一回查**（成本高，且多數引用為整段複製而非
單句節錄）。**提請**：是否須做一次回查。若須，建議限縮於「以引用作為
裁決依據」之處，非全部引用。

## R-TM39 — 不觸碰優於主動保護

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z-A3_positive_verification.md` §2.1。
依據為執行層 `04Z-A2` 上繳 §3.2(4)。）

```
R-TM39（分析層自裁，2026-08-21）—— 不觸碰優於主動保護

評估一項保護時，須區分「有邏輯在保護它」與「根本沒有程式碼會動到它」。
後者強度較高：主動保護有可失效之邏輯，不觸碰沒有。

故評估報告中，對「未被任何程式碼觸及」之結論，其舉證方式為
**全檔搜尋該識別字並確認零命中（或僅命中註解）**，而非追蹤保護邏輯
之正確性。

依據：04Z-A2 上繳對 x14 extLst 之判讀。母本 R 欄 x14 下拉之存活，
其依據為 backend/ 全檔 grep `extLst` 僅命中註解，非某個保護分支。
```

**執行層回報（2026-08-21）**：已知悉並於本包 T3 之舉證中套用。

**執行層補一項本條之界線**：「零命中」之舉證須確認**搜尋範圍涵蓋全部
可能觸及該識別字之路徑**。x14 之案例中，搜尋範圍為
`backend/xlsx_surgical.py` 全檔 —— 但寫回路徑若日後引入其他模組
（如另一個 XML 後處理步驟），該搜尋範圍即不再充分。
**故本條之舉證有效期限於「寫回路徑之組成不變」**，路徑變動時須重做。

## G-TM3 — 寫回後須有正向驗證

（閘門，2026-08-21。上游包 `docs/handoff/04Z-A3_positive_verification.md` §3。
發現者為執行層 `04Z-A2` 上繳 §5.3 項 1。）

```
G-TM3（閘門，2026-08-21）—— 寫回後須有正向驗證

B1 生成後之首次寫回前，寫回路徑須具備至少一項正向驗證：
寫回完成後，**重新開啟輸出檔，讀取目標分頁之指定 cell，
確認其值等於預期值**。

理由：現有三層全為反向驗證（A-TM22）。反向驗證再嚴格也無法發現
「寫對了內容但寫錯了地方」—— 而錯地方之後果是交付件靜默損壞。

最小實作：寫回後取 N 列（首列、末列、任一中間列）之
tc_id / test_item / design_method 三欄，與寫入前之預期逐項比對。
比對失敗即 raise，不得僅警告。

本條與 G-TM1 / G-TM2 並列為 B1 前之閘門。
```

**執行層回報（2026-08-21）**：已登記，**本包未實作**（凍結）。

**執行層補一項最小實作之細節提請**：本條指定取「首列、末列、任一中間
列」三欄比對。**該取樣對 A-TM22 之 member 層錯誤有效**（寫錯分頁則三列
皆讀不到預期值），**但對 column 層錯誤（A-TM21(a)）之偵測力取決於所取
之欄**：若 `feature.yaml` 之字母整體位移一格，讀 `tc_id` / `test_item` /
`design_method` 三欄仍會各自讀到「鄰欄之值」而非預期值，故可偵測。
**惟若某兩欄之值恰巧相同（如兩個空欄），該列該欄之比對會偽陰性。**
建議取樣時**排除預期為空之欄**，或改以「非空且各列互異」之欄為準
（`tc_id` 依序號必互異，為最佳取樣欄）。
