Common Scripts
=======================

The following contains notes and scripts that commonly appears
in many places in development. This is not an exhaustive list.


RPGMV Variables
-----------------------------------

Basic common data getters and setters. These are scripts
but commonly used in-line in conditionals.

Get current Map ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  $gameMap._mapId
  this._mapId // In event page

Get current Event ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  this._eventId
  this.eventId() // In event page

Get current Player Position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  $gamePlayer.x
  $gamePlayer.y

Self-Switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  $gameSelfSwitches.setValue([mapId, eventId, letter], value)
  $gameSelfSwitches.value([mapId, eventId, letter])
  
  $gameSelfSwitches.setValue([this._mapId, 4, 'C'], true); // In same map, set event 4 self switch C on
  $gameSelfSwitches.value([this._mapId, 4, 'C']); // Check value of event 4 self switch C (true if on)

Variables and Switches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript
    
  $gameVariables.setValue(id, type);
  $gameVariables.value(id, type);
  $gameSwitches.setValue(id, type);
  $gameSwitches.value(id, type);


RPGMV Script Block
-----------------------------------

These are larger scripts usually used in Script blocks.

Bulk Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Directly inserting lines into an event with script allows using
variables to insert multiple in a loop. For example:

.. code:: javascript

  let list = []
  for (let i = 10; i <= 50; i++) {
    list.push({code: 356, indent: 0, parameters: ['ShowMessage FILENAME.message_${i}']}) 
  } 
  $gameMap._interpreter.setupChild(list, $gameMap._ interpreter._ eventId)

This example runs showing message_10 to message_50 from ``FILENAME.yaml``.

.. note::

  OneMaker contains shortcut to generate this in the event page.

  For code number see RPGMV Documentation:
  https://kinoar.github.io/rmmv-doc-web/classes/game_interpreter.html


Setting Follower Location or Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Useful for setting follower location after cutscene.

Here's example of moving player to 18, 16, having everyone facing up and
behind the player:

.. code:: typescript

  $gamePlayer.locate(18, 16);
  $gamePlayer.setDirection(8);
  $gamePlayer.followers().follower(0).setDirection(8);
  $gamePlayer.followers().follower(1).setDirection(8);
  $gamePlayer.followers().follower(2).setDirection(8);
  $gamePlayer.followers().follower(0).setPosition($gamePlayer.x, $gamePlayer.y+1);
  $gamePlayer.followers().follower(1).setPosition($gamePlayer.x, $gamePlayer.y+2);
  $gamePlayer.followers().follower(2).setPosition($gamePlayer.x, $gamePlayer.y+3);

Add Battle Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds the text on the battle window. In OMORI this is the top window.

.. code:: javascript

  BattleManager.addText(text) 
  SceneManager._scene._logWindow.push("addText", text)
  // Window_BattleLog class also defines addText(text) 

This is commonly used with "EVAL:" in Skills action sequence in combination
of user and target variable. For example:

.. code::

  <setup action>
    eval: BattleManager.addText(user.name() + " attacks " + target.name())
  </setup action>

Whole Target targeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<whole action> tag only executes once, which means it only affects 
single target when ran through EVAL.

To make some action affect a group in single line do the following in the notes:

.. code::

  <whole action>
    eval: BattleManager.makeActionTargets('actors').forEach(x=>x.someStuff())
  </whole action>

Which executes ``someStuff()`` on all actors


Random Specific Number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here's an example of generating a random number to set to variable 1502.

.. code:: javascript
  
  let list = [709,711,712,714,715,721]; 
  let type = list[Math.randomInt(list.length)];
  $gameVariables.setValue(1502, type);

This is useful for specific list of number such as Troop IDs or States, removing
the need for long else if chain for each number case.

Change Game Speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the game run faster by how many times it processes in a single frame.
Useful while debugging, commonly ran in console.

.. code:: javascript

  SceneManager.determineRepeatNumber = function() { return 1; }




RPGMV Plugin Block
-----------------------------------

The following is used in the "Plugin" block in the Event page.

Show Message, Add Choices, Show Choices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  ShowMessage yaml_file.message_name ShowMessage 01_cutscenes_neighbor.message_1
  AddChoice yaml_file.message_name label AddChoice XX_GENERAL.message_4 YES
  ShowChoices num ShowChoices 2

Camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``[SPEED]`` is an optional parameter for a number representing how fast
the camera moves. 800 is the default, lower numbers increase the speed
while higher numbers decrease it.

``CAM PLAYER [SPEED]``
  Focuses the camera onto the player.

``CAM EVENT [ID] [SPEED]``
  Moves the camera to an event. The event ID is the number 
  at the bottom right of the screen after selecting an event.

``CAM [X] [Y] [SPEED]``
  Moves the camera to the x and y coordinates set.

``CAM DISABLE``
  Disables custom camera movement, returning it to default (camera follows the player).

  It may be good idea to pair with ``CAM PLAYER`` and ``Wait`` block first for smooth transition.

Event Notetags
-----------------------------------

The following are used in the Note field in the Event page located at top left.

Event Hitbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Units in tiles.

.. code::

  <Hitbox Up: x>
  <Hitbox Left: x>
  <Hitbox Right: x>
  <Hitbox Down: x>

Sprite Offset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Units in pixels. +X is right, +y is down.

.. code::

  <Sprite Offset X: +n>
  <Sprite Offset X: -n>
  <Sprite Offset Y: +n>
  <Sprite Offset Y: -n>
  <Sprite Offset: +x, +y>
  <Sprite Offset: -x, -y>


Activation Range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Give activation range, activating certain events from a distance.   

- Square: x tiles from center in a square shape. 
- Radius: x tiles from  center in a diamond shape. 
- Row: Horizontal bar to whole map, with x thickness. 
- Column: Vertical bar to whole map, with x thickness.     

`Event Proximity Activate (YEP) - Yanfly.moe                        
Wiki <http://www.yanfly.moe/wiki/Event_Proximity_Activate_(YEP)>`__ 

.. code::

  <Activation Square: x>
  <Activation Radius: x>
  <Activation Row: x>
  <Activation Column: x>

Copy Event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copies event, recommended to read in more detail in wiki. 
Commonly used by enemies. `Event Copier (YEP) - Yanfly.moe Wiki <http://www.yanfly.moe/wiki/Event_Copier_(YEP)>`__           

.. code::

  <Copy Event: Map x, Event y>
  <Copy Event: mapId, eventId>
  <Copy Event: template>

Save Event Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes it so event stays in same position even when reloading the map,
such as entering the map again or loading the save.

.. code::

  <Save Event Location>




Event Movement Script
-----------------------------------

The following are used in the Event Movement block in the event page.

Move To
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  MOVE TO: x, y
  MOVE TO: EVENT x
  MOVE TO: PLAYER

Move To
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  SELF SWITCH x: ON
  SELF SWITCH x: OFF
  SELF SWITCH x: TOGGLE

Custom Frame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Force sprite to use a specific frame, where (0,0) is top left.
Setting to null will revert to the default behavior.

.. code:: javascript

  this.setCustomFrameXY(x,y)
  this.setCustomFrameXY(null,null)

Sprite Offset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sets offset of the sprite in pixel. +X is left; +Y is down.

.. code:: javascript

  this._spriteOffsetX = 32
  this._spriteOffsetY = -32


Shaking / Trembling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  Fuku_Plugins.EventTremble.start(eventId, power, speed)
  Fuku_Plugins.EventTremble.stop(eventId)

  // Example Movement Route Script
  Fuku_Plugins.EventTremble.start(this._eventId,3,1)
  Fuku_Plugins.EventTremble.stop(this._eventId)



Omori Specific
-----------------------------------

YAML Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Script version of ShowMessage command

.. code:: javascript

  // Game_Message: showLanguageMessage(string) 
  $gameMessage.showLanguageMessage("XX_GENERAL.message_1");

Emotion Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Base game emotion checks. Note that this checks hard coded list of states.

.. code:: javascript

  // Game_Battler: isEmotionAffected(string) 
  $gameActor.actor(1).isEmotionAffected("happy")

  // Game_Battler: isAnyEmotionAffected()  
  $gameActor.actor(1).isAnyEmotionAffected()

Javascript
-----------------------------------

The following is useful JavaScript to know for general use.
This is intended for common JS that is used in places such as EVAL note tags in Enemy AI.

Arrays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Working with Arrays, common with AI evaluation.

.. code:: javascript

  every(callbackFn)
  // Example: Check if ALL switch 1,2,3 is on 
  [1, 2, 3].every((x) => $gameSwitches.value(x))

  some(callbackFn)
  // Example: Check if ANY of switch 1,2,3 is on 
  [1, 2, 3].some((x) => $gameSwitches.value(x)) 
  // Example: Check if ANY party member has weapon 203 
  $gameParty.members().some((actor) => actor.hasWeapon($dataWeapons[203]));

  forEach(callbackFn)
  // Example: Add Happy State to EACH Alive Enemies 
  $gameTroops.aliveMembers().forEach((enemy) => enemy.addState(5));
  
  reduce((accumulator, currentValue) => accumulator + currentValue, initialValue)
  // Example: Count amount of Happy Enemies 
  $gameTroops.aliveMembers().reduce((count, battler) => count + battler.isStateAffected(5), 0);


Get username of logged in user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: javascript

  const userName = process.env.WINEUSERNAME ? process.env.WINEUSERNAME : require('os').userInfo().username;

