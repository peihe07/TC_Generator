# 03 下放包 — 01 輪啟動指令

分析層寫入，2026-08-20。短式：脈絡在 repo，指令只點路徑與順序。

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                     流程權威
  features/vehicle_setting/docs/handoff/01_review_and_rulings.md
  features/vehicle_setting/docs/handoff/02_coverage_baseline_correction.md
01/02 為現行依據；00～00J 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 先補文書（本輪第一件事）

上一段（W-0c／W-16／W-18）之工作已完成、報告已落
docs/reports/w16_w18_leaf_universe.md，**但上繳包未寫、INDEX 未更、
ANOMALIES 與該報告互相矛盾**。先補齊：

1. 寫 docs/upstream/01_leaf_universe.md，含 canon §8.2 之必要成分
   （預期 vs 實測逐項、掃描條件揭露、三分法分類、獨立判斷）
2. 更新 docs/INDEX.md：新增 NN=01 列；並修 NN=00 列之兩處過時
   —— 「34 未覆蓋」改記為「237 可測 leaf／0 缺口」（R-VS15）、
      「W-13 約 112 檔」改「107」
3. 修 ANOMALIES.md 四處：
   A-VS01 → 除役（037 Categorization 對 SYS2 Category 逐 leaf 零錯配，
            25 個 Heading 為兩份文件各自正確標記，非錯配）
   A-VS06 → id 改為 A-VS06′（內容已改寫，id 未改）
   A-VS18 → 除役（recon 與 W-2 為兩判準數兩件事，recon 與 036 投影一致）
   A-VS20 → 新增：Categorization 大小寫不一致（information 一筆）。
            **措辭注意方向**：影響 Information 側計數（8 vs 9），
            不影響 Functional 母體界定（區分/不分大小寫皆 237）
4. 位元層核對兩處疑似多位元組毀損，回報但不逕改：
   ANOMALIES.md 之 A-VS06 列「相異 259」後
   handoff/00_intake_and_rulings.md §1 第 6 點「沙」字後

## 再跑殘項（此順序，不得調換）

W-8    三來源 $變數$ 對照 → data/spec_variables.tsv
       CFTS044 內嵌值域（兩式：`$var$ = [值]`、`路徑.名稱 == "值"`）
       ／DBC VAL_ ／LID 表 Format。**三者不一致逐項列出並停**
W-13   /Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/
       'R1LR SR26 ATL-H'/26PI2.5/HMI/ 全文掃描（實測 107 檔）
       關鍵詞 Fail_Present / STATFailSts / 'Heated Steering Wheel Icon'
       / 'Left Side' / 'Right Side'。唯讀，不複製任何檔案
W-15b′ DBC ↔ LID 表逐屬性交叉（本 feature 所用之 message／signal）
W-17   LID 列數差 6 之追因；TRUNCATED_ENUM 之其他形態
W-9    Comfort 逐條對照 → docs/reports/comfort_overlap.md
       **本 feature 側母體為 237 個 Functional leaf，非 271**
       **做完必停**，等 R-VS7

## 禁區

git 寫入性操作一律不執行，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。

## 升級條件

W-8 出現三來源不一致；W-9 完成；實測與 01/02 包之數字不符；
撞到 §8.4.1 編造壓力；需要判斷而無條文。

## 尚未裁定

R-VS7（待 W-9 素材）／R-VS9 v2／R-VS10。
R-VS8、R-VS11 撤回、DR-10 撤銷、R-VS15 待 Pei 追認 —— 本輪依現行版作業。
```
