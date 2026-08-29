# CFTS020 全域重判 — 逐物件三軸實值與 R-ICS2 **v2(b)** 判定

> **本檔取代 `02_cfts020_face_recon.md`**（該檔為 R-ICS2 **v1** 下之結果，
> 依 R-ICS2 v2(d) **已作廢**；舊檔依 R-TM13 保留不刪、不改）。
> 下放包 03 作業 B。**本檔不生 TC**（R-ICS9(e)）。
> 本檔由 `scripts/gen_recon_v2.py` 產生，**表格非人工謄寫**。

現行判準 **R-ICS2 v2(b)**（CFTS020 專用，逐字見 `RULINGS.md`）：

- (i) `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE Architecture ∈ {Atlantis High, All}`
- (ii) `ECU` 軸**存在時**須含 `{ICS, LTM}`；**不存在時不視為不適用，亦不記 WARN**
- (iii) 章節分支為**輔證**，不得取代逐物件實測（v2(c)／R-ICS9(b)）

已作廢之 v1 判準（僅為產生 §2 差異表而保留於腳本，**不得引用**）：
`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`，
軸缺而無實質落空者標 `WARN-軸缺`。

---

## §0 掃描條件與母數

| 項 | 條件／實測 |
|---|---|
| 來源檔 | `inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` 之 `word/document.xml` |
| 轉純文字 | `</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape` |
| 物件辨識 | 屬性頭正則 `^(\d{7}): \[`，**區分大小寫**，行首先 `strip()` |
| 章節辨識 | `^(\d+(?:\.\d+)*) (.+?) \{(\d{7})\}$` 且該行不含 `PAGEREF`（目次行帶 `PAGEREF`）|
| 屬性抓取 | 同一行 `\[([^:\]]+):([^\]]*)\]` 逐段，key 大小寫原樣 |
| 軸值切分 | 逗號切分後 `strip()`；軸不存在記 `None`，**不視為空集合、不以章節屬性代替** |
| 軸值比對 | 區分大小寫之精確字串集合交集（不正規化、不前綴比對）|

- 物件總數（上式正則命中數）：**2180**
- 相異 ObjectID：**2180**（無重號）
- `ECU` 軸不存在者：**1916**（87.9%）
- `Radio` 軸不存在者：**10**
- `EE Architecture` 軸不存在者：**11**
- Artifact Type 分佈：{'Description': 160, 'Subsystem Functional Requirement': 2020}

> **407 為章節標題數，非物件數**（A-ICS15）。本檔全部統計之母數皆為物件數 2180，二者不混用。

---

## §1 全域判定分佈（v2）

| 判定 | 物件數 | 佔比 |
|---|---|---|
| 適用 | **254** | 11.7% |
| 不適用 | **1926** | 88.3% |
| 合計 | 2180 | 100% |

**v2 無 WARN 類**：v2(b)(ii) 明文「ECU 軸不存在時不視為不適用，亦不記 WARN」，
故 v1 之 `WARN-軸缺` 於 v2 全數消滅，判定只餘二類。
R-DD24 之第四欄「強度」仍保留，於 v2 下改以**軸齊備與否**分級（非 WARN）：

| 強度 | 物件數 |
|---|---|
| — | 1926 |
| 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） | 226 |
| 正面命中（三軸齊備且全命中） | 28 |

對照（**僅供沿革，判準已作廢**）v1 分佈：{'不適用': 1916, 'WARN-軸缺': 236, '適用': 28}。

---

## §2 v1 → v2 差異表

判定改變者共 **236** 筆（母數 2180，即 10.8%）。轉變型態統計：

| v1 判定 | → | v2 判定 | 筆數 |
|---|---|---|---|
| WARN-軸缺 | → | 適用 | **226** |
| WARN-軸缺 | → | 不適用 | **10** |

轉變原因分類：

| 原因 | 筆數 |
|---|---|
| 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） | 226 |
| 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） | 10 |

下表以 ObjectID 為鍵**逐一列出全部 236 筆**（不只給統計，下放包 03 §4 差異表要求）。

<details><summary>v1 → v2 差異全表（逐筆，236 列）</summary>

| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | v1 判定 | → | v2 判定 | 轉變原因 |
|---|---|---|---|---|---|---|---|---|---|
| 4819144 | 1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, R1L-R | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819146 | 1.4.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1L, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819150 | 1.4.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819151 | 1.4.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819152 | 1.4.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819153 | 1.4.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1L-R, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819154 | 1.4.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1H, R1M | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819157 | 1.4.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1M, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819158 | 1.4.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819159 | 1.4.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1L, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819160 | 1.4.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819161 | 1.4.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1H, R1M | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819185 | 1.4.1.1.6 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819186 | 1.4.1.1.6 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819187 | 1.4.1.1.6 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819188 | 1.4.1.1.6 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819189 | 1.4.1.1.6 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L, R1L-R | Atlantis Mid, CUSW, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819192 | 1.4.1.1.7 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1H, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819193 | 1.4.1.1.7 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819194 | 1.4.1.1.7 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819195 | 1.4.1.1.7 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819196 | 1.4.1.1.7 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, R1L | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819213 | 1.4.1.1.10 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819214 | 1.4.1.1.10 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819215 | 1.4.1.1.10 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819216 | 1.4.1.1.10 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819217 | 1.4.1.1.10 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1L-R, R1H | Atlantis High, CUSW, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819220 | 1.4.1.1.11 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819221 | 1.4.1.1.11 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819222 | 1.4.1.1.11 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819223 | 1.4.1.1.11 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819224 | 1.4.1.1.11 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1M, R1L-R | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819227 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819228 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819229 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819230 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819231 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | Atlantis Mid, Atlantis High, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819233 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819234 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819235 | 1.4.1.1.12 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819238 | 1.4.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819239 | 1.4.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819240 | 1.4.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1H, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819241 | 1.4.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1M, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819242 | 1.4.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1M, R1L-R | Atlantis Mid, Atlantis High, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819245 | 1.4.1.2.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1H, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819246 | 1.4.1.2.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819247 | 1.4.1.2.2 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819248 | 1.4.1.2.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1L-R, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819249 | 1.4.1.2.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, R1L | Atlantis Mid, Atlantis High, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819270 | 1.4.1.2.6 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1M, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819271 | 1.4.1.2.6 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1M, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819272 | 1.4.1.2.6 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819273 | 1.4.1.2.6 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819274 | 1.4.1.2.6 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1L-R, R1H | Atlantis Mid, CUSW, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819294 | 1.4.1.2.9 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1M, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819297 | 1.4.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1H, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819298 | 1.4.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819299 | 1.4.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819300 | 1.4.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819301 | 1.4.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1M, R1H | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819304 | 1.4.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819305 | 1.4.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819306 | 1.4.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819307 | 1.4.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819308 | 1.4.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | CUSW, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819311 | 1.4.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1L, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819312 | 1.4.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L-R, R1L, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819313 | 1.4.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819314 | 1.4.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819315 | 1.4.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1L-R, R1H | Atlantis Mid, Atlantis High, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819331 | 1.4.1.3.5 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819334 | 1.4.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819335 | 1.4.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819336 | 1.4.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819337 | 1.4.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819338 | 1.4.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L | Atlantis High, Atlantis Mid, CUSW | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819341 | 1.4.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1L, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819344 | 1.4.2.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819347 | 1.4.3.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1L, R1H, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819348 | 1.4.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, R1M, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819349 | 1.4.3.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819350 | 1.4.3.1 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1M, R1L-R | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819351 | 1.4.3.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1H, R1M | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819355 | 1.4.3.3 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1M, R1H | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819365 | 1.5.1 | Description | **軸缺** | R1L-R, R1L | All | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819541 | 1.8.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, R1L, R1L-R, R1M, VP4R84, VP484 | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819543 | 1.8.1.1 | Description | **軸缺** | R1M, VP4R84, R1L, VP484, R1H, VP384, R1L-R | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819545 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819547 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, VP484, R1M, R1L, R1L-R, R1H | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819548 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, R1M, R1H, R1L-R, VP384, VP484 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819549 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, R1L, VP4R84, R1H, R1L-R, VP484 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819550 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1M, VP384, R1H, VP4R84, VP484 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819551 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, VP484, R1M, R1L-R, R1H, VP384 | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819552 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819553 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP384, R1H, VP484, R1M, VP4R84 | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819555 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, VP484, VP384, R1L-R, VP4R84, R1M | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819558 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, VP384, VP5R120, VP4R84, R1L, VP484 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819559 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, VP484, VP4R84, R1L, R1L-R, R1H | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819560 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, VP384, R1L-R, VP4R84, VP484, R1H, R1M | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819561 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, VP5R120, R1L-R, VP484, R1L, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819563 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP484, VP5R120, VP384, R1H, R1M, VP4R84, R1L-R | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819564 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP4R84, R1L, R1L-R, VP5R120, R1M, R1H, VP384 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819571 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, VP5R120, VP484, VP4R84, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819572 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, R1M, R1H, VP384, VP5R120, VP484, R1L-R | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819573 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, R1L-R, R1H, VP484, R1M, VP5R120, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819574 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, R1L-R, VP5R120, R1H, R1M | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819575 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, VP384, VP4R84, R1L-R, VP5R120, VP484, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819576 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, VP484, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819578 | 1.8.1.2 | Description | **軸缺** | VP484, VP384, R1L-R, R1M, VP4R84, R1H, R1L | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819579 | 1.8.1.2 | Description | **軸缺** | R1M, R1H, R1L-R, VP484, VP4R84, R1L, VP384 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819580 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, VP4R84, VP484, R1M, VP384 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819581 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP484, VP384, R1M, VP4R84, R1H | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819582 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L, VP384, VP4R84, VP484 | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819583 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819584 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, VP4R84, R1H, VP484, R1M, VP384 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819585 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, VP384, VP4R84, R1M, VP484, R1H, R1L-R | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819586 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP4R84, R1H, R1M, VP384, R1L, VP484 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819588 | 1.8.1.3 | Description | **軸缺** | VP384, R1M, R1L, VP484, R1L-R, R1H, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819616 | 1.8.1.4 | Description | **軸缺** | R1M, R1H, R1L-R, VP384, VP484, VP4R84, R1L | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819617 | 1.8.1.4 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP484, R1M, R1H, R1L, VP384, R1L-R | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819618 | 1.8.1.4 | Description | **軸缺** | R1L, R1L-R, R1H, R1M, VP4R84, VP484, VP384 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819619 | 1.8.1.4 | Description | **軸缺** | R1M, VP4R84, R1H, R1L, VP484, R1L-R, VP384 | PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819628 | 1.8.2.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, VP384, VP5R120, R1M, R1L-R, R1H, VP484 | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819630 | 1.8.2.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP384, VP4R84, R1L, R1M, R1H, VP484, VP5R120 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819631 | 1.8.2.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, R1L-R, R1H, R1L, R1M, VP484, VP384 | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819632 | 1.8.2.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP484, VP4R84, R1L-R, R1L, VP5R120, VP384, R1H | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819635 | 1.8.2.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP5R120, VP384, R1L, R1M, R1L-R, VP4R84, VP484 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819637 | 1.8.2.1.2 | Subsystem Functional Requirement | **軸缺** | VP384, R1L-R, VP484, R1H, VP5R120, R1M, VP4R84, R1L | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819638 | 1.8.2.1.2 | Subsystem Functional Requirement | **軸缺** | VP484, VP384, R1L, R1H, R1M, VP4R84, VP5R120, R1L-R | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819641 | 1.8.2.1.2.1 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, VP5R120, VP484, R1L-R, R1M, VP4R84, R1H | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819642 | 1.8.2.1.2.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1H, R1L-R, VP4R84, VP384, R1L, R1M, VP484 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819644 | 1.8.2.1.2.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP4R84, R1H, VP484, R1M, R1L-R, VP5R120, R1L | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819645 | 1.8.2.1.2.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L-R, R1L, R1M, VP384, VP484, VP5R120, R1H | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819646 | 1.8.2.1.2.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, R1L, VP5R120, VP4R84 | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819648 | 1.8.2.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, VP484, VP5R120, R1L-R, VP384, R1H, R1M | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819651 | 1.8.2.1.3.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP484, R1L, VP384, R1H, R1L-R, R1M, VP4R84 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819652 | 1.8.2.1.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, VP4R84, R1H, VP384, VP484, R1L-R, VP5R120 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819654 | 1.8.2.1.3.1 | Subsystem Functional Requirement | **軸缺** | VP484, R1L-R, VP384, R1M, VP5R120, VP4R84, R1L, R1H | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819657 | 1.8.2.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, VP384, VP5R120, R1L, R1H, VP4R84, VP484 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819659 | 1.8.2.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, R1H, VP384, R1L-R, VP484, R1M, VP5R120 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819662 | 1.8.2.1.3.3 | Subsystem Functional Requirement | **軸缺** | VP384, VP484, R1M, VP5R120, R1L-R, VP4R84, R1L, R1H | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819664 | 1.8.2.1.3.3 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, VP484, VP384, VP5R120, R1L, VP4R84, R1H | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819667 | 1.8.2.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP4R84, VP5R120, R1H, VP384, R1L, R1L-R, VP484 | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819668 | 1.8.2.1.4.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP5R120, VP484, R1M, VP4R84, R1H, R1L, R1L-R | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819670 | 1.8.2.1.4.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1L-R, VP4R84, VP384, VP484, VP5R120, R1H | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819671 | 1.8.2.1.4.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP384, VP4R84, R1L, R1M, VP5R120, R1H, R1L-R | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819679 | 1.8.2.1.4.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, VP384, VP5R120, VP4R84, VP484, R1H, R1L | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819712 | 1.8.2.3 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819748 | 1.8.2.3.3 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819827 | 1.8.2.3.10 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819849 | 1.8.2.5 | Description | **軸缺** | R1H, VP5R120, R1M, VP384, R1L-R, VP484, R1L, VP4R84 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819859 | 1.8.2.5.2 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, R1L-R, R1M | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819861 | 1.8.2.5.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1L, R1M | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819863 | 1.8.2.5.2 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L-R, R1L | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819865 | 1.8.2.5.2 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L-R, R1L | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819868 | 1.8.2.5.2 | Subsystem Functional Requirement | **軸缺** | R1H, R1M, R1L-R, R1L | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819869 | 1.8.2.5.2 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819871 | 1.8.2.6 | Description | **軸缺** | VP484, R1H, VP5R120, R1L, R1L-R, R1M, VP384, VP4R84 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819872 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP384, R1M, R1L, R1H, VP484, VP5R120, VP4R84 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819875 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP5R120, VP384, R1M, R1L, R1L-R, R1H, VP484 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819877 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1L, VP5R120, VP4R84, R1H | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819878 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP384, R1M, R1L-R, VP4R84, R1L, VP484, R1H, VP5R120 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819879 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | R1M, VP484, VP5R120, R1L-R, R1L, VP4R84, R1H, VP384 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819880 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | R1H, VP484, VP4R84, R1L, R1L-R, R1M, VP384, VP5R120 | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819884 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, R1L, VP5R120, R1M, VP484, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819885 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, VP5R120, VP4R84, VP384, R1H, VP484, R1M | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819889 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP484, VP4R84, R1H, R1L, VP384, R1M, R1L-R | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819890 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1H, VP4R84, VP384, R1M, R1L, VP484, R1L-R | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819897 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP384, R1L-R, R1L, R1H, R1M, VP4R84, VP484 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819905 | 1.8.2.6 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP484, R1M, R1L, VP5R120, VP384, R1H, R1L-R | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819914 | 1.8.2.7 | Description | **軸缺** | R1M, R1L-R, R1H, VP484, R1L, VP384, VP4R84, VP5R120 | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819915 | 1.8.2.7 | Subsystem Functional Requirement | **軸缺** | VP384, VP4R84, R1H, R1M, R1L, VP5R120, VP484, R1L-R | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819916 | 1.8.2.7 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, R1L-R, VP484, R1L, R1H, VP4R84 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819917 | 1.8.2.7 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, VP5R120, R1M, R1L-R, R1H | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819919 | 1.8.2.7 | Subsystem Functional Requirement | **軸缺** | R1H, VP484, VP384, R1L, VP4R84, R1L-R, VP5R120, R1M | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819921 | 1.8.2.8 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1H, R1L, R1M, R1L-R, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4819947 | 1.8.4.2 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819960 | 1.8.5.1 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819985 | 1.8.5.2.1 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819990 | 1.8.5.2.1 | Description | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819996 | 1.8.5.2.1 | Subsystem Functional Requirement | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4819997 | 1.8.5.2.1 | Subsystem Functional Requirement | **軸缺** | **軸缺** | **軸缺** | WARN-軸缺 | → | 不適用 | 軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定） |
| 4820117 | 1.9.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L, R1L-R | Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820120 | 1.9.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP484, VP384, R1H, VP5R120, R1L, R1M, R1L-R | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820130 | 1.9.1.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1M, R1L, VP384, VP484, R1L-R, VP5R120, R1H | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820134 | 1.9.1.1.2 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1M, R1L, VP5R120, R1H, R1L-R, VP484, VP384 | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820135 | 1.9.1.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP4R84, VP484, R1H, VP384, R1L, VP5R120, R1M | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820137 | 1.9.1.1.2 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1H, VP484, R1M, R1L-R, R1L, VP5R120, VP384 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820147 | 1.9.2.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP384, VP4R84, VP484, R1M, VP5R120, R1L-R, R1H | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820152 | 1.9.3.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820153 | 1.9.3.1 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L, VP5R120, VP484, R1L-R, R1M, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820157 | 1.9.3.2 | Subsystem Functional Requirement | **軸缺** | VP484, R1M, R1L, R1H, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4820159 | 1.9.3.3 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1M, VP4R84, VP484, R1L-R, VP384, R1L, R1H | Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821013 | 1.15.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, R1L-R, VP5R120, R1M, R1H, VP484 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821015 | 1.15.3.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP484, R1L, R1M, VP384, R1L-R, VP4R84, VP5R120 | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821016 | 1.15.3.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP484, VP384, VP5R120, R1L, VP4R84, R1L-R, R1M | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821017 | 1.15.3.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1L-R, R1H, VP4R84, VP484, VP384, R1L, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821023 | 1.15.3.2 | Subsystem Functional Requirement | **軸缺** | R1L, VP384, R1M, VP5R120, VP4R84, R1H, R1L-R, VP484 | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821027 | 1.15.3.2.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP484, R1M, R1L-R, VP5R120, VP384, VP4R84, R1L | Atlantis Mid, PowerNet, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821030 | 1.15.3.2.1 | Subsystem Functional Requirement | **軸缺** | VP484, R1L-R, R1L, R1H, R1M, VP384, VP5R120, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821031 | 1.15.3.2.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP4R84, R1H, R1L, R1L-R, VP5R120 | Atlantis Mid, Atlantis High, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821033 | 1.15.3.3 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, VP484, R1H, VP384, R1L, R1L-R, R1M | PowerNet, Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821037 | 1.15.3.3.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP5R120, R1H, VP484, VP384, VP4R84, R1M, R1L-R | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821042 | 1.15.3.3.2 | Subsystem Functional Requirement | **軸缺** | VP484, R1M, R1L, VP5R120, VP384, R1L-R, VP4R84, R1H | Atlantis High, PowerNet, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821049 | 1.15.3.3.3 | Subsystem Functional Requirement | **軸缺** | VP484, VP5R120, VP4R84, R1H, VP384, R1L, R1M, R1L-R | PowerNet, Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821053 | 1.15.3.4.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, R1H, R1L-R, VP384, R1M, VP484, VP4R84 | Atlantis High, Atlantis Mid, PowerNet | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821675 | 1.18.1 | Description | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821676 | 1.18.1 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821679 | 1.18.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821681 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821683 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821684 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821685 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821686 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821687 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821688 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821689 | 1.18.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821691 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821693 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821694 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821695 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821696 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821697 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821698 | 1.18.1.1.3 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821700 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821701 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821702 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821703 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821704 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821705 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821706 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821707 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821708 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821709 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis Mid, Atlantis High | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |
| 4821710 | 1.18.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | Atlantis High, Atlantis Mid | WARN-軸缺 | → | 適用 | 軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除） |

