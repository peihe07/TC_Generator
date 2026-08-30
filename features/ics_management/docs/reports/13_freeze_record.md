# ICS 線凍結記錄（2026-08-30，b13 完工）

> **本檔之用途**：讓解凍之人**不必重讀十三包**即可接手。
> 每一節皆自量測取得，非轉抄。凡本線自身之誤已在對應處具名。

---

## §1 現況數字

| 項 | 值 | 量法 |
|---|---|---|
| TC 總數 | **31** | `generated/b01..b07/*_tcs.json` |
| Test Set 相異值 | **5** | Volume Control／Browse Control／Display Control／Menu Navigation／Stuck Button |
| 錨行總數 | **65**（相異 ObjectID **38**）| `specification_reference` 逐行 |
| 佔位 | **18 處／涉 14 條 TC** | `scripts/pending_census.py`（A-ICS31：禁人工列舉）|
| 未錨定斷言 | **3（弱驗證）＋ 6（已標明 A-ICS16）** | `scripts/gen_pre_delivery_08.py` |
| 候選篩基線 | 原始 **140** 行／殘餘 **66** 行／殘餘率 **47%** | 同上（前四包 53／53／43／52%）|
| 逐字驗證 | **31／31** | `scripts/verify_verbatim_b01.py` |
| 機檢 | 19 項 FAIL 0 | `scripts/selfcheck_b01.py` |
| 裁決 | 錨點 **49**、相異 ruling_id **42**（七組 v1／v2）| `scripts/ledger_guard.py` |
| anomaly | **A-ICS83**、相異 83、無缺口 | 同上 |
| DR | **20／20**、無缺口 | 同上 |
| 四支 gate | `canon_refs`／`rulings_hash`／`gates_tsv`／`lint_paths` **紅** | **本線開工前即紅，十三包未動**；非 ICS 所致 |

### 佔位之逐 DR 分佈

| DR | 佔位處數 | 涉 TC 數 | 缺件 |
|---|---|---|---|
| DR-ICS4 | 1 | 1 | CFTS019 volume level range |
| DR-ICS6 | 5 | 5 | HMI L&F 之 browse／scroll／tune／Enter／Back 對映 |
| DR-ICS8 | **12** | **8** | `TGW_DISP_STAT` CAN signal |

**「12」之出處已於 b13 複驗**：12 個 `PENDING:` 佔位全數落在 **`test_procedure`** 欄
（census 口徑為六個交付欄）。b13 作業 C 曾報「12 不可複現」，係其漏計 `test_procedure`、
且將**訊號名字面出現次數 24** 誤作佔位數；**該質疑不成立，數字無誤**。

---

## §2 不可現狀出貨之條（逐條）

| 條 | 阻因 | 所繫 |
|---|---|---|
| **V1**（Volume pop-up 顯示）| `VOLUME POP_UP` 之顯示條件在 CFTS022／020／019 與所有 HMI L&F 中**查無**；線索止於 `HMI Pop Up List`，該件不在 repo | **DR-ICS9**。**無佔位** —— 外觀完整而 ER 可能永遠判不出對錯，**此為凍結之最大風險** |
| **V2**（同上，第二態）| 同 V1 | 同上 |
| **V3** | 同族 | DR-ICS9 |
| **B5** | 同族阻因 | DR-ICS2 |
| b03 × 8 條 | `$TGW_DISP_STAT$` 觀察點未定（12 處佔位）| **DR-ICS16**（b13 作業 C 判「部分」可解，見 §3）|
| b01/b04/b05/b07 × 6 條 | HMI L&F 對映缺件（DR-ICS6）、音量級距（DR-ICS4）| DR-ICS6／4 |
| **G2／G3** | 效力繫於上游追認 | **DR-ICS20**（R-ICS41(b)）|

**V1／V2 之特性須特別交班**：其**無佔位**，故 `pending_census` 不會提醒，
`selfcheck` 亦全綠 —— **只有本記錄會提醒**。連續十包無進展。

---

## §3 掛帳清單（解凍時逐項處理）

| # | 掛帳事項 | 現況 | 所繫 |
|---|---|---|---|
| 1 | **§1.4 之 86 個 `Unclassified` 物件**依 SYS2 分類處置 | b13 三值化後已與 `Associated` 分離；OoS／Information 者不入範圍 | R-ICS42(d) |
| 2 | **`4819353` 覆蓋缺口** | **未覆蓋**（三要件命中皆 0；31 條中提及 `DCSD_DISP_STAT` 者 **0 條**）。已登記，**未生成** | R-ICS42(d) |
| 3 | **DR-ICS18 追認風險** | 上游若否認 `Disassociated`，**009 ＋ b12 加錨之 15 條須退回** | DR-ICS18 |
| 4 | **G5 押後** | 未解 | A-ICS60 |
| 5 | **SYS2 掃描起點盲區 73 列（21.9%）** | b13 作業 B 已盤點，**未處置** | A-ICS78 |
| 6 | **E19 觸發之 `NRL-180522`** | 判為 HMI 軟體側**可驗證之行為**；範圍屬分析層，**未裁** | 本記錄 §4 |
| 7 | **PDT27 dbc 綁定** | 唯讀量過，判「部分」；未綁定 | A-DM14 |
| 8 | **A-ICS80（`R-ICS40` 正本來源）** | 待 Pei 答 | R-ICS42(i) |
| 9 | **`$Touchscreen_ICS$` 第四路** | 登記不走 | R-ICS42(j) |
| 10 | **SYS2 自帶之 `Verifiability`／`Verification Criteria`／`Verification Method` 三欄從未量過** | b13 新發現，**已複驗欄位存在**（欄 33／56／57）| 見 §4 |
| 11 | **已綁 FDCAN8 檔載 `BO_TX_BU_ 1427 : ETM,LTM;`** | 與 upstream-07 之「二 DBC 中無 DUT 發送側」E3 依據**相對**，未調和 | 見 §4 |

---

## §4 解凍觸發條件（逐 DR 對映應做之事）

| DR | 上游回覆後應做 |
|---|---|
| **DR-ICS16**（`TGW_DISP_STAT` 觀察點）| 若定於 PDT27／FDCAN8：回收 b03 之 12 處佔位（作業 C 估最可能覆蓋 **8 條**）；`$Telematic_Power$` 估 **3** 處。**須先解訊號拼法**：佔位字面 `TGW_DISP_STAT` 在三支 dbc 中**查無**，實名為 `TGW_DISP_STATSts`；值名亦不符（b03 書 `[DISP_OFF]`／`[DISP_NORMAL]`，`VAL_ 1500` 為 `"Display_off"`／`"Normal_mode"`）|
| **DR-ICS9**（VOLUME POP_UP 顯示條件）| 解 V1／V2／V3 —— **凍結前之最高優先**，因其無佔位而不會自行浮出 |
| **DR-ICS2** | 解 B5 |
| **DR-ICS6** | 回收 5 處佔位（browse／scroll／tune／Enter／Back 對映）|
| **DR-ICS4** | 回收 1 處佔位 |
| **DR-ICS18**（變體追認）| 確認 → 掛帳 #3 解除；否認 → **009 ＋ 15 條加錨退回** |
| **DR-ICS20** | G2／G3 之效力確立或退回 |

**不依賴任何上游、隨時可做之二件**：
1. 以 SYS2 之 `Verifiability` 三欄反查本線 31 條之自行推導（掛帳 #10）；
2. 73 列盲區中之 42 列節標題錨與 31 列空白列之處置（掛帳 #5）。

---

## §5 解凍時第一件事

1. 跑 `python3 scripts/ledger_guard.py` —— 確認錨點／anomaly／DR 與 §1 相符；
2. 以 **`docs/reports/13_rulings_snapshot.md`** 為基準作圍籬 diff（**不動用 git**，R-ICS38(a)）；
3. 讀本記錄 §2 —— **先看 V1／V2**，它們不會自己浮出來；
4. 讀 §3 掛帳表，逐項確認其所繫之 DR 是否已有回覆。

---

## §6 交班給 PM／SU／DD 之一句話

十三包裡最值錢的不是任何一條 TC，是 **A-ICS78：掃描起點本身會有盲區**。
本線以 CFTS020 為起點掃了十二包，SYS2 中 **21.9% 的列**從未進入視野，
其中 **23 列是在案 FR**；而 SYS2 早已自帶逐列的可驗證性判定，本線卻自行推導了十三包。
**開工第一件事應是盤點「我的掃描起點漏了什麼」，而不是先掃。**
