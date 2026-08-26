# 下放包 11 —— Vehicle Category：pilot 停點之裁定（profile ＋ 爭議值 verbatim）

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/11_pilot_resume.md`
- 前一包：`docs/handoff/10_pilot_tc.md`
- 對應之上繳包：`docs/upstream/10_pilot_tc.md` §8 待裁三項
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 現止於 `10_`，無碰撞。

---

## 一、上繳包 10 之覆核

**核可,無退回項。** 停於收斂條件第 7b 項、不自行修補後續、
兩個停點皆具名待裁 —— 處置正確。四項具名：

1. **§5.3 之「三件我沒有做的事」全部正確。** 尤其第 2 項
   （不代 profile 說話）—— §11 之例外其啟動條件寫的是
   「when the feature profile says so」，無 profile 即無例外，
   自行援用等於偽造一份不存在的 profile。
2. **§3.1 之檢查器自報錯誤**（modal 未排除引號內 `must`）
   與 **§9 之「寫檢查器的人和寫被檢查物的人是同一個」** ——
   後者是本輪最有價值的一句自我限定，本包據以在 §四加一項配套。
3. **§4 第 17 項自陳「該項尤應由你複核，不宜採信我的自評」** ——
   採認，本包 §四第 3 項處理。
4. **§5.5「若第一次遇到它是在 100 筆的批次裡，代價是 100 筆的返工」** ——
   成立。這是 pilot 選 `Glove Box` 之決定於此兌現。

---

## 二、§5 之停點：裁 **甲**（寫 VC profile）

### 2.1 否決乙與丙

**乙（立 R-VC 專條）否決**：裁決層記的是本 feature 之**政策決定**
（範圍、母體、錨點、優先級判準）；引號記法屬**格式規範**，
其歸屬是 profile。以裁決條代 profile，等於讓 profile 繼續缺著，
而下一個格式問題還會再來一次。

**丙（歸入 R-4 排版正規化）否決 —— 且理由不只是邊界**：
引號記法**不是排版，是引用之忠實性**。R-4 允許句首字母轉大寫，
因其不影響語意亦不影響可追溯性；引號記法一旦改寫，
讀者無法自 TC 反推規格原文用的是 `'...'` 還是 `«...»`，
**verbatim 之證據力即受損**。且 R-4 為全域條，丙會使全部 13 個
feature 之 verbatim 判準一起鬆動。

### 2.2 R-VC19（裁決條文，逐字抄入 `RULINGS.md`）

```
R-VC19（VC profile 之設立；§11 引號例外之啟動）

（Pei 授權範圍內之 Tier 2 裁定，2026-08-26。）

本 feature 設立 profile：
  `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md`
命名依既有慣例（CamelCase 無分隔，同 `VehicleSetting`／`PowerModing`／
`UserProfiles`）—— 該慣例非由 `feature` 字串機械推導，見 R-VC1 之註。

profile 之**首要條款**為啟動 IN §11 之引號例外，其範圍嚴格限定：

(a) **僅 `test_item` 上半之 verbatim 區段**得保留來源記法。
    037 `Requirement Title` 之 `'...'` 與 `Requirement Description` 之
    `«...»` 皆為來源記法，於該區段內逐字保留，不改寫。
(b) **作者之散文一律 `"..."`** —— procedure 之按壓標的、
    非引用之 ER 行、括號下半、reasoning，無例外。
    上繳包 10 §3 第 7 項已驗此層全數合規，該狀態須維持。
(c) 保留之記法**須對得上所引之來源列** —— 即該 token 確實逐字出現於
    該 leaf 之 `Title` 或 `Description`。lint 之職責由「禁止」
    改為「驗證其來源」（IN §11 例外末句之明文）。
(d) 本例外**不及於**任何其他欄位、不及於 `«...»` 以外之新記法。
    若日後出現第三種來源記法，須另裁後始得納入，**不得類推**。

依據：IN §11 之例外其啟動條件為「when the feature profile says so」。
在 profile 存在並載明之前，該例外未啟動 —— 執行層拒絕自行援用
（上繳包 10 §5.3 第 2 項）為正確處置。

本條不改任何既有全域條文。R-4 之範圍不變，引號記法**不屬**
排版正規化 —— 其改寫會使讀者無法自 TC 反推規格原文之記法，
損及 verbatim 之證據力。
```

### 2.3 profile 之最小內容

**只寫當前需要的,不預先設計未來條款**（避免 A-VC8 家族之
「宣告一個不被讀的東西」）。最小內容四節：

1. **§0 適用範圍** —— feature slug、test_group、其權威來源（R-VC16／R-VC4）
2. **§11 `[OVERRIDE]` 引號例外** —— 逐字採 R-VC19 (a)–(d)
3. **lint 之 profile 分流** —— 先查 `scripts/lint036.py` 對
   `--profile` 之現有支援程度（IN §8.7.5 記其已有分流機制），
   **如實回報其能否實作 (c) 之「驗證來源」**。
   若現況只能「禁止或放行」而無法驗證來源，
   **據實記為 profile 之已知限制並登記 A-VC{n}，不得改 lint**
   （R-VC8 之授權邊界不涵蓋 lint）。
4. **§8.7.5 之適用** —— 本 feature 037 全文之 CAN／PROXI／VF 命中皆為 0
   （下放包 02 R-VC10），故 §8.7.5 之訊號寫法條款**於本 feature 無適用對象**，
   記明以免日後誤引。

---

## 三、§6 之裁定：**(b)**，並立通則

### 3.1 先釐清一件事：那不是自我矛盾

`test_item` 上半是**引用**，不是**斷言**。
其性質為「規格對此事的原話是這樣」，非「本 TC 認定門檻為 3」。

`test_procedure` 之 `PENDING` 則是**執行側**之狀態：這個值現在不可用。

二者分屬需求側與執行側，**其不一致正是忠實反映了上游的狀態** ——
上游的 Title 說 3，而該值有爭議且未解。若為了讓 TC 內部看起來一致
而改寫或迴避 verbatim，那是**把上游的問題藏進我們的產出**。

執行層之顧慮（讀者會困惑）成立，但其解方不是消除不一致，
是**讓不一致可被讀懂**。

### 3.2 R-VC20（裁決條文，逐字抄入 `RULINGS.md`）

```
R-VC20（verbatim 上半含爭議值之處置）

