# 表 B 草稿｜覆蓋落差揭露 —— Vehicle Category（17 節）

> **草稿，非交付件。** 最終措辭待 DR-VC3 回覆（R-VC12 二(b)、下放包 03 T23）。
> 母體依 **R-VC12 一**：未引用 42 節 ＝ 非需求性質 25 ＋ 有實質內容 **17**。
> §16.1 已由 (b) 改列 (a)（交叉引用，非實質需求內容），故非 18 節。
> 內容來源一律為 repo `inputs/` 之 SYS1 `Description` 欄
> （SHA256 `1fcc8711…b091d6`）—— **不引用下放包 01 §4.2(b) 之摘要**
> （R-VC12 二已就 §15／§10.1／§10.2 作廢之，見 `docs/REVISIONS.md` REV-07）。

### ⚠ 本表全體之效力限制（R-VC12 二(d)；下放包 27 §2.2 要求寫在表上）

```
本表各節之「內容」欄，其效力僅及於「**與 repo `inputs/` 之 SYS1 匯出相符**」，
**非「與規格原件相符」**。

FO §3 之 Mode A 盲點：匯出可能靜默漏句，而本法看不見 ——
即「SYS1 沒有的句子」與「規格原件沒有的句子」在本表中無法區分。
```

### ⚠ 待 DR-VC3 之**四處**（下放包 28 §2.1 追認；下放包 27 §2.2 原列三處）

| 處 | 涉及列 | 若 DR-VC3 回覆「應補」之後果 |
|---|---|---|
| 章 8／9 Cabrio 本體 | 1–7（§8.1–§9.2）| 另立 Test Set `Cabrio Rooftop`，**framework 由 8 組變 9 組**（R-VC16(c)）|
| `Brake Service` 待補節 | 14–15（§14.2／§15）| 併入 #7，該組由 2 leaf 長大 |
| `Cabrio Widget` 待補節 | 16–17（§16.2.1／§16.2.2）| 併入 #8，該組由 1 leaf 長大 |
| **§11.9 群**（執行層補列，下放包 28 §2.1 **追認**）| 10–13 | 其歸 #5 為**條件性生效**，待 DR-VC3（R-VC16(d)）|

**上開四處若生效，表 A 之 `Test Set` 欄與 `verify_partn.py` 皆須重編。**

---

