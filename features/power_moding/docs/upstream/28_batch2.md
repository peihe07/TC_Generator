# 上繳包 28 —— 覆核線之收束、apparatus 凍結與 batch 2

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/28_batch2.md](../handoff/28_batch2.md)
- 前一包上繳：[27_verdict_for_every_cell.md](27_verdict_for_every_cell.md)
- **本包零寫回工作簿**

**27 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`（待授權）`）——
**⚠ 更正：27 包尚未提交**，其異動仍在工作區內，本包之 pathspec 須併含之。

---

## ⚠ 本包之三項須先看

1. **停止條件 7 觸發並已解** —— batch 2 之音訊斷言與矩陣 `r45`
   （`Mute Button Pressed` → `Mute --> Active`）**牴觸**；
   **六條 TC 各加兩項事件層限定**後解除。（§5.3）
2. **`-014`（`Never`，負向）之限定不可省，其理由與正向相反** ——
   **靜音會使該條以錯誤之理由通過**（canon §7 之 false pass）。（§5.3）
3. **本包新增 0 支檢查程式、0 項檢查**（R-PMH104 自檢）——
   **兩處既有檢查之一般化不計為新增**，其理由具名於 §5.2。

---

## 一、§三二條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH103 | 覆核線之收束判準（實質項 vs 精化項） | 369 | `fb29dcf1d6aac404` | `fb29dcf1d6aac404` | ✅ |
| R-PMH104 | apparatus 凍結；其解凍條件 | 323 | `7703ef72dbbf2c85` | `7703ef72dbbf2c85` | ✅ |

**命中數**：handoff 2 塊、RULINGS 回讀 2 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH100`／`R-PMH102` SHA256 皆相符。

---

## 二、三項實質項之處理（步驟 2）

### 2.1 (a) —— 「待判定」不再計入「已判定」

`popup`／`popup_after` 之各 21 格由 `未對照` 改記 **`待定義`**
（R-PMH85 之第四詞）。**其理由**：`未對照` 為一個**已作成之判定**，
而該 21 格之判定**尚未作成**（其列層記法在 `matrix_vs_chapter.VERDICT`）。

| | 27 包 | **28 包** |
|---|---|---|
| `popup` | 未對照 174 | **待定義 21**／未對照 153 |
| `popup_after` | 未對照 174 | **待定義 21**／未對照 153 |
| `verdict_form.py` 之合計 | 未對照 879／待定義 4 | 未對照 **879**／**待定義 46** |

### 2.2 (b) —— PC 之全枚舉：**4,176 項判定取代 21 個零命中探針**

```
=== 結果 ===
  **`pre_conditions` 之斷言 24**（R-PMH102 新入母體）／**`expected_result` 之斷言 26**（`-007` 另計）
  二分（R-PMH97）：SUT **48**／測試執行 **2**
  記法：牴觸 **0**／印證 **1**／未對照 **47**／待定義 **0**
  未具名 **0**

  === `test_procedure` 之逐步驟二分（28 包步驟 2(c)，R-PMH97）===
  步驟總數 **25**；未具名 **0**；**歸為 SUT 斷言者 0**
  **全部歸為測試執行斷言，其對象皆由對應之 ER／PC 斷言承載並已入母體。**
  ⚠ 三步驟另具名其隱含之 SUT 前提：
     `-003` 步驟 2 之 `until the screen changes` → ER2.2（27 包查出者）
     `-004` 步驟 2 之「逾時長度已知」→ 規格未給秒數，以「長於」表述（§8.4.1）
     `-007` 步驟 5 之「SUT 能接收該報導」→ PC2.1，已入母體

  === PC 之全枚舉（28 包步驟 2(b)，R-PMH98／R-PMH100）===
  **24 個 PC 斷言 × 174 格 = 4176 項判定**（非零命中探針）
  記法分布：{'未對照': 4166, '印證': 10}
  待定義（入選而未具名）：**0**
  **21 個「零命中探針」之依據自此由 4,176 項逐格判定取代。**
