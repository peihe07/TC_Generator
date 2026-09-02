# 下放包 08 — vsm_v42：-059 一列（R-VL23 A 路）→ b1 凍結

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–07，取 08
台帳不重生；DR 不送；不寫工作簿。

## 一、唯一修訂

**-059**：test_item 上半改 037 Requirement Description **完整原句 verbatim**（含 ignition 子句與 `| (Ignition_{S}tatus)`，上繳 07 第 4 節已備之修法照施）；括號下半、Procedure、ER、PENDING、reasoning／remarks 之未涵蓋揭露**皆不動**（上半變更若使 reasoning 之敘述不再對應，僅允許補一句「上半為完整原句，ignition 分支未涵蓋見 remarks」）。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E62 | 修訂檔數 | 2（-059 之 json＋md）；其餘 32 檔 diff = 0 |
| E63 | E56 重跑 | **17/17**（機讀子字串斷言 True） |
| E64 | E38–E45／E53–E55 重跑 | 全過 |

## 三、凍結

E62–E64 全過 → INDEX 記 **`b1 FROZEN (R-VL23)`** 並列凍結時之檔數／sha 摘要（逐檔 sha256 前 8 碼表）。上繳 `docs/upstream/08_freeze.md`（極簡：diff、三 E、凍結表、gate_all 歸因）。
