# 上繳包 28 —— T43 執行結果（下放包 30）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`docs/handoff/30_batch1_v3.md`
- **下放包 30 之落檔驗證：§四／§五之事實主張全數覆核相符**（見 §0）
- **`I-cross` v2 二錨點皆符**（見 §3）

---

## 0. 落檔驗證 —— 本包無不符

下放包 30 之事實主張逐項實測：

| 主張 | 實測 | |
|---|---|:--:|
| §四 五碼之碼值與 Description | `327680`／`393216`／`393217`／`393219`／`2147483330` **逐字相符** | ✅ |
| §四 `-2147483330` 與 `2147483330` 符號相反數值相同 | 二碼並存，分屬 `Install ( M-CPU: Redbend )` 與 `RedBend update engine` | ✅ |
| §五 `Model Code` 44 列 | 非空 **44** 列（`Model Code`／`Model Name` 二欄） | ✅ |
| §五 `Issue Mapping Version` 為 SharePoint 連結 | 標頭即 `https://shiftup.sharepoint.com/sites/R1LProject/…` | ✅ |
| §五 `Flash Status` 之 `Error Code` 欄實填 | **`262147`／`336643`／`393219`** —— 三值皆為在案碼 | ✅ |
| §1.1 TC-1 之引文不存在 | 實測 `…continuously until the update finishes`，**無起點** | ✅ |

**§1.2／§1.3 之追認收到**，補抄與拒填之處置皆已記入台帳。

---

## 1. T43e —— 抄錄與索引

### 1.1 逐字核對（機器比對）

| 條文 | 逐字相符 |
|---|:--:|
| `R-SU33 v2（全稱否定式之觀測窗法 —— (c) 之限定）` | **True** |
| `R-SU34 v2（跨 req_id 之偽通過 —— 指標更換）` | **True** |
| `R-SU36（否定式觀測之時間解析度）` | **True** |

**R-SU35(a) 之補**依明令作**條文修訂加註**（非新版）——
於原條文之對照表後加「**補（下放包 30 §四）**」段，
逐碼載其內容依據，並記 `±2147483330` 之符號拘束。**原文一字未改。**

### 1.2 索引表（以現場為準）

| 項 | 抄錄前 | **抄錄後** |
|---|---:|---:|
| 現行 | 35 | **36**（+R-SU36） |
| 留存 | 19 | **21**（+`R-SU33`(v1)、+`R-SU34`(v1)） |

`R-SU1` – `R-SU36` **無缺號、無重複**。R-SU33／R-SU34 改標 v2（版本升級不佔新列）。

### 1.3 PLAYBOOK

**(32)** 以引文支撐一個判斷前，回原文核對該引文存在 —— 引錯的引文會讓錯的結論看起來有依據。

其判準寫成可操作式：**「這句話我是從原文複製的，還是從別人的複述複製的？」**
另記二事：**引文之危險性高於論斷**（論斷會被檢驗，引文會被信任）；
**誤引會沿用**，因後續各包引的是前一包而非原文 —— 本案即二度出現。

---

## 2. T43a／T43b —— 改寫明細

### 2.1 TC-8 改判（T43a）

`newR1L-SU-008` 三欄改寫，其餘逐字不動；**掛三個 `PENDING`**，
成因記為**不可區辨**（R-SU32(iii)），DR-SU2 第三型段增為 3 列。

### 2.2 R-SU36 之時間解析度（T43b）

**pilot 升為 `pilot04`**（`pilot01`–`03` 不覆寫，沿其慣例）。逐列改動：

| TC | 欄 | 前 | **後** |
|---|---|---|---|
| `001` | proc 3 | `Record … continuously until the update finishes` | `Record … **as continuous video capture** until the update finishes` |
| `001` | er 3 | `… is recorded` | `… is recorded **as continuous video capture**` |
| `002` | proc 3 | `Record … continuously until the software version changes` | `Record … **as continuous video capture** until …` |
| `002` | er 3 | `… is recorded` | `… is recorded **as continuous video capture**` |
| **`004`** | **proc 2** | **`Record every SW Update screen shown on the head unit until the update finishes`** | **`Record the head unit screen content as continuous video capture until the update finishes`** |
| **`004`** | **er 2** | **`Every SW Update screen shown until the update finishes is recorded`** | **`The head unit screen content until the update finishes is recorded as continuous video capture`** |
| `004` | proc 3／er 3 | `none of the recorded **screens** offers …` | `no opt-out control and no defer control appear in the recorded **screen content**` |
| `006`／`007` | proc 3 | `Record the head unit screen content from …` | `Record … **as continuous video capture** from …` |
| `006`／`007` | er 3 | `… is recorded` | `… is recorded **as continuous video capture**` |
| `010` | proc 3／er 3 | `Record the head unit screen content and any user input from …` | `Record the head unit screen content **as continuous video capture**, and any user input, from …` |