```

**24 個 PC 斷言 × 174 格 = 4,176 項**；記法分布
**未對照 4,166／印證 10／待定義 0／牴觸 0**。

**十個印證**（先前為「零命中探針」所看不見者）：

| PC 斷言 | 格 | 記法之依據 |
|---|---|---|
| `-008` PC1 `The radio is in Power Button Off state` | `r7c13`／`r8c12` | `Power Button remains off with open and closure of door` —— **同一謂詞取相同值**，矩陣支持該前提可被**維持** |
| 同上 | `r40c2`～`c5` | `Power press OFF > … (Power Button OFF state)` —— 矩陣支持該前提之**可達性** |
| `-008` PC3 `No phone call scenario is in progress` | `r26c4`／`c5`／`c8`／`c9` | **矩陣以 `Call Not Active` 為一個成立之欄軸** —— 其存在即支持該前提可被建立 |

**其 33 個 `Call Active` 欄之格判 `未對照`，依據為欄軸本身**（二者不可同時成立）。

### 2.3 (c) —— `test_procedure` 之逐步驟二分：**25 步全具名，SUT 斷言 0**

**三步驟另具名其隱含之 SUT 前提**：

| 步驟 | 隱含之 SUT 前提 | 其承載處 |
|---|---|---|
| `-003` 步驟 2 `until the screen changes` | 畫面逾時 | **ER2.2**（27 包 §3.3 所查出者，已入母體） |
| `-004` 步驟 2 「逾時長度已知」 | —— | **規格未給任何秒數**，故以「長於」表述（§8.4.1 不造值） |
| **`-007` 步驟 5 `Deliver a traffic announcement…`** | **SUT 能接收該報導** | **PC2.1**（`A traffic announcement is available to be received`），已入母體並判未對照 |

**28 包步驟 2(c) 所指名之 `-007` 步驟 5 已具名判定 → 停止條件 8 未觸發。**

---

## 三、三項精化項入 KNOWN-INCOMPLETE（步驟 3）

已寫入 `DECISIONS.md`，**各附風險陳述，不再排程**：

| 項 | 風險陳述之要點 |
|---|---|
| 切分之連接詞仍是列舉 | 某 ER 含兩命題而只判為一個，其一因而未掃 —— **27 包之 `-003` ER2 即此形態之實例（已修），惟該次是靠 `while` 被列入才抓到** |
| `SPLIT_REVIEW` 無第二來源 | 產生候選與複核為同一人；某候選被錯判為「非獨立命題」而併回 |
| 規格側全枚舉未做 | 規格某行與某斷言取相反值而其用詞未被關鍵詞命中 —— **23 包之 `pop-up` 掃描曾以關鍵詞查出 p9 兩行（A-PMH21），故該風險非理論** |

---

## 四、batch 1 之覆核結束宣告（步驟 4）

已寫入 `DECISIONS.md`：

> batch 1（8 條 TC，7 leaf）之覆核線依 **R-PMH103** 結束。
> 其殘餘為三項精化 ＋ `-007` 之 `L160` 待確認（`DR-PMH7`）。
> **batch 1 仍不得寫回工作簿，其阻斷改為單一項**：
> `tc_id` 為 provisional，待全 **47** leaf 完成後單次指派（12 包 §五）。

---

## 五、batch 2 —— `Startup Sounds`（步驟 5）

### 5.1 產出

| tc_id | leaf | outline | pri | design method | 標題 |
|---|---|---|---|---|---|
| `NR1L-DisclaimerScreen-009` | `SWE1-HMI-PM-012` | 8.1 | P1 | 狀態轉換 | Start-up sounds start on driver door close and sync with the animation |
| `NR1L-DisclaimerScreen-010` | `SWE1-HMI-PM-012` | 8.1 | P1 | 狀態轉換 | Goodbye sounds sync on start with the shut-down animation |
| `NR1L-DisclaimerScreen-011` | `SWE1-HMI-PM-013` | 8.2 | P1 | 功能測試 | The sound setting offers Always, Once a Day and Never options |
| `NR1L-DisclaimerScreen-012` | `SWE1-HMI-PM-014` | 8.2.1 | P1 | 等價劃分 | Always plays the sounds every time the startup animation is played |
| `NR1L-DisclaimerScreen-013` | `SWE1-HMI-PM-015` | 8.2.2 | P1 | 等價劃分 | Once a Day plays the sounds only once per day |
| `NR1L-DisclaimerScreen-014` | `SWE1-HMI-PM-016` | 8.2.3 | P1 | 負向測試 | Never plays no start-up or goodbye sound in any situation |
| `NR1L-DisclaimerScreen-015` | `SWE1-HMI-PM-017` | 8.3 | P2 | 功能測試 | Sound volume level matches the current entertainment sounds volume |

**7 條 TC 自 6 leaf** —— `SWE1-HMI-PM-012` 依 profile §4「不同觸發即拆分」
拆為 2 條（**駕駛門關閉**／**關機動畫開始**）。

**priority 分布**：P1 **6**／P2 **1**。
**P2 唯一者為 `-015`**（音量位準），其依據為「其失效不使任何功能缺失」——
**與 P1 六條之「音效行為錯誤」不同量級**（R-PMH59：批內依據互不矛盾）。

**`source_clause` 六段逐字取自 PDF p8**（R-PMH50），`origin` = `spec_pdf p8`。

### 5.2 ⚠ **兩處既有檢查之一般化 —— 其為何不計為 R-PMH104 之新增**

batch 2 之 `test_set` 為 `Startup Sounds`，而 lint 有兩項檢查為 **batch-01 專屬之硬編碼**：

| 檢查 | 原 | 改為 |
|---|---|---|
| `R-PMH36 test_set = 'Disclaimer Screen'` | 硬編碼字串 | **讀該批之 `test_set` 欄**，驗各 TC 與其相同 |
| `本批 leaf == Disclaimer Screen 之 7 leaf` | 硬編碼 7 個 leaf id | **讀該批之 `leaf_scope` 欄**（且其不得為空） |

**檢查項數不變（32 → 32），檢查之語意不變（仍驗同一件事）** ——
**改變者為其取得期望值之方式：由寫死改為讀該批之宣告。**
**故不計為 R-PMH104 之新增。**（`batch01.json` 亦增 `leaf_scope` 欄以配合。）

**⚠ 一項副作用須具名**：`batch01_r2.json` 之 must-hit fixture **多 FAIL 一項**
（其無 `leaf_scope` 欄），**其仍 FAIL 故 must-hit 之效力不變**。

### 5.3 ⚠ **停止條件 7 觸發並已解 —— batch 2 之音訊斷言 × `r45`**

依步驟 6 對 batch 2 之各斷言重跑 `audio` 掃描：

| | 逐字 |
|---|---|
| batch 2 之音訊斷言（`-009`／`-010`／`-012`／`-013`／`-014`／`-015`） | `The sound is played…`／`No … sound is played…`／`its volume level is recorded` |
| 矩陣 `r45`（`Mute Button Pressed`，`Key On, Gear != Reverse`） | **`Mute --> Active`**（使聲音不可聞） |

**共同謂詞取相反值；其欄軸與 batch 2 之相位重疊；條件互斥未證 → 牴觸**（R-PMH84）。

**處置（R-PMH87／R-PMH94／R-PMH95）**：**六條各加兩項事件層限定**——

```
1. Do not press the Mute key or the Headunit Mode key      （11 字）
2. Do not change the headunit mode by voice recognition     （9 字）
```

**`r46`／`r47` 之納入不是因為判定其為牴觸** —— 其 `Else: Mute Active`
記法未定義（**A-PMH22**），依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。

**⚠ `-014`（`Never`，負向）之限定不可省，其理由與正向相反**：
正向之風險是「靜音使 TC 誤判為失敗」；
**負向之風險是「靜音使 TC 以錯誤之理由通過」**（canon §7 之 false pass）。
**已於其 `reasoning` 具名。**

**`-011`（設定選項之存在）未加限定** —— 其 ER 不涉音訊，**謂詞不同**。

**⚠ 一項未涵蓋須具名**：R-PMH99(c) 之 lint 字串檢查**只施行於 `-007`**
（其以 tc_id 判定）。**batch 2 之十二項限定（6 條 × 2）不在其射程內** ——
**擴及之即為新增檢查項，依 R-PMH104 不做**；據實記載。

### 5.4 逐 TC 之關鍵判定（節錄其 `reasoning` 之要點）

| tc | 要點 |
|---|---|
| `-009` | 跨螢幕同步（`Sounds will sync amongst all supported vehicle displays.`）**併入本條之 ER 而不另立一條**（canon §5.7 同一觸發之必然後果不拆）—— **該決定據實記載，其亦可讀為獨立之能力** |
| `-010` | `sync on start` 之 `on start` 逐字承載於 ER；**不斷言其結束時之行為**。**關機動畫之觸發條件不在射程**（`SU4.)` 屬 `Startup Animation` 組，§8.5） |
| `-011` | **只驗選項之存在，不驗其行為**；⚠ **規格未給該設定之所在路徑**，故 pre-condition 不指任何選單層級 |
| `-012` | `everytime` 以**連續兩次播放**承載（證明「非只一次」之最小次數）；**不斷言任何次數上限** |
| `-013` | ⚠ **規格未定義「一日」之起算點**（午夜？點火週期？）—— pre-condition 只寫「今日尚未播放過」，步驟只說 `on the same day`。**該未定義已具名，若上游另有定義則本條須重寫** |
| `-014` | `on any situation` 以**三個已知觸發**承載（門關閉／開機動畫／關機動畫）—— **該三者為規格於 ch 8 所載之全部觸發**；⚠ **「any situation」之涵蓋不可窮舉，其餘情境未驗**（NEG 之固有限度） |
| `-015` | ⚠ **規格未給任何音量單位或容差**（只說 `match`）—— ER 只斷言「相符」而不給數值 |

---

## 六、lint 全跑（步驟 6）—— **32 項，不得增減**

```
batch = batch02；TC 數 = 7；leaf 數 = 6

  R-PMH50 每 leaf 有 source_clause 且非空                       PASS
  R-PMH50 source_clause 取自 PDF（非 SYS1）                     PASS
  profile §3.1 test_item 具下半括號（硬規則）                        PASS
  profile §3.3 design_method ∈ 下拉選單 9 詞條                   PASS
  profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符  PASS
  profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）             PASS
  profile §3.6 estimated_test_time 留白                      PASS
  profile §3.8 vehicle_models 留白                           PASS
  profile §3.7 functional_safety = NA                      PASS
  R-PMH18 test_group = 'Disclaimer screen'（小寫 s）           PASS
  R-PMH36 各 TC 之 test_set == 該批之 test_set（大小寫敏感）           PASS
  R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}             PASS
  test_set ∈ Layer 2 定版 8 組                                PASS
  canon §11 方括號禁止（本 feature 無 profile 例外）                  PASS
  procedure 與 ER 步數一致                                      PASS
  必填欄無空                                                    PASS
  ER 未以 NA 充當未知                                            PASS
  canon §10.5 test_procedure >= 2 步                        PASS
  canon §5.1 procedure 無禁用動詞                               PASS
  canon §5.2B/§5.5 Final Step 含驗證意圖                        PASS
  canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）      PASS
  交付欄位無 markdown 標記（**／__／`）                               PASS
  canon §11 無彎引號                                           PASS
  canon §11 UI 標籤加直雙引號                                     PASS
  canon §5.2 步驟字數（normal <=12／final <=18）                  PASS
  R-PMH53 交叉引用存在且語意相容                                      PASS
  R-PMH99(c) `-007` 之七項限定字串各出現一次                           PASS
  R-PMH99(a) `-007` 每步之限定項數 <= 2                           PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == 其宣告之 leaf_scope（且 leaf_scope 非空）              PASS

32/32 PASS

⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：
    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 `COVERED` 產生，**不手寫**。
    執行：`python scripts/canon_coverage.py`
    本 lint 宣告涵蓋 10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**
    R-PMH52：lint 全綠不得作為 TC 可用之證據。

⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。
  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  本檢查只保證覆核所需之材料存在，不保證覆核已做。
```

**batch 2：32/32 PASS。batch 1：32/32 PASS。**
**兩份 must-hit fixture 仍 FAIL**（退出碼 1）。

---

## 七、由程式產生之檢查總表（R-PMH92）

| 檢查 | must-hit | 退出碼 | 期望 | **結果** | 備註 |
|---|---|---:|---:|---|---|
| `lint_batch.py generated/batch01.json` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `lint_batch.py generated/batch02.json` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `lint_batch.py <fixture prerework>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py <fixture r2>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py --limit-must-hit` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `check_granularity.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --check-doc-sync` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --doc-sync-must-hit` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_write_back.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 三項故意失敗全被攔下 |
| `marker_coverage.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --verify-extraction` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --window-compare` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `canon_coverage.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其只做差集，無刻意構造之反例 |
| `check_state_consistency.py` | ✅ | 0 | 0 | **PASS** | `--self-test` 之故意注入 |
| `challenge_rulings.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其判準為標記列舉，R-PMH67 之抽樣非 must-hit |
| `tsv_vs_pdf.py --truncation` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 只做逐字比對之量測 |
| `chapter_bidirectional.py 7..12` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --partition` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --source-must-hit` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --export-residue` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `matrix_vs_chapter.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 8` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 11` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 12` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 7` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`r48` × `SU3.)`）→ 退出碼 1 為設計 |
| `matrix_vs_chapter.py 10` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`10.3` × `r48c10`，已登記 R-PMH80）→ 退出碼 1 為設計 |
| `spec_assertion_scan.py --assertion popup` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --assertion audio` | ✅ | 1 | 1 | **PASS** | **查出牴觸 1**（`r45` × `-007` ER4(b)，24 包）—— **25 包已以第 5～7 項限定排除之，其牴觸記錄保留** |
| `spec_assertion_scan.py --assertion announcement` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --assertion popup_after` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --cell-must-hit` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `spec_assertion_scan.py --spec-population` | ✅ | 0 | 0 | **PASS** | `--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確** |
| `batch_er_vs_matrix.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入 |
| `verdict_form.py` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |
| `verdict_form.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |

**未註冊 must-hit 而標「未實測」者 = 4**  ← R-PMH92：其不得標 PASS

> 本表由 `python scripts/check_table.py` 產生。**手寫之結果欄不予採認**（R-PMH92）。

---

## 八、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— `DR-PMH5`／`DR-PMH7` |
| 2 | 判準衝突未決 | **是** —— `10.3` × `r48c10`（已登記，`DR-PMH6`） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| **7** | batch 2 之任一斷言掃描發現**牴觸** | **`r45` × 音訊斷言，牴觸 1** | **觸發 → 已解**（六條各加兩項限定，§5.3） |
| 8 | 步驟 2(c) 發現某步驟實為 SUT 斷言**且未經掃描** | 25 步全歸測試執行；三處隱含 SUT 前提**皆已由 ER／PC 承載並入母體** | **否** |
| 9 | **本包新增任何檢查程式或檢查項**（R-PMH104 之自我檢查） | 新增 **0 支程式、0 項檢查**；兩處為既有檢查之**一般化**（§5.2） | **否** |

---

## 九、未結 DR 清單（R-PMH82）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | p9 矩陣之來源 | **`DRAFT`** | **（待填）** | **ch 9 之 7 leaf** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` ／ `Else: Mute Active` ／ `Note:` 之範圍（三問） | **`DRAFT`** | **（待填）** | 矩陣對照之四列 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第七次空著。**

