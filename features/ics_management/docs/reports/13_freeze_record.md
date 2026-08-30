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

> **b19 更新（R-ICS54(d)，執行層依令改本節）**：原 11 項保留於下，並增列 b16～b18 之 OPEN 項。
> **凡本表所列者，`pending_census` 與 `selfcheck` 皆不會提醒 —— 只有本表會。**

| # | 掛帳事項 | 現況 | 所繫 |
|---|---|---|---|
| 1 | §1.4 之 86 個 `Unclassified` 物件依 SYS2 分類處置 | 未處置 | R-ICS42(d) |
| 2 | `4819353` 覆蓋缺口 | 未覆蓋；31 條提及 `DCSD_DISP_STAT` 者 0 條 | R-ICS42(d) |
| 3 | DR-ICS18 追認風險 | 上游若否認 `Disassociated`，009 ＋ b12 加錨之 15 條須退回 | DR-ICS18 |
| 4 | G5 押後 | 未解 | A-ICS60 |
| 5 | SYS2 掃描起點盲區 73 列（21.9%）| b13 已盤點，未處置 | A-ICS78 |
| 6 | E19 之 `NRL-180522`（觸控去重／CarPlay 認證）| 判為 HMI 軟體側可驗證行為，未裁 | 待 Pei |
| 7 | PDT27 dbc 之跨 feature 歸屬 | **BHCAN2 已於 b16 綁為 `reference.dbc_bh2`**；`display` 側未動 | A-DM14 |
| 8 | A-ICS80（`R-ICS40` 正本來源）| 待 Pei 答 | R-ICS42(i) |
| 9 | `$Touchscreen_ICS$` 第四路 | 登記不走 | R-ICS42(j) |
| 10 | SYS2 之 `Verifiability`／`Verification Criteria`／`Verification Method` 三欄 | **b17 已量**：75 列非空，**其中 37 列為逐字相同之樣板** | DR-ICS23 |
| 11 | 已綁 FDCAN8 載 `BO_TX_BU_ 1427 : ETM,LTM;` | 與 upstream-07 之 E3 依據相對，未調和 | 未裁 |
| **12** | **A-ICS116：列 39 `4821022` 之檢查點缺口** | SYS2 Criteria 要求 screen ON 態檢查 `$RQ_DISP_INTS$ != 0%`，我方 6 行全為 screen OFF 後之 `= 0 (0 %)`。**b18 因 E40 停，未補** | **待裁定性** |
| **13** | **A-ICS125：`4819578` 未加錨** | 與已覆蓋之 `4821693` 文字相似度 0.97，行為已涵蓋而未加錨（b12 加錨時未納入）| 未裁 |
| **14** | **A-ICS118②：`4819632`／`4819879`／`4821017` 三物件** | 適用 ∧ 在 SYS2 在案 ∧ 未覆蓋，載 `ON_BLANK`／`SNA`，**無 Camera Transition 之既存成因**。維持上呈中，未生成 | 待 Pei |
| **15** | **A-ICS109** | 維持待 Pei，b18／b19 未碰 | 待 Pei |
| **16** | **A-ICS130 及 b17／b18 後之其餘 OPEN 項** | 含 SYS2 之 `Category` 大小寫不一致、`Verifiability`＝`Criteria` 非空為同一集合、14 列 `Out of Scope` 而我方已驗且理由欄全空 | DR-ICS23 等 |
| **17** | **CFTS022 無 SYS2 匯出** | b17 主鍵表結構性無法回答 CFTS022 側覆蓋；7 個錨全屬該族 | **DR-ICS22** |
| **18** | **寫回後之交付狀態** | b19 依現狀寫回 036 工作簿；**非出貨授權**（IN §8.4.3 不變）。6 處 PENDING 原樣寫入 | R-ICS54(a) |

---

## §4 解凍觸發條件

> **b19 更新（R-ICS54(d)）**：依「寫回後非上游 DR 回覆不開窗」，本節收斂為單一條件。

**唯一之解凍觸發條件：上游 DR 回覆。**

其餘一切（新量測、新生成、補檢查點、加錨、三物件）**皆不構成解凍理由** ——
b18 之 E39／E40 與 b17 之 E33／E34 皆已停在該處，其續行繫於分析層之裁定，非繫於新的量測。

回覆到達後，逐 DR 對映應做之事：

| DR | 回覆後應做 |
|---|---|
| **DR-ICS9** | 解 V1／V2／V3 —— **最高優先**，因其**無佔位**而不會自行浮出 |
| **DR-ICS2** | 解 B5；並復活 Camera Transition Test Set（29 個未覆蓋物件繫於此）|
| **DR-ICS6** | 回收 5 處佔位（browse／scroll／tune／Enter／Back 對映）|
| **DR-ICS4** | 回收 1 處佔位（CFTS019 volume level range）|
| **DR-ICS18** | 確認 → 掛帳 #3 解除；否認 → 009 ＋ 15 條加錨退回 |
| **DR-ICS20** | G2／G3 之效力確立或退回 |
| **DR-ICS22** | CFTS022 之 SYS2 到手 → b17 主鍵表得涵蓋該族之 7 個錨 |
| **DR-ICS23** | SYS2 三項品質事實澄清 → 37 列樣板 Criteria 之性質確定，A-ICS116 之推廣面才有分母 |

**不依賴任何上游、隨時可做之二件**（保留自 b13）：
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

---

## §7 分析層附註（R-ICS43，2026-08-30）—— 解凍時必讀

本記錄經 upstream-13 §11-2 自評「大致足夠，缺三件」，分析層同意，
**不另開包補，列為解凍第一件**（R-ICS43(b)）：

1. **以 SYS2 333 列為主鍵之對照表**，標各列是否已有 TC 覆蓋 —— 結構性，最重。
   本記錄 §1～§5 仍以 CFTS020 為骨架；照 §5 四步開機會再次從 CFTS020 進場。
   同步將 31 條 ER 與 SYS2 `Verification Criteria`（欄 56）逐列對照（A-ICS85）。
2. **254 → 31 之收斂軌跡**（回讀 b01～b07 上繳包即可重建）。
3. **失敗史附錄**，至少含：節前定義塊須搜不能只搜需求句（A-ICS34）；
   布林旗標會合桶（A-ICS77）；未量即斷五例（A-ICS56／64／70／81／83）；
   以自身記憶代替讀檔（A-ICS70）。

**解凍後第一批量測**（R-ICS43(f)，非凍結期間之事）：
- 已綁 FDCAN8 載 `BO_TX_BU_ 1427 : ETM,LTM;` 與 A-ICS47 相對 —— 若 LTM 為發送方，
  b03 八條「觀察 TGW_DISP_STAT」之前提可能反向（A-ICS87）。
- `DCSD_DISP_STAT` 與 `TGW_DISP_STAT` 是否同一訊號之不同側命名。
- 佔位字面與 dbc 實名／值名之不符（A-ICS88），依 IN §8.7.5(g) 處置。

**待 Pei 裁**：E19 之 `NRL-180522`（A-ICS84）—— 分析層建議轉 `display` feature。
**待 Pei 答**：正本 `R-ICS40` 之來源（A-ICS80）。

凍結基準快照：`13_rulings_snapshot.md`（49 錨點；本附註後分析層又落 R-ICS43，
故解凍時圓籬 diff 預期新增一條，非異常）。
