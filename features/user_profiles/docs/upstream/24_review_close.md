# 上繳 24 — 40 條覆核之修正、需求單位判準、A-UP11 降級

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`24_review_close.md`（**無裁決條文**）；23 包之 M-1～M-5／M-7 已於前一輪完成
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）；**第三批未開**
- 語料：**78 條，未變動**（本輪未生成 TC）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 78 條，**違規 0** |
| `lint_tcs.py --self-test` | 56 / 56 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 78 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3／K-4a／K-4b 各 **0 處** |
| `audit_consistency.py --self-test` | **20 / 20**（＋2 案，見 §3.2）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | **紅 0 ／ 黃 8** ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |

```
priority 分布：P0×24, P1×21, P2×30, P3×3   （P-1 之對調：24 不變、22→21、29→30）
```

---

## 1. P-4（先辦）—— **Description 為需求單位**；六條**不重生成**

### 1.1 判準

> 037 之一個 leaf，其**需求內容以 `Description` 欄為準**；
> `Title` 欄為人為擬定之**索引標籤**，不是需求單位。

19 輪已依此生成七條，但當時只寫「單位之內容以其 Description 為準 ——
標題不是內容」，**未給證據**。本輪補上，落 `DECISIONS.md` **D-UP24-01**
與 profile §1.1。

### 1.2 證據（180 leaf 全量實測）

| # | 量測 | 結果 |
|---|---|---|
| 1 | Description 以 spec **條款編號**起首（`EDPR1.)`／`PVAL8.)` …）| **105 / 180** |
| 2 | **Title 以條款編號起首** | **0 / 180** |
| 3 | Description 前 60 字元**逐字**見於該節 `pdf_text` | **120 / 180** |
| 4 | 對節文之詞彙涵蓋率（平均）| Desc **0.859** ／ Title **0.667** |
| 5 | 逐 leaf 比較 | Desc 較高 **130** ／ Title 較高 29 ／ 平手 21 |

**第 1、2 項是決定性的**：Description 常常**就是條文本身**（連條款編號一併帶入），
Title 則**無一條**如此。兩者不是同一種東西 —— 一個是內容，一個是標籤。

### 1.3 **決定性論證：只有 Description 能分割條文**

以 A-UP11 之現場（12.8 / PVAL8）驗之。該條文有六個斷言，
四個 leaf 之 Description **恰好無重疊、無缺漏地分割它**：

| leaf | 其 Description 所取之斷言 |
|---|---|
| `125-01` | 只有 HVAC／Media 可用 ＋ Media 內 Device Manager 鎖住 |
| `125-02` | Projection／native HFP 停用 ＋ VR 不啟用 ＋ 五個區域鎖住 |
| `125-03` | 狀態列互動受限（僅 Valet Profile 與 HVAC 圖示例外）|
| `125-04` | 所有不可互動項變灰 |

**若改以 Title 為單位，同一組 leaf 會同時產生缺漏與重複**：

- `125-03` 之 Title 為 `Glove Box Lock Prompt on Valet Mode Entry` ——
  **PVAL8 通篇沒有手套箱**（手套箱屬 12.8.1）。
  即該 Title 所指之物**與該 leaf 自己的 `outline` 相衝。**
- 於是 PVAL8 之「狀態列互動受限」**將無任何 leaf**，
  而手套箱提示會**同時有兩個**（`125-03` 與 `126-01`）。

**一個需求單位不可能指向不屬於自己章節的行為。Title 會，Description 不會。**

### 1.4 六條之判定：**`TC-057`～`TC-062` 不重生成**

六條皆依 Description 生成，而 Description 即需求單位 ——
**24 包所慮之「驗的可能不是該 leaf 所指者」不成立**。

其 **TC 標題**由執行層依 Description 另擬（19 輪即如此），
**未沿用 037 之錯位標題**，故無標題誤導之殘留。

### 1.5 A-UP11 **降為記載瑕疵，但不關閉**

- 錯位仍在 037 內，**未修**（素材不得改，§8.2）
- **任何以 `Title` 為索引找 leaf 的人，在 12.8／12.8.1 仍會找錯**
- 範圍已由 23 輪之全量掃描確認為**僅此七個 leaf**，不及於其他 173 個
- 是否回報上游修正 037 之標題欄，屬 Pei 之裁定

### 1.6 盲區（R-G11）

**29 個 leaf 之 Title 涵蓋率高於 Description** —— 多為 Description 係
split leaf 之改寫者（如 `001-01`：`system shall store all profile-linked
preferences listed in PLP table.`）。本判準對它們仍成立（改寫者仍是需求內容），
**但第 3、4 項證據對它們較弱** —— 那 29 條之 Description 不是逐字條文，
其正確性倚賴 037 作者之改寫，而非可機器複驗之逐字對應。

---

## 2. P-1 —— **依建議調整**，且 24 包之推論比我原先的更強

### 2.1 調整

