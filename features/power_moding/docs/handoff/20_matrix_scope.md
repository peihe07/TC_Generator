# 下放包 20 —— State Matrix 之定位更正、Off Road+ 之互補分支與兩項停止條件之處置

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/20_matrix_scope.md`
- 前一包：[19_broken_source.md](19_broken_source.md) ＋ [19a_pei_dr_rulings.md](19a_pei_dr_rulings.md)
  （上繳 [../upstream/19_broken_source.md](../upstream/19_broken_source.md)）

---

## 一、19 包之覆核結果 —— **通過，三項觸發皆為正確觸發**

七條抄錄逐位相符；六章殘餘全具名；分割檢查未覆蓋段不含 marker；
granularity 以 47 重跑五項全 PASS 且與對照值逐項相符；
`shasum -c` 6/6；lint 30/30；兩份 fixture 仍 FAIL。

**三項特別記明**：

1. **§3.3 之鍵碰撞** —— 章 9 兩句殘餘之前 60 字元完全相同，
   **一句之人讀結論會被另一句靜默借用，而檢查不會察覺（兩句都「有結論」）**。
   其自評更值得記：**「判準之正確性有時依賴輸入之偶然性質」**
   —— `-layout` 下兩句之前 60 字元恰好不同，故 18 包不會撞上。
2. **§8.4 之「新漏 2 不結清、新漏 3 結清」之分辨** ——
   新漏 3 缺的是**一句指標**，指標所指之物已到 → 結清；
   新漏 2 缺的是**矩陣之內容**，而已到之物不含該內容 → 不得結清。
   **在 R-PMH73 明文寫著「改為 RESOLVED」之下仍拒絕照做，並具名理由。**
3. **§14 六項自評** —— 其第 1 項（「逐字不對應」與「內容不涵蓋」是兩件事，
   我只驗了前者）**直接促成本包 §二之複驗**，且其疑慮方向正確。

---

## 二、A-PMH18 —— 分析層複驗：**執行層之結論成立，而我之 R-PMH73 定位錯誤**

執行層 §14 第 1 項自陳只做了標籤層比對，未做語意層對照，
且指出 `HU on`／`HU off` 確實在該 Excel 內。**我做了語意層之對照。**

**量測條件**：`openpyxl` `read_only=True, data_only=True` 讀
`State Matrix` 分頁全 43 非空列之結構（區塊標題、欄軸、列軸、格內容）。

### 2.1 兩份矩陣之結構對照

| | **PDF p9 之矩陣** | **Excel `State Matrix`** |
|---|---|---|
| 型別 | **靜態能力表** | **事件驅動之狀態轉移表** |
| 列軸 | 電源狀態：`KEY ON ENGINE ON`／`KEY OFF (ACC)`／`KEY OFF (No ACC)` | **事件**：`ON/OFF button Pressed`／`Door opened`／`Incoming Call`／`Plug in Projection`／`VR button long press`／`Call Ended`／`Key-off`／`SRT or Off Road+ Hard Button press`／`Screen Off Button Pressed`／`Mute Button Pressed`／`HVAC Hard Control Adjustment`／`Gear changes to Reverse` … |
| 欄軸 | 受控對象：`ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`，各分 `HEADUNIT POWER OFF`／`ON` | **情境條件**：`Turn Off @ door opening Enabled/Disabled` × `HU on`／`HU off`／`Power Button OFF` × `Call Active/Not Active` × `Door Open/Closed` |
| 格內容 | **是否可用**（`Fully functional`／`Not Visible due to…`） | **轉移後之結果**（`VP Stays ON Pop-up: Cannot Power Off`／`Event ignored`／`Radio Wakes Up and mutes` …） |
| 區塊 | 單一表 | **三塊**：`Key-on`（列 1–16）／`Key-off`（19–33）／`Key On, Gear ≠ Reverse`（37–48） |

**二者主題不同、粒度不同、問題不同。**
p9 問「在某電源狀態下某控制是否可用」；Excel 問「在某情境下某事件發生後轉移到何狀態」。

**結論：該 Excel 不含 p9 之內容。A-PMH18 成立，且不因語意層對照而動搖。**
執行層之停手正確。

### 2.2 但 **R-PMH73 把它定位錯了 —— 錯在我**

R-PMH73 逐字寫「該矩陣自此為 **ch 9（`Power Transitions` 組）之判讀背景**」。
**我在沒有讀過該檔內容之前就寫下了它的效力範圍** ——
依據只是 PDF p10 那句 `Power Moding behavior shall not be developed without
following the Power Moding State Matrix` 與檔名。

**其真正之效力範圍，由內容決定**（見 §三）：
它涵蓋 **ch 12（Off Road+）** 與 **ch 10 之一部**（Screen Off／Mute／HVAC 硬控），
**而非 p9 之能力矩陣**。

---

## 三、**新發現：該 Excel 對 `Off Road Plus` 組有直接效力**

`Off Road Plus` 組（`-027`／`-029`，2 leaf）**未凍結，且為最接近可交付者**。

### 3.1 逐字對照

**PDF `OFF1.)`（`pm.txt` 行 528）**：

> `OFF1.) `**`If vehicle is in Off Road state prior to pressing Off Road+ hard
> control`**` head unit will not initiate wake up (Power Button On).`

**Excel `State Matrix` 列 16**（`Key-on` 區塊）：

| 列 | 欄（`Power Button OFF` × `Call Not Active`） | 格內容 |
|---|---|---|
| `SRT or Off Road+ Hard Button press.` | `Door = Open` | **`Radio Wakes Up and rmutes`** |
| 同上 | `Door = Closed` | **`Radio Wakes Up and mutes`** |

其餘十欄（`HU on` 之各情境）皆為 `-`。

### 3.2 二者不衝突，**但只有在讀出 `OFF1.)` 之條件句時才不衝突**

- `OFF1.)` 之適用條件為「**車輛於按壓前已處於 Off Road state**」→ 不喚醒；
- Excel 列 16 之情境**未含 Off Road state**（其軸為 Power Button／Call／Door）
  → **喚醒並靜音**。

**二者為互補之兩支**：已在 Off Road state → 不喚醒；否則 → 喚醒並靜音。

### 3.3 這對 `-027` 之 TC 是硬要求

若 `-027` 之 Pre-Condition **未載明「車輛已處於 Off Road state」**，
其 ER「不喚醒」即與該矩陣直接衝突 —— 而矩陣是規範性文件
（`shall not be developed without following`）。

**且 Excel 補上了規格文字所無之另一半**：`Radio Wakes Up and mutes`
與 `OFF3.)`（`Head unit is muted when launching app from Power Off State`）
互相印證 —— **`OFF3.)` 假設了「喚醒」這件事而未言之，喚醒之來源在矩陣裡。**

→ **`Off Road Plus` 組開批前，須先完成矩陣對照**（步驟 3）。

---

## 四、停止條件 7 之字面／目的分歧 —— **分析層裁定：不重做 batch 1**

執行層兩面回報（字面觸發／目的不觸發），本層判定「不重做」並交裁。

**採其判定。** 理由三項，皆可查：

1. 殘餘三句**全為已登記且已裁定者**（A-PMH03 之 7.1；A-PMH14 新漏 1
   之 `SU9.)`／`SU9.1)`，後者已由 R-PMH74 裁 `ACCEPTED`），**無新發現**；
2. batch 1 之 `source_clause` 取自 **PDF**（R-PMH50），7.1 之被漏子句
   **在 PDF 內、在 `source_clause` 內** —— batch 1 並非建於失真材料上；
3. `SU9.1` 所生之「不按任何硬鍵」限定，已依 R-PMH55 於 `-003`／`-004`
   落實且 R-PMH74 已確認其適用繼續成立。

**而該分歧本身是我寫停止條件時之缺陷**：我寫「發現**任一**漏字或漏句」，
而我要問的是「發現**新的**漏字或漏句」。**同一形態已於 18 §9 出現一次
（執行層當時即指出「若條件寫成後者，本包會停」），我沒有把那次的指認
回頭套用到我自己後續所寫之停止條件上** —— **R-PMH62 之同型，第三次。**

→ R-PMH77。

---

## 五、停止條件 8 —— **我的 must-hit 前提為假，撤回**

19 包步驟 4 令：「以 `-layout` 跑章 9 → A-PMH16 之三處**查不出**」。
**執行層實測：三個探針於 `-layout` 之殘餘中同樣存在（3/3）。前提為假。**

**我在指定一個 must-hit 之期望結果時，沒有先驗證該期望成立** ——
而 R-PMH35(c) 正是我立的條：must-hit 須「刻意構造之反例，**實跑並證明其 FAIL**」。
**我要求執行層實跑，自己卻用推測寫下了期望值。**

執行層之歸因正確：**真正使 18 包漏掉 A-PMH16 的不是來源，是 13 包之
6-gram 門檻**（R-PMH66 之立條依據）。

**惟 R-PMH71(a) 之改動仍然正確** —— 其成立之鑑別量是執行層 §4.3 所量者：

| 來源 | 章 9 對 SYS1 `9.1` 之字級 diff |
|---|---|
| `layout` | 差異段 **26** 個 |
| `block` | 差異段 **10** 個（38%） |

**A-PMH16 之三處即由 block 層之字級 diff 讀出**；`layout` 側被矩陣格灌爆。

→ R-PMH78：撤回該 must-hit，改為驗 R-PMH71 之**本文主張**（結論可由預設重現），
其形式為二值，不涉門檻。

---

## 六、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH76（State Matrix 之效力範圍更正）
R-PMH73 所稱「該矩陣自此為 ch 9（`Power Transitions` 組）之判讀背景」
**更正**。

實測（分析層 20 包 §2.1）：該 Excel 為**事件驅動之狀態轉移表**
（列軸為事件、欄軸為情境條件、格為轉移後之結果，分 `Key-on`／`Key-off`／
`Key On, Gear ≠ Reverse` 三區塊）；PDF p9 之矩陣為**靜態能力表**
（列軸為電源狀態、欄軸為受控對象、格為是否可用）。
**二者主題不同、粒度不同，該 Excel 不含 p9 之內容。**

其真正之效力範圍為：
  **ch 12（Off Road+）** —— 列 16 `SRT or Off Road+ Hard Button press.`；
  **ch 10 之一部** —— 列 44–48（`Screen Off Button Pressed`／
  `Mute Button Pressed`／`HVAC Hard Control Adjustment`）；
  另涵蓋 `Incoming Call`／`Projection`／`Door` 等事件之電源轉移。

**p9 之能力矩陣仍無來源** —— A-PMH18 維持 `PENDING`，
其狀態不因該 Excel 到齊而改變。**須另開 DR-PMH5。**

**R-PMH73 之其餘部分維持**：該檔為第六筆素材、須入 `MANIFEST.sha256`、
其為規範性文件（`shall not be developed without following`）。

**本條之成因記明**：R-PMH73 於**未讀該檔內容之前**即寫定其效力範圍，
依據僅為 PDF p10 之一句與檔名。**素材之效力範圍須由其內容決定，
不得由其名稱或引用它的那句話推定。**
```

