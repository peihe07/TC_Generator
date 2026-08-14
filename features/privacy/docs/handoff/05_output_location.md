# 下放包 05 — 寫回輸出位置與摘要落點（R26）

分析層 → 執行層。2026-08-13。Pei 本日裁示：寫回輸出指定於
`features/privacy/output/`；摘要落點依分析層建議改置 feature 根目錄（「寫」）。

**本包取代**：下放包 04 §3.4 之「建立 `features/privacy/inputs/BASELINE.sha256`」
一項，改依 §1 R26-2 執行。04 包該項之停手條件（被 `.gitignore` 排除即停手）
已預先攔截此衝突，**不必再觸發**。04 包其餘各項不受影響。

---

## 1. 裁決條文

```text
[RULING] R26 — Privacy 寫回輸出位置與摘要落點（Pei 簽署 2026-08-13）

R26-1  寫回輸出位置
  裁：P7 寫回輸出寫入 **`features/privacy/output/`**（feature 內部），
      不使用 repo 根之 `output/`。
      該目錄已由 `features/privacy/.gitignore` 之 `output/` 一行排除，
      **維持排除** —— 交付 xlsx 為大二進位且可重產，不進版控。
      `.gitignore` **不修改**。

R26-2  摘要落點 —— 移出被排除目錄，改置 feature 根
  事實：`features/privacy/.gitignore` 排除 `inputs/` 與 `output/` 兩個
      目錄。目錄層級之排除使 `!inputs/*.sha256` 形式之反向規則無效
      （git 不進入被排除目錄），欲保留需改寫為 `inputs/*` + 反向規則。
  裁：**不改 `.gitignore`**，改將兩份摘要置於 feature 根目錄（本即追蹤）：

        features/privacy/BASELINE.sha256   ← 素材基準（inputs/ 8 檔）
        features/privacy/DELIVERY.sha256   ← 交付產出摘要（output/）

      兩者皆 **進版控**。
  理由：為兩個小文字檔改寫版控規則，風險大於收益；且目錄層排除之反向
      規則易寫錯而不報錯（與 §5a「詞彙型工具之缺陷不會報錯」同型）。

R26-3  摘要為唯一之交付身分證明
  裁：`DELIVERY.sha256` 於每次 `--write` 後更新，逐次追加不覆蓋，
      欄位：產出檔名 / SHA256 / bytes / 產製日期 / 對應 tag（若已打）/
      lint 結果 / zip 成員數。
  理由（先例，逐字記錄以免日後被當成過度設計）：
      AMFM v2 從未進版控，`output/` 一經清除即不存在；而 v1 因
      `write_back.py` 已改接外科手術路徑、openpyxl 存檔路徑在檔內
      已不存在，**連重產都做不到**，tag `fw036-amfm-regen-v1` 指向一個
      無法再現的產物。
      `output/` 為 gitignored 是正確的；**錯的是沒有任何追蹤中的紀錄
      能證明當初交付的是哪一份**。本裁決即補此缺。
  §5a 新增：**可重產之產物不進版控是對的；但「可重產」本身是一項需要
      維持的能力，工具鏈變更可能使其失效。故產物之身分摘要必須進版控，
      且與產物本身分開存放。**

R26-4  BASELINE.sha256 欄位（承 R25-3，落點更正）
  裁：內容不變 —— 逐檔記錄檔名 / SHA256 / 命中之客戶樹路徑 / 稽核日期；
      落點由 `inputs/BASELINE.sha256` 改為 `features/privacy/BASELINE.sha256`。
      本日稽核之 8 檔全數 MATCH，直接落檔，不需重測。
```

---

## 2. 執行層作業

1. 貼入 §1（R26）至 `features/privacy/RULINGS.md`
2. 建立 `features/privacy/BASELINE.sha256`（R26-4）—— 取代 04 包 §3.4
3. 建立 `features/privacy/DELIVERY.sha256`，寫入表頭與欄位定義，
   資料列留空（尚未寫回）
4. 確認上述兩檔**未**被任何層級之 `.gitignore` 排除
   （含 repo 根與 feature 兩份）；**若被排除，停手回報，不自行修改**
5. 建立 `features/privacy/output/` 目錄（可留 `.gitkeep`；
   若 `.gitkeep` 因 `output/` 排除而無法追蹤，**不強求**，目錄由寫回時建立即可）
6. `feature.yaml`：寫回輸出路徑指向 `features/privacy/output/`
7. `PLAYBOOK.md` §6 之 P7 列加註輸出位置與兩份摘要之落點

---

## 3. 停手條件

1. `RULINGS.md` R26 編號已占用 → 停止貼入，續行第 2–7 項
2. 第 4 項確認發現任一摘要檔被排除 → **停止第 5–7 項**，續行回報，
   附排除規則之檔名與行號。不得自行修改任何 `.gitignore`
3. 第 6 項發現 `feature.yaml` 之寫回路徑欄位不存在或名稱與預期不符 →
   停止該項，續行第 7 項，回報實際欄位結構

---

## 4. 上繳包要求

併入 `features/privacy/docs/upstream/04_framework.md`（與 04 包同一份，
不另開），須增列：

1. §2 七項完成狀態
2. `BASELINE.sha256` 與 `DELIVERY.sha256` 全文
3. 第 4 項之確認方式與結果（用何指令驗證未被排除）
4. `feature.yaml` 寫回路徑之變更前後

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R26-1 寫回輸出位置 `features/privacy/output/`，維持 gitignored —— §1
- [x] R26-2 摘要移至 feature 根，不改 `.gitignore` —— §1，區塊形式
- [x] R26-3 DELIVERY.sha256 為交付身分證明 + §5a「可重產是需維持的能力」—— §1
- [x] R26-4 BASELINE.sha256 落點更正（承 R25-3）—— §1，區塊形式
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §3

<!-- HANDOFF-LINK: 05 -> merged into 07 -->
