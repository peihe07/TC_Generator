# DATA_REQUESTS — FW036 Projection

Files the corpus needs but did not arrive with the drop, and files whose
identity or version had to be established before use. One row per file.

Standing rule (carried from AMFM / SXM): any newly discovered external
reference gets a row HERE at the moment it is found, with the citing rows or
leaves named — not after the batch that needs it stalls. Every row here has a
matching ANOMALIES entry; neither exists without the other.

Rows 1–5 arrived with the Phase 0 下放包 §9. Rows 6–8 were opened by Phase 0
recon off the workbook's own `Specification Reference` column, which names its
sources on 558 of 559 rows and is the strongest 缺件 signal in this corpus
(A-PJ02). Rows 9–11 were opened by the Phase 2 PCTS on-device capture.

**Phase 2 結束狀態（2026-08-12，含補裁與 R-P21/R-P22）：11 列中 5 列 CLOSED**
（#3 #4 #5 #6 #7 —— 其中 **#4 曾於同日重開又關閉**，見該列）、
**2 列撤銷**（#9 #10，補裁 #2 / #3 判定不指認，需求消失）、
**OPEN 4 列** —— #1（取證部分滿足）、#2、#8、#11（併入首次實跑）。

**#4 的重開值得記一筆**：它是本專案唯一一條「關閉後又被證明關錯」的 DR。
關錯的原因不是疏忽，是 `inputs/` 內有一份**檔名含 `HUIG_4_5` 的檔案**，在
清單上看起來就是到位了。判斷缺件不能只看檔名，要看**被引用的錨點形式**該
文件給不給得出來（A-PJ24）。

---

