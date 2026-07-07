Custom Battles
==============

Being an RPG Maker MV game, Omori features a combat system with enemies
and fights that can be modified using the software.

.. note::

   This requires the use of RPG Maker MV. Editing JSON will contains raw numeric code.

Creating a Custom Enemy
-----------------------

Making a new enemy in Omori starts off simple; you just use the Enemies
tab in RPG Maker database. A picture of it is shown below.

.. figure::
   https://user-images.githubusercontent.com/87251065/217147218-9835951e-893b-43d7-a491-0b92353163f5.PNG
   :alt: Enemy Screen

   Enemy Screen

Everything after that gets a little complicated, though.

Configuring Enemy Emotions
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Omori's emotion system for enemies is complicated. It works by taking
an enemy "base ID", then adding 1, 2, or 3 to that ID to apply the new
emotion.*

You will need to create an extra enemy in the database for each emotion
they have, including neutral. This can be easily done by finishing the
neutral enemy first, then copying it (using CTRL+C/CTRL+V) to however
many new entries you need. The way the game determines emotion is by
adding a number to the enemy's ID, so the emotions will have to be in
specific places. An image roughly showing the order is shown below.
Please copy the same format for your custom enemy.

.. figure::
   https://user-images.githubusercontent.com/87251065/217153614-6a2c7f78-ec53-4df2-8eba-683bfb5a5f5d.PNG
   :alt: Emotions

   Emotions

General Settings
~~~~~~~~~~~~~~~~

Here you can change the enemy's name and stats. Omori does not use the
M. Attack and M. Defense stats, and editing them will do nothing. The
other stats are used, though. You can change the enemy's "image" too,
but this will be unused in actual combat. You're still required to set
it to some image, though. More info on this can be found in the "Note"
section.

Rewards
   Here you can change the EXP and Gold an enemy drops.

Drop Items
   Here you can change the Items an enemy drops, and the rate at which they drop them.

Action Patterns
   Here you can add skills the enemy can use, and the frequency at which
   they use them. However, for the most part, Omori's enemies use a more
   complex battle AI system via notes.

Traits
   Here you can add specific parameters that affect the enemy's behaviors.
   There is a lot to mess with here, but for reference, the average enemy
   will have resistances to all 2nd and 3rd tier emotions.

Note
   Here is where the Plugin Note Tags are placed. There are a lot of
   important things every enemy needs. An explanation of the tags is shown
   below.

``<TransformBaseID: id>``
   Please replace the number with the ID (number to the left of the entry)
   of your own enemy's **neutral version,** or base. This applies even to
   the different emotion variants.

``<Static Level: x>``
   TBA

``<AI Level: x>``
   This determines how often the enemy will follow the actions in
   ``<AI Priority>``, percentage based. Lower numbers means a more random
   enemy, and vice versa.

``<AI Priority></AI Priority>``
   This is where the actual enemy AI and skills go. The comprehensive
   explanation can be found on the Yanfly Wiki found
   `here <http://www.yanfly.moe/wiki/Battle_A.I._Core_(YEP)>`__.

``<Sideview Battler: filename>``
   Determines the sprite used, based on sheets found in the
   ``img/sv_actors`` folder, following the naming scheme of "!battle_x".
   For example, Sweetheart's sprite is ``!battle_sweetheart.png``.

   .. info::

      The filename of the sprite in this folder must
      also have a corresponding sprite of the same name (in this case,
      ``!battle_sweetheart.png``) in the ``img/enemies`` folder.

``<Sideview Battler Frames: x>``
   Determines how many frames of animation the enemy has. You will most
   likely keep this at 4 unless you know what you're doing.

``<Sideview Battler Speed: x>``
   Determines the animation speed. Normally set to 12.

``<Sideview Battler Size: width, height>``
   Determines the size of your sprites. This is based on the width and
   height of a **single frame** on the sprite sheet. 

``<Sideview Battler Motion></Sideview Battler Motion>``
   The Index number in Omori case is essentially what Row of sprite is to
   be used. The name field is more of a left over, with only Damage and
   Dead field being used.

   Note that you will have to change all the values that are "0" to
   different numbers for the emotion variations: Happy is set to 5, Sad is
   set to 3, and Angry is set to 4. 

``<FallOnDeath>``
   Makes enemy move down when dead. This is typically used for generic
   enemies.

.. note::

   The Sideview Battler Motion is from a plugin by
   Yanfly in **Animated Sideview Enemies (YEP)**. The wiki can be found
   here: `<http://www.yanfly.moe/wiki/Animated_Sideview_Enemies_(YEP)>`__

   Though it is to note that Omori heavily overrides the plugin.

Creating a Custom Battle
~~~~~~~~~~~~~~~~~~~~~~~~

With the new enemy created, they can now be used in custom battles.

First you must create an entry in the "Troops" tab for the enemy, or a
group of enemies, to be fought. This does not need anything special and
can be done the same way it's normally done in RPG Maker. 

To start the battle, you need to create a new event using the "Battle
Processing" block. From there you can select the troop you wish to
battle.

Omori battles normally have a transition before them. These transitions
are activated through the Common Event block. The same can also be said
for basic post-battle functions. I would highly recommend using both of
these events in your battle events.
