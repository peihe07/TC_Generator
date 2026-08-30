# PENDING 清單 —— 交付說明之附件（Pei 裁定 2026-08-30 §2.1(b)）

> **帶 `PENDING` 出貨之附件。** 全案 **317** 個 TC，其中 **195** 個含 `PENDING`；
> `PENDING` 行數合計 **712**。
> **`PENDING` 之文字一律保留原樣**（§2.1(a)）；**可交付列與帶 `PENDING` 之列分開計數**（§2.1(d)）。

## 一、型別分布

| 型別 | TC 數 | `PENDING` 行 |
|---|---:|---:|
| 第二型（觀測手段） | 81 | 268 |
| 第四型（觸發手段） | 30 | 143 |
| 切分型（統攝／重複表述） | 27 | 104 |
| 判準型（能力／全稱） | 17 | 53 |
| 車外表徵（伺服器側） | 13 | 57 |
| 中斷處理之判準 | 11 | 36 |
| 安全與認證之觀測 | 11 | 34 |
| 第三型（區辨手段） | 5 | 17 |
| **合計** | **195** | **712** |

## 二、DR 分布

| DR | TC 數 |
|---|---:|
| `DR-SU2` | 151 |
| `DR-SU3` | 27 |
| `DR-SU6` | 17 |
| `DR-SU4` | 11 |
| `DR-SU7` | 11 |
| `DR-SU1` | 3 |
| `DR-SU5` | 1 |

## 三、逐列

| TC ID | 037 列 | Test Set | DR | 型別 | `PENDING` 行 |
|---|---|---|---|---|---:|
| `newR1L-SU-001` | `175` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 1 |
| `newR1L-SU-002` | `176` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 1 |
| `newR1L-SU-003` | `176` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 3 |
| `newR1L-SU-008` | `184` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-009` | `179` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-010` | `181` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 2 |
| `newR1L-SU-011` | `315` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 5 |
| `newR1L-SU-012` | `316` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-013` | `317` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-014` | `318` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 5 |
| `newR1L-SU-015` | `319` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-016` | `320` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-017` | `313` | Interruption Handling | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-021` | `131` | Update HMI | `DR-SU5` | 第二型（觀測手段） | 3 |
| `newR1L-SU-030` | `093` | ROV Installation | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-031` | `094` | ROV Installation | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-052` | `083` | USB Update | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-053` | `084` | USB Update | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-056` | `012` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-058` | `014` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-059` | `015` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-060` | `028` | Update Policy | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-061` | `030` | Update Policy | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-066` | `171` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-067` | `172` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-068` | `173` | Integrity Verification | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-069` | `174` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-070` | `310` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-071` | `311` | Integrity Verification | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-072` | `312` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-073` | `338` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-078` | `343` | Deployment Conditions | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-101` | `062` | Wi-Fi Download | `DR-SU2` | 第三型（區辨手段） | 5 |
| `newR1L-SU-102` | `063` | Wi-Fi Download | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-106` | `067` | Wi-Fi Download | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-110` | `330` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 5 |
| `newR1L-SU-111` | `331` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-112` | `332` | Status Reporting | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-113` | `333` | Status Reporting | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-114` | `334` | Status Reporting | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-115` | `339` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-116` | `358` | Status Reporting | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-119` | `005` | FOTA Overview | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-122` | `008` | FOTA Overview | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-123` | `347` | Session Management | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-124` | `348` | Session Management | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-125` | `349` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-126` | `350` | Session Management | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-127` | `351` | Session Management | `DR-SU2` | 第四型（觸發手段） | 4 |
| `newR1L-SU-128` | `352` | Session Management | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-129` | `353` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-131` | `355` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-132` | `356` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-133` | `361` | Session Management | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-134` | `368` | Session Management | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-135` | `369` | Session Management | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-136` | `111` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 4 |
| `newR1L-SU-139` | `114` | TBM Reflash | `DR-SU2` | 第二型（觀測手段） | 1 |
| `newR1L-SU-143` | `118` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-145` | `120` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-147` | `122` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-149` | `124` | TBM Reflash | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-153` | `187` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-154` | `169` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-155` | `191` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-156` | `272` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-157` | `277` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-158` | `273` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-159` | `274` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-160` | `275` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-161` | `276` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-162` | `279` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-163` | `288` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-164` | `289` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-165` | `290` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-166` | `370` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-167` | `371` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-168` | `372` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-169` | `373` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-170` | `374` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-171` | `375` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 4 |
| `newR1L-SU-172` | `376` | Update Agent | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-173` | `377` | Update Agent | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-174` | `378` | Update Agent | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-175` | `379` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-177` | `381` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-178` | `382` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-179` | `383` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-180` | `321` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-181` | `322` | Interruption Handling | `DR-SU2` | 車外表徵（伺服器側） | 1 |
| `newR1L-SU-182` | `323` | Interruption Handling | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-183` | `324` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-184` | `325` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 4 |
| `newR1L-SU-185` | `326` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-186` | `327` | Interruption Handling | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-188` | `329` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-189` | `357` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-191` | `360` | Interruption Handling | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-192` | `363` | Telematics Client | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-193` | `364` | Telematics Client | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-194` | `365` | Telematics Client | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 6 |
| `newR1L-SU-195` | `366` | Telematics Client | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-196` | `367` | Telematics Client | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-197` | `195` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-198` | `198` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-199` | `199` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-200` | `201` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-202` | `205` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-203` | `206` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-204` | `207` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-205` | `208` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-206` | `209` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-207` | `210` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-208` | `211` | Client Architecture | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-209` | `212` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-211` | `252` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-212` | `253` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-213` | `254` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-214` | `255` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-215` | `256` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-216` | `257` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-217` | `258` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-218` | `260` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-219` | `261` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-220` | `262` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-221` | `264` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-222` | `265` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-223` | `267` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-224` | `268` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-225` | `269` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-226` | `270` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-227` | `281` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-228` | `282` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-229` | `283` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-230` | `284` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-231` | `286` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-233` | `026` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-235` | `033` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-236` | `036` | Update Policy | `DR-SU3` | 切分型（統攝／重複表述） | 1 |
| `newR1L-SU-237` | `126` | Configurable Parameters | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-238` | `128` | Configurable Parameters | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-239` | `138` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-240` | `139` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-245` | `144` | Deployment Flow | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-253` | `152` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 1 |
| `newR1L-SU-255` | `154` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-258` | `157` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 5 |
| `newR1L-SU-259` | `160` | Deployment Flow | `DR-SU2,DR-SU6` | 判準型（能力／全稱） | 4 |
| `newR1L-SU-261` | `162` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-262` | `163` | Deployment Flow | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-264` | `167` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 5 |
| `newR1L-SU-265` | `215` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-266` | `216` | HU FOTA via TBM | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-267` | `217` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-271` | `221` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-272` | `222` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-275` | `225` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-276` | `226` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-277` | `227` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-278` | `228` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-279` | `229` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-280` | `230` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-282` | `232` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-283` | `233` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-284` | `234` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-285` | `235` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-287` | `237` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-288` | `238` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-290` | `240` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-291` | `241` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-292` | `242` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-293` | `243` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-294` | `244` | HU FOTA via TBM | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-295` | `245` | HU FOTA via TBM | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-297` | `247` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-298` | `248` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-299` | `249` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-300` | `250` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-301` | `292` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-302` | `293` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-303` | `294` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-304` | `295` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-305` | `297` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-306` | `298` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-307` | `299` | Bearer Selection | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-308` | `300` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-309` | `301` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-310` | `302` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-311` | `303` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-312` | `304` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-313` | `305` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 4 |
| `newR1L-SU-314` | `306` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-315` | `307` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-316` | `308` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-317` | `057` | Wi-Fi Download | `DR-SU4` | 中斷處理之判準 | 5 |
