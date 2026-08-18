# 20 下放包 — 第一批 28 條之內容覆核（分析層積欠項）

**本包無裁決條文。** 與 19 包同輪執行：19 之作業 1–4（工具與標示）照跑，
**作業 5–6（第二批生成）於本包之 C-1／C-2 修正完成後同輪進行**。

## 覆核範圍之聲明（先講我查了什麼、沒查什麼）

- **逐條讀全文者**：TC-028～TC-044（17 條）
- **僅經 18 輪對照表覆核其出處與範圍層級者**：TC-017～TC-027（11 條）
  —— **未逐條讀其 pre_conditions／procedure／reasoning 全文**
- 本包之發現皆出自前者。**後者之內容覆核仍為未完成**，
  不得因本包核可而視為已覆核（C-6）。

## 發現

### C-1（defect）TC-039 之 ER 以「applicable examples」指代 chart 內容

ER2 逐字引了引言字串，其後寫 `followed by the applicable examples,
including the Navigation examples` —— **範例本身沒有列出**。

這是 **D-3 的復發**：14 輪之 `the list items of Table CPA2`、
`the string described in note PRACC7.2`，同一個形狀。
測試者讀 ER 無從得知該頁該顯示哪些範例，§6「observable, judgeable」未達。

**與 D-3 的差別是：這次工具已經有了。** `render_spec_region.py`
（17 輪落成，7/7 regression）正是為此型而建 —— 10.3.1 之 chart 與
Table CPA2 同型：文字層攤平、版面仍在。

**作業**：以 `render_spec_region.py` 讀 10.3.1 之頁內 chart，
逐項列出其範例（含 Navigation 項），依 §6.1 之 `a./b./c.` 補入 ER。
若該 chart 之列項確實無法判讀，具名回報並記其方法。

### C-2（defect）TC-036 之 design_method 為 BVA，但無邊界對

§12 之 BVA 為「Boundary (=limit, limit±1)」。TC-036 之
`input_test_data` 為 `Line count per page: 6 (limit)`，
procedure 只驗「不超過六行」，**無 limit±1**，亦無界前基準線 ——
18 輪 §1 自陳「`036`（9.9）只驗上限，**無界前基準線**」，
而 design_method 仍掛 BVA，**兩處記載互相矛盾**。

依 §12 首匹配：單一功能檢查 → **功能測試（Functional Based）**。

**作業**：改 design_method；並自檢全批之 BVA 條目
（現為 6 條）是否皆有邊界對或界前基準線，無者一併改判，逐條回報。

### C-3（style-divergence）TC-044 之 ER2 後半不可觀察

`No info button is shown next to the Connected Account button,
**and the Local vs Connected Profile screen cannot be opened**`。

後半句無法以觀察證實 —— 沒有按鈕時，測試者能證的是「按鈕不在」，
不是「該畫面開不起來」。其判定實際上仍回到前半句。

**建議**：刪除後半句，或改寫為可觀察之形式
（`no entry point to the Local vs Connected Profile screen is present`）。
負向配對之效力來自前半句，不因此減損。

### C-4（note）priority 之一致性規則須明文，以免漂移

現況三條之判級可各自成立，但其分野未寫下來：

| tc_id | 內容 | 判 |
|---|---|---|
| TC-004（5.9）| 偏好之自動儲存機制 | **P0** |
| TC-031（9.6）| 座椅位置儲存與其歸屬 | **P0** |
| TC-032（9.6.1）| Welcome popup 尺寸設定值 | **P2** |

分野應為：**儲存與回復之機制本身 → P0；個別設定項之值與其呈現 → P2**。
寫入 `DECISIONS.md`（併 D-UP16-01 之 tie-break 一節），
否則下一批會出現「某個設定項也算偏好儲存」之漂移。

### C-5（note）TC-040 之 reasoning 措辭與判級不符

11.3 為「具連網能力之車輛**一律顯示**」—— 那是主路徑，
而 reasoning 寫「連網配置之**非主路徑分支**」。
**判級 P1 不改**（其為主要功能之呈現），只改述。

### C-6（未覆核，具名）TC-017～TC-027 之全文未逐條讀

11 條僅經出處對照覆核。第三批開批前補齊。

## 值得記下的兩處（非缺陷）

1. **TC-033（9.7）之 ER 寫「the Profile is not yet deleted」** ——
   若只驗 popup 出現而不驗資料仍在，一個「先刪再問」之實作也會通過。
   §7 false-pass 之防線寫在 ER 裡，這是對的做法。
2. **TC-035（9.7.2）之 ER 照錄條文之二擇一**（`"User 1"` 或前一個 profile），
   未自行選定其一。其鑑別力因此受限，但那是 spec 之歧義，
   **保留歧義優於自造確定性**（§8.4.1）。

## 作業

1. C-1：以 `render_spec_region.py` 補完 TC-039 之 ER
2. C-2：TC-036 改 design_method；全批 BVA 六條自檢並回報
3. C-3：TC-044 之 ER2 後半刪除或改寫
4. C-4：priority 分野寫入 `DECISIONS.md`
5. C-5：TC-040 之 reasoning 修正（判級不動）
6. 重跑全部閘，貼輸出
7. 完成 1–6 後，接 19 包之作業 5–6（第二批生成與其出處對照）

## 不在本包授權範圍

- 任何 git 操作（R-G5／R-G12）
- 寫回工作簿（R-U14）
- 調整 D-UP16-01 之 tie-break（J-9）

## 上繳

`docs/upstream/20_batch01_review_fixes.md`，與 19 輪之上繳合併或分列皆可，
具名說明所擇。附獨立判斷。
