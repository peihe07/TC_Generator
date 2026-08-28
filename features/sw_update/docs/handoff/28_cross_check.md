# 下放包 28 —— TC-8 之處置（部分採認、部分否證）、R-SU33、R-SU34、lint 跨列檢查

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`27_batch1_fix.md`；對應上繳：`docs/upstream/26_cross_check.md`
- 裁定狀態：R-SU33、R-SU34 —— 分析層即裁
- **§0.3（`180` facet B）已於下放包 27 §1.3 裁定，本包不重裁**

---

## 一、上繳包 25 審查判定

**收。§6.1 之逐行 diff 是本輪最有力之一節，而其結論須拆成兩半 ——
一半採認，一半否證。**

### 1.1 §2.3 —— `I-sibling` 之範圍，本輪最重要之發現

`check_sibling_parens()` 之分組鍵**含 `req_id`**，故
`175`／`179`／`184` 三個不同 req_id 之間，**該檢查在結構上永不觸發**。

執行層之正確讀法採認：
> `I-sibling=0` 之語意是「同一需求列底下沒有重複的括號行」，
> **不是**「本簿無互相重複之 TC」。
> **跨 req_id 之偽通過目前無任何機器檢查覆蓋。**

且其對 R-SU32(c) 之修正正確：條文寫「**可能**因措辭不同而過關」，
**實測為「必然過關」——它連比都不會比。** §三 R-SU34 補此缺口。

**併簿探針（`probe_sibling9`）為未被要求而做者**，其價值在於：
若只交 `I-sibling=0` 一行，分析層極可能把它讀成
「機器已確認 TC-8 與 TC-1 不重複」。**任務問「lint 過了嗎」，
真正待答的是「lint 有沒有在看這件事」。**

### 1.2 §4.2 之附帶推論 —— 採認並記入台帳

> 拼寫型是四型中唯一**拼字檢查抓得到**的，而它留到了這裡 ——
> 即 037 之交付流程沒有這道關卡。故同型缺陷應假設尚有未發現者，
> **本台帳所載仍為下界。**

**正確。** `DESCRIPTION_DEFECTS.md` 之四筆為下界，不得陳述為全集。

### 1.3 §3.3 之實作陷阱 —— 記錄採認

`_rows_desc()` 之 311 列已濾除 Heading，餵給 `group_by_heading()`
**分群恆為 0 且不報錯**；由腳本自帶之閉合檢查當場擋下。
**「不報錯的空結果」是最危險的失敗模式** —— 其防線只有閉合檢查。

---

## 二、TC-8（`184`）之處置 —— **部分採認、部分否證**

### 2.1 採認之半：「across the check, download and installation phases」不可觀測

執行層之論證成立：靜默更新之錄影上**無任何階段界線**，
「check 何時結束、download 何時開始」在畫面上無表徵。
**故 ER 不得作階段歸屬之宣稱** —— 該措辭須刪。

**下放包 26 §五為 TC-8 所寫之區分理由（「ER 明列三階段」）確為措辭上的**，
分析層之誤，確認。

### 2.2 否證之半：**其增額驗證點不為零**

執行層 §6.1(丙) 稱「TC-8 相對於已有之三列，其增額驗證點為零」——
**此結論過強，不成立。**

**理由在觀測窗之起點，而非階段之歸屬**：

| TC | Procedure 第 3 步之錄影窗 | 所檢之違例 |
|---|---|---|
| `TC-1`（`175`） | **自更新開始執行**起 | prompt、progress notification |
| `TC-6`（`180`） | 自可用性查詢起 | **download** confirmation screen |
| `TC-7`（`182`） | 自可用性查詢起 | **deployment** confirmation screen |
| `TC-8`（`184`） | **自可用性查詢**起 | prompt、progress notification、confirmation screen |

**TC-1 之窗起於執行，TC-8 之窗起於查詢。**
一個在**查詢階段**彈出「有可用更新」提示、而執行階段完全靜默之系統：
`TC-1` 判 pass（該提示落在其窗外）、`TC-8` 判 fail。
**存在可使二者判決相異之系統行為，故其增額驗證點非空**（§8.3 之壓力測試）。

