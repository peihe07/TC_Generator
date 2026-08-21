# 33 下放包 — P18／P20 裁定（R-VS7(a)′、R-VS19′）與連帶重算

分析層寫入，2026-08-20。Pei 指示「裁決就照你的建議」。

---

## 1. 裁決正文（執行層逐字轉錄入 `RULINGS.md`）

### 1.1 R-VS19′

```
R-VS19′（Pei 2026-08-20，取代 R-VS19 之排除段）
CFTS044 條文之適用性判準為：

  in-scope ⟺ `Artifact Type` 含 `Subsystem Functional Requirement`
             ∧ `Radio` 含 `R1L` 或 `R1L-R`（欄為空者視為不限）
             ∧ `ECU` 含 `LTM`／`ETM`／`RRM` 之一

`EE Architecture` **降為輔助資訊，不作為排除判準**。

依據（13 輪 W-42 實測）：
  純 Mid 118 條與無 Mid 127 條，於 `Radio`／`ECU`／`Market` 三屬性
  100% 一致（各組皆 118/118、127/127 含 R1L／R1L-R 且 ECU 為頭端）；
  純 Mid 之 `4859399`／`4859463` 全文逐字為
  `The requirements in this section are applicable for R1 Low only
   from SR22 and beyond.`
  —— 標記 `Atlantis Mid` 之章節自身宣告適用於 R1 Low。
  架構標籤反映條文之來源沿革（自 Atlantis Mid 遷入），非適用範圍。

推論（binding）：
(a) R-VS19 之「他架構條文之值域一律不取用」**縮限為 `CUSW`／`PowerNet`
    專屬者**（即 `Radio`／`ECU` 判準不通過者）；`Atlantis Mid` 不再排除。
(b) R-VS20 第一階之範圍隨之擴大：112 個純 Mid leaf 之值域
    **得自其自身 CFTS044 條文取得**，不必落至第二階。
(c) 先前以舊判準算出之 in-scope 數（1,128／294／169／39／76.9% 等）
    **全部失效**，須以新判準重算。
(d) `$HSW_StatFailSts$` 之 R-VS20 階梯歸屬須重查 ——
    其 Atlantis Mid 條文若入 in-scope，第一階即有值。
(e) R-VS19（原條）保留於 `RULINGS.md`，加註「排除段經 R-VS19′ 取代」，
    不刪除（R-TM13）。
```

### 1.2 R-VS7(a)′

```
R-VS7(a)′（Pei 2026-08-20，修訂 R-VS7(a) 之委派句要求）
委派句改為指名**功能群**（Layer 3）而非單一 Comfort leaf id。

reasoning 之委派句形如：
  「加熱方向盤之畫面行為由 Comfort 擁有，見 SWE1-HVAC-062／063／…
    （群層級，Layer 3）」
並須註明其為群層級。

依據（14 輪 W-44 實測）：
  完全收斂 **0 / 174**；階數與側別兩維度用盡後，每列仍餘 5～8 個
  Comfort leaf；剔除 24 個泛用 id 後仍餘 5／7／8。
  逐 leaf 指名在現有資料上不可達。

R-VS7 之其餘各段（(a) 之委派原則、(b) 之例外、(c) 之佐證）不變；
R-VS7(b) 對同一 leaf 仍優先於 (a)（26 包 §1 之讀法）。
```

---

## 2. 連帶重算 —— 併入 16 輪，不另開輪次

R-VS19′(c) 使多輪之數字失效。**該重算不是新面向，是既有數字之維護**，
故不佔 R-VS25 之三項名額，列為 D-5。

```
D-5（文書兼重算，16 輪執行）
以 R-VS19′ 之新判準重算下列各數，逐項列出「舊值 → 新值」：

  (1) CFTS044 全文之 in-scope 條文數      舊 1,128（27 包）／294（12 輪）
  (2) 21 章節內之 in-scope 條文數          舊 169
  (3) 其中未被 037 leaf 覆蓋者             舊 39 → 11 輪歸因後 (a)=0
  (4) 覆蓋率                               舊 76.9%
  (5) 251 個已覆蓋 reqid 是否全數仍在新 in-scope 內
      —— **任一落外即升級**（同 W-39(2) 之範圍向）

**(3) 之重算須重跑歸因**：新判準納入之條文中，
若有未被任何 037 leaf 覆蓋者，其 (a)／(b)／(c) 分類須重做。
**(a) 類非 0 為升級條件** —— 其表示母體 237 在新判準下不完整。
```

**注意**：R-VS19′ 之後，「母體 237 完整」此一結論**回到未證狀態**。
11 輪之 (a)=0 係在舊判準下得出；新判準納入更多條文，
**其中是否有 037 未涵蓋者，未知**。

