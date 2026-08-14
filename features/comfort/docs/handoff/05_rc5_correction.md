# 05 — Comfort HMI / R-C5 訂正、04 §2 訂正、Phase 2 建議

- 產出層：分析層
- 日期：2026-08-14
- 對象：執行層
- 覆核對象：`features/comfort/docs/upstream/02_phase2_review.md`

---

## 1. 覆核結論：**PASS**，並接受甲、乙兩項指正

R-C9 反向驗證四項全 PASS，護欄置於 `write_decisions()` 單一寫入點而非呼叫端
—— 採納。條文所指之失效形態是「任何人在任何時候重跑」，需要呼叫端記得的
設計在定義上防不住它。佔位判定改 `^[\s_]*$` 以涵蓋 Projection 之
`____________`：正確，佔位長度不是判準。

量測腳本 `${PIPESTATUS[0]}` 於 zsh 取到空字串而把 PASS 報成 FAIL —— 此自我
更正之揭露與 A-CF05、`difflib.autojunk` 同形態且同等重要：**工具無聲取到
空值，而空值在比較式裡看起來像結論**。三例已足以構成一類，於下次 canon
re-sync 併入 §5a。

---

## 2. 甲項 —— R-C5 之訂正（分析層錯誤）

```
R-C5-1  R-C5 適用範圍之限縮（訂正 R-C5，非取代）

R-C5 列舉之 22 節中，經對 SR24 export 逐節查存，16 節同樣存在於 SR24 基線：
  18.2 / 18.3 / 18.4
  19.1 / 19.2 / 19.3
  20.1 / 20.1.1 / 20.1.2 / 20.1.3 / 20.2 / 20.3 / 20.4 / 20.4.1 / 20.4.2 / 20.4.3

R-C5 之推論鏈為「屬 SR25 → 因基線為 SR24 → out of scope」。對此 16 節，
第一個前提不成立，故結論不成立。此 16 節自即日起退出 R-C5 之適用範圍，
併入 A-CF08 之 in-baseline substantive 集合，處置待 D-C10。

R-C5 對其餘 6 節（21.1 / 21.2 / 21.3 / 21.3.1 / 21.4 / 21.5）之結論不變：
SR24 export 最大 outline 為 20.4.3，無第 21 章，該 6 節確為 SR24 所無。

在 D-C10 裁定前，該 16 節維持：不產 TC、不入 coverage 分母、不列 BLOCKED、
不補 RD 項目。退出 R-C5 只改變其「為何暫不處置」的理由，不改變其現況。
```

### 錯因

我於 handoff 01 §5 建 A-CF01 時，取「SR25 outline 187 節 − 037 引用 129 節
= 58 節未引用」，再從中挑出形態像需求者，直接標為「SR25 新增」。

**中間少了一步：我從未查過這些節是否也存在於 SR24。**「037 沒引用」被當成
「SR24 沒有」用了。這是以代理判準（037 的引用範圍）凌駕實質判準（SR24
export 的實際節次集合），正是 §5a 明列的失效形態。

代價具體可數：16 節實質需求被錯誤地排除於範圍之外，而它們在基線之內。
若未被指出，framework Part N 會在缺 16 節的前提下切 Test Set。

R-C5 原文不改寫（已被取用），以 R-C5-1 限縮。

---

## 3. 乙項 —— handoff 04 §2 之訂正（分析層錯誤）

04 §2 第 2 點稱「全部 feature 之該區塊都是空白範本，偵測器永遠回報未簽署，
護欄形同虛設」。實測推翻：`amfm` 與 `sxm` 之 Sign-off 已填
（PeiPYHsu / 2026-08-09），sxm 另有 11 條 Amendment。

我讀了 privacy 一個檔，就寫下關於「全部 feature」的斷言。**單一樣本推及全集，
且該全集當時可完整列舉、可實測。** 與甲項同源。

訂正後之影響：

- **R-C10 之結論不變** —— 另三個 feature 確為空白範本，要求簽署標記被實際
  填寫仍必要。改變的是理由，不是條文。
- **R-C9 今日即有效**，非「一次也不會觸發」。amfm 與 sxm 若被重跑，覆蓋的
  是有 repo 證據的簽署。
- **R-C8 份量上升** —— 它保護的不是假設中的簽署，是實存的簽署。
- **A-CF09 範圍限縮**：空白範本者為 privacy 及另二 feature（執行層實測清單
  為準），非全部。amfm、sxm 不在其列。`media` 無 `DECISIONS.md` 一事另記。

執行層於上繳 01 §6 稱「Privacy 已簽署」亦為誤述，已自行更正；不重跑之結論
不變（R-C8 之理由是「無數字更正」，非「保全簽署」）。

---

## 4. Phase 2 之兩項提案 —— 分析層建議（Pei 簽署時採用與否）

### 第 6 項 exemplar source

提案原文「nearest sibling feature done region, cross-feature: style only」
解析不到對象：時序最近之 privacy／sxm 皆 BLANK。

**建議改為具名**：`home` 之 done region（144 列，PARTIAL_INTERLEAVED）為
唯一 exemplar 來源。`amfm`（158 列）不作為 exemplar —— 其 recon 自記
requirement-family mismatch，借樣式與借別的在實務上難以劃線，具名排除比
註記警語可靠。

理由：handoff 01 §1 已要求每個字面值回溯 Comfort 自身 spec 並以 lint 強制；
`cross-feature: style only` 這個標記若無具名對象，lint 沒有可比對的來源，
標記就只是文字。

### 第 10 項 batch plan

「smallest coherent batch」機械地選到第 6 章 1 個 leaf。

**建議 pilot 取第 13 章（14 leaves，Seat Control Tab）**，非第 9 章（8）。
pilot 之用途是在小樣本上暴露判斷漂移；樣本若不含難判斷之處，跑完等於沒跑。
第 13 章含 13.1 之 variant 條件（lower comfort screen 之有無），會逼出
§8.7.3 variant label 與 §4.4 Pre-Condition 兩類判斷；第 9 章 8 節為附加
控制，形態較單一。若 Pei 傾向更小樣本，第 9 章可接受，但須知其代價是
pilot 不會碰到 variant 判斷。

**「依章分組」本身應於 Part N 後改寫**：章 2（92）與章 16（99）各成一個
90+ 的批不是批次規劃。執行層此判斷正確，採納。batch plan 於 Phase 2 簽署時
宜標為暫定，Part N 定案後重寫。

---

## 5. D-C10 之前置 —— 適用性判讀（本包指示）

執行層 §8.2 第 4 項之自我判斷正確且為本輪最有價值之揭露：**分類回答的是
「這節長得像不像需求」，不是「這節是否該由 Comfort R1L 驗證」。** D-C10
需要後者，現有材料不足以裁。

指示：對 17 節 `substantive`（16.1 ＋ 18.2–18.4 ＋ 19.1–19.3 ＋ 20.1~20.4.3）
產出適用性判讀，寫入 `features/comfort/data/sr24_substantive_applicability.tsv`
與上繳包。每節輸出：

| 欄 | 內容 |
|---|---|
| `outline` | 節次 |
| `scope_verdict` | `in_scope` / `out_of_scope` / `undetermined` |
| `basis` | 判定依據之文件與位置，逐節具名 |
| `variant_condition` | 適用之車型／市場／螢幕尺寸條件（如有） |

判讀依據限以下來源，逐節具名，不得以形態推論代替：

- **20.x（LATAM Alternative Rear Blower）**：節標題自身寫明
  `See CFTS043 for applicable vehicles`。須讀 CFTS043，優先
  `SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx`
  （檔名即宣稱 R1L-R scope，若其內容支持，即為最直接之判準）。
- **19.x（7" Home screen Comfort Widget）** 與 **18.x（10.25"）**：螢幕尺寸
  適用性，須對 R1LR ATL-H 之機種配置確認，不得以「spec 有寫」即認定在範圍。
- **16.1（EMEA ICS CARRYOVER）**：市場適用性。

`undetermined` 是合法且鼓勵的結論 —— 判不出來就標 `undetermined` 並具名
缺什麼，勝於填一個看起來完整的判定（§5a：檢查項不可能失敗者標「未實測」
而非 PASS，同理適用於判讀）。

**仍不得產 TC、不得補 RD、不得改 R-C5／R-C5-1。** 本項為量測，非處置。

素材：CFTS043 已確認存在於
`1_Customer_Requirement/R1LR SR26 ATL-H/25PI3.5/Reference Docs/CFTS043/`（27 件附件）
及 `25PI3.5/Sub System/Cabin/…CFTS_043 HVAC Controls and Displays…doc`，
另有 `9_ASPICE/01_SYS.1 Requirement Elicitation/SYS1_R1L-R/` 下三份 SYS1
對照表。**素材補入 `inputs/` 屬 Tier 3**，執行層於 DATA_REQUESTS.md 開列，
不自行搬移。基線 release 取 25PI3.5（與既有 feature 一致）。

---

## 6. 執行層作業指示

1. R-C5-1 原文貼入 `features/comfort/RULINGS.md`，置於 R-C5 之後。
2. A-CF08 更新：substantive 集合之處置理由更新（16 節退出 R-C5）；
   A-CF09 範圍限縮為實測之空白範本 feature 清單。
3. `DATA_REQUESTS.md` 開列 CFTS043 之具名檔案請求（Urgency: 高 ——
   D-C10 與 Phase 3 Part N 皆待其解）。
4. 素材落位後執行 §5 之適用性判讀，上繳 03。
5. `DECISIONS.md` 仍不簽署（Tier 2）；第 6／10 項於簽署時依 §4 建議調整，
   由 Pei 決定。
6. Phase 3 不開始 —— 依執行層 §8.4 判斷，D-C10 牽動 Part N 之輸入。

---

## 7. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C5-1 R-C5 適用範圍限縮至 6 節 | ✅ §2 | 分析層訂正自身錯誤，即時生效 |

§3（04 §2 訂正）不產生新條文，僅更正既有條文之理由陳述，R-C8／R-C9／R-C10
原文皆不變。§4 為建議，非條文，待 Pei 簽署時採納與否。
§5 為量測指示，非條文。
