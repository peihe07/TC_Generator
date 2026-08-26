# 上繳包 39 —— A-PMH32 修正、第二次寫回與交付文件（交付前最後一包）

- 日期：2026-08-26
- 下放包：[handoff/39_delivery.md](../handoff/39_delivery.md)

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH147～149 **3/3 逐字相符** |
| 2 `-012`／`-013` 擴涵蓋 | 各由 5:5 增為 **6:6**；告別音側已驗；六批 lint 32/32 |
| 3 `delivery_state` | 已增；**`workbook_state` 維持 `BLANK`** |
| **4 第二次寫回** | 新副本 SHA256 `01e917b88e050ce1`；**母本未被動過** → 停止條件 7 未觸發 |
| **5 `Cover` 作者欄** | **實測後停手，未自行擇定** —— 母體 17 檔 **11 空／6 非空**，非空者為**兩個他人姓名** |
| 6 17 §5.4 之結清 | **實載 6 項（非下放包所謂之五項）**；第 4 項**由實測結清**、第 1 項大部分已被 R-PMH127 取代、其餘四項入 KNOWN-INCOMPLETE |
| 7 `DELIVERY_NOTE.md` | 十節（七節之要求全數涵蓋） |
| 8 交付揭露清單 | **與 `DELIVERY_NOTE.md` 併為一份**（其 §8）；**16 筆，非下放包所謂之 15 筆** |
| 停止條件 7／8／9 | **全未觸發** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH147 | A-PMH32 擴而不拆 | 543 | `db3754369b99b4f9` | `db3754369b99b4f9` | 1 | ✅ |
| R-PMH148 | `delivery_state` 另立 | 318 | `11d2154f0e1321fa` | `11d2154f0e1321fa` | 1 | ✅ |
| R-PMH149 | 停手三筆於交付文件載明 | 414 | `fc3d0f85e3a59a28` | `fc3d0f85e3a59a28` | 1 | ✅ |

---

## 2. 步驟 2 —— `-012`／`-013` 之擴涵蓋（R-PMH147）

#### `NR1L-DisclaimerScreen-025`（provisional `NR1L-DisclaimerScreen-012`）— Always plays the sounds every time the startup animation is played

**pre_conditions**

```
1. The start-up and goodbye sound setting is Always
2. Start-up sounds are supported on this vehicle
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Play the startup animation and record the start-up sound output
4. Play the startup animation a second time and record the sound output
5. Trigger the shut-down animation and record the goodbye sound output
6. Check that both sounds were played on every occasion
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. The start-up sound is played the first time the animation is played
4. The start-up sound is played the second time the animation is played
5. The goodbye sound is played when the shut-down animation is triggered
6. Both the start-up and the goodbye sounds were played every time
```

#### `NR1L-DisclaimerScreen-026`（provisional `NR1L-DisclaimerScreen-013`）— Once a Day plays the sounds only once per day

**pre_conditions**

```
1. The start-up and goodbye sound setting is Once a Day
2. No start-up or goodbye sound has been played today
```

**test_procedure**

```
1. Do not press the Mute key or the Headunit Mode key
2. Do not change the headunit mode by voice recognition
3. Play the startup animation and record the start-up sound output
4. Play the startup animation a second time on the same day
5. Trigger the shut-down animation on the same day and record the sound
6. Check that each sound was played once and not a second time
```

**expected_result**

```
1. No Mute key press and no Headunit Mode key press occurs
2. The headunit mode is not changed by voice recognition
3. The start-up sound is played the first time the animation is played
4. No start-up sound is played the second time on the same day
5. The goodbye sound is played once on that day and not a second time
6. Each sound was played only once on that day
```


其 `reasoning` 各具名 §2.2 之三項（同軸單位一致／與 §5.7 之張力／§7 只要求一條負向）
與其成因（**「我當時取了字面之觸發而未取字面之主語」**）。

### 2.1 停止條件 8 之核驗 —— **兩面並陳**

| | |
|---|---|
| **字面** | 「`desc_coverage` 正向，**告別音之斷言**仍為 `未涵蓋`」 |
| 實測 | **A-PMH32 所指之二處已轉為已涵蓋** —— `SWE1-HMI-PM-014` A1 現由 `-012` **ER6** 涵蓋、`-015` A1 由 `-013` **ER6** 涵蓋 |
| **惟** | 正向仍有 **1 處與告別音有關之 `未涵蓋`**：`SWE1-HMI-PM-012` A3（`Sounds will sync amongst all supported vehicle displays.`）之**告別音側** |

**該處非本條件所指** —— 其為 **A-PMH23**（29 包登記，繫於 `DR-PMH8` Q3），
**與 A-PMH32 之成因不同**：A-PMH32 為「主語有二而只驗其一」，
A-PMH23 為「`SSND 1)` 末句是否涵蓋告別音，其本身未定」。
**R-PMH147 只處置前者。**

**故停止條件 8 未觸發** —— **惟「告別音」三字在正向表中仍出現一次，此處具名之。**

正向現況：60 斷言／45 leaf，**未涵蓋 3**（R-PMH137 之重複二例 ＋ A-PMH23）；
反向 **157** ER 斷言（+2），**無依據 0**。

---

## 3. 步驟 3 —— `delivery_state`（R-PMH148）

```yaml
workbook_state: "BLANK"        # 維持不動 —— 其描述交付基底之**初始狀態**，為歷史事實
delivery_state: "WRITTEN"
delivery:
  copy:   "output/…_PowerModing_20260826_writeback_rev2.xlsx"
  sha256: "01e917b88e050ce1f164db1f1121ea9fe665bae34bcfa5e153c03d1f322f248c"
  rows_written: 51
  first_row: 10
  written_on: "2026-08-26"
  supersedes: "…_20260825_writeback.xlsx (sha256 070ef73c…, 38 包)"
  master_sha256_unchanged: "6372fb6b…"
  delivery_path_copy: "PENDING — Pei"
```

`check_state_consistency` 通過。

---

## 4. 步驟 4 —— 第二次寫回

| 項 | 值 |
|---|---|
| 來源 | **母本**（`inputs/…_ext.xlsx`）—— **未在第一次之產出上疊改** |
| 產出 | `output/…_PowerModing_20260826_writeback_rev2.xlsx` |
| 新副本 SHA256 | **`01e917b88e050ce1f164db1f1121ea9fe665bae34bcfa5e153c03d1f322f248c`** |
| 與第一次不同 | ✅（第一次為 `070ef73c…`；其內容已因 §2 而變） |
| **母本 SHA256 前後** | **同為 `6372fb6b…`** → **停止條件 7 未觸發** |
| 四項不變量 | 分頁 9／DV（含 x14，由 `verify_structure` 逐 member 比對）／`last_capacity_row` 1411／B 欄公式 —— **全同** |
| zip 48 members | **僅 `sheet6.xml` 相異** |
| 前置閘 | `check_write_back` 三項先跑一次**故意失敗**，**三項全被攔下**；其後三項正跑全 PASS |
| `openpyxl.save()` | **未呼叫**（R-G3） |

**第一次之產出不覆寫、不刪除** —— 其為 38 包上繳所載之對象。

---

## 5. ⚠ 步驟 5 —— `Cover 封面` 作者欄：**實測後停手**

**母體 17 個交付夾之 036 工作簿全數實測**（R-PMH24 之 (a′) 母體）：

| 作者欄之值 | 檔數 |
|---|---|
| **（空）** | **11** |
| `張愷霏 ErinKFChang` | 5 |
| `林政宇 BillyZYLin` | 1 |

**核准者欄 17/17 皆為 `劉安哲 AllenACLiu`。**

**「依既有交付件之慣例填」之前提不成立**：
- 慣例之**多數是不填**（11/17）；
- **填者填的是別人的名字** —— **無一為本 feature 之作者**。

**依停止條件 9，我未自行擇定。** `Cover` 之作者欄**維持空白**（＝母本現況＝多數側），
**其處置待裁**（已入 `DELIVERY_NOTE.md` §6 與 §8 之待決）。

> ⚠ **須與工作簿之 `AA` 欄分辨**：`AA`（Test Case Author）**已填 `PeiPYHsu`**，
> 其為 `feature.yaml` 之 `author_value`；**二者為不同欄位，本項不動之。**

> ⚠ **我第一次挑錯了檔** —— 以「夾內最後一個 xlsx」取樣，挑到 037 報告與 SYS1 匯出，
> 17 夾中 14 夾報「無 Cover」。**改以檔名含 `FM-WI-FSM-036` 為判準後 17/17 全數命中。**

---

## 6. 步驟 6 —— 17 §5.4 之結清

> ⚠ **下放包謂「其餘五項」，而 17 §5.4 實載 6 項** —— 以 6 項處置。

| # | 條 | 處置 |
|---|---|---|
| 1 | R-PMH50 × TSV 之 `section_title` 取自 SYS1 | **大部分已被 R-PMH127 取代** —— 射程之比對已改取 037 之 `Requirement Description`，`section_title` 不再是比對基準；其殘餘已無下游用途 |
| **4** | R-PMH23 所放行之三頁是否受同一污染 | **由實測結清** —— 見 §6.1 |
| 2 | R-PMH39 之判準未套用於 G3／G5 | **入 KNOWN-INCOMPLETE（七）** |
| 3 | R-PMH60 之「代理量」未套用於其他代理量 | 同上 |
| 5 | R-PMH27 之母體未回頭掃其他結論 | 同上 |
| 6 | R-PMH63 未回頭掃其他下放包之措詞 | 同上 |

### 6.1 第 4 項之實測

| 分頁 | 母本 | 客戶那份 | 判 |
|---|---|---|---|
| `Reference` | `44d2f19c0832` | `44d2f19c0832` | **相同 → 未受污染** |
| `QS Suggestion` | `44a1977eadff` | `44a1977eadff` | **相同 → 未受污染** |
| `Test Case Framework` | **無此分頁** | 有 | **無從比對** —— 其只存在於客戶那份；**本 feature 從未取用其內容** |

（逐格轉字串後取 SHA256。）

---

## 7. 步驟 7／8 —— `DELIVERY_NOTE.md`

