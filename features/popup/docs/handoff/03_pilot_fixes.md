# 下放包 03 — Popup pilot 修正、-002-05 補生成、台帳一致性

日期：2026-08-27
Feature slug：`popup`
前置：下放包 02 已完成並入庫；pilot 四條經分析層覆核；A-POP6～A-POP9
四件已裁（R-POP12／14／16／17），A-POP5 之處分（改 `xlsx_surgical`）追認。

## 禁區

- git 一切操作屬 Pei（R-G5）
- xlsx 寫入**一律** `backend/xlsx_surgical.surgical_save`；
  **不得** `openpyxl.save()`（A-POP5 已實證其會靜默刪除 R10:R1411 之
  x14 下拉，這是 R-G3 存在的具體理由）
- `forms/Pop Up List HMI R1 (26PI).xlsx` 唯讀；`sources/raw/` 不改
- 甲類真陽性（sxm／audio_mgmt／time_management 之跳號）**不代改他 feature
  台帳**，只造清單（R-POP16 甲）

## 裁決引用（R-G13）

R-POP12～R-POP17 全文見 `features/popup/RULINGS.md`（本輪新立／更正）。
另引 R-G3、R-G5、R-G13、G-D、G-K、G-N。
**注意**：R-POP12／13／14 之 anomaly 掛號於落檔後曾更正一次（分析層轉抄
上繳包摘要之號碼所致，A-POP9(1)）；引用時以 repo 現行文為準，勿引本
對話早期版本。

---

## 一、分析層之誤（先行揭露）

R-POP12／13／14 初落檔時分別掛 A-POP6／A-POP8／A-POP7，與 repo 台帳
不符 —— 分析層轉抄了上繳包之聊天摘要而未 live 查 `ANOMALIES.md`。
已更正為 A-POP7／A-POP9／A-POP8，並將此失手寫入 R-POP15 F5 之註。
**分析層與執行層同受 R-POP17 第 1 項之規。**

## 二、pilot 六件修正（R-POP15，逐件）

對 `features/popup/generated/pilot_01.json` 之四條全數適用：

| # | 修正 | 範圍 |
|---|---|---|
| F1 | Final Step 補 check target：`Read <對象> and check that <可觀察結果>` | 四條之末步驟 |
| F2 | Procedure 之按壓標的改 `"..."`；PU 記法保留僅及 ER 引文段與 test_item；反引號等 Markdown 全數移除 | POP-002 步驟 1／2、POP-004 步驟 2；全欄掃 Markdown 記號 |
| F3 | 刪 `The vehicle is stationary with the ignition in RUN` 類前提句 | 四條之 pre_conditions |
| F4 | timeout 值單一欄位歸屬：`input_test_data` 一律 `NA`，值內聯於 Procedure／ER | POP-001／003／004（POP-002 已為 `NA`，不動）|
| F5 | reasoning 之 anomaly 號 live 查後改寫 | POP-002 之「登 A-POP7」自我循環 |
| F6 | POP-002 之 reasoning 改寫為 R-POP12 之理由（規格側無此分支），**刪去「真軸但無實例」一說** | POP-002 |

F3 之連帶：刪除後 POP-003 之 pre_conditions 第 2／3 項（Profile 存在、
All Profiles tab 可達）**保留** —— 那是該 TC 之規格觸發前提，非環境穩定性。
F4 之連帶：POP-001 之 `Time-out = 5 s` 已於 ER 3 具名，`input_test_data`
改 `NA` 不損失資訊。

## 三、TC ID 重排（R-POP13）

- `feature.yaml` 之 `project` 模板殘值 `PROJ` → 正確值
- TC ID 全數重排為 `NR1L-Popup-001` ～ `NR1L-Popup-005`，NNN 序不變
  （-002-01→001、-002-02→002、-002-03→003、-002-04→004、-002-05→005）
- 重排後全簿掃 `newR1L`／`PROJ`／`POP-`，命中須為 0

## 四、-002-05 補生成（R-POP14）

- 照 GP4-4 規格原句生成一條 TC，`spec_reference` 單行
  `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.6`
- **不引 PU**、**不落 PENDING**、**不列舉 search keyboard 以外之實例**
  （IN §8.4.1；PU0022／PU0023／PU0861 皆不得代入）
- 受測情境即規格自舉之 search keyboard：TC 以「popup 內作出選擇後
  popup 仍保持開啟」為驗證命題，procedure 之鍵盤實例以規格措辭表述，
  不宣稱其為某具名 PU
- test_item 下半（括號）須與其餘四條可區分（IN §4.3.1）
- 若生成過程中發現非造值不可 → 停下回報（不得 PENDING、不得造值）

## 五、工具二修

