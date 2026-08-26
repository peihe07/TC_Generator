# 下放包 09 —— Vehicle Category：pilot 提案之更正 + DR-VC8

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）／Pei
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/09_pilot_amend.md`
- 前一包：`docs/handoff/08_pilot.md`
- **本包更正下放包 08 §4.3 之一處判斷，並新立 DR-VC8、A-VC14。**
- pilot 仍待 Pei 裁；本包不授權任何 TC 產出。

---

## 〇、本包之由來

下放包 08 §4.3 稱「未結 DR 對本組之波及：無」，執行層於上繳包 08 §6
機械覆核成立。**該覆核正確，但其母體是「已知之七筆 DR」** ——
它能證明既有 DR 不波及本組，不能證明本組沒有未發現之缺件。

分析層於裁定前讀 `Glove Box` 12 leaf 之 `Requirement Title` 與
`Requirement Description` 全文（037，SHA256 `cb80a77e…d877ed`，
與素材台帳相符），**發現一處邊界值分歧**。

**這是「未讀即斷言」之變體**：我當時之檢視方法（逐筆對照 DR 標的）
形式正確，但只能抓已登記者。我未讀 12 筆內容即宣告「無波及」，
其涵蓋範圍小於該詞之字面。與 A-VC5／R-VC12 二為同一家族之第四例。

---

## 一、發現：`VC-033-01` 之鎖定門檻，Title 與 Description 不一致

```
Title       : After three sequential wrong PINs during Glove Box deactivation,
              block the deactivation feature for 30 minutes
Description : Inserts the wrong PIN more than three times in sequence,
              the feature will be blocked for 30'.
```

| 來源 | 字面 | 觸發於第幾次 |
|---|---|---|
| Title | `After three sequential wrong PINs` | **第 3 次** |
| Description | `more than three times in sequence` | **第 4 次** |

二者相差一次。

**這不是措辭問題，是可測門檻之分歧。** 依 IN §8.3，boundary 為
sibling axis，TC 須測 `=limit`、`limit−1`、`limit+1`。
而本案之 `limit` 究為 3 或 4 不明 —— TC 作者無論選哪一個，
都是在二個上游來源之間**替上游做決定**，觸 IN §8.4.1（不得造值）。

**不得以「取較嚴者」或「取 Title 為準」等規則自行消解** ——
R-VC15／R-VC17 之精神同樣適用於此：來源分歧時，
分析層之職責是登記與查詢，不是選一個。

### 與 A-VC10 之關係

A-VC10 已載「037 之 `Title` 資訊量大於 `Description`」，並舉
`VC-035-03`／`VC-036-02` 二例（Title 多出「不變更／不清除」之條件）。

**本案為不同形態**：非 Title 多載條件，而是**二欄之數值相互矛盾**。
A-VC10 之處置（以二欄之聯集為據）在此不適用 —— 聯集無法消解矛盾。
故另立 A-VC14，不併入 A-VC10。

---

## 二、DR-VC8（新立）

| 項 | 內容 |
|---|---|
| 標的 | 037 作者 |
| 內容 | `SWE1-HMI-VC-033-01`（§7.1）之鎖定門檻，`Requirement Title` 載 `After three sequential wrong PINs`（第 3 次觸發），`Requirement Description` 載 `more than three times in sequence`（第 4 次觸發），二者相差一次。請確認實際門檻，並說明 30 分鐘之計時起點（末次錯誤輸入時 / 彈窗顯示時）與其間之 HMI 呈現（按鈕灰化 / 顯示倒數 / 無提示） |
| 阻斷範圍 | **僅 `SWE1-HMI-VC-033-01`**。缺件期間該 TC 之門檻欄填 `PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3），不得留空、不得填 NA、不得自行取 3 或 4 |
| 批次 | **同批 A**（與 DR-VC2 ＋ DR-VC7 ＋ A-VC2 ＋ A-VC10 同為對 037 作者之查詢）—— 一次往返 |

> 附帶查詢之理由：30 分鐘之計時起點與其間之 HMI 呈現，
> 規格與 037 皆未載。若不一併問，撰寫該 TC 時會再缺一次。
> 但**不得因此擴大提問至規格未涵蓋之範圍** —— 只問已存在需求之未明處。

---

## 三、A-VC14（新立）

```
A-VC14（037 Title 與 Description 之數值矛盾）

`SWE1-HMI-VC-033-01`（§7.1，Glove Box 停用之錯誤鎖定）：

  Requirement Title       : After three sequential wrong PINs …
                            → 第 3 次觸發
  Requirement Description : more than three times in sequence …
                            → 第 4 次觸發

二欄之數值相差一次，為**可測門檻之分歧**，非措辭差異。

與 A-VC10 之區別：A-VC10 為「Title 多載 Description 未載之條件」，
其處置為取二欄之**聯集**；本案為「二欄之數值相互矛盾」，
聯集無法消解，故另立本條，不併入。

拘束：
(a) TC 作者**不得**自行取 3 或 4，不得以「取較嚴者」、「以 Title 為準」
    或任何一般性規則消解之。來源分歧時之職責為登記與查詢
    （DR-VC8），非選擇。
(b) 缺件期間該 TC 之門檻欄填
    `PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3）。
(c) 本條之範圍限於 `VC-033-01`。**未掃描其餘 116 個 leaf 是否存在
    同型矛盾** —— 本條不得被讀為「全表僅此一例」。
    全表掃描列為 T52。

狀態：PENDING（待 DR-VC8）。
```

---

## 四、下放包 08 §4.3 之更正

原文：

> **本組無 `PENDING: DR-{n}` 之佔位需求**（IN §8.4.3）。

**更正為**：

> 本組於七筆既有 DR 之下無波及（執行層上繳包 08 §6 已覆核成立）；
> 惟 `VC-033-01` 因 A-VC14／DR-VC8 而帶**一筆 PENDING**。
> 12 筆中 11 筆無 PENDING，1 筆有。

記入 `docs/REVISIONS.md` 為 **REV-13**。

### pilot 提案是否因此改變？—— 不改

`Glove Box` 仍為建議之 pilot，四項理由不變，另加一項：

**一筆 PENDING 對 pilot 而言是資產而非負債。** pilot 之目的是驗證
TC 生成之全部形態；`PENDING: DR-{n}` 之佔位寫法（IN §8.4.3）是本
feature 尚未實地驗證過的形態之一。在 12 筆之小批中驗過它，
勝過在 100 筆之大批中第一次遇到。

替代組之比較不受影響：`Settings Behavior`（15）之 P0 與分歧揭露義務、
`Brake Service`／`Cabrio Widget` 之待補節重審風險，皆仍成立。

---

## 五、pilot 之規模預估（供 Pei 裁定時參考，非授權）

依 IN §8.2.2「RD sub-id ≠ TC count」，12 leaf 未必產 12 TC。
逐筆研判可能需拆分者：

| leaf | 可能之拆分軸 | 估 TC |
|---|---|---|
| `VC-026-03`（PIN 輸入兩次，僅指示文字不同）| 單一 | 1 |
| `VC-028-02`（啟用流程不限錯誤次數）| 單一，惟需 N 次之具體值 —— 取「多次」而非造具體數 | 1 |
| `VC-033-01`（停用三次錯誤鎖 30 分）| **boundary（§8.3）**：門檻−1 不鎖／=門檻 鎖／鎖定期滿後解除 | **2–3** |
| `VC-033-02`（3 位數 + Enter → 彈窗）| boundary 之另一軸（位數）；4 位為正常路徑已由他筆涵蓋 | 1 |
| 其餘 8 筆 | 單一 | 8 |
| | **合計** | **13–14** |

> `VC-033-01` 之拆分數取決於 DR-VC8 之回覆 —— 門檻未定則
> boundary 之三點無法定值。此為該 leaf 帶 PENDING 之直接後果。

### 一項須注意之 sibling 陷阱（撰寫時）

`VC-028-02`（啟用流程：**不限**錯誤次數）與
`VC-033-01`（停用流程：**三次**鎖定）**並不矛盾** ——
二者分屬啟用（§5.1）與停用（§7.1）兩個流程。

此為極易被誤讀為規格衝突之處。TC 撰寫時，二筆之
`test_item` 括號下半必須明確區分其流程
（R-S4 之 sibling 區分 token），否則審閱者會將其讀為矛盾。

---

## 六、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T52 | **全表掃描 A-VC14 之同型矛盾** —— 對 117 leaf 之 `Title` 與 `Description`，抽出二欄各自之數值（次數、位數、時間、數量），比對其是否一致。逐筆回報不一致者。**只回報，不處置**。掃描方法與其偽陰性須揭露（數值以文字書寫者、單位不同者、隱含於語意者）| 1 |
| T53 | `DATA_REQUESTS.md` 新增 DR-VC8（含阻斷範圍與同批 A），未結數更新為**八筆**；同批 A 更新為**五項** | 1 |
| T54 | `ANOMALIES.md` 新增 A-VC14（條文逐字）| 1 |
| T55 | `docs/REVISIONS.md` 新增 REV-13（§4.3 之更正）| 1 |

**T51（pilot）仍待 Pei 裁。** 本包未授權任何 TC 產出。

---

## 七、Pei 之最短回覆格式

```
pilot: Glove Box / 其他（列出）
DR-VC8: 准（併同批 A）/ 改
```

同批 A 現為五項，發送後可一次解決：
DR-VC2（Source Requirement ID 之來源）、
DR-VC7（欄 18 Priority 之判準）、
A-VC2（封面 Reviewer／Date）、
A-VC10（Title 與 Description 之分工）、
**DR-VC8（VC-033-01 之鎖定門檻）**。

**DR-VC3 仍未發**，牽動 R-VC16(c)(d)、表 B、A-VC12。
