# 下放包 20：PM 收尾（台帳補記、DR 證據補強、lint 缺口）

## 一、PENDING 措辭偏離 —— **追認**

下放令之 `PENDING: DR-PW22 geolocation pop-up 與 disclaimer 之擇一判準`
含中文，寫入 proc／er 將觸發 lint K，與同包「lint A–N 全零」互斥。
執行層改用等義英文並將中文描述置於 DATA_REQUESTS.md，**處置正確**。

成文（避免再犯）：
```
R-14 PENDING 佔位之語言
`PENDING: DR-{n} <說明>` 寫入 TC 欄位時，`<說明>` 一律英文
（canon §1 TC 欄位 English only）；中文描述置於 DATA_REQUESTS.md
之 DR 條文。下放包擬定 PENDING 字串時同此。
```
分析層之疏失：擬定字串時未套用自身既有之 §1 規則。

## 二、R-9～R-12 補記台帳（分析層補擬，執行層逐字寫入）

四條為本次 283 列改寫之主要依據，未入正式帳。執行層未逕自補記
（逾本包所令）—— 判斷正確。補記格式比照既有 R 條文：

```
| R-9  | 2026-08-21 | Pre-Condition 一條件一行一編號 | ACTIVE | 13 | 全案 |
| R-10 | 2026-08-21 | 空白與字元正規化（分區適用） | ACTIVE | 13 | 全案 |
| R-11 | 2026-08-21 | 一觀察點一步驟／須寫出應觀察值／Input 一律 NA | ACTIVE | 14 | 全案 |
| R-12 | 2026-08-21 | Pre-Condition 句式與排序（工具行置末） | ACTIVE | 15 | 全案 |
| R-13 | 2026-08-21 | 規格訊號名與 DBC 不符時保留原文名 | ACTIVE | 19 | 全案 |
| R-14 | 2026-08-21 | PENDING 佔位說明一律英文 | ACTIVE | 20 | 全案 |
```
並於 R-12 列後加註：
> R-12(b)（spec_ref 條數上限 4）已於 `specref_anchor_chain_verified.md`
> 撤銷；R-12 現行僅存 (a) Pre-Condition 句式與排序。

## 三、DR-PW21 證據補強（分析層實測，補入該 DR 條文）

```
DBC 實查（BH-CAN sha256 9ef1ec98…30d0；FD-CAN8 51c8fd60…1cd2）：
VAL_ 854 PowerModeSts 0 "Standard_Power" 1 "Logistic_Mode_ON"
                      2 "Logistic_Mode_PR" 3 "LogisticModeON_and_EngineON"
CFTS009-4941562 原文：signal PowerModeSts_Telematic passes from
                      "Standard_Power" to "Logistic_Mode_On"
→ 二值逐字相符（僅 ON/On 大小寫）。研判 PowerModeSts_Telematic
  即 STATUS_BH_BCM1.PowerModeSts（BH-CAN），規格加 _Telematic 後綴。
  請上游確認。若確認，row 72 應改：
    PROC 1: Send the signal $STATUS_BH_BCM1.PowerModeSts$ = 0 (Standard_Power)
    PROC 2: Send the signal $STATUS_BH_BCM1.PowerModeSts$ = 1 (Logistic_Mode_ON)
  觸發（BCM 側）與觀察（TLM 側 PowerSts_Telematic）之因果結構即回復。
```

**現行寫法在 R-13 下正確，維持不動**；證據強度雖高，
「規格名 = DBC 某訊號」之認定屬上游職權，分析層不代為認定
（§8.4.1）。執行層「不是終局」之判斷正確，已登記。

## 四、verify.py 覆蓋缺口（登記，不在本包修）

`read_without_value` 僅檢 proc，row 291 之 ER 2 為純 PENDING 行，
屬**未覆蓋**而非通過 —— 執行層之自我判斷正確，予以登記為
**A-PM16**。俟 lint feature-scoped 改寫時一併納入（見 §五）。

## 五、lint feature-scoped 改寫 —— 另立包，排入

執行層指出：Q／R 若已入 lint，本次 CJK 衝突會在下放階段被攔下，
而非由執行層自行發現。**此論成立。**
依 17 包 §四之裁定，以 `--profile <feature>` 實作，
未指定時行為與現行八本基線完全一致。
併入 A-PM16 之 ER 側檢查。**另立包，不併入 PM 內容批。**

## 六、執行

基底 `sandbox/b19/pm_19.xlsx`（b4dd5ca0…）。
本包**不改工作簿內容**，僅文件：
1. RULINGS_LEDGER.md 補記 §二之六列
2. DATA_REQUESTS.md 之 DR-PW21 補入 §三證據段
3. ANOMALIES.md 新增 A-PM16（§四）

上繳 `docs/fw036/upstream/20_pm_closeout.md`，附
「本包是否仍有該驗而未驗者」獨立判斷。
