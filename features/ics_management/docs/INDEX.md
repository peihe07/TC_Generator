# ICS Management — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-29（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| — | 2026-08-29 | 建檔前之偵察與四項判斷（Pei 准①命名②DR 即發③首波動工面④骨架） | **未落檔**（聊天）† | — | R-ICS1 ~ R-ICS4 | A-ICS1 ~ A-ICS7 | — |
| 01 | 2026-08-29 | 建檔與首批 TC（b01，6 條） | [handoff/01_onboarding_first_batch.md](handoff/01_onboarding_first_batch.md) | [upstream/01_onboarding_first_batch.md](upstream/01_onboarding_first_batch.md) | **無**（執行層不代擬） | 建議登錄 4 則（上繳 §十一） | **已審結**（b01 收下不退件；分析層即裁 R-ICS5～8，Pei 裁 R-ICS9／R-ICS10） |
| 02 | 2026-08-29 | 訊號解佔位、ignore 面（b02，2 條）、CFTS020 三面偵察 | [handoff/02_signal_resolution_and_ignore_face.md](handoff/02_signal_resolution_and_ignore_face.md) | [upstream/02_signal_resolution_and_ignore_face.md](upstream/02_signal_resolution_and_ignore_face.md) | **無**（執行層不代擬） | 建議登錄 3 則（上繳 §十二） | **已審結**（b02 收下；即裁 R-ICS11～17 與 R-ICS2 v2）｜註：其 §8 追補未隨包執行，改由 03 之作業 F 補做 |
| 03 | 2026-08-29 | 並行防護、CFTS020 全域 v2 重判、Display 面解鎖（b03，8 條） | [handoff/03_parallel_guard_and_display_unlock.md](handoff/03_parallel_guard_and_display_unlock.md) | [upstream/03_parallel_guard_and_display_unlock.md](upstream/03_parallel_guard_and_display_unlock.md) | **無**（執行層不代擬） | 建議登錄 6 則（上繳 §十四） | **已審結**（b03 收下；即裁 R-ICS18～21，登 A-ICS21～27，新開 DR-ICS14／15） |
| 04 | 2026-08-29 | profile 落檔、四訊號解佔位、Browse／Navigation 面（b04，7 條） | [handoff/04_profile_signals_and_navigation.md](handoff/04_profile_signals_and_navigation.md) | [upstream/04_profile_signals_and_navigation.md](upstream/04_profile_signals_and_navigation.md) | **無**（執行層不代擬） | 建議登錄 5 則（上繳 §十二） | **已審結**（b04 收下；即裁 R-ICS22／23，登 A-ICS28～33，新開 DR-ICS16／17） |
| 05 | 2026-08-29 | 佔位補齊、Display ER 主錨改寫、交付前體檢（**不新增 TC**，維持 23 條） | [handoff/05_anchor_rework_and_pre_delivery.md](handoff/05_anchor_rework_and_pre_delivery.md) | [upstream/05_anchor_rework_and_pre_delivery.md](upstream/05_anchor_rework_and_pre_delivery.md) | **無**（執行層不代擬） | 建議登錄 3 則＋G2~G7 六筆待取號（上繳 §14） | 待覆核 |

---

## 2. 註記

### † 01 以前之往返未落檔

R-ICS1～4 與 A-ICS1～7 之產生過程只存在於 2026-08-29 之聊天；
`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`
由分析層於下放包 01 同日寫入 repo，條文本身已落檔，
**其往返包未落檔**。與 AMFM／Projection 之同類缺口一致，不追補。

### 01 之未結事項

01 之待裁 6 項全數由 R-ICS5～R-ICS10 裁結（見 `RULINGS.md`）。

### 02 之未結事項

02 之待裁 6 項全數由 R-ICS11～R-ICS17 與 R-ICS2 v2 裁結。

### 03 之未結事項

03 之待裁 8 項由 R-ICS18～R-ICS21 裁結其六；出貨資格已由 R-ICS18 解鎖。

### 04 之未結事項

04 之待裁 7 項由 R-ICS22／R-ICS23 裁結其五。

### 05 之未結事項（詳見 upstream-05）

- **本輪自承二誤**：(1) 連續三包斷言「時間符號於 CFTS020 無值」為誤 ——
  值實存於 **`CFTS020-4819541`**（§1.8.1，v2 判適用，SFR 型）：`<Tstuck_button> = 120 sec`、
  `<TPeriodToSendNoChange> = 20 msec`、`<TPeriodToCountKnobDetents> = initial value 50 msec`；
  **DR-ICS10／DR-ICS12 疑可結**。(2) 「`1.8.1.3` 之 23 皆為 `[ECU:FPDM]`」實為 **16／2／5**，
  R-ICS23(a) 之理由有誤（結論不變）
- **`ledger_guard` 前後不逐字相同** —— `ANOMALIES.md` 於執行期間由分析層新增 A-ICS34；
  exit code 二次皆 0，**只比 exit code 會漏**
- 交付前體檢：23 條**強 12／弱 11**，**可出貨 13／不可 10**
- DR-ICS1 ~ DR-ICS17 **17 條全開**；覆蓋缺口 7 筆
- 該驗而未驗者 5 項

### 04 之未結事項（已作廢，保留於下）

- 待裁 7 項（§9），最重者為 **`$TGW_DISP_STAT$` 之 E1** —— 其為**匯流排變體**
  （B-CAN vs CAN-FD）而非 ECU 變體，R-ICS13 之「取 ICS 面板」語意無對應物；
  **b03 之 12 處佔位與 Display 面八條之訊號面驗證強度全繫於此**
