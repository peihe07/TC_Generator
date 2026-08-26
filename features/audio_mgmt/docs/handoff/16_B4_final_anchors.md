# Audio Management — 下放包 16：B4 定案錨表（待裁 12 葉全數裁畢）

- 日期：2026-08-26
- 依據：13 包（第一路）＋ 15 包（第二路對帳）＋ 本裁定
- 池內一致之 38 葉已依 R-AM20 逕寫，本包不重複；以下為待裁 12 葉之定案
  與一處池籍分類更正。

---

## 一、池籍分類更正（先行）

15 包 §四 之池外表**誤列 264、漏列 311**：

- **264 之錨 4867598 在主池內**（匯出實有該物件），非池外；其「單源佐證」
  標記撤除，改依池內程序（第二路以匯出本文覆核後逕寫）。本裁定已代行
  覆核：匯出與全文同文（`IF $Surround$ = [1] THEN enable the HMI…`），成立。
- **311（4866914）為池外**，且 15 包 §一「A 級 30 葉亦入逕寫」將其掃入
  自動通道——**此違 R-AM20 除外條款**（池外葉不入免審範圍）。實質無害
  （本裁定即刻定案，見 §三），但池外錨登記表必須以正確集合記載：
  **B4 池外 = 311、266、306、307、308**，非 264。
- 程序註記：逕寫段之葉集今後須先過池籍過濾再併入，A 級標記不豁免
  池外檢查。此為綠色通道首批之校準，不立新條，記於本包即可。

## 二、池內待裁六葉之定案

| 葉 | 定案錨 | 裁定 |
|---|---|---|
| SWE1_AMM_002 | **CFTS019-4865913** | 改錨准。4867570 之「left or right drive」為左右駕車型（4867569 之 `$DriverSide$` 上下文可證），非左右聲道；4865913「assign Entertainment sources to the Entertainment Left and Right audio paths」與葉逐字對應。第二路之錯配診斷（詞面同、語意異）成立 |
| SWE1_AMM_122 | **CFTS019-4866444**，部分覆蓋 | 改錨准。4865895 為表名非條文；4866444 為外部參照句（Routing Table 在 {Component Technical Specification - VP1 and VP2 System}），與 076b／087 同型：TC 僅驗仲裁依表執行之可觀察面，Routing Table 具體對應併入 DR-AM1 |
| SWE1_AMM_145 | **CFTS019-4866497**，升 A | 准。「Applied Channels」面向獨立物件，與 144（4866494 一般去活化斜坡）不同物件，共錨警示解除，無需 R-AM16 論證 |
| SWE1_AMM_155 | **CFTS019-4866513**，升 A | 准。通道面向獨立物件，與 154（4866512 音量位準面向）分立。附帶：4866513 含 `<Tinfo Ramp Up>`，該參數有定義，實值入 TC |
| SWE1_AMM_204 | 維持 4866845 | `<Temp Ramp Down>` 依 DR-AM5 掛 `PENDING: DR-AM5`，無異議准 |
| SWE1_AMM_207 | 維持 4866854 | 同上 |

## 三、C 級三葉——**全數解決，零 PENDING**（分析層補查）

15 包建議三葉維持 PENDING；分析層依其線索換詞補查，三葉皆有正解：

### SWE1_AMM_020 → **CFTS019-4865981 ⏎ CFTS019-4866286**（併列雙錨，池內）
葉為雙分支：「至少前聲道」＋「全聲道區設定時routed 全聲道」。
- **4866286**：「entertainment and information alerts feature…shall be played
  on the **front speakers**」——前聲道分支。
- **4865981**：「alerts can be played on **all channels**…」——全聲道分支
  （[Market:NAFTA] 標記，本案適用）。
15 包以「all vs front 範圍不符」棄 4865981 係因只拿它單獨對整葉；
拆成兩分支後兩物件各對其一，齊備。spec_reference 升冪併列。
註：4866286 之啟用設定指向 {CFTS024}，屬設定面外部參照；
TC 驗路由不驗啟用細節，不掛 DR。

