# 26 下放包 — 09 輪覆核、R-VS7(a)/(b) 之讀法、10 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/07_residual_verification.md`。

**覆核結論：接受。** 兩個升級條件皆命中且皆據實回報；
§1.1 之「兩個 0 之別」正是 R-VS32 立條之目的，本輪首次適用即發揮作用。

---

## 1. A-VS33（R-VS7(a)/(b) 重疊 3 筆）—— 條文已自帶答案

執行層回報 3 筆重疊並拒絕自行擇一，正確。

**惟 R-VS7 之原文已定其序**：(b) 之首字為「**例外**」——

```
(b) 例外：CFTS044 條文自身以 `Refer to TLM HMI Document` 指出畫面
    行為者（16 leaf），其畫面層斷言仍屬本 feature，惟在 DR-5-B
    到位前標 BLOCKED（見 R-VS17）。
```

例外條款之定義即「於其適用範圍內排除主規則」。故：

```
R-VS7 之讀法（分析層裁定 2026-08-20；Pei 得推翻）
(b) 為 (a) 之例外，二者對同一 leaf 皆適用時 **(b) 優先**。

即：CFTS044 條文自身以 `Refer to TLM HMI Document` 或
`Refer to PDO graphics` 指出畫面行為者，該 leaf 之畫面層
**不委派 Comfort**，依 R-VS17 標 BLOCKED。

實質理由（非僅字面）：委派之前提為「該行為由 Comfort 擁有」；
而這 3 筆之 CFTS044 條文**明文將該行為指給 TLM HMI Document**，
即規格作者已宣告其歸屬，該歸屬不是 Comfort。
委派一個規格已明文另有歸屬之行為，會使 reasoning 之委派句指向
一個不擁有它的 feature。

適用：`HeatedSteeringWheelManagement-026`（PDO graphics）、
`-031`、`-035`（TLM HMI Document）——
`delegation_lookup.tsv` 之該 3 列 `delegate` 保持 `blocked`，
`comfort_leaf_ids` 清空並於 `basis` 註明「R-VS7(b) 優先，見 26 包 §1」。

**A-VS33 依此關閉**，不列入待 Pei。若 Pei 認為委派應優先，逕以新條文推翻。
```

---

## 2. A-VS34（反向新增 84）—— 處置

成因具名清楚：06 輪之 Layer 3 清單只列 6 個，
漏列 One/Two/Three Stages 五個 —— 其名稱不含 `LeftFront`／`RightFront`，
故側別判定分支接不到。**假陰性源自詞彙不全（§5a 條 7）。**

```
分析層裁定 2026-08-20
(1) `docs/reports/comfort_overlap.md`（06 輪之單向表）**降為證據**，
    不再作為委派之依據。檔頭首行加註：
        # SUPERSEDED as delegation source — incomplete Layer 3 list
        # (A-VS34); use data/... delegation_lookup.tsv
    **不刪除**（R-VS26(3)）。
(2) `delegation_lookup.tsv` 為委派之**唯一**來源。
(3) 06 輪之 Comfort 側（43 條）**不需重測**：漏的是本 feature 側之
    Layer 3 清單，Comfort 側之關鍵詞（heated/vented seat、heated
    steering）本就涵蓋階數型條文。**惟此為推論，須以 W-34(3) 實測。**
```

---

## 3. 六項未驗之處置

| 項 | 處置 |
|---|---|
| §6-3 **極性未回算** | **最高優先 → W-33**。DR-8／DR-12 之論據建立在未分極性之集合上；**該二 DR 尚未送出，若以錯誤論據送出將浪費上游一輪** |
| §6-1 委派為 Layer 3 層級非逐 leaf | → **W-34(1)** |
| §6-2 46 個 `no` 未逐筆人讀 | → **W-34(2)**。其形態與 A-VS34 完全相同（詞彙不全之假陰性），**已知會漏而未驗者，不得留為 `no`** |
| §6-4 式六／式八邊界未互驗 | → W-34(4)，小項 |
| §6-5 W-32(d) 兩側皆以 7 位數為鍵 | **登記 A-VS35，不排作業**。其驗的是「章節歸屬一致」非「id 指向同一條文」；後者之獨立驗證須另一份載有條文正文之匯出，現無此素材 —— **具名為已知界線，非缺口** |
| §6-6 03／04 上繳之獨立判斷節未回填 | **登記 A-VS36，不排作業**。上繳包為當輪之快照，回填會使其失去時序意義；改於 `docs/INDEX.md` 註明「其未驗項已由 09 輪之 W-29／W-30 涵蓋」 |

