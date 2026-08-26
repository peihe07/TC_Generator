# 上繳包 04 —— Vehicle Category：R-VC11(b) 修訂與 priority 定案（T25–T30）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層 / Pei
- 對應下放：`docs/handoff/04_priority.md`
  （SHA256 `9d9e9b10e9d2e1093d0bc319c32481aed60dc17c13801fac7b9c10a9be9194f7`，13,854 B）
- 前一包上繳：`docs/upstream/03_rulings.md`
- **結論：T25–T30 六項全數完成，無停點。priority 定案 P0 5 / P1 32 / P2 45 / P3 35。**
- 未產出任何 TC、未寫入任何 TC 欄位、未合併 `DECISIONS.md`、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T25 | 抄錄 R-VC13 / R-VC14 | ✅ 二條逐字；**十四條全驗通過**。R-VC11 原文未改，加註後複驗仍逐字未改 |
| T26 | A-VC10 新立 | ✅ 條文逐字 + 獨立重測；另查出一項**比條文更強的證據**（見 §3）|
| T27 | A-VC10 併入同批 A | ✅ 同批 A 現為四項；DR 未結維持七筆 |
| T28 | priority 定案 | ✅ `data/priority_final.tsv`；**異動 9 筆，分布與下放包 04 §三預期完全一致** |
| T29 | REV-09 / REV-10 | ✅ `docs/REVISIONS.md` 現十筆 |
| T30 | `DECISIONS` 差異 | ✅ 逐項列出，**含一項須先修再簽者**（見 §7）|

**一件請你先看**：`DECISIONS.new.md` §4 之 `spec_reference: [PROPOSED: None]`
—— 那個 `None` 是 `spec_reference_template: null` 被 f-string 印出來的，
不是一個裁定值。簽在這上面等於簽了一個字面 `None`。詳見 §7.2。

---

## 1. T25 —— 抄錄與核對

抄入位置：`RULINGS.md`（R-VC13 行 419、R-VC14 行 453）。**十四條全驗**。

| 條 | 來源 | bytes | lines | sha256(前16) | 逐字一致 |
|---|---|---|---|---|---|
| R-VC1 | 包01 35–58 | 1,311 | 24 | `2344769c6998db1e` | 是 |
| R-VC2 | 包01 62–86 | 1,262 | 25 | `12c10f107cbe85ca` | 是 |
| R-VC3 | 包01 90–113 | 1,145 | 24 | `8dd3cbfa7fb69053` | 是 |
| R-VC4 | 包01 117–143 | 1,361 | 27 | `b7aeb14a67bf05d8` | 是 |
| R-VC5 | 包01 147–164 | 1,026 | 18 | `de1debf16da7e164` | 是 |
| R-VC6 | 包02 84–109 | 1,617 | 26 | `28119d9877a36cf3` | 是 |
| R-VC7 | 包02 113–129 | 957 | 17 | `2d74bfedacce38ee` | 是 |
| R-VC8 | 包02 133–159 | 1,612 | 27 | `39087f49494aa651` | 是 |
| R-VC9 | 包02 163–193 | 1,619 | 31 | `71ef7e57c6fd6308` | 是 |
| R-VC10 | 包02 197–227 | 1,749 | 31 | `bd8b65d4acc0c457` | 是 |
| R-VC11 | 包03 50–89 | 2,251 | 40 | `9287539d8972ce56` | 是 |
| R-VC12 | 包03 93–138 | 2,437 | 46 | `a1daceaa0e23bca8` | 是 |
| **R-VC13** | 包04 69–97 | 1,671 | 29 | `056a381abacfd2e7` | **是** |
| **R-VC14** | 包04 101–125 | 1,456 | 25 | `cb0a086cba19bb88` | **是** |

### R-VC11(b) 之作廢加註（R-TM13）

R-VC11 之 code fence **原字未刪、未改**，於其後加註一段引用區塊，
載明：(b) 已作廢、作廢理由（粒度錯配）、新 (b) 見 R-VC13、
以及 (a)(c) 繼續適用。

**加註後複驗**：以 `diff -q` 將 `RULINGS.md` 內之 R-VC11 fence 內容
與下放包 03 行 50–89 再比對一次 → **逐字未改**（sha `9287539d8972ce56`
與上表相同）。加註寫在 fence 外，未污染條文本體。

---

## 2. T28 —— priority 定案

腳本：`features/vehicle_category/scripts/t28_priority_final.py`。

**本輪未重做判定** —— 本地預判以 `importlib` 自 `t24_priority_draft.py`
匯入其 `LOCAL` 字典，不複製第二份，避免二處各改其一而分歧。
本輪只做兩件事：套 R-VC13 之章級驗算、套 R-VC14 之即時適用。

### 2.1 R-VC13 章級約束驗算（六章有約束者 + 五章不設約束者）

