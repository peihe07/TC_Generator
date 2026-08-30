# 原子 token 代理量字典（71 包 / R-P396(a)）

> **逐字採 71 包 §1 表**（R-P396(a)：`proxy_dictionary_71.md` 逐字採該表）。
> 母體 59 token 出自 `composite_tokens_70.md`；**覆蓋 59 / 59，未覆蓋 0**（執行層複核）。
> 分類：直接代理 41、佔位 `PENDING` 12、既裁確認 6、查無 0。

> ⚠ 本檔為**分析層人讀之產物**（R-P395(b)），執行層只機器套用（R-P395(c)）；
> **字典外之代理量不得自填**（R-P396(e) / §I）。

---

## 0. 字典建法

59 token 逐一人讀（token 表 ＋ 29 個代表錨點全文皆讀）。
代理量取自：66 包 §1 表先例、`4941453` 狀態表（R-P387(b)）、R-P392、R-P368 已解得訊號。
**同義判定**（70 包 §6-2）：規格全篇以 `TLM_Status.Info and $Telematic_Power$` 成對書寫且值恆同，
`TLM state`／`HU mode`／`power mode` 於各錨點所指皆為同一狀態機之狀態名 —— **五者判為同物**，
代理量同為 `$STATUS_TELEMATIC.PowerSts_Telematic$`；`TLM_Status.Info` 之內部性不再單獨佔位。

## 1. 字典（`data/proxy_dictionary_71.md` 逐字採本表）

類別：(i) 訊號 (ii) 具名 UI (iii) 音訊 (iv) log/bus (v) 電氣 P = `PENDING: DR-PW{n}`。
`<STATE>` = 該 TC ER 所期望之狀態；`<VAL>` 取 `VAL_ 1470`。

### A. 狀態機（合計 105 次）

| token | 代理量 | 類 | 依據 |
|---|---|---|---|
| `TLM_Status.Info` | `$STATUS_TELEMATIC.PowerSts_Telematic$ = <raw> (<STATE>)` | (i) | R-P368；同義判定 §0 |
| `$Telematic_Power$` | 同上 | (i) | LID r2069 逐字 |
| `TLM state` | 同上 | (i) | §0 |
| `HU mode` | 同上 | (i) | §0；`4941375` 之 IDLE／Full-Operation 為同一狀態名集 |
| `power mode`、`its power mode` | 同上 | (i) | §0 |
| `TLM power indication` | 同上 | (i) | 66 包 `-271` 先例 |
| `HU timer` | `-122` 之 8 日計時器不可觀察；子項 `P: DR-PW26 Suspend-to-RAM 觀察面`（併 ENTER_SLEEP 問）| P | `4941990` 無觀察面 |

### B. 畫面（合計 88 次）

| token | 代理量 | 類 | 依據 |
|---|---|---|---|
| `screen`（50）| `FUNC_STATE_<STATE>` 之 Display 子項；TC ER 若已指名畫面則用該名 `"…"` | (ii) | R-P387(b)；`4941453` Display 欄含 `(*)(**)` 註腳 |
| `display`、`TLM display` | 同上 | (ii) | 同上 |
| `TLM display before`、`after SplashScreen_Time`、`TLM display through SplashScreen_Time` | `"Splash Screen"` 於 `SplashScreen_Time` 前未顯示／後顯示（錄影時間戳）；時間值 `P: DR-PW30` | (ii)+P | 66 包 `-004` 先例 |
| `shown Splash Screen` | `"Splash Screen"` | (ii) | 既裁 |
| `its duration`（`-105/106`）| `"Splash Screen"` 顯示時長 = `Response_Wait_Time`；該值執行層查 PROXI `Format`／CFTS009 參數節，查無 → 併 DR-PW30 | (ii) | `4941600` |
| `display backlight` | 畫面全暗（背光 OFF）；顯示 HMI 畫面時亮 | (ii) | `4941895` 逐字 |
| `screen sequence` | 依序 `"Start-up Animation"` → `"Splash Screen"` → `"Disclaimer"`，三者分別顯示 | (ii) | `4941942` 逐字「separately」 |
| `startup flow`、`HMI`（`-219~221`）| `"Geolocation + SOS"` pop-up 顯示 (ii)；流程細節 `P: DR-PW27`（GDPR flow in HMI）| (ii)+P | `4941962` 「in the HMI」 |
| `avatar list in the profile screen` | `"Profile"` 畫面之 avatar 清單為 `"<Brand> avatars"`；辨識參照 DR-PW27，ER 不 P | (ii) | `4942027` 指名；R-P388 分流 |
| `shown seat graphic` | 66 包 `-249` 先例：指派在台帳外 → `P: DR-PW27` | P | R-P388 |
| `applied theme`、`configured value` | theme 由 `VC_SpecialPKG` 決定，值定義在 [PDO Theme Configuration] → `P: DR-PW27` | P | `4942013`；R-P388 |
| `its timing`（`<Tsend>`）| `P: DR-PW27`（`<Tsend>` 無值）| P | 66 包 `-231` 先例 |
| `played animation`、`season the HU determines` | new season animation／normal brand animation (ii)，辨識參照 DR-PW27，ER 不 P | (ii) | 66 包 `-255~258` 先例 |

