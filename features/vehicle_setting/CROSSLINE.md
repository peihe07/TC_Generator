# CROSSLINE — 跨線拘束項（R-VF38）

**兩線共用。`<Feature>, 接手` 時須先讀本檔，位於 `PLAYBOOK.md` §6 與 `INDEX.md` 之前。**

本檔**只收跨線拘束項**，不複述條文全文。**短是其有效性之前提** ——
超過一頁即失去被讀之可能。已解除者立即移入檔末「已解除」區，不刪。

**「未受保護」之意義**（R-VF38 三）：條文仍有拘束力，惟其被無聲違反之風險
未被消除。**非「未生效」。** 須於每次上繳具名，直至補齊機械檢查。

---

## 受保護（有能失敗之檢查）

| 條文 | 受拘束之對象 | 一句話 | 機械檢查 | 開立 |
|---|---|---|---|---|
| **R-VF17** | `docs/reports/writability.tsv`／`generatable.tsv` 之 4 leaf（見 `data/grade_overrides.tsv`） | 該 4 leaf 之分級為 W0，四欄皆有其應有之值 | `python3 scripts/grade_overrides.py --check` | 2026-08-23 |
| **R-VF20 / R-VF32 / R-VF39** | 同上 | **`writability_driver.py --write` 之尾段已自動呼叫覆寫層**（R-VF39 授權）—— 重跑 driver 會使該 4 leaf **自動回復 W0**，此為裁定之意圖 | `python3 scripts/writability_driver.py --write` 後 `--check` 應 exit 0 | 2026-08-23 |
| **R-VF16** | `data/vf230_leaves.tsv` | VF230 之 leaf 母體為 627，8 列標 `disagree=1` | `python3 scripts/vf230_layer2.py`（內含 `assert tot_leaf == 627`） | 2026-08-23 |
| **R-VF23** | `docs/handoff/`、`docs/upstream/` 之檔名 | VF230 線之檔須以 `V` 起首；`docs/upstream/vf230/` 不得存在 | `grade_overrides.py --check`（檢查一，R-VF40） | 2026-08-23 |
| **R-VF10** | `RULINGS.md`／`ANOMALIES.md` 之編號 | 同一編號不得有兩個定義 | `grade_overrides.py --check`（檢查二，R-VF40）—— **⚠ 現行即失敗：`R-VS59`–`R-VS66` 各有兩義，見 A-VF10。修法為 W-VF13 之改編，未執行** | 2026-08-23 |

## 未受保護（無機械檢查 —— 每次上繳須具名）

| 條文 | 受拘束之對象 | 一句話 | 缺何檢查 | 開立 |
|---|---|---|---|---|
| **R-VF18** | 全庫之數字陳述 | 母體變更時只改現行有效之陳述，歷史不追改 | 無檢查（`vf230_wvf20_619.py` 只涵蓋 `619` 一數） | 2026-08-23 |
| **R-VF21 / R-VF28** | 任何新寫之判準 | 判準須附必命中／必不命中／鑑別錨點；錨點須先驗存在；以內容定錨不以行號 | 無檢查（僅 `PLAYBOOK.md` 檢查表） | 2026-08-23 |
| **R-VF26** | 全部 036 工作簿 | 現階段不執行任何寫回；解凍須 Pei 明示 | 無檢查 | 2026-08-23 |
| **R-VF13 第 5 項** | 覆寫清單所列 leaf 之 TC `reasoning` | 須具名來源欄名與 reqid | `L-VF1` **已設計未實作**（`docs/reports/wvf26_reasoning_gate.md`） | 2026-08-23 |
| **R-VF33** | 任何既有檔之修改 | 修改前須列其消費者與解析路徑 | 無檢查。已致一次實害：A-VF7 之首行加註會使 `DictReader` 取不到欄 | 2026-08-23 |

## 已解除

（無）
