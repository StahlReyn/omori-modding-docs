Party Members : Only the bare minimum for them
==============================================



.. image:: ../images/image84.png
   :align: center



NOTE: Party Members are inherently very complex and need so much more
than this. They need skills, equipment, dialogue, tag photos, tag
abilities, battle graphics, etc. BUT, those are either;

#. Already covered elsewhere in here
#. Dependent on what you’re doing

So I will just explain the bare minimum of the Actors and Classes tab,
plus how to set movement sprites.

.. _h.5z5k55klya34:

Actors
------

<Screenshot of Actor tab>

This is the Actors tab, which is where one part of all our Party Members
are stored. I'll break down everything here.

Name: Self-Explanatory.

Class: This is more of an RPG Maker MV holdover. Every Party Member has
their own Class. Basically the Actor is the “character” while the Class
is the “role” but again that’s redundant in OMORI.

Levels: DW Characters cap at 50, RW Characters cap at 1.

Character: This is more of a fallback as movements are coded into a
Common Event, but this will be the walking sprites if that Event is not
run. Make sure face and battler images are not set.

Traits: Various Effects the Party Member will always have. This is just
State Resistances in the Actors tab. Everyone besides Omori & Basil
resists tier 3 emotions, and Omori resists Afraid. These are the same
traits featured in the rest of the Database. You can see a full
explanation of them in the \ `States <#h.g7yzgvnqi3cb>`__ section.

.. _h.ecodhqc5e6zt:

Notes:
~~~~~~

<BattleStatusFaceName: faceset> The Faceset the character uses in
Battle.

<FearBattleFaceIndex: #>  Normally used by Sunny, if the control switch
“Neutral Face” is turned on, the Party Member's neutral face will be
changed to the row specified here.

<BattleStatusIndex: #> What corner they are displayed in Battle. 0 for
Top-Left, 1 for Top-Right, 2 for Bottom-Left, 3 for Bottom-Right

<MenuStatusFaceName: faceset> Used by characters whose faces are larger
than 106x106. These get used in Menus so that they don’t cut off.
Traditionally they are 125x125.

The rest of the BattleCommandList code can and should be copy pasted,
with the id for “skill” being replaced with the Party Member's basic
attack skill id.

.. _h.wdtur25oor16:

Classes
-------

<Screenshot of Classes tab>

This is the Classes tab, which is where all our Party Members' stats are
stored. I'll break down everything here.

Name: Self-Explanatory, doesn't show in game though.

Parameter Curves: This is how the leveling will scale for a character.
It looks like the devs manually set each level stat, which I think is
crazy. You can use the Generate curve button and set the stats as you
like there. They will make you input the stat for level 99, even if
OMORI caps at 50, so just put double of the level 50 stat. And after
it's done generating you can make adjustments if you want.

Skills to Learn: Self Explanatory. Make sure that the Follow-Up
checks are added to the list of learned skills.

Traits: Various Effects the Party Member will always have. This is
mainly equipment types for the Classes tab. Everyone is assigned the
POWER OF FRIENDSHIP skill type and CHARM Armor type. And each character
gets their own weapon type. In case you're wondering what the KEL type
armor is for, it's RW Kel's pet rock.

.. _h.di44otr84zdg:

Movement Graphics
-----------------

Movement Graphics for OMORI's Party Members are done through 3 Common
Events, Graphics Base, Graphics Climb, and Graphics Swim.

Luckily, all of the cases that are in these events are labeled in Code
Comments, so all you have to do is add another script under the main one
to add your party member. The format looks like this.

var bwalk = { name: 'DW_BASIL', index: 0 }

var brun = '$DW_BASIL_RUN%(8)'

$gameActors.actor(5).setMovementGraphics(bwalk, bwalk, brun);

The only parts you have to change are the variable names, so that there
are no duped variables, the images referenced, and the index for the
walking sprite.

The index is done the same as every other image in OMORI, but it refers
to the set of movement sprites, not any individual sprite.

REMINDER: If you try to edit the original scripts in these events, you
will notice that they get cut off. This is because RPG Maker MV by
default limits Script Commands to 12 lines. OMOCAT used a modified
version to bypass this. I assume that change was made by Archeia, who is
OMORI’s lead programmer and on RPG Maker MV’s actual dev team. No, this
version isn’t available and you just have to work with it or get
OneMaker.

.. _h.nkup6138v2ly:
