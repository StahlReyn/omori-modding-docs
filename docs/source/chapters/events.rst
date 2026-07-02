Events
======



.. image:: ../images/image99.png
   :align: center



“What is an event?”

Well, an event is anything that happens in the game. Even the Player is
a type of event, but that’s a level of technical we’re going to ignore
for this.

To turn on the Event Editor, click the following button at the top of
your main RPG Maker MV window.



.. image:: ../images/image254.png
   :align: center



(source: FruitDragon)

.. _h.jloze3db1ozb:

Making Events
-------------

It is highly recommended that you look at events similar to the one you
are trying to make to figure out how they work before you try making one
of your own.

Also, you can always copy/paste events and then edit them.

To make a new Event, all you have to do is double click any empty square
in the Event Editor. You’ll get a new page that looks something like
this:



.. image:: ../images/image238.png
   :align: center



(Source: FruitDragon)

There’s a few important things to note when we’re talking about Events.
First, you can see just how many things there are to consider. This is
because of just how specific Events can be.

We’ll go over almost all the sections in detail.

.. _h.lh8uiqwbjm3z:

Event Page - The Top
~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/image91.png
   :align: center



It’s pretty self-explanatory. An Event can have multiple pages, and this
is where you can make a new event page, copy an existing event page to
paste somewhere else or duplicate in the same event, or delete/clear an
existing event page.

Of course, there’s always the option to name your event. And the notes
box is used for things like extending the Hitbox of the Event or
changing the X/Y-offset of the event.

Some of the possible Notetags that can go in the notes box:

Hitbox changers:

<Hitbox Left: 2> (extends the hitbox left 2 squares)

<Hitbox Right: 4> (extends the hitbox right 4 squares)

<Hitbox Up: 1> (extends the hitbox up 1 square)

<Hitbox Down: 1> (extends the hitbox down 1 square)

Sprite Offset: (positive means right/down, negative means left/up)

<Sprite Offset Y: +20> (sprite moves 20 pixels down)

<Sprite Offset X: -3> (sprite moves 3 pixels left)

<Sprite Offset: +7, -5> (sprite moves 7 pixels right and 5 pixels up)

Note: This does NOT change the hitbox of the event.

Copy Event: This basically copies the entirety of an event from one map
and adds it to another. Good for events like a specific enemy that you
want consistent across multiple maps.

Note #1: You will run into events with Copy Event tags that don’t
specify the event they’re copying. Those events are selected with the
help of plugins. You can usually find the event that they’re copying in
the Dev Rooms.

Note #2: Maps you copy events from must be added to a list of maps to
preload in YEP_EventCopier in the Plugin Manager. Where that is and how
to modify stuff like that can be found in the
\ `Plugins <#h.rxmxx9evltp>`__\  section.

<Copy Event: Map 46, Event 3> (acts the same as Event 3 in Map 46. If
you want to know what event this is, it’s the door to Basil’s room in
Faraway Town.)

Activation changers: Extends the area a event can be triggered by Player
Touch or Event Touch, explained later.

<Activation Square: 4> (extends the area the event can be triggered by
player or event touch is extended by 4 units in a square shape.)

<Activation Radius: 2> (extends the area the event can be triggered by
player or event touch is extended by 2 units in a diamond shape.)

Mini Label: Causes a small line of text— the “mini label”— to show up in
the game above the event. This is used pretty much exclusively in the
dev rooms, for organization purposes.

<Mini Label: label goes here>

It’s also important to note the ID number at the top of the Event page.
That ID number is important for Scripting later. Sometimes, it’s a good
idea to include the ID number when naming the event, so that it’s easy
to tell the number without having to open the Event page every time.

.. _h.ydhbn486qsq2:

Event Page - Conditions
~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/image138.png
   :align: center



(Source: FruitDragon)

These tell you what Conditions need to be fulfilled in order to run that
particular event page. Since there can be multiple event pages in an
event, this helps to differentiate things.

Quick Guide:

- Switches are true/false statements you can use to trigger events. You
  may also know these as flags or booleans.
- Variables are just that— variables.
- Self Switches are true/false statements specific to the event you’re
  currently coding. These aren’t meant to be used for multiple events,
  but with Scripting you can do so. More on this later.
- Item: This means the player has to have that particular item in their
  inventory. This cannot check for equipment.
- Actor: That means that the event runs only if that specific actor
  (character) is in the player’s party.  To check for a tagged actor,
  place a Conditional Branch that checks the following script
  “$gameParty.leader()._actorId === ACTOR ID”

Event Pages run from left to right in priority, so if the Conditions of
Event Page 4 and Event Page 6 are both met, it will run Event Page 6 as
that one has the highest priority.

Here’s some examples:



.. image:: ../images/image18.png
   :align: center



(Source: FruitDragon)

This set of Conditions means that the Event Page won’t run unless the
Switch Mom’s Broom Equipped is true— basically, it won’t run unless the
player equips Mom’s Broom.



.. image:: ../images/image69.png
   :align: center



(Source: FruitDragon)

This set of conditions means that the event page will run when the
player has started sorting and the Self Switch A was triggered.



.. image:: ../images/image287.png
   :align: center



(Source: FruitDragon)

This set of Conditions means that the event page will run when Omori is
in the party and you are holding an item. (This particular one is
impossible in the vanilla game— since the Holding Item Switch is
specific to the sorting chore in Sunny’s house.)



.. image:: ../images/image137.png
   :align: center



(Source: FruitDragon)

This one means that the event page will run when the save’s WTF Value is
greater than or equal to 10 and the Mystery Potion is in the player’s
inventory.

.. _h.xn0oirjpe53f:

Event Page - Image
~~~~~~~~~~~~~~~~~~



.. image:: ../images/image58.png
   :align: center



(Source: FruitDragon)

This one’s also pretty self explanatory. When you double click on the
gray and white checkered box, it’ll summon an image selection window.



.. image:: ../images/image120.png
   :align: center



(Source: FruitDragon)

From there, you can select a sprite from the img/characters folder to
use as the image for the sprite.



.. image:: ../images/image57.png
   :align: center



(Source: FruitDragon)

These are typically found in the basic walking animation groups of 3 x
4— however, in some cases (like the one above), there are some
animations that require fewer sprites. To see exactly how those work,
you can skip ahead to the \ `Sprites Section <#h.gsbdya7y8lgi>`__\ .

There are also some unusually shaped spritesheets in the folder, and
those will look very strange when selecting, because they’re used with
the help of plugins.

Here’s a common one that is used aside from actual character sprite
sheets, usually for dev purposes:



.. image:: ../images/image112.png
   :align: center



(Source: FruitDragon)

The boxes on the far side are used to denote where Tag Events, Camera
Events, Teleport Events, Initializing Events, Enemies, and more are on
the map, since it’s hard to tell these types of events apart
otherwise. DEV\_ sheets don’t appear in-game, so you don’t have to worry
about a random INIT box showing up in the middle of Forest Playground or
something.

.. _h.sroolriinfxy:

Event Page - Autonomous Movement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This box is used to decide where the Event moves when it’s not being
triggered.



.. image:: ../images/image226.png
   :align: center





.. image:: ../images/image240.png
   :align: center





.. image:: ../images/image271.png
   :align: center





.. image:: ../images/image23.png
   :align: center



(Source: FruitDragon)

Honestly, they’re pretty self-explanatory.

You can look at the Forest Playground cutscenes to see most of their
advanced capabilities.

.. _h.wczems5bw6cc:

Event Page - Priority
~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/image282.png
   :align: center



(Source: FruitDragon)

Priority is what layer of the map the event is on.

Below characters means it’s below the characters’ feet.

Same as characters means it’s on the same layer as the characters, as
though it were a solid obstacle in their path.

Above characters means that it’s above the characters’ heads, so they
can walk underneath without issue.

.. _h.yxr49f829h9e:

Event Page - Trigger
~~~~~~~~~~~~~~~~~~~~

.. _h.w2h3l2mtyci7:

 

.. image:: ../images/image44.png
   :align: center

 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Source: FruitDragon)

This determines how the event gets triggered.

Action Button means the player has to activate it using the action
button (Z by default for OMORI). If the event is Above characters or
Below characters, this means they’ll have to stand below it/on top of it
and press the action button to activate it, while Same as
characters means the player needs to face it from the side and use the
action button.

Player Touch means the player has to touch the event ( and face the
event if it’s Same as characters) to activate it. Can also be triggered
the same as Action Button.

Event Touch means the event can touch the player to activate itself.
(The player does not need to face the event.) Can also be triggered the
same as Action Button or Player Touch.

Autorun means that it runs automatically the moment its conditions are
fulfilled. This also locks all player movement until the event changes
pages or is deleted.

Parallel means that the event page runs at the same time as whatever
other event page is running at the moment on that map. Player movement
will not be locked.

.. _h.hfiblx21xj8y:

Event Page - Options
~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/image97.png
   :align: center



(Source: FruitDragon)

Walking means that the walking animation is turned on when the event is
moving, and only then.

Stepping means that the walking animation is turned on even when the
event isn’t moving.

Direction Fix means that the character in the event can’t change
direction. Useful if you want to make a character walk backward without
having them turn around, or if they only have sprites for one direction.

Through makes it so the character can pass through normally impassable
objects, tiles, and events.

.. _h.m3vv65v4pqh8:

Event Page - Contents
~~~~~~~~~~~~~~~~~~~~~

And finally, we reach the last part of the Event Editor.



.. image:: ../images/image186.png
   :align: center



(Source: FruitDragon)

This empty box is where the code goes.

“But…” you ask, “what code? What can we even put here?”

Well, dear future OMORI modder, I’m glad you asked! Because that’s our
next topic!

.. _h.n9a33t54rq48:

Event Code
----------

This section is going to be a lot of summary, mostly, since there’s
plenty to go through. For more in-depth, detailed explanations, ask
someone in the \ `Mods.one Discord
Server <https://www.google.com/url?q=https://discord.gg/EDTMF85Hnp&sa=D&source=editors&ust=1782966892321465&usg=AOvVaw2PYq9pQ3lwAkAJ7tdc2wRW>`__\  or
the \ `OMORI Modding
Hub <https://www.google.com/url?q=https://discord.gg/pkBEr7ywCG&sa=D&source=editors&ust=1782966892321580&usg=AOvVaw385Lc3ygdr0RxTCTQE2vZ0>`__\ ,
perhaps one of us.

When you double-click on the Contents box, you get the following menu,
with three pages of options:



.. image:: ../images/image13.png
   :align: center



(Source: FruitDragon)

Many of them are self-explanatory, especially if you already know how to
code, so I’ll just go over a few that are used often in OMORI and a
couple that are more specific to RPG Maker MV.

.. _h.5n2z0ej0bphn:

Event Commands - Message
~~~~~~~~~~~~~~~~~~~~~~~~

This is a special case. OMORI uses a different system of displaying text
and choices and the like. Therefore, don’t use any of these. Instead,
you would use a Plugin Command, located down below.

.. _h.5r195mh62ho2:

Event Commands - Game Progression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are all really important, as they are how you can set Switches and
Self Switches on and off, as well as change the values of Control
Variables and set up a timer using real-life time instead of in-game
frames.\ `[c] <#cmnt3>`__\ :sup:`\ `\ `[d] <#cmnt4>`__

.. _h.2zq34t7fixyq:

Event Commands - Flow Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comments are useful in being able to tell what is happening on an event
page, oftentimes to label a Script.

Conditional Branches (or If-Then/If-Else statements) are extremely
useful in making certain things in events happen only when certain
conditions are met. They’re basically the same as if-else statements in
the majority of programming languages.

Exit Event Processing— Essentially terminates the event in the middle.
Like pressing a big red “STOP” button. This will not end the
Autorun player lock, you have to change Event Pages or delete the event.

Label and Jump to Label are the kinds of things that are much better
understood through looking at example events, but I’ll do my best to
explain.

They act as headers that allow you to skip large amounts of code.

Because of the linearity of RPG Maker MV’s code windows, going from top
to bottom, it’s incredibly hard to make it so that portions of code get
passed over without the use of Conditional Branches. Labels solve that
problem. You place a Label somewhere in the code, place a Jump to
Label for that Label somewhere else in the code, and then you can have
the code go straight from the Jump statement to the Label without
running anything in between. It works the other way, too— it lets you
repeat sections of code without having to use a loop. Labels are usually
used in tandem with Conditional Branches. (They are also often found
with the Plugin Commands AddChoice and ShowChoices)

Lastly are Common Events. These are much more complex so we will give
them their own section.

.. _h.8hsacdxrvfa6:

Common Events Vs. Map Events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Common Event is an event that can be called in multiple places, like
reusable code, or a function/method for those already experienced in
coding. As mentioned in the \ `YAML Section <#h.eyo0h7t5nx1p>`__\  of
this guide, it can also be called by the dialogue. Examples of this
include the Shake Screen event, the Picnic Save event, and more— all
things used in multiple places, so the code doesn’t have to be copied
over each time. Events that aren’t specific to a location can also be
put here. An example of this is the Tag System event in the basegame,
shown below:



.. image:: ../images/image126.png
   :align: center



(source: FruitDragon)

Since tagging occurs when you use the Tag option in the menu, and not
when the player interacts with an object, it’s put as a Common Event so
the menu can call it.

A Map Event is an event that occurs in only one place on the map and is
usually much more specific. Examples of this include Cutscenes and Map
Transitions, since Map Transitions need specific coordinates and
Cutscenes require specific characters and dialogues.

An important thing to note is that Map Events can call Common Events,
but Common Events can’t call Map Events. That being said, Common
Events can call other Common Events.

.. _h.emb55q2fjdi:

Parallel Common Events
^^^^^^^^^^^^^^^^^^^^^^

Now to go another layer deeper, there are three types of Common Events,
based on their Trigger conditions.

Most Common Events are triggered by Map Events and we’ll call these
Regular Common Events, as you will primarily see these throughout the
game and most mods. However there are two other types, being Autorun and
Parallel Common Events, which we will group as Automatic Common Events.
Unlike Regular Common Events, these are not called by Map Events and
instead run when a Switch is active. Autorun Common Events will lock the
player’s movement while active, and Parallel Common Events will run in
parallel to the player and Map Events. They are both very useful for
systems that you want passively occuring across many maps so that you
don’t have to have multiple Map Events running the same code across
different maps, which can be a problem if you need to change all of
them.

It’s also worth noting that Automatic Common Events can be called from
Map Events like Regular Common Events are, albeit this rarely sees use.

.. _h.u9hmorpbrltg:

Making Common Events
^^^^^^^^^^^^^^^^^^^^

To create a Common Event, all you need to do is find an open Common
Event slot in the Database and put your code in. In addition, to assign
it the types listed above, you’ll want to change the Trigger option to
the desired mode, with None being a Regular Common Event, and then
assigning a Switch to control the activity of Automatic Common Events.



.. image:: ../images/image288.png
   :align: center



(Source: FruitDragon)

Of course, don’t forget to name it! That’s how you’ll be able to
identify the Common Event when you’re trying to call it later on.



.. image:: ../images/image270.png
   :align: center



(Source: FruitDragon)

Otherwise, adding code is basically identical to coding in Map Events,
so let’s return to those!

The only significant thing to note is that any commands that apply to
the Map Event itself (Self Switches, Movement Routes, etc.) apply to the
Map Event that called the Common Event that called it. Automatic Common
Events by proxy don’t support these commands.

.. _h.c9e51ad7t4ma:

Event Commands - Movement
~~~~~~~~~~~~~~~~~~~~~~~~~

I’ll specifically talk about Set Movement Route here. This is how you
can get characters to move around in cutscenes. When you click on it:



.. image:: ../images/image80.png
   :align: center



(Source: FruitDragon)

Movement Routes are highly versatile. All of these options are mostly
self-explanatory, so I will instead focus on options provided by the
Script option. These scripts come from the
\ `YEP_MoveRouteCore.js <https://www.google.com/url?q=http://www.yanfly.moe/wiki/Move_Route_Core_(YEP)&sa=D&source=editors&ust=1782966892330803&usg=AOvVaw2cgZpdV0-6yCB1O5dI8XHd>`__\  plugin,
so you may see more options in there. I will cover the basics.

UP: x

LEFT: x

RIGHT: x

DOWN: x

UPPER LEFT: x

UPPER RIGHT: x

LOWER LEFT: x

LOWER RIGHT: x

JUMP FORWARD: x

All of these will move the event in the stated direction for x tiles.

MOVE TO: x

JUMP TO: x

STEP TOWARD: x

STEP AWAY FROM: x

TURN TOWARD: x

TURN AWAY FROM: x 

TELEPORT: x

All of these are self-explanatory, but X operates specially here. x can
be either x, y for exact map coordinates, EVENT X, for the event with an
ID of X, or PLAYER for the, well, I think you can guess.

.. _h.cpsecgbzymtx:

Event Commands - Character
~~~~~~~~~~~~~~~~~~~~~~~~~~

I’ll specifically talk about Show Balloon Icon and Erase Event.

Show Balloon Icon: Shows that icon that sometimes pops up in a cutscene
to show a character’s mood.

Note: To get this command to work correctly, you’ll have to set two
things. You’ll have to set the Control Variable “Change Balloon
Variable” to 0 and then run the Common Event “Balloon Image.” This only
needs to be run once.

The source images can be found in img/system/balloon.png



.. image:: ../images/image176.png
   :align: center



Erase Event: Erases the event for the duration of the player’s stay on
the current map. The event will be brought back when the player leaves
and comes back to the map.

.. _h.ic5ln0yyl9ub:

Event Commands - Picture, Audio & Video
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are all used for cutscenes and sound effects. Take a look at some
of the events with cutscenes (Especially the INIT Event in the “❈ >>
BEGIN” map) to find out how they work.

Acronym meanings:

BGM - Background Music (video game soundtrack) [Loops]

BGS - Background Sounds (like ambient noise) [Loops]

SE - Sound Effects (like a door opening) [Doesn’t Loop]

ME - Music Effects (when an ME is playing, all sounds aside from the
ME are paused) [Doesn’t Loop]



.. image:: ../images/image170.png
   :align: center



(Source: FruitDragon)

And now for the third and final page. I’m only gonna cover the
Advanced section, since the rest are all pretty self-explanatory.

These are a lot more in-depth than the rest, though, so I’ll talk about
them individually.

.. _h.datv5m12g97r:

Plugin Command
--------------

OMORI has a lot of plugins. All you have to do is visit the Plugin
Manager, located next to the Database, to see that. All Plugin
Command does is take a command meant for one of the plugins and runs it.

Probably most used is the ShowMessage plugin command, which is used to
run… dialogue.

We’ve come full circle.

.. _h.kwpdo5k2ky8n:

Dialogue
~~~~~~~~

We’ve talked about how to write dialogue in the .yaml files. But now
it’s time to talk about how to run said dialogue in the game itself.



.. image:: ../images/image14.png
   :align: center



(Source: FruitDragon)

When we click on Plugin Command, we get the above window. All you have
to do is enter the below text:



.. image:: ../images/image218.png
   :align: center



(Source: FruitDragon)

Replace file_name with the name of the file you want to get the message
from (e.g. 00_template) and XX with the number of the message.

And that’s it! When you trigger the event in the game, the dialogue will
show.

.. _h.dzkh81t39vca:

Dialogue Options
^^^^^^^^^^^^^^^^

Now, you may know, actually you should know, that OMORI has multiple
instances in which the player must make a choice in the dialogue. This
will usually dictate what is said next. Well, these are done with Plugin
Commands as well. This time there are two.

The first of these commands is the AddChoice command. This adds your
dialogue to be called later. To use it, place this text.

“AddChoice file_name.message_XX label”

