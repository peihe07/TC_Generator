# 65 包 —— 執行層回報

§H 第 1–4 步完成，依第 3 步「停」停在 39 名供料之後（第 4 步無停止條件，已一併做完）。

## 1. G255 —— 本包數字與重算（R-P379(c)）

抄錄前逐一重跑，**4 / 4 相符**：

| 條文所引 | 機讀來源 | 重算 |
|---|---|---|
| 六名七條 | `g252_six_63.md` 之 `## ` / `### ` 標題計 | **6 名 / 7 條** |
| 39 | `proxy_reachability_63.md` 之 `**有錨**` 列 | **39** |
| 22 / 17 | `observable_proxy_64.md` 總計行 | **填不出 22 / 可填 17** |
| 0 查無 | 65 包 §0 人讀之結論 | **0**（開 DR 1）|

現行最大號：`DR-PW26` → 開 **`DR-PW27`**；`A-PW364` → 開 **`A-PW365`**。

## 2. 抄錄與登記

- `RULINGS.md`：**R-P383–R-P385** 逐字抄入（3 / 3）。§J 重驗：3/3/三條，一致。
- R-P36 加註一處：**R-P382**（產出退回，二項理由）。
- `ANOMALIES.md`：**A-PW364 加註**（「方向相反」→「二者非同一變數」）、**A-PW365**（見 §6）。
- `DATA_REQUESTS.md`：DR-PW26 第 (1) 問拆為 (1a) / (1b)；**新開 DR-PW27**（未尋獲文件型）。

## 3. R-P383 —— 七條改寫（`apply_r_p383_65.py`）

7 / 7 全數命中並落檔（`batch_002` / `batch_004` / `batch_005` / `batch_007`）。
JSON round-trip 逐位元組一致，diff 僅該七條。

| tc_id | 原 `<X>` | 改為 |
|---|---|---|
| `-027` | `call audio routing and the TLM state` | 手機端顯示 ＋ HU 揚聲器通話音訊 (iii)、來電 pop-up (ii)、`PowerSts_Telematic = 2` (i) |
| `-031` | 同上 | HU 揚聲器通話音訊 (iii)、`PowerSts_Telematic = 2` (i)；`Timeout1` 前置改 `ENTER_TIMED` ＋ `$BCM_FD_27.Comfort_Enable_Time$` |
| `-117` | `remote start outcome flag and the TLM state` | `PowerSts_Telematic = 1` (i)；`RemStartFail` **維持 PENDING** |
| `-172` | `HU behavior and the stored logs` / `both processors` | 畫面熄滅後重顯 `"Splash Screen"` (ii)、bus trace 上 `$STATUS_TELEMATIC$` 中斷後恢復 (iv) |
| `-224` | `shown wording` | `"Disclaimer"` 畫面／geolocation pop-up (ii)；文字 **PENDING: DR-PW27** |
| `-262` | `TLM_Status.Info after each one` | `PowerSts_Telematic = 4` (i) ＋ 音源持續播放 (iii) |
| `-271` | `TLM state again after Timeout1 has elapsed` | `= 2 (Timed)` → `Hold for $BCM_FD_27.Comfort_Enable_Time$` → `= 1 (Standby)`，皆 (i) |

驗證：七條之舊複合名**殘留 0**；Remarks 皆標 `(R-P383)`；
五欄逐字相同對仍 **11**（未增減）。

副作用（據實記）：
- **家族 K 158 → 154** —— `-117` / `-172` / `-224` / `-179` 之 ITD 回指經內聯而消失；
  `-262` 依 R-P366(c) / R-P373(a) **保留**（(c) 類），故不為 0。
- **corpus 之 PENDING 由 0 → 2**（`-117`、`-224`）—— 此為 I 家族首次由 0 回升，
  與 55 包 §六所預告者一致。S6 甲案下該二條不出貨。

`-172` 之 **IN §8.2.1 移除**已落實：原 ER 2「collects and saves logs」屬 `CFTS009-4941860`，
非本條 `test_item` 所本之 `4941861`，已移除並於 `reasoning_note` 註明由該錨點之 TC 承擔。

## 4. R-P384 —— 39 名供料頁

落檔 `data/g252_thirtynine_65.md`（109 KB，39 名 / 67 條 TC）。
**不判定、不查詢；複合觀察目標保留原形，未預拆**（R-P384(d)）。
錨點自 `layer3_full.tsv` 之 `leaf → item_ids` 取，段落全文逐字。
**39 名之錨點全部取到，缺口 0。**

`observable_proxy_64.md` 之退回本層無異議 —— R-P384(a) 之指摘成立：
機器抽出之 (i) 類確為段落中之**觸發**訊號（`disclaimer wording` → `CmdIgnSts`、
`displayed font` → `Radio_Theme`），**本層當時未區分觸發與觀察**，
該區分正是 R-13 之核心。R-P384(b) 之「具名不以引號為要件」亦成立，
本層之收緊判準（須含 UI 名詞且非值）把規格未加引號之具名元件一併篩掉了。

## 5. ⚠ R-P385(b) 之實際適用列為 **1**，非 9

`$PowerMode$` 於現行 corpus 出現於 **9 條 TC**，惟：

| 出現處 | 條數 | 可否改 |
|---|---|---|
| **僅 `test_item` 上半 verbatim** | **8** | **不得改** —— 該處為規格逐字（R-6 / R-P343 / R-P347）|
| `input_test_data`（`-179`：`$PowerMode$: "IGN_START"`）| **1** | 可改 |

故 R-P385(b)「凡 TC 引 `$PowerMode$` 之步驟改以候選寫」之實際適用列為 **1 條**。

`-179` 已改：ITD 依 R-P366(a) 內聯 → 步 1
`Send the signal $STATUS_BH_BCM2.CmdIgnSts$ = 5 (START) during the animation (DR-PW26)`，
ITD 改 `NA`，Remarks 標 `(R-P385(b) 候選，待上游確認)`。
`IGN_START` 對 `VAL_ 1132` 之 `5 "START"` 為 `IGN_` 前綴差，與 R-P385(b) 之判準一致。

**本條未動之處據實記**：`-179` 步 2 之 `screen and the power mode`（複合非白名單 `<X>`）
與 ER 2 之 `as defined`（R-P353 末段所禁）**屬 B5 範圍，本包不動**。

## 6. A-PW365 —— 63 包之 6 個「查無」經人讀全部推翻

65 包 §0 人讀結果：**查無 0**、TC 措辭問題 6、新開 DR 1。

執行層於 63 包已保留（「本輪仍非人讀」「6 個查無不足以登 R-G13」），**該保留正確**——
若當時逕行開 6 個 DR 並登 M-n，**將有 6 筆誤報進入全案查無台帳**，
而 `LOOKUP_MISSES.md` 之設立目的正是避免重複發現，誤報之代價由全案承擔。

**本條為 A-PW355 教訓之第一次正面驗證**：前三次（A-PW355 / A-PW361 / A-PW364）
皆為「查得不夠而誤判不存在」，本次為「**疑而不報，事後證明疑得對**」。

## 7. 現況

| 項 | 值 |
|---|---|
| corpus | 283 條 |
| PENDING | **2**（`-117`、`-224`）|
| 內部訊號 PENDING（R-P380 甲）| 99 |
| 家族 K 殘留 | 154（(c) 類 1 條為應保留者）|
| 五欄逐字相同對 | 11 |
| G0 | 素材 9/9 ＋ 參考庫 7/7 |

## 8. 待裁

1. **39 名之代理量**（§4）：供料頁已備，待分析層 66 包逐名人讀。
2. **R-P385(b) 適用列為 1**（§5）：條文預期與實測之落差已記，是否須訂正條文。
3. `-179` 之殘留缺陷（`screen and the power mode`、`as defined`）歸 B5，確認無誤。

**B5 依 R-P374(a) 續凍。**