```
R-PMH77（停止條件須寫成可判之形式）
停止條件之文字須與其所欲攔截之事一致。「發現任一 X」與「發現**新的** X」
為不同之條件；前者於已登記之 X 存在時必然觸發，使該條件失去分辨力。

撰寫停止條件時之三項要求：
(a) 若所欲攔截者為**新增**之情形，須寫「新的」「未經登記之」「未經裁定之」，
    不得只寫「任一」；
(b) 條件之判定所需之基準（何謂「已登記」）須於同一條件內指明其出處；
(c) 字面與目的分歧時，**執行層據實兩面回報並繼續**，由分析層裁；
    **不得由執行層自行以目的覆蓋字面**。

依據：19 包停止條件 7 寫「章 7 殘餘發現任一漏字或漏句」，
而其目的為「發現**新的**漏句則 batch 1 重做」；殘餘三句皆為已登記且已裁定者，
致字面觸發而目的不觸發（19 包 §2.1）。
**同一形態於 18 包 §9 已由執行層指出過一次，而分析層未將該指認
回頭套用於其後所寫之停止條件** —— R-PMH62 之同型，第三次。
```

```
R-PMH78（R-PMH71 之 must-hit 撤回並改寫）
19 包步驟 4 所指定之 must-hit（「以 `-layout` 跑章 9 → A-PMH16 之三處
查不出」）**撤回** —— 其前提為假：三個探針於 `-layout` 之殘餘中同樣存在
（3/3，19 包 §4）。

**撤回之成因**：分析層指定該 must-hit 之期望結果時**未先驗證該期望成立**，
而 R-PMH35(c) 明訂 must-hit 須「實跑並證明其 FAIL」。
**要求他人實跑而自己以推測寫下期望值，即為該條之單向套用。**

改寫後之 must-hit（驗 R-PMH71 之本文主張，形式為二值，不涉門檻）：

  以該檢查之**預設設定**重跑，其 `RESIDUE_VERDICT` 所引之逐字內容
  須出現於輸出中 —— 此為範圍向。
  must-hit：將預設來源換為一個**確定不含該內容之替身**
  （例如僅取 SYS1 側文字），輸出須**不含**該逐字內容而 FAIL。

`--source-must-hit` 於改寫完成前**維持紅燈**，且其紅燈為正確
（19 包 §14 第 6 項）。**不得為使其轉綠而調整其期望值。**
```