**十節**，涵蓋下放包所要求之七節（(a)～(g)）並增三節（未涵蓋者之總表、驗證狀態、未結 DR）。

**交付揭露清單與其併為一份**（下放包令執行層擇一並載理由）——
**理由**：二者之讀者相同，且 §2／§3／§4 之每一項在未決清單中皆有其對應筆；
**分立會使同一件事在兩份文件裡各說一次，而其中一份先過期。** 未決清單為其 **§8**。

> ⚠ **下放包謂「`PENDING-ON-DR` 現 15 筆」，實測 16 筆** ——
> 第 16 筆為 38 包步驟 3 所增（A-PMH32），**下放包 §四步驟 8 之數字未及更新**。

### 7.1 一項自查

**`DELIVERY_NOTE.md` §4 我第一次把 `-001-01` A1 之承載者寫成 `NR1L-DisclaimerScreen-011`，
而該 id 是電源鍵／免責畫面那條；正確者為 `-012`。**
**其為我在寫文件時以 provisional 之直覺換算 final 所致** ——
已改，並對文中所引之**每一個 `tc_id` 逐一回查其 leaf**，現全數相符。

---

## 8. 六批 lint ＋ 檢查總表

```
batch01–06 各 32/32 PASS
desc_coverage exit 0（正向未涵蓋 3、反向 157 項無依據 0）  --must-hit 通過
check_write_back --self-test 通過   check_state_consistency 通過
check_granularity --self-test 通過  verdict_form 0 failure   check_table 通過
```

**新增檢查程式 0、新增檢查項 0** —— apparatus 維持凍結。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（9 問）** | **其 Q9 封鎖四條**；**其為唯一仍在 Pei 手上者** |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **第二次寫回之 51 列同樣無人以 Excel 開啟看過。** 38 輪之四點確認你已做過，
   **而本次之內容已變**（`-012`／`-013` 各多兩列文字）—— **其須重做一次**。
2. **`Cover` 作者欄之處置未定，而交付在即。** 我維持空白並具名；
   **若你要填，其值須由你給定**（母體中無一可援引之前例指向本 feature 之作者）。
3. **`DELIVERY_NOTE.md` 為我一人所寫，未經任何人讀。**
   **其 §8 之 16 筆是自 `DECISIONS.md` 機器截取的，而該簿之完整性從無檢查**
   （36 包已具名：漏登之判定不會出現於此，亦不會有東西指出它漏了）。
4. **`-012`／`-013` 之擴涵蓋使二條各多一個觸發（關機動畫）** ——
   **而 canon §5.7 之字面是「不同觸發即拆」**。R-PMH147 已具名該張力並裁不拆，
   **惟其代價是本 feature 之三條同軸 TC 各含兩個觸發**，
   **若日後之覆核以 §5.7 之字面為準，該三條皆會被判須拆。**
5. **17 §5.4 之第 2／3／5／6 項只是被登記，未被處置** ——
   **四者皆為「同一判準是否應擴及某處」，其未擴及之處，其結論之支持度未知。**
