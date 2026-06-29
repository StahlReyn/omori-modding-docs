Dev Tools
=========

**Disclaimer**
--------------

This guide assumes that you are already familiar with OMORI mod
development, and that you know where some files need to go. You should
also already know `how to fix your OMORI
installation <resetting-installation.md>`__, in case you break it.

Furthermore, `some mods might not work in SDK
mode. <#user-content-fn-1>`__\  [1]_

**Installation**
----------------

To get `dev tools <https://flaviocopes.com/browser-dev-tools>`__ in
OMORI, which can be very helpful in debugging your mod, you need to do a
few steps:

1. Download the SDK edition of the exact same NW.js version that OMORI
   is using 

   - For OMORI v1.0.8 -
     `nwjs-sdk-v0.29.0-win-x64.zip <https://dl.nwjs.io/v0.29.0>`__

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
