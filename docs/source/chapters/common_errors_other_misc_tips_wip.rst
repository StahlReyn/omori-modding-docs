Common Errors & Other Misc. Tips - WIP
======================================

[This segment still needs to be properly styled.]

This short section here will be to cover some common errors and tips
that didn’t quite fit elsewhere.

.. _h.iozhgd9xiinu:

Common Crashes/Errors
---------------------

$atlasData is not Defined

This one is probably the most common error in modding. It happens on
bootup whenever you have an invalid YAML file. More specifically, you
have duplicated keys. This is most commonly because you copied a message
but forgot to rename it, so you may have 2 message_23s. Simply rename
these and it’s fixed. It can also occur if you define the same parameter
twice in a single message, such as two facesets.

Cannot read property ‘tilewidth’ of undefined

This error is also well known. It occurs when a rotated or mirrored tile
is loaded. You most likely did this by accident by fat-fingering the
Z key while mapping. This is the hotkey to rotate a tile. You can simply
replace these rotated tiles with their normal version to fix this. A
reminder that the bucket tool counts rotated tiles as different from
normal ones in case you have to search for a solid color rotated tile.

You can also outright remove the hotkey in Edit > Preferences > Keyboard
> RotateRight.

Cannot read property ‘hp’ of null

This error is the first to require a plugin to fix. If you enter a
battle without Omori or Sunny, the game will crash as it is trying to
get their hp in order to determine whether to show the low hp overlay or
not. To fix this, you’ll want to install the
\ `Nomori <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/ESSENTIAL%2520plugins/rph.no%2520omori%2520crash.patch.js&sa=D&source=editors&ust=1782966892600228&usg=AOvVaw1DTRwGchdJpeYAztFb2txW>`__\  plugin.

Cannot read property ‘Window_ScrollingTextSource’ of undefined

This error is caused by the XX_Blue.yaml file being missing. This
happens in some pirated copies of the game which run on older versions.
Updating to the Steam 1.0.8 version will fix this issue.

Failed to Load: img/pictures/OMORI_RS.png \| ERR_FILE_NOT_FOUND:
OMORI_RS.png

This error occurs if you load up the game with
FD_EasyTitleScreen without configuring the Plugin Parameters. Simply go
into the Plugin Manager and either assign the images to what you want or
delete them. In addition, if you want to see the assets in use they are
also accessible next to wherever you downloaded the plugin from, and you
can add them to img/pictures.

Failed to Load: img/faces/default_face_image_here.png /
ERR_FILE_NOT_FOUND: default_face_image_here.png

This error occurs if you load up the game with Save Load Plus without
adding a default image. The Save Load Plus menu hardcodes a list of the
actor IDs and what image to use for each, before falling back to
default_face_image_here. You can simply add an image to img/faces with
that name and it’ll be fixed.

Failed to Load: img/faces/06_SUNNY_HOUSE_BATTLE.png /
ERR_FILE_NOT_FOUND: 06_SUNNY_HOUSE_BATTLE.png

This error occurs if you have saves from other mods in your save folder
without having the mod loaded. The example shown here is a face from
\ `Pink Tinted Love
Stories <https://www.google.com/url?q=https://mods.one/mod/pinktintedlove&sa=D&source=editors&ust=1782966892602158&usg=AOvVaw2-rENRUyufuabjAdAOEudI>`__\ ,
but this can happen for nearly any mod with custom faces. To fix this,
install the \ `Mod Save File
Fix <https://www.google.com/url?q=https://mods.one/mod/modsavefiles&sa=D&source=editors&ust=1782966892602314&usg=AOvVaw1yB3nowAKtZchTcDoLlWQK>`__\ .

“I can’t see the player when I start the game!”

Make sure that in your starting map you add an Autorun event to disable
player transparency when they load in.

“My actors don’t have a turn in battle!”

This error is a result of really weird hardcoding in the game, which
forces the turn order to just the Headspace or Faraway party IDs. To fix
this, use either
\ `Geo_AutoTurnOrder <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/ESSENTIAL%2520plugins/Geo_AutoTurnOrder.js&sa=D&source=editors&ust=1782966892602908&usg=AOvVaw2p5g23273WXIBaU3VQXftr>`__\  to
set the turn order by their BattleStatusIndex notetags or their position
in the party, or use
\ `ActualTurnOrder <https://www.google.com/url?q=https://mods.one/mod/actualturnorder&sa=D&source=editors&ust=1782966892603086&usg=AOvVaw1xaLkPkS42PI6qrRAN9fHz>`__\  to
set the turn order based on the speed of each party member.

“I can move during my cutscene!”

Make sure that during your cutscene, you run it through an Autorun
event, which blocks player movement while active. Make sure to also
disable this event at the end of the cutscene.

“My event isn’t running automatically!”

Make sure that you set it to Autorun or Parallel. If you set it to
Autorun, make sure to also disable the event after it’s completed.

“My picture is showing under the characters!”

This error is a result of a plugin in OMORI which makes all Pictures
with the ID 1 be displayed as Below Characters. Simply changing the ID
to any other number should fix the problem.

“I have an event that changes a character’s sprite, but they disappear
for a bit before switching!”

This is a result of the image taking time to load. To alleviate this
issue, add a Script command shortly before the switch with the script:

ImageManager.loadCharacter(“IMAGENAME”);

This will load the image into memory, which will reduce the loading time
when it actually gets swapped out.

.. _h.y4naka5n9es6:
