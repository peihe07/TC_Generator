# 上繳包 29 —— batch 2 之人讀覆核、凍結範圍之界定與 DR-PMH8（含 29a）

- 日期：2026-08-25
- 下放包：[handoff/29_batch2_review.md](../handoff/29_batch2_review.md) ＋ [29a_dr_sent.md](../handoff/29a_dr_sent.md)
- **零寫回工作簿**；`workbook_state = BLANK` 未變

---

## 0. 摘要

| 項 | 結果 |
|---|---|
| 條文抄錄 | **4/4 逐字相符**（R-PMH107～109 ＋ 29a 之 R-PMH110），命中數各 1 |
| batch 2 之四項修正 | **全部完成**，lint **32/32 PASS** |
| **`animation` 掃描** | **⚠ 牴觸 3 處（L299／L300／L301）—— 停止條件 7 觸發，未自行調和** |
| 限定字串檢查之一般化 | 完成；must-hit **19/19**；**檢查項數維持 32** |
| `DR-PMH8` | 已開立（`DRAFT`），全文 SHA256 `b4aa530edf320216` |
| 三筆 DR 之 `SENT` | 已落實（2026-08-25），**`DR-PMH8` 維持 `DRAFT`** |
| 覆蓋缺口 | **A-PMH23** 已登記 |

---

## 1. 條文抄錄核對表（步驟 1）

以程式自 handoff 擷取 fenced block、附加至 `RULINGS.md`、**再讀回**逐 byte 比對。

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH107 | 凍結之範圍界定 | 581 | `a6b76c2f4a928cfe` | `a6b76c2f4a928cfe` | 1 | ✅ |
| R-PMH108 | `-013`／`-011` 開 `DR-PMH8` | 496 | `230743b664d34739` | `230743b664d34739` | 1 | ✅ |
| R-PMH109 | 跨螢幕同步維持併入 | 579 | `6ede4f6c7ae461b2` | `6ede4f6c7ae461b2` | 1 | ✅ |
| R-PMH110（29a） | 三筆 DR 之 `SENT` 落實 | 492 | `68b1a265ba8cbe7e` | `68b1a265ba8cbe7e` | 1 | ✅ |

---

## 2. batch 2 之四項修正（步驟 2）

### 2.1 `-015`：PC2 移為 procedure 步驟（§4.4／§5.6）

`The current entertainment sounds volume has been recorded` **含動作而非狀態**
（canon §4.4 之自測：`record` → NOT a Pre-Condition），且本條正為 §5.6 之
before／after 比較。**記錄移為步驟 3，比較留在 final ER**，PC 只留一項。

> **停止條件 9 之檢查**：`-015` 之 procedure **5 步**、ER **5 條** —— **1:1 維持，未觸發。**

### 2.2 `-014`：`design_method` NEG → EP

`Never` 為合法之設定值，非無效輸入亦非非法操作，故 canon §12 之 first-match 落在
`Input partitioned valid / invalid` → **EP**。`reasoning` 已記明
**§7（覆蓋）與 §12（技術）不同層** —— 本條仍為 §7 所要求之負向配對。

### 2.3 `-009`／`-010`：PC2 之來源與必要性已具名

`reasoning` 各補一句：其來源為 `SSND 2.1)`／`SSND 2.3)`（**他 leaf**），
不加則 ER 於 `Never` 下不成立；**其只出現於 pre_condition，不擴入斷言**。

### 2.4 `-014` 步驟 5：檢查範圍與 ER5 對齊

`check that no sound was played` → `check that no goodbye sound is played`。
**分析層所傾向之前案**（ER3／ER4 已各自承載前兩次）。

### 2.5 修正後之四條全文

#### `NR1L-DisclaimerScreen-009` — Start-up sounds start on driver door close and sync with the animation

- **leaf**：`SWE1-HMI-PM-012`　**design_method**：狀態轉換 (State Transition Testing)　**priority**：P1

**pre_conditions**

```
1. Start-up sounds are supported on this vehicle
2. The start-up sound setting is Always
3. The driver door is open and the head unit is off
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Close the driver door and record the sound output and the animation
4. Read all supported vehicle displays and record their sound output
5. Check that the start-up sound started with the start-up animation
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. The start-up sound starts when the driver door is closed
4. The sound is synchronised amongst all supported vehicle displays
5. The start-up sound is synchronised with the start-up animation
```

#### `NR1L-DisclaimerScreen-010` — Goodbye sounds sync on start with the shut-down animation

- **leaf**：`SWE1-HMI-PM-012`　**design_method**：狀態轉換 (State Transition Testing)　**priority**：P1

**pre_conditions**

```
1. Goodbye sounds are supported on this vehicle
2. The goodbye sound setting is Always
3. The head unit is on and the shut-down animation has not started
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Trigger the shut-down animation and record the sound output
4. Read the start of the goodbye sound and of the animation
5. Check that the goodbye sound started with the shut-down animation
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. The shut-down animation starts
4. The goodbye sound starts at the start of the animation
5. The goodbye sound is synchronised with the shut-down animation
```

#### `NR1L-DisclaimerScreen-014` — Never plays no start-up or goodbye sound in any situation

- **leaf**：`SWE1-HMI-PM-016`　**design_method**：等價劃分 (Equivalence Partitioning, EP)　**priority**：P1

**pre_conditions**

```
1. The start-up and goodbye sound setting is Never
2. Start-up and goodbye sounds are supported on this vehicle
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Close the driver door and record the sound output
4. Play the startup animation and record the sound output
5. Trigger the shut-down animation and check that no goodbye sound is played
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. No start-up sound is played when the driver door is closed
4. No start-up sound is played when the startup animation is played
5. No goodbye sound is played when the shut-down animation is triggered
```

#### `NR1L-DisclaimerScreen-015` — Sound volume level matches the current entertainment sounds volume

- **leaf**：`SWE1-HMI-PM-017`　**design_method**：功能測試 (Functional based ; no specific technique)　**priority**：P2

**pre_conditions**

```
1. Start-up sounds are supported and the setting is Always
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Read the current entertainment sounds volume and record it
4. Play the startup animation and record the start-up sound volume
5. Check that the recorded start-up sound volume matches the recorded entertainment sounds volume
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. The current entertainment sounds volume is read and recorded
4. The start-up sound is played and its volume level is recorded
5. The recorded start-up sound volume level matches the recorded entertainment sounds volume
```


### 2.6 lint 輸出

```
batch01 → 32/32 PASS（exit 0）
batch02 → 32/32 PASS（exit 0）
```

---

## 3. ⚠ `animation` 斷言之掃描（步驟 3）—— **牴觸 3 處，停止條件 7 觸發**

**斷言**：`-009` ER3／ER5、`-010` ER3～ER5（動畫之播放與聲音之同步）。

**矩陣側**：174 格**全枚舉**，**入選 0 格**（實測全簿無任何動畫用詞），
174 格全部以「無共同謂詞」記 **`未對照`**（R-PMH100，「落選」類別已消滅）。
分類錯誤之稽核 **0** 格。

**規格側**：命中 **23 行**，**逐行具名記法**，未具名 **0**。

| 行 | 逐字（節錄） | 記法 | 謂詞 |
|---|---|---|---|
| L19 | `· Reference PDO release for all official graphics and animation examples` | 未對照 | 素材參照 vs 動畫是否播放／是否同步 |
| L39 | `Vehicle Start Up Animation,` | 未對照 | 圖／清單之標籤 vs 動畫是否播放 |
| L91 | `Vehicle Start Up Animation,` | 未對照 | 圖／清單之標籤 vs 動畫是否播放 |
| L175 | `Vehicle Start Up Animation,` | 未對照 | 圖／清單之標籤 vs 動畫是否播放 |
| L224 | `Vehicle Start Up Animation,` | 未對照 | 圖／清單之標籤 vs 動畫是否播放 |
| L269 | `Vehicle Start Up Animation,` | 未對照 | 圖／清單之標籤 vs 動畫是否播放 |
| L282 | `SU1.) When the vehicle’s driver door is closed a startup animation will ` | 印證 | 門關閉 → 啟動動畫是否呈現 |
| L283 | `each). If ignition remains off after animation, screen is black. If igni` | 未對照 | 動畫**之後**之畫面 vs 動畫是否播放／同步 |
| L295 | `SU4.) If start-up animation is supported, it shall start upon driver doo` | 印證 | 門關閉 → 啟動動畫開始；關機動畫開始 |
| L296 | `and conclude within 10s. Begin shut down animation only when you have th` | 未對照 | 關機動畫之**觸發條件** vs `-010` 之「動畫已被觸發」 |
| L297 | `key off, later Radio Shut Down (delayed mode): show outro animation) (DC` | 未對照 | 延遲模式之 outro animation 之例 vs 本批之斷言 |
| L298 | `DS4.1) If doors are removed/not present and ignition is turned to ACC, R` | 未對照 | 門被移除 → 不顯示啟動動畫 |
| L299 | `SU5.) If ignition cycle has not changed the animation should only be pla` | **牴觸** | 同一 ignition cycle 內第二次觸發 → 啟動動畫是否播放 |
| L300 | `- Animation should only play once per CAN BUS wake up upon closing the d` | **牴觸** | 同一 CAN BUS wake up 內重複門關閉 → 啟動動畫是否播放 |
| L301 | `-- If vehicle ignition is turned to ACC, RUN or START ON with the door o` | **牴觸** | 門開著時點火轉 ACC/RUN/START → 啟動動畫是否播放 |
| L302 | `SU6.) If last state is Radio OFF, play startup animation and show applic` | 印證 | 最後狀態為 Radio OFF 時門關閉 → 播放啟動動畫 |
| L303 | `pressed On do not show Start Up Animation.` | 未對照 | 按 Power Button 開機 → 不顯示啟動動畫 |
| L304 | `SU7.) Start up animation should sync on start up with all capable screen` | 印證 | 啟動動畫於各螢幕間之同步 |
| L305 | `behavior) during any interruptions of animation (timeout, ignition butto` | 未對照 | 動畫被中斷時之行為 vs 未被中斷時之同步 |
| L307 | `SU9.) Pressing “Screen Off” or “Power Off” hard key will not do anything` | 未對照 | 動畫期間之硬鍵按壓之效果 vs 動畫是否播放 |
| L311 | `SSND 1) If start-up sounds are supported, it will start upon driver door` | 印證 | 門關閉 → 啟動音開始且與啟動動畫同步 |
| L312 | `start with the shut-down animation. Sounds will sync amongst all support` | 印證 | 告別音於關機動畫開始時同步；跨螢幕同步 |
| L314 | `SSND 2.1) If the setting is Always, start-up and goodbye sounds should b` | 印證 | 設定為 Always → 每次啟動動畫播放時皆播放聲音 |

**合計：印證 7／未對照 13／牴觸 3。**

### 3.1 三處牴觸（**未自行調和，依 R-PMH79 上呈**）

| 行 | 逐字 | 與何者相反 |
|---|---|---|
| **L299** | `SU5.) If ignition cycle has not changed the animation should only be played once.` | `-009` ER5 斷言啟動音與**啟動動畫**同步；同一 ignition cycle 內第二次門關閉**不再播放動畫** |
| **L300** | `- Animation should only play once per CAN BUS wake up upon closing the driver door.` | 同上形態，**計次單位不同**（CAN BUS wake up）—— 二者各自成立，不合併 |
| **L301** | `-- If vehicle ignition is turned to ACC, RUN or START ON with the door open, the animation screen shall be skipped …` | `-009` PC3 只言「駕駛門開著且 head unit off」，**未言 ignition 之位置**；該情形下動畫被跳過 |

**共同結構**：`-009` 之 pre_condition **未界定「本次門關閉是否為該 cycle／wake up 之第一次」**，
亦**未界定 ignition 之位置**。R-PMH84：**條件互斥須被證明，不得被假定** —— 三者皆未證。

