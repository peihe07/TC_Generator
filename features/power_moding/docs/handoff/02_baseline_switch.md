# 下放包 02 —— 母本改定、workbook_state 改判與 Phase 1 前置

- 日期：2026-08-22
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/02_baseline_switch.md`
- 前一包：[01_intake.md](01_intake.md)（上繳 [../upstream/01_intake.md](../upstream/01_intake.md)，已覆核）

---

## 一、01 包之覆核結果

**通過。** 十二節齊備，§9 之六項獨立判斷具實質內容，§10／§11 之 git 揭露與動作
清單逐項對得起來。三項特別記明：

1. **§3.3 之自我更正（037 列號 +1 之推算錯誤）為本包最有價值之一項** ——
   「跨表列號一律以 id 實測比對，不以位移推算」升為本 feature 之作業常規
   （見 R-PMH12 之附帶條款）。
2. **§4.4 之 336/336 逐格驗證**使 R-PMH5 由宣稱變為實證，並在本包成為
   「丟棄該 48 列零資訊損失」之依據（§二 R-PMH8）。
3. **§9 第 6 項（三分頁未讀）自評為風險最高者，分析層同意** ——
   已列為本包步驟 3，且其中 `Test Case Framework` 分頁**只存在於客戶那份**
   （ext 母本為 9 分頁，無此頁），故該頁之內容只能自客戶檔取得。

### 1.1 A-PMH01 —— 採認執行層之更正（分析層自裁）

`FROP` 相異值為 **12** 而非 13；13 係將 8 個 Heading 列之空值計為一類。
**採認執行層所擬之口徑定義**：

> `FROP` 相異值 = 「`Categorization == Functional Requirement` 之列，
> `FROP` 欄非空值之相異數」。

R-PMH6 之原文**不改字**，以勘誤附註承接（比照 R-P36）。A-PMH01 → **RESOLVED**。
此屬量測口徑之定義，分析層自裁，不上呈。

### 1.2 A-PMH03 / A-PMH04 —— 核可其提案

- **A-PMH03**（SYS1 匯出相對 PDF 之內文偏離）：核可「通則 3 分工 ＋ 通則 7 並存
  ＋ Phase 4 逐 leaf 複核」。**outline 7.1 之重排列為 Phase 4 之指名複核項** ——
  該章節有 5 個 leaf（單一章節最大宗），且被移位改寫之子句正是動畫／splash
  之時序（3 sec／1.5 each），時序誤讀在 Power Management 出過一次
  （`006`，A-PW68，歷經兩輪修正與多次 lint 全綠而未被察覺）。狀態維持 **PENDING**
  至 Phase 4 複核完成。
- **A-PMH04**（6 則 outline 為圖片佔位）：核可「不判 export 不可讀」。惟依
  §9.1 通則 6，**圖像形式之抽取能力尚未實測**，列為本包步驟 8。狀態 **PENDING**。
- **spec_mode `A+B`**：**核可**（Home hybrid 前例）。含 canon §3 之圖像 render
  無條件義務。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

> 抄錄逐字，不改寫、不合併。抄畢附逐條核對表（比照 01 包 §2 之方式）。

```
R-PMH7（交付母本）
本 feature 之交付基底為 `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果
_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`
（SHA256 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`），
即 R-G1 所定之全域母本，不另行例外。

客戶交付夾之 `…_SWQT_PowerModingHMI_20260819.xlsx`
（SHA256 `2be63febf005dd87ad302b78989ee7800a1a90c60f1f6673f9b455e664625a54`）
自本條起之身分為「需求對應之來源複本」，其用途限於 037→036 之 leaf 對應
查核與其三個附屬分頁之內容取得，**不作交付基底、不作版面依據、
不作 style authority**。

判準：交付副本之 r9 表頭欄數為 34（A–AH），`Estimated Test Time (mins)`
恰出現一次。出現兩次或欄數為 35 者，即非本條所定之母本。
```

```
R-PMH8（workbook_state）
`workbook_state` 為 `BLANK`。

Q1 所核可之 `PREFILLED_DRAFT` 提案**撤回**。撤回之依據為 R-PMH7 更換交付
基底，致該狀態所描述之 48 列預填不存在於交付標的，**非原判定有誤** ——
01 包 §4.3 對客戶那份之逐列判定（filled 48 / qualifying-done 0）仍然成立，
且為本條之前提。

丟棄該 48 列之資訊損失為零：01 包 §4.4 已逐格驗證其 336/336 逐字等同 037
之七欄，037 本身為本 feature 之權威輸入且已在 `inputs/` 內。

連帶：`done_region` 不適用（`author_value: null`）；write-back 為自首資料列
（r10）append；done invariant 不適用。
```

```
R-PMH9（欄位對應重測）
01 包 §4.2 之 `16/16` 欄位對應**作廢** —— 其量測對象為 R-PMH7 所排除之
離群版面（35 欄，priority Q / design_method S / author AB / remarks AI）。

重測須對 R-PMH7 之母本 r9 表頭進行，並與下列三份**已交付件**交叉佐證
（G-H：先查他 feature 之交付件，且須先確認母本同一）：

  User Profiles 20260820、Comfort 20260817、Time Management 20260822

四者（母本 ＋ 三份交付件）之 r9 表頭須逐欄相等；不相等者停並回報，
不得擇一採用。
```

```
R-PMH10（前言欄之留白）
工作簿 `Test Case Specification 測試用例規範` 分頁之
`D3 審查者` / `D4 目的` / `D5 範圍 Scope` 三欄**一律留空**。

依據為實測：已交付件 User Profiles 20260820、Comfort 20260817、
Time Management 20260822、Power Management 20260821 四份之該三欄皆空，
R-PMH7 之母本亦空 —— 語料 5/5 無一填寫。

不得自擬字串填入。若日後客戶要求填寫，其字串由 Pei 給定，本條屆時另立
新條取代，不以「補上」之名逕行填寫。
```

```
R-PMH11（素材雜湊檔之版控）
`features/power_moding/inputs/MANIFEST.sha256` 須入版控。

實施方式：於 `features/power_moding/.gitignore` 之 `inputs/` 排除規則後
增列否定規則 `!inputs/MANIFEST.sha256`，並以 `git check-ignore -v` 對該
路徑實測其不再被忽略（唯讀指令，執行層可執行）。

素材檔本身（四份）維持不入版控。本條解 A-PMH05 所指之 §9.1 通則 9 衝突，
其適用範圍限於本 feature；`scripts/new_feature.py` 之 `GITIGNORE` 樣板
是否同步修改，屬 canon 層，本條不及之。
```

```
R-PMH12（跨表列號之比對方式）
跨表之列號對應一律以 id 實測比對，不以列號位移推算。

依據：037 之 56 列含 8 個 Heading 列而 036 之 48 列不含之，位移非定值
（01 包 §3.3）。本條適用於本 feature 之全部跨表比對，不限於 037↔036。
```

---

## 三、待裁清單（本包新增，不阻斷步驟 1–8）

| # | 事項 | 層級 | 分析層提案 |
|---|---|---|---|
| Q7 | `tc_id` 之 `{project}-{abbr}-{NNN}` 中之 `{abbr}` | **[PEI]** | 提案 `NR1L-PowerModing-{NNN}`（隨 `test_group`，比照 R-PMH2 之「取規格模組名，不取交付夾名」）。**裁定前執行層須先實測語料**：三份 rev C 已交付件之 `F` 欄實際值，回報其 `{abbr}` 與該 feature 之 `test_group`／交付夾名三者之關係，供 Pei 據以裁定 |
| Q8 | 客戶那份 036 之 `Test Case Framework` 分頁若含客戶側 Test Group／Test Set 期望值 | [PROPOSED]，Phase 3 | 提案：若非空，其值為 Layer 1／Layer 2 之**第三個輸入**（與 FROP 12 值、規格目次並列），且因其出自客戶而**權重高於** FROP 欄；若為空（Power Management 之 A-PW56 前例即實測為 0 非空儲存格），則 R-PMH6 之輸入維持兩項 |

---

## 四、作業步驟

> 步驟 3 為本包風險最高者（執行層 01 §9 第 6 項自評），排在前段。
> 任一步觸及 §五即停並回報，不跳過續做。

1. **抄錄** —— §二六條（R-PMH7 ~ R-PMH12）逐字抄入 `RULINGS.md`，附核對表。
   R-PMH6 條後之勘誤附註依 §1.1 落實（**原條文不改字**），A-PMH01 標 RESOLVED。

2. **版控修正（R-PMH11）** —— 改 `features/power_moding/.gitignore`，
   以 `git check-ignore -v features/power_moding/inputs/MANIFEST.sha256`
   實測其不再被忽略（**唯讀指令**）。`git add` / `commit` 只準備不執行（R-G5）。

3. **讀客戶那份 036 之三個附屬分頁** —— `Test Case Framework`、`Reference`、
   `QS Suggestion`。逐分頁 dump 全部非空儲存格（座標 ＋ 值），
   **不摘要、不判讀**。`Test Case Framework` 若非空，另附其與 037 `FROP`
   12 值之比對（相同／相異／新增各若干）。此為 Q8 之輸入。

4. **母本身分驗明（R-PMH7）** —— 對 `forms/…_20260817_ext.xlsx` 實測並登記：
   SHA256、zip 成員數、分頁清單、r9 表頭全欄、合併儲存格、
   **DV 清單（含 x14 擴充之有無與其範圍）**、B 欄公式、
   `last_capacity_row`（B 欄公式與各 DV 之實測上界）、欄寬、凍結窗格。
   此節同時清償 01 §9 之第 1、2 兩項。
   **不得以 `openpyxl` 開啟後存回**（R-G1 註／R-G3：x14 DV 一存即毀）。

5. **欄位對應重測（R-PMH9）** —— 對母本 r9 實測 16 鍵，並與三份已交付件
   逐欄比對。路徑：
   - `/Users/peihe/Work/…/ASW-R2/User Profiles/…_UserProfiles_20260820.xlsx`
   - `/Users/peihe/Work/…/ASW-R2/Climate Control Interface/…_Comfort_20260817.xlsx`
   - `/Users/peihe/Work/…/ASW-R2/Time Management/…_20260822.xlsx`

   **三份為唯讀來源，不得寫入、不得搬入 `inputs/`**（其非本 feature 之素材，
   僅為版面佐證）。報告匹配數與盲區聲明（R-G11），並附排除向（R-G9）：
   `C` 與 `E` 不得被誤配至 `req_id` / `tc_id`。

6. **`feature.yaml` 依 R-PMH7 / R-PMH8 / R-PMH9 更新** —— `paths.workbook`
   指向母本之工作副本；`workbook_state: BLANK`；`workbook.columns` 換為
   重測值；`done_region.author_value: null`；`write_back` 之起始列為 r10。
   宣告值與生效值分開記（G-C）。`tc_id_pattern` 維持 `TBD`（待 Q7）。

7. **`下拉選單` 分頁實測** —— 母本與客戶那份各自 dump，回報
   `design_method` 之 vocabulary 全集與二者之差異。
   `lint.design_method_source` 由「沿用預設」改為「實測」（01 §9 第 3 項）。

8. **PDF 圖像抽取能力實測（§9.1 通則 6，A-PMH04）** —— 對 SYS1 匯出之
   6 則圖片佔位所對應之 outline，找出其於 PDF 之頁次，render 為點陣圖
   （註明 DPI），回報：能否辨讀圖內文字、向量線條是否可分辨、
   其解析度下之可讀性判定。**本步驟只驗能力，不抽內容、不寫任何 TC 依據。**

9. **Q7 之語料實測** —— 三份已交付件之 `F` 欄（Test Case ID）實際值取樣，
   回報 `{abbr}` 字串與該 feature 之 `test_group`、交付夾名之對應關係表。
   **不提案、不採用**，供 Pei 裁定。

10. **037 ↔ SYS1 outline map** —— 建立 `data/outline_map.json`：
    037 之 48 leaf → `HMI Source ID` → SYS1 `Outline Number` → PDF 頁次。
    29/29 章節命中須以本表重現（01 §5.2 之數字為對照向，須先算後比）。
    失敗即 fail-loud，不靜默丟棄（Power Management 之 G103 前例：
    `build_layer3` 曾靜默丟棄一個無法解析之錨點，三閘全綠）。

---

## 五、停止條件

canon §0 六條，另加本包三條：

7. 母本與三份已交付件之 r9 表頭有任一欄不相等（R-PMH9）
8. `Test Case Framework` 分頁之內容與 037 `FROP` 或規格目次直接矛盾
9. 任何操作需以 `openpyxl` 對母本或工作副本執行 `save()`

**本包零寫回工作簿內容**（步驟 4 之工作副本僅為位元組複製 ＋ 結構登記，
不寫入任何儲存格）。**全部 git 之改狀態操作屬 Pei**（R-G5）。

---

## 六、上繳包要求（`docs/upstream/02_baseline_switch.md`）

1. §二六條之抄錄核對表 ＋ R-PMH6 勘誤附註之落實證明（原文 SHA256 未變）
2. 步驟 3 之三分頁全 dump ＋ `Test Case Framework` 之比對表
3. 步驟 4 之母本結構登記（十項，含 x14 DV 之有無）
4. 步驟 5 之欄位對應表 ＋ 四方比對結果 ＋ 盲區與排除向
5. 更新後之 `feature.yaml` 全文
6. 步驟 7 之 vocabulary 全集與差異
7. 步驟 8 之 render 可行性判定（含 DPI 與樣本說明）
8. 步驟 9 之 `{abbr}` 對應關係表（**不含提案**）
9. 步驟 10 之 `outline_map.json` 與 29/29 之重現結果
10. `A-PMH{n}` 更新（A-PMH01 → RESOLVED、A-PMH05 → RESOLVED、
    A-PMH03/04 維持 PENDING 並註明其複核時點）
11. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
12. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之 git 揭露分列
13. `docs/INDEX.md` 補本輪次列（執行層維護）

---

## 七、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH7 | 交付母本為 forms ext；客戶那份降為來源複本 | ✅ |
| R-PMH8 | `workbook_state` = `BLANK`；撤回 `PREFILLED_DRAFT` | ✅ |
| R-PMH9 | 欄位對應作廢重測，四方交叉佐證 | ✅ |
| R-PMH10 | D3／D4／D5 一律留空 | ✅ |
| R-PMH11 | `MANIFEST.sha256` 入版控 | ✅ |
| R-PMH12 | 跨表列號以 id 實測，不以位移推算 | ✅ |

六條各管一事（§9.1 通則 11）。R-PMH8 為**撤回型**，其撤回範圍已於條內明載
（撤回 `PREFILLED_DRAFT`，不撤回 01 §4.3 之逐列判定）。
