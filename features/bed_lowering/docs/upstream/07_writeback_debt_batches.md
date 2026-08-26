# 上繳包 07 — Bed Lowering Mode：pilot 寫回 + 工程債收斂 + B1 先行預查

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/07_writeback_debt_batches.md`
（sha256 `d4385525dbd8c277cc79043485ba2946ad69b23251856592cf7be6986a8baa2e`）
執行層：Tier 1

**結論：§一～§三完成。寫回 round-trip 差異 0、交付 lint clean、三件工程債全收。
過程中新設之交付 lint 首跑即抓到一個 round-trip 驗不出來的真缺陷（§二-4），
recon 亦揭出兩條與 R-BLM5 結構性衝突之 assertion（§三-3）—— 兩項皆須 Pei 一看。**

---

## 〇、兩件最要緊的

1. **H 欄 test_set 13 列全空，而我的 round-trip 驗證說「差異 0」。**
   抓到它的是新寫的交付 lint，不是 round-trip。原因在 §二-4 —— 這是本包
   最有價值的一件事，因為它證明了為什麼 lint 必須讀工作簿而不是讀 JSON。
2. **`recon.py` 之兩條 assertion 對本 feature 結構性不成立**（§三-3），
   其中一條是我在下放包 02 自己宣告的 `spec_reference_stem`。
   **不自行改綠**，回報請裁。

---

## 一、寫回前之兩處小修

1. 038-04 Pre-Condition 6 已改為可用性狀態句（R-BLM14(3)）：
   `The SYS1 normalised text of NRL-193702 is available to the tester as the wording baseline`
2. manifest 已重 stamp（見 §四）

另補 `feature.yaml` 一鍵：**`tc_id_format: "newR1L-BLM-{n:03d}"`**。
下放包 §二-2 稱「project 前綴依 feature.yaml」，而本檔原無任何 project 鍵。
全案之前綴為 `newR1L`（權威為工作簿 D2 儲存格，本包實測 = `newR1L`；
amfm 交付本之 `newR1L-AMFM-001…143` 為既有實例）。
沿 amfm 之既有鍵名 `tc_id_format`，**不另立 `project:` 裸鍵** ——
真正被讀的是完整格式字串，拆兩鍵會多一個無人讀的鍵（R-VC9）。

---

## 二、pilot 13 條寫回

輸出：`features/bed_lowering/workbook/bed_lowering_01.xlsx`
sha256 `aa1015f24eca883fee64d272b6f0b402091297da8b22dad7c4a65b08a317943e`
來源：`bed_lowering_00.xlsx`（`6372fb6b…825b2`，與 R-G1 母本逐位元相同）

### 2.1 XML 外科式（R-BLM3）

以 `backend/xlsx_surgical.py` 之 `surgical_save`：openpyxl 只作計算層，
emit 層 diff 出儲存格變更後**改 SOURCE 之 sheet XML 文字**，其餘 zip 成員原樣複製。
`verify_structure` 對成員集變動、DV 計數變動、非目標成員差異三者一律 raise。

```
sheets_patched  {'Test Case Specification 測試用例規範': 208}
zip members     48
differing       ['xl/worksheets/sheet6.xml']
dv_counts       {'xl/worksheets/sheet5.xml': (1, 0), 'xl/worksheets/sheet6.xml': (3, 1)}
```

### 2.2 保全計數（上繳 02 口徑，legacy 與 x14 分開計）

| 指標 | 寫回前 | 寫回後 |
|---|---|---|
| zip_members | 48 | 48 |
| sheet_xml / sheets_declared | 9 / 9 | 9 / 9 |
| drawing_rels | 13 | 13 |
| dataValidation (legacy) | 4 | 4 |
| **x14:dataValidation** | **1** | **1** |
| extLst | 3 | 3 |

差異欄位僅 `size` 與 `sha256`。

### 2.3 一個看起來像壞事而不是的現象：檔案變小了

寫回 13 列之後，檔案由 200,650 → **172,578 bytes，小了 28KB**。
加內容而變小值得查，查完是這樣：

| | 未壓縮 raw 總量 | 壓縮後總量 |
|---|---|---|
| 寫回前 | 1,289,942 | 192,550 |
| 寫回後 | **1,316,315** | 166,310 |

- **raw 內容是增加的**，增量 26,373 bytes；
- 而 `sheet6.xml` 之 raw 增量**恰好也是 26,373** ——
  兩數相等即證明 **`sheet6.xml` 是唯一內容改變之成員**，其餘 46 個成員
  raw 逐位元相同。
- 檔案變小純為**重壓縮**：`surgical_save` 用 `zipfile.ZIP_DEFLATED` 預設等級，
  原檔由 Excel 以較低等級寫出，故每個成員壓縮後都小一些。

**附帶一個口徑提醒**：`verify_structure` 比的是 `a.read(m) != b.read(m)`，
即**解壓後**之內容，所以它正確地通過。但若有人用 `cmp` 比兩檔之 zip 條目
原始位元組，會看到 46 個成員「都不一樣」。
**「逐位元複製」在此指成員內容層級，不指 zip 儲存流層級** —— 兩者不同，
查核時要挑對層級，否則會誤報一場大災難。

### 2.4 **H 欄 test_set 全空 —— round-trip 驗不出來的缺陷**

首次寫回後，round-trip 報「13 列 × 15 欄，差異 0」。
**但新寫的交付 lint 首跑就抓到 13 筆 `[A-empty] test_set is empty`。**

成因：`write_back.py` 之 `cell_values()` 原寫

```python
col["test_set"]: tc.get("test_set") if fill else None,
```

而 `pilot_tcs.json` 之 `test_set` **只存在於批次層**，逐條 TC 無此鍵
（實測：`['test_set' in t for t in tcs]` → 全 False）。
`tc.get()` 靜默回 `None`，該欄因而被過濾、根本沒寫。

**round-trip 為什麼沒抓到**：它用**同一個 `cell_values()`** 產生期望值。
「沒寫什麼」與「該寫什麼」出自同一支函式，兩邊一致，比對當然全綠。
**一個拿自己的輸出當期望值的驗證，驗的是自我一致，不是正確。**

這正是 R-BLM3／canon 之 `BLANK → FILL` 要求 test_group **與** test_set
兩欄皆填，而當時只填了 test_group —— 少的那半沒有任何機制會叫。

已修：`test_set` 改取批次層之值。重跑：

```
sheets_patched  {'...': 208}      ← 由 195 增為 208，正是 13 個 test_set 儲存格
round-trip       13 列 × 16 欄，差異 0
交付 lint        clean — 0 findings
```

### 2.5 列對映與欄位

工作簿列 **10–22**（表頭第 9 列，首個空列為 10），TC ID
`newR1L-BLM-001` … `newR1L-BLM-013` 連續。
每列寫 16 欄：req_id／tc_id／test_group／test_set／test_item／pre_conditions／
input_test_data／test_procedure／expected_result／spec_reference／tc_ref_id(`NEW`)／
priority／design_method／functional_safety(`NA`)／author(`PeiPYHsu`)／test_version(`1.0`)。

`functional_safety = "NA"` 與 `test_version = "1.0"` 為本包所定之常數
（feature.yaml 未載、下放包未指定）。**請確認** —— 此二值我是依全案慣例
填的，若有既定值請指正。

reasoning 未入工作簿（profile §4）。

---

## 三、工程債三件 —— 全收

### 3.1 generator 實跑 —— 組得出來，但**第一次是炸的**，且揭出兩個缺口

第一次以 pilot context 走 `backend/prompt_builder.build_batch_prompt`：

```
KeyError: 'test_item'   （prompt_builder.py:830，`row['test_item']`，非 .get）
```

契約查明後為：`rows` 需 `req_id`／`test_set`／**`test_item`**，
`context` 需 **`project`**／`test_group`／`test_set`。
我的 adapter 兩個必要鍵都沒給 —— **這就是四輪未驗的那件事，一驗即現。**

補上後仍有第二個缺口：prompt 之每條 `Spec:` 欄皆為 `N/A`，
**`signal_candidates` 整段不進 prompt**。後果不是報錯而是靜默 ——
生成端看不到 `$ASCM_FD_2.*$` 之候選與 VAL_ 列舉，只能省略訊號或造名（IN §8.4）。

查明 `_get_spec_context(row, spec_index)` 讀的是 `row["matched_spec_context"]`，
**該鍵即通道，屬 adapter 側，不需動 `backend/`**（全域線禁區）。
adapter 已補：每列之 `matched_spec_context` 承載 R-BLM5 之 N 欄常數
與 R-BLM11 四庫預查所得之訊號候選。

重跑：

```
build_batch_prompt   OK  長度 64145
  含 'ASCM_FD_2': True     含 'ASCM_SysFail': True
  含 'SYS1_HMI_Bed_Lowering': True
  13 條 req_id 全含: True
```

prompt 全文落 `batches/pilot/dryrun_prompt.txt` 供覆核。
**dry-run 未呼叫模型**（下放包允許）。

### 3.2 `scripts/lint_tcs.py` —— 已建，讀工作簿

移植自 `features/amfm/scripts/lint_tcs.py`（同形：openpyxl read_only 讀工作簿、
gate 回傳 (gate, message)、`--json-report`）。**與 `selfcheck_pilot.py` 是兩支不同的程式**：
後者讀 `pilot_tcs.json`，答「我寫對了嗎」；本支開交付 xlsx，答「客戶檔裡的東西對嗎」。

16 個 gate：`A-empty`／`B-testitem`／`B-lang`／`C-space`／`C-period`／`C-bracket`／
`C-quote`／`D-verb`／`E-pairing`／`E-minsteps`／`E-modal`／`F-specref`／
`G-priority`／`G-method`／`G-group`／`H-sibling`。

兩個 feature 專屬點：
- `F-specref` 比對 R-BLM5 之單行常數；
- `D-verb` **全行比對而非行首比對** —— 上繳 05 之兩處 `and observe that`
  正是被行首式漏掉的。

結果：`clean — 0 findings`（13 列）。報告落 `batches/pilot/lint_report.json`。

### 3.3 `recon.py` 實跑 —— 對帳 0 差異，但**兩條 assertion FAIL**

R-G4 之顧慮**未發生**：recon 把其表寫成 `data/recon_leaf_to_section.tsv`
（自己的名字），我方 `leaf_inventory.tsv` 逐位元未變（已 diff 確認）。

對帳全綠：

| 項 | recon | 我方 | |
|---|---|---|---|
| leaf 數 | 176 | 176 | 一致 |
| leaf req_id 集合差 | — | — | **雙向皆空** |
| workbook_state | BLANK | BLANK（R-BLM3）| 一致 |
| 欄位命中 | 16 | 16 | 一致 |
| design_method 詞彙 | 9 | IN §12 之 9 種 | 一致 |
| ambiguous_rows | 0 | — | — |

**但兩條 ruled-constant assertion FAIL，且 `DECISIONS.md` 因而未被寫出：**

```
FAIL — citation stem is the ruled baseline, and only that:
       expected ['SYS1_HMI_Bed_Lowering_Mode_..._(June_21_2021)'], measured []
FAIL — every leaf's citation parses to a section:
       expected 0, measured 176
```

**兩條都是 R-BLM5 之直接後果，不是資料有錯。** recon 之 citation 解析器
把 `HMI Source ID` 拆成 `(stem, section)`，而本 feature 之該欄**沒有章節號可拆**：

- 拆不出 section → `citation_stems` 為空 → 第一條 FAIL；
- 176 條全部「無法解析為 section」→ 第二條 FAIL。

`recon.py:915` 之 R-VC8 註解已為 `spec_reference_template: null` 處理了
**TSV 輸出**那一段，但 **assertion 那一段仍假定 section 存在**。
兩處對同一個 null 情境作了不同假設。

其中 `spec_reference_stem` 這個鍵**是我在下放包 02 自己宣告的**，
當時寫「R-BLM5 之基線，實測相異值數 = 1」。現在看，那個宣告
**誤解了該 assertion 在量什麼** —— 它量的是**解析後之 stem**，
不是欄位原值。原值確實只有一個，但解析後是零個。

**未自行改綠。** 三個選項（**本包不自擇，屬 Tier 2**）：

1. 自 `recon_assertions` 移除 `spec_reference_stem` —— 誠實，但少一道保護
2. `recon.py` 之 citation 解析對「無章節號」情境補一條分支（stem = 全欄值）
   —— 治本，但動全域腳本，屬全域線
3. profile 立 `[OVERRIDE]` 明記本 feature 之該二 assertion 恆 FAIL 且為預期

**影響面**：`DECISIONS.md` 未產出。本 feature 之裁決一直記在 `RULINGS.md`
而非 `DECISIONS.md`，故實務上不阻斷；但 FO §4 之 DECISIONS 契約在本 feature
從未落地，**這件事本包才看見，一併回報。**

---

## 四、manifest

| 項 | 值 |
|---|---|
| `workbook_01` | `aa1015f24eca883fee64d272b6f0b402091297da8b22dad7c4a65b08a317943e` |
| `pilot_tcs.json` | `c62348c8b7f7fabb9fb24db9b3198e6047fb1a03deee16f47f3ed712fad2fef5` |
| `manifest.json` | `c6359db1f3f0e891f330ff7e67eac6fbdd6111e29c6fa5670f8e76d8925db358` |
| `feature.yaml` | `120f2d1292e990513cf24649a4f1f29cb18431133f98622323d1ed0b8ae32d79` |
| prompt_template | `34e5d0ac43decdb0b9bd78d4d6710c769243cfea41a2432a06bf964c8b1ad206` |
| exemplar_set | `e3b0c442…`（空集，未變）|

`written_back: true`、`tc_ids: newR1L-BLM-001 … 013 (列 10–22)` 已入 manifest。
重 stamp 後比對相符。

---

## 五、§四 B1 先行預查（Restore And Exit，9 leaf）

leaf 數 **9**，與 framework Part III 一致。九條：

```
022-01 Monitor Vehicle Speed After Bed Lowering Mode   [Service/High]
022-02 Detect                                          [Service/High]
022-03 Exit Bed Lowering Above Threshold               [Service/High]
022-04 Restore Previous Ride Height                    [Service/High]
027-01 Vehicle Stationary Condition                    [HMI/High]
027-02 Cancel and Restore Height Request               [HMI/High]
027-03 Reference Stored Ride Height                    [HMI/High]
027-04 Command Previous Ride-Height Restore            [HMI/High]
027-05 Restore Only When Stationary                    [HMI/High]
```

- **速度語彙命中 9 次** —— 下放包預期「DR-1 必然命中」**成立**。
- ride height 命中 18 次；本 feature 已驗有 `$ASCM_FD_1.FL/FR/RL/RR_Lvl$`
  與 `$IPC_VEHICLE_SETUP2.Default_Ride_Height$`（VAL_ `0 Normal`／`1 Aerodynamic`），
  故「restore previous ride height」有可觀察物，**不預期重演 B 類之困境**。
- **`022-02` 之 Requirement Title 逐字就是 `Detect`（單字）**。
  非擷取錯誤 —— 037 原欄即如此。該條之 test_item 上半須取 Description 而非 Title，
  屆時具名處理。

**B1 未生成**（下放包 §五：待 Pei 認可 §四順序）。

---

## 六、執行層自陳

1. **`functional_safety` 與 `test_version` 兩個常數是我定的**（§二-5），
   無來源明載。若全案有既定值，本包之 13 列需改。
2. **generator dry-run 未呼叫模型**，故「prompt 組得出來」已驗，
   「模型吃了這個 prompt 會產出合格 TC」**未驗**。續批首批才會知道。
3. **交付 lint 之 16 gate 仍不覆蓋 §9 之閱讀判斷項**（3／6／7／9／11／12／17）。
   本包新增之 lint 讀的是工作簿，覆蓋面比 selfcheck 廣（多了 A-empty 這類
   只有工作簿才看得到的），但**不覆蓋語意**。
4. **台架可執行性仍未驗**（第四次記載）。
5. **B1 之訊號預查僅做語彙先行掃描，未回 DBC 逐條定位**
   —— 那屬 B1 生成包，本包不代做。

---

## 七、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`）| 已登記，未送出 |

下放包 §六建議此時送出。**執行層無異議**：B1 九條中速度語彙命中 9 次，
`022-03 Exit Bed Lowering Above Threshold` 直接需要該門檻值，
屆時若未回覆即須落 `PENDING: DR-1 ...`。**送出與否屬 Tier 3，由 Pei 決。**

---

## 八、停點

**已停。** §一～§三完成，B1 未生成。

待 Pei 之項：
1. §三-3 `recon.py` 兩條 assertion 之處置（三選一）
2. §二-5 `functional_safety` / `test_version` 兩常數之確認
3. §四 續批順序之認可（本包已先行做 B1 預查，順序若改，該預查作廢重做）
4. DR-1 送出與否（Tier 3）
