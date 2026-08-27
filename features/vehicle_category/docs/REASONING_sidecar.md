# `reasoning` 側檔 —— Vehicle Category

> **隨工作簿一併交付**（下放包 28 §2.2）。
> 工作簿之 TC 欄位為 English only（IN §1）；本檔為繁中之判讀紀錄，故不入工作簿而另立。

- 產出：`scripts/build_reasoning_sidecar.py`，下放包 28 T150
- 鍵：`leaf_id#n`，`n` 為該 leaf 於其批內之 TC 序（拆分筆據此區分）
- 筆數：**120**，與六批 JSON 之 TC 總數相同（`--verify` 驗之）
- `split_flag`／`split_reason` 不入本檔（profile §11）

---


## 批次 `pilot_glovebox`

### `SWE1-HMI-VC-026-01#1` — Explanatory popup shown on selecting Glove Box

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_4.1`
- **`distinguishing_axis`**：流程階段：說明彈窗（對 -026-02 之 PIN 請求彈窗、-026-03 之兩次輸入）
- **`reasoning`**：**驗證目標**：選取 Glove Box 後之說明彈窗確實出現且載明啟用所需動作。**關鍵情境條件**：Glove Box 尚未啟用，自 Controls 進入。**為什麼這樣切**：本 leaf 只擁有「說明彈窗出現」一句，PIN 請求彈窗屬 -026-02，故 1 筆即足（§8.2.2）。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-026-02#1` — PIN request popup shown after Yes

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_4.1`
- **`distinguishing_axis`**：流程階段：按 Yes 後之 PIN 請求彈窗（對 -026-01 之說明彈窗）
- **`reasoning`**：**驗證目標**：說明彈窗按 Yes 後轉入 PIN 請求彈窗。**關鍵情境條件**：說明彈窗已開啟。**為什麼這樣切**：本 leaf 擁有「按 Yes → PIN 請求彈窗」之單一轉換；說明彈窗本身屬 -026-01，兩次輸入屬 -026-03。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-026-03#1` — PIN entered twice with instruction text differing

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_4.1`
- **`distinguishing_axis`**：流程階段：兩次鍵盤輸入及其差異點（對 -026-01／-026-02 之單一彈窗）
- **`reasoning`**：**驗證目標**：PIN 須輸入兩次，且二次之差異僅在指示文字。**關鍵情境條件**：自說明彈窗按 Yes 進入鍵盤彈窗。**為什麼這樣切**：「兩次」與「僅指示文字不同」是同一句需求之二個面向，同一次執行即可觀察，拆分會使二者失去對照（§8.2.2）。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-027#1` — Glove Box Activated popup after matching PINs

- **`test_set`**：Glove Box　**`priority`**：P2　**`spec_ref`**：`…_4.2`
- **`distinguishing_axis`**：驗證標的：啟用成功之確認彈窗（對 -028-01 之不符警告彈窗）
- **`reasoning`**：**驗證目標**：兩次 PIN 相符後顯示啟用確認彈窗。**關鍵情境條件**：二次輸入之值相同。**為什麼這樣切**：本 leaf 擁有確認彈窗之顯示一句；不符之路徑屬 -028-01。**設計方法**：未啟用 → 已啟用之狀態轉換，故取狀態轉換。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-028-01#1` — Incorrect PIN warning on mismatched second entry

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_5.1`
- **`distinguishing_axis`**：錯誤面向：單次不符之警告（對 -028-02 之次數上限不存在）
- **`reasoning`**：**驗證目標**：第二次輸入與第一次不符時之警告彈窗，且功能未被啟用。**關鍵情境條件**：二次輸入之值不同。**為什麼這樣切**：本 leaf 為**單次**不符之回饋；次數上限之不存在屬 -028-02，二者為不同標的（§8.2.1）。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-028-02#1` — No upper limit on incorrect activation attempts

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_5.1`
- **`distinguishing_axis`**：錯誤面向：啟用流程無次數上限（對 -033-01 之停用流程有鎖定門檻）
- **`reasoning`**：**⚠ 測試設計參數（下放包 12 §3.2）**：本步驟之重複次數 **N = 10** 為**測試設計選擇，規格未給上限值**。037 之 `There's not a limit for the incorrect input.` 為否定性存在命題 —— **無法以有限次數證明**，測試至多做到「重複 N 次仍可用」。N 之正當性來自其被明確標示為測試設計，非被偽裝成規格值；此與 §8.4.1 所禁之「發明來源未述之規格值」不同類。**前一版之 `a comparable attempt ceiling` 已移除** —— 該參照指向 `-033-01` 之停用門檻（正由 DR-VC8 爭議），既造了一個規格未述之參照對象，又使本筆之可執行性隱性繫於他筆之未定值。 **驗證目標**：啟用流程之錯誤輸入次數無上限。**關鍵情境條件**：連續多次不符。**為什麼這樣切**：本 leaf 之標的是「上限不存在」，屬否定性存在命題，以重複步驟表述，**不造具體次數**（§8.4.1）—— 037 未給 N 之值。⚠ 本筆與 -033-01（停用流程三次鎖定）**不矛盾**：二者分屬啟用（§5.1）與停用（§7.1）兩個流程，括號下半已明載其流程。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-029#1` — Activation succeeds on first-entered PIN after mismatches

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_5.2`
- **`distinguishing_axis`**：錯誤面向：多次錯誤後之成功復原（對 -028-02 之上限不存在）
- **`reasoning`**：**驗證目標**：多次錯誤後輸入第一次所設之 PIN，功能仍可啟用。**關鍵情境條件**：先前之錯誤次數不影響第一次所設值之有效性。**為什麼這樣切**：本 leaf 擁有「錯誤後仍可成功」之復原路徑；-028-02 擁有「無上限」之存在命題，二者標的不同。「N 次」不造具體值（§8.4.1）。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-030#1` — Deactivation prompts for the same PIN

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_6.1`
- **`distinguishing_axis`**：流程階段：停用之進入與 PIN 要求（對 -031 之停用確認彈窗）
- **`reasoning`**：**驗證目標**：停用之進入點要求輸入與啟用時相同之 PIN。**關鍵情境條件**：功能已啟用且 PIN 已知。**為什麼這樣切**：本 leaf 擁有停用之進入與其 PIN 要求；接受後之確認彈窗屬 -031。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-031#1` — Glove Box Mode deactivated popup after PIN accepted

- **`test_set`**：Glove Box　**`priority`**：P2　**`spec_ref`**：`…_6.2`
- **`distinguishing_axis`**：流程階段：停用確認彈窗（對 -032 之按 OK 後返回）
- **`reasoning`**：**驗證目標**：停用 PIN 通過後顯示停用確認彈窗。**關鍵情境條件**：輸入之 PIN 與啟用時相同。**為什麼這樣切**：本 leaf 擁有確認彈窗之顯示；按 OK 之後續導覽屬 -032。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-032#1` — OK on confirmation popup returns to Controls

- **`test_set`**：Glove Box　**`priority`**：P3　**`spec_ref`**：`…_6.3`
- **`distinguishing_axis`**：流程階段：按 OK 後之返回目標（對 -031 之彈窗顯示）
- **`reasoning`**：**驗證目標**：按 OK 關閉確認彈窗並返回 Controls 主頁。**關鍵情境條件**：確認彈窗已顯示。**為什麼這樣切**：本 leaf 擁有關閉後之導覽目標；彈窗之顯示屬 -031。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-033-01#1` — Deactivation locked for 30 minutes after repeated wrong PINs

- **`test_set`**：Glove Box　**`priority`**：P1　**`spec_ref`**：`…_7.1`
- **`distinguishing_axis`**：錯誤面向：停用流程之次數門檻與鎖定（對 -033-02 之位數門檻）
- **`reasoning`**：**⚠ 爭議值揭露（R-VC20(b)，四項）**：(1) 二欄之逐字內容 —— `Requirement Title`：`After three sequential wrong PINs during Glove Box deactivation, block the deactivation feature for 30 minutes`；`Requirement Description`：`Inserts the wrong PIN more than three times in sequence, the feature will be blocked for 30'.`。(2) 分歧點 —— 二者之數字同為 three，**差別在比較器**：`After three` 觸發於第 3 次，`more than three` 觸發於第 4 次，相差一次。此為可測門檻之分歧，非措辭差異（A-VC14）。(3) 以 `Title` 為 verbatim 上半 —— 依 R-S4「上半為需求／規格原句」，取之係因其為完整之需求句，**非採信其值為 3**；依 R-VC20(a) 不改寫、不迴避、不換欄取值（換取 Description 只是換一個爭議值）。(4) 阻斷之 DR —— **DR-VC8**（同批 A）。其回覆到達後本筆依值 Revise，並依 R-VC18 另裁是否補拆 boundary 之 2–3 筆。**R-VC20(c) 已複查**：本筆 ER 三項皆為行為表述（彈窗顯示／逐次拒絕且計數推進／功能被鎖定 30 分鐘），**無次數門檻出現於判準位置**；門檻由 procedure 之 `PENDING` 承載。 **驗證目標**：停用流程連續錯誤達門檻後鎖定 30 分鐘。**關鍵情境條件**：連續錯誤，非累計錯誤。**為什麼這樣切**：R-VC18 明文本輪就本 leaf 產 1 筆 —— §8.3 之 boundary 三點（門檻−1／=門檻／鎖定期滿）因 A-VC14 之門檻未定而無從定值，DR-VC8 回覆後另裁是否補拆為 2–3 筆。**未涵蓋**：門檻−1 不鎖、鎖定期滿後解除、30 分鐘之計時起點 —— 後者規格與 037 皆未載，已併 DR-VC8 附帶查詢。⚠ 與 -028-02（啟用流程無上限）**不矛盾**：本筆為**停用**流程。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。

### `SWE1-HMI-VC-033-02#1` — Four-digit rule enforced on 3-digit entry

- **`test_set`**：Glove Box　**`priority`**：P2　**`spec_ref`**：`…_7.1`
- **`distinguishing_axis`**：錯誤面向：停用流程之位數門檻（對 -033-01 之次數門檻）
- **`reasoning`**：**驗證目標**：位數不足之輸入被擋下並提示 4 位規則。**關鍵情境條件**：輸入 3 位後按 Enter。**為什麼這樣切**：本 leaf 之門檻為**位數**，-033-01 之門檻為**次數**，二者為不同軸；4 位之正常路徑已由 -030／-031 涵蓋（§8.2.2）。 §8.2.1 委派：進入 Glove Box 流程之 Controls 頁籤操作寫於 setup 步驟，但按下 Glove Box 鈕所開之 Privacy Lock 彈窗，其 id／標題／按鈕組成由 `SWE1-HMI-VC-021`（§3.6）擁有且受 DR-VC1 阻斷，本 TC 之 ER 不驗證之。


## 批次 `batch1_category_structure`

### `SWE1-HMI-VC-001-01#1` — Controls and Settings tabs present in Vehicle Category

- **`test_set`**：Category Structure　**`priority`**：P1　**`spec_ref`**：`…_2.2`
- **`distinguishing_axis`**：頁籤集之組成（對 -001-02 之首次預設、-001-03 之回復）
- **`reasoning`**：**驗證目標**：Vehicle Category 之主要頁籤集含 Controls 與 Settings。**關鍵情境條件**：車輛配備該 feature。**為什麼這樣切**：本 leaf 只擁有「有哪些頁籤」一句；哪一個為預設作用中屬 -001-02、回復上次屬 -001-03（§8.2.2）。

### `SWE1-HMI-VC-001-02#1` — Controls active on first entry

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.2`
- **`distinguishing_axis`**：進入次序：首次（對 -001-03 之後續進入）
- **`reasoning`**：**驗證目標**：首次進入時預設作用頁籤為 Controls。**關鍵情境條件**：尚無頁籤瀏覽紀錄 —— 此為與 -001-03 之分界。**為什麼這樣切**：037 已將「首次」與「其後」拆為二 leaf，依 R-VC18 之一 leaf 一 TC 先例不合併。

### `SWE1-HMI-VC-001-03#1` — Last viewed tab restored on re-entry

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.2`
- **`distinguishing_axis`**：進入次序：後續進入之回復（對 -001-02 之首次預設）
- **`reasoning`**：**驗證目標**：再次進入時回復上次瀏覽之頁籤，而非回到預設之 Controls。**關鍵情境條件**：離開前之作用頁籤非預設值 —— 若取 Controls 則本 TC 與-001-02 無法區辨。**為什麼這樣切**：本 leaf 之標的為回復行為，首次之預設屬 -001-02。**設計方法**：離開 → 再進入之狀態轉換。

### `SWE1-HMI-VC-002#1` — Specialty tabs placed left of Controls and Settings

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.3`
- **`distinguishing_axis`**：排列面向：相對於基本頁籤之位置（對 -003 之固定優先序）
- **`reasoning`**：**驗證目標**：Specialty 頁籤出現且位於 Controls／Settings 之左。**關鍵情境條件**：車輛配備至少一個 Specialty feature —— 未配備則無標的。**為什麼這樣切**：本 leaf 之標的為**相對位置**；固定優先序屬 -003，可列入之功能列舉屬 -006。

### `SWE1-HMI-VC-003#1` — Tab priority order follows the fixed five-position list

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.3.1`
- **`distinguishing_axis`**：排列面向：五位置之絕對優先序（對 -002 之相對位置）
- **`reasoning`**：**驗證目標**：五個位置之固定優先序。**關鍵情境條件**：須同時配備 My Car、Cameras 與其他 Specialty，否則序列不完整而無法驗其優先。**為什麼這樣切**：-002 驗相對位置（Specialty 在左），本 leaf 驗**絕對序**；二者為不同標的。**設計方法**：多個配備條件共同決定一個排列，取決策表。

### `SWE1-HMI-VC-004#1` — Controls tab label reads "Controls"

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.3.2`
- **`distinguishing_axis`**：標籤標的：Controls 頁籤（對 -005 之 Settings 頁籤）
- **`reasoning`**：**驗證目標**：Controls 頁籤之字面標籤。**關鍵情境條件**：無 —— 該標籤不隨配備變動。**為什麼這樣切**：037 將二個頁籤之標籤拆為 -004／-005 二 leaf，不合併。

### `SWE1-HMI-VC-005#1` — Vehicle Settings tab label reads "Settings"

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.3.3`
- **`distinguishing_axis`**：標籤標的：Settings 頁籤（對 -004 之 Controls 頁籤）
- **`reasoning`**：**驗證目標**：Vehicle Settings 頁籤之字面標籤為 Settings（非 Vehicle Settings）。**關鍵情境條件**：無。**為什麼這樣切**：同 -004，037 已拆。

### `SWE1-HMI-VC-006#1` — Off Road, PHEV and SRT eligible as Specialty tabs

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.3.4`
- **`distinguishing_axis`**：集合面向：列舉成員之有效性（非窮舉，故不驗排他）
- **`reasoning`**：**驗證目標**：來源所列舉之三個 Specialty 功能確可成為頁籤。**關鍵情境條件**：三者皆配備。**為什麼這樣切**：來源明文 `include, but are not limited to` —— **該列舉非窮舉**，故本 TC 只驗所列之三者為**有效成員**，不驗「僅此三者」（那會是對開放列舉之錯誤封閉，觸 §8.4.2）。**未涵蓋**：列舉外之 Specialty 功能 —— 來源未給其名，不造值（§8.4.1）。

### `SWE1-HMI-VC-007-02#1` — PHEV family maps to E. Hybrid, Performance group to Dashboard

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.4`
- **`distinguishing_axis`**：對照列範圍：VC2.2.2 and VC2.2.3 of the Vehicle Tab Labels and Order table
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之頁籤名與位置。**取材（下放包 15 §5.2）**：值取自 **SYS1 §2.4 之四欄表**（`Note | Specialty Feature | Tab Name | Order`，11 資料列，每列 4 欄），037 之扁平化格僅為索引。**⚠ `VC2.2.3` 之 Specialty Feature 欄於 SYS1 即為 `Performance Pages Race OptionsDrive Modes DXROff Road Pages…`——**多個功能名之間無分隔且有黏連**（`OptionsDrive`／`DXROff`），無法可靠切成個別功能名，故 ER 以「該列所載之功能」整體表述，**不自行拆分**（§8.4.1）。**為什麼這樣切**：037 已將表切為四 leaf，依 R-VC18 不合併。

### `SWE1-HMI-VC-007-03#1` — Trip, Camera App and Vehicle Info tab names and positions

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.4`
- **`distinguishing_axis`**：對照列範圍：VC2.2.4 to VC2.2.6 of the Vehicle Tab Labels and Order table
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之頁籤名與位置。**取材（下放包 15 §5.2）**：值取自 **SYS1 §2.4 之四欄表**（`Note | Specialty Feature | Tab Name | Order`，11 資料列，每列 4 欄），037 之扁平化格僅為索引。**為什麼這樣切**：037 已將表切為四 leaf，依 R-VC18 不合併。

### `SWE1-HMI-VC-007-04#1` — BEV, ARM Performance and Maserati Drive Modes tab names and positions

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.4`
- **`distinguishing_axis`**：對照列範圍：VC2.2.7 to VC2.2.9 of the Vehicle Tab Labels and Order table
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之頁籤名與位置。**取材（下放包 15 §5.2）**：值取自 **SYS1 §2.4 之四欄表**（`Note | Specialty Feature | Tab Name | Order`，11 資料列，每列 4 欄），037 之扁平化格僅為索引。**為什麼這樣切**：037 已將表切為四 leaf，依 R-VC18 不合併。

### `SWE1-HMI-VC-007-05#1` — Fuel Cell and Active Driving Assist tab names and positions

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.4`
- **`distinguishing_axis`**：對照列範圍：VC2.2.10 and VC2.2.11 of the Vehicle Tab Labels and Order table
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之頁籤名與位置。**取材（下放包 15 §5.2）**：值取自 **SYS1 §2.4 之四欄表**（`Note | Specialty Feature | Tab Name | Order`，11 資料列，每列 4 欄），037 之扁平化格僅為索引。**為什麼這樣切**：037 已將表切為四 leaf，依 R-VC18 不合併。

### `SWE1-HMI-VC-008#1` — Cameras tab surfaced when Camera App is equipped

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.5`
- **`distinguishing_axis`**：Camera 面向：頁籤之出現（對 -009 之 Controls 內去重）
- **`reasoning`**：**驗證目標**：配備 Camera App 時 Cameras 出現為頁籤。**關鍵情境條件**：車輛配備 Camera App。**未涵蓋 —— §8.4.2 之委派**：來源明文 `(see Camera HMI Logic and Flow)`，**Camera App 自身之任何行為皆不在本 TC 範圍**（開啟後之畫面、影像、切換等），其屬 Camera HMI Logic and Flow 之 SWE 需求。本 TC 僅驗頁籤之出現。

### `SWE1-HMI-VC-009#1` — Cameras entry removed from Controls when the tab is present

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.5.1`
- **`distinguishing_axis`**：Camera 面向：Controls 內去重（對 -008 之頁籤出現）
- **`reasoning`**：**驗證目標**：Cameras 頁籤存在時，Controls 內之 Cameras 項被移除。**關鍵情境條件**：同 -008 之觸發（配備 Camera App）。**為什麼這樣切**：本筆與 -008 為**同一觸發之兩個後果**，037 已拆為二 leaf —— 依 R-VC18 之一 leaf 一 TC 先例**不合併**（§8.2.2 之反向；下放包 14 §2.5 已裁）。

### `SWE1-HMI-VC-010#1` — Dashboard shows only equipped apps

- **`test_set`**：Category Structure　**`priority`**：P2　**`spec_ref`**：`…_2.6`
- **`distinguishing_axis`**：Dashboard 面向：依配備過濾（對 -011 之排序）
- **`reasoning`**：**驗證目標**：Dashboard 只顯示車輛實際配備之 app。**關鍵情境條件**：車輛配備部分而非全部 Dashboard apps —— 全配備則過濾與否無從區辨。**為什麼這樣切**：本 leaf 之標的為**過濾**，排序屬 -011。

