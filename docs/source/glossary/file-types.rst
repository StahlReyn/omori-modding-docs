File Types
==========

.. |bdg-none| replace:: :bdg-muted:`None`
.. |bdg-patch| replace:: :bdg-link-primary-line:`patching <https://omori.wiki.mods.one/modding:patching>`
.. |bdg-delta| replace:: :bdg-link-primary-line:`delta patching <https://omori.wiki.mods.one/modding:file-types#jsond_-_json_patch_files>`
.. |bdg-img-delta| replace:: :bdg-link-primary-line:`image delta <https://omori.wiki.mods.one/modding:replacing_images#image_deltas>`
.. |bdg-yaml-delta| replace:: :bdg-link-primary-line:`.yamld delta <https://omori.wiki.mods.one/modding:file-types#yamld_-_yaml_patch_files>`


When modding OMORI, you'll encounter different file types. This page
aims to explain the
`decrypted <https://omori.wiki.mods.one/modding:getting_started#decrypting_the_game>`__
files, and the file types you can use to modify the game, which are not
the same.


Common file types 
------------------

These file types are commonly used by OMORI and you'll encounter these
when
`decrypting <https://omori.wiki.mods.one/modding:getting_started#decrypting_the_game>`__
the game.

.. glossary::
    .js
        :Encrypted: ``.OMORI``
        :Patching: not directly (read on)
        :Description: 
            OMORI uses
            `JavaScript (JS) <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript>`__
            files for its game logic. See: :ref:`js-patch`

            Generally, js are not patched directly, but rather comes in 
            different load order. How patching works for most JS plugins are
            by defining the function in later loads.

    .json
        :Encrypted: ``.KEL``
        :Patching: |bdg-patch| |bdg-delta|
        :Description: 
            `JavaScript Object Notation (JSON) <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON>`__
            files only hold data, no JavaScript logic. They are used by the game to
            store enemy descriptions, or events. They might contain data that gets
            interpreted by the game as if it was game logic.

            JSON files are very easy to work with in JavaScript, because all data
            types supported by JSON can be mapped 1-to-1 into a JavaScript object or
            array. It's worth mentioning that JSON doesn't support all types that a
            JS object does, like functions.

    .png
        :Encrypted: ``.rpgmvp``
        :Patching: |bdg-patch| |bdg-img-delta|
        :Description:
            PNG files are image files that support transparency. This is how the
            game stores all common images.

    .yaml
        :Encrypted: ``.HERO``
        :Patching: |bdg-patch| |bdg-yaml-delta|
        :Description:
            `YAML Ain't Markup Language (YAML) <https://www.tutorialspoint.com/yaml/yaml_introduction.htm>`__
            files are similar to *.json* files, in that they hold the same data
            types, like strings, numbers, objects etc. 
            
            The two big differences
            regarding OMORI is that YAML files have a different, more human-friendly
            syntax, and they support comments, which JSON files don't. YAML files
            are primarily used for dialogue files found in *\\/languages\\*/, and
            are therefore more comfortable to edit than JSON.

    .yml
        ``.yml`` is a `legacy file extension <https://yaml.org/faq.html>`__, which
        means it used to be used for YAML files, but the official file extension
        today is ``.yaml``. Most programs will still recognise ``.yml`` as a YAML
        file. 
        
        **We recommend using only ``.yaml``** for
        constistency**. You'll encounter ``.yml`` with projects that used files
        decrypted using the `decryptor mod for
        Gomori <https://github.com/toshirodesu/omori_decrypt>`__, which outputs
        files with the *.yml* extension. The built-in
        `decryptor <https://omori.wiki.mods.one/modding:getting_started#decrypting_the_game>`__
        of OneLoader will output the same files with a *.yaml* extension.

        .. seealso::

            Modern extension form :term:`.yaml`

    .ogg
        :Encrypted: ``.rpgmvo``
        :Patching: |bdg-patch|
        :Description:
            *.ogg* files contain compressed audio using the
            `Vorbis <https://en.wikipedia.org/wiki/Vorbis>`__ codec.

            For RPGMaker MV specifically, it also reads the file's metadata
            of fields ``LOOPSTART`` and ``LOOPLENGTH``, measured in samples.

        .. note::
            Games often uses ``.ogg`` files for it's metadata support
            and generally much better audio quality in higher compression
            range compared to ``.mp3``

            It is encouaged to compress your audio files, as it usually is the
            main factor in large game size. 128kbps or 192kbps is generally good enough.

    .webm
        :Encrypted: -
        :Patching: |bdg-patch|
        :Description:
            `WebM <https://en.wikipedia.org/wiki/WebM>`__ files are lossy video
            files encoded using `VP9 <https://en.wikipedia.org/wiki/VP9>`__.

    .ttf
        :Encrypted: -
        :Patching: |bdg-patch|
        :Description:
            These are font files that omori uses. Stands for TrueType Font 
            and is the the most common format for fonts on the classic Mac OS,
            macOS, and Microsoft Windows OS.
    
