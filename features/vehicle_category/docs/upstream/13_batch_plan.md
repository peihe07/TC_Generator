# 上繳包 13 —— Vehicle Category：pilot 放行後之常數表與批次檢查（T73–T77）

- 日期：2026-08-26
- 對應下放：`docs/handoff/13_batch_plan.md`
  （SHA256 `3f01ec5c65280bf9272abed41fd2dc6170830af797df41b6cd3c711c73b1fb78`，189 行）
- **結論：T73–T77 五項全數完成。`verify_batch` 17 checked / 0 failed。**
- **未生成任何新批次**（下放包 §五末句：待裁 §四之順序後另行下放）。
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T73 | profile §5 常數表 | ✅ `ENTER_CONTROLS_TAB` ＋ 擴充規則三項 |
| T74 | 第 13、14 項 | ✅ 新增，**皆實測會 FAIL** |
| T75 | 更名 | ✅ `verify_pilot.py` → **`verify_batch.py`** |
| T76 | `PLAYBOOK.md` §7 二則慣例 | ✅ 記為建議，非條文 |
| T77 | pilot 標記已收斂 | ✅ `status: converged` ＋ 修改範圍限定 |

---

## 1. T73 —— profile §5

profile 由 112 行增為 154 行。新增 §5 三小節：

### §5.1 常數

```
ENTER_CONTROLS_TAB:
  Open the Vehicle Category screen and select the "Controls" tab
```

首次使用：pilot 12 筆之 Procedure 首步（下放包 12 T67 之導覽移入）。

### §5.2 擴充規則（逐字採下放包 §三）

(a) 新增常數須**同時**更新 profile 與 `verify_batch.py` 之常數表，二處不得分歧。
(b) 新片語之加入須先確認既有片語不敷用 —— **不得為措辭偏好而增設近義常數**。
(c) 常數之措辭**一經登記即凍結**；修改須經裁定並**回溯既有 TC**。

### §5.3 —— 我對 (a) 多做了一步

(a) 要求「二處不得分歧」。若二處各自維護，那個「不得」只是規定，
沒有承載者。故 **`verify_batch.py` 之常數自 profile §5.1 之 code fence
解析取得，非硬編於腳本** ——

> **二處不得分歧由解析保證，不靠人記得。**

已於 profile §5.3 記明，並附其偽陰性：本項只驗**首步**是否為表中常數；
若某批把導覽寫在第二步、或把常數拆成兩步，看不到。

---

## 2. T74 —— 第 13、14 項

### 2.1 第 13 項：Test Set 與 framework 相符

名稱**自 `framework.md` §2 之表解析**（正則取 `| n | \`名稱\` |`），
**不硬編** —— 硬編會使本項只驗到腳本自己。

```
 13  該批 Test Set 全筆一致且與 framework.md §2 逐字相符          PASS
     批內 test_set=['Glove Box']；framework §2 之 8 組=8 個；相符=True
```

### 2.2 第 14 項：setup 片語取自常數表

```
 14  本批 setup 片語（Procedure 首步）皆取自 profile §5 常數表      PASS
     profile 常數 1 條；批內相異首步 1 種；不在表中 無
```

### 2.3 二項之實測 FAIL（依 §一之標準作法）

注入二處反例：`026-01` 之 `test_set` 改為 `GloveBox`（變體拼寫）；
`026-02` 之首步把 `tab` 改為 `Tab`（一個字母之大小寫）。

```
 13  該批 Test Set 全筆一致且與 framework.md §2 逐字相符          **FAIL**
     批內 test_set=['Glove Box', 'GloveBox']；相符=False
 14  本批 setup 片語（Procedure 首步）皆取自 profile §5 常數表      **FAIL**
     不在表中 ['Open the Vehicle Category screen and select the "Controls" Tab']
exit: 1
```

隨後還原，複跑回到 17/0。

> **第 14 項之反例只差一個字母的大小寫，仍被抓到。**
> 那正是 IN §5.3 所列之 variant 類（case／hyphenation／spacing／wording）
> 之最小形態 —— 也是最容易在七批之間悄悄長出來的那種。

---

## 3. T75 —— 更名為 `verify_batch.py`

**更名，不維持原名。** 理由：第 13、14 項加入後其已非 pilot 專用 ——
二者皆為**每批**之收斂條件（下放包 §4.4）。名實相符優於相容性。

配套二項：

1. 檔頭 docstring 記其更名與理由，使日後讀腳本者不必翻上繳包。
2. 待驗檔改由 `BATCH` 常數指定（預設仍為 `pilot_glovebox.json`），
   使其可指向後續批次而不需改動檢查邏輯。

> **更名以 `mv` 執行，非 `git mv`** —— 後者會 stage，屬 git 操作。
> git 視之為 delete + add，由 Pei 之 commit 承接。

---

## 4. T76 —— `PLAYBOOK.md` §7 二則操作慣例

**記為建議，非條文**（下放包 §五 T76 之明文）。二則之由來皆為實際發生過的錯：

### 7.1 新增檢查項時，以反向輸入實測其會 FAIL

由來：上繳包 11 §5.3 之自我限定。**光寫反例仍是自己說了算。**
實例四項（第 11／12／13／14）皆先注入反例確認 FAIL、再還原確認 PASS。

### 7.2 複核腳本之掃描標的不得為顯示用之截斷字串

由來：下放包 13 §二之第六件 —— 分析層對截斷至 74 字元的顯示字串跑正則，
`record` 落在截斷之後，誤報 `VC-028-02` 無檢查動詞。

