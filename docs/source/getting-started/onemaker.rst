OneMaker
=====================

OneMaker is a project that adds UI modifications to RPG Maker MV,
bringing its functionality to the level of which was used during OMORI
development.

Features:

- Resizable window sizes, such as the Database and Event Viewer.
- Event Page Conditions now have variable operator selection, Self
  Variables, and Self Switches E-Z are available.
- Conditional Branches can now use check Self Variables, you also get
  access to Control Self Variable event commands.
- Map image files in the ``render`` folder will now automatically be
  displayed onto maps, using a stretch format so they don't have to be
  resized to match MV's 48x48 tile sizes.
- Event Block Selection screen can be made into one giant tab instead of
  having three tabs.
- The Show Text command is now formatted correctly to fit OMORI's face
  images. Comments and Script Commands can now have way more lines.

:samp:

Installation
-------------------------------

To start installation, you will want to download this:

- On Windows: `Download
  Here <https://github.com/FoGsesipod/OneMaker-MV/releases/download/1.2.2/Installer.7z>`__
  (Extract the zip and run the .bat file)
- On Linux (Or just manually): `Download
  Here <https://github.com/FoGsesipod/OneMaker-MV/releases/download/1.2.2/OneMaker-MV.zip>`__
  (Extract the zip, then copy the contents to ``steam/steamapps/common/RPGMaker MV/``)

You may need to disable antivirus if you are choosing to run the .bat.
Do not worry, as this is a safe file developed by a trusted source.

Some features are disabled until a compatibility plugin is added to the
Plugin Manager ("puzzle" icon in the top bar.) `Download
this, <https://github.com/FoGsesipod/OneMaker-MV/releases/download/1.2.2/Plugins.7z>`__
and then extract the zip. Copy the js plugin into the ``js/plugins/``
folder, and add it through the plugin manager at the top.

The github for the project can be found here:
https://github.com/FoGsesipod/OneMaker-MV

 
Visible Tiled Maps in RPG Maker
-------------------------------

.. note::

  This may have some issues with newer versions of Tiled. 
  It is recommended to use 1.0.3.

By default, tiled maps will not show in RPG Maker. However, OneMaker has
functionality that allows them to be visible in game without the use of
parallaxes.

Download the file here:
- `Link <https://github.com/rphsoftware/omori-map-preview-renderer/releases/download/0.1.0/OmoriMapRenderer_win64.exe>`__
  (Windows)
- `Link <https://github.com/rphsoftware/omori-map-preview-renderer/releases/download/0.1.0/OmoriMapRenderer_linux>`__
  (Linux)

You will want to put it into your playtest folder as shown, and then run it.

:samp:

You can use a checkbox in the map options of OneMaker to disable or
enable tiled map viewing.
