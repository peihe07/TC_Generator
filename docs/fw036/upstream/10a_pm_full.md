# 上繳 10a：Power Management 整批回修（A 段）

執行層：Opus5（Claude Code）｜日期：2026-08-21｜新規 0 條
基底：交付本之位元組副本（見 §1）｜產出：`features/power/sandbox/b10/pm_10a.xlsx`
**未交付**：止於 sandbox。

**本包六項作業中，四項全做、一項部分做、一項保留。** 保留項之理由與
證據見 §5、§6 —— 皆為「硬做即造值」之情形，非工時問題。

## 1. ⚠ 基底異動：交付檔在交付後被重新儲存

| 時點 | sha256 | 位元組 |
|---|---|---|
| 2026-08-21 16:05 執行層交付 | `f59de2e7…`（DELIVERY_NOTE §8.1a 所登） | 128,130 |
| 2026-08-21 16:16 現況 | **`3d14a092…`** | 135,801 |

客戶目錄之 `…20260821(Revise).xlsx` 於交付 11 分鐘後被開啟並存檔
（Excel 重新序列化，+7,671 bytes）。執行層逐項複驗其影響：

```
zip 成員 42 → 42（遺失 0、新增 0）｜classic DV 4 → 4｜x14 DV 1 → 1
資料列 283 → 283｜六欄逐格內容差異 0
```

**內容零差異，x14 下拉未受損。** 依 10a「基底＝交付本之位元組副本」，
本包以現況檔為基底。惟 **DELIVERY_NOTE §8.1a 所登之 sha256 已失效**，
須更新為 `3d14a092…` 或註明其為交付當時值。具名回報，未自行追改。

## 2. 已完成之作業

| 項 | 內容 | 完成量 | 驗證 |
|---|---|---|---|
| A1 | 三件組 → `MESSAGE.Signal`／(a)(b) 式 | 四欄 41 → **13**（餘 13 屬 §5 保留列） | 見 §3 |
| A6 | DBC `VAL_` 括號標籤 | 全數（凡本包改寫之賦值皆帶標籤） | 抽驗見 §4 |
| A4 | PROXI 前綴與 `$` 式 | **19 行轉換**、13 行保留（§6.2） | 見 §4 |
| A2/A3 | Input 內聯、步驟自足 | **57/158 列**（can 17、internal 40） | 見 §3 |
| — | transition 型拆步 ＋ ER 同步增列 | 6 列 | **E 維持 0** |
| A5 | spec_reference R-2 遷移 | **283/283 完成**（§5.1，更正） | 見 §5.1 |

### 驗收對照

| 項目 | 目標 | 實測 |
|---|---|---|
| 不得變動 A B C D E F G H I I-sib J K L M N | 全 0 | **全 0，逐項未動** |
| Procedure ↔ ER 1:1（E） | 0 | **0**（6 列拆步後仍 0） |
| `test_item` 零變動 | 0 格 | **0 格** |
| 逐格 diff 限 spec／input／pre／proc／er | — | **154 格，欄 J/K/L/M，非目標欄 0** |
| Input 非 `NA` | 0 | 158 → **101**（未達成，§5.2） |
| 含 `listed in Input Test Data` | 0 | 158 → **101**（未達成，§5.2） |
| 三件組殘留 | 0 | 41 → **13**（未達成，§5.2） |
| spec 首行 `^CFTS0(09\|10)-\d{7}(, \d{7})*$` | 283−PENDING | **283/283，PENDING 0**（達成） |
| P（lint036） | — | 51 → **23**（明細 §7） |

x14 讀回：zip 成員 42 保留、僅目標 sheet XML 相異、DV 計數前後相等。
寫入路徑 `surgical_save()`，全域無 `Workbook.save()`。

## 3. 改寫實例（逐字）

**A1 拆步 ＋ ER 同步（row 57）**
```
前 P: 1. Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from "Not_Pressed" to "Pressed"
      2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ …
   E: 1. The TLM registers the press transition
      2. VPLastStatus reads "OFF", …
後 P: 1. Send CAN: CLIMATIC_PANEL.Radio_btn0 = 0 (Not_Pressed)
      2. Send CAN: CLIMATIC_PANEL.Radio_btn0 = 1 (Pressed)
      3. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ …
   E: 1. CLIMATIC_PANEL.Radio_btn0 = 0 (Not_Pressed) is sent      ← 新增，(b) 式
      2. The TLM registers the press transition                   ← 原句保留於對應步
      3. VPLastStatus reads "OFF", …
```

**A2/A3 can 類（row 17）**
```
前 IN: RemStActvSts in STATUS_BH_BCM2 on BH-CAN = "Remote Start Active"
   P1: Send the signal listed in Input Test Data
後 IN: NA
   P1: Send CAN: STATUS_BH_BCM2.RemStActvSts = 1 (Remote Start Active)
```

**A2/A3 internal 類（row 68）**：`Send the transition listed in Input Test Data`
→ `Drive Phone_Call.Info from "Not_Active" to "Active"`。
動詞 `Drive`／`Set` 取自 **PM 自身既有語料**（proc 內 `Drive …Req from …` 6 處、
`Set …` 5 處），非執行層發明。

