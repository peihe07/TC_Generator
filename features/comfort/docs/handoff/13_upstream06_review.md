# 13 — Comfort HMI / 上繳 06 覆核：R-C18、Test Set 更名、全文抽出

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/06_framework.md`
- 結論：**PASS**。三項處置見下，其中兩項源於分析層自身之錯誤。

---

## 1. 6.3 —— 分析層錯誤，且錯得比表面更值得記

12 §3 我以「non-foldable second row」語意偏後座為由，要求執行層確認落位。
實測全文為 `non-foldable **secondary lower screen**` —— 60 字截斷恰好切在
`secon|dary`，`secondary` 被腰斬成看似 `second`。

**危險之處不在資訊遺失，而在遺失後仍讀得通。** 若截斷產生亂碼，我會去讀
全文；它產生的是另一個完整、合理、但錯誤的語意，於是我在它上面繼續推論。
與 `difflib.autojunk`、`${PIPESTATUS[0]}`、A-CF05 同屬一類：**缺陷不報錯，
且其輸出具備正確之外觀。**

```
R-C18  導覽欄位不得用於判讀

凡經截斷、摘要或正規化之欄位（如 layer3_map.tsv 之 section_title 取前 60
字），其用途限於導覽、排序與人工檢索。

不得據以做落位、範圍、等價、適用性或分組之判斷。此類判斷一律讀全文。

理由：截斷之失敗形態是靜默的，且可能產生語意完整而錯誤之片段
（先例：6.3 之 `secondary` 截為 `second`，導致「次要下方螢幕」誤讀為
「後座」）。片段讀得通，不代表它是原文。

推論：凡以此類欄位為輸入之既有判斷，須回頭以全文複核。
```

**R-C18 之最後一句即刻對我自己生效**，見 §3。

---

## 2. Test Set #15 更名：`Comfort Widget` → `Home Screen Widget`

執行層將命名判定由條件式中之隱藏豁免（`and n != "Comfort Widget"`）改為
獨立回報項，並請分析層裁定。**該改法本身是本輪最重要的處置**：若那行豁免
留在程式碼裡，本節之更名永遠不會發生 —— 檢查會 PASS，而問題會被 PASS 蓋住。

**裁定：更名。**

§4.2 之範例為：Test Group = `Bluetooth` 時，用 `Connection`／`Pairing`，
不用 `BT Connection`／`Bluetooth Pairing`。直接類推：Test Group = `Comfort`
時，該組應為 `Home Screen Widget`，不是 `Comfort Widget`。

執行層之讀法（spec 稱其為 "the Comfort widget"，故該字指涉受測物件）成立，
但 spec 同樣稱整個 feature 為 Comfort —— Bluetooth 之例中，spec 也稱該功能
為 "Bluetooth pairing"。§4.2 禁的正是這個形態。

更名後 Layer 3 不變（17.1 ~ 17.5、18.1），leaves 仍 21。`framework.md`、
`test_set_map.tsv`、`verify_partn.py` 之期望值三處同步更新，**第四項
assertion 之回報項應隨之消失**（更名後無任何 Test Set 以 `Comfort` 起首）；
若仍回報，即為未同步。

---

## 3. ch11／ch12 合併 —— 依 R-C18 必須複核（執行層 §7.2 第 1 項成立）

執行層指出：它只複測了「標籤重複」之事實，未複測我的結論「無證據顯示進入
路徑不同」。

**該質疑成立，且比它所寫的更嚴重**：我做那次查證所讀的，正是
`layer3_map.tsv` 之 60 字截斷標題 —— **即本輪剛被證明不可靠的同一欄位**。
我以「標題沒提到不同入口」推出「入口相同」，這既是截斷判讀（違反 R-C18），
也是以缺席為證據（R-C13 之同構形態）。

合併之結論可能仍為真，但**目前之依據不足以支持它**。

處置見 §4 之全文抽出；複核後若結論翻轉，`Heated Vented Seats`（59）拆回
兩組，屬 Part N 變更，回分析層重簽。**在複核完成前不進 Phase 4 之該組**；
pilot 為 `Seat Control Tab`，不受影響。

---

## 4. 作業指示 —— 一次抽出全部 129 節全文

不做選擇性抽出。截斷欄位之風險在 Phase 4 會反覆出現（每寫一條 TC 都要讀
spec 條文），一次解決優於逐次繞開。

產 `features/comfort/data/section_fulltext.tsv`，129 列，欄位：

| 欄 | 內容 |
|---|---|
| `outline` | 節次 |
| `req_id` | parent `SWE1-HVAC-NNN` |
| `test_set` | 所屬 Test Set（更名後之值） |
| `full_text` | **完整條文，不截斷**；內部換行以 `\n` 轉義，不破壞 TSV |

assertion（PASS/FAIL + 實測值）：
1. 列數 == 129
2. `full_text` 無任何一列等於其在 `layer3_map.tsv` 之截斷值（若相等，
   表示該列仍為截斷輸出）
3. `full_text` 最短長度 > 60，或明示列出 ≤ 60 者並確認其原文確實短於 60
4. `outline` 集合與 `layer3_map.tsv` 相等

### 4.1 抽出後之複核（本包唯一之判讀作業，得下放）

以全文複核 **ch11.1 與 ch12.1**（`HVS1.` 兩節）、**ch11.2 與 ch12.2**
（`HVS2.`），回報下列事實，**不下結論**：

- 兩者所述之操作元件為何（實體鍵／軟鍵／狀態列／彈窗）
- 兩者所述之顯示位置為何
- 兩者之差異詞句逐一列出

「入口是否相同」之判定由分析層做（Part N 內容，Tier 2）。執行層只供事實。

### 4.2 順帶查明

`14.19`（8 leaves，遠大於同章其他節）之全文與其 leaf 分布 —— 供 Phase 4
判斷是否需拆多 TC（§8.2.2）。只回報，不處置。

---

## 5. 接受、無須處置者

- **`[PROPOSED]` 未動 ＝ 生效**，8 項已逐項列入 Ruling notes：正確。此為
  日後最容易被誤讀為「遺漏」之處，明文化是對的。
- **簽署日 2026-08-14 ≠ 寫入日 2026-08-15**，已記為轉錄時差非追溯簽署：
  正確。`Reviewed by`／`Date` 由 Pei 指定而非執行層自填，符合 R-C10。
- **R-C9 對真實已簽檔四項行為全 PASS**，`DECISIONS.new.md` 驗畢即刪
  （不留假狀態）：正確。此為 R-C9／R-C10 立條文後首次於真實簽署上生效。
- **`specification_reference` 是 traceability 欄位而非 Layer 3 欄位**之
  明文化：採納。若無此句，Phase 4 確有可能因「section 不入工作簿」而把
  N 欄留白。
- **A-CF13 第三項**與「條款標籤在 SR24 內不是唯一鍵」之歸納：採納。
  Phase 4 一律以 outline 節次為引用鍵。

---

## 6. 執行層 §7.2 第 2 項（15 組之組內語意一致性）

**暫不處置，但不是駁回。**

該項要問的是「切得好不好」，須讀全文並判斷語意，屬 Tier 2。§4 之全文抽出
完成後，分析層即具備複核之材料；屆時一併處理 #2 `Climate Modes`（41）之
內聚性。

若 Phase 5 pilot 顯示某組過雜，屬 Part N 變更，回分析層重簽 —— 此路徑已存在，
不需為此推遲 Phase 4。

---

## 7. 下一步與 Phase 4 之硬前置

執行層 §7.4 指出之硬前置成立：`DECISIONS.md` §6 profile `[OVERRIDE]` 未定，
其中 **A-CF07（範本第 10–11 列樣本殘留）之寫回處置必須明文**，不得留到
write-back 當下決定。

profile 草案由分析層下一包提出（Tier 2），**得與 §4 之全文抽出並行**，
互不阻塞。

Phase 4 開始之條件：profile `[OVERRIDE]` 簽署 ＋ §4.1 之複核完成
（後者僅阻塞 `Heated Vented Seats` 一組，不阻塞 pilot）。

---

## 8. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C18 導覽欄位不得用於判讀 | ✅ §1 | 已簽 2026-08-15 |

R-C18 須貼入 `RULINGS.md`，適用全 feature，安置位置待 canon re-sync。
§2 之更名為 Part N 變更，隨 `framework.md` 更新，不入 `RULINGS.md`。
