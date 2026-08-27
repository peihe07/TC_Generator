# COVERAGE_GAPS — Bed Lowering Mode

R-BLM2 之 coverage gap disclosure table。落檔依下放包 13 §三。

**本表之意義**：下列 leaf 已收錄於覆蓋台帳，但**不生成 TC** —— 其驗證屬設計審查或
實車量測，非 SWE.6 層之 HMI 可觀察行為。**不生成不等於不驗**，只是不由本工作簿承載。

**與 PENDING 之區別**：PENDING 是「驗得了但缺一份文件」（生成 TC 而不出貨，見 DATA_REQUESTS.md）；
本表是「SWE.6 層驗不了」（不生成 TC）。兩者混談會把「缺一份文件」講成「這件事驗不了」。

母體 176 leaf；生成 163、本表 13，合計 176，未歸屬 0（上繳 13 §二之機器對帳）。

| leaf id | 037 原文摘句 | 不生成之理由 | 建議驗證方式 |
|---|---|---|---|
| `SWE1-HMI-BLM-013-04` | The system shall ensure daytime visibility of Bed Lowering related display content from a comfortable driving posture. | 實車駕駛姿態下之可視性 —— 需人因姿態量測，非 HMI 可觀察行為 | 設計審查（實車人因姿態評估） |
| `SWE1-HMI-BLM-013-05` | The system shall ensure daytime visibility of Bed Lowering related display content without requiring the driver to lean. | 「不需前傾」為人因姿態判準，需實車包裝量測 | 設計審查（實車人因姿態評估） |
| `SWE1-HMI-BLM-013-06` | The system shall ensure daytime visibility of Bed Lowering related display content without requiring the driver to bend. | 「不需彎腰」為人因姿態判準，需實車包裝量測 | 設計審查（實車人因姿態評估） |
| `SWE1-HMI-BLM-013-07` | The system shall ensure daytime visibility of Bed Lowering related display content without requiring the driver to twist. | 「不需扭身」為人因姿態判準，需實車包裝量測 | 設計審查（實車人因姿態評估） |
| `SWE1-HMI-BLM-014-04` | The system shall ensure nighttime visibility of Bed Lowering related display content from a comfortable driving posture. | 同 013-04，夜間條件 | 設計審查（實車人因姿態評估，夜間） |
| `SWE1-HMI-BLM-014-05` | The system shall ensure nighttime visibility of Bed Lowering related display content without requiring the driver to lean. | 同 013-05，夜間條件 | 設計審查（實車人因姿態評估，夜間） |
| `SWE1-HMI-BLM-014-06` | The system shall ensure nighttime visibility of Bed Lowering related display content without requiring the driver to bend. | 同 013-06，夜間條件 | 設計審查（實車人因姿態評估，夜間） |
| `SWE1-HMI-BLM-014-07` | The system shall ensure nighttime visibility of Bed Lowering related display content without requiring the driver to twist. | 同 013-07，夜間條件 | 設計審查（實車人因姿態評估，夜間） |
| `SWE1-HMI-BLM-017-01` | The system shall position the Bed Lowering HMI touch target so that adequate hand clearance is provided at the head unit. | 手部淨空為實車包裝量測，非 HMI 行為 | 實車量測（手部觸及包裝／人體計測試驗） |
| `SWE1-HMI-BLM-017-02` | The system shall position the Bed Lowering HMI touch target so that adequate finger clearance is provided at the head unit. | 手指淨空為實車包裝量測，非 HMI 行為 | 實車量測（手部觸及包裝／人體計測試驗） |
| `SWE1-HMI-BLM-017-03` | The system shall support Bed Lowering HMI access for users from 5th percentile female anthropometry with gloves. | 5th percentile 女性人體計測（含手套），需人因試驗 | 實車量測（手部觸及包裝／人體計測試驗） |
| `SWE1-HMI-BLM-017-04` | The system shall support Bed Lowering HMI access for users up to 95th percentile male anthropometry with gloves. | 95th percentile 男性人體計測（含手套），需人因試驗 | 實車量測（手部觸及包裝／人體計測試驗） |
| `SWE1-HMI-BLM-017-05` | The system shall implement Bed Lowering HMI hand-access packaging in compliance with HMI_BP_X-01_Hand_Anthropometry_A.Mar-6-2013. | 手部觸及包裝之指引符合性，屬實車包裝設計驗證 | 實車量測（手部觸及包裝／人體計測試驗） |

## 判準與其模稜之處

二分判準（R-BLM2）：**可功能化改寫為 HMI 可觀察行為者生成；純設計驗證性質者不生成。**
逐條理由見上表第三欄。下列兩點為判準套用時之模稜處，依下放包 13 §三
「寧可揭露過多，不可默默吸收」一併揭露：

1. **`017-05`（手部觸及包裝符合 HMI_BP_X-01）判為 gap，而形態相近的 `016-04`／`016-05`／
   `023-01`／`023-02`（符合 W-01／L-34）判為 PENDING。** 四者都是「符合某份 HMI_BP 指引」，
   分開的理由是驗證對象不同：016／023 驗螢幕上的文案與軟鍵外觀，指引到手即可目視比對；
   017-05 驗實車手部包裝，指引到手仍需人因試驗。**此一分界為執行層之判斷，非 037 明載。**
2. **`013-01`～`03`／`014-01`～`03` 判為可生成，而同母號之 `-04`～`-07` 判為 gap。**
   前者只說「日／夜條件下可見」，可於台架以環境光設定觀察；
   後者附加「從舒適駕駛姿態」「不需前傾／彎腰／扭身」，那是姿態判準。
   **同一母號之下拆兩邊，界線落在原文有無姿態語彙。**

## 未列入本表者

`023-01`／`023-02` 雖屬人因群母號範圍，但驗的是軟鍵行為與外觀（HMI 可觀察），
故生成 TC 並以 DR-4 之 PENDING 承接，**不入本表**。
