<!-- source_sha256: 46bdbeecaa3729891ed8fccbd65c0b002962fce0a3f5c6c2a9e26a7aaf21fa1c -->
# Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022).pdf

## p.1

R1 – Phone
HMI Logic and Flow
Spec Release: SR24 Post 2A
st
June 21 , 2022
CR21122
HMI Lead:
Marc Van De Keere
Marc.Vande@stellantis.com
HMI: Elizabeth Mary Beaubien (Manager)
NOTE: All graphics are placeholders. Please see PDO release for official graphics. Use HMI Logic
and Flow for all official text strings and behavior.
Changes in orange

## p.2

Assumptions
Assumptions
• Orange text indicates changes made from previous release.
• This specification covers the requirements for the R1 Low and R1 High radios.
• Differences between the radios will be specified.
• Unless otherwise specified, the 12" user interface will be a scaled up version of the 10.1".
• Unless otherwise specified, the 12.3" user interface will be a scaled up version of 10.25".
• Reference PDO release for all official graphics and animation examples.
PA2.) All graphics are placeholders, but text and logic/behavior are representative.
PA4.) Orange text indicates changes made from the SR22 1A to the 2A HMI release.
PA5.) The words “Contacts” and “Phonebook” may be used interchangeably throughout this release. The tab name is “Contacts” for R1 8.4", 10.1", 10.25" and
12" and “Phonebook” for 7" but R1 Low 7" and 10.1 Portrait has “Favorites” and “Contacts” sub-sections within its “Phonebook” section.
PA6.) R1 Low 7" and 8.4 inch and R1M will not have Voice Recognition (VR). Requirements pertaining to VR throughout this Logic and Flow should be assumed to
pertain to R1 High and radios that support VR, unless otherwise specified.
PA7.) R1 Low 7" and 8.4 inch and R1M and radio variants that do not support text messaging will not have the Messages tab, the ability to download messages,
the ability to receive messages, and the ability to send messages (except for Do Not Disturb if supported). Requirements pertaining to Messaging throughout this
Logic and Flow should be assumed to pertain to R1 High and radios that support messaging only (except for Do Not Disturb), unless otherwise specified.
PA8). “Notes” are requirements.
PA9.) For references to BUX market, refer to Market Configuration table. Follow the market configuration, and if that points to an APAC collation requirements
document, that will be followed. Outside of the countries specified, the default for other countries would follow NAFTA.
Multiphone Assumptions:
MPA01) HU shall allow max of two connected phones at any given time.
MPA02) HU shall allow only one active call using the HU mic and speakers at any given time.
MPA03) HU shall allow only one phone to be in Projection Mode at any given time. During an active Projection session, only that device will have active phone
functions except CarLife.
MPA04) The Phone section will display phonebooks individually (not merged) with a method for users to toggle between both phonebooks.
MPA05) For Voice Recognition and Steering Wheel Controls, refer to VR requirements (Teleprompter and Voice Bar HMI L&F and VR Command reference tables
MPA06) The “active” phone is defined as the connected phone with active phonebook.
MPA07) Switching to a new phonebook switches to a new “active” phone.
MPA08) The term “Multiphone” refers to having two connected phones at the same time.
MPA09) Multiphone feature allows Phone functions (calls, texts) for two phones (but not BTSA for two phones)
MPA10) If user attempts to place a 3rd call while there are 2 connected calls, the system shall block it from dialing out.
2

## p.3

Phone Category
R1 High Phone Category – Main Wireframe R1 Low 8.4" Phone Category – Main Wireframe
SSttaattuuss BBaarr SSttaattuuss BBaarr R1 Low 8.4" Phone Category – during call
R1 High Phone Category – during call
Keypad Recent Favorites Contacts Messages Keypad Recent Favorites Contacts
SSttaattuuss BBaarr SSttaattuuss BBaarr
CCuu CC rr aa rree llll nntt KKeeyyppaadd RReecceenntt FFaavvoorriitteess CCoonnttaaccttss MMeessssaaggeess CCuu CC rr aa rree llll nntt Keypad Recent Favorites Contacts
PPhhoonnee CCaatteeggoorryy DDoommaaiinn//TTaabb CCoonntteenntt PPhhoonnee CCaatteeggoorryy DDoommaaiinn//TTaabb CCoonntteenntt
PPhhoonnee CCaatteeggoorryy DDoommaaiinn//TTaabb CCoonntteenntt PPhhoonnee CCaatteeggoorryy DDoommaaiinn//TTaabb CCoonntteenntt
CCoonnnneecctteedd PPhhoonnee TTaabb CCoonnnneecctteedd PPhhoonnee TTaabb DDeevviiccee CCoonnnneecctteedd PPhhoonnee TTaabb CCoonnnneecctteedd PPhhoonnee TTaabb DDeevviiccee
((PPrriimmaarryy//FFaavvoorriittee11)) ((SSeeccoonnddaarryy//FFaavvoorriittee 22)) MMaannaaggeerr ((PPrriimmaarryy//FFaavvoorriittee11)) ((SSeeccoonnddaarryy//FFaavvoorriittee 22)) MMaannaaggeerr
MMaaiinn CCaatteeggoorryy BBaarr CCoonnnneecctteedd PPhhoonnee TTaabb CCoonnnneecctteedd PPhhoonnee TTaabb DDeevviiccee MMaaiinn CCaatteeggoorryy BBaarr CCoonnnneecctteedd PPhhoonnee TTaabb CCoonnnneecctteedd PPhhoonnee TTaabb DDeevviiccee
((PPrriimmaarryy//FFaavvoorriittee11)) ((SSeeccoonnddaarryy//FFaavvoorriittee 22)) MMaannaaggeerr ((PPrriimmaarryy//FFaavvoorriittee11)) ((SSeeccoonnddaarryy//FFaavvoorriittee 22)) MMaannaaggeerr
MMaaiinn CCaatteeggoorryy BBaarr MMaaiinn CCaatteeggoorryy BBaarr
Example of 2 Bluetooth Phones connected –
R1 Low 7" Phone Tabs (no active call) R1 Low 7" Phone Tabs during call
Contacts screen of Each Phone 1
CALL
Example of 1 Bluetooth Phone connected – Contacts screen R1 High 10.25"" Phone Tabs (no active call)
R1 High 10.25"" Phone Tabs during active call
PSR01) For vehicles with Passenger Screen, refer to Passenger Screen L&F for requirements and exceptions to this logic.
PHCAT1.) The Phone Category Domain (also called Phone Category) will have 6 tabs per Connected Phone (for R1 High), in the following order: “Current Call”, “Keypad”, “Recent”, “Favorites”,
“Contacts”, and “Messages”. For R1 Low 7" the Phone section will have 4 tabs in the following order: “Phonebook”, “Recent”, Keypad”, and “Devices” (or “Call”). Users can toggle between two
Connected Phones through the Connected Phone Tabs to switch active phonebooks.
PHCAT1.1) Current Call tab will be displayed when a call is initiated, answered, active, or recently ended in the respective Connected Phone Tab until there are no active calls currently on through
that device, in which case the Current Call tab will no longer be visible to the customer. For R1 Low 7" the “devices” tab will change to the “Call” tab when a call is active. After the calls ends, the Call
tab will be replaced by the Devices tab again.
PHCAT1.2) For R1M, messaging is supported suppressing the TTS related features, like listen and new message with voice.
PHCAT2.) If no Phones connected, the Phone Category Domain screen will 1st show popup PU0065 and, if cleared, show text “Go to Device Manager to add or connect a phone.” (see Bluetooth
Pairing page for more detail). Only the Device Manager button will be selectable. Grey out the tabs (“Keypad”, “Recent”, “Favorites”, “Contacts”, and “Messages”) and do not show the Connected
Phone tab). For R1 High, only display PU0065 in this scenario when there are no paired phones.
3

## p.4

Phone Category 2
R1 Low 7" Phone Category – Recent R1 Low 7" Phone Category – “Call”
during call 10.1 Portrait Phonebook – Call Tab – Replaces 10.1 Portrait Phonebook
Favorit Contact Messag Favorites + Contacts Keypad Tab Contact – Drop Down List
Keypad Recent
es s es
R1 Low 7" Phonebook -Favorites and R1 Low 7" Phonebook
Contacts Example of 2 BT Phones connected Example of 1 BT Phone connected
R1 High 10.25" Example of 1 Bluetooth Phone
connected – Contacts screen
PHCAT2.1) If zero (0) or one (1) Bluetooth (BT) Phone is connected, only one Connected Phone Tab will be present. The second Connected Phone tab will only appear if the Setting to
enable “Two Connected Phones..” is On and a second BT Phone is connected.
RL7.1.) For R1 Low 7" the Connected Phone tabs only appear on the Phonebook and Recent sections.
PHCAT3.) The Connected Phone Tab that is active will be highlighted. If the user switches to the second Connected Phone Tab, the previous Connected Phone Tab will no longer be
highlighted and the newly selected Connected Phone Tab will be highlighted. The Favorites, Recent, Contacts, Keypad, Messages, and Current Call tabs (For R1 Low 7" also “Devices/Call”
tab) will only be applicable to the selected/highlighted/active Connected Phone Tab. While on an active call on one Phone and user switches to the other Phone tab, the Current Call tab
will not be present.
PHCAT3.1) If two BT phones are connected and the first (left most Connected Phone Tab) BT Phone is disconnected, second BT phone will move to that tab. If a third phone has already
been paired and is able to be connected, the Connected Phone Tab on the right will populate with that phone (“last in” connected Phone that is not already showing in the Phone
Category).
PHCAT3.2) The Device Manager button (“Devices” tab for R1 Low 7") will go to the Device Manager screen (reference Device Manager Logic and Flow).
PHCAT4.) If Android Auto or Apple CarPlay are active, they will take over the Phone Category section and the Phone category icon on the Main Category Bar.
PHCAT5.) Phone call status information during an active call will be shown in the status bar. Pressing the active call link in status bar will take the user to the active Call tab in the Phone
section. Call status info will not be displayed on pages where the call timer info is redundant like Current Call tab or if a widget with call status info is displayed.
PHO5.1) For 10.1" Portrait, Keypad will combine with the “Call” tab. Name “Keypad” will change to “Call” on active calls. All buttons available on the current call screen and keypad
screen will be available.
4

## p.5

Phone - Secondary Menu Popup
Phone Section Phone Section – Secondary Menu Popup
Projection Mode
(example: Android Auto)
Press the Android
Auto button on
Main Menu Bar
Phone Section while in Projection – Secondary Menu Popup
Android
PSMP1.) If already in Phone section and if the connected Phone with active phone book supports AA/CP, show a caret (in the inactive state) with the Phone Category icon on the main
menu bar (Not applicable to R1 Low 7" because there is no native menu bar displayed during projection mode)
PSMP2.) When Phone category main menu bar icon is pressed, the caret switches to the active state and a popup shows options: “Android Auto” or “Apple CarPlay” , whichever is
applicable, and a Device Manager button that links to Device Manager screen. The CP/AA option has a corresponding CP/AA icon that when pressed will connect that device for CP/AA
and launch CP/AA screen focus.
PSMP3.) During active Projection mode, if AA/CP has screen focus there will be a caret (in the inactive state) on the Projection icon on the main menu bar. If the Projection main menu
bar icon is pressed, the caret will switch to the active state and a popup with show: “Uconnect Phone” and “Device Manager” options. Pressing “Uconnect Phone” will connect that
device for native Phone functions and screen focus will change to native Phone screen (last screen viewed).
PSMP4.) The popups for Launch AA/CP or Uconnect will have a 10 second timeout if not acted upon. Making a selection from the popup, pressing outside of the popup, or pressing on
the Phone/Projection main menu bar icon while the popup is showing will close the popup.
5

## p.6

Phone
Phone Contacts Screen Current Call Tab – Outgoing Call Current Call Tab – Incoming Call Current Call Tab – Call Ended Battery Level Display Chart
Calling Call Ended 03:25
Redial
Signal Strength Display Chart
Current Call Tab – Active Call Current Call Tab – Call Held Current Call Tab – Call Muted Current Call Tab – Call Transferred SSiiggnnaall SStrtreennggtthh OOnn--ssccrreeeenn SSigignnaal l
VVaalluuee ffrroomm DDeevviiccee SStrterennggthth C Coololoreredd
BaBrsa rDs iDsipslpalya yIc on
0 None No Bars
1 1 Bar
2 2 Bar
3 3 Bar
Resume Mute 4 4 Bar
5 55 4 Bar
6 (if available) 55 4 Bar
7 (if available) 55 4 Bar
Not Supported None No Bars
Mute
Unknown None No Bars
PHPR1.) When a phone is connected, the signal strength of the active phone will be shown in the dynamic Phone icon in the menu bar.
PHLM1.) When entering the Phone Category domain, the last screen viewed will be displayed. This last mode behavior for the Phone Category domain will be latching over ignition cycles. For first time entry,
the user can be taken to the “Recent” calls tab screen but all subsequent presses of the Phone icon will follow the ‘last Phone screen viewed’ behavior. Current Call tab will be returned to only if a call is still
active, otherwise navigating away from the Current Call screen to another Category and going back to Phone after the active call has ended will bring the user to the last known tab prior to Current Call tab.
MP04) By default, the Favorite 1 phone, Favorite 2 phone or most recently connected phone has an active phonebook until a user switches phonebooks.
MP04.1) The Connected Phone tabs follow the same prioritization as active phonebook [MP04] with the left tab having highest priority (FAV 1) and the right tab (FAV 2). If no favorited devices are available then
follow BT reconnection with most recent connection displayed in the left tab, 2nd most recent in right tab.
MP05) The last selected phonebook will persist until changed by the user or until an ignition cycle.
PHCC1.) When there is an outgoing call that is not yet connected, the Current Call tab shows : 1) Hold Call (greyed out) and 2) End Call 3) Mute greyed out, and 4) Transfer. When there is an incoming call or
second incoming call on the same phone, the controls are shown in an incoming call popup: 1) Answer and 2) Decline; the first incoming call also has the following controls which are not on second incoming call
pop-up: 3) Transfer. When there is a second incoming call on the same phone, the active call is shown only on the Current Call tab and the incoming call is shown in a popup. When there is an active 2 call
scenario, the controls are: 1) Hold Call 2) End Call (for active phone) 3) Mute, 4) Transfer and 5) Join Calls and 6) Swap calls. When there is an active conference call, the controls are: (1) Transfer (2) Mute (3)
End Call (4) Hold/ When a call is ended, the temporary controls for 5 seconds on the Current Call tab are: 1) “Redial” (which calls the previous active call) and 2) End Call (greyed out). The ‘Hold’ buttons
changes to the “Resume” button when call is On Hold. When audio is transferred, the controls change to display ‘Transfer Back’ button instead of ‘Transfer to Phone” and all other controls are grayed out, with
both icons greyed out. If user is not in Phone Category during active call, Call Time is shown in the status bar. The voice system allows the user to callback the previous incoming caller. The haptic HMI only
allows this by going into the recent calls browser.
PHCC1.1) If an outgoing call is placed through the handset the user will be redirected to the Current Call tab of the active phone in the Phone category (for R1 Low 7", the “Call” tab). Buttons on the active call
screen should not be interactive/pressable when there is an incoming call popup shown. User must take action on the popup before any other action. If a second incoming call is received, it will be suppressed
until first incoming call popup has been acted upon or until it times out. If a call is placed for ASSIST, R-call or E-call the user will not be taken to the phone category domain. When the user is in an active call and
switches to another tab (like Media), the phone number/contact name and time elapsed are displayed in a button in the top status bar. If the user is on any screen in the Phone Category other than the
“Current Call” tab of the active Phone, the phone number/contact name and time elapsed are display in the status bar. Selecting the call status from the status bar will take the user to the Current Call (“Call”
for R1 Low 7") tab of the active Phone. If the outgoing call is a virtual call, remain on current screen and do not switch to phone domain. Examples of virtual calls could include navigation HFP prompts and
personal assistants such as Samsung S Voice, Cortana or others. Defer to specific features and general Audio Arbitration of system to handle specific use cases.
PHCC2.) During an active call, activating MUTE soft control mutes the HFM microphone. The mute function and button remain active until 1) the call ends, 2) the user deactivates it by pressing MUTE again or 3)
the user answers or makes a second call.
PHCC3.) During an active call, the user can press the Transfer button to transfer the audio to the handset. The button label changes to "Transfer Back" and the button remains active until 1) the user transfers
the call back by pressing the button again or 2) the call ends. When there is an incoming call or second incoming call on the same phone, pressing Transfer performs a macro function of answer and then
transfer. When the phone is not active, the transfer button is greyed out.
6

## p.7

Phone 2
R1 Low 7" Phonebook Screen R1 Low 7" Call Tab - Outgoing Call R1 Low 7" Call Tab – Incoming Call Popup R1 Low 7" Call Tab – Call Ended
Alessandra Perex
Roam
R1 Low 7" Call Tab – Active Call R1 Low 7" Call Tab – Call Held R1 Low 7" Call Tab – Call Muted R1 Low 7" Call Tab – Call Transferred
Transferred to Phone
Audio Transferred
RESUME
Mute
MUTE
Transfer to Phone
R1 High 10.25" – Contacts R1 High 10.25" – Incoming Call R1 High 10.25" – Outgoing Call
R1 High 10.25" – Active Call R1 High 10.25" – Active Call R1 High 10.25" – Call Redial 5 secs
PHCC3.2 If user has transferred the call and they leave the vehicle (while still running) out of BT range, when the user returns to the vehicle and connection is restored, display the pop-up (PU0047) ‘Would you like to transfer your
call to Hands-Free Mode?’ if there are no other Phones already connected. If there is already a phone connected with an active call, do not display pop-up(PU0047) for the second phone until the first active call has ended. For R1
High, do not display PU0047 when the user enters the vehicle while on an active call.
7

## p.8

Phone cont...
Current Call Tab - 2nd Incoming Call Current Call Tab – Join Calls Conference Call Ended
Call Ended 03:25
Redial
Current Call Tab – 2 active calls Phonebook Limit Reached (PU0056) Conference Call Muted Conference Call Held
Mute Resume
Notes:
NPL1) The Connected phone status(es) will be displayed in the Connected Phone Tab(s) in the Phone Category screen. Battery strength, phone name, signal strength (with roam status ), and Do Not Disturb status (if On) for each
connected phone are shown at all times. Battery strength should show 4 segments and signal strength has up to 5 white bars available (5 total bars should always be shown. Grey out bars that are not filled in white). This
information will be taken from the device status. ROAMING will be displayed on the Connect Phone Tab of the relevant phone on the Phone category screen if the device sends a ROAMING signal. ROAMING is for EMEA markets
only. Otherwise it will not be shown. Follow table above for how many bar to display within items.
NPL1.1) The Current Call tab screen shows the call status in the top-center: “Calling…” while the call is outgoing and not connected, Call timer for the duration of the call when the call is connected, “Call Ended” for 5 secs after the
call ends when the call is ended, and “Transferred to Phone” when audio is transferred. Incoming calls will be popups For R1 Low 7"display “<Device Name> Calling…” while the call is outgoing and not connected, “Connected Call
on <Device Name>” for the duration of the call when the call is connected.
NPL1.2) Current Call screen displays the caller ID (name of the caller or the phone number if the contact is not saved in the phone) unless the audio is transferred, in which case “Audio Transferred” is displayed. If number does not
have caller ID information, show: "Private Number". Contact ID should show for 5 seconds after call termination. In one connected call scenarios, there is a Favorite star which can be pressed (highlighted/un-highlighted) to
favorite or unfavorite the phone number of the active call. A private or unknown number cannot be favorited so do not display a favorite star.
NPL1.3) Current Call screen displays the call time: Display "MM:SS" or "HH:MM:SS" once a call is connected and keeps the call time display for 5 secs after call ends. This area is blank when no phone is connected. Call time is
accumulating, does not restart when switching between calls or accepting/starting a 2nd call. The call time should be MM:SS until an hour of call time has occurred. After an hour of call time the time will switch to HH:MM:SS. No
leading zero will be shown after the first minute. Call timer begins when both call parties are connected if Bluetooth-connected phone is GSM. If Bluetooth-connected phone is CDMA, call timer starts when dialing begins.
NPL1.4) If the phonebook is being downloaded for the first time, "Downloading Phonebook" is displayed. If the phonebook is being updated, "Updating Phonebook" is displayed.
PHCC5.5) When there is an incoming call, the user can answer the phone by pressing the answer button or the caller information in the incoming call popup. When a call is on hold, pressing the caller info on the Current Call screen
un-holds it. When there are two calls on one phone, pressing the held call information area (on the right) makes that call active (or by pressing swap).
PHCC4.) When there are two connected calls on the active phone (one active call and one on hold), the user can link the calls by pressing the Join Calls button. The resultant connection is called "Conference Call" in the CID box and
for all intents and purposes, the HMI treats it as a single call with the exception of not allowing the user to save "Conference Call" as a favorite via hold-to-set. The Join Calls button does not remain active (highlighted) once the
conference is created because the user cannot un-conference the calls. Join Calls button should not be displayed during Conference Call. In other use cases (not Conference calls), the Join Calls button should be greyed out if phone
or service provider does not support this functionality. If the phone source does not support the Join/Swap functions, the Join/Swaps button shall do nothing.
PHCC4.1) When there are two connected calls on the active Connected Phone (one active call and one on hold) or when a conference call has been established, the ways in which a user can start another call must be greyed out
for the active phone. Some examples are calling from: contacts, messaging, favorites, favorite presets and recent calls. During 2 active call scenario, any attempts to make a third call shall be blocked.
PHCC5.3) Displayed phone numbers are parsed with dashes (e.g. 555-262-4312, NOT (555)262-4312) for NAFTA, it will be displayed as a single string for non-NAFTA (e.g. 5552624312).
PHCC5.4) When there is a second call on the same phone, the currently active call is always shown on the Current Call tab . i.e. if calls are swapped, the positions of the call data will also swap (if both calls are answered, the active
call will show on the left in the Current Call tab and the held call will be shown on the right). The right side info block does not have a separate call timer (see graphics). “Answer” and “Decline” will be displayed within the Incoming
Call info block. The currently active call will not be affected until the user selects to answer the new call, then the current call will be placed on hold. During a two connected call scenario, a Favorite star is not displayed.
MP06) During an active call, the Connected Phone tab highlights to indicate the active phone. The phonebook changes to match the active phone for the duration of the call, if it was not the active phonebook before the call. If the
phonebook changed, it returns to the previously active phonebook after the call unless the user interacts with the Phone section by pressing any buttons in the Favorites, Recent, Contact, Keypad, Messages during the active call.
MP08) During an active call on one device, If the user switches phonebooks to the other device by interacting with Phone section on HU, the Connected Phone tab changes color to indicate the phonebook change, but the phone
with the active call remains the active phone (VR dial commands, SWC).
8

## p.9

Phone cont... 2
R1 High - Direct Dialing – Keypad Tab R1 High - Current Call Tab – Active Call Not on Phone – Incoming call Pop-up (PU0045) Call Timer in Status Bar
Answer
R1 High - Touch Tone Entry – 1 Call
R1 High - Touch Tone Entry – 1 Call On Hold No Active Call
Ignore
Transfer Call Request (PU0047)
Gal Gadot
R1 High - Touch Tone Entry – 2 Calls
R1 Low 7" – Keypad (two DIAL buttons)
PHCC7.) Incoming call popup (PU0045) is shown whenever the user is not on the Phone screen. For NAFTA, If the incoming call number includes a 1 before the area code, match the number to a contact with the same area code regardless if
it is in the phone with a 1 in front of the area code or not. If the backup camera or cargo camera is currently on the screen the user will hear the ringtone of the currently incoming call but will not view the incoming call popup until the
camera view has been removed. Do not go to the phone screen. when backup camera closes unless the phone screen was last page before backup camera was triggered.
PHCC7.1) Mute will be available during an incoming call to mute ringing in a one call scenario,; show mute button on incoming call popup in this use case. Pressing Mute during an incoming call highlights the Mute button and silences the
ringtone. If the user presses Mute again, the highlight will be removed and the ringtone will resume. If the call is answered after being muted, the mute button will un-highlight and the call will start. If the call is ignored after being muted,
audio will resume as normal and the next time a call is received or made the phone audio will not be muted. The Mute button is not displayed on incoming call pop-ups during an active call scenario (second incoming call on any phone).
PHCC8.) If there are multiple contacts with the same number for one connected phone, show the contact which alphabetically comes first in the contacts list. This applies to Incoming Calls, Incoming Call Pop-Ups, Accepted Calls, and
Incoming SMS Messages.
PHCC9.) If the user begins a call through their handset while the phone is connected to the head unit the call will go through the head unit and the user will be taken to the Current Call tab of the active connected phone.
PHDP1.) The Keypad allows the user to type in a call number. While in an active call, the keypad becomes "Touch Tone Entry" screen which has controls 1) Hold Call (2) End Call, (2) Join Calls (3) Transfer (4) Mute which are available or
grayed out if that function is not available. The call status will be displayed in the status bar Connected Phone Tab of the active phone which if pressed will take the user to the Current Call tab of the Active Call. The Touch Tone screen does
not have the “Dial” button. The Touch Tone Entry screen allows the user to send DTMF tones. If a call is on hold, the keypad becomes Direct Dialing screen, and user can dial a number in addition the one that's on hold. If a call is placed on
hold and send DTMF is requested using a voice command, then the HU shall unhold the call, send DTMF, and place the call back on hold. The call audio should be muted while the call is not on hold, consistent with sending DTMF through
voice commands when a call is not placed on hold first. For R1 High, there is one DIAL button for the active phone on the Keypad screen. For R1 Low 7" there are two DIAL buttons during Multiphone mode if two phones are connected to
allow user to dial a call from either connected phone.
PHDP2.) When entering the Keypad the top text field will be empty. Pressing and hold of the ‘0’ button will insert a ‘+’ into the text field. ‘+’ will always be available while in the Keypad screen. When pressing the backspace button, with
each press a digit will be removed from what has been entered. The backspace button short press clears last digit, press and hold at 500ms begins to clear digits with a digit clearing at 200ms increments. The system shall remember partial
number input in case the user starts inputting a number and leaves screen to find remaining part of phone number.
PBT1.3) If the phone menu bar icon or Steering Wheel button is pressed while Bluetooth streaming is active but no phone is connected, go to Phone mode and show popup message PU0065 (No phone Connected, do you want to pair a
phone?).
9

## p.10

Multiphone - Incoming Calls
R1 High Incoming Call on 2nd phone R1 High Incoming Call on 2nd phone during 1 active call on 1st phone
to Handset
PPiixxeell XXLL
R1 High Incoming Call on 2nd phone during 2 active calls on 1st phone R1 High Connected Call on 2nd phone
Lois Lane
to Handset
to Handset
R1 High 10.25" Incoming Call on 2nd phone
during 1 active call on 1st phone
PPiixxeell XXLL
End Call and Dial popup
MP17) During one active call on one phone, an incoming call on a second device will display a pop up that reads: “Incoming Call on <device name>” Display the <contact name> (or <phone number> if name is not available to display). The
contact picture will be displayed if picture is available. There are options: (1) “End Current Call and Answer” which ends the active Connected Call and the new call data replaces the previous active call box. During 2 active calls display “End
Current Calls and Answer” (2) Decline
MP18) During Multiphone connection, an incoming call will display the name of phone: “Incoming Call on <Phone Name>”.
MP20) During an active call on one phone, if an incoming or outgoing call is made or answered on the 2nd phone itself (not the HU) then the active call on the HU should not be interrupted or ended. In this use case, actions by a user on
the physical device should be handled by the physical device.
MP21) During an active call, the user can access the inactive phonebook but the “Listen” buttons are grayed out and all buttons that trigger an outgoing call will display a pop up (PUXXX1) that reads: “Do you want to End Call on <active
device name> and Dial this call on <inactive device name>?” This pop up has “Yes”, “No” and an [X} to close the pop up with no timeout. If there are two active calls then display pop up (PUXXX2) with “End Calls” wording. Pressing ‘No’ or
[X] will dismiss outgoing call. Pressing ‘Yes’ will end active calls and make new outgoing call on the inactive phone.
MP22) Incoming call popups are displayed over current screen. If user selects DECLINE, there is no screen change. If user selects ACCEPT then display the Current Call screen. When user presses END call button (or if call ends via device or
second party disconnect) then return to previously viewed screen unless the user interacted with the Phone domain during the call (pressed Contacts, Recent, Favorites, Keypad, Messages, Devices). If user interacted with Phone domain
during the active call then display last screen viewed in Phone domain. Buttons on the active call screen should not be interactable when there is an incoming call popup shown. User must take action on the popup before any other action.
10

## p.11

Phone Prioritization
R1 High - Device Manager > Device Settings
R1 High - Device Manager
R1 Low 7" - Device Manager > Device Settings
R1 Low 7" - Device Manager
MP09) Phone priority can be edited on Device Settings screen in Device Manager by pressing the Settings icon (or “Devices” tab for R1 Low 7"). There are 2
checkboxes to set device as “Favorite 1” or “ Favorite 2". Changes to these settings will replace a currently selected Favorite 1 or Favorite 2 and dynamically
update the other device’s settings. For example, if a phone is checked as “Favorite 1” then it replaces the current “Favorite 1”. Changes to the device
connection order apply to the next possible connection scenario.
MP10) Priority settings are remembered across ignition cycles.
MP11) If user selects “Favorite 1” or “Favorite 2” in Device Settings or during the pairing process, this user selection assigns priority and dynamically updates
the “Favorite 1” or “Favorite 2” setting for that device on Device Settings screen.
MP12) Checking one priority box unchecks the other if it was checked. Pressing a checked box will uncheck it. The checkboxes can be empty if the user does
not want to assign a priority. In this case, the phone follows normal reconnection strategy without favorited prioritization.
MP14) The Favorite 1 phone is the default phone with top priority to connect first. When connected, it has the active phonebook and is the default source for
VR dial commands and Steering Wheel Controls commands until a user changes the active phonebook.
MP15) The Favorite 2 phone has priority as the second phone to connect when a Favorite 1 phone is present. If Favorite 1 is not available to connect then the
Favorite 2 phone connects and becomes the active phone with active phonebook, and if available, another device enabled for Multiphone will connect as the
additional second phone. 11

## p.12

Multiphone Settings
GLOBAL MULTIPHONE SETTINGS: Settings > Phone/Bluetooth R1 High -PER DEVICE MULTIPHONE SETTINGS: Device Manager > Device Settings
Moto Z Force
R1 High - Device Manager
Samsung S6
Connected
iPhone X
Connected
R1 Low 7" – Devices Settings screen Settings Options
R1 Low 7" – Devices / Device Manager
MPS01) The Multiphone feature will have a global setting to enable/disable the feature for all devices (“Enable Two Active Phones” checkbox located in Settings > Phone/Bluetooth),
and a “Two Active Phones” checkbox on the Device Manager screen to toggle ON/OFF the feature. For R1 Low 7", there is no button for “Two Active Phones” on the Devices screen.
MPS05) Disabling the Global setting while 2 phones are connected will assign Phone functions to the Favorite device (if connected – Favorite 1 wins, then Favorite 2). If no Favorite
devices are present then the active phonebook becomes the active Phone. However, if the Global setting is disabled during an active call then this active phone becomes the default
Phone to prevent disconnection. Follow reconnection strategy in the Device Manager L&F.
MPS06) The Global setting cannot be disabled during 3 connections use case (Phone #1 with 1 or 2 calls and incoming call on Phone#2) to prevent loss of calls. During this time, the
Global and Per Device setting will be grayed out and the checkbox will not function until the user answers or declines the incoming call.
12

## p.13

Phone DND
Phone Ready – DND off Phone Ready – Global DND On Device Manager - Device Settings Feature not available (PU0321)
(No DND in Connected Phone Box)
Device Manager
Do Not Disturb
Phone Call/Text counter
DND Icon in Connect Phone Box Phone Ready – DND On, Auto Reply On Phone Device Settings – DND Settings
Phone Settings – DND, Customize Reply
Auto Text Reply
If DND is on for active Phone, Connected Phone tab will have DND icon
PHPR2.) When a device is connected, the supported features become readily available for that device. The user is able to press the global Do Not Disturb button to turn the feature on for all phones. Auto Reply Message is available in the
Device Settings screen and can be implemented only if the device supports outgoing SMS. The head unit shall load with DND in an off state and shall return to an off state upon ignition cycle. The Phone mode button updates when DND is
turned on and off. See the latest graphics release for the latest Phone mode button.
PMDND1.2) The default for Auto Reply setting for each phone is ‘text’ for all markets except EMEA and LATAM. For EMEA and LATAM regions, default to ‘Call’
PMDND2.) When on an active call, DND can be turned on or off using the GUI in Device Manager. While on an active phone call with DND On or Off, the user can place a second phone call but can only receive a second phone call when
DND is turned off.
PMDND2.1) If DND is enabled but the phone does not support MAP or no SMS service is available from phone for Auto Reply Message, if the user presses the Auto Reply Message Setting for the corresponding device, the user should be
informed that the feature is not available due to their device settings per the Feature Not Available popup (PU0321).
PMDND3.) DND maintains its current set status when two active calls are present. (i.e. if the user turns DND off while on a call, and places a second phone call the DND status remains off). The user may change the status of DND using the
appropriate voice command
PMDND4.) The user has the ability to turn DND off while on a conference call using the GUI on the Device Manager or Phone Settings screen. Similarly, the user can turn the feature on during a conference call; this will result in blocking all
incoming calls and/or texts depending on the related DND setting (example: Block Calls, Texts, Both). Turning DND on will not terminate current calls.
PMDND5.) When a device is connected, the DND feature can be activated. Auto Reply Message is only available on the phones that support outgoing SMS. Turning DND on shall keep DND on until the user turns DND off or there is an
ignition cycle. If the device is disconnected, the DND state shall be remembered and applied if that device connects later on in the same ignition cycle. Auto Reply Message on/off status and DND Settings shall be remembered per phone
and stored until the user changes their selection. All DND Settings (Auto Reply: Both/Text/Call, Auto Reply Message: Custom/Default, and the Customizable Auto Reply Message) shall be remembered per phone across ignition cycles.
PMDND6.) When the device is connected and the DND feature is on, the user can turn Auto Reply Message on or off through the Do Not Disturb Settings ( per device).
PMDND8.) If the DND feature is turned on and there is an incoming call, a call counter shall be present on the Connected Phone Tab of the active call, if in the Phone Category to indicate the number of calls missed while DND is on. If the
device supports incoming SMS, then the counter shall also display the number of SMS missed. The user is not taken to the Phone screen when the counter updates. The counter is removed from the phone status bar and reset when DND is
turned off or the device is disconnected.
PMDND9.) In Device Manager, within the settings for each phone, under DND settings Auto Reply has 3 checkboxes: Both, Text, Call. The user can set up Auto Reply to respond to incoming Calls, Text, or Both. DND settings only appear
when a phone is connected regardless of if DND is ON or OFF. Auto Reply is turned off within the Do Not Disturb Settings (per device) when turned On in the Device Manager screen.
PMDND10.) The user is able to select the Default or Custom Auto Reply Message. Selecting the check box shall read out the selected message using TTS.
PMDND10.1) The default for Auto Reply Message is “Default”
PMDND10.2) The default message and default customizable message for Auto Reply Message is “I am currently driving. I will respond later.”
PMDND11.) The user is able to customize the Auto Reply Message. The text is limited to 160 characters. Customize Auto Reply Message is locked out while in motion.
PMDND12.) Once the «Customize auto reply message» item is pressed, a keyboard is displayed to allow the typing of a custom message. The very fist time the «Customize auto reply message» item is pressed (a custom message is not set
yet) the keyboard is displayed without any text inside the entry box. All other times the «Customize auto reply message» item is pressed (a custom message is already set), open the keyboard with entry box populated with the custom
message previously set. If the message is too long to fit in the entry box visualization, when the keyboard is open, the last part of the message should be displayed with the cursor positioned in the last character of that message.
PMDND12.1) For R1 Low 7" and other radio variants that do not support DND Auto Text Reply, do not display this line item in DND section.
13

## p.14

Do Not Disturb 2
GLOBAL DND: Settings > Phone/Bluetooth Global DND ON: Device Manager screen
PER DEVICE DND: Device Manager > Device Settings
DND Per Device Settings
MPDND01) Do Not Disturb will have a global setting for all devices and DND settings per device that control DND for an individual phone.
MPDND02) The main DND button is global setting and turns DND ON/OFF for all devices. There is a checkbox for Do Not Disturb Mode All Phones in the Settings > Phone/Bluetooth screen and a DND
button to toggle ON/OFF global settings on the Device Manager screen.
MPDND03) Each device can individually enable Do Not Disturb mode using the checkbox on the Device Settings screen for that device in the Device Manager. The per device DND settings for Auto
Text Reply can be enabled/disabled and edited from Device Settings screen. If a phone is not connected then gray out the Do Not Disturb Mode text and disable checkbox until connected.
MPDND04) During global DND ON follow the Per Device DND Settings for each device.
MPDND05) During DND ON, there is a DND ON icon to indicate DND is on. DND settings per device will dynamically display DND symbol in the Functions Panel of Device Manager and also on Phone
section. For Global DND ON, only connected phones that have DND ON will display DND ON symbol. The dynamic Phone icon in the menu mar will display DND ON symbol during global DND ON or if
only one phone is connected which is DND ON mode. During Multiphone connections, if only one phone of two connected phones is in DND Mode then menu bar will not include DND ON symbol.
MPDND06.) Global DND Setting wins over Per Device DND settings. Example, if Phone#2 is DND ON and Global Setting is toggle ON then OFF, it will turn DND OFF for all phones. Phone#2 would have
to turn its per device DND ON settings on using Device Settings screen because it would turn off when turning Global DND OFF.
14

## p.15

Contacts
Contacts Contact Info Expanded Favorite removed
R1 Low 7" Phonebook
Wade Wilson Wade Wilson
Mobile
Anne Gack Anne Gack
Gal Gadot Gal Gadot Home Favorites
H G Gary H G Gary Work section
CH Clint Harp CH Clint Harp (top)
Contacts
section
Call Info Call Block - Outgoing Favorite added (below)
Wade Wilson
Mobile (313) 555-1212
AAnnnnee GGaacckk
Wade Wilson GGaal lG Gaaddoott Home (313) 555-1212
HH GG GGaarryy Work (313) 555-1212
CCHH CClilnint tH Haarrpp
RL7.2.) For R1 Low 7" the Phonebook tab contains two sub-sections (“Favorites” and “Contacts”). The Favorites is displayed first at top of page and the Contacts section is below it
within the Phonebooks section.
PBB1.) Contacts tab screens do not time out when no changes are made. If user picks a contact to call, the system initiates the call (if phone can initiate call at that time) and
automatically goes to the Current Call tab. Un-highlight the Contacts tab and highlight and go to the Current Call tab when a call is placed. If only one call is active, put current call on
hold and place 2nd call. When the call is ended, bring the user back to the Contacts tab (or the previous Phone tab/screen from which the call was placed) with highlighted text for the
tab name. If the system cannot call a contact at that time (e.g. two calls or conference call already in progress), grey-out buttons (not tabs) that would initiate a call and block calls if
needed.
PBB1.1) Contact names in Contacts list will all be one color text. Example: if the first name is white the last name should also be white.
PBB1.2) Contact image will appear next to the Contact name. If the Contact does not have an image associated with the name (or the image has not yet loaded), show the initials (first
and last) of the Contact in the place of an image. If the Contact only has one name (first or last) use only one letter in place of the Contact image. If the contact has no name or image
then display blank silhouette as contact image
PBB1.3) Contact list can contain duplicates of the same entry.
PBB2.) Select a list item by pressing on it. Cursor is a highlight outline. When browsing within the contacts, the cursor location is not remembered by the system. In other words, if the
user exits the Contacts screen and returns, the cursor location is brought to the top of the list. Search will be the top Contacts list item. Selecting the contact list item displays the
available phone numbers for that contact in the system. In this Contact Info screen, a star is displayed with each phone number to allow the user to make the number a favorite or un-
favorite it and a text message icon with each number to allow the user to send a text message to that number (the message icon/button will not be present for R1 Low 8.4 inch).
Selecting a phone number takes the user to the Current Call tab of the active Phone as the system starts dialing that number (if the phone can initiate the call at that time). Selecting
the text message icon takes the user to the Messaging screen to send an SMS to that contact number. Pressing the BACK button on Contact Info screen will return to previous screen in
same position within the list. After initiating a call or text from the Contact Info screen, it can be closed. Returning to Phone section after a call will take user to Contacts or Recent,
based on which Contact Info screen was used, but user would not return to previous Contact Info screen.
PBB2.05) Contact list should be presented in numeric then alphabetic order. The individual contact numbers should be shown in order 1) Mobile 2) Home 3) Work 4) Other, with the
HMI only showing entries and icons that have been assigned. The user is allowed up to 6 numbers per contact, they are not limited to a certain number per type (home, mobile, work,
other) but can only have 6 different numbers. If there are duplicate types, the numbers will simply be shown with the same type icon next to them. NAFTA and LATAM market will
display contacts as First Name then Last Name, EMEA market will display Last Name then First Name. BUX and APAC markets will display Last Name then First Name for contacts. For
APAC market do not display space separator between Last Name and First Name if the contact is in Chinese/Japanese/Korean language. See page 10 for specific Chinese/Japanese/
Korean language requirements.
PBB2.06) If the connected device does not support PBAP profile (for ex:iPod), the option to 'Download data' should be grayed out. 15

## p.16

Contacts 2
Phonebook - Favorites + Contacts R1 Low 7" Call Tab - Outgoing
Contact Info
Favorite added Favorite removed
R1 High 10.25"
PBB2.1) The user will always be taken to the top of the list for all lists in Phone Category, including Contacts and Recent Calls, when switching from tab to tab or leaving and
returning the Phone Category. They will not be taken to the last position they were on.
PBB3.) If the device does not allow Contacts download, grey out the Contacts tab for that phone.
If the Contacts are being downloaded for the first time, display "Downloading Contacts..." on the first line. The Contacts should not update in front of the user. Do not show ‘Search’
until the contacts have completed downloading.
PBB8.) When going from a contact’s details on the Contact Info screen back into browse Contacts, the system shall show the section of the list where the CURSOR position was last,
i.e. in the list of Contacts, go to the Contact that had been picked.
16

## p.17

Contacts Continued...
Search bar with VR button Keyboard – Contact Search
R1 Low 7" - Phonebook
ABC Search
Search
Search bar (speed lockout)
PHCC5.6) If user has more contacts than allowed in the system, present a pop-up (PU0056) stating “Phonebook limit reached, remaining contacts will not be added to system” when the maximum
number is reached. The contacts not added to system will not be able to be accessed to through voice or Contacts on screen. This pop-up (PU0056) will only appear the first time the user has exceeded
the limit per connected phone. If the phonebook is altered and the user goes under the allowable limit, the next time they exceed the limit the pop-up (PU0056) will be presented again.
PHB8.1) When scrolling the Contacts list, a letter pop-up will display as an overlay so user can see which letter of list they are scrolling though as they scroll up or down.
PHBB8.2) The ABC Search button when pressed will allow user to search contacts following ABC search logic (See Core L&F for ABC Search behavior)
PBB10.4) For R1M, Displayed phone numbers will follow Google phone library. For R1 High, NAFTA/APAC - AOSP library format and replacing parenthesis and spaces by dashes. Other regions - format as
received from the phone. Contact numbers can be displayed as they are shown on the person's mobile device. Follow Google phone library format.
PBB3.1) NAFTA: The user’s Contacts and recent calls will be automatically downloaded after pairing process is complete. BUX: After pairing a phone, the user will be presented with a pop-up (PU0057)
asking ‘Do you want to download your contacts and recent calls?’ and the Phone Contacts and Recent Calls will not be downloaded. If the user selects Yes, the Contacts and Recent Calls will be
downloaded. If the user selects No, their Contacts and Recent Calls will not be downloaded but their Text Messages will be downloaded with only phone numbers shown instead of contact names. If the
user tries to go into the Contacts or Recent Calls lists they will be shown a blank list with ‘Download Phone Data’ as the first line item in the list. The user will still be able to go into favorites to access
their Emergency and Towing Assistance numbers. No Text Messages will be downloaded for R1 Low 8.4 inch.
PBB4.) Search Function: For R1 High and R1 Low 8.4", the Search will be the top option in the Contacts list and is permanently fixed to screen along with the ABC search button. When the ‘Search’ button
(pressable area of line item) is pressed, it will launch the keyboard. Pressing the VR button in Search bar will shortcut VR prompts and when pressed will start with “Who would you like to call…” and VR
flow for contact search. The Search icon and text bar are not available while vehicle in motion (grayed out). If pressed during motion, the keyboard will handle speed lockout with Keyboard Unavailable
behavior, but the VR button In Search bar is always available for contact search (no speed lockout). For R1 Low 7" and R1 High 10.25", the SEARCH function is the Search icon button in different location.
PBB4.1) SEARCH refers to searching within Contacts for the active Phone. If a second Bluetooth phone is connected, only the contacts list for the selected Phone will be searched. Pressing the SEARCH
button brings up a speller that replaces the Contacts list. Default is to show alphabet. Pressing 123 toggle button brings up set of numbers and special characters and toggle button label changes to A-Z.
User can choose to START after how many character entries he/ she wants (investigate autofill list behavior). When pressing START/OK, a list with all search results is shown. The user can either press on
a search item in order to leave search or hit the CLEAR RESULTS button. Clear search cancels and returns to top of Contacts list. Pressing a search item goes to the Contact Info screen for that contact
SPELLER shall be intelligent and gray out impossible characters. On Results page, underline relevant characters in each search result line, e.g. 'BE' underlined in result "The Beatles". Only show the first
‘BE’ in the line item should be underlined. If there are no results, show "No Results Found..." on the first line of search results are and do not display the cursor. Follow SEARCH requirements in Core L&F.
PBB4.3) R1 Low 7" and R1 Low 8.4" will not have a VR button or option within Contacts Search due to not having VR available on the vehicle.
17

## p.18

Contacts Continued – APAC Requirements
Notes:
PCONA1.) APAC requirements for Contacts list order:
For Japan market, use first Hiragana “あいう…わをん” of “Phonetic Last Name”. If “Phonetic Last Name” field is blank, use first Hiragana of “Phonetic First Name”, as
the indicator. Use “#” for contacts without phonetic properties.
PCONA1.1) For Korea market, use A-Z as the English name indicator, then use Korean consonants “ㄱ…ㅎ” as the Korean name indicator.
ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
PCONA1.2) For China market, just use A-Z as the indicator, same as NAFTA.
18

## p.19

Phone Favorites
Phone Screen - Favorites Adding a Favorite – Contact Selection Adding a Favorite – Favorites Contact Info Favorite Added
Copied to
Favorites in
next
available
King Arthur KWinagd Ae rWthilusorn
position in
Favorites
Empty tab and
Contact Contact Contact Contact widget. Contact Contact Contact
Card Card Card Card Returns Card Card Card
user to the
entry point King Arthur
(Favorites
screen or
Favorites
widget)
Phone Favorites widget
Contacts Contact Info Contact Info – Favorite Added
Adds to next
available
Anne Gack position in
Gal Gadot Favorites tab.
H G Gary R s e c m re a e in n o if n
CH Clint Harp entry point
was not from
Favorites
screen.
PBB10.) For R1 High and R1 Low 8.4", present all favorites as cards in the Favorites tab. Per item, show contact name or phone number (if no name stored), phone number type, and a dropdown button.
Pressing the arrow will open the Contact Info screen, and pressing anywhere else on the Favorite card will place the call to the associated number for that Favorite. To delete a favorite, click on the
dropdown button and un-star the associated number.
RL7.3.) For R1 Low 7" Present all favorites above Contacts in the Phonebook tab. Per item, show contact name or phone number (if no name stored), phone number type, and a filled in star button. To
delete a favorite, click on the star icon of the Favorited contact in the Favorites list.
PBB10.1) For R1 High and R1 Low 8.4", when selecting to “Add Favorite Contact” when no call is active, open up the Contact Selection screen with text “Select a Contact” and header below as “Contacts”
that displays contacts for that device. . The user can then scroll through the contact names. Pressing the contact name or the arrow displays the Favorites Contact Info screen. Click on the star in the
Contact Info screen to select the desired phone number as a favorite with a popup confirming the add. If an incoming call is accepting during this process, return to Favorites after the call is ended.
RL7.4.) For R1 Low 7", the Phonebook tab will have the Connected Phone Tabs at the top, then start the list with a “Favorites” Label. When there are no Favorites, show instructional text “Add a Favorite
by selecting the Star of a Contact number” below Favorites label. After the Favorites list, show Contacts label above Contacts list. When scrolling the list the Favorites label will scroll up and not remain at
the top. When scrolling the list the Favorites and Contacts labels will scroll up with the list and not remain visible.
PBB10.2) If adding a favorite from browsing the contacts list, selecting the star in the Contact Info screen will add the contact number to the bottom of the Favorites List. The user will remain in the contact
list, with the ability to continue to add Favorites to the Favorites list
PBB10.2.1) Favorites can be reordered by pressing and holding the Contact Card and dragging left, right, up or down (when applicable). A preview of the placement should be shown during dragging.
PBB10.2.2) The system should default with one page of empty Favorites (besides Towing and Emergency) and when a page is filled, another page with one empty Contact Card/Add Favorite button will be
added. The “Add Favorites Contact” text/button will move to the bottom of the list (above the Towing and Emergency numbers) until the maximum number of Favorites is reached.
PBB10.3) For R1 High and R1 Low 8.4", the max number of Favorites is 4 pages (for 8.4" screen: 14 Favorites + Emergency and Towing numbers, for 10.1" and larger screens: 18 Favorites + Emergency and
Towing ). When the Favorites list is full if the user attempts to favorite a phone number then a pop-up will display with the text “Maximum number of Favorites reached. Unselect a Favorite then add a new
Favorite.” This pop-up will have an OK button and [X] and a 3 second timeout.
RL7.5.) For R1 Low, the max number of Favorites is 5 pages (17 Favorites + Emergency and Towing numbers). When the Favorites list is full if the user attempts to favorite a phone number then a pop-up
will display with the text “Maximum number of Favorites reached. Unselect a Favorite then add a new Favorite.” This pop-up will have an OK button and [X] and a 3 second timeout. For use cases when the
vehicle displays Emergency and/or Towing numbers, if the Contacts for device did not download (device did not allow it or user selected not to download phonebook), do not prevent access to Phone tab
that allows access to these numbers. Display the Emergency and/or Towing numbers as 2 Favorites in the Favorites section and on top line of the Contacts section, display the text "No Contacts."
19

## p.20

Favorites 2
R1 Low 7"
Phone Favorites widget – Favoriting flow
Copied to Favorite Added
Favorites – Phone widget Adding a Favorite – Favorites Contact Selection Adding a Favorite – Favorites Contact Info Favorites
in next
available
position in
Favorites
section
and
Favorite
widget.
Returns
user to
AAAllleeessssssaaannndddrrraaa PPPeerreezz
Favorites WWWooorrrkkk
widget
Contacts Contact Info Expanded
Added under
other added
Favorites
R1 High 10.25" R1 Low 10.1 Portrait
PHF1.) Pressing the call portion of a favorite Contact Card will dial that selected favorite number and switch to the Current Call tab of the respective Connected Phone. Un-highlight the
Favorites tab when a call is placed. If the user does not leave the Current Call tab during the connected call, when the call is ended, bring the user back to the previous Favorites tab.
Buttons are inactive during certain incoming and outgoing call situations
PHF2.) Store a new favorite during an active call or while the just-ended is still shown on the Current Call Tab by pressing the star next to the contact name or number (only if the name/
number is already saved as a Contact in the Phonebook)
PHF1.1) From the Favorites main screen or the Favorites phone widget, pressing the Add Favorite button will display the Favorites Contact Selection screen. Pressing a contact name or
arrow will display the Favorite Contact Info screen (similar to Contact Info but with no Favorite stars). After pressing a phone a number to favorite it, a confirmation pop-up is displayed
and the user returns to the Favorites main screen or Favorites phone widget whichever was their entry point for adding the favorite.
PHO2.1) For 10.1 Portrait, use the same layout as 8.4’’/10.1 screens (using image blocks for favorites contacts). 20

## p.21

Phone Favorites Continued...
Edit Number Dialpad (PU0351)
Favorites Favorites Options (PU0087)
Reset to Default Pop-up (PU0088)
PHF2.1) Set favorite numbers are loaded and saved for the current connected device using a unique identifier such as Bluetooth Address. Favorite numbers set for one
unique identifier are not visible when no device is connected or a device with a different unique identifier is connected. Favorite numbers are stored for 20 total
devices. Once a phone is deleted/unpaired/removed from the list of paired phones on the ECU, all the associated data and information, including but not limited to,
personal phone history, phone numbers, favorites numbers, personal information, encryption keys, link keys, shall be securely deleted from the HU. When favorite
numbers are already stored for 20 paired devices, and a new device with a new unique identifier is being paired, the paired device that has gone the longest without
being connected to the head unit will have its favorite numbers deleted.
PB13.) The list position for a Favorite contact is based on the order added or whichever position the user reordered it to be (by dragging and holding). If a Favorite is
removed and there are empty slots the empty spot should be removed and the list should move up. For R1 High and R1 Low 8.4", there will always be only one “Add
Favorite Contact” button (unless max is reached). For R1 Low 7", follow requirement RL7.4 for behavior of Add Favorite line item. Favorites will also be preloaded with
two permanent contacts at the bottom of the favorites list: Emergency and Towing Assistance (NAFTA, for BUX names should be localized for GUI and VUI) that appear
as the last two items in the Favorites list. The contact name will show up in yellow text. These contacts cannot be deleted or renamed. Their associated number may be
deleted or changed. Only one number is possible for these contacts and the icon will be the Other icon (the white circle). Options popup (PU0087) for these two entries
shows “Edit Number” and Reset to Default (Reset to Default will be shown greyed if currently set to default number). Edit number shows a dial pad with Edit Number in
the top left of the popup (PU0351) and the previous number prefilled in the blank. Reset to Default provides popup (PU0088) with Title: "Reset to Default", Text "Do
you want to change this number back to the default?" and buttons for close, "Yes" and "Cancel".
PBB10.3) Vehicles with embedded phone E-Call/Assist-Call features should not display the Towing Assistance and Emergency numbers. Towing Assistance call or
Emergency call VR commands should initiate the Assist / E-Call process respectively. If there is embedded cell with E-Call/R-Call in the Mirror, then Towing Assistance
and Emergency are removed from the contacts. Towing Assistance should not show up in Favorites for countries which do not have a default number available per the
Market Configuration Table.
21

## p.22

Phone Recent
Recent Calls Recent Calls Contact Info Messaging Screen from Recent Calls 10.1 Portrait Recents
Gal Gadot
R1 Low 7" - Recent Calls R1 Low 7" - Recent Calls Contact Info
Calling from Recent Calls
Call that Recent number
PRB1.) Phone Category tabs do not time out when no changes are made. If user selects a contact/number to call from the Recent Calls list, the system initiates the call (if phone can initiate call at that
time) with the number associated with the Recent call and automatically goes to the Current Call tab within the same Connected Phone and un-highlights the Recent Calls tab. Ending the call brings the
user back to Recent Calls tab and re-highlights the tab. If the system cannot call a contact at that time (e.g. two calls already in progress on that Phone) grey out the Recent Call tab. Selecting the text
message icon from the Contact Info screen will allow the user to send a text message to the number for the line item it was selected using the Messaging Screen from Recent Calls (similar to Messages
screen but with no Inbox or New Message tabs. There will be no text message icon/button for R1 Low 8.4 inch or for R1 Low 7" or other radios that do not support text messaging.
PRB1.1) The Recent Calls list should have an arrow which opens the Contact Info screen (like in the Contacts list). Pressing a number in the Contact Info screen will call that number and numbers can also
be favorited using the stars.
PRB2.) Select a list item by pressing the call type icon or the device name. Selecting list item calls the number associated with that recent call. Cursor is a highlight color outline. For Recent Calls, cursor
location is not remembered by the system; i.e. when coming back to Recent Calls browse after going to a different tab, the system will always default with cursor on first item of that list.
PRB2.1) Recent Call lists should be presented in chronological order with the latest first (most recent).
PRB2.2) Call grouping is displayed for all R1 radios. is not displayed for R1 High. Call grouping is displayed for R1M. Calls from the same number will be displayed in grouped format, similar to behavior on
a smartphone when receiving several calls from same contact. The number of calls will display in parenthesis on top line after the contact name/number. The calls will be grouped by call type (Missed,
Incoming, etc) and also group per day (create new grouping each day). Follow same logic for displaying the timestamp for the most recent call when grouping occurs. If excessive number of calls take up
line space, truncate number with "..."
PRB3.) Recent Calls can be further sorted into the following categories: 1) “All Calls” 2) “Incoming”3) “Outgoing” and 4) “Missed” For R1 Low 7", there is no sorting tabs to filter recent calls due to size
limitation.
PRB5.) In the Recent Calls list, the entries should start with an icon showing the call type (incoming, outgoing or missed), followed by the CID: contact name, “Private Number” or phone number (if
contact name unavailable) and on the second line display the phone type in words (Mobile, Home, Work) and display the time as: “Just Now” if received within 1 min. “[X] min ago” between 1 min and
less than 1hr ago, and “XX:YY AM/PM format after 1 hr on same day. For yesterday to previous week, display the abbreviated name of the day in order received (Sun, Sat, Fri, Thurs, Weds, Tues, Mon),
after one week or further in the same year, display the date in words for the month as “[Month][Date]” (Ex: June 3), For previous year, also display the year “[Month][Date], [Year]”(Ex: June 3, 2021) If
the device is not capable of providing the time of calls then do not display it in the list. Missed Calls should display “Missed Call” before the phone type and time.
PRB5.2) If number does not have caller ID information, show "Private Number" (without quotes). If the user selects a “Private Number” call entry the details shown should include 1) “Private Number”
(without quotes) 2)Phone call time 3) Call date. Private calls will not have pressable areas on line items because user can’t call back the unknown number or set it as a favorite or send it a text message.
22

## p.23

Phone Pairing
Enter Phone – No Phone Connected (PU0065) Phone – No Phone Connected Device Manager
PU1277 or PU1278
When the new device is paired, it will
Go to Device Manager
to add or connect a Phone Yes end your current Android Auto session.
Active
projection OK Cancel
Select
device?
No Phone Connected Device
Manager No
Bluetooth Pairing Successful – 1st Paired device (PU0353)
Bluetooth Pairing (PU0050)
Bluetooth Pairing in Progress (PU0054)
Device
PU0473
Manager
Do you want to connect Apple CarPlay?
Bluetooth Pairing Successful (PU0055)
Wireless CP/AA & Wired AA First Time Yes /
No /
SSP Pairing Confirmed on device Successful Pairing Not Now = OK
pair Phone &
PU0630 BTSA
Follow instructions on your device.
to enable Apple CarPlay. Bluetooth Pairing Not Successful (PU0061/62/63)
Start HU
search for BT
devices (see
BTP01)
See below
Wired CP First Time
Launch CP/AA
Fiat/un-branded vehicles: Vehicle Website
Launch CP
Chrysler: UconnectPhone.com
SSP Pairing Screen (PU0051) Maserati: Maserati.com/BT
PHCC6.) If the user goes to Phone mode and there is no connected phone, the system should show a popup (PU0065) showing "No Phone connected." (1st line) "Would you like to pair a Phone?" (2nd line) with close(X), Yes, No buttons. If user presses yes, system
brings up Phone pairing popup (PU0050). If user presses no/close, system closes the popup (PU0065). If the vehicle is in motion, do not provide this popup (PU0065).
SB7.) On successful pairing of a first paired phone scenario, the pop-up (PU0353) should indicate which browse categories the device is being added to if the device supports currently displayed device type (Phone / Audio
SB8.) When connecting a BTSA phone device from the Device List within the Device Manager, if no BTSA device is connected as an Audio device then the BTSA phone device should connect as Phone and Audio. If there is currently a BTSA device connected as an Audio
Device, the phone device will only be connected as a Phone device.
SB9.) If After user selects to Pair a Phone or Add Device, the Device Manger screen is loaded in background of pairing pop-ups. After pairing a device, the user will be taken to the Device Manager screen to show where the device is.
SB10.)The Bluetooth Pairing screen (PU0050) will be shown when starting pairing if there is no active projection devices. Display PU1277 before PU0050 if there is a projection device connected using 2.4 Ghz, or if there is a projection device connected using 5Ghz,
display PU1277 after pressing ‘Add Device’ before PU0050. For 2.4Ghz, CarPlay connection will disconnect upon popup 1277 confirmation, for 5Ghz, the projection connection will disconnect once until new device successful pairs. For PU0050, a randomly generated
pin will be displayed. If the phone being paired uses SSP Pairing the screen will change to the SSP Pairing (PU0051) with a randomly generated 6 digit pin after the user selects Uconnect on their device. The user will need to confirm the pin matches the one displayed
on their phone. If the user selects ‘Search for Bluetooth Devices” the vehicle will search and provide a list of BT devices for user to select a device to initiate pairing (Refer to ‘Bluetooth Pairing 2’ page)
SB10.1) For pairing a new device during an active CP/AA connection, maintain the projection connection until the new device is successfully paired for 5 GHz but disconnect the projection connection prior to pairing the new device for 2.4 GHz.
MLO1.) Add Device is disabled while in motion. If item pressed, present popup (PU0091) for 3 secs saying “Function not available while vehicle is in motion.” The same pop-up (PU0091) will appear if they are in the middle of pairing and the vehicle starts in motion,
the user is exited from pairing their device and will need to start the entire process again once the vehicle is not in motion.
PHCC10.) When pairing a new phone to connect to the system. it will display a pop-up (PU0054) stating ‘Bluetooth connection in progress. Please wait…’ with animated dots. Pressing ‘X’ will not abort connection, but will continue the pairing process.
PHCC11.) Show small pop-up that reads “<device name> is connected for phone and audio. <previously connected device name> disconnected.”. The wording of “phone” and "audio" are shown according to the connected profiles, HFP and A2DP respectively. This
notification is per device profile connection since each profile is connected separately based on the device settings. This popup (PU00167) has an X/Close button and 3 second timeout and is displayed if phone connection is lost and another phone auto connects.
PPS01) If device is paired from Passenger Screen, the head unit (driver) will not switch screens to Device Manager. After pairing process from the Passenger screen, the Passenger screen (PS) should display Device Manager screen but not the HU.
23

## p.24

Phone Pairing – Variants
R1 Low 7"
Enter Phone – No Phone Connected (PU0065) Device Manager – Devices Tab
Disconnect Confirmation
Pixel 2
When the new device is paired, it will
Yes end your current Android Auto session.
Active
projection OK Cancel
device?
No
Bluetooth Pairing in Progress
(PU0054)
Bluetooth Pairing
(PU0050)
24

## p.25

Phone Pairing 2
Bluetooth Pairing (PU0050) Search End – Devices Found
Searching for Bluetooth Devices
Yes
Were
Devices
Found?
Search End – No Devices Found
SSP Pairing SSP Pairing Screen (PU0051)
Confirmed
on device
No
PU0473 1st Paired device (PU0353)
PU0630
Do you want to connect Apple CarPlay?
BTP01) In Bluetooth Pairing (PU0050) if user selects ‘Search for Bluetooth Devices’, the ‘Searching for Bluetooth Devices’ pop-up is displayed and the head unit searches for available BT devices which will populate the list
on that screen. The list has scroll bar if needed to display more device than on the screen and there is an [X] to close with not timeout. The pop-up has text “Make sure your device is Bluetooth enabled and visible.” If the
user presses a device in the list, the pairing process is initiated for that device. The device and head unit will confirm PIN numbers and pair. If no results are found after search, the user returns to the initial Bluetooth
Pairing pop-up (PU0050). If devices are found, display the ‘Devices Found’ pop-up with the list and text of “Select to Pair” and a “Search for Bluetooth Device” button and ‘Cancel’ button and [X] to close window with no
timeout.
BTP01.1) During Bluetooth pairing process, directly after the Bluetooth Pairing in Progress pop up (PU0054) and after the ‘Connect CP/AA?” popup, the “Make Favorite” popup is displayed to allow user to favorite the
device. This pop-up is displayed as title of “Bluetooth Pairing” with text “Bluetooth Pairing Successful” then next line <Phone Name> then next line has text “Favorite phones have priority to connect before other
available devices.” and next line has text “Make this phone your favorite?”. This pop-up has “Favorite 1” and “Favorite 2” and “No” buttons and [X] to close with no timeout. Pressing FAV 1 or FAV 2 buttons assigns
favoriting priority. Pressing NO does not favorite the device. If the system does not have a Favorite device then a newly paired device is automatically set as Favorite 1 and the Make Favorite pop-up is not displayed and
the ‘Enable CP/AA’ pop-up is displayed instead. For the second phone paired to the system, if the user chooses to connect CP/AA then it will be automatically favorited as Favorite 2. Until the user chooses to favorite 2
devices from the Make Favorite popup, if it is displayed when user does not connect CP/AA, the system will automatically favorite a CP/AA device until there are 2 favorites. Afterwards, the user can choose to update
Favorites from the Make favorite popup if user does not connect CP/AA during pairing process.
BTP02) Before the Make Favorite pop-up, if the device is detected as capable of CP/AA, the “Enable CP/AA” popup is displayed “Do you want to connect Apple CarPlay? Settings can be changed later using the Device
Manager.” (For AA, replace “Apple CarPlay” text with “Android Auto”). This pop up has an ‘OK’ and ‘Not Now’ buttons and [X] to close with no timeout. If user selects the ‘Not Now’ button then pair the device for Phone
(HFP) and BTSA following standard pairing process. If user selects the ‘OK’ button for wired CP FRX then launch CP. For Wireless CP/AA and wired AA FRX, display pop up that reads: “Follow instructions on your device.”
This pop up has a 1 minute timeout and is displayed until CP/AA launches. This popup is displayed for Wireless AA when the AA app is opened to prevent it being displayed twice and may not need to be displayed if user
accepts on device before launching wireless AA. This popup is not displayed for wired CP FRX. The user’s selections will be saved as the Device Settings for that device in the Device Manager. For the first paired device (or
any pairing with no currently paired phones) pressing ‘Not Now’ will pair for Phone/BTSA and display PU0353 after successful pairing.
BTP04) After these pairing pop ups, the final BT pairing pop ups will display based on pairing success or failure. Refer to ‘Bluetooth Pairing’ page for requirements.
BTP04.1)
25

## p.26

Bluetooth Pairing & Projection Use Cases
Projection-Related Pairing Requirements:
BTP04.1) If the device list is full with the max number of paired phones, plugging in a new, not paired projection device will launch the first run experience for CarPlay or Android Auto.
The popup (PU0064 – The Paired Device List is full popup) must not be displayed immediately. It must be delayed to display when the actual out of band pairing (OOB) begins.
BTP04.2) If there are no paired devices that support CP or AA when the user presses a CarPlay or Android Auto icon, it will display popup. This popup has text “No Apple CarPlay device
connected. Do you want to pair a device?” with YES and NO options and [X] to dismiss and no timeout. For Android Auto, replace “Apple CarPlay” with “Android Auto” text. If the user
presses NO then dismiss the popup. If the user presses YES then it will initiate the pairing process. This behavior will apply to CP/AA icons when disconnected that are not status
indicators (ie: It would not apply to the Media widget audio selector but it would apply to the Media Shortcut or an App Shortcut if the user had added one to the system. (ie: User
presses AA icon in App Drawer or a Pinned Favorite Audio source in Media or a Shortcut on Homescreen when there are no paired devices that support AA. If the user selects YES from
the popup then it starts the pairing process.
BTP04.3) For R1 High, when the user pairs a new phone if the Enable Wireless Cameras setting is enabled, automatically disable the wireless camera setting and follow the normal pairing
process. and a popup will be displayed. This popup will replace the existing PU0473 for this scenario. The popup will have text that reads “Do you want to disable wireless cameras and
connect Apple CarPlay? Settings can be changed later using the Device Manager.” For Android Auto, replace "Apple CarPlay" text with "Android Auto". This popup has OK and ‘Not Now’
buttons, X to dismiss and no timeout. Pressing the OK button will disable wireless cameras (turn setting OFF) and connect CP/AA. Pressing ‘Not Now’ will not disable wireless cameras
settings (no settings change) and continue the phone pairing process as native phone connection (not CP/AA connection). Pressing X will dismiss popup.
26

## p.27

Multiphone Pairing
Pairing popup With One Connected Phone
Enable CP/AA popup
Connect As Second Phone
Make Favorite 1 or 2 popup
iPhone 6
With Two Connected Phones
Device Manager Connect As Replace Phone popup to replace a phone
MPP1.) If one or more phones are connected, when the Pairing process is initiated it displays the Pairing popup, then the Make Favorite 1 or 2 popup is displayed (if it is not the first paired phone and the user
does not connect CP/AA). This popup displays text: Line#1 = “Bluetooth Pairing Successful:”, Line#2 = “<Phone Name>” is displayed. Line#3 = “Favorite phones have priority to connect before other available
devices.” Line#4= “Make this phone your favorite?”. This popup has options for “Favorite 1”, “Favorite 2” and “No”. Selecting to favorite the phone will update the Device Settings screen with the favorited
selection (1 or 2). If “No” is selected the phone will be connected but not favorited. This popup is displayed after the Enable CP/AA Auto popup so user can select how to connect the device.
MPP2) For Multiphone, if there are no paired phones, set the first paired phone as Favorite #1 and remove the “Make Favorite” popup and follow normal pairing and connection process for no phones paired
followed by “Pairing Successful” popup (PU0353) if user connects for Phone/BTSA. After the first phone is paired and made the Favorite 1 device, all future pairings will display the Make Favorite 1 or 2 popup if
there is already a Favorite 1 device in the system and if the user does not connect CP/AA.
MPP3) After the Make Favorite 1 or 2 popup when there are no connected phones, the new phone is connected as the only phone and the users is taken to the Device Manager. When there is one connected
phone, the new phone is connected as a second phone and the user is taken to Device Manager screen with a popup that has text: Line#1 = “Connected as Second Phone”, Line#2 = “Use the Device Manager to
change connections or go to Phone Settings for more options.” This popup has an OK button an [X] with no timeout.
MPP4) After the Make Favorite 1 or 2 popup when there are two connected phones, a popup is displayed so user can choose which phone to replace. The popup has text: “How do you want to connect this
phone?” with 2 options “Replace <Phone Name1>” or “Replace <Phone Name2>”. This popup has an [X] with no timeout. Whichever phone the user selects to replace will be disconnected and the new phone
will be connected in its place, and the user is taken to the Device Manager screen.
27

## p.28

Phone Messaging – Incoming
Favorites Screen Messaging Not Supported (PU0080/81/82) Incoming Message (PU0083)
Anne Gack
Gal Gadot OR Feature Not Available (PU0321)
G Gary
H
CH Clint Harp
Messaging - Inbox Messaging – View Messaging – Listen (PU0084)
PHS1.) For R1 High, grey out Messages tab if respective phone does not support SMS messaging because phone cannot support SMS in general or device Bluetooth settings are not configured properly. Do not show the
Messages tab for R1 Low 8.4 inch.
PHS1.1.) If user presses any SMS button (ex. reply, forward, call, etc.) and phone does not support feature, provide popup (PU0080/81/82) with no title, OK button and text: line1: "Feature not supported on"; line 2: "the current
phone."; line 3: blank line: line 4 "For device compatibility information"; line 5: "Visit UconnectPhone.com" (if Chrysler) or “Visit Maserati.com/bt” (if Maserati) or “Visit Vehicle Website” (if Fiat or unbranded), timeout after 3
secs. If SMS is blocked due to driver distraction (ex. View), present popup (PU0091) for 3 secs saying "Feature not available while vehicle is in motion”.
PHS1.2.) If Bluetooth MAP (message access profile) is supported per SDP (service discovery profile) response and the user presses the Messages tab, even though it is greyed out due to device Bluetooth settings, the user should
be informed that the feature is not available due to their device Bluetooth settings per the Feature Not Available popup (PU0321). If SMS is not supported in general on the phone, but the user presses the greyed out Messages
tab button, provide the user with the Messaging Not Supported popup (PU0080/81/82).
TMP1.) When user gets a text message, provide popup (PU0083) telling the sender name or number if not in Contacts List , Provide buttons to VIEW, LISTEN, show "X" (close) button. Pressing VIEW goes to the Full Message
Popup (PU0203). Pressing LISTEN starts TTS reading of the message from beginning if TTS not currently active and stops TTS if TTS currently active. Pushing the Listen button takes user to the Listen popup (PU0084). After the
message is read, the popup (PU0084) should time out and user should be taken back to the previous screen (not popup PU0083). Pressing either the "X" (close) button on popup PU0083 or PU0084 will close the popup and
brings user back to previous screen. If REPLY, Call, or FORWARD buttons are not available, grey out, and if pressed play Conf 2 tone and display the Siri Ready popup (PU0255) if the device has Siri enabled. If the device does not
have Siri enabled show the feature not supported popup (PU0080/81/82). Provide popup (PU0080/81/82) with no title, OK button and text: line1: "Feature not supported on"; line 2: "the current phone."; line 3: blank line: line
4 "For device compatibility information"; line 5: "Visit UconnectPhone.com" timeout after 3 secs. If SMS is blocked due to driver distraction, present popup for 3 secs saying "Feature not available while vehicle is in motion”
(PU0091).
TMP2.) The full message popup (PU0203) will provide the text of the message (up to 5 lines). Buttons of the popup (PU0203) allow the user to "Listen" to the message (starts TTS from beginning if TTS not currently active, Stops
TTS if TTS currently active), "Reply" to the message (brings user to the select outgoing message list of SMS send dialog (see SMS6, SMS8)), "Forward" the message (skips user to select contact portion of SMS send dialog (see
SMS6,SMS7)), "Inbox" (closes popup (PU0203) and goes to SMS inbox screen), and "Call" (closes popup (PU0203), goes to Phone Category domain and initiates call to that number (if phone can initiate call at that time)). If it is a
Private number, gray out CALL buttons.
SLO1.1) Message text cannot be shown while in motion. If user receives text message during lockout, grey out the View button on the notification popup (PU0083). The View button in the Inbox would also be greyed out and
unavailable. If the user is viewing text message details while in motion, close the message details popup (PU0203) and present popup (PU0091) for 3 secs saying “Function not available while vehicle is in motion.” if the vehicle
comes back to a stop do not switch back to the view text message details screen (PU0203).
TMB4.) While the system is downloading the users text messages ‘Downloading…’ will appear in the top line of the Messages Inbox, all other lines will be displayed as blank. Once the system has completed downloading it will
display the text messages in the screen. The user does not need to exit the inbox for the update.
TMB5.) If the user has selected messaging to be off for the current phone, when entering the Messages tab the New Message button will be greyed out, messages will be removed, and the top line will state ‘Messaging On’. The
user can press on the first list item to turn messaging back on for the current device, this will make the New Message button available and the list of text messages appear.
28

## p.29

Phone Messaging – Incoming 2
R1 High - Text Messaging Flow
29

## p.30

Phone Messaging – Multiple Incoming
Multiphone Multiple Incoming Text Pop-up
Multiple Incoming Text Pop-up (PU0149)
Last
Incoming SMS
Mode
Display incoming SMS =1 ≥2
Incoming SMS
pop-up following SMS
count
pop-up conditions
Messages > Inbox
Message Inbox
(PUXXX1)
TMP1.2) If there are 2 new SMS popups (PU0083) awaiting the user's acknowledgement, merge all into a single popup (PU00149) which indicates the amount of new messages available, and
only provides options to go to Inbox or Ignore them all.
TMP1.3) While on a phone call, viewing a text message, or composing a text message via haptic selection or VR, if a text message(s) has been received, once the phone call or text message is
complete a pop-up (PU0149) will appear. Composing a text message via haptic selection begins when the user enter the ‘New Message’ screen. Text messaging is considered complete when
the user has sent the message and the ‘message sending popup (PU0205) disappears’ either because the user closes it or because the popup (PU0205) disappears after a certain amount of
time. Text messaging is also considered complete if the user cancels out of the composition of the message. The user will be given the option to either view their list of messages (inbox) or
ignore the pop-up (PU0149). The number of messages indicated will be dynamic, if another message is received while on this pop-up (PU0149) the number will increase.
Multiphone Assumptions:
• Multiphone connection involves two connected SMS-enabled phones.
• Multiphone Text Messaging will follow the same behavior as one phone as long as the other connected phone is inactive (not interrupting the flow).
• Buttons within Text Message pop up apply to the Phone (and phonebook) that received the text.
MSMS01) During Multiphone connection, the Multiphone Incoming Message pop up (PU0083) will display the phone name: “Text Message on <Phone Name>” to indicate which connected
phone received the text.
MSMS02) During Multiphone connection, the Multiphone Multiple Incoming Text pop up (PU0083) will be displayed if text were missed on both devices. The total number of texts missed on
both phones will be displayed: “You have <n> new text messages”. This pop up will have two INBOX buttons, one labeled with each <Phone Name> and a number indicator for each INBOX
button to denote the number of new messages on that phone. Pressing either INBOX button will take the user to that respective Inbox (switching phonebooks if needed). The Favorite phone’s
INBOX button is displayed on the left. If no Favorite is connected, the phone with an active phonebook is displayed on the left.
MSMS03) During an active phone call on one device, any buttons in the Messages section of the second device’s phonebook that would trigger an outgoing call will display pop up (PUXXX1) to
notify the user that the current call must be ended before making a call from the second device.
30

## p.31

Phone Messaging
Messaging – Inbox Messaging – View (PU0203) Messaging – Inbox (top line Read) Messaging – Listen (PU0084)
Vehicle in
Motion
Contact Info
Vehicle in Start SMS Vehicle Not Messaging – View (PU0203)
Motion VR Session in Motion
Messaging – Message Type Select
Vehicle
Parked
SMS1.) In the Text Message View popup (PU0203) and Listen popup (PU0084), Iin upper right corner, show "X" (close) button. Pressing "X" (close) button brings user back to previous Phone screen. User
must press the "X" (close) button or the Phone Category button to switch back to Phone screen. If user picks ‘Call’ button from a Text Messaging Pop-up selection, the system initiates the call (if phone can
initiate call at that time) and automatically bring up Phone Current Call tab of active Phone.
SMS2.) Select a list item by pressing on it. Cursor is a highlight color outline, which moves to selected list items (pressing View or Listen qualifies as selecting a list item). For SMS, neither cursor location
nor browse category are remembered by the system when leaving the Messages tab; i.e. when coming back to the Messages tab after leaving, system will always default to Inbox browse view with cursor
on first item of that list. Finally, if the user presses the view or listen button on a line, move the cursor to that line (if it is not already there).
SMS3.) Browse (filters along the side) categories available within Messages: 1) “Inbox” 2) “New Message”
SMS4.) Display 'No messages' as first list item if the message list is empty and do not show cursor.
SMS5.) On Messages tab screen, highlight Inbox category in highlight color when Inbox is selected. Present all messages in a list in order from newest to oldest. On the first line of each message, show
contact name, if available. Show read/unread message icon next to each entry to denote if it's been read yet or not. On the second line of each message show the phone number type and the time the
message was received (follow the format of Recent calls time). Show Listen and View buttons on right hand side of screen.
Pressing Listen while the vehicle is not in motion will popup the View Message (PU0203) and read the message out loud. Pressing the Listen button during message TTS will stop reading of the message
and un-highlight the Listen button. Also pressing the “X” button to dismiss the pop-up will stop TTS reading of the message. Pressing the Listen button while the vehicle is in motion, the message is played
out loud and the user is taken to the Listen pop-up (PU0084) to allow for selections such as Reply, Forward, etc. The ‘Listen’ button will not be accessible during an active phone call.
Selecting View goes to the full message popup (PU0203) for that message (See TMP2). Selecting Listen starts TTS reading of the message from beginning if TTS not currently active and stops TTS if TTS
currently active. Selecting a line through either Enter hard control or pressing on the line is equivalent to pressing View or Listen, if the vehicle is not in motion View will be selected, if the vehicle is in
motion Listen will be selected, both will bring up the Text Message pop-up (PU0084 or PU0203).
SMS12.) After sending a text message, wait until any text message popups (PU0205) close, or are closed, and return the user to the following screens depending on how the text message was sent: If the
user enters New Message to send a text, they shall be returned to Messages Inbox with the newest message on top. If the user chooses to ‘Reply’ while viewing a text message, they shall be returned to
Messaging Inbox with the newest message on top. If the user enters Contacts, selects a contact, and sends the Contacts a text they shall be returned to Contacts with the first contact on top. If the user
creates and sends a text message using Voice Recognition, they shall be returned to the screen which was active immediately prior to beginning the Voice Recognition session. Any other ways to send a
text message, if not defined in this requirement, shall return the user to Phone Category domain.
SMS12.1) Text messages can be sent to any contact numbers (Mobile, Home, Work or Other).
SMS12.2) For China Market, do not display the "Send Predefined Message with Voice" option in Messages screen because it is not supported by Tencent VR.
SMS12.3) For R1M, Messaging will be suported but TTS related features will be suppressed like listen and new message with voice if radio lacks support of TTS related features. 31

## p.32

Phone Messaging Send – Pre-Defined Message
Messages - Inbox New Message Contact Selection New Message Contact Info
Start SMS
Messaging – View (PU0203)
Messaging – Pre-Defined Message Review (PU0273) VR Session Messaging – Message Type Select
Messaging – Pre-Defined Message
Messaging – Sending (PU0205)
Qualifier List
Notes:
SLO2.) If the user is anywhere in the process of sending a message (i.e. before hitting send) and lockout is exhibited, return the user to the Messages Inbox and present popup (PU0354) for 8 secs saying “Function not
available while vehicle is in motion. Press phone button on steering wheel to send a message.” with Cancel Button. Send a predefined message line is greyed out in the Messages New Message view. If item pressed,
present popup (PU0354).
SMS6.) If user requests to send new text message from Messages Inbox, present the New Message Contact Selection screen (a modified version of the Contacts Selection screen). The user can press the arrow on a
contact to open the New Message Contact Info screen and select a phone number to send the text message. After a contact number is selected (or if user selected the text messaging icon from a Contact or Recent),
show New Message tab of Messages screen , and present two options: "Send a Predefined Message with Voice" (show ">"), and "Send a Predefined Message" (show ">"). If Send a Predefined Message with Voice is
selected, start SMS VR session. If Send a Predefined Message is selected, present all available messages in numbered list. Selecting a line chooses that message. Some messages require a follow-up qualifier list (e.g.
I'll be there in <XX> minutes). The user can either select a message with qualifier from the Qualifier List or use the back button to select another message from the Pre-Defined Message list.
SMS6.1) Once the user has selected a predefined message to send, the user is shown a preview popup (PU0273) of the outgoing message and addressee (do not show automatically appended signatures). The buttons
shown are SEND, CANCEL and X (close). SENDing the message shows a brief status screen OK or X (Close) on the popup (PU0205). Where available during text messaging process, Back button steps the user back one
step in the process with the previous cursor and list position maintained if using Back button.
SMS6.2) SMS sending result pop-up (PU0205) time-out: 5 3 sec.
SMS6.3) Provide a BACK arrow button during the process of sending a New Message so user can return to previous screens by pressing the BACK arrow.
SMS8.) If the user replies to a text message, the user only needs to select the outgoing message from the available outgoing messages list as the recipient is assumed. Back arrow is unavailable on the first screen of
this flow.
SMS8.1) After sending a message, the user returns to previous tab from which the message was initiated (Contacts, Recent). User remains on previous screen if replying to an incoming text. For example, user is
32
in Climate and replies to incoming text then return to Climate after text is sent.

## p.33

Phone Messaging Send – Forward
New Message Contact Info
Messaging – View (PU0203) New Message Contact Selection Messaging – Sending (PU0205)
Messaging – Listen (PU0084)
Notes:
SMS7.) If the user forwards a text message from the Full Message Popup (PU0203), they are brought directly to the New Message Contact Selection screen (see SMS6) as the text
of the message is assumed. Back arrow is available on the first screen of this flow.
33

## p.34

Phone Messaging Send – VR
Messaging Messages - Inbox Messaging – New Message Contact Selection Messaging – New Message Contact info Incoming Message (PU0083)
Greyed out if
Vehicle in Motion
Messaging – Message Type Select
Start SMS
VR Session
Greyed out if
Vehicle in Motion
Notes:
SMSD1.) Starting SMS VR session does not take user away from current screen
SMSD1.1) If SMS VR is launched from an SMS popup (PU0084 or PU0203), Starting SMS VR session does not take user away from New Message screen. Once message has been sent
via VR, user is taken back to screen under the text message popup (PU0084 or PU0203) their flow originated from. There is no GUI event associated with a sent message.
SMSD1.2) If SMS VR Session is launched from New Message tab in Messages screen, once message has been sent, user is taken back to New Message tab in Messages screen.
34

## p.35

Voice Recognition
Multiphone Assumptions:
• Both phonebooks will be accessible for VR commands.
• Refer to VR requirements (Teleprompter and Voice Bar HMI L&F and VR Command reference tables)
35

## p.36

Phone Data Download and SMS (EMEA ONLY)
(PU0086) (PU0057)
(PU0059)
Notes: Exceptions for EMEA Market
PD1.) After the user pairs a phone they will see a pop-up (PU0057) that asks ‘Would you like to download your phonebook and recent calls?’. If the user selects yes then the phonebook and recent call
list will be downloaded to the head unit. If the user selects no, the phonebook and recent call list will not be downloaded. SMS will still be downloaded but it will only show numbers instead of contact
names. (Also Reference note PBB3.1). Default setting for Text Messaging is ON.
PD2.) If the user has selected No to downloading their phonebook/recent calls, if they press the phonebook or recent calls button they will be taken to a blank list with the top option as ‘Download
data’. If the user presses ‘Download Data’ they will be presented with the same pop-up (PU0057) asking ‘Would you like to download your phonebook and recent calls?’ (Also Reference note
PBB3.1). Even if the phone data is not downloaded the user will still able to access the 911/help list. Recent call list will show empty calls in that case.
PD4.) Text Messaging Enable will be available within the messaging screen and from the Device Settings screen in the Device Manager. If Messaging is enabled it will operate as normal, if disabled the
user will not be alerted to incoming text messages, their inbox will be grayed out, and they cannot send text messages. This setting will be per phone and not system wide.
PD8.) If the user has selected messaging to be off for the current phone, when entering the messaging screen the Inbox and New Message buttons will be greyed out, messages will be removed, and
the top line will display text “Enable Text Messaging”. The user can press on “Enable Text Messaging” to turn messaging back on for the current device, this will make the New Message button
available and the list of text messages appear and update the corresponding setting in Device Settings screen of Device Manager for that device. See Device Manager L&F for related EMEA Phonebook
requirements.
PD9.) If Messaging is not available on the current phone the “Enable Text Messaging” option in Device Manager will appear greyed out. If phonebook download is not available on the current phone
Delete Phonebook Data/Download Phonebook Data options will appear greyed out on the Device Settings screen of Device Manager. The button labels will depend on the current status of the system.
Delete Phonebook Data will delete the phonebook and recent calls of the selected phone from the head unit, Phonebook Data Delete will only be shown as an option if the phonebook and recent calls
are currently downloaded otherwise ‘Download Phonebook Data will be displayed. Messaging ON / OFF will turn on/off the text messaging feature off for the currently selected device. (Reference
Note PBB3.2 in Contacts Cont)
PD10.) If the user selects Delete Phonebook Data in Device Manager, a pop-up (PU0116) will appear asking the user ‘Are you sure you want to remove your phonebook and recent calls?’ with yes/no
as options. If the user selects no they will be taken back to the previous screen and keep their data. If the user selects yes the Contacts and Recent calls will be removed. The user will be taken back to
the previous screen but “Delete Phonebook Data” button will be shown as ‘Download Phonebook Data’. If the user selects to Download Data, the user will be presented with the pop-up (PU0057)
‘Would you like to download your phonebook and recent calls?’ If yes selected the users phone data is downloaded, if no, the data is not downloaded.
PD11.) Messaging will not appear in the Phone Options list for R1 Low 8.4 inch.
36

## p.37

Phone Widgets – Home Screen
Phone Widget – No Phone Connected Screen Phone Widget – Recents Screen Phone Widget – Favorites Screen
Phone Widget – Current Call Screen Phone Widget – Two Current Calls Screen
Recent Calls screen – No Recent Calls Favorites screen – No Favorites
No Recent Calls
Refer to previous pages of Phone Logic and Flow for complete logic.
Favorites Heading – Widget Title
W01.) Widget title for Current Call is “Current Call” for R1 Low 7" and for R1 High, the title is <phone name> <battery strength icon>. Follow PDO graphics. Widget title for Favorites is “Favorites” for R1 Low 7" and for other radio sizes with space it is
“Favorites, <phone name> <battery strength icon>. Widget title for Recent is “Recent” for R1 Low 7" and for larger radio sizes like R1 High it is “Recent, <phone name> <battery strength icon>.
PW1.) There will be two Phone widget options: Recents and Favorites. Other screens variations will be available depending on phone connection status.
PW1.1) If there is no connected phone, show only the “No Phone Connected” screen with Widget title as “Phone” until a phone is connected with text message “Select “Add Device” to start the pairing process.” This screen has a Device Manager button
(“Devices” button for R1 Low 7") and an Add Device button that takes the user to the phone pairing process.
PW1.2.) The “Phone - Recent” widget shows the status of the active connected phone. The 50% widget will show a maximum of 6 recent calls and the 25% widget will show a maximum of 3 recent calls. For R1 Low 7", show a maximum of 3 recent calls in
widget. Display icon for type of call, name or phone number, phone type, and time). Pressing a contact number will place a call to that number. If no recent calls are available display text “No Recent Calls” Pressing the top header of widget opens Recent tab
as full screen.
PW1.3.) The Favorites widget, for the 50% widget will show a maximum of 6 Favorite Contacts and the 25% widget will show a maximum of 3 Favorite Contacts. For R1 Low 7", show a maximum of 3 Favorites in widget. Pressing a contact number will place a
call to that number. If the rows in the Favorites widget do not contain favorited contacts then they will act as buttons to Add Favorite from the widget. Pressing the top header of widget opens Favorites tab as full screen.
PW1.4) The Favorites widget will display Add Favorite buttons after the last favorite. If user adds a favorite, it displays after the last added Favorite so the Favorites widget and Favorites screen will be similarly sorted to match.
PW2.) If the active phone receives a call or has an ongoing call, the Phone widget(s) will display the Current Call screens.
PW2.1.) While on a single call, the 50% widget will show the status of the connected phone, the Contact Photo (if available), call Contact name or phone number (if Contact name not available, call timer, and the following buttons with the applicable
available/grey state: End Call, Mute, Hold, Transfer, and if there are two calls show Join, and Swap. For R1 Low 7", the Connected Call widget displays the Contact photo as background (if available) and displays the following buttons: End Call, Mute, Hold (if
available), and Transfer.
PW2.2.) While on a single call, the 25% widget screen will show the Contact Photo (if available), call Contact name of phone number (if Contact name not available), call timer, Hold, Mute, and an End Call button.
PW3.) If a second incoming call is accepted, the Current Call screen will show the Two Current Calls screen in place of the Recent and Favorites screens.
PW4). When a Home page has both the Favorites and Recent Phone widgets, during an active call, replace the larger of the two widgets with the Current Call content. If both Phone widgets are the same size, replace the Favorites widget with the Current Call
content.
PW4.1). When a Home page has an active call in a widget, if the user initiates a call in any other Phone widget or via device then the widget with the active call will handle the new call. There will not be two instances of active calls present at the same time. If
user makes VR call from Home screen when there is a widget(s) then the Current Call widget will populate with phone call info and follow Current Call flow. If no widget is on Home screen then a VR command will open the Current Call screen. If user receives
a call it will be answered in the phone widget of Home screen (the larger of the two widgets on Home screen a call
PW3.1.) While there are two calls (one on hold and one active) the 50% widget will show the Contact Photo (if available), call Contact name or phone number if Contact name not available), and call timer for the active call. The screen will display the
following buttons: End Call, Mute, Hold (if available), Transfer, Join, and Swap. For R1 Low 7" during two call scenario, the Two Connected Calls widget displays the Contact photo as background (if available) on active call and displays the following buttons:
End Call, Mute, Join, and Swap.
PW3.2.) While there are two calls (one on hold and one active), on the 25% widget, show the contact name (or phone number) of both calls, caller timer of the active call, End Call button for the active call
and a Swap button.
PW4) If making a call from a Phone widget, the widget will temporarily be replaced by the Outgoing Call and then Current Call screens for the duration of the call and return to previous widget after the call has ended.
PW5) If making a call via VR on the Home screen, the new call will transition to the Current Call screen.
PW5.1.) During an active CarPlay or Android Auto session, the phone widgets will be populated by data from the Android or CarPlay device and function with same behaviors as native phone widgets.
HOM1.1) For 10.1 Portrait, 50% widgets should use the 50% layout of 8.4/10.1 landscape screen size, and 25% widget will contain content of the 7" 50% widget.
37

## p.38

Phone Widgets 2
R1 Low 7"
No Connected Phone Screen Recent Calls screen Favorite Contacts screen 10.1 Portrait Phone Homescreen
Recent Calls screen – No Recent Calls
No Recent Calls
Favorites Calls screen – No
Current Call Screen Two Current Calls Screen Favorite Contacts Refer to previous pages of
++
Phone Logic and Flow for
complete logic. +
+
+
R1 High 10.25"
Current Call Screen Widget Recent Widget Favorites Widget
38

## p.39

Shortcuts – Make a Call
Select Shortcut Type – Make a Call Make a Call – Contact Selection Make a Call - Contact Info Selection
Work
Shortcuts
Is this a
NO Is this the active YES connected
phonebook? phone?
YES NO
Make Call Make Call Gray out
on inactive phone on active phone Shortcut
PSC01) Pressing the ‘Make a Call’ button in Shortcuts will display the Contact Selection screen. Users can press device name or arrow to show the Favorites Contact Info screen
where user can select the phone number to assign as the Make a Call shortcut. After selecting the phone number, the user is taken back to the Shortcuts screen with the newly
added shortcut displayed.
PSC02) Make a Call shortcuts are linked to the phones and the active phonebooks from which they are assigned. If this shortcut was created from a phone that is not currently
connected then that shortcut button on Shortcut screen will be grayed out because calling is not possible. Make a Call shortcut buttons will not be grayed out if the related phone
is connected because calling is possible.
PSC03) If the Make a Call shortcut is linked to the connected phone with active phonebook (highlighted Connected Phone tab) then pressing the Make a Call shortcut will initiate a
call to that number on that device. If the shortcut is linked to a connected phone which is not currently the active phonebook (not highlighted Connected Phone tab), a pop-up will
display that reads ”Do you want to switch active phones and call <Contact name> on <Phone name>?". This pop up has ‘OK’ and ‘Cancel’ buttons with an [X] to close and no
timeout. Pressing OK will place the call on that device and temporarily switch active phonebooks to the other phone for the duration of the call. Follow same rules for returning the
active phonebook to the previous phonebook if the user does not interact with the Phone category during the call (user does not press any tabs within the Phone screen other than
Current Call tab)
PSC042) If contact name exceeds space allowed, truncate the last letters with "..." after last available letter. See Core L&F for truncation requirements.
PSC05) If no phones are connected, gray out any Make a Call buttons and display a popup that reads “No Phone is Connected". This popup has an OK and [X] to dismiss and 3 second
timeout.
39

## p.40

Shortcuts 2 - Make a Call
Make a Call - Contact Info Selection
R1 Low 7" Select Shortcut Type – Make a Call
Make a Call – Contact Selection
Shortcuts
CCaallll AAlleessssaannddrraa
PPeerreezz
40

## p.41

Wireless Charger (ARM Only)
10.25’’ 12.3’’ – Wireless Charger Status Icon inside Phone screen and Phone Widgets
WC01) Wireless charger empty icon (black) is always shown on widget and inside phone screen. If there is no phone on wireless charger
pad, no colored icon is shown.
WC02) If there is a phone on wireless charger pad, the icon on widget and inside the phone screens becomes:
• Blue if phone is charging
• Green if phone is fully charged
• Blinking Red for system fail or foreign object - The blink has a timeout (refer to VF to know the tval), after this timeout the icon
becomes solid until the fail is solved.
41

## p.42

Wireless Charger 2 (ARM Only)
Example of system fail or foreign object, the red icon will blink.
42