The middle section is the same as regular dialogue, except now, it’s
what message the option will show as. Then there’s the label. If you
remember from above, labels are markers in RPG Maker MV events that can
be jumped to in order to skip or loop code. In this context, each
dialogue option will basically act a Jump To Label command to the
specified label, which you input in place of the word label. Now you
just do this for all of your dialogue choices.

Then we need to actually display the choices. This is done with the
ShowChoices command. Simply add the command and then the number of which
choice would be selected if the player were to click “X” or “Cancel”.

Note: It starts from 0, so if you want the second choice to run if the
player clicks cancel, you actually have to put 1. It’s kinda weird but
it’s just how computers are. If you want the player to not be able to
press cancel to skip a dialogue choice box, you can type -1 instead.

And now you know how to fully use dialogue. Congrats!

.. _h.3x1tjmpwqtpn:

Camera Controls
~~~~~~~~~~~~~~~

The other common use for Plugin Commands is to control the camera. This
is done through four mostly self explanatory commands.

Note: The way speed works is slightly counterintuitive. Higher numbers
actually decrease the speed and vice versa. The default is 800, which is
what will be chosen if you exclude Speed from the command.

CAM PLAYER SPEED: Follows the player at the chosen speed.

CAM EVENT ID SPEED: Follows the chosen event at the chosen speed.

CAM DISABLE: Resets the camera to follow the player at default speed.

.. _h.u6hcehxl07t0:

Weather
~~~~~~~

While base RPG Maker MV does have a command for weather effects, OMORI
uses a much more in-depth plugin to control its weather. The plugin
consists of three plugin commands to change the weather and uses six
weather types, those being rain, storm, snow, embers, shine, and leaves.

AriesSetWeatherImage weather filename

This determines what image the game will use for the specified weather
type, pulled from the img/pictures folder. OMORI, despite only using
rain, storm, and snow, also has images for the other three types that
you can use. However you may also use your own images for this.

AriesToggleStormThunder boolean

This is a true or false that determines whether the storm weather type
will show flashes of thunder periodically.

AriesWeather weather power duration

This is what actually sets the weather. Power is a number 1-9 that
dictates the intensity of the weather. Duration is the number of frames
it takes for the weather to fade in.

.. _h.3e2f57whopyw:

Scripts
-------

Scripts are powerful. They let you do things that vanilla RPG Maker
MV doesn’t let you do. Sure, you theoretically have to know Javascript…
but that’s also why looking at pre-existing events is so important. You
can puzzle out and copy their scripts, if applicable. That’s less work
for you, and you don’t need to know Javascript. You just need to know
how to figure out what code does.

A lot of things in the game use Scripts to set variables for things such
as teleportation. Scripts can also be used to set Self Switches of other
events. And these are just a few examples. Like I said, seriously
powerful stuff.



.. image:: ../images/image96.png
   :align: center



(Source: FruitDragon)

An example of a Script commonly found in the game. This script is used
for setting the variables used to teleport from map to map.

Note: RPG Maker MV has a built-in cap of 12 lines in a Script command.
Due to Omocat working with Archeia, a developer for RPG Maker MV, she
got a customized version to bypass this. So if you see a 13+ line Script
command, do not edit it or else it will be cut off and
broken.\ `[e] <#cmnt5>`__\  That being said, however, you can bypass
this restriction with the recently released RPG Maker MV mod \ `OneMaker
MV <#h.4a99xvlix9d1>`__\ .

Other commonly used scripts include scripts for picture cutscenes, for
better follower control, and scripts for setting variables and switches.
For a full list of nearly all the possible scripts you can use, visit
\ `this official
spreadsheet <https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/1-Oa0cRGpjC8L5JO8vdMwOaYMKO75dtfKDOetnvh7OHs/edit?gid%3D1186334695%23gid%3D1186334695&sa=D&source=editors&ust=1782966892342768&usg=AOvVaw1sUjuRa_oHV_WmGV0DHwir>`__\ .

.. _h.30ui65nu67ka:

Animated Events
~~~~~~~~~~~~~~~

Sprite animation is a pretty large topic, so I’m only going to go over
the basics here.

Usually, it’s done by setting the sprite to a certain section of the
spritesheet and turning the sprite back and forth and left and right so
that the images that you want show up, or by setting them manually with
a Script command. For a guide on which images are in which direction,
just look at the walking animation found for nearly every NPC in the
game.

Here’s an example of a script found when opening doors:



.. image:: ../images/image169.png
   :align: center



(Source: FruitDragon)



.. image:: ../images/image234.png
   :align: center



(Source: !objects_fa_doors.png, basegame)

Here’s what the spritesheet looks like, so you can see how it works.

For more complex animations, you can use this script:

script: this.setCustomFrameXY(x,y)

Note: The word “this” in this context is the event the code is being run
from. If you want to set the animation of another event, you’ll have to
replace it with the script call for that, which is
$gameMap.event(eventId). When putting this in a movement route for that
event, however, you would return to using this.

This script sets an Event to an exact frame in their sheet. It’s used
for most complex animations in the game. To cancel out these custom
frames, use this.setCustomFrameXY(null, null). A good example to look at
are the hugging animations.

It’s usually a good idea to look for examples of animations that you
want to make elsewhere in the game so you have an idea of how you’re
going to animate what you want to animate.

.. _h.vehgwrux8uzj:

Shops
~~~~~

Shops are strange little things, since they don’t really appear much.
Nonetheless, I’ll explain how to set them up.

First off, assuming you’re making a shop with new dialogue, you’ll have
to write all of that dialogue. This dialogue has to be placed in
System.yaml. The easiest way to do this is just copy paste one of the
pre-existing dealers and just change their name and their dialogue.

Note: You’ll notice that most of the Faraway Town dealers call for other
yaml files. This is a requirement.

Now we’re going to actually make our shop. First things first, make your
new event and add whatever beginning dialogue or other stuff you want.
Then, once you get to the point of buying or selling, make a dialogue
selection between Buying, Selling, and Cancel. You can refer to the
above sections on how to do that.

Now, in the Buying section, we’re going to use a Script Command, that
being “this.setupShop('name', 0)” What this does is it tells the game
what dialogue it should be showing, which is done through the ‘name’,
which should be the name you gave your dealer in the System.yaml file.
Then the 0 tells the game you are buying. Now just use the Shop
Processing Command to add all your items and set their prices. Make sure
to not tick the “Purchase Only” box. It doesn’t work in OMORI.

Then, for Selling, we’re going to do all of that the exact same, except
for one change. We’re going to replace the 0 with a 1, to tell the game
we are selling instead of buying. You’re still going to need the Shop
Processing by the way, even if it does nothing when selling, since it’s
what tells the game to actually pull up the shop menu.

Lastly for Cancel, you just end the event. Not much to say about it.

Also if you want to add a portrait for your dealer, you’ll have to mess
with plugins to do that, or use
\ `TR_PictureShops <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/Data%2520Organization%2520Plugins/TR_PictureShops.js&sa=D&source=editors&ust=1782966892347341&usg=AOvVaw31CDcnxbOZtCL0vGJ9rlE8>`__\ .
Honestly, though, it’s not super important, as only the Mailbox has a
portrait in OMORI.

.. _h.9j8d825dwjpk:

Animated Pictures
~~~~~~~~~~~~~~~~~

In OMORI, pictures get animated all the time for various cutscenes, such
as the White Space intro. The game will also store multiple pictures
together in one sheet, and yet be able to only use one frame of it. So
how does it do that?

The answer is that it uses scripts.

The first thing we need to do is to create the picture we want to
animate. Simply use the Show Picture command and preferably set the
opacity for the time being to 0. Also make sure to keep in mind the ID
you are using. The higher IDs will always display higher, and an ID of
1 displays below the characters.

Now we can begin to script.

Firstly we need to define to the game what the divisions are between
each frame, so we use this script:

this.setupPictureCustomFrames(id, width, height, hframes, vframes);

Now let’s break down what each of those are.

The id is simply the ID of the picture you’re applying the frames to.

The width and height are the pixel widths and heights of the ENTIRE
image, not just one frame.

The hframes and vframes are the amount of horizontal and vertical frames
in the image.

Now what we add after is dependent on what we’re doing.

If you’re just setting a single frame of an image, like say a lighting
overlay, use this;

this.setPictureFrameIndex(id, frameId);

Once again id is the picture ID, meanwhile frameId is the ID of the
frame. Frame IDs are ordered from left-to-right, top-to-bottom, starting
at 0. So the top left is 0 and then the one to the right is 1 and so on.

However if you’re setting an Animation, then use this instead;

this.setPictureAnimation(id, frames, delay, loops, wait);

Alright now let’s break this down again.

First up the id is the same as always, the Picture ID.

Next is the frames. This is an Array of the frameIds that you want the
animation to go through. For those who don’t know, an Array in
JavaScript is a list of values stored as a variable. They look like
this: [value,value,value,value] So if you want to have your frames go
from 0-6, then your frames will look like [0,1,2,3,4,5,6].

The delay is the number of frames (as in your monitor’s fps) that it
takes to update from one frame to another.

The loops determines how many times the animation should play before
being complete, if you want to set it to infinity, type Infinity.

Lastly, the wait is a true or false (otherwise known as a boolean) that
determines whether or not the game waits for the animation's completion.

Now with the Move Picture command, you can fade in your animating
picture. And once you’re done with all your custom framed pictures, make
sure to include a this.removePictureCustomFrames();

.. _h.toiszrxt17u7:

Fog \ `🕊️ <https://www.google.com/url?q=https://mods.one/author/FoG&sa=D&source=editors&ust=1782966892352030&usg=AOvVaw1ma6TLmAG4M-Dp6gpquyOx>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A feature I rarely see get used in mods is fog. Fog is used in basegame
areas like the North Lake for a misty atmosphere.

From a technical standpoint, fog is effectively just a tiled (tiled as
in it has seamless edges, not the program Tiled) image looping across an
entire map. This means that you can actually use it for a lot of cool
things aside from just fog, but that's for you to figure out how to be
creative with it. I’m simply here to break down the script.

let fog = this.generateMapFog()

fog.move.x = x_scroll

fog.move.y = y_scroll

fog.name = ‘name’

fog.opacity = opacity

fog.blendMode = blendmode

this.createMapFog(‘fog1’, fog);

Now let's break down everything in this script.

The move.x & move.y determine the scroll speed of the fog, equivalent to
that of parallax scrolling.

The name is the filename of the fog from img/overlays.

The opacity is from 0-255 and is the, well, opacity of the image.

The blendmode is a value that determines the Blend Mode of the image.
These take a number value associated with the 4 Blend Modes in RPG Maker
MV, being 0 (Normal), 1 (Additive), 2 (Multiply), 3 (Screen).

Lastly an important note, if you use fog in a looping map, the fog
image’s dimensions must be a factor or multiple of the map’s image
dimensions, so for example a 1024\*1024 map must have the dimensions be
factors/multiples of 1024. Otherwise when reaching the looping points of
the map, the fog will begin to teleport.

.. _h.49my6p8x81ju:

Event Examples
--------------



.. image:: ../images/image169.png
   :align: center





.. image:: ../images/image96.png
   :align: center



(source: parallels, courtesy of FruitDragon)

Teleport Scripts!

The door is animated, as you can see with the Movement Route; and then
the Game Variables are set using a Script.

Finally, the Common Event Teleporting Style is used, the sound effect is
used, and the movement route to close the door is shown. The Common
Event Fade-In Screen is used to make it so the new map kind of fades
into view.

There are other types of Teleport Scripts aside from front doors,
though, so it’s always good to check those out!



.. image:: ../images/image249.png
   :align: center



(source: parallels, courtesy of FruitDragon)

Door cutscenes!

As you can see, there’s an animation added to show the door opening.
Sound effects are used for the audio. In the first visible script,
$gameMap.event(6).setPosition(x, y); changes the position of Event 6 to
46, 10. Afterwards in the second part of that same script, though it’s
partially cut off, the Self Switch of that event is set to True, which
in this case will make the Event’s sprite visible.

.. _h.uhf8h4xswr8:
