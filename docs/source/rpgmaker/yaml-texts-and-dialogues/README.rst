YAML Texts and Dialogues
========================

Omori uses YAML files for displaying majority of texts seen in game.

.. raw:: html

   <table data-view="cards">

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th>

.. raw:: html

   </th>

.. raw:: html

   <th>

.. raw:: html

   </th>

.. raw:: html

   <th>

.. raw:: html

   </th>

.. raw:: html

   <th data-hidden data-card-target data-type="content-ref">

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

Text Codes

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

text-codes.md

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Omori Color Convention

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

omori-text-color-convention.md

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   </td>

.. raw:: html

   <td>

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

Displaying Messages in RPGMV
----------------------------

Display Basic Message
~~~~~~~~~~~~~~~~~~~~~

To display a message, create a Plugin Command block and enter the
following:

{% code title=“Show Message Format” %}

::

   ShowMessage fileName.messageName

{% endcode %}

.. raw:: html

   <details>

.. raw:: html

   <summary>

Example Code

.. raw:: html

   </summary>

{% code title=“Example” %}

::

   ShowMessage 14_cutscenes_sweetheartquest.message_37

{% endcode %}

.. raw:: html

   </details>

{% hint style=“info” %} Despite Omori dialogue almost always using the
``message_x`` naming convention, other name can be given as well. {%
endhint %}

Display Choices
~~~~~~~~~~~~~~~

TBA: To display a choice

::

   AddChoice message label
   ShowChoices number

.. raw:: html

   <figure>

.. raw:: html

   <figcaption>

.. raw:: html

   <p>

Example in RPG Maker MV Event Screen

.. raw:: html

   </p>

.. raw:: html

   </figcaption>

.. raw:: html

   </figure>

*TBA: ShowChoices jank with numbers, default selection when pressing
escape*

{% hint style=“info” %} The choice plugin is done in the
``Text_Language_Processor.js`` plugin file made by TDS. {% endhint %}

YAML Formatting
---------------

Names
~~~~~

Omori has main 2 ways of displaying names:

**Shortcut macro:** This is a plugin parameter done in
``YEP_X_MessageMacros1.js`` plugin, that is replaced with the name.

{% hint style=“info” %} Benefit with shortening names of reoccurring
characters and also ease of potentially mass-changing names later. {%
endhint %}

**Direct name:** Add ``\n<NAME>`` directly on the text field

{% hint style=“info” %} Benefit of being easy to implement, increases
readability from being direct, and good for one off side characters. {%
endhint %}

Dialogue only
~~~~~~~~~~~~~

{% code title=“Dialogue only example” %}

.. code:: yaml

   message_0:
       text: \n<HUMPHREY>I fucking love air-conditioning.

{% endcode %}

Dialogue with Portrait
~~~~~~~~~~~~~~~~~~~~~~

Dialogue with portraits are done with main characters in Omori. 

``faceset:`` Image file name (without file extension, case sensitive)

``faceindex:`` The target image in the 106x106 grid, counting from top
left as 0.

``text:`` The text displayed

{% code title=“Dialogue with Portrait Exampleeee” %}

.. code:: yaml

   message_2:
         faceset: MainCharacter_Basil
         faceindex: 0
         text: Hope you don't mind the photo.\bas

{% endcode %}

{% hint style=“info” %} In this case ``\bas`` is a shorthand command to
show BASIL name, which is hard coded. This is the case for most primary
characters as well. This is part of text codes. {% endhint %}

Battle Dialogue
~~~~~~~~~~~~~~~

Battle dialogue tends to have the character name inside the text box
itself due to smaller size. This can be done with ``>`` with newline of
``\>NAME: \<`` at the start.

{% code title=“Battle Dialogue Example” %}

.. code:: yaml

   message_141:
      text: >
       \>PERFECTHEART: \<I said that you would regret this, children.

{% endcode %}
