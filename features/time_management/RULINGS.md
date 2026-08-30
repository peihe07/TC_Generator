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

```
R-TM9 及 R-TM9-A1 關於 D5 值之全部內容撤回，包括
「feature 識別段 = Time-and-Date-HMI-V0.1」與前綴段之切分作業。
```
撤回理由：D5 之語意為「本工作簿所依據之 037 報告之文件識別」，
非 feature 標籤，故不可由 feature 名組成。

證據（交付路徑實測，2026-08-20）：
  Core HMI/HomeHMI/            → FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx
  Core HMI/Menu Bar and AppDrawer/ → FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx
  User Profiles/               → FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx
  Time Management/             → 無任何符合該形態之檔案

```
新規定：
1. D5 之值 = 本 feature 所依據之 037 報告之檔名（去副檔名），逐字照抄。
2. ~~該值在 A-TM02a（037 身分）裁定前無法取得。D5 維持空白。~~
3. ~~空白是可見狀態；指向不存在文件之值不是。~~任何情況下不得以
   feature 名、spec 標題或類推形態組出一個字串填入（§8.4.1）。
   ← **第 2、3 點之處置見條末訂正（canon §8.4.3）**
4. A-TM11 之解除條件改為：A-TM02a 裁定 + 037 檔名逐字實測。
   不再綁 Home 之前綴段切分。
```

```
R-TM8（test_group = "Time and Date"）不受本條影響 —— 該欄語意為功能
模組名，與 D5 之文件識別語意不同，兩者本不必一致。
```

## R-TM11 — 驗收條件不得預設 commit 節奏

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A3_review.md` §2）

```
下放包之驗收條件不得以 `git diff` 之範圍為判準。本專案全部 git 操作屬
Pei，執行層之工作樹持續累積跨往返之未提交更正，故 `git diff` 反映的是
「自上次 commit 以來」而非「本包」。

單行修改之正確驗收方式為：修改前 assert 目標字串存在且唯一、
以 count=1 取代、修改後複查該行。
```

依據：01Z-A2 T1 之驗收條件不可能成立。與 R-TM7 同族 —— 前者是指令
未經實測，本條是驗收條件未經可行性檢查。

## R-TM12 — 下放包一律附可執行指令段

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A4_command_set.md`）

```
每一個下放包末尾須有「指令」節，內容為執行層可直接照做之動作：
shell 指令、或逐字之貼入區塊與其插入位置。不得以「執行層下一步」之
散文條列代替。

R-TM7（指令須經實測）之射程限於有 CLI 之指令；檔案編輯、條文登記、
索引更新無 CLI 可查，一律直接寫死逐字內容與插入位置。
```

依據：00 rev A（無指令）、01（指令錯誤）、01Z-A3（散文條列）三次同型
缺失；01Z-A2 為唯一正確形態。

## R-TM13 — 條文之作廢一律加註保留，不刪除

（分析層自裁，2026-08-20。上游包 `docs/handoff/02_framework.md` §1.1）

```
任何已寫入 RULINGS.md／ANOMALIES.md 之條文、提案或推理，經證否或撤銷後
一律保留原文，加刪除線並以區塊引言標明作廢時點、依據包、與作廢理由。
下放包不得使用「整段換為」「刪除該段」等措辭。
```

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

```
（分析層，2026-08-20。上游包 `docs/handoff/02R_framework_lock.md` §1）

下放包末尾「本包產生之新條文清單」之每一列，指令段須有對應之登記指派
（寫入哪個檔、插在哪個位置、逐字內容）。自檢表列了而指令段未指派者，
視為下放包缺陷，非執行層漏做。

自檢表之功能是「確認條文已以區塊形式出現」，不等同「已指派落檔」。

依據：01Z-A4（A-TM02a）、02（R-TM13、framework）三次同型。
與 R-TM11／R-TM12／R-TM13 同族：四者皆為下放包自身之缺陷。
```

## R-TM15 — Layer 3 訊號之判讀限制

```
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
```

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

**第三實例（2026-08-22，`14` §4.2 / `15` §2）**：執行層為自檢 12 條 TC
所寫之「步驟 ↔ ER 語意對應」判準，實作為**共同實詞比對**（過濾長度 ≤3
之字後取交集）。`Wake the CAN bus` ↔ `The CAN bus is awake` 因 `bus` 被濾、
`wake` ≠ `awake` 而判為不對應 —— **10 項 style 發現全部為誤報**。

「共同實詞」不是語意對應之有效代理。**該判準正是「以結構特徵代替內容
判斷」，而它出現在為檢查該形態而寫的判準裡。** 分析層已獨立抽驗
（對 CFTS015 原文實查四項），四項複核與執行層一致。

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


### 記錄完備而內容錯誤 —— A-TM26 之實例（2026-08-22，`21` §4）

A-TM26 要求「凡自 LID 表取值者，須記錄取自哪一組架構欄」。
該要求在 `11`–`17` **九輪中逐輪執行，每條 TC 之 reasoning 皆載
`Atlantis High (col 26-30)`** —— 而 R-TM75 證實那九輪取的都是錯的欄。

**記錄完備，而記錄的內容整整九輪都是錯的。**
記錄之存在使人相信該面向已受控，其內容錯誤卻無人察覺。

**這同時是 A-TM26 最完整的一次驗證與最完整的一次否證**：
判準本身運作無誤（每次都記了），而它所保證的事與所需保證的事不同。
`14` §1.2 已將該射程限制寫入 docstring（「只驗記錄之存在，
不驗其正確性」），本次即為其實例化。

**正解為把記錄綁到另一個獨立來源**：`lint_arch_column` 現改驗
「reasoning 所記之架構欄須與該 TC 之 Pre-Condition 架構限定行一致」
（R-TM76）—— 兩者不一致時可被發現，而單一記錄自己與自己永遠一致。

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

## R-TM59 — 死常數處置採 (b)

（分析層裁定，2026-08-22。上游包 `docs/handoff/09_constants.md` §1。
發現者為執行層 `08` 上繳 §5；執行層所提之三選項中採 (b)，其理由
一併採納為本條依據。）

```
R-TM59（分析層裁定，2026-08-22）—— 死常數處置採 (b)

TC_ID_FORMAT：改為自 feature.yaml 之 write_back.tc_id_format 讀入，
  消除雙來源。不刪除該識別字 —— 保留「此處曾有一個值」之痕跡，
  且使 lint 日後可比對兩處。
  **同時加一項一致性檢查**：模組層讀入之值與 write_rows 實際使用者
  須為同一來源，不得各讀一次。

PLACEHOLDER_BODY：保留 TODO 標記，但**移出 unresolved 清單**。
  理由：其無任何使用點，未決不影響任何寫入。留在 unresolved 內
  等於以一個不生效之未決項阻擋整條寫回路徑。
  待 BLOCKED 佔位之寫入路徑實作時再移回。

執行層傾向 (b) 之理由（雙來源即本 feature 一路在防之漂移形態，
而現況恰為「一處已裁定、另一處還是 None」，且 lint 不會發現因兩處
從不比對）—— **採納為本條之依據**。

unresolved 檢查之判準由 `v is None` 改為 `v is None or v == ""`
（§4.1 紅向 2 之已知射程缺口，本包一併補）。
```

**執行層回報（2026-08-22）**：已實作，紅綠 **8/8**。
`--write` 之 unresolved **實測為空**（dry-run 印出「內容常數：全部已決」）。

**實作時發現本條所述之「雙來源」實為三來源**：除模組常數與 `write_rows`
外，`run()` 之 tc_id 預覽列印**又自行讀了一次** `cfg['write_back']
['tc_id_format']`。三處已全部改走唯一入口 `resolve_tc_id_format(cfg)`。

**`TC_ID_FORMAT` 之保留值刻意不是格式字串**，而是來源指標
`"<see feature.yaml: write_back.tc_id_format>"`。理由：若保留一份真的
格式字串，痕跡是留下了，但**雙來源也一併留下了** —— 誤用者會靜默產出
看似正常的 tc_id。改為指標後，任何誤用立即失敗（`.format()` 不含 `{n}`
會產出常數字串，而 `resolve` 對此有明確檢查）。

`resolve_tc_id_format` 另加一項本條未要求之檢查：格式**須含 `{n`**。
無序號欄位之格式會使 189 列拿到同一個 tc_id，而 `check_written_back`
（G-TM3）逐列比對預期值時兩側同錯，驗不出來 —— 此為 R-TM21（檢查須能
失敗）之直接應用。

`assert_tc_id_single_source` 為**可獨立呼叫**之守衛（R-TM56）：
一行 `assert_tc_id_single_source(cfg, "<壞值>")` 即可觸發，
紅向 2 即以此構造，不經由 `run()` 之間接路徑。

## R-TM60 — 常數表 v3：刪除三條手動時區/DST 常數

（分析層裁定，2026-08-22。上游包 `docs/handoff/10_constants_v3.md` §1。
發現者為執行層 `09` 上繳 §5.1；分析層回查 CFTS015 原文後確認成立。）

```
R-TM60（分析層裁定，2026-08-22）—— 常數表 v3：刪除三條手動時區/DST 常數

v2 之 SET_TIME_ZONE / DST_ON / DST_OFF **刪除，不改佔位**。

刪除而非佔位之理由：佔位表示「該操作存在但方式未知」，而此三者是
**該操作依 spec 不存在** —— 012 / 013 之能力為自動判定，無使用者介面。
留佔位會使日後讀者以為只差一個 DR 就能填。

替代：012 / 013 之觸發改由位置與時間之改變為之：

    CROSS_TIME_ZONE = 'PENDING: DR-10 使車輛位置跨越時區邊界之操作方式'
    CROSS_DST_BOUNDARY = 'PENDING: DR-10 使車輛時間跨越 DST 切換點之操作方式'

`CROSS_TIME_ZONE` 由 v2 之具體措辭**改為佔位** —— 我在 09 §3.3 保留
具體措辭之理由（「位置設定是 GPS 測試之基本能力」）同樣是未經查證之推測，
與被我自己否決之 `Remove the GPS antenna …` 同型。**同一錯誤我犯了兩次，
第二次還為它寫了一段辯護。**
```

**spec 佐證（分析層回查 CFTS015 原文）**：

| spec | 逐字 |
|---|---|
| 1.3.1.1.5.3 Time Zones（物件 4813992） | `The HU that has a GPS input shall set the time zone **automatically**.` |
| 1.3.1.1.5.4 Daylight Saving Time（物件 4813995） | `The daylight saving time shall be **adjusted automatically**.` |

**執行層回報（2026-08-22）**：已知悉。`tm_constants.py` **仍未建**
（v3 待 Pei 過目），故本條於本包無程式碼落點，其效力現於
`10` T3 之逐片複驗與日後之常數表建檔。

**本條所指之失效形態，執行層記為一條可操作之判準**：凡「設定類功能」之
步驟措辭，落筆前須先查 spec 該能力是**自動**或**由使用者觸發** ——
二者之測試操作完全不同，而「設定類功能通常有 UI 開關」是最容易成立的
常識推論，也是最容易寫出 spec 未述能力（§8.4.2 scope fabrication）之路徑。

## R-TM61 — 搜尋未決項須兼搜識別字與字面量鍵

（分析層自裁，2026-08-22。上游包 `docs/handoff/10_constants_v3.md` §4。
發現者為執行層 `09` 上繳 §2。）

```
R-TM61（分析層自裁，2026-08-22）—— 搜尋未決項須兼搜識別字與字面量鍵

清點某項之使用點時，不得只搜其識別字（常數名、變數名），
須同時搜其**字面量鍵**（字典鍵字串、yaml 鍵名、欄位標題文字）。

理由：同一個值常有兩條存取路徑 —— 具名常數與字典查表，
前者可由識別字搜得，後者只出現為字串。只搜前者會漏掉後者，
而漏掉的那條往往正是實際生效的那條。

依據：09 上繳 §2 —— `TC_ID_FORMAT` 之使用點實為三處，
第三處（run() 之預覽列印）以 `cfg['write_back']['tc_id_format']` 存取，
分析層於 08 §5 之 grep 未命中，致 R-TM59 述為「雙來源」。

本條與 R-TM31（判準須列明細）同族：前者管輸出之可歸屬，
本條管輸入之涵蓋完整。
```

**執行層回報（2026-08-22）**：已套用於本包之全部清點。
`09` §2.1 之三項超出指令之設計決定（來源指標、格式須含 `{n`、
守衛抽為可獨立呼叫）分析層全部採納，無須調整。

## ~~R-TM62 — TLM_MANAGED_TIME_DATE_* 不適用於 Atl-H~~ **已撤回**

> **本條撤回 —— 見 R-TM75(4)。** 五個 `TLM_MANAGED_TIME_DATE_*` 在
> Atlantis 欄（16–20）有值，**適用於 Atl-Mid 之 TC**。撤回之成因為
> 分析層由 spec 檔名之 `Atl-H` 推定範圍（R-TM75 §1.2）。
> 依 R-TM13 加刪除線保留，不刪除。


（Pei 裁定，2026-08-22。上游包 `docs/handoff/12_scope.md` §1。
發現者為分析層 `11` §2.2 之 LID 表探測。）

