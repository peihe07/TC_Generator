# 下放包 19 —— Vehicle Category：第 2 批收斂確認 ＋ 第 3 批勘查前置

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/19_batch3_survey.md`
- 前一包：`docs/handoff/18_batch2_tc.md`
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `18_`，無碰撞。
- **第 2 批 32 筆收斂確認。本包不授權生成任何 TC。**

---

## 一、上繳包 18 之覆核

**核可。19/0，第 2 批確認。** 四項具名：

1. **T99 之 34/34** —— 下放包 §2.3 預留之「第 3 種情形」（不通過時
   須看實例才能裁）本輪不需要。子串判準改採，token 比對移除。
2. **子串判準之附帶效益**（§1.3）：其輸出**報出取材來源分布**
   （`{'Description': 30}`／pilot `{'Title': 8, 'Description': 4}`）——
   **那正是下放包 §3.2 要求記於 `reasoning` 之「取自哪一欄」，
   現在由機器算出，不再只靠人寫。** 一個檢查項順帶消滅了一項人工義務。
3. **第 15 項「不採信 JSON 之宣告值」**（§4）—— `split_delta` 之實際值
   自 `tcs` 之 `leaf_id` 計數推得。宣告與實際分離，(a) 已實測其能抓到分歧。
4. **§5.3 之自行處理**：`VC-050` 之 500 ms **同時為觸發門檻與重複間隔**，
   意義不同。下放包未點名，生成時發現並分別表述。
   **這類「同一數值在一句內有二個角色」正是造值與誤讀之溫床**，處置正確。

### 1.1 一項已知限制，本輪不改

上繳包 §9 揭露：子串判準之**保護力隨來源長度遞減** ——
來源極短者（如 `Vehicle Tab Labels and Order.`），任何更短之上半皆為其子串。

**目前受影響者恰好全在 b 段**（`VC-007-01` 30 字元、
`VC-013-04` 24 字元），故不緊迫。**不現在改判準** ——
改動須對 66 筆回歸，成本高於當前收益。

**但 b 段解除時必然遇到。** 屆時之處置預先定下（不待彼時臨時判斷）：

```
b 段生成時，其 leaf 之來源字串長度 < 60 字元者，
其 test_item 上半須為**來源之完整句**（非任意子串），且須人工複核。
理由：該長度下子串判準幾近無保護，機器檢查不可依賴。
```

第 3 批之 `VC-025-01`（27 字元）**同屬此類**，見 §2.1。

---

## 二、第 3 批 `Controls` 之粗查（17 leaf）

> 分析層粗查，量自 037 完整儲存格值（**依 PLAYBOOK §7.2 修訂文，
> 未截斷**；各筆長度已列）。依 R-VC15，本節判讀不得沿用，須由執行層重測。

### 2.1 `VC-025-01` —— A-VC17 之第三筆，確認為 b 段候選

```
Description（27 字元）: C1.) Controls Button Table.
Title                 : Adopt the Controls Button Table as the authoritative
                        source for each Controls button's status semantics
```

與 `VC-007-01` 逐點同型：Description 為表格題名、Title 被改寫為
「Adopt X as the authoritative source」句式。

**處置：b 段保留**（R-VC22），阻斷於 DR-VC9(二)。
第 3 批因而為 **a 段 16 筆 ＋ b 段 1 筆**。

> 且其來源僅 27 字元 —— 即使日後確認為需求，亦適用 §1.1 之短來源處置。

### 2.2 ⚠ `VC-025-02` 之 Title **跨越了 037 自己的 leaf 邊界**

```
Description（-02）: … FamCam | … Forward Facing Camera | … Trlr Gdnc Camera | …
Title       （-02）: … the camera-family entries (Cargo, Surround, Rear View,
                     FamCam, Forward Facing, **Aux 1, Aux 2**, Trlr Gdnc) …
```

**`Aux Camera 1`／`Aux Camera 2` 在 `-03` 之 Description，不在 `-02`。**
037 作者改寫 Title 時，把 `-03` 之內容併入了 `-02` 之敘述。

**後果**：若 `-02` 之 `test_item` 上半取 **Title**，
該 TC 即涵蓋 `-03` 所擁有之行為 → **違反 IN §8.2.1**
（TC 不得擴張至 sibling Req 所擁有之行為），並產生重複追溯。

**拘束**：`VC-025-02` 之上半**必須取 `Description`**，不得取 Title。
其餘 `-03`／`-04`／`-05` 亦須逐筆檢查同型越界。

> **這是 A-VC10 之第四面。** 前三面為資訊量不對稱、數值矛盾（A-VC14）、
> 記法不對稱；**第四面是改寫跨越了 leaf 邊界**，其危害最大 ——
> 前三面影響單筆之正確性，第四面影響**批次之追溯結構**。
> A-VC10 之加註須增列此面。

### 2.3 `VC-019-02` —— 跨 leaf 之代名詞指涉

```
VC-019-01（96 字元）: Headrest fold will not be able to show status, the user
                      will simply be able to press the button.
