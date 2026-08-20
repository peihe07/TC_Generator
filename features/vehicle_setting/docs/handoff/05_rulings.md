# 05 下放包 — Pei 裁決全案落檔（2026-08-20）

分析層寫入。Pei 指示「全都裁定」，即**採分析層各包所附之建議**。
本檔為裁決正文，逐條以可直接貼入之區塊呈現。
**執行層須將 §1～§10 逐字轉錄入 `features/vehicle_setting/RULINGS.md`**
（不得摘要、不得以編號代替），並於 `ANOMALIES.md` 套用 §11 之狀態變更。

> 落檔註記：本檔於 2026-08-20 首次 `write_file` 逾時，實測為**完全失敗**
> （ENOENT，非零位元組）。MCP 重啟後重寫。內容與逾時當時之聊天備份一致。

---

## 1. R-VS7 — Comfort 重疊之委派界線

```
R-VS7（Pei 2026-08-20）
本 feature 與 Comfort（CFTS043 / Comfort HMI Logic and Flow）之界線採
**分層委派**：

  Comfort 擁有：座椅加熱／通風／方向盤加熱之**畫面行為**
                （按鍵循環、LED 與箭頭數、highlight、seat zone 彈窗、
                  Front Comfort 與 Status Bar 之控制列）
  Vehicle Setting 擁有：同一批實體功能之**訊號與配置層**
                （CAN 狀態值、失效狀態、按鍵請求訊號、
                  PROXI／車型配置分支）

推論（binding）：
(a) 本 feature 之 TC 不重複驗證 Comfort 已擁有之畫面行為。
    需要提及畫面時，以 §8.2.1 之委派句於 reasoning 指名 Comfort 之
    對應 leaf id，不寫入 procedure／expected_result 之斷言。
(b) 例外：CFTS044 條文自身以 `Refer to TLM HMI Document` 指出畫面
    行為者（16 leaf），其畫面層斷言仍屬本 feature，惟在 DR-5-B
    到位前標 BLOCKED（見 R-VS17）。
(c) 佐證：CFTS044 內文以 `{CFTS043}` 顯式引用 Comfort 規格 3 處。

**W-9 之角色改變**：其產出由「裁定素材」變為「委派句之來源對照表」。
故 **W-9 之「做完必停」解除**，改為做完併入該輪上繳，不中斷批次。
```

---

## 2. R-VS8 — 追認

```
R-VS8（Pei 追認 2026-08-20）
本 feature 之 CAN 基線為兩份並用，非二擇一：

  PDT27_E2A_R4_BHCAN.dbc   BH-CAN／CAN-B 網段。STATUS_CSWM、
      STATUS_CLIMATE8、TELEMATIC_DISPLAY2、TELEMATIC_VEHICLE_SETUP3、
      STATUS_BH_BCM2 全部在此。**主要來源。**
  PDT27_E2A_R5_FDCAN8.dbc  CAN-FD 網段（BA_ "BusType" = "CAN FD"）。
      TELEMATIC_FD_4、BCM_FD_10 等 FD 對應。**指明 FD 網段時引用。**

兩檔 VersionYear = 25、VersionWeek = 50，完全相同；R4／R5 在本組檔名
中指網段，不指 release，不存在選錯版本之風險。

配套判準（適用於日後任何 DBC 之入庫）：
DBC 之身分由檔內 BA_ "VersionYear" / "VersionWeek" / "BusType" 三項
屬性判定，不由檔名之 R 碼判定。入庫時記錄該三項屬性與 SHA256。
```

---

## 3. R-VS9 — CAN 訊號書寫形式（v2 定案）

```
R-VS9（Pei 2026-08-20，取代一切先前草案）
TC 中書寫 CAN 訊號時：

(1) 訊號逐字名與所屬 message 以 Logical Identifiers and CAN Mapping
    之對應欄組為第一權威：
      - `CAN Mapping` 分頁 → `Atlantis High` 欄組
      - `Proxi & Configuration` 分頁 → `Atlantis & Atlantis High` 欄組
        （該欄組同時涵蓋兩種架構，見 R-VS11）
(2) 值域以同表 Format 欄為準，並與對應 DBC 之 VAL_ 表交叉核對；
    兩者不一致時停下回報，不自行調和。
(3) **訊號斷言須同時指明 message 與網段**，三者成組出現，缺一不可：
        <signal 名> in <message 名> on <網段>
    例：STATUS_CSWM.HSW_StatFailSts in STATUS_CSWM on CAN-B
    理由：兩份 DBC 之 141 個共有 signal 中 128 個起始位元不同（91%），
    只寫 signal 名不足以定位量測點。
(4) 網段對應：CAN-B／BH-CAN → PDT27_E2A_R4_BHCAN.dbc；
    CAN-FD → PDT27_E2A_R5_FDCAN8.dbc。
(5) `$var$` 形態僅出現於 test_item 上半段之來源逐字內，不出現於
    procedure／expected_result 之作者自撰文字。
    理由：`$PowerMode$` 之匯流排名為 `CmdIgnSts`，DBC 內另有一支
    `PowerModeSts`；以 `$var$` 檢索會抓到錯的訊號。

lint 判準（L-VS1）：procedure／expected_result 內出現 DBC signal 名而
同句無 message 名者 FAIL。
**該規則須附範圍向（R-G9）**：對 test_item 上半段之來源逐字不得轉紅，
且須以實測證明其對該類輸入不轉紅。
```

