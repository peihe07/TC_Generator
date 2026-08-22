# 下放包 23 — SYS3 比對結果：A-TM09 確為真缺口，我的假設被推翻

分析層 → 執行層。往返編號 `23`。對應上繳 `docs/upstream/23_sys3_result.md`。

分析層已自行完成 `22` 之 T2 / T3（將 SYS2 與 037 複製入沙箱後比對）。
**結果與 `22` §3 之假設相反。**

---

## 1. 集合比對 —— 完全相等（`22` T2）

```
SYS3 相異 id      126
SYS2 FR           126
SYS3 有而 SYS2-FR 無    0
SYS2-FR 有而 SYS3 無    0      ← 兩向差集皆為空，集合相等
037 引用          78
A-TM09 之缺口      48
  其中 SYS3 涵蓋者  48 / 48
```

**SYS3 完整涵蓋全部 126 筆 FR，48 筆缺口全在其中。**
與版本 C 之修訂說明「complete source coverage」相符。

## 2. **但 SYS3 不是分配文件 —— 我的假設被推翻**

`22` §3 我推測「48 筆在 SYS.3 被分配給 HU 軟體以外之單元（IPC / LTM），
故 037 未涵蓋」。**實測不成立。**

### 2.1 SYS3 之需求表無「分配單元」欄

表格結構（126 列，七欄）：

```
id | 需求描述 | 物件 id | Category | (第 5 欄) | 架構 | 訊號
```

**第 5 欄實測 126/126 皆為 `NA`** —— 該欄非分配單元。
七欄中無任何欄位標明「分配給 HU / IPC / LTM / ETM」。

### 2.2 48 筆之架構分佈 —— **過半為 ATL-Hi**

```
ATL-Hi   18  +  Atl-Hi  8   =  26      ← 大小寫漂移，同 A-TM03
ATL-Mid  20
All       2
```

**26 / 48 為 ATL-Hi**，即 HU 主控之架構剖面。

### 2.3 抽讀六筆 —— **明確為 HU 軟體行為**

```
012  ATL-Hi  OperationalModeSts, HU_Time.Info
     In the following Ignition Working Conditions: Ignition Off / On / Pre Start / …

016  ATL-Hi  GPS_Presence, Country_Code, VC_VEH_LIN…
     The HU and VES shall configure the time display behavior based on par…

036  ATL-Hi  NAVPrsnt
     Nav HUs shall default to GPS time. Non-Nav HUs shall use manual time.

038  ATL-Hi  GPSDateTmHour, GPSDateTmMinute, GPSDateTmSecond
     Nav HUs shall use GPS data to maintain a GPS clock in addition to an
     internal calculated clock.

040  ATL-Hi  N/A (behavioural requirement)
     If the internal clock is set manually and 'Sync Time with GPS' is turned
     ON, the radio shall maintain…
```

**六筆中五筆逐字以 `The HU` / `Nav HUs` / `the radio` 為主詞。**
036 與 038（Nav / Non-Nav HU 之時間來源）尤其是**核心 HU 行為**，
不是別的單元的事。

### 2.4 結論

```
A-TM09 之定性不變且獲強化（2026-08-22，分析層實測）

48 筆並非「分配予 HU 軟體以外之單元」。SYS3 無分配欄；48 筆中 26 筆
標為 ATL-Hi，抽讀六筆有五筆逐字以 HU / Nav HU / radio 為主詞。

**故 A-TM09 為真缺口：037（SWE.1）未將該 48 筆分解為 SWE leaf，
而其中相當部分是 HU 軟體行為。**

`22` §3 之假設（分配結果）**推翻**，其於該包所提之交付說明改寫
（「不在 SWE.6 範圍」）**不採**。交付說明維持現行陳述：
48 筆 SYS2 FR 無對應 SWE leaf，覆蓋率 78/126 = 61.9%。
```

## 3. 對現行產出之影響 —— **TC 不變，但缺口之份量變重**

**59 條 TC 不需增加，理由不變**：生成單位為 037 之 22 片 leaf，
canon §8.2 禁止 TC 作者創設或分解 leaf。**我方不能替 037 補做它沒做的事。**

**但兩件事變了**：

1. **缺口之嚴重性提高。** 先前只知「48 筆無 leaf」；現在知道其中
   26 筆標 ATL-Hi、且含 Nav/Non-Nav 時間來源這類核心行為。
   **這不是邊緣需求被略過。**
2. **RD-1 之 Q-TM3 應據此改寫。** 原問法為「該 48 筆是否分配予其他
   feature 之 037，或屬本 feature 之分配缺口」——
   **SYS3 已排除前者**（SYS3 無分配欄，且該 48 筆與其餘 78 筆在
   同一份表、同樣格式、無任何區別標記）。問法應收斂為：
   **「037 為何未涵蓋此 48 筆？是否將補件？」**

