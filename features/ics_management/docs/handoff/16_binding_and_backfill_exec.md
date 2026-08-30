# 下放包 16 — 綁定與讀者、12 處回填、reasoning 更正（2026-08-30）

## §0 背景與量測時點

**Pei 於 2026-08-30 下「開」** → 第三次窗口式解凍，落為 **R-ICS48**。

b15 之作業 B（綁定）與 C（回填）因 **E26 觸發**而未執行。分析層審後 **放行**（R-ICS47(a)）：

| E26 之立法理由 | 實測 |
|---|---|
| 「綁定與回填皆以**訊號解析正確**為前提」 | **成立** —— 17 個已用訊號之起始位元、長度、字節序、factor／offset、值域、單位、`VAL_` 列舉於四支 dbc 中 **17／17 全數相同**；交付欄受影響 **0 條** |

實際觸發者為 `reasoning` 三條之引述過時（A-ICS100），性質較輕。
**E26 之措辭為分析層之瑕疵**（A-ICS101：判定面寫「任何一條 TC」而立法理由只涉交付欄）。
**執行層依字面停下且不自行放行，正是 E9 所要求之行為，不追究。**

### 本輪之三項判定變更（影響本包範圍）

| 項 | 變更 |
|---|---|
| **回填範圍** | **擴至 TC 2／TC 4**（R-ICS48(c)）。R-ICS47(d) 已判「Pre-Condition 未寫建立法」非缺陷（IN §4.4）；A-ICS91 之論據已崩解（A-ICS102，分析層之誤） |
| **A-ICS93** | 改述：差異在**匯流排族**（BHCAN vs FDCAN）**不在世代**；數值面風險經量測不成立 |
| **A-ICS91** | 論據須重新指認；核心觀察仍成立，惟其對 TC 2／4 之含意已失。**台架可行性面維持 OPEN，不因本包回填而結案** |

### 本輪分析層之寫入

- `RULINGS.md`：**R-ICS47**（E26 放行、A-ICS91 崩解、Pre-Condition 非缺陷）、**R-ICS48**（本窗口）
- `ANOMALIES.md`：**A-ICS100 ~ A-ICS107**

> ⚠ **台帳版面事項（A-ICS107，執行層須知）**：`ANOMALIES.md` 之
> A-ICS100~106 七列因追加錨點不唯一而**插於 A-ICS72 與 A-ICS73 之間**。
> **完整性未損**（106→107 列、相異、無重號、無缺口），`ledger_guard` 判準全過，
> 唯列序非遞增。**執行層讀台帳時不得以「檔案末列」推定最大號**，
> 一律以 `grep` 取最大值。

### 前提（量測時點 2026-08-30）

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：`## R-ICS` 標題 **55** 行、相異 **48**；無重複條號 | `ledger_guard.py` |
| P2 | `ANOMALIES.md` **107 列**、相異 107、**號段 1–107 無缺口**（列序非遞增，見上）；DR 主登記表 **21 列**、相異 21、無缺口 | 同上 |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | 圍籬 diff 對 `docs/reports/15_rulings_snapshot.md`：**新增 `R-ICS47`＋`R-ICS48` 二條**、刪除 0 行 | 快照法，**不碰 git** |

P1／P2 為分析層自算（`## R-ICS` 現場實測 54 行／相異 47，本輪 +1）。
不符以實測為準並具名，不停工；重複條號 → E18。

---

## §1 禁區

- **git 全數不執行，唯讀亦不可。**
- **`features/display/`、`features/vehicle_setting/` 一字不改**（R-ICS46(b)：本裁定射程限 `ics_management`）。
- **`FORMS.md` 僅得改 BHCAN2 一列之「使用 feature」欄**；其版次、sha、取代關係欄，
  及其他所有列，**一字不改**。
