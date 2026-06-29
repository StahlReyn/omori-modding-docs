Enemy Notetags
==============

Explanation TBA, copy paste note tags for convenience for now

.. raw:: html

   <details>

.. raw:: html

   <summary>

Forest Bunny (Neutral) Notetag Example

.. raw:: html

   </summary>

::

   <TransformBaseID: 19>

   <Static Level: 1>

   <AI Level: 100>

   <AI Priority>
   State === State 186: SKILL 209, target
   Random 55%: SKILL 209, target
   Random 40%: SKILL 210, target
   Random 100%: SKILL 211, target
   </AI Priority>

   <Sideview Battler: !battle_forest_bunny>
   <Sideview Battler Frames: 4>
   <Sideview Battler Speed: 12>

   <Sideview Battler Size: 147, 159>
   <Sideview Width: 0>
   <Sideview Height: 0>
   <StatusYOffset: -150>
   <DamageOffsetY: 30>

   <Sideview Battler Motion>
   Name: Walk
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Thrust
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Guard
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Victory
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Damage
   Index: 1
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Dead
   Index: 2
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Spell
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Skill
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Item
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Other
   Index: 0
   Loop
   </Sideview Battler Motion>

   <FallOnDeath>

.. raw:: html

   </details>

Sideview Battler Motion
~~~~~~~~~~~~~~~~~~~~~~~

Sideview Battler Motion is the one that changes between emotion, with
Index changing the row the sprite is referring to in OMORI’s case.
Here’s all common emotion variant to save time with editing by copy
paste, in order same as enemy in Neutral, Happy, Sad, then Angry.

{% tabs %} {% tab title=“Empty” %} This is empty tab just to save wall
of text. {% endtab %}

{% tab title=“Neutral” %}

::

   <Sideview Battler Motion>
   Name: Walk
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Thrust
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Guard
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Victory
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Damage
   Index: 1
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Dead
   Index: 2
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Spell
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Skill
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Item
   Index: 0
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Other
   Index: 0
   Loop
   </Sideview Battler Motion>

{% endtab %}

{% tab title=“Happy” %}

::

   <Sideview Battler Motion>
   Name: Walk
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Thrust
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Guard
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Victory
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Damage
   Index: 1
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Dead
   Index: 2
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Spell
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Skill
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Item
   Index: 5
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Other
   Index: 5
   Loop
   </Sideview Battler Motion>

{% endtab %}

{% tab title=“Sad” %}

::

   <Sideview Battler Motion>
   Name: Walk
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Thrust
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Guard
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Victory
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Damage
   Index: 1
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Dead
   Index: 2
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Spell
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Skill
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Item
   Index: 3
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Other
   Index: 3
   Loop
   </Sideview Battler Motion>

{% endtab %}

{% tab title=“Angry” %}

::

   <Sideview Battler Motion>
   Name: Walk
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Thrust
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Guard
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Victory
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Damage
   Index: 1
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Dead
   Index: 2
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Spell
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Skill
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Item
   Index: 4
   Loop
   </Sideview Battler Motion>

   <Sideview Battler Motion>
   Name: Other
   Index: 4
   Loop
   </Sideview Battler Motion>

{% endtab %} {% endtabs %}
