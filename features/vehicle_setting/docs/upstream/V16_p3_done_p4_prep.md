# 上繳 V16 —— VF230 之 writability 與 Priority 已備、PROXI 值域缺口、R-VF48 攔到二例

執行層寫入。依據：`docs/handoff/V16_p3_done_p4_prep.md` §5（4 項工單）。canon §8.2 六節。

**本輪未生成任何 TC、未執行任何寫回**（R-VF26）、**`framework.md` 未動**。

---

## 1. 交付總表

| 工單 | 狀態 | 產物 |
|---|---|---|
| W-VF44 VF230 之 writability（**P4 長徑**） | **完成** | `docs/reports/vf230_writability.tsv`、`scripts/vf230_wvf44_writability.py` |
| W-VF45 Priority 預判與批次規劃 | **完成，待核可** | `docs/reports/vf230_priority_batches.md`、`scripts/vf230_wvf45_priority.py` |
| W-VF42 R-VF48 之檢查實作 | **完成，攔到二項真缺漏** | `scripts/grade_overrides.py` |
| W-VF43 158 處判線別 | **未執行** | 見 §5 |
| 條文落檔 | **完成** | R-VF48／R-VF49（R-VF 現 **42 條**）；A-VF1（補落）／A-VF11 |
| DR | **DR-34 新開** | `DATA_REQUESTS.md` |

---

## 2. W-VF44 —— VF230 之 writability

```
627 leaf        W0 593 ／ W1 28 ／ W2 6
blocker         B5-signal-absent 6
```

**沿用 Part 1 之分級定義（R-VS47／R-VS71）與 blocker 分類碼，未新設。**
Part 1 之 B1／B2／B3 為委派與畫面層之碼，**VF230 尚無委派判定，本輪不用**。

**值域來源鏈（取用順序，先命中者為準）**：

```
1-LID   （Atlantis High 欄組，R-VS67）        4 次
2-DBC   （VAL_，含 A-VS137 之補收）          370 次
3-PROXI （PROXI 表 Format 分頁）              87 次命中 ／ 28 次未解
4-VCVM  （037 之 VC/VM，R-VF13）               0 次
```

**`not clear` 之 90 leaf 皆未被用為來源** ✅（R-VF13 第 4 項）。

**鑑別錨點（LID／DBC 皆無而 VC-VM 有者）：0 個 —— 不存在。**
即 A-VS118 之形態於 VF230 **無對應者**；R-VF13 之來源開放於 VF230 現無實際作用。
**依 W-VF44 第 5 項具名。**

### 2.1 ⚠ 一項首版之重大低估

首版判 **621 W0 / 6 W2**，其成因為**鏈 3（PROXI）宣告而未實作** ——
627 leaf 中 **252 leaf 無訊號引用**，其可測內容立於 PROXI 配置之取得
（`retrieve the <X> PROXI configuration`），而首版將其一律歸為 W0。

實作鏈 3 後得 **593 / 28 / 6**。

**PROXI 之量測亦兩度更正**：首版報「46 個參數中僅 4 個於表內」——
係掃描範圍過窄（各分頁前 400 列、前 6 欄、逐字相等）。
改掃 `Format` 分頁 800 列後得 **35 個在表內、11 個無**。

**11 個無來源者影響 28 leaf → 判 W1，標 `PENDING: DR-34`**（R-VS47／R-VS71：
其未解值為前提條件而非驗證目標，故不判 W2）。**已開 DR-34。**

PROXI 鏈之三錨點實測：必命中 `Heated_Seats` ✅／必不命中 `AUX_Switch_Types` ✅／
**鑑別 `Blind_Spot_Monitoring`（在表內）vs `Blindspot_Trailer_Detection`（不在）** ✅
—— 二者名近，一條以子字串比對之規則會誤判其一。

---

## 3. W-VF45 —— Priority 預判與批次規劃

### 3.1 ⚠ R-VS56 之 P0 二類係以 Part 1 之內容界定，VF230 二者皆無

R-VS56 之 P0(a) 為第三排頭枕下放、P0(b) 為加熱元件 ——
**VF230 無頭枕下放、無加熱功能**。

故本層依其**原則**（實體致動且具傷害可能／熱源）對映 VF230，
**逐簇具名，附「其驅動何機構、乘員何以可能在其行程內」**：

```
Power Tailgate ／ Power Liftgate/Tailgate Alert   電動尾門，行程內可能有人
Power Side Step                                   電動側踏板，貼近上下車者足部
Suspension Auto Entry or Exit ／ Default Ride Height
  ／ Flash Lights With Lower ／ Sound Horn With Lower ／ Service Mode
                                                  車身升降，人在其側或車下
Driver Easy Exit Seat                             駕駛座椅自動退移，人在座
```

**P0(b)（熱源）= 0。**

**此對映為本層之預判，非 R-VS56 之逐字 —— 待覆核。**

```
P0  49  ／  P1 288  ／  P2 290       （合計 627）
```

**鑑別錨點**：`Suspension Display Messages` **判非 P0** ——
其為訊息顯示而非車身致動；一條以 `Suspension` 為鍵之規則會誤判之。

### 3.2 選池與批次

依 **R-VS58**（P0→P1→P2；同序內逐 Test Set 輪流 ＋ reqid 升冪）：
可生成之池 **621**（627 − W2 6），**63 批 × 10**。

**pilot 批建議為第 1 批**（含 P0 之前 10 條，風險最高者先驗其書寫形式）。
**其範圍與時點待分析層核可，本輪未生成任何 TC。**

---

## 4. W-VF42 —— R-VF48 之檢查，**首次執行即攔到二項真缺漏**

1. **`A-VF1` 自始未落檔** —— 分析層於 V04 §4 登記，其後無對應上繳
   （`docs/upstream/V04_*` 為缺號），條文遂未進 `ANOMALIES.md`。
   **與 `R-VF9` 同型之第二例。** 本輪已補落。
2. **`feature.yaml` 兩處仍引用 `A-VS131`** —— 該號已於上繳 V12 §2 讓號為
   `A-VS134`。**改號時漏了設定檔。** 本輪已更正。

**檢查現仍 FAIL（57 項），逐類具名、未抑制**：

| 類 | 例 | 處置 |
|---|---|---|
| **(a) 真缺漏** | `R-VF1`／`R-VF2`／`R-VF8` | 即 A-VF10 之撞號集，現以 `R-VS59`–`R-VS66` 存在。**待 R-VF49 之改號** |
| **(b) 判準過窄之殘留** | `R-VS1`／`DR-5`／`DR-11` | `RULINGS.md` 早期條文之標題形態、`DATA_REQUESTS.md` 之表列編號（`5-A`／`9`）不合現行抽取式 |
| **(c) 偽陽性** | `A-VS001`／`A-VS199`／`R-VF99` | 文字中之數列片段；`R-VF99` 為本腳本 docstring 內之錨點示例 |

**判準已兩度修正（84 → 73 → 57）**，見 **A-VF11** ——
其中一次之成因為 **R-VF10 所令之舊制標記使 R-VF48 之抽取式失效**：
**兩條規則各自正確，其交互產生誤報。此形態於本線為首見。**

---

## 5. W-VF43 —— **未執行**

V16 §6 列其為最低優先且「在寫回凍結期間不阻塞」。本輪四項工單以
W-VF44／W-VF45 為長徑（二者合計為 P4 之全部前置），未及 W-VF43。

**其範圍已由 W-VF39 備妥**（516 處／60 檔，現行 158／歷史 358，含鑑別錨點之實例），
階段一可逕自該表接續。**具名為本輪未做者。**

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **W1 之判定路徑只涵蓋 PROXI 一源。** Part 1 之 88 個 W1 多源於
   DR-15／DR-25 之未解值（訊號值域），而 VF230 之 W1 全數來自 PROXI。
   **本層未對 VF230 之訊號值域跑 `guard_new_conclusion()` 之 DR 衝突閘** ——
   W-VF6 實測 VF230 只受 DR-21 波及 7 leaf，故其影響應小，
   **但「應小」是推論，未實測。**

2. **委派判定（R-VS7／B1–B3）於 VF230 完全未做。** Part 1 有 99 個 B2
   （畫面層委派 Comfort）。VF230 之 627 leaf 中是否有應委派者**未查** ——
   若有，其現被判 W0 而將被寫成 TC。**此為本輪最大之未驗項。**

3. **P0 之對映未經覆核即用於選池排序。** §3.1 之九簇為本層預判；
   若覆核後 P0 集合改變，選池順序隨之改變，**而 pilot 批正是自池首取**。

4. **R-VF48 之 (b) 類殘留使該檢查現無法作為「一切正常」之訊號** ——
   與 A-VF10 對 `R-VF10` 項之影響同型。**已由 R-VF46 之總表區隔**，
   惟「新失敗 1」現恆為 1（R-VF48 項），**其區辨力已被稀釋**。

5. **W-VF43 未執行**（§5）。

**另**：本輪之 `A-VF1` 與上輪之 `R-VF9`，其發現路徑皆為
**「一項新立之檢查於首次執行時攔到」** —— 而二者皆已存在逾十包。
**R-VF48 立法後之首跑價值，等同其後所有次跑之總和。**
