# 09 — 補閘與 Phase 4 首批（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 09
結果：**B1 / B2 / B3 完成；B4（Phase 4 首批 TC）暫停。**
暫停原因為**下放包內容中斷**，非任何閘門或裁決之阻斷。

---

## 一、下放包中斷 —— 暫停 B4 之理由（A-PW39）

09 下放包之內容於 **§B4 句中中斷**。最後一個字元為：

```
  §10.7 `specification_reference` 須列該 TC 直接驗證之全部章節，
        格式 `{spec_filename}_{section_id}`；
        三條皆源自 CFTS010，檔名以 `inputs/`
```

句子未完成。自該處起，以下**全部缺漏**：

| 缺漏 | 影響 |
|---|---|
| §B4 之其餘要求 | 首批 TC 之規格不完整 |
| **§C 抽取規格** | 本包是否沿用或異動未知 |
| **§D 閃點** | **G45 / G46 之期望值未給定**；本包全表未給 |
| §E framework | — |
| §F Anomaly 異動 | 新增條目之編號與內容未給 |
| §G DATA_REQUESTS | — |
| **§H 作業指示** | **步驟清單完全缺漏** |
| **§I 禁區** | **含「不得寫回 FW036 workbook」等一貫禁令，本包無** |
| §J 自檢清單 | 無法對照 |
| 「依其 §H 執行」之指示 | — |
| 「上繳包必附」清單 | 本上繳包之必附項目未知 |

### 執行層之處置

**§A 之七條裁決條文完整無缺**（區塊數實測 = 7，與 §A 末句「以上七條」相符），
已逐字抄入 `RULINGS.md`。

依前八包一貫之原則 —— **不得自行猜測下放內容**（01 包 §-1.C、02 包 §I、
05 包 R-P36 一脈相承）—— 執行層**未補寫任何缺漏章節**。

執行範圍因此限於**規格完整者**：

- **B1（補閘 G45 / G40 改寫 / G46）** —— 規格完整，已完成
- **B2（`feature.yaml` 更新與盤點）** —— 規格完整，已完成
- **B3（R-P62 加註）** —— 註記文字逐字給定，已完成
- **B4（首批 3 條 TC）** —— **暫停**

### 為何 B4 不宜「照現有資訊先做」

§B4 已給之四項（Test Set、tc_id、priority 判定來源、spec_reference 格式）
確實足以起草，但：

1. **§I 禁區完全缺漏。** 前八包每包皆有，且含「不得寫回 FW036 workbook」——
   本包是第一次產出 TC，正是最需要禁區明確的一包。
2. **§D 閃點未給。** 首批 TC 之驗收標準不明；R-P71 要求「上繳前以真實檔案
   執行完整 lint 並回報」，但通過標準未定義。
3. **§B4 之句子在 `specification_reference` 的檔名規則處斷掉** ——
   而該欄正是 G45 新閘所驗、且三條 TC 皆須填寫者。
   檔名應用完整檔名、去副檔名、或某種縮寫，無從得知。
4. **本包是八包以來第一次寫 TC。** 先前每一包的教訓（05 包判讀單位、
   07 包 `\b` bug、09 包 `workbook.columns` 錯位）都指向同一件事：
   **在規格不完整處自行補值，錯誤會沉默地一路帶下去。**

**請補發 §B4 後半與 §C–§J。** 補齊後首批可立即執行 ——
R-P65 之三項開始條件已齊備，阻斷者純為下放內容不完整。

---

## 二、B1 —— 補閘（R-P66 / R-P68 / R-P69(c)）

`scripts/lint_tcs.py` 現含**七閘**。`--self-test` 之
**22 個 TC fixture ＋ G46 全數如期**（全為合成，未讀 `generated/`）。

### 2.1 G45 —— §10.7（R-P66）

`check_s107_spec_reference`：`specification_reference` 非空；
每項須符 `{spec_filename}_{section_id}`，其中 `section_id` 為點分隔數字串；
多項以 `;` 分隔。

| fixture | 期望 | 實際 |
|---|---|---|
| 非空且形態正確（`CFTS010_1.7.1.1.1; CFTS010_1.7.2`） | （無） | （無） |
| 為空 | `§10.7` | **`§10.7`** |
| 形態不符（`see the power down chapter`） | `§10.7` | **`§10.7`** |

> **一項附帶效果須登記**：G37 之第二個 fixture（`specification_reference`
> 引用 `SWE-PM-089`）在 G45 上線後**同時觸發 §10.7** ——
> 因 `SWE-PM-089_source_pending` 之 section_id 非數字串。
> 二閘皆觸發為正確行為，該 fixture 之期望值已改為 `["R-P1", "§10.7"]`，
> 並於程式碼註明理由。

### 2.2 G40 改為子集檢查（R-P68）

原實作僅於 `len(leaves) == 114` 時比對分布。已改為三項：

| 項 | 實作 | 有效範圍 |
|---|---|---|
| (a) 上界 | 各 Test Set 之已產出 leaf 數 ≤ 定版數 | **每批皆驗** |
| (b) 逐 leaf | 歸屬須符 `leaf_testset.tsv` | 每批皆驗 |
| (c) 相等 | 114 齊備時驗完全相等 | 齊備時 |

**新增 fixture 證明 (a) 攔得下原讀法攔不下之情形**：

| fixture | 期望 | 實際 |
|---|---|---|
| 部分批次（3 條 `Power Down`），未達上界 | （無） | （無） |
| **整批一致地歸錯**（4 個 leaf 全記 `Power Down`，定版僅 3） | `R-P35` | **`R-P35`** |

訊息：`Test Set 'Power Down' 已產出 4 個 leaf，超過定版之 3`。

### 2.3 G46 —— `feature.yaml` 一致性（R-P69(c)）

驗 `spec_mode` / `test_group` / `tc_id_format` 三值與裁決條文一致，
並偵測殘留之 scaffold placeholder（`<...>`）。

**首次執行 FAIL**（feature.yaml 尚未更新）→ B2 更新後 **PASS**。
即該閘已實測「確實可能失敗」，非不可能失敗而標 PASS。

---

## 三、B2 —— `feature.yaml` 更新與盤點（R-P69(a)(d)）

### 3.1 已更新之欄位

| 欄位 | 原（scaffold） | 現（依裁決條文／實測） | 依據 |
|---|---|---|---|
| `spec_mode` | `"A"` | **`"D"`** | R-P9 / R-P3′ |
| `test_group` | `"Power"` | **`"Power Management"`** | R-P2 |
| `paths.*` | 全為 `<placeholder>` | **七份素材之實際檔名** | 02 包 §二台帳 |
| `tc_id_format` | **無此欄** | **`"NR1L-PowerManagement-{NNN}"`** | R-P2 |
| `spec_reference_template` | `"<Spec Filename>_{outline}"` | `"{spec_filename}_{section_id}"` | §10.7 / G45 |

### 3.2 盤點 —— **`workbook.columns` 自 `priority` 起全部錯位（A-PW37）**

實測 FW036 之 r9 表頭，與 scaffold 值逐欄對照：

| 欄位 | scaffold | **實測應為** | 該 scaffold 欄位實際是什麼 |
|---|---|---|---|
| `req_id` | D | D | ✓ 相符 |
| **`tc_id`** | **無此欄** | **F** | scaffold 完全沒有這一欄 |
| `test_group` … `tc_ref_id` | G–O | G–O | ✓ 相符（九欄） |
| **`priority`** | **P** | **Q** | P 實為 `Estimated Test Time` |
| **`design_method`** | **Q** | **S** | Q 實為 `Test Case Priority` |
| **`functional_safety`** | **R** | **T** | R 實為 `Estimated Test Time`（第二個） |
| **`author`** | **Z** | **AB** | Z 實為車型欄 `Toro(2261) Atl-Mi` |
| **`remarks`** | **AH** | **AI** | AH 實為 `Defect ID` |

**成因**：本 workbook 之 r9 有**兩個** `Estimated Test Time` 欄（P 與 R，
標頭字串逐字相同）。Privacy 之 **A-PV13 / R39-2** 曾記錄 Revision C 於 Q 插入一欄，
並將 design_method / functional_safety / author 各右移一格（Q→R、R→S、Z→AA）。
**本 workbook 較該修訂版又多插入一欄**，故其後每欄再右移一格。

