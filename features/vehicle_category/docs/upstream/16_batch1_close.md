# 上繳包 16 —— Vehicle Category：第 14 項修法，第 1 批 a 段收斂（T90–T94）

- 日期：2026-08-26
- 對應下放：`docs/handoff/16_batch1_close.md`
  （SHA256 `d372cd2ed4cd4467f389907180ae9d47032236727554e9c3e5693f7e99b373b7`，210 行）
- **結論：T90–T94 五項全數完成。收斂 19 項全過 → 第 1 批 a 段收斂。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T90 | profile §5 二則常數 | ✅ 含機讀值域行與帶參數之凍結語意 |
| T91 | 第 14 項改判準 | ✅ 正規化硬檢查 ＋ 軟檢查；**雙向實測** |
| T92 | 重跑收斂 | ✅ **19 checked / 0 failed** |
| T93 | PENDING 書寫慣例 | ✅ 採納，入 profile §7；**未機器化，已記明** |
| T94 | a 段標記收斂 | ✅ 含二種可能之異動來源與其範圍 |

**一件我自己抓到的漏**：下放包 15 §5.3 列了第 15、16 項，
**我上一輪只實作到第 14 項就交了**。本輪補上，第 16 項一加就有用 ——
它是續行型 leaf 上半之唯一機器保護。見 §3。

---

## 1. T90 —— profile §5.1

依 §2.2 改登記二則：

```
ENTER_VEHICLE_CATEGORY:
  Open the Vehicle Category screen

ENTER_VC_TAB(<tab>):
  Open the Vehicle Category screen and select the "<tab>" tab
  <tab> 之值域：framework §2 所載之 Test Set 對應頁籤名
                （現為 Controls、Settings；Specialty 諸名待其批次時擴充）
  values(<tab>) = Controls | Settings
```

`ENTER_CONTROLS_TAB` 成為 `ENTER_VC_TAB(Controls)` 之實例，
**字串不變** —— 22 筆與 pilot 12 筆皆不需改動。
§5.1.1 逐字登記帶參數之凍結語意（模板凍結、值域得擴充須經裁定）
與「不再擴大參數化」之四項禁令。

### 1.1 一處我自行增設，須報備

**末行 `values(<tab>) = Controls | Settings` 為機讀行，下放包未指定。**

理由同 §5.3 之既有作法：值域之擴充須同時改 profile 與 verifier，
而**「須同時」若無承載者就只是規定**。中文值域說明為裁定措辭，
機讀行供 `verify_batch.py` 解析，二者須一致 —— 已於 profile 內記明其關係。

若你認為 profile 不該含機讀行（其為給人讀的文件），
改法是把值域移入 verifier 並在 profile 註明「值域見腳本」——
**但那會使二處分歧無承載者**。**我選了前者，可推翻。**

---

## 2. T91 —— 第 14 項之新判準

### 2.1 全碼

```python
def _norm(s):                      # 小寫 + 去標點 + 壓縮空白 + 去首尾
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

norm_const = {_norm(c): c for c in consts}
for t in TCS:
    for ln in t["test_procedure"].split("\n"):
        step = re.sub(r"^\d+\.\s*", "", ln).strip()
        c = norm_const.get(_norm(step))
        if c is not None and step != c:
            variants.append(...)          # 硬檢查：正規化相等而原字不同 → FAIL
        elif c is None:
            # 軟檢查：Jaccard ≥ 0.7 之候選，列出供人工判讀，**不自動 FAIL**
```

**零閾值於硬檢查**，閾值只用於軟檢查之候選列示。
不以編輯距離作硬判準之理由已逐字寫入腳本註解
（前綴關係之距離大但非變體；閾值鬆則誤報緊則漏報，**因為它量錯了東西**）。

常數展開後為 **3 條**：`ENTER_VEHICLE_CATEGORY`、
`ENTER_VC_TAB(Controls)`、`ENTER_VC_TAB(Settings)`。

### 2.2 雙向實測（PLAYBOOK §7.1）

**(a) 反向輸入 —— 二種變體，皆 FAIL**

注入 `001-01` 之大小寫＋單引號變體（`Screen`／`'Controls'`）
與 `004` 之空白變體（`Open  the`／`screen  and`）：

```
 14  常數之變體擴散（正規化後相等而原字不同 → FAIL；§5.3）   **FAIL**
     變體 2 處
     ['SWE1-HMI-VC-001-01: "Open the Vehicle Category Screen and select the \'Controls\' t" ≠ …',
      'SWE1-HMI-VC-004: \'Open  the Vehicle Category screen  and select the "Controls"\' ≠ …']
exit: 1
```

§5.3 之四類中，**case、hyphenation、spacing 三類已實測抓得到**。

**(b) 已知標的 —— 本批 22 筆之真實首步，全數不觸發**

包含前一輪 FAIL 之二筆：
`Open the Vehicle Category screen`（`001-02`）與
`Open the Vehicle Category screen and select the "Settings" tab`（`001-03`）。
前者不是任何常數之變體（是另一個常數 `ENTER_VEHICLE_CATEGORY`），
後者是 `ENTER_VC_TAB(Settings)` 之逐字相同 —— **二者皆合法，新判準放行。**

**(c) 回歸 —— pilot 12 筆仍 19/0**

### 2.3 §2.3 之要點我照收

> 乙優於甲之關鍵：它把一個需要語意判斷的問題，變成一個不需要語意判斷的問題。

新判準確實不問「該步驟是否為 setup」。`001-02` 之首步放行**不是因為
我們判定它是 test action，而是因為它根本不是任何常數之變體**。

---

## 3. ⚠ 第 15、16 項 —— 我上一輪漏實作

下放包 15 §5.3 明列「pilot 之 15 項 ＋ 第 13／14 項 ＋ 本批二項：
**15. 母體為 22**、**16. `VC-012-03`／`VC-013-03` 之 `test_item` 上半與
SYS1 之完整句逐字相符**」。

**我上一輪只實作到第 14 項就交了上繳包 15**，且在其 §3 標題寫
「收斂驗證：17 checked / 1 failed」—— **那個 17 本身就少了兩項**，
而我沒發現。本輪補上，19 項與下放包所述之數目相符。

### 3.1 第 16 項一加就有用

```
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）   PASS
     適用 4 筆；不符 0 筆
```

**反向實測**：把 `012-03` 之上半改回 037 之片段
（`continuing with additional features below the banners (refer to PDO Graphics)`）：

```
 16  ...   **FAIL**
     不符 1 筆 ["SWE1-HMI-VC-012-03: 上半 'continuing with additional features below the ba'
                ≠ SYS1 'If there are two or more features, display them '"]
exit: 1
```

**這是續行型 leaf 上半之唯一機器保護。** 下放包 14 §2.2 之處置
（取完整句）在此之前只靠我寫對；現在若有人把它改回片段，會被擋下。

### 3.2 這一漏之形態

與 A-VC16 之「把一個窄的檢查用一個寬的詞報出去」不同 ——
**這次是漏做，且漏在一個明確列舉的清單上。**
下放包 15 §5.3 是編號清單，15、16 就寫在那裡。

未立新條（無規則缺口，是執行疏漏）。記於此。

---

## 4. T92 —— 收斂 19 項全過

```
  1  22 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                    PASS
  2  IN §9 十七項自檢                                              PASS
 11  pre_conditions 無 §4.4 三類禁項                                PASS  default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴                                            PASS  命中 0 處
  3  test_item 括號下半 22 筆兩兩不同                                  PASS  相異 22
 3b  test_item 括號下半無中文                                        PASS
  4  specification_reference 22 筆逐字相符                          PASS  不符 0
  5  priority 22 筆逐字相符                                         PASS  不符 0
  6  Test Set 22 筆一致                                            PASS  ['Category Structure']
  7  尾句號／方括號／單引號／行首尾空白                                     PASS  皆 0
 7b  保留記法對得上來源                                               PASS  保留 token 0 個
  8  PENDING 之分布（pilot 專屬）                                     PASS
  9  流程區分（pilot 專屬）                                           PASS
 10  VC-021 委派（pilot 專屬；本批不適用）                               PASS  N/A
  A  Procedure ≥2 步 ∧ 1:1 ∧ ER 無 modal ∧ 無禁用起首動詞               PASS
 13  Test Set 與 framework §2 逐字相符                              PASS  8 組
 14  常數之變體擴散                                                  PASS  常數 3 條；變體 0
 15  收斂母體為 a 段之筆數（R-VC22(b)）= 22                             PASS  tcs=22；leaf_scope=22；held=2
 16  續行型 leaf 上半與 SYS1 完整句逐字相符                              PASS  適用 4 筆；不符 0
19 checked / 0 failed
```

**pilot 亦以同一腳本重跑，19/0**（第 16 項對其報 N/A —— 無續行型 leaf）。

---

## 5. T93 —— PENDING 書寫慣例

**採納**，逐字入 profile §7，並記三事：

1. **自第 2 批起適用，不回溯**（§7.1）—— pilot 之 `VC-033-01` 與
   第 1 批之 `VC-011`／`VC-012-03` 維持現狀。其形態為 §8.4.3 之合法佔位，
   問題是可讀性非合規性。
2. 現行形態之留痕（§7.2），含下放包 §三之三項不阻斷理由。
3. **⚠ 未機器化**（§7.3）—— 「可讀為標註而非句子成分」需語意判斷；
   其可機械化之近似（`PENDING:` 前須為 `(` 或行首）**會把現行三筆判為違規**，
   而它們依 §7.1 不回溯。**故本節靠審閱承擔，不靠檢查器。記明以免誤以為已受保護。**

---

## 6. T94 —— a 段標記收斂

`status: converged`，`status_note` 記**二種可能之異動來源與其範圍**：

1. DR-VC9 回覆 → 異動限於 `VC-011`（`the table` 之指涉）與 `VC-012-03`
   （PDO graphics 之版面細節）二筆；
2. b 段補生成 → 依 **R-VC22(d)** 複驗 a 段未因補入而失效，
   特別是**括號下半之兩兩不同須以 a＋b 全集重驗**。

其餘 20 筆不動。

---

## 7. 未結清單

**DR 九筆全未結**。同批 A 六項；DR-VC9(一) 獨立發。
**A 十二筆未結**。已結五筆。

---

## 8. 待你裁

1. **profile 之機讀行**（§1.1）—— 我自行增設，可推翻。
2. **第 2 批 `Settings List`（30 leaf）之勘查前置** ——
   R-VC21 末句要求每批生成前先勘查。
3. 同批 A（六項）、DR-VC3、DR-VC9(一) 之發送（Tier 3）。

---

## 9. 量測條件揭露（R-G8）

### 第 14 項之偽陰性 —— **wording 變體抓不到**

正規化 = 小寫 + 去標點 + 壓縮空白。故 §5.3 之四類中：

| 類 | 抓得到？ |
|---|---|
| case（`Screen` vs `screen`）| ✅ 已實測 |
| spacing（`Open  the`）| ✅ 已實測 |
| hyphenation（`half-banner` vs `half banner`）| ✅（去標點後相等）|
| **wording** | ❌ **抓不到** |

**具體反例**：`Go to the Vehicle Category screen and select the "Controls" tab`
—— 正規化後與常數不等（`go to` vs `open`），故硬檢查不觸發。
軟檢查（Jaccard ≥ 0.7）會列為候選，**但那是人工判讀，不是保證**。

**故第 14 項之 PASS 應讀作「無 case／spacing／hyphenation 之變體」，
非「無任何變體」。**

### 第 16 項

- 續行型 leaf 之對應以**硬編表** `CONT` 指定（leaf → SYS1 節與句序）。
  **偽陰性**：新批次若另有續行型 leaf 而未加入該表，本項看不到。
  硬編之理由：句序無法自 037 推導（037 之片段不帶序號），
  須人工判定後登記 —— 但**該表本身無檢查**。
- 句子切分以 `(?<=\.)\s+(?=[A-Z])` 為界。
  **偽陽性**：若句中含縮寫之句點（`e.g. Foo`），會被誤切。
  本次四筆之來源句無此形態，未實現。

### 第 15 項

`EXPECT_N` 與 `leaf_scope` 同源，**本項驗不到 `leaf_scope` 自身是否正確**
（承上繳包 15 §9 之同一揭露）。其能驗到的是 `tcs` 與 `leaf_scope` 之一致。
