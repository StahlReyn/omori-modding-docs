Decryption and Playtest Generation
==================================

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
   :alt: modsettings

   modsettings

Here we are focusing on the "Decrypt" label. Here is an explanation of
what everything here does:

``Decryption Mode``- Decides what the game will decrypt. "Everything"
decrypts the base game with mods, "Base Game" only decrypts the vanilla
assets, and "Only Mods" decrypts only the currently enabled mods.

``Generate as Rpgmaker project?``- Decides whether or not an Rpgmaker
project file will be generated. Unless you're only doing basic asset
editing, you will want to select "Yes" on this.

``Start decryption``- Clicking the button will start game decryption
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