---

## 4. R-VS10 — Pop Up List 基線

```
R-VS10（Pei 2026-08-20）
本 feature 不採用任何版本之 Pop Up List：CFTS044 全文對 `Pop Up`
與 `Settings List` 之命中皆為 0，本 feature 條文不引用該文件。

`features/comfort/inputs/` 之 SR24 Post 2A (Dec 15, 2023) 版與
`26PI2.5/HMI/` 之 26PI 版之差異（A-VS09），**不在本 feature 之範圍內**，
不因本 feature 而處置。

若 DR-5-B（失效彈窗）之上游答覆指向 Pop Up List，本條重議。
`DATA_REQUESTS.md` 須留「已查而不取用」之痕（G-D）。
```

---

## 5. R-VS11 — 撤回之追認

```
R-VS11（Pei 追認 2026-08-20：撤回）
「LID 表之 Atlantis 欄能否代 Atlantis High」不是待裁事項。
`Proxi & Configuration` 分頁列 2 之欄組標題逐字為
`Atlantis & Atlantis High`，即該欄組同時涵蓋兩種架構；
`CAN Mapping` 分頁則二者分列。

故該 10 個 PROXI 類參數之 Atlantis 欄值，對 Atlantis High 直接適用，
不需假設、不需 RD-1、不需於 profile 標註為假設。

本條以撤回形式記載，不以「已裁定」記載 —— 它從來不是判斷問題，
是一次讀漏。
```

---

## 6. R-VS14 / DR-10 — 追認

```
R-VS14（Pei 追認 2026-08-20）
specification_reference 為字串清單，非單值（§10.7 明文：String list、
Multiple specs allowed）。leaf 對映到多個 CFTS044 章節者，逐一列出
全部章節，依 §10.7 由最具體排至一般。

實測之 5 個多章節 leaf：
  SWE1-VC-LeftFrontHeatedSeat-004      1.3.2.1.3.1 ~ .4
  SWE1-VC-LeftFrontHeatedSeat-011      同上
  SWE1-VC-HeatedSteeringWheelManagement-025 / -026 / -027
                                       1.3.2.1.3；1.3.3.3.6.1

**DR-10 撤銷** —— 單值形式從來不是政策，是分析層敘述時之簡化。
```

---

## 7. R-VS15 — 追認

```
R-VS15（Pei 追認 2026-08-20）
本 feature 之 TC 母體為 037 四份中 `Categorization` 開頭為 `Functional`
（不分大小寫）之列，共 237 個 leaf：

  Common Features 46／Heated Seat 88／Vented Seat 72／Heated Steering Wheel 31

其餘 34 列（Heading 25／Information 9）為文件結構與說明，非可測需求，
不產 TC、不佔 036 之列、不計入覆蓋稽核之分母。

`Categorization` 之值域全集（271 列逐列取值）：
  Functional Requirement 237／Heading 25／Information 8／information 1
  —— 四值合計 271，無其他值、無空值。

推論：
(a) 「34 個未覆蓋 leaf」之表述作廢。**本 feature 沒有覆蓋缺口。**
(b) 覆蓋稽核判準：TC 數 >= 237，且每個 Functional leaf 至少一列
    （§8.2.2：一 leaf 得對多 TC，反向不可）。
(c) 271 僅用於描述 037 之列數，不得作為任何比率之分母。
(d) N 欄：可測 leaf 237 中已定 236、未定 1（DR-11）。
```

---

## 8. R-VS16 — `.gitignore` 例外

```
R-VS16（Pei 2026-08-20）
features/vehicle_setting/.gitignore 於 `inputs/` 之後增列：

    !inputs/INPUTS.sha256

理由：canon G-9 明文要求雜湊檔入版控；現行 .gitignore 註解之意旨為
「不提交客戶素材」，雜湊檔非素材。無此例外則素材落地之證據鏈在
版控中是斷的。

範圍：僅及於 INPUTS.sha256 一檔，不及於 inputs/ 內任何其他檔案。
其餘 feature 之同一缺陷不在本裁定範圍，各自於下次開輪次時自檢。

**執行由 Pei**（版控政策 + git 皆屬 Pei）。
```

---

## 9. R-VS3′ — 目錄名之修正

```
R-VS3′（Pei 2026-08-20，修正 R-VS3 之內部不一致）
Test Group（036 G 欄）= `Vehicle Setting`（單數，逐字）—— 不變。
feature 目錄 = `features/vehicle_setting` —— 不變。
scaffold 指令參數改為 `vehicle_setting`（原記之 "Vehicle Setting" 會
產生含空白之目錄，見 A-VS19）。

`features/vehicle setting/`（含空白之誤建目錄）由 Pei 刪除。
`new_feature.py` 之名稱正規化缺陷（`scripts/new_feature.py:144` 僅
`feature.lower()`，不轉空白）維持登記為工具缺陷，不在本 feature 修。
```

---

## 10. R-VS17 — BLOCKED 之適用範圍

```
R-VS17（Pei 2026-08-20，配合 R-VS7(b)）
DR-5-B（失效彈窗內容、加熱方向盤圖示之左右駕鏡像）未到位期間：

  受影響之 17 leaf（16 引 TLM HMI Document ＋ 1 引 PDO graphics）
  仍產出 TC，其 ER 寫至**訊號層**為止
  （例：STATUS_CSWM.FL_HS_STATFailSts in STATUS_CSWM on CAN-B
        之值為 Fail_Present），
  **畫面層之斷言以 Remarks 標 BLOCKED 並註明其待補來源**，
  不寫入 expected_result。

不得以「畫面文字未知」為由不產 TC —— 訊號層可測且來源明確
（canon：「不知道適用於誰」≠「不知道存在什麼」）。
```

---

## 11. 異常狀態變更（執行層於 `ANOMALIES.md` 套用）

| id | 變更 |
|---|---|
| A-VS01 | **除役** —— 037 `Categorization` 對 SYS2 `Category` 逐 leaf 零錯配 |
| A-VS06 | **id 更正為 A-VS06′**，狀態除役（差額 16 為轉檔文字之產物） |
| A-VS18 | **除役** —— recon 未錯，兩判準數兩件事 |
| A-VS07′ | 維持登記（FYI 類，RD-1） |
| A-VS20 | 維持登記（RD-1 FYI；措辭依 02 包 §1.3 之方向） |
| **A-VS21** | **新開**：分析層經 MCP 讀取含中文之 repo 檔時偶發單字元顯示為替代字元；曾兩度被誤報為「檔案疑似毀損」，位元層實測 `U+FFFD` = 0。**通則：跨層回報「檔案毀損」前須先位元層確認** |

---

## 12. Pei 待執行之動作（**裁決已定，執行仍屬 Pei**）

```bash
# P1 刪除誤建之空白目錄（R-VS3′）
ls -la "features/vehicle setting"        # 先確認其內僅 scaffold 模板
rm -rf "features/vehicle setting"

# P10 .gitignore 例外（R-VS16）
#   於 features/vehicle_setting/.gitignore 之 `inputs/` 次行加入：
#       !inputs/INPUTS.sha256

# P2 入庫（00／01 兩輪產物 + 本裁決）
git add features/vehicle_setting/.gitignore \
        features/vehicle_setting/inputs/INPUTS.sha256 \
        features/vehicle_setting/RULINGS.md \
        features/vehicle_setting/ANOMALIES.md \
        features/vehicle_setting/DATA_REQUESTS.md \
        features/vehicle_setting/DECISIONS.md \
        features/vehicle_setting/docs/ \
        features/vehicle_setting/data/ \
        features/vehicle_setting/feature.yaml \
        features/vehicle_setting/RECON.md \
        features/vehicle_setting/PLAYBOOK.md \
        features/vehicle_setting/RUNBOOK.md
git commit -m "feat(vehicle_setting): rounds 00-01 intake and recon; rulings R-VS1..R-VS17"
```

---

## 13. 裁決後之淨效果

| 影響 | 內容 |
|---|---|
| **解除阻塞** | R-VS9 定案 → lint 規則可定稿 → W-8 完成後不再擋 pilot |
| **解除 gate** | R-VS7 定案 → **W-9 之「做完必停」解除**，改為併入上繳 |
| **母體確立** | 237 可測 leaf，四 Test Set 為 46／88／72／31 |
| **仍開啟** | DR-11（CFTS100，1 leaf）、DR-5-B（失效彈窗＋PDO 圖示，17 leaf 之畫面層）、DR-7（PROXI 表）、DR-8（VC_VEH_LINE 車型碼） |
| **下一個人工 gate** | **pilot**（canon §1.2）。其前置為：02 輪殘項完成 → framework Part Vehicle Setting ＋ profile → 首批生成 |

---

## 14. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS7 | Comfort 分層委派；W-9 必停解除 | ✔ §1 |
| R-VS8 | 兩份 DBC 並用（追認） | ✔ §2 |
| R-VS9 | CAN 訊號書寫形式 v2 定案 ＋ L-VS1 | ✔ §3 |
| R-VS10 | 不採用 Pop Up List | ✔ §4 |
| R-VS11 | 撤回追認 | ✔ §5 |
| R-VS14 | spec_reference 為清單；DR-10 撤銷 | ✔ §6 |
| R-VS15 | 可測母體 237 ＋ 值域全集 | ✔ §7 |
| R-VS16 | `.gitignore` 例外 | ✔ §8 |
| R-VS3′ | 目錄名修正 | ✔ §9 |
| R-VS17 | BLOCKED 適用範圍 | ✔ §10 |

十條皆以獨立可貼入之區塊呈現，未夾在敘述中。