---

## 七、作業步驟

1. **抄錄** —— §六之 R-PMH76 ~ R-PMH78 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **`DR-PMH5` 之開立（R-PMH76）** —— 索取 **PDF p9 之能力矩陣**之來源文件。
   問題全文須含 §2.1 之結構對照表，並具名說明
   「已提供之 `DCR21421` State Matrix 為另一主題之矩陣，不含 p9 之內容」。
   `ANOMALIES.md` 之 A-PMH18 補記 §2.1 之語意層對照結論
   （**逐字不對應 ＋ 語意亦不涵蓋**，二者皆已驗）。
   `DECISIONS.md` 記 **ch 9 仍不得開批**。

3. **`Off Road Plus` 之矩陣對照（§三，開批前置）** ——
   逐項回報：
   - Excel 列 16 之十二欄逐欄內容與其軸；
   - `OFF1.)`（12.1）、`OFF3.)`（12.3）之逐字與該列之關係；
   - **`-027` 之 Pre-Condition 是否須含「車輛已處於 Off Road state」**
     —— 回報其依據，**不自行撰寫 TC**；
   - 該 Excel 是否另有與 ch 12 相關之列（`SRT` 以外）。

4. **ch 10 之矩陣對照（§二 R-PMH76 之第二效力面）** ——
   Excel 列 44–48 與 outline `10.x` 之逐項對照，
   回報有無**矛盾**或**規格未載而矩陣有載**之情形。
   **只回報，不改任何 TC**（batch 1 之 `-008` 引 10.4，若發現矛盾即停）。

