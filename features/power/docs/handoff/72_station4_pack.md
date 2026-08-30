# 72 — 六閘全綠；站④ 完整目視包與 sandbox 工作簿；DR 發送清單

下放包 | 分析層 → 執行層 | 往返 NN = 72

前置：`data/71_report.md` 已覆核，判定 **ACCEPT**。六閘全案首次歸零；字典套用限定 170 條而不破壞既有正確內容之設計決定正確；
`AUD_LVL` 取 FDCAN8 逐字同名、`AUD_LVLSts` 不採——**確認**（R-P389(a) 判準）；四處補正皆據實。
本包為站④ 準備包，**不寫回、不出貨**（S6）。

## 0. 分析層之誤（自陳）

71 包字典之 `played animation` 條目寫入 `normal brand animation`，**分析層自己違反 R-P353 末段**；
執行層 IN §11 引號三犯，分析層字典同樣未加引號 —— 產生器與字典之書寫規則須由 lint 擋而非靠人記。登 A-PW。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P397] 站④ 標的 = 全 287 條；先出 sandbox 工作簿與目視包；IN §11 引號入 lint。
         （a）執行層自現行 batch JSON 產出 `sandbox/b72/pm_72.xlsx`
              （openpyxl 寫入 ＋ XML 修補，方法同 27 包；SHA 記 MANIFEST；**不複製至 delivered/**），
              另出 `data/reviewed_287_72.md`（tc_id／req_id／五欄／Remarks，逐字）；
              二者為 Pei 站④ 之標的，`reviewed_75_69.md` 由其取代
         （b）IN §11 引號規則入 lint：Procedure／ER 中出現 R-P353(ii) 類名詞
              （screen／icon／pop-up／logo／animation／button／menu／font／graphic／gauge／avatar）
              而未以 `"…"` 包覆者列出，期望 0；新增 G256
         （c）站④ 期間執行層不改 corpus；Pei 抽查所出之項以 Remarks 標 `(站④-n)` 由分析層逐項裁
         裁決者：分析層（Tier 2）。
```

## B. DR 發送清單（Tier 3 事項，交 Pei）

S6 之解消途徑只剩上游回覆。**開中 7 張 DR 是否已實際送出，分析層無從得知**（發送權在 Pei）。
請 Pei 核對下表「已送／未送」；未送者本包附 `DATA_REQUESTS.md` 現行條文可直接發：

| DR | 級別 | 內容 | 影響條數（`pending_recount_71.tsv`）| 開立包 |
|---|---|---|---|---|
| DR-PW23 | High | 內部訊號 13 名之驅動／觀察方法 | 最多 | 22/23 包，58/62 包擴大 |
| DR-PW25 | — | 設定項名（timeout／auto switch-on）| | |
| DR-PW26 | High | ENTER_INIT／ENTER_SLEEP 觀察面；`LTM_OperationalModeSts` ≟ `OperationalModeSts`；`$PowerMode$` ≟ `CmdIgnSts`；`Comfort_Enable_*` 確認 | | 57 包 |
| DR-PW27 | — | HMI／PDO 參考文件七項（disclaimer 文字、PDO Theme Config、graphics、TLM HMI docs、CFTS057、CFTS024／VF654）| | 65/66 包 |
| DR-PW28 | High | `VC_*` 命名空間 9 名 ＋ `$TBM_Present$` 之載體與值域 | 277 處引用 | 67 包 |
| DR-PW29 | Low | `4941453` 雙列；ICS≟DCSD；FPDM 展開；ANC/ACN 觀察面 | | 67/68/71 包 |
| DR-PW30 | Medium | `SplashScreen_Time`／`StandardScreen_Time`／`Response_Wait_Time` 值 | | 67/71 包 |

## H. 作業指示

1. 抄 R-P397；§0 登 A-PW；G256 實作並跑全案
2. `sandbox/b72/pm_72.xlsx` ＋ `reviewed_287_72.md`，`get_file_info` 驗二檔
3. Excel GUI 開啟驗證留 Pei（DELIVERY_CHECKLIST 手動項）
4. 上繳 `features/power/docs/upstream/72_station4_pack.md`，附 G255／G256 表

## I. 禁區

沿用 71 包 §I。不得複製至 `delivered/`；站④ 期間不得改 corpus（R-P397(c)）。

## J. 自檢

一條。對既有 canon：S6 — 不出貨，合；R-P374(a) 甲 — 不變；IN §11 — (b) 為其 lint 化；R-P200(a) — 前包不改。

本包數字（R-P379(a)）：287／146／10／3（`71_report.md` §4–§6）。

## K. 待 Pei（三項，皆 Tier 3）

1. **站④ 抽查**：`pm_72.xlsx`（Excel 開）＋ `reviewed_287_72.md`。
2. **DR 是否已送**：§B 七張逐張核對；未送者請發。146/287 PENDING 全繫於此。
3. **S6**：甲（等）／乙（分段出貨 141 條，146 條附清單）／丙（逐名審）。不開口即甲。
