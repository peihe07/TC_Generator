# 23b — W-P2 補充下放包（四項裁定落地 + 兩處併入 W-P2）

> **[SUPERSEDED by 25_wp2.md — 2026-08-24]**
> 本檔為並行 session 所產之同輪下放包，與 `25_wp2.md` 對裁定 D 之落點分歧
> （上繳 25 §五-1）。**以 25 為準**；本檔內文一字未改，僅加本標頭（26 包 §A）。
> 依 R-G23（26 包 §C [DEFAULT]）：同輪重複下放者，另一份標 [SUPERSEDED] 不刪。

日期：2026-08-24
主工單：`docs/fw036/handoff/23_process_improvement.md` §E W-P2（本檔為其補充，同讀）
另讀：`docs/fw036/upstream/24_wp1_continuation.md`（§五-2／§五-3／§七-2／§十三-7 之背景）
上繳：`docs/fw036/upstream/23b_wp2.md`（不變）

**裁定記錄**：Pei 2026-08-24 chat「裁完」—— 四項照分析層建議通過；
23 包與 24 包之兩項 [DEFAULT]（R-G13 回報格式、sha 變動處置）一併追認轉正式。

**本包引用之裁決（R-G13@abdc56e3 格式）**：
R-G5@9814d24c、R-G12@eabe2726、R-G13@abdc56e3、R-G14@fb508d10、
R-G18@8f61f9fd、R-G20@3d0cd37b、R-VF45@bea4bbb8（加註後之值）

---

## A. 禁區（23 包 §A 全數沿用，另加）

- 38 處前綴改寫**不得範圍取代**，逐處人判（W-VF39 與 24 包 §十-1 之誤傷實例）
- 歷史 handoff / upstream 不追改（R-G18@8f61f9fd）
- waiver 只減不增：改寫完成之列**刪除**，不得留 stale

## B. 四項裁定條文（可直接貼入）

### 裁定 5 — active-backlog 採 (b)

```
active-backlog 279 處之處置：僅改寫 features/vehicle_setting/RULINGS.md
與 features/vehicle_setting/ANOMALIES.md 之 38 處（產線所在），逐處在
FO / IN 之間做語意判別加前綴，判定依據逐處列表入上繳；其餘 241 處留
waiver，以「只減不增」守住，各 feature 於日後開輪時消化自己之份。
```

### 裁定 6 — R-G13 條文內之裸 `canon §9` 維持現狀

```
R-G13 條文本體不改；24 包 §七-2 之加註與 waiver 1 列
（reason = verbatim-ruling-text）即為定案處置。
```

### 裁定 7 — R-G22（sha 變動之處置；24 包 [DEFAULT] 轉正式）

```
R-G22：條文之任何字元變動（含加註、沿革、SUPERSEDED 標記）皆變更其
sha；不設「加註不算改動」之例外。下放包所引 sha 與實讀不符時，執行層
停下回報（R-G13）；分析層核對變動性質後換發新 sha 引用；屬實質修訂者
依通則 11 出 ′ 版新條，不覆寫原條。
```

### 裁定 8 — R-G14 之生效起點（vehicle_setting）

```
R-G14 生效起點：vehicle_setting 量產自本裁定後之首個批次起算，
連續 3 批滿足 R-G14@fb508d10 四條件即自第 4 批進通道；四條件、
彙總節奏與退出規則照 FO §9.2 原文。其他 feature 之起點於各自
pilot 通過後另裁。
```

## C. W-P2 作業增項（接主工單 §E W-P2 之 1–4）

5. **38 處前綴改寫**（裁定 5）：`CANON_REFS_WAIVER.tsv` 取
   `features/vehicle_setting/{RULINGS,ANOMALIES}.md` 之 `active-backlog`
   列為工作清單；逐處判 FO / IN、改寫、自 waiver 刪列；
   上繳附逐處對照表（檔:行｜原文｜改後｜判 FO/IN 之依據一句）。
   改寫觸及條文本體者，`rulings_hash.py` 重產 tsv 並回報 sha 變動清單
   （R-G22 之首次適用）
6. **FO §2 fallback chain 修正**（24 包 §五-2）：無編號子節
   `### BLANK fallback chain (style decisions when no done region exists)`
   升為 `### 2.1 BLANK fallback chain …`；策略表該格
   `fallback chain (§3)` 改 `fallback chain (FO §2.1)`。準備入 diff，
   Pei commit 時過目即裁
7. **R-G22 與裁定 8 併入 canon §9.2**（隨本包 diff；R-G 最大號 21 → 22，
   裁定 8 作為 R-G14 錨點段內之「生效起點」小節 —— 依 R-G22，
   R-G14 之 sha 將變，新 sha 入上繳回報）

## D. 預期數字（增項；主工單 §E W-P2 之 1–2 照舊）

| # | 指標 | 預期 |
|---|---|---|
| 1 | waiver `active-backlog` 列數 | 279 → **241** |
| 2 | waiver 總列數 | 805 → **767**（−38；`historical-record` 與 `verbatim-ruling-text` 不變）|
| 3 | `canon_refs.py --waiver` FAIL | **0** 維持；stale | **0**（改寫列已刪）|
| 4 | FO 內 `fallback chain (§3)` 字面落點 | 1 → **0** |
| 5 | canon R-G 最大號 | 21 → **22** |
| 6 | R-G14 之 sha8 | `fb508d10` → **變**（實測回報，R-G22 首例）|
| 7 | 全套 pytest 失敗數 | **8**（既有，不得增減）|

## E. 升級條件（主工單 §F 沿用，另加）

1. 38 處中任一處 FO / IN 實指無法判定（列出候選與上下文，不猜）
2. 改寫觸及之條文其引用者（下放包、腳本常數）讀舊 sha —— 列清單回報，
   不自行改引用方

## F. 上繳要求

主工單 §G 全項 + 逐處對照表（C-5）+ sha 變動清單（C-7）+
R-G13 引用回報表（本包已附 sha8，首次可比對「不符」）。
