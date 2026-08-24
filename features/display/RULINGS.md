# RULINGS — Display (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Display 之裁決權威；
跨 feature 條文承接時註明來源包。

抄錄方式：以 `re` 自下放包之 fenced 區塊機器抽取後原樣寫入，未經人工
轉錄。逐條 SHA256 核對表見文末。

---

## 來源：下放包 01

```
R-DM1（feature 身分與 test_group）
`feature` 為 `Display`，slug 為 `display`，`test_group` 為 `Display`。
（Pei 2026-08-24 裁定「就用 Display」。）

037 之模組名 `Display Management` 與 CFTS_020 之文件名
`ICS and DCSD` 皆不進入 `test_group`、不進入任何 TC 欄位；二者僅得
記於 `feature.yaml` 之路徑註解與 `framework.md` 之說明文字。

裁決前綴為 `R-DM`、異常前綴為 `A-DM`、資料請求前綴為 `DR-DM`，
不與任何既有 feature 共用序號。
```

## 來源：下放包 01

```
R-DM2（037 之來源授權）
037 A03 SWRA（`Display_Management_FMWIFSM037A03_STLA_Report_SWRA.xlsx`）
於 2026-08-24 在 Pei 之磁碟上未能定位；分析層已查
`9_ASPICE/`（無 SWE.1 目錄）、`10_Reviewing/00_TestCase/`、
`6_SW_Test/`、`7_Delivery/`、`0_Project_Management/`、
`Work_Projects/` 下各專案，皆無。

Pei 2026-08-24 授權：以 Claude Project 之附件為該檔之唯一來源，
由 Pei 手動置入 `_intake/Display/`。

執行層拘束二項：
(a) 不得自行向上游索取該檔，亦不得以任何其他檔案代替；
(b) 該檔一經置入即記其 SHA256 與 mtime 入素材台帳；台帳建立後，
    後續各輪之引用一律對台帳所記之 repo 內複本實測，不回頭引用
    本包之任何數字（canon §5a：不以自身先前輸出為來源）。
```

## 來源：下放包 01

```
R-DM3（多套 id 命名之處置 —— 登記，不解）
本 feature 之追溯鏈在文件間出現多套互不相同之 id 命名：

  037 `SWE1 Requirements` 分頁   → `SWE-DM-001` … `SWE-DM-008`
  037 `SWE1 Requirements` 分頁   → `SYS-DISP-001` …（Source Requirement ID）
  037 `SYS2 Traceability` 分頁   → `SWE1-DM-001` …（同一物件，另一寫法）
  037 `SYS2 Traceability` 分頁   → `SYS-RA-DISP-001` …（指向 SYS2）
  SYS2 `Basic Report` 分頁       → `SYS-RA-DM-001` … `SYS-RA-DM-087`
                                    及 `SYS2-RA-088` 以後

`SYS-RA-DISP-*` 與 `SYS-DISP-*` 兩種寫法在 SYS2 released 版中之出現次數
為 **0**（量測條件見 §三 3.3）。

本輪之處置為**登記而非解決**：執行層以 `A-DM{n}` 逐項登記，附證據與
提案處置，不得自行推定其對應關係（例如推定
`SYS-RA-DISP-001` ↔ `SYS-RA-DM-001`）。任何跨命名之對應皆屬
canon §0 逸出觸發第 1 條「規格查找未解」，須停並回報。

`feature.yaml` 之 `req_id` 欄最終寫何種形態，屬 Tier 2，於 Phase 2 裁定；
本輪僅記現況。
```

## 來源：下放包 01

```
R-DM4（037 之 Excluded 分頁其 id 語意已查明）
037 `Excluded NRLs (HW-only)` 分頁之 `NRL ID` 欄，其 8 個值
（`PSCFTS020-1-45-1` 等）**不是 SYS2 之 NRL ID**（SYS2 之 NRL ID
形態為 `NRL-52839`），而是 SYS2 `SYS2 Melco ID` 欄之值。

分析層已實測：該 8 值在 SYS2 Melco ID 欄之 99 個 token 中 8/8 命中
（量測條件見 §三 3.3）。

拘束：執行層引用該分頁時一律稱其為 Melco ID，不得以「NRL ID」之欄名
為據去 SYS2 之 NRL 欄查找 —— 那會 8/8 查無，並被誤讀為追溯斷鏈。
本條為已解之項，不再登記為 anomaly。
```

## 來源：下放包 01

```
R-DM5（intake.py 之 sniffer 對本 037 之已知偏差）
`scripts/intake.py` 之 `SHEET_SIGNATURES` 以
`"Analysis Report" in names` 判定 `swra_report`。本 037 之分頁為
`SWE1 Requirements` / `SYS2 Traceability` / `Excluded NRLs (HW-only)`，
無 `Analysis Report`，故必然被分類為 `spec_xlsx`。

執行層拘束三項：
(a) 照跑 `intake.py`，如實回報其實際分類結果，不得預先改腳本使其命中；
(b) 分類偏差之修法（新增分頁簽章、或以 feature.yaml 人工指定
    `a03_report`）屬 Tier 2，本輪只提案不實作 —— 改判準會改結論，
    不屬 AUTO 之技術選擇；
(c) `intake.py` 之 need-list 推導對本檔亦不適用：其
    `Source Requirement ID` 欄之內容為 `SYS-DISP-nnn` 形態之
    Polarion id，非 `name_{section}` 形態之文件引用。腳本應如實
    報告「不可推導」而非產出空清單；若其產出空清單而未說明，
    以 `A-DM{n}` 登記。
```

## 來源：下放包 01

```
R-DM6（素材台帳之到齊定義）
素材之「到齊」定義為：清單每項附其檔案系統絕對路徑與 SHA256，且
`shasum -c` 對得上。「檔名相符」「大小相同」皆不構成到齊。

搬入 `features/display/inputs/` 者為複本，來源目錄一律唯讀，
搬入前後各記 SHA256 與 mtime 並登入台帳。

四份以外之檔案不得搬入；`_intake/Display/` 若另有本包未列之檔，
登記後停手詢問。
```

## 來源：下放包 01

```
R-DM7（覆蓋落差之量測義務 —— 8 vs 80）
037 之 leaf 全集為 8，而 SYS2 released 版之 `Functional Requirement`
列數為 80（`SYS-RA-DM-*` 區段 44 + `SYS2-RA-*` 區段 36；大小寫變體
1 列已計入，見 §三 3.3）。

本落差不得以「037 為權威、故 8 即全集」一句帶過。執行層須於本輪
產出可審之對照：以 SYS2 之 `Functional Requirement` 全集為母體，
逐列標記其是否可對應到 8 個 SWE-DM leaf 之一，對應依據逐列寫明
（Melco ID、Description 文字、或無）。無法對應者列出其列號與
`SYS2 Sys-RA-Feature-ID`。

該對照之用途為**揭露**，不是重新界定範圍。範圍之裁定屬 Tier 2，
於 Phase 2 依此對照為之。此處之判準為 canon §5a：引用任何單一來源
為「權威」前，先確認其涵蓋範圍是否等同其類別 —— 037 只有 8 筆，
不等於 Display 之軟體需求只有 8 筆。
```

## 來源：下放包 01

```
R-DM8（缺值不得自填）
037 之 8 筆需求描述皆為 SWE 層抽象語句，其中至少四處之具體值
在 037 內不存在：

  SWE-DM-003  Splash / sleep 之時長門檻
  SWE-DM-004  thermal warning threshold 之門檻值與單位
  SWE-DM-005  thermal protection 之 critical 判準與回復條件
  SWE-DM-006  popup priority arbitration 之優先序規則與 timeout

上述各項一律先回 CFTS_020 本文與 SYS3 SYSAD 查；查得者記其章節，
查不得者以 `DR-DM{n}` 登記，不得以領域常識、其他 feature 之值、
或 037 之 `Verification Criteria` 欄文字回填（canon §8.4.1）。

`Verification Criteria` / `Verification Method` 二欄之地位為
**參考輸入而非權威**：其為上游之推導產物，以其為據等同以推導物
取代來源。（形態同 Vehicle Setting R-VF13，惟本 feature 尚未取得
該條之五項限制之對應裁定，故本輪一律不用。）
```

## 來源：下放包 02

```
R-DM2（廢止並以 R-DM2′ 取代）
~~037 A03 SWRA 於 2026-08-24 在 Pei 之磁碟上未能定位……以 Claude
Project 之附件為該檔之唯一來源，由 Pei 手動置入 `_intake/Display/`。~~

廢止理由（2026-08-24，下放包 02）：前提「磁碟上未能定位」為誤。
分析層以附件之正規化檔名 `FMWIFSM037A03`（無連字號）為搜尋字串，
而磁碟實際檔名為 `FM-WI-FSM-037-A03`（帶連字號），致搜尋落空；
且查 `10_Reviewing/00_TestCase/` 時僅列至 `ASW-R2` 一層即轉往他處，
未下鑽至 `ASW-R2/Display/`。
```

