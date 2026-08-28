# 上繳包 15 —— 三重閉合驗證、framework 全定稿、Phase 4 前置盤點

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/16_layer2_final.md`
  （SHA256 `08649b736cb05c07ba5c06a3447f1fce6bb3c938e9176a0aa34c14a2a5fd61ef`，203 行）
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜新腳本：`scripts/layer2_close.py`

## 本輪四個主結果

1. **三重閉合全部通過** —— 21 組之列數 311/311、群數 45/45、
   列 id 聯集 311/311 且**相交組對 0**。§4.1 所宣告之 21 個列數與實測**逐格相符**。
2. **§七.6 之答案是「有，且可精確指出」**：`309` 群內有 **7 個孤島列**
   （其組別與前後鄰居皆不同），全部落在 `338–339` 與 `357–361` 兩段。
   後者**逐列交替**（356 SM／357 IH／358 SR／359 SM／360 IH／361 SM）——
   **這是標題選詞而非能力叢集之特徵**。詳見 §6.1。
3. **下放包 §五 之「有 GT 支持者 9 組」與其自身之表不符** —— 逐列數為 **8** 組
   （`TBM Reflash` 標題重疊、`USB Update` 推定，二者非 GT）。`framework.md` 採 8。
4. **T29d 之「寫回變體丙″」在本 feature 不適用** —— 丙″ 為 vehicle_category
   之 openpyxl 變體，而 **R-SU2 已裁本 feature 一律採 XML 外科式**，
   且 vehicle_category 下放包 36 §一自身亦已將出貨版改為外科式。
   本 feature 真正缺的是**外科式寫回腳本尚未建**。詳見 §5.4。

---

## 1. T29c —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU10 v2 | 653 | **OK** | `544f1d1eb4d5` |
| R-SU19 | 441 | **OK** | `04ba8a302cea` |

二條逐字 append，**既有 29 個條文區塊未受影響** ✅（現 31 塊）。
索引表現行 **19 條**（R-SU10→**v2**、新增 **R-SU19**）；
留存不得引用者 **12 條**（新增 `R-SU10`(v1)）。與下放包 16 §六 T29c 所定之數一致。

`PLAYBOOK.md` §7 追加 **(13)**「0 列物件是閉合檢查之系統性盲區」，
並補其一般形式：**檢查式與被檢物之度量單位不同**時即產生此類盲區；
作法為「至少查兩個單位（量與種類），更嚴者加 id 集合之不相交」。

---

## 2. T29a —— 三重閉合之驗證（本輪核心）

> 依 R-SU10 v2：(i) 列數、(ii) 群數、(iii) 列 id 集合，**三者缺一不可**。

### (i) 列數閉合

| # | Test Set | 所轄 (Heading id, 列區間) | 列數 | 下放包 16 §4.1 | |
|---:|---|---|---:|---:|:--:|
| 1 | `Wi-Fi Download` | 038、055、058 | **29** | 29 | ✅ |
| 2 | `Update Policy` | 009、024 | **17** | 17 | ✅ |
| 3 | `Silent Update` | 178、`175`–`177` | **9** | 9 | ✅ |
| 4 | `Deployment Flow` | 137 | **26** | 26 | ✅ |
| 5 | `Session Flows` | 016、017、018、168、185、188、271、278、287 | **16** | 16 | ✅ |
| 6 | `Client Architecture` | 072、073、192、200、202、251、259、263、266、280、285 | **35** | 35 | ✅ |
| 7 | `Bearer Selection` | 291 | **16** | 16 | ✅ |
| 8 | `ROV Installation` | 085、086、091、096 | **20** | 20 | ✅ |
| 9 | `TBM Reflash` | 110 | **14** | 14 | ✅ |
| 10 | `HU FOTA via TBM` | 214 | **36** | 36 | ✅ |
| 11 | `USB Update` | 020、074、076、078 | **5** | 5 | ✅ |
| 12 | `Update HMI` | 129 | **6** | 6 | ✅ |
| 13 | `Configurable Parameters` | 125、127 | **2** | 2 | ✅ |
| 14 | `FOTA Overview` | 001 | **6** | 6 | ✅ |
| 15 | `Integrity Verification` | 022、`171`–`174`、`310`–`312`、`338` | **8** | 8 | ✅ |
| 16 | `Interruption Handling` | `313`、`315`–`329`、`357`、`360` | **18** | 18 | ✅ |
| 17 | `Status Reporting` | `330`–`334`、`339`、`358` | **7** | 7 | ✅ |
| 18 | `Deployment Conditions` | `336`–`337`、`340`–`341`、`343`–`346` | **8** | 8 | ✅ |
| 19 | `Session Management` | `347`–`356`、`359`、`361`、`368`–`369` | **14** | 14 | ✅ |
| 20 | `Telematics Client` | `363`–`367` | **5** | 5 | ✅ |
| 21 | `Update Agent` | `370`–`383` | **14** | 14 | ✅ |
| | **合計** | | **311** | 311 | ✅ |

### (ii) 群數閉合

- 21 組所涵蓋之 Heading id 聯集：**45**（應 45） —— ✅
- 45 群中未被任何組涵蓋者：**0** ✅
- 組中出現而不存在於 45 群者：**0** ✅

### (iii) 列 id 集合閉合

- 聯集大小：**311**（應 311） —— ✅
- 母體有而 Layer 2 無（漏）：**0** ✅
- Layer 2 有而母體無（溢）：**0** ✅
- 相交之組對：**0** ✅

### 跨章群之內部分割（R-SU10 v2(a)）

| Heading 群 | 列數 | 分屬之 Test Set | 組數 | 各組列數和 | |
|---|---:|---|---:|---:|:--:|
| `SWE1-FOTA-309` | 70 | `Integrity Verification`(4)、`Interruption Handling`(18)、`Status Reporting`(7)、`Deployment Conditions`(8)、`Session Management`(14)、`Telematics Client`(5)、`Update Agent`(14) | 7 | **70** | ✅ |
| `SWE1-FOTA-170` | 7 | `Silent Update`(3)、`Integrity Verification`(4) | 2 | **7** | ✅ |

---

**三重閉合結果：全部通過 ✅**

### 2.1 驗證之實作與其自停

`scripts/layer2_close.py`：21 組以 **Heading id（整群）或 037 列區間**
宣告，由程式解析為列 id 集合後再驗，**不以人手抄錄之列數為輸入**
—— 故 §4.1 所宣告之 21 個列數是被**獨立重算並比對**的，不是被複製的。
任一項不符即 `sys.exit`（沿 `anchor_table.py` 之自檢慣例）。

**下放包 §4.1 之 21 個宣告列數與實測逐格相符**（表中「下放包 16 §4.1」欄），
含跨章群之七段切分（4/18/7/8/14/5/14 = 70）與 `170` 之二段（3/4 = 7）。

---

## 3. T29b —— `framework.md` 改版

已改版（204 行）。變更：

| 項 | 前（上繳包 14） | 後 |
|---|---|---|
| Layer 2 | 12 組定稿 + PENDING 二群（77 列）+ UNASSIGNED `022` | **21 組全定稿**，PENDING／UNASSIGNED 標記**全部解除** |
| 分群鍵之表示 | Heading id | **(Heading id, 列區間)**（R-SU10 v2(a)(c)） |
| 閉合檢查 | 列數 + 群數（二重） | **三重**（加列 id 集合與不相交） |
| Layer 3 | 空，標 `PROVISIONAL — 待下放包 16` | **寫入 §五之 provisional 表**（10 組有值、11 組 TBD）+ 覆蓋狀態 |
| R-SU19 | — | 新增「套用記錄」節（本輪二處拆分與拆後最大組 36 < 40） |

### 3.1 ⚠ 下放包 §五 之「9 組」與其自身之表不符

下放包 16 §五 之結語稱「有 GT 支持者 **9** 組／21；TBD **11** 組」。
逐列數其表：**10 組有值**，其中標 **GT** 者 **8** 組，
另二組非 GT —— `TBM Reflash`（依據為「標題全詞重疊」）與
`USB Update`（依據為「推定」）。

| 依據 | 組數 |
|---|---:|
| **GT** | **8** |
| 標題全詞重疊 | 1（`TBM Reflash`） |
| 推定 | 1（`USB Update`） |
| TBD | 11 |
| **合計** | **21** ✅ |

10 有值 + 11 TBD = 21，**組數本身閉合**；不符者只有「GT 支持者」之計數
（9 vs 8）。`framework.md` 採 **8** 並於該處加註。

**此為 §7(9)（引用他文之敘述須以本文數字重驗）之又一次觸發** ——
若直接抄「9 組」，該數與同頁之表就會互相矛盾，且矛盾在檔內而非跨檔，
更難被日後查出。

---

## 4. T29d —— Phase 4 前置盤點（只盤點缺項，不裁定）

### 4.1 `design_method` 下拉之實測值清單 —— **已備，9 值**

母本之 R 欄下拉為 **x14 擴充**（R-SU2）。實測 `xl/worksheets/sheet6.xml`：

```
<x14:dataValidation type="list" …><x14:formula1><xm:f>下拉選單!$A$1:$A$9</xm:f>
```

即其值域為 `下拉選單` 分頁之 **A1:A9，共 9 個字串**（與上繳包 01 §之
「design-method 詞彙 9 字串」相符）：

| # | 值（逐字） |
|---:|---|
| 1 | `功能測試 (Functional based ; no specific technique)` |
| 2 | `狀態轉換 (State Transition Testing)` |
| 3 | `決策表 (Decision Table Testing)` |
| 4 | `等價劃分 (Equivalence Partitioning, EP)` |
| 5 | `邊界值分析 (Boundary Value Analysis, BVA)` |
| 6 | `組合測試 (Combinatorial Testing ; Pairwise / t-wise)` |
| 7 | `情境 / 用例 (Scenario / Use Case Testing)` |
| 8 | `負向測試 (Negative / Invalid)` |
| 9 | `基礎故障注入 (Fault Injection Lite)` |

**缺項**：**無**（值清單已備）。
**但待裁者有一**：各 Test Set／各列**採哪一值**之判準未定。
21 組中至少 `Interruption Handling`（負向／故障注入）、
`Deployment Conditions`（決策表／組合）、`Update Policy`（等價劃分）
之選值可能不同 —— **執行層不自行裁定**。

> ⚠ **一處措辭之澄清**：R-SU2 之「R 欄 design_method 下拉為 **x14 擴充**」
> 指 OOXML 之 `x14:dataValidation` 擴充命名空間，**非「14 個值」**。
> `feature.yaml` §workbook 之註解「（x14 下拉，R-SU2）」同義。
> 值為 9 個。此處記明以免日後被讀成數量。

### 4.2 `priority` 之 High/Medium/Low → P0–P3 對應 —— **缺，且為硬缺**

母本 P 欄之**標準 dataValidation** 實測：`P10:Q1411`，值域 `"P0,P1,P2,P3"`。
037 側之 Priority 實測（上繳包 01 §）：

| 037 值 | 列數 |
|---|---:|
| `High` | 271 |
| `Medium` | 34 |
| `Low` | 6 |
| **空白** | **72** |
| （合計 383 個資料列） | |

**缺項二**：
1. `High`／`Medium`／`Low` → `P0`–`P3` 之對應**未裁**（四值對三值，非一對一）
2. **空白 72 列之處置未裁** —— 上繳包 01 已實測「Priority 空白 72 列
   **全部落在 SubCat 空白 73 列之內**」，故其空白疑為同源；
   但工作簿 P 欄有 DV 拘束，**寫入空值是否為 DV 所容許亦未驗**

**執行層不自行裁定**，亦未推測對應表。

### 4.3 `lint.popup_ids` —— **已備，51 個**

`feature.yaml` §lint 之 `popup_ids` 實測 **51 個**，與 T5' 之
「兩源聯集之已查得者 51」相符。`PU971`（PDF p.46）依 A-SU3 排除，
**未代以語意相近之 `PU0971`**（`PU0971` 為另一獨立查得之 id，二者不混）。

**缺項**：**無**。
**待確認一**：A-SU3 之 `PU971` 為 RESOLVED（判讀問題非缺件），
但若階段二撰寫 TC 時真有列引用 p.46 之該 popup，其 lint 將無值可比 ——
屆時之處置未定。

### 4.4 寫回 —— **缺，且下放包所指之「丙″」在本 feature 不適用**

**丙″ 之出處**：`features/vehicle_category/docs/handoff/29_writeback_resume.md` §2.4
定義為「丙′ 減圖片還原、加 xmlns:xr 補宣告」，其第 1 步為
**「openpyxl 開母本副本、寫入 14 欄、save」**，事後再以解壓／注入修補。

**本 feature 不用丙″，理由有二**：
1. **R-SU2 已裁**：「**任何以 openpyxl 存回母本之操作都會摧毀該下拉**
   （R-G1 註）。寫回**一律採 XML 外科式修改**」——
   丙″ 之第 1 步即 openpyxl save，與 R-SU2 直接牴觸。
2. vehicle_category 自身之下放包 36 §一已裁
   **「出貨版改用外科式」**（移植 `features/display/scripts/write_back_036.py` 之法），
   丙″ 僅保留於其**已產出之工作版**，不重產。
   即：丙″ 在其原 feature 亦已非現行方法。

**故「丙″ 之 GUI 驗證」是 vehicle_category 對其工作版之未結項
（`DELIVERY_CHECKLIST` 第 1／2 項，待 Pei 於有 Excel 之環境執行），
不是 sw_update 之前置。**

**本 feature 之真正缺項（缺項三）**：

| # | 缺項 | 現況 |
|---:|---|---|
| 3a | **外科式寫回腳本尚未建** | `features/sw_update/scripts/` 無任何 `write_back*`。可移植之既有實作：`features/display/scripts/write_back_036.py`（180 行）—— 依 PLAYBOOK §7.3 附註「方案評估時先掃他 feature 之 `scripts/`」，此處已掃並記明 |
| 3b | **Excel GUI 驗收之執行者未定** | LibreOffice headless 返回碼 0 **不等於** Excel；**GUI 應用程式不由執行層啟動**（vehicle_category 之既定原則）。須 Pei 或有 Excel 之環境 |

**母本之前後比對基線已實測**（R-SU2 令比對之各項，寫回後須逐項相等）：

| 量 | 母本值 |
|---|---:|
| 母本 SHA256 | `6372fb6be02f…825b2`（寫回後須**未變**） |
| zip 部件總數 | **48** |
| worksheet 數 | **9** |
| `<dataValidation `（sheet6，標準） | **3** |
| `<x14:dataValidation `（sheet6） | **1** |
| `<extLst>`（sheet6） | **1** |
| `<conditionalFormatting`（全簿） | **0** |
| printerSettings | **5** |
| media | **2** |
| drawing 相關部件 | **13** |
| `t="shared"` | **1401** |
| sheet6 dimension | `A1:AH1411` |

> ⚠ **`<conditionalFormatting` 之計數為 0** —— R-SU2 令比對此項，
> 而本母本根本沒有條件式格式。**該項之前後相等會恆真通過**，
> 即它在本 feature 是一個**不具鑑別力的檢查**。
> 記明以免其全綠被讀成「條件式格式已保全」。
> （此即 PLAYBOOK §7(7)「證明零是真的零」之同型：0 是真的 0，
> 但據以宣稱保全則無意義。）

### 4.5 其餘盤點所見（下放包未列，一併陳報）

| # | 缺項 | 說明 |
|---:|---|---|
| 4 | **TC ID 之命名未裁** | vehicle_category 有 R-VC28（`newR1L-VC-001…`）之先例；本 feature 無對應條文。母本 D2（專案名稱）未實測 |
| 5 | **`functional_safety`（S 欄）之值未裁** | S 欄落在 DV `T10:Z1411`（值域 `"0,1"`）**之外**，其值域與填法未查 |
| 6 | **`spec_reference` 之寫入格式未定案** | R-SU4 v2 定其為**查得**（CFTS057-{ObjectID}／SYS1 章節 token）非構造，但雙家族並存時之欄內表示法（分隔符、順序）未裁 |
| 7 | **Layer 3 之 11 組 TBD** | 不阻斷 TC 撰寫（R-SU18(c)：Layer 3 provisional 得就地修正），但影響導航效率 |

**以上 7 項只盤點，不裁定。**

---

## 5. 未結 DR 清單

**空表。** 本輪 0 筆、無變動。

### 待分析層確認之事項（非 DR，無外部資料需求）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **`338`／`357`／`360` 三個孤島列之歸屬**：其組別與前後鄰居皆不同，且依據疑為標題選詞 | §6.1 |
| 2 | **`Integrity Verification` 疑為二能力**：`310`/`311` 之 GT 章為 `4.8.2`（OMA-DM 通道），`312` 為 `4.8.3`（部署包）—— 依原則 2「跨章必拆」之同一精神，本組內部即跨章 | §6.1 |
| 3 | **`022`（0 列）併入 `Integrity Verification` 之依據為標題字面** —— 該群 0 列，**在原理上不可能有列證據**，故此歸屬永遠無法被證實或否證 | §6.1 |
| 4 | **T29d 之「丙″」** 在本 feature 不適用（R-SU2 已裁外科式），前置改為 3a／3b | §4.4 |
| 5 | **`priority` 空白 72 列之處置**與 High/Medium/Low → P0–P3 之對應 | §4.2 |

---

## 6. 獨立自評

### 6.1 §七.6 所問：七組切分中，有無哪一組之依據只是標題字面而非能力同一

**有，且可用一個客觀量指出，不必靠讀感。**

**量法**：於 `309` 群內，找出**其組別與前後鄰居皆不同**之列（下稱「孤島列」）。
037 之列序即 CFTS 之文件序，**同一能力之列在文件中傾向相鄰**；
一個列若被單獨從連續段中抽出，其依據就必須強過「相鄰」這個先驗。

**實測：孤島列 7 個，全部落在兩段。**

| 037 列 | 其組 | 前鄰 | 後鄰 |
|---|---|---|---|
| `338` | `Integrity Verification` | 337 `Deployment Conditions` | 339 `Status Reporting` |
| `339` | `Status Reporting` | 338 `Integrity Verification` | 340 `Deployment Conditions` |
| `357` | `Interruption Handling` | 356 `Session Management` | 358 `Status Reporting` |
| `358` | `Status Reporting` | 357 `Interruption Handling` | 359 `Session Management` |
| `359` | `Session Management` | 358 `Status Reporting` | 360 `Interruption Handling` |
| `360` | `Interruption Handling` | 359 `Session Management` | 361 `Session Management` |
| `361` | `Session Management` | 360 `Interruption Handling` | 363 `Telematics Client` |

各組於 `309` 內之連續段數：

| 組 | 段數 | 各段 |
|---|---:|---|
| `Telematics Client` | **1** | 363–367 |
| `Update Agent` | **1** | 370–383 |
| `Integrity Verification` | 2 | 310–312、**338** |
| `Deployment Conditions` | 2 | 336–337、340–346 |
| `Interruption Handling` | **3** | 313–329、**357**、**360** |
| `Status Reporting` | **3** | 330–334、**339**、**358** |
| `Session Management` | **4** | 347–356、**359**、**361**、368–369 |

**答案有三層：**

**(甲) `356`–`361` 這一段是逐列交替的。** SM／IH／SR／SM／IH／SM ——
六個連續列分屬三組，每一列都換組。
文件序上如此密的交替，只有兩種可能：規格作者在那六列裡真的交替寫了三種能力，
或者**切分是照標題裡的關鍵詞挑的**。
考慮那三列之標題為 `Installation Interruption State Management`(357)、
`Update Status Reporting to SWMC`(358)、`Download Interruption Recovery`(360)
—— **`Interruption`／`Reporting` 二詞恰好就是其被指去的組名**，
**且上繳包 14 §7.1 已先行記明** `321 Interruption Recovery Handling`、
`325 Download Interruption Handling`、`360 Download Interruption Recovery`
**三個近義標題無法由標題判其為同一能力之三面或三個不同能力**。
即：本輪把 `360` 指去 `Interruption Handling`，用的正是上一包已宣告不足以判斷的那個資訊。

**(乙) `338` 同型。** 其標題 `Pre-Deployment Package Authenticity Verification`
含 `Verification`，被自 336–346 之部署條件連續段中抽出。
其前鄰 `337 Deployment Flow Initiation`、後鄰 `339 OTA Status Reporting via Backchannel`
—— 若照文件序，338 屬部署流程之一步（下載後、回報前之驗證），
**「部署流程中的一個驗證步驟」與「驗證能力」是不同的切法**，二者皆可辯，
**而標題不能決定何者為是**。

**(丙) `022` 是最極端的一例，且它在原理上不可驗。**
下放包 §二 #1 之依據為「其標題 `Communication Security` 與該 Test Set 之
通訊／封包完整性性質相符」——**這是純粹的標題字面**，
而該群**所轄 in-scope 列為 0**，**故它永遠不會有任何一列的證據可支持或推翻此歸屬**。
其歸屬對交付無影響（0 列），但它是本輪唯一一個
**「依據只能是字面，因為別無他物可依」**的組成。

**另陳一項與此相關而下放包未問的**：`Integrity Verification` 之內部本身跨章 ——
`310`/`311` 之 GT 正解章為 `4.8.2`（OMA-DM 通道之訊息完整性與 DM Tree 加密），
`312` 為 `4.8.3`（部署包完整性）。切分原則 2 為「跨章之 Heading 群必拆」，
而本組是**跨章之 Test Set**。原則 2 之射程是否比照 R-SU19 及於 Test Set，未裁。

**不在本輪自行更動任何歸屬**（Test Set 之切分屬 R-SU18(b) 之分析層裁定），
四項列入待確認。

### 6.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §2 之「三重閉合全部通過」。**

那八個 ✅ 是本輪最像交付的東西，而它們證明的事情比看起來窄得多：
**三重閉合只證明這 311 列被無重複、無遺漏地分完了**，
完全不證明**分得對**。§6.1 指出的七個孤島列，
在三重閉合裡**每一個都是合格的**——它們既沒被漏、也沒被重複指派。

這與上繳包 14 §7.2 是同一件事的再現，而且更該記：
上一輪是「二重閉合全綠而原則 4 在報警」，本輪是
**「三重閉合全綠，而唯一能查『分得對不對』的信號（孤島列）我得自己去造」**。
R-SU10 v2 把閉合從二重加嚴到三重，加嚴的仍然全是**完整性**維度；
**正確性維度在條文裡至今只有原則 3、4 兩條，且都不可機器化。**

**能誠實說的是**：Layer 2 之完整性已被三種互不相同的方式驗過；
其正確性只被「文件序相鄰」這一個弱先驗檢查過一次，
而該檢查報出了 7 個例外。

### 6.3 一項我做了而下放包未要求的事

**§6.1 之孤島列量法。**

§七.6 問「有無哪一組之依據只是標題字面」。照字面回答，
就是逐組讀依據、憑判斷指認幾組 —— 那會是**我的讀感對分析層的讀感**，
沒有第三方可裁。

孤島列把它變成可量的：**文件序相鄰是一個與標題完全獨立的信號**
（來自 037 之排列，不來自任何人的措辭），
所以「被從連續段中抽出」是一個客觀事件，數得出來。
數完是 7 個，且它們不是散布的，而是聚在 `338–339` 與 `357–361` 兩處 ——
**聚集本身也是證據**：若切分真的照能力，錯誤應該散開；聚在一段，
表示那一段有系統性的東西（該段規格文字之能力邊界本就模糊，
或切分者在該段改用了不同的判準）。

**這一步之限度也須說明**：文件序相鄰只是**弱先驗**，不是判準。
規格作者確實可能在六列裡交替寫三種能力，那樣 7 個孤島全都是對的。
**孤島列指出的是「該處之依據需高於相鄰之先驗」，不是「該處錯了」** ——
判其對錯仍須讀那六列之描述，而那屬分析層。

### 6.4 T27 併行線之現況

依下放包 16「T27 併行線照跑」：**T27 之三項於上繳包 13 已交付**
（GT-A2 30 列材料、GT-C 50 物件材料、獨立觀測 16 組），
**其人裁尚未開始**（80 筆待分析層裁定）。
本包未推進併行線，亦未因 framework 定稿而改其優先序。
