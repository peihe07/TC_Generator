# 58 下放包 — Priority 判準之定義（R-VS56）

分析層寫入，2026-08-22。Pei 指示「照交付本，Priority 需要去定義」。

---

## 1. 自交付本枚舉之事實

`SWQT_SWC_20260708.xlsx`，286 條：**P0 27／P1 190／P2 68／空 1**。

**(1) Priority 不由 Test Set 決定** —— 同一 Test Set 橫跨三級：

| Test Set | P0 | P1 | P2 |
|---|---:|---:|---:|
| Volume | 8 | 22 | 4 |
| Seek | 4 | 24 | 6 |
| Preset | 1 | 19 | 5 |
| IPC Audio Controls | 1 | 19 | 9 |

**(2) P0 之分布集中於核心使用者功能**：
Volume 8／Phone Answer 7／Seek 4／Voice Recognition 4／
Audio Mode Advance・Preset・Mute・IPC Audio Controls 各 1。

**(3) P2 之最大宗為 `Diagnois and Timing`（30 / 68）** —— 診斷與時序。

**(4) 三級之 test_item 文字形態相同**（皆 `HW supplier shall notify the
$X$ signal via the VHAL interface…`）—— **故判準不在條文措辭，在其驗證標的**。

**與 canon §10.2 之對照**：交付本之 P0 集合（音量／接聽／選台／語音）
落在 §10.2 之 `audio output`、`connection`、`eCall` 三類內。
**交付本忠實套用 canon §10.2，未另立判準。**

---

## 2. 本 feature 之 P0 為 0 —— 追因

現況 P1 64／P2 12／**P0 0**。

canon §10.2 之 P0 七類（safety／boot-recovery／connection／audio output／
eCall／vehicle-critical CAN signal／data-loss risk）中，
本 feature 觸及者僅 **`vehicle-critical CAN signal`** 一類，
而該類之判定從未於本 feature 定義過 —— **P0 = 0 是判準缺席之結果，不是判定結果。**

---

## 3. R-VS56 —— Priority 判準（待 Pei 追認）

```
R-VS56（**Pei 追認 2026-08-22**）
本 feature 之 Priority 依 canon §10.2 之七類判定，
其於 Vehicle Setting 之操作型定義如下。**逐 TC 判定，不由 Test Set 決定**
（交付本實證：同一 Test Set 橫跨三級）。

**P0 —— 二類**
 (a) **實體致動且具傷害可能者**
     第三排頭枕下放（`ThirdRowHeadrestDump`）之致動行為 ——
     其驅動實體機構且乘員可能在其行程內。
     **限致動本身**；其軟鍵之顯示／灰階屬 P1。
 (b) **加熱元件之啟用與其失效狀態**
     加熱座椅、加熱方向盤之「開啟」與 `*_STATFailSts = Fail_Present`
     之處置 —— 其為熱源，失效未被反映即有燙傷可能。
     **限開啟與失效**；階數之顯示同步屬 P1。

**P1 —— 主要功能邏輯**
 狀態訊號之顯示同步、階數切換、喚醒初始化、
 LHD/RHD 之標籤與圖示、Stop-Start 之開關可用性、配置相依之控制項有無。

**P2 —— 次要與診斷**
 無效值之忽略、SNA 之處置、時序（`<Tsend>`／`<Tdisplay>`）、
 前言型與適用性條件之驗證。
 **交付本之 `Diagnois and Timing` 佔 P2 之 44%，本 feature 之對應即此類。**

**P3 —— 不使用。** 交付本 286 條中 P3 為 0；本 feature 亦不設。

**判定之記錄要求**：每條 TC 之 `reasoning` 須記其 Priority 所依之類別
（如「P0(b)：加熱元件失效狀態」），使其可覆核。
```

---

## 4. 依 R-VS56 之重判規模（估計，須實測）

| 級 | 現況 | 依 R-VS56 之預期 | 依據 |
|---|---:|---:|---|
| P0 | 0 | **約 8–14** | 頭枕致動（`ThirdRowHeadrestDump` 之致動類）＋ 加熱開啟／失效 |
| P1 | 64 | 約 50–56 | 其餘主要功能 |
| P2 | 12 | 約 12–14 | 無效值忽略（現有 5 條 `Negative / Invalid`）＋ 時序 |

**此為估計，非實測** —— 逐條重判屬 W-101。

---

## 5. 併入 36 輪之作業（**取代 57 包 §5 之 W-99**）

W-99（`ThirdRowHeadrestDump-038` 之退回）併入 W-101 一併執行。

```text
（取代 57 包 §5 之 W-99）

W-101 **Priority 之逐條重判 ＋ design_method 對齊 ＋ -038 退回**
      (1) 依 **R-VS56** 逐條重判 76 條之 Priority；
          每條之 `reasoning` 補記其所依類別（如 `P0(b)`）
          **必列**：重判前後之三級計數與逐條變動清單
      (2) 依 57 包 §4 之一對一對照，`design_method` 對齊交付本之
          **受控值域**（`中文 (English)` 形態，9 值）：
            State Transition        → 狀態轉換 (State Transition Testing)
            Decision Table          → 決策表 (Decision Table Testing)
            Functional Based        → 功能測試 (Functional based ; no specific technique)
            Equivalence Partitioning→ 等價劃分 (Equivalence Partitioning, EP)
            Negative / Invalid      → 負向測試 (Negative / Invalid)
          **錨點（R-VS54）**：對齊後，凡值不在該 9 值內者須被檢出；
          以對齊前之版本為必命中之對照
      (3) `ThirdRowHeadrestDump-038` 依 57 包 §3.3 退回記錄形態
      各批次產 `_v{n+1}`，原版保留。重跑 §9 自檢 ＋ 錨點。
```

---

## 6. 待 Pei

| 項 | 內容 |
|---|---|
| **R-VS56 之追認** | **已追認（Pei 2026-08-22）** —— P0 二類為分析層依 canon §10.2 所推導，非交付本明載，此一來源差別須於 `reasoning` 中保留可追 |
| **DR-25**（33 leaf，High） | 57 包 §2，最急 |
| 其餘八份 DR | 待送 |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS56 | Priority 依 canon §10.2 之七類，逐 TC 判；P0 二類具名；P3 不使用 | **Pei（追認 2026-08-22）** |
