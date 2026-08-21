# 下放包 00b：lint036 規格修訂（批 0 覆核後修正）

批 0 判定：**條件性通過**。A–L 之中 11 項校準命中、pytest 42 綠、
8 本報告齊、唯讀自證充分（mtime 未變、grep save 零命中、git 零項）。
三項需修，其中一項為執行層實作方向錯誤，兩項為分析層規格缺陷。

## 修訂 1：N 檢查方向錯誤（實作，非規格）

**實測（分析層，沙箱副本，唯讀）**：8 本 pre/input/proc/er 四欄、
strip 後非空行合計 39,745 行；其中行尾匹配 `[.。]$` 者 6,704 行
（16.9%）。分佈：HFP 2112/2565(82.3%)、DealerMode 1304/1906(68.4%)、
AMFM 2916/5077(57.4%)、Home 369/2386(15.5%)、Media 2、Projection 1、
BT 0、PM 0。

**證據**：Projection 報告明細行寫「行尾**缺**句號」，且列出
`1. Trigger vehicle system shutdown`（無句號）為違規。規格 N 之
定義為「行尾 `[.。]$`」= 命中句號即違規（canon §11「No trailing
period ... strip the final `.`」）。實作取反。

**判定**：規格無誤，實作反向。修 lint 不修規格。
- 上繳所稱「語料與規則系統性相反」不成立 —— 該結論係反向實作
  之產物；BT/Media/PM/Projection 四本實為 0.0% 尾句號（合規）
- 上繳所稱「M 之 NA 三態與 N 衝突」同樣不成立 —— input 恰為 `NA`
  之 2,441 列在正確方向下 N 命中 0（`NA` 不以句號結尾）
- 修正後 N 真值 6,704；8 本總違規由 35,700 降至約 10,700
  （精確值以修正後重跑為準，勿沿用本估值 —— §5a 不以推估為據）

提出質疑本身正確，且未自行改規格、誠實標「未校準」——
此行為符合規範，予以確認。

## 修訂 2：J 首字大寫誤判（規格缺陷，分析層）

原規格「首個含字母 token」導致 `4. 5 sources are displayed`
跳過數字 `5` 而判 `sources` 小寫違規（Media 8 筆全屬此型）。

**新定義**：去除行號後之**第一個 token**若非以字母開頭
（數字、`$`、引號、符號），該行**豁免 J**，不再往後尋找。
僅當第一個 token 以字母開頭且該字母小寫、且不match豁免表
(a)(b)(c)(d) 時，方為違規。

## 修訂 3：K 欄位範圍明確化（規格缺陷，分析層）

「六欄」定義為：`test_item`、`test_set`、`pre`、`input`、`proc`、
`er`（不含 `spec`、`author`、`remarks`）。分析層原實測即用此六欄。
K 分級（雙語制／UI 標籤／工作備註）仍待 R-5。

## 接受之偏離（無須改）

`--length-limit` 新增：接受，補入 argparse 規格。
報告日期 `date.today()`：接受。

## 新發現須登記（分析層將納回修計畫）

PM I-sibling=104：104 列括號行逐字重複，違 S4 sibling 區分。
登記為 M15，不在本包處理。

## 執行指令

```bash
cd /Users/peihe/Work_Projects/TC_Generator
# 1. 修 lint036.py 三處：N 反向、J 首 token 規則、K 六欄
# 2. 更新 tests/test_lint036.py：N 正反例對調並加註；J 加
#    「數字開頭行豁免」案例；K 加六欄邊界案例
pytest tests/test_lint036.py -q
# 3. 全 8 本重跑，覆蓋原報告
python3 scripts/lint036.py <8 本路徑> --report-dir docs/fw036/lint_reports
```

## 校準基準（修訂後，Media 0625）

A=0 B=0 C=1 D=0 E=1 F=0 G=0 H=0 I=2 K=0 L=0 **N=2 J=0**（新增校準）。
J 由 8 降為 0 即證修訂 2 生效；N 由大數降為 2 即證修訂 1 生效。
不符即 lint 有誤，修 lint 不修基準。

## 上繳

`docs/fw036/upstream/00b_lint_revision.md`：修訂前後對照表、
新校準結果、pytest 結果、8 本新總違規數（各檢查分項）、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。
本包新增需 Pei 裁定之新規：0 條。
