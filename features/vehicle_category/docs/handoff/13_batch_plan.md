# 下放包 13 —— Vehicle Category：pilot 放行 ＋ setup 常數 ＋ 全量批次順序

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/13_batch_plan.md`
- 前一包：`docs/handoff/12_pilot_fix.md`
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `12_`，無碰撞。
- **裁定：pilot 放行。Phase 4 進入全量批次規劃。**

---

## 一、複核結果：放行

分析層對修正後之 `generated/pilot_glovebox.json` **獨立重測**
（未採信上繳包 12 之自評）：

| 項 | 實測 | 判 |
|---|---|---|
| `pre_conditions` 條數與內容 | 12/12 各一條，全為 feature initial state | ✅ |
| §4.4 三類禁項詞掃 | 命中 0 | ✅ |
| Procedure ↔ ER 1:1 | 12/12 相符（3/3 八筆、4/4 四筆）| ✅ |
| Final Step 含檢查動詞 | 12/12（見 §二之更正）| ✅ |
| `VC-028-02` 之門檻參照 | 已移除；N=10 標為測試設計參數；ER 第 4 項為測試條件描述而非規格門檻 | ✅ |
| 首步逐字一致 | ×12 完全相同 | ✅（另見 §三）|

**pilot 收斂，放行。** 下放包 10 §四末句之前置解除，
Phase 4 得議全量批次。

上繳包 12 之二項具名採認：

1. **§4.2 之「把反例真的塞進 JSON 跑一次」超出要求。**
   我只要求「載明反例」，你們做的是實測其會 FAIL。
   **光寫反例仍是自己說了算，跑一次才知道判準接得住。**
   此法納為往後新增檢查項之標準作法（§五 T76）。
2. **§5.2 之自我診斷準確**：「把一個窄的檢查，用一個寬的詞報出去」——
   與 REV-13 同型。A-VC16 之登記與「不立新條」之判斷皆正確。

---

## 二、我的檢查器也出了一錯 —— 第六件

複核 Final Step 時，我的正則對 `VC-028-02` 報「⚠ 無檢查動詞」。

**誤報。** 該筆末步逐字為：

```
4. Repeat the mismatch cycle until ten consecutive incorrect entries have been
   made, and record whether the keypad popup is still reachable
```

`record` 在句末。**我對一個截斷至 74 字元的顯示字串跑正則**，
而 `record` 落在截斷之後。判準本身沒錯，我把它套在錯的輸入上。

計入既有清單：

| 件 | 層 | 形態 |
|---|---|---|
| 1–3 | 執行層 | 判準太嚴 → 誤報 |
| 4–5 | 執行層 | 判準太鬆 → 漏檢 |
| **6** | **分析層** | **判準正確，輸入被截斷** |

**這一件證明上繳包 11 §9 之自我限定不限於執行層。**
「寫檢查器的人帶著自己的盲點」對複核者同樣成立 ——
而複核者的錯更難被發現，因為複核之後沒有下一道。

配套：**分析層之複核腳本，其掃描標的不得為顯示用之截斷字串**。
記於 §五 T76 之同一處，不立條文（此為操作瑕疵，非制度缺口）。

---

## 三、`§5.3` 之標準 setup 片語 —— 現在該建常數表

12 筆之 Procedure 首步**逐字完全相同**：

```
1. Open the Vehicle Category screen and select the "Controls" tab
```

逐字重用是對的（IN §5.3 所要）。但目前它**只存在於 12 筆 JSON 裡**，
未進任何常數表。全量批次時 `Category Structure`／`Controls`／
`Settings List` 等組亦需導覽首步，**屆時各自書寫即產生變體**
（IN §5.3 所禁之「case, hyphenation, spacing, and wording variants
spread across TCs」）。

**pilot 是建表的最好時機** —— 現在只有一個片語，且已驗證可用。

處置：於 **VC profile 新增 §5「標準 setup 片語」**，
登記首個常數並載明其擴充規則：

```
ENTER_CONTROLS_TAB:
  Open the Vehicle Category screen and select the "Controls" tab