6. **交付路徑之複製、Excel 抽驗、git tag 皆屬你** —— 本包未觸及交付路徑。

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): package 39 — A-PMH32 fixed, second write-back, delivery note
```

pathspec（**11 路徑**）：

```
features/power_moding/DECISIONS.md
features/power_moding/DELIVERY_NOTE.md
features/power_moding/RULINGS.md
features/power_moding/data/tc_id_map.tsv
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/39_delivery.md
features/power_moding/docs/upstream/39_delivery.md
features/power_moding/feature.yaml
features/power_moding/generated/batch02.json
features/power_moding/generated/final
features/power_moding/scripts/desc_coverage.py
features/power_moding/scripts/gen_batch02.py
features/power_moding/scripts/write_back.py
```

> ⚠ **`output/` 不入 pathspec**（`.gitignore:29`）—— **兩份工作副本皆不進 git**；
> 其身分由 `feature.yaml` 之 `delivery.sha256` 與本上繳所載者承載。

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| **寫回** | **第二次已為之**；**母本未被動過**（SHA256 前後同值，實測） |
| `openpyxl.save()` | **未呼叫**（R-G3） |
| 交付路徑 | **未觸** —— 其複製屬 Pei（R-G5） |
| 停止條件 7／8／9 | **全未觸發**（8 之兩面已並陳） |
| apparatus | **維持凍結** —— 新增程式 0、新增檢查項 0 |
| **未自行擇定者** | **`Cover` 作者欄** —— 實測與「填」之前提不符，停手待裁 |
| 與下放包不同之處 | **三處**：17 §5.4 為 6 項非 5 項；`PENDING-ON-DR` 為 16 筆非 15 筆；停止條件 8 之兩面並陳 |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（9 問） |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |

---

# 39a 之執行（與 39 同一往返，不另佔編號）

- 下放包：[handoff/39a_pei_closures.md](../handoff/39a_pei_closures.md)
- 性質：**裁定補充包** —— 不新增 TC、不新增檢查、**不動工作簿**

## 39a.0 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH150～152 **3/3 逐字相符**；**既有條文一 byte 未改**（實測：新檔以舊檔為前綴，增 1871 bytes）→ 停止條件 7 未觸發 |
| 2 第 16 筆之結案 | **實測告別音斷言已涵蓋** → 停止條件 9 未觸發；結案 `RESOLVED-BY-R-PMH147` |
| 3 `DELIVERY_NOTE` 修訂 | §2／§8／§8.1／§8.2／§9 已改；**§1 統計數字一字未動** → 停止條件 8 未觸發 |
| 4 `DR-PMH8` Q6／Q7 | 已標〔告知性附註〕，**編號不重排**；**CFTS009 全表掃描已為之** → 停止條件 10 未觸發 |
| 5 一致性覆掃 | 8 處改動，逐處列於 §39a.5 |

## 39a.1 抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH150 | #11／#12 照預設排除；Q6／Q7 降格附註 | 507 | `d469fac0a1b7c56f` | `d469fac0a1b7c56f` | 1 | ✅ |
| R-PMH151 | `-002`／`-028` 依裁定結案 | 853 | `ea6a108b1a712f29` | `ea6a108b1a712f29` | 1 | ✅ |
| R-PMH152 | #9／#10 終態為揭露 | 445 | `9822c575ce2c9d9a` | `9822c575ce2c9d9a` | 1 | ✅ |

> **停止條件 7 之核驗**：`RULINGS.md` 之新內容**以舊內容為前綴**（`startswith` 實測 True），
> 增 **1871 bytes**。**R-PMH72／R-PMH117 之正文未動一字** —— R-PMH151 以沿革語句取代其等待語義。

## 39a.2 第 16 筆之結案 —— **先實測，後結案**

| leaf | 其 DESC 之斷言 | 涵蓋 | 該 ER 逐字 |
|---|---|---|---|
| `SWE1-HMI-PM-014` | `SSND 2.1)` … `start-up and goodbye sounds` … | **已涵蓋** → `-012` ER6 | `Both the start-up and the goodbye sounds were played every time` |
| `SWE1-HMI-PM-015` | `SSND 2.2)` … `start-up and goodbye sounds` … | **已涵蓋** → `-013` ER6 | `Each sound was played only once on that day` |

> ⚠ **一項須分辨**：`-013` 之 ER6 為**總結句**（`Each sound`），
> **其告別音之明確斷言在 ER5**：`The goodbye sound is played once on that day and not a second time`。
> `-012` 同（ER5：`The goodbye sound is played when the shut-down animation is triggered`）。
> **二條之告別音側皆有明確 ER，故第 16 筆得結** —— `RESOLVED-BY-R-PMH147`。

## 39a.3 `DELIVERY_NOTE.md` 修訂後之各節

### §2

不寫入工作簿之三筆 —— **1 停手 ＋ 2 依裁定結案**（此為裁定之結果，非遺漏）

| leaf | outline | 037 之 Requirement Title | 依據 | **所需之上游輸入** |
|---|---|---|---|---|
| `SWE1-HMI-PM-002` | 7.1.1 | Power Button Transitions during Ignition Off | **R-PMH117** ＋ **R-PMH151**（Pei 裁定 2026-08-26） | **無 —— 依 R-PMH151 結案**。其行為逐字委於 `based on vehicle architecture. See CFTS009 for clarification.`，**行為定義在外部規格 CFTS009，屬該規格 owner 之 SWE 需求範圍**（canon §8.4.2），不得由本 feature 吸收 |
| `SWE1-HMI-PM-023` | 10.5 | Headunit Functionality during Key OFF Power ON | **R-PMH111**（條件式，停手待答） | **`DR-PMH8`／`DR-PMH5` 之 (1)(2)**：p9 能力矩陣之權威來源。其斷言之謂詞正是「`Headunit` 於 `KEY OFF (No ACC)` × `HEADUNIT POWER ON` 下之可用程度」，與 p9 同格同一謂詞 |
| `SWE1-HMI-PM-028` | 12.2 | CFTS009 Behavior Reference | **R-PMH72** ＋ **R-PMH151**（Pei 裁定 2026-08-26） | **無 —— 依 R-PMH151 結案**。其內文逐字為 `OFF2.) Please refer to CFTS009 for complete behavior.`，同上 |

> ⚠ **`-002` 與 `-028` 為 out of scope（經裁定不寫入）；`-023` 仍在範圍內，只是暫不產出。**
> **三者之狀態詞因而不同**（`ACCEPTED`／`ACCEPTED`／`STOPPED-PENDING-DR`），此為刻意。
>
> ⚠ **`3` 之組成（R-PMH151，2026-08-26）**：**3 = 1 停手（`-023`）＋ 2 依裁定結案（`-002`／`-028`）**。
> **`CFTS009` 自此不再是本 feature 之待取件** —— 取得與否不改變本輪交付；
> 若日後取得且上游要求納入，屬**範圍變更**，另案。**§1 之統計數字不因本條而變。**

---


### §8／§8.1／§8.2

已知未決清單（R-PMH132(b)）—— **11 筆**

> **交付日至而 `DR-PMH5`／`6`／`7`／`8` 有任一未 `ANSWERED` 者，以現況交付**，
> 其 TC 不因未覆而延（R-PMH121／R-PMH132(a)）。**下表即該規則所要求之揭露。**

| # | 判定之所在 | 所繫之 DR | 答覆為何值時改為何（節錄） |
|---|---|---|---|
| 1 | `matrix_vs_chapter.VERDICT[(9, 1, 15)]` —— 矩陣 `r15`（`Key-off`）× `PM1)` 之記法，現為 `待定義` | `DR-PMH5` (1)(2)／`DR-PMH7` Q1（`VP`）／`DR-PMH8` Q4（二延遲 | **逐值**：(甲) `VP` = head unit 顯示螢幕 **且** 二延遲名同指 → **改記 `牴觸`**（同謂詞相反值，條件完全重合）；(乙) `VP` = head unit 顯示螢幕 **而** 二延遲名為不同設定 → **仍記 `牴觸`惟其範圍縮小**，須重寫其依據並登記條件；(丙) `VP` **非** head unit 之顯示螢幕 → **改記 `未對照`**（無共同謂詞），與二延遲名之答覆無關；(丁) 任一問未獲答覆 → **維持 `待定義`**… |
| 2 | `gen_batch02.py` 之六條 TC 各二項事件層限定中，因 `r46`／`r47` 而納入者（R-PMH95 之涵蓋兩讀） | `DR-PMH7` Q2（`Else: Mute Active` 之記法） | **逐值**：(甲) 答為「**使之靜音**」（事件使 mute 變為 active）→ **限定正當，維持不動**，並將該二列由 `待定義` 改記 `牴觸`；(乙) 答為「**維持靜音**」（mute 狀態不變）→ **該二列改記 `未對照`**，而**六條之第二項限定即為過度限定** —— 其不致誤判，惟使 TC 較規格所需為窄；**須逐條評估是否移除**（移除須重跑 lint 之限定字串檢查，因 `limits` 宣告隨之改變）；(丙) 未獲答覆 → 維持現狀（限定保留… |
| 3 | `gen_batch02.py` 之 `-013`（`Once a Day`）之 procedure 與 `-011` 之 pre_condition | `DR-PMH8` Q1（「一日」之起算點）／Q2（設定之所在路徑） | **逐值**：(甲) Q1 答為具體起算點（午夜／點火週期／滾動 24 小時）→ **`-013` 之步驟須重寫**，以該起算點表述其「第二次觸發」之時點，並增一項 input_test_data；(乙) Q1 答為「未定義／由實作決定」→ **維持現狀**（現行措詞 `on the same day` 於三讀皆成立），並將此登記為永久限度；(丙) Q2 答為具體路徑 → **`-011` 之 pre_condition 改寫為該路徑**，其 `test_procedure`… |
| 4 | `ANOMALIES.md` 之 **A-PMH23**（告別音之跨螢幕同步無 ER 斷言）與 `gen_batch02.py` 之 `-010` | `DR-PMH8` Q3（`Sounds will sync amongst all supported | **逐值**：(甲) 答為「涵蓋二者」→ **`-010` 之 ER 須增一條**（告別音於各支援螢幕間同步）**且其 procedure 須增一步**（維持 1:1），A-PMH23 改 `RESOLVED`；(乙) 答為「只涵蓋啟動音」→ **`-010` 不動**，A-PMH23 改 `ACCEPTED（經釐清不補）`；(丙) 答為「只涵蓋告別音」→ **`-009` 之 ER4 須移至 `-010`**（此讀法目前未被任何產出所採，其後果最大）；(丁) 未答 → 維持… |
| 5 | `gen_batch03.py` 之 `Power Transitions` 各 TC 之 Pre-Condition `No phone call or projection call is | `DR-PMH8` Q5（IGN OFF 後通話結束且有 popup 待顯示時之行為） | **逐值**：(甲) 答為「**應 stay awake**」（`PM1)` 優先）→ **該 Pre-Condition 得移除**，且**應增一條 TC** 驗「通話結束後 popup 仍顯示」；`r31`／`r32` 之記法由 `牴觸` 改為 `未對照`（矩陣該格須更正）；(乙) 答為「**應關機**」（矩陣優先）→ **該 Pre-Condition 保留**，且 `PM1)` 之條件須加註例外；**應增一條 TC** 驗「通話結束即關機」；`r31`／`r32` 改… |
| 6 | `matrix_vs_chapter.VERDICT[(9, 1, 6)]`／`[(9, 19, 24)]`／`[(9, 19, 25)]` —— 三列現為 `待定義` | `DR-PMH7` Q1（`VP` 之定義） | **逐值**：(甲) `VP` = head unit 之顯示螢幕 → **三列逐列重判**，其中 `r25`（`VP Turns Off` 於 key-off 狀態門開啟）**極可能改記 `牴觸`**（與 `PM1)` 之 stay awake 期間可同時成立而取相反值）；(乙) `VP` 為他物（如儀表板顯示）→ **三列改記 `未對照`**；(丙) 未答 → 維持 `待定義`。⚠ **本筆與第 1 筆之差別**：`r15` 另受 A-PMH24 所阻，即使本問獲答仍可能… |
| 7 | `Power Transitions` 組（batch 3）之全部斷言 —— 其是否須依 R-PMH94 重掃 | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」並提供之 → **該文件為第七筆素材**，須補 `MANIFEST.sha256`，**batch 3 之全部斷言須依 R-PMH94 對其重掃一次**（R-PMH111 末段明令）；(乙) 答為「p9 自身即權威」→ **batch 3 之各 TC 須逐條複驗 R-PMH111 之判別法結果**（原判「不倚賴 p9」者仍成立，惟其依據由「來源不明」改為「主題不同」）；A-PMH18 改 `RESOLVED`；(丙) 未答 → 維持現狀，… |
| 8 | `spec_assertion_scan.IGNOFF_LINE_VERDICT[160]` —— 規格 p4 之 `Note: do not show popup again if popu | `DR-PMH7` Q3（該 `Note:` 之適用範圍） | **逐值**：(甲) 答為「**泛指所有 popup**」→ **改記 `牴觸`** —— 於 Radio Off 已顯示過之 popup 於 IGN OFF 不得再顯示，與 batch 3 之斷言取相反值；**`-016`～`-021` 須加 Pre-Condition「本次點火週期內該 popup 尚未於 Radio Off 顯示過」**；(乙) 答為「**僅適用於同段之 `Geolocation + SOS Popup`**」→ **改記 `未對照`**，batch 3… |
| 13 | `generated/batch03.json` 之 `stopped` 中之 **`-023`**（`PITA8`）—— 停手待答，**非 out of scope** | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」→ 取得後 **`-023` 得撰寫 TC**，`Power Transitions` 組由 5 leaf 有 TC 增為 **6**；(乙) 答為「p9 自身即權威」→ **`-023` 得撰寫，惟其斷言須逐條套 R-PMH111 之判別法並具名**；(丙) 答為「p9 無權威來源」→ `-023` **改判 out of scope**，其狀態詞屆時方改為 `ACCEPTED`，`n_leaf` 46 → **45**；(丁) 未答 … |
| 14 | `gen_batch01.py` 之 `-008`（leaf `-022-02`）—— 其 DESC 之例外 `unless certain phone call scenarios have | `DR-PMH8` Q8（該 `certain` 指哪些情境） | **逐值**：(甲) 上游列舉該等情境 → **`-008` 之 pre_condition 須增其排除**，且**應評估是否另立 TC 驗該例外之行為**（其時該例外即成為可驗之行為）；(乙) 答為「無特定情境／該句為贅語」→ **`-008` 不動**，該例外自 DESC 之涵蓋要求中移除；(丙) 未答 → **`-008` 之射程持續不足**，其於「已知未決清單」中具名。⚠ **037 之 DESC 於同處亦未列舉** —— 非 SYS1 側之偏差，而是上游本身未定義… |
| 15 | `generated/batch06.json` 之 `-050`／`-051`／`-052`／`-053` 四條 —— **標 `BLOCKED-UNTIL-DR`，已產出而不可執行**（R | `DR-PMH8` Q9（四種互動結果各自之適用條件） | **逐值**：(甲) 答覆**載明各類之條件** → **四條各加其條件為 Pre-Condition，`BLOCKED` 解除**，其 procedure 之步驟 1 隨之具體化；(乙) 答為「**四者皆為可能之結果而無條件之分**」→ **四條併為一條**（其 ER 為「結果為所列四類之一」），並依 R-PMH137 於其餘三 leaf 記 `未涵蓋-重複`；**二路皆須屆時另裁，R-PMH142 明言不預判**；(丙) 未答 → **四條維持封鎖，隨交付附其封鎖依據**… |

### 8.2 本輪已結之 5 筆（**其原文依 R-TM13 保留，不刪**）

| # | 判定之所在（節錄） | 結案詞 | 所依條號 | 結案語 |
|---|---|---|---|---|
| 9 | `gen_batch03.py` 之 `-017` —— `60 秒無互動` 與 `總計 10 分鐘` 二上限**何者先到即何者生效**，本條以二個獨立步驟分別 | **`ACCEPTED-RISK`** | **R-PMH152** | 不另開問；`-017` 之二上限交互作用不斷言，其風險依裁定為**終態**（§9 第 8 項） |
| 10 | `ANOMALIES.md` 之 **A-PMH25**（9.1 權威文本於逾時處為破句）與 `-016` 之不斷言處置 | **`ACCEPTED-RISK`** | **R-PMH152** | 不另開問；`-016` 之逾時秒數不斷言，其風險依裁定為**終態**（§9 第 7 項） |
| 11 | `gen_batch04.py` 之 `-024` **撤除**（R-PMH129）—— `SU1.)` 之「動畫後呈現 splash，1.5 each」一句無 | **`CLOSED-BY-RULING`** | **R-PMH150** | 照既定預設排除 —— 037 未載者不納入本輪交付，永久登記為覆蓋缺口（§9 第 5 項） |
| 12 | `ANOMALIES.md` 之 **A-PMH28**（p3–p7 流程圖之五類行為）—— 依 **R-PMH131** 不寫 TC | **`CLOSED-BY-RULING`** | **R-PMH150** | 同上（§9 第 4 項） |
| 16 | `gen_batch02.py` 之 `-012`／`-013` —— 其 `source_clause` 主語為 `start-up **and** good | **`RESOLVED-BY-R-PMH147`** | **R-PMH147** | `-012`／`-013` 已擴涵蓋告別音側（各 ER5 明載 `goodbye`，ER6 為其總結），**實測已涵蓋** |

> **其「逐值」欄之原文未刪** —— 仍在 `DECISIONS.md` 之 `PENDING-ON-DR` 登記簿內；
> **本表只縮為結案語**（R-TM13：不刪除，加註保留）。
> ⚠ **第 9／10 筆日後若上游主動釐清，屬 Revise 批次**，屆時依其原載之 (甲)(乙) 路處置，**R-PMH152 不預判**。

### 8.1 未結 DR

| DR | 狀態 | 其所繫之未決 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 之停手；p9 矩陣之權威來源 |
| `DR-PMH6` | `SENT` 2026-08-25 | RVC 情境下 HVAC popup；三項無需求之行為 |
| `DR-PMH7` | `SENT` 2026-08-25 | `VP` 之定義；`Else: Mute Active`；`Note:` 之範圍 |
| **`DR-PMH8`** | **`DRAFT`（9 問，其中 2 為附註）** | **其 Q9 封鎖四條**；**Q1–Q5、Q8 另繫五筆未決**；**Q6／Q7 為告知性附註（R-PMH150），不繫任何未決** |

---


### §9

本交付未涵蓋者（一次列全）

1. **停手一筆**（`-023`）**與依裁定結案二筆**（`-002`／`-028`）之行為（§2）；
2. **封鎖四條**之行為（§3）—— 其 TC 已寫入而不可執行；
3. `SWE1-HMI-PM-012` A3 之**告別音跨螢幕同步**（§4）；
4. **p3–p7 流程圖**所載而散文所無之**五類行為**（A-PMH28／R-PMH131；**依 R-PMH150 屬裁定排除**）——
   其中 `If vehicle supports more than 1 Splash screen, toggle them one after
   another with a 1.5 timeout each` 直接落在 splash 各條之標的內；
5. `SU1.)` 之 `after the animation (3 sec) a splash screen is presented timeout
   (1.5 each).` —— **該句於 SYS1 匯出 0 命中，037 因而無其 leaf**（A-PMH29／R-PMH129；
   **依 R-PMH150 屬裁定排除**）；
6. **9.1 之 `the radio should shut Off`**（§7）；
7. `-044` 之 `hard control` 接聽路徑與 `-041` 之 `ACC`／`RUN` 其一（A-PMH31）——
   **其「同結果故不拆」為推定，規格未言其實作為同一路徑**；
8. **`-016` 之逾時秒數**（`the 60-second timeout defined in the pop-up list` 之逾時本身）
   **無任何 TC 驗到**（A-PMH25／**R-PMH152**，`ACCEPTED-RISK`）——
   **與第 6 項之 `the radio should shut Off` 同源而非同項，故分列**；
9. **`-017` 之二上限交互作用**（`60 秒無互動` 與 `總計 10 分鐘` 何者先到即何者生效）
   **無任何 TC 驗到**（**R-PMH152**，`ACCEPTED-RISK`）—— 規格未言其優先。

---


## 39a.4 `DR-PMH8` 之 Q6／Q7 標註 ＋ CFTS009 全表掃描

**標註後之原文（節錄）**：

```text
  〔告知性附註 —— 不待覆，通報性質。本問為通報上游漏項之附註，其答覆不改變本輪交付物；若上游日後裁納入，屬新 leaf 之變更申請，於 Revise 批次另案處理。（R-PMH150）〕
  Q6: The following clause appears in the logic and flow document but not in the
      SYS1 structured export, and consequently has no requirement in the SWE.1
      analysis report:

          SU1.) ... after the animation (3 sec) a splash screen is presented
          timeout (1.5 each).

      Should it be included in the analysis report? At present no test case
      covers it, because we do not author test cases for behaviour that has no
      requirement of its own.

  〔告知性附註 —— 不待覆，通報性質。本問為通報上游漏項之附註，其答覆不改變本輪交付物；若上游日後裁納入，屬新 leaf 之變更申請，於 Revise 批次另案處理。（R-PMH150）〕
  Q7: The flow diagrams on p
```

**編號未重排**（Q1–Q9 維持）；新 SHA256 **`0ed8d781cc27e996`**。
**R-PMH152 令不增 Q10／Q11，本 DR 之問數自此定於 9。**

### CFTS009 之全表掃描（停止條件 10）

**`DATA_REQUESTS.md` 全表 1054 行，`CFTS009` 命中 9 處，逐處覆核**：

| 命中處 | 性質 |
|---|---|
| L15、L150 | **`DR-PMH1`** —— 其標的逐字為「CFTS009 所定之 Off Road+ power moding 行為」，**唯一以 CFTS009 為標的之 DR 項** |
| L32、L36、L39、L45、L48、L53、L54 | **敘述文字**（`-028` 之內文引用、06 包之零命中量測、§8.4.2 之判準說明）—— **非 DR 項目** |

**結論**：`DR-PMH1` **早已 `CLOSED`**（R-PMH72，**歷程中從未 `SENT`**）。
**故未結 DR 中無任何一項之唯一用途為替 `-002`／`-028` 取 CFTS009** ——
**「查無」係經全表掃描後方斷言，非預設。**

## 39a.5 一致性覆掃之改動清單（8 處）

| # | 檔 | 改動 |
|---|---|---|
| 1 | `ANOMALIES.md` | **A-PMH25** `RESOLVED` → **`ACCEPTED-RISK`**（R-PMH152）—— 並具名「被解決者為**前提**，非**缺口**，`RESOLVED` 一詞於此不成立」 |
| 2 | `ANOMALIES.md` | **A-PMH28** → **`ACCEPTED（裁定排除）`**（R-PMH150） |
| 3 | `ANOMALIES.md` | **A-PMH29** `PENDING` → **`ACCEPTED（裁定排除）`**（R-PMH150） |
| 4 | `ANOMALIES.md` | **A-PMH32** `PENDING` → **`RESOLVED`**（R-PMH147，附 39a §二之實測） |
| 5 | `DECISIONS.md` | `PENDING-ON-DR` 之「合計 16 筆」下加註**已結 5 筆／主表餘 11 筆**；**原文全數保留不刪**（R-TM13） |
| 6 | `DECISIONS.md` | R-PMH123 之條目補記「**R-PMH151 改其性質而不改其狀態詞**」 |
| 7 | `DECISIONS.md` | 新增 39a 之二條記錄（三項裁定之執行；`DR-PMH8` 問數定於 9 ＋ CFTS009 掃描結果） |
| 8 | `DELIVERY_NOTE.md` | §2 標題「停手三筆」→「**不寫入工作簿之三筆 —— 1 停手 ＋ 2 依裁定結案**」 |

> ⚠ **`docs/INDEX.md` 之歷史列與各包要點未改** —— 其為**當輪之紀錄**
> （如 37 包要點載「停手 3（`-002`／`-023`／`-028`）」）。
> **該等陳述在其當輪為真**，依 R-PMH44 之精神不回改；**本包之變更記於 39 包要點。**
> `RUNBOOK.md`／`feature.yaml` **命中 0**，無須改。

## 39a.6 未結 DR（本包後）

| DR | 狀態 | 其所繫 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 之停手（未決 #7／#13） |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160（未決 #1／#2／#6／#8） |
| **`DR-PMH8`** | **`DRAFT`（9 問，其中 **2 為附註**）** | **Q9 封鎖四條**；Q1–Q5、Q8 另繫五筆；**Q6／Q7 不繫任何未決** |

**未決清單 16 → 11；停手 3 → 1；「無所繫之 DR」歸零。**

## 39a.7 本包是否仍有該驗而未驗者 —— **有**

1. **`-002`／`-028` 之改判使 `CFTS009` 自本 feature 之視野消失，而那兩個行為並未消失。**
   R-PMH151 令其屬 CFTS009 owner 之 SWE 需求範圍 —— **本 feature 無從確認該 owner 是否真的寫了它**。
   **「出範圍」是我方之分類，不是對方之承諾。** 該限度已入 `DELIVERY_NOTE.md` §9 第 1 項，
   **惟其未被任何一封 DR 通知過**（`DR-PMH1` 從未發出）。
2. **`DELIVERY_NOTE.md` §8 主表現為 11 筆，而其內容仍是我自 `DECISIONS.md` 機器截取的。**
   **該簿之完整性從無檢查**（36 包已具名），**結案 5 筆並未改變這件事** ——
   **漏登之判定仍不會出現於此。**
3. **A-PMH25 之狀態詞我改為 `ACCEPTED-RISK` 而非下放包所令之字面。**
   下放包 §三步驟 5 逐字為「A-PMH25 依 R-PMH152 改 `ACCEPTED-RISK`」—— **與我所為相同**；
   **惟其原狀態為 `RESOLVED`（34 包所改），而非 `PENDING`** ——
   **本包等於把一個已標 `RESOLVED` 之項目改回未結類**。其理由已於該處具名，**惟該轉向未經裁定**。
4. **第 9／10 筆之 `ACCEPTED-RISK` 使兩項風險自「待問」變為「已承擔」，而其承擔者是誰未載。**
   R-PMH132(b) 令其入交付揭露清單 —— **交付方讀到它時，其選擇只有接受或退回**；
   **本 feature 未提供第三種可能（如「若貴方認為須驗，我方可於 Revise 補」）。**
5. **本包之三條裁定皆為「縮小範圍」，而其總和未被回頭檢查對覆蓋率之影響。**
   48 leaf 之全集不變，惟**其中 3 筆之行為自此永久無 TC，5 項未決自此不再追問** ——
   **該總和之比例（3/48 ＝ 6.25% 之 leaf 無行為驗證）未於任何一處被算出並具名。**

