# REASONING — 逐 TC 之撰寫理由（暫行落點）

> ## ⚠ **本檔為暫行處置，其落點待裁**
>
> 歷來多條裁定令「記於 `reasoning`」（R-SU35(b)2、R-SU42、`006`／`007` 之情態差、
> D-4 之 `shalll`、T54b…），**而 `feature.yaml` 查無 `reasoning` 欄之映射**；
> 036 母本最接近者為 **`AH` Remarks 備註**，而各批自 pilot v3 起**一律未寫 `AH`**。
>
> **故該等內容至今只存在於腳本註解與台帳中，不隨 TC 走。**
> 交付時之審閱者拿到的是工作簿，不是本 repo。
>
> **三個可能之落點（待裁，不在逕行條件內 —— 其涉交付欄集）**：
> **(甲)** 啟用 `AH` 欄承載；**(乙)** 本檔，交付時附上；**(丙)** 明記 reasoning 不進交付物。
>
> **本輪暫採 (乙)** —— 其為三者中唯一「不動交付欄集且內容不遺失」者。
> **裁定後若取 (甲)，本檔之內容逐列搬入 `AH` 即可；若取 (丙)，本檔改為內部文件。**

---

## batch 1（`Silent Update`）

### `newR1L-SU-001` ← `SWE1-FOTA-175`

- **判定核心之限定**：末行之 `while no safety-related notification condition applies`
  依 **R-SU43 v2(a)** 加註 —— `CFTS057-4907477` 為
  `SHALL NOT be notified **unless** necessary for safety requirements`，
  **明文許可之他值**；不加該限定則本列會判一個合規系統為 fail。
- **其前提掛 `PENDING: DR-SU1`**（安全條件清單未知）。

### `newR1L-SU-002` ← `SWE1-FOTA-176`（facet A）

- **原措辭含造值**：`at any point of the session` **不見於 037 `176` 全文**，
  為分析層所加之強化語，其效果為把一個有例外之規則寫成無例外者。**已刪。**
- 限定與前提同 `001`。
- **保留 `The recorded screen content contains no …` 之句式** ——
  其一，維持與 R-SU36 之連結（該內容為 `as continuous video capture` 所錄）；
  其二，實測若改為 `is displayed on the head unit`，`I-cross` 之
  `IX_NEG` 即不命中，本列會整列掉出跨列比對之範圍。

### `newR1L-SU-003` ← `SWE1-FOTA-176`（facet B）

- **情態問題（待 DR-SU1）**：`4907477` 用 `allow`（許可），
  而本列 ER 斷言「通知**被顯示**」—— **即把許可讀成義務**。
  一個在安全條件成立時選擇不通知之系統並未違反 `allow`。
  **縱使安全條件清單到手，本問仍在。**
- 觀測手段明文化為 `as continuous video capture`，**雖其 ER 為肯定式**
  （R-SU36(a) 不強制）—— 理由為所驗通知之最短持續時間未知（DR-SU1）。

### `newR1L-SU-004` ← `SWE1-FOTA-177`

- 觀測步驟由 `Record every SW Update screen …` 改為
  `Record the head unit screen content as continuous video capture …`
  —— **`every` 是一個宣稱不是一個動作**（R-SU36(c)）。
- 其 proc 3／ER 3 為連帶改動：原文說「所錄下之**各個畫面**」，
  而步驟 2 已不再產生一組畫面而是一段錄影，不改則二步互相矛盾。

### `newR1L-SU-005` ← `SWE1-FOTA-183`

- ⚠ **判定核心失格，成因為規格自身抵觸**（R-SU43 v2(a)）：
  其錨 `4907485`（4.7.3.2 第 3 步）令「完成時顯示成功通知」，
  而同章 `4907477` 令「靜默期間不得通知，除非安全所需」——
  **success notification 是一種 notification**，而本列 pre 明載套件為 Silent Update。
  **改寫解決不了，併入 DR-SU1 之問 (ii)。**

### `newR1L-SU-006` ← `SWE1-FOTA-180`｜`newR1L-SU-007` ← `SWE1-FOTA-182`

- **情態差之記明**：037 為 `shalll not`／`shall not`，
  CFTS `4907482`／`4907484` 為 `MAY NOT display`。
  **SWE.6 以 037 為需求本文**，TC 依 037 之強度撰寫；不改二者、不發 DR。
- ⚠ **`MAY NOT` 於英文有歧義**（「得不顯示」／「不得顯示」）。
  **本列之 R-SU43 通過繫於「037 為需求本文」這一條** —— 若日後改以 CFTS 為準，須重驗。
- `006` 之 `test_item` 上半 **verbatim 保留 037 之 `shalll`**（D-4，拼寫殘留）——
  R-4 僅允句首大寫之正規化，拼寫不在其列。

### `newR1L-SU-008` ← `SWE1-FOTA-184`

- **第三型（R-SU32(iii)），掛 `PENDING: DR-SU2`**：其三類違例
  （prompt／progress notification／confirmation screen）**逐類皆已有專屬 TC**
  （`001`／`006`／`007`），而其獨有之宣稱 `across the three phases`
  **不可觀測**（階段界線於 HU 外部無表徵）。
- 所求為**區辨手段**；若無，其驗證應**併入 `175`**（須上游確認，R-SU32(d)）。

### `newR1L-SU-009` ← `SWE1-FOTA-179`｜`newR1L-SU-010` ← `SWE1-FOTA-181`

- **第三型，掛 `PENDING: DR-SU2`**。`009` 之後果與 `175` 完全相同（不可區辨）；
  `010` 之限定詞 `immediately` **不可量**（下載完成時點無觀測通道，規格未給閾值）。
- ⚠ **`181` 不屬 105 列** —— **R-SU32 v2(e) 之首例**：
  語形判準未攔下它，而它同樣不可完整驗證。

---

## batch 2a（`Interruption Handling`）

### `newR1L-SU-011` ← `315`｜`newR1L-SU-014` ← `318`

- **第四型（R-SU39）：觸發手段不可得** —— 其外部後果**可觀測**
  （版本未變、HU 可操作），缺者為**使該條件發生之手段**
  （`315` 需 socket 層錯誤注入；`318` 需事故偵測訊號而本 feature 未綁 DBC）。
- **DR-SU2(d) 求觸發手段，DR-SU4 求判定準據 —— 二者不互相取代**，
  一者到手而另一者未到，本列仍不可交付。
- ⚠ **不得以「模擬碰撞訊號」充數**（`318`）：訊號名與值域皆無來源，寫之即造值。

### `newR1L-SU-011`–`016`（六列共通）

- **判定核心降為記錄**（R-SU43(f)）：原斷言 `Version_after equals Version_initial`
  **不是規格所允許之唯一結果** —— `4907673` Table 4-6 對「中斷落於 deployment 階段」
  建議 `Complete the deployment`（**版本會變**），
  故依該建議實作之**合規**系統會被原 ER 判 fail。
- **判定核心改掛 `PENDING: DR-SU4`**；版本之讀取與記錄保留為證據。
- ⚠ **暫態**：六列之 Final Step 現字面相同，各列之 (a2) 觸發側狀態退回 ER 前段
  —— **違 R-SU41 全條**（(a) 區分退回前置、(b) Final Step 相同）。
  **DR-SU4 回覆後須依 R-SU41(c) 重建區分並重跑遮蔽測試。**
- `016` 之 ER 第 3 行改為 `The host system connector is disconnected`
  —— 原句斷言 HU 之狀態，**需消歧「HU 是被拔者還是觀察者」**；
  改寫後陳述連接器之狀態，**繞開該消歧而非回答它**（`4907340` 之多主機讀法有據而未消歧）。

### `newR1L-SU-015` ← `319`

- `test_item` 上半 **verbatim 保留 D-1 之缺字**（`the handling of condition`，條件名脫落）。
- **錨不取路徑 A 之首選**：首選 `4907380`（章 4.5.4.1，分 0.174）與本列無關，
  其成因為 D-1 之缺字使本列無詞可共；錨取 **GT-A1 已裁之 `4907671`**。
  **本列為 R-SU14 v5「不取首選為錨」之最強實例。**

### `newR1L-SU-017` ← `313`

- **統攝列，餘量為空**（R-SU37 v2(b)）：其 Description 二句拆解後
  全部由 `315`–`320` 與 `358` 承擔；其餘量（協調行為本身）
  **於其自身 Description 中無文字依據可支撐獨立之驗證點**。
- 曾被考慮而否決之餘量：「多個中斷條件併發時處理錯亂」——
  **問 1 否**（`313` 未提併發）、**問 2 是**（併發屬本組他列）。**推想不是需求。**
- `specification_reference` 取其自證六錨（R-SU15(b)）。

---

## batch 3（`Update HMI`）

### `newR1L-SU-018`–`020` ← `SWE1-FOTA-130`

- **拆三之依據**：三語言為三個獨立之部分失效（法語正常而西語不正常時，
  單一 TC 之判決不可辨）。**肯定式全稱，依 R-SU33(d) 需逐 X 確認**，
  不適用觀測窗法。三 TC 同 trace `130`。
- ⚠ **TC 數與資料軸綁定**：語言集若擴增，TC 數隨之變動而 037 一字未改。
  **現行 N=3 之依據為 037 該列自身之列舉。**

### `newR1L-SU-021` ← `SWE1-FOTA-131`

- **掛 `PENDING: DR-SU5`**：其驗證單元為「伺服器所設之類型決定所適用之流程」，
  **一個 campaign 只有一個類型，故本質上需二次執行**。
  而原第 3 步之「還原至更新前版本」**不可行且不可確認**：
  素材全無降版之需求或程序；`Rollback Protection` 為本 feature 之一個 Test Set，
  **其需求即防止回退**；縱可回退，「與更新前等價」無需求可據以確認，
  **而二次之差異須可歸因於類型方有意義**。
- 措辭改為「回到**可比之起始狀態**」—— **不預設其手段為降版**，
  使 DR 之請求不被一個未經驗證之作法所侷限。
- ⚠ **`131` 之 s4（跨更新類型之一致互動流程）本批未涵蓋** ——
  037 該列標題即以此為名。**見 DR-SU5 請求 2。**

### `newR1L-SU-022` ← `SWE1-FOTA-132`

- **上半取 s3＋s4（相鄰二句）**：s3 即 ER 第 4 行前半之驗證點，s4 即其後半 ——
  **上半與判定對象逐句對應**。原取 s2＋s4 時，**被驗的那句不在上半內**。
- s2（SWMC 查詢客戶接受狀態）為其前置行為，其**狀態**由 pre_conditions 第 3 行承載。
  ⚠ **其行為本身是否仍有 TC 涵蓋，見上繳包 36 §5 之自評。**

### `newR1L-SU-023`／`024` ← `SWE1-FOTA-133`

- **拆二之依據**：「顯示」與「可互動」為二個獨立之部分失效
  （連結顯示而不可點選時，單一 TC 之判決不可辨）。二 TC 同 trace `133`。

### `newR1L-SU-025` ← `SWE1-FOTA-134`

- **標點依 037 原文逐字保留**：`to the user ␣.` 之句點前空格、
  `“Install”`／`“Schedule Later”` 之彎引號（U+201C／U+201D）。
  **R-4 僅允句首大寫之正規化，標點不在其列** —— **非我方打錯。**
- 上半取 s3＋s4，**已刪除自 s2 移接之時間子句** `After completion of the download,`
  —— 原文中該子句修飾「SWMC 提供細節給 HMI」，移接後主詞變為 HMI，
  **產生一個原文沒有的句子（造句非摘句）**。下載完成之時點由 procedure 第 2 步承載。
- ⚠ **引號不一致**：`test_procedure`／`expected_result` 依下放包 41 §3.2 之全文
  用**直引號**，而 `test_item` 為彎引號 —— **同一 TC 內同一標籤二種寫法**。
  執行層依 T32b 未改寫，**待裁**。
- **情態差**：CFTS `4907662` 為 `SHOULD provide`，037 為 `shall provide`；
  依 SWE.6 以 037 為準，差異記此，不改二者、不發 DR。

### `newR1L-SU-026`／`027` ← `SWE1-FOTA-136`

- **配對之依據**（IN §7）：枚舉之支援情形須配至少一個未支援之負向 TC。
- **其區分位於判定對象內**（`offers … an option` vs `offers … no option`），
  滿足 R-SU41(b)。
- 標點依 037 原文逐字保留（`Silent Install flag ␣.`）。

---

## ROV-A（`ROV Installation` 首四列）

### `newR1L-SU-028` ← `SWE1-FOTA-090`

- **`PU0303` 於本 TC 僅為時點指標，不是驗證對象**（下放包 43 §3.1(i)）——
  其作用是告訴測試者「更新已成功、可以切 Body OFF 了」。
  **該彈窗本身之驗證屬 `SWE1-FOTA-088`**（IN §8.2.1，不擴入 sibling）。
- **取彈窗而不取 `$FOTA_Status$` 之依據**（同 §3.1(ii)）：
  後者為 CarPropertyManager 之車輛屬性，**台架不可觀測**（R-SU25(b)）；
  前者之對應關係**載於彈窗清單**（`PU0303` Description 逐字：
  `Shown after a successful update.`），**非推想**。
- `test_item` 上半之 `$FOTA_Status$` 記法**依 037 逐字保留**（R-S4）——
  **上半是需求原文，步驟與 ER 是可執行之描述，二者不必同形。**

### `newR1L-SU-029` ← `SWE1-FOTA-092`

- proc 3 之限定子句 `while $FOTA_Status$ = [Installing FOTA Update]` **已刪** ——
  其為不可觀測之限定，**且刪後 ER 3 仍可判**（錄影中有無安裝進度畫面）。
- 上半保留該訊號寫法（037 逐字）。

### `newR1L-SU-030`／`031` ← `SWE1-FOTA-093`／`094`

- **第四型（R-SU39）：觸發手段不可得** —— 其觀測面（`"Reverted"`／
  `"Walk Home Scenario"` 二彈窗）明確，缺者為**使更新失敗之手段**。
  DR-SU2(d) 之第四型段由 2 列增為 4 列。
- **二者須可互相區辨**：`093` 要求回退**成功**、`094` 要求**失敗未回退**。
  若上游只給「使更新失敗」之單一手段而不能控制回退之成敗，**二列仍不可分**。

---

## 未起草者之預先記錄

### `SWE1-FOTA-104`／`105`／`106` —— 彈窗編號於**二側皆為佔位**

037 引 `PUXXX3`（`104`／`105`）與 `PUxxx1`（`106`，**大小寫與前者不一致**）。

**實測**：二者於 `Pop Up List HMI R1 (26PI).xlsx` **皆非任何一列之 `ID Number`**，
只出現於他列 `Description` 之敘述文字中
（`show TBM Update Popup (PUXXX1)`／`TBM Ongoing Update Popup (PUXXX3)`；
另有 `PUXXX2`、`PUXXX1 b`、`PUXXX3 b`）。

> ### ⚠ **與 A-SU3 形態相同而處置相反，不得比照**
>
> **A-SU3**：一個**已存在**之彈窗被寫錯編號（`PU971` → `PU0971`）——**可推定正解**。
> **本項**：一個**尚未被指派編號**之彈窗 —— **沒有正解可推。**
>
> 二者於清單中皆表現為「查無」。**若台帳只記「查無」，日後會有人比照 A-SU3
> 去推一個不存在的編號。**

**處置（下放包 43 §二 #2）**：其 ER **以彈窗之功能描述指稱**
（如 `the schedule update pop-up`），**不引任何編號**；
**不開 DR**（不阻斷交付），列 `DELIVERY_CHECKLIST.md` **D-9**。
