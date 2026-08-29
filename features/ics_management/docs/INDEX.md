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
| 02 | 2026-08-29 | 訊號解佔位、ignore 面（b02，2 條）、CFTS020 三面偵察 | [handoff/02_signal_resolution_and_ignore_face.md](handoff/02_signal_resolution_and_ignore_face.md) | [upstream/02_signal_resolution_and_ignore_face.md](upstream/02_signal_resolution_and_ignore_face.md) | **無**（執行層不代擬） | 建議登錄 3 則（上繳 §十二） | 待覆核 |

---

## 2. 註記

### † 01 以前之往返未落檔

R-ICS1～4 與 A-ICS1～7 之產生過程只存在於 2026-08-29 之聊天；
`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`
由分析層於下放包 01 同日寫入 repo，條文本身已落檔，
**其往返包未落檔**。與 AMFM／Projection 之同類缺口一致，不追補。

### 01 之未結事項

01 之待裁 6 項全數由 R-ICS5～R-ICS10 裁結（見 `RULINGS.md`）。

### 02 之未結事項（詳見上繳包 02）

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
| CFTS020 三面偵察 | `docs/reports/02_cfts020_face_recon.md` |
| 036 表單工作副本 | `sandbox/ics_management_00.xlsx`（不入版控）|
| 自檢 | `scripts/selfcheck_b01.py`（02 輪起合檢 b01+b02，增非 ASCII 與角括號列示）|
| 逐字比對 | `scripts/verify_verbatim_b01.py`（02 輪起兼比 CFTS020）|
| CFTS020 物件抽取／三軸判定 | `scripts/cfts020_probe.py` |
| 偵察報告產生器 | `scripts/gen_face_recon.py` |

落點取 `generated/`／`sandbox/` 而非下放包所令之 `batches/`／`workbook/`，
依 R-G25 與 `scripts/lint_paths.py` 之實跑；理由與證據見上繳包 §二。
