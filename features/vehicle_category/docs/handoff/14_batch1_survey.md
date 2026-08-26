# 下放包 14 —— Vehicle Category：批次計畫定案 ＋ 第 1 批之勘查前置

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/14_batch1_survey.md`
- 前一包：`docs/handoff/13_batch_plan.md`
- 裁定：Pei 2026-08-26 —— **批次順序准、批次規模准**
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `13_`，無碰撞。
- **本包不授權生成任何 TC。** 第 1 批先勘查，勘查回報後另行下放生成。

---

## 一、裁決條文（逐字抄入 `RULINGS.md`）

```
R-VC21（Phase 4 全量批次計畫）

（Pei 2026-08-26 裁定：順序准、規模准。）

pilot（`Glove Box`，12 TC）已收斂放行（下放包 13 §一）。
剩餘 105 leaf（117 leaf 母體）分 **7 批**，一 Test Set 一批，
**不跨組合批** —— Test Set 為 framework 所定之能力群，
跨組會使 `Test Set` 欄在同一批內分歧，批次即失去作為審閱單位之意義。

順序（排序判準依序為：DR 阻斷程度 → 格式形態新舊 → 規模）：

  1  `Category Structure`      24 leaf   無 DR 阻斷
  2  `Settings List`           30 leaf   無 DR 阻斷
  3  `Controls`                17 leaf   DR-VC1（僅 `VC-021` 一筆）
  4  `Settings Behavior`       15 leaf   無 DR 阻斷；含 2 個 P0 ＋ R-VC14 揭露
  5  `Ignition Availability`   16 leaf   DR-VC5（FROP 跨域全 16 筆）
  6  `Brake Service`            2 leaf   DR-VC3（邊界待重審）
  7  `Cabrio Widget`            1 leaf   DR-VC3（同上）

第 4 批不更前之理由：其含本 feature 5 個 P0 中之 2 個
（`035-03`／`036-02`）與 R-VC14 之分歧揭露義務（`036-01`）；
第 1、2 批將首次驗證非 Glove Box 形態之格式，待其穩定再做第 4 批風險最低。

第 6／7 批置末之理由：R-VC16(c) 明文其邊界待 DR-VC3 重審，
且屆時章 8／9 之 Cabrio 本體應另立 `Cabrio Rooftop`。重審前生成，
其結論可能被推翻。

每批之收斂條件：pilot 之十二項（實跑 15 項）＋ 二項：
  13. 該批之 `Test Set` 全筆一致，且與 `framework.md` §2 逐字相符
  14. 該批所用之 setup 片語皆取自 VC profile §5 之常數表

**每批之生成前須先勘查。** pilot 之 `Glove Box` 為純流程需求，
其素材全在文字層，故未設勘查步驟；其餘各組不得據此免除
（下放包 14 §二即為第 1 批之勘查所發現）。
```

---

## 二、第 1 批之粗查 —— 五個風險點

> **以下為分析層之粗查**，量自 037（SHA256 `cb80a77e…d877ed`）之
> `Requirement Description` 欄。**依 R-VC15 之精神，本節數字與判讀
> 不得沿用**，須由執行層重測；列出之目的是使勘查聚焦，非代替勘查。

### 2.1 `VC-013-04` —— 整條僅為交叉引用，且其標的不在素材清單

```
SWE1-HMI-VC-013-04  §2.6.3  P3
  Description: Refer to PDO graphics.
```

**該 leaf 之全部內容即此一句。** 其形態與 §16.1 同 ——
下放包 06 R-VC12 一已裁定 16.1「為交叉引用，非實質需求內容」
並改列非需求類。

**但二者地位不同**：16.1 在 037 之**未涵蓋** 17 節內；
`VC-013-04` 是 037 **已涵蓋之 leaf**，在 117 leaf 母體內，有 priority（P3）。

即：**037 把一個純交叉引用登記成了需求 leaf。**

且其標的 **PDO Graphics 不在素材清單**（`reference:` 六項無此件，
下放包 02 R-VC10 已窮舉）。

**處置（本包裁定）**：
- **不得自行剔除該 leaf** —— 117 母體為 R-VC3 所裁，剔除屬 Tier 2。
- 立 **DR-VC9** 索取 PDO Graphics，並請上游確認該 leaf 是否應為需求。
- 該 leaf 之 TC 帶 `PENDING: DR-VC9 PDO graphics`（IN §8.4.3）。
- 登記 **A-VC17**：037 之 leaf 中存在純交叉引用者，
  **未掃描其餘 116 leaf 是否另有同型**，該掃描列為 T79。

`VC-012-03` 亦含 `(refer to PDO Graphics)`，但其**另有可測內容**
（`continuing with additional features below the banners`），
與 `VC-013-04` 不同類 —— 其處置見 §2.2。

### 2.2 句子片段作為 leaf —— verbatim 上半之語意不完整

037 於 §2.6.2／§2.6.3 將長句拆成多個 leaf，**拆點在句中**：

| leaf | Description | 形態 |
|---|---|---|
| `VC-012-02` | `If there are two or more features, display them in the two half banners (topmost feature in the left, followed by the right)` | 完整句 |
| `VC-012-03` | `continuing with additional features below the banners (refer to PDO Graphics)` | **小寫起首之續行** |
| `VC-013-02` | `For four or more features, display the first two features as single banners, the next two features as half banners in the same row.` | 完整句 |
| `VC-013-03` | `follow with remaining features as tiles below the half banners` | **小寫起首之續行** |

R-4 只許「句首字母轉大寫」之排版正規化，**不及於語意補全**。
一個句子片段作為 `test_item` 上半，讀者無法理解其所指。

**處置（本包裁定）**：
續行型 leaf 之 `test_item` 上半，**取包含該片段之完整句**
（即跨 leaf 取整句），括號下半則載明**本 leaf 之驗證範圍**。

依據：R-S4 之上半為「需求／規格原句 verbatim」——
取完整句比取片段**更忠實於原句**。R-S4 僅禁「括號下半逐字相同」，
未禁上半相同；`-012-02`／`-012-03` 之上半相同而下半不同，合規。

**且須於 `reasoning` 載明**：本 leaf 之 Description 為句中片段，
上半取整句係為語意完整，本 TC 之驗證範圍以括號下半為準。

### 2.3 `VC-007` 系列 —— 表格被扁平化成一格

```
VC-007-01  Vehicle Tab Labels and Order.                        ← 疑為表頭
VC-007-02  VC2.2.2 | PHEV / MEV / HEV | E. Hybrid | Fourth
           VC2.2.3 | Performance Pages … Power Panel | Dashboard | Seventh
VC-007-03  VC2.2.4 | Trip | Trip | Fourth   VC2.2.5 | Camera App | Cameras | Second
           VC2.2.6 | Vehicle Info | My Car | First
VC-007-04  VC2.2.7 | BEV | Electric Vehicle | Fifth   …
VC-007-05  VC2.2.10 | Fuel Cell | Electric | Fifth   …
```

一張四欄表（規格 ID｜來源功能｜頁籤名｜位置）被扁平化，
且**多列擠在同一格**、以空白分隔而非換行。

須勘查三項：
(a) `VC-007-01` 之 `Vehicle Tab Labels and Order.` 是否為**表頭而非需求** ——
    若是，其形態同 §2.1 之 `VC-013-04`，併入 DR-VC9 一併詢問。
(b) 各格內之列數與欄邊界能否**逐列可靠切分**（`|` 之數量是否一致）。
(c) 該表是否另有**權威來源**（規格 §2.4 之原表、或 `HMI Settings List`）——
    若有，`spec_reference` 與值之取材應以原表為準，
    037 之扁平化格僅為索引。

### 2.4 `VC-011` 之 `the table` 指涉不明

```
VC-011  §2.6.1  Within the Dashboard tab, display the applicable content
                in order of the table.
```

`the table` 未具名。候選二：§2.4 之 Vehicle Tab Labels and Order 表、
或 `HMI Settings List`。**不得自行認定**（§8.4.1）——
勘查回報其可否自規格 §2.6.1 之上下文確定；不能確定則併 DR-VC9 詢問。

### 2.5 `VC-008` 之外部規格引用

```
VC-008  §2.5  If the vehicle has the Camera App (see Camera HMI Logic and Flow),
              Cameras will appear as a tab.
```

依 IN §8.4.2：本 TC 之範圍**僅及於「Cameras 出現為頁籤」**，
**不得測 Camera App 自身之任何行為**（那屬 Camera HMI Logic and Flow
之 SWE 需求）。`reasoning` 須載明此項委派。

`VC-009`（`If the Camera tab is present, remove Cameras from the Controls tab`）
同批，二者為同一觸發之兩個後果 —— 依 §5.7「一觸發多後果屬同一 TC」
**或**依 037 之既有拆分（二 leaf）各自成 TC？
**依 R-VC18 之先例，一 leaf 一 TC** —— 037 已拆，不得合併（§8.2.2 之反向）。

---

## 三、第 1 批之勘查任務（T78）

| # | 勘查項 | 回報形態 |
|---|---|---|
| a | 24 leaf 之 `Title`／`Description` 逐字全文 | 表 |
| b | §2.1–§2.5 五個風險點逐項覆核，**確認或推翻分析層之粗查** | 逐項判 |
| c | **素材可用性**：24 leaf 中，其可測內容需要 037 以外之素材者，逐筆列出該素材與其是否在手 | 表 |
| d | 24 leaf 之 SYS1 `Description` 對照 —— 037 之扁平化格是否在 SYS1 有更完整之形態（同 T17 之作法，以 repo `inputs/` 之權威複本為準，R-VC7）| 表 |
| e | 橫向／直向版面（§2.6.2／2.6.3）之 Pre-Condition 形態：顯示器方向是否為 §4.4 允許之 hardware/peripheral 類 | 判 |
| f | 預估 TC 數（24 leaf → n TC），並標出需 `PENDING` 者 | 表 |

**勘查後停，回報，不生成。** 生成之下放包待勘查結果另行發出。

> 本批不設「逾 N 條即停」之閾值 —— Display 之 R-G39 已證明
> 母體條數不是批次份量之正確代理量。本批之份量以 **leaf 數（24，已定）**
> 與 **TC 數（勘查 f 項）** 衡量。

---

## 四、其他任務

| # | 任務 |
|---|---|
| T79 | **全表掃描純交叉引用型 leaf**（承 §2.1 之 A-VC17）：117 leaf 中，其 `Title` 與 `Description` 皆僅為交叉引用而無可測內容者。逐筆列出。方法與偽陰性須揭露 |
| T80 | `DATA_REQUESTS.md` 新增 **DR-VC9**：索取 PDO Graphics；並詢問 `VC-013-04`（及 T79 所得之同型者）是否應登記為需求 leaf。未結數更新為**九筆** |
| T81 | `ANOMALIES.md` 新增 **A-VC17**（037 之 leaf 中存在純交叉引用者，範圍待 T79）|
| T82 | 承下放包 13 —— T73（profile §5 常數表）、T74（第 13/14 項）、T75（腳本更名）、T76（PLAYBOOK 二則）、T77（pilot 標記已收斂）如尚未完成則本輪完成 |

---

## 五、上繳包要求

1. T78 之勘查表（a–f 六項）
2. T79 之全表掃描結果
3. T80–T82 逐項結果
4. 量測條件揭露（R-G8）：T78(d) 之 SYS1 對照、T79 之掃描方法與偽陰性

---

> 同批 A（五項）與 DR-VC3 仍待發送。**DR-VC9 可併入同批 A**
> （同為對 037／規格作者之查詢），使其成為六項 —— 待 Pei 定。
