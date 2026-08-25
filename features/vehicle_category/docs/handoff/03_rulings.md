# 下放包 03 —— Vehicle Category 裁定（上繳包 02 §9 待裁四項）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/03_rulings.md`
- 前一包：`docs/handoff/02_rulings.md`
- 對應之上繳包：`docs/upstream/02_rulings.md` §9「待裁」四項

---

## 〇、本包之性質

上繳包 02 之 T10–T18 九項全數完成、T12 為 30/30、Phase 1 收斂。
本包裁定其 §9 所列四項，新立 R-VC11 / R-VC12 兩條、A-VC9 一筆、
DR-VC6 / DR-VC7 兩筆，並**修訂 R-VC3 之表 B 母體**。

**本包再次更正下放包 01 之實質錯誤（§4.2(b) 之摘要文字），
其性質與 A-VC5 同源 —— 見 §二。**

---

## 一、先認第二次同類錯誤

上繳包 02 §7.3 查出：下放包 01 §4.2(b) 對 **§15（11 個 EPB PU id）**
與 **§10.1／10.2（Type / Power Source / Last State 四種組合、
Last State 之可用條件）** 之摘要，描述了 repo 權威素材中**不存在的文字**。

成因與 A-VC5 同源，是同一個病的第二次發作：

| | A-VC5 | 本次 |
|---|---|---|
| 表象 | 斷言九欄全為 `\xa0` | 摘要描述圖內內容為規格文字 |
| 實情 | 該九欄從未被讀取 | 讀的是衍生 PDF 之圖層判讀 |
| 共同病灶 | **把不可靠或不存在的來源，以實測值之格式寫入下放包** | 同 |

R-VC7 已裁「衍生物不得作為判準來源」，而這兩處摘要**正是那樣的判讀** ——
即 R-VC7 所禁之事，在下放包 01 中已經發生過，只是當時未被識別。

執行層之處置（DR-VC3 改寫措辭、表 B 不寫入摘要文字、不使用 OCR、
不對圖作視覺判讀）**全部正確**，本包予以追認並條文化。

---

## 二、裁決條文（逐字抄入 `RULINGS.md`）

> 逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。抄畢附 byte-level diff。

```
R-VC11（TC priority 之判定；R-VC6(a) 之落地）

037 `Analysis Report` 欄 18 `Priority` 之實測分布為
High 28 / Medium 88 / Low 1（117 leaf）。

**該欄係按規格章節整批賦值，非逐 leaf 判斷**（證據見 A-VC9）：
  章 4/5/6/7（Glove Box 全部）      → High  12，章內無例外
  章 13（Settings Behavior/Ignition）→ High  16，章內無例外
  章 2/3/11/12/14                   → Medium 88，章內無例外
  章 16（Cabrio Widget）             → Low    1
且欄 18 **無對應之 Description-Action 欄**，037 未載其判準。

故：**不得建立 High/Medium/Low → P0/P1/P2/P3 之機械映射表。**
機械映射會將一個判準不明、粒度為「章」的量，搬入一個判準明確、
粒度為「TC」的欄位 —— 其結果具有實測值之外觀而無實測值之內容，
即 IN §8.4.1 所禁之造值換一種形式。

TC 之 `priority` 依下列三層決定：

(a) **主判準** —— IN §10.2 之 P0–P3 rubric，逐 TC 判定。
    該 rubric 有明確定義（P0 安全／開機／連線／音訊輸出／eCall／
    車輛關鍵 CAN／資料遺失風險；P1 主要使用者功能或關鍵操作邏輯；
    P2 次要／支援功能；P3 次要 UI、低影響客製、罕用情境、外觀細節）。

(b) **上游約束** —— 037 Priority 為**邊界**而非映射來源：
      037 = High → 該 leaf 所衍生之 TC **不得低於 P1**
      037 = Low  → 該 leaf 所衍生之 TC **不得高於 P3**
      037 = Medium → 不設邊界（該格含 88 筆語意跨度極大之需求，
                     不具區辨力）
    此為 R-VC6(a)「不得於忽略本欄之情況下本地推導」之落地形式：
    本欄之資訊被用於設界，而非被抄寫。

(c) **分歧揭露** —— 依 (a) 所判與 037 之值語意相悖時
    （例如本地判 P0 而 037 為 Medium、本地判 P3 而 037 為 High），
    須於該 TC 之 `reasoning` 記明分歧與本地判定之依據，
    引 §10.2 之對應款。**不得為求一致而遷就任一方。**

R-VC6(a) 之「priority 欄不得產出」之凍結，於本條落地後**解除**。

DR-VC7 之回覆若載明 037 之 Priority 判準，本條 (b) 之邊界重審。
```

```
R-VC12（§4.2 分類之修訂；圖內內容之處置）

**一、16.1 改列 (a)，表 B 母體由 18 節改為 17 節。**

上繳包 02 §7.4 之觀察成立：SYS1 `Description` 所載 16.1 之內容為
「Refer to the Vehicle Category - Cabrio Rooftop and Cabrio Wind
Draught Deflector HMI sections for complete logic.」——
其為**交叉引用**，非該節自身之實質需求內容，與 §4.2(a) 之
「非需求性質」同類。

下放包 01 §4.2 之計數修訂為：
    未引用 42 節 ＝ 非需求性質 **25** 節 ＋ 有實質內容 **17** 節
（原為 24 ＋ 18）

R-VC3 所稱「表 B｜覆蓋落差揭露」之母體隨之改為 **17 節**：
  8.1, 8.2, 8.3, 8.4, 8.5, 9.1, 9.2, 10.1, 10.2,
  11.9, 11.9.1, 11.9.2, 11.9.3, 14.2, 15, 16.2.1, 16.2.2

R-VC3 之其餘部分（117 leaf 全取、表 A、兩表為出貨門檻）**不變**。

**二、下放包 01 §4.2(b) 之摘要文字，就下列各節作廢。**

  §15         —— 「PU0132…PU0275 之訊息文字與逾時」
  §10.1／10.2 —— 「Type / Power Source / Last State 之四種組合、
                  Last State 之可用條件（Latching + Ignition）」

依 R-VC7，該等文字係讀 Project 附件之衍生 PDF 所得，
repo 權威素材（SYS1 `Description`、repo PDF 文字層）皆不載之，
其內容僅存於 `(image: imageNN.png)` 佔位之後。

拘束：
(a) 表 B 之該三節，「內容」欄一律書
    「該節內容僅存於圖，SYS1 匯出未帶文字」，**不得寫入任何摘要文字**。
(b) DR-VC3 對該三節之提問同此措辭（執行層已實作，予以追認）。
(c) §8.3 為**摘要漏列**而非錯誤（權威素材另載
    「A graphic representation of the vehicle status will be present
    on pop up」）。表 B 之該節內容補入此句，來源記為 SYS1 `Description`。
(d) 其餘 13 節之摘要經 T17 驗為「與 SYS1 所載相符」，予以保留，
    惟其效力僅及於「與 SYS1 相符」，**非「與規格原件相符」**
    （FO §3 Mode A 之盲點，執行層已於上繳包 02 §10 揭露）。

**三、通則。**
分析層日後對任何規格內容之摘要，其來源須為 repo `inputs/` 之權威複本；
以 Project 附件、衍生 PDF、OCR 或圖之視覺判讀所得者，
一律不得以實測值之格式寫入下放包。
如確需引用圖內內容，須標為「圖內內容，未經文字層確認」並登記 DR。
```

---

## 三、A-VC9（新立）

```
A-VC9（037 Priority 按章節整批賦值）

037 `Analysis Report` 欄 18 `Priority` 於 117 個 leaf 之分布，
按規格章節完全分群，每章內部無任何例外：

  章  4  Glove Box – Activation         High    4
  章  5  Glove Box – Activation Error   High    3
  章  6  Glove Box – Deactivation       High    3
  章  7  Glove Box – Deactivation Error High    2
  章 13  Settings Behavior/Ignition     High   16
  章  2  Vehicle Category Notes         Medium 24
  章  3  Controls                       Medium 17
  章 11  Settings Templates / Notes     Medium 20
  章 12  Settings                       Medium 25
  章 14  EPB Service Mode               Medium  2
  章 16  Cabrio Widget                  Low     1

即：Priority 之粒度為「章」，非「leaf」。

佐證其粒度不足之一例：章 14（EPB Service Mode，煞車服務模式，
含車輛在動時之禁入條件）與章 12（Settings，含字型與清單排列）
同為 Medium。二者於 IN §10.2 之 rubric 下語意相距甚遠。

另：欄 18 為 037 九個分析欄中**唯一無對應 Description-Action 欄**者
（欄 10/11、12/13、14/15、16/17 皆成對，欄 18 無配對），
故 037 未載其判準。

處置：不回報為缺陷 —— 按章賦值可能是上游之刻意作法。
以 DR-VC7 查詢其判準；在回覆前，依 R-VC11(b) 僅取其為邊界。

狀態：PENDING（待 DR-VC7）。
```

---

## 四、DR-VC6 / DR-VC7（新立）

