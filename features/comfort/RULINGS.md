# RULINGS — Comfort (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Comfort 之裁決權威；
跨 feature 條文承接時註明來源包。

**檔案建立於 2026-08-14**（下放包 01 §5.1）。R-C1～R-C5 原文取自
`docs/handoff/01_phase0_intake.md` §3，R-C6～R-C7 取自
`docs/handoff/02_rulings_addendum.md`，皆 2026-08-14 已簽。
Comfort 現**無 open PENDING**（01 §4 之 P-C1／P-C2 已由 R-C6／R-C7 關列）。

---

## R-C1 ~ R-C5 —— 下放包 01 §3（Pei 裁定，2026-08-14）

```
R-C1  spec baseline
Comfort feature 之 spec baseline 採 SWE.1（037）所引用者，即
SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)。

spec_reference stem 一律使用上列 SR24 檔名，與 037 之 HMI Source ID 完全一致，
不得改寫為 SR25。

SR25 CR29359 (Feb 24 2025) 於本 feature 為 out-of-scope 參考資料，不得作為
spec 來源、不得用以推翻 SR24 之字面內容、不得據以擴張驗證範圍。

依據：037 之 HMI Source ID 129/129 全數指向 SR24 CR24879；trace chain 完整性
優先於文件新舊。
```

```
R-C2  UI label 拼寫
TC 之 UI label 與狀態文字依 SR24 之拼寫與大小寫（例：AUTO、RECIRC、grayed、
A/C），不採 SR25 之 Auto／recirc／greyed／AC。

背景：SR25 對同一批 section 做過大小寫與拼寫調整；因 R-C1 定 SR24 為基線，
SR25 之拼寫不進 TC。pilot review 時若見 TC 使用 SR24 拼寫而與 SR25 不同，
不構成 defect。
```

```
R-C3  leaf 判準
leaf（驗證單位）集合 = Categorization == "Functional Requirement"，共 403 列。

禁止以 tc id 後綴形態（是否具 -NN）判定 leaf。該判準只得 369 列，會漏掉 34 列
「ID 為 parent 形態、但自身即為 Functional Requirement 且無子項」者
（例：037 row 66 SWE1-HVAC-011 Fan Speed Control、row 137 SWE1-HVAC-026
Rear Defrost Control、row 183 SWE1-HVAC-037 On/ State）。

此判準須以 recon 腳本之 assertion 機械強制（403 == Functional Requirement
計數），不得僅寫在文件裡。
```

```
R-C4  HMI Source ID 解析
HMI Source ID 儲存格取第一行為 spec section id。其後各行為 Polarion item id
（例 ..._7.3\n4803284\n4803285），共 92 列具此形態，不參與 section 解析，
保留為 audit 佐證欄位。

解析後之 section id 相異數必須為 129；不符即 fail-loud，不得靜默略過。
```

```
R-C5  SR25 新增內容之處置
SR25 outline 共 187 節，其中 58 節未被 037 引用；扣除章級容器標題、1.x
Assumptions 與影像頁後，屬實質需求而 037 未分析者為：
  18.2 / 18.3 / 18.4          （BCW1、BCW2，10.25" Comfort Widget）
  19.1 / 19.2 / 19.3          （W0、LCW1、LCW2，7" Home screen Comfort Widget）
  20.1 ~ 20.4.3（10 項）       （CRB1–CRB4.3，LATAM Alternative Rear Blower）
  21.1 ~ 21.5 + 21.3.1（6 項） （L3H1–L3H5，L3 HVAC management）

因 R-C1 定基線為 SR24，上列全部 out of scope，不產 TC、不入 coverage 分母、
不列 BLOCKED。僅以單一 note 型 anomaly 記錄其存在，供日後 037 升版時查考。

不得以「求完整」為由自行補成 RD 項目或 TC（§8.2、§8.4.2）。
```

---

## R-C5-1 —— 下放包 05 §2（分析層訂正自身錯誤，2026-08-14，即時生效）

置於 R-C5 之後（05 §6.1）。**訂正 R-C5，非取代**；R-C5 原文不改寫。

```
R-C5-1  R-C5 適用範圍之限縮（訂正 R-C5，非取代）

R-C5 列舉之 22 節中，經對 SR24 export 逐節查存，16 節同樣存在於 SR24 基線：
  18.2 / 18.3 / 18.4
  19.1 / 19.2 / 19.3
  20.1 / 20.1.1 / 20.1.2 / 20.1.3 / 20.2 / 20.3 / 20.4 / 20.4.1 / 20.4.2 / 20.4.3

R-C5 之推論鏈為「屬 SR25 → 因基線為 SR24 → out of scope」。對此 16 節，
第一個前提不成立，故結論不成立。此 16 節自即日起退出 R-C5 之適用範圍，
併入 A-CF08 之 in-baseline substantive 集合，處置待 D-C10。

R-C5 對其餘 6 節（21.1 / 21.2 / 21.3 / 21.3.1 / 21.4 / 21.5）之結論不變：
SR24 export 最大 outline 為 20.4.3，無第 21 章，該 6 節確為 SR24 所無。

在 D-C10 裁定前，該 16 節維持：不產 TC、不入 coverage 分母、不列 BLOCKED、
不補 RD 項目。退出 R-C5 只改變其「為何暫不處置」的理由，不改變其現況。
```

---

## R-C4-1 —— 下放包 03 §2（分析層自裁，2026-08-14，即時生效）

置於 R-C4 之後（R19-2）。**訂正 R-C4，不取代**；R-C4 之實質規則不變。

