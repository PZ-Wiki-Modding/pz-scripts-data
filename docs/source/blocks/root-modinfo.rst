.. _root-modinfo:

ROOT-ModInfo
============

The mod.info file, which contains all the information about a mod.


Hierarchy
---------

This block does not require a parent block.


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _name:

**name**
   Type: ``string``

   The name of the mod. A translation can be provided in the `Mod.json translation file <https://pzwiki.net/wiki/Translation>`_.

.. _description:

**description**
   Type: ``string``

   A description of the mod. The description supports `rich text tags <https://pzwiki.net/wiki/ISRichTextPanel>`_. A translation can be provided in the `Mod.json translation file <https://pzwiki.net/wiki/Translation>`_.

.. _id:

**id**
   Type: ``string``

   The unique identifier of the mod.

.. _author:

**author**
   Type: ``string``

   The author of the mod. Multiple authors are often separated by commas but no convention exists.

.. _poster:

**poster**
   Type: ``string``

   The relative path to the mod's poster image. The image should be placed in the same folder as the mod's .mod file.

