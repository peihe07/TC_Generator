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
        m = PROXI_CLAUSE.search(text)
        if not m:
            return None, "PROXI 型而抽不出參數名（無 `retrieve the … configuration`）"
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
        want = None
        for rx in SIG_VALUE:
            mm = rx.search(text)
            if mm:
                want = mm.group(1).strip()
                break
        raw = None
        if want:
            for r, lab in d["vals"].items():
                if norm(lab) == norm(want):
                    raw = r
                    break
            if raw is None:
                return None, (f"條文指名之值 `{want}` 不在 `{sig}` 之 DBC 值域 "
                              f"{sorted(d['vals'].values())} 內 —— 不臆造")
        else:
            # 條文未指名值 → 取 DBC 之最大 raw 為被驗分區（其對偶為最小 raw）
            raw = max(d["vals"], key=lambda x: int(x))
        other = min(d["vals"], key=lambda x: int(x))
        if other == raw:
            other = next((r for r in d["vals"] if r != raw), None)
        if other is None:
            return None, f"訊號 `{sig}` 之 DBC 值域只有一個值，無對偶分區"
        return {**base, "msg": msg, "sig": sig, "raw": raw,
                "label": d["vals"][raw], "other_raw": other,
                "other_label": d["vals"][other],
                "value_named": bool(want)}, ""

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
    body = set(json.loads((FEAT / "data/_vf230_body.json").read_text())["body"])

    facts, skipped = [], []
    for leaf in order:
        if leaf not in body:
            continue
        f, why = extract(leaf, lv[leaf], forms.get(leaf, "?"), D)
        (facts if f else skipped).append(f or {"leaf_id": leaf,
                                               "form": forms.get(leaf, "?"),
                                               "why": why})
    return facts, skipped


if __name__ == "__main__":
    from collections import Counter
    fa, sk = load_all()
    print(f"量產母體 {len(fa) + len(sk)}；可抽 **{len(fa)}**；抽不出 **{len(sk)}**")
    print("\n可抽者之形態分布：", dict(Counter(f["form"] for f in fa)))
    print("抽不出者之形態分布：", dict(Counter(s["form"] for s in sk)))
    print("\n抽不出之理由分類：")
    for why, n in Counter(re.sub(r"`[^`]*`", "`…`", s["why"]) for s in sk).most_common():
        print(f"  {n:4}  {why}")
    print(f"\n前 150 條（seq 268–417）之形態分布：",
          dict(Counter(f["form"] for f in fa[:150])))
