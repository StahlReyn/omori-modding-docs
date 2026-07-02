Community Resources for Mod Making
==================================



.. image:: ../images/image55.png
   :align: center



Now. For the final step to this guide. Up until now, we’ve been mostly
going under the assumption that you have just been using the
basegame and your own assets, which is commendable. However, we are a
modding community, therefore there are quite a few community made mods
and plugins made for modders like you and me. This section will detail
how to add them to your mod and some of what I deem to be some of the
most useful.

.. _h.e4724h8if1zt:

Adding Plugins
--------------

Plugins are super easy to add. Plugins are stored as .js files. These
are placed in the js/plugins folder.

Then in RPG Maker MV, open up this tab



.. image:: ../images/image164.png
   :align: center



^This one

This will open up a new menu listing all of OMORI’s Plugins, now scroll
all the way to the bottom, and double click on the empty space. Then you
can select your plugin and set its Status to ON.

And that’s really it. The plugins are loaded from top to bottom, so
lower plugins will overwrite upper plugins, which is why we can make
plugins to overwrite the base code.

Now for what you’re probably here for, which is for me to list you a
bunch of cool plugins that are gonna help you make mods easier. So here
you go, curated by yours truly:

.. _h.ssry8i2y1zxb:

Development Mods\ `[g] <#cmnt7>`__\ :sup:`\ `\ `[h] <#cmnt8>`__\ :sup:`\ `\ `[i] <#cmnt9>`__\ :sup:`\ `\ `[j] <#cmnt10>`__\ :sup:`\ `\ `[k] <#cmnt11>`__
--------------------------------------------------------------------------------------------------------------------------------------------------------

These are mods that are made to assist in the development of other mods.

Note: All mods in this section should not be included in the compiled
mod.

.. _h.v3mwl8k89w33:

`BundleTool <https://www.google.com/url?q=https://mods.one/mod/bt&sa=D&source=editors&ust=1782966892575305&usg=AOvVaw0HZ5L2nISp-BrW-Te2Wj_b>`__\ : by Rph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An absolutely crucial piece of software. If you’ve noticed, you’d know
me and FruitDragon never explained how to compile a mod. While this can
be done manually, which you can see
\ `here <https://www.google.com/url?q=https://omori-modding.gitbook.io/wiki/getting-started/packaging-mods/mod.json-file&sa=D&source=editors&ust=1782966892575633&usg=AOvVaw0V0oy86EWJLf5bdukQLY8k>`__\ ,
BundleTool makes this process much cleaner and faster.

To use BundleTool, place it in your OMORI mod folder as if it were a
regular mod (Recommended that you don’t include other mods while doing
this.). Once you turn the game on, you will be prompted to select your
playtest folder. From there just follow the instructions.

.. _h.udcw3m54h5ew:

`Better $atlasData Errors <https://www.google.com/url?q=https://mods.one/mod/betteratlaserror&sa=D&source=editors&ust=1782966892576131&usg=AOvVaw3yKIDX0caPaLKma70k_FNm>`__\ : by DraughtNyan & Rph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This plugin will make any error messages much more detailed, explaining
properly what the problem was that caused the crash. When adding this
plugin, make sure to move it above the plugin “GTP_OmoriFixes” by
clicking and dragging it up.

.. _h.endi21z8zcmk:

`Console <https://www.google.com/url?q=https://mods.one/mod/console&sa=D&source=editors&ust=1782966892576498&usg=AOvVaw18ENoDV1ZOZWMCaUp5eUHf>`__\  & \ `Console + <https://www.google.com/url?q=https://mods.one/mod/consoleplus&sa=D&source=editors&ust=1782966892576561&usg=AOvVaw1YqmX9onICaEC-nTED40yU>`__\ : by surrealEgg, Lee, & GlitchyZorua
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of two mods that allow much more detailed debugging than the base
debug menu. This will give a more streamlined debug menu with access to
changing items, skills, switches, variables, activate events and
battles, and more.

Note: Console + commands are each stored as individual
plugins\ `[l] <#cmnt12>`__\ :sup:`\ `\ `[m] <#cmnt13>`__\ :sup:`\ `\ `[n] <#cmnt14>`__\ :sup:`\ `\ `[o] <#cmnt15>`__\ ,
so I recommend only including the “quit” command, which just closes the
game, as the rest are not really helpful for development.

.. _h.2weksv431gzb:

`Save Drag and Drop <https://www.google.com/url?q=https://mods.one/mod/dragdrop&sa=D&source=editors&ust=1782966892577156&usg=AOvVaw0K7SN6xiKvEk1NQZWjXhxn>`__\ : by Rph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod allows you to drag downloaded .rpgsave files onto an open OMORI
window and have them load easily. This is good if you have to test a
change for a specific section of the game or test if a change works at
different stages in the game.

A collection of Save Files at various points in the game can be found
\ `here <https://www.google.com/url?q=https://docs.google.com/document/u/0/d/1qYsW_uXsBD0wMtmQG06UxIMfbGYuTgeu-AHzzdjCw-s/mobilebasic&sa=D&source=editors&ust=1782966892577645&usg=AOvVaw0Hks6DaJ4lJzHlVSwmbXSU>`__\ .

.. _h.52sd8orsouhr:

`Quick Load on Start <https://www.google.com/url?q=https://mods.one/mod/quickload&sa=D&source=editors&ust=1782966892577760&usg=AOvVaw35rJzuzuMTusLOhjg8z0Gw>`__\ : by VykosX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod makes it so that the game will instantly load the most recently
used save file, skipping the splash, title, and save file selection.
This is very helpful if you are playtesting often.

.. _h.9wolyc60zom6:

`Improved Save & Load Menu <https://www.google.com/url?q=https://mods.one/mod/saveloadplus&sa=D&source=editors&ust=1782966892578126&usg=AOvVaw2M8nJid6J-YDh0BVMeIUmC>`__\ : by tommy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is technically just a mod for general use, but it’s especially
helpful in mod making. This mod increases your save count to effectively
as many as your computer can handle. This is very useful for Total
Conversion mods (The OMORI term for a romhack) or mods that have
numerous changes with the basegame where you need to have many saves at
various points in the game.

.. _h.gmud7g22zohd:

Customization Mods
------------------

These mods add visible changes to the game that allows you to have
increased control over certain aspects of the game. These have to be
included in the compiled mod. Make sure to give credit where it's due!

.. _h.jocm5gdespy5:

`Enemy Z Offset <https://www.google.com/url?q=https://mods.one/mod/enemyoffsetz&sa=D&source=editors&ust=1782966892578952&usg=AOvVaw2JY3BcJsRBWE8VnjeB7SkF>`__\ : by Riomo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod allows you to add an enemy’s z position to their notetags,
making them appear above or behind most other enemies. Helpful for
battles that have more complex enemy arrangements.

.. _h.bgfu25fl9tkh:

`Tiled Fixer <https://www.google.com/url?q=https://gist.github.com/rphsoftware/51cc72721c25eeea54de50850abd8ea6&sa=D&source=editors&ust=1782966892579347&usg=AOvVaw1YmHPlo0Isoc4A5DrVLuvy>`__\ : by Rph, Draughtnyan, and FoG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows versions 1.8.5+ of Tiled to be used with OMORI projects. Also
requires TerrainTiles.json to be
\ `updated <https://www.google.com/url?q=https://github.com/FoGsesipod/Terrain-Fix&sa=D&source=editors&ust=1782966892579624&usg=AOvVaw3MBtyrgfZqXyItm6_qTq3w>`__\ .

.. _h.c3w5fqwk74r6:

Badges: by Draughtnyan
~~~~~~~~~~~~~~~~~~~~~~

.. _h.68v0dos1ofgm:

`Yaml Title Screen <https://www.google.com/url?q=https://mods.one/mod/easytitlescreen&sa=D&source=editors&ust=1782966892579790&usg=AOvVaw1Dt8G-PfSd53PlXefzEX0H>`__\ : by FruitDragon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows the user to create a custom OMORI title screen with the use of
Yaml. If you want base game title assets, use EasyTitleScreen instead
(same download link).

.. _h.6wllfueib0v:

Weather Extension: by FruitDragon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _h.ibbfyx99z650:

`Forced Action Targeting + Skill Emotion Targeting <https://www.google.com/url?q=https://mods.one/mod/weaknesstargeting&sa=D&source=editors&ust=1782966892580319&usg=AOvVaw0jBiDwRnOcfo0zXrQVdFSH>`__\ : by vl & Draughtnyan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod allows you to place notetags onto skills to change how enemies
using the skill target actors. This is primarily to allow them to
exploit emotions and target actors with the highest/lowest of a specific
stat.

.. _h.9ykm9x3hwboj:

`Tiered State Functions <https://www.google.com/url?q=https://mods.one/mod/statetier&sa=D&source=editors&ust=1782966892580725&usg=AOvVaw3l-6xoGdTeVDVi6lFXO7GV>`__\ : by Stahl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod skips the annoying lists of if-then commands used to add tiered
states (emotions and buffs/debuffs). This instead allows you to use an
eval command to add or subtract specific amounts of a state type to a
battler. You can also reference the tier of emotion or buff as a
variable with this.

Note: This plugin has been significantly updated in the
\ `Reverie <https://www.google.com/url?q=https://mods.one/mod/reverie&sa=D&source=editors&ust=1782966892581172&usg=AOvVaw0S5uTB3b-QiokQ2Jgm2CtU>`__\  mod
to allow more specifications, and I recommend using that version
instead.

.. _h.qg2uqfrbsm1o:

`More Than 4 Skills <https://www.google.com/url?q=https://github.com/rphsoftware/omori-utils/tree/master/more-than-4-skills&sa=D&source=editors&ust=1782966892581381&usg=AOvVaw1jektudtvkEK1waE2dkfoG>`__\ : by Rph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is one of Rph’s utility plugins, which are in a github repo. This
one allows for Party Members to equip more than skills by specifying
that using a script call that can be activated using an event. This can
be separately specified for each Party Member.

.. _h.beb2x2rrtge5:

`Splash Extender <https://www.google.com/url?q=https://github.com/rphsoftware/omori-utils/tree/master/splash-expander&sa=D&source=editors&ust=1782966892581798&usg=AOvVaw3EGeFnWg_CABNsZiRjbaER>`__\ : by Rph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another utility plugin. This allows you to add extra images to the
splash screen (where the Omocat logo and Content warning is).

.. _h.fjhi2bt507cf:

`Gold Counter Disabler <https://www.google.com/url?q=https://mods.one/mod/goldcounterdisabler&sa=D&source=editors&ust=1782966892582100&usg=AOvVaw2eSGkAsNrLEiSvL1VLoiNN>`__\ : by FoG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disables the Gold (Clam) counter in the Dream World. For any mod that
doesn’t plan on having currency.

.. _h.q6f219c8pbzx:

`Mod Configs <https://www.google.com/url?q=https://mods.one/mod/modconfigs&sa=D&source=editors&ust=1782966892582336&usg=AOvVaw0jHg-EQxxwA8WKcZYJnets>`__\ : by Snek
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows you to add settings to your mod that can be changed in the main
menu. This is useful for customisable mods like \ `Customisable
Difficulty <https://www.google.com/url?q=https://mods.one/mod/customisabledifficulty&sa=D&source=editors&ust=1782966892582585&usg=AOvVaw3RyTzC17mGeQpl9le9ChV2>`__\ .

.. _h.hs8eagyehi1c:

`Compatibility Patch for Save & <https://www.google.com/url?q=https://mods.one/mod/saveloadpluscompatibility&sa=D&source=editors&ust=1782966892582717&usg=AOvVaw1cTZ7Bf9A0QyQKay-jsQXn>`__ `Load+ <https://www.google.com/url?q=https://mods.one/mod/saveloadpluscompatibility&sa=D&source=editors&ust=1782966892582764&usg=AOvVaw2feLrdNzkyWf8UqT_Vcewb>`__\ : by Pyro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a patch allowing you to customize the Save Load + menu without
having to ship the mod. This is good if you have new party members or
want your new areas to have backgrounds for Save Load + users.

.. _h.ef334qgnwb5m:

`Custom State Damage Face <https://www.google.com/url?q=https://mods.one/mod/statedamageface&sa=D&source=editors&ust=1782966892583123&usg=AOvVaw2M-3iBiFrWdPPv0BSxxWjx>`__\ : by Riomo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod allows you to set a damage face for each state. This is good if
your state faces look radically different and you don’t want the damaged
face to look jarring when switching expressions.

.. _h.g0uueziq5m8q:

`In-battle Choices Box Fix <https://www.google.com/url?q=https://mods.one/mod/fixbattlechoices&sa=D&source=editors&ust=1782966892583479&usg=AOvVaw0kLVrwZF0GpomwcQOEV7fS>`__\ : by dawn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixes the position of choice boxes in battle to be aligned like how it
is in the console version of the game for Bossman Hero.

.. _h.eteq2vmg7erj:

`Fixed Priority Skills <https://www.google.com/url?q=https://mods.one/mod/fixedpriorityskills&sa=D&source=editors&ust=1782966892583758&usg=AOvVaw2NJmKfmhms5P-b1oPPaw-C>`__\ : by vl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Redoes the way moves that act first are handled, due to the default
method occasionally not functioning. (I don’t know exactly how the
original method breaks, as I’ve never encountered any bugs, but if you
want to be extra safe, then you can use this.)

.. _h.en0wz7pipec9:

`YAML Extended <https://www.google.com/url?q=https://mods.one/mod/yamlextended&sa=D&source=editors&ust=1782966892584112&usg=AOvVaw1NO3DOWzmo0KI7Dx8R0Q0y>`__\ : by WHITENOISE & Bajamaid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mod allows for playing sounds at the start of a YAML, changing the
text sounds, & changing the WindowSkin, all through parameters similar
to Facesets and Faceindexes.

.. _h.4a99xvlix9d1:

`OneMaker MV <https://www.google.com/url?q=https://mods.one/mod/onemakermv&sa=D&source=editors&ust=1782966892584535&usg=AOvVaw32Hy_olZwWzZ0-TXOidWF7>`__\ : by FoG, Rph, and Draughtnyan
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This one is so important it gets its own section. OneMaker MV is a mod
to RPG Maker MV itself, removing editor limits and adding extra features
especially helpful for OMORI modding.

.. _h.4f4e8z9jdb5g:

Installation
~~~~~~~~~~~~

Due to the nature of the tool, it requires special setup to get
functional. This will cover the basic steps:

#. Download the
   \ `Installer <https://www.google.com/url?q=https://mods.one/dl/ed133e09-5a67-4de7-b1c5-5cbb2f5cf7fa&sa=D&source=editors&ust=1782966892585139&usg=AOvVaw2gGD1HMLjyNkDbnY2Mbq4j>`__\  from
   mods.one.
#. Run the Run Installer.bat file inside the 7z.
#. Download the
   \ `OneMakerMV-Core <https://www.google.com/url?q=https://mods.one/dl/a0c7c70b-98e3-43fb-bee9-1fc73bc0d984&sa=D&source=editors&ust=1782966892585387&usg=AOvVaw3hY4_SRw1RJokHwGstXwBq>`__\  plugin
   from mods.one.
#. Add it to your project and move it to the top of your priority list.

And now you’re good to go! If you need to install further updates,
simply rerun the Installer and you’ll have the newest version.

Now onto the features of OneMaker.

.. _h.mfb1g09e0gjy:

Automatic Tilemap Display
~~~~~~~~~~~~~~~~~~~~~~~~~

In standard RPG Maker MV, you cannot see the tilemap in the editor, due
to it being a separate program. However, with OneMaker, by turning on
the Show Tiled Maps checkbox from the Map Properties (which replaces the
Show Parallax checkbox and therefore is likely already on), it will pull
the map from the render folder, allowing you to see both the tilemap and
the parallax. This folder is automatically made when using Rph’s
\ `Omori Map
Renderer <https://www.google.com/url?q=https://github.com/rphsoftware/omori-map-preview-renderer/actions/runs/20416117980&sa=D&source=editors&ust=1782966892586405&usg=AOvVaw2ksbacVInS8QnTZJVZypAz>`__\ ,
but can also be manually made. To add a map, simply extract it like
shown in the \ `Mapping Section <#h.xeqmo5erxcjt>`__\ , then relocate it
to render.

Note: You will want to extract your images at 100% scale, compared to
the standard 150%.



.. image:: ../images/image21.png
   :align: center


(source: TomatoRadio)

.. _h.6nxq5acxasz1:

Window Size Increases
~~~~~~~~~~~~~~~~~~~~~

OneMaker increases the size of the Database window dramatically,
allowing much more room for writing out in the Notes tab and other uses.
These can be reduced back down if they are too large for your display in
the OneMaker’s Window Sizing Settings.



.. image:: ../images/image246.png
   :align: center



(source: TomatoRadio)



.. image:: ../images/image136.png
   :align: center



(path to OneMaker settings, source: TomatoRadio)

The Event Command menu has also been merged into one menu, rather than
split between 4 pages. This can also be toggled.

The Control Self Variable, Switch Statement, and Sound Manager commands
are also only available if the OneMakerMV-Core plugin is present,
otherwise they will be grayed out, however the Custom Advanced commands
will still be available.



.. image:: ../images/image123.png
   :align: center



(source: TomatoRadio)

.. _h.7mftl0zar9vu:

Expanded Event Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~

Events now have more Conditions available. These are as follows:

- Variables can now use multiple operators, being ≥, >, =, <, ≤, ≠
- Self Switches can now use every letter of the alphabet
- Self Variables, a normally script exclusive data type, can now be
  accessed in the editor.
- Scripts may be used for more complex conditions.

Note: Conditionals are only checked on the $gameMap.refresh() function.
This effectively means that scripts will only be checked when
switches/variables are changed, actors/items are changed, or when the
map is loaded.



.. image:: ../images/image62.png
   :align: center



(Source: TomatoRadio)

.. _h.3yo6w2oxg5ut:

Expanded Event Commands
~~~~~~~~~~~~~~~~~~~~~~~

Various Event commands have been granted new functionality or expanded
limits in addition to new ones being added!

.. _h.d8a5jm17w37o:

Show Text
^^^^^^^^^

Show Text now uses a 106x106 pixel grid when selecting faces, making it
more compatible with OMORI’s Facesets.



.. image:: ../images/image90.png
   :align: center



(Source: TomatoRadio)

Previews will also now display in OMORI’s standard typeface as well.



.. image:: ../images/image117.png
   :align: center



(Source: TomatoRadio)(Note: This will not display edited versions of the
font or alternative fonts such as Stranger’s font)

.. _h.bsbfxmny37qd:

Control Variables
^^^^^^^^^^^^^^^^^

Variables can now be set to be equal to a Self Variable.



.. image:: ../images/image82.png
   :align: center



(Source: TomatoRadio)

.. _h.x8naxeui52at:

Control Self Switch
^^^^^^^^^^^^^^^^^^^

Self Switches may now include all letters of the alphabet!



.. image:: ../images/image293.png
   :align: center



(Source: TomatoRadio)

.. _h.928hg5rbizox:

New - Control Self Variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^

New to OneMaker, this command allows you to set Self Variables, a data
type normally exclusive to Scripts. They behave just like normal
Variables, except attached to an Event, just like a Self Switch. You are
allocated 10 slots for Self Variables.



.. image:: ../images/image104.png
   :align: center



(Source: TomatoRadio)

.. _h.g8388c4bilbs:

Conditional Branch
^^^^^^^^^^^^^^^^^^

Conditional Branches now allow you to check Self Variables.



.. image:: ../images/image129.png
   :align: center



(Source: TomatoRadio)

.. _h.7j236iudhkdz:

New - Switch Statement
^^^^^^^^^^^^^^^^^^^^^^

A new command, Switch Statements, are lists of cases that something can
evaluate to, and then runs code from whatever case(s) match. So
basically, it’s like a long list of If-Then statements but more concise.

In OneMaker, these are your options. Simply fill in the Case’s textbox
with whatever you want the input to return as. So for example if I want
a case for if Self Variable Five is ‘17’, then I simply put 17.
Lastly, the Default checkbox acts as an “else” where it will run if no
other conditions are met.

(Note1: Inventory returns the Number of Item/Charm/Weapon you have.)

(Note2: Direction returns as a Number. These are the numbers RPG Maker
MV internally uses to refer to direction, being 2 for Down, 4 for Left,
6 for Right, and 8 for Up. These are based on a number pad on
calculators and phones.)



.. image:: ../images/image135.png
   :align: center



(Source: TomatoRadio)

.. _h.81s9t8pysevr:

Comment
^^^^^^^

You may now add virtually infinite lines to Comments.



.. image:: ../images/image187.png
   :align: center



(Source: TomatoRadio)

.. _h.1isn8wzpwtl:

Set Movement Route
^^^^^^^^^^^^^^^^^^

You can now display the Map and click on Tiles and Events to show their
coordinates and IDs, which is helpful for scripting.



.. image:: ../images/image132.png
   :align: center



(Source: TomatoRadio)

.. _h.bsngrc3wfqbc:

Wait
^^^^

You can now increase the time to 99999 frames or ~27.7 minutes.



.. image:: ../images/image160.png
   :align: center



(Source: TomatoRadio)

.. _h.rpxzo8l4nlhb:

New - Sound Manager
'''''''''''''''''''

A new command, Sound Manager gives you all of the Audio functions in one
command, plus some bonuses that weren’t originally there. These are:

- Fade In and Fade Out BGM and BGS at specific timings
- Save and Replay BGM and BGS to 4 slots each
- Pitches of a sound can be between 5% and 200% instead of 50% and 150%.



.. image:: ../images/image162.png
   :align: center



(Source: TomatoRadio)

.. _h.bo95qepvw8az:

Scripts
^^^^^^^

You can now use virtually infinite lines in a Script command.



.. image:: ../images/image277.png
   :align: center



(Source: TomatoRadio)

.. _h.1lm5ajvxevl6:

New - YAML Selector
^^^^^^^^^^^^^^^^^^^

A new command, YAML Selector allows you to preview and select messages
from your YAMLs directly instead of having to type them out.

Select the Message to display here, with the option of adding Choices
like so;



.. image:: ../images/image272.png
   :align: center



(Source: TomatoRadio)

Then select the exact message from this menu;



.. image:: ../images/image2.png
   :align: center



(Source: TomatoRadio)

And then it gets converted into a Plugin Command just like how the
basegame does it!



.. image:: ../images/image257.png
   :align: center



(Source: TomatoRadio)

.. _h.4qvo5lbrghkz:

New - Transfer Player Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. image:: ../images/image70.png
   :align: center

A new command, this
automates the creation of Map Teleports. Simply input your location and
other applicable information and it will be converted into a Script.



.. image:: ../images/image110.png
   :align: center

 

.. image:: ../images/image118.png
   :align: center



(Source: TomatoRadio)

.. _h.wydkn6bi4m37:

New - Actor Movement Animations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A new command, this allows you to automate the setting of walking and
running sprites for your Actors.



.. image:: ../images/image188.png
   :align: center





.. image:: ../images/image102.png
   :align: center



(Source: TomatoRadio)

.. _h.grgqmskce6a2:

Expanded Troop Event Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Troop Events are granted new Conditions to work with. These include:

- Switches
- Variables
- State checks for both Actors and Enemies
- Checks for an Item/Weapon/Charm in the party’s inventory
- Scripts



.. image:: ../images/image291.png
   :align: center



(Source: TomatoRadio)

.. _h.o70bzabhxs0m:

Expanded Event Searcher
~~~~~~~~~~~~~~~~~~~~~~~

The Event Searcher can now search the Names, Note, Comments, and Scripts
of Events.



.. image:: ../images/image77.png
   :align: center



(Source: TomatoRadio)

.. _h.gpw5z589qpoy:

Custom UI
~~~~~~~~~

OneMaker comes with three image packs that change the UI of RPG Maker.
The Koffin and Krypt image packs use Cookie Run Kingdom UI, and the MZ
pack uses the UI of RPG Maker MZ, MV’s successor. You may also select a
Custom pack, which is completely empty and allows for personally made UI
to be used. You can add your own through RPG Maker
MV/\_hijack_root/qml/Images and then create a folder named Custom.
Capitals matter!

Here is an example of my own image that I use:



.. image:: ../images/image34.png
   :align: center



(Source: TomatoRadio)

It’s absolute rubbish, but it is a good showcase of how you can use any
image you like in here.

If you for whatever reason wish to use this, here’s the
\ `link <https://www.google.com/url?q=https://drive.google.com/file/d/1UBdwmCFE008Xwy5s0C7RiODf_loDM6t2/view?usp%3Dsharing&sa=D&source=editors&ust=1782966892598139&usg=AOvVaw2ICdnvt7MEq-kR5sFRJ5TZ>`__\ .

.. _h.ymgqck7cib0v:
