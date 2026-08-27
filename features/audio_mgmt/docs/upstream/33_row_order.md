# Audio Management — 上繳包 33：列序依 req_id 重排、tc_id 重編

- 日期：2026-08-27
- 依據：Comfort 96 §1（Pei 裁定，列序依 leaf id 遞增）＋ Pei 2026-08-27 裁 (b)
- 狀態：**已寫回並驗畢。** 交付簿 `req_id` 與 `tc_id` 兩欄同時遞增。

---

## 一、缺失之由來（先講清楚，這是執行層之漏）

Comfort 96 §1 之裁定早已存在，且已在 `features/user_profiles/feature.yaml`
落為 `row_order: {value: req_id, applied: true}`，並抽為參數「改值不改程式」。

**但它只活在 user_profiles 一個 feature 裡。** 實測全 repo：

| feature | write_back 有排序邏輯 | `feature.yaml` 有 `row_order` |
|---|---|---|
| user_profiles | ✓ | ✓ |
| time_management | ✗ | ✗ |
| power_moding | ✗ | ✗ |
| audio_mgmt（本件） | ✗ | ✗ |

本 repo 每個 feature 各持一份 `write_back.py`；audio_mgmt 這份移植自
time_management，而 TM 本無此鍵——**整條裁定隨移植掉失**。audio_mgmt 之列序
遂為生成序（批內依 test set 分組、批間 B1→B7 累加），369 列**有 39 處遞減**。

**無任何下放包提過列序，執行層亦未問。** user_profiles profile §5.1 寫著
「一個沒有被任何程式讀取的設定值，會一直看起來像是決定過的」——此處更甚：
連宣告都沒有，所以沒有任何東西會察覺它缺席。**責在執行層。**

## 二、處置（Pei 裁 (b)）

| 項 | 內容 |
|---|---|
| 列序 | 依 `req_id` 數值遞增；同葉多條保持原撰寫序（stable），該序即 sibling 分野之論證序 |
| `tc_id` | **全數重編** `NR1L-AMM-001`–`369`，使 D 欄與 F 欄同時遞增 |
| 影響 | **369 條全部換號** |
| 對照表 | `data/tc_id_remap.tsv`（`old_tc_id / new_tc_id / req_id / batch`，369 列） |

### 2.1 重建之前置閘

列內容自 `generated/B*.json` 重建，故先驗 JSON 與簿**逐格相等**
（369 列 × 12 交付欄，**差異 0**）才動手。若源已飄移而逕行重建，
會把飄移連同一起洗掉且不留痕。

## 三、驗證

| 檢項 | 值 |
|---|---|
| surgical_save | 48 成員、patched `sheet6.xml` |
| dataValidation（classic, x14） | sheet6 (3, 1) 不變 |
| conditionalFormatting | 不變 |
| 列數 | 369 |
| **D 欄 `req_id`** | 遞減 **0 處**（原 39） |
| **F 欄 `tc_id`** | 嚴格遞增、連續、唯一 369、無缺號 |
| 唯一 SWE ID | 317，差集 0 |
| N 欄 | PENDING 0、空白 0、`NA` 3 |
| **新 SHA256** | `3cdd14dec754d6e46a88800e17c50eeda3634041ae8c8a91e89c856b035de9cd` |

四閘複跑：自檢 ×7 pass、lint ×7 green、葉集 ×7 ok、R-AM21 green。

## 四、防止再漏（宣告 ＋ 讀者）

1. **宣告**：`feature.yaml` `write_back.row_order` 依 user_profiles 之
   `{value, applied, why}` 形制落檔，並記此條掉失之經過。
2. **讀者**：`scripts/write_back.py` 新增 **WB-ORDER** 閘——
   - `row_order` 未宣告即 **raise**（列序是交付屬性，不得任由批次執行序決定）；
   - `applied: false` 則跳過而非失敗（那是決定，不是缺陷）；
   - `applied: true` 則驗簿上 `req_id` 非遞減且 `tc_id` 連續。

   **一條沒有讀者的規則，與沒有規則無法區分。** 宣告與閘須成對，缺一即等於無。

## 五、歷史包不回改

包 03–32 所具名之 `tc_id` 為**當時之交付事實**，不予改寫——改了就看不出交付曾是何貌。
現況之唯一權威為 `DELIVERY_NOTE.md`＋本包＋`data/tc_id_remap.tsv`。

## 六、跨 feature 建議（不擅動他人 feature）

time_management、power_moding 之交付簿同樣未依 `req_id` 排序，且其
`feature.yaml` 亦無 `row_order`。**是否回溯更正，屬 Pei 之裁定**，本包僅揭露。