```
R-TM62（Pei, 2026-08-22）—— TLM_MANAGED_TIME_DATE_* 不適用於 Atl-H

LID 表 `CAN Mapping` 分頁中，五個 `TLM_MANAGED_TIME_DATE_*`
（Hour / Minute / Day / Month / Year）於 Atlantis High 欄（26–30）無值，
僅 Atlantis 欄（16–20）有值。

裁定：該五 LID **視為不適用於 Atl-H**，不寫入本 feature 之任何
訊號斷言，亦不列為 `PENDING`（其非缺件，而是本架構無此對映）。

DR-6b（原擬登記「無 Atl-H 對應者」之缺件）**取消** —— 依本條，
該類非缺件。

**本條之射程限於此五 LID。** 其邏輯是否延伸至 Atl-Mid 專屬之需求物件，
見 A-TM27，待 Pei 另裁。
```

**執行層回報（2026-08-22）**：五 LID 於 `data/lid_atlantis_high.tsv`
記為 `N/A (R-TM62)`（六欄全填該值），與 `(EMPTY)` 在同一檔內可區分。
DR-6b **未建立**，始末記於 `DATA_REQUESTS.md`。

**但實測另發現一個 Atl-H 欄為空、且不在本條射程內者**：`DateTmFormat2`
（Powernet 欄有值 `Radio_A3.DateTmFormat2`，Usage Comment 為 `For PHEV`，
來源列 408）。**執行層未逕行套用本條**（射程擴張屬條文範圍），
於 tsv 記為 `(EMPTY)`。提請裁定 —— 見 `docs/upstream/11_lid.md` §3.2。

## ~~R-TM63 — A-TM27 採選項 (c)：引用標註，不縮減 TC~~ **已撤回**

> **本條撤回 —— 見 R-TM75(1)。** Atl-Mid 物件之引用寫**真值**
> `CFTS015-{objid}`，不寫 `PENDING: DR-11`。
> **其「覆蓋不縮減」之原則本身正確且維持** —— 錯的是處置前提
> （誤認 Atl-Mid 為他架構）。依 R-TM13 加刪除線保留，不刪除。


（Pei 裁定，2026-08-22。上游包 `docs/handoff/13_b1.md` §1。
**B1 之最後一個內容阻塞於此解除。**）

```
R-TM63（Pei, 2026-08-22）—— A-TM27 採選項 (c)：引用標註，不縮減 TC

037 引用之物件若標為 Atlantis Mid 專屬（`[EE Architecture:Atlantis Mid]`
且不含 `Atlantis High`、非 `All`），其處置為：

1. **TC 照寫，覆蓋範圍不縮減。** 該驗證點仍生成 TC —— 037 引用了它，
   即上游 SWE.1 認為其在範圍內；推翻上游之範圍判斷非本層權限
   （§8.2「TC 作者不得重新分解 RD 項目」之同一精神）。

2. **該物件之 specification_reference 條目改為佔位**：
   `PENDING: DR-11 Atl-H 對應需求（CFTS015-{objid} 標為 Atlantis Mid）`
   —— 不寫 `CFTS015-{objid}`（該物件不適用於本架構），
   亦不留空（canon §8.4.3）。

3. **同一 leaf 若另有 Atl-Hi 物件**，該等物件正常寫 `CFTS015-{objid}`；
   佔位與真值並存，佔位不取代真值（同 R-TM41 訂正之形態）。

4. **020 / 021 兩片之全部條目皆為佔位**（Atl-Hi 錨點為零）。
   該二片仍生成 TC，其 spec_reference 全為 `PENDING: DR-11`。

5. **判準之單一來源**：is_atl_hi 之判定取自
   `data/ee_architecture_by_leaf.tsv`（`12` T3 產出），
   context 層與 lint 層共用同一檔，不各自判定（`tm_rulings` 之同一精神）。

**與 R-TM62 之關係**：R-TM62 處理 LID（訊號對映層，判為 N/A 不寫）；
本條處理需求物件（spec 引用層，判為佔位仍寫 TC）。
**兩者處置不同，因其性質不同** —— 前者是「本架構無此訊號」，
後者是「本架構之對應需求未知」。不得互相套用。
```

**執行層回報（2026-08-22）**：`data/ee_architecture_by_leaf.tsv` 已產出
（88 資料列 × 6 欄，22 片逐 leaf 與下放包 `12` §2.1 全符）。
`is_atl_hi` 之判準逐字為「標籤含 `Atlantis High`（不分大小寫）或等於
`All`」，於 context 層與 lint 層**由同一檔供給**（本條第 5 項）。

**A-TM27 之量值經執行層更正**：分母 78 → **88**，比例 45% → **40%**。
**本條所依賴之五項事實（35 Atl-Mid、020/021 零錨點、003 為 1/6、
014 為 1/5、017 為 1/4）全部不受影響** —— 更正只及於總數與百分比。
詳見 `ANOMALIES.md` A-TM27 之量值更正段。

## R-TM64 — spec_reference 只放真值，佔位放 Remarks

（分析層裁定，2026-08-22。上游包 `docs/handoff/14_pilot.md` §1。
發現者為執行層 `13` 上繳 §4 之 lint 四項發現；採其所傾向之 (a)，
並補其自陳之 020/021 空欄缺口。）

```
R-TM64（分析層裁定，2026-08-22）—— spec_reference 只放真值，佔位放 Remarks

specification_reference（工作簿 N 欄）**只放符合 canon §10.7(a) 之真值**，
排列依 §10.7（前綴一次、`, ` 續列、升冪、禁 `;`）。

**佔位一律放 Remarks（AH 欄）**，與 A-TM13 之 DR-5 佔位同處
（G-TM1 項 3 已如此規定）。Remarks 因此成為**全部缺口宣告之單一落點**。

**例外 —— 零真值之片**：若某條 TC 之全部引用物件皆非 Atl-Hi
（020 / 021 兩片），spec_reference 留空即違反 canon §8.4.3。
故該情形下 spec_reference 寫**單一佔位**：

    PENDING: DR-11 Atl-H 對應需求

（不含物件 id —— 逐項明細寫在 Remarks，N 欄只需標明「此欄待補」）

**B7 之判準隨之調整為**：
  (i) 欄值符合 `CFTS015-<7位>(, <7位>)*` 之形式；**或**
  (ii) 欄值恰為 `PENDING: DR-11 Atl-H 對應需求` 單一佔位
二者以外皆報。**分隔符 ` / ` 自此不再使用。**
```

**執行層回報（2026-08-22）**：B1 之四條受影響 TC 已依本條重寫，
lint 之 B7 判準已調整，紅綠俱備。`13` 上繳 §4 所報之 4 項發現隨之清零。

