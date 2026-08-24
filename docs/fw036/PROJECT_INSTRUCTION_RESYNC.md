# Project 指令副本重貼指引（R-G20 首次執行，2026-08-24）

給 Pei 的一次性操作單。貼完可刪本檔或留存皆可（未入版控前不影響 gate）。

---

## 第一部分：§-rules 區塊整段替換

**來源**：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`（現行，sha8 `61ccd5e5`）

**操作**：打開該檔，全選複製；在 Claude Project 指令中，把
`## 0. Purpose` 起、`## 13. Final Rule` 段落止的整個區塊刪除，
貼入該檔全文。

**不要**逐段挑著改 —— 副本落後的至少有四處
（§8.4.3、§8.7.5、§10.7、§11 補段），整段換才不會漏。

## 第二部分：Operating Charter 三處修改

### 2-1 sha 行（必改，否則 R-G20 比對永遠不符）

找到：

```
They are a verbatim copy of
`docs/runtime/ASPICE_SWE6_AI_Instruction.md` (sha256 fa9833ae64c9092f);
that file is authoritative — edit there, then re-concatenate.
```

改為：

```
They are a verbatim copy of
`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
(sha256 61ccd5e5fd02dde9be5647a0c22ca6ee73e6e899456056a4caf86b203fe605d8,
sha8 61ccd5e5); that file is authoritative — edit there, then
re-concatenate. Pilot review 與 feature close-out 時比對本值與 repo
現行 sha（R-G20），不符先重貼再審。
```

### 2-2 「落檔」節，「裁決條文」條目之後加一行

```
- **裁決引用**：下放包引用既有裁決以 `R-XX@<sha8>`（R-G13），sha8 以
  `docs/fw036/RULINGS.sha.tsv` 為準；逐字照錄不再要求，附了不算錯。
  新立條文仍以可直接貼入之區塊產出。
```

### 2-3 「工作形態」節，第二條修改

找到：

```
- 一批一上繳；前批未覆核不得開下批
```

改為：

```
- 一批一上繳；前批未覆核不得開下批（除 R-G14 綠色通道生效期間 ——
  連 3 綠批後自動續批，每 5 批彙總上繳，Pei 抽樣覆核）
```

## 完成檢核（貼完自查）

- [ ] 副本內搜尋 `8.7.5` 有命中（訊號寫法節已入）
- [ ] 副本內搜尋 `CFTS{nnn}-{ObjectID}` 有命中（§10.7 新制已入）
- [ ] 副本內搜尋 `fa9833ae` **無**命中（舊 sha 已清）
- [ ] 副本內搜尋 `61ccd5e5` 有命中（新 sha 已載）

> 注意：canon 之後每次變動（例如 25 包將加入 R-G22 與 §2.1，IN 若再被
> 修訂），sha 會再變 —— 屆時只改 sha 行與變動段落即可，不必每次整段重貼。
> 25 包只動 FO 不動 IN，故本次貼完在 W-P3 結束前應保持有效。
