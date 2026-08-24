"""VF230 量產：逐 leaf 之事實抽取（W-VF69 §5 之前置）。

**本檔只抽取，不臆造。** 抽不出者回 `None` 並具名其缺何項，
由呼叫端排除且逐條回報 —— **一個抽不出事實之 leaf，其 TC 無從書寫**。

抽取之項：
  setting   畫面上之設定名（TC 內加引號者）
  form      形態（取 `_vf230_forms.json`，分類式不改，R-VF77 三）
  PROXI 型  參數之條文逐字名（R-VF78 二）＋ 條文所帶之值
  訊號型    message／signal／raw／label（label 一律取 DBC `VAL_` 逐字，R-VF13）
"""
import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent

PROXI_CLAUSE = re.compile(r"retrieve the (.+?) (?:PROXI )?configuration", re.I)
# **W-VF71 第 3 項之放寬（R-VF82，2026-08-24）**：另有一式以參數名**起首**
# （`Turn_Signal_Camera_View PROXI configuration.` —— 無 `retrieve the`）。
# 其 2 條原判「連參數名都抽不出」而擬開 DR；**實測其參數名逐字在條文內、
# 且在 PROXI 表內** —— 即本層抽取式過窄，非資料所缺。
# **A-VF13／A-VF21／A-VF25／A-VF27 之同族**：抽取式與資料之實際形狀不合，
# 而其失敗回報為「無」而非「未查」（R-VF79 一）。
# 收窄之防：須為**句首**且緊接 `PROXI configuration`，不吞條文中段之任意底線詞。
PROXI_CLAUSE_LEAD = re.compile(
    r"^([A-Z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+) PROXI configuration\b")
# PROXI 條文帶值之**二式**（首版只認第一式，致 47 條誤報「未帶值」）：
#   (a) `If <param> = [Present], the LTM or ETM shall display …`
#   (b) `When the HMI receives the value [as] Absent via signal, $P$,
#        Then the HMI shall not display …`
PROXI_VALUE = [
    re.compile(r"If .{0,80}?=\s*\[([^\]]+)\]", re.I),
    re.compile(r"receives the value\s*(?:as\s*)?\[?([A-Za-z0-9_ ]+?)\]?\s*via signal",
               re.I),
]
# 極性：條文之結論句為 `shall not display` 者為否定分區
PROXI_NEG = re.compile(r"shall not display", re.I)

SIG = re.compile(r"\b(TELEMATIC_\w+|IPC_\w+)\.(\w+)\b")
# **message 有而 signal 無**者（`TELEMATIC_VEHICLE_SETUP signal value as Warn`）——
# 其訊號名於條文缺席，**不得以 DBC 值域反解**（實測：唯一解 13／多解 13，
# 多解者佔半，反解即推測）。列為獨立之缺類，不生成。
SIG_MSGONLY = re.compile(r"\b(TELEMATIC_\w+|IPC_\w+)\b(?!\.)")
# **值不得跨詞**：`signal value as LATCHING and send the signal to IPC within.`
# 若允許空格並以 `[.,]` 收尾，會吞掉整句 —— 故值一律為單一 token（不含空格）。
def match_label(tail: str, vals: dict[str, str]) -> tuple[str | None, str | None]:
    """以 **DBC 值域反向界定值之邊界** —— 取能與 `tail` 之起首相符之**最長**標籤。

    **不以散文界定**：首版以 `[A-Za-z0-9_]+`（不含空格）取值，
    致 `1st Press`／`Dynamic Gridlines ON`／`Level1` 等含空格或帶尾綴之標籤被截斷；
    而允許空格並以標點收尾者，又會把整句吞為值（R-VF82 所記之假陽）。
    **以值域為界則二病皆無**：候選集有限且來自資料，散文之長短不影響其邊界。
    """
    t = norm(tail)
    best = None
    for r, lab in vals.items():
        if t.startswith(norm(lab)) and (best is None or len(norm(lab)) > len(best[1])):
            best = (r, norm(lab), lab)
    return (best[0], best[2]) if best else (None, None)