擴充規則：
(a) 新增常數時，須同時更新本節與 `verify_*.py` 之常數表，二處不得分歧。
(b) 新片語之加入須先確認既有片語不敷用 —— 不得為措辭偏好而增設近義常數。
(c) 常數之措辭一經登記即凍結；其修改須經裁定並回溯既有 TC。
```

> 選 profile 而非 `framework.md`：片語屬格式規範（同引號例外），
> 而 framework 記的是 Layer 1/2/3 之切分。

---

## 四、全量批次順序 —— 提案，待裁

剩餘 **105 leaf**（117 − 12）／**7 個 Test Set**。

### 4.1 排序之判準（三項，依序）

1. **DR 阻斷程度** —— 受阻者後置，使其有時間等回覆
2. **格式形態之新舊** —— 已驗形態者先行，新形態者在基線穩固後
3. **規模** —— 同等條件下先小後大，使問題早現形

### 4.2 提案順序

| 序 | Test Set | leaf | DR 阻斷 | 新形態 |
|---|---|---|---|---|
| 1 | `Category Structure` | 24 | 無 | 對照表類（P3 佔 16）—— 形態單純 |
| 2 | `Settings List` | 30 | 無 | 旋鈕／長按速率／指示標退回 —— 互動類 |
| 3 | `Controls` | 17 | **DR-VC1**（僅 `VC-021` 一筆）| 按鍵狀態對照 |
| 4 | `Settings Behavior` | 15 | 無 | **3 個 P0 ＋ R-VC14 分歧揭露** |
| 5 | `Ignition Availability` | 16 | **DR-VC5**（FROP 跨域全 16 筆）| 電源狀態機 |
| 6 | `Brake Service` | 2 | **DR-VC3**（邊界待重審）| — |
| 7 | `Cabrio Widget` | 1 | **DR-VC3**（同上）| — |

**#4 置於第 4 位而非更前**：其含本 feature 全部 5 個 P0 中之 2 個
（`035-03`／`036-02`）與 R-VC14 之分歧揭露義務（`036-01`）。
下放包 08 §4.4 已載其理由 —— **P0 與分歧揭露宜在格式基線穩定後再做**。
pilot 雖已收斂，但第 1、2 批將首次驗證「非 Glove Box 形態」之格式；
待其穩定，#4 之風險最低。

**#6／#7 置末**：R-VC16(c) 明文其邊界待 DR-VC3 重審，
且屆時章 8／9 之 Cabrio 本體應另立 `Cabrio Rooftop`。
**在重審前生成，其結論可能被推翻。**

### 4.3 批次規模

pilot 為 12 筆。建議全量批次以 **20–30 筆為上限**：

- `Category Structure`（24）、`Settings List`（30）→ **各自一批**
- 其餘各組 ≤ 17，各自一批

即 **7 批**，不再細分。理由：Test Set 是 framework 所定之能力群，
跨組合批會使 `Test Set` 欄在同一批內分歧，失去批次作為審閱單位之意義。

### 4.4 每批之收斂條件

沿用 pilot 之十二項（實跑 15 項），另加二項：

13. 該批之 `Test Set` 全筆一致，且與 `framework.md` §2 逐字相符
14. 該批所用之 setup 片語皆取自 profile §5 之常數表（§三）

---

## 五、執行層任務

| # | 任務 |
|---|---|
| T73 | VC profile 新增 §5 標準 setup 片語（§三），登記 `ENTER_CONTROLS_TAB` 與擴充規則三項 |
| T74 | `verify_pilot.py` 新增第 13、14 項（§4.4），並依 §4.2 之作法**實測其會 FAIL** |
| T75 | `verify_pilot.py` 更名為 `verify_batch.py`（其已非 pilot 專用），或另行說明為何維持原名 |
| T76 | `PLAYBOOK.md` 記二則操作慣例（**建議，非條文**）：<br>(a) 新增檢查項時，以反向輸入實測其會 FAIL，不只載明反例<br>(b) 複核腳本之掃描標的不得為顯示用之截斷字串 |
| T77 | pilot 之 12 筆 JSON 標記為**已收斂**（`generated/pilot_glovebox.json` 加 `status` 或另存 `.final`，形式由執行層定），其後不再修改，除非 DR-VC8 回覆觸發 Revise |

**待 Pei 裁 §四之順序後**，另行下放第 1 批。本包不授權任何新批次之生成。

---

## 六、上繳包要求

1. T73–T77 逐項結果
2. profile §5 全文
3. 第 13、14 項之實測 FAIL 輸出
4. 量測條件揭露（R-G8）

---

## 七、Pei 之最短回覆格式

```
pilot 放行: 已裁（本包）
批次順序: 准 / 改（列出）
批次規模: 准（7 批，一組一批）/ 改
```

> 同批 A（五項）與 DR-VC3 仍待發送（Tier 3）。
> **DR-VC3 現已直接影響批次順序**（#6／#7 置末之理由），
> 其回覆愈早，末二批愈早能定案。
