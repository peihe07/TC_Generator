# PENDING 清單 —— 交付說明之附件（Pei 裁定 2026-08-30 §2.1(b)）

> **列序依 `Requirement or Design ID` 升冪**（R-BLM17）；TC ID 隨列指派。
> 全案 **319** 個 TC，其中 **195** 個含 `PENDING`，行數合計 **712**。
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

## 三、逐列（依交付本之列序）

| TC ID | 列 | 037 列 | Test Set | DR | 型別 | `PENDING` 行 |
|---|---:|---|---|---|---|---:|
| `newR1L-SU-003` | 12 | `005` | FOTA Overview | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-006` | 15 | `008` | FOTA Overview | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-009` | 18 | `012` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-011` | 20 | `014` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-012` | 21 | `015` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-015` | 24 | `026` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-017` | 26 | `028` | Update Policy | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-018` | 27 | `030` | Update Policy | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-020` | 29 | `033` | Update Policy | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-023` | 32 | `036` | Update Policy | `DR-SU3` | 切分型（統攝／重複表述） | 1 |
| `newR1L-SU-041` | 50 | `057` | Wi-Fi Download | `DR-SU4` | 中斷處理之判準 | 5 |
| `newR1L-SU-045` | 54 | `062` | Wi-Fi Download | `DR-SU2` | 第三型（區辨手段） | 5 |
| `newR1L-SU-046` | 55 | `063` | Wi-Fi Download | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-050` | 59 | `067` | Wi-Fi Download | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-057` | 66 | `083` | USB Update | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-058` | 67 | `084` | USB Update | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-063` | 72 | `093` | ROV Installation | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-064` | 73 | `094` | ROV Installation | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-080` | 89 | `111` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 4 |
| `newR1L-SU-083` | 92 | `114` | TBM Reflash | `DR-SU2` | 第二型（觀測手段） | 1 |
| `newR1L-SU-089` | 98 | `118` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-091` | 100 | `120` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-093` | 102 | `122` | TBM Reflash | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-095` | 104 | `124` | TBM Reflash | `DR-SU2` | 第三型（區辨手段） | 3 |
| `newR1L-SU-096` | 105 | `126` | Configurable Parameters | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-097` | 106 | `128` | Configurable Parameters | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-101` | 110 | `131` | Update HMI | `DR-SU5` | 第二型（觀測手段） | 3 |
| `newR1L-SU-108` | 117 | `138` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-109` | 118 | `139` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-114` | 123 | `144` | Deployment Flow | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-122` | 131 | `152` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 1 |
| `newR1L-SU-124` | 133 | `154` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-127` | 136 | `157` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 5 |
| `newR1L-SU-128` | 137 | `160` | Deployment Flow | `DR-SU2,DR-SU6` | 判準型（能力／全稱） | 4 |
| `newR1L-SU-130` | 139 | `162` | Deployment Flow | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-131` | 140 | `163` | Deployment Flow | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-133` | 142 | `167` | Deployment Flow | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 5 |
| `newR1L-SU-134` | 143 | `169` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-135` | 144 | `171` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-136` | 145 | `172` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-137` | 146 | `173` | Integrity Verification | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-138` | 147 | `174` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-139` | 148 | `175` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 1 |
| `newR1L-SU-140` | 149 | `176` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 1 |
| `newR1L-SU-141` | 150 | `176` | Silent Update | `DR-SU1` | 第二型（觀測手段） | 3 |
| `newR1L-SU-143` | 152 | `179` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-145` | 154 | `181` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 2 |
| `newR1L-SU-148` | 157 | `184` | Silent Update | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-149` | 158 | `187` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-152` | 161 | `191` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-153` | 162 | `195` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-154` | 163 | `198` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-155` | 164 | `199` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-156` | 165 | `201` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-158` | 167 | `205` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-159` | 168 | `206` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-160` | 169 | `207` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-161` | 170 | `208` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-162` | 171 | `209` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-163` | 172 | `210` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-164` | 173 | `211` | Client Architecture | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-165` | 174 | `212` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-167` | 176 | `215` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-168` | 177 | `216` | HU FOTA via TBM | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-169` | 178 | `217` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-173` | 182 | `221` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-174` | 183 | `222` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-177` | 186 | `225` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-178` | 187 | `226` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-179` | 188 | `227` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-180` | 189 | `228` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-181` | 190 | `229` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-182` | 191 | `230` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-184` | 193 | `232` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-185` | 194 | `233` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-186` | 195 | `234` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-187` | 196 | `235` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-189` | 198 | `237` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-190` | 199 | `238` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-192` | 201 | `240` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-193` | 202 | `241` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-194` | 203 | `242` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-195` | 204 | `243` | HU FOTA via TBM | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-196` | 205 | `244` | HU FOTA via TBM | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-197` | 206 | `245` | HU FOTA via TBM | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-199` | 208 | `247` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-200` | 209 | `248` | HU FOTA via TBM | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-201` | 210 | `249` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-202` | 211 | `250` | HU FOTA via TBM | `DR-SU2` | 第四型（觸發手段） | 5 |
| `newR1L-SU-203` | 212 | `252` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-204` | 213 | `253` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-205` | 214 | `254` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-206` | 215 | `255` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-207` | 216 | `256` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-208` | 217 | `257` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-209` | 218 | `258` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-210` | 219 | `260` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-211` | 220 | `261` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-212` | 221 | `262` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-213` | 222 | `264` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-214` | 223 | `265` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-215` | 224 | `267` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-216` | 225 | `268` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-217` | 226 | `269` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-218` | 227 | `270` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-219` | 228 | `272` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-220` | 229 | `273` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-221` | 230 | `274` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-222` | 231 | `275` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-223` | 232 | `276` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-224` | 233 | `277` | Session Flows | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-225` | 234 | `279` | Session Flows | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-226` | 235 | `281` | Client Architecture | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-227` | 236 | `282` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-228` | 237 | `283` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-229` | 238 | `284` | Client Architecture | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-230` | 239 | `286` | Client Architecture | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-231` | 240 | `288` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-232` | 241 | `289` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-233` | 242 | `290` | Session Flows | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-234` | 243 | `292` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-235` | 244 | `293` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-236` | 245 | `294` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-237` | 246 | `295` | Bearer Selection | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-238` | 247 | `297` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-239` | 248 | `298` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-240` | 249 | `299` | Bearer Selection | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-241` | 250 | `300` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-242` | 251 | `301` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-243` | 252 | `302` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-244` | 253 | `303` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-245` | 254 | `304` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-246` | 255 | `305` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 4 |
| `newR1L-SU-247` | 256 | `306` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-248` | 257 | `307` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-249` | 258 | `308` | Bearer Selection | `DR-SU7` | 安全與認證之觀測 | 3 |
| `newR1L-SU-250` | 259 | `310` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-251` | 260 | `311` | Integrity Verification | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-252` | 261 | `312` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-253` | 262 | `313` | Interruption Handling | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-254` | 263 | `315` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 5 |
| `newR1L-SU-255` | 264 | `316` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-256` | 265 | `317` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-257` | 266 | `318` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 5 |
| `newR1L-SU-258` | 267 | `319` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-259` | 268 | `320` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 2 |
| `newR1L-SU-260` | 269 | `321` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-261` | 270 | `322` | Interruption Handling | `DR-SU2` | 車外表徵（伺服器側） | 1 |
| `newR1L-SU-262` | 271 | `323` | Interruption Handling | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-263` | 272 | `324` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-264` | 273 | `325` | Interruption Handling | `DR-SU2,DR-SU4` | 中斷處理之判準 | 4 |
| `newR1L-SU-265` | 274 | `326` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-266` | 275 | `327` | Interruption Handling | `DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-268` | 277 | `329` | Interruption Handling | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-269` | 278 | `330` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 5 |
| `newR1L-SU-270` | 279 | `331` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-271` | 280 | `332` | Status Reporting | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 3 |
| `newR1L-SU-272` | 281 | `333` | Status Reporting | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-273` | 282 | `334` | Status Reporting | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-276` | 285 | `338` | Integrity Verification | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-277` | 286 | `339` | Status Reporting | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-280` | 289 | `343` | Deployment Conditions | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-284` | 293 | `347` | Session Management | `DR-SU2` | 車外表徵（伺服器側） | 3 |
| `newR1L-SU-285` | 294 | `348` | Session Management | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-286` | 295 | `349` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-287` | 296 | `350` | Session Management | `DR-SU2` | 第二型（觀測手段） | 5 |
| `newR1L-SU-288` | 297 | `351` | Session Management | `DR-SU2` | 第四型（觸發手段） | 4 |
| `newR1L-SU-289` | 298 | `352` | Session Management | `DR-SU2` | 車外表徵（伺服器側） | 6 |
| `newR1L-SU-290` | 299 | `353` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-292` | 301 | `355` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-293` | 302 | `356` | Session Management | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-294` | 303 | `357` | Interruption Handling | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-295` | 304 | `358` | Status Reporting | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-297` | 306 | `360` | Interruption Handling | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 4 |
| `newR1L-SU-298` | 307 | `361` | Session Management | `DR-SU2` | 第四型（觸發手段） | 3 |
| `newR1L-SU-299` | 308 | `363` | Telematics Client | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-300` | 309 | `364` | Telematics Client | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-301` | 310 | `365` | Telematics Client | `DR-SU2,DR-SU3` | 切分型（統攝／重複表述） | 6 |
| `newR1L-SU-302` | 311 | `366` | Telematics Client | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-303` | 312 | `367` | Telematics Client | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-304` | 313 | `368` | Session Management | `DR-SU2` | 第二型（觀測手段） | 6 |
| `newR1L-SU-305` | 314 | `369` | Session Management | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-306` | 315 | `370` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-307` | 316 | `371` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-308` | 317 | `372` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-309` | 318 | `373` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-310` | 319 | `374` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
| `newR1L-SU-311` | 320 | `375` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 4 |
| `newR1L-SU-312` | 321 | `376` | Update Agent | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-313` | 322 | `377` | Update Agent | `DR-SU2` | 第四型（觸發手段） | 6 |
| `newR1L-SU-314` | 323 | `378` | Update Agent | `DR-SU4` | 中斷處理之判準 | 3 |
| `newR1L-SU-315` | 324 | `379` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-317` | 326 | `381` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 4 |
| `newR1L-SU-318` | 327 | `382` | Update Agent | `DR-SU6` | 判準型（能力／全稱） | 3 |
| `newR1L-SU-319` | 328 | `383` | Update Agent | `DR-SU2` | 第二型（觀測手段） | 3 |
