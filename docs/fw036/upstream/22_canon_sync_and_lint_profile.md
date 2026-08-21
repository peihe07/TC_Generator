# 上繳包 22：canon 同步 ＋ lint feature-scoped 改寫

來源：17 包 §四、20 包 §五、21 包 §五之「另立包」裁定，
以及上繳 21 §六-1／§六-2 之二項缺口。**無下放包，由 Pei 口頭指示執行。**
日期：2026-08-21　　**工作簿未動**（`pm_19.xlsx` 雜湊 `b4dd5ca0…`）。

---

## 一、canon §8.7.5 同步為 R-1 v3

`docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5 原載 R-1 v2 條文，
而台帳已於 21 包將 v2 標 SUPERSEDED、v3 標 ACTIVE ——
**條文全文所在之檔案與台帳相牴觸**。已改寫為 v3：

| 項 | 內容 |
|---|---|
| (a) | 訊號一律 `$<MESSAGE>.<Signal>$`，值 `= <raw> (<label>)`，label 取自 DBC `VAL_` |
| (b) | 觀察步驟須寫出應觀察之值（R-11(b)） |
| (c) | `PROXI <Param> = <值>`，**不加 `$`** |
| (d) | 內部訊號優先轉可觀察 CAN 訊號；**DBC 查無對應者保留來源名不加 `$`**（17 包 §三修訂） |
| (e)(f) | 保持／等待、baseline —— 內容同 v2，未變 |
| **(g)** | **R-13**：規格訊號名與 DBC 不符時保留原文名，不得代以語意相近之他訊號 |

依 R-TM13 於節末新增「沿革」小節，**v2(a)–(d) 以刪除線逐字保留**，
並記三段撤銷／修訂理由（12 包之 `$` 指派相反、17 包 §三之 (d) 再修訂、
19 包 `PowerModeSts_Telematic` 一案促成 (g)）。

台帳「條文落檔位置」表已改指：`R-1 v3` 與 `R-13` 皆指向 canon §8.7.5，
不再指向 handoff 檔。

---

## 二、lint feature-scoped 改寫

### 2.1 `scripts/lint036.py` 新增 `--profile <feature>`

未指定時**行為與 21 包之前完全一致**；指定時：

| 檢查 | 內容 | 依據 |
|---|---|---|
| **P**（改判準） | 三件組殘留／`Send CAN:` 舊式／訊號賦值未以 `$` 包覆／賦值缺 `(<VAL_ label>)`／`PROXI $X$` | R-1 v3(a)(c) |
| **Q**（新增） | 不可見字元：NBSP、全形空格、行尾空白 —— **全欄位含 verbatim 上半與 spec** | R-10(a) |
| **R**（新增） | Pre-Condition 未編號行／多條件並列於同一行 | R-9(a) |
| **T**（新增） | `PENDING:` 說明含非 ASCII 字元 | R-14 |
| **U**（新增） | `PENDING:` 佔位逐一列出（四欄全掃，**含 ER 側**） | A-PM16 |

**U 之用意**（20 包 §四／21 包 §五所令之「併入 A-PM16 之 ER 側檢查」）：
`verify.py` 之 `read_without_value` 僅施於 `proc`，致 ER 側之 `PENDING` 行
「未被覆蓋」與「通過」無從分辨。U 不判對錯，**只令其於報告中可見**。

### 2.2 迴歸：既有九本無 `--profile` 之報告**位元組全等**

語料（九本，含非零案例）：comfort ×2、power inputs、privacy、sxm、
time_management、user_profiles、vehicle_setting、`pm_19.xlsx`。

```
九本迴歸（無 --profile）：位元組全等 —— PASS
```

其中 vehicle_setting 之基線為
`B=134 F=2 I=234 L=230 M=329 N=121 P=16`（非零），
故該迴歸具鑑別力，非全零之空比對。

> 為達「位元組全等」，profile 標示行改為**僅於指定 profile 時**插入報告，
> 未指定時報告內容與 21 包之前逐位元組相同。

### 2.3 profile 模式之實測

| 對象 | 結果 |
|---|---|
| `pm_19.xlsx`（改寫後） | `A–N=0`、**`Q=0 R=0 T=0`**、`P=10`（全在 `test_item` 括號下半）、`U=10` |
| `pm_10a5b.xlsx`（改寫前，**紅向 fixture**） | **`P=124`、`Q=205`、`R=49`** |

`Q=205` 與 13 包所報之「上半 NBSP 205 行」逐數相符 ——
**該三項檢查確實會叫**，非恆為零之擺設。
`U=10` 即 rows 73／74／119／245（各 proc＋er）與 row 291（proc＋er）。

### 2.4 `scripts/lint_docs036.py`（`docs_structure`，新檔）

21 包 §五所令。檢查台帳／DR／ANOMALIES 三份治理文件：

- 台帳：編號格式與重複、狀態值合法性（`ACTIVE`／`[DEFAULT]`／
  `SUPERSEDED`／`WITHDRAWN`）、條文欄非空、`R-n` 序號連續性、
  每條須列於落檔位置表、**落檔位置表不得使用「同上」**（A-PM17）
- DR-PW／A-PW／A-PM：序號連續性與重複（R-TM13：撤回列不刪、不重編號）
- 三檔共通：**表格列以 `|` 起而不以 `|` 收**（渲染錯位）

**未併入 `lint036.py`**：後者之輸入為 `.xlsx`，本檢查之輸入為 markdown，
共用一支 CLI 將使參數語意分裂。二者於同一包交付，職責分立。**請追認。**

### 2.5 `docs_structure` 首跑即攔下三項真實缺陷

| 缺陷 | 性質 |
|---|---|
| `DATA_REQUESTS.md` 之 **DR-PW12 列缺結尾 `|`** | 既有缺陷，該列於 markdown 下渲染錯位。已補 |
| `RULINGS_LEDGER.md` 之 **S6 列缺結尾 `|`** | **21 包執行層所致** —— 加註「併見 R-14」時寫在最後一格之外。已改為置於格內 |
| **DR-PW19 從未登載** | 15 包立、16 包撤回，而 `DATA_REQUESTS.md` **無其列** —— 違 R-TM13（撤回不刪、不重編號）。已補撤回列 |

第二項為本工具攔下之**自身當包缺陷**；第三項為跨六包無人發現之遺漏。

修正後：`docs_structure：PASS`。

### 2.6 測試

- `tests/test_lint036.py`：新增 **19 項**（profile 開關、Q／R／T／U 各一正一反、
  P v3 六項含 `PENDING` 佔位不誤判為缺標籤）。原 67 項全數維持。
- `tests/test_lint_docs036.py`：**新增 12 項**（含「長條目被空行切成獨立表格時
  不得跳過表首」—— 該案為本工具開發時實際踩到之誤報）。
- `tests/test_lint036.py::test_every_check_has_status_and_granularity`
  之斷言改以 `check_order("power")` 為母體（原以 `CHECK_ORDER`）。

```
tests/test_lint036.py tests/test_lint_docs036.py  →  99 passed
```

---

## 三、本包是否仍有該驗而未驗者 —— 執行層獨立判斷

**有，五項。**

1. **`--profile` 之值目前不影響判準內容。** 任何非空字串都啟用同一組
   Q／R／T／U 與 P v3；`power` 與其他 feature 之差異未實作。
   現階段僅 PM 依 v3 撰寫，故無實害；**但「profile」之命名已承諾了
   per-feature 差異化，而該能力不存在。** 若日後他 feature 需要不同判準，
   須先設計 profile 表，勿逕自沿用。
2. **P v3 之 `RE_P3_BARE_ASSIGN` 可能誤傷。** 其判 `<全大寫MSG>.<Sig> =`
   未包 `$` 者為違規，然全大寫加點之字串未必皆為 CAN 訊號
   （例如某些檔名或常數）。九本迴歸中未觸發，
   **但該迴歸之九本皆未以 profile 模式跑過** —— profile 模式僅實測 PM 兩本。
   他 feature 首次啟用 profile 時須重新校準。
3. **Q 檢查與 R-10(b) 之其餘項未實作。** R-10(b) 尚有彎引號、方括號、
   行尾句號、破折號、連續空格、標點前空格 —— 其中方括號與行尾句號
   已由既有 F／N 承接，**彎引號／破折號／連續空格三項無任何檢查**。
4. **`docs_structure` 不驗 R-15。** 「條文全文不得簡寫」須比對下放包字串
   與台帳字串是否等同，而下放包為自由格式 markdown。
   20 包上繳 §五-3 已指出，本包未解決，**維持人工項**。
5. **`--gate` 仍未啟用**（S3）。二支工具皆備 `--gate`，但未接入任何流程；
   `lint_docs036.py` 目前為 PASS，**是接入 CI 之最佳時點** ——
   一旦再度劣化，其修復成本高於現在接入之成本。

另二項為既有且非本包所生：
- `tests/test_single_write_path.py` 與 `tests/test_intake_scaffold.py`
  合計 **8 項失敗**，全部落在 `features/user_profiles/`（新增之
  `openpyxl` save 呼叫點三處）與 `_intake`。
  **已以 `git stash` 驗明：本包之改動全數移除後，該 8 項仍失敗**
  —— 與本包無關，於此登記。
- `lint036.py` 之 `report_stem()` 對兩本不同 feature 產生同一 tag
  （`20260817_ext`），後者覆寫前者之報告。既有行為，本包未動。

---

## 四、引用之裁決編號

R-1 v2（SUPERSEDED）、**R-1 v3**（canon §8.7.5 落檔）、R-6、R-7、
R-9、R-10(a)、R-11(b)、R-13（canon §8.7.5(g)）、R-14、R-15、
R-TM13、S3（gate 政策）、S6。
關聯異常：**A-PM16**（U 檢查之由來）、**A-PM17**（`docs_structure` 之由來）。

---

## 五、未做之事

- **未改工作簿**、未送達、未覆寫任何交付本。
- 未啟用 `--gate`。
- 未實作 per-feature 之判準差異（見 §三-1）。
- 未處置 `features/user_profiles/` 之 8 項既有測試失敗。
