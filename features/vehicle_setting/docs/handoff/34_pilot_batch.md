# 34 下放包 — R-VS19″ 更正、驗證凍結、17 輪＝首批生成

分析層寫入，2026-08-20。Pei 指示「我需要加快速度」。

---

## 0. 速度診斷（分析層自評）

| 量 | 值 |
|---|---:|
| 已進行輪次 | 16 |
| 已產出 TC | **0** |
| 已立條文 | R-VS1～R-VS39（＋′ 版）約 45 條 |
| 已登記 anomaly | 55 |

**主因在分析層**：幾乎每輪覆核都立新條文，而每條新條文都衍生新驗證作業
（R-VS27 → W-19；R-VS32 → 重跑；R-VS37 → W-46；R-VS38/39 → W-50…）。
**驗證在驗證自己的驗證**，而交付物一列未寫。

前置條件之實況（本輪已全綠）：

| 前置 | 狀態 |
|---|---|
| 母體 237 | ✅ 檔界 0 / 237 不一致（W-52） |
| Layer 1／2 | ✅ 四數 46／88／72／31 相符 |
| Layer 3 | ✅ R-VS37′ 判定完成 |
| N 欄 reqid | ✅ 236 / 237（1 筆 DR-11） |
| 訊號名寫法 | ✅ R-VS9(1)′ ＋ L-VS2 |
| 值域來源 | ✅ R-VS20 ＋ R-VS39 |
| 委派 | ✅ R-VS7(a)′（群層級） |

**沒有任何前置在擋首批生成。** 阻塞只及於特定 leaf：

| DR | 影響 leaf | 影響什麼 |
|---|---:|---|
| DR-15 | 160（Heated 88 ＋ Vented 72） | 請求訊號之分支結構與設計方法 |
| DR-17 | 14（OneStageHeatedSeat） | 委派界線 |
| DR-14′ | 16（`$HdRstRelRq$` 引用者） | 訊號讀取途徑 |
| DR-11 | 1 | N 欄 |

**Common Features 46 個 leaf 中，扣除 `$HdRstRelRq$` 相關者，
仍有一批完全無阻塞** —— 首批應自此出。

---

## 1. R-VS19″ —— 我的條文自相矛盾，更正

執行層指出 R-VS19′ 主文與 (a) 段互斥，且 (a) 段之括號
「（即 `Radio`／`ECU` 判準不通過者）」在資料上不成立
（實測 270 條為他架構專屬**且**通過判準）。**指摘完全正確，是分析層之起草缺陷。**

**原意為讀法一。** 13 輪之證據**只證明 `Atlantis Mid` 不應排除**
（其章節自稱 `applicable for R1 Low`、三屬性與無 Mid 組 100% 一致），
**未證明 `CUSW`／`PowerNet` 亦應納入**。

且執行層本輪提供之旁證強化此讀：**251 個已覆蓋條文中，
`CUSW`／`PowerNet` 專屬者為 0** —— 037 從未引用任何純 CUSW／純 PowerNet 條文。

```
R-VS19″（分析層更正 2026-08-20，取代 R-VS19′ 全文；Pei 得推翻）
CFTS044 條文之適用性判準為：

  in-scope ⟺ `Artifact Type` 含 `Subsystem Functional Requirement`
             ∧ `ECU` ∩ {LTM, ETM, RRM} ≠ ∅
             ∧ （`Radio` 為空 ∨ `Radio` ∩ {R1L, R1L-R} ≠ ∅）
             ∧ **NOT（`EE Architecture` ⊆ {CUSW, PowerNet}）**

即：`EE Architecture` **仍為排除判準，但僅排除 `CUSW`／`PowerNet` 專屬者**；
`Atlantis Mid` 不再排除。

R-VS19′ 主文之「`EE Architecture` 降為輔助資訊，不作為排除判準」
**為誤，撤回**。其 (a) 段括號內之等式亦誤，撤回。

依據：
 (1) 13 輪之證據範圍僅及 Atlantis Mid（`4859399`／`4859463` 自稱
     applicable for R1 Low；三屬性與無 Mid 組 100% 一致）
 (2) 16 輪實測：251 個已覆蓋條文中 CUSW／PowerNet 專屬者 **0**；
     其分布為 Atlantis Mid 121／AH+PN 112／Atlantis High 14／All 4
 (3) 讀法一之 (a) = 0，母體 237 完整；讀法二之 43 條全為 PowerNet 專屬，
     若納入則須向上游解釋為何 037 從未引用任何 PowerNet 專屬條文

**定案數字（讀法一）**：
  全文 in-scope 425／21 章節內 259／未覆蓋 8／覆蓋率 96.9%／
  已覆蓋 reqid 落外 0／(a) 類 0
**A-VS55 依本條關閉。43 條不歸因，其為 out-of-scope。**
```

---

## 2. R-VS40 —— 驗證凍結（分析層裁定）

```
R-VS40（分析層裁定 2026-08-20）
自 17 輪起，未結之驗證項一律凍結為 backlog，**不排入輪次**，
除非其滿足下列任一：

 (a) pilot review 發現之缺陷可追溯至該項
 (b) 其阻塞某個具體 leaf 之 TC 內容（須具名該 leaf）
 (c) Pei 指定

現行凍結項（`docs/reports/BACKLOG.md`，執行層本輪建檔）：
  `normalized_key` 之基欄未涵蓋 exclude／other_arch／lid／dbc（14 輪 §6-1）
  `$HSW_StatFailSts$` 之階梯重查（14 輪 §6-2）
  `1.3.1.1.3` 上位節與 `1.3.1.1.*` 其他分節未掃（14 輪 §6-3）
  四檔 id 互斥未逐 id 驗（14 輪 §6-4）
  A-VS41／A-VS48／A-VS35／A-VS36 等 FYI 類
  W-17 之 LID 列數差 6、`TRUNCATED_ENUM` 其他形態
  A-VS37 之 102 上界

**同時凍結分析層之立條**：自 17 輪起，覆核每輪至多立**一條**新條文，
且僅在其**會改變已生成或待生成之 TC 內容**時才立；
其餘發現一律登記 anomaly 後入 backlog。

理由：16 輪、0 TC。驗證之邊際收益已低於其輪次成本，
而 pilot review 是唯一能揭露 TC 內容層缺陷之關卡（canon §1.2），
其至今未曾啟動。
```

---

## 3. 17 輪指令 —— **首批生成**

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  docs/runtime/ASPICE_SWE6_AI_Instruction.md                **TC 內容規則（本輪起適用）**
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/framework.md                      Layer 1–3
  features/vehicle_setting/docs/handoff/34_pilot_batch.md    本輪依據（本檔）

## 文書

D-1  依 R-VS18 建立 docs/upstream/15_pilot_batch.md，六節先留空。
D-2  逐字轉錄 34 包 §1 之 **R-VS19″** 與 §2 之 **R-VS40** 入 RULINGS.md；
     R-VS19′ 標「經 R-VS19″ 取代」（保留原文，不刪）。A-VS55 關閉。
D-3  建 docs/reports/BACKLOG.md，登錄 R-VS40 所列之凍結項。
D-4  以 R-VS19″ 之定案數字更新 framework.md 之阻塞項第 1（已解）。

## 作業（**一項**）

W-53  首批 TC 生成 —— **10 個 TC**

      選 leaf：自 Layer 2 = `Common Features` 之 46 個 Functional leaf 中，
      **排除**下列者後，依 `leaf_to_reqid.tsv` 之 reqid 升冪取前 10：
        - 引用 `$HdRstRelRq$` 者（DR-14′）
        - `delegate = pending` 者（DR-17）
        - `delegate = blocked` 者（R-VS17）
        - reqid 為空者（DR-11）
      **實際選出者不足 10 時，取全部並回報其數**。

      每個 TC 依 canon §4～§12 產出十鍵，並套下列本 feature 條文：
        test_item   上半段＝037 Requirement Description 逐字；
                    下半段＝作者自訂，**全部置於括號內**（R-VS6）
        pre_cond    狀態／環境，一條件一行（R-9）
        input_data  一律 `NA`（R-VS5）
        procedure   訊號斷言須 `<signal> in <message> on <網段>`（R-VS9(3)）；
                    signal 拼寫取 DBC 逐字（R-VS9(1)′）；
                    `$var$` 不得出現於此欄（R-VS9(5)）
        ER          值取 DBC `VAL_` 逐字（R-VS39）；無模態動詞（§6）
        spec_ref    `CFTS044-<7位數>`，多值升冪（R-VS33′／R-VS14）
        reasoning   繁中 2–5 句；委派句指名功能群並註明群層級（R-VS7(a)′）

      **不寫回工作簿**（write-back 屬 Pei）。輸出至
      `features/vehicle_setting/generated/batch01.json`。

      自檢：canon §9 之十七項逐項列出通過與否，**不得只寫「已自檢」**。

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
**不寫回 036 工作簿。不鎖定 framework。**
**不執行任何 backlog 項**（R-VS40）。

## 升級條件

選出之 leaf 不足 10；
某 leaf 之 TC 無法在不違反 §8.4.1 之下寫出（具名該 leaf 與缺何值）；
canon §9 自檢有項目不通過而無法修正。

## 完成後

首批送 **pilot review**（canon §1.2，Pei 之必要人工關卡）。
```

---

## 4. 待 Pei（**三項，皆可今日完成**）

| # | 事項 | 為何現在做 |
|---|---|---|
| **P19** | **framework 簽核** | W-52 已 0 / 237 不一致；未解項掛在條文上，不必擋在門口 |
| — | **DR-15／DR-17／DR-18 一次送出** | 三份皆已定稿。DR-15 影響 160 leaf，其答覆之前置時間最長，**越早送越不擋** |
| — | 追認 **R-VS19″**（§1）與 **R-VS40**（§2） | 一句話即可；不追認亦依此執行 |

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS19″ | 適用性判準：架構仍排除 CUSW／PowerNet 專屬者，Mid 不排除 | 分析層更正（Pei 得推翻） |
| R-VS40 | 驗證凍結；分析層每輪至多立一條新條文 | 分析層 |
