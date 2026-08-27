# 上繳包 15 — Bed Lowering Mode：同儕基準量測（判定方式口徑）

日期：2026-08-27
對應下放包：`features/bed_lowering/docs/handoff/15_peer_baseline_measure.md`
（sha256 `119b2a4cfa033786e397c09e479750018392d096effa6c6e4135439c5df70fb4`）
執行層：Tier 1
性質：單一量測。**未改任何 TC、未改任何工作簿。**

---

## 〇、結論先講

**本 feature 之 80.8% 不是異常，而且比同儕更好。**

兩本可分類之同儕交付本，**A 類（最終判定取自訊號）皆為 0 條、B+C 皆為 100.0%**。
本 feature 為 A 29 條（19.2%）、B+C 122 條（80.8%）。

| 本 | 母體 | A | B | C | **B+C** |
|---|---|---|---|---|---|
| **bed_lowering（本 feature）** | 151 | **29（19.2%）** | 80（53.0%）| 42（27.8%）| **122（80.8%）** |
| audio_mgmt B1（本管線，v3 記法）| 70 | **0（0.0%）** | 6（8.6%）| 64（91.4%）| **70（100.0%）** |
| vehicle_setting VF230（本管線，R-VS52 override）| 457 | **0（0.0%）** | 296（64.8%）| 161（35.2%）| **457（100.0%）** |

下放包 §一 之問法是「若同儕亦在此量級，則 80.8% 是常態形狀而非異常」。
**實測答案：同儕在 100%，本 feature 在 80.8%，方向與擔憂相反。**

---

## 一、量測對象之選取

磁碟現況掃描（`find` + 分頁檢查），標準 036 分頁且有 ER 內容者四本：

| 本 | 有 req_id 列 | 有 ER 列 | 是否可分類 |
|---|---|---|---|
| `vehicle_setting` VF230 | 457 | 457 | **可** |
| `vehicle_setting` CFTS044（Arif 人寫 done region）| 237 | 191 | **不可**，見 §三 |
| `audio_mgmt` B1 generated | 70 | 70 | **可** |
| `privacy` regen-v1 | 11 | 11 | **不可**，見 §三 |

另三本（`power`、`audio_mgmt` AACP、`privacy` 原始）**無標準分頁**
（僅 `Cover_old`／`ChangeHistory_old`），排除。

**下放包建議之 AMFM v1 tagged 取不到** —— `features/amfm/inputs/` 於本機為空目錄
（`inputs/` 全案 gitignore，檔案不在此工作副本）。tag `fw036-amfm-regen-v1` 存在，
但 tag 只帶交付摘要，xlsx 本身不入 git。同上繳 08 §一-2 之情形。

---

## 二、逐本識別規則（§二-2 要求，不得默默調整判準）

**四本四種記法。** 判準（A／B／C 之定義）完全不變，變的只是「什麼字串算訊號」：

| 本 | 訊號識別規則 | 依據 |
|---|---|---|
| bed_lowering | `$MESSAGE.Signal$` | IN §8.7.5 v3（R-1 v3）|
| audio_mgmt B1 | `$MESSAGE.Signal$` | 同上，與本 feature 同慣例 |
| vehicle_setting VF230 | `Send CAN:` 前綴 **或** 裸 `MSG.Signal` | **R-VS52／R-VS67 之 override** —— IN §8.7.5 明載 vehicle_setting 依 SWC 0708 風格，不適用 v3 |

實測佐證各規則確實命中：VF230 之 `Send CAN:` 184 次、裸 `MSG.Signal` 776 次；
audio_mgmt B1 之 `$MSG.Sig$` 15 次。若對 VF230 套 v3 正則，命中為 **0**，
會得出「該本完全不用訊號」之假結論 —— 這就是本節存在的理由。

---

## 三、兩本套不上，具名回報（§四）

### 3.1 `vehicle_setting` CFTS044（Arif 人寫本）—— **判準套不上**

- ER 含結構化訊號記法 **0** 列、裸 `MSG.Signal` **0** 列
- ER 為自由散文，樣本：
  `CAN signal to be trigger System update CAN value to HMI HU show the Front Left Ventd Seat`
- 該句**同時是訊號斷言與畫面斷言**，且無結構可供機器區分判定對象

**不勉強給數字。** 若硬以「ER 是否含 CAN 字樣」分類（130 次命中），
得到的是另一個判準下的數字，與本 feature 之 A／B／C 不可比 ——
那正是 §二-2 所禁之「默默調整判準後直接給數字」。

**這一本原是最有價值的基準**（非本管線之人寫本），取不到很可惜，如實回報。

### 3.2 `privacy` regen-v1 —— 母體過小且無結構化記法

11 列，ER 含結構化訊號記法 0 列。散文式（`The Interior CAN is awake`）。
即使套上判準，11 列之百分比不具比較意義。

---

## 四、一個結構性發現（本包之副產物）

兩本可分類之同儕，**A 皆為 0 並非因為它們不用訊號**：

| 本 | 訊號出現於 Procedure | 出現於 ER | ER 含訊號之列 | 其中訊號落在 ER **最末行**者 |
|---|---|---|---|---|
| VF230 | 572 次 | 388 次 | 296 列 | **0** |
| audio_mgmt B1 | 9 次 | 6 次 | 6 列 | **0** |

**訊號一律落在 ER 中段（第 2 行／共 3 行），最末行一律是 HMI 觀察。**

這是一個穩定的撰寫慣例：**訊號用來確認前置條件已建立，最終判定留給畫面。**
本 feature 沿用同一慣例，差別只在另有 29 條之最終判定確實就是訊號值
（多為 Activation Gating 與 Fault Handling 之 `$ASCM_FD_2.BDL_Enbl$` 狀態斷言）。

**故 80.8% 反映的是 HMI 工作簿之共同形狀，不是本 feature 之選擇失當。**

### 判準盲區（§三 要求逐本回報）

「A 類最終 ER 同時含訊號與人字樣」之命中：VF230 **0**、audio_mgmt B1 **0**
（兩本 A 類皆為空集合，故不可能命中）。本 feature 為 1 條，已於上繳 14 §四-2 人工複核。

---

## 五、未入版控之本 feature 相關檔案（§五）

**git 操作專屬 Pei（R-G5），執行層未自行 commit。** 清單如下，交 Pei 一次處理：

| 狀態 | 路徑 | 是否含生效中之規則 |
|---|---|---|
| M | `docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` | **是** —— §4 `[OVERRIDE IN §10.4]`（R-BLM14(2)）自包 07 起生效 |
| M | `features/bed_lowering/DATA_REQUESTS.md` | **是** —— DR-2／DR-3／DR-4 之登記與 DR-1 結案動作清單 |
| ?? | `features/bed_lowering/COVERAGE_GAPS.md` | **是** —— R-BLM2 之 13 條不生成揭露 |
| ?? | `features/bed_lowering/DELIVERY_NOTE.md` | 否 |
| ?? | `features/bed_lowering/data/{testrail_new,bus_class_all,nonbus_verdict,pending_ledger}.tsv` | 否 |
| ?? | `features/bed_lowering/docs/handoff/{13,14,15}_*.md` | 否 |
| ?? | `features/bed_lowering/docs/upstream/{13,14}_*.md` | 否 |

共 13 項，**其中 3 項含生效中之規則**。
最要緊者為 profile —— **一個生效中的 `[OVERRIDE]` 不在版本控制裡**，
其他 session 讀 git 版之 profile 會看不到 §4。

---

## 六、執行層自陳

1. **本包未回答「80.8% 可不可接受」** —— 依 §四，該判定屬 Pei（台架能力為其領域）。
   本包只提供比較基準。
2. **可分類之同儕僅 2 本，且皆為本管線產出**（audio_mgmt、vehicle_setting 之 VF230 段）。
   **非本管線之人寫本（CFTS044）恰好是套不上的那本** ——
   故本包之基準**未涵蓋「人手寫的 HMI 工作簿長什麼樣」**，
   這是基準本身之限制，不是量測誤差。
3. **VF230 之 457 列未區分「本管線寫回的 438 條」與「其餘 19 列」**。
   R-BLM1 載該本有 438 TC 由本管線寫回；本包按整本計。
   若要純比「本管線 vs 人寫」，該本需先切段，本包未做。
4. **判準對 `$` 之依賴**：三本之識別規則皆以特定標點或大寫樣式辨識訊號。
   若某本以自然語言寫訊號名（如 CFTS044），判準即失效 —— §三 已具名該情形。

---

## 七、停點

**已停。** 量測報告產出，未改任何 TC 或工作簿。

待 Pei：
1. 依本包之基準重判交付前置第 2 項（`DELIVERY_NOTE.md` §8-2）——
   **執行層之建議已因本包而改變**：上繳 14 曾建議「重新評估目視判定可接受之裁定」，
   本包實測後，**該建議撤回** —— 同儕基準在 100%，本 feature 之 80.8% 無異常可言。
2. §五 之 13 項未入版控檔案（3 項含生效中規則）
3. R-G14 抽樣覆核與四筆 DR，狀態不變