```
R-C4-1  R-C4 之量測母體補標（訂正 R-C4，不取代）

R-C4 原文「共 92 列具此形態」未標母體，違反 §5a「標明量測條件」。訂正：

  母體 = 全部資料列 498（含 95 列 Heading）→ 多行 citation 儲存格 92 列
  母體 = leaves 403（Functional Requirement）→ 多行 citation 儲存格 57 列

兩數皆經執行層獨立實測復現，不衝突。R-C4 之實質規則（取第一行、相異
section 數 assert == 129）不變。

凡條文載有計數者，一律同時載明母體；未載母體之計數視為未完成之陳述。
```

---

## R-C6 ~ R-C7 —— 下放包 02 補遺（Pei 裁定，2026-08-14）

```
R-C6  Test Group
workbook Test Group 欄一律填 "Comfort"。

依 §4.1.1：Layer 1 Test Group 等同 spec 文件標題之模組名；spec 標題為
"Comfort HMI Logic and Flow"，故模組名為 Comfort。客戶交付路徑中之
"Climate Control Interface" 為資料夾分類，非 spec 標題，不作為 Test Group
來源。

Test Set（Layer 2）不得重複 "Comfort" 前綴（§4.2）。
```

```
R-C7  tc_id scheme
tc_id 格式為 NR1L-ComfortHMI-{NNN}，NNN 為三位零填補序號，於同一
NR1L-ComfortHMI 群組內單調遞增。

序號由 generator 指派，LLM 不得自行產生 tc_id（§10.3）。
本 scheme 自本包起凍結，生成開始後不得變更。
```

---

## R-C8 ~ R-C10 —— 下放包 04 §1（Pei 裁定，2026-08-14）

**R-C9、R-C10 適用全 feature，非 Comfort 專屬**；其安置位置（是否另立 repo
層級 canon）於下次 canon re-sync 時處理（04 §4）。

```
R-C8  既有 feature 之 recon 重跑政策

不因共用腳本改版而重跑既有 feature 之 recon。

理由：recon.py 之修改對 Privacy 之 diff 經實測全為增益（新增 assertion 段、
outline map 段誠實回報無 Outline Number 欄、[RULED] tc_id、兩處措辭修正），
無任何數字更正，既有結論之事實基礎未變。重跑之唯一實效為覆蓋
DECISIONS.md，代價大於收益。

例外：若日後發現某腳本缺陷會改變既有 feature 之「數字」而非「呈現」
（如 A-CF05 之靜默漏計形態），該 feature 必須重跑，且重跑前先將現行
DECISIONS.md 另存為 DECISIONS.<date>.superseded.md 保全。

判準為「數字是否改變」，不是「差異是否看起來無害」。
```

```
R-C9  已簽 DECISIONS.md 之覆寫防護（機械強制）

recon.py 於寫入 DECISIONS.md 前，必須讀取既有檔之 Sign-off 區塊。
偵測到已簽署時：拒絕覆寫，改寫 DECISIONS.new.md，以非零碼離開，
訊息指名兩檔路徑。

簽署偵測之判準（機械可判，非人工閱讀）：
  Sign-off 區塊之 "Reviewed by:" 欄位值非空且不等於底線佔位字串。

本條為機械強制而非紀律：全檔重寫是 recon.py 之既有性質，任何人在任何時候
重跑既有 feature 都會觸發，不可能靠「記得不要重跑」防守（R19-3）。
R-C8 是政策，R-C9 是政策失守時的護欄；兩者不互相取代。

適用於所有 feature，非 Comfort 專屬。
```

```
R-C10  簽署標記必須被實際填寫

Phase 2 sign-off 完成時，DECISIONS.md 之 Sign-off 區塊必須填入
Reviewed by 與 Date；留白之範本佔位不構成簽署。

未填寫者，其簽署狀態於 repo 內不可考，依「A ruling not written to the repo
did not happen」視為未簽署。

recon.py 於 Phase 2 之後、Phase 4 之前的任何階段，若偵測到
DECISIONS.md 存在 [PROPOSED] 標記且 Sign-off 為空，須輸出警告
（非阻塞），指明該 feature 之簽署狀態不可考。
```

---

## R-C11 —— 下放包 06 §1（Pei 裁定，2026-08-14）

其推廣段（spec 素材一律留在 `spec-index/`）**適用全 feature**；安置位置於
下次 canon re-sync 時處理（06 §5）。

```
R-C11  spec 來源之單一性

Comfort 之 SR24 SYS1 export 只保留一份，位於
spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_
CR24879_(September_25_2023).xlsx。

features/comfort/inputs/ 下之同名副本刪除。feature.yaml 維持以
../../spec-index/… 全名相對路徑回指，不改為 inputs/。

理由：R-C1 之遵守目前靠「feature.yaml 寫全名指向唯一檔案」達成機械強制
（上繳 01 §2）。同一基線存在兩份副本時，該強制降級為「目前取對」——
兩份副本一旦分歧，無任何機制會報錯。

推廣：spec 素材一律留在 spec-index/，不複製進 feature 之 inputs/。
inputs/ 只放該 feature 專屬且不屬 spec-index 管轄者（037、036 範本、
CFTS 等引用文件）。
```

---

## R-C12 ~ R-C14 —— 下放包 07 §1（Pei 裁定，2026-08-14）

**R-C13、R-C14 適用全 feature**；安置位置待 canon re-sync（07 §7）。
R-C13 與 Privacy R22-2 同構，合併處置於下次 re-sync（條文明載）。

