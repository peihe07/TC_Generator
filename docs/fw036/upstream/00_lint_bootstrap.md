# 上繳 00：lint036 建置與校準（報告模式）

執行層：Opus5（Claude Code）｜日期：2026-08-21｜模式：報告，零檔案修改

## 1. 交付物

| 項目 | 路徑 |
| --- | --- |
| linter | `scripts/lint036.py` |
| 測試 | `tests/test_lint036.py`（42 項，全數通過） |
| 報告 | `docs/fw036/lint_reports/{tag}_20260821.md`（8 本） |

## 2. 校準結果對照表（Media 0625）

| 檢查 | 基準 | lint 實測 | 判定 |
| --- | ---: | ---: | --- |
| A 禁用動詞 | 0 | 0 | 一致 |
| B ER 情態詞 | 0 | 0 | 一致 |
| C hedge | 1 | 1 | 一致 |
| D PC 違規 | 0 | 0 | 一致 |
| E 對齊 | 1 | 1 | 一致 |
| F 方括號 | 0 | 0 | 一致 |
| G Test Set | 0 | 0 | 一致 |
| H ER 模糊 | 0 | 0 | 一致 |
| I 缺括號 | 2 | 2 | 一致 |
| K CJK | 0 | 0 | 一致 |
| L >50 字 | 0 | 0 | 一致 |
| J 行首大寫 | 未校準 | 8 | 未校準 |
| M 空欄三態 | 未校準 | 0 | 未校準 |
| N 尾句號 | 未校準 | 7093 | 未校準 |
| I-sibling | 未校準 | 6 | 未校準（I 之第二子型，基準僅涵蓋「缺括號」） |

**11 項已校準檢查全數與基準相符，未修改任何基準。**

## 3. 八本報告

| tag | 報告 | A | B | C | D | E | F | G | H | I | I-sib | J | K | L | M | N |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MediaHMI | `docs/fw036/lint_reports/MediaHMI_20260821.md` | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 6 | 8 | 0 | 0 | 0 | 7093 |
| BT | `docs/fw036/lint_reports/BT_20260821.md` | 37 | 0 | 0 | 275 | 1 | 33 | 8 | 1 | 8 | 2 | 49 | 1058 | 375 | 14 | 8229 |
| CFTS012_DealerMode | `docs/fw036/lint_reports/CFTS012_DealerMode_20260821.md` | 6 | 22 | 0 | 6 | 1 | 129 | 0 | 6 | 29 | 0 | 0 | 0 | 0 | 54 | 518 |
| CFTS026_HandsFreePhone | `docs/fw036/lint_reports/CFTS026_HandsFreePhone_20260821.md` | 31 | 18 | 0 | 21 | 5 | 3 | 29 | 0 | 28 | 2 | 0 | 44 | 44 | 39 | 453 |
| Projection | `docs/fw036/lint_reports/Projection_20260821.md` | 5 | 0 | 2 | 20 | 5 | 1 | 1 | 0 | 2 | 2 | 6 | 648 | 91 | 96 | 9047 |
| Home | `docs/fw036/lint_reports/Home_20260821.md` | 0 | 2 | 0 | 2 | 0 | 0 | 216 | 0 | 16 | 0 | 2 | 0 | 17 | 5 | 2017 |
| AMFM | `docs/fw036/lint_reports/AMFM_20260821.md` | 57 | 0 | 0 | 8 | 0 | 21 | 0 | 0 | 154 | 12 | 1 | 0 | 29 | 0 | 2161 |
| PowerManagement | `docs/fw036/lint_reports/PowerManagement_20260821.md` | 20 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 104 | 2 | 0 | 71 | 0 | 2165 |

8 本合計 35,700 筆違規；各檢查總量：A=156 B=42 C=6 D=332 E=13 F=187 G=254
H=7 I=239 I-sib=128 J=68 K=1750 L=627 M=208 N=31683。

八本 header 皆定位於第 9 列，欄位對照一致（test_set=7, test_item=8, pre=9,
input=10, proc=11, er=12, spec=13，0-based）。TC sheet 名兩種變體皆命中：
`Test Case Specification 測試用例規範` 與 `Test Case Specification&Result`。

## 4. pytest 結果

```
$ .venv/bin/python -m pytest tests/test_lint036.py -q
42 passed in 0.09s
```

涵蓋：header 定位（命中／缺錨點報錯）、欄位對照全鍵命中、A–N 每項一正一反例
（D/I/J/M/N 因豁免分支較多，反例多於一項）、報告檔名 tag 推導。

## 5. 硬性約束自證

- 全程 `openpyxl.load_workbook(path, read_only=True, data_only=True)`；
  程式碼中無任何 `save`／`Workbook.save` 呼叫（`grep -n "save" scripts/lint036.py`
  零命中）。