---

## 4. 10 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/26_review_round09.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/08_polarity_and_delegation.md，六節先留空。
D-2  ANOMALIES.md：
     - A-VS33 標為**關閉**（26 包 §1：R-VS7(b) 為例外，優先）
     - 新開 A-VS35：W-32(d) 之交叉驗證兩側皆以 7 位數 id 為鍵，
       驗的是章節歸屬一致，非 id 指向同一條文；現無素材可驗後者。
       **已知界線，非缺口**
     - 新開 A-VS36：03／04 上繳之獨立判斷節未回填 09 輪之發現；
       依 26 包 §3 不回填，改於 INDEX 註明
D-3  依 26 包 §2(1) 於 docs/reports/comfort_overlap.md 檔頭加註
     SUPERSEDED 標記（不刪除）；
     `delegation_lookup.tsv` 之 3 筆重疊列依 26 包 §1 修正
     （`delegate=blocked`、`comfort_leaf_ids` 清空、`basis` 註明依據）。

## 作業（三項，R-VS25）

W-33  極性回算（最高優先）
      W-22(d) 已將 CFTS044 側之值分為 include／exclude 兩集合。
      **W-8／W-19 之差異對比對係以未分極性之混合集合進行** ——
      依極性重算：
      (1) 逐 token 重算 CFTS044 側之 include 集合（排除式四之 91 筆），
          與 DBC `VAL_`／LID `Format` 重比
      (2) 列出「重算前後之差異對計數」新舊兩組（R-VS32(2)）
      (3) **DR-8（$VC_VEH_LINE$）與 DR-12（$PowerMode$）之論據逐項重述**：
          其「無交集」／「值不存在」之結論在分極性後是否仍成立？
          不成立者，**該 DR 於送出前須改寫**，逐項具名
      (4) exclude 集合本身之用途另記：`$var$ != [X]` 表示 X 為
          spec 明文排除之值，**其為負向測試（§7）之來源**，
          須於 `spec_variables.tsv` 保留且標明

W-34  委派表之精度與假陰性
      (1) `delegation_lookup.tsv` 之 174 個 `yes`：
          `comfort_leaf_ids` 現為 Layer 3 層級之對應（同 Layer 3 共用同一組）。
          **逐 leaf 收斂**：對每個本 feature leaf，自其
          `Requirement Description` 之行為描述，判定該組 Comfort leaf
          中哪些真與之對應。無法收斂者保留全組並於 `basis` 註明
          「Layer 3 層級，未逐 leaf 收斂」——**不得靜默保留**
      (2) 46 個 `no` **逐筆人讀**其 `Requirement Description`，
          確認其確無 Comfort 對應。改判者具名。
          **理由**：A-VS34 已證功能詞清單不全會產生假陰性，
          而 `no` 正是以「六組功能詞皆不命中」判定
      (3) 驗證 26 包 §2(3) 之推論：06 輪 Comfort 側之 43 條是否
          已涵蓋階數型（One/Two/Three Stages）所對應之 Comfort leaf？
          以 W-29 反向掃出之 84 筆其 `comfort_leaf_ids` 是否全落在
          該 43 條內判定。**有落在 43 條之外者，即 Comfort 側亦有漏**
      (4) 式六／式八之重複覆蓋筆數（§6-4），小項

W-35  10 輪小項打包
      - W-17：LID 列數差 6 之追因；`TRUNCATED_ENUM` 其他形態
      - W-24：`IGN_OFF` 兩處條文是否落在 237 個 Functional leaf 內
      - DR-14′ 之追問文字定稿（第三排頭枕訊號）
      - `unesc()` 併入 `scripts/lid_parse.py` 作為公開介面（05 輪 §6.2-3）

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
衍生檔之刪除屬 Pei；.gitignore 之修改屬 Pei。

## 升級條件

W-33(3)：DR-8 或 DR-12 之結論在分極性後不成立；
W-34(2)：`no` 之 46 筆有改判；
W-34(3)：84 筆之 `comfort_leaf_ids` 有落在 43 條之外者；
實測與 26 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。

## 完成後

06 輪 §6-1 之 36 條「未分左右」複核排 11 輪。
DR-15 到位後即進 framework Part Vehicle Setting ＋ profile（Tier 2）。
```

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS7 之讀法 | (b) 為例外，對同一 leaf 優先於 (a) | 分析層（Pei 得推翻） |
| A-VS34 之處置 | 06 輪單向表降為證據；`delegation_lookup.tsv` 為唯一來源 | 分析層 |
| W-33／W-34／W-35 | 作業 | 分析層 |