TC-6／TC-7 雖同窗，但其所檢者為二種 confirmation screen，
**不含 prompt 與 progress notification**。
故 TC-8 之獨有覆蓋為：**查詢階段之 prompt 與 progress notification**。

### 2.3 關鍵之一般化 —— 「及於全部 X」型需求不需逐 X 歸屬

`184` 之需求為「Silent 規則**及於全部** session flows」。
其為**否定式之全稱**（各 flow 皆不得觸發 HMI）。

**否定式全稱之驗證，不需要能區辨 X** ——
若規則在任一 flow 失效，該 flow 即會產生一次提示，
而該提示**必然落在涵蓋全部 flow 之觀測窗內**。
**故「窗內無違例」即為「各 flow 皆無違例」之充分驗證。**

執行層之分析在「不可作階段歸屬」上正確，
**但由此推出「無法驗證全稱」則不成立** —— 二者不是同一件事。

### 2.4 TC-8 之改寫（`newR1L-SU-008`）

**test_item**（括號下半改寫，去除階段歸屬）
```
The WiFi Update Service shall apply Silent Update execution rules to all supported update session flows, including update check, deployment package download and installation processing.
(No user-facing interaction from the availability check through installation)
```

**test_procedure 第 3 步**（明確化窗之起訖，不改其餘）
```
3. Record the head unit screen content continuously from the availability check until the software version changes
```

**expected_result 第 5 行**（**去除階段歸屬，改以觀測窗表述**）
```
5. Version_after differs from Version_initial; the recorded screen content, taken continuously from the availability check until the software version changes, contains no SW Update prompt, no progress notification and no confirmation screen
```

其餘各欄逐字不動。**PENDING 不掛** —— 其驗證點可觀測且非空。

**與 TC-1 之區分（記入 reasoning）**：
> 本 TC 之觀測窗起於**可用性查詢**，`newR1L-SU-001`（`175`）之窗起於
> **更新開始執行**。查詢階段之提示落於本 TC 之窗內、落於前者之窗外，
> 故二者之判決可相異。本 TC 不作階段歸屬之宣稱 ——
> 全稱之否定式由「窗內無違例」驗證即足（R-SU33）。

---

## 三、裁決條文（抄入 RULINGS.md，逐字）

```
R-SU33（全稱否定式需求之驗證 —— 觀測窗法）

需求形如「規則 R 及於全部 X（各 X 皆不得發生 E）」者，
其驗證**不需要能區辨個別之 X**。

理由：若 R 於任一 X 失效，E 即發生一次；只要觀測窗涵蓋全部 X，
該次 E 必落於窗內。**故「窗內無 E」為「各 X 皆無 E」之充分驗證。**

拘束：
(a) ER **不得作 X 之歸屬宣稱**（如「三階段皆無提示」），
    除非各 X 之界線本身可觀測。歸屬宣稱若不可觀測即為紙上措辭，
    其存在會使該 TC 看似有獨有驗證點而實無（下放包 26 §五之誤）。
(b) ER 須**明載觀測窗之起訖**，因窗之範圍即該 TC 之實質驗證點。
(c) **窗之起訖為 sibling 區分之合法依據** —— 二 TC 檢同一類違例而
    窗不同者，存在可使其判決相異之系統行為，故非 R-SU32(iii) 之
    不可區辨。
(d) 本條不適用於**肯定式**之全稱（「各 X 皆須發生 E」）——
    該型需逐 X 確認 E 發生，故仍需 X 可區辨。
```