### C. 音訊（合計 31 次）

| token | 代理量 | 類 | 依據 |
|---|---|---|---|
| `audio`、`entertainment audio`、`audio output`、`audio output state`、`TLM audio output state`、`audio path`、`AMP` | HU 揚聲器有／無娛樂音訊輸出 | (iii) | R-P353(iii)；`4941453` Source／AMP 欄 |
| `active source`、`active audio source` | 音源指示器顯示 `"<source>"`；「restore」型用 baseline (f)：`record as Source_initial` → 通話後 `Check that Source_after = Source_initial` | (ii)+(f) | `4941720` 逐字「restore the active source」 |
| `volume limit` | `AUD_LVL` 訊號值 = 20；訊號名執行層走 R-P368 解（LID `AUD_LVL`）| (i) | `4942354` 逐字「send the AUD_LVL signal」 |
| `audio output for ANC`、`chimes` | chime：R-P392(a) 刺激 ＋ 左前喇叭有聲 (iii)；ANC／ACN：規格無刺激與觀察面 → 子項 `P: DR-PW29`（附問）| (iii)+P | R-P392 |
| `ACN` | 同上 P | P | |

### D. 功能可用性（合計 30 次）

| token | 代理量 | 類 | 依據 |
|---|---|---|---|
| `ICS`、`ICS functionality availability` | `$TELEMATIC_FD_5.CM_TCH_STAT$ = 1 (TCH_PSD)` ＋ 座標有值（可用）；觸控後無該訊號（不可用）| (i) | R-P392(b) |
| `DTV state`、`DTV states`、`DTV functionality availability` | `FUNC_STATE_<STATE>` 之 Display 子項涵蓋（DTV 影像僅經顯示可見）；規格無獨立 DTV 觀察面，Remarks 記 | (ii) | 66 包 `-202` 先例 |
| `TLM`、`active functionality` | `FUNC_STATE_<STATE>` 全組子項 | 多 | R-P387(b) |
| `FPDM` | `FUNC_STATE_<STATE>` 之 Display／Illumination 子項；**分析層判斷** FPDM 指前面板顯示模組，Remarks 記明為判斷非規格明文 | (ii) | `4941453` 欄名「Display / Illumination」 |
| `network state` | bus trace：HU 之 `STATUS_TELEMATIC` 訊息持續發送（Network on）／停止發送（Network off）| (iv) | `4941411/4941417` 逐字「TLM OFF with Network on/off」 |

### E. 內部變數（合計 33 次）— 維持佔位

| token | 代理量 | 依據 |
|---|---|---|
| `VPLastStatus`、`stored last status` | `P: DR-PW23 VPLastStatus` | R-P355(c)／R-P380 |
| `antitheft request`、`Antitheft_Activation.Req` | `P: DR-PW23 Antitheft_Activation.Req` | 同上；19 條 |
| `RemStartFail` | `P: DR-PW23 RemStartFail` | 同上 |
| `SwitchOff_Timeout_Setting.Req`、`Auto_SwitchOn_Setting.Req` | `P: DR-PW23`／`DR-PW25`（設定名）| R-P377(b)／R-P380 |

### F. 其他（合計 8 次）

| token | 代理量 | 類 | 依據 |
|---|---|---|---|
| `HU reaction`（`-159~161`，SOS/Assist 視同通話）| 同通話代理：`"Call Screen"` 顯示 (ii) ＋ 通話音訊 (iii) ＋ 狀態訊號 (i) | 多 | R-P383 `-027` 先例；`4941873` |
| `HU behavior`（`-173`）| R-P383 `-172` 先例：畫面熄滅後 `"Splash Screen"` 重顯 ＋ bus 上 `STATUS_TELEMATIC` 中斷後恢復 | (ii)+(iv) | |
| `$Radio_Theme$`、`$PowerMode$`、`LTM_OperationalModeSts.Info` | 既裁確認可直接套用 | (i) | R-P368／R-P385 |

**59 token 全數有解：直接代理 41、佔位 P 12、既裁 6。查無 0。**
