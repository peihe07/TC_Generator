# 上繳 28 — 第三批 30 條落地，四項裁示實施

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`28_batch03_go.md`（**無裁決條文**）
- 另附：`docs/upstream/28_provenance4.md`（**第三批之 ER 出處對照**）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）；**RD 查詢單未寄出**（Tier 3，屬 Pei）
- 語料：**78 → 108 條**；leaf 覆蓋 **72 → 100 / 180**

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | **108 條，違規 0** |
| `lint_tcs.py --self-test` | 60 / 60 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ **108 條違規 0** |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／K-4b 0／**Q-1 9 處待判** |
| `audit_consistency.py --self-test` | **25 / 25**（＋2：K-4a v4）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | **紅 0 ／ 黃 13** ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| **`lint_outbound_doc.py --self-test`（本輪新建）** | **8 / 8** |
| **`lint_outbound_doc.py` 對 `27_rd_queries_v2.md`** | **違規 0** |

```
全語料 design_method：功能測試×64, 基礎故障注入×2, 情境/用例×3,
                      狀態轉換×22, 負向測試×11, 邊界值分析×6
全語料 priority：P0×33, P1×35, P2×35, P3×5
第三批 design_method：功能測試×17, 狀態轉換×12, 負向測試×1
第三批 priority：P0×9, P1×14, P2×5, P3×2
```

**P0 比例 33 / 108 ＝ 30.6%**（前為 24 / 78 ＝ 30.8%）——
**未因批次擴大而回頭調判準**（J-9）。

---

## 1. 第三批 —— **ch4 剩餘 26 ＋ A-UP13 附掛 3**（＋`009` 之負向配對 1）＝ 30 條

**批界之寫法依 R-4**：一律記為上式，**不寫「第三批 ＝ ch4」** ——
附掛之三項落在 ch6／ch7，**批界是被修訂，不是被稀釋**。
該寫法已寫入 `gen_batch03.py` 之 docstring 與 profile §0.1。

| 區段 | tc_id | 內容 |
|---|---|---|
| ch4 剩餘 26 leaf | `079`–`104` | 4.1／4.1.1／4.2／4.3／4.3.1／4.4／4.5／4.5.1／4.5.2／4.5.3／4.5.3.1／4.5.4／4.6／4.6.1／4.6.2／4.6.3 |
| §7 之額外配對 | `105` | `SWE1-HMI-PROF-009-neg` —— 4.5.2 之全稱限制之反向 |
| A-UP13 附掛 | `106` | `SWE1-HMI-PROF-048-del`（6.2.1 後半，**已覆蓋 leaf 之第二條 TC**）|
| A-UP13 附掛 | `107` | `SWE1-HMI-PROF-059-02`（7.2.1 之 More Options，新 leaf）|
| A-UP13 附掛 | `108` | `SWE1-HMI-PROF-059-03`（7.2.1 之切換後新 popup，新 leaf）|

**全文路徑**：`features/user_profiles/generated/`（30 個檔，檔名為 leaf id）。
生成器為 `scripts/gen_batch03.py`。

### 1.1 四項先具名處置之落實

| 項 | 落實 |
|---|---|
| **`002-02` popup 內文不寫（R-U27）** | `NR1L-UserProfiles-082` 之 ER 僅斷言 `PU1087`／`PU1088` **顯示**與其時序，**不寫其上之文字**；remarks 具名該限制與「DR #4 到齊後得補」 |
| **`005` 之順序斷言可區分** | 見 §1.2 —— **本批最值得單獨講的一條** |
| **委派指名 leaf id** | 第三批新增之委派 5 處，皆指名 `SWE1-HMI-PROF-…`；`audit_delegation` 紅 0 |
| **PLP 併列之代價聲明隨引用欄同讀** | `079`／`080`／`088`／`100` 四條（`PLP_LEAVES`）之 remarks 一律以 `PLP_COST` 起首，**與引用欄同在一條 TC 內** |

### 1.2 `005`（`NR1L-UserProfiles-088`）—— 順序如何被測出來

條文：`If a Profile is switched within a key cycle, any changed preferences
will be saved **before** the new Profile is loaded.`

**難處在於「回來還在」證不了「存在載入之前」** ——
`A 切走再切回，值還在`（ER3）與下列兩種實作都相容：

- 正確：切換前先存 → 載入 B
- **錯誤**：載入 B 後才把 A 的變更寫出去

**能分開兩者的是 ER2**：若實作在 B 載入後才寫入，
**那筆變更會落到 B 上**（或覆蓋 B 之值）。故 ER2 斷言

> `Driver Profile B is active and its preference is **its own value, not the
> value recorded in step 1**`

**ER2 ＋ ER3 併存才構成順序之斷言**；任一單獨都不夠。
已於 remarks 與 reasoning 兩處具名該推理。

### 1.3 生成時被閘擋下者（**7 處，皆為我方之錯**）

| 閘 | 處 | 成因 |
|---|---|---|
| G15（步驟字數）| 5 | 步驟過長（14／20／14／13／13 詞）—— 縮寫後過 |
| G18（數值溯源）| 2 | `091`／`105` 之座椅編號 `1` 溯不到條文 —— **該判定是對的**：條文確實沒給編號。已登記為測試設置（J-12）並於 remarks 具名 |

**G18 那兩處值得記**：閘沒有誤報，是我寫了條文裡沒有的數字。
處置不是放寬閘，是**把它登記為測試設置並在 TC 內說明它不是條文來的**。

---

## 2. R-1 —— 對外文件之最小閘（`lint_outbound_doc.py`）

### 2.1 判準與其自我限制

> 對每張 markdown 表格，取其緊鄰之前一段：找 `<數字> <複數名詞>`，
> **被數之物須出現在該表之表頭或首欄**；
> **若該段內任一數字等於表列數 → 綠**，否則紅。

**只做這一項。** 語意之審查留給人工 ——
「這個主張有沒有證據」不可測，「說七條而列四列」可測。

### 2.2 **v1 判準對它所為之文件本身誤報兩處 —— 已修**

初版判準（只看「數字＋複數名詞」是否等於表列數）實跑 `27_rd_queries_v2.md`，
**判紅兩處，而那兩處都是對的**：

| 誤報 | 成因 |
|---|---|
| `covered by **seven** leaves … In **four** of the seven …` ＋ 4 列表 | 該段**同時**寫了總數與本表筆數，v1 只抓到前者（`four of the seven` 之被數之物不是複數名詞）|
| `measured across all **180 leaves** of this feature:` ＋ 4 列量測表 | 那個 180 **根本不是在數這張表** |

**一支會把正確文件判紅的閘活不過三輪（R-G9）**，故加兩道收斂
（被數之物須出現在表頭／首欄；段內任一數字命中即通過）。

修正後：**v2 綠、v1 之原始缺陷仍紅**（其段內數字為 7／12.8／037／one，無一為 4）。
方向性案例 **8 / 8**，其中兩條即上表之誤報案例 —— **它們是護欄**。

### 2.3 盲區（R-G11）

只看緊鄰前一段（筆數寫在表後看不見）；只認英文數字詞與阿拉伯數字
（**中文不認 —— 本閘為對外英文文件而設**）；數字對得上不代表內容對。

---

## 3. R-2 —— `ANOMALIES.md` 之「整體位移」**加註，原文保留**

依 R-2 與 R-G4-1 之先例：原文不刪，另起一段註明 27 輪之修正與其反證
（七條實查：`125-03`／`125-04` 取自 12.8.1 組、`126-01`／`126-02` 取自 12.8 組，
**兩組互相取用，非單向 +1**；七條中僅**四條**錯置）。

**理由照收**：刪掉就看不出「曾經主張過一個未經證明的模式」。

---

## 4. R-3 —— Q-1 引號界線寫入 profile，`039`／`013` 不改

profile 新增 **§3.3.1**：

> 測試者會在畫面上逐字讀到的一句文字，或可點擊元件之 label → **加雙引號**；
> 我方以清單形式轉錄之表格列項 → **不加**。

**盲區一併寫入**：Q-1 之 ≥7 詞閾值係看了結果才定
（N=6 得 19／N=7 得 8／N=8 得 7）—— **短於 7 詞之未加引號顯示文字，本掃描看不見**。

**本批新增之 Q-1 待判 2 處**（`098`／`104`），逐條判**皆非缺陷**：
`a default profile associated with that seat`（行為敘述）、
`in the status bar edit mode drawer`（位置名）—— 與既有 7 處同型。

---

## 5. R-4 —— 批界寫法

已落三處：`gen_batch03.py` docstring、profile §0.1、本檔 §1 與 `docs/INDEX.md`。

---

## 6. 生成後之閘所抓到者（**K-4a 四處，判準與案例各有其錯**）

第三批生成後 `audit_consistency` 之 K-4a 紅 4 條，**逐條判非一律放寬**：

| tc_id | 判 | 處置 |
|---|---|---|
| `099`（4.5.3.1）| **判準漏詞** —— 刪除 profile 確使**現用者**改變，是真狀態遷移 | 詞表補 `delete` |
| `106`（6.2.1）| **判準漏詞** —— 客製化使該 profile **不再是預設**，是持續狀態之改變 | 詞表補 `customize` |
| `108`（7.2.1）| **判準漏詞** —— 自 popup 選另一 profile 即切換 | 詞表補 `select driver profile` |
| **`103`（4.6.2）** | **案例錯，非判準錯** | **改判為功能測試** |

**`103` 是這組裡唯一不該靠放寬詞表解決的**：其受測對象是
**按鈕之 highlight 隨區段開闔而變** —— 那是**條件式呈現**，
不是系統狀態機之遷移。與 `099`（現用 profile 由 A 變 B）對照即明：
後者變的是**持續存在之系統狀態**，前者變的是畫面上的一個樣式。
沿 P-1 之同一分野（§8.7.4：視覺狀態不等於機制）。

**並補一條護欄案例**：「只有開啟／讀取之 procedure 標狀態轉換 → **仍須紅**」——
它守住這次放寬沒有溢出（`open`／`read` **未**收進詞表）。

---

## 7. 出處對照之獨立發現（詳見 `28_provenance4.md`）

**`G18` 只掃 `expected_result`，不掃 `pre_conditions`。**

依 28 包指示併掃 pre-condition，於 `NR1L-UserProfiles-100`（4.5.4）抓到
`“Driver 2”` **溯不到 4.5.4** —— 該節寫的是 `default **Driver 1-2**
Profiles`，`Driver 2` 單獨出現在 **4.5.1**。

**處置**：改用本節自己的寫法（`“Driver 1-2”`），**未另引 4.5.1**（引之即多引）。

**這是本輪唯一由出處對照抓出而閘抓不到者。**
15 個引號字面值，**未溯得者 0**；變體／配置範圍層級逐條列於該檔 §2 ——
**本批無任何 R1 High／China 變體條件**，與 25 包取樣清單之預告一致。

---

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **第三批 30 條未經第二人讀過** | **分析層待辦** | 覆核用全文尚未產出 —— **待下包指示是否比照 21／23 輪出 review pack** |
| 2 | **`G18` 不掃 `pre_conditions`** | **本輪之自陳缺口** | §7 之發現即出自此。擴之會大量誤報（pre-condition 多為測試設置描述），**未擴**，待裁 |
| 3 | **`002-02` 帶上游未決事項** | 承前（DR #4）| ER 不寫 popup 內文；DR #4 到齊後得補 |
| 4 | **A-UP13 三行為已生成，但其**覆核**未做** | 待覆核 | 生成 ≠ 覆核（22 輪之聲明） |
| 5 | **`pending` 兩 axis 仍未兌現** | 待第四批 | `046`（6.1）／`065`（8.1）不在本批；絆線仍在 |
| 6 | **(b) 類委派本批兌現 2 / 5** | 待後批 | `047`（6.2）、`073-02`／`073-03`（8.7）未涵蓋 |
| 7 | **對外閘只查數字** | 判準盲區 | §2.3 |
| 8 | **RD v2 未寄出** | **待 Pei（Tier 3）** | 執行層不代寄 |
| 9 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

---

## 9. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/gen_batch03.py`（第三批生成器）| 否 |
| 2 | **檔案新建** | `scripts/lint_outbound_doc.py`（R-1，＋8 方向性案例）| 否 |
| 3 | **檔案生成 ×30** | `generated/`（`079`–`108`）| 否 |
| 4 | 檔案編輯 | `scripts/lint_tcs.py`（`TEST_SETUP_NUMERALS` ＋2）、`scripts/audit_consistency.py`（K-4a v4 ＋2 案）| 否 |
| 5 | 檔案編輯 | `ANOMALIES.md`（R-2 加註）、`docs/runtime/profiles/…UserProfiles_Profile.md`（R-3 §3.3.1、R-4 §0.1）| 否 |
| 6 | **檔案新建** | `docs/upstream/28_batch03.md`（本檔）＋ `docs/upstream/28_provenance4.md` | 否 |
| 7 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 8 | 程式執行 | 生成 ×1、全部閘、六支 audit／lint 之 `--self-test`、出處對照 | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_variant_labels.py`、`render_spec_region.py`、`build_batch_context.py`、
`audit_variant_pairs.py`、`audit_delegation.py`、`scan_override_notes.py`、
**他 feature 之任何檔**、`docs/fw036/`。

**第四批未取樣** —— 待第三批覆核。
