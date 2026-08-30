# 作業 D-1 — `DELIVERY_CHECKLIST.md` 之 ICS 條目逐項對照｜2026-08-30

**本表為交付前之現況對照，非出貨授權。** IN §8.4.3 不變（R-ICS54(a)）。

## §1 逐項對照

| 項 | 現況 | 判 |
|---|---|---|
| TC 總數 | **31** | — |
| Test Set 相異值 | **5**（Volume Control／Browse Control／Display Control／Menu Navigation／Stuck Button）| — |
| 錨行 | **65**（相異 ObjectID 38：CFTS020 31 ＋ CFTS022 7）| — |
| `verify_verbatim` | **31／31** | PASS |
| `selfcheck`（機檢 19 項）| FAIL **0** | PASS |
| `verify_reference_binding` | **11／11 MATCH** | PASS |
| `pending_census` | **6 處／6 條** | **未清空** |
| 母本 sha256 | `6372fb6b…fb825b2`，與 `feature.yaml` 宣告相符 | PASS |
| x14 DV（R10:R1411）| `xlsx_surgical` 實測保留（E43 未觸發）| PASS |
| **TC ID** | **已指派**：`NR1L-ICS-001` ~ `NR1L-ICS-031`（R-ICS56(a)(b)，b19b）| PASS |
| sandbox 工作簿 | `sandbox/v1/ics_management_v1.xlsx`，sha `d31d81d211d11593…` ＋ sidecar | 已產出 |
| 讀回逐字比對 | **403／403 格逐字相同**（31 條 × 13 欄）| PASS |
| zip 結構 | 成員 48／順序／timestamps 與母本一致；僅 `sheet6.xml` 有差 | PASS |
| 工作簿 GUI 驗證 | **未做 —— 屬 Pei 之手動項** | 待 |
| `delivered/` ＋ MANIFEST.tsv | **已產出**（2026-08-30，Pei 令）——`delivered/…_SWQT_ICSManagement_20260830.xlsx` 整檔複製自 `sandbox/v1/`，`cmp` 逐位元組一致，sha `d31d81d2…2ddea` 不變 | PASS |
| `lint_docs036` | 既有紅，成因在 `features/power/DATA_REQUESTS.md` | 具名不修 |

## §2 PENDING 6 處及所繫 DR

| # | tc_title | 欄位 | DR | 缺件 |
|---|---|---|---|---|
| 1 | Three detents rotated clock-wise | `pre_conditions` | **DR-ICS4** | `CFTS019 volume level range` |
| 2 | Knob 2 signals acted on by the HU | `pre_conditions` | **DR-ICS6** | `HMI Logic and Flow browse mapping for ICS_KNOB2` |
| 3 | Enter button pressed | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow screen mapping for Enter_Button` |
| 4 | Knob 2 rotated on a scrollable screen | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow scroll mapping for ICS_KNOB2` |
| 5 | Knob 2 rotated on a tuner source | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow tune mapping for ICS_KNOB2` |
| 6 | Back button pressed | `pre_conditions` | DR-ICS6 | `HMI Logic and Flow screen mapping for Back_Button` |

**6 處全部在 `pre_conditions` 欄**；繫於二個 DR：**DR-ICS6（5 處）** 與 **DR-ICS4（1 處）**。
依 R-ICS54(a) **原樣寫入，不降轉、不留白、不臆填**。

## §3 不可出貨之 4 條及所繫 DR

| 標號 | tc_title | 所繫 |
|---|---|---|
| V1 | VOLUME knob rotated clock-wise | **DR-ICS9** |
| V2 | VOLUME knob rotated counter clock-wise | DR-ICS9 |
| V3 | Three detents rotated clock-wise | DR-ICS9 |
| B5 | Three detents counted in one rotation | **DR-ICS2** |

**其中 V1／V2 無任何佔位**（V3 之 1 處佔位繫 DR-ICS4，非其阻因；B5 亦無佔位）——
故 `pending_census` 不報、`selfcheck` 全綠。**只有本表與凍結記錄 §2／§3 會提醒。**

**四條依令仍寫入工作簿**（依現狀寫回），**工作簿內不加任何註記**。

## §4 Excel GUI 驗證（**手動項，屬 Pei**）

執行層**未做**，具名如下。已知須以 GUI 確認之項（來自母本結構之實測）：

- R 欄（`Test Case Design Methods`）之 **x14 下拉**於 GUI 中是否仍可展開
  —— `xlsx_surgical` 之 DV 計數檢查只驗數量與 sqref，**不驗 GUI 可用性**；
- P／Q 欄（`P10:Q1411`）、T～Z 欄、AF 欄之 classic 下拉；
- 換行字元於儲存格內之呈現（本 feature 之 `test_procedure`／`expected_result` 皆為多行）；
- 中文表頭與英文內容混排之欄寬與截斷。

## §5 並行寫入對 sha 可信度之影響（R-ICS54(f)）

**本 session 期間 repo 有持續之並行寫入**，實證三項：

1. `canon_refs` 之計數於本 session 內由 **445 → 446 → 459 → 460 → 473 → 478**，
   而**執行層每輪之新檔於其 unresolved／ambiguous 報表中皆 0 命中**（b16／b17／b18 各驗一次）；
2. 掃描檔數由 **2523 → 2574**；
3. 分析層五簿之數輪變更於 `git status` 中已不顯示為未提交，
   表示**由並行 session 先行提交**（b17／b18 之 commit 均具名此事）。

**含意**：作業 C 產出之工作簿 sha256，**只在產出當下對其自身有效**；
它不保證「產出時 repo 之其他部分」與 tag 時相同。
**`verify_reference_binding` 之 11／11 是對 11 個參考件之保證，不是對 repo 全域之保證。**

**建議**（不裁）：`--write` 與 tag 之間若相隔任何時間，**tag 前應重跑一次 `verify_reference_binding`**。

---

## §6 b19b 之增列（R-ICS55(h)、A-ICS135／136）

1. **`tc_id` 已指派**：`NR1L-ICS-001` ~ `NR1L-ICS-031`，依工作簿列序連續、無重號無缺號。
   前綴取 `NR1L`（R-ICS56 普查：占 609／783 列、3／5 本）。**欄 E（TestRail）留空**（R-ICS55(d)）。
2. **tag 前須重跑 `verify_reference_binding`**（R-ICS55(h)）——
   本包完工時為 11／11，但該保證只在當下有效。
3. **工作簿 sha 之可信度受並行寫入影響**（A-ICS135／136）：
   `d31d81d211d11593cfbc6878e89fb87b3f9fcf3cbf33621a761857f4b2e2ddea` 只對該檔自身有效；
   它**不保證 repo 其他部分於 tag 時與產出時相同**。本 session 內 `canon_refs` 由 445 升至 486、
   掃描檔數 2523 → 2591 即為並行寫入之規模實證。
4. **`--write` 與 tag 屬 Pei**；本包**未複製入 `delivered/`**，`delivered/` 未動。

---

## §7 交付複製之執行（2026-08-30，Pei 令「確認了 寫回吧」）

§6 第 4 項所述「`delivered/` 未動」為 b19b 完工當下之狀態記錄，**現已由 Pei 令解除**。

| 項 | 實測 |
|---|---|
| `verify_reference_binding`（tag 前重驗，R-ICS55(h)）| **11／11 MATCH**，exit 0 |
| sandbox 工作簿 sha 自檢 | `shasum -c` **OK**，檔案自產出後未改動 |
| 複製 | `sandbox/v1/ics_management_v1.xlsx` → `delivered/…_SWQT_ICSManagement_20260830.xlsx` |
| 交付檔名 | 依 **R-ICS57(a)(b)(c)** 更名；sandbox 作業名不得作交付名（R-ICS57(d)）|
| 逐位元組比對 | `cmp` **一致** |
| 交付件 sha256 | `d31d81d211d11593cfbc6878e89fb87b3f9fcf3cbf33621a761857f4b2e2ddea`（與 sandbox 同）|
| `MANIFEST.tsv` | 5 欄一列，依 `features/power/delivered/MANIFEST.tsv` 之格式 |

**仍未做，且未因本次交付複製而改變**：

1. **Excel GUI 驗證**（§4 所列各項）—— 屬 Pei 之手動項，執行層未做；
2. **不可出貨之 4 條**（V1／V2／V3 繫 DR-ICS9、B5 繫 DR-ICS2）**仍在工作簿內**，
   依 R-ICS54(a) 以現狀寫入、簿內不加註記。**本次複製不構成對該 4 條之出貨授權**；
   IN §8.4.3 不變。已於 `MANIFEST.tsv` 之 `note` 欄具名。
3. **6 處 PENDING**（`pre_conditions` 欄，DR-ICS6 五處、DR-ICS4 一處）原樣保留。
4. **git commit 與 tag 屬 Pei**，執行層未執行。

### §7-1 檔名之更正（具名）

首次複製時執行層以 `features/power/delivered/pm_29.xlsx` 為前例，
將交付本命名為 `ics_management_v1.xlsx` —— **該推定錯誤**，
`pm_29.xlsx` 本身即為 sandbox 作業名，不合語料之交付命名慣例
（`inputs/` 五本實測：`_SWQT_PowerManagement_20260816`／`_SWQT_SXM_20260810` 等）。

成因：`docs/fw036/REMEDIATION_DELIVERY_MGMT_20260821.md` §版次命名
自 2026-08-21 起標「待 Pei 裁定一制」，選項框九日未勾 ——
**執行層未查該節即以前例推定**。經 Pei 直接裁定落 **R-ICS57**，
檔案於 commit 前更名，sha 不變（`cmp` 複驗逐位元組一致）。