### `SWE1-HMI-VC-011#1` — Dashboard content follows the table order

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.1`
- **`distinguishing_axis`**：Dashboard 面向：排序（對 -010 之過濾）
- **`reasoning`**：**驗證目標**：Dashboard 內容依表排序。**⚠ PENDING（IN §8.4.3）**：來源逐字為 `in order of the table`，**`the table` 未具名**。自上下文查：章 2 之唯一表為 §2.4 之 Vehicle Tab Labels and Order，但該表談的是 Vehicle Category 之頁籤，本節談的是 Dashboard 內之 apps —— **層級不同**；`HMI Settings List`（已在手）亦查無 Dashboard 內容之排序表。**不自行認定**（§8.4.1），以 `PENDING: DR-VC9 Dashboard content table` 佔位。**排序規則本身為需求無疑**，故本筆生成而非保留（R-VC22 之 a 段）。

### `SWE1-HMI-VC-012-01#1` — Single feature fills one full-width banner

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.2`
- **`distinguishing_axis`**：數量段：恰一個（對 -012-02 之二個以上）
- **`reasoning`**：**驗證目標**：橫向版面下，恰一個 feature 時之呈現。**關鍵情境條件**：恰一個 —— 取二個則落入 -012-02 之規則。**設計方法**：一／二／二以上為同一規則族之三段，本筆為其下界。

### `SWE1-HMI-VC-012-02#1` — Two features render as paired half banners

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.2`
- **`distinguishing_axis`**：數量段：恰兩個（下界；對 -012-03 之額外 feature）
- **`reasoning`**：**驗證目標**：橫向版面下，二個 feature 之配對半幅呈現與其左右次序。**⚠ 取「恰好兩個」為測試資料之依據（下放包 15 §3.2）**：**SYS1 §2.6.2 有三句，037 之 leaf 覆蓋第 1、3 句；第 2 句無對應 leaf。**第 2 句逐字為 `If there are two features, display them in the two half banners (topmost feature in the left, followed by the right).`，其在語意上被第 3 句之 `two or more` 涵蓋 —— 即**第 2 句為第 3 句之下界**，而規格對該下界有明文。依 §8.3，本 TC 以「恰好兩個」為測試資料；取三個以上則下界未被觸及。**test_item 上半取 SYS1 之完整句**（第 3 句），因 037 之 `012-02` 為該句之前半、`012-03` 為其續行（下放包 14 §2.2）。

### `SWE1-HMI-VC-012-03#1` — Additional features placed below the banner row

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.2`
- **`distinguishing_axis`**：數量段：三個以上之溢位置放（對 -012-02 之恰兩個）
- **`reasoning`**：**驗證目標**：橫向版面下，超出前二個之 feature 置於半幅列之下方。**test_item 上半取 SYS1 之完整句**：037 之 `012-03` 逐字為 `continuing with additional features below the banners (refer to PDO Graphics)` —— **小寫起首之句中片段**，單獨作為上半讀者無法理解其所指。依 R-S4「上半為需求／規格原句」，取完整句比取片段**更忠實於原句**（下放包 14 §2.2）。**本 leaf 之驗證範圍以括號下半為準**。**⚠ PENDING**：其細部版面 `refer to PDO Graphics` 之標的未到手，以 `PENDING: DR-VC9 PDO graphics` 佔位；**相對位置（在半幅列下方）可觀察**，故本筆生成而非保留（R-VC22 之 a 段）。

### `SWE1-HMI-VC-013-01#1` — Up to three features each get a single banner

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.3`
- **`distinguishing_axis`**：數量段：至三個（對 -013-02 之四個以上）
- **`reasoning`**：**驗證目標**：直向版面下，至三個 feature 時各佔一列單幅。**關鍵情境條件**：取三個 —— 該規則之上界（`up to three`），取一或二則未觸及上界。**設計方法**：三／四以上為相鄰之二段，本筆為前段之上界。

### `SWE1-HMI-VC-013-02#1` — Four features split into two singles and one shared row

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.3`
- **`distinguishing_axis`**：數量段：恰四個（下界；對 -013-03 之剩餘 feature）
- **`reasoning`**：**驗證目標**：直向版面下，四個 feature 之前二單幅、後二共列半幅。**關鍵情境條件**：恰四個 —— `four or more` 之下界（§8.3）。**test_item 上半取 SYS1 之完整句**：037 之 `013-02` **在句中補了句號並刪去 `and`**，使其看似完整句；其實與 `013-03` 同屬一句（下放包 14 §2.2）。取完整句以忠實於原句。**本 leaf 之驗證範圍以括號下半為準** —— 剩餘 feature 之磚塊置放屬 -013-03。

### `SWE1-HMI-VC-013-03#1` — Remaining features placed as tiles below the shared row

- **`test_set`**：Category Structure　**`priority`**：P3　**`spec_ref`**：`…_2.6.3`
- **`distinguishing_axis`**：數量段：五個以上之剩餘置放（對 -013-02 之恰四個）
- **`reasoning`**：**驗證目標**：直向版面下，超出前四個之 feature 以磚塊置於半幅列下方。**test_item 上半取 SYS1 之完整句**：037 之 `013-03` 逐字為 `follow with remaining features as tiles below the half banners` —— **小寫起首之句中片段**。同 -013-02 之處置，取完整句（下放包 14 §2.2）。**本 leaf 之驗證範圍以括號下半為準**。


## 批次 `batch2_settings_list`

### `SWE1-HMI-VC-040#1` — Left Menu Rail titled from the HMI Settings List

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_11.7`
- **`distinguishing_axis`**：版面：有左選單列（對 -041 之無）
- **`reasoning`**：**驗證目標**：有左選單列時，其標題取自 HMI Settings List 之 category。**素材**：`HMI Settings List`（已在手）之 `Settings` 分頁確載 36 個頂層 category（勘查 §2.4），**不需 PENDING**。**為什麼這樣切**：本 leaf 之標的為「有選單列」之情形；無選單列屬 -041。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 037 之 `(image: image13.png)` 為輔助說明，其文字層殘餘足以構成可測內容（勘查 §2.5），故照常生成。

### `SWE1-HMI-VC-041#1` — Categories become the first level without a rail

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_11.7.1`
- **`distinguishing_axis`**：版面：無左選單列（對 -040 之有）
- **`reasoning`**：**驗證目標**：無左選單列時，category 成為 Settings 之第一層。**關鍵情境條件**：版面不含左選單列 —— 與 -040 互斥之二分支。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 圖同 -040 之處置。

### `SWE1-HMI-VC-042-01#1` — Truncating options replaced by an arrow

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_11.8`
- **`distinguishing_axis`**：次層成因：截斷觸發（對 -042-02 之次層呈現）
- **`reasoning`**：**驗證目標**：選項文字會截斷時改以箭號，選項下推次層。**為什麼不拆**：「截斷 → 改箭號 → 選項下推」為一個後果鏈，拆開後前半之 ER 不完整（勘查 §2.7）。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 上半含來源之彎雙引號 `“>”`，依 R-VC23 逐字保留。

### `SWE1-HMI-VC-042-02#1` — Next level lists one option per line

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_11.8`
- **`distinguishing_axis`**：次層成因：次層之呈現（對 -042-01 之截斷觸發）
- **`reasoning`**：**驗證目標**：次層之每列一選項、每列一單選鈕。**為什麼這樣切**：-042-01 驗**成因**（截斷），本筆驗**結果之呈現**。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-043#1` — Selected option shown in parenthesis by the arrow

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_11.8.1`
- **`distinguishing_axis`**：層級：父層之目前值顯示（對 -042-02 之次層列表）
- **`reasoning`**：**驗證目標**：父層於箭號旁以括號顯示目前選項。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 上半含來源之彎雙引號 `“>”` **與方括號** `[Example: Language (English) >]` —— 依 R-VC23 逐字保留。**IN §11 之方括號禁令於 verbatim 上半讓位**（R-VC23 末段）：該禁令之立意為禁止作者使用方括號，非禁止引用含方括號之原文。

### `SWE1-HMI-VC-044#1` — Settings listed in HMI Settings List order

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.1`
- **`distinguishing_axis`**：清單屬性：順序與非編號呈現
- **`reasoning`**：**驗證目標**：清單依 HMI Settings List 之順序，且不以編號列表呈現。**素材**：該素材確載 318 筆編號 list item，列序即順序（勘查 §2.4），**不需 PENDING**。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-045#1` — Settings screen neither times out nor closes on selection

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.2`
- **`distinguishing_axis`**：持續性：閒置與選擇後皆不關閉
- **`reasoning`**：**驗證目標**：SETTINGS 畫面閒置不逾時、選擇後不關閉。**為什麼不拆**：二者為同一規則之二個情境（來源明文其目的為`in order to allow for more adjustments`），共用同一 ER 語意。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-01#1` — List item selected by pressing it

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：輸入路徑：觸控按壓（對 -046-05 之旋鈕）
- **`reasoning`**：**驗證目標**：按壓即選取。**為什麼這樣切**：本 leaf 為觸控主路徑；箭號開次層屬 -046-02、旋鈕路徑屬 -046-05。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-02#1` — Arrow item opens a further list

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：項目型態：帶箭號者（對 -046-04 之內嵌選項）
- **`reasoning`**：**驗證目標**：帶箭號之項目按壓後開啟次層清單。**未涵蓋**：來源明文 `unless otherwise stated in the Settings List` —— 個別設定之例外由該素材各自規定，**不在本 TC 範圍**（§8.4.2）。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-03#1` — Cursor starts at the first position

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：游標：首次進入之起始位置
- **`reasoning`**：**驗證目標**：首次進入瀏覽清單時游標在第一位。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-04#1` — Inline options touched directly

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：項目型態：內嵌調整選項（對 -046-02 之箭號）
- **`reasoning`**：**驗證目標**：列內之調整選項可直接觸碰變更。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-05#1` — Knob and arrows move the cursor

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：旋鈕行為：移動游標（對同 leaf 之按下選取）
- **`reasoning`**：**驗證目標**：旋鈕轉動與方向鍵按壓皆移動游標。**⚠ 拆分（IN §8.2.2；勘查 §2.7）**：本 leaf 載二個獨立行為 —— (i) 移動游標、(ii) 按下旋鈕選取並進入次層。**前者成而後者敗時，單一 TC 判準不明**，故拆為二筆。本筆為 (i)。二筆之 `Requirement or Design ID` 與 `specification_reference` 相同，其區分**僅在括號下半**。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-046-05#2` — Knob press selects and enters the next level

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.3`
- **`distinguishing_axis`**：旋鈕行為：按下選取並進入次層（對同 leaf 之移動游標）
- **`reasoning`**：**驗證目標**：按下旋鈕選取該項並進入次層或變更設定。**⚠ 拆分之第二筆**（見同 leaf 之前一筆）：本筆為 (ii) 按下選取。**設計方法**：游標態 → 次層／已變更之狀態轉換。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-047-01#1` — Knob toggles a single checkbox

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.1`
- **`distinguishing_axis`**：列型態：單一核取方塊（對 -047-02 之多單選鈕）
- **`reasoning`**：**驗證目標**：單一核取方塊列上按旋鈕即切換。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-047-02#1` — Sequential knob presses cycle radio options

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.1`
- **`distinguishing_axis`**：列型態：多單選鈕（對 -047-01 之單一核取方塊）
- **`reasoning`**：**驗證目標**：多單選鈕列上連續按旋鈕依左至右循環。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-047-03#1` — Knob enters down state and adjusts the value

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.1`
- **`distinguishing_axis`**：列型態：-/+ 選擇器之進入與調整（對 -047-04 之解除）
- **`reasoning`**：**驗證目標**：-/+ 列按旋鈕進入 down state，轉動左右增減其值。**為什麼不拆**：「按下進入 down state → 轉動增減」為**一個互動序列**，拆開後前半之 ER 不完整（勘查 §2.7）。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 上半含來源之直雙引號 「down」之直雙引號形態，依 R-VC23 逐字保留。

### `SWE1-HMI-VC-047-04#1` — Knob press or touch releases the down state

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.1`
- **`distinguishing_axis`**：列型態：-/+ 選擇器之解除（對 -047-03 之進入）
- **`reasoning`**：**驗證目標**：再按旋鈕或觸碰螢幕皆解除 down state。**為什麼不拆**：二個解除途徑為同一行為之二個等價輸入（§8.3 之等價類），其 ER 相同。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 上半含來源之直雙引號 「releases」／「released」之直雙引號形態，逐字保留。

### `SWE1-HMI-VC-048-01#1` — Cursor moves to the selected line

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.3.2`
- **`distinguishing_axis`**：選取後果：游標移動（對 -048-02 之確認音）
- **`reasoning`**：**驗證目標**：選取後游標移至該列。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-048-02#1` — Confirmation tone plays on a settings change

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.2`
- **`distinguishing_axis`**：確認音：正向（對同 leaf 之例外清單負向）
- **`reasoning`**：**驗證目標**：一般設定變更時播放確認音。**⚠ 拆分（IN §7；勘查 §2.2）**：本 leaf 同時載正向規則與三類例外。IN §7 明文列舉之支援項須配對至少一個不支援之負向 TC；且二個獨立失效（一般無音／例外有音）在單一 TC 下**分不出是哪一個**。本筆為正向。**FROP 註**：本 leaf 為 `FROP = Audio Management` 之唯一一筆，**表 A 之揭露須標其落於第 2 批且拆後為 2 筆**。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-048-02#2` — Exception settings play no confirmation tone

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.2`
- **`distinguishing_axis`**：確認音：例外清單負向（對同 leaf 之正向）
- **`reasoning`**：**驗證目標**：三類例外設定變更時**不**播放確認音。**⚠ 拆分之第二筆**（見同 leaf 之前一筆）：本筆為 IN §7 所要之負向配對。二筆之 `Requirement or Design ID` 與 `specification_reference` 相同，其區分**僅在括號下半**。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-049#1` — Press and hold repeats at one step per 200 ms

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.3.3`
- **`distinguishing_axis`**：適用對象：Clock 等五類（對 -050 之 Brightness）
- **`reasoning`**：**驗證目標**：五類設定之長按連續增減速率為每 200 ms 一步。**500 ms 為 spec-sourced 之門檻**，於同一 TC 內以步驟涵蓋其二側 —— **不拆**：拆開後各自之 ER 皆不完整（勘查 §2.3）。**sibling 區分（下放包 18 §4.3）**：本筆與 -050 之括號下半以**適用對象**區分（五類 vs Brightness），**不以速率區分** —— 速率是後果不是情境。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-050#1` — Brightness repeats at one step per 500 ms

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.4`
- **`distinguishing_axis`**：適用對象：Brightness（對 -049 之 Clock 等五類）
- **`reasoning`**：**驗證目標**：Brightness 之長按連續增減速率為每 500 ms 一步。**門檻與速率同值（500 ms）但意義不同** —— 前者為觸發門檻、後者為重複間隔；步驟已分別表述以免混讀。**sibling 區分**：括號下半以適用對象（Brightness）區分，非以速率。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-051-01#1` — Checkmark moves to the selected item

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.5`
- **`distinguishing_axis`**：結果分支：接受（對 -051-02 之拒絕）
- **`reasoning`**：**驗證目標**：選取後指示標移至該項。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-051-02#1` — Indicator returns on a rejected change

- **`test_set`**：Settings List　**`priority`**：P1　**`spec_ref`**：`…_12.5`
- **`distinguishing_axis`**：拒絕時機：仍在畫面（對 -051-03 之已離開）
- **`reasoning`**：**驗證目標**：設定被拒時指示標退回目前狀態。**為什麼這樣切**：本筆為**仍在畫面上**之拒絕；已離開畫面者屬 -051-03。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-051-03#1` — Popup shown when rejection arrives after leaving

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.5`
- **`distinguishing_axis`**：拒絕時機：已離開畫面（對 -051-02 之仍在畫面）
- **`reasoning`**：**驗證目標**：離開畫面後才收到拒絕時之補救彈窗與返回。**⚠ 記法（下放包 18 §3.2）**：本 leaf 之 `Description` 用**彎單引號** `‘Setting not saved, please try again’`，`Title` 用**直單引號** —— **二欄記法不對稱**。本 TC 之上半取自 `Description`，故 ER 之引用亦保留彎單引號，**二者不混用**（R-VC23(c)）。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-052-01#1` — Entry lands at the top of the list

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.6`
- **`distinguishing_axis`**：導覽方向：進入（對 -052-02 之返回）
- **`reasoning`**：**驗證目標**：進入 Settings 或次類別時視圖置頂。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-052-02#1` — Back returns to the entry position

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.6`
- **`distinguishing_axis`**：導覽方向：Back 返回（對 -052-01 之進入置頂）
- **`reasoning`**：**驗證目標**：Back 返回上一層之進入位置而非置頂。**關鍵情境條件**：返回前須先捲離進入位置 —— 否則與 -052-01 無法區辨。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-053#1` — Info icon shown for a setting with a definition

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.7`
- **`distinguishing_axis`**：圖示生命週期：出現（對 -054 之按壓後內容）
- **`reasoning`**：**驗證目標**：有 Definition 之設定其列上出現 info 圖示。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。 上半含來源之彎雙引號 `“info icon”`／`“i”`，依 R-VC23 逐字保留。圖 `image15.png` 為輔助說明，文字層殘餘足夠（勘查 §2.5）。

### `SWE1-HMI-VC-054#1` — Info popup carries description, telltale and options

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.7.1`
- **`distinguishing_axis`**：圖示生命週期：按壓後之彈窗內容（對 -053 之出現）
- **`reasoning`**：**驗證目標**：按 info 圖示開啟之彈窗含描述、telltale、選項三者。**條件性成分**：`telltale` 之來源明文為 `(if applicable)` —— ER 以 `where applicable` 表述，**不主張其恆存在**（§8.4.2）。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-055#1` — Info icon and popup available while in motion

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.7.2`
- **`distinguishing_axis`**：行進狀態：仍可用（非禁用）
- **`reasoning`**：**驗證目標**：行進中 info 圖示與其彈窗**仍可用**。**⚠ 拘束（下放包 18 §4.3）**：本筆為「行進中**仍可用**」，**非**「行進中禁用」—— ER **不得**寫成禁用或灰化。其失效形態為功能缺失（該可用而不可用），非安全風險。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-056-01#1` — Option changed from the info popup

- **`test_set`**：Settings List　**`priority`**：P2　**`spec_ref`**：`…_12.8`
- **`distinguishing_axis`**：彈窗互動：變更選項（對 -056-02 之關閉返回）
- **`reasoning`**：**驗證目標**：可自 info 彈窗直接變更設定選項。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。

### `SWE1-HMI-VC-056-02#1` — Popup closes and returns to the Settings List

- **`test_set`**：Settings List　**`priority`**：P3　**`spec_ref`**：`…_12.8`
- **`distinguishing_axis`**：彈窗互動：關閉返回（對 -056-01 之變更選項）
- **`reasoning`**：**驗證目標**：自彈窗選畢後關閉並返回設定清單。**設計方法**：彈窗開 → 關閉並返回清單之狀態轉換。**取材（R-VC23(c)／下放包 18 §3.2）**：上半取自 037 `Description`。


## 批次 `batch3_controls`

### `SWE1-HMI-VC-014#1` — Controls tab lists the eligible items

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.1`
- **`distinguishing_axis`**：清單屬性：成員資格（對 -015 之分組、-016 之條件出現）
- **`reasoning`**：**驗證目標**：Controls 頁籤列出車輛所配備之可列入項目。**⚠ PENDING（IN §8.4.3）**：來源逐字含 `(See table above)`，而**執行層以 SYS1 實測**：§3 僅為章標題、其下無表；章 3 之唯一表在 **§3.9（本節之後方）**；章 2 之 §2.4 雖有表但其為頁籤名與位置，與 Controls 項目無關。**即 `above` 於規格自身即不成立** —— 不自行認定（§8.4.1），以 `PENDING: DR-VC9 Controls table reference` 佔位。**範圍**：來源明文 `include, but are not limited to` —— **非窮舉**，故只驗所列項目為有效成員，不驗排他（§8.4.2）。`Screen Off` 之 `(only shown if vehicle is not equipped with Screen Off hard control)` 為條件式，其條件已入 Pre-Condition 之配備敘述。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-015#1` — Camera entries grouped together in Controls

- **`test_set`**：Controls　**`priority`**：P3　**`spec_ref`**：`…_3.1.1`
- **`distinguishing_axis`**：清單屬性：分組（對 -014 之成員資格）
- **`reasoning`**：**驗證目標**：二個以上攝影機項目時，其於 Controls 內成組。**關鍵情境條件**：恰為「二個以上」之下界 —— 僅一個時無「成組」可言。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-016#1` — Settings appears in Controls only when substituted

- **`test_set`**：Controls　**`priority`**：P3　**`spec_ref`**：`…_3.1.2`
- **`distinguishing_axis`**：清單屬性：條件式出現（對 -014 之常態成員）
- **`reasoning`**：**驗證目標**：Settings 僅在其頁籤被替換時才出現為 Controls 項目。**關鍵情境條件**：頁籤已被替換 —— 未替換則不應出現，但來源只述替換之情形，**不驗其反面**（§8.4.2：來源未述者不造）。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-017#1` — State changes shown on screen and in the status bar

- **`test_set`**：Controls　**`priority`**：P1　**`spec_ref`**：`…_3.2`
- **`distinguishing_axis`**：顯示面：畫面與狀態列（單一狀態變更之二個表面）
- **`reasoning`**：**驗證目標**：狀態變更同時反映於 CONTROLS 畫面與（適用時）狀態列。**條件性成分**：`where applicable` 為來源明文 —— ER 保留該條件，**不主張狀態列恆顯示**（§8.4.2）。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-018#1` — Settings shortcut available from the App drawer

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.3`
- **`distinguishing_axis`**：進入路徑：App drawer（對本批其餘之 Controls 頁籤）
- **`reasoning`**：**⚠ Pre-Condition 之更正（本輪自檢第 11 項所抓）**：前一版寫 `The App drawer is available on the head unit` —— **觸 §4.4 之二類禁項**：App drawer 為 HMI 之常駐介面（system defaults），且其開啟即本 TC 之步驟 1（step-controlled state）。已改為 feature initial state。 **驗證目標**：App drawer 提供 settings 之捷徑。**為什麼首步非 `ENTER_VC_TAB(Controls)`**：本 leaf 之進入路徑為 **App drawer**，非 Vehicle Category 頁籤 —— 取常數反而使該 TC 驗錯路徑。（同 `VC-001-02` 之情形：首步即受測動作之一部分。）**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-019-01#1` — Headrest Fold button shows no status

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.4`
- **`distinguishing_axis`**：按鍵屬性：無狀態顯示（對 -019-02 之按壓不高亮）
- **`reasoning`**：**驗證目標**：Headrest Fold 按鍵不顯示狀態，僅可按壓。**為什麼這樣切**：本 leaf 擁有「無狀態顯示」；「按壓不高亮」屬 -019-02。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-019-02#1` — Headrest Fold button does not highlight

