# 上繳 37 — J-15 作業 3 補做、號碼指派檢查、第四批收尾

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`37_j15_and_assignment.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未刪除任何檔**；**未寫回工作簿**；
  **RD v2 未寄出**（Tier 3，屬 Pei）；**第五批未開**
- 語料：**134 條，未變動**（本輪修改 **5 條**之 pre-condition／remarks）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 134 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 134 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` ／ `--self-test` | 十項掃描（見 §5）／ 43 / 43 |
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 14 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |
| **`audit_assignment.py`（本輪新建）** | **違規 0** |
| **`audit_assignment.py --self-test`** | **6 / 6** |

---

## 1. 作業 1 —— J-15 作業 3：11 輪盲區掃描之逐條複核

母體：`DECISIONS.md` **D-UP11-01** 之 17 條命中表。
`134`（第 17 條）已於 19 輪複核並更正，故本輪複核**其餘 16 條**。

### 1.1 逐條回報

| # | leaf | sec | 當時之結論 | 當時之理由 | **複核判定** |
|---|---|---|---|---|---|
| 1 | `001-01` | 4.1 | **是**（指 PLP）| `see list of linked content above` | **結論對、理由對** —— ch3 在 ch4 之前，位置指涉成立 |
| 2 | `001-02` | 4.1 | 是 | 同節同句 | 結論對、理由對 |
| 3 | `001-03` | 4.1 | 是 | 同節同句 | 結論對、理由對 |
| 4 | `014` | 4.6.1 | 否 | 圖（username 圓框示意）| 對 —— 條文逐字 `as pictured above` |
| **5** | **`047`** | **6.2** | **否** | **前段之 default Welcome Popup 流程** | **結論對、理由錯** —— 見 §1.2 |
| **6** | **`066`** | **8.2** | **否** | **8.x 之 New Profile 流程** | **結論對、理由錯** —— 見 §1.2 |
| 7 | `076-01` | 8.8 | 否 | 版面方位 | 對 —— `displayed strictly above the save button` |
| 8 | `076-02` | 8.8 | 否 | 版面方位 | 對 |
| 9 | `076-03` | 8.8 | 否 | 版面方位 | 對 |
| 10 | `078` | 8.8.2 | 否 | 圖（7" 分頁示意）| 對 —— `an example is pictured above` |
| **11** | **`090`** | **9.3.1** | **否** | **Table EDPR1**（行車限制項目）| **結論對、理由錯** —— 見 §1.3 |
| **12** | **`091-01`** | **9.3.2** | **否** | **Table EDPR1 ＋ 9.3.1 之訊息** | **結論對、理由半錯** —— 見 §1.3 |
| **13** | **`091-02`** | **9.3.2** | **否** | 同上 | 同上 |
| 14 | `106` | 10.2 | 否 | 圖（Profile Info Page 截圖）| 對 —— `(see example above` |
| **15** | **`108`** | **10.3.1** | **否** | **頁內之 chart（Nav 等分類範例）** | **結論對、理由不精確 —— 20 輪已精確化**，見 §1.4 |
| 16 | `111` | 11.4 | 否 | Table CPA2 | 對 —— `See table CPA2 for list items` |

**16 條中：理由對 10、理由錯 3、理由半錯 2、理由不精確 1。結論則 16 條全部不變。**

### 1.2 `047`（6.2）與 `066`（8.2）—— 指的是圖，不是條文

**`047`**：條文為
`There will be prompts … within the default Welcome Popup **(see above)**`。
11 輪記其指向「前段之 default Welcome Popup 流程」。

**該理由不成立**：ch6 之前**沒有任何 Welcome Popup 條文** ——
6.1（NOPR0）是 R1 High 之 CPA 註記；而 ch7（`PRWEL`，welcome popup 之專章）
**在其下方**，不可能是 `above` 所指。
其 037 description 另帶 `(image: …)` 標記。
**故其指涉之物為頁內之圖，非條文。**

**`066`**：條文為
`NEWPR1.) See flow for setting up a New Profile above. Connecting an account
… are **not pictured here**.`

