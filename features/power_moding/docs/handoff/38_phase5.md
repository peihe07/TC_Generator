# 下放包 38 —— Phase 5：`-050`～`-053` 之封鎖、`tc_id` 單次指派與首次寫回

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/38_phase5.md`
- 前一包：[37_batch6.md](37_batch6.md)
  （上繳 [../upstream/37_batch6.md](../upstream/37_batch6.md)）

---

## 一、37 包之覆核 —— **通過，惟 batch 6 有一項嚴重（見 §二）**

三條抄錄逐位相符；`-004` 之處置使反向 `無依據` 由 1 降為 **0**；
正向 60 斷言／45 leaf、未涵蓋 3（皆已裁）；六批 lint 32/32；
priority 全批自套 51/51 不符 0。

**兩項特別記明**：

1. **`-045` 之修正過程中「新犯又同輪更正」** —— 其唯一性宣稱不實，
   自查後改。**修正一個缺陷時新犯一個缺陷，而在同一輪內被自己抓到。**
2. **§5 之限度自陳** —— priority 全批自套為**一次性**，
   **「下一批不會自動再做，而 `-045` 之矛盾正是因為 batch 1 有 `self_check`
   而其餘沒有」**。其取捨（apparatus 凍結故未擴及）已具名。

---

## 二、`-050`～`-053` —— **四條互斥而 procedure 相同，至多一條能過**

### 2.1 事實

| tc | leaf | ER |
|---|---|---|
| `-050` | `-026-02` | 螢幕 **開**／音訊 **關** |
| `-051` | `-026-03` | 螢幕 **關**／音訊 **關** |
| `-052` | `-026-04` | 螢幕 **關**／音訊 **開** |
| `-053` | `-026-05` | 螢幕 **開**／音訊 **開** |

**四條之 procedure 逐字相同**：`Read the screen state and the audio state
after the interaction` → `Check that …`。

**同一組步驟執行一次只會落在一類 —— 四條之中至多一條能通過，其餘三條必然 fail。**

**其為 canon §7 之 false fail**（測試因設計而非因缺陷而失敗）。

### 2.2 成因不在執行層

執行層 §10 第 2 項已指出：**「規格與 037 皆未言如何控制之」**，
故其未寫入任何使結果落入某類之步驟。

**在無條件可寫時不造值（§8.4.1）是對的。**
**其代價是這四條現在不可執行 —— 而該代價須被記為封鎖，不得被記為通過。**

### 2.3 處置

**四條保留，標 `BLOCKED-UNTIL-DR`**，比照 R-PMH69（來源損壞時凍結該組）
與 R-PMH111（條件式解凍）之形態。

**`DR-PMH8` 增第九問**：`VRLP1` 所列之四種結果，其各自之適用條件為何。

→ R-PMH142。

---

## 三、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH142（`-050`～`-053` 之封鎖）
`-050`／`-051`／`-052`／`-053` 四條標 **`BLOCKED-UNTIL-DR`**，
**其狀態為「已產出、不可執行」**，於交付時隨附其封鎖依據。

依據：四條之 `test_procedure` 逐字相同而其 `expected_result` **互斥**
（螢幕開關 × 音訊開關之四個組合）——
**同一組步驟執行一次只會落在一類，四條之中至多一條能通過，
其餘三條必然 fail**，其為 canon §7 之 **false fail**（因設計而失敗，非因缺陷）。

**成因不在撰寫** —— 規格 `VRLP1` 與 037 之 DESC **皆未言如何使互動之結果
落在某一類**；執行層於無條件可寫時未造值（§8.4.1），其處置正確。
**其代價為該四條不可執行，該代價須被記為封鎖，不得被記為通過。**

**`DR-PMH8` 增第九問**：該四種結果各自之適用條件為何。

**解封條件**：`DR-PMH8` Q9 `ANSWERED` 且其答覆載明各類之條件；
屆時四條各加其條件為 Pre-Condition，`BLOCKED` 解除。
**若答覆為「四者皆為可能之結果而無條件之分」**，則四條**併為一條**
（其 ER 為「結果為所列四類之一」），並以 R-PMH137 之形態於其餘三 leaf
記 `未涵蓋-重複`。**二路皆須屆時另裁，本條不預判。**

**入 `PENDING-ON-DR`**（第 15 筆），第 (3) 欄逐值列出上開二路。
```

```
R-PMH143（`tc_id` 之單次指派規則）
Phase 5 之 `tc_id` 單次指派，其規則四項：

(a) **連續編號，不留空** —— provisional 期間之空位（`-024` 依 R-PMH129
    撤除所遺者）**不保留**；provisional 本為暫號，其連續性無保存價值；
(b) 編號順序依 **Test Set 之 Layer 2 定版順序**（R-PMH36：`Splash Screen` →
    `Disclaimer Screen` → `Startup Animation` → `Startup Sounds` →
    `Power Transitions` → `Power Off Behavior` → `Voice Assistant Key` →
    `Off Road Plus`），組內依其 leaf 之 037 列序；
(c) 格式為 `NR1L-DisclaimerScreen-{NNN}`（R-PMH16），`NNN` 自 `001` 起；
(d) **須產出 provisional → final 之映射表**並落檔於
    `data/tc_id_map.tsv`，其為 TestRail 對應與日後追溯之依據。

**指派後 `tc_id_status` 由 `provisional` 改 `final`**，
`check_write_back` 之第四項（R-PMH104 時期所加之 provisional 防護）
於其為 `final` 時方放行。
```

```
R-PMH144（`and`／`or` 並列之一次性全批掃描）
A-PMH31（`and`／`or` 並列之語意未定）之範圍**擴及全六批**，
以**一次性人讀**為之，**不建檢查程式**（apparatus 凍結，R-PMH104）。

其產出為一份清單：逐項載該 TC、其並列之逐字、其兩讀、
以及本 feature 現行採何讀及其理由。
**採「兩讀皆涵蓋之處置」者（R-PMH95）記明之，不必開 DR；
採其一讀而另一讀未涵蓋者，入 `PENDING-ON-DR`。**

依據：37 包 §10 第 3 項 —— 執行層自陳其只查了 batch 6 之四條，
**其餘五批未查**。
```

---

## 四、作業步驟

1. **抄錄** —— §三之 R-PMH142 ~ R-PMH144 逐字抄入 `RULINGS.md`，附核對表。

2. **`-050`～`-053` 之封鎖（R-PMH142）** —— 四條加 `blocked` 旗標，
   `DECISIONS.md` 記其封鎖依據；`DR-PMH8` 增 Q9；
   `PENDING-ON-DR` 增第 15 筆（二路逐值列出）。

3. **`and`／`or` 之全批掃描（R-PMH144）** —— 一次性，六批全數。

4. **`tc_id` 單次指派（R-PMH143）** —— 51 條依 (a)~(d)；
   產出 `data/tc_id_map.tsv`；`tc_id_status` 改 `final`。
   **其後不得再改編號** —— 若後續有 TC 增減，須另裁其編號策略。

5. **`check_write_back` 之首次接線（本 feature 之首次寫回）** ——
   該三項檢查自 04 包實作、經故意失敗驗證後，
   **至今未被任何寫回路徑呼叫**（其自陳為「已知未完成」，見 DECISIONS）。
   **本步為其首次上場**，須：
   (a) 將三項接上寫回路徑，寫回前自動執行，任一失敗即中止；
   (b) **接線後先跑一次故意失敗**（於暫存副本上令 `first_row` ≠ 10）
       → 寫回須被攔下；還原後方進行真寫回。

