# 62 — R-P368 段 1 之範圍擴至 forms/ 全部參考檔

下放包 | 分析層 → 執行層 | 往返 NN = 62

前置：Pei 2026-08-30 問「會不會已經可以查到了」。分析層實查 `forms/` 內 LID／DBC 以外之三檔，
**有命中**。R-P368 把段 1 限於 LID `CAN Mapping`，是分析層對 Pei「以 forms 為主」之窄讀。
寫回移至 63 包。

## 0. 分析層之誤（自陳）

Pei 08-30 指示為「以 `forms` 為主」，未限於 LID／DBC。R-P368(a) 將段 1 定為 LID `CAN Mapping`
單一入口，(c) 之 PROXI 路徑又以「PROXI 參數」為前提，致 `.Req` 類設定值與 `.Info` 類致能狀態
從未被拿去查 `HMI Settings List`、`PROXI Format`、`SR26 Default Settings`。
執行層依條文施作，無誤；**窄讀在分析層**。登 A-PW。

分析層實查（`openpyxl` 全表 regex，僅示命中，**不認定同一物**）：

| 規格原名 | 命中檔／分頁／列 | 命中值 |
|---|---|---|
| `Auto_SwitchOn_Setting.Req` | HMI Settings List `Settings` r96–97 c2/c4 | `Auto-On Comfort` / `Auto_On_Comfort_Remote` / `Auto_On_Comfort_No_Remote` |
| 同上 | PROXI `Format` r354 / r639 c6 | `Auto_On_Comfort_Enable` / `Auto_On_Comfort_Menu` |
| `SwitchOff_Timeout_Setting.Req` / `SwitchOffSetting.Req` | PROXI `Format` r510 c6 | `Switch_Off_Time` |
| `Rear_Camera_Enable.Info` | PROXI `Format` r401 / r494 c6；SR26 Default `Default Parameters` r14–15 c12 | `Rear_View_Camera` / `Rear_View_Camera_Soft_Button` / `Rear Camera Present` |
| `RemStartFail` | PROXI `Format` r469 / r1013 c6 | `Remote_start` / `Wired_Remote_Start_Presence`（**存在性參數，非失敗狀態**，僅記） |
| `Phone_Call.Info` / `Antitheft_*` / `Front_Panel_OnOff.Req` / `Audio_Data_Exchange.Info` | 三檔 | 無可用命中 |

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P375] R-P368 段 1 之入口擴為 forms/ 全部參考檔；設定類與致能類另走 UI／PROXI 路徑。
         （a）段 1 入口自 LID `CAN Mapping` 擴為 `forms/` 所列全部參考檔：
              LID 全分頁、`HMI Settings List R1 SR25`、`PROXI_HDCC27_R3` `Format`、
              `SR26 Default Settings and PNet ECU Configuration`、
              `SR24 R1 Market Configuration Table`；每一檔以 FORMS.md 之 SHA 入台帳
         （b）`.Req` 類（`Auto_SwitchOn_Setting.Req`、`SwitchOff_Timeout_Setting.Req` /
              `SwitchOffSetting.Req`）為 HMI 設定值：
              段 1 命中 HMI Settings List 者 → TC 以 UI 元件寫
              （`Select "<設定名>" = "<值>"`，白名單 (ii)）；
              命中 PROXI `Format` 者 → `PROXI <Param> = <值>`（R-1 v3 (c)）；
              二者皆命中時，Procedure 用 UI、Pre-Condition 用 PROXI，各引其列
         （c）`.Info` 類致能狀態（`Rear_Camera_Enable.Info`）：
              命中 PROXI／Default Settings 之存在性參數者，為 Pre-Condition
              `PROXI <Param> = <值>`；其運行時狀態仍須 CAN／UI 觀察面，另查
         （d）命中即「候選」，非認定：每一候選於 DR-PW23 附表記
              `候選（檔／分頁／列）`，TC 施作以候選寫，並於 Remarks 標
              `(DR-PW23 候選，待上游確認)`；**PENDING 佔位撤除**，
              上游否認則回滾（同 R-P371(c) 之處置）
         （e）R-P368(b) 不變：候選之比對依據須載明欄／列；語意跳接仍不許。
              `RemStartFail` 對 `Remote_start`（存在性）**非候選**，維持 PENDING
         （f）DR-PW23 附表重做為 `dr_pw23_internal_signals_62.md`；PENDING 重算
         R-P368 依 R-P36 原文不改，加註指向本條。
         裁決者：分析層（Tier 2，訂正對 Pei 08-30 指示之窄讀）。
```

## H. 作業指示

1. 抄 R-P375；R-P368 加註；§0 登 A-PW
2. G0 台帳增列 (a) 之檔（SHA 取 FORMS.md；FORMS.md 未載者先算並補登 FORMS.md）
3. 十一名依 (a) 全檔重查，附表 `dr_pw23_internal_signals_62.md`，欄同 58 版加 `候選來源`
4. PENDING 重算 → `pending_recount_62.tsv`
5. 61 包 R-P374(c) 丁案試作照做（`RemStartFail` 仍 PENDING，試作對象不變）
6. 上繳 `features/power/docs/upstream/62_forms_full.md`

## I. 禁區

沿用 61 包 §I。不得將「命中」寫成「解得」（R-P375(d)）。不得以存在性參數代狀態（R-P375(e)）。

## J. 自檢

一條。對既有 canon：R-P368 — 擴其 (a)，加註；R-1 v3 (c) — (b) 引用，合；R-P353 白名單 — (b) 落 (ii)，合；R-13 — (d) 回滾條款，合；§8.4.1 — (d)(e) 候選不認定，合。無違反。

## K. 待 Pei

無。
