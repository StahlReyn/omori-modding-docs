Decrypting Game
===============

*Omori's assets are decrypted by default, making them impossible to
modify. The mod community has created tools to decrypt those assets and
allow for modification.*

The first step to decrypting the game is to make sure you have
`Oneloader <https://github.com/rphsoftware/OneLoader/releases>`__
installed on your copy of the game.

Open the game and go to the options menu. You should see a new tab
labeled "Mods". An image showing the tab is seen below.

.. figure::
   https://user-images.githubusercontent.com/87251065/217338415-9b251b6d-bcf1-4eb2-91ea-40d8337985b6.PNG
   :alt: Mod Settings
   :align: center
   :width: 400px
   
   Mod Settings

Here we are focusing on the "Decrypt" label. Here is an explanation of
what everything here does:

``Decryption Mode`` - Decides what the game will decrypt. "Everything"
decrypts the base game with mods, "Base Game" only decrypts the vanilla
assets, and "Only Mods" decrypts only the currently enabled mods.

``Generate as Rpgmaker project?`` - Decides whether or not an Rpgmaker
project file will be generated. Unless you're only doing basic asset
editing, you will want to select "Yes" on this.

``Start decryption`` - Clicking the button will start game decryption
with the settings. It may take a while, so be patient! Progress is shown
on a blue bar at the top of the screen. The decrypted assets will be in
the OMORI game folder, under a new folder named "www_playtest_xxxxxx" or
"www_decrypt_xxxxxx", depending on whether or not you chose to generate
an RPG Maker project file.

Opening the Game in RPG Maker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Opening the game in RPG Maker MV is as simple as opening the project
file found in the "www_playtest_xxxxxx" folder through the application.
The project can be playtested normally, by clicking the green play
button at the top.

Resetting Installation
^^^^^^^^^^^^^^^^^^^^^^

.. warning::

   This might override (delete) mod files, so make sure you back up files
   you want to keep.

If you broke your installation of OMORI (meaning it doesn't work
properly or at all), then you can fix your installation using Steam.

Save files should not be affected, but they might become unusable if
they require a specific mod.

Here's how to fix your installation:

1. Open Steam
2. Right-click OMORI and choose *Properties*
3. On the tabs on the left, click *Local files*
4. Click *Verify integrity of game files…* This will make Steam check
   the files and cue an update to download fresh files from it's server
   if needed.

Dev Tools
^^^^^^^^^

.. warning::

   This guide assumes that you are already familiar with OMORI mod
   development, and that you know where some files need to go. You should
   also already know how to fix your OMORI installation, in case you break it.

   Furthermore, some mods might not work in SDK mode.\ [1]_

To get `dev tools <https://flaviocopes.com/browser-dev-tools>`__ in
OMORI, which can be very helpful in debugging your mod, you need to do a
few steps:

1. Download the SDK edition of the exact same NW.js version that OMORI
   is using. For OMORI v1.0.8 it is `nwjs-sdk-v0.29.0-win-x64.zip <https://dl.nwjs.io/v0.29.0>`__

2. Drag all your files into the OMORI folder and choose replace /
   overwrite

3. Add this code to *www/js/main.js* to disable SDK mode protection:

   .. code:: javascript

      window.navigator.plugins.namedItem = function() {
          return null;
      }

4. Rename OMORI.exe to something else, like OMORI_old.exe, and rename
   the new file nw.exe to OMORI.exe

5. Launch the game and press *F12* to open the dev tools.

.. [1]
   *For example,* `Painful Bossrush <https://mods.one/mod/painrush>`__
   *will check for SDK mode and stop working if detected.*
