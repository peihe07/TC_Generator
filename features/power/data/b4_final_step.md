# B4 —— G77 判準詞彙之經驗導出（R-P101）

> 語料：Comfort + Privacy 已交付之 `test_procedure` **末步**。
> 依 **R-P80** 僅用其「末步為驗證步驟」之結構性事實，不引用內容裁決。
> 二份皆 `read_only=True`，**未呼叫 `save()`**。
> 產生指令：`python features/power/scripts/build_final_step.py`

## 1. 語料

末步共 **472** 條（Comfort 461、Privacy 11）。

末步字數：中位 7、P90 12、最長 19。

## 2. 驗證意圖措詞之出現次數

| 詞 | 末步命中 | 佔比 |
|---|---|---|
| `check` | **0** | 0.0% |
| `verify` | **0** | 0.0% |
| `confirm` | **0** | 0.0% |
| `ensure` | **0** | 0.0% |
| `validate` | **0** | 0.0% |
| `observe` | **0** | 0.0% |
| `look` | **0** | 0.0% |
| `note` | **0** | 0.0% |
| `measure` | **0** | 0.0% |
| `compare` | **0** | 0.0% |
| `read` | **243** | 51.5% |
| `count` | **3** | 0.6% |
| `wait` | **7** | 1.5% |

**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）於語料命中 0 / 472。**

## 3. 已交付末步之行首動詞

| 動詞 | 次數 |
|---|---|
| `read` | 160 |
| `pres` | 140 |
| `change` | 51 |
| `turn` | 35 |
| `select` | 13 |
| `adjust` | 9 |
| `touch` | 8 |
| `move` | 8 |
| `wait` | 7 |
| `open` | 6 |
| `set` | 5 |
| `trigger` | 5 |

## 4. 結論 —— 一項須回報之衝突

**§5.2B 之措詞在已交付實務中 0 / 472 attested。**
已交付件之末步慣例為「Read <具體可觀察標的>」——
以「所讀之標的」滿足 §5.5「Final Step 自身即揭示所檢查者」，不另加子句。
Privacy 之末步全數為此形態（例：`Read the state of the speed controlled volume on the HU`）。

**執行層之判別**：R-P101 所指之缺陷**成立** —— 13 包之末步
「Read the TLM display through SplashScreen_Time」所讀者為**載體**（display）
而非**標的**（splash screen），連已交付慣例之標準都未達到。
故本閘依 R-P101 之明令實作並列為阻斷類。

**惟須明載**：採 §5.2B 措詞後，Power 之末步慣例將與 Comfort / Privacy
**分歧**（A-PW67）。此與 G73 之情形不同 ——
G73 是判準無法與合法回讀區分（故不阻斷），
G77 是判準明確而**交付慣例與 canon 條文不一致**（故阻斷，但須登記）。

## 5. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）

| 版本 | G77 findings |
|---|---|
| 13 包版（修正前） | **9** |
| 14 包版（修正後） | **0** |
