# 下放包 30 —— batch 3 之限定授權、術語同一性之詢問與待回覆判定之登記簿

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/30_batch3.md`
- 前一包：[29_batch2_review.md](29_batch2_review.md) ＋ [29a](29a_dr_sent.md) ＋ [29b](29b_ch9_unfreeze.md)

---

## 一、29b 之覆核 —— **停止條件 10 為正確觸發，且你停對了**

執行層於發現牴觸後**停在裁定前**，並明說
「**解法我看見了…須 R-PMH87 型授權，本包無之**」。

**這是正確的**：`PM1)` 之 stay-awake 正是 `-018-01`～`-05` 之標的，
**照常產出等於以某一讀法作成 TC 而未經裁定**。

**另一項記明**：其指出停止條件 11 為「**不適用**，非未觸發」——
TC 尚未存在，判別法無可套用之對象。**二者不同，其分辨正確。**

---

## 二、牴觸 —— 分析層獨立複驗，**成立**

**量測條件**：`pm.txt` p9 之 `PM1)` 段；Excel `State Matrix` 第 31、32 列
（`Key-off` 區塊）及其欄軸（第 20–23 列）。

| | 逐字 |
|---|---|
| **`PM1)`** | `In the event that there are popups to show at IGN OFF but the user has set **Power Accessory Delay to 0 seconds**, the head unit should 'stay awake' for 60 seconds up to 2.5 minutes to display the popup(s).` |
| **`r31`**（`Call Ended`） | c2 `End Call, **HU OFF**` ／ c3 `End Call but: If **Radio off Delay = 0** or Radio off Delay time…` |
| **`r32`**（`Projection call ends`） | c2 `End Projection Call and **HU OFF**` ／ c3 `End Projection Call and HU remains ON…` |

**共同謂詞**：head unit 於 key-off 後是否維持喚醒。
`PM1)` 取「stay awake」，`r31`／`r32` 取「HU OFF」。**取相反值。**

**條件互斥未證**：key-off 之後通話結束、而同時有 FOTA popup 待顯示 ——
**素材未載何者優先**。

**→ 牴觸成立**（R-PMH84）。執行層之判定與其停手皆正確。

### 2.1 而其真正之核心，執行層已經指出了

`PM1)` 之條件為 **`Power Accessory Delay = 0`**；
`r31` 之條件為 **`Radio off Delay = 0`**。

**二者從未同時出現於任一份文件**（A-PMH24）。故有兩讀：

| 讀法 | 則 |
|---|---|
| **二者為同一物之兩名** | 條件完全重合，**牴觸最尖銳** —— 同一設定值下，一方說 stay awake、一方說 HU OFF |
| 二者為不同設定 | 條件未必重合，牴觸之範圍縮小，**惟仍未證互斥** |

**兩讀皆通向「須加限定」，故限定之授權不待其釐清；
而該釐清本身仍須問**（§四 R-PMH114）。

---

## 三、限定之授權 —— **准，且其位置與 R-PMH87 不同**

執行層提案：加事件層限定「無通話進行中」，使 `r31`／`r32` 之
`Call Ended`／`Projection call ends` **不可能發生**。

**准。** 其機制與 R-PMH87 同（排除事件即排除該格），
且**充分**：無進行中之通話，則通話不可能結束。

### 3.1 但它該放 Pre-Condition，不是 procedure

R-PMH87 之七項限定置於 procedure，**因其為測試員之動作**（不按、不轉、不開）。

**本項不同** —— 「無通話進行中」是一個**狀態**，不是一個動作。

| canon | 依據 |
|---|---|
| §4.4 | Pre-Condition 為 starting **state / environment**；`Bluetooth is enabled.` 為其合法型態之一 |
| §4.5 | 互動資料（測試員選擇之按鈕、選項）→ Procedure |

**故其位置為 Pre-Condition**：`No phone call or projection call is active`。
**不得為求與 R-PMH87 一致而寫成 `Do not…` 形態** ——
限定之位置由**其型別**決定，非由前例決定。

→ R-PMH113。

### 3.2 連帶之覆蓋缺口

加此限定後，**「IGN OFF 時通話結束且有 popup 待顯示」之行為不被任何 TC 涵蓋**。

其行為只在矩陣有（`r31`／`r32`）、規格未載 →
依 R-PMH55(b) 不得為其撰寫 TC，**登記為覆蓋缺口**，
併入 `DR-PMH8`（其尚未發出）。

---

## 四、A-PMH24 —— **不與 `DR-PMH5` 同源，須另問**

執行層自陳其判「與 `DR-PMH5` 同源」而未開新問，**且該判斷未經裁定**。

**不採。** 三者之對象不同：

| DR | 其對象 |
|---|---|
| `DR-PMH5` | **p9 之能力矩陣**其來源何在 |
| `DR-PMH7` | 素材中三處**未定義之記法**（`VP`／`Else: Mute Active`／`Note:`） |
| **A-PMH24** | **兩個名詞是否指同一設定**（`Power Accessory Delay` vs `Radio off Delay`） |

**A-PMH24 之形態屬 `DR-PMH7` 之類（術語未定義），非 `DR-PMH5` 之類（文件缺失）。**

**併入 `DR-PMH8` 為第四問**（其尚未發出，無須另發），→ R-PMH114。

---

## 五、`r15` 之條件式判定 —— **建登記簿，非建檢查**

執行層 §5 第 3 項：`r15` 之判定寫作「**若 `DR-PMH5`／`DR-PMH7` 二問皆肯定
即為牴觸**」，而**該條件式寫在依據文字裡，答覆到達時沒有任何東西會提醒回來改它**；
擴充檢查即新增檢查項（R-PMH104），故其停手。

**停手正確，而正解不是檢查。**

**一份清單不是一個檢查** —— 其不判定任何事、不產生 PASS／FAIL、
不增加「檢查什麼種類的錯誤」。**故不在 R-PMH104 之凍結範圍內**
（其判別法見 R-PMH107）。

→ R-PMH115：於 `DECISIONS.md` 立 **`PENDING-ON-DR` 登記簿**，
每筆記「哪一個判定、繫於哪一個 DR 之哪一問、其答覆為何值時該判定改為何」。
**DR 之狀態改為 `ANSWERED` 時，該簿之對應筆為必辦事項。**

---

## 六、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH113（batch 3 之限定授權）
`Power Transitions` 組之各 TC，其斷言涉及 head unit 於 key-off 後是否維持
喚醒者，**加 Pre-Condition**：

    No phone call or projection call is active

**其位置為 Pre-Condition 而非 procedure** —— 「無通話進行中」為一個**狀態**
（canon §4.4 之合法型態），非測試員之動作。
**不得為求與 R-PMH87 之七項一致而寫成 `Do not…` 形態** ——
**限定之位置由其型別決定，非由前例決定。**

其充分性：`r31`（`Call Ended`）與 `r32`（`Projection call ends`）之事件
**皆以「有一通進行中之通話」為前提**；無之則該事件不可能發生，二格不適用。

**連帶之覆蓋缺口**：「IGN OFF 時通話結束且有 popup 待顯示」之行為
只在矩陣有、規格未載，依 R-PMH55(b) 不得為其撰寫 TC，
**登記為覆蓋缺口並併入 `DR-PMH8`**。

**本授權不預判 `Power Accessory Delay` 與 `Radio off Delay` 是否同一**
（A-PMH24）—— 兩讀皆通向「須加限定」，故限定不待其釐清。
```

```
R-PMH114（A-PMH24 併入 `DR-PMH8` 為第四問）
A-PMH24（`Power Accessory Delay` 與 `Radio off Delay` 從未同時出現於任一
文件，二者是否指同一設定未知）**併入 `DR-PMH8`**，為其第四問。

**執行層所判「與 `DR-PMH5` 同源」不採** —— 三者對象不同：
`DR-PMH5` 問**文件之缺失**（p9 矩陣之來源）；
`DR-PMH7` 問**記法之未定義**（`VP`／`Else: Mute Active`／`Note:`）；
A-PMH24 問**兩個名詞是否指同一物**。
**其形態屬 `DR-PMH7` 之類，非 `DR-PMH5` 之類。**

`DR-PMH8` 尚未發出，故直接增問，不另發文。
```

```
R-PMH115（`PENDING-ON-DR` 登記簿）
凡某項判定之結論**繫於某 DR 之答覆**者，須登記於 `DECISIONS.md` 之
`PENDING-ON-DR` 一節，每筆四欄：

  (1) 該判定之所在（檔案、條目、格號）；
  (2) 其所繫之 DR 與其第幾問；
  (3) **答覆為何值時，該判定改為何** —— 逐值列出，不得只寫「須重看」；
  (4) 登記日期。

**DR 之狀態改為 `ANSWERED` 時，該簿中對應之各筆為必辦事項**，
須於該輪之上繳逐筆回報其處置。

**本簿不是檢查** —— 其不判定任何事、不產生 PASS／FAIL、
不增加「檢查什麼種類的錯誤」，**故不在 R-PMH104 之凍結範圍內**
（R-PMH107 之判別法）。

現行應登記者至少三筆：
  `r15` 之條件式判定（繫於 `DR-PMH5` (1)(2) 與 `DR-PMH7` Q1）；
  `r46`／`r47` 之納入限定（繫於 `DR-PMH7` Q2 —— 若答為「維持靜音」，
  batch 2 之六條限定即為過度限定）；
  `-013` 之「一日」與 `-011` 之設定路徑（繫於 `DR-PMH8` (a)(b)）。

依據：29b 上繳 §5 第 3 項 —— 執行層指出該條件式「寫在依據文字裡，
而依據文字不是機器可判之物，答覆到達時沒有任何東西會提醒我們回來改它」。
```

---

## 七、作業步驟

1. **抄錄** —— §六之 R-PMH113 ~ R-PMH115 逐字抄入 `RULINGS.md`，附核對表。

2. **`DR-PMH8` 之第四問增補（R-PMH114）** —— 其逐字：

```text
  Q4: Are "Power Accessory Delay" and "Radio off Delay" the same setting under
      two names, or two different settings?

      The logic and flow document uses "Power Accessory Delay" (PM1, page 9);
      the State Matrix uses "Radio off Delay" (rows "Call Ended" and
      "Projection call ends"). Neither term appears in the other document, so
      we cannot tell whether they refer to the same value. This matters to us
      because PM1 says the head unit should stay awake when that value is 0 and
      there are pop-ups to show, while the matrix says the head unit goes off
      when that value is 0 and a call ends.
```

   並增列 §三之覆蓋缺口為第五問（或併入 Q4 之後段，由執行層擇一並載理由）。

3. **`PENDING-ON-DR` 登記簿之建立（R-PMH115）** ——
   至少三筆，四欄齊備；第 (3) 欄須**逐值列出**。

4. **batch 3 之產出 —— `Power Transitions`（7 leaf）** ——
   依 29b §4.1 步驟 9 之三項拘束，另加 R-PMH113 之 Pre-Condition。
   **逐條套用 R-PMH111 之判別法並具名（含「否」者）。**
   `tc_id` 續 provisional；零寫回。

5. **章 9 之規格側全枚舉（29b §5 之附項）** —— 若其規模允許則做，
   否則量其行數並具名其未做，**不得靜默略過**。

---

## 八、停止條件

canon §0 六條，另加本包三條：

7. batch 3 之任一斷言掃描發現**新的**牴觸（未經登記者）
8. 步驟 4 之任一斷言經 R-PMH111 判別為倚賴 p9 **而仍被產出**
9. 9.1 之五 leaf 有任一 `source_clause_origin` 非 `sys1_export`（R-PMH75）

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 九、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH8`（四問 ＋ 更正句）之發出 ＋ 日期與對象** —— **其首段之更正句未發出期間，上游所知之我方狀態仍是「section 9 已暫停」，而我方已恢復撰寫**（29b §5 所指之不符，現正存在） | 否，但其不符每日累積 |
| 2 | 29 §八第 2 項 —— 舊 DR 稿之處置（分析層認為執行層之保留加註正確） | 否 |
| 3 | 9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §六 |
|---|---|---|
| R-PMH113 | batch 3 之限定授權；限定之位置由型別決定，非由前例決定 | ✅ |
| R-PMH114 | A-PMH24 併入 `DR-PMH8` 第四問；不採「與 `DR-PMH5` 同源」 | ✅ |
| R-PMH115 | `PENDING-ON-DR` 登記簿；其不是檢查，不在凍結範圍 | ✅ |

三條各管一事。**本包未新增任何檢查程式或檢查項**（符合 R-PMH104）。