| 章 | 037 | leaf | 定案分布 | 約束 | 判 |
|---|---|---|---|---|---|
| 2 | Medium | 24 | `{'P1': 1, 'P2': 7, 'P3': 16}` | 不設約束 | 滿足 |
| 3 | Medium | 17 | `{'P2': 10, 'P3': 4, 'P1': 3}` | 不設約束 | 滿足 |
| **4** | **High** | 4 | `{'P1': 3, 'P2': 1}` | 至少一筆 ≥P1 | **滿足** |
| **5** | **High** | 3 | `{'P1': 3}` | 至少一筆 ≥P1 | **滿足** |
| **6** | **High** | 3 | `{'P1': 1, 'P2': 1, 'P3': 1}` | 至少一筆 ≥P1 | **滿足** |
| **7** | **High** | 2 | `{'P1': 1, 'P2': 1}` | 至少一筆 ≥P1 | **滿足** |
| 11 | Medium | 20 | `{'P2': 7, 'P1': 4, 'P0': 2, 'P3': 7}` | 不設約束 | 滿足 |
| 12 | Medium | 25 | `{'P2': 14, 'P1': 5, 'P3': 6}` | 不設約束 | 滿足 |
| **13** | **High** | 16 | `{'P1': 10, 'P2': 4, 'P0': 2}` | 至少一筆 ≥P1 | **滿足** |
| 14 | Medium | 2 | `{'P0': 1, 'P1': 1}` | 不設約束 | 滿足 |
| **16** | **Low** | 1 | `{'P3': 1}` | 不得高於 P3 | **滿足** |

**十一章全部滿足，零違反。** 與下放包 04 §一之驗算表逐章相符
（章 4 = P1,P1,P1,P2；章 5 = P1,P1,P1；章 6 = P1,P2,P3；章 7 = P1,P2；
章 13 = P1×10,P2×4,P0×2；章 16 = P3）。

> 腳本對「章不滿足」之處理為 `sys.exit(1)` 並印出違反清單 ——
> **不自行逐筆抬升以求滿足**（R-VC13 明禁）。本輪未觸發。

### 2.2 分布與異動

| | P0 | P1 | P2 | P3 | 合計 |
|---|---|---|---|---|---|
| 上繳包 03 之定案（含抬升）| 6 | 39 | 38 | 34 | 117 |
| **本輪定案** | **5** | **32** | **45** | **35** | **117** |

**與下放包 04 §三第 1 項所預期之定案分布完全一致。**

異動 9 筆：

