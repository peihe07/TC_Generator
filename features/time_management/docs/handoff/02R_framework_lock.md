# 02R — 上繳 02 之覆核，framework Part N 鎖定草案

分析層 → 執行層。覆核對象：`docs/upstream/02_framework.md`。

**結論：受理。** §5.4 之提請成立且已由分析層執行 —— 22 筆 leaf 描述全文
已讀，Set 3 與 Set 7 之判讀據此定案。Layer 2 維持七組不變，Layer 3 鎖定。
**Layer 2 仍待 Pei 簽**（Tier 2），本包為呈簽稿。

---

## 1. §0 逕行登記 R-TM13 —— 採納，且這是我第三次同型缺口

執行層逕行正確，其區辨亦正確：`01Z-A4` 明文寫「不自行調整」故僅提請，
本包無該限制且條文登記為歷來常規義務。

**但根因是我的**。三次同型：

| 次 | 自檢表列了 | 指令段漏了 |
|---|---|---|
| `01Z-A4` | —— | A-TM02a 升級（`01Z-A3` 已裁） |
| `02` | R-TM13 | R-TM13 之登記指派 |
| （同上） | Layer 2/3 | framework 落檔指派 |

```
R-TM14（分析層自裁，2026-08-20）—— 自檢表與指令段須一一對應

下放包末尾「本包產生之新條文清單」之每一列，指令段須有對應之登記指派
（寫入哪個檔、插在哪個位置、逐字內容）。自檢表列了而指令段未指派者，
視為下放包缺陷，非執行層漏做。

自檢表之功能是「確認條文已以區塊形式出現」，不等同「已指派落檔」。
兩者是不同的檢查，本包之前一直當成同一個。

依據：01Z-A4（A-TM02a）、02（R-TM13、framework）三次同型。
與 R-TM11／R-TM12／R-TM13 同族：四者皆為下放包自身之缺陷。
```

## 2. §5.4 第 1 項 —— 提請成立，分析層已補測

「Layer 2 是語意分組，章節只是外部檢驗；本包七組觀察全部僅憑章節，
未讀任何 leaf 描述全文，故只能說章節證據支持／不支持／無鑑別力，
不能說某組分對或分錯」—— **完全正確，且這是本次最有價值的一句。**

分析層已讀 037 之 `Requirement Description` 欄全 22 筆（沙箱副本，
唯讀解析）。結果如下。

### 2.1 Set 3 `Master Clock` —— 維持五筆不變，章節訊號為假陽性

五筆之描述（節錄關鍵字）：

| leaf | 描述關鍵字 |
|---|---|
| 005 Internal Clock Accuracy | maintain **internal clock** ±2 sec / 24h when GPS unavailable |
| 006 Internal Time Representation | maintain **internal time signal**, update HU_Time.Info |
| 016 Date Master Function | maintain an **internal calendar**, master for vehicle date |
| 018 Default Initialization | **initialize** time/date to default values after reset or battery reconnection |
| 021 Sleep/Wakeup Handling | maintain time using **internal counters** during sleep, update on wakeup |

**四筆之主要動詞與受詞完全同型：maintain internal {clock / time signal /
calendar / counters}。** 018 為該內部狀態之初始化。語意軸為
「內部計時狀態之維持與初始化」，五筆全部落在該軸上。**021 尤其不是
outlier —— 其描述與 005/006 是同一句型。**

**為何章節證據誤導**：`1.5.2.2 Time Indication management on Key Off
Status` 是**條件章節**（何時），非能力章節（做什麼）。spec 依敘述情境
分章，Layer 2 依能力分組，兩者本不同構。

```
R-TM15（分析層自裁，2026-08-20）—— Layer 3 訊號之判讀限制

canon §4.1.4 第 4 用途（章節分散即 Layer 2 切錯之訊號）僅在
「該 leaf 所落之章節為另一能力所有」時成立。若其所落章節為**條件章節**
（依情境／時機分章，如 Key Off、Wake Up、Power State）而非能力章節，
分散不構成訊號 —— spec 依敘述情境分章，Layer 2 依能力分組，
兩者不同構是預期的。

判讀順序固定：先讀 leaf 描述之語意軸，再看章節。章節證據不得單獨
推翻語意分組。

依據：Set 3 之 021，章節層孤立於 1.5.2.2（條件章節），
語意層與 005/006/016 同句型（maintain internal …）。
```

### 2.2 Set 7 `Fault Handling` —— 維持，且章節無鑑別力之判定正確

- 010：handle **invalid/missing** time signals using last valid values and fallback
- 022：send **SNA/default** values when time/date data is invalid or unavailable

同一能力（無效資料之處置）之兩個方向：010 收端（用最後有效值），
022 送端（發 SNA）。**成組成立。**

執行層稱「異常處理在 spec 中本就散佈於各功能章節之內，不會自成一節，
故章節證據對本組既不支持也不反對」—— 讀過描述後確認此判定正確，
且該理由本身即 R-TM15 之另一形態。

### 2.3 Set 4 之 020 —— 維持，`1.5.2.2` 之跨組共用不構成問題

020：synchronize time/date between HU, IPC, and LTM **via TIME_DATE
messages** —— 語意軸明確為訊息傳輸，屬 `CAN Transmission`。
其落在 `1.5.2.2` 是因同步發生於 Key Off／Wake 之時機，同 R-TM15。

**021 與 020 共用 `1.5.2.2` 而分屬兩組，是正確結果**：同一時機下，
一者維持內部計數（021），一者送出訊息（020）。時機相同、能力不同。

### 2.4 Set 5 之 019 —— 分析層自陳之不確定項解除

執行層以 `1.3.1.1.1 Time Display Configuration` 為據支持歸入 Display，
描述亦相符：enable/disable time/date features based on Proxi parameters
—— 其可觀察面為功能之顯示與否。**歸屬 Display 定案，不再標為不確定。**

### 2.5 §4.3 之 005 證據殘缺 —— 此觀察應併入 A-TM13

「005 之 `#SYS-RA = 2` 而 sections 僅 1，另一筆即 A-TM13 之 `SYS-RA-221`，
故其章節證據只有一半可用」—— **此為本包第二有價值之發現**，且是
A-TM13 首次出現具體下游影響。

A-TM13 之條文須補記：其影響不限於 `spec_reference` 欄無值可寫，
亦使 005 與 002 兩筆之章節證據殘缺，連帶影響 framework 之檢驗力。

---

## 3. framework Part N —— 鎖定稿（Layer 2 待 Pei 簽）

### 3.1 Layer 1

```
Test Group = "Time and Date"        （R-TM8，已裁）
```

### 3.2 Layer 2 —— 七組，維持 `02` §2.2 不變

| # | Test Set | leaf | 數 |
|---|---|---|---|
| 1 | `Manual Setting` | 001, 015 | 2 |
| 2 | `GPS Sync` | 002, 003, 004, 014 | 4 |
| 3 | `Master Clock` | 005, 006, 016, 018, 021 | 5 |
| 4 | `CAN Transmission` | 008, 009, 017, 020 | 4 |
| 5 | `Display` | 007, 011, 019 | 3 |
| 6 | `Zone and DST` | 012, 013 | 2 |
| 7 | `Fault Handling` | 010, 022 | 2 |

合計 22 = leaf 全集。經 §2 之語意複核，七組全部維持，無一調整。

### 3.3 Layer 3 —— 主軸章節（全表見 `data/leaf_to_section_probe.txt`）

| Test Set | 主軸章節 | 標題 |
|---|---|---|
| `Manual Setting` | `1.5.2.3` / `1.5.2.6` | Time / Date function setting（同層姊妹節）|
| `GPS Sync` | `1.3.1.1.3` / `1.5.2.4` / `1.5.2.5` | GPS TIME / Automatic Time Adjustment via GPS / GPS Time and Date |
| `Master Clock` | `1.3.1.1.2` / `1.3.1.1.6.2` | Vehicle Time / Date Master Requirements |
| `CAN Transmission` | `1.3.1.1.4` / `1.5.2.1` | Time Information Transmission / T&D indication management |
| `Display` | `1.3.1.1.1` / `1.3.1.1.5` / `1.3.1.1.5.1` / `1.3.1.1.6.3` | Display Configuration / Time Display / Formats / Date Display |
| `Zone and DST` | `1.3.1.1.5.3` / `1.3.1.1.5.4` | Time Zones / Daylight Saving Time |
| `Fault Handling` | —— | 無主軸；異常處理散佈各章（§2.2）|

**條件章節不列為任一組之主軸**：`1.5.2.2`（Key Off）、`1.5.2.7`（Output
behavior）依 R-TM15 為條件／輸出章節，跨組出現屬預期。

### 3.4 相鄰組界線（§8.2.1 用，寫 TC 時據此避免重複覆蓋）

讀過描述後浮現三處鄰接，**須在 framework 內明記**，否則 TC 作者會雙重覆蓋：

| 鄰接 | 界線 |
|---|---|
| 004 GPS Fallback ↔ 010 Invalid Data | 004 只管 **GPS 來源**不可用時改用內部時鐘；010 管**收到之時間訊號**無效時用最後有效值。觸發源不同 |
| 014 GPS Date/Time Broadcast ↔ 022 SNA Handling | 014 之描述含「or SNA if unavailable」，022 專責 SNA/預設值。**SNA 之送出規則屬 022**；014 只驗 GPS 資料之送出 |
| 018 Default Initialization ↔ 011 Time Format Handling | 018 管 reset／斷電後之預設值；011 管格式（12H/24H）跨喚醒週期之保存與廣播。兩者都涉「重開之後」，但一者是時間值、一者是格式 |

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加兩條（R-TM14、R-TM15）

於末尾追加，逐字：

```markdown
## R-TM14 — 自檢表與指令段須一一對應

（分析層，2026-08-20。上游包 `docs/handoff/02R_framework_lock.md` §1）

下放包末尾「本包產生之新條文清單」之每一列，指令段須有對應之登記指派
（寫入哪個檔、插在哪個位置、逐字內容）。自檢表列了而指令段未指派者，
視為下放包缺陷，非執行層漏做。

自檢表之功能是「確認條文已以區塊形式出現」，不等同「已指派落檔」。

依據：01Z-A4（A-TM02a）、02（R-TM13、framework）三次同型。
與 R-TM11／R-TM12／R-TM13 同族：四者皆為下放包自身之缺陷。

## R-TM15 — Layer 3 訊號之判讀限制

（分析層，2026-08-20。上游包 `docs/handoff/02R_framework_lock.md` §2.1）

canon §4.1.4 第 4 用途（章節分散即 Layer 2 切錯之訊號）僅在「該 leaf
所落之章節為另一能力所有」時成立。若其所落章節為**條件章節**（依情境／
時機分章，如 Key Off、Wake Up、Power State）而非能力章節，分散不構成
訊號 —— spec 依敘述情境分章，Layer 2 依能力分組，兩者不同構是預期的。

判讀順序固定：先讀 leaf 描述之語意軸，再看章節。章節證據不得單獨推翻
語意分組。

依據：Set 3 之 021，章節層孤立於 1.5.2.2（條件章節），語意層與
005/006/016 同句型（maintain internal clock / time signal / calendar /
counters）。
```

追加後 `## R-TM` 條數應為 **18**（16 + 2）。

### T2 — `ANOMALIES.md`：A-TM13 補下游影響

於 A-TM13 條文末尾追加，逐字：

```markdown
**下游影響（2026-08-20，執行層 02 上繳 §4.3 之發現）**

本條之影響不限於 `spec_reference` 欄無章節可寫，亦使受影響 leaf 之
**章節證據殘缺**，連帶降低 framework 檢驗之效力：

| leaf | `#SYS-RA` | 可解析出之章節數 | 缺口來源 |
|---|---|---|---|
| `SWE-RA-TIME&DATE-005` | 2 | 1 | `SYS-RA-221` → 物件 `6151328` 不在 CFTS 基線 |
| `SWE-RA-TIME&DATE-002` | 6 | 4 | `SYS-RA-224` → 物件 `6151331` 不在 CFTS 基線 |

即 005 之章節證據僅一半可用。framework 檢驗時若據其判定歸組，
係據殘缺樣本而為 —— 02R §2.1 之定案改以 leaf 描述之語意軸為據，
不依賴該殘缺章節證據。
```

### T3 — framework 落檔

建 `features/time_management/framework.md`，內容為本包 §3 全文
（§3.1 至 §3.4，含表格），檔首加：

```markdown
# framework — Time Management（Test Group: Time and Date）

**狀態：Layer 1 已裁（R-TM8）；Layer 2 [PROPOSED]，待 Pei 簽；
Layer 3 依實測鎖定（`data/leaf_to_section_probe.txt`）。**

**Layer 2 未經 Pei 簽核前，不得據以生成任何 TC。**

來源：`docs/handoff/02R_framework_lock.md` §3。
語意複核依據：037 `Requirement Description` 欄全 22 筆（分析層讀）。
章節對映依據：`data/leaf_to_section_probe.txt`（執行層 02 上繳 §3）。
```

**不寫入 `docs/fw036/framework.md`**（全域檔，跨 feature，待 Pei 裁
是否併入）。

### T4 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 18
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 16（T2 不增條）
grep -n '下游影響' features/time_management/ANOMALIES.md     # 應命中 A-TM13 內
test -f features/time_management/framework.md && echo OK
```

四項不符即回報，不自行調整。

### T5 — 上繳

`docs/upstream/02R_corrections.md`，僅差異。須含：

1. T4 四項結果
2. T1–T3 之寫入確認
3. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集
   —— 請續用 02 上繳 §5.1 之五全集（第 5 個「草案設計說明之逐項可驗性」
   為執行層本包新增，分析層採納為常態）

### 不得執行者

- 不動 git
- **不生成任何 TC**（Layer 2 待 Pei 簽）
- 不寫 `docs/fw036/framework.md`（全域檔）
- 不改 §3.2 之七組分組
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不以 openpyxl 存回任何工作簿
- 不跑 `recon.py`（A-TM15）

---

## 5. 呈報 Pei

| # | 事項 | 建議 |
|---|---|---|
| 1 | **framework Layer 2 七組** | 待簽。§2 已以 leaf 描述語意軸複核，七組無一調整；Set 3 之章節訊號經查為假陽性（條件章節所致） |
| 2 | A-TM02a（037 身分）+ A-TM13（2 筆 CFTS 缺口） | RD-1 併問。A-TM13 現有具體下游影響（005 章節證據半殘） |
| 3 | R-TM10-A1 解除／替代樣式來源 | 仍 SUSPENDED |
| 4 | `recon.py` 五項修法 | 併為一次 |
| 5 | `docs/fw036/framework.md` 是否併入本 feature 之 Part N | 全域檔，本包未寫 |

## 6. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | **指令段指派** |
|---|---|---|---|
| R-TM14 | 分析層自裁 | §1 | ✅ T1 |
| R-TM15 | 分析層自裁 | §2.1 | ✅ T1 |
| A-TM13 下游影響 | anomaly 補記 | §2.5 | ✅ T2 |
| framework Part N §3.1–3.4 | Layer 2 待簽 | §3 | ✅ T3 |

分析層本包未動 git、未改腳本、未改執行層產出之任何檔案。
§2 之 leaf 描述讀取跑在 Project 附件之沙箱副本（唯讀解析）；
其為文字內容比對，非檔案狀態，依 charter 屬沙箱可用範圍。
