# V48 — DBC 實測：對 VF230 零影響，且新本非較新；拆題得逕行

下放包 **V48**。所據：Pei 於 2026-08-24 給出之路徑
`/Users/peihe/Work_Projects/TC_Generator/forms`
＋ 分析層對該目錄二本 DBC 與現行 `inputs/` 二本之**逐訊號 diff**。
新增 **一條**（開號取實測最大 +1，**回報實得之號**）。
**W-VF80 之 §5.1-2（DBC 阻斷）解除**，其餘不變。

---

## 1. `forms/` 之實測

```
forms/PDT27_E2A_R1_FDCAN8.dbc                          1.06 MB
forms/PDT27_E2A_R1_BHCAN2.dbc                        163.31 KB
forms/Logical Identifiers and CAN Mapping v1_78.xlsx     609 KB   ← 現行 inputs/ 為 v1_76
forms/PROXI_HDCC27_R3_20250424.xlsx                      726 KB   ← 與 inputs/ 同名
forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx         196 KB
forms/FORMS.md ／ LOOKUP_MISSES.md
```

---

## 2. FDCAN8 之逐訊號 diff（`R5`（現行）vs `R1`（`forms/`））

```
                現行 R5      forms R1     交集     僅 R5     僅 R1
BO_（訊息）        323          318        318       5        0
SG_（訊號）       1755         1634       1633     122        1
VAL_（值域）      1512         1395       1394      —         —
```

**值域相異之訊號：3。**

| 訊號 | 僅 R5 有 | 僅 R1 有 |
|---|---|---|
| `TGW_CAMERA_DISP_STAT` | `9 DISP_TRAILER_SURROUND_CAMERA` | — |
| `Lane_DispPopupSts` | `140 SIALC_Confirmation` | — |
| `ACC_DispPopupSts` | `112 ACC_Unavailable Parking Maneuver`／`113 ACC_Limited_Map_Unavailable` | `112 Stopping_Ahead`／`113 Press_xx_Confirm_To_Pass`／`118`–`121` 六項 |

**僅 R5 有之 122 個訊號，其大宗為高壓電池族**
（`BMS_HV_*`／`BPCM_HV_*`／`HVBatCellVoltage_Cell0xx`／`ChargeSystemSts` 等）；
**僅 R1 有之 1 個為 `EngRPM_Tach`（引擎轉速）。**

---

## 3. 【裁定】`forms/` 之 DBC **非「較新」，為另一車型變體**

```
R-VF-甲（`forms/` 之 DBC 之定位，分析層裁定 2026-08-24）
【落檔取實測最大 +1】

**Pei 稱其為「最新的 dbc」，而實測不支持「較新」之讀法**：

  一、**版號相反**：現行為 `R5`，`forms/` 為 `R1`。
  二、**檔名不同族**：現行 BH 側為 `R4_BHCAN`，`forms/` 為 `R1_BHCAN2`
      —— **`BHCAN2` 與 `BHCAN` 非同一匯流排之不同版次，而是不同之匯流排名。**
  三、**訊號之增減呈變體形態而非版次形態**：
      減去 122 個高壓電池／充電系統訊號、增加 1 個引擎轉速訊號
      —— **其為 BEV → ICE（或含引擎之變體）之差異，非時間上之演進。**
      版次演進通常為增補與修訂，**不會整族移除電池訊號而換入引擎訊號。**

**故：`forms/` 之 DBC 不取代 `inputs/` 之現行本。二本並存。**

**其取用依車型判定**，而 VF230 之目標車型未載於本層現有素材。
**開 DR 詢之**（查 `DATA_REQUESTS.md` 最大已用號；登記，送出屬 Pei）。

**本裁定為「不取代」，非「不採用」** —— 其差異之 3 個值域與 122 個訊號
若日後證實與 VF230 相關，**須以該 DR 之覆文為據，不以本層之推定為據。**

**`Logical Identifiers and CAN Mapping v1_78.xlsx` 之處置另計**
（現行 `inputs/` 為 `v1_76`，**其版號為遞增，與 DBC 之情形不同**）——
**其為真正之較新本，須複驗**（見 §5 第 4 項）。

**若 Pei 明示 `forms/` 之本即 VF230 之正確目標，本條即改用，不待 DR。**
```

---

## 4. 對現行 440 條之影響：**零**

**量測**：自 `docs/reports/vf230_writeback_preview.tsv` 之
`I`／`J`／`K`／`L`／`M` 五欄抽出 `MESSAGE.Signal` 形態之 token（**159 個**），
與二本 DBC 之 `SG_` 集合比對。

```
在現行 R5 內       157 / 159
在 forms R1 內     157 / 159
舊有而新無          **0**
新有而舊無          **0**
```

**VF230 所用之訊號，二本 DBC 皆有且完全一致。**
§2 之 3 個值域相異訊號**皆不在 VF230 之 159 個 token 內**。

**故：DBC 之更換與否，對現行 440 條之訊號名與值域皆無影響。**
**W-VF80 §5.1-2 之阻斷解除，拆題得逕行。**

**未在任一 DBC 內之 2 個 token** 推定為抽取式之假陽（形如 `X.Y` 而非訊號者），
**其身分須於 W-VF81 具名 —— 推定不得代替實測。**

---

## 5. W-VF81 — 拆題（**承 W-VF80，DBC 阻斷已解除**）

1. **VF230 自身之拆題倍率量測**，依 V47 §3 之壓力測試逐條判其
   可獨立觀察之結果數，回報分布與總數。**不得以 PM 之 2.23 外推。**
2. ~~DBC 到位後複驗值域~~ —— **本包已測，零影響，本項刪除。**
3. **10 條試作**（拆出最多之前 3 個 leaf ＋ 不拆之 2 個），
   依 V47 §2 之括號下半格式與 §3 之驗證點單位。
   逐條回報：原 leaf、拆出列數、各列下半逐字、摘句後之上半 token 數。
4. **【新】`Logical Identifiers and CAN Mapping v1_78` 之複驗** ——
   其版號較現行 `v1_76` 遞增，**且 LID 為值域來源鏈第一位（R-VF13），
   其位階在 DBC 之前**。比對二本於 VF230 所用訊號上之差異，逐項回報，
   有差異者具名其影響條數。**只比不換。**
5. **【新】159 個 token 中 2 個不在任一 DBC 者之身分**（§4 末）。
6. **開 §3 所令之車型 DR**（登記，未送出）。

**自檢增四項**（V47 §5.3）不變：
```
test_item 不含 "\n\n(" 或不以 ")" 結尾   → FAIL
test_item 上半 token > 50                → FAIL
同一上半之各列，下半逐字相同             → FAIL
下半不含 " -> "                          → FAIL
```

**不得全量重生成** —— 待第 3 項之 10 條經覆核。

---

## 6. 給 Pei —— 一件與你所述不符者

你稱 `forms/` 之 DBC 為「最新」，**而實測顯示其為另一車型變體，非較新版次**：

```
版號    現行 R5     →  forms R1         （相反）
BH 側   現行 BHCAN  →  forms BHCAN2     （不同匯流排名）
訊號    減 122 個高壓電池族，增 1 個引擎轉速
```

**若你確知 `forms/` 之本為 VF230 之正確目標，請直接告知，本層即改用，不待 DR。**

**好消息**：無論取哪一本，**對現行 440 條零影響**（157 個訊號二本皆有且一致），
**故拆題不必等此事釐清即可開始。**

**另一件**：`forms/` 內之 `Logical Identifiers and CAN Mapping v1_78.xlsx`
**版號較現行 `v1_76` 遞增，其為真正之較新本**。
LID 為值域來源鏈第一位，位階在 DBC 之前，已令複驗（§5 第 4 項）。

---

## 7. 新條文清單（自檢）

| 暫稱 | 內容 |
|---|---|
| 甲 | `forms/` 之 DBC 非較新而為車型變體；不取代現行本；二本並存待 DR；LID v1_78 另計 |

**⚠ 編號於落檔時取實測最大 +1，並回報實得之號。**

**工單**：W-VF81（承 W-VF80；DBC 複驗項刪除；增 LID v1_78 複驗、2 個 token 身分、車型 DR）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
