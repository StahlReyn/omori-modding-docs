Text Codes
==========

RPG Maker MV Text Codes
-----------------------

RPG Maker MV comes with text codes on it’s own, being the following:

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="108">

Code

.. raw:: html

   </th>

.. raw:: html

   <th>

Function

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

:raw-latex:`\V[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Will be replaced with the value of the nth variable.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\N[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Will be replaced with the name of the nth actor.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\P`[n]

.. raw:: html

   </td>

.. raw:: html

   <td>

Will be replaced by the name of the nth (arranged order) party member.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\G<`/td>

.. raw:: html

   <td>

Will be replaced by the currency unit.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\C[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Draw the subsequent text in the nth color. Text color conforms to the
contents of the [Window.png] system image.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\I[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Draws the nth icon.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{

.. raw:: html

   </td>

.. raw:: html

   <td>

Increases the text by 1 step.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

}

.. raw:: html

   </td>

.. raw:: html

   <td>

Decreases the text by 1 step.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

\\

.. raw:: html

   </td>

.. raw:: html

   <td>

Replaced with the backslash character.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

$

.. raw:: html

   </td>

.. raw:: html

   <td>

Open the gold window.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.

.. raw:: html

   </td>

.. raw:: html

   <td>

Wait for 1/4 second.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

\|

.. raw:: html

   </td>

.. raw:: html

   <td>

Wait for 1 second.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

!

.. raw:: html

   </td>

.. raw:: html

   <td>

Wait for button input.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

>

.. raw:: html

   </td>

.. raw:: html

   <td>

Display remaining text on same line all at once.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

&#x3C;

.. raw:: html

   </td>

.. raw:: html

   <td>

Cancel the effect that displays text all at once.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

^

.. raw:: html

   </td>

.. raw:: html

   <td>

Do not wait for input after displaying the next.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

*Credit: Yanfly.moe Wiki*

{% hint style=“info” %} Beware of the slashes! Text code uses
backslashes (\\) not normal slashes (/). {% endhint %}

TDS Text Effects
----------------

The following contains code related to text movements used in Omori.

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="154.5">

Code

.. raw:: html

   </th>

.. raw:: html

   <th>

Function

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

:raw-latex:`\SINV[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Makes the text shake vertically. When n is:0 - Disable1 - Normal wave2 -
Dense wave

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\SINH[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Makes the text shake horizontally. When n is:0 - Disable1 - Enable

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\QUAKE[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Makes the text wobble aggressively. When n is:0 - Disable1 - Intense
quake2 - Softer quake

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

:raw-latex:`\RAINBOW[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Adds an animated rainbow effect to the text. When n is:0 - Disable1 -
Enable

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Archeia Text Codes
------------------

In the following the most used are common event text code. For example,
to call shake screen common event. There are other codes but it isn’t
used at all in Omori

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="177">

Code

.. raw:: html

   </th>

.. raw:: html

   <th>

Function

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

:raw-latex:`\com[n]`

.. raw:: html

   </td>

.. raw:: html

   <td>

Invokes the common event of ID n

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

{% hint style=“info” %} Fun fact: Text Codes can be invoked when set as
character name and the name is trying to be called. {% endhint %}

Useful Resources
----------------

- http://www.yanfly.moe/wiki/Category:Text_Codes_(MV)
- https://github.com/Gilbert142/gomori/wiki/Text-Formatting