| tc_id | 前 | 後 |
|---|---|---|
| `062`（126-02，變灰）| P0 | **P2**（同 `060`）|
| `063`（126-03，按下不生效 ＋ PU0833）| P1 | **P0** |

**21 輪之 K-1 判反了。** 其理由為「變灰即該防線之執行手段 —— 未變灰則按下可解鎖」，
而 canon §8.7.4 逐字：

> `A visual state (greyed-out, dimmed) does NOT imply non-operability`

**變灰是指示，不是機制。** 一個變灰、按下卻仍解鎖之實作，`062` 會通過 ——
它證不了手套箱鎖得住。

且與 D-UP16-01 附二方向相反（防護本身 → P0／其呈現 → P2），
又與同形之 `060`（不可互動項變灰，P2）不一致 —— **同形不同級**。

### 2.2 一項連帶更正：**判級取核心斷言，不「取中」**

21 輪對 `063` 寫「ER1 為防線、ER2 為回饋，兩者各半，**取中**」而判 P1。
**「取中」本身就是錯的做法** —— 一條 TC 之判級取其**核心斷言**，
不取各 ER 之平均。`063` 之核心斷言是 ER1（按下不生效、鎖定狀態未變），
ER2 是它的呈現面；**不因與呈現併於一條而拉低判級**。

該判準已寫入 profile §3.1（與 §8.7.4 之交互一併）。

### 2.3 佐證：手套箱「真的鎖上」由誰驗

順帶查證 P-1 之推論在語料上是否成立 —— **成立，且更強**：

| TC | 節 | 其斷言 |
|---|---|---|
| `061` | 12.8.1 | PU0832 提示（呈現）|
| `062` | 12.8.1 | 按鈕變灰（呈現）|
| `063` | 12.8.1 | **按下不生效、鎖定狀態未變**（防護）|
| `064` | 12.8.2 | ER2 **`Valet Mode is active and the glove box is locked`**（防護，實體狀態）|

**「手套箱實際鎖上」之唯一斷言在 `064` 之 ER2** —— 而 `064` 屬 12.8.2。
`062` 在此四條中**是唯一完全不觸及實體狀態者**。判 P2 與此一致。

（附帶確認：PVAL8.1 首句 `Valet Mode will enable "electronic" Glove Box Lock`
**有覆蓋** —— 由 `064` 之 ER2 承擔，非缺口。）

---

## 3. P-2 —— `TC-070` 之 ER3 收斂

### 3.1 改法

| | |
|---|---|
| 前 | `Valet Mode is still active and **any popup that would allow an exit is blocked**` |
| 後 | `Valet Mode is still active and **the PU0934 exit popup is not shown**` |

「所有入口皆被阻擋」之全稱移入 reasoning，不入 ER。

**加一層 24 包未點出的理由**：13.2 逐字為
`Any screens or popups that may allow a user to exit Valet Mode must be
blocked (**PU0934, etc**)` —— **`etc` 本身即表示 spec 未列盡該集合**。
**spec 沒列盡的東西，ER 不可能驗得完** —— 全稱斷言在此不只是超出 procedure，
是超出**條文自己所能界定的範圍**。

### 3.2 **本改動使 K-4a 轉紅 —— 而紅的是判準**

收斂後 `TC-070` 之 design_method（負向測試）立刻被 `audit_consistency` 判紅：
其 ER 側詞表要求 `is blocked` 之類的明說，而該詞正是我剛移除者。

複核：**`TC-070` 仍是負向測試** —— procedure 步驟 1
`Press the Valet Profile icon in the status bar` 正是對一個**不該生效之操作**
的嘗試，ER1 `does not open a deactivation flow` 即該嘗試**無作用**。
漏的是「嘗試後無作用」這種 ER 措辭。

**判準補之（v3），且刻意不放寬到一般缺席斷言**：
只加 `does not open`／`does not initiate`，**不加 `no X is shown`** ——
否則 `TC-047` 那種「到兩個地方看，那裡沒有該控制」會被誤收為負向測試，
而那條在 21 輪剛被判為功能測試。

方向性案例補兩條（18 → **20**）：
「嘗試後無作用 → 須綠」與「**純缺席斷言 → 仍須紅**」。
**後者是護欄** —— 它守住這次放寬沒有溢出。

---

## 4. P-3 —— `TC-072`：**改 remarks，不補列 12.6**

### 4.1 所擇與理由

**改 remarks。** 補列 12.6 會**立刻被 G17 判為多引** ——
19 輪之 G17 首跑正是以此擋下 12.6（見上繳 19 §4）：
J-10 要求「登記之節其 `provides` 字面值須真的出現在該 TC 內」。

本 TC 之 procedure **只走 welcome popup 之「Exit Valet Mode」按鈕這一路**，
未走狀態列 Profile 鍵那一路；而 12.6（PVAL6）所述之詢問 popup 屬**後者**，
其字面值不在本 TC 任何欄位內。

### 4.2 這處矛盾之成因值得記

**19 輪把引用欄改對了，卻沒同步改 remarks。**
於是「複位到 12.3.1 與 12.6，故併列該二節」這句話，
在 12.6 被移出引用欄之後仍留在原地 ——
**同一條 TC 內兩處記載互相矛盾，形狀與 C-2 完全相同**
（18 輪之文字說「無界前基準線」而 `design_method` 欄掛 BVA）。

**C-2 之教訓是「改一處就要掃同一條的其他記載」，而本處正是同一個教訓的再犯。**
現行 `audit_consistency` 之 K-4a／K-4b 只掃 `design_method` ↔ 形態、
`priority` ↔ `basis` 兩組 —— **不掃 `remarks` ↔ `specification_reference`**。
已列 §6 待驗項。

---

## 5. 23 包之 M-1～M-5、M-7（照原指示，前一輪已完成）

| 項 | 狀態 |
|---|---|
| M-1 profile 檔補建 | 已完成 —— `FW036_R1L_UserProfiles_Profile.md`，**本輪再增 §1.1（需求單位）與 §3.1 之 §8.7.4 交互** |
| M-2 委派指名 leaf ＋ 三閘 | 已完成 —— 紅 0 黃 7；**本輪新增之 `062` reasoning 一度違反 D-1**（寫「由 126-03 承擔」），已改為完整 leaf id |
| M-3 覆寫母體擴掃 | 已完成 —— 6 axis，`--check` 一致 |
| M-4 `TC-077` 前提具名 ＋ RD #6 | 已完成 |
| M-5 `9.1.1` 另一側 → RD #7 | 已完成 |
| M-7 `23_review_pack_35.md` | 已完成（864 行 / 35 條）|

**M-2 之閘在本輪立刻抓到我自己的新違規**，值得記一筆：
`062` 之新 reasoning 我寫「防線本身由 **126-03** 之 ER1 承擔」——
`126-03` 不是合格之 leaf id，D-1 判紅。**閘在同一輪內就攔下了立閘者本人。**

改為完整 leaf id 後，該句落**黃**（其委派句無 ≥3 詞英文詞串，D-3 之盲區 1），
黃清單由 7 增為 **8**。人工判讀：`SWE1-HMI-PROF-126-03` 之 Description 為
「按下已變灰之手套箱鎖按鈕時系統須阻擋該動作並顯示 PU0833」——
**委派成立**。

---

## 6. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **`remarks` ↔ `specification_reference` 無一致性閘** | **本輪之自陳缺口** | P-3 之矛盾與 C-2 同形，而現行 K-4a／K-4b 掃不到它。**同一形狀已出現兩次** |
| 2 | **A-UP13 之三個行為仍無 TC** | 承前（23 輪）| 記載已更正，**覆蓋未補**；23 輪具名延後，本輪未變 |
| 3 | **`TC-074`～`078` 仍未經覆核** | **分析層待辦** | 24 包載其覆核用全文尚未產出 —— **實已於 23 輪之 `23_review_pack_35.md` 產出**（含該五條）。未讀者為 **5 條** |
| 4 | **判級「取核心斷言」之判準無閘** | 判準盲區 | §2.2 之更正寫入 profile，**但「一條 TC 之核心斷言是哪一個 ER」不可測** —— 靠人工 |
| 5 | **P-4 之 29 條弱證據 leaf** | 判準盲區 | §1.6：Description 為改寫者，其正確性不可機器複驗 |
| 6 | **`pending` 兩個 axis 未兌現** | 待第三批 | 絆線已設 |
| 7 | **D-3 之 8 處黃仍靠人工** | 判準盲區 | 承 23 輪；本輪新增之 `062` 一句亦落黃，已人工判成立 |
| 8 | A-UP09／R-U14、DR #3–#7、R-U17、N-XF01、A-UP10 | 承前 | 擋 Phase 6 寫回 |

---

## 7. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch02.py`（P-1 判級與兩條 reasoning、P-2 之 ER3 與 reasoning、P-3 之 remarks）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（K-4a v3 ＋2 方向性案例）| 否 |
| 3 | 檔案追加 | `DECISIONS.md`（**D-UP24-01**）、`ANOMALIES.md`（A-UP11 降級補記）| 否 |
| 4 | 檔案編輯 | `docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md`（§1.1、§3.1 之 §8.7.4 交互、§4 之 A-UP11 列）| 否 |
| 5 | 檔案重生成 ×29 | `generated/`（batch02；**內容變動者 4 條**：`062`／`063`／`070`／`072`）| 否 |
| 6 | 檔案新建 | `docs/upstream/24_review_close.md`（本檔）| 否 |
| 7 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 8 | 程式執行 | 180 leaf 之 title↔desc 全量量測、生成 ×1、全部閘、四支 audit 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`.gitignore`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_pairs.py`、`lint_*.py`、
`audit_variant_pairs.py`、`audit_delegation.py`、`scan_override_notes.py`、
**他 feature 之任何檔**、`docs/fw036/`。

**第三批未開** —— P-4 之前置已解除（判準已定、六條不重生成），
惟 `074`–`078` 之五條覆核仍未完成，依 24 包仍不開。