**A4（row 94／253）**：`3. $PwrAccDelayAct$ reads 10 minutes`
→ `3. PROXI $PwrAccDelayAct$ = 10 minutes`。

## 4. 抽驗

- **A6 標籤**：本包產生之每一賦值皆經 `VAL_LABELS` 表產出，
  raw↔label 由 `resolve_raw()` 反查；查不到者回傳 `None` 並落入保留清單
  （row 195 即此情形，§5.2）。無任何標籤由執行層臆造。
- **A1 七種對照**：逐字取自 10a §A1 表，程式常數即該表，未自行擴充。
- **A4 轉換 19 行**：逐行列印覆核，19 行皆為明確等值述語。

## 5. 保留項（未做）與其理由

### 5.1 A5 spec_reference 遷移 —— **已完成（283/283）**

> **⚠ 本節為更正。** 初版判定「前置資料不足，全數保留」，
> **該判定錯誤，予以撤回。** 錯誤成因：執行層取
> `data/anchor_attribution_53.json` 為唯一來源，該檔回答的是
> 「這條 TC **驗哪一個**錨點」（語意歸屬，125/283 `determined`），
> 而非「這個 leaf **引用哪些** SYS2 ObjectID」（事實對照）。
> 二者為不同問題；spec_reference 需要的是後者。
> 且 §10.7 本即明訂「同一文件內多個 ObjectID 以 `, ` 續列」——
> **無須自多個錨點中挑選其一**，故不存在「不確定性」之障礙。
> 經 Pei 指出「要回去對 SYS2 的文件」後改依 SYS2 重做。

**來源鏈（全程可查證，無推測）**：

```
工作簿 req_id（SWE-PM-nnn）
  → data/layer3_full.tsv 之 tokens（Sys-RA-PM-nnnn）
  → SYS2 Polarion 匯出之 Source Requirement ID（7 位 ObjectID）
  → SYS2 Document ID（CFTS009／CFTS010）
```

**鏈驗證**：layer3 之 140 筆記錄，其 `item_ids` 與「tokens 經 SYS2 解出之
ObjectID 集合」**逐筆相等，0 筆不符**；tokens 缺於 SYS2 者 **0**；
leaf 跨兩份 CFTS 文件者 **0**。

（初次比對曾得「36 筆不符」，係 SYS2 之 `Source Requirement ID` 單格
內含多個以**換行**分隔之 ObjectID 未拆所致，非真實不符。已修正解析。）

**寫法**：第一行 `CFTS009-{ids}`／`CFTS010-{ids}`，多個 ObjectID 以 `, `
續列、文件前綴僅敘明一次（§10.7）。ObjectID 取該 leaf 於 SYS2 所引之
**全集**，不由章節號反推、不挑選其一。
第二行保留原有 `{檔名}_{章節號}` 參照，使章節層級精度不因遷移而流失。

```
row 10 SWE-PM-001
 舊：R1LR_Atl-H_25PI3.5_…_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.1
 新：CFTS009-4941354, 4941355, 4941357, 4941358, 4941360, 4941453
     R1LR_Atl-H_25PI3.5_…_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.1
```

**結果**：283/283 首行匹配 `^CFTS0(09|10)-\d{7}(, \d{7})*$`、
283/283 保留第二行原參照、**PENDING 0 列**、
`test_item`／`pre`／`input`／`proc`／`er` 五欄零變動、
逐格 diff 283 格全落 `spec`（N 欄）、其餘檢查值未動。
產出：`features/power/sandbox/b10/pm_10a5.xlsx`（sha256 `7ff2501b…`）。

### 5.2 A2/A3 之 101 列 —— **需內容判斷，非機械可解**

| 類別 | 列數 | 保留理由 |
|---|---:|---|
| free（自由文字） | 59 | 回指語與資料為不同名詞，機械代入產生病句。實測例：`Apply each ignition working condition listed in Input Test Data in turn` ＋ `Ignition working conditions: Ignition Pre_Start, …` → `Apply each ignition working condition Ignition working conditions: Ignition Pre_Start…`（名詞重複、不成句） |
| proxi | 33 | **PM 語料中 `$X$` 於 proc 僅有 `Read` 一種動詞（35 處），無「設定 PROXI」之先例**。且該 33 列語意不一：配置參數（`$VC_SpecialPKG_IC$: "Tungsten (147)"`）、訊號轉態（`$ACCDlyAct$: active to inactive`）、實體按鍵（`$ICSPowerButton$: Pressed for 10 seconds consecutively`）三者混雜，通用動詞必錯其二 |
| can+free | 6 | 一列同時含 CAN 賦值與自由文字，回指語指向後者。實測代入結果：`Set STATUS_LIN.PN14_LS_Actv = 1 (Active) and … and Starting volume level: 25`（代錯名詞） |
| can | 2 | rows 191、192，回指行不在 `proc` 欄 |
| 無法解析 | 1 | row 195 `Batt_ST_Crit in STATUS_LIN on BH-CAN = [1h] (held)` —— 值帶 `(held)` 修飾語，`resolve_raw()` 不猜 |

