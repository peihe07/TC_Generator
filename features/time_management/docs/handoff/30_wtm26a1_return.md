# 30 — W-TM-26-A1 回繳（rev A, 2026-08-25）

上游包：`28_wtm26a1_testitem.md`（§7 三項決議：Q1 裁 (b)、VES KEEP、
P3 結案）。全部解鎖後一輪執行 T1–T4。

基準：0825 輸出件 SHA `b45659624330c5d7578481d6b3d9989fea72697066b37ba1dc137ff95c0fe483`
輸出：`output/…_SWQT_20260825-A1.xlsx`（`--out`，R-G19-2）
SHA256 `717d48d8fb0b5e44117f4ac0bb4e26eed5c87f243a1630b6212ece9ff0e78f65`
dry-run 先行（R-G19-1）：已執行，tc_id 起訖與 test_group 於 dry-run 即確認。

---

## §1 完成度

| 工作 | 內容 | 狀態 |
|---|---|---|
| T1 | 59 條 test_item 下半改空行分隔＋首字母大寫（R-TM84） | 完成 59/59 |
| T2 | F 欄 59 列、G 欄 59 列回改（R-TM85） | 完成 |
| T3 | A-TM30 前提更正、A-TM31 登記並結案 | 完成 |
| T4 | 逐列 diff、lint、未結 DR | 本文 |

R-TM84／R-TM85／R-TM86 已謄入 `RULINGS.md` 並附執行層回報。
條數 85 → 88（含撤回）、83 → 86（不含撤回），增量 +3 相符（R-TM46／R-TM79）。

## §2 驗收 —— 全欄逐列 diff（R-G19-4）

比對 0825 → 0825-A1，**全 9 分頁、全欄、全列**：

| 分頁!欄 | 變更數 |
|---|---|
| Test Case Specification!F（TC ID） | 59 |
| Test Case Specification!G（Test Group） | 59 |
| Test Case Specification!I（test_item） | 59 |
| **其餘所有欄、所有分頁** | **0** |

**非受令欄變更 0 處** —— 驗收判準達成。

內容複驗：
- F 欄前綴唯一 `NR1L-TimeManagement-`，序號 001–059 連續（已驗）
- G 欄唯一值 `Time Management`
- I 欄 `\n\n(` ＋首字大寫 59/59；殘留單換行括號 0
- D5 對齊仍為 left+top 295 格；zip member 48→48；
  data-validation 計數（classic, x14）逐分頁相同

## §3 lint

```
lint_tcs.py --feature-dir .   → 檔 4；發現 0 項
lint_tcs.py --self-test       → 自驗 53 / 53
```

**self-test 一則紅向因 R-TM85 而失效，已修。** `test-group` 之紅向
fixture 原寫死 `"Time Management"` 當錯值，前提是「feature 名不是
Test Group」（R-TM8 之舊讀法）。R-TM85 定案 test_group ＝ feature 名之後，
該錯值變成正解，閘門正確地不叫 —— self-test 遂報「閘失效」（53 → 52）。

**閘門本身（`lint_test_group`：逐字等於 feature.yaml）未受影響**，
壞的是 fixture 之前提。錯值改取前一版之 `"Time and Date"` ——
既是真實可能之回歸，也保住紅向覆蓋；自驗回到 53/53。
同檔 `no-tc-id` 紅向之示例值一併由舊前綴更新（該判準為「攜帶 tc_id
即報」，值本身無關，僅避免誤導）。

> 此即 R-TM69(3) 之同型第三例：**條文變更會使以該欄位為判準之既有
> 檢查失效**。前兩例為 W-TM-26 之 `arch-column`（`27` §3）與本例。
> 差別在這次是 self-test 主動叫出來的 —— 紅向覆蓋在此付了它的租金。

## §4 A-TM30 ／ A-TM31（T3）

**A-TM31（新登記，已 RESOLVED）**：兩個「0822」為不同檔案 ——
ASW-R2 已送審件（`088a4476`，`NR1L-TimeManagement-` / `Time Management`）
與 repo output 0822（`2afd87be`，`NR1L-TimeAndDate-` / `Time and Date`）。
F/G 各 59 列之改名不在 W-TM-26 任何一項工作內，亦未於任何回繳包申報。
處置即 R-TM85 之回改，本輪執行完畢。

**A-TM30 前提部分更正**：本條原記成因為「`26` §0 之 SHA 抄錯」——
**不成立**。`088a4476…` 是 repo 外送審件之真實值；`27` §C1 只搜 repo 內，
把「repo 內查無」誤讀為「不存在」，並以一次「更正」抹去了
「兩個 0822 不同」這個真訊號。本條之建議（SHA 由腳本對宣告路徑實測）
仍成立且已由 R-G19-3 承接。

`26` §6 C1 與 `27` §7 均已加註推翻，原文照留不刪（R-TM13）。

## §5 未結 DR 清單（隨附義務）

DR-2（High）、DR-4（High）、DR-5（中）、DR-8（High）、DR-9（High）、
DR-10 四分項（High）、DR-12（開放）、DR-12b（High）、DR-20（High）。
DR-6 追溯用；DR-7 空號；DR-11 已取消。

工作簿 PENDING 處數 59（與 0825 件相同 —— 本輪三欄皆非 PENDING 承載欄）。

## §6 待 Pei

無。`27` §7 之 VES 項已由 R-TM86 裁定 KEEP；`28` §4 Q1 已由 R-TM85
裁定 (b)；P3 已結案。**W-TM-26 與 W-TM-26-A1 全部工作項關閉。**

送審件之前綴對照（若需附於 Revise note）：0825-A1 與 ASW-R2 已送審件
之 F/G 欄體系一致，序號亦一致 —— **不需對照表**。
