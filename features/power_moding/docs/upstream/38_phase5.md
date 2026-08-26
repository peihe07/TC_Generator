# 上繳包 38 —— Phase 5：封鎖、`tc_id` 單次指派與**首次寫回**（含 38a）

- 日期：2026-08-25
- 下放包：[handoff/38_phase5.md](../handoff/38_phase5.md) ＋ [38a_q10_and_profile.md](../handoff/38a_q10_and_profile.md)
- **本包為本 feature 之首次寫回** —— 其目標為 repo 內部之工作副本，非交付路徑

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH142～144 ＋ 38a 之 R-PMH145／146 —— **5/5 逐字相符** |
| 2 封鎖 | `-050`～`-053` 標 `BLOCKED-UNTIL-DR`；`DR-PMH8` 增 **Q9**（9 問）；`PENDING-ON-DR` 第 15 筆 |
| **3 `and`／`or` 全批掃描** | 33 項全判定；**查出一處先前未知之缺口（A-PMH32）** |
| 4 `tc_id` 指派 | **51 → 51，編號空位 0**；`data/tc_id_map.tsv` 已落檔 |
| 5 `check_write_back` 接線 | **首次上場**；故意失敗**三項全被攔下** |
| **6 寫回** | **51 列自 r10 寫入**；**四項不變量全同**；**母本未被動過** |
| 7 停手／封鎖之處置 | 停手 3 **未寫入**；封鎖 4 **已寫入**且 `Remarks` 載其依據 |
| 8 profile §1.2（38a） | 已落檔，**§1 原文未改一字**（byte 比對） |
| 9 Q10 揭露（38a） | 已入交付揭露清單 |
| 停止條件 7／8／9 | **全未觸發** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH142 | `-050`～`-053` 封鎖 | 691 | `1299376430c8f112` | `1299376430c8f112` | 1 | ✅ |
| R-PMH143 | `tc_id` 單次指派 | 682 | `e4a4a1ceca117d89` | `e4a4a1ceca117d89` | 1 | ✅ |
| R-PMH144 | `and`／`or` 全批掃描 | 300 | `793d5756a4658f48` | `793d5756a4658f48` | 1 | ✅ |
| R-PMH145（38a） | Q10 不填 | 555 | `c8e18052baf1d67d` | `c8e18052baf1d67d` | 1 | ✅ |
| R-PMH146（38a） | profile §1.2 授權 | 599 | `843bf29c164246d3` | `843bf29c164246d3` | 1 | ✅ |

---

## 2. 步驟 2 —— `-050`～`-053` 之封鎖

四條之 JSON 增 `blocked: true` 與 `blocked_reason`，**其為交付揭露之依據，非散文**。
`DR-PMH8` 增 **Q9**（新 SHA256 `a553fc762dddbb5e`，**現 9 問 ＋ 首段更正句**），
`PENDING-ON-DR` 增第 15 筆（其解封二路逐值列出，**R-PMH142 明言不預判**）。

---

## 3. 步驟 3 —— `and`／`or` 之一次性全批掃描（R-PMH144）

