# 06 下放包 — 02 輪啟動指令（取代 03）

分析層寫入，2026-08-20。`03_round01_prompt.md` 標為 SUPERSEDED：
其「W-9 做完必停」已因 R-VS7 裁定而解除，且文書補寫項已完成。

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/docs/handoff/05_rulings.md        **裁決正文**
  features/vehicle_setting/docs/handoff/04_review_round01.md 現況與待驗
  features/vehicle_setting/docs/handoff/02_coverage_baseline_correction.md
00～03 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 先落裁決（本輪第一件事）

Pei 已全案裁定。05 包 §1–§10 之十條區塊**逐字轉錄**入
features/vehicle_setting/RULINGS.md（不摘要、不以編號代替）；
依 05 §11 套用 ANOMALIES.md 之狀態變更
（A-VS01 除役／A-VS06 → A-VS06′ 除役／A-VS18 除役／A-VS21 新開）。

## 作業（此順序）

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
       **「做完必停」已由 R-VS7 解除** —— 其產出改為委派句之來源
       對照表，做完併入本輪上繳，不中斷
W-16′  於 W-16 產物補一行：Categorization 值域全集
       （Functional Requirement 237／Heading 25／Information 8／
         information 1，合計 271，無其他值、無空值）

## 禁區

git 寫入性操作一律不執行，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
.gitignore 之修改屬 Pei（R-VS16），不得自行改。

## 升級條件

W-8 出現三來源不一致；實測與 02／04／05 包之數字不符；
撞到 §8.4.1 編造壓力；需要判斷而無條文。
**本輪無「必停」項。**

## 仍開啟（不得預設答案）

DR-11（CFTS100，1 leaf）／DR-5-B（失效彈窗＋PDO 圖示，17 leaf 之畫面層）
／DR-7（PROXI 表）／DR-8（VC_VEH_LINE 車型碼）。
遇到需要它們的判斷 → 依 R-VS17 標 BLOCKED 或登記待判，繼續其他作業。

## 完成後

本輪上繳後之下一步為 framework Part Vehicle Setting ＋ profile（Tier 2），
再首批生成，再 pilot（唯一必要人工 gate）。**本輪不做這三項。**
```
