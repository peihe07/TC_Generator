#!/usr/bin/env python3
"""變體對造與覆蓋補洞之生成器（22 包 L-2／L-3）—— tc_id 074–078。

## 為什麼另起一支而不併入 gen_batch01／gen_batch02

號碼是**依批指派**的：batch01 為 017–044、batch02 為 045–073。
往 batch01 尾端追加會**撞上 batch02 之起點**。
本支自 074 起，`TC_START` 一改即知其邊界，兩支既有批次不動。

**本批不是「第三批」**：第三批指尚未取樣之 leaf；本支之四條**全部掛在已覆蓋
之 leaf 之下**（085／108／111／088），是對造與補洞，非新 leaf。

## 四條之由來

| tc_id | leaf | 由來 |
|---|---|---|
| 074 | `085`（9.1）| L-3：p14 `R1 High Only: "Stellantis Account" → "Connected Account"` 之對造（base variant）|
| 075 | `108`（10.3.1）| L-3：p16 `R1 High Only: ... Connected Account category ...` 之對造（R1 High）|
| 076 | `111`（11.4）| L-3：p17 `For China market only: do not show this content` 之對造（China）|
| 077 | `088`（9.2）| **L-2：9.2 條件 2 之覆蓋缺口** —— 原委派 11.3 不成立 |
| 078 | `109`（11.3）| **L-2 之連帶**：11.3 第二句之覆蓋缺口 —— 原委派 9.2，與 077 互指 |

## L-2 揭出的是一組**互指之委派**，不是單向的指錯

9.2 之 reasoning 稱其條件 2「由 11.3 承擔」，
而 11.3 之 remarks 同時稱其第二句「由 9.2 承擔」——
**兩條各自把那一側推給對方**，而雙方所指之條件並非同一件事
（`connected profile feature` vs `connectivity`）。
於是**兩個缺口同時存在，且兩份記載都看起來已交代**。
22 包點名的是其中一側；另一側是照同一把尺量出來的。

## L-3 之判準（V-1，本輪立）

**觸發要件為「spec 有明文之變體覆寫註記」，不是「另有一種配置」。**
判準與其母體見 `scripts/audit_variant_pairs.py`。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import steps, FUNCTIONAL               # noqa: E402
from gen_batch01 import _rec                          # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
TC_START = 74

# 每項：檔名後綴、req_id、priority、basis、內容
PAIRS = [
    # ── 074 —— 9.1 之 base variant 對造（L-3）────────────────────────
    dict(
        suffix="base",
        req_id="SWE1-HMI-PROF-085",
        prio=("P2", "Edit Profile 清單之順序；呈現層（與 TC-017 同級）"),
        spec=dict(
            title="Edit Profile tab lists options with Stellantis Account label",
            design=FUNCTIONAL,
            pre=steps("The vehicle is not an R1 High variant",
                      "A Driver Profile is active and setup assistant is not "
                      "completed for it"),
            data="NA",
            proc=steps("Open the Profile section and select the “Edit Profile” tab",
                       "Read the option list and check that the fourth item "
                       "reads Stellantis Account"),
            er=steps("The “Edit Profile” tab is displayed",
                     "The options are listed in the Table EDPR1 order: Resume "
                     "Setup (only if not complete), Edit Name, Edit Avatar, "
                     "Stellantis Account, Memory Seat (if applicable), Welcome "
                     "Pop Up, Delete Profile, What is linked to my Profile?, "
                     "Tutorials, More Settings; and a circled number 1 is shown "
                     "next to Resume Tutorials"),
            remarks="**L-3 之對造**：正向為 NR1L-UserProfiles-017（R1 High，"
                    "第四項為 Connected Account）。依 V-1 判準，p14 之變體覆寫註記"
                    "「R1 High Only: \"Stellantis Account\" to be replaced with "
                    "\"Connected Account\"」使該字面值隨變體而異，故須配對造。"
                    "本條為 base variant，其字面值取自 must_carry 之 Table EDPR1"
                    "（PDF p14）之「 Stellantis Account」",
            reasoning=(
                "驗證目標：9.1（EDPR1）之 **base variant** —— 非 R1 High 車上，"
                "Table EDPR1 第四項之 label 為 Stellantis Account。"
                "關鍵情境條件：變體為條件本身（§8.7.3），列 pre-condition；"
                "圈號 1 之前提同 TC-017。"
                "為什麼這樣切：**TC-017 把變體設為前提，於是多數車輛（非 R1 High）"
                "之清單反而未被測** —— 本條補的正是那一側。"
                "與 TC-017 構成 §7 之列舉配對：**只有兩條並存，才擋得住一個把"
                "兩個變體寫成同一個 label 之實作**。"
                "來源標示：字面值取自 must_carry（PDF p14 之 Table EDPR1），"
                "非 xlsx —— 該覆寫註記於 xlsx 側掉句"
                "（`data/xlsx_missing_clauses.tsv`）。"),
            kw=["Stellantis Account", "Table EDPR1", "base variant", "order"],
        ),
    ),
    # ── 075 —— 10.3.1 之 R1 High 對造（L-3）─────────────────────────
    dict(
        suffix="r1h",
        req_id="SWE1-HMI-PROF-108",
        prio=("P2", "linked-info 頁之內容（與 TC-039 同級）"),
        spec=dict(
            title="Driver Profile info page on R1 High omits subscription clause",
            design=FUNCTIONAL,
            pre=steps("The vehicle is an R1 High variant",
                      "The vehicle is equipped with Navigation",
                      "A Driver Profile is active",
                      "The vehicle is stationary"),
            data="NA",
            proc=steps("Open the Driver Profile info page",
                       "Read the Connected Account row and check that its "
                       "description carries no subscription clause"),
            # Q-1（25 包）：內嵌之逐字顯示文字須加雙引號（§11）——
            # 同批之 TC-055／TC-072 已加，本條漏加。
            er=steps("The Driver Profile Info Page is displayed",
                     "The Connected Account row reads “Save your preferences "
                     "to the cloud and access them from vehicle to vehicle.”, "
                     "with no Uconnect.com subscription clause; the other rows "
                     "of Table PIP1 are unchanged"),
            remarks="**L-3 之對造**：正向為 NR1L-UserProfiles-039（非 R1 High，"
                    "該列含「(with a Uconnect.com subscription)」）。依據為 PDF p16 之"
                    "**列級**註記「****R1 High Only: for the \"Connected Account\" "
                    "category title (if applicable) the Description is the "
                    "following: \"Save your preferences to the cloud and access "
                    "them from vehicle to vehicle.\"」。"
                    "本條只驗該列之差異，其餘 14 列由 TC-039 承擔",
            reasoning=(
                "驗證目標：10.3.1（PRINFO2.1）之 **R1 High 變體** —— Table PIP1 之"
                "Connected Account 列，其 Description 在該變體上少了訂閱那一句。"
                "關鍵情境條件：變體為條件本身；Navigation 之有無沿用 TC-039 之前提，"
                "使兩條之其餘 14 列可逐列比對。"
                "為什麼這樣切：**TC-039 以「非 R1 High」為前提，該覆寫本身遂無人測** ——"
                "而它是一個**列級**覆寫（20 包 C-1 之連帶發現），"
                "不測則「R1 High 上仍顯示訂閱句」之實作會通過。"
                "刻意略過：其餘 14 列不重複斷言 —— 覆寫只及於該列，"
                "重複斷言會使兩條之失敗訊號分不開。"),
            kw=["R1 High", "Table PIP1", "Connected Account", "row override"],
        ),
    ),
    # ── 076 —— 11.4 之 China market 對造（L-3）──────────────────────
    dict(
        suffix="china",
        req_id="SWE1-HMI-PROF-111",
        prio=("P2", "說明頁之內容展示（與 TC-013 同級）"),
        spec=dict(
            title="Connected Navigation row hidden on China market vehicles",
            design=FUNCTIONAL,
            pre=steps("The vehicle is a China-market vehicle",
                      "The vehicle is not an R1 High variant",
                      "A Driver Profile is active and the Edit Profile tab is "
                      "available"),
            data="NA",
            proc=steps("Open the Edit Profile tab and select the info icon",
                       "Read the row list and check that no Connected "
                       "Navigation row is shown"),
            er=steps("The Local vs Connected Profile screen is displayed",
                     "The row list shows only:\n"
                     "   a. Personalization (Presets, Menu Bar Order, App "
                     "Drawer Favorites, and more)\n"
                     "   b. App Store Download\n"
                     "   c. Marketplace (Access to Marketplace)\n"
                     "   and no Connected Navigation row is present"),
            remarks="**L-3 之對造**：正向為 NR1L-UserProfiles-013（非中國市場，"
                    "四列俱全）。依據為 PDF p17 之註記「For China market only: do "
                    "not show this content」—— 其掛在 **Connected Navigation 該列**"
                    "而非整張表（14 輪之範圍判定，J-5 同型）。"
                    "故本條驗「該列不在」，其餘三列仍在",
            reasoning=(
                "驗證目標：11.4（CPA2）之 **China market 變體** —— Table CPA2 之"
                "Connected Navigation 列不顯示。"
                "關鍵情境條件：市場別為條件本身（§8.7.3）；"
                "另排除 R1 High —— 該變體整張表不適用（TC-044 已承擔），"
                "**兩個覆寫若同時成立則無從分辨是哪一個生效**。"
                "為什麼這樣切：TC-013 以「非中國市場」為前提排除了本覆寫，"
                "**於是該覆寫本身無人測**；本條與 TC-013 構成列級之列舉配對。"
                "刻意略過：其餘三列之欄別標記（哪一欄有勾）由 TC-013 承擔，"
                "本條只斷言該列之缺席與其餘三列之在場。"),
            kw=["China market", "Connected Navigation", "Table CPA2", "hidden"],
        ),
    ),
    # ── 077 —— 9.2 條件 2 之覆蓋補洞（L-2）──────────────────────────
    dict(
        suffix="nofeat",
        req_id="SWE1-HMI-PROF-088",
        prio=("P1", "車輛不支援該功能之配置分支（與 TC-020 同級）"),
        spec=dict(
            title="Connected Account hidden when connected profile unsupported",
            design=FUNCTIONAL,
            pre=steps("The vehicle does not support the connected profile "
                      "feature",
                      "The vehicle is in a region with the brand app",
                      "A Driver Profile is active"),
            data="NA",
            proc=steps("Open the “Edit Profile” tab",
                       "Read the option list and check that no account button "
                       "or Connected Profile info is shown"),
            er=steps("The “Edit Profile” tab is displayed",
                     "No Connected Profile options or info and no Stellantis "
                     "Connected Account button are shown"),
            remarks="**L-2 之補洞**：9.2 有兩個獨立條件，TC-020 取「區域無 "
                    "<Brand> app」一側，本條取「車輛不支援 connected profile "
                    "feature」一側。**原 reasoning 將本側委派 11.3 之 leaf，"
                    "該委派不成立** —— 11.3 之條件為 `equipped with "
                    "connectivity`，與本側非同一語意（見上繳 22 §2）。"
                    "pre-condition 明列「區域有 app」，使兩個條件不同時成立。"
                    "**該前提為推得，非條文所載（M-4，23 包）**：spec 未明言"
                    "「有 `<Brand>` app 之區域、而車輛不支援 connected profile "
                    "功能」此一組合存在。若該組合在實車上造不出來，本 TC 之情境"
                    "即無法佈署 —— **但條件 2 是條文寫的，TC 不因情境難佈署而刪**"
                    "（§8.4.1）。已併 DR #3 送 RD 查詢",
            reasoning=(
                "驗證目標：9.2（EDPR2）之**第二個條件** —— 車輛不支援 connected "
                "profile 功能時，不顯示 Connected Profile 之選項／資訊與 "
                "Stellantis Connected Account 按鈕。"
                "關鍵情境條件：**pre-condition 明載「區域有 <Brand> app」** ——"
                "若不排除條件 1，兩個條件同時成立，失敗時分不出是哪一個沒生效"
                "（與 TC-020 之切法同一理由）。"
                "為什麼這樣切：**本條之存在理由是一個委派錯誤** ——"
                "TC-020 之 reasoning 原稱本側由 11.3（CPA1）承擔，"
                "而 11.3 之條件為 `equipped with connectivity`："
                "連網能力是硬體配置，支援 connected profile 功能是功能授權，"
                "**9.2 自身把「區域無 app」與本條件並列，即證兩者不等價** ——"
                "若「不支援該功能」只等於「無連網」，條件 1 便無處安放。"
                "指錯承擔者比不指更糟：它讓覆蓋稽核看起來是滿的（§8.2.1）。"
                "刻意略過：兩個條件同時成立之情形不另生成 —— 其結果與各自單獨"
                "成立時相同，加測不增訊號。"
                "**來源標示（M-4）**：pre-condition 之「區域有 `<Brand>` app」"
                "為**推得**（隔離條件 1 之需要），非 spec 所載；其可造性已送 DR #3。"),
            kw=["connected profile feature", "unsupported", "hidden",
                "Connected Account"],
        ),
    ),
    # ── 078 —— 11.3 第二句之覆蓋補洞（L-2 之連帶）──────────────────
    dict(
        suffix="noconn",
        req_id="SWE1-HMI-PROF-109",
        prio=("P1", "無連網車輛之配置分支（與 TC-040 同級之反面）"),
        spec=dict(
            title="Connected Account line hidden without connectivity",
            design=FUNCTIONAL,
            pre=steps("The vehicle does not support connectivity",
                      "A Driver Profile is active",
                      "The vehicle is stationary"),
            data="NA",
            proc=steps("Open the “Edit Profile” tab",
                       "Read the option list and check that no Connected "
                       "Account line item is shown"),
            er=steps("The “Edit Profile” tab is displayed",
                     "No Connected Account line item is displayed"),
            remarks="**L-2 之連帶補洞**：正向為 NR1L-UserProfiles-040"
                    "（有連網則一律顯示）。條文第二句 `Do not show if the "
                    "vehicle does not support connectivity` 原記為「由 9.2 之 "
                    "leaf 承擔」，而 9.2 同時記為「由 11.3 承擔」——"
                    "**互指之委派，兩側皆空**（見上繳 22 §2）。"
                    "本條與 TC-077 是同一個檢查量出來的兩個洞，非同一個洞",
            reasoning=(
                "驗證目標：11.3（CPA1）之**第二句** —— 車輛不支援連網時，"
                "Edit Profile 分頁不顯示 Connected Account 項目。"
                "關鍵情境條件：車輛配置為條件本身（§8.7.3），列 pre-condition。"
                "為什麼這樣切：本條與 TC-040 構成 §7 之列舉配對 ——"
                "**只有正向會使一個「永遠顯示該項目」之實作通過**。"
                "與 TC-077 之分野：077 驗「不支援 connected profile **功能**」"
                "（9.2 條件 2），本條驗「不支援**連網**」（11.3 第二句）——"
                "**兩者條件不同、所屬條文不同**，正是互指委派所掩蓋的那個差別。"
                "刻意略過：6.4.1（NOPR3.1）之無連網行為（PU0585 與 "
                "Login/Register 畫面）屬另一 leaf，已由 TC-006 承擔，本條不重複。"),
            kw=["connectivity", "unsupported", "hidden", "Connected Account"],
        ),
    ),
]


def build() -> list:
    rows = B.leaf_rows()
    out = []
    for n, item in enumerate(PAIRS, TC_START):
        rid = item["req_id"]
        ctx = B.assemble(rid, rows[rid])
        rec = _rec(rid, ctx, item["spec"], ctx["specification_reference"],
                   *item["prio"], n)
        rec["parent"] = f"{rid}-{item['suffix']}"
        rec["batch"] = "pairs22"
        rec["note"] = (
            f"22 包之對造／補洞 —— 與 `{rid}` 同一 leaf，**非新 leaf**；"
            f"檔名加 `-{item['suffix']}` 以免覆寫該 leaf 之既有產物")
        out.append(rec)
    return out


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    recs = build()
    for r in recs:
        (OUT / f"{r['parent']}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"寫出 {len(recs)} 個檔，共 {sum(len(r['tcs']) for r in recs)} 條 TC "
          f"（{recs[0]['tcs'][0]['tc_id']} … {recs[-1]['tcs'][0]['tc_id']}）")
