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
2. ~~該值在 A-TM02a（037 身分）裁定前無法取得。D5 維持空白。~~
3. ~~空白是可見狀態；指向不存在文件之值不是。~~任何情況下不得以
   feature 名、spec 標題或類推形態組出一個字串填入（§8.4.1）。
   ← **第 2、3 點之處置見條末訂正（canon §8.4.3）**
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
Part VII 之相鄰組界線表由三條增為五條。（**編號改以鄰接對 B-1…B-6，見 R-TM53**）
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

**計數盲點出現於守衛內部（2026-08-22，06Z 上繳 §3.1）**

`tm_rulings.py` 之首版模組載入斷言以 `len()` 檢查常數完整性，
而 key 改名（`"002"` → `"_x"`）使長度不變即漏網 —— **本條所指之計數
盲點，出現在為防止裁決值遺失而設的守衛內部**。已改驗 key 集合。

此為「防護規則與其防護對象同形」之第二實例（第一實例：01Z-A4 之
負向後查 regex 自我抵銷，已列為 canon 再同步候選）。

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
4. ~~界線閘門 —— 011 / 008 / 014 各自 owns / not_ours 之訊號名表，
   TC 全文命中 not_ours 即報 boundary。~~ ← **見條末項 4 訂正**
   訊號名一律取自 T3 已複驗之錨點（R-TM23、R-TM25）

~~現存之 build_batch_context.py（執行層版）已含 SPEC_GAP 與 BOUNDARIES
兩表，故 3、4 在 context 層有編碼，僅 lint 層缺。~~  ← **見條末更正**
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

**同源之三種形態（2026-08-21，04Z-A3 上繳 §4.5）**

本條（引用截斷）與 A-TM21(a)(b)（docstring 承諾／實作缺失）、
「找到保護所在」當「保護有效」（04Z-A2 §6.3(2)）為同一形態之三種發生位置：

  寫的人切斷：docstring 保留承諾，丟掉實作
  讀的人切斷：保留「找到了」，丟掉「驗過了」
  引用的人切斷：保留形式，丟掉操作

三者皆非疏忽，而是**每一步都在「已經夠了」的地方停下**。
故評估、引用、檢查之完成回報，須明列「還沒做的那半是什麼」。

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

~~理由：現有三層全為反向驗證（A-TM22）。反向驗證再嚴格也無法發現
「寫對了內容但寫錯了地方」—— 而錯地方之後果是交付件靜默損壞。~~
← **見條末訂正：主要防護對象為 column 層，非 member 層**

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

## R-TM40 — spec_reference 之格式

（Pei, 2026-08-21。上游包 `docs/handoff/04Z-A4_spec_reference.md` §1）

```
R-TM40（Pei, 2026-08-21）—— spec_reference 之格式

specification_reference 欄之每一條目格式為：

    CFTS{doc_num}-{Source Requirement item id}

本 feature 之 doc_num = 015，item id 取自 SYS2 匯出之
`SYS2 來源需求項目ID  Source Requirement items` 欄（Basic Report 第 5 欄）。

例：CFTS015-4813905、CFTS015-4813974

不採 `<Spec Filename>_{outline}`（章節號）形式。
feature.yaml 之 spec_reference_template 隨之改寫。
```

### R-TM40 之連鎖後果（六項，`04Z-A4` §2）

**1. A-TM12 降為非阻塞**（§2.1）—— 取值止於物件 id，不再需要
「物件 id → 章節號」之 docx 解析。錨鏈工作不作廢，其角色由「交付欄位
之來源」改為「framework 導航之依據」（Layer 3 主軸章節表、R-TM23 兩條
界線之 spec 依據）。已於 `ANOMALIES.md` A-TM12 條末註記。

**2. 多物件儲存格展開為多條目**（§2.2）—— canon §10.7 允許 string list。
排序改採**物件 id 數值遞增**（本格式無章節層級可比），使同一 leaf 之
條目順序具決定性。

**3. leaf 層之聯集是上限，非每條 TC 之預設值**（§2.3）—— canon §10.7
拘束「List every spec section the TC directly verifies or relies on as
setup；Do NOT cite specs only used as background context」。一片 leaf
產生多條 TC 時，各 TC 只列該 TC 實際驗證之物件。

**4. A-TM13 兩片仍阻塞**（§2.4）—— 見 R-TM41。

**5. `feature.yaml` 之 `spec_reference_template` 改寫**（§2.5）—— 已執行。

**6. lint 層新增閘門**（§2.6）—— 每一條目須 (i) 形式符合
`CFTS015-\d{7}`、(ii) 其 7 位部分存在於 SYS2 第 5 欄之全集、
(iii) 存在於 CFTS015 docx。第 (iii) 項與現存 `lint_tcs.py` 之
`lint_spec_reference` 方向相同，**使該閘門由「額外保護」升為
「格式正確性之必要條件」**（G-TM2 項 6 之「不得回退」因此更硬）。

**執行層回報（2026-08-21）**：六項全數登記。第 5 項已執行；第 6 項屬
`scripts/`，凍結中未實作。逐 leaf 之候選表已產出於
`data/spec_reference_candidates.txt`（22 列全表見上繳）。

**依據訂正（2026-08-21，Pei 於聊天層質疑後實測）**

`04Z-A4` §3 以 `CFTS015-806` / `-1203` / `-1520` 為據，主張文件本身即以
`CFTS015-` 前綴指涉其需求物件。**該依據取自短號家族，而本條之取值為
7 位家族**；`CFTS015-<7 位>` 於 CFTS015 全文出現 0 次。

本條之裁定不受影響（Pei 為工作簿定義之參照體系）。受影響者為其依據：
`CFTS015-4813905` 為本專案新定之形式，非沿用文件既有慣例。
兩套編號並存之事實見 A-TM23。

前綴之三位零填（`CFTS015` 非 `CFTS15`）仍成立 —— 26 個短號值皆用此前綴。

**依據再訂正（2026-08-21，依 `04Z-A5` 上繳 §3.4 之提請）**

`05R` T1 指示將依據改為 canon §10.7 **Rules 第 2 條**
（`Use the SourceID format from SYS1 / Polarion when available`）。

**執行層實測後未照該字面執行 —— 該條規則已不存在。**
canon `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 之 §10.7 已由他方
整節改寫（工作樹變更，未 commit）：舊節之 `Format per entry` 與六條
`Rules` 全數刪除。`grep -c 'Use the SourceID format'` = **0**。

**新 §10.7 為更直接且更強之依據**，逐字：

```
### 10.7 specification_reference
依母 spec 型態分流：
(a) CFTS 母文件 → `CFTS{nnn}-{ObjectID}`，ObjectID 為該物件之
    Polarion 7 位號碼。短號需求 ID（如 CFTS015-824）不得作為錨，
    僅得於 reasoning 引用。
```

即：本條之格式**由 canon 明文規定**，非「明文允許」亦非「本專案新定」。
且新 canon **明文禁止短號作為錨**，其舉例恰為 `CFTS015-824`
（本 feature 之短號家族成員）。

**連帶之格式要求（新 §10.7 排列段，本條原文未涵蓋）**：

```
排列：一來源文件一行（換行分隔）；同一文件內多個 ObjectID／章節號
以 `, ` 續列且文件前綴僅敘明一次；禁用 `;`。TC 直接驗證之主要來源
列於首行，同文件內 ID／章節號升冪。
```

**此與 `04Z-A4` T4 所產之候選表格式不符** —— 該表為
`CFTS015-4813919, CFTS015-4813920, …`（前綴逐條重複），
依新規應為 `CFTS015-4813919, 4813920, 4813984, 4814069`（前綴僅一次）。
**已於階段 B 之 B7 依新規實作**，候選表檔案本身保留為軌跡未改。

## R-TM41 — A-TM13 兩物件不得寫入 spec_reference

（分析層裁定，2026-08-21。上游包 `docs/handoff/04Z-A4_spec_reference.md` §2.4）

```
R-TM41（分析層裁定，2026-08-21）—— A-TM13 兩物件不得寫入 spec_reference

CFTS015-6151328 與 CFTS015-6151331 不得寫入 specification_reference。

理由：R-TM40 之格式使該二字串在字面上可組出，但組出來即為一個
我方已實測為偽之斷言（該二物件於 CFTS015 SR26 全檔零命中）。
§8.4.1 禁止捏造來源未述之值；「格式湊得出來」不等於「來源有此內容」。

~~處置：`SWE-RA-TIME&DATE-005` 與 `-002` 之受影響 TC，其
specification_reference 只列該 TC 實際驗證且確實存在於 CFTS015 之物件；
缺口於 Remarks 宣告（G-TM1 項 3 之 spec gap 閘門）。~~
← **處置見條末訂正（canon §8.4.3）**

**兩片仍留在 B2，不因格式改變而移入 B1。** B1 之零 A-TM13 曝險設計
（03 §3）不變。
```

**執行層回報（2026-08-21）**：已登記。T4 之候選表實測確認
**BLOCKED 恰 2 筆**，且只出現於 `-005`（`CFTS015-6151328`）與
`-002`（`CFTS015-6151331`），其餘 20 片全數 OK ——
**未出現第三片，A-TM13 之範圍與既有記載一致。**

**執行層補一項實測所得之事實**：`-005` 之 OK 條目僅 **1 筆**
（`CFTS015-4813936`），為 22 片中最少者。即該片之 `spec_reference`
在扣除 BLOCKED 後只剩單一物件 —— **其 spec 依據之單薄程度為全 feature
之最**，與 `02R` §2.5 所記「005 之章節證據只有一半可用」同源而更具體。
撰寫該片之 TC 時值得特別注意。

### G-TM3 訂正（2026-08-21，依據包 `docs/handoff/04Z-A5_numbering_correction.md` §2）

**原理由段加刪除線保留於上（R-TM13），訂正如下：**

```
G-TM3 訂正（2026-08-21，依 04Z-A3 上繳 §3.4）

原條文之理由段將 G-TM3 定位為 A-TM22（member 層）之對策。訂正為：

**主要防護對象為 column 層（A-TM21(a)）**，member 層（A-TM22）為次要。

| 盲區 | 對映之保證 | G-TM3 之防護力 |
|---|---|---|
| member 層（A-TM22） | 有（rels 權威 + 下游 raise） | 錦上添花 |
| column 層（A-TM21(a)） | **無**（feature.yaml 字母純宣告，複驗不存在） | **主要** |

**取樣欄之選擇**：以 `tc_id` 為首選取樣欄 —— 其依序號賦值必逐列互異，
可排除「兩欄值恰好相同」之偽陰性。次選 `test_item`（逐列互異且長）。
**不取 `design_method` / `priority` 一類值域小之欄** —— 該類欄位
位移一格仍可能取到合法值，偽陰性率高。

**另一項理由（04Z-A3 上繳 §4.3(1)）**：backend/xlsx_surgical.py 之
全部評估皆為讀碼與對母本之唯讀探測，**寫入路徑在本 feature 從未執行過**。
B1 之首次寫回即為該路徑之首次實跑，屆時 G-TM3 之正向驗證是唯一能發現
「讀碼推論與實際行為不符」之機制。

原條文之其餘部分（最小實作、比對失敗即 raise 不得僅警告）不變。
```

## R-TM42 — 受測物之鑑別力須先於測試本身確認

（分析層自裁，2026-08-21。上游包 `docs/handoff/04Z-A5_numbering_correction.md` §1.1。
發現者為執行層 `04Z-A3` 上繳 §3.1(4)。）

```
R-TM42（分析層自裁，2026-08-21）—— 受測物之鑑別力須先於測試本身確認

以某一資料或檔案作為某項實作之驗證受測物前，須先確認
**該受測物能區分正確實作與已知的錯誤實作**。

具體作法：列出該項最可能之錯誤實作（如以索引推算取代 rels 解析），
判斷受測物在該錯誤實作下會通過或失敗。若會通過，該受測物對此項
無鑑別力，須另尋或另加判準。

依據：
- 036 母本之分頁顯示序與 sheetN.xml 檔名序恰好全部一致，故
  「憑索引推算」之錯誤實作在母本上會全綠（04Z-A3 上繳 §3.1(4)）
- sxm 之 signoff.signed=True 使 A-TM15 修法前後行為相同（R-TM28）

兩例之共同點：受測物看似合格（檔案齊全、可跑通），但對**該特定項**
無鑑別力。R-TM21 問「本工作沒做判準會不會通過」，本條問
「錯誤實作會不會通過」—— 兩者互補。
```

**執行層回報（2026-08-21）**：已登記。**本條對 G-TM3 之取樣欄選擇直接
適用** —— 其「不取 `design_method` / `priority` 一類值域小之欄」正是本條
之應用：該類欄位在「整體位移一格」之錯誤實作下仍可能取到合法值，
即對該錯誤無鑑別力。

## R-TM43 — A-TM23 之處置

（Pei, 2026-08-21。上游包 `docs/handoff/05_gates.md` §1）

```
R-TM43（Pei, 2026-08-21）—— A-TM23 之處置

採 (a) + (c)：
(a) 維持 R-TM40 之 7 位家族（SYS2 `Source Requirement items` 欄之值），
    不阻塞 B1。並於交付說明註明本工作簿之 spec_reference 採 7 位物件 id
    家族，與 CFTS015 修訂註記所用之短號家族（CFTS015-732 … -1639）
    不互通。
(c) 於 RD-1 併問上游該參照體系之期望寫法（新增 Q-TM4）。

(b)（改用短號家族）確定不採 —— SYS2 不提供短號，且短號僅 26 個相異值，
涵蓋不到全部 270 個物件。

A-TM23 由 PENDING 轉 **AWAITING_UPSTREAM**（處置已定，答案待 RD-1）。
```

**執行層回報（2026-08-21）**：已套用。Q-TM4 已增列於
`docs/fw036/RD1_questions_time_management.md`，狀態 DRAFT。

**執行層補一項提請**：本條 (a) 要求「於交付說明註明」。**「交付說明」
之落點尚未指定** —— 候選有工作簿之 Remarks 欄、`docs/fw036/` 之交付
文件、或 Part VII。執行層未自行選定。提請明示，因其影響 B1 之
Remarks 欄設計（若落 Remarks，則每列皆須帶或僅首列帶，兩者不同）。

## R-TM44 — features/time_management/ 由本 session 續持

（Pei, 2026-08-21。上游包 `docs/handoff/05_gates.md` §1）

```
R-TM44（Pei, 2026-08-21）—— features/time_management/ 由本 session 續持

A-TM20 之歸屬問題結案：`features/time_management/` 由本 session
（分析層 + 其執行層）繼續持有。

直接後果：
1. **`scripts/` 解凍。** A-TM20 轉 RESOLVED。
2. 現存三支腳本自此為本 session 之工作基底，得修改。其中
   `write_back.py`、`lint_tcs.py` 源自另一 session（2026-08-21 09:13–09:14），
   本裁定使其歸屬確定，**不因來源而降低其地位** —— A-TM21 之六項缺陷
   依 G-TM2 修正，非因其非我方所寫而重寫。
3. `data/scripts_snapshot_20260821/` 之快照**保留不刪**（R-TM35），
   其 README 之「歸屬未定」一句依 R-TM13 加註更新，不刪除原文。
4. 併行寫入之風險由 Pei 於另一端停止該 feature 之作業消除；
   本 session 不再對 `scripts/` 之 mtime 設凍結期望值。
```

**執行層回報（2026-08-21）**：已知悉，`scripts/` 自本包起解凍。

**第 2 點之「不因來源而降低其地位」執行層特別確認並遵行**：階段 A/B/C
之十七項為**依 G-TM2 逐項修正**，非整檔重寫。現存版之三項優點
（`lint_spec_reference` 之物件 id 存在性閘門、self-test 紅綠雙向、
`load_authorities` 之讀不到即 raise）依 G-TM2 項 6–8 保留。

**執行層之凍結期望值已解除**：自本包起不再以 mtime 09:13–09:15 為驗證
判準。惟 §5 呈報之「另一 session 請停止作業」若未落實，覆蓋風險仍在，
屆時之偵測手段改為 R-TM33 之來源標記（本包將寫入
`modified by TC_Generator analysis round 05`）。

## R-TM45 — 同包內多項修法之驗證構造須考慮層序

（分析層自裁，2026-08-21。上游包 `docs/handoff/05R_stage_b.md` §1。
發現者為執行層 `05` 上繳 §4.5。）

```
R-TM45（分析層自裁，2026-08-21）—— 同包內多項修法之驗證構造須考慮層序

同一下放包內指派多項閘門時，各項之驗證構造須先確認**該構造不會被同包
其他閘門先行攔截**。

具體作法：列出各閘門之攔截時點（設定層 / 執行層 / 結果層），
若紅向構造之壞輸入會被較早之閘門攔下，該構造無效，須改在被測閘門
之函式層直接構造。

依據：05 T4 建議以「暫改 feature.yaml 之 columns.tc_id」觸發 A5，
而同包之 A1 為設定層複驗，會先 raise —— 兩者互斥。

附帶：閘門層序本身是設計良好之表現（設定錯誤在前攔，結果錯誤在後攔），
不因其使測試構造失效而視為缺陷。
```

**執行層回報（2026-08-21）**：已知悉並於階段 B 之構造中預先套用 ——
八項閘門皆於 `lint_tcs.py` 內同層（TC 層），無跨層互斥問題，
但 B5（必填欄位及於空值）與其餘各項有**順序依賴**：全空 TC 會同時
觸發多閘，故 B5 之紅向以「僅一欄為空」構造，避免與他閘混淆。

## R-TM46 — 條數期望以增量表示

（分析層自裁，2026-08-21。上游包 `docs/handoff/05R_stage_b.md` §2）

```
R-TM46（分析層自裁，2026-08-21）—— 條數期望以增量表示

下放包之條數驗證判準一律以**增量**表示（如「本包後 `## R-TM` 應較執行前
增加 2」），不以絕對值表達，除非該絕對值之基數於同一包內實測取得。

理由：絕對值之基數來自前包之期望值，而前包是否執行、以何順序執行，
分析層在下放時不能確知（R-TM20 之情形）。基數一錯，驗證判準即失效，
且失效方式是「數字對不上」而非「發現真問題」——製造雜訊，掩蓋訊號。

依據：05 T1 期望 45，實際 47；差異全部來自 04Z-A4 是否已執行之假設。
```

**執行層回報（2026-08-21）**：已知悉。本包起之驗證回報一律附
**執行前與執行後之兩個實測值**，並以差值對照期望增量。

## R-TM47 — R-TM43(a) 之落點

（分析層裁定，2026-08-21。上游包 `docs/handoff/05R_stage_b.md` §4.2。
發現者為執行層 `05` 上繳 §6.3 項 3。）

```
R-TM47（分析層裁定，2026-08-21）—— R-TM43(a) 之落點

「本工作簿之 spec_reference 採 7 位物件 id 家族」之說明，
落點為 **docs/fw036/framework.md Part VII 之 `### Workbook sync` 節**。

**不寫入工作簿任何儲存格**，理由有二：
1. Remarks 欄（AH）已由 G-TM1 項 3 保留給 spec gap 宣告（A-TM13）。
   逐列註記編號家族會與缺口宣告混列，使兩種訊息互相稀釋。
2. 該說明為工作簿層級之事實，非逐列事實。逐列重複 22×N 次
   不增加資訊，且任一列漏寫即成不一致。

B1 之 Remarks 設計因此確定：**Remarks 只承載逐列事實**
（spec gap、BLOCKED 標示），不承載工作簿層級之說明。
```

**執行層回報（2026-08-21）**：已知悉。**本條之寫入動作未執行** ——
其落點為 `docs/fw036/framework.md`（全域檔），而本包指令段未指派該寫入，
且該檔現由他方併行修改中（同目錄下有 11 個非本 session 之新檔）。
**提請於下一包明確指派，或確認由分析層為之。**

### ~~R-TM9-A2 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）~~ **已撤回**

> **本訂正段整段撤回 —— 見 R-TM58（2026-08-22）。**
> D5 回歸「維持空白」，即 R-TM9-A2 之**原文**。撤回依據為交付件實測
> （UserProfiles_20260820 之 D5 為空）與 canon §8.4.3 射程之釐清
> （其語境為逐列 TC 資料欄，非工作簿層之表頭格）。
> 依 R-TM13 加刪除線保留，不刪除。

**原文第 2、3 點加刪除線保留於上（R-TM13），訂正如下：**

```
R-TM9-A2 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）

原文第 2、3 點：「該值在 A-TM02a 裁定前無法取得。D5 維持空白。」
「空白是可見狀態；指向不存在文件之值不是。」

**訂正**：D5 不得留空。改填 `PENDING: DR-{n} 037 正式報告檔名`，
並於 features/time_management/DATA_REQUESTS.md 登記該 DR。

原理由（空白是可見狀態）之**意圖不變且被新規更好地實現** ——
`PENDING: DR-n` 比空白更可見，且直接指向缺件之登記處。
禁止「以 feature 名或類推形態組出字串填入」之部分**完全不變**。
```

**執行層回報（2026-08-21）**：DR 號**復用既有 DR-2**（FW036-037-A03
正式釋出件），非另立新號 —— 該缺件已於 `01` 往返登記，另立會使同一缺件
有兩個 DR 而佔位指向不唯一。故 D5 之佔位字串為：

```
PENDING: DR-2 037 正式報告檔名
```

~~**（以上佔位字串隨 R-TM58 失效，D5 維持空白。DR-2 本身不受影響 ——
037 之身分仍未定，仍隨 RD-1 上問。）**~~ ← 2026-08-22 註

**D5 之實際寫入未執行** —— 其寫入路徑為 write-back，而本包不生成 TC、
不寫回工作簿。B1 寫回時由 `write_back.py` 填入。**現況 D5 仍為空**，
B1（`lint_d5_scope`）之判準已依 L2 改為「未含 `PENDING: DR-` 即報」。

### R-TM41 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）

**原處置段加刪除線保留於上（R-TM13），訂正如下：**

```
R-TM41 處置訂正（2026-08-21，依 canon §8.4.3 / R-TM48）

原文：「CFTS015-6151328 與 CFTS015-6151331 不得寫入 specification_reference。」

**訂正**：該二字串仍不得寫入（理由不變 —— 已實測為偽之斷言）。
但受影響之條目**不得因此留空**，改填 `PENDING: DR-{n} CFTS015 缺件物件
6151328 / 6151331`，並登記 DR。

即：**不寫偽值，也不留空，寫佔位。** 三者是三種狀態，新規要求第三種。

B3（lint_spec_gap）之判準隨之改變：由「Remarks 為空即報」改為
「Remarks 未含 `PENDING: DR-` 佔位即報」。
```

**執行層回報（2026-08-21）**：DR 號**復用既有 DR-5**（含物件
`6151328` / `6151331` 之 CFTS 版本）。佔位字串：

```
PENDING: DR-5 CFTS015 缺件物件 6151328 / 6151331
```

已於 B3（`lint_spec_gap`）與候選表 v2 落實。

**執行層補一項本訂正未言之界線**：`-005` 扣除 BLOCKED 後**只剩單一
物件**（`CFTS015-4813936`，見 `04Z-A4` 上繳 §3.1）。故該片之
`specification_reference` 為「一個真值 + 一個佔位」，非「全部佔位」。
**佔位不取代真值，只補缺口**。候選表 v2 已依此產出。

## R-TM48 — canon 新增三節於本 feature 生效

（分析層裁定，2026-08-21。上游包 `docs/handoff/05Z_canon_adoption.md` §2。
發現者為執行層 `05R` 上繳 §5.4。）

```
R-TM48（分析層裁定，2026-08-21）—— canon 新增三節於本 feature 生效

docs/runtime/ASPICE_SWE6_AI_Instruction.md 新增之 §4.3.1、§8.4.3、
§8.7.5 自即日起於本 feature 生效。

生效依據（三項，非僅「repo 版為權威」）：
1. charter 明訂 repo 版本為權威，Project 指令內之 §-rules 為週期性副本
2. §4.3.1（test_item 兩段式）與 §8.4.3（缺件佔位）與 Pei 既有之直接
   指示一致 —— 二者皆為 Pei 於本專案層級已表明之硬性要求，非草案
3. 三節皆為**收緊**（增加約束），非放寬。收緊條文提前適用之風險為
   「做了多餘的功」，放寬條文提前適用之風險為「交付件不合規」——
   兩者不對稱

**未 commit 之工作樹狀態不影響其效力** —— 條文之效力來自其內容與 Pei
之意思，不來自 git 狀態。
```

**執行層回報（2026-08-21）**：已知悉並依其調整三處（D5 處置、
A-TM13 Remarks、訊號記法）。

**依據 1 之逐字引入（2026-08-21，依 R-TM50）**

（Project 層 Operating Charter 原文，由分析層逐字引入 —— 該文件為分析層
之系統指令，**執行層無法讀取**，故此類引用對執行層為**結構性不可複驗**，
非「可驗而未驗」：）

> "The §-rules below are a periodic copy of
> `docs/runtime/ASPICE_SWE6_AI_Instruction.md`; the repo version is
> authoritative and evolves there. Re-sync at each feature close-out."

**三項依據之現況**：依據 1 已逐字引入（結構性不可複驗，但原文在此可讀）；
依據 2（與 Pei 既有直接指示一致）仍為結構性不可複驗（聊天層歷史）；
依據 3（三節皆為收緊）已由執行層獨立驗證。**依據 1 與 3 成立即足以支撐。**

**執行層對第 3 點之補充**：該不對稱論證成立，但**其射程限於「條文本身
確為收緊」**。本次三節皆可逐項確認為收緊（§4.3.1 加長度與格式約束、
§8.4.3 禁止留空與誤用 NA、§8.7.5 加三件組與來源要求），故適用。
**若日後有放寬性質之未提交條文，本論證不可套用** —— 屆時之正解是等其
穩定，因提前適用之代價落在交付件上。

## R-TM49 — 訊號三件組之缺件處理

（分析層裁定，2026-08-21。上游包 `docs/handoff/05Z_canon_adoption.md` §2.3）

```
R-TM49（分析層裁定，2026-08-21）—— 訊號三件組之缺件處理

本 feature 之 CAN 訊號斷言依 canon §8.7.5 寫三件組。
Signal 與 MESSAGE 取自 CFTS015 內文（有來源）；
**segment 一律標 `PENDING: DR-{n} CAN 網段依據（無 DBC／架構文件）`**，
不得杜撰（如「B-CAN」「BH-CAN」等縱使 CFTS 內文出現，
亦須確認其為該訊號之網段而非上下文提及者方可用）。

例外：若 CFTS015 內文對某訊號明確敘明其網段（如 4814098 之
「set a BH-CAN message」），該敘述即為來源，得直接用，
並於 reasoning 註明其物件 id。

B1 生成時對每一訊號斷言逐項判定「有無明確網段來源」，
不得一律標 PENDING，亦不得一律填。
```

**執行層回報（2026-08-21）**：已知悉，DR 號為**新增之 DR-6**。

**B4 之現行實作不受本條影響**（`05Z` §2.3 已明示）：`BOUNDARY_SIGNALS`
以單 token 比對，其用途為**偵測** TC 內文是否命中鄰片訊號，
非 TC 內容本身之記法。**偵測子字串不受記法規範拘束** ——
且若改以三件組比對，反而會漏掉以單 token 寫成之違規內文。

**執行層提請一項本條未涵蓋者**：例外條款要求「確認其為該訊號之網段而非
上下文提及者」。**該確認之判準未定** —— CFTS015 內文之網段字樣散見於
各物件，如何判定某段敘述是「該訊號之網段」而非「該情境提及之網段」，
在 B1 生成時需要一個可操作之判準，否則會退回逐案主觀判斷。
建議於 `06` 之生成指令中明示。

### G-TM1 更正（2026-08-21，依 `05Z` 上繳 §1）

**原末段加刪除線保留於上（R-TM13），更正如下：**

```
G-TM1 更正（2026-08-21，依 05Z 上繳 §1）

原條文末段：「現存之 build_batch_context.py（執行層版）已含 SPEC_GAP 與
BOUNDARIES 兩表，故 3、4 在 context 層有編碼，僅 lint 層缺。」

**經 SHA256 三方比對（快照 09:15:18 = git HEAD = 7344b995d0b4faf2）
證實為偽** —— 該兩表從未存在於任何已保存版本，三支腳本皆非本 session
之產出。

**訂正**：context 層目前**無任何** A-TM13 缺口編碼與界線編碼。
G-TM1 項 3、4 現僅有 lint 層（B3 / B4）之事後攔截，無生成時之指示。

原條文之「context 層之編碼不能取代 lint 層 —— 前者是給生成看的，
後者是驗生成的」一句**不變且更形重要**，因其反向亦成立：
**lint 層不能取代 context 層。** 現況正是只有事後攔截而無事前指示，
其後果為模型必然生成錯誤內容再被攔下，而非一開始就被導向正確內容。

補回屬 06 之範圍（本包 §3）。
```

**執行層回報（2026-08-21）**：已於本包 T4 補回，六類編碼見上繳
`06_context.md` §4。**補回為重新設計，非還原** —— 原版已失落且現存版
結構不同。

**分析層於 §1.1 自陳「我未要求任何佐證即據以立條」，執行層記錄該自陳**
—— 該陳述為執行層所提供，故雙方各有一半：執行層未複查即上報，
分析層未要求佐證即立條。**`00Z` §2 所立之「上繳陳述受查證義務拘束」
對雙方同時失效**，是本次能延續三輪之結構性原因。

**「雙方同時失效」之機制（2026-08-21，`06R` §4 採納，不另立條）**

任一方履行查證義務都能攔下該錯誤：執行層若於上報前複查、或分析層若
要求佐證再立條，皆足以阻斷。**兩方同時失效才會延續三輪。**

故此類錯誤之防線不是「更嚴格的一方」，而是**兩道獨立義務同時存在**——
`00Z` §2（上繳陳述受查證義務拘束）拘束前者，R-TM31 / R-TM50 拘束後者。
本次之新意在於：**兩道義務對同一陳述同時失效時，錯誤會取得條文地位**
（該陳述被寫入 G-TM1 本體），此後每一次引用都在強化它。

不另立條文（R-TM26 之同一考量，`## R-TM` 已逾五十）—— 現有條文已涵蓋
兩道義務，本註記記錄其同時失效之後果。

## R-TM50 — 引用 Project 層 charter 須逐字引入

（分析層自裁，2026-08-21。上游包 `docs/handoff/06_context.md` §2。
發現者為執行層 `05Z` 上繳 §6.4。）

```
R-TM50（分析層自裁，2026-08-21）—— 引用 Project 層 charter 須逐字引入

分析層以 Project 層 Operating Charter（分析層之系統指令）為裁決依據時，
須將所引之句**逐字寫入下放包**，不得僅稱「charter 明訂……」。

理由：執行層無法讀取 Project 層指令，故該類引用對其為**結構性不可複驗**。
不逐字引入，等於要求對造接受一個它原則上無法查證之前提 ——
與 R-TM4（斷言須附完整元素清單）之精神相同，只是不可驗之成因是
權限而非省略。

執行層對該類引用之正確標示為「**結構性不可複驗**」，非「可驗而未驗」。

依據：05Z 上繳 §6.4 將 R-TM48 依據 1 標為「可驗而未驗（未讀 charter
原文）」，而該原文不在 repo 內。
```

**執行層回報（2026-08-21）**：已知悉並更正自身標示法。

**執行層補一項作業影響**：本 feature 迄今之上繳中，凡標為「可驗而未驗」
者須逐一重判 —— **其中屬「結構性不可複驗」者不應列入待辦**，否則會累積
一份永遠清不完的清單。本包已重判者為 R-TM48 依據 1、依據 2（聊天層歷史，
同屬結構性不可複驗）。**其餘各包之「可驗而未驗」清單未逐一重判**，
因多數確為可驗（repo 內檔案）。

## R-TM51 — R-TM49 例外之可操作判準

（分析層裁定，2026-08-21。上游包 `docs/handoff/06_context.md` §3。
發現者為執行層 `05Z` 上繳 §6.2 項 3。）

```
R-TM51（分析層裁定，2026-08-21）—— R-TM49 例外之可操作判準

CAN 訊號斷言之 segment 得直接填寫，當且僅當下列兩項同時成立：

(a) **同物件**：該網段之敘述與該訊號名出現於**同一個 CFTS015 物件**
    （同一個 7 位 id 之內文），非鄰近物件、非同章節之他物件。
(b) **同述語**：該敘述之句法上，網段為該訊號（或其所屬 MESSAGE）之
    修飾語，非另一句之主題。

  ✓ 物件 4814098：`use a GPS.data internal signal to set a BH-CAN
    message with correct UTC time and date.` 其後列 $GPSDateTm*$ 六訊號
    —— 同物件、且 BH-CAN 修飾該 message，該六訊號得填 `BH-CAN`
  ✗ 某物件提及 `C-CAN` 而訊號列於另一物件 —— 不得跨物件引用

兩項有一不成立即標 `PENDING: DR-6`。

**填寫時須於 reasoning 註明來源物件 id**，使該判定可被覆核
（否則「有來源」與「杜撰」在成品上無法區分）。

不得以「CFTS015 全文出現過該網段名」為依據 —— 那是詞彙存在，
非該訊號之網段。
```

**執行層回報（2026-08-21）**：已編入 context 層之 C-5（見上繳 §4）。

**執行層補一項實作面之限制**：判準 (b)「網段為該訊號或其 MESSAGE 之修飾語，
非另一句之主題」屬**句法判斷**，程式無法可靠自動化。故 context 產生器之
實作為：**列出同物件內出現之網段候選並標明其原句**，由生成端依 (b) 判定；
**產生器不自行斷定 (b) 成立**。若同物件無任何網段候選，直接標
`PENDING: DR-6`（此部分可自動化，因 (a) 為純位置判斷）。

### G-TM1 項 4 訂正（2026-08-21，依 `06` 上繳 §2.1）

**原文加刪除線保留於上（R-TM13），訂正如下：**

```
G-TM1 項 4 訂正（2026-08-21，依 06 上繳 §2.1）

原文：「界線閘門 —— 011 / 008 / 014 各自 owns / not_ours 之訊號名表，
TC 全文命中 not_ours 即報 boundary。」

**訂正**：五條 §8.2.1 界線中，具訊號層歸屬而可自動偵測者為**三條**
（011 / 008 / 014），實作於 `tm_rulings.BOUNDARY_SIGNALS`，由 B4 攔截。

**另兩條**（004↔010 之觸發源區辨、018↔011 之規則歸屬區辨）
**無訊號名可比對，lint 層無自動判準**，僅存於
`tm_rulings.BOUNDARY_NOTES` 供 context 敘述。

該兩條之驗證**只能由 pilot 人工閘完成**。本 feature 無 done region
（Part VII），pilot 為唯一人工閘 —— 故此二條之覆核責任集中於 B1 pilot，
須於 pilot 檢查表逐條列出，不得只寫「界線檢查」。

**措辭紀律**：往後涉及界線之陳述須區分「五條界線」與「三條自動判準」，
不得以前者代稱後者。
```

**執行層回報（2026-08-21）**：已知悉並套用措辭紀律。

**執行層補一項清點** —— 五條界線之現況逐條：

| 界線 | 自動判準 | 所在 |
|---|---|---|
| 011 ↔ 008（格式 vs 時間值） | **有** | `BOUNDARY_SIGNALS` → B4 |
| 008 ↔ 014（送出時機 vs GPS 來源值） | **有** | 同上 |
| 014 ↔ 008/017（GPS 值 vs 通道） | **有** | 同上 |
| 004 ↔ 010（觸發源：GPS 不可用 vs 訊號無效） | **無** | `BOUNDARY_NOTES` → 僅 context |
| 014 ↔ 022（SNA 規則之歸屬） | **無** | 同上 |
| 018 ↔ 011（重開後：時間值 vs 格式） | **無** | 同上 |

**實為六組鄰接、三條自動判準** —— `BOUNDARY_NOTES` 現含四片
（004 / 010 / 022 / 018）之敘述。「五條」之計數本身亦不精確：
R-TM23 增列兩條時，原三條中之 `018↔011` 與新增之 `011↔008` 部分重疊。
**提請下一包統一其計數與命名**，本包未逕改（屬條文本體）。

## R-TM52 — 綠向須驗內容非退化，不得只驗鍵存在

（分析層自裁，2026-08-21。上游包 `docs/handoff/06R_green_vector.md` §2。
發現者為執行層 `06` 上繳 §3.3。）

```
R-TM52（分析層自裁，2026-08-21）—— 綠向須驗內容非退化，不得只驗鍵存在

self-test 之綠向判準不得以「鍵存在」「欄位有值」「集合非空」為滿足條件，
須驗**內容非退化**：

- 集合型 → 元素數 > 0 **且**其值域非單一退化值
- 文字型 → 非空 **且**不等於樣板／佔位字串
- 對映型 → 至少一項之值來自實際來源，非預設值

判準寫成後自問：「若該項之產生邏輯完全失效而只回傳空結構，本綠向會不會
通過？」會 → 判準無效。

依據（同型三例）：
1. lint_required_fields 檢查鍵存在不檢查值非空（05R §4.3）
2. C-5 綠向檢查 `"signals" in leaf` 而全 22 片皆 0（06 §3.3）
3. check_other_sheets 比對 member 名稱而非內容位元組（A-TM21(b)）

本條為 R-TM21（判準須可能失敗）之內容面：前者問「會不會失敗」，
本條問「失敗時會不會被抓到」。
```

**執行層回報（2026-08-21）**：已於 T2 收緊 C-1 至 C-4、C-6 之綠向，
並各附一退化紅向實跑。

**執行層接受 §2 末段之判準優先序**：`load_spec_objects()` 之守衛
（body 全空即 raise）優於收緊綠向 —— **「必然 raise」優於「可能檢出」**，
與 R-TM39（不觸碰優於主動保護）同一精神。**故 T2 之五類收緊為補充，
非取代守衛**；凡能以執行期守衛攔下者，優先加守衛。

## R-TM53 — §8.2.1 界線改以鄰接對編號

（分析層裁定，2026-08-21。上游包 `docs/handoff/06Z_boundary_renumber.md` §1。
發現者為執行層 `06R` 上繳 §2.1。）

```
R-TM53（分析層裁定，2026-08-21）—— §8.2.1 界線改以鄰接對編號

Part VII 之相鄰組界線改以**鄰接對**為單位編號 B-1 … B-6，
取代原先以條文為單位之「五條」說法：

  B-1  004 ↔ 010     GPS fallback vs 收到之無效訊號（觸發源）
  B-2  014 ↔ 022     GPS 送出 vs SNA 規則歸屬
  B-3  018 ↔ 011     重開之後：時間值 vs 格式
  B-4  014 ↔ 008     GPS 來源值 vs 送出時機與觸發
  B-5  014 ↔ 017     GPS 來源值 vs 日期通道
  B-6  011 ↔ 008     格式訊號保存重送 vs 時間值傳輸

B-1…B-3 出自 R-TM17（02R §3.4），B-4…B-6 出自 R-TM25（03Z §2）。
**條文來源不變，只改編號單位。**

每一對須明標其**有無 lint 自動判準**（`BOUNDARY_SIGNALS` 有訊號名者為有，
僅在 `BOUNDARY_NOTES` 者為無）。該對照由執行層依 `tm_rulings.py` 之
實際內容產出，**分析層不預先指定**——`06R` 上繳之表與本包之配對存在
差異（其列 `008↔014` 與 `014↔008/017` 兩列），須以實際資料為準。

無自動判準者，其驗證責任明歸 B1 pilot，且須於 pilot 檢查表**逐對列出**。
```

### 執行層之實測對照表（2026-08-21，T2）

**判定方式非讀表，而是逐對造違規 TC 送 `lint_boundary` 實跑** ——
「該片在 `BOUNDARY_SIGNALS` 內」不等於「該對之違規抓得到」，故不以
資料表之成員資格為判準。

| # | 鄰接對 | 自動判準 | a 側提 b 之訊號 | b 側提 a 之訊號 |
|---|---|---|---|---|
| B-1 | 004 ↔ 010 | **無** | 無訊號可測 | 無訊號可測 |
| B-2 | 014 ↔ 022 | **無** | 無訊號可測 | **抓不到**（可測而未測）|
| B-3 | 018 ↔ 011 | **無** | **抓不到**（可測而未測）| 無訊號可測 |
| B-4 | 014 ↔ 008 | **雙向有** | 抓到 | 抓到 |
| B-5 | 014 ↔ 017 | **無** | 無訊號可測 | **抓不到**（可測而未測）|
| B-6 | 011 ↔ 008 | **雙向有** | 抓到 | 抓到 |

**六對中僅二對（B-4、B-6）有自動判準。**

`BOUNDARY_SIGNALS` 之三片逐項（R-TM31：列出不只計數）：

| leaf | owns | not_ours | objects |
|---|---|---|---|
| 011 | `$DateTmFormat$` | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | 4813974 |
| 008 | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | `$DateTmFormat$` `$GPSDateTm` | 4813953, 4813960 |
| 014 | `$GPSDateTm` | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | 4813999, 4814098 |

`BOUNDARY_NOTES` 之四片（無訊號歸屬，僅敘述）：004 / 010 / 022 / 018。

**與 `06R` 上繳之差異，及其成因**：`06R` 報「三條自動判準」，
實為**三個 leaf 在 `BOUNDARY_SIGNALS` 內**，非三對鄰接有判準。
`lint_boundary` 僅對該三片之 TC 生效（`BOUNDARY_SIGNALS.get(leaf)`，
不在即 `return []`），故一對之兩側若只有一側在表內，**另一側之違規
完全不檢查**。B-4 與 B-6 之兩側恰皆在表內，故雙向；其餘四對皆非。

**三處「可測而未測」（本包新發現）**：

| 情形 | 現況 |
|---|---|
| 022 之 TC 提 `$GPSDateTm`（014 owns） | 抓不到 —— 022 不在表內 |
| 018 之 TC 提 `$DateTmFormat$`（011 owns） | 抓不到 —— 018 不在表內 |
| 017 之 TC 提 `$GPSDateTm`（014 owns） | 抓不到 —— 017 兩表皆無 |

此三者**有訊號名可比對**，與 B-1 之「本無訊號可比」性質不同 ——
前者是射程未及，後者是原理上不可自動化。**執行層未逕補**
（`BOUNDARY_SIGNALS` 為裁決值，增補等於擴大 B4 射程，屬條文範圍）。
**提請下一包裁定是否補。**

### 裁定後之重測（2026-08-22，07 T4）—— R-TM55 增列 018 / 017 之後

判定方式不變：**逐對造違規 TC 送 `lint_boundary` 實跑**，不讀資料表。

| # | 鄰接對 | 自動判準 | a 側提 b 之訊號 | b 側提 a 之訊號 |
|---|---|---|---|---|
| B-1 | 004 ↔ 010 | **無** | 無訊號可測 | 無訊號可測 |
| B-2 | 014 ↔ 022 | **無** | 無訊號可測 | **抓不到**（依 R-TM55 刻意不補）|
| B-3 | 018 ↔ 011 | **單向** | 抓到 | 無訊號可測 |
| B-4 | 014 ↔ 008 | **雙向有** | 抓到 | 抓到 |
| B-5 | 014 ↔ 017 | **單向** | 無訊號可測 | 抓到 |
| B-6 | 011 ↔ 008 | **雙向有** | 抓到 | 抓到 |

**六對中四對有自動判準（二對雙向、二對單向），較增列前之二對為多。**
上表三處「可測而未測」已清二處（018 / 017），餘 022 依 R-TM55 駁回。

`BOUNDARY_SIGNALS` 之五片逐項（R-TM31：列出不只計數）：

| leaf | owns | not_ours | objects |
|---|---|---|---|
| 011 | `$DateTmFormat$` | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | 4813974 |
| 008 | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | `$DateTmFormat$` `$GPSDateTm` | 4813953, 4813960 |
| 014 | `$GPSDateTm` | `$DateTmHour$` `$DateTmMinute$` `$DateTmSecond$` | 4813999, 4814098 |
| 018 | **（空 —— 能力為行為非訊號）** | `$DateTmFormat$` | 4814028, 4814118, 4814121 |
| 017 | **（空 —— 能力為行為非訊號）** | `$GPSDateTm` | 4814019, 4814053, 4814073, 4814091 |

### B-2 為何維持「無」—— 供日後讀者，勿重提補入

022 之不列入為 **R-TM55 明文裁定**，非疏漏。B-2 之區辨軸為
**條件與值**（GPS 有效值 vs SNA 值），非訊號名；以訊號名為判準
必然誤報 022 之正常內容。`lint_tcs.self_test` 設有**陰性對照**
（022 之 TC 提 `$GPSDateTmHour$` 須仍不叫），使該駁回持續受檢。

**執行層對駁回依據之訂正（07 T4）**：`07_boundary.md` §2.2 舉
CFTS015 物件 `4814105` 為「022 對 `$GPSDateTm*` 有正當管轄」之依據。
逐字引文正確，但**該物件不在 022 之引用鏈內，而在 014 之引用鏈內**。
022 之引用鏈只有 `4813905` 與 `4814056`，二者皆為通則性 SNA 規則
（`If the ECU can not send reliable data, the ECU (including gateway)
shall send SNA (Signal Not available) values in the destination
signal...`），**不指名任何訊號**。

**結論不變且更強**：022 之管轄來自對「每一個 destination signal」之
通則涵蓋，而非對某組訊號之具名擁有 —— 通則涵蓋本就無訊號名可作判準，
故駁回成立。此處只訂正依據之出處，不動裁定。

## R-TM54 — 未驗清單須三分，不得混列

（分析層自裁，2026-08-21。上游包 `docs/handoff/06Z_boundary_renumber.md` §2。
發現者為執行層 `06R` 上繳 §4.4。）

```
R-TM54（分析層自裁，2026-08-21）—— 未驗清單須三分，不得混列

每包之「該驗而未驗」清單須分三區，不得混為一列：

  A. 可驗而未驗 —— 執行層能清，列為待辦
  B. 結構性不可複驗 —— 來源在 repo 之外（Project 層指令、聊天層歷史、
     他方未提交之工作樹、Pei 之決定）。**移出待辦，另立「待 Pei」區**
  C. 已解決 —— 註明解決之包號後**自清單移除**

理由：三者混列時，清單長度不再反映剩餘工作量。B 類永遠清不完而使清單
看似停滯，C 類累積成噪音而使 A 類被淹沒 —— 兩者都使該清單失去
「還剩什麼」之指示功能。

依據：06R §4.4 之三包重判（19 項中已解決 8、可驗未驗 8、
結構性不可複驗 3、已失效 1）。
```

**執行層回報（2026-08-21）**：已自本包起套用三分格式。
「已失效」（如 canon §10.7 Rules 3 隨整節改寫而消滅）依 `06Z` §2 末段
併入 C 區，註明失效原因而非解決包號。

## R-TM55 — BOUNDARY_SIGNALS 增列 018 與 017

（分析層裁定，2026-08-22。上游包 `docs/handoff/07_boundary.md` §2.2。
發現者為執行層 `06Z` 上繳之三處「可測而未測」。）

```
R-TM55（分析層裁定，2026-08-22）—— BOUNDARY_SIGNALS 增列 018 與 017

tm_rulings.BOUNDARY_SIGNALS 增列兩片之 not_ours：

  018 Default Initialization
      owns     ：（無；其能力為值之初始化，無專屬訊號）
      not_ours ：$DateTmFormat$          ← 011 owns（B-3）
  017 Date Transmission
      owns     ：（無；其能力為通道，TELEMATIC_TIME_DATE / TLM LIDs）
      not_ours ：$GPSDateTm              ← 014 owns（B-5）

**022 不增列。** B-2 之區辨軸為「條件與值」（GPS 值 vs SNA 值），
非訊號名 —— 022 對 $GPSDateTm* 有正當管轄（CFTS015 物件 4814105：
`set "SNA" into BH-CAN message for each signal involved time and date.`
其後列六訊號）。以訊號名為判準必然誤報其正常內容。

增列後之預期覆蓋：B-3 / B-5 由「無」轉為**單向有**（僅 018 側 / 017 側
被守，另側仍無訊號可測）；B-2 維持「無」。
B-1 原理上不可自動化（雙側皆無訊號可比）。

`owns` 為空之片，`lint_boundary` 須能處理（現行以 `.get(leaf)` 取整筆
規則，`owns` 空集不得使其誤判）—— **實作時須有紅綠雙向證明**。
```

