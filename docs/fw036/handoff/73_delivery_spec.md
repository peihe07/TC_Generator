# 下放包 73 — 全域：交付規格表 R-G42 之讀者（DELIVERY-SPEC 閘）

日期：2026-08-30
取號：落檔當下 `list_directory` 實測 `docs/fw036/handoff/` 止於 72，取 73
依據：R-G42（Pei 2026-08-30 裁「NR1L、全名」「不要再回歸，請寫下規則」）。
性質：**分析層直寫**（Pei：「你直接幫我寫回不用執行層」）。不改任何已交付簿、不搬任何檔。
本包不設執行層工單；留給 Pei 之事項見 §四。

---

## 一、已落檔（分析層直寫，逐檔 get_file_info 驗過）

| 檔 | 動作 | 大小 |
|---|---|---|
| `scripts/lint_delivery_spec.py` | 新建。R-G42 一～七逐項判；`--gate`／`--emit-baseline`；只掃 `features/*/delivered/*.xlsx`，跳過 `~$` 鎖檔 | 13,344 B |
| `tests/test_lint_delivery_spec.py` | 新建。16 項 pytest：1 正向（全合規零紅）＋ 15 反向（逐項破壞恰命中該項）＋ 基線豁免／`--gate` 退出碼。分析層沙箱實跑 **16 passed** | — |
| `scripts/gate_all.py` | 接入 `lint_delivery_spec --gate` 為第六支 | — |
| `scripts/gates_tsv.py` | 新增 `DELIVERY_CHECKS`／`delivery_gate_rows()`，插於 docs 閘之後、feature 閘之前 | — |
| `docs/runtime/GATES.tsv` | 手插 `delivery_spec` 一列，**與 `gates_tsv.py` 之生成字串逐字相同**（分析層以生成函式產出該列再貼入） | — |
| `docs/fw036/DELIVERY_SPEC_BASELINE.tsv` | 基線 4 檔：ICS `…20260830.xlsx`、power `pm_29.xlsx`／`pm_73.xlsx`、sw_update `…20260830.xlsx`（2026-08-30 實測 `delivered/` 內全部 xlsx） | — |

閘之判準與 R-G42 條文之對應：

| 項 | 判準 | 紅／警／註 |
|---|---|---|
| 一(a) | D 欄自表頭下一列起，數字 token 逐段比較，非遞減 | 紅 |
| 一(b) | `feature.yaml delivery.leaf_ids` 有宣告 → 母體差集非空即紅；未宣告 → 註「未比對」；無 TC 之需求列其餘欄非空 → 紅 | 紅／註 |
| 二 | F 欄全 `^NR1L-[A-Za-z]+-\d{3}$`；ABBR 單一且 = `delivery.tc_id_abbr`；未宣告即紅；tc_id 非依列序 → 註 | 紅／註 |
| 三 | G 欄唯一值 = `delivery.test_group`（缺則頂層 `feature`）；未宣告即紅 | 紅 |
| 四 | Author 全 PeiPYHsu；Priority 全 P0–P3；Est. Time 非空 → 警 | 紅／紅／警 |
| 五 | 檔名合客戶形制且 `{FeatureName}` = G 欄去空白；MANIFEST 有列且 sha 相符 | 紅 |
| 六 | 同目錄有 `DELIVERY_NOTE.md`；同目錄有 DR／PENDING 檔或 NOTE 內有 `DR-` | 紅 |
| 七 | I～N 欄 PENDING = 0，或 MANIFEST note 含 `R-` 號 → 註 | 紅／註 |

## 二、自測（PLAYBOOK §7.1 雙向，分析層沙箱以實檔副本跑）

以 ICS／SU／PM（`output/…20260830`）／Display／Popup 五本實檔副本組最小 repo：

- **已知靶 ICS**：命中 三（G 欄 `ICS` 非全名）、四（Author 全空 31 列）、五（檔名 `ICSManagement` ≠ `ICS` 去空白 —— 與三同因）；七 PENDING 6 格因 MANIFEST note 載 `R-ICS54(a)` 而為註不為紅。**與 §一預期相符。**
- **反向 SU**：命中 二（`newR1L-` 319 列）、五（MANIFEST 無列）、七（568 格無 R- 號）。
- **反向 PM（output 名副本）**：命中 四 Priority 全空 287 列、七 267 格；tc_id 非列序 → 註（PARTIAL 本，符合 R-G40 四）。
- Display：僅命中 二（`TC-DM-`），列序／空列／Author／Priority 皆綠。

實 repo 上跑 `python scripts/lint_delivery_spec.py`：預期 4 檔皆在基線內 → 只計警示 → **PASS，exit 0**。此為 Pei 端實跑項（§四-1），分析層無法在其機器上執行。

## 三、未做（具名，不假裝）

1. `feature.yaml` 之 `delivery.{tc_id_abbr,test_group,leaf_ids}` **未寫入任何既有 feature**（補填屬回歸之一種）。日後各 feature 再交付時，其下放包補此三鍵；`new_feature.py` 樣板亦未改，留待下一個新 feature 起建時併入。
2. `rulings_hash.py` 未重生（分析層無法執行）——R-G41、R-G42 之 sha 待 §四-2。
3. `gates_tsv.py --check` 於本包前是否已因手插之 `body_kind` 列而紅，分析層未量；本包之 `delivery_spec` 列位置與生成函式一致，**不會新增不符**，但若 `body_kind` 列本已使 `--check` 紅，本包不解之。
4. `features/<f>/output/` 廢用（R-G42 八）只入條文，未加 `.gitignore`、未清檔（Pei：不回歸；git 屬 Tier 3）。

## 四、待 Pei

1. 實跑 `python scripts/lint_delivery_spec.py` 與 `python -m pytest tests/test_lint_delivery_spec.py -q`，回報 PASS／16 passed 與否。
2. `python scripts/rulings_hash.py`（重生 R-G41／R-G42 sha）→ 回填 ledger 兩處「待重生」。
3. commit：ledger、FO、本包、六個新增／修改檔。建議訊息 `feat(gate): add DELIVERY-SPEC gate for R-G42 (delivery layout spec)`。
4. R-G42 四之 Est. Time「留空」為 [DEFAULT]，一句可改。
