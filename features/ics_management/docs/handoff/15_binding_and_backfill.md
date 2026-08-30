# 下放包 15 — 世代錯配、綁定與讀者、12 處回填（2026-08-30）

## §0 背景與量測時點

**Pei 於 2026-08-30 下二字：「開」「裁 BHCAN2」** → 落為 **R-ICS46**。

| 裁 | 效果 |
|---|---|
| 「裁 BHCAN2」 | `forms/PDT27_E2A_R1_BHCAN2.dbc` 歸屬確立，**得綁入 `feature.yaml` 並採認入 TC**。R-ICS44(d) 之「不逕裁」解除 |
| 「開」 | **第二次窗口式解凍，範圍限本包**。b15 完工自動回凍 |

**射程限制（R-ICS46(b)）**：本裁定**不裁** display 線之 A-DM14，
**不令** `display`／`vehicle_setting` 改用任何檔。
`features/display/`、`features/vehicle_setting/` 本包**一字不改**。

### 本輪分析層之寫入

- `RULINGS.md`：**R-ICS45**（b14 之採認與上呈）、**R-ICS46**（本裁定與本窗口）
- `ANOMALIES.md`：**A-ICS91 ~ A-ICS99**
- `docs/fw036/RULINGS_LEDGER.md`：R-17 加註（(c) 三項之可比性可能結構性為零，A-ICS94）

### 前提（量測時點 2026-08-30）

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md`：相異 ruling_id **46**、`## R-ICS` 標題行 **53**；無重複條號 | `ledger_guard.py` |
| P2 | `ANOMALIES.md` 至 **A-ICS99**、相異 99、無缺口；DR 主登記表 **21 列**、相異 21、無缺口 | 同上 |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | 同上 |
| P4 | 圍籬 diff 對 `docs/reports/14_rulings_snapshot.md`：**新增 `R-ICS45`＋`R-ICS46` 二條**、刪除 0 行 | 快照法，**不碰 git** |

**P4 之算法已依 A-ICS99 之拿法修正**：預期數自**快照時點**至現在之全部寫入取得，
含前一包完工後所落之條（`R-ICS45` 即屬此類）。P1／P2 為分析層自算，不符以實測為準並具名。

---

## §1 禁區

- **git 全數不執行，唯讀亦不可。**
- **`features/display/`、`features/vehicle_setting/` 一字不改**（R-ICS46(b)）。
  `FORMS.md` 僅得於 BHCAN2 之「使用 feature」欄增列 `ics_management`，
  **不得改其版次、sha、取代關係欄，不得改其他任何檔之列**。
- **作業順序不得顛倒**（R-ICS46(f)）：A → B → C → D。
- **回填限於不涉 TC 2／TC 4 者**（R-ICS46(g)）。TC 2／TC 4 **不改、不回填、不推定**。
- **不得因回填而改動未被回填之 TC**（R-ICS46(h)）；G5 維持押後。
- 不得對任何 DR 結案（DR-ICS8 之結案待佔位實際回收後由分析層裁）。
- 分析層五簿一字不寫；不自取 `A-`／`DR-` 編號。
- **不得以本下放包之敘述代替檔案現況**：所引之數字（12 處、8 條、四支 dbc）皆須複驗。

---

## §2 裁決引用

**R-ICS46(a)~(h)** 為本包主據；**R-17(a)(c)(e)(f)**、**R-G40**、**R-G41(a)**、
R-ICS45(a)(c)(e)、R-ICS43、R-ICS38(a)、R-ICS8、R-ICS26(a)(b)、R-ICS17(e)(f)、
R-ICS29(f)、R-ICS32(c)、R-ICS34；IN §8.7.5、§10.7、§11。

---

## §3 作業清單

### 作業 A — 世代錯配（A-ICS93）**最高優先，在回填之前**

出 `docs/reports/15_dbc_generation_diff.md`。

**問題**：本 DUT 為 **R1L**，而已綁之二支 dbc 為 **R4／R5**、未綁之二支為 **R1**。
前十四包之訊號解析皆建立於 R4／R5 上 —— **該前提從未量過。**

**量測項**：

1. **四支 dbc 之清單自 `forms/` 與各 feature `inputs/` 重建**（不採本包所述之四支為定數；
   若有第五支，停下回報 —— 同 E25 之精神）。
2. **本線已用訊號之全集**：自 `generated/` 全部 TC 與 `docs/reports/` 之訊號解析報告中
   抽出**所有**曾被解析或引用之 CAN 訊號名，去重後列出（給實數）。
3. **逐訊號跨世代比對**：對 (2) 之每一訊號，列其於 A(R1_BHCAN2)／B(R4_BHCAN)／
   C(R5_FDCAN8)／D(R1_FDCAN8) 四支中之：存否、承載 `BO_`、起始位元、長度、
   `VAL_` 列舉、發方、收方。
4. **差異分類**：`四支一致`／`僅 R1 與 R4-R5 有差`／`僅存於某世代`／`其他`，各給實數。
5. **對本線既有 31 條之影響**：差異訊號中，有多少已被寫入現有 TC？逐條列出受影響之 TC。

**輸出**：`無差異`／`有差異（列出）`／`不可判`。

**E26**：若 (5) 判出**任何一條既有 TC 受世代差異影響**，**停下回報** ——
不進入作業 B／C。理由：綁定與回填皆以「訊號解析正確」為前提。

---

### 作業 B — 綁定 BHCAN2 ＋ 建立讀者（R-ICS46(a)(d)）

**前提：作業 A 判 `無差異`，或雖有差異但 (5) 之受影響 TC 為 0。** 否則本作業不做。

1. **`ics_management/feature.yaml`**：於 `reference:` 增 BHCAN2 一項
   （`file` ＋ `sha256`）。sha 須**現場重算**，不得抄用本包或前包所載之值。
   既有 10 鍵**一字不改**。
2. **`forms/FORMS.md`**：BHCAN2 之「使用 feature」欄增列 `ics_management`
   （現為 `display` 單一）。**其餘欄位與其餘所有列一字不改。**
   若該表另有 R-G15 之反向記載列，一併增列；**若無該列，不新建**。
3. **建立讀者**（R-ICS46(d)／R-G40）：於 `features/ics_management/scripts/` 新建
   `verify_reference_binding.py`。
   - 移植自 `features/display/scripts/` 之同名檔，**逐項對照其鍵後移植**（R-G40 五）；
   - 讀本 feature 之 `feature.yaml` `reference:` 段，逐項重算 sha256 並與宣告值比對；
   - 不符 → exit 1 並印出不符之鍵；
   - **本作業完成後立即跑一次，報 11／11 之結果**（11 ＝ 原 10 ＋ BHCAN2）。
4. **納入 gate**：將該腳本加入本 feature 之 gate 集，於 §5 之「四支 gate」改報**五支**。

**E27**：若步驟 3 之首跑顯示**既有 10 鍵中有任何一鍵 sha 不符**，**停下回報** ——
那表示過去十四包某個參考件已被改動而無人察覺，屬重大事實。

---

### 作業 C — 12 處佔位回填（R-ICS46(g)(h)）

**前提：作業 A、B 皆完成且未觸發 E26／E27。**

1. **複驗佔位面**：`pending_census.py` 現報 18 處／14 條。
   逐處列出 12 處 `DR-ICS8` 佔位所在之 TC 與欄位，**並標明其中哪些屬 TC 2／TC 4**。
   （本包所述「12 處皆為 `<TGW_DISP_STAT CAN signal>`」須複驗。）
2. **回填不涉 TC 2／TC 4 者**，依 **R-17(a)**：
   - 訊號名 → `$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$`（依 IN §8.7.5(a) 之 `$MESSAGE.Signal$` 式）
   - 值 → `= <raw> (<label>)`，`label` 逐字取自 `VAL_`：`0 (Display_off)`、`2 (Normal_mode)` 等
   - **值名與訊號名同批改**，不得出現「訊號名用 DBC、值名用規格」之混用
3. **`reasoning` 逐條追記**（R-17(b)）：「規格作 `$TGW_DISP_STAT$`，
   DBC 實名 `TGW_DISP_STATSts`＠`BO_ 1500`，依 R-17 採 DBC；
   同一物之判定僅繫於 R-17(c) 項③（項①② 對 CFTS020 結構性不可比，A-ICS94），
   列為可重驗項。」
4. **`test_item` 上半之 verbatim 一字不改**（R-17(b)）。
5. **複審 `(supporting observation)` 標記**（A-ICS98）：方向已定（DUT 為發出者），
   該標記是否仍正確？**逐條給判定；若判不正確，改之並具名**（本款為 R-ICS46(h) 所授權）。
6. 回填後全批重跑 `selfcheck_b01.py`、`verify_verbatim_b01.py`、`pending_census.py`。
   **`verify_verbatim` 預期仍 31／31**（上半未動）。

---

### 作業 D — TC 2／TC 4 之前提建立法（**只量不改**，A-ICS91）

出 `docs/reports/15_tc2_tc4_precondition.md`。

1. TC 2／TC 4 之現行 `pre_conditions`、`test_procedure`、`expected_result` **全文逐字引**。
2. 其前提（`Telematic Power = Full Operation`／`= Idle`）**現行以何法建立**？
   - 以 CAN 輸入餵入（哪一步驟）？
   - 以 DUT 自身之電源模式／PROXI／其他設定建立？
   - 或**根本未寫如何建立**（僅列於 Pre-Condition 而無對應步驟）？
3. 若為第三種，則 A-ICS91 之「餵不進去」**可能根本不是本 TC 之問題**
   —— 逐字說明，**不推定**。
4. 規格 `4819144`／`4820117` 之主詞為 **ICS（面板）**而非本 DUT：
   該二物件是否為 TC 2／TC 4 之錨？若否，其錨為何？逐條列出。