1. **R-POP16 乙**：`lint_docs036.py` 之「編號重複」改為同一表格內重複才
   判紅，跨表降 note；前綴抽取限定於**檔內首個表格**。
   迴歸兩向（G-K／G-N）：
   (a) `power_moding` DR-PMH1、`projection` A-PJ37 由紅轉綠，且
       `privacy` 之假前綴 `S` 消失 —— 三者逐一實證
   (b) 注入向：於 scratch 副本之**主表內**注入真重複，實證仍 FAIL
   （只放寬跨表，不得把真重複一起放掉）
2. **R-POP16 丙**：抽得前綴集為空時明示回報 `no series detected`，
   不得靜默 PASS。以 amfm／home／media／user_profiles 四者實證輸出改變。
3. **R-POP17 第 2 項**：`ledger_xref.py` 增一檢 —— 掃 `docs/handoff/`、
   `docs/upstream/` 內之 `A-\w+\d+`／`DR-\w+\d+` 引用，與該 feature 台帳
   之實存號碼**及其標題**對照，對不上即回報。
   迴歸：以本輪 A-POP9(1) 之實況（R-POP12 曾掛 A-POP6）為固定案例釘入
   測試 —— 缺陷原文字面入測，不以當前語料為案例（G-N）。

## 六、R-POP16 甲之清單（只造不改）

sxm `A-SX18`／`A-SX19`、audio_mgmt `DR-AM7`、time_management `A-TM2`
之跳號，逐筆寫入**各該 feature 之 BACKLOG**（若無該檔則建立），
註明「由 popup R-POP10 之前綴自動抽取浮現，2026-08-27，未代改」。
**不動各該 feature 之 ANOMALIES.md／DATA_REQUESTS.md 本體。**

## 七、寫回與 gate

- `sandbox/` 作業，`surgical_save` 寫回，落檔後以 `zipfile` 直讀複驗
  x14 DV 存活（`f=下拉選單!$A$1:$A$9`、`sqref=R10:R1411`）
- `lint036.py --profile popup` 全跑；`gate_all.py` 五支
- `rulings_hash.py` 重產 tsv（R-POP12～17 新增，既有列 sha 不得變）

## 八、預期數字（[MANUAL]）

| 項 | 預期 | 量測條件 |
|---|---|---|
| TC 總數 | 5 | `generated/` 之 JSON 陣列長度，逐條 |
| PENDING 佔位 | 0 | 全簿全欄字串 `PENDING:` |
| `newR1L`／`PROJ` 殘留 | 0 | 全簿＋feature.yaml＋generated/ 字串掃 |
| Markdown 記號殘留（反引號） | 0 | 五個交付欄逐 item 掃 |
| `input_test_data` = `NA` 之條數 | 5 | 逐條字串等值比對 |
| pre_conditions 含 `ignition in RUN` | 0 | 全條掃，不分大小寫 |
| Final Step 含 `check that` | 5 | 逐條末步驟掃 |
| spec_reference 兩行者 | 1（POP-002）| 逐條行數 |
| 既有 R-G 條 sha 變動 | 0 | tsv 逐列前後比對 |
| x14 DV | 1，存活 | `zipfile` 直讀輸出 sheet xml |
| lint／gate | 全綠；canon_refs 既存 463 不增減 | gate_all 五支 |

## 九、上繳要求

- **摘要一律自 repo 台帳 live 產**（R-POP17-1）—— anomaly 號與狀態尤其；
  手寫重述即為 A-POP9 之再犯
- 預期數字對照（相符者亦列）；不符停下不調和
- R-G13 引用表（R-POP12～17 之 sha8，取自重產後 tsv）
- 工具二修之迴歸兩向實跑輸出（含「只放寬跨表、真重複仍紅」之實證）
- 三分法、掃描條件揭露、獨立判斷、gate 實跑輸出
- 五條 TC 全文

## 十、升級條件

- -002-05 之生成須造值（停下，不 PENDING 不造）
- F3 刪除後某條 TC 之前提不足以執行（回報，勿自行補回）
- lint 放寬後真重複亦轉綠（判準過寬，停下）
- tsv 既有列 sha 變動
- 甲類清單寫入時發現該 feature 之台帳與 popup 側所見不符（勿代改，回報）

## 十一、未結 DR 清單（IN §8.4.3）

DR-POP2（Priority Matrix Post 2A 現版）、DR-POP3（POP-004 懸空引用）、
DR-POP4（multi-task popup 例外清單＋search keyboard 之 PU 具名）。
DR-POP1 已 RESOLVED。三者皆「已登記，未送出」，皆不阻斷本包。

## 十二、留給 Pei 之未決項（本包不處理）

A-POP2 §四-3：`forms/` 之落點政策 —— R-G2 字面為「`forms/` 只保留
`…_SWQT_20260817_ext.xlsx`」，但實際已收 LID／DBC／PROXI／HMI Settings
List／Pop Up List 等共用參考件，且兩件 Pop Up 未登錄於 `forms/FORMS.md`。
是否移入 `sources/raw/` 並入 `MANIFEST.tsv`，屬全域政策，待 Pei 裁。
