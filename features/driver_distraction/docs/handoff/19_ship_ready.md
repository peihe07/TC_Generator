# 下放包 19 —— forms/ 查證（DD8 不解）、A-DD11、R-DD20 v3（DD9 撤 PENDING）、R-DD24、11-1~11-5、T25

- 日期：2026-08-28
- 方向：分析層 → 執行層 ＋ Pei（§六）
- 前一包：`18_gate.md`；對應上繳：`15_gate.md`
- 27 檢、T24e 三項閉合、注入 P／Q／P2／P3／R 全數採認

---

## 一、forms/ 查證 —— Pei 指名之 DTC 檔與分析層之候選，**皆非 Lockout Table**

分析層本輪實測（唯讀，經 `copy_file_user_to_claude` 取副本後以 openpyxl 讀）：

| 檔 | 母體 | lockout 類命中 | 判 |
|---|---|---|---|
| `forms/DTCs Matrix Core List Rev. 1.6.xlsx` | 7 分頁、2,130 格 | `lock` 11 —— **全為診斷碼**（`PLL unlocked.`／`Touch Screen Locked`）；`distraction`／`L/O`／任一 feature 名 **0** | **非** Lockout Table |
| `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | 3 分頁、3,013 格 | `lockout` 10、`in motion` 6、`distraction` 1 | **非** —— 見 §1.1 |

### 1.1 HMI Settings List 何以仍不解 [CG-DD1]

其 `Settings` 分頁 1,015 列之欄頭為
`List Item／Template／Options／Technical Reference／Notes／Info Popup`，
**無 lockout 欄**；命中全在 **Notes 自由文字欄**，形如：

- r151 c7：`This category is locked out while vehicle is in motion. …`
- r250–253 c7：`Will not be available while the vehicle is in motion for some regions.
  Please refer to CFTS022 (Driver Distraction Lockout section) for requirements.`

**即：它以自由文字標註「某些設定被鎖」，而非以欄位區分 L/O 與非 L/O。**

**1,005 列無註記者不得推論為「不在表內」** —— 那是**從沉默推論**，
與本 feature 三度栽過之「看起來像就當它是」同族；且 r250 逐字把
requirements **指回 CFTS022**，反證該表才是權威。

**故 DR-DD8 必發等級不變。** 惟其文稿**加一句**載明已查範圍（§三-1）——
使上游知道我們找過何處，減少一輪往返。

### 1.2 順帶查得 —— **彈出字串二變體（A-DD11）**

同檔全簿正則掃 `(Function|Feature).*not available`：

| 變體 | 出處 | 與已生成 TC 之關係 |
|---|---|---|
| `Feature not available while the vehicle is in motion` | `Settings` r666 c7 | **與 profile §2.1 觀察面 B 逐字相同**（源 HMI spec p4）|
| `Function not available while vehicle is in motion` | `Settings` r151 c7 | **不同**：`Function`／無 `the` |

**對已生成 TC 之影響：無。** 觀察面 B 之權威為 **Driver Lockout HMI spec p4**
（R-DD5 所綁），Settings List **未綁於本 feature**，非語料。
**故不回修任何 TC，亦不改 profile §2.1。**

**處置**：登 **A-DD11（INFORMATIONAL，不阻斷）**，載二變體、出處、
「本 feature 以 p4 為準」之判定。**不登 DR** —— 該不一致在未綁之文件內，
若日後綁定該檔或 Settings 側之 popup 進入範圍，再依 A-DD11 處理。

---

## 二、R-DD20 v3（11-1 ＋ DR-DD9 之處置；v1／v2 留存）

執行層 §一-3 之丙案採認：**v2(c) 只書「不變」而所指之字串在 v1**，
且 T-抄 無自撰條文之權——**不自撰為正確**。分析層本輪出 v3 全文，一次解三事。

```
R-DD20 v3（-001／-002 之激勵：Body OFF 同一性、施加式、終止步驟 —— 分析層裁；v3 2026-08-28）

(a) 同一性（marker A-DD10 維持）：同 v2(a) —— CFTS022 `-113` 之
    `Body OFF HU System Sleep Mode` 與 CFTS009 文字層錨點 4941238 之
    同名定義採認為同一（`OFF`／`Off` 之大小寫差屬排版正規化，R-4 同型）。
    殘餘假設＝台架實現與 DR-DD9 回覆之一致性。
(b) 施加式：同 v2(b) —— power 線之通稱式步驟寫法為體例，條件與觀察
    錨定 CFTS009（4941028／4941238／4941100／4941103），不得自編未錨定之
    條件或時序值。
(c) **`-002` 之終止步驟（v3 改述，取代 v2(c) 之「不變」）**：
    業務行照 037 Method 逐字 `Terminate the DD process in the test environment`；
    **不附 `$` 指令行**。理由：IN §5.4 之二行式適用於「步驟需 shell／adb／
    CAN 工具等外部指令」者；本步驟與同則之電源時序步驟
    （`Bring the HU through the Body OFF power down`，亦不附指令）
    **同屬台架程序層級**，其可執行性屬台架程序，**非規格缺件**。
    ER 書可觀察結果 `The DD process is no longer running in the test environment`。
    ~~v1(c)／v2(c) 之 `PENDING: DR-DD9 <…>`~~ **撤** ——
    缺件之認定不成立（037 本以通稱書之，上游未擬給指令），
    IN §8.4.3 之佔位義務於本欄不發生。
    **不得自 SYSAD 取服務名充之（R-DD4）不變。**
(d) DR-DD9 **由必發降為緩發**：process 之具名仍為品質問題（測試員需知終止何物），
    但其缺席不使步驟不可執行，**不阻斷出貨**。回覆到位後得將具名補入步驟。
(e) 代價衡量同 v2(e)。
(f) `TLM_Status.Info`／`$Telematic_Power$` 不用於本二則（同 v2(f)）。
（分析層裁，下放包 19 §二）
```

**效果**：`-002` 之 PENDING 消失 → **可出貨數 23 → 24**，
**唯一阻斷出貨之 DR 消失**。

---

## 三、DR 之調整（T-登）

1. **DR-DD8 文稿**，於 `Request:` 段末**插入一句**（其餘逐字不動）：

> The following bound and shared sources were searched without finding a
> machine-readable form of the table: the SYSRA workbook (no embedded
> objects), the Driver Lockout HMI Logic and Flow document (May 3 2021,
> `L/O`-marked rows only), `DTCs Matrix Core List Rev. 1.6`, and
> `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)` (lockout appears
> only as free-text notes in the Notes column, which itself refers back to
> CFTS022 for the requirements).

2. **DR-DD9** 等級改 **緩發**；`Batch impact` 欄改
   「不阻斷 —— `-002` 依 R-DD20 v3(c) 已可出貨；具名為品質改善項」。
   **文稿本身不動**（其二問仍成立）。
3. **A-DD11** 建條（§1.2 逐字）。

---

## 四、R-DD24（11-3：判定之強度 —— R-DD23 之第四欄）

執行層 §四-2 之 R 注入證明：R-DD23 三欄全合格而結論仍不可信。

```
R-DD24（判定之強度 —— R-DD23 之第四欄）

R-DD23 所列三欄（detail 之數據／判斷本身／所印之理由）皆合格時，
判定仍可能不可信 —— 若其係落於判準序末之 fallback 而非正面命中。

(a) 凡以 first-match／序列判準指派者，須回傳**是否為正面命中**；
    落 fallback 者一律 **WARN**，不得靜默給出結論。
    「什麼都沒命中」與「確定是某某」不是同一件事。
(b) WARN 之 detail 須列出**所有未命中之判準**，非僅書「未命中」。
(c) 分類與覆核自本條起問四欄：數據來源／判斷機制／所印理由／**判定強度**。
（分析層裁，下放包 19 §四）
```

## 五、其餘裁定

| # | 裁定 |
|---|---|
| **11-2** | **接受其為未行使分支，不造注入** —— 造注入須動 `inputs/`（偽造含非 ASCII 之 037 來源列），代價高於所得。已記入 R-G8 界線即可 |
| **11-4** | **舊包不回改**。上繳包為**當輪之紀錄**，其「26 檢」在當輪為真；台帳與現況一律以**最新一包**為準。自本包起，檢數以當輪實數書之並附一句「檢數隨輪次增長」。**此與 §2.4 之過期狀態陳述拘束不衝突** —— 後者規制**現行台帳**之一致，非歷史紀錄之回溯 |
| 10-5（承）| 取樣共用維持接受；**根因仍為 DR-DD8**，§一之查證使該根因更明確（非「沒找」，是「找過且不存在於可得來源」）|

## 六、待 Pei —— 出貨閘（材料已完備）

| | 本包後之數字 |
|---|---|
| 已產出 | **24**（`-001`~`-024`）|
| **可出貨** | **24**（R-DD20 v3(c) 解除 `-002` 之 PENDING）|
| 凍結 | 4（`-025`~`-028`，DR-DD1）|
| 阻斷出貨之 DR | **無** |

**發送清單（本包後）**：

| 級 | DR |
|---|---|
| **必發** | **DD1**（凍 4 leaf）、**DD5**、**DD6**、**DD8**（文稿已加查證範圍）|
| 緩發 | DD2、DD4、DD7、**DD9**（本包降級）|

**分析層意見仍為乙案**（即寫回 24 則，marker 隨之入簿，DR 照發，回覆後機械回修）。
**寫回為 Tier 3 之權，本線不裁。**

## 七、任務（T25）

| # | 任務 |
|---|---|
| T-抄 | R-DD20 v3（v1／v2 皆留存；`ANCHOR_OVERRIDE` 同步補列）、R-DD24 入 `RULINGS.md`；錨點數與停止值同步回報 |
| T-登 | A-DD11 建條；DR-DD8 文稿插句（§三-1 逐字）；DR-DD9 降緩發；marker 表**不加 A-DD11**（INFORMATIONAL，非生成義務）|
| **T25a** | `-002` 依 **R-DD20 v3(c)** 重生成：去 `$` 行、業務行逐字、ER 改可觀察結果；重跑 27 檢 |
| T25b | **T24e 重跑**：應為 **24 可出貨 ＋ 0 不得出貨 ＋ 4 凍結 ＝ 28**，三項覆核全過 |
| T25c | 檢 8 因 `-002` 不再有指令行而**回到 N/A** —— 確認其 detail 書「無適用對象」（R-DD23 之推論），非沿用前輪之 PASS 敘述 |

**不在本輪**：寫回工作簿、git、tsv、`-025`~`-028`。

## 八、上繳包要求（`docs/upstream/16_ship_ready.md`）

T-抄／T-登、`-002` 全文＋27 檢、T25b 之盤點（24/0/4）、T25c 之確認、
未結 DR 清單（依 §六 級別）、獨立自評、R-G8。
