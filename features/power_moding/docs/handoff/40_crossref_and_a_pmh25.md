# 下放包 40 —— 交叉引用之位移重掃（出貨阻斷）、R-PMH152 第 10 筆之撤回、39b 之收錄

- 日期：2026-08-28
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/40_crossref_and_a_pmh25.md`
- 前一包：[39a_pei_closures.md](39a_pei_closures.md)
  （上繳併入 [../upstream/39_delivery.md](../upstream/39_delivery.md)，已覆核 —— 見 §一）
- 性質：**覆核包 ＋ 出貨阻斷包**。不新增 TC、不新增檢查程式；**改動 51 條之 `test_item` 括號下半**（僅引用之號碼），重跑寫回一次。

---

## 零、分析層之自我更正（先於一切）

1. **39a 之提案建在一句過期陳述上。** 分析層於 39a 提案「第 10 筆不另開問、揭露為終態」時，
   以「`-016` 不斷言逾時秒數」為事實；**該陳述於 35 包（R-PMH133）即已不成立**（見 §二）。
   Pei 以「出」核可者為分析層之提案，**其前提錯在分析層**。R-PMH152 第 10 筆部分因而須撤回（§三 R-PMH154）。
2. **分析層於 39 包步驟 8 未令重掃交叉引用。** R-PMH53 明令「tc_id 位移時須重掃該批全部交叉引用」；
   R-PMH143 於 38 包全體重編號，**分析層於 38／39 兩包皆未把 R-PMH53 列為 Phase 5 之必辦**。
   執行層於 R-PMH153 落檔時見 `-040` 自我引用一處而標「另案」，**分析層當時亦未追問其是否為系統性**。

（二者皆為 R-VS50′ 可達性原則之違反 —— 事實可自 `generated/final/` 一讀而得，而分析層未讀。）

---

## 一、上繳 39（含 39a 之執行）之覆核結果

**39 主體 §1–§9：通過。** 特別記明三項：
- §5 `Cover` 作者欄之停手**正確** —— 母體 11/17 空、6/17 為他人姓名，「依慣例填」之前提確不成立。**其值仍待 Pei**（本包不裁）。
- §6 之 17 §5.4 為 6 項非 5 項、§7 之 16 筆非 15 筆 —— **執行層之更正皆採認**，錯在下放包。
- §7.1 之自查（`-001-01` A1 承載者誤寫 `-011`，正確 `-012`）—— 採認其「逐 `tc_id` 回查 leaf」之補救。

**39a 之執行 §39a.1–§39a.6：通過。** 停止條件 7／8／9／10 之核驗方式（`startswith`、§1 數字比對、告別音實測、CFTS009 全表掃描）皆為實測而非宣告。

**39a.7 之五項自陳**：第 1、2、4、5 項為已具名之限度，不阻斷，**惟第 5 項所求之比例本包順手算出**（§六）。
**第 3 項（A-PMH25 之狀態詞）—— 問題本身不成立**，見 §二。

**覆核另查出二項執行層未自陳者**（皆為分析層自 `generated/final/` 與 `feature.yaml` 實測）：
- **交叉引用全數指向 provisional 號**（§四）—— **出貨阻斷**；
- `feature.yaml` 之 `delivery` 區塊仍記 **rev2**（`01e917b8…`），而 `DELIVERY_NOTE.md` 抬頭已記 **rev3**（`8f471ddf…`），
  **二者不一致**，且 `check_state_consistency` 未攔（其比對範圍不含 `DELIVERY_NOTE.md`）。

---

## 二、A-PMH25 之實情 —— 缺口早已補，第 10 筆之前提為假

`generated/final/batch03.json`，`NR1L-DisclaimerScreen-029`（provisional `-016`，leaf `SWE1-HMI-PM-018-01`）逐字：

```
ER4  The pop-up is closed after the 60-second timeout defined in the pop-up list
ER5  The radio shuts off when no other pop-ups remain
```

其 `reasoning` 自載：「35 包 §3（R-PMH133）之修正 —— 前開『不造值』之前提已被 037 之 DESC 推翻 …
**60 秒與其後二句皆完整，故 ER4／ER5 補之。A-PMH25 已改 `RESOLVED`。**」
R-PMH138(d) 之 must-hit 更以「刪去 `-016` 之 ER4 → 正向須報 `未涵蓋`」為錨點 —— **ER4 涵蓋 DESC 斷言一事經機械驗證**。

### 2.1 事故鏈

| 輪 | 發生之事 |
|---|---|
| 34／35 | R-PMH133 推翻 A-PMH25 之前提；ER4／ER5 補入；A-PMH25 改 `RESOLVED`。**`PENDING-ON-DR` 第 10 筆未於當輪結案**（應為 `RESOLVED-BY-R-PMH133`） |
| 36 | 第 10 筆被記為「無所繫 DR」之形態問題，**未回頭查其是否仍為未決** |
| 39a 分析層 | 以「`-016` 不斷言逾時秒數」提案終態揭露 → Pei 核可 → R-PMH152 |
| 39a 執行層 | A-PMH25 `RESOLVED` → `ACCEPTED-RISK`；`DELIVERY_NOTE.md` §9 增第 8 項「`-016` 之逾時秒數無任何 TC 驗到」 |

**§9 第 8 項為一句對客戶為假之揭露** —— 它告訴交付方我們沒驗一件已驗之事。

### 2.2 第 9 筆不受影響

`-030`（provisional `-017`）之三條 ER 實測**確未斷言** `60 秒無互動` 與 `總計 10 分鐘` 之交互作用，
R-PMH152 之第 9 筆部分**維持**。

### 2.3 連帶須覆核者（本包令實測，不預判）

- `DELIVERY_NOTE.md` §7 與 §9 第 6 項之 R-PMH75 風險（「`the radio should shut Off` 不會有任何一條 TC 驗到」）：
  ER5 已驗 037 DESC 之**條件式**關機（`If no other popups remain, the system shall shut off the radio`）。
  R-PMH75 所指者為 PDF 側被刪之子句 `the radio should shut Off the popup should close`（逾時後**無條件**關機之一讀）。
  **二者是否同一行為，須由執行層對照 PDF p9 block 層與 037 DESC 後具名**；同一 → 第 6 項一併移除；不同 → 第 6 項改寫為「無條件關機之一讀未驗」。
- §8.2 之 §9 項次引用錯位：第 9 筆記「§9 第 8 項」實為第 9 項；第 10 筆記「第 7 項」實為第 8 項。

---

## 三、裁定條文 —— **待 Pei 核可，核可前不生效**（比照 R-PMH117／R-PMH121 之形態）

```
R-PMH154（R-PMH152 第 10 筆部分撤回 —— A-PMH25 回 `RESOLVED`）
R-PMH152 中關於未決清單第 10 筆（A-PMH25——`-016` 不斷言逾時秒數）之部分**撤回**，
其第 9 筆部分（`-017` 之二上限交互作用）**維持**。R-PMH152 正文不改字，以沿革附註承接。

撤回之依據為實測：`NR1L-DisclaimerScreen-029`（provisional `-016`）之 ER4 逐字為
`The pop-up is closed after the 60-second timeout defined in the pop-up list`，
係 35 包依 R-PMH133 所補，且為 R-PMH138(d) must-hit 之錨點。
「`-016` 不斷言逾時秒數」於 39a 提案時已非事實，**該錯在分析層**。

效果：
(a) A-PMH25 之狀態詞回 `RESOLVED（037 之 DESC 為完整句，34 包查出；ER4 於 35 包補入）`，
    39a 所加之 `ACCEPTED-RISK` 標頭改為沿革附註，不刪；
(b) `PENDING-ON-DR` 第 10 筆之結案詞改 `RESOLVED-BY-R-PMH133`（非 `ACCEPTED-RISK`），
    `DELIVERY_NOTE.md` §8.2 該列隨之改；
(c) `DELIVERY_NOTE.md` §9 第 8 項**自交付文件移除**（其為對客戶不實之揭露）；
    內部紀錄（`DECISIONS.md`）依 R-TM13 留痕：載該項曾存在、移除依據為本條；
(d) §9 第 6 項與 §7 之 R-PMH75 風險陳述，依 40 包 §2.3 之實測結果改寫或移除。

裁定：Pei，2026-08-__（待核可）。
```

```
R-PMH155（交叉引用之位移重掃 —— rev3 不得出貨）
R-PMH143 之單次指派使 51 條 TC 之 `tc_id` **全體位移**（映射表 `data/tc_id_map.tsv` 中無任一列為恆等），
而 R-PMH53「tc_id 位移時須重掃該批全部交叉引用」**未於 Phase 5 執行**。
實測（40 包 §四）：`generated/final/` 六批之 `test_item` 括號下半共 **42 處** `-\d{3}` 引用，
**42/42 為 provisional 號**，於工作簿中全部錯指；其中 `-040`／`-043` 二處指向自身。

處置：
(a) `output/…_20260826_writeback_rev3.xlsx` **不得出貨**（與 rev2 同其處置：不覆寫、不刪除）；
(b) 執行層依 `tc_id_map.tsv` 將六批 `generated/final/` 之括號下半引用**逐處映射為 final 號**，
    僅改號碼，不改其餘文字；`generated/batch0N.json`（provisional 版）**不動**；
(c) 映射後須跑 R-PMH153 已擴之 C7（不帶反引號之 `-\d{3}` 形態），
    其語意相容比對之對象為被引用者之 `leaf_id`／`distinguishing_axis`，42 處逐處出示結果；
(d) 重跑 `write_back.py` 產出 **rev4**，其前置閘（R-PMH22 三項、故意失敗）與四項不變量照 39 包步驟 4 之規格重做；
(e) `feature.yaml` 之 `delivery` 區塊改記 rev4，`supersedes` 鏈載 rev2→rev3→rev4 及各自作廢之依據（R-PMH153／本條）。

R-PMH53 之義務自此明定為 Phase 5 之必辦：**凡執行 R-PMH143 之指派，同輪須完成交叉引用重掃並出示逐處對照表**。
本條為既有條文之執行，非新判準；apparatus 凍結（R-PMH103／104）不受影響。

裁定：Pei，2026-08-__（待核可）。
```

---

## 四、交叉引用之實測（分析層，`generated/final/` 六批）

| 批 | 有引用之 TC | 引用數 | 全為 provisional 號 | 自我引用 |
|---|---:|---:|---|---|
| batch01 | 5 | 5 | ✅ | — |
| batch02 | 7 | 12 | ✅ | — |
| batch03 | 7 | 8 | ✅ | — |
| batch04 | 10 | 12 | ✅ | — |
| batch05 | 4 | 5 | ✅ | `-040`→`-040`、`-043`→`-043` |
| batch06 | 0 | 0 | — | — |
| **合計** | **33** | **42** | **42/42** | **2** |

無引用者 17 條（含 `-004`、batch06 之 5 條）。

**經映射表換算後，42 處之所指全數落回其設計上之 sibling**（例：`-029`「paired with -017」→ `-030`，
`-030`「paired with -016」→ `-029`；`-040` 之自我引用 `-040` → `-039`，即 provisional `-040` 之 final 號）。
**故本項為純位移，非語意錯誤** —— 修法為機械映射，不須重寫任何一條之語意。
**執行層須以自己的程式重算此表（先算後比，R-G7-1）**，與本表逐格相符後方得進入步驟 4。

---

## 五、作業步驟

### 即刻（不待核可）

1. **重算 §四之表** —— 自 `tc_id_map.tsv` 與六批 `generated/final/` 獨立量測，逐格與 §四比對；不符者停手回報。
2. **§2.3 之實測** —— PDF p9 block 層之 `the radio should shut Off the popup should close` 與 037 `-018-01` DESC 之
   `If no other popups remain, the system shall shut off the radio` 是否同一行為，出示兩造逐字與判定理由。
3. **39b 之收錄** —— 於 `docs/upstream/39_delivery.md` 闢「39b 之執行（R-PMH153）」節，載：
   R-PMH153 之落檔核對表、50 條改寫之前後各一例、`lint_batch.py` 二項新檢查之故意失敗輸出、
   rev3 之 SHA256 與四項不變量、`generated/final/` 六批之改寫前後 SHA256。
   `docs/INDEX.md` 之 39 包要點增 39b 一行。**該輪已發生，本步驟只補紀錄，不重做。**
4. **`feature.yaml` 之 `delivery` 區塊** —— 先改記 rev3（`8f471ddf…`，`supersedes` 載 rev2 作廢依據 R-PMH153），
   使其與 `DELIVERY_NOTE.md` 一致；rev4 產出後再改（步驟 8）。
   **並於 `check_state_consistency` 增一項比對**：`feature.yaml` 之 `delivery.sha256` 與 `DELIVERY_NOTE.md` 抬頭所載 SHA256 須相等
   —— 此為既有檢查之範圍擴充，非新程式；附故意失敗。

### 核可 R-PMH154 後

5. 抄錄 R-PMH154 入 `RULINGS.md`（核對表同 39a 步驟 1 之格式）；R-PMH152 條後加沿革附註。
6. A-PMH25 依 (a) 改；`DECISIONS.md` 第 10 筆依 (b) 改；`DELIVERY_NOTE.md` 依 (b)(c)(d) 改，
   §8.2 之項次引用一併更正；§8 標題數字不變（11 筆，第 10 筆本已在 §8.2）。
   `DELIVERY_NOTE.md` §1 統計數字**一字不動**。

### 核可 R-PMH155 後

7. 抄錄 R-PMH155；依 (b) 映射六批 `generated/final/`，出示 42 處之前後對照；依 (c) 跑 C7 並出示逐處結果。
8. 六批 lint 重跑（含 R-PMH153 之語言檢查）；`desc_coverage`、`check_granularity --self-test`、`verdict_form`、`check_table` 重跑；
   依 (d) 產出 rev4，母本 SHA256 前後比對；依 (e) 改 `feature.yaml`；`DELIVERY_NOTE.md` 抬頭改 rev4，rev3 之作廢句比照 rev2 之寫法。

---

## 六、39a.7 第 5 項所求之比例（分析層算出，執行層複算）

48 leaf 全集：45 有 TC、1 停手（`-023`）、2 依裁定結案（`-002`／`-028`）。
**3/48 = 6.25% 之 leaf 無行為驗證**；另 4 條 TC 封鎖（`-045`～`-048`，leaf `-026-01`～`-04`，4/48 = 8.33% 之 leaf 有 TC 而不可執行）。
二者相加 **7/48 = 14.58% 之 leaf 於交付時無可執行之驗證**。
執行層複算後寫入 `DELIVERY_NOTE.md` §10（驗證狀態）末段，**只記數字與其組成，不加評語**。

---

## 七、停止條件

canon §0 六條，另加本包六條：

7. §四之重算與本表任一格不符
8. 映射後任一處引用之所指 `leaf_id` 與引用處之語意不相容（C7 FAIL）而被放行
9. `generated/batch0N.json`（provisional 版）任一 byte 被改動
10. rev4 之母本 SHA256 前後不同
11. 未經 Pei 核可而執行步驟 5–8
12. `DELIVERY_NOTE.md` §1 之任何統計數字因本包而變

**apparatus 維持凍結**（`check_state_consistency` 之增項為既有檢查之範圍擴充，須於上繳具名其與 R-PMH104 之界線）。
**本包未由分析層授權提交（R-PMH65）；git 屬 Pei。** 39 包建議之 pathspec 須併入本包之 rev4 異動後重列。

---

## 八、上繳要求（`docs/upstream/40_crossref_and_a_pmh25.md`）

1. §四重算表 ＋ 逐格比對結果
2. §2.3 之實測與判定
3. 39b 收錄之各項（步驟 3）
4. `feature.yaml`／`DELIVERY_NOTE.md` 一致性檢查之增項 ＋ 故意失敗輸出
5. （核可後）R-PMH154／155 之抄錄核對表；A-PMH25／第 10 筆／§8.2／§9 之修訂後原文
6. （核可後）42 處引用之前後對照表 ＋ C7 逐處結果；rev4 之 SHA256、母本前後 SHA256、四項不變量、zip member 差異
7. §六之複算結果
8. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 揭露表
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 九、待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **R-PMH154** | 核可與否 | 交付文件之 §9 第 8 項為不實揭露 —— **出貨前置** |
| **R-PMH155** | 核可與否 | rev3 之 I 欄 42 處引用錯指 —— **出貨前置** |
| `Cover` 作者欄 | 填值或裁定留空（39 包 §5 停手至今） | 出貨前置 |
| commit 授權 | 39＋39a＋39b＋40 累積未提交 | 否 |

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 | 生效 |
|---|---|---|---|
| R-PMH154 | R-PMH152 第 10 筆撤回；A-PMH25 回 `RESOLVED`；§9 第 8 項移除 | ✅ | 待核可 |
| R-PMH155 | 交叉引用位移重掃；rev3 作廢；rev4 | ✅ | 待核可 |

二條各管一事。**本包後未決清單仍 11 筆**（第 10 筆本已在 §8.2，只改結案詞）；停手 1；封鎖 4；統計數字全數不變。
