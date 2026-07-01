Event Plugin Commands
=====================

This page will document important Plugin Commands used in OMORI, and
their functions. These can be used by selecting the Plugin Command
option in the Rpgmaker event block, and then typing in the commands
below. **USAGE OF THESE COMMANDS REQUIRES RPGMAKER MV**

.. figure::
   https://user-images.githubusercontent.com/87251065/204021804-74aa7d1d-8054-426e-84f8-8979893a9991.PNG
   :alt: plugin

   plugin

Dialogue
~~~~~~~~

*NOTE: Dialogue in OMORI is stored in yaml files in the languages
folder, and are organized by message numbers (usually). A template yaml
can be found in the decrypted game files or*
`here <https://github.com/saikedemon/omori-modding/blob/main/00_template.yaml>`__
*if you are struggling to figure it out.*

| ``ShowMessage file.messageId`` - This will display a dialogue box with
  the selected message.
| EXAMPLE: "ShowMessage dw_boss_rush.message_1" will show the message
  "message_1" in the dw_boss_rush.yaml file.

Choices
~~~~~~~

``AddChoice file.messageId Label`` - This will add a choice with the
text of the selected message, and jumping to the Label "Label" when
selected.

EXAMPLE: ``AddChoice XX_GENERAL.message_4`` Label1 will add a choice
displaying the text "YES", jumping to the label "Label1" when selected.

*NOTE: Labels are another option in RPGMaker's event block menu. I would
advise familiarizing yourself with how they work before attempting usage
of this command and the ShowChoices command below.*

``ShowChoices [AMOUNT]`` - This will show choices that were created
using the AddChoice command, up to a set amount. This is needed to make
the choices selectable. The amount starts from 0 and goes up.

EXAMPLE: ShowChoices 1 will show up to 2 choices created, rather than 1.

{% hint style="info" %} Extra Note for Choices:
**``XX_GENERAL.message_4``** will always be "YES" and
**``XX_GENERAL.message_5``** will always be "NO", unless manually
modified. {% endhint %}

Camera Movement
~~~~~~~~~~~~~~~

*NOTE: [SPEED] is an extra parameter for a number representing how fast
the camera moves. 800 is the default, lower numbers increase the speed
while higher numbers decrease it. If you choose to not include the
parameter entirely, it will be set to its default, 800.*

| ``CAM PLAYER [SPEED]`` - Focuses the camera onto the player.
| EXAMPLE: "CAM PLAYER" Moves the camera to the player at the default
  speed.

| ``CAM EVENT ID [SPEED]`` - Moves the camera to an event. The event ID
  is the number at the bottom right of the screen after selecting an
  event.
| EXAMPLE: "CAM EVENT 7" Moves the camera to event 7 at the default
  speed.

| ``CAM X Y [SPEED]`` - Moves the camera to the x and y coordinates set.
  Self explanatory.
| EXAMPLE: "CAM 5 9" Moves the camera to the position [5, 9] at the
  default speed.

``CAM DISABLE`` - Disables custom camera movement, returning it to
rpgmaker default (the camera follows the player).
