# G180 —— `GLUED_OR_RE` 之大小寫敏感度查明（R-P258）

> **本檔只查不改**（R-P258(c) / §I）。返工面估出後於 38 包裁定。

## 一、`GLUED_OR_RE` 於文字層之組成

現行定義：`(?<=[a-z0-9\"'])(OR|NOR)(?=[A-Z(\"' ])`

| 項 | 數 |
|---|---|
| 現行命中（區分大小寫） | **2** |
| 加 `re.I` 後之**增量** | **2406** |
| 　其中 `OR` / `NOR` 為大寫者 | 80 |
| 　**左鄰為字母 → 某單詞之字尾（誤命中）** | **2406** |
| 　**左鄰為引號或數字 → 可能之真黏連 OR** | **0** |

**判定**：增量 2406 個中，**2406 個之左鄰為字母**，即 `DOORS` / `NORMAL` / `U_APPLICATION_LOW_TO_NORMAL` / `SWITCH_OFF_DOOR` / `FOR` 之字尾 —— **誤命中**。
可能之真黏連 OR：**0 個**。

**大寫增量為 0 —— 即 `re.I` 所增之 2406 全為小寫 `or` / `nor`，與『黏連之大寫 OR』無關。**
**故 `GLUED_OR_RE` 未漏檢真黏連 OR，G113 自 23 包起之結論不因本項而須重估。**

**預估返工面：0 條。**

## 二、增量之語境樣本（前 30）

| 命中 | 語境 |
|---|---|
| `or` | ```` Requirement Specification Report R1LR_Atl-H_25PI3.5_Acti` |
| `or` | `to any third party without the prior written permission of Ste` |
| `OR` | `ESET MODE {4941069}13 1.3.1.11.3 NORMAL OPERATION MODE GROUP {` |
| `or` | `}13 1.3.1.12 Asynchronous CAN network operation {4941085}14 1.` |
| `or` | `operation {4941085}14 1.3.1.13 Error handling {4941087}14 1.3.` |
| `or` | `al Sleep and Wakeup Requirements for CAN-I {4941205}26 1.3.3.3` |
| `or` | `41213}26 1.3.3.3.4 HU Wakeup By Door Lock/Unlock {4941215}27 1` |
| `or` | ``` **Requirement Specification Report** **R1LR_Atl-H_25PI3.5_` |
| `or` | `to any third party without the prior written permission of Ste` |
| `OR` | `ESET MODE {4941069}13 1.3.1.11.3 NORMAL OPERATION MODE GROUP {` |
| `or` | `}13 1.3.1.12 Asynchronous CAN network operation {4941085}14 1.` |
| `or` | `operation {4941085}14 1.3.1.13 Error handling {4941087}14 1.3.` |
| `or` | `al Sleep and Wakeup Requirements for CAN-I {4941205}26 1.3.3.3` |
| `or` | `41213}26 1.3.3.3.4 HU Wakeup By Door Lock/Unlock {4941215}27 1` |
| `or` | ```` Requirement Specification Report R1LR_Atl-H_25PI3.5_Acti` |
| `or` | `to any third party without the prior written permission of Ste` |
| `or` | `0094" 1.4.1.1 Voltage Level Behavior {4942203} PAGEREF _Toc25` |
| `or` | `000095" 1.4.1.2 Low Voltage Behavior {4942207} PAGEREF _Toc25` |
| `or` | `00099" 1.4.1.3 High Voltage Behavior {4942223} PAGEREF _Toc25` |
| `or` | `System Voltage Out-Of-Range Behavior for Different Modes {4942` |
| `or` | `em Voltage Out-Of-Range Behavior for Different Modes {4942251}` |
| `or` | `1" 1.4.1.5 High temperature Behavior {4942256} PAGEREF _Toc25` |
| `or` | ``` **Requirement Specification Report** **R1LR_Atl-H_25PI3.5_` |
| `or` | `to any third party without the prior written permission of Ste` |
| `or` | `0094" 1.4.1.1 Voltage Level Behavior {4942203} PAGEREF _Toc25` |
| `or` | `000095" 1.4.1.2 Low Voltage Behavior {4942207} PAGEREF _Toc25` |
| `or` | `00099" 1.4.1.3 High Voltage Behavior {4942223} PAGEREF _Toc25` |
| `or` | `System Voltage Out-Of-Range Behavior for Different Modes {4942` |
| `or` | `em Voltage Out-Of-Range Behavior for Different Modes {4942251}` |
| `or` | `1" 1.4.1.5 High temperature Behavior {4942256} PAGEREF _Toc25` |

## 三、其餘大小寫敏感謂詞之增量（R-P258(d)）—— 9 個

| 模組.謂詞 | 語料 | 現行 | 加 `re.I` | 增幅 | 該謂詞是否刻意區分大小寫 |
|---|---|---|---|---|---|
| `lint_tcs.ER_PROPER_RE` | 文字層 | 31324 | 128707 | **+97383** | **是** —— 以大寫辨識具名標的；加 `re.I` 將吞下全部普通英文字 |
| `audit_precond_state.MODE_RE` | 文字層 | 12538 | 69022 | **+56484** | **是** —— 狀態名為專有名詞（`Standby` / `Sleep`） |
| `build_template_diff.COL_RE` | 文字層 | 96746 | 151772 | **+55026** | 待判 —— 表格欄位擷取，非語義判準 |
| `reverse_coverage.NAMED_RE` | 文字層 | 37005 | 69327 | **+32322** | **是** —— 同上（透鏡 2 之具名標的） |
| `build_residual_sample.GLUE_RE` | 文字層 | 130 | 7022 | **+6892** | 待判 —— 殘差詞黏連偵測，與 `GLUED_OR_RE` 同型 |
| `reverse_coverage.SPLIT_RE` | 文字層 | 5103 | 5842 | **+739** | **是** —— 條件子句起首詞於句首方為子句起首 |
| `lint_tcs.SPEC_PARAM_RE` | 文字層 | 5246 | 5286 | **+40** | **是** —— 規格參數名之大小寫具意義 |
| `or_branch_coverage.OR_TOKEN_RE` | 文字層 | 956 | 958 | **+2** | **是** —— 已明列 `OR|or|NOR|nor` 四形，加 `re.I` 之增量為冗餘 |
| `build_swepm025_triggers.TRIGGER_RE` | 文字層 | 43 | 44 | **+1** | 待判 |
