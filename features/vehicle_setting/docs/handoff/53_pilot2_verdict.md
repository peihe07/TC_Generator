# 53 下放包 — pilot #2 裁決、A-VS62 定案

分析層寫入，2026-08-22。Pei 指示「裁定」——
依 51 包 §5 之待裁二項，採分析層所附之建議定案。

---

## 1. pilot #2 之裁決

```
pilot #2（Pei 2026-08-22）
15 條之分類依 51 包 §1 之建議表定案：

  pass   10 條
  defect  4 項（涉 5 條）—— 修法逐條具名，31 輪 W-89 已執行完畢，
                            三批機械自檢各 0 項
  note    1 條（`HeatedSteeringWheel-021`，`duplicate_of` 標記正確）

**四項 defect 修正後放行。** pilot #2 通過。

未經抽樣之 53 條（68 − 15）**不因本次通過而視為已 review**；
其品質推論受 §2.3 之偏斜所限（`Heated Seat` 佔母體 37%，
於 15 條抽樣中僅 1 條）。
下一次 pilot 之時機：**累計交付達 120 條，或 batch 之 defect 率
較 pilot #2 上升時**，二者孰先。
```

**pilot #1（8 條）＋ pilot #2（15 條）＝ 23 條經人工關卡，佔已交付 76 條之 30%。**

---

## 2. A-VS62 定案

```
A-VS62（Pei 2026-08-22，採 51 包 §2.5 之路徑 (a)）
送出型步驟之 ER 措辭 `The signal $X$ = <raw> (<label>) is registered
without a bus error` **認可為本 feature 之既定寫法**。

其適用範圍：`Send the signal …` 型步驟之對應 ER。
讀取型（`Read the signal …`）之 ER 仍用 `reads <raw> (<label>)`。

**記入 `docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md` 之 [ADD] 段。**

限制：本認可為 feature-scoped，**不得援引至他 feature**；
日後若取得 SWC 0708 或任一已交付本之「送 CAN 訊號」樣本而其措辭不同，
以該樣本為準並逐條替換（單欄字串替換，成本有界）。

A-VS62 關閉（懸置 25→31 輪，共七輪）。
```

---

## 3. 32 輪指令 —— 無變動

52 包 §4 之指令仍為現行，**唯一追加**：

```text
（追加於 52 包 §4 之「文書」段）

D-7  profile 增列 A-VS62 之 [ADD] 段（53 包 §2 全文）；
     ANOMALIES.md 之 A-VS62 標「關閉，Pei 2026-08-22」。
D-8  `docs/reports/pilot2_sheet.md` 檔頭加註
     「pilot #2 通過，Pei 2026-08-22；defect 4 項已於 31 輪 W-89 修正」。
```

---

## 4. 待 Pei（**僅餘 DR 之送出**）

| DR | 型 | 狀態 |
|---|---|---|
| **DR-21** | A | 已定案（137 leaf／215 次／27 token），**可送** |
| DR-17／DR-24′／DR-18／DR-11 | A | 待送 |
| DR-20／DR-23／DR-8′ | B | 待送（搜尋已停止，訴求為取得文件） |
| DR-15 | A | **待覆**；32 輪 D-3 補入架構欄組之觀察段 |

**條文面無待裁項。**

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| pilot #2 之裁決 | pass 10／defect 4 已修／note 1；下次 pilot 之時機 | **Pei** |
| A-VS62 | 送出型 ER 措辭認可為 feature-scoped 既定寫法 | **Pei** |
