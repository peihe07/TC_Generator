# b1_epb — pilot 產出索引（EPB Maintenance Mode）

## **b1 FROZEN (R-VL23)** — 2026-09-02
## **-057 amended per R-VL26(a); refrozen** — 2026-09-02

凍結後任何變更**須新裁決**（R-VL23(d)）。`-057` 之括號下半依 R-VL26(a) 解凍修一列後**重新凍結**，
其餘 16 條一位元未動。凍結時之狀態：
- req_id（＝leaf）：**17**　TC 總數：**17**　檔數：**35**
- PENDING 項：**6**（錨 DR-VL4）
- E38–E45／E53–E56 重跑：**全過**（E56 = 17／17、hedge = 0）
- **已寫回** `sandbox/b1/vsm42_b1.xlsx`（下放包 12）；交付候選 `candidate_vsm42_b1.xlsx`（sha256 相等）
- lint 實跑：C=0／P 對銷後淨紅 **0**／U=6（計數）／I-cross=17（窗未宣告基線型）／其餘 0

生成 05 ／ 修訂 06（REV-1／2／4）／ 微修 07（R-VL22）／ 收尾 08（R-VL23 A 路）／ **-057 修訂 12（R-VL26(a)）**。

**族內一致選擇（R-VL21(f)）**：Fdbk 族之回讀步一律削去，無例外。
**歸類（R-VL22(c)）**：`-048`〜`-052` 進入側；`-055`〜`-057` 退出側；**`-054` in-mode 狀態回報型**。