Delta files 
-----------

Delta files are special file types to modify a game file. 
They are not used by the base
game, only by OMORI mods through the help of OneLoader.

.. glossary::
    .jsond
        JSON Delta.

        Patch only parts of the object contained within a game's JSON file by
        loading a \`.jsond\` file. The syntax to modify JSON objects can be
        found `here <https://jsonpatch.com/>`__. Here's a `JSON patch
        generator <https://extendsclass.com/json-patch.html>`__ which you can
        use to generate patches by supplying the original file, and the state
        after your modifications. We recommend this, because manually writing
        JSON patches is hard.

    .yamld
        YAML Delta.

        You can use *.yamld* files to patch YAML files similar to *.jsond*. You
        might think that the content needs to be the json-patch format, but
        instead with YAML syntax, but this is not the case. Unlike YAML files,
        which naturally contain YAML syntax, *.yamld* files **must contain
        JSON** syntax that matches the json-patch schema, just like \`.jsond\`
        files. *(Todo: add example to illustrate)*

    .olid
        One Loader Image Delta (olid)
        
        Contain patching instructions for PNG files.
        You can find out more on the wiki page about `replacing
        images <https://omori.wiki.mods.one/modding:replacing_images#image_deltas>`__.

Less common file types 
----------------------

.. glossary::
    donottouch.xlxs - language file index table 
        :Encrypted: ``.KEL`` with ``.xlxs``
        :Patching: |bdg-none|
        :Description:
            Not used.

    .so
        TBA

    .lib
        TBA

    .dll
        TBA
        
.. hint::

    You should know that you don't have to keep the same file structure, or
    names, or even contents. You can name your files whatever you want, as
    long as you load them properly through the
    `mod.json <https://omori.wiki.mods.one/modding:mod.json>`__ file. You
    can also have all functions in a single or just a few files, if you
    want.

.. _js-patch:

Javascript Patching
-------------------
The game runs in an environment that combines a conventional browser
with a `Node.js <https://www.educative.io/blog/what-is-nodejs>`__
instance. Because OMORI uses `RPG Maker
MV <https://en.wikipedia.org/wiki/RPG_Maker#RPG_Maker_MV>`__, which
in turn uses `PIXI.js <https://pixijs.com/>`__, you mostly don't need
any HTML or CSS knowledge. We might go into the details of PIXI.js in
relation OMORI in a different wiki entry.

These files can't be
`patched <https://omori.wiki.mods.one/modding:patching>`__, but the
functions they define can usually be just overwritten. This means that
in mods you can, for the most part, just create the same file structure
the game has and modify functions as you need. Just remember that your
code doesn't *replace* the original files, your function definitions
will simply overwrite the previous ones, normally through object
prototype manipulation, which is what the normal game files do as well:

.. code:: javascript

    SomeObject.prototype.function = function() {...}

To summarize, mods may look like they are patching JavaScript files,
because for the most part, you can overwrite the functions as if the
files where able to be patched, but it's an important difference to the
other files, where the mod's file will be loaded instead of the normal
game file (Excluding delta files) and not *in addition to*, as is
with JS files. `More Info on JS in
OMORI <https://omori.wiki.mods.one/modding:file-types#javascript_addendum>`__.