Sprites and Art
===============



.. image:: ../images/image252.png
   :align: center



Now, I hear what some of you are thinking, “FruitDragon, events and
tilemaps are nice and all, but I don’t want them to look like they do.
What if my mod takes place in the war-tattered wreckage of the Black
Mesa Research Facility? How do I make that?” Well first, I’m not
FruitDragon, this is the point where we switch over to TomatoRadio
mainly guiding you. Secondly, I can’t draw, so that part is on you. But,
I can tell you how to format that art.

This section will detail the formatting of every image type in OMORI, so
that you know how to make them for your own purposes.

Note: All of these images are found in the img folder, which has
numerous subfolders, which is how I’m categorizing these. The subfolders
do matter, and they determine what an image is used for.

.. _h.qcht5dp9swo1:

Overworld Sprites
-----------------

The majority of overworld sprites in OMORI are stored in the
"characters" folder as spritesheets. More specifically, these are the
images that Events can be set to use. Now before I show you all the ways
these can be set up, I’ll show you how these work at a basic level.

This is the most basic spritesheet you can have in OMORI. They are made
up of 8 3x4 sets of sprites, all uniform in size. The size of the
sprites between spritesheets can vary, as long as they follow this
format. Each of these 8 sets make up a “section,” as I’ll call them.
These sections will have 3 sprites of movement in the 4 cardinal
directions as pictured below. You don’t need to do anything to make the
animations work aside from lining them up correctly.



.. image:: ../images/image258.png
   :align: center



(source: DW_NPC_10.png, basegame)

Now. As you can see here, Capt. Spaceboy’s spritesheet, while sized the
same, has a few “sections” that don’t follow this structure at all. Many
spritesheets will also store character animations in the same sheet.
These are called through scripts in the event coding.



.. image:: ../images/image86.png
   :align: center



(source: DW_SBF.png, basegame)

Now. This is actually just one of 5 ways that these sheets can be set
up. And the way these formats are chosen is by their file name. RPG
Maker MV (or plugins) will check the filenames of all loaded
spritesheets to see how to split them. I will show you now what these
look like.

If a $ is added to the front of a filename, it becomes a 3x4 sheet
designed for one character/section. This is best for animated characters
or objects with special dimensions.



.. image:: ../images/image28.png
   :align: center



(source: $glassomori.png, basegame)



.. image:: ../images/image134.png
   :align: center



(source: $BS_Raft.png, basegame)

If [SF] is added to the front of a filename, it becomes a single image
designed for one character/section. This is best for unanimated
characters or objects with special dimensions.

Note that in the Event Editor, it will be divided into a 12x8. Don't
worry about that, it will show as one sprite in game.



.. image:: ../images/image47.png
   :align: center



(source: [SF]Blanket_Fort_Empty.png, basegame)



.. image:: ../images/image200.png
   :align: center



(source: [SF]FA_basil_TV.png, basegame)

If %(x) is added to the back of a filename, it extends the amount of
walking sprites by the number that takes the place of x. This is used by
the overworld somethings and running sprites. In addition, due to the
plugin that OMORI uses for this feature being older than the version of
RPG Maker MV that OMORI uses, this plugin is slightly buggy and will
only work on $ images. If you need/want to use larger sheets, you can
use \ `this Galv
plugin <https://www.google.com/url?q=https://galvs-scripts.com/2015/12/12/mv-character-frames/&sa=D&source=editors&ust=1782966892436993&usg=AOvVaw0DM45MKdZZccwLXu-WDMCP>`__\ ,
which works nearly the same. (This is OMORI-exclusive. If you try this
feature in base RPGMaker MV, it will not work.) 

Note that in the Event Editor, it will be divided into a 12x8 or 3x4.
Don't worry about that, it will show correctly in game.



.. image:: ../images/image265.png
   :align: center



(source: $DW_BASIL_RUN%(8).png, basegame)



.. image:: ../images/image290.png
   :align: center



(source: $bs_en_nanci%(7).png, basegame)

In RPG Maker MV, characters are automatically shifted up 6 pixels in
comparison to the map. This is to add a sense of depth. However, if you
want this disabled for certain sprites, like doors, you can add ! to the
front of the filename in order to disable this.



.. image:: ../images/image161.png
   :align: center



(source: !FA_PLAYERHOUSE_OBJ.png, basegame)



.. image:: ../images/image4.png
   :align: center



(source: !objects_fa_doors_sunset_2.png, basegame)

.. _h.anmh2bbipons:

Dialogue Portraits
------------------

These made a brief mention in the
\ `YAML/Dialogue <#h.eyo0h7t5nx1p>`__\  section, but might as well go
slightly more in depth for sake of completeness.

All dialogue portraits are stored in the "faces" folder. These follow a
very specific format that can't be deviated from.

Each image (as in png file) is a "faceset" containing 4 106x106px faces
per row, though you can add effectively as many rows as you want.
Seriously, you can merge every faceset in the game into one image and it
works fine.

Each face in the faceset has a number assigned to it, being its
"faceindex." These start at 0 and go left to right, top to bottom. This
is how they are selected in the dialogue files. If you have trouble
keeping track of what number each face has, a good practice is to add
pure black (#000000 hex code) numbers in the corner of each slot that
state the number. Since they are black, they will not be visible against
the in-game text box. (This method does not work with custom
windowskins/text boxes, like the ones shown in mods such as \ `OMORI IS
MISSING <https://www.google.com/url?q=https://mods.one/mod/omoriismissing&sa=D&source=editors&ust=1782966892439588&usg=AOvVaw0Zpy2gnGeu2IFRnYy3xC4F>`__\  or
\ `HIKITO <https://www.google.com/url?q=https://mods.one/mod/hikito&sa=D&source=editors&ust=1782966892439673&usg=AOvVaw0_Ikoo7ttNxjF87tBgFfnA>`__\ .)

Note: Another thing to keep in mind with the basegame textbox is that
its borders will crop off 4 pixels of all dialogue portraits.



.. image:: ../images/image157.png
   :align: center



(source: TomatoRadio)

An example of numbering a faceset. The background is added for
visibility, and shouldn't be present in the actual faceset.



.. image:: ../images/image131.png
   :align: center



(source: MainCharacter_Mari.png, basegame)

A Faceset for Mari. A bunch of other sprites, used in Black Space and
memory sequences, can also be seen here. It's a good idea to condense
your facesets to include multiple characters, especially if there are no
plans to add additional faces. It will save on the amount of filenames
and overlapping indexes for you to remember and cuts down on file size.

In fact, there is virtually no limit to the size of a faceset, as an
image as large as this still works perfectly okay in game. For
reference, that’s 400 faces.



.. image:: ../images/image113.png
   :align: center



(Source: big.png, TomatoRadio’s dearly beloved creation)

.. _h.9mqtv2fx48di:

Party Battle Sprites
--------------------

Battle portraits operate very similarly to dialogue portraits and are
stored in the same folder. They’re also 106 by 106 px for each portrait;
however, the game’s UI actually covers the outer 6 pixels, leaving you
with a 100x100 area to work with.

Unlike dialogue portraits though, battle portraits are stored in rows of
three, each row being the frames of animation used for a specific
emotion. They will loop from left to right.

The rows used for each emotion are coded into the states, so if you are
making new sheets, you must follow this format.

0. Neutral
1. Happy
2. Ecstatic
3. Afraid (Also used for the "OMORI did not succumb" state)
4. Sad
5. Depressed
6. Angry
7. Enraged
8. Toast/Blacked Out
9. Hurt
10. Victory
11. Manic
12. Miserable
13. Furious
14. Stressed Out (Only used by Sunny)

If you want more emotions you must extend the sheet lower down by adding
more rows.

Here is the confetti used for DW victory faces. Feel free to download it
for yourself.



.. image:: ../images/image74.png
   :align: center



(source: \ `this google
doc <https://www.google.com/url?q=https://docs.google.com/document/d/1LyoDxBbtw4MUb7HirIZEaigpbJOcbwTelby7vttIAlg/edit%23heading%3Dh.dckld2q0kapk&sa=D&source=editors&ust=1782966892442816&usg=AOvVaw06w27_FA8vUBwjTWWkbu0H>`__\ ,
image creator unknown)



.. image:: ../images/image280.png
   :align: center



(source: 01_OMORI_BATTLE.png, basegame)

In the example above, the bottom row with each stage 3 emotion is not
used by Omori, but it is where Stressed Out sprites would be if used.



.. image:: ../images/image205.png
   :align: center



(source: 03_KEL_BATTLE.png, basegame)

Since only Omori and Dreamworld Basil (console exclusive) can reach 3rd
tier emotions, most sheets end here.

.. _h.fzvywuiuvpta:

Enemy Battle Sprites
--------------------

Enemy battle sprites are stored in two locations. A single neutral frame
of the enemy is stored in the "enemies" folder, while the full sheet is
stored in the "sv_actors" folder.

The full sheet in the sv_actors folder operates similarly to the party
battle portraits. Each row contains 4 sprites; however, frames 2 and 4
are identical to make the animation look like "1, 2, 3, 2, 1" instead of
"1, 2, 3, 1." This is otherwise known as boomeranging, rubberbanding,
and some other names.

Note: The number of frames in the animation is only convention, and you
can have many more frames for specific enemies if you want. For example,
in the final fight with Omori, he only uses 3 frames.

Unlike for party members, the sprites called for each emotion are chosen
manually by every enemy’s programming, so you can put them on the sheet
in any order you like. However, by convention, they will usually go:

0. Neutral
1. Hurt
2. Defeat
3. Sad
4. Angry
5. Happy



.. image:: ../images/image153.png
   :align: center



(source: !battle_sprout_mole.png, basegame)

Above is what the formatting of most enemy spritesheets in the sv_actors
folder will look like.



.. image:: ../images/image166.png
   :align: center



(source: !battle_humphrey_face.png, basegame)

This is what they look like in the enemies folder. It’s just one frame
of their neutral sprite.

Note that this is only used for the RPG Maker MV Database, and is not
seen in-game, so if the design of your enemy changes slightly (while
retaining the original dimensions), then you don’t need to update this.
You can actually see this with both Basil and Stranger sporting old
designs in their enemies images.

Also, yes, the third phase of Humphrey is just his face in the files.
Not that hard to guess, but still funny nonetheless.



.. image:: ../images/image192.png
   :align: center



(source: !battle_basil_something.png, basegame)

Most Something-related enemies can't feel emotion; therefore those
sprites aren't included. Here is Basil's sheet, only containing neutral
and hurt sprites, and an unused defeat sprite.



.. image:: ../images/image100.png
   :align: center



(source: !battle_biscuit_doughie.png, basegame)

Extra emotions, such as third-tier emotions, are usually shoved at the
bottom, like above.

.. _h.w178lzu1rzgf:

Battle Animations
-----------------

The majority of attacks in OMORI use the "animations" folder to hold all
their frames and are animated in the "Animations" tab of the RPG Maker
MV Database.

Animations are stored in sheets with 192x192px given to each "Pattern"
(frame of animation). These have a horizontal limit of 5 Patterns per
row, but like Portraits, have no limit on the amount of rows. In OMORI,
a frame often uses multiple patterns, and therefore must be aligned
together when animating.



.. image:: ../images/image289.png
   :align: center



(source: e_protect_the_earth.png, basegame)



.. image:: ../images/image189.png
   :align: center

(source: TomatoRadio)

Here is an example of the above image in the actual Animations tab. As
you can see by the gray squares, the images are being broken up into
multiple parts.

.. _h.erkrcheu7d10:

Battle Backgrounds
------------------

Battle Backgrounds, or Battlebacks as they are often called, are really
easy and fun to make. They are stored in the "battlebacks1" folder.

Technically speaking, you may place any 640x480 image in the folder and
it will be usable as a battleback; however, OMORI uses a very specific
style for its battlebacks. Specifically, OMORI uses dithered stock
photos for its battlebacks.

OMORI sources its photos
from\ `  <https://www.google.com/url?q=https://www.pexels.com&sa=D&source=editors&ust=1782966892448224&usg=AOvVaw1KpmGz5j1W3B5t-i61PbSj>`__\ `Pexels <https://www.google.com/url?q=https://www.pexels.com&sa=D&source=editors&ust=1782966892448307&usg=AOvVaw2mjIMYH_7qS6NigJjObPJd>`__\  and\ `  <https://www.google.com/url?q=https://pixabay.com&sa=D&source=editors&ust=1782966892448349&usg=AOvVaw0AhFYg8fcdl6N_8K41qy9m>`__\ `Pixabay <https://www.google.com/url?q=https://pixabay.com&sa=D&source=editors&ust=1782966892448385&usg=AOvVaw3bSeMzqY3DlCydH4h3G6Xw>`__\ ,
which I would also recommend, as the photos are all free and
watermarkless. Once you have your photo, you must crop and/or scale it
down to 640x480, and then place it through a dithering tool. Photoshop
gives the most accurate results,
but\ `  <https://www.google.com/url?q=http://ditherit.com&sa=D&source=editors&ust=1782966892448646&usg=AOvVaw3WjdYfOb3ZGVCL6m5F1yan>`__\ `Ditherit <https://www.google.com/url?q=http://ditherit.com&sa=D&source=editors&ust=1782966892448684&usg=AOvVaw3gROQ9vaDtBa62aLIxnBOo>`__\  gives
good results too.

What is dithering, though? It’s basically just reducing the color
palette of the given image by using alternating pixels to mimic more
shades. That makes the image retain its depth, but become small in file
size. It also has a very specific, unique effect on images that frankly
just sorta looks cool.

Example:



.. image:: ../images/image203.jpg
   :align: center



Original Image
(\ `Photograph <https://www.google.com/url?q=https://www.pexels.com/photo/water-fountain-beside-green-leaf-trees-242258/&sa=D&source=editors&ust=1782966892449266&usg=AOvVaw3liujNduVxHdDoPVoakjLf>`__\  by:
Mike Bird)



.. image:: ../images/image65.png
   :align: center



Cropped to 640x480



.. image:: ../images/image236.png
   :align: center



Dithered using
\ `Ditherit <https://www.google.com/url?q=https://ditherit.com/&sa=D&source=editors&ust=1782966892449575&usg=AOvVaw0MnEsgS93851O4Ha9uSIP8>`__

Pay special attention to the texture of the bushes on either side of the
image. The colors are reduced from hundreds of different shades of green
to just five or six, as you can see, but the bush still retains its
texture. Fascinating, right?

Also a rarely mentioned feature is that you can have multiple battleback
images at once in battle with the use of Plugin Commands, including
scrolling battlebacks. This is how the Omori fight works in addition to
the final fight in \ `Autumn
Break <https://www.google.com/url?q=https://mods.one/mod/autumnbreak&sa=D&source=editors&ust=1782966892450174&usg=AOvVaw1WK3H4rsqrXVJ0bkADlNcA>`__\ .
So don’t be afraid to make some cool looking scenery!

.. _h.1zgigevc1sol:

Tilesets
--------

Tilesets feature all the tiles and props used in OMORI's maps. They are
sheets stored in the "tilesets" folder.

Most of OMORI's tilesets are 1024x1024, which is the maximum size
available. Each individual tile is 32x32, with some larger props using
multiple tiles, like trees and buildings. Tiles can be animated with a
looping animation of other tiles on the sheet, which is explained in
detail in the \ `Mapping Section <#h.uhf8h4xswr8>`__\ .



.. image:: ../images/image46.png
   :align: center



(source: DW_SnowForest.png, basegame)

Snowglobe Mountain's Tileset. Notice how all three frames of the water
are present. These are used for animated tiles.

Also notice how the Church of Something’s mountain is here, too. You
don’t have to stick to just one region for your tileset, and it’s
usually better to merge smaller tilesets to save on file space,
especially if they have similar types of assets. It’s less clutter for
you and less storage/processing for your and the players’ computers.

.

.

.

.

.

.

TILESETS, i know you just read about how to make em, BUT, here i've
taken some time to gather up and make a base for ya. i know,
how handy!!! Of course, you can just edit basegame stuff, but their
layouts are BAD! really bad oh god. so bad.



.. image:: ../images/image197.png
   :align: center



(Source: DW_SlimegirlLairTiles.png, basegame)

LOOK AT HOW BAD THIS IS!!! IT’S ALL OVER THE PLACE IT SUCKS!!! No no no,
let me explain why this sucks so much. The bridges are a mess, seemingly
added wherever they fit. The waterfalls are a whole school district away
from the actual water. Meanwhile the blue water cliffs are hanging in
Maine whilst their siblings are wondering how they got there when they
live in Arizona.

Now let me show you something far better!



.. image:: ../images/image92.png
   :align: center

 

.. image:: ../images/image231.png
   :align: center

 

.. image:: ../images/image38.png
   :align: center



(Source: ME!!! and basegame stuff too… oh and my sis…)

THIS!!! IS A TILE BASE!!!

“BUT WAIT, I HEAR YOU CRY!!! WHAT IS THIS???? WHY IS EVERYTHING SO
BRIGHT??” Let me explain.

Let's start with the standard base.



.. image:: ../images/image92.png
   :align: center



If you don't need any pre-existing objects, use this as a standard!
Anything on here you're gonna need for later. Firstly, the colors.



.. image:: ../images/image219.png
   :align: center



(Source: ME AGAIN!!!!, but TOMATO “fixed” it by changing it to say
cliff…)

Red is where your grass is going to go. In these, i've chopped off the
extra grass, so make sure to extend your edge grass OVER the red parts
and onto the blue, like this;



.. image:: ../images/image233.png
   :align: center



(Source: Aseprite)

OMORI tends to use the same grass for most things, but you may not want
to do that, of course. the dark blue is your CLIFFS. These tend to have
some slight shading and cracking at the bottom, but it depends on the
area.



.. image:: ../images/image155.png
   :align: center



(Source: edit of HS_PIREFLAIFORIST.png, basegame?)

Green is your water. For animated water, you have to manually add the
frames through tiled. I'm about 90% sure someone explained this in the
tiled part, but the frames go in this order && have a frame delay of
approx. 200 ms of delay. I don’t know man, you know it when you see it.



.. image:: ../images/image107.png
   :align: center



(Source: The green gunk from my gunk palace)

Yellow is your stairs! i kept this simple (not the trees i'll get there
wait). The one over on the left side IS different from the one more in
the middle. That bottom right one has straight edges, better for more
man-made (or whatever freaky creatures are the intelligent species of
the world you are creating), while the top-right has rougher edges for
us doofuses and unintelligent life. Meanwhile the rest are for larger
stairs, like the big boy stuff!

Cyan are your paths and the random debris that are around. Sprinkling
them around helps a lot. And as I said with the red, the grass can and
will go over the cyan. This is the farthest inward basegame does.



.. image:: ../images/image15.png
   :align: center



Now almost everything else is self explanatory. Grass, trees, rocks, you
know the deal. Just be aware that you may not need trees that are a
different color, but i'd seriously recommend it. Even if it's only a
minor change, it can add a lot to a map.



.. image:: ../images/image51.png
   :align: center



(Source: map159.png, basegame, compiled by an rph tool
\ `idr <https://www.google.com/url?q=https://github.com/rphsoftware/omori-map-preview-renderer/actions/runs/20416117980&sa=D&source=editors&ust=1782966892456077&usg=AOvVaw2mM48N5aA-qLt_z_Tb6-HF>`__\ ` the
name of
lmao <https://www.google.com/url?q=https://github.com/rphsoftware/omori-map-preview-renderer/actions/runs/20416117980&sa=D&source=editors&ust=1782966892456203&usg=AOvVaw16K930FInRGZEfTx6NKa09>`__\ )

“Now, what's with all the black stuff scattered around?”

Those are your connectors. think of them like parts in a puzzle piece.
make sure these line up at all times. you can just select them using any
kind of color picker (or The Eyedropper Tool ) to check. i’d personally
cut them and put them on another layer to be able to check them at any
time



.. image:: ../images/image33.png
   :align: center



(Source: I think they were like those little plastic connectors that
autistic kids really like K’NEK THEY CALLED K’NEK!!!)

here's a lovely test map TOMATO did to show how all this works



.. image:: ../images/image101.png
   :align: center



(Source: AGHHHITBURNSITBURNSAGHHHHHHHHHHHH.png)

now the outside and inside bases.

same stuff, but now with stolen goods! There are a lot of
basegame assets here to edit, all laid out by type.



.. image:: ../images/image174.png
   :align: center



(Source: I made it the \*@(# up)



.. image:: ../images/image172.png
   :align: center



(Source: I made it the @#@% up again)

Some basegame tiles are aligned weird, but they do serve a purpose. a
lot of the time they will be there to go on counters or line up to
another object. if something isn't looking right, try moving it around
by a few pixels.

Now, i’m sure you've noticed me and PINKER by now. I'm simply here to
fill up space! id kindly ask you not to remove me if you plan to use
these bases by the way! i \\sinv[1]looovee\\sinv[0] credit for my
work!!! anyway PINKER does serve a use. She's offset by six pixels
upwards. In RPG Maker MV, all events (with the exception of ones with a
‘!’ in their name) are shifted up Six (6) pixels compared to the
tilemap. This is for depth reasons, but means that you may need to make
some guesses for what the player would look like when mapping, but you
do know what PINKER would look like!!! She’s the one with cooties, so i
had to put her in the biohazard box, but i think you’re safe from those…



.. image:: ../images/image208.png
   :align: center



ok have fun \\{\\{\\sinv[1]byyeeee\\sinv[0]

if you want to grab my SLOP for your own use, then you can find them in
\ `this
pack <https://www.google.com/url?q=https://mods.one/mod/fdtromoutils/&sa=D&source=editors&ust=1782966892458986&usg=AOvVaw0dznYeXsSRsxLktX_uloD2>`__\  that
these other two NERDS made. They are really nice for letting me in…

- `Tester <https://www.google.com/url?q=https://mods.one/author/Patch357&sa=D&source=editors&ust=1782966892459203&usg=AOvVaw0oDtYLWtByh6aKbaZ91bRA>`__

.

.

.

.

.. _h.5tjo6sderudd:

Parallaxes
----------

Parallaxes are looping images used as map backgrounds. They’re stored in
the "parallaxes" folder. They are primarily used for the sky in
Headspace and Faraway, and also as backgrounds for Black Space maps.



.. image:: ../images/image214.png
   :align: center



(source: Space_parallax.png, basegame)

Headspace's starry sky.



.. image:: ../images/image256.png
   :align: center



(source: sunset_sky.png, basegame)

Faraway's sunset sky.



.. image:: ../images/image19.png
   :align: center



(source: !parallax_glitch.png, basegame)

The static used in Black Space’s Subconscious Spill. The pictures of
Mari in the Room of Stumps and the clocks in the Time Area are also
parallaxes, as are a bunch more that it would probably take a while to
name.

There’s only one specification for parallax images. Images with a
! placed at their front will stay aligned with the map, whilst images
without a ! will move with the player. In addition any scrolling
parallax should ideally have seamless edges, but you should’ve been able
to figure that out yourself…

Parallaxes can also be used for loading a map into the editor to make it
easier to place events in the right places, but that’s discussed in more
detail in the \ `mapping section <#h.26aes05t898p>`__\ .

.. _h.t18x2wwdh8k:

Pictures
--------

Pictures are images that will appear on top of the screen and can be
controlled in a few different ways. Pictures get used for various
purposes, but generally can be boiled down to images that appear above
the world for one reason or another.

This includes but is not limited to:

- Cutscenes
- Art popups
- Lighting



.. image:: ../images/image124.png
   :align: center



(source: release_stress[5x5].png, basegame)

Release Stress Cutscene.



.. image:: ../images/image223.png
   :align: center



(source: pictures_fa_extra.png, basegame)

A sheet of some of Faraway Town’s art popups. Yes, there are some
Dreamworld pictures mixed in, too. :D



.. image:: ../images/image235.png
   :align: center



(source: lighting_overlay.png, basegame)

Lighting Overlays.

The dimensions of each frame of a picture that you want to display on
the top of the screen have to fit within 640 by 480 pixels, but they’re
a lot more versatile than most of the other asset forms.

They can also be given the Multiply, Screen, and Add blend modes
in-game, which can be really helpful. For example the blackout in the
Spaceship of
\ `parallels <https://www.google.com/url?q=https://mods.one/mod/parallels&sa=D&source=editors&ust=1782966892462622&usg=AOvVaw3L9TK5o6wHxardQX_8DHA0>`__\  uses
a multiply layer.

In addition these can also be animated using scripts, which is how
cutscenes work usually. We list these scripts in the \ `Event
section <#h.9j8d825dwjpk>`__\ .

Lastly! (I know it's a lot but pictures are just really good) Pictures
can be ‘pinned’ to the center of the current map. And because pictures
with an ID of 1 display below the player and events, this means that you
can make a map be a picture, and display it that way. This can also be
used for more complex map specific overlays.

.. _h.vsfi51blno5f:

Item Icons
----------

Next up is Item Icons. These icons in base game are found in the
img/system folder, in a set of sheets called itemCharms.png,
itemConsumables.png, itemImportant.png, and itemWeapons.png. While
itemWeapon.png and itemWeapons.png are identical, itemWeapons is the
used version.

As the names suggest, each sheet is used for a specific type of item.
Depending on what the item is marked as in game, it calls the image from
that specific sheet.



.. image:: ../images/image85.png
   :align: center



(source: itemWeapons.png, basegame)

Item icons are 108x108px, and can be organized in any way as long as the
sheet is a fixed width and fits a whole number of icons in a single row.
This is especially clear when looking at base game's sheets, which are a
mix of 7, 8, or 9 icons across. The height of the sheet can be extended
indefinitely, allowing you to add as many rows as you want.

Stylistically, they are always white pencil on black background in base
game, but realistically they can be anything that you want them to look
like.

Accessing the icons using basegame's method can be difficult and
unrealistic, however. Using Stahl_AltItemIcon, you can just specify the
name of the sheet and then the index, enabling you to get any icon
regardless of what type of item it is. This plugin can be found in the
\ `OMORI Modding Resources
Repository <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources&sa=D&source=editors&ust=1782966892464995&usg=AOvVaw1h_m5OZOhZofCnH2sK1DxR>`__\ ,
and if it's not there, it can be found by asking in the \ `Omori Modding
Hub <https://www.google.com/url?q=https://discord.gg/exu5KTxDvC&sa=D&source=editors&ust=1782966892465157&usg=AOvVaw2IlydHlybDT6gNs4rguU7t>`__\ .
This method also allows you to define new item sheets.

Something to keep in mind, though, is that icons are compressed and
rescaled in order to fit where the game wants them to fit. Therefore,
using a pixel sprite as an icon won't work without it being blurred. If
using a pixel sprite is something that you want to do, you can use
\ `FD_ItemIconRescale <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/Battle%2520System%2520Plugins/Menu%2520and%2520UI/FD_ItemIconRescale.js&sa=D&source=editors&ust=1782966892465602&usg=AOvVaw0rga07v6ZrVSmYu0-h_s-->`__\  to
create an icon sheet that will not be resized. (Please note, it has not
been tested with shop icons and may not work if the item is put in an
in-game shop. Contact FruitDragon, the author of the plugin and owner of
this document, for assistance.)

.. _h.1403ms5rn6k4:

Windowskins
-----------

After that are Windowskins! If you’ve ever played \ `Broken
Dreams <https://www.google.com/url?q=https://mods.one/mod/brokendreams&sa=D&source=editors&ust=1782966892466009&usg=AOvVaw1IN6x3NI5S5SAeb18BBJFo>`__\ ,
\ `HIKITO <https://www.google.com/url?q=https://mods.one/mod/hikito&sa=D&source=editors&ust=1782966892466067&usg=AOvVaw2WhLxlJ3eLOB4IzoIP19sF>`__\ ,
\ `OMORI.exe <https://www.google.com/url?q=https://mods.one/mod/omoriexe&sa=D&source=editors&ust=1782966892466188&usg=AOvVaw2bGMzu7sTT3b83UCGo5lsL>`__\ ,
or many other mods, then you’ve seen Windowskins in use. These are
images in img/system that determine the appearance of the various
windows in the game, such as text boxes and menus.



.. image:: ../images/image260.png
   :align: center

 

.. image:: ../images/image204.png
   :align: center

 

.. image:: ../images/image20.png
   :align: center



(sources (left to right): Window.png, basegame \| REDACTED.png,
Unreleased Project by TomatoRadio \| Window_Guide.png, TomatoRadio)

Here we can see the anatomy of the windowskins. We’ll start at the top
left. This 96x96 square is the back of the windowskin, and is stretched
to fit the size of whatever window there is. Due to the stretching,
detailed images will get distorted and blurred, so instead, colors and
gradients are the best fit for the background of a windowskin.

To the right of the background is the frame and arrows. The frame
consists of 4 sides and 4 corners, which it tiles to create the border.
These do not get distorted. While most windowskins are 5 pixels thick,
it can go up to 24 pixels. Designs can also be added to the corners, but
may get messy on smaller windows, like the name box.

The arrows are used for menus to indicate that scrolling is possible.
They fit within the gray rectangles seen in the guide image. They do not
stretch.

In the bottom left of the image is a tiling pattern. This a 96x96 sprite
that will be overlaid on top of the background and tiled across the
window. This is how stuff like the stars on
\ `Lucille <https://www.google.com/url?q=https://mods.one/mod/roseglass&sa=D&source=editors&ust=1782966892467786&usg=AOvVaw0Bry9ZUsuyxxkXYrqrhOrc>`__\ ’s
windowskin work. In the green windowskin depicted, vines will be shown
across the window. It’s recommended for these to be partially
transparent.

The cursor and pause sign, which can be seen in the top half of the
bottom right quadrant, will very rarely if ever be seen in OMORI, but
for completion I will explain the both.

For menus that do not use the Red Hands cursor icon to select an option,
the game may default back to the normal RPG Maker MV method of showing
the cursor, which is with this section of the windowskin. It will be
stretched akin to the background across the option, and fade in and out
over about a second.

Meanwhile, the pause symbol is a 24x24 animated icon that would appear
in place of the Red Hands when waiting for the player’s input in a
message window. This goes completely unused, and therefore so does this
section of the windowskin.

Lastly, the colors! A grid of 32 12x12 squares make up the list of
colors that can be used for text via that windowskin. To be more
precise, the game uses the (7,7, starting at 1 from the top left)th
pixel, outlined in the guide image, to determine the color, allowing the
other pixels to be used for whatever, such as marking the index number.
It’s worth noting that changing windowskins can cause issues with these
colors, so caution is advised.

And on that topic, how do we actually change the windowskin?

Well normally, you can’t (easily) change the windowskin. So instead,
mods use the
\ `HIME_WindowskinChange <https://www.google.com/url?q=https://himeworks.com/2016/04/windowskin-change/&sa=D&source=editors&ust=1782966892469784&usg=AOvVaw3p3eZY6MilKs9-Puvo64Np>`__\  plugin.
From here, the script:

$gameSystem.setWindowskin(“NAME”);

Can be used to change the windowskin. Now, there are many caveats to
this that I’m going to rattle off with regards to errors that
windowskins can have. If applicable, a solution will be provided.

- Changing the windowskin every time a character talks is a hassle.

- Using
  \ `WN_ExtendedYAML <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/Data%2520Organization%2520Plugins/WN_ExtendedYAML.js&sa=D&source=editors&ust=1782966892470436&usg=AOvVaw31vGFIbuSiXnCRaoc32cmM>`__\  or
  preferably
  \ `DoubleExtendedYAML <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/Data%2520Organization%2520Plugins/DoubleExtendedYAML.js&sa=D&source=editors&ust=1782966892470562&usg=AOvVaw2TmWgYq0-W8AlN4ZIR1IQ->`__\  will
  allow setting windowskins in the YAML directly, bypassing this.

- Changing the windowskin for a message will apply it to the main menu
  and other places I don’t want.

- Using
  \ `TR_RestrictiveWindowskins <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/UI%2520plugins/Window%2520Skins%2520or%2520Layout/TR_RestrictiveWindowskins.js&sa=D&source=editors&ust=1782966892470911&usg=AOvVaw3F4cMYfKP_DL2lXXAlDk7g>`__\  enables
  you to control which windows are modified by the windowskin change.

- The text color isn’t updating.

- Using
  \ `BABY_ExternalColorImage <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/UI%2520plugins/Window%2520Skins%2520or%2520Layout/BABY_ExternalColorImage.js&sa=D&source=editors&ust=1782966892471194&usg=AOvVaw2YdqIcPCqTKegru09-b91t>`__\  should
  fix it, but might not always.

- I need more than 32 colors.

- Use
  \ `BABY_ExternalColorImage <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/UI%2520plugins/Window%2520Skins%2520or%2520Layout/BABY_ExternalColorImage.js&sa=D&source=editors&ust=1782966892471442&usg=AOvVaw3JF-dzoebla4gXSHKyZviT>`__\  and
  get 288 colors. Should be enough for you.

- My windowskin isn’t working in retail/I have text that’s black in
  retail.

- Make sure your
  \ `OneLoader <https://www.google.com/url?q=https://mods.one/mod/oneloader&sa=D&source=editors&ust=1782966892471723&usg=AOvVaw2DwMt8iwn7vRw2wYD1XMKk>`__\  and
  \ `BundleTool <https://www.google.com/url?q=https://mods.one/mod/bt&sa=D&source=editors&ust=1782966892471784&usg=AOvVaw25lE1qX5KS7bHjK6yx3y9q>`__\  are
  updated. Older versions had issues patching the base Window.png.

.. _h.faldvhvy9afa:

Movies
------

Movies are pre-rendered videos played in-game. These are exclusively
used for various in-game cutscenes. They are all 640x480 .webm files.

These are mainly used for when there are too many moving layers for
pictures to be usable or effective. Some examples are as follows:

- All three credits cutscenes
- Red Space cutscenes
- The Bookcase cutscene
- The Creation Of OMORI cutscene

We can’t embed these examples in this tutorial unfortunately :), but
definitely check them out in the “movies” folder found in the playtest
folder! (NOT the img folder!)

.. _h.k1o98u5ou6yk:

Atlases
-------

Lastly, we have Atlases. These guys are pretty weird but they are also
extremely useful, and I’d be remiss to exclude them, especially due to
being the most complex image type in OMORI.

Atlases are, in basic terms, spritesheets. They are larger images that
are composed of multiple smaller images, usually laid out in a grid or
other format. These sheets are then broken up by the engine into
individual images that can be called separately.

Let’s take a look at one from the basegame to better explain:



.. image:: ../images/image3.png
   :align: center



(Source: battleATLAS.png, basegame)

This is the atlas that stores the sprites for the Title Screen! Looking
through here, you can see both Omoris, Sunny, and whichever title color
is opposite of your theme right now.

Now let’s see what actually breaks down this image.

Heading over to your playtest’s data, you’ll find a file called
Atlas.yaml. Open it up in your editor of choice and you’ll be greeted
with this sight:



.. image:: ../images/image98.png
   :align: center



(Source: atlas.yaml, basegame) (I feel like this one should be obvious…)

Firstly, all of these are indented inside of the source: line. To avoid
getting especially technical, if a line is indented inside another, the
indented line can be called from the higher one in code. Therefore, the
game needs all of these to be indented inside of source:.

Now for the actual images.

Conveniently, the title screen is the first image in the list, so we
won’t have to scroll to analyze it.

The first line is the file path of the image you’re creating, including
all folders and the file extension, which is .png.

This will also therefore be the filename used when actually playing the
game, so remember it.

The following lines are then indented inside of the filename.

atlasName: This is the name of the full atlas image in img/atlases.

rect: The x and y are the coordinates of where what was the top left of
the original image will go in the new image. The width and height are
the size of the new image. If this sounds confusing, just set x and y to
0 and the width and height to the size of the image.

sourceRect: The x and y are the coordinates of the top left of the image
in the full atlas. Width and Height are self-explanatory.

If you did it all correctly, then you can now use these images whenever
you like in game, as they behave just like any other.

However, there are of course some notes.

These images will not appear in the editor, so if you’re using the
editor to select your image, it will not appear. This means that these
are best used for images that are called by notetags or scripts, such as
facesets or badges.

Here’s an example of them being used for the State Icons of
\ `parallels <https://www.google.com/url?q=https://mods.one/mod/parallels&sa=D&source=editors&ust=1782966892476621&usg=AOvVaw2ma29n5cXJDlB198HLTGul>`__\ .



.. image:: ../images/image119.png
   :align: center



(Source: parallels, sprites created by TomatoRadio)

When adding a new atlas, it's a good idea to get the
\ `Stahl_AtlasExtended <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources/blob/main/Data%2520Organization%2520Plugins/Stahl_AtlasExtended.js&sa=D&source=editors&ust=1782966892476999&usg=AOvVaw0Qo-xBz5jZwx61hLoKbhRU>`__\  plugin
from the \ `OMORI Modding Resources
GitHub <https://www.google.com/url?q=https://github.com/modsone/omori-modding-resources&sa=D&source=editors&ust=1782966892477114&usg=AOvVaw0rfHUhbndybluqKg1pN1e7>`__\  and
create a new atlas instead of editing the base game's Atlas.yaml. This
is because the base game atlas is very useful as reference, and due to
its syntax being extremely easy to mess up, it's easier to simply leave
it as reference and not modify it if it can be avoided. That way, you'll
have a file to reference in case things go wrong with your atlas.

Other images that are atlased in base game include almost all of the
assets of the various photo albums, a variety of UI assets for battles
and such, tag photos, and Omori's sketchbooks. They can all be found in
the img/atlases folder.

.. _h.g7yzgvnqi3cb:
