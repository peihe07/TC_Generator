# 上繳包 03 — R-C5-1／R-C11 落實 ＋ 17 節適用性判讀

執行層 → 分析層。2026-08-14。回應下放包 `05_rc5_correction.md` §6
與 `06_source_singularity.md` §3／§4。

**結論：六項作業全部完成。判讀結果 10 `in_scope`／7 `undetermined`／
0 `out_of_scope`。** `DECISIONS.md` 未簽署，Phase 3 未開始。

另有一項判讀陷阱與一項上游矛盾須分析層知悉 —— 兩者都會改變 D-C10 的
輸入，且都不是形態問題。

---

## 0. 置頂：兩件影響 D-C10 的事

| # | 事項 | 為何重要 |
|---|---|---|
| **甲** | **CFTS043 寫的是 "Altern*ate*"，SR24 寫的是 "Altern*ative*"** —— 以 SR24 自己給的名稱搜尋 CFTS043 得 **0 命中**。若就此收手，10 節會被判 `out_of_scope`，且該結論會有完整的依據外觀 | 判讀方向會完全相反。A-CF11 |
| **乙** | **CFTS043 4803259 之 NOTE 與其自身 metadata 矛盾** —— NOTE 稱「only applicable to R1H」，同 item 之 `Radio` 含 `R1L-R` 且該節 30 個 item 全部 `Scope=Yes` | 10 節之 `in_scope` 繫於「採結構化欄位而非散文」這個**選擇**。A-CF12 |

---

## 1. §6.1 條文貼入

`RULINGS.md` 現載 **R-C1 ~ R-C11 + R-C4-1 + R-C5-1**，共 13 條，全部原文照錄。

- **R-C5-1** 置於 R-C5 所屬區塊之後、R-C4-1 之前（05 §6.1「置於 R-C5 之後」）。
- **R-C11** 另立小節，並標注其推廣段適用全 feature、安置位置待 canon
  re-sync（06 §5）。

## 2. §6 / 06 §1 —— R-C11 刪除，前提逐項確認在先

刪除不可逆，故**先驗後刪**：

| 前提 | 實測 | 結果 |
|---|---|---|
| `spec-index/cache/` 該份仍在 | 存在 | ✅ |
| 大小為 70,040 bytes | 70,040 | ✅ |
| **（自加）兩份內容相同** | 兩者 SHA256 皆 `6982d37db81b36e4…` | ✅ |

第三項為執行層自加。條文只要求確認「在且大小相符」，但**「大小相同」不蘊含
「內容相同」**，而刪除的正當性取決於後者。兩份逐位元組相同，故刪除不損失
任何內容。

若兩者曾分歧，本次比對就是唯一會發現它的時機 —— 這正是 R-C11 立條的理由
（兩份副本分歧時無任何機制會報錯）。實測未分歧，但這個結論只有做了比對
才講得出來；不做比對而刪，講得出來的只有「大小一樣」。

**刪後複測**：`spec-index/` 該份仍在且仍為 70,040 bytes；`recon.py` 四個
assertion 全 PASS（129/129 outline 查得，miss=0）；`feature.yaml` 之
`../../spec-index/…` 路徑照常解析，**未改為 `inputs/`**（R-C11 明文）。

登記 **A-CF10**。附註：`inputs/` 列於 `.gitignore`，該副本從未進版控，
故此刪除無 git 歷史可回溯；可回溯者為 `spec-index/cache/` 之同內容檔案
與該條紀錄。

## 3. §5 / 06 §3 —— 17 節適用性判讀

`data/sr24_substantive_applicability.tsv`，欄位依指示：
`outline`｜`scope_verdict`｜`basis`｜`variant_condition`。
17 節與 A-CF08 之 substantive 集合**對稱差為空**（機械比對）。

| verdict | 節數 | 節次 |
|---|---|---|
| `in_scope` | **10** | 20.1、20.1.1、20.1.2、20.1.3、20.2、20.3、20.4、20.4.1、20.4.2、20.4.3 |
| `undetermined` | **7** | 16.1、18.2、18.3、18.4、19.1、19.2、19.3 |
| `out_of_scope` | **0** | —— |

### 3.1 20.x 十節 —— `in_scope`，依據逐層具名

SR24 §20 標題自身寫 `See CFTS043 for applicable vehicles`，故 CFTS043 就是
該指示所指的判準來源。對應節為 **CFTS043 §1.3.5.1.22 Alternate Rear Blower
Control Softkeys**（items 4803257–4803286，含三個子節 Power／Select／Lock
Softkey）。

**關鍵發現：tree view 有它自己的 R1L-R scope 白名單。** 該 workbook 之
`Scope` 欄由 sheet `工作表1` 驅動 —— 599 筆 `ReqIF.ForeignID` 的明列清單，
全表 4,264 列中 709 列命中。這不是推論出來的範圍，是**這份檔案自己對
「什麼在 R1L-R 範圍內」的表態**，也是本判讀最直接的依據。

實測該節 33 個 item：

| | 數 | 說明 |
|---|---|---|
| `Scope=Yes` | **30** | 全部實質需求與標題 |
| 非 `Yes` | 3 | 4803258／4803274（空 Description 之版面 artefact）、4803273（`Radio=noSys`） |

且 30 者之 `Radio` 皆含 `R1L-R`、`Market` 皆為 `All`。

**`EE Architecture` = Atlantis Mid 不構成排除**，這點需要說明：該批 item 之
EE 為 Atlantis Mid，而本交付為 R1LR **ATL-H**。看起來像矛盾，但實測
`Scope=Yes` 之 709 列中，EE 分布為 Atlantis High 264、Atlantis High+Mid 151、
Atlantis Mid+High 131、**Atlantis Mid 130**、All 21 等 —— **白名單同時含
High 與 Mid**，故 EE **不是**本檔的 scope 閘，`Scope` 欄才是。若 EE 是閘，
白名單裡不會有 130 列純 Mid。

逐節條文對應（抽驗，非全稱）：

| SR24 | CFTS043 |
|---|---|
| CRB3「Fan ranges: 1-4」 | 4803264「`$R_BLW_Speed$` shall range from 1h-4h. 0h = OFF」 |
| CRB2「REAR LOCK has on / off state」 | §1.3.5.1.22.3 Lock Softkey（4803279–4803286） |
| CRB4「Rear Blower climate off has on/off state」 | §1.3.5.1.22.1 Power Softkey（4803266–4803273） |
| CRB4.2「front ventilation mode not front/front+feet → grey out」 | 4803261／4803262（softkey 僅於 `$FT_HVAC_MD_STAT$` = Panel／BiLvl 可用） |

**`variant_condition`（全 10 節共通）**：
`$Indipendent_Rear_Fan$ = [Present]`（CFTS043 4803260：「The requirements in
'Alternate Rear Blower Control Softkeys' section shall be supported when PROXI
parameter `$Indipendent_Rear_Fan$` = [Present]」）。

這是**條件，不是排除**，但意味著日後 TC 之 Pre-Condition 必須寫明該參數，
不可預設其存在。另注意：SR24 以 **LATAM** 為該功能之標題修飾，而 CFTS043
以 **PROXI 參數**決定適用性、從不提 LATAM —— 兩者的適用性模型不同，
TC 若照 SR24 標題寫成「LATAM 市場」會與 CFTS043 不符。

### 3.2 七節 —— `undetermined`，缺什麼逐項具名

**判 `undetermined` 而非 `out_of_scope`：CFTS043 不涵蓋這三類判準，
而非否定它們**（06 §3 明文）。實測其涵蓋範圍：

| 搜尋字串 | 主檔（442 頁） | tree view Description |
|---|---|---|
| `Comfort Widget` | 0 | 0 |
| `Home screen` | 0 | 0 |
| `10.25` | 0 | 0 |
| `EMEA` | **0** | **0** |

- **18.2–18.4（10.25"）與 19.1–19.3（7"）**：需 R1LR ATL-H 之機種／螢幕尺寸
  配置來源。CFTS043 是 HVAC controls 規格，不承載 home-screen widget 之
  scope。SR24 §1.1 確實把 7" 列於本文件涵蓋之機種中，但 06 §3 已明示
  **「spec 有寫」不等於在交付範圍內** —— 該句列舉的是文件涵蓋範圍，
  不是本次交付的機種。→ `DATA_REQUESTS.md` #6。