</details>

---

## §3 三面之物件清單（依 v2 重列）

四欄依 R-DD23／R-DD24：**數據**（ECU／Radio／EE 三軸實值）、**判斷**、**所印之理由**、**強度**。

### §3.1 Display（SWRA 006／007）

（本面所列章節之物件合計 18，判定分佈 {'不適用': 6, '適用': 12}）

#### §1.8.1.1.1 HU behavior in response to ICS POWER hardkey pressed events {4819556} — 主

物件 **8** 個；v2 判定分佈 **{'不適用': 2, '適用': 6}**；（v1 為 {'不適用': 2, 'WARN-軸缺': 6}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819557 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, VP484, VP384 | PowerNet | 不適用 | Radio ['VP5R120', 'VP4R84', 'VP484', 'VP384'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819558 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, VP384, VP5R120, VP4R84, R1L, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819559 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, VP484, VP4R84, R1L, R1L-R, R1H | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819560 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, VP384, R1L-R, VP4R84, VP484, R1H, R1M | PowerNet, Atlantis High, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819561 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, VP5R120, R1L-R, VP484, R1L, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819562 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819563 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP484, VP5R120, VP384, R1H, R1M, VP4R84, R1L-R | Atlantis Mid, PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819564 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP4R84, R1L, R1L-R, VP5R120, R1M, R1H, VP384 | Atlantis Mid, Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |

<details><summary>逐物件本文（逐字，8 條）</summary>

- **4819557**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819558**（Subsystem Functional Requirement／適用）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819559**（Subsystem Functional Requirement／適用）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819560**（Subsystem Functional Requirement／適用）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819561**（Subsystem Functional Requirement／適用）：If $Telematic_Power$ = [Full_Operation] and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity]. See {CFTS009-829}.
- **4819562**（Subsystem Functional Requirement／不適用）：During the '3-second' time period if the ICS Power button is pressed the HU shall cancel the "3-second" screen timer, shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and shall return to the previous 'HU Screen On' screen.
- **4819563**（Subsystem Functional Requirement／適用）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819564**（Subsystem Functional Requirement／適用）：If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen. See {CFTS009-829}.

