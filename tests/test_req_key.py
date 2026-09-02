"""`scripts/lint_delivery_spec.req_key()` 之單元測試（VS-SL-08 §1）。

要旨：鍵之各段須**型別可比**，且**純同型資料之相對序不得改變**。
"""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lint_delivery_spec import req_key  # noqa: E402


def test_混型同位不再拋錯():
    """原 TypeError 案：第 4 段一為數字 `6`、一為字串 `AutoDoorLocks`。"""
    a = req_key("SWE1-VC-6AuxSwitches-002")
    b = req_key("SWE1-VC-AutoDoorLocks-015")
    assert a < b or b < a          # 可比即可，不預設方向
    assert a != b


def test_同位數字先於字串():
    assert req_key("SWE1-VC-6AuxSwitches-002") < req_key("SWE1-VC-AutoDoorLocks-015")


def test_純數字段按值而非字典序():
    """`-10` 須排在 `-2` 之後（字典序會相反）。"""
    assert req_key("SWE1-VC-Foo-002") < req_key("SWE1-VC-Foo-010")
    assert req_key("SWE1-VC-Foo-002") < req_key("SWE1-VC-Foo-015")


def test_純字串段按字典序():
    assert req_key("SWE1-VC-AutoDoorLocks-001") < req_key("SWE1-VC-BlindSpotAlert-001")


def test_相同鍵相等():
    """重複之 D 值（相鄰列共用同一需求 ID）須判相等，非逆序。"""
    a = req_key("SWE1-VC-HeadlightsOffDelay-014")
    assert a == req_key("SWE1-VC-HeadlightsOffDelay-014")
    assert not (a < a)


def test_較短之鍵排前():
    assert req_key("SWE1-VC-Foo") < req_key("SWE1-VC-Foo-001")


def test_段之切分未變():
    """切分規則沿用 `\\d+|[A-Za-z]+`，非英數字元一律為分隔。"""
    assert [seg[1] for seg in req_key("SWE1-VC-Foo-002")] == ["SWE", 1, "VC", "Foo", 2]


@pytest.mark.parametrize("ids", [
    ["SWE1-VC-Foo-001", "SWE1-VC-Foo-002", "SWE1-VC-Foo-010"],
    ["SWE1-VC-A-001", "SWE1-VC-B-001", "SWE1-VC-C-001"],
])
def test_純同型之相對序不變(ids):
    """純數字段與純字串段之既有序不得因本修而改變。"""
    assert sorted(ids, key=req_key) == ids


def test_全鍵可排序_無TypeError():
    """混型集合整體可排序 —— 修前此處即拋 TypeError。"""
    ids = ["SWE1-VC-6AuxSwitches-002", "SWE1-VC-AutoDoorLocks-015",
           "SWE1-VC-4AUXSwitches-028", "SWE1-VC-HeadlightsOffDelay-014"]
    out = sorted(ids, key=req_key)
    assert len(out) == len(ids)
    assert out[0].endswith("-028") and "4AUX" in out[0]      # 數字段 4 最小
