# Project Profile — FW036 / R1L SWE1 Comfort (SR24 Comfort HMI Logic and Flow, Stellantis newR1L)

> **Approved 2026-08-15** — 下放包 `15_profile_draft.md` 之全部條款，
> 加 `16_profile_signed.md` §1 之三項裁定（Pei，2026-08-15：「裁的都是是是是」）。
> 三項皆「照建議」：§3.1 繼承但附實測條件（轉為 **G-1** gate）、§3.4 source
> token 照錄、§0.1 之 Excel 實開確認由 Pei 執行。

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.
>
> Instantiated from `FW036_R1L_Privacy_Profile.md` — 最近之 BLANK／revision C
> sibling。**結構條款可繼承，內容條款不繼承**：凡標「繼承」者為結構性，
> 其餘一律就 Comfort 自身證據重新導出。Comfort 與 Privacy 無共通 spec、
> 無共通 037 家族，故每一處內容差異皆重新推導，見 §7。

---

## 0. Project identity [ADD]

- Program：Stellantis newR1L；scope 037-A03 Comfort，**403 leaves**
  `SWE1-HVAC-001…129`（含 34 列 parent 形態之 Functional Requirement，**R-C3**）
- spec baseline：**SR24 CR24879 (September 25 2023)**（**R-C1**）。
  SR25 為 out-of-scope 參考，**不得作為來源**
- Deliverable workbook：FM-WI-FSM-036-A01 通用空白範本 `SWQT_20260121`
  （與 Privacy 同一份，65,821 bytes，SHA256 `cd876c202c71e74b…`）。
  **workbook_state = BLANK** —— 無 legacy region、無 done region、無凍結列
- Test Group = `Comfort`（**R-C6**）；tc_id = `NR1L-ComfortHMI-{NNN}` 自 001
  （**R-C7**，序號由 generator 指派，LLM 不得自行產生）；
  author on new rows = `PeiPYHsu`
- **Form revision C，欄位位移同 Privacy §0**：Q = Estimated Test Time、
  R = design_method、S = functional_safety、AA = author、AH = remarks。
  資料工作表 `Test Case Specification 測試用例規範`
- style authority：**具名 `home`** done region（144 列），
  **`amfm` 具名排除**（`DECISIONS.md` §4 已簽）。cross-feature exemplar 一律標
  `style only`；**每個字面值須回溯 Comfort 自身 spec 並以 lint 強制**（A-026 教訓）

### 0.1 Template preparation state [ADD] —— A-CF07 之處置

範本附帶兩列樣本殘留（第 10–11 列）。**依 Privacy §0.1 之 R23-4 程序處理，
逐字繼承**：

- 以 `backend/xlsx_surgical.py` 清空五格：**D10 / F10 / G10 / S10 / D11**，
  `s=` style 屬性原地保留
- **B 欄不得動**：B10 為 `=IF(ISBLANK($D10),"",ROW()-9)`，清 B 會刪掉範本
  自己的編號機制
- **不得整列刪除**：會位移 DV 之 `sqref` 與 R10 之 x14 下拉

首筆 TC 落於 **row 10**。備妥之 workbook 與其來源記入
`features/comfort/DELIVERY.sha256`（ENTRY 001）。

**寫回前須經 Pei 於 Excel 實際開啟確認四項**（Privacy R29-1 前例，
16 §1 裁定 3 確認由 Pei 執行）：

1. 無修復提示
2. R 欄下拉可用且為九項
3. D5 Scope 正確
4. 第 10–11 列已清且無殘留列號

**程式層檢查不能代替 Excel 自身之檔案完整性判定。**

---

## 1. Requirements authority chain [ADD]

- Chain：SR24 spec section → 037-A03 leaf（`SWE1-HVAC-nnn(-nn)`）→ FW036 TC
- **spec_mode A**（SYS1 export）。條文權威為
  `spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx`
  （70,040 bytes）。**唯一來源**，`inputs/` 不得存副本（**R-C11**）
- section ↔ parent req_id 為 **1:1 雙射**（129 ↔ 129，上繳 05 實測）
- **條款標籤（`C13.)`／`ICE11.)`／`HVS1.`／`W0.)`）不是唯一鍵**（A-CF13 四項）。
  traceability 一律以 **outline 節次**為鍵；條款標籤僅得出現於 `reasoning`
  與 `test_item` 之敘述
- **全文權威**：`data/section_fulltext.tsv`（129 列，不截斷）。
  `layer3_map.tsv` 之 `section_title` 為導覽欄位，**不得用於判讀**（**R-C18**）

## 2. Test Set vocabulary [OVERRIDE — 取代泛用自由標籤]

- Test Group（G 欄）= `Comfort`；Test Set（H 欄）取 framework Part N 之
  **15 組**，逐列填入。`fill_test_group_set: true`（BLANK，canon §2）
- **Layer 3 = SR24 outline 節次，framework 內部，永不寫入 workbook**（§4.1.5）
- `specification_reference`（N 欄）依 §10.7 承載 section —— **那是
  traceability 欄位，不是 Layer 3 欄位**，不得因「Layer 3 不入 workbook」
  而留白
- 最大組 `Heated Vented Seats`（59）**刻意不拆**（12 §1 裁定：同一進入路徑）。
  工作量以 BATCH 處理，不以拆 Set 處理

> **Part N 之兩次修正案已生效**（`features/comfort/framework.md`）：
> #15 更名 `Comfort Widget` → `Home Screen Widget`（13 §2）；
> 四節改置 `2.16`／`16.17` → Temperature and Fan 對、`2.14`／`16.14` →
> Anatomy 對（14 §1）。Test Set 之數量與名稱邊界不變。

## 3. Comfort house style

### 3.1 Test Item [OVERRIDE — 取代 §4.3 僅 tc_title]

> **G-1 PASS 2026-08-15**（下放包 17 §1）。本段生效。
> provenance 但書降為腳註，**不再具阻卻效力** —— 見本段末 †。

**繼承 Privacy §3.1 / SXM §3.1（結構性）**：Test Item = 以 spec 語言濃縮之
需求陳述，**modal 僅此欄允許**（引用需求原文）。泛用 §4.3 之 tc_title
（無 modal）仍產出於 JSON 供 lint 與 sibling 判別。ER 一律無 modal（§6）。

**G-1 實測結果**（`features/comfort/scripts/gate_g1_test_item.py`，可重跑）：

| 量測項 | 值 |
|---|---|
| 母體 | `home` done region，Z 欄 == `ArifChen`，**144 列**（assertion PASS） |
| 含 modal | **143 / 144（99.3%）** |
| 不含 modal | 1（row 135 —— 內容為 widget 對照表，非行為陳述） |
| modal 詞頻 | `shall` ×176、`would` ×1 |
| Test Item 長度 | min 83、**中位 273**、max 2657 |
| 形態 | `The system shall …` ＋ 情境括號；**非 tc_title 型短語** |

→ 與 §3.1 所述一致，**§3.1 生效**。

> † **provenance 腳註**（17 §1.1：事實保留，不阻卻判定）：`home` 之 RECON 所測檔
> （`…_Home_20260720.xlsx`，SHA256 `0e72b1ec…`）與 Home v2
> （SHA256 `cfc007f3…`）**皆不在 repo**。本次量測對象為
> `forms/…_Home_20260809.xlsx`（SHA256 `1895fb2a…`），FORMS.md 記其為
> pre-A-H26 build 加四道編修（**D5 / F / G / K / Z**）。
> **I 欄（Test Item）不在該四道之列**，此為「內容未受影響」之論據 ——
> 但該論據來自 FORMS.md 自身之 diff，在 Home v2 缺席下無法交叉驗證。
> 17 §1.1 依 **R-C15**（判準為蘊含，非直接）裁定此不改變判定：可設想之風險
> 為「該副本之 I 欄曾被編修」，然**一次「把 `shall` 引入 144 列中 143 列」
> 之編修並非可信之情形**。證據為真即蘊含結論，縱其來源鏈有一段未經交叉驗證。
>
> **母體選擇器之發現須保留**：`features/home/feature.yaml` 之
> `done_region.author_value` 為 `Arif`，該副本實為 `ArifChen`；以 `Arif`
> 選取得 0 列，而 0 列會產出「全數不含 modal」之空集合結論。母體列數
> assertion 擋下此事 —— 登為 **A-CF14**。

### 3.2 Pre-Conditions [ADD] —— Comfort 之 spec trigger

以下為 §8.5 例外之合法 Pre-Condition 類別，**每一句須標 source class**
（`spec-verbatim` / `spec-derived` / `test-setup`），**未標者視為未追溯**
（Privacy R36-4）：

**逐軸之類別（R-C34，35 §1）**：**介面型**者其某值移除的是**承載可觀察量
之介面**（功能可能仍在），**須逐條檢查**；**功能型**者其某值移除的是**功能
本身**，既有之「該功能有無」PC 即已排除。**未判類別之軸不得使用。**

| # | 軸 | 類別 | 某值之後果 |
|---|---|---|---|
| 1 | ATC / MTC | 功能型 | 缺離散溫度與 Auto 控制（2.14）|
| 2 | 單區 / 雙區 / 四區 | 功能型 | 無該區之控制 |
| 3 | **前排氣流模式集合**（43 §3 換軸，原為「tri-mode 有無」）—— 三值：**4 模式**（2.12 `C13.`）／**5 狀態**（2.12.1 `C13.0`）／**tri-mode 3 鍵 7 組合**（3.1 `C19`）| 功能型 | 三值互斥：某值移除的不是「tri-mode 功能」，而是**另外兩組模式集合**。原二值軸無位置可放 `C13.0` 之 5 狀態（它是「非 tri-mode」之細分，非其並列項）|
| 4 | MAX A/C 有無 | 功能型 | 無該功能 |
| 5 | MAX DEF 有無 | 功能型 | 無該功能 |
| 6 | 独立座椅分區有無 | 功能型 | 無該分區 |
| 7 | 加熱方向盤 Multi / Single | 功能型 | 層級數不同 |
| 8 | Standard vs Multi-Level 座椅 | 功能型 | 層級數不同 |
| 9 | **secondary lower screen 之有無**（19 §2.1）| **介面型** | 非可收合者 → **comfort section 自 head unit 移除**（6.3），僅 comfort popup 留存 |
| 10 | REAR DEFROST 之有無（29 §2）| 功能型 | 無該功能與其按鈕 |
| 11 | soft top 車身之有無（29 §2）| 功能型 | 影響 rear defrost 之配備 |
| 12 | **僅前排氣候**（33 §3）| **介面型** | → **tabs 不顯示**（2.1）|
| 13 | **HVAC 實體控制型式**（33 §3）| **介面型** | 3 旋鈕 ICS → **無 HVAC menu bar icon／畫面／popup**（2.14）|
| 14 | 前排 HVAC 風速範圍（37 §4）| 功能型 | `Off, 1-7`（2.7 `C6.`）／`Off, 1-8`（2.7.1 `C6.1`）—— 兩值皆不移除介面，改變者為值域 |
| 15 | **動力系統（EV／BEV vs 非 EV）**（39 §2）| **功能型** | 非 EV 車輛無 `ECO HVAC` 這組能力；AUTO 鍵、Menu Bar icon 與 comfort popup **仍在**（10.5 引 `standard ICE AUTO logics`、10.9.1 對照 `the standard ICE AUTO pop up`）|
| 16 | **Comfort Features 有無**（50 §1）—— 二值：**equipped**（17.3「all Comfort features **available to the vehicle** (i.e. Heated/Vented seats, Heated steering wheel)」）／**not equipped**（17.3「If the vehicle is **not equipped with Comfort Features** this widget page will not be shown」）| **功能型** | 無值移除的是**功能本身**（車上沒有加熱／通風座椅與加熱方向盤），widget 第二頁之消失是其**後果**而非另一個介面之移除；既有之「該功能有無」PC 即已排除。判定依據見下方附註 |
| — | 機型軸 R1 Low / R1 High | 功能型 | `14.19` 之 `-02` 為唯一含此條件者 |
| — | **市場／變體軸 EMEA ICS** | **介面型** | **ch16 全章為另一套介面** —— ch2／ch3 之 TC 於該車無對象 |

> **第十六軸之類別判定（50 §1，2026-08-15）—— 功能型，其依據**
>
> R-C34 之判準為：某值移除的是**承載可觀察量之介面**（功能仍在）＝介面型；
> 抑或**功能本身**＝功能型。
>
> 逐一比對既有之三個介面型軸，其共同形態是**功能還在，只是換了地方看或看不到**：
> 第九軸（comfort section 移到下螢幕，氣候功能仍運作）、
> 第十二軸（tabs 不顯示，各分頁之功能仍在）、
> 第十三軸（3 旋鈕 ICS 無 HVAC 畫面，氣候仍可由旋鈕操作）。
>
> **第十六軸不是這個形態**：車輛若未配備 Comfort Features，
> 加熱／通風座椅與加熱方向盤**本身就不存在**，不是「功能在而看不到」。
> `17.3` 之「this widget page will not be shown」是**功能不存在之後果**，
> 不是另一個介面之移除。
>
> **反面檢驗**（決定性）：介面型軸須逐條問「該軸之某值是否使**此介面**不存在」，
> 其價值在於**功能仍在而別條 TC 之可觀察量消失**。
> 實測全 124 條已生成 TC：**無一條之可觀察量位於 widget 第二頁**
> （`17.3` 之二 leaf 已停下），亦**無一條之功能是 Comfort Features 而其
> 可觀察量在別處**。故該軸不產生「功能仍在而觀察端消失」之情形。
>
> **結論：功能型 → 不進 `interface_axis_review` 之鍵，既有 124 條不回填。**
> 其使用方式為正向或否定式 PC（如 `17.3` 之二 leaf），出處具名 `17.3`。

> **第三軸換軸之附註（43 §3，2026-08-15）—— 值一之適用條件無條文**
>
> 三值皆逐字出現於條文，且全 129 節掃描（pattern `airflow mode|Airflow
> Mode|distribution mode|mode buttons|states`，逐一命中判讀）無第四個前排值。
> 惟 **`C13.` 陳述「There are 4 Airflow Mode」時未附任何配置條件** ——
> 它是無限定之一般句，`C13.0` 才以 `In some non-tri mode equipment types`
> 把 5 狀態切出來。
>
> 故**值一（4 模式）之適用條件只能由排除得出**（非 tri-mode、且非 5 狀態那類），
> 而條文從未正面陳述它。這與 `2.1` 之 tab 集合同型（`DATA_REQUESTS` #17：
> 條文說「depending on vehicle configuration」而不說哪種配置產生哪一組）。
>
> **後果，於 `Airflow and Defrost` 生成時必然遇到**：`2.12` 與 `2.12.2`
> 之 TC 寫不出一句有出處的肯定式 PC 來選定值一。已登 `DATA_REQUESTS` #31。
> `2.12.1`（值二）與 `3.1`（值三）不受影響 —— 兩者之條文各自帶正面限定語。

**生成時之義務（非事後掃描）**：每條 TC 定稿前，指出其可觀察量所在之介面，
並對**四個介面型軸**各問一次「該軸之某值是否使此介面不存在」。
答是者補排除式 PC（出處依 R-C29 具名）；答否者於 `reasoning` 或上繳包
具名理由。

**生成時檢查清單之二：入口未定義**（48 §1，2026-08-15）——
本項為 §8.4.1 與 R-C30 之**組合適用，非新規則**，故不另立 R-Cnn：
條文已 39 條，每多一條即多一份被引錯或被遺忘的機會，能以既有條文組合
表述者不另立。

```
生成時，若 procedure 之操作目標為條文所命名之畫面或功能，而其入口於本
feature 之全部 spec 節內未定義：

  一、照錄條文用語，不自造入口步驟（§8.4.1）
  二、reasoning 具名該入口未定義
  三、開 DR，歸入「入口未定義」類；同類合併為一項，逐例列其節次與詞
  四、不阻塞

判定「未定義」須具名搜尋範圍（R-C30）。
```

**現有二例**（`DATA_REQUESTS` #34 為該類之單一項）：
`16.16` 之 `controls screen`（全 129 節 pattern `controls screen` 僅 1 命中，
即該節自身）、`16.17` 之 `Voice Recognition session`
（pattern `Voice Recognition|voice command` 命中 4 節，無一節定義如何啟動）。

**此檢查與介面型軸之檢查不同**：軸問「這條在哪種車上跑不起來」，
本項問「**這條的第一步做不做得到**」。兩者皆非 lint 可判，
故同樣寫成生成時之必答項。

- **設備配置軸**（本 feature 之主軸，逐節出現）：ATC / MTC、單區 / 雙區 /
  四區、**前排氣流模式集合（三值，第三軸，43 §3）**、MAX A/C 有無、
  MAX DEF 有無、独立座椅分區有無、
  加熱方向盤 Multi-Level / Single-Level、Standard vs Multi-Level 座椅、
  **secondary lower screen 之有無**（第九軸，19 §2.1）、
  **REAR DEFROST 之有無**（第十軸，29 §2）、
  **soft top 車身之有無**（第十一軸，29 §2）、
  **僅前排氣候之有無**（第十二軸，33 §3）、
  **HVAC 實體控制型式**（第十三軸，33 §3）、
  **前排 HVAC 風速範圍**（第十四軸，37 §4）、
  **動力系統（EV／BEV vs 非 EV）**（第十五軸，39 §2）、
  **Comfort Features 有無**（第十六軸，50 §1，功能型）
- **機型軸**：R1 Low / R1 High（`14.19` 之 `-02` 為唯一含此條件者）
- **市場／變體軸**：EMEA ICS（ch16 全章）
- **禁用**：`HU is powered on`、`Climate is available`（皆為隱含環境前提）

<!-- AXIS-VALUES: machine-read by lint_tcs.py's axis-value-count gate.
     Do not reformat. Adding a value here without bumping
     negation-reviewed-at-value-count is a FAIL by design (35 §4).

     43 §4 — ONE BLOCK PER AXIS THAT USES A NEGATED pre_condition.
     Until 43 §4 this existed for axis 13 alone, so the other four
     negations (116 of the 181 negated PC lines) had no protection at
     all. 34 §4's reason — a negated PC silently covers whatever values
     the axis happens to have — does not depend on the axis number.

     A negated PC whose phrase matches no block below, and is not named
     in lint_tcs.py's NON_AXIS_NEGATIONS, is a FAIL. That is the part
     that makes a NEW unprotected negation audible instead of silent.

     44 §6 — `value-count` 之語意已改。原為「已知之值數」，現為
     **「經 129 節全語料掃描，未見第 N+1 個值」**，每塊以 `scan:` 欄
     具名其日期、pattern 與逐句判讀結果（R-C30）。無 `scan:` 欄者，
     其 value-count 未經證明。

     兩類窮盡，強度不同，`scan:` 欄一律載明係哪一類：
       列舉窮盡   —— 值全部具名，無 catch-all（軸 2、軸 10）。
                     gate 之 value-count 檢查在此類上是**活的**。
       catch-all —— 值列以 `other` 收尾（軸 13、EMEA、軸 9）。
                     此類**由構造保證窮盡**，故 value-count 永不會
                     合法增加，gate 對它只能偵測「有人改了清單」，
                     偵測不到「清單本來就漏了一個值」。
                     這不是缺陷，是該檢查在此類軸上的能力上限，
                     記之以免把它的綠燈讀成比實際更強的保證。
-->

<!-- FUNCTION-AXIS-REVERSE-TEST: machine-read by lint_tcs.py's
     `axis-type-reverse-test` gate (52 §3；**判準經 54 §1 訂正**).

     每一個判為**功能型**之軸，其判定所用之反面檢驗於此登記，**每次 lint
     重跑**。旗標記錄的是「有人看過」，常設檢查記錄的是「現在仍成立」——
     本案要的是後者，故不立旗標。

     **判準（54 §1 訂正後之目的版）**：
       FAIL —— 任一條 TC，其可觀察量所在之介面會因某軸之某值而不存在，
               而該 TC **未陳述該軸之值**。
       次要回報行 —— 上列命中之中，其**功能亦為該軸所轄**者（即 52 §3
               原措辭版）。兩版分列而不合併：日後若再發散，差異即是發現。

     **訂正之出處與理由**：52 §3 原寫「其功能為該軸所轄」，較窄；
     而該檢驗之目的（35 §1.1）為「功能仍在而**別條** TC 之可觀察量消失」
     —— 目的版要找的正是**功能不屬該軸、卻依賴該軸所移除之介面**者。
     上繳 36 §3.3 之 `-115`／`-117` 即此形態（其功能為 widget 內容，
     而第二頁之存在由軸 16 決定）。54 §1 裁定以目的版為 FAIL 判準。

     `removed-interface: none` 者為顯式聲明「該軸之值不移除任何介面」，
     其檢驗恆真。**顯式聲明與漏寫不同** —— 漏寫會被 gate 抓出來。
     **惟目的版之下，`none` 是一個比先前更強的主張**：它斷言全語料無任何
     TC 之可觀察量依賴該軸，而非僅「無軸所轄之功能如此」。

     **兩個 TC 數，語意不同，不以一個數字兼表兩義**（54 §4）：
       judged-at-tc-count    —— **判定當時**之語料規模。無可考者記
                                `unknown` 並具名其判定所在之下放包編號
                                （`judged-at-provenance`）。
       declared-at-tc-count  —— **本聲明寫下時**之語料規模。
     前者答「當初以多少證據判的」，後者答「這份聲明是何時寫下的」。

     **`declared-at-tc-count` 只在內容變更時更新**（56 §4）。判準為
     `content-sha` —— 下列欄位之雜湊前 12 碼，**逐一具名**：
         axis / function-keywords / removed-interface-keywords /
         axis-pc-keywords / judged-at-tc-count / judged-at-provenance
     不參與雜湊者：declared-at-tc-count 自身、judged-at、註解行。
     lint 之 `axis-type-reverse-test` 另驗記錄之 `content-sha` 與實際內容
     相符 —— 改了內容而忘了更新 `declared-at-tc-count` 會 FAIL。

     理由（`RUNBOOK.md` 另記其通則）：上一輪全批一律更新為 202，
     致該欄語意由「聲明寫下之時點」漂為「最近一次全量更新之時點」。
     **一個記錄「何時」的欄位，若隨每輪重寫，記的就不再是那個「何時」。**
-->

```function-axis-reverse-test
axis: 16  Comfort Features 有無
function-keywords: heated seat | vented seat | heated/vented | heated steering wheel | heated wheel | Comfort feature
removed-interface-keywords: second Comfort widget screen | second widget screen
axis-pc-keywords: equipped with Comfort features | not equipped with Comfort Features
judged-at-tc-count: 124
declared-at-tc-count: 202
content-sha: 38a2ea8458ec
judged-at: 2026-08-15 (50 §1)
# 反面檢驗只找**未帶本軸 PC** 之 TC —— 帶了該 PC 者已被限定於某一值，
# 其可觀察量不會意外消失。`-125`／`-126` 之可觀察量正在該介面上且其功能
# 為本軸所轄，但兩者皆帶本軸之 PC，故不算違反（上繳 36 §3.2 之解讀）。
```

```function-axis-reverse-test
axis: 1  ATC / MTC
function-keywords: discrete temperature | Auto control over the set temperature
removed-interface-keywords: none
axis-pc-keywords: ATC climate system | MTC configuration | relays MTC functionality
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 2612b256d074
judged-at-provenance: 33 §3（第一軸自 profile 建立時即列，其類別未見單獨裁定包）
judged-at: 2026-08-15 (52 §3 之補登)
# MTC 值移除的是**功能**（離散溫度設定與對設定溫度之 Auto 控制），
# 其「AUTO 不顯示」為功能不存在之後果。2.14 之 3 旋鈕 ICS 段落屬第十三軸
# （介面型），不屬本軸。
```

```function-axis-reverse-test
axis: 2  單區 / 雙區 / 四區
function-keywords: single zone | dual zone | 4 Zone | SYNC | Sync
removed-interface-keywords: "SYNC" button | SYNC button | Sync button | SYNC is on | SYNC is off
axis-pc-keywords: not a single zone climate configuration
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: d06665238baa
judged-at-provenance: profile §3.2 建檔時（15／16 §1），無單獨裁定包
judged-at: 2026-08-15 (52 §3 之補登)；**removed-interface 於 54 §2 由 `none` 改為實測值**
# 54 §2 —— 本軸之 `none` 聲明經執行層自陳可爭（上繳 36 §7.3）：2.11 之
# 「Sync is not shown for single zone climate configurations」確為介面後果。
# 原判功能型之理由「功能與觀察端同時消失」只對**以 SYNC 為功能**之 TC 成立，
# 而目的版問的是**以 SYNC 指示為可觀察量、功能是別的**之 TC。
# 故本軸改為宣告其所移除之介面（SYNC 指示），使目的版能實際跑起來。
# **類別未改判**（54 §2 明示不先行改判）—— 實測結果見上繳 37 §2。
```

```function-axis-reverse-test
axis: 3  前排氣流模式集合
function-keywords: airflow mode | Airflow Mode | distribution mode
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 4615492aa2e2
judged-at-provenance: 43 §3（換軸時同輪判定）
judged-at: 2026-08-15 (52 §3 之補登)
# 三值互斥，某值移除的是另外兩組模式集合本身，非承載它們的介面
```

```function-axis-reverse-test
axis: 4  MAX A/C 有無
function-keywords: MAX A/C
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 1e5faf644e4c
judged-at-provenance: profile §3.2 建檔時（15／16 §1）
judged-at: 2026-08-15 (52 §3 之補登)
# 未配備者無該功能，其按鈕不存在亦因功能不存在（2.13「screens/popups are to be used when CCM relays presence of MAX A/C functionality」）
```

```function-axis-reverse-test
axis: 5  MAX DEF 有無
function-keywords: MAX DEF | MAX DEFROST
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 411e4935031b
judged-at-provenance: profile §3.2 建檔時（15／16 §1）
judged-at: 2026-08-15 (52 §3 之補登)
# 同軸 4：未配備者無該功能
```

```function-axis-reverse-test
axis: 6  独立座椅分區有無
function-keywords: seat zone | 座椅分區
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 42655c12214c
judged-at-provenance: profile §3.2 建檔時（15／16 §1）
judged-at: 2026-08-15 (52 §3 之補登)
# 未配備者無該分區之功能
```

```function-axis-reverse-test
axis: 7  加熱方向盤 Multi / Single
function-keywords: heated steering wheel | heated wheel
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 68a6622b226b
judged-at-provenance: profile §3.2 建檔時（15／16 §1）
judged-at: 2026-08-15 (52 §3 之補登)
# 兩值之差為層級數，皆有該功能，無介面被移除
```

```function-axis-reverse-test
axis: 8  Standard vs Multi-Level 座椅
function-keywords: heated seat | vented seat
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 00dff58dc162
judged-at-provenance: profile §3.2 建檔時（15／16 §1）
judged-at: 2026-08-15 (52 §3 之補登)
# 同軸 7：兩值之差為層級數
```

```function-axis-reverse-test
axis: 10  REAR DEFROST 之有無
function-keywords: REAR DEFROST | rear defrost
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 939c379a94c9
judged-at-provenance: 29 §2
judged-at: 2026-08-15 (52 §3 之補登)
# 3.4「the rear defrost button will not appear when not present in the vehicle」—— 按鈕不出現係因該功能不在車上
```

```function-axis-reverse-test
axis: 11  soft top 車身之有無
function-keywords: soft top | rear defrost
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 013f8258788e
judged-at-provenance: 29 §2
judged-at: 2026-08-15 (52 §3 之補登)
# 其作用為影響 rear defrost 之配備，即透過軸 10 生效，本身不移除介面
```

```function-axis-reverse-test
axis: 14  前排 HVAC 風速範圍
function-keywords: fan range | fan speed
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: d51d5b0d6d38
judged-at-provenance: 37 §4
judged-at: 2026-08-15 (52 §3 之補登)
# 兩值皆不移除介面，改變者為值域（37 §4 原文）
```

```function-axis-reverse-test
axis: 15  動力系統（EV／BEV vs 非 EV）
function-keywords: ECO HVAC | AUTO ECO
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: 693b812908af
judged-at-provenance: 39 §2
judged-at: 2026-08-15 (52 §3 之補登)
# 非 EV 車無 ECO 這組能力，而 AUTO 鍵、Menu Bar icon 與 comfort popup 仍在（39 §2）—— 被移除者為能力，非介面
```

```function-axis-reverse-test
axis: —  機型軸 R1 Low / R1 High
function-keywords: R1Low | R1H | R1 Low | R1 High
removed-interface-keywords: none
axis-pc-keywords: none
judged-at-tc-count: unknown
declared-at-tc-count: 202
content-sha: cb027fab6cd4
judged-at-provenance: 14 §1（機型軸之列入）
judged-at: 2026-08-15 (52 §3 之補登)
# 14.19 之 -02 為唯一含此條件者；兩值皆有 widget，差異為某 popup 顯示與否，屬該 leaf 自身之內容
```

### 3.2.1 待軸化候選 [ADD]（R-C42 三，下放包 64 §1，2026-08-16）

R-C42 一使「條文自帶條件」得以直接寫成 PC；R-C42 三要求**同一條件出現於
兩節以上而仍未登記為軸者，gate FAIL** —— 因為屆時「兩節之寫法是否一致」
由潛在風險變成實在風險。

**執行層之偏離與其理由（請裁）**：R-C42 三之字面要求「登記為軸」，
而 R-C42 二要求軸之登記仍依既有三條件。**本輪出現兩者相衝之實例**：
`dual airflow modes` 出現於三節，惟其**否定值於全 129 節無任何字面**
（DR #38），依三條件不得登記。**逕行登記等於替條文造一個值（§8.4.1）**，
那正是三條件所防者。

故本層之實作為：**每一個 ≥2 節之候選，須有一個具名之處置** ——
`registered: 第 N 軸` 或 `deferred: DR #x`，**沉默即 FAIL**。
這保住了 R-C42 三之目的（不一致之風險不得無人認領），
而不必為了滿足其字面去造一個值。

### 3.2.2 R-C42 之限定語 [ADD]（下放包 65 §3；**判準式定義：66 §2.2**）

**定義（取代逐詞列舉）**：

> 限定語為**任何限制該句適用範圍之前置成分**，含連接詞（`If`／`When`／
> `Where`）、限定性名詞片語（`Some vehicles`／`Vehicles equipped with`）、
> **及介系詞片語（`For …`／`On …`）**。
> 逐詞清單為其**實例**，非其定義；新形態出現時**擴充清單並記其出處**。

```rc42-qualifiers
markers: Some vehicles | On some vehicles | In some | If | For | When | Where | Vehicles equipped with | On the
# 65 §3 立、66 §2.2 擴充（加 Where / Vehicles equipped with / On the）。
# 清單是實例，定義在上方散文。**新增仍須記其出處**（本行即出處欄）。
# 66 §2.2 —— 執行層自陳「六個詞是從 21 條反推的，非自語料窮舉」（R-C37：
# 樣本全取陽性側），故改為判準式定義；逐詞清單只用於機器比對。
#
# 對照組（65 §3）：`2.11` 之「Adjusting Fan speed and Mode will alter the
# Front and Rear passengers」為**無限定語之陳述句**，其 leaf（`015-04`／
# `015-05`）維持停下 —— 兩側實例俱在。
```

**gate 之效力（66 §2.2）**：命中失敗**不硬阻**，改為要求該條之作者給出
**具名之處置** —— `condition:`（此為條件，附其逐字片段）或
`not-a-condition:`（此非條件，回復停下）。**沉默即 FAIL。**
理由與 R-C42-1 同：**該 gate 之目的是使「我讀成條件」與「它以條件之語法
出現」之落差可見，不是替語法作判準**；硬阻會使一個真條件因語法形態而被
擋下 —— 65 §3 之首次執行即是該例（`125-08`／`126-02`）。

```rc42-disposition
req_id: 125-08
section: 17.2
condition: 12' Portrait 50% widget also includes fan speed
why: **PC 已於 67 §2 改為逐字引用**（`12' Portrait 50% widget also includes
     fan speed`，含條文自己的 `12'` 而非 `12"`），惟其範圍仍以**名詞片語**
     界定，無前置連接詞或介系詞，故逐詞比對仍不命中 —— **這是形態問題，
     不是引用問題**（對照 `126-02`：改為逐字引 `On the 50% widget,` 後
     直接命中，其區塊已撤）。依 66 §2.2 之判準式定義，**名詞片語仍是限定
     該句適用範圍之前置成分**，故判為條件。**其適用性另由 DR #6 管**
     （R-C42 管可陳述，DR #6 管適用）
source: 66 §2.1（分析層裁定不回復停下）
```

```pending-axis
condition: dual airflow modes
pattern: dual airflow mode
sections: 2.3.1 | 14.14 | 17.5
disposition: deferred: DR #38
why: 正向值三節逐字；**否定值全語料無字面**，三條件第一項不成立。
     三節之 PC 皆逐字引其所在節之句子（R-C42 一），故其寫法之一致性
     目前由 `spec-verbatim` 之逐字要求保證，非由軸保證
```

```pending-axis
condition: ch9 變體（additional Rear Climate controls and shortcuts）
pattern: additional Rear Climate controls
sections: 9.2 | 9.3 | 9.4 | 9.4.1
disposition: deferred: DR #41
why: 正向值於 `9.1` 逐字，`9.2`／`9.4` 以「in these variants」回指；
     否定值無字面。四節之 PC 皆引 `9.1` 同一句，寫法一致
```

```pending-axis
condition: 螢幕尺寸／型號
pattern: 8.4
sections: 14.14 | 17.4
disposition: deferred: DR #6
why: **四節之值集合互異**（`14.14` 為 8.4/10.1 Landscape/10.25/12.3、
     `17.4` 為 8.4/10.1/12 landscaped、`17.2` 為 12" Portrait），
     故它們**不是同一個條件，而是同一個維度**。DR #6 未答之前，
     其值域無法定義；且該軸若登記將為**介面型**（R-C34），
     須回填全部 381 條之 `interface_axis_review` —— 該成本不應由一個
     值域未定之軸觸發