`test_item` 上半之 verbatim 若含一個正由 DR 爭議之值
（其值於 037 二欄不一致，或與規格／DBC 不一致），處置三項：

(a) **verbatim 照抄，不改寫、不迴避、不換欄取值。**
    上半為引用而非斷言；改寫損及 R-S4 所要之規格原句，
    換取另一欄之值則只是換一個爭議值（上繳包 10 §6(a) 已指出）。

(b) **該爭議須於 `reasoning` 明文揭露**，四項齊備：
    二欄各自之逐字內容、其分歧點、以何欄為 verbatim 上半及其理由
    （R-S4 要規格原句，非採信其值）、阻斷之 DR 編號。
    **括號下半之提示（如 `threshold value pending`）不構成揭露** ——
    其為 sibling 區分 token，欄位性質不同（上繳包 10 §6(b) 之自陳正確）。

(c) **該爭議值不得出現於 `expected_result` 之判準位置。**
    ER 是 pass/fail 之依據；一個未定之值不得成為判準。
    ER 應以行為表述（「the deactivation feature is blocked」），
    次數門檻由 procedure 之 `PENDING` 承載。

即時適用：`SWE1-HMI-VC-033-01` 依 (a) 保留 Title 之
`After three sequential wrong PINs` 為 verbatim 上半；
依 (b) 補 `reasoning` 之四項揭露；依 (c) **須複查其 ER 是否出現
`third`／`three`／`fourth` 等次數判準**，出現即改為行為表述。

DR-VC8 回覆後，本筆依其值 Revise，並依 R-VC18 另裁是否補拆
boundary 之 2–3 筆。
```

---

## 四、續作之三項配套

1. **§4 第 17 項之複核（執行層自陳不宜採信自評）** ——
   `-028-02` 與 `-033-01` 之流程區分，由**分析層**於下一輪上繳後
   逐字複核其括號下半與 reasoning，不採信機械檢查之
   「含 activation／deactivation 字樣」。
2. **檢查器之判準錯誤（§9 之自我限定）** —— 本輪兩支新檢查器各出一錯，
   成因為「寫檢查器與寫被檢查物者同一」。配套：
   `verify_pilot.py` 之**每一項判準須於上繳包載明其反例**
   （什麼樣的輸入應該 FAIL），使判準本身可被複核。
   本輪已知二例（modal 未排除引號、T52 之類別切分）逐項記入。
3. **T52 之全表掃描結果**尚未見於上繳包 10 —— 若已完成請一併回報；
   A-VC14(c) 明文「未掃描其餘 116 個 leaf 是否存在同型矛盾，
   本條不得被讀為全表僅此一例」，R-VC20 之適用範圍取決於該掃描。

---

## 五、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T60 | 抄錄 R-VC19／R-VC20 入 `RULINGS.md`（接 R-VC18 之後），byte-level diff | 1 |
| T61 | 依 §二.3 寫 `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md`（四節最小內容）。**先查 lint036.py 之 `--profile` 支援程度並如實回報**；不得改 lint | 1 |
| T62 | 依 R-VC19 重驗 6 筆之 verbatim 上半（`026-01`／`026-02`／`027`／`030`／`031`／`032`），確認其保留之記法逐字出現於該 leaf 之 Title 或 Description（R-VC19(c)）| 1 |
| T63 | 依 R-VC20 修 `VC-033-01`：(b) 之四項揭露補入 `reasoning`；**複查 ER 有無次數判準**，有則依 (c) 改為行為表述 | 1 |
| T64 | 重跑 `verify_pilot.py`，收斂條件十項全過。依 §四.2 為每項判準載明其反例 | 1 |
| T65 | T52（A-VC14 同型矛盾全表掃描）如未完成則本輪完成；完成則回報結果 | 1 |
| T66 | `RUNBOOK.md` 之 Phase 3 profile 項勾選；`ANOMALIES.md` 記 §二.3 第 3 項之 lint 限制（如成立）| 1 |

**不在本輪範圍**：寫回工作簿（Phase 6）、其餘 7 個 Test Set、
`VC-033-01` 之 boundary 拆分（待 DR-VC8）。

---

## 六、上繳包要求

1. T60–T66 逐項結果
2. R-VC19／R-VC20 之 byte-level diff
3. profile 全文 ＋ lint `--profile` 支援程度之如實回報
4. `verify_pilot.py` 重跑之全輸出（十項全過），**每項判準之反例**
5. `VC-033-01` 修改前後之 `reasoning` 與 ER 對照
6. T52 之全表掃描結果
7. 量測條件揭露（R-G8）

---

> 同批 A（五項）與 DR-VC3 仍待發送（Tier 3）。不再重複列於後續包。