</details>

#### §1.8.1.1.3 HU behavior in response to ICS SCREEN OFF hardkey press events {4819570} — 主

物件 **6** 個；v2 判定分佈 **{'適用': 6}**；（v1 為 {'WARN-軸缺': 6}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819571 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, VP5R120, VP484, VP4R84, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819572 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, R1M, R1H, VP384, VP5R120, VP484, R1L-R | Atlantis Mid, Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819573 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, R1L-R, R1H, VP484, R1M, VP5R120, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819574 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, R1L-R, VP5R120, R1H, R1M | Atlantis Mid, PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819575 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, VP384, VP4R84, R1L-R, VP5R120, VP484, R1M | Atlantis High, PowerNet, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819576 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, VP484, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |

<details><summary>逐物件本文（逐字，6 條）</summary>

- **4819571**（Subsystem Functional Requirement／適用）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819572**（Subsystem Functional Requirement／適用）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS SCREEN OFF hardkey should be responded to, then the HU shall continue to send $TGW_DISP_STAT$ = [DISP_NORMAL], and $RQ_DISP_INTS$ <> [0% Intensity] until the 3 second "TOUCH SCREEN TO TURN ON" timer expires as defined in the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4.
- **4819573**（Subsystem Functional Requirement／適用）：During the '3-second' time period if the ICS SCREEN OFF hardkey is pressed the HU shall cancel the "TOUCH SCREEN TO TURN ON" screen timer, the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819574**（Subsystem Functional Requirement／適用）：After the '3-second' time period is complete, the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819575**（Subsystem Functional Requirement／適用）：For the pop-ups stated in HMI core specification requirement H4; the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity] for the duration of the pop-up and then send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] once the pop-up expires.
- **4819576**（Subsystem Functional Requirement／適用）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS SCREEN OFF hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.

</details>

#### §1.5.1.1.1 HU behavior in response to ICS POWER hardkey pressed events {4819385} — 對照

物件 **3** 個；v2 判定分佈 **{'不適用': 3}**；（v1 為 {'不適用': 3}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819386 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819387 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819388 | 1.5.1.1.1 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |

<details><summary>逐物件本文（逐字，3 條）</summary>

- **4819386**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819387**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note PITA4, "Screen Off and HU Power button selections shall be ignored while backup cam is being shown."
- **4819388**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.

</details>

#### §1.5.1.1.2 HU behavior in response to ICS SCREEN OFF hardkey press events {4819389} — 對照

物件 **1** 個；v2 判定分佈 **{'不適用': 1}**；（v1 為 {'不適用': 1}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819390 | 1.5.1.1.2 | Subsystem Functional Requirement | **軸缺** | allSys | PowerNet | 不適用 | EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |

<details><summary>逐物件本文（逐字，1 條）</summary>

- **4819390**（Subsystem Functional Requirement／不適用）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."

</details>

### §3.2 Browse（SWRA 003／004）

（本面所列章節之物件合計 9，判定分佈 {'適用': 9}）

#### §1.8.1.2 Rotary Knob Data Transfer {4819577} — 主

物件 **9** 個；v2 判定分佈 **{'適用': 9}**；（v1 為 {'WARN-軸缺': 9}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819578 | 1.8.1.2 | Description | **軸缺** | VP484, VP384, R1L-R, R1M, VP4R84, R1H, R1L | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819579 | 1.8.1.2 | Description | **軸缺** | R1M, R1H, R1L-R, VP484, VP4R84, R1L, VP384 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819580 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, R1L-R, VP4R84, VP484, R1M, VP384 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819581 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP484, VP384, R1M, VP4R84, R1H | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819582 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1H, R1M, R1L, VP384, VP4R84, VP484 | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819583 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819584 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, VP4R84, R1H, VP484, R1M, VP384 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819585 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L, VP384, VP4R84, R1M, VP484, R1H, R1L-R | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819586 | 1.8.1.2 | Subsystem Functional Requirement | **軸缺** | R1L-R, VP4R84, R1H, R1M, VP384, R1L, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |

<details><summary>逐物件本文（逐字，9 條）</summary>

