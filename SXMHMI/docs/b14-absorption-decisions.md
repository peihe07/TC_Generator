# B14 — R10-2 decision for the 1 unallocated clause

**1 of 1 absorbed.** Running total of absorptions in this delivery: **4**
(B8 `4872880` → 094; B10 `4872953` → 148 and `4872955` → 149; B14 `4873322` → 187).

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4873322 | 1.5.21.2.3 | SFR | pass | **pass** | **absorbed into leaf 187** |

> The value of T<OD Response> shall be 2 seconds.

Leaf 187's clause requires the user to be notified of a buffering event "after
T<OD Response> time expires" and never says what that value is. Alone it has no
pass criterion — a notification after any delay satisfies it, including one
after thirty seconds.

`4873322` is the value. One buffering event shows both the notification and its
timing, so condition (b) holds in the same strong form as the B8 and B10
absorptions: the absorbed clause is what makes the allocated clause testable
rather than merely convenient to observe alongside.

The ER reads both sides of the boundary — nothing at 1 second, the notification
at 3 seconds — which is what turns "after 2 seconds" into a failing condition.

Leaf 186 depends on the same value from the other direction: it requires
T<OD Response> to be a modifiable parameter, and its TC verifies the change by
watching the notification move off the 2 second mark.
