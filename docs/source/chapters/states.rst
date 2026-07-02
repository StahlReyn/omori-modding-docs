States
======



.. image:: ../images/image7.png
   :align: center



“Oh boy, I’m going to learn about states? Aren’t those how battle
emotions are stored? Can I make my own emotions? I’m gonna make so many
cool emotions for the player to use!”



.. image:: ../images/image87.png
   :align: center

  

(source: image by u/Whisp_Is_My_Waifu)

“What the [WTF Value 13] is wrong? Why isn’t it working!”

It’s not actually that scary, especially since you’re having it
explained to you directly, but it sure was hell figuring this out when I
(TomatoRadio) literally just started modding.

Now. Like your hypothetical future modding peer said, yes you’re going
to learn about States, and that does include learning about emotions.
But before we can start making new feelings for our friends and foes to
feel, we have to learn the basics of how states work, since they are
much more than just emotions.



.. image:: ../images/image88.png
   :align: center



(source: TomatoRadio)

Wowie! It’s the States tab, in the Database. This is where every single
passive battle effect in the game resides. Buffs, debuffs, counters, an
immense amount of game logic, they’re all in here.

.. _h.keyjwp9cztg:

Basic Settings
--------------

I’ll first give a brief overview of the middle column stuff. If I don’t
mention something, don't touch it, it probably just doesn’t work in
OMORI. (If you haven’t already figured it out… OMORI tends to go its own
route most of the time instead of just using default RPG Maker
MV tools.)

- Name: This is the name of your state (wow, so smart…). However, this
  name is never shown in OMORI. For example, the UNCONSCIOUS state is
  actually what TOAST & BLACKED OUT is called. Still, it’s best to name
  these states something easily distinguishable, so you can tell them
  apart.
- Remove at Battle End: This is self-explanatory. You want this enabled
  for pretty much everything so that states don’t persist between
  battles. (Charms that add states at the start of battle work
  differently.)
- Auto-removal Timing: Determines how long a state lasts. Mostly
  self-explanatory.
- Messages: Self-Explanatory.

.. _h.3us6hxj0kton:

RPG Maker MV's Traits
---------------------

Traits are modifiers placed onto the battler inflicted with the state.
You can add as many as you like in one state. An \* indicates the trait
is not used in OMORI.



.. image:: ../images/image158.png
   :align: center



(all trait windows source: TomatoRadio)

Element Rate: A percentage based multiplier on the damage taken from the
element listed. This is used mainly for Emotions.

\*Debuff Rate: Changes the probability that a skill or item will debuff
the listed stat.

\*State Rate: Changes the probability that a skill or item will inflict
the listed state.

(Note: These only affect the “Add State” effect in skills and items, not
the notetags that most of OMORI uses.)

State Resist: Become immune to the listed state.



.. image:: ../images/image10.png
   :align: center



Parameter: A percentage based multiplier on the listed stat.

Ex-Parameter: A percentage based adder on the listed stat.

Sp-Parameter: A percentage based multiplier on the listed stat.
All of these parameters will be detailed in the following section.



.. image:: ../images/image114.png
   :align: center



Attack Element: Adds the listed element to any skills used. Mainly used
for Emotions.

\*Attack State: Adds percentage based chance that an attack will add the
listed state.

(Note: These only affect the “Add State” effect in skills and items, not
the notetags that most of OMORI uses.)

\*Attack Speed: A speed boost added to any skill used.

Attack Times +: Repeats the skill used. So +1 makes the skill happen
twice.



.. image:: ../images/image6.png
   :align: center



\*Add Skill Type: Adds the listed skill type to the available skills.
This doesn't really apply to OMORI.

Seal Skill Type: Seals use of the listed skill type. Only really used by
afraid.

\*Add Skill: Learn the skill listed. The learned skill is not equipped,
but simply added to the available skills. Equipping skills is done
through troop events in OMORI.

\*Seal Skill: Seals use of the listed skill. Works fine, it's just not
used in OMORI.



.. image:: ../images/image195.png
   :align: center



\*Equip Weapon: Unlocks the inputted weapon type. This would allow for
characters to equip each other's weapons if out of battle.

\*Equip Armor: Unlocks the inputted armor type. All of OMORI's charms
except for FA Kel's Pet Rock are the same type.

Lock Equip: Locks the inputted equipment type. This means you can't
change your equipment while the state is active. This isn’t used by any
states, but is used for Omori and Sunny’s weapons.

\*Seal Equip: Seals the inputted equipment type.

\*Slot Type: Meant for dual-wielding. Doesn't work in OMORI.



.. image:: ../images/image11.png
   :align: center



\*Action Times +: A percentage based chance that an actor will execute a
command a second time. These can stack.

\*Special Flag: Applies effects that don't work in OMORI.

\*Collapse Effect: Determines the death animation. Doesn't work in
OMORI. That is handled in the enemy’s note tab.

Party Ability: Adds a party wide ability. Only Gold Double and Item Drop
Double work and only Gold Double is used.

.. _h.5g2iuqsaut7f:

Parameters
----------

Parameters are a rather weird aspect of RPG Maker MV in regards to
OMORI, due to many parameters, which I will now interchangeably refer to
as stats, not having much effect, or having inconsistent effect due to
OMORI’s extensive use of plugins.

Now, there are three categories of Parameters, normal parameters
(referred to simply as parameters), Ex-Parameters, and Sp-Parameters.
The differences in these is how the stats are numerated, which I will
break down now.

.. _h.kb2gvx73224i:

Normal Parameters
~~~~~~~~~~~~~~~~~

These are the most normal form of stats in RPG Maker MV. These are
integers that increase from 0 and grow for every level an Actor gains,
with the rate of growth determined by their Class. Here’s a list of each
of these individually and what they do:

The left name is the full name of the stat while the name on the right
is the 3 letter code the engine uses to refer to the stat.

Max HP: mhp

This is the maximum HP (or HEART) of the battler. The current HP of the
battler uses the code hp.

Max MP: mmp

This is the maximum MP(or JUICE) of the battler. The current MP of the
battler uses the code mp.

Attack: atk

This stat has no defined function in RPG Maker MV. Instead it is used by
the developers for the formulas of the Skills. However in OMORI, this
stat is obviously used to determine the damage a battler deals.

Defense: def

Another freeuse stat. In OMORI, this stat is used for determining how
much damage a battler resists from an attack.

M. Attack: mat

Yet another freeuse stat. This stat goes unused in OMORI, so make of it
what you will as for how you want to apply it.

M. Defense: mdf

The last freeuse stat. This stat also goes unused in OMORI, so make of
it what you will as for how you want to apply it.

Agility: agi

Known in OMORI as SPEED, this does have a combat function. Turn order is
determined by agility, so faster battlers act first.

Luck: luk

Used for critical hit rate (as in hitting in the heart). Every point of
luck is +1% to a base crit chance of 0%.

.. _h.uyrilhqkzdlm:

Ex-Parameters
~~~~~~~~~~~~~

These are Extra stats (get it that’s why they’re called Ex-Params) that
are percentages increasing from 0%. They do not grow with level. When
calling them by scripts, they are a decimal between 0 for 0% and 1 for
100%. So a 0.5 is 50%.

Hit Rate: hit

Exactly what it says on the tin. Any skill using the “Physical Attack”
Hit Type will perform a hit rate check to see if the skill connects.

Evasion: eva

The counter to hit rate. If the hit rate check is passed, then a
separate check for the defender’s evasion is done for the chance to
evade the attack. This means that an attacker with 1000% hit rate can
whiff an attack to a 1% evasion. It’s pretty dumb but that’s just the
way it is.

Critical Rate: cri

In normal RPG Maker MV, this stat is used to determine the chances to
land a critical hit. However, OMORI placed this role on luck instead,
leaving this unused.

Critical Evasion: cev

Same deal as critical rate.

Magic Evasion: mev

An unused stat in OMORI, if the skill’s Hit Type is “Magical Attack”,
then this stat is checked instead of evasion for dodging attacks.

Magic Reflection: mrf

An unused stat in OMORI, if the skill’s Hit Type is “Magical Attack”,
then this stat is checked to reflect the attack back to the attacker.

Counter Attack: cnt

An unused stat in OMORI, if the skill’s Hit Type is “Physical Attack”,
then this stat is checked to initiate a counterattack back to the
attacker.

HP Regeneration: hrg