```

```pending-axis
condition: widget 尺寸（25% / 50%）
pattern: 50%
sections: 17.2 | 17.3
disposition: deferred: DR #6
why: 與螢幕尺寸同源（widget 尺寸依螢幕配置），其值域同受 DR #6 所限
```

```axis-values
axis: 12  僅前排氣候（→ tabs 不顯示）
values: 僅前排氣候 (2.1) | 具其他 comfort 分頁（Seats／Massage／Rear，2.1）
value-count: 2
negation: is not a front-climate-only vehicle
scan: 2026-08-16 | pattern `only Front climate|tabs will not be displayed|up to 4 tabs` | 全 129 節 **3 句命中，全在 `2.1`**（`up to 4 tabs`／`only Front climate`／`tabs will not be displayed`）—— **二值為邏輯上之窮盡（是／否），非列舉**；**哪一種配置產生哪一組 tab 仍未定（DR #17），惟本軸只需「tabs 是否顯示」二值，不需該對照**
negation-reviewed-at-value-count: 2
negation-users: NR1L-ComfortHMI-304, NR1L-ComfortHMI-305, NR1L-ComfortHMI-306, NR1L-ComfortHMI-307, NR1L-ComfortHMI-308, NR1L-ComfortHMI-309, NR1L-ComfortHMI-310, NR1L-ComfortHMI-311, NR1L-ComfortHMI-313, NR1L-ComfortHMI-314, NR1L-ComfortHMI-315, NR1L-ComfortHMI-316, NR1L-ComfortHMI-317, NR1L-ComfortHMI-318, NR1L-ComfortHMI-319, NR1L-ComfortHMI-320, NR1L-ComfortHMI-321, NR1L-ComfortHMI-322, NR1L-ComfortHMI-323, NR1L-ComfortHMI-324, NR1L-ComfortHMI-325, NR1L-ComfortHMI-326, NR1L-ComfortHMI-327, NR1L-ComfortHMI-328, NR1L-ComfortHMI-329, NR1L-ComfortHMI-330, NR1L-ComfortHMI-331, NR1L-ComfortHMI-332, NR1L-ComfortHMI-333, NR1L-ComfortHMI-334, NR1L-ComfortHMI-335, NR1L-ComfortHMI-336, NR1L-ComfortHMI-340, NR1L-ComfortHMI-341, NR1L-ComfortHMI-342, NR1L-ComfortHMI-343, NR1L-ComfortHMI-344, NR1L-ComfortHMI-345, NR1L-ComfortHMI-346, NR1L-ComfortHMI-347, NR1L-ComfortHMI-348, NR1L-ComfortHMI-349, NR1L-ComfortHMI-351, NR1L-ComfortHMI-352, NR1L-ComfortHMI-353, NR1L-ComfortHMI-354, NR1L-ComfortHMI-355, NR1L-ComfortHMI-356, NR1L-ComfortHMI-357, NR1L-ComfortHMI-358, NR1L-ComfortHMI-359, NR1L-ComfortHMI-360
# 63 §1 首次以排除式使用：ch11／ch12 之座椅控制位於 comfort category 之
# Seats 分頁內，2.1 於僅前排氣候之車輛移除全部 tabs，故該介面消失。
# 狀態列與 temperature/comfort popup 不隨 tabs 消失，故其 TC 不補
# （interface_axis_review 之 axis_12 欄逐節記其分野）。
```

```axis-values
axis: 16  Comfort Features 有無
values: equipped (17.3) | not equipped (17.3)
value-count: 2
negation: is not equipped with Comfort Features
scan: 2026-08-15 | pattern `Comfort [Ff]eatures?` | 全 129 節 3 句命中：14.16 之 `comfort feature control`（指單一控制，非配備集合，不計）、17.3 之正向與否定兩句 | **二值為邏輯上之窮盡（有／無），非列舉**；類別判定為功能型，見 §3.2 之附註
negation-reviewed-at-value-count: 2
negation-users: NR1L-ComfortHMI-126
# 值出處：17.3 CW2.（`all Comfort features available to the vehicle` /
# `If the vehicle is not equipped with Comfort Features`）
```

```axis-values
axis: 13  HVAC 實體控制型式
values: 3 knob ICS | one zone MTC with push button TEMPERATURE | other
value-count: 3
negation: does not have 3 knob HVAC controls with ICS
negation-reviewed-at-value-count: 3
scan: 2026-08-15 | pattern `knob|physical control|hard control type|push button|rocker|toggle|ICS\b` | 15 句命中 | 三值互斥且以 `other` 收尾 → **窮盡係由 catch-all 保證，非由列舉**（見下方附註）
negation-users: NR1L-ComfortHMI-003, NR1L-ComfortHMI-015, NR1L-ComfortHMI-016, NR1L-ComfortHMI-017, NR1L-ComfortHMI-018, NR1L-ComfortHMI-019, NR1L-ComfortHMI-020, NR1L-ComfortHMI-021, NR1L-ComfortHMI-022, NR1L-ComfortHMI-023, NR1L-ComfortHMI-024, NR1L-ComfortHMI-025, NR1L-ComfortHMI-026, NR1L-ComfortHMI-027, NR1L-ComfortHMI-028, NR1L-ComfortHMI-029, NR1L-ComfortHMI-030, NR1L-ComfortHMI-031, NR1L-ComfortHMI-032, NR1L-ComfortHMI-033, NR1L-ComfortHMI-034, NR1L-ComfortHMI-035, NR1L-ComfortHMI-036, NR1L-ComfortHMI-037, NR1L-ComfortHMI-038, NR1L-ComfortHMI-039, NR1L-ComfortHMI-040, NR1L-ComfortHMI-041, NR1L-ComfortHMI-042, NR1L-ComfortHMI-043, NR1L-ComfortHMI-044, NR1L-ComfortHMI-048, NR1L-ComfortHMI-049, NR1L-ComfortHMI-050, NR1L-ComfortHMI-051, NR1L-ComfortHMI-052, NR1L-ComfortHMI-053, NR1L-ComfortHMI-054, NR1L-ComfortHMI-055, NR1L-ComfortHMI-056, NR1L-ComfortHMI-057, NR1L-ComfortHMI-058, NR1L-ComfortHMI-059, NR1L-ComfortHMI-060, NR1L-ComfortHMI-061, NR1L-ComfortHMI-062, NR1L-ComfortHMI-063, NR1L-ComfortHMI-064, NR1L-ComfortHMI-065, NR1L-ComfortHMI-066, NR1L-ComfortHMI-067, NR1L-ComfortHMI-068, NR1L-ComfortHMI-069, NR1L-ComfortHMI-070, NR1L-ComfortHMI-071, NR1L-ComfortHMI-072, NR1L-ComfortHMI-073, NR1L-ComfortHMI-074, NR1L-ComfortHMI-075, NR1L-ComfortHMI-076, NR1L-ComfortHMI-077, NR1L-ComfortHMI-078, NR1L-ComfortHMI-079, NR1L-ComfortHMI-080, NR1L-ComfortHMI-081, NR1L-ComfortHMI-082, NR1L-ComfortHMI-083, NR1L-ComfortHMI-084, NR1L-ComfortHMI-085, NR1L-ComfortHMI-086, NR1L-ComfortHMI-087, NR1L-ComfortHMI-088, NR1L-ComfortHMI-089, NR1L-ComfortHMI-090, NR1L-ComfortHMI-091, NR1L-ComfortHMI-092, NR1L-ComfortHMI-093, NR1L-ComfortHMI-098, NR1L-ComfortHMI-099, NR1L-ComfortHMI-100, NR1L-ComfortHMI-101, NR1L-ComfortHMI-102, NR1L-ComfortHMI-103, NR1L-ComfortHMI-104, NR1L-ComfortHMI-105, NR1L-ComfortHMI-106, NR1L-ComfortHMI-107, NR1L-ComfortHMI-108, NR1L-ComfortHMI-109, NR1L-ComfortHMI-110, NR1L-ComfortHMI-111, NR1L-ComfortHMI-112, NR1L-ComfortHMI-113, NR1L-ComfortHMI-114, NR1L-ComfortHMI-115, NR1L-ComfortHMI-116, NR1L-ComfortHMI-117, NR1L-ComfortHMI-118, NR1L-ComfortHMI-119, NR1L-ComfortHMI-120, NR1L-ComfortHMI-121, NR1L-ComfortHMI-122, NR1L-ComfortHMI-123, NR1L-ComfortHMI-124, NR1L-ComfortHMI-125, NR1L-ComfortHMI-126, NR1L-ComfortHMI-127, NR1L-ComfortHMI-128, NR1L-ComfortHMI-129, NR1L-ComfortHMI-130, NR1L-ComfortHMI-131, NR1L-ComfortHMI-132, NR1L-ComfortHMI-133, NR1L-ComfortHMI-134, NR1L-ComfortHMI-135, NR1L-ComfortHMI-136, NR1L-ComfortHMI-137, NR1L-ComfortHMI-138, NR1L-ComfortHMI-139, NR1L-ComfortHMI-140, NR1L-ComfortHMI-141, NR1L-ComfortHMI-142, NR1L-ComfortHMI-143, NR1L-ComfortHMI-144, NR1L-ComfortHMI-145, NR1L-ComfortHMI-146, NR1L-ComfortHMI-147, NR1L-ComfortHMI-148, NR1L-ComfortHMI-149, NR1L-ComfortHMI-150, NR1L-ComfortHMI-151, NR1L-ComfortHMI-152, NR1L-ComfortHMI-153, NR1L-ComfortHMI-154, NR1L-ComfortHMI-155, NR1L-ComfortHMI-156, NR1L-ComfortHMI-157, NR1L-ComfortHMI-158, NR1L-ComfortHMI-159, NR1L-ComfortHMI-160, NR1L-ComfortHMI-161, NR1L-ComfortHMI-162, NR1L-ComfortHMI-163, NR1L-ComfortHMI-164, NR1L-ComfortHMI-165, NR1L-ComfortHMI-166, NR1L-ComfortHMI-167, NR1L-ComfortHMI-168, NR1L-ComfortHMI-169, NR1L-ComfortHMI-170, NR1L-ComfortHMI-171, NR1L-ComfortHMI-172, NR1L-ComfortHMI-173, NR1L-ComfortHMI-174, NR1L-ComfortHMI-175, NR1L-ComfortHMI-176, NR1L-ComfortHMI-177, NR1L-ComfortHMI-178, NR1L-ComfortHMI-179, NR1L-ComfortHMI-180, NR1L-ComfortHMI-181, NR1L-ComfortHMI-182, NR1L-ComfortHMI-183, NR1L-ComfortHMI-184, NR1L-ComfortHMI-185, NR1L-ComfortHMI-186, NR1L-ComfortHMI-187, NR1L-ComfortHMI-188, NR1L-ComfortHMI-189, NR1L-ComfortHMI-190, NR1L-ComfortHMI-191, NR1L-ComfortHMI-192, NR1L-ComfortHMI-193, NR1L-ComfortHMI-194, NR1L-ComfortHMI-195, NR1L-ComfortHMI-196, NR1L-ComfortHMI-197, NR1L-ComfortHMI-198, NR1L-ComfortHMI-199, NR1L-ComfortHMI-200, NR1L-ComfortHMI-201, NR1L-ComfortHMI-202, NR1L-ComfortHMI-203, NR1L-ComfortHMI-204, NR1L-ComfortHMI-205, NR1L-ComfortHMI-206, NR1L-ComfortHMI-207, NR1L-ComfortHMI-208, NR1L-ComfortHMI-209, NR1L-ComfortHMI-210, NR1L-ComfortHMI-211, NR1L-ComfortHMI-212, NR1L-ComfortHMI-213, NR1L-ComfortHMI-214, NR1L-ComfortHMI-215, NR1L-ComfortHMI-216, NR1L-ComfortHMI-217, NR1L-ComfortHMI-218, NR1L-ComfortHMI-219, NR1L-ComfortHMI-220, NR1L-ComfortHMI-221, NR1L-ComfortHMI-222, NR1L-ComfortHMI-223, NR1L-ComfortHMI-224, NR1L-ComfortHMI-225, NR1L-ComfortHMI-226, NR1L-ComfortHMI-227, NR1L-ComfortHMI-228, NR1L-ComfortHMI-229, NR1L-ComfortHMI-230, NR1L-ComfortHMI-231, NR1L-ComfortHMI-232, NR1L-ComfortHMI-233, NR1L-ComfortHMI-234, NR1L-ComfortHMI-235, NR1L-ComfortHMI-236, NR1L-ComfortHMI-237, NR1L-ComfortHMI-238, NR1L-ComfortHMI-239, NR1L-ComfortHMI-240, NR1L-ComfortHMI-241, NR1L-ComfortHMI-242, NR1L-ComfortHMI-243, NR1L-ComfortHMI-244, NR1L-ComfortHMI-245, NR1L-ComfortHMI-246, NR1L-ComfortHMI-247, NR1L-ComfortHMI-248, NR1L-ComfortHMI-249, NR1L-ComfortHMI-250, NR1L-ComfortHMI-251, NR1L-ComfortHMI-252, NR1L-ComfortHMI-253, NR1L-ComfortHMI-254, NR1L-ComfortHMI-255, NR1L-ComfortHMI-256, NR1L-ComfortHMI-257, NR1L-ComfortHMI-258, NR1L-ComfortHMI-259, NR1L-ComfortHMI-260, NR1L-ComfortHMI-261, NR1L-ComfortHMI-262, NR1L-ComfortHMI-263, NR1L-ComfortHMI-264, NR1L-ComfortHMI-265, NR1L-ComfortHMI-266, NR1L-ComfortHMI-267, NR1L-ComfortHMI-268, NR1L-ComfortHMI-269, NR1L-ComfortHMI-270, NR1L-ComfortHMI-271, NR1L-ComfortHMI-272, NR1L-ComfortHMI-273, NR1L-ComfortHMI-274, NR1L-ComfortHMI-275, NR1L-ComfortHMI-276, NR1L-ComfortHMI-277, NR1L-ComfortHMI-278, NR1L-ComfortHMI-279, NR1L-ComfortHMI-280, NR1L-ComfortHMI-281, NR1L-ComfortHMI-282, NR1L-ComfortHMI-283, NR1L-ComfortHMI-284, NR1L-ComfortHMI-285, NR1L-ComfortHMI-286, NR1L-ComfortHMI-287, NR1L-ComfortHMI-288, NR1L-ComfortHMI-289, NR1L-ComfortHMI-290, NR1L-ComfortHMI-291, NR1L-ComfortHMI-292, NR1L-ComfortHMI-293, NR1L-ComfortHMI-294, NR1L-ComfortHMI-295, NR1L-ComfortHMI-296, NR1L-ComfortHMI-297, NR1L-ComfortHMI-298, NR1L-ComfortHMI-299, NR1L-ComfortHMI-300, NR1L-ComfortHMI-301, NR1L-ComfortHMI-302, NR1L-ComfortHMI-303, NR1L-ComfortHMI-304, NR1L-ComfortHMI-305, NR1L-ComfortHMI-306, NR1L-ComfortHMI-307, NR1L-ComfortHMI-308, NR1L-ComfortHMI-309, NR1L-ComfortHMI-310, NR1L-ComfortHMI-311, NR1L-ComfortHMI-312, NR1L-ComfortHMI-313, NR1L-ComfortHMI-314, NR1L-ComfortHMI-315, NR1L-ComfortHMI-316, NR1L-ComfortHMI-317, NR1L-ComfortHMI-318, NR1L-ComfortHMI-319, NR1L-ComfortHMI-320, NR1L-ComfortHMI-321, NR1L-ComfortHMI-322, NR1L-ComfortHMI-323, NR1L-ComfortHMI-324, NR1L-ComfortHMI-325, NR1L-ComfortHMI-326, NR1L-ComfortHMI-327, NR1L-ComfortHMI-328, NR1L-ComfortHMI-329, NR1L-ComfortHMI-330, NR1L-ComfortHMI-331, NR1L-ComfortHMI-332, NR1L-ComfortHMI-333, NR1L-ComfortHMI-334, NR1L-ComfortHMI-335, NR1L-ComfortHMI-336, NR1L-ComfortHMI-337, NR1L-ComfortHMI-338, NR1L-ComfortHMI-339, NR1L-ComfortHMI-340, NR1L-ComfortHMI-341, NR1L-ComfortHMI-342, NR1L-ComfortHMI-343, NR1L-ComfortHMI-344, NR1L-ComfortHMI-345, NR1L-ComfortHMI-346, NR1L-ComfortHMI-347, NR1L-ComfortHMI-348, NR1L-ComfortHMI-349, NR1L-ComfortHMI-350, NR1L-ComfortHMI-351, NR1L-ComfortHMI-352, NR1L-ComfortHMI-353, NR1L-ComfortHMI-354, NR1L-ComfortHMI-355, NR1L-ComfortHMI-356, NR1L-ComfortHMI-357, NR1L-ComfortHMI-358, NR1L-ComfortHMI-359, NR1L-ComfortHMI-360, NR1L-ComfortHMI-361, NR1L-ComfortHMI-362, NR1L-ComfortHMI-363, NR1L-ComfortHMI-364, NR1L-ComfortHMI-365, NR1L-ComfortHMI-366, NR1L-ComfortHMI-367, NR1L-ComfortHMI-368, NR1L-ComfortHMI-369, NR1L-ComfortHMI-370, NR1L-ComfortHMI-371, NR1L-ComfortHMI-372, NR1L-ComfortHMI-373, NR1L-ComfortHMI-374, NR1L-ComfortHMI-375, NR1L-ComfortHMI-376, NR1L-ComfortHMI-377, NR1L-ComfortHMI-378, NR1L-ComfortHMI-379, NR1L-ComfortHMI-380, NR1L-ComfortHMI-381, NR1L-ComfortHMI-382, NR1L-ComfortHMI-383
# 值出處：2.14 C15.（3 旋鈕 ICS 例外；one zone MTC with push button TEMPERATURE 之反例外）
```

```axis-values
axis: EMEA  市場／變體軸 EMEA ICS
values: EMEA ICS (ch16 之另一套介面) | other
value-count: 2
negation: is not an EMEA ICS vehicle
negation-reviewed-at-value-count: 2
scan: 2026-08-15 | pattern `EMEA|LATAM|market|ICS\b|region` | 5 句命中，**無一句字面出現 `EMEA`** | 值名源自 16.1 之適用性判讀（R-C15／A-CF08），非條文字面；以 `other` 收尾 → 窮盡由 catch-all 保證
negation-users: NR1L-ComfortHMI-018, NR1L-ComfortHMI-019, NR1L-ComfortHMI-020, NR1L-ComfortHMI-021, NR1L-ComfortHMI-022, NR1L-ComfortHMI-023, NR1L-ComfortHMI-024, NR1L-ComfortHMI-025, NR1L-ComfortHMI-026, NR1L-ComfortHMI-027, NR1L-ComfortHMI-028, NR1L-ComfortHMI-029, NR1L-ComfortHMI-030, NR1L-ComfortHMI-032, NR1L-ComfortHMI-033, NR1L-ComfortHMI-034, NR1L-ComfortHMI-035, NR1L-ComfortHMI-036, NR1L-ComfortHMI-038, NR1L-ComfortHMI-039, NR1L-ComfortHMI-040, NR1L-ComfortHMI-043, NR1L-ComfortHMI-044, NR1L-ComfortHMI-048, NR1L-ComfortHMI-049, NR1L-ComfortHMI-050, NR1L-ComfortHMI-051, NR1L-ComfortHMI-052, NR1L-ComfortHMI-053, NR1L-ComfortHMI-054, NR1L-ComfortHMI-055, NR1L-ComfortHMI-056, NR1L-ComfortHMI-057, NR1L-ComfortHMI-058, NR1L-ComfortHMI-059, NR1L-ComfortHMI-060, NR1L-ComfortHMI-061, NR1L-ComfortHMI-062, NR1L-ComfortHMI-063, NR1L-ComfortHMI-064, NR1L-ComfortHMI-115, NR1L-ComfortHMI-116, NR1L-ComfortHMI-117, NR1L-ComfortHMI-118, NR1L-ComfortHMI-119, NR1L-ComfortHMI-120, NR1L-ComfortHMI-121, NR1L-ComfortHMI-122, NR1L-ComfortHMI-123, NR1L-ComfortHMI-124, NR1L-ComfortHMI-125, NR1L-ComfortHMI-126, NR1L-ComfortHMI-127, NR1L-ComfortHMI-128, NR1L-ComfortHMI-129, NR1L-ComfortHMI-130, NR1L-ComfortHMI-131, NR1L-ComfortHMI-132, NR1L-ComfortHMI-133, NR1L-ComfortHMI-134, NR1L-ComfortHMI-135, NR1L-ComfortHMI-136, NR1L-ComfortHMI-137, NR1L-ComfortHMI-138, NR1L-ComfortHMI-139, NR1L-ComfortHMI-140, NR1L-ComfortHMI-141, NR1L-ComfortHMI-142, NR1L-ComfortHMI-143, NR1L-ComfortHMI-144, NR1L-ComfortHMI-145, NR1L-ComfortHMI-146, NR1L-ComfortHMI-147, NR1L-ComfortHMI-148, NR1L-ComfortHMI-149, NR1L-ComfortHMI-150, NR1L-ComfortHMI-151, NR1L-ComfortHMI-152, NR1L-ComfortHMI-153, NR1L-ComfortHMI-154, NR1L-ComfortHMI-155, NR1L-ComfortHMI-156, NR1L-ComfortHMI-157, NR1L-ComfortHMI-158, NR1L-ComfortHMI-159, NR1L-ComfortHMI-160, NR1L-ComfortHMI-161, NR1L-ComfortHMI-162, NR1L-ComfortHMI-163, NR1L-ComfortHMI-164, NR1L-ComfortHMI-165, NR1L-ComfortHMI-166, NR1L-ComfortHMI-167, NR1L-ComfortHMI-168, NR1L-ComfortHMI-169, NR1L-ComfortHMI-170, NR1L-ComfortHMI-171, NR1L-ComfortHMI-172, NR1L-ComfortHMI-173, NR1L-ComfortHMI-174, NR1L-ComfortHMI-175, NR1L-ComfortHMI-176, NR1L-ComfortHMI-177, NR1L-ComfortHMI-178, NR1L-ComfortHMI-179, NR1L-ComfortHMI-180, NR1L-ComfortHMI-181, NR1L-ComfortHMI-182, NR1L-ComfortHMI-183, NR1L-ComfortHMI-184, NR1L-ComfortHMI-185, NR1L-ComfortHMI-186, NR1L-ComfortHMI-187, NR1L-ComfortHMI-188, NR1L-ComfortHMI-189, NR1L-ComfortHMI-190, NR1L-ComfortHMI-191, NR1L-ComfortHMI-192, NR1L-ComfortHMI-193, NR1L-ComfortHMI-194, NR1L-ComfortHMI-195, NR1L-ComfortHMI-196, NR1L-ComfortHMI-197, NR1L-ComfortHMI-198, NR1L-ComfortHMI-199, NR1L-ComfortHMI-200, NR1L-ComfortHMI-201, NR1L-ComfortHMI-202, NR1L-ComfortHMI-266, NR1L-ComfortHMI-267, NR1L-ComfortHMI-268, NR1L-ComfortHMI-269, NR1L-ComfortHMI-270, NR1L-ComfortHMI-271, NR1L-ComfortHMI-272, NR1L-ComfortHMI-273, NR1L-ComfortHMI-274, NR1L-ComfortHMI-275, NR1L-ComfortHMI-276, NR1L-ComfortHMI-277, NR1L-ComfortHMI-278, NR1L-ComfortHMI-279, NR1L-ComfortHMI-280, NR1L-ComfortHMI-281, NR1L-ComfortHMI-282, NR1L-ComfortHMI-283, NR1L-ComfortHMI-284, NR1L-ComfortHMI-285, NR1L-ComfortHMI-286, NR1L-ComfortHMI-287, NR1L-ComfortHMI-288, NR1L-ComfortHMI-289, NR1L-ComfortHMI-290, NR1L-ComfortHMI-291, NR1L-ComfortHMI-292, NR1L-ComfortHMI-293, NR1L-ComfortHMI-294, NR1L-ComfortHMI-295, NR1L-ComfortHMI-296, NR1L-ComfortHMI-297, NR1L-ComfortHMI-298, NR1L-ComfortHMI-299, NR1L-ComfortHMI-300, NR1L-ComfortHMI-301, NR1L-ComfortHMI-302, NR1L-ComfortHMI-303, NR1L-ComfortHMI-304, NR1L-ComfortHMI-305, NR1L-ComfortHMI-306, NR1L-ComfortHMI-307, NR1L-ComfortHMI-308, NR1L-ComfortHMI-309, NR1L-ComfortHMI-310, NR1L-ComfortHMI-311, NR1L-ComfortHMI-312, NR1L-ComfortHMI-313, NR1L-ComfortHMI-314, NR1L-ComfortHMI-315, NR1L-ComfortHMI-316, NR1L-ComfortHMI-317, NR1L-ComfortHMI-318, NR1L-ComfortHMI-319, NR1L-ComfortHMI-320, NR1L-ComfortHMI-321, NR1L-ComfortHMI-322, NR1L-ComfortHMI-323, NR1L-ComfortHMI-324, NR1L-ComfortHMI-325, NR1L-ComfortHMI-326, NR1L-ComfortHMI-327, NR1L-ComfortHMI-328, NR1L-ComfortHMI-329, NR1L-ComfortHMI-330, NR1L-ComfortHMI-331, NR1L-ComfortHMI-332, NR1L-ComfortHMI-333, NR1L-ComfortHMI-334, NR1L-ComfortHMI-335, NR1L-ComfortHMI-336, NR1L-ComfortHMI-337, NR1L-ComfortHMI-338, NR1L-ComfortHMI-339, NR1L-ComfortHMI-340, NR1L-ComfortHMI-341, NR1L-ComfortHMI-342, NR1L-ComfortHMI-343, NR1L-ComfortHMI-344, NR1L-ComfortHMI-345, NR1L-ComfortHMI-346, NR1L-ComfortHMI-347, NR1L-ComfortHMI-348, NR1L-ComfortHMI-349, NR1L-ComfortHMI-350, NR1L-ComfortHMI-351, NR1L-ComfortHMI-352, NR1L-ComfortHMI-353, NR1L-ComfortHMI-354, NR1L-ComfortHMI-355, NR1L-ComfortHMI-356, NR1L-ComfortHMI-357, NR1L-ComfortHMI-358, NR1L-ComfortHMI-359, NR1L-ComfortHMI-360, NR1L-ComfortHMI-361, NR1L-ComfortHMI-362, NR1L-ComfortHMI-363, NR1L-ComfortHMI-364, NR1L-ComfortHMI-365, NR1L-ComfortHMI-366, NR1L-ComfortHMI-367, NR1L-ComfortHMI-368, NR1L-ComfortHMI-369, NR1L-ComfortHMI-370, NR1L-ComfortHMI-371, NR1L-ComfortHMI-372, NR1L-ComfortHMI-373, NR1L-ComfortHMI-374, NR1L-ComfortHMI-375, NR1L-ComfortHMI-376, NR1L-ComfortHMI-377, NR1L-ComfortHMI-378, NR1L-ComfortHMI-379, NR1L-ComfortHMI-380, NR1L-ComfortHMI-381, NR1L-ComfortHMI-382, NR1L-ComfortHMI-383
# 值出處：16.1 之適用性判讀（R-C15）＋ ch16_mirror_map.tsv；R-C36-1 之逐條問句另行承載
```

```axis-values
axis: 9  secondary lower screen 之有無
values: non-foldable secondary lower screen containing comfort information (6.3) | lower screen that can be stowed (13.2) | other
value-count: 3
negation: is not configured with a non-foldable secondary lower screen
negation-reviewed-at-value-count: 3
scan: 2026-08-15 | pattern `lower screen|secondary screen|stowed|stowable|foldable|second screen` | 6 句命中（6.3／13.2×3／13.3.1×2），13.3.1 之 `stowed/retracted` 仍屬既有第二值 | 未見第四值；以 `other` 收尾 → 窮盡由 catch-all 保證
negation-users: NR1L-ComfortHMI-003, NR1L-ComfortHMI-034, NR1L-ComfortHMI-039, NR1L-ComfortHMI-042, NR1L-ComfortHMI-045, NR1L-ComfortHMI-046, NR1L-ComfortHMI-047, NR1L-ComfortHMI-059, NR1L-ComfortHMI-077, NR1L-ComfortHMI-082, NR1L-ComfortHMI-083, NR1L-ComfortHMI-089, NR1L-ComfortHMI-091, NR1L-ComfortHMI-092, NR1L-ComfortHMI-093, NR1L-ComfortHMI-094, NR1L-ComfortHMI-095, NR1L-ComfortHMI-096, NR1L-ComfortHMI-097, NR1L-ComfortHMI-098, NR1L-ComfortHMI-099, NR1L-ComfortHMI-100, NR1L-ComfortHMI-102, NR1L-ComfortHMI-104, NR1L-ComfortHMI-105, NR1L-ComfortHMI-106, NR1L-ComfortHMI-107, NR1L-ComfortHMI-108, NR1L-ComfortHMI-109, NR1L-ComfortHMI-110, NR1L-ComfortHMI-112, NR1L-ComfortHMI-113, NR1L-ComfortHMI-114, NR1L-ComfortHMI-115, NR1L-ComfortHMI-116, NR1L-ComfortHMI-117, NR1L-ComfortHMI-118, NR1L-ComfortHMI-119, NR1L-ComfortHMI-120, NR1L-ComfortHMI-121, NR1L-ComfortHMI-122, NR1L-ComfortHMI-123, NR1L-ComfortHMI-124, NR1L-ComfortHMI-125, NR1L-ComfortHMI-126, NR1L-ComfortHMI-127, NR1L-ComfortHMI-128, NR1L-ComfortHMI-129, NR1L-ComfortHMI-130, NR1L-ComfortHMI-131, NR1L-ComfortHMI-132, NR1L-ComfortHMI-133, NR1L-ComfortHMI-134, NR1L-ComfortHMI-135, NR1L-ComfortHMI-136, NR1L-ComfortHMI-137, NR1L-ComfortHMI-138, NR1L-ComfortHMI-139, NR1L-ComfortHMI-140, NR1L-ComfortHMI-141, NR1L-ComfortHMI-142, NR1L-ComfortHMI-143, NR1L-ComfortHMI-144, NR1L-ComfortHMI-145, NR1L-ComfortHMI-146, NR1L-ComfortHMI-147, NR1L-ComfortHMI-148, NR1L-ComfortHMI-149, NR1L-ComfortHMI-150, NR1L-ComfortHMI-151, NR1L-ComfortHMI-152, NR1L-ComfortHMI-153, NR1L-ComfortHMI-154, NR1L-ComfortHMI-155, NR1L-ComfortHMI-156, NR1L-ComfortHMI-157, NR1L-ComfortHMI-158, NR1L-ComfortHMI-159, NR1L-ComfortHMI-160, NR1L-ComfortHMI-161, NR1L-ComfortHMI-162, NR1L-ComfortHMI-163, NR1L-ComfortHMI-164, NR1L-ComfortHMI-165, NR1L-ComfortHMI-166, NR1L-ComfortHMI-167, NR1L-ComfortHMI-168, NR1L-ComfortHMI-169, NR1L-ComfortHMI-170, NR1L-ComfortHMI-171, NR1L-ComfortHMI-172, NR1L-ComfortHMI-173, NR1L-ComfortHMI-174, NR1L-ComfortHMI-175, NR1L-ComfortHMI-176, NR1L-ComfortHMI-177, NR1L-ComfortHMI-178, NR1L-ComfortHMI-179, NR1L-ComfortHMI-180, NR1L-ComfortHMI-181, NR1L-ComfortHMI-182, NR1L-ComfortHMI-183, NR1L-ComfortHMI-184, NR1L-ComfortHMI-185, NR1L-ComfortHMI-186, NR1L-ComfortHMI-187, NR1L-ComfortHMI-188, NR1L-ComfortHMI-189, NR1L-ComfortHMI-190, NR1L-ComfortHMI-191, NR1L-ComfortHMI-192, NR1L-ComfortHMI-193, NR1L-ComfortHMI-194, NR1L-ComfortHMI-195, NR1L-ComfortHMI-196, NR1L-ComfortHMI-197, NR1L-ComfortHMI-198, NR1L-ComfortHMI-199, NR1L-ComfortHMI-200, NR1L-ComfortHMI-201, NR1L-ComfortHMI-202, NR1L-ComfortHMI-203, NR1L-ComfortHMI-204, NR1L-ComfortHMI-205, NR1L-ComfortHMI-206, NR1L-ComfortHMI-207, NR1L-ComfortHMI-208, NR1L-ComfortHMI-209, NR1L-ComfortHMI-210, NR1L-ComfortHMI-211, NR1L-ComfortHMI-212, NR1L-ComfortHMI-213, NR1L-ComfortHMI-214, NR1L-ComfortHMI-215, NR1L-ComfortHMI-216, NR1L-ComfortHMI-217, NR1L-ComfortHMI-218, NR1L-ComfortHMI-219, NR1L-ComfortHMI-220, NR1L-ComfortHMI-221, NR1L-ComfortHMI-222, NR1L-ComfortHMI-223, NR1L-ComfortHMI-224, NR1L-ComfortHMI-225, NR1L-ComfortHMI-226, NR1L-ComfortHMI-227, NR1L-ComfortHMI-228, NR1L-ComfortHMI-229, NR1L-ComfortHMI-230, NR1L-ComfortHMI-231, NR1L-ComfortHMI-232, NR1L-ComfortHMI-233, NR1L-ComfortHMI-234, NR1L-ComfortHMI-235, NR1L-ComfortHMI-236, NR1L-ComfortHMI-237, NR1L-ComfortHMI-238, NR1L-ComfortHMI-239, NR1L-ComfortHMI-240, NR1L-ComfortHMI-241, NR1L-ComfortHMI-242, NR1L-ComfortHMI-243, NR1L-ComfortHMI-244, NR1L-ComfortHMI-245, NR1L-ComfortHMI-246, NR1L-ComfortHMI-247, NR1L-ComfortHMI-248, NR1L-ComfortHMI-249, NR1L-ComfortHMI-250, NR1L-ComfortHMI-251, NR1L-ComfortHMI-252, NR1L-ComfortHMI-253, NR1L-ComfortHMI-254, NR1L-ComfortHMI-255, NR1L-ComfortHMI-256, NR1L-ComfortHMI-257, NR1L-ComfortHMI-258, NR1L-ComfortHMI-259, NR1L-ComfortHMI-260, NR1L-ComfortHMI-261, NR1L-ComfortHMI-262, NR1L-ComfortHMI-263, NR1L-ComfortHMI-264, NR1L-ComfortHMI-265, NR1L-ComfortHMI-266, NR1L-ComfortHMI-267, NR1L-ComfortHMI-268, NR1L-ComfortHMI-269, NR1L-ComfortHMI-270, NR1L-ComfortHMI-271, NR1L-ComfortHMI-272, NR1L-ComfortHMI-273, NR1L-ComfortHMI-274, NR1L-ComfortHMI-275, NR1L-ComfortHMI-276, NR1L-ComfortHMI-277, NR1L-ComfortHMI-278, NR1L-ComfortHMI-279, NR1L-ComfortHMI-280, NR1L-ComfortHMI-281, NR1L-ComfortHMI-282, NR1L-ComfortHMI-283, NR1L-ComfortHMI-284, NR1L-ComfortHMI-285, NR1L-ComfortHMI-286, NR1L-ComfortHMI-287, NR1L-ComfortHMI-288, NR1L-ComfortHMI-289, NR1L-ComfortHMI-290, NR1L-ComfortHMI-291, NR1L-ComfortHMI-292, NR1L-ComfortHMI-293, NR1L-ComfortHMI-294, NR1L-ComfortHMI-295, NR1L-ComfortHMI-296, NR1L-ComfortHMI-297, NR1L-ComfortHMI-298, NR1L-ComfortHMI-299, NR1L-ComfortHMI-300, NR1L-ComfortHMI-301, NR1L-ComfortHMI-302, NR1L-ComfortHMI-303, NR1L-ComfortHMI-304, NR1L-ComfortHMI-305, NR1L-ComfortHMI-306, NR1L-ComfortHMI-307, NR1L-ComfortHMI-308, NR1L-ComfortHMI-309, NR1L-ComfortHMI-310, NR1L-ComfortHMI-311, NR1L-ComfortHMI-313, NR1L-ComfortHMI-314, NR1L-ComfortHMI-315, NR1L-ComfortHMI-316, NR1L-ComfortHMI-317, NR1L-ComfortHMI-318, NR1L-ComfortHMI-319, NR1L-ComfortHMI-320, NR1L-ComfortHMI-321, NR1L-ComfortHMI-322, NR1L-ComfortHMI-323, NR1L-ComfortHMI-324, NR1L-ComfortHMI-325, NR1L-ComfortHMI-326, NR1L-ComfortHMI-327, NR1L-ComfortHMI-328, NR1L-ComfortHMI-329, NR1L-ComfortHMI-330, NR1L-ComfortHMI-331, NR1L-ComfortHMI-332, NR1L-ComfortHMI-333, NR1L-ComfortHMI-334, NR1L-ComfortHMI-335, NR1L-ComfortHMI-336, NR1L-ComfortHMI-340, NR1L-ComfortHMI-341, NR1L-ComfortHMI-342, NR1L-ComfortHMI-343, NR1L-ComfortHMI-344, NR1L-ComfortHMI-345, NR1L-ComfortHMI-346, NR1L-ComfortHMI-347, NR1L-ComfortHMI-348, NR1L-ComfortHMI-349, NR1L-ComfortHMI-351, NR1L-ComfortHMI-352, NR1L-ComfortHMI-353, NR1L-ComfortHMI-354, NR1L-ComfortHMI-355, NR1L-ComfortHMI-356, NR1L-ComfortHMI-357, NR1L-ComfortHMI-358, NR1L-ComfortHMI-359, NR1L-ComfortHMI-360, NR1L-ComfortHMI-361, NR1L-ComfortHMI-362, NR1L-ComfortHMI-363, NR1L-ComfortHMI-364, NR1L-ComfortHMI-365, NR1L-ComfortHMI-366, NR1L-ComfortHMI-367, NR1L-ComfortHMI-368, NR1L-ComfortHMI-369, NR1L-ComfortHMI-370, NR1L-ComfortHMI-371, NR1L-ComfortHMI-372, NR1L-ComfortHMI-373, NR1L-ComfortHMI-374, NR1L-ComfortHMI-375, NR1L-ComfortHMI-376, NR1L-ComfortHMI-377, NR1L-ComfortHMI-378, NR1L-ComfortHMI-379, NR1L-ComfortHMI-380, NR1L-ComfortHMI-381
# 值出處：6.3 CM1.（不可收合者）／13.2 LS1.（stowed position 蘊含可收合者）
```

```axis-values
axis: 2  單區 / 雙區 / 四區
values: single zone (2.11) | dual zone (2.6) | 4 zone (7.10)
value-count: 3
negation: is not a single zone climate configuration
negation-reviewed-at-value-count: 3
scan: 2026-08-15 | pattern `single zone|dual zone|4 Zone|four zone|tri zone|zone climate|zones` | 10 句命中，逐句判讀：2.11／16.11 = single、2.6／2.3.1／14.14／17.5 = dual、7.10×2 = 4 zone、11.6／11.7 之 `seat zones` 為座椅分區非氣候分區（同形異義，不計） | **未見第四值，無 catch-all，係列舉窮盡**
negation-users: NR1L-ComfortHMI-053, NR1L-ComfortHMI-054, NR1L-ComfortHMI-085, NR1L-ComfortHMI-103, NR1L-ComfortHMI-104, NR1L-ComfortHMI-105, NR1L-ComfortHMI-119, NR1L-ComfortHMI-122, NR1L-ComfortHMI-149, NR1L-ComfortHMI-150, NR1L-ComfortHMI-151, NR1L-ComfortHMI-223, NR1L-ComfortHMI-224, NR1L-ComfortHMI-230, NR1L-ComfortHMI-241, NR1L-ComfortHMI-283, NR1L-ComfortHMI-293, NR1L-ComfortHMI-294, NR1L-ComfortHMI-295
# 值出處：2.11 C12.（single zone climate configurations）／2.6 C5.（driver 與 passenger）／7.10 CR10.（4 Zone Climate）
```

```axis-values
axis: 10  REAR DEFROST 之有無
values: rear defrost present | not present in the vehicle (3.4)
value-count: 2
negation: Rear defrost is not present in the vehicle
negation-reviewed-at-value-count: 2
scan: 2026-08-15 | pattern `rear defrost|REAR DEF\b|defrost button|not present` | 18 句命中，唯一陳述配置者為 3.4「the rear defrost button will not appear when not present in the vehicle」 | **二值為邏輯上之窮盡（有／無），非列舉**
negation-users: NR1L-ComfortHMI-031
# 值出處：3.4 C22.（the rear defrost button will not appear when not present in the vehicle）
```


**每一條配置條件須具名其來源節次**；不得以「某些車輛有此配置」概括
（§8.4.1 禁造值）。

> **「On vehicles with X」判別 —— 候選產生器，非判準**（33 §4.2）
>
> 條文帶有選擇子（`On vehicles with …`／`For soft top vehicles …`／
> `When a vehicle is configured with …`）者，**幾乎必然需要一個配置軸**，
> 故該判別**可用於產生候選**。
>
> **不得用於認定不需要**：無選擇子**不得推出無需軸**。
> 它是**詞彙型代理判準**，§5a 明定代理不得凌駕實質，R-C13 明定陰性結果
> 只是索引層事實。
>
> **本案例**：2.2 全篇無選擇子，執行層據此判其 8 條無需配置類 PC。
> 但 2.14 明文 `no HVAC screens` —— 3 旋鈕 ICS 之車輛根本沒有氣候觸控畫面，
> 2.2 之 8 條在該車上無一可執行。**判別產生的候選是空的，而實質答案不是。**
> 該 8 條已於 33 §4.1 之實質複查後各補一行 PC。

**第十軸 REAR DEFROST 之有無**（29 §2）：來源節 **3.4**（C22 明文
`when not present in the vehicle`）。**3.3 之條文（C21 一句）不含任何裝備
條件，不得作為本軸之出處** —— 3.3 之 TC 若需此條件，依 **R-C29** 標 `(3.4)`。

> **逐節判定規則（31 §4）**：全 129 節掃 `rear defrost` 命中 **8 節**
> —— `2.9`(4)、`2.10`(6)、`3.2`(8)、`3.4`(1)、`16.4`(1)、`16.8`(12)、
> `16.9`(2)、`16.10`(8)，合計 **42 leaf**。
> **「提及 rear defrost」不等於「需要 rear defrost 有無之 PC」。**
> `Climate Modes`（2.9／2.10）與四個 ICS 組（16.4／16.8／16.9／16.10）
> 生成時，凡欲寫入本軸之 PC 者，**一律逐節走 R-C28 三問 ＋ R-C31**，
> 第一問須具名**該節自身**之條文相關句。
> **不得以 3.4 之句子為所有節之出處** —— R-C29 允許跨節取據，
> 但要求具名**實際**出處，不是允許一句話覆蓋全語料。

**第十一軸 soft top 車身之有無**（29 §2）：來源節 **3.4**（C22 明文
`For soft top vehicles such as JL/JT`）。與機型軸（R1 Low／R1 High）
**為不同維度**：前者為車身型式，後者為主機變體，**不併入機型軸**。

> **措辭限制**：PC 一律寫「soft top」，**不寫成「JL or JT」**。條文為
> `such as JL/JT`（**例示**），寫成 JL/JT 即窄於條文 —— 屬 §8.4.1 之
> **反向造值：把例示讀成窮舉**。JL/JT 得於同句以 `such as` 形式引為例示。

**第十五軸 動力系統（EV／BEV vs 非 EV）**（39 §2）：來源節 **10.1**
（`ECO HVAC is an HVAC Mode, used on **EV Vehicles only**`）與 **10.2**
（`**For BEV vehicles**, the AUTO functionality can have 3 states`）。

> **判為一軸而非二軸**（39 §2 之判準）：ch10 內僅 10.9.1 另用
> `When ECO HVAC is equipped on a vehicle`，而該句係重述本章之適用範圍，
> **未使「配備 ECO HVAC」成為可獨立取值之第二性質**（實測 ch10 全章
> `configured` 0 命中、無任何 `if … ECO` 型條件句）。
> `AUTO ECO`／`AUTO ON` 之切換為**執行期狀態**（10.4／10.5 之按壓循環），
> 依 R-C28 第三問落 `test_procedure`，非配置軸。
>
> **判為功能型而非介面型**：非 EV 車輛是**沒有 ECO HVAC 這組能力**，
> 而非「有能力而無介面」—— AUTO 鍵、Menu Bar icon、comfort popup 於
> ICE 車上皆存在（10.5 引 `standard ICE AUTO logics`、10.9.1 對照
> `the standard ICE AUTO pop up`）。
>
> **與 EMEA ICS 形狀相似而類別相反**（R-C18）：ch16 是**另一套介面**實現
> 同一批能力，故為介面型；ch10 是**多出來的一組能力**，故為功能型。
> 兩者皆為「整章繫於一個車輛屬性」，**不得以形狀類推**。
>
> **既有影響**：本軸為功能型，故不進 `interface_axis_review` 之鍵，
> 既有 66 條不需逐條補答。

**第十四軸 前排 HVAC 風速範圍**（37 §4）：值 **`Off, 1-7`**（來源節 **2.7**，
`C6.`）／**`Off, 1-8`**（來源節 **2.7.1**，`C6.1`）。**功能型** —— 兩值皆不
移除任何介面，風速顯示於 climate screen 與 main category control，
7 段或 8 段皆在；改變者為值域。

> **兩值分屬兩節而非推論補齊**：`C6.1` 為 `C6.` 之子條，合讀為同一需求之
> 兩條文字，跨節取據本即 R-C29 所允許。`2.7.1` 之首語 `In some vehicles`
> 自身即宣告一個配置變數。
>
> **既有影響：0 條**（實測 —— 2.7 之 `-058`…`-062` 五條無一之判定依賴
> 風速上界為 7 或 8）。

**第十二軸 僅前排氣候（Front-only climate）**（33 §3）：來源節 **2.1**
（明文 `If only Front climate is available in a specific vehicle`）。
值：僅前排 ／ 含其他氣候區。

**第十三軸 HVAC 實體控制型式**（33 §3）：來源節 **2.14**。
值：3 旋鈕 ICS（`3 knob HVAC controls`）／ 單區 MTC 附 push button
TEMPERATURE（`one zone MTC with push button TEMPERATURE`）／ 其他。
本軸為**控制型式**，與第一軸（ATC／MTC）、第二軸（區數）**正交**，
三者於 2.14 同時出現且各自獨立。

> **與市場／變體軸之 `EMEA ICS` 不同，不得混用**：後者之範圍寫明
> **ch16 全章**，指 EMEA 市場之整套 ICS 氣候介面；本軸指 **ch2** 所述之
> 實體旋鈕配置，其後果為 HVAC 觸控 UI 不顯示。
> 兩者外觀皆含「ICS」而所指不同 —— 此正是 **R-C18 之同型風險：
> 措辭正確地屬於別處**。
>
> **否定式表述之限制**（34 §4）：本軸有三值，而
> `does not have 3 knob HVAC controls with ICS` 之寫法把它壓成二值。
>
> - 否定式**僅得用於「只需排除某一值」之情形**，且該 PC 須可辨識為排除式
> - **凡 TC 之行為隨軸值而異者，PC 一律具名該值**，不得用否定式
>   —— 首個案例為 `NR1L-ComfortHMI-046`，其 PC 明寫
>   `one zone MTC with push button TEMPERATURE`
>
> 理由：**否定式之涵蓋範圍取決於軸現有幾個值，而軸會增值。**
> 今日正確之否定式，會在增值當日靜默地變成錯誤，且無任何 gate 會報。

> **`MTC has a Climate screen` 不另立軸**（33 §3）：「有無 climate screen」
> 是本軸之**後果**，不是獨立的配置變數。把後果立成軸，會使同一事實有兩個
> 來源而無人維護其一致性。

**每一個 `pre_conditions` 行須先通過 R-C28 之三問，出處在最前**（24 §4.3）：
先問「該事實在其標註來源節之 `full_text` 有無明文對應」，無則停 ——
那不是落點問題，是 §7 FF 或 §8.4.1。第一問之回答**須具名條文之相關句**，
不得以「合理」「顯然」「恆常如此」代之。
**此為 Phase 4 展開之前置，非預防性建議** —— pilot 之 TC-007 即栽在此處。

**第九軸之 source class 逐節判定，不得跨節套用措辭**（19 §2.1）：讀該節
`full_text`，條文有字面表述者標 `spec-verbatim` 並照錄其措辭；由條文推得者標
`spec-derived`。**不得將 6.3 之 `non-foldable secondary lower screen` 措辭
套用於 13.x** —— 那是另一節的文字（R-C18 同型風險：措辭正確地屬於別處）。

**lower screen 之 stowed／retracted 為執行期狀態，非配置軸**（19 §2.2）。
判定測試：

> 該 TC 之驗證目標，是否就是「螢幕處於該狀態時之行為」？
> 是 → 該狀態為 spec 定義之 trigger condition，入 `pre_conditions`，標 source class
> 否 → 該狀態係為使測試可執行而設置，入 `test_procedure` 之步驟

不得因「寫在 Pre-Condition 比較省事」而上移；亦不得因「它是狀態」而一律歸
Pre-Condition —— §4.4 明禁 step-controlled state。

### 3.3 Design Method [OVERRIDE — 限縮 §12 輸出字串]

**繼承 Privacy §3.3**：僅得回傳 workbook `下拉選單!A1:A9` 之九個字串，
逐字元相符。Privacy 所記兩處範本瑕疵（R11:R59 之 DV 指向 `$A$1:$A$11`；
`Reference!C9` 與 `下拉選單!A6` 字串不一致）**同一範本，同樣適用**，
不繞過，隨 RD-1 上報。

### 3.4 Source-quoted tokens [ADD] —— §11 profile-scoped 例外

SR24 條文含下列原文標記，**引用時照錄，不得改寫為 `"..."`**
（16 §1 裁定 2；前例 Home A-H10）：

| token | 出處 |
|---|---|
| `«Front»`／`«Rear»` | 9.3、9.4.1（法文引號） |
| `15h`、`7/7`、`1-7`、`1-8` | 2.7、16.7、16.8、16.13 |
| `°F/C` | 2.10、16.10 |
| `LEDs (.` | 12.1 —— **明顯誤植，仍照錄**；修正 spec 原文非 TC 作者權限（§8.4.2） |
| `(-, +)` | 13.2 ~ 13.6（6 節）—— 條文自有記法。**依位置分割**（19 §3，不新增例外）：<br>`test_item`（承載需求原文，§3.1）與 ER 中之引用片段 → **照錄 `(-, +)`**<br>`test_procedure` 之按壓目標與非引用之 ER 敘述 → **`"-"` / `"+"`** |

作者自身之敘述（procedure 之按壓目標、非引用之 ER）一律用 `"..."`。
lint 對照 `section_fulltext.tsv` 之來源列驗證保留 token，**不逕行禁用**。

### 3.5 Spec Reference [ADD] —— 沿用 §10.7 預設格式

格式 `{spec_filename}_{section_id}`，stem 固定為
`SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
（**R-C1**）。**不得改寫為 SR25。**

外部 spec 引用（Home Screen HMI L&F，**R-C17**）另列其自身 section，
**不併入 Comfort stem**，且須寫全名指向 **SR24 Post 2A (March 17 2023)**
—— cache 內同時存有 SR25 版（上繳 06 §6 之警示）。

### 3.6 Remarks [ADD]

空字串，除非 BLOCKED 列、anomaly 標記或已記錄之 workaround。
**外部可見**（AMFM R10-4）：不得出現內部 ruling id 或 `A-CF…`。

**增補（下放包 66 §3，2026-08-16）—— 歧義須出現於 Remarks**：

> **凡條文之歧義會使測試員在執行時無法判定者，該歧義須出現於 Remarks。**
>
> `reasoning` 之讀者是**覆核者**，Remarks 之讀者是**執行者**，
> **而撞到它的是後者**。

其措辭須自足：**不得出現內部 ruling id、DR 編號或 `A-CF…`**
（歧義本身不是內部 id，故此增補與上列限制不衝突）。
現行實例（`14.12` 三條，`NR1L-ComfortHMI-374`／`-375`／`-376`）：

> The clause refers to the hard controls collectively. On vehicles whose
> hard controls are of mixed types, this case cannot be determined from the
> Comfort HMI specification alone.

**該類列須登錄於 `lint_tcs.py` 之 `AMBIGUITY_REMARKS`** ——
**惟其性質為登錄簿，非許可證**（下放包 67 §1 訂正 66 §4.2 之實作）：

| | marker 白名單（R-C26）| 本登錄簿（67 §1）|
|---|---|---|
| 作用 | **豁免 lint** | **不豁免任何檢查，只對帳** |
| 增列 | 須裁定 | **作者逕行寫入並同時登錄，不需個案裁定** |
| 理由 | 放寬須有人負責 | 66 §3 是**一般義務**；對義務加審批，其淨效果是那件事不再發生 |

**gate 雙向對帳**（`ambiguity-register`）：Remarks 帶歧義而未登錄 → FAIL；
已登錄而其 Remarks 無該文字 → FAIL（後者即上繳 44 §7.3 所指之缺口）。

**內容之三項限制為硬性，由 gate 檢查而非由登錄簿把關**：
（一）無內部 id（`R-C…`／`DR #…`／`A-CF…`／`§`）；
（二）長度足以說明何者不可判定（現行門檻 40 字元）；
（三）以執行者於該欄所讀之語言陳述（英文；非拉丁字元即 FAIL）。

### 3.6.1 散文欄位之引用鍵 [ADD]（下放包 60 §1，2026-08-16）

> **編號說明**：60 §1 指定寫入「§3.6」，惟該編號已為 Remarks 所用，
> 故置於其下為 §3.6.1，內容未改。

`reasoning`、`distinguishing_axis`（`axis`／`delta`）、`split_reason`、
`assumptions`、`remarks` 及一切散文欄位內，**不得以 tc_id 具名他條**，
一律以 **req_id** 具名（`113-08` 或 `SWE1-HVAC-113-08`）。

**理由**：R-C7 定 tc_id 由 generator 指派，且會因撤下、拆分而位移
（58 §2 首次實現）；req_id 為穩定識別。**以會動的東西當引用鍵，
其正確性只在下一次位移前成立。**

gate `no-tcid-in-prose`：散文欄位命中 tc_id → FAIL，指名該條與該欄。
**此為禁令而非正確性檢查** —— 「引用之 tc_id 存在且其所指與描述相符」
之檢查，前半機械可行而無用（位移後 `-227` 仍存在，只是指向別條），
後半需語意判斷而不可靠；**一道抓不到主要失效形態之 gate，
會使下一個人以為那件事已被覆蓋**。

**兩種形態皆禁**：`NR1L-ComfortHMI-233`（全稱）與 `` `-233` ``（短式）。
60 §1 只指定全稱；**實測全稱於 corpus 出現 2 次，短式 132 次**，
而 58 §2 所壞者正是短式 —— 只擋全稱之 gate，會在催生它的那份 corpus 上通過。

### 3.7 / 3.8 / 3.9 [繼承 Privacy 同編號條款]

- **Q 欄 Estimated Test Time**：`UNRULED_BLANK`，生成時留白並於 dry-run
  摘要列為具名之 blank-by-decision 欄
- **S 欄 Functional Safety**：一律 `NA`（Privacy R30-3；AMFM 158/158 前例）
- **T–Z 欄 Vehicle Model**：一律留白（Privacy R30-4）。
  **A-PV15 同樣適用於 Comfort**：範本七欄止於 27 世代，本專案平台為
  HDCC28，**不得將 27 世代欄位對映至 28 平台**。登為 Comfort 自身 anomaly

### 3.7.1 相似度之量測規約 [ADD]（下放包 64 §2，2026-08-16）

> **編號說明**：64 §2 指定寫入「§3.7」，惟該編號已為繼承 Privacy 之
> Estimated Test Time 所用（同 §3.6 之情形），故置於其下為 §3.7.1。

```
相似度之量測一律 `autojunk=False`；長文比對**須同時報共同子字串之長度**，
不得只報比值。比值為代理，長度為實質（§5a）。
```

**其由來**（62 §1.1 (b) 之首次執行）：`difflib.SequenceMatcher` 預設之
`autojunk` 於序列長度 > 200 時，把出現率 > 1% 之元素視為雜訊丟棄 ——
在英文段落上那是大半個字母表。實測 `16.13` ↔ `2.13` 之共同句 100 字元
被算成 **1 字元**，`mirror-map-verified` 差點把三個正確之 `mirrored` 判紅。

**其誤差方向為低估**，而低估之後果須寫明：
**相似度被低估 → 判為「非鏡射」→ 不加排除式 PC → 該 TC 之適用範圍過寬。**

**系統性重測之結果（64 §2，方法 `[machine]`）**：

| 層級 | 受影響？ | 說明 |
|---|---|---|
| 節級（`section_fulltext`，86–534 字元）| **否** | 五對節級數字重測後完全相同 |
| leaf 級（037 描述，61–110 字元）| **否** | 三對重測後完全相同；ch11 全 37 leaf 之最相似對造重測，**0 / 37 改變** |
| TC 文字級（數千字元）| **是** | `16.8`↔`2.8` 0.097→**0.317**、`16.8`↔`3.2` 0.070→**0.365**、`16.12`↔`2.12.1` 0.211→**0.576** |

**判定是否改變：否。** 三處皆為「相似度低，故不互相移植」之佐證，
訂正後仍低；惟 `16.8` 之兩對**大小關係翻轉**（訂正後鏡射對較相似），
該事實反而支持鏡射表之記載。

`lint_tcs.py` 之 `_longest_run()` 已固定 `autojunk=False`，
`verify_b_gates.py` 第四向把該回歸釘住 —— 若有人改回預設，該向即紅。

## 4. Split policy [ADD]

泛用 §8.3 適用。Comfort 特有：

- **`14.19` 之 8 leaves 已與條文 8 個 bullet 一一對應**（上繳 07 §5），
  037 之拆法與條文結構一致，**不得再合併**
- **R-C19 適用**：ch11／ch12 之 `opens popup` 差異一律以 `expected_result`
  表達，**不得**寫成不同 `test_procedure` 步驟或 `pre_conditions`。
  pilot review 時違反者列 **defect**（非 style-divergence）
- **SYNC 重疊**：`2.6.1`／`2.11`（及 `16.6.1`／`16.11`）內容重疊而分屬兩組，
  撰寫時須一併閱讀對造節，依 §4.6 判 sibling，必要時輸出 `duplicate_of`
- **ch2 ↔ ch16 之平行節不得互相引用或省略**：兩章條文近似但非等同
  （如 airflow 4 states vs 5 states、`ICE7` 之 MAX DEF 為 ch16 獨有），
  每組 TC 一律回自身節之全文

## 5. Marker vocabulary [ADD]

prefix `A-CF`。

### 5.1 `[BLOCKED-SPEC]`（R-C24，2026-08-15 裁定）

**適用**：某 leaf 之全部內容為對外部 spec 之委派或等效性宣告，扣除該委派後
於本 feature 範圍內**無任何可獨立驗證之餘留**者。

**產出 BLOCKED row** —— 不省略、不併入 sibling leaf、**不以複製 sibling 之
procedure 充數**（後者為 §7 之 False Pass：一條會通過但不驗證其 leaf 所要求
之事的 TC，remarks 之標記不會使它停止通過）。

| 欄 | 值 |
|---|---|
| `test_procedure` / `expected_result` | **空** |
| `specification_reference` | 該 leaf 自身之 outline，照常填 |
| Remarks | `[BLOCKED-SPEC]` ＋ 擁有該內容之文件名 ＋ 一句說明何以無餘留 |
| 其餘 | 依 profile 常規 |

Remarks **外部可見**（AMFM R10-4）：不得出現內部 ruling id 或 `A-CF` 編號。

**與 Privacy `[BLOCKED-ECU]` 之區別 —— 不得互相類推**：

| | `[BLOCKED-ECU]`（Privacy） | `[BLOCKED-SPEC]`（本 feature） |
|---|---|---|
| 成因 | 行為由**另一 ECU** 執行 | 行為**可觀察**，但其規範內容由**另一份 spec** 擁有 |
| 本 ECU 有無可觀察端 | **無** | **有**（只是無獨立於 sibling 之內容可驗） |
| 解除條件 | 該行為改由本 ECU 執行，或取得其可觀察指標 | 外部 spec 之內容納入本 feature 範圍，或該 leaf 經 037 改寫 |

**兩者外觀相同（皆無 procedure），成因不同。** 見到空 procedure 時，
須讀 Remarks 之 marker 方知其類別。

**lint 之豁免為具名回報行，不得靜默跳過**（前例：上繳 06 §2.1 之
`and n != "Comfort Widget"`）。`proc-min-steps` 與 `proc-er-1to1` 對
BLOCKED row 之豁免，每次 lint 皆輸出受豁免之 tc_id 清單。

**目前之 `[BLOCKED-SPEC]` 列**：`SWE1-HVAC-080-02`（HMI Core Logic and
Flow requirement N0）、`SWE1-HVAC-081-02`（CFTS044）。

### 5.2 `[BLOCKED-NON-HMI]`（R-C38，2026-08-15 裁定）

**適用**：某 leaf 之內容**既未委派予外部文件，亦非任何介面可觀察之行為**，
於本 feature 全部 spec 內無可觀察端者。

**產出 BLOCKED row** —— 與 `[BLOCKED-SPEC]` 同形（procedure／ER 空、
spec ref 照填），差別在 Remarks **不得填擁有者**：沒有擁有者正是本類之定義。

| 欄 | 值 |
|---|---|
| `test_procedure` / `expected_result` | **空** |
| `specification_reference` | 該 leaf 自身之 outline，照常填 |
| Remarks | `[BLOCKED-NON-HMI]` ＋ `Not an HMI-observable property` ＋ 一句說明何以無可觀察端。**不填擁有者** |
| 其餘 | 依 profile 常規 |

**使用條件五項（R-C38，缺一即回報停下）**：一、條文內無任何委派字面
（`see`／`as per`／`refer to`／具名文件）；二、037 確實產出該 leaf；
三、於本 feature 全部 spec 節內無可觀察端，須具名已查之節與搜尋範圍
（R-C30）；四、其可能之替代觀察量若已由其他 leaf 涵蓋，須具名該 leaf
（§4.5）；五、tc_id 經白名單增列（R-C26）。

**須同時列 RD-1**：037 對該 leaf 標 `Manual UI Testing` 而其 Expected
Result 無任何 UI 可觀察量者，係上游之分類問題（見 DATA_REQUESTS #24）。

**目前之 `[BLOCKED-NON-HMI]` 列**：`SWE1-HVAC-044-02`（ECO HVAC 之降耗）。

### 5.3 三類 BLOCKED marker 之對照 —— 不得互相類推

| | `[BLOCKED-ECU]`（Privacy） | `[BLOCKED-SPEC]`（本 feature） | `[BLOCKED-NON-HMI]`（本 feature，R-C38） |
|---|---|---|---|
| 成因 | 行為由**另一 ECU** 執行 | 行為**可觀察**，但其規範內容由**另一份 spec** 擁有 | **無外部擁有者**，且其內容**不是介面行為** |
| 條文有無委派字面 | 不必然 | **有**（具名文件／具名硬體控制）| **無** |
| 本 ECU／本 feature 有無可觀察端 | **無**（在別的 ECU）| **有**（只是無獨立於 sibling 之內容可驗）| **無**（不是任何介面上的量）|
| Remarks 之擁有者欄 | 具名該 ECU | 具名該文件（R-C27 首行可見）| **不得填** —— 寫不出擁有者即本類之判準 |
| 解除條件 | 該行為改由本 ECU 執行，或取得其可觀察指標 | 外部 spec 之內容納入本 feature 範圍，或該 leaf 經 037 改寫 | 037 改寫該 leaf 使其具可觀察量，或上游確認其驗證方法非 `Manual UI Testing` |

**三者外觀相同（皆無 procedure），成因不同。** 見到空 procedure 時，
須讀 Remarks 之 marker 方知其類別。

**判別次序**（44 §2 增第四類出口）：

```
條文有無委派字面（see / as per / refer to / 具名文件或節）？
├─ 有 → 委派對象是外部文件，抑或本 spec 之節？
│   ├─ 外部文件        → [BLOCKED-SPEC]（§5.1）
│   └─ 本 spec 之節    → [COVERED-BY]（§5.2a，R-C39）
│                        對象節尚未生成 → 不得先標，該 leaf 記 deferred
└─ 無 → 本 feature 內有無可觀察端？
    ├─ 無              → [BLOCKED-NON-HMI]（§5.2）
    └─ 有              → 不是 BLOCKED，正常生成
```

**037 未產出該 leaf 者不進入本次序**，屬 §5.4 之覆蓋缺口。

**上繳 32 §7.5 之診斷**：次序原本「能告訴我不是前兩類，但它的終點是
『正常生成』，而這一個生成不了」—— 缺的正是本節新增之第四類出口。

### 5.2a `[COVERED-BY]`（R-C39，2026-08-15 裁定）

**適用**：某 leaf 之內容全部委派予**同一 spec 之另一節**，而該節之 leaf
**已於本交付件產出 TC**。

**與前三類之根本差異 —— 不得混用**：

> `[BLOCKED-ECU]`／`[BLOCKED-SPEC]`／`[BLOCKED-NON-HMI]` 三者皆為
> **「本交付件不涵蓋」**；`[COVERED-BY]` 是 **「本交付件涵蓋，但在別的列上」**。
> 標成任何一種 BLOCKED，等於向評閱方宣告一個實際上已被涵蓋的缺口。

| 欄 | 值 |
|---|---|
| `test_procedure` / `expected_result` | **空** |
| `specification_reference` | 該 leaf 自身之 outline，照常填 |
| Remarks | `[COVERED-BY] <涵蓋之 req_id>` ＋ 一句說明。R-C27 首 60 字元內須見該 req_id |
| 其餘 | 依 profile 常規 |

**五項使用條件**（R-C39，缺一即回報停下）：一、委派對象為本 spec 之節；
二、該對象節之 leaf 已產出 TC，具名其 tc_id；三、該 TC 之 `expected_result`
**確實涵蓋**本 leaf 之內容，須**逐句比對並具名**，不得以「兩者述及同一事」
代替；四、扣除委派後無獨立餘留；五、tc_id 經白名單增列（R-C26）。

**第二項未滿足時**（對象節尚未生成）：**不得先標**，該 leaf 記 `deferred`，
於對象節生成後再判。

**lint 之具名回報行須與 BLOCKED 分列** —— 兩者於統計上意義相反：
BLOCKED 是缺口，`[COVERED-BY]` 不是。合併輸出會使 coverage 讀錯。

**目前之 `[COVERED-BY]` 列**：無。
（`SWE1-HVAC-122-02` 之第二項未滿足，記 `deferred`，見 DATA_REQUESTS #32。）

**lint 之豁免為具名回報行，不得靜默跳過**（前例：上繳 06 §2.1 之
`and n != "Comfort Widget"`）。`proc-min-steps` 與 `proc-er-1to1` 對
BLOCKED row 之豁免，每次 lint 皆輸出受豁免之 tc_id 清單，**三類合併輸出**。

### 5.4 不產生 workbook 列者

**16.1、18.2–18.4 四節依 R-C16 為 RD-1 覆蓋缺口項，不產生任何 workbook 列**
—— 與 `[BLOCKED-SPEC]`／`[BLOCKED-ECU]`／`[BLOCKED-NON-HMI]` **皆不同**：
那三者產生 BLOCKED 列，本類**連列都不產**（037 未對其產出需求，故無 leaf
可掛）。不指派 tc_id、不入 coverage 分母、不列 BLOCKED。

**第五項成員（56 §3，2026-08-15）—— `15.1` 之圖表部分**：

| 成員 | 形態 |
|---|---|
| `16.1`／`18.2`／`18.3`／`18.4` | **整節未被 037 引用** |
| **`15.1` 之圖表部分** | **節被引用，而節內之一部分未被引用** |

`15.1`（HVACP11.1）**既是圖表也是行為條文**：其
「the HVAC pop ups displayed will **follow the chart below**」為對照表
（該表為圖片，A-CF23），而「all pop ups should display current state of the
HVAC systems (not the exact pictures below…)」為可驗之行為條文。

**037 已把兩者分開**：其兩個 leaf（`105-01`／`105-02`）**皆屬行為條文之殘餘**，
**圖表本身沒有 leaf**。故該圖表所載之對照（某功能進入／退出 → 顯示哪一個
popup）**無任何 TC 驗證**，且**不得由 TC 作者自行補**（55 §1.1）。

> **此形態須單獨標記**：先前四項皆為「整節未被引用」，本項為「**節被引用，
> 而節內之一部分未被引用**」。**日後以節為單位掃描缺口者，找不到它** ——
> `15.1` 有 leaf、有 TC、在 coverage 分母內，掃描只會看見一個已涵蓋的節。

**本類與 `[BLOCKED-NON-HMI]` 之界線（R-C38 使用條件第二項）**：
差別**不在該 leaf 可不可驗，而在 037 有沒有產出它**。037 產出者若以本類
處置，該 leaf 在工作簿中不留任何痕跡，評閱方比對 037 與工作簿時它憑空消失
—— 那正是 BLOCKED row 機制存在的理由（可見、可稽核的缺口，而非無聲的）。

新增 marker 須先裁決，**生成當下不得自行創造**。

### 5.5 推導欄之重算風險 [ADD]（44 §1，2026-08-15）

**凡「由狀態推導、且會被機器每輪重算」之欄位，新增時須一併檢查其重算方向。**

前例（上繳 32 §1.5）：`data/pending_sibling.tsv` 之 `provisional` 欄。
42 §1 只寫了「`false` 不可被改回 `true`」（避免人工複核被抹除），
**單向不夠** —— 缺的那一側一落地，重建就把 `true` 改成 `false`，
而**那正是 gate 要問問題的那一刻**。機器自己蓋了橡皮圖章，
重新確認永遠不會發生，且 lint 全綠。

| 方向 | 失效樣態 |
|---|---|
| `true → false` | 旗標在該問問題的瞬間自行消失；gate 永遠不問 |
| `false → true` | 人工複核被下一次重建抹除；gate 永遠無法被滿足 |

**正解為「已記錄之值一律不重算」** —— 只在首次寫入時計算，其後僅由人手變更。

**新增任何推導欄時之三問**：

1. 這個值會不會被下一次重建覆蓋？
2. 覆蓋的那一刻，是不是恰好是它應該被人看見的那一刻？
3. 人改過的值，重建之後還在嗎？

第 2 問是關鍵：**推導欄之危險不在它會變，而在它變的時機
往往正好是它該被凍住的時機。**

## 6. 寫回與交付完整性 [繼承 Privacy §9 ＋ 跨 feature 條款]

- `features/comfort/BASELINE.sha256`（來源檔，tracked）與
  `DELIVERY.sha256`（append-only，tracked）；每次 session 開啟與 batch gate
  以 `shasum -a 256 -c` 驗，任何 `FAILED` 停工
- **R18-3**：`backend/xlsx_surgical.py` 為唯一寫入路徑；zip member 與 DV
  count 之 invariant 為 **ABORT 級**
- **R20-5**：既有四個 feature 之 `write_back.py` 已隔離，**不得作為起點**
- **R22-1**：hash 稽核為現在式陳述，「相符」不蘊含「未曾被覆寫」

## 7. 不繼承者 [ADD]

| Privacy／SXM 條款 | Comfort |
|---|---|
| Privacy §1.1 ECU 歸屬（tag vs subject） | **不繼承** —— Comfort 之 037 無 ECU 欄，spec_mode 亦不同 |
| Privacy §3.5 `CFTS022-{artifact_id}` | **不繼承** —— Comfort 用 §10.7 預設 filename_section 格式 |
| SXM cite-form（R11） | **不繼承** —— 129 節全數解析成功，無短碼 |
| SXM 吸收機制（R10-2） | **不繼承** —— 覆蓋缺口依 R-C16 走 RD-1 |
| Privacy `[BLOCKED-ECU]` marker | **不繼承** —— 見 §5 |
| revision C 之 Q／S／T–Z 處置 | **繼承**（範本層級，非 feature 層級） |

**其他 feature 之裁決不因類比而適用於 Comfort。** 遇 AMFM／SXM／Privacy
裁決可涵蓋之情形，回 chat 取得 Comfort 之裁決。

## 8. Known anomalies [ADD]

`features/comfort/ANOMALIES.md`，A-CF01 … A-CF13（第四項為 `12.1` 之
`LEDs (.`）。**A-CF07 由 §0.1 處置後可結案** —— 待 Pei 於 Excel 確認四項。
新發現於發現當下登記並具名引用之節次。
