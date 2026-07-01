Custom Skill Notetags
=====================

Only the usage of notetags in skills will be covered here, as the rest
is focused on base RPG Maker MV.

General Parameter Notetags
^^^^^^^^^^^^^^^^^^^^^^^^^^

These notetags can be added to skills to make small functional or
aesthetic changes. These can be placed anywhere in the Notes tab, but
are usually placed at the top for organization.

``<BattleLogType: string>`` This notetag determines what text to display
from a .js file called Custom Battle Action Text.js. Personally I prefer
using a different way of displaying text, but this can be used for basic
attacks where you just want "User attacks Target!" In this case just add
"<BattleLogType: ATTACK>"

``<AntiFail>`` Some skills do things other than heal or harm a friend or
foe, but RPG Maker MV might still show a "It had no effect" message.
This disables that.

``<HideInMenu>`` Self-Explanatory. Hides it from the skill equip menu.
Use this for your Basic Attacks and Follow-Ups.

``<Enemy or Actor Select>`` The emotion skills, Sad Poem, Pep Talk,
Annoy, and Massage, can be used on both friends and foes. This is
achieved with this Notetag.

Action Sequence Notetags
^^^^^^^^^^^^^^^^^^^^^^^^

These notetags can be added to skills to add extra flairs to the skill
in the Notes Coding. All of these must be placed before and after their
contained code, with the closing version having a / in front of the name
like this </Target Action>

``<Setup Action>`` The earliest of the 4. This happens before any juice
is consumed, so things like User animations and other "setup actions"
will usually occur here.

``<Whole Action>`` This occurs right before the main action, and applies
its effects to all targets simultaneously. However, it does this in a
bit of an odd way. It calculates the action for one target, and then
dupes the results onto everyone else. This can cause some issues for
effects that are based on target-by-target variables like their level of
buff or debuff.

``<Target Action>`` In my opinion, the better Whole Action. Occurs
exactly as the main action effect will occur, and works its effects on
each target individually. So things like attack animations and state
changes should occur here. However unlike Whole Action, you can visually
seMake sure that if you use Target Action, you must define when the
skill's main action occurs. This is done with the line "action effect,"
which can be placed multiple times if you want the move to activate
multiple times, like Red Hands.

``<Follow/Finish Action>`` Two rarely used aftermath sections. These are
used for times where a closing action needs to occur that isn't part of
the target action. I don't know the difference between Follow and Finish
but Finish comes after Follow if both are used.

Action Sequences
^^^^^^^^^^^^^^^^

NOTE: Y in all of these contexts is what the action is targeting. This
can be filled in with a frankly overwhelming amount of options. The
important ones are user, target, actors, and enemies. These should
hopefully be self-explanatory. Once again, Yanfly's page for the plugin
lists all your options.

``add state x:`` y Adds the specified state to the target.

``remove state x:`` y Adds the specified state from the target.

``animation x: y`` Plays the specified animation. Y is where the
animation will play.

``wait for animation`` Waits for all animations to end before
proceeding. Can sometimes be a bit buggy.

wa\ ``it: #`` Waits the set number of frames before continuing. RPG
Maker MV runs at 60fps, so wait: 60 will wait for one second.

``HP ± x: y(, show)`` Adds or subtracts the specified heart from the
target. If show is placed after the target, the damage popup will be
displayed. Percentages may be used.

``MP ± x: y(, show)`` Adds or subtracts the specified juice from the
target. If show is placed after the target, the damage popup will be
displayed. Percentages may be used.

Text Notetag
^^^^^^^^^^^^

The "eval:" notetag can be added to skills to execute JavaScript, but it
is mainly used in OMORI to display text. Like this:

:literal:`eval: BattleManager._logWindow.push("addText", \`${user.name()} hypes up ${target.name()}!\`)`

This is a line from a mod I'm working on, but that's not important. What
is important is that this is all you need to display detailed text in
OMORI's battle box. The red text is what's actually shown in game, with
the user and target name's being self-explanatory. Since it's part of
the Notes coding, you can determine when in the skill it plays, and have
if and then statements change the line used. It's rather versatile and
simple.

Eval Notetags
^^^^^^^^^^^^^

These are some other Notetag Headers that can be added to Skills. Unlike
the Action Sequences, these use pure JavaScript, so be aware of that.

``<Custom Requirement>`` This sets any extra requirements for a skill to
be usable. This does NOT prevent the player from selecting it, but will
stop the skill's execution during their turn. This is done by the
boolean "value" that determines if a skill can be performed or not. This
is mainly used for Follow-Ups, which check if the recipient is dead.

Follow-Ups
~~~~~~~~~~

Follow-Ups, as to be expected, work quite differently from all the other
skills in OMORI. This will explain how to set them up.

All Tiers Of The Follow-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^

In OMORI, your follow-ups get stronger after hitting specific story
beats. These upgrades to your follow-ups are separate skills in the
Database, and as such you need to have a "Pre-Skill" that checks what
skill should be used, and then activates that skill. In OMORI, these are
called Checks.

Before the Checks actually determine what skill to use, they have a
<Custom Requirement> notetag that checks to see if the party members
involved in the follow-up are dead. This will lock the skill if they are
dead. You can just copy paste that requirement from a pre-existing
check.

Now for the actual Check. This is done by activating a Common Event from
the Effect section. This Common Event will then go through an if-else
chain to see if the player has met the story beat needed for a specific
tier, if they have, it uses the Force Action event on the Party Member
to use the actual Follow-Up on the Last Target. It roughly looks like,

If : StoryBeat2 is on

Force Action : Basil, Vent 3, Last Target

jump to label: stop

  end

Else :

If : StoryBeat1 is on

Force Action : Basil, Vent 2, Last Target

jump to label: stop

  end

Else:

Force Action : Basil, Vent 1, Last Target

end

label : stop

However, if your follow-ups don't get stronger over time (for example
Basil in the console version, due to only being accessible on One Day
Left, after both story beats) then you don't need these Checks.

Attaching The Follow-Ups To Your Attacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we're done with the annoying and tedious part. The rest is easy.

To attach your follow-ups, you have to add this Notetag to your basic
attack for all 3 follow-ups it has.

``<ChainSkill: #, direction>`` The # gets replaced with the ID of the
Check, not any of the actual Follow-Ups. The direction is what arrow key
has to be pressed to activate the Follow-up. up, down, left, and right.

Follow-Up Notetags
^^^^^^^^^^^^^^^^^^

``<ChainSkillIcon: #>`` This determines what image to use for the
Follow-Up bubble. You can see them in img/system/ACS_Bubble.png. If
you're adding new Follow-Ups, refer to the `Sprites &
Art <https://docs.google.com/document/d/1t59hzeERvwok2ZsQVs6AgFj5WVZdeAPwiWYFgkDGLiE/edit?tab=t.0#heading=h.gsbdya7y8lgi>`__
page for adding new Follow-Up bubbles. What I didn't mention there is
how they are indexed. It's the same as most images in OMORI, starting at
0, left-to-right, top-to-bottom.

``<ChainSkill[Name of a followup]>`` I don't know what exactly these do,
but I recommend just setting them to the Follow-Up that uses that slot
normally. So for example, Basil's comfort follow-up is his down
follow-up, and he takes Kel's place in the battle menu, so I'd set
Comfort to <ChainSkillPassToOmori>

``<EnergyCost: #>`` Self Explanatory. All but Release Energy cost 3
energy, with Release energy costing 10, but you can set them all to
whatever you like(Within reason. I don't know what would happen if you
set one to 0 or anything above 10, probably works as expected, but just
be ready if something goes wrong).

| 
| ``<HideInMenu>`` Not Follow-Up specific but make sure they don't show
  in the skill menu.
