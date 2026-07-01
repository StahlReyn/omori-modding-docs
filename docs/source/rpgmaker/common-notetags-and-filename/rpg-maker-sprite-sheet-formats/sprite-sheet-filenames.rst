Sprite Sheet Filenames
======================

Sometimes some sprite sheet have special character associated in the
file name, which changes it's function.

Sprites are set by the **top-left corner** of the sprite. Meaning larger
sprites will overlap to the bottom-right tiles.

Table Summary
-------------

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="96">

Char

.. raw:: html

   </th>

.. raw:: html

   <th width="162">

Example

.. raw:: html

   </th>

.. raw:: html

   <th width="339">

Description

.. raw:: html

   </th>

.. raw:: html

   <th>

Omori Use Case

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   </thead>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

name.png

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <p>

Standard regular sprite sheet. Having 8 character in total in sets of
3x4 tiles, totals to 12x8 tiles. In OMORI case the cells are usually in
32x32 pixel.

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </p>

.. raw:: html

   <p>

It is possible to have larger sprite, the engine simply divide by 12x8.

.. raw:: html

   </p>

.. raw:: html

   </td>

.. raw:: html

   <td>

Default

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

\ :math:`</code></td><td>`\ name.png

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <p>

Turns the sprite so it's only single character.

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </p>

.. raw:: html

   <p>

It is possible to have larger sprite, the engine simply divide by 3x4.

.. raw:: html

   </p>

.. raw:: html

   </td>

.. raw:: html

   <td>

Large unique enemies, Animated decorations

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

!

.. raw:: html

   </td>

.. raw:: html

   <td>

!name.png

.. raw:: html

   </td>

.. raw:: html

   <td>

In RPGMV characters will be shown 6 pixels above tile by default. This
removes that offset.

.. raw:: html

   </td>

.. raw:: html

   <td>

Doors, Decorations

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

[SF]

.. raw:: html

   </td>

.. raw:: html

   <td>

[SF]name.png

.. raw:: html

   </td>

.. raw:: html

   <td>

This makes it singular sprite. This may appear in preview incorrectly as
divided, but will display in-game as singular image.

.. raw:: html

   </td>

.. raw:: html

   <td>

Large Decorations: Chandeliers, Holes, Curtains

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

%(x)

.. raw:: html

   </td>

.. raw:: html

   <td>

name%(5).png

.. raw:: html

   </td>

.. raw:: html

   <td>

This is a suffix, put at the end. This specifies specific amount of
frames in horizontal direction, with x being the number.

.. raw:: html

   </td>

.. raw:: html

   <td>

Running Sprites, Fear Enemies

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

{% hint style="info" %} Prefixes also can be combined {% endhint %}

Examples
--------

Here's some example sprite used in actual game, with context.

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   [SF]SW_Hole.pngThis hole is a single large spriteAppears in
   Sweetheart Castle.

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   !objects_fa_doors.png! removes the offset, good for doors.Note that
   the doors are 2 tiles tall as well,as it is slightly taller than 1
   tile.

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   $FA_OMORI_RUN%(8).pngThis is a running sprite, $ sign tells it's
   single character,%(8) tells there are 8 frame horizontal.

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

{% hint style="info" %} In some sprite you might notice some have a
combination of multiple things in the same area. This is likely that the
frames are still or hard set to specific frames, being set in RPGMV. By
default RPGMV will go by 3x4 set treating like characters. {% endhint %}

Extra Resources
---------------

{% embed
url="https://forums.rpgmakerweb.com/index.php?threads/sprite-sheet-formats-and.63612/"
%} RPG Maker Forums on Sprite Sheet Formats {% endembed %}