| req_id | §節 | 037 | 03 包 | 定案 | 依 |
|---|---|---|---|---|---|
| `SWE1-HMI-VC-027` | 4.2 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-031` | 6.2 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-032` | 6.3 | High | P1 | **P3** | R-VC13 |
| `SWE1-HMI-VC-033-02` | 7.1 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-036-01` | 11.3 | Medium | P0 | **P1** | R-VC14 |
| `SWE1-HMI-VC-058-02` | 13.1.1 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-058-03` | 13.1.1 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-062-02` | 13.4.1 | High | P1 | **P2** | R-VC13 |
| `SWE1-HMI-VC-063-02` | 13.4.2 | High | P1 | **P2** | R-VC13 |

八筆 R-VC13 者**全部回歸本地判定**（`local_p` 欄可逐筆覆核，非另行判過）。

### 2.3 定案之五個 P0

| req_id | § | 類 | 依據 |
|---|---|---|---|
| `SWE1-HMI-VC-035-03` | 11.2 | data-loss | restore-defaults 之 Cancel **攔阻失效** → 設定被意外清空 |
| `SWE1-HMI-VC-036-02` | 11.3 | data-loss | clear-personal-data 之 Cancel **攔阻失效** → 個資被意外清除 |
| `SWE1-HMI-VC-062-01` | 13.4.1 | safety | 行進中 Wi-Fi 軟體下載之攔阻（駕駛分心）|
| `SWE1-HMI-VC-063-01` | 13.4.2 | safety | FOTA 流程中車輛起步之攔阻（駕駛分心）|
| `SWE1-HMI-VC-065-01` | 14.1 | safety | 行進中煞車服務模式須灰化 |

`VC-036-01`（選 Yes 清除個人資料）依 R-VC14(b) 為**執行失效** ——
該清而未清，資料仍在，非 data-loss，定案 P1。其隱私外洩風險依
R-VC11(c) 須記於該 TC 之 `reasoning`（本輪未產出 TC，義務隨定案傳遞）。

### 2.4 定案全表（117 leaf）

⬇ 標記者為本輪相對 03 包之下修。「本地」為 T24 之原判，未變。

| req_id | §節 | 037 | 本地 | 03 包 | **定案** | 依據 |
|---|---|---|---|---|---|---|
| `SWE1-HMI-VC-001-01` | 2.2 | Medium | P1 | P1 | **P1** | 主要導覽結構：頁籤集不成立則整個 feature 不可達 |
| `SWE1-HMI-VC-001-02` | 2.2 | Medium | P2 | P2 | **P2** | 首次進入之預設頁籤，錯了仍可手動切換 |
| `SWE1-HMI-VC-001-03` | 2.2 | Medium | P2 | P2 | **P2** | 回復上次頁籤，屬便利性 |
| `SWE1-HMI-VC-002` | 2.3 | Medium | P2 | P2 | **P2** | Specialty 頁籤之位置，錯位不阻斷取用 |
| `SWE1-HMI-VC-003` | 2.3.1 | Medium | P2 | P2 | **P2** | 頁籤排序 |
| `SWE1-HMI-VC-004` | 2.3.2 | Medium | P3 | P3 | **P3** | 字面標籤 |
| `SWE1-HMI-VC-005` | 2.3.3 | Medium | P3 | P3 | **P3** | 字面標籤 |
| `SWE1-HMI-VC-006` | 2.3.4 | Medium | P3 | P3 | **P3** | 可列入之 Specialty 列舉，開放式 |
| `SWE1-HMI-VC-007-01` | 2.4 | Medium | P2 | P2 | **P2** | 採用對照表為權威來源 |
| `SWE1-HMI-VC-007-02` | 2.4 | Medium | P3 | P3 | **P3** | 對照表單列：命名與位置 |
| `SWE1-HMI-VC-007-03` | 2.4 | Medium | P3 | P3 | **P3** | 對照表單列 |
| `SWE1-HMI-VC-007-04` | 2.4 | Medium | P3 | P3 | **P3** | 對照表單列 |
| `SWE1-HMI-VC-007-05` | 2.4 | Medium | P3 | P3 | **P3** | 對照表單列 |
| `SWE1-HMI-VC-008` | 2.5 | Medium | P2 | P2 | **P2** | 失敗＝少一個頁籤，非攝影機功能失效 |
| `SWE1-HMI-VC-009` | 2.5.1 | Medium | P3 | P3 | **P3** | 去重複，重複只是冗餘 |
| `SWE1-HMI-VC-010` | 2.6 | Medium | P2 | P2 | **P2** | 依配備過濾，未過濾則出現不可用項 |
| `SWE1-HMI-VC-011` | 2.6.1 | Medium | P3 | P3 | **P3** | Dashboard 內容排序 |
| `SWE1-HMI-VC-012-01` | 2.6.2 | Medium | P3 | P3 | **P3** | 橫向版面配置 |
| `SWE1-HMI-VC-012-02` | 2.6.2 | Medium | P3 | P3 | **P3** | 橫向版面配置 |
| `SWE1-HMI-VC-012-03` | 2.6.2 | Medium | P3 | P3 | **P3** | 橫向版面配置 |
| `SWE1-HMI-VC-013-01` | 2.6.3 | Medium | P3 | P3 | **P3** | 直向版面配置 |
| `SWE1-HMI-VC-013-02` | 2.6.3 | Medium | P3 | P3 | **P3** | 直向版面配置 |
| `SWE1-HMI-VC-013-03` | 2.6.3 | Medium | P3 | P3 | **P3** | 直向版面配置 |
| `SWE1-HMI-VC-013-04` | 2.6.3 | Medium | P3 | P3 | **P3** | 直向版面之尺寸與溢位 |
| `SWE1-HMI-VC-014` | 3.1 | Medium | P2 | P2 | **P2** | Controls 可列入項目之清單 |
| `SWE1-HMI-VC-015` | 3.1.1 | Medium | P3 | P3 | **P3** | 攝影機項目之分組 |
| `SWE1-HMI-VC-016` | 3.1.2 | Medium | P3 | P3 | **P3** | 條件式項目出現規則，罕用情境 |
| `SWE1-HMI-VC-017` | 3.2 | Medium | P1 | P1 | **P1** | 狀態回報：失敗則使用者依錯誤狀態操作車輛 |
| `SWE1-HMI-VC-018` | 3.3 | Medium | P2 | P2 | **P2** | 捷徑，非唯一路徑 |
| `SWE1-HMI-VC-019-01` | 3.4 | Medium | P2 | P2 | **P2** | 無狀態按鍵之語意 |
| `SWE1-HMI-VC-019-02` | 3.4 | Medium | P3 | P3 | **P3** | 按壓時不高亮，外觀細節 |
| `SWE1-HMI-VC-020` | 3.5 | Medium | P1 | P1 | **P1** | HMI 狀態須跟隨實際系統狀態，否則顯示與車態相悖 |
| `SWE1-HMI-VC-021` | 3.6 | Medium | P1 | P1 | **P1** | 置物箱鎖之 Privacy Lock 彈窗，屬存取控制入口 |
| `SWE1-HMI-VC-022` | 3.7 | Medium | P3 | P3 | **P3** | 雙螢幕之內容去重 |
| `SWE1-HMI-VC-023` | 3.8 | Medium | P2 | P2 | **P2** | 電控玻璃不跨鑰匙循環記憶 |
| `SWE1-HMI-VC-024` | 3.8.1 | Medium | P2 | P2 | **P2** | 車頂開啟時標為不可用並灰化 |
| `SWE1-HMI-VC-025-01` | 3.9 | Medium | P2 | P2 | **P2** | 採用 Controls Button Table 為權威來源 |
| `SWE1-HMI-VC-025-02` | 3.9 | Medium | P2 | P2 | **P2** | 按鍵狀態語意對照 |
| `SWE1-HMI-VC-025-03` | 3.9 | Medium | P2 | P2 | **P2** | 按鍵狀態語意對照 |
| `SWE1-HMI-VC-025-04` | 3.9 | Medium | P2 | P2 | **P2** | 按鍵狀態語意對照 |
| `SWE1-HMI-VC-025-05` | 3.9 | Medium | P2 | P2 | **P2** | 按鍵狀態語意對照 |
| `SWE1-HMI-VC-026-01` | 4.1 | High | P1 | P1 | **P1** | 啟用流程之入口彈窗 |
| `SWE1-HMI-VC-026-02` | 4.1 | High | P1 | P1 | **P1** | PIN 輸入彈窗，存取控制主流程 |
| `SWE1-HMI-VC-026-03` | 4.1 | High | P1 | P1 | **P1** | 兩次輸入確認，PIN 設定之核心邏輯 |
| `SWE1-HMI-VC-027` | 4.2 | High | P2 | P1 | **P2** ⬇ | 啟用成功之確認彈窗，屬回饋 |
| `SWE1-HMI-VC-028-01` | 5.1 | High | P1 | P1 | **P1** | 錯誤 PIN 之警示，存取控制回饋 |
| `SWE1-HMI-VC-028-02` | 5.1 | High | P1 | P1 | **P1** | 啟用流程不限制錯誤次數 —— 存取控制之明文性質 |
| `SWE1-HMI-VC-029` | 5.2 | High | P1 | P1 | **P1** | 正確 PIN 後啟用，主流程終點 |
| `SWE1-HMI-VC-030` | 6.1 | High | P1 | P1 | **P1** | 停用需同一 PIN，存取控制主流程 |
| `SWE1-HMI-VC-031` | 6.2 | High | P2 | P1 | **P2** ⬇ | 停用成功之確認彈窗，屬回饋 |
| `SWE1-HMI-VC-032` | 6.3 | High | P3 | P1 | **P3** ⬇ | 按 OK 關閉彈窗並返回，導覽細節 |
| `SWE1-HMI-VC-033-01` | 7.1 | High | P1 | P1 | **P1** | 三次錯誤鎖定 30 分鐘 —— 防暴力嘗試之核心規則 |
| `SWE1-HMI-VC-033-02` | 7.1 | High | P2 | P1 | **P2** ⬇ | 位數不足之驗證彈窗 |
| `SWE1-HMI-VC-034-01` | 11.1 | Medium | P2 | P2 | **P2** | 不適用之設定隱藏 |
| `SWE1-HMI-VC-034-02` | 11.1 | Medium | P2 | P2 | **P2** | key-off 不可用者灰化而非隱藏 |
| `SWE1-HMI-VC-035-01` | 11.2 | Medium | P1 | P1 | **P1** | 回復預設值確實生效 |
| `SWE1-HMI-VC-035-02` | 11.2 | Medium | P2 | P2 | **P2** | 回復完成之確認彈窗 |
| `SWE1-HMI-VC-035-03` | 11.2 | Medium | P0 | P0 | **P0** | **資料遺失風險**：Cancel 若未攔住，使用者設定被靜默清空 |
| `SWE1-HMI-VC-036-01` | 11.3 | Medium | P0 | P0 | **P1** ⬇ | R-VC14(b) 執行失效：該清而未清，資料仍在，非 data-loss；隱私外洩風險依 R-VC11(c) 記於 reasoning |
| `SWE1-HMI-VC-036-02` | 11.3 | Medium | P0 | P0 | **P0** | **資料遺失風險**：Cancel 若未攔住，個人資料被靜默清除 |
| `SWE1-HMI-VC-037-01` | 11.4 | Medium | P1 | P1 | **P1** | 懸吊模式互斥 —— 車輛動態設定之關鍵邏輯 |
| `SWE1-HMI-VC-037-02` | 11.4 | Medium | P1 | P1 | **P1** | 啟用一者即停用其餘，同上 |
| `SWE1-HMI-VC-038-01` | 11.5 | Medium | P2 | P2 | **P2** | 語言變更之進度彈窗 |
| `SWE1-HMI-VC-038-02` | 11.5 | Medium | P3 | P3 | **P3** | 彈窗以新語言呈現 |
| `SWE1-HMI-VC-038-03` | 11.5 | Medium | P2 | P2 | **P2** | 彈窗持續至完成或使用者關閉 |
| `SWE1-HMI-VC-038-04` | 11.5 | Medium | P3 | P3 | **P3** | 關閉後返回語言設定頁 |
| `SWE1-HMI-VC-038-05` | 11.5 | Medium | P3 | P3 | **P3** | 更新期間其餘語言灰化 |
| `SWE1-HMI-VC-039` | 11.6 | Medium | P3 | P3 | **P3** | 中文之特定彈窗文字 |
| `SWE1-HMI-VC-040` | 11.7 | Medium | P2 | P2 | **P2** | 左側選單列標題取自 HMI Settings List |
| `SWE1-HMI-VC-041` | 11.7.1 | Medium | P2 | P2 | **P2** | 無選單列時之第一層呈現 |
| `SWE1-HMI-VC-042-01` | 11.8 | Medium | P3 | P3 | **P3** | 文字截斷時改以箭號下推 |
| `SWE1-HMI-VC-042-02` | 11.8 | Medium | P3 | P3 | **P3** | 下一層之單選列呈現 |
| `SWE1-HMI-VC-043` | 11.8.1 | Medium | P3 | P3 | **P3** | 父層括號顯示目前選項 |
| `SWE1-HMI-VC-044` | 12.1 | Medium | P2 | P2 | **P2** | 清單順序依 HMI Settings List |
| `SWE1-HMI-VC-045` | 12.2 | Medium | P2 | P2 | **P2** | SETTINGS 不逾時、選擇後不關閉 |
| `SWE1-HMI-VC-046-01` | 12.3 | Medium | P1 | P1 | **P1** | 按壓選取 —— 設定之主要互動 |
| `SWE1-HMI-VC-046-02` | 12.3 | Medium | P1 | P1 | **P1** | 箭號開啟次層清單，主要導覽 |
| `SWE1-HMI-VC-046-03` | 12.3 | Medium | P3 | P3 | **P3** | 首次進入之游標位置 |
| `SWE1-HMI-VC-046-04` | 12.3 | Medium | P1 | P1 | **P1** | 直接觸碰內嵌選項調整，主要互動 |
| `SWE1-HMI-VC-046-05` | 12.3 | Medium | P1 | P1 | **P1** | 旋鈕與方向鍵操作，主要互動之替代路徑 |
| `SWE1-HMI-VC-047-01` | 12.3.1 | Medium | P2 | P2 | **P2** | 旋鈕於核取列之切換 |
| `SWE1-HMI-VC-047-02` | 12.3.1 | Medium | P2 | P2 | **P2** | 旋鈕於多選列之循環 |
| `SWE1-HMI-VC-047-03` | 12.3.1 | Medium | P2 | P2 | **P2** | 旋鈕於 -/+ 列之下壓態 |
| `SWE1-HMI-VC-047-04` | 12.3.1 | Medium | P2 | P2 | **P2** | 下壓態之解除 |
| `SWE1-HMI-VC-048-01` | 12.3.2 | Medium | P3 | P3 | **P3** | 選取後游標移至該列 |
| `SWE1-HMI-VC-048-02` | 12.3.2 | Medium | P2 | P2 | **P2** | 設定變更確認音及其例外清單 |
| `SWE1-HMI-VC-049` | 12.3.3 | Medium | P2 | P2 | **P2** | 長按連續增減之速率（500ms／200ms） |
| `SWE1-HMI-VC-050` | 12.4 | Medium | P2 | P2 | **P2** | 亮度長按連續增減之速率（500ms／500ms） |
| `SWE1-HMI-VC-051-01` | 12.5 | Medium | P2 | P2 | **P2** | 選取後指示標移動 |
| `SWE1-HMI-VC-051-02` | 12.5 | Medium | P1 | P1 | **P1** | 設定被拒時指示標須退回 —— 否則 HMI 顯示車輛未接受之狀態 |
| `SWE1-HMI-VC-051-03` | 12.5 | Medium | P2 | P2 | **P2** | 離開頁面後才收到拒絕之補救彈窗 |
| `SWE1-HMI-VC-052-01` | 12.6 | Medium | P3 | P3 | **P3** | 進入時視圖置頂 |
| `SWE1-HMI-VC-052-02` | 12.6 | Medium | P3 | P3 | **P3** | Back 返回原位置而非置頂 |
| `SWE1-HMI-VC-053` | 12.7 | Medium | P3 | P3 | **P3** | 資訊圖示之呈現 |
| `SWE1-HMI-VC-054` | 12.7.1 | Medium | P2 | P2 | **P2** | 資訊彈窗之內容組成 |
| `SWE1-HMI-VC-055` | 12.7.2 | Medium | P2 | P2 | **P2** | 資訊圖示於行進中仍可用 |
| `SWE1-HMI-VC-056-01` | 12.8 | Medium | P2 | P2 | **P2** | 自資訊彈窗直接變更選項 |
| `SWE1-HMI-VC-056-02` | 12.8 | Medium | P3 | P3 | **P3** | 選畢關閉並返回清單 |
| `SWE1-HMI-VC-057` | 13.1 | High | P1 | P1 | **P1** | Key Off／Timed／ACC 下 Settings 不可用 —— 電源狀態之關鍵邏輯 |
| `SWE1-HMI-VC-058-01` | 13.1.1 | High | P1 | P1 | **P1** | 不可用時之提示彈窗 |
| `SWE1-HMI-VC-058-02` | 13.1.1 | High | P2 | P1 | **P2** ⬇ | 該彈窗不逾時 |
| `SWE1-HMI-VC-058-03` | 13.1.1 | High | P2 | P1 | **P2** ⬇ | 關閉後返回原畫面 |
| `SWE1-HMI-VC-059-01` | 13.2 | High | P1 | P1 | **P1** | Phone 設定之取用路徑 |
| `SWE1-HMI-VC-059-02` | 13.2 | High | P1 | P1 | **P1** | Phone 設定於 Key Off／ACC 仍可用 —— 例外規則 |
| `SWE1-HMI-VC-060-01` | 13.3 | High | P1 | P1 | **P1** | Audio 設定之取用路徑 |
| `SWE1-HMI-VC-060-02` | 13.3 | High | P1 | P1 | **P1** | Audio 設定於 Key Off／ACC 仍可用 —— 例外規則 |
| `SWE1-HMI-VC-061` | 13.4 | High | P1 | P1 | **P1** | 軟體更新於 Key Off／ACC 仍可用 —— 例外規則 |
| `SWE1-HMI-VC-062-01` | 13.4.1 | High | P0 | P0 | **P0** | **行車中禁入**：Wi-Fi 軟體下載之行進中攔阻，駕駛分心 |
| `SWE1-HMI-VC-062-02` | 13.4.1 | High | P2 | P1 | **P2** ⬇ | 攔阻彈窗關閉後之返回目標 |
| `SWE1-HMI-VC-063-01` | 13.4.2 | High | P0 | P0 | **P0** | **行車中禁入**：FOTA 流程中車輛起步之攔阻，駕駛分心 |
| `SWE1-HMI-VC-063-02` | 13.4.2 | High | P2 | P1 | **P2** ⬇ | 攔阻彈窗關閉後之返回目標 |
| `SWE1-HMI-VC-064-01` | 13.5 | High | P1 | P1 | **P1** | 行進間轉入 Key Off 時之強制彈窗 |
| `SWE1-HMI-VC-064-02` | 13.5 | High | P1 | P1 | **P1** | 該彈窗不逾時且不可關閉 —— 可關閉即進入無效狀態 |
| `SWE1-HMI-VC-064-03` | 13.5 | High | P1 | P1 | **P1** | 回到 Run／Key On 時自動關閉並還原 |
| `SWE1-HMI-VC-065-01` | 14.1 | Medium | P0 | P0 | **P0** | **安全**：行進中煞車服務模式須灰化 |
| `SWE1-HMI-VC-065-02` | 14.1 | Medium | P1 | P1 | **P1** | 按下灰化項之提示彈窗 |
| `SWE1-HMI-VC-066` | 16.2 | Low | P3 | P3 | **P3** | widget 標題字面 |

---

## 3. T26 —— A-VC10

條文逐字抄入 `ANOMALIES.md`。條文所舉二例**已獨立重測，逐字相符**：

| req_id | 欄 | 原值 |
|---|---|---|
| `VC-035-03` | Title | `... returns the user to the previous screen **without changing any settings**` |
| | Description | `Selecting cancel will take the user back to the previous screen.` |
| `VC-036-02` | Title | `... returns the user to the previous screen **without clearing any data**` |
| | Description | `Selecting cancel will take the user back to the previous screen.` |

### 一項比條文更強的證據（執行層另查）

條文以二例說明「Title 資訊量大於 Description」。執行層對全 117 leaf
盤點該欄之相異值：

```
Description 相異值: 116 / 117
重複之 Description: 1 組，涉 2 筆
  x2  ['SWE1-HMI-VC-035-03', 'SWE1-HMI-VC-036-02']
        'Selecting cancel will take the user back to the previous screen.'
```

**全表唯一的一組重複，恰好就是 A-VC10 所舉的那兩筆。**
即：`Description` 欄單獨**無法區辨**這兩個需求（同一句），
而 `Title` 可以，且其差額正是二筆定案 P0 的依據。
這比「Title 較長」更能說明二欄之分工 —— 已寫入 DR-VC7 之附帶一問。

> 另測：117 筆中 Title 長於 Description 者 **74 筆**。但長度非資訊量，
> 該數字僅供參考，未作為判準。

---

## 4. T27 —— 同批 A 與 DR 清單

**同批 A 現為四項**（皆為對 037 作者之說明性查詢，一次往返）：

1. DR-VC2 —— `SYS-HMI-RA-VC-###` 之來源系統
2. DR-VC7 —— 欄 18 `Priority` 之賦值判準
3. A-VC2 —— 037 封面 `Reviewer` 空白、`Date` 為 2020/09/05
4. **A-VC10 —— `Title` 與 `Description` 之分工**（本輪新增）

**DR 未結維持七筆**（DR-VC1 ~ DR-VC7）—— A-VC10 併入既有 DR，未新立 DR。

---

## 5. T29 —— REVISIONS

`docs/REVISIONS.md` 現有**十筆**：

| REV | 標的 | 依據 |
|---|---|---|
| REV-01 | 01 §3.3 九欄之 `\xa0` 斷言作廢 | R-VC6 |
| REV-02 | 01 §3.1 規格 PDF 位元組數 | R-VC7 |
| REV-03 | 01 §五 T9「reference 七項」→ 六項 | R-VC10 |
| REV-04 | 01 §五 T1「forms/ 不複製」作廢 | R-VC10 |
| REV-05 | 01 §八 `recon_assertions` 四鍵 → 二鍵 | R-VC9 |
| REV-06 | 01 §4.2 計數 24＋18 → 25＋17 | R-VC12 一 |
| REV-07 | 01 §4.2(b) 摘要文字三節作廢 | R-VC12 二 |
| REV-08 | 01 §五 T5「16 列」之口徑（實為 22 列）| 執行層實測 |
| **REV-09** | **R-VC11(b) 作廢：粒度錯配** | **R-VC13** |
| **REV-10** | **priority 定案：八筆撤銷、一筆改判** | **R-VC13 + R-VC14** |

`data/priority_draft.tsv` **保留為軌跡，未刪**；定案在
`data/priority_final.tsv`。二檔並存。

---

## 6. T30 —— `DECISIONS` 差異逐項表

`DECISIONS.md`（80 行）為 scaffold 樣板，全部欄位仍是佔位符
（`[AUTO]`／`[PROPOSED: value — rationale]`／`[PEI]` 之說明文字）。
`DECISIONS.new.md`（53 行）為 recon 於 T14 產出之實測填充版。

**二者不是同一份文件之兩個版本，是「說明書」與「填好的表」。**
故本節不逐行 diff（那只會列出 80 + 53 行全異），改列**新版之實質內容**
與其是否可簽。

### 6.1 可逕簽者（`[AUTO]`，機器實測，本包已交叉驗證）

| 項 | 新版之值 | 交叉驗證 |
|---|---|---|
| spec_mode | `A` | T9 依 FO §3 實測；intake 獨立提案亦為 A |
| spec text layer | 18,750 chars (pymupdf) | T17 逐頁量測相符（28 頁）|
| source files | 6 present | T16 之 `reference:` 六項 |
| ruled-constant assertions | 3 checked / 3 PASS / 0 FAIL | 上繳包 02 §5 |
| spec outline map | 66 cited / 108 entries | T4／T12 第 25／29 項 |
| workbook_state | `BLANK` | R-VC2 所裁 |
| form layout revision | C (has Estimated Test Time) | T3 實測 |
| column mapping | 15 fields from header text | T3，conflicts (none) |
| done segments / ambiguous rows | none | 一致 |
| design-method vocabulary | 9 exact strings | T3 |
| 037 leaves | 145 | **注意：此為 `Categorization` 判準之 145，非 R-VC3 之 117**（R-VC9 之揭露義務）|
| regen targets | 145 | 同上 |
| covered nowhere | 145 = all leaves | BLANK 下之預期，非缺口 |

