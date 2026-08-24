# 下放包 02 —— Display 素材來源更正，續跑 01

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`display`
- 對應上繳：`features/display/docs/upstream/02_intake_recon.md`
- 前一包：`01_intake_recon.md`（步驟 1 停手，停手正確）

---

## 一、上繳包之核可

**核可。停手正確，且發現了分析層之錯誤。**

執行層之三項判斷逐項成立：

1. §五第 8 條之觸發正確 —— `_intake/Display/` 不存在，037 未就位。
2. **拒絕以磁碟檔 B 代替附件，正確。** R-DM2(a) 明文禁止代替；縱使
   跡象高度相符（分頁名一致、`max_row = 226` 逐字相符），由執行層
   逕行認定「B 即該檔」仍屬推定。此處之克制是對的。
3. 不建骨架以免誤觸 §五第 7 條，正確。

**分析層之錯誤，由分析層承擔：** R-DM2 之前提「磁碟上未能定位」為誤。
致誤原因是我以 Project 附件之檔名 `FMWIFSM037A03`（無連字號）為搜尋
字串，而磁碟上之實際檔名為 `FM-WI-FSM-037-A03`（帶連字號）。附件之
檔名是上傳時被正規化過的，我把正規化後的檔名當成原始檔名去找，
於是六個目錄全部落空。

更嚴重的是：我當時查了 `10_Reviewing/00_TestCase/`，卻只列到
`ASW-R2` 這一層就轉往他處，沒有下鑽。而 `ASW-R2/Display/` 這個目錄裡
**四份素材全部齊備**（見 §三）。我在 01 §3.4 給出的三條路徑是我從
`9_ASPICE/` 與 `1_Customer_Requirement/` 東拼西湊來的，而交付夾裡本來
就有一份現成的完整素材組 —— 這與 `power_moding` 之
`ASW-R2/Disclaimer screen/` 是完全相同的組織慣例，我應該先想到。

---

## 二、A/B 兩份 037 之身分 —— 已以實測解決，非推定

執行層所報之 A、B 兩份，分析層已完成兩項量測：

### 2.1 B 與 Project 附件為**同一份**（位元級）

| 標的 | SHA256 | size |
|---|---|---|
| Project 附件 | `ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050` | 46993 |
| 磁碟 B | `ab3198e8…f3185050`（執行層所報） | 46993 |

量測條件：分析層對 `/mnt` 沙箱之附件複本執行 `sha256sum`；執行層對
磁碟 B 執行其雜湊工具。兩者之首尾八碼與長度皆相符。

**故「以 B 為來源」不是代替，是同一組位元的另一個路徑。** R-DM2 授權
之標的內容與 B 之內容為同一物，此為量測結果而非推定 —— 執行層原先
不能自行做這個判斷（手上沒有附件可比），分析層有附件，可以做。

> 惟：首尾八碼相符不等於全 64 碼相符。執行層於 §四步驟 1 須以
> **完整 64 碼**與本節之值逐字比對，不符即停。

### 2.2 A 與 B 之差異為**格式層，非內容層**

分析層將 A 複製至沙箱後，與附件逐儲存格比對：

| 項 | 結果 |
|---|---|
| SHA256 | 相異（A = `100f75b7110e3c83330fd6401be00aa0da859af4bcc12fc8665b72fda5f374f0`） |
| size | A 44697 / B 46993 |
| 分頁名 | 三分頁完全一致 |
| 非唯讀模式之非空列數 | 三分頁皆一致（14 / 9 / 9） |
| **全儲存格值逐格比對（三分頁、涵蓋兩者之 max_row × max_column 聯集）** | **差異 0 格** |

量測條件：`openpyxl`，`data_only=True`，非唯讀模式；對每分頁取
`max(a.max_row, b.max_row) × max(a.max_column, b.max_column)` 之全域，
越界者取 `None`，逐格 `!=` 比對。

> 執行層先前所報「A 之 max_row = 228」與此處之 226 不符。差異來源
> 應為唯讀模式與非唯讀模式之 `max_row` 計算不同（唯讀模式讀 sheet
> dimension 之宣告值，非唯讀模式重算）。**此為量測條件差異，不是
> 資料差異** —— 逐格比對已證兩份內容同一。此點請於上繳包確認。

**結論：A 與 B 之需求內容無任何差異。** 版本歧異之疑慮解除；兩者是
同一份 037 的兩次存檔，差別在格式／中繼資料。

---

## 三、素材來源目錄之更正 —— 交付夾即單一來源

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/
```

該目錄實測含**四份**（分析層 2026-08-24 以 `list_directory` 確認）：

| 檔名 |
|---|
| `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` |
| `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` |
| `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` |
| `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` |

**01 §3.4 之三條路徑作廢，改以本目錄為唯一來源目錄。**

分析層已就 SYS2 一份比對兩處之 size 與 mtime：交付夾版與
`9_ASPICE/SYS.2 …/CFTS_020 ICS and DCSD/` 版皆為 193683 bytes、
mtime 皆為 2026-08-16T06:30:00。**size 與 mtime 相符不構成內容同一之
證明**，執行層須以 SHA256 實測，並於上繳包報告四份在兩處（有兩處者）
之雜湊比對結果。

> 交付夾內**無 036 工作簿** —— 此為 Q1（`workbook_state`）之正面證據，
> 但仍須依 01 §四步驟 10 實測，不得以本節代替判定。

---

## 四、裁決條文更正與新增（抄入 `RULINGS.md`）

> R-DM2 為分析層自訂條文（非 Pei 直接口述之條文），其前提經實測為誤，
> 由分析層更正並全文揭露。Pei 之原始授權（2026-08-24「授權 就用Display」）
> 之內容為「以該份 037 之內容為準」，本次更正未改動該授權之標的，
> 僅更正該內容之取得路徑 —— 且已由 §2.1 之雜湊證明兩者為同一組位元。

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

```
R-DM11（檔名正規化之通則）
Claude Project 附件之檔名經上傳正規化（連字號、空格、`&` 等字元
被移除或替換），與磁碟原始檔名不同。分析層引用附件檔名於磁碟搜尋時，
**須先以其去除分隔符後之骨幹字串為鍵**，或改以目錄下鑽窮舉，
不得以附件檔名逐字搜尋後即斷定「磁碟上無此檔」。

本條為 R-DM2 致誤之防再犯條文。適用範圍為全案，非僅本 feature。
```

---

## 五、續跑指示

**回到下放包 01 §四步驟 1，依下列更正後續跑至步驟 14。**

步驟 1 之更正版：

1. **建 `_intake/Display/`，自 R-DM9 之來源目錄複製四份**（不再等 Pei
   手動置入 —— R-DM2′ 已使該前提消失）。逐檔記來源絕對路徑、目的路徑、
   搬入前後 SHA256、size、mtime，`shasum -c` 對帳。
   037 之雜湊須逐字等於 R-DM2′ 所載之 64 碼，不符即停。
1b. **兩處同名檔之比對**：SYS2、SYS3、CFTS 三份在
    `9_ASPICE/` 與 `1_Customer_Requirement/` 之對應檔，各計 SHA256
    並與交付夾版比對，結果入台帳（R-DM9）。相異者登
    `A-DM{n}` 並停手詢問 —— 相異表示交付夾版與 ASPICE 歸檔版不同步，
    屬須裁事項。

步驟 2–14 依 01 原文，**惟下列兩點併同更正**：

- 01 §3.2 / §3.3 之實測數字仍有效（其標的為附件，已證與 R-DM2′ 之
  標的位元同一），續作對照向使用。
- 01 §五第 8 條之觸發條件改為：`_intake/Display/` 之檔案清單與
  R-DM9 來源目錄之四份不符 → 登記後停。

**A-DM 之首批登記**（骨架建立後，即 01 §四步驟 3 完成後立即為之）：

| 編號 | 內容 |
|---|---|
| A-DM1 | 037 `SWE1 Requirements` 與 `SYS2 Traceability` 二分頁對同一物件使用 `SWE-DM-nnn` 與 `SWE1-DM-nnn` 兩種寫法（01 R-DM3） |
| A-DM2 | 037 所引之 `SYS-RA-DISP-*` / `SYS-DISP-*` 在 SYS2 released 版中 0 命中（01 R-DM3） |
| A-DM3 | 037 `SYS2 Traceability` 之 `Source NRL ID(s)` 欄 8/8 為空，而 `Excluded NRLs` 分頁反有 id（01 §3.2） |
| A-DM4 | SYS2 `Category` 欄有大小寫變體共 8 列，逐字比對之 gate 會少算（01 §3.3） |

> 執行層先前所報「尚未登記 A-DM{n}，待骨架建立後首批登記」之安排，
> 分析層採納，並以上表指定其內容。**A/B 版本歧異不列入** —— 已由
> §2.2 解決（R-DM10）。

---

## 六、上繳包要求（`docs/upstream/02_intake_recon.md`）

沿用 01 §七之十三節，並增下列三節：

14. R-DM2′ 之 64 碼雜湊逐字比對結果（實際值 vs 條文值）
15. §五步驟 1b 之兩處同名檔比對表
16. §2.2 之「A 之 max_row = 228 vs 226」之量測條件確認 —— 說明該差異
    是否確為唯讀／非唯讀之計算差異

---

## 七、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 是否已以可貼區塊出現於 §四 |
|---|---|---|
| R-DM2 | 廢止（附前提致誤之全文揭露） | 是 |
| R-DM2′ | 037 之來源路徑與 64 碼雜湊 | 是 |
| R-DM9 | 素材來源目錄 = `ASW-R2/Display/`，01 §3.4 三路徑作廢 | 是 |
| R-DM10 | A 版本內容同一（0 差異格），不搬入不登歧異 | 是 |
| R-DM11 | 附件檔名正規化之搜尋通則（全案適用） | 是 |

五條皆為獨立單一事項。
