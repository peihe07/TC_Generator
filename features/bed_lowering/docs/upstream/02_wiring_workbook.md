# 上繳包 02 — Bed Lowering Mode：feature 佈線與工作簿起建（執行層回報）

日期：2026-08-26
對應下放包：`features/bed_lowering/docs/handoff/02_wiring_workbook.md`
（sha256 `b827cf79c466dc8dd81f1dd706f23649bd431324981b84fdececd647d0473a2b`）
執行層：Tier 1
**結論：§三／§四 全綠並全數對帳相符；§二 形制須改（已改並附證）；§五 pilot 未執行（Tier 2 且受 A-BLM7 阻斷）。**

本包一切數字皆自腳本 stdout 複製，無一憑印象謄寫（R-G20）。
可重跑之指令逐節具名。

---

## 〇、先講三件與下放包所寫不同的事

1. **§二 之 `feature.yaml` 形制不可用**，且其 `spec_reference_template` 之值
   **不會報錯而會靜默寫壞 176 列**。已改用管線既有編碼並附三值實跑證據。→ §二、A-BLM6
2. **§二 之 `spec_mode: hmi_logic_and_flow` 無此值域**，且本 feature 之
   歸類有兩讀，非機械可決。留 `null`，**pilot 因此無法開工**。→ A-BLM7
3. **§五 之 R-G15／§六 之 R-G16 等引用落在一段全域撞號區**
   （R-G12~R-G20 於 FO 與 RULINGS_LEDGER 各有一套不同條文）。本包依 FO
   讀法執行，語境自洽；但該撞號本身違反 R-G18。→ A-BLM8

以上四項已登錄 `ANOMALIES.md`（A-BLM6 ~ A-BLM9，依 R-G23′ 落檔當下 live 取號，
現行最大為 A-BLM5，故自 6 起）。登錄屬 Tier 1；**裁決屬 Tier 2，本包不代裁**。

---

## 一、R-G20 —— 規則副本現行指紋

| 檔 | SHA256 |
|---|---|
| `docs/runtime/ASPICE_SWE6_AI_Instruction.md` | `0b0cea006552a2f244ba8e733ef6227b132b591a34defb65234934985fe2598e` |
| `docs/fw036/FEATURE_ONBOARDING.md` | `02bddd3da2bdc10c90eb6faa5d53ad7df07ec5d51b3ea25871b49132b2849ede` |
| `docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` | `0b050aae4844aa0ee722728aaaed719dc2ff3407b4bf090994007d74c2605008` |
| `features/bed_lowering/RULINGS.md` | `e0a7e7f4cd2c9d4041840eff80c5e6c36462bf909b7115d041ca4b587ecb3df8` |
| `features/bed_lowering/framework.md` | `c07692197ae494356ef9b1d5f8a295f778c9ec8235ca4f3f01f7027bd32de800` |

---

## 二、`feature.yaml` 佈線 —— **形制已改，請追認**

落點：`features/bed_lowering/feature.yaml`
sha256 `fbad5bc87e065cfe5e248ff57607c10576ffdda35af369a028e372d6b113f007`

### 2.1 為何不能照 §二 落檔

`scripts/feature_config.py` 之 `load_feature_config()` 讀
`cfg["workbook"]["columns"]` 與 `cfg["paths"]`。§二 之草案為扁平鍵
（`slug`／`profile`／`form_template`／`spec_pdf`／`spec_sys1`／`rd_037`…），
**無 `paths:`、無 `workbook:`、無 `done_region:`、無 `lint:`、無 `reference:`**，
照落即於 `cfg["workbook"]["columns"]` 以 KeyError 中止。

### 2.2 `spec_reference_template` —— 靜默寫壞，非報錯

§二 之警語預期「schema 不認得該值 → 停下回報」。**實測之危害比預期更重：
它不會被拒絕。** `scripts/recon.py:915`：

```python
ref = citations.get(rid, "") if tpl is None else tpl.replace("{outline}", sec)
```

三個候選值各實跑一次（可重跑，見 §七）：

| `spec_reference_template` | N 欄實際寫入 | 合於 R-BLM5？ |
|---|---|---|
| `null` | `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)` | **是** |
| `"literal_037_hmi_source_id"`（§二 之值）| `literal_037_hmi_source_id` | 否 |
| 鍵**省略** | `3.2.3`（裸章節號）| 否 |

第二列即 §二 之值：該字串不含 `{outline}`，`replace` 為 no-op，
於是 176 列 N 欄全部寫入字面字串 `literal_037_hmi_source_id`。
**不中止、不報錯、輸出看起來像有值** —— R-G16 所述之「擷取正確而其後階段出錯，
且輸出不會自曝」之形態。

第三列同樣要緊：**省略該鍵不是安全作法**，`cfg.get` 之預設為 `"{outline}"`，
會構造出裸章節號，同樣違反 R-BLM5。**`null` 是三者中唯一正確者。**

### 2.3 `null` 不是新增枚舉

`scripts/recon.py:908` 之 R-VC8 註明載：鍵存在且為 `null` 時，該欄取 037
citation 之**逐字值**（"When the key is present and null, the column takes the
037 citation VERBATIM"）。而 R-BLM5 自陳與 R-VC4 為同一條文，
R-VC4 於 `features/vehicle_category/feature.yaml` 之編碼即為 `null`。

**故本項未改 schema、未新增枚舉，是把 R-BLM5 寫成管線既有之編碼。**
惟其與 §二 之字面指示不同，依 FO §0 登錄為 A-BLM6，**請 Pei 追認**。

### 2.4 依 R-VC9 未宣告之鍵

§二 之 `workbook_state`／`form_template`／`tc_id_pattern`／`slug`／`profile`
**未落為 live 鍵**，改記於註解。實測其 py 消費者數：`form_template` 0、
`tc_id_pattern` 0、`slug` 1（`scripts/rulings_hash.py` 之欄名，非本檔之鍵）、
`workbook_state` 於 `recon.py` 為**偵測輸出**而非讀入之宣告。

依 R-VC9：「宣告一個不被讀取的鍵，比不宣告更糟 —— 不宣告至少誠實，
宣告則製造一個永不失敗之檢查」。`frop` 為例外，沿 vehicle_category 慣例
保留為事實登記（其註解已寫明此點）。

### 2.5 補入 `reference:`（A-BLM9）

§二 無此節，R-G15（ledger 版）要求之。已補四項，雜湊為本包實算：

| 項 | SHA256 |
|---|---|
| `a03_report` | `8d09ab46e69da3ad804703c6ed33e113aef8f47e06ac32363040212cab59b9ab` |
| `sys1_export` | `487354fa935dbc5397428dc633d1fa707fc77f7e5250db3f00c0aa310299a7fa` |
| `spec_pdf` | `0277ed00beab2d05d3a95a68d996c8297bfc9ae09ce0d43c4158ea667750e9d0` |
| `workbook_master` | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |

**`dbc_b`／`dbc_fd`／`lid`／`proxi` 四項未綁，且本包不裁定為不需要。**
與 vehicle_category R-VC10（訊號命中數 0，明文排除）不同 —— §七-2／§七-4
已具名 PROXI 車型參數與 DBC 訊號為生成期必需，四檔尚未擇定版本，無從綁。
生成期首批開工前須先擇定並補綁，否則 R-G15 對該四項之保護為空。

### 2.6 載入驗證

`load_feature_config()` 實跑通過；四條 `paths:` 各解析到**恰好一個**檔
（`resolve_path` 於 0 或 2+ 命中時會中止）；`spec_reference` 欄解析為 index 13（= N 欄）。

---

## 三、工作簿起建 —— 全綠

