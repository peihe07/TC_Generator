#!/usr/bin/env python3
"""T24 —— priority 判定草案（R-VC11）。

**草案，非交付件。** 逐 leaf 以 IN §10.2 之 rubric 預判 P0–P3，
再套 R-VC11(b) 之上游邊界，並標出 R-VC11(c) 之分歧。

判定原則（framework.md「Priority follows the verification target」）：
    優先級由「這條 TC 失敗時，什麼漏檢了」決定，
    不由底層功能有多重要決定。

rubric（R-VC11(a) 所引之 IN §10.2）：
    P0  安全／開機／連線／音訊輸出／eCall／車輛關鍵 CAN／資料遺失風險
    P1  主要使用者功能或關鍵操作邏輯
    P2  次要／支援功能
    P3  次要 UI、低影響客製、罕用情境、外觀細節

邊界（R-VC11(b)）：
    037 High   -> 不得低於 P1
    037 Low    -> 不得高於 P3
    037 Medium -> 不設邊界（88 筆語意跨度過大，不具區辨力）

輸出：`data/priority_draft.tsv` + 主控台摘要。只讀 037，不寫任何 TC 欄位。
"""
import re
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

# 本地預判。每筆附一句依據 —— 判準是「失敗時漏檢什麼」。
LOCAL = {
 # 章 2 —— Vehicle Category 頁籤結構
 "SWE1-HMI-VC-001-01": ("P1", "主要導覽結構：頁籤集不成立則整個 feature 不可達"),
 "SWE1-HMI-VC-001-02": ("P2", "首次進入之預設頁籤，錯了仍可手動切換"),
 "SWE1-HMI-VC-001-03": ("P2", "回復上次頁籤，屬便利性"),
 "SWE1-HMI-VC-002":    ("P2", "Specialty 頁籤之位置，錯位不阻斷取用"),
 "SWE1-HMI-VC-003":    ("P2", "頁籤排序"),
 "SWE1-HMI-VC-004":    ("P3", "字面標籤"),
 "SWE1-HMI-VC-005":    ("P3", "字面標籤"),
 "SWE1-HMI-VC-006":    ("P3", "可列入之 Specialty 列舉，開放式"),
 "SWE1-HMI-VC-007-01": ("P2", "採用對照表為權威來源"),
 "SWE1-HMI-VC-007-02": ("P3", "對照表單列：命名與位置"),
 "SWE1-HMI-VC-007-03": ("P3", "對照表單列"),
 "SWE1-HMI-VC-007-04": ("P3", "對照表單列"),
 "SWE1-HMI-VC-007-05": ("P3", "對照表單列"),
 "SWE1-HMI-VC-008":    ("P2", "失敗＝少一個頁籤，非攝影機功能失效"),
 "SWE1-HMI-VC-009":    ("P3", "去重複，重複只是冗餘"),
 "SWE1-HMI-VC-010":    ("P2", "依配備過濾，未過濾則出現不可用項"),
 "SWE1-HMI-VC-011":    ("P3", "Dashboard 內容排序"),
 "SWE1-HMI-VC-012-01": ("P3", "橫向版面配置"),
 "SWE1-HMI-VC-012-02": ("P3", "橫向版面配置"),
 "SWE1-HMI-VC-012-03": ("P3", "橫向版面配置"),
 "SWE1-HMI-VC-013-01": ("P3", "直向版面配置"),
 "SWE1-HMI-VC-013-02": ("P3", "直向版面配置"),
 "SWE1-HMI-VC-013-03": ("P3", "直向版面配置"),
 "SWE1-HMI-VC-013-04": ("P3", "直向版面之尺寸與溢位"),
 # 章 3 —— Controls
 "SWE1-HMI-VC-014":    ("P2", "Controls 可列入項目之清單"),
 "SWE1-HMI-VC-015":    ("P3", "攝影機項目之分組"),
 "SWE1-HMI-VC-016":    ("P3", "條件式項目出現規則，罕用情境"),
 "SWE1-HMI-VC-017":    ("P1", "狀態回報：失敗則使用者依錯誤狀態操作車輛"),
 "SWE1-HMI-VC-018":    ("P2", "捷徑，非唯一路徑"),
 "SWE1-HMI-VC-019-01": ("P2", "無狀態按鍵之語意"),
 "SWE1-HMI-VC-019-02": ("P3", "按壓時不高亮，外觀細節"),
 "SWE1-HMI-VC-020":    ("P1", "HMI 狀態須跟隨實際系統狀態，否則顯示與車態相悖"),
 "SWE1-HMI-VC-021":    ("P1", "置物箱鎖之 Privacy Lock 彈窗，屬存取控制入口"),
 "SWE1-HMI-VC-022":    ("P3", "雙螢幕之內容去重"),
 "SWE1-HMI-VC-023":    ("P2", "電控玻璃不跨鑰匙循環記憶"),
 "SWE1-HMI-VC-024":    ("P2", "車頂開啟時標為不可用並灰化"),
 "SWE1-HMI-VC-025-01": ("P2", "採用 Controls Button Table 為權威來源"),
 "SWE1-HMI-VC-025-02": ("P2", "按鍵狀態語意對照"),
 "SWE1-HMI-VC-025-03": ("P2", "按鍵狀態語意對照"),
 "SWE1-HMI-VC-025-04": ("P2", "按鍵狀態語意對照"),
 "SWE1-HMI-VC-025-05": ("P2", "按鍵狀態語意對照"),
 # 章 4–7 —— Glove Box PIN（存取控制）
 "SWE1-HMI-VC-026-01": ("P1", "啟用流程之入口彈窗"),
 "SWE1-HMI-VC-026-02": ("P1", "PIN 輸入彈窗，存取控制主流程"),
 "SWE1-HMI-VC-026-03": ("P1", "兩次輸入確認，PIN 設定之核心邏輯"),
 "SWE1-HMI-VC-027":    ("P2", "啟用成功之確認彈窗，屬回饋"),
 "SWE1-HMI-VC-028-01": ("P1", "錯誤 PIN 之警示，存取控制回饋"),
 "SWE1-HMI-VC-028-02": ("P1", "啟用流程不限制錯誤次數 —— 存取控制之明文性質"),
 "SWE1-HMI-VC-029":    ("P1", "正確 PIN 後啟用，主流程終點"),
 "SWE1-HMI-VC-030":    ("P1", "停用需同一 PIN，存取控制主流程"),
 "SWE1-HMI-VC-031":    ("P2", "停用成功之確認彈窗，屬回饋"),
 "SWE1-HMI-VC-032":    ("P3", "按 OK 關閉彈窗並返回，導覽細節"),
 "SWE1-HMI-VC-033-01": ("P1", "三次錯誤鎖定 30 分鐘 —— 防暴力嘗試之核心規則"),
 "SWE1-HMI-VC-033-02": ("P2", "位數不足之驗證彈窗"),
 # 章 11 —— Settings 樣板與通則
 "SWE1-HMI-VC-034-01": ("P2", "不適用之設定隱藏"),
 "SWE1-HMI-VC-034-02": ("P2", "key-off 不可用者灰化而非隱藏"),
 "SWE1-HMI-VC-035-01": ("P1", "回復預設值確實生效"),
 "SWE1-HMI-VC-035-02": ("P2", "回復完成之確認彈窗"),
 "SWE1-HMI-VC-035-03": ("P0", "**資料遺失風險**：Cancel 若未攔住，使用者設定被靜默清空"),
 "SWE1-HMI-VC-036-01": ("P0", "**資料遺失風險**：清除個人資料之執行"),
 "SWE1-HMI-VC-036-02": ("P0", "**資料遺失風險**：Cancel 若未攔住，個人資料被靜默清除"),
 "SWE1-HMI-VC-037-01": ("P1", "懸吊模式互斥 —— 車輛動態設定之關鍵邏輯"),
 "SWE1-HMI-VC-037-02": ("P1", "啟用一者即停用其餘，同上"),
 "SWE1-HMI-VC-038-01": ("P2", "語言變更之進度彈窗"),
 "SWE1-HMI-VC-038-02": ("P3", "彈窗以新語言呈現"),
 "SWE1-HMI-VC-038-03": ("P2", "彈窗持續至完成或使用者關閉"),
 "SWE1-HMI-VC-038-04": ("P3", "關閉後返回語言設定頁"),
 "SWE1-HMI-VC-038-05": ("P3", "更新期間其餘語言灰化"),
 "SWE1-HMI-VC-039":    ("P3", "中文之特定彈窗文字"),
 "SWE1-HMI-VC-040":    ("P2", "左側選單列標題取自 HMI Settings List"),
 "SWE1-HMI-VC-041":    ("P2", "無選單列時之第一層呈現"),
 "SWE1-HMI-VC-042-01": ("P3", "文字截斷時改以箭號下推"),
 "SWE1-HMI-VC-042-02": ("P3", "下一層之單選列呈現"),
 "SWE1-HMI-VC-043":    ("P3", "父層括號顯示目前選項"),
 # 章 12 —— Settings
 "SWE1-HMI-VC-044":    ("P2", "清單順序依 HMI Settings List"),
 "SWE1-HMI-VC-045":    ("P2", "SETTINGS 不逾時、選擇後不關閉"),
 "SWE1-HMI-VC-046-01": ("P1", "按壓選取 —— 設定之主要互動"),
 "SWE1-HMI-VC-046-02": ("P1", "箭號開啟次層清單，主要導覽"),
 "SWE1-HMI-VC-046-03": ("P3", "首次進入之游標位置"),
 "SWE1-HMI-VC-046-04": ("P1", "直接觸碰內嵌選項調整，主要互動"),
 "SWE1-HMI-VC-046-05": ("P1", "旋鈕與方向鍵操作，主要互動之替代路徑"),
 "SWE1-HMI-VC-047-01": ("P2", "旋鈕於核取列之切換"),
 "SWE1-HMI-VC-047-02": ("P2", "旋鈕於多選列之循環"),
 "SWE1-HMI-VC-047-03": ("P2", "旋鈕於 -/+ 列之下壓態"),
 "SWE1-HMI-VC-047-04": ("P2", "下壓態之解除"),
 "SWE1-HMI-VC-048-01": ("P3", "選取後游標移至該列"),
 "SWE1-HMI-VC-048-02": ("P2", "設定變更確認音及其例外清單"),
 "SWE1-HMI-VC-049":    ("P2", "長按連續增減之速率（500ms／200ms）"),
 "SWE1-HMI-VC-050":    ("P2", "亮度長按連續增減之速率（500ms／500ms）"),
 "SWE1-HMI-VC-051-01": ("P2", "選取後指示標移動"),
 "SWE1-HMI-VC-051-02": ("P1", "設定被拒時指示標須退回 —— 否則 HMI 顯示車輛未接受之狀態"),
 "SWE1-HMI-VC-051-03": ("P2", "離開頁面後才收到拒絕之補救彈窗"),
 "SWE1-HMI-VC-052-01": ("P3", "進入時視圖置頂"),
 "SWE1-HMI-VC-052-02": ("P3", "Back 返回原位置而非置頂"),
 "SWE1-HMI-VC-053":    ("P3", "資訊圖示之呈現"),
 "SWE1-HMI-VC-054":    ("P2", "資訊彈窗之內容組成"),
 "SWE1-HMI-VC-055":    ("P2", "資訊圖示於行進中仍可用"),
 "SWE1-HMI-VC-056-01": ("P2", "自資訊彈窗直接變更選項"),
 "SWE1-HMI-VC-056-02": ("P3", "選畢關閉並返回清單"),
 # 章 13 —— Settings 與點火狀態
 "SWE1-HMI-VC-057":    ("P1", "Key Off／Timed／ACC 下 Settings 不可用 —— 電源狀態之關鍵邏輯"),
 "SWE1-HMI-VC-058-01": ("P1", "不可用時之提示彈窗"),
 "SWE1-HMI-VC-058-02": ("P2", "該彈窗不逾時"),
 "SWE1-HMI-VC-058-03": ("P2", "關閉後返回原畫面"),
 "SWE1-HMI-VC-059-01": ("P1", "Phone 設定之取用路徑"),
 "SWE1-HMI-VC-059-02": ("P1", "Phone 設定於 Key Off／ACC 仍可用 —— 例外規則"),
 "SWE1-HMI-VC-060-01": ("P1", "Audio 設定之取用路徑"),
 "SWE1-HMI-VC-060-02": ("P1", "Audio 設定於 Key Off／ACC 仍可用 —— 例外規則"),
 "SWE1-HMI-VC-061":    ("P1", "軟體更新於 Key Off／ACC 仍可用 —— 例外規則"),
 "SWE1-HMI-VC-062-01": ("P0", "**行車中禁入**：Wi-Fi 軟體下載之行進中攔阻，駕駛分心"),
 "SWE1-HMI-VC-062-02": ("P2", "攔阻彈窗關閉後之返回目標"),
 "SWE1-HMI-VC-063-01": ("P0", "**行車中禁入**：FOTA 流程中車輛起步之攔阻，駕駛分心"),
 "SWE1-HMI-VC-063-02": ("P2", "攔阻彈窗關閉後之返回目標"),
 "SWE1-HMI-VC-064-01": ("P1", "行進間轉入 Key Off 時之強制彈窗"),
 "SWE1-HMI-VC-064-02": ("P1", "該彈窗不逾時且不可關閉 —— 可關閉即進入無效狀態"),
 "SWE1-HMI-VC-064-03": ("P1", "回到 Run／Key On 時自動關閉並還原"),
 # 章 14 —— EPB
 "SWE1-HMI-VC-065-01": ("P0", "**安全**：行進中煞車服務模式須灰化"),
 "SWE1-HMI-VC-065-02": ("P1", "按下灰化項之提示彈窗"),
 # 章 16 —— Cabrio Widget
 "SWE1-HMI-VC-066":    ("P3", "widget 標題字面"),
}

RANK = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def apply_bound(local: str, upstream: str) -> tuple[str, str]:
    """R-VC11(b)：037 之值作為邊界，非映射來源。"""
    if upstream == "High" and RANK[local] > RANK["P1"]:
        return "P1", f"037=High 之下限，本地判 {local}"
    if upstream == "Low" and RANK[local] < RANK["P3"]:
        return "P3", f"037=Low 之上限，本地判 {local}"
    return local, ""


wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
raw = list(wb["Analysis Report"].iter_rows(values_only=True))
data = [r for r in raw[7:] if r[0] not in (None, "")]
P = re.compile(r"^SWE1-HMI-VC-(\d{3})$")
C = re.compile(r"^SWE1-HMI-VC-(\d{3})-(\d{2})$")
ids = [str(r[0]).strip() for r in data]
pc = {C.match(i).group(1) for i in ids if C.match(i)}
leaves = {i for i in ids
          if C.match(i) or (P.match(i) and P.match(i).group(1) not in pc)}

rows, conflicts, diverge = [], [], []
missing = sorted(leaves - set(LOCAL))
if missing:
    raise SystemExit(f"LOCAL 未涵蓋 {len(missing)} 個 leaf: {missing[:5]}")

for r in data:
    rid = str(r[0]).strip()
    if rid not in leaves:
        continue
    sec = str(r[2]).split("\n")[0].strip().rsplit("_", 1)[-1]
    up = str(r[17]).strip()
    local, why = LOCAL[rid]
    final, bound = apply_bound(local, up)
    rows.append((rid, sec, up, local, final, bound, why, str(r[3]).strip()))
    if bound:
        conflicts.append((rid, sec, up, local, final, bound))
    # R-VC11(c)：語意相悖 —— 本地 P0 而上游非 High
    if local == "P0" and up != "High":
        diverge.append((rid, sec, up, local))

out = ROOT / "data" / "priority_draft.tsv"
out.parent.mkdir(exist_ok=True)
with out.open("w", encoding="utf-8") as f:
    f.write("req_id\tsection\t037_priority\tlocal_p\tfinal_p\tbound_note\t"
            "basis\trequirement_title\n")
    for row in rows:
        f.write("\t".join(row) + "\n")

print(f"leaf 母體: {len(rows)}")
print("本地預判分布:", dict(Counter(r[3] for r in rows)))
print("套邊界後分布:", dict(Counter(r[4] for r in rows)))
print(f"\nR-VC11(b) 邊界抬升／壓低者: {len(conflicts)}")
for c in conflicts:
    print(f"  {c[0]:<20} §{c[1]:<8} 037={c[2]:<7} 本地={c[3]} -> 定案={c[4]}")
print(f"\nR-VC11(c) 語意相悖（本地 P0 而 037 非 High）: {len(diverge)}")
for d in diverge:
    print(f"  {d[0]:<20} §{d[1]:<8} 037={d[2]:<7} 本地={d[3]}")
print(f"\n寫出: {out}")
