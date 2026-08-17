# 95 — Comfort HMI / `test_item` 之規則（訂正）

- 產出層：分析層｜2026-08-17｜對象：執行層／規則存續
- 裁定：Pei，2026-08-17
- 性質：**既有規則之訂正記載**。該規則自始存在，分析層於 Comfort 誤實作。

---

## 1. 規則

```
test_item 欄由兩部分構成，以**一個空行**分隔：

  上半 —— **條文原文，原封不動**
    取自該 leaf 所屬節之 spec 條文，逐字照抄。
    不改寫、不濃縮、不加主詞、不換句型。

  下半 —— **一組括號，內含作者所理解之測項定義**
    以自己的話寫出「這一條 TC 驗的是什麼」。
    同一 leaf 拆出之多條 TC，其上半相同、**下半各自不同** ——
    下半即其區分之所在。
```

### 1.1 形式

```
<條文原文>
                              ← 空一行
(<本條所驗之測項定義>)
```

---

## 2. 下半之內容 —— 是「測項定義」，不是「出處」

**下半寫的是作者對該條 TC 之理解**：在什麼條件下、做了什麼、預期看到什麼。

**不是**條款編號（`HVS6.`）、**不是**節次（`11.5`）、**不是**文件名。
出處另有其欄（`specification_reference`），**不由此欄承擔**。

### 2.1 其功能 —— 拆分之區分

一個 leaf 拆為多條 TC 時（§8.2.2、§8.3），**各條之上半完全相同**，
其差別全數落在下半。**下半是那幾條 TC 在 test_item 欄上唯一可分辨之處。**

`features/home` 之 `SWE1-HMI-HOME-020` 為其實例：一 leaf 三條 TC，
上半三份逐字相同，下半為

```
(Apple CarPlay connected and no CarPlay layout exists on any Home Screen
 page -> both additional CarPlay layout options are provided and selectable)

(Apple CarPlay not connected -> neither additional CarPlay layout option is
 provided on the layout selection screen)

(Apple CarPlay connected and a CarPlay layout already exists on a Home
 Screen page -> both additional CarPlay layout options are greyed out)
```

其內容與該 leaf 之 `distinguishing_axis.delta` 對應。

---

## 3. Comfort 之誤實作 —— 兩處皆錯

| | 規則 | Comfort 之實作 |
|---|---|---|
| 上半 | 條文原文原封不動 | **改寫為 `The system shall follow …`**（加主詞、改句型、濃縮）|
| 下半 | 作者所理解之測項定義 | **條款編號 `(HVS6.)`** |

### 3.1 上半之錯 —— 出自 profile §3.1

profile §3.1（下放包 15）寫「Test Item = 以 spec 語言濃縮之需求陳述，
modal 僅此欄允許」。**「濃縮」二字即錯之所在** —— 規則要的是原文不動。

G-1（下放包 16 §2）量了 `home` 之 Test Item 欄，其結論為
「143/144 含 modal、中位 273 字元」，據以認定 §3.1 之 override 有據。
**該量測量了「有沒有 modal」與「多長」，未量「是原文還是改寫」** ——
而 home 之 modal 來自**條文原文本身**（`shall`／`will` 為 RD 語言），
不是作者加上去的。

**量對了指標，答錯了問題。**

### 3.2 下半之錯 —— 使該欄失去其功能

Comfort 有 51 條係自 leaf 拆出（`024-07`→4、`002-05`→2、`020-04`→2、
`15.1`→2、列舉式 28 leaf→+41、缺口 2 leaf→+3）。

**那些拆出之 TC，其 test_item 下半全為同一個條款編號** ——
於該欄上完全無從分辨。

§4.3 之 sibling-distinction 要求「兩個 sibling 之 tc_title 讀來相同即 FAIL」，
分析層守住了 `tc_title`，**而未察 test_item 承擔同一功能**。

---

## 4. 據此須改者

| # | 欄 | 改法 |
|---|---|---|
| 1 | `pre_conditions` | 移除 source class 標籤（下放包 94 已裁），節次括號保留 |
| 2 | `test_item` 上半 | 改回**條文原文**，取自該節之 `full_text`／`source_clause`，逐字 |
| 3 | `test_item` 下半 | 改為**該條 TC 之測項定義**；拆分出之各條**各自不同** |

第 3 項於 51 條拆分列上為**逐條撰寫**，其餘各列一條一則。

---

## 5. 檢查

新增 gate：

- `test-item-two-parts`：`test_item` 須含且僅含一個空行分隔之兩部分，
  下半須以 `(` 起首、`)` 結尾
- `test-item-upper-verbatim`：上半須為其所標節次之 `full_text` 之
  連續子字串（空白正規化後）
- `test-item-lower-distinct`：同一 `req_id` 之多條 TC，其下半**兩兩不得相同**
- `test-item-lower-not-a-reference`：下半不得僅由條款編號／節次／文件名構成
  （形態：`^\([A-Z]+\d*\.?\)$`、`^\(\d+(\.\d+)*\)$`）

四者皆須反向驗證。

**第三道之必要性由本案自證**：51 條拆分列之下半現全相同，
而至交付為止無任何檢查問過這件事。

---

## 6. 本包之性質

**Pei 自行修改檔案。** 本包為規則之書面化，使該規則不再只存在於
`features/home` 之既有產出裡。

執行層不執行 §4 之改寫，**惟 §5 之 gate 須落實** ——
規則寫下而無檢查，即為本案再發生一次之條件。

---

## 7. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| `test_item` 之兩部分規則 | ✅ §1 | 已簽 2026-08-17（**既有規則之記載，非新立**）|

| 本輪於 chat 承諾落檔之包 | 編號 | 已落檔？ |
|---|---|---|
| test_item 規則 | **95** | ✅ 本包 |