6. **寫回工作簿（Phase 6 之首步）** ——
   目標為 `forms` 母本之工作副本（R-PMH7），自 **r10** 起 append 51 列。
   **四項不變量須於寫回前後各測一次並比對**：
   分頁數、DV 組數（**含 x14**）、`last_capacity_row`、B 欄公式。
   **以 XML 外科式修改為之，不得以 `openpyxl` 存回**（R-G3／R-PMH7）。

   **欄位依 profile §0.1（rev C 34 欄）**：
   `D` req_id／`F` tc_id／`G` `Disclaimer screen`／`H` Test Set／
   `I` test_item／`J` pre／`K` `NA`／`L` proc／`M` ER／`N` specref／
   `P` priority／`R` design_method／`S` `NA`／`AA` author／`AH` remarks。
   **`Q`（Estimated Test Time）留白**（profile §3.6 —— 其 DV 為 priority 之
   `"P0,P1,P2,P3"`，任何分鐘數皆會被 Excel 擋下）。
   **`D3`／`D4`／`D5` 留空**（R-PMH27）。
   **`T`–`Z` 留白**（profile §3.8）。

7. **停手三筆與封鎖四條之處置** ——
   `-002`／`-023`／`-028` **不寫入**（R-PMH72／R-PMH117／R-PMH111）；
   `-050`～`-053` **寫入**（其為已產出，只是不可執行），
   其 `Remarks` 載 `[BLOCKED-UNTIL-DR] DR-PMH8 Q9 — applicable condition for
   each outcome not stated in the specification.`
   **形態沿用 Comfort 之 `[BLOCKED-SPEC]`**（R-PMH47(b) 之同一慣例）。

---

## 五、停止條件

canon §0 六條，另加本包三條：

7. 步驟 5(b) 之故意失敗**未攔下寫回**
8. 步驟 6 之四項不變量有任一項寫回前後不同
9. 步驟 4 之映射表其 provisional 與 final 之筆數不等（應各 51）

**本包為本 feature 之首次寫回** —— **其目標為 repo 內部之工作副本，
非交付路徑**；交付路徑之複製屬 Pei（R-G5 之同一分工）。
**本包未由分析層授權提交**（R-PMH65）。
**apparatus 維持凍結；追溯維度維持封閉為三項。**
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 六、上繳包要求（`docs/upstream/38_phase5.md`）

1. §三三條之抄錄核對表（含命中數）
2. 步驟 2 之封鎖登記 ＋ `DR-PMH8` Q9 ＋ `PENDING-ON-DR`（15 筆）
3. 步驟 3 之 `and`／`or` 全批清單
4. `data/tc_id_map.tsv`（51 → 51）
5. 步驟 5 之接線 ＋ **故意失敗之實跑輸出**
6. **步驟 6 之寫回結果** —— 四項不變量之前後對照、寫入列數、
   工作副本之 SHA256
7. 六批 lint ＋ 檢查總表
8. 未結 DR 清單
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
10. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 七、之後 —— **兩輪**

| 輪 | 內容 |
|---|---|
| 39 | Q10（`Product Document` 分頁，待 Pei）、profile 之 9.1 例外（待 Pei）、`Cover 封面` 署名欄、17 §5.4 其餘五項之結清 |
| 40 | **交付揭露清單**（R-PMH132(b)）：`PENDING-ON-DR` 15 筆 ＋ 停手 3 筆 ＋ A-PMH30 二例 ＋ 封鎖 4 條；`DELIVERY_NOTE.md`；Pei 之 Excel 抽驗與複製至交付路徑 |

---

## 八、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH8`（現 9 問 ＋ 更正句）之發出 ＋ 日期與對象** | 否，惟 Q9 封鎖四條 |
| 2 | **Q10** —— `Product Document 記錄封面頁`（profile §3.10 已預留；提案不填） | **39 輪** |
| 3 | **9.1 之 `source_clause` 例外是否寫入 profile** | **39 輪** |
| 4 | 交付路徑之複製（Pei 手動）；Excel 抽驗 | 40 輪 |

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-PMH142 | `-050`～`-053` 封鎖；其解封二路不預判 | ✅ |
| R-PMH143 | `tc_id` 單次指派四項規則 ＋ 映射表 | ✅ |
| R-PMH144 | `and`／`or` 之一次性全批掃描，不建程式 | ✅ |

三條各管一事。**本包未新增任何檢查程式或檢查項**（符合 R-PMH104）。