| # | 檔案／資料 | 狀態 | 服務列數 | Anomaly | Urgency |
|---|---|---|---|---|---|
| 1 | **PCTS 5 個測項之操作路徑與讀值位置** —— 依 §3 改寫：不再索取整本手冊，改為由實機取證滿足。**取證已於 2026-08-12 執行**（Pixel 10 / Android 16 / PCTS Verifier `5.1-prod.922397802`，與 `inputs/` 之 apk 建號一致）。結果：`C2` **confirmed**、`NavigationStatusTests` **confirmed**、`MT1` / `D5` / `WP43` **partial**、row 443 的無名測項 **not_found**。23 列中 **14 列解鎖**（C2 的 13 列 + row 371），9 列維持 ABORT。詳見 `data/pcts_evidence.json` | ⚠️ **部分滿足** —— 3 項 partial 待人工確認 | 23（已解 14） | R-P11 / A-PJ20 / A-PJ21 | 取證中 |
| 2 | **`Est_Range_BEV` 的正式 LID 對映** —— mapping v1_76 無此 LID。9 個 `Est_Range*` LID 無一為 BEV 變體；三個近似候選互不等價，三選一即編造 | ❌ 未提供 | 2 | A-PJ03 | RD-1 |
| 3 | **`Vehicle_Line_Configuration` 值 332 定義** | ✅ **CLOSED by R-P8′** —— 332 是代碼 105 的標籤，非未定義值。更正為 `= 105 (332)` | 41 引用 | A-PJ04 / A-PJ10 | — |
| 4 | **HUIG 4.5 規格本文**（原名「Android Auto `AA-V4.5` 文件」，**2026-08-12 由 R-P21 重開並更名**）—— R-P13 原判「缺件不存在」只對了一半：在 `inputs/` 的 `SYS2_HUIG_4_5_…SYSRA…xlsx` 是 SYS.2 安全分析報告，而 workbook 79 列引的是 SYS.1 規格本文的 §/R-ID 條款錨點（`HUIG_4_5 §7.15 R07-326`、`HUIG_4.5_R12-460`），分析報告給不出那種錨點。實測複驗：79 列中 **43 僅引規格本文、36 兼引、0 僅引 SYSRA** | ✅ **CLOSED by R-P22**（2026-08-12 補入）—— `HUIG 4.5.pdf` `4cad6608…`（三處副本位元全同）+ `SYS1_HUIG4.5.xlsx` `5df67a2a…`；異 hash 分支未觸發 | **79 列** + 16 leaf | A-PJ24 / A-PJ05 / A-PJ09 | — |
| 5 | **CarPlay `CP-R46` 文件** | ✅ **CLOSED by R-P13** —— 立論撤銷。所指 4 條實為 `SYS-RA-CP_R10`（9 條）+ `CP-R10-3.2.7.2`（1 條），對應之 `SYS2_CP.R10_…_V01.xlsx` 已在 `inputs/` | 9 + 1 leaf | A-PJ05 / A-PJ09 | — |
| 6 | **`Accessory Interface Specification CarPlay Addendum R10`** | ✅ **CLOSED by R-P16** —— 已入 `inputs/`，三種格式：PDF `b8d4d6e1…`、docx `6fc6d1fc…`、SYS1 xlsx `5665820f…`。兩處 PDF 副本 hash 位元相同，無版本衝突 | 82 | A-PJ14 | — |
| 7 | **`Projection Device HMI Logic and Flow (May 3 2023)` + Change Log** | ✅ **CLOSED by R-P17** —— 已入 `inputs/`，PDF `36e585c3…`、Change Log `61338e3b…`、同版 SYS1 匯出 `530274f8…`（自行判斷補入，待覆核）。定為 O-1 之核對基準 | 116 | A-PJ15 | — |
| 8 | **CFTS025 需求本文** —— 專案樹內僅見 CFTS025 之測試用例簿與 SYS.2 目錄，需求本文未確認存在。leaf `SWE1-PROJ-146` 全文轉指 `CFTS025-4660` | ❌ 未提供 —— 依 R-P18 **不阻塞** | 24 + leaf 146 | A-PJ16 | Medium |
| ~~9~~ | ~~`V59 - Video Config 60 FPS` 之操作路徑與量測值顯示位置~~ | ✅ **撤銷（補裁 #2）** —— 裁定不指定 V59/V8，故無取證需求。row 441 維持不動並入 RD-1 | 1（row 441） | A-PJ20 | — |
| ~~10~~ | ~~row 443 無名測項之身分認定~~ | ✅ **撤銷（補裁 #3）** —— 裁定不指定 V45。row 443 比照 leaf 146，維持不動並入 RD-1 | 1（row 443） | A-PJ21 | — |
| **14** | **B5 跨車型前置條件之三層問題**（R-P47 改寫）—— `Knob` 42 列的 PRE 為 `PROXI VC_Veh_Line = <車型代號>`，7 值逐一對應 workbook 第 3 列的 7 個車型欄。**根因非「值寫錯」，而是 `PROXI_HDCC27_R3_20250424.xlsx` 為 HDCC27 單車型配置檔**（Header: `HDCC27 - Draft`），跨車型前置條件天生無法以本檔驗證。架構分層吻合：5 個對不上者全為 **Atl-Mid**，2 個對得上輪廓者全為 **Atl-Hi**，而 profile §4 之訊號解析僅取 mapping 表的 **Atlantis High** 欄。<br>**三層提問**：<br>**(a)** 這 42 列是否確實要跨 7 車型執行？→ 若是，需另 6 台車的 PROXI<br>**(b) 【先問，建議措辭】**「Atlantis Mid 車型（VF ProMaster 637 / Commander 598 / Renegade 5210 / Toro 2261 / Fastack 376）是否在 R1LR SWQT 驗證範圍內？」——(b) 是唯一**不預設任何事**的問題：(a) 答「是」會帶出取檔工程，(c) 已預設 Atl-Mid 在範圍內；只有 (b) 的答案能讓另外兩支自動消失→ 若否，30 列（5 車型 × 6）應標範圍外，**阻塞由 42 列縮為 12 列**<br>**(c)** 若在範圍內，Atl-Mid 之訊號對照走 mapping 表哪一欄？（mapping 有 Atlantis Mid 欄，但 profile §4 未涵蓋） | ❌ 未提供 | **42**（Atl-Mid 30 / Atl-Hi 12） | A-PJ45 | **停下條件** —— B5 全批阻塞；**影響止於 `Knob`，B6/B7 不牽連** |
| **13** | **`Performance` 組 7 列之量測設備規格** —— r110/r113（CarPlay：mode-update 與 audio-setup 響應時間）、r114–r118（Android Auto：video setup latency、input-to-display latency、end-to-end latency、audio output latency、RTT／bandwidth）。現況僅寫 `Test equipment for measuring … is available`。已查 CarPlay Tests User Manual R2.19.4：`Performance Tests > Touch Latency`(p26) 與 `Connectivity Utilities > CarPlay Network Tests`(p36) 存在但**不涵蓋這 7 列**（5 列為 Android Auto，CarPlay App 不適用；2 列無對應功能）。需取得：Android Auto 側之量測工具，及 CarPlay 側 mode-update／audio-setup 之量測方式。**2026-08-12 增補**：B4 另發現 3 列 `trace tool` 型泛稱（r141/r142/r147，Voice Recognition），CarPlay 側之 requestSiri／KEYCODE_SEARCH trace 工具應為 ATS 但簿內未載明（A-PJ44），一併請求 | ❌ 未提供 | 7 + 3 = 10 | A-PJ39 | **列級阻塞（7 列）** —— 依 R-P35 同型邏輯，阻塞的是那 7 列而非批次或階段。`Performance` 批照常結案，7 列列為「正確地不動」 |
| **12** | **`mobile GAL log` 之操作手冊** —— Android Auto 裝置端 log capture 工具，不在 `inputs/` 三個工具目錄（`ATS 8.10.0` / `PCTS` / `CarPlay TestApp`）內，無任何手冊或 README。需取得：啟動方式、log 檔位置、過濾條件。**併請 `logcat` 之過濾條件依據**（A-PJ35，程度較輕：啟動方式公知，缺的是該以何 tag／關鍵字過濾 Android Auto 位置資料） | ❌ 未提供 | 4（r231–234）+ 3（r222–224） | A-PJ32 / A-PJ35 | **Phase 5 前** —— 此 7 列在取得前無法修訂 |
| **11** | **MT1 / WP43 / D5 之操作細節** —— adb 唯讀取證無法取得三項：MT1 的「OK 鈕啟動自動量測 + 量測值顯示位置」、WP43 的「提示流程步驟」、D5 的「色深顯示位置」。三者皆須實際開啟測項頁才看得到。**補裁 #4 定為併入首次實跑回填**，不另辦人工確認 —— 這些細節本來就要在真正執行該測項時才看得到，另辦一次是重複勞動 | ⚠️ **併入首次實跑** | 3（267, 521, 522）+ 441 另因 A-PJ20 鎖定 | R-P11 | 隨首次實跑 |

---

## 已到位、無需請求（recon 確認）

| 檔案 | 引用列數 | 版本核對 |
|---|---|---|
| `R1LR_Atl-H_25PI3.5_…CFTS_85 Brought In Device Mirroring_20250910_1704.docx` | 473（spec_reference 主力） | 25PI3.5，與 workbook 引用一致 |
| `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023)` | 75 | ✅ 版本相符 |
| `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023)` | 40 | ✅ 版本相符；引用 5 個 PU id：`PU0252` `PU0254` `PU0520` `PU0523` `PU0816`，已寫入 `feature.yaml → lint.popup_ids` |
| `HUIG 4.5.pdf` + `SYS1_HUIG4.5.xlsx` | **79** | ✅ 2026-08-12 補入（R-P22）—— 這才是 79 列引用的規格本文 |
| `SYS2_HUIG_4_5_…_V01.xlsx` | 0（不供任何引用） | SYS.2 安全分析報告。**不作為規格來源**（R-P21）。專案樹內另有一份 `SYS2_HUIG_4_5.xlsx`（`4a049e0c…`，231,157 B）內容不同，因本檔已不在引用路徑上，僅記錄 |
| `SYS2_CP.R10_…_V01.xlsx` | 26（`CP-R10`） | 見第 5 列 |
| `R1LR_Atl-H_25PI3.5_…CFTS 019_Audio Management_20250910_1235.doc` | 16 | ✅ |
| `ATS User Guide.pdf` + `ATS 8.10 README.rtf` | 10 列 Procedure 提及 ATS | O-3 手冊到位 |
| `CarPlay Tests User Manual R2.19.4.pdf` + README | 6 列 Procedure 提及 testapp | O-3 手冊到位。手冊位於 `CarPlay TestApp/` 一層，非下放包 §3.2 所寫的 `…/CarPlay Tests App Test Files and README/` 子目錄；README rtf 則在子目錄內 |
| `PROXI_HDCC27_R3_20250424.xlsx` | 全部前置條件 | 1,052 個 distinct parameter；`Projection Mode Selection` 分頁位元編碼可用 |
| 兩份 DBC | 39 列 CAN 步驟 | FDCAN8 244 msg、BHCAN 123 msg、重疊 24；ISO-8859 編碼 |

## 跨 feature 同源政策

R-P16 / R-P17 **明文授權跨出 R-P5 根目錄取檔**，Phase 0 所記的「未做跨目錄
複製」限制隨之解除。取檔一律先對全部副本計算 SHA256 再選版，沿用 AMFM / SXM
的規則 —— 「檔名相同」不足以證明「內容相同」。

本次兩案的 hash 結果：

- **CarPlay Addendum R10** —— `1_Customer_Requirement/CPAA_spec/` 與
  `10_Reviewing/00_TestCase/Bluetooth/REF/` 兩份 PDF **位元相同**
  （`b8d4d6e1…`），依 §4.1 規則 2 取前者。異 hash 分支未觸發。同文件另有
  `.docx` 與 SYS.1 匯出 `.xlsx` 兩種格式，屬不同產物而非不同版本，一併落地。
- **Projection Device HMI (May 3 2023)** —— PDF 與 Change Log 各僅一處副本，
  無可比對象，無衝突。

Bluetooth 目錄的副本僅記錄路徑，未另行複製 —— 本 repo 內 `features/bluetooth/`
尚未 scaffold，且該檔與已落地者位元相同。
