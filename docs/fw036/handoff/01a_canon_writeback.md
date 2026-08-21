# 下放包 01a：canon 條文回寫（Pei 已裁定，2026-08-21）

Pei 指示「都裁定」= 全數採納提案。兩項提案內含選項者取保守值
並標 `[DEFAULT]`（Pei 得逕行推翻，無須走裁決流程）。
本包為純文件編輯，零內容修改、零不可逆操作。新規 0 條。

目標檔：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
編輯後須重算 sha256 並更新引用該 hash 之處（Project 指示內註記）。

## 插入位置與逐字區塊

### 1. §4.3 末（Forbidden 段之後）插入

```
### 4.3.1 test_item 兩段式（R-S4）
test_item 分上下兩半：
- 上半 = 需求／規格原句 verbatim。摘句以「與括號下半之測試目的
  直接相關之句」為限；上半 token 數上限 50（R-3）。超限須摘句，
  全文以 specification_reference 指回，不得整段傾倒。
- 下半 = 作者生成之測試目的或情境標籤，獨立成行，格式 `(...)`。
同一 Requirement ID 衍生之多列，其括號下半內容不得逐字相同
（sibling 區分 token）。缺括號下半 = FAIL，不得出貨。
verbatim 自原句中段起抄時，句首字母轉大寫屬排版正規化，允許（R-4）。
```

### 2. §8.4 末插入

```
### 8.4.3 缺件佔位（S6）
欄位因來源文件缺失而無法填寫時，寫 `PENDING: DR-{n} <缺件名>`，
不得留空、不得填 NA。NA 僅限「確認不適用」。DR 登記於該 feature
之 DATA_REQUESTS.md；每包上繳附未結 DR 清單。含 PENDING 之工作簿
不得出貨，交付前須全數結案或由 Pei 裁定降轉 NA。
```

### 3. §8.7 末插入

```
#### 8.7.5 訊號記法（R-1）
三層記法各有其形，同一行可並列多層，但每一 token 須自我識別所屬層：
- PROXI 參數 → `$X$`（沿來源原文）
- 內部訊號 → `X.Info` / `X.Req`（沿來源原文）
- CAN 訊號斷言 → 三件組 `<Signal> in <MESSAGE> on <segment>`
  例：`RemStActvSts in STATUS_BH_BCM2 on BH-CAN`
網段須有來源（DBC 或架構文件）依據；查無者依 §8.4.3 標 PENDING，
不得杜撰。
```

### 4. §10.7 全節替換（家族分流，R-2）

```
### 10.7 specification_reference
依母 spec 型態分流：
(a) CFTS 母文件 → `CFTS{nnn}-{ObjectID}`，ObjectID 為該物件之
    Polarion 7 位號碼。短號需求 ID（如 CFTS015-824）不得作為錨，
    僅得於 reasoning 引用。
(b) HMI Logic and Flow 類 → `{檔名}_{章節號}`，檔名以底線 token 化
    （空格→底線），全案逐字一致，禁止同檔名拼寫變體。
排列：一來源文件一行（換行分隔）；同一文件內多個 ObjectID／章節號
以 `, ` 續列且文件前綴僅敘明一次；禁用 `;`。TC 直接驗證之主要來源
列於首行，同文件內 ID／章節號升冪。
```

### 5. §11 收斂（S2）—— 於「UI element labels」段前插入

```
本節之引號規則與尾句號規則自 canon 生效日起適用；
09_ 目錄舊版 Writing Rules 之方括號範例與帶尾句號範例已 superseded。
尾句號之規制單位為 numbered item，非物理行：item 之尾句號落於續行
時，該 item 仍屬違規。子步驟 `a./b./c.` 為實質測試內容，同受規制。
```

### 6. §1 末插入

```
[OVERRIDE-R5][DEFAULT] 雙語並列（中文 AC + 英譯、英文 + 簡中對照）
於 BT、Projection 兩 feature 為既存制度性格式，予以合法化，
不回修；lint K 對此二本配置豁免。UI 標籤之簡中 verbatim 全案豁免。
工作備註中文一律不得留於交付欄，應移至 Remarks。
新 feature 一律 English only，不得援引本例。
```

## 執行

編輯後 `git diff --stat` 應僅 1 檔變動；不得 commit（屬 Pei）。
上繳 `docs/fw036/upstream/01a_canon_writeback.md`：diff 摘要、
新 sha256、各區塊插入行號、「該驗未驗」獨立判斷。
