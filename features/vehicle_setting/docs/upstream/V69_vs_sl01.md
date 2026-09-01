# 上繳包 V69 —— 下放包 VS-SL-01（Vehicle Settings 設定項查找配方，dry-run）

日期：2026-09-01　層級：Tier 1 → Tier 2　對應下放包：**VS-SL-01**
取號：落檔當下實測 `docs/upstream/` 止於 `V67_wvf89.md`，取 **V69**（沿雙數序）
性質：**dry-run。未寫回任何工作簿，未動 `forms/`，未動 `delivered/`。**

---

## §1　產物路徑與 SHA256

| 檔 | bytes | SHA256 |
|---|---:|---|
| `features/vehicle_setting/scripts/settings_lookup.py` | 18,136 | `f26f2ae4012412bff8295c871b0ee55372cba66b7b106bf1042ac8dbc2c1d7dc` |
| `features/vehicle_setting/scripts/vs_sl01_dryrun.py` | 14,691 | `727bc9ff6040e72bde3a9c9cb9c38d18a05855e6951344479d30cb42056c6f3f` |
| `features/vehicle_setting/scripts/vs_sl01_selfcheck.py` | 4,068 | `e4fb701209b8354de3add9e926963923e89376a599f7bf81ce2b623115061763` |
| `features/vehicle_setting/data/settings_alias.tsv` | 7,805 | `94fcec25c11010ec9e54fc0ab4082df52f1176881870461ce626c5fc9a48bebc` |
| `features/vehicle_setting/reports/vf230_settings_dryrun.tsv` | 79,694 | `065a0bb754ace82d2d4a12cf9d99bdaab1145311a5a106ed7ca2bc9c9c67e1f4` |
| `features/vehicle_setting/reports/vf230_settings_dryrun.md` | 7,533 | `a2535e5f8855198a834568bb1e491232e1050eb538c5a34912cb29d668546759` |
| `features/bed_lowering/reports/bl_settings_dryrun.tsv` | 39,371 | `f2b7a2ab606e6c4f140bdbf289ddd9781acd44e553df3b202ffaec508c27519e` |
| `features/bed_lowering/reports/bl_settings_dryrun.md` | 2,405 | `bf8656d9a551062d32145a9d527c1388889aeeb242a423f95386e9cd5d570b47` |
| `features/vehicle_category/reports/vc_settings_dryrun.tsv` | 21,426 | `2d0611cef52cd5eb90fed67d15639e1a6c041d2322c92859af9a68dfe1340703` |
| `features/vehicle_category/reports/vc_settings_dryrun.md` | 2,619 | `aa9aca225ebbb343e11fe83677c8e0a9f1af8deb1c570b78368b31c5f4577328` |

治理文件之改動（無 SHA，逐段可 diff）：
`RULINGS.md`（+`R-VS84`–`R-VS88`）、`DATA_REQUESTS.md`（+`DR-49`）、
`ANOMALIES.md`（+`A-VS166`–`A-VS168`）。

## §2　摘要 §A–§D

全文見 `features/vehicle_setting/reports/vf230_settings_dryrun.md`。要點：

- **§A**　457 列全掃；相異設定名 **107**；別名 `exact` 51／`manual` 2／`UNRESOLVED` 54。
  **與包內三個數不符**（106→107、18→19、7→5），逐項附證據，記 `A-VS166`。
- **§B**　`NEG_CONTRA` **3 列**（r150／r153／r156）為真矛盾；`PATH_ABSENT` **365 列**
  且逐層路徑 **0 列**（記 `A-VS168`）；`NON_NAFTA` **19 列**（r400–r418）。
- **§C**　`Always false` 對得上者 **3 名 8 列**，依 `R-VS85` 不出負向，登記備查。
- **§D**　六項待 Pei 決 ＋ 一項備忘，含**編號命名空間之疑**（見 §4）。

## §3　未結 DR 清單

| DR | 狀態 | 內容 |
|---|---|---|
| **DR-49** | **本輪新開，登記未送出** | 54 個設定項顯示名於 HMI Settings List 與 FIP 总控表皆無逐字對應（涉 207 列）；另含 VC 之 `Vehicle Category feature` 存在性表述（16 列）與 `Camera App` 指稱（2 列） |
| DR-41 ~ DR-48 | 沿前輪，未結 | 本輪未觸及 |

## §4　自報之執行層事項

1. **編號命名空間未自裁**　本五條依包內 `R-VS{live}` 取 `R-VS84`–`R-VS88`（主線實測最大 `R-VS83`），
   **但 `R-VS63` 已將 VF230 線之 ruling 空間定為 `R-VS100` 起、其後改用 `R-VF`（實測最大 `R-VF142`）**，
   而本五條之範圍為 VF230／VF665。**若應為 `R-VF143`–`R-VF147`，請裁，本層不自行搬號。**
   三筆 anomaly 同（取 `A-VS166`–`A-VS168`，主線實測最大 `A-VS165`）。

2. **包內第五條未取號**　`R-VS{live+5}`（本輪範圍）為作業範圍宣告而非判準，
   且其所令之 BL／VC 裁定應記於 `R-BL`／`R-VC`。本層未於 `RULINGS.md` 取號，已於該處具名。

3. **本層自報之誤（已於落檔前更正）**
   - `_parse_terms()` 初版未去條件式引導詞，致 param 帶 `If`，FCW 產出四條重複 PROXI。已修。
   - 負向 TC 之提議初版列出全部正值，**與 §4「負向 TC 取 raw 0 (Absent)」相違**。
     已改為 `propose_proxi()` 統一處理（負向取 Absent、OR 列舉取本列之值並註記 EP 兄弟）。

4. **`gate_all.py` 之紅為本輪之前既有，本輪無增紅**　落檔前後各跑一次，
   紅者同為 `canon_refs`（503）／`rulings_hash`／`gates_tsv`／`lint_paths`（4），**數字逐項相同**。
   其中 `lint_paths` 之 4 筆為 `driver_distraction/workbook/` 兩檔與 ICS／SWUpdate `delivered/` sha，
   與本包無涉。`rulings_hash` 本輪之前已紅，本層**未重跑** `rulings_hash.py`
   —— 重生指紋表屬治理動作且會與既有紅混在一起；`R-VS84`–`R-VS88` 之指紋待該紅結清後一併重生。

5. **選項字串保留原文**　Settings List r249 之 E 欄逐字為 `Off/ Only Warning/Warning+ Active Braking`，
   與包內 §4 之 `Warning + Active Braking` 差一空格。**本層不修**，列為 §D 第 6 項待裁。