- **16.1（EMEA ICS CARRYOVER）**：需市場適用性來源。CFTS043 之 `Market` 欄
  全部相異值僅 `All`／`NAFTA`／`NAFTA - Mexico`／`NAFTA - United States,
  Canada` —— **無 EMEA 值**，且 `Scope=Yes` 之 709 列 `Market` 全為 `All`，
  該欄無法據以納入或排除任何市場。其 11 列 in-scope `ICS` 內容是 ICS 硬體
  （rotary knob、lost communication），非 EMEA ICS 氣候畫面。
  → `DATA_REQUESTS.md` #7。

### 3.3 ⚠️ 甲 —— "Alternative" vs "Alternate"（A-CF11）

| 搜尋字串 | 主檔 | tree view |
|---|---|---|
| `Alternative Rear Blower`（**SR24 之用詞**） | **0** | **0** |
| `Alternate Rear Blower`（CFTS043 之用詞） | 7 | 10 |
| `LATAM` 與該功能相關者 | 0 | 0 |

**若就此收手會發生什麼**：依 SR24 §20 標題的指示去查 CFTS043，用 SR24 自己
給的名稱，得 0 命中 → 結論「CFTS043 未涵蓋此功能」→ 10 節判
`out_of_scope`。該結論會有**完整的依據外觀**：查了指定文件、用了文件指定的
名稱、留了搜尋紀錄。而它與實測（30 個 item 全部 `Scope=Yes`、`Radio` 含
R1L-R）**方向完全相反**。

**與 06 §3 所防形態的差別**：條文防的是「讀不到 → 判 out_of_scope」。
本例更隱蔽：**不是讀不到，是用錯字串去讀而讀不到**，而錯的字串是文件自己
給的。零命中被當成陰性結果使用，但它其實只是索引層事實 —— 與 Privacy
R22-2「以檔名為索引之比對，其陰性結果只能陳述索引層事實，不得升格為內容層
結論」同構。

**實際如何撞見**：改以三路交叉 —— 先全列舉語義相關者（`Rear Blower`，
109 blocks）、再篩 `Radio` 含 R1L-R（19）、再讀該批所屬節 —— 才在第三步
看到 "Alternate Rear Blower Control Softkeys"。**零命中應觸發換路徑，
不應觸發下結論。**

### 3.4 ⚠️ 乙 —— CFTS043 4803259 之 NOTE 與其 metadata 矛盾（A-CF12）

item 4803259 全文末句：

```
NOTE: The requirements below are only applicable to R1H starting on SR22.
```

| 來源 | 陳述 |
|---|---|
| 該 NOTE（散文） | below 之需求**只**適用 R1H |
| 同 item 之 `Radio` 屬性 | `R1L-R, R1L, R1H` —— **含 R1L-R** |
| tree view `Scope` 欄 | 該節 30 個 item **全部 `Scope=Yes`**（R1L-R 白名單） |

散文說只有 R1H，結構化欄位說含 R1L-R 且在 R1L-R scope 內。**兩者不可能
同時為真。**

**本次採結構化欄位**，理由：`Scope` 欄是該 workbook 為 R1L-R 專門建立之
白名單（599 筆明列 ForeignID），是本檔對「什麼在 R1L-R 範圍內」最直接的
表態；而 NOTE 之措辭（"starting on SR22"）讀來像歷史沿革註記，可能未隨
R1L-R 納入而更新。

**但這是選擇，不是推導。** 若 NOTE 為準，10 節應為 `out_of_scope`。
D-C10 裁定前必須知悉：`in_scope` 這個結果**繫於此選擇**。
已開 `DATA_REQUESTS.md` #8 請上游釐清（RD-1 候選，不阻塞）。

### 3.5 未做者

不產 TC、不入 coverage 分母、不列 BLOCKED、不補 RD 項目、未改 R-C5 或
R-C5-1。判讀為量測，非處置（06 §3）。

## 4. §6.2 / 06 §4.2 —— anomaly 更新

| # | 動作 |
|---|---|
| A-CF08 | 更新：16 節退出 R-C5（R-C5-1）；併記 17 節判讀結果與依據 |
| A-CF09 | **範圍限縮**為 `home`／`projection`／`privacy` 三者；amfm、sxm **不在其列**；`media` 無該檔另記 |
| A-CF10 | 新登（CLOSED）：`inputs/` SR24 副本已刪，前提三項留痕 |
| A-CF11 | 新登（OPEN，方法論）："Alternative" vs "Alternate" |
| A-CF12 | 新登（OPEN，RD-1 候選）：4803259 NOTE 與 metadata 矛盾 |

`DATA_REQUESTS.md` 新增 #5（CFTS043，已解）、#6（機種／螢幕配置，**High**）、
#7（EMEA 市場，**High**）、#8（NOTE 釐清，Medium）。#6／#7 是本 feature
**第一次出現的真正缺檔**。

## 5. §6.5 / 06 §4.3-4 —— 未簽署、Phase 3 未開始

- `DECISIONS.md` **未簽署**（Tier 2）。Sign-off 仍為空白範本，recon 每次跑
  仍發 R-C10 警告，屬正確狀態。第 6／10 項之調整建議（05 §4：exemplar
  具名 `home`；pilot 取第 13 章）**未代為寫入** —— 那是簽署時的裁量。
- **Phase 3 未開始**：未寫 framework Part N、未寫 profile、未建 Test Set 表。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 6.1 已驗

1. R-C11 刪除之三項前提（存在、70,040 bytes、SHA256 相同），刪後複測四個
   assertion 全 PASS。
2. CFTS043 tree view 之 `Scope` 白名單機制（599 筆 ForeignID，709 列命中）
   與 Alternate Rear Blower 節之 30/33 命中。
3. `Scope=Yes` 集合之 EE 分布（High 264 / Mid 130 …），據以判定 EE 非 scope 閘。
4. CFTS043 對 `Comfort Widget`／`Home screen`／`10.25`／`EMEA` 之涵蓋（皆 0）。
5. 17 節與 A-CF08 substantive 集合之對稱差為空。
6. `.doc` 可解析（`textutil`，442 頁 → 1,739,548 bytes 文字）—— **無工具缺口**，
   故未登 06 §3 所預留之工具異常。

### 6.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **4803259 NOTE 之效力** | 需上游確認，非本地可驗 | **高** —— 10 節之 `in_scope` 繫於此。已開 DR #8 |
| 2 | **7"／10.25" 是否屬本交付機種** | 判準來源不在 `inputs/`（DR #6） | **高** —— 6 節維持 undetermined |
| 3 | **EMEA 是否屬本交付市場** | 判準來源不在 `inputs/`（DR #7） | 中 —— 1 節維持 undetermined |
| 4 | **20.x 逐節之條文級對應** | 只抽驗四條（CRB3／CRB2／CRB4／CRB4.2），未逐節逐句比對 | 低 —— scope verdict 立於**節級**依據（SR24 §20 標題指向 CFTS043、該節全部 `Scope=Yes`），不繫於逐句對應。逐句對應是 Phase 4 寫 TC 時的工作 |
| 5 | **`$Indipendent_Rear_Fan$` 之實際配置值** | PROXI 參數值不在任何已有素材中（Privacy 亦曾遇同類，其 RD-1 #11） | 中 —— 不影響 scope verdict，但影響 TC 之 Pre-Condition 能否寫出具體值 |
| 6 | A-CF02 交付夾、A-CF06 PDF text layer | 狀態未變 | 低 |

第 4 項需要說明界線：本次判的是**「這 10 節該不該由 Comfort R1L-R 驗證」**，
不是「這 10 節的每一句在 CFTS043 都有對應」。後者若有缺口，是 spec 一致性
問題，屬 Phase 4 逐條展開時才會浮現，且不會反過來推翻節級的 scope 判定。

### 6.3 未做、亦未偷做者

- 未簽署 `DECISIONS.md`；未代寫 05 §4 之兩項調整建議。
- Phase 3 未開始。
- 未對 17 節之任何一節做 TC 處置。
- 未改 R-C5、R-C5-1 或任何既有條文原文。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 6.4 執行層對「本包可否結案」之判斷

**可結案。** 判讀已產出且依據逐節具名；7 節之 `undetermined` 各有具名缺料
並已開 DR，非含混。

**但 D-C10 現在還不宜裁**，理由是乙項（A-CF12）：10 節之 `in_scope` 繫於
「採結構化欄位而非散文 NOTE」這個選擇。若 D-C10 在此矛盾釐清前裁定，
裁的是一個**建立在單方選擇上**的判讀結果 —— 而該選擇本身有 50% 的機率
是錯的方向（NOTE 若有效，10 節全部翻面）。

DR #8 之釐清成本低（單一問句），相對於「10 節全部翻面」的代價，值得先問。

Phase 3 Part N 之切分母體因此仍未定：現況是 403 leaves 確定 ＋ 10 節
待 D-C10 ＋ 7 節待缺料。
