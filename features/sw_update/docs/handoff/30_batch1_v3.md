# 下放包 30 —— 分析層之誤三項、TC-8 改判、R-SU33 v2／R-SU34 v2／R-SU36、Error Code 補裁

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`28_cross_check.md`（T41）、`29_error_code_intake.md`（T42）—— 二線於本包合流
- 對應上繳：`docs/upstream/28_batch1_v3.md`
- 裁定狀態：R-SU33 v2、R-SU34 v2、R-SU36、R-SU35(a) 補 —— 分析層即裁
- **本包撤銷下放包 28 §2.2 之否證：執行層上繳包 25 §6.1 之原結論成立**

---

## 一、分析層之誤 —— 三項，逐項記明

### 1.1 以一段**不存在之引文**否證了一個正確之結論（最重）

下放包 28 §2.2 之表載「TC-1 步驟 3：**自更新開始執行**起」，
`sandbox/pilot03` 之實際文字為
`Record the head unit screen content continuously until the update finishes`
—— **無起點**。下放包 27 §四引之 `throughout the update execution` 同樣不存在。

**同一處誤讀出現二次，且上繳包 25 已指出而下放包 28 §一逐節回應其餘卻獨漏此處。**

**後果**：§2.2 之壓力測試（查詢階段彈提示、執行階段靜默）在 TC-1 底下判不出來，
「二者判決可相異」未經證立，**「TC-8 之增額驗證點非空」隨之落空**。

**且該誤不可由改寫 TC-1 補救** —— 見 §二 2.1。

### 1.2 令執行層依一條 repo 裡不存在之條文行事

下放包 28 T41d(ii) 令「DR-SU2 依下放包 27 §二改三段」，
而 T41e 之抄錄清單**未含 R-SU32 v2** —— 該條自下放包 27 發出後從未落檔
（T40 未執行）。執行層依 charter「未寫入 repo 之裁決等於沒發生」**自行補抄**，
處置正確，**追認**。PLAYBOOK 編號更正（(28) 正交／(29) 含實例）一併追認；
下放包 29 T42b 誤引之「(28)」應為 **(29)**。

### 1.3 R-SU35(a) 之階段鏈漏兩階段，5 碼無落點

實測 `Error Code List` 分頁有 **10 個階段標題**，R-SU35(a) 只列 7 個。
`After HU start-up, suddenly` **不是表首說明，是帶 4 碼之階段標題**。
執行層依 R-SU20(d) 拒絕以字面填該欄，**正確**。§四補裁。

---

## 二、TC-8（`184`）之改判 —— 撤銷否證，採原結論

### 2.1 為何不能靠「釘死 TC-1 之起點」補救

若將 TC-1 步驟 3 改為「自**更新開始執行**起錄」，
**該起點本身不可觀測** —— 靜默更新之執行開始無任何外部表徵
（此正是 `179`／`181` 掛 `PENDING` 之同一成因）。
釘一個不可觀測之起點，等於把不可執行性從 ER 移到 Procedure。

若改為自**可用性查詢**起錄（唯一可觀測之起點，因其為測試者主動觸發），
**TC-1 之窗即與 TC-8 相同**。

**兩條路皆通向同一結論**：TC-8 相對於 `TC-1 ∪ TC-6 ∪ TC-7` 之增額驗證點
**確為空**（其 `no confirmation screen` 已由 TC-6／TC-7 覆蓋，
`no prompt／no progress notification` 已由 TC-1 覆蓋，
`across the three phases` 不可觀測）。

**執行層上繳包 25 §6.1(丙) 之結論成立，下放包 28 §2.2 之否證撤銷。**

### 2.2 TC-8 之處置

`newR1L-SU-008` 依 **R-SU32(iii)** 改判為**第三型（不可區辨）**：

- 掛 `PENDING`，成因記為**不可區辨**（非無後果）
- DR-SU2 第三型段由 2 列增為 **3 列**：`179`、`181`、**`184`**
- 其所求為**區辨手段**：`184` 求「三階段之界線在外部如何辨識」；
  若無，則其驗證應併入 `175` —— **併入須上游確認**（R-SU32(d)），
  分析層不逕併

**改寫（其餘各欄逐字不動）**：

**pre_conditions** 增第 3 行
```
3. PENDING: DR-SU2 means of identifying the boundaries between the update check, download and installation phases
```
**test_procedure** 第 3 步改
```
3. PENDING: DR-SU2 step to record the head unit screen content with the check, download and installation phases identifiable
```
**expected_result** 第 3 行改
```
3. PENDING: DR-SU2 observable evidence delimiting the check, download and installation phases
```
其餘行不動。**預期 U 由 5 增為 8**（TC-9 之 3 + TC-10 之 2 + TC-8 之 3）。

### 2.3 TC-1 不改

其步驟 3 之無起點雖為缺陷，但**釘死起點需要一個可觀測之事件，而該事件不存在**。
TC-1 之驗證單元（Silent 時無使用者互動而更新完成）不因無起點而失效 ——
其 ER 為「錄影全程無提示」，錄影自步驟 3 執行時起算，
**涵蓋下載與安裝之全程**，足以驗其單元。**記錄此限度，不改。**