VC-019-02（22 字元）: It will not highlight.
```

`-02` 為**完整句**（非第 1 批之小寫起首片段），
但其主詞 `It` 之先行詞在 `-01`。單獨作為上半，讀者不知 `It` 何指。

**形態與第 1 批之續行型不同，處置方向相同**：
上半取 SYS1 §3.4 之**完整脈絡**（二句或含先行詞之段），
括號下半載本 leaf 之驗證範圍（不高亮）。

勘查須先以 SYS1 確認 §3.4 之句構（R-VC7）。

### 2.4 `VC-014` 之 `(See table above)` —— 指涉存疑

```
Description: … include, but are not limited to (See table above): Headrest Fold, …
Title      : … per the Controls table
```

`VC-014` 在 **§3.1**，而 Controls Button Table 在 **§3.9** ——
**`above` 於章節序上不成立**。037 作者於 Title 逕改為
`per the Controls table`，但該表在其後方。

勘查須以 SYS1 確認 **§3.1 上方是否另有表**。
- 若有 → 該表為其標的，須確認素材在手
- 若無 → 指涉不明，同第 1 批 `VC-011` 之處置（PENDING ＋ 併 DR）

**不自行認定**（§8.4.1）。

### 2.5 `VC-025-05` 之二處外部委派

```
Cabrio       | Opens Cabrio pop up (see Cabrio requirements)
Memory Seats | Opens Memory Seats second level screen (see Virtual Memory Seats L&F)
```

- **Cabrio requirements** = 章 8／9，**037 零涵蓋**（R-VC3 表 B 之 17 節）
- **Virtual Memory Seats L&F** = 外部規格，**不在素材清單**（R-VC10 六項）

依 IN §8.4.2，本 TC 之範圍**僅及於「按下該鈕後有對應之彈窗／次層畫面開啟」**，
**不得驗其內容**（彈窗之組成、次層畫面之項目皆屬他規格）。
`reasoning` 須載明二處委派。

> 注意：Cabrio 之委派標的**在本 feature 內但未涵蓋** ——
> 與 Memory Seats（在他 feature）性質不同。二者皆不測其內容，
> 但前者須於表 B 之脈絡下理解（章 8／9 待 DR-VC3）。

### 2.6 其餘二項

- **`VC-021`**：DR-VC1 阻斷（`PUXXXX` 為規格原文之字面）。
  **地位無疑，屬 a 段**，帶 `PENDING: DR-VC1 …`。
  其 `Refer to Glove Box Lock section for behavior` 為委派 ——
  **不得測 Glove Box 之行為**（pilot 已擁有，§8.2.1）。
- **`VC-025-04`** 之三處括號項（`(Pass Screen Screen Off)`／
  `(Power Side Step)`／`(Exhaust Sound)`）：括號之含義未明
  （疑為條件性項目或選配）。勘查回報 SYS1 是否有其說明；
  無則逐字保留括號（R-VC23），**不自行詮釋其含義**。

### 2.7 表格扁平化 —— 同第 1 批，處置沿用

`VC-025-02`~`-05` 為 Controls Button Table 之四段扁平化，
形態同第 1 批之 `VC-007-02`~`-05`。沿用其處置：
逐字引用整格、不自行拆分黏連、值之權威為 SYS1 §3.9 之原表。

---

## 三、第 3 批勘查任務（T105）

| # | 勘查項 |
|---|---|
| a | 17 leaf 之 `Title`／`Description` 逐字全文（**完整值，不截斷**）|
| b | §二之七項風險逐項覆核，確認或推翻 |
| c | **Title 越界之全批檢查** —— 承 §2.2，逐筆比對 Title 是否含 Description 所無而屬他 leaf 之內容。**此項為本批最重要之勘查** |
| d | SYS1 對照（R-VC7）：§3.1 上方是否有表（§2.4）、§3.4 之句構（§2.3）、§3.9 原表、`VC-025-04` 括號項之說明 |
| e | 素材可用性：逐筆列其所需素材與是否在手 |
| f | 來源記法全批掃描 |
| g | 拆分候選 —— 逐筆施 §8.3 壓力測試 |
| h | TC 數預估；標出 a 段／b 段、需 `PENDING` 者 |

**勘查後停，回報，不生成。**

---

## 四、其他任務

| # | 任務 |
|---|---|
| T106 | A-VC10 之加註**增列第四面**（改寫跨越 leaf 邊界，§2.2），並註明其危害異於前三面（影響追溯結構而非單筆正確性）|
| T107 | §1.1 之短來源處置（< 60 字元須取完整句 ＋ 人工複核）記入 profile 或 PLAYBOOK，擇一並說明理由。**本輪不改判準**，僅記其適用時機 |

---

## 五、上繳包要求

1. T105 之勘查表（a–h 八項），**(c) 之全批 Title 越界檢查為重點**
2. T106／T107 逐項結果
3. 量測條件揭露（R-G8）：(c) 之比對方法與其偽陰性
   （Title 之改寫若為同義而非逐字挪用，字串比對看不到）

---

> 九筆 DR 全未結。**DR-VC9(二) 現已阻斷二個批次之 b 段**
> （第 1 批 2 筆、第 3 批 1 筆）。
> DR-VC1 阻斷 `VC-021`（第 3 批 a 段，帶 PENDING 可生成）。
> DR-VC3 阻斷第 6／7 批之邊界重審。
>
> **進度**：117 leaf 中 64 筆已收斂，TC 累計 66 筆。
