mod.json File
=============

Introduction
------------

The *mod.json* file is the central file that tells mod loaders like
**OneLoader** which files to load, and some data about the mod, like its
name and description. It's vaguely inspired by package.json, but only in
terms of role, and less in terms of content structure.

Structure
---------

To describe the structure of a JSON file for a specific purpose, JSON
schemas are used. You can find the current (at the time of writing) JSON
schema for OneLoader *mod.json* files here:
https://rph.space/oneloader.manifestv1.schema.json

| This schema can be used for validating the structure of a *mod.json*
  file through Node.js, but also through your editor, and to get
  auto-completion (linting/hinting) as well.
| For VSCode (and maybe other editors too), all you need to do is start
  your *mod.json* like this:

::

   {
     "$schema": "https://rph.space/oneloader.manifestv1.schema.json"
   }

Your editor should then download the schema and give you hints about
which fields the JSON file has.

Individual Fields
~~~~~~~~~~~~~~~~~

**manifestVersion**

| Describes which version of OneLoader schema this *mod.json* is
  supposed to be compatible with. If you set the
  *:math:`schema_ field as described above, it's version should match up with this one. This field's purpose is to be able to tell OneLoader which version of the schema it is, since _`\ schema*
  is a special field that shouldn't be processed by code for this kind
  of validation.
| At the time of writing, this value should be *1*.

**id**

The id is a unique identifier for every OMORI mod. It's used by
OneLoader to allow users to prioritize one mod over another mod when
there's a conflict, among other things. It's important that this string
is unique (among the mods on mods.one) for OneLoader to operate properly
with multiple mods.

**name**

The name field is an arbitrary string you can choose that will be
displayed in OneLoader's menu for managing mods. No special care needs
to be taken considering name collisions, but using a proper name will
make it easier for users of your mod :)

**description**

The description is also arbitrary, and will also be displayed in
OneLoader's mod menu.

**version**

The version is also arbitrary, but it's highly recommended to use
something along the lines of "v1.0" for versioning. In software
development, `semver <https://semver.org/>`__ is a popular principle to
use for naming versions.

**files**

The files property is an object of fields that each contain an array of
strings, which represent either individual files, or directories.