- 執行前後比對 8 本 xlsx mtime，全數維持原值（最新者為 2026-08-20 15:09，
  無任一為今日）。`/Users/peihe/Work/02_Project_R1LR/` 下今日異動者僅
  Finder 產生之 `.DS_Store`，非本包寫入。
- 開檔時 openpyxl 發出 `Data Validation extension is not supported and will be
  removed` 警告——此為讀取期告知，因未 save 而不落盤，x14 下拉未受影響。
- git 操作零項。
- 檔案取得以 glob 加「命中非一檔即中止」守衛（`Bluetooth` 目錄下 BT 有
  0611／0729 兩本，故樣式含日期段），未猜檔。

## 6. 與下放包規格之偏離（2 項，均為規格內部衝突所迫）

1. **argparse 多一旗標 `--length-limit`**：檢查 L 明訂「閾值 CLI 可調，待 R-3
   定案」，但 argparse 規格未列該旗標。取兩者交集不可行，故新增旗標，預設 50，
   不改變預設行為。
2. **報告檔名日期取系統當日**：規格要求輸出 `{tag}_20260821.md` 但未提供日期
   來源旗標，故以 `date.today()` 生成；今日執行結果與規格字面一致。

上述兩項不新增裁決需求，僅回報。

## 7. 規格層發現（不自行改規格，待裁定）

- **N 尾句號與 `NA` 佔位衝突**：M 檢查將 `NA` 視為合法三態值，N 檢查之豁免表
  僅列 `$` 指令行與縮排續行，未豁免 `NA`，故每列 input=`NA` 均計為 N 違規。
  已照抄實作並以 `test_n_exempts_nothing_for_na_placeholder` 固化此行為。
- **N 於現有語料近乎全量觸發**（Media 7093／Projection 9047）：8 本工作簿的
  行尾句號慣例與 N 規則相反。此為規則與語料之系統性衝突，非個案違規；
  N 之閾值或方向需裁定後才具 gate 價值。
- **J「首個含字母 token」對數字開頭行誤判**：如
  `4. 5 sources are displayed…`，首個含字母 token 為 `sources`（小寫）而被標記，
  但該行實為 `5` 開頭、語法正確。Media 8 筆 J 全屬此型。
  建議 J 改為「首個 token（含純數字）」判定，待裁定。
- **K「六欄」定義未明**：規格僅寫「六欄」而欄位鍵有八個。本版取
  test_item/pre/input/proc/er/spec（排除 test_set 詞彙欄與 author）。
  Media K=0 於任一組合皆成立，故校準無法區辨此選擇，待確認。
- **I 之兩子型**：規格於 I 下同時定義「缺括號」與「sibling 逐字相同」，
  但基準僅給 I(缺括號)=2。本版分列為 `I` 與 `I-sibling` 以免混淆基準。

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項：**

1. **J/M/N 三檢查無實測基準**：本包僅能自證「實作符合規格文字」，無法自證
   「規格文字符合意圖」。8 本違規總計 35,700 筆，其中 J=68、M=208、N=31,683，
   三者合計 31,959 筆、占 89.5%（N 單項即占 88.7%）。在取得基準前不得進 gate。
2. **G 詞彙表外值未驗**：規格明載「詞彙表外值檢查待 framework 詞彙表接入後
   啟用，本版僅報空值」。Home G=216 全為空值型；BT G=8、HandsFreePhone G=29
   亦然。詞彙表接入後 G 數字必然上升，現值非最終值。
3. **K 分級未驗**：規格載明雙語制／UI 標籤／工作備註三級待 R-5 裁定。
   BT K=1058、Projection K=648 目前為未分級總量，其中含大量規格引用原文
   （如 AC 條款中文）與 UI 中文標籤（如 `"适配器"`），兩者性質不同，
   現值不可直接當違規數解讀。
4. **L 閾值未驗**：50 為暫定值（待 R-3）。BT L=375、Projection L=91 對閾值
   高度敏感，閾值定案前該欄數字僅供分佈觀察。

另聲明：本包未對 8 本以外之 036 工作簿跑檢查（同目錄下另有 50 餘本歷史版本），
亦未跑 gate 模式——兩者皆按下放包範圍排除，非遺漏。

## 9. 引用之既有裁決

- **R-TM7**（argparse 先定義後書寫）：CLI 規格於 `00_lint_bootstrap.md` 已先行
  定義，實作照其書寫；偏離 2 項見第 6 節。
- **R-VS18**（第一任務即寫上繳）：本文件即為第一任務產出。
- **S5 上限**（單包新增待裁決新規 ≤ 上限）：本包新增需 Pei 裁定之新規 **0 條**；
  第 7 節五項均為既有規格之內部衝突回報，非新規提案。
