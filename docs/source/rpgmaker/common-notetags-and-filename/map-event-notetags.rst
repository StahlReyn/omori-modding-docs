Map Event Notetags
==================

Here are some common plugin note tags used in events used in Omori.

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="320">

Command

.. raw:: html

   </th>

.. raw:: html

   <th width="305">

Notes

.. raw:: html

   </th>

.. raw:: html

   <th>

Plugin

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

.. raw:: html

   <pre><code><strong>&#x3C;Hitbox Up: x>
   </strong><strong>&#x3C;Hitbox Left: x>
   </strong><strong>&#x3C;Hitbox Right: x>
   </strong><strong>&#x3C;Hitbox Down: x>
   </strong></code></pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Expand the hitbox upward, left, right, or down by x tiles. If used,
makes the event immobile.Commonly used in teleports and walls

.. raw:: html

   </td>

.. raw:: html

   <td>

Event Hitbox Resize (YEP)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <p>

.. raw:: html

   </p>

.. raw:: html

   <pre><code>&#x3C;Sprite Offset X: +n>
   &#x3C;Sprite Offset X: -n>
   &#x3C;Sprite Offset Y: +n>
   &#x3C;Sprite Offset Y: -n>
   &#x3C;Sprite Offset: +x, +y>
   &#x3C;Sprite Offset: -x, -y>
   </code></pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Offset sprite by n amount of pixels, in x or y direction.

.. raw:: html

   </td>

.. raw:: html

   <td>

Event Sprite Offset (YEP)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <pre><code>&#x3C;Copy Event: Map x, Event y>
   &#x3C;Copy Event: mapId, eventId>
   &#x3C;Copy Event: template>
   </code></pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <p>

Copies event, recommended to read more detail in wiki.

.. raw:: html

   </p>

.. raw:: html

   <p>

Commonly used in enemies.

.. raw:: html

   </p>

.. raw:: html

   </td>

.. raw:: html

   <td>

Event Copier (YEP)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   <p>

.. raw:: html

   </p>

.. raw:: html

   <pre><code>&#x3C;Activation Square: x>
   &#x3C;Activation Radius: x>
   &#x3C;Activation Row: x>
   &#x3C;Activation Column: x>
   </code></pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <p>

Give activation range, activating certain events from a distance.

.. raw:: html

   </p>

.. raw:: html

   <p>

.. raw:: html

   </p>

.. raw:: html

   <p>

Square: x tiles from center in a square shape.

.. raw:: html

   </p>

.. raw:: html

   <p>

Radius: x tiles from center in a diamond shape.Row: Horizontal bar to
whole map, with x thickness.

.. raw:: html

   </p>

.. raw:: html

   <p>

Column: Vertical bar to whole map, with x thickness.

.. raw:: html

   </p>

.. raw:: html

   </td>

.. raw:: html

   <td>

Event Proximity Activate (YEP)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>
