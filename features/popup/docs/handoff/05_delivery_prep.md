# 下放包 05 — Popup 交付準備

日期：2026-08-28
Feature slug：`popup`
前置：pilot 已結案（上繳包 04；分析層 2026-08-28 覆核，F7 修畢後無其他
TC 內容發現）。五條 TC 齊備、lint 全綠、x14 DV 存活。
本包產出交付候選簿，交 Pei 人工抽查後決定是否上繳。

## 禁區

- git 屬 Pei（R-G5）；xlsx 寫入一律 `surgical_save`（R-G3；理由見 A-POP5）
- 不代改他 feature 之任何檔（R-POP16 甲、R-POP19）——
  vehicle_setting 31 項、`gates_tsv` 之 driver_distraction、
  `lint_paths` 之紅，本包一律不碰
- `ledger_xref.py` 仍**不接入** `gate_all.py`

## 裁決引用（R-G13）

本輪新立 R-POP21、R-POP22，並修訂 R-POP18（實作二項追認）與
R-POP20（詞數算法訂正 ＋ 001 例外追認）。全文見
`features/popup/RULINGS.md` 現行文。

---

## 一、本輪新裁四項（先讀，影響本包作業）

1. **R-POP18 追認二項**（上繳包 04 §三之獨立判斷）：≥50% 第二門檻、
   標題式只作存在性佐證。兩項皆先證偽兩個方向再定案，追認。
2. **R-POP20 訂正**：詞數算法應為「去 `N. ` 序號後 `str.split()`，
   `(sec)` 計為一詞」—— 原條文「`(sec)` 括弧不計」為**分析層之誤**
   （寫條文時未回測自身數字之可重現性）。001 保留 `the elapsed time`
   之例外追認。
3. **R-POP21（新）**：節號列舉不得省 canon 前綴。執行層自產自修之
   canon_refs +1 是可複製的寫作陷阱，**分析層寫包同受此規**。
4. **R-POP22（新）**：**Q 欄（Estimated Test Time）留空**。
   分析層實測五本交付／產出簿之 Q 欄 **875/875 全空、零例外** ——
   既定實務而非待決政策。原列為「待 Pei」之 Q 欄政策**就此撤下**。

## 二、交付簿產出

1. 自 `sandbox/pilot01/` 之工作簿產交付候選，落
   `features/popup/output/`，檔名沿既有慣例：
   `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Popup_20260828.xlsx`
   （形制沿 Display／SXM／UserProfiles；產出前 `list_directory`
   確認無同名，有則停下回報，勿覆寫）
2. 五列寫入 `row 10`–`row 14`，逐欄複驗：

| 欄 | 值 |
|---|---|
| B（No.#） | 1–5 |
| C（Polarion ID） | 空（本 feature 無 CFTS 家族） |
| D（Requirement or Design ID） | `SWE1-POP-002-01` ～ `-05` |
| E（Test Case ID (TestRail)） | 空 —— 見 §三 |
| F（Test Case ID） | `NR1L-Popup-001` ～ `-005` |
| G（Test Group） | `Popup` ×5 |
| H（Test Set） | `Pop-up Close` ×5 |
| P（Priority） | `P1` ×5 |
| **Q（Estimated Test Time）** | **空 ×5**（R-POP22） |
| R（Design Method） | `狀態轉換 (State Transition Testing)` ×5 |
| Author | `PeiPYHsu` ×5 |

3. 落檔後 `zipfile` 直讀複驗 x14 DV 存活（`f=下拉選單!$A$1:$A$9`、
   `sqref=R10:R1411`），並回讀 `R10:R14` 確認其值屬下拉 9 字串

## 三、TestRail 對映表

本 feature 五條**全數為 `NEW`**，無舊 ID 可映（workbook_state = BLANK，
無 done region）。故對映表為**空表加說明**，非省略：
`DELIVERY_NOTE.md` 載明「舊 ID → 新 ID 對映：無 —— 本 feature 為 BLANK
起建，五條皆新增；E 欄（TestRail）留空待 TestRail 建號後回填」。

## 四、DELIVERY_NOTE.md（新建）

至少含：

1. **交付範圍**：037 V0.2 之 5 個 Functional Requirement leaf；
   Heading 2 列標 `No TC`（R-POP5，[DEFAULT] 仍待 Pei 追認；
   追認與否不改本包結果）
2. **範圍缺口具名上報（R-POP2）——【須醒目】**：
   GP1（spec 5.3）、GP2（spec 5.4）、queue／priority 本體於 037 V0.2
   無任何 SWE1 列，故**本交付不涵蓋 queue／priority**，儘管工單名稱為
   「Pop-Up Queue and Priority Management」。不寫明則收件方會以工單名
   推定範圍
3. **未結 DR 三件**：DR-POP2（Priority Matrix Post 2A 現版）、
   DR-POP3（POP-004 懸空引用）、DR-POP4（multi-task popup 例外清單）
4. **素材版位殘留兩點（R-POP6）**：CR25802 vs CR22510、`(26PI)` 適用性
5. **指紋**：交付簿 sha256、`generated/pilot_01.json` sha256、
   來源三件之 doc_id 與 sha256

## 五、gate 與複驗

- `lint036.py --profile popup`（21 項）全綠
- `ledger_xref --feature popup` PASS
- `gate_all.py` 五支，**逐支歸因**（預期：`lint_docs036` 綠、
  `rulings_hash` 綠、`gates_tsv` 紅（driver_distraction，非本包）、
  `lint_paths` 紅（driver_distraction，非本包）、`canon_refs` 紅
  （既存 ＋ 本包新增之 `R-G29` 引用））
- `rulings_hash.py` 重產：R-POP21、R-POP22 新增（+2）；
  R-POP18、R-POP20 之 sha **會變**（本輪修訂，預期）；其餘既有列變動 0

## 六、預期數字（[MANUAL]）

| 項 | 預期 | 量測條件 |
|---|---|---|
| 交付簿資料列 | 5 | `row 10`–`row 14`，F 欄非空 |
| F 欄值 | `NR1L-Popup-001`～`-005` | 逐列等值 |
| D 欄值 | `SWE1-POP-002-01`～`-05` | 逐列等值 |
| G 欄／H 欄 | `Popup` ×5 ／ `Pop-up Close` ×5 | 逐列等值 |
| P 欄 | `P1` ×5 | 逐列等值 |
| **Q 欄非空** | **0** | 逐列（R-POP22） |
| E 欄非空 | 0 | 逐列（§三） |
| R 欄值屬下拉 9 字串 | 5/5 | 對 `下拉選單!$A$1:$A$9` 逐列比對 |
| spec_reference 兩行者 | 1（002） | 逐列行數 |
| PENDING 佔位 | 0 | 全簿全欄 |
| Final Step ≤ 18 words | 5/5 | R-POP20 之訂正算法 |
| x14 DV | 1，存活 | `zipfile` 直讀 |
| RULINGS.sha.tsv 新增／變動／其餘變動 | 2／2／0 | 逐列比對 |

## 七、上繳要求

- 摘要一律 live 產（R-POP17-1）；待裁清單逐項複驗後重寫，不轉抄
- **節號列舉逐一冠 canon 前綴**（R-POP21，本包起適用於雙方）
- 預期數字對照（相符者亦列）；不符停下不調和
- R-G13 引用表（含 R-POP18、R-POP20 之**新** sha8）
- 交付簿之 sha256 與落點；`list_directory` 實測
- 三分法、掃描條件揭露、gate 逐支歸因

## 八、升級條件

- 交付簿之 R 欄值不在下拉 9 字串內
- x14 DV 未存活
- 五列任一欄與語料不符
- 除 R-POP18、R-POP20 外之既有 sha 變動
- `output/` 已有同名檔（勿覆寫，回報）

## 九、待 Pei（本包後之殘餘，四項）

| # | 事項 | 分析層意見 |
|---|---|---|
| 1 | R-POP5（Heading 台帳處置 [DEFAULT]）追認 | 維持現裁 |
| 2 | `-002-05` 之 `design_method`：狀態轉換 vs 負向測試 | 維持狀態轉換 —— 同一狀態機於合法輸入下不轉移，仍屬 state-change focus；IN §12 之 Negative 指非法輸入 |
| 3 | `scripts/ledger_xref.py` 與 vehicle_category 同名檔是否合併；是否接入 `gate_all.py` | 暫不接入（接入即全 repo 轉紅） |
| 4 | `forms/` 落點政策（全域；`forms/` 現有 12 項而 R-G2 字面只允 1 件） | 待裁 |

**已撤下**：Q 欄政策（R-POP22 實測結案）、DECISIONS.md 未簽（上繳包 04
§六 實測已簽）、pilot review（已結）。

**純他 feature，不入本清單**：vehicle_setting 31 項、`gates_tsv` 之
driver_distraction 未登錄、`lint_paths` 之 driver_distraction 在製品、
`media` 之 G-D 盲區。

## 十、未結 DR（IN §8.4.3）

DR-POP2、DR-POP3、DR-POP4，皆「已登記，未送出」，皆不阻斷交付。
DR-POP1 已 RESOLVED。三者須列於 DELIVERY_NOTE（§四-3）。
