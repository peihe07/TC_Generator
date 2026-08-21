# 交付語料 vs 撰寫規則 遵循度實測（2026-08-21）

量測條件：7 本已交付 036 全列（2,489 rows），對
`09_作業流程與單位規範/02_TC Design Flow & Standard/
ASPICE_SWE6_Test_Case_Writing_Rules_v2.md`（= 現行 canon 上游母版）
之機器可判條文跑 8 項 lint；命中皆經人工抽樣核實。

## 違規分佈（列數 / 佔比）

| 工作簿 | A 禁用動詞 | B ER情態詞 | D PC違規 | F 方括號 | G TestSet空 |
|---|---|---|---|---|---|
| DealerMode 0417 | 6 | 16 | 6 | **120/125** | 0 |
| HFP 0316 | 4 | 19* | 18 | 2 | 29 |
| Media 0625 | 0 | 0 | 0 | 0 | 0 |
| Projection 0623 | 4 | 0 | 20 | 1 | 1 |
| BT 0729 | 4 | 0 | **275/436** | 15 | 8 |
| Home 0809 | 0 | 1 | 2 | 0 | **216/216** |
| AMFM 0810 | **30**(Wilson) | 0 | 8 | 10(Pei) | 0 |

*HFP 之 B 含少數引號內 UI 原文（"...will not be added..."），屬合法引用，
實際違規略低於帳面。

## 三類成因（非同一種「不認真」）

1. **系統性單點遺漏**（影響最大、最易修）
   - BT：275 列 PC 首行 `HU is powered on and in FULL OPERATION MODE` /
     `...adb shell is accessible` — v2 §2.1 明禁之系統預設狀態
   - Home：Test Set 欄整本空白（Arif 144 + Pei 72），§4.1/§4.2 整章
     未執行；對照 Media 602/602 全填、12 個 distinct Test Set
2. **規則換版殘留**（舊制合法、新制違規）
   - 方括號 `[Screen Off]`：v2 自身範例即用方括號；canon §11 改
     `"..."`。DealerMode(4月) 120 列屬舊制交付，非作者失誤
   - 步驟尾句號：v2 範例帶尾句號；canon §11 禁止 — 同型衝突
3. **個人書寫習慣**
   - Wilson（AMFM done 區 30 列）：`...and check whether the item...`
     作主動詞 — v2 §4.5.1 / canon §5.1 禁用
   - DealerMode/HFP ER 直抄需求語 `shall include:` / `shall jump` —
     v2 §5.4 / canon §6 禁止

## 判定

- v2 與 canon 有兩處實質衝突（方括號、尾句號），舊規目錄文件
  未標 superseded → 兩套規則並存是「感覺偏軌」的第二根因
  （第一根因見 SPECREF_SURVEY_20260821.md）
- Media 0625 全項清零，證明 pipeline + canon 嚴格執行時可達標；
  偏離集中於人工撰寫區與早期交付

## 待 Pei 裁定

1. 已交付本是否回修（BT powered-on 275 列、Home Test Set 216 列
   為最高價值目標）；回修屬交付變更，全屬 Pei
2. 09_ 目錄 v2 等舊規文件處置：標 superseded 指向 canon，或先收斂
   方括號/尾句號差異
3. lint A/B/D/G 四項是否納入 pipeline 出貨前檢查