執行層已實作通用代入器並**對全 158 列試跑**，才據實測結果劃定範圍：
57 列輸出合格（can／internal，動詞有 PM 語料先例），101 列輸出不合格。
不合格者未寫入 —— 交付物之步驟文字若不成句，比保留回指更糟。

此與 **04 §六**「內容判斷屬分析層職責，不下放」同型。
`features/power/sandbox/b10/edits.json` 之 `log.held` 載全 101 列與其類別，
可直接作為分析層逐列覆核之工作清單。

## 6. 發現（3 項）

### 6.1 ⚠ 10a 之「test_item 零變動」與 R-6／R-1 v2 相牴觸

批 1（M15）所寫入之 sibling 區分 token，**逐字引用當時之 proc 文字**，
其中 10 列含 v1 三件組，例：

```
(Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from "Not_Pressed" to "Pressed" — …)
```

依 **R-6**，括號下半屬作者生成內容，受 R-1 規制；v1 既撤銷，此 10 處即違規
（lint P 已計入，見 §7）。但 10a 驗收明訂「`test_item` 零變動」，
兩者不可兼得。本包**遵驗收，未動 test_item**，具名回報。
建議下一包解除該限制以修此 10 處。

### 6.2 A4 之 13 行為非等值述語，無法以 (c) 式表達

`$VC_VEH_BRAND$ reads a value other than "Maserati"`（6 行）、
`$Country_Code$ is marked as a country needing…`（2 行）、
`The ETM carries $X$ greater than "2025"`（2 行）等。
`PROXI $X$ = <值>` 只能表達等值；硬轉將改變語意
（`= a value other than "Maserati"` 不成立）。**保留原句。**
R-1 v2(c) 未規定否定／不等式條件之寫法，待補。

### 6.3 A4 之量與下放包所述不符

10a 載「現 129 行無 `PROXI` 前綴」。實測 `pre` 欄含 `$` 之行共 **94 行**，
其中 **60 行**為 `TLM_Status.Info and $Telematic_Power$ read "Full-Operation"`
之複合狀態句（內部訊號＋PROXI 並述），非 PROXI 設定行，
轉換將丟失內部訊號一側。真正可轉者 19 行、非等值者 13 行、
其餘為複合句。**129 之來源未明。**

## 7. 殘留 P=23 之明細

| 欄 | 數 | 內容 |
|---|---:|---|
| `input` | 13 | §5.2 保留列之 input 仍含三件組（隨該列一併保留） |
| `test_item(括號下半)` | 10 | §6.1 之 M15 token（受「test_item 零變動」限制而未修） |

`pre`／`proc`／`er` 三欄之三件組已全數清除。

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項：**

1. **本包新增之 6 則 ER 行（拆步所需）未經內容覆核。** 形如
   `CLIMATIC_PANEL.Radio_btn0 = 0 (Not_Pressed) is sent`，係依 (b) 式機械產生。
   其斷言「訊號已送出」是否為該步驟應驗之觀察點，未經判斷 ——
   原 ER 之「The TLM registers the press transition」才是行為斷言。
2. **57 列內聯後之步驟未逐列覆核可執行性。** 本包能自證動詞有語料先例、
   資料逐字取自原 input 欄；不能自證改寫後之步驟於實機可執行。
3. **A6 之 DBC 標籤未對 DBC 原檔複驗。** 標籤取自 10a §A6 表（分析層稱
   DBC 實查）。執行層**未開啟 DBC 檔案驗證**該表 —— 考量 R-1 v1 之教訓
   （分析層表格曾與語料不符），此為未閉合之信任鏈。
4. **10a 之 B–H 段（其餘七本）未動** —— 依 Pei 指示凍結，非遺漏。
5. **PM 交付本仍為批 2 版本。** 本包產出止於 sandbox；交付需另行授權
   （R-P309 之效力範圍不及於本包之 81 列變動）。

## 9. 引用之既有裁決

R-1 v2（(a)–(f)，canon §8.7.5）、R-2（A5 之母條）、R-6／R-6b（§6.1）、
R-7（VAL_ 標籤）、§4.5（欄位歸屬）、§8.4.1（不得造值，§5.1／§5.2）、
§8.4.3（PENDING 三態，§5.1）、§8.2.1（不得刪列）、
R16／R-G3（`surgical_save`）、R-P228（交付前備份）、R-P309（授權範圍）、
§5a（量測條件，§6.3）、03 §四（同欄兩制之判斷，§5.1）、
04 §六（內容判斷不下放，§5.2）。

## 10. 產出

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b10/pm_10a.xlsx` | 回修後工作副本（sha256 `0ab0e603…`） |
| `features/power/sandbox/b10/edits.json` | 154 格編輯集 ＋ `log.held` 101 列待判清單 |
| `features/power/sandbox/b10/pm_10a_20260821.md/.json` | lint036 報告 |
| `features/power/scripts/b10/{signals,inline,build,apply}.py` | 回修程式 |
