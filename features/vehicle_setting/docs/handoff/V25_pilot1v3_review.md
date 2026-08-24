# V25 下放包 — pilot #1 v3 之覆核、R-VF70、W-VF63

分析層寫入，2026-08-24。**補落檔（原輪次因 MCP 逾時未寫成）。**
對象：`docs/upstream/V24_pilot1v3.md` ＋ `generated/vf230_pilot1_v3.json`。

---

## 1. §2.1 —— **V24 §4 之表漏列 `seq 241`，且 247 之字數我數錯**

| seq | V24 §4 所載 | 機械實測 |
|---:|---:|---:|
| 241 | *（歸入「其餘 7 條合規」）* | **15** |
| 244 | 16 | 16 |
| 246 | 15 | 15 |
| 247 | **17** | **18** |

**兩處皆為我之手數之誤。** 判準（`len(title.split())`，括號與引號內計入）
為 V24 §4 所自定，執行層以同一判準機械實測，**其數為準**。

**執行層 §6-2 之對照成立**：V24 §2 指 V23「執行層據以自檢、回報通過，
而系統預設原封未動」；本輪換成**分析層之表列漏了一條** ——
**兩次同型：未經機械執行之量測，其結果不可靠。**

**Defect C 之範圍為 4 條。** 一併縮短 241 **正確** ——
其與 247 為同一 leaf 之 Absent／Present 對，只縮其一會使該對之標題形式不一致。

---

## 2. §2.3 —— 去冒號，採純句式

Part 1 之 225 條 `tc_title` **無一採情境標籤式**（實測），
V24 §4 之但書生效。**現行之冒號式介於二者之間，不採。**

```
分析層裁定 2026-08-24
四條改純句式，形式 `<主體> <動詞> when <條件>`：

  241  Suspension Service Mode not displayed when CAN node 27 is Absent        11
  244  Power Tailgate Alert modifiable when CAN node 82 is Present             10
  246  Lane Sense Warning modifiable when Lane_Assist is Active Lane Management 11
  247  Suspension Service Mode modifiable when CAN node 27 is Present          10

手足區辨 token 保留（節點號、分割值）。
`displayed and modifiable` 縮為 `modifiable` —— 其於正向條中蘊含 displayed；
若條文將二者並列為獨立斷言，則 ER 須分列二行，而標題只需其區辨軸。
```

---

## 3. §2.2 —— `listed`／`displayed` 以**條文所用之動詞**為準

```
分析層裁定 2026-08-24
procedure 與 ER 之動詞統一為該 leaf 之條文所用者：
  條文用 `displayed` → 二處皆 displayed；條文用 `listed` → 二處皆 listed
**不以我方之語感擇一** —— 其為 §6 之 1:1 於用詞層面之要求，
而其基準為來源（R-VS6 之精神）。

執行層照 V24 只改 procedure 而未動 ER、並具名其為自身判斷，**正確**。
```

---

## 4. R-VF70 —— 判準以**允許型別之白名單**為之

§6-1 之判斷為本輪最重要者：

> pattern 化把「解讀之不可檢驗」換成「列舉之不完整」——
> **它是嚴格的改善，但不是消除。**

```
R-VF70（分析層裁定 2026-08-24）
凡 canon 之條文載有**允許型別之列舉**者，其自檢判準以**白名單**為之，
不以禁止串之黑名單為之。

`pre_conditions` 依 canon §4.4，其允許者為四類：
    外部環境／硬體周邊／功能初始狀態／系統版本或模式

**判準改為**：每一條 `pre_conditions` 須可歸入上開四類之一，
**不可歸類者一律報違規**（而非「命中禁止串者報違規」）；
歸類之依據須於自檢之輸出逐條具名。

`PRE_FORBIDDEN` 之六串保留為**輔助**（其命中即已知之違規形態，可加速定位），
**惟通過黑名單不等於通過白名單**。

理由：黑名單之完整性無檢查可管（R-VF69 之列舉即其例）；
白名單之完整性由 canon 之條文本身保證 —— canon 已列四類，不可歸類者即在其外。
```

**代價具名**：白名單須逐條歸類，而該歸類之對象為「屬四類中哪一類」
（有限選項、可覆核），**非「這條是不是系統預設」（無限開放）**。

---

## 5. §6-3 —— 起始狀態，Part 1 有既有做法

Part 1 之 `pre_conditions` 用 `The HU is in the Full-Operation state`
（見 `pilot6_sheet.md` #5／#7）—— **其為具名之電源狀態，屬 canon §4.4 之
「功能初始狀態」**，非「HU is powered on」之系統預設，且已通過 pilot #5＋#6。

```
分析層裁定 2026-08-24
本批十條之 `pre_conditions` 增列 `The HU is in the Full-Operation state`，
**置於 PROXI 設定之前**（其為狀態，PROXI 為配置）。
依 R-VF70 歸類為「功能初始狀態」。
**其非回復 Defect A** —— Defect A 所刪者為過程之描述，本項為具名之終態。
```

---

## 6. W-VF63 指令

```text
W-VF63  pilot #1 v4

 (1) 四條 tc_title 依 V25 §2 改純句式（去冒號）
 (2) listed／displayed 依 V25 §3 統一為條文所用之動詞，逐條列其條文所用者與所採者
 (3) 十條之 pre_conditions 增列 `The HU is in the Full-Operation state`，
     置於 PROXI 設定之前
 (4) 自檢依 R-VF70 改白名單：每條 pre_conditions 歸入 canon §4.4 之四類，
     不可歸類者報違規；逐條輸出其歸類
     可失敗性實測：插入一條不可歸類者（如 `The user has an account`），須 rc=1
 (5) 產 vf230_pilot1_v4.json，supersedes: vf230_pilot1_v3.json

 不重跑選池、不改 leaf 集合、不改 specification_reference、
 不改 reasoning 之 Priority 段。

 必列：四項之逐條差異行；自檢對 v4 得 0、對 v3 得幾；白名單之逐條歸類表。
```

---

## 7. 三項確認

| 項 | 確認 |
|---|---|
| **引號慣例** | **成立**。關鍵證據為「7 個標籤中 5 個之來源未加而 Part 1 加」——**可證偽且測法已列**。採之 |
| **接工單前之查核** | V19a 之教訓已內化為固定動作（查 `docs/upstream/`＋`git log`＋`git status`）。記明 |
| **§6-5** | **成立**。v3 未碰選池／leaf／reasoning，**故 v3 之通過不構成對 v2 那些判斷之第二次確認**；其排入 pilot #2 之母體另抽 |

---

## 8. 待 Pei

| # | 事項 |
|---|---|
| 1 | **DR-35**（A-VF18，`LaneSenseWarning-014` 條文自相矛盾）之送出，與 DR-34 併同（R-VF27） |

---

## 9. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| **R-VF70** | 判準以允許型別之白名單為之；黑名單降為輔助 | 分析層 |
| Defect C 之範圍 | 4 條；V24 §4 之手數為誤，以機械實測為準 | 分析層 |
| 動詞之統一 | 以條文所用者為準 | 分析層 |
| 起始狀態 | 增 `The HU is in the Full-Operation state` | 分析層 |
