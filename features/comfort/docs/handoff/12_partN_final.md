# 12 — Comfort HMI / Part N 定稿（已簽署）

- 產出層：分析層｜2026-08-14｜對象：執行層
- 簽署：Pei，2026-08-14（「是」）
- 取代：`11_partN_draft.md` §2 之草案表。11 之 §1、§3、§5、§6 仍有效。

---

## 1. 分析層查證結果 —— ch11／ch12 合併

11 §4.1 曾將 ch11／ch12 拆為兩組並請 Pei 裁定。Pei 指出該項應由分析層查證
而非上呈。查證已完成，結論：**合併**。

實測 `data/layer3_map.tsv` 之節標題：

| ch11 R1 Heated/Vented Seats | ch12 Heated/Vented Seats - CARRYOVER |
|---|---|
| 11.1 `HVS1.` Multi-Level 加熱座椅按壓 | 12.1 `HVS1.` Multi-Level 加熱座椅按壓 |
| 11.2 `HVS2.` 通風 | 12.2 `HVS2.` 通風 |
| 11.3 `HVS4.` climate OFF 時狀態列 | 12.4 `HVS4.` climate OFF 時狀態列 |
| 11.4 `HVS5.` 加熱鍵亮紅 | 12.5 `HVS5.` 加熱鍵亮紅 |
| 11.5 `HVS6.` 參照 HMI Settings List | 12.6 `HVS6.` 參照 HMI Notes |
| 11.6 ~ 11.11.1 `R1HVS*`／`W1HVS2` 獨立座椅分區、加熱方向盤 | 12.8 ~ 12.9 `SHVS*` Standard 座椅 |

`HVS1／HVS2／HVS4／HVS5／HVS6` 五個條款標籤跨兩章重複，開頭文字近乎逐字
相同。兩章皆為同一 comfort 畫面與狀態列上之座椅／方向盤控制；**無證據顯示
進入路徑不同**，差異在設備等級（Multi-Level／Single-Level／Standard）與
program baseline。

設備等級為能力**之內**之變體軸（§8.3 sibling axis），非不同進入路徑。
依 §4.2「Prefer broader shared capability when unsure」→ 合併。

### 判準（本 feature 內一體適用，使 ICS 之分立與本項之合併互相一致）

> **測試：該組是否隱含共用之 setup pattern 與 UI 進入路徑？**
> - **ICS（ch16）** —— 車輛須為 EMEA ICS 變體，操作走實體控制堆疊。
>   setup 與進入路徑皆不同 → **分立**
> - **ch12 carryover** —— 同畫面、同控制，僅座椅等級與 baseline 不同
>   → **合併**

### A-CF13 第三項（新增）

`HVS1／HVS2／HVS4／HVS5／HVS6` 跨 ch11／ch12 重複，為本 feature 第三處
條款標籤衝突（前兩處：`C16.)` 跨 2.15／16.17；`W0.)` 跨 17.1／18.1／19.1）。

合併之副效果為正向：近似重複落於同一 Test Set，§4.6 之 sibling 判定與
`duplicate_of` 得以見效；分立則兩者分屬兩組，審閱者看不到彼此。

---

## 2. Part N 定稿 —— Test Group `Comfort`，15 個 Test Set

| # | Test Set | Layer 3（spec sections） | leaves |
|---|---|---|---|
| 1 | `Front Climate Anatomy` | 2.1, 2.2, 6.3 | 12 |
| 2 | `Climate Modes` | 2.3, 2.3.1, 2.4, 2.5, 2.5.1, 2.10, 2.11, 2.13, 2.14, 2.16 | 41 |
| 3 | `Temperature and Fan` | 2.6, 2.6.1, 2.7, 2.7.1 | 17 |
| 4 | `Airflow and Defrost` | 2.8, 2.9, 2.12, 2.12.1, 2.12.2, 2.15 | 23 |
| 5 | `Tri-Mode Climate` | 3.1, 3.2, 3.3, 3.4 | 14 |
| 6 | `Rear Climate` | 7.1, 7.1.1, 7.2 ~ 7.10, 9.1 ~ 9.4.1 | 46 |
| 7 | `ECO HVAC` | 10.1 ~ 10.9.1 | 15 |
| 8 | `Heated Vented Seats` | 11.1 ~ 11.11.1, 12.1 ~ 12.9 | 59 |
| 9 | `Seat Control Tab` | 13.2 ~ 13.6 | 14 |
| 10 | `Climate Popups` | 14.1 ~ 14.19, 15.1 | 42 |
| 11 | `ICS Anatomy` | 16.2, 16.16 | 14 |
| 12 | `ICS Climate Modes` | 16.3, 16.4, 16.5, 16.10, 16.11, 16.13, 16.14, 16.17 | 40 |
| 13 | `ICS Temperature and Fan` | 16.6, 16.6.1, 16.7 | 16 |
| 14 | `ICS Airflow and Defrost` | 16.8, 16.9, 16.12, 16.12.1, 16.15 | 29 |
| 15 | `Comfort Widget` | 17.1 ~ 17.5, 18.1 | 21 |

**合計 403。** 區間 12–59；最大者佔 14.6%。

### 必要之 assertion（PASS/FAIL + 實測值）

1. 各 Test Set `leaf_count` 總和 == 403
2. `layer3_map.tsv` 之 129 節**每節恰屬一個** Test Set（無漏、無重）
3. 章別回算：ch2 == 92、ch16 == 99、其餘 12 章與上繳 01 §3 逐章相符
4. Test Set 名稱皆不含 `Comfort` 一詞以外之 Test Group 前綴、無
   `Misc`／`General`／`Unclassified`、無前後空白

期望值寫死於腳本，不由同一份資料回推。

---

## 3. 分析層自身之訂正

11 §2 記章 6 之節次為 `6.1`，**實測為 `6.3`**（`CM1.) When a vehicle is
configured with a non-foldable second…`）。本定稿已更正。

**該節之落位為暫置。** 其全文分析層無法讀取（SR24 export 為 xlsx，唯讀探測
不可及），僅憑 60 字截斷判斷；「non-foldable second row」語意偏後座，與
所置之 `Front Climate Anatomy` 未必相符。

**執行層指示**：寫 `framework.md` 時讀 `6.3` 全文，確認落位。
**若判斷應改置他組（如 `Rear Climate` 或 `Seat Control Tab`），回報，
不自行搬移** —— 落位屬 Part N 內容，Part N 已簽署，變更須回分析層。

---

## 4. 未入 Part N 者（重申，同 11 §5）

- 17 節 substantive：`in_scope` 4 節依 R-C16 為 RD-1 覆蓋缺口項；
  `undetermined` 13 節尚無處置。皆不入 Test Set、不入 coverage 分母。
- **插入邊界**：章 20 若日後 in_scope → 新增 Test Set `Rear Blower`，
  **不併入 #6**（進入路徑與市場變體不同，同 §1 判準）。
  章 19 若日後 in_scope → 併入 #15 `Comfort Widget`。
  兩處皆不需重整既有切分。

---

## 5. 執行指示

1. 寫 `features/comfort/framework.md`：
   - Layer 1 = `Comfort`
   - Layer 2 = 上表 15 個 Test Set
   - Layer 3 = section 對照表
   - **Layer 3 不入工作簿**（§4.1.5）：不得存入工作簿欄位、
     不得串接進 Test Set 名稱
2. 執行 §2 之四個 assertion，以 PASS/FAIL + 實測值輸出。
3. 讀 `6.3` 全文，依 §3 確認或回報。
4. `DECISIONS.md`：
   - 第 6 項 Framework Part N 由 `[PROPOSED]` 轉為已定，記本包為依據
   - 第 6 項 profile `[OVERRIDE]` 仍為 Tier 2，**維持未定**
   - 依 05 §4 之兩項建議填入：exemplar source 具名 `home`（144 列，
     done region）、**`amfm` 具名排除**；batch plan pilot 取第 13 章
     （`Seat Control Tab`，14 leaves）
   - **Sign-off 區塊填入**（R-C10）：Reviewed by `PeiPYHsu`、
     Date `2026-08-14`、Ruling notes 註明 Part N 依本包簽署
5. 上繳 `docs/upstream/06_framework.md`，附「本包是否仍有該驗而未驗者」
   之獨立判斷，更新 `docs/INDEX.md`。
6. **Phase 4 不開始。** 本包只到 framework 落地與 `DECISIONS.md` 簽署。
7. git 不執行，只準備 commit message。

---

## 6. 本包產生之新條文清單（自檢）

無新條文。§1 之判準為 Part N 內部之設計依據，隨 `framework.md` 落地，
不以 R-Cnn 形式進入 `RULINGS.md`。A-CF13 新增第三項為 anomaly 更新，
非條文。
