# G117 —— 多值欄之集合正規化比對（R-P173）

> 多值欄（`ECU` / `EE Architecture` / `Radio` / `Market`）以**集合**比對：去空白、統一大小寫、次序不計。
> 其餘欄位仍以字串比對（僅正規化連續空白）。
> 屬性自原始 CFTS 文字層重抽，未採信既有表格之抄錄值。

## `SWE-PM-025` 三對（R-P167 / 23 §四）

### `4941569` vs `4941572` —— **正規化後仍相異：ECU**

| 屬性 | 多值 | `4941569` | `4941572` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | LTM, RRM | LTM, RRM, ETM | **否** | `4941572` 獨有 {etm} |
| EE Architecture | 是 | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | 2017 | 2017 | 是 | — |
| Radio | 是 | allSys | allSys | 是 | — |
| State | 否 | Under Review | Under Review | 是 | — |

### `4941570` vs `4941573` —— **正規化後仍相異：ECU**

| 屬性 | 多值 | `4941570` | `4941573` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | RRM, LTM | RRM, ETM, LTM | **否** | `4941573` 獨有 {etm} |
| EE Architecture | 是 | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | 2017 | 2017 | 是 | — |
| Radio | 是 | allSys | allSys | 是 | — |
| State | 否 | Under Review | Under Review | 是 | — |

### `4941571` vs `4941574` —— **正規化後仍相異：ECU**

| 屬性 | 多值 | `4941571` | `4941574` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | LTM, RRM | ETM, RRM, LTM | **否** | `4941574` 獨有 {etm} |
| EE Architecture | 是 | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | 2017 | 2017 | 是 | — |
| Radio | 是 | allSys | allSys | 是 | — |
| State | 否 | Under Review | Under Review | 是 | — |

## R-P135 三對（`SWE-PM-038`）

### `4941727` vs `4941728` —— **正規化後仍相異：Model Year**

| 屬性 | 多值 | `4941727` | `4941728` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | LTM, ETM, RRM | RRM, LTM, ETM | 是 | — |
| EE Architecture | 是 | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | （無） | 2017 | **否** | `4941727` 獨有 {（無）}；`4941728` 獨有 {2017} |
| Radio | 是 | allSys | allSys | 是 | — |
| State | 否 | Under Review | Under Review | 是 | — |

### `4941729` vs `4941730` —— **正規化後仍相異：Model Year、Radio、State**

| 屬性 | 多值 | `4941729` | `4941730` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | LTM, ETM, RRM | RRM, ETM, LTM | 是 | — |
| EE Architecture | 是 | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | （無） | 2017 | **否** | `4941729` 獨有 {（無）}；`4941730` 獨有 {2017} |
| Radio | 是 | allSys, noSys | allSys | **否** | `4941729` 獨有 {nosys} |
| State | 否 | New | Under Review | **否** | `4941729` 獨有 {new}；`4941730` 獨有 {under review} |

### `4941735` vs `4941736` —— **正規化後仍相異：Model Year、Radio、State**

| 屬性 | 多值 | `4941735` | `4941736` | 集合相同 | 差集 |
|---|---|---|---|---|---|
| Artifact Type | 否 | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 | — |
| ECU | 是 | LTM, ETM, RRM | RRM, LTM, ETM | 是 | — |
| EE Architecture | 是 | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 | — |
| Market | 是 | All | All | 是 | — |
| Model Year | 否 | （無） | 2017 | **否** | `4941735` 獨有 {（無）}；`4941736` 獨有 {2017} |
| Radio | 是 | allSys, noSys | allSys | **否** | `4941735` 獨有 {nosys} |
| State | 否 | New | Under Review | **否** | `4941735` 獨有 {new}；`4941736` 獨有 {under review} |

## 彙總

| 對 | 正規化後 | 相異欄 |
|---|---|---|
| `4941569` vs `4941572` | **相異** | ECU |
| `4941570` vs `4941573` | **相異** | ECU |
| `4941571` vs `4941574` | **相異** | ECU |
| `4941727` vs `4941728` | **相異** | Model Year |
| `4941729` vs `4941730` | **相異** | Model Year、Radio、State |
| `4941735` vs `4941736` | **相異** | Model Year、Radio、State |