**界限**：**只量不改。不改步驟、不改 ER、不回填、不改錨。**
**E28**：若量得 TC 2／TC 4 之錨即為 `4819144`／`4820117`（主詞為 ICS 面板），
**停下回報** —— 那表示該二條可能錨在非本 DUT 之行為上，屬範圍事項。

---

### 作業 E — 常設自檢集

1. **圍籬 diff**（R-ICS38(a)）：對 `docs/reports/14_rulings_snapshot.md`。
   預期新增 `R-ICS45`＋`R-ICS46` 二條、刪除 0 行。**不碰 git。**
2. 候選篩（R-ICS34）：二數並報＋殘餘率（前六包 53／53／43／52／47／47%）。
3. 未錨定斷言（R-ICS32(c)）：3（弱驗證）＋6（已標明）。
4. **五支 gate**（新增 `verify_reference_binding`）開工前／完工後各一跑；差值報出。
   **開工前基線含 `lint_docs036` 之紅（成因在 `features/power/`，非本包所致，不修）。**
5. 開工時重測本包 sha256（R-ICS17(e)）。
6. 完工時存 `docs/reports/15_rulings_snapshot.md` —— **回凍之新基準**。

---

## §4 停下回報條件

沿 E1／E9／E18，並：

- **E26**：作業 A 判出任何一條既有 TC 受世代差異影響 → 停下，不進 B／C。
- **E27**：`verify_reference_binding` 首跑顯示既有 10 鍵中任一 sha 不符 → 停下。
- **E28**：TC 2／TC 4 之錨即為 `4819144`／`4820117`（主詞 ICS 面板）→ 停下。
- **E29**：作業 A 之 dbc 清單重建若發現**第五支** → 停下回報。
- **E30**：作業 C 步驟 5 判 `(supporting observation)` 須改，而該改動會牽動
  **ER 之驗證目標**（非僅標記）→ 停下，不改。

---

## §5 預期數字（審查基準）

**凡有列舉者，數字自列舉長度取得（A-ICS72 之拿法）。**

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；`## R-ICS` **53** 行（相異 **46**）、A-ICS **99**、DR **21／21**；無重複條號 |
| 2 | 圍籬 diff | 新增 **`R-ICS45`＋`R-ICS46` 二條**、刪除 **0** 行 |
| 3 | 作業 A：已用訊號全集 | **實測值**（不預設）|
| 4 | 作業 A：四支 dbc 之差異分類 | 四類各有實數 |
| 5 | 作業 A：受影響之既有 TC | **0**（若非 0 → E26 停）|
| 6 | 作業 B：`feature.yaml` `reference:` 鍵數 | **10 → 11** |
| 7 | 作業 B：`FORMS.md` 變動 | **僅 BHCAN2 一列之「使用 feature」欄**；其餘 0 |
| 8 | 作業 B：`verify_reference_binding` 首跑 | **11／11 相符**（若非 → E27 停）|
| 9 | **`features/display/`／`features/vehicle_setting/` 變動** | **0 處** |
| 10 | 作業 C：回填處數 | **12 減去 TC 2／TC 4 所佔者**（實測值）|
| 11 | 作業 C 後之佔位總數 | **18 － 回填處數**（實測值）|
| 12 | `verify_verbatim` | **31／31**（上半未動）|
| 13 | TC 總數 | **31**（不變）|
| 14 | Test Set 相異值 | **5**（不變）|
| 15 | 錨變動 | **0 處** |
| 16 | 作業 D | 二條全文逐字；前提建立法三分之一；錨逐條列 |
| 17 | 候選篩 | 二數並報＋殘餘率 |
| 18 | 五支 gate | 差**皆 0** |
| 19 | **git 指令執行次數** | **0**（含唯讀）|
| 20 | 快照 | `docs/reports/15_rulings_snapshot.md` 已產出 |

---

## §6 上繳包要求

`docs/upstream/15_binding_and_backfill.md`。沿 upstream-14 之節構，並須含：

- §1 裁決指紋（R-ICS1～R-ICS46 ＋ 全案 R-17／R-G41）＋前提驗證＋圍籬 diff
- 作業 A～E 之結果；**回填後之逐處全文**（訊號名、值、reasoning 追記）
- **§n 未結 DR 清單（21 條）**
- **結果三分法**
- **獨立判斷**：本包是否仍有該驗而未驗者；
  以及 —— **DR-ICS8 是否可標「可結」**（只建議不裁）：
  若 12 處未全回填，其殘餘之處與所繫
- 建議登錄之 anomaly（編號由分析層取）

---

## §7 本包之次序為何是這樣

**因為「訊號解析正確」是綁定與回填共同的前提，而那個前提上一包才被發現沒量過。**

本 DUT 是 R1L，我們十四包都在 R4／R5 上解訊號。若 R1 與 R4／R5 在已用訊號上有差，
現在綁定的是對的檔、回填的卻是錯的值 —— **而且錯得看不出來**，
因為訊號名會對、值名也會對，只有位元佈局或值域悄悄不同。

作業 A 先跑，就是為了讓 B 與 C 站在量過的地上。
若 A 判出差異，E26 停 —— 那一停比填完再退回便宜得多。