| tc（provisional） | 連接詞 | 逐字（節錄） | 判定 |
|---|---|---|---|
| `-001` | `and` | `’ will be removed and display an Accept Button.` | 後果連接 |
| `-001` | `or` | `their last mode screen or wait for the screen` | 選項並列-拆為二條 |
| `-002` | `and` | `’ will be removed and display an Accept Button.` | 後果連接 |
| `-002` | `or` | `their last mode screen or wait for the screen` | 選項並列-拆為二條 |
| `-003` | `and` | `’ will be removed and display an Accept Button.` | 後果連接 |
| `-003` | `or` | `their last mode screen or wait for the screen` | 選項並列-拆為二條 |
| `-004` | `and` | `’ will be removed and display an Accept Button.` | 後果連接 |
| `-004` | `or` | `their last mode screen or wait for the screen` | 選項並列-拆為二條 |
| `-008` | `or` | `to ignition in ACC or RUN` | **選項並列-取其一** |
| `-009` | `and` | `upon driver door close and sync with the start-up` | 後果連接 |
| `-010` | `and` | `upon driver door close and sync with the start-up` | 後果連接 |
| `-011` | `and` | `Start-up and goodbye sounds shall have` | 主語並列-皆驗 |
| `-012` | `and` | `start-up and goodbye sounds should be` | **主語並列-一讀未涵蓋** |
| `-013` | `and` | `start-up and goodbye sounds should be` | **主語並列-一讀未涵蓋** |
| `-014` | `and` | `start-up and goodbye sounds should not` | 主語並列-皆驗 |
| `-018` | `and` | `start update and dismiss FOTA via Wi-Fi` | 後果連接 |
| `-019` | `or` | `schedules an update time or dismisses update` | 選項並列-拆為二條 |
| `-020` | `or` | `schedules an update time or dismisses update` | 選項並列-拆為二條 |
| `-027` | `and` | `Show the splash screen and disclaimer screen once per` | 主語並列-皆驗 |
| `-029` | `and` | `it shall begin playing and conclude within 10s.` | 後果連接 |
| `-030` | `and` | `of a KEY OFF and radio UI shut down.` | 條件合取 |
| `-031` | `and` | `not present and ignition is turned to` | 條件合取 |
| `-033` | `or` | `RUN or START ON with the` | **選項並列-取其一** |
| `-033` | `and` | `screen shall be skipped and start from applicable splash` | 後果連接 |
| `-034` | `and` | `play startup animation and show applicable splash screens` | 後果連接 |
| `-038` | `and` | `Screen Off and HU Power button selections` | 主語並列-皆驗 |
| `-041` | `or` | `to ignition in ACC or RUN` | **選項並列-取其一** |
| `-044` | `or` | `either by soft control or hard control and the` | **選項並列-取其一** |
| `-045` | `and` | `SOS and ASSIST can turn head` | 主語並列-皆驗 |
| `-049` | `and` | `when radio is OFF and KEY ON or ACC.` | 條件合取 |
| `-050` | `and` | `Screen Off and Audio OFF` | 主語並列-皆驗 |
| `-051` | `and` | `Screen ON and Audio OFF` | 主語並列-皆驗 |
| `-053` | `and` | `Screen ON and Audio ON.` | 主語並列-皆驗 |

**候選 33 項**（`and`／`or` 各計一次／條）。分布：
- 後果連接：**10** —— `and` 連接**同一觸發之連續後果**，非選項 —— 無兩讀問題（§5.7）
- 主語並列-皆驗：**8** —— `and` 連接兩個受詞，**二者皆已驗**（各有其 ER）
- 選項並列-拆為二條：**6** —— `or` 之二成員**各立一條**（§8.2.2）
- 選項並列-取其一：**4** —— `or` 之成員**只驗其一**，其「同結果故不拆」為推定 —— **A-PMH31**
- 條件合取：**3** —— `and` 連接**條件**（合取），非選項
- 主語並列-一讀未涵蓋：**2** —— **`and` 連接兩個受詞而只驗其一** —— **A-PMH32**
- **未判定**：**1** —— 


### 3.1 ⚠ 查出一處先前未知之缺口 —— **A-PMH32**

| | 逐字 |
|---|---|
| `-012`／`-013` 之 `source_clause` | `If the setting is Always／Once a Day, **start-up and goodbye sounds** should be played …` |
| 二條之觸發 | **只有 startup animation** |
| 二條之斷言 | 泛稱 `the sound`，**未分辨啟動音與告別音** |

**同軸三值之中，只有 `-014`（`Never`）驗了告別音側**（其步驟 5 逐字含 `no goodbye sound`）。

**其成因可辨**：`SSND 2.1)`／`2.2)` 之句子自身不一致 ——
**主語為「啟動音**與**告別音」，而觸發只寫 `startup animation`**；
告別音依 `SSND 1)` 是與**關機**動畫同步的。
**我當時取了字面之觸發，而未取字面之主語。**

**本包不補條** —— `tc_id` 指派與寫回同輪進行，改動 TC 內容會使映射表與寫回不同步。
**入 `PENDING-ON-DR` 第 16 筆（無所繫之 DR）。**

> ⚠ **R-PMH144 令「採其一讀而另一讀未涵蓋者，入 `PENDING-ON-DR`」，而本項無 DR 可繫** ——
> 其與第 9／10 筆同形；**該簿之必辦機制繫於 DR 之 `ANSWERED`，故本筆亦無觸發點。**

---

## 4. 步驟 4 —— `tc_id` 單次指派（R-PMH143）

```
指派 51 條；provisional 相異 51；final 相異 51；一致 ✅
編號空位 = 0（R-PMH143(a)）
```

**停止條件 9（映射表之 provisional 與 final 筆數不等）未觸發。**

**`-024` 之空位未保留** —— 依 (a)，provisional 本為暫號，其連續性無保存價值。

**產出寫入 `generated/final/`，不覆寫 `generated/batchNN.json`** ——
其理由：後者為 `gen_batchNN.py` 之產物，**就地改寫會在下一次執行產生器時被無聲還原**；
分處二地使該風險不存在。**寫回之來源為 `generated/final/`。**

### 4.1 映射表（`data/tc_id_map.tsv`）

| provisional | final | leaf | Test Set |
|---|---|---|---|
| `NR1L-DisclaimerScreen-025` | **`NR1L-DisclaimerScreen-001`** | `SWE1-HMI-PM-001-01` | Splash Screen |
| `NR1L-DisclaimerScreen-026` | **`NR1L-DisclaimerScreen-002`** | `SWE1-HMI-PM-001-02` | Splash Screen |
| `NR1L-DisclaimerScreen-027` | **`NR1L-DisclaimerScreen-003`** | `SWE1-HMI-PM-011` | Splash Screen |
| `NR1L-DisclaimerScreen-001` | **`NR1L-DisclaimerScreen-004`** | `SWE1-HMI-PM-001-03` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-002` | **`NR1L-DisclaimerScreen-005`** | `SWE1-HMI-PM-001-04` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-003` | **`NR1L-DisclaimerScreen-006`** | `SWE1-HMI-PM-001-04` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-004` | **`NR1L-DisclaimerScreen-007`** | `SWE1-HMI-PM-001-05` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-005` | **`NR1L-DisclaimerScreen-008`** | `SWE1-HMI-PM-003` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-006` | **`NR1L-DisclaimerScreen-009`** | `SWE1-HMI-PM-004` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-007` | **`NR1L-DisclaimerScreen-010`** | `SWE1-HMI-PM-005` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-008` | **`NR1L-DisclaimerScreen-011`** | `SWE1-HMI-PM-022-02` | Disclaimer Screen |
| `NR1L-DisclaimerScreen-028` | **`NR1L-DisclaimerScreen-012`** | `SWE1-HMI-PM-006-01` | Startup Animation |
| `NR1L-DisclaimerScreen-029` | **`NR1L-DisclaimerScreen-013`** | `SWE1-HMI-PM-006-02` | Startup Animation |
| `NR1L-DisclaimerScreen-030` | **`NR1L-DisclaimerScreen-014`** | `SWE1-HMI-PM-006-03` | Startup Animation |
| `NR1L-DisclaimerScreen-031` | **`NR1L-DisclaimerScreen-015`** | `SWE1-HMI-PM-007` | Startup Animation |
| `NR1L-DisclaimerScreen-032` | **`NR1L-DisclaimerScreen-016`** | `SWE1-HMI-PM-008-01` | Startup Animation |
| `NR1L-DisclaimerScreen-033` | **`NR1L-DisclaimerScreen-017`** | `SWE1-HMI-PM-008-02` | Startup Animation |
| `NR1L-DisclaimerScreen-034` | **`NR1L-DisclaimerScreen-018`** | `SWE1-HMI-PM-009-01` | Startup Animation |
| `NR1L-DisclaimerScreen-035` | **`NR1L-DisclaimerScreen-019`** | `SWE1-HMI-PM-009-02` | Startup Animation |
| `NR1L-DisclaimerScreen-036` | **`NR1L-DisclaimerScreen-020`** | `SWE1-HMI-PM-010` | Startup Animation |
| `NR1L-DisclaimerScreen-037` | **`NR1L-DisclaimerScreen-021`** | `SWE1-HMI-PM-010` | Startup Animation |
| `NR1L-DisclaimerScreen-009` | **`NR1L-DisclaimerScreen-022`** | `SWE1-HMI-PM-012` | Startup Sounds |
| `NR1L-DisclaimerScreen-010` | **`NR1L-DisclaimerScreen-023`** | `SWE1-HMI-PM-012` | Startup Sounds |
| `NR1L-DisclaimerScreen-011` | **`NR1L-DisclaimerScreen-024`** | `SWE1-HMI-PM-013` | Startup Sounds |
| `NR1L-DisclaimerScreen-012` | **`NR1L-DisclaimerScreen-025`** | `SWE1-HMI-PM-014` | Startup Sounds |
| `NR1L-DisclaimerScreen-013` | **`NR1L-DisclaimerScreen-026`** | `SWE1-HMI-PM-015` | Startup Sounds |
| `NR1L-DisclaimerScreen-014` | **`NR1L-DisclaimerScreen-027`** | `SWE1-HMI-PM-016` | Startup Sounds |
| `NR1L-DisclaimerScreen-015` | **`NR1L-DisclaimerScreen-028`** | `SWE1-HMI-PM-017` | Startup Sounds |
| `NR1L-DisclaimerScreen-016` | **`NR1L-DisclaimerScreen-029`** | `SWE1-HMI-PM-018-01` | Power Transitions |
| `NR1L-DisclaimerScreen-017` | **`NR1L-DisclaimerScreen-030`** | `SWE1-HMI-PM-018-02` | Power Transitions |
| `NR1L-DisclaimerScreen-018` | **`NR1L-DisclaimerScreen-031`** | `SWE1-HMI-PM-018-03` | Power Transitions |
| `NR1L-DisclaimerScreen-019` | **`NR1L-DisclaimerScreen-032`** | `SWE1-HMI-PM-018-03` | Power Transitions |
| `NR1L-DisclaimerScreen-020` | **`NR1L-DisclaimerScreen-033`** | `SWE1-HMI-PM-018-03` | Power Transitions |
| `NR1L-DisclaimerScreen-021` | **`NR1L-DisclaimerScreen-034`** | `SWE1-HMI-PM-018-04` | Power Transitions |
| `NR1L-DisclaimerScreen-022` | **`NR1L-DisclaimerScreen-035`** | `SWE1-HMI-PM-018-04` | Power Transitions |
| `NR1L-DisclaimerScreen-023` | **`NR1L-DisclaimerScreen-036`** | `SWE1-HMI-PM-018-05` | Power Transitions |
| `NR1L-DisclaimerScreen-038` | **`NR1L-DisclaimerScreen-037`** | `SWE1-HMI-PM-019` | Power Off Behavior |
| `NR1L-DisclaimerScreen-039` | **`NR1L-DisclaimerScreen-038`** | `SWE1-HMI-PM-020` | Power Off Behavior |
| `NR1L-DisclaimerScreen-040` | **`NR1L-DisclaimerScreen-039`** | `SWE1-HMI-PM-021` | Power Off Behavior |
| `NR1L-DisclaimerScreen-041` | **`NR1L-DisclaimerScreen-040`** | `SWE1-HMI-PM-022-01` | Power Off Behavior |
| `NR1L-DisclaimerScreen-042` | **`NR1L-DisclaimerScreen-041`** | `SWE1-HMI-PM-024-01` | Power Off Behavior |
| `NR1L-DisclaimerScreen-043` | **`NR1L-DisclaimerScreen-042`** | `SWE1-HMI-PM-024-02` | Power Off Behavior |
| `NR1L-DisclaimerScreen-044` | **`NR1L-DisclaimerScreen-043`** | `SWE1-HMI-PM-024-03` | Power Off Behavior |
| `NR1L-DisclaimerScreen-045` | **`NR1L-DisclaimerScreen-044`** | `SWE1-HMI-PM-025` | Power Off Behavior |
| `NR1L-DisclaimerScreen-049` | **`NR1L-DisclaimerScreen-045`** | `SWE1-HMI-PM-026-01` | Voice Assistant Key |
| `NR1L-DisclaimerScreen-050` | **`NR1L-DisclaimerScreen-046`** | `SWE1-HMI-PM-026-02` | Voice Assistant Key |
| `NR1L-DisclaimerScreen-051` | **`NR1L-DisclaimerScreen-047`** | `SWE1-HMI-PM-026-03` | Voice Assistant Key |
| `NR1L-DisclaimerScreen-052` | **`NR1L-DisclaimerScreen-048`** | `SWE1-HMI-PM-026-04` | Voice Assistant Key |
| `NR1L-DisclaimerScreen-053` | **`NR1L-DisclaimerScreen-049`** | `SWE1-HMI-PM-026-05` | Voice Assistant Key |
| `NR1L-DisclaimerScreen-046` | **`NR1L-DisclaimerScreen-050`** | `SWE1-HMI-PM-027` | Off Road Plus |
| `NR1L-DisclaimerScreen-047` | **`NR1L-DisclaimerScreen-051`** | `SWE1-HMI-PM-029` | Off Road Plus |

---

## 5. 步驟 5 —— `check_write_back` 之首次接線

**其三項自 04 包實作、經故意失敗驗證後，至今未被任何寫回路徑呼叫。**
本包接於 `scripts/write_back.py` 之 §1 前置閘，**寫回前自動執行，任一失敗即中止**。

```
母本 SHA256 == R-PMH7 ✅  6372fb6be02f48dc…
待寫回 = **51** 條（自 generated/final/）

