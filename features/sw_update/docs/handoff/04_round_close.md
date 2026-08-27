# 下放包 04 —— 本輪收束（A-SU2 結案、R-SU7 v2、spec_mode 回填）

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`03_review_rulings.md`；對應上繳：`docs/upstream/03_round_close.md`
- 裁定狀態：待裁 1、2 —— **Pei 2026-08-27 准**；待裁 3 —— 分析層裁

---

## 一、處分

### 1.1 A-SU2 —— RESOLVED（處分文逐字入 ANOMALIES.md）

```
A-SU2 處分（2026-08-27，Pei 准）：

形態面：R-SU5 v2 已結（上繳包 02 §二核對 OK）。

家族面：**VF747 不立為第三錨點家族**，R-SU5 v2 (a) 對 (iii) 之
「暫行維持」轉**確定維持**。依據：T11 三項獨立事實同向 ——
(a) 在手 VF747_V1_R3 無 Polarion 物件宣告、(b) 無任何 7 位
ObjectID、(c) 037 引用 V2／V6 與在手 V1_R3 為不同大版，
10/10 目標 id 於全文 0 命中（上繳包 02 §一 T11、§三）。

該 10 列（SWE1-FOTA-225, 226, 227, 228, 230, 239, 240, 241, 242,
243）之 spec_reference 於 Phase 2/3 錨定時走既有兩家族
（R-SU4 v2 (a)(b)）；屆時仍無錨可落者，個案依 IN §8.4.3 掛
PENDING 並發 DR。

休眠線索（記錄即止，不納素材、不開檔、不發 DR）：
`~/Work/02_Project_R1LR/9_ASPICE/SYS.1 Requirement Elicitation/
SYS1_VF_with source ID/HDCC27/VF747_V1_R3_PHDCC27.xlsx` 及
`SYS1_DT27_VF_Diff_HDCC27/VF747_V1_R3_PDT27_DiffHDCC27.xlsx`。
若上述個案 DR 發生，優先向此線索取 V2／V6 對應之 export，
屆時為新素材、新登記。
```

### 1.2 R-SU7 v2（抄入 RULINGS.md，逐字，append 於 R-SU7 之後）

```
R-SU7 v2（CFTS_57 之 Description 物件 —— 統計數依 T12 分類法修正）

（Pei 2026-08-27 准統計數更正。）

上繳包 02 T12 實測：T10 之「首見為準」分類法將 11 個帶
`[Artifact Type:…]` 宣告之 id 誤歸「不可歸類」；改採
**宣告優先於文序**後：

  錨點池 = **574**（章節物件 87 + 需求物件 **487**）
  Description 物件 = **137**（歸需求 45、歸章節 92、不可解 **0**）
  不可歸類 = 10

v1 之 565／478／135 為分類法缺陷下之值，撤銷；成因為量測法
修正，非素材變動（素材 sha 不變）。兩路獨立計數閉合：
87 + 487 + 137 + 10 = 721 = 裸命中 unique 總數。

其餘不變：Description 不入池；其內容被取用時錨落所屬需求／
章節物件，對照表見 `ANCHOR_POOL.md` §六（137/137 可歸，
空表確認）。

沿革：v1 見下放包 03 §二 2.2；更正依據上繳包 02 §一 T12。
```

### 1.3 spec_mode（分析層裁，待裁 3）

`spec_mode: [A, B, D]`（list 形態，projection 前例）。T13 之逐條核對
採認為裁定依據；B 之「文字管線成立、reference 形態不採」之部分成立
判定照納（reference 形態由 R-SU4 v2 專管，不因 B 成立而動）。
`feature.yaml` 之待裁註銷除。intake.py `propose_spec_mode()` 單值
結構限制**不立案**（FO §3 組合由人判定，函式未逾其職 —— 採認
上繳包 02 之判斷）。

---

## 二、任務

| # | 任務 |
|---|---|
| T15 | 抄錄：A-SU2 處分文（§1.1）入 ANOMALIES.md、A-SU2 → RESOLVED；R-SU7 v2（§1.2）append 入 RULINGS.md（R-SU7 v1 不刪不改）。程式回讀逐字元核對法照舊 |
| T16 | `feature.yaml`：`spec_mode: [A, B, D]` 回填、撤待裁註；重跑 `scripts/recon.py` 使 `DECISIONS.md` 重生，assertions 須維持 2/2 PASS，回報全輸出 |
| T17 | PLAYBOOK.md 教訓節錄入（上繳包 02 自評 #1）：「分類型產出應對每一類都有一路獨立計數，不能只驗最好驗的那類」——註明出處（上繳包 02 §六，T10/T12 案例） |

---

## 三、上繳包要求（`docs/upstream/03_round_close.md`，小包）

1. T15–T17 逐項結果（含核對表與 recon 全輸出）
2. RULINGS.md／ANOMALIES.md 之最終條目序與狀態表
3. 未結 DR 清單（應仍空）
4. 獨立自評（每包必答）

本包收束後，Phase 0/1 全結。下一輪 Phase 3：framework 起草由分析層
發包（Layer 1/2 自 spec TOC ∩ 037 分群交集起草、Layer 3 對 spec
章節，IN §4.1），執行層屆時配合量測。
