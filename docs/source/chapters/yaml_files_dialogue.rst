YAML Files & Dialogue
=====================



.. image:: ../images/image5.png
   :align: center



A good way to start is by looking at the existing .yaml files in the
vanilla game. Those can be located in the Playtest Folder provided
by OneLoader, with the following filepath:

.. _h.on4cnbrrktnj:

Location
--------

playtest_folder/languages/en



.. image:: ../images/image125.png
   :align: center



(Source, FruitDragon)

In this folder is most of the written text in the game. Basically unless
it’s battle text (barring dialogue), it’s likely stored in one of these
yamls. This folder is also where you will have to put any new .yaml
files that you create.

.. _h.2oe8c7v0nxky:

Syntax
------

When we open the 00_template.yaml, we’re shown the following code:



.. image:: ../images/image111.png
   :align: center



(Source, 00_template.yaml, basegame)

The meaning of this is pretty basic. Each message without a face
attached (so all dialogues not involving Omori/Sunny, Aubrey, Kel, Hero,
Mari, or Basil/Stranger) is defined as a single line of text following
“message\_XX” (where XX is some number) and messages with a face get two
additional values that must be defined— the faceset, aka the file in
which the face you want belongs, and the faceindex, aka which of the
faces on the file. More on that later.

Note: message\_XX is convention, not requirement. Any string of text
could work in this place. And in many cases, it could make it easier to
remember certain dialogue choices if you give it a name other than
convention. An example of a mod that uses this feature is
\ `Reverie <https://www.google.com/url?q=https://mods.one/mod/reverie&sa=D&source=editors&ust=1782966892287534&usg=AOvVaw3zUUz8zUFX2W2LRkSPi6GD>`__\ .

.. _h.jkwhfutwca8h:

Examples
~~~~~~~~



.. image:: ../images/image159.png
   :align: center



(source: 01_cutscenes_neighbors.yaml, basegame)



.. image:: ../images/image212.png
   :align: center



(source: fa_map_flavor.yaml, basegame)

As you can see here, flavor text (text that pops up when you interact
with objects) is defined in much the same way as cutscene dialogue,
shown in the first example.

.. _h.xdrvpi4i3661:

Comments
--------

Also, comments! The green lines of text, denoted with a # symbol at the
beginning of the line are ignored by the file and are a great way of
making your .yaml file easier to read, usually to show information that
you can’t glean with just the messages such as character movement or
dialogue options.

Without these comments, you will end up with something like this:



.. image:: ../images/image286.png
   :align: center



(source: curated example, courtesy of TomatoRadio)

It’s a lot more difficult to tell what anything is for if you’re looking
at the files and are trying to figure out what each line is for. What
does Kel do? What happens if you say no? Can you say no? You can’t tell.

Now look at the same .yaml file with comments added in:



.. image:: ../images/image16.png
   :align: center



(source: curated example, courtesy of TomatoRadio)

Now we learned a bunch of helpful info. We know how to animate Kel and
Aubrey fighting, what the dialogue options are, and we know what Kel
does in the Yes branch.

Going over your yamls again to comment may also let you catch an error
or two, which you can even see here. Can you spot what changed?

.. _h.k8tk6b6mr2yc:

In-Game Formatting
------------------

“But, FruitDragon,” you may be saying, “what are all of these random
backslashes and dots and lines in between the text for? And how does
formatting like the really wavy text from Sweetheart’s iconic laugh
happen?”

“Well, dear aspiring mod maker,” I say in return, “those random
backslashes and dots and lines in between the text are exactly what
causes that formatting to happen.”

Almost. Technically, the wavy text is caused by the \\sinv[] function.
But I digress.

Here’s a quick guide to super basic formatting. For a more comprehensive
guide, I highly recommend visiting
\ `this <https://www.google.com/url?q=https://github.com/Gilbert142/gomori/wiki/Text-Formatting&sa=D&source=editors&ust=1782966892290756&usg=AOvVaw3WPOoSFNECyXi-GYyFq-w1>`__\  link.

All formatting commands start with a backslash (\\) except for one—
that's <br> which, much like the HTML version, causes a line break.

- <br> = line break
- \\. = Pause 15 frames, approx. 1/4 of a second\*
- \\\| = Pause 60 frames, approx. 1 second\*
- \\! = Wait for user input before progressing, basically meaning you
  have to press z to continue
- \\^ = Automatically closes a text window once it's done writing
  itself, like if you want someone to be interrupted
- \\sinv[2] = Wavy text (For less intense waving use \\sinv[1])
- \\quake[2] = Shakes text (For less intense quaking use \\quake[1])
- \\v[#] = Passes in the value of the variable number given (eg:
  \\v[143] passes in the save’s WTF value)
- \\c[#] = Changes text color! These colors are based off of the
  checkerboard in img/system/Window.png. 0 is the white square in the
  top left and it keeps going from there, left to right. You can add
  your own colors by changing this image. This table shows OMORI’s color
  conventions:

======= == ===============
#FFFFFF 0  Default
#6095ff 1  Skills
#5bd863 3  Snacks
#fed966 4  Important Items
#ff9233 5  Toys
#64f7ed 11 Locations
#c263e1 13 Equipment
======= == ===============

RPG Maker audio is ran independently of the game’s framerate, which can
cause desyncs if you are assuming a consistent 60fps.

Again, it’s a good idea to look at already existing .yaml files for
certain types of formatting, like if you want to mimic Sweetheart’s
iconic laugh. No better way than to learn by example!

…

Okay, now I’ve made myself curious.



.. image:: ../images/image263.png
   :align: center



(source: 15_cutscenes_herothebachelor.yaml, basegame)

We have here Sweetheart’s iconic entrance with Sweetheart’s iconic
laugh. Repeated a grand total of three times, each time with different
formatting.

What exactly is going on with this dialogue?

Here’s what I see in terms of formatting:

- \\Com[2]
- \\sinv[1]
- \\sinv[2]
- \\{
- \\!
- \\\|
- <br>
- \\smm
- \\swh

We already know most of these. As I mentioned, \\sinv[1] and
\\sinv[2] are the thing that caused Sweetheart’s dialogue to get all
wavy. \\\| is pause 60 frames, and \\! is wait for user input before
progressing. And <br>, of course, is line break. So what are \\{,
\\Com[2], \\smm, and \\swh?

\\{ is what increases the text size. Similarly, \\} is what decreases
the text size.

\\Com[x] runs the Common Event from the game that has the same number as
the number passed in to the command in place of x. In this case, Common
Event #2 is Shake Screen, which means that every time \\Com[2] is run,
it’ll shake the screen. (Wow, that’s a lot of screen shaking in that
last Sweetheart laugh.)

Now what are \\smm and \\swh?

It’s simple, really. But it involves getting into a topic that we
haven’t really gotten into yet.

It’s time to talk about:

.. _h.m0lmbk2z27gs:

Names
-----

That’s right, names. That little box that pops up on top of dialogue
boxes to tell you who’s speaking.

Now that I think about it… we haven’t really seen how names are defined,
yet. Only the dialogue itself. How does the game know who’s talking?



.. image:: ../images/image229.png
   :align: center



(source: farawaytown_extras_dailydialogue.yaml, basegame)

Well it’s just the following line tacked on to the beginning or end of
the text:

\\n<NAME OF PERSON HERE>

But where is that for the other dialogues we’ve encountered so far?

Here’s the thing. Writing \\n<NAME> over and over and over again can get
tiring, especially when the name is super long. So OMORI has a set of
Macro Plugins. What these are are shorthands for strings of text, which
can include text codes. You can put anything into these Macros, and you
can add your own by changing the parameters in the Plugin Manager, but
in OMORI, they are mostly for names. 

Here’s a short guide of common names:

- \\aub = Aubrey
- \\her = Hero
- \\bas = Basil
- \\kel = Kel
- \\mar = Mari
- \\omo = Omori
- \\who = ???
- \\swh = Sweetheart
- \\smm = Sprout Mole Mike
- \\sbf = Space Boyfriend
- \\cap = Capt. Spaceboy
- \\spxh = Space Ex-Husband

Recognize any?

That’s right. \\smm and \\swh were used to denote that Sprout Mole Mike
and Sweetheart were talking! That makes a lot of sense.

Of course, there’s definitely more. For a full list of macros, visit
\ `this <https://www.google.com/url?q=https://github.com/Gilbert142/gomori/wiki/Text-Macros&sa=D&source=editors&ust=1782966892300169&usg=AOvVaw00ETgemo02FsoVLTufk544>`__\  link.

Note: For a renameable character like Sunny (barring the examples
earlier;
\ `parallels <https://www.google.com/url?q=https://mods.one/mod/parallels&sa=D&source=editors&ust=1782966892300405&usg=AOvVaw0_32_SGR5paQneQ-TQc0PQ>`__\  doesn’t
have a renameable Sunny) you’ll have to use \\n[8] for the character’s
name. 8 is the actor ID for Sunny. If there’s a different character that
you want to get the name for like that, just use \\n[ACTOR ID]. So the
final product would be \\n<\\n[ACTOR ID]>

Now, it’s time to go over the things I said I would go over earlier.
Faceset and faceindex.

.. _h.5i94vch76e39:

Faceset
-------



.. image:: ../images/image141.png
   :align: center



(source: 01_cutscenes_neighbors.yaml, basegame)

What is faceset? What are these random strings in the faceset?

They’re filenames. More specifically, for files in the img/faces folder,
shown here:



.. image:: ../images/image48.png
   :align: center

  

(source: FruitDragon)

The files in specific that we’ll be referring to for yaml files are the
ones at the bottom of the image, denoted with the MainCharacter\_ or
MainCharacters\_ prefix.

Here are options provided with the basegame:

- MainCharacter_Basil_dark — For all your nighttime Faraway Town
  character needs!
- MainCharacter_Basil — All of the daytime faces for Faraway Basil and
  Dreamworld Basil! With Stranger, nighttime Aubrey, and a little
  nighttime Hero thrown in for good measure!
- MainCharacter_Mari — Dreamworld Mari and the unused Spirit Mari! Plus
  a few faces belonging to our faceless mannequins in Black Space and
  our Faraway Town twelve year olds.
- MainCharacters_Dreamworld — Dreamworld Hero, Aubrey, and Kel. Plus
  Hector.
- MainCharacters_Faraway — Faraway Town Hero, Aubrey, and Kel.

The file formatting for one of these facesets is pretty specific. 106
pixels by 106 pixels per face, 4 faces per row. You can have as many
rows as you need.



.. image:: ../images/image209.png
   :align: center



(source: FruitDragon)

How does the game know which face in each faceset to use, though?

Well, that’s where the next topic comes in.

.. _h.w39or5al8zx:

Faceindex
---------

This number tells the game which file to fetch from the given faceset.

Here’s an example using a darkened monochrome version of
MainCharacters_Faraway:



.. image:: ../images/image32.png
   :align: center



(source: FruitDragon (edit of MainCharacters_Faraway, face 15 is
custom))

As you can see, the count starts from 0 (because computers) and goes up
by one, wrapping around to the next row each time. So calling
MainCharacters_Faraway and assigning the faceindex value to 2 would show
the face with the value 2, or Aubrey with her eyes closed, when that
dialogue is printed.

.. _h.jz74153ns5i1:

Dialogue Examples:
------------------



.. image:: ../images/image35.png
   :align: center



Let’s see what each of these turn out to look like!



.. image:: ../images/image73.png
   :align: center





.. image:: ../images/image29.png
   :align: center





.. image:: ../images/image175.png
   :align: center



(source: Biggie Cheese)

I used pretty basic formatting, since a lot of the text moving ones like
\\sinv can’t translate well to screenshots. \\!, \\., \\\|, and any
other wait/player input commands also don’t translate to screenshots.

There is a new one: \\fr, which resets all font changes. This is used
because at the beginning of Kel’s dialogue, the font size is increased,
but we don’t want the font size to stay large for the entirety of the
line.

Now, you may be wondering, how do you add these dialogues to the game?

Well, I’ll go over that in the next section:

.. _h.3ek5unxwrmmt:
