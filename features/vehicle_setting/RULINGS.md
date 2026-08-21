# RULINGS — FW036 Vehicle Setting

本檔為裁決正文。條文**逐字轉錄**自下放包，不摘要、不以編號代替（canon §8.1）。

| 來源 | 條 |
|---|---|
| `docs/handoff/00_intake_and_rulings.md` §3 | R-VS1 ~ R-VS6（**仍逐字有效**） |
| `docs/handoff/00I_claude_code_prompt_v2.md` §0 | R-VS12（素材授權） |
| `docs/handoff/05_rulings.md` §1–§10 | R-VS7 / R-VS8 / R-VS9 / R-VS10 / R-VS11 / R-VS14 / R-VS15 / R-VS16 / R-VS3′ / R-VS17 |

> R-VS1 ~ R-VS6 之正文見 `docs/handoff/00_intake_and_rulings.md` §3，
> 依 canon §8.7 其下放包已落檔且入版控，本檔不重複轉錄以免二處分岔。
> **R-VS13**（Comfort HMI L&F 素材授權）之正文僅見於 `00J_consolidated.md:44` 之表格註記，
> **無條文區塊** —— 已於 01 輪回報，Pei 於 02 輪口頭確認並授權執行；記於此以留痕。

---

## 05 包裁決條文（Pei 2026-08-20 全案裁定）

抄錄核對：以程式自 `05_rulings.md` §1–§10 抽出**頂層 fenced block**，逐字寫入。

### 1. R-VS7 — Comfort 重疊之委派界線

```
R-VS7（Pei 2026-08-20）
本 feature 與 Comfort（CFTS043 / Comfort HMI Logic and Flow）之界線採
**分層委派**：

  Comfort 擁有：座椅加熱／通風／方向盤加熱之**畫面行為**
                （按鍵循環、LED 與箭頭數、highlight、seat zone 彈窗、
                  Front Comfort 與 Status Bar 之控制列）
  Vehicle Setting 擁有：同一批實體功能之**訊號與配置層**
                （CAN 狀態值、失效狀態、按鍵請求訊號、
                  PROXI／車型配置分支）

推論（binding）：
(a) 本 feature 之 TC 不重複驗證 Comfort 已擁有之畫面行為。
    需要提及畫面時，以 §8.2.1 之委派句於 reasoning 指名 Comfort 之
    對應 leaf id，不寫入 procedure／expected_result 之斷言。
(b) 例外：CFTS044 條文自身以 `Refer to TLM HMI Document` 指出畫面
    行為者（16 leaf），其畫面層斷言仍屬本 feature，惟在 DR-5-B
    到位前標 BLOCKED（見 R-VS17）。
(c) 佐證：CFTS044 內文以 `{CFTS043}` 顯式引用 Comfort 規格 3 處。

**W-9 之角色改變**：其產出由「裁定素材」變為「委派句之來源對照表」。
故 **W-9 之「做完必停」解除**，改為做完併入該輪上繳，不中斷批次。
```

### 2. R-VS8 — 追認

```
R-VS8（Pei 追認 2026-08-20）
本 feature 之 CAN 基線為兩份並用，非二擇一：

  PDT27_E2A_R4_BHCAN.dbc   BH-CAN／CAN-B 網段。STATUS_CSWM、
      STATUS_CLIMATE8、TELEMATIC_DISPLAY2、TELEMATIC_VEHICLE_SETUP3、
      STATUS_BH_BCM2 全部在此。**主要來源。**
  PDT27_E2A_R5_FDCAN8.dbc  CAN-FD 網段（BA_ "BusType" = "CAN FD"）。
      TELEMATIC_FD_4、BCM_FD_10 等 FD 對應。**指明 FD 網段時引用。**

兩檔 VersionYear = 25、VersionWeek = 50，完全相同；R4／R5 在本組檔名
中指網段，不指 release，不存在選錯版本之風險。

配套判準（適用於日後任何 DBC 之入庫）：
DBC 之身分由檔內 BA_ "VersionYear" / "VersionWeek" / "BusType" 三項
屬性判定，不由檔名之 R 碼判定。入庫時記錄該三項屬性與 SHA256。
```

