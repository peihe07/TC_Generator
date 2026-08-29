# RULINGS — ICS Management (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。前綴 `R-ICS` / `A-ICS` / `DR-ICS`，
不與既有 feature 共用序號。取號依 R-G23：落檔當下 grep 本檔與
`docs/handoff/` 全目錄，不得自記憶推定。

來源：2026-08-29 chat 偵察報告＋分析層判斷四項，Pei 同日「准」
（①命名 ②DR-ICS1~9 即發 ③首波動工面 ④落檔骨架）。

---

## R-ICS1

```
R-ICS1（feature 命名）

slug = `ics_management`，Test Group = `ICS`。
依據：三份來源檔名／題名均為 ICS Management／ICS Buttons Management，
「Integration」於全部來源零命中；IN §4.1.1 Layer 1 取 spec 題名。
Pei 口頭之「ICS Intergration」判為代稱，不入檔。
```

---

## R-ICS2

```
R-ICS2（CFTS022 適用域，暫定）

CFTS022 物件適用判準：ECU ∋ {ICS, LTM} ∧ Radio ∋ {R1L, R1L-R, allSys}
∧ EE ∋ {Atlantis High, All}。

{ICS, LTM} 聯集為暫定：Stuck Button 物件 ECU 列 ICS，Volume 物件
（4914972–76）僅列 LTM/ETM/RRM，而 DUT 實為 HU 側軟體（SYSAD 通篇
AAOS14 HU 棧）。邊界由 DR-ICS9 上游確認；裁定收窄時，受影響 TC
以 A- 登冊回收，不靜默改判。
```

---

## R-ICS3

```
R-ICS3（Tstuck_button 首波取值，暫定）

<Tstuck_button> 首波採 120 秒，來源 CFTS022 物件 4914956（HU 側，
ECU 明列 ICS，Radio allSys，EE 含 Atlantis High）。
SCCM 側之 10 分鐘（4914954）不適用本 DUT。
SWRA 所稱「configured」之組態值由 DR-ICS7 上游確認；
確認值異於 120 s 時回收修正。非造值（IN §8.7.1 spec-sourced）。
```

---

## R-ICS4

```
R-ICS4（verbatim 來源分流：SWRA Description 錯置期間）

A-ICS1 五列（001/005/006/009/010）之 SWRA Description 不得作
test_item 上半之 verbatim 來源。依 IN §8.6（來源 spec 勝過索引輸出），
凡 CFTS022 有直載原句者（現況：010 之 4914955/56/57；001 之 4914975/76），上半 verbatim
取 CFTS022 原句，specification_reference 錨 CFTS022-{ObjectID}；
CFTS022 無載者（005/006/009）俟 DR-ICS1 回覆，不得動工。
未受錯置之列（002/003/004/007/008）仍以 SWRA Description 為上半來源。
```
