# 下放包 10 —— Vehicle Category：Phase 4 pilot（Glove Box）

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/10_pilot_tc.md`
- 前一包：`docs/handoff/09_pilot_amend.md`
- 裁定：Pei 2026-08-26 —— **pilot 采 `Glove Box`**
- **本包授權產出 12 筆 TC 之 JSON。不授權任何寫回工作簿。**

---

## 一、裁決條文（逐字抄入 `RULINGS.md`）

```
R-VC18（Phase 4 pilot：Glove Box）

（Pei 2026-08-26 裁定。）

pilot Test Set ＝ **#3 `Glove Box`**（R-VC16）。

範圍：12 leaf（117 leaf 母體）／ 8 section（66 section 母體）——
  4.1  SWE1-HMI-VC-026-01 / -026-02 / -026-03
  4.2  SWE1-HMI-VC-027
  5.1  SWE1-HMI-VC-028-01 / -028-02
  5.2  SWE1-HMI-VC-029
  6.1  SWE1-HMI-VC-030
  6.2  SWE1-HMI-VC-031
  6.3  SWE1-HMI-VC-032
  7.1  SWE1-HMI-VC-033-01 / -033-02

**產出 12 筆 TC，一 leaf 一 TC。**

`SWE1-HMI-VC-033-01` 之 boundary 拆分（§8.3：門檻−1 / =門檻 /
鎖定期滿）**本輪不做** —— 其門檻因 A-VC14 而未定，拆分點無從定值。
本輪就該 leaf 產 1 筆 TC，其門檻欄填
`PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3）。
DR-VC8 回覆後另裁是否補拆為 2–3 筆。

**本輪不寫回工作簿。** 產出為 JSON，置於 `generated/`。
寫回屬 Phase 6，另裁。

pilot 之收斂條件見下放包 10 §四。收斂後始得議 Phase 4 之全量批次。
```

---

## 二、逐 leaf 之產出規格

`Test Group` = `Vehicle Category`（G 欄）
`Test Set` = `Glove Box`（H 欄）—— 12 筆皆同，不得出現變體拼寫

| # | req_id | §節 | priority | 驗證標的（一句） |
|---|---|---|---|---|
| 1 | `VC-026-01` | 4.1 | P1 | 選 Glove Box 後彈出「說明所需動作」之彈窗 |
| 2 | `VC-026-02` | 4.1 | P1 | 於該彈窗按 Yes 後彈出 PIN 請求彈窗 |
| 3 | `VC-026-03` | 4.1 | P1 | PIN 須輸入兩次，二次之間**僅指示文字不同** |
| 4 | `VC-027` | 4.2 | P2 | 兩次相符後顯示 `Glove Box Activated` 確認彈窗 |
| 5 | `VC-028-01` | 5.1 | P1 | 第二次輸入與第一次不符 → `Incorrect PIN. Please try again` |
| 6 | `VC-028-02` | 5.1 | P1 | 啟用流程**不限**錯誤次數 |
| 7 | `VC-029` | 5.2 | P1 | N 次錯誤後輸入**第一次所設之** PIN → 功能啟用 |
| 8 | `VC-030` | 6.1 | P1 | 於 Controls 按 Glove Box 開啟要求**同一 PIN** 之停用彈窗 |
| 9 | `VC-031` | 6.2 | P2 | 停用 PIN 通過後顯示 `Glove Box Mode deactivated` |
| 10 | `VC-032` | 6.3 | P3 | 按 OK 關閉彈窗並返回 Controls 主頁 |
| 11 | `VC-033-01` | 7.1 | P1 | 停用連續錯誤達門檻 → 鎖定 30 分鐘（**帶 PENDING**）|
| 12 | `VC-033-02` | 7.1 | P2 | 停用時輸入 3 位數後按 Enter → `PIN must be 4 digits` 彈窗 |

priority 取自 `data/priority_final.tsv`，**不得重判**（R-VC11／R-VC13／R-VC14 已定案）。

---

## 三、本 feature 特有之撰寫約束

### 3.1 `specification_reference`（R-VC4）

逐字取 037 `HMI Source ID` 欄原值，**不構造**。形態：

```
SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_R1_SR24_Post_2A_(December_27_2023)_4.1
```

一個章節號一行、前綴逐行重述、禁用 `,`／`、`／`;` 串接（IN §10.7）。
資料件見 `data/recon_leaf_to_section.tsv`（145/145 逐字相符）。

### 3.2 `test_item` 兩段式（R-S4）——本輪之最大風險

- **上半** = 需求／規格原句 verbatim，token ≤ 50。
  取材依 **A-VC10**：`Title` 與 `Description` 二欄皆為 037 正式欄位，
  須**同時檢視**。僅取 Description 會漏 Title 所載之條件；
  僅取 Title 會失去規格原句。擇一為 verbatim 上半時，
  另一欄之獨有條件若為本 TC 之驗證標的，須確認其未被丟失。
- **下半** = 括號獨立成行 `(...)`，為 sibling 區分 token。

**同 section 之 sibling 尤須注意**（下半不得逐字相同）：

| section | sibling | 下半須區分之點 |
|---|---|---|
| 4.1 | `026-01` / `026-02` / `026-03` | 三者為同一流程之三個階段：說明彈窗 / PIN 請求彈窗 / 兩次輸入 |
| 5.1 | `028-01` / `028-02` | 前者為**單次錯誤之回饋**，後者為**次數上限之不存在** |
| 7.1 | `033-01` / `033-02` | 前者為**次數**門檻，後者為**位數**門檻 |

### 3.3 ⚠ 啟用不限次數 vs 停用三次鎖定 —— **不是矛盾**

`VC-028-02`（§5.1，**啟用**流程：不限錯誤次數）與
`VC-033-01`（§7.1，**停用**流程：連續錯誤達門檻即鎖定）
**分屬兩個流程，並不衝突**。

二筆之 `test_item` 括號下半**必須明載其流程**（activation / deactivation），
否則審閱者會將其讀為規格衝突。此為本 pilot 最易出錯之處。

### 3.4 §8.2.1 —— 不得擴張至 `VC-021`

Glove Box 之 UI 進入路徑為 Controls 頁籤內之 Glove Box 按鈕。
按下該鈕所開啟之 Privacy Lock 彈窗，其行為由 **`VC-021`（§3.6）**
擁有，且該筆受 DR-VC1 阻斷（彈窗 id 於規格原文即為字面 `PUXXXX`）。

- 到達 Glove Box 流程之操作，寫在 **Procedure 之 setup 步驟**，可行。
- **ER 不得驗證 `VC-021` 所擁有之行為**（該彈窗之 id、標題、按鈕組成）。
- 各 TC 之 `reasoning` 須載明此項委派（IN §8.2.1 之要求）。

### 3.5 `PENDING` 之寫法（`VC-033-01`）

```
PENDING: DR-VC8 Glove Box lockout threshold
```

**不得留空、不得填 NA、不得自行取 3 或 4**（A-VC14(a)）。
該 TC 之其餘欄位照常撰寫 —— 30 分鐘之鎖定時長規格有載，可用；
未定者僅「第幾次觸發」。

### 3.6 spec-sourced 之可用值

| 值 | 來源 | 可用 |
|---|---|---|
| PIN 長度 **4 位** | `VC-033-02` 之 `PIN must be 4 digits` | ✅ |
| 鎖定時長 **30 分鐘** | `VC-033-01` 二欄皆載 | ✅ |
| 鎖定觸發次數 | 二欄矛盾（A-VC14）| ❌ **PENDING** |
| 30 分鐘之計時起點 | 無載 | ❌ 不得寫入；已併 DR-VC8 附帶查詢 |
| 彈窗文字 | Title 逐字載 | ✅ 以 `"..."` 引（IN §11）|
| 彈窗 PU id | 規格未給 | ❌ 不得引用任何 PU 編號 |

`VC-028-02`／`VC-029` 之「N 次」**不得造具體數** —— 以「多次」或
`<multiple>` 表述，或設計為可重複之步驟（IN §8.4.1）。

### 3.7 格式（IN §11，逐筆自檢）

- `pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`
  之**每個 numbered item 皆無尾句號**
- UI 標籤一律 `"..."` 雙引號，禁 `[...]`、`'...'`、`<...>`
- Pre-Condition 為**狀態／環境**，非動作；
  **不得寫**「Glove Box is accessible」（feature under test as premise，§4.4）
- `input_test_data` 以 `NA` 為常態（R-1 v2）；PIN 值內聯至 Procedure
- Procedure ≥ 2 步；Final Step owns validation（§5.5）
- 禁 `observe`／`verify` 作主動詞；ER 禁 modal（`shall`／`will`／`should`）

---

## 四、收斂條件

pilot 收斂須**全部**滿足：

1. 12 筆 JSON 產出完整，10 個必要 key 齊備（IN §10.1）
2. IN §9 之十七項自檢逐筆通過，**逐項回報**（不得只報「全通過」）
3. `test_item` 括號下半 12 筆**兩兩不同**（機械驗證，非目視）
4. `specification_reference` 12 筆與 `data/recon_leaf_to_section.tsv`
   逐字相符（機械驗證）
5. `priority` 12 筆與 `data/priority_final.tsv` 逐字相符（機械驗證）
6. `Test Set` 12 筆皆為 `Glove Box`，無變體拼寫
7. 尾句號、引號規則之 lint 通過
8. `VC-033-01` 帶且僅帶一處 `PENDING: DR-VC8 …`
9. §3.3 之流程區分於 `028-02`／`033-01` 二筆之括號下半明確可見
10. §3.4 之 `VC-021` 委派於各 TC 之 `reasoning` 載明

**任一項不過即停並回報**，不自行修補後續。

---

## 五、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T56 | 抄錄 R-VC18 入 `RULINGS.md`（接 R-VC17 之後），byte-level diff | 1 |
| T57 | 依 §二／§三產出 12 筆 TC 之 JSON，置於 `generated/pilot_glovebox.json` | 1 |
| T58 | 依 §四逐項驗證，**十項逐項回報**；產出驗證腳本 `scripts/verify_pilot.py`（第 3–8 項可機械化者一律機械化）| 1 |
| T59 | 承下放包 09 —— T52（A-VC14 同型矛盾之全表掃描）、T53（DR-VC8 建檔）、T54（A-VC14）、T55（REV-13）如尚未完成則本輪完成 | 1 |

**不在本輪範圍**：寫回工作簿（Phase 6）、其餘 7 個 Test Set、
`VC-033-01` 之 boundary 拆分。

> DR-VC8 之**建檔**（T53）不待裁定，逕行；其**發送批次**歸屬待 Pei 確認
> （下放包 09 §二建議併同批 A）。二者不相依。

---

## 六、上繳包要求

1. T56–T59 逐項結果
2. R-VC18 之 byte-level diff
3. **12 筆 TC 全文**（JSON 原樣）
4. §四之十項逐項驗證結果，附 `verify_pilot.py` 原始輸出
5. IN §9 十七項自檢之逐筆逐項結果
6. T52 之全表掃描結果（同型矛盾清單）
7. 更新後之未結 DR（八筆）與 A（十筆）清單
8. 量測條件揭露（R-G8）：§四第 2 項與第 9、10 項含人工判斷成分者，
   須標明其主觀範圍
