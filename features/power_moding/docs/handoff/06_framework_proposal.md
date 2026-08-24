# 下放包 06 —— 兩項停止條件之處置、Layer 2 提案與跨規格缺口

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/06_framework_proposal.md`
- 前一包：[05](05_corpus_fix_and_framework_prep.md) ＋
  [05a](05a_upstream_naming_scope.md) ＋ [05b](05b_q3_final.md)
  （上繳 [../upstream/05_corpus_fix_and_framework_prep.md](../upstream/05_corpus_fix_and_framework_prep.md)，已覆核）

---

## 一、05 包之覆核結果

**通過，且兩項停止條件之觸發皆為正確觸發。** 三項特別記明：

1. **§4.2 之 `_Rebuilt` 為本輪最有價值之一項** —— 它指出 R-PMH19 (b) 之
   字面比對「選中了資料較少（211 vs 527）且檔名拼錯（`EngeeringMode`）的那一份」。
   這是**判準本身在做它沒被授權做的判斷**，而非資料有誤。
2. **§7.1 之 TSV 結構缺陷自陳** —— `section_title` 含實體換行與 `_x000D_`，
   未正規化即寫入 TSV，致列被拆開。自行識出、修正、並**加寫出後之回讀自檢**
   （不以「寫出成功」為通過）。與 A-PMH08 同族之第二例。
3. **§9 第 5 項之誠實** —— 明說 §3 之計數部分倚賴分析層之量測而未複驗，
   依通則 5 為「被取代而非被複驗」。

---

## 二、停止條件 7（母體 17 ≠ 16）之處置

### 2.1 差異歸屬：我漏了第 17 個

`Engineering Mode/App Team Effort/…_SWQT_CFTS011_EngMode.xlsx` 確實存在，
(a′) 生效後與那五個一併回到母體，而我 05 包 §3.2 之補測清單只列了五個。
**這是我的列舉遺漏**，不是執行層之計算差異。

### 2.2 但 (a′) 之字面把工作子目錄當成了交付夾

執行層 §9 第 2 項已指出：`App Team Effort/` 內四檔為
`CFTS011_EngMode`(258)→`20251222(Refine)`→`20260129(Revise)`→`20260416(done)`(296)
之遞進，而**其成品以 `20260429`(296 列) 出現在父層 `Engineering Mode/`** ——
其形態是**工作子目錄**，其產出被拔擢至父層交付。

(a′) 只排除「用途目錄」，未處理「同一 feature 之多層目錄」，故它成了
獨立 group。**這是 R-PMH24 之缺口，不是執行層之誤判。**

### 2.3 裁定

依 R-PMH28（§四），`App Team Effort/` 為 `Engineering Mode/` 之下層目錄，
其 036 依 (c) 視為同夾舊版而排除。**母體回到 16**，
`D5` 計數回到 **9 空 / 7 非空**，**R-PMH27 所載之數字成立，其勘誤附註撤除**。

---

## 三、停止條件 8（`_Rebuilt` 之排除理由不成立）之處置

### 3.1 執行層之判斷正確，但其自律使問題懸著

執行層刻意不測 `_Rebuilt` 之 `D3`／`D4`／`D5`，理由是「測了會產生把被排除者
數據併入母體之誘惑」。**自律正確，但它讓一個可以被關掉的不確定性繼續開著。**

**正確作法是第三條路：測全部候選，然後證明結論對該不確定性不敏感。**
測量本身不是把它併入母體 —— 併入才是。

### 3.2 分析層實測

**量測條件**：`…/Engineering Mode/…_EngMode_20260816_Rebuilt.xlsx`，
`openpyxl` `data_only=True` 唯讀。

| 項 | `EngeeringMode_20260816`（現入母體） | `_Rebuilt_20260816`（現被排除） |
|---|---|---|
| 分頁 | `…&Result` | `…&Result` |
| 欄數 | 35 | 35 |
| `Cover!D6` | `A` | `A` |
| 資料列 | 211 | **527** |
| `D3` | 空 | **空** |
| `D4` | 空 | **空** |
| **`D5`** | **空** | **空** |

**兩個候選之三欄皆空。** 故：

> **無論 `Engineering Mode` 之交付態是哪一份，Q3 之計數皆不變**
> （該夾恆計為「`D5` 空」1 份）。**該不確定性對 Q3 之結論不敏感。**

**停止條件 8 得以解除，而不需要判定他 feature 之交付態** —— 那件事本來就不
在本 feature 之權限內（與 R-PMH26 同一道理）。

### 3.3 (b) 清單本身要改

執行層指出兩處：

- **`_Rebuilt`** 之字面語意為「已重建」，是**成品**之語意；把它列為中間態標記，
  等於讓字串比對去判定交付態。**自 (b) 移除。**
- **`(done)`** 之字面語意為「完成」，與「中間態」相反；其排除之實際依據是
  「工作目錄內之階段快照」，而該情形由 R-PMH28 之下層目錄規則涵蓋。
  **自 (b) 移除。**

移除後 (b) 僅保留語意明確為未完成態者：`(Review)`／`(Revise)`／`(Refine)`／
`pre_writeback`／`pre_fullwrite`／`pre_final`。

**移除之影響已驗**：`_Rebuilt` 與 `(done)` 兩檔改由 R-PMH28 之下層目錄規則
或 (c) 之同夾舊版規則排除，**母體仍為 16**（`Engineering Mode` 夾恆取一份，
且無論取哪一份，其三欄皆空）。

---

## 四、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH28（多層目錄之交付夾判準，補 R-PMH24 之缺口）
同一 feature 之交付夾若有下層目錄亦持有 036，取**最上層**持有該 feature
036 之目錄為其交付夾；下層目錄之 036 依 (c) 視為同夾舊版，具名排除。

判準：下層目錄之 036 與上層之現行交付件，其 `Requirement or Design ID`
欄之值域屬同一 feature 者，即為同一交付夾之多層結構。

本條不適用於 (a′) 所列之用途目錄 —— 那些不論層數一律排除。

依據：`Engineering Mode/App Team Effort/` 內四檔為 258→296 之遞進，
其成品以 `20260429`(296 列) 出現於父層，形態為工作子目錄而非交付夾。
R-PMH24 之 (a′) 只處理用途目錄，未處理同 feature 之多層結構。
```

