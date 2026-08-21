# 下放包 00：lint036 建置與校準（報告模式）

執行層：Opus5（Claude Code）。本包零裁決依賴、零內容修改、
零不可逆操作；R-1~R-5 / M 系列裁定前唯一可動工項。
本包新增需 Pei 裁定之新規：0 條（符合 S5 上限）。

## 任務

1. 建 `scripts/lint036.py`：對 036 工作簿跑檢查 A–N（規格見同目錄
   `00_lint_spec.md`，正則與豁免表照抄，勿自行重發明——該表為
   分析層對 2,489 列實測校準之結果）。
2. **僅報告模式**：輸出違規清單，不修改任何檔案。gate 模式留
   `--gate` 旗標但本包不啟用。
3. 對 8 本已交付 036 跑報告，輸出至 `docs/fw036/lint_reports/
   {tag}_20260821.md`。
4. 校準：Media 0625 實測基準（分析層已量測）：
   A=0 B=0 C=1 D=0 E=1 F=0 G=0 H=0 I(缺括號)=2 K=0 L(>50字)=0。
   lint 輸出與基準不符 → lint 有誤，修 lint 不修基準。
   J/M/N 無實測基準，報告值標「未校準」。

## 硬性約束

- 交付檔一律唯讀：`openpyxl.load_workbook(path, read_only=True,
  data_only=True)`。**絕不 save 任何 xlsx**（x14 下拉破壞風險）。
- 不寫入 `/Users/peihe/Work/02_Project_R1LR/` 任何位置。
- 標頭定位：掃前 15 列找含 `Specification Reference` 之列為
  header；TC sheet 名以 `Test Case Specification` 開頭。
- Python 3.10+、snake_case、pytest 測試（至少：header 定位、
  每檢查項一正一反例）。
- git 操作零項——commit 屬 Pei。

## argparse 規格（先定義後書寫，R-TM7）

```
lint036.py FILES... [--report-dir DIR] [--gate] [--json]
  FILES        一個或多個 .xlsx 路徑
  --report-dir 預設 docs/fw036/lint_reports/
  --gate       任一違規 exit 1（本包不啟用）
  --json       另輸出機讀 json
```

## 執行指令

```bash
cd /Users/peihe/Work_Projects/TC_Generator
mkdir -p docs/fw036/lint_reports
python3 scripts/lint036.py \
  "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Media/Media/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_MediaHMI_20260625.xlsx" \
  --report-dir docs/fw036/lint_reports
# Media 校準通過後，再跑其餘 7 本（路徑見 00_lint_spec.md 末節）
pytest tests/test_lint036.py -q
```

## 上繳（第一任務即寫，R-VS18）

`docs/fw036/upstream/00_lint_bootstrap.md`：校準結果對照表、
8 本報告路徑、pytest 結果、**「本包是否仍有該驗而未驗者」
獨立判斷**（不得省略）、引用之既有裁決編號清單（本包：R-TM7、
R-VS18、S5 上限自證）。
