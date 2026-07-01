Map Creation
============

Required Tools
--------------

To start creating custom maps (or editing vanilla ones) you will need a
few things:

- RPGMAKER MV (for data editing)
- Tiled (for tile editing)
- Playtest copy of the game assets (`see the mod workspace
  page <https://github.com/saikedemon/omori-modding/wiki/Mod-Workspace-Setup>`__)

Setting Up Tiled
----------------

As stated on the resources page, Tiled is the application of the game's
maps and tilesets. Note: This is the visual aspect of the maps, the data
and events stored in the maps are accessed via RPGMAKER.

Tiled 1.0.3
~~~~~~~~~~~

This is an older version of Tiled, and it is the version that is the
most stable out of the box for omori modding. You just `follow the
instructions
here <https://github.com/mapeditor/tiled/releases/tag/v1.0.3>`__ to
install it and you're ready to make maps!

Later Versions of Tiled
~~~~~~~~~~~~~~~~~~~~~~~

For any versions of Tiled beyond 1.0.3, more specifically the latest
version, the maps created on it will be unstable when put into the game.
`The latest version is linked
here. <https://github.com/mapeditor/tiled/releases/latest>`__. To
correct this there are a few things you will have to do.

First, Download the ``TerrainTiles.json`` file found
`here <https://github.com/FoGsesipod/Terrain-Fix>`__, and replace it
with the one in your playtest copy. The file should be located in the
"maps" folder.

Next, download the Tiled Map Fixer plugin on the page linked
`here <https://gist.github.com/rphsoftware/51cc72721c25eeea54de50850abd8ea6>`__
to the ``js/plugins`` folder.

The maps should now work fine on your playtest copy and when packaged
into a proper mod!

Creating a New Map
------------------

Maps can be created from RPG Maker's main interface. You can either
right click on the maps list toward the left or press the enter key to
create a new map. You'll know if you're doing it right if the menu shown
below appears.

.. figure::
   https://user-images.githubusercontent.com/87251065/218343523-b3a230e7-baf9-4532-a987-dcd0810a5a76.PNG
   :alt: mapcreation

   mapcreation

The creation menu is straightforward but if you're struggling to
understand it I would advise watching tutorials on how RPG Maker MV
works. What's important here for Omori modding specifically is that you
remember the id and the width and the height set, but if you need a
refresher that information can be found toward the bottom of the screen.

.. figure::
   https://user-images.githubusercontent.com/87251065/218343634-55431148-0b1b-4037-a2b7-65139010b4e5.PNG
   :alt: mapID

   mapID

In the image shown here, the map's id is 516, and the dimensions are
40x40 (in order of widthxheight). I recommend remembering the location
of these items as you'll reference them often!

Now you have to make the Tiled map file. If you don't do this, the map
will not load in game! This is usually the next step you'd want to take
anyways as you can only set tiles and collision in Tiled.

Open Tiled. A template file for maps can be found in the game's maps
folder, titled ``map00_Template_32x32.json``. It is highly recommended
to use this file as a base for your own map, but if you're interested in
learning how to create the maps from scratch a Youtube tutorial can be
found `here <https://www.youtube.com/watch?v=jsTH5DHw-g0>`__. To use the
file as a base, open it then go to ``File>Save As...`` at the top left
menu. You will want the save the map as map[id], in the maps folder. For
example, using the map in the previously shown image, the map's name
would be ``map516.json``. It is important that you save the map in the
maps folder and not the data folder. The data folder contains the map
data from RPG Maker and not Tiled!

The template map comes with layers and properties already prepared for
you. They're even labeled! All you have to do to use it now is resize
the map, which you can do by going to ``Map>Resize Map...`` on the top
left menu. You should change the width and height to the one of your own
map's. Again following the previous image example, the width and height
would both be 40.

Map and Data Editing
--------------------

In Tiled
~~~~~~~~

Tiling/Map editing in Tiled is rather simple, but you're confused on the
basics, you can find a YouTube guide here. Here's just some core things
to remember:

Layers
^^^^^^

Like in any editing program, layers higher up on the list in Tiled will
appear overtop of the lower layers. In addition, there are three extra
layer levels! Layers labeled ``GROUND`` will appear below the player
character, layers labeled ``SAME AS CHARACTER`` will appear on the same
level as the player character and above the ground layers, and layers
labeled with ``ABOVE ALL`` will appear above the player character and
all other layers. (It's important to note that usually level objects
such as chairs and tables are actually put on the ground layer, but with
collision tiles on top to prevent character movement through them)

Collision
^^^^^^^^^

There is a tile based collision system in Tiled that Omori uses, using
the tileset ``TileCollision_32x32.json`` found in the "maps" folder. If
the tileset doesn't appear in the tilesets tab, then open the file in a
separate tab and it should appear. The tiles for collision must be put
on the ``COLLISION`` layer or else they won't work! The layer isn't
visible in game so don't worry. The red tile in the tileset, found at
the top left is for spaces that can't be passed through in any
direction. This will be your go-to for most collision purposes. The
tiles with arrows on them indicate the directions in which the tiles can
be passed through. Any side that has a dot on them is still impassable,
though.

Tilesets
^^^^^^^^

Tilesets in Tiled will appear toward the right side of the screen. You
can click on one tile to select it for placement, or click and drag to
select a whole section of tiles at one time. This is especially useful
for placing objects more than one tile in length, such as buildings and
tables. The different tilesets will appear as tabs that can be selected
toward the top of the menu. They can be added for use in your own map by
opening the tileset or a map that uses it on a separate tab or by going
to ``Map>Add External Tileset...`` and selecting the tileset from there.
All of Omori's tilesets are found in the "maps" folder and are named
according to their use.

Terrains
^^^^^^^^

Terrains are complex tile patterns that are automated for ease of use.
You can access Omori's terrains by opening ``TerrainTiles.json`` on a
seperate tab. To use them, you go to the bottom right side of the screen
and switch the tab from Tilesets to Terrains. You can select the terrain
that you want and then click and drag on the map, "blocking in" the
shapes. Terrains make placing commonly used cliffs and walls incredibly
easy so it's recommended to use them for this purpose.

Regions
^^^^^^^

Regions work similar to the collision layer but instead of prevent
movement, tiles placed on this layer will do special things depending on
what number "regionId" is on the Custom Properties tab. The tileset used
on this layer is ``Tile_Regions_32x32.png``\ and the layer used for
regions is labeled ``REGION`` on the template map. Here is a table of
possible regionId values:

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th>

regionId

.. raw:: html

   </th>

.. raw:: html

   <th>

effect

.. raw:: html

   </th>

.. raw:: html

   <th data-hidden>

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

10

.. raw:: html

   </td>

.. raw:: html

   <td>

Makes the player slide, like the snowglobe mountain caves (or Pokemon
ice)

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

20

.. raw:: html

   </td>

.. raw:: html

   <td>

Acts like the collision tiles, but only for enemies

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

28

.. raw:: html

   </td>

.. raw:: html

   <td>

Makes footprints appear

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

90

.. raw:: html

   </td>

.. raw:: html

   <td>

Changes the player from walking to climbing, and vice versa.

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

92

.. raw:: html

   </td>

.. raw:: html

   <td>

Flashes the screen red and deals 10 damage to the entire party

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

The region tileset has different numbered tiles, up to 127. Use them to
properly organize your region layers! 

Custom Regions (javascript)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

With javascript, you can create and use custom region effects! To check
for a custom region id, you can use the boolean
``$gamePlayer.regionId() === (id)`` to check for the specific region to
apply the effects accordingly. For example,
``$gamePlayer.regionId() === 100`` will be true or false depending on if
the region id is 100 or not.

Tiled Levels
~~~~~~~~~~~~

Using Tiled you can make certain layers visible based on where the
player has been, for instance a bridge, that can appear above the player
if they walk under it, or appear below the player if they walk above it.
Tiled levels use a minimum of 5 new layers to your map, and therefore is
a little complicated to setup.

To Level layers
^^^^^^^^^^^^^^^

| With that being said, lets start with the layers that will transition
  to a different level, this is done with ``To Level - X`` layers, as
  seen here:
| |image|
| While the name of the layer itself doesn't matter, the properties of
  the layer do, adding a string property onto a layer and typing in
  ``level`` specifies what level this layer is, and by itself the level
  property doesn't do much. Going back to our ``To Level`` layer, we
  want to not only add a ``level`` property, but also another string
  property ``toLevel`` after which we want to set a value to them, for
  ``To Level - 0`` (which will sent the player to level 0 when they walk
  those tiles) we want to set its properties like so:
| |image1|
| And on ``To Level - 1`` we want the opposite values for the
  properties:
| |image2|
| So now tiles placed on ``To Level - 0`` will sent the player to level
  0, while tiles on ``To Level - 1`` will sent them to level 1, for
  reference any layer without a ``level`` property is level 0.

``level`` and ``hideOnLevel`` properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| So now that we have the ability to get the player onto a different
  level, we need to setup something to actually change in the map, lets
  use the bridge example once more, first we want to make a new above
  all layer that is on level 0, after adding in the ``priority`` and
  ``zIndex`` properties we want to also add ``level`` of 0 and
  ``hideOnLevel`` of 1, ``hideOnLevel``, as the name suggests, hides
  this layer when the player is on the specified level, in this case
  that being 1. Here is a example as to how this should look:
| |image3|
| |image4|
| On this layer we created, we want to place a bridge (or whatever it is
  you want to appear above the player when they are on level 0), after
  which, we want to duplicate this layer and flip the ``level`` and
  ``hideOnLevel``, alongside changing its name and ``priority`` and
  ``zIndex`` properties accordingly, like so:
| |image5|
| |image6|
| Now this ground layer will appear when the player is on level 1 while
  hiding the above all layer.

Collision Layer
^^^^^^^^^^^^^^^

| With that we have one more layer to create, a extra collision layer,
  it is recommended to save this until the map is completely done and do
  collision last, we need to modify the existing collision layer like
  so:
| |image7|
| |image8|
| this collision will be active when the player is on level 0 (when they
  enter the map, this collision will be used), duplicate this layer and
  flip the ``hideOnLevel`` and ``level`` properties like so:
| |image9|
| |image10|
| This new level 1 collision layer is where we need to set the collision
  for when the player is able to walk onto the bridge. When the player
  is on level 0 and enters the map, they should be able to walk under
  the bridge no issues, but when we want the player to walk on top of
  the bridge, we obviously don't want the player to be able to walk off
  the bridge, so you need to change this level 1 collision layer to
  account for that.

Only other thing to mention is that regions need to be level'd also,
using the same properties ``level`` and ``hideOnLevel``.

In RPG Maker MV
~~~~~~~~~~~~~~~

RPG Maker MV is where you can change things such as the map's music,
background, and most importantly, the events on the map, including
flavor text. Note that the Tiled map will not appear on the software
normally, so most maps will appear almost invisible. All of the tiles on
the map should correspond to that specific tile on the Tiled map, for
example, The tile (26,5) on the Tiled map will be the same one as (26,5)
on the RPG Maker map. This is important to keep in mind when trying to
position an event for flavor text, or put an NPC on top of a specific
object such as a chair.

Showing Tiled Maps in RPG Maker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're struggling to grasp the connection between Tiled and RPG Maker
you can export the tiled map as an image by setting the zoom in Tiled to
150% at the bottom right, then going to ``File>Export As Image...``.
Save the image to ``img/parallaxes``, only checking the specific options
shown on the image below.

.. figure::
   https://user-images.githubusercontent.com/87251065/218526243-09fd0cb4-4105-442d-a9b4-6f445fc7864b.PNG
   :alt: tiledexport

   tiledexport

You will now be able to change the parallax to the Tiled map on RPG
Maker's map settings menu, which can be accessed by either right
clicking the target map or by hitting the space key with the map
selected. The map should now appear, making Event placement
significantly easier!

Event editing
^^^^^^^^^^^^^

To create a new event or edit an existing one, double click on any of
the tiles in RPG Maker. Events will appear as tiles with thick white
borders, and can be selected by left or right clicking on them. They can
even be copied, cut, and pasted when selected using the ``CTRL+C``,
``CTRL+X``, and ``CTRL+V`` commands, respectively. For reference, here
is what the menu should look like when you create or edit and event.

.. figure::
   https://user-images.githubusercontent.com/87251065/218528498-b91c41da-2a78-4d2f-a128-118515980857.PNG
   :alt: eventmenu

   eventmenu

A detailed guide on what can be done in RPG Maker's event menu will be
created later. For now, I would recommend going onto YouTube for
tutorials on RPG Maker MV's event system!

.. |image| image:: https://user-images.githubusercontent.com/104705517/218759587-662237b7-43cd-4f6c-babe-c1c3a12315ba.png
.. |image1| image:: https://user-images.githubusercontent.com/104705517/218760874-2d696616-c235-48ec-a95f-0ff239eccdf7.png
.. |image2| image:: https://user-images.githubusercontent.com/104705517/218761387-e8b9bd5a-41e9-496e-afb8-51f222c02ee4.png
.. |image3| image:: https://user-images.githubusercontent.com/104705517/218763241-33fd3605-b842-4161-b5d5-765a10cf9266.png
.. |image4| image:: https://user-images.githubusercontent.com/104705517/218763272-faf700ae-675a-4e79-a7e5-37689a016af0.png
.. |image5| image:: https://user-images.githubusercontent.com/104705517/218764135-ea32183d-7c80-4ea2-a6fd-f27c2ef75dcf.png
.. |image6| image:: https://user-images.githubusercontent.com/104705517/218764186-11969d8c-d67c-4d6e-a46e-4d48e3280120.png
.. |image7| image:: https://user-images.githubusercontent.com/104705517/218764926-3eda90bf-ba1e-489d-b0b2-c6d48a883ce3.png
.. |image8| image:: https://user-images.githubusercontent.com/104705517/218764944-8ef1746d-bf6b-4b08-b9a5-a9849b23d28d.png
.. |image9| image:: https://user-images.githubusercontent.com/104705517/218765159-4d037b1f-dab6-439b-b368-b323ca176a70.png
.. |image10| image:: https://user-images.githubusercontent.com/104705517/218765186-af4eca5a-ae0a-499d-9de7-f765ac1f3d3f.png