**本條使 Remarks 成為缺口宣告之單一落點**，其副作用須並記：同一條 TC
若既有 A-TM13 缺件（DR-5）又有 Atl-Mid 引用（DR-11），Remarks 會同時
承載兩種佔位。B1 七片無此重疊（002 / 005 不在 B1），**但 B2 含 002 與 005
且其 Atl-Mid 物件分別為 3 與 0**，屆時 002 會是首個重疊樣本。已列入未驗清單。

## R-TM65 — 欄位鍵名統一為 feature.yaml 之宣告

（分析層裁定，2026-08-22。上游包 `docs/handoff/14_pilot.md` §2。
發現者為執行層 `13` 上繳 §5.1；採其所傾向之 `spec_reference`，
並採納其所建議之 write_back 啟動檢查。）

```
R-TM65（分析層裁定，2026-08-22）—— 欄位鍵名統一為 feature.yaml 之宣告

TC JSON 之欄位鍵名以 `feature.yaml` 之 `workbook.columns` 宣告為準。
本 feature 即 `spec_reference`（非 `specification_reference`）。

lint 之 B7 與 arch 閘改讀 `spec_reference`。
**19 條 TC 之 `specification_reference` 鍵移除** —— 兩鍵並存本身即雙來源
（`13` §5.1 自陳為權宜非解法）。

**write_back 增啟動檢查**（執行層 §5.1 之建議，採納）：
`cols` 之每個 key 是否至少在一條 TC 內出現；未出現者報
「該欄將全空寫入」並 raise，不得靜默續行。

canon §10.1 之 `specification_reference` 為**輸出契約之欄名**，
與 TC JSON 之鍵名為兩件事；本條只統一後者。
```

**執行層回報（2026-08-22）**：三處已改（lint 之 B7、lint 之 arch 閘、
19 條 TC 之鍵），`specification_reference` 於 TC JSON 內**零殘留**。
write_back 之啟動檢查已實作並附紅綠。

**啟動檢查之射程須說明**：本檢查為「該 key 是否至少在一條 TC 出現」，
**不是「每條 TC 都有該 key」** —— 後者會誤攔 `remarks`（僅缺口 TC 需要）
與 `tc_id` / `author` / `functional_safety`（由條文決定，本就不從 TC 讀）。
故四個由條文決定之欄與條件性欄位列為豁免，其清單寫在原始碼內並附理由。

## R-TM66 — §4.5 之判準為資料性質，非字串形態

（分析層裁定，2026-08-22。上游包 `docs/handoff/15_b2.md` §1。
發現者為執行層 `14` §2.4 之自陳。）

```
R-TM66（分析層裁定，2026-08-22）—— §4.5 之判準為資料性質，非字串形態

input_test_data 之歸屬依 canon §4.5 之資料性質判定
（環境資料 → Pre-Condition／互動操作 → Procedure／獨立資料集 → 本欄），
**不得以佔位字串之字面形態為篩選依據**。

本 feature 之落實：TC#4 / #5 / #18（GPS 位置，DR-10）與
TC#15 / #16 / #17（訊號注入，DR-20）**六條之 input_test_data 一律改 `NA`**，
該操作寫在 Procedure。

執行層以字串匹配掃出前三條而漏後三條，成因即以字面代替判準
（`14` §2.4 自陳）。**同型風險**：日後新增之 DR 號若字串不同，
同一問題會再度漏掃。
```

**執行層回報（2026-08-22）**：六條已改，lint 歸零。
**同型風險已自動化**（`15` T3 之 §4.5 閘）：判準改為「`input_test_data`
之任一行與 `test_procedure` 之任一行逐字相同即報」——**不再依賴任何
特定字串**，故新增之 DR 號不會使其失效。

## R-TM67 — 紅向須先證明壞值確實壞

（分析層自裁，2026-08-22。上游包 `docs/handoff/15_b2.md` §3。
發現者為執行層 `14` §3.2 之自陳，該處已自行提請立為條文。）

```
R-TM67（分析層自裁，2026-08-22）—— 紅向須先證明壞值確實壞

self-test 之紅向須於斷言守衛反應之前，先以一行複驗**證明所構造之輸入
確實違反該守衛所檢查之條件**（如「改名後之 TC 含舊鍵者 0 條」）。

理由：紅向未觸發時，「守衛失效」與「壞值不壞」在現象上完全相同，
而後者會使一個實際無效之守衛被記為已驗。

依據：13 §1.3（用了不存在之物件 id）、14 §3.2（`{**r}` 先展開致新舊鍵
並存）—— 兩次皆為構造錯誤，兩次皆一度被讀為守衛問題。

本條與 R-TM42（受測物須有鑑別力）同族：前者管受測物，本條管壞值。
```

**執行層回報（2026-08-22）**：本包新增之兩閘，其紅向皆附構造複驗
（見 `docs/upstream/15_b2.md` §3）。**既有之 42 項自驗尚未回溯補做** ——
逐項補做屬可觀工作量且非本包指派，列入未驗清單 A 區。

## R-TM68 — Remarks 內多種佔位之排列

（分析層裁定，2026-08-22。上游包 `docs/handoff/15_b2.md` §4。
發現者為執行層 `14` A4。）

```
R-TM68（分析層裁定，2026-08-22）—— Remarks 內多種佔位之排列

Remarks 為缺口宣告之單一落點（R-TM64）。一條 TC 若有多個佔位：

1. **一佔位一行**，不合併
2. **依 DR 號數值升冪**（DR-5 在 DR-11 之前）
3. 每行格式不變：`PENDING: DR-{n} {缺件描述}`
4. **不加小計、不加前言** —— Remarks 只承載逐列事實（R-TM47）

B2 之 002 將同時承載 DR-5（CFTS015 缺件物件）與 DR-11（Atl-Mid 引用），
依本條排列。lint 增一項：Remarks 之佔位行若非升冪即報。
```

**執行層回報（2026-08-22）**：已實作並附紅綠。**升冪須以數值比較，
非字串比較** —— `DR-11` 之字串序在 `DR-5` 之前（`1` < `5`），
若以字串排序，一個已經正確升冪的 Remarks 會被判為錯。此點已寫入註解。

## R-TM69 — 佔位之閘門須驗特定 DR 號，並增齊全性閘

（分析層裁定，2026-08-22。上游包 `docs/handoff/16_b3.md` §1。
發現者為執行層 `15` §5.2。）

