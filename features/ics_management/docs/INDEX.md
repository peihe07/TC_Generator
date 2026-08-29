# ICS Management — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-29（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| — | 2026-08-29 | 建檔前之偵察與四項判斷（Pei 准①命名②DR 即發③首波動工面④骨架） | **未落檔**（聊天）† | — | R-ICS1 ~ R-ICS4 | A-ICS1 ~ A-ICS7 | — |
| 01 | 2026-08-29 | 建檔與首批 TC（b01，6 條） | [handoff/01_onboarding_first_batch.md](handoff/01_onboarding_first_batch.md) | [upstream/01_onboarding_first_batch.md](upstream/01_onboarding_first_batch.md) | **無**（執行層不代擬） | 建議登錄 4 則（上繳 §十一） | 待覆核 |

---

## 2. 註記

### † 01 以前之往返未落檔

R-ICS1～4 與 A-ICS1～7 之產生過程只存在於 2026-08-29 之聊天；
`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`
由分析層於下放包 01 同日寫入 repo，條文本身已落檔，
**其往返包未落檔**。與 AMFM／Projection 之同類缺口一致，不追補。

### 01 之未結事項（詳見上繳包）

- 待裁 6 項（上繳 §十）：落點、S1 priority、Description 得否充錨、
  CFTS020 之納入、`<Tstuck_button>` 忽略行為面之範圍、DR-ICS8 之解法
- DR-ICS1 ~ DR-ICS9 **9 條全開**
- 該驗而未驗者 4 項（上繳 §八）

### 產出物落點

| 物 | 路徑 |
|---|---|
| b01 之 TC JSON | `generated/b01/b01_tcs.json` |
| b01 之 manifest | `generated/b01/manifest.json` |
| 036 表單工作副本 | `sandbox/ics_management_00.xlsx`（不入版控）|
| 自檢 | `scripts/selfcheck_b01.py` |
| 逐字比對 | `scripts/verify_verbatim_b01.py` |

落點取 `generated/`／`sandbox/` 而非下放包所令之 `batches/`／`workbook/`，
依 R-G25 與 `scripts/lint_paths.py` 之實跑；理由與證據見上繳包 §二。