## 4. 附帶發現：SYS3 之架構欄有同一大小寫漂移

```
ATL-Hi 67 / Atl-Hi 10 / ATL-Mid 45 / All 4
```

**與 A-TM03（SYS2 之 `ATL-Hi` 101 / `Atl-Hi` 10）同型。**
凡以字串等值篩 SYS3 之架構欄者，會靜默漏掉 10 列。
併入 A-TM03 之註記，不另立 anomaly。

## 5. 指令

### T0 / T1 — 素材落地與登記

SYS3 複製入 `inputs/`；`DATA_REQUESTS.md` 新增一列
`RECEIVED（2026-08-22）`，註明其為 SYS.3 層。

### T2 — 分析層結論之獨立複驗

**分析層之 §1–§2 跑在沙箱複本**（SYS2 與 037 為自 `inputs/` 複製）。
執行層對 `inputs/` 重做，逐項對差：

1. 三個集合之兩兩差集（期望：SYS3 ↔ SYS2-FR 兩向皆 0）
2. 48 筆全在 SYS3（期望 48/48）
3. SYS3 需求表之七欄結構，**第 5 欄是否 126/126 皆 `NA`**
4. 48 筆之架構分佈（期望 ATL-Hi 18 + Atl-Hi 8 + ATL-Mid 20 + All 2）
5. **抽讀 48 筆中另取 10 筆**（非分析層所抽之六筆），
   逐筆判定其主詞是否為 HU / radio / Nav HU 一類
   —— **若 10 筆中多數非 HU 行為，回報並停**，該情形會推翻 §2.4

### T3 — `ANOMALIES.md`：A-TM09 之定性強化

追加 §2.4 之區塊全文。**狀態維持 PENDING**（其解除仍需上游答覆）。
A-TM03 追加 §4 之大小寫漂移註記。

### T4 — RD-1 之 Q-TM3 改寫（§3 項 2）

`docs/fw036/RD1_questions_time_management.md` 之 Q-TM3，
將「是否分配予其他 feature 之 037」一段依 SYS3 之實測排除，
問法收斂為「037 為何未涵蓋此 48 筆？是否將補件？」，
並附 SYS3 之三項證據（無分配欄、26 筆標 ATL-Hi、抽讀之主詞）。

**狀態仍 DRAFT，不送出**（Pei 已指示不送 RD-1；本項為文件正確性，
非送出動作）。

### T5 — 上繳

`docs/upstream/23_sys3_result.md`。**依 R-TM74 列逐 T 對照表。**

### 不得執行者

- 不動 git；**不加 `--write`**
- **不生成任何 TC**、不補 leaf（canon §8.2）
- 不改 A-TM09 之狀態（仍 PENDING）
- 不送出 RD-1
- 不碰 `features/vehicle_setting/`

---

## 6. 呈報 Pei —— **寫回可以放行了，但缺口比原先以為的重**

`22` §7 我建議暫緩寫回，理由是「若 §4.3 含 037 未涵蓋之 HU 行為，
leaf 全集就不是 22 片」。

**實測結果：確實含 037 未涵蓋之 HU 行為（26 筆標 ATL-Hi），
但 leaf 全集仍是 22 片** —— 因為 leaf 由 037 定義，而 037 就是沒做。
**我方不能替它補**（canon §8.2）。

**故暫緩之理由消失，寫回可放行。**

但交付時要知道：**48 筆缺口不是邊緣需求被略過**。抽讀之六筆中有
`Nav HUs shall default to GPS time. Non-Nav HUs shall use manual time.`
與 `Nav HUs shall use GPS data to maintain a GPS clock…` ——
**那是 GPS 時間來源之核心行為，而我方無對應 TC。**

交付件之覆蓋率為 **78/126 = 61.9%**，這個數字現在有 SYS3 作為
「126 確為完整需求集」之佐證，**比先前更難辯解為統計口徑問題**。

**建議**：交付時附一句說明，指明覆蓋率之分母與缺口成因指向 037。
要我起草那段文字就說一聲 —— 那是交付形式，屬你。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| A-TM09 定性強化 | anomaly 註記，狀態不變 | §2.4 | ✅ T3 |
| A-TM03 大小寫漂移註記 | 併入既有條 | §4 | ✅ T3 |
| Q-TM3 改寫 | RD-1 草案，仍 DRAFT | §3 | ✅ T4 |

**無新條文。** 分析層本包未動 git、未改任何腳本、未改任何 TC。
§1–§2 跑在沙箱複本，T2 為對 `inputs/` 之重測。
