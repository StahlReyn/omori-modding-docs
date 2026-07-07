Quests
======

About setting up quests. Omori uses custom plugins to make quests.

Important Common Events
-----------------------

Many of the event dependent on **Variable 16** which is grabbed as **event ID**

47: ★ Display New Quest
   Displays the "lightbulb" bubble that shows the quest is new.

   Alternative: ``this.setEventIcon(eventid, 'quest', index);``

48: ★ Display Ongoing Quest
   Displays the "..." bubble that shows the quest is ongoing.

49: ★ Display Quest Finish
   Displays the "lightbulb" bubble that shows the quest is completable.
   When the quest is finished the buubble is erased, so this is specifically
   when the condition is satisfied.

50: ★ Erase Bubble
   Erases the bubble of event ID

300: -- Quest Accept
   Plays Sound: ``SYS_quest_get``

301: -- Quest Complete
   Plays Sound: ``SYS_quest_complete``


Example - LEAFY's Quest
-----------------------

For bubble, set the Variable 16 "Quest Balloon ID" to the event ID that
you want the bubble to be over.

Example used here is LEAFY's Quest in Map 105 - TRAIN STATION WAITING
AREA, Event 5 at 14,38. The event has ID of 5, so the variable is set to
5 accordingly to be used in other Event

The starting events of LEAFY's Quest

- \ **Control Switches : #1661:**\  Any switch to keep track for using
  in other events
- \ **Control Variables : #16:**\  to set Event ID, in this case LEAFY
  event is 5. (Technically redundant here as it's set already before at
  start, but for good measure.)
- \ **Common Event : - Quest Accept:**\  Plays Quest accept sound
- \ **Common Event : ★ Display Quest Finish:**\  Quest is finished, in
  this case it's in case player already has slain 5 bunnies before
  interacting with LEAFY.
- \ **Common Event : ★ Display Ongoing Quest:**\  Quest is Ongoing, the
  usual if the player has not finished yet, so therefore quest is still
  going on
- \ **Control Self Switch : A:**\  To toggle own event to another page,
  which in LEAFY's case cuts off intro and throws to more quest loop to
  kill more bunnies.
