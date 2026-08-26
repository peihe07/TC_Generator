# 上繳包 10 —— Vehicle Category：Phase 4 pilot（Glove Box）—— **停並回報**

- 日期：2026-08-26
- 對應下放：`docs/handoff/10_pilot_tc.md`
  （SHA256 `41d7cb71413555ee73481507048015492ac9cab1e0059ae2996fa59595910b90`，205 行）
- **結論：T56／T57 完成，T58 之收斂條件 1 項不過 → 依 §四「任一項不過即停
  並回報，不自行修補後續」，停於此。**
- 12 筆 TC 已產出（`generated/pilot_glovebox.json`），**未寫回工作簿**。
- 未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T56 | R-VC18 抄錄 | ✅ 逐字 |
| T57 | 12 筆 TC | ✅ 產出，一 leaf 一 TC |
| T58 | 收斂條件十項 | ⚠️ **13 checked / 1 failed** |

**停點：`test_item` 上半之 verbatim 帶非 `"..."` 之來源記法，6 筆。**
根因是 **Vehicle Category 尚無 profile**，而 IN §11 之引號例外是
**profile-scoped**。這不是筆誤，是本 feature 缺一份 profile ——
pilot 把它逼出來了。詳見 §5。

**另有一項我認為須裁而不在收斂條件內**：`VC-033-01` 之 `test_item`
上半逐字抄了 Title（`After three sequential wrong PINs`），
而該筆之門檻正是 A-VC14 所爭者。**交付欄位裡出現了一個 PENDING 說它未定
的值。** 見 §6。

---

## 1. T56 —— R-VC18

抄入 `RULINGS.md` 行 607。byte-level diff 逐字一致。

---

## 2. T57 —— 12 筆 TC

`generated/pilot_glovebox.json`。一 leaf 一 TC，12 筆。

| # | leaf | § | priority | design_method | tc_title |
|---|---|---|---|---|---|
| 1 | `VC-026-01` | 4.1 | P1 | 功能測試 | Explanatory popup shown on selecting Glove Box |
| 2 | `VC-026-02` | 4.1 | P1 | 功能測試 | PIN request popup shown after Yes |
| 3 | `VC-026-03` | 4.1 | P1 | 功能測試 | PIN entered twice with instruction text differing |
| 4 | `VC-027` | 4.2 | P2 | 狀態轉換 | Glove Box Activated popup after matching PINs |
| 5 | `VC-028-01` | 5.1 | P1 | 負向測試 | Incorrect PIN warning on mismatched second entry |
| 6 | `VC-028-02` | 5.1 | P1 | 負向測試 | No upper limit on incorrect activation attempts |
| 7 | `VC-029` | 5.2 | P1 | 狀態轉換 | Activation succeeds on first-entered PIN after mismatches |
| 8 | `VC-030` | 6.1 | P1 | 功能測試 | Deactivation prompts for the same PIN |
| 9 | `VC-031` | 6.2 | P2 | 狀態轉換 | Glove Box Mode deactivated popup after PIN accepted |
| 10 | `VC-032` | 6.3 | P3 | 狀態轉換 | OK on confirmation popup returns to Controls |
| 11 | `VC-033-01` | 7.1 | P1 | 邊界值分析 | Deactivation locked for 30 minutes after repeated wrong PINs |
| 12 | `VC-033-02` | 7.1 | P2 | 負向測試 | Four-digit rule enforced on 3-digit entry |

priority 逐筆取自 `data/priority_final.tsv`，**未重判**（機械驗證見 §4 第 5 項）。
JSON 全文見該檔（`indent=1`，12 筆完整）。

### 2.1 §8.4.1 —— 未造之值

- `VC-028-02`／`VC-029` 之「N 次」**未造具體數** ——
  以 `repeating this mismatch cycle multiple times` 之可重複步驟表述。
- `VC-033-01` 之門檻**未取 3 亦未取 4** —— 填
  `PENDING: DR-VC8 Glove Box lockout threshold`。
- 30 分鐘之**計時起點未寫入** —— 規格與 037 皆未載，已併 DR-VC8。
- **未引用任何 PU 編號** —— 規格未給。

### 2.2 §8.2.1 —— `VC-021` 之委派

到達 Glove Box 之 Controls 操作寫在 setup 步驟；
**12 筆之 ER 皆不驗證 Privacy Lock 彈窗之 id／標題／按鈕組成**。
委派載於全部 12 筆之 `reasoning`（機械驗證見 §4 第 10 項）。

---

## 3. T58 —— 收斂條件逐項

腳本：`scripts/verify_pilot.py`。原始輸出：

```
verify_pilot — Glove Box pilot（R-VC18，下放包 10 §四）
  1  12 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                      PASS
     TC 數 12；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8 項；全項見上繳包）                         PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
  3  test_item 括號下半 12 筆兩兩不同（機械）                               PASS
     缺括號 無；重複 無；相異 12
 3b  test_item 括號下半無中文（R-S4）                                   PASS
     含中文 無
  4  specification_reference 12 筆與 recon_leaf_to_section.tsv 逐字相符  PASS
     不符 0 筆
  5  priority 12 筆與 priority_final.tsv 逐字相符                      PASS
     不符 0 筆
  6  Test Set 12 筆皆為 `Glove Box`，Test Group 皆為 `Vehicle Category` PASS
     test_set=['Glove Box']；test_group=['Vehicle Category']
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                            PASS
     尾句號 0；單引號 0；方括號角括號 0；空白 0
 7b  test_item 上半之 verbatim 是否帶非 "..." 之來源記法                   **FAIL**
     帶來源記法者 6 筆 ['VC-026-01','VC-026-02','VC-027','VC-030','VC-031','VC-032']
  8  `VC-033-01` 帶且僅帶一處 PENDING，字串逐字相符                          PASS
     033-01 之 PENDING 數 1；字串相符 True；他筆帶 PENDING 無
  9  `028-02`／`033-01` 之括號下半明載其流程                              PASS
     未載者 無
 10  `VC-021` 之委派載於全部 12 筆之 reasoning（§8.2.1）                  PASS
     未載者 無
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 無 observe/verify 起首 PASS
     步數不足 無；1:1 不符 無；ER 含 modal 無；禁用起首動詞 無
13 checked / 1 failed
```

### 3.1 ⚠ 一項檢查器自身之誤報，已修

初版之 modal 檢查對 `VC-033-02` 報 FAIL —— 其 ER 含
`A popup is displayed reading "PIN must be 4 digits / OK"`。
那個 **must 在引號內，是規格所載之畫面文字，不是作者之 modal**。
檢查器未排除引號內文字。已修（`_unquoted()`），修後 PASS。

**這是檢查器的錯，不是 TC 的錯** —— TC 未改。與 T52 掃描器初版漏抓
A-VC14 自身同型：**本輪兩支新寫的檢查器，各有一個判準錯誤。**

---

## 4. IN §9 十七項逐項

| # | 項 | 判 | 依據 |
|---|---|---|---|
| 1 | Test Set 名詞片語、與 framework 相符、無 Test Group 前綴 | PASS | 機械（§3 第 6 項）；`Glove Box` 與 `framework.md` §2 #3 逐字相同 |
| 2 | tc_title 三形之一、2–14 字、sibling token 可見、無 modal | PASS | 人工：12 筆皆為 (b) 句式或 (c) 標籤；字數 6–10；無 shall/will/should |
| 3 | Pre-Condition 僅狀態／環境 | PASS | 人工：二式（未啟用／已啟用且 PIN 已知）＋ 進入畫面；**未寫**「Glove Box is accessible」 |
| 4 | Input Test Data 欄位歸屬 | PASS | 12 筆皆 `NA`；PIN 值內聯至 Procedure（§4.5 第 2 類） |
| 5 | 步驟可執行、無禁用動詞、Final Step 擁有驗證 | PASS | 機械（§3 第 A 項）＋人工 |
| 6 | 步長與意圖層級 | PASS | 人工：2–3 步 |
| 7 | 標準 setup 片語重用 | N/A | 本 feature 無既有 done region，無片語庫 |
| 8 | CLI 步驟格式 | N/A | 無 CLI 步驟 |
| 9 | 需要前後對照時設 baseline | PASS | `VC-026-03` 之第 1 步記錄第一次彈窗，第 3 步與之對照 |
| 10 | Procedure ↔ ER 1:1、ER 可觀察、無 modal、涵蓋完整 | PASS | 機械（§3 第 A 項） |
| 11 | 無 FP／FF；supported 配負向 | PASS | 人工：`-027` 配 `-028-01`、`-030/-031` 配 `-033-01/-033-02` |
| 12 | 追溯至 Req、不擴張至 sibling、允許 sub-id ≠ TC 數、無造值、無造範圍 | PASS | §2.1／§2.2；一 leaf 一 TC 為 R-VC18 所定 |
| 13 | Design Method 於 procedure 定稿後指派 | PASS | 人工：先寫流程後套 §12 首匹配 |
| 14 | 四欄無尾句號 | PASS | 機械（§3 第 7 項） |
| 15 | UI 標籤用 `"..."` | **PASS（作者欄位）／見 §5（verbatim 上半）** | 機械（§3 第 7 項）作者散文全數合規；上半之來源記法為 7b 之停點 |
| 16 | specification_reference 列出所驗之全部 section | PASS | 機械（§3 第 4 項）；12 筆各驗一節 |
| 17 | 原始規格優先於索引匯出；門檻為 spec-sourced；相似操作於 ER 區辨 | **部分** —— 見 §6 | 4 位 PIN／30 分鐘為 spec-sourced；**次數門檻不是**，故 PENDING |

