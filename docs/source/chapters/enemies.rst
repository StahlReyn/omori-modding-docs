Enemies
=======



.. image:: ../images/image201.png
   :align: center



So. You know how to make dialogue, events, maps, art(or at least how to
format it), states, equipment, skills, even party members(technically).
You’re building quite the repertoire. But now I’m going to introduce
something even worse than that.

Making enemies.



.. image:: ../images/image87.png
   :align: center

  

(source: image by u/Whisp_Is_My_Waifu, same as last time)

This is mostly just because they take a lot of work to explain and to
make. So let’s see how well I can do!

.. _h.3g51mlq6u5uy:

Images
------

This will be brief since I already explained this in the section in
\ `Sprites and Art <#h.gsbdya7y8lgi>`__\ , but you’ll want two images
for your enemies. You’ll need an image of all frames for your enemy
arranged like below in the “img/sv_actors” folder.



.. image:: ../images/image127.png
   :align: center



(source: !battle_snow_angel.png, basegame)

Then you’ll want just one frame of the neutral state as a separate in
the “img/enemies” folder, like pictured below.



.. image:: ../images/image75.png
   :align: center



(source: !battle_snow_angel.png, basegame)

NOTE: This single frame is only used by the Database, so the player will
never see this image. Therefore if your enemy's design changes you don’t
have to edit this image. You can actually see this in practice on Basil
and Stranger’s single frame sprites, both sporting slightly different
designs.

.. _h.reewkxco6cgw:

Basic Parameters
----------------

Now that we have our images, let’s put them into a new enemy. The first
place we’ll have to go is in the Database’s enemies tab. Then, just
scroll down until you reach empty space (you’ll need at least 4 slots)
and start working. For demonstration, I’ll just be showing the Snow
Angel’s page.



.. image:: ../images/image145.png
   :align: center



(source: TomatoRadio)

Let’s break this stuff down one at a time:

- Name: This is the enemy’s name. Wow. Very enthralling I know.
- Image: This is what the “enemies” image is for. You want to set that
  image in here. This is how your enemy will appear in the project file
  when arranging troops or testing animations.
- All Stats: These are self-explanatory. Note that for the EXP, Gold,
  and Item Drops, you have to change these for each emotion, since
  emotions are supposed to affect these drop rates.
- Action Patterns: Holdover from RPG Maker MV. OMORI doesn’t use this. I
  wonder where AI is set up…
- Traits: It’s the same traits tab you’ve come to know and… feel
  something towards. I don’t know if you love it or not. Anyway for
  enemies you’ll really just be using the traits shown above, all
  self-explanatory.

.. _h.8v8iuahpn88a:

Emotions
--------

So as you’ve noticed, every enemy has 4 versions. These are all of their
emotional variants. The way enemy emotions work is that when an enemy is
given an emotion, a function is called to transform the enemy to the new
version. This is what the <TransformEmotion> notetag in the states is
for. The number of slots these are moved is hardcoded, so enemies MUST
be placed in this order:

#. Neutral
#. Happy
#. Sad
#. Angry

And now you can change the drops, exp, AI (you’ll see below), and
anything else really.

.. _h.r6uf1afk3ltt:

Notes
-----

You can run all you like but there’s no escaping the notes tab. It’s
always there.

Let’s start with all the single line notetags.

General Notetags:

- <TransformBaseID: X> This tells the enemy what its neutral slot is. So
  you should set this to the ID of the enemy’s neutral form. Yes, even
  the neutral slot needs this.
- <Static Level: 1> Holdover from the plugins OMORI uses. This is always
  set to 1.
- <PassiveState: X> Can be used to add a state to the enemy as a passive
  state. This is mainly for passive game logic.
- <FallOnDeath> This is the notetag that makes enemies fall off screen
  when they are killed. Use this for normal enemies.

Graphical Notetags:

- <Sideview Battler: x> This is the image in the “sv_actors” folder.
  This is what is actually shown to players. You can place multiple of
  these to make an enemy have multiple possible appearances. However
  you’ll need /sv_actors and /enemies images and these need to be the
  same sizes for all versions. I guess you can use this to make varied
  colors for an enemy.
- <Sideview Battler Frames: x> This is how many frames are in a row.
  This is usually 4 in OMORI.
- <Sideview Battler Speed: x> This is the speed of the animation. It’s
  usually 12.

NOTE: This is not FPS. I don’t know exactly what it is, but higher
numbers are actually slower than lower numbers.

- <Sideview Battler Size: x, y> This is how large one frame of the enemy
  is. Basically just use the dimensions of your “img/enemies” image.
- <Sideview Width: 0> Holdover from the plugins OMORI uses. This is
  always 0
- <Sideview Height: 0> Ditto.
- <Position Offset Y: 0> Ditto.
- <StatusYOffset: x> This is the vertical offset of the Status box that
  shows an enemy’s health and name. A good starting point is a little
  less than the negative of the Sideview Battle Size Y value.
- <StatusXOffset: x> Ditto but for horizontal offset. This is rarely
  needed.
- <DamageOffsetY: x> This is the vertical offset of the Damage Numbers
  that will appear on an enemy. It looks like a lot of the inanimate
  object enemies (Things like Doombox and Watermimic) have a value
  of 30.
- <DamageOffsetX: x> Ditto but for horizontal offset. This is rarely
  needed.

Emotion Notetags:

<Sideview Battler Motion>

Name: x

Index: y

Loop

</Sideview Battler Motion>

This is a group that sets what row of the “sv_actors” images will show
depending on the enemy’s state.

X will be one of 7 things:

- Walk/Thrust/Guard/Skill/Other/Item/Spell

- This is for emotions. The y variable should be set to the row of the
  enemy’s emotion. According to the plugin description, you should only
  need the Other and Walk sets, but every enemy in OMORI uses all 7, so
  make of that what you will.

- Damage

- This is for taking damage. This is usually row 2, which is indexed as
  1.

- Dead

- This is for dying. This is usually row 3, which is indexed as
  2.        

- No line, as in the “Name: x” line is just not there.

- This should be the neutral enemy row, which is usually 0. Why this is
  needed I don’t know.

.. _h.mu3tdun032b1:

AI Notetags:
~~~~~~~~~~~~

Now for the AI, that thing that’s apparently taking everyone’s jobs.

So let’s get into how to set up the brain of your enemy.

OMORI uses the \ `Battle A.I.
Core <https://www.google.com/url?q=http://www.yanfly.moe/wiki/Battle_A.I._Core_(YEP)&sa=D&source=editors&ust=1782966892559744&usg=AOvVaw2MQLJ81N5sfSNceSDC1Jw0>`__\  plugin
by Yanfly to determine how enemies behave, so you can read that page to
get the full scope of what the plugin is capable of, because it is much
more versatile than is used in OMORI.

But for the actual tutorial, which will still be more in depth than the
basegame, but more tailored to how OMORI works.

First you’ll need this notetag.

<AI Level: 100>

This tells the game to follow the formula you’re about to write with
100% accuracy. We want that for OMORI.

Then we need to make a Notetag Group using

<AI Priority>

Now we can place down our skills.

The formula is structured with a series of checks to determine the skill
used, run from top to bottom where if a check fails, it proceeds until
one succeeds. Each check roughly look like this:

condition: SKILL x, target

That’s a lot of red, so let’s break it down a little bit.

The condition is what has to be met for the skill to be activated.
Here’s a list of the available conditions

ALWAYS: This will always activate once met. Good to use as the final
skill in a series of checks.

RANDOM X%: This is what the majority of OMORI uses. Replace x with the
percentage chance for the enemy to use this skill.

STATE === State X: This will activate if a party member has the listed
state.

