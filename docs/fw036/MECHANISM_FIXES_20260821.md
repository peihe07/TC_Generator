# 機制缺陷修正（2026-08-21，Pei 指示修改；條文供末端確認後回寫 canon）

## 機制一：test_item 括號下半（測試目的）硬性化

實測：AMFM 154/298 缺（51.7%，含 row87–90 四條 sibling 逐字相同）；
Media 2/602、PM 0/283、Projection 2/653。結論：規則僅存於部分輪次
prompt，未入 canon、未入 lint → 逐 feature 漂移。

**條文（貼入 canon §4.3 末）：**
```
test_item 採兩段式：上半 = 需求/規格原句 verbatim；下半 = 括號內
作者生成之測試目的或情境標籤，獨立成行，格式 `(...)`。
同一需求衍生多個 TC 時，括號即 sibling 區分 token，兩條 sibling
之括號內容不得相同。缺括號下半 = lint FAIL（硬性，不得出貨）。
```
**工具側：** lint 新增檢查 I（test_item 末行須匹配 `^\(.+\)$`）；
prompt builder 模板將括號下半列為必填輸出鍵，不隨輪次增減。

## 機制二：裁決回數多、散落、易漏

病灶：裁決散於多輪聊天，§8.7「不落檔=不存在」有原則無配套。

**條文（貼入 FEATURE_ONBOARDING.md §7 handoff contract）：**
```
a. 每 feature 設 RULINGS_LEDGER.md 單一台帳；R 條文僅在台帳全文
   落檔一次，各包引用編號不重抄。
b. 每包需 Pei 裁定之新規上限 3 條；超過即拆包，不得於同包堆疊。
c. 包尾自檢表增列「本包引用之既有裁決編號清單」；引用未落檔
   編號 = 包退回。
d. Tier 1 事項（純格式、可逆、單 feature）分析層以保守預設先行，
   標 [DEFAULT] 記入台帳供 Pei 事後追認或推翻；僅 Tier 2+ 阻塞等裁。
```

## 機制三：缺件不得留空

病灶：來源文件缺（例 TLM HMI Document）時欄位直接留空，
「未寫 / 不適用 / 缺件」三態不可分。

**條文（貼入 canon §8.4 後新設 §8.4.3）：**
```
§8.4.3 缺件佔位制：TC 欄位因來源文件缺失而無法填寫時，一律寫
`PENDING: DR-{n} <缺件名>`，不得留空、不得填 NA（NA 保留給
「確認不適用」）。DR 登記於 feature 之 DATA_REQUESTS.md；每包
上繳附「本包新增/未結 DR 清單」。lint：必填欄空白 = FAIL；
含 PENDING 之工作簿 = 不得出貨，交付前必須全數結案或由 Pei
裁定降轉 NA。
```

## 併入回修計畫

上述三項登記為 REMEDIATION_PLAN S4（機制一）/ S5（機制二）/
S6（機制三）。M 系列既有項目對應補修：AMFM 154 列缺括號併入
M6 批（同本、同區作業）或另立 M9，由 Pei 裁定。