```
R-C12  適用性判讀之保守原則

scope_verdict 於其依據來源存在未解之內部矛盾時，一律記 undetermined，
不得記 in_scope。

理由（不對稱錯誤成本）：in_scope 為「擴大驗證範圍」之主張，須自足證據；
undetermined 為「尚未認定」，可由後續證據往任一方向收斂。矛盾未解時記
in_scope，等於以未經裁決之單方選擇擴大範圍。

據此，上繳 03 §3.1 之 10 節（20.1 ~ 20.4.3）verdict 自 in_scope 降為
undetermined，pending DR #8。降級不推翻其依據，亦不否定其結論可能為真。

TSV 之 basis 欄原有依據全部保留不刪，另加 pending_on 欄記其所待。
```

```
R-C13  零命中之處置

以字串檢索為手段之查找，零命中只能陳述索引層事實（該字串不出現於該文件），
不得升格為內容層結論（該文件不涵蓋該事項）。

零命中應觸發換路徑，不應觸發下結論。最少須再走一條不依賴同一字串之路徑
（語義相關詞全列舉、結構化欄位篩選、章節逐節閱讀）；三路交叉仍無所獲方得
記 undetermined，即便如此仍不得記 out_of_scope。

來源文件自身給出之名稱亦可能與被引文件用詞不一致（A-CF11：SR24 稱
Alternative Rear Blower，CFTS043 稱 Alternate Rear Blower，以前者檢索後者
得零命中）。引用關係中的名稱不是可信的檢索鍵。

與 Privacy R22-2 同構，合併處置於下次 canon re-sync。
```

```
R-C14  刪除前之同一性確認

任何以「他處已有同一份」為理由之刪除，須以內容雜湊確認同一性，不得以檔案
大小、檔名或修改時間代替。大小相同不蘊含內容相同，而刪除之正當性恰取決於
內容相同。若兩份曾分歧，刪除前之比對是唯一會發現它的時機。

先驗後刪，驗不過即不刪。
```

---

## R-C15 ~ R-C16 —— 下放包 09 §2／§3（Pei 裁定，2026-08-14）

**兩條適用全 feature**；安置位置待 canon re-sync（09 §7）。
R-C15 係回答上繳 04 §6.2 第 3 項所標之界線問題。

```
R-C15  scope_verdict 之證據判準

判準為「蘊含」，不是「直接」。

證據若為真即蘊含結論者，得記 in_scope，縱其形式為間接。證據為真仍不蘊含
結論者，記 undetermined，縱其形式為直接聲明。

R-C12 之觸發條件為「來源存在未解之內部矛盾」，不擴及「依據為間接」。
間接而蘊含者不降級；直接而不蘊含者本就不得升級。

適用於本輪四節：
- 16.1：037 於 ch16 產出 99 leaves。若 EMEA 不在交付範圍，該 99 leaves
  不可能存在。為真即蘊含，故 in_scope 成立。
- 18.2–18.4：037 引用 18.1 得三個 leaf；18.1 與 19.1 條文文字相同，
  被分析者為 10.25" 實例。執行層已證此結論於兩種解讀下皆成立 ——
  「於所有可讀解讀下一致」即為蘊含，故 in_scope 成立。
```

```
R-C16  引用之單向性，與未引用節之 in_scope 意義

一、037 之引用作為證據具單向性：
    有引用 → 該事項在 SWE.1 分析範圍內，得為 in_scope 之證據
    無引用 → 不構成任何方向之證據，不得推出 out_of_scope，亦不得推出
             in_scope
    A-CF01／R-C5 之錯誤即違反此單向性（「037 沒引用」被當成「SR24 沒有」）。

二、某節判 in_scope 而 037 未引用之者，其意義為：
    該節屬交付範圍，而 037 未對其產出需求 —— 即 in-scope 之覆蓋缺口。

    此類節一律列 RD-1，請上游 037 補分析。
    **不得由 TC 作者自行補成 RD 項目或直接產 TC**（§8.2、§8.4.2）。
    在 037 補分析並落版前，此類節不入 coverage 分母、不列 BLOCKED、
    不指派 tc_id。

    16.1、18.2、18.3、18.4 四節依此處置：RD-1 覆蓋缺口項，非 TC 工作項。
```

---

## R-C17 —— 下放包 10 §1（Pei 裁定，2026-08-14）

```
R-C17  Home Screen HMI L&F 之定位

Home Screen HMI Logic and Flow（R1 SR24 Post 2A, March 17 2023）於 Comfort
feature 為外部參照 spec，非本 feature 之驗證來源。

Comfort ch17／ch18 所擁有者，僅「Comfort widget 自身之內容與行為」。
Home Screen 之首頁管理行為（HSD1–HSD13、HSS、SW、BSP 各條 —— 新增／刪除／
重排頁面、widget 拖放、Shortcuts 編輯、品牌頁預設配置等）由 Home Screen 之
SWE 需求擁有，不得寫入 Comfort TC（§8.4.2）。

判定測試：該規則定義於 Comfort spec，或定義於 Home Screen spec？
定義於後者即 out of scope，縱使 Comfort spec 引用之。

若 Home Screen 於本專案無對應 SWE 需求，該情形為 coverage hole，於
reasoning 揭露並列 RD-1，不得靜默吸收進 Comfort TC。
```

---

## R-C18 —— 下放包 13 §1（Pei 裁定，2026-08-15）

**適用全 feature**；安置位置待 canon re-sync（13 §8）。

```
R-C18  導覽欄位不得用於判讀

凡經截斷、摘要或正規化之欄位（如 layer3_map.tsv 之 section_title 取前 60
字），其用途限於導覽、排序與人工檢索。

不得據以做落位、範圍、等價、適用性或分組之判斷。此類判斷一律讀全文。

理由：截斷之失敗形態是靜默的，且可能產生語意完整而錯誤之片段
（先例：6.3 之 `secondary` 截為 `second`，導致「次要下方螢幕」誤讀為
「後座」）。片段讀得通，不代表它是原文。

推論：凡以此類欄位為輸入之既有判斷，須回頭以全文複核。
```

---

## R-C19 —— 下放包 14 §3（Pei 裁定，2026-08-15）

**適用全 feature**；安置位置待 canon re-sync（14 §6）。
本條源於執行層於上繳 08 §1 自加之 Phase 4 約束，分析層**不駁回，升格為條文**
—— 其理由具一般性，不應只以 `framework.md` 內一句話之形式存在。

```
R-C19  裁定之表達形式一致性

凡分析層之裁定，其實質內容為「某差異屬 X 類而非 Y 類」者，Phase 4 之 TC
表達形式須與該分類一致，不得以不一致之形式將裁定於 TC 層推翻回去。

具體適用（ch11／ch12）：`opens popup` 既經裁定為輸出回饋而非進入路徑，
ch11 之 11.1／11.2 與 ch12 之 12.1／12.2 之差異一律以 **expected_result**
表達（是否出現 popup），**不得**寫成不同的 test_procedure 步驟或不同的
pre_conditions。

理由：分類裁定之效力止於文件，除非它同時約束 TC 的寫法。無任何機械檢查
會擋住「步驟寫得不一樣」，故須明文，且須在該裁定作成時一併寫下，
而非留待 pilot review 發現。

pilot review 時，違反本條者列為 defect（非 style-divergence）。
```

---

## R-C20 —— 下放包 17 §2（Pei 裁定，2026-08-15）

**適用全 feature**；安置位置待 canon re-sync（17 §6）。既有 feature 之
BASELINE 是否補齊屬 Pei 裁定，**另案，本包不自行擴及**（17 §2 末）。

```
R-C20  BASELINE 之涵蓋範圍以來源為準，不以目錄為準

features/<feature>/BASELINE.sha256 須涵蓋該 feature 賴以生成之全部來源檔，
不論其位於 inputs/、spec-index/ 或其他路徑。

判準為「此檔若變動或消失，該 feature 之產出是否失去依據」，
而非「此檔在不在 inputs/」。

理由：目錄型判準會在來源被搬移時靜默失效（R-C11 將 spec 移出 inputs/ 即為
一例），而 gitignore 之涵蓋範圍與 BASELINE 之涵蓋範圍各自獨立演變，
兩者之交集無人維護。

Comfort 之 BASELINE 為 8 檔：inputs/ 5 檔 ＋ spec-index/ 之 SR24
export .xlsx／.json 與 SR24 PDF。
```

---

## R-C21 ~ R-C22 —— 下放包 19 §1／§5（Pei 裁定，2026-08-15）

**兩條適用全 feature**；安置位置待 canon re-sync（19 §8）。

```
R-C21  跨 feature 發現之登記位置

於 A feature 之作業中發現 B feature 之缺陷者，登記於 A 之 ANOMALIES.md 與
A 之 DATA_REQUESTS.md，並於該列具名對象 feature。

不代 B feature 建檔、不改 B 之任何既有檔案。B 之處置由 B 自身之 workstream
決定。

理由：跨 feature 寫入使「誰在維護這個檔」失去單一答案；而登記之目的是讓
發現不遺失，該目的在發現者之帳上即已達成。
```

```
R-C22  不可量化 ≠ 不可觀察

ER 之判準為「可觀察、可判定」，非「可量化」。條文未給數值者，ER 以條文
自身命名之可觀察量表述，不得補具體量值（§8.4.1），亦不得因無法量化而
標 BLOCKED。

BLOCKED 保留給「該行為完全由他方執行，本 ECU 無任何可觀察端」之情形
（Privacy [BLOCKED-ECU] 前例）。「值不知道但變化看得見」不屬之。
```

---

## R-C23 ~ R-C24 —— 下放包 21 §3／§1.3（Pei 裁定，2026-08-15）

**R-C23 適用全 feature**；R-C24 之 marker 為 Comfort 專屬（profile §5），
其原則適用全 feature。安置位置待 canon re-sync（21 §6）。

```
R-C23  自評不得以工具未報為依據

§9 self-check 之每一項，其依據須獨立於 lint 之涵蓋範圍。
「lint 未報此項」不構成該項 PASS 之依據。

某項若無獨立依據可具名，標「未實測」，不標 PASS。

理由：rev1 之 §9 自評四項報 PASS 而實際為 FAIL，同時 lint 25/25 全綠 ——
兩者同時錯且錯在同一處，因為自評複述了 lint 之涵蓋範圍。工具與自評若
共用同一涵蓋範圍，其中一者即不提供任何額外保障。
```

```
R-C24  外部 spec 全權委派之 leaf —— BLOCKED row ＋ [BLOCKED-SPEC]

某 leaf 之全部內容為對外部 spec 之委派或等效性宣告，扣除該委派後於本
feature 範圍內無任何可獨立驗證之餘留者：**產出 BLOCKED row，不省略、
不併入 sibling leaf、不以複製 sibling 之 procedure 充數。**

marker：`[BLOCKED-SPEC]`，置於 Remarks 之開頭 token。

BLOCKED row 之內容：
- `test_procedure` / `expected_result`：空
- `specification_reference`：該 leaf 自身之 outline，照常填
- Remarks：`[BLOCKED-SPEC]` ＋ 擁有該內容之文件名 ＋ 一句說明何以無餘留
  （外部可見，不得出現內部 ruling id 或 A-CF 編號，AMFM R10-4）
- 其餘欄位依 profile 常規

**與 Privacy `[BLOCKED-ECU]` 之區別須寫入 profile §5**：前者為「行為由
另一 ECU 執行，本 ECU 無可觀察端」；本條為「行為可觀察，但其規範內容
由另一份 spec 擁有」。兩者外觀相同（皆無 procedure），成因不同，
不得互相類推。

**lint 之豁免必須是具名回報項，不得為條件式中之靜默跳過**（前例：
上繳 06 §2.1 之 `and n != "Comfort Widget"`）。`proc-min-steps`、
`proc-er-1to1` 對 BLOCKED row 之豁免，須以獨立回報行輸出，形如：
`- PASS — rows exempted as BLOCKED-SPEC: ['NR1L-ComfortHMI-010', ...]`
使豁免在每次 lint 輸出中可見。
```

---

## R-C25 ~ R-C26 —— 下放包 22 §1.1／§2（Pei 裁定，2026-08-15）

**兩條適用全 feature**；安置位置待 canon re-sync（22 §6）。

> **旁註（24 §1，2026-08-15）**：本條之兩問即 **R-C28** 之第二、三問。
> R-C28 於其前補「第一問：出處」——「該事實在其標註來源節之 full_text
> 有無明文對應」。**本條原文不改寫**；兩者並存，R-C28 為完整判準。

```
R-C25  §8.5 例外賦予資格，§4.5 決定落點

某狀態為 spec 定義之 trigger condition 者，依 §8.5 例外**取得**進入
pre_conditions 之資格。該資格不等於落點 —— §4.5 仍要求同一事實只出現於
一個欄位。

當該 TC 自身之步驟無論如何都必須建立該狀態時（§7 FF：include setup,
don't assume hidden state），落點為 test_procedure，pre_conditions 不再
重複陳述。

判定順序：先問「這是不是 spec trigger」（§8.5，資格），
再問「誰建立它」（§7／§4.5，落點）。兩問答案可以是「是」與「procedure」，
兩者不衝突。
```

```
R-C26  觸發 lint 豁免之標記須經白名單

凡標記之出現會使某列免受一個或多個 lint gate 檢查者，其得使用之 tc_id
須列於 profile 之具名白名單。

gate 檢查：列帶該標記而 tc_id 不在白名單 → FAIL。
白名單之增列須經裁定（profile §5「新增 marker 須先裁決」之延伸：
不只新增 marker 須裁，既有 marker 之新增使用者亦須裁）。

理由：豁免若可自我授予，其條件即不成立。此與「豁免須為具名回報行、
不得為條件式中之靜默跳過」（R-C24）互補 —— 後者使豁免可見，
本條使豁免不可自取。
```

---

## R-C27 —— 下放包 23 §3（Pei 裁定，2026-08-15）

**適用全 feature**；安置位置待 canon re-sync（23 §6）。

```
R-C27  受可見性限制之欄位，其資訊依可見性排序

某欄位之實際可見範圍小於其內容者，該欄位之關鍵資訊須置於可見範圍內。

適用於 Remarks 之 marker 型內容：marker 之後**緊接**擁有者／原因之最短
可辨識形式，說明性文字置後。

判準為「截斷於首行時，讀者是否仍取得該欄位存在之目的所要傳達者」。
```

---

## R-C28 —— 下放包 24 §1（Pei 裁定，2026-08-15）

**適用全 feature**；安置位置待 canon re-sync（24 §5）。
本條源於執行層上繳 15 §5.2 指出之 R-C25 缺口：**可用推論回答的資格問題，
等於沒有資格問題。**

```
R-C28  pre_conditions 之三問，出處在最前

pre_conditions 之每一行，依序回答三問，任一問失敗即不得寫入該欄：

  一、出處 —— 該事實在其標註來源節之 full_text 有無明文對應？
       無 → 不是落點問題，是 §7 FF（假定隱藏狀態）或 §8.4.1（造值）。
       停在此，不進入第二問。
  二、資格 —— 該狀態是否為 spec 定義之 trigger condition（§8.5 例外）？
  三、落點 —— 誰建立它？TC 自身步驟無論如何都須建立者，落點為
       test_procedure（§7 FF ＋ §4.5），pre_conditions 不再重複陳述。

R-C25 之兩問即本條之第二、三問；本條補第一問並置於最前。
R-C25 原文不改寫，於其旁註明此關係。

第一問之回答須具名條文之相關句，不得以「合理」「顯然」「恆常如此」代之。
```

---

本條源於執行層上繳 18 §3.5 第 3 問：3.3 之 PC 需 REAR DEF 存在，
而該事實之明文在 3.4。**至今所有 PC 之出處節與所屬節同一，係語料使然，
非規則使然。**

```
R-C29  pre_conditions 之節次標註指向事實之出處，非 TC 之所屬節

PC 每一行括號內之節次，係該事實之**明文出處**，不是該 TC 所屬之節。
兩者不同時，以出處為準。

連帶三項義務：
一、該出處節須一併列入 specification_reference —— §10.7 明定該欄涵蓋
    「TC 直接驗證或**賴以作為 setup**」之節，跨節取據之 PC 即屬後者。
二、reasoning 須說明何以跨節取據，並確認**未擴張驗證範圍**（§8.2.1）：
    引用 3.4 之裝備事實，不等於驗證 3.4 之行為。
三、coverage 分母以 leaf（req_id）計，不以 specification_reference 計；
    跨節引用不改變任何 leaf 之歸屬。

至今所有 PC 之出處節與所屬節同一，係語料使然，非規則使然。
本條使該巧合不再被誤認為規則。
```

---

本條源於執行層上繳 17 §3.5：A-CF02 原記「交付樹不可達（已搜尋）」，
而該次 `find` 之起點在 `TC_Generator/` 之內，交付樹在 repo 之外。
**零命中被當成「不存在」，而它其實只是「不在我搜的地方」。**

```
R-C30  以搜尋為依據之陳述，須載明其涵蓋範圍

凡結論之依據為「搜尋未命中」者，該陳述須同時載明搜尋之**根目錄**與
**pattern**；未載明者，其陰性結果不得作為任何結論之依據。

此為 R-C13 之補充：R-C13 要求零命中須換路徑，本條要求**已走過的路徑
留下痕跡**。無痕跡者，第二人無從判斷該換哪條路。

適用於 anomaly、上繳包、下放包之一切陰性陳述。
```

---

## 執行層回報（2026-08-14，Phase 0 → Phase 1）

以下為執行層對上列條文之落實紀錄與實測值，**非條文本身**。

### R-C1 —— 落實於三處，非僅文件

1. `feature.yaml` `spec_reference_template` 寫死 SR24 全名 stem。
2. `paths.sys1_export` / `paths.spec_pdf` 指名 SR24 全名 —— **不使用萬用字元**。
   `spec-index/cache/` 同時存有 SR25 CR29359，一個 `SYS1_HMI_Comfort_*`
   會同時命中兩份基線並讓 `resolve_glob()` 以「ambiguous」中止；寫全名是
   為了讓「取到 SR25」在結構上不可能發生，而非靠命名運氣。
3. `recon.py` assertion `spec_reference_stem`：037 全 403 leaves 之 citation
   stem 必須是且僅是 SR24 全名。實測 **PASS** —— 相異 stem 數 = 1。

### R-C3 —— 機械強制已就位（條文明文要求）

`recon.py` assertion `functional_requirement_count`，期望值置於
`feature.yaml` `recon_assertions`（Comfort 之裁決常數，非 pipeline 常數）。

- 實測：Categorization 分布 `{'Functional Requirement': 403, 'Heading': 95}`
  → leaf 計數 **403**，**PASS**。
- 同時輸出被禁判準之實測值：`-NN` 後綴形態只得 **369**，漏 **34** 列
  （`SWE1-HVAC-011`、`-026`、`-027`、`-037`、`-039`、`-041` … 全列於
  `data/recon.json` `parent_shape_functional`）。條文舉之三例
  （011 / 026 / 037）全在該 34 列內。差額 34/403 = 8.4%，與 A-CF03 相符。
- 反向驗證：將期望值改為 402 重跑，腳本輸出 `FAIL`、**不寫 DECISIONS.md**、
  以非零碼離開。assertion 為真正之閘，非裝飾。

### R-C4 —— 129 已查得，且逐節對 SR24 export 查核

- 解析規則：取儲存格第一行，其後各行為 Polarion item id，保留不解析。
- 實測相異 section 數 **129**，**PASS**。
- 具多行形態之 citation 儲存格：**57 列**（限 Functional Requirement 範圍內計）。
  條文所載之 92 列係對全部 498 資料列（含 Heading）計；兩數不衝突，統計母體不同。
- outline map 對 SR24 export（`Basic Report`，180 個 outline number，無重複）
  建立；129 節**逐一查得，miss = 0**。map 落於
  `data/spec_id_to_outline.tsv`（403 列 + 表頭，追蹤入版控）。
- fail-loud 已實作於兩處：export 缺 outline 欄或 `sys1_export` 為 null 時，
  「無基線可查」本身即記為 FAIL；查得不到之節列入 `outline_misses`。
  **不曾、也不會以「SR25 有」代替**——`sys1_export` 只指向 SR24。

### R-C6 / R-C7 —— 已寫入 `feature.yaml`

`test_group: "Comfort"`；`write_back.tc_id_format: "NR1L-ComfortHMI-{n:03d}"`。
序號由 generator 指派之約束於 Phase 4 落實，此處僅凍結格式。

---

## 執行層回報（2026-08-14，下放包 03／04）

### R-C4-1 —— 兩個母體皆已實測復現

| 母體 | 多行 citation 儲存格 |
|---|---|
| 全部資料列 498（含 95 Heading） | **92** |
| leaves 403（Functional Requirement） | **57** |

`RECON.md` 之 `citation cells with extra lines…: 57` 一行係 403 母體。
兩數皆為本機直接量測，非引用。

### R-C9 —— 已實作於 writer，含反向驗證三項

實作位置 `scripts/recon.py`：`read_signoff()` 讀既有檔之 Sign-off 區塊，
`write_decisions()` 為唯一寫入點 —— 護欄放在 writer 而非呼叫端，是因為條文
指出的失效形態是「任何人在任何時候重跑」，任何需要呼叫端記得的設計都防不住。

偵測判準除條文所定之 `Reviewed by:` 非佔位外，另接受 SXM 形態之
`- Amendment (…): … directive「…」` 條目（R-C10 註「兩者擇一即可」）。
佔位字串以 `^[\s_]*$` 判定，因 Projection 用的是 `____________` 而非 `____`。

**反向驗證（人工填 `Reviewed by: TEST  Date: 2026-08-14` 重跑）**：

| # | 應然 | 實測 | 結果 |
|---|---|---|---|
| 1 | 拒絕覆寫 | `DECISIONS.md` sha256 前後皆 `e6283e90a266222c` | **PASS** |
| 2 | 寫出 `DECISIONS.new.md` | 已寫出，55 行 | **PASS** |
| 3 | 非零離開 | `exit=1` | **PASS** |
| 4（自加） | 已簽時不誤發 R-C10 警告 | 該警告 0 次 | **PASS** |

訊息實測指名兩檔絕對路徑。**驗畢已還原**：測試填值復原，
`diff` 與測試前逐位元組相同，`DECISIONS.new.md` 已刪除，重跑回到正常寫入路徑。

第一次量測曾把第 3 項報成 FAIL —— 係 zsh `pipestatus` 索引自 1 而腳本寫
`${PIPESTATUS[0]}`，取到空字串，屬**量測腳本之缺陷，非實作失敗**。改以直接
捕捉 `$?` 重測得 `exit=1`。記此一筆，因為它與 §5a 所戒之形態相同：
量測工具無聲取到空值，而空值在比較式裡看起來像一個結論。

### R-C10 —— 已實作（非阻塞），且對 04 §2 之前提有一處實測訂正

警告於偵測到「`[PROPOSED]` 存在且 Sign-off 為空」時輸出，不影響離開碼。
Comfort 本身現即觸發（尚未簽署，屬正確狀態）。

**訂正 04 §2 第 2 點之前提**：該點稱「全部 feature 之該區塊都是空白範本，
偵測器永遠回報未簽署，護欄形同虛設」。以 `read_signoff()` **唯讀**掃描
（未重跑任何 recon，R-C8）實測：

| feature | signed | Reviewed by | Date | Amendment | `[PROPOSED]` |
|---|---|---|---|---|---|
| home | ✗ | — | — | 0 | 有 |
| **amfm** | **✓** | PeiPYHsu | 2026-08-09 | 0 | 有 |
| **sxm** | **✓** | PeiPYHsu | 2026-08-10 | 11 | 有 |
| projection | ✗ | — | — | 0 | 有 |
| media | — | （無 `DECISIONS.md`） | | | |
| privacy | ✗ | — | — | 0 | 有 |
| comfort | ✗ | — | — | 0 | 有 |

**六個有 `DECISIONS.md` 之 feature 中，兩個已簽。** R-C9 之護欄對 amfm 與
sxm **今日即為有效**，非「形同虛設」。04 §2 之裁決結論（加 R-C10）不受影響
——R-C10 仍是必要的，因為另外四個確實是空白範本 —— 但其理由中「一次也不會
觸發」一句不成立。

此訂正同時使 R-C8 之份量上升：amfm／sxm 若被重跑，覆蓋的是**有 repo 證據
的簽署**，不只是空白範本。

`media` 無 `DECISIONS.md` —— 既非已簽亦非空白範本，屬 A-CF09 之外的第三種
狀態，一併記於該條。

---

## 執行層回報（2026-08-14，下放包 05／06）

### R-C5-1 —— 已生效，A-CF08 已更新

該 16 節退出 R-C5 之適用範圍，併入 A-CF08 之 in-baseline substantive 集合。
**現況未變**：仍不產 TC、不入分母、不列 BLOCKED、不補 RD，待 D-C10。
改變的是「為何暫不處置」的理由 —— 由「屬 SR25 故 out of scope」改為
「在基線內，處置待裁」。

### R-C11 —— 已執行刪除，前提逐項確認在先

刪除為不可逆，故先驗後刪，逐項留痕：

| 前提 | 實測 | 結果 |
|---|---|---|
| `spec-index/cache/` 該份仍在 | 存在 | ✅ |
| 大小為 70,040 bytes | 70,040 | ✅ |
| （自加）與待刪副本內容相同 | 兩者 SHA256 皆 `6982d37db81b36e4…` | ✅ |

第三項為執行層自加。條文只要求確認 `spec-index/` 那份在且大小相符，但
「大小相同」不蘊含「內容相同」—— 而刪除的正當性取決於後者。兩份 SHA256
逐位元組相同，故刪除不損失任何內容。若兩者曾分歧，本次比對就是唯一會
發現它的時機（也正是 R-C11 立條之理由：分歧無任何機制會報錯）。

刪後複測：`spec-index/` 該份仍在且仍為 70,040 bytes；`recon.py` 四個
assertion 全 PASS（129/129 outline 查得，miss=0），`feature.yaml` 之
`../../spec-index/…` 路徑照常解析，未改為 `inputs/`。

登記 **A-CF10**，記錄該副本曾存在之事實。

### 06 §3 適用性判讀 —— 10 in_scope／7 undetermined／0 out_of_scope

`data/sr24_substantive_applicability.tsv`，17 節與 A-CF08 之 substantive
集合對稱差為空。詳見 `docs/upstream/03_applicability.md`。

**一處差點造成誤判，記於此**：SR24 §20 標題作 "LATAM **Alternative** Rear
Blower"，CFTS043 全篇作 "Altern**ate** Rear Blower"，且從不使用
"Alternative"、亦不以 LATAM 標示該功能。以客戶自己的用詞搜尋 CFTS043
得 **0 命中**，若就此收手，10 節會被判成 `out_of_scope`——
一個有完整依據外觀、方向完全相反的結論。詳 **A-CF11**。

這是下放包 06 §3「讀不到即 undetermined，不得以讀不到判 out_of_scope」所
防的形態，但實際發生的版本更隱蔽：**不是讀不到，是用錯字串去讀而讀不到**。

---

## 執行層回報（2026-08-14，下放包 07／08）

### R-C12 —— 10 節已降級，依據全數保留

`data/sr24_substantive_applicability.tsv` 加 `pending_on` 欄。
20.1 ~ 20.4.3 十節 `in_scope` → `undetermined`，`pending_on` =
「DR #8 — CFTS043 4803259 NOTE vs its own Radio attribute (A-CF12)」。

`basis` 欄**原有依據一字未刪**（機械檢查：10 列全部仍含 `Scope=Yes` 字樣），
僅前綴 `[R-C12: downgraded from in_scope 2026-08-14; evidence below retained
in full, not retracted]`，並依 07 §3 追加層級訂正段。

### R-C13 —— A-CF11 已升格，且本輪再次派上用場

A-CF11 已註記升格為 R-C13。**本輪 DR #6／#7 判讀就是 R-C13 的直接應用**：
Market Configuration Table 對 `R1L-R` 與任何螢幕尺寸皆 **0 命中**，若依
零命中下結論，7 節會全判 `out_of_scope`。改走三路：

| 路徑 | 作法 | 結果 |
|---|---|---|
| 一 | 結構化欄位篩選（radio variant / 地理分組欄之相異值） | 得知該表之 variant 軸是市場別（ROW/ECE/US-CAN…），非機型別，**不承載 R1L-R** |
| 二 | 全 8 工作表 token 掃描（R1L-R／螢幕尺寸／widget／EMEA／LATAM） | `R1L-R` 0、螢幕尺寸 0、`EMEA` 158、`LATAM` 26 |
| 三 | **037 自身之引用結構** | ch16 引 18/19（99 leaves）、ch18 引 1/4（3 leaves）、ch19 引 0/3 |

第三路才是決定性的，而它不依賴任何字串檢索。

### R-C14 —— 本輪對 Market Configuration Table 之取用即依此條

08 §1 已警示四個 release 之該檔全標 `v1.6` 而內容互異
（25PI3.5 `ae4cf0b9…`／25PI4.5 `9efae74f…`／26PI1.5 `2e66a6d9…`／
26PI2.5 `7e865d55…`）。取用前實測：

| 項 | 值 |
|---|---|
| bytes | 279,779（與 08 §1 相符） |
| SHA256 | `ae4cf0b929b033ac3baabf9d2e6e7497da5539d3f774be30d52d636a67816cfc` |
| 對 `ae4cf0b9…` | **PASS** |

Gate 通過方進入判讀。R-C14 原文所治為「刪除前」，此處是「取用前」——
同一命題的另一面：**版本標籤不能識別內容，雜湊才能**。

---

## 執行層回報（2026-08-15，下放包 13）

### R-C18 —— 已貼入，並已建立其所需之基礎設施

`data/section_fulltext.tsv`（129 列，`full_text` 不截斷）為「一律讀全文」
之來源。四個 assertion 全 PASS。

**規模佐證**：`full_text` 長度最短 27、**中位 245**、最長 1232，對照
`layer3_map.section_title` 之 60 字上限 —— 中位即截斷值之 4 倍，最長者 20 倍。
R-C18 所治之資訊遺失，在本 feature 是多數列之常態，非少數例外。

**R-C18 末句之盤點**（「凡以此類欄位為輸入之既有判斷，須回頭以全文複核」）：

| 既有判斷 | 輸入 | 受影響？ |
|---|---|---|
| A-CF08 之 51 節四值分類 | 直接讀 export 全文（`bare_text()` 無長度限制） | 否 |
| 17 節適用性判讀 | CFTS043 `.doc` 全文 ＋ tree view 結構化欄位 | 否 |
| 6.3 落位 | 上繳 06 已讀全文複核 | 已複核 |
| ch11／ch12 合併 | 13 §3 已自承係讀截斷標題 | **是** —— 全文已供（上繳 07 §4） |
| **Part N 之 15 組切分** | 11 §2／12 §2 依 `layer3_map.tsv` | **是（部分），唯一未複核者** |

末項之複核需逐節讀全文再對照分組理由，屬 Tier 2 語意判斷；材料已齊備
（`section_fulltext.tsv`），是否複核待分析層明示。

### Test Set #15 更名（13 §2）—— 三處同步，驗收條件達成

`Comfort Widget` → `Home Screen Widget`。Layer 3 不變，leaves 仍 21。
`verify_partn.py` 第四項回報由 `measured ['Comfort Widget']` 轉為
`measured []`，即 13 §2 所定之驗收條件。

接受該裁定。我原主張「spec 稱其為 the Comfort widget」，但 13 §2 指出
Bluetooth 之範例中 spec 同樣稱該功能為 "Bluetooth pairing" —— 若我的理由
成立，§4.2 之範例本身就不成立。

**更值得記者**：13 §2 指出，若原先那行 `and n != "Comfort Widget"` 留在
條件式裡，此次更名永遠不會發生 —— 檢查會 PASS，而問題會被 PASS 蓋住。
該理由已寫入 `verify_partn.py` 該項檢查之註解。
