Packaging Mods
==============

*Omori mods must be in a specific folder/zip format in order to properly
run.*

Using Bundletool
----------------

{% embed url="https://mods.one/mod/bt" %} Link to BundleTool on mods.one
{% endembed %}

After editing the game's data and assets from the "www_decrypt_xxxxxx"
or "www_playtest_xxxxxx" folder, you can package your mod into a zip for
use by running `Bundletool <https://mods.one/mod/bt>`__. It is installed
the same way other mods are installed. After installing, run the game
and follow the on-screen prompts to properly package your mod.

1. Drag Bundletool zip file to the mods folder, `like how you install
   mods. <../installing-mods.md>`__
2. Run OMORI; Click "Use BundleTool"
3. Select folder of the mod you want to package. This is likely a folder
   named ``www_decrypt`` or ``www_playtest`` or similar
4. Enter mod details. Mod ID should ideally align with the mod ID you
   are going to upload in mods.one.
5. Select the files need changing. (Tip: Pressing the top header will
   select all for that category)

   1. **Ignore** means don't include the file in the package. This can
      be used to ignore some plugins only used in testing and don't want
      to appear in final product. For example: console, quick save and
      load, or better saves.
   2. **Delta** means only includes the changes, and does not replace
      it. This is good for compatibility, especially if the mod only
      changes small amount of things and don't want to replace entire
      file (which would break compatibility). For example, small single
      changes to some Skills in ``skills.json``, as you don't need to
      replace everything, just change only one specific thing.
   3. **Include** means add the file to the package, this totally
      replaces the files. This is commonly for audio and image files, as
      delta can potentially cause strange changes.
   4. **Unique Name** is specific to plugins. It makes it so when
      multiple mods has the same plugin added or changed, it will simply
      make two of them for each mod and will not override the file
      entirely. As of current it may run into some bugs so it may be
      better avoided. [NEEDS CHECKING]

6. Wait for the bundle process to finish. This can take a few minutes
   especially for bigger mods.
7. Select the location for where the final export will be.
8. You're finished!

Delta or Include?
-----------------

Sometime it gets confusing whether to do Delta or full Include. Here's a
common rough use case for these, though this is a rough guideline, not
strictly a rule.

**Key: **\ \ **Red - Avoid;**\  \ **Orange - Depends;**\  \ **Green -
Likely**\ 

.. raw:: html

   <table>

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th width="132">

Type

.. raw:: html

   </th>

.. raw:: html

   <th width="305">

Delta / Unique Name

.. raw:: html

   </th>

.. raw:: html

   <th>

Include

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

Audio

.. raw:: html

   </td>

.. raw:: html

   <td>

Rarely needed / Prone to breaking

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely to be full include than delta, due to tendency to break.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Data

.. raw:: html

   </td>

.. raw:: html

   <td>

This is better for smaller mods. Small edits to database in RPGMV, such
as skills or items. This is good for mods that only change a few things
like singular skill balance change, or a new item.

.. raw:: html

   </td>

.. raw:: html

   <td>

This is safer bet for larger mods that may edit many things, especially
if it interacts between each other a lot.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Fonts

.. raw:: html

   </td>

.. raw:: html

   <td>

This could potentially be used in language mods that requires original
Omori font to be altered to include special character.

.. raw:: html

   </td>

.. raw:: html

   <td>

If font is being changed at all, it's likely full include.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Icon

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely won't appear in most mod as it remains unchanged.

.. raw:: html

   </td>

.. raw:: html

   <td>

If icon is being changed at all, it's likely full include.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Image (img)

.. raw:: html

   </td>

.. raw:: html

   <td>

Small edits to images. This is likely additional changes on top of pixel
sprites or portraits. For example: - Shiba Kel (edits only hoodie on
Kel)- Girlmori (edits pigtail on Omori portraits)

.. raw:: html

   </td>

.. raw:: html

   <td>

Safer to use full include than delta, due to tendency to break or
unintended changes.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Languages

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely won't appear in most mod as it remains unchanged.

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely won't appear in most mod as it remains unchanged.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Maps

.. raw:: html

   </td>

.. raw:: html

   <td>

Small edits to maps. Should ideally keep same Tiled versions unless you
have Tiled compatibility.

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely to be full include than delta, due to tendency to break.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Movies

.. raw:: html

   </td>

.. raw:: html

   <td>

Rarely needed / Prone to breaking

.. raw:: html

   </td>

.. raw:: html

   <td>

Likely to be full include than delta, due to nature of video files.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Plugins

.. raw:: html

   </td>

.. raw:: html

   <td>

Dependent on context, is prone to bugs currently.

.. raw:: html

   </td>

.. raw:: html

   <td>

Plugins you are sure you need to totally override, or totally new made
up specific for the mod.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

For **Plugins**, you may want to **ignore** some plugins used only in
testing the mod. Some common ones are:

- `Quick Load <https://mods.one/mod/quickload>`__ - Called
  ``VykosX-QuickLoadOnStart`` which is sometime used to playtest fast,
  skipping the menu startup intro
- `Console <https://mods.one/mod/console>`__ - Adds a plugin called
  ``console``
- `Better Save and Load <https://mods.one/mod/saveloadplus>`__ - Which
  alters ``Omori Save & Load`` plugin

Bundletool Screen Examples
--------------------------

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   The start up screen; click "use Bundletool"

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   The prompt for finding www_playtest folder

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

.. container::

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Mod detail prompt

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>

   .. raw:: html

      <figure>

   .. raw:: html

      <figcaption>

   .. raw:: html

      <p>

   Example of selecting changes, using Reverie as example. In this case
   all files are included for change.

   .. raw:: html

      </p>

   .. raw:: html

      </figcaption>

   .. raw:: html

      </figure>