- DR-ICS1 ~ DR-ICS15 **15 條全開**；建議新開 1 條（`Pop-up List Notification`）
- 該驗而未驗者 6 項（§10-2）
- **`VOLUME POP_UP` 之四包追索首次收斂**：CFTS 系列（022／020／019）與 HMI L&F 六本
  全數掃遍皆查無，線索指向一份具名而**不在 repo** 之 `Pop-up List Notification`

### 03 之未結事項（已作廢，保留於下）

- 待裁 8 項（上繳 §十），其中二項卡住出貨：
  **(1) R-G13 與 R-ICS17(d) 之交互**（改題即改指紋，`R-ICS2 v1` 由 `ad557b5d` → `4a8819f0`，
  圍欄內容 diff 0）；**(2) 方括號／單引號之 profile 缺口** —— IN §11 之 Exception 為
  profile-scoped 而本 feature 無 profile，**b03 八條之出貨資格繫於此**
- DR-ICS1 ~ DR-ICS13 **13 條全開**
- 該驗而未驗者 5 項（上繳 §12-2），首項仍是 `VOLUME POP_UP` 之 6 行 ER
  —— 連續三包具名，本包窮盡 CFTS019 七件仍查無

### 02 之未結事項（已作廢，保留於下）

- 待裁 6 項（上繳 §十）：**CFTS020 之 `ECU` 軸 87% 不存在使 R-ICS2 三軸判準幾近不可用**、
  R-ICS8(c) 同 DBC 多名之決斷、CFTS020 得否繞過 SWRA 位移、S1 未增等待步驟之處置、
  `SIS-5161` 之 DR、CFTS020 物件母數之口徑（407 vs 2180）
- DR-ICS1 ~ DR-ICS10 **10 條全開**；另建議新開 1 條（`SIS-5161`）
- 該驗而未驗者 5 項（上繳 §十一），首項為 b01 之 `VOLUME POP_UP` 顯示條件（FF 風險 6 行）

### 產出物落點

| 物 | 路徑 |
|---|---|
| b01 之 TC JSON | `generated/b01/b01_tcs.json`（02 輪修訂：訊號實名、DTC 具名、de-mature 步驟）|
| b01 之 manifest | `generated/b01/manifest.json` |
| b02 之 TC JSON | `generated/b02/b02_tcs.json`（ignore 面 2 條）|
| b02 之 manifest | `generated/b02/manifest.json`（含 `signal_resolution` 之逐步實測）|
| b03 之 TC JSON | `generated/b03/b03_tcs.json`（Display Control 8 條）|
| b03 之 manifest | `generated/b03/manifest.json` |
| b04 之 TC JSON | `generated/b04/b04_tcs.json`（Browse Control 6 條＋Menu Navigation 1 條）|
| b04 之 manifest | `generated/b04/manifest.json` |
| 9 個 LID → CAN 對照 | `generated/b03/lid_dbc_map.json` |
| **累計** 12 個 LID → CAN 對照 | `generated/b04/lid_dbc_map.json`（b03 八筆沿用＋b04 四筆實測）|
| feature profile | `docs/runtime/profiles/FW036_R1L_ICS_Profile.md`（R-ICS18(e)，逐字取 R-ICS18(a)(b)(c)）|
| CFTS020 三面偵察（v1，**已作廢**）| `docs/reports/02_cfts020_face_recon.md` |
| CFTS020 全域重判（v2，現行）| `docs/reports/03_cfts020_recon_v2.md` |
| HMI L&F ／ CFTS019 偵察 | `docs/reports/03_source_recon.md` |
| Pop Up List ／ Camera 偵察 | `docs/reports/04_source_recon_2.md` |
| 覆蓋缺口清單 | `docs/reports/05_coverage_gaps.md`（7 筆）|
| 交付前體檢 | `docs/reports/05_pre_delivery_check.md`（23 條逐條強度與出貨判斷）|
| 036 表單工作副本 | `sandbox/ics_management_00.xlsx`（不入版控）|
| 自檢 | `scripts/selfcheck_b01.py`（02 輪起合檢 b01+b02，增非 ASCII 與角括號列示）|
| 逐字比對 | `scripts/verify_verbatim_b01.py`（02 輪起兼比 CFTS020）|
| CFTS020 物件抽取／三軸判定 | `scripts/cfts020_probe.py`（03 輪起 v1／v2 並存，預設 v2）|
| 偵察報告產生器 | `scripts/gen_face_recon.py`（v1）、`scripts/gen_recon_v2.py`（v2，現行）|
| 台帳並行防護 | `scripts/ledger_guard.py`（R-ICS17(f)，每包上繳須附前後二次輸出）|
| LID → DBC 對照 | `scripts/lid_dbc_probe.py` |
| 來源偵察 | `scripts/src_recon_03.py`、`scripts/src_recon_04.py` |
| LID → DBC（四訊號）| `scripts/lid_dbc_probe_b04.py` |
| 佔位普查（口徑統一）| `scripts/pending_census.py`（A-ICS31；禁人工列舉）|
| 覆蓋缺口量測 | `scripts/gap_probe_05.py` |
| 交付前體檢產生器 | `scripts/gen_pre_delivery_05.py` |

落點取 `generated/`／`sandbox/` 而非下放包所令之 `batches/`／`workbook/`，
依 R-G25 與 `scripts/lint_paths.py` 之實跑；理由與證據見上繳包 §二。
