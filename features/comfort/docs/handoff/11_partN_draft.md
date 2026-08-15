# 11 — Comfort HMI / Part N 草案（Layer 2 Test Set）

- 產出層：分析層｜2026-08-14｜對象：Pei（Tier 2 簽署）／執行層（簽署後執行）
- 依據：上繳 05 之 Layer 3 map（129 節、403 leaves、section↔parent 1:1 雙射）
- 狀態：**草案，未簽署。** 簽署前執行層不得依此寫 `framework.md`。

---

## 1. 先答執行層 §9.4 之問：章 2／16 逐條覆核 **不做**

執行層問：若 Part N 要利用章 2 與章 16 的平行性，那份對應表需逐條覆核；
該工作屬 Tier 2 或可下放。

**答：兩章不合併，故該覆核不是 Part N 的前置，暫不做。**

理由在 §4.2 而非在等價與否：「Same Test Set should imply a shared setup
pattern and UI entry path」。章 16 是 **ICS 實體控制 + EMEA carryover**，
其 UI 進入路徑與市場變體皆與章 2 之觸控面不同。**即使逐條等價，也不應合併**
—— 等價的是「能力」，不同的是「進入路徑」，而 §4.2 綁的是後者。

故執行層 §9.2 第 1 項之風險（對應表未逐條覆核）**不落在 Part N 的關鍵路徑
上**。該對應表在本草案中只用於一件事：讓兩章的 Test Set **結構彼此鏡像**，
方便導覽。鏡像即使有個別條文對不齊也不失效。

若日後 Pei 傾向合併型切法，該覆核才成為前置，屆時屬 Tier 2（產生「哪些條文
等價」之判斷），由分析層做。

---

## 2. Part N 草案 —— Test Group `Comfort`，16 個 Test Set

| # | Test Set | Layer 3（spec sections） | leaves |
|---|---|---|---|
| 1 | `Front Climate Anatomy` | 2.1, 2.2, 6.1 | 12 |
| 2 | `Climate Modes` | 2.3, 2.3.1, 2.4, 2.5, 2.5.1, 2.10, 2.11, 2.13, 2.14, 2.16 | 41 |
| 3 | `Temperature and Fan` | 2.6, 2.6.1, 2.7, 2.7.1 | 17 |
| 4 | `Airflow and Defrost` | 2.8, 2.9, 2.12, 2.12.1, 2.12.2, 2.15 | 23 |
| 5 | `Tri-Mode Climate` | ch3 全 | 14 |
| 6 | `Rear Climate` | ch7 全, ch9 全 | 46 |
| 7 | `ECO HVAC` | ch10 全 | 15 |
| 8 | `Heated Vented Seats` | ch11 全 | 37 |
| 9 | `Heated Vented Seats Carryover` | ch12 全 | 22 |
| 10 | `Seat Control Tab` | ch13 全 | 14 |
| 11 | `Climate Popups` | ch14 全, ch15 全 | 42 |
| 12 | `ICS Anatomy` | 16.2, 16.16 | 14 |
| 13 | `ICS Climate Modes` | 16.3, 16.4, 16.5, 16.10, 16.11, 16.13, 16.14, 16.17 | 40 |
| 14 | `ICS Temperature and Fan` | 16.6, 16.6.1, 16.7 | 16 |
| 15 | `ICS Airflow and Defrost` | 16.8, 16.9, 16.12, 16.12.1, 16.15 | 29 |
| 16 | `Comfort Widget` | ch17 全, ch18 全 | 21 |

**合計 403**（12+41+17+23+14+46+15+59+14+42+14+40+16+29+21）。
章別驗算：ch2 = 12−1(6.1) +41+17+23 = 92 ✅；ch16 = 14+40+16+29 = 99 ✅。

執行層簽署後須以 assertion 驗算：各 Test Set leaves 總和 == 403、
每個 section 恰屬一個 Test Set、129 節全數獲派。

---

## 3. 設計依據

**Test Set 數 16，區間 12–46。** 通過 §4.1.3 之決策測試：任一 Test Set
篩選後既非單一 TC（最小 12），亦非整個工作簿（最大 46 = 11.4%）。無
`Misc`／`General`／`Unclassified`。無 Test Group（`Comfort`）前綴（§4.2）。

**#12–15 之 `ICS` 前綴不違反 §4.2** —— 該條禁的是重複 Test Group，
`Comfort` 未出現；`ICS` 是 UI 進入路徑之限定詞，正是 §4.2 所要的
「shared setup pattern and UI entry path」之標記。

**#2 / #3 / #4 與 #13 / #14 / #15 刻意鏡像**，使審閱者在觸控面與 ICS 面之間
移動時面對同一組概念邊界（§4.1.4 第 1 點：TC 排序與審閱者的認知成本）。

**章 6（`6.1`，1 leaf）併入 #1 而非自成一組** —— 12.3" 之 Comfort 頁為
螢幕尺寸變體，屬 anatomy 範疇；單一 leaf 自成 Test Set 會使 Test Set 欄
淪為 TC ID 之副本（§4.1.3「過細」）。

---

## 4. 三處須 Pei 裁定之邊界

### 4.1 #8 / #9 是否應合併（**我最不確定的一處**）

ch11「R1 Heated/Vented Seats」與 ch12「Heated/Vented Seats - CARRYOVER」，
草案依 ICS 之同一邏輯拆開（carryover 為不同變體）。

但 **ICS 之拆分依據是「進入路徑不同」（實體控制鍵），而 ch12 是否也走不同
進入路徑，本草案未經查證**。若 ch12 只是同一觸控面上的舊版行為，則依 §4.2
應與 ch11 合併為單一 `Heated Vented Seats`（59 leaves）。

**可解此題之證據**：ch11 與 ch12 之首節條文是否描述不同的操作入口。
一次逐節閱讀即可，成本低。若 Pei 要求，可下放執行層取證後再定。

### 4.2 #2 `Climate Modes` 41 leaves 是否再拆

41 為次大組，內含 AUTO／AC／Recirc／MAX A/C／MTC／Climate Off／SYNC 七類
開關狀態。可再拆為 `Climate On Off and Sync`（2.10, 2.11 = 11）與
`Climate Modes`（其餘 30）。

草案選擇不拆：七者共用同一組合鍵區與同一狀態指示列，符合 §4.2「不同 sub-state
應共用一個 Test Set」。惟若 Pei 認為 41 過大，上述切法可直接採用，
#13 亦須同步鏡像拆分以維持結構對稱。

### 4.3 命名之大小寫與拼寫

全部採 Title Case、無縮寫展開（`ICS`、`ECO HVAC` 保留原文）、無標點。
`Heated Vented Seats` 不寫 `Heated/Vented Seats` —— 斜線在欄值中易生
比對歧義。此為格式決定，屬 Pei。

---

## 5. 不入 Part N 者（重申）

- 17 節 substantive：`in_scope` 之 4 節依 R-C16 為 RD-1 覆蓋缺口項；
  `undetermined` 之 13 節尚無處置。**皆不入 Test Set、不入 coverage 分母。**
- 章 20（Alternate Rear Blower）若日後 in_scope，其插入點為新增 Test Set
  `Rear Blower`，不併入 #6 `Rear Climate`（進入路徑與市場變體不同，
  同 ICS 之理）。
- 章 19（7" widget）若日後 in_scope，插入 #16 `Comfort Widget`。

此二插入點即 07 §5 所要求之「可插入邊界」，本草案已預留，不需重整。

---

## 6. A-CF13 之處置建議（併請裁）

- **`C16.)` 重複**（2.15 與 16.17）：Phase 4 撰寫時一律以 **outline 節次**
  為引用鍵，不以條款標籤為引用鍵。`specification_reference` 依 §10.7 本就
  用 `{spec_filename}_{section_id}`，故此問題不影響工作簿輸出，只影響
  `reasoning` 與 `test_item` 之敘述。列 RD-1 候選，不阻塞。
- **`W0.)` 三節共用**：17.1 與 18.1 各有一個 parent，6 leaves 覆蓋同一條
  規範句。草案將兩者同置 #16，故不會產生跨 Test Set 之重複。Phase 4 須就
  此 6 leaves 做 sibling 判定（§4.6），可能出現 `duplicate_of`。
  **此為 Phase 4 之判斷，不在本草案處理。**

---

## 7. 簽署後之執行指示（簽署前不得執行）

1. 依本草案寫 `features/comfort/framework.md`：Layer 1 = `Comfort`，
   Layer 2 = 16 個 Test Set，Layer 3 = section 對照表。**Layer 3 不入工作簿**
   （§4.1.5）。
2. 三個 assertion 驗算（見 §2）。
3. `DECISIONS.md` 第 6 項（Framework Part N）由 [PROPOSED] 轉為已定，
   併同 Pei 之簽署一併填入 Sign-off（R-C10）。
4. 上繳 `docs/upstream/06_framework.md`。

---

## 8. 本包產生之新條文清單（自檢）

無新條文。本包為 Tier 2 草案，其內容於 Pei 簽署後成為 `framework.md`，
不以 R-Cnn 形式進入 `RULINGS.md`。

§4.1／§4.2／§4.3 三項邊界待 Pei 裁定；§1 之「不做逐條覆核」為分析層自裁
（比對方法之技術性選擇），已生效。
