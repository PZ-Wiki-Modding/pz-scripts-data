.. _root-mapinfo:

ROOT-MapInfo
============

The ``map.info`` file is used to define the map's information. It is used by the game to display the map in the map selection screen and to load the map into the world.
It needs to be located in:

.. code-block::

   📁 media
       📁maps
           📁 <map folder>
               📄 map.info


Hierarchy
---------

This block does not require a parent block.


ID Properties
-------------

This block should not have an ID.


Parameters
----------

.. _title:

**title**
   Type: ``Any``

   Title of the map.

.. _description:

**description**
   Type: ``Any``

   Description of the map.

.. _lots:

**lots**
   Type: ``Any``

   Refers to the world map the map will be loaded into. For a map which is inside the vanilla world map, use ``lots=Muldraugh, KY``.

.. _fixed2x:

**fixed2x**
   Type: ``Any``

   Boolean which fixes rendering issues. Leave it as ``true`` if you are not sure.

.. _zoomx:

**zoomX**
   Type: ``Any``

   Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.

.. _zoomy:

**zoomY**
   Type: ``Any``

   Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.

.. _zooms:

**zoomS**
   Type: ``Any``

   Zoom parameter used to define the position of the camera on the world map when chosing the map to spawn in.

.. _demovideo:

**demoVideo**
   Type: ``Any``

   `Video file <https://pzwiki.net/wiki/File_formats#Video_format>`_ used to showcase the map when selecting it.