```
R-PMH29（不確定性之處置方式）
當某判準之適用結果不確定，且該不確定性之解決須判定**他 feature 之交付態**
或其他本 feature 無權判定之事項時，不得任選一案，亦不得擱置。

處置為：**量測全部候選**，並就當前結論做敏感度陳述 ——
(a) 各候選皆導致同一結論者，記明「結論對此不確定性不敏感」，該不確定性
    即不必解決，並具名記載其存在；
(b) 不同候選導致不同結論者，停並上呈，附各候選之結論。

量測候選不等於將其併入母體；併入才是。以「測了會有併入之誘惑」為由
不測，會讓一個可關閉之不確定性繼續開著。

依據：`Engineering Mode` 兩候選（211 列 vs 527 列）之 `D3`／`D4`／`D5`
實測皆空，Q3 之計數對該夾之取捨不敏感（分析層 06 包 §3.2）。
```

```
R-PMH30（母體揭露須含量測時點）
R-PMH19 之揭露義務增列一項：**母體之量測時點**（日期與時分）。

依據：`ASW-R2` 為活動中之目錄，04 包量得候選 28、05 包量得 32，
兩者皆正確，差別只在時點（新增之 4 檔為併行 session 於 04 包之後產生之
寫回前備份）。未載明時點者，兩份上繳之數字無法對得起來。
```

```
R-PMH31（R-PMH19 (b) 清單之收斂）
R-PMH19 (b) 之中間態標記清單移除 `_Rebuilt` 與 `(done)` 兩項，
保留者為語意明確表示未完成之標記：
`(Review)`／`(Revise)`／`(Refine)`／`pre_writeback`／`pre_fullwrite`／
`pre_final`。

理由：`_Rebuilt`（已重建）與 `(done)`（完成）之字面語意皆為成品，
以其為中間態標記，等同讓檔名字串去判定交付態 —— 而該判定不在
判準之授權範圍內。二者所涉之檔案改由 R-PMH28 或 (c) 排除。
```

---

## 五、Layer 2 提案（framework）—— **待 Pei 裁定**

依 canon §4.1.2，取**規格目次**與**RD 分群（FROP）**之交集；
資料來源為 `data/layer3_sections.tsv`（48 列，執行層產出）。

### 5.1 提案：8 個 Test Set

| # | Test Set | leaf | Layer 3（規格章節） | 主要 FROP |
|---|---|---:|---|---|
| 1 | `Splash Screen` | 3 | 7.1（部分）、7.9 | Customizable Splash |
| 2 | `Disclaimer Screen` | 7 | 7.1（部分）、7.2、7.3、7.4、10.4（部分） | Disclaimer screen |
| 3 | `Startup Animation` | 9 | 7.5、7.5.1、7.6、7.7、7.8 | Customizable Splash |
| 4 | `Startup Sounds` | 6 | 8.1、8.2、8.2.1–8.2.3、8.3 | Audio Management |
| 5 | `Power Transitions` | 7 | 7.1.1、9.1、10.5 | Power Management／FOTA／WiFi／EV-PHEV |
| 6 | `Power Off Behavior` | 8 | 10.1、10.2、10.3、10.4（部分）、10.6、10.7 | RVC／Climate／BT／e-call |
| 7 | `Voice Assistant Key` | 5 | 11.1 | Steering Wheel Controls |
| 8 | `Off Road Plus` | 3 | 12.1、12.2、12.3 | Power Management／Audio |

**48 = 3+7+9+6+7+8+5+3，餘數 0**（R-G10）。

### 5.2 逐 leaf 分配（供核對，執行層須以 TSV 重算後比對）

- **1 Splash Screen**：`001-01`、`001-02`、`011`
- **2 Disclaimer Screen**：`001-03`、`001-04`、`001-05`、`003`、`004`、`005`、`022-02`
- **3 Startup Animation**：`006-01`、`006-02`、`006-03`、`007`、`008-01`、`008-02`、`009-01`、`009-02`、`010`
- **4 Startup Sounds**：`012`、`013`、`014`、`015`、`016`、`017`
- **5 Power Transitions**：`002`、`018-01`、`018-02`、`018-03`、`018-04`、`018-05`、`023`
- **6 Power Off Behavior**：`019`、`020`、`021`、`022-01`、`024-01`、`024-02`、`024-03`、`025`
- **7 Voice Assistant Key**：`026-01`~`026-05`
- **8 Off Road Plus**：`027`、`028`、`029`

### 5.3 三處須說明之切法

1. **7.1 之五個 leaf 拆入兩個 Test Set**（`001-01/02` → Splash、
   `001-03/04/05` → Disclaimer）。依據為 FROP 欄之既有分群 ——
   **這是上游 RD 之切法，不是我重新分解**（§8.2 禁止 TC 作者重新分解 RD）。
2. **10.4 之兩個 leaf 拆入兩個 Test Set**（`022-01` → Power Off Behavior、
   `022-02` → Disclaimer）。同上，依 FROP。
3. **章 9 之五個 leaf 全歸 `Power Transitions`**，雖其 FROP 有四個值
   （Power Management／FOTA／WiFi／EV-PHEV）—— 因其同屬 9.1 一節，
   共用「IGN OFF 時之 popup 與 Power Accessory Delay」之同一觸發情境，
   合乎 §4.2「同一 Test Set 應共用 setup 與 UI 進入路徑」。

### 5.4 **一處與 canon §4.2 相衝，須 Pei 裁**

§4.2 明訂 Test Set **不得重複 Test Group 之字樣**。而依 R-PMH13，
本 feature 之 Test Group 為 **`Disclaimer screen`**，
提案之 Test Set #2 為 **`Disclaimer Screen`** —— **字面重複**。

此衝突源於 R-PMH13 使 Test Group 取交付夾名（FROP 標籤）而非模組名：
交付夾名恰好等於其中一個能力群之名稱。

| 案 | Test Set #2 之名 | 代價 |
|---|---|---|
| （甲） | `Disclaimer Screen` | 與 §4.2 字面相衝；但讀者一望即知其內容 |
| （乙） | `Acceptance Screen` | 合 §4.2；但 `Acceptance` 非規格用語，屬自創（§8.4.1 之精神） |
| （丙） | 併入 `Splash Screen`，成 7 個 Test Set | 合 §4.2；但把 10 個 leaf 併為一組，且混合兩個 FROP |

**分析層提案（甲）**，理由：§4.2 禁止重複之目的是避免冗餘
（`Bluetooth` 群下寫 `Bluetooth Connection`），而此處 Test Group 是**交付夾標籤**
而非能力名，重複並不製造冗餘資訊。惟此為 §4.2 之字面例外，**須 Pei 裁定**，
不由分析層自行豁免 canon。

---

## 六、新發現 —— `SWE1-HMI-PM-028` 指向已交付 feature 之規格

`layer3_sections.tsv` 第 12.2 節之 `section_title` 逐字為：

> `OFF2.) Please refer to CFTS009 for complete behavior.`

該 leaf **本身不含任何可驗證之行為**，其行為定義在 **CFTS009** ——
而 CFTS009 正是**已交付之 `features/power`（Power Management）之來源規格**。

**這是 canon §8.4.2（no scope fabrication）之典型情形**：
行為定義於外部規格者，屬該規格之 SWE 需求，不得吸收進本 feature 之 TC。
但本 leaf 又確實在本 feature 之 48 個 Functional Requirement 之內
（R-PMH1 之判準），不能不涵蓋。

**登記為 A-PMH13**，三種可能處置並列（**本包不裁**）：

- (i) 撰寫一條僅驗證「該行為存在且與 CFTS009 一致」之 TC，
  `specification_reference` 同時列 12.2 與 CFTS009 之對應節；
- (ii) 依 §8.4.2 判為 out of scope，於 `reasoning` 記為 coverage gap
  並指向 `features/power` 之對應 TC；
- (iii) 開 DR 詢問上游該 leaf 是否應存在於本報告。

**須先查 `features/power` 之已交付 283 條是否已涵蓋該行為** ——
若已涵蓋，(ii) 成立且無缺口；若未涵蓋，則為真缺口。**此查證列為步驟 4。**

---

## 七、待 Pei 之其他項

| # | 事項 | 阻斷 |
|---|---|---|
| Q10 | `Product Document 記錄封面頁!B7` —— 母本為空，16 檔母體中 12 檔填 `Confidential`。若須填，**本 feature 之 `write_back` 範圍將不只 `Test Case Specification` 一個分頁**，而現行 `feature.yaml` 只描述該一分頁 | 否，Phase 7 前決定即可 |
| Q11 | §5.4 之 Test Set #2 命名（甲／乙／丙） | **是** —— Layer 2 定版前 |
| — | A-PMH06 canon 層（`new_feature.py` 樣板） | 否，PENDING-CANON |

---

## 八、作業步驟

1. **抄錄** —— §四之 R-PMH28 ~ R-PMH31 逐字抄入 `RULINGS.md`，附核對表。
   **撤除 R-PMH27 條後之勘誤附註**（母體 16 成立），改記「經 R-PMH28 定案，
   母體 16，原載數字成立」。R-PMH19 (b) 依 R-PMH31 加註（**原文不改字**）。

2. **母體重算複驗** —— 依 R-PMH24 ＋ R-PMH28 ＋ R-PMH31 重篩，
   **須得 16**；載明量測時點（R-PMH30）。排除清單逐項反向覆核（R-PMH24 之義務），
   並確認 `_Rebuilt` 與 `(done)` 兩檔之新排除理由成立。

3. **Layer 2 之機器複算** —— 以 `data/layer3_sections.tsv` 重算 §5.2 之
   逐 leaf 分配，驗 48/48、各 Test Set 之計數與 §5.1 相符、餘數 0。
   **不符者以 TSV 為準並回報差異。** 產出 `framework.md`（Layer 1 ＋ Layer 2
   ＋ Layer 3 對照表），**Test Set #2 之名暫記 `<PENDING Q11>`**，不預填。

4. **A-PMH13 之查證** —— 讀 `features/power` 之已交付 283 條，
   查其是否已涵蓋 `OFF2` 所指之「Off Road+ 期間之 power moding 行為」。
   回報：命中之 TC ID 與其 `specification_reference`；若無命中，明言「零命中」。
   **不裁定處置**（(i)/(ii)/(iii) 由 Pei 或後續包決定）。
   **只讀 `features/power`，不得修改其任何檔案。**

5. **Q10 之影響評估** —— 若 `Product Document!B7` 須填，
   列出 `feature.yaml` 之 `write_back` 需增補之項目（分頁、儲存格、DV 約束），
   **只列不改**。

---

## 九、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 之母體 ≠ 16
8. 步驟 3 之 Layer 2 複算與 §5.2 不符，且差異非「TSV 為準」可解者
9. 步驟 4 發現 `features/power` 之涵蓋狀態無法判定（既非命中亦非零命中）

**本包零寫回工作簿。** 全部改狀態 git 屬 Pei（R-G5）。
**不得改動 `scripts/new_feature.py`，不得修改 `features/power` 之任何檔案。**

---

## 十、上繳包要求（`docs/upstream/06_framework_proposal.md`）

1. §四四條之抄錄核對表 ＋ R-PMH27 勘誤附註撤除之證明（R-PMH27 原文 SHA256 未變）
2. 步驟 2 之母體 16 ＋ 量測時點 ＋ 排除清單逐項覆核
3. 步驟 3 之 Layer 2 複算結果 ＋ `framework.md`
4. 步驟 4 之 `features/power` 涵蓋查證（命中 TC ID 或「零命中」）
5. 步驟 5 之 Q10 影響清單
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
7. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之唯讀／改狀態分列

---

## 十一、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-PMH28 | 多層目錄之交付夾判準（取最上層） | ✅ |
| R-PMH29 | 不確定性以敏感度處置，量測全部候選 | ✅ |
| R-PMH30 | 母體揭露須含量測時點 | ✅ |
| R-PMH31 | (b) 清單移除 `_Rebuilt` 與 `(done)` | ✅ |

四條各管一事。R-PMH31 為**收斂型**，其移除之兩項改由何條涵蓋已於條內載明。

**待 Pei 者二項**：Q11（Test Set #2 命名，阻斷 Layer 2 定版）、
Q10（`Product Document!B7`，不阻斷）。