- **4819578**（Description／適用）：The ICS will send signals on the BH-CAN to communicate the status of the rotary knobs.
- **4819579**（Description／適用）：This section describes the signals to be used to support the communication of knob rotations to the HU. Refer to the feature sections that describe specific features to determine how the knob information supports those features.
- **4819580**（Subsystem Functional Requirement／適用）：The ICS shall send the $ICS_KNOB<n>_DIR$ and $ICS_KNOB<n>_VAL$ signals to indicate the periodic and on-change status of any physical knob on the ICS. Within the scope of this section the value of "<n>" will represent a value of 1 or 2 for the assigned knobs.
- **4819581**（Subsystem Functional Requirement／適用）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$$ICS_KNOB2_DIR$ and $ICS_KNOB2_VAL$
- **4819582**（Subsystem Functional Requirement／適用）：When a physical knob is not rotated, the ICS shall send the $ICS_KNOB<n>_DIR$ = [no change] signal. For this state, the value of $ICS_KNOB<n>_VAL$ shall be ignored by the receiving components and no action taken on the value.
- **4819583**（Subsystem Functional Requirement／適用）：While a knob is being rotated, the ICS shall count the relative number of detents rotated through in <TPeriodToCountKnobDetents> seconds. The ICS shall send the information in a pair of on-change messages using the $ICS_KNOB<n>_DIR$ = [increment or  decrement] and $ICS_KNOB<n>_VAL$ = [1 to 63] signals and values and then within <TPeriodToSendNoChange> seconds send the $ICS_KNOB<n>_DIR$ = [Knob_no_change] and $ICS_KNOB<n>_VAL$ = [0] signals and values.
- **4819584**（Subsystem Functional Requirement／適用）：When the ICS determines no change in the rotation direction or value, the ICS shall send $ICS_KNOB<n>_DIR$ = [no change] and $ICS_KNOB<n>_VAL$ = [0] signals and values at the scheduled periodic rate until the knob is rotated again.
- **4819585**（Subsystem Functional Requirement／適用）：When the HU receives the $ICS_KNOB1_DIR$ and $ICS_KNOB1_VAL$ signals it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819586**（Subsystem Functional Requirement／適用）：When the HU receives $ICS_KNOB2_DIR$ and $ICS_KNOB2_VAL$ signals it shall determine the corresponding HMI screen to 'flow' to (Browse), if any, HMI screen to update (Scroll) or change in Entertainment Audio state ('Tune').

</details>

### §3.3 Navigation（SWRA 008／009）

（本面所列章節之物件合計 55，判定分佈 {'適用': 23, '不適用': 32}）

#### §1.8.1.1 Push Button Data Transfer {4819542}（含其子節 1.8.1.1.x） — 主

