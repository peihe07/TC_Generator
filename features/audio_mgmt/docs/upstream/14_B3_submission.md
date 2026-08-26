# Audio Management — 上繳包 14：Batch B3 交付

- 日期：2026-08-26
- 對應下放包：`docs/handoff/12_B3_final_anchors.md`
- 依據裁定：R-AM1–R-AM20

---

## 一、交付摘要

| 項目 | 值 |
|---|---|
| 批次 | B3（Mute Requests 後 13 ＋ Volume Control 前 37） |
| 葉數 | 50／50 |
| TC 數 | 63 |
| Test Set 分佈 | Mute Requests 18，Volume Control 45 |
| Priority | P0 3，P1 60 |
| 設計方法 | 功能測試 21，決策表 14，狀態轉換 13，負向測試 10，邊界值分析 5 |
| 池外錨 | 7（**單源佐證**，R-AM18） |
| 無錨葉 | 2（026、076a） |
| 交付簿 | `SWQT_AudioMgmt_B1-B3.xlsx`，**199 列**，tc_id `NR1L-AMM-001`–`199` |
| 交付簿 SHA256 | `4b25c38669d35f482f0e91ce3cce55d409f0def7cf3acfc0edde3cfdd5c30243` |

累計：B1 70 ＋ B2 66 ＋ B3 63 ＝ **199 條／150 葉**（318 葉之 47%）。

## 二、§9 自檢與 Lint

自檢 63 條全過；`lint_tcs.py --batch B3 --profile audio_mgmt` **green**（十六項）。
步驟 1 起始狀態提示歸零（14 條補 pre_conditions）。

首輪 lint 攔下 **11 項違規**，全數為真並已修正：檢查 O（無錨葉之 PENDING
格式，屬 lint 本身之缺口，已放寬並同步修 selfcheck）、檢查 L（四葉逾 R-3
50 token，摘句處理）、**檢查 P（見 §三）**。

## 三、檢查 P 攔截下放包之訊號判定（首例）

包 12 §四.6 將 `$ShiftLeverPosition$` 列入「HU 側 CAN 定義整體缺件，
依 R-13(g) 保留原文名」清單。第二路實測：**DBC 確實載有該訊號**——

> `TRANSM_FD_4.ShiftLeverPosition`，`VAL_` 表 `2 = "R"`、`4 = "D"`，
> 與規格原文之 `[R]` 相符。

處置：288/290/291/295 四條改寫為 §8.7.5 v3(a) 全名式
`$TRANSM_FD_4.ShiftLeverPosition$ = 2 (R)`，**不掛 DR-AM4**。

成因（R-AM20 附記已載）：該訊號屬**變速箱側** TRANSM_FD_4，不在 B2
「HU 側整體缺件」之結論母體內，係歸納範圍溢用。

其餘 B3 訊號依包 12 §四.8 之新規則以**大小寫不敏感**複查，確認全部查無，
維持 R-13(g) 處置。

## 四、逐案處置之落實（對應包 12 §三）

| 葉 | 裁定 | 落實 |
|---|---|---|
| 026 | 無錨，PENDING: DR-AM1 | `spec_reference` 帶 PENDING；TC 依 SWE.1 描述撰寫，未代入 4866011/4866015（其驗證對象為斜坡連續性） |
| 076a | 無錨，PENDING: DR-AM1 | 同上。reasoning 註明本列為 SYS-RA-AMM-242，076b 已於 B2 交付；交付欄依 R-AM6 同讀 `SWE1_AMM_076` |
| 050 | 部分覆蓋 | 僅驗三類別音量互不影響；未寫 Radio Performance Standard 之細節（R-AM5 範圍外，且包 12 禁引為錨） |
| 087 | 部分覆蓋，4866221 | 取 4866221 不取 4866223（僅前者含 HU HMI Specification）；未寫 Routing_Table 對應 |
| 088 | 改錨 4866230 | 已採。原 4866309 為 fader/balance 之結構平行句 |
| 147 | 併列 4866527 ⏎ 4866878 | 兩行升冪。4866878 池外，該半為單源佐證 |
| 291 | 部分覆蓋，DR-AM9 | 僅驗抑制解除；CFTS028 內容一字未寫 |
| 055/056 | 改錨 4866152/4866153 | 已採（原候選為查表值定義，非行為條款） |
| 072/075、054/065、084/091、147/158 | 四組共錨（R-AM16） | 括號下半逐字不同，各寫側重 |
| 081/082 | 市場列舉對，須成對 | 兩條齊備（NAFTA=Off／非 NAFTA=Level 1） |
| 114/119 | 同文異錨對 | 括號分取 fade 與 balance 兩控制 |

## 五、池外錨登記表（R-AM2′／**R-AM18 單源佐證**）

| 葉 | 錨 | Title | 佐證強度 |
|---|---|---|---|
| SWE1_AMM_147 | CFTS019-4866527 | Audio Management - Information Volume Re | 單源佐證 |
| SWE1_AMM_288 | CFTS019-4866823 | Audio Management - Reverse Entertainment | 單源佐證 |
| SWE1_AMM_289 | CFTS019-4866824 | Audio Management - VR Request Suppressio | 單源佐證 |
| SWE1_AMM_290 | CFTS019-4866825 | Audio Management - Entertainment Audio R | 單源佐證 |
| SWE1_AMM_291 | CFTS019-4866826 | Audio Management - VR Request Resumption | 單源佐證 |
| SWE1_AMM_295 | CFTS019-4867710 | Audio Management - Reverse Mute Disable  | 單源佐證 |
| SWE1_AMM_296 | CFTS019-4867712 | Audio Management - Reverse Mute Default  | 單源佐證 |

**R-AM18 之標記意義**：匯出既無該物件，第二路無獨立語料，只能回讀全文，
與第一路同源。此類「雙路」為同源二讀，**不構成獨立佐證**。
DR-AM3 全文件重匯回件後須以新池重跑並回溯覆驗。

## 六、PENDING 清單

| DR | 條數 | 葉 |
|---|---|---|
| DR-AM1（無錨） | 2 | SWE1_AMM_026、SWE1_AMM_076 |
| DR-AM4（訊號） | 35 | 多葉 |
| DR-AM9（CFTS028） | 1 | SWE1_AMM_291 |

## 七、寫回驗證

48 成員不變、僅 `sheet6.xml` 受改、`<dataValidation>` classic 3 ／ x14 1 不變、
`<conditionalFormatting>` 不變（母本計數 0，仍為 vacuously true）、
逐列回讀 63 列追溯性與完整性全符、累積 199 列 tc_id 001–199 無重複無缺號。

## 八、B2 之出處更正（連帶事項）

`<Vent off>` 之出處判定經分析層更正並經執行層複驗：定義列存在於
**CFTS019-4867782**（`<Vent off> = -16 dB`，Radio 清單含 R1L-R），
故該值為 spec-sourced。原判「文件中無定義」係**大小寫敏感檢索**所致
（小寫 1 筆、首字大寫 8 筆）。

287 之 reasoning 已改引 4867782；交付欄摘要比對前後一致，工作簿未重寫。
spec_reference 之補列（287→4867782、312–317→4867783）依 R-AM18 併入
回溯覆驗站，不觸發即時回修。

此錯之機制已登記 A-AM08：原註寫「檢索此值者將查無」，本意防誤判，
實際會使後人放棄尋找一個存在的定義——**假留痕比無留痕糟**。
包 12 §四.8 已將「大小寫不敏感複查」立為掛 PENDING 之前置。

## 九、待分析層

1. 綠色通道自 B4 起適用（R-AM20），本包無待裁項。
2. DR-AM1／AM2／AM4／AM5／AM9 是否送出；DR-AM3 已升級為全文件重匯。