```
R-SU34（跨 req_id 之偽通過 —— lint 覆蓋缺口）

實測（上繳包 25 §2.3）：`lint036.py::check_sibling_parens()` 之分組鍵
**含 `req_id`**，故不同 `Requirement ID` 之列之間，
**無論其括號行、Procedure、ER 多麼相同，該檢查在結構上永不觸發**。

R-SU32(c) 原文稱該類偽通過「於 sibling 檢查**可能**過關」——
**實測為「必然過關」**，條文之表述過弱，本條更正之。

裁定：

(a) **`I-sibling=0` 之語意**為「同一需求列底下無重複之括號行」，
    **不是**「本簿無互相重複之 TC」。凡引用該值者須連同本限定一併陳述。

(b) **增設 lint 檢查 `I-cross`**（跨 req_id）：
    對同一 Test Set 內之任二 TC，計其 `test_procedure` 與
    `expected_result` 之**逐行相同行數比率**；
    比率逾門檻者列為**待人裁**，不逕判 FAIL。
    門檻之初值由回測定（T41a），**不得自訂**。

(c) `I-cross` 為**警示器非判準** —— 逐行高度相同而仍合法者存在
    （如 R-SU33(c) 之窗不同者，其 Procedure 多數行相同而判決可相異）。
    **故其輸出一律送人裁，不得自動掛 PENDING。**

(d) 在 `I-cross` 落地前，**跨 req_id 之偽通過無任何機器覆蓋**，
    此事實須逐包揭露。
```

---

## 四、任務（T41）

| # | 任務 |
|---|---|
| T41a | **`I-cross` 之實作與回測**（R-SU34(b)）：計算同一 Test Set 內任二 TC 之 procedure／ER 逐行相同比率。**回測集為現有 10 個 TC**（pilot 5 + batch 1 之 5）：其中 **TC-8 vs TC-1 為已知之高相似但合法**（窗不同，R-SU33(c)）、**TC-9 vs TC-1 為已知之不可區辨**（`179`，已掛 PENDING）。門檻須使二者**分屬不同側**；若無門檻可使其分開，**如實回報「該指標分不開此二例」，不得挑一個剛好的數字** |
| T41b | **TC-8 之改寫產出**（§2.4）：`sandbox/batch01/` 更新 `newR1L-SU-008` 之 test_item 括號下半、procedure 第 3 步、ER 第 5 行；其餘不動。跑 lint，**預期 U 不變** |
| T41c | **TC-10 之產出**（`181`，下放包 27 §3.2）：`newR1L-SU-010`，**預期 U=5**（TC-9 之 3 + TC-10 之 2）。跑 lint 全輸出 |
| T41d | **台帳更新**：(i) `DESCRIPTION_DEFECTS.md` 檔首加註「本台帳所載為**下界**」及其理由（§1.2）；(ii) DR-SU2 依下放包 27 §二改**三段**，第三型現 **2 列**（`179`、`181`）——**`180` facet B 不入**（下放包 27 §1.3 已裁其行為歸 `179`，只掛一次）；(iii) `SOURCE_COLUMNS.md` 之未定 0 維持 |
| T41e | **T-抄**：R-SU33、R-SU34 逐字 append；索引表同步（**34 條現行**）。PLAYBOOK 追加二則：(1)「任務問『檢查過了嗎』，真正待答的是『檢查有沒有在看這件事』」（出處：上繳包 25 §6.2）；(2)「不報錯的空結果是最危險的失敗模式 —— 其防線只有閉合檢查」（出處：上繳包 25 §3.3） |

**不在本輪**：併行線 26 列之 TC、寫回、git。

---

## 五、上繳包要求（`docs/upstream/26_cross_check.md`）

1. T41e 核對結果 + 索引表（**34 條**）
2. **T41a 之 `I-cross` 回測 —— 本輪核心**（含「分不開」之如實回報選項）
3. T41b／T41c 之 lint 全輸出
4. T41d 之三項台帳
5. 未結 DR 清單（2 筆；DR-SU2 三段）
6. 獨立自評 —— 特別回答：**§2.3 之觀測窗論證，其成立依賴
   「查詢階段之提示會出現在畫面上」。若某系統之查詢階段提示
   出現後隨即自動消失（如 3 秒後淡出），連續錄影是否仍能捕捉到 ——
   即觀測窗法對「短暫顯示」之違例是否有盲區**