### SWE1_AMM_024 → **CFTS019-4866001**（池內）
**葉之 SWE.1 描述原文即載明 `CFTS019-4866001`**——上游自己給了錨，
此為最強追溯（上游權威明名 ObjectID）。第二路零命中之因：4866001 為
**內嵌表格物件**（WrapperResource，輸出對映表），文字層抽不出
「external amplifier」字樣——與 A-AM03 圖表型遺漏同機理，只是此物件
恰在池內。TC 內容以 SWE.1 描述＋錨表為據；reasoning 註明錨為內嵌表格。

### SWE1_AMM_146 → **CFTS019-4866498**（池內）
「Ramp Down the Entertainment audio on the **remaining audio channels**
as defined in {CIP Radio DSPPP}, using `<Tent Ramp Down>`」——與葉
「更新剩餘輸出通道」逐字對應，且與 145（4866497）**連號成序**
（Attenuate 分支：Applied Channels 先、remaining channels 後）。
15 包零命中之因：搜尋詞「remaining channel」單數，原文為
「remaining audio channels」，加上其換詞集未含此式。
註 1：`<Tent Ramp Down>` 有定義，實值入 TC（勿與 DR-AM5 之
`<Temp/Temt Ramp Down>` 混淆——204/207 掛 PENDING、146 不掛）。
註 2：{CIP Radio DSPPP} 之通道定義屬外部件，TC 不寫其具體通道集，
reasoning 註明；不併 DR-AM1（DSPPP 在 `inputs/` 但依 R-AM5 範圍外）。

## 四、池外五葉之定案（R-AM18 單源佐證，R-AM20 待裁段）

五錨原文分析層已逐條覆核：

| 葉 | 錨 | 覆核 | 定案 |
|---|---|---|---|
| SWE1_AMM_311 | CFTS019-4866914 | Phone 作用中偵得 NAV 事件 → NAV 於駕駛側啟用 | 准 |
| SWE1_AMM_266 | CFTS019-4867604 | ELSE 分支：不呈現、使用者不得啟停 surround | 准（與 264 之 IF 分支成對，§7 配對） |
| SWE1_AMM_306 | CFTS019-4866207 | 座艙音訊作用中：低於現行音量 15 dB 或 step 6 等效值取大者 | 准 |
| SWE1_AMM_307 | CFTS019-4866208 | 座艙音訊非作用（HU off）：step 6 等效值 | 准 |
| SWE1_AMM_308 | CFTS019-4866242 | SVC_Level_Setting.Req=="Off"（LTM High 為 SVS_Setup.Req=="Disable"）→ 停用 | 准 |

全數標「單源佐證」入池外錨登記表；DR-AM3 回件後回溯覆驗（R-AM18）。

**306 之撰寫裁定**：15 包附記採認——「15 dB below 或 step 6 取大者」
為兩情境各自主導之比較條款，依等價劃分拆兩條 TC（座艙音量高→15 dB
分支主導；座艙音量低→step 6 分支主導），兩值皆溯源 4866207。
**308 之附帶**：錨文之「unless some minimal settings are defined in the
vehicle EQ settings」為但書，ER 不得寫成無條件停用；但書之具體
minimal settings 無正文定義，reasoning 揭露，不造值。

## 五、B4 收斂統計

| 段 | 葉數 |
|---|---|
| 池內逕寫（R-AM20） | 38 ＋ 本包裁定升入 8（002、122、145、155、020、024、146、264 覆核） |
| 池外定案 | 5（311、266、306、307、308） |
| PENDING | 0 葉全額；204／207 僅時序值掛 DR-AM5 |
| 合計 | 50，B4 零無錨葉 |

**B4 為首個零 PENDING 葉之批次**（B1 零、B2 零、B3 有 026／076a 兩葉）。
C 級三葉全數翻案的方法學註記：三案之共通根因皆為**檢索詞形**
（left/right 詞面撞題、單複數、內嵌物件無文字層）——換詞集與內嵌物件
警覺併入第二路腳本之改善清單，執行層自酌，不立條。

## 六、開工

B4 可開工。上繳包需附：池外錨登記表（**5 筆：311、266、306、307、308**，
§一更正後之集合）、PENDING 清單（僅 DR-AM5 兩項）、未結 DR 八件、
葉集差集核對、自檢與 lint、寫回計數驗證。
306 拆兩條、266/264 成對、256/257 成對——§7 配對三組勿漏。
