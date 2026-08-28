# COVERAGE_GAPS — driver_distraction (FW036)

已知之覆蓋缺口。**登記於此者為「應驗而本輪未驗」**，非「不必驗」。
每項須載：缺口之內容、**其行為由誰所有**（IN §8.2.1／§8.4.2）、
未涵蓋之**成因**（是規格未載，或是可測性不足）、以及解除之條件。

登記為 Tier 1（record + propose）；處置為 Tier 2。

---

## [CG-DD1] Lockout Table 之負向面 —— 「不在表內之 feature 仍可存取」未驗

- 登記：2026-08-28（T20c，下放包 14 §3.2）
- 影響 leaf：`-013`／`-015`（`newR1L-DD-B007`／`newR1L-DD-B009`）
- 狀態：**OPEN**

### 缺口

`-013`／`-015` 各取一個標 `L/O` 之樣本，斷言其被鎖。
**如此無法區辨「表被正確套用」與「全部都鎖」** ——
Lockout Table 之要義為**選擇性**（L/O 與非 L/O 之別）。

IN §7 逐字：`Enumerated supported items → ALWAYS pair with at least one
unsupported negative TC`。

### 該負向面由誰所有 —— **上游所有，非本層所造**（T20c 實測）

| 母體 | 結果 |
|---|---|
| 037 `Analysis Report` `-013`~`-016`，全 20 欄 | **未載**（4 處命中皆為 AC2 之 `unavailable`／`Exception`，與負向面無關）|
| **CFTS022 `Basic Report` `-120`／`-121`，全欄** | **載** |

**CFTS022 `-120` c38（SYS2 驗證標準）逐字**：

```
Features not listed in the table remain accessible and unaffected.
```

**CFTS022 `-121` c38 逐字**：

```
Features not included in the table remain accessible and function normally.
```

**二者之 c39（SYS2 驗證方法）逐字**：

```
4. Verify allowed features
   Access features not in the table
   Verify normal operation
```

> ⚠ **位階之精確陳述**：上述文字位於**驗證標準／驗證方法欄**，
> **非規範欄（c3 `Description`）**。c3 之規範句為
> `The HU shall apply lockout to the features in the The Driver Distraction Lockout Table.`
> 其 Note 云該表 `indicates the features which are locked-out` ——
> **選擇性由「in the table」之限縮與該 Note 隱含支持，但 c3 未明文書出負向面。**
>
> 即：**負向面明載於來源需求自身之驗證欄，隱含於其規範欄。**
> 二者皆非本層所造，故驗之不違 IN §8.4.2。

### 為何本輪仍未補 —— **樣本不可自綁定來源決定**

補負向斷言須具名一個**不在表內**之 feature（profile §2.1 禁泛稱）。
**該樣本取不到**，二個獨立成因：

1. **HMI spec p7 只列 L/O 側。** 本輪逐列傾印 p7 之
   `Driver Lockout Tables`：**16 個 feature 列全部標 `L/O`**
   （末列 `SXM 360L` 全欄為 `Inv.`）。**表內無「非 L/O」之列** ——
   故樣本必須來自**表外**，而 p7 不列表外之物。
2. **CFTS022 之表本體不可機讀。** c3 以
   `(image: 1-_3bc8e108-12c5-4694-a9e9-80b1f915b9af.rtf)` 參照該表，
   而該 xlsx **無任何嵌入物件**（本輪實測：`media`／`embed`／`.rtf`／`.emf`
   命中 **0**），三個分頁亦無該表之文字列（命中 0）。
   **即：權威表之內容於綁定來源中不存在。**

**故無從確認任一具名 feature「不在表內」。** 寫下去即造值（IN §8.4.1）。

> **本項不是「規格未要求」**（要求明載於 CFTS022），
> **是「要求已知而樣本不可定」。** 二者性質不同：
> 前者登記後可能永遠不必補；**後者一旦樣本可得即應補。**

### 解除之條件（任一）

| # | 條件 | 效果 |
|---|---|---|
| 甲 | 上游提供 `Driver Distraction Lockout Table` 之**可機讀版本**（或確認 p7 即該表之完整呈現）| 得自表外選具名樣本，於 `-013`／`-015` **同則**加負向斷言（同一 trigger 之另一後果，IN §5.7；**不另立 TC**）|
| 乙 | 分析層指定一個經確認不在表內之 feature | 同上 |
| 丙 | 上游確認負向面不屬 `-120`／`-121` 之驗證範圍 | 本項改為 CLOSED（不必驗）|

**未解除前**：`-013`／`-015` 之 `reasoning` 載明該面未涵蓋及其理由（已載）。

### ~~本項未登 DR 之理由~~ —— **已由 DR-DD8 承接（下放包 16 §二）**

> ~~甲案之標的（可機讀之表）為**素材**，性質同 DR-DD3 之 MCT ——
> **是否另立 DR 索取，屬分析層**（執行層不代登，同上繳 09 §3.3 之處置）。~~

**分析層已裁：立 `DR-DD8`（必發）**，文稿逐字見
`DATA_REQUESTS.md` §`DR-DD8`（下放包 16 §二，本輪 T-登建檔 DRAFTED）。
其所索者即上表**甲案**之標的：`Driver Distraction Lockout Table` 之
可機讀本（所引之 `.rtf`，或等效之試算表／文字匯出）。

| 本缺口之解除條件 | 承接之 DR | 對應關係 |
|---|---|---|
| 甲（可機讀之表）| **DR-DD8** | 直接 —— DR-DD8 之 Request 段即甲案 |
| 乙（分析層指定樣本）| — | 不需 DR；分析層逕指定即可 |
| 丙（上游確認不屬驗證範圍）| **DR-DD8** | 間接 —— 回覆若為「表中無非 L/O 列」即丙 |

**狀態仍為 OPEN**：DR-DD8 為 DRAFTED（**未發送**），故甲、丙皆未成就。
DR-DD8 文稿末句已逐字載明本缺口之連結：
`Until then this negative aspect is recorded as a coverage gap ([CG-DD1])
in SWQT test case generation.`

### ~~⚠ 影響 leaf 之範圍 —— 本輪未擴，但須記明~~ —— **提案有誤，已由下放包 17 §一-2 更正**

上繳包 13 §2.3 曾提案：DR-DD8 所引之 CFTS022 `-120`／`-121` 之 037 衍生 leaf
為 `-021`~`-024`，與本條之 `-013`／`-015` 相連。**該對映是錯的。**

**分析層之更正（下放包 17 §一-2）＋ 執行層之覆核（本輪實測 CFTS022 `Basic Report`）**：

| ObjectID | CFTS022 列 | 037 衍生 leaf | 出處 |
|---|---|---|---|
| `4915112` | `SYS-RA-Driver_Distraction-120` | **`-013`／`-014`** | r121；B1 之 `-013`／`-014` spec_ref |
| `4915115` | `SYS-RA-Driver_Distraction-121` | **`-015`／`-016`** | r122；B1 之 `-015`／`-016` spec_ref |
| `4915120` | `-125`（HK 章閘）| `-017`~`-024` 之共同閘 | r126 |
| `4915123`／`4915124` | `-128`／`-129` | `-021`~`-024` | r129／r130 |

**即 `-021`~`-024` 之 source 為 `-125` ＋ `-128`／`-129`，與 `-120`／`-121` 無關。**

**裁定（下放包 17 §四 10-5）**：本條之影響範圍**維持 `-013`／`-015`**；
`-014`／`-016` 為 AC2（fail-safe）列，不受負向面影響，**不擴列**。

> **這一條兩邊都要記。** 執行層依「範圍之認定屬分析層」之拘束**不逕改而提交裁定**，
> 程序正確 —— **而提案本身是錯的**。
> **若當時逕改，錯的對映就會直接寫進台帳。**
> 這正是「不逕改」拘束存在的理由（下放包 17 §一-2 逐字）。