You will notice that this is present on every enemy with State 186. This
is the way Observe works in OMORI, meaning that if you want to use
Observe, you must define what skills are used when it’s activated.

Note that for this and all other checks that check a stat related to the
party, only party members who meet the check can be targeted.

STATE !== State X: This will activate if a party member doesn’t have the
listed state.

SWITCH X Case: This will activate if the specified switch meets the case
listed (ON or OFF).

VARIABLE X PARAM Eval: This will activate if the specified variable
meets the eval.

Note: eval refers to basic equalities and inequalities like >= and ===
and can reference any script call or number.

USER stat PARAM eval: This will activate the user’s specified stat’s
eval is true.

STAT PARAM eval: This will activate if a party member meets specified
stat’s eval.

Type PARTY LEVEL eval: This will activate if the (Highest, Lowest, or
Average) Party Member’s Level meets the eval.

Party/Troop ALIVE/DEAD MEMBERS eval: This will activate if the
party/troop’s alive/dead members count meet the eval.

Troop is the name for enemy groups in RPG Maker MV. These will be
explained after this.

TURN eval: This will activate if the turn number meets the eval.

EVAL eval: Literally just a code check basically.

Two checks can be put together by placing +++ between them.

Next, you just put the skill you want to be used under that condition by
id.

Lastly, you put the type of target you want to prioritize. This can be

Target: Picks at random from the available targets.

Highest/Lowest Stat: The target with the highest/lowest stat.

Now. That was a bunch of words that probably sounded only partially
logical, so let me make an example with annotations.

<AI Level: 100> //This makes sure our enemy always follows this formula

<AI Priority> // This opens the group

State === State 186: SKILL 344, target //This skill will activate if
Observe is used, and will target a random party member.

Switch 21 === ON +++ Random 30%: SKILL 234, Highest HP //If the above
check failed, this skill has a 30% chance to be used if Switch 21 is ON,
and will target the foe with the highest HP.

ATK param > user.atk: SKILL 445, Lowest MP //If the above checks failed,
this skill will activate if a party member has a higher attack than the
user, and of the members with higher attack, the one with the lower MP
will be targeted.

Always: SKILL 143, target //If the above checks failed, this skill will
always be used, and the user will target a random party member.

</AI Priority> //Closes the group

Okay. That’s all for AI. I know it's pretty complex looking, and that’s
because it is. But in practice you will only be using a few of these at
a time, and once you get adjusted they are very versatile.

.. _h.mdex85wfil7i:

2-3 Tier Emotions
-----------------

Alright. Now some of you astute readers may have noticed my disregarding
of enemies capable of reaching 2nd and 3rd tier emotions, those being
Space Ex-Boyfriend, Sweetheart, The Unbread Twins, Space Ex-Husband,
and… Snaley…(I still don’t know why Snaley can feel 2nd and 3rd tier
emotions, almost certainly an oversight).

Well the reason is that they behave much differently than you might
think. If you remember way back to the states section, you’ll know that
the <TransformEmotion:> Notetag only has cases for Happy, Sad, and
Angry. So how do we make an enemy something higher?

Well there are two ways.

The first is the far simpler way, but also more rudimentary. 2nd and 3rd
tier emotions still have the <TransformEmotion:> Notetag, so if they are
used, the enemy will simply use their 1st tier emotion slot. So a
furious enemy uses its angry slot. This is how Space Ex-Husband and
Snaley work, and all you have to do is just disable the State
Resistances. However the problem with this is that it means you can’t
make any behavioral or visual adjustments between emotional tiers, just
the state changes baked into the emotions. This is why SXH and Snaley
don’t have sprites for their 2nd and 3rd tier emotions. So how do we do
what the other three emotional bosses do?

Well, it’s a little confusing at first.

So remember way back when I explained the <TransformEmotion:> Notetag?
The way it works is that each case will transform the enemy into the one
that is a hardcoded number of id slots forward from their neutral
variant. Now here’s what's good about that. You can put any emotion into
the <TransformEmotion:> Notetag, even if it doesn’t correspond with the
actual emotion of the state. So if I say, made an alternate version of
Angry, Enraged, and Furious, but set their <TransformEmotion:> to Happy,
Sad, and Angry, then we’ll have enemy slots that are unique to each of
these emotions. That’s what OMORI does. These three bosses are actually
two enemies, the first version is when they can feel all regular
emotions, and then when they become Emotion locked, they Transform into
the second version, which houses their tiered emotions.

So how do we set all that up? Simple actually.

First, make the first phase of your boss, with all their normal
emotions. Then once you’re done, copy over the neutral version of the
enemy again right below. Now make the next three slots your 1st, 2nd,
and 3rd tiers of your boss once they’ve been locked into their emotion.
Also make sure these new versions are resistant to the normal versions
of ALL regular emotions, even the ones they are locked into, since we
don’t want you to be able to add the regular emotions, which will change
the Boss’s slot.

It should once you’re done look like this.



.. image:: ../images/image54.png
   :align: center



(source: TomatoRadio)

So now we have our boss, but how do we actually fight it? Well, that’s
where the next section comes in.

.. _h.7q6h7if8ny0e:

Troops
------

Troops are the actual battles that you fight in. Both regular and boss
encounters are in here, but since regular encounters are very simple, we
will be looking at this tab from the Boss perspective, specifically the
tiered bosses.

Welcome to the Troops tab! The first thing you’ll want to do is add your
boss in here. You’ll want to select their neutral form.



.. image:: ../images/image281.png
   :align: center



(source: TomatoRadio)

Now, most bosses have about 6-8 pages of “Battle Events.” These are
Events that get triggered by specific requirements in the battle. They
are structured the same as Common Events and Regular Events, so your
workflow will be similar.

While there are a multitude of things you can do, I’ll just explain
what’s commonly done for sake of simplicity.

- Turn 0: This is a page for anything that you want before the battle
  begins. Things like dialogue and start of battle state changes should
  occur here. It’s also worth noting for all battle text, if the text is
  being spoken by the enemy, then the Control Switch “BSytem Bubble
  Toggle” should be ON, and OFF for narration. I believe this is what
  enables and disables the arrow on the text box.
- Enemy HP < #%: These pages will activate at the end of the turn once
  the enemy has reached below the specified HP.
  Since this is when Tiered emotion switches are performed, I’ll explain
  them here. You may skip ahead if your boss doesn’t have this.

- First, remove all regular emotions the enemy might have.
- Second, transform the enemy into their new form with Enemy
  Transform (SPECIFICALLY THE NEUTRAL FORM)
- Third, add the specialized 1st tier emotion to the enemy. These states
  are called Space Ex-Angry, Sweet Happy (This one is further down from
  the rest of these), and BD Sad.
- For the 2nd and 3rd tiers, remove the lower emotion and add the higher
  tier. It’s worth noting that these have check states as well. I don’t
  know what they do but you might as well add them to be safe. Likely
  game logic for certain skills or plugins.

- In addition, this is how the game plays victory events. All bosses
  that gray out the screen use the Common Event “Enemy Defeat” at the
  beginning of their event page, and then any additional dialogue may
  play.
- Actor HP < #%: These pages activate when the actor’s HP (Usually
  OMORI’s) is below a certain threshold, usually dead. This is how
  defeat text is displayed.
- Turn #: These will activate on the selected turn number. Most used for
  scripted fights like Basil or Stranger.

Lastly, these troops are what events use to start battles. You can use
the “Battle Processing” command to make a troop’s battle begin.

And I think that’s everything about OMORI's enemies. It’s a lot of small
vital pieces, so you will likely have to do some of your own
experimentation, but this should act as a good springboard to make all
of this less daunting.

.. _h.rxmxx9evltp:
