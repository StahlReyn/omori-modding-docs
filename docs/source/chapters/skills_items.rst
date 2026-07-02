Skills & Items
==============



.. image:: ../images/image49.png
   :align: center



And now we’re right back into the hole of complexity. But at least these
are more fun, at least in my opinion. You may already know of the skills
the party can learn in OMORI, but in modding, Skills are not just those,
but rather every type of attack/move that both you and your enemies can
perform. So this means we can do a lot with these.

.. _h.fcxo3a1o12yf:

General Skill Configuration
---------------------------



.. image:: ../images/image181.png
   :align: center



(source: TomatoRadio)

This is the Skills tab, with Omori's Exploit open. Here I will detail
all the settings in the middle column. Anything I don't mention is not
used in OMORI, and should be left as is.

General Settings:

        Name: Self Explanatory

        Description: The description used in the menu. Don’t forget to
list the cost.

        Skill Type: All skills except regular attacks and Calm Down
should be Power Of Friendship. This is how Afraid restricts skill
access.

        MP Cost: Juice Cost. Make sure to update the Description with
this value.

        Scope: Who is the target. Note that being able to target both
friends and foes is done in Note Coding, so set it to 1 Ally for those.

        Occasion: If a skill can be used from the Menu, select Always,
otherwise select Battle Screen.

Invocation:

        Speed: Added speed when determining turn order. If you want a
skill to act first, spam 9 in here. There is a cap of 2000.

        Repeat: Times the skill's action is repeated. This can also be
done with Note Coding.

        Hit Type: Physical Attack for all damaging skills, Certain
Hit for non-damaging skills. Effectively determines if the skill factors
in Hit Rate.

        Animation: The animation that plays upon use. It will play on
the target of the skill. Can also be done with more precision in Notes
Coding.

Message: Adds text. Can be done with more detail in Notes Coding. If you
are using this, make sure to include a space at the front.

.. _h.ive0gi77lac:

Damage Formulas
---------------

Most skills have their damage calculated in the Damage section in the
top right corner. I'll go over the settings aside from the Formula
before delving into that.

[Probably best to place a crop of the damage section here]

Type: Determines whether Heart or Juice is affected, and whether it's a
healing or damaging skill. HP Drain and MP Drain aren't used by OMORI,
but they heal the damage done back to the user. This can be achieved
with more precision with Notes Coding.

Element: Almost always None. If you set it to something other than None,
emotional typing won't work with the skill. Best use for this is setting
it to EMOTION to be strong against a target with emotion.

Variance: A variance applied to the final damage of an attack. Normally
20% for damaging skills.

Critical Hits: Self-Explanatory

And now for the Formulas. RPG Maker MV uses a very specific system for
writing out formulas that must be followed correctly.

The first part of the system is how the user and target of a skill are
referred. They are known as a and b respectively. In addition if an
extra party member's stats are needed, they can be called by
$gameActors.actor(#), with # being their ID (1 for Omori, 2 for Aubrey,
3 for Kel, and 4 for Hero).

The next part is the stats being factored in. If we want to use the stat
of a battler, we must put their name with a period, and then the
abbreviation for the stat. In practice this looks like "a.atk" for the
user's attack stat.

List of Stat Shorthands:

hp - HP (Heart)

mhp - Max HP (Max Heart)

mp - MP (Juice)

mmp - Max MP (Max Juice)

atk - Attack

def - Defense

mat - Magic Attack (Not used by OMORI)

mdf - Magic Defense (Not used by OMORI)

agi - Agility (Speed)

luk - Luck

tp - TP (Not used by OMORI)

level - Level

After that we have the operations that can be used. These include
Addition, Subtraction, Multiplication, and probably Division(In OMORI
the devs just multiplied by decimals), all of which use the standard
keyboard symbols for them. Parenthesis can be used to create Order of
Operations equations. If you don’t remember what that is just google
“PEMDAS.”

<These formulas could have better color coding. Maybe faint highlights
like This>

This is all you need for basic formulas that don't have any variables
other than character stats. So for example an attack that adds the
attack of the user and Hero's luck, multiplies the sum by 2, and then
subtracts that by the target’s defense would look like: "(a.luk +
$gameActors.actor(4).luk) \* 2 - b.def"

The last part of these damage formulas are what I will call "State
Checks," which use if-then statements to determine what formula to use.

<Is this example too complicated? Should a simpler one be used? I chose
it so that a reader could see how to work with basically every operator
that if-thens have.>

(a.isStateAffected(6) \|\| a.isStateAffected(10) \|\|
a.isStateAffected(14)) ? a.atk \* 4 - b.def : (a.isStateAffected(7) \|\|
a.isStateAffected(11) \|\| a.isStateAffected(15)) ? a.atk \* 5 - b.def :
(a.isStateAffected(8) \|\| a.isStateAffected(12) \|\|
a.isStateAffected(16)) ? a.atk \* 6 - b.def : a.atk \* 3 - b.def;

This is one of the most extreme examples of this in OMORI, being the
skill Final Strike, which deals more damage the higher Omori's emotion
is. Let's take it one step at a time.

"(a.isStateAffected(6) \|\| a.isStateAffected(10) \|\|
a.isStateAffected(14)) ?”

This code checks if the user (Omori) is affected by state 6, 10, or 14,
which are Happy, Sad, and Angry respectively. The \|\| acts as a
shorthand for "or." And the "?" as a shorthand for "then."

So this code would read to a normal person as "If the user is affected
by state 6, or state 10, or state 14, then [proceeds to the rest of the
action.]"

"a.atk \* 4 - b.def"

This code will activate if the previous conditions were met, which is
thanks to the ? before this code.

This is the actual damage calculation for if Omori is at a stage 1
emotion. It's the user(Omori)'s attack times 4 minus the foe's defense.

": (a.isStateAffected(7) \|\| a.isStateAffected(11) \|\|
a.isStateAffected(15)) ?"

This code will activate if the previous conditions were not met, which
is thanks to the ":" at the front of this section, which acts as a
shorthand for "else." This code does the same check as before, but now
for the stage 2 emotions. So this will be the condition to be met.

"a.atk \* 5 - b.def" This code will activate if the newly defined
conditions of being at a stage 2 emotion are met. The code reads the
same as the previous formula, but now the user's attack is multiplied by
5.

": (a.isStateAffected(8) \|\| a.isStateAffected(12) \|\|
a.isStateAffected(16)) ?" This code is the exact same as the check for
stage 2 emotions, but now for stage 3.

"a.atk \* 6 - b.def" This code is the exact same as the stage 2 formula,
but now the user's attack is multiplied by six.

": a.atk \* 3 - b.def;" This code is activated if all the above
conditions are failed, meaning Omori has no emotions. The damage formula
itself is once again the same but the user's attack is multiplied by
only three.

And lastly any state checking formulas like this must have the final
formula end with a semicolon (";")

This was a really complex example, which I chose for demonstration
purposes, but you can make much simpler ones with only one state check,
or go even further and add more checks and variables. Since this simply
checks if you are affected by a specific state, you aren't limited to
just emotions. Buffs, Debuffs, and other states can also be checked, and
for anyone, not just the user. For example you could have
"$gameActor.actor(4).isStateAffected(1)" Which will check if Hero is
dead. This system is very versatile.

.. _h.cdim5qhr6fzn:

Notes Coding
------------

Now for the most complex section of making skills. The Notes tab. As
you’ve seen before, the notes tab in OMORI can act as a JavaScript host
alongside a lot of Plugin Commands, allowing you to make much more
complex skills. Thankfully due to how many skills are in OMORI, you can
pretty easily learn how to use them here by cross referencing different
skills. A lot of these notetags are from the \ `YEP Action Sequence
Packs <https://www.google.com/url?q=http://www.yanfly.moe/wiki/Category:Action_Sequences_(MV)%23Action_Sequence_Pack_1&sa=D&source=editors&ust=1782966892528710&usg=AOvVaw05SuI3pq-lBLyS6FLCmZ8a>`__\ ,
which will give you the full list of the options that you can use from
these plugins. I will only discuss the common stuff.

.. _h.fyxt06s3lygi:

General Parameter Notetags
~~~~~~~~~~~~~~~~~~~~~~~~~~

These notetags can be added to skills to make small functional or
aesthetic changes. These can be placed anywhere in the Notes tab, but
are usually placed at the top for organization.

<BattleLogType: string> This notetag determines what text to display
from a .js file called Custom Battle Action Text.js. Personally I prefer
using a different way of displaying text, but this can be used for basic
attacks where you just want "User attacks Target!" In this case just add
"<BattleLogType: ATTACK>"

<AntiFail> Some skills do things other than heal or harm a friend or
foe, but RPG Maker MV might still show a "It had no effect" message.
This disables that.

<HideInMenu> Self-Explanatory. Hides it from the skill equip menu. Use
this for your Basic Attacks and Follow-Ups.

<Enemy or Actor Select> The emotion skills, Sad Poem, Pep Talk, Annoy,
and Massage, can be used on both friends and foes. This is achieved with
this Notetag.

.. _h.hboc9ai01d2u:

Action Sequence Notetags
~~~~~~~~~~~~~~~~~~~~~~~~

These notetags can be added to skills to add extra flairs to the skill
in the Notes Coding. All of these must be placed before and after their
contained code, with the closing version having a / in front of the name
like this </Target Action>

<Setup Action> The earliest of the 4. This happens before any juice is
consumed, so things like User animations and other "setup actions" will
usually occur here.

<Whole Action> This occurs right before the main action, and applies its
effects to all targets simultaneously. However, it does this in a bit of
an odd way. It calculates the action for one target, and then dupes the
results onto everyone else. This can cause some issues for effects that
are based on target-by-target variables like their level of buff or
debuff.

<Target Action> In my opinion, the better Whole Action. Occurs exactly
as the main action effect will occur, and works its effects on each
target individually. So things like attack animations and state
changes should occur here. However unlike Whole Action, you can visually
seMake sure that if you use Target Action, you must define when the
skill's main action occurs. This is done with the line "action effect,"
which can be placed multiple times if you want the move to activate
multiple times, like Red Hands.

<Follow/Finish Action> Two rarely used aftermath sections. These are
used for times where a closing action needs to occur that isn't part of
the target action. I don’t know the difference between Follow and Finish
but Finish comes after Follow if both are used.

.. _h.nc96qwcgvx5y:

Action Sequences
~~~~~~~~~~~~~~~~

NOTE: Y in all of these contexts is what the action is targeting. This
can be filled in with a frankly overwhelming amount of options. The
important ones are user, target, actors, and enemies. These should
hopefully be self-explanatory. Once again, Yanfly’s page for the plugin
lists all your options.

add state x: y Adds the specified state to the target.

remove state x: y Adds the specified state from the target.

animation x: y Plays the specified animation. Y is where the animation
will play.

wait for animation Waits for all animations to end before proceeding.
Can sometimes be a bit buggy.

wait: # Waits the set number of frames before continuing. RPG Maker
MV runs at 60fps, so wait: 60 will wait for one second.

HP ± x: y(, show) Adds or subtracts the specified heart from the target.
If show is placed after the target, the damage popup will be displayed.
Percentages may be used.

MP ± x: y(, show) Adds or subtracts the specified juice from the target.
If show is placed after the target, the damage popup will be displayed.
Percentages may be used.

.. _h.sevnhmmfix5b:

Text Notetag
~~~~~~~~~~~~

The "eval:" notetag can be added to skills to execute JavaScript, but it
is mainly used in OMORI to display text. Like this:

eval: BattleManager._logWindow.push("addText", \`${user.name()} hypes up
${target.name()}!\`)

This is a line from a mod I'm working on, but that's not important. What
is important is that this is all you need to display detailed text in
OMORI's battle box. The red text is what's actually shown in game, with
the user and target name's being self-explanatory. Since it's part of
the Notes coding, you can determine when in the skill it plays, and have
if and then statements change the line used. It's rather versatile and
simple.

.. _h.czp8rta8z9qe:

Eval Notetags
~~~~~~~~~~~~~

These are some other Notetag Headers that can be added to Skills. Unlike
the Action Sequences, these use pure JavaScript, so be aware of that.

<Custom Requirement> This sets any extra requirements for a skill to be
usable. This does NOT prevent the player from selecting it, but will
stop the skill’s execution during their turn. This is done by the
boolean "value" that determines if a skill can be performed or not. This
is mainly used for Follow-Ups, which check if the recipient is dead.

.. _h.1crp8crmb2xy:

Follow-Ups
----------

Follow-Ups, as to be expected, work quite differently from all the other
skills in OMORI. This will explain how to set them up.

.. _h.6gniamqs8nek:

All Tiers Of The Follow-Up
~~~~~~~~~~~~~~~~~~~~~~~~~~

In OMORI, your follow-ups get stronger after hitting specific story
beats. These upgrades to your follow-ups are separate skills in the
Database, and as such you need to have a "Pre-Skill" that checks what
skill should be used, and then activates that skill. In OMORI, these are
called Checks.

Before the Checks actually determine what skill to use, they have
a <Custom Requirement> notetag that checks to see if the party members
involved in the follow-up are dead. This will lock the skill if they are
dead. You can just copy paste that requirement from a pre-existing
check.

Now for the actual Check. This is done by activating a Common Event from
the Effect section. This Common Event will then go through an if-else
chain to see if the player has met the story beat needed for a specific
tier, if they have, it uses the Force Action event on the Party Member
to use the actual Follow-Up on the Last Target. It roughly looks like,

If : StoryBeat2 is on

        Force Action : Basil, Vent 3, Last Target

        jump to label: stop

         end

Else :

If : StoryBeat1 is on

        Force Action : Basil, Vent 2, Last Target

        jump to label: stop

         end

        

        Else:

Force Action : Basil, Vent 1, Last Target

                end

label : stop

However, if your follow-ups don’t get stronger over time (for example
Basil in the console version, due to only being accessible on One Day
Left, after both story beats) then you don’t need these Checks.

.. _h.o7876hxu3byv:

Attaching The Follow-Ups To Your Attacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we're done with the annoying and tedious part. The rest is easy.

To attach your follow-ups, you have to add this Notetag to your basic
attack for all 3 follow-ups it has.

<ChainSkill: #, direction> The # gets replaced with the ID of the Check,
not any of the actual Follow-Ups. The direction is what arrow key has to
be pressed to activate the Follow-up. up, down, left, and right.

.. _h.g864wb6yqmvh:

Follow-Up Notetags
~~~~~~~~~~~~~~~~~~

<ChainSkillIcon: #> This determines what image to use for the
Follow-Up bubble. You can see them in img/system/ACS_Bubble.png. If
you're adding new Follow-Ups, refer to the \ `Sprites &
Art <#h.gsbdya7y8lgi>`__\  page for adding new Follow-Up bubbles. What I
didn't mention there is how they are indexed. It's the same as most
images in OMORI, starting at 0, left-to-right, top-to-bottom.

<ChainSkill[Name of a followup]> I don't know what exactly these do, but
I recommend just setting them to the Follow-Up that uses that slot
normally. So for example, Basil's comfort follow-up is his down
follow-up, and he takes Kel's place in the battle menu, so I'd set
Comfort to <ChainSkillPassToOmori>

<EnergyCost: #> Self Explanatory. All but Release Energy cost 3 energy,
with Release energy costing 10, but you can set them all to whatever you
like(Within reason. I don't know what would happen if you set one to
0 or anything above 10, probably works as expected, but just be ready if
something goes wrong).

<HideInMenu> Not Follow-Up specific but make sure they don't show in the
skill menu.

.. _h.nmc754yr9x7j:

Items
-----

Luckily for us, Items for the most part are simply one time use skills,
so most of the skill code carries over to here, and therefore I will
only go over the differences.

.. _h.l9zryvyt8sd6:

General Settings
~~~~~~~~~~~~~~~~

Item Type: Regular Item for Snacks and Toys. Key Item for Important
Items, alongside any Items that are hidden in the menu, like Hangman
Keys (Known internally as Blackletters)

Price: Not actually the cost in a store, but rather double the sell
price. Yes it’s weird but OMORI is just like that.

Consumable: Yes for Snacks and Toys. No for Important Items.

Element: HEART ITEMS for hp snacks. JUICE ITEMS for juice snacks. Items
that heal both are HEART ITEMS. Physical for damaging toys.

Variance & Crits: No. None. N/A. Null.

<IconIndex: #> The icon to be used in the menu. Indexed the same way
everything else in OMORI is. The sheet used
is img/system/itemConsumables.png or img/system/itemImportant.png
depending on if it’s a regular or key item.

<IsToy> Add this to the notes if it's a toy.

.. _h.qw460trh7jcv:
