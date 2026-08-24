# V35 — 抽樣覆核結果：**不通過**（手足標題逐字相同 8 條）

下放包 **V35**。所據上繳：W-VF71 完成報告（2026-08-24）
＋ 分析層對 `vf230_batch01.json`／`vf230_batch04.json` **100 條之機械稽核**。
新增 **R-VF97／R-VF98**（**開號前須查 `RULINGS.md` 最大已用號，不符即以實測為準**）、
**W-VF72**（1 項工單）。

---

## 1. 抽樣方法與通過項（本層自測，非採信自檢）

**方法**：`json` 讀入 `tcs`，以 regex 逐條測；**非目視**（R-VF73）。
**樣本**：batch01 全 50 ＋ batch04 全 50 = **100 條**（超過 R-VF76 之 20%）。

**通過（0 違規）**：

```
tc_title > 14 字                    0 / 100
Pre-Condition 系統預設 pattern       0 / 100
禁用動詞（observe/check whether…）   0 / 100
四欄之尾句號                         0 / 100
procedure ↔ ER 之編號數不符          0 / 100
```

**上繳所報之六批自檢 0 筆，於上列五項與本層獨立實測一致。**

---

## 2. Defect 1（blocking）—— 手足 `tc_title` 逐字相同，**8 條 4 對**

canon §4.3 逐字：**「two sibling tc_titles that read identically = FAIL」**

| 對 | seq | leaf | tc_title |
|---|---|---|---|
| A | 293 / 295 | `PowerTailgate-027` / `-028` | `Power Tailgate is displayed as Disabled when Power_Tailgate_Enable is 0 (Disabled)` |
| B | 294 / 300 | `SuspensionAutoEntryorExit-090` / `-092` | `Suspension Auto Entry or Exit is displayed and modifiable` |
| C | 307 / 309 | `SuspensionFlashLightsWithLower-002` / `-003` | `Suspension Flash Lights With Lower is displayed and modifiable` |
| D | 313 / 314 | `SuspensionSoundHornWithLower-008` / `-009` | `Suspension Sound Horn With Lower is displayed and modifiable` |

**B／C／D 三對之標題無任何區辨 token** —— 其形式為「`<設定> is displayed and modifiable`」，
不含條件子句，**同一 Test Set 內任兩條皆可共用之**。

**A 對更重，其為實質錯誤而非僅標題重複**：

```
seq 293  leaf -027  條文：HW supplier shall provide … When the LTM or ETM
                        receives the value via signal, $IPC_VEHICLE_SETUP2…$
seq 295  leaf -028  條文：The default value of the IPC_VEHICLE_SETUP2.
                        Power_Tailgate_Enable signal **shall be Enabled**.
```

**二條文完全不同**（前者為收訊後顯示，後者為預設值），
**而 seq 295 之標題稱 `displayed as Disabled`，與其條文之 `shall be Enabled` 相反。**

→ **seq 295 須逐條複核其 procedure／ER／`reasoning` 是否亦沿用了錯誤之值。**

---

## 3. Defect 2 —— `tc_title` 之條件主體遺失，**3 條**

```
seq 426  Torque Unit is not displayed when (SRT) is "Absent"
seq 433  Torque Unit is displayed and modifiable when (SRT) is "Present"
seq 454  Rear Guidance Lights with Cargo Lights is not displayed when (Utility_Lighting) is "Absent"
```

**`when (SRT) is "Absent"` 之括號前無主體。** 其條文逐字為
`HMI receives the value as Absent via signal, $SRT$ ,Then HMI shall not display the (Torque Unit)…`
—— **`$SRT$` 為訊號名、`(Torque Unit)` 為被顯示之設定**；
標題將訊號名寫成裸括號並丟失其主體。

**成因推測（待實測）**：括號別名剝除規則（R-VF70 二）將 `$SRT$` 之
`$` 剝除後，其與別名括號之形態不可分辨。

---

## 4. Defect 3 —— `(PTGM)` 別名仍在標題，**2 條**

```
seq 281  Power Tailgate is not displayed when CAN node 82 (PTGM) is "Absent"
seq 285  Power Tailgate is displayed and modifiable when CAN node 82 (PTGM) is "Present"
```

**R-VF70 二令「括號內之別名不入 `tc_title`」，此二條未遵行。**

---

## 5. R-VF97 —— R-VF70 二之 carve-out（**本節之編號以落檔時實測之最大號 +1 為準**）

```
R-VF97（`tc_title` 括號之三分，分析層裁定 2026-08-24）

R-VF70 二（括號別名不入標題）與 R-1 v2（`= <raw> (<label>)`）
**在字面上不可機械區辨** —— 二者皆為 `X (Y)`。
本層之機械稽核初測命中 57／100，其中 32 為合法之 DBC 標籤。

**三分之判準**：

  **甲、DBC `VAL_` 標籤 —— 保留。**
      形態：`as <raw> (<Label>)`／`is <raw> (<Label>)`，其 `<Label>` 逐字取自 DBC。
      **R-1 v2 所令，R-VF70 二不及於此。**

  **乙、節點／參數之別名 —— 移除。**
      形態：`CAN node 82 (PTGM)`／`SVC_SK_PRSNT (Surround_View_Camera)`。
      **R-VF70 二所指者即此。**

  **丙、裸括號（其前無主體）—— 為缺陷，非樣式問題。**
      形態：`when (SRT) is "Absent"`。
      **其成因為抽取，不得以「移除括號」修之** ——
      移除後成 `when SRT is "Absent"`，而 `SRT` 為訊號名，
      **須先確認標題所欲表達者為訊號或為設定，再重寫。**

**機械判準**：以 `as \d+ \(...\)`／`is \d+ \(...\)` 匹配者為甲；
括號前一 token 為空白或介系詞者為丙；其餘為乙。
**三類之處置不同，不得以單一 regex 一併剝除。**
```