**主觀成分之範圍（下放包 10 §六第 8 項所要求之揭露）**：
第 2、3、6、7、9、11、13 項為**人工判讀，無機械證據**。
第 15 項之判定分作者欄位（機械）與 verbatim 上半（見 §5）二層。
第 17 項之「相似操作於 ER 區辨」我判為通過，但那是我自己讀自己寫的東西 ——
`-028-02` 與 `-033-01` 之區分是本批最可能被審閱者讀成矛盾之處（§3.3），
**該項尤應由你複核，不宜採信我的自評**。

---

## 5. 停點 —— `test_item` 上半之來源記法（6 筆）

### 5.1 事實

037 之二欄對彈窗文字各用一種記法：

| 欄 | 記法 | 例 |
|---|---|---|
| `Requirement Title` | `'...'` 單引號 | `present a popup ... the 'Glove Box' option` |
| `Requirement Description` | `«...»` 法式引號 | `Selecting «Glove Box» option a popup is displayed` |

IN §11 禁 `'...'`、`<...>`、`[...]`，只許 `"..."`。
其**例外**（quoted verbatim from a cited source may retain the source's
notation）明文為 **profile-scoped** —— 「**when the feature profile says so**」。

**Vehicle Category 目前沒有 profile。** `docs/runtime/profiles/` 下
無 `FW036_R1L_VehicleCategory_Profile.md`（`RUNBOOK.md` Phase 3 之該項
仍未勾選）。故該例外**未被啟動**。

### 5.2 我試過的規避與其結果

逐筆檢查有無「不帶引號之 verbatim 可選」：

| leaf | Title | Desc | 可選之無引號 verbatim |
|---|---|---|---|
| `026-03`、`028-02`、`029`、`033-01` | 無引號 | — | ✅ **已採 Title** |
| `028-01`、`033-02` | `'...'` | **`"..."`** | ✅ **已採 Desc** |
| `026-01`、`026-02`、`027`、`030`、`031`、`032` | `'...'` | `«...»` | ❌ **二欄皆帶非法記法** |

**6 筆無解。** 我採了 Title（單引號）並停在此處回報。

### 5.3 我沒有做的三件事，及其理由

1. **未把 `'...'` 改寫成 `"..."`** —— 那會破壞 verbatim（R-S4 上半為
   規格原句）。R-4 只許「句首字母轉大寫」之排版正規化，未及於引號記法。
2. **未自行援用 §11 之例外** —— 該例外之啟動條件是 profile 明文，
   我不能代 profile 說話。
3. **未改 lint 使其放行** —— 拘束 4：不得為了讓結果好看而預先改腳本。

### 5.4 三條可能之出路（**未擇一，待裁**）

| 出路 | 內容 | 代價 |
|---|---|---|
| 甲 | 寫 VC profile，其中載明 §11 例外對 037 二欄記法之適用 | Phase 3 之 profile 本就待寫（`RUNBOOK.md` 未勾），順勢補齊；但 profile 屬 Tier 2 |
| 乙 | 立 `R-VC{n}` 專條，允許 `test_item` 上半保留來源記法 | 快，但把本該在 profile 的事寫進裁決層 |
| 丙 | 裁定引號記法之正規化屬 R-4 之排版正規化 | 最省事，但**擴張了 R-4 之範圍**，且會使日後「什麼算排版」失去邊界 |

我的判斷是**甲** —— 這件事本來就是 profile 該管的，而 VC 缺 profile
是一個獨立於本 pilot 的既有缺口；用乙或丙繞過去，等於讓 profile 繼續缺著。
**但這是 Tier 2，我不自裁。**

### 5.5 這正是 pilot 的用處

12 筆之小批把「VC 沒有 profile」這件事逼了出來。
若第一次遇到它是在 100 筆的批次裡，代價是 100 筆的返工。

---

## 6. 另一項須裁 —— `VC-033-01` 之 verbatim 帶入了爭議值

不在收斂條件內，但我認為不能不說。

該筆之 `test_item` 上半逐字抄了 Title：

```
After three sequential wrong PINs during Glove Box deactivation, block the
deactivation feature for 30 minutes
```

而 `three` 正是 A-VC14 所爭者（Title 第 3 次 vs Desc 第 4 次）。
於是同一筆 TC 裡同時出現：

- `test_item`（交付欄位）：`After three sequential wrong PINs` —— **斷言 3**
- `test_procedure`：`PENDING: DR-VC8 Glove Box lockout threshold` —— **說它未定**

**交付欄位裡出現了一個 PENDING 說它未定的值。**

A-VC14(a) 禁的是「TC 作者自行取 3 或 4」。我沒有自行取 ——
是 verbatim 把 Title 的 3 帶了進來。形式上不違反，實質上使該 TC
自我矛盾。

三種處置（**未擇一，待裁**）：
- (a) 上半改採 Desc（`more than three times`）—— 只是換一個爭議值，不解決；
- (b) 上半保留 Title，另於括號下半或 `remarks` 明載二欄之分歧 ——
  我在括號下半已寫 `threshold value pending`，但那是提示不是揭露；
- (c) 該筆之 `test_item` 上半改摘不含門檻之句段 ——
  但 §7.1 之整句就是門檻句，摘不出來。

---

## 7. 未結清單

**DR 八筆全未結**（DR-VC1 ~ DR-VC8）。同批 A 五項。
**A 十筆未結**：A-VC2、A-VC3、A-VC4、A-VC8、A-VC9、A-VC10、A-VC11、
A-VC12、A-VC13（通則）、**A-VC14**。
已結四筆：A-VC1（撤銷）、A-VC5／A-VC6／A-VC7（RESOLVED）。

---

## 8. 待你裁

1. **§5 之停點** —— 甲／乙／丙（我建議甲：寫 VC profile）。
2. **§6 之 `VC-033-01` verbatim** —— (a)／(b)／(c)。
3. 同批 A（五項）與 DR-VC3 之發送（Tier 3）。

**未自行修補後續。12 筆 TC 已在 `generated/pilot_glovebox.json`，
未寫回工作簿。**

---

## 9. 量測條件揭露（R-G8）

- **§3 之機械檢查**：13 項中 10 項為純機械、3 項（第 2、9、10）為
  「機械化其可機械化之部分」。第 9 項只驗括號下半是否含
  `activation`／`deactivation` 字樣，**不驗其語意是否真的區分了流程** ——
  後者見 §4 第 17 項之揭露。
- **檢查器之可信度**：本輪兩支新檢查器各出一個判準錯誤
  （T52 之類別切分、verify_pilot 之 modal 未排除引號）。
  二者都是**寫檢查器的人和寫被檢查物的人是同一個**所致 ——
  我對自己的產出設判準，判準就帶著我的盲點。§4 之人工項尤其如此。
- **§5.2 之逐筆檢查**為人工讀 12 筆之二欄，非機械 ——
  「有無不帶引號之 verbatim 可選」無法機械判定，因為「哪一句是
  verbatim 上半該取的句」本身是判斷。
