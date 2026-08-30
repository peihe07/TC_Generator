# COVERAGE GAPS — SW Update (FW036)

> **建檔 2026-08-30（下放包 59 §三 #6 T71d）**；其前之各項散於 `REASONING.md`，
> **本檔為回填後之集中處**，非新發現之清單。
>
> **建檔之二個理由**（下放包 59 §三 #6）：
> 1. **交付時須附** —— 追溯矩陣看 trace 與 `test_item`，
>    **看不出「這一句沒有被任何 ER 動到」**（B-8 之發現）
> 2. **其為 DR 之候選來源** —— 未覆蓋而非不可覆蓋者，其成因可能是缺件
>
> **成因之四類**：`委派`（他列驗之）／`間接涵蓋`（其失效必然表現於他處）／
> `不可觀測`（掛 `PENDING`，屬 DR）／**`未起草`（可觀測、可觸發，只是沒做）**。
> **⚠ 只有第四類是我方之欠帳** —— 前三類為處置，第四類為待辦。

---

## 一、`未起草` —— **我方之欠帳（4 項）**

| # | 037 列 | 未覆蓋之 facet（原文摘句） | 其去向 |
|---:|---|---|---|
| CG-1 | `116` | `…the user **ignores** … the update pop-up` | **無** —— batch 10 之 TC 取 `Update Later` 一支 |
| CG-2 | `116` | `…the user … **closes** the update pop-up` | **無** —— 同上 |
| CG-3 | `330` | `…regardless of whether the session **completes successfully or fails**` 之**失敗**支 | 其 TC 之 proc 已含二支，**惟二支皆掛 `PENDING`（伺服器側）** |
| CG-4 | `063` | `High / Medium / **Low** Signal Strength` 三類之逐類判定 | **無** —— 其門檻值未載（DR-SU2(a)），現只驗分類之存在 |

> **CG-1／CG-2 為 IN §8.2.2 之「可拆而未拆」** —— 三個使用者動作可獨立觸發，
> **非不可觀測，只是沒做**。**其補作成本低，應在下一次觸及 `TBM Reflash` 時補。**

---

## 二、`委派` —— 他列驗之（**非欠帳**）

| 037 列 | facet | 委派去向 |
|---|---|---|
| `100` | s2（取消）／s3（逾時） | `newR1L-SU-035`／`034` **各持其一** |
| `109` | s3（各狀態之畫面內容） | `092`–`095` |
| `108` | 使用者選 `Update Now` 之處理 | `099`（`033`） |
| `044`（Body ON 模式之判定） | 模式判定 | `088` |
| `107` | `FOTA_Delay = Prohibited` 之分支 | `037`（ROV-B） |

## 三、`間接涵蓋` —— 其失效必然表現於他處（**非欠帳**）

| 037 列 | facet | 依據 |
|---|---|---|
| `132` | s2 | 先例：其失效必然表現於 s2／s3 之外部後果 |
| `100` | s4／s5 | 依 `132` s2 之先例（上繳包 39） |

## 四、`不可觀測` —— 掛 `PENDING`，屬 DR（**非欠帳，惟其數最大**）

**本類不逐項重列** —— 其權威在 `DATA_REQUESTS.md` 之 DR-SU2 三段式台帳
（(a) 第二型 12／(c) 第三型 7／(d) 第四型 14／**(e) 伺服器側 6**）
與各批之 `PENDING` 行（全案 213 行）。

**惟二項統攝殘餘須在此具名**（R-SU37 v2，**不掛 `PENDING` 故不在 DR 台帳上**）：

| TC | 037 列 | 殘餘 |
|---|---|---|
| `SU-083` | `040` | `notify subscribed modules that software download via Wi-Fi has been enabled` |
| `SU-089` | `047` | 四個儲存欄位（SSID／security type／encryption type／passphrase）之逐項表徵 |
| `SU-140` | `115` | `$UpdateAction$ = [Update Now]` 之設值與其經 TBM FW Service 之傳送 |

> **殘餘之危險在於它不在任何清單上** —— `PENDING` 有 `U` 檢查數它，
> DR 台帳有段落收它，**而殘餘只寫在 `REASONING.md` 的一句話裡**。
> **本節即其收攏處。**
