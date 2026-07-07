YAML Formatting
===============

This section gives succinct list of YAML related formattings.

YAML Message
---------------

Name Display
^^^^^^^^^^^^^^^^

Omori has main 2 ways of displaying names:

Shortcut macro
    Plugin parameter in ``YEP_X_MessageMacros1.js`` plugin, that is replaced with the name.

    Benefit from shortening names of reoccurring characters and also ease of potentially mass-changing names later.

Direct name
    Add ``\n<NAME>`` directly on the text field

    Benefit of being easy to implement, increases readability from being direct, and good for one off side characters.

Dialogue Only
^^^^^^^^^^^^^^^^

.. code:: yaml

    message_0:
        text: \n<HUMPHREY>I fucking love air-conditioning.

Dialogue with Portrait
^^^^^^^^^^^^^^^^

.. code:: yaml

    message_2:
        faceset: MainCharacter_Basil
        faceindex: 0
        text: Hope you don't mind the photo.\bas

Battle Dialogue
^^^^^^^^^^^^^^^^

.. code:: yaml

    message_141:
    text: >
        \>PERFECTHEART: \<I said that you would regret this, children.

Text Codes
----------

.. hint::

    Beware of the slashes! Text code uses backslashes ``\`` not normal slashes ``/``.

RPG Maker MV Text Codes
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Code
      - Function
    * - ``\V[n]``
      - Value of the nth variable
    * - ``\N[n]``
      - Name of the nth actor
    * - ``\P[n]``
      - Name of the nth (arranged order) party member
    * - ``\G``
      - Currency unit
    * - ``\C[n]``
      - Draw the subsequent text in the nth color from ``Window.png`` system image
    * - ``\I[n]``
      - Draws the nth icon
    * - ``\{``
      - Increases the text by 1 step
    * - ``\}``
      - Decreases the text by 1 step
    * - ``\\``
      - Replaced with the backslash character
    * - ``\$``
      - Open the gold window
    * - ``\.``
      - Wait for 1/4 second
    * - ``\|``
      - Wait for 1 second
    * - ``\!``
      - Wait for button input
    * - ``\>``
      - Display remaining text on same line all at once
    * - ``\<``
      - Cancel the effect that displays text all at once
    * - ``\^``
      - Do not wait for input after displaying the next


TDS Text Effects
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Code
      - Function
    * - ``\SINV[n]``
      - | Makes the text shake vertically. When n is:
        | 0 - Disable
        | 1 - Normal wave
        | 2 - Dense wave
    * - ``\SINH[n]``
      - | Makes the text shake horizontally. When n is:
        | 0 - Disable
        | 1 - Enable
    * - ``\QUAKE[n]``
      - | Makes the text wobble aggressively. When n is:
        | 0 - Disable
        | 1 - Intense quake
        | 2 - Softer quake
    * - ``\RAINBOW[n]``
      - | Adds an animated rainbow effect to the text. When n is:
        | 0 - Disable
        | 1 - Enable


Archeia Text Codes
^^^^^^^^^^^^^^^^^^^^^^^
In the following the most used are common event text code.
For example, to call shake screen common event.
There are other codes but it isn't used at all in Omori

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Code
      - Function
    * - ``\com[n]``
      - Invokes the common event of ID n

.. note::
    
    Text Codes can be invoked when set as character name and the name is trying to be called.

    A common hack is to set the player name as ``\com[3]`` to trigger the 
    save menu when the player is mentioned. Assuming if the game allows 7 
    characters for player name.

.. seealso::

    - `<http://www.yanfly.moe/wiki/Category:Text_Codes_(MV)>`__
    - `<https://github.com/Gilbert142/gomori/wiki/Text-Formatting>`__


Omori Text Color Convention
---------------------------

Omori tends to have a color for specific type of items, which are labelled to give emphasis.
This is done with the color code command of ``/c[n]``. 

The color picked are from ``img/system/Windows.png`` color pallette 
on the bottom right corner, with the first square being number 0. Omori changes the color palette from the default.

.. list-table::
   :widths: 15 20 65
   :header-rows: 1

   * - ID
     - Color
     - Type
   * - 0
     - White
     - Default
   * - 1
     - Blue
     - Skills
   * - 3
     - Green
     - Food
   * - 4
     - Yellow
     - Important Items
   * - 5
     - Orange
     - Toys
   * - 11
     - Light Blue
     - Locations
   * - 13
     - Purple
     - Equipment and Character Names (excluding casual referrals, which remains white)
