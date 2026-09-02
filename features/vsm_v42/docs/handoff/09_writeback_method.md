# 下放包 09 — vsm_v42：寫回工法查證（R-VL22(e)／R-VL23(d) 後續）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–08，取 09
台帳不重生；DR 不送。**本包只查證與提案，不寫回**——任何對 sandbox 副本之寫入僅限工法試驗件（見 W-2），且試驗件另建目錄，`sandbox/base/` 原副本仍一位元不動。

## 一、W 清單

**W-1 存量工法盤點**：搜 `scripts/` 與各 feature 目錄之既有寫回工具（`writeback*`、`export*`、openpyxl 寫入類），逐件列：路徑、吃什麼輸入、寫哪些欄、是否經 openpyxl `save()`、其所屬 feature 之工作簿有無 x14 DV／下拉，及該線交付後有無 DV 損毀紀錄（查各線 ANOMALIES）。

**W-2 x14 DV 保全實測**：copy `sandbox/base/` 副本至 `sandbox/wb_trial/`，以 openpyxl 開啟→不改任何值→`save()`→實測比對：zip member 數、`xl/worksheets/` 內 `x14:dataValidation` 節點存廢、R 欄下拉可用性（以 XML 斷言，非猜）。再做第二件：寫入一列假資料後 save，同斷言。**兩件試驗之結果決定工法**：x14 存活→openpyxl 直寫可行；不存活→改提案「XML 手術式」（zip 解包、直接改 `sheet1.xml` 之 `<c>` 節點、原樣回封，不經 openpyxl save）或其他，提案附可行性實測。

**W-3 列對應方案**：b1 凍結檔表（34 檔 sha8）↔ 工作簿列之對應規則提案：D 欄（Source Requirement ID）＋F 欄（TC ID `NR1L-VSM42-{n:03d}`，本包一併提案 b1 之起始編號＝001 起依 INDEX 序）＋凍結 sha8 記於何處（建議 Remarks 不記 sha、對應表落 `data/writeback_map_b1.tsv`）。欄位映射逐欄列（`feature.yaml` columns 21 鍵 → 十鍵＋固定值欄），固定值欄（Author=PeiPYHsu 等）依 DECISIONS。

**W-4 lint 首跑預演**：以 W-2 之假資料試驗件跑 `lint036.py --profile vsm_v42`（首次可實跑），輸出全文上繳——文字形自檢未涵蓋而 lint 會抓的項先現形。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E69 | W-2 斷言 | 兩件試驗各附 zip member 數與 x14 節點 XML 證據 |
| E70 | `sandbox/base/` | 一位元不動（cmp） |
| E71 | 工法提案 | 附可行性實測，非紙上提案 |
| E72 | lint 首跑 | 輸出全文＋逐紅歸因 |

## 三、上繳（`docs/upstream/09_writeback_method.md`）

盤點表；兩件試驗證據；工法提案（單一建議案＋備案）；列對應與 TC ID 提案；lint 首跑；E69–E72；gate_all 歸因。**分析層覆核＋Pei 授權後，方有寫回執行包。**
