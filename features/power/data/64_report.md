# 64 包 —— 執行層回報

§H 第 1–4 步完成，依第 4 步「停，待覆核」停在代理量表之後。

## 1. G255 —— 本包條文數字與重算（R-P379(c)）

抄錄前逐一重跑，**5 / 5 相符**：

| 條文所引 | 機讀來源 | 重算 |
|---|---|---|
| 3 條（靜態組態可撤）| `(names − 解得2) ⊆ 強中候選` 且該候選僅見於 Pre-Condition／ITD | **3**（`-062` / `-076` / `-077`）|
| 6 條（運行時維持 PENDING）| 同上，候選見於 Procedure／ER 或帶轉移措辭 | **6**（`-017`/`-018`/`-019`/`-070`/`-081`/`-107`）|
| 2 條（`SwitchOffSetting.Req`）| corpus 含該名者 | **2**（`-049`/`-280`），皆運行時 |
| 99（PENDING 甲）| `102 − 3` | **99** |
| 39 / 6 | `proxy_reachability_63.md` 之 `**有錨**` / `**查無**` 列數 | **39 / 6** |

⚠ **一處來源形態瑕疵（非數字錯）**：R-P380(c) 稱「以 `pending_recount_63.tsv` 甲情形為準」，
該檔**無甲情形之列**（列為 93 與 79）；99 係由 `102 − 3` 導出。
本包出 `pending_recount_64.tsv` 補該列。

## 2. 抄錄與登記

- `RULINGS.md`：**R-P380–R-P382** 逐字抄入（3 / 3）。§J 重驗：3/3/三條，一致。
- R-P36 加註二處：**R-P377(a)**（撤除限靜態組態；PENDING 99 非 93）、
  **R-P372(a)**（「人讀」改由分析層，執行層只供料）。
- `ANOMALIES.md`：**A-PW363**（R-P364(d) 首次失效）、**A-PW364**（見 §5）。

### A-PW363 —— R-P364(d) 失效之機制

R-P364(d) 立於 57 包，令「列出每一新條所**引用或觸及**之既有 canon 條」。
63 包 §J 列了 R-P377 所**引用**之 R-P368(b)，漏了其所**觸及**之 R-P375(c)。

**「引用」看得見，「觸及」看不見** —— 前者可由條文文字掃出，
後者須推想該條之結論會動到誰。(d) 未區分二者之查法，故形同只查了引用條。

## 3. R-P380 —— PENDING 回退（`pending_recount_64.tsv`）

| 情形 | 條數 | 佔 283 |
|---|---|---|
| 62 包（解得 2 名扣除）| 102 | 36.0% |
| R-P377(a) 原機讀（強中候選全撤）| 93 | 32.9% |
| **R-P380(a) 甲：僅靜態組態用法撤除** | **99** | **35.0%** |

撤除者 3 條（`-062` / `-076` / `-077`）；
維持 PENDING 之運行時 6 條（`-017`/`-018`/`-019`/`-070`/`-081`/`-107`）。
`SwitchOffSetting.Req` 之 2 條皆運行時，**一條不撤**，與 R-P380(b) 一致。

## 4. R-P381 —— 六名供料頁

落檔 `data/g252_six_63.md`（17.5 KB，7 條 TC）。
**執行層不判定、不查詢、不機掃**，只搬運四件事。

⚠ **一處須說明之取徑**：R-P381(a) 令供「其錨點 ObjectID 之段落全文」，
惟現行 corpus 之 `specification_reference` 為 `{檔名}_{章節}` 式而**無 ObjectID**（A-PW344），
`reasoning_note` 亦非每條皆載。故錨點改自
**`data/layer3_full.tsv`**（G94 / G99 之來源，`leaf` → `item_ids`）取，
段落全文自文字層**逐字**取、未截斷。**7 條 TC 之錨點全部取到，無缺口。**

## 5. ⚠ A-PW364 —— `$PowerMode$` 之 LID 解與 R-P354(a) 相反

**本條為執行層於 §H 第 4 步抽取代理量時之附帶發現，非本包指示之標的。**

代理量之 (i) 類須將段落中之 `$X$` 走 R-P368 段 1→2 解為 `MESSAGE.Signal`。
執行 LID 對照時發現：

| | |
|---|---|
| LID `Logical Identifier` | **`PowerMode`**（逐字命中），`Function` = `Commanded ignition switch status` |
| `Atlantis High` 欄 | **`STATUS_BH_BCM2.CmdIgnSts`**（`CAN-B`）／`BCM_FD_10.CmdIgnSts`（`FD`）|
| `VAL_ 1132 CmdIgnSts` | `0 Initialization / 1 IGN_LK / 3 ACC / 4 RUN / 5 START / 7 SNA` |

CFTS009-4941027 / 4941028 之 `$PowerMode$` 值域為
`IGN_ACC` / `IGN_OFF_ACC` / `IGN_RUN` / `IGN_LK` / `IGN_OFF` / `IGN_START` / `SNA`。

**`IGN_LK`、`SNA` 逐字相符；`ACC` / `RUN` / `START` 為 `IGN_` 前綴差。**

對照之下，R-P354(a) 所用之 `STATUS_BH_BCM1.OperationalModeSts`
其 `VAL_ 854` 為 `Ignition_Off` / `Ignition_Acc` / `Ignition_On`…
—— **與 `$PowerMode$` 之 token 集不符**。

**該名承自 pm_29（27 包）而從未經 LID 解**（DR-PW26 第 (1) 問即問其等同性）。
本條為該問之**證據，且方向與原假設相反**。

**本層不代認定**（§8.4.1）；DR-PW26 第 (1) 問已補此證據。
**若上游確認，`ENTER_<STATE>` 六個可用片段之 Body ON/OFF 驅動步須改訊號。**

形態為 A-PW355 / A-PW361 同族之第三面：
前二者為「查詢範圍窄」「跳過段次」，本條為「**從未查過就沿用**」。

## 6. R-P382 —— 代理量表：機器只到候選，擇一仍須人判

落檔 `data/observable_proxy_64.md`。母體 39 名。

| 判定 | 數 |
|---|---|
| 有白名單類候選 | **17** |
| 填不出 | **22** |

### 據實回報：本表是**候選抽取**，不是填好的代理量表

R-P353 令「由執行層為每一功能指定**一個**」代理量。本層做到的是：

- **(i) 類可機器解到底** —— 段落中之 `$X$` 走 LID 段 1→2 再經 forms DBC `SG_` 確認，
  結果可逐筆追溯（如 `$Radio_Theme$` → `$RADIO_B4.Radio_Theme$`、
  `$Telematic_Power$` → `$STATUS_TELEMATIC.PowerSts_Telematic$`、
  `$PwrAccDelayAct$` → `$BODY_CNTRL3.Comfort_Enable_Time$`）。
- **(ii) 類只能篩掉明顯不是的** —— 初版把 `"present"` / `"00 min"` / `"True"` 這類
  **欄位之值**當成 UI 名，錯；收緊為「須含 screen／icon／pop-up／menu／logo／button
  等 UI 名詞且非值」後，39 名中只剩 1 名抽得到（`"Splash Screen logo visualization"`）。
- **(iii)(iv) 類機器只能標面向** —— 「段落載有音訊詞」不等於「指定了哪一個音訊量」。

**擇一為代理量與 R-P381 之人讀同性質。** 本層列全部候選並標類別，**未擇一**。

### 22 個「填不出」

其錨點段落內無 `$…$`（經 DBC `SG_` 確認）、無具名 UI 元件、無音訊／log 具名詞。
依 R-P382「填不出白名單類者不得硬填，回報」，**本層不硬填**。
其中多數為複合觀察目標（`season the HU determines`、`three stored variables`、
`offered items against the TLM HMI documents`），須先拆為單一觀察量才談得上代理。

## 7. 待裁

1. **代理量之擇一**（§6）：17 名之候選是否由分析層擇定，或連同 R-P381 之六名一併人讀。
2. **22 名填不出**（§6）：是否先回 R-P353 拆為單一觀察量再談代理。
3. **A-PW364**（§5）：`$PowerMode$` → `CmdIgnSts` 之證據是否足以改 R-P354(a)，
   或維持現狀等上游回 DR-PW26(1)。**六個可用片段之驅動步繫於此。**

**B5 依 R-P374(a) 續凍。**
