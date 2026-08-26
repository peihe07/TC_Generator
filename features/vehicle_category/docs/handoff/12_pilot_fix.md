# 下放包 12 —— Vehicle Category：pilot 複核結果（不放行，二項退回）

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/12_pilot_fix.md`
- 前一包：`docs/handoff/11_pilot_resume.md`
- 對應之上繳包：`docs/upstream/11_pilot_resume.md` §8 待裁三項
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `11_`，無碰撞。
- **結論：pilot 不放行。** 二項退回，皆為 `verify_pilot` 未覆蓋之形態。

---

## 一、§四.1 之分析層複核：**通過**

`-028-02` 與 `-033-01` 之流程區分，逐字讀過括號下半與 `reasoning`：

| 筆 | 括號下半 |
|---|---|
| `-028-02` | `(Activation error -- absence of an attempt ceiling, repeated across multiple mismatches)` |
| `-033-01` | `(Deactivation error -- attempt-count threshold and the 30 minute lockout, threshold value pending)` |

**通過，且優於機械檢查所驗者。** 二項具名：

1. 流程詞在**首詞位置**（`Activation error` / `Deactivation error`），
   非夾在句中之字樣 —— 讀者掃過即見，不需讀完整句。
   機械檢查只驗「含 activation／deactivation 字樣」，驗不到這一層。
2. `reasoning` 之 ⚠ 段為**雙向互指** —— 讀任一筆皆會看到另一筆之存在
   與「不矛盾」之理由。單向會使先讀到的那筆漏掉該資訊。

R-VC20 之四項揭露亦逐項到位，**其中第 (2) 項比我下裁時所知更精確**：
我在 A-VC14 記為「數值 3 vs 4」，執行層查明**二欄之數字同為 `three`，
差別在比較器**（`After three` vs `more than three`）。
該修正併入 A-VC14 之加註（不改原文，R-TM13）。

---

## 二、退回第一項：`pre_conditions` 12/12 逐字命中 §4.4 禁項

### 2.1 事實

12 筆之 `pre_conditions` 第 1 條全為：

```
1. The head unit is powered on and the Vehicle Category screen is displayed
   with the "Controls" tab active
```

IN §4.4 之 **Forbidden 首例逐字為 `system defaults (HU is powered on.)`**。
`The head unit is powered on` 即該例，**12/12 命中**。

該條後半（`the Vehicle Category screen is displayed with the "Controls"
tab active`）另觸 §4.4 之 **`step-controlled state`** ——
導覽至某畫面／頁籤是步驟可達成之狀態，屬 Procedure，非 Pre-Condition。
其自檢即為 §4.4 之「requires *do / check / confirm* → NOT a Pre-Condition」：
到達該畫面需要 *do*。

**`pre_conditions` 第 2 條合法**（`The Glove Box feature is not activated` /
`is activated with a known 4-digit PIN`）—— 屬 §4.4 允許之
**feature initial state**，且 `4-digit` 為 spec-sourced（`VC-033-02`）。

### 2.2 為何 §9 第 3 項判 PASS 而未抓到

上繳包 10 §4 第 3 項之判讀依據為：

> 人工：二式（未啟用／已啟用且 PIN 已知）＋ 進入畫面；**未寫**「Glove Box is accessible」

該判讀**只檢查了 §4.4 三類禁項中的一類**（feature under test as premise），
未檢查 `system defaults` 與 `step-controlled state`。

### 2.3 處置

12 筆之 `pre_conditions` 改為**只留 feature initial state**：

```
1. The Glove Box feature is not activated          （七筆：026-01/02/03、027、028-01/02、029）
1. The Glove Box feature is activated with a known 4-digit PIN   （五筆：030、031、032、033-01/02）
```

原第 1 條之後半（導覽至 Controls）**移入 Procedure 之首步**。
其形態由執行層依 §5.2 A 類（≤ 12 字、動作＋標的）決定，
**不得因此使既有首步之驗證語意改變**。

> §8.5 之決策測試在此成立：`head unit is powered on` 是
> 「測試得以執行所需之隱含環境穩定前提」，非本 TC 直接驗證之觸發條件 →
> **drop**。

---

## 三、退回第二項：`VC-028-02` 之 `comparable attempt ceiling`

### 3.1 事實

該筆 Procedure 第 3 步：

```
3. Continue the mismatch cycle beyond the point at which a comparable attempt
   ceiling would apply, and record whether the flow stays available
```

`a comparable attempt ceiling` 之最自然讀法為**指向 `-033-01` 之停用門檻**。
問題三層，由輕至重：

1. 該門檻正由 DR-VC8 爭議中 —— 本步驟因而**間接依賴一個未定值**，
   而該筆並未帶 `PENDING`（收斂條件第 8 項驗過「他筆帶 PENDING 無」，
   此處恰為其反面：該依賴是隱性的，機械檢查看不到）。
2. **規格從未述及啟用流程有一個「可比較的門檻」。**
   該參照是 TC 作者引入之概念，觸 §8.4.1 —— 不造具體數值，
   卻造了一個來源未述之**參照對象**。
3. 二筆之獨立性受損：`-028-02` 之可執行性繫於 `-033-01` 之值，
   而下放包 10 §3.3 之全部工夫正是要讓二者**各自可讀、不被讀成關聯**。

### 3.2 根本問題：否定性存在命題之可測性

`-028-02` 之標的為「上限不存在」。**否定性存在命題無法以有限次數證明**，
測試至多做到「重複 N 次仍可用」。

**N 是測試設計參數，不是規格值。** 二者須明確分開：

- 規格未給 N → 不得寫成規格所載之門檻，亦不得參照他筆之門檻
- 測試需要一個具體重複次數才可執行 → 由測試設計決定，
  **並於 `reasoning` 明標其為測試設計選擇**

**此非 §8.4.1 之造值** —— §8.4.1 禁的是「發明來源未述之規格值」；
測試執行參數（重複幾次、等待幾秒之測試側取值）屬測試設計，
其正當性來自被明確標示為測試設計，而非被偽裝成規格值。

### 3.3 處置

第 3 步改寫，二項要求：

(a) **移除門檻參照**。以純重複表述，其重複次數若須具體化，
    由測試設計給定並在 `reasoning` 標明
    「N 為測試設計選擇，規格未給上限值（§8.4.1 之區分見下放包 12 §3.2）」。
(b) ER 第 3 項之 `no attempt ceiling applied` **保留** ——
    該句為行為表述，未引入門檻值，合規。

---

## 四、檢查器之第四件 —— 方向與前三件相反

上繳包 11 §5.3 記三輪三支檢查器各出一錯，皆為**判準寫得比標的粗**。
本輪之二項退回為**第四、第五件**，但**方向相反**：

| 件 | 形態 | 後果 |
|---|---|---|
| 1–3（T52 初版／modal／ER 序號） | 判準**太嚴** → 誤報 | 停下來看一眼，虛驚 |
| **4（§4.4 只驗一類禁項）** | 判準**太鬆** → **漏檢** | **12 筆帶錯往下走** |
| **5（隱性依賴他筆之值）** | 判準**看不到** | 同上 |

**太嚴會浪費時間，太鬆會讓錯誤通過。** 前者自己會現形（FAIL 逼人去看），
後者只有靠外部複核 —— 本次即是。

### 4.1 配套

`verify_pilot.py` 之 §4.4 檢查（第 3 項）**須機械化為三類齊備**：

| 類 | 應 FAIL 之輸入（§四.2 之反例要求） |
|---|---|
| system defaults | `The head unit is powered on`／`HU is booted`／`Ignition is ON`（若非該 TC 直接驗證之觸發條件）|
| feature under test as premise | `Glove Box is accessible`／`Glove Box feature is available` |
| step-controlled state | `The "Controls" tab is active`／`The PIN popup is displayed`／`Device is not connected` |

**第三類最難機械化** —— 「這個狀態是否步驟可達成」需語意判斷。
其可機械化之近似為：**該 `pre_condition` 之文字若與任一 procedure 步驟之
標的重疊，即列為候選並人工判讀**。
如實作，須於上繳包載明其偽陰性（不重疊但仍為 step-controlled 者）。

---

## 五、pilot 之放行條件（承下放包 10 §四）

原十項不變，另加二項：

11. `pre_conditions` 12 筆皆無 §4.4 之三類禁項（機械，三類齊備）
12. 12 筆之任一欄位皆不含**對他筆之值的隱性依賴** ——
    即不得出現「與某筆相當之門檻／次數／時間」之參照。
    可機械化之近似：掃 `comparable`／`corresponding`／`similar`／
    `equivalent` ＋ 門檻類名詞；命中即人工判讀

**十二項全過始得放行。** 放行後始議 Phase 4 之全量批次。

---

## 六、執行層任務

| # | 任務 |
|---|---|
| T67 | 依 §2.3 修 12 筆之 `pre_conditions`；導覽步移入 Procedure 首步。回報修改前後對照（12 筆逐筆）|
| T68 | 依 §3.3 修 `VC-028-02` 之 Procedure 第 3 步與其 `reasoning` |
| T69 | 依 §四.1 擴充 `verify_pilot.py` 之第 3 項為三類齊備；依 §五 新增第 11、12 項。每項載明反例 |
| T70 | 重跑 `verify_pilot.py`，**十二項全過**。任一不過即停並回報 |
| T71 | A-VC14 加註（不改原文）：分歧之精確形態為「二欄數字同為 `three`，差別在比較器」，依上繳包 11 §4.2 之查明 |
| T72 | `ANOMALIES.md` 記本輪二項退回為 §9 判讀之漏檢實例（**不立新條** —— §4.4 已明文，缺的是檢查覆蓋，非規則）|

**不在本輪範圍**：寫回工作簿、其餘 7 個 Test Set、
`VC-033-01` 之 boundary 拆分。

---

## 七、上繳包要求

1. T67–T72 逐項結果
2. 12 筆 `pre_conditions` 之修改前後對照
3. `VC-028-02` 第 3 步與 `reasoning` 之修改前後對照
4. `verify_pilot.py` 十二項全輸出 ＋ 新增三項之反例
5. 量測條件揭露（R-G8）：§四.1 第三類之偽陰性

---

> **本輪之意義**：12 筆抓到二個形態，若第一次遇到是在 117 筆之全量批次，
> 代價是 117 筆返工。下放包 08 §4.2 選 `Glove Box` 為 pilot 之四項理由，
> 於此第二次兌現（第一次為 profile 缺口，上繳包 10 §5.5）。

> 同批 A（五項）與 DR-VC3 仍待發送（Tier 3）。