- **`test_set`**：Controls　**`priority`**：P3　**`spec_ref`**：`…_3.4`
- **`distinguishing_axis`**：按鍵屬性：按壓不高亮（對 -019-01 之無狀態顯示）
- **`reasoning`**：**驗證目標**：按壓 Headrest Fold 不產生高亮。**⚠ 上半取 SYS1 §3.4 之整段（CONT 表，指涉型）**：037 之 Description 逐字為 `It will not highlight.` —— 為完整句，但其主詞 `It` 之先行詞（`Headrest fold`）在 `-019-01`。單獨作為上半讀者不知 `It` 何指。依 R-VC7 取 SYS1 §3.4 之整段（一段二句），使指涉可解；**本 leaf 之驗證範圍以括號下半為準**。> 注意其與 `025-02` 之別：本筆取整段是為**資訊量**（讓 `It` 可讀），非因 Title 越界 —— 其 Title 為情境脈絡（R-VC24）。

### `SWE1-HMI-VC-020#1` — Exhaust Sound status follows the system

- **`test_set`**：Controls　**`priority`**：P1　**`spec_ref`**：`…_3.5`
- **`distinguishing_axis`**：狀態來源：跟隨系統（實體控制之情形）
- **`reasoning`**：**驗證目標**：配備實體控制時，HMI 之 Loud/Quiet 狀態跟隨系統狀態。**關鍵情境條件**：來源明文 `in the event the vehicle is equipped with a hard control` —— 未配備者不在範圍。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-021#1` — Glove Box Lock opens the Privacy Lock popup

- **`test_set`**：Controls　**`priority`**：P1　**`spec_ref`**：`…_3.6`
- **`distinguishing_axis`**：委派邊界：彈窗開啟（Glove Box 行為屬 pilot）
- **`reasoning`**：**驗證目標**：按下 Glove Box Lock 開啟 Privacy Lock 彈窗。**⚠ PENDING（IN §8.4.3）**：來源逐字為 `open PUXXXX (Privacy Lock)` —— **`PUXXXX` 於規格原文即為字面**，非實 id（DR-VC1）。不得代以語意相近者，以 `PENDING: DR-VC1 Privacy Lock popup ID` 佔位。**未涵蓋 —— §8.2.1 之委派**：來源明文 `Refer to Glove Box Lock section for behavior`。**Glove Box 之行為由 pilot 之 `026`~`033` 擁有**，本 TC 之 ER **不驗置物箱之啟用／停用／PIN 任何行為**，僅驗彈窗之開啟。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-022#1` — Redundant content removed with a lower screen

- **`test_set`**：Controls　**`priority`**：P3　**`spec_ref`**：`…_3.7`
- **`distinguishing_axis`**：配備條件：下方非可動螢幕
- **`reasoning`**：**驗證目標**：配備下方非可動螢幕時，重複內容自主機移除。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-023#1` — Electrochromic returns to tinted each key cycle

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.8`
- **`distinguishing_axis`**：狀態面向：跨鑰匙循環之回復（對 -024 之即時不可用）
- **`reasoning`**：**驗證目標**：電控玻璃之狀態不跨鑰匙循環保留，回復為 tinted。**關鍵情境條件**：循環前須置於非 tinted —— 否則回復與否無法區辨。**記法**：來源之彎雙引號 `“tinted”` 依 R-VC23 逐字保留。**設計方法**：跨鑰匙循環之狀態轉換。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-024#1` — Electrochromic greyed out when the roof is open

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.8.1`
- **`distinguishing_axis`**：狀態面向：車頂開啟時之不可用（對 -023 之鑰匙循環）
- **`reasoning`**：**驗證目標**：車頂開啟時電控玻璃不可用且按鍵灰化。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-025-02#1` — Controls button statuses map as the table defines (02)

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.9`
- **`distinguishing_axis`**：對照列範圍：Table rows for Rear Sunshade, Screen Off and the camera entries
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之按鍵狀態語意。**⚠ 上半必須取 `Description`，不得取 Title**（R-VC24 已判其 Title 為**行為主張**型越界：Title 之 `Map … to their respective camera-feature shortcuts` 把 `Aux 1`／`Aux 2` 納為受詞，而該二項屬 `-03` 之 Description —— 取 Title 即違 IN §8.2.1）。**表格取材（勘查 §3.7）**：值之權威為 **SYS1 §3.9 之二欄表**（`Button | Button Status`，28 資料列），037 之扁平化格僅為索引。**逐字引用整格，不自行拆分**；ER 逐列表述 —— 此為勘查 (g) 判其不拆之前提。  **取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-025-03#1` — Controls button statuses map as the table defines (03)

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.9`
- **`distinguishing_axis`**：對照列範圍：Table rows for Mirror Dimmer, Headrest Fold rows, Power Side Step, Aux cameras and Outlet
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之按鍵狀態語意。**表格取材（勘查 §3.7）**：值之權威為 **SYS1 §3.9 之二欄表**（`Button | Button Status`，28 資料列），037 之扁平化格僅為索引。**逐字引用整格，不自行拆分**；ER 逐列表述 —— 此為勘查 (g) 判其不拆之前提。 **⚠ 括號項**：`(Power Side Step)` 之按鍵名**本身帶括號**，SYS1 §3.9 未給任何說明。依勘查 §3.6 逐字保留，**不自行詮釋其含義**。同型之括號項另有三個在 `-04` —— **四個括號項跨越二個 leaf**，其含義若日後查明，影響面不止一筆。 **取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-025-04#1` — Controls button statuses map as the table defines (04)

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.9`
- **`distinguishing_axis`**：對照列範圍：Table rows for the passenger screen controls, Exhaust Sound, Glove Box Lock, Start and Stop and Settings
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之按鍵狀態語意。**表格取材（勘查 §3.7）**：值之權威為 **SYS1 §3.9 之二欄表**（`Button | Button Status`，28 資料列），037 之扁平化格僅為索引。**逐字引用整格，不自行拆分**；ER 逐列表述 —— 此為勘查 (g) 判其不拆之前提。 **⚠ 括號項**：`(Pass Screen Screen Off)`／`(Pass Screen Power Off)`／`(Exhaust Sound)` 三個按鍵名**本身帶括號**，SYS1 未給說明 —— 逐字保留，不詮釋（勘查 §3.6）。 **取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。

### `SWE1-HMI-VC-025-05#1` — Controls button statuses map as the table defines (05)

- **`test_set`**：Controls　**`priority`**：P2　**`spec_ref`**：`…_3.9`
- **`distinguishing_axis`**：對照列範圍：Table rows for Bed Lowering, blind spot views, Electrochromic, Cabrio, Memory Seats and Ambient Lighting
- **`reasoning`**：**驗證目標**：本 leaf 所載對照列之按鍵狀態語意。**表格取材（勘查 §3.7）**：值之權威為 **SYS1 §3.9 之二欄表**（`Button | Button Status`，28 資料列），037 之扁平化格僅為索引。**逐字引用整格，不自行拆分**；ER 逐列表述 —— 此為勘查 (g) 判其不拆之前提。 **⚠ 二處外部委派（§8.4.2）**：`Cabrio | Opens Cabrio pop up (see Cabrio requirements)` 與 `Memory Seats | Opens Memory Seats second level screen (see Virtual Memory Seats L&F)`。本 TC 之範圍**僅及於「按下該鈕後有對應之彈窗／次層畫面開啟」，不驗其內容**。**二者性質不同**：Cabrio 之標的（章 8／9）**在本 feature 內但 037 零涵蓋**（R-VC3 表 B 之 17 節，待 DR-VC3）；Memory Seats 之標的在**他 feature 之規格**且不在素材清單（R-VC10）。 **取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。


## 批次 `batch4_settings_behavior`

### `SWE1-HMI-VC-034-01#1` — Settings absent from the vehicle are not listed

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.1`
- **`distinguishing_axis`**：不適用者之處置：隱藏（對 -02 之灰化）
- **`reasoning`**：**驗證目標**：不屬於該車之設定不出現於其 Settings 清單。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。**為什麼這樣切**：§11.1 之二規則由 037 拆為 -01／-02 二 leaf，本筆只驗「隱藏」，灰化屬 -02（§8.2.1）。**範圍**：不驗該設定於其他車型是否出現 —— 那是他車之組態，非本需求所斷言（§8.4.2）。

### `SWE1-HMI-VC-034-02#1` — Key Off greys out unavailable settings

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.1`
- **`distinguishing_axis`**：不適用者之處置：灰化（對 -01 之隱藏）
- **`reasoning`**：**驗證目標**：車輛有、但 key-off 下不可用之設定，於 key-off 呈灰而非消失。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 進入路徑之拘束（上繳包 22 §2.3）**：SYS1 §13.1 於 Key Off／Timed Mode／ACC 擋住 **Settings 頁籤**，故本筆**不得以該頁籤進入**，否則於待測狀態下不可執行。改經 §13.2 明文於 Key Off 可用之 Phone screens 進入 Phone settings。§11.1 與 §13.1 **非衝突** ——一管入口、一管入口之後的呈現，§13.5 之 `tab or a Settings category` 為旁證，故不發 DR。**⚠ 測試資料未具名（§8.4.1）**：`HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)` 之 `Settings` 分頁已實測搜尋 `key-off`／`key off`／`ignition`／`ACC`／`Timed Mode`（命中 21 列）與 `grey`／`gray`（命中 15 列）—— **其所載之灰化成因為頭燈關閉、Display Mode 為 Auto、sync 選項、Steering only、車輛行進中，無一為 key-off**；該清單無「key-off 可用性」之欄位。故不自行指定某一設定，以規格語言之通稱表述之。

### `SWE1-HMI-VC-035-01#1` — Restore defaults resets the settings

- **`test_set`**：Settings Behavior　**`priority`**：P1　**`spec_ref`**：`…_11.2`
- **`distinguishing_axis`**：回復預設之三段：值之生效（對 -02 之確認彈窗、-03 之取消）
- **`reasoning`**：**驗證目標**：於回復預設之提示選 Yes，設定確實回到預設值。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼含前後二次記錄**：「回到預設」為值之變化，無變化前之值即無從判其已變（§5.6 之 baseline）。