### 3.2 我**未**做的事，及其理由

**下放包步驟 3 逐字為「發現牴觸即停並上呈」。**
28 包之同類觸發我以事件層限定自行解除（R-PMH87／R-PMH94 之授權），
**本包無該授權** —— 故我**未**對 `-009` 加任何 pre_condition，
**未**改其 ER，**未**改其 reasoning。**三處牴觸原樣上呈。**

> ⚠ **可能之解法已看見但不執行**：於 `-009` 加 pre_condition
> 「本 ignition cycle 內啟動動畫尚未播放過」與「ignition 在 OFF」，
> 三處即互斥可證。**該處置須裁定** —— 其為 pre_condition 之增設，
> 非 R-PMH87 所授權之事件層限定（後者為 procedure 之限定子句）。

### 3.3 兩處判定之**不對稱**須具名

L303（`When Power Button is pressed On do not show Start Up Animation`）我判 **`未對照`**，
而 L299／L301 判 **牴觸**。其差別：

- **L303 之條件是一個動作** —— 按 Power Button，**不在 `-009` 之 procedure 中**，故可證不發生；
- **L299／L301 之條件是測試前既存之狀態** —— 本 cycle 內是否已播放、ignition 在何位置，
  **不能以「程序不含該動作」排除**。

**該區分即本次三處牴觸與二處非牴觸之分界，於此具名以供覆核。**

---

## 4. 限定字串檢查之一般化（步驟 4）

### 4.1 作法

比照 28 §5.2：**期望值由寫死改為讀該批之宣告**。

| | 原 | 現 |
|---|---|---|
| 母體 | 寫死 `tc_id.endswith("007")` × `LIMIT_TOKENS`（7 項） | **讀 `d["limits"]`**（該批之宣告） |
| batch 1 | `-007` × 7 項 | 同（由 `gen_batch01.py` 宣告） |
| batch 2 | **不在保護內** | **6 條 × 2 項 = 12 項** |

未宣告 `limits` 之舊 fixture **回退為原寫死值**，故既有 fixture 之期望不變。

### 4.2 檢查項數維持 32 之證明

```
batch01 → 32/32 PASS
batch02 → 32/32 PASS
```

**兩檢查點之 `chk(...)` 呼叫數未變**（R-PMH99(c)、R-PMH99(a) 各一），
只有其標題所報之數字由該批算得。**停止條件 8 未觸發。**

### 4.3 must-hit 實跑

```
刪去 19/19 皆 FAIL: True；重複 FAIL: True；一步三項 FAIL: True
```

19 = batch 1 之 7 ＋ batch 2 之 12。
**batch 2 之限定僅 2 項，故「一步含三項」之錨點於該批不適用** ——
**該情形明白印出，不計為 PASS 亦不計為 FAIL**（不以「無法構造」冒充「已通過」）。

---

## 5. `DR-PMH8`（步驟 5）

**狀態 `DRAFT`，發出日期留空** —— 依 29a §二，本筆**不在 R-PMH110 之發出範圍**
（其於該裁定當下尚未開立）。全文見 `DATA_REQUESTS.md` §八，SHA256 `b4aa530edf320216`。

三問：(a) `SSND 2.2)` 之「一日」起算點；(b) `SSND 2)` 之設定路徑；
(c) `Sounds will sync amongst all supported vehicle displays.` 是否涵蓋告別音。

**其答覆將回頭改寫既有產出**（`-013` 之步驟／`-011` 之 PC／`-010` 之 ER），已於該節具名。

---

## 6. 覆蓋缺口之登記（步驟 6）

**A-PMH23** —— 告別音之跨螢幕同步**無任何 ER 斷言**。
其為**缺口而非牴觸**（規格未言其不同步，只是本批未驗）。
依 R-PMH109 **不另立 TC**，併入 `DR-PMH8` Q3。
**風險具名**：答覆到達前，該行為不會有任何一條 TC 驗到。

---

## 7. 檢查總表（程式產生，R-PMH92）

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


