# 上繳包 19：更正回復 ＋ 軌 C 補列 ＋ 三項裁決

下放：`docs/fw036/handoff/19_pm_final.md`
日期：2026-08-21　　**止於工作副本，未送達、未覆寫交付本。**

| 項 | 值 |
|---|---|
| 基底 | `features/power/sandbox/b18/pm_18.xlsx`（`c61a6d55…`） |
| 產出 | `features/power/sandbox/b19/pm_19.xlsx`（`b4dd5ca0…`） |
| 寫回 | `features/power/scripts/b19/apply.py` —— `surgical_save` 唯一路徑 |
| 改動 | **6 列／24 格**（rows 72、271、272、273、274、291） |

---

## 一、驗收 —— **十二項全表全零**

```
=== 驗收（全 283 列）===
[OK ] input_not_na: 0          [OK ] listed_in_input: 0
[OK ] triplet: 0               [OK ] send_can: 0
[OK ] pre_unnumbered: 0        [OK ] pre_multi: 0
[OK ] pre_first_is_tool: 0     [OK ] pre_last_not_tool: 0
[OK ] step_multi_obs: 0        [OK ] read_without_value: 0
[OK ] nbsp: 0                  [OK ] proc_er_mismatch: 0
```

18 包所餘之 `pre_last_not_tool` 4 筆與 `read_without_value` 4 筆
（即 rows 271–274）**已歸零**。

lint036：

| | A | B | C | D | E | F | G | H | I | I-sib | J | K | L | M | N | P |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 前（pm_18） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| 後（pm_19） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |

**A–N 全零、E = 0**；P 之 10 筆全在 `test_item` 括號下半（各包明令不動）。

x14 讀回 1＋3 個 DV；壓縮成員 **42** 未變；差異成員僅 `xl/worksheets/sheet6.xml`。

### 自 `pm_10a5b` 起算之累計 diff

| 欄 | 變動格數 | 說明 |
|---|---:|---|
| `test_item`（I） | 163 | 僅不可見字元；內容變動 **0** |
| `pre`（J） | **283** | 全部 283 個 TC 列 |
| `input`（K） | 101 | 內聯後改 `NA` |
| `proc`（L） | **283** | 全部 283 個 TC 列 |
| `er`（M） | 277 | 6 列改寫後與原文逐字相同，不計入 |
| `spec_reference`（N） | **0** | 零變動 |
| 其餘各欄 | 0 | 零變動 |

軌 C 30 列四欄皆有變動（`verify.py` 逐列列出，30/30）。

---

## 二、§一 row 72 —— 回復規格原文

依 **R-13** 逐字套用下放所給之三段。`PowerModeSts_Telematic` 不加 `$`
（DBC 無對應，比照 R-1 v3(d)）；觀察側維持 `$STATUS_TELEMATIC.PowerSts_Telematic$`
= `5 (Logistic_On)`。改後四欄殘留 `$STATUS_TELEMATIC.PowerSts_Telematic$`
之誤代入：**0**。

lint P 未因此新增違規 —— `PowerModeSts_Telematic` 無 `.` 分隔，
不觸發 `RE_P_ASSIGNMENT`（其判準要求 `<全大寫MSG>.<Sig>`）。

**已登記**：
- `docs/fw036/RULINGS_LEDGER.md` —— 新增 **R-13**（ACTIVE，源 19 包），
  並於「撤銷紀錄」逐字加註 **17 包 §五之撤銷**（依 R-TM13 不刪除）。
- `features/power/DATA_REQUESTS.md` —— 新增 **DR-PW21（High）**，
  內含兩份 DBC 之 sha256、相近二訊號之對照，並載明
  `STATUS_BH_BCM1.PowerModeSts` 之 VAL_（`0 Standard_Power`／
  `1 Logistic_Mode_ON`／`2 Logistic_Mode_PR`／`3 LogisticModeON_and_EngineON`）
  **與原文二值逐字相符** —— 供上游判斷是否即同一訊號。

---

## 三、§二 rows 271–274 —— 軌 C 補列

| 列 | 型式 | 展開內容 |
|---|---|---|
| 271 | 全文 | 4 步／4 行（Full-Operation 分支，splash ＋ disclaimer） |
| 272 | 全文 | 3 步／3 行（Idle → Timed，僅 disclaimer） |
| 273 | 展開自 272 | 僅 PRE 1 → `The TLM is in Standby state`；PROC／ER 逐字同 272 |
| 274 | 展開自 272 | PRE 1 → `Partial_Operation state`；PROC 1 → `Bring the HU to Full-Operation mode`；PROC 2／ER 2 之值 → `4 (Full_Operation)`；ER 1 → `The HU reaches Full-Operation mode`；PROC 3／ER 3 逐字同 272 |

軌 C 至此 **30/30 完成**。

---

## 四、§三 三項裁決之處置

| 項 | 裁定 | 處置 |
|---|---|---|
| 1 | row 291 二擇一改標 `PENDING: DR-PW22` | 已改 PROC 2／ER 2，其餘三步不動。開 **DR-PW22（Medium）** |
| 2 | 8 列首步抽象動作維持，登記 A-PM15，不標 PENDING | 未改該 8 列；**A-PM15 已入 `ANOMALIES.md`** |
| 3 | A-PM13／A-PM14 條文登入 `ANOMALIES.md` | 已逐字登入（連同 A-PM15，新設「A-PM 系列」表） |

### ⚠ 對裁決 §三-1 之一處措辭偏離

下放令標 `PENDING: DR-PW22 geolocation pop-up 與 disclaimer 之擇一判準`。
該字串含 CJK，直接寫入將觸發 **lint 檢查 K**（CJK 字元，範圍含
`pre`／`input`／`proc`／`er`），與同包驗收條「lint A–N 全零」互斥。

**執行層改以等義英文書寫**：

```
PROC 2: Read the TLM screen and check that PENDING: DR-PW22 (which of the
        geolocation pop-up and the disclaimer is shown)
ER   2: PENDING: DR-PW22 (which of the geolocation pop-up and the disclaimer is shown)
```

DR 編號與指涉不變，僅語言改為英文。中文之描述已逐字載於
`DATA_REQUESTS.md` 之 DR-PW22 條文內。**請追認。**

---

## 五、本包是否仍有該驗而未驗者 —— 執行層獨立判斷

**有，四項。**

1. **`RULINGS_LEDGER.md` 缺 R-9／R-10／R-11／R-12。**
   本包已補入 R-13，但 13／14／15 三包所立之 R-9（PC 版面）、
   R-10（空白正規化）、R-11（一觀察點一步驟）、R-12(a)（PC 句式）
   **從未進入該帳**，其「條文落檔位置」亦缺。
   四條為本次 283 列改寫之主要依據，卻在正式帳外。
   **執行層未逕自補入**（逾本包所令），請分析層決定補記格式。
2. **lint P／Q／R 仍未 feature-scoped 改寫**（17 包 §四已裁「排入、另立包」）。
   現行 P 之判準仍為 R-1 v2；`verify.py` 代行而非共用閘。
   **本次已見其代價**：§四之 CJK 衝突須由執行層自行發現，
   若 Q／R 已入 lint 則該類衝突會在下放階段即被攔下。
3. **`verify.py` 之 `read_without_value` 對 `PENDING:` 行不設限。**
   row 291 之 ER 2 現為純 `PENDING: …`，不含 `check that`，
   但 ER 側本不受該檢查（僅檢 `proc`），故未命中。
   **此為檢查未覆蓋而非通過** —— 若日後 ER 側加檢，該列須另計。
4. **DR-PW21 之答覆可能反轉 row 72。**
   若上游確認 `PowerModeSts_Telematic` 即 `STATUS_BH_BCM1.PowerModeSts`
   （其 VAL_ 與原文二值逐字相符），則 row 72 應改為
   `$STATUS_BH_BCM1.PowerModeSts$ = 0 (Standard_Power)` → `1 (Logistic_Mode_ON)`，
   因果結構亦回復。**現行寫法為 R-13 下之正確處置，但非終局。**

已知且非本包所生：`test_item` 括號下半 10 筆三件組殘留（明令不動）；
A-PM13 之五列重複與 A-PM14 之二列重複待 Pei 裁拆併；
A-PM15 之 8 列不可執行至訊號層。

---

## 六、引用之裁決編號

**R-13（本包新立）**、R-1 v3(a)(c)(d)、R-6／R-6b、R-7、R-8、
R-9、R-10(a)(b)(c)、R-11(a)(b)(c)、R-12(a)、R-TM13（撤銷加註不刪除）、
R-P310(三)、§8.2.1、§8.3、§8.4.1、§10.6、路線 (c)。

**撤銷**：**17 包 §五**（已於 `RULINGS_LEDGER.md` 加註）。

**新開**：**DR-PW21（High）**、**DR-PW22（Medium）**。
**新登記異常**：**A-PM13**、**A-PM14**、**A-PM15**。

---

## 七、未做之事

- 未送達、未覆寫任何交付本、未改 `output/`。
- 未改 `scripts/lint036.py`。
- 未改 `test_item`（除不可見字元）、未改 `spec_reference`。
- 未補記 R-9～R-12 至 `RULINGS_LEDGER.md`（逾本包所令，見 §五-1）。
- 未增列、未刪列、未合併列。
