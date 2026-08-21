# 交付回修計畫 v3（2026-08-21，待 Pei 逐項裁定）

依據：同目錄三份 survey + PM 訊號實測 + test_item 長度/大小寫/CJK
全語料掃描。通則不變：xlsx_surgical.py 唯一寫回、一批一上繳、
交付寫回與 DELIVERY.sha256 屬 Pei。

## 先決裁決

- **R-1 訊號記法**：PROXI `$X$`／內部 `X.Info`／CAN 三件組
  `<Signal> in <MESSAGE> on <segment>`。 ☐
- **R-2 spec_reference**：家族分流、一文件一行、`, ` 續列、禁 `;`、
  檔名底線化、短號不作錨。 ☐
- **R-3 test_item 長度**：上半 verbatim 摘句以「與括號目的直接相關
  之句」為限；≥2 完整句或 >50 字（提案值，據 Media 分佈 P100=30）
  須摘句並以 spec_reference 指回全文。閾值待裁：☐50 ☐其他___
- **R-4 verbatim 首字正規化**：摘句自原文中段起抄時，句首字母轉
  大寫屬排版正規化，允許（Projection 429–432 "if..."、PM 20/204
  "the R1 HU..." 型即合法化為轉大寫後保留）。 ☐
- **R-5 雙語制存廢**：BT（中文 AC+英譯並列，436 列）、Projection
  （英文+簡中對照，648 列）為制度性格式。
  ☐立 profile [OVERRIDE] 合法化（僅 lint 豁免，不回修）
  ☐去中文化回修（工程量最大項）
  無論何者：UI 標籤簡中 verbatim（"适配器" 型）一律豁免；
  工作備註中文（HFP row75 型）一律移出交付欄。

## 回修項目

| # | 對象 | 列數 | 缺陷 | 前置 | 裁定 |
|---|---|---|---|---|---|
| M1 | BT | 275 | PC powered-on（§8.5 逐列判 FULL OPERATION） | — | ☐ |
| M2a | Home | 216 | Test Set 整欄空（先簽 Layer 2） | 框架 | ☐ |
| M2b | BT159–184 + HFP29 + Proj1 | 46 | 殘缺列整列重建：Test Set+author+中文proc+小寫，一次補齊 | R-5 | ☐ |
| M3 | PM | 105 | 訊號記法混雜；網段自 DBC 實查 | R-1 | ☐ |
| M4 | DealerMode | 120 | 方括號→`"X"` | — | ☐ |
| M5 | DM16+HFP18 | 34 | ER shall/will；引號內原文豁免 | — | ☐ |
| M6 | AMFM | 30 | Wilson check whether→check that；先知會 | 知會 | ☐ |
| M7 | AMFM32+PU8+短號12 | 52 | spec_ref 正規化 | R-2 | ☐ |
| M8 | HFP5+Proj5+DM6 | 16 | 步驟/ER 不對齊、模糊詞 | — | ☐ |
| M9 | AMFM | 154 | test_item 缺括號下半（row87–90 sibling 同文） | S4 | ☐併M6 |
| M10 | BT375+Proj91+PM71+AMFM29+Home17（極端 Home r135 415字整表） | 583 | test_item 過長/多句/表格傾倒 → 依 R-3 摘句 | R-3 | ☐ |
| M11 | 全語料 | ~24 | 首字小寫真違規（豁免技術token/引號後）；verbatim 型依 R-4 轉大寫 | R-4 | ☐ |
| M12 | HFP 7 型列 | ~15 | 工作備註中文洩入 test_item/proc → 移 Remarks | — | ☐ |

## 批次順序（提案）

R-1~R-5 + S4~S6 裁定回寫 → M1 → M2b → M4+M5+M8+M11+M12（小批合併）
→ M7 → M3 → M6+M9（AMFM 一批，知會後）→ M10（量大、需 R-3）→
M2a（需框架，最後）。若 R-5 裁去中文化，另立 M13 排最末。

## 配套

- S1 09_ 舊規標 superseded ☐  S2 canon §10.7/§11 收斂 ☐
- S3 lint 出貨 gate：A/B/D/G + I(括號下半) + J(首字大寫含豁免表)
  + K(CJK 依 R-5 配置) + L(長度 R-3 閾值) ☐
- S4 括號下半條文 ☐  S5 裁決台帳+上限3+[DEFAULT] ☐
- S6 缺件 PENDING 佔位制 ☐
