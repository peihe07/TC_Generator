# Audio Management — 上繳包 11：B3 第二路對帳（R-AM15）

- 日期：2026-08-26
- 對應下放包：`docs/handoff/10_B3_anchor_candidates.md`（第一路）
- 執行層：Claude Code

---

## 一、第二路之語料與獨立性

第一路取 **CFTS019 全文 PDF**（1,730 個屬性物件），故第二路取另一件工件：
**兩本 Basic Report 匯出**（R-AM2 主池，811 物件）。兩者失效模式相反 ——
全文含匯出所遺漏之物件；匯出含全文所無之 SYS2 審查欄與 Category 標記。

`scripts/route2_b3.py` 可重跑。判定以閱讀為之，分數不入判準（R-AM15）。

**一項獨立性之限制須揭露**：對於**池外**之錨，第二路無可用之獨立語料 ——
匯出既無該物件，僅能回讀全文，與第一路同源。此類葉（本批之 291 等）之
「雙路」實為同源二讀，不構成 R-AM15 所要之獨立佐證。此非執行怠惰，
而是 DR-AM3 未結前的結構性限制，見 §五。

## 二、對帳總表

| 類別 | 葉數 | 結果 |
|---|---|---|
| A 級 | 36 | 抽核通過（含 087 之判別，見 §三.1） |
| B 級 | 14 | **10 一致，4 不一致**（§三.2–§三.5） |
| C 級 | 5 | 291 確認可升 A；050／087 確認部分覆蓋；026／076a 維持未決 |

## 三、逐案

### 三.1 SWE1_AMM_087 — 4866221 正確，判別依據補上

包 10 §三.3 請第二路判別 4866221 與 4866223（同文、皆 Atlantis Mid）。

| 錨 | 池 | 本文差異 |
|---|---|---|
| **4866221** | **池內** | 「…according to **HU HMI Specification** and to Routing_Table in {CTS - VP1 and VP2}」 |
| 4866223 | 池外 | 「…according to Routing_Table in …」— **無 HU HMI Specification** |

葉之描述為「依**設定之 HMI 行為**與適用之音訊路由設定」——**兩者兼具**，
唯 4866221 之本文含 HMI Specification。取 4866221。部分覆蓋之判定維持
（Routing_Table 為外部件，併入 DR-AM1）。

### 三.2 SWE1_AMM_088 — **錯配，建議改錨 4866230**

包 10 給 4866309。第二路實測其本文為：

> `In any "Ignition Working Conditions" IF TLM_Status.Info == "Full-Operation"
> OR "Timed" THEN the user can adjust set adjustment of **fader and balance**,
> through signals Fader_Setup.Req and Balance_Setup.Req respectively.`

該物件之題旨為 **fader／balance**，非 SCV。葉 088 為「Full-Operation 或
Timed 下，使用者可經 HMI 啟用或停用 SCV，處理 SVC_Setup.Req」。

正確候選 **4866230**：

> `In any "Ignition Working Conditions" IF STATUS_TELEMATIC.PowerSts_Telematic
> == "Full-Operation" OR "Timed" THEN user can activate or deactivate this
> functionality`（章節上下文為 SCV，見 4866231 之 SVC_Level_Setting.Req）

**錯配之來源可辨**：4866230 與 4866309 為**結構平行句**（同一「Ignition
Working Conditions ＋ Full-Operation/Timed ＋ 使用者可調整」句型，分別套用於
SCV 與 fader/balance 兩個功能）。以句型相似度對位極易互換。

另註：SCV 之啟用／停用細則 4866232／4866233 已於包 10 A 級分派予 089／090，
故 088 不宜再取該二者；4866230 為其上位之啟用權限條款，層級相符。

### 三.3 SWE1_AMM_147 — **錨為序列前提句，需裁定**

包 10 給 4866526，其本文為：

> `IF an Information source is deactivated THEN the following sequence shall
> be performed:`

係**序列標頭**，非行為本體。其下之 4866527「The HU shall store the current
volume level」才是儲存行為 —— 而 **4866527 已於包 10 A 級分派予 158**。

葉 147 為「將最後選用之 Information 音量存入持久儲存，並於該來源再次作用時
回復」，含**儲存與回復兩側**。現況為：儲存側之物件歸 158，147 只剩序列標頭。

**建議**：由分析層裁定 —— (a) 147 與 158 共錨 4866527（R-AM16 允許共錨，
惟括號下半須各異：158 取儲存、147 取回復）；或 (b) 147 錨定 4866526 標
**部分覆蓋**（回復側無獨立物件）；或 (c) 掛 PENDING。第二路不逕定。

### 三.4 SWE1_AMM_055／056 與 072 — **疑似錨定互換**

| 葉 | 包 10 之錨 | 該錨之匯出本文 |
|---|---|---|
| 055（INFO1 音量傳達） | 4866503 | `$VolumeINFO1$ = [Refer to "Volume Level" column in the Information Source Handling Table]` —— **值之定義** |
| 072（並發 Information 之獨立音量控制） | 4866152 | `HU has to send the volume of Information 1 audio output through $VolumeINFO1$, everytime it is changed…` —— **傳達行為** |

葉 055 為「將請求之 INFO1 音量映射至 `$VolumeINFO1$` 並經介面傳送」——
其本體為**傳達**，與 **4866152** 相符；4866503 係查表取值之定義。
056／4866508 同型。

**建議**：分析層複核 055/056 與 072 之錨是否互換。第二路不逕改（R-AM15）。

### 三.5 SWE1_AMM_114／119 — 同文異錨對（非錯配，撰寫注意）

4866299 與 4866308 之匯出本文**逐字相同**：
`IF the user adjusts the Fade/Balance controls THEN the HU shall update the
Fade/Balance HMI within <Tdisp> of adjustment.`

兩葉分別錨定之，屬同文異錨對。撰寫時 tc_title 括號下半須可辨（R-S4）。
`<Tdisp>` 有實值 Max = 100 ms，可入 TC。

### 三.6 SWE1_AMM_291 — 4866826 本文確認，惟屬部分覆蓋

> `4866826: IF $ShiftLeverPosition$ != [R] THEN HU shall perform VR requests
> according to CFTS028 and VR HMI documentation`

與葉「離開 R 檔後 VR 請求恢復」相符，**可升 A 級**。

惟本文將行為推給 **CFTS028 與 VR HMI documentation**，二者皆不在 `inputs/`
—— 與 061／CFTS020（A-AM07）同型。建議標**部分覆蓋**，TC 僅驗「離開 R 後
VR 請求不再被忽略」，細則掛 PENDING，並將 CFTS028 併入 DR-AM6 之範圍
（或另開）。

**獨立性限制**：4866821–4866826 全章池外，第二路只能回讀全文，與第一路同源。

## 四、包 10 之計數標示與 B3 葉集（須更正）

實測（`route2_b3.py` 之解析）：

| 項 | 包 10 標示 | 實測 |
|---|---|---|
| A 級葉數 | 26 | **36** |
| B 級葉數 | 14（§二標題）／12（§六） | **14** |
| §五 之 A+B 錨數 | 39 | **48** |

表格本身之內容無誤，**誤在標題與統計行之數字**。A∪B∪C 之唯一葉數為 **50**，
與批次規模相符（C 級之 291 亦列於 A，026／050／076／087 亦列於 B）。

**§五 之 EE 統計連帶失準**：以 A+B 全 48 錨重算 —— 含 Atlantis High 或 All 者
**39**，僅 Atlantis Mid 者 **9**（19%），非包 10 所記之 27／12（31%）。
DR-AM7 之趨勢判斷（跨批顯著）不受影響，惟本批之比例應更正為 19%。

### 四.1 SWE1_AMM_194 之去向須明示（無聲遺漏之風險）

以包 02 §二 之歸位表推算 B3 應含之 50 葉，與包 10 比對：

- 包 10 有而推算無：`SWE1_AMM_076`（＝076a）
- 推算有而包 10 無：**`SWE1_AMM_194`**（Entertainment Volume Restoration After
  TBM，SYS-RA-AMM-519，Test Set = Volume Control，**尚未交付**）

成因已查明且包 10 之取捨正確：076a 之標題為 *Steering Wheel Information
**Volume** Control*，題旨屬 Volume Control；而包 02 §二 之表僅 317 列
（每個 SWE ID 一列），076a 無獨立列，故推算時其名額由 194 遞補。
框架 `framework.md` 之 Volume Control 計 50、02 表僅 49 列，差額即為 076a。

**風險**：194 未列於 B3，亦未見任何文件明載其遞延。若無明示，該葉將在
批次計畫之算術中消失。**建議於定案錨表明載「194 遞延至 B4」**，
並於 B4 下放時核對。

## 五、DR-AM3 之範圍嚴重低估（新證據，建議升級）

第二路量測匯出之涵蓋率：

| 母體 | 池外比例 |
|---|---|
| 圖表型物件 | 12/13 = 92%（A-AM03 原記） |
| **非圖表之 Subsystem Functional Requirement** | **982/1,562 = 63%** |

**A-AM03 原判之根因「系統性遺漏圖表型需求物件」不完整。** 圖表確為效應最強
之子集，但遺漏遍及一般功能需求：匯出僅涵蓋約三分之一之功能需求物件。

具體實例：**1.3.3.12 Reverse Mute 全章（4866821–4866826）池外**，六個物件
中四個為 `Subsystem Functional Requirement`、皆為普通 IF/THEN 條文、
無一為圖表。

**影響**：DR-AM3 現行請求範圍為「chapter-level 重匯，涵蓋 1.3.3.11 與導航
Fade-Out 段，非僅圖表型物件」——依本證據仍然過窄。建議改請**全文件重匯**，
並於 DR 中附本節之量測。

**連帶**：R-AM2 所定之錨源池（兩本 Basic Report）僅涵蓋約 37% 之功能需求，
第二路之獨立語料因而對池外葉恆不可用（§一之限制）。此為 R-AM15 雙路制之
結構性上限，非個案問題。

## 六、待分析層裁定

1. 088 改錨 4866230（§三.2）。
2. 147 之處置三選一（§三.3）。
3. 055/056 與 072 之錨是否互換（§三.4）。
4. 291 升 A 並標部分覆蓋；CFTS028 是否併入 DR-AM6（§三.6）。
5. 包 10 之計數標示與 EE 統計更正（§四）。
6. **194 之遞延明載**（§四.1）。
7. DR-AM3 範圍是否依 §五 升級為全文件重匯。

## 七、未動之項

026（目標音量）、076a（方向盤音量）維持 C 級未決 —— 第二路以匯出語料
複查，`StWhl_Volume`、`steering wheel` 於匯出同樣零命中，
`target volume` 亦僅命中斜坡函數定義，與第一路結論一致，無新證據。