落點：`features/bed_lowering/workbook/bed_lowering_00.xlsx`
sha256 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`

### 3.1 §三-4 所要之 sha256

**與 R-G1 母本逐位元相同**（`cmp` 全等），故雜湊亦同母本、亦同
`forms/FORMS.md` §母本節所載之值。`workbook_state = BLANK`（R-BLM3），
本階段無儲存格改動，**故最強之保全形式就是不重打包** ——
連 zip 重壓都沒發生，x14 下拉無從損壞。

### 3.2 §三-3 所要之結構計數（起建前後）

以 `zipfile` 讀原始 XML，全程未開啟 openpyxl：

| 指標 | 母本 | `bed_lowering_00.xlsx` |
|---|---|---|
| size | 200650 | 200650 |
| zip_members | 48 | 48 |
| sheet_xml | 9 | 9 |
| sheets_declared | 9 | 9 |
| drawing_rels | 13 | 13 |
| chart_rels | 0 | 0 |
| dataValidation (legacy) | 4 | 4 |
| **x14:dataValidation** | **1** | **1** |
| conditionalFormatting | 0 | 0 |
| extLst | 3 | 3 |

差異欄位：**無**。

### 3.3 一個計數口徑之修正（R-G16 口徑補充、R-G8）

首版探針之 legacy DV 正則寫作 `<(?:\w+:)?dataValidation[ >]`，
該 `\w+:` 會把 `<x14:dataValidation>` 一併算進 legacy，得 **5**。
R-G1 註之實測值為「三條 legacy（P／T–Z／AF）存活」，兩者對不上，
遂逐檔拆算：

| 檔 | legacy（無前綴）| x14 | sqref |
|---|---|---|---|
| `xl/worksheets/sheet5.xml` | 1 | 0 | `B7:C7` |
| `xl/worksheets/sheet6.xml` | 3 | 1 | legacy `P10:Q1411`／`T10:Z1411`／`AF10:AF1411`；x14 `R10:R1411` |

**R-G1 註所指之三條即 sheet6 之 P／T–Z／AF**，x14 那條在 `R10:R1411`
（design_method 下拉）。全簿 legacy 合計 4（含 sheet5 之 `B7:C7`，與 R 欄無關）。

口徑因而具名為：**legacy 與 x14 分開計，前綴不通配**。
理由是 R-G1 註所防之損壞形態正是「x14 掉 1」——
若兩者合計，x14 掉 1 而 legacy 不變時總數從 5 變 4，
**看起來像少了一條 legacy，而不像下拉被摧毀**。合併計數會讓 legacy 替 x14 補位。

---

## 四、資料工件 —— 全綠，逐項與 §六 相符

腳本：`features/bed_lowering/scripts/build_inventory.py`
sha256 `dd7ddc761342da462eb2048934073c6253d6935082b69de8a40de47d74390618`

| 檔 | 資料列 | SHA256 |
|---|---|---|
| `data/leaf_inventory.tsv` | 176 | `e64082ba44dd2fc072a23a004bbec78b2d815148cfda6f2e3ba4a1c9305d7d09` |
| `data/heading_ledger.tsv` | 42 | `94b26a3fa6c247457021c249903136f9a2d29852aed19491ae6edc19f98d899d` |
| `data/test_set_map.tsv` | 42 | `3b92cd2469aa0394932c3b398fd3295e73c13ca3fa00b7e815d52e03452d0c3b` |

### 4.1 R-G10 餘數驗證（執行層自行重跑）

母體：037 `Analysis Report`，表頭第 7 列，資料列 8–225。

```
037 資料列（有 req_id）= 218
  Heading（無 -NN 尾碼）= 42
  leaf（有 -NN 尾碼）    = 176
  req_id 不合式         = 0
