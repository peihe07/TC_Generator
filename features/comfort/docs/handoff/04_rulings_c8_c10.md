# 04 — Comfort HMI / D-C8・D-C9 裁決 ＋ 簽署標記缺陷

- 產出層：分析層
- 日期：2026-08-14
- 對象：執行層
- 裁定：Pei，2026-08-14（「照你的建議去做」）

---

## 1. 已簽裁決條文

```
R-C8  既有 feature 之 recon 重跑政策

不因共用腳本改版而重跑既有 feature 之 recon。

理由：recon.py 之修改對 Privacy 之 diff 經實測全為增益（新增 assertion 段、
outline map 段誠實回報無 Outline Number 欄、[RULED] tc_id、兩處措辭修正），
無任何數字更正，既有結論之事實基礎未變。重跑之唯一實效為覆蓋
DECISIONS.md，代價大於收益。

例外：若日後發現某腳本缺陷會改變既有 feature 之「數字」而非「呈現」
（如 A-CF05 之靜默漏計形態），該 feature 必須重跑，且重跑前先將現行
DECISIONS.md 另存為 DECISIONS.<date>.superseded.md 保全。

判準為「數字是否改變」，不是「差異是否看起來無害」。
```

```
R-C9  已簽 DECISIONS.md 之覆寫防護（機械強制）

recon.py 於寫入 DECISIONS.md 前，必須讀取既有檔之 Sign-off 區塊。
偵測到已簽署時：拒絕覆寫，改寫 DECISIONS.new.md，以非零碼離開，
訊息指名兩檔路徑。

簽署偵測之判準（機械可判，非人工閱讀）：
  Sign-off 區塊之 "Reviewed by:" 欄位值非空且不等於底線佔位字串。

本條為機械強制而非紀律：全檔重寫是 recon.py 之既有性質，任何人在任何時候
重跑既有 feature 都會觸發，不可能靠「記得不要重跑」防守（R19-3）。
R-C8 是政策，R-C9 是政策失守時的護欄；兩者不互相取代。

適用於所有 feature，非 Comfort 專屬。
```

```
R-C10  簽署標記必須被實際填寫

Phase 2 sign-off 完成時，DECISIONS.md 之 Sign-off 區塊必須填入
Reviewed by 與 Date；留白之範本佔位不構成簽署。

未填寫者，其簽署狀態於 repo 內不可考，依「A ruling not written to the repo
did not happen」視為未簽署。

recon.py 於 Phase 2 之後、Phase 4 之前的任何階段，若偵測到
DECISIONS.md 存在 [PROPOSED] 標記且 Sign-off 為空，須輸出警告
（非阻塞），指明該 feature 之簽署狀態不可考。
```

---

## 2. 為何加 R-C10 —— 覆核時發現之缺陷

實測 `features/privacy/DECISIONS.md` 檔尾：

```
## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
```

**Privacy 之 DECISIONS.md 於 repo 內並未簽署。** 上繳包 §6 稱「Privacy 之
DECISIONS.md 已簽署」，該陳述無 repo 證據支持；簽署若曾發生，只存在於聊天
記錄，未落檔。

此發現有三層後果：

1. **D-C8 之裁決結論不變，理由改變。** 原建議「不重跑以保全簽署」——
   實則無簽署可保全。不重跑之成立理由是「無數字更正、無收益」，
   已如此寫入 R-C8。
2. **R-C9 若僅依 Sign-off 區塊偵測，對現況一次也不會觸發** ——
   全部 feature 之該區塊都是空白範本，偵測器永遠回報「未簽署」，
   護欄形同虛設。故必須同時有 R-C10 要求該欄位被實際填寫，
   R-C9 才是可運作的機制而非可運作的錯覺。
3. 這是 `new_feature.py` 不產 `RULINGS.md` 同一病灶的第二例：**欄位存在
   但從不被填寫，與欄位不存在，在稽核上等價。** 執行層已診斷出第一例；
   本例補齊第二例。

登記 `A-CF09`（OPEN，跨 feature）：既有 feature（至少 Privacy）之
DECISIONS.md Sign-off 區塊為空白範本，簽署狀態於 repo 內不可考。
不回溯補簽（補簽等於偽造當時之簽署行為）；自 Comfort 起依 R-C10 執行。
既有 feature 之簽署狀態如何補記，屬 Pei 裁定，另案。

註：SXM 之 DECISIONS.md 以 Amendment 條目逐次記載裁決與指令原文
（如「DRY-RUN APPROVED（directive「核准」）」），其簽署事實有 repo 證據，
形態與 Privacy 不同。R-C10 之偵測判準採 Sign-off 欄位，不排除
Amendment 形態；兩者擇一即可，但至少須有其一。

---

## 3. 執行層作業指示

1. R-C8、R-C9、R-C10 原文貼入 `features/comfort/RULINGS.md`（R19-2）。
   R-C4-1（下放包 03 §2）若尚未貼入，一併補。
2. 依 R-C9 實作 recon.py 之覆寫防護，含反向驗證：
   人工填入 `Reviewed by: TEST` 後重跑，須確認**拒絕覆寫、寫出
   DECISIONS.new.md、非零離開**，三者皆實測，缺一不算通過。
   驗畢還原測試用之填值。
3. 依 R-C10 實作 Phase 2 後之空簽署警告（非阻塞）。
4. **不重跑任何既有 feature 之 recon**（R-C8）。
5. 登記 A-CF09。
6. Phase 2 併同下放包 03 §3 之 51 節分類（A-CF08）。

---

## 4. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C8 既有 feature recon 重跑政策 | ✅ §1 | 已簽 2026-08-14 |
| R-C9 已簽 DECISIONS.md 覆寫防護 | ✅ §1 | 已簽 2026-08-14 |
| R-C10 簽署標記必須被實際填寫 | ✅ §1 | 已簽 2026-08-14 |

三條均須貼入 `features/comfort/RULINGS.md`。R-C9、R-C10 適用全 feature，
其安置位置（是否另立 repo 層級 canon）於下次 canon re-sync 時處理。
