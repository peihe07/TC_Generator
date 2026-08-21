# RD-1 Questions — Time Management (CFTS015)

狀態：DRAFT。送出日期：____。送出屬 Pei。

## Q-TM1 — 037 之文件身分（阻塞交付欄位）

本 feature 收到之 SWE.1 分析報告檔名為 `SWE1_Secure_Date&Time.xlsx`，
封面 Project Name `New R1L`、日期 2020/09/05。

交付路徑 `ASW-R2/` 下其他三個 feature 之 037 命名形態一致：

| feature | 037 檔名 |
|---|---|
| Home | `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx` |
| AppDrawer | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx` |
| User Profiles | `FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` |

`ASW-R2/Time Management/` 下無任何符合該形態之檔案。

**問**：Time Management 是否另有依 FM-WI-FSM-037-A03 命名之正式報告？
或 `SWE1_Secure_Date&Time.xlsx` 即是而命名未依慣例？

**影響**：036 工作簿之範圍 Scope 欄（D5）值即為所依據 037 之文件識別，
在本問答覆前無值可填，交付件該欄將留空。

## Q-TM2 — 兩筆需求之來源物件不在 CFTS015 基線內

SYS2 匯出之下列兩筆，其 `Source Requirement items` 所指物件於 CFTS015
（R1LR Atl-H 25PI3.5 SR26, 20250909-1851）全檔零命中：

| SYS-RA id | 來源物件 id | 需求要旨（節錄自 SYS2） |
|---|---|---|
| `SYS-RA-TIME&DATE-221` | `6151328` | `$GPS_Presence$ = [Absent]` 時之內部時鐘精度 |
| `SYS-RA-TIME&DATE-224` | `6151331` | `$GPS_Presence$ = [Present]` 時之個人化設定 |

CFTS015 全篇物件 id 皆為 `481xxxx` 區段；`615\d{4}` 形態零命中。
兩者分別被 `SWE-RA-TIME&DATE-005`（Internal Clock Accuracy）與
`SWE-RA-TIME&DATE-002`（GPS Sync Enable/Disable Logic）引用。

**問**：此二物件源自 CFTS015 之較新版本，或源自另一份 CFTS？
應以哪一份文件為該二筆之 spec 依據？

**影響**：該二 leaf 之 `specification_reference` 於此二筆上無章節可寫。
依 §8.4.1 不得以鄰近章節填充，交付件將於 Remarks 標示缺口。

## Q-TM3 — 48 筆 SYS2 功能需求無對應 SWE leaf（分配政策）

SYS2 之 Functional Requirement 共 126 筆；037 之 22 片 leaf 合計引用
78 筆，**48 筆無任何 leaf 對應**（覆蓋率 61.9%）。

引用之 78 筆全數為 Functional Requirement，無懸空引用（037 未引用任何
不存在之 id）。48 筆清單可另附。

同時觀察到：037 可達之 21 個 CFTS 章節全落 `1.3.1.*`（PNet/CUSW/AtlHi
共通）與 `1.5.2.*`（LTM），**`1.5.3.*`（ETM）零命中**。兩者是否同源
尚未查證。

**問**：該 48 筆是否分配予其他 feature 之 037，或屬本 feature 之
分配缺口？若為後者，037 是否將補件？

**影響**：TC 生成單位為 037 之 22 片 leaf；48 筆無 leaf 即無工作簿列可
寫。依 §8.2 不得由 TC 作者自行創設 leaf 或分解 SYS2 條文湊覆蓋，
故此缺口以宣告處理，不以生成填補。

## N-TM1 — spec_reference 之參照體系（說明，非提問）

CFTS015 內存在兩套並存且可互相對應之物件編號：

  短號家族：CFTS015-732 … CFTS015-1639（26 個相異值，僅見於修訂註記）
  7 位家族：4813898 … 4814253（270 個相異值，全篇正文與章節標題）

對應實例：物件 4814185 之內文含 `CFTSMV015_CIP_R1_O922_118_inline.rtf`，
其次一物件 4814186 稱 `CFTS015-922` —— 短號 922 即 7 位 4814185。

本工作簿之 specification_reference 採 `CFTS015-{7 位物件 id}`，
id 取自 SYS2 匯出之 `Source Requirement items` 欄。
`CFTS015-<7 位>` 之寫法於 CFTS015 全文出現 0 次，惟依 canon §10.7(a)
（`CFTS 母文件 → CFTS{nnn}-{ObjectID}，ObjectID 為該物件之 Polarion
7 位號碼`）採 Polarion SourceID 形式，且該節明文禁止短號作為錨。

**說明（非提問）**：依 canon §10.7(a)，本工作簿採 `CFTS015-{Polarion
7 位 ObjectID}`，短號需求 ID 不作為錨、僅於 reasoning 引用。
此處記載供上游知悉，不需回覆。

**附帶提示**：兩套編號字面不互通 —— 審閱者見工作簿之 `CFTS015-4814185`
而於文件搜尋同字串將零命中，須改搜 `4814185`。
