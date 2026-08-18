# 38 下放包 — 第四批覆核結案（26／26）與第五批開批

**本包無裁決條文。** 37 輪上繳**核可**。

## 覆核進度

**`TC-109`～`TC-134` 全部 26 條逐條讀畢。第四批內容覆核結案。**
語料 134 條之中，未經第二人讀過者：**0**。

## 發現

### Z-1（defect）`TC-110` 誤用 R-U56，`per Profile` 未被驗

`TC-110` 之 remarks：

> 逐 profile 之隔離未於本條驗 …… 條文有述而 037 未為其另切 leaf ——
> 依 R-U56 為 OUT-OF-SCOPE，不列缺口。

**但 `per Profile` 就寫在該 leaf 自己的 037 description 內**：

> `The system will latch on whichever tab was last used within and over key
> cycles, **per Profile**, when entered through pushing the Profile button.`

**R-U56 之適用範圍是「spec 有內容而 037 未為其產出 leaf」。**
此處 037 **產出了 leaf**，而該 leaf 之描述本身即含 `per Profile` ——
**這不是範圍外，是該 leaf 自己的斷言沒有被驗完**（§6：
最終 ER 須涵蓋完整之 Test Item outcome）。

**且其為獨立之部分失效**：一個把分頁存成**全域**（非逐 profile）之實作，
`TC-110` 照樣通過 —— A 存 Edit Profile、key cycle 後回來仍是 Edit Profile，
與現行 ER 完全相符。§8.3 之壓力測試（「若只有部分行為失效，
我的判定是否仍明確？」）在此為否。

**改（擇一，具名所擇）**：
- (a) 擴充 `TC-110`：pre-condition 加第二個 profile 各自之分頁狀態，
  ER 併驗「B 之分頁不因 A 之操作而改變」
- (b) 依 §8.2.2（RD sub-id ≠ TC 數）另立一條，同 trace `018-02`

**(a) 較省**，且 latch 之範圍（`within and over key cycles`）與其
**逐 profile 限定**本為同一句之兩個修飾，併驗不失焦。

**連帶自檢（重要）**：全批凡以 **R-U56 判為 OUT-OF-SCOPE** 者，
逐條確認其標的**確實不在任何 leaf 之 description 內**。
**判準**：該行為之關鍵詞是否出現於本 leaf 或他 leaf 之 037 description。
**出現 → R-U56 不適用，須改判**。命中 0 亦回報。

R-U56 是我裁的。**它若被用成「這句話我不驗」的通行證，
那是我立條時沒有把適用範圍寫得夠窄之代價** —— 故本項自檢須全批跑。

## 已讀 5 條中值得記下的兩處

1. **`TC-109` 之 pre-condition「該 profile 從未開過 Profile 區」** ——
   否則 latch 會蓋過預設值，**測到的是上次的分頁而不是預設分頁**。
2. **`TC-110` 取跨 key cycle 一側之理由** ——
   「若只驗同一 key cycle 內之保留，一個把分頁存在揮發性記憶體之實作會通過」。
   **選較難成立之一側，而非較好測之一側。**

## 作業

1. Z-1：依 (a) 或 (b) 處置並具名 ＋ **R-U56 判定之全批自檢**
2. 重跑全閘，貼輸出
3. **第五批取樣清單**（先回報，不生成）
   - 範圍：**5.12 – 5.16（`ALLPR1` – `ALLPR6`）**，13 leaf，估 ≈ 14 條
   - 加 `041-04`（5.13.2）之失敗路徑 —— 29 輪已具名其須故障注入，
     **且 34 輪已更正其不屬第四批**
   - 三項必含比照前例具名
   - `pending` 兩 axis（`046` 6.1／`065` 8.1）**仍不在本批**，
     須再次具名其預定兌現之批次

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- **寄出 RD 查詢單** —— Tier 3，屬 Pei
- 寫回工作簿（R-U14）
- 第五批之生成 —— 待取樣清單覆核

## 上繳

`docs/upstream/38_batch05_sample.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 現況

| 項 | 值 |
|---|---|
| 語料 | 134 條 ／ leaf 覆蓋 125 / 180 |
| 已覆核 | **134 / 134** |
| 餘 leaf | 55（ch5 之 13 ＋ ch6 之 9 ＋ ch7 之 10 ＋ ch8 之 23）|
| 擋 Phase 6 | A-UP09 / R-U14（DV gate 未立）|
| 待 Pei | RD v2 寄出、R-U17、DR #4、N-XF01、A-UP10、A-UP11 是否回報上游 |