物件 **31** 個；v2 判定分佈 **{'適用': 22, '不適用': 9}**；（v1 為 {'WARN-軸缺': 22, '不適用': 9}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819543 | 1.8.1.1 | Description | **軸缺** | R1M, VP4R84, R1L, VP484, R1H, VP384, R1L-R | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819544 | 1.8.1.1 | Description | FPDM | R1L-R, VP4R84, VP384, R1H, VP484, R1L, R1M | Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819545 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1M, R1H, VP484, VP4R84, VP384, R1L | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819546 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP484 | PowerNet | 不適用 | Radio ['VP384', 'VP484'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819547 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, VP484, R1M, R1L, R1L-R, R1H | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819548 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP4R84, R1M, R1H, R1L-R, VP384, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819549 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, R1L, VP4R84, R1H, R1L-R, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819550 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L-R, R1L, R1M, VP384, R1H, VP4R84, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819551 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, VP484, R1M, R1L-R, R1H, VP384 | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819552 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819553 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1L-R, VP384, R1H, VP484, R1M, VP4R84 | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819554 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, VP484 | PowerNet | 不適用 | Radio ['VP4R84', 'VP384', 'VP484'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819555 | 1.8.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, R1H, VP484, VP384, R1L-R, VP4R84, R1M | Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819557 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, VP4R84, VP484, VP384 | PowerNet | 不適用 | Radio ['VP5R120', 'VP4R84', 'VP484', 'VP384'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819558 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, R1H, R1L-R, VP384, VP5R120, VP4R84, R1L, VP484 | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819559 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1M, VP384, VP5R120, VP484, VP4R84, R1L, R1L-R, R1H | PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819560 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP5R120, R1L, VP384, R1L-R, VP4R84, VP484, R1H, R1M | PowerNet, Atlantis High, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819561 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1H, VP384, VP5R120, R1L-R, VP484, R1L, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819562 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819563 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | R1L, VP484, VP5R120, VP384, R1H, R1M, VP4R84, R1L-R | Atlantis Mid, PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819564 | 1.8.1.1.1 | Subsystem Functional Requirement | **軸缺** | VP484, VP4R84, R1L, R1L-R, VP5R120, R1M, R1H, VP384 | Atlantis Mid, Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819566 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中）；Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ | — |
| 4819567 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中）；Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ | — |
| 4819568 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中）；Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ | — |
| 4819569 | 1.8.1.1.2 | Subsystem Functional Requirement | FPDM | noSys | Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中）；Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ | — |
| 4819571 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1H, R1L-R, VP5R120, VP484, VP4R84, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819572 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, R1L, R1M, R1H, VP384, VP5R120, VP484, R1L-R | Atlantis Mid, Atlantis High, PowerNet | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819573 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP384, R1L, R1L-R, R1H, VP484, R1M, VP5R120, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819574 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | VP4R84, VP384, R1L, VP484, R1L-R, VP5R120, R1H, R1M | Atlantis Mid, PowerNet, Atlantis High | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819575 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1H, R1L, VP384, VP4R84, R1L-R, VP5R120, VP484, R1M | Atlantis High, PowerNet, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819576 | 1.8.1.1.3 | Subsystem Functional Requirement | **軸缺** | R1L, R1M, R1H, VP484, VP384, VP4R84, R1L-R, VP5R120 | PowerNet, Atlantis High, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |

<details><summary>逐物件本文（逐字，31 條）</summary>

- **4819543**（Description／適用）：The ICS will send signals on the BH-CAN to communicate the status of the mechanical push buttons. Note: Some signals may not be used for various pushbuttons based on the version of the ICS module that is present.
- **4819544**（Description／不適用）：This section describes the signals to be used to support the communication of button presses to the HU and the FPDM.  Refer to the sections that describe specific features to determine the specific requirements to support these features. See Section {CFTS022-679} for a discussion of Stuck Button Behavior.
- **4819545**（Subsystem Functional Requirement／適用）：The ICS shall send the ICS signals to indicate the periodic and on-change status of any physical button on the ICS.
- **4819546**（Subsystem Functional Requirement／不適用）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICSMuteButton$$Enter_Button$$ICSScreenOffButton$$Back_Button$
- **4819547**（Subsystem Functional Requirement／適用）：See the latest version of the [Logical Identifiers and CAN Mapping v*.xlsx] file for the CAN signals related to the following Logical Identifiers (LIDs): $ICSMuteButton$$Enter_Button$$ICSScreenOffButton$$ICSPowerButton$
- **4819548**（Subsystem Functional Requirement／適用）：For all ICS buttons, the [not pressed] value shall be sent when the button is not pressed.
- **4819549**（Subsystem Functional Requirement／適用）：When a physical button is pressed, the ICS shall send an on-change[pressed] signal value within a time period of <Tbutton>.
- **4819550**（Subsystem Functional Requirement／適用）：As a physical button is pressed and held, the ICS shall continue to send the[pressed] value at a rate of <Tbutton> until the button is released.
- **4819551**（Subsystem Functional Requirement／適用）：After a physical button press is released, the ICS shall send an on-change [not pressed] signal value.
- **4819552**（Subsystem Functional Requirement／適用）：It may be possible that several buttons can be pressed at the same time. Each button event change (press or release) shall cause the ICS to send an on-change message with updated button status within the time period of <Tbutton>.
- **4819553**（Subsystem Functional Requirement／適用）：When the HU receives $ICSMuteButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819554**（Subsystem Functional Requirement／不適用）：When the HU receives $Enter_Button$ = [pressed] or$Back_Button$ = [pressed] it shall determine the corresponding HMI screen to 'flow' to, if any.
- **4819555**（Subsystem Functional Requirement／適用）：When the HU receives $Enter_Button$ = [pressed] it shall determine the corresponding HMI screen to 'flow' to, if any.
- **4819557**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819558**（Subsystem Functional Requirement／適用）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event or respond to it based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state. See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819559**（Subsystem Functional Requirement／適用）：When the HU receives $ICSPowerButton$ = [pressed] it shall determine the corresponding Volume adjustment behavior as defined in {CFTS019} and represented by the internal HU signal named ICS_Volume_Adjustment.Info.
- **4819560**（Subsystem Functional Requirement／適用）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819561**（Subsystem Functional Requirement／適用）：If $Telematic_Power$ = [Full_Operation] and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity]. See {CFTS009-829}.
- **4819562**（Subsystem Functional Requirement／不適用）：During the '3-second' time period if the ICS Power button is pressed the HU shall cancel the "3-second" screen timer, shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and shall return to the previous 'HU Screen On' screen.
- **4819563**（Subsystem Functional Requirement／適用）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819564**（Subsystem Functional Requirement／適用）：If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen. See {CFTS009-829}.
- **4819566**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [Power Button Not Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Not Pressed].When the HU receives $ICSPowerButton$ = [Power Button Pressed] it shall set the internal signal ICS_btn_46.Info = [Power Button Pressed].
- **4819567**（Subsystem Functional Requirement／不適用）：When the HU receives $ICSPowerButton$ = [pressed] the HU shall determine whether to ignore the POWER hardkey pressed event for the Front Passenger Display or respond to it based on the current power On/Off state and screen priority state.  See the HMI documents which define some states of the system when POWER hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom.
- **4819568**（Subsystem Functional Requirement／不適用）：If the HU/Front Passenger Display is in the 'Front Passenger Display Screen ON' state ($TGW_FPDM_DISP_STAT$ = [DISP_NORMAL] and $FPDM_RQ_DISP_INTS$ <> [0% Intensity]) and the FPDM Screen is in the 'FPDM Screen ON' state ($FPDM_DISP_STAT$ = [ON]) and the HU determines that the ICS POWER hardkey should be responded to, then the HU shall immediately send $TGW_FPDM_DISP_STAT$ = [DISP_OFF], and send $FPDM_RQ_DISP_INTS$ = [0% Intensity].
- **4819569**（Subsystem Functional Requirement／不適用）：When the Front Passenger Display is in the 'Front Passenger Display Screen OFF' state (displaying the "completely black screen") and the ICS POWER hardkey is pressed the HU shall send the signal $TGW_FPDM_DISP_STAT$ = [DISP_NORMAL] and $FPDM_RQ_DISP_INTS$ = [current non-zero value] and the Front Passenger Display shall return to the previous 'Front Passenger Display Screen ON' screen.
- **4819571**（Subsystem Functional Requirement／適用）：When the ICS SCREEN OFF hardkey is pressed the HU shall determine whether to ignore the SCREEN OFF hardkey pressed event or respond to it based on the current screen priority. See the HMI documents which define some states of the system when SCREEN OFF hardkey pressed events are ignored.Ex. In the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4, "Press Screen Off Hard or Soft Controls displays a Screen Off graphic over the entire screen with ‘Touch Screen to turn On’ displayed at the bottom, except while the backup cam is being shown, in which case Screen Off requests shall be ignored."
- **4819572**（Subsystem Functional Requirement／適用）：If the HU is in the 'HU Screen ON' state ($TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity]) and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and the HU determines that the ICS SCREEN OFF hardkey should be responded to, then the HU shall continue to send $TGW_DISP_STAT$ = [DISP_NORMAL], and $RQ_DISP_INTS$ <> [0% Intensity] until the 3 second "TOUCH SCREEN TO TURN ON" timer expires as defined in the latest version of ''VP* SR* * HMI Logic and Flow Release *.pdf''; HMI Note H4.
- **4819573**（Subsystem Functional Requirement／適用）：During the '3-second' time period if the ICS SCREEN OFF hardkey is pressed the HU shall cancel the "TOUCH SCREEN TO TURN ON" screen timer, the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.
- **4819574**（Subsystem Functional Requirement／適用）：After the '3-second' time period is complete, the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity].
- **4819575**（Subsystem Functional Requirement／適用）：For the pop-ups stated in HMI core specification requirement H4; the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity] for the duration of the pop-up and then send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] once the pop-up expires.
- **4819576**（Subsystem Functional Requirement／適用）：When the HU is in the 'HU Screen OFF' state (displaying the "completely black screen") and the ICS SCREEN OFF hardkey is pressed the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' screen.

</details>

#### §1.8.1.3 Button Press Events {4819587} — 主

物件 **24** 個；v2 判定分佈 **{'適用': 1, '不適用': 23}**；（v1 為 {'WARN-軸缺': 1, '不適用': 23}，已作廢）

| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | 數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |
|---|---|---|---|---|---|---|---|---|
| 4819588 | 1.8.1.3 | Description | **軸缺** | VP384, R1M, R1L, VP484, R1L-R, R1H, VP4R84 | Atlantis High, PowerNet, Atlantis Mid | 適用 | 三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除） | 正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN） |
| 4819589 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP484, R1H, VP4R84, R1L-R, VP384, R1M, R1L | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819590 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP4R84, R1L, R1L-R, VP484, VP384, R1M, R1H | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819591 | 1.8.1.3 | Subsystem Functional Requirement | FPDM | VP384, R1H, R1L-R, VP484, R1M, VP4R84, R1L | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819593 | 1.8.1.3.1 | Description | FPDM | VP4R84, VP484, R1L, R1H, R1L-R, R1M, VP384 | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819594 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | VP384, VP484, VP4R84 | PowerNet | 不適用 | Radio ['VP384', 'VP484', 'VP4R84'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819595 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L, R1L-R, R1M, VP4R84, R1H, VP484, VP384 | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819596 | 1.8.1.3.1 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819597 | 1.8.1.3.1 | Subsystem Functional Requirement | FPDM | R1L-R, R1L, R1M, R1H, VP484, VP4R84, VP384 | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819599 | 1.8.1.3.2 | Description | FPDM, CCDMF | VP4R84, R1H, R1L, R1L-R, R1M, VP484, VP384 | Atlantis Mid, PowerNet, Atlantis High | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819600 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | R1M, R1H | Atlantis High | 不適用 | Radio ['R1M', 'R1H'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅ | — |
| 4819601 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP484, R1M, R1L-R, VP384, R1H, R1L, VP4R84 | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819602 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | VP384, R1H, VP4R84, R1M, R1L-R, VP484, R1L | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819603 | 1.8.1.3.2 | Subsystem Functional Requirement | FPDM, CCDMF | VP384, R1L-R, VP484, R1L, R1H, VP4R84, R1M | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['FPDM', 'CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819604 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP384, R1M, VP484, R1L, VP4R84, R1H, R1L-R | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819605 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | R1L-R, VP4R84, R1M, VP384, R1H, VP484, R1L | Atlantis High, Atlantis Mid, PowerNet | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819606 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF | R1H, R1M, R1L-R, R1L, VP4R84, VP484, VP384 | Atlantis High, PowerNet, Atlantis Mid | 不適用 | ECU ['CCDMF'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819607 | 1.8.1.3.2 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819608 | 1.8.1.3.2 | Subsystem Functional Requirement | CCDMF, FPDM | VP4R84, VP384, R1L-R, R1L, R1H, VP484, R1M | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['CCDMF', 'FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819610 | 1.8.1.3.3 | Description | FPDM | VP4R84, VP484, R1L-R, R1M, R1L, R1H, VP384 | Atlantis Mid, PowerNet, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819611 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1H, VP4R84, R1L-R, VP484, VP384, R1L, R1M | PowerNet, Atlantis High, Atlantis Mid | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819612 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1M, R1L-R, R1H, VP484, VP384, R1L, VP4R84 | PowerNet, Atlantis Mid, Atlantis High | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |
| 4819613 | 1.8.1.3.3 | Subsystem Functional Requirement | **軸缺** | noSys | PowerNet | 不適用 | Radio ['noSys'] ∩ ['R1L', 'R1L-R', 'allSys'] = ∅；EE ['PowerNet'] ∩ ['All', 'Atlantis High'] = ∅ | — |
| 4819614 | 1.8.1.3.3 | Subsystem Functional Requirement | FPDM | R1L, VP384, VP484, R1L-R, VP4R84, R1H, R1M | Atlantis Mid, Atlantis High, PowerNet | 不適用 | ECU ['FPDM'] ∩ ['ICS', 'LTM'] = ∅（v2(b)(ii)：軸存在故須命中） | — |

<details><summary>逐物件本文（逐字，24 條）</summary>

- **4819588**（Description／適用）：There are several button press events that can be applied to the physical (hardkeys) and virtual (touchscreen) softkey presses. These events are described below. Refer to specific sections in this specification for the applied behavior related to these events.
- **4819589**（Subsystem Functional Requirement／不適用）：If the user touches a region of the screen that has no active screen object and then slides their finger onto an active screen object; regardless of whether the screen object has related 'Short Press', 'Long Press' or 'Press and Move' behavior, the HU/Front Passenger Display shall not play the softkey pressed tone Conf1 (See {CFTS019-723}) and shall determine that no 'Press' event has occurred (during the 'not pressed' to 'pressed' transition the user must press the screen within the boundary of the active screen object in order to determine that a Press event has occurred).
- **4819590**（Subsystem Functional Requirement／不適用）：Upon the initial transition to the pressed state, the HU/Front Passenger Display shall play the softkey pressed tone; either Conf1 for 'active' controls or Conf2 for 'inactive' controls (See {CFTS019-723}) and the HU/Front Passenger Display shall show the screen object in the 'pressed' state.
- **4819591**（Subsystem Functional Requirement／不適用）：The HU/Front Passenger Display shall determine which screen object (control) has been pressed and whether the object has 'Short Press', 'Long Press and Hold' or 'Press and Move' behavior.
- **4819593**（Description／不適用）：A short press event will be used by the HU/Front Passenger Display for hardkey or touch screen HMI controls that have behavior that is not related to how long the control is pressed or controls that can be moved ('dragged'). I.e. those that are not related to any Long Press or any Press and Move features.
- **4819594**（Subsystem Functional Requirement／不適用）：For 'active' controls, when a 'Short Press' event occurs, the HU shall immediately implement the action associated with the control (example actions are transitioning to some other state and displaying a corresponding screen) - See HMI Rule MCCA6. For 'inactive' controls no action is taken when the control is pressed (other than remaining on the same screen and, for touchscreen HUs, showing the softkey in the pressed state).
- **4819595**（Subsystem Functional Requirement／不適用）：For 'active' controls, when a 'Short Press' event occurs, the HU/Front Passenger Display shall immediately implement the action associated with the control (example actions are transitioning to some other state and displaying a corresponding screen). For 'inactive' controls no action is taken when the control is pressed (other than remaining on the same screen and, for touchscreen HUs/Front Passenger Display, showing the softkey in the pressed state).
- **4819596**（Subsystem Functional Requirement／不適用）：During the time that the HU senses that the control is pressed, all other control presses shall be ignored.
- **4819597**（Subsystem Functional Requirement／不適用）：When the HU determines the control is no longer being touched, the HU/Front Passenger Display shall prepare to act on the next control pressed event.
- **4819599**（Description／不適用）：A Long Press (or Press and Hold) event will be used by the HU/DCSD/CCDMF/Front Passenger Display for hardkey or touch screen HMI controls (ex. 'Line/Page Up/Down Accelerated List Scrolling', 'Storing Presets/Favorites', HVAC Temperature Up/Down, HVAC Blower Speed Up/Down, etc.) that have behavior that differs based on how long a control is pressed and the action to be taken for that screen control.
- **4819600**（Subsystem Functional Requirement／不適用）：The below requirements for long press event are only applicable for DCSD if $VC_VEH_LINE$ = [EJ]. These requirements shall be applied for the HVAC controls present in CFTS043 referring CFTS020 for long press event behavior.
- **4819601**（Subsystem Functional Requirement／不適用）：For some screen objects that have 'Long Press' control, the related action to take occurs after the initial time period has elapsed and then no further action is taken. For the 'Preset/Favorite Store' screen controls, the HU/DCSD/CCDMF/Front Passenger Display shall not act on the initial press event (leading edge) and shall wait to determine if the object has been pressed continuously for a period of <Tpress>. Once the time period of <Tpress> has elapsed, the HU/Front Passenger Display shall act on the press and hold event.
- **4819602**（Subsystem Functional Requirement／不適用）：For some screen objects that have 'Long Press' control, the related action to take occurs as soon as the button is pressed and again after the initial time period has elapsed and the action can be repeated if the control is continuously held. For the 'HVAC Temperature/Blower' screen controls, upon the initial transition to the pressed state, the HVAC shall act on the initial press event (leading edge) and shall wait to determine if the object has been pressed continuously for a period of <Tpress>. Once the time period of <Tpress> has elapsed, the HVAC shall act again and then shall repeat the action until the control is released, the user moves their finger to a region outside of the boundary of that screen object or until some other reason to stop is encountered (ex. Maximum Temperature reached and there is no wraparound behavior for this control).
- **4819603**（Subsystem Functional Requirement／不適用）：For screen objects that exhibit Long Press behavior, if the user is pressing the screen object and the <Tpress> time has not elapsed yet and the user moves their finger to a region outside of the boundary of that screen object, the HU/DCSD/CCDMF/Front Passenger Display shall cancel the Long Press timer (and shall not act upon this screen press event). In addition if the user moves to a region of the screen that has no active screen object and moves onto some other active screen object, the HU/DCSD/CCDMF/Front Passenger Display shall not act upon the other screen object (the user must release their finger from the screen before the HU/Front Passenger Display will act upon other screen objects).
- **4819604**（Subsystem Functional Requirement／不適用）：For controls that have a single action behavior, such as a Preset Storage behavior, when the <Tpress> timer has expired, the HU/DCSD/CCDMF/Front Passenger Display shall play the Confirmation Tone Conf3 (See {CFTS019-723} and HMI Rule RHP2), implement the action associated with the control (store the preset value) and theHU/DCSD/CCDMF/Front Passenger Display shall remain on the same screen but shall update the associated screen object as appropriate (ex. Radio Preset softkey label/background will change from 'HOLD to Set' to '89.7' and the softkey is shown in the 'currently selected' state).
- **4819605**（Subsystem Functional Requirement／不適用）：For screen objects that have a continuous action behavior, if the user slides off the screen object the HU/DCSD/CCDMF/Front Passenger Display shall treat this as if the user has released their finger from the screen - the user must release their finger from the screen and repress the screen object to start another Press and Hold event (if they slide back onto the object do not resume the action associated with the screen object).
- **4819606**（Subsystem Functional Requirement／不適用）：The value of <Tpress> shall be determined by the specific function that uses the long press event. Refer to the specific feature section for the <Tpress> timing.
- **4819607**（Subsystem Functional Requirement／不適用）：After the HU determines the initial press event applies to a screen control with long press behavior then; while that screen object continues to be pressed, it shall ignore all other screen press events.
- **4819608**（Subsystem Functional Requirement／不適用）：When the HU/DCSD/CCDMF/Front Passenger Display determines the control with long press behavior is no longer being touched, the HU/DCSD/CCDMF/Front Passenger Display shall prepare to act on the next control pressed event.
- **4819610**（Description／不適用）：A Press and Move event will be used by the HU/Front Passenger Display for all touch screen HMI controls (ex. 'Playtime Position Slider' for SAT Replay or Player sources that support playtime repositioning, 'List Slider', 'Audio Balance/Fade slider') that allow the customer to press and move their finger across the display.
- **4819611**（Subsystem Functional Requirement／不適用）：If the HU/Front Passenger Display determines that the screen object is a 'Press and Move' control, the HU/Front Passenger Display shall act on the initial press event (leading edge). The HU/Front Passenger Display shall react to the movement on the screen until the point where the screen is no longer being pressed.
- **4819612**（Subsystem Functional Requirement／不適用）：For screen objects that exhibit single direction Press and Move behavior (Vertical only or Horizontal only), if the user is pressing and moving the screen object in the adjustment direction and the user then moves their finger perpendicular to the adjustment direction and transitions to a region outside of the boundary of the screen object, the HU/Front Passenger Display shall terminate the Press and Move event (and shall not act any further upon this screen press event). The user must release their finger from the screen and repress the screen object to start another Press and Move event (if they slide back onto the object do not resume the action associated with the screen object).
- **4819613**（Subsystem Functional Requirement／不適用）：After the HU determines the initial press event applies to a screen control with press and move behavior then; while that screen object continues to be pressed, it shall ignore all other screen press events.
- **4819614**（Subsystem Functional Requirement／不適用）：When the HU/Front Passenger Display determines the control with press and move behavior is no longer being touched, the HU/Front Passenger Display shall prepare to act on the next control pressed event.

</details>

---

## §4 實測值對照（下放包 03 §5）

全部為本次實測，不沿用他人陳述。量測條件見 §0。

| # | 項 | 實測 |
|---|---|---|
| (a) | v2 之適用物件總數 | **254**（v1 為 28）|
| (b) | `4819617` 之 v2 判定 | **適用**（§1.8.1.4；ECU **軸缺**／Radio VP4R84, VP484, R1M, R1H, R1L, VP384, R1L-R／EE Atlantis High, PowerNet）|
| (c) | 1.5 章節下 Artifact Type = Subsystem Functional Requirement 之物件 | 114 個，其中不適用 **114** 個 → **仍 100% 不適用** |
| (d) | `1.8.1.1.1 {4819556}` 群之適用數 | **6** / 8 |
| (e) | `1.8.1.1.3 {4819570}` 群之適用數 | **6** / 6 |
| (f) | `1.8.1.3 {4819587}` 群 | v1：24 中 23 不適用；v2：24 中 **23 不適用、1 適用** |

### §4.1 既有 TC 之錨點複驗

CFTS022 走 v2(a)（＝v1 之三軸交集，判準未變），故 b01／b02 所錨之 CFTS022 物件不受本次重判影響。CFTS020 側之錨點逐一複驗：

| 錨 | 批 | v1 | v2 | 結論 |
|---|---|---|---|---|
| CFTS020-4819617 | b02 | WARN-軸缺 | **適用** | 錨仍成立（R-ICS2 v2(e) 相符），I1／I2 無需回收 |
| CFTS020-4819583 | b01（作業 D 將引為 Pre-Condition）| WARN-軸缺 | **適用** | 錨仍成立 |

### §4.2 與 R-ICS2 v2(c) 所述 1.5 實例之對照（輔證，非判準）

- 1.5 章節下物件 **132** 個；`EE` 恰為 `['PowerNet']` 者 **130** 個（與 v2(c) 所述「130 為 PowerNet」相符）
- Artifact Type 分佈：{'Description': 18, 'Subsystem Functional Requirement': 114}（v2(c) 所述「餘二皆 Description 型章節引言」指的是 EE 非 PowerNet 之二個，非指 1.5 只有二個 Description）
- 該二個為 `4819364`（Description，`[ECU:FPDM]`、EE `PowerNet, Atlantis High` → v2 **不適用**，即 v2(b)(ii) 所舉之實例）與 `4819365`（Description，Radio `R1L-R, R1L`、EE `All` → v2 **適用**）
- 故 1.5 下唯一 v2 適用者為 `4819365`，其 Artifact Type 為 Description，**非需求物件**；需求物件（Subsystem Functional Requirement）114 個仍 100% 不適用，與 v2(c) 相符

