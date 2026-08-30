# 14 — BHCAN2 綁定之影響量測（唯讀，不綁）

下放包 14 作業 C。DUT：Radio `R1L`／EE `Atlantis High`／ECU `LTM`／變體 `Disassociated`。

**本包一字未改之檔**（R-ICS44(d)）：`forms/FORMS.md`、
`features/ics_management/feature.yaml`、`features/display/` 底下任何檔、
`forms/PDT27_E2A_R1_BHCAN2.dbc`。本檔為本包唯一新建之檔。
**本包未執行任何 git 指令**（唯讀者亦未執行）。

量測工具：`grep -rn`／`grep -rc`／`shasum -a 256`／`awk 'END{print NR}'`／
`python3 -c`（json 列舉）。凡有數字者皆自列舉長度取得，無手估。

---

## §1 `forms/FORMS.md` 之現行登錄

`forms/FORMS.md` 共有 **4** 個 `### ` 級參考資料庫登錄（§「參考資料庫（DBC / PROXI / LID）」，
行 452–543），其中 **.dbc 者 2 支**：`PDT27_E2A_R1_BHCAN2.dbc`、`PDT27_E2A_R1_FDCAN8.dbc`。

### 1.1 節前之通則（行 452–463，逐字）

```
## 參考資料庫（DBC / PROXI / LID）

依 **R-G12**（Pei 2026-08-24，全域）：DBC、PROXI 表、LID 對照表一律置於
`forms/`，不另立 `reference/`。`forms/*` 已由根 `.gitignore` 排除、
`FORMS.md` 已 tracked，形狀未變更（檔案不入 git，manifest 入 git）。

每檔六項必填欄位：(a) 檔名／SHA256／bytes／mtime　(b) 涵蓋範圍
(c) 版次與其來源　(d) 已知不涵蓋者　(e) 取代關係　(f) 首個採用之 feature
與日期。(b) 為必填之理由見 **R-G13**：無涵蓋範圍之登錄，「查無」不構成發現。

涵蓋範圍(b) 一律為執行層實測所得，量測條件見
`features/display/docs/upstream/04_reference_store.md` §4。
```

### 1.2 `PDT27_E2A_R1_BHCAN2.dbc`（行 465–481，逐字全文）

```
### `PDT27_E2A_R1_BHCAN2.dbc`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19 選定為其 B-CAN 資料庫）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。

- **(a)** SHA256 `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`
  · 167,226 bytes · mtime 2026-08-24T19:59:45
- **(b) 涵蓋範圍**：B-CAN（BHCAN2）。訊號定義列 **344**（相異訊號名 342）、
  訊息 **63**。編碼非 UTF-8（以 cp1252 解讀）；行尾 CRLF 3,359 + 裸 LF 8
- **(c) 版次**：`R1`（檔名所載，非推定）
- **(d) 已知不涵蓋**：FD-CAN 上之訊號。例：`CM_TCH_STAT` 於本檔 0 命中，
  但 LID r368 載其為 `TELEMATIC_FD_5.CM_TCH_STAT`、`CAN` 欄為 `FD` ——
  **本檔本就不該有，不得記為缺漏**（R-G13 之教案）
- **(e) 取代關係**：與 `PDT27_E2A_R4_BHCAN.dbc`
  （`features/vehicle_setting/inputs/`）**並非版次關係**。訊號名集合
  三分實測：兩者皆有 310、僅 R4 有 **573**、僅 BHCAN2 有 **32**。
  何者適用於本專案**未裁定**（A-DM14）
- **(f) 首個採用**：`display`，2026-08-24
```

**逐欄摘出（供對照，非轉述取代原文）**：
使用 feature = `display`（唯一，R-DM19）；版本 = `R1`；來源 = 檔名所載；
sha256 = `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`（**有登**）；
bytes = 167,226；mtime = 2026-08-24T19:59:45；首個採用 = `display`，2026-08-24。

**本包實測複驗**：`shasum -a 256 forms/PDT27_E2A_R1_BHCAN2.dbc`
= `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60` —— **與登錄值相符**。
`ls -l` 實測 bytes = 167226、mtime = `Aug 24 19:59` —— 與登錄相符。

### 1.3 `PDT27_E2A_R1_FDCAN8.dbc`（行 483–496，逐字全文）

```
### `PDT27_E2A_R1_FDCAN8.dbc`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。

- **(a)** SHA256 `2a86c4bf3e670d71b362d430b446d8d157c74b94429e833362f81f4a48f6a22e`
  · 1,106,532 bytes · mtime 2026-08-24T19:59:52
- **(b) 涵蓋範圍**：FD-CAN（FDCAN8）。訊號定義列 **1,916**（相異訊號名
  1,634）、訊息 **318**。cp1252；CRLF 19,805 + 裸 LF 2
- **(c) 版次**：`R1`（檔名所載）
- **(d) 已知不涵蓋**：B-CAN 上之訊號。例：`DCSD_DISP_STAT`、
  `RQ_DISP_INTS` 於本檔 0 命中，二者皆在 B-CAN 上
- **(e) 取代關係**：與 `PDT27_E2A_R5_FDCAN8.dbc`（vehicle_setting）並存；
  R5 有訊號定義列 2,037／訊息 323，較 R1 多。兩者之差異本輪未逐一比對
- **(f) 首個採用**：`display`，2026-08-24
```

### 1.4 另二支 dbc —— `PDT27_E2A_R4_BHCAN.dbc`、`PDT27_E2A_R5_FDCAN8.dbc`

**`forms/FORMS.md` 中查無此二檔之登錄。**

實測：`grep -c 'R4_BHCAN\|R5_FDCAN8' forms/FORMS.md` = **2**，二處皆非自身之登錄，
而是出現在他檔登錄之 (e) 欄內：

- 行 477（`BHCAN2` 之 (e)）：``- **(e) 取代關係**：與 `PDT27_E2A_R4_BHCAN.dbc```
- 行 494（`FDCAN8-R1` 之 (e)）：``- **(e) 取代關係**：與 `PDT27_E2A_R5_FDCAN8.dbc`（vehicle_setting）並存；``

`grep -n '^### ' forms/FORMS.md` 於「參考資料庫」節內只回四個標題（行 465／483／498／522），
無 R4／R5 之標題列。故此二檔**無 (a)–(f) 六欄登錄、無 sha256 登錄、無「使用中之 feature」反向記載**。

**此為 §6 之未預料事項第 1 條**：`ics_management/feature.yaml` 現行綁定之
`dbc_b`／`dbc_fd` 二檔，**皆不在 `FORMS.md` 台帳內**，且其實體位置
（`features/vehicle_setting/inputs/`）與 R-G12「DBC 一律置於 `forms/`」不合。

四支 dbc 之 sha256（本包 `shasum -a 256` 實測）：

| 檔 | sha256 | FORMS.md 有無登錄 |
|---|---|---|
| `forms/PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60` | 有（(a)） |
| `forms/PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71b362d430b446d8d157c74b94429e833362f81f4a48f6a22e` | 有（(a)） |
| `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0` | **查無** |
| `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2` | **查無** |

（另二支非 dbc 之參考資料庫登錄為 `Logical Identifiers and CAN Mapping v1_78.xlsx`
行 498 與 `PROXI_HDCC27_R3_20250424.xlsx` 行 522；前者已為 ics_management 所綁，
後者本 feature 未綁。）

---

## §2 `features/ics_management/feature.yaml` 之現行綁定與需改之鍵

### 2.1 `reference:` 區塊逐字（dbc 相關項及其前後註解）

節首（逐字）：

```
# R-G15：其變動會使既有產出失效者一律綁定。
# paths 記「檔在哪」，reference 記「檔是哪一份」。同一檔出現於兩節不是重複。
# 下列 sha256 皆本包自實體檔重算（`shasum -a 256`），非抄他處宣告值。
reference:
```

dbc 相關項（逐字，含其上之註解區塊）：

```
  # ── R-ICS8／R-ICS10（2026-08-29，下放包 02）起綁下列四件 ──────────
  # 01 輪之「本包未綁」註記作廢：其理由為「無經裁定之庫」，
  # R-ICS8 已指名 LID v1_78 與二 DBC 為對照權威，該理由消滅。
  # 皆綁原件不複製（R-ICS10）；sha256 皆本包自實體檔重算。
  #
  # LID：R-ICS8(a) 明令取 v1_78（CFTS020-4819547 逐字令取 latest version）。
  # **不承接 driver_distraction 所綁之 v1_76** —— 該綁定繫於 R-DD5，非全域。
  lid:
    file: "forms/Logical Identifiers and CAN Mapping v1_78.xlsx"
    sha256: "a01e1679c706cd454daf82573a732fe5ad5eedb3865083897cb18c970b312433"
  # 二 DBC：R-ICS8(c) 之篩用庫。b02 實測 ICS 之按鍵／旋鈕訊號全在 BHCAN
  # （`BO_ 1050 CLIMATIC_PANEL: 8 ICS`），FDCAN8 三候選訊息皆無。
  dbc_b:
    file: "features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc"
    sha256: "9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0"
  dbc_fd:
    file: "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc"
    sha256: "51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2"
```

`reference:` 節之完整鍵集（`yaml.safe_load` 後之 `len()` 與 `sorted()`，共 **10** 鍵）：
`a03_report`／`cfts020_fs`／`cfts022_fs`／`dbc_b`／`dbc_fd`／`dtcs_matrix`／
`lid`／`sys2_export`／`sysad`／`workbook_master`。**BHCAN2 不在其中。**
其中宣告了 `sha256` 者 **10**（即 10/10）。

`paths:` 節之鍵集（同法，共 **6** 鍵）：
`a03_report`／`cfts020_fs`／`cfts022_fs`／`sys2_export`／`sysad`／`workbook`，
**無任何 dbc 鍵**。

對照：`features/display/feature.yaml` 之 `reference:` 為 **13** 鍵
（`a03_report`／`cfts013_doc`／`cfts013_sysra`／`cfts_doc`／`dbc_b`／`dbc_fd`／`lid`／
`popup_list`／`popup_priority_matrix`／`proxi`／`sys2_export`／`sys3_sysad`／`workbook_master`），
其 `dbc_b` 即 BHCAN2。

### 2.2 加入 BHCAN2 需改哪些鍵（逐鍵；本包只列，不改）

`reference:` 節每一項之形制為 `{file, sha256}` 二鍵，`file` 之基準為 **repo 根**
（display 之 feature.yaml 行 55 註：`reference:` 記「檔是哪一份」；其 `dbc_b.file`
即寫 `forms/PDT27_E2A_R1_BHCAN2.dbc`，為 repo 根相對）。

| # | 鍵名 | 現值 | 需要的新值形態 |
|---|---|---|---|
| 1 | `reference.<新鍵>` | **不存在** | 新增一個 `{file, sha256}` 項。鍵名有二選一，見下方註 A |
| 2 | `reference.<新鍵>.file` | — | `"forms/PDT27_E2A_R1_BHCAN2.dbc"`（repo 根相對，不加 `features/` 前綴） |
| 3 | `reference.<新鍵>.sha256` | — | `"46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60"`（本包實測） |
| 4 | `reference.dbc_b.file` | `"features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc"` | **視 A-DM14 之裁定而定**：若裁「BHCAN2 取代 R4」則本鍵之 file／sha256 二值皆須改；若裁「並存」則不動。**本包不裁、不提案** |
| 5 | `reference.dbc_b.sha256` | `"9ef1ec98…30d0"` | 同上，繫於 A-DM14 |
| 6 | `paths.*` | 無 dbc 鍵 | **不需新增**。本 feature 之六支讀 dbc 腳本（§5）無一自 `paths:` 取路徑 |

> **註 A（鍵名之衝突面）**：display 之 `reference:` 以 `dbc_b` 指 BHCAN2；
> ics_management 之 `reference:` 以 `dbc_b` 指 R4_BHCAN。二者鍵名相同、所指檔不同。
> 若 ics_management 採「並存」而以 `dbc_b` 加入 BHCAN2，將與其現行 `dbc_b`（R4）撞名，
> 必須另取鍵名（例如 `dbc_b2`）；若採「取代」則直接改 `dbc_b` 之二值。
> **鍵名之選定隱含 A-DM14 之取捨，故本包不提具體鍵名。**

### 2.3 sha256 欄位機制 —— 是否必填、由誰檢查

- **形制上必填**：`reference:` 現行 10 項**每一項皆有 `sha256`**（自列舉，10/10），
  且檔頭註明「下列 sha256 皆本包自實體檔重算（`shasum -a 256`），非抄他處宣告值」。
- **檢查程式**：全 repo 之 `verify_reference_binding.py` 實測共 **2** 份
  （`grep -rn "verify_reference_binding" --exclude-dir=.git .` 之檔案列舉）：
  - `features/display/scripts/verify_reference_binding.py`
  - `features/bed_lowering/scripts/verify_reference_binding.py`

  **`features/ics_management/scripts/` 下查無此檔**（`ls features/ics_management/scripts/ | grep -i verify`
  只回 `cfts022_reverify_07.py`、`verify_verbatim_b01.py`，二者皆非綁定檢查）。
- 其判準（display 版逐字，行 55–66 摘）：

  ```
      cfg = yaml.safe_load(FEATURE_YAML.read_text(encoding="utf-8"))
      ref = cfg.get("reference") or {}
  ```
  ```
          elif not declared:
              verdict, actual = "**NO SHA DECLARED**", sha256_of(path)[:16] + "…"
              bad.append((key, "no sha256 declared"))
  ```

  即：**未填 sha256 → 記為 bad → exit non-zero**。故對有此腳本之 feature 而言 sha 為必填。
- **實測結論**：`ics_management` 目前**無任何程式比對其 `reference:` 之 sha256**
  —— 該節之 10 個 sha 是宣告，不是保護（此即 display RULINGS 所稱 R-G23 之「宣告不等於保護」）。
  加入 BHCAN2 一項後亦同：**若不同時落一份 `verify_reference_binding.py`，
  新增之 sha 仍不受檢**。此為 §6 未預料事項第 2 條。
- **BHCAN2 之 sha256（本包 `shasum -a 256` 實測）**：
  `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`

---

## §3 會動到誰 —— `display` feature 之現行使用面（唯讀）

### 3.1 引用清單（逐檔）

`grep -rlc "BHCAN2" features/display/` 之檔案列舉長度 = **25 檔**。逐檔與命中數
（`grep -rc`，命中數為含 `BHCAN2` 之行數）：

| # | 路徑 | 命中行數 | 類別 |
|---|---|---|---|
| 1 | `features/display/ANOMALIES.md` | 11 | 分析層五簿 |
| 2 | `features/display/DATA_REQUESTS.md` | 1 | 分析層五簿 |
| 3 | `features/display/DECISIONS.md` | 1 | 分析層五簿 |
| 4 | `features/display/RULINGS.md` | 4 | 分析層五簿 |
| 5 | `features/display/data/signal_resolution.tsv` | 23 | 資料產出 |
| 6 | `features/display/docs/INDEX.md` | 3 | 文件 |
| 7 | `features/display/docs/handoff/04_reference_store.md` | 16 | 文件 |
| 8 | `features/display/docs/handoff/05_proxi_and_values.md` | 14 | 文件 |
| 9 | `features/display/docs/handoff/19_consolidated.md` | 1 | 文件 |
| 10 | `features/display/docs/proxi_triage_proposal.md` | 1 | 文件 |
| 11 | `features/display/docs/upstream/04_reference_store.md` | 53 | 文件 |
| 12 | `features/display/docs/upstream/05_proxi_and_values.md` | 3 | 文件 |
| 13 | `features/display/docs/upstream/06_glossary_anchor.md` | 1 | 文件 |
| 14 | `features/display/docs/upstream/08_recon_and_norm.md` | 1 | 文件 |
| 15 | `features/display/docs/upstream/11_binding_verify.md` | 1 | 文件 |
| 16 | `features/display/docs/upstream/12_assertions.md` | 1 | 文件 |
| 17 | `features/display/docs/upstream/13_honest_guards.md` | 1 | 文件 |
| 18 | `features/display/docs/upstream/19_consolidated.md` | 2 | 文件 |
| 19 | `features/display/docs/upstream/21_pilot01_rev2.md` | 1 | 文件 |
| 20 | `features/display/docs/upstream/22_pilot01_rev3.md` | 3 | 文件 |
| 21 | `features/display/docs/upstream/27_stale_fix.md` | 1 | 文件 |
| 22 | `features/display/docs/upstream/28_cfts013_full_and_rvc.md` | 1 | 文件 |
| 23 | `features/display/feature.yaml` | 2 | 設定 |
| 24 | `features/display/scripts/dbc_probe.py` | 7 | 腳本 |
| 25 | `features/display/scripts/signal_resolution.py` | 2 | 腳本 |

以**完整檔名**（`PDT27_E2A_R1_BHCAN2.dbc`）為鍵之引用，`grep -rn` 命中列舉長度 = **21 行**，
分佈於 **16** 檔。其中「以路徑實際開檔」者，逐字如下：

- `features/display/feature.yaml:28`：
  ```
      file: "forms/PDT27_E2A_R1_BHCAN2.dbc"
  ```
  （其上下文為 `reference.dbc_b`，行 27–29；行 24 之註逐字：
  `# 選定依據見 R-DM19（B-CAN = BHCAN2，Pei 2026-08-24 指示並親自置檔）。`）
- `features/display/scripts/dbc_probe.py:22`：
  ```
      "BHCAN2-R1": ROOT / "forms" / "PDT27_E2A_R1_BHCAN2.dbc",
  ```
- `features/display/scripts/signal_resolution.py:38`：
  ```
      "BHCAN2-R1": ROOT / "forms" / "PDT27_E2A_R1_BHCAN2.dbc",
  ```

其餘 18 行為 `.md`／`.tsv` 內之記述或驗證表列（如
`features/display/docs/upstream/11_binding_verify.md:54`：
``| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |``），
非開檔點。

### 3.2 實數 —— 已交付 TC 幾條、腳本幾支

- **腳本：2 支**（自 3.1 之「腳本」類列舉：`dbc_probe.py`、`signal_resolution.py`）。
  二支皆為**硬寫路徑**（`ROOT / "forms" / "PDT27_E2A_R1_BHCAN2.dbc"`），
  **不自 `feature.yaml` 取值**。
- **已交付 TC：0 條。**
  依據：`features/display/delivered/MANIFEST.tsv` 之總行數（`awk 'END{print NR}'`）= **1**，
  該行為表頭 `filename	sha256	source_path	delivered_round	note`，**資料列 0**。
  故 `display` 至今**無任何已交付件**。
- **未交付但已生成之 TC：23 條**（`features/display/generated/` 三檔之 `tcs` 陣列長度和：
  `ops-01.json` 14 ＋ `pilot-01.json` 3 ＋ `rvc-01.json` 6 = 23；另有 `deferred` 陣列
  6＋3＋4 = 13 條不計入）。
  其中內容含 BHCAN2 所解出之訊號名
  （`DCSD_DISP_STAT`／`RQ_DISP_INTS`／`TGW_DISP_STATSts`／`CameraDisplaySts`／`FPDM_DISP_STAT`
  任一）者 **15 條**（ops-01 7、pilot-01 2、rvc-01 6）。
  `grep` 三檔 json 之 `BHCAN2` 字面命中 **0** —— 即 TC 內文不出現庫名，只出現其解出之訊號名。
- **資料產出：1 檔**（`data/signal_resolution.tsv`），總行數 **27**（含表頭），
  含 `BHCAN2` 之行 **23**。R-DM19 逐字自承其承載為「`features/display/data/signal_resolution.tsv` 之 26 列」。

### 3.3 【E24 停下條件】判定 —— **E24 未觸發**

判定所據之三項實測：

1. **工具鏈不以 `feature.yaml` 決定「唯一擁有者」。**
   `verify_reference_binding.py` 之作用域逐字（display 版行 20–21）：
   ```
   ROOT = Path(__file__).resolve().parents[3]
   FEATURE_YAML = Path(__file__).resolve().parents[1] / "feature.yaml"
   ```
   即**只讀自己 feature 之 feature.yaml**，逐鍵比對「宣告 sha vs 實檔 sha」。
   全 repo 查無任何跨 feature 之擁有者／獨佔性檢查：
   `grep -rn "owner\|唯一擁有者" scripts/lint036.py scripts/gate_all.py scripts/lint_paths.py`
   命中 **0**；`scripts/feature_config.py` 內 `reference` 命中 **0**
   （即共用設定載入器根本不讀 `reference:` 節）。
2. **不會產生版本／sha 分歧。** 二 feature 若同宣告此檔，宣告值必同為
   `46cb73f3…1cc60`（同一實體檔、同一 `shasum` 演算法）。FORMS.md 之 (c) 版次
   欄亦同為 `R1`。故無「二 feature 對同一檔宣告不同版本／不同 sha」之情形。
3. **display 之既有產出不因此改變。** display 之二支腳本硬寫 `forms/…BHCAN2.dbc`
   絕對路徑，與任何 feature.yaml 之綁定無關；其 `signal_resolution.tsv` 23 列、
   `generated/` 之 23 條 TC、`LOOKUP_MISSES.md` M-1／M-2 之輸入皆為同一實體檔，
   該檔本包不動（`shasum` 複驗與 FORMS.md 登錄值相符）。
   `display/delivered/MANIFEST.tsv` 資料列 0，無已交付件可被動搖。

**故：綁定 BHCAN2 到 `ics_management` 不會改變 `display` feature 之任何既有產出。E24 未觸發。**

**但須明記兩項「非 display 產出、卻仍會被動到」之處**（不構成 E24，因其不在 `features/display/` 內）：

- `forms/FORMS.md` 行 467 之引用列（逐字）：
  `> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19 選定為其 B-CAN 資料庫）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。`
  依 R-G15 之反向記載義務，綁定後**此列須增列 `ics_management`**。該列在 `forms/`，不在 `features/display/`。
  **本包依 R-ICS44(d) 一字不改。**
- (f) 欄「首個採用：`display`，2026-08-24」**不變** —— 首個採用是歷史事實，不因新增使用者而改。

---

## §4 A-DM14 之現況

### 4.1 正本位置與逐字全文

正本：`features/display/ANOMALIES.md` 行 255–284。逐字：

```
## A-DM14 — BHCAN2 與 BHCAN-R4 為不同資料庫，且顯示訊號之收發節點相反  [PENDING]

`forms/PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3…`）與
`features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` 之訊號名集合
三分（相異名，逐字，`scripts/dbc_probe.py`）：

| | 數 |
|---|---|
| 兩者皆有 | 310 |
| 僅 BHCAN-R4 有 | **573** |
| 僅 BHCAN2-R1 有 | 32 |

**故二者非版次關係，是不同的資料庫。** 573 個只在舊檔存在之訊號名，其在
新架構下之地位（移除／改名／移至他匯流排）本輪不推定。

三個顯示訊號之位元定義與 `VAL_` 列舉**兩本逐字相同**，但**節點相反**：

| 訊號 | 訊息 | BHCAN2-R1 | BHCAN-R4 |
|---|---|---|---|
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK` | tx=**SGW**，rx=`ETM,LTM` | tx=**DCSD**，rx=`SGW` |
| `RQ_DISP_INTS` | `BO_ 1283 RADIO_B3` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |
| `TGW_DISP_STATSts` | `BO_ 1500 TELEMATIC_DISPLAY2` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |

> 下放包 04 §3.2 只列 tx。本輪一併實測 rx（`SG_` 行末之接收節點清單），
> **rx 亦隨之改變**，方向與 tx 一致地對調。

**發送節點決定 TC 該寫「送出」還是「觀察」**，故此差異非中繼資料。

- 提案處置：登記。**何者適用於本專案未裁定** —— 二選一需要專案之
  EE 架構配置為據，不在手上四份素材內
```

### 4.2 現行狀態

**`[PENDING]`**（標題列逐字所載）。`features/display/ANOMALIES.md` 內 `A-DM14` 命中共 **2** 行
（行 255 之正本標題、行 638 之內文引用），**無任何狀態改寫列**。

### 4.3 是否已有任何一方之處置紀錄

**無任何一方之結案處置；已有之紀錄全為「登記／押後／不逕裁」。**

repo 全域 `grep -rn "A-DM14"`（排除 `.git`）命中列舉長度 = **41 行**，分佈於 **21** 檔。
其中屬「處置性」之逐字紀錄如下：

- `features/display/ANOMALIES.md:255`（正本）：狀態 `[PENDING]`；提案處置逐字
  「登記。**何者適用於本專案未裁定** —— 二選一需要專案之 EE 架構配置為據，不在手上四份素材內」。
- `features/display/RULINGS.md:394–396`（R-DM19 之承載，逐字）：
  ```
  BHCAN-R4 有 573 個訊號名不在 BHCAN2 中（A-DM14）。其他 feature 若
  改用 BHCAN2，須逐一複驗既有訊號 —— 不在本 feature 範圍，登記於
  `forms/LOOKUP_MISSES.md` 之備註區。
  ```
  即 display 線**明示將跨 feature 面推出自身範圍**。
- `forms/FORMS.md:480`（逐字）：`  何者適用於本專案**未裁定**（A-DM14）`。
- `forms/LOOKUP_MISSES.md:37`、`:42`：二處為引用，非處置。
- `features/ics_management/RULINGS.md:1487`（R-ICS 條文，逐字）：
  ```
      綁定與否待 A-DM14（R4）之跨 feature 裁定，**不在本線逕裁**。
  ```
  其上文（行 1484–1486，逐字）：
  ```
  (h) **`forms/PDT27_E2A_R1_BHCAN2.dbc` 登記，不逕綁定**（A-ICS82）。
      其 `BO_ 1445 DIS_CENTERSTACK` 由 SGW 轉發、`DCSD_DISP_STAT` 收方明列 `ETM,LTM`，
      **可能部分回答 DR-ICS16**。b13 以唯讀方式量其對 DR-ICS16 之填補程度，
  ```
- `features/ics_management/RULINGS.md:1540`（逐字）：
  ```
      **DR-ICS16 維持 OPEN，判「部分」不採認**；PDT27 綁定待 A-DM14。
  ```
- `features/ics_management/RULINGS.md:1578–1581`（逐字）：
  ```
  (d) **`FORMS.md` 與 `feature.yaml` 本包一字不改**。
      BHCAN2 之綁定繫於 A-DM14（跨 feature，`display` 線），
      b14 只量「綁定需要什麼、會動到誰」，**不綁**。
      Pei 裁「BHCAN2」是定台架觀察點，不等於已裁跨 feature 之檔案歸屬。
  ```

**已查而查無之位置**（列出以示範圍）：
`features/display/DECISIONS.md`（`A-DM14` 命中 0）、
`features/display/BACKLOG.md`（命中 0）、
`features/display/DATA_REQUESTS.md`（命中 0；即 **A-DM14 未曾轉為 DR 發出**）、
`docs/`（全樹 `grep -rn "A-DM14" docs/` 命中 0，即**全案台帳無 A-DM14 之登錄**）、
`features/vehicle_setting/`（命中 0 —— 即 R4 之持有方**從未被告知**此爭點）。

> **關鍵不對稱（陳述，不裁決）**：A-DM14 之兩造為 `display`（持 BHCAN2）與
> `vehicle_setting`（持 R4_BHCAN），但該異常只登在 `display` 之簿內，
> `vehicle_setting` 樹下 0 命中，且從未進入任何 DR 或全案台帳。
> 其「待裁」因而沒有承載它的流程 —— 這是 §6 未預料事項第 3 條。

---

## §5 若不綁而僅引用 —— 現行工具鏈允許嗎

### 5.1 逐支列出 `features/ics_management/scripts/` 下讀 dbc 之腳本

`grep -rl "\.dbc" features/ics_management/scripts/*.py` 之列舉長度 = **6 支**。

| # | 腳本 | dbc 來源 | 是否含 BHCAN2 | 關鍵行（逐字） |
|---|---|---|---|---|
| 1 | `crossref_probe_12.py` | **硬寫路徑** | 是 | 行 45–48：`DBCS = [REPO / "forms/PDT27_E2A_R1_BHCAN2.dbc",` / `        REPO / "forms/PDT27_E2A_R1_FDCAN8.dbc",` / `        REPO / "features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc",` / `        REPO / "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc"]` |
| 2 | `etm_probe_07.py` | **硬寫檔名 + 硬寫目錄** | 否 | 行 128–130：`    for name in ["PDT27_E2A_R4_BHCAN.dbc", "PDT27_E2A_R5_FDCAN8.dbc"]:` / `        p = ROOT / "features/vehicle_setting/inputs" / name` / `        txt = p.read_text(encoding="latin-1")` |
| 3 | `lid_dbc_probe.py` | **硬寫路徑** | 否 | 行 26–29：`DBCS = {` / `    "R4_BHCAN": REPO / "features" / "vehicle_setting" / "inputs" / "PDT27_E2A_R4_BHCAN.dbc",` / `    "R5_FDCAN8": REPO / "features" / "vehicle_setting" / "inputs" / "PDT27_E2A_R5_FDCAN8.dbc",` / `}` |
| 4 | `lid_dbc_probe_b04.py` | **硬寫路徑** | 否 | 行 39–42：`DBCS = {` / `    "R4_BHCAN": REPO / "features" / "vehicle_setting" / "inputs" / "PDT27_E2A_R4_BHCAN.dbc",` / `    "R5_FDCAN8": REPO / "features" / "vehicle_setting" / "inputs" / "PDT27_E2A_R5_FDCAN8.dbc",` / `}` |
| 5 | `pdt27_probe_13.py` | **硬寫路徑** | 是 | 行 26–30：`DBCS = {` / `    "PDT27_R1_BHCAN2 (未綁)": REPO / "forms/PDT27_E2A_R1_BHCAN2.dbc",` / `    "PDT27_R4_BHCAN (dbc_b)": REPO / "features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc",` / `    "PDT27_R5_FDCAN8 (dbc_fd)": REPO / "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc",` / `}` |
| 6 | `variant_probe_10.py` | **硬寫路徑** | 否 | 行 40–43：`DBC_FILES = [` / `    ROOT / "features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc",` / `    ROOT / "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc",` / `]` |

**取自 `feature.yaml` 者：0 支。硬寫路徑者：6 支。取自命令列參數者：0 支。**
佐證：`grep -rln "feature_config\|feature.yaml" features/ics_management/scripts/*.py`
命中 **0 檔** —— 即本 feature 之腳本無一載入 `feature.yaml`。

`pdt27_probe_13.py` 之 docstring 逐字（行 4）更是明文承認此用法：
```
量測 `forms/PDT27_E2A_R1_BHCAN2.dbc`（未綁定，只讀）對 DR-ICS16 之填補程度，
```

### 5.2 判定

**答：允許。**（非「部分」）

理由，三項皆為實測而非推測：

1. **無任何強制點。** 六支腳本 0 支自 `feature.yaml` 取 dbc 路徑；
   `scripts/feature_config.py` 對 `reference` 之命中為 0，即共用載入器不讀該節。
   故「未綁定」在執行面**不產生任何阻擋**。
2. **已有二次既成事實。** `crossref_probe_12.py`（b12）與 `pdt27_probe_13.py`（b13）
   已在 BHCAN2 未綁定之狀態下讀它並產出報告
   （`docs/reports/12_cfts022_crossref_and_third_variant.md`、
   `docs/reports/13_pdt27_dbc_vs_dr16.md`），且該二報告皆自行標註「未綁定」。
   量測用而不綁定**已是本 feature 之現行慣行**。
3. **條文面亦已明示。** `features/ics_management/RULINGS.md:1484` 逐字
   「**`forms/PDT27_E2A_R1_BHCAN2.dbc` 登記，不逕綁定**（A-ICS82）」，
   同條授權「b13 以唯讀方式量其對 DR-ICS16 之填補程度」。

**唯一之限制不在工具鏈而在條文**：綁定與否決定該檔之量測結果**能否進入 TC 之實名實值**。
`RULINGS.md:1540` 逐字「**DR-ICS16 維持 OPEN，判「部分」不採認**」即此線——
可讀、可量、可寫報告；**不可採認入 TC**。

### 5.3 這對 A-DM14 意味什麼（**只陳述，不裁決**）

- A-DM14 之待裁點是「BHCAN2 與 R4 何者適用於本專案」。若「量測用而不綁定」為允許
  （5.2 之判定），則 **ics_management 取得 BHCAN2 之量測事實，不以 A-DM14 之裁定為前提**；
  A-DM14 所閘住的只是「採認入 TC」與「寫入 `feature.yaml`／`FORMS.md`」二事。
- 反面陳述：這也意味 A-DM14 之未裁**不會自動因量測累積而消解** ——
  b12／b13／b14 三包已累積之量測，無論多少，都不構成對「何者適用」之回答，
  因其待裁所需之據為「專案之 EE 架構配置」（A-DM14 提案處置逐字），
  而該據不在任何 dbc 檔內。
- 另陳述一項本包實測之新條件：A-DM14 假設之對立面是「BHCAN2 vs R4 二選一」，
  但 §1.4 實測顯示 R4／R5 二檔**根本未登錄於 `FORMS.md`**，
  與 R-G12「DBC 一律置於 `forms/`」不合。此為 A-DM14 成立時未見之條件變化。

---

## §6 下放包未預料之事

1. **`ics_management` 現行綁定之二支 dbc（R4_BHCAN／R5_FDCAN8）不在 `FORMS.md` 台帳內。**
   下放包令「一併列出該檔中另三支 dbc 之登錄」，前提是四支皆有登錄；實測只有二支有
   （§1.4）。故「另三支之登錄」一項**只能交付一支**（FDCAN8-R1），其餘二支為確定之查無。
   附帶：此二檔位於 `features/vehicle_setting/inputs/`，與 R-G12「DBC 一律置於 `forms/`」不合，
   而 ics_management 以 R-ICS10「綁原件不複製」綁之。**三者之相容性未見於任何條文。**
2. **`ics_management` 無 `verify_reference_binding.py`。**
   其 `reference:` 節 10 項 sha256 目前無任何程式比對（§2.3）。
   下放包問「該檔之 sha256 欄位機制為何（是否須填 sha）」，
   實測之答是：**形制上 10/10 皆填，但本 feature 無檢查者**——
   「須填」是慣例，不是被強制的。加入 BHCAN2 若不同時落檢查腳本，只是多一個未受檢之宣告。
3. **A-DM14 只登在 `display` 之簿內，其對造 `vehicle_setting` 樹下 0 命中，
   且未進入任何 DR、未進入全案台帳 `docs/`。**（§4.3）
   即一件明示為「跨 feature」之待裁，目前沒有任何承載它的跨 feature 流程。
   下放包問「是否已有任何一方之處置紀錄」，實測之答是：
   **只有 display 與 ics_management 兩線各自的「不逕裁」，第三方（R4 持有者）從未被告知。**
4. **鍵名撞名。** display 之 `reference.dbc_b` = BHCAN2；
   ics_management 之 `reference.dbc_b` = R4_BHCAN。**同鍵名指不同檔。**
   下放包未預期「加入 BHCAN2」會先撞上鍵名，而鍵名之選定（`dbc_b` 改綁 vs 另開 `dbc_b2`）
   本身即隱含 A-DM14 之取捨（§2.2 註 A）。本包因此不提具體鍵名。
5. **display 之「已交付 TC」實數為 0。**
   下放包問「其中屬已交付 TC 者幾條」，隱含存在已交付件；
   實測 `delivered/MANIFEST.tsv` 資料列 0。真正會受動搖之量體在 `generated/`（23 條，
   其中 15 條帶 BHCAN2 解出之訊號名），而該量體**不是交付態**。
6. **TC 內文不出現庫名。** `generated/*.json` 對 `BHCAN2` 之字面命中為 0；
   庫之影響是**經由訊號名間接承載**。故任何「以 grep 庫名找受影響 TC」之做法必回 0，
   而那個 0 是假的。本包改以五個訊號名列舉，得 15 條。

---

## §7 已知局限

1. **本包全程未執行任何 git 指令**（含唯讀），故無法確認上述任一檔之版本控管狀態、
   是否有未提交之變更、或 `forms/*` 之 `.gitignore` 實際生效情形。
   「未改檔」之自證僅以 `ls -l` 與 `shasum -a 256` 為據。
2. **§3.2 之「15 條帶 BHCAN2 解出之訊號名」以五個訊號名為探針**
   （`DCSD_DISP_STAT`／`RQ_DISP_INTS`／`TGW_DISP_STATSts`／`CameraDisplaySts`／`FPDM_DISP_STAT`），
   該五名取自 A-DM14 與 A-DM15 之表列。**若尚有其他經 BHCAN2 解出而本包未列之訊號名，
   則 15 為下界而非確數。** `signal_resolution.tsv` 之 23 列未逐列展開為訊號名清單。
3. **E24 之判定限於「工具鏈與既有產出」二面。**
   本包未評估、亦無權評估：綁定是否構成流程面／簽核面之影響
   （例如 R-G15 反向記載未同步更新是否構成缺失）。該面屬分析層。
4. **§1.2 之 (b) 涵蓋範圍數值（344／342／63／CRLF 3,359 等）本包未複驗**，
   只複驗 sha256、bytes、mtime 三項。理由：複驗 (b) 需重跑 display 之 `dbc_probe.py`，
   屬他 feature 之腳本，且對本包之綁定影響判定無增益。
5. **本包未量「若真綁定後 ics_management 之既有 8 條 TC 是否受影響」。**
   下放包只令量「會動到誰（display 側）」。ics 側之回改面繫於 R-17(f)，
   其逐字為「既有 TC 回改逐 feature 裁」，於 ICS 之裁定待 b14 量完再作 ——
   即該量測不在本作業 C 之範圍。
6. **`display` 之 25 檔引用中，22 檔為 `.md` 文件與五簿。**
   本包判定其「不因綁定而改變」是基於「文字記述不隨他 feature 之 yaml 而變」；
   若分析層認為 R-G15 之反向記載義務及於 display 之 `RULINGS.md:394–396`
   （該段明示「其他 feature 若改用 BHCAN2，須逐一複驗既有訊號」），
   則會多出一項文件同步義務。**該判斷屬分析層，本包不作。**

---

## 附錄 A — 本包之量測指令（可重跑）

```
shasum -a 256 forms/PDT27_E2A_R1_BHCAN2.dbc forms/PDT27_E2A_R1_FDCAN8.dbc \
  features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc \
  features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc
grep -n "^### \|^## " forms/FORMS.md
grep -c 'R4_BHCAN\|R5_FDCAN8' forms/FORMS.md
grep -rlc "BHCAN2" features/display/ | sort
grep -rc  "BHCAN2" features/display/ | grep -v ":0" | sort
grep -rn "PDT27_E2A_R1_BHCAN2\.dbc" features/display/
awk 'END{print NR}' features/display/delivered/MANIFEST.tsv
awk 'END{print NR}' features/display/data/signal_resolution.tsv
grep -rn "A-DM14" . | grep -v "/\.git/"
grep -rl "\.dbc" features/ics_management/scripts/*.py
grep -rln "feature_config\|feature.yaml" features/ics_management/scripts/*.py
grep -rn "verify_reference_binding" --exclude-dir=.git .
python3 -c "import yaml;c=yaml.safe_load(open('features/ics_management/feature.yaml'));print(len(c['reference']),sorted(c['reference']))"
```

TC 條數與訊號承載之列舉（python3，唯讀）：

```
python3 -c "
import json,glob
sigs=['DCSD_DISP_STAT','RQ_DISP_INTS','TGW_DISP_STATSts','CameraDisplaySts','FPDM_DISP_STAT']
for f in sorted(glob.glob('features/display/generated/*.json')):
    d=json.load(open(f))
    for key in ('tcs','deferred'):
        n=sum(1 for t in d[key] if any(s in json.dumps(t,ensure_ascii=False) for s in sigs))
        print(f,key,len(d[key]),'sig',n)
"
```
