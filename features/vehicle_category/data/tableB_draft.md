# 表 B 草稿｜覆蓋落差揭露 —— Vehicle Category（17 節）

> **草稿，非交付件。** 最終措辭待 DR-VC3 回覆（R-VC12 二(b)、下放包 03 T23）。
> 母體依 **R-VC12 一**：未引用 42 節 ＝ 非需求性質 25 ＋ 有實質內容 **17**。
> §16.1 已由 (b) 改列 (a)（交叉引用，非實質需求內容），故非 18 節。
> 內容來源一律為 repo `inputs/` 之 SYS1 `Description` 欄
> （SHA256 `1fcc8711…b091d6`）—— **不引用下放包 01 §4.2(b) 之摘要**
> （R-VC12 二已就 §15／§10.1／§10.2 作廢之，見 `docs/REVISIONS.md` REV-07）。

| # | 章節 | 群 | 內容（SYS1 `Description`） | 處置 |
|---|---|---|---|---|
| 1 | §8.1 | Cabrio 車頂開闔 | Convertible top operations: • Open rooftop operation: operation for start and complete rooftop opening (when is closed), for start operation push and hold (for entire operation) button A1 When rooftop in moving present graphic popup (3D render animation) • Close rooftop operation: operation for … | 037 未涵蓋，本次不產出 TC |
| 2 | §8.2 | Cabrio 車頂開闔 | If user release the button when folding top in moving (opening/closing), the rooftop stops (warning in cluster for complete operation indication to the user and on head unit a specific 30 render animation in head unit) | 037 未涵蓋，本次不產出 TC |
| 3 | §8.3 | Cabrio 車頂開闔 | A graphic representation of the vehicle status will be present on pop up (when top is open there will be a open vehicle, when top is closed there will be a closed vehicle) | 037 未涵蓋，本次不產出 TC |
| 4 | §8.4 | Cabrio 車頂開闔 | Convertible top opera ions are available with this conditions: • Car speed below 50 kmlh (see VF507 for official reference) • The A 1 / A2 button has to be pressed and hold until movement is completed, that will last up to 15s (see VF507 for reference) • For all the preconditions and fall status … | 037 未涵蓋，本次不產出 TC |
| 5 | §8.5 | Cabrio 車頂開闔 | The roof controls are greyed if the system detect a fail (service required) | 037 未涵蓋，本次不產出 TC |
| 6 | §9.1 | Cabrio 擋風板 | Wind draught deflector/backlight top operations: • Low up wind draught deflector: push and hold button B1 • Raise down wind draught deflector: push and hold button B2  (image: image8.png) | 037 未涵蓋，本次不產出 TC |
| 7 | §9.2 | Cabrio 擋風板 | If user release the button when wind draught deflector during moving (up/down), the window will stop to the user desiderate position. The roof controls are greyed if the system detect a fail (service required) | 037 未涵蓋，本次不產出 TC |
| 8 | §10.1 | Aux Switch | **該節內容僅存於圖，SYS1 匯出未帶文字**（`(image: imageNN.png)` 佔位） | 037 未涵蓋，本次不產出 TC |
| 9 | §10.2 | Aux Switch | **該節內容僅存於圖，SYS1 匯出未帶文字**（`(image: imageNN.png)` 佔位） | 037 未涵蓋，本次不產出 TC |
| 10 | §11.9 | Settings 通則邏輯 | General logic for setting with options | 037 未涵蓋，本次不產出 TC |
| 11 | §11.9.1 | Settings 通則邏輯 | In a setting line with many options: - pressing on option currently not selected (no check selection in option) move the selection and change the option accordingly. - pressing on option already selected (with selection) do not perform action (maintain the option selection). | 037 未涵蓋，本次不產出 TC |
| 12 | §11.9.2 | Settings 通則邏輯 | When in a setting line with one option only: -If on/off setting (e.g. ‘Touchscreen beep’) pressing on option select/deselect the option (check appear/disappear). For driver distraction the same behavior is performed pressing on the entire row area. -If one-of-many option setting (e.g. ‘English’ u… | 037 未涵蓋，本次不產出 TC |
| 13 | §11.9.3 | Settings 通則邏輯 | General logic for setting with +/- options:  - When in a line with +/- buttons: if press on a +/- button, increment or decrement the option’s value depending on the button selected. Pressing outside the +/- buttons do not perform action. - At max values + greys out, at min values - greys out. | 037 未涵蓋，本次不產出 TC |
| 14 | §14.2 | EPB 彈窗優先序 | EPB Service Mode Pop-up Priority:  E-Call  Incoming Call /Text Message System Errors EPB Service Mode  System Feedback (e.g. Mute Pop-up)  (image: image19.png) | 037 未涵蓋，本次不產出 TC |
| 15 | §15 | EPB 彈窗 | **該節內容僅存於圖，SYS1 匯出未帶文字**（`(image: imageNN.png)` 佔位） | 037 未涵蓋，本次不產出 TC |
| 16 | §16.2.1 | Cabrio Widget | Convertible top operations: • Open rooftop opera ion: operation for start and complete rooftop opening (when is closed) for s art operation push and hold (for entire operation) button A1 When rooftop in moving present graphic popup on cluster • Close rooftop operation: operation for start and com… | 037 未涵蓋，本次不產出 TC |
| 17 | §16.2.2 | Cabrio Widget | Wind draught deflector/backliight top operations: • Low up wind draught deflector: push and hold button B1 • Raise down wind draught deflector: push and hold button B2 | 037 未涵蓋，本次不產出 TC |

---

## 註

1. **§8.3** 於下放包 01 §4.2(b) 之摘要中漏列，本表依 R-VC12 二(c) 補入，
   來源記為 SYS1 `Description`。
2. **§10.1／10.2／§15** 三節之「內容」欄依 R-VC12 二(a) 一律書
   「該節內容僅存於圖，SYS1 匯出未帶文字」，**不得寫入任何摘要文字**。
   其可讀來源之取得已立 **DR-VC6**（條件性，待 DR-VC3）。
3. 其餘各節之內容經 T17 驗為**與 SYS1 所載相符**；其效力僅及於此，
   **非「與規格原件相符」** —— FO §3 之 Mode A 盲點（匯出可能靜默漏句）
   本法看不見。
4. 本表為 **R-VC3 之出貨門檻二表之一**，缺之不得出貨。表 A（FROP 跨域，
   17 列）另備。
