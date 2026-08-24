# 上繳 V25 —— pilot #1 v4 完成；**第 2 批停在生成之前**（形態變更）

執行層寫入。依據：`docs/handoff/V25_pilot1v3_review.md` §6（W-VF63）。canon §8.2 六節。

**未寫回**（R-VF26）。**第 2 批未生成 —— 理由見 §4，非遺漏。**

---

## 1. 交付總表

| 項 | 狀態 |
|---|---|
| R-VF70／R-VF71 落檔 | **完成**（R-VF 現 63 條） |
| W-VF63 §6.1 `tc_title` 十條全改 | **完成** |
| W-VF63 §6.2 `listed` → `displayed` | **完成**（ER 未動） |
| W-VF63 §6.3 自檢增二項 ＋ 加註「已知集合，非全集」 | **完成，含可失敗性實測** |
| W-VF63 §6.4 逕開第 2 批 | **停手，見 §4** |

產物：`generated/vf230_pilot1_v4.json`（`supersedes: vf230_pilot1_v3.json`），
delta **17 處**（tc_title 10 ＋ procedure 7；三條之 procedure 原已為 `displayed`）。

---

## 2. v4 之二項取代

**§6.1**：十條之 `tc_title` 依 R-VF70 改為純句式、無冒號、括號別名移除
（別名保留於 `test_item`／`test_procedure`／`expected_result`）。
正向採 `is displayed and modifiable`。

**§6.2**：procedure 之 `is listed`／`is not listed` → `displayed`／`not displayed`。
**ER 未動**（其已為 `displayed`）。

**自檢**：`vf230_selfcheck_wvf62.py` 增二項（`tc_title` 不得含 `:`／不得含括號），
`PRE_FORBIDDEN`／`VERB_FORBIDDEN` 之定義處加註**「已知集合，非全集」**（R-VF71 三），
並具名其發現輪次。

**可失敗性實測**：人為將 `tc_title` 設為 `X: Y (Z)` → 二項皆報。
v4 全批自檢失敗 **0**。

> **一項自承**：新增二項之首版誤用變數名 `out`（實際為 `e`），
> **而真批因無冒號、無括號而未觸及該行，自檢仍報 0** ——
> 其錯只在人為破壞時才現形。**一個永不執行之檢查與一個通過之檢查不可分辨** ——
> A-VS106 之形態，且為本層本輪之第二次（前次為 V19 之寫死 `priority`）。
> **可失敗性實測即為此而設**，本輪因有做而查出。

---

## 3. V25 §6.1 之字數表 —— **又有二處誤**

依 **R-VF71 二**（分析層之量測須機械執行）複驗，判準為 `len(title.split())`：

| seq | V25 §6.1 所載 | 實測 | 判 |
|---:|---:|---:|---|
| 239 | 11 | **10** | 少 1 |
| 245 | 12 | **11** | 少 1 |

其餘八條相符。**無逾 14 字者**，故不影響結論。依 R-VF71 末句以實測為準。

**此為連續第二輪**：V24 §4 之表漏列 seq 241、seq 247 少算 1（V25 §2 已自記）；
本輪 V25 §6.1 又有二處。**R-VF71 二於其自身所在之包中即被違反一次。**

---

## 4. ⚠ **第 2 批停在生成之前** —— 其形態未經 pilot review

依 §6.4 取池首 11–20（seq 248–257）並讀其條文後，發現：

```
10 條中 —— PROXI 型（同 pilot #1）           4 條
            **訊號斷言型（pilot #1 完全未檢）**  6 條
```

訊號斷言型之條文形態為：

> When the customer chooses to enable the X setting …, the HMI layer shall send
> the updated customer preference to CarPropertyManager via the Android Car API
> … `CarPropertyManager.setProperty()` with the
> `TELEMATIC_VEHICLE_SETUP.<Sig>` signal value as `<Value>`

**其值域可解**（自 DBC）：`PLGAlert_Req` {off, on}／
`BSDEnable_Req` {not_enable, enable_led, enable_ led_chime}／
`Susp_Tire_Jack_Req` {off, on}／`Trailer_detection_blind_spot_Req` {auto, max}。

**惟其書寫形式（`Send CAN: MSG.Sig = raw (label)`／ER `… is sent`）
在 VF230 從未經 pilot review。**

### 4.1 停手之理由

V25 §6.4 令「逕行開第 2 批，不待本層再覆核 v4」，
**其所免除者為 v4 之覆核**（其修正無判斷餘地），
**非免除一個新形態之首次書寫之覆核**。

V25 §7 同時載明：「pilot 之覆蓋面限制不變 —— 本批十條同屬『PROXI 值決定設定項有無』
一型，**訊號斷言型、狀態轉換型、值域切換型未受檢**。**pilot #2 之分層取樣仍須為之**，
其時點建議在第 2–3 批之後」。

**該建議之前提為「第 2–3 批仍為已檢之形態」** ——
而實測第 2 批即含 6 條未檢形態。**前提不成立。**

**若逕行生成，其結果為：一個從未經 review 之書寫形式，
以 6 條之量直接進入量產批次。** 而 pilot review 之存在目的正為防此。

### 4.2 本層不自行決定，請示

三個選項，本層不擇一：

1. **照原令生成第 2 批**（10 條混合形態），其 6 條訊號斷言型於該批之上繳中
   一併受檢 —— 等同以第 2 批兼作該形態之 pilot。
2. **第 2 批改取同形態之 10 條**（PROXI 型），將訊號斷言型延後至 pilot #2。
   **惟此須偏離 R-VS58 之選池序**，屬裁定事項。
3. **提前 pilot #2 之分層取樣**，其樣本涵蓋訊號斷言型。

**本層之觀察（非建議）**：選項 1 之成本為「若形式有誤，6 條須改」，
而 pilot #1 之經驗為 v1→v4 共四版 —— **形式之首次書寫平均需三輪修正**。

---

## 5. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，三項。**

1. **v4 之 `test_item` 未複驗其與條文之逐字一致性。** V24 已核 v3 之引號插入
   未誤傷 `test_item`，而本輪之 delta 不觸及該欄 —— **惟本層未自行複驗**，
   係承接 V25 §1 之「delta 已核」。

2. **§4 之形態統計（4 PROXI ／ 6 訊號斷言）以條文首句之形態判**，
   未逐條讀全文。**其分類可能有誤**，惟其結論（含未檢形態）不因個別誤分而改變。

3. **`.HEAD_V19` 三旁檔、`vf230_batch01.json`、`vf230_pilot1.json`（v2）、
   `vf230_pilot1_v3.json` 皆未刪**。v4 已 `supersedes` v3，
   **而 v2 之檔名 `vf230_pilot1.json` 與 v4 之 `vf230_pilot1_v4.json` 並存**，
   易被誤取。**刪檔屬 Pei**，本層具名。
