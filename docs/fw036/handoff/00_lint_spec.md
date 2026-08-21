# 下放包 00 附件：lint 檢查規格（正則與豁免表，實測校準版）

欄位鍵：test_set / test_item / pre / input / proc / er / spec /
author（header 關鍵字：Test Set、Test Item、Pre-Conditions、
Input Test Data、Test procedure、Expected Result、
Specification Reference、Test Case Author，取 startswith 匹配）。
「行」= 欄內以 \n 切分；「編號行」= 匹配 `^\s*\d+[.)]`。

## 檢查定義（Python re）

- **A 禁用動詞**（proc）：
  `(^\s*\d+[.)]\s*(Observe|Verify|See if|Watch|Monitor|Inspect)\b)|\b(observe whether|check whether|confirm whether|see if)\b`
  旗標 re.I|re.M
- **B ER 情態詞**（er）：`\b(shall|should|will)\b`；
  豁免：整段位於成對引號（" " 或 “ ”）內者
- **C hedge**（test_item）：`\b(properly|successfully|within reasonable time)\b` re.I
- **D PC 違規**（pre）：`\b(HU|system|unit) is powered on\b` re.I，
  或編號行行首動詞 `(Insert|Connect|Press|Open|Enable|Disable|Launch|Select|Tap|Trigger|Perform|Set)\b`
- **E 對齊**：proc 編號行數 ≠ er 編號行數（兩者皆 >0 時）
- **F 方括號**（proc）：`\[[A-Za-z][^\]]{0,30}\]`
- **G Test Set**：strip 後空字串（詞彙表外值檢查待 framework
  詞彙表接入後啟用，本版僅報空值）
- **H ER 模糊**（er）：`\b(as expected|works? normally|normal(ly)? operation)\b` re.I
- **I 括號下半**（test_item）：無任何 strip 後整行匹配 `^\(.+\)$`
  之行，且結尾不匹配 `\([^)]{3,}\)\s*$` → 違規。
  另：同 Requirement ID 下多列之括號行內容逐字相同 → sibling 違規
- **J 行首大寫**（test_item 首行 + 三欄編號行）：首個含字母 token
  之首字母為小寫 → 違規。豁免 token：
  (a) 白名單 {adb, tmpfs, iPod, iOS, iPhone, dd, cat, mount,
      btsnoop, hciconfig, hcitool, logcat, sdptool}
  (b) camelCase `^[a-z][a-zA-Z0-9_]*[A-Z]`
  (c) 點呼叫 `^[a-z][a-z0-9_]*\.[a-zA-Z(]`
  (d) `$` 或引號（" ' “）開頭
- **K CJK**（六欄）：`[\u4e00-\u9fff]`。本版全報告；
  分級（雙語制/UI 標籤/工作備註）待 R-5 裁定後配置
- **L 長度**（test_item 上半 = 去除 `^\(.+\)$` 行後）：
  token 數 `[A-Za-z0-9$_.'"-]+` 計，>50 報告（閾值 CLI 可調，
  待 R-3 定案）
- **M 空欄三態**（pre/proc/er/spec）：strip 後空且非 `NA` 且
  無 `PENDING:` 前綴 → 報告
- **N 尾句號**（pre/input/proc/er 每行）：行尾 `[.。]$`；
  豁免 `$` 指令行與縮排續行

## 校準基準（Media 0625，勿改）

A=0 B=0 C=1 D=0 E=1 F=0 G=0 H=0 I=2 K=0 L=0；J/M/N 未校準。

## 其餘 7 本路徑（皆於 10_Reviewing/00_TestCase/ 下，唯讀）

Bluetooth/…SWQT_BT_20260729.xlsx
DealerMode/…SWQT_CFTS012_DealerMode_20260417(done).xlsx
HandsFreePhone/…SWQT_CFTS026_HandsFreePhone_20260316(Refine).xlsx
Projection/CP:AA:iPod/…SWQT_Projection_20260623.xlsx
ASW-R2/Core HMI/HomeHMI/…SWQT_Home_20260809.xlsx
ASW-R2/AM:FM/…SWQT_AMFM_20260810.xlsx
ASW-R2/Power Management/…SWQT_PowerManagement_20260820.xlsx
（檔名前綴同 Media；以 glob `FM-WI-FSM-036*SWQT_{tag}*.xlsx` 取檔，
命中非一檔即中止報錯，不得猜檔）