At the beginning of every turn, the battler will restore a percentage of
their Max HP. The exact percentage is your stat.

MP Regeneration: mrg

At the beginning of every turn, the battler will restore a percentage of
their Max MP. The exact percentage is your stat.

TP Regeneration: trg

At the beginning of every turn, the battler will gain a percentage of
TP. The exact percentage is your stat. TP goes unused in OMORI.

.. _h.1ts9hbpxayew:

Sp-Parameters
~~~~~~~~~~~~~

These are special stats that are percentage based modifiers to general
rates. When calling them by scripts, they are a decimal of 1 for 100%.

Target Rate: tgr

From what I currently know, this stat likely has no effect in OMORI.
However it is supposed to determine the chance of an enemy targeting an
actor.

Guard Effect: grd

The effectiveness of using Guard.

Recovery Effect: rec

Increases/Decreases the amount of HP and/or MP recovered from any source
by the modified percentage.

Pharmacology: pha

Increases/Decreases the potency of item formulas by the modified
percentage.

MP Cost Rate: mcr

Increases/Decreases the cost of Juice skills in battle by the modified
percentage.

TP Charge Rate: tcr

Unused in OMORI and doesn’t work.

Physical Damage: pdr

Increases/Decreases the damage taken from skills using the “Physical
Attack” Hit Type by the modified percentage.

Magical Damage: mdr

Increases/Decreases the damage taken from skills using the “Magical
Attack” Hit Type by the modified percentage.

Floor Damage: fdr

Unused in OMORI and doesn’t work.

Experience: exr

Increases/Decreases the exp received at the end of a battle by the
modified percentage.

Note: The state tag, “Remove at Battle End” removes the state before the
party is given exp, so this effect will go unused if placed like this.
You can actually see this in the Release Energy buff.

.. _h.vvpb0wv5houi:

Notetags
--------

Now it’s time for you to meet the section of RPG Maker MV where you will
slowly lose your sanity. The Notes Section.

\*The Dracula Piano Sting and a lighting strike.\*

You’ve seen these a little in the \ `Events
Section <#h.3ek5unxwrmmt>`__\ , but now you’ll see them properly.

In standard RPG Maker MV, this is simply an area to put regular notes,
but since OMORI is an actually respectable RPG Maker MV game, it uses a
plentitude of plugins which turn the Notes section into a pseudo
JavaScript host. The top 9 tabs of the Database all have Notes (Except
Troops) and over the course of these tutorials you’ll learn what you can
do with them. But to start out, let’s look at their use in the States
tab.

.. _h.irht3fpwxs74:

Notetag Groups
~~~~~~~~~~~~~~

In the States tab, most Notetags are held in what we’ll call “Notetag
Groups” which are Heading Notetags that are set up like this.

<Notetag Group>

Code

Code

</Notetag Group>

If that looks familiar it’s because that’s how HTML works.

For our states, there are a few different Notetag Groups that determine
when the code in them gets triggered. These are only the common ones, a
few more can be found at the \ `YEP Buff States
Core <https://www.google.com/url?q=http://www.yanfly.moe/wiki/Buffs_%2526_States_Core_(YEP)%23Lunatic_Mode&sa=D&source=editors&ust=1782966892497931&usg=AOvVaw0zkRNb5ccn9fR1uE_sM0wt>`__\  plugin
page.

<Custom Apply Effect> Runs when the state is first applied.

<Custom Remove Effect> Runs when the state is removed.

<Custom Leave Effect> Runs when the state is removed specifically due to
its duration ending.

<Custom Turn Start/End Effect> Runs when the battler’s turn starts/ends.

<Custom Action Start/End Effect> Runs when the battler’s action
starts/ends.

<Custom Battle Effect> Runs when a battle is started. Useful for Armors
that add states at the beginning of the battle.

<Custom React Effect> Runs when the battler is selected as the target of
a skill. You can see this used by Sad for the Juice drain.

.. _h.1nzlmujslwqj:

Coding Notetags
~~~~~~~~~~~~~~~

States specifically use very little of what these are capable of, so
I’ll only detail a small fraction of it. These are placed inside the
notetag groups.

NOTE: X in all of these contexts is what the code is targeting. In most
contexts you will use “user” for the battler with the state. However, if
you are using <Custom React Effect>, then you will instead use target.
You can also use the $gameActors.actor(ID) script call for specific
actors.

x.addState(y) adds the state with the ID of y to x.

x.removeState(y) removes the state with the ID of y from x.

x.removeStateCategoryAll(“y”) removes all states with the category “y”
from x.

x.gainHp(y) heals x for y Heart.

x.gainMp(y) heals x for y Juice.

.. _h.oaru3n8icamy:

OMORI Emotions
--------------

So. We’re here. We made it to the emotions. The part you are probably
here for.

This section will go over how emotions are set up. Now, let me give a
huge asterisk to all of this section. OMORI’s emotion system is built
off of many plugins working in tandem with the built in state effects.
What I am going to teach is what I believe are the minimum requirements
to get emotions to function, meaning there are likely cases where your
emotion will break.



.. image:: ../images/image103.png
   :align: center



(source: TomatoRadio)

This is the State for the Ecstatic emotion.

First we will look at the traits, as they are the easy part of this.

The traits have 3 parts.

- The stat changes. For Ecstatic, these are the Hit Rate, Luck, and
  Speed modifiers. Every emotion should have at least 1 positive and 1
  negative stat change.
- Elemental typing. In RPG Maker MV you set the resistances and
  weaknesses for elements.

- First you should set the attack element to the emotion (new elements
  can be defined in the Types tab), making all attacks from the
  character be the emotion’s element.
- Then, add the Element Rate for the resistance, which in this case is
  angry. Set it to the correct percentage listed above.
- Finally, add the Element Rate for the weakness, which in this case is
  sad. Also do this for the Emotion element. I don’t know exactly what
  uses it, but it’s likely important.

- State Resistances. Make your state resistant to the lower tiers of its
  emotion. So for Ecstatic we are resistant to the basic Happy emotion.

And, presto, we have 1 of three parts of our emotion done!

Also, this is how Buffs and Debuffs are set up, excluding the elemental
stuff.

Next step, the Notes coding. Which actually is really easy for emotions.

<TransformEmotion: happy>

//GRAPHICS

<StateFaceIndex: 2>

<StateBackIndex: 3>

<StateListIndex: 4>

<BattleLogType:ECSTATIC>

//STATE CATEGORIES

<Category: EMOTION>

<Category: HAPPY>

<Custom Apply Effect>

user.removeStateCategoryAll("SAD")

user.removeStateCategoryAll("ANGRY")

user.removeStateCategoryAll("AFRAID")

user.result().removedStates = user.result().removedStates.filter(s =>
!user._isEmotionalState(s))

</Custom Apply Effect>

Here are the Notes for Ecstatic. We'll go step-by-step.

- The <TransformEmotion: x> is for Emotions that change the enemy’s
  appearance. If you don’t want that, remove this line. What this does
  is it tells the game what variant of an enemy a foe should use when
  affected by this state. I’ll explain this better in a little bit.
- The “//GRAPHICS” lines are for your party and determine what
  portraits, backgrounds, and labels to use for the state, respectively.
  These are all indexed from 0 and go from top to bottom.
- The <BattleLogType:X> determines what text to display when afflicted
  by the emotion. This is done with the “Custom Battle Action Text.js”
  plugin. If you’re adding your own, you can just copy paste another
  emotion and replace the text as needed.

- The “//STATE CATEGORIES” lines are used in various other Notetags so
  that emotions can be referenced without having to check for every
  tier.
- The <Custom Apply Effect> removes Sad, Angry, and Afraid, and is an
  example of State Categories in use.

.. _h.wsmakoihvb9:

JavaScript Modding
~~~~~~~~~~~~~~~~~~

Lastly is two bits of plugin modification. I have never seen a mod use
this first one before, and in fact I had to discover this on my own, so
be warned— this is likely buggy.

When modding JavaScript files, it’s better to make new JavaScript files
that overwrite code rather than patching it. This is for mod
compatibility. So that’s what this will do. So make a new JavaScript
file, this can easily be done by copy pasting any of the "Header files"
like ------------------.js, and then add these two bits of code into
your file. These are modded versions of existing code, so when loaded in
game, these will overwrite the original files.

//=============================================================================

// REFRESH ENEMY EMOTIONS from Omori BASE.js

// What this code does is it defines what Emotions can be felt by
Enemies, and what slot each emotion should use. The emotion states
reference this code with <TransformEmotion: emotion> with emotion being
one of the cases listed with happy, sad, angry, and new_emotion_here.
The 'new_emotion_here' case is a demonstration of how to add more
emotions. So if I put <TransformEmotion: new_emotion_here> on a state
and give it to an enemy, it will transform into the enemy four slots
ahead of its neutral form in the Database.

// tl;dr 'text in quotes like this' can be put in <TransformEmotion:
emotion> on states and these lines do that work.

//Add more lines for all emotions you want to add. Don’t forget to add 1
to the number for each one, too.

//=============================================================================

Game_Enemy.prototype.refreshEmotionStateTransform = function() {

  // If Not Dead

  if (!this.isDead() && !this._isStateTransforming) {

        // Get Emotion

        var emotion = this.getStateEmotion();

        // Get base Id

        var baseId = this.enemy().meta.TransformBaseID;

        // Set Base ID

        baseId = baseId ? Number(baseId) : this._enemyId;

        // Set Transform ID

        var transformId = this._enemyId;

        // Switch Case Emotion

        switch (emotion) {

          case 'normal': transformId = baseId ;break;

          case 'happy': transformId = baseId + 1 ;break;

          case 'sad': transformId = baseId + 2 ;break;

          case 'angry': transformId = baseId + 3 ;break;

          case 'new_emotion_here': transformId = base Id + 4 ;break;

          break;

        };

        // If Transform Id

        if (transformId !== this._enemyId) {

          this._isStateTransforming = true;

          if(this.name() === "SPACE EX-HUSBAND") {

            $gameScreen.setFlashWait(60)

            $gameScreen.startFlash([255,255,255,255], 130)

          }

          this.transform(transformId)

          this._isStateTransforming = false;

        };

  };

};

//-----------------------------------------------------------------------------

// EMOTION ELEMENTAL FIXES from YIN_OmoriFixes.js

// What this code does is it controls what states are emotions and uses
that for moving and dull attacks. So in order to have new emotions work
with that system, we must add them here. Replace x, y, and z with the
ids of the three tiers of your new emotion. In case you're wondering,
the states for Sxbf, Sweetheat, and the Twins are special versions of
their tiered emotions.

// tl;dr Replace x y and z with your new emotion ids so Moving and Dull
attacks work.

//-----------------------------------------------------------------------------

Game_Action.prototype.calcElementRate = function(target) {

        /\*if (this.item().damage.elementId < 0) {

            return this.elementsMaxRate(target,
this.subject().attackElements());

        } else {\*/

            // YIN Instead of bypassing the subject's attack element, we
want to use it if they are inflicted with an emotion.

            // If elementId == None or Normal Attack

            if (this.item().damage.elementId < 1) {

                // These are all base emotion states (non afraid)

                var emotionStates = [6, 7, 8, 10, 11, 12, 14, 15, 16];

                emotionStates = [...emotionStates, 119,120,121]; //
Space Ex Boyfriend

                emotionStates = [...emotionStates, 122,123,197]; //
Sweetheart

                emotionStates = [...emotionStates, 124,125,126]; //
Unbread Twins

                emotionStates = [...emotionStates, x,y,z]; // New
Emotions

                // Search states for emotion states

                var emotionAfflicted;

                this.subject()._states.forEach(function(stateId) {

                    // Do we have an emotion state on us?

                    if (emotionStates.contains(stateId)) {

                        emotionAfflicted = true;

                    }

                }, this);

                if (emotionAfflicted) {

                    return
target.elementRate(this.subject().attackElements()[0]); // If so, that
is our attack element

                } else {

                    return
target.elementRate(this.item().damage.elementId);

                }

            } else {

            return target.elementRate(this.item().damage.elementId);

            }

        //}

};

.. _h.7bhqrvvklm0t:

Plot Armor
----------

[TODO] [Basically a rephrasing of
\ `this <https://www.google.com/url?q=https://omori-modding.gitbook.io/wiki/rpgmaker/custom-battles/plot-armor&sa=D&source=editors&ust=1782966892513834&usg=AOvVaw28Z31OkEU94ZXzuX-vdcnA>`__\ ]

.. _h.fxyhekvcpn5l:
