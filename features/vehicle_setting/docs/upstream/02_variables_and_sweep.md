# 02 上繳 — 值域三來源比對、HMI 目錄餘數掃描、殘項收尾

執行層寫入。往返 NN = 02。
**本輪未生成任何 TC，未寫回任何工作簿，未執行任何 git 寫入性操作。**

> **本檔依 R-VS18 於開工第一個動作建立**，六節先留空，逐項完成即填。
> `docs/reports/` 之逐項報告為**附件**，非本檔之替代 —— 本檔所載之
> 跨項對照、三分法與獨立判斷，逐項報告不會自然產生。

## 本輪作業清單

| # | 作業 | 狀態 |
|---|---|---|
| — | 裁決落檔（05 §1–§10 逐字轉錄入 `RULINGS.md`；§11 套用 ANOMALIES） | ✅ 已完成（02 輪前段） |
| W-8 | 三來源 `$變數$` 對照 | ✅ 已完成（附件 `reports/w8_spec_variables.md`） |
| W-13 | 26PI2.5/HMI 全文掃描（107 檔） | ✅ 已完成（附件 `reports/w13_hmi_sweep.md`） |
| W-16′ | `Categorization` 值域全集補行 | ✅ 已完成 |
| W-19 | 值域完整性複驗（判準改為「值集合不相等即列出」＋ `arch_scope`） | ✅ |
| W-20 | CFTS044 值域抽取之第三式 | ✅ |
| W-15b′ | DBC ↔ LID 表逐屬性交叉 | ❌ **未執行** |
| W-17 | LID 列數差 6 之追因；`TRUNCATED_ENUM` 其他形態 | ❌ **未執行** |
| W-9 | Comfort 逐條對照（母體 237） | ❌ **未執行** |
| W-21 | 登記 A-VS22（另新開 A-VS23／A-VS24） | ✅ |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 裁決落檔

| 項 | 預期 | 實測 | 判定 |
|---|---|---|---|
| 05 §1–§10 頂層 fenced block | 10 | **10** | 符 |
| 逐字轉錄核對 | 10 / 10 | **10 / 10** | 符 |
| 條文 id | R-VS7/8/9/10/11/14/15/16/3′/17 | **相同** | 符 |

### 1.2 W-16′ `Categorization` 值域全集（05 §7 / 07 §4）

| 值 | 預期 | 實測 |
|---|---|---|
| `Functional Requirement` | 237 | **237** |
| `Heading` | 25 | **25** |
| `Information` | 8 | **8** |
| `information` | 1 | **1** |
| 合計／空值 | 271／0 | **271／0** |

**四值合計 271、無其他值、無空值** —— 全集宣告成立。

### 1.3 W-13（07 §4 已覆核接受，本節補跨項對照）

| 項 | 預期 | 實測 | 判定 |
|---|---|---|---|
| 目錄檔數 | 107（07 已採本層實測值） | **107**（PDF 89／XLSX 15／PPTX 3） | 符 |
| `Fail_Present`／`STATFailSts`／`Heated Steering Wheel Icon` | 0 | **0 / 0 / 0** | 符 |
| 無文字層之 PDF | 1 | **1**（`Core HMI Logic and Flow…`，21 頁、40 影像、21 字元） | 符 |
| 該檔經處理後可讀 | 旋轉 180° | **旋轉 180° 後 OCR 得 35,901 字元** | 符 |

### 1.4 W-20 第三式（07 §5 指定之錨點驗證）

| 項 | 預期 | 實測 | 判定 |
|---|---|---|---|
| `$HSW_StatFailSts$` 應含 `Fail_Present` | 是（DBC／LID 皆載） | **是** —— 式三取得 | **符，錨點滿足** |
| 第三式之形態 | 未知，須反推 | **`路徑.名稱 passes to "值"`** | 已定 |
| 三式逐式命中（全 token 合計） | — | 式一 **451**／式二 **45**／式三 **34** | — |
| 式三之獨有貢獻 | — | **6 token**：`$HSW_Stat$`／`$HSW_StatFailSts$`／`$HeatedSeatFL$`／`$HeatedSeatFR$`／`$VentedSeatFL$`／`$VentedSeatFR$` | — |

### 1.5 W-19（07 §6 指定之判準變更）

| 項 | 舊判準（W-8） | 新判準（W-19） |
|---|---|---|
| 判準 | 兩來源**無交集**才列 | 兩來源**值集合不相等**即列 |
| 命中之來源對 | **1** | **39** |
| ── 完全無交集 | 1 | **1**（`$VC_VEH_LINE$`，即 DR-8） |
| ── 部分重疊而不相等 | （舊判準看不見） | **38** |

`[EE Architecture]` 標籤之值域全集（逐條文 2030 個，多值展開）：
`Atlantis High` **825**／`PowerNet` **498**／`CUSW` **388**／`All` **354**／`Atlantis Mid` **247**；
**無標籤者 4**。本 feature 依 R-VS19 取 `Atlantis High` ＋ `All`。
30 token 中，in-scope 架構有值者 **26**。

---

## 2. 不符項目（不自行調和）

### 2.1 三項實質差異（**升級條件所指者**）

| # | token | 內容 | 處置 |
|---|---|---|---|
| 1 | **`$VC_VEH_LINE$`** | CFTS044 用字母碼 `DT`／`WS`／`HDCC`／`M240`／`JL`／`K8`；LID 表列數字車型碼並截斷於 `101 = WL (65 Hex)`。**完全無交集** | **即 DR-8**，維持開啟 |
| 2 | **`$PowerMode$`** | CFTS044 in-scope 值含 `IGN OFF`／`IGN OFF ACC`；而 `CmdIgnSts` 之值域（DBC 與 LID 一致）為 `Initialization`／`IGN_LK`／`ACC`／`RUN`／`START`／`SNA` —— **無任何 OFF** | **A-VS24 新開，登記待判**。⚠ 非拼字差異，是**狀態不存在**；不自行對映至 `IGN_LK` |
| 3 | **`$TGW_DISP_STAT$`** | DBC 作 `Display_closed`，LID 表 `Format` 欄作 **`Diplay_closed`**（缺 `s`） | **A-VS23 新開**。RD-1 FYI；⚠ 若以 LID 字串為 ER 逐字值，會寫出匯流排上不存在之狀態名 |

**其中第 2 項為升級條件「跨來源值集合不相等且非架構差異」之命中** —— 已停下回報，不自行調和。

### 2.2 其餘 36 項之歸因（**先報自己的錯**）

| 類 | 數 | 說明 |
|---|---|---|
| **我方之別名切分產物** | 多數 | CFTS044 寫 `Heated Seat High / HS_HI`，我以 ` / ` 切為兩值，於是 `hs hi` 成為「僅 CFTS 有」。**是我的正規化產生的，不是資料差異** |
| **LID 列之訊號粒度不同** | `$HeatedSeatFL/FR$`／`$VentedSeatFL/FR$`／`$HSW_Stat$` | LID 之一列同時對映**狀態訊號與失效訊號**（`FL_HS_STATSts` ＋ `FL_HS_STATFailSts`），故其值集合含 `Fail_Present`；CFTS044 之 `$HeatedSeatFL$` 僅指狀態。**粒度差異，非不一致** |
| **我方 LID `Format` 解析仍有殘缺** | `'heated seat high 1 bit signal (fl hs statfailsts)'`／`'fail present statsts'` | 該儲存格含**兩個訊號之列舉串接**，我的鍵值切分跨越了其邊界。**W-8 修過一次，此處為其殘餘** |
| **CFTS044 只引用其所需之子集** | `$RVC_SK_PRSNT$`（只引 `Present`）／`$Heated_Steering_Levels$`（未引 `2 Levels`） | 規格引用子集為常態，**不構成不一致** |
| **縮寫 vs 全名** | `$Hybrid_Type$`（`BEV` vs `battery electric vehicle`）／`$ESS_ENG_ST$`（`ENS DSBL` vs `ENS disabled`） | 命名體系差異 |

### 2.3 R-VS19 之實例確認

`$HeatedSeatFL$` 之三階列舉出自 `4857940`，其標籤為 **`[EE Architecture:CUSW]`**，
**不在本 feature 之 in-scope**；Atlantis High 側之具名式與 LID 表皆為四階（含 MED）。
→ **依 R-VS19 不列為不一致，實測確認 07 §3.1 之判斷。**

**另一項 R-VS19 之新實例**：`$HSW_StatFailSts$` 之值
（`Fail_Present`／`Fail_Not_Present`）**全部出自 `[EE Architecture:Atlantis Mid]` 條文，
CFTS044 之 Atlantis High 側對該 token 無任何值域**。
其值域因而**只能取自 DBC 與 LID 表**。此事實影響 17 個 BLOCKED leaf 之訊號層 ER 依據，
**登記待判，不自行認定 Atlantis Mid 之值可用於 Atlantis High。**

---

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `RULINGS.md` 建檔並逐字轉錄十條；`ANOMALIES.md` 套用 05 §11（A-VS01／A-VS06′／A-VS18 除役、A-VS21 新開）；W-16′ 補值域全集宣告；**W-8 之比對判準由「無交集」改為「值集合不相等」**；**CFTS044 值域抽取自兩式增為三式** |
| **核實無誤** | §1 之全部相符項；W-13 之 107 檔零相關命中（含 OCR 後之 `Core HMI Logic and Flow`）；R-VS19 之 `$HeatedSeatFL$` 實例經逐條文架構標籤確認 |
| **正確地不動** | `$PowerMode$` 之 `IGN OFF` **未自行對映**至 `IGN_LK`（A-VS24 登記待判）；`$HSW_StatFailSts$` 之 Atlantis Mid 值**未自行認定**可用於 Atlantis High；`.gitignore` 未改（R-VS16 屬 Pei）；未執行 git；未裁定任何條文 |

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| CFTS044 | 原始 docx `word/document.xml` 之 `w:body`／`w:p`／`w:t` 串接。**條文切分**：以 `\d{7}\s*:\s*\[Artifact Type` 為界，得 **2030** 個區塊 |
| 架構標籤 | 每區塊取 `\[EE Architecture:([^\]]*)\]` 之**首次命中**，以 `,` 展開為多值。⚠ **若一區塊內有二個標籤，只讀到第一個**（已知界線） |
| 值域式一 | `re.escape(token) + r"\s*(?:=\|==\|is\|shall be)?\s*\[([^\]]{1,80})\]"` |
| 值域式二 | `(?:路徑\.)?名稱 \| $var$` ＋ `==?` ＋ 引號值 |
| **值域式三（W-20 新增）** | `(?:路徑\.)?名稱 \| $var$` ＋ `\s+passes\s+to\s+` ＋ 引號值 |
| DBC | `^VAL_\s+(\d+)\s+(\w+)\s+…;` 之值表；兩份皆掃 |
| LID Format | `(-?[0-9A-Fa-f#]+)\s*[=:]\s*(.*?)(?=\s+-?[0-9A-Fa-f#]+\s*[=:]\|$)` —— **以「下一個鍵 =」為邊界**，非以逗號（該欄無逗號分隔） |
| 橋接 | token → LID 表 `Atlantis High` 之 signal 名（空則 `Atlantis`）→ DBC。**必要**：逐字比對僅 3 token 在 DBC 中存在 |
| 值正規化 | 剝 `Nh: ` 編碼前綴；` / ` 切為別名；`\s+`／`_` 併為單一空格；**轉小寫** |
| W-13 | PDF `pdftotext -q`；XLSX `openpyxl` 全分頁全格；PPTX 全 `*.xml`；`Fail_Present`／`STATFailSts` **區分大小寫**；`Heated\s+Steering\s+Wheel\s+Icon` **不分大小寫**；`Left Side`／`Right Side` **區分大小寫、首版無詞界**（詳見附件 §3） |
| W-13 之 OCR | `pdftoppm -r 200 -png` → `PIL.Image.rotate(180)` → `tesseract --psm 3 -l eng` |

---

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS22** | —（RD-1 FYI） | `$VentedSeatFL$` 之值含 `Vented Seat Off / HS_OFF`（應為 `VS_OFF`）。規格筆誤，不影響取值 |
| **A-VS23** | —（RD-1 FYI） | LID 表之 `TGW_DISP_STAT` 值域拼字錯誤 `Diplay_closed`（DBC 作 `Display_closed`） |
| **A-VS24** | **DR-12（新）** | CFTS044 以 `IGN OFF` 描述 `$PowerMode$`，而 `CmdIgnSts` 之值域無 OFF。**狀態不存在，非拼字差異** |
| **A-VS21** | — | （05 §11 指定）分析層經 MCP 讀取中文檔偶發替代字元；曾兩度誤報「檔案毀損」 |

**DR-12（新）**：`$PowerMode$ = IGN OFF` 之對應訊號值為何？
`CmdIgnSts` 無 OFF；是否對映至 `IGN_LK`，或另有他訊號承載該狀態。
**影響**：引用 `$PowerMode$` 之條文其 ER 無法以單一訊號值表達。Urgency **Medium**。

**待判（非 DR，屬條文）**：`$HSW_StatFailSts$` 之值域僅存於
`[EE Architecture:Atlantis Mid]` 條文；Atlantis Mid 之值是否可用於 Atlantis High，
R-VS19 未涵蓋此情形（其只說「不列為不一致」，未說「可取用」）。

---

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，六項**

### 6.1 本輪未執行之作業（具名，不假裝已做）

| 作業 | 狀態 |
|---|---|
| **W-15b′** DBC ↔ LID 逐屬性交叉 | **未執行**。W-8 之盲區 3（「橋接依賴 LID 表，其若錯則三來源一致地錯」）**因而仍未收** |
| **W-17** LID 列數差 6；`TRUNCATED_ENUM` 其他形態 | **未執行** |
| **W-9** Comfort 逐條對照 | **未執行**。R-VS7 之委派句來源對照表尚未備 |

### 6.2 已知而未收之界線

1. **架構標籤只讀首次命中。** 若一條文區塊內有二個 `[EE Architecture:…]`，
   本輪只讀到第一個 —— **抽取式之缺陷不會報錯**（§5a 條 12）。未驗其是否存在。
2. **「值集合不相等」之 38 項中，我方產物與資料差異尚未逐項分離為可機器判定之類別。**
   §2.2 之歸因為人讀分類，**未寫成判準**；下輪若重跑，同樣的 38 項會再次全部列出。
3. **W-20 之第三式以單一錨點（`Fail_Present`）反推。**
   其驗證了「式三能抓到該錨點」，**未驗證「三式已窮盡」** ——
   若存在第四式，本輪同樣看不見。§5a 條 12 之要求為「以已知全集驗證」，
   而本輪之已知全集只有一個 token。**這是本輪最弱的一環。**

### 6.3 一項流程觀察

本輪依 R-VS18 先開上繳包再作業，**確實改變了行為**：
§1 之跨項對照與 §6 之未執行清單在作業進行中即已成形，
而非事後回憶。**前三輪之所以漏寫，正是因為這兩節只能跨項產生。**

---

## 7. 給 Pei 之 git 指令草稿（未執行，帶 pathspec）

```bash
# P1 刪除誤建之空白目錄（R-VS3′）—— 先確認其內僅 scaffold 模板
ls -la "features/vehicle setting" && rm -rf "features/vehicle setting"

# P10 .gitignore 例外（R-VS16）—— 於 inputs/ 次行加入：
#     !inputs/INPUTS.sha256

# P2 入庫（00–02 三輪產物 ＋ 裁決）
git add features/vehicle_setting/RULINGS.md \
        features/vehicle_setting/ANOMALIES.md \
        features/vehicle_setting/DATA_REQUESTS.md \
        features/vehicle_setting/docs/ \
        features/vehicle_setting/data/ \
        features/vehicle_setting/feature.yaml
git commit -m "feat(vehicle_setting): rounds 00-02 — intake, recon, rulings R-VS1..R-VS19, variable domains"
```

> **git 唯讀與改狀態分列**（R-G6）：本輪執行之 git 指令僅 `git status --porcelain`。
> **未執行任何 add／commit／checkout／restore／stash／clean／tag。**