---

## 3. 對 W-51 之影響

32 包 §5 之 W-51 原註「本輪只取證，不依任一版判準排除任何條文」——
**P20 已裁，該限制解除**。

`1.3.1.1.3.*` 四節之適用性改依 R-VS19′ 判定：
其條文若 `Radio` 含 R1L／R1L-R 且 `ECU` 為頭端，即 in-scope，
**不因其標記 `CUSW` 而排除**（R-VS19′ 之排除僅及於判準不通過者）。

**W-51 之產出須列出該四節逐條之 `Radio`／`ECU`／`EE Architecture` 三欄**，
以供判定；並列「依 R-VS19′ 為 in-scope 者幾條」。

---

## 4. 16 輪指令（取代 32 包 §5）

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/32_review_round15.md 前輪覆核
  features/vehicle_setting/docs/handoff/33_rulings5.md       本輪裁決（本檔）
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/14_normalization_and_lock.md，六節先留空。
D-2  逐字轉錄入 RULINGS.md：
       32 包 §1 之 R-VS38、§2 之 R-VS39
       33 包 §1.1 之 R-VS19′、§1.2 之 R-VS7(a)′
     並將 R-VS19 標「排除段經 R-VS19′ 取代」、
     R-VS7(a) 標「經 R-VS7(a)′ 修訂」（保留原文，加註，不刪）。
D-3  ANOMALIES.md：A-VS54 依 R-VS38 關閉；A-VS53 併入 A-VS05
     （加交互參照，兩者皆保留）。依 R-VS35 列兩數。
D-4  DATA_REQUESTS.md 新開 DR-18（32 包 §3 全文），
     Urgency Medium、確認型不阻塞。**不送出。**
D-5  依 33 包 §2 重算五項，逐項列「舊值 → 新值」。
     **(5) 任一落外、或 (3) 之 (a) 類非 0，即升級。**

## 作業（三項，R-VS25）

W-50  值域正規化與剩餘 token 之污染掃描
      (1) 依 R-VS39 增 `normalized_key` 欄，保留全部原始寫法；
          列「原始相異值數」與「正規化後相異值數」逐 token 對照
      (2) 16 個無語意前綴 token 改以**反向判準**掃描：
          其值中是否出現他 token 之語意前綴（`HS_`／`VS_`／`HSW_`）
      (3) 大小寫重複對**全部 30 個 token** 重量，列出受影響者

W-51  CUSW 遷入節族之逐位對照（依 R-VS19′ 判定其適用性）
      `1.3.1.1.3.*` 四節逐位對照，比對引用狀態與方括號值之對稱性。
      **不得用 difflib**；值抽取條件**不分大小寫**。
      **併列該四節逐條之 `Radio`／`ECU`／`EE Architecture` 三欄**，
      並列「依 R-VS19′ 為 in-scope 者幾條」。

W-52  framework 鎖定前之最後驗證
      (1) **逐 leaf 驗證 Layer 2 歸屬**：改以「該 leaf 出自哪一份 037 檔」
          逐筆核對，列出不一致者
          （待驗：`CrossZone Common` 之 2 leaf 歸 `Heated Seat` 一事）
      (2) 更新 `framework.md` 之鎖定前未解項清單，逐項標阻塞／不阻塞
          與所待之 DR 編號
      (3) **framework 仍不鎖定** —— 鎖定屬 Pei（P19）

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
不得合併或改寫 `spec_variables.tsv` 之原始值（R-VS39 僅增欄）。
不得鎖定 framework。

## 升級條件

D-5(5) 之 251 個已覆蓋 reqid 有任一落在新 in-scope 之外；
D-5(3) 重跑歸因後 (a) 類非 0；
W-50(2) 之反向掃描有命中；
W-50(3) 之大小寫重複影響 `$VentedSeat*$` 以外之 token；
W-51 出現與 Vented／Heated 兩節皆不同型之不對稱；
W-52(1) 之 Layer 2 歸屬有不一致；
實測與 32／33 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。
```

---

## 5. 待 Pei（**現僅二項**）

| # | 事項 | 狀態 |
|---|---|---|
| P19 | framework 簽核 | 俟 W-52 之未解項清單 |
| — | **DR-15／DR-17 送出**（阻塞型）、DR-18（確認型） | 三者皆已定稿未送 |

**P18／P20 已裁，無其他待裁條文。**

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS19′ | 適用性判準改以 `Radio`＋`ECU`；架構標籤降為輔助 | Pei |
| R-VS7(a)′ | 委派句改指名功能群（Layer 3） | Pei |
| D-5 | R-VS19′ 之連帶重算五項 | 分析層 |
