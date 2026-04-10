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

.. _root-mapinfo-demovideo:

**demoVideo** `🔗 <#root-mapinfo-demovideo>`_
   Type: ``Any``

   `Video file <https://pzwiki.net/wiki/File_formats#Video_format>`_ used to showcase the map when selecting it.

.. _root-mapinfo-description:

**description** `🔗 <#root-mapinfo-description>`_
   Type: ``Any``

   Description of the map.

.. _root-mapinfo-fixed2x:

**fixed2x** `🔗 <#root-mapinfo-fixed2x>`_
   Type: ``Any``

   Boolean which fixes rendering issues. Leave it as ``true`` if you are not sure.

.. _root-mapinfo-lots:

**lots** `🔗 <#root-mapinfo-lots>`_
   Type: ``Any``

   Refers to the world map the map will be loaded into. For a map which is inside the vanilla world map, use ``lots=Muldraugh, KY``.

.. _root-mapinfo-title:

**title** `🔗 <#root-mapinfo-title>`_
   Type: ``Any``

   Title of the map.

.. _root-mapinfo-zooms:

**zoomS** `🔗 <#root-mapinfo-zooms>`_
   Type: ``Any``

   Zoom parameter used to define the position of the camera on the world map when chosing the map to spawn in.

.. _root-mapinfo-zoomx:

**zoomX** `🔗 <#root-mapinfo-zoomx>`_
   Type: ``Any``

   Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.

.. _root-mapinfo-zoomy:

**zoomY** `🔗 <#root-mapinfo-zoomy>`_
   Type: ``Any``

   Position parameter used to define the position of the camera on the world map when chosing the map to spawn in.

