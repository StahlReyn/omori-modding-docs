Sprite Sheet Filenames
======================

Sometimes some sprite sheet have special character associated in the
file name, which changes it's function.

Sprites origin is the **top-left corner** of the sprite. Meaning larger
sprites expands towards bottom-right tiles.

Standard - ``name.png``
   Standard regular sprite sheet. 
   Having 8 character in total in sets of 3x4 tiles, totals to 12x8 tiles. 
   In OMORI, the cells are usually in 32x32 pixel. 

   It is possible to have larger sprite, the engine simply divide by 12x8.

Single Set - ``$name.png``
   Turns the sprite so it's only single character.

   It is possible to have larger sprite, the engine simply divide by 3x4.

No Offset - ``!name.png``
   Removes the offset 6 pixels above tile offset that RPGMaker does by default.

   Useful for static decoration such as doors.

Single Sprite - ``[SF]name.png``
   This makes it singular sprite. This may appear in preview incorrectly as divided, but will display in-game as singular image.

   Useful for large decoration such as curtains or trees.

Frame Count - ``name%(x).png``
   This is a suffix, put at the end. 
   This specifies specific amount of frames in horizontal direction, with ``x`` being the number.

   Useful for character needing more animations, such as running sprites or "Something" enemies.

.. tip::

   Prefix and Suffixes can be combined. This is common in run sprites such as ``$FA_OMORI_RUN%(8)``
   To indicate that it is a single set of character with 8 frames.

.. note::

   In some sprite you might notice some have a
   combination of multiple objects in the same area. This is likely that the
   frames are still or hard set to specific frames, being set in RPGMV. By
   default RPGMV will go by 3x4 set treating like characters.

.. seealso::

   Also see `RPG Maker Forums on Sprite Sheet Formats <https://forums.rpgmakerweb.com/index.php?threads/sprite-sheet-formats-and.63612/>`__