037 之相異母號 = 42；framework 已分類 = 42
餘數（全集−已分類）= 空
溢出（已分類−全集）= 空
孤兒 leaf（母號不在 Heading 列中）= 空
```

**全綠。** 另驗 framework 轉錄本身無重複指派（以 assert，見腳本 §h2set）。

### 4.2 兩判準之交叉（R-G11：判準須聲明其盲區）

leaf 之判定用「req_id 帶 `-NN` 尾碼」，另以 Categorization 欄交叉：

```
Heading 列 Categorization=='Heading'                = 42/42
leaf 列   Categorization=='Functional Requirement'  = 176/176
```

**兩判準在本 feature 完全重合。** 此為實測結果，不是可外推之通則 ——
`vehicle_category` 之三判準（145／117／79）即彼此分歧，
其 `feature.yaml` 已載該分歧。本 feature 之重合須於日後 037 改版時重驗。

### 4.3 逐組 leaf 數 vs framework Part III

| Test Set | 實測 | framework | |
|---|---|---|---|
| Feature Entry | 31 | 31 | OK |
| Activation Gating | 28 | 28 | OK |
| Lowering Operation | 33 | 33 | OK |
| HU Feedback | 20 | 20 | OK |
| Cluster Feedback | 13 | 13 | OK |
| Fault Handling | 13 | 13 | OK |
| Restore And Exit | 9 | 9 | OK |
| Display Legibility | 22 | 22 | OK |
| Access Ergonomics | 7 | 7 | OK |
| **合計** | **176** | **176** | |

### 4.4 §六 預期數字之逐列對帳

| 指標 | §六 | 實測 | |
|---|---|---|---|
| 037 資料列 | 218 | 218 | OK |
| Heading | 42 | 42 | OK |
| leaf | 176 | 176 | OK |
| Sub Categorization = HMI | 134 | 134 | OK |
| Sub Categorization = Service | 42 | 42 | OK |
| Test Set 數 | 9 | 9 | OK |
| 各 Test Set leaf 數 | 31／28／33／20／13／13／9／22／7 | 同左 | OK |
| SYS1 Polarion 物件 | 70 | 70（下放包 01 §一-1；本包未重測，見 §八-2）| — |
| N 欄相異值數 | 1 | **1** | OK |

N 欄之唯一值實測為：
`SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)`
—— 與 R-BLM5／profile §1 所載逐字相同。
另測 `Source Requirement ID` 相異值數 = **42**（與 profile §1.1 相符），
`FROP` 相異值 = `['Vehicle Settings']` 單值（與 R-BLM1 相符）。

### 4.5 TSV 之分隔符與正規化（R-G16(a)）

037 之 `Requirement Description`／`Verification Criteria` 內含換行與 NBSP。
落 TSV 前一律：`\xa0`→空格、`[\t\r\n]+`→單一空格、連續空格收斂、去頭尾。
**分隔符為 tab，而 tab 已自資料中移除**，故不存在「分隔符出現於資料」之塌陷。
NBSP 折為空白使「空」與「看起來空」成為同一值 ——
037 以 `\xa0` 填空儲存格，不折則兩者不相等。

---

## 五、Pilot 批 —— **未執行**

§五 指定 `Fault Handling` 全組 13 leaf（母號 011／037／038）。
該組之 leaf 數已驗為 13（§4.3），範圍本身無疑義。

**未執行之兩個理由，皆非可由執行層排除者：**

1. **A-BLM7 阻斷。** `spec_mode` 未定，而它決定批次語料自何處取得
   （export／PDF 文字層／render）。在其未裁前組批即為猜測。
2. **Pilot 為 Tier 2。** FO §0 Tier 1 明列
   「Generation of all post-pilot batches（**pilot itself is Tier 2**）」，
   §五 亦自載「Pilot 為 Tier 2：生成後停，交 Pei 逐 TC 審」。

§五 另要求之 R-G19 prompt 指紋與 R-G20 exemplar 集雜湊，
待 pilot 實跑時隨批次 manifest 一併回報；本包無批次，故無該二值。
**不預先產出一個沒有批次的 manifest。**

---

## 六、`_polarion` 與 SYS1 側之未動項

下放包 01 §六-3 之「`_polarion` 分頁展開」已由分析層完成並記於
A-BLM3（RESOLVED）；本包未重做。SYS1 側之 70 物件計數沿用下放包 01，
**本包未重測**（見 §八-2）。

---

## 七、可重跑指令

```bash
# §四 資料工件 + R-G10 餘數驗證（退出碼 0 = PASS）
python3 features/bed_lowering/scripts/build_inventory.py

# §三 工作簿結構比對（母本 vs 副本）
python3 features/bed_lowering/scripts/xlsx_structure_probe.py \
  "forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx" \
  features/bed_lowering/workbook/bed_lowering_00.xlsx

# §二 feature.yaml 載入驗證
python3 -c "import sys; sys.path.insert(0,'scripts'); \
from feature_config import load_feature_config, resolve_path; \
c=load_feature_config('features/bed_lowering'); \
print([str(resolve_path(c,k)) for k in ('workbook','a03_report','sys1_export','spec_pdf')])"
```

---

## 七之二、版控範圍 —— 本包擴充 `.gitignore`（Tier 1）

本包產出兩類**不得入版控**之物，起建當下 `features/bed_lowering/.gitignore`
（下放包 01 輪所建）尚未涵蓋，已補：

| 落點 | 處置 | 依據 |
|---|---|---|
| `workbook/` | 排除 | `bed_lowering_00.xlsx` 與 R-G1 母本逐位元相同，而 `forms/*` 本就排除該母本。**全案無任何 feature 追蹤工作簿**（`git ls-files` 實測 `features/` 下 tracked `.xlsx` 為 **0**）；`audio_mgmt` 與 `projection` 之 `.gitignore` 皆為此明文排除 |
| `data/leaf_inventory.tsv` | 排除 | 逐字內嵌 037 之 `Requirement Description` 與 `Verification Criteria` |
| `data/heading_ledger.tsv` | 排除 | 逐字內嵌 037 之 `Requirement Title` |
| `data/test_set_map.tsv` | **追蹤** | `heading_id → Test Set → leaf_count`，純衍生結構，無客戶文字；且它正是 framework 鎖定版移動時審查者需要看到 diff 之工件 |

判準沿 `projection/.gitignore` 之原文：
「Carry customer prose rather than derived structure — same policy as `inputs/`」。
三份 TSV 皆可由 `build_inventory.py` 重建，排除不損失任何稽核價值。

**此為本包第二次補同一道防線** —— 01 輪補的是 `inputs/*`
（當時 `features/bed_lowering/` 全無 `.gitignore`）。兩次皆非下放包所指示。

其成因已查明，且**與初判不同，值得記下**：
`scripts/new_feature.py:175` **確實**會產出 `.gitignore`（模板見同檔 `GITIGNORE`），
故「scaffold 不產 `.gitignore`」之推測**不成立** ——
本 feature 之目錄是手建的，未經該 scaffold，所以一個都沒有。

但該模板即使跑了也**不足以涵蓋本包之兩類產出**：模板只有
`inputs/`／`data/recon.json`／`batches/`／`lint_report.json`／local noise，
**無 `workbook/`，亦無任何「內嵌客戶散文之 data 工件」條款**。
`audio_mgmt` 與 `projection` 兩處之排除是各自事後手加的。

故建議分兩項，且第二項與第一項無關：
1. 新 feature 一律經 `scripts/new_feature.py` 起建，勿手建目錄；
2. 該模板補 `workbook/` 一條 —— 全案 tracked `.xlsx` 為 0，
   該事實已是通例，通例宜落在模板而非逐 feature 事後補。

本包未改該腳本（屬全域線）。

---

## 八、執行層自陳 —— 本包應驗而未驗者

逐項自問「這一項現在驗得了嗎？」之結果：

1. **`prompt_builder` 是否認得本 feature 之配置** —— **未驗**。
   本包未組批，未觸及 `backend/prompt_builder.py`。§二 之警語含此項，
   本包只驗到 `feature_config` 與 `recon.py` 兩處。
   **`prompt_builder` 側之相容性仍是未知，不得因本包 §二 全綠而視為已驗。**
2. **SYS1 側 70 物件** —— **驗得了而未驗**。沿用下放包 01 之計數。
   理由：本包之任何動作皆不以該數為輸入（§四 之母體全在 037 側）。
   **但它在本包中是個未經本包驗證之數字**，§4.4 已標明其出處。
3. **`recon.py` 未實跑** —— **驗得了而未驗**。本包以自寫腳本建工件，
   未跑 `scripts/recon.py`。理由：`spec_mode` 未定（A-BLM7），
   且 recon 會寫 `RECON.md` 與 `data/` 下之另一張表（R-G4 所記之
   `spec_id_to_outline.tsv` 覆寫事故即此形態），在配置未追認前不宜寫入。
   **§二 之 `recon_assertions` 兩鍵因而是宣告而未經 recon 實跑驗證**
   —— 其值（176 與 stem 字串）本身出自本包實測，但「recon 跑起來會 PASS」
   這件事未驗。
4. **`distinct_spec_sections` 未宣告** —— 有意為之。其值本包未實測，
   而宣告一個未實測之期望值即製造一個假的保護（R-VC9）。
5. **A-BLM8 之撞號僅就本包所引之四條查證**（R-G15／R-G16／R-G19／R-G20），
   **R-G12／R-G13／R-G14／R-G17／R-G18 僅自兩份文件之標題列比對，
   未逐條文比對全文**。故「全段撞號」之範圍下界為已查之四條，
   上界為 R-G12~R-G20 九條 —— **上界未經逐條驗證**。

---

## 九、未結 DR 清單（IN §8.4.3）

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`，owner: chassis engineering）| 已登記，未送出 |

本包未新增 DR。§七-2 之 PROXI 車型參數對照仍為候選 DR，
待生成期查 `forms/` 後確定 —— **本包未查**（該查詢屬生成期，且本包無生成動作）。

---

## 十、待 Pei 裁之項（Tier 2）

| # | 項 | 阻斷什麼 |
|---|---|---|
| 1 | **A-BLM7 `spec_mode`** | **pilot 批**。未裁不可開工 |
| 2 | A-BLM6 `feature.yaml` 形制與 `spec_reference_template: null` 之追認 | 不阻斷；已按管線既有編碼落檔，追認後即定案 |
| 3 | A-BLM9 四個參考資料庫之版本擇定 | 不阻斷本包；阻斷生成期首批 |
| 4 | A-BLM8 全域撞號 | 不阻斷本 feature；屬全域線 |