```
R-TM69（分析層裁定，2026-08-22）—— 佔位之閘門須驗特定 DR 號，並增齊全性閘

1. **B3（lint_spec_gap）之判準改為**：該 leaf 若在 `SPEC_GAP` 內，
   其 Remarks 須含 `PENDING: DR-{該 leaf 之特定 DR 號}`
   （002 / 005 為 DR-5），**非「含任一 PENDING: DR-」**。

2. **新增齊全性閘 `lint_placeholder_completeness`**：
   逐 TC 比對「應有之佔位集合」與「Remarks 實有之佔位集合」——
   應有集合由 context 之 `arch.placeholders` + `SPEC_GAP` 推得，
   兩集合不等即報，**缺與多皆報**。

   理由：R-TM68 只驗排列、B3 只驗特定號之存在，
   **「該有的都有沒有」在本包之前無任何閘門負責**（執行層 §5.2 自陳）。

3. **一般化**：條文變更若改變某欄位之語意（如「Remarks 承載什麼」），
   **須逐一檢查以該欄位為判準之既有閘門**。R-TM64 未做此檢查，
   致 B3 靜默失效兩輪。

   本條與 R-TM61（搜尋須兼搜字面量）同族：前者管找得全，
   本條管改得全。
```

**執行層回報（2026-08-22）**：兩項已實作，紅綠俱備。
第 1 項對 B2 重跑後**抓到 002 之兩條**（TC#2 與 TC#3），停止條件未觸發。

**第 2 項之「應有集合」有一項條文未言明之裁量，執行層採 leaf 全集**：
`arch.placeholders` 為該 **leaf** 之全部 Atl-Mid 物件，非「該 TC 所涉」。
**「該 TC 所涉」無法實作** —— `spec_reference` 只含真值（Atl-Hi），
Atl-Mid 物件不在其中，無從推出該 TC 涉及哪些。

**此判準使 B1/B2 產生 32 項發現，其中僅 1 項為真遺漏**
（001 之 4814069 從未被任何 TC 宣告）。以「leaf 聯集」為判準則精確抓出
該 1 項而無其餘 31 項。詳見 `docs/upstream/16_b3.md` §2，提請裁定。

## R-TM70 — §8.2.1 界線不及於 verbatim 上半

（分析層裁定，2026-08-22。上游包 `docs/handoff/16_b3.md` §2。
發現者為執行層 `15` §5.3。）

```
R-TM70（分析層裁定，2026-08-22）—— §8.2.1 界線不及於 verbatim 上半

§8.2.1 之相鄰組界線拘束的是**作者所撰之內容**（test_item 下半、
pre_conditions、input_test_data、test_procedure、expected_result），
**不及於 test_item 上半之 verbatim 需求原文**。

理由：上半為逐字照錄之上游文字（canon §4.3.1，來源限
`leaf_descriptions.txt`），作者無權改寫。若界線及於上半，
唯一的遵守方式就是改寫需求原文 —— **那正是 §4.3.1 所禁**。
兩條規則不可能同時要求「照錄」與「不得出現某詞」。

先例同源：既有之「verbatim 上半豁免於作者品質檢查」為同一原理，
本條為其在 §8.2.1 上之延伸。

**lint 之 B4（界線閘）隨之調整**：掃描範圍排除 `test_item` 之上半
（第一段），只掃下半括號與其餘內容欄。
**reasoning 亦排除** —— 執行層 §5.3 之自我更正已證：掃 reasoning 會把
「本條不涵蓋 SNA」這句聲明本身當成違規。
```

**執行層回報（2026-08-22）**：`lint_boundary` 之掃描範圍已改，
紅綠雙向已證（同一訊號置於上半豁免、置於下半仍報）。

**「掃 reasoning 會把聲明本身當成違規」已第三次出現**：
`15` §5.3（SNA）、本包 B-2 之複驗、本包 B-5 之複驗（017 之
`TLM_MANAGED_*`）。**三次皆為執行層自寫之臨時判準**，而非 lint ——
lint 自 R-TM70 起已排除 reasoning。**臨時判準無條文拘束，是同型錯誤
反覆之處**，列入未驗清單。

## R-TM71 — R-TM67 之適用範圍

（分析層自裁，2026-08-22。上游包 `docs/handoff/16_b3.md` §4。
發現者為執行層 `15` A3。）

```
R-TM71（分析層自裁，2026-08-22）—— R-TM67 之適用範圍

構造複驗（R-TM67）適用於：
  (a) 本條立訂後**新增**之紅向；
  (b) 既有紅向中**曾經出現過構造錯誤者**（13 §1.3、14 §3.2 二處）。

**既有 42 項不回溯補做。** 理由：回溯之成本與其發現機率不成比例 ——
該 42 項皆已通過紅綠雙向且多數經多輪重跑；而構造錯誤之特徵是
「紅向不觸發」，該 42 項若有此問題，早已在歷次重跑中顯示為失敗。

**但若某既有紅向日後出現不觸發**，須先依 R-TM67 複驗構造，
不得逕判為守衛失效。
```

**執行層回報（2026-08-22）**：已知悉。本包新增之 7 項紅向皆附構造複驗。

## R-TM72 — 齊全性閘改以 leaf 為單位

（分析層裁定，2026-08-22。上游包 `docs/handoff/17_b4.md` §1。
發現者為執行層 `16` §2。）

```
R-TM72（分析層裁定，2026-08-22）—— 齊全性閘改以 leaf 為單位

R-TM69(2) 之 `lint_placeholder_completeness` 判準由「逐 TC 比對該 leaf
全集」改為 **「以 leaf 為單位取聯集比對」**：

  該 leaf 之全部 TC 之 Remarks 佔位聯集，須等於該 leaf 應有之佔位集合。
  缺與多皆報，**報在 leaf 層而非逐 TC**。

理由三點：
1. **缺口是 leaf 層級之事實** —— 「該需求在 Atl-H 無對應」與哪一條 TC
   驗證它無關。逐 TC 重複列出，Remarks 膨脹而不帶新資訊。
2. **判準 (b)（逐 TC 比對該 TC 所涉）不可實作** —— `spec_reference`
   只含真值，無從推出該 TC 涉及哪些 Atl-Mid 物件（執行層 §2.1 已證）。
3. **鑑別力**：(a) 32 項中 31 項為形式不符，雜訊率 97%，
   真遺漏被淹沒；(c) 恰好 1 項且即為該真遺漏。

**可讀性之保證**：同一 leaf 之 TC 於工作簿中相鄰（tc_id 依序），
故讀者掃該 leaf 之數列即見全部佔位，不因分散而漏看。

**B1/B2 之 32 項發現隨本條歸零**（判準 (c) 下已齊全，執行層 §7 實測）。
001 之 4814069 已補，該補正確且應保留。
```

**執行層回報（2026-08-22）**：已改，三檔重跑後 `placeholder-completeness`
歸零（以 `grep` 取全部命中判定，非 `tail`）。

**本閘之報點隨判準改變而移動**：由「逐 TC」改為「逐 leaf」後，
訊息不再繫於某一條 TC，故 `where` 改為該 leaf 之識別。
**其副作用須並記**：一個 leaf 若跨批次生成（本 feature 無此情形，
Part VII 之批次計畫使每片只屬一批），聯集會跨檔而本閘只看單檔 ——
**現行實作為單檔內聯集**，此限制已寫入 docstring。

## R-TM73 — 自檢之臨時判準須與對應 lint 閘同範圍

（分析層自裁，2026-08-22。上游包 `docs/handoff/17_b4.md` §2。
發現者為執行層 `16` §4 之三次同型誤判自陳。）

```
R-TM73（分析層自裁，2026-08-22）—— 自檢之臨時判準須與對應 lint 閘同範圍

執行層為自檢而臨時撰寫之掃描判準，其**掃描範圍須與 lint 中對應閘門
一致**。lint 已排除者（`reasoning`、`test_item` 上半 —— R-TM70），
臨時判準亦須排除。

理由：三次同型誤判（掃 reasoning 而把「本條不涵蓋 X」之聲明本身
當成違規）皆發生於臨時判準，而非 lint —— **lint 受條文拘束並經紅綠雙向，
臨時判準兩者皆無。**

**最低要求**：臨時判準之掃描範圍須在該次回報中明列
（掃哪些欄、排除哪些），使誤判之成因可被對造判讀，
而非只在「覺得不對再查一次」時偶然發現。

依據：15 §5.3、16 §4 之三次同型誤判。
```

**執行層回報（2026-08-22）**：已套用於本包之 B4 自檢，
掃描範圍逐項明列於 `docs/upstream/17_b4.md` §3.2。

**一項本條未涵蓋而執行層自加者**：臨時判準之**欄位清單改由一個具名常數
供給**，與 lint 之 `lint_boundary` 讀同一份 —— 使「同範圍」不靠人記得，
而是取自同一處。條文只要求「一致」，未要求「同源」；
**一致靠人維持會漂移**，這是本 feature 一路在記的形態。

## R-TM74 — 上繳須含逐 T 項對照表

（分析層自裁，2026-08-22。上游包 `docs/handoff/17_b4.md` §3。
發現者為執行層 `16` §6.1 之 T1 漏做自陳。）

```
R-TM74（分析層自裁，2026-08-22）—— 上繳須含逐 T 項對照表

上繳包之 §0 須列**下放包之全部 T 項編號**，逐項標
「完成／未做／不適用」，未做者附理由。

不得只列已做者 —— 只列已做者時，漏做之項不會出現在表上，
而讀者無從察覺其缺席（**缺席不是可見的狀態**）。

依據：16 §6.1 —— T1 被跳過，靠 R-TM46 之增量檢查間接抓到；
若該包無條文新增，增量為 0，該漏做不會現形。
```

**併入本條之作業紀律（分析層 §3 末段）**：判定「有沒有抓到」之停止條件
時，不得用截斷過的輸出（`tail`）；改以 `grep <類別>` 取該類全部命中再判。

**執行層回報（2026-08-22）**：已套用。本包之 §0 逐 T 對照表列
T1–T4 全部四項。

## R-TM75 — 本 feature 涵蓋 Atl-Hi 與 Atl-Mid 兩架構

（分析層裁定，2026-08-22。上游包 `docs/handoff/18_arch.md` §2。
**撤回 R-TM62 / R-TM63，取消 DR-11，作廢 A-TM27 之結論。**）

```
R-TM75（分析層裁定，2026-08-22）—— 本 feature 涵蓋 Atl-Hi 與 Atl-Mid 兩架構

依 §1 之實測：037 引用之 35 個 Atl-Mid 專屬物件，其 Radio 標籤
35/35 含 R1L / R1L-R（即本專案），ECU 標籤 35/35 為 LTM。
036 母本之七個車型欄中五欄為 Atl-Mi。

**本 feature 之驗證範圍涵蓋 Atlantis High 與 Atlantis Mid 兩種
EE architecture**，以 Radio 維度（R1L / R1L-R）為專案界線。

隨之撤回／更正：

(1) **R-TM63 撤回。** Atl-Mid 物件之引用寫**真值** `CFTS015-{objid}`，
    不寫 `PENDING: DR-11`。R-TM63 之「覆蓋不縮減」原則本身正確且維持
    —— 錯的是其處置前提。

(2) **DR-11 取消。** 其所登記之缺件（Atl-H 對應需求）不存在 ——
    那些需求本就是本專案的。約 40 處佔位改為真值。

(3) **A-TM27 之結論作廢，事實記載保留。** 「35 個物件標為 Atl-Mid」
    為真；「架構不符」為偽。依 R-TM13 加註不刪。

(4) **R-TM62 撤回。** 五個 `TLM_MANAGED_TIME_DATE_*` LID 在 Atlantis 欄
    有值，**適用於 Atl-Mid 之 TC**。017 / 020 之相關斷言得寫。

(5) **A-TM26 修正**：架構欄之選取**依該條 TC 之目標架構**而定 ——
    Atl-Hi 之 TC 取欄 26–30、Atl-Mid 之 TC 取欄 16–20。
    **強制記錄之要求不變且更形重要**：須記錄取自哪一欄，
    因現在兩欄都可能是對的，取錯更難察覺。
```

**執行層回報（2026-08-22）**：五項全部落實，工具三處連動已改，
B1–B4 四批全部重生成。`PENDING: DR-11` 於生成物中**零殘留**。

**執行層對本條成因之一項補充**：分析層自陳「以檔名代替內容」，
而執行層在 `11`–`17` 之九輪中**逐輪使用 `Atlantis High (col 26-30)`
並將其寫入每一條 TC 之 reasoning**，卻從未質疑該前提 ——
A-TM26 之強制記錄使「取自哪一欄」可追，**但可追不等於正確**：
它記錄的是我方選了哪一欄，不是那一欄是否該選。
**該判準之射程限制先前已寫入 docstring**（`14` §1.2），
本次即為該限制之實例化。

## R-TM76 — 架構限定之 Pre-Condition 措辭

（分析層裁定，2026-08-22。上游包 `docs/handoff/18_arch.md` §3，
依 Pei 2026-08-22 之指示。）

```
R-TM76（分析層裁定，2026-08-22）—— 架構限定之 Pre-Condition 措辭

某條 TC 若只適用於單一 EE architecture，其 Pre-Condition 加一行：

    The vehicle is an Atlantis High architecture variant
    The vehicle is an Atlantis Mid architecture variant

**取值來源**：CFTS015 物件之 `[EE Architecture:...]` 標籤值逐字
（`Atlantis High` / `Atlantis Mid`），非自擬簡稱（不寫 `Atl-Hi` / `High only`）。

**加與不加之判準**：
- 該 TC 之全部引用物件皆為單一架構 → **加**該架構之限定行
- 引用物件跨兩架構 → **不加**（該行為適用於兩者之共通行為）
- 引用物件標為 `All` → 不加

canon §4.4 之允許類型含「system version / mode」（如 `Dev / Pre-Prod
build only`），架構變體屬同類，為合法之 Pre-Condition。

**置於 Pre-Condition 之首行**，使審閱者一眼見其適用範圍。
```

**執行層回報（2026-08-22）**：已實作為 context 之 `arch.precondition`，
並由 `lint_arch_column` 驗其與所取架構欄一致。

## R-TM77 — T–Z 車型欄留空

（分析層裁定，2026-08-22。上游包 `docs/handoff/18_arch.md` §4。）

```
R-TM77（分析層裁定，2026-08-22）—— T–Z 車型欄留空

`feature.yaml` 之 T–Z 七欄由 `TODO(R-TM10-A1)` 改為
`BLANK_BY_DECISION`，理由：交付件 UserProfiles_20260820 之該七欄
189/189 全空，**車型欄在既有交付實務中不作為範圍標示之用**。

範圍標示改由 Pre-Condition 承載（R-TM76）。

**此項自 `04` 起掛在 `TODO(R-TM10-A1)` 下未裁，而它正是會逼分析層
去看架構的那一步** —— 我未將其視為阻塞項，反而繞過它推定架構。
記於此，因該疏漏是 §1.2 之錯誤能存活四輪的原因之一。
```

**執行層回報（2026-08-22）**：`write_back.BLANK_BY_DECISION` 之
T–Z 項已由 `TODO(R-TM10-A1) —— 待本 feature 條文` 改為本條之理由。

## R-TM78 — dry-run 為寫回之必要前置

（分析層裁定，2026-08-22。上游包 `docs/handoff/21_writeback.md` §1。
發現者為執行層 `20` §6.1 之 dry-run。）

```
R-TM78（分析層裁定，2026-08-22）—— dry-run 為寫回之必要前置

`write_back` 之 `--write` 前必跑一次不帶 `--write` 之 dry-run，
並**逐項核對其輸出**：`rows` 數、`skipped` 清單、`tc_id` 區間、
`columns` 對映、`unresolved` 是否為空。

不得視為選用之檢查。依據：20 §6.1 —— 首次 dry-run 顯示 114 列而應為 57，
成因為軌跡備份進入 glob；該備份係依下放包指令刻意建立，
而指令未提示其會進入寫回路徑。**建立產物之指令與消費產物之路徑
分屬兩包，無人負責其交集。**

**dry-run 之核對須逐項寫入上繳**，不得只寫「dry-run 通過」——
本次若只看「無錯誤訊息」，114 這個數字不會被注意到。
```

**執行層回報（2026-08-22）**：已套用，本包 §5 逐項核對五個欄位。

**一項本條未涵蓋者**：dry-run 能核對之項目，限於 `run()` 所列印者。
`rows` 之所以能被發現，是因為它恰好被印出來；**若某項不在列印清單內，
逐項核對也核不到它**。現行列印涵蓋來源檔 SHA、分頁、表頭列、欄位對映、
列數、skipped、tc_id 區間、test_group、BLANK_BY_DECISION、unresolved
——**未涵蓋者包括「每欄實際將寫入之值」**。列入未驗清單。

## R-TM79 — 條數檢查須兼計撤回條

（分析層自裁，2026-08-22。上游包 `docs/handoff/21_writeback.md` §3。
發現者為執行層 `20` §0。）

```
R-TM79（分析層自裁，2026-08-22）—— 條數檢查須兼計撤回條

R-TM46 之增量檢查，其計數樣式須兼計刪除線標題：

    grep -cE '^## (~~)?R-TM'

理由：R-TM13 要求撤回條加刪除線保留，而刪除線改變了標題之字面，
使其脫離既有計數樣式。**兩條規則各自正確，其交互作用使計數失準** ——
與 R-TM69(3)（條文變更須檢查以該欄位為判準之既有閘門）同族。

上繳須同時回報兩個數（含撤回、不含撤回），使差額可見。
```

**執行層回報（2026-08-22）**：已套用。本包起上繳之增量欄一律回報兩個數。


## R-TM80 — 寫回指令一律帶 `--out`

（分析層裁定，2026-08-22。上游包 `docs/handoff/25_closure.md` §1。
發現者為執行層 `24` §2 —— 依 `24` T2 之指令執行，輸出落入 `inputs/`。）

```
R-TM80（分析層裁定，2026-08-22）—— 寫回指令一律帶 --out

下放包之 `write_back.py --write` 指令**一律明寫 `--out`**，
指向 `features/<feature>/output/`。不得依賴腳本預設。

理由：`write_back.py:452` 之預設為來源檔同目錄（`inputs/`），
與「輸出落 output/」之慣例相反。**預設值與慣例相衝時，
沉默地依賴預設即等於指令與要求不一致。**

腳本預設之修改（改為 `feature-dir/output/`）**跨 feature，Tier 2**，
本條不逕改，登記為 A-TM29。
```

**執行層回報（2026-08-22）**：已落檔。`24` 之寫回已以 `--out` 重跑至
`output/`，誤落 `inputs/` 之檔已刪（兩次 SHA256 相同，內容無異）。
本條自 A-TM29 修畢前為唯一迴避手段，下次寫回時適用。


## R-TM81 — 本 feature 之 Clock 設定狀態不得寫於 Pre-Condition

（分析層裁定，2026-08-25，依 Pei 同日指示。上游包
`docs/handoff/26_pei_review_remediation.md` §2。發現者為 Pei 之交付後
審查第 (1) 項：「Setting 操作應放步驟並給入口路徑」。）

```
R-TM81（分析層裁定，2026-08-25，依 Pei 同日指示）

本 feature 之 Clock 設定項狀態（Sync Time with GPS、Time Format 等
§7 Clock 節項目）不得寫於 Pre-Condition；一律以 Procedure 步驟建立，
入口固定

    1. Open the "Clock" settings
    2. Set "<項名>" to <值>

項名逐字取 HMI Settings List R1L-R (Feb 13 2026) §7。

理由：Clock 設定即本 feature 之受測物，寫入 J 欄同時觸犯 canon §4.4
之「feature under test as premise」與「step-controlled state」兩禁，
且前提式寫法無從承載入口路徑，執行者不知從何按起。

Proxi 配置行不在射程 —— 車輛配置屬外部環境，為合法 PC，
僅記法正規化為 canon §8.7.5(c)。

頁名沿用既有常數字面 "Clock"（DR-12b 之佔位語意不變，A-TM28 未裁前照留）。
```

**執行層回報（2026-08-25）**：已套用。37 條之 Clock 設定狀態全數遷入
Procedure（14 條補入口、23 條併入既有入口步），J 欄殘留 0 行。
清單原記 35 條，執行層反驗為 37 條（漏列 #041 #042），見
`docs/handoff/26_pei_review_remediation.md` §6 C3。#041 #042 含次序約束
（設定須先於 sleep），依 Pei 2026-08-25 之 Q1(a) 裁定成四步式。
Proxi 行之正規化對象為 5 條（原記 4 條，漏 #021），見同文 §6 C4。
回繳見 `docs/handoff/27_wtm26_return.md`。


## R-TM82 — §8.7.5 之適用版本隨 repo canon 現行版

（分析層裁定，2026-08-25。上游包
`docs/handoff/26_pei_review_remediation.md` §2。發現者為 Pei 之交付後
審查第 (2) 項所連帶之逐列稽核 —— D4：22 條 29 處仍為已撤銷之 v1 三件組。）

```
R-TM82（分析層裁定，2026-08-25）

§8.7.5 於本 feature 之適用版本隨 repo canon 現行版（v3）。

R-TM48 之引用為**動態引用** —— charter 明訂 repo 版為權威且持續演進，
故該條之生效客體是 §8.7.5 本身，而非其 2026-08-21 前之文字。canon 已於
2026-08-21 撤銷 v1/v2 改行 v3，且 `docs/runtime/profiles/` 無
TimeManagement profile、無 cited override，依 FO §0 本 feature 從現行 v3。

R-TM49 之 segment 缺件處理隨 v3 失所附麗（v3 不寫網段，segment 缺件
不復存在），條文保留為軌跡不刪（R-TM13）。DR-6 佔位依
`26_pei_review_remediation.md` D4 處置：#035 之佔位隨 v3 消滅，
DATA_REQUESTS #6 降轉為「僅供追溯，不再阻塞」，加註不刪列。
```

**執行層回報（2026-08-25）**：已套用。22 條 29 處 v1 三件組全數改為 v3，
網段字樣殘留 0。#035 之 `PENDING: DR-6` 佔位隨 v3 消滅，`DATA_REQUESTS.md`
已加註降轉為僅供追溯、不刪列。

**連帶發現一項閘門失效（R-TM69(3)）**：lint 之 `arch-column` 檢查以 LID
別名為「本條是否談及訊號」之偵測判準，v3 改寫後別名消失，該閘門覆蓋
由 11 條掉到 0 條而不報錯 —— 改寫後第一次 lint 之「0 項」有一部分是
閘門失效而非真的乾淨。判準已擴充為「LID 別名 ∪ 兩架構訊號全名」，
覆蓋還原為同一組 11 條。回繳見 `docs/handoff/27_wtm26_return.md` §3。


## R-TM84 — test_item 下半之格式定式

（Pei, 2026-08-25。上游包 `docs/handoff/28_wtm26a1_testitem.md` §2。
發現者為 Pei 之 0825 件審查 P1／P2。）

```
R-TM84（Pei, 2026-08-25）—— test_item 下半之格式定式

test_item 之括號下半（R-S4）：
  1. 與 verbatim 上半之間以空行分隔（連續兩個換行 `\n\n(`）
  2. 括號內首字母大寫（`(Confirm …)`）

基準：UserProfiles 0824 交付本之 189/189 既有形態
（`…\n\n(Verifies that …`）。canon §4.3.1 之「獨立成行」自此
於本 feature 讀為「空行分隔」。sibling 區分 token 之既有內容不動，
只改分隔與首字母。
```

**執行層回報（2026-08-25）**：已套用，59/59。原形態齊一為單換行＋
小寫（`\n(confirm …`），改為 `\n\n(Confirm …`；括號內其餘內容逐字未動
（僅首字母大寫化，長度差恰為每條 +1 字元之換行）。殘留單換行括號 0。
本項為 B1 生成樣式，0822 交付件同樣如此，非 W-TM-26 引入。


## R-TM85 — TC ID family 與 Test Group 回改定案

（Pei, 2026-08-25。上游包 `docs/handoff/28_wtm26a1_testitem.md` §7。
發現者為分析層對 `27` §C1 之覆核 —— 兩個 0822 為不同檔案，A-TM31。）

```
R-TM85（Pei, 2026-08-25）—— TC ID family 與 Test Group 回改定案

F 欄 TC ID family 回改 NR1L-TimeManagement-NNN（NNN 不變），
G 欄 Test Group 回改 Time Management —— 與已送審之 ASW-R2 交付件
（SHA `088a4476…`）一致。R-TM2 之 [PROVISIONAL] 就此定案：
test_group = "Time Management"、非 canon §4.1.1 之 spec 標題預設
（"Time and Date"），Pei 明裁優先。feature.yaml 若已被改為
"Time and Date" 一併回改並移除 [PROVISIONAL] 註記。
A-TM31 之未經裁定改名，處置即本條之回改；日後 identifier 欄之
任何變更依 R-G19-4 先裁後動。
```

**執行層回報（2026-08-25）**：已套用。F 欄 59 列
`NR1L-TimeAndDate-NNN` → `NR1L-TimeManagement-NNN`（序號 001–059 不變、
連續性已驗）；G 欄 59 列 → `Time Management`。`feature.yaml` 之
`test_group` 與 `write_back.tc_id_format` 一併回改（單一來源，R-TM59），
`generated/*.json` 之 per-TC `test_group` 59 筆同步。全欄逐列 diff：
F/G/I 各 59 處，**其餘欄全分頁零變更**（R-G19-4 驗收判準）。


## R-TM86 — VES 供電行 KEEP

（Pei, 2026-08-25。上游包 `docs/handoff/28_wtm26a1_testitem.md` §7。
發現者為執行層 `27` §2 之借調判斷上呈。）

```
R-TM86（Pei, 2026-08-25）—— VES 供電行 KEEP

`The VES screens are powered on`（5 行，#009 #015 #016 #017 #043）
維持 KEEP —— 執行層 27 §2 之借調判斷（VES 獨立供電，非點火 ON
所蘊含）獲 Pei 追認，非 §4.4 system default。
```

**執行層回報（2026-08-25）**：無須改動 —— W-TM-26 已按 KEEP 處置，
Pei 追認即定案。該 5 行現以編號形態留於 J 欄。