## 來源：下放包 02

```
R-DM2′（037 之來源）
037 A03 SWRA 之來源為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/
Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`，
其 SHA256 須為
`ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050`。

該值與 Pei 授權之 Claude Project 附件為位元級同一（分析層 2026-08-24
以 `sha256sum` 對附件複本實測所得）。故本條非「以他檔代替附件」，
而是同一內容之磁碟路徑。

拘束：搬入前以完整 64 碼比對，不符即停並回報，不得以「首尾相符」
或「size 相符」放行。
```

## 來源：下放包 02

```
R-DM9（素材來源目錄）
本 feature 之素材來源目錄為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/`
（唯讀，不得寫入），四份素材皆取自該目錄。

下放包 01 §3.4 所列之三條路徑（`9_ASPICE/SYS.2 …`、
`9_ASPICE/SYS.3 …`、`1_Customer_Requirement/… 26PI1.5/SubSystem/Cabin/`）
**作廢，不得再作為來源**；該三處之同名檔僅得作為比對對象，
其與交付夾版之 SHA256 比對結果登入台帳。

依據：`power_moding` 之 `ASW-R2/Disclaimer screen/` 為同型前例 ——
FROP 交付夾內含該 feature 之完整素材組，為專案之組織慣例。
```

## 來源：下放包 02

```
R-DM10（A 版本之處置）
`/Users/peihe/Work_Projects/R1L_RTM_V3/data/9_ASPICE/
04_SWE.1 Software Requirements Analysis/Display Management/
Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
（SHA256 `100f75b7…a5f374f0`，44697 bytes）與 R-DM2′ 之標的
**內容同一、檔案相異**。

分析層 2026-08-24 之逐儲存格比對（三分頁、`data_only=True`、
非唯讀模式、取兩者 max_row × max_column 之聯集、越界取 None）
差異格數為 0。

處置：不搬入、不引用、不登記為版本歧異。其存在僅記於台帳之
「同內容他處副本」欄。若日後任一方內容變動致比對不再為 0，
以 `A-DM{n}` 登記並停手。

同目錄之 `SWE1_DISPLAY_MANAGEMENT_INIT_ONLY_OBSELETE.xlsx`
（檔名自書 OBSOLETE）不搬入、不開啟。
```

## 來源：下放包 02

```
R-DM11（檔名正規化之通則）
Claude Project 附件之檔名經上傳正規化（連字號、空格、`&` 等字元
被移除或替換），與磁碟原始檔名不同。分析層引用附件檔名於磁碟搜尋時，
**須先以其去除分隔符後之骨幹字串為鍵**，或改以目錄下鑽窮舉，
不得以附件檔名逐字搜尋後即斷定「磁碟上無此檔」。

本條為 R-DM2 致誤之防再犯條文。適用範圍為全案，非僅本 feature。
```

---

## 抄錄核對表

| # | 條號 | 來源包 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 1 | R-DM1 | 01 | 337 | `f8181c4bd16d0ca9` | 是 |
| 2 | R-DM2 | 01 | 488 | `231830d8d5cda432` | 是 |
| 3 | R-DM3 | 01 | 739 | `dc68c2bbe20556b5` | 是 |
| 4 | R-DM4 | 01 | 367 | `25f632b137ac858d` | 是 |
| 5 | R-DM5 | 01 | 607 | `19bfd2399bb2aad2` | 是 |
| 6 | R-DM6 | 01 | 216 | `1d8eb69193c73a8b` | 是 |
| 7 | R-DM7 | 01 | 498 | `b967b09652669c91` | 是 |
| 8 | R-DM8 | 01 | 559 | `e6ff38e7f7472ac1` | 是 |
| 9 | R-DM2 | 02 | 329 | `eecfc177bae79ee9` | 是 |
| 10 | R-DM2′ | 02 | 406 | `c4f6853689107fd1` | 是 |
| 11 | R-DM9 | 02 | 397 | `ac0b6373fe6b919d` | 是 |
| 12 | R-DM10 | 02 | 519 | `4a0756e807a1d6ef` | 是 |
| 13 | R-DM11 | 02 | 193 | `381220990cd1e12e` | 是 |

核對方法：抄錄後自 `RULINGS.md` 反向抽取各 fenced 區塊，與下放包原檔
之對應區塊逐字元 `==` 比對並比對 SHA256；13 條全數相符。
