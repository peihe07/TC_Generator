# Audio Management — 上繳包 21：Batch B5 交付

- 日期：2026-08-26
- 下放包：`18_B5_anchor_candidates.md`（第一路）、`20_B5_final_anchors.md`（定案）
- 對帳：`19_B5_route2_reconciliation.md`（第二路）
- 池基準：展開池 v2，891 ID

---

## 一、交付摘要

| 項目 | 值 |
|---|---|
| 批次 | B5（Tones and Alerts 32 ＋ Audio Processing 前 18） |
| 葉數 | **49／50**（293 留置，見 §三） |
| TC 數 | 50 |
| Test Set | Tones and Alerts 31，Audio Processing 19 |
| Priority | P1 50 |
| 設計方法 | 決策表 20，功能測試 19，負向測試 6，狀態轉換 3，邊界值分析 2 |
| 池外錨 | 11（R-AM18 單源佐證） |
| 無錨葉 | 0 |
| 交付簿 | `SWQT_AudioMgmt_B1-B5.xlsx`，**300 列**，tc_id `NR1L-AMM-001`–`300` |
| SHA256 | `aa8b78519761124d533460d7494dd6adb04ace6e6df31a89de6f171d6a486382` |

累計 B1–B5：**300 條／249 葉**（318 葉之 **78%**）。

## 二、四關卡之實效（包 20 §四）

本批為四關全備後之首批。三關於第二路各命中一次（023 自引、025 詞形、
040／107 不截斷），**第四關（區段掃描）命中兩次**：

- **168 → 4866594**：關鍵詞零同現為真但非證據（規格用語 `requires HU
  audio`，與 `exclusive/override/emergency` 無交集）。
- **293 → 4866193**：包 20 §二.3 之條件授權由第四關執行。

## 三、SWE1_AMM_293 留置（單件回分析層）

第四關於 1.3.2.10.3.2 段查得 **4866193**：

> `The Gear Position Based strategy for Park Assist and Side Distance volume
> allows the Park Assist system to request a specific chime volume as part of
> the chime request.`

與葉逐項對應。**惟該物件池外**。包 20 §二.3 之授權為「查得**且池內** →
兩路一致逕寫；池外或不明 → 單件回分析層」，故**不逕寫**，本葉留置。

**待裁**：比照其餘池外葉依 R-AM2′／R-AM18 寫入並標單源，或掛 PENDING。
（葉之覆蓋另有一處部分性：「disable user adjustment」在錨文無明文，
係策略之推論，若採寫入建議標部分覆蓋。）

## 四、共錨四組（R-AM16，括號下半逐字不同）

| 組 | 錨 | 分野 |
|---|---|---|
| 021／023 | 4865986 | 021 取「依接收事件型別取參數」、023 取「依所選 alert type 取參數」 |
| 022／281 | 4865984 | 022 取「事件→識別碼對映」、281 取「Alert6–8 保留不指派」 |
| 043／048 | 4866090 | 043 取「換算後送出」、048 取「AMP 端收到」 |
| 292／294 | 4866173 | 292 取「策略明配」、294 取「策略缺席之預設回退」 |
| 283／285 | 4867695 | 283 取「參數缺席」、285 取「值不支援」 |

（實為五組；包 20 §一、§二.2 各新增一組。）

## 五、R-AM21 跨批共錨檢查（出貨前置，本批首次全簿執行）

```
anchors cited            238
cited by more than one    63
of those, across batches   2
  CFTS019-4866286: B4/SWE1_AMM_020, B5/SWE1_AMM_107
  CFTS019-4866727: B1/SWE1_AMM_199, B3/SWE1_AMM_195
→ no shared anchor carries duplicate bracket halves（綠）
```

**4866727（B1/199 與 B3/195）為本次回溯掃描新發現之跨批共錨** ——
兩葉皆引 SOS/TBM 靜音解除之 ELSE 分支，在 R-AM21 之前無任何檢查看得到它。
括號下半不同（199 取「SOS 結束後回復」、195 取「TBM 釋放後指示清除」），
故通過，惟該共用**至今未經申報**，請分析層補認 R-AM16 或另裁。

## 六、本批攔下之檢查缺陷（執行層自身）

**情態詞檢查誤判 `CAN`。** 檢查 B 以 `\bcan\b` 不分大小寫比對，
遂將 **CAN amplified**（匯流排名）之 `CAN` 判為情態動詞 can，
SWE1_AMM_080 因此誤報。已修：比對前先移除全大寫技術詞 `CAN`。
四批回溯複驗仍全綠，無因此被遮蔽之真違規。

（與 A-AM11 系列同族：**詞面相同而語意不同**——此前是 021/023 之
left/right drive vs 左右聲道，此次是 CAN 匯流排 vs can 情態詞。）

## 七、寫回驗證

48 成員不變、僅 `sheet6.xml` 受改、dataValidation classic 3／x14 1 不變、
conditionalFormatting 不變、逐列回讀 50 列全符、
累積 300 列 tc_id 001–300 無重複無缺號。

## 八、池外錨登記表（R-AM18 單源佐證，11 筆）

| 葉 | 錨 | Title | 佐證 |
|---|---|---|---|
| SWE1_AMM_021 | CFTS019-4865986 | Audio Management - Entertainment and | 單源佐證 |
| SWE1_AMM_023 | CFTS019-4865986 | Audio Management - Alert Tone Parame | 單源佐證 |
| SWE1_AMM_279 | CFTS019-4865976 | Audio Management - Confirmation Tone | 單源佐證 |
| SWE1_AMM_282 | CFTS019-4865990 | Audio Management - Alert Sound Selec | 單源佐證 |
| SWE1_AMM_283 | CFTS019-4867695 | Audio Management - Default Sound Fil | 單源佐證 |
| SWE1_AMM_284 | CFTS019-4867696 | Audio Management - Fiat Latam Sound  | 單源佐證 |
| SWE1_AMM_285 | CFTS019-4867695 | Audio Management - Default Sound Fil | 單源佐證 |
| SWE1_AMM_292 | CFTS019-4866173 | Audio Management - Customer Selectab | 單源佐證 |
| SWE1_AMM_294 | CFTS019-4866173 | Audio Management - Default Park Assi | 單源佐證 |
| SWE1_AMM_304 | CFTS019-4866200 | Audio Management - Confirmation Tone | 單源佐證 |
| SWE1_AMM_305 | CFTS019-4866201 | Audio Management - Default Confirmat | 單源佐證 |

## 九、待分析層

1. **293 之處置**（§三）。
2. **4866727 跨批共錨之補認**（§五）。
3. DR-AM3 之理由改寫（A-AM13：圖表論據已作廢，一般性缺漏仍成立）。
4. B6 之下放（Audio Processing 後 16 ＋ Surround and Fade 24 ＋ Power and Persistence 前 10）。
