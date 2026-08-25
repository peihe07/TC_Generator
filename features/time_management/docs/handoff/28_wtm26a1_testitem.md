# 28 — W-TM-26-A1：test_item 下半格式整改與基準分歧報告（rev A, 2026-08-25）

上游：Pei 於 2026-08-25 對 `output/…_SWQT_20260825.xlsx` 提出三項；
另含分析層對 `27` §C1 之覆核結果（基準分歧，見 §3）。

---

## §1 Pei 三項之核驗（基準：0825 輸出件，SHA `b4565962…`）

### P1 — test_item 括號下半首字母小寫：證實，59/59

`(confirm …)` 型。**0822 交付件同樣如此** —— 此為 B1 生成樣式，
非 W-TM-26 引入；`26` 包稽核僅驗「括號下半存在」未驗其大小寫與分隔，
屬分析層漏檢，於此自陳。

### P2 — 括號下半與上半之間無空行：證實，59/59

現為單一換行 `…\n(confirm …`。交付基準（UserProfiles 0824，189 條）
為 `…\n\n(Verifies that …` —— 空行分隔＋首字大寫。P1/P2 一體整改。

### P3 — Procedure／ER 編號前一格空格：**檔內不可復現**，三重驗證

1. 文字層：全 59 條 I/J/K/L/M 逐字元普查，`\n` 後續字元僅
   數字與 `(`（122/101/84/59/48/14/4 處），**空白 0 處**；行首
   空白（含 U+00A0／全形／tab）0 處；儲存格首字元空白 0 處
2. 樣式層：I–M 資料格 295 格全為 `left + top + wrapText`，
   `indent = 0`（xf 176，raw styles.xml 驗證）
3. 渲染層：LibreOffice 轉 PDF 後 pdftotext -layout，編號行齊左無縮排

**可能之混淆源**：(i) `ASW-R2/Time Management/` 資料夾內之 0822
交付件**仍為置中對齊**（D5 只修了 output 件），並排比對時空格來自
該檔；(ii) macOS Quick Look 之 xlsx 預覽引擎自帶邊距。
**請 Pei 於 Excel 重新開啟 0825 件確認；若仍見空格，給一個具體
儲存格位址（如 L10），分析層對其逐位元組追查。**

---

## §2 條文（待謄 RULINGS.md）

**R-TM84（Pei, 2026-08-25）—— test_item 下半之格式定式**

```
R-TM84（Pei, 2026-08-25）—— test_item 下半之格式定式

test_item 之括號下半（R-S4）：
  1. 與 verbatim 上半之間以空行分隔（連續兩個換行 `\n\n(`）
  2. 括號內首字母大寫（`(Confirm …)`）

基準：UserProfiles 0824 交付本之 189/189 既有形態
（`…\n\n(Verifies that …`）。canon §4.3.1 之「獨立成行」自此
於本 feature 讀為「空行分隔」。sibling 區分 token 之既有內容不動，
只改分隔與首字母。
```

---

## §3 基準分歧 —— `27` §C1 之覆核結果（A-TM31）

`27` C1 判 `088a4476…` 為「謄錄錯誤」，理由是 repo 內無此雜湊。
**該判定錯誤。** `088a4476…` 為 `26` §0 明文宣告之基準 ——
`ASW-R2/Time Management/…_SWQT_20260822.xlsx`（**repo 外**之交付件）——
之實測 SHA256，分析層持有其複本可隨時複驗。C1 只搜了 repo 內，
把「repo 內查無」誤讀為「雜湊不存在」，並以「更正」抹去了一個真訊號：

**兩個 0822 是不同的檔案。**

| 件 | F 欄 | G 欄 | SHA256 前綴 |
|---|---|---|---|
| ASW-R2 交付件 0822 | `NR1L-TimeManagement-NNN` | `Time Management` | `088a4476` |
| repo output 0822（27 之基準，現已不在 output/） | `NR1L-TimeAndDate-NNN` | `Time and Date` | `2afd87be` |

交付件 0822 → 輸出件 0825 之逐欄 diff：**F、G 各 59 列全改，
其餘非受令欄（B/D/E/I/N/P/R/S/AA）零變更**。ID family 與 Test Group
之改名不在 W-TM-26 之 T1–T6 任何一項，`27` §4 之逐列 diff 亦未申報 ——
其成因落在 repo 側某次寫回（G 欄改名有 canon §4.1.1 之依據：Test Group
＝spec 文件標題 `Time and Date`；R-TM2 之 [PROVISIONAL] 值為
`Time Management`，推翻須留痕），但**送出 ASW-R2 的是改名前的件**。

**連帶更正**：A-TM30（「基準 SHA 手抄致誤」）之前提部分失效 ——
SHA 沒抄錯，錯的是 C1 之搜尋範圍與結論。A-TM30 之「SHA 應由腳本產出」
建議仍成立（保留），另登 **A-TM31：交付件與 repo 基準分歧、
identifier 欄未經裁定即改名且未申報**。

---

## §4 裁定點（Pei）

**Q1 — TC ID family 與 Test Group 之定名**（審查者手上是
`NR1L-TimeManagement-*`，repo 現行是 `NR1L-TimeAndDate-*`；序號兩邊一致，
只差前綴）：
(a) 維持 `NR1L-TimeAndDate-*` / `Time and Date`（canon §4.1.1 對齊
    spec 標題），Revise note 附前綴對照一行
    （`NR1L-TimeManagement-NNN → NR1L-TimeAndDate-NNN`，NNN 不變）；
(b) 回改 `NR1L-TimeManagement-*` / `Time Management`，與已送審件一致。
分析層建議 (a)：canon 依據在彼；前綴對照零歧義，審查方成本一行。
無論何者，R-TM2 之 [PROVISIONAL] 推翻須補一條裁定落 RULINGS.md。

（另：`27` §7 之 VES KEEP/DELETE 仍待 Pei 一字裁定，此處不重敘。）

---

## §5 下放工作單 W-TM-26-A1（T1 可即刻開工，T2 待 Q1）

基準：0825 輸出件（`b4565962…`），`--out` 另檔（R-TM80）、
dry-run 先行（R-TM78）。

T1 P1+P2：59 條 test_item 之 `\n(x…` → `\n\n(X…`（僅動分隔與首字母，
    括號內其餘內容逐字不動）；R-TM84 謄 RULINGS.md（含 27 §7-2 之
    回報欄回填）。
T2 依 Q1 裁定處理 F/G 59 列（(a) 則不動檔、只補 Revise note 對照與
    R-TM2 推翻裁定；(b) 則 F/G 回改）。
T3 A-TM30 加註前提更正、A-TM31 登記（ANOMALIES.md）。
T4 回繳附：逐列 diff（僅 I 欄應有 59 處、其餘零）、lint 報告、
    未結 DR 清單。**diff 之「其餘零」為驗收條件 —— 任何非受令欄
    變更即退回。**

## §6 未結 DR 清單（隨附義務）

DR-2（High）、DR-4（High）、DR-5（中）、DR-8（High）、DR-9（High）、
DR-10 四分項（High）、DR-12（開放）、DR-12b（High）、DR-20（High）。
DR-6 追溯用；DR-7 空號；DR-11 已取消。

---

## §7 決議（Pei, 2026-08-25）與 T2 具體化

Pei 三項裁定：**Q1 裁 (b) 回改 TimeManagement**；**VES KEEP**；
**P3 重開後確認不在** —— P3 結案，無缺陷，混淆源即 §1 P3 所列。

**R-TM85（Pei, 2026-08-25）—— TC ID family 與 Test Group 回改定案**

```
R-TM85（Pei, 2026-08-25）—— TC ID family 與 Test Group 回改定案

F 欄 TC ID family 回改 NR1L-TimeManagement-NNN（NNN 不變），
G 欄 Test Group 回改 Time Management —— 與已送審之 ASW-R2 交付件
（SHA `088a4476…`）一致。R-TM2 之 [PROVISIONAL] 就此定案：
test_group = "Time Management"、非 canon §4.1.1 之 spec 標題預設
（"Time and Date"），Pei 明裁優先。feature.yaml 若已被改為
"Time and Date" 一併回改並移除 [PROVISIONAL] 註記。
A-TM31 之未經裁定改名，處置即本條之回改；日後 identifier 欄之
任何變更依 R-G19-4 先裁後動。
```

**R-TM86（Pei, 2026-08-25）—— VES 供電行 KEEP**

```
R-TM86（Pei, 2026-08-25）—— VES 供電行 KEEP

`The VES screens are powered on`（5 行，#009 #015 #016 #017 #043）
維持 KEEP —— 執行層 27 §2 之借調判斷（VES 獨立供電，非點火 ON
所蘊含）獲 Pei 追認，非 §4.4 system default。
```

**T2 具體化**（依 Q1(b)，可開工）：

- F 欄 59 列：`NR1L-TimeAndDate-NNN` → `NR1L-TimeManagement-NNN`
- G 欄 59 列：`Time and Date` → `Time Management`
- feature.yaml `test_group` 回改確認；回改後 R-TM2 定案（R-TM85）
- `output/DELIVERY_NOTE.md` 內之 identifier 提及處同步（文件標題之
  「Time and Date」係指 spec 名，不在回改射程）
- R-TM85／R-TM86 謄 RULINGS.md，A-TM31 結案註記、A-TM30 前提更正
  （§3）一併落 ANOMALIES.md
- 驗收（R-G19-4）：F/G 各 59 處、I 欄 59 處（T1），其餘欄零變更

T1（test_item 空行＋首字大寫）與 T2 可同一輪寫回，dry-run 先行。
