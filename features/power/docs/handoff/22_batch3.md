# 22 — 節奏重整、第二批發現與第三批啟動

下放包 | 分析層 → 執行層 | 往返 NN = 22

前置：`docs/upstream/20_falsifiability.md` 已覆核（ACCEPT）；
21 包之執行狀態不影響本包，其五條裁決（R-P148 ~ R-P152）維持有效。

**分析層已完成第二批之覆核**（R-P152 之啟動條件解除）。
覆核方式：8 個 leaf 之 `source_clause` 與 `reasoning` 全讀；
`018`、`033`–`043` 之 TC 全文；其餘取樣。
**發現四項（T13 ~ T16），其中三項為 leaf 層，一項為 TC 層。**

沿用不變之節：`§C 抽取規格` 同 02 包；`§I 禁區` 同 21 包 §I，另增列見本包 §I。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P153] R-P143 裁定：三對成對錨點**不合併、不刪除**，
         保留現有三條 TC，開 DR-PW10（Medium）。

         20 §二實測之形態一致：含 `RemStartFail` 之一側
         **全部帶 `Model Year: 2017` 且 `State: Under Review`**
         （`4941728` / `4941730` / `4941736`）。

         二項疑點：
         （a）`Model Year: 2017` 出現於 25PI3.5 專案，需解釋
         （b）`State: Under Review` 非最終狀態，
              而 SYS2 匯出無 `State` 欄（20 §2.1 已證），
              故本專案之範圍判定從未看過此欄

         裁定理由：合併會使三條 TC 消失，
         **而其問題是「適不適用」，非「重不重複」** ——
         刪除等同替 RD 作範圍決定。
         保留並標記，比照 R-P121 對 `015` 之處置：
         待決狀態須於工作簿內可見。

         處置：
         （i）`037` / `039` / `042` 之 `remarks` 標明
              「待範圍確認：來源錨點 Model Year 2017 / State Under Review」
         （ii）開 DR-PW10，Urgency **Medium**（不阻斷撰寫，僅影響最終內容）
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P154] T13 —— `SWE-PM-057` 之委出須列 sibling Req ID，
         且該委出可能無人承接。

         其 `reasoning` 載：「刻意略過：`4941706` 之
         『LTM High Radio present』分支明指另一節
         （Auto_SwitchOn_Setting.Req management），依 R-P42
         不在本 leaf 之錨點範圍。」

         **兩項錯誤：**
         （a）**R-P42 用錯** —— `4941706` **在** `source_anchor` 清單內，
              為被引用之錨點。R-P42 管「未被引用者不測」，
              不管「被引用者之某分支得不測」。
              略過該分支之正當依據為 §8.2.1（行為由 sibling Req 承擔），
              而 §8.2.1 **要求列出承擔之 sibling Req ID** ——
              此即 R-P137 對 `SWE-PM-063` 之要求，同型問題未一併處置。
         （b）**委出可能無人承接** —— 該分支所述為
              「LTM High 存在時 `SwitchOff_Timeout_Setting.Req` 如何選」，
              而 `SWE-PM-062`（`025`–`027`）之錨點 `4941710` 所述為
              **`Auto_SwitchOn_Setting.Req` 之三個值**，非同一對象。
              **規格叫人去看那一節，不等於那一節有對應之 leaf 在測它。**

         處置：查 115 leaf 之全部錨點清單，找出承接該分支者。
         （i）找到 → `reasoning` 補列該 leaf 與其 TC id
         （ii）**找不到 → 真 coverage hole**，依 R-P118(d) 裁決；
              若該行為在 115 母體內無 leaf 承接，開 DR
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P155] T14 —— `SWE-PM-062` 之 LTM High 條件須查證分支涵蓋。
         `4941710` 之三個值各帶
         `(If LTM High is present: "Timeout1" = / <> "00 minutes")`。
         查 `025` / `026` / `027` 是否僅測 LTM High **存在**側。
         若是，依 §8.3（mode 為拆分軸）判斷不存在側是否須補測；
         若規格未定義不存在側之行為，登記為
         「規格未定義，不補測」，不得造值（§8.4.1）。
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P156] T15 —— `037` 之 ER1 斷言規格未載之事。
         `037` ER1 載 `The call is released at MaxCallTimeout expiration`。
         Case 2 原文僅載
         `at MaxCallTimeout expiration, TLM sets TLM_Status.Info to
          "Standby" and then it passes to Standby state` ——
         **未載通話被釋放**。轉入 Standby 或致通話結束，然此為推論。

         對照：`040` / `043` 之 ER1
         `The active call is not dropped by the ignition change`
         有原文支撐（`TLM has to manage the phone call(s) and to stay
         in Timed state`），成立。

         處置：`037` ER1 改為僅述有原文依據者；
         **並逐條檢查全批 43 條之 ER，凡斷言通話狀態變化者
         皆須指出其原文依據**，無依據者一併修正。
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P157] T16 —— ER 之斷言不得以本 leaf 範圍外之錨點為依據。
         `038` / `039` 之 ER1 載
         `No call is active when Timeout1 expires and
          MaxCallTimeout does not start`。
         「MaxCallTimeout 不啟動」之依據為 `4941718`
         （僅於 `Phone_Call.Info` 仍 Active 時啟動），
         而 `4941718` 屬 **`SWE-PM-064`**，
         不在 `SWE-PM-038` 之 `source_anchor` 清單內。

         此與 T13 同類：**於 ER 中斷言，而其規格依據落於本 leaf 範圍外。**
         §8.4.2 禁止測試當前 spec 未擁有者；
         ER 之斷言同受此拘束 —— ER 即判準，判準之依據必須在範圍內。

         處置：
         （i）刪除該斷言，或
         （ii）於 `reasoning` 明示其為 sibling Req 之行為、
              本條僅描述觀察到之事實而不以之為 pass/fail 判準
         二擇一，須附依據。
         **並逐條檢查全批 43 條，凡 ER 斷言之依據落於本 leaf
         `source_anchor` 外者，一併處置。**

         此形態應可機械檢查：ER 之具名標的若不出現於本 leaf 之
         `source_clause`，即為候選。評估其可行性；
         可行者實作為 G109，不可行者明列理由。
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P158] 節奏重整：剩餘 103 leaf 以四批完成。

         現況：21 包往返、43 條 TC、11 / 114 leaf。
         **產出端不慢** —— 第二批 8 leaf / 26 條一包完成。
         慢在流程：至少八包為「發現一問題 → 出一包 → 修 → 再發現」
         之單點循環；同一 ER 品質問題歷
         R-P87 → R-P96 → R-P101 → R-P133 → R-P142 五包方定案。

         批次規劃：
         | 批 | Test Set | leaf |
         | 3 | Power State（前半，依 SWE-PM ID 序前 32） | 32 |
         | 4 | Power State（後半） | 31 |
         | 5 | Startup Display | 24 |
         | 6 | Branding and Theme | 16 |

         每批之上繳須含：全部 leaf 之 `source_clause` ＋ `reasoning`、
         反向涵蓋報告全文、`§D` 全表、以及分層取樣之 TC 全文
         （每 leaf 至少一條 ＋ **全部 P0**）。
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P159] 分析層覆核改為按例外，並明載其取捨。
         前二批之覆核顯示投報率懸殊：
         逐條讀 `033`–`043` 十一條僅多抓 T15 一項；
         讀 8 個 leaf 之 `source_clause` 抓到 T13 / T14 / T16 三項。

         往後分析層每批之覆核範圍：
         （a）全部 leaf 之 `source_clause` 與 `reasoning` —— **全讀**
         （b）反向涵蓋報告 —— **全讀**
         （c）TC 全文 —— **分層取樣**（每 leaf 至少一條 ＋ 全部 P0）

         **明載其代價**：非取樣之 TC 未經分析層目視，
         其品質倚賴閘門與執行層自裁。
         前二批已證閘門全綠不代表品質（A-PW64 / A-PW92 / T15），
         **故本規則為速度與覆核深度之取捨，非品質改善**。
         此取捨由 Pei 裁定，登記為已知限制。
         裁決者 Pei，逐字依據：「一次下放」。
```

```
[R-P160] 裁決改為累積式。
         往後分析層之發現先累積，一批一次出條文，
         不再一發現一包。
         **例外**：若某發現會使該批之產出方向錯誤
         （如 R-P125 之 `source_clause` 保真度、
          R-P132 之第二批前置），仍即時下放。
         判準：該發現若不即時處置，是否會導致已產出之內容須重作。
         裁決者 Pei，逐字依據：「一次下放」。
```

## B. 本包須產出

### B1. R-P153 之落實

`037` / `039` / `042` 之 `remarks` 標記；開 DR-PW10（Medium）。
`remarks` 內容須通過 G50 之 §11 規則（R-P131 後 `remarks` 已入 `LONG_FIELDS`）。

### B2. R-P154 之承接查證 —— **最重要**

查 115 leaf 之全部錨點清單（`layer3_full.tsv`），
找出承接「LTM High present → `SwitchOff_Timeout_Setting.Req` 選擇」之 leaf。
（i）找到 → 補列於 `SWE-PM-057` 之 `reasoning`
（ii）找不到 → 依 R-P118(d) 裁決並開 DR
回報查詢方法與其涵蓋範圍。

### B3. R-P155 之分支查證

`025` / `026` / `027` 是否僅測 LTM High 存在側；依 R-P155 處置。

### B4. R-P156 / R-P157 之全批檢查

- 全 43 條之 ER，凡斷言通話狀態變化者 → 指出原文依據；無者修正
- 全 43 條之 ER，凡斷言依據落於本 leaf `source_anchor` 外者 → 依 R-P157 處置
- 評估 G109 之可行性；可行即實作並附 fixture

### B5. 第三批：Power State 前半（32 leaf）

依 R-P158 啟動。tc_id 自 044 起（臨時）。
上繳內容依 R-P158 所列四項。

## D. 閃點

G0 為前置閘。G0–G108 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| G109 | ER 斷言依據落於範圍外（R-P157） | 【可行性評估】可行則實作並以 fixture 證明會 FAIL；不可行則明列理由 |
| G110 | R-P154 之承接查證 | 【實測填入】找到承接 leaf 或判定為 coverage hole |
| G111 | 第三批產出（R-P158） | 32 leaf；`spec_reference` 全部指向 CFTS009 |
| G112 | 第三批反向涵蓋 | 【實測填入】行為項／已覆蓋／無對應；三桶計數與信噪比；事前未知缺口數 |
| G70 | lint 全閘 | 全 PASS；leaf 11 → 43；TC 43 → N |

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

開新號前先查現行最大號並回報（R-P147）。

- 新增：`SWE-PM-057` 之委出誤用 R-P42，且可能無人承接（R-P154）
- 新增：`037` ER 斷言通話釋放，規格未載（R-P156）
- 新增：`038`/`039` ER 之依據落於本 leaf 範圍外（R-P157）
- 新增：成對錨點含 `Model Year 2017` / `State Under Review`，保留待範圍確認（R-P153）
- 新增：分析層覆核改按例外，為速度與深度之取捨，非品質改善（R-P159）

## G. DATA_REQUESTS

新增 **DR-PW10**（Medium）—— 成對錨點之 `Model Year 2017` / `State Under Review` 是否適用本案。
R-P154(ii) 若成立，另開 DR（編號待查後開，R-P147）。
其餘沿用 21 包。

## H. 作業指示

1. G0 前置閘
2. 查現行最大號並回報
3. 落實 B1（R-P153）
4. 產出 B2 承接查證，驗 G110 —— **最重要**
5. 產出 B3 分支查證
6. 執行 B4 全批 ER 檢查；評估並（可行時）實作 G109
7. 產出 B5 第三批，驗 G111 / G112
8. 以 §D 全表自驗
9. §A 八條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md；§G 入 DATA_REQUESTS.md
10. 上繳 `features/power/docs/upstream/22_batch3.md`，更新 `docs/INDEX.md`

## I. 禁區

沿用 21 包 §I 全部條目，另增列：

- **不得合併或刪除三對成對錨點所生之 TC**（R-P153）
- **不得以「規格指向另一節」作為略過分支之依據，須列 sibling Req ID**（R-P154）
- **不得為使 ER 有依據而造值**（R-P156 / §8.4.1）
- **第三批之 leaf 範圍限 Power State 前 32（依 SWE-PM ID 序）**

## J. 本包產生之新條文清單（自檢）

1. R-P153 三對成對錨點不合併不刪除，開 DR-PW10
2. R-P154 `SWE-PM-057` 之委出須列 sibling Req ID，且可能無人承接
3. R-P155 `SWE-PM-062` 之 LTM High 分支查證
4. R-P156 `037` ER 斷言規格未載之事
5. R-P157 ER 之斷言不得以本 leaf 範圍外之錨點為依據
6. R-P158 剩餘 103 leaf 以四批完成
7. R-P159 分析層覆核改按例外，並明載取捨
8. R-P160 裁決改為累積式

逐條確認：**八條**，皆以獨立 fenced block 呈現於 §A，未夾於敘述中。
自檢：§A 區塊數 = 8、§J 列數 = 8、§H 步驟 9 寫「八條」，三處一致。
本次已逐一數過 §A 之 fenced block。

## K. 分析層自判：本包是否仍有該驗而未驗者

**有，三項。**

1. **R-P159 是取捨，不是改善。** 非取樣之 TC 不再經分析層目視，
   而 A-PW64 / A-PW92 / T15 皆證閘門全綠不代表品質。
   本規則以覆核深度換速度，其代價由本條明載，不假裝無代價。
2. **T13 / T16 顯示「ER 依據落於範圍外」可能不只這兩處。**
   B4 之全批檢查為人工，43 條尚可，第三批之後量將增大。
   G109 若不可行，該形態往後只能靠取樣抓到。
3. **21 包之 R-P148 ~ R-P152 若尚未執行，本包與其並行。**
   二者無衝突，但 DR-PW9 與 DR-PW10 之編號須由執行層查後開，
   不得依本包所寫之 `DR-PW10` 逕用（R-P147）。