**同一句裡的 `not pictured here` 就是證據** —— 被指之 `flow above` 是**圖**。
11 輪記其指向「8.x 之 New Profile 流程（條文）」，不成立。

### 1.3 `090`／`091-01`／`091-02`（9.3.x）—— 指的是 9.3 自己的散文列舉

9.3 逐字：

> `EDPR3.) While vehicle is in motion, the following will be greyed out and
> cannot be selected/completed: **Deleting a Profile, editing username,
> editing avatar, Tutorials, Resume Setup, and viewing info of what is linked
> to a Profile.**`

9.3.1 之 `any items listed above`、9.3.2 之 `any of the above listed items`
所指者即**該句之六項散文列舉**。

**11 輪記為 `Table EDPR1` —— 那是 9.1 之選項順序表，與行車限制無關。**
`091-01`／`091-02` 之理由另含「9.3.1 之訊息」（指 `the message specified
above`）—— **那一半是對的**，故記為「半錯」。

**一項重要之查證**：該錯誤理由**未流入語料**。
`TC-022`（`090`）之 reasoning 逐字為
「受限項目之清單**出自 9.3**，故併列該節」——**寫的是對的**。
`TC-011`／`TC-023` 之 remarks 雖提及 Table EDPR1，
但那是指 **9.3.2 之 R1 High 列級覆寫**（其 `****` 標於 p14 之 Table EDPR1 該列），
**與本處之指涉是兩件事，且該記載正確**。

> **故：錯的只有 D-UP11-01 那張表裡的三格，TC 本身沒有受影響。**

### 1.4 `108`（10.3.1）—— 理由不精確，20 輪已精確化

11 輪記為「頁內之 chart（Nav 等分類範例）」——**方向正確但未複位**。
20 輪 C-1 以 `render_spec_region.py --table` 將其精確複位為
**PDF p16 之 Table PIP1「Profile Info Display Text」（15 列）**，
並逐列補入 `TC-039` 之 ER。**本輪不另行改述**，僅記其已被精確化。

### 1.5 改述之落點

依 36 輪 R-2 之先例（**加註，不刪原文**），
`DECISIONS.md` D-UP11-01 之表**保持原樣**，另加一段
「37 輪 J-15 複核之更正」，逐條列出上述五處之正確指涉。

**理由錯而結論不變者亦具名** —— 37 包明令。

---

## 2. 作業 2 —— 號碼指派檢查（`audit_assignment.py`）

### 2.1 成因

36 輪之兩處指錯，**成因是生成器之 `remarks` 先寫、`tc_id` 後指派**，
而兩者之間沒有任何檢查。Y-1 抓得到跨 leaf 群者，抓不到同群內指錯。

### 2.2 三項檢查

| # | 檢查 | 性質 |
|---|---|---|
| **A-1** | **號碼指派表**（自生成器之取樣清單與 `TC_START` **重算**）與 `generated/` 之 `tc_id`↔`req_id` 相符 | 紅 |
| A-2 | 文內**同句同時出現** `tc_id` 與 leaf id 者，兩者須在指派表中對應 | 紅 |
| A-3 | 文內提及之 `tc_id` 須存在於指派表 | 紅 |

**A-1 是地基**：指派表**不讀 `generated/`**，而由六支生成器之
`SAMPLE`／`sample()`／TSV ＋ `TC_START` ＋ `EXTRAS` 重算。
**若兩者不符，代表產物與生成器已分岔** ——
那種情形下，任何以產物為據之檢查都不可信。

### 2.3 **首跑結果：綠（違規 0）** —— 依 37 包，不論紅綠皆回報

| 項 | 值 |
|---|---|
| 號碼指派表 | **134 條** |
| 語料 | **134 條** |
| A-1 不符 | **0** |
| A-2 不符 | **0** |
| A-3 不存在之號碼 | **0** |

**「0」之意義須說清楚**：36 輪之兩處指錯**已於該輪修正**，
故本檔首跑本來就該是綠的 —— **它證明的是修正確實生效，
不是「從來沒有這種錯」**。

其**擋得住之形狀**由方向性案例證明（**6 / 6**），
其中三條紅向即 36 輪兩處之形態：
`096` 之 `req_id` 被改（A-1）、同句稱 `104`＋`SWE1-HMI-PROF-009`（A-2）、
提及不存在之 `999`（A-3）。

### 2.4 **盲區（R-G11）—— 這一項必須講清楚**

**A-2 只在同句同時出現 `tc_id` 與 leaf id 時才驗。**
而 **36 輪之兩處指錯正是「只寫號碼、未附 leaf id」**：

> `§7 之列舉配對：反向為 `NR1L-UserProfiles-104`（同一座椅位置…）`

**若當時那句附了 leaf id，A-2 會擋下它；沒附，就擋不下。**
已納為護欄案例（「同句只寫號碼而無 leaf id → 綠」）——
**它固化的是本檔之界線，不是它的能力。**

該類由 **Y-1（leaf 群）** 與人工覆核承擔。
**建議**：往後生成器之 remarks 提及他條時，**號碼與 leaf id 併寫** ——
如此 A-2 才有東西可比。本輪未回頭改既有 remarks（範圍過大），具名待裁。

---

## 3. 作業 4 —— 兩項待裁之落地

### 3.1 `TC-003`：維持現狀，remarks 具名核心斷言

依 37 包之裁定（**共用觀察點，非越界**），ER 不改，remarks 補：

> **本條之核心斷言為「數目上限」** —— 最多五個 Driver Profile，
> 外加一個 Valet Mode Profile（`021-01` 之 description）。
> ER1（四個時按鈕在）與 ER2（第五個建得起來）為其**邊界對**；
> **ER3 之其餘三項（按鈕不在／圖示與字串不在／PU0584 顯示）為情境確認，
> 非本條之受測對象** —— 其各自之驗證屬 `SWE1-HMI-PROF-021-02`
> （`NR1L-UserProfiles-115`）與 `SWE1-HMI-PROF-021-03`（`NR1L-UserProfiles-116`）。

**號碼與 leaf id 併寫** —— 即 §2.4 之建議，本條先行套用。

### 3.2 PU0580 四條：pre-condition 指定「已開啟」

| tc_id | leaf | 節 | 新增之 pre-condition |
|---|---|---|---|
| `117` | `022` | 5.3 | `The welcome popup is turned on for Driver Profile B` |
| `119` | `024` | 5.3.2 | 同上 |
| `120` | `025` | 5.3.3 | 同上 |
| `108` | `059-03` | 7.2.1 | 同上 |

理由照 37 包：**未指定則 popup 出現與否不確定，測試結果不可重現**（§2）。
四條之 ER 皆未斷言該 popup —— 其顯示本身由 `SWE1-HMI-PROF-023`
（`NR1L-UserProfiles-118`）驗；本處只需其**狀態確定**。

### 3.3 `(if turned on for that Profile)` 之另一分支 —— **OUT-OF-SCOPE（R-U56）**

查 037 之 180 leaf 母體：**`5.3.1` 只有一個 leaf**（`SWE1-HMI-PROF-023`），
其 description 為 PRACC9.1 之**整句**（含該括號）。

**「關閉時不顯示」之分支無對應 leaf** ——
依 **R-U56**（spec 有內容而 037 未為其產出 leaf 者，不生成 TC、不列覆蓋缺口、
不向上游索取），判為 **OUT-OF-SCOPE**，具名於此，**不列缺口**。

---

## 4. 作業 3 —— 餘 5 條之內容變動（供分析層對照）

37 包要求：若 `109`／`110`／`111`／`122`／`123` 因本輪修正而變動，須具名。

| tc_id | 本輪是否變動 |
|---|---|
| `109`／`110`／`111` | **未變動** |
| `122`／`123` | **未變動** |

**該五條之內容與 `35_review_pack_26a.md`／`26b.md` 所載完全一致，可直接讀。**

