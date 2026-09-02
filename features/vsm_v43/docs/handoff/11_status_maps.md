# 下放包 11 — vsm_v43：R-VT23 落地（隔離標記、占比重算、1.14 對映）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–10，取 11
台帳不重生；DR 不代發；不寫工作簿；已凍 b1 不動。

## 一、W 清單

**W-1 標記落地（R-VT23(a)(b)(c)）**：`leaves_interim_v2.tsv` 加 `status` 欄——`active`／`superseded`（`-472`/`-473`，superseded_by_r4.tsv 擴至 5 列並補 R4 逐字依據）／`deprecated_r4`（`-577`〜`-582`、`-844`、`-824`、`-825`）／`stale_ref_r4`（`-897`/`-899`/`-907`，附「被刪條件子句生成時不入 TC」註）。對帳：active 325＋stale_ref 3＋superseded 2＋deprecated 9 ＝ 339？——**以實測為準逐項列**（superseded 原 3 列已不在 v2，勿重複計；算式自行對齊並報，E82）。

**W-2 Layer 2 v2 表落 framework**：依 R-VT23(d) 之 19 組（Side Distance Warning 10／PROXI Configuration 65 等）以 status=active＋stale_ref 之列實測各組數，寫入 framework.md v2 表（R-VT19 表不刪只標）；合計 = active＋stale_ref 實測值（E83）。**表直標「鎖定 (R-VT24)」（Pei 已准）**；實測與 R-VT23(d) 預期不符者回報不自調。

**W-3 占比重算（R-VT23(e)）**：對 active＋stale_ref 列，詞界式重掃含 v5 訊號名／含解得二數與占比；分組分布表更新（E84）。

**W-4 `1.14.*` 對映**：規格組態節（para 1287 起之 Configuration Parameters 區）逐參數列 token ∩ `01.14.01`／`01.14.02.01.*` 各列 token（詞界式）；輸出對映表與無對應清單；不硬配（E85）。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E82 | status 四類對帳 | 逐類列數＋算式自洽；已凍 b1 之 10 列全為 active |
| E83 | Layer 2 v2 合計 | = active＋stale_ref 實測 |
| E84 | 占比 | 新舊二數並列（v1 43% 對照） |
| E85 | 1.14 對映 | 覆蓋數／無對應清單 |

## 三、上繳（`docs/upstream/11_status_and_maps.md`）

E82–E85；framework v2 表全文（待 Pei 准）；獨立判斷；gate_all 歸因。**Pei 准表後即出 b2 生成包（批次序屆時提案）。**
