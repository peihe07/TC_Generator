# 71 包 —— 執行層回報

§H 四步完成。**全案六閘首次全數歸零**（G251 之 3 為 (c) 類應保留）。

## 1. G255 —— 本包數字與重算（R-P379(c)）

| 條文所引 | 機讀來源 | 重算 |
|---|---|---|
| 59 / 303 | `composite_tokens_70.md` 標題 | **59 token / 303 次** ✓ |
| 170 | 同檔母體行 | **170 條** ✓ |
| 41 / 12 / 6 / 0 | 71 包 §1 表 | 合計 **59**，與供料 token 數一致 ✓ |
| **字典覆蓋率** | 供料 59 token 逐一比對 §1 表 | **59 / 59，未覆蓋 0** ✓ |

## 2. 抄錄

`RULINGS.md`：**R-P396** 逐字抄入（1 / 1）。
R-P36 加註：**R-P355(c) / R-P380** —— `TLM_Status.Info` 之 PENDING 佔位範圍受限縮
（R-P396(b) 之同物判定），G247 判準相應排除該名；**明記為分析層判斷，Pei 得否決**。

`data/proxy_dictionary_71.md` 已落，**逐字採 71 包 §1 表**。

## 3. §H 第 2 步 —— 二項查詢回報

### `AUD_LVL`（R-P368 三段鏈）

| 段 | 結果 |
|---|---|
| 1（LID `Logical Identifier`）| **0 命中** |
| 3（forms DBC 逐字 `SG_`）| **FDCAN8 查得**：`SG_ AUD_LVL : 103\|8@0+ (1,0) [0\|38] "levels" SGW`，訊息 **`TELEMATIC_FD_13`**，`CM_` = `"Audio level"` |

依 **R-P389(a)** 之判準（`SG_` 逐字即段 3 查得，不以 LID 段 2 為必經）→ **解得**
`$TELEMATIC_FD_13.AUD_LVL$`，字典採之。

⚠ **B-CAN 側有近似名 `AUD_LVLSts`**（BHCAN2 msg 1478，`CM_` 亦為 `"Audio level"`）——
與 `AUD_LVL` **差 `Sts` 後綴**。本層**取 FDCAN8 之逐字同名者**，
近似名記此供對照，**不採**（R-P368(b)）。

### `Response_Wait_Time`

| 來源 | 結果 |
|---|---|
| PROXI `Format` | **0 命中** |
| CFTS009 | 出現 **9 次**，**無一處給值** |
| SYS3 | 出現 **5 次**，**無一處給值** |

以「數字＋時間單位」之上下文掃三份文字層：**0 命中**。
依 R-P396(d) **併入 DR-PW30**。

### DR 併問

- **DR-PW30** 併入 `Response_Wait_Time`（影響 `-105` / `-106`）
- **DR-PW29** 併問二項：**`FPDM` 之展開**（分析層判斷，非規格明文，R-P396(c)）；
  **ANC / ACN 之刺激與觀察面**（`4941453` 載其應 active 而無對應訊號）

## 4. §H 第 3 步 —— 字典機器套用

`apply_dictionary_71.py`：母體 **170 條**（三閘未歸零者），**套用 170 / 170**，
**字典未覆蓋 token 0**。

⚠ **一處設計決定須記**：首版把字典套到全案 287 條，
會把 55–70 包**已改寫且六閘已過**之句（`$STATUS_TELEMATIC.PowerSts_Telematic$`、
`"Brand Logo Screen"`、`HU speakers` 等）當成 token 再展開一次 —— **等於破壞既有正確內容**。
改為：(1) 只處理三閘未歸零之 170 條；(2) 句內**已為白名單之原子原文保留**，不經字典。
修正後未覆蓋 token 由 33 降為 **0**。

### 全案六閘 —— **首次全數歸零**

| 閘 | 期望 | 實測 | 判 |
|---|---|---|---|
| G245 家族 A（上界，R-P362）| 0 | **0** | ✓ |
| G250 `proper` / `as defined` / `normal` | 0 | **0** | ✓ |
| G250 `Read the HU mode/state` | 0 | **0** | ✓ |
| G247 Proc/ER 內部訊號（排除 `TLM_Status.Info`，R-P396(b)）| 0 | **0** | ✓ |
| G251 `listed in Input Test Data` | 0 | **3** —— `-005`/`-218`/`-262`，皆 (c) 類應保留 | ✓ |
| G249 五欄逐字相同對 | — | **10**，全 (b) 型（req_id 皆不同），互註齊 | ✓ |

配套：`ENTER_<STATE>` 使用 **134** 條、`FUNC_STATE_<STATE>` 使用 **68** 條。

### 套用後之四處補正，據實記（皆本層之字典措辭所生）

1. **`played animation` / `season the HU determines`**（6 條）：字典原文
   「new season animation or **normal** brand animation」**含 R-P353 末段所禁之 `normal`**，
   且元件未加引號 → 改 `"New Season Animation"` / `"Brand Animation"`，二閘同時解。
2. **`display backlight`**（2 條）：`HU screen` 未具名 → 改 `"Display Backlight"`。
3. **`LTM_OperationalModeSts.Info` 於 Send 句**（4 條）：字典只換 Read/Check 句，
   而該 token 之既裁（R-P368）**不限於 Read 句** → Send 句同換
   `$STATUS_BH_BCM1.OperationalModeSts$`。
4. **`STATUS_BH_BCM1.DriverDoorSts` 未加 `$`**（1 條）→ 補。

⚠ 第 1 項為**本包第三次**同型錯（67 包批一、68 包批二、本包字典）——
**具名元件加引號屬 IN §11 之書寫規則，我在產生器裡一再漏掉**。

### G249 由 12 降為 10 —— 非回歸

字典套用後 `-153`/`-196`、`-154`/`-197` 二對之 Procedure／ER 依各自 token 展開而**相異**，
**不再成對**。其 R-P357(b) 互註已改為**歷史記載**（不刪）——
「二列皆保留」之事實不因此改變。現行 10 對全為 (b) 型且互註齊備。

## 5. PENDING（`pending_recount_71.tsv`）

| 項 | 值 |
|---|---|
| corpus | 287 |
| **`PENDING` 條數** | **146**（70 包 125 → 本包 146）|

⚠ 增加 21 條，成因為字典之 12 個佔位 token（`VPLastStatus`、`antitheft request`、
`applied theme`、`its timing`、`shown seat graphic`、`HU timer`、`ACN` 等）
在此輪被明確展開。**與 A-PW369 同理：該等目標改寫前同樣不可觀察**，
只是先前以複合名詞掩蓋。**S6 之出貨阻斷未變。**

## 6. 現況

| 項 | 值 |
|---|---|
| corpus | **287**（283 ＋ §8.3 拆分 4）|
| 已改寫 | **287 / 287** |
| **六閘** | **全數歸零**（G251 之 3 為應保留、G249 之 10 為 (b) 型）|
| `PENDING` | 146 |
| 開中 DR | PW23／25／26／27／28／29／30 |
| G0 | 素材 9/9 ＋ 參考庫 7/7 |

## 7. 待裁

1. **六閘既已全綠，下一步為寫回（72 包）** —— 惟 S6 之 146 條 PENDING 仍在，
   甲案下不出貨。**乙／丙仍只有 Pei 能開。**
2. **`AUD_LVLSts` vs `AUD_LVL`**（§3）：本層取 FDCAN8 逐字同名者，
   B-CAN 側近似名未採，請確認。
3. **站④ 抽查**：75 條之目視包在 Pei 手上；**全 287 條之目視包本層可同法產出**，
   六閘已全綠，此時產出之版本即為站④ 之完整標的。
