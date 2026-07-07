Intro to RPGMaker MV
=====================

*Omori was created in RPG Maker MV, and with a playtest folder you can
open the game in the application and edit it.*

Modding Omori is different from other games because you can open, edit
and playtest a cloned version of the game in RPG Maker MV. Through this,
you can modify and create maps, events, player and enemy data, and much
more. 

.. note::

   If you or your team are using github for mod version control,
   please make sure to pull the repository changes before opening the
   project in RPG Maker MV.

Opening the Game in RPG Maker MV
--------------------------------

To open the game as a RPG Maker project, first create a playtest folder
(`click here for steps on how to do
that <../getting-started/decryption-and-playtest-generation/>`__) and
then open RPG Maker MV, From there, you can click ``File -> Open...`` at
the top left corner, then navigate to the playtest folder and open the
project file found there.

RPG Maker Tools
---------------

Below is a diagram annotating the different essential tools that can be
used on an Omori RPG Maker project:

<PICTURE HERE>

Most of the buttons can be used for Omori modding, but the tools that
aren't highlighted are either not required or don't work for an Omori
project.

Map Event Editor
~~~~~~~~~~~~~~~~

Found in the center of the screen, the Map Event Editor is where map
events can be edited, and it takes up the majority of RPG Maker MV's
interface. It is tile based, and events can be selected, edited, or
created by clicking, double-clicking, and right-clicking the respective
tiles.

The zoom of the editor can be changed using the magnifying glass buttons
on the top bar, or by using the mouse scroll wheel/laptop trackpad, like
most other editing software.

Quick Save/Open
~~~~~~~~~~~~~~~

At the top left and highlighted in purple on the diagram, the quick
save/open buttons are self explanatory; the left button saves the
project, and the right button opens a new one. Alternatively, this can
be done using ``CTRL + S`` and ``CTRL + O``.

Copy/Cut/Paste
~~~~~~~~~~~~~~

At the top left and highlighted in orange on the diagram, the
Copy/Cut/Paste buttons can copy, cut, and paste selected events.
Alternatively, this can be done using ``CTRL + C``, ``CTRL + X``, and
``CTRL + V``, like most other editing software.

Database
~~~~~~~~

At the middle of the top bar and highlighted in red on the diagram, the
Database button opens the database window, which is one of the most
important parts to Omori modding. Here, you can edit actor, item, enemy,
system, animation, state, and common event data. An image of the window
is shown below.

<PICTURE HERE>

Each tab has its own smaller windows, but they're labaled and should be
easy to navigate.

Playtest
~~~~~~~~

At the top right and highlighted in green on the diagram, the Playtest
button will open a new window when clicked that will run the current
project as a game. This is used to playtest and bug fix mods.

Map Selector
~~~~~~~~~~~~

At the bottom left and highlighted in blue on the diagram, the Map
Selector shows a list of all created maps. Here, you can create new maps
by right-clicking or pressing the enter key, and select maps by
left-clicking normally. The new map's events will then appear on the Map
Event Editor.

Map and Event Details
~~~~~~~~~~~~~~~~~~~~~

At the bottom bar and highlighted in yellow on the diagram, the Map and
Event Details bar gives some information on the selected map and event.
From left to right, the bar will show:

- Map ID, name, and size (width x height)
- Map zoom size
- Selected tile (x, y)
- Event ID and name (if event tile is selected)
  