**我把這一件記進 PLAYBOOK 時保留了它的來源是分析層。**
其意義不在誰出錯，在於：上繳包 11 §9 之自我限定不限於執行層，
而**複核者的錯更難被發現，因為複核之後沒有下一道**。

---

## 5. T77 —— pilot 標記已收斂

`generated/pilot_glovebox.json` 頂層新增二鍵（置於 `ruling` 之後）：

```json
"status": "converged",
"status_note": "pilot 收斂並放行（下放包 13 §一，Pei 2026-08-26）。收斂條件實跑 17 項全過（`scripts/verify_batch.py`）。**本檔其後不再修改**，除非 DR-VC8 回覆觸發 Revise —— 屆時之異動限於 `VC-033-01`（門檻值與 R-VC18 之 boundary 拆分），其餘 11 筆不動。"
```

**修改範圍已寫死在檔內** —— 不只寫「不再修改」，而是寫明
**唯一可能之異動是哪一筆、因什麼觸發、其餘幾筆不動**。
下放包 §五 T77 允許形式由執行層定，取此形式之理由：
「不再修改」四字若無範圍，日後任何人都可以主張自己那次是例外。

---

## 6. 六件檢查器錯誤之現況

| 件 | 層 | 形態 | 誰抓到 | 現況 |
|---|---|---|---|---|
| 1 | 執行層 | T52 類別切分，漏抓標的自身 | 我 | 已修，記於 A-VC14 加註 |
| 2 | 執行層 | modal 未排除引號內 `must` | 我 | 已修 |
| 3 | 執行層 | ER 快掃未排除行首序號 | 我 | 已修（未影響結論）|
| 4 | 執行層 | §4.4 只驗一類禁項 → 漏檢 12/12 | **分析層** | 已修，A-VC16 |
| 5 | 執行層 | 隱性依賴他筆之值 → 漏檢 | **分析層** | 已修，A-VC16 |
| 6 | **分析層** | 判準正確，輸入被截斷 | 分析層自陳 | 記入 PLAYBOOK §7.2 |

前五件之處置皆為**修判準**；第六件之處置為**修慣例** ——
因其判準沒錯，錯在套用。二者不同類，故一入檢查器、一入 PLAYBOOK。

---

## 7. §四之批次順序 —— 未執行，僅回報一項覆核

**未生成任何新批次。** 下放包 §五明文待裁 §四之順序。

惟 §4.2 之三項 DR 阻斷標記為可覆核之主張，順帶自既有資料件驗之
（**不構成任何批次產出**）：

| 序 | Test Set | leaf（實測）| DR 阻斷（實測）|
|---|---|---|---|
| 1 | `Category Structure` | 24 | 無 |
| 2 | `Settings List` | 30 | 無 —— 惟含 `VC-048-02`（FROP=Audio Management，DR-VC5 之 1 筆）|
| 3 | `Controls` | 17 | DR-VC1 —— `VC-021`（§3.6），**1 筆** |
| 4 | `Settings Behavior` | 15 | 無 —— 含 P0 二筆（`035-03`／`036-02`）＋ R-VC14 揭露一筆（`036-01`）|
| 5 | `Ignition Availability` | 16 | DR-VC5 —— 章 13 之 PM 12 筆（117 leaf 母體）|
| 6 | `Brake Service` | 2 | DR-VC3 |
| 7 | `Cabrio Widget` | 1 | DR-VC3 |

leaf 數與 `data/test_set_map.tsv` 逐組相符（合計 24+30+17+15+16+2+1 = 105，
＋ pilot 12 = **117 leaf 母體**）。

⚠ **一處與 §4.2 表不同**：§4.2 於 #2 `Settings List` 標「DR 阻斷：無」，
但 **DR-VC5（FROP 跨域 17 列）之 `Audio Management` 一列
（`VC-048-02`，§12.3.2）落在該組**（framework §3.6 已載）。
其於 145 列母體為 1 列，於 117 leaf 母體亦為 1 筆。

**不影響排序建議** —— DR-VC5 依 R-VC3 已裁全取、不阻斷生成；
但 §4.1 第 1 項之排序判準為「DR 阻斷程度」，#2 之標記宜改為
「DR-VC5（1 筆，不阻斷）」以與 #5 之標記一致。**僅回報，未改。**

---

## 8. 待你裁

1. **批次順序**（§4.2 七項）—— 另請看 §7 之一處標記更正。
2. **批次規模**（7 批，一組一批）。
3. 同批 A（五項）與 DR-VC3 之發送（Tier 3）。
   **DR-VC3 現已直接影響批次順序**（#6／#7 置末之理由）。

---

## 9. 量測條件揭露（R-G8）

- **第 13 項**之名稱自 `framework.md` 解析，正則為
  `^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|`。**偽陰性**：若 framework §2 之表
  改動欄序或改用非 code-span 標記名稱，解析會取不到而使
  `fw_names` 為空 —— 屆時本項會因 `batch_ts <= set()` 為 False 而 FAIL，
  **失敗方向為安全側**（不會誤放）。
- **第 14 項**之常數自 profile §5.1 之 code fence 解析。
  **偽陰性同上為安全側**：解析不到常數時 `bool(consts)` 為 False → FAIL。
  另一類偽陰性見 profile §5.3：只驗首步，導覽寫在第二步或拆成兩步則看不到。
- **§7 之覆核**取自 `data/test_set_map.tsv`、`data/priority_final.tsv` 與
  `framework.md` §3.6，未重讀 037。三檔之一致性由 `verify_partn.py`
  之 5/5 PASS 背書（上繳包 07 §4）。