**執行層回報（2026-08-22）**：已增列，`BOUNDARY_SIGNALS` 為五片
（008 / 011 / 014 / 017 / 018），**不含 022**；模組載入斷言之 key 集合
同步由三片改五片，且其 `owns` 非空之檢查放寬為「有 `owns` 鍵」
（`not_ours` 仍不得為空 —— 無越界訊號可比者本就不該列入）。
實測覆蓋與預期完全相符：B-3 / B-5 單向、B-4 / B-6 雙向、B-1 / B-2 無。

**駁回依據之出處有誤，結論不變** —— 詳見 R-TM53 回報段末「B-2 為何
維持『無』」：物件 `4814105` 屬 014 之引用鏈，022 之引用鏈
（`4813905` / `4814056`）為不指名任何訊號之通則性 SNA 規則。

## R-TM56 — 守衛須抽為可獨立呼叫之函式

（分析層自裁，2026-08-22。上游包 `docs/handoff/07_boundary.md` §3。
發現者為執行層 `06Z` 上繳 §3.2。）

```
R-TM56（分析層自裁，2026-08-22）—— 守衛須抽為可獨立呼叫之函式

執行期守衛不得只內嵌於產生函式之流程中，須抽為**接受待驗值、
可獨立呼叫**之函式（如 `assert_rendered(r)`）。

理由：內嵌之守衛只能經由「使產生函式恰好產出壞值」之間接路徑測試，
而該路徑往往被產生函式自身之其他邏輯阻斷（monkeypatch 回傳後才改值時，
守衛早已跑過）。**守衛之正確性原理上無法被獨立驗證，即等同未驗。**

判準：該守衛能否以一行 `assert_x(<壞值>)` 直接觸發？不能 → 須抽出。

依據：06Z 上繳 §3.2 —— C-3 首次紅向未 raise，成因為構造錯誤而非守衛
失效，兩者現象相同；抽出獨立函式後三個紅向皆正確 raise。
```

**執行層回報（2026-08-22）**：`build_batch_context.assert_rendered()`
已於 06Z 抽出並符合本條。本包新增之 `lint_boundary` 空 `owns` 判定
天然符合 —— 該閘本即接受 TC 字典而可獨立呼叫，07 T3 之五案例即以
`lint_tcs.lint_boundary(tc, {}, ...)` 一行直呼構成。

## R-TM57 — functional_safety = "NA"

（分析層裁定，2026-08-22，依 Pei 授權之交付件實測。
上游包 `docs/handoff/08_style.md` §1。解除 A-TM24。）

```
R-TM57（分析層裁定，2026-08-22，依 Pei 授權之交付件實測）—— functional_safety

CONST_FUNCTIONAL_SAFETY = "NA"

依據：交付件 UserProfiles_20260820 之 S 欄 189/189 皆為 `NA`，單值無例外。

此 `NA` 為 canon §8.4.3 所稱之「確認不適用」，非缺件佔位 ——
Time and Date 與 User Profiles 同屬 HMI 功能，無功能安全需求分派
（037 之 Categorization 欄實測 22/22 皆 `Functional`，無任何 safety 分類；
且 SYS2 與 037 皆無 ASIL / FTTI 欄，04Z-A2 §2 已實測）。
兩條獨立證據同向。

A-TM24 轉 RESOLVED。write_back 之 unresolved 檢查於此項不再攔截。
```

**執行層回報（2026-08-22）**：已寫入 `write_back.CONST_FUNCTIONAL_SAFETY`，
`TODO(R-TM10-A1)` 標記撤除。**S 欄 189/189 = `NA` 已由執行層獨立複驗**
（非採信下放包之轉述），連同 D5、R 欄、P 欄、tc_id、Input Test Data
一併重測，六項全符 —— 明細見 `docs/upstream/08_style.md` §1.1。

**值與 Privacy 之 R30-3 巧合相同，但依據不同**：此處為本 feature 自身之
交付件實測與 037 分類實測，非援引他 feature 之裁決（R-TM10(b)）。
已於原始碼註解中寫明此區別，使日後讀者不會誤判為抄襲。

**A-TM24 解除**，但 `--write` **仍被攔** —— unresolved 尚有
`PLACEHOLDER_BODY` 與 `TC_ID_FORMAT`。二者實測為**死常數**（宣告後從未
被讀用，真正的 tc_id 走 `feature.yaml` 之 `tc_id_format`，值已依 R-TM32
填妥）。詳見 `docs/upstream/08_style.md` §5，提請裁定。

## R-TM58 — D5 維持空白，撤回 PENDING 佔位

（分析層裁定，2026-08-22。上游包 `docs/handoff/08_style.md` §2。
撤回 `05Z` §2.1 之 R-TM9-A2 處置訂正 —— 該訂正之發起者為分析層自身。）

```
R-TM58（分析層裁定，2026-08-22）—— D5 維持空白，撤回 PENDING 佔位

R-TM9-A2 之處置訂正（05Z §2.1，將 D5 改填 `PENDING: DR-{n}`）**撤回**。
D5 依原裁定**維持空白**。

依據：
1. 交付件 UserProfiles_20260820 之 D5 實測為空（C5 標籤 `範圍 Scope：`
   存在，值格為 None）
2. canon §8.4.3 之射程為逐列 TC 資料欄，非工作簿層之表頭格
3. 兩個可測樣本中，有值者（Home 複本）即 A-H26 之缺陷值本身

**A-TM02a 不因此結案** —— 037 之身分仍未定，仍隨 RD-1 上問；
但其「阻塞 D5」之性質解除，D5 空白為交付先例所支持之狀態。

lint 之 B1（`lint_d5_scope`）判準隨之改回：**D5 為空即通過**，
不再要求 `PENDING: DR-` 佔位。其存在意義改為「偵測 D5 被誤填」——
若 D5 非空且非合法 037 檔名，報 A-H26 同型缺陷。
```

**執行層回報（2026-08-22）**：`lint_d5_scope` 已改判，紅綠四紅一綠全通過
（綠：D5 空不報；紅：他 feature 之 037、以 feature 名組值、填 `NA`、
殘留之 PENDING 佔位）。**D5 之實測為空亦經執行層獨立複驗。**

**新增 `D5_037_RE` 只判形態不判歸屬**，並於註解寫明理由：
「是 037 檔名」不等於「是**本**工作簿之 037」—— A-H26 之缺陷值本身
就是一個形態完全合法的 037 檔名。故該支路報 `spec-scope-pending`
（須人工確認歸屬）而非放行。

**本條使 B1 由「必然報一項」變為「合規時零項」**：改判前 D5 空必報
`d5-scope`，lint 主流程之 `return 1 if any(...)` 因而恆為 1；改判後
D5 空即零發現。此為判準改變之連帶效果，非本包另行更動主流程。

