# 下放包 02 — Popup 值來源接線＋工具修＋Pilot 生成

日期：2026-08-27
Feature slug：`popup`
前置：上繳包 01 覆核完畢；Pei 已裁 A-POP1～A-POP4 處置（R-POP6～R-POP11，
2026-08-27）。P2（DECISIONS.md 簽署）與 commit 由 Pei 於本包起跑前完成；
未簽則本包停在 §六-0。

## 禁區

- git 一切操作屬 Pei（R-G5）
- `sources/raw/` 落檔後不改；`forms/Pop Up List HMI R1 (26PI).xlsx` 唯讀
- xlsx 只准在 `sandbox/` 修改（R-G25）；不得以 openpyxl `wb.save()` 寫回
  母本衍生簿（R-G3），寫回一律 `backend/xlsx_surgical.py`

## 背景

037 V0.2 之 5 leaf（SWE1-POP-002-01～-05）全數為 popup 關閉行為。
A-POP2 查證後 Pei 納入 Pop Up List（R-POP6），DR-POP1 結案 —— 原定
落 PENDING 之 3 個 leaf 改填實值。本 feature 無 done region，pilot 為
唯一人工閘（同 time_management 形態）；本包之生成即 pilot 批（全量）。

## 裁決引用（R-G13）

R-POP6～R-POP11 全文見 `features/popup/RULINGS.md`（本輪新立，sha8 於
§六-1 重產 tsv 後以實值回報）；另引 R-G3、R-G5、R-G10、R-G25、G-B、
G-K、G-N（canon FO §9）。framework 已鎖定：`features/popup/framework.md`
（分析層落檔，本包生效前提）。

## 六、作業清單

0. **前置確認**：DECISIONS.md 已簽（P2）；工作樹乾淨（Pei commit 已入）。
   未達即停，回報不起跑。

1. **R-POP11 — rulings_hash 範圍擴充**：`scripts/rulings_hash.py` 預設
   範圍納 `features/*/RULINGS.md`，重產 `docs/fw036/RULINGS.sha.tsv`。
   invariant：既有條目 sha 逐列比對前後版，**任一既有列變動即停下回報**。
   新增列數回報（預期含 R-POP1～11 共 11 列；他 feature RULINGS.md 之
   新增列數為實測值，本包不預估——分母未量測）。

2. **R-POP10 — lint_docs036.py 跳號檢查改自動抽取**：前綴自動抽取
   `(A|DR|R)-[A-Z]+`＋G-B 差集回報（抽得前綴集 vs 原硬寫清單）。
   迴歸兩向（G-K／G-N）：
   (a) 已知案例轉受檢：A-POP／DR-POP 現身受檢清單
   (b) 注入向：scratch 副本注入一個跳號（如虛構 A-POP9 而無 A-POP5～8
   之連號）實證 FAIL，修回後 PASS。
   缺陷原文以字面釘入測試（G-N：不以當前語料為案例）。

3. **R-POP9 backlog — sanitizer 傳染性掃描**：掃 `scripts/` 內名稱
   正規化／檔名淨化函式（`safe_name` 同型：strip、replace、casefold 缺席），
   逐支回報「有無 A-POP1 同缺陷（前導剝除／大小寫不敏感撞名）」。
   只掃只報，不逕改（發現者登 anomaly 附建議處置）。

4. **值來源接線（R-POP6）**：
   - feature.yaml `paths.popup_list` = `../../forms/Pop Up List HMI R1 (26PI).xlsx`（相對路徑實測可達後寫入）
   - 產 `features/popup/data/popup_list_candidates.tsv`：三類候選逐列
     （PU id／Module／Timeout (sec)／Exit Conditions／String 摘 60 字／類別標記）：
     (a) timeout 類：C 欄 strip 後為純數字者
     (b) touch-outside 類：D 欄含 `outside`（不分大小寫子字串）
     (c) keyboard 類：D／E／G 欄含 `keyboard`（不分大小寫子字串）
   - 來源 sha 對照隨 tsv 附（G-F 靜態轉錄加指紋）

5. **Pilot 生成（全量一批）**：5 leaf → TC，工作簿 `sandbox/` 作業：
   - 值選定原則：-002-01 自 (a) 類選定一 PU（選定理由入 reasoning：
     台架可觸發、timeout 為純數值秒數者優先）；-002-03 自 (b) 類；
     -002-05 以 GP4 原文之 search keyboard 例為準，自 (c) 類查對其 PU，
     **查無對應列即停下回報**（升級條件，不改用他例）
   - -002-02 之 H/K vs UI 按鈕 sibling 軸（IN §8.3 device 軸）由生成
     判斷拆或不拆，reasoning 述明；拆則兩 TC 同引 -002-02（IN §8.2.2）
   - spec_reference 依 framework Part IV（-002-02 併列 `_5.5`＋`_5.6`，
     R-POP8；其餘單行 `_5.6`）
   - Heading 2 列台帳標記依 R-POP5；Test Group `Popup`／Test Set
     `Pop-up Close` 逐列寫入（BLANK＝FILL，FO §2.1）
   - PENDING 預期 **0**（DR-POP1 已結；DR-POP2／3 不阻欄位）
   - lint 全跑＋`gate_all.py`

## 預期數字（[MANUAL]；popup_list 三類為分析層 2026-08-27 對 forms/ 原檔實測）

| 項 | 預期 | 量測條件 |
|---|---|---|
| PU 母體 | 1340 | Main r3 起，A 欄 `^PU\d`，逐列 |
| (a) timeout 純數值列 | 240 | C 欄 strip 後 `^\d+(\.\d+)?$`，逐列（"5 seconds"／"30 sec" 等帶單位者不計入本類） |
| (b) outside 列 | 102 | D 欄含 `outside`，不分大小寫，子字串 |
| (c) keyboard 列 | 15 | D／E／G 欄任一含 `keyboard`，不分大小寫，子字串 |
| 生成 TC 數 | 5–7 | -002-02 拆分±1、其餘各 1；逐 TC |
| PENDING 佔位 | 0 | 全簿全欄，字串 `PENDING:` |
| RULINGS.sha.tsv 既有列 sha 變動 | 0 | 逐列前後比對 |
| lint | 全綠 | gate_all 五支；canon_refs 既存 463 不因本包增減（本包新檔引用一律帶前綴，R-G18） |

## 七、上繳要求

- 預期數字對照（相符者亦列）；不符停下不調和
- R-G13 引用表（R-POP1～11 之 sha8 實值，取自重產後 tsv）
- R-POP10 迴歸兩向之實跑輸出；sanitizer 掃描清單
- pilot 語料全文（generated/ json）＋逐 TC 自查表人工項勾檢（R-G21）
- 三分法、掃描條件揭露、獨立判斷、gate 實跑輸出

## 八、升級條件

- §六-0 前置未達；tsv 既有列 sha 變動；popup_list 三類計數不符
- -002-05 之 search keyboard 於 Pop Up List 查無對應列
- -002-03 之 (b) 類候選皆不可台架觸發
- lint 新規誤傷既有台帳（差集含非預期前綴）
- 任何值須造而來源無載（IN §8.4.1 → 停下，勿 PENDING 勿造，此情境
  理論上不應出現，出現即為 R-POP6 之前提有誤）

## 九、未結 DR 清單（IN §8.4.3）

DR-POP2（Priority Matrix **Post 2A 現版**，repo 僅存 SR24 1A 舊版）、
DR-POP3（POP-004 懸空引用）—— 已登記未送出。DR-POP1 已 RESOLVED
（R-POP6，不送上游）。全文見 `features/popup/DATA_REQUESTS.md`。
