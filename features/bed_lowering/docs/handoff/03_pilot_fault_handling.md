# 下放包 03 — Bed Lowering Mode：pilot 批（Fault Handling）+ 四庫補綁

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01、02，取 03
對象：執行層（Tier 1）
前置：四裁已落（R-BLM7 ~ R-BLM10，見 `RULINGS.md`）。**pilot 阻斷已解除。**

---

## 一、本包生效之裁定（引用，全文在 RULINGS.md）

| 裁定 | 一句話 | 對本包之效果 |
|---|---|---|
| R-BLM7 | `spec_mode = D` | 批次語料取 `data/leaf_inventory.tsv`；PDF 不入 prompt |
| R-BLM8 | yaml 巢狀形制 + `spec_reference_template: null` 追認 | 現行 `feature.yaml` 即定案，僅補 `spec_mode: D` 一鍵 |
| R-BLM9 | 四庫沿 vehicle_setting | 本包 §三 |
| R-BLM10 | R-G 引用一律 FO 讀法 | 本包引用同此 |

---

## 二、`feature.yaml` 補一鍵

`spec_mode: null` → `spec_mode: D`。其餘不動（R-BLM8 已追認現檔）。
改後重跑載入驗證（上繳 02 §七之指令），回報通過。

---

## 三、四庫補綁（R-BLM9，pilot 前完成）

1. 讀 `features/vehicle_setting/feature.yaml` 之 `reference:` 節
2. `dbc_b`／`dbc_fd`／`lid`／`proxi` 四項**逐字抄**檔名與路徑至本 feature
   `reference:` 節，sha256 **自實體檔重算**（不抄 vehicle_setting 之雜湊值——
   抄值驗不出檔案已被替換；算出後若與 vehicle_setting 所載不符，停下回報）
3. vehicle_setting 未綁全四項 → 缺項列出，停下回報待 Pei 點名，不得自擇
4. 上繳附四項之 `{檔名, sha256}` 表

---

## 四、Pilot 批（Tier 2 產物，生成後停）

- 範圍：`Fault Handling` 全組 **13 leaf**（母號 011／037／038），
  以 `data/test_set_map.tsv` 過濾 `leaf_inventory.tsv` 取列，不手挑
- 語料：每 leaf 之 037 欄位（title／description／verification criteria／
  method／priority_037）+ profile + framework Part II/III + IN 規則。
  PDF 不入語料（R-BLM7）
- 產出落 `batches/pilot/`，工作簿**不寫回**——pilot 審過才進工作簿
- manifest 必附：prompt 模板 sha256、exemplar 集 sha256、IN 現行 sha256、
  批內 N 欄相異值數（**預期 1**，R-BLM5 生效之單一指標）
- 每 TC 過 IN §9 自查；`test_item` 括號下半缺 = FAIL 不出貨（R-S4）
- 缺值依 §8.4.3：速度門檻落 `PENDING: DR-1 ...`（011/037/038 群預期不含，
  出現即如實落，不繞）
- **生成 13 TC 後停。不續批、不寫回、不自評通過。** 上繳含逐 TC 全文，
  交 Pei 審（退出準則 R-G15，FO 讀法）

## 五、上繳自陳要求

照例逐項自問「這一項現在驗得了嗎」。特別點名：prompt_builder 相容性
（上繳 02 §八-1 之未驗項）在本包**必然被驗到**——首次組批即是實測，
無論過不過都寫明結果。

## 六、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |
