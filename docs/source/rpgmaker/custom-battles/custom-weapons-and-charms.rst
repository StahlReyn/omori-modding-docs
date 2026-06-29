Custom Weapons and Charms
=========================

“Hey, how do I make a cool weapon?”

Oh, thank god, an easy question.

Yes. Lucky for both of us, Weapons and Charms are some of the easiest
things to implement in OMORI, so this will be brief.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

All right. Lightning round on what all these do.

- Name: It’s the name. Don’t forget all-caps.
- Description: It’s the description. Make sure to use <br> for line
  breaks.
- Weapon Type: Who can equip this?
- Animation: Don’t use this
- Price: Don’t use this
- Parameter Changes: Stat Changes. Remember that MP is juice, Agility is
  speed, and M Attack/M Defense aren’t used.
- Traits: These are the exact same as from the states tab, so I won’t
  repeat myself. Just know that you need to give all weapons their hit
  rates and that Omori and Sunny’s weapons use the Lock Equip trait to
  prevent you from changing them.

Now for a brief Notes Section round too:

- <IconIndex:x> Determines the icon used. It’s based from
  img/system/itemWeapons.png and is indexed from 0, left to right, top
  to bottom. For charms it’s img/system/itemCharms.png.
- <PassiveState:x> Applies the specified state by id to the wearer while
  equipped.

And that’s it really. If only everything was this simple.
