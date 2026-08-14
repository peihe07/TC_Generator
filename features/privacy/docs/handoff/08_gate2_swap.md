# 下放包 08 — B1-GATE-2 通過、換檔完成確認

分析層 → 執行層。2026-08-13。短包，僅記錄兩項確認與連動作業。

---

## 1. 裁決條文

```text
[RULING] R29 — B1 前置條件之兩項確認（2026-08-13）

R29-1  B1-GATE-2 —— Excel 實開確認通過
  裁：Pei 於 2026-08-13 開啟
      `features/privacy/output/FM-WI-FSM-036-A01 … _Privacy_20260813.xlsx`，
      四點全過：
        1. 無「檔案已損毀，Excel 已修復」提示
        2. R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
        3. D5 範圍 Scope 顯示 `SWE1_CFTS_022-Privacy_Features`
        4. 第 10–11 列已清，B 欄序號未顯示殘值
      **B1-GATE-2 通過。**
  意義（逐字記錄，避免日後被當成形式手續）：本項是 zip 層外科手術
      路徑**第一次**取得人為 Excel 開啟之確認。此前所有驗證皆在程式層
      （zip 成員 48→48、DV 4:2→4:2），程式層驗不到 Excel 之檔案完整性
      判定。R18-3 規則 1 至此取得端到端佐證。
  DELIVERY.sha256 之 ENTRY 001 加註：
      「Excel 開啟確認：Pei, 2026-08-13, 四點全過（R29-1）」。

R29-2  V6_R2 換檔完成 —— A-PV14 事實面結案
  實測（分析層，2026-08-13，對 repo 實體路徑）：
      `features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_
       Amplified_Audio_System_VF651_V6_R2.docx`
      SHA256 = e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2
      size   = 177,388 bytes
      與 R28-2 之預期值 `e20ba7a4f8f7…` 相符 → 換檔完成。
  裁：**A-PV14 → RESOLVED**。三處連動即刻辦理（見 §2）。
      平台歸屬之佐證有二且互相獨立：路徑（HDCC28_Split）與文件內文
      （revision note `derived from VF651_V6_R1_PHDCCMCA`，hunk 8）。
```

---

## 2. 執行層作業

1. 貼入 §1（R29）至 `features/privacy/RULINGS.md`
2. `DELIVERY.sha256` ENTRY 001 加註 R29-1 之 Excel 確認行
   （**追加不改寫**既有欄位）
3. `BASELINE.sha256` 之 V6_R2 該行改為
   `e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2`
   （size 177,388），命中路徑改為
   `VF/VF_Split document/HDCC28_Split/`，檔頭記 R24-2(2) / R28-2 / R29-2；
   **就地修正**（素材為同一批，非新增 ENTRY）
   改後跑一次 `shasum -a 256 -c BASELINE.sha256`，8 檔須全 OK
4. `ANOMALIES.md` A-PV14 → **RESOLVED**，記入兩項獨立佐證
5. 解除三處「不得引用 V6_R2」之限制：
   - framework Part VI 注 3
   - profile §6 之 V6_R2 列
   - profile §5 之 `[A-PV14]` marker 表 —— **整條移除**，
     §5 若因此無任何 marker，改記「本 feature 目前無 marker」
6. `PLAYBOOK.md` §6 之 Open PENDING 同步（A-PV14 移出）

---

## 3. B1 剩餘前置條件（本包不解除）

| Gate | 狀態 |
|---|---|
| B1-GATE-1 PROF→artifact 全 10 筆獨立重驗 | **未辦** —— 下放包 07 §6.6，執行層作業 |
| B1-GATE-2 Excel 實開確認 | ✅ 通過（R29-1） |
| B1-GATE-3 欄 S（P-4）與車型欄（P-5）填值政策 | **未裁** —— P-5 待執行層回報 rev C 之 T–Z 標頭 |

**三項全備方可下放 B1 生成包。** 本包不得視為 B1 之啟動授權。

---

## 4. 停手條件

1. `RULINGS.md` R29 編號已占用 → 停止貼入，續行第 2–6 項
2. 第 3 項改後 `shasum -c` 非 8 檔全 OK → 停止第 4–6 項，續行回報
3. 第 5 項解除限制時發現尚有第四處未列之「不得引用 V6_R2」字樣 →
   一併解除並於上繳包載明（此為事實性補正，依 R28-3 得逕行）

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R29-1 B1-GATE-2 通過 + 外科手術路徑首次端到端佐證 —— §1，區塊形式
- [x] R29-2 V6_R2 換檔完成，A-PV14 RESOLVED —— §1，區塊形式
- [x] B1 剩餘前置條件表（本包非啟動授權）—— §3
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §4

<!-- HANDOFF-LINK: 08 -> no-upstream-produced -->