> **若未查出，Phase 4 寫回會把 priority 寫進預估工時欄、design_method 寫進 priority、
> functional_safety 寫進第二個預估工時欄、author 寫進車型欄（該欄依 R30-3/R30-4
> 應留白）、remarks 寫進 Defect ID 欄。**

登記為 **A-PW37**；兩個同名欄之情形另登為 **A-PW38**。

### 3.3 其餘欄位之盤點

| 欄位 | 現值 | 與實測之相符情形 |
|---|---|---|
| `workbook.sheet` | `"Test Case Specification&Result"` | **相符**（03 包 G12 實測） |
| `workbook.header_row` | `9` | **相符**（03 包 G12 實測 r9） |
| `done_region.detection` | `"author"` | 語法有效，惟 workbook 為 BLANK（G10），**無 done region 可保護** |
| `done_region.author_value` | `"Arif"` | **可疑** —— 為 scaffold 樣板值。Comfort 於同情形刻意留空並註明：填佔位作者值會靜默匹配零列，使空的 invariant 看起來像已滿足。**本包未改**（無裁決依據），見 §五第 2 項 |
| `done_region.invariant` | `"content_hash"` | 語法有效，BLANK 下不適用 |
| `write_back.author_value` | `"PeiPYHsu"` | 未驗（Phase 4 寫回時始生效） |
| `write_back.fill_test_group_set` | `false` | **與 canon §2 不符之嫌** —— 註解自稱「true only under BLANK」，而本 workbook 實測即為 BLANK（G10）。**本包未改**，見 §五第 3 項 |
| `lint.design_method_source` | `"dropdown_sheet"` | **相符** —— 02 包實測 `下拉選單!A1:A9` 九詞條 |
| `lint.popup_ids` / `extra_rules` | `[]` | 未驗 |

---

## 四、B3 —— R-P62 加註（R-P66）

依 R-P36，**原文一字不改**，於 R-P62 之下新增註記段落。

| | SHA256 |
|---|---|
| 加註前 | `ed8fe3a5b6e889a5989f55a4e1001a6303c5fa294c7b9d0509a53882e03b91a1` |
| 加註後 | `ed8fe3a5b6e889a5989f55a4e1001a6303c5fa294c7b9d0509a53882e03b91a1` |

**UNCHANGED PASS。** 註記全文即 §B3 所逐字指定者。
加註逐處獨立完成、未共用任何預先算好之偏移量（06 §六之教訓）。

---

## 五、獨立判斷：本包是否仍有該驗而未驗者

> **本上繳包之「必附項目」清單隨 §C–§J 一併缺漏**，
> 故本節依前八包之慣例自行編列。

### 新增未驗項（五項）

**1.（最重）`workbook.columns` 之錯位是靠「盤點」偶然查出的，不是靠閘門。**
   R-P69(d) 要求盤點，我照做才發現。但**若 09 包沒有要求盤點，這個錯位會一路
   帶到 Phase 4 寫回**，而寫回是不可逆的（會動到交付用的 FW036）。
   G46 只驗三個值（`spec_mode` / `test_group` / `tc_id_format`），
   **不驗 `workbook.columns`** —— 因為 lint 的權威值裡沒有欄位對應。
   **應補設一閘：`workbook.columns` 之每個欄位字母須與 FW036 r9 之實測標頭相符。**
   這是可完全機械化的，且是 Phase 4 寫回前的最後一道防線。

**2. `done_region.author_value: "Arif"` 未處置。**
   §3.3 已指出這是 scaffold 樣板值，而 Comfort 在同樣的 BLANK 情形下**刻意留空**
   並註明理由（填佔位作者值會靜默匹配零列，讓空的 invariant 看起來像已滿足）。
   Power 的值是一個具體人名，**若 Phase 4 之 done-region 偵測跑起來，
   它會匹配零列並回報「invariant 已滿足」**。這正是 Comfort 註解所警告的失敗形態。
   本包未改（無裁決依據，且 R-P69 只點名四項）。

**3. `write_back.fill_test_group_set: false` 與其自身註解矛盾。**
   註解寫「true only under BLANK per canon §2」，而本 workbook 實測即為 BLANK（G10）。
   若 canon §2 之意為「BLANK 時應填 Test Group / Test Set 欄」，
   則此值應為 `true`。**本包未改** —— 我未讀 canon §2 原文，不確定其語意方向。

**4. G45 之 `section_id` 形態假設未經真實資料驗證。**
   我把 `section_id` 定義為「點分隔之數字串」（`1.7.2`、`1.7.1.1.1`），
   依據是 CFTS 之章節號形態。但 §B4 在說明檔名規則時斷掉，
   **`{spec_filename}` 的實際寫法未知** —— 是完整檔名、去副檔名、
   或某種縮寫，會直接決定 G45 的通過與否。目前 fixture 用的是我猜的
   `CFTS010_1.7.1.1.1`。若真實格式不同，**G45 會把每一條合法 TC 都判 FAIL**。

**5. 七閘全部仍只在合成 fixture 上驗證過（R-P71 未能執行）。**
   `generated/` 不存在，故 R-P71 之「以真實檔案執行完整 lint」無從進行。
   該義務已移轉至首批實際產出之包次，未落空 ——
   但這意味著 **09 包新增的 G45 / G46 / G40 改寫也同樣未經真實資料考驗**。
   07 包的 `\b` bug 是「邏輯看似正確而實際不觸發」；
   §五第 4 項的風險則是反向的「邏輯正確但假設錯，導致全部誤殺」。

---

## 六、禁區遵守聲明

> **本包之 §I 禁區隨下放包一併缺漏。** 執行層依前八包一貫之禁令自我約束，
> 逐項回報如下。

| 禁區（沿用 08 包） | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | **未寫回**。B2 之欄位盤點僅以 `read_only=True` 讀 r9 表頭 |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補 |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改 |
| 不得修改任何已落檔裁決條文之內文（R-P36） | R-P62 加註以雜湊證原文未變 |
| 不得測試未被引用之錨點（R-P42） | 本包未產生任何 TC |
| 不得解析任何 RTF 或 OLE stream 之內容 | 未讀任何 RTF 或 OLE stream |
| 不得續行章節層反向缺口調查（R-P37） | 未做任何章節層量測 |
| 不得變更 §E 之分布數字（R-P35） | 63/24/16/8/3 未動 |
| 不得以 A-PW29 之存在逕行填寫車型欄（R-P54） | 未填；`feature.yaml` 之註解已註明 U–AA 依 R30-3/R30-4 留白 |
| 不得調整 `MIN_FINGERPRINT`（R-P62） | 維持 40 |
| 不得以 repo 現況作為 fixture 之測試對照 | 22 個 fixture 全為合成 |
| **本包不撰寫任何 TC** | **未撰寫** —— B4 暫停 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

**另自我約束一項**：`feature.yaml` 之修改雖由 R-P69(a) 明令，
但我只改了 R-P69 點名之四項＋盤點所查出之 `workbook.columns`（A-PW37）。
**§五第 2、3 項（`done_region.author_value`、`fill_test_group_set`）雖同樣可疑，
未改** —— 無裁決依據者不動。

---

## 七、待裁

- **Q1（阻斷 Phase 4）請補發 09 下放包之 §B4 後半與 §C–§J。**
  補齊後首批可立即執行；R-P65 三項條件已齊備。
- **Q2（最重，Phase 4 寫回前必須解決）§五第 1 項：
  應補設 `workbook.columns` 與 FW036 r9 實測標頭之一致性閘。**
  本次錯位是靠盤點偶然查出，非靠閘門；寫回不可逆。
- **Q3 A-PW37 之更新請覆核**（priority Q / design_method S / functional_safety T /
  author AB / remarks AI，＋新增 `tc_id: F`）。
- **Q4 A-PW38：FW036 r9 有兩個標頭逐字相同之 `Estimated Test Time` 欄**（P 與 R）。
  何者為權威、另一者是否留空？是否向上游回報為 workbook 缺陷？
- **Q5 §五第 2 項：`done_region.author_value: "Arif"` 是否改為留空**
  （Comfort 於同情形之作法與其理由）。
- **Q6 §五第 3 項：`write_back.fill_test_group_set` 與其註解矛盾**，
  BLANK 下應為 `true` 或 `false`？
- **Q7 §五第 4 項：`specification_reference` 之 `{spec_filename}` 實際寫法為何？**
  G45 之形態檢查繫於此；若我猜錯，該閘會把每一條合法 TC 都判 FAIL。
  此項於 §B4 之斷句處，屬 Q1 之一部分但影響最直接。
