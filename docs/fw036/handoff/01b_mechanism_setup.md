# 下放包 01b：機制文件建置（S1／S5／S3，Pei 已裁定）

承 01a。純文件建置，零內容修改。新規 0 條。

## S1：舊規標 superseded

於下列兩檔**檔首**插入區塊（僅加標頭，內文不動、不刪檔）：
- `/Users/peihe/Work/09_作業流程與單位規範/02_TC Design Flow & Standard/ASPICE_SWE6_Test_Case_Writing_Rules_v2.md`
- 同目錄 `ASPICE_SWE6_Test_Case_Writing_Rules.md`
- 同目錄 `ASPICE_SWE6_AI_Instruction.md`、`ASPICE_SWE6_AI_Instruction_20260507.md`、`ASPICE_SWE6_AI_Instruction_mygpt.md`

```
> **SUPERSEDED（2026-08-21）**
> 現行權威版本為 TC_Generator repo 之
> `docs/runtime/ASPICE_SWE6_AI_Instruction.md`。
> 本檔保留作歷史參考，不得作為撰寫或覆核依據。
> 已知與現行版之實質衝突：方括號 UI 標籤範例（現行為 `"..."`）、
> 範例帶尾句號（現行禁止）。
```

**注意**：此路徑位於 `/Users/peihe/Work/`，非 repo。屬文件標記，
非交付物；仍屬可逆編輯。若任一檔不存在則跳過並於上繳列明。

## S5：裁決台帳

建 `docs/fw036/RULINGS_LEDGER.md`，格式：

```
# 裁決台帳（FW036 全案）
欄位：編號｜日期｜標題｜狀態｜出處包｜適用範圍
狀態：ACTIVE / [DEFAULT] / SUPERSEDED / WITHDRAWN
規則：條文全文僅於本台帳落檔一次，各包引用編號不重抄。
撤銷之裁決以刪除線保留並附區塊引註，不得刪除（R-TM13）。

| 編號 | 日期 | 標題 | 狀態 | 出處 | 範圍 |
|---|---|---|---|---|---|
| R-1 | 2026-08-21 | 訊號記法三層 | ACTIVE | 01a | 全案 |
| R-2 | 2026-08-21 | spec_reference 家族分流 | ACTIVE | 01a | 全案 |
| R-3 | 2026-08-21 | test_item 上半 50 token | ACTIVE | 01a | 全案 |
| R-4 | 2026-08-21 | verbatim 首字轉大寫 | ACTIVE | 01a | 全案 |
| R-5 | 2026-08-21 | 雙語制合法化不回修 | [DEFAULT] | 01a | BT/Projection |
| S1 | 2026-08-21 | 舊規 superseded | ACTIVE | 01b | 09_ 目錄 |
| S2 | 2026-08-21 | §11 收斂 | ACTIVE | 01a | 全案 |
| S3 | 2026-08-21 | lint 出貨 gate | ACTIVE | 01b | pipeline |
| S4 | 2026-08-21 | test_item 括號下半 | ACTIVE | 01a | 全案 |
| S5 | 2026-08-21 | 裁決台帳制 | ACTIVE | 01b | 流程 |
| S6 | 2026-08-21 | 缺件 PENDING 佔位 | ACTIVE | 01a | 全案 |
| N-1 | 2026-08-21 | N 規制單位為 item，子步驟與續行同受規制 | ACTIVE | 00c/00d | lint |
```

同時於 `docs/fw036/FEATURE_ONBOARDING.md` §7 handoff contract 末插入：

```
每包需 Pei 裁定之新規上限 3 條，超過即拆包。
包尾自檢表增列「本包引用之既有裁決編號清單」；引用未落檔編號
= 包退回。Tier 1 事項（純格式、可逆、單 feature）分析層以保守
預設先行，標 [DEFAULT] 記入 RULINGS_LEDGER 供 Pei 事後追認或
推翻；僅 Tier 2+ 阻塞等裁。
```

## S3：gate 尚不啟用

`--gate` 旗標保留關閉。啟用時機為尾批（全數回修完成後），
現階段若啟用將使所有既有交付本 exit 1，阻斷正常作業。
本包僅於 `scripts/lint036.py` docstring 註明此政策。

## 執行

```bash
cd /Users/peihe/Work_Projects/TC_Generator
pytest -q            # 確認無回歸
git diff --stat      # 不得 commit（屬 Pei）
```

上繳 `docs/fw036/upstream/01b_mechanism_setup.md`：各檔變更清單、
跳過之檔案、「該驗未驗」獨立判斷、引用裁決編號清單。