**惟本輪變動之五條中有三條在該兩檔內**（`117`／`119`／`120`，皆在 `26a`）——
其 pre-condition 各增一行。`108` 在第三批（`29_review_pack_30.md`），
`003` 在 pilot（無 review pack）。**若分析層已讀過 `117`／`119`／`120`，
其變動僅為新增一條 pre-condition，ER 與 procedure 未動。**

---

## 5. 十項掃描之現況

| 掃描 | 型態 | 現況 |
|---|---|---|
| K-3／K-4a／K-4b／T-1／U-2 | 紅 | **各 0** |
| Y-1（§7 配對之宣稱）| 待判 | 1（`121` → `022`，36 輪已處置）|
| X-1（跨節 popup）| 待判 | 6（35 輪已逐條判）|
| W-1（完成式 pre）| 待判 | 4（33 輪已逐條判）|
| V-1（時序語）| 待判 | 15（32 輪已逐條判）|
| U-1（多觸發 popup）| 待判 | 7（31／34 輪已逐條判）|
| Q-1（引號外之逐字引用）| 待判 | 11 |

**待判項之數目本輪未增** —— PU0580 四條之 pre-condition 屬 X-1 之處置，
**而 X-1 之判準是「procedure 是否處理該 popup」，非「pre 是否指定其開關」**，
故其命中數不變（仍為 6）。**兩者是不同的事，未混為一談。**

---

## 6. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **A-2 之盲區：只寫號碼者驗不到** | **本輪之判準界線** | §2.4 —— 36 輪之兩處正屬此形態。建議「號碼與 leaf id 併寫」，**既有 remarks 未回頭改** |
| 2 | **D-UP11-01 之表未重寫** | 設計選擇 | 依 36 輪 R-2 之先例加註而不刪原文 —— **刪掉就看不出曾經給過錯的理由** |
| 3 | **11 輪判準之盲區未變** | 承前 | 其四項盲區（無指涉字樣、圖內文字、`below`、版面方位偽陽性）於 D-UP11-01 已聲明；**本輪只複核理由，未重跑掃描** |
| 4 | **`047`／`066` 之正確指涉未經版面複位** | **note** | §1.2 之判定依「ch6／ch8 之前無該條文」＋「description 帶 image 標記」＋「`not pictured here`」三項推得，**未如 20 輪之 `108` 那樣以座標複位**。兩者皆未取樣（無 TC），**取樣時應複位確認** |
| 5 | **第四批餘 5 條未覆核** | **分析層待辦** | 內容未變動（§4）|
| 6 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 7 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

---

## 7. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/audit_assignment.py`（A-1／A-2／A-3 ＋6 方向性案例）| 否 |
| 2 | 檔案追加 | `DECISIONS.md`（D-UP11-01 之 J-15 複核更正，**加註不刪原文**）| 否 |
| 3 | 檔案編輯 | `scripts/gen_pilot.py`（`TC-003` 之 remarks）| 否 |
| 4 | 檔案編輯 | `scripts/gen_batch03.py`（`108` 之 pre-condition）、`gen_batch04.py`（`117`／`119`／`120` 之 pre-condition）| 否 |
| 5 | 檔案重生成 ×72 | `generated/`（pilot／batch03／batch04；**內容變動者 5 條**：`003`／`108`／`117`／`119`／`120`）| 否 |
| 6 | **檔案新建** | `docs/upstream/37_j15_and_assignment.md`（本檔）| 否 |
| 7 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 8 | 程式執行 | 11 輪 17 條之逐條複核（讀 `outline_map.json` 之 9.3／6.2／8.2 等節文）、指派表重建與比對、生成 ×3、全部閘、十支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**未刪除任何檔**。**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第五批未開** —— 待第四批餘 5 條覆核完成。

**未動**：工作簿、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、`docs/handoff/`、
`scripts/gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、`lint_tcs.py`、
`lint_variant_labels.py`、`render_spec_region.py`、`build_batch_context.py`、
`audit_consistency.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
