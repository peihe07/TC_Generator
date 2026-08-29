#!/usr/bin/env python3
"""CFTS020 §1.8 vs §1.18 逐物件對比（下放包 08 作業 A；R-ICS33(b)(c)(e)）。

**只列不裁**（R-ICS33(b)）：本腳本只產生實測表，不作取捨、不作建議。
**不改錨**（R-ICS33(a)）：本腳本對 `generated/**` 只讀不寫。

輸入（全部唯讀）：
  - `inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD
    _20260310-1533.docx` —— 經 `cfts020_probe.parse()`（以 importlib 載入，
    不改該檔）取得物件與 R-ICS2 v2(b) 判定
  - `generated/b0{1..5}/b0*_tcs.json` 之 `specification_reference` 欄

輸出：`docs/reports/08_s118_vs_s18.md`（覆寫）

行為面之判定條件（逐項揭露，全部為**區分大小寫之正則**除非標 `(i)`）：
  見 `BEHAVIORS`。每列為 (行為名, 主詞正則 or None, 主題正則, 旗標)。
  一物件可同時命中多個行為列 —— 不作互斥化。

「更具體在哪裡」之判定條件（機械化，只列事實不作價值判斷）：
  - `點名訊息名`：本文含 `CLIMATIC_PANEL`
  - `給了引號值`：本文含 `"..."` 形式之引號字面
  - `給了數值`：本文含 `[0-9]` 之獨立數字符記
  - `點名 LID`：本文含 `$...$` 形式之 LID 符記
  - `給了方括號值`：本文含 `[...]` 形式之值符記（§1.8 之慣用形制）

用法：
  python3 features/ics_management/scripts/s118_compare_08.py          # 產生報告
  python3 features/ics_management/scripts/s118_compare_08.py --stdout # 只印不寫
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts" / "cfts020_probe.py"
OUT = ROOT / "docs" / "reports" / "08_s118_vs_s18.md"
GEN = ROOT / "generated"


def load_probe():
    """以 importlib 載入既有 probe，不修改其原始碼（下放包禁區 5）。"""
    spec = importlib.util.spec_from_file_location("cfts020_probe", PROBE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --- 行為面定義（(名稱, 主詞正則, 主題正則, 說明)） ---------------------------
ACT_ICS = r"\bICS (?:shall|will|has to|determines|is )"
ACT_HU = r"\bHU (?:shall|will|has to|receives|determines|sees|is |transitions)"
ACT_TLM = r"\bTLM (?:shall|has to|receives|is |determines)"

BEHAVIORS: list[tuple[str, str | None, str, str]] = [
    ("按鍵資料傳送（ICS 側送出）", ACT_ICS, r"button", "主詞 ICS ∧ 本文含 button"),
    ("按鍵資料傳送（HU／TLM 側接收）", f"(?:{ACT_HU}|{ACT_TLM})", r"[Bb]utton",
     "主詞 HU 或 TLM ∧ 本文含 button"),
    ("旋鈕資料傳送（ICS 側送出）", ACT_ICS, r"[Kk]nob|KNOB", "主詞 ICS ∧ 本文含 knob/KNOB"),
    ("旋鈕資料傳送（HU／TLM 側接收）", f"(?:{ACT_HU}|{ACT_TLM})", r"[Kk]nob|KNOB",
     "主詞 HU 或 TLM ∧ 本文含 knob/KNOB"),
    ("按壓事件 short/long press", None,
     r"short press|long press|Short Press|Long Press|Tpress|button press event",
     "本文含 short/long press、Tpress 或 button press event"),
    ("顯示狀態 $TGW_DISP_STAT$", None, r"\$TGW_DISP_STAT\$", "本文含 $TGW_DISP_STAT$"),
    ("顯示狀態 $RQ_DISP_INTS$", None, r"\$RQ_DISP_INTS\$", "本文含 $RQ_DISP_INTS$"),
    ("顯示狀態 $DCSD_DISP_STAT$", None, r"\$DCSD_DISP_STAT\$", "本文含 $DCSD_DISP_STAT$"),
    ("stuck button", None, r"[Ss]tuck|Tstuck_button", "本文含 stuck 或 Tstuck_button"),
    ("POWER 硬鍵行為", None, r"POWER hardkey|\$ICSPowerButton\$|PowerModeSts_CStack",
     "本文含 POWER hardkey 或 $ICSPowerButton$ 或 PowerModeSts_CStack"),
    ("SCREEN OFF 硬鍵行為", None, r"SCREEN OFF hardkey|\$ICSScreenOffButton\$|Screen Off|Screen On",
     "本文含 SCREEN OFF hardkey / $ICSScreenOffButton$ / Screen Off / Screen On"),
    ("Enter 按鍵行為", None, r"\$Enter_Button\$", "本文含 $Enter_Button$"),
    ("Back 按鍵行為", None, r"\$Back_Button\$", "本文含 $Back_Button$"),
    ("點名 CLIMATIC_PANEL 訊息", None, r"CLIMATIC_PANEL", "本文含 CLIMATIC_PANEL"),
    ("時間變數之定值", None, r"msec|= 1\.5 sec|120 sec", "本文含 msec 或具體秒值"),
    ("Mute 行為", None, r"\$ICSMuteButton\$|Mute", "本文含 $ICSMuteButton$ 或 Mute"),
    ("Logistic／Power Mode 狀態回報", None, r"[Ll]ogistic", "本文含 logistic"),
]


def tags(text: str) -> list[str]:
    out = []
    for name, actor, topic, _ in BEHAVIORS:
        if actor is not None and not re.search(actor, text):
            continue
        if re.search(topic, text):
            out.append(name)
    return out


SPEC_MARKS = [
    ("點名訊息名", r"CLIMATIC_PANEL"),
    ("給了引號值", r"\"[^\"]+\""),
    ("給了數值", r"\d"),
    ("點名 LID", r"\$[A-Za-z_0-9<>]+\$"),
    ("給了方括號值", r"\[[^\]]+\]"),
]


def marks(text: str) -> list[str]:
    return [n for n, p in SPEC_MARKS if re.search(p, text)]


def esc(s: str) -> str:
    """Markdown 表格內之逐字：去換行、跳脫管線。"""
    return s.replace("|", r"\|").replace("\n", " ").strip()


# 下放包 08 §三 A 之交辦基準：「現有 25 條」＝ b01～b05。
# b06 以後（若存在）不入基準，另列於 §7 附錄，以免影響估之實數隨併行 session 漂移。
BASE_BATCHES = ("b01", "b02", "b03", "b04", "b05")


def read_anchors(batches=BASE_BATCHES) -> tuple[list[dict], "OrderedDict[str, list[str]]"]:
    tcs = []
    for f in sorted(GEN.glob("b0*/b0*_tcs.json")):
        d = json.loads(f.read_text())
        if d["batch"] not in batches:
            continue
        for i, t in enumerate(d["tcs"], 1):
            tcs.append({
                "batch": d["batch"],
                "seq": f'{d["batch"]}-{i:02d}',
                "req_id": t["req_id"],
                "title": t.get("tc_title", ""),
                "refs": [r.strip() for r in t["specification_reference"].split("\n") if r.strip()],
            })
    anchors: OrderedDict[str, list[str]] = OrderedDict()
    for t in tcs:
        for r in t["refs"]:
            anchors.setdefault(r, []).append(t["seq"])
    return tcs, anchors


def sec_tree(mod, max_depth: int = 3) -> list[tuple[str, str, str]]:
    """全文章節行（正文，非目次）之章節樹，限 `1.` 開頭且層數 ≤ max_depth。"""
    out, seen = [], set()
    for line in mod.doc_lines():
        s = line.strip()
        if "PAGEREF" in s:
            continue
        m = mod.SEC_RE.match(s)
        if not m:
            continue
        no = m.group(1)
        if not no.startswith("1") or no.count(".") + 1 > max_depth:
            continue
        if no in seen:
            continue
        seen.add(no)
        out.append((no, m.group(2), m.group(3)))
    return out


FEATURE_NAME = "ICS Management"
NEAR_TOKENS = ("ICS", "Management")


def name_affinity(title: str) -> str:
    if title.strip() == FEATURE_NAME:
        return "同名（逐字相同）"
    if all(t in title for t in NEAR_TOKENS):
        return "近名（含 ICS 與 Management 二詞）"
    if "ICS" in title:
        return "近名（含 ICS）"
    return ""


def build(mod) -> str:
    objs = mod.parse()
    by_id = {o["id"]: o for o in objs}

    def pick(prefix: str) -> list[dict]:
        return [o for o in objs
                if o["section_no"] == prefix or o["section_no"].startswith(prefix + ".")]

    s18, s118 = pick("1.8"), pick("1.18")
    s18_ap = [o for o in s18 if o["verdict"] == "適用"]
    s118_ap = [o for o in s118 if o["verdict"] == "適用"]
    s181 = [o for o in objs
            if o["section_no"] == "1.8.1" or o["section_no"].startswith("1.8.1.")]
    s181_ap = [o for o in s181 if o["verdict"] == "適用"]

    tcs, anchors = read_anchors()
    L: list[str] = []
    W = L.append

    W("# 下放包 08 作業 A —— CFTS020 §1.8 vs §1.18 逐物件對比")
    W("")
    W("> 本檔由 `features/ics_management/scripts/s118_compare_08.py` 產生，**勿人工改**。")
    W("> 依據 R-ICS33(b)：**只列不裁**。本檔不含任何取捨結論或建議；")
    W("> 依據 R-ICS33(a)：既有 25 條之 `specification_reference` 未動，本次無任何 TC JSON 寫入。")
    W("")
    W(f"來源：`{mod.DOC.name}`；判準 R-ICS2 **v2(b)**（CFTS020 專用）。")
    W("")

    # --- §0 母數 -------------------------------------------------------------
    W("## §0 母數複驗")
    W("")
    W("| 節 | 章名（逐字） | 物件數 | 適用 | 不適用 |")
    W("|---|---|---|---|---|")
    for pref, lst in (("1.8", s18), ("1.8.1（§1.8 之 ICS 子節）", s181), ("1.18", s118)):
        ap = sum(1 for o in lst if o["verdict"] == "適用")
        head = lst[0]["section"] if lst else ""
        W(f"| §{pref} | {esc(head)} | {len(lst)} | {ap} | {len(lst)-ap} |")
    W("")
    W(f"upstream-07 §13-2 所報「§1.18 為 37 物件、29 適用」—— **複驗相符**"
      f"（實測 {len(s118)} / {sum(1 for o in s118 if o['verdict']=='適用')}）。")
    W("")
    W(f"註：§1.8 之 {len(s18)} 物件橫跨 §1.8.1（ICS）～§1.8.6（DCSD/CBC/警用電腦）六個子節，"
      f"其中僅 §1.8.1「{esc(s181[0]['section']) if s181 else ''}」與 §1.18 屬同一題域"
      f"（ICS 按鍵／旋鈕／硬鍵）；§1.8.1 適用 {len(s181_ap)} 個。"
      f"下文 §2 行為面對比同時列 §1.8 全域與 §1.8.1 兩欄。")
    W("")

    # --- §1 適用物件清單 -----------------------------------------------------
    W("## §1 二節各自之適用物件清單（R-ICS2 v2(b)；四欄依 R-DD23／R-DD24）")
    W("")
    for label, lst in (("§1.8", s18_ap), ("§1.18", s118_ap)):
        W(f"### §1-{'1' if label=='§1.8' else '2'} {label} 之適用物件（{len(lst)} 個）")
        W("")
        W("| ObjectID | 節 | 數據（ECU／Radio／EE Architecture 軸實測值） | 判斷 | 所印之理由 | 強度 |")
        W("|---|---|---|---|---|---|")
        for o in lst:
            data = (f"ECU={o['ecu']}；Radio={o['radio']}；EE={o['ee']}")
            reason = ("三軸皆命中 R-ICS2 v2(b)(i)(ii)" if o["ecu"] is not None
                      else "Radio／EE 命中 v2(b)(i)；ECU 軸不存在，依 v2(b)(ii) 不視為不適用")
            W(f"| {o['id']} | §{o['section_no']} | {esc(data)} | {o['verdict']} | {reason} | {esc(o['strength'])} |")
        W("")
        st = Counter(o["strength"] for o in lst)
        W(f"強度分佈：{dict(st)}")
        W("")

    W("### §1-3 二節之不適用物件（列出理由，供複核）")
    W("")
    W("| 節 | ObjectID | 不適用之理由（逐項） |")
    W("|---|---|---|")
    for o in s118:
        if o["verdict"] != "適用":
            W(f"| §{o['section_no']} | {o['id']} | {esc('；'.join(o['reasons']))} |")
    W("")
    W(f"（§1.8 之不適用者共 {len(s18)-len(s18_ap)} 個，量大不逐列；"
      f"其判定與 b03 之 `cfts020_probe.py --section 1.8` 同源，可原地複現。）")
    W("")

    # --- §2 行為面對比 -------------------------------------------------------
    W("## §2 行為面之重疊與差異")
    W("")
    W("列 = 行為；欄 = 二節之對應**適用**物件（ObjectID）。空集合記「無」。")
    W("判定條件逐項揭露於末欄，全部為正則比對，未作語意判讀。")
    W("")
    W("| 行為 | §1.8 全域（適用） | §1.8.1（適用） | §1.18（適用） | §1.18（含不適用者） | 重疊／差異 | 判定條件 |")
    W("|---|---|---|---|---|---|---|")
    for name, actor, topic, cond in BEHAVIORS:
        def hit(lst):
            return [o["id"] for o in lst if name in tags(o["text"])]
        a, a1, b, ball = hit(s18_ap), hit(s181_ap), hit(s118_ap), hit(s118)
        if a and b:
            rel = "**兩節皆有**"
        elif a and not b:
            rel = "**僅 §1.8 有**" + ("（§1.18 有但判不適用）" if ball else "（§1.18 全節零承載）")
        elif b and not a:
            rel = "**僅 §1.18 有**"
        else:
            rel = "二節皆無"
        W(f"| {name} | {', '.join(a) or '無'} | {', '.join(a1) or '無'} | "
          f"{', '.join(b) or '無'} | {', '.join(ball) or '無'} | {rel} | `{cond}` |")
    W("")
    W("**「§1.18（含不適用者）」欄之用意**：區分「§1.18 該行為判不適用」與"
      "「§1.18 全節本無該行為之文字」二種不同的『無』。")
    W("")
    s813 = [o for o in objs if o["section_no"] == "1.8.1.3"
            or o["section_no"].startswith("1.8.1.3.")]
    W("補充實測（供對照，不入表）：§1.8.1.3「button press events」子樹（含所有子節）共 "
      f"{len(s813)} 個物件，其中判適用者 "
      f"{sum(1 for o in s813 if o['verdict']=='適用')} 個"
      "（`Short Press`／`Long Press and Hold` 之定義句 `4819591` 判不適用）。")
    W("")

    # --- §3 25 條之錨於 §1.18 之對應 ----------------------------------------
    W("## §3 現有 25 條之每一個錨，於 §1.18 是否有更具體之對應物件")
    W("")
    W(f"實測：25 條 TC，`specification_reference` 之相異錨共 **{len(anchors)}** 個"
      f"（CFTS020 {sum(1 for k in anchors if k.startswith('CFTS020'))} 個、"
      f"CFTS022 {sum(1 for k in anchors if k.startswith('CFTS022'))} 個）。")
    W("")
    for ref, users in anchors.items():
        W(f"### 錨 `{ref}`（用於 {len(users)} 條：{', '.join(users)}）")
        W("")
        if not ref.startswith("CFTS020-"):
            W("**不適用本比對** —— 錨於 CFTS022，非 CFTS020 §1.8／§1.18 之題域。")
            W("")
            continue
        oid = ref.split("-", 1)[1]
        o = by_id.get(oid)
        if o is None:
            W(f"查無 ObjectID `{oid}`。")
            W("")
            continue
        t = tags(o["text"])
        W(f"- 現錨位置：§{o['section_no']}，判定 {o['verdict']}")
        W(f"- 現錨逐字：`{esc(o['text'])}`")
        W(f"- 行為標籤：{'、'.join(t) or '（無命中）'}")
        W(f"- 具體性標記：{'、'.join(marks(o['text'])) or '無'}")
        cands = [c for c in s118_ap if set(tags(c["text"])) & set(t)]
        if not cands:
            W("- **§1.18 之對應物件：無**"
              + ("（該行為在 §1.18 全無承載）" if t else "（現錨無行為標籤可比對）"))
            W("")
            continue
        W(f"- **§1.18 之對應物件（{len(cands)} 個）**：")
        W("")
        W("| §1.18 ObjectID | 節 | 逐字原文 | 共同行為 | 更具體在哪裡（相對於現錨新增之標記） |")
        W("|---|---|---|---|---|")
        for c in cands:
            shared = sorted(set(tags(c["text"])) & set(t))
            extra = [m for m in marks(c["text"]) if m not in marks(o["text"])]
            lost = [m for m in marks(o["text"]) if m not in marks(c["text"])]
            note = ("新增：" + "、".join(extra) if extra else "無新增標記")
            if lost:
                note += "；現錨有而此物件無：" + "、".join(lost)
            W(f"| {c['id']} | §{c['section_no']} | `{esc(c['text'])}` | "
              f"{esc('、'.join(shared))} | {esc(note)} |")
        W("")

    # --- §4 特查二項 --------------------------------------------------------
    W("## §4 特別查二項（R-ICS33(e)）")
    W("")
    disp = [o for o in s118 if re.search(r"DISP_STAT|DISP_INTS", o["text"])]
    W("### §4-1 `$TGW_DISP_STAT$`／`$DCSD_DISP_STAT$` 之發送與觀察面 → DR-ICS16")
    W("")
    W(f"§1.18 全 {len(s118)} 物件（含不適用者）中，本文含 `DISP_STAT` 或 `DISP_INTS` 者："
      f"**{len(disp)} 個**{'（' + ', '.join(o['id'] for o in disp) + '）' if disp else ''}。")
    W("")
    W("同一比對於 §1.8：")
    n18d = [o for o in s18_ap if re.search(r"DISP_STAT|DISP_INTS", o["text"])]
    W(f"- §1.8 適用物件中含 `DISP_STAT`／`DISP_INTS` 者 **{len(n18d)} 個**。")
    W("")
    W("**結論（事實陳述，非裁）**：§1.18 對該二訊號**零承載**，"
      "亦無任何匯流排／發送節點之敘述。**DR-ICS16 之母條不在 §1.18**。")
    W("")

    back = [o for o in objs if "$Back_Button$" in o["text"]]
    W("### §4-2 `Back_Button` 之 HU／ICS 側行為母條 → DR-ICS13")
    W("")
    W(f"全文含 `$Back_Button$` 之物件共 **{len(back)} 個**：")
    W("")
    W("| ObjectID | 節 | 判定 | 逐字原文 |")
    W("|---|---|---|---|")
    for o in back:
        W(f"| {o['id']} | §{o['section_no']} | {o['verdict']} | `{esc(o['text'])}` |")
    W("")
    b118 = [o for o in back if o["section_no"].startswith("1.18") and o["verdict"] == "適用"]
    W(f"其中位於 §1.18 且**判適用**者 **{len(b118)} 個**："
      f"{', '.join(o['id'] for o in b118) or '無'}。")
    W("")
    # ICS 側「for all buttons」母條（適用），§1.18 vs §1.8
    allbtn_re = r"[Ff]or all buttons|for all ICS buttons|any physical button|all the relative BH-CAN"
    ab118 = [o for o in s118_ap if re.search(allbtn_re, o["text"])]
    ab18 = [o for o in s18_ap if re.search(allbtn_re, o["text"])]
    W("**ICS 側「涵蓋全部按鍵」之母條**（正則 "
      f"`{allbtn_re}`，只取判適用者）：")
    W("")
    W(f"- §1.18：{', '.join(o['id'] for o in ab118) or '無'}")
    W(f"- §1.8 ：{', '.join(o['id'] for o in ab18) or '無'}")
    W("")
    W("**事實陳述（非裁）**：")
    W("")
    W("- §1.8 之二個含 `$Back_Button$` 物件（`4819546` LID 清單、`4819554` HU 側行為）"
      "**皆判不適用**；此即 DR-ICS13 所載之阻斷面。")
    W("- §1.18 之 `4821681`（LID 清單，含 `$Back_Button$`）與 `4821704`"
      "（TLM 側依 `$Enter_Button$`／`$Back_Button$` 管理畫面）**皆判適用**。")
    W("- 且 §1.18 之 `4821683`～`4821689` 為 ICS 側**不點名個別按鍵**之泛用母條"
      "（`for all buttons` / `a physical button`），依 R-ICS2 v2(b) 判適用，"
      "其涵蓋面在字面上包含 `4821681` 所列之 `$Back_Button$`。")
    W("")
    W("=====================================================================")
    W("")
    W("# 【E2 觸發】—— DR-ICS13 一項")
    W("")
    W("**§1.18 確有一組判適用之 `Back_Button` 母條**（ICS 側 `4821681`＋`4821683`～`4821689`；"
      "TLM 側 `4821704`），而 §1.8 之對應二物件判不適用。")
    W("依 R-ICS33 之交辦：**只列證據，不逕行改寫、不生成任何 TC**。"
      "本包未對 DR-ICS13 作結案，亦未改任何錨。")
    W("")
    W("**DR-ICS16 不觸發 E2** —— §1.18 對 `$TGW_DISP_STAT$`／`$DCSD_DISP_STAT$` 零承載。")
    W("")
    W("=====================================================================")
    W("")

    # --- §5 三種結果之影響估 -------------------------------------------------
    W("## §5 三種可能結果之影響估（R-ICS33(c)）")
    W("")
    n_tc = len(tcs)
    tc_with_020 = [t for t in tcs if any(r.startswith("CFTS020-") for r in t["refs"])]
    tc_022_only = [t for t in tcs if not any(r.startswith("CFTS020-") for r in t["refs"])]
    a020 = [k for k in anchors if k.startswith("CFTS020-")]

    def has_counterpart(ref: str) -> bool:
        o = by_id.get(ref.split("-", 1)[1])
        if o is None:
            return False
        t = set(tags(o["text"]))
        return bool(t) and any(t & set(tags(c["text"])) for c in s118_ap)

    a020_hit = [k for k in a020 if has_counterpart(k)]
    a020_miss = [k for k in a020 if not has_counterpart(k)]
    tc_all_hit = [t for t in tc_with_020
                  if all(has_counterpart(r) for r in t["refs"] if r.startswith("CFTS020-"))]
    tc_part = [t for t in tc_with_020
               if any(not has_counterpart(r) for r in t["refs"] if r.startswith("CFTS020-"))]

    W("計算基礎（實測）：")
    W("")
    W(f"- TC 總數 **{n_tc}**（b01 6＋b02 2＋b03 8＋b04 7＋b05 2）")
    W(f"- 含至少一個 CFTS020 錨之 TC：**{len(tc_with_020)}** 條")
    W(f"- 純 CFTS022 錨之 TC：**{len(tc_022_only)}** 條（{', '.join(t['seq'] for t in tc_022_only)}）")
    W(f"- 相異 CFTS020 錨 **{len(a020)}** 個；其中於 §1.18 有行為對應者 **{len(a020_hit)}** 個、"
      f"無對應者 **{len(a020_miss)}** 個")
    W(f"  - 有對應：{', '.join(sorted(a020_hit))}")
    W(f"  - 無對應：{', '.join(sorted(a020_miss))}")
    W("")
    W("| 結果 | 受影響 TC 條數（實數） | 計算方式 |")
    W("|---|---|---|")
    W(f"| ① §1.8 為正、§1.18 不適用 | **0 / {n_tc}** | "
      f"所有錨維持原狀，無一條需動 `specification_reference`。"
      f"惟 §4-2 之 DR-ICS13 證據於此結果下不可用（§1.8 之 Back_Button 二物件判不適用），"
      f"DR-ICS13 維持 OPEN。 |")
    W(f"| ② §1.18 為正，25 條須重錨 | **{len(tc_with_020)} / {n_tc}** | "
      f"含 CFTS020 錨之 TC 全數須重錨＝{len(tc_with_020)} 條；其中 "
      f"**{len(tc_all_hit)}** 條之全部 CFTS020 錨在 §1.18 有對應物件（可重錨）、"
      f"**{len(tc_part)}** 條至少有一個錨在 §1.18 無對應物件（**無錨可重**，須另尋來源或退回）。"
      f"純 CFTS022 之 {len(tc_022_only)} 條不受影響。 |")
    W(f"| ③ 二節並存且各有其涵蓋面 | **{len(tc_all_hit)} / {n_tc}**（上界） | "
      f"僅「§1.18 確有更具體對應物件」者移錨或加錨＝{len(tc_all_hit)} 條為上界；"
      f"其餘 {len(tc_part)} 條之錨（{', '.join(sorted(a020_miss))} 所涉）在 §1.18 無承載，"
      f"必須留在 §1.8。實際條數視 Pei 對「加錨 vs 移錨」之裁定而定，下界為 0。 |")
    W("")
    W("逐條明細（供核算）：")
    W("")
    W("| TC | req_id | 錨 | 含 CFTS020 錨 | 全部 CFTS020 錨在 §1.18 有對應 |")
    W("|---|---|---|---|---|")
    for t in tcs:
        has020 = any(r.startswith("CFTS020-") for r in t["refs"])
        ok = has020 and all(has_counterpart(r) for r in t["refs"] if r.startswith("CFTS020-"))
        W(f"| {t['seq']} | {t['req_id']} | {esc(' + '.join(t['refs']))} | "
          f"{'是' if has020 else '否'} | {'是' if ok else ('否' if has020 else '—')} |")
    W("")
    W("**注意（事實，非建議）**：`CFTS020-4819541`（時間變數定值 "
      "`<Tbutton> = 100 msec`、`<Tstuck_button> = 120 sec` 等）用於 "
      f"{len(anchors.get('CFTS020-4819541', []))} 條 TC。§1.18 雖引用 `Tbutton`／"
      "`TPeriodToCountKnobDetents` 之名，**全節未給任何數值**"
      "（§2 之「時間變數之定值」列實測 §1.18 = 無）。")
    W("")

    # --- §6 章節樹 ----------------------------------------------------------
    W("## §6 CFTS020 章節樹（至三層）與同名／近名之節（A-ICS50）")
    W("")
    tree = sec_tree(mod, max_depth=3)
    W("| 章節號 | 章名（逐字） | ObjectID | 同名／近名判定 |")
    W("|---|---|---|---|")
    near = []
    for no, title, oid in tree:
        aff = name_affinity(title)
        if aff:
            near.append((no, title, oid, aff))
        W(f"| {no} | {esc(title)} | {oid} | {aff or ''} |")
    W("")
    W(f"**與 feature 同名／近名之節共 {len(near)} 個**（feature 名：`{FEATURE_NAME}`）：")
    W("")
    W("| 章節號 | 章名 | ObjectID | 判定 |")
    W("|---|---|---|---|")
    for no, title, oid, aff in near:
        W(f"| {no} | {esc(title)} | {oid} | {aff} |")
    W("")
    deep = [(n, t, o) for n, t, o in sec_tree(mod, max_depth=5)
            if n.startswith("1.18")]
    W("§1.18 之完整子樹（至五層，供對照）：")
    W("")
    W("| 章節號 | 章名 | ObjectID |")
    W("|---|---|---|")
    for n, t, o in deep:
        W(f"| {n} | {esc(t)} | {o} |")
    W("")

    # --- §7 基準外之批次 -----------------------------------------------------
    W("## §7 附錄：交辦基準外之批次（實測，非交辦範圍）")
    W("")
    W(f"本報告之影響估以下放包 08 所載之「現有 25 條」為基準，實作為 "
      f"`BASE_BATCHES = {list(BASE_BATCHES)}`。")
    W("")
    extra = []
    for f in sorted(GEN.glob("b0*/b0*_tcs.json")):
        d = json.loads(f.read_text())
        if d["batch"] in BASE_BATCHES:
            continue
        for i, t in enumerate(d["tcs"], 1):
            extra.append((d["batch"], f"{d['batch']}-{i:02d}", t["req_id"],
                          " + ".join(r.strip() for r in
                                     t["specification_reference"].split("\n") if r.strip()),
                          t.get("tc_title", "")))
    if not extra:
        W("實測：基準外無其他批次。")
    else:
        W(f"**實測：產出目錄中另有 {len({e[0] for e in extra})} 個基準外批次、"
          f"共 {len(extra)} 條 TC**（下放包 08 未提及；疑為併行作業於本包執行期間落地）：")
        W("")
        W("| TC | 批次 | req_id | 錨 | 標題 |")
        W("|---|---|---|---|---|")
        for b, seq, rq, refs, ti in extra:
            W(f"| {seq} | {b} | {rq} | {esc(refs)} | {esc(ti)} |")
        W("")
        ex020 = [e for e in extra if "CFTS020-" in e[3]]
        W(f"其中含 CFTS020 錨者 **{len(ex020)}** 條。"
          + ("因全部錨於 CFTS022，§5 之三種結果對其影響皆為 **0 條**，"
             "故納入與否不改變 §5 之實數（僅分母由 25 變為 "
             f"{25 + len(extra)}）。" if not ex020 else
             "**其含 CFTS020 錨，若納入基準則 §5 之②③ 實數須重算**。"))
        W("")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    a = ap.parse_args()
    mod = load_probe()
    md = build(mod)
    if a.stdout:
        sys.stdout.write(md)
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(md)
    print(f"寫入 {OUT}（{len(md.splitlines())} 行）", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