### `SWE1-HMI-VC-035-02#1` — Confirmation pop-up after a reset to default

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.2`
- **`distinguishing_axis`**：回復預設之三段：確認彈窗（對 -01 之值生效、-03 之取消）
- **`reasoning`**：**驗證目標**：回復完成後顯示 `Settings reset to default` 之彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：本 leaf 之 Description 用彎單引號 `‘…’`、Title 用直單引號 `'…'`。**取 Description 一欄，不混用**；上半之彎單引號依 R-VC23 逐字保留，ER 之彈窗文字為作者散文，依 R-VC23(b) 用直雙引號。

### `SWE1-HMI-VC-035-03#1` — Cancel leaves the settings unchanged

- **`test_set`**：Settings Behavior　**`priority`**：P0　**`spec_ref`**：`…_11.2`
- **`distinguishing_axis`**：回復預設之三段：取消（對 -01 之值生效、-02 之確認彈窗）
- **`reasoning`**：**驗證目標**：於回復預設之提示選 Cancel，返回前一畫面且設定未變。**⚠ 取材為 R-VC25 之例外路徑（Title），三件逐筆記**：(a) **理由** —— 本筆與 `036-02` 之 Description **逐字相同**（`Selecting cancel will take the user back to the previous screen.`），而其 P0 之依據 `without changing any settings` **只在 Title**；Description 未載該條件，取之則本 TC 之驗證標的落空（A-VC10 第一面）。(b) **R-VC24 判別結果** —— Title 之謂語為 `returns the user…`，為本 leaf 之行為；`restore-defaults prompt` 用以定位是哪一個提示，屬**情境脈絡**。(c) **非行為主張** —— 由 (b) 滿足。**ER 之 baseline（§5.6）**：「未變」無變前之值即不可判，故第 2 步記錄、第 4 步回讀。**測試資料之三筆為測試設計參數**，非來源所載（§8.4.1）。

### `SWE1-HMI-VC-036-01#1` — Clear personal data confirmed

- **`test_set`**：Settings Behavior　**`priority`**：P1　**`spec_ref`**：`…_11.3`
- **`distinguishing_axis`**：清除個人資料之二支：執行（對 -02 之取消）
- **`reasoning`**：**驗證目標**：選 Yes 清除個人資料，並顯示帶右上 X 之確認彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Description 用彎單引號、Title 用直單引號 —— 取 Description 一欄。**⚠ R-VC14(b) 之分歧揭露**：037 給 Medium，本地初判 P0（資料遺失風險），**改判 P1** —— 本筆之失效為「該清而未清」，資料仍在，**非 data-loss**；其風險為隱私外洩，依 R-VC11(c) 記於本欄而**不入 priority**。取消支（-02）之失效才是靜默清除，故其為 P0。**為什麼一 TC 不拆**：清除與彈窗為同一觸發（按 Yes）之二個後果，IN §398 明文不拆，列為二條 ER。

### `SWE1-HMI-VC-036-02#1` — Cancel leaves the personal data intact

- **`test_set`**：Settings Behavior　**`priority`**：P0　**`spec_ref`**：`…_11.3`
- **`distinguishing_axis`**：清除個人資料之二支：取消（對 -01 之執行）
- **`reasoning`**：**驗證目標**：於清除個人資料之提示選 Cancel，返回前一畫面且資料未被清除。**⚠ 取材為 R-VC25 之例外路徑（Title），三件逐筆記**：(a) **理由** —— 本筆與 `035-03` 之 Description 逐字相同，而其 P0 之依據 `without clearing any data` **只在 Title**（A-VC10 第一面）。(b) **R-VC24 判別結果** —— Title 之謂語為 `returns the user…`，為本 leaf 之行為；`clear-personal-data prompt` 為**情境脈絡**。(c) **非行為主張** —— 由 (b) 滿足。**與 `035-03` 之區分**：二筆之 Title 僅以提示之別區分（restore-defaults／clear-personal-data），括號下半即以此區分。**ER 之 baseline（§5.6）**：「未被清除」須有清除前之內容可比。

### `SWE1-HMI-VC-037-01#1` — Only one suspension mode is on

- **`test_set`**：Settings Behavior　**`priority`**：P1　**`spec_ref`**：`…_11.4`
- **`distinguishing_axis`**：互斥之靜態面：任一時刻之狀態（對 -02 之切換動作）
- **`reasoning`**：**驗證目標**：懸吊模式於任一時刻至多一者為開。**取材（R-VC25）**：上半取自 037 `Description`。**一靜一動之區分（下放包 20 §3.4／上繳包 22 §5.2）**：本筆驗**規則**（同時僅一），`-02` 驗**行為**（開一關餘）；括號下半以此區分。本筆之第 3 步逐一按過每個模式，其驗的是每次之後不變式仍成立，非某一次之轉換結果。

### `SWE1-HMI-VC-037-02#1` — Activating a mode turns the others off

- **`test_set`**：Settings Behavior　**`priority`**：P1　**`spec_ref`**：`…_11.4`
- **`distinguishing_axis`**：互斥之動態面：開一關餘之轉換（對 -01 之不變式）
- **`reasoning`**：**驗證目標**：開啟一個懸吊模式時，其餘自動關閉。**取材（R-VC25）**：上半取自 037 `Description`。**ER 之 baseline（§5.6，下放包 23 §3.2）**：「其餘被關掉」須先知道原本哪些是開的 —— 無 baseline 則「餘者為 off」與「餘者本來就 off」不可分。**一靜一動之區分**：本筆為行為，`-01` 為規則。

### `SWE1-HMI-VC-038-01#1` — Progress pop-up on a language change

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：語言變更五段：彈窗之出現（對 -02 之語言、-03 之持續、-04 之返回、-05 之清單呈現）
- **`reasoning`**：**驗證目標**：選擇變更語言時出現進度彈窗，其文字為所載者。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Description 用彎單引號、Title 用直單引號 —— 取 Description 一欄。ER 之彈窗文字含來源之刪節號 `…`，逐字保留（R-VC23(c)）；其引號為作者散文之直雙引號（R-VC23(b)）。

### `SWE1-HMI-VC-038-02#1` — Pop-up appears in the new language

- **`test_set`**：Settings Behavior　**`priority`**：P3　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：語言變更五段：彈窗之呈現語言（對 -01 之出現）
- **`reasoning`**：**驗證目標**：進度彈窗以新選之語言呈現，非固定英文。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 `Description` 之 `It` 其先行詞（pop-up）在 s1，取單句則指涉無解。**登記 SYS1 §11.5 範圍 `1-2`，33 token，未逾 R-3 之 50**（profile §9.2 層次 1 之預設處置對本筆成立，故不採第三處置類）。上半即 s1＋s2 之逐字，收斂第 16 項逐字比對。

### `SWE1-HMI-VC-038-03#1` — Pop-up stays until the user presses X

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：離開條件：使用者動作（對完成路徑之時間性離開）
- **`reasoning`**：**驗證目標**：彈窗持續顯示，直到使用者按 X 才離開。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2，下放包 23 §2.2）**：`This pop-up` 之先行詞在 SYS1 §11.5 s1，而連續 `1-3` 為 **54 token，逾 R-3 之 50**（profile §10 之工作定義）；非連續 `1,3` 為 42 但破壞 verbatim 之連續性，使第 7b 項與第二層之子串判準對本筆失效。**採單句 s3 ＋ 指涉由 TC 結構承載** —— 其先行詞「語言變更彈窗已顯示」**本即本 TC 驗證持續性之前提**，不解指涉也必須建立它。CONT 登記 `resolution=PC`／`resolution_key=pop-up`，**第三檢查點驗其 pre_conditions 確含該詞**。**⚠ 拆 2（下放包 24 §1.3 之裁定，推翻上繳包 23 §5 之不拆判讀）**：上繳包 23 我判二個離開條件為同一規則之二個邊界而不拆，**分析層以覆蓋洞推翻** —— 不拆之實質後果是「系統完成時彈窗不消失」這個失效**現有 16 筆無一會 FAIL**（本筆之 Procedure 只走 X 路徑；`038-05` 未完成支第 3 步記錄的是語言清單非彈窗）。**判準不是「二觸發」之形式論，是「這個失效哪一筆會 FAIL」。**本筆改為 X 路徑，完成路徑另立一筆。

### `SWE1-HMI-VC-038-03#2` — Pop-up leaves when updating completes

- **`test_set`**：Settings Behavior　**`priority`**：P2　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：離開條件：系統完成（對 X 路徑之使用者動作離開）
- **`reasoning`**：**驗證目標**：系統完成語音命令變更時，彈窗自行離開，不需使用者動作。**⚠ 本筆為下放包 24 §1.3 所補之覆蓋洞**：第 4 批原 16 筆中，「完成時彈窗不消失」這個失效**無一筆會 FAIL**。**取材同 X 路徑筆**：第三處置類，單句 s3，CONT 登記 `resolution=PC`／`resolution_key=pop-up`。**連帶之實益（下放包 24 §1.3）**：`038-05` 未完成支第 3 步等到完成後驗「選項不再灰」—— 若彈窗該消失而未消失，它可能正擋著清單，該步之 FAIL 原因會混淆（灰化未解 vs 彈窗未關）。本筆使「完成 → 彈窗消失」成為該步之明確前置。**第 2 步之 `without pressing any control`**：離開須由系統完成所致，不得由使用者動作促成 —— 否則本筆與 X 路徑筆驗的是同一件事。

### `SWE1-HMI-VC-038-04#1` — Return to the language settings screen

- **`test_set`**：Settings Behavior　**`priority`**：P3　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：語言變更五段：彈窗關閉後之落點（對 -03 之持續）
- **`reasoning`**：**驗證目標**：彈窗結束後使用者返回語言設定畫面。**⚠ 第一層偽陰性之第二實例（上繳包 22 §6）**：037 之 `The user is **then** taken back…` 以 `then` 承接前句，但首字大寫、非代名詞起首 —— 二特徵皆不命中，候選偵測看不到，由勘查之 SYS1 對照發現。**取材為第三處置類**：`then` 所承接之「按 X 或系統完成」**即本 TC 之必然步驟**，故取單句 s4，CONT 登記 `resolution=Step`／`resolution_key=pop-up`，**第三檢查點驗其 test_procedure 確含該詞**。

### `SWE1-HMI-VC-038-05#1` — Language screen normal once updating completes

- **`test_set`**：Settings Behavior　**`priority`**：P3　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：更新完成與否：完成支（對未完成支之勾選＋灰化）
- **`reasoning`**：**驗證目標**：語音命令更新完成後，語言設定畫面呈現如常。**取材（R-VC25）**：上半取自 037 `Description`（含 s5＋s6 二句）。**⚠ 拆 2 之理由（IN §8.2.2／§5.2，上繳包 22 §5.1）**：s5 自身即二個 if 分支（完成 → 如常；未完成 → 現用語言勾選、其餘灰化），二者為**二個獨立失效**，單一 TC 之判準不明；且 IN §5.2 禁一 TC 內寫條件分支。二筆同 req_id，括號下半以分支區分（IN §8.2.2：sub-id 數 ≠ TC 數）。

### `SWE1-HMI-VC-038-05#2` — Other languages grey while updating runs

- **`test_set`**：Settings Behavior　**`priority`**：P3　**`spec_ref`**：`…_11.5`
- **`distinguishing_axis`**：更新完成與否：未完成支（對完成支之如常呈現）
- **`reasoning`**：**驗證目標**：更新未完成時，現用語言勾選、其餘灰化，且灰化持續至完成。**取材（R-VC25）**：上半同完成支，取自 037 `Description`。**為什麼第 3 步在本支而不在完成支**：s6 之「持續至完成」是對**未完成**狀態之時間性斷言，其終點才是完成；把它放到完成支則無灰化可觀察。**與完成支之區分**：括號下半載其分支條件。

### `SWE1-HMI-VC-039#1` — Chinese language change pop-up

- **`test_set`**：Settings Behavior　**`priority`**：P3　**`spec_ref`**：`…_11.6`
- **`distinguishing_axis`**：語言之特定值：中文（對 -038 各筆之語言無關流程）
- **`reasoning`**：**驗證目標**：語言改為中文時顯示所載之彈窗，帶 X/Close 按鍵。**取材（R-VC25）**：上半取自 037 `Description`。**記法（R-VC23）**：上半之彎雙引號 `“…”` 與 `X/Close` 之斜線逐字保留；ER 之彈窗文字為作者散文，依 R-VC23(b) 用直雙引號，其內容含來源之三點刪節 `...` 逐字。**⚠ 範圍（§8.4.2）**：來源之 `Driver screen only will display language in Chinese` 為彈窗**文字之內容**，其所述之叢集（Driver screen）中文顯示屬**叢集側之行為**，非本 HMI 需求所斷言 —— 本筆之 ER 限於 HU 彈窗之出現與其文字，叢集顯示委派記於本欄，不入 ER。


## 批次 `batch5_ignition_availability`

### `SWE1-HMI-VC-057#1` — Settings tab unavailable in three ignition states

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.1`
- **`distinguishing_axis`**：頁籤本身之可用性（對 058-* 之彈窗、059/060/061 之他路徑）
- **`reasoning`**：**驗證目標**：Settings 頁籤於 Key Off／Timed Mode／ACC 三個狀態皆不可用。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼三狀態同一筆（R-VC26）**：三者**不互相消耗** —— 點火狀態可循環切換，走完其一不使另一之情境消失，故各以一個步驟／一條 ER 涵蓋即可，不拆。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。

### `SWE1-HMI-VC-058-01#1` — Pop-up on a blocked Settings tab attempt

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.1.1`
- **`distinguishing_axis`**：嘗試進入之後果：彈窗出現（對 -02 之持續、-03 之關閉落點）
- **`reasoning`**：**驗證目標**：於三個受阻狀態嘗試進入 Settings 頁籤時，顯示所載文字之彈窗，帶 OK 與 X 二個選項。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Title 用直單引號、Description 用彎單 `‘…’` 與彎雙 `“…”` —— **取 Description 一欄，不混用**。**為什麼彈窗與其二選項同一筆**：同一觸發（嘗試進入）之數個後果，IN §398 明文不拆，列為 ER 之內容。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### `SWE1-HMI-VC-058-02#1` — Blocked-tab pop-up does not time out

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.1.1`
- **`distinguishing_axis`**：嘗試進入之後果：彈窗不逾時（對 -01 之出現、-03 之關閉）
- **`reasoning`**：**驗證目標**：該彈窗不會自行逾時消失。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 之 `This pop-up` 其先行詞在 SYS1 §13.1.1 s1。**s1+s2 共 43 token，未逾 R-3 之 50** → **profile §9.2 層次 1 之預設處置成立，不採第三處置類**（層次不得跳層）。與 `064-02` 之對照值得記：二筆句型幾乎相同，而 `064-02` 因其 s1 較長（42 vs 37 token）落入層次 2。**觀察期之 5 分鐘為測試設計參數，非來源所載**（§8.4.1）——來源未給逾時值。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### `SWE1-HMI-VC-058-03#1` — Closing the blocked-tab pop-up with X

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.1.1`
- **`distinguishing_axis`**：關閉之控制項：X（對 OK 支之同一落點）
- **`reasoning`**：**驗證目標**：以 X 關閉該彈窗，返回嘗試進入時所在之畫面。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `Closing **the pop-up**…` 為**定冠詞回指**，其先行詞在 s1；整段 s1-s3 為 **68 token，逾 R-3 之 50**，故不取整段。單句 s3 ＋ 指涉由 TC 結構承載，CONT 登記 `resolution=PC`／`resolution_key=pop-up`。**⚠ 本筆為第一層之偽陰性**（定冠詞回指，非代名詞起首）——由勘查 (d) 之 SYS1 對照發現，非由候選偵測發現（profile §9.4.1）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**追溯佐證（不入 ER）**：`Pop Up List HMI R1 (26PI)` `Main` 第 239 列 `PU0237` 之 `String/Popup Message` 與本筆之彈窗文字逐字相同，其 `Timeout (sec)` = `N/A`、`Exit Conditions` = `<X>`／`<OK>`。**PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載），故只入本欄作追溯，不入 ER（沿 DR-VC1 對 `VC-021` 之分寸）。

### `SWE1-HMI-VC-058-03#2` — Closing the blocked-tab pop-up with OK

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.1.1`
- **`distinguishing_axis`**：關閉之控制項：OK（對 X 支之同一落點）
- **`reasoning`**：**驗證目標**：以 OK 關閉該彈窗，返回嘗試進入時所在之畫面。**取材同 X 支**（第三處置類，單句 s3）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**二支之落點相同而控制項不同** —— 括號下半以控制項區分。

### `SWE1-HMI-VC-059-01#1` — Phone settings reached through the Phone screens

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.2`
- **`distinguishing_axis`**：Phone settings 之路徑（對 -02 之點火狀態）
- **`reasoning`**：**驗證目標**：使用者可經 Phone screens 進入 Phone settings。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼與 -02 分立**：本筆驗**路徑存在**，`-02` 驗**該路徑於受阻狀態仍可用** —— 二者之失效不同（路徑不通 vs 路徑於 Key Off 被擋）。

### `SWE1-HMI-VC-059-02#1` — Phone settings available in Key Off and ACC

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.2`
- **`distinguishing_axis`**：Phone settings 之點火狀態（對 -01 之路徑）
- **`reasoning`**：**驗證目標**：Phone settings 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。**二狀態不互相消耗**（R-VC26）—— 不拆，各以步驟／ER 涵蓋。

### `SWE1-HMI-VC-060-01#1` — Audio settings reached through the Media

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.3`
- **`distinguishing_axis`**：Audio settings 之路徑（對 -02 之點火狀態）
- **`reasoning`**：**驗證目標**：使用者可經 Media 進入 Audio settings。**取材（R-VC25）**：上半取自 037 `Description`。**來源用語逐字為 `through the Media`**（非 `Media screens`）——上半保留其原字；Procedure 之 `the Media screens` 為作者散文，其所指同一（§13.3 之標的）。

### `SWE1-HMI-VC-060-02#1` — Audio settings available in Key Off and ACC

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.3`
- **`distinguishing_axis`**：Audio settings 之點火狀態（對 -01 之路徑）
- **`reasoning`**：**驗證目標**：Audio settings 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**引上繳包 22 §2 之路徑解**：§13.1 擋的是 Settings 頁籤這一條進入路徑，§13.2–§13.4 所載之他路徑於 Key Off／ACC 明文可用 —— `057` 與本筆**並存不悖**，非例外，**不發 DR**。

### `SWE1-HMI-VC-061#1` — Software Updates available in Key Off and ACC

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.4`
- **`distinguishing_axis`**：Software Updates 之點火狀態（對 059/060 之已載路徑）
- **`reasoning`**：**驗證目標**：Software Updates 於 Key Off 與 ACC 仍可用。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC19／DR-VC10(二)）**：章 13 為三個「他路徑仍可用」之需求給出路徑，**獨缺本筆** —— `059-*` 有 §13.2 之 `through the Phone screens`、`060-*` 有 §13.3 之 `through the Media`，而 §13.4 **只斷言可用，未載經何路徑**。**執行層之實測**：SYS1 全表搜 `Software Update|FOTA|Wi-Fi` **僅命中 §13.4／§13.4.1／§13.4.2**，三節皆無路徑；`HMI Settings List` `Settings` 分頁之 `Software Updates` 為**第 27 類**（第 650 列），即在被 §13.1 擋住的頁籤後方，其第 651 列作 `See Software Updates Logic and Flow for logic` ——**委派至我方未持有之文件**。**為何不以通稱表述帶過（下放包 25 §2.1）**：`034-02` 所缺者為**測試資料**，通稱後 Procedure 仍可執行；本筆所缺者為**進入路徑**，「經一條於 Key Off 仍可用之路徑進入」**不是可執行的步驟**。

### `SWE1-HMI-VC-062-01#1` — Wi-Fi download setting blocked while in motion

- **`test_set`**：Ignition Availability　**`priority`**：P0　**`spec_ref`**：`…_13.4.1`
- **`distinguishing_axis`**：攔阻之觸發：按下設定（對 063-01 之流程中起步）
- **`reasoning`**：**驗證目標**：行進中按下 Wi-Fi 下載設定時，操作被攔阻並顯示彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC18／DR-VC10(一)）**：彈窗文字二源相左 —— SYS1 §13.4.1／§13.4.2 與 037 作 `“**Feature** not available while vehicle is in motion”`；`Pop Up List` 第 93 列 `PU0091` 之 `String/Popup Message` 作 `**Function** not available while vehicle is in motion**.**`（含句末句點），`HMI Settings List` 第 150 列亦作 `Function`。**二份獨立來源對規格一份**，且該欄位就是彈窗的字。**不自行擇一**（§8.4.1）。**不需 §5.6 之 baseline（下放包 25 §三）**：本筆攔的是**動作**（設定未被進入）而非**值** —— 與 `035-03` 之值比對不同型，「未進入」由該次操作之結果直接可判，不需操作前之基準值。**⚠ 記法不對稱（A-VC10 第三面）**：Title 直單、Description 彎單＋彎雙 —— 取 Description 一欄。**`Software Downloads Over Wi-Fi` 之大小寫**：`HMI Settings List` 第 651 列作 `over`（小寫 o），SYS1／037 作 `Over` —— **依 R-VC7 以 SYS1／037 為準**，記明以免誤判為抄錯。

### `SWE1-HMI-VC-062-02#1` — OK on the in-motion pop-up returns to the Settings list

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.4.1`
- **`distinguishing_axis`**：離開之控制項：OK（對 X 支之同一落點）
- **`reasoning`**：**驗證目標**：按 OK 離開行進中攔阻彈窗，返回 Settings 清單。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 之 `If **they** press…` 其代名詞**非句首**（句首為 `If`），且其所按之標的為 s1 之彈窗。**s1+s2 共 46 token，未逾 R-3 之 50** → **profile §9.2 層次 1**，取 s1-s2，不採第三處置類。**⚠ 本筆為第一層之偽陰性**（非句首代名詞）——由勘查 (d) 發現。**R-VC24 判別**：Title 含 `Software Downloads Over Wi-Fi`（屬 `062-01`），其謂語為 `return them to the Settings list`（本 leaf 之行為），該詞用以定位是哪一個 in-motion 彈窗 —— **情境脈絡，非行為主張，非越界**。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。**PENDING 置於 Procedure 而非 ER**：本筆之驗證標的為**返回落點**，非彈窗文字（後者屬 `062-01`）；文字於此只用於**辨識按的是哪個彈窗**，故置於步驟。另立 ER 斷言其文字會與 `062-01` 之驗證點重複（IN §527）。

### `SWE1-HMI-VC-062-02#2` — X on the in-motion pop-up returns to the Settings list

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.4.1`
- **`distinguishing_axis`**：離開之控制項：X（對 OK 支之同一落點）
- **`reasoning`**：**驗證目標**：按 X 離開行進中攔阻彈窗，返回 Settings 清單。**取材同 OK 支**（層次 1，s1-s2）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### `SWE1-HMI-VC-063-01#1` — Motion during a FOTA via Wi-Fi flow raises the block

- **`test_set`**：Ignition Availability　**`priority`**：P0　**`spec_ref`**：`…_13.4.2`
- **`distinguishing_axis`**：攔阻之觸發：流程中起步（對 062-01 之按下設定）
- **`reasoning`**：**驗證目標**：FOTA via Wi-Fi 流程中車輛起步時，顯示攔阻彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ PENDING（IN §8.4.3；A-VC18／DR-VC10(一)）**：彈窗文字二源相左 —— SYS1 §13.4.1／§13.4.2 與 037 作 `“**Feature** not available while vehicle is in motion”`；`Pop Up List` 第 93 列 `PU0091` 之 `String/Popup Message` 作 `**Function** not available while vehicle is in motion**.**`（含句末句點），`HMI Settings List` 第 150 列亦作 `Function`。**二份獨立來源對規格一份**，且該欄位就是彈窗的字。**不自行擇一**（§8.4.1）。**與 `062-01` 之區分**：`062-01` 之觸發為**使用者按下設定**（先靜後動之進入嘗試），本筆之觸發為**車輛開始移動**（先進入後起步）—— 二個不同觸發，IN §402 之既有判準即足，不需援引 R-VC26。**不需 baseline**（同 `062-01`）—— 攔的是動作。**範圍（§8.4.2）**：`any of the logic for FOTA via Wi-Fi` 之流程內容屬 Software Updates 側，本筆只驗**起步時之攔阻**，不驗流程本身。

### `SWE1-HMI-VC-063-02#1` — OK on the FOTA in-motion popup returns to the pre-flow screen

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.4.2`
- **`distinguishing_axis`**：離開之控制項：OK（對 X 支之同一落點）
- **`reasoning`**：**驗證目標**：按 OK 離開該彈窗，返回進入 FOTA via Wi-Fi 流程前之畫面。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `If **they** press…` 為非句首代名詞，其標的為 s1 之彈窗；**s1+s2 共 68 token，逾 R-3 之 50**，故不取整段，單句 s2 ＋ CONT 登記 `resolution=PC`。**⚠ `resolution_key` 為 `popup` 而非 `pop-up`** —— SYS1 §13.4.2 原文即作 `popup`（§13.1.1／§13.5 作 `pop-up`），依 profile §9.3 **逐字不寬鬆**：不去連字號、不同義展開。故本筆之 Pre-Condition 與 Procedure 一律書 `popup`。**與 `062-02` 之落點不同**：`062-02` 返回 Settings 清單，本筆返回**進入流程前之畫面** —— 二者非同一落點，故非重複。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### `SWE1-HMI-VC-063-02#2` — X on the FOTA in-motion popup returns to the pre-flow screen

- **`test_set`**：Ignition Availability　**`priority`**：P2　**`spec_ref`**：`…_13.4.2`
- **`distinguishing_axis`**：離開之控制項：X（對 OK 支之同一落點）
- **`reasoning`**：**驗證目標**：按 X 離開該彈窗，返回進入流程前之畫面。**取材同 OK 支**（第三處置類，單句 s2，`resolution_key=popup`）。**拆分依 R-VC26（互相消耗）**：按下其一，彈窗即消失 —— 另一條路徑之情境不復存在，須完整重建才能走。單一 TC 之 Procedure 結構上只能走一條，不拆即必有覆蓋洞。**二筆之 Procedure 各自完整重建情境**（下放包 25 §三）。

### `SWE1-HMI-VC-064-01#1` — Transition to Key Off with the Settings tab open

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.5`
- **`distinguishing_axis`**：開啟之範圍：Settings 頁籤（對 category 支）
- **`reasoning`**：**驗證目標**：Settings 頁籤開啟中車輛轉入 Key Off 時，顯示彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 拆 2 依 R-VC26（下放包 25 §2.3）**：`tab` 與 `category` 為二個**範圍**，且 `064-02` 已載該彈窗**不可被使用者關閉** ——走完其一須**整輪點火循環**才能重建另一之情境，即互相消耗。**⚠ 記法不對稱（A-VC10 第三面）**：Title 作 `Key Off/Timed Mode/ACC`（斜線），Description 作 `Key Off, Timed Mode or ACC` —— 取 Description 一欄，其形態隨之。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### `SWE1-HMI-VC-064-01#2` — Transition to ACC with a Settings category open

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.5`
- **`distinguishing_axis`**：開啟之範圍：Settings 類別（對 tab 支）
- **`reasoning`**：**驗證目標**：不可用之 Settings 類別開啟中車輛轉入 ACC 時，顯示彈窗。**取材同 tab 支**。**§13.5 之 `tab **or a Settings category**` 是本拆分之依據** ——該措辭明文承認 category 可獨立於 tab 被開啟（上繳包 22 §2.2 之旁證）。**二支之點火目標狀態分取 Key Off 與 ACC**：來源之 `turned to Key Off or ACC` 為二個狀態，二者**不互相消耗**（可循環），本可同筆涵蓋；分置二支使二個範圍各配一個狀態，**不增加 TC 數而涵蓋二者**。

### `SWE1-HMI-VC-064-02#1` — Transition pop-up neither times out nor closes

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.5`
- **`distinguishing_axis`**：轉換彈窗之持續：不逾時且不可關（對 -03 之自動解除）
- **`reasoning`**：**驗證目標**：該彈窗不逾時，且使用者關不掉。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2）**：037 之 `This pop-up` 先行詞在 s1；**s1+s2 共 54 token，逾 R-3 之 50** →單句 s2 ＋ `resolution=PC`／`resolution_key=pop-up`。**與 `058-02` 之對照**：二筆句型幾乎相同，而 `058-02` 之 s1 較短（37 vs 42 token）使其整段未逾限、落在層次 1。**層次不得跳層** —— 差別只在來源句之長度。**為什麼二個斷言不拆（R-VC26）**：「不逾時」與「不可關」**不互相消耗** —— 同一個彈窗可連續觀察，走完其一另一之情境仍在。沿 `045`（不逾時＋選取後不關閉）之既有處置，以二條 ER 涵蓋。**觀察期之 5 分鐘為測試設計參數，非來源所載**。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### `SWE1-HMI-VC-064-03#1` — Returning to Run clears the transition pop-up

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.5`
- **`distinguishing_axis`**：解除之目標狀態：Run（對 Key On 支）
- **`reasoning`**：**驗證目標**：車輛回到 Run 時彈窗自動關閉，並回到轉換前之 Settings 畫面。**⚠ 取材為第三處置類**：037 之 `while **pop-up** is on screen` 為**無冠詞名詞回指**；整段 s1-s3 為 **83 token，逾 R-3 之 50** → 單句 s3 ＋ `resolution=PC`／`resolution_key=pop-up`。**⚠ 本筆為第一層之偽陰性**（無冠詞名詞回指）——由勘查 (d) 發現。**ER 之 baseline（§5.6）**：「回到轉換前之畫面」須先記錄那是哪一個。**⚠ 拆 2（下放包 26 §三之裁定）**：來源作 `turned to **Run or Key On**`。上繳包 25 §4.3 我已施 R-VC26 之問法（「轉到 Key On 時彈窗不消失，哪一筆會 FAIL？」——沒有）但**未自行增筆**，因授權為 20 筆而拆分清單無本筆；分析層裁定拆，第 5 批 21 筆。**互相消耗之形態**：轉到 Run 後彈窗已消失，須整輪點火循環重建才能走 Key On。**⚠ 與 `057` 之界線（R-VC26 之適用說明，下放包 26 §3.1）**：本筆之標的為**一次性事件**（彈窗消失）故拆；`057` 之標的為**持續狀態**（tab 不可用），情境不因觀察而消耗，切換狀態即可續驗，故其三態不拆。**R-VC26 不得被讀成「凡 or 列舉皆拆」。****追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

### `SWE1-HMI-VC-064-03#2` — Returning to Key On clears the transition pop-up

- **`test_set`**：Ignition Availability　**`priority`**：P1　**`spec_ref`**：`…_13.5`
- **`distinguishing_axis`**：解除之目標狀態：Key On（對 Run 支）
- **`reasoning`**：**驗證目標**：車輛回到 Key On 時彈窗自動關閉，並回到轉換前之 Settings 畫面。**取材同 Run 支**（第三處置類，單句 s3，`resolution=PC`／`pop-up`）。**本筆即下放包 26 §三所補之覆蓋洞** —— 拆前「轉到 Key On 時彈窗不消失」無任何一筆會 FAIL。**Procedure 自 Pre-Condition 完整重建情境**：本支不接續 Run 支之結果，其彈窗須重新觸發（互相消耗之直接後果，下放包 25 §三）。**等價性不需另判**（下放包 26 §三）：Run 與 Key On 是否同一等價類，不改互相消耗之判準所定之拆分結論。**追溯佐證（不入 ER）**：`Pop Up List` 第 321 列 `PU0319` 之文字與本筆逐字相同，其 `Timeout (sec)` = `N/A`、**`Exit Conditions` = `N/A`**，其 `Description` 作 `Ignition Status: In RUN and then turned to Key Off or ACC … Pop-up is shown and is unable to be closed`。**`058` 與 `064` 確為二個不同彈窗**（文字相同、行為不同）。PU 編號未載於 SYS1／037，只入本欄。