| # | 章節 | 群 | 內容（SYS1 `Description`） | 處置 | 待 DR-VC3 |
|---|---|---|---|---|---|
| 1 | §8.1 | Cabrio 車頂開闔 | Convertible top operations: • Open rooftop operation: operation for start and complete rooftop opening (when is closed), for start operation push and hold (for entire operation) button A1 When rooftop in moving present graphic popup (3D render animation) • Close rooftop operation: operation for … | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 2 | §8.2 | Cabrio 車頂開闔 | If user release the button when folding top in moving (opening/closing), the rooftop stops (warning in cluster for complete operation indication to the user and on head unit a specific 30 render animation in head unit) | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 3 | §8.3 | Cabrio 車頂開闔 | A graphic representation of the vehicle status will be present on pop up (when top is open there will be a open vehicle, when top is closed there will be a closed vehicle) | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 4 | §8.4 | Cabrio 車頂開闔 | Convertible top opera ions are available with this conditions: • Car speed below 50 kmlh (see VF507 for official reference) • The A 1 / A2 button has to be pressed and hold until movement is completed, that will last up to 15s (see VF507 for reference) • For all the preconditions and fall status … | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 5 | §8.5 | Cabrio 車頂開闔 | The roof controls are greyed if the system detect a fail (service required) | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 6 | §9.1 | Cabrio 擋風板 | Wind draught deflector/backlight top operations: • Low up wind draught deflector: push and hold button B1 • Raise down wind draught deflector: push and hold button B2  (image: image8.png) | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 7 | §9.2 | Cabrio 擋風板 | If user release the button when wind draught deflector during moving (up/down), the window will stop to the user desiderate position. The roof controls are greyed if the system detect a fail (service required) | 037 未涵蓋，本次不產出 TC | ✅ 章 8／9 |
| 8 | §10.1 | Aux Switch | **逐字引錄**（`/` 為換行，不摘要、不省略）：`The flow of pressing the Aux settings from Controls /  (image: image9.png)  /  (image: image10.png)  / Refer to the HMI Settings list for settings location.  / All four Aux switches (Aux 1 Aux 2, Aux 3, and Aux 4) can be used simultaneously / Graphics are visual aids only. Please see PDO release for official graphics`| 037 未涵蓋，本次不產出 TC | — |
| 9 | §10.2 | Aux Switch | **逐字引錄**（`/` 為換行，不摘要、不省略）：`The flow of pressing the Aux settings from Apps /  (image: image11.png)  /  (image: image12.png)  / Refer to the HMI Settings list for settings location.  / All four Aux switches (Aux 1 Aux 2, Aux 3, and Aux 4) can be used simultaneously / Graphics are visual aids only. Please see PDO release for official graphics`| 037 未涵蓋，本次不產出 TC | — |
| 10 | §11.9 | Settings 通則邏輯 | General logic for setting with options | 037 未涵蓋，本次不產出 TC | ⚠ §11.9 群 |
| 11 | §11.9.1 | Settings 通則邏輯 | In a setting line with many options: - pressing on option currently not selected (no check selection in option) move the selection and change the option accordingly. - pressing on option already selected (with selection) do not perform action (maintain the option selection). | 037 未涵蓋，本次不產出 TC | ⚠ §11.9 群 |
| 12 | §11.9.2 | Settings 通則邏輯 | When in a setting line with one option only: -If on/off setting (e.g. ‘Touchscreen beep’) pressing on option select/deselect the option (check appear/disappear). For driver distraction the same behavior is performed pressing on the entire row area. -If one-of-many option setting (e.g. ‘English’ u… | 037 未涵蓋，本次不產出 TC | ⚠ §11.9 群 |
| 13 | §11.9.3 | Settings 通則邏輯 | General logic for setting with +/- options:  - When in a line with +/- buttons: if press on a +/- button, increment or decrement the option’s value depending on the button selected. Pressing outside the +/- buttons do not perform action. - At max values + greys out, at min values - greys out. | 037 未涵蓋，本次不產出 TC | ⚠ §11.9 群 |
| 14 | §14.2 | EPB 彈窗優先序 | EPB Service Mode Pop-up Priority:  E-Call  Incoming Call /Text Message System Errors EPB Service Mode  System Feedback (e.g. Mute Pop-up)  (image: image19.png) | 037 未涵蓋，本次不產出 TC | ✅ Brake Service |
| 15 | §15 | EPB 彈窗 | 標題句 `Electronic Park Brake Service Mode Pop-up`，其餘內容為三個圖佔位（image20／21／22），SYS1 匯出未帶其文字。**逐字**：`Electronic Park Brake Service Mode Pop-up /  (image: image20.png)  /  (image: image21.png)  /  (image: image22.png)`| 037 未涵蓋，本次不產出 TC | ✅ Brake Service |
| 16 | §16.2.1 | Cabrio Widget | Convertible top operations: • Open rooftop opera ion: operation for start and complete rooftop opening (when is closed) for s art operation push and hold (for entire operation) button A1 When rooftop in moving present graphic popup on cluster • Close rooftop operation: operation for start and com… | 037 未涵蓋，本次不產出 TC | ✅ Cabrio Widget |
| 17 | §16.2.2 | Cabrio Widget | Wind draught deflector/backliight top operations: • Low up wind draught deflector: push and hold button B1 • Raise down wind draught deflector: push and hold button B2 | 037 未涵蓋，本次不產出 TC | ✅ Cabrio Widget |

---

## 註

1. **§8.3** 於下放包 01 §4.2(b) 之摘要中漏列，本表依 R-VC12 二(c) 補入，
   來源記為 SYS1 `Description`。
2. **§10.1／10.2／§15** 三節 —— **R-VC12 二(a) 已作廢，改依 R-VC27**
   （下放包 28 §一）。其「內容」欄改為**逐字引錄 SYS1 `Description`**，
   不以任何形式之概括代之。
   原措辭「該節內容僅存於圖，SYS1 匯出未帶文字」**於 §10.1／§10.2 實測不成立**
   （A-VC20）—— 該二節之文字含實質需求敘述
   `All four Aux switches (Aux 1 Aux 2, Aux 3, and Aux 4) can be used simultaneously`。
   **DR-VC6 之問法隨之改為三問**（見 `DATA_REQUESTS.md`）。
3. 其餘各節之內容經 T17 驗為**與 SYS1 所載相符**；其效力僅及於此，
   **非「與規格原件相符」** —— FO §3 之 Mode A 盲點（匯出可能靜默漏句）
   本法看不見。
4. 本表為 **R-VC3 之出貨門檻二表之一**，缺之不得出貨。表 A（FROP 跨域，
   17 列）另備。

5. **§11.9 群為執行層補列之第四處待 DR-VC3**（下放包 27 §2.2 只列三處）——
   R-VC16(d) 明文「11.9 群歸 #5 …**條件性生效，待 DR-VC3**」。
   若該群補入，其四節之歸屬須依該條重審。**記於此以免漏於重編清單。**

6. **A-VC20 已解**（R-VC27，下放包 28 §一）。其成因值得留在這裡：
   R-VC12 二(a) 之措辭係讀**衍生 PDF** 所得而**從未讀 SYS1 那三格**，
   而 R-VC12 **三、通則**所禁者正是「以衍生物之判讀充當實測值」——
   **一條為糾正該錯誤而立的條文，其中一款是該錯誤的產物**，
   且此後被引用 24 個包，包括本表。
   **本表之「內容」欄自此一律逐字引錄，不概括** ——
   概括會使讀表者無從判斷該節有沒有可用之文字，而那正是本表要回答的問題。