`verdict_form.py`：母體 **1164** 項（含 `animation` 之 23 行 ＋ 174 格），**0 failure**。

---

## 8. 未結 DR 清單 —— **4 筆**

| DR | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|
| `DR-PMH5` | **`SENT`** | 2026-08-25 | **ch 9 之 5 leaf** —— **`SENT` ≠ `ANSWERED`，不解除** |
| `DR-PMH6` | **`SENT`** | 2026-08-25 | 否 |
| `DR-PMH7` | **`SENT`** | 2026-08-25 | 矩陣四列之判定（`待定義`） |
| `DR-PMH8` | **`DRAFT`** | （待填） | 否 —— **待 Pei 發出** |

**發出管道欄三筆皆留空**，待 Pei 告知。

---

## 9. 本包是否仍有該驗而未驗者 —— **有**

1. **三處牴觸未解，而 `-009` 已在 batch 2 中。** batch 2 於 R-PMH105(c) 已「開批」，
   **其產出現在帶著一個已具名之牴觸**。在其解除前，`-009` 之 ER5
   **可能因規格所允許之行為（動畫不重播）而失敗**。
   **這是本包最要緊的一項。**
2. **`-010` 未受同樣檢驗。** 三處牴觸皆關於**啟動**動畫；關機動畫之重播限制
   **規格未載**（`SU4.)` 只給其觸發組合）。**「未載」不等於「無限制」** ——
   我未就此開 DR，因 R-PMH108 之裁定只涵蓋已知之二項；**該判斷未經裁定。**
3. **`animation` 之關鍵詞仍是列舉。** 本次判準為 `animation`／`start-up animation`／
   `shut-down animation`；`transition`／`intro`／`outro`／`splash` 等**未納入判準**
   （`outro` 於 L297 是因該行同時含 `animation` 才被看見）。**其偽陰未量測。**
4. **L305（動畫中斷時之行為）我判 `未對照`，但其下有一個未驗之問題**：
   動畫被中斷時**聲音是否隨之停止**，規格未言、本批未驗。**已於該行之依據具名，未開 DR。**
5. **batch 2 之修正後版本未經人讀覆核。** 本包依 29 §二之四項修正，
   **修正本身出自分析層之覆核**，但**修正後之文字是我寫的**，未再經人讀。
6. **29a §三之兩案（ch 9 維持凍結／限縮解凍）未處理** —— 其明載為 Pei 之裁定事項。
   **我未對 ch 9 做任何動作。**

---

## 10. 建議之 commit（**未執行**）

```
feat(power_moding): packages 28a-29 — DRs sent, freeze scope defined, batch 2 review fixes, animation scan
```

pathspec（**17 路徑** —— **含 28a**，該包經覆核通過但未授權提交，其異動仍在工作區）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/28a_dr_final.md
features/power_moding/docs/handoff/29_batch2_review.md
features/power_moding/docs/handoff/29a_dr_sent.md
features/power_moding/docs/upstream/28_batch2.md
features/power_moding/docs/upstream/29_batch2_review.md
features/power_moding/generated/batch01.json
features/power_moding/generated/batch02.json
features/power_moding/scripts/gen_batch01.py
features/power_moding/scripts/gen_batch02.py
features/power_moding/scripts/lint_batch.py
features/power_moding/scripts/spec_assertion_scan.py
features/power_moding/scripts/verdict_form.py
```

### 10.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** —— `workbook_state = BLANK` 未變，`openpyxl.save()` 未被呼叫 |
| 他 feature 之檔案 | **未觸** —— 工作區中 `display`／`vehicle_setting`／`time_management`／`docs/fw036` 之異動屬併行 session，**不入 pathspec**（R-G12） |
| `docs/runtime/` | **未觸** |
| `scripts/new_feature.py` | **未觸** |
| 新增檢查程式／檢查項 | **0／0** —— 本包所做者為 R-PMH107 所界定之「既有檢查對新資料之適用」 |
| DR 之發出 | **執行層未發出任何一封**（R-PMH83）；`SENT` 之填入依 Pei 於 29a §一之裁定逐字 |