### 3. R-VS9 — CAN 訊號書寫形式（v2 定案）

> **註記（14 包 §3）**：「(1) 之權威分工經 R-VS9(1)′ 更正，以 R-VS9(1)′ 為準」。

```
R-VS9（Pei 2026-08-20，取代一切先前草案）
TC 中書寫 CAN 訊號時：

(1) 訊號逐字名與所屬 message 以 Logical Identifiers and CAN Mapping
    之對應欄組為第一權威：
      - `CAN Mapping` 分頁 → `Atlantis High` 欄組
      - `Proxi & Configuration` 分頁 → `Atlantis & Atlantis High` 欄組
        （該欄組同時涵蓋兩種架構，見 R-VS11）
(2) 值域以同表 Format 欄為準，並與對應 DBC 之 VAL_ 表交叉核對；
    兩者不一致時停下回報，不自行調和。
(3) **訊號斷言須同時指明 message 與網段**，三者成組出現，缺一不可：
        <signal 名> in <message 名> on <網段>
    例：STATUS_CSWM.HSW_StatFailSts in STATUS_CSWM on CAN-B
    理由：兩份 DBC 之 141 個共有 signal 中 128 個起始位元不同（91%），
    只寫 signal 名不足以定位量測點。
(4) 網段對應：CAN-B／BH-CAN → PDT27_E2A_R4_BHCAN.dbc；
    CAN-FD → PDT27_E2A_R5_FDCAN8.dbc。
(5) `$var$` 形態僅出現於 test_item 上半段之來源逐字內，不出現於
    procedure／expected_result 之作者自撰文字。
    理由：`$PowerMode$` 之匯流排名為 `CmdIgnSts`，DBC 內另有一支
    `PowerModeSts`；以 `$var$` 檢索會抓到錯的訊號。

lint 判準（L-VS1）：procedure／expected_result 內出現 DBC signal 名而
同句無 message 名者 FAIL。
**該規則須附範圍向（R-G9）**：對 test_item 上半段之來源逐字不得轉紅，
且須以實測證明其對該類輸入不轉紅。
```

### 4. R-VS10 — Pop Up List 基線

```
R-VS10（Pei 2026-08-20）
本 feature 不採用任何版本之 Pop Up List：CFTS044 全文對 `Pop Up`
與 `Settings List` 之命中皆為 0，本 feature 條文不引用該文件。

`features/comfort/inputs/` 之 SR24 Post 2A (Dec 15, 2023) 版與
`26PI2.5/HMI/` 之 26PI 版之差異（A-VS09），**不在本 feature 之範圍內**，
不因本 feature 而處置。

若 DR-5-B（失效彈窗）之上游答覆指向 Pop Up List，本條重議。
`DATA_REQUESTS.md` 須留「已查而不取用」之痕（G-D）。
```

### 5. R-VS11 — 撤回之追認

```
R-VS11（Pei 追認 2026-08-20：撤回）
「LID 表之 Atlantis 欄能否代 Atlantis High」不是待裁事項。
`Proxi & Configuration` 分頁列 2 之欄組標題逐字為
`Atlantis & Atlantis High`，即該欄組同時涵蓋兩種架構；
`CAN Mapping` 分頁則二者分列。

故該 10 個 PROXI 類參數之 Atlantis 欄值，對 Atlantis High 直接適用，
不需假設、不需 RD-1、不需於 profile 標註為假設。

本條以撤回形式記載，不以「已裁定」記載 —— 它從來不是判斷問題，
是一次讀漏。
```

### 6. R-VS14 / DR-10 — 追認

```
R-VS14（Pei 追認 2026-08-20）
specification_reference 為字串清單，非單值（§10.7 明文：String list、
Multiple specs allowed）。leaf 對映到多個 CFTS044 章節者，逐一列出
全部章節，依 §10.7 由最具體排至一般。

實測之 5 個多章節 leaf：
  SWE1-VC-LeftFrontHeatedSeat-004      1.3.2.1.3.1 ~ .4
  SWE1-VC-LeftFrontHeatedSeat-011      同上
  SWE1-VC-HeatedSteeringWheelManagement-025 / -026 / -027
                                       1.3.2.1.3；1.3.3.3.6.1

**DR-10 撤銷** —— 單值形式從來不是政策，是分析層敘述時之簡化。
```

### 7. R-VS15 — 追認

```
R-VS15（Pei 追認 2026-08-20）
本 feature 之 TC 母體為 037 四份中 `Categorization` 開頭為 `Functional`
（不分大小寫）之列，共 237 個 leaf：

  Common Features 46／Heated Seat 88／Vented Seat 72／Heated Steering Wheel 31

其餘 34 列（Heading 25／Information 9）為文件結構與說明，非可測需求，
不產 TC、不佔 036 之列、不計入覆蓋稽核之分母。

`Categorization` 之值域全集（271 列逐列取值）：
  Functional Requirement 237／Heading 25／Information 8／information 1
  —— 四值合計 271，無其他值、無空值。

推論：
(a) 「34 個未覆蓋 leaf」之表述作廢。**本 feature 沒有覆蓋缺口。**
(b) 覆蓋稽核判準：TC 數 >= 237，且每個 Functional leaf 至少一列
    （§8.2.2：一 leaf 得對多 TC，反向不可）。
(c) 271 僅用於描述 037 之列數，不得作為任何比率之分母。
(d) N 欄：可測 leaf 237 中已定 236、未定 1（DR-11）。
```

### 8. R-VS16 — `.gitignore` 例外

```
R-VS16（Pei 2026-08-20）
features/vehicle_setting/.gitignore 於 `inputs/` 之後增列：

    !inputs/INPUTS.sha256

理由：canon G-9 明文要求雜湊檔入版控；現行 .gitignore 註解之意旨為
「不提交客戶素材」，雜湊檔非素材。無此例外則素材落地之證據鏈在
版控中是斷的。

範圍：僅及於 INPUTS.sha256 一檔，不及於 inputs/ 內任何其他檔案。
其餘 feature 之同一缺陷不在本裁定範圍，各自於下次開輪次時自檢。

**執行由 Pei**（版控政策 + git 皆屬 Pei）。
```

### 9. R-VS3′ — 目錄名之修正

```
R-VS3′（Pei 2026-08-20，修正 R-VS3 之內部不一致）
Test Group（036 G 欄）= `Vehicle Setting`（單數，逐字）—— 不變。
feature 目錄 = `features/vehicle_setting` —— 不變。
scaffold 指令參數改為 `vehicle_setting`（原記之 "Vehicle Setting" 會
產生含空白之目錄，見 A-VS19）。

`features/vehicle setting/`（含空白之誤建目錄）由 Pei 刪除。
`new_feature.py` 之名稱正規化缺陷（`scripts/new_feature.py:144` 僅
`feature.lower()`，不轉空白）維持登記為工具缺陷，不在本 feature 修。
```

### 10. R-VS17 — BLOCKED 之適用範圍

```
R-VS17（Pei 2026-08-20，配合 R-VS7(b)）
DR-5-B（失效彈窗內容、加熱方向盤圖示之左右駕鏡像）未到位期間：

  受影響之 17 leaf（16 引 TLM HMI Document ＋ 1 引 PDO graphics）
  仍產出 TC，其 ER 寫至**訊號層**為止
  （例：STATUS_CSWM.FL_HS_STATFailSts in STATUS_CSWM on CAN-B
        之值為 Fail_Present），
  **畫面層之斷言以 Remarks 標 BLOCKED 並註明其待補來源**，
  不寫入 expected_result。

不得以「畫面文字未知」為由不產 TC —— 訊號層可測且來源明確
（canon：「不知道適用於誰」≠「不知道存在什麼」）。
```

---

## 14／15 包裁決條文（Pei 2026-08-20，第二批）

抄錄核對：以程式自 `14_review_round04.md` §3／§4 與 `15_rulings2_round05.md` §1.1–§1.6
抽出**頂層 fenced block**，逐字寫入。

### R-VS9(1)′ — signal 拼寫以 DBC 為權威、對映以 LID 為權威；L-VS2

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

### R-VS25 — 單輪作業上限三項

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

### R-VS18 — 上繳包為每輪第一項

```
R-VS18（Pei 2026-08-20）
上繳包不是最後一項，是**第一項**。

每輪開工之第一個動作為：建立 `docs/upstream/NN_<slug>.md`，
寫入標題、本輪作業清單、與 canon §8.2 之六個空節
（預期 vs 實測／不符項目／三分法／掃描條件／新開 anomaly 與 DR／
獨立判斷），各節先留空白。

其後每完成一項作業，**當下就把該項之結果填入對應節**，
`reports/` 之細節報告為其附件而非替代。

理由：`reports/` 逐項落檔會產生「已交付」之錯覺，而上繳包所要求之
六項（尤其「預期 vs 實測逐項對照」與「本包是否仍有該驗而未驗者」）
是**跨項的**，逐項報告不會自然產生它們。
```

### R-VS19 — 值域須連同 [EE Architecture] 取用

```
R-VS19（Pei 2026-08-20）
CFTS044 之值域列舉須連同其條文之 [EE Architecture] 標籤一併取用。
本 feature 僅採 `Atlantis High`（含 `All`）之條文；標記為
`CUSW`／`PowerNet`／`Atlantis Mid` 而未含 Atlantis High 者，
其值域不適用於本 feature，亦不得作為「CFTS044 與 DBC 不一致」之證據。

實例：`$HeatedSeatFL$` 於 CUSW 條文（4857940）列 0h/1h/3h 三階，
於 Atlantis High 之具名式與 LID 表皆為四階（含 MED / 2）。
本 feature 取四階。

推論：值域比對之輸出須加一欄 `arch_scope`，記錄該值域出自哪些
架構標籤之條文；跨架構之差異不列為不一致。
```

### R-VS20 — 值域來源之三階梯

```
R-VS20（Pei 2026-08-20）
token 之值域依下列次序取用，前者有值即止：

  第一階  CFTS044 之 in-scope 條文（[EE Architecture] 含 Atlantis High
          或 All）之值域
  第二階  LID 表之對應欄組（CAN Mapping → Atlantis High；
          Proxi & Configuration → Atlantis & Atlantis High）
          ＋ 對應 DBC 之 VAL_ 值表
  第三階  停下回報，登記待判

**他架構條文（CUSW／PowerNet／Atlantis Mid）之值域一律不取用**，
僅得作為旁證記於 reasoning，不得寫入 TC 欄位。

理由：LID 表與 DBC 之值域**無架構條件**（其架構條件在欄組層，已由
R-VS9(1)′ 指定），故第二階不引入架構風險；而他架構條文之值域帶有
該架構之假設，取用等同以 CUSW 之行為描述 Atlantis High。

實例：$HSW_StatFailSts$ 於 CFTS044 之 in-scope 無值域（其值僅見於
Atlantis Mid 條文），依本條走第二階 —— 取 LID 表與 DBC 之
`Fail_Not_Present` / `Fail_Present`（二來源一致）。
該 token 之值域**不因 Atlantis Mid 條文而成立，亦不因之而受質疑**。
```

### R-VS21 — 積壓項排入頭部

```
R-VS21（Pei 2026-08-20）
一項作業連續兩輪未執行者，下輪**排入頭部**，且該輪不得於其前方
加入新作業。新發現之事項一律登記為 anomaly／DR 並排入其後輪次。

例外：新事項為**阻塞既有作業之前置**時得插隊，惟須於下放包具名
說明其為何是前置。

本條與 R-VS25（單輪上限三項）併用：頭部由本條決定，長度由 R-VS25 決定。
```

### R-VS23 — 入庫阻斷判準在暫存區

```
R-VS23（Pei 2026-08-20）
入庫作業之阻斷判準為「**暫存區**內出現 pathspec 以外之路徑」，
非「工作區存在 pathspec 以外之變更」。

步驟中之 `git status` 掃描其用途為揭露與留痕，其有輸出時應
**列出並續行**；真正的閘門在暫存區之逐檔核對。

理由：多 feature 並行時工作區幾乎永遠有他 feature 之在途變更，
以「存在」為阻斷判準會使每次入庫都停。
```

### R-VS24 — 窄口授權一次性（追認）

```
R-VS24（Pei 追認 2026-08-20）
附錄 A 入庫之窄口授權，內容如 12 包 §4；該授權已於執行時用畢並失效。
追認其行使正當。

一併確立通則：窄口授權**一次性、用畢即失效**，不因同一指令被再次
貼上而復活。執行層拒絕重跑為正確行為。
```

### R-VS26 — 衍生檔紀律（不得壓平語義分隔；比對自來源重建；有損者標記）

```
R-VS26（Pei 2026-08-20）
(1) 衍生檔（`data/*.tsv` 等）之寫出，**不得改變來源之語義分隔符**。
    來源以換行區分多個條目者，衍生檔須保留該區分
    （逐條目一列，或以不出現於資料中之逸出序列表示），
    不得以 `" ".join(cell.split())` 之類壓平。

(2) **凡需要語義結構之比對，一律自來源重建，不以衍生檔為輸入。**
    衍生檔之定位為「供人讀之快照」與「跨輪次之對照基準」，
    不是比對之輸入。

(3) 一份衍生檔若經證實有損，須於檔頭首行加註
        # SUPERSEDED — lossy, do not use as input; rebuilt by <script>
    並於同輪次之上繳包具名列出其下游使用者。
    **實際刪除屬 Pei**（版控範圍），分析層與執行層皆只標記。

理由：C3 之四次現身中，第 1–3 次修的是讀取，第 4 次證明
**寫出端與讀取端是同一條鏈**；只修一端，缺陷會在另一端重現。
```

### R-VS27 — C4 須加窮舉宣告之必要條件

```
R-VS27（Pei 2026-08-20）
歸因類別 C4（規格引用子集）不得單以「CFTS 側為他來源之真子集」成立。
須加一項必要條件：

  C4 成立 ⟺ 單向子集 **且** 該值域所在之 CFTS044 條文
            **不含窮舉宣告**

窮舉宣告之判準（字面，區分大小寫）：條文內含
    `Valid values for the`
  或 `All other states shall be considered invalid`

若條文**含**窮舉宣告而其值集合仍為他來源之真子集 →
**不歸 C4，一律進待判**，並登記為疑似真漏列。

理由：窮舉宣告是規格作者對「這就是全部」之明示；
在其之下的子集不是引用，是矛盾。

配套：C4 之輸出須附 `exhaustive_marker` 欄（true／false／not_found），
`not_found` 者（無法定位其來源條文）**亦進待判**，不得預設為 false。

實測基數：CFTS044 全文 `Valid values for the` 49 處、
`All other states shall be considered invalid` 48 處，
其中 in-scope（含 Atlantis High）者 15 條。
```


### R-VS28 — 連續四輪未執行者成為該輪唯一作業

```
R-VS28（Pei 2026-08-20）
一項作業連續**四輪**未執行者，下輪成為**該輪唯一作業**，
不得與任何其他作業同輪，亦不得有前置插隊。
若其確有未完成之前置，則該前置本身成為該輪唯一作業，
且下放包須具名說明其為前置之依據。

理由：R-VS21 保證排序、R-VS25 保證長度，二者併用仍不能保證出清 ——
一項只要每輪都有前置，就能無限期延後。本 feature 已出現兩次
（W-27 兩度成為頭部並各自用掉整輪，W-9 因而延至第五輪）。
```

### R-VS29 — 更嚴格判準使命中下降者，須逐筆判定差集

```
R-VS29（更嚴格判準之驗收，待 Pei 裁）
以更嚴格之判準（加詞界、加大小寫、加必要條件）重測而**命中數下降**者，
不得逕行接受該下降。須：

(1) 逐筆列出「舊判準命中而新判準未命中」之差集
(2) 逐筆判定其為**真偽陽性**（舊判準過寬）或**假陰性**（新判準過窄）
(3) 差集非空而未逐筆判定者，該次重測**不得作為更正之依據**

理由：更嚴格之判準使數字下降時，其方向與「修正高估」一致，
因而不易被質疑；但同一個下降也可能來自新判準本身之缺陷。
**兩者在計數上不可分辨，只能逐筆分辨。**

實例：`\bseat\b` 於 `seats` 不匹配，使 43 降為 30；
13 筆差集全為複數形，屬假陰性，非偽陽性。
```