`004` 之 proc 3／er 3 為**連帶改動**：其原文說「所錄下的**各個畫面**」，
而步驟 2 已不再產生「一組畫面」而是一段錄影，不改則二步互相矛盾。
**驗證單元不變**（無 opt-out／defer 控制項），僅觀測手段具體化。

### 2.3 未納入 T43b 清單者 —— `003`，**經核為正確之排除**

`newR1L-SU-003` 步驟 2 亦為錄影步驟（`… continuously from the start of the session`），
**不在下放包 30 之改寫清單內**。執行層覆核其 ER：四行**全為肯定式**
（`The safety-related notification **is displayed** …`），
**R-SU36(a) 之射程為否定式**，故不適用。**排除正確，未擅改。**

> ⚠ **惟其殘留二項**，記錄不裁：
> (i) 其 `continuously` 仍未定義是否排除定時截圖（R-SU36(b) 所指之含混）；
> (ii) 其窗之起點 `the start of the session` —— **session 開始是否可觀測未經裁定**，
> 此為 **R-SU33 v2(c)** 之同型問題（起訖點須為可觀測之事件）。
> 該 TC 本已因 DR-SU1 掛三個 `PENDING`，故不阻斷。

### 2.4 lint 全輸出（逐字，二簿）

```
python3 scripts/lint036.py <pilot04 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=3  V=0        exit 0

python3 scripts/lint036.py <batch01 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=8  V=0        exit 0
```

| 項 | 預期 | 實測 | |
|---|---:|---:|:--:|
| batch01 之 U | **8**（`184` 3 + `179` 3 + `181` 2） | **8** | ✅ |
| pilot04 之 U | 3（DR-SU1，不變） | **3** | ✅ |
| 二簿其餘 20 項 | 0 | **全 0** | ✅ |

> **`I-sibling=0` 之限定（R-SU34 v2(a)，逐包揭露）**：其語意為
> 「同一需求列底下無重複之括號行」。跨 req_id 之覆蓋由 `I-cross` v2 承擔，
> **而 `I-cross` 尚未併入 `lint036.py`**，現為獨立腳本 ——
> **缺口未完全補上，逐包揭露**（R-SU34 v1(d)）。

---

## 3. T43c —— `I-cross` v2 回測（R-SU34 v2(b)）

**指標為布林條件，無門檻**：窗之起訖相同 **且** 違例類有交集 → 待人裁。

### 各 TC 之抽取結果

| TC | 037 列 | 窗（起 → 訖） | 否定式違例類（最細） |
|---|---|---|---|
| TC-1 | `175` | `availability-check` → `version-change` | `progress-notification`／`prompt` |
| TC-2 | `176` | `availability-check` → `version-change` | `progress-notification` |
| TC-3 | `176` | `session-start` → `availability-check` | —（無否定式 ER） |
| TC-4 | `177` | `availability-check` → `version-change` | `defer`／`opt-out` |
| TC-5 | `183` | `availability-check` → `availability-check` | —（無否定式 ER） |
| TC-6 | `180` | `availability-check` → `version-change` | `confirmation-screen/download` |
| TC-7 | `182` | `availability-check` → `version-change` | `confirmation-screen/deployment` |
| TC-8 | `184` | `availability-check` → `version-change` | `confirmation-screen`／`progress-notification`／`prompt` |
| TC-9 | `179` | `availability-check` → `availability-check` | —（無否定式 ER） |
| TC-10 | `181` | `availability-check` → `version-change` | —（無否定式 ER） |

### `I-cross` 命中（5 組 / 45）

| 配對 | 037 列 | 共同窗 | **違例類交集（上下位判定）** |
|---|---|---|---|
| TC-1 vs TC-2 | `175`／`176` | `availability-check` → `version-change` | `progress-notification` |
| TC-1 vs TC-8 | `175`／`184` | `availability-check` → `version-change` | `progress-notification`／`prompt` |
| TC-2 vs TC-8 | `176`／`184` | `availability-check` → `version-change` | `progress-notification` |
| TC-6 vs TC-8 | `180`／`184` | `availability-check` → `version-change` | `confirmation-screen` |
| TC-7 vs TC-8 | `182`／`184` | `availability-check` → `version-change` | `confirmation-screen` |

### 二錨點（下放包 30 T43c 之驗收條件）

| 錨點 | **應** | 實測 | |
|---|---|---|:--:|
| TC-8 vs TC-1（窗經 §2.1 判為同） | 命中 | **命中** | ✅ |
| TC-6 vs TC-7（違例類不同） | **不**命中 | **未命中** | ✅ |

**驗收：✅ 二錨點皆符**

### 3.1 驗收與一處實作上的關鍵

**二錨點皆符。** 但首版**錨點 2 不符**（TC-6 vs TC-7 誤報），成因值得記：