| DR | 標的 | 內容 | 阻斷範圍 |
|---|---|---|---|
| **DR-VC6** | 規格作者 | 規格 §15（EPB 彈窗表：PU0132/0133/0134/0136/0139/0141/0143/0144/0145/0202/0275 之訊息與逾時）與 §10.1／10.2（Aux Switch 之 Type / Power Source / Last State 組合表及 Last State 之可用條件）之內容僅存於投影片圖中，SYS1 Polarion 匯出未帶文字（`(image: imageNN.png)` 佔位）。若該二節需納入測試範圍，請提供其文字版本或可讀之來源 | **條件性** —— 該二節皆在 037 未涵蓋之 17 節內，依 R-VC3 本次不產出 TC。**僅當 DR-VC3 回覆為「應補」時始為必要素材**；DR-VC3 回覆前不催 |
| **DR-VC7** | 037 作者 | 欄 18 `Priority` 於 117 個 leaf 按規格章節整批賦值（High 28 / Medium 88 / Low 1，每章內部無例外，證據見 A-VC9），且該欄為九個分析欄中唯一無 Description-Action 配對者。請說明其賦值判準，及 Medium 一格（88 筆）內是否有更細之區辨 | 不阻斷 —— R-VC11 已裁定其僅作邊界使用。回覆到後 R-VC11(b) 重審 |

**發送批次**：DR-VC7 與 **DR-VC2**（Source Requirement ID）、
**A-VC2**（封面 Reviewer／Date）同為對 037 作者之說明性查詢，
**同批發送**，一次往返。DR-VC6 待 DR-VC3 回覆後另批。

DR 由 Pei 發出（Tier 3），執行層只建檔不發送。

---

## 五、上繳包 02 §9 其餘二項之裁定

**第 3 項｜16.1 之分類** → 裁定改列 (a)，見 R-VC12 一。
執行層「未自行改分類，僅回報」為正確處置 —— 該切分為 R-VC3 表 B 之
母體，變更確屬 Tier 2。

**第 4 項｜A-VC8 之修法時程（`leaf_count` assertion）**
裁：**維持 PENDING，不排入本 feature 之任何 Phase**，處置同 A-VC4。
理由：117 之守護目前由 T4／T12 之集合相等判定承擔（非計數相等，
「數目對但成員錯」會被抓到），且每包負 R-VC9 之揭露義務。
此為人工守護，但**不是無守護** —— 在此前提下，工具修法之急迫性
不足以插隊全域排程。

**R-VC8 之授權範圍再申明**：不得順手併入 A-VC4（`new_feature.py`
之 abbr 推導）、A-TM04（slugify）、A-VC8（`leaf_count` assertion）。
四者標的各異，併案即失去授權邊界。

---

## 六、執行層續作任務

| # | 任務 | Tier |
|---|---|---|
| T19 | 抄錄 R-VC11 / R-VC12 入 `RULINGS.md`（接 R-VC10 之後），附 byte-level diff | 1 |
| T20 | `ANOMALIES.md` 新增 A-VC9（條文逐字）；A-VC8 補記 §五第 4 項之裁定理由 | 1 |
| T21 | `DATA_REQUESTS.md` 新增 DR-VC6 / DR-VC7（含阻斷範圍與發送批次），更新未結清單為 **七筆** | 1 |
| T22 | 依 R-VC12 一，將 `docs/handoff/01_intake_recon.md` §4.2 之計數修訂記入 `DECISIONS.new.md` 或本 feature 之修訂紀錄。**下放包 01 之原文不改** —— 其為已交付之軌跡，修訂以本包為據（R-TM13：不刪除，加註保留）| 1 |
| T23 | 依 R-VC12 二，產出**表 B 之草稿**（17 節，含 §8.3 補入之句、三節之「僅存於圖」措辭），置於 `data/` 或 `docs/`。**草稿而非交付件** —— 交付時之最終措辭待 DR-VC3 回覆 | 1 |
| T24 | 依 R-VC11 產出 **priority 判定草案**：以 IN §10.2 rubric 對 117 leaf 逐項預判 P0–P3，並標出與 037 邊界 (b) 衝突者。**只產出草案供裁，不寫入任何 TC 欄位** | 1 |

**不在本輪範圍**：`framework.md`（Phase 3）、profile、任何 TC、
任何寫回、任何 git 操作、Phase 2 之 `DECISIONS.md` 簽署。

> T24 之草案為 Phase 4／6 之前置。R-VC6(a) 之凍結已由 R-VC11 解除，
> 但**解除的是「不得產出」，不是「可逕自定案」** —— 草案仍須經裁。

---

## 七、上繳包要求

`features/vehicle_category/docs/upstream/03_rulings.md` 須含：

1. T19–T24 逐項結果，附實際指令與原始輸出
2. R-VC11 / R-VC12 之 byte-level diff 核對
3. T23 之表 B 草稿全文（17 節逐節）
4. T24 之 priority 草案全表（117 leaf），含與 037 邊界衝突者之清單
5. 更新後之未結 DR 清單（七筆）與 A 清單
6. 量測條件揭露（R-G8）：T24 之判定方法、其主觀成分之範圍、偽陽性風險