# 值之**起點**（其終點由 `match_label` 依 DBC 值域決定）
SIG_VALUE_AT = [
    re.compile(r"signal value as\s+\[?"),
    re.compile(r"value\s*=\s*\["),
    re.compile(r"receives the value\s*(?:as\s*)?\[?"),
]

SIG_VALUE = [
    re.compile(r"signal value as\s+\[?([A-Za-z0-9_]+)\]?"),
    re.compile(r"value\s*=\s*\[([^\]]+)\]"),
    re.compile(r"receives the value\s*(?:as\s*)?\[?([A-Za-z0-9_ ]+?)\]?\s*via signal"),
]


def norm(x: str) -> str:
    """標籤之比對用正規化 —— 去非英數字並轉小寫。

    DBC 內有 `Enable_ LED_Chime`（多一個空格）等排版瑕疵，
    其與條文之 `Enable_LED_Chime` 為同一值。
    **只吸收排版差異，不吸收字義差異**（`Disable` ≠ `Disabled`，仍判不符）。
    """
    return re.sub(r"[^a-z0-9]", "", x.lower())


# ---- R-VF81：未指名值時之分區選法 ----
# 舊法「取最大 raw」**不認可**（V30 §3）—— 其與條文之動作語意無對應，
# 實測所取標籤含 `False` 2 次而條文動作為 `enable`，語意相反。
# 改為：依條文動作動詞之語意取值；語意側以 **DBC 標籤逐字**為據，不以 raw 大小為據。
ACT_ON = re.compile(r"chooses to (?:enable|turn on|activate)"
                    r"|selection .{0,30}\bto enable\b", re.I)
ACT_OFF = re.compile(r"chooses to (?:disable|turn off|deactivate)"
                     r"|selection .{0,30}\bto disable\b", re.I)
LAB_ON = {"on", "enabled", "enable", "true", "active", "present", "yes", "requested"}
LAB_OFF = {"off", "disabled", "disable", "false", "inactive", "absent", "no",
           "notenable", "notrequest", "zero"}


def lab_side(label: str) -> str | None:
    k = re.sub(r"[^a-z0-9]", "", label.lower())
    return "ON" if k in LAB_ON else ("OFF" if k in LAB_OFF else None)


def pick_unnamed(text: str, vals: dict[str, str]) -> tuple[str | None, str]:
    """回 (raw, 依據)。取不到者回 (None, 理由) —— 呼叫端標 PENDING，不取任一值。"""
    want = "ON" if ACT_ON.search(text) else ("OFF" if ACT_OFF.search(text) else None)
    if want is None:
        return None, "條文無 `chooses to enable/disable` 等動作動詞，語意側無從判"
    sides = {r: lab_side(l) for r, l in vals.items()}
    hit = [r for r, sd in sides.items() if sd == want]
    if len(hit) == 1:
        return hit[0], f"條文動作為 {want}，DBC 標籤 `{vals[hit[0]]}` 為該語意側之唯一者"
    if not hit:
        return None, (f"條文動作為 {want}，而 DBC 標籤 "
                      f"{sorted(vals.values())} 皆非二元語意，無對應側")
    return None, (f"條文動作為 {want}，而該語意側有 {len(hit)} 個標籤 "
                  f"{sorted(vals[r] for r in hit)}，非唯一")


# ---- R-VF91 二：訊號上行型之未指名值改依 canon §8.4.1 之佔位形式 ----
# **本判準之射程須自證**（R-VF82）：條文逐字列 `SNA`／`Not_Used`／`Invalid`／
# `Reserved` 四名，而 DBC 實有大小寫與數字尾綴之變體（`Not_used2`／`Reserved3`）。
# 判準取「四名之大小寫變體 ＋ 純數字尾綴」，**不及於含其他語素者**
# （`IGN_SNA`／`Reserved_for_future_use`／`No_Error`／`ChargeError`）——
# 擴及之則 `Not_Enable`／`No_Error` 等**真功能值**被誤殺，
# 即以一個收窄造出假資料缺陷（R-VF82 之同一形態，反向）。
EXCLUDE = re.compile(r"^(?:sna|not_?used|invalid|reserved)\d*$", re.I)


def valid_domain(vals: dict[str, str]) -> list[tuple[str, str]]:
    """回 [(raw, label)]，**依 DBC 之 raw 序**，已排除保留值。

    **序之選擇須具名**：R-VF91 二令「取列舉之首值」，而「列舉」所指為
    `input_test_data` 所列之 DBC 值域。**DBC 值域之列舉序為 raw 序**；
    字母序為本層施加者，非來源所有。二者於本組 100 條中 **38 條給出不同代表值**
    （`Trail_Num` 字母序給 `Four`、raw 序給 `One`；
    `Illuminated_Approach` 字母序給 `Ninety`、raw 序給 `Zero`），
    **字母序之代表值為任意**，故採 raw 序。
    """
    out = [(r, vals[r]) for r in sorted(vals, key=lambda x: int(x))
           if not EXCLUDE.match(vals[r].strip())]
    return out


def dbc() -> dict:
    d = json.loads((FEAT / "data/_dbc_parsed.json").read_text())
    out = {}
    for bus in d.values():
        for sig, occ in bus["sigs"].items():
            e = out.setdefault(sig, {"msgs": set(), "vals": {}})
            e["msgs"].update(o["msg"] for o in occ)
            e["vals"].update(bus["vals"].get(sig) or {})
    return out


def setting_name(title: str) -> str:
    """畫面上之設定名 —— 取 leaf 之 layer3 標題逐字。"""
    return re.sub(r"\s+", " ", title.replace("\\n", " ")).strip()


def extract(leaf: str, lf: dict, form: str, D: dict) -> tuple[dict | None, str]:
    text = re.sub(r"\s+", " ", lf["desc"].replace("\\n", " "))
    base = {"leaf_id": leaf, "form": form, "setting": setting_name(lf["title"]),
            "text": text}

    if form == "PROXI 型":
        m = PROXI_CLAUSE.search(text) or PROXI_CLAUSE_LEAD.match(text)
        if not m:
            return None, ("PROXI 型而抽不出參數名"
                          "（無 `retrieve the … configuration`，亦非參數名起首式）")
        v = next((mm for rx in PROXI_VALUE for mm in [rx.search(text)] if mm), None)
        if not v:
            return None, ("PROXI 型而條文未帶值"
                          "（無 `If … = [ … ]`，亦無 `receives the value … via signal`）")
        return {**base, "param": m.group(1).strip(), "value": v.group(1).strip(),
                "negative": bool(PROXI_NEG.search(text))}, ""

    if form in ("訊號送出型", "訊號上行型"):
        sigs = SIG.findall(text)
        if not sigs:
            mo = SIG_MSGONLY.search(text)
            if mo:
                return None, (f"{form} 而條文**只有 message `{mo.group(1)}`、無訊號名** "
                              "—— 不以 DBC 值域反解（多解者佔半），列 DR")
            return None, f"{form} 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名"
        msg, sig = sigs[0]
        d = D.get(sig)
        if not d:
            return None, f"訊號 `{sig}` 不存在於 DBC"
        if msg not in d["msgs"]:
            return None, (f"訊號 `{sig}` 之 DBC message 為 {sorted(d['msgs'])}，"
                          f"條文寫 `{msg}` —— 不符，不臆造")
        if not d["vals"]:
            return None, f"訊號 `{sig}` 於 DBC 無 `VAL_` 值域"
        want, raw = None, None
        for rx in SIG_VALUE_AT:
            mm = rx.search(text)
            if mm:
                # `receives the value **via signal** $X$` —— 其未指名值。
                # 無此守衛則該式被當成「有值而對不上」，18 條訊號上行型因而誤報。
                if re.match(r"\s*via\s", text[mm.end():]):
                    continue
                raw, want = match_label(text[mm.end():], d["vals"])
                if raw:
                    break
                # **不換訊號。** 首版於此加了「值對不上則改取同條文內值域能容納該值
                # 之另一訊號」—— 實測其於 `TrailerBrakeType032` 把條文明寫之
                # `Trail_Brk_Type_Req`（值域 Heavy_Electric 等）偷換為後句另一情境之
                # `Trail_Num_Req`（值域 One/Two/…），**產出驗錯訊號之 TC**。
                # 值屬條文所指名之訊號；對不上即為條文與 DBC 之不符，
                # **應報為不符，不得以換訊號消解之**（R-VF79 一）。
                tail = text[mm.end():mm.end() + 30].strip()
                # 比對失敗且首字小寫 → 其為散文而非值
                # （`signal value as selected language`）——
                # 應歸「未指名值」而非「值不符」。DBC 之標籤皆以大寫或數字起首。
                if tail[:1].islower():
                    continue
                return None, (f"條文指名之值 `{tail[:24]}` 對不上 `{sig}` 之 DBC 值域 "
                              f"{sorted(d['vals'].values())} —— 不臆造")
        pick_why, pending = "", False
        if raw is None:
            raw, pick_why = pick_unnamed(text, d["vals"])
            if raw is None:
                # R-VF81 三：**不取任一值，標 `PENDING: DR-39`** ——
                # 依 R-VS71／A-VS157 之作法，TC 照寫而於未解處標 PENDING，
                # **不以一個能通過之斷言代替**。
                pending = True
                raw = None
        if pending:
            # ---- R-VF91 一：R-VF81 三之適用範圍限縮為「訊號送出型」 ----
            # 上行型之刺激來自 HW，顧客不執行任何動作，其條文本就無動作動詞，
            # 故第一款對其恆不適用、第三款遂恆成立 —— 該恆成立非立法意圖。
            # ---- R-VF91 二：改依 canon §8.4.1 之佔位形式 ----
            if form == "訊號上行型":
                dom = valid_domain(d["vals"])
                if len(dom) >= 2:
                    (rep_raw, rep_lab), (oth_raw, oth_lab) = dom[0], dom[1]
                    return {**base, "msg": msg, "sig": sig,
                            "raw": rep_raw, "label": rep_lab,
                            "other_raw": oth_raw, "other_label": oth_lab,
                            "value_named": False, "pending": False,
                            "placeholder": True,
                            "domain": [l for _, l in dom],
                            "domain_raw": [r for r, _ in dom],
                            "excluded": [l for l in d["vals"].values()
                                         if EXCLUDE.match(l.strip())],
                            "pick_why": pick_why}, ""
                # 排除保留值後不足二值者**仍隔離** —— 佔位式需一代表值與一對偶，
                # 缺之則 procedure 之第 1 步無從寫，**不生成空殼**（R-VF91 二末）。
                return {**base, "msg": msg, "sig": sig, "raw": None, "label": None,
                        "other_raw": None, "other_label": None,
                        "value_named": False, "pending": True,
                        "domain": sorted(d["vals"].values()),
                        "pick_why": pick_why + f"；排除保留值後之有效值域為 "
                                               f"{[l for _, l in dom]}，不足二值"}, ""
            return {**base, "msg": msg, "sig": sig, "raw": None, "label": None,
                    "other_raw": None, "other_label": None,
                    "value_named": False, "pending": True,
                    "domain": sorted(d["vals"].values()),
                    "pick_why": pick_why}, ""
        # 對偶分區：取語意相反側之唯一者；無則取任一異值
        side = lab_side(d["vals"][raw])
        opp = [r for r, l in d["vals"].items()
               if lab_side(l) and lab_side(l) != side] if side else []
        other = opp[0] if len(opp) == 1 else next(
            (r for r in d["vals"] if r != raw), None)
        if other is None:
            return None, f"訊號 `{sig}` 之 DBC 值域只有一個值，無對偶分區"
        return {**base, "msg": msg, "sig": sig, "raw": raw,
                "label": d["vals"][raw], "other_raw": other,
                "other_label": d["vals"][other], "pending": False,
                "value_named": bool(want), "pick_why": pick_why}, ""

    if form == "設定顯示與修改型":
        return base, ""

    return None, f"形態 `{form}` 無對應之書寫式（未經 pilot）"


def load_all() -> tuple[list, list]:
    """回 (facts, skipped)。facts 依選池序。"""
    D = dbc()
    forms = {r["leaf_id"]: r["form"]
             for r in json.loads((FEAT / "data/_vf230_forms.json").read_text())["rows"]}
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    order = json.loads((FEAT / "data/_vf230_priority.json").read_text())["pool"]
    # **候選 = 選池（writability W0+W1）− pilot**，不扣隔離 ——
    # 隔離表由本檔之結果導出（抽不出者／PENDING 者皆入隔離），
    # 若此處再扣隔離即成環，其表徵為「事實抽不出」一類於次跑消失。
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    pool = {k for k, v in wr.items() if v["writable"] in ("W0", "W1")}
    pilots = set()
    for f in ("generated/vf230_pilot1.json", "generated/vf230_pilot2.json"):
        pilots |= {t["leaf_id"] for t in json.loads((FEAT / f).read_text())["tcs"]}
    body = pool - pilots

    facts, skipped = [], []
    for leaf in order:
        if leaf not in body:
            continue
        f, why = extract(leaf, lv[leaf], forms.get(leaf, "?"), D)
        (facts if f else skipped).append(f or {"leaf_id": leaf,
                                               "form": forms.get(leaf, "?"),
                                               "why": why})
    return facts, skipped


# ---- R-VF82：放寬判準之連帶檢驗（假陰／假陽二側）----
# 本輪之放寬為「值之終點改由 DBC 值域界定，不再由散文界定」。
# 其回收（假陰側）與其誤收（假陽側）皆須實測，且**須附一個
# 「原應不命中而放寬後可能命中」之實例**。
WIDEN_ANCHORS = [
    # (tail 片段, 值域, 期望之標籤 或 None, 性質)
    ("1st Press. CarPropertyService shall …", {"0": "Off", "1": "1st Press",
                                               "2": "2nd Press"},
     "1st Press", "假陰之回收：含空格之標籤，首版截為 `1st` 而對不上"),
    ("Dynamic Gridlines ON. The HMI …", {"0": "Dynamic Gridlines OFF",
                                         "1": "Dynamic Gridlines ON"},
     "Dynamic Gridlines ON", "假陰之回收：多詞標籤"),
    ("LATCHING and send the signal to IPC within.", {"0": "Latching",
                                                     "1": "Momentary"},
     "Latching", "**假陽之防**：放寬後仍只取標籤本身，不吞後續整句"),
    ("Disable to CarPropertyService …", {"0": "Disabled", "1": "Enabled"},
     None, "**假陽之防**：`Disable` 非 `Disabled` —— 字義差異不得被吸收"),
    ("Level1 …", {"0": "Level1", "1": "Level2"},
     "Level1", "假陰之回收：帶數字尾綴之標籤，首版截為 `Level`"),
    ("Level …", {"0": "Level1", "1": "Level2"},
     None, "**假陽之防**：`Level` 本身非任一標籤，不得取其一"),
]


# ---- R-VF82：`EXCLUDE`（保留值排除）之假陰／假陽錨點 ----
# 本判準為**收窄**（自值域中移除項），故其二側為：
#   假陰＝該排而未排（保留值混入有效值域，可能成為代表值）
#   **假陽＝不該排而排（真功能值被誤殺）** —— 本側為本判準之主要風險，
#   蓋 `Not_Enable`／`No_Error` 之字面與 `Not_Used` 近。
EXCLUDE_ANCHORS = [
    # (標籤, 期望排除?, 性質)
    ("SNA", True, "假陰之收：條文逐字四名之一"),
    ("Not_Used", True, "假陰之收：條文逐字四名之一"),
    ("Not_used2", True, "假陰之收：大小寫＋數字尾綴之變體"),
    ("Reserved3", True, "假陰之收：數字尾綴之變體"),
    ("Invalid", True, "假陰之收：條文逐字四名之一"),
    ("Not_Enable", False, "**假陽之防**：真功能值，本組 3 條之值域含之，不得誤殺"),
    ("No_Error", False, "**假陽之防**：`No_Error` 為狀態值，非保留值"),
    ("IGN_SNA", False, "**假陽之防**：含其他語素，非四名之變體 —— 具名為射程之邊界"),
    ("Reserved_for_future_use", False,
     "**假陽之防**：語意上為保留值而不符逐字四名 —— **具名待裁，本輪不擴**"),
    ("Enable", False, "**假陽之防**：與 `Not_Enable` 成對之另一側"),
]


# ---- R-VF82：`PROXI_CLAUSE_LEAD`（參數名起首式）之假陰／假陽錨點 ----
LEAD_ANCHORS = [
    ("Turn_Signal_Camera_View PROXI configuration. VehicleConfigManager shall …",
     "Turn_Signal_Camera_View", "假陰之回收：本輪 2 條之實際形態"),
    ("The HMI layer shall send a request to VehicleConfigManager to retrieve the "
     "Turn_Signal_Camera_View configuration.", None,
     "**假陽之防**：參數名於句中而非句首 —— 本式不得命中"
     "（其由 `PROXI_CLAUSE` 負責，二式不得互相掩蓋）"),
    ("VehicleConfigService shall check the requested Turn_Signal_Camera_View value "
     "from SystemProperties.", None,
     "**假陽之防**：條文中段之底線詞不得被當作參數名"),
    ("Country_Code PROXI configuration is read.", "Country_Code",
     "假陰之回收：同形態之另一參數"),
    ("Language PROXI configuration.", None,
     "**假陽之防**：無底線之單詞不符參數名之形，不得命中"),
]


def verify_lead() -> None:
    bad = []
    for text, want, kind in LEAD_ANCHORS:
        m = PROXI_CLAUSE_LEAD.match(text)
        got = m.group(1) if m else None
        ok = got == want
        print(f"  {'✅' if ok else '❌'} {kind}\n      {text[:52]!r} → {got!r}"
              f"（期望 {want!r}）")
        if not ok:
            bad.append(kind)
    if bad:
        raise SystemExit("R-VF82 錨點（PROXI_CLAUSE_LEAD）不符，停 —— " + "；".join(bad))


def verify_exclude() -> None:
    bad = []
    for lab, want, kind in EXCLUDE_ANCHORS:
        got = bool(EXCLUDE.match(lab))
        ok = got == want
        print(f"  {'✅' if ok else '❌'} {kind}\n      {lab!r} → 排除={got}（期望 {want}）")
        if not ok:
            bad.append(kind)
    if bad:
        raise SystemExit("R-VF82 錨點（EXCLUDE）不符，停 —— " + "；".join(bad))


def verify_widening() -> None:
    bad = []
    for tail, vals, want, kind in WIDEN_ANCHORS:
        raw, lab = match_label(tail, vals)
        ok = (lab == want)
        print(f"  {'✅' if ok else '❌'} {kind}\n      tail={tail[:44]!r} → {lab!r}"
              f"（期望 {want!r}）")
        if not ok:
            bad.append(kind)
    if bad:
        raise SystemExit("R-VF82 錨點不符，停 —— " + "；".join(bad))


if __name__ == "__main__":
    from collections import Counter
    print("=== R-VF82：放寬判準之假陰／假陽錨點 ===")
    verify_widening()
    print("\n=== R-VF82：`EXCLUDE`（R-VF91 二之保留值排除）之假陰／假陽錨點 ===")
    verify_exclude()
    print("\n=== R-VF82：`PROXI_CLAUSE_LEAD`（參數名起首式）之假陰／假陽錨點 ===")
    verify_lead()
    print()
    fa, sk = load_all()
    print(f"量產母體 {len(fa) + len(sk)}；可抽 **{len(fa)}**；抽不出 **{len(sk)}**")
    print("\n可抽者之形態分布：", dict(Counter(f["form"] for f in fa)))
    print("抽不出者之形態分布：", dict(Counter(s["form"] for s in sk)))
    print("\n抽不出之理由分類：")
    for why, n in Counter(re.sub(r"`[^`]*`", "`…`", s["why"]) for s in sk).most_common():
        print(f"  {n:4}  {why}")
    print(f"\n前 150 條（seq 268–417）之形態分布：",
          dict(Counter(f["form"] for f in fa[:150])))

