# 下放包 04 — vsm_v42：P3 —— framework 落地、Layer 3 章節號回填、W-5 收尾落地、DECISIONS 簽核準備

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–03，取 04
對象：執行層。00–03 包續有效。sha8 報 body_sha8；台帳不重生（R-VL13，Pei 已追認）；DR 一律不送。
本包新落檔（分析層）：`framework.md`（R-VL17 鎖定本）、`docs/runtime/profiles/FW036_R1L_VSM_V42_Profile.md`。
**profiles/ 仍為執行層禁區** —— 讀可、寫不可。

---

## 一、上繳 03 覆核之落地事項（條文已裁，本包執行）

| 裁 | 落地 |
|---|---|
| R-VL15(a) K-1 改判 | `signal_chain_v42_v3.tsv` 之 `LanguageSelection_Req` 列改「解得」（目標欄逐字），備註記 Sts 孪生 `IPC_VEHICLE_SETUP.LanguageSelection`；B-1 → 0 |
| R-VL16(a) 拼字值域 | 掃 v3 全表：段 3 查無而正確拼法存在者改記 `未解得（規格拼字疑誤）`（上繳 03 已知 `RestoreDefaulSetting`／`RestoreDefaultSettimgReq` 兩列，另全掃一次） |
| R-VL16(b) 非 CAN 形審計 | 「解得」中 Req 1／Info 1／PROXI 1 三列逐列出段 1 依據；無者退回「未解得(止於段1)」。輸出 v3 就地更新（本包例外准就地改 v3，diff 逐列上繳） |
| R-VL16(c) | `PassiveEntry` 二列備註補 R-VL16(c) 引註 |
| A-VL11 | RESOLVED（R-VL14 加註）；ANOMALIES 狀態行更新 |

## 二、作業清單

**W-8 Layer 3 章節號回填**：自 `sources/extracted/vf665_v42_spec_r6/document_paragraphs.tsv` 取標題層級段（heading style 或編號式 `n.n(.n)` 起始段），對映 24 家族 → 規格章節號；回填 `framework.md` 表尾欄（**只填該欄，不動其他**；str_replace 逐列）。對映不上的家族列「未對映」並上繳，不硬配。

**W-9 forms 三件 xlsx 登錄**（FORMS.md 末節指派）：HMI Settings List R1 SR25／SR24 Market Config v1.6／SR26 Default Settings v1_0 各補 (a)–(f)（sha256、涵蓋以 W-5 實測事實填、(f) 首個採用 = vsm_v42,vsm_v43）。寫入 `forms/FORMS.md`（本包例外授權此一檔；格式照既有條目）。

**W-10 DECISIONS 簽核準備**：`DECISIONS.md` 依 recon 預填本補齊四欄實值（spec_mode D、workbook BLANK、母體 128、框架 R-VL17），標「待 Pei 簽」。**不代簽。**

**W-11 leaves.tsv 加 Layer 2 欄**：每 leaf 依 framework.md 對映 `test_set` 欄；合計對測（18/10/11/21/13/5/15/17/14/4 = 128）。

**W-12 P4 預備（只建表不生成）**：
- `data/val_tables_v42.tsv`：解得各列之 VAL_ 逐值（raw → label，逐字取 DBC）；
- `data/ba_sendtype_v42.tsv`：解得各列之 `GenSigSendType`／`GenSigStartValue`（BA_ 屬性，Procedure 之 Send／Hold 寫法參考）。

## 三、預期數字

| # | 項 | 判準 |
|---|---|---|
| E32 | v3 更新後 B-1 | 0 |
| E33 | v3 更新後「解得」 | 95 ＋ 審計存活數（觀測；≤ 98） |
| E34 | W-11 十組合計 | 逐組 = framework 表，總 128 |
| E35 | W-8 已對映家族數 | 觀測（未對映者列名） |
| E36 | R-VL12–R-VL17 body_sha8 | 與 RULINGS.md 現檔一致（樹外 --out） |
| E37 | VAL_ 表列數 | = E33 之解得數 |

## 四、上繳要求（`docs/upstream/04_p3_framework.md`）

W-8～W-12 逐項；v3 就地更新之逐列 diff；E32–E37；FORMS.md 三條目全文；A／DR 狀態；獨立判斷；gate_all（rulings_hash 紅記「依 R-VL13 待 Pei 重生」）。

## 五、升級條件

E32 ≥ 1；E34 任一組不合；W-8 需語意猜測方能對映（列「未對映」，不猜）；framework.md 除 Layer 3 欄外任何變動。

## 六、未結 DR（皆 Pei 裁先不送）

DR-VL1（191 列揭露）／DR-VL2（標註三面）。DR-VL3 已結案。
