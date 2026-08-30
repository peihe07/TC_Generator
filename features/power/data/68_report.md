# 68 包 —— 執行層回報

§H 五步全部完成。

## 1. G255 —— 本包數字與重算（R-P379(c)）

R-P392 之 `CM_` 證據**逐字複核 3 / 3 相符**（`forms` DBC 直取）：

| 條文所引 | 實測 |
|---|---|
| `PARK_INFO.ChimeActivation_LHF` | `CM_` = `"This signal indicates the chime activation request for the left hand, front audio speaker, or rear hardwired buzzer."`；訊息 `PARK_INFO`(950)、發送 `SGW`、接收 `ETM,LTM`、`VAL_ 0 "NotActive" 1 "Active"` ✓ |
| `TELEMATIC_FD_5.CM_TCH_STAT` | `CM_` = `"Touch Screen Status"`、`VAL_ 1 "TCH_PSD"`、**發送節點 `ETM`（HU 側輸出）** ✓ |
| `CM_TCH_X_COORD` / `Y_COORD` | `CM_` = `"Value for the touch screen X axis coordinates"` / `Y` ✓ |

R-P392(c) 亦複核：`DIS_CENTERSTACK.DCSD_DISP_STAT` **發送節點為 `SGW`**，
確為輸入非 HU 輸出，不取之判斷成立。

其餘：37（67 包 §1）、12 對 24 處（67 包 §7）—— 未變。
拆分增列數由執行層計 = **4**。

## 2. 抄錄

`RULINGS.md`：**R-P392 – R-P393** 逐字抄入（2 / 2）。§J 重驗 2/2/二條，一致。

## 3. 第二批改寫（§H 第 2 步）—— 25 / 25

`apply_batch2_68.py` → **25 / 25 命中**。含 `-224` 之訂正：
該條於 65 包依 R-P383 改寫時前置寫成 `PROXI VC_VEH_BRAND` / `PROXI TBM_Present`
（其時 66 包 §1 表尚以 PROXI 指定），67 包實測**四名皆不在 PROXI `Format`**，
本包依 R-P389(c) / R-P393(a) 改為保留規格原名。

- `-055`：`FUNC_STATE_PARTIAL_OPERATION` ＋ chime 刺激
  `$PARK_INFO.ChimeActivation_LHF$ = 1 (Active)`，ER 為左前喇叭有 chime 聲 (iii)
- `-202`：`FUNC_STATE_IDLE` —— **Display `OFF (*)` 之 `(*)` 例外含 Splash Screen**，
  故畫面僅 `"Splash Screen"`；ICS 可用取 `$TELEMATIC_FD_5.CM_TCH_STAT$ = 1 (TCH_PSD)`
  ＋ 座標訊號有值 (i)。**ICS↔DCSD 未寫成等同**（§I），Remarks 記「觀察面取自 4941453 Idle 列」
- `-125`：`FUNC_STATE_SLEEP`，`ENTER_SLEEP` 項維持 `PENDING: DR-PW26`，其餘照改
- `-281`：`FUNC_STATE_BENCH`，BoosterOUT／天線之 (v) 類位準值 `PENDING: DR-PW27`
- 品牌指派類 13 條：依 **R-P388 之分流** —— font／App icon（元件已指名）**ER 不 PENDING**；
  theme／element／recirc／gauge／seat（指派在台帳外）ER 該項 `PENDING: DR-PW27`

## 4. §8.3 拆分增列 4 條（§H 第 2 步，R-P393(c)）

| 新 tc_id | 拆自 | req_id | 支別 |
|---|---|---|---|
| **`-284`** | `-169` | `SWE-PM-075` | FOTA pop-up **dismissed** 支 |
| **`-285`** | `-169` | `SWE-PM-075` | `$ACCDlyAct$` **active→inactive** 支 |
| **`-286`** | `-249` | `SWE-PM-087` | **M240** 支（原條為非 M240）|
| **`-287`** | `-182` | `SWE-PM-093` | **下一喚醒週期**支（原條為 30 分鐘）|

**corpus 283 → 287。** 三代對照表已增補第四節（既有 001–283 號碼不變，同 R-P349(c)）。

`-285` 之 `$ACCDlyAct$`：段 1 命中 LID r29 `AccDelayAct` 而其 `Atlantis High` 欄為 `N/A`
（止於段 2）；FD 側同義訊號為 `$BCM_FD_27.Comfort_Enable_Act$`
（`CM_` = `Accessory Delay Active`，與 LID r29 之 `Function` 逐字同，R-P371 型證據），
依 R-P371 之先例採之並標 `(DR-PW26)`。

⚠ `-222` / `-223` 之「依 `Country_Code` 分支各一」—— **二條本即為二分支**
（`-222` = TBM 缺、`-223` = 不需 SOS/geolocation 之市場），**未另增列**，據實記。

## 5. 全 corpus 閘門（§H 第 3 步）

| 閘 | 全案 | **已改寫範圍內** | 未改寫（B5 範圍）|
|---|---|---|---|
| G245 家族 A（上界，R-P362）| 189 | **0** ✓ | 189 |
| G250 `proper` / `as defined` / `normal` | 22 | **0** ✓ | 22 |
| G250 `Read the HU mode/state` | 16 | **0** ✓ | 16 |
| G251 `listed in Input Test Data` | 118 | **3** —— `-005`/`-218`/`-262`，**皆 (c) 類應保留** ✓ | 115 |
| G247 Procedure/ER 內部訊號 | 97 | **9** —— **9 / 9 皆為 `PENDING: DR-PW23 <名>` 佔位句** ✓ | 88 |
| G249 五欄逐字相同對 | **12** | 全為 **(b) 型**（req_id 皆不同），互註 **24 處**齊備 ✓ | — |
| G246 使用 `ENTER_<STATE>` | 40 | — | — |

**已改寫 75 / 287；未改寫 212（B5 範圍）。**

### ⚠ 二處補正，據實記：本層於第二批**重蹈第一批之誤**

第二批首輪 G245 於已改寫範圍內殘留 **15 條**，成因與 67 包完全相同 ——
**具名 UI 元件未加引號**。R-P384(b) 之「不以引號為要件」為**抽取**判準，
**書寫仍依 IN §11**。67 包已自陳過一次，本包又犯。

補正：`"Incoming Call"` pop-up、`"Rear View Camera"` video、`"Start-up Animation"`、
`"Theme"`、`"PDO Branded Element"`、`"Recirc Icon"`、`"Seat Graphic"`、
`"Performance Gauges"` 加引號；音訊面改明寫 `on the HU speakers`
以落 R-P353(iii)「指定揚聲器有／無輸出」。補正 15 條後 G245 已改寫範圍內歸零。

## 6. PENDING 重算（§H 第 4 步）

`data/pending_recount_68.tsv`。

| 項 | 值 |
|---|---|
| corpus | **287** |
| corpus 內 `PENDING` 文字 | **36**（67 包 20 → 本包 36）|
| 內部訊號 PENDING（R-P380 甲，未改寫範圍）| 99（未變）|

⚠ **PENDING 由 20 升至 36** —— 第二批之 DR-PW27（品牌指派、位準值）、
DR-PW26（`ENTER_SLEEP`）、DR-PW23（`Rear_Camera_Enable.Info` 運行時）佔位所致。
**S6 甲案下該 36 條不出貨。**

## 7. 待裁

1. **`-222`/`-223` 之分支**（§4）：二條本即二分支，未另增列，請確認 R-P393(c) 之意。
2. **B5 範圍之 212 條**：本包後第一、二批合計 75 條已達站④ 可審狀態；
   其餘 212 條之 G245 189／G250 38／G251 115 仍在。**下一包若給總帳，該三數為主軸。**