**`DR-PMH7` 之第二問（`Else: Mute Active`）於本包再度生效** ——
batch 2 之六條 TC 之限定即為繞過它而加。

---

## 十、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，五項。**

1. **batch 2 之七條 TC，其斷言之逐條掃描我只做了 `audio` 一類。**
   `-009`／`-010` 之 ER 含 `animation`（開機／關機動畫）之斷言，
   **而 `animation` 不是現行四個斷言之任一** ——
   **依 R-PMH94 它該有自己的一次掃描，而新增斷言即新增檢查項（R-PMH104）。**
   **我停在這裡並具名，未自行擴充。**

2. **`-013` 之「一日」與 `-011` 之「設定路徑」皆為規格未定義。**
   我以「不造值」處理並具名，**但未開 DR** ——
   **二者與 `VP`／`Else: Mute Active` 同為「素材未定義」之類，
   依 R-PMH85 之形態本該開 DR。我沒有開，因為 R-PMH104 之凍結不及於 DR，
   而我判其「已由措詞繞過」** —— **該判斷與 A-PMH22 之處置一致，惟其未經裁定。**

3. **batch 2 之七條未經任何人讀覆核。**
   batch 1 曾在 12 包被 Pei 判「產出面不通過」而重寫。
   **本批之 lint 32/32 只證明其合於已編碼之規則。**

4. **`-009` 之「跨螢幕同步併入而不另立一條」是我的判斷。**
   canon §5.7 支持之，**惟該子句亦可讀為一個獨立能力**
   （`Sounds will sync amongst all supported vehicle displays.` 為獨立句），
   **若如此則 leaf 012 應拆為三條而非兩條。**

5. **R-PMH99(c) 之字串檢查不及於 batch 2**（§5.3 末）——
   **batch 2 之十二項限定無任何機器檢查保護其不被刪去或重複。**

---

## 十一、建議之 commit 與 pathspec（**不執行**）

**⚠ 27 包尚未提交，其異動與本包併存於工作區** —— 本 pathspec 併含之。

**訊息**：

```
feat(power_moding): packages 27-28 — verdict for every cell, review line closed, batch 2 (Startup Sounds)
```

**pathspec（逐一具名，R-G12）**：

```
git commit -- \
  features/power_moding/DECISIONS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/27_verdict_for_every_cell.md \
  features/power_moding/docs/handoff/28_batch2.md \
  features/power_moding/docs/upstream/27_verdict_for_every_cell.md \
  features/power_moding/docs/upstream/28_batch2.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/generated/batch02.json \
  features/power_moding/scripts/batch_er_vs_matrix.py \
  features/power_moding/scripts/check_table.py \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/gen_batch02.py \
  features/power_moding/scripts/lint_batch.py \
  features/power_moding/scripts/spec_assertion_scan.py \
  features/power_moding/scripts/verdict_form.py
```

（實為 **16 路徑**。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **只增 `leaf_scope` 欄**（配合檢查之一般化）；八條 TC 之內容未動 |
| `generated/batch02.json` | **新增** —— 7 條 TC，`tc_id_status: provisional` |
| `ANOMALIES.md`／`DATA_REQUESTS.md` | **未動** |
| State Matrix xlsx／規格 PDF | **只讀** |
| **新增之檢查程式／檢查項** | **0 支／0 項**（R-PMH104 自檢通過） |
| **對外發文** | **無** |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`features/display`、`docs/runtime/`） | **未動** |

---

## 十二、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出** —— 第七次。`DR-PMH5` 凍結 ch 9 之 7 leaf | **ch 9** |
| 2 | **batch 2 之人讀覆核**（§10 第 3 項）—— lint 32/32 只證明合於已編碼之規則 | batch 2 之寫回 |
| 3 | §10 第 1 項 —— `animation` 斷言之掃描未做（新增斷言即新增檢查項，R-PMH104） | batch 2 之寫回 |
| 4 | §10 第 2 項 —— `-013` 之「一日」與 `-011` 之「設定路徑」未開 DR，其判斷未經裁定 | 否 |
| 5 | §10 第 4 項 —— `-009` 之跨螢幕同步是否應獨立為第三條 | 否 |
| 6 | 9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |
