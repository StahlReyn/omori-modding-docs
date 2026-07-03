Data Files
==========

.. admonition:: Disclaimer
    :class: warning
    
    This is a very early-stage list. Files may contain more
    important data than mentioned here, so you're more than welcome to
    contribute details via the `mods.one
    Discord <https://discord.gg/Rxr5QfQnFd>`__.

This page documents useful information about
`decrypted <https://omori.wiki.mods.one/modding:getting_started#decrypting_the_game>`__
files found in the **www_decrypt/data/** subfolder. More info can be
found `here <./>`__.


.. glossary::
    Actors.json
        Seems to store information on your team (Omori, Kel, Aubrey, Hero),
        which items they carry (initially), what level they have, and more.

    Animations.json
        Animation data for the individual sprites being rendered. Might best be
        edited by using RPG Maker instead of manually.

    Armors.json
        :bdg-info:`Translation`

        Charms/equipment descriptions, sprites, and properties.

    Atlas.yaml
        *TBA*

    Classes.json
        *TBA*

    CommonEvents.json
        Data for many different events (basically any action you can do). Seems
        to be on maps only (not in combat).

        **Examples:** Opening Blackspace doors, horror effects (screen
        glitches), waking up animation, looking at photos, Kel throwing…

    Enemies.json
        :bdg-info:`Translation`

        Enemy names, sprites, and properties.

    Items.json
        :bdg-info:`Translation`

        Item names, descriptions, sprites, and properties.

    MapXXX.json
        :bdg-info:`Translation`

        Map files describe all places and rooms in OMORI. *displayName*: This
        field will be used when creating or overwriting a save file. *todo,
        there's a LOT more about these files* For anything that goes beyond
        small modifications, you definitely want to use RPG Maker: `Mapping in
        OMORI using RPG Maker. <https://omori.wiki.mods.one/modding:mapping>`__

    MapInfos.json
        TBA

    Notes.yaml
        TBA

    Quests.yaml
        TBA

    Skills.json
        :bdg-info:`Translation`

        Skill names, descriptions, sprites, and properties.

    States.json
        :bdg-info:`Translation`

        State change names (emotions, dying, resurrection etc.), descriptions,
        and properties.

        **Examples:** "X became TOAST!", "X feels ECSTATIC!", "X's SPEED fell!"

    System.json
        TBA

    Tilesets.json
        :bdg-muted:`Unused`

        Tileset for rpgmaker. OMORI stores map externally and uses Tiled.

    Troops.json
        Enemy data. HP among other things.

    Weapons.json
        :bdg-info:`Translation`

        Weapon names, descriptions, and other properties.

    Conflicted copies
        :bdg-muted:`Unused`
        
        Typically named *[…] OMORI Dev's conflicted copy […].json*

        These files are most likely unused and left there by accident.

.. note::

    In later versions of OMORI, these file are
    removed since then. This might be important to old mods when using
    Bundletool to detect changes.
