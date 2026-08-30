# 74 包（續）—— Pei 授權執行層直接處置之結果

Pei 逐字：「**授權你直接去做吧**」。範圍讀為 73/74 包所餘之二項阻出貨事項
＋ §B-5 之客戶夾複製。**未做二事**：刪 `_20260824.xlsx`（刪除動作，74 包 §B-7 明定由 Pei 定）、
發送七張 DR（本層無發送能力）。

## 1. 站④-2 —— 15 條 `<STATE>` 逐條指定，**佔位符歸零**

依據**取自各條自身之 `test_item` 上半 verbatim 或既有裁決**，未另造判準：

| 條 | 指定 | 依據 |
|---|---|---|
| `-198`–`-201` | `FUNC_STATE_IDLE`、`3 (Idle)` | `test_item` 逐字為 `CFTS009-4941365`（§1.6.2.1.2 **Idle**）之段落 |
| `-105` / `-106` | 改直接檢查 `"Splash Screen"` | `test_item`：「TLM has to show a proper Splash Screen」—— 標的為該具名元件本身 |
| `-135` / `-136` | 改直接檢查 `"Rear View Camera"` 影像 | `test_item`：「rear view camera images shall be provided」|
| `-178` | **`PENDING: DR-PW29`** | 觸發為「power mode 轉 BODY ON」，而 BODY ON 群依 `4941042` / `4941039` **二分支**，規格未指單一值 → **不猜**（§8.4.1）|
| `-179` | `4 (Full_Operation)` | 步 1 送 `CmdIgnSts = 5 (START)`；`4941357` 逐字列 `Ignition Start` 為 Full-Operation 保持之條件 |
| `-180` | `2 (Timed)` | 步 1 觸發逐字為「a status change to TIMED MODE」|
| `-184` | baseline (f) ＋ `"Splash Screen"` 不出現 | `tc_title` 逐字「resumes the state diagram **without a splash**」|
| `-270` | baseline (f)（基線不變）| 「shall not enter stolen vehicle mode under any condition」；`VAL_ 1470` 無 stolen vehicle 值 |
| `-122` | `PENDING: DR-PW26` | Suspend-to-RAM 對應之 `PowerSts_Telematic` 值規格未載 |
| `-279` | `PENDING: DR-PW26 INIT 觀察量` | `INIT` 不在 `VAL_ 1470`（A-PW350 / R-P363(c)）|

**未替換佔位符：120 → 0。** 十五條中**三條仍為 PENDING**（`-178` / `-122` / `-279`）——
其為**規格確實未載**，不是本層未做；已各歸其 DR。

## 2. G257 —— 拆步至 47 步（5.7%），其餘不動

### 判準之一項明示假設（待分析層追認）

IN §5.2 只定義三種角色：**A** 一般 setup／transition（≤12，明載「Action + target only;
**no purpose clause**」）、**B** Final Step（≤18）、**C** 帶 `to …` 之 setup（≤18）。

本 corpus 之慣例為**一 TC 多個 check 步**（ER 1:1 對齊之基礎，自早期各包既然），
故存在**非末步而自帶 `check that` 之步** —— **該形態不在 §5.2 之三分類內**。
§5.2A 之定義明言其為「無 purpose clause」之步，**不涵蓋帶 check 之步**；
G257 據此把「非末步但帶 check」歸為**驗證步，取 18 字**。

⚠ **此為分類假設，非內容判斷。** 若分析層裁為應取 12，則須先裁
「一 TC 只能有一個 check 步」——那是 §5.5 之適用問題，非字數問題。

### 拆步之取捨

保守版（`split_conservative_74.py`）**只在帶逗號之並列連接處切**
（`, and check that ` / `, and read ` / `, then ` / ` —— `），
故 `Read … and check that …`（R-P354(a) 之原子）**不被拆**、§5.5 之驗證擁有者保有 `check that`。

- 73 包之激進版（裸 ` and check that ` 亦切）已**撤回**，腳本註解保留
- 拆步後 **G257 由 153 → 47 步（涉 46 條）**，占 Procedure 總步數 **827** 之 **5.7%**
- 餘 47 步**無乾淨切點**（如 `Start the TLM boot sequence and send each ignition value…`）；
  **R-P366(b) 明文「不得刪減資料以合字數」**，故不動，據實列於 `data/g257_steplen_73.md`

### 拆步之副作用，已補正

保守拆步後有 **5 句之受詞被指代詞孤立**（`the paired phone screen`、`it`），
G245 由 0 升至 5；已回填具名元件（`"Call Screen"`、`"FOTA update available"` pop-up、
`$STATUS_TELEMATIC.PowerSts_Telematic$`、`HU speakers`），**G245 回到 0**。
`-119` / `-120` 之 ER 因拆步而步數不齊，已逐步重寫（原第 4 句合併二事，現分列第 4、6 句）。

## 3. 最終閘表

| 閘 | 期望 | 實測 | 判 |
|---|---|---|---|
| G245 家族 A（上界）| 0 | **0** | ✓ |
| G250 `proper` / `as defined` / `normal` | 0 | **0** | ✓ |
| G250 `Read the HU mode/state` | 0 | **0** | ✓ |
| G247 內部訊號 | 0 | **0** | ✓ |
| G256 引號 lint | 0 | **0** | ✓ |
| **未替換佔位符** | 0 | **0** | ✓ |
| Procedure / ER 1:1 | 全對齊 | **不等者 0** | ✓ |
| G251 | 0 | **3**（皆 (c) 類應保留）| ✓ |
| G249 | — | **10**（全 (b) 型、互註齊）| ✓ |
| **G257 Procedure 字數** | 0 | **47 步 / 827（5.7%）** | **殘留，見 §2** |

`lint_docs036` PASS、`ledger_xref` PASS。

## 4. 交付件（已重出）

| 檔 | |
|---|---|
| `sandbox/b73/pm_73.xlsx` | 288 列、129,292 bytes、sha256 `9e729b3f…` |
| `delivered/pm_73.xlsx` | `filecmp` 實測逐位元組一致；`delivered/MANIFEST.tsv` 已更新 |
| `delivered/PENDING_LIST.md` | **147 條 / 377 處**（站④-2 已解，不再列）|
| `delivered/DR_DISPATCH.md` | 七張 DR 全文 |
| `delivered/tcid_three_gen_73.tsv` | 287 列 |
| `output/…_20260830.xlsx` | 逐位元組一致 |

PENDING 分布：DR-PW23 **92 條**、DR-PW27 **54**、DR-PW25 9、DR-PW30 6、DR-PW26 4、DR-PW29 2。

## 5. ⚠ 已複製至客戶夾

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/
  FM-WI-FSM-036-A01 …_SWQT_PowerManagement_20260830.xlsx
```

129,292 bytes、sha256 `9e729b3f3ee4b85df804b219661a8c6e1543ad1a88af0b52028de0738eb89538`，
與 `delivered/pm_73.xlsx` **逐位元組一致**。

該夾現有三個版本：`_20260820`（132,332 B）、`_20260824`（155,653 B，第一代 pm_29／390 列）、
**`_20260830`（本次）**。

## 6. 未做，與理由

| 項 | 理由 |
|---|---|
| **刪 `_20260824.xlsx`** | 刪除動作，74 包 §B-7 明定「是否移除**由 Pei 定**」；授權未及於刪檔，**不動** |
| **發送七張 DR** | 本層無發送能力；`delivered/DR_DISPATCH.md` 已備妥全文 |
| **Excel GUI 開啟驗證** | 74 包 §B-6 之手動項；本層已做 `openpyxl` 層之結構驗證（見 72 包站④ §A）|
| **git push** | 未指示；15+ commit 待 push |

## 7. 交分析層（不阻出貨）

1. **G257 之分類假設**（§2）—— 「非末步之 check 步取 18 字」待追認。
2. **G257 殘留 47 步** —— 無乾淨切點，依 R-P366(b) 不刪資料而保留。
3. **`-178` 之 BODY ON 二分支** —— 已開問於 DR-PW29。

---

# 附記 —— 列序訂正（Pei「Requirement or Design ID 要照順序排」）

## 1. `req_id` 之列序**本就正確**，錯的是同 leaf 內之次序

以 comfort 96 §6 之判準（`<` 為違規、`==` 為同 leaf 多條屬合法）實測交付本：
**288 列，逆序斷點 0** —— 與 ICS `b35e651` 之陳述（「power/delivered measures 0 breaks」）一致。

**真正的缺陷在第二層**：同一 leaf 內 `tc_id` 不遞增。

| leaf | 訂正前 | 訂正後 |
|---|---|---|
| `SWE-PM-075` | `169、284、285、170、171` | **`169、170、171、284、285`** |
| `SWE-PM-087` | `248、249、286` | `248、249、286`（本就正確）|
| `SWE-PM-093` | `174…182、287` | 同（本就正確）|

## 2. 根因 —— 68 包 §8.3 之 `clone()` 沿用了來源條之 `split_index`

列序鍵為 `(req_id, split_index)`（R-P113 / R-P115）。
68 包之拆分四條以 `clone()` 產生，**整份複製來源條**，故 `split_index` 一併沿用：

| 拆分條 | 來源 | 沿用之 `split_index` | 訂正為 |
|---|---|---|---|
| `-284` | `-169` | 1 | **4** |
| `-285` | `-169` | 1 | **5** |
| `-286` | `-249` | 2 | **3** |
| `-287` | `-182` | 9 | **10** |

同 leaf 內出現**重複鍵**，Python 之穩定排序遂保留 JSON 陣列序，
把 `-284`/`-285` 排到 `-169` 之後而非該 leaf 之末。

⚠ **68 包當時未察** —— 該包只驗了「五欄鍵下與原條相異，不觸 R-P357」，
**沒驗列序**。`split_index` 是列序鍵而非內容欄，五欄鍵看不到它。

## 3. 新增列序 gate（`scripts/verify_row_order_74.py`）

判準取自 **comfort 96 §6** 三道 ＋ **ICS `b35e651`** 之第四道，逐道對交付本跑：

| # | gate | 結果 |
|---|---|---|
| 1 | `row-order-by-reqid` | **PASS** |
| 2 | `tc-id-sequence`（同 leaf 內遞增）| **PASS** |
| 3 | `all-leaves-present` | 112 / 115；缺 `SWE-PM-008`（DR-PW11）、`SWE-PM-010`（DR-PW11）、`SWE-PM-112`（DR-PW9）—— **皆 DR 阻斷，PASS** |
| 4 | `blank-row-shape` | **PASS**（留空列 r233 只有 B 序號與 D req_id，A-PW102 所定）|

**含反向驗證**（comfort R-C41 之同一理由：一道只會通過的檢查證明不了任何事）——
對前二道各注入一個壞序，**皆轉紅 ✓**。

⚠ 第一版之反向驗證**未轉紅**：我互換的是二個**同 leaf** 之相鄰列，
而判準為 `<` 不含 `==`，故不構成逆序。已改為挑「相鄰而 leaf 號不同」之一對。
**反向驗證自己也需要被驗證。**

## 4. 附帶發現 —— 站④-3：`-286` 與 `-248` 內容重疊

`-286` 為 68 包依 R-P393(c)「`-249` 補 M240 支」所增，
惟 **`-248` 本即為 M240 支**（`tc_title`「The M240 vehicle line uses the M240 seat graphics」，
Procedure 送 `VC_VEH_LINE = "M240"`，ER 驗 `"M240 seat graphics"`）——
**R-P393(c) 立條時未察該支已存在**。

二者五欄不逐字相同（措辭有別），故 R-P357 不機械觸發。
**去留屬 IN §8.2.1 / §8.3 之處置，執行層不逕刪**；已標
`(站④-3：與 -248 同為 SWE-PM-087 之 M240 分支，內容重疊，待分析層裁去留)`。

## 5. 交付本已重出並同步三處

sha256 `cedb6b84d422d872649733795164fe9896421cbffbd6b98d81e0bcca3a9fcf00`

| 位置 | 一致性 |
|---|---|
| `sandbox/b73/pm_73.xlsx` | 來源；`MANIFEST.tsv` 已更新 |
| `delivered/pm_73.xlsx` | `filecmp` 逐位元組一致；`delivered/MANIFEST.tsv` 已更新 |
| `output/…_20260830.xlsx` | 逐位元組一致 |
| 客戶夾 `…/Power Management/…_20260830.xlsx` | **逐位元組一致** |
