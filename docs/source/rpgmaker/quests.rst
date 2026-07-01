Quests
======

Important Common Events
-----------------------

Many of the event dependent on \ **Variable 16**\  which is grabbed as
**event ID**

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="81">

ID

.. raw:: html

   </th>

.. raw:: html

   <th width="174">

Name

.. raw:: html

   </th>

.. raw:: html

   <th width="349">

Note

.. raw:: html

   </th>

.. raw:: html

   <th>

Uses

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

47

.. raw:: html

   </td>

.. raw:: html

   <td>

★ Display New Quest

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <p>

Displays the Lightbulb bubble that shows the quest is still Finished.

.. raw:: html

   </p>

.. raw:: html

   <p>

Alternative: this.setEventIcon(eventid, 'quest', index);

.. raw:: html

   </p>

.. raw:: html

   </td>

.. raw:: html

   <td>

Var 17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

48

.. raw:: html

   </td>

.. raw:: html

   <td>

★ Display Ongoing Quest

.. raw:: html

   </td>

.. raw:: html

   <td>

Displays the Lightbulb bubble that shows the quest is still Ongoing.

.. raw:: html

   </td>

.. raw:: html

   <td>

Var 17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

49

.. raw:: html

   </td>

.. raw:: html

   <td>

★ Display Quest Finish

.. raw:: html

   </td>

.. raw:: html

   <td>

Displays the Lightbulb bubble that shows the quest is still Finished.

.. raw:: html

   </td>

.. raw:: html

   <td>

Var 17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

50

.. raw:: html

   </td>

.. raw:: html

   <td>

★ Erase Bubble

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

Var 17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

300

.. raw:: html

   </td>

.. raw:: html

   <td>

– Quest Accept

.. raw:: html

   </td>

.. raw:: html

   <td>

Plays Sound: SYS_quest_get

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

301

.. raw:: html

   </td>

.. raw:: html

   <td>

– Quest Complete

.. raw:: html

   </td>

.. raw:: html

   <td>

Plays Sound: SYS_quest_complete

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

Example - LEAFY's Quest
-----------------------

For bubble, set the Variable 16 "Quest Balloon ID" to the event ID that
you want the bubble to be over.

Example used here is LEAFY's Quest in Map 105 – TRAIN STATION WAITING
AREA, Event 5 at 14,38. The event has ID of 5, so the variable is set to
5 accordingly to be used in other Event

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

The starting events of LEAFY's Quest

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

- \ **Control Variables : #16:**\  to set Event ID, in this case LEAFY
  event is 5.
- \ **Common Event : ★ Erase Bubble:**\  Removes existing bubble on
  event of \ **Variable 16**\ , like cleaning up before doing other
  bubbles.

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

LEAFY's Initial quest Accept later on.

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

- \ **Control Switches : #1661:**\  Any switch to keep track for using
  in other events
- \ **Control Variables : #16:**\  to set Event ID, in this case LEAFY
  event is 5. (Technically redundant here as it's set already before at
  start, but for good measure.)
- \ **Common Event : – Quest Accept:**\  Plays Quest accept sound
- \ **Common Event : ★ Display Quest Finish:**\  Quest is finished, in
  this case it's in case player already has slain 5 bunnies before
  interacting with LEAFY.
- \ **Common Event : ★ Display Ongoing Quest:**\  Quest is Ongoing, the
  usual if the player has not finished yet, so therefore quest is still
  going on
- \ **Control Self Switch : A:**\  To toggle own event to another page,
  which in LEAFY's case cuts off intro and throws to more quest loop to
  kill more bunnies.
