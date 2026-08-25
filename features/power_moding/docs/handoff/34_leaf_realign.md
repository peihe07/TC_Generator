# 下放包 34 —— 射程之比對欄更正、`-017`／`-018` 之 leaf 更正、`-024` 之撤除

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/34_leaf_realign.md`
- 前一包：[33_batch4_rework.md](33_batch4_rework.md)
  （上繳 [../upstream/33_batch4_rework.md](../upstream/33_batch4_rework.md)）

---

## 一、33 包之覆核 —— **通過，且停止條件 8 之觸發極有價值**

五條抄錄相符；限定改由旗標決定而**樣板在結構上已不可貼**；
`-035` 之矛盾隨限定移除而消失；四批 lint 32/32。

**三項採認**：

1. **限定三筆而非五筆 —— 你對。** `SU9.)` 逐字為
   `Pressing "Screen Off" or "Power Off" hard key **will not do anything** when
   pressed during animation.` —— **「不做任何事」不與任何斷言取相反值**，
   故 `-028`／`-029`／`-032` 無須限定。
   而 `-027` 之保留亦對 —— `SU9.1)` 後半
   `the radio shall display the screen the next time the screen turns on`
   與其「不再顯示」相反，**我 33 包把它歸入「無逾時斷言」而漏看了後半句**。
2. **`-023` 之狀態詞維持不改 —— 你對。** 其**仍在交付範圍內**，
   與判 out of scope 之 `-002`／`-028` 不同類；
   **標 `ACCEPTED` 會讓人以為它已被裁定不寫入，而它沒有。**
   該區別正是 R-PMH119(b) 所分者。
3. **停止條件 9 之字面觸發判斷正確** —— 母體來源已改 glob 而規模不變
   之成因為「32 包已把列舉補齊」，**差別要到第五批才可觀測**；
   且主動釐清 `33→22` 是限定筆數所致而非本步之產物。

---

## 二、停止條件 8 之五處 —— **我複驗了，兩處成立、三處不成立，而錯在我令錯了欄**

### 2.1 決定性之量測：**`Requirement Title` 不是射程，`Requirement Description` 才是**

R-PMH125 令「驗其射程與其 leaf 之 **`requirement_title`** 相符」。
**我令錯了欄。** 037 之 `Requirement Description` 才載其範圍。

**實測**（037 `Analysis Report`）：

```
-001-01  title: Startup Animation on Driver Door Close
         DESC : When driver door is closed, the system plays a 3-second startup
                animation. If ignition remains OFF after animation, the system
                turns the screen black.

-008-01  title: Single Animation per CAN BUS Wake Up
         DESC : If the ignition cycle has not changed, the system shall play the
                animation only once per CAN BUS wake-up upon closing the driver door.
```

### 2.2 逐處判定

| # | 執行層之指摘 | 分析層複驗 |
|---|---|---|
| **`-017`** 掛 `-018-01` | 應在 `-018-02` | **成立** —— `-018-02` 之 DESC 為 `If the user interacts with the FOTA popup, the system shall stay awake until … 60 seconds. The maximum … is 10 minutes.`，**與 `-017` 逐項相符**；`-018-01` 之 DESC 為 2.5 分鐘與 60 秒逾時，**是 `-016` 之標的** |
| **`-018`** 掛 `-018-02` | 應在 `-018-03` | **成立** —— `-018-03` 之 title 為 `Pop-up Priority 1: FOTA Update Available`，即接受／排程／取消之分支 |
| `-025` 掛 `-001-01` | title 為「動畫」而 TC 為黑螢幕 | **不成立** —— `-001-01` 之 **DESC 第二句逐字為 `If ignition remains OFF after animation, the system turns the screen black.`**，`-025` 正是其標的 |
| `-032` 之單位 | 037 已替我選 `CAN BUS Wake Up` | **不成立** —— **DESC 兩個單位皆在**（`If the ignition cycle has not changed … only once per CAN BUS wake-up`），**037 未替任何人選**；title 與 DESC 之不一致屬上游，依 R-PMH26 只登記 |
| **`-024`** 掛 `-001-01` | title 為「動畫」而 TC 為 splash | **成立，且其理由更深** —— 見 §2.3 |

**五處中兩處成立、三處為 title 之偽陽** —— **偽陽之成因是我令錯了欄。**

### 2.3 `-024` —— **它是為一個沒有 leaf 的句子寫的 TC，而那是我要求的**

`SU1.)` 之四個子句與其 leaf：

| 子句 | leaf |
|---|---|
| 門關閉 → 3 秒動畫 | `-001-01`（DESC 第一句） |
| **動畫後 → splash 呈現，1.5 each** | **無** ← **A-PMH03 之漏句** |
| 點火維持關閉 → 黑螢幕 | `-001-01`（DESC 第二句） |
| 點火於動畫期間開啟 → splash | `-001-02` |

**第二句於 SYS1 0 命中 → 037 無對應 outline → 無 leaf。**

**而 `-024` 正是為該句所寫。** 依 **R-PMH55(b)**（無 leaf 之規格內容
不得為其撰寫 TC），**`-024` 不應存在**。

**其成因是我 32 包 §4.2(a)** —— 我令「`-001-01`／`-001-02` 之 `source_clause`
**須含該子句**」，**而該指示與 R-PMH55(b) 直接相衝**。
**執行層依指示照做，錯不在它。**

**且此事已有前例**：`-028`（12.2）之行為定義於外部而無可驗內容 →
R-PMH72 裁定不寫入。**A-PMH03 之漏句形態相同 —— 上游未納入，故無 leaf，故無 TC。**

→ **`-024` 撤除**，其內容登記為覆蓋缺口。**32 包 §4.2(a) 撤回。**

---

## 三、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH127（射程之比對取 `Requirement Description`）
TC 射程與其 leaf 之比對，**取 037 之 `Requirement Description` 欄**，
**不取 `Requirement Title`** —— title 為標籤，DESC 為範圍。

**R-PMH125 之比對欄更正**：該條「驗其射程與其 leaf 之
`requirement_title` 相符」**撤回**，改為 DESC。
**其增欄之要求保留並擴充**：`layer3_sections.tsv` 增
`requirement_title` **與 `requirement_description` 兩欄**。

依據：33 包依 R-PMH125 以 title 比對得五處不符，
**分析層以 DESC 複驗，其中三處為偽陽**：
  `-025` —— `-001-01` 之 DESC 第二句逐字為
    `If ignition remains OFF after animation, the system turns the screen black.`，
    `-025` 正是其標的；
  `-032` —— `-008-01` 之 DESC **兩個單位皆在**
    （`If the ignition cycle has not changed … only once per CAN BUS wake-up`），
    037 未替任何人選；其 title 與 DESC 之不一致屬上游（R-PMH26，只登記）。

**偽陽之成因為分析層令錯了欄**，非執行層之判讀。
```

```
R-PMH128（`-017`／`-018` 之 leaf 更正）
batch 3 之 `-017` 由 `SWE1-HMI-PM-018-01` 改掛 **`-018-02`**；
`-018` 由 `-018-02` 改掛 **`-018-03`**。

依據（037 `Requirement Description`）：
  `-018-02` = `If the user interacts with the FOTA popup, the system shall stay
    awake until the user has not interacted with the popup for 60 seconds.
    The maximum time … is 10 minutes.` —— **與 `-017` 逐項相符**；
  `-018-01` = 2.5 分鐘與 60 秒逾時 —— **為 `-016` 之標的**；
  `-018-03` = `Pop-up Priority 1: FOTA Update Available` —— **為 `-018` 之標的**。

**本更正不計入 batch 3 之輪數上限（R-PMH120）** ——
**更正一個事實錯誤不是重做一批**；其計入者為產出面之覆核循環。

**分析層之覆核責任記明**：batch 3 於 31 包經分析層覆核通過，
**而該次覆核未查 leaf 與 DESC 之對應** —— 其為分析層之遺漏。
`requirement_title`／`requirement_description` 兩欄不存在時該項不可查，
**惟不可查不等於已查**。
```

```
R-PMH129（`-024` 撤除；32 包 §4.2(a) 撤回）
batch 4 之 `-024`（`SU1.)` 之「動畫後呈現 splash，1.5 each」）**撤除**，
不寫入交付工作簿。

依據：該子句於 SYS1 匯出 **0 命中**（A-PMH03），037 因而**無對應 outline、
無 leaf**；依 **R-PMH55(b)**，無 leaf 之規格內容**不得為其撰寫 TC**。

**32 包 §4.2(a)（令 `-001-01`／`-001-02` 之 `source_clause` 須含該子句）
撤回** —— **該指示與 R-PMH55(b) 直接相衝，而執行層依指示照做，錯不在它。**
32 包之停止條件 7 一併失效。

**其內容登記為覆蓋缺口**（比照 `-028` 之 R-PMH72、A-PMH03 之既有登記），
**併入 `DR-PMH8`** —— 其問題為：該子句是否應納入 037？
若上游確認應納入，則其成為新 leaf，`Splash Screen` 組由 3 增為 4，
`-024` 屆時重寫。

**`-025`／`-026` 不受影響** —— 二者各有其 leaf（`-001-01` 之 DESC 第二句、
`-001-02`），其 `source_clause` 各取其所驗之句（R-PMH122）。

batch 4 由 14 條減為 **13 條**；`Splash Screen` 組為 **2 leaf 有 TC**
（`-001-01`／`-001-02`）＋ `-011`，合 3 leaf。
```

```
R-PMH130（`-023` 之狀態詞維持，不改 `ACCEPTED`）
`-023`（`PITA8`）之 anomaly 狀態詞**維持不改為 `ACCEPTED`**。
**採認執行層 33 包之判斷，分析層 33 包步驟 4 所令之一併改動撤回。**

其理由成立：`-023` **仍在交付範圍內**，其停手繫於 `DR-PMH5` 之答覆
（R-PMH111 之條件式），**與經裁定不寫入之 `-002`／`-028` 不同類**；
**標 `ACCEPTED` 會使人以為它已被裁定不寫入，而它沒有。**
該區別正是 R-PMH119(b) 所分者。

**三筆之狀態詞自此不同而各有其理由**：
  `-002`／`-028` → `ACCEPTED`（經裁定不寫入，其缺口事實不消失）；
  `-023` → 維持其原狀態（**待 DR 答覆，仍在範圍內**）。
```

---

## 四、作業步驟

1. **抄錄** —— §三之 R-PMH127 ~ R-PMH130 逐字抄入 `RULINGS.md`，附核對表。
   **R-PMH125 之比對欄撤回、32 包 §4.2(a) 撤回、33 包步驟 4 之一併改動撤回**，
   三者各加附註（**原文不改字**，R-PMH44）。

2. **TSV 增 `requirement_description`（R-PMH127）** —— 48 列全數。

3. **四批之射程重驗（以 DESC）** —— 33 包之 23 條 title 比對作廢，
   **改以 DESC 重驗全 43 條**（batch 1 8 ＋ batch 2 7 ＋ batch 3 8 ＋ batch 4 13 之修正後）。
   **發現任一不符即停並上呈** —— 不自行改掛。

4. **`-017`／`-018` 之改掛（R-PMH128）** —— 其 `reasoning` 之
   `distinguishing_axis` 與 leaf 引用一併更新；**batch 3 重跑 lint**。

5. **`-024` 之撤除（R-PMH129）** —— 自 `batch04.json` 移除，
   其內容寫入 `ANOMALIES.md` 之覆蓋缺口；`DR-PMH8` 增問
   （**與 A-PMH28 之第六問合為一節或分立，由執行層擇一並載理由**）；
   batch 4 之 tc_id 不重編（provisional，末次統一指派）。

6. **33 包 §5 第 2 項之「單位」比對** —— 037 之 DESC 於多處指定單位
   （`per CAN BUS Wake Up`／`per CAN BUS Cycle`／`Ignition Off`），
   **對全 43 條驗其單位與 DESC 相符**，不符者具名。

7. **33 包 §5 第 3 項** —— batch 1 之七項、batch 2 之十二項限定**是否亦為樣板**，
   依 R-PMH126 逐條查其 `reasoning` 是否具名該條之**該一個** ER 斷言。
   **本輪只查與具名，不改** —— 其修正待下輪，以免與本輪之改動相混。

---

## 五、停止條件

canon §0 六條，另加本包三條：

7. 步驟 3 之 DESC 重驗發現**任一**不符（不限於新的 —— 其為追溯正確性）
8. 步驟 6 之單位比對發現**任一**不符
9. `-024` 撤除後，`Splash Screen` 組之 leaf 計數 ≠ 3（其中 2 leaf 有 TC）

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**apparatus 維持凍結。**
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 六、上繳包要求（`docs/upstream/34_leaf_realign.md`）

1. §三四條之抄錄核對表 ＋ 三處撤回之附註（原文 SHA256 未變之證明）
2. TSV 增欄後之 48 列
3. **步驟 3 之 43 條 DESC 射程重驗全表**
4. `-017`／`-018` 改掛後之 batch 3 ＋ lint
5. `-024` 撤除後之 batch 4（13 條）＋ 覆蓋缺口登記 ＋ `DR-PMH8` 增問
6. 步驟 6 之單位比對表
7. 步驟 7 之 batch 1／2 限定樣板查核（**只查不改**）
8. 由程式產生之檢查總表
9. 未結 DR 清單
10. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
11. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 七、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **A-PMH28（流程圖之規範性）** —— 提案：比照 R-PMH55(b) 登記為覆蓋缺口、併入 `DR-PMH8`，不為其撰寫 TC。**其與 `-024` 之處置同型，二者宜一併裁** | 否 |
| 2 | **R-PMH121 之核可**（DR 未覆之交付截止規則） | 交付日 |
| 3 | **`DR-PMH8` 之發出**（現 5 問，擬增至 7 問） | 否 |
| 4 | 9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | Phase 6／7 前 |

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-PMH127 | 射程之比對取 DESC；R-PMH125 之比對欄撤回 | ✅ |
| R-PMH128 | `-017`／`-018` 之 leaf 更正；更正不計入輪數上限 | ✅ |
| R-PMH129 | `-024` 撤除；32 包 §4.2(a) 撤回 | ✅ |
| R-PMH130 | `-023` 之狀態詞維持；33 包步驟 4 之一併改動撤回 | ✅ |

四條各管一事。**本包未新增任何檢查程式或檢查項**（符合 R-PMH104）。