---

## 三、裁決條文（抄入 RULINGS.md，逐字）

```
R-SU33 v2（全稱否定式之觀測窗法 —— (c) 之限定）

v1(a)(b)(d) 維持。(c) 更正。

(c) v2 —— **窗之起訖得為 sibling 區分之依據，惟其起訖點本身
    必須是可觀測之事件。**

    v1 之 (c) 未加此限，致下放包 28 §2.2 以一個不可觀測之起點
    （「更新開始執行」）作為二 TC 之區分依據；該起點在靜默更新下
    無任何外部表徵，**故其區分不可執行**（下放包 30 §2.1）。

    可觀測之起訖點，其典型為：**測試者主動觸發之動作**
    （如「觸發可用性查詢」）、**可讀值之變化**（如版本號改變）、
    **明確之畫面事件**。
    不可作起訖點者：內部狀態之轉換、無外部表徵之階段界線。

    **推論**：二 TC 若其窗之唯一差異在一個不可觀測之起點，
    則其為 R-SU32(iii) 之不可區辨，**不因 ER 措辭不同而免除**。
```

```
R-SU34 v2（跨 req_id 之偽通過 —— 指標更換）

v1(a)(c)(d) 維持。(b) 作廢並更換。

(b) v1 之指標（procedure／ER 之逐行相同比率）經回測**與其欲測之性質
    負相關**，作廢。實測（上繳包 26 §2）：
      合法之高相似配對（TC-8 vs TC-1，窗不同）      **0.60**
      已知不可區辨之配對（TC-9 vs TC-1）            **0.00**
    **任一門檻皆攔下合法者而放行不可區辨者。**

    成因為結構性：`TC-9` 之差異**全來自其三行 `PENDING` 佔位**，
    而佔位之存在正因該問題**已被人裁攔下**。
    **一個尚未被抓到的偽通過不會有佔位行 —— 它必然長得像正常 TC，
    故必然高分。** 即該指標量的是「已修過」，不是「有問題」。

(b) v2 —— **改量「觀測窗 × 違例類」，不量行文**：
    自各 TC 之 ER 抽取 (i) 觀測窗之起訖點（R-SU33 v2(b) 已令明載）、
    (ii) 所檢違例之類別。
    **窗之起訖相同 且 違例類別有交集者** 列為 `I-cross` 待人裁。
    本指標與 `PENDING` 佔位無關，故不受 v1 之反轉所困。

    **仍為警示器非判準**（v1(c) 不變）：窗同而違例類不同者合法
    （如 TC-6 之 download confirmation vs TC-7 之 deployment confirmation）。

    門檻不適用 —— 本指標為布林條件，非比率。

    **落地前之缺口揭露義務不變**（v1(d)）。
```

```
R-SU36（否定式觀測之時間解析度）

實測（上繳包 26 §6）：現行 TC 之錄影步驟未指定任何取樣參數，
致「連續錄影」「每 5 秒截圖」「測試者目視」皆滿足同一步驟 ——
**同一份 TC，三個測試者可得三個判決，而三人皆照著寫的做了。**

R-SU25(e) 之判別問句「台架上的人要看哪裡」已被問過並回答，
**「他要以什麼頻率看、看多久算看過」則從未被問**。
對持續狀態不重要，**對瞬時事件則決定判決**。

裁定：

(a) 凡 ER 為「觀測窗內無 E」之**否定式**者，其 procedure 之觀測步驟
    **須載其時間解析度**，且該解析度須嚴於所驗事件之最短持續時間。

(b) 最短持續時間**未知**時，該不確定性即為一個 DR 標的，
    **不得以「連續」一詞含混帶過** ——「連續」未定義是否排除定時截圖。
    現階段之寫法為 `Record … as continuous video capture`
    （明文排除定時截圖），並於 `reasoning` 記明所驗事件之最短持續時間未知。

(c) **宣稱式之觀測步驟一律不合格**：`Record every X shown …` 之 `every`
    是一個宣稱不是一個動作，其實現全繫於測試者。
    須改為具體之觀測手段（`newR1L-SU-004` 之步驟 2 屬此，見 T43b）。

(d) 本條與 R-SU33 之關係：R-SU33 保證「違例若發生必落於窗內」，
    **本條保證「落於窗內者被記錄下來」** —— 前者是範圍，後者是解析度，
    二者缺一則否定式之驗證不成立。
```

---

## 四、R-SU35(a) 之補裁（5 碼之落點）

**依據為碼之內容，非階段名之字面**（R-SU20(d)）：

| 階段 | 碼 | Description（節錄） | **裁定之 Test Set** | 內容依據 |
|---|---|---|---|---|
| `After HU start-up, suddenly` | `393217` | HU is in bricked state - two or more VCPU update were failed | **`Update Agent`** | `SWE1-FOTA-379`／`380` 為 failsafe 與**防磚**之需求單元，本碼即其失效之表現 |
| 同上 | `393216` | Report PBL mode enter — VCPU update failed by the previous USB update | **`Update Agent`** | 同上，為前次更新失敗後之復原態（`381` recovery） |
| 同上 | `327680` | General VCPU FW update error | **`Update Agent`** | V-CPU 更新之總括錯誤，其單元為更新執行本身 |
| 同上 | `393219` | Version sync error — newly installed package version didn't register | **`Update Agent`** | 安裝後版本未登錄，屬 `383` deployed software validation 之失效 |
| `RedBend update engine` | `2147483330` | Source ↔ Target versions mismatch | **`Update Agent`** | `382` differential update 之來源／目標相容性失效 |

**五碼全歸 `Update Agent`。** 併記：`Install ( M-CPU: Redbend )` 之
`-2147483330`（CRC Signature mismatch）與本碼**符號相反、數值相同**，
其為同一底層錯誤之二種呈現，**引用時須連同其符號逐字抄**（R-SU35(b)1）。

---

## 五、`Error_Code_List.xlsx` 九分頁之用途裁定

| 分頁 | 裁定 | 理由 |
|---|---|---|
| `Error Code List` | **已用** | R-SU35 |
| `Model Code`（44 列） | **不用** | 車型代碼↔車型名之對照，與 TC 之驗證內容無供給關係 |
| `Issue Mapping Version`（2 列） | **不用** | 內容為 SharePoint 連結字串，**素材不在本地、不可及**；不得據以推定其內容 |
| `ProvideSW_final`／`Flash Status`／`Flash Record`／`MD_IMAGE`／`R1L_Need_Machine`／`PROD_Parameter_Compare` | **不用** | 台架作業與版本發佈之記錄（其欄為 `Machine Label`／`FTP Image Path`／`Done Date` 等作業欄），非需求或驗證面之定義 |

**惟記一項可用之附帶事實**（不改上表）：`Flash Status` 之 `Error Code` 欄
實填 `262147` 等碼，**證明該錯誤碼確於實機作業中被觀測到並記錄** ——
此為 DR-SU2 v2(a)（顯示途徑）之一條線索，**但其未載「在哪裡讀到」**，
故不解該 DR。**線索與答案不得混同。**

---

## 六、任務（T43）

| # | 任務 |
|---|---|
| T43a | **TC-8 改判之產出**（§2.2）：`newR1L-SU-008` 三欄改寫，其餘不動。跑 lint，**預期 U=8** |
| T43b | **`newR1L-SU-004` 之步驟 2 改寫**（R-SU36(c)）：`Record every SW Update screen shown on the head unit until the update finishes` 改為<br>`Record the head unit screen content as continuous video capture until the update finishes`；其 ER 第 2 行對應改為<br>`The head unit screen content until the update finishes is recorded as continuous video capture`。**其餘 TC 之錄影步驟一併加註 `as continuous video capture`**（`001`／`002`／`006`／`007`／`010`），逐列列出改動前後 |
| T43c | **`I-cross` v2 之實作**（R-SU34 v2(b)）：自 ER 抽取窗之起訖與違例類，輸出「窗同且違例類有交集」之配對清單。**以現有 10 TC 回測**：TC-8 vs TC-1 **應**命中（窗經 §2.1 判定為同）、TC-6 vs TC-7 **應不**命中（違例類不同）。二者任一不符即如實回報 |
| T43d | **台帳更新**：(i) DR-SU2 第三型段增 `184`（3 列），成因逐列記；(ii) `ERROR_CODES.md` 之五碼補填 `Update Agent`（依 §四之內容依據，逐碼抄其依據）；(iii) `SOURCE_COLUMNS.md` 補 Error_Code_List 九分頁之裁定（§五），**未定歸 0** |
| T43e | **T-抄**：R-SU33 v2、R-SU34 v2、R-SU36 逐字 append；R-SU35(a) 之階段鏈補兩階段（**條文修訂，非新版** —— 其為漏列之補全，於原條文加註「補：下放包 30 §四」）。索引表以現場為準。PLAYBOOK 追加：「以引文支撐一個判斷前，回原文核對該引文存在 —— 引錯的引文會讓錯的結論看起來有依據」（出處：下放包 30 §1.1） |

**不在本輪**：`Interruption Handling` 批次、併行線 26 列之 TC、寫回、git。

---

## 七、上繳包要求（`docs/upstream/28_batch1_v3.md`）

1. T43e 核對結果 + 索引表
2. T43a／T43b 之改寫明細與 lint 全輸出（**預期 U=8**）
3. **T43c 之 `I-cross` v2 回測 —— 本輪核心**（二錨點是否分屬正確之側）
4. T43d 之三項台帳
5. 未結 DR 清單（DR-SU1、DR-SU2 v2；第三型 3 列）
6. 獨立自評 —— 特別回答：**§2.1 之推論（TC-1 之窗只有兩種可能，二者皆通向
   TC-8 增額為空）是否窮盡 —— 有無第三種可觀測之起點，
   能使 TC-1 之窗既可執行又與 TC-8 相異**
