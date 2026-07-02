Maps
====



.. image:: ../images/image40.png
   :align: center



“So… what, exactly, is a map?”

Well you’re looking at one right now! Look at that banner. It’s a map!
Excluding the words and npcs…

A Map is the land that the party gets to move around on, and where
events are located.

Maps are located in the bottom left corner of the RPG Maker MV editor:



.. image:: ../images/image17.png
   :align: center



(source: FruitDragon)

.. _h.y2wi4nyj8sy8:

Basic Facts about Maps
----------------------

You can find all the information here at the bottom right of your
editor!!



.. image:: ../images/image25.png
   :align: center



(source: parallels, courtesy of FruitDragon)

#. The Coordinate System

Maps use a coordinate system of (x, y), much like most grids; however,
the origin, or the (0, 0), is located at the upper left corner, so
farther right equals a higher X value, and farther down means a higher
Y value.

Coordinates are how you decide where certain events go, based on the
tilemap, and they are also an easier way to figure out where to move
events around the map. Teleport scripts also use the coordinate system
to figure out exactly where to put the player.

2. Map ID

This is an ID number assigned to each map. In the example above, it’s
520. It’ll be very relevant later, when we’re discussing how to assign
tilemaps to maps, and it is how you can reference a map from another one
in Events.

3. Dimensions

The numbers inside the parenthesis. Basically, it tells you how large
your map is. This’ll also be very important when making tilemaps.

“FruitDragon,” you might say, “you’ve mentioned tilemaps, but what
actually is a tilemap?”

Tilemaps are what you see when you load a map in the game. Let’s go over
them in a bit more detail.

.. _h.mmbjv9ne17a2:

Tilemaps
--------



.. image:: ../images/image224.png
   :align: center



(source: map28, Kim & Vance’s house, basegame)

This is a Tilemap. They’re made of tiles, using the \ `Tiled
1.0.3 <https://www.google.com/url?q=https://github.com/mapeditor/tiled/releases/v1.0.3&sa=D&source=editors&ust=1782966892358962&usg=AOvVaw01okWJzzhbNkontRJcfLJh>`__\  software.
No other version will work correctly without external plugins.

(Note: You can use the \ `most recent Tiled
version <https://www.google.com/url?q=https://www.mapeditor.org/&sa=D&source=editors&ust=1782966892359223&usg=AOvVaw0h4KgFa3PoBN0-8HYwpj6x>`__\  alongside
the \ `tiledfixer plugin <#h.bgfu25fl9tkh>`__\ . It provides more
stability and support, and better tools. If you download it, however, it
overwrites your Tiled 1.0.3 software, so it’s best to install it in
every playtest you plan to edit maps in.)

All Tilemaps found in the game are in the maps folder in the playtest
folder.



.. image:: ../images/image41.png
   :align: center



(source: FruitDragon)

The maps themselves just look like a bunch of numbers when you open them
in a code editor. Definitely not like what you’d expect from the game.

When you open the same file with the Tiled editor though, this is what
shows up.



.. image:: ../images/image251.png
   :align: center



(source: map53, Artist & Angel’s house, basegame)

A Tilemap is made up of multiple Layers: the Layers below the
characters, the Layers on the same levels as the characters, the Layers
above the characters, and the Collision Layer. That Collision
Layer makes it so that the player can’t walk through objects, or
wherever you place a collision tile. It will not show up in-game.

In the photo above, the translucent red layer is a visual representation
of the Collision Layer. That same layer is made invisible in the image
of Vance & Kim’s house, mostly to make it easier to tell what things
are.

Where do the tiles used in Tilemaps come from, though?

.. _h.duuhxgwfm0h:

Tilesets
--------

Tilesets are included with the basegame. They’re basically just sets of
all the 32px by 32px Tiles that are used in Tilemaps.

They’re located in the same folder as the maps themselves
(playtest_folder/maps), and can also be opened with the Tiled map
editor. To use a Tileset in a Tilemap, you need to load the tileset in,
so that the Tilemap can access it.

The images associated with the tilesets (separate from the tilesets
themselves) are located in the img/tilesets folder, like so:



.. image:: ../images/image121.png
   :align: center



(source: FruitDragon)

Tilesets are generally densely packed, as shown above. This is so you
can have as many tile options as possible while having as few tilesets
loaded in at once as possible. Sure makes finding certain tiles in the
tilesets a pain, though… It certainly helps to look at previously
existing maps and find out which tilesets the tiles you want come from.

But how do we use all this to create a map?

.. _h.744w6vj0sw7n:

Creating Maps
-------------

Here is a \ `really good video
tutorial <https://www.google.com/url?q=https://youtu.be/pstj8qSbM0g&sa=D&source=editors&ust=1782966892362576&usg=AOvVaw32HtKu5k-SlHiMW0PT78Iv>`__\  on
how to create maps. I seriously recommend you watch it! However, I’ll
also go over it here in much more detail, too. And, as always, it helps
to experiment with the Tiled editor or watch a few tutorials about it,
too!

First, we have to make a new map in RPG Maker MV. It’s important to note
that the map organization is based on which map you have selected in the
editor when you create the map. Here’s an example:



.. image:: ../images/image140.png
   :align: center



(source: FruitDragon)

Right now, I have the Developer’s Room selected. When I create a new
map, it goes here, at the bottom of the Developers’ Room category.



.. image:: ../images/image115.png
   :align: center



(source: FruitDragon)



.. image:: ../images/image276.png
   :align: center



(source: FruitDragon)

However, when I select the main game…



.. image:: ../images/image248.png
   :align: center



(source: FruitDragon)

The map shows up here instead.

Don’t worry, though! If you end up creating your map in the wrong place,
you can drag and drop it to where you want it to go. Just drop it on the
map you want it to nest underneath.

So, now that we’ve got that out of the way… let’s get into making a map.

Right-click on the map category you want your map to fall under, then
click on New.



.. image:: ../images/image266.png
   :align: center



(source: FruitDragon)

It’ll open up the following window:



.. image:: ../images/image173.png
   :align: center



(source: FruitDragon)

There, you can name your map, change the width and height, make it
scroll if you want (making it an infinite map instead of a map bound by
the dimensions, think of the Endless Highway in Deeper Well or many of
of the rooms in Black Space) and add specific music to play when the
player enters the map.

Note: Display Name is usually what is shown as the name at Save Points.

It’s important to understand that background sounds persist between maps
if they aren’t directly changed. Toggling the selection but leaving it
blank cuts off any audio that’s already playing, though. For example, if
you have background audio, such as wind rustling through trees, that you
want to cut off when you walk inside a house, turning on the setting
like below but not selecting any sound will make it so that the music
will stop but there won’t be any audio playing in its place.

This is also the case for Battlebacks, the term used for battle
backgrounds.



.. image:: ../images/image163.png
   :align: center

  

(source: FruitDragon)

You can also add a parallax image. Parallaxes are located in the
img/parallaxes folder.



.. image:: ../images/image206.png
   :align: center



(source: FruitDragon)

They’re basically the background images of maps, and they show up when
the player moves to the edge of a map, or through empty gaps in maps,
such as in the Town Area in Black Space. Usually they’re considered the
sky of the map, but there are cases, mainly in Black Space, where
they’re something else.

You can make the parallax image move across the screen using the Loop
options. Feel free to fiddle with the numbers and find out how best to
do it!

So, here are my settings for this map:



.. image:: ../images/image225.png
   :align: center



(source: FruitDragon)

It’s important to note the ID (530, for me) at the top of the screen.
We’ll need this when we make our tilemap.

I also decided to have the map loop horizontally but not vertically,
similar to the Endless Highway. This means that the player won’t be able
to go past the top or bottom of the map, but can go left or right
indefinitely.

Once you’ve decided all your settings, make sure to click “OK” at the
bottom. Your new map should show up in the list of maps on the corner of
your RPG Maker MV editor!

And that’s all there is to do in RPG Maker MV. Now, it’s time to switch
over to Tiled.

Before we can do that, though, we need a tilemap to edit. In the maps
folder, find the following file:

maps/map00_Template_32x32.json



.. image:: ../images/image130.png
   :align: center



(source: FruitDragon)

Make a copy of it and rename it to mapXX (XX being the ID number we
noted down earlier). That’s how RPG Maker MV will know that the tilemap
we’re gonna make belongs to the map we made in RPG Maker MV.

Here’s mine:



.. image:: ../images/image150.png
   :align: center



(source: FruitDragon)

Now, open it in Tiled.



.. image:: ../images/image245.png
   :align: center



(source: FruitDragon)

This is what the resulting editing window will look like. First, before
we do anything else, we want to resize the tilemap to fit the dimensions
of our map in RPG Maker MV. We can do that by clicking on Map > Resize
Map from the toolbar at the top of the screen.



.. image:: ../images/image168.png
   :align: center



(source: FruitDragon)

Once that’s done, it’s time to make our map.

“But why are there so many layers? What do they all mean? How do I get
the tileset that I want?”

Let’s go over a few things about the Tiled map editor before we start
making our map.

.. _h.c6knh11gmt4l:

Loading Tilesets
~~~~~~~~~~~~~~~~

Loading a tileset is pretty simple.



.. image:: ../images/image31.png
   :align: center



(source: FruitDragon)

This window in the corner is where the tilesets show. If I want a
tileset that isn’t there, though, all I have to do is:

#. Locate the tileset in my file manager (usually, the name is the
   internal name of the area)
#. Click on Map > Add External Tileset
   

.. image:: ../images/image239.png
   :align: center



(source: FruitDragon)

3. Select the tileset that I want (make sure that the file type is set
   to .json)
   

.. image:: ../images/image45.png
   :align: center



And that’s all! The tileset that I want is now added to the map that I
just made, and I can freely use any tile from it in my tilemap.



.. image:: ../images/image128.png
   :align: center



(source: FruitDragon)

Note: Do not load every tileset at once. Learned this the hard way,
haha. There are some tilesets in the folder that don’t work due to
calling for images that don’t exist, and those will basically render
your new tilemap useless— not to mention that after a certain number of
tilesets (approximately 16), Tiled can no longer identify tiles
properly. I have gone through every single file in the maps folder, and
a list of every usable tileset is in \ `this
spreadsheet <https://www.google.com/url?q=https://docs.google.com/spreadsheets/d/157gbdncgn1_1sT9ZbLotL1KiRml7Y1oFKG7rZEccOA0/edit?usp%3Dsharing&sa=D&source=editors&ust=1782966892371222&usg=AOvVaw0CHXN3Fh16FroxER6VX8jA>`__\  for
your reference, with some styling and extra info from TomatoRadio.
Generally, if a tileset doesn’t have a corresponding image
in img/tilesets, it’s busted.

“What’s the difference between all of these layers? Which layer do I
use, though? What even is a layer?”

Well, I think it’s time to go over the next major part of making a map
in Tiled:

.. _h.54pr6pc8yb8l:

Layers
~~~~~~

Layers are what add depth to our maps. How else will we make it so that
some tiles go above the player, but other tiles are below the player’s
feet, and still others are on the same level as the player?

The answer is simple: Layering.

If you’ve ever heard of the Layers used in digital art and photo
editing, Tiled’s Layer system works much the same way. They go in order
from bottom to top, the topmost layer being the Region and Collision
layers, usually. This makes it easier to tell what parts of the map
you’ve already set as a certain region or blocked off, since they’re not
blocked by any tiles from layers above.



.. image:: ../images/image72.png
   :align: center



(source: FruitDragon)

The layer menu for an OMORI tilemap will look somewhat like this.

The naming convention for tile layers is as follows: GROUND, for tiles
that go under the characters’ feet. SAME AS CHARACTER, for objects that
they can interact with. And ABOVE ALL, for things like tree leaves and
overhangs (the secret path in Otherworld comes to mind) that the player
has to walk under. Then there’s COLLISIONS, for collisions, and REGIONS,
for region tiles; both of which we will go over later.

However, the game doesn’t read the layers with the name that Tiled has—
if you opened the map as is to RPG Maker MV, you’d get the characters
traveling around on a flat plane. (And worse, the collision layer and
region layer would be visible.) Instead, we have to set a few custom
properties. But how do we add custom properties?

.. _h.3swd68k6a8dj:

Adding Custom Properties
~~~~~~~~~~~~~~~~~~~~~~~~



.. image:: ../images/image63.png
   :align: center



(source: FruitDragon)

This is your properties window. By default, if you used the template,
you’ll already have two custom properties loaded in; priority and
zIndex. However, there’s more types of custom properties than just those
two. To add a new one:



.. image:: ../images/image68.png
   :align: center



(source: FruitDragon)

Click on the plus sign at the bottom.



.. image:: ../images/image37.png
   :align: center



(source: FruitDragon)

Put the name of the property in the corresponding box. You should
not change the data type of the property from ‘string.’



.. image:: ../images/image244.png
   :align: center



(source: FruitDragon)

You’ll be redirected to the Custom Properties bar, where your new
property will pop up. Once there, you can put in the value for that
layer.

.. _h.8h5e0uugfcqj:

Guide to Custom Properties 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most important properties that we’re gonna have to add, the ones
that need to be added to every single layer (excluding Region and
Collision layers) are zIndex and priority.

.. _h.6m2jfl5vulxq:

zIndex
^^^^^^

zIndex tells OMORI what layers are in relation to the player. OMORI
typically uses three different zIndex values:

1: Ground (below character)

3: Same as character (same layer as the player)

5: Above all (character goes underneath)

Note: The game is only able to display 256 Same as Character tiles at
once, so use them only when needed.

There are more possible values than this, but OMORI doesn’t use them, so
you don’t have to. Still, here’s a quick guide.



.. image:: ../images/image184.png
   :align: center



(source: \ `this google
doc <https://www.google.com/url?q=https://docs.google.com/document/d/1LyoDxBbtw4MUb7HirIZEaigpbJOcbwTelby7vttIAlg/edit%23heading%3Dh.dckld2q0kapk&sa=D&source=editors&ust=1782966892376861&usg=AOvVaw2_PrKN1bpRHBfZMRR2cy-m>`__\ )

.. _h.il08r9x6bhne:

Priority
^^^^^^^^

priority is basically in what order the layers should be loaded (as in
loaded into memory, not layering). Priority numbers reset with each
zIndex change. The lowest priority number with the lowest zIndex value
is loaded first, followed by the next highest priority layer loading on
top of it, and the next; until the zIndex goes up and the priority goes
back to 1.

A good way to visualize it is through a table. Each value in the
table is in the order (zIndex, priority) and it goes from left to right,
top to bottom.

==== ==== ==== ==== ====
1, 1 1, 2 1, 3 1, 4 1, 5
3, 1 3, 2 3, 3 3, 4 3, 5
5, 1 5, 2 5, 3 5, 4 5, 5
==== ==== ==== ==== ====

.. _h.6dcu8zc6ja26:

RegionId
^^^^^^^^

regionId is basically a way to apply an effect to sections of your map.
There are a few different RegionIds that have specific effects on the
party. These can be set by setting the “regionId” custom property to the
specific id.

The effects are:

1: Used to make the mirrors in Headspace reflect the player.

10: Makes the player slide. The Snowglobe Mountain ice uses this.

20: Acts as a collision tile, but only for events, not the player. The
rugs in the Last Resort use this.

28: Makes footprints appear. Sand and snow use this, as do the bloody
footprints from the Truth Sequence. To make the bloody footprints show
up, however, you have to turn on Switch 84 ‘used in recital’.

90: Makes the party use their climbing sprites. All ladders use this.

92: Flashes the screen red and damages the party for 10 Heart. Cannot
kill. Used by the shattered mirror in Black Space 2.

The tileset “Tile_Region_32x32” has tiles for regions 1-127. These don’t
have any inherent effect on regions, but they are good for labeling.

You can use Regions to make JavaScript checks on where the player is
with $gamePlayer.regionId(). For example if you need to check if the
player is in Region 3, just use $gamePlayer.regionId() === 3. In
addition, you can use plugins to run a common event when a player stands
in a certain region.

There is one big limitation however to keep in mind however. A tile can
only be assigned one region. So you can’t for example, have a patch of
snow that leaves footprints with Region 28. Those tiles are not able to
also block event movement with Region 20.

.. _h.pqgfttwpjtgu:

Collision
^^^^^^^^^

collision is basically what makes a Layer a Collision Layer. All
collision layers are automatically set to invisible when loaded in game,
and they are used with a special tileset known as
TileCollision_32x32.json, located in the maps folder (though it’s
automatically loaded in with the template map.)

When you create a collision layer, all you need to do is set the
collision property to tile-base, like so:



.. image:: ../images/image262.png
   :align: center



(source: FruitDragon)

Note: The Collision Layer in the template map is already set up
correctly

.. _h.ok4qspe7hp9b:

Levels 
^^^^^^^

In addition, you can also make multiple Levels on your map in order to
create layouts where for example you can pass under bridges taking one
path, but that you walk over on a different path.

Levels are easily the most complicated of these properties, so I’ll
break it down into the two parts of it.

.. _h.5rwfcmuncpe0:

To Level Tiles
''''''''''''''

The first thing we’ll need is to create two new layers, which we’ll call
TO LEVEL 0 & TO LEVEL 1. What these are going to do is that when we pass
by a tile on that layer, it will move the player up or down to the
corresponding Level. Usually the transition is placed on the “path”
(ladder, stairs, etc) that takes you between layers, where TO LEVEL 0 is
at the bottom and TO LEVEL 1 is at the top, looking similar to this
crudely drawn diagram.



.. image:: ../images/image253.png
   :align: center



(Source: TomatoRadio)

Conveniently, the Collision Tileset has tiles to mark these tiles on the
map for ease of use. 

.. image:: ../images/image42.png
   :align: center



However, we need Custom Properties to get these layers to actually do
anything.



.. image:: ../images/image60.png
   :align: center



(Source: TomatoRadio)

First, the level property marks what Level the layer is on. By default,
all layers are on Level 0.

Next, the toLevel property marks that when stepping on a tile of this
layer, the player is moved to the specified Level, here being 1.

Now make an inverse version for returning to Level 0 and you have your
transition layers done!

.. _h.1be4xd4z0nt3:

Level Layers
''''''''''''

Now that we have the ability to move between Levels, we need to create
the layers that change between levels.

Once again, we’ll need two types of Custom Properties.



.. image:: ../images/image53.png
   :align: center





.. image:: ../images/image194.png
   :align: center



(Source: TomatoRadio)

Here we have an Above All layer and a Ground layer, respectively. This
Above All will only display if the player is on Level 0, and the
Ground Layer will only display if the player is on Level 1.

These are done with these two properties:

Level once again simply marks what Level a layer is on.

HideOnLevel is pretty self-explanatory— if the player is on the
specified level, then the layer is hidden.

When used in pairs like these, we can create objects like bridges that
act as Above All when on Level 0, and act as Ground when on Level 1.

Lastly, in maps with Levels, collision and region layers need to be made
for both levels, using the same properties as above.

Still don’t understand? Scroll down to the \ `Level
section <#h.mbezaci7kne4>`__\  in the Making Our Map heading for a more
step-by-step explanation.

.. _h.xeqmo5erxcjt:

Making Our Map
--------------

Now let’s use what we’ve learned to make our map!



.. image:: ../images/image12.png
   :align: center



(source: FruitDragon)

Here’s my editor in its entirety. My plan is going to be a map of
islands connected by bridges that the player can move around, with
ladders leading into the water so that the player can swim underneath
the bridges and between islands. Let’s see how to implement that!

For this we’ll need two levels: one for the ground layer with the
islands, and one for the water. They’ll need different collision
layers as well.

I’m going to start building the island layer first. I’ll start with the
terrain tiles and set up a basic idea of what I want my terrain to look
like.

“Wait— terrain tiles?”

.. _h.w249jq4tobw:

Terrain Tiles
~~~~~~~~~~~~~

Terrain tiles are a much much easier way of tilemapping, especially with
tiles such as land tiles. Instead of having to manually place each piece
and potentially getting mixed up, Tiled has a way of doing it
automatically with the use of Terrain Tiles.

To create Terrain Tiles, simply open the tileset in the Tiled editor by
clicking “Edit Tileset”, then set them up. It’s the little icon with the
wrench.



.. image:: ../images/image109.png
   :align: center



(source: FruitDragon)

Now that you have your tileset open, click the icon that looks like a
tiny tilemap to open the Terrain Sets editor.



.. image:: ../images/image242.png
   :align: center



(source: FruitDragon)

Click the plus sign and add a new Corner Set.

Note: If you are using v1.0.3, then it will not prompt for what type of
Terrain Set you want, as v1.0.3 only has Corner Sets.



.. image:: ../images/image139.png
   :align: center



(source: FruitDragon)

Feel free to name your terrain set whatever you want! I just named mine
after the tileset I’m using, DW_VastForest.



.. image:: ../images/image177.png
   :align: center

  

(source: FruitDragon)

Now all you have to do is set up the terrain set like below. To do this,
all you need to do is drag your mouse where you want the terrain to be.
All this is doing is defining what type of tile each of these tiles are—
a top tile, a corner tile, an inverted corner tile, etc. Make sure to
save!



.. image:: ../images/image198.png
   :align: center



(source: FruitDragon)

Then, you can navigate to ‘Terrains’ at the bottom of the editor and
select your terrain set.



.. image:: ../images/image108.png
   :align: center



(source: FruitDragon)

Now you can simply drag your cursor and your land will be made
perfectly, just like that!



.. image:: ../images/image191.png
   :align: center



(source: FruitDragon)

Note: OMORI does come with a premade set of Terrain Sets, in
TerrainTiles.json. If you load that tileset to your map, it will
automatically load the corresponding Terrain Sets for your access.

Now let’s go back to making our maps.

.. _h.vh0gxfz6yi3u:

Making the Map
~~~~~~~~~~~~~~

Here, I’ve gone and set up an island archipelago using the light green
grass from Vast Forest (DW_VastForest.json, or more specifically the
Vast Forest grass in TerrainTiles.json) and the medium blue water from
North Lake (DW_NorthLake.json). I used the bottom two layers— GROUND -
I for my water, and GROUND - II for the islands. It’s looking pretty
good so far!



.. image:: ../images/image279.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Now I’m interested in making the bridge system. I’ve created some custom
bridge tiles by editing the bridges from DW_NorthLake.json, so I’ll be
using those.



.. image:: ../images/image89.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Looking nice! I decided to make it so that in order to reach some of the
islands, the player will have to go through the water instead of only
using the bridges to navigate. I also like how it’s a little bit like a
maze. I ended up using two layers for this, GROUND - III and GROUND -
IV, because of some overlap between tiles that required using a second
layer.

Speaking of going through the water, the player will need to be able to
get into the water. Let’s put down some ladders.



.. image:: ../images/image193.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

I used some of the ladder tiles from general_use.json for this. There
are quite a few types of ladders on that tileset! I’ll put these on
GROUND - V.

But wait, I’ve already run out of GROUND layers!

That’s okay. To create a new layer, all I need to do is right-click the
layer window, then click New > Tile Layer.



.. image:: ../images/image284.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

After that, I can name it whatever I want. I’ll put custom properties at
the end, once I’m finished with the map, in case I need more layers.



.. image:: ../images/image105.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Now it’s probably a good idea to add some detailing. Things like grass
tiles, flowers, and trees. For detail work, I like to go section by
section— in this case, island by island— so I don’t lose track of where
I’ve done detailing and where I haven’t. I’ll start with adding grass
and flowers, then add trees on a different layer.

Note: For detailing with multiple variants of a single-tile piece of
decor, like grass tufts or flowers, you can select all of the tiles you
want by holding ctrl and then enable the random tool, which looks like a
pair of dice. This will make every tile you place be a random one of the
selected tiles. This also works on the fill and rectangle tools.



.. image:: ../images/image71.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)



.. image:: ../images/image207.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

All of these grass and flower tiles are on the
DW_VastForest.json tileset. Now for trees. I’m going to place the bottom
half of the trees on the GROUND layer, and place the top half of the
trees on the ABOVE ALL layer. This is so that we can appear above the
stump, but behind (below) the leaves.

Note 1: This is a good time to remind you that you can select multiple
tiles (without the random tool), and be able to mass-place them with the
rectangle tool. This is especially useful for blocking out where trees
will be.

Note 2: For small amounts of trees, you can also place them on the SAME
AS CHARACTER layer; however, there is a limit to how many of these tiles
will be visible to the player at once, and will display as invisible if
exceeded.



.. image:: ../images/image274.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

I decided to add bushes on the same layer as the trees. These are also
from the DW_VastForest.json tileset.

Also, I saw a submerged tree tile on DW_VastForest.json that seems cool
to add in the water. Let me add a few of those. I’m going to add these
on the same layer as my land tiles for ease (GROUND - II).



.. image:: ../images/image171.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

With that, I’m done with my tilemap!

…Or at least I would be if I didn’t need collision. And region layers.
Oh, and levels, of course.

On that note, let’s get our land and water level system set up. You can
skip to the \ `Region and Collision <#h.hv052rq283sr>`__\  section if
you’re not interested in making a level system.

.. _h.mbezaci7kne4:

Levels
~~~~~~

Because I want the player to start on the land, I’m going to make that
Level 0. RPG Maker MV automatically sets a player to Level 0 when they
enter a map, so that’s the easiest option. This makes our water layer
Level 1, since that’s the level that the player has to transition on to.

When the player is on Level 1, I want the bridge to go above the player.
In order to do that, I’m going to make a duplicate of my two bridge
layers and set them to Above All.



.. image:: ../images/image144.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Of course, I need to remember to set my zIndex to 5!



.. image:: ../images/image106.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

.. _h.i6g3tk6bxuj8:

level and hideOnLevel
^^^^^^^^^^^^^^^^^^^^^

Now it’s time to add the level and hideOnLevel properties. The ground
bridge needs to be hidden when the player is in the water (Level 1), and
the above all bridge needs to be hidden when the player is on land
(Level 0). Let’s see what that looks like.

My GROUND bridge:



.. image:: ../images/image133.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

My ABOVE ALL bridge:



.. image:: ../images/image215.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Now to set up a way for the player to go between those levels. Because
the only way from the water to the land and vice versa is through the
ladders, I only need to set up a transition next to each ladder.

You’ll want to create two layers like this, preferably at the top of
your layers list for organization purposes.



.. image:: ../images/image180.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

TO LEVEL 1 will be located at the base of the ladder, while TO LEVEL
0 will be located at the top of the ladder. Let’s see what that looks
like.

.. _h.lsfiao7qtahz:

TO LEVEL 0:
^^^^^^^^^^^



.. image:: ../images/image278.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The “LVL 0” tile shown is from the Tile_Collisions_32x32.json tileset.
Here’s what the Custom Properties look like:



.. image:: ../images/image267.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

.. _h.xc88rfjemkb5:

TO LEVEL 1:
^^^^^^^^^^^



.. image:: ../images/image147.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The “LVL 1” tile shown is from the Tile_Collisions_32x32.json tileset.
Here’s what the Custom Properties look like:



.. image:: ../images/image294.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

.. _h.la0zlwojldex:

Final Note
^^^^^^^^^^

And that’s about it! Make sure to do the hideOnLevel and level
properties for any other layers that change between levels. For any
layers that don’t change between levels, however (such as the water
layer and the land layers for my map), you don’t need to add a level or
hideOnLevel property. Those ones will remain the same regardless of what
level that you are on.

However, for REGION layers and COLLISION layers, you will need to have
separate layers for each level. The COLLISION layer is especially
crucial, as if you don’t have a separate collision layer for every
level, the game will break.



.. image:: ../images/image211.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The custom properties for these will look something like this.

Collision:



.. image:: ../images/image64.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Region (Region 90):



.. image:: ../images/image210.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Now let's talk about making these region and collision layers.

.. _h.hv052rq283sr:

Region and Collision
~~~~~~~~~~~~~~~~~~~~

.. _h.lhdbh6c7uyg5:

Collision
^^^^^^^^^

Making a collision layer is simple. There’s a tileset, called
Tile_Collisions_32x32.json, that is used for collision layers.



.. image:: ../images/image151.png
   :align: center



(source: FruitDragon)

The red collision tile, known as the full collision tile, is the tile
that we generally use most for collision. It’s the easiest to use and
the hardest to mess up. The player and other events (barring those with
Through turned on) cannot step onto these tiles in any way.



.. image:: ../images/image196.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The other collision tiles (ignoring the LVL 0, LVL 1, and LVL
BLK tiles), known as partial collision tiles, are slightly different.
With these tiles, the player will still be able to walk onto the tile
with a partial collision tile, but only from the direction marked with
an arrow. Similarly, the player will only be able to leave the tile from
the direction marked with an arrow. Therefore, these are used in much
rarer cases, where the ‘wall’ is between two tiles.

In the example below, I didn’t want the player to be able to access the
ladder from the side, so I used a partial collision tile.



.. image:: ../images/image185.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Basegame also uses these for things like poles.



.. image:: ../images/image149.png
   :align: center

 

.. image:: ../images/image183.png
   :align: center



(sources: map63, Faraway Park, basegame; and map383, Beach Memory,
basegame)

Once a collision layer is done, add the collision Custom Property to it.



.. image:: ../images/image250.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

And that’s about it for collision! With Levels, each level needs to have
a separate collision layer, but otherwise, collision is complete.

.. _h.ur8ac4njpw83:

Region
^^^^^^

I need to add Region 90 to my map on the ladders, so that the player has
a climbing animation when they climb it. How do I do that?

A region layer is just as simple as a collision layer. Just like
collision, there’s a tileset known as Tile_Regions_32x32.json, which is
the tileset that we use for regions.

For my Region 90 layer, I’ll use the tile marked with a ‘90’. All I need
to do is put the ‘90’ tile on each ladder.



.. image:: ../images/image199.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

And to finish it off, I’ll make sure my regionId Custom Property is set
to 90.



.. image:: ../images/image56.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

When working with regions, however, it’s important to note that if you
put two different region tiles on the same tile in two separate region
layers, they cancel out. So watch out for that! Also, make sure to have
separate region layers per level.

.. _h.32pa3rmtd2dr:

Organization
~~~~~~~~~~~~

Organization is really, really important when it comes to making maps.

Because right now? My map is a total mess.



.. image:: ../images/image264.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Not to mention, my zIndex and priority Custom Values aren’t lined up
properly. But I can barely tell what anything is supposed to be, let
alone what zIndex and priority values go where.

So how do I organize this?

.. _h.vr5yao4107kr:

Step 1: Delete Unused Layers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. image:: ../images/image78.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

This is already looking significantly better. Way less overwhelming and
easier to deal with.

.. _h.ycgknkie60k4:

Step 2: Rename All Layers
^^^^^^^^^^^^^^^^^^^^^^^^^

It’s so much easier if all of your layers use the same name scheme. It
doesn’t have to be the basegame’s naming scheme of “GROUND - I, SAME AS
CHARACTERS - I, ABOVE ALL - I,” though that’s what I’ll be using. Other
schemes you could use could be something like “G1, S1, A1” or “Ground 1,
Character 1, Above 1.” Whatever works best for you!



.. image:: ../images/image94.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

.. _h.gpmwhl65zbm1:

Step 3: Levels
^^^^^^^^^^^^^^

A little something I like to add is Level Specification. This helps on a
map with multiple levels, especially to help me tell what layers are a
duplicate of other layers so that if I edit one layer, I remember to
edit the other layer.



.. image:: ../images/image83.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

.. _h.ug8c9ees54j1:

Step 4: Priority and zIndex
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, I can figure out what my custom properties are! Going from the
bottom up, I can put the proper zIndex and priority without much of a
struggle because of my map’s organization.

And that’s it! You have a fully finished map!

Because you named the map mapXX (XX being the ID of the map in RPG Maker
MV), it should load perfectly fine upon accessing that map in the game.

…Right?



.. image:: ../images/image116.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Well. It’s not there. Upon playtesting the game, it loads fine, but it
sure doesn’t show up in the editor. How do I make it appear so that I
can place events without having to go back and forth between Tiled and
RPG Maker MV?

Simple: by loading a parallax. (Or by using \ `OneMaker
MV <#h.4a99xvlix9d1>`__\ .)

.. _h.26aes05t898p:

Loading a Map in RPGMaker MV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have
\ `OneMaker <#h.4a99xvlix9d1>`__\ ` MV <#h.4a99xvlix9d1>`__\ , you can
skip to the \ `‘Loading a Map in OneMaker MV’
section <#h.1qxync9w9sll>`__\ . If you don’t have it, I recommend you
get it— it has a lot of amazing tools that OMORI modders can really use.
But if you don’t want to, or can’t, I’ll walk you through the steps to
loading a map into the editor in base RPG Maker MV.

First, we’ll need to open the map that we want to load into RPG Maker
MV in our Tiled editor.



.. image:: ../images/image52.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Set the zoom level to 150%. This is important. Importing the map to
RPGMaker will not work properly otherwise.



.. image:: ../images/image217.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

(Note: This is because OMORI’s tile size is 32x32 pixels, while RPG
Maker MV’s tiles are all 48x48 pixels. Setting the zoom to 150% is how
we increase the size of the map from 32x32 to 48x48 pixel tiles,
ensuring everything lines up properly.)

Next, I’ll need to export the map as an image. I can do this by
selecting File > Export as Image.



.. image:: ../images/image269.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

It’ll open the following window.



.. image:: ../images/image165.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The only two boxes you should have checked are “Only include visible
layers” and “Use current zoom level”. Assuming that your collision and
region layers are hidden, this will ensure that your entire map is
visible and the proper size for RPG Maker MV.

In addition, you’ll need to change the filepath for where your image is
going to be located. It exports to the following file path by default:

…/www_playtest/maps/mapname.png

Instead, change ‘maps’ to ‘img/parallaxes’.

…/www_playtest/img/parallaxes/mapname.png

You can set the name of the map to whatever you want, but it’s usually
easiest to just keep it in the mapXX format.



.. image:: ../images/image79.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Now that that’s done, click ‘Export’!

It’s time to go back to RPG Maker MV.

Right click on the map name in the map list on the left of the screen,
then click ‘Edit’.



.. image:: ../images/image66.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

It’ll open the following window:



.. image:: ../images/image39.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The section we’ll need is the Parallax Background section. Open the
image selection window and locate the map image you just exported. It’ll
only show images in the img/parallaxes folder, which is why we had to
put it there instead of the maps folder.



.. image:: ../images/image237.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Click “OK”, then make sure the “Show in the Editor” checkmark is
selected. It should look something like this:



.. image:: ../images/image148.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The ‘Loop Horizontally’ and ‘Loop Vertically’ checkmarks won’t affect
anything, so if you already have a moving parallax that you’re being
forced to replace with this, you can leave the scroll settings intact.

Now, once you exit out of the map editing window, your map will
automatically show up in the editor!



.. image:: ../images/image230.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

If you’re replacing a parallax, though, just make sure to remember to
switch the parallax back to the original once you’re done or when you’re
compiling or exporting.  

As a note, you can do this method in OneMaker MV, but you don’t have
to. There is a far easier method.

.. _h.1qxync9w9sll:

Loading a Map in OneMaker MV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don’t have OneMaker MV and have no intention or method of getting
it, you can \ `skip this section <#h.m2ks2m2si3vf>`__\ .

When in OneMaker MV, upon opening the map editor, you’ll find that the
“Show in the Editor” checkmark has been replaced by a checkmark labeled
“Show Tiled Maps”. This is because all parallax images are rendered on
the map by default, and Tiled maps are separately rendered.



.. image:: ../images/image285.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

It still doesn’t work automatically, but it’s now a lot easier to save
and export.

.. _h.7foqhu7wzjgb:

Automatic Map Rendering Tool (OMORI Map Renderer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have a lot of maps that you want to export renders for, you can
use the \ `OMORI Map
Renderer <https://www.google.com/url?q=https://github.com/rphsoftware/omori-map-preview-renderer/actions/runs/20416117980&sa=D&source=editors&ust=1782966892416921&usg=AOvVaw26C29L-j1YEezrNmhx-Adb>`__\  to
export them automatically. Simply go to the link, scroll down, and
download the version for your OS (shown below).



.. image:: ../images/image227.png
   :align: center



(source: FruitDragon, GitHub)

I’ll be using the Windows OS version.

Next, bring the application to your playtest folder and drop it in. It
should be located in the same folder as your Game.rpgproject file.
(Note: The file may not be called 'renderifier.exe' for you.)



.. image:: ../images/image81.png
   :align: center



(source: FruitDragon)

Run the application. You should get a terminal window that looks
something like this:



.. image:: ../images/image24.png
   :align: center



(source: FruitDragon)

Caution: it’s laggy and takes a lot of processing power from your
machine. Be aware of this. You may not be able to do anything while it’s
rendering, or your computer battery may drain faster, etc.

The OMORI Map Renderer creates two folders in your playtest, scaled and
render. The render folder has all the maps your maps folder exported at
100% zoom level, which is what OneMaker MV will use. The scaled folder,
on the other hand, contains all the maps in your maps folder exported at
150% zoom level. This is the size that you would use were you adding the
maps to RPG Maker MV as parallaxes. Thankfully, we don’t need to do
that.

The folders would appear something like this in your File
Explorer window, in the same folder your Game.rpgproject file is in:



.. image:: ../images/image61.png
   :align: center



(source: FruitDragon)

Now you can simply open your RPG Maker MV project and the maps will
automatically be rendered by OneMaker MV.



.. image:: ../images/image255.png
   :align: center



(source: map14, Player’s House (Day), basegame, in the OneMaker
MV editor)

To disable the Tiled map view on any map, simply uncheck the “Show Tiled
Maps” checkmark for that map. You’ll be left with the checkered event
grid instead.



.. image:: ../images/image202.png
   :align: center



(source: FruitDragon)

And don’t worry, the Tiled maps won’t show up in game! Parallaxes will
still be visible with them on, too. Here’s an example.

Without the Tiled map:



.. image:: ../images/image95.png
   :align: center



(source: map55, Shopping Center (Day), basegame, in the OneMaker
MV editor)

With the Tiled map (edited slightly for testing purposes lol):



.. image:: ../images/image122.png
   :align: center



(source: map55, Shopping Center (Day), basegame, in the OneMaker
MV editor)

The same map, loaded in the playtest:



.. image:: ../images/image22.png
   :align: center



(source: map55, Shopping Center (Day), basegame)

Okay, this is cool and all, but now comes the part that I know you’ve
all been waiting for.

Rendering custom maps.

.. _h.l4c9pn74zvqx:

Custom Maps (Tiled)
^^^^^^^^^^^^^^^^^^^

Unfortunately, the OMORI Map Renderer doesn’t support rendering custom
maps (This section is deprecated, it does do that now). This means we’ll
have to render the maps ourselves in Tiled.

(Note: This method works for basegame maps as well. If you only want to
render one or two maps from the basegame instead of all of them, it’s
recommended you use this method instead.)

However, this is a lot easier than doing it without OneMaker MV, because
now we don’t care about the zoom level.

Before exporting the map, though, we’ll first have to make sure the
render folder exists. If you don’t already have one from the OMORI Map
Renderer, create a new folder in your playtest folder (the same folder
that contains Game.rpgproject) and name it ‘render’. That’s all you need
to do.

Going back to using the Vast Forest Maze example, we’ll have to open the
map in Tiled again.



.. image:: ../images/image52.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

Don’t bother setting the zoom level.

Now I’ll need to export the map as an image. I can do this by selecting
File > Export as Image.



.. image:: ../images/image269.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

It’ll open the following window.



.. image:: ../images/image165.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

The “Only include visible layers” is the only box that needs to be
checked. Not setting it to “Use current zoom level” will make it so that
it exports at 100% size by default.

Change the ‘maps’ in the file path to ‘render’, like so.



.. image:: ../images/image146.png
   :align: center



(source: FruitDragon, a map made for The Dreamer)

And that’s it! Export!

Now, if you open your map in OneMaker MV, it’ll show up in the editor.
Amazing, right?

“But, FruitDragon,” you say, “now I know how to make a custom map and
load it in OneMaker MV, but how do I make a custom tileset? You
mentioned those earlier but didn’t talk about them!”

Oh, right, I did! Well, it’s really easy! Let me show you.

.. _h.m2ks2m2si3vf:

Custom Tilesets
---------------

Before you start with your custom tileset… you need a custom tileset
image. The \ `Tilesets section <#h.1zgigevc1sol>`__\  under the Sprites
and Art heading talks more about the specifications of those, so I won’t
go over that here.

Here’s my tileset:



.. image:: ../images/image268.png
   :align: center



(source: FruitDragon, edited version of DW_CattailField.png)

It’s just an edited version of DW_CattailField.png, turning it pink.
Make sure to put your tileset image in the img/tilesets folder!

Next, I’m going to make a new tileset in Tiled. Go to File > New >
Tileset.



.. image:: ../images/image243.png
   :align: center



(source: FruitDragon)

It’ll open to the following window:



.. image:: ../images/image221.png
   :align: center



(source: FruitDragon)

You can name it, but you don’t need to. Instead, click “Browse” and
locate your tileset image in the tilesets folder. If you don’t put
anything in the Name box, your tileset will automatically take the name
of whatever the image of your tileset is.



.. image:: ../images/image8.png
   :align: center



(source: FruitDragon)

The rest of the settings can be left as default. Save the tileset in the
maps folder as whatever you want.
\ `Tiledfixer <#h.bgfu25fl9tkh>`__\  users, make sure you save the
tileset as .json. You can do this by selecting “JSON tileset files” and
then manually typing .json at the end of the file name, then clicking
“Save”.



.. image:: ../images/image275.png
   :align: center



(source: FruitDragon)

As soon as you’re done with that, your new tileset should pop up in
Tiled.



.. image:: ../images/image190.png
   :align: center



(source: FruitDragon)

After that, you can do whatever you want with it! It’ll automatically
pop up in the tilesets list of any map you have open, so you can start
using it immediately.

 “But wait! FruitDragon! How do I animate tiles?”

.. _h.r0kkl9qkm62j:

Animating Tilesets
^^^^^^^^^^^^^^^^^^

To animate tiles, first click on the tile you want to animate. Then,
click on the video camera icon thing at the top to open the Tile
Animation Editor. I don’t really know what the icon is called lol.

“It’s called a film camera.” - TomatoRadio



.. image:: ../images/image222.png
   :align: center



(source: FruitDragon)

It’ll open up this window.



.. image:: ../images/image232.png
   :align: center



(source: FruitDragon)

Here, you can drag tiles into the animation editor and set the
milliseconds that tile is shown for. Setting the frame duration at the
top sets the default time that is set when you drag a tile into the
editor.



.. image:: ../images/image27.png
   :align: center



(source: FruitDragon)

Here’s the typical animation for water.

And once you’re done, all you need to do is close the window!

An interesting trait of Tiled is that animation is only stored on one
tile, instead of all tiles that the animation includes.

This means that if you want to have the animated tile play at different
speeds in different areas, you can start the animation on a
different tile and it will be stored separately.

What happens if you want to replace all of one tileset with an edited
version of that tileset, though? What do you do then?

.. _h.m94arvi4oxvp:

Replacing a Tileset
^^^^^^^^^^^^^^^^^^^

Well, if you’re using the OMORI-specific 1.0.3 version of Tiled, it’s a
fairly in-depth process. It’s a lot easier if you’re using the most
recent version of Tiled with the \ `Tiled
Fixer <#h.bgfu25fl9tkh>`__\  plugin, but still doable without. So, let’s
say I wanted to replace DW_Cattail.json with my
DW_CattailFieldPink.json in one of the Otherworld maps. First, I’d have
to locate which map.

Here’s the map I picked:



.. image:: ../images/image273.png
   :align: center



(source: FruitDragon)

Now, I need to locate it in the maps folder.



.. image:: ../images/image179.png
   :align: center



(source: FruitDragon)

Then I need to open it with my code editor of choice. I’ll use \ `Visual
Studio
Code <https://www.google.com/url?q=https://code.visualstudio.com/&sa=D&source=editors&ust=1782966892430008&usg=AOvVaw1ahPe6fhdd1yVsRotS1i43>`__\  for
this.

It takes me to a window that looks like this:



.. image:: ../images/image156.png
   :align: center



(source: FruitDragon)

Scroll all the way to the bottom, and you’ll find the names of the
tilesets.



.. image:: ../images/image241.png
   :align: center



(source: FruitDragon)

Simply replace “DW_Cattail.json” with “DW_CattailFieldPink.json”. Then
open your map and see what it looks like now!



.. image:: ../images/image93.png
   :align: center



(source: FruitDragon, edited map118.json)

And would you look at that! Pink Cattail Field! Though… it only replaces
DW_Cattail.json and not DW_Junkyard.json, which is why not all of the
tiles are replaced with pink. You would need to edit all the tilesets
that the map requires in order to replace an entire map this way.

To replace tilesets if you have the most recent version of Tiled
(through the \ `Tiled Fixer <#h.bgfu25fl9tkh>`__\  plugin), the above
method would still work for you. But you also have access to a much
easier way. Select the tileset you want to replace, then click on the
“Replace Tileset” icon here. After that, locate the tileset you want to
replace it with in the file explorer window that pops up. And that’s
all!



.. image:: ../images/image154.png
   :align: center



(source: FruitDragon)

And now that’s the end of this in-depth guide to Tiled and
tilemap-making! I hope it was helpful!

(Also, yes, the map I used as a tutorial for making maps was the Vast
Forest Maze map from \ `The
Dreamer <https://www.google.com/url?q=https://mods.one/mod/thedreamer&sa=D&source=editors&ust=1782966892432241&usg=AOvVaw2E8FUGJaColDWtg6xn-4It>`__\ .
It’s a map that I, FruitDragon, made for that mod!)

Onto the next thing:

.. _h.gsbdya7y8lgi:
