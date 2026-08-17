# ANOMALIES — FW036 Power HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-PWnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

來源：下放包 01 §F（A-PW01–A-PW07）、02 §F（A-PW07 撤回、A-PW08 新增；
執行層新登 A-PW09–A-PW11）、03 §F（A-PW12、A-PW13；執行層新登 A-PW14–A-PW16）。
撤回列不刪、不重編號。

---

| ID | 內容 | 證據 | 狀態 |
|---|---|---|---|
| A-PW01 | `SWE-PM-089` 之 `Source Requirement ID` = `SWE1-PM-ANT-008`，為 037 自身另一套命名空間，非上游來源 | 全表 18 欄 × r8–r145 掃描，該 token 不存於任一 SYS2 匯出 | PENDING（DR-PW1；03 包 G3 再度復現：114/115，唯一失敗者即此 leaf） |
| A-PW02 | `Sys-RA-PM-0334` 之 source id `4942087` 於兩份 CFTS 本文皆不存在；`4942xxx` 為 CFTS010 號段但低於其首個 id `4942192` | SYS2 CFTS009 匯出 r325 | PENDING（DR-PW3）。**03 包實測全部證實**：`4942087` 為 439 個 token 中**唯一**既非需求錨點亦非章節錨點者（G6b）；CFTS010 首個 id 實測為 `4942192`（§1 Power Down），`4942087 < 4942192` 成立 |
| A-PW03 | 037 `Excluded NRLs (HW-only)` 26 筆全落 NRL-928xx–930xx（CFTS009 域），**不含** `NRL-99476`（`Sys-RA-PD_013`，HW） | 排除台帳涵蓋範圍不等於其名稱所宣稱 | **證據成立，且應加強**（03 包複驗）。26 筆號段實測 92882–93063，全落區間內，0 例外；`NRL-99476` 確不在其中，而該 NRL 於 SYS2 CFTS010 之 `SW/HW/System` 欄實測為 `HW`。**加強**：分頁名為 "(HW-only)" 但 26 筆之分類實測為 `HW` 18 / `Information` 4 / `Out of Scope` 2 / `Heading` 1 / 空白 1 —— 名稱在**分類**上亦不實，非僅涵蓋範圍 |
| A-PW04 | 037 `SYS2 Traceability` 33 列不含任何 `NRL-994xx` 或 `Sys-RA-PD` | CFTS010 全域未進追溯分頁 | **逐字成立**（03 包複驗）。33 列實測 `NRL-994xx` 出現 0 次、`Sys-RA-PD` 出現 0 次、`Sys-RA-PM-` 出現 76 次 |
| A-PW05 | ~~037 內部 id 命名空間不一致：`SWE1 Requirements` 用 `SWE-PM-001..115`，`SYS2 Traceability` 用 `SWE1-PM-TLM-001..033` / `-ANT-`~~ | 兩套互不對應 | **描述須修正**（03 包複驗）。`SYS2 Traceability` c1 實測為 `SWE1-PM-TLM-001` … `SWE1-PM-TLM-033`，**33 列全為 TLM 前綴，無任何 `-ANT-`**；`SWE1-PM-ANT-008` 於該分頁任一儲存格皆不存在（它只出現在 `SWE1 Requirements` 分頁 `SWE-PM-089` 之 `Source Requirement ID` 欄）。**核心主張仍成立**：該分頁 `SWE-PM-` 出現 0 次，兩套 id 完全不重疊。修正後描述：「`SWE1 Requirements` 用 `SWE-PM-001..115`，`SYS2 Traceability` 用 `SWE1-PM-TLM-001..033`，兩套互不對應；另有第三組 `SWE1-PM-ANT-`，僅見於 `SWE-PM-089` 之來源欄」 |
| A-PW06 | 037 `Sub Categorization` 詞彙漂移：`HMI` 36 / `Service\nHMI` 35 / `Service` 27 / `HMI Service` 16 / `HMI/Service` 1 | 三種寫法指涉同一組合，不可作分批判準 | PENDING（03 包未複驗，見上繳包 §七第 4 項） |
| A-PW07 | ~~三份 `.docx` 實為 Markdown 純文字，副檔名與內容不符~~ | ~~magic bytes 實測（R-P3）~~ | **撤回（R-P12）**。原始檔實測：CFTS009 `.docx` = OOXML、CFTS010 `.doc` = OLE2、SYS3 `.docx` = OOXML。副檔名與內容**實為相符** |
| A-PW08 | 01 下放包 §B 之「真實格式」欄與 `bytes` 欄與原始檔不符，源於以衍生物冒充原始檔。CFTS010 之原始檔副檔名為 `.doc` 非 `.docx` | 01 包記 412,654 / 81,064 / 51,264 bytes「純文字」；原始檔實測 154,588 / 245,248 / 3,474,091。三個宣稱之 SHA256 於整個家目錄內無符合檔案 | **已處置**（R-P9–R-P13） |
| A-PW09 | 01/02 包 §C 之 SYS2 CFTS009 讀取座標 `r2–r338` 漏一列：實際延伸至 **r339** | r339 = `NRL-142587`，`Type` 欄實測 `Heading`，`Sys-RA-Feature-ID` 欄為空，`Source Requirement items` 欄為空 | **已處置（R-P18）**。座標改 r2–r339；G6a = 337/338 |
| A-PW10 | §E Layer 3 未涵蓋 CFTS009 **§1.6.2.1.17**（1 leaf：`SWE-PM-057`）；§E 於 Power State 列出之 **§1.8.1** 主章節落點為 0 | 02 包 §E 重算 | §1.8.1 部分依 **R-P16 已刪除，惟前提須複核**（見 A-PW14）；§1.6.2.1.17 部分 **live**，B2 素材已備妥（§1.6.2.1.17 = `Proxi Parameters management`），待 Q1 裁定 |
| A-PW11 | CFTS009 與 CFTS010 之標題以不同機制表達粗體（`pStyle 1–8` vs run 層），單一序列化無法同時滿足 §C rule 1 與 rule 2 | 全粗體序列化：009 得 172/904、010 得 0/148；未標記序列化：009 得 196/0、010 得 92/0 | **已處置（R-P17）**，保留為文字層定義之理據 |
| A-PW12 | 01/02 包之 G6 期望值「336/337」將錨點鏈第一段（欄內 token 可抽取）與第三段（token 可解析至章節）混為一談 | 03 包實測：G6a（第一段）= 337/338；G6b（第三段，列層）= **336/337**，唯一失敗者 `Sys-RA-PM-0334` —— 舊值精確落在第三段上 | **已處置（R-P18）**。舊 G6 作廢，拆為 G6a / G6b |
| A-PW13 | §E 之 leaf 分布缺乏可重現之產生程序；主章節規則未書面化即產出數字 | 02 包重算得 62/24/16/8/3 + 未歸類 1，與 §E 之 64/24/16/7/3 不符 | **已處置（R-P15）**，惟 §E 定版本身仍待 Q1 裁定 |
| A-PW14 | **R-P16 刪除 §1.8.1 之前提「實測 0 leaf 落點」僅在 02 包主章節規則下成立** | `SWE-PM-057` 之章節集合實測含 CFTS009 **§1.8.1.1.1（ID 1 Description）**，出現 3 次，與 §1.6.2.1.17（3 次）、§1.6.3.1.1（3 次）同票。即 §1.8.1 有 leaf 觸及，只是在該規則下未勝出 | **新增（執行層 Tier 1 登記）**。依 R-P15(b)，`SWE-PM-057` 之歸屬待裁；若裁為 §1.8.1.1.1，R-P16 之刪除須撤回 |
| A-PW15 | SYS2 之 `Source Requirement items` 欄所填 id 並非全為需求錨點 id：**81 個為章節錨點 id**（Sys-RA 直接指向章節而非其下之需求） | 03 包 G6b：439 個 token 中 82 個無法經需求錨點路徑解析，其中 81 個實為 CFTS009 章節錨點 id（如 `4941006` = §1 Wake-up and Power-up），僅 1 個（`4942087`）兩路皆無 | **新增（執行層 Tier 1 登記）**。§C rule 3 稱該欄「即為上述 id」（rule 2 之需求錨點 id），與實測不符。已驗：兩種讀法對 G3（114/115）與跨章節 leaf 名單（11 個）**皆無影響**，故本包未擴張 rule 3；待分析層決定是否明文化第二條解析路徑 |
| A-PW16 | **跨章節 leaf 之次章節中有 9 章未被任何 leaf 之主章節覆蓋** —— 在現行主章節作法下，這 9 章不會產生任何 TC | 03 包 G14：被丟棄之相異次章節 10 個，僅 1 個被他 leaf 之主章節覆蓋。未覆蓋者：CFTS009 §1.6.2.1（TLM algorithm requirements）、§1.6.2.1.4（Stolen Vehicle Mode）、§1.6.2.1.9（Logistic Idle）、§1.6.2.1.10（Logistic Standby）、§1.6.2.1.11（Logistic Sleep）、§1.6.2.1.14（TLM modules and functionalities depending on operative state）、§1.6.2.1.15.1（ICS Wakeup Reasons by POWER Button Pressed）、§1.6.3.1.1（SwitchOff_Timeout_Setting.Req management）、§1.8.1.1.1（ID 1 Description） | **新增（R-P22 之閘門所捕獲）**。其中 `Stolen Vehicle Mode`、三個 `Logistic` 狀態、`ICS Wakeup Reasons by POWER Button Pressed` 為實質功能章節。Layer 3 之涵蓋宣稱在此 9 章上不成立 |

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-PWnn]`.
