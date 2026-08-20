# 14 下放包 — 04 輪覆核：兩條異常降級、一條成立、R-VS9 須改權威

分析層寫入，2026-08-20。對象：`docs/upstream/03_crosscheck_and_overlap.md`。

**覆核結論：接受，惟三條新異常經複驗後結論改變兩條。**
本輪上繳有一項迄今未見之處置值得記明：**執行層在有直接證據（六個 commit
是它自己跑的）之情況下照抄了上游之推測，並自行指出此事**（§0 之
「執行層亦有責」）。該自陳比 W-25 之結果本身更有價值。

---

## 1. A-VS26（`$ESS_ENG_ST$` message 歸屬矛盾）—— **降級為解析產物**

上繳記：LID 載於 `ENGINE_FD_2`，DBC 實際於 `STATUS_CCAN3`，判為矛盾。

分析層自 `inputs/` 實體檔複驗（LID `CAN Mapping` r695，Atlantis High 欄組）：

```
AtlHigh Signal Name : STATUS_CCAN3.ESS_ENG_ST   ENGINE_FD_2.ESS_ENG_ST
AtlHigh CAN         : CAN-B  FD
```

**該儲存格同時載明兩個 message，對應兩個網段。** 對照兩份 DBC：

| message | BHCAN | FDCAN8 |
|---|---|---|
| `STATUS_CCAN3` | **有** | 無 |
| `ENGINE_FD_2` | 無 | **有** |

→ **LID 與 DBC 完全一致，兩者皆對。** `ESS_ENG_ST` 在 CAN-B 走
`STATUS_CCAN3`、在 CAN-FD 走 `ENGINE_FD_2`，與 R-VS8 之「兩份並用」同型。

**A-VS26 降級為我方解析產物**（單格多 message 未展開）；**DR-13 撤銷**。

> 此為 §2.3 所述「LID 儲存格含多訊號」缺陷之**第三次**現身：
> W-8 之 C3、W-15b′ 之交叉配、本項。**同一缺陷連三輪以不同面貌出現。**
> W-23 之 C3 判準化與解析式修正因此**不再是可延項**。

---

## 2. A-VS28（8 支訊號不在基線 DBC）—— **範圍大幅縮小**

分析層逐支複驗（`SG_\s+<name>\b`，兩份 DBC）：

| LID 欄組 | signal | BHCAN | FDCAN8 | 判定 |
|---|---|---|---|---|
| **Atlantis High** | `FL_HS_Tlm`（`TELEMATIC_VEHICLE_SETUP3`）| **有** | 無 | 在 |
| **Atlantis High** | `FL_VS_Tlm` | **有** | 無 | 在 |
| **Atlantis High** | `HSW_Tlm` | **有** | 無 | 在 |
| Atlantis（**非 in-scope**）| `HeatLeftSeatTgl`（`TGW_HVAC_CTRL_M`）| 無 | 無 | **不適用** |
| Atlantis（**非 in-scope**）| `FL_HS_Cmd_Tlm_Req` | 無 | 無 | **不適用** |
| Atlantis（**非 in-scope**）| `HSW_Cmd_Tlm` | 無 | 無 | **不適用** |
| **Atlantis High** | `HDRstRelRq_3rdRow`（`RADIO_B3`）| **無** | 無 | **真缺** |

`TGW_HVAC_CTRL_M` 於兩份 DBC 皆不存在 —— 該 message 屬 Atlantis（非 High）
架構之對映，依 **R-VS9(1)** 本就不取用。

**`HDRstRelRq_3rdRow` 為唯一真缺**：`RADIO_B3` 存在於 BHCAN，
其 signal 為 `ManDispCtrl` / `PowerSideStep_Req` / `RQ_DISP_INTS` / `VR_Blower_Req`
—— **無任何頭枕相關**。兩份 DBC 內含 `HDRst`／`Headrest` 者僅
`Driver_Headrest_Req`、`Passenger_Headrest_Req`（皆在 BHCAN），
**無第三排**。

→ **A-VS28 由 8 支縮為 1 支**；**DR-14 改寫**（Urgency 由 High 降 Medium，
但問題更銳利）：

```
DR-14′（取代 DR-14）
LID 表載 `HdRstRelRq` 之 Atlantis High 對映為 `RADIO_B3.HDRstRelRq_3rdRow`，
但基線 DBC 之 `RADIO_B3` 不含該 signal（其 4 支為 ManDispCtrl /
PowerSideStep_Req / RQ_DISP_INTS / VR_Blower_Req）；
兩份 DBC 全域僅有 `Driver_Headrest_Req` 與 `Passenger_Headrest_Req`，無第三排。

請確認第三排頭枕釋放請求之實際 signal 名與所屬 message，
或該功能於本專案是否不落在此二網段。
影響：037 引用 `$HdRstRelRq$` 之 16 處，其 procedure 之操作步驟需要此訊號。
```

---

## 3. A-VS27（signal 名大小寫）—— **成立，且其後果比上繳所述更廣**

複驗確認：LID 寫 `HSW_STATSts`／`HSW_STATFailSts`，
DBC 為 `HSW_StatSts`／`HSW_StatFailSts`。**BHCAN 無任何 `HSW_STATSts`。**

上繳指出「依 R-VS9(1) 照 LID 寫入 TC 即寫出匯流排上不存在之名」——
**正確，且分析層之 00G §2 表格已據 LID 抄了該拼法**，
即該錯誤已一度落在下放包內。

```
R-VS9(1)′（Pei 2026-08-20，已裁）
R-VS9(1) 原文以 LID 表為訊號逐字名之第一權威。**該分工須拆開**：

  signal 之**逐字拼寫** → **DBC 為第一權威**
       （DBC 是匯流排之定義本身；LID 表為對映表，其拼寫為轉錄）
  signal 之**所屬 message、網段、與 LID ↔ signal 之對映**
       → **LID 表為第一權威**（DBC 不含 LID 之概念，無從對映）
  值域 → 依 R-VS20 之階梯，並與 DBC `VAL_` 交叉核對

實例：`$HSW_Stat$` 之名取 DBC 之 `HSW_StatSts`（非 LID 之 `HSW_STATSts`），
其 message `STATUS_CSWM` 與網段 CAN-B 取自 LID 表（與 DBC 相符）。

配套 lint（L-VS2）：TC 內出現之 signal 名須在基線 DBC 中**區分大小寫**
逐字存在；不存在者 FAIL，且錯誤訊息須列出不分大小寫之近似命中，
以區分「拼寫差異」與「真不存在」。

理由：本輪之 A-VS27 顯示第一權威本身可能為轉錄錯誤；
而「匯流排上是否存在此名」只有 DBC 能回答。
```

---

## 4. 三項作業之積壓 —— R-VS21 已不足

`W-17`／`W-9` 自 06 包列入，**連續三輪未執行**；
`W-22`／`W-23`／`W-24` 連續兩輪。R-VS21（連兩輪者排入頭部）本輪已生效
—— **頭部確實是 W-15b′／W-17／W-9** —— 但 W-15b′ 一項就用掉整輪。

**成因不是排序，是單輪容量。** W-15b′ 找到三條真異常並自我修正一次配對式，
其工作量本就足以構成一輪。

```
R-VS25（Pei 2026-08-20，已裁）
每輪之作業上限為**三項**（唯讀查證與文書項不計）。
下放包列出超過三項者，第四項起標記為「本輪不做，排入次輪」，
執行層不得因有餘力而提前執行。

理由：本 feature 連續三輪之作業清單為 6–8 項，實際完成 1–3 項，
未完成者於次輪重列 —— 清單之預測價值因而為零，且「未執行」佔據
上繳包之獨立判斷節，稀釋了真正的未驗項。

例外：一項在該輪被證明為零工作量（如標的不存在）時，得續行下一項。
```

依本條，**05 輪為三項：W-9／W-23／W-22**（W-17 讓位 —— 見 §5 理由）。

---

## 5. 05 輪作業（**三項**）

| # | 作業 | 為何是這三項 |
|---|---|---|
| 1 | **W-23** 歸因判準化 C1–C5 **＋ 修正 C3 解析式** | C3 之同一缺陷已三度現身（§1 末）。**先修工具再比對**，否則 W-22 會第四次踩到 |
| 2 | **W-22** 餘數驗證 | 02 上繳自陳之最弱一環；且 W-15b′ 新增了對 LID 表之依賴，該弱點只會擴大 |
| 3 | **W-9** Comfort 逐條對照（母體 237） | 連三輪未執行；framework 之前置 |

**W-17／W-24／DR-14′ 之追問** 排入 06 輪。

**順序理由**：W-23 修的是 W-22 會用到的解析器 —— 這是 R-VS21 例外條款
所稱之「阻塞既有作業之前置」，故 W-23 置於 W-9 之前不違反 R-VS21。

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| P11 | 裁 R-VS18／R-VS19 |
| P12 | 裁 R-VS20／R-VS21 |
| P13 | 裁 R-VS23／R-VS24（R-VS24 已用畢，追認即可） |
| ~~P14~~ | ~~裁 R-VS9(1)′、R-VS25~~ — **已裁（Pei 2026-08-20）**，見 §3／§4 |
| — | 附錄 A 與本輪產物之入庫；推送（分支領先 origin 8+） |

**R-VS9(1)′ 已裁定** → 訊號名之寫法定案，`L-VS2` 可實作。

**擋在 framework 之前者現僅剩 R-VS20**（值域來源之階梯）：
`$HSW_StatFailSts$` 這類 in-scope 無值域之 token 尚無合法取值路徑，
而該 token 為 17 個 BLOCKED leaf 之訊號層 ER 依據。
**R-VS20 未定案，首批生成無法開始。**

### 6.1 落條文之作業（05 輪首件）

執行層須將 §3 之 `R-VS9(1)′` 與 §4 之 `R-VS25` 兩個區塊**逐字轉錄**入
`features/vehicle_setting/RULINGS.md`（不摘要、不以編號代替），
並於 `RULINGS.md` 之 R-VS9 條目加註「(1) 之權威分工經 R-VS9(1)′ 更正，
以 R-VS9(1)′ 為準」。

**R-VS25 自 05 輪起生效**：05 輪之作業為 W-23／W-22／W-9 三項，
第四項起不得執行。

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS9(1)′ | signal 拼寫以 DBC 為權威、對映以 LID 為權威；L-VS2 | ✔ §3 |
| R-VS25 | 單輪作業上限三項 | ✔ §4 |
| DR-14′ | 第三排頭枕訊號之追問（取代 DR-14） | ✔ §2 |
