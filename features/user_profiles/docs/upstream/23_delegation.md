# 上繳 23 — profile 檔補建、委派可驗化、覆寫母體擴掃

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`23_delegation.md`（**無裁決條文**）
- 另附：`docs/upstream/23_review_pack_35.md`（**M-7 之 35 條覆核用全文**）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）；**第三批未開**
- 語料：**78 條，未變動**（本輪未生成 TC —— 理由見 §2.4）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 78 條，**違規 0** |
| `lint_tcs.py --self-test` | 56 / 56 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 78 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` ／ `--self-test` | K-3／K-4a／K-4b 各 0 處 ／ 18 / 18 |
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ **7 / 7**（＋2 案）|
| **`audit_delegation.py`（本輪新建）** | **紅 0 ／ 黃 7** |
| **`audit_delegation.py --self-test`** | **8 / 8** |
| **`scan_override_notes.py --check`（本輪新建）** | **與 TSV 一致** |

---

## 1. M-1 —— profile 檔補建

`docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md` 已建
（格式參照 Power profile —— 最近之同類，同為 BLANK 工作簿、同為後補之 profile）。

### 1.1 移入者：**只有一條**

| 條款 | 原載體 | 新載體 |
|---|---|---|
| §11 方括號例外 | `DECISIONS.md` D-UP22-01 | **profile §3.3** |

`DECISIONS.md` D-UP22-01 之「記載限制」段已改寫為**權威載體變更**聲明：
條文與理由留檔不刪，但**以 profile 檔為準**，兩者日後分岔時以 profile 為權威。
**自本輪起得聲稱該例外係依 canon §11 之形式所立**（22 輪明言當時不得如此聲稱）。

### 1.2 **其餘八條為「重述」，不是「搬移」—— 這個分野須先講**

23 包要求「其餘 feature 級 OVERRIDE/ADD 條款一併歸位」。
歸位清單已具於 profile §6，此處說明其判準：

> `RULINGS.md` 為 **Pei 裁決之逐字登記**（R19-2：原文貼入，不改寫不摘要）。
> **把裁決條文搬出裁決檔，會使裁決失去其權威載體。**

故 Priority rubric（R-U5＋D-UP16-01 三層釐清）、Test Set 八值（R-U20）、
spec 雙載體（R-U25）、variant label override（R-U35 (c)）、
V-1（D-UP22-02）、workbook BLANK（R-U6）、母體 180／閘值（R-U4／R-U8）
**於 profile 內重述並標明原載體**，裁決檔不動。

**唯一真正移入者是 D-UP22-01**，因為 canon §11 **明文指定** profile 為其載體
（`when the feature profile says so`）——
其餘條款 canon 並未指定載體，重述即足。

### 1.3 判定為**非 profile 條款**者（具名，以便覆核）

| 條款 | 為何不移 |
|---|---|
| D-UP11-01／11-02 | 生成期之**素材處理**判準，非輸出格式規則 |
| D-UP12-01／12-02 | **判讀口徑**（spec 解讀），非 runtime 覆蓋 |
| D-UP16-02／D-UP17-01 之代價聲明 | **盲區聲明** —— 其位置須與被限制之判準相鄰才讀得到；搬走等於讓人讀不到 |
| R-U7／R-U9／R-U12–R-U19 等 | 一次性之 Phase 0/1 流程裁決，非常設規則 |

---

## 2. M-2 —— 委派指名 leaf，三項閘

### 2.1 語料側之改寫（8 處）

| TC | 原（指節）| 現（指名）|
|---|---|---|
| `001` | 「該二 sibling leaf」| `SWE1-HMI-PROF-001-02`／`-03` |
| `005` | 「6.2 之其他 leaf」| **委派刪除**（見 §2.3）|
| `007` | 「7.2」| **委派刪除**（見 §2.3）|
| `009` | 「8.7 之 sibling leaf」| `SWE1-HMI-PROF-073-02`／`-03` |
| `011` | 「該 leaf」| `SWE1-HMI-PROF-090` |
| `028` | 「9.5.2」| `SWE1-HMI-PROF-097` |
| `065` | 「128-03」| `SWE1-HMI-PROF-128-03` |

### 2.2 閘之三項與其**兩次判準修正**

| 閘 | 判準 |
|---|---|
| D-1 | 委派句須指名 leaf id 或 tc_id |
| D-2 | 被指名者存在於 180 母體或語料 |
| D-3 | 被指名者所屬節之 `pdf_text` 須含**自委派句抽出之英文詞串** |

**D-3 之判準改了兩次，兩次都是被自己的方向性案例逼出來的**：

| v | 作法 | 為何倒 |
|---|---|---|
| v1 | 以 `承擔` 為錨之非貪婪回看取句 | 取**最短**前綴，**把剛指名之 leaf id 切在窗外** —— 一批已指名者被誤報為 D-1。**判準把自己要找的東西切掉了** |
| v2 | 切句後以**單詞**比對節文 | `TC-020` → `109` 那一案之三個詞（`support`／`connected`／`profile`）**每一個都在 11.3 之節文裡**（`does not support connectivity`、`The Connected Account line item`）—— **23 包點名要擋下的那一案，v2 判它綠** |
| v3 | 取最長連續英文**詞串**整串比對 | 現行。`support connected profile feature` 不在 11.3 → 紅 |

**v2 之教訓值得單獨記**：差別不在詞，在**詞的組合**。
`does not support connectivity` 與 `does not support the connected profile
feature` 共用三個詞 —— **單詞比對不可能分開它們**。

**另補一次停用詞**：`TC-028` 之委派句唯一英文術語為 `pre-condition`
（方法學詞彙，spec 節文當然沒有），v2 判它假委派。
複核 9.5.2 之節文（`If the active Profile was **not** previously linked…`）
確認該委派**成立** —— **紅的是判準，不是案例**。

### 2.3 **黃清單掃出另兩處假委派 —— 登記 A-UP13**

**這兩處是「黃」抓到的，不是「紅」。** 兩者之委派句都無 ≥3 詞之英文詞串
可比對（D-3 之盲區 1），**本閘不可能判它們紅**；它把兩者列入人工判讀清單，
人工複讀條文才發現委派不成立。

| # | TC | 原委派 | 實況 |
|---|---|---|---|
| 1 | `TC-005`（6.2.1）| 「客製化或刪除後預設 profile 之消失，由 **6.2** 承擔」| 6.2（NOPR1）只述 Welcome popup 與客製化提示，**未述其消失** |
| 2 | `TC-007`（7.2.1）| 「`More Options` 進 Edit Profile tab、選別的 profile 顯示新 popup，由 **7.2** 承擔」| 7.2（PRWEL2）述的是**小型** popup，**其文無 `More Options`** |

**與 A-UP12 之形狀不同**：

- A-UP12 是**互指** —— 兩節各自把那一側推給對方
- A-UP13 是**外推** —— 推給鄰節，而該行為其實出自**本 TC 自己的條文**

`6.2.1` 逐字 `…will remain on the vehicle **until a user customizes or
deletes it**`、`7.2.1` 逐字 `Choosing "More Options" will take user to Edit
Profile tab. If a different Profile is selected, show the applicable welcome
popup…` —— **三個行為都寫在本節裡，卻被推到隔壁**。

**若當初把「黃」設計成「綠」，這兩處會原封不動地留著。**

### 2.4 **三個行為之 TC：本輪不生成，具名延後**

23 包 §M-7 **逐條列舉**了覆核包之組成（`TC-027` ＋ `045`–`073` ＋ `074`–`078`，
共 35 條）。本輪若再生成 2–3 條，**覆核包之母體就與下放包所指定者不同**。

而 22 輪剛立下之聲明是「**補了覆蓋不等於補了覆核**」——
在 35 條尚無人讀過時再加三條未覆核之 TC，**是把同一個問題做大**。

**故：記載已更正（不成立之委派已刪、缺口已具名於 reasoning 與 A-UP13），
覆蓋未補。** 建議下包指示後補生成；若分析層認為應即補，本輪之更正不妨礙。

### 2.5 D-3 之盲區（R-G11）

1. **無 ≥3 詞英文詞串者一律落黃** —— 本閘對它們**無判定能力**。
   現行 7 處黃即此類，已逐條人工複核（見 §2.6）。**黃不是綠。**
2. **命中不等於承擔** —— 節文含該詞串，不代表該節**斷言**了那個行為。
   D-3 是必要條件，不是充分條件。
3. **(b) 類承諾無法由本閘兌現** —— 只能驗那個 leaf 存在，
   不能驗它日後真被生成。兌現靠第三批開批時之複查。

### 2.6 現行 7 處黃之人工判讀 —— **全部成立**

| TC → 目標 | 委派之行為 | 目標節文 | 判 |
|---|---|---|---|
| `001` → `001-02` | 啟用時回復 | `recall stored preferences when profile is activated` | ✅ |
| `001` → `001-03` | 不可用項目跳過 | `If a feature is unavailable… skip storing & recalling` | ✅ |
| `009` → `073-02` | 最少 1 字元 | `The minimum number of characters for a username is 1` | ✅ |
| `009` → `073-03` | 空白計入長度 | `Spaces… must count toward the 12-character maximum` | ✅ |
| `011` → `090` | 行進中選取受限項目 | `If any items listed above are selected while vehicle in motion, a bonk tone…` | ✅ |
| `028` → `097` | 前置未連結 | `If the active Profile was **not** previously linked…` | ✅ |
| `065` → `128-03` | 30 分鐘之長度 | `After the 30-minute lockout period has fully elapsed…` | ✅ |

---

## 3. M-3 —— 覆寫母體擴掃：**真正的漏不在 `**`，在 `kind` 欄**

### 3.1 擴掃結果

以六組語意形態（`Only:`／`not applicable`／`to be replaced with`／`instead`／
`(if applicable)`／`do not show this`）掃 PDF 全 21 頁，**命中 14 處，逐條判讀，未判 0**。
落為 `data/override_notes_m3.tsv`，`scan_override_notes.py --check` 驗其不飄移。

### 3.2 **新入母體者 2 個 —— 而它們不是 `**` 漏掉的**

| axis | 節 | 註記 |
|---|---|---|
| `r1h-cpa-6.1` | 6.1 | `NOPR0.) R1 High Only: this passage is not meant to be implemented…` |
| `r1h-cpa-8.1` | 8.1 | `****NEWPR0.) R1 High Only: this passage is not meant to be implemented…` |

**兩條都有 `**`、也都在 `pdf_starred_notes.tsv` 裡** ——
卻被 07 輪之 `kind` 欄歸為 **`圖／表內標籤`**，於是 V-1 之母體看不到它們。

> **23 包要我擴掃 pattern；擴掃 pattern 救不到這兩條，重新判 `kind` 才救得到。**

V-1 之母體來源已改為本輪之逐條判讀（不再讀 `kind` 欄），**由 4 個 axis 增為 6 個**。

### 3.3 三分法（22 輪之分野，本輪再細一層）

| 判 | 定義 | 入母體 | 本輪實例 |
|---|---|---|---|
| **覆寫** | 依變體／市場指定另一字面值或另一種適用性 | **是** | 6 個 axis |
| **適用條件** | 某配置下不顯示，**未指定替代物** | 否 | `(if applicable)` ×4、5.1.2 之 7 吋排除 |
| **狀態條件** | 條件為**執行期狀態**而非變體 | 否 | 5.2 之 `A text will be displayed instead` |

**第三類為本輪新增。** 5.2 確實是「改顯示另一段文字」——
**但其條件是「達到 5 個 profile」，那是狀態不是變體**。
收進 V-1，它會與一般條件式行為混為一談。
（該行為已由 `TC-003` 覆蓋，其 ER 逐字含 PU0584。）

### 3.4 兩個新 axis 之處置：`pending`，並在閘裡留絆線

`6.1`／`8.1` 之 leaf（`SWE1-HMI-PROF-046`／`065`）**尚未取樣**，
故非「不配對造」而是「**未到**」。`audit_variant_pairs` 新增 `pending` 狀態，
其閘驗兩件事：

1. 該 leaf 在 180 母體內
2. **該 leaf 尚無 TC** —— 一旦第三批生成了它，`pending` 即失效而轉紅，
   須改判為配對或具名不配

**這是為第三批留的絆線**：否則那兩個 R1 High 覆寫會像 `017`／`039`／`013`
當初那樣被寫成前提而無人測。方向性案例已補（+2，共 7/7）。

---

## 4. M-4 —— `TC-077` 之前提具名，送 RD #6

`remarks` 與 `reasoning` 已具名該前提為**推得**：

> spec 未明言「有 `<Brand>` app 之區域、而車輛不支援 connected profile 功能」
> 此一組合存在。若該組合造不出來，本 TC 之情境即無法佈署 ——
> **但條件 2 是條文寫的，TC 不因情境難佈署而刪**（§8.4.1）。

`DATA_REQUESTS.md` 新增 **RD #6**，併 DR #3 送出。
問法即 23 包所指定者；並預先寫明**若答覆為「不存在」之處置**
（remarks 改記為「不可佈署之條文條件」，並轉為上游澄清該條件是否為贅語）。

---

## 5. M-5 —— `9.1.1` 另一側：**037 無對應 leaf，為上游缺口**

以 `leaf_rows()` 全量查證 180 母體：`9.1.1` **僅一個 leaf**
（`SWE1-HMI-PROF-086`，標題 `(8.4") Hide Username/Avatar Left of Edit List`）。
**另一側（大螢幕在清單左側顯示 username 與 avatar）無 leaf。**

**關鍵佐證 —— 037 自己在別處是分兩個 leaf 的**：

| 節 | leaf | 標題 |
|---|---|---|
| 8.8 | `SWE1-HMI-PROF-076-02` | `(8.4"+) Avatar Displayed Above Save & Continue Button` |
| 8.8 | `SWE1-HMI-PROF-076-03` | `(7") Avatar Displayed Next to Save Button` |

**同一份 037，對螢幕尺寸之兩側在 8.8 切了兩個 leaf，在 9.1.1 只切了一個。**
故此非「037 之慣例如此」，而是**該節之覆蓋缺漏**。

登記 **RD #7**，併 DR #3 送出。**不自行補 leaf**（母體為 037 之權威，§8.2）。

---

## 6. M-6 —— A-UP11 全量掃描：**範圍確認為 12.8／12.8.1，不及其他**

### 6.1 偵測器與其自我驗證

A-UP11 之形狀是**標題相對於描述整體位移**。故判準為：
某 leaf 之 `title` 與**他 leaf 之 `desc`** 顯著更合（差 ≥0.25）者即為候選。

**該偵測器在未被告知的情況下，重現了 A-UP11 已知之四條**
（`125-03`／`125-04`／`126-01`／`126-02`）—— 此即其有效性之證據。

### 6.2 全 180 leaf 之結果

近鄰（±4）比對命中 **7 條**：已知 4 條 ＋ **新候選 3 條**。
三條新候選逐條複讀，**皆為偽陽性**：

| 候選 | 最佳匹配 | 判 |
|---|---|---|
| `034-03`（5.10.1）| `034-02` | 兩者同為 PU0588 之分支，共用詞彙；各自標題與自身描述相符 |
| `066`（8.2）| `068` | `068` 之描述含 `New Profile Setup` 字面，屬詞彙巧合 |
| `095`（9.5）| `096` | `096` 之描述為 `095` 之**超集**（9.5.1 較 9.5 詳），非位移 |

另以**全集**比對（拿掉窗寬這個判準參數）另得 4 條遠距命中
（距離 70–129），**皆為詞彙巧合，非位移** ——
位移之特徵是**近鄰**，遠距命中不具該形狀。

另查 `title` 與自身 `desc` 重疊 < 0.2 者 4 條（`002-02`／`002-03`／`025`／`077`），
逐條複讀**皆對齊** —— 低重疊之成因是**標題為改寫而非引用**
（例：`Display Popups for Restoring Settings Progress` ↔ `PU1087`／`PU1088`）。
**低重疊不是位移訊號。**

### 6.3 結論與盲區

**A-UP11 之範圍即 12.8／12.8.1 七條，不及於其他 173 個 leaf。**
該項自 19 輪掛起，**承前四輪，本輪結案**。

**盲區（R-G11）**：偵測器以詞彙重疊為度。
**若某兩 leaf 之標題皆為改寫式（與各自描述重疊本就低），其互換不會浮出。**
本輪已對「低重疊」之 4 條逐條複讀作為補償，但那 4 條是**閾值以下**者，
不等於窮盡。

---

## 7. M-7 —— 35 條覆核用全文

`docs/upstream/23_review_pack_35.md`（864 行，**35 條**）：
`TC-027` ＋ `TC-045`–`073` ＋ `TC-074`–`078`，每條含 spec 原文、
must_carry（若有）與 037 description。

**23 包之記錄照收**：分析層自本輪起以每輪 10–12 條推進，
**不以「閘全綠」推定其內容已讀**。

---

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **A-UP13 之三個行為無 TC** | **PENDING（本輪具名延後）**| 記載已更正，**覆蓋未補**。延後之理由見 §2.4 —— 不因記載更正而視為已處理 |
| 2 | **D-3 對 7 處黃無判定能力** | 判準盲區 | 已逐條人工複核成立（§2.6），但**那是人工，不是閘**。同型之新 TC 仍會落黃 |
| 3 | **`pending` 兩個 axis 尚未兌現** | **待第三批** | 絆線已設（生成即紅），但**絆線不是覆蓋** |
| 4 | **A-UP11 偵測器對「雙向改寫式標題」無感** | 判準盲區 | §6.3 已具名；閾值以下之 4 條已補讀，非窮盡 |
| 5 | **M-3 之 pattern 仍是我列的六組** | 判準盲區 | 本輪證明漏在 `kind` 欄而非 pattern，**但那不證明 pattern 已窮盡** —— 以完全不同措辭表達之覆寫仍看不見 |
| 6 | **RD #6／#7 未送出** | 承前 | 已落檔待併 DR #3；**送出與否非執行層可決** |
| 7 | **35 條之內容覆核仍待分析層** | **分析層待辦** | 本輪只交格式 |
| 8 | **profile 檔之八條「重述」可能與原載體分岔** | **新增風險** | 重述即複本；**現無閘驗兩者一致**。若日後改 R-U5 而未改 profile §3.1，兩處會不一致而無人發現 |
| 9 | A-UP09／R-U14、DR #3／#4／#5、R-U17、N-XF01、A-UP10 | 承前 | 擋 Phase 6 寫回 |

**第 8 項為本輪自陳之新風險**：M-1 要求歸位，而歸位之最安全形式是「移動」；
我選了「重述」以保住裁決檔之權威（§1.2 之理由成立），
**但重述會製造複本，複本會分岔**。
建議下包指示是否為此設一致性閘（形態同 G16 之 `feature.yaml` ↔ 現測）。

---

## 9. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案新建** | `docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md`（**跨 feature 目錄**）| 否 |
| 2 | 檔案編輯 | `DECISIONS.md`（D-UP22-01 之載體變更聲明）| 否 |
| 3 | 檔案追加 | `ANOMALIES.md`（**A-UP13**）、`DATA_REQUESTS.md`（**RD #6**／**RD #7**）| 否 |
| 4 | **檔案新建** | `scripts/audit_delegation.py`（D-1／D-2／D-3 ＋ 8 案）、`scripts/scan_override_notes.py`（M-3 擴掃 ＋ `--check`）| 否 |
| 5 | 檔案編輯 | `scripts/audit_variant_pairs.py`（母體改自 M-3、新增 2 axis 與 `pending` 閘 ＋2 案）| 否 |
| 6 | 檔案編輯 | `scripts/gen_pilot.py`（5 處委派改寫）、`gen_batch01.py`（2 處）、`gen_batch02.py`（1 處）、`gen_pairs.py`（M-4 之具名）| 否 |
| 7 | **檔案新建** | `data/override_notes_m3.tsv` | 否 |
| 8 | 檔案重生成 ×78 | `generated/`（**內容變動者 8 條**：`001`／`005`／`007`／`009`／`011`／`028`／`065`／`077` 之 reasoning 或 remarks）| 否 |
| 9 | 檔案新建 | `docs/upstream/23_delegation.md`（本檔）＋ `docs/upstream/23_review_pack_35.md` | 否 |
| 10 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 11 | 程式執行 | 生成 ×4、全部閘、四支 audit 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。

**跨 feature 之寫入僅第 1 項**（`docs/runtime/profiles/`）——
該目錄為九個 feature 共用之 runtime 層，本檔為 User Profiles 自己的 profile，
**未觸及他 feature 之任何 profile**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`BASELINE.sha256`、`.gitignore`、`scripts/lint_*.py`、
`scripts/render_spec_region.py`、`scripts/build_batch_context.py`、
`scripts/audit_consistency.py`、`data/` 之既有各檔、**他 feature 之任何檔**、`docs/fw036/`。

**第三批未開** —— 依 23 包，待 35 條覆核完成。