- **`test_item` 上半之 verbatim 一字不改**（R-17(b)）。
- **`reasoning` 之更正限於 A-ICS100 所指之三條**；不得順手改其他 TC 之 `reasoning`。
- **錨（`specification_reference`）一處不改。**
- **作業 D 只量不改**（R-ICS48(f)）：不得因體例量測結果而改任何 TC。
- G5 維持押後；A-ICS104／105 本包不排入。
- 不得對任何 DR 結案。
- 分析層五簿一字不寫；不自取 `A-`／`DR-` 編號。
- **不得以本下放包之敘述代替檔案現況**：12 處／14 條、17 個訊號、三條 `reasoning`
  等數字**皆須現場複驗**。

---

## §2 裁決引用

**R-ICS48(a)~(g)**、**R-ICS47(a)(d)(f)**、**R-17(a)(b)(c)**、**R-G40**、**R-G41(a)** 為本包主據；
R-ICS46(a)(b)(d)、R-ICS43、R-ICS38(a)、R-ICS8、R-ICS26(a)(b)、R-ICS17(e)(f)、
R-ICS29(f)、R-ICS32(c)、R-ICS34；IN §4.4、§8.7.5、§10.7、§11。

---

## §3 作業清單

> **順序**：A（綁定＋讀者）→ B（回填）→ C（reasoning 更正）→ D（體例抽查）→ E（自檢）。
> A 必須先於 B：未綁定之 dbc 不得採認入 TC（R-ICS47 前之既有拘束）。

### 作業 A — 綁定 BHCAN2 ＋ 建立讀者（R-ICS48(d)／R-G40）

1. **`ics_management/feature.yaml`**：於 `reference:` 增 BHCAN2 一項（`file` ＋ `sha256`）。
   - sha **現場重算**，不得抄用本包或前包所載之值；
   - 既有 10 鍵**一字不改**；
   - 鍵名自訂但須與既有命名體例一致，於上繳包中具名其所取之鍵名。
2. **`forms/FORMS.md`**：BHCAN2 一列之「使用 feature」欄增列 `ics_management`
   （現為 `display` 單一）。若該表另有 R-G15 之反向記載列，一併增列；
   **若無該列，不新建**。
3. **建立讀者**：於 `features/ics_management/scripts/` 新建 `verify_reference_binding.py`。
   - **移植自 `features/display/scripts/` 之同名檔**，逐項對照其鍵後移植（R-G40 五）；
     移植檢查表隨上繳包附上，缺鍵即補，**不得默默沿用**；
   - 讀本 feature 之 `feature.yaml` `reference:` 段，逐項重算 sha256 並與宣告值比對；
   - 不符 → exit 1 並印出不符之鍵。
4. **首跑並報 11／11**（11 ＝ 原 10 ＋ BHCAN2）。
5. **納入 gate 集**；§5 之 gate 由四支改報**五支**。

**E27**（沿 b15）：首跑若顯示**既有 10 鍵中任一 sha 不符** → **停下回報**，不進作業 B。
那表示過去十五包某個參考件已被改動而無人察覺。

---

### 作業 B — 12 處佔位回填（R-ICS48(c)）

**前提：作業 A 完成且未觸發 E27。**

1. **複驗佔位面**：`pending_census.py` 現報 18 處／14 條。
   逐處列出 `DR-ICS8` 之 12 處佔位所在之 TC、欄位、行號。
   **本包所述「12 處皆為 `<TGW_DISP_STAT CAN signal>`」須複驗**；若非，停下回報。
2. **回填，依 R-17(a) ＋ IN §8.7.5(a)**：
   - 訊號 → `$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$`
   - 值 → `= <raw> (<label>)`，`label` **逐字取自 `VAL_`**：
     `0 (Display_off)`、`2 (Normal_mode)`、`7 (Rear_Camera_Display)`、
     `8 (On_blanked_screen)`、`15 (SNA)`
   - **值名與訊號名同批改**；不得出現「訊號名用 DBC、值名用規格」之混用
   - **TC 2／TC 4 一併回填**（R-ICS48(c)）
3. **`$Telematic_Power$` 之裸符號**（A-ICS106）：於本次所觸之列，
   一併改為 `$STATUS_TELEMATIC.PowerSts_Telematic$` 式，值取 `3 (Idle)`／`4 (Full_Operation)`。
   **只改本次回填所觸之列**，不擴及其他 TC。
4. **`reasoning` 逐條追記**（R-17(b)）：
   > 規格作 `$TGW_DISP_STAT$`，DBC 實名 `TGW_DISP_STATSts`＠`BO_ 1500 TELEMATIC_DISPLAY2`
   > （`forms/PDT27_E2A_R1_BHCAN2.dbc`），依 R-17 採 DBC 實名實值。
   > 同一物之判定**僅繫於 R-17(c) 項③**（項①② 對 CFTS020 結構性不可比，A-ICS94），
   > **列為可重驗項**。
5. **複審 `(supporting observation)` 標記**（A-ICS98）：方向已定（DUT 為發出者），
   逐條給判定；**若判不正確，改之並具名**（R-ICS48 授權範圍內）。
   **E30**：若該改動會牽動 ER 之**驗證目標**（非僅標記）→ 停下，不改。
6. 回填後全批重跑 `selfcheck_b01.py`、`verify_verbatim_b01.py`、`pending_census.py`。
   **`verify_verbatim` 預期仍 31／31**（上半未動）。

---

### 作業 C — `reasoning` 過時引述之更正（A-ICS100／R-ICS48(e)）

b03 三條之 `reasoning` 逐字引 B 檔（R4_BHCAN）之
`SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" DCSD` 並斷「發送節點為 SGW 而非 ICS」；
而於裁定之 A 檔（R1_BHCAN2），`RQ_DISP_INTS` 為 **`ETM`→`SGW`**。

1. **先複驗**：三條之現行 `reasoning` 全文逐字引出；A 檔之 `RQ_DISP_INTS` 行逐字引出。
2. 更正為 A 檔之實情，**並註明所據之 dbc 檔名**（以免再次發生同型過時）。
3. **限於 `reasoning` 三條，不及交付欄**（交付欄受影響 0 條，已由 b15 量實）。

---

### 作業 D — 其餘 29 條之 Pre-Condition 體例抽查（**只量不改**）

出 `docs/reports/16_precondition_style.md`。

31 條逐條列其 `pre_conditions` 之每一項，標：

| 類 | 判準 |
|---|---|
| 狀態陳述、無建立步驟 | 該項所述之狀態於 `test_procedure` 中無對應建立步驟 |
| 狀態陳述、有建立步驟 | 有對應步驟 |
| 環境／硬體前提 | IN §4.4 之 allowed types |
| 其他 | 逐條說明 |

給四類之實數，並答：**「未寫建立法」是否為全批體例，抑或 TC 2／4 之個例？**

**界限**：**只量不改**（R-ICS48(f)）。依 R-ICS47(d)，該形態本身非缺陷；
本項只為知其分佈。**不得因量測結果而改任何 TC。**

---

### 作業 E — 常設自檢集

1. **圍籬 diff**：對 `docs/reports/15_rulings_snapshot.md`。
   預期新增 `R-ICS47`＋`R-ICS48` 二條、刪除 0 行。**不碰 git。**
2. 候選篩（R-ICS34）：二數並報＋殘餘率（前七包 53／53／43／52／47／47／47%）。
3. 未錨定斷言（R-ICS32(c)）：3（弱驗證）＋6（已標明）。
4. **五支 gate**（含新建之 `verify_reference_binding`）開工前／完工後各一跑；差值報出。
   開工前基線含 `lint_docs036` 之紅（成因在 `features/power/`，**非本包所致，不修**）。
5. 開工時重測本包 sha256（R-ICS17(e)）。
6. 完工時存 `docs/reports/16_rulings_snapshot.md` —— **回凍之新基準**。

---

## §4 停下回報條件

沿 E1／E9／E18，並：

- **E27**：`verify_reference_binding` 首跑顯示既有 10 鍵中任一 sha 不符 → 停，不進作業 B。
- **E30**：`(supporting observation)` 之改動會牽動 ER 之驗證目標 → 停，不改。
- **E31**：作業 B 步驟 1 複驗發現 12 處佔位**並非全為 `<TGW_DISP_STAT CAN signal>`** → 停下回報。
- **E32**：回填後 `pending_census` 之殘餘處數**不等於 6**（18 － 12）→ 停下回報。
  數字不合表示佔位面之理解有誤。

---

## §5 預期數字（審查基準）

**凡有列舉者，數字自列舉長度取得（A-ICS72 之拿法）。**

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；`## R-ICS` **55** 行（相異 **48**）、A-ICS **107 列**（無缺口）、DR **21／21**；無重複條號 |
| 2 | 圍籬 diff | 新增 **`R-ICS47`＋`R-ICS48` 二條**、刪除 **0** 行 |
| 3 | `feature.yaml` `reference:` 鍵數 | **10 → 11** |
| 4 | `FORMS.md` 變動 | **僅 BHCAN2 一列之「使用 feature」欄**；其餘 **0** |
| 5 | `verify_reference_binding` 首跑 | **11／11 相符**（若非 → E27 停）|
| 6 | **`features/display/`／`features/vehicle_setting/` 變動** | **0 處** |
| 7 | 回填處數 | **12** |
| 8 | 回填後佔位總數 | **6 處**（若非 → E32 停）|
| 9 | 涉佔位之 TC 數 | **14 → 6** |
| 10 | `verify_verbatim` | **31／31**（上半未動）|
| 11 | TC 總數 | **31**（不變）|
| 12 | 錨變動 | **0 處** |
| 13 | Test Set 相異值 | **5**（不變）|
| 14 | 作業 C | `reasoning` 更正 **3 條**；each 註明所據 dbc 檔名 |
| 15 | 作業 D | 31 條逐條四類判；四類各有實數；答「全批體例抑或個例」 |
| 16 | `(supporting observation)` 複審 | 逐條判定；改動數為實測值 |
| 17 | 候選篩 | 二數並報＋殘餘率 |
| 18 | 五支 gate | 差**皆 0** |
| 19 | **git 指令執行次數** | **0**（含唯讀）|
| 20 | 快照 | `docs/reports/16_rulings_snapshot.md` 已產出 |

---

## §6 上繳包要求

`docs/upstream/16_binding_and_backfill_exec.md`。沿 upstream-15 之節構，並須含：

- §1 裁決指紋（R-ICS1～R-ICS48 ＋ 全案 R-17／R-G41）＋前提驗證＋圍籬 diff
- 作業 A～E 之結果；
  - **`verify_reference_binding.py` 之移植檢查表**（逐鍵對照）
  - **12 處回填後之逐處全文**（訊號名、值、reasoning 追記）
  - **三條 `reasoning` 更正前後之逐字對照**
- **§n 未結 DR 清單（21 條）**
- **結果三分法**
- **獨立判斷**：本包是否仍有該驗而未驗者；
  以及 —— **DR-ICS8 是否可標「可結」**（只建議不裁），
  以及 **ICS 線於本包後是否已達「可部分交付」之點**（31 條中無佔位者之條數與其可交付性）
- 建議登錄之 anomaly（編號由分析層取）

---

## §7 本包之意義

**十六包來第一次真的把一件缺件補完。**

DR-ICS8 從 b03 開到現在，12 處佔位卡了十三包。其解法走了三步：
Pei 裁匯流排（BHCAN2）→ Pei 裁寫法權威（R-17：以 DBC 為主）→ b14／b15 量同一物與方向。

本包做完，ICS 之佔位由 **18 處降至 6 處**（只剩 DR-ICS6 五處、DR-ICS4 一處），
涉佔位之 TC 由 **14 條降至 6 條** —— **25 條將成為無佔位之條**。

那不等於可出貨（V1／V2／V3、B5 仍有 ER 判不出對錯之問題，且無佔位故工具不會提醒），
但那是十六包來第一次，「還差什麼」這個問題有一個短到可以寫在一行裡的答案。
