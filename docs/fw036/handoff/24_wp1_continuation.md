# 24 — W-P1′ 下放包（canon 整併與四項裁定落地）

日期：2026-08-24
所據上繳：`docs/fw036/upstream/23a_wp1.md`（覆核 PASS，判定記錄見本包 §B）
下放：分析層　執行：Claude Code
上繳：`docs/fw036/upstream/24_wp1_continuation.md`
（W-P2／W-P3 不受本包影響，其上繳維持 `23b_wp2.md`／`23c_wp3.md`）

**Pei 裁定（2026-08-24 chat，逐字）**：
「1採 2採 3准 4准 我希望這裡儘快結束 但不能草率 因為我需要繼續產生測項」
—— 四項全數通過；本包為其落地工單。速度要求之落實方式：
本包一輪做完 W-P1 之全部殘項，Pei 之人工檢查點集中於 commit 前之 diff 過目一次。

---

## A. 禁區

- 全部 git 操作屬 Pei（R-G5）；執行層只準備，不 commit、不 restore
- **歷史 handoff / upstream 檔一律不改寫**（裁定 2 之核心；含引用改寫）
- 不得改動任何 feature 之已交付件與 done region
- xlsx 一律不碰
- `features/user_profiles/`、`_intake` 不碰（23 包 §A）
- IN（`docs/runtime/ASPICE_SWE6_AI_Instruction.md`）除 §D-5 指名之一行
  範圍註記外不得改動；該註記亦僅「準備入 diff」，Pei 於 diff 過目時裁

## B. 23a 之覆核判定（記錄）

PASS。預期數字對照合規（「未達」正確歸因於步驟未執行）；三項升級停在
該停之處；FO sha `c32b764d…` 未動已驗。分析層已獨立查證三項升級之事實
基礎：FO §8.3 確為「三層檢驗」；`features/display/` 實測僅空 `docs/`；
R-VF 現行最大號實測 R-VF82（`RULINGS.sha.tsv`）。

## C. 四項裁定條文（Pei 2026-08-24 追認；可直接貼入）

### 裁定 1 — FO 行 432 之懸空引用修正

```
**雙向查證是三層檢驗（FO §8.3）在事實陳述上的對應物。**
```

（原文「雙層檢驗（canon §7.3）」，節號與「雙層」兩誤一次修。）

### 裁定 2 — R-G18 以修訂版併入 canon（本包 §D-1 有一處措辭修正）

```
R-G18：canon 節號引用一律帶文件前綴（`FO §X` / `IN §X`）；此為書寫
規則，適用於兩份 canon 自身、模板、與所有新寫文件。歷史 handoff /
upstream 檔不追改（歷史記錄不改寫）；其既有 unresolved 與 ambiguous
引用逐檔逐行列舉於 `docs/fw036/CANON_REFS_WAIVER.tsv`（入版控）。
閘判準：waiver 清單外之 unresolved 或 ambiguous > 0 即 FAIL；
waiver 只減不增，新增即紅。裸「canon §X」於兩 canon 共用節號時計
ambiguous。本閘為每 feature close-out 必跑項。
```

### 裁定 3 — R-VS59~66 之 VF230 線八條改編為 R-VF83~R-VF90

依 R-VF10（命名空間）與 R-VF45（改號只及於現行有效之陳述）。
執行層產出對映表（舊號＋行號＋slug → 新號，照原立條時序），
**同包套用**；Pei 於 commit 前 diff 一併過目 —— 即最終確認點。
`RULINGS.sha.tsv` 於改編後重產。過渡期不需複合鍵（同包完成即無過渡期）。

### 裁定 4 — W-P1 §4 之 display 範圍改定

```
W-P1 §4 改為：RULINGS.md 結構化以 canon §9 + vehicle_setting 完成即足；
display 於其 01_intake_recon 交付後補做，屆時為 Tier 1 事項。
```

### [DEFAULT] R-G13 之上繳回報格式（S5，分析層先裁，Pei 事後追認）

```
R-G13 之上繳回報：逐條表列 `ruling_id | 下放引用 sha8 | 實讀 sha8 | 判`，
相符者亦列（FO §8.2 精神）。不符者依 R-G13 停下回報。
```

## D. 作業清單

1. **裁定 2 之一處措辭修正，入 canon 時採上列 §C 版**：原追認文字
   「unresolved 一律 FAIL」改為「waiver 清單外之 unresolved … FAIL」。
   理由：23a §四-1 之 57 處 section 型 unresolved 若有落在歷史檔者，
   「一律 FAIL」將使閘永紅而歷史又不許改 —— 與裁定 2 之核心自相矛盾。
   此修正已在 §C 條文內；**Pei 於 diff 過目時視同追認，有異議以 diff 階段為準**
2. FO 整併（23 包 W-P1 步 2）：合併兩個 `## 9.` 為一；R-G1~G12 單一落點，
   摘要出入處列表入上繳；全文加逐條錨點；被移動內容於原位標 [MOVED]
3. R-G13~R-G21 併入 canon §9（R-G18 採 §C 版全文）；§8.1／§8.8／§1.2
   修訂文字併入（23 包 §C／§D）；裁定 1 之行 432 修正
4. **FO 全文引用加前綴**（R-G18 書寫規則首個適用對象）：FO 內部之
   「canon §X」逐處改 `FO §X` 或 `IN §X`（依實指）；實指不明者列表升級
5. **IN §8.7.5 範圍查驗**：讀其現行文字，判是否載明適用範圍
   （PM profile-scoped 或全域）。未載明者**準備**一行範圍註記
   （PM 依 R-1 v3；vehicle_setting 依 R-VS52／R-VS67 之 SWC 0708 風格
   不受其拘束），入 diff 由 Pei 裁 —— **不逕行寫定為全域或限定**
6. `CANON_REFS_WAIVER.tsv` 產出：`canon_refs.py` 全跑，歷史檔
   （`docs/fw036/{handoff,upstream}/`、`features/*/docs/{handoff,upstream}/`）
   之 unresolved＋ambiguous 逐檔逐行入 waiver；活躍文件（兩 canon、
   `docs/fw036/templates/`、`features/vehicle_setting/RULINGS.md` 等
   現行有效文件）之引用**改寫加前綴**，不入 waiver
7. 裁定 3 之改編：對映表 + 套用 + `rulings_hash.py` 重產 tsv
8. `canon_refs.py` 增 waiver 支援（`--waiver` 讀 tsv；FAIL 判準照 §C 條文）；
   測試補：waiver 內不紅、waiver 外同型引用紅、waiver 新增列即紅（G-K／R-G9）
9. 全套 pytest；上繳

## E. 預期數字（量測條件同 23a §四；waiver 生效後）

| # | 指標 | 預期 |
|---|---|---|
| 1 | FO `^## 9\.` 標題數 | 2 → **1** |
| 2 | FO 之 `R-G1` 詞界落點 | 2 → **1** |
| 3 | ruling 型 unresolved 之 `R-G13`~`R-G21` 類 | 125 → **0**（23a §四-1 之驗收數）|
| 4 | FO 行 432 原句 `canon §7.3` 全 repo 落點（詞界不適用，字面串）| 1 → **0**（歷史檔引用它者若有，入 waiver 並回報數）|
| 5 | `canon_refs.py --waiver` 之 FAIL 數 | **0** |
| 6 | waiver 列數 | 未知 — 首產即基線，回報實測 |
| 7 | `rulings_hash.py` 重複 ruling_id 組數 | 8 → **0** |
| 8 | R-VF 最大號 | 82 → **90** |
| 9 | 全套 pytest 失敗數 | **8**（既有，不得增減；增 = 本包引入，減 = 越權碰了禁區）|

## F. 升級條件（停下回 chat）

1. FO 兩版 §9 有無法調和之實質矛盾（非摘要措辭差）
2. 步 4 之「實指不明」引用（列表升級，不猜）
3. IN §8.7.5 之範圍查驗結果使註記無法以一行表述
4. 改編八條時發現第九條以上同號（掃描面之外者）
5. waiver 產出時發現活躍文件與歷史檔之界線有未定案例
   （例：已 close-out feature 之 RULINGS.md 算哪邊 —— 預設歸活躍、
   改寫加前綴；若量大到不成比例，回報實測數再裁）

## G. 上繳要求

23 包 §G 全項，另加：R-G13 回報格式首次適用（本包引用之裁決以
`R-XX@sha8` 逐條列表，sha8 取自現行 `RULINGS.sha.tsv`；canon 側條文
於併入前無 sha，標 `pre-merge`）；裁定 3 對映表全文；步 4 改寫之
逐處 diff 統計（改了幾處、各檔幾處）；IN §8.7.5 查驗結果與註記草稿。

## H. 本包產生之新條文清單（自檢表）

- [x] 裁定 1（行 432 修正文字）— 區塊已列
- [x] 裁定 2（R-G18 修訂版）— 區塊已列
- [x] 裁定 3（改編指示）— 已列（條文性內容為對映表，由執行層產出）
- [x] 裁定 4（W-P1 §4 改定）— 區塊已列
- [x] [DEFAULT] R-G13 回報格式 — 區塊已列，待 Pei 追認

本包引用之既有條文：R-G5、R-G9、R-G12、R-G13~R-G21（23 包 §D，pre-merge）、
R-VF10、R-VF45、R-VS52、R-VS67、G-K、G-D、FO §8.2、FO §8.3、FO §5a-11、
23 包 §A／§C／§D／§E、23a §四-1／§五／§六。