**粒度即指標本身。**

- **類太粗**（download／deployment confirmation 併為 `confirmation-screen`）
  → TC-6 與 TC-7 落入同類而**誤報**；
- **類太細**（二者各自獨立，且 TC-8 之概括式 `no confirmation screen` 自成一類）
  → TC-8 與二者皆不相交而**漏報**，**而 TC-8 正是本檢查要抓的那一個**。

**兩端都失敗，故問題不在選哪個粒度，而在「交集」之定義。**
解法為取**最細之類**並以**上下位關係**判交集：
`confirmation-screen` ⊃ {`…/download`, `…/deployment`}；
概括式與任一子類相交，二子類彼此不相交。二錨點遂同時成立。

> **此事對條文之意涵**：R-SU34 v2(b) 只寫「違例類別有交集」，
> **未定義類之粒度與交集之語意**。上述二者是實作時被迫做出的決定，
> **不同的決定會給出不同的檢查結果** —— 建議條文補明。

### 3.2 命中之解讀

TC-8 被四個配對指到（vs TC-1／TC-2／TC-6／TC-7）——
**與下放包 30 §2.1 之判定一致**：其違例類為其餘三者之聯集，窗相同。
**該指標指對了人。**

**另有一組本包未預期之命中**：**TC-1 vs TC-2**（`175`／`176` facet A）——
窗相同（`availability-check` → `version-change`），
違例類交集 `progress-notification`。二者之區別在
`175` 驗「背景執行且無互動」、`176` facet A 驗「無進度通知」，
而**後者之違例類為前者之真子集**。**警示器所為即此** —— 待人裁，執行層不動。

### 3.3 一項須明記之事：本檢查有一處判斷不是從文字讀出來的

`NORMALISE` 表把「未指定之起點」正規化為**可用性查詢**、
把 `until the update finishes` 正規化為**版本號改變**。

**其依據為下放包 30 §2.1 之裁定，不是 TC 之文字。**
若無該正規化，TC-1 之窗為 `(None → update-finish)`、TC-8 為
`(availability-check → version-change)`，**二者不同，錨點 1 即不成立**。

故 **TC-8 vs TC-1「窗相同」之判定，其效力來自該裁定而非該檢查**。
已於腳本檔首以警語記明：**若日後改裁，本表須同步改，
否則本檢查會沉默地沿用一個已失效之前提。**

---

## 4. T43d —— 三項台帳

### 4.1 DR-SU2 第三型段 —— **3 列**

| 型 | 列 | 成因 | 所求 |
|---|---|---|---|
| 第三型 | `179` | 下載請求與整體背景執行不可區辨 | 下載請求已發出之跡象 |
| 第三型 | `181` | 限定詞 `immediately` 不可量（**不屬 105 列**，R-SU32 v2(e)） | 下載完成時點之可觀測跡象 |
| **第三型** | **`184`** | **增額驗證點為空** —— 其三類違例已由 TC-1／TC-6／TC-7 分別覆蓋，`across the three phases` 不可觀測 | 三階段界線之外部辨識手段；若無，**併入 `175`**（須上游確認） |

**記法**：第二型 **5 / 106**；**第三型 3 列，母群未知**。
母群沿革表增一列，成因記為「下放包 28 §2.2 之否證係以不存在之引文為據，已撤銷」。

### 4.2 `ERROR_CODES.md` —— 五碼補填

五碼皆填 `Update Agent`，**逐碼抄其內容依據**（下放包 30 §四）。
腳本設**閉合檢查**：逐碼依據須套用 5/5，不符即 `sys.exit`（PLAYBOOK (31)）。
`±2147483330` 之符號拘束於**二碼各自之註欄**皆記。

**另於台帳檔首加一段粒度說明**：除該 5 碼有逐碼依據外，
其餘 75 碼仍為 **R-SU35(a) 之階段級對照**，即一個粗粒度代理；
**候選非裁定**，逐碼正解須自 Description 讀出失敗情境再對照 037 列，本輪未做。

### 4.3 `SOURCE_COLUMNS.md` —— 九分頁裁定，**未定 0**

| 素材 | 單位 | 已用 | 不用 | 未定 |
|---|---:|---:|---:|---:|
| 037／SYS1／036 | 58 欄 | 28 | 30 | **0** |
| **`Error_Code_List.xlsx`** | **9 分頁** | **1** | **8** | **0** |
| **合計** | **67** | **29** | **38** | **0** |

**九分頁於下放包 29 入案、下放包 30 裁定，未跨輪** —— R-SU26(b) 全程未觸犯。

§五之附帶事實已入檔並加拘束：`Flash Status` 之 `Error Code` 欄實填三碼
（**執行層實測 `262147`／`336643`／`393219`，三值皆為在案碼**），
證明該錯誤碼於實機作業中被觀測並記錄；**但該分頁未載「在哪裡讀到」**——
它記的是結果，不是觀測手段。**線索與答案不得混同，不解 DR-SU2 v2(a)。**

---

## 5. 未結 DR 清單（**2 筆**）

| DR | 標的 | 狀態 | 進度 |
|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | **OPEN**｜High | `176` facet B；`newR1L-SU-003` 三個 `PENDING` |
| **DR-SU2 v2** | (a) Error Code 之顯示途徑／(b) Wi-Fi session 之正向狀態觀測／(c) **第三型之區辨手段（`179`／`181`／`184`）** | **OPEN**｜High | 第二型 **5 / 106**；**第三型 3 列，母群未知** |

**`PENDING` 總計 11 行**：`newR1L-SU-003` 3（DR-SU1）＋
`008` 3、`009` 3、`010` 2（DR-SU2）。

> ⚠ **DR 文本（`docs/upstream_requests/DR-SU1_SU2_request.md`）已過時** ——
> 其 §3.4 只列 `179`／`181` 二列，**未含 `184`**。本輪未改（下放包 30 未令），
> **發送前須更新**，否則上游收到的第三型清單少一列。

---

## 6. 獨立自評 —— §七-6 所問：§2.1 之二分是否窮盡

**答：不窮盡。存在第三種起點，且它可執行 —— 但它救不了 TC-8。**

**(甲) §2.1 之二分。** 其列 TC-1 之窗起點只有二種可能：
(i) 更新開始執行 —— 不可觀測；(ii) 可用性查詢 —— 可觀測但與 TC-8 相同。

**(乙) 第三種：以「測試者主動觸發之另一動作」為起點。**
可觀測之起點不限於可用性查詢 —— R-SU33 v2(c) 自己列了三類，
其中「測試者主動觸發之動作」是一個**類**，不是一個特定動作。

具體地：**先讓更新下載完成並停在安裝前，再開始錄影**。
其起點為「下載完成」—— 而下載完成之時點正是 `181` 所求者（DR-SU2 v2(c)），
**現不可觀測**。**故此路現階段不通，但其不通之成因與 (i) 不同** ——
(i) 是**原理上**無外部表徵，本項是**現階段**無觀測手段，
**DR-SU2 v2(c) 一旦有答案，本項即可執行**。

**(丙) 更接近可行者：以「使用者操作」為起點。**
如「錄影自使用者按下 X 起」。但靜默更新之定義即**無使用者操作**，
故本 feature 內無此類事件可用。**此路對 Silent Update 這一組封閉，
對他組（如 `USB Update`）則開放。**

**(丁) 然而 —— 第三種起點救不了 TC-8，理由與窗無關。**

即使 TC-1 之窗被縮到「自下載完成起」而與 TC-8 相異，
**TC-8 之增額驗證點仍為空**：其所檢之三類違例
（prompt／progress notification／confirmation screen）
**逐類皆已有專屬之 TC**（TC-1／TC-2／TC-6／TC-7），
而其獨有之宣稱（`across the three phases`）**不可觀測** ——
**這一半與 TC-1 之窗完全無關，是 TC-8 自身之問題。**

**故 §2.1 之結論成立，但其論證路徑比所需的窄**：
它只論證了「窗分不開」，而 TC-8 之空**還有第二個獨立成因**（違例類全被覆蓋）。
**二個成因中，只有前者依賴 TC-1 之窗。** §3.2 之 `I-cross` v2 命中恰為後者之機器佐證
—— TC-8 被四個配對同時指到，其中 TC-6／TC-7 之命中**與窗之正規化無關**。

**(戊) 對條文之建議（非裁定）**：R-SU33 v2(c) 之「可觀測之起訖點」
宜再分二級 —— **原理上不可觀測**（無外部表徵，如靜默更新之執行開始）與
**現階段無手段**（有外部後果但缺觀測通道，如下載完成）。
**前者永遠不可用作起點，後者是一個 DR 標的。**
現行條文把二者併為「不可作起訖點者」，會使後者被誤判為死路。

---

## 7. 待裁事項

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **`I-cross` v2 之類粒度與交集語意** —— 條文未定義，實作被迫決定，不同決定給不同結果 | §3.1 |
| 2 | **TC-1 vs TC-2 之命中**（`175`／`176` facet A，違例類為真子集關係） | §3.2 |
| 3 | **DR 文本須更新** —— 其第三型清單少 `184` | §5 |
| 4 | `newR1L-SU-003` 之 `continuously` 與 `the start of the session` 起點 | §2.3 |
| 5 | **R-SU33 v2(c) 是否再分「原理上不可觀測」與「現階段無手段」** | §6(戊) |
| 6 | `I-cross` 是否併入 `lint036.py`（現為獨立腳本，缺口未完全補上） | §2.4 |