| req_id | 工作簿列 | TC ID | D 欄 | 修訂輪 | tc_title | prio | design_method | PEND |
|---|---|---|---|---|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-044` | 10 | `NR1L-VSM42-001` | `SWE1-VC-EPBMaintenanceMode-044` | — | EPB Maintenance Mode menu hidden when PROXI is Absent | P2 | 負向測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-045` | 11 | `NR1L-VSM42-002` | `SWE1-VC-EPBMaintenanceMode-045` | — | EPB Maintenance Mode menu shown when PROXI is Present | P2 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-046` | 12 | `NR1L-VSM42-003` | `SWE1-VC-EPBMaintenanceMode-046` | 06+07 | EPB Maintenance Mode enabled from HMI → request sent and Initializing popup shown | P1 | 功能測試 | 0 |
| `SWE1-VC-EPBMaintenanceMode-047` | 13 | `NR1L-VSM42-004` | `SWE1-VC-EPBMaintenanceMode-047` | — | IPC EPB_MaintenanceMode Off → On | P1 | 狀態轉換 | 0 |
| `SWE1-VC-EPBMaintenanceMode-048` | 14 | `NR1L-VSM42-005` | `SWE1-VC-EPBMaintenanceMode-048` | 06 | EPB Maintenance feedback = 2: Vehicle speed is not 0 mph | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-049` | 15 | `NR1L-VSM42-006` | `SWE1-VC-EPBMaintenanceMode-049` | 06 | EPB Maintenance feedback = 3: Vehicle is not in Park or Neutral | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-050` | 16 | `NR1L-VSM42-007` | `SWE1-VC-EPBMaintenanceMode-050` | 06 | EPB Maintenance feedback = 4: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-051` | 17 | `NR1L-VSM42-008` | `SWE1-VC-EPBMaintenanceMode-051` | 06 | EPB Maintenance feedback = 5: EPB switch is currently engaged | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-052` | 18 | `NR1L-VSM42-009` | `SWE1-VC-EPBMaintenanceMode-052` | 06 | EPB Maintenance feedback = 6: Brake pedal is currently pressed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-053` | 19 | `NR1L-VSM42-010` | `SWE1-VC-EPBMaintenanceMode-053` | 07 | No IPC response before T_EPB_MM expires | P1 | 基礎故障注入 | 0 |
| `SWE1-VC-EPBMaintenanceMode-054` | 20 | `NR1L-VSM42-011` | `SWE1-VC-EPBMaintenanceMode-054` | 06+07 | EPB Maintenance feedback = 8: park brake retracted | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-055` | 21 | `NR1L-VSM42-012` | `SWE1-VC-EPBMaintenanceMode-055` | 06 | EPB Maintenance feedback = 9: vehicle speed not zero on exit | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-056` | 22 | `NR1L-VSM42-013` | `SWE1-VC-EPBMaintenanceMode-056` | 06 | EPB Maintenance feedback = 10: exit blocked while vehicle in motion | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-057` | 23 | `NR1L-VSM42-014` | `SWE1-VC-EPBMaintenanceMode-057` | 06+**12** | EPB Maintenance feedback = 11: exit process completed | P2 | 等價劃分 | 0 |
| `SWE1-VC-EPBMaintenanceMode-058` | 24 | `NR1L-VSM42-015` | `SWE1-VC-EPBMaintenanceMode-058` | — | EPB Maintenance Mode active state forwarded to the display controller | P2 | 功能測試 | 2 |
| `SWE1-VC-EPBMaintenanceMode-059` | 25 | `NR1L-VSM42-016` | `SWE1-VC-EPBMaintenanceMode-059` | 08 | Vehicle speed crosses V_Car_Moving upward | P1 | 邊界值分析 | 2 |
| `SWE1-VC-EPBMaintenanceMode-060` | 26 | `NR1L-VSM42-017` | `SWE1-VC-EPBMaintenanceMode-060` | — | Vehicle Setup menu updated on EPB_MaintenanceMode message reception | P2 | 狀態轉換 | 2 |

## 凍結檔表（sha256 前 8 碼，`-057` 為修訂後之新值）

| 檔 | sha256[:8] |
|---|---|
| `SWE1-VC-EPBMaintenanceMode-044.json` | `02e1fb74` |
| `SWE1-VC-EPBMaintenanceMode-044.md` | `8e19a191` |
| `SWE1-VC-EPBMaintenanceMode-045.json` | `843fb429` |
| `SWE1-VC-EPBMaintenanceMode-045.md` | `e9ec541a` |
| `SWE1-VC-EPBMaintenanceMode-046.json` | `82091592` |
| `SWE1-VC-EPBMaintenanceMode-046.md` | `4f37e562` |
| `SWE1-VC-EPBMaintenanceMode-047.json` | `b112d9ba` |
| `SWE1-VC-EPBMaintenanceMode-047.md` | `112bb083` |
| `SWE1-VC-EPBMaintenanceMode-048.json` | `3b4303a1` |
| `SWE1-VC-EPBMaintenanceMode-048.md` | `268ebed7` |
| `SWE1-VC-EPBMaintenanceMode-049.json` | `e46408e1` |
| `SWE1-VC-EPBMaintenanceMode-049.md` | `4cb8d533` |
| `SWE1-VC-EPBMaintenanceMode-050.json` | `17114b92` |
| `SWE1-VC-EPBMaintenanceMode-050.md` | `1fe69be7` |
| `SWE1-VC-EPBMaintenanceMode-051.json` | `94dd9fed` |
| `SWE1-VC-EPBMaintenanceMode-051.md` | `bca8f736` |
| `SWE1-VC-EPBMaintenanceMode-052.json` | `0cb58c48` |
| `SWE1-VC-EPBMaintenanceMode-052.md` | `ae373d51` |
| `SWE1-VC-EPBMaintenanceMode-053.json` | `e87ffd3b` |
| `SWE1-VC-EPBMaintenanceMode-053.md` | `aba1ff41` |
| `SWE1-VC-EPBMaintenanceMode-054.json` | `8d23aaea` |
| `SWE1-VC-EPBMaintenanceMode-054.md` | `081104fc` |
| `SWE1-VC-EPBMaintenanceMode-055.json` | `1c573252` |
| `SWE1-VC-EPBMaintenanceMode-055.md` | `c9350796` |
| `SWE1-VC-EPBMaintenanceMode-056.json` | `0fa76d57` |
| `SWE1-VC-EPBMaintenanceMode-056.md` | `70c2038e` |
| `SWE1-VC-EPBMaintenanceMode-057.json` | `72c5b02a` |
| `SWE1-VC-EPBMaintenanceMode-057.md` | `1d0abcd2` |
| `SWE1-VC-EPBMaintenanceMode-058.json` | `a1e0ff42` |
| `SWE1-VC-EPBMaintenanceMode-058.md` | `84d67318` |
| `SWE1-VC-EPBMaintenanceMode-059.json` | `7abc9589` |
| `SWE1-VC-EPBMaintenanceMode-059.md` | `638973e6` |
| `SWE1-VC-EPBMaintenanceMode-060.json` | `ca9ec0a0` |
| `SWE1-VC-EPBMaintenanceMode-060.md` | `86b23ea1` |

> `INDEX.md`（本檔）不入表 —— 其內容含本表，自指。

## 寫回產物（下放包 12）

| 檔 | sha256 |
|---|---|
| `sandbox/b1/vsm42_b1.xlsx` | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6` |
| `sandbox/b1/candidate_vsm42_b1.xlsx` | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6`（相等） |

## PENDING 清單

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `SWE1-VC-EPBMaintenanceMode-058` | test_procedure | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-058` | expected_result | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | test_procedure | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-059` | expected_result | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | test_procedure | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |
| `SWE1-VC-EPBMaintenanceMode-060` | expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |

## 凍結時之未結（皆已具名）

§K K-1（Fdbk 2–11 無 `VAL_` label；已由 `data/lint_p_waivers_b1.tsv` 對銷）／K-2（Fdbk 4 與 5 同文）／
K-3（`-059` ignition 分支無合法訊號名）／K-4（規格拼字瑕疵）／K-5（退出側請求路徑規格未載）／
K-6（`-054` 歸屬，已由 R-VL22(c) 量測定案）。DR-VL1／VL2／VL4 皆登記未送出。
