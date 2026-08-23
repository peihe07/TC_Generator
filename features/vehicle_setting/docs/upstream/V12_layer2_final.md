# 上繳 V11＋V12 —— 提案 C 判 (b)、CROSSLINE 建立、driver 尾段機械化

執行層寫入。依據：`docs/handoff/V11_layer2_and_regression.md`（**本輪前未執行，
於此一併補做**）＋ `docs/handoff/V12_layer2_final.md` §5。canon §8.2 六節。

**本輪未生成 TC、未執行任何寫回**（R-VF26）、**`framework.md` 未寫入、未鎖**。

> **先具名一項流程事實**：V11 下放後未經一次上繳即續發 V12，
> 致 R-VF32–R-VF35、A-VF9、DR-31、W-VF29–W-VF31 於本輪前**全未執行**。
> 本包一併補做。**此與 R-VF30 所欲防者為對稱之另一面** ——
> R-VF30 令分析層成文前須讀最新上繳；本例為**上繳尚未存在即續發**。

---

## 1. 交付總表

| 項 | 狀態 | 產物 |
|---|---|---|
| R-VF32–R-VF35 補落（V11） | **完成** | `RULINGS.md` |
| A-VF9 補落 | **完成** | `ANOMALIES.md` |
| DR-31 開立（R-VF34 第 3 項） | **完成（未送出）** | `DATA_REQUESTS.md` |
| R-VF36–R-VF39 落檔（V12） | **完成** | `RULINGS.md`（R-VF 現 **30 條**） |
| W-VF31 提案 C 之表 | **完成，判 (b)** | `docs/reports/wvf31_layer2c.md`、`scripts/vf230_wvf31_layer2c.py` |
| W-VF32 `CROSSLINE.md` ＋ 全集盤點 | **完成** | `CROSSLINE.md`、`PLAYBOOK.md` |
| W-VF30 (b) 先行 ＋ (a) 授權施行 | **完成，含可失敗性實測** | `scripts/grade_overrides.py`、`scripts/writability_driver.py` |
| W-VF29 跨界簇之代理查證 | **完成** | 本檔 §5 |

---

## 2. W-VF31 —— 提案 C：**判 R-VF37(b)，framework 未鎖**

依 R-VF36 之二條件規則**逐簇**過（不批次）：**移動 33 筆／留置 85 筆**，
12 個跨界簇依起點二整併，合計 **627**（自各 Test Set 重算）。

**形式上合 (a)**：Test Set 名為已核可 11 名之**子集**，新名 0、消失 0。
**實質判 (b)**，二理由：

### 2.1 規則以單一泛用詞誤配（鑑別錨點證實）

**鑑別錨點 `Power Unit`**（量測單位，與 `Switch Power Mode` 僅共用泛用詞
`power`）—— **實測被移入 `Switch Power Mode`，錨點不符。**

同型者：`Charge Power Level`(8)／`Engine Off Power Delay`(7)／
`Power Side Step`(5)／`Hour Mode`(4，時間)／`Max Power Level`(4)／
`Rear Guidance Lighting with Approach`(5→`Daytime Lighting`)。

**泛用詞之操作型定義（可量測）**：出現於跨 ≥3 個 Test Set 之簇章名者。
本輪 18 個，以其為唯一相交依據之移動 **24 筆**。

> **本診斷之界限（已於報告具名）**：`suspension` 亦被判為泛用詞，
> 故 **R-VF36 起點一之 4 筆 Suspension 移動亦落入該 24**，而該 4 筆語義正確。
> **「相交詞為泛用詞」不等於「該移動錯誤」** —— 診斷只證規則之依據
> 不足以區辨，不證每一筆皆錯。

### 2.2 **規則之產出與其立法意圖相反**

R-VF36 起點二令「12 個跨界之 SWITCH 簇整併入 `Auxiliary Switches`」，
而**同一規則將 SWITCH 1–6 之 Power Mode／Type／Hold Last State 全數移出
`Auxiliary Switches`**（相交詞 `switch`／`power`／`mode`／`type`／`state`）。

結果：`Switch Power Mode`(45) 與 `Switch Type and State`(12) **不但未消失，
反成 SWITCH 專屬 Test Set** —— 而 **V11 §7 之整個論證即為此二名不成立、須消去**。

且跨界之 12 簇因起點二而整併、非跨界之 SWITCH 5／6 則被規則移走 ——
**同族之簇因是否跨界而分屬不同 Test Set**。

**本層未改 R-VF36 之規則**（其為裁定，且本層無權以自訂之區辨力門檻取代之）。
**逐筆列出待裁。**

### 2.3 C 案之表（供參，未鎖）

```
136 Trailer and Signage    104 Driver Convenience     87 Auxiliary Switches
 63 Units and Cameras       62 Suspension and Comfort  49 Lane and Lighting
 45 Switch Power Mode       41 Approach and Tailgate   17 Daytime Lighting
 12 Switch Type and State   11 Measurement Units       ── 合計 627
```

canon §4.1.3：**過細否** 11 set／平均 57／最小 11 → 否；**過粗否** 無收容簇 → 否。

---

## 3. W-VF32 —— `CROSSLINE.md` 與全集盤點

`CROSSLINE.md` 已建（**34 行，一頁內** —— R-VF38 一之「短是其有效性之前提」）。
`PLAYBOOK.md` 之 `接手` 讀取清單已加本檔**且置首**（R-VF38 二，兩線皆適用）。

**全集盤點（不抽樣）**：`RULINGS.md` 之 **22 條 R-VF** 中，
**16 條之效果落於他線產物**（Part 1 之 driver／分級產物／leaf 資料／交付，
或兩線共用之腳本、設定、簿冊、編號空間）。

```
受保護（有能失敗之檢查）    3   R-VF17／R-VF20+32+39／R-VF16
未受保護                   13   R-VF10・23／R-VF18／R-VF21・28／R-VF26／
                               R-VF13 第 5 項／R-VF33 等
```

**依 R-VF38 三，13 條之跨線效力現為「未受保護」，於此具名。**
其非「未生效」—— 條文仍有拘束力，惟其被無聲違反之風險未被消除。

---

## 4. W-VF30 —— (b) 先行，(a) 依 R-VF39 施行

**(b)**：`--check` 已擴及 `writable`／`blocker_class`／`blocker_detail`／
`evidence_note` 四欄（R-VF29 第 6 項），與 `--apply` **共用單一 `expected_row()`**。

**(a)**：`writability_driver.py` 之 `--write` 尾段新增呼叫覆寫層。
**差異 18 行，全在 `__main__` 尾段**；`value_sourced()` 及任何分級判定邏輯
未觸及（R-VF39 約束 1）。

**R-VF33／R-VF39 約束 2 之消費者清單**：

```
誰呼叫 driver      無腳本呼叫；僅 RUNBOOK.md／PLAYBOOK.md 之文件指示
其輸出被誰讀       16 支腳本（batch15–19／endgame／redundancy／warn18／
                   domain_gap／preamble_criterion／各 anchor 腳本／
                   vf230_wvf14_registry／vf230_wvf18_rd1／grade_overrides）
exit code 之語義   __main__ 現無 sys.exit，恆為 0
```

**本次修改未改變 exit code 語義** —— 覆寫層失敗時只印 stderr，不改 exit code，
以免影響 16 個下游之判讀。**此為刻意之限縮，於此具名。**

**可失敗性實測**：人為將 4 leaf 改回 `W2`／`B6-value-absent` →
跑 `driver --write` → 尾段自動覆寫 4 筆 → `--check` exit 0。

**約束 4**：施行前實測 `git status`，driver 無併行線之未提交變更。

---

## 5. W-VF29 —— 12 跨界簇之代理查證：**兩半確有系統性差異，但只在 4 個簇**

以條文形態為可測代理（`HMI layer shall send`／`HW supplier shall notify`／
`display`／`LTM or ETM shall`），逐簇比對兩半：

| 簇群 | 數 | `6 Aux Switches` 半 | 另一半 | 判 |
|---|---:|---|---|---|
| SWITCH 1–4 **Type**／**Hold Last State** | 8 | 顯示 2 ＋ HW通知 1 | 顯示 2 ＋ HW通知 1 | **形態相同，無系統性差異** |
| SWITCH 1–4 **Power Mode** | 4 | 顯示 2 ＋ HW通知 1 | **HMI送出 2 ＋ 顯示 1** | **形態不同** |

→ **4 個 Power Mode 簇之兩半非同質**：一半為顯示與 HW 通知，
另一半為 HMI 送出。**依 V12 §5 之 W-VF29，該差異須記入 Layer 3 或
`reasoning`，以免 TC 書寫時將二者當作同質。**

**本層未合併亦未分割該 4 簇**（其歸屬由 R-VF36 起點二所定）。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **R-VF36 之規則須修訂方能產出可鎖之表**（§2）。本輪之 C 案含已證之誤配，
   且與其起點二相反。**Layer 2 因而仍未鎖，TC 生成之最後一閘仍關。**
   **此為本輪最須處置者。**

2. **13 條跨線條文「未受保護」**（§3）。本輪只完成盤點與登錄，
   **未為任一條新增檢查**（W-VF32 第 5 項明令只盤點）。
   依 R-VF38 三，此狀態須於**每次上繳**具名，直至補齊。

3. **W-VF31 之移動規則未經上游查證**，與上繳 V10 §6 第 2 項同一形態 ——
   本層只測「章名主題詞相交與否」，**未查上游為何如此分章**。
   規則之修訂若仍不問上游意圖，下一版仍可能誤配。

4. **`CROSSLINE.md` 之有效性未經實測**。其立法目的為使併行線讀到，
   而**本輪無從驗證併行線是否會讀** —— 與 A-VF8 所證之
   「`RUNBOOK`／`PLAYBOOK` 已載而未被遵行」為同一風險。
   **真正之保證仍在機械檢查**（R-VF38 三已如此明定），
   而 13 條尚無檢查。

**另**：本輪補做 V11 時發現，**V11 下放後未經上繳即續發 V12** ——
R-VF30 令分析層成文前須讀最新上繳，而此例為**上繳尚未存在**。
**建議 R-VF30 增一項**：續發下放包前，須確認前一包已有對應上繳；
無者於新包中明列「前包未執行之工單」清單，避免其靜默沉沒。