### 6.2 **須先修再簽者 —— 一項**

```
## 4. Style bindings
- spec_reference: [PROPOSED: None]
```

該 `None` 是 `feature.yaml` 之 `spec_reference_template: null` 被
f-string 直接印出的 Python `None`，**不是一個裁定值**。
R-VC4 所裁為「`spec_reference` 逐字取 037 `HMI Source ID` 欄原值」，
R-VC8 之修法已使 `data/recon_leaf_to_section.tsv` 依此產出
（145/145 逐字相符）。

**簽在這一行上等於簽了一個字面 `None`。** 建議簽署前改為：

```
- spec_reference: [PROPOSED: 逐字取 037 HMI Source ID 欄原值（R-VC4）；
  template 為 null 係「查得而非構造」之宣告，非空值]
```

此為 `recon.py` 之顯示層問題（與 R-VC8 所修之資料層不同處），
**未自行改動**：`DECISIONS.new.md` 是 recon 之產出，手改它會在下次
重跑時被覆寫且無痕。若要根治屬 Tier 2 工具修法，本包未授權。
**已登記為待裁，未新立 A**（等你決定是修腳本、或簽署時手動覆蓋）。

### 6.3 待 Pei 裁之 `[PROPOSED]`（6 項）與 `[PEI]`（2 項）