=== 步驟 5(b) —— 故意失敗須攔下寫回 ===
  (b) 起始列 44 → **被攔下** ✅  (b) start_row_source FAILED — 起始列 44 != feature.yaml write_back.first_row 10 —…
  (d) provisional → **被攔下** ✅  (d) tc_id_not_provisional FAILED — 批次 'batch01' 之 tc_id_status = 'provisional'…
  (c) 列數 0+51 != 50 → **被攔下** ✅  (c) row_count_delta FAILED — 寫回前 0 列，本批 51 筆，預期 51 列，實測 50 列…

三項故意失敗全被攔下：True
```

**停止條件 7（故意失敗未攔下寫回）未觸發。**

---

## 6. 步驟 6 —— **首次寫回**

| 項 | 值 |
|---|---|
| 母本 | `inputs/…_20260817_ext.xlsx`，SHA256 `6372fb6b…` **== R-PMH7**（寫回前實測） |
| 產出 | `output/…_PowerModing_20260825_writeback.xlsx` |
| 產出 SHA256 | `070ef73cea7b6ed99b2ddd1dfdc6c3532b2db44c94a0839a79f47cd19af0e851` |
| 寫入 | **51 列**，自 **r10** |
| **母本寫回後** | SHA256 **仍為 `6372fb6b…`** —— **未被動過**（實測） |

### 6.1 四項不變量之前後對照

| 不變量 | 寫回前 | 寫回後 | 同 |
|---|---|---|---|
| 分頁數 | 9 | 9 | ✅ |
| **DV 組數（含 x14）** | —— | —— | ✅ **由 `verify_structure` 逐 zip member 比對 classic 與 x14 之計數，不同即 raise** |
| `last_capacity_row` | 1411 | 1411 | ✅ |
| B 欄公式（r10／r710／r1411 三點） | `=IF(ISBLANK($D{n}),"",ROW()-9)` | 同 | ✅ |

**zip 48 members 中僅 `xl/worksheets/sheet6.xml` 相異** —— 即目標分頁。
**`openpyxl` 之 `save()` 未被呼叫**（R-G3）—— 寫入路徑只經
`backend/xlsx_surgical.surgical_save`。

**停止條件 8（四項不變量有任一不同）未觸發。**

### 6.2 §3 讀回斷言（**自產出之檔案讀回，非自記憶體**）

```
D 欄非空列 = 51（應為 51）
F 欄 tc_id 首末 = NR1L-DisclaimerScreen-001 … NR1L-DisclaimerScreen-051；相異 = 51
Q 欄留白 = True；D3/D4/D5 = [None, None, None]
G 欄唯一值 = {'Disclaimer screen'}；K／S 欄唯一值 = {'NA'}；AA 欄唯一值 = {'PeiPYHsu'}
Test Set 分布 = Splash 3／Disclaimer 8／Startup Animation 10／Startup Sounds 7／
                Power Transitions 8／Power Off Behavior 8／Voice Assistant Key 5／Off Road Plus 2
```

---

## 7. 步驟 7 —— 停手三筆與封鎖四條

| 類 | 處置 | 實測 |
|---|---|---|
| 停手 `-002`／`-023`／`-028` | **不寫入** | **三者皆不在寫入之 45 leaf 內** ✅ |
| 封鎖 `-050`～`-053`（final `-046`～`-049`） | **寫入**，`Remarks` 載其依據 | r55–r58 各載 `[BLOCKED-UNTIL-DR] DR-PMH8 Q9 — applicable condition for each outcome not stated in the specification.` ✅ |

---

## 8. 步驟 8（38a）—— profile §1.2 之落檔（R-PMH146）

| 項 | 值 |
|---|---|
| 檔 | `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` |
| SHA256 | `8f8a15145bdf3b16` → `80304b6f3baeacb1` |
| 行數 | 284 → 306（**+22**） |
| 逐字比對 | **38a §三之區塊逐字存在於該檔** ✅ |
| **§1 原文** | **未改一字**（`before[:i] == after[:i]` 之 byte 比對）✅ |
| 位置 | **§1.1 之後、§2 之前**（38a §三明令） |

⚠ **`PROFILE_INTEGRATION.md` 未動** —— R-PMH46 之明文不授權至今未解。

---

## 9. 步驟 9（38a）—— Q10 之交付揭露登記

`Product Document 記錄封面頁` **整張分頁不填**，維持母本現況。
**其為語料之少數側**（4 空／12 填）—— 已入交付揭露清單，載明
「依裁定留空，**與 12/16 之語料多數不同**」，**使交付方一望即知其為選擇而非遺漏**。

---

## 10. 六批 lint ＋ 檢查總表

```
batch01–06 各 32/32 PASS
desc_coverage exit 0（正向未涵蓋 3、反向無依據 0）  desc_coverage --must-hit 通過
check_write_back --self-test 通過   check_state_consistency 通過
check_granularity --self-test 通過   verdict_form 0 failure
```

**新增檢查程式 0、新增檢查項 0** —— `assign_tc_ids.py` 與 `write_back.py` **非檢查程式**
（其不判定任何事、不產生 PASS／FAIL），不在 R-PMH104 之凍結範圍（R-PMH107 之判別法）。

---

## 11. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（9 問）** | **其 Q9 封鎖四條** |

---

## 12. 本包是否仍有該驗而未驗者 —— **有**

1. **寫回之 51 列無人以 Excel 開啟看過。** 本包所驗者為
   **檔案結構**（zip member、DV 計數、B 欄公式）與**格內字串**（自檔案讀回）——
   **而 Excel 自身之四點確認（DV 是否仍作用、公式是否重算、版面是否可讀、列高是否合理）
   屬 Pei，程式層之檢查代替不了它。**
2. **A-PMH32 之二條未補，而其修正會改動 TC 內容** ——
   **一旦改動，本次寫回之 51 列即與 `generated/final/` 不同步**，須重寫一次。
   **本包選擇先寫回、後補條，其代價是必然要再寫一次。**
3. **`workbook_state` 仍為 `BLANK`** —— 其描述之對象為**母本**（母本確實仍空），
   **而現在另有一份已寫入之工作副本存在**。**該欄是否應隨之改變，未裁。**
4. **`Remarks` 欄現只載封鎖四條之依據** —— **停手三筆之「為何不在此」於工作簿內無任何痕跡**。
   其只在交付揭露清單裡。**若交付方只看工作簿，48 → 45 之差是看不出來的**
   （對照 comfort 之作法：未產出 TC 之 leaf 仍佔一列而其餘欄留空）。**該差異未裁。**
5. **`and`／`or` 之判定 33 項全為我一人所讀** —— 其中 4 項判為「取其一而推定同結果」
   （A-PMH31）、2 項判為「一讀未涵蓋」（A-PMH32）；**其餘 27 項之判定無第二人複核**。
6. **`tc_id` 之指派順序依 037 列序，而 037 列序我只在本包讀了一次** ——
   **其若有跳號或重複，映射表會沿用其錯**。本包未對 037 之列序另做一致性檢查。

---

## 13. 建議之 commit（**未執行**）

```
feat(power_moding): package 38 — tc_id assigned, first write-back (51 rows), -050~-053 blocked
```

pathspec（**14 路徑**）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/data/tc_id_map.tsv
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/38_phase5.md
features/power_moding/docs/handoff/38a_q10_and_profile.md
features/power_moding/docs/upstream/38_phase5.md
features/power_moding/generated/batch06.json
features/power_moding/generated/final/
features/power_moding/scripts/assign_tc_ids.py
features/power_moding/scripts/gen_batch06.py
features/power_moding/scripts/write_back.py
docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md
```

> ⚠ **`output/` 不入 pathspec** —— 其為 `features/power_moding/.gitignore:29` 所忽略。
> **產出之工作副本因而不進 git**；其身分由本上繳所載之 SHA256 承載。
> **該設定非本包所加，亦未改之。**
>
> ⚠ **最後一路徑在 `docs/runtime/` 下** —— 其為 **R-PMH146 之一次性授權**所及；
> **除該檔之 §1.2 外，`docs/runtime/` 下無任何改動。**

### 13.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| **寫回工作簿** | **已為之** —— 產出新檔於 `output/`，**母本未被動過**（SHA256 前後同值，實測） |
| `openpyxl.save()` | **未呼叫**（R-G3）—— 只經 `surgical_save` |
| 交付路徑 | **未觸** —— 其複製屬 Pei（R-G5） |
| 停止條件 7／8／9 | **全未觸發** |
| apparatus | **維持凍結** —— 新增檢查程式 0、新增檢查項 0 |
| `docs/runtime/` | **動了一處** —— profile §1.2，**R-PMH146 明文授權**；`PROFILE_INTEGRATION.md` 未動 |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（9 問） |
| 他 feature／`new_feature.py` | **未觸** |