---

## 6. R-VF98 —— 「無條件子句之標題」不得作為手足

```
R-VF98（手足區辨之最低要件，分析層裁定 2026-08-24）

canon §4.3 令手足之 `tc_title` 不得逐字相同。**本條補其可執行形式**：

**凡同一 leaf 家族（`leaf_id` 去尾綴後相同）之二條以上 TC，
其 `tc_title` 須各含一個相異之區辨 token。**

**「`<設定> is displayed and modifiable`」此一形式無條件子句，
其對同家族之任兩條皆適用，故不得單獨作為標題。**
須補其條件（觸發之訊號與值、或其所驗之分區）。

**自檢增項（逐字可執行）**：
```
  同一 leaf 家族內，tc_title 逐字相同者 → FAIL
  tc_title 不含 " when " 且該家族之 TC 數 > 1 → FAIL
```

**成因**：本輪 8 條 4 對命中，其中 3 對之標題完全無條件子句。
**六批自檢 0 筆而本層抽樣命中 8 條 —— 該項不在自檢之判準內。**
```

---

## 7. 上繳之三項與裁定不符 —— 逐項核可

| # | 事項 | 判 |
|---|---|---|
| 1 | B 類為 9 條非 11 條；2 條係抽取式讀不到而報為資料缺 | **核可**。其自判「問上游等於問錯問題」正確，且附 5 個假陰／假陽錨點。**A-VF13／21／25／27 同族之第六例** |
| 2 | `vf230_wvf18_rd1.py` 之死錨點（`in subst` 恆 False → `not False` 恆 True） | **核可**。**A-VF4 之改正當時只套用到 R-VF17 之腳本，未及於此支** —— 此即 R-VF92 一所欲攔者，其於立法後首跑即命中。換錨後結論不變（160／158／差 2），**錨點修好而結論未動**為正解 |
| 3 | 12 處落點與實際錨點非同一組；真正在執行者在腳本裡，共 18 支 | **核可，且本層之列舉為錯**。V34 §4-5 之「12 處落點」取自文件內之提及，**而 R-VF92 一管的是錨點本身**。**只掃文件不會發現死錨點** —— 其判斷正確 |

**`Greeting_Lights_Menu` 之處置正確** —— 名近而不同，依 R-VF92 二未改取、未據以生成，
登記進 DR-34 請上游裁示。**DR-34 若因此結案，其為八件 DR 中第一件可望自解者。**

---

## 8. W-VF72 — 修正與續行

1. **Defect 1**：8 條 4 對之標題補區辨 token。
   **seq 295 另須逐條複核其 procedure／ER／`reasoning`** —— 其標題之值與條文相反，
   須確認錯誤是否止於標題。
2. **Defect 2**：3 條裸括號 —— **先判其標題所欲表達者為訊號或設定，再重寫**，
   不得逕行剝括號。
3. **Defect 3**：2 條之 `(PTGM)` 移除。
4. **自檢增二項**（R-VF98 之逐字形式），**可失效性實測**。
5. **R-VF97 之三分判準實作**，以本輪之 57 命中為回歸樣本：
   甲 32 保留、乙 2 移除、丙 3 修正，**其餘 20 逐條歸類並回報**。
6. **`vf230_wvf45_priority.py` 之 exit 1**（池首 88 條含 `{P0: 82, P1: 6}`）——
   **只查不改**：判其為 (i) `leaves.tsv`／`writability.tsv` 之前輪 staged 內容所致、
   或 (ii) 選池序之再度失真。**二者處置不同。**
7. **上繳之「本包是否仍有該驗而未驗者」一節為空**（僅有標題）——
   **該節為 canon §8.2 之必要節，須補**。

**批次生成暫停至 W-VF72 完成** —— 300 條中已知 13 條有缺陷，
其形態（標題）跨全部批次，**續生成會等比例複製之**。

---

## 9. 給 Pei

**抽樣結果**：100 條中五項機械判準全數 0 違規，**而標題層有 13 條缺陷**。
**其中 8 條為 canon §4.3 明列之 FAIL，自檢六批全 0 未攔到** ——
判準不在自檢清單內，非自檢失效。

**進度三數**：已生成 300（待修 13）／可直接書寫 478／隔離 76。

**待你**：DR-34（`Greeting_Lights_Menu` 一問可望結案）／35–41，**八件未送出**。

---

## 10. 新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF97（`tc_title` 括號三分：標籤保留／別名移除／裸括號為缺陷） | 分析層裁定 | ✅ §5 |
| R-VF98（手足區辨之最低要件；無條件子句之標題不得單獨使用） | 分析層裁定 | ✅ §6 |

**⚠ 開號前須查 `RULINGS.md` 之最大已用號（R-VF10、R-VF94 三）**；
本包以 R-VF96 為現行最大而取 97／98，**若實測不符即以實測為準並回報**。

**工單**：W-VF72（13 條修正、自檢增二項、三分判準實作、選池 exit 1 查明、補上繳末節）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷 —— 本輪該節為空，須補。**