| 項 | 新版之值 | 備註 |
|---|---|---|
| safety attributes | ruled source 無 ASIL/FTTI 欄 → SYS2/SYSRA 不入 trace chain | T4 已測：037 無 safety 欄 |
| parent/child dupes | 28 筆，逐案比例檢定 | 即 R-VC3 之「有子之父」28，數字一致 |
| style authority | fallback chain — no done region | BLANK 之必然 |
| test item shape | standard §4.3 tc_title | |
| test group/set columns | FILL per framework Part N | R-VC2(a) 已裁 `fill_test_group_set: true` |
| exemplar source | nearest sibling done region, cross-feature: style only | |
| author on new rows | `PeiPYHsu` | R-VC2(b) 已裁，一致 |
| split_mode | standard | |
| batch plan | 依 spec chapter 分組，pilot = 最小連貫批 | |
| **Test Set table (Part N)** | `[PEI — draft with Claude, Tier 2]` | **Phase 3，尚未開始** |
| **profile [OVERRIDE] clauses** | `[PEI — draft with Claude, Tier 2]` | 同上 |

### 6.4 一項本包定案而 `DECISIONS.new.md` 未載

`priority` 之判定（R-VC11(a)／R-VC13／R-VC14，定案表 117 筆）
**不在 recon 之產出範圍**，故 `DECISIONS.new.md` 無此項。
簽署時建議增列一行指向 `data/priority_final.tsv`，否則該定案不在
決策表之視野內。

**執行層不自行合併**（Tier 2 不變）。上列即送簽之全部內容。

---

## 7. 未結清單

### DR —— 七筆全未結

DR-VC1 / DR-VC2 / DR-VC3 / DR-VC4 / DR-VC5 / DR-VC6 / DR-VC7。
同批 A ＝ DR-VC2 ＋ DR-VC7 ＋ A-VC2 ＋ A-VC10。

### A —— 六筆未結

| A | 狀態 | 待 |
|---|---|---|
| A-VC2 | PENDING | 同批 A |
| A-VC3 | PENDING | 併入 DR-VC3 |
| A-VC4 | PENDING | 全域排程 |
| A-VC8 | PENDING | 全域排程 |
| A-VC9 | PENDING | DR-VC7 |
| **A-VC10** | **PENDING** | **同批 A** |

已結四筆：A-VC1（撤銷）、A-VC5 / A-VC6 / A-VC7（RESOLVED）。

### 待裁

1. **`DECISIONS.new.md` §4 之 `spec_reference: [PROPOSED: None]`**
   —— 修腳本、或簽署時手動覆蓋（見 §6.2）。
2. **`DECISIONS.md` 之簽署**（Tier 2，Pei）。上列 §6 即送簽內容。
3. Phase 3（framework Part N、Layer 2 切分）—— Tier 2，待你指示。
4. 表 B 之最終措辭（待 DR-VC3，非本輪可結）。

---

## 8. 量測條件揭露（R-G8）

### T28 之異動套用方法與可重現性

- **未重做判定**：本地預判以 `importlib.util` 自 `t24_priority_draft.py`
  匯入 `LOCAL` 與 `RANK`，**不複製第二份**。
  故 T24 之 117 筆人工判定與本輪定案之關係為
  「同一組輸入 + 兩條機械規則」，可逐筆回推。
  副作用揭露：匯入時會執行 t24 腳本、重出 `data/priority_draft.tsv`
  —— 其內容與前次相同（同一輸入同一字典），非新判定。
- **R-VC13 為機械規則**：章級分群鍵取自 `HMI Source ID` 尾段之首段
  （`sec.split(".")[0]`），與 T20（A-VC9 重測）同法；
  約束以集合量詞實作（High 用 `any(...)`、Low 用 `all(...)`）。
  **不滿足即 `sys.exit(1)`**，不自行修補。本輪未觸發。
- **R-VC14 為列舉表**：`RVC14` 字典僅一筆（`VC-036-01`），
  逐字對應下放包 04 §二之即時適用。
  **未自行推廣**至其他 leaf —— 條文只點名這一筆，本輪就只改這一筆。
  若「攔阻失效／執行失效」之區分應普遍套用於全表，
  那是對 R-VC14 適用範圍之擴張，須另裁。
- **偽陽性風險（承 T24 未消）**：本地判定之依據仍為
  `Requirement Title` 一句，**未讀 `Requirement Description` 全文**。
  下放包 04 §四之關鍵詞掃描對本地判 P2／P3 之 72 筆做了獨立覆核並
  追認未發現低估，但該掃描自陳為**關鍵詞比對而非語意判讀**，
  其效力為「以該詞表為準未發現低估」，非「已證明無低估」。
  **此風險本輪未消除，僅被二次覆核降低。**
- **一項本輪新得之反證**：A-VC10 顯示 `Description` 欄之資訊量在
  至少二筆上**低於** `Title`（且該二筆之 Description 逐字相同）。
  即「未讀 Description」之風險，在這兩筆上不成立 ——
  讀了反而更少。此不推廣至其餘 115 筆。

### T26 之全表盤點

- `Description` 相異值以精確字串集合計（strip 後，不正規化空白與大小寫）。
  **偽陽性風險**：若二筆之 Description 僅差一個空白或大小寫，
  本法會判為相異而漏報。本次唯一之重複組為完全相同之字串，
  故該風險未實現於已報結果；但「還有沒有近似重複」本法看不見。

---

**T25–T30 全數完成，無停點。未自行合併 `DECISIONS.md`，未進入 Phase 3。**