5. **`--source-must-hit` 之改寫（R-PMH78）** —— 依條文改為二值形式，
   附替身來源之 FAIL 實跑與預設之 PASS 實跑。

6. **`build_layer3_sections.py` 之重跑與 diff（19 §14 第 4 項）** ——
   重跑後與現有 TSV 逐列 diff；**若截斷行為使 `section_title` 改變，
   具名回報，不得靜默覆寫**。若重跑會破壞現值，改為只產出至暫存檔比對。

7. **`RESIDUE_VERDICT` 之第二來源（19 §14 第 2 項）** ——
   本輪**不做** —— 其正解為分析層人讀，已排入下一輪。
   **於 `DECISIONS.md` 具名登記為已知未完成**，不得靜默略過。

---

## 八、停止條件

canon §0 六條，另加本包三條：

7. 步驟 4 發現 Excel 與 outline `10.x` 有**矛盾**（batch 1 之 `-008` 引 10.4）
8. 步驟 5 之替身來源未 FAIL，或預設未 PASS
9. 步驟 6 之重跑使 `section_title` 改變**且該改變未經具名即被寫入**

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**ch 9（`Power Transitions`）不得開批**（A-PMH18 維持 PENDING）。
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 九、上繳包要求（`docs/upstream/20_matrix_scope.md`）

1. §六三條之抄錄核對表（含命中數）
2. `DR-PMH5` 全文 ＋ A-PMH18 之補記
3. **`Off Road Plus` 之矩陣對照全表**（步驟 3 四項）
4. **ch 10 之矩陣對照**（步驟 4）
5. `--source-must-hit` 改寫後之兩份實跑
6. `build_layer3_sections.py` 重跑之 diff
7. lint 全跑輸出
8. 未結 DR 清單（現應為 **1** 筆：`DR-PMH5`）
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
10. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 十、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH5`（p9 之能力矩陣）之發出** | **ch 9 開批** |
| 2 | 19／20 之 commit 授權（19 之 pathspec 見其上繳 §15，19 路徑） | 否 |
| 3 | 9.1 之 `source_clause` 例外是否寫入 profile（須核可，R-PMH46 已用畢） | `Power Transitions` 開批前 |
| 4 | 17 §5.4 其餘五項；Q10、`PROFILE_INTEGRATION.md` | 否 |

**19a §1.1 之解讀（「DR-PMH1 拿掉」採乙）已執行且未被反轉，視為確認。**

---

## 十一、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §六 |
|---|---|---|
| R-PMH76 | State Matrix 之效力範圍更正；素材效力須由內容決定 | ✅ |
| R-PMH77 | 停止條件須寫成可判之形式（「新的」vs「任一」） | ✅ |
| R-PMH78 | R-PMH71 之 must-hit 撤回並改寫為二值形式 | ✅ |

三條各管一事。R-PMH76／R-PMH78 為**部分撤回型**，
其撤回與保留之範圍已於條內分別明載。
