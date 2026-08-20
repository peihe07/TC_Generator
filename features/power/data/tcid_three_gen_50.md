# B2 —— 三代 `tc_id` 對照表（R-P324）

> **⚠ 提案版，已由重建版取代（R-P329 / 54 包）** —— 其第三代號為 001–280，
> 而 51 包補齊 15 個錨點、54 包補測 3 條後，最終號為 **001–283**。
> 現行版見 [`tcid_three_gen_54.md`](tcid_three_gen_54.md)。
> **依 R-P329 保留不刪** —— 其第三代號未落於任何交付物，故不構成一代。

> 鍵：`(req_id, tc_title)`。產生指令：`python features/power/scripts/tcid_three_gen_50.py`

## 一、三代之量

| 代 | 涵蓋 | 號段 |
|---|---|---|
| （一）歷史臨時號 | 3 個時點 | 見第三節 |
| （二）現行交付副本最終號 | **260** 條 | 001–260 |
| （三）本次新最終號 | **280** 條 | 001–280 |

## 二、（二）→（三）之位移 —— **作廢之核心資訊**

**260 / 260 條之最終號改變**（100.0%）。

第七批新增 **20** 條（（二）無對應）。

**⚠ 若已有人引用（二）之號碼，該號碼於（三）指向另一條 TC** —— 須憑本表逐一換算，不得逕以號碼相認。

## ⚠ A-PW299 之 2 條鍵斷裂 —— **已人工補齊**

| req_id | 歷史標題 | 現行標題 |
|---|---|---|
| `SWE-PM-091` | The day theme mode keeps the Day theme regardless of the | The day theme mode uses the Day theme |
| `SWE-PM-092` | The night theme mode keeps the Night theme regardless of | The night theme mode uses the Night theme |

補齊後**歷史階段之涵蓋為 266 / 266**（前為 264 / 266）。

## 三、逐條三代對照

| req_id | 27 包重編前 | 27 包重編後 | 44 包合併前 | 現行臨時 | **（二）交付副本** | **（三）新最終** | `tc_title` |
|---|---|---|---|---|---|---|---|
| `SWE-PM-001` | **—** | **—** | **—** | `261` | **新增** | **`001`** | Full-Operation keeps the TLM ON with all functionali |
| `SWE-PM-001` | **—** | **—** | **—** | `262` | **新增** | **`002`** | Full-Operation holds in each listed ignition working |
| `SWE-PM-002` | **—** | **—** | **—** | `263` | **新增** | **`003`** | Idle mutes the audio and allows only the Splash Scre |
| `SWE-PM-002` | **—** | **—** | **—** | `264` | **新增** | **`004`** | Idle keeps ICS available and DTV off |
| `SWE-PM-002` | **—** | **—** | **—** | `265` | **新增** | **`005`** | Idle provides the rear view camera images when neede |
| `SWE-PM-002` | **—** | **—** | **—** | `266` | **新增** | **`006`** | Idle disables settings and all HMI interaction excep |
| `SWE-PM-003` | **—** | **—** | **—** | `267` | **新增** | **`007`** | Remote Start Active reports Partial_Operation with A |
| `SWE-PM-003` | **—** | **—** | **—** | `268` | **新增** | **`008`** | Partial Operation keeps ANC, ACN and chimes audio ac |
| `SWE-PM-003` | **—** | **—** | **—** | `269` | **新增** | **`009`** | Partial Operation enables only the interaction that  |
| `SWE-PM-003` | **—** | **—** | **—** | `270` | **新增** | **`010`** | The HU does not enter stolen vehicle mode under any  |
| `SWE-PM-004` | **—** | **—** | **—** | `271` | **新增** | **`011`** | Timed keeps the TLM on with all functionalities avai |
| `SWE-PM-004` | **—** | **—** | **—** | `272` | **新增** | **`012`** | Timed mode disables the Customer setting screens |
| `SWE-PM-005` | **—** | **—** | **—** | `273` | **新增** | **`013`** | Standby turns the TLM off while the network stays on |
| `SWE-PM-005` | **—** | **—** | **—** | `274` | **新增** | **`014`** | Entering Standby clears the antitheft activation req |
| `SWE-PM-006` | **—** | **—** | **—** | `275` | **新增** | **`015`** | Sleep turns the TLM off with the network off as well |
| `SWE-PM-006` | **—** | **—** | **—** | `276` | **新增** | **`016`** | Entering Sleep clears the antitheft activation reque |
| `SWE-PM-007` | **—** | **—** | **—** | `277` | **新增** | **`017`** | Bench turns the AMP, ICS and DTV on for the Engineer |
| `SWE-PM-009` | **—** | **—** | **—** | `278` | **新增** | **`018`** | The ex-factory defaults are applied on the first pow |
| `SWE-PM-009` | **—** | **—** | **—** | `279` | **新增** | **`019`** | A battery disconnection puts the TLM into the INIT s |
| `SWE-PM-009` | **—** | **—** | **—** | `280` | **新增** | **`020`** | Leaving INIT restores the last settings and starts f |
| `SWE-PM-011` | `044` | `044` | `044` | `043` | `001` | **`021`** | VR button press in IDLE mode transitions the HU to F |
| `SWE-PM-011` | `045` | `045` | `045` | `044` | `002` | **`022`** | CarPlay requesting audio and video keeps audio unmut |
| `SWE-PM-011` | `046` | `046` | `046` | `045` | `003` | **`023`** | CarPlay requesting audio only activates the Screen O |
| `SWE-PM-011` | `047` | `047` | `047` | `046` | `004` | **`024`** | CarPlay requesting video only mutes the audio and ke |
| `SWE-PM-011` | `048` | `048` | `048` | `047` | `005` | **`025`** | CarPlay requesting neither audio nor video returns t |
| `SWE-PM-011` | `049` | `049` | `049` | `048` | `006` | **`026`** | VR button long press in IDLE mode transitions the HU |
| `SWE-PM-012` | `050` | `050` | `050` | `049` | `007` | **`027`** | User settings are restored after a battery reconnect |
| `SWE-PM-012` | `051` | `051` | `051` | `050` | `008` | **`028`** | TLM starts from Sleep state after leaving INIT |
| `SWE-PM-013` | `052` | `052` | `052` | `051` | `009` | **`029`** | Remote Start Active reports Partial_Operation |
| `SWE-PM-013` | **—** | `053` | `053` | `052` | `010` | **`030`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-013` | **—** | `054` | `054` | `053` | `011` | **`031`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-013` | **—** | `055` | `055` | `054` | `012` | **`032`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-013` | `053` | `056` | `056` | `055` | `013` | **`033`** | AMP, ICS and DTV are off while chime audio stays act |
| `SWE-PM-013` | `054` | `057` | `057` | `056` | `014` | **`034`** | HMI interaction is disabled except for status change |
| `SWE-PM-014` | `055` | `058` | `058` | `057` | `015` | **`035`** | Remote Start ends at ignition off: RemStartFail is s |
| `SWE-PM-014` | `056` | `059` | `059` | `058` | `016` | **`036`** | RemStartFail is cleared when the call is not active |
| `SWE-PM-014` | `057` | `060` | `060` | `059` | `017` | **`037`** | Behaviour 1 with no active call passes the TLM to St |
| `SWE-PM-014` | `058` | `061` | `061` | `060` | `018` | **`038`** | Behaviour 1 with an active call passes the TLM to Ti |
| `SWE-PM-014` | `059` | `062` | `062` | `061` | `019` | **`039`** | Behaviour 2 on a Jeep with the driver door open pass |
| `SWE-PM-014` | `060` | `063` | `063` | `062` | `020` | **`040`** | Behaviour 2 otherwise passes to Timed keeping the ac |
| `SWE-PM-014` | `061` | `064` | `064` | `063` | `021` | **`041`** | Behaviour 1 reached through Auto_SwitchOn_Setting.Re |
| `SWE-PM-014` | `062` | `065` | `065` | `064` | `022` | **`042`** | Behaviour 2 reached through Auto_SwitchOn_Setting.Re |
| `SWE-PM-014` | `063` | `066` | `066` | `065` | `023` | **`043`** | Remote Start ends at ignition pre off: RemStartFail  |
| `SWE-PM-015` | `064` | `067` | `067` | `066` | `024` | **`044`** | Front_Panel_OnOff.Req press with no active call pass |
| `SWE-PM-015` | `065` | `068` | `068` | `067` | `025` | **`045`** | CLIMATIC_PANEL.Radio_Btn0 press with no active call  |
| `SWE-PM-015` | `066` | `069` | `069` | `068` | `026` | **`046`** | Front_Panel_OnOff.Req press with the rear camera not |
| `SWE-PM-015` | `067` | `070` | `070` | `069` | `027` | **`047`** | CLIMATIC_PANEL.Radio_Btn0 press with the rear camera |
| `SWE-PM-016` | `068` | `071` | `071` | `070` | `028` | **`048`** | Rear camera activation keeps the TLM in Full-Operati |
| `SWE-PM-017` | `069` | `072` | `072` | `071` | `029` | **`049`** | Rear camera deactivation restores the last active so |
| `SWE-PM-018` | `070` | `073` | `073` | `072` | `030` | **`050`** | Ignition off in Idle passes the TLM to Standby |
| `SWE-PM-018` | `071` | `074` | `074` | `073` | `031` | **`051`** | Ignition pre off in Idle passes the TLM to Standby |
| `SWE-PM-019` | `072` | `075` | `075` | `074` | `032` | **`052`** | Front_Panel_OnOff.Req press is ignored while the rea |
| `SWE-PM-019` | `073` | `076` | `076` | `075` | `033` | **`053`** | Front_Panel_OnOff.Req press otherwise shows the Spla |
| `SWE-PM-019` | `074` | `077` | `077` | `076` | `034` | **`054`** | CLIMATIC_PANEL.Radio_Btn0 press is ignored while the |
| `SWE-PM-019` | `075` | `078` | `078` | `077` | `035` | **`055`** | CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the  |
| `SWE-PM-020` | `076` | `079` | `079` | `078` | `036` | **`056`** | Incoming call in Idle passes the TLM to Full-Operati |
| `SWE-PM-020` | `077` | `080` | `080` | `079` | `037` | **`057`** | Call ending on the Phone Main Screen returns the TLM |
| `SWE-PM-020` | `078` | `081` | `081` | `080` | `038` | **`058`** | Call ending on another screen keeps the TLM in Full- |
| `SWE-PM-021` | `079` | `082` | `082` | `081` | `039` | **`059`** | Rear camera enable in Idle keeps Idle with video onl |
| `SWE-PM-022` | `080` | `083` | `083` | `082` | `040` | **`060`** | Logistic mode on passes the TLM to Logistic Idle |
| `SWE-PM-023` | `081` | `084` | `084` | `083` | `041` | **`061`** | Leaving Ignition Off in Timed passes the TLM to Full |
| `SWE-PM-024` | `082` | `085` | `085` | `084` | `042` | **`062`** | Remote Start not active on leaving Ignition Off clea |
| `SWE-PM-025` | `083` | `086` | `086` | `085` | `043` | **`063`** | Front_Panel_OnOff.Req press in Timed with an active  |
| `SWE-PM-025` | `084` | `087` | `087` | `086` | `044` | **`064`** | Accepting the Front_Panel_OnOff.Req popup passes the |
| `SWE-PM-025` | `085` | `088` | `088` | `087` | `045` | **`065`** | Declining the Front_Panel_OnOff.Req popup keeps the  |
| `SWE-PM-025` | `086` | `089` | `089` | `088` | `046` | **`066`** | Front_Panel_OnOff.Req press in Timed with no active  |
| `SWE-PM-025` | `087` | `090` | `090` | `089` | `047` | **`067`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with an act |
| `SWE-PM-025` | `088` | `091` | `091` | `090` | `048` | **`068`** | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes |
| `SWE-PM-025` | `089` | `092` | `092` | `091` | `049` | **`069`** | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps  |
| `SWE-PM-025` | `090` | `093` | `093` | `092` | `050` | **`070`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with no act |
| `SWE-PM-026` | `091` | `094` | `094` | `093` | `051` | **`071`** | Door open on a Jeep from Full-Operation passes the T |
| `SWE-PM-026` | `092` | `095` | `095` | `094` | `052` | **`072`** | Door open with an active call keeps the TLM in Timed |
| `SWE-PM-026` | `093` | `096` | `096` | `095` | `053` | **`073`** | Door open with Standby as the previous state keeps t |
| `SWE-PM-026` | **—** | `097` | `097` | `096` | `054` | **`074`** | A non Jeep brand does not take the door transition t |
| `SWE-PM-027` | `094` | `098` | `098` | `097` | `055` | **`075`** | Antitheft failure clears the activation request with |
| `SWE-PM-027` | `095` | `099` | `099` | `098` | `056` | **`076`** | Antitheft failure in Partial Operation keeps the ori |
| `SWE-PM-028` | `096` | `100` | `100` | `099` | `057` | **`077`** | Antitheft success clears the activation request |
| `SWE-PM-028` | `097` | `101` | `101` | `100` | `058` | **`078`** | Antitheft success with a zero timeout takes Timeout1 |
| `SWE-PM-028` | `099` | `103` | `103` | `101` | `059` | **`079`** | Antitheft success on LTM High takes Timeout1 from PR |
| `SWE-PM-029` | `100` | `104` | `104` | `102` | `060` | **`080`** | Antitheft success clears the activation request on t |
| `SWE-PM-029` | `101` | `105` | `105` | `103` | `061` | **`081`** | Timeout1 follows Switch_Off_Time when the setting is |
| `SWE-PM-029` | `102` | `106` | `106` | `104` | `062` | **`082`** | Timeout1 follows PwrAccDelayAct when the setting is  |
| `SWE-PM-030` | `104` | `108` | `108` | `105` | `063` | **`083`** | Splash Screen is shown for the configured wait time |
| `SWE-PM-030` | `105` | `109` | `109` | `106` | `064` | **`084`** | Splash Screen is shown for the Recall_Last branch |
| `SWE-PM-031` | `106` | `110` | `110` | `107` | `065` | **`085`** | Rear view camera images follow the enable signal in  |
| `SWE-PM-032` | `107` | `111` | `111` | `108` | `066` | **`086`** | Remote Start from Standby passes the TLM to Partial  |
| `SWE-PM-033` | `108` | `112` | `112` | `109` | `067` | **`087`** | Ignition Pre Off from Partial Operation passes the T |
| `SWE-PM-033` | `109` | `113` | `113` | `110` | `068` | **`088`** | Ignition Off from Partial Operation passes the TLM t |
| `SWE-PM-034` | `110` | `114` | `114` | `111` | `069` | **`089`** | Front panel press in Partial Operation arms the anti |
| `SWE-PM-035` | `111` | `115` | `115` | `112` | `070` | **`090`** | Antitheft success with auto switch on active passes  |
| `SWE-PM-035` | `112` | `116` | `116` | `113` | `071` | **`091`** | Antitheft success with auto switch on not active pas |
| `SWE-PM-035` | `113` | `117` | `117` | `114` | `072` | **`092`** | Antitheft success with recall last and last status o |
| `SWE-PM-035` | `114` | `118` | `118` | `115` | `073` | **`093`** | Antitheft success with recall last and last status o |
| `SWE-PM-036` | `115` | `119` | `119` | `116` | `074` | **`094`** | Remote start from Timed passes the TLM to Partial Op |
| `SWE-PM-037` | `116` | `120` | `120` | `117` | `075` | **`095`** | Call end in Timed with a failed remote start passes  |
| `SWE-PM-038` | `033` | `033` | `033` | `032` | `076` | **`096`** | Case 1 with RemStartFail true: TLM stops and passes  |
| `SWE-PM-038` | `034` | `034` | `034` | `033` | `077` | **`097`** | Case 1 with RemStartFail false: previous source is r |
| `SWE-PM-038` | `035` | `035` | `035` | `034` | `078` | **`098`** | Case 2: MaxCallTimeout starts at Timeout1 expiry and |
| `SWE-PM-038` | `036` | `036` | `036` | `035` | `079` | **`099`** | Case 2 exit on call end: TLM_Status.Info passes to S |
| `SWE-PM-038` | `037` | `037` | `037` | `036` | `080` | **`100`** | Case 2 exit with RemStartFail cleared on MaxCallTime |
| `SWE-PM-038` | `038` | `038` | `038` | `037` | `081` | **`101`** | Case 3: call already ended at Timeout1 expiry |
| `SWE-PM-038` | `039` | `039` | `039` | `038` | `082` | **`102`** | Case 3 with RemStartFail cleared at Timeout1 expiry |
| `SWE-PM-038` | `040` | `040` | `040` | `039` | `083` | **`103`** | Case 4: ignition off with Timeout1 at 00 min enters  |
| `SWE-PM-038` | `041` | `041` | `041` | `040` | `084` | **`104`** | Case 4 exit: TLM passes to Standby when the call end |
| `SWE-PM-038` | `042` | `042` | `042` | `041` | `085` | **`105`** | Case 4 exit with RemStartFail cleared on MaxCallTime |
| `SWE-PM-038` | `043` | `043` | `043` | `042` | `086` | **`106`** | Case 4 with ignition pre off: TLM enters Timed state |
| `SWE-PM-039` | `117` | `121` | `121` | `118` | `087` | **`107`** | An SNA operational mode is handled as an ignition of |
| `SWE-PM-039` | `118` | `122` | `122` | `119` | `088` | **`108`** | A zero switch off timeout loads Timeout1 from the PR |
| `SWE-PM-039` | `119` | `123` | `123` | `120` | `089` | **`109`** | Auto switch on active on LTM High Radio loads Timeou |
| `SWE-PM-039` | `120` | `124` | `124` | `121` | `090` | **`110`** | Only TLM menu items are guaranteed in the Timed stat |
| `SWE-PM-040` | `121` | `125` | `125` | `122` | `091` | **`111`** | A normal power down into Suspend to RAM starts the 8 |
| `SWE-PM-041` | `122` | `126` | `126` | `123` | `092` | **`112`** | No TLM function is available in the TLM off with net |
| `SWE-PM-041` | `123` | `127` | `127` | `124` | `093` | **`113`** | Entering the TLM off with network on status clears t |
| `SWE-PM-042` | `124` | `128` | `128` | `125` | `094` | **`114`** | No TLM function is available in the TLM off with net |
| `SWE-PM-042` | `125` | `129` | `129` | `126` | `095` | **`115`** | Entering the TLM off with network off status clears  |
| `SWE-PM-043` | `126` | `130` | `130` | `127` | `096` | **`116`** | The backlight stays off during Standby mode |
| `SWE-PM-043` | `127` | `131` | `131` | `128` | `097` | **`117`** | The backlight is allowed during Standby when an HMI  |
| `SWE-PM-044` | `128` | `132` | `132` | `129` | `098` | **`118`** | Front panel press in Standby arms the antitheft and  |
| `SWE-PM-044` | `129` | `133` | `133` | `130` | `099` | **`119`** | Front panel press in Sleep arms the antitheft and sh |
| `SWE-PM-044` | `130` | `134` | `134` | `131` | `100` | **`120`** | Climatic panel press in Standby arms the antitheft a |
| `SWE-PM-044` | `131` | `135` | `135` | `132` | `101` | **`121`** | Climatic panel press in Sleep arms the antitheft and |
| `SWE-PM-045` | `132` | `136` | `136` | `133` | `102` | **`122`** | A failed antitheft keeps the TLM in the original Sta |
| `SWE-PM-045` | `133` | `137` | `137` | `134` | `103` | **`123`** | A failed antitheft keeps the TLM in the original Sle |
| `SWE-PM-046` | `134` | `138` | `138` | `135` | `104` | **`124`** | Rear view camera is provided while the antitheft is  |
| `SWE-PM-046` | `135` | `139` | `139` | `136` | `105` | **`125`** | Rear view camera is provided after an unsuccessful a |
| `SWE-PM-047` | `136` | `140` | `140` | `137` | `106` | **`126`** | A failed antitheft keeps the TLM in Standby and show |
| `SWE-PM-047` | `137` | `141` | `141` | `138` | `107` | **`127`** | A failed antitheft keeps the TLM in Sleep and shows  |
| `SWE-PM-048` | `138` | `142` | `142` | `139` | `108` | **`128`** | Antitheft success with auto switch on active reaches |
| `SWE-PM-048` | `139` | `143` | `143` | `140` | `109` | **`129`** | Antitheft success with auto switch on not active rea |
| `SWE-PM-048` | `140` | `144` | `144` | `141` | `110` | **`130`** | Recall last with last status on reaches Full-Operati |
| `SWE-PM-048` | `141` | `145` | `145` | `142` | `111` | **`131`** | Recall last with last status off reaches Idle after  |
| `SWE-PM-048` | `142` | `146` | `146` | `143` | `112` | **`132`** | The ex-factory default selects recall last with the  |
| `SWE-PM-049` | `143` | `147` | `147` | `144` | `113` | **`133`** | A failed antitheft keeps the TLM blocked in Idle |
| `SWE-PM-050` | `144` | `148` | `148` | `145` | `114` | **`134`** | The else branch stores the last status off and passe |
| `SWE-PM-051` | `145` | `149` | `149` | `146` | `115` | **`135`** | Antitheft success stores the last status on and pass |
| `SWE-PM-052` | `146` | `150` | `150` | `147` | `116` | **`136`** | A failed antitheft keeps the TLM in the original Par |
| `SWE-PM-053` | `147` | `151` | `151` | `148` | `117` | **`137`** | The vehicle brand logo screen follows the brand conf |
| `SWE-PM-054` | `148` | `152` | `152` | `149` | `118` | **`138`** | No audio brand without SDARS shows the vehicle brand |
| `SWE-PM-054` | `149` | `153` | `153` | `150` | `119` | **`139`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-054` | `150` | `154` | `154` | `151` | `120` | **`140`** | SDARS present without audio brand adds the Sirius lo |
| `SWE-PM-054` | `151` | `155` | `155` | `152` | `121` | **`141`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-055` | `152` | `156` | `156` | `153` | `122` | **`142`** | The special package drives the Klipsch Splash Screen |
| `SWE-PM-055` | `153` | `157` | `157` | `154` | `123` | **`143`** | The splash screen type drives the Klipsch Splash Scr |
| `SWE-PM-056` | `154` | `158` | `158` | `155` | `124` | **`144`** | The Fiat Latam startup animation replaces the vehicl |
| `SWE-PM-057` | `018` | `018` | `018` | `017` | `125` | **`145`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-057` | `019` | `019` | `019` | `018` | `126` | **`146`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-057` | `020` | `020` | `020` | `019` | `127` | **`147`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-058` | `155` | `159` | `159` | `156` | `128` | **`148`** | The ex-factory default sets a zero switch off timeou |
| `SWE-PM-059` | `156` | `160` | `160` | `157` | `129` | **`149`** | A network sleep request in Standby passes the TLM to |
| `SWE-PM-059` | `157` | `161` | `161` | `158` | `130` | **`150`** | A network sleep request during boot is served only a |
| `SWE-PM-060` | `021` | `021` | `021` | `020` | `131` | **`151`** | LTM or ETM Radio offers one timeout parameter |
| `SWE-PM-060` | `022` | `022` | `022` | `021` | `132` | **`152`** | Radio other than LTM or ETM offers two timeout param |
| `SWE-PM-061` | `023` | `023` | `023` | `022` | `133` | **`153`** | Timeout settings are selectable in Full-Operation st |
| `SWE-PM-061` | `024` | `024` | `024` | `023` | `134` | **`154`** | Timeout settings are not selectable outside Full-Ope |
| `SWE-PM-062` | `025` | `025` | `025` | `024` | `135` | **`155`** | Auto_SwitchOn_Setting.Req can be set to Active |
| `SWE-PM-062` | `026` | `026` | `026` | `025` | `136` | **`156`** | Auto_SwitchOn_Setting.Req can be set to Not_Active |
| `SWE-PM-062` | `027` | `027` | `027` | `026` | `137` | **`157`** | Auto_SwitchOn_Setting.Req can be set to Recall_Last |
| `SWE-PM-063` | `028` | `028` | `028` | `027` | `138` | **`158`** | Bluetooth calls can be made and received in Timed st |
| `SWE-PM-064` | `029` | `029` | `029` | `028` | `139` | **`159`** | MaxCallTimeout starts on ignition off with Timeout1  |
| `SWE-PM-064` | `030` | `030` | `030` | `029` | `140` | **`160`** | MaxCallTimeout starts at Timeout1 expiry with the ca |
| `SWE-PM-065` | `031` | `031` | `031` | `030` | `141` | **`161`** | Call ends before Timeout1 expiry: previous source is |
| `SWE-PM-065` | `032` | `032` | `032` | `031` | `142` | **`162`** | Further calls are still managed within Timeout1 |
| `SWE-PM-066` | `158` | `162` | `162` | `159` | `143` | **`163`** | An SOS call is treated as a phone call becoming acti |
| `SWE-PM-066` | `159` | `163` | `163` | `160` | `144` | **`164`** | An Assist call is treated as a phone call becoming a |
| `SWE-PM-067` | `160` | `164` | `164` | `161` | `145` | **`165`** | A projection device call is treated as a phone call  |
| `SWE-PM-068` | `161` | `165` | `165` | `162` | `146` | **`166`** | An incoming call from IDLE bypasses the disclaimer s |
| `SWE-PM-069` | `162` | `166` | `166` | `163` | `147` | **`167`** | The HU returns to IDLE when the call ends on the pho |
| `SWE-PM-069` | `163` | `167` | `167` | `164` | `148` | **`168`** | The HU returns to IDLE when the call ends on the pho |
| `SWE-PM-070` | `164` | `168` | `168` | `165` | `149` | **`169`** | The bypassed disclaimer is shown at the next transit |
| `SWE-PM-071` | `001` | `001` | `001` | `001` | `150` | **`170`** | Splash screen shown after SplashScreen_Time on norma |
| `SWE-PM-071` | `002` | `002` | `002` | `002` | `151` | **`171`** | No splash screen when TLM passes to Standby |
| `SWE-PM-071` | `003` | `003` | `003` | `003` | `152` | **`172`** | No splash screen when TLM passes to Bench |
| `SWE-PM-071` | `004` | `004` | `004` | `004` | `153` | **`173`** | Standard screen shown after StandardScreen_Time |
| `SWE-PM-072` | `005` | `005` | `005` | `005` | `154` | **`174`** | Events during boot are buffered without loss |
| `SWE-PM-073` | `007` | `007` | `007` | `006` | `155` | **`175`** | Load Shed limits volume and mutes TLM |
| `SWE-PM-073` | `008` | `008` | `008` | `007` | `156` | **`176`** | Load Shed signals lost: last values retained |
| `SWE-PM-073` | `009` | `009` | `009` | `008` | `157` | **`177`** | Battery Critical minimizes draw and keeps ACN active |
| `SWE-PM-073` | `010` | `010` | `010` | `009` | `158` | **`178`** | Normal operation resumes 10 seconds after recovery |
| `SWE-PM-073` | `011` | `011` | `011` | `010` | `159` | **`179`** | Load Shed recovers: normal volume and audio restored |
| `SWE-PM-073` | `012` | `012` | `012` | `011` | `160` | **`180`** | Continuing call transferred to head set under Load S |
| `SWE-PM-073` | `013` | `013` | `013` | `012` | `161` | **`181`** | Continuing call transferred to head set under Batter |
| `SWE-PM-073` | `014` | `014` | `014` | `013` | `162` | **`182`** | Battery Critical minimizes draw in BODY OFF-TIMED mo |
| `SWE-PM-073` | `015` | `015` | `015` | `014` | `163` | **`183`** | Battery Critical exits on voltage out of range condi |
| `SWE-PM-073` | `016` | `016` | `016` | `015` | `164` | **`184`** | Load Shed with volume already below the cap: no AUD_ |
| `SWE-PM-073` | `017` | `017` | `017` | `016` | `165` | **`185`** | Battery Critical with volume already below the cap:  |
| `SWE-PM-074` | `165` | `169` | `169` | `166` | `166` | **`186`** | A Radio FOTA update at Body OFF brings the HU to Tim |
| `SWE-PM-074` | `166` | `170` | `170` | `167` | `167` | **`187`** | A TBM FOTA update at Body OFF brings the HU to Timed |
| `SWE-PM-074` | `167` | `171` | `171` | `168` | `168` | **`188`** | A ROV FOTA update at Body OFF brings the HU to Timed |
| `SWE-PM-075` | `168` | `172` | `172` | `169` | `169` | **`189`** | The HU leaves Timed one minute after the FOTA pop-up |
| `SWE-PM-075` | `169` | `173` | `173` | `170` | `170` | **`190`** | The HU leaves Timed when the FOTA pop-up is dismisse |
| `SWE-PM-075` | `170` | `174` | `174` | `171` | `171` | **`191`** | The HU leaves Timed when the accessory delay becomes |
| `SWE-PM-076` | `171` | `175` | `175` | `172` | `172` | **`192`** | A ten second power button press performs a radio res |
| `SWE-PM-076` | `173` | `177` | `177` | `173` | `173` | **`193`** | No power button reset occurs while a firmware image  |
| `SWE-PM-077` | `224` | `231` | `231` | `227` | `174` | **`194`** | The special package value determines the theme used  |
| `SWE-PM-078` | `225` | `232` | `232` | `228` | `175` | **`195`** | A none special package falls back to the brand defau |
| `SWE-PM-078` | `226` | `233` | `233` | `229` | `176` | **`196`** | An unsupported special package falls back to the bra |
| `SWE-PM-079` | `227` | `234` | `234` | `230` | `177` | **`197`** | An unsupported CAN value on a branded element uses t |
| `SWE-PM-080` | `228` | `235` | `235` | `231` | `178` | **`198`** | The theme special package value is sent while the CA |
| `SWE-PM-080` | `229` | `236` | `236` | `232` | `179` | **`199`** | A theme change updates the sent value within the sen |
| `SWE-PM-081` | `230` | `237` | `237` | `233` | `180` | **`200`** | The Chrysler brand selects the Chrysler font |
| `SWE-PM-081` | `231` | `238` | `238` | `234` | `181` | **`201`** | The Jeep brand selects the Jeep font |
| `SWE-PM-081` | `232` | `239` | `239` | `235` | `182` | **`202`** | The Fiat brand selects the default Fiat font |
| `SWE-PM-082` | `233` | `240` | `240` | `236` | `183` | **`203`** | The Chrysler brand selects the Chrysler App icon |
| `SWE-PM-082` | `234` | `241` | `241` | `237` | `184` | **`204`** | The Jeep brand selects the Jeep App icon |
| `SWE-PM-082` | `235` | `242` | `242` | `238` | `185` | **`205`** | The Fiat brand selects the default Fiat App icon |
| `SWE-PM-083` | `236` | `243` | `243` | `239` | `186` | **`206`** | The Jeep brand offers the Jeep avatars in the profil |
| `SWE-PM-083` | `237` | `244` | `244` | `240` | `187` | **`207`** | The Fiat brand offers the default Fiat avatars |
| `SWE-PM-083` | `238` | `245` | `245` | `241` | `188` | **`208`** | The Abarth brand is mapped to the Fiat avatars |
| `SWE-PM-084` | `239` | `246` | `246` | `242` | `189` | **`209`** | The recirc icon follows the PROXI parameters on the  |
| `SWE-PM-084` | `240` | `247` | `247` | `243` | `190` | **`210`** | The recirc icon follows the body style signal on the |
| `SWE-PM-085` | `241` | `248` | `248` | `244` | `191` | **`211`** | The settings seat graphic follows the PROXI paramete |
| `SWE-PM-085` | `242` | `249` | `249` | `245` | `192` | **`212`** | The settings seat graphic follows the body style sig |
| `SWE-PM-086` | `243` | `250` | `250` | `246` | `193` | **`213`** | The theme special package value is sent on this chap |
| `SWE-PM-086` | `244` | `251` | `251` | `247` | `194` | **`214`** | A theme change on this chapter updates the sent valu |
| `SWE-PM-087` | `245` | `252` | `252` | `248` | `195` | **`215`** | The M240 vehicle line uses the M240 seat graphics |
| `SWE-PM-087` | `246` | `253` | `253` | `249` | `196` | **`216`** | A non M240 vehicle line falls back to the brand seat |
| `SWE-PM-088` | `247` | `254` | `254` | `250` | `197` | **`217`** | The performance gauges follow the vehicle line signa |
| `SWE-PM-090` | `248` | `255` | `255` | `251` | `198` | **`218`** | The auto theme mode follows the day night signal int |
| `SWE-PM-090` | `249` | `256` | `256` | `252` | `199` | **`219`** | The auto theme mode follows the day night signal int |
| `SWE-PM-091` | `250` | `257` | `257` | `253` | `200` | **`220`** | The day theme mode uses the Day theme |
| `SWE-PM-092` | `251` | `258` | `258` | `254` | `201` | **`221`** | The night theme mode uses the Night theme |
| `SWE-PM-093` | `174` | `178` | `178` | `174` | `202` | **`222`** | Closing the driver door in SLEEP MODE plays the star |
| `SWE-PM-093` | `175` | `179` | `179` | `175` | `203` | **`223`** | Closing the driver door in STANDBY MODE plays the st |
| `SWE-PM-093` | `176` | `180` | `180` | `176` | `204` | **`224`** | Closing the driver door in PARTIAL OPERATION MODE pl |
| `SWE-PM-093` | `177` | `181` | `181` | `177` | `205` | **`225`** | A removed driver door makes the HU skip the start-up |
| `SWE-PM-093` | `178` | `182` | `182` | `178` | `206` | **`226`** | A mode change cancels a start-up animation in progre |
| `SWE-PM-093` | `179` | `183` | `183` | `179` | `207` | **`227`** | An ignition crank event cancels a start-up animation |
| `SWE-PM-093` | `180` | `184` | `184` | `180` | `208` | **`228`** | A mode change to TIMED MODE cancels a start-up anima |
| `SWE-PM-093` | `181` | `185` | `185` | `181` | `209` | **`229`** | An open driver door makes the HU skip the animation  |
| `SWE-PM-093` | `182` | `186` | `186` | `182` | `210` | **`230`** | A second start-up animation waits for the wakeup cyc |
| `SWE-PM-094` | `183` | `187` | `187` | `183` | `211` | **`231`** | The startup animation is displayed separately from t |
| `SWE-PM-095` | `184` | `188` | `188` | `184` | `212` | **`232`** | Leaving the SNA value resumes the state diagram with |
| `SWE-PM-096` | `252` | `259` | `259` | `255` | `213` | **`233`** | The season changes to Summer at the December date |
| `SWE-PM-096` | `253` | `260` | `260` | `256` | `214` | **`234`** | The season changes to Fall at the March date |
| `SWE-PM-096` | `254` | `261` | `261` | `257` | `215` | **`235`** | The season changes to Winter at the June date |
| `SWE-PM-096` | `255` | `262` | `262` | `258` | `216` | **`236`** | The season changes to Spring at the September date |
| `SWE-PM-096` | `256` | `263` | `263` | `259` | `217` | **`237`** | A season change plays the new season startup animati |
| `SWE-PM-096` | `257` | `264` | `264` | `260` | `218` | **`238`** | No season change plays the normal brand based startu |
| `SWE-PM-097` | `185` | `189` | `189` | `185` | `219` | **`239`** | The Fiat Latam startup animation selection replaces  |
| `SWE-PM-098` | `186` | `190` | `190` | `186` | `220` | **`240`** | The always setting plays a startup sound with the an |
| `SWE-PM-099` | `187` | `191` | `191` | `187` | `221` | **`241`** | The once a day setting plays the startup sound on th |
| `SWE-PM-099` | `188` | `192` | `192` | `188` | `222` | **`242`** | A change of the customer selected date allows the so |
| `SWE-PM-099` | `189` | `193` | `193` | `189` | `223` | **`243`** | Passing midnight allows the startup sound to play ag |
| `SWE-PM-099` | `190` | `194` | `194` | `190` | `224` | **`244`** | An automatic time zone adjustment allows the startup |
| `SWE-PM-100` | `191` | `195` | `195` | `191` | `225` | **`245`** | The never setting plays no startup sound with the an |
| `SWE-PM-101` | `192` | `196` | `196` | `192` | `226` | **`246`** | No audio brand without SDARS shows the vehicle brand |
| `SWE-PM-101` | `193` | `197` | `197` | `193` | `227` | **`247`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-101` | `194` | `198` | `198` | `194` | `228` | **`248`** | SDARS present without audio brand adds the Sirius lo |
| `SWE-PM-101` | `195` | `199` | `199` | `195` | `229` | **`249`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-102` | `196` | `200` | `200` | `196` | `230` | **`250`** | The special package drives the Klipsch Splash Screen |
| `SWE-PM-102` | `197` | `201` | `201` | `197` | `231` | **`251`** | The splash screen type drives the Klipsch Splash Scr |
| `SWE-PM-103` | `198` | `202` | `202` | `198` | `232` | **`252`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | **—** | `203` | `203` | `199` | `233` | **`253`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | **—** | `204` | `204` | `200` | `234` | **`254`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | **—** | `205` | `205` | `201` | `235` | **`255`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | `199` | `206` | `206` | `202` | `236` | **`256`** | ICS stays available while DTV is off in this status |
| `SWE-PM-104` | `200` | `207` | `207` | `203` | `237` | **`257`** | The splash and disclaimer screens appear on the firs |
| `SWE-PM-104` | `201` | `208` | `208` | `204` | `238` | **`258`** | The splash and disclaimer screens appear on the firs |
| `SWE-PM-104` | `202` | `209` | `209` | `205` | `239` | **`259`** | The disclaimer appears on the first transition from  |
| `SWE-PM-104` | `203` | `210` | `210` | `206` | `240` | **`260`** | The disclaimer appears on the first transition from  |
| `SWE-PM-104` | `204` | `211` | `211` | `207` | `241` | **`261`** | The disclaimer appears on the first transition from  |
| `SWE-PM-105` | `205` | `212` | `212` | `208` | `242` | **`262`** | An ongoing call temporarily skips the disclaimer and |
| `SWE-PM-105` | `206` | `213` | `213` | `209` | `243` | **`263`** | A backup camera view temporarily skips the disclaime |
| `SWE-PM-105` | `207` | `214` | `214` | `210` | `244` | **`264`** | An incoming call temporarily skips the disclaimer an |
| `SWE-PM-105` | `208` | `215` | `215` | `211` | `245` | **`265`** | An outgoing call temporarily skips the disclaimer an |
| `SWE-PM-105` | `209` | `216` | `216` | `212` | `246` | **`266`** | A climate pop-up temporarily skips the disclaimer an |
| `SWE-PM-105` | `210` | `217` | `217` | `213` | `247` | **`267`** | An SOS or Assist call temporarily skips the disclaim |
| `SWE-PM-105` | `211` | `218` | `218` | `214` | `248` | **`268`** | A FOTA pop up temporarily skips the disclaimer and s |
| `SWE-PM-105` | `212` | `219` | `219` | `215` | `249` | **`269`** | The skipped screens are displayed at the next transi |
| `SWE-PM-106` | `213` | `220` | `220` | `216` | `250` | **`270`** | The SOS button variant selects the SOS disclaimer te |
| `SWE-PM-107` | `214` | `221` | `221` | `217` | `251` | **`271`** | The help button variant replaces the SOS text in the |
| `SWE-PM-108` | `215` | `222` | `222` | `218` | `252` | **`272`** | A non Maserati brand shows the core disclaimer once  |
| `SWE-PM-109` | `216` | `223` | `223` | `219` | `253` | **`273`** | A GDPR market with the TBM present follows the GDPR  |
| `SWE-PM-110` | `217` | `224` | `224` | `220` | `254` | **`274`** | A missing TBM follows the non GDPR non Maserati star |
| `SWE-PM-110` | `218` | `225` | `225` | `221` | `255` | **`275`** | An unmarked country follows the non GDPR non Maserat |
| `SWE-PM-111` | `219` | `226` | `226` | `222` | `256` | **`276`** | A missing TBM adds the ADAS text to the disclaimer |
| `SWE-PM-111` | `220` | `227` | `227` | `223` | `257` | **`277`** | A country not requiring SOS or geolocation adds the  |
| `SWE-PM-113` | `221` | `228` | `228` | `224` | `258` | **`278`** | A geolocation and SOS market adds the ADAS and SOS t |
| `SWE-PM-114` | `222` | `229` | `229` | `225` | `259` | **`279`** | An incoming call from IDLE bypasses the not yet show |
| `SWE-PM-115` | `223` | `230` | `230` | `226` | `260` | **`280`** | The disclaimer bypassed for a call is shown at the n |
