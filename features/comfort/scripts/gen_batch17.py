#!/usr/bin/env python3
"""Batch 17 generator — 97／98 之補產，五個此前無檔之 parent。

97 §1 訂正了判準（「條文說了什麼，就驗什麼」），據此解封 20 個 leaf；
98 之六問裁定其確切條數為 **31**。其中 **23 條**屬五個**此前連 JSON 檔都
沒有**之 parent，由本檔擁有：

    2.12    SWE1-HVAC-016   016-01 ×4／-02／-03            6   （98 §C／§F）
    2.12.2  SWE1-HVAC-018   018-01 ×5／-02／-03／-04 ×3／-05／-06
                                                          12   （98 §D／§E）
    9.1     SWE1-HVAC-039                                  1
    14.15   SWE1-HVAC-099                                  1
    18.1    SWE1-HVAC-129   129-01／-02／-03                3

其餘 8 條之 parent **已有檔**，依批次 16 之前例（一個 JSON 只有一個 owner）
於各自之 owner 內解封，其列同樣取自 `gap_tcs.py`：

    gen_batch3.py   2.1    001-01 ×3／001-02   4
    gen_batch9.py   2.5    006-04              1
    gen_batch9.py   2.13   019-02              1
    gen_batch5.py   10.4   047（第二條）        1
    gen_batch6.py   16.16  122-02              1

**tc_id 435–465，明寫於 `gap_tcs.py`**（R-C43），依 req_id 遞增指派 ——
既有 434 列一列都不重編（65 §1）。

`019-03` 與 `072` 不在本包內：前者之全部內容為對 VF HVAC document 之委派
（97 §2.4，比照 `080-02` 維持不產，其列為 96 §1 之留空列），後者維持
`[BLOCKED-SPEC]`。

Usage:
    python3 features/comfort/scripts/gen_batch17.py
"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_item import apply_test_item   # 95 —— 上半照抄條文、下半測項定義
from gap_tcs import gap_for             # 97／98 之 31 列，tc_id 明寫

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

# 本檔所擁有之五個 parent。其餘三個 parent 之列由 owner generator 取用。
#
# **parent id 以 `PARENT()` 組出而不寫成 `("SWE1-HVAC-nnn", …)` 之字面**：
# `withheld-not-generated` gate 以該形態辨識 WITHHELD 之宣告（`lint_tcs.py`
# 之 `WITHHELD_DECL`），寫成 tuple 字面會被讀成「這個 leaf 被停下」——
# 而本檔正是產出它們的地方。**同 gen_batch9.py 於 81 §2.1 所記之同一陷阱。**
def PARENT(n: str) -> str:
    return "SWE1-HVAC-" + n


OWNED = {
    "2.12":   dict(parent=PARENT("016"), test_set="Airflow and Defrost"),
    "2.12.2": dict(parent=PARENT("018"), test_set="Airflow and Defrost"),
    "9.1":    dict(parent=PARENT("039"), test_set="Rear Climate"),
    "14.15":  dict(parent=PARENT("099"), test_set="Climate Popups"),
    "18.1":   dict(parent=PARENT("129"), test_set="Home Screen Widget"),
}

_R16 = (
    "**C 之缺口（98 §C）**：`C13` 之「There are 4 Airflow Mode displayed in "
    "this order (1) Face, (2) Face plus Feet, (3) Feet, (4) Feet plus "
    "Windshield」**在 037 沒有任何 leaf** —— 三個 leaf 分別為高亮放大、"
    "main category control 之顯示、互斥，無一承載該列舉與其順序；"
    "**不借掛 `016-01` 之 req_id**：那等於以我方之切分冒充 037 之單位"
    "（§8.2、R-C33 第一項），故登為 **R-C16 覆蓋缺口**，入 profile §5.4 之"
    "清單並與既有成員分記其形態；**其被涵蓋之程度如實記** —— 本節四條逐一選取"
    "四個模式，**四模式之存在因此被間接驗證，而其顯示順序未被驗證**"
    "（兩者分別陳述，不以前者掩蓋後者），且**鏡射表已獨立記載同一缺口**"
    "（`ch16_mirror_map.tsv` 之 16.12 ↔ 2.12 列，分界欄寫「未涵蓋：C13 之"
    "四模式清單與其順序」）。")

REASONING = {
 "2.12":
   "驗證目標：2.12（C13）定出四個氣流模式之 ON 態呈現、主類別控制對所選模式之顯示，以及一次只能選一個，三個 037 leaf 分別對應之；**本節此前全節停下**（批次 10 之 WITHHELD，理由為 DR #31：四模式配置於條文中無正面之適用條件），而 97 §1 裁定該理由錯 ——「不知道誰適用」與「不知道有哪些」是兩件事，條文把四個模式逐字列出且給定順序，哪一種車配四模式則是測試員面對實車時看得見的事。關鍵情境條件：第三軸之值一（4 模式），PC 逐字取條文所列之四個模式名並具名 (2.12)；**DR #31 不撤** —— 它問的仍是「哪一種配置產生值一」，只是不再阻塞生成；依 **R-C34**，可觀察量在 climate screen 與主類別控制，第九／十三軸與 EMEA 皆暴露 → 全數補，第十二軸不暴露（不觀察 tab）；EMEA 之逐條答依鏡射表 `16.12 ↔ 2.12`（partial）之分界欄，涵蓋側者 `yes`、落在未涵蓋側（四模式之身分）者 `no`。為什麼這樣切：`016-01` 依 **§8.3 之列舉軸**拆為四條（條文逐字列舉四個模式，一模式一條，各自可失效），`016-02` **不依四模式展開**（98 §F —— 其列舉軸已於 `016-01` 用過一次，再展開四條僅差觀察位置，落入 §10.6 之近重複），`016-03` 之互斥另取狀態轉換。刻意略過：**ER 不寫模式圖示之外觀**（PDO 所有），只驗高亮與尺寸增加此二條文明載之事；" + _R16,
 "2.12.2":
   "驗證目標：2.12.2（C13.1）定出 Mode 硬鍵之循環序與其排除項、長按只跳一格、Climate main 內外之兩種呈現、主類別標籤之更新，以及後排畫面上該鍵改的是前排模式，六個 037 leaf 分別對應之；**本節此前全節停下**（批次 10，同 DR #31），解封之理由同 `2.12`。關鍵情境條件：第三軸之值一（其迴圈即 C13 之四模式集合，故 2.12 依 R-C29 併入 specification_reference，只取其模式集合之事實而不驗其行為，§8.2.1）；**Mode 硬鍵之存在依 R-C31 為條文自身之執行前提**（條文把它指為被操作之物），`018-06` 另取「後排氣候畫面之存在」為同一形態之前提；依 **R-C34** 第九軸全數補 —— `018-04` 三條之 pop-up 雖為 6.3 之明文例外，惟其位置以 Climate main category control 為錨，**與其鏡射節 16.12.1 之既有判斷一致**（同一句條文，兩側不得異判）—— 第十三軸與 EMEA 補，第十二軸不暴露。為什麼這樣切：`018-01` 依 §8.3 之列舉軸拆為**四段轉換各一條**（第四條即繞回起點），**另依 §7 之 `ALWAYS` 加一條負向**（98 §E）—— 條文列舉了迴圈之四個成員並明文排除 Defrost，該負向條走完整個迴圈並驗 Defrost 自始至終不出現，其驗證目標為迴圈成員之封閉性而非四段轉換之附帶；`018-04` 依 **§5.7 拆為三條**（98 §D）—— 按鍵所生之「彈窗出現」與「不跳轉」為同一觸發之兩個後果故併為一條，而「閒置 3 秒」與「按下 Mode HC 以外之鍵」為條文逐字列舉之兩個不同觸發故各一條。刻意略過：**`018-06` 之 ER 不寫「後排模式不變」**（條文只說該鍵改前排，後排是否連動由 7.1 CR1 承載，跨節移植違 §8.2.1）；**`018-05` 維持一條** —— 條文以「In both cases」把兩個情境併為一句，其驗證目標為標籤之更新此一事，兩個步驟各覆一個情境。**上半之句界須記**：`sents()` 於 C13.1 之括號處斷句，致「Defrost will not be included in the loop)」落入 `018-02` 之句而非 `018-01` 之句，故該負向條之 test_item 上半為迴圈句、Defrost 之驗證由其下半承載 —— 此為切句工具之界線（`clause_map.py` 自陳括號非可靠句界訊號），非選錯句",
 "9.1":
   "驗證目標：9.1（CR11）一句定出某些車輛另有後排氣候之附加控制與捷徑，其 037 leaf 即本節自身（無子條）；**本節此前停下**（批次 14，理由為「其內容只有『某些車輛另有附加控制』一句，無可觀察之行為」），而 97 §1 裁定該理由錯 ——「那些控制存在」本身即測試員對照實車可判之事，「是哪些」則由該車之配置回答。關鍵情境條件：本節之句子逐字為 PC 並標 `spec-verbatim`；依 **R-C34** 第九／十三軸與 EMEA 暴露 → 補，EMEA 之逐條答為 `no`（ch16 十八節無後排氣候之節）。為什麼這樣切：一葉一 TC，兩個步驟各覆條文所列之一類（controls 與 shortcuts）；**現行之不一致於此修正**（97 §2.5）—— `9.2`／`9.3`／`9.4`／`9.4.1` 之七條**以本句為 PC**，而本句自身之 leaf 此前無列，即七條引一個在工作簿上不存在的條件。刻意略過：**「See CFTS043 for details」為對外部文件之指引** —— 其內容（哪些車、哪些控制）不在本條之 ER 內（§8.2.1）；CFTS043 雖已列 profile §1.1，惟本條所引者僅為條文自身之句子，不引該文件之清單",
 "14.15":
   "驗證目標：14.15（HVACSB1）一句定出可用之舒適控制隨車輛配置而異，"
   "其 037 leaf 即本節自身。**本節此前停下**（批次 11，理由為「陳述有對照"
   "關係而不給對照」，併入 DR #32）—— **97 §2.8 裁定其可驗**："
   "ER 寫「顯示之控制與該車配置相符」，**不寫是哪一組控制**（那才是缺的"
   "對照），而「有控制且與該車配置相符」為測試員對照實車可判之事。"
   "關鍵情境條件：本節之句子為 14.16～14.18 三節之 PC 出處（R-C29），"
   "本條回取其自身；依 **R-C34** 三軸暴露 → 補，其組裝與所引之三節同形。"
   "為什麼這樣切：一葉一 TC。刻意略過：**DR #32 不撤** —— "
   "它問的仍是「哪一種配置給哪一組控制」，本條不回答該問，"
   "只驗兩者相符（§8.4.1：不寫條文沒給的值 ≠ 不寫測試）。",
 "18.1":
   "驗證目標：18.1（W0）與 17.1 之條文**逐字相同**，定出 Comfort widget 具兩個畫面（Comfort 與 Seats），三個 037 leaf 與 `17.1` 之 `124-01`／`124-02`／`124-03` **逐條對位**（畫面數／第一頁之身分／第二頁之身分），故照其測法寫三條（97 §2.7）；**本節此前停下**（批次 8，理由為「章標題不是條文，故螢幕尺寸之 PC 連出處都沒有，不補則與 17.1 全同」），97 §2.7／98 §1 裁定生成。**其 PC 之出處須具名為何物**：`10.25\" Home screen` 出自 SR24 export 之**章標題** —— **此為全語料唯一一處 PC 之出處為章標題而非條文句子者**，已逐字記於 `gap_tcs.py` 之 `PC_1025`，使它日後不被讀成一般用法；其功能即區辨本節與 17.1，故 `duplicate_of` 不填（§10.6 之四項嚴格等價中 verification target 相異：所驗者為該螢幕上之 widget），**惟三條之 `test_item`／`test_procedure`／`expected_result` 與 17.1 三條逐字相同**，已入 `pending_sibling.tsv` 之 `equivalent_tc_pairs` 並具名為本包之發現。關鍵情境條件：同 17.1 —— `129-01`／`129-03` 另取第十六軸（Comfort Features 有無，出處 17.3），`129-02` 不取（第一頁為 Comfort，其存在不依賴座椅類配備）；依 **R-C34** 第九／十三軸與 EMEA 暴露 → 補。為什麼這樣切：三者之失效可各自獨立發生（畫面數對而內容錯、或 Seats 頁缺）；刻意略過：**18.1 之 full_text 不含 17.1 尾端之「(Refer to the Comfort – Front Comfort/Climate and Comfort – Heated/Vented Seats HMI sections for complete logic.)」** —— 故 `17.1` 之 R-C39 討論於本節不適用，三條同樣只驗兩個畫面之存在與其名稱而不驗其內容（§8.2.1），另依 **R-C17**，首頁之頁面管理行為定義於 Home Screen spec，不寫入本批",
}

DIST_AXIS = {
 "2.12": {"axis": "verification target within 2.12 (C13)",
          "delta": "-440…-443 = 四個模式各自之 ON 態呈現（§8.3 列舉軸）；"
                   "-444 = 主類別控制 fan space 之顯示；"
                   "-445 = 四者之互斥。§10.6 之四項嚴格等價中 verification "
                   "target 相異，`duplicate_of` 不填"},
 "2.12.2": {"axis": "trigger within 2.12.2 (C13.1)",
            "delta": "-446…-449 = 迴圈之四段轉換；-450 = 迴圈成員之封閉性"
                     "（Defrost 之排除，§7 之負向配對）；-451 = 長按；"
                     "-452 = Climate main 內之高亮；-453 = Climate main 外之"
                     "彈窗與不跳轉（同一觸發之兩個後果，§5.7 併為一條）；"
                     "-454／-455 = 條文逐字列舉之兩個消失觸發；"
                     "-456 = 主類別標籤；-457 = 後排畫面上之前排改動"},
 "18.1": {"axis": "verification target within 18.1 (W0)",
          "delta": "-463 = 畫面之數目（two）；-464 = 第一頁之身分（Comfort）；"
                   "-465 = 第二頁之身分（Seats）。與 17.1 之 -115／-116／"
                   "-117 之區辨在 PC 之螢幕（10.25\"），其 verification "
                   "target 因而相異，`duplicate_of` 不填"},
}


def _iar() -> dict:
    with (FEATURE / "data" / "interface_axis_review.tsv").open(
            encoding="utf-8") as fh:
        return {r.pop("outline"): r for r in csv.DictReader(fh, delimiter="\t")}


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    iar = _iar()
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0

    for o, meta in OWNED.items():
        parent, test_set = meta["parent"], meta["test_set"]
        tcs = gap_for(parent)
        if not tcs:
            raise SystemExit(f"{parent}: gap_tcs.py 無此 parent 之列")
        doc = {
            "parent": parent, "outline": o, "batch": test_set,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o],
            "keywords": [], "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [], "interface_axis_review": iar[o],
            "tcs": apply_test_item(tcs),
        }
        (OUT / f"{parent}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{parent}  {o:8} {len(tcs)} TC  [{test_set}]")

    leaves = len({x["req_id"] for m in OWNED.values()
                  for x in gap_for(m["parent"])})
    print(f"\n{leaves} leaves -> {total} TCs (tc_id 明寫於 gap_tcs.py)")
    if total != 23 or leaves != 14:
        raise SystemExit(f"expected 14 leaves / 23 TCs, got {leaves} / {total}")


if __name__ == "__main__":
    main()
